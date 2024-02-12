from datetime import datetime
from pathlib import Path


def process_logs(input_path, output_path, selected_key):
    last_heartbeat_time = {}

    with open(input_path, mode="r") as log_file:
        lines = log_file.readlines()

    lines.sort(key=lambda line: (line.split("Key")[1].split("Timestamp")[0], line.split("Timestamp")[1]))

    with open(output_path, mode="w") as output:
        for line in lines:
            parts = line.split()

            timestamp_str = parts[parts.index("Timestamp") + 1]
            key = parts[parts.index("Key") + 1]

            if key != selected_key:
                continue

            timestamp = datetime.strptime(timestamp_str, "%H:%M:%S").time()

            if key in last_heartbeat_time:
                time_diff = datetime.combine(datetime.today(), timestamp) - datetime.combine(datetime.today(),
                                                                                             last_heartbeat_time[key])

                if 31 < time_diff.seconds <= 32:
                    output.write(f"WARNING: {line}")
                elif time_diff.seconds > 32:
                    output.write(f"ERROR: {line}")

            last_heartbeat_time[key] = timestamp

    print(f"Analysis complete. Check file '{output_path.name}' for results.")


if __name__ == "__main__":
    filename = Path(__file__).parent / "hblog"
    output_file = Path(__file__).parent / "hb.log"
    key_log = "TSTFEED0300|7E3E|0400"

    process_logs(filename, output_file, key_log)
