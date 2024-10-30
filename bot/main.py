from colorama import Fore
from decorators.input_error import input_error

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    if len(args) < 2:
        return f"{Fore.RED}Error: Please provide both name and phone number. Usage: add [name] [phone]"

    name, phone = args
    contacts[name] = phone
    return f"{Fore.GREEN}Contact {name} added."

@input_error
def change_contact(args, contacts):
    if len(args) < 2:
        return f"{Fore.RED}Error: Please provide both name and new phone number. Usage: change [name] [new phone]"

    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return f"{Fore.GREEN}Contact {name} updated."
    else:
        return f"{Fore.RED}Error: Contact {name} not found."

@input_error
def show_phone(args, contacts):
    if len(args) == 0:
        return f"{Fore.RED}Error: Please provide name. Usage: phone [name]"

    name = args[0]
    if name in contacts:
        return f"{Fore.GREEN}{name}: {contacts[name]}"
    else:
        return f"{Fore.RED}Error: {name} not found."

@input_error
def show_all(contacts):
    if not contacts:
        return f"{Fore.YELLOW}No contacts found."

    res = []
    for name, phone in contacts.items():
        res.append(f"{Fore.CYAN}{name}: {Fore.GREEN}{phone}")
    return "\n".join(res)

def show_help():
    return f"""{Fore.BLUE}Available commands:
    {Fore.CYAN}hello - greet the bot
    {Fore.CYAN}add [name] [phone] - add a new contact
    {Fore.CYAN}change [name] [new phone] - change the phone number of an existing contact
    {Fore.CYAN}phone [name] - show the phone number of a contact
    {Fore.CYAN}all - show all contacts
    {Fore.CYAN}close/exit - exit the bot
    """

def main():
    contacts = {}
    print(f"{Fore.MAGENTA}Welcome to the assistant bot! \n{Fore.YELLOW}Type 'help' to see available commands or 'hello' to get started.")

    while True:
        user_input = input(f"{Fore.CYAN}Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print(f"{Fore.MAGENTA}Good bye!")
            break
        elif command == "hello":
            print(f"{Fore.MAGENTA}How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        elif command == "help":
            print(show_help())
        else:
            print(f"{Fore.RED}Invalid command. Type 'help' to see available commands.")

if __name__ == "__main__":
    main()