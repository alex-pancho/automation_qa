from pathlib import Path
import json
import csv
import xml.etree.ElementTree as ET
from logger import logger as log

current_lesson_path = Path(__file__).parent
idea_for_test_folder = current_lesson_path.parent / "ideas_for_test"

# task 1
"""
Візміть два файли з теки
ideas_for_test/work_with_csv
порівняйте на наявність дублікатів
результат запишіть у файл result_<your_second_name>.csv
"""

idea_for_test_csv_folder = idea_for_test_folder / "work_with_csv"
csv_file_1 = idea_for_test_csv_folder / "random-michaels.csv"
csv_file_2 = idea_for_test_csv_folder / "random.csv"
csv_out_file = current_lesson_path / "result_viki.csv"

# Find duplicate lines and write in the file
with csv_file_1.open() as csv_file_1, csv_file_2.open() as csv_file_2, csv_out_file.open(mode='w') as out_file:
    data_read_1 = csv.reader(csv_file_1, delimiter=",", quotechar='"')
    next(data_read_1, None)  # skip the headers
    data_read_2 = list(csv.reader(csv_file_2, delimiter=",", quotechar='"'))  # Put CSV element in a list
    data_read_2.pop(0)  # remove the headers
    csv_writer = csv.writer(out_file, delimiter=",", quotechar='"')
    for row in data_read_1:
        # Convert to string for comparison
        row_as_string = ''.join(row).strip()
        duplicate_row = False
        for row_2 in data_read_2:
            # Convert to string for comparison
            row_2_as_string = ''.join(row_2).strip()
            if row_as_string == row_2_as_string:
                duplicate_row = True
                break
        if duplicate_row:
            csv_writer.writerow(row)

# task 2
""" 
Провалідуйте, чи усі файли у папці
ideas_for_test/work_with_json
є валідними json.
результат для невалідного файлу виведіть через логер на рівні еррор
"""

idea_for_test_json_folder = idea_for_test_folder / "work_with_json"

for file in idea_for_test_json_folder.iterdir():
    if file.is_file():
        with file.open("r", encoding="utf-8") as json_file:
            try:
                data = json.loads(json_file.read())
            except json.decoder.JSONDecodeError:
                log.error(f"Invalid json file: {file}")

# task 3
""" 
Для файла ideas_for_test/work_with_xml/groups.xml
створіть функцію  пошуку по group/number і далі
по значенню timingExbytes/incoming
результат пошуку виведіть через логер на рівні інфо
"""


def search_in_xml(xml_root: ET.Element, group_number: int, search_element: str = "timingExbytes/incoming"):
    v = xml_root.findall(f".//group[number='{group_number}']/{search_element}")
    values = [x.text for x in v]
    if len(values) == 0:
        log.info(f"No '{search_element}' element found for group number '{group_number}'")
    else:
        log.info(f"group {group_number} value for timingExbytes/incoming element: {values}")


idea_for_test_xml_folder = idea_for_test_folder / "work_with_xml"
xml_groups_file = idea_for_test_xml_folder / "groups.xml"

with xml_groups_file.open() as xml_file:
    xml_content = xml_file.read()

root = ET.fromstring(xml_content)

search_in_xml(root, 0)
search_in_xml(root, 1)
search_in_xml(root, 2)
search_in_xml(root, 3)

