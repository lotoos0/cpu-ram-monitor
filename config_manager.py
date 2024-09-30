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


def update_config(config, new_settings):
    # Aktualizujemy wartości w bieżącej konfiguracji
    config['Settings'].update({k: str(v) for k, v in new_settings.items()})

    # Zapisujemy zmiany do pliku config.ini
    with open('config.ini', 'w') as configfile:
        config.write(configfile)


from tkinter import messagebox


def reset_to_default(config, show_message=True):
    # Zresetuj ustawienia do wartości domyślnych
    config['Settings'] = {k: str(v) for k, v in DEFAULT_SETTINGS.items()}

    # Zapisz nową konfigurację do pliku
    with open('config.ini', 'w') as configfile:
        config.write(configfile)

    # Wyświetl informację o zresetowaniu ustawień, jeśli opcja jest włączona
    if show_message:
        messagebox.showinfo("Reset to Default", "Settings have been reset to default values.")
