import tkinter as tk
from threading import Thread
from gui import make_draggable
from tray import setup_tray
from monitoring import update_stats
from config_manager import load_config, get_config_path
from monitoring_with_config import start_config_monitoring

# Load settings from config.ini
config_path = get_config_path()
config = load_config()

# Start monitoring config.ini
start_config_monitoring(config_path, config)

# Create the main window
root = tk.Tk()
root.title("CPU and RAM Monitor")
root.geometry("165x35")  # Adjusted window size for two sections
root.attributes("-topmost", True)
root.overrideredirect(True)

# Enable dragging of the window
make_draggable(root)

# Position the window in the bottom right corner
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = screen_width - 300  # Adjusted width for two sections
y = screen_height - 100
root.geometry(f'+{x}+{y}')

# Create two labels: one for CPU and one for RAM
cpu_label = tk.Label(root, text="CPU: 0%", font=("Helvetica", 10), bg="green", width=5, height=5)
ram_label = tk.Label(root, text="RAM: 0%", font=("Helvetica", 10), bg="green", width=5, height=5)

# Place the labels in the window (side by side)
cpu_label.pack(side="left", fill="both", expand=True)
ram_label.pack(side="right", fill="both", expand=True)

# Start the resource monitoring function in a separate thread
thread = Thread(target=update_stats, args=(cpu_label, ram_label, config))  # Update for both CPU and RAM labels
thread.daemon = True
thread.start()

# Start the tray icon in a separate thread
tray_thread = Thread(target=setup_tray, args=(root,))
tray_thread.daemon = True
tray_thread.start()

# Start the main loop of the application
root.mainloop()
