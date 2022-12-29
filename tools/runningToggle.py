import streamlit as st
import numpy as np
import pandas as pd


def runningToggle(bool):
    if bool == True:
        hide_streamlit_style = """
              <style>

              div[class='css-4z1n4l ehezqtx5']{
                background: rgba(0, 0, 0, 0.3);
                color: #fff;
                border-radius: 15px;
                height: 40px;
                max-width: 160px;


                position: fixed;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                width: 50%;
              }

              </style>
              """
        st.markdown(hide_streamlit_style, unsafe_allow_html=True)
