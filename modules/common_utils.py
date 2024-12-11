import os
import time

def clear_screen():
    """Очищає екран для кращої візуалізації."""
    os.system('cls' if os.name == 'nt' else 'clear')

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

def print_banner(title):
    """Друкує банер програми з динамічним заголовком."""
    print("╔════════════════════════════════════════╗")
    print(f"║     🖥️  {title} 🖥️       ║")
    print("╚════════════════════════════════════════╝\n")

def display_status(container, container_name):
    """Відображає статус контейнера (черги, стеку або deque)."""
    print(f"📊 Статус {container_name}:")
    if not container:
        print(f"🔹 {container_name} порожній.")
    else:
        print(f"🔹 Кількість елементів у {container_name}: {len(container)}")
        print(f"🔹 Елементи у {container_name}:")
        for item in container:
            print(f"   ➡️ {item}")
    print()
