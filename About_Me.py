import time as tm
import datetime
import calendar
import streamlit as st
import numpy as np
import pandas as pd

########################


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


########################
name = 'Ansel'
birth_y = 1998
birth_m = 1
birth_d = 2
sex = "Male"
college = "NPUST國立屏東科技大學"
github_url = "https://github.com/AnselCh?tab=repositories"
experience = ["Datavan鴻翊國際"]
jobtitle = ["Field Application Engineer"]
yy, mm, dd = cal_age(birth_y, birth_m, birth_d)
########################

st.title('About me ')

with st.container():
    st.markdown(
        f"我叫 {name}, 目前在 __{experience[0]}__ 擔任 _{jobtitle[0]}_  \n\
        接下來我會在左邊分頁加入不同功能來介紹Streamlit ")
