from pystray import Icon, MenuItem, Menu
from PIL import Image, ImageDraw
from config_manager import load_config, reset_to_default
from utils import night_mode, auto_night_mode, toggle_night_mode, toggle_auto_night_mode
from gui import show_settings_dialog  # Import of a function displaying settings

def create_image(color="green"):
    image = Image.new('RGB', (64, 64), color=(0, 0, 0))
    draw = ImageDraw.Draw(image)
    draw.rectangle((16, 16, 48, 48), fill=color)
    return image

def setup_tray(root):
    menu = Menu(
        MenuItem('Night mode (manual)', lambda icon, item: toggle_night_mode(), checked=lambda item: night_mode),
        MenuItem('Automatic night mode', lambda icon, item: toggle_auto_night_mode(), checked=lambda item: auto_night_mode),
        MenuItem('Settings', lambda: root.after(0, show_settings_dialog)),
        MenuItem('Reset to Default', lambda: root.after(0, lambda: reset_to_default(load_config()))),  # Load configuration and reset settings with confirmation
        MenuItem('Quit', lambda icon, item: root.quit())
    )
    icon = Icon("CPU_RAM Monitor", create_image(), menu=menu)
    icon.run()

