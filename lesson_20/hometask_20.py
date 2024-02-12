from pathlib import Path
from datetime import datetime
from logger import logger


def extract_value(line, first_separator, second_separator):
    first_split = line.split(first_separator)
    second_split = first_split[1].split(second_separator)
    return second_split[0].strip()


filename = Path(__file__).parent.parent / "ideas_for_test" / "heartbeat" / "hblog"
with open(filename, mode="r") as file:
    old_heartbeat_timestamp = None
    for file_index, line in enumerate(file):
        heartbeat_time = extract_value(line, "Timestamp", "Key")
        heartbeat_key = extract_value(line, "Key", "|")
        heartbeat_timestamp = datetime.strptime(heartbeat_time, '%H:%M:%S')
        if old_heartbeat_timestamp is None:
            old_heartbeat_timestamp = heartbeat_timestamp
        elif heartbeat_timestamp != old_heartbeat_timestamp:
            diff_in_seconds = (old_heartbeat_timestamp - heartbeat_timestamp).seconds
            old_heartbeat_timestamp = heartbeat_timestamp
            if 30 <= diff_in_seconds < 32:
                logger.warn(f"Heartbeat in index: {file_index} and key: {heartbeat_key}, did not take more than 32 seconds")
            elif diff_in_seconds >= 32:
                logger.error(f"Heartbeat in index: {file_index} and key: {heartbeat_key}, took 32 seconds or more")
