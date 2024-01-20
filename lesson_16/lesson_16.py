import json
import math
import os
import random
import re
import sys

from datetime import datetime
from collections import OrderedDict
from urllib import request


def greeting(name:str) -> str:
    return f"Hello, {name}"

def square(x:int) -> int:
    return x ** 2

# __all__ = [] # "greeting", "square" # пустий __all__ забороняє модуль вього

if __name__ == "__main__":
    print(math.pi)
    now = datetime.now()
    print(now)
    random_number = random.randint(1, 10)
    print(random_number)
    print(os.name)
    print(sys.version)
    pattern = re.compile(r'\b\w+\b')
    text = "Hello, world!"
    matches = pattern.findall(text)
    print(matches)
    response = request.urlopen('https://www.example.com')
    html = response.read()
    print(html)

    my_dict = {'b': 1, 'c': 2, 'a': 3}
    ordered_dict = OrderedDict(my_dict)
    print(ordered_dict)
    print(__file__)
    print(json.__file__)
    print(request.__file__)
    print(__name__)
    print(__cached__)

    # pip freeze > requirements.txt
    # pip install -r requirements.txt