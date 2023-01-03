import streamlit as st
from rembg import remove
from io import StringIO
import time
uploaded_file = st.file_uploader('上傳')
file = ''
switch = 0
col1, col2 = st.columns([2, 19])


def load(picture):
    with st.spinner('removing background...'):
        global file
        with picture:
            data = picture.getvalue()
            file = picture.name[:-4:]

        input_path = data
        output_path = (f'rmbg{file}.png')

        with open(output_path, 'wb') as o:
            rm_pic = remove(input_path)
            o.write(rm_pic)
        switch = 1
    return rm_pic, switch


if uploaded_file:
    rm_pic, switch = load(uploaded_file)


# button
if switch == 1:
    with col1:
        ok = st.button('預覽')

    if ok:
        st.image(rm_pic)

if file:
    with col2:
        download = st.download_button(
            label='Download file', data=rm_pic, file_name=f'{file}.png')
