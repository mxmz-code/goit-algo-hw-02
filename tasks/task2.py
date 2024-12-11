from modules.ui_utils import clear_screen, print_banner, pause
from modules.language import translate, set_language
from modules.logger import log_action
from collections import deque
import random
import string
from colorama import init, Fore, Style

# Инициализация colorama
init(autoreset=True)

def is_palindrome(text):
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    char_deque = deque(cleaned_text)

    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    return True

def show_examples(language):
    examples = [
        "madam",
        "racecar",
        "radar",
        "A man, a plan, a canal, Panama",
        "Я несу гусеня"
    ]
    print(f"\n{translate('palindrome_examples', language)}")
    for example in examples:
        print(f"🔹 {Fore.CYAN}{example}{Style.RESET_ALL}")
    input(translate("press_enter", language))

def generate_random_string(language):
    length = random.randint(5, 10)
    random_str = ''.join(random.choices(string.ascii_letters, k=length))
    print(f"\n{translate('random_string', language)}: {Fore.CYAN}{random_str}{Style.RESET_ALL}")
    result = is_palindrome(random_str)
    status = Fore.GREEN + translate("palindrome", language) if result else Fore.RED + translate("not_palindrome", language)
    print(f"{status}\n")
    log_action(f"Generated string '{random_str}' -> {status}")
    input(translate("press_enter", language))

def main(language):
    while True:
        clear_screen()
        print_banner(translate("task2", language))
        print(f"🔹 [1] {translate('enter_text', language)}")
        print(f"🔹 [2] {translate('show_examples', language)}")
        print(f"🔹 [3] {translate('generate_random', language)}")
        print(f"🔹 [l] {translate('change_language', language)}")
        print(f"🔹 [q] {translate('exit', language)}")
        print()

        choice = input(f"{translate('enter_command', language)}: ").strip().lower()

        if choice == '1':
            text = input(f"{translate('enter_text', language)}: ").strip()
            if not text:
                print(Fore.RED + translate("empty_input", language))
                input(translate("press_enter", language))
                continue

            result = is_palindrome(text)
            status = Fore.GREEN + translate("palindrome", language) if result else Fore.RED + translate("not_palindrome", language)
            print(f"\n{status}\n")
            log_action(f"Checked text '{text}' -> {status}")
            input(translate("press_enter", language))

        elif choice == '2':
            show_examples(language)

        elif choice == '3':
            generate_random_string(language)

        elif choice == 'l':
            language = set_language()
            input(translate("press_enter", language))

        elif choice == 'q':
            print(Fore.GREEN + translate("goodbye", language))
            log_action(translate("goodbye", language))
            break

        else:
            print(Fore.RED + translate("unknown_command", language))
            input(translate("press_enter", language))

if __name__ == "__main__":
    language = set_language()
    main(language)
