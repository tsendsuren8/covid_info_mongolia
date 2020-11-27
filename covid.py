'''
2020/nov/24 12:04PM
J U S T F O R F U N
'''
import requests
from scrapy.selector import Selector
import datetime
import PySimpleGUI as sg
url = "https://www.worldometers.info/coronavirus/country/mongolia/"
request = requests.get(url)
response = str(request.text)
result = Selector(text=response).css("div.maincounter-number").extract()
for index, value in enumerate(result):
	if index == 2:
		recovered = Selector(text=value).xpath("//span/text()").get()
	elif index == 0:
		cases = Selector(text=value).xpath("//span/text()").get()
	elif index == 1:
		death = Selector(text=value).xpath("//span/text()").get()
date = datetime.datetime.now()
date = date.strftime("%x")
sg.theme("Dark")
layout = [
[sg.Text(f"{date} -ны байдлаар")],
[sg.Text(f"  Тохиолдол: {cases}")],
[sg.Text(f"  Эдгэрсэн: {recovered}")],
[sg.Text(f"  Нас барсан: {death}")]]
window = sg.Window("😷 COVID-19 СТАТИСТИК 🇲🇳", layout, size=(400,140), font=('Roboto', 14))
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == sg.WIN_CLOSED:
        break
window.close()