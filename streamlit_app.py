'''
Let's expand on the first example using the Pandas Styler object to highlight some elements in the interactive table.
'''
import time as tm
from datetime import time
from datetime import datetime
import streamlit as st
import numpy as np
import pandas as pd

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))

'''
> - Streamlit also has a method for static table generation: st.table().
'''


dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
st.table(dataframe)

'''
> - You can easily add a line chart to your app with st.line_chart(). We'll generate a random sample using Numpy and then chart it.
'''


chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)

'''
> __Plot a map__
With st.map() you can display data points on a map. Let's use Numpy to generate some sample data and plot it on a map of San Francisco.
'''

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [25.09, 121.51],
    columns=['lat', 'lon'])

st.map(map_data)
'''
> - datetime slider
'''
appointment = st.slider(
    "Schedule your appointment:",
    value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)

'''
> - age
'''
age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

'''
> - selectbox
'''
'''
option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)
'''
'''
> - accessed by key
'''

st.text_input("Your name", key="name")
# You can access the value at any point with:
st.session_state.name

'''
> - Use checkboxes to show/hide data
'''

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'],
        index=[i for i in range(1, 21)])

    chart_data

'''
> __Use a selectbox for options__
'''


df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

option = st.selectbox(
    'Which number do you like best?',
    df['first column'])

'You selected: ', option


'''
> __Layout__
Streamlit makes it easy to organize your widgets in a left panel sidebar with st.sidebar. Each element that's passed to st.sidebar is pinned to the left, allowing users to focus on the content in your app while still having access to UI controls.

For example, if you want to add a selectbox and a slider to a sidebar, use st.sidebar.slider and st.sidebar.selectbox instead of st.slider and st.selectbox:
'''

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)
'''
> Beyond the sidebar, Streamlit offers several other ways to control the layout of your app. st.columns lets you place widgets side-by-side, and st.expander lets you conserve space by hiding away large content.
'''

# left_column, right_column = st.columns(2)
# # You can use a column just like st.sidebar:
# left_column.button('Press me!')

# # Or even better, call Streamlit functions inside a "with" block:
# with right_column:
#     chosen = st.radio(
#         'Sorting hat',
#         ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
#     st.write(f"You are in {chosen} house!")


'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    # Update the progress bar with each iteration.
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    tm.sleep(0.1)

'...and now we\'re done!'
