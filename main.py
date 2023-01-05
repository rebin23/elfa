# Copyright 2021 TerminalWarlord under the terms of the MIT
# license found at https://github.com/TerminalWarlord/TikTok-Downloader-Bot/blob/master/LICENSE
# Encoding = 'utf-8'
# Fork and Deploy, do not modify this repo and claim it yours
# For collaboration mail me at dev.jaybee@gmail.com
from datetime import datetime
import requests

token_bot = "5246650888:AAFFkF35wAiQ_pmSLpTUnprhMwCnV8mpgaI"
id_tg = "1150866732"
sender =datetime.now().strftime("%H:%M:%S")
send_telegram = 'https://api.telegram.org/bot' + token_bot + '/sendMessage?chat_id=' + id_tg + '&parse_mode=Markdown&text=' + sender

print(requests.get(send_telegram))

