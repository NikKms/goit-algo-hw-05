import sys


def parse_logs(line: str) -> dict | None:
    """
    Parses a log line into components: date, time, log level, and message.
    """
    try:
        date, time, level, message = line.split(" ", 3)
        return {
            "date": date,
            "time": time,
            "level": level,
            "message": message.strip()
        }
    except ValueError:
        # Return None if the line does not match the expected format
        return None


def load_logs(path: str):
    """
    Loads and parses logs from a file, returning a list of valid entries.
    """
    logs = list()
    try:
        with open(path, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                entry = parse_logs(line)
                if entry:  # Only add valid entries
                    logs.append(entry)
    except FileNotFoundError:
        print(f'Error: File "{path}" not found')
    except (OSError, IOError) as error:
        print(f'Error reading file: {error}')

    return logs


def filter_logs_by_level(logs, level: str):
    """
    Filters logs by the specified log level.
    """
    level = level.casefold()
    return [log for log in logs if log["level"].casefold() == level]


def count_logs_by_level(logs):
    """
    Counts the number of logs by level.
    """
    levels_count = {}
    for log in logs:
        level = log['level']
        levels_count[level] = levels_count.get(level, 0) + 1
    return levels_count


def display_log_counts(log_counts):
    """
    Displays a table with the number of logs per level.
    """
    header_level = "Рівень логування"
    header_count = "Кількість"

    print(f"{header_level} | {header_count}")
    print("-" * (len(header_level) + len(header_count) + 3))

    for level, count in log_counts.items():
        print(f"{level:<16} | {count}")


def main():
    # Check the number of arguments
    if len(sys.argv) < 2:
        print("Usage: python main.py <file path> [log level]")
        sys.exit(1)

    file_path = sys.argv[1]
    log_level = sys.argv[2].upper() if len(sys.argv) > 2 else None

    # Load logs
    logs = load_logs(file_path)
    if not logs:
        print(f"No valid log entries found in file '{file_path}'.")
        sys.exit(1)

    # Count and display statistics
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    # Filter by level if specified
    if log_level:
        filtered_logs = filter_logs_by_level(logs, log_level)
        if filtered_logs:
            print(f"\nLog details for level '{log_level}':")
            for log in filtered_logs:
                print(f"{log['date']} {log['time']} - {log['message']}")
        else:
            print(f"No log entries found for level '{log_level}'.")


if __name__ == "__main__":
    main()
