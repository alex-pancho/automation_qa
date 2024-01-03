from pathlib import Path
import json
import logging
import xml.etree.ElementTree as ET

# task 1
""" Візміть два файли з теки
ideas_for_test/work_with_csv
порівняйте на наявність дублікатів
результат запишіть у файл result_<your_second_name>.csv
"""

path_random_csv = Path('C:/Python study Slavych/automation_qa/ideas_for_test/work_with_csv/random.csv')
path_random_michaels_csv = Path('C:/Python study Slavych/automation_qa/ideas_for_test/work_with_csv/random-michaels.csv')
result_Slavych_csv = Path('C:/Python study Slavych/automation_qa/ideas_for_test/work_with_csv/result_Slavych.csv')

uniq_elements = set()

with open(path_random_csv, 'r') as file1:
    for i in file1:
        uniq_elements.add(i)
        # print(i)

with open(path_random_michaels_csv, 'r') as file2:
    with open(result_Slavych_csv, 'w') as result:
        for a in file2:
            if a in uniq_elements:
                result.write(a)

# task 2
""" Провалідуйте, чи усі файли у папці
ideas_for_test/work_with_json
є валідними json.
результат для невалідного файлу виведіть через логер на рівні еррор
"""


logging.basicConfig(filename='errors.log', level=logging.ERROR, format='%(levelname)s: %(message)s')
folder_path_json = Path('C:/Python study Slavych/automation_qa/ideas_for_test/work_with_json')
for file_path_json in folder_path_json.glob('*.json'):
    try:
        with open(file_path_json, 'r', encoding="UTF-8") as file:
            json.load(file)
    except json.JSONDecodeError:
        logging.error(f"File {file_path_json.name} is not correct json")


# task 3
""" Для файла ideas_for_test/work_with_xml/groups.xml
створіть функцію  пошуку по group/number і далі
по значенню timingExbytes/incoming
результат пошуку виведіть через логер на рівні інфо
"""

logging.basicConfig(filename='logs.txt', level=logging.INFO)

def search_group_value_xml():
    file_xml_path = Path('C:/Python study Slavych/automation_qa/ideas_for_test/work_with_xml/groups.xml')
    try:
        tree = ET.parse(file_xml_path)
        root = tree.getroot()
        for group in root.findall('.//group'):
            number = group.attrib.get('number')
            timing_exbytes_incoming_elem = group.find('./timingExbytes/incoming')
            if timing_exbytes_incoming_elem is not None:
                timing_exbytes_incoming = timing_exbytes_incoming_elem.text
                logging.info(f"Number is {number}, timingExbytes/incoming: {timing_exbytes_incoming}")
            else:
                logging.error(f"Attribute 'timingExbytes/incoming' not found in group {number}")
    except ET.ParseError as xml_e:
        logging.error(f"Error: {xml_e}")

if __name__ == '__main__':
    search_group_value_xml()