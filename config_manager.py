import configparser
from tkinter import messagebox

DEFAULT_SETTINGS = {
    'update_interval': 1,
    'cpu_warning_threshold': 50,
    'cpu_alert_threshold': 80,
    'ram_warning_threshold': 50,
    'ram_alert_threshold': 80
}

def load_config():
    config = configparser.ConfigParser()
    config.read('config.ini')

    # Set defaults if the config file is missing
    if not config.has_section('Settings'):
        config['Settings'] = DEFAULT_SETTINGS

    return config


# Function to validate whether the threshold values are within the correct range
def validate_config_values(config):
    try:
        update_interval = int(config['Settings']['update_interval'])
        cpu_warning_threshold = int(config['Settings']['cpu_warning_threshold'])
        cpu_alert_threshold = int(config['Settings']['cpu_alert_threshold'])
        ram_warning_threshold = int(config['Settings']['ram_warning_threshold'])
        ram_alert_threshold = int(config['Settings']['ram_alert_threshold'])

        # Validate CPU and RAM thresholds (must be in the range of 0-100%)
        if not (0 <= cpu_warning_threshold <= 100):
            raise ValueError(f"CPU warning threshold {cpu_warning_threshold}% is out of range (0-100%).")
        if not (0 <= cpu_alert_threshold <= 100):
            raise ValueError(f"CPU alert threshold {cpu_alert_threshold}% is out of range (0-100%).")
        if not (0 <= ram_warning_threshold <= 100):
            raise ValueError(f"RAM warning threshold {ram_warning_threshold}% is out of range (0-100%).")
        if not (0 <= ram_alert_threshold <= 100):
            raise ValueError(f"RAM alert threshold {ram_alert_threshold}% is out of range (0-100%).")

    except ValueError as e:
        messagebox.showerror("Invalid Configuration", str(e))
        return False  # Return False in case of validation error

    return True  # Return True if everything is valid

def update_config(config, new_settings):
    try:
        # Validate new values before updating
        config['Settings'].update({k: str(v) for k, v in new_settings.items()})

        # Validate the new values
        if not validate_config_values(config):
            return  # Do not save the file if validation fails

        # Save changes to the config.ini file
        with open('config.ini', 'w') as configfile:
            config.write(configfile)

    except Exception as e:
        # Handle file write errors and notify the user
        messagebox.showerror("Error", f"Failed to save configuration: {e}")

def reset_to_default(config, show_message=True):
    # Reset settings to default values
    config['Settings'] = {k: str(v) for k, v in DEFAULT_SETTINGS.items()}

    # Save the new configuration to the file
    with open('config.ini', 'w') as configfile:
        config.write(configfile)

    # Display a message about resetting the settings if the option is enabled
    if show_message:
        messagebox.showinfo("Reset to Default", "Settings have been reset to default values.")
