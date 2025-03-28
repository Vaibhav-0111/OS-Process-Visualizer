#The Visualization Module is designed to create graphical representations of real-time
#system resource usage. The module uses Matplotlib and Seaborn for creating clear,
#informative, and interactive visualizations.
    
import matplotlib.pyplot as plt
import psutil
import seaborn as sns
import numpy as np
import time

def plot_gauge():
    """Displays CPU & Memory Usage as a bar chart."""
    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent

    plt.figure(figsize=(5, 3))
    plt.barh(["CPU"], [cpu], color='red', height=0.3)
    plt.barh(["Memory"], [memory], color='blue', height=0.3)
    plt.xlim(0, 100)
    plt.xlabel("Usage (%)")
    plt.title("CPU & Memory Usage")
    plt.show()

def plot_pie_chart():
    """Displays Process Distribution (User vs System)."""
    user_processes, system_processes = 0, 0
    for proc in psutil.process_iter(['username']):
        try:
            if proc.info['username']:
                user_processes += 1
            else:
                system_processes += 1
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    plt.figure(figsize=(5, 5))
    plt.pie([user_processes, system_processes], labels=["User", "System"],
            autopct="%1.1f%%", colors=['orange', 'purple'])
    plt.title("Process Distribution")
    plt.show()

def plot_heatmap():
    """Displays a heatmap for random resource consumption data."""
    heatmap_data = np.random.rand(10, 10) * 100  # Simulated data
    plt.figure(figsize=(6, 4))
    sns.heatmap(heatmap_data, cmap="coolwarm", annot=True, fmt=".1f", linewidths=0.1)
    plt.title("Process Resource Consumption")
    plt.show()

def plot_histogram():
    """Displays CPU Load Distribution using a histogram."""
    cpu_usage = [psutil.cpu_percent(interval=0.1) for _ in range(20)]
    plt.figure(figsize=(6, 4))
    plt.hist(cpu_usage, bins=10, color='green', alpha=0.7)
    plt.title("CPU Load Distribution")
    plt.xlabel("CPU Usage (%)")
    plt.ylabel("Frequency")
    plt.show()

# ** NEW ** - Line Plots for CPU & Memory Usage Over Time
def plot_cpu_usage():
    """Shows a real-time line plot of CPU usage over 30 seconds."""
    usage = []
    for _ in range(30):  # Collect data for 30 seconds
        usage.append(psutil.cpu_percent(interval=1))

    plt.figure(figsize=(6, 4))
    plt.plot(usage, marker='o', linestyle='-', color='red')
    plt.xlabel("Time (seconds)")
    plt.ylabel("CPU Usage (%)")
    plt.title("CPU Usage Over Time")
    plt.grid(True)
    plt.show()

def plot_memory_usage():
    """Shows a real-time line plot of Memory usage over 30 seconds."""
    usage = []
    for _ in range(30):  # Collect data for 30 seconds
        usage.append(psutil.virtual_memory().percent)

    plt.figure(figsize=(6, 4))
    plt.plot(usage, marker='o', linestyle='-', color='blue')
    plt.xlabel("Time (seconds)")
    plt.ylabel("Memory Usage (%)")
    plt.title("Memory Usage Over Time")
    plt.grid(True)
    plt.show()

def plot_resource_utilization():
    """Shows a real-time line plot for both CPU & Memory usage together."""
    cpu_usage, memory_usage = [], []
    
    for _ in range(30):  # Collect data for 30 seconds
        cpu_usage.append(psutil.cpu_percent(interval=1))
        memory_usage.append(psutil.virtual_memory().percent)

    plt.figure(figsize=(6, 4))
    plt.plot(cpu_usage, marker='o', linestyle='-', color='red', label="CPU Usage")
    plt.plot(memory_usage, marker='s', linestyle='-', color='blue', label="Memory Usage")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Usage (%)")
    plt.title("CPU & Memory Utilization Over Time")
    plt.legend()
    plt.grid(True)
    plt.show()
