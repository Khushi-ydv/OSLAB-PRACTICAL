# OS Lab 1: Process Management in Python (Jupyter Notebook)

This project contains a Jupyter Notebook (`Linux.ipynb`) that simulates and demonstrates key Linux process management operations.

## Description

The notebook is divided into five tasks, each addressing a core concept in operating systems:
1.  **Process Creation:** Creates multiple child processes and shows the parent-child PID relationship.
2.  **Command Execution:** Executes standard Linux commands like `ls`, `date`, and `whoami` from Python.
3.  **Zombie & Orphan States:** Simulates the conditions that lead to zombie (defunct) and orphan processes.
4.  **Process Inspection:** Reads data directly from the `/proc` filesystem to inspect a running process's details.
5.  **Process Prioritization:** Demonstrates the effect of `nice` values on process scheduling and includes robust error handling.

This implementation uses Python's modern `subprocess` module to ensure stable execution within a notebook environment, dynamically creating helper scripts for more complex simulations.

## How to Run

1.  **Prerequisites:** You need a Linux-based environment with Python 3 and Jupyter Notebook installed.
2.  **Launch:** Place the `Linux.ipynb` file in a directory and start a Jupyter session.
3.  **Execution:** Open the `Linux.ipynb` notebook and run the cells sequentially from top to bottom.
4.  **Helper Files:** The cells for **Task 3** and **Task 5** use the `%%writefile` command. Running these cells will automatically create the necessary helper scripts (`zombie_maker.py`, `orphan_maker.py`, etc.) in the same directory.

## File Structure

This submission includes the following files:

* `Linux.ipynb`: The main Jupyter Notebook containing all the code, explanations, and outputs.
* `output.txt`: A plain text file summarizing the output from a complete run of the notebook.
* `report.pdf`: A formal report detailing the experiment's objectives, methods, results, and conclusions.
* `README.md`: This file.