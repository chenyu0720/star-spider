import time
import os
import requests
import random
import platform


def download_star_file(star_name, star_chinese_name):
    if platform.system() == 'Windows':
        dir_name = time.strftime('%Y-%m-%d', time.localtime(time.time())) + '\\'
    else:
        dir_name = time.strftime('%Y-%m-%d', time.localtime(time.time())) + '/'
    filename = dir_name + star_chinese_name + '.html'
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    url = 'https://www.xzw.com/fortune/' + star_name + '/1.html'
    print(url)
    response = requests.get(url)
    if response.encoding == 'ISO-8859-1':
        encodings = requests.utils.get_encodings_from_content(response.text)
        if encodings:
            encoding = encodings[0]
        else:
            encoding = response.apparent_encoding
    else:
        encoding = response.encoding
    encode_content = response.content.decode(encoding, 'ignore').encode('utf-8', 'ignore')
    print(filename)
    with open(filename, 'wb') as f:
        f.write(encode_content)


star = ['aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra', 'scorpio', 'sagittarius', 'capricorn',
        'aquarius', 'pisces']
star_chinese = ['白羊', '金牛', '双子', '巨蟹', '狮子', '处女', '天秤', '天蝎', '射手', '摩羯', '水瓶', '双鱼']
i = 0
for item in star:
    download_star_file(item, star_chinese[i])
    i = i + 1
    time.sleep(random.randint(1, 5))
