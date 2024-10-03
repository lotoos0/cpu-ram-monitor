# *CPU and RAM Monitor CHANGELOG*

## [v1.0.2] - Features & Bug Fixes & Improvements 
### 1. HotFix: Corrected config loading from config.ini file to apply custom user settings.
    - Fixed an issue where the application was not loading custom settings from config.ini and was using default values (e.g., 1-second interval). Ensured the app now correctly reads user-defined settings like update interval.
### 2. Feature: Added config file monitoring to dynamically apply updated settings during runtime
    - Introduced a feature to monitor changes in the config.ini file. The application now detects and applies any updates to settings (such as the update interval) dynamically while running, without the need for a restart.
### 3. Fix: Implemented dynamic update of monitoring interval based on config changes
    - Modified the resource monitoring function to dynamically adjust the update interval based on changes detected in config.ini. The monitoring loop now uses the updated interval without requiring a restart of the application.