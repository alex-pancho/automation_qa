# task 1
""" Візміть два файли з теки
ideas_for_test/work_with_csv
порівняйте на наявність дублікатів
результат запишіть у файл result_<your_second_name>.csv
"""
import path

# task 2
""" Провалідуйте, чи усі файли у папці
ideas_for_test/work_with_json
є валідними json.
результат для невалідного файлу виведіть через логер на рівні еррор
"""

# task 3
""" Для файла ideas_for_test/work_with_xml/groups.xml
створіть функцію  пошуку по group/number і далі
по значенню timingExbytes/incoming
результат пошуку виведіть через логер на рівні інфо
"""
import csv
import glob
import json
from logger import logging as log
from pathlib import Path
import xml.etree.ElementTree as ET

# task1
def csv_comparator():
    first_csv_file = Path("//Users//Artem//hw_12//ideas_for_test//work_with_csv//random.csv")
    second_csv_file = Path("//Users//Artem//hw_12//ideas_for_test//work_with_csv//rmc.csv")
    with first_csv_file.open() as file_1, second_csv_file.open() as file_2:
        f = open("test_file.csv", 'w')
        writer = csv.writer(f)
        data_1 = csv.reader(file_1, delimiter=";")
        data_2 = csv.reader(file_2, delimiter=";")
        for lines in data_2:
            if lines not in data_1:
                writer.writerow(lines)

# task2
""" Провалідуйте, чи усі файли у папці
ideas_for_test/work_with_json
є валідними json.
результат для невалідного файлу виведіть через логер на рівні еррор
"""
def verify_json():
    path = Path("//Users//Artem//hw_12//ideas_for_test//work_with_json")
    for i in path.glob("*.json"):
        pass
    else:
        log.error("invalid file founded")

# task3
""" Для файла ideas_for_test/work_with_xml/groups.xml
створіть функцію  пошуку по group/number і далі
по значенню timingExbytes/incoming
результат пошуку виведіть через логер на рівні інфо
"""


def xml_search(n):
    my_xml_filepath = Path("//Users//Artem//hw_12//ideas_for_test//work_with_xml//groups.xml")
    with my_xml_filepath.open() as xml_file:
        x_data = xml_file.read()
        root = ET.fromstring(x_data)
        number = n
        v = root.findall(f".//group[number='{number}']")
        values = [x.text for x in v]
        for child in v:
            value: object = child.find("timingExbytes/incoming")
            if value is None:
                raise ValueError("Not founded any value !")
            # print(value.text)
            log.info(value.text)

if __name__ == "__main__":
    csv_comparator()
    verify_json()
    xml_search(0)

