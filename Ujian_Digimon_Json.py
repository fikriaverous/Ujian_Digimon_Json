from bs4 import BeautifulSoup
import requests
import json

req = requests.get('http://digidb.io/digimon-list/')
soup = BeautifulSoup(req.content, 'html.parser')

data = soup.find_all('td', width="5%")

digimon = []
for i in range(341):
    satu_digimon = {
    "no" : int(data[i].text),
    "digimon" : data[i].find_next_sibling().text.replace("\xa0 ",""),
    "image" : data[i].find_next_sibling().img['src'],
    "stage" : data[i].find_next_sibling().find_next_sibling().text,
    "type" : data[i].find_next_sibling().find_next_sibling().find_next_sibling().text,
    "attribute" : data[i].find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().text,
    "memory" : int(data[i].find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().text),
    "equip slots" : int(data[i].find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().text),
    "hp" : int(data[i].find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().text),
    "sp" : int(data[i].find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().text),
    "atk" : int(data[i].find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().text),
    "def" : int(data[i].find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().text),
    "int" : int(data[i].find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().text),
    "spd" : int(data[i].find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().text)
    }
    digimon.append(satu_digimon)

with open('digimon.json', 'w') as x:
    json.dump(digimon,x)