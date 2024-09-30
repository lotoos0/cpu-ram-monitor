import psutil
import time
import logging
from utils import is_night_mode

# Logging configuration
logging.basicConfig(
    filename='monitoring.log',  # Log file where messages will be saved
    level=logging.INFO,  # Logging level set to INFO
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def update_stats(label, root, config):
    # Load configuration settings
    update_interval = int(config['Settings']['update_interval'])
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
            # Log the error instead of printing it
            logging.error(f"Error retrieving system stats: {e}")
            cpu_usage, ram_usage = 0, 0  # Fallback values in case of error

        try:
            # Update UI depending on night mode and thresholds
            if is_night_mode():
                label.config(bg="darkslategray", fg="lightgray")
            else:
                if cpu_usage > cpu_alert_threshold or ram_usage > ram_alert_threshold:
                    label.config(bg="red", fg="white")
                elif cpu_usage > cpu_warning_threshold or ram_usage > ram_warning_threshold:
                    label.config(bg="yellow", fg="black")
                else:
                    label.config(bg="green", fg="black")

            # Update the label text with CPU and RAM usage
            label.config(text=f'CPU: {cpu_usage}%  RAM: {ram_usage}%')

        except Exception as e:
            # Log the error instead of printing it
            logging.error(f"Error updating UI: {e}")

        time.sleep(update_interval)
