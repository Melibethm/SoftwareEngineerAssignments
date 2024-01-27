import random

cpu_usage = random.randint(0, 100)

if cpu_usage > 90:
    print("High CPU usage!")
elif 80 < cpu_usage <= 90:  # corrected the syntax here
    pass
#Added a colon at the end of the elif line.
#Adjusted the syntax for checking if cpu_usage is between 80 and 90 (inclusive).

import random

def monitor_system():
    cpu_usage = random.randint(0, 100)
    memory_usage = random.randint(0, 100)
    disk_space = random.randint(0, 100)

    print(f"CPU Usage: {cpu_usage}%")
    print(f"Memory Usage: {memory_usage}%")
    print(f"Disk Space: {disk_space}%")

    if cpu_usage > 90:
        print("High CPU usage! Alert!")
    elif 80 < cpu_usage <= 90:
        pass  # Gray zone, silently log

    if memory_usage > 90:
        print("High Memory usage! Alert!")
    elif 80 < memory_usage <= 90:
        pass  # Gray zone, silently log

    if disk_space > 90:
        print("Low Disk Space! Alert!")
    elif 80 < disk_space <= 90:
        pass  # Gray zone, silently log

# Run the system monitor
monitor_system()
