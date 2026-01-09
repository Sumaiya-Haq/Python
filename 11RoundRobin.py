import statistics
from collections import deque

class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.start_time = None
        self.completion_time = None
        self.waiting_time = 0
        self.turnaround_time = 0
        self.response_time = None
        self.execution_count = 0

class EnhancedRoundRobin:
    def __init__(self, adjustment_factor=1.5, aging_threshold=3):
        self.adjustment_factor = adjustment_factor
        self.aging_threshold = aging_threshold
        self.context_switches = 0
        self.total_idle_time = 0
        
    def calculate_quantum(self, processes):
        """Calculate time quantum based on median of remaining times"""
        remaining_times = [p.remaining_time for p in processes if p.remaining_time > 0]
        if not remaining_times:
            return 1  # Default quantum
        
        median_time = statistics.median(remaining_times)
        return max(1, int(median_time * self.adjustment_factor))
    
    def classify_process(self, process, quantum):
        """Classify process based on remaining time"""
        if process.remaining_time < quantum / 2:
            return "SHORT"
        elif process.remaining_time > quantum * 2:
            return "LONG"
        else:
            return "MEDIUM"
    
    def schedule(self, processes):
        """Enhanced RR scheduling algorithm"""
        time = 0
        ready_queue = deque()
        completed_processes = []
        process_dict = {p.pid: p for p in processes}
        
        # Sort processes by arrival time
        processes.sort(key=lambda x: x.arrival_time)
        process_index = 0
        
        while len(completed_processes) < len(processes):
            # Add arriving processes to ready queue
            while process_index < len(processes) and processes[process_index].arrival_time <= time:
                ready_queue.append(processes[process_index])
                process_index += 1
            
            if not ready_queue:
                time += 1
                self.total_idle_time += 1
                continue
            
            # Calculate dynamic quantum
            quantum = self.calculate_quantum(list(ready_queue))
            
            # Get next process
            current_process = ready_queue.popleft()
            
            # Record start time if first execution
            if current_process.start_time is None:
                current_process.start_time = time
                current_process.response_time = time - current_process.arrival_time
            
            # Execute process
            execution_time = min(quantum, current_process.remaining_time)
            time += execution_time
            current_process.remaining_time -= execution_time
            current_process.execution_count += 1
            
            # Add arriving processes during execution
            while process_index < len(processes) and processes[process_index].arrival_time <= time:
                ready_queue.append(processes[process_index])
                process_index += 1
            
            # Check if process completed
            if current_process.remaining_time == 0:
                current_process.completion_time = time
                current_process.turnaround_time = current_process.completion_time - current_process.arrival_time
                current_process.waiting_time = current_process.turnaround_time - current_process.burst_time
                completed_processes.append(current_process)
            else:
                # Apply aging - boost priority if waiting too long
                if current_process.execution_count >= self.aging_threshold:
                    # Move to front for next execution
                    ready_queue.appendleft(current_process)
                else:
                    ready_queue.append(current_process)
            
            self.context_switches += 1
        
        return completed_processes

class TraditionalRoundRobin:
    """Traditional RR for comparison"""
    def __init__(self, quantum=4):
        self.quantum = quantum
        self.context_switches = 0
        self.total_idle_time = 0
    
    def schedule(self, processes):
        time = 0
        ready_queue = deque()
        completed_processes = []
        process_dict = {p.pid: p for p in processes}
        
        processes.sort(key=lambda x: x.arrival_time)
        process_index = 0
        
        while len(completed_processes) < len(processes):
            while process_index < len(processes) and processes[process_index].arrival_time <= time:
                ready_queue.append(processes[process_index])
                process_index += 1
            
            if not ready_queue:
                time += 1
                self.total_idle_time += 1
                continue
            
            current_process = ready_queue.popleft()
            
            if current_process.start_time is None:
                current_process.start_time = time
                current_process.response_time = time - current_process.arrival_time
            
            execution_time = min(self.quantum, current_process.remaining_time)
            time += execution_time
            current_process.remaining_time -= execution_time
            
            while process_index < len(processes) and processes[process_index].arrival_time <= time:
                ready_queue.append(processes[process_index])
                process_index += 1
            
            if current_process.remaining_time == 0:
                current_process.completion_time = time
                current_process.turnaround_time = current_process.completion_time - current_process.arrival_time
                current_process.waiting_time = current_process.turnaround_time - current_process.burst_time
                completed_processes.append(current_process)
            else:
                ready_queue.append(current_process)
            
            self.context_switches += 1
        
        return completed_processes

def calculate_metrics(processes, context_switches, total_time, idle_time):
    """Calculate performance metrics"""
    total_turnaround = sum(p.turnaround_time for p in processes)
    total_waiting = sum(p.waiting_time for p in processes)
    total_response = sum(p.response_time for p in processes)
    
    avg_turnaround = total_turnaround / len(processes)
    avg_waiting = total_waiting / len(processes)
    avg_response = total_response / len(processes)
    
    cpu_utilization = ((total_time - idle_time) / total_time) * 100 if total_time > 0 else 0
    throughput = len(processes) / total_time if total_time > 0 else 0
    
    return {
        'avg_turnaround': avg_turnaround,
        'avg_waiting': avg_waiting,
        'avg_response': avg_response,
        'cpu_utilization': cpu_utilization,
        'throughput': throughput,
        'context_switches': context_switches
    }

def generate_test_cases():
    """Generate different test scenarios"""
    test_cases = []
    
    # Test Case 1: Mixed workload
    test_cases.append([
        Process(1, 0, 10),
        Process(2, 0, 5),
        Process(3, 0, 8),
        Process(4, 0, 12),
        Process(5, 0, 6)
    ])
    
    # Test Case 2: Short processes
    test_cases.append([
        Process(1, 0, 3),
        Process(2, 1, 2),
        Process(3, 2, 4),
        Process(4, 3, 1),
        Process(5, 4, 2)
    ])
    
    # Test Case 3: Long processes
    test_cases.append([
        Process(1, 0, 20),
        Process(2, 2, 15),
        Process(3, 4, 25),
        Process(4, 6, 18),
        Process(5, 8, 22)
    ])
    
    # Test Case 4: Bursty arrival
    test_cases.append([
        Process(1, 0, 8),
        Process(2, 0, 6),
        Process(3, 10, 4),
        Process(4, 10, 7),
        Process(5, 20, 5)
    ])
    
    return test_cases

def run_comparison():
    """Compare Enhanced RR with Traditional RR"""
    test_cases = generate_test_cases()
    results = []
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n{'='*60}")
        print(f"Test Case {i}")
        print(f"{'='*60}")
        
        # Reset process states
        processes_enhanced = [Process(p.pid, p.arrival_time, p.burst_time) 
                            for p in test_case]
        processes_traditional = [Process(p.pid, p.arrival_time, p.burst_time) 
                               for p in test_case]
        processes_fixed = [Process(p.pid, p.arrival_time, p.burst_time) 
                         for p in test_case]
        
        # Run Enhanced RR
        enhanced_rr = EnhancedRoundRobin(adjustment_factor=1.5)
        enhanced_result = enhanced_rr.schedule(processes_enhanced)
        total_time = max(p.completion_time for p in enhanced_result)
        enhanced_metrics = calculate_metrics(
            enhanced_result, enhanced_rr.context_switches, 
            total_time, enhanced_rr.total_idle_time
        )
        
        # Run Traditional RR with quantum=4
        traditional_rr = TraditionalRoundRobin(quantum=4)
        traditional_result = traditional_rr.schedule(processes_traditional)
        total_time = max(p.completion_time for p in traditional_result)
        traditional_metrics = calculate_metrics(
            traditional_result, traditional_rr.context_switches,
            total_time, traditional_rr.total_idle_time
        )
        
        # Run Traditional RR with quantum=2 for comparison
        traditional_rr_small = TraditionalRoundRobin(quantum=2)
        traditional_result_small = traditional_rr_small.schedule(processes_fixed)
        total_time = max(p.completion_time for p in traditional_result_small)
        traditional_metrics_small = calculate_metrics(
            traditional_result_small, traditional_rr_small.context_switches,
            total_time, traditional_rr_small.total_idle_time
        )
        
        # Store results
        results.append({
            'test_case': i,
            'enhanced': enhanced_metrics,
            'traditional_quantum_4': traditional_metrics,
            'traditional_quantum_2': traditional_metrics_small
        })
        
        # Print results
        print(f"\nEnhanced RR (Dynamic Quantum):")
        for key, value in enhanced_metrics.items():
            print(f"  {key}: {value:.2f}")
        
        print(f"\nTraditional RR (Quantum=4):")
        for key, value in traditional_metrics.items():
            print(f"  {key}: {value:.2f}")
        
        print(f"\nTraditional RR (Quantum=2):")
        for key, value in traditional_metrics_small.items():
            print(f"  {key}: {value:.2f}")
    
    return results

def main():
    """Main function to run the simulation"""
    print("Enhanced Round Robin Scheduling Algorithm")
    print("="*60)
    
    results = run_comparison()
    
    # Calculate average improvements
    avg_improvement_turnaround = 0
    avg_improvement_waiting = 0
    avg_improvement_response = 0
    
    for result in results:
        enhanced = result['enhanced']
        traditional = result['traditional_quantum_4']
        
        improvement_turnaround = ((traditional['avg_turnaround'] - enhanced['avg_turnaround']) 
                                / traditional['avg_turnaround']) * 100
        improvement_waiting = ((traditional['avg_waiting'] - enhanced['avg_waiting']) 
                             / traditional['avg_waiting']) * 100
        improvement_response = ((traditional['avg_response'] - enhanced['avg_response']) 
                              / traditional['avg_response']) * 100
        
        avg_improvement_turnaround += improvement_turnaround
        avg_improvement_waiting += improvement_waiting
        avg_improvement_response += improvement_response
    
    num_tests = len(results)
    avg_improvement_turnaround /= num_tests
    avg_improvement_waiting /= num_tests
    avg_improvement_response /= num_tests
    
    print(f"\n{'='*60}")
    print("SUMMARY OF IMPROVEMENTS (Enhanced vs Traditional RR)")
    print(f"{'='*60}")
    print(f"Average Improvement in Turnaround Time: {avg_improvement_turnaround:.2f}%")
    print(f"Average Improvement in Waiting Time: {avg_improvement_waiting:.2f}%")
    print(f"Average Improvement in Response Time: {avg_improvement_response:.2f}%")
    
    # Export results to CSV
    export_results(results)

def export_results(results):
    """Export results to CSV file"""
    import csv
    
    with open('scheduling_results.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        
        # Write header
        header = ['Test Case', 'Algorithm', 'Avg Turnaround', 'Avg Waiting', 
                 'Avg Response', 'CPU Utilization', 'Throughput', 'Context Switches']
        writer.writerow(header)
        
        # Write data
        for result in results:
            # Enhanced RR
            writer.writerow([
                result['test_case'], 'Enhanced RR',
                result['enhanced']['avg_turnaround'],
                result['enhanced']['avg_waiting'],
                result['enhanced']['avg_response'],
                result['enhanced']['cpu_utilization'],
                result['enhanced']['throughput'],
                result['enhanced']['context_switches']
            ])
            
            # Traditional RR (Quantum=4)
            writer.writerow([
                result['test_case'], 'Traditional RR (Q=4)',
                result['traditional_quantum_4']['avg_turnaround'],
                result['traditional_quantum_4']['avg_waiting'],
                result['traditional_quantum_4']['avg_response'],
                result['traditional_quantum_4']['cpu_utilization'],
                result['traditional_quantum_4']['throughput'],
                result['traditional_quantum_4']['context_switches']
            ])
            
            # Traditional RR (Quantum=2)
            writer.writerow([
                result['test_case'], 'Traditional RR (Q=2)',
                result['traditional_quantum_2']['avg_turnaround'],
                result['traditional_quantum_2']['avg_waiting'],
                result['traditional_quantum_2']['avg_response'],
                result['traditional_quantum_2']['cpu_utilization'],
                result['traditional_quantum_2']['throughput'],
                result['traditional_quantum_2']['context_switches']
            ])
    
    print("\nResults exported to 'scheduling_results.csv'")

if __name__ == "__main__":
    main()