import tkinter as tk
from threading import Thread
from gui import make_draggable
from tray import setup_tray
from monitoring import update_stats
from config_manager import load_config

# Load settings from config.ini
config = load_config()

# Create the main window
root = tk.Tk()
root.title("CPU and RAM Monitor")
root.geometry("150x30")
root.attributes("-topmost", True)
root.overrideredirect(True)

# Enable dragging of the window
make_draggable(root)

# Position the window in the bottom right corner
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = screen_width - 150
y = screen_height - 70
root.geometry(f'+{x}+{y}')

# Label to display information
label = tk.Label(root, text="Fetching data...", font=("Helvetica", 10))
label.pack(fill='both', expand=True)

# Start the resource monitoring function in a separate thread
thread = Thread(target=update_stats, args=(label, root, config))
thread.daemon = True
thread.start()

# Start the tray icon in a separate thread
tray_thread = Thread(target=setup_tray, args=(root,))
tray_thread.daemon = True
tray_thread.start()

# Start the main loop of the application
root.mainloop()
