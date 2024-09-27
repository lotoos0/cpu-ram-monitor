import tkinter as tk
import psutil
import time
from threading import Thread
from pystray import Icon, MenuItem, Menu
from PIL import Image, ImageDraw
from datetime import datetime
import platform

# Check if the system is Linux
is_linux = platform.system() == "Linux"

# Flags for modes
night_mode = False  # Manual night mode
auto_night_mode = False  # Automatic night mode

# Function to monitor resource usage and update the widget
def update_stats(label, root):
    while True:
        cpu_usage = psutil.cpu_percent(interval=1)
        ram_usage = psutil.virtual_memory().percent

        if is_night_mode():
            label.config(bg="darkslategray", fg="lightgray")  # Night mode: background and text color
        else:
            # Change background color based on CPU and RAM usage
            if cpu_usage > 80 or ram_usage > 80:
                label.config(bg="red", fg="white")
            elif cpu_usage > 50 or ram_usage > 50:
                label.config(bg="yellow", fg="black")
            else:
                label.config(bg="green", fg="black")

        label.config(text=f'CPU: {cpu_usage}%  RAM: {ram_usage}%')

        time.sleep(1)

# Function to determine if night mode should be enabled (manual or automatic)
def is_night_mode():
    if night_mode:
        return True
    if auto_night_mode:
        current_hour = datetime.now().hour
        return 21 <= current_hour or current_hour < 6
    return False

# Function to make the window draggable
def make_draggable(widget):
    widget.bind("<Button-1>", start_drag)
    widget.bind("<B1-Motion>", drag_window)

def start_drag(event):
    widget = event.widget.winfo_toplevel()  # Get the main window
    widget._drag_data = {"x": event.x, "y": event.y}

def drag_window(event):
    widget = event.widget.winfo_toplevel()  # Get the main window
    x = widget.winfo_pointerx() - widget._drag_data["x"]
    y = widget.winfo_pointery() - widget._drag_data["y"]
    widget.geometry(f"+{x}+{y}")

# Function to create the tray icon
def create_image(color="green"):
    image = Image.new('RGB', (64, 64), color=(0, 0, 0))  # Black square
    draw = ImageDraw.Draw(image)
    draw.rectangle((16, 16, 48, 48), fill=color)  # Colorful square inside
    return image

# Function to toggle night mode
def toggle_night_mode(icon, item):
    global night_mode
    night_mode = not night_mode

# Function to toggle automatic night mode
def toggle_auto_night_mode(icon, item):
    global auto_night_mode
    auto_night_mode = not auto_night_mode

# Function to set up the system tray
def setup_tray():
    menu = Menu(
        MenuItem('Night mode (manual)', toggle_night_mode, checked=lambda item: night_mode),
        MenuItem('Automatic night mode', toggle_auto_night_mode, checked=lambda item: auto_night_mode),
        MenuItem('Quit', lambda icon, item: root.quit())
    )
    icon = Icon("CPU_RAM Monitor", create_image(), menu=menu)
    icon.run()

# Create the main window for normal mode
root = tk.Tk()
root.title("CPU and RAM Monitor")
root.geometry("150x30")
root.attributes("-topmost", True)
root.overrideredirect(True)

# Enable dragging of the window
make_draggable(root)

# Position the window in the bottom right corner of the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = screen_width - 150
y = screen_height - 70
root.geometry(f'+{x}+{y}')

# Label to display information
label = tk.Label(root, text="Fetching data...", font=("Helvetica", 10))
label.pack(fill='both', expand=True)

# Start the resource monitoring function in a separate thread
thread = Thread(target=update_stats, args=(label, root))
thread.daemon = True
thread.start()

# Start the tray icon in a separate thread (for both Linux and Windows)
tray_thread = Thread(target=setup_tray)
tray_thread.daemon = True
tray_thread.start()

# Start the main loop of the application
root.mainloop()
