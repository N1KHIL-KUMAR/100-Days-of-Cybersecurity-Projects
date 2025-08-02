#!/usr/bin/python3

#module
import requests 

url = 'https://static.getimg.ai/media/getimg_ai_img-josVHBEoFF1WxfOfNCArd.jpeg'
r = requests.get(url, allow_redirects=True)
open('ai.png', 'wb').write(r.content) 
