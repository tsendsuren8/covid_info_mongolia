'''
2020/nov/24 12:04PM
J U S T F O R F U N
'''
import requests
from scrapy.selector import Selector
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

print("       \n              COVID-19 СТАТИСТИК ")
print("-----------------------------------------------")
print("|  Бүртгэгдсэн  |  Эдгэрсэн  |   Нас барсан   |")
print("-----------------------------------------------")
print(f"|     {cases}      |    {recovered}     |        {death}       |")
print("-----------------------------------------------")

