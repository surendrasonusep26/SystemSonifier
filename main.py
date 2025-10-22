import psutil
import winsound
import time

def play_cpu_sound():
    cpu = psutil.cpu_percent(interval=0.5)
    freq = 200 + int(cpu * 8)   # CPU usage  frequency
    duration = 100
    winsound.Beep(freq, duration)

def play_ram_sound():
    ram = psutil.virtual_memory().percent
    freq = 400 + int(ram * 6)   # RAM usage  frequency
    duration = 100
    winsound.Beep(freq, duration)

def play_disk_sound():
    disk = psutil.disk_usage('/').percent
    freq = 600 + int(disk * 5)  # Disk usage  frequency
    duration = 100
    winsound.Beep(freq, duration)

while True:
    play_cpu_sound()
    play_ram_sound()
    play_disk_sound()
    time.sleep(0.1)

