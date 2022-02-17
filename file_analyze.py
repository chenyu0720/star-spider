from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import pymysql
import os
import time


def save_data(today, star_name):
    total = '0'
    love = '0'
    health = '0'
    wealth = '0'
    job = '0'
    discuss = '0'
    color = ''
    lucky_numbers = ''
    match_star = ''
    summary = ''
    total_summary = ''
    love_summary = ''
    work_summary = ''
    wealth_summary = ''
    health_summary = ''

    soup = BeautifulSoup(open(os.getcwd() + '/' + today + '/' + star_name + '.html', encoding='utf-8'), 'html5lib')

    tag_1 = soup.find_all(name='dl')[1]
    tag_li = tag_1.find_all(name='li')

    # print(tag_li[3].find(name='em')['style'].replace('width:', '').replace('px;', ''))
    # print(tag_li[9])
    i = 0
    for tag in tag_li:
        i = i + 1
        if i == 1:
            total = tag.find(name='em')['style'].replace('width:', '').replace('px;', '')
        elif i == 2:
            love = tag.find(name='em')['style'].replace('width:', '').replace('px;', '')
        elif i == 3:
            job = tag.find(name='em')['style'].replace('width:', '').replace('px;', '')
        elif i == 4:
            wealth = tag.find(name='em')['style'].replace('width:', '').replace('px;', '')
        elif i == 5:
            health = tag.text.replace('健康指数：', '').replace('%', '')
        elif i == 6:
            discuss = tag.text.replace('商谈指数：', '').replace('%', '')
        elif i == 7:
            color = tag.text.replace('幸运颜色：', '')
        elif i == 8:
            lucky_numbers = tag.text.replace('幸运数字：', '')
        elif i == 9:
            match_star = tag.text.replace('速配星座：', '')
        elif i == 10:
            summary = tag.text.replace('短评：', '')

    tag_content = soup.find(name="div", attrs={"class": "c_cont"})
    i = 0
    tag_p = tag_content.find_all(name='span')
    for p in tag_p:
        i = i + 1
        text = p.text.replace('星', '').replace('座', '').replace('屋', '').replace('^', '')
        if i == 1:
            total_summary = text
        elif i == 2:
            love_summary = text
        elif i == 3:
            work_summary = text
        elif i == 4:
            wealth_summary = text
        elif i == 5:
            health_summary = text
    # print("综合：" + total_summary)
    # print("爱情：" + love_summary)
    # print("工作：" + work_summary)
    # print("财富：" + wealth_summary)
    # print("健康：" + health_summary)
    # print("综合：" + total)
    # print("爱情：" + love)
    # print("工作：" + job)
    # print("财富：" + wealth)
    # print("健康：" + health)
    # print("discuss：" + discuss)
    # print("color：" + color)
    # print("lucky_numbers：" + lucky_numbers)
    # print("match_star：" + match_star)
    # print("summary：" + summary)

    date = datetime.strptime(dir_name, "%Y-%m-%d")
    modified_date = date + timedelta(days=1)
    tomorrow = datetime.strftime(modified_date, "%Y-%m-%d")

    host = 'localhost'
    user = 'root'
    password = 'chengenfa0720~'
    # which database to use.
    db = 'renren_fast'
    conn = pymysql.connect(host=host, user=user, password=password, database=db)
    cursor = conn.cursor()

    sql = "insert into sm_fortune_star (star_name, today, total, love, job, wealth, health, discuss, color, " \
          "lucky_numbers,match_star, summary, total_summary, love_summary, work_summary, wealth_summary," \
          "health_summary)values ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}'," \
          "'{13}','{14}','{15}','{16}'); " \
        .format(star_name, tomorrow, total, love, job, wealth, health, discuss, color, lucky_numbers, match_star,
                summary, total_summary, love_summary, work_summary, wealth_summary, health_summary)
    cursor.execute(sql)
    conn.commit()
    conn.close()


dir_name = time.strftime('%Y-%m-%d', time.localtime(time.time()))
dir_files = os.listdir(dir_name)
for file in dir_files:
    save_data(dir_name, file.replace('.html', ''))

