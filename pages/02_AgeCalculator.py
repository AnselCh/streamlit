import streamlit as st
import datetime
import calendar
import requests
from bs4 import BeautifulSoup

# 算年齡


def cal_age(year, month, day):
    today = datetime.date.today()
    yy = today.year - year
    mm = today.month - month
    if month < 0:
        yy = yy - 1
        mm = 12 + mm
        day_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if calendar.isleap(today.year):         # 判斷如果是閏年
        day_list[1] = 29                    # 就將二月份的天數改成 29 天
    dd = today.day - day
    if dd < 0:
        mm = mm - 1
    if mm < 0:
        yy = yy - 1
        mm = 12 + mm
        dd = day_list[month] + dd

    return yy, mm, dd


#########################
# 算星座
iAstro = ''


def star_judge(month, day):
    if (month == 1 and day > 20) or (month == 2 and day < 19):
        iAstro = 'iAstro=10'
        return ("Aquarius水瓶座"), iAstro
    elif (month == 2 and day > 18) or (month == 3 and day < 21):
        iAstro = 'iAstro=11'
        return ("Pisces雙魚座"), iAstro
    elif (month == 3 and day > 20) or (month == 4 and day < 21):
        iAstro = 'iAstro=0'
        return ("Aries牡羊座"), iAstro
    elif (month == 4 and day > 20) or (month == 5 and day < 22):
        iAstro = 'iAstro=1'
        return ("Taurus金牛座"), iAstro
    elif (month == 5 and day > 21) or (month == 6 and day < 22):
        iAstro = 'iAstro=2'
        return ("Gemini雙子座"), iAstro
    elif (month == 6 and day > 21) or (month == 7 and day < 23):
        iAstro = 'iAstro=3'
        return ("Cancer巨蟹座"), iAstro
    elif (month == 7 and day > 22) or (month == 8 and day < 24):
        iAstro = 'iAstro=4'
        return ("Leo獅子座"), iAstro
    elif (month == 8 and day > 23) or (month == 9 and day < 24):
        iAstro = 'iAstro=5'
        return ("Virgo 處女座"), iAstro
    elif (month == 9 and day > 23) or (month == 10 and day < 24):
        iAstro = 'iAstro=6'
        return ("Libra天秤座"), iAstro
    elif (month == 10 and day > 23) or (month == 11 and day < 23):
        iAstro = 'iAstro=7'
        return ("Scorpio天蠍座"), iAstro
    elif (month == 11 and day > 22) or (month == 12 and day < 22):
        iAstro = 'iAstro=8'
        return ("Sagittarius射手座"), iAstro
    elif (month == 12 and day > 21) or (month == 1 and day < 21):
        iAstro = 'iAstro=9'
        return ("Capricorn摩羯座"), iAstro


# 接收前端選擇的日期，開始帶入年齡與星座函式
def app():

    st.header("AgeCalculator")

    today = datetime.date.today()  # 今天

    birth = st.date_input('請點選日期', min_value=datetime.date(1922, 1, 1),
                          max_value=today)  # 點選生日

    yy, mm, dd = cal_age(birth.year, birth.month, birth.day)  # 計算年齡

    ss, iAstro = star_judge(birth.month, birth.day)  # 判斷星座
    #############
    # 開始爬蟲，網址帶入今天日期星座
    response = requests.get(
        f"https://astro.click108.com.tw/daily_10.php?iAcDay={today}&{iAstro}")

    soup = BeautifulSoup(response.text, "html.parser")
    today_content = soup.find('div', class_='TODAY_CONTENT')
    # 將接收的資料整理
    head = today_content.find('h3').text
    t_all = today_content.find_all('p')[0].text
    t_all2 = today_content.find_all('p')[1].text
    t_love = today_content.find_all('p')[2].text
    t_love2 = today_content.find_all('p')[3].text
    t_business = today_content.find_all('p')[4].text
    t_business2 = today_content.find_all('p')[5].text
    t_money = today_content.find_all('p')[6].text
    t_money2 = today_content.find_all('p')[7].text
    #############

    if birth != today:
        st.markdown(''' >  __%d__ 歲 __%d__ 個月又 __%d__ 天
                        %s''' % (yy, mm, dd, ss))
        st.text("")  # 空行

        star_analyze = st.checkbox('顯示星座分析')

    st.text("")
    if birth != today:
        if star_analyze:
            st.markdown(f'''##### **{head}**''')
            st.markdown(f''' > __{t_all}__ {t_all2}''')
            st.markdown(f''' > __{t_love}__ {t_love2}''')
            st.markdown(f''' > __{t_business}__ {t_business2}''')
            st.markdown(f''' > __{t_money}__ {t_money2}''')


app()
