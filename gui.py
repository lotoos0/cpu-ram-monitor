from tkinter import simpledialog
from config_manager import load_config, update_config

# Function to make the window draggable
def make_draggable(widget):
    widget.bind("<Button-1>", start_drag)
    widget.bind("<B1-Motion>", drag_window)
    
def start_drag(event):
    widget = event.widget.winfo_toplevel()
    widget._drag_data = {"x": event.x, "y": event.y}

def drag_window(event):
    widget = event.widget.winfo_toplevel()
    x = widget.winfo_pointerx() - widget._drag_data["x"]
    y = widget.winfo_pointery() - widget._drag_data["y"]
    widget.geometry(f"+{x}+{y}")


def show_settings_dialog():
    """
        Displays a settings dialog to allow the user to modify monitoring parameters
        (update interval, CPU and RAM warning and alert thresholds).

        The current settings are loaded from the configuration file and displayed in
        the dialog boxes. If the user provides new values, the configuration file is updated.
        """
    # Load the current configuration every time the settings dialog is opened
    config = load_config()

    # Get current values from the configuration
    update_interval = int(config['Settings']['update_interval'])
    cpu_warning_threshold = int(config['Settings']['cpu_warning_threshold'])
    cpu_alert_threshold = int(config['Settings']['cpu_alert_threshold'])
    ram_warning_threshold = int(config['Settings']['ram_warning_threshold'])
    ram_alert_threshold = int(config['Settings']['ram_alert_threshold'])

    # Display dialog windows with current values
    new_update_interval = simpledialog.askinteger("Settings", "Update interval (seconds):", initialvalue=update_interval)
    new_cpu_warning_threshold = simpledialog.askinteger("Settings", "CPU warning threshold (%):", initialvalue=cpu_warning_threshold)
    new_cpu_alert_threshold = simpledialog.askinteger("Settings", "CPU alert threshold (%):", initialvalue=cpu_alert_threshold)
    new_ram_warning_threshold = simpledialog.askinteger("Settings", "RAM warning threshold (%):", initialvalue=ram_warning_threshold)
    new_ram_alert_threshold = simpledialog.askinteger("Settings", "RAM alert threshold (%):", initialvalue=ram_alert_threshold)

    # Check if the user provided new values and update them
    if all(v is not None for v in [new_update_interval, new_cpu_warning_threshold, new_cpu_alert_threshold, new_ram_warning_threshold, new_ram_alert_threshold]):
        # Update the config.ini file
        update_config(config, {
            'update_interval': new_update_interval,
            'cpu_warning_threshold': new_cpu_warning_threshold,
            'cpu_alert_threshold': new_cpu_alert_threshold,
            'ram_warning_threshold': new_ram_warning_threshold,
            'ram_alert_threshold': new_ram_alert_threshold
        })
