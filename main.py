from collections import deque

class Process:
    def __init__(self, process_id, arrival_time, burst_time, memory_requirements):
        self.process_id = process_id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.memory_requirements = memory_requirements
        self.completion_time = 0
        self.start_time = None
        self.end_time = None
        self.waiting_time = None
        self.turnaround_time = None

    def __str__(self):
        return (f"Process(process_id={self.process_id}, arrival_time={self.arrival_time}, "
                f"burst_time={self.burst_time}, memory_requirements={self.memory_requirements})")

def readyQueue(job_queue):
    ready_queue = []
    for process in job_queue:
        ready_queue.append(process)
    ready_queue.sort(key=lambda p: p.arrival_time)
    return ready_queue

def executing_process_fcfs(ready_queue):
    print("Executing processes in first-come, first-served algorithm")
    time = 0
    for process in ready_queue:
        if time < process.arrival_time:
            time = process.arrival_time
        process.start_time = time
        print(f"\nExecuting Process ID: {process.process_id}")
        print(f"Arrival Time: {process.arrival_time}")
        print(f"Memory Requirements: {process.memory_requirements}")
        time += process.burst_time
        process.end_time = time
        process.completion_time = time
        process.turnaround_time = process.end_time - process.arrival_time
        process.waiting_time = process.turnaround_time - process.burst_time
        print(f"Process {process.process_id} executed for {process.burst_time} units of time")
        print(f"Process {process.process_id} has been successfully executed!")

def readyQueue_sjf(ready_queue):
    ready_queue_sjf = []
    for process in ready_queue:
        ready_queue_sjf.append(process)
    ready_queue_sjf.sort(key=lambda p: p.burst_time)
    return ready_queue_sjf

def executing_process_sjf(ready_queue_sjf):
    print("Executing processes in the shortest job first algorithm")
    time = 0
    for process in ready_queue_sjf:
        if time < process.arrival_time:
            time = process.arrival_time
        process.start_time = time
        print(f"\nExecuting Process ID: {process.process_id}")
        print(f"Arrival Time: {process.arrival_time}")
        print(f"Memory Requirements: {process.memory_requirements}")
        time += process.burst_time
        process.end_time = time
        process.completion_time = time
        process.turnaround_time = process.end_time - process.arrival_time
        process.waiting_time = process.turnaround_time - process.burst_time
        print(f"Process {process.process_id} executed for {process.burst_time} units of time")
        print(f"Process {process.process_id} has been successfully executed!")

def round_robin(ready_queue, quantum):
    time = 0
    queue = deque(ready_queue)
    completed_process = []

    while queue:
        process = queue.popleft()

        if process.arrival_time <= time:
            if process.remaining_time > quantum:
                time += quantum
                process.remaining_time -= quantum
                queue.append(process)
            else:
                time += process.remaining_time
                process.remaining_time = 0
                process.completion_time = time
                process.end_time = time
                process.turnaround_time = process.end_time - process.arrival_time
                process.waiting_time = process.turnaround_time - process.burst_time
                completed_process.append(process)
            print(f"Time: {time}, Process: {process.process_id}, Remaining Time: {process.remaining_time}")
        else:
            queue.append(process)
            if queue and queue[0].arrival_time > time:
                time = queue[0].arrival_time

    return completed_process

def main():
    print("Process Scheduler")

    num_of_processes = int(input("Enter the number of processes: "))
    input_processes = []
    for i in range(num_of_processes):
        arrival_time = int(input(f"Enter the arrival time for process {i+1}: "))
        burst_time = int(input(f"Enter the burst time for process {i+1}: "))
        memory_requirement = int(input(f"Enter the memory requirement for process {i+1}: "))
        input_processes.append(Process(process_id=i+1, arrival_time=arrival_time, burst_time=burst_time, memory_requirements=memory_requirement))

    print("\nChoose preferred scheduling algorithm:")
    print("1. First Come First Served (FCFS)")
    print("2. Shortest Job First (SJF)")
    print("3. Round Robin (RR)")
    scheduling_choice = int(input("Enter your preferred algorithm: "))

    if scheduling_choice == 1:
        input_processes = readyQueue(input_processes)
        executing_process_fcfs(input_processes)
    elif scheduling_choice == 2:
        input_processes = readyQueue_sjf(readyQueue(input_processes))
        executing_process_sjf(input_processes)
    elif scheduling_choice == 3:
        quantum = int(input("Enter the time quantum for Round Robin: "))
        completed_processes = round_robin(readyQueue(input_processes), quantum)
        input_processes = completed_processes
    else:
        print("Invalid input! Please provide a valid choice.")

    print("\nProcess Scheduling Results:")
    for process in input_processes:
        print(f"Process {process.process_id}: Start Time: {process.start_time}, End Time: {process.end_time}, "
              f"Waiting Time: {process.waiting_time}, Turnaround Time: {process.turnaround_time}")

if __name__ == "__main__":
    main()
