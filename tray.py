import os
import sys
from pystray import Icon, MenuItem, Menu
from PIL import Image
from config_manager import load_config, reset_to_default
from utils import night_mode, auto_night_mode, toggle_night_mode, toggle_auto_night_mode
from gui import show_settings_dialog  # Import of a function displaying settings


def resource_path(relative_path):
    """ Get the absolute path to the resource, works for both development and PyInstaller builds """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


def create_image():
    # Load the appropriate icon based on the operating system
    if sys.platform == "win32":
        icon_path = resource_path('icon.ico')
    else:
        icon_path = resource_path('icon.png')  # Use PNG for Linux

    return Image.open(icon_path)


def setup_tray(root):
    menu = Menu(
        MenuItem('Night mode (manual)', lambda icon, item: toggle_night_mode(), checked=lambda item: night_mode),
        MenuItem('Automatic night mode', lambda icon, item: toggle_auto_night_mode(),
                 checked=lambda item: auto_night_mode),
        MenuItem('Settings', lambda: root.after(0, show_settings_dialog)),
        MenuItem('Reset to Default', lambda: root.after(0, lambda: reset_to_default(load_config()))),
        # Load configuration and reset settings with confirmation
        MenuItem('Quit', lambda icon, item: root.quit())
    )

    # Load the correct icon based on the platform
    icon = Icon("CPU_RAM Monitor", create_image(), menu=menu)
    icon.run()
