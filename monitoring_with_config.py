import os
import time
import logging
from threading import Thread
import configparser

# Funkcja do monitorowania zmian w pliku konfiguracyjnym
def monitor_config_changes(config_path, config, update_function):
    """
    Monitoruje zmiany w pliku konfiguracyjnym i aktualizuje ustawienia aplikacji w razie zmiany.

    Args:
        config_path (str): Ścieżka do pliku config.ini.
        config (configparser.ConfigParser): Obiekt konfiguracji.
        update_function (function): Funkcja aktualizująca ustawienia aplikacji.
    """
    last_modified_time = os.path.getmtime(config_path)  # Pobieramy czas modyfikacji pliku
    
    while True:
        current_modified_time = os.path.getmtime(config_path)
        if current_modified_time != last_modified_time:
            logging.info("Detected changes in config.ini. Reloading configuration.")
            config.read(config_path)
            update_function(config)
            last_modified_time = current_modified_time
        
        time.sleep(1)  # Sprawdzenie co sekundę

# Funkcja aktualizująca ustawienia aplikacji
def update_application_settings(config):
    """
    Aktualizuje ustawienia aplikacji na podstawie nowej konfiguracji.

    Args:
        config (configparser.ConfigParser): Obiekt konfiguracji z nowymi ustawieniami.
    """
    try:
        # Odczytujemy nowe wartości z pliku konfiguracyjnego
        update_interval = int(config['Settings']['update_interval'])
        logging.info(f"New update interval: {update_interval} seconds")
        
        # Tutaj można dodać więcej parametrów do aktualizacji, np. progi CPU, RAM itp.
        # cpu_warning_threshold = int(config['Settings']['cpu_warning_threshold'])
        # cpu_alert_threshold = int(config['Settings']['cpu_alert_threshold'])
        # ...
        
        # Funkcja będzie kontynuować z nowymi wartościami
        
    except Exception as e:
        logging.error(f"Error updating application settings: {e}")

# Funkcja uruchamiająca monitorowanie zmian w osobnym wątku
def start_config_monitoring(config_path, config):
    """
    Uruchamia monitorowanie pliku konfiguracyjnego w osobnym wątku.

    Args:
        config_path (str): Ścieżka do pliku config.ini.
        config (configparser.ConfigParser): Obiekt konfiguracji.
    """
    thread = Thread(target=monitor_config_changes, args=(config_path, config, update_application_settings))
    thread.daemon = True
    thread.start()

# Zakładamy, że config i config_path są już dostępne w aplikacji
def main(config_path, config):
    # Uruchom monitorowanie pliku konfiguracyjnego
    start_config_monitoring(config_path, config)

    # Inne elementy aplikacji nadal działają...
    while True:
        time.sleep(5)  # Placeholder for the application's main loop

