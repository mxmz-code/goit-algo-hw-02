from modules.ui_utils import clear_screen, print_banner, pause
from modules.language import translate, set_language
from modules.logger import log_action
from queue import Queue
import random
from colorama import init, Fore, Style

# Инициализация colorama
init(autoreset=True)

def generate_request(queue, language):
    if queue.full():
        print(Fore.YELLOW + translate("queue_full", language))
    else:
        request_id = f"request-{random.randint(1000, 9999)}"
        print(Fore.GREEN + f"✅ {translate('request_created', language)}: {request_id}")
        queue.put(request_id)
        log_action(f"Created {request_id}")

def process_request(queue, language):
    if queue.empty():
        print(Fore.YELLOW + translate("queue_empty", language))
    else:
        request_id = queue.get()
        print(Fore.CYAN + f"⚙️  {translate('processing_request', language)}: {request_id}")
        log_action(f"Processing {request_id}")
        print(Fore.GREEN + f"✅ {translate('request_processed', language)}: {request_id}")

def queue_status(queue, language):
    if queue.empty():
        print(Fore.YELLOW + translate("queue_empty", language))
    else:
        print(Fore.CYAN + translate("current_queue", language))
        for item in list(queue.queue):
            print(f"🔹 {item}")

def main(language):
    queue = Queue(maxsize=5)

    while True:
        clear_screen()
        print_banner(translate("task1", language))
        print(f"🔹 [g] {translate('create_request', language)}")
        print(f"🔹 [p] {translate('process_request', language)}")
        print(f"🔹 [s] {translate('queue_status', language)}")
        print(f"🔹 [l] {translate('change_language', language)}")
        print(f"🔹 [q] {translate('exit', language)}")
        print()

        command = input(f"{translate('enter_command', language)}: ").strip().lower()

        if command == 'g':
            generate_request(queue, language)
            input(translate("press_enter", language))
        elif command == 'p':
            process_request(queue, language)
            input(translate("press_enter", language))
        elif command == 's':
            queue_status(queue, language)
            input(translate("press_enter", language))
        elif command == 'l':
            language = set_language()
            input(translate("press_enter", language))
        elif command == 'q':
            print(Fore.GREEN + translate("goodbye", language))
            log_action(translate("goodbye", language))
            break
        else:
            print(Fore.RED + translate("unknown_command", language))
            input(translate("press_enter", language))

if __name__ == "__main__":
    language = set_language()
    main(language)
