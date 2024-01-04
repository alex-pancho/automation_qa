from pathlib import Path
import logging
import json
import csv
import xml.etree.ElementTree as ET


current_file_path = Path(__file__)  # homework_12.py
current_folder_path = current_file_path.parent  # lesson_12
global_folder_path = current_folder_path.parent  # automation_qa

# task 1
""" Візміть два файли з теки
ideas_for_test/work_with_csv
порівняйте на наявність дублікатів
результат запишіть у файл result_<your_second_name>.csv
"""

csv_file_01 = global_folder_path / 'ideas_for_test' / 'work_with_csv' / 'random.csv'
csv_file_02 = global_folder_path / 'ideas_for_test' / 'work_with_csv' / 'r-m-c.csv'
result_file = global_folder_path / 'ideas_for_test' / 'work_with_csv' / 'result.csv'


def find_csv_duplicates(csv_file_1, csv_file_2, output_file):
    """
    This function reads two csv files, compares for duplicates, and writes unique values to the output file.
    """
    with open(csv_file_1, 'r') as csvfile:
        data_01 = set(csvfile.readlines())
    with open(csv_file_2, 'r') as csvfile:
        data_02 = set(csvfile.readlines())

    unique_data = data_01.symmetric_difference(data_02)
    duplicates = data_01.intersection(data_02)

    with open(output_file, 'w') as file:
        for line in unique_data:
            file.write(line)

    return duplicates


resulting_duplicates = find_csv_duplicates(csv_file_01, csv_file_02, result_file)

# task 2
""" Провалідуйте, чи усі файли у папці
ideas_for_test/work_with_json
є валідними json.
результат для невалідного файлу виведіть через логер на рівні еррор
"""

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

json_file_01 = global_folder_path / 'ideas_for_test' / 'work_with_json' / 'localizations_en.json'
json_file_02 = global_folder_path / 'ideas_for_test' / 'work_with_json' / 'localizations_ru.json'
json_file_03 = global_folder_path / 'ideas_for_test' / 'work_with_json' / 'login.json'
json_file_04 = global_folder_path / 'ideas_for_test' / 'work_with_json' / 'swagger.json'


def json_files_validator(filenames: list):
    """ This function validates all json files and displays an error if the file is not json format."""
    for file in filenames:
        try:
            with open(file, 'r', encoding="utf-8") as f:
                json.load(f)
        except (json.JSONDecodeError, KeyError, AttributeError, ValueError) as e:
            logging.error(f'File "{file.name}" is not valid JSON file. Error: {e}')


json_files_validator([json_file_01, json_file_02, json_file_03, json_file_04])
# ERROR:root:File "login.json" is not valid JSON file. Error: Expecting ',' delimiter: line 8 column 1 (char 324)


# task 3
""" Для файла ideas_for_test/work_with_xml/groups.xml
створіть функцію  пошуку по group/number і далі
по значенню timingExbytes/incoming
результат пошуку виведіть через логер на рівні інфо
"""

logger = logging.getLogger('search_xml_logger')
logger.setLevel(logging.INFO)

xml_file_01 = global_folder_path / 'ideas_for_test' / 'work_with_xml' / 'groups.xml'

# FIRST SOLUTION TO THE TASK
def search_xml(file, paths):
    """ This function parse XML file and find required element. """
    tree = ET.parse(file)
    root = tree.getroot()

    for path in paths:
        elements = root.findall(path)

        for element in elements:
            logger.info(f' Element was found: {ET.tostring(element, encoding="unicode")}')


search_xml(xml_file_01, ['./group/number'])
# example of output: INFO:search_xml_logger: Element was found: <number>0</number>
search_xml(xml_file_01, ['./group/timingExbytes/incoming'])
# example of output: INFO:search_xml_logger: Element was found: <incoming>0xQUIN</incoming>


# SECOND SOLUTION TO THE TASK
def search_xml(file, path_group_by, path_value):
    """ This function parse XML file and find required element grouped by another element.
    The log will display only those values that are in the group, sorted by path_group_by. """
    tree = ET.parse(file)
    root = tree.getroot()

    for group in root.findall('group'):
        elem_1 = group.find(path_group_by)

        if elem_1 is not None:
            value_1 = elem_1.text
            elem_2 = group.find(path_value)

            if elem_2 is not None:
                value_2 = elem_2.text

                logger.info(f" Group: {value_1}, Value: {value_2}")


search_xml(xml_file_01, './number', './timingExbytes/incoming')
# example of output: INFO:search_xml_logger: Group: 0, Value: 0xQUIN