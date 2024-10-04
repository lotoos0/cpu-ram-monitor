# 🖥️ *CPU and RAM Monitor*
This project is a lightweight CPU and RAM monitor built with Python and Tkinter. The application displays real-time system statistics (CPU and RAM usage) in a floating window and includes a system tray icon for managing settings like night mode, update intervals, and more.

# ✨ *Features*
* **Real-time monitoring** of CPU and RAM usage.
  * **Night Mode**: Switch to a darker theme.
    * **Manual mode**: toggle it from the tray.
    * **Automatic mode**: enables between 9 PM and 6 AM.
* **System Tray Icon**: Control the app directly from the tray with options to:
  * Toggle manual night mode.
  * Enable/disable automatic night mode.
  * Open settings dialog.
  * Reset settings to default.
  * Quit the application.
* **Draggable Window**: Move the window freely across the screen.
* **Customizable thresholds** for CPU and RAM alerts (set via config file or settings dialog).
* **Dynamic configuration updates**: Automatically apply changes from the config file (such as update intervals and CPU/RAM thresholds) in real time without restarting the app.
* **Background split into two sections**: One section for CPU and one for RAM. The color of each section changes based on the respective usage.
* **Cross-platform compatibility**: Runs on Windows and Linux.

# 🔧 *Planned Bug Fixes*
  - Fix display of options in the tray menu on Linux.

# 🐞 *Bug Fixes and Small Improvements*
  * ~~Hotfix: Corrected config loading from config.ini to apply custom user settings.~~
  * ~~Fixed compatibility on Linux~~
  * ~~Change the background color based on usage in regular mode~~
  * ~~Increased the window width slightly to improve text alignment and appearance~~
  * ~~Applied real-time dynamic updates for all monitored settings.~~
    
# 🚀 *Planned Features*
 * Add a checkmark next to the active option in the tray, e.g., auto night mode (9-6).
 * ~~Split the background into two sections: one for CPU and one for RAM. The color of each section will change based on the respective CPU or RAM usage.~~
 * ~~Save configuration and logs to user-specific directories.~~

# 🛠️ *Requirements*
Make sure you have the following installed:

* **Python 3.x**
* **Python packages**:
  * [tkinter](https://docs.python.org/3/library/tkinter.html) (usually pre-installed)
  * [psutil](https://pypi.org/project/psutil/)
  * [pystray](https://pypi.org/project/pystray/)
  * [Pillow](https://pillow.readthedocs.io/)


# 🔧 *Installation*
### Option 1: Download the pre-built files (recommended)

If you don't want to set up the development environment, you can download the pre-built application from the [Releases](https://github.com/lotoos0/cpu-ram-monitor/releases) section.

1. For **Windows**:
   - Download `cpu_ram_monitor_v1.0.exe` from the latest release.
   - Double-click the `.exe` file to run the application.

2. For **Linux**:
   - Download `cpu_ram_monitor_v1.0_linux.tar.gz` from the latest release.
   - Extract the file:
     ```bash
     $ tar -xzf cpu_ram_monitor_v1.0_linux.tar.gz
     ```
   - Run the binary:
     ```bash
     $ ./cpu_ram_monitor
     ```
### Option 2: Clone the repository and set up the environment

1. **Clone the repository**:

   ```bash
   $ git clone https://github.com/lotoos0/cpu-ram-monitor
   $ cd cpu-ram-monitor
   ```
2. Set up a virtual environment (optional, but recommended):
   ```bash
   $ python -m venv venv
   $ source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install the dependencies:
    * For Windows:
      ```
      $ pip install -r requirements.txt
      ```
    * For Linux:
      ```
      $ sudo apt-get install python3-tk python3-psutil python3-pil
      ```
 4. Configure the config.ini file:
    * Ensure there is a config.ini file in the root of the project. A default configuration might look like this:
      ```
      [Settings]
      update_interval = 1
      cpu_warning_threshold = 50
      cpu_alert_threshold = 80
      ram_warning_threshold = 50
      ram_alert_threshold = 80
      ```
      * These settings can be updated either manually in the file or through the application's settings dialog.
5. Run the application:
   ```bash
   $ python main.py
   ```
# ⚙️ *Usage*
 * **Floating Window:** The application shows a small floating window displaying the real-time CPU and RAM usage.
 * **Draggable Window:** You can move the window freely across the screen by clicking and dragging.
 * **System Tray:** The tray icon provides quick access to:
   * **Night Mode:** Toggle manual night mode or enable/disable automatic night mode.
   * **Settings:** Open the settings dialog to adjust monitoring parameters.
   * **Reset to Default:** Restore all settings to their default values.
   * **Quit:** Exit the application.

# ⚙️ *Configuration*
  The application uses a ```config.ini``` file for its settings. These include:
  * ```update_interval:``` How often (in seconds) the CPU and RAM usage stats are updated.
  * ```cpu_warning_threshold:``` CPU usage percentage that triggers a warning (yellow background).
  * ```cpu_alert_threshold:``` CPU usage percentage that triggers an alert (red background).
  * ```ram_warning_threshold:``` RAM usage percentage that triggers a warning (yellow background).
  * ```ram_alert_threshold:``` RAM usage percentage that triggers an alert (red background).
    
  You can either edit this file manually or change the settings via the application’s settings dialog.
       
# 📜 License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/lotoos0/CpuRamTracker/blob/main/LICENSE) file for details.
