# recusion
def factorial(n):
    """Обчислює факторіал числа n."""
    if n <= 1:
        return 1
    return n * factorial(n-1)

for i in range(11):
    print(factorial(i))

from urllib.request import Request, urlopen
from urllib.parse import urlencode


url = "https://www.example.com"
response = urlopen(url)
html_content = response.read()

print(html_content)

# POST
url = "https://www.example.com"
data = {"key1": "value1", "key2": "value2"}
data = urlencode(data).encode("utf-8")  # Кодуємо дані для POST-запиту

request = Request(url, data=data, method="POST") # PUT для  пут запиту
response = urlopen(request)


html_content = response.read()
print(html_content)


