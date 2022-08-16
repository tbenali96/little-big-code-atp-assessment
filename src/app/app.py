import pandas as pd
import streamlit as st
from PIL import Image
import plotly.express as px
import plotly


def plot_top_best_players(data: pd.DataFrame, n: int) -> plotly.graph_objs._figure.Figure:
    data["date"] = data["tourney_date"].apply(lambda x: pd.to_datetime(str(x), format='%Y%m%d'))
    new_dataframe = data[["date", "p1_name", "p1_rank_points", "p1_age", "p1_ht", "p1_rank"]]\
        .sort_values(by=["p1_rank", "date"], ascending=[True, False])\
        .drop_duplicates(["p1_name", "p1_rank"], keep="first")\
        .head(n)
    fig = px.bar(new_dataframe, x="p1_rank_points", y="p1_name")
    st.dataframe(new_dataframe)
    return fig


image = Image.open("logo.png")
st.image(image)

uploaded_file = st.file_uploader("Choose a CSV", type=["csv"])
if uploaded_file is not None:
    dataframe = pd.read_csv(uploaded_file, sep=";")
    st.write(dataframe)
    number = st.number_input('Choose the number of top players you wish to see')
    if int(number) > 1:
        st.plotly_chart(plot_top_best_players(dataframe, int(number)))
