import os
import time
import logging
from threading import Thread
import configparser


# Function to monitor changes in the configuration file
def monitor_config_changes(config_path, config, update_function):
    """
    Monitors changes in the configuration file and updates the application settings if changes are detected.

    Args:
        config_path (str): Path to the config.ini file.
        config (configparser.ConfigParser): Configuration object.
        update_function (function): Function that updates the application's settings.
    """
    last_modified_time = os.path.getmtime(config_path)  # Get the file's last modification time

    while True:
        current_modified_time = os.path.getmtime(config_path)
        if current_modified_time != last_modified_time:
            logging.info("Detected changes in config.ini. Reloading configuration.")
            config.read(config_path)
            update_function(config)
            last_modified_time = current_modified_time

        time.sleep(1)  # Check every second


# Function to update the application's settings
def update_application_settings(config):
    """
    Updates the application's settings based on the new configuration.

    Args:
        config (configparser.ConfigParser): Configuration object with updated settings.
    """
    try:
        # Read new values from the configuration file
        update_interval = int(config['Settings']['update_interval'])

        cpu_warning_threshold = int(config['Settings']['cpu_warning_threshold'])
        cpu_alert_threshold = int(config['Settings']['cpu_alert_threshold'])

        ram_warning_threshold = int(config['Settings']['ram_warning_threshold'])
        ram_alert_threshold = int(config['Settings']['ram_alert_threshold'])



        logging.info(f"New update interval: {update_interval} seconds.")
        logging.info(f"New update cpu warning threshold: {cpu_warning_threshold} percent.")
        logging.info(f"New update cpu alert threshold: {cpu_alert_threshold} percent.")
        logging.info(f"New update ram_warning_threshold: {ram_warning_threshold} percent.")
        logging.info(f"New update ram_warning_threshold: {ram_alert_threshold} percent.")




        # Additional parameters can be updated here, e.g., CPU and RAM thresholds, etc.
        # cpu_warning_threshold = int(config['Settings']['cpu_warning_threshold'])
        # cpu_alert_threshold = int(config['Settings']['cpu_alert_threshold'])
        # ...

        # The function will continue with the new values

    except Exception as e:
        logging.error(f"Error updating application settings: {e}")


# Function to start monitoring changes in a separate thread
def start_config_monitoring(config_path, config):
    """
    Starts monitoring the configuration file in a separate thread.

    Args:
        config_path (str): Path to the config.ini file.
        config (configparser.ConfigParser): Configuration object.
    """
    thread = Thread(target=monitor_config_changes, args=(config_path, config, update_application_settings))
    thread.daemon = True
    thread.start()


# Assuming config and config_path are already available in the application
def main(config_path, config):
    # Start monitoring the configuration file
    start_config_monitoring(config_path, config)

    # Other parts of the application continue running...
    while True:
        time.sleep(5)  # Placeholder for the application's main loop
