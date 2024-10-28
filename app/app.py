import os

import pandas as pd
from matplotlib import pyplot as plt
import streamlit as st

home_path = os.getcwd()
df_bp_path = os.path.join(home_path, "data", "business_performance.csv")
df_c_path = os.path.join(home_path, "data", "crossprice.csv")
df_e_path = os.path.join(home_path, "data", "df_elasticity.csv")


# Carregar os dataframes
df_bp = pd.read_csv(df_bp_path)
df_c = pd.read_csv(df_c_path)
df_e = pd.read_csv(df_e_path)


# Layout Streamlit
st.set_page_config(layout="wide")
st.header("Elasticidade de Preços dos Produtos")

tab1, tab2, tab3 = st.tabs(
    [
        "Elasticidade de Preços dos Produtos",
        "Business Performances",
        "Elasticidade Cruzada de Preços",
    ]
)

with tab1:
    tab4, tab5 = st.tabs(
        ["Elasticidade de Preços- Gráfico", "Elasticidade de Preços - Dataframe"]
    )
    with tab4:
        # Aprensentar elasticidade de preços graficamente
        st.header("Elasticidade de Preços - Grafico")
        df_e["ranking"] = (
            df_e.loc[:, "price_elasticty"].rank(ascending=True).astype(int)
        )
        df_e = df_e.reset_index(drop=True)

        fig, ax = plt.subplots(figsize=(12, 4))

        ax.hlines(
            y=df_e["ranking"],
            xmin=0,
            xmax=df_e["price_elasticty"],
            alpha=0.5,
            linewidth=3,
        )
        for name, p in zip(df_e["name"], df_e["ranking"]):
            ax.text(4, p, name)

        for x, y, s in zip(
            df_e["price_elasticty"],
            df_e["ranking"],
            df_e["price_elasticty"],
        ):
            ax.text(
                x,
                y,
                round(s, 2),
                horizontalalignment="right" if x < 0 else "left",
                verticalalignment="center",
                fontdict={"color": "red" if x < 0 else "green", "size": 10},
            )
        plt.gca().set(ylabel="Ranking Number", xlabel="Price Elasticity")
        plt.title("Price Elasticity")
        ax.grid(linestyle="--")

        st.pyplot(fig)

    with tab5:
        # Apresentar elasticiade de preços datagrame
        st.header("Elasticidade de Preços - Dataframe")
        df_order_elasticity = df_e[["ranking", "name", "price_elasticty"]].sort_values(
            by="price_elasticty", ascending=False
        )
        st.dataframe(df_order_elasticity, use_container_width=True)


with tab2:
    # apresentar business performance
    st.header("Business Performance")
    df_bp = df_bp.set_index("name")
    st.dataframe(df_bp, use_container_width=True)

with tab3:
    # apresentar elasticidade cruzada de preços
    st.header("Elasticidade Cruzada de Preços")
    df_c = df_c.set_index("name")
    st.dataframe(df_c, use_container_width=True)
