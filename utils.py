from datetime import datetime
import os
from pathlib import Path


night_mode = False
auto_night_mode = False

def is_night_mode():
    try:
        if night_mode:
            return True
        if auto_night_mode:
            current_hour = datetime.now().hour
            return 21 <= current_hour or current_hour < 6
    except Exception as e:
        print(f"Error determining night mode: {e}")
    return False

def toggle_night_mode():
    global night_mode
    night_mode = not night_mode

def toggle_auto_night_mode():
    global auto_night_mode
    auto_night_mode = not auto_night_mode

def get_config_dir():
    """
    Get or create the configuration directory in the user's Documents folder.
    On Windows, it uses the Documents folder inside USERPROFILE.
    On Linux, it uses the ~/Documents/CPU_RAM_Monitor folder.
    """
    if os.name == 'nt':  # Windows
        config_dir = Path(os.getenv('USERPROFILE')) / 'Documents' / 'CPU_RAM_Monitor'
    else:  # Linux and others
        config_dir = Path.home() / 'Documents' / 'CPU_RAM_Monitor'

    # Create the directory if it doesn't exist
    config_dir.mkdir(parents=True, exist_ok=True)
    return config_dir
