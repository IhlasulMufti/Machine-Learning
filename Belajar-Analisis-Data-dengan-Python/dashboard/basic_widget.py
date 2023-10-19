import streamlit as st
import pandas as pd
import datetime


# 1. Input Widget
# 1.1 Text Input
name = st.text_input(label='Nama lengkap', value='')
st.write('Nama: ', name)

# 1.2 Text Area
text = st.text_area('Feedback')
st.write('Feedback: ', text)

# 1.3 Number Input
number = st.number_input(label='Umur')
st.write('Umur: ', int(number), ' tahun')

# 1.4 Date Input
date = st.date_input(label='Tanggal lahir', min_value=datetime.date(1900, 1, 1))
st.write('Tanggal lahir:', date)

# 1.5 File Uploader
uploaded_file = st.file_uploader('Choose a CSV file')

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)

# 1.6 Camera Input
picture = st.camera_input('Take a picture')
if picture:
    st.image(picture)



# 2. Button Widget
# 2.1 Button
if st.button('Say hello'):
    st.write('Hello there')

# 2.2 Checkbox
agree = st.checkbox('I agree')

if agree:
    st.write('Welcome to MyApp')

# 2.3 Radio Button
genre = st.radio(
    label="What's your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary'),
    horizontal=False
)

# 2.4 Select Box
genre2 = st.selectbox(
    label="What's your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary')
)

# 2.5 Multiselect
genre3 = st.multiselect(
    label="What's your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary')
)

# 2.6 Slider
values = st.slider(
    label='Select a range of values',
    min_value=0, max_value=100, value=(0, 100))
st.write('Values:', values)
