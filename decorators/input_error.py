from colorama import Fore

def input_error(func):
    """
    A decorator that handles common user input errors for bot commands.
    """
    def inner(*args, **kwargs):
        try:
            result =  func(*args, **kwargs)
            if result is None or result == "":
                return f"{Fore.YELLOW}😱 Nothing found."
            return result
        except KeyError:
            return f"{Fore.RED}Error: Contact not found."
        except ValueError:
            return f"{Fore.RED}Error: Error: Please provide both command, name and phone number. Usage: [command] [name] [phone]"
        except IndexError:
            return f"{Fore.RED}Error: Missing required arguments. Please check your input."
    return inner