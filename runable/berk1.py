import time
import threading
import random

class BerkeleyTimeSync:
    def __init__(self, num_machines):
        self.num_machines = num_machines
        self.clock_offsets = [0] * num_machines
        self.lock = threading.Lock()

    def synchronize_time(self, machine_id, current_time):
        self.lock.acquire()
        self.clock_offsets[machine_id] = time.time() - current_time
        self.lock.release()

    def adjust_time(self, current_time):
        self.lock.acquire()
        average_offset = sum(self.clock_offsets) / self.num_machines
        new_time = current_time + average_offset
        self.lock.release()
        return new_time

def machine_function(machine_id, time_sync):
    while True:
        current_time = time.time()
        # Simulate some work
        time.sleep(random.uniform(0.1, 0.5))
        time_sync.synchronize_time(machine_id, current_time)

if __name__ == "__main__":
    num_machines = 5
    time_sync = BerkeleyTimeSync(num_machines)

    # Create and start threads for each machine
    threads = []
    for i in range(num_machines):
        t = threading.Thread(target=machine_function, args=(i, time_sync))
        threads.append(t)
        t.start()

    # Main loop for adjusting time
    while True:
        current_time = time.time()
        adjusted_time = time_sync.adjust_time(current_time)
        print(f"Adjusted time: {adjusted_time}")
        time.sleep(1)  # Adjust time periodically
