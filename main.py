import requests
import webbrowser

url = "https://jsonplaceholder.typicode.com/todos"

a = requests.get(url)
a.raise_for_status()

print(a)

with open('qwerty.json', 'w') as file:
    file.write(a.text)

URL = 'qwerty.json'
webbrowser.open_new_tab(url)
