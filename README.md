# 🖥️ CPU and RAM Monitor
A simple cross-platform application built with Python and Tkinter to monitor CPU and RAM usage in real-time. The app supports both manual and automatic night mode, allows dynamic window dragging, and includes a system tray icon with various options.

# ✨ Features
* Real-time monitoring of CPU and RAM usage.
  * Night Mode: Switch to a darker theme.
  * Manual mode: toggle it from the tray.
* Automatic mode: enables between 9 PM and 6 AM.
* System Tray Icon: Control the app directly from the tray with options to:
  * Toggle manual night mode.
  * Enable/disable automatic night mode.
  * Quit the application.
* Draggable Window: Move the window freely across the screen.
* Cross-platform compatibility: Runs on Windows and Linux.

# 🛠️ Requirements
Make sure you have the following installed:

* Python 3.x
* Python packages:
  * [tkinter](https://docs.python.org/3/library/tkinter.html) (usually pre-installed)
  * [psutil](https://pypi.org/project/psutil/)
  * [pystray](https://pypi.org/project/pystray/)
  * [Pillow](https://pillow.readthedocs.io/)

# 🔧 Installation
1. Clone the repository:
   ```
   git clone https://github.com/lotoos0/cpu-ram-monitor
   cd cpu-ram-monitor
   ```
2. Install the dependencies:
   For Windows:
   ```
   pip install psutil pystray pillow
   ```
   For Linux:
   ```
   sudo apt-get install python3-tk python3-psutil python3-pil
   ```
3. Run the application:
   ```
   python main.py
   ```
# 📜 License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/lotoos0/CpuRamTracker/blob/main/LICENSE) file for details.
