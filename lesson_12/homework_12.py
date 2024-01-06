import csv
import json
import xml.etree.ElementTree as ET
import logging
from pathlib import Path

my_path = Path("C:\\Hillel_lessons\\")

# task 1
""" Візміть два файли з теки
ideas_for_test/work_with_csv
порівняйте на наявність дублікатів
результат запишіть у файл result_<your_second_name>.csv
"""

def read_csv(file_path):
    """
    Reads a CSV file and returns the header and data as a tuple.
    """
    with open(file_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)
        data = [row for row in reader]
    return header, data


def write_csv(file_path, header, data):
    """
    Writes data to a CSV file.
    """
    with open(file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(data)


def find_duplicates(file1_data, file2_data):
    """
    Finds and returns duplicate rows between two sets of data.
    """
    file1_set = set(map(tuple, file1_data))
    file2_set = set(map(tuple, file2_data))

    duplicates_set = file1_set.intersection(file2_set)
    duplicates = list(map(list, duplicates_set))

    return duplicates

file_path1 = my_path  / "automation_qa" / "ideas_for_test" / "work_with_csv" / "r-m-c.csv"
file_path2 = my_path  / "automation_qa" / "ideas_for_test" / "work_with_csv" / "random.csv"

result_file_name = "result_litvin.csv"

header1, data1 = read_csv(file_path1)
header2, data2 = read_csv(file_path2)

duplicates = find_duplicates(data1, data2)

result_filename = result_file_name
write_csv(result_filename, header1, duplicates)

print(f"Duplicates found between {file_path1.stem} and {file_path2.stem}. Saved in {result_filename}")

# task 2
""" Провалідуйте, чи усі файли у папці
ideas_for_test/work_with_json
є валідними json.
результат для невалідного файлу виведіть через логер на рівні еррор
"""

logging.basicConfig(level=logging.ERROR)

def validate_json_file(file_path):
    """
    Validates the content of a JSON file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            json.load(file)
    except json.JSONDecodeError as e:
        logging.error(f"Невалідний JSON у файлі {file_path}")

def validate_json_files_in_directory(directory_path):
    """
    Validates all JSON files in a given directory.
    """
    for file_path in directory_path.glob('*.json'):
        validate_json_file(file_path)


folder_path = my_path  / "automation_qa" / "ideas_for_test" / "work_with_json"

validate_json_files_in_directory(folder_path)

# task 3
""" Для файла ideas_for_test/work_with_xml/groups.xml
створіть функцію  пошуку по group/number і далі
по значенню timingExbytes/incoming
результат пошуку виведіть через логер на рівні інфо
"""

logging.basicConfig(level=logging.INFO)

def search_by_group_and_timing_exbytes(file_path, group_number, timing_exbytes_value):
    """
    Searches for a specific group in an XML file based on group number and timingExbytes/incoming value.
    """
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()

        for group in root.findall(".//group[number='" + str(group_number) + "']"):
            timing_exbytes_element = group.find("timingExbytes/incoming")
            if timing_exbytes_element is not None and timing_exbytes_element.text == timing_exbytes_value:
                logging.info(f"Знайдено відповідність: group/number={group_number}, timingExbytes/incoming={timing_exbytes_value}")

    except ET.ParseError as e:
        logging.error(f"Помилка при обробці XML-файлу {file_path}")


xml_file_path = my_path  / "automation_qa" / "ideas_for_test" / "work_with_xml" / "groups.xml"


search_by_group_and_timing_exbytes(xml_file_path, 2, "0xACDC")
