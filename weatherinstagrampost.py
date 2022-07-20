import json
import requests
from datetime import date
from PIL import Image,ImageDraw,ImageFont

api_key = "2cc35a42f8529b9a36ede188feb74c52"
position = [300,425,560,695,820]

uk_list = ["London", "Manchester", "Edinburgh", "Bristol", "Birmingham"]
india_list = ["Jaipur", "Delhi", "Mumbai", "Kolkata", "Chennai"]
us_list = ["New York", "Chicago", "San Francisco", "Los Angeles", "San Diego"]
country_list = [uk_list, india_list, us_list]

for country in country_list:
    image = Image.open('post.png')
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype('Inter.ttf', size=20)
    content = "Latest Weather Forecast"
    color = 'rgb(255, 255, 255)'
    (x, y) = (100,60)
    draw.text((x, y), content, color, font=font)

    font = ImageFont.truetype('Inter.ttf', size=20)
    content = date.today().strftime("%A - %B %d, %Y")
    color = 'rgb(255, 255, 255)'
    (x, y) = (100,150)
    draw.text((x, y), content, color, font=font)

    index = 0
    for city in country:
        url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric".format(city, api_key)
        response = requests.get(url)
        data = json.loads(response.text)

        font = ImageFont.truetype('Inter.ttf', size=20)
        color = 'rgb(0, 0, 0)'
        (x, y) = (110, position[index])
        draw.text((x, y), city, color, font=font)

        font = ImageFont.truetype('InterBlack.ttf', size=20)
        content = str(data['main']['temp']) + "\u00b0"
        color = 'rgb(255, 255, 255)'
        (x, y) = (430, position[index])
        draw.text((x, y), content, color, font=font)

        font = ImageFont.truetype('Inter.ttf', size=20)
        content = str(data['main']['humidity']) + "%"
        color = 'rgb(255, 255, 255)'
        (x, y) = (560, position[index])
        draw.text((x, y), content, color, font=font)

        index += 1
        
    image.save(str(date.today()) + country[0] + ".png")
    image_pdf = image.convert('RGB')
    image_pdf.save(str(date.today()) + country[0] + ".pdf")