🧠 OS-Process-Visualizer
A Python-based interactive simulator for visualizing Operating System process management concepts. Includes a clean GUI, multiple scheduling algorithms, and real-time visualization of process execution.



📘 Project Info
Project Name: OS-Process-Visualizer
Authors: Vaibhav, Dhruv, Mihir
Version: 1.0
License: MIT

🧩 Overview
The OS-Process-Visualizer is an educational tool built with Python to simulate and visually demonstrate key Operating System concepts, specifically process scheduling and execution.
It features an intuitive Graphical User Interface (GUI) that allows users to input process details, choose different scheduling algorithms, and watch the process flow in real time.

✨ Key Features
✅ Interactive GUI using Tkinter
✅ Multiple process scheduling algorithms:

FCFS (First-Come-First-Serve)

SJF (Shortest Job First)

Round Robin (with custom time quantum)
✅ Real-time Gantt Chart-style process visualization
✅ User-defined process inputs (arrival time, burst time, priority)
✅ Modular codebase — easy to read, extend, and maintain

🖼️ Screenshot


🛠️ Installation Guide
Follow these steps to set up and run the project locally:

1️⃣ Clone the Repository:
'''bash
git clone https://github.com/Vaibhav-0111/OS-Process-Visualizer.git
cd OS-Process-Visualizer

2️⃣ Install Dependencies
'''bash
pip install -r requirements.txt

3️⃣ Run the Application
'''bash
python main.py



📁 Project Structure
📂 OS-Process-Visualizer  
├── main.py                 # Entry point of the application  
├── gui_module.py           # Handles the GUI components  
├── process_management.py   # Core scheduling logic  
├── visualization_module.py # Process visualization logic  
├── requirements.txt        # Required libraries  
├── README.md               # Project documentation  


🧪 How to Use
Launch the app using python main.py

Enter process details like:

Arrival Time

Burst Time

(Optional) Priority

Choose a scheduling algorithm (e.g., FCFS, SJF, Round Robin)

Click Start to see a live visualization of how the processes are scheduled and executed

💻 Requirements
1)Python 3.x
2)Required libraries:
      ------>tkinter (standard GUI library for Python)
      
      ------>matplotlib

      ------->numpy

Install all required dependencies:
'''bash
pip install -r requirements.txt

🤝 Contribution
We welcome all contributions! Here's how you can contribute:

Fork the repository

Create a new branch:

bash
Copy
Edit
git checkout -b feature-branch
Make your changes and commit:

bash
Copy
Edit
git commit -m "Add feature"
Push to your fork:

bash
Copy
Edit
git push origin feature-branch
Create a Pull Request on GitHub

📜 License
This project is licensed under the MIT License.
You are free to use, modify, and distribute this software under the license terms.

📬 Contact
For questions, feedback, or collaboration:

Email: vaibhavtripathi724@gmail.com
GitHub: Vaibhav-0111

