import streamlit as st
import numpy as np
import pandas as pd
import time as tm
import datetime
import calendar


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


st.markdown(' ')
birth = st.date_input('點選日期', min_value=datetime.date(1922, 1, 1),
                      max_value=datetime.date.today())

yy, mm, dd = cal_age(birth.year, birth.month, birth.day)
st.markdown('你現在是 __%d__ 歲 __%d__ 個月又 __%d__ 天' % (yy, mm, dd))
