import os
import time

def log_action(message):
    """Логує дії або результати у файл 'logs/actions.log'."""
    log_dir = "logs"
    log_file_path = os.path.join(log_dir, "actions.log")

    # Створити папку для логів, якщо вона не існує
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    try:
        with open(log_file_path, "a", encoding="utf-8") as log_file:
            log_file.write(f"{time.ctime()}: {message}\n")
    except IOError:
        print("❌ Помилка запису до файлу логів.")
