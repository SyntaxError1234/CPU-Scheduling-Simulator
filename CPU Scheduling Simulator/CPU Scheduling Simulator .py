import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class CPUScheduler:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced CPU Scheduling Simulator")
        self.root.geometry("1200x800")
        
        # Scheduling Algorithms Dictionary
        self.scheduling_algorithms = {
            "FCFS (Non-Preemptive)": self.fcfs_non_preemptive,
            "SJF (Non-Preemptive)": self.sjf_non_preemptive,
            "SJF (Preemptive)": self.sjf_preemptive,
            "Priority (Non-Preemptive)": self.priority_non_preemptive,
            "Priority (Preemptive)": self.priority_preemptive,
            "Round Robin": self.round_robin
        }
        
        self.setup_ui()
    
    def setup_ui(self):
        # Main Frame
        main_frame = ttk.Frame(self.root, padding=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Algorithm Selection
        ttk.Label(main_frame, text="Select Scheduling Algorithm:").grid(row=0, column=0, sticky='w')
        self.algorithm_var = tk.StringVar()
        algorithm_dropdown = ttk.Combobox(
            main_frame, 
            textvariable=self.algorithm_var, 
            values=list(self.scheduling_algorithms.keys()),
            state="readonly",
            width=40
        )
        algorithm_dropdown.grid(row=0, column=1, sticky='w', pady=10)
        algorithm_dropdown.set("Select an Algorithm")
        
        # Process Inputs Section
        ttk.Label(main_frame, text="Process Details:").grid(row=1, column=0, sticky='w')
        
        # Columns for Process Input
        columns = ["Process ID", "Arrival Time", "Burst Time", "Priority"]
        self.process_entries = []
        
        for i, col in enumerate(columns):
            ttk.Label(main_frame, text=col).grid(row=2, column=i, padx=5)
        
        # Dynamic Process Input Rows
        for i in range(7):  # Allow up to 7 processes
            process_row = []
            for j in range(4):
                entry = ttk.Entry(main_frame, width=15)
                entry.grid(row=i+3, column=j, padx=5, pady=2)
                process_row.append(entry)
            self.process_entries.append(process_row)
        
        # Quantum Time for Round Robin (initially hidden)
        self.quantum_label = ttk.Label(main_frame, text="Time Quantum:")
        self.quantum_entry = ttk.Entry(main_frame, width=15)
        
        # Algorithm-specific binding
        algorithm_dropdown.bind('<<ComboboxSelected>>', self.toggle_quantum_input)
        
        # Buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=10, column=0, columnspan=4, pady=10)
        
        ttk.Button(button_frame, text="Simulate", command=self.simulate).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Clear", command=self.clear_inputs).pack(side=tk.LEFT, padx=5)
        
        # Results Display
        self.results_text = tk.Text(main_frame, height=10, width=80, wrap=tk.WORD)
        self.results_text.grid(row=11, column=0, columnspan=4, pady=10)
    
    def toggle_quantum_input(self, event):
        # Show/hide quantum input for Round Robin
        if self.algorithm_var.get() == "Round Robin":
            self.quantum_label.grid(row=10, column=0, sticky='w')
            self.quantum_entry.grid(row=10, column=1, sticky='w')
        else:
            try:
                self.quantum_label.grid_remove()
                self.quantum_entry.grid_remove()
            except:
                pass
    
    def get_process_data(self):
        processes = []
        for row in self.process_entries:
            # Check if first entry (Process ID) is not empty
            if row[0].get().strip():
                try:
                    pid = row[0].get()
                    arrival = float(row[1].get())
                    burst = float(row[2].get())
                    priority = float(row[3].get()) if row[3].get() else 0
                    processes.append([pid, arrival, burst, priority])
                except ValueError:
                    messagebox.showerror("Input Error", "Please enter valid numeric values")
                    return None
        return processes
    
    def simulate(self):
        # Clear previous results
        self.results_text.delete(1.0, tk.END)
        
        # Get selected algorithm
        selected_algorithm = self.algorithm_var.get()
        if selected_algorithm == "Select an Algorithm":
            messagebox.showerror("Error", "Please select a scheduling algorithm")
            return
        
        # Get process data
        processes = self.get_process_data()
        if not processes:
            return
        
        # Get quantum for Round Robin if applicable
        quantum = None
        if selected_algorithm == "Round Robin":
            try:
                quantum = float(self.quantum_entry.get())
            except ValueError:
                messagebox.showerror("Input Error", "Please enter a valid quantum time")
                return
        
        # Run selected algorithm
        algorithm_func = self.scheduling_algorithms[selected_algorithm]
        if quantum is not None:
            result = algorithm_func(processes, quantum)
        else:
            result = algorithm_func(processes)
        
        # Display results
        self.display_results(result, selected_algorithm)
        
        # Visualize Gantt Chart
        self.visualize_gantt_chart(result)
    
    def display_results(self, result, algorithm):
        # Display textual results
        self.results_text.insert(tk.END, f"Algorithm: {algorithm}\n\n")
        
        # Create DataFrame for results
        df = pd.DataFrame(result['process_details'])
        df.columns = ['Process', 'Arrival Time', 'Burst Time', 'Waiting Time', 'Turnaround Time']
        
        # Calculate average waiting and turnaround times
        avg_waiting_time = df['Waiting Time'].mean()
        avg_turnaround_time = df['Turnaround Time'].mean()
        
        # Display results in text widget
        self.results_text.insert(tk.END, df.to_string(index=False))
        self.results_text.insert(tk.END, f"\n\nAverage Waiting Time: {avg_waiting_time:.2f}")
        self.results_text.insert(tk.END, f"\nAverage Turnaround Time: {avg_turnaround_time:.2f}")
    
    def visualize_gantt_chart(self, result):
        plt.figure(figsize=(12, 5))
        plt.title(f"Gantt Chart")
        plt.xlabel("Time")
        plt.ylabel("Processes")
        
        # Plot processes
        for process in result['gantt_chart']:
            plt.barh(
                process[0], 
                process[2] - process[1],  # Duration
                left=process[1],  # Start time
                height=0.5, 
                align='center', 
                color='skyblue', 
                edgecolor='navy'
            )
        
        plt.tight_layout()
        plt.show()
    
    def clear_inputs(self):
        # Clear all input entries
        for row in self.process_entries:
            for entry in row:
                entry.delete(0, tk.END)
        
        # Clear results
        self.results_text.delete(1.0, tk.END)
        
        # Reset algorithm selection
        self.algorithm_var.set("Select an Algorithm")
    
    def fcfs_non_preemptive(self, processes):
        # Sort by arrival time
        processes.sort(key=lambda x: x[1])
        
        current_time = 0
        process_details = []
        gantt_chart = []
        
        for process in processes:
            pid, arrival, burst, _ = process
            
            # Wait if process hasn't arrived
            if current_time < arrival:
                current_time = arrival
            
            # Record Gantt chart entry
            gantt_chart.append([pid, current_time, current_time + burst])
            
            # Calculate waiting and turnaround times
            waiting_time = current_time - arrival
            turnaround_time = waiting_time + burst
            
            process_details.append([pid, arrival, burst, waiting_time, turnaround_time])
            
            # Update current time
            current_time += burst
        
        return {
            'process_details': process_details,
            'gantt_chart': gantt_chart
        }
    
    def sjf_non_preemptive(self, processes):
        processes.sort(key=lambda x: x[1])  # Sort by arrival time
        current_time = 0
        process_details = []
        gantt_chart = []
        remaining_processes = processes.copy()
        
        while remaining_processes:
            # Find processes that have arrived
            available_processes = [p for p in remaining_processes if p[1] <= current_time]
            
            if not available_processes:
                # If no process has arrived, move time to next arrival
                current_time = remaining_processes[0][1]
                continue
            
            # Select process with shortest burst time
            selected_process = min(available_processes, key=lambda x: x[2])
            
            pid, arrival, burst, _ = selected_process
            
            # Record Gantt chart entry
            gantt_chart.append([pid, current_time, current_time + burst])
            
            # Calculate waiting and turnaround times
            waiting_time = current_time - arrival
            turnaround_time = waiting_time + burst
            
            process_details.append([pid, arrival, burst, waiting_time, turnaround_time])
            
            # Update current time
            current_time += burst
            
            # Remove processed process
            remaining_processes.remove(selected_process)
        
        return {
            'process_details': process_details,
            'gantt_chart': gantt_chart
        }
    
    def sjf_preemptive(self, processes):
        processes.sort(key=lambda x: x[1])  # Sort by arrival time
        current_time = 0
        process_details = {}
        gantt_chart = []
        remaining_processes = processes.copy()
        
        while remaining_processes:
            # Find processes that have arrived
            available_processes = [p for p in remaining_processes if p[1] <= current_time]
            
            if not available_processes:
                # If no process has arrived, move time to next arrival
                current_time = remaining_processes[0][1]
                continue
            
            # Select process with shortest remaining time
            selected_process = min(available_processes, key=lambda x: x[2])
            
            pid, arrival, burst, _ = selected_process
            
            # Initialize process details if not exists
            if pid not in process_details:
                process_details[pid] = [pid, arrival, burst, 0, 0]
            
            # Allocate 1 time unit
            current_time += 1
            selected_process[2] -= 1  # Reduce remaining burst time
            
            # Record Gantt chart entry
            gantt_chart.append([pid, current_time - 1, current_time])
            
            # Remove process if completed
            if selected_process[2] == 0:
                # Calculate waiting and turnaround times
                waiting_time = current_time - arrival - burst
                turnaround_time = current_time - arrival
                
                process_details[pid][3] = waiting_time
                process_details[pid][4] = turnaround_time
                
                remaining_processes.remove(selected_process)
        
        return {
            'process_details': list(process_details.values()),
            'gantt_chart': gantt_chart
        }
    
    def priority_non_preemptive(self, processes):
        processes.sort(key=lambda x: x[1])  # Sort by arrival time
        current_time = 0
        process_details = []
        gantt_chart = []
        remaining_processes = processes.copy()
        
        while remaining_processes:
            # Find processes that have arrived
            available_processes = [p for p in remaining_processes if p[1] <= current_time]
            
            if not available_processes:
                # If no process has arrived, move time to next arrival
                current_time = remaining_processes[0][1]
                continue
            
            # Select process with highest priority (lower number means higher priority)
            selected_process = min(available_processes, key=lambda x: x[3])
            
            pid, arrival, burst, priority = selected_process
            
            # Record Gantt chart entry
            gantt_chart.append([pid, current_time, current_time + burst])
            
            # Calculate waiting and turnaround times
            waiting_time = current_time - arrival
            turnaround_time = waiting_time + burst
            
            process_details.append([pid, arrival, burst, waiting_time, turnaround_time])
            
            # Update current time
            current_time += burst
            
            # Remove processed process
            remaining_processes.remove(selected_process)
        
        return {
            'process_details': process_details,
            'gantt_chart': gantt_chart
        }
    
    def priority_preemptive(self, processes):
        processes.sort(key=lambda x: x[1])  # Sort by arrival time
        current_time = 0
        process_details = {}
        gantt_chart = []
        remaining_processes = processes.copy()
        
        while remaining_processes:
            # Find processes that have arrived
            available_processes = [p for p in remaining_processes if p[1] <= current_time]
            
            if not available_processes:
                # If no process has arrived, move time to next arrival
                current_time = remaining_processes[0][1]
                continue
            
            # Select process with highest priority (lower number means higher priority)
            selected_process = min(available_processes, key=lambda x: x[3])
            
            pid, arrival, burst, priority = selected_process
            
            # Initialize process details if not exists
            if pid not in process_details:
                process_details[pid] = [pid, arrival, burst, 0, 0]
            
            # Allocate 1 time unit
            current_time += 1
            selected_process[2] -= 1  # Reduce remaining burst time
            
            # Record Gantt chart entry
            gantt_chart.append([pid, current_time - 1, current_time])
            
            # Remove process if completed
            if selected_process[2] == 0:
                # Calculate waiting and turnaround times
                waiting_time = current_time - arrival - burst
                turnaround_time = current_time - arrival
                
                process_details[pid][3] = waiting_time
                process_details[pid][4] = turnaround_time
                
                remaining_processes.remove(selected_process)
        
        return {
            'process_details': list(process_details.values()),
            'gantt_chart': gantt_chart
        }
    
    def round_robin(self, processes, quantum):
        processes.sort(key=lambda x: x[1])  # Sort by arrival time
        current_time = 0
        process_details = {}
        gantt_chart = []
        remaining_processes = processes.copy()
        
        while remaining_processes:
            # Find processes that have arrived
            available_processes = [p for p in remaining_processes if p[1] <= current_time]
            
            if not available_processes:
                # If no process has arrived, move time to next arrival
                current_time = remaining_processes[0][1]
                continue
            
            # Select first available process
            selected_process = available_processes[0]
            
            pid, arrival, burst, _ = selected_process
            
            # Initialize process details if not exists
            if pid not in process_details:
                process_details[pid] = [pid, arrival, burst, 0, 0]
            
            # Allocate quantum time or remaining burst time
            execution_time = min(quantum, selected_process[2])
            current_time += execution_time
            selected_process[2] -= execution_time
            # Record Gantt chart entry
            gantt_chart.append([pid, current_time - execution_time, current_time])
            # Remove process if completed
            if selected_process[2] == 0:
                # Calculate waiting and turnaround times
                waiting_time = current_time - arrival - burst
                turnaround_time = current_time - arrival
                
                process_details[pid][3] = waiting_time
                process_details[pid][4] = turnaround_time
                
                remaining_processes.remove(selected_process)
            else:
                # Move process to end of queue
                remaining_processes.remove(selected_process)
                remaining_processes.append(selected_process)
        
        return {
            'process_details': list(process_details.values()),
            'gantt_chart': gantt_chart
        }
def main():
    root = tk.Tk()
    app = CPUScheduler(root)
    root.mainloop()

if __name__ == "_main_":
    main()