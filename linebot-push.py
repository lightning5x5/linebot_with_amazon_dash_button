#!/usr/bin/env python3

from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError


line_bot_api = LineBotApi('<channel access token>')

try:
    line_bot_api.push_message('<to>', TextSendMessage(text='Hello, I\'m testing now.'))
except LineBotApiError as e:
    print(e.status_code)
    print(e.error.message)
    print(e.error.details)
