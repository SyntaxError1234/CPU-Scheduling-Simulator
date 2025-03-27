# CPU-Scheduling-Simulator
Project Overview

This repository contains our project for the CSE316 course at Lovely Professional University, submitted as part of Academic Task-2. Our team developed a CPU Scheduling Simulator that models and visualizes the execution of different CPU scheduling algorithms. The project is implemented in Python and follows a three-module architecture, ensuring modularity and scalability.

What It Does

Our CPU Scheduling Simulator allows users to:

Select a CPU scheduling algorithm (FCFS, SJF, Priority, Round Robin, etc.).

Input process details such as burst time, arrival time, and priority.

Simulate and visualize process execution using Gantt charts.

Calculate and display key performance metrics:

Average waiting time

Turnaround time

Response time

CPU utilization

Features

Multiple Scheduling Algorithms: Supports FCFS, SJF (preemptive & non-preemptive), Priority, and Round Robin.

Graphical Visualization: Displays process execution using Gantt charts.

Performance Metrics: Computes and displays scheduling efficiency.

Modular Design: Divided into three distinct modules for easy maintainability.

Interactive Interface: Allows users to input custom processes for simulation.

How to Run It

Follow these steps to set up and run the project on your system:

1. Install Python 3

Download and install Python 3 from python.org.

Ensure Python is added to your system's PATH.

2. Install Required Libraries

Open a terminal or command prompt and run the following command:

pip install matplotlib numpy

3. Clone or Download the Repository

To clone the repository using Git:

git clone https://github.com/your-repo-link/CPUSchedulingSimulator.git

Or download the ZIP file from GitHub and extract it.

4. Navigate to the Project Directory

cd CPUSchedulingSimulator

5. Run the Project

Execute the main script to start the simulator:

python main.py

Project Structure

The project is divided into three main modules, each responsible for a specific functionality:

Process Input & Management (process_manager.py): Handles user input for processes and scheduling parameters.

CPU Scheduling Algorithms (scheduler.py): Implements multiple scheduling algorithms.

Visualization (visualizer.py): Generates Gantt charts to visualize process execution.

Main Script (main.py): Integrates all modules to run the simulator.

Team Members and Contributions

Our team consists of three members, each responsible for one module:

Reg Number 12319490: Developed the Process Management module.

Reg Number 12312303: Developed the CPU Scheduling Algorithms module.

Me (Reg Number 12314690): Developed the Visualization module and integrated all modules in main.py.

Technologies Used

Python 3: The programming language for the entire project.

Libraries Used:

matplotlib: For generating Gantt charts.

numpy: For numerical computations.

GitHub: For version control and collaboration.

Development Process

Repository Setup: Created a public repository on GitHub.

Module Development:

Each team member worked on their respective module in separate branches.

Used multiple commits to track progress.

Revisions & Integration:

Merged all branches into main using pull requests.

Ensured all modules work seamlessly together.

Documentation:

Created this README.md for detailed project description.

Notes

The scheduling simulation supports a configurable time quantum for Round Robin.

You can stop the simulation early using Ctrl+C in the terminal.

The visualization module generates a Gantt chart for process execution.

Future Improvements

Add live process execution animation.

Implement interactive UI using Tkinter or PyQt.

Support multi-core scheduling simulation.

Improve error handling and user input validation.

GitHub Contributions

We made 25+ commits in this repository to track our progress. Each team member contributed through their respective branches, and all changes were merged into main. Check the commit history for detailed progress!

Course: CSE316

Institution: Lovely Professional University

Date: March 25, 2025
