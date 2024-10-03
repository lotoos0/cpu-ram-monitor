import psutil
import time
import logging
from utils import is_night_mode, get_config_dir

# Get the path for monitoring.log in the same directory as config.ini (Documents/CPU_RAM_Monitor)
log_path = get_config_dir() / 'monitoring.log'

# Logging configuration to write to monitoring.log file
logging.basicConfig(
    filename=str(log_path),  # Convert Path object to string
    level=logging.INFO,  # Set logging level to INFO
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def update_stats(label, root, config):
    """
    Monitors system CPU and RAM usage and updates the Tkinter label with the stats.

    Args:
        label (tk.Label): The label widget in the Tkinter window that displays the CPU and RAM usage.
        root (tk.Tk): The root Tkinter window.
        config (configparser.ConfigParser): The loaded configuration object containing settings such as update interval and thresholds.

    Raises:
        psutil.Error: If there is an issue retrieving system stats.
        Exception: If there is an error updating the UI.
    """
    try:
        update_interval = int(config['Settings']['update_interval'])
    except (ValueError, KeyError):
        update_interval = 1  # Default value in case of error

    cpu_warning_threshold = int(config['Settings']['cpu_warning_threshold'])
    cpu_alert_threshold = int(config['Settings']['cpu_alert_threshold'])
    ram_warning_threshold = int(config['Settings']['ram_warning_threshold'])
    ram_alert_threshold = int(config['Settings']['ram_alert_threshold'])

    while True:
        try:
            # Try to retrieve CPU and RAM usage
            cpu_usage = psutil.cpu_percent(interval=1)
            ram_usage = psutil.virtual_memory().percent
        except (psutil.Error, Exception) as e:
            logging.error(f"Error retrieving system stats: {e}")
            cpu_usage, ram_usage = 0, 0  # Fallback values in case of error

        try:
            # Update UI based on night mode and thresholds
            if is_night_mode():
                label.config(bg="darkslategray", fg="lightgray")
            else:
                if cpu_usage > cpu_alert_threshold or ram_usage > ram_alert_threshold:
                    label.config(bg="red", fg="white")
                elif cpu_usage > cpu_warning_threshold or ram_usage > ram_warning_threshold:
                    label.config(bg="yellow", fg="black")
                else:
                    label.config(bg="green", fg="black")

            # Update the label with CPU and RAM usage
            label.config(text=f'CPU: {cpu_usage}%  RAM: {ram_usage}%')

        except Exception as e:
            logging.error(f"Error updating UI: {e}")

        # Dynamic update of the interval based on the latest config
        try:
            new_interval = int(config['Settings']['update_interval'])
            if new_interval != update_interval:
                logging.info(f"Update interval changed to: {new_interval} seconds.")
                update_interval = new_interval  # Update the interval dynamically
        except (ValueError, KeyError):
            logging.error("Error reading update interval from config. Using default.")

        time.sleep(update_interval)  # Use the dynamically updated interval