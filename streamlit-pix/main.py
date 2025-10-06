import streamlit as st
import pandas as pd
import altair as alt

st.write("## FIR Data")
df = pd.read_csv("./firs.csv")
st.dataframe(df)

bar_chart=(
    alt.Chart(df).mark_bar().encode(
    x=alt.X("Year:O", title="Year"),
    y=alt.Y("FIRs:Q", title="Number of FIRs"),
    tooltip=["Year","FIRs"]
    )
    .properties(
    title="Number of FIRs Registered (2020–2025)"
)
)

st.altair_chart(bar_chart)


