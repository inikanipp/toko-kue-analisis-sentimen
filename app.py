import streamlit as st
import pandas as pd
import numpy as np
import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import plotly.express as px

df = pd.read_csv("preprocessing/output/data.csv")

st.set_page_config(layout="wide")

# CSS: styling box untuk container Streamlit
st.markdown("""
    <style>
    div[data-testid="stVerticalBlock"] {
        background-color: #ffffff;
        border-radius: 12px;
        padding: 20px 20px 20px 20px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.08);
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)


# Hilangkan padding bawaan Streamlit
st.markdown("""
    <style>
        .block-container {
            padding-top: 0rem;
            padding-bottom: 0rem;
            padding-left: 0rem;
            padding-right: 0rem;
        }
    </style>
""", unsafe_allow_html=True)


st.markdown(
    """
    <style>
        [data-testid="stSidebar"] {
            background-color: #1B2232; /* ganti dengan warna favorit */
            color: white;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# st.line_chart(data)
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)"),

    )

st.title("Dashboard Toko Barokah")
# Baris 2 (2 kolom)
col1, col2 = st.columns([6,3])
with col1:
    options = ["North", "East", "South", "West"]
    selection = st.segmented_control(
        "Filter", options, selection_mode="multi", key='s'
    )
    # st.markdown(f"Your selected options: {selection}.")
    # st.subheader("Kolom 1")
    # st.write("Konten kolom pertama")
    import streamlit as st
    import plotly.graph_objects as go

    # Data contoh
    months = ["Jan", "Feb", "Mar", "Apr", "May"]
    online = [5, 15, 10, 20, 5]
    store = [3, 12, 8, 25, 15]

    # Buat figure
    fig = go.Figure()

    # Online sales (orange)
    fig.add_trace(go.Scatter(
        x=months,
        y=online,
        mode='lines',
        name='Online',
        line=dict(shape='spline', color="orange", width=3),
        fill='tozeroy',   # area di bawah garis diwarnai
        fillcolor="rgba(255,165,0,0.2)"
    ))

    # Store sales (purple)
    fig.add_trace(go.Scatter(
        x=months,
        y=store,
        mode='lines',
        name='Store',
        line=dict(shape='spline', color="purple", width=3),
        fill='tozeroy',
        fillcolor="rgba(128,0,128,0.2)"
    ))

    # Layout style
    fig.update_layout(
        title="Monthly Earnings",
        # xaxis_title="Month",
        # yaxis_title="Sales",
        template="simple_white",
        height=400,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )

    st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})


with col2:
    # st.subheader("Kolom 2")
    # st.write("Konten kolom kedua")
    data = pd.DataFrame({
    "Kategori": ["A", "B", "C", "D"],
    "Jumlah": [40, 25, 20, 15]
    })

# Pie Chart
    fig = px.pie(
        data,
        values="Jumlah",
        names="Kategori",
        color_discrete_sequence=px.colors.sequential.RdBu,
        hole=0.4,  # kalau mau jadi donut chart
    )

    st.plotly_chart(fig, use_container_width=True)

   
import matplotlib.pyplot as plt
import numpy as np

col3, col4 = st.columns([6,3])

with col3 :
    options1 = ["positif", 'negatif']
    selection1 = st.segmented_control(
        "Filter", options1, selection_mode="single", key='s1'
    )
     # Contoh teks
    text = """
    Streamlit memudahkan pembuatan dashboard
    Python sangat populer untuk data science
    Word cloud bisa digunakan untuk visualisasi teks
    Streamlit mendukung matplotlib dan plotly
    """

    # Buat WordCloud
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)

    # Tampilkan
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation="bilinear")
    ax.axis("off")

    st.pyplot(fig)


