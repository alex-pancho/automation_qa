from pathlib import Path
import json
import csv
import xml.etree.ElementTree as ET

my_path = Path("c:\\")
print([x.name for x in my_path.iterdir() if x.is_dir()])
p =  my_path / "tp_testing_code"/ "hillel" / "automation_qa_copy" / "lesson_12"
print([x.name for x in p.iterdir()])
# Methods - Перевірка існування файлів та папок, ітерування та інше
print(__file__)
current_file_path = Path(__file__)
print(current_file_path)
print(current_file_path.parts)
print(current_file_path.parent)
print(current_file_path.parent.parent)
print(current_file_path.parents[0])
print(current_file_path.parents[1])
print(current_file_path.parents[2])
print(current_file_path.parents[3])
print(current_file_path.parents[4])
print(current_file_path.parents[-2])

current_file_path = current_file_path.parent / "file.txt" #
print(current_file_path)
print(current_file_path.suffix) # розширення файлу
# print(current_file_path.parent.suffixes)
print(current_file_path.stem)  # Частина назви без розширення
print(current_file_path.name)  #  назва як є

print(Path.cwd()) # current work dir
print(Path(__file__)) # curreent file path

print(Path.home())  # user home

print(current_file_path.exists())
print(current_file_path.parent.exists())
print("Exsisting")
print(current_file_path.is_dir())
print(current_file_path.is_file())
print(current_file_path.parent.is_dir())
print(current_file_path.parent.is_file())

if current_file_path.exists():
    print(current_file_path.is_dir())
    print(current_file_path.is_file())

# print([x for x in p.parent.iterdir()])
print([x for x in current_file_path.parent.glob('*.py')])

new_dir = current_file_path.parent / "subfolder"
new_dir.mkdir(mode=0o777, parents=False, exist_ok=True)

temp2 = my_path / "temp2" / "temp"
temp2.mkdir(parents=True, exist_ok=True)

# Читання та запис у файл, режими роботи

with current_file_path.open("r", encoding="utf-8") as file:
    f = file.read()
print(f)
f = f.replace("стало", "минало")
with current_file_path.open("w", encoding="utf-8") as file:
    file.write(f)

# with current_file_path.open("a", encoding="utf-8") as file:
#     file.write("f")

my_json_file = current_file_path.parent / "try.json"
with my_json_file.open("r", encoding="utf-8") as file:
    try:
        data = json.loads(file.read())
    except json.decoder.JSONDecodeError:
        data = {}

print(data)
test_results = {"pass": 95, "skip": 5, "failed": 0}
json_test_results = json.dumps(test_results, indent=3)
print(json_test_results)

test_result_file = current_file_path.parent / "test_result.json"
with test_result_file.open("w", encoding="utf-8") as file:
    file.write(json_test_results)

csv_file = current_file_path.parent / "random-michaels.csv"
with csv_file.open() as csvfile:
    data_read = csv.reader(csvfile, delimiter=",", quotechar='"')
    for row in data_read:
        print(row)

my_xml_file = current_file_path.parent / "group.xml"
with my_xml_file.open() as xmlfile:
    x_content = xmlfile.read()

root = ET.fromstring(x_content)
# for i in root:
#     print(i.tag, i.tail, i.attrib, i.text)

number = 1
v = root.findall(f".//group[number='{number}']")
values = [ x.text for x in v ]
for child in  v:
    value = child.find('timingExbytes/micro')
    if value is None:
        raise ValueError("опис що чи чому значення нема")
    print(value.text)