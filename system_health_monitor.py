import psutil
import logging

# Set up logging
logging.basicConfig(filename='system_health.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define thresholds
CPU_THRESHOLD = 80  # CPU usage percentage
MEMORY_THRESHOLD = 80  # Memory usage percentage
DISK_THRESHOLD = 80  # Disk usage percentage

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        logging.warning(f'High CPU usage detected: {cpu_usage}%')
    else:
        logging.info(f'CPU usage is normal: {cpu_usage}%')

def check_memory_usage():
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    if memory_usage > MEMORY_THRESHOLD:
        logging.warning(f'High memory usage detected: {memory_usage}%')
    else:
        logging.info(f'Memory usage is normal: {memory_usage}%')

def check_disk_usage():
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent
    if disk_usage > DISK_THRESHOLD:
        logging.warning(f'High disk usage detected: {disk_usage}%')
    else:
        logging.info(f'Disk usage is normal: {disk_usage}%')

def check_running_processes():
    process_count = len(psutil.pids())
    logging.info(f'Number of running processes: {process_count}')

def main():
    check_cpu_usage()
    check_memory_usage()
    check_disk_usage()
    check_running_processes()

if __name__ == "__main__":
    main()
