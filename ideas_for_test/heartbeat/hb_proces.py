import re
import logging
from pathlib import Path
from datetime import datetime


logging.basicConfig(filename='BPM.log', level=logging.INFO, format='%(levelname)s: %(message)s')
filepath = Path(__file__).parent / "hblog"
with open(filepath, mode="r") as f:
    line_data = f.readlines()

def parse_timestamp(entry):
    timestamp_match = re.search(r'Timestamp (\d+:\d+:\d+)', entry)
    if timestamp_match:
        return timestamp_match.group(1)
    return None

def parse_key(entry):
    key_match = re.search(r'Key (\w+)', entry)
    if key_match:
        return key_match.group(1)
    return None

def analyze_logs(log_entries):
    for entry in log_entries:
        timestamp = parse_timestamp(entry)
        key = parse_key(entry)
        if timestamp and key:
            current_time = datetime.strptime(timestamp, '%H:%M:%S')
            if key == 'TSTFEED0300' and current_time.second > 30 and current_time.second < 32:
                logging.warning(f'Heartbeat more than 30 seconds for Key {key} at {timestamp}')
            elif key == 'TSTFEED0300' and current_time.second >= 32:
                logging.error(f'Heartbeat exactly 32 seconds or more for Key {key} at {timestamp}')

if __name__ == "__main__":
    analyze_logs(line_data)
