from datetime import datetime
from pathlib import Path
import logging

logging.basicConfig(filename='hb.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def analyze_and_log(log_file):
    with open(log_file, mode="r") as f:
        previous_timestamps = {}
        for line in f:
            parts = line.split()
            key_index = parts.index('Key')
            key = parts[key_index + 1]

            timestamp_str = None

            for part in parts:
                if part.startswith("Timestamp"):
                    timestamp_str = " ".join(part.split()[1:])
                    break

            if timestamp_str:
                try:
                    timestamp = datetime.strptime(timestamp_str, "%H:%M:%S")
                    if key in previous_timestamps:
                        time_difference = timestamp - previous_timestamps[key]
                        if 30 < time_difference.total_seconds() < 32:
                            log_warning(key, time_difference)
                        elif time_difference.total_seconds() >= 32:
                            log_error(key, time_difference)
                    previous_timestamps[key] = timestamp
                except ValueError:
                    logging.error(f"Invalid timestamp format: {timestamp_str}")

def log_warning(key, time_difference):
    logging.warning(f"Time difference for {key} is {time_difference.total_seconds()} seconds. It should be between 30 and 32 seconds.")

def log_error(key, time_difference):
    logging.error(f"Time difference for {key} is {time_difference.total_seconds()} seconds. It should be exactly 32 seconds.")

def main():
    log_file = Path(__file__).parent / "hblog"
    analyze_and_log(log_file)

if __name__ == "__main__":
    main()

