from datetime import datetime

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
