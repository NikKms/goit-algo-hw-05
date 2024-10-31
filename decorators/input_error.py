from colorama import Fore

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return f"{Fore.RED}Error: Contact not found."
        except ValueError:
            return f"{Fore.RED}Error: Error: Please provide both command, name and phone number. Usage: [command] [name] [phone]"
        except IndexError:
            return f"{Fore.RED}Error: Missing required arguments. Please check your input."
    return inner