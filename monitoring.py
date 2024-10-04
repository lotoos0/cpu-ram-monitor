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


def update_stats(cpu_label, ram_label, config):
    """
    Monitors system CPU and RAM usage and updates the Tkinter labels with the stats.

    Args:
        cpu_label (tk.Label): The label widget displaying CPU usage.
        ram_label (tk.Label): The label widget displaying RAM usage.
        config (configparser.ConfigParser): The loaded configuration object containing settings such as update interval and thresholds.
    """
    try:
        update_interval = int(config['Settings']['update_interval'])
        cpu_warning_threshold = int(config['Setting']['cpu_warning_threshold'])
        cpu_alert_threshold = int(config['Settings']['cpu_alert_threshold'])
        ram_warning_threshold = int(config['Settings']['ram_warning_threshold'])
        ram_alert_threshold = int(config['Settings']['ram_alert_threshold'])

    except (ValueError, KeyError):
        # Default value in case of error
        update_interval = 1
        cpu_warning_threshold = 50
        cpu_alert_threshold = 80
        ram_warning_threshold = 50
        ram_alert_threshold = 80

    while True:
        try:
            # Try to retrieve CPU and RAM usage
            cpu_usage = psutil.cpu_percent(interval=1)
            ram_usage = psutil.virtual_memory().percent
        except (psutil.Error, Exception) as e:
            logging.error(f"Error retrieving system stats: {e}")
            cpu_usage, ram_usage = 0, 0  # Fallback values in case of error

        try:
            # Update UI based on night mode and thresholds for CPU and RAM separately
            if is_night_mode():
                cpu_label.config(bg="darkslategray", fg="lightgray")
                ram_label.config(bg="darkslategray", fg="lightgray")
            else:
                # CPU color logic
                if cpu_usage > cpu_alert_threshold:
                    cpu_label.config(bg="red")
                elif cpu_usage > cpu_warning_threshold:
                    cpu_label.config(bg="yellow")
                else:
                    cpu_label.config(bg="green")

                # RAM color logic
                if ram_usage > ram_alert_threshold:
                    ram_label.config(bg="red")
                elif ram_usage > ram_warning_threshold:
                    ram_label.config(bg="yellow")
                else:
                    ram_label.config(bg="green")

            # Update the labels with CPU and RAM usage stats
            cpu_label.config(text=f'CPU: {cpu_usage}%')
            ram_label.config(text=f'RAM: {ram_usage}%')

        except Exception as e:
            logging.error(f"Error updating UI: {e}")

        # Dynamic update of the interval, warnings and alerts based on the latest config
        try:
            new_interval = int(config['Settings']['update_interval'])
            new_cpu_warning_threshold = int(config['Settings']['cpu_warning_threshold'])
            new_cpu_alert_threshold = int(config['Settings']['cpu_alert_threshold'])
            new_ram_warning_threshold = int(config['Settings']['ram_warning_threshold'])
            new_ram_alert_threshold = int(config['Settings']['ram_alert_threshold'])

            if new_interval != update_interval:
                logging.info(f"Update interval changed to: {new_interval} seconds.")
                update_interval = new_interval  # Update the interval dynamically
            if new_cpu_warning_threshold != cpu_warning_threshold:
                logging.info(f"Update cpu_warning_threshold changed to: {new_cpu_warning_threshold} percent.")
                cpu_warning_threshold = new_cpu_warning_threshold # update dynamically
            if new_cpu_alert_threshold != cpu_alert_threshold:
                logging.info(f"cpu_alert_threshold changed to: {new_cpu_alert_threshold} percent.")
                cpu_alert_threshold = new_cpu_alert_threshold # update dynamically
            if new_ram_warning_threshold != ram_warning_threshold:
                logging.info(f"ram_alert_threshold changed to: {new_ram_warning_threshold} percent.")
                ram_warning_threshold = new_ram_warning_threshold
            if new_ram_alert_threshold != ram_alert_threshold:
                logging.info(f"ram_alert_threshold changed to: {new_ram_alert_threshold} percent.")
                ram_alert_threshold = new_ram_alert_threshold

        except (ValueError, KeyError):
            logging.error("Error reading update interval from config. Using default.")


        time.sleep(update_interval)  # Use the dynamically updated interval
