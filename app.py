import streamlit as st
import pandas as pd
import numpy as np

# App title
st.title("Streamlit Elements Demo")

# =============================
# DataFrame Section
# =============================
st.subheader("Dataframe")
chart_data = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 32, 37, 45]
})
st.dataframe(chart_data)


print(f"Type Chart data: {type(chart_data)}")
print(f"Chart data: {chart_data}")

# Bar Chart Section
st.subheader("Bar Chart")
st.bar_chart(data=chart_data.set_index("Name"))

import altair as alt

bar_chart = alt.Chart(chart_data).mark_bar().encode(
    x='Name',
    y='Age'
)

st.altair_chart(bar_chart, use_container_width=True)





