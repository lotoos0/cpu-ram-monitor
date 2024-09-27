import tkinter as tk
import psutil
import time
from threading import Thread
from pystray import Icon, MenuItem, Menu
from PIL import Image, ImageDraw
from datetime import datetime
import platform

# Sprawdzamy, czy to Linux
is_linux = platform.system() == "Linux"

# Flagi dla trybów
night_mode = False  # Tryb nocny ręczny
auto_night_mode = False  # Tryb nocny automatyczny

# Funkcja do monitorowania zużycia i zmiany widgetu
def update_stats(label, root):
    while True:
        cpu_usage = psutil.cpu_percent(interval=1)
        ram_usage = psutil.virtual_memory().percent

        if is_night_mode():
            label.config(bg="darkslategray", fg="lightgray")  # Tryb nocny: tło i kolor tekstu
        else:
            # Zmiana koloru zależnie od zużycia (tło z napisami)
            if cpu_usage > 80 or ram_usage > 80:
                label.config(bg="red", fg="white")
            elif cpu_usage > 50 or ram_usage > 50:
                label.config(bg="yellow", fg="black")
            else:
                label.config(bg="green", fg="black")

        label.config(text=f'CPU: {cpu_usage}%  RAM: {ram_usage}%')

        time.sleep(1)

# Funkcja sprawdzająca, czy włączyć tryb nocny (ręcznie lub automatycznie)
def is_night_mode():
    if night_mode:
        return True
    if auto_night_mode:
        current_hour = datetime.now().hour
        return 21 <= current_hour or current_hour < 6
    return False

# Funkcja do dynamicznego przeciągania okna
def make_draggable(widget):
    widget.bind("<Button-1>", start_drag)
    widget.bind("<B1-Motion>", drag_window)

def start_drag(event):
    widget = event.widget.winfo_toplevel()  # Uzyskaj okno główne
    widget._drag_data = {"x": event.x, "y": event.y}

def drag_window(event):
    widget = event.widget.winfo_toplevel()  # Uzyskaj okno główne
    x = widget.winfo_pointerx() - widget._drag_data["x"]
    y = widget.winfo_pointery() - widget._drag_data["y"]
    widget.geometry(f"+{x}+{y}")

# Funkcja do tworzenia ikony w tray
def create_image(color="green"):
    image = Image.new('RGB', (64, 64), color=(0, 0, 0))  # Czarny kwadrat
    draw = ImageDraw.Draw(image)
    draw.rectangle((16, 16, 48, 48), fill=color)  # Kolorowy kwadrat wewnątrz
    return image

# Funkcja zmieniająca tryb nocny
def toggle_night_mode(icon, item):
    global night_mode
    night_mode = not night_mode

# Funkcja zmieniająca tryb nocny automatyczny
def toggle_auto_night_mode(icon, item):
    global auto_night_mode
    auto_night_mode = not auto_night_mode

# Funkcja ustawiająca tray
def setup_tray():
    menu = Menu(
        MenuItem('Tryb nocny (ręczny)', toggle_night_mode, checked=lambda item: night_mode),
        MenuItem('Tryb nocny automatyczny', toggle_auto_night_mode, checked=lambda item: auto_night_mode),
        MenuItem('Quit', lambda icon, item: root.quit())
    )
    icon = Icon("CPU_RAM Monitor", create_image(), menu=menu)
    icon.run()

# Tworzenie okna aplikacji dla trybu zwykłego
root = tk.Tk()
root.title("CPU i RAM Monitor")
root.geometry("150x30")
root.attributes("-topmost", True)
root.overrideredirect(True)

# Umożliwienie przeciągania okna
make_draggable(root)

# Umieszczenie okna w prawym dolnym rogu ekranu
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = screen_width - 150
y = screen_height - 70
root.geometry(f'+{x}+{y}')

# Etykieta wyświetlająca informacje
label = tk.Label(root, text="Pobieranie danych...", font=("Helvetica", 10))
label.pack(fill='both', expand=True)

# Uruchamianie funkcji aktualizacji w osobnym wątku
thread = Thread(target=update_stats, args=(label, root))
thread.daemon = True
thread.start()

# Uruchamianie tray w osobnym wątku
if is_linux:
    tray_thread = Thread(target=setup_tray)
    tray_thread.daemon = True
    tray_thread.start()

# Uruchomienie pętli głównej aplikacji
root.mainloop()
