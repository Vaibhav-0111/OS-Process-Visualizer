#It is main part 

import psutil

from tkinter import messagebox 

class ProcessManager:
    def list_processes(self):
        """Fetch running processes with details (PID, CPU, Memory)."""
        processes = {}
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
            try:
                info = proc.info
                processes[info['name']] = (info['pid'], {'cpu': info['cpu_percent'], 'memory': info['memory_percent']})
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        return processes
    
    def terminate_process(self):
        """Terminate the selected process with proper error handling"""
        selected_item = self.process_tree.selection()
        if not selected_item:
            messagebox.showwarning("Error", "Please select a process to terminate")
            return
        
        pid = int(self.process_tree.item(selected_item)['values'][0])
        name = self.process_tree.item(selected_item)['values'][1]
    
        try:
        # Ask for confirmation
            if not messagebox.askyesno("Confirm Termination", 
                                 f"Are you sure you want to terminate:\n{name} (PID: {pid})?"):
                return
            
            p = psutil.Process(pid)
        
        # Try graceful termination first
            p.terminate()
        
        # Check if process still exists
            try:
                if p.is_running():
                # If still running, try killing it
                    p.kill()
            except psutil.NoSuchProcess:
                pass
            
        # Verify termination
            try:
                if p.is_running():
                    messagebox.showerror("Error", f"Failed to terminate process {name} (PID: {pid})")
                else:
                    messagebox.showinfo("Success", f"Process {name} (PID: {pid}) terminated successfully")
                    self.refresh_processes()
            except psutil.NoSuchProcess:
                messagebox.showinfo("Success", f"Process {name} (PID: {pid}) terminated successfully")
                self.refresh_processes()
            
        except psutil.AccessDenied:
            messagebox.showerror("Error", f"Access denied. Try running as Administrator.")
        except psutil.NoSuchProcess:
            messagebox.showerror("Error", f"Process {name} (PID: {pid}) no longer exists")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to terminate process: {str(e)}")
