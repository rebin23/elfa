import requests
from datetime import datetime
token_bot = "5246650888:AAFFkF35wAiQ_pmSLpTUnprhMwCnV8mpgaI"
id_tg = "1150866732"
url = 'https://api.ipify.org'

for x in range(2000):
	proxylist = requests.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=all&timeout=750&country=all").text
	print(" Started..")
	
	for x in proxylist.splitlines():
		prox = x.split(":")[0]
		port = x.split(":")[1]
		proxies = {
		"http": "http://"+x+"/",
		"https": "http://"+x+"/"
		}
		try:
			response = requests.get(url, proxies=proxies)
			assert response.text==prox
			print(response.text)
			send_telegram = 'https://api.telegram.org/bot' + token_bot + '/sendMessage?chat_id=' + id_tg + '&parse_mode=Markdown&text=' + x
		except:
			print("Proxy does not work")


