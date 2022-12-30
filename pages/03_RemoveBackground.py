import streamlit as st
from rembg import remove
from io import StringIO

uploaded_file = st.file_uploader('上傳')
with uploaded_file:
    data = uploaded_file.getvalue()
    file = uploaded_file.name

input_path = data
output_path = (f'rmbg{file}.png')

with open(output_path, 'wb') as o:
    output = remove(data)
    o.write(output)
#loading fun
def show(path):
    st.image(path)

ok = st.button('預覽')
if ok:
    show(output)
    
# st.download_button('Download file')
