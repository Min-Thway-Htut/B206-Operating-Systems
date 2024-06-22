"""Defining a class including process id, arrival time, burst time, and memory requirements."""

class Process:
    def __init__(self, process_id, arrival_time, burst_time, memory_requirements):
        self.process_id = process_id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.memory_requirements = memory_requirements

 
    def __str__(self):
           return (f"Process(process_id={self.process_id}, arrival_time={self.arrival_time}, "
                f"burst_time={self.burst_time}, memory_requirements={self.memory_requirements})")
    

process1 = Process(process_id=1, arrival_time=0, burst_time = 5, memory_requirements = 500)
process2 = Process(process_id=2, arrival_time=2, burst_time = 2, memory_requirements = 400)
process3 = Process(process_id=3, arrival_time=4, burst_time = 6, memory_requirements = 400)
process4 = Process(process_id=4, arrival_time=3, burst_time = 4, memory_requirements = 300)
process5 = Process(process_id=5, arrival_time=8, burst_time = 35, memory_requirements = 300)
process6 = Process(process_id=6, arrival_time=9, burst_time = 1, memory_requirements = 400)
process7 = Process(process_id=7, arrival_time=12, burst_time = 13, memory_requirements = 500)

job_queue = []


"""All of the processes in the Process class are added into the job queue."""

job_queue.append(process1)
job_queue.append(process2)
job_queue.append(process3)
job_queue.append(process4)
job_queue.append(process5)
job_queue.append(process6)
job_queue.append(process7)


"""Implementing a function to add porcesses into the ready queue based on their arrival time."""

def readyQueue (job_queue):
     ready_queue = []
     for processes in job_queue:
          ready_queue.append(processes)

     ready_queue.sort(key=lambda p: p.arrival_time)
     return ready_queue
          

ready_queue = readyQueue(job_queue)

"""Implementing the First Come Frist Served algorithm"""

def excuting_process_fcfs(ready_queue):
     print("Executing processes in first-come, first-served algorithm")
     for process in ready_queue:
          print(f"\nExecuting Process ID: {process.process_id}")
          print(f"Arrival Time: {process.arrival_time}")
          print(f"Memory Requirements: {process.memory_requirements}")

          print(f"Process {process.process_id} executed for {process.burst_time} units of time")
          print(f"Process {process.process_id} has been successfully executed!")

"""excuting_process_fcfs(ready_queue)"""


def readyQueue_sjf(ready_queue):
     ready_queue_sjf = []
     for process in ready_queue:
          ready_queue_sjf.append(process)

     ready_queue_sjf.sort(key=lambda p: p.burst_time)
     return ready_queue_sjf

ready_queue_sjf = readyQueue_sjf(ready_queue)

def executing_process_sjf(ready_queue_sjf):
     print("Excuting process in shortest job first algorithm")
     for process in ready_queue_sjf:
          print(f"\nExecuting Process ID: {process.process_id}")
          print(f"Arrival Time: {process.arrival_time}")
          print(f"Memory Requirements: {process.memory_requirements}")

          print(f"Process {process.process_id} executed for {process.burst_time} units of time")
          print(f"Process {process.process_id} has been successfully executed!")

executing_process_sjf(ready_queue_sjf)