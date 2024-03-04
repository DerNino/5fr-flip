import altair as alt
import numpy as np
import pandas as pd
import streamlit as st


st.title("Coin Flip")

st.sidebar.header("Steuerung")

chart_color = st.sidebar.selectbox("Wählen Sie eine Farbe für das Diagramm aus", ["Grün", "Blau", "Rot", "Violett", "Schwarz"])

color_mapping = {
    "Grün": "#008000",
    "Blau": "#0000FF",
    "Rot": "#FF0000",
    "Violett": "#800080",
    "Schwarz": "#000000"
}

if 'results' not in st.session_state:
    st.session_state['results'] = []

def flip_coin():
    result = "Kopf" if np.random.rand() > 0.5 else "Zahl"
    st.session_state['results'].append(result)
    
    if result == "Zahl":
        image_path = "5 Fr. Vorne.jpg"
    else:
        image_path = "5-Franken-hinten.jpg"
    
    st.image(image_path, caption=f"Ergebnis: {result}", width=200)  # Breite nach Bedarf anpassen
    return result

flip_button = st.button("Münze werfen")

if flip_button:
    flip_coin()

results_df = pd.DataFrame(st.session_state['results'], columns=["Ergebnis"])
results_count = results_df["Ergebnis"].value_counts().reset_index()
results_count.columns = ["Ergebnis", "Anzahl"]

bar_chart = alt.Chart(results_count).mark_bar().encode(
    x='Ergebnis',
    y='Anzahl',
    color=alt.value(color_mapping[chart_color])
).properties(
    width=400,
    height=300
)

st.altair_chart(bar_chart)

st.subheader("Statistik")
st.table(results_count)