import requests
from bs4 import BeautifulSoup
import time

def request():
  name = "sister"
  search_url = "https://gapo.glitch.me/search"
  search_params = {
      "q": name,  
      "p": "1",
  }

  # x = requests.get(f'https://gapo.glitch.me/?q={name}&p=1')
  response = requests.get(search_url, params=search_params)
  print(response.url)
  data = response.json()

      # حالا اگر داده‌ها مشابه داده‌هایی باشند که شما ارسال کردید
      # مانند یک لیست از ویدیوها، می‌توانیم آن‌ها را به صورت دیکشنری پردازش کنیم
  link = []
  image = []
  videoo = []
  titlee = []
  for video in data:
      lin = video[0]  # عنوان ویدیو
      title = video[1]  # عنوان ویدیو
      duration = video[2]  # مدت زمان ویدیو
      image_link = video[3]  # لینک تصویر
      video_link = video[4]  # لینک ویدیو

      # نمایش داده‌ها
      link.append('https://gapo.glitch.me'+lin)
      image.append(image_link)
      videoo.append(video_link)
      titlee.append(title)
  else:
      print(f"Error: {response.status_code}")
  
  return link,image,videoo,titlee
