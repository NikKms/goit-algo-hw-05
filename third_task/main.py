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


def load_logs(path: str) -> list:
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


def filter_logs_by_level(logs, level: str) -> list:
    """
    Filters logs by the specified log level.
    """
    level_lower = level.casefold()
    return list(filter(lambda log: log.get("level", "").casefold() == level_lower, logs))


def count_logs_by_level(logs) -> dict:
    """
    Counts the number of logs by level.
    """
    levels_count = {}
    for log in logs:
        level = log['level']
        levels_count[level] = levels_count.get(level, 0) + 1
    return levels_count


def display_log_counts(log_counts,
                       header_level="Level",
                       header_count="Count",
                       divider_header=" | ",
                       divider_body="-",
                       empty_message="No log data available."):
    """
    Displays a table with the number of logs per level.
    """
    if not log_counts:
        print(empty_message)
        return

    max_level_width = max(len(header_level), max((len(level) for level in log_counts), default=0))
    max_count_width = max(len(header_count), max((len(str(count)) for count in log_counts.values()), default=0))

    header = f"{header_level:<{max_level_width}}{divider_header}{header_count:<{max_count_width}}"
    separator = divider_body * (max_level_width + len(divider_header) + max_count_width)

    print(header)
    print(separator)

    for level, count in log_counts.items():
        print(f"{level:<{max_level_width}}{divider_header}{count:<{max_count_width}}")


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
    display_log_counts(counts,
                        header_level = "Рівень логування",
                        header_count = "Кількість",
                        divider_header = " | ",
                        divider_body = "-")

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
