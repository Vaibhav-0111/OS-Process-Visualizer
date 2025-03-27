import tkinter as tk
from tkinter import ttk, messagebox
import psutil
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import platform

class ProcessVirtualizationGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Process Virtualization Dashboard")
        self.root.geometry("1000x700")
        self.root.configure(bg='#f0f0f0')
        
        # Initialize status_var before using it
        self.status_var = tk.StringVar()
        self.status_var.set("Status: Ready")
        
        # Apply a modern theme
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('TNotebook', background='#f0f0f0')
        self.style.configure('TNotebook.Tab', background='#e0e0e0', padding=[10, 5])
        self.style.map('TNotebook.Tab', background=[('selected', '#4a7dc9')])
        
        # Create main notebook (tabbed interface)
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand=True, fill='both', padx=10, pady=10)
        
        # Create tabs
        self.create_process_tab()
        self.create_visualization_tab()
        self.create_system_tab()
        
        # Status bar
        self.status_bar = ttk.Label(root, textvariable=self.status_var, relief='sunken', anchor='w')
        self.status_bar.pack(side='bottom', fill='x')
        
    def update_status(self, message):
        self.status_var.set(f"Status: {message}")
        
    def create_process_tab(self):
        """Tab for process management"""
        self.process_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.process_tab, text='Process Manager')
        
        # Frame for process list
        list_frame = ttk.LabelFrame(self.process_tab, text="Running Processes", padding=10)
        list_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Treeview for process list
        self.process_tree = ttk.Treeview(list_frame, columns=('pid', 'name', 'cpu', 'memory'), show='headings')
        self.process_tree.heading('pid', text='PID', anchor='w')
        self.process_tree.heading('name', text='Process Name', anchor='w')
        self.process_tree.heading('cpu', text='CPU %', anchor='w')
        self.process_tree.heading('memory', text='Memory %', anchor='w')
        
        # Set column widths
        self.process_tree.column('pid', width=80)
        self.process_tree.column('name', width=300)
        self.process_tree.column('cpu', width=80)
        self.process_tree.column('memory', width=80)
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=self.process_tree.yview)
        self.process_tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        self.process_tree.pack(fill='both', expand=True)
        
        # Button frame
        button_frame = ttk.Frame(self.process_tab)
        button_frame.pack(fill='x', padx=10, pady=5)
        
        # Buttons
        refresh_btn = ttk.Button(button_frame, text="🔄 Refresh", command=self.refresh_processes, style='Accent.TButton')
        refresh_btn.pack(side='left', padx=5)
        
        terminate_btn = ttk.Button(button_frame, text="⛔ Terminate", command=self.terminate_process)
        terminate_btn.pack(side='left', padx=5)
        
        # Configure styles for buttons
        self.style.configure('Accent.TButton', foreground='white', background='#4a7dc9')
        
        # Initial refresh
        self.refresh_processes()
        
    def create_visualization_tab(self):
        """Tab for visualizations"""
        self.viz_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.viz_tab, text='Visualizations')
        
        # Create notebook within visualization tab for different chart types
        self.viz_notebook = ttk.Notebook(self.viz_tab)
        self.viz_notebook.pack(expand=True, fill='both', padx=10, pady=10)
        
        # Create visualization frames
        self.create_gauge_frame()
        self.create_pie_frame()
        self.create_line_frame()
        self.create_histogram_frame()
        
    def create_gauge_frame(self):
        """Frame for gauge visualization"""
        frame = ttk.Frame(self.viz_notebook)
        self.viz_notebook.add(frame, text='Gauge Charts')
        
        # Matplotlib figure
        fig = Figure(figsize=(8, 4), dpi=100)
        self.gauge_plot = fig.add_subplot(111)
        
        # Canvas for embedding in Tkinter
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill='both', expand=True)
        
        # Button to update
        btn = ttk.Button(frame, text="Update Gauge", command=self.update_gauge)
        btn.pack(pady=5)
        
        # Initial update
        self.update_gauge()
        
    def update_gauge(self):
        """Update the gauge visualization"""
        try:
            cpu = psutil.cpu_percent()
            memory = psutil.virtual_memory().percent
            
            self.gauge_plot.clear()
            self.gauge_plot.barh(["CPU"], [cpu], color='red', height=0.3)
            self.gauge_plot.barh(["Memory"], [memory], color='blue', height=0.3)
            self.gauge_plot.set_xlim(0, 100)
            self.gauge_plot.set_xlabel("Usage (%)")
            self.gauge_plot.set_title("CPU & Memory Usage")
            
            # Redraw canvas
            fig = self.gauge_plot.figure
            fig.canvas.draw_idle()
            self.update_status("Gauge chart updated successfully")
        except Exception as e:
            self.update_status(f"Error updating gauge: {str(e)}")
        
    def create_pie_frame(self):
        """Frame for pie chart visualization"""
        frame = ttk.Frame(self.viz_notebook)
        self.viz_notebook.add(frame, text='Process Distribution')
        
        # Matplotlib figure
        fig = Figure(figsize=(8, 6), dpi=100)
        self.pie_plot = fig.add_subplot(111)
        
        # Canvas for embedding in Tkinter
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill='both', expand=True)
        
        # Button to update
        btn = ttk.Button(frame, text="Update Pie Chart", command=self.update_pie)
        btn.pack(pady=5)
        
        # Initial update
        self.update_pie()
        
    def update_pie(self):
        """Update the pie chart visualization"""
        try:
            user_processes, system_processes = 0, 0
            for proc in psutil.process_iter(['username']):
                try:
                    if proc.info['username']:
                        user_processes += 1
                    else:
                        system_processes += 1
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    pass

            self.pie_plot.clear()
            self.pie_plot.pie([user_processes, system_processes], 
                             labels=["User", "System"],
                             autopct="%1.1f%%", 
                             colors=['orange', 'purple'])
            self.pie_plot.set_title("Process Distribution")
            
            # Redraw canvas
            fig = self.pie_plot.figure
            fig.canvas.draw_idle()
            self.update_status("Pie chart updated successfully")
        except Exception as e:
            self.update_status(f"Error updating pie chart: {str(e)}")
        
    def create_line_frame(self):
        """Frame for line chart visualization"""
        frame = ttk.Frame(self.viz_notebook)
        self.viz_notebook.add(frame, text='Resource Usage Over Time')
        
        # Matplotlib figure
        fig = Figure(figsize=(8, 6), dpi=100)
        self.line_plot = fig.add_subplot(111)
        
        # Canvas for embedding in Tkinter
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill='both', expand=True)
        
        # Button to update
        btn = ttk.Button(frame, text="Update Line Chart", command=self.update_line)
        btn.pack(pady=5)
        
        # Initial update
        self.update_line()
        
    def update_line(self):
        """Update the line chart visualization"""
        try:
            cpu_usage, memory_usage = [], []
            
            self.update_status("Collecting CPU and memory data (30 seconds)...")
            self.root.update()  # Force UI update
            
            for _ in range(30):  # Collect data for 30 seconds
                cpu_usage.append(psutil.cpu_percent(interval=1))
                memory_usage.append(psutil.virtual_memory().percent)

            self.line_plot.clear()
            self.line_plot.plot(cpu_usage, marker='o', linestyle='-', color='red', label="CPU Usage")
            self.line_plot.plot(memory_usage, marker='s', linestyle='-', color='blue', label="Memory Usage")
            self.line_plot.set_xlabel("Time (seconds)")
            self.line_plot.set_ylabel("Usage (%)")
            self.line_plot.set_title("CPU & Memory Utilization Over Time")
            self.line_plot.legend()
            self.line_plot.grid(True)
            
            # Redraw canvas
            fig = self.line_plot.figure
            fig.canvas.draw_idle()
            self.update_status("Line chart updated successfully")
        except Exception as e:
            self.update_status(f"Error updating line chart: {str(e)}")
        
    def create_histogram_frame(self):
        """Frame for histogram visualization"""
        frame = ttk.Frame(self.viz_notebook)
        self.viz_notebook.add(frame, text='CPU Load Analysis')
        
        # Matplotlib figure
        fig = Figure(figsize=(8, 6), dpi=100)
        self.hist_plot = fig.add_subplot(111)
        
        # Canvas for embedding in Tkinter
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill='both', expand=True)
        
        # Button to update
        btn = ttk.Button(frame, text="Update Histogram", command=self.update_histogram)
        btn.pack(pady=5)
        
        # Initial update
        self.update_histogram()
        
    def update_histogram(self):
        """Update the histogram visualization"""
        try:
            cpu_usage = [psutil.cpu_percent(interval=0.1) for _ in range(20)]
            
            self.hist_plot.clear()
            self.hist_plot.hist(cpu_usage, bins=10, color='green', alpha=0.7)
            self.hist_plot.set_title("CPU Load Distribution")
            self.hist_plot.set_xlabel("CPU Usage (%)")
            self.hist_plot.set_ylabel("Frequency")
            
            # Redraw canvas
            fig = self.hist_plot.figure
            fig.canvas.draw_idle()
            self.update_status("Histogram updated successfully")
        except Exception as e:
            self.update_status(f"Error updating histogram: {str(e)}")
        
    def create_system_tab(self):
        """Tab for system information"""
        self.sys_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.sys_tab, text='System Info')
        
        # System information labels
        info_frame = ttk.LabelFrame(self.sys_tab, text="System Information", padding=10)
        info_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # OS info
        ttk.Label(info_frame, text="OS:", font=('Arial', 10, 'bold')).grid(row=0, column=0, sticky='w')
        self.os_label = ttk.Label(info_frame, text=f"{platform.system()} {platform.release()}")
        self.os_label.grid(row=0, column=1, sticky='w')
        
        # CPU info
        ttk.Label(info_frame, text="CPU:", font=('Arial', 10, 'bold')).grid(row=1, column=0, sticky='w')
        self.cpu_label = ttk.Label(info_frame, text="")
        self.cpu_label.grid(row=1, column=1, sticky='w')
        
        # Memory info
        ttk.Label(info_frame, text="Memory:", font=('Arial', 10, 'bold')).grid(row=2, column=0, sticky='w')
        self.mem_label = ttk.Label(info_frame, text="")
        self.mem_label.grid(row=2, column=1, sticky='w')
        
        # Disk info
        ttk.Label(info_frame, text="Disk (C:):", font=('Arial', 10, 'bold')).grid(row=3, column=0, sticky='w')
        self.disk_label = ttk.Label(info_frame, text="")
        self.disk_label.grid(row=3, column=1, sticky='w')
        
        # Update button
        btn = ttk.Button(info_frame, text="Update System Info", command=self.update_system_info)
        btn.grid(row=4, column=0, columnspan=2, pady=10)
        
        # Initial update
        self.update_system_info()
        
    def update_system_info(self):
        """Update system information labels"""
        try:
            # CPU info
            cpu_count = psutil.cpu_count()
            try:
                cpu_freq = psutil.cpu_freq().current
                cpu_info = f"{cpu_count} cores, {cpu_freq:.0f} MHz"
            except Exception:
                cpu_info = f"{cpu_count} cores"
            self.cpu_label.config(text=cpu_info)
            
            # Memory info
            mem = psutil.virtual_memory()
            mem_info = f"{mem.used/1024/1024/1024:.1f} GB used / {mem.total/1024/1024/1024:.1f} GB total"
            self.mem_label.config(text=mem_info)
            
            # Disk info - handle potential errors
            try:
                disk = psutil.disk_usage('C:\\')  # Use C: drive on Windows
                disk_info = f"{disk.used/1024/1024/1024:.1f} GB used / {disk.total/1024/1024/1024:.1f} GB total"
            except Exception as e:
                disk_info = "Disk info unavailable"
            self.disk_label.config(text=disk_info)
            
            self.update_status("System info updated successfully")
        except Exception as e:
            self.update_status(f"Error updating system info: {str(e)}")
        
    def refresh_processes(self):
        """Refresh the process list in the treeview"""
        try:
            self.process_tree.delete(*self.process_tree.get_children())
            
            processes = {}
            for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
                try:
                    info = proc.info
                    processes[info['name']] = (info['pid'], info['cpu_percent'], info['memory_percent'])
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    pass
            
            # Sort by CPU usage (descending)
            sorted_procs = sorted(processes.items(), key=lambda x: x[1][1], reverse=True)
            
            for name, (pid, cpu, mem) in sorted_procs:
                self.process_tree.insert('', 'end', values=(pid, name, f"{cpu:.1f}", f"{mem:.1f}"))
                
            self.update_status(f"Process list updated - {len(sorted_procs)} processes")
        except Exception as e:
            self.update_status(f"Error refreshing processes: {str(e)}")
        
    def terminate_process(self):
        """Terminate the selected process"""
        selected_item = self.process_tree.selection()
        if not selected_item:
            messagebox.showwarning("Error", "Please select a process to terminate")
            return
            
        pid = int(self.process_tree.item(selected_item)['values'][0])
        name = self.process_tree.item(selected_item)['values'][1]
        
        try:
            # Ask for confirmation
            if messagebox.askyesno("Confirm", f"Terminate process {name} (PID: {pid})?"):
                p = psutil.Process(pid)
                p.terminate()
                messagebox.showinfo("Success", f"Process {name} (PID: {pid}) terminated")
                self.refresh_processes()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to terminate process: {e}")