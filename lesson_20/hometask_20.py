"""
### Heartbeat time testing

The client's monitoring system sends a signal that it is operational every 30 seconds. or less

Analyze the log provided to us by means of automation: ideas_for_test\heartbeat\hblog

Change the workpiece - the file hb_proces.py so that there is an analysis of the correctness of the requirements:
     for each case where heartbeat is more than 30 seconds but less than 32, a warning was logged in the file hb.log
     for each case where heartbeat has more than exactly 32 errors logged in the file hb.log

An optional part, a challenge for the most persistent:

(it does not affect the assessment, it affects self-esteem)

Consider that there are several monitoring processes and they are identified by a key, for example:

     Key TSTFEED0300
     Key TSTFEED0240

these are two different processes, respectively, to find the next "hit" the key should also be taken into account.

Consider that tomorrow you will use the file hb_proces.py for tests of many files

Remember what we learned about serialization and generators, maybe it is needed here.

(or maybe not and I will attract you) (or maybe a database in memory???)

There is a link to PR with changes to one file, everything according to the classic scenario, BUT additionally attach a log that your work will create.

The LOG MUST NOT get into PR
"""

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
