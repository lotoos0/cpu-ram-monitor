import tkinter as tk
from tkinter import messagebox
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
    # Ładujemy aktualną konfigurację za każdym razem, gdy otwieramy okno dialogowe
    config = load_config()

    # Pobieramy aktualne wartości z konfiguracji
    update_interval = int(config['Settings']['update_interval'])
    cpu_warning_threshold = int(config['Settings']['cpu_warning_threshold'])
    cpu_alert_threshold = int(config['Settings']['cpu_alert_threshold'])
    ram_warning_threshold = int(config['Settings']['ram_warning_threshold'])
    ram_alert_threshold = int(config['Settings']['ram_alert_threshold'])

    # Wyświetlamy okna dialogowe z aktualnymi wartościami
    new_update_interval = simpledialog.askinteger("Settings", "Update interval (seconds):", initialvalue=update_interval)
    new_cpu_warning_threshold = simpledialog.askinteger("Settings", "CPU warning threshold (%):", initialvalue=cpu_warning_threshold)
    new_cpu_alert_threshold = simpledialog.askinteger("Settings", "CPU alert threshold (%):", initialvalue=cpu_alert_threshold)
    new_ram_warning_threshold = simpledialog.askinteger("Settings", "RAM warning threshold (%):", initialvalue=ram_warning_threshold)
    new_ram_alert_threshold = simpledialog.askinteger("Settings", "RAM alert threshold (%):", initialvalue=ram_alert_threshold)

    # Sprawdzamy, czy użytkownik podał nowe wartości i je aktualizujemy
    if all(v is not None for v in [new_update_interval, new_cpu_warning_threshold, new_cpu_alert_threshold, new_ram_warning_threshold, new_ram_alert_threshold]):
        # Aktualizacja pliku config.ini
        update_config(config, {
            'update_interval': new_update_interval,
            'cpu_warning_threshold': new_cpu_warning_threshold,
            'cpu_alert_threshold': new_cpu_alert_threshold,
            'ram_warning_threshold': new_ram_warning_threshold,
            'ram_alert_threshold': new_ram_alert_threshold
        })
