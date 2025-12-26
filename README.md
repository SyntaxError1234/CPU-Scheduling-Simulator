# CPU Scheduling Simulator - Three-Module Architecture

---

## 📌 Project Overview
This repository contains our project for the **CSE316** course at Lovely Professional University, submitted as part of **Academic Task-1**. Our team developed a **CPU Scheduling Simulator** that models and visualizes the execution of different CPU scheduling algorithms. The project is implemented in Python and follows a **three-module architecture**, ensuring modularity and scalability.

---

## 🔹 What It Does
Our CPU Scheduling Simulator allows users to:
- Select a CPU scheduling algorithm (FCFS, SJF, Priority, Round Robin, etc.).
- Input process details such as burst time, arrival time, and priority.
- Simulate and visualize process execution using Gantt charts.
- Calculate and display key performance metrics
  - ✅ Average waiting time
  - ✅ Turnaround time
  - ✅ Response time
  - ✅ CPU utilization

---

## ✨ Features
- **Multiple Scheduling Algorithms**: Supports FCFS, SJF (preemptive & non-preemptive), Priority, and Round Robin.
- **Graphical Visualization**: Displays process execution using Gantt charts.
- **Performance Metrics**: Computes and displays scheduling efficiency.
- **Modular Design**: Divided into three distinct modules for easy maintainability.
- **Interactive Interface**: Allows users to input custom processes for simulation.

---

## 🚀 How to Run It
Follow these steps to set up and run the project on your system:

### 1️⃣ Install Python 3
- Download and install **Python 3** from [python.org](https://www.python.org/).
- Ensure Python is added to your system's PATH.

### 2️⃣ Install Required Libraries
Open a terminal or command prompt and run the following command:
```sh
pip install matplotlib numpy
```

### 3️⃣ Clone or Download the Repository
To clone the repository using Git:
```sh
git clone https://github.com/your-repo-link/CPUSchedulingSimulator.git
```
Or download the ZIP file from GitHub and extract it.

### 4️⃣ Navigate to the Project Directory
```sh
cd CPUSchedulingSimulator
```

### 5️⃣ Run the Project
Execute the main script to start the simulator:
```sh
python CPU Scheduling Simulator.py
```

---

## 📂 Project Structure
The project is divided into three main modules, each responsible for a specific functionality:

- 📌 **Main Script (`CPU Scheduling Simulator.py`)**: Integrates all modules to run the simulator.

---

## 👥 Team Members and Contributions
Our team consists of three members, each responsible for one module:

- **Poorv Patidar (12322094)**: Developed the **Process Management** module.
- **Prashant Kumar (12324360)**: Developed the **CPU Scheduling Algorithms** module.
- **Veeresh A (12319252)**: Developed the **Visualization** module..

---

## 🛠️ Technologies Used
- **Python 3**: The programming language for the entire project.
- **Libraries Used**:
  - `matplotlib`: For generating Gantt charts.
  - `numpy`: For numerical computations.
- **GitHub**: For version control and collaboration.

---

## 🔄 Development Process
1. **Repository Setup**: Created a public repository on GitHub.
2. **Module Development**:
   - Each team member worked on their respective module.
   - Used multiple commits to track progress.
3. **Revisions & Integration**:
   - Ensured all modules work seamlessly together.
4. **Documentation**:
   - Created this README.md for detailed project description.

---

## 📝 Notes
- The scheduling simulation supports a configurable **time quantum** for Round Robin.
- You can stop the simulation early using **Ctrl+C** in the terminal.
- The visualization module generates a **Gantt chart** for process execution.

---

## 🔮 Future Improvements
- ✅ Add **live process execution animation**.
- ✅ Implement **interactive UI** using Tkinter or PyQt.
- ✅ Support **multi-core scheduling simulation**.
- ✅ Improve **error handling and user input validation**.

---

## 📌 GitHub Contributions
We made **5+ commits** in this repository to track our progress. Check the commit history for detailed progress!

---

### 📚 Course: CSE316  
### 🏫 Institution: Lovely Professional University  
### 📅 Date: March 27, 2025

