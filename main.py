from tasks import task1, task2, task3
from modules.ui_utils import clear_screen, print_banner
from modules.language import translate, set_language
import time

# Вибір мови інтерфейсу
language = set_language()

def welcome_message(language):
    """Виводить привітання для користувача з перекладом та відліком часу."""
    clear_screen()
    print("╔════════════════════════════════════════════════════════════╗")
    print(f"║            📚 {translate('welcome', language)} 📚              ║")
    print(f"║          {translate('topic', language)}                     ║")
    print("╚════════════════════════════════════════════════════════════╝\n")
    
    for i in range(5, 0, -1):
        print(f"⏳ {i}...")
        time.sleep(1)
    print(translate("lets_go", language))
    time.sleep(1)

def main_menu():
    """Головне меню програми з псевдографікою."""
    while True:
        clear_screen()
        print_banner(translate("main_menu", language))
        print(f"🔹 [1] {translate('task1', language)}")
        print(f"🔹 [2] {translate('task2', language)}")
        print(f"🔹 [3] {translate('task3', language)}")
        print(f"🔹 [q] {translate('exit', language)}")
        print()

        choice = input(f"{translate('enter_command', language)}: ").lower()

        if choice == '1':
            task1.main(language)
        elif choice == '2':
            task2.main(language)
        elif choice == '3':
            task3.main(language)
        elif choice == 'q':
            print(translate("goodbye", language))
            break
        else:
            print(translate("unknown_command", language))
            time.sleep(1)

if __name__ == "__main__":
    welcome_message(language)
    main_menu()
