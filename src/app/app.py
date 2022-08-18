import pandas as pd
import streamlit as st
from PIL import Image
import plotly.express as px
import plotly
import numpy as np


def plot_rankings_for_player_per_year(
    data: pd.DataFrame, player: str
) -> plotly.graph_objs._figure.Figure:
    new_dataframe = (
        data[data.p1_name == player]
        .sort_values(by=["date"], ascending=False)
        .drop_duplicates(["year"], keep="first")
    )
    fig = px.bar(
        new_dataframe, x="year", y="p1_rank", title=f"Last ranking of {player} per year"
    )
    fig.update_yaxes(autorange="reversed")
    return fig


def plot_number_of_games_per_year(
    data: pd.DataFrame, player: str
) -> plotly.graph_objs._figure.Figure:
    new_dataframe = data[data.p1_name == player]
    fig = px.histogram(
        new_dataframe,
        x="year",
        color="p1_won",
        title=f"Number of games played by {player}",
    )
    return fig


def extract_date(df: pd.DataFrame) -> pd.DataFrame:
    df["date"] = df["tourney_date"].apply(
        lambda x: pd.to_datetime(str(x), format='%Y%m%d')
    )
    df["year"] = df["tourney_date"].apply(lambda x: int(str(x)[0:4]))
    return df


def main_app():
    image = Image.open("logo.png")
    st.image(image)
    uploaded_file = st.file_uploader("Choose a CSV", type=["csv"])
    if uploaded_file is not None:
        dataframe = pd.read_csv(uploaded_file, sep=";")
        dataframe = extract_date(dataframe)
        st.write(dataframe)
        player_name = st.selectbox(
            'Choose the player of whom you wish to see the stats',
            np.sort(dataframe.p1_name.unique()),
        )
        st.plotly_chart(plot_rankings_for_player_per_year(dataframe, str(player_name)))
        st.plotly_chart(plot_number_of_games_per_year(dataframe, str(player_name)))


if __name__ == '__main__':
    main_app()
