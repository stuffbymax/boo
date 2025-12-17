

# importing modules

import cowsay
from datetime import date
import psutil
import platform
import os
import socket
import GPUtil

# i need to find amd and intel one because GPUtil only works for nvidia

def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


# setting up variables for the script

name = os.environ.get('USER') or os.environ.get('USERNAME') # user system var

today = date.today().strftime('%d, %m, %Y') # to day date by D-M-Y format 

cpu = psutil.cpu_percent(interval=1) # get the cpu usage

ram = psutil.virtual_memory() # all ram usage
ram_usage = ram.percent # get the % of used ram

os = platform.system() # get the system OS name
os_Ver = platform.version() #get the version of OS


# Get the local IP address
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

# get the system info
uname = platform.uname()

# get cpu cores
cores = psutil.cpu_count(logical=False) # Physical cores
total_Cores = psutil.cpu_count(logical=True) # Total cores


gpus = GPUtil.getGPUs()
list_gpus = []
for gpu in gpus:
    # get the GPU id
    gpu_id = gpu.id
    # name of GPU
    gpu_name = gpu.name
    # get % percentage of GPU usage of that GPU
    gpu_load = f"{gpu.load*100}%"
    # get free memory in MB format
    gpu_free_memory = f"{gpu.memoryFree}MB"
    # get used memory
    gpu_used_memory = f"{gpu.memoryUsed}MB"
    # get total memory
    gpu_total_memory = f"{gpu.memoryTotal}MB"
    # get GPU temperature in Celsius
    gpu_temperature = f"{gpu.temperature} °C"
    gpu_uuid = gpu.uuid
    

message = f"BOO!\nName: {name}\nDate: {today} \n cpu usage {cpu}% \n ram usage {ram_usage}% \n system {os} \n system version {os_Ver} \n Processor {uname.processor} \n architecture {uname.machine} \n Local IP {local_ip} \n cores {total_Cores} \n {gpu.name} \n {gpu.memoryTotal} \n {gpu.memoryUsed}"

cowsay.cow(message)


#print(f"System: {uname.system}")
#print(f"Node Name: {uname.node}")
#print(f"Release: {uname.release}")
#print(f"Version: {uname.version}")
#print(f"Machine: {uname.machine}")
#print(f"Processor: {uname.processor}")




# CPU frequencies
#cpufreq = psutil.cpu_freq()
#print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
#print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
#print(f"Current Frequency: {cpufreq.current:.2f}Mhz")



# Memory Information
# get the memory details
#svmem = psutil.virtual_memory()
#print(f"Total: {get_size(svmem.total)}")
#print(f"Available: {get_size(svmem.available)}")
#print(f"Used: {get_size(svmem.used)}")
#print("="*20, "SWAP", "="*20)
# get the swap memory details (if exists)
#swap = psutil.swap_memory()
#print(f"Total: {get_size(swap.total)}")
#print(f"Free: {get_size(swap.free)}")
#print(f"Used: {get_size(swap.used)}")
#print(f"Percentage: {swap.percent}%")
