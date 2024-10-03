import configparser
import logging
from tkinter import messagebox
from utils import get_config_dir

DEFAULT_SETTINGS = {
    'update_interval': 1,
    'cpu_warning_threshold': 50,
    'cpu_alert_threshold': 80,
    'ram_warning_threshold': 50,
    'ram_alert_threshold': 80
}

# Logging configuration to append messages to monitoring.log
log_path = get_config_dir() / 'monitoring.log'
logging.basicConfig(
    filename=str(log_path),  # Convert Path object to string
    level=logging.INFO,  # Set logging level to INFO
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def get_config_path():
    """Get the path to the config.ini file in the Documents directory."""
    return get_config_dir() / 'config.ini'

def load_config():
    """
    Loads the configuration from the config.ini file, applying default values if necessary.

    Returns:
        configparser.ConfigParser: The loaded configuration object with default or user-defined settings.
    """
    config_path = get_config_path()
    config = configparser.ConfigParser()

    if config_path.exists():
        config.read(config_path)
        logging.info(f"Config file loaded from {config_path} (config_manager.py)")
    else:
        # If the config file does not exist, create one with default settings
        config['Settings'] = {k: str(v) for k, v in DEFAULT_SETTINGS.items()}
        try:
            with open(config_path, 'w') as configfile:
                config.write(configfile)
            logging.info(f"Config file successfully created at {config_path} (config_manager.py)")
        except Exception as e:
            logging.error(f"Failed to create config file: {e} (config_manager.py)")
            messagebox.showerror("Error", f"Failed to create configuration file: {e}")

    # Ensure that the loaded config has all necessary settings
    for key, value in DEFAULT_SETTINGS.items():
        if key not in config['Settings']:
            config['Settings'][key] = str(value)

    return config

def update_config(config, new_settings):
    """
    Updates the configuration file with new settings provided by the user.

    Args:
        config (configparser.ConfigParser): The current configuration object.
        new_settings (dict): Dictionary containing the new settings to be updated in the config file.
    """
    try:
        # Validate new values before updating
        config['Settings'].update({k: str(v) for k, v in new_settings.items()})

        # Save changes to the config.ini file
        with open(get_config_path(), 'w') as configfile:
            config.write(configfile)
        logging.info(f"Updated config file at {get_config_path()} (config_manager.py)")

    except Exception as e:
        # Handle file write errors and notify the user
        logging.error(f"Failed to save configuration: {e} (config_manager.py)")
        messagebox.showerror("Error", f"Failed to save configuration: {e}")

def reset_to_default(config, show_message=True):
    """
    Resets the configuration settings to default values.

    Args:
        config (configparser.ConfigParser): The current configuration object to reset.
    """
    # Reset settings to default values
    config['Settings'] = {k: str(v) for k, v in DEFAULT_SETTINGS.items()}

    # Save the new configuration to the file in the correct directory
    try:
        with open(get_config_path(), 'w') as configfile:
            config.write(configfile)
        logging.info(f"Reset config file to default at {get_config_path()} (config_manager.py)")
    except Exception as e:
        logging.error(f"Failed to reset configuration: {e} (config_manager.py)")

    # Display a message about resetting the settings if the option is enabled
    if show_message:
        messagebox.showinfo("Reset to Default", "Settings have been reset to default values.")
