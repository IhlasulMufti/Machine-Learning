import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import pandas as pd


# 1. write() Output
st.write(pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
}))


# 2. Teks
# 2.1 Markdown()
st.markdown(
    """
    # My first app
    Hello, para calon praktisi data masa depan!
    """
)

# 2.2 title()
st.title('Belajar Analisis Data')

# 2.3 header()
st.header('Pengembangan Dashboard')

# 2.4 subheader()
st.subheader('Pengembangan Dashboard')

# 2.5 caption()
st.caption('Copyright (c) 2023')

# 2.6 code()
code = """def hello():
    print("Hello, Streamlit!")"""
st.code(code, language='python')

# 2.7 text()
st.text('Halo, calon praktisi data masa depan.')

# 2.8 latex()
st.latex(r"""
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
""")


# 3. Data Display
# 3.1 Dataframe()
df = pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})

st.dataframe(data=df, width=500, height=150)

# 3.2 table()
df = pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})
st.table(data=df)

# 3.3 metric()
st.metric(label="Temperature", value="28 °C", delta="1.2 °C")

# 3.4 jason()
st.json({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})


# 4. Chart
x = np.random.normal(15, 5, 250)

fig, ax = plt.subplots()
ax.hist(x=x, bins=15)
st.pyplot(fig)