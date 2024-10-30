from colorama import Fore

def input_error(func):
    """
    A decorator that handles common user input errors for bot commands.
    """
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return f"{Fore.RED}Error: Contact not found."
        except ValueError:
            return f"{Fore.RED}Error: Please provide valid name and phone number."
        except IndexError:
            return f"{Fore.RED}Error: Missing required arguments. Please check your input."
    return inner