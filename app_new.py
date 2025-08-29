import streamlit as st
import pandas as pd
import numpy as np
import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import random
import joblib

komentar = []
classification = []

st.set_page_config(layout="wide")

navbar_html = """
<style>
.navbar1 {
  background: #F86A69;
  border-radius: 12px;
  padding: 12px 24px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  color: white;
  font-family: Arial, sans-serif;
  margin-top:5rem
}
.navbar1 .nav-links {
  display: flex;
  gap: 20px;
}
.navbar1 a {
  color: white;
  text-decoration: none;
  font-weight: 500;
  padding: 6px 12px;
  border-radius: 8px;
  transition: background 0.3s;
}
.navbar1 a:hover {
  background: rgba(255,255,255,0.2);
}
.brand {
  font-size: 20px;
  font-weight: bold;
}
</style>

<div class="navbar1">
  <div class="brand">Toko Kue</div>
  <div class="nav-links">
    <a href="#home">Home</a>
    <a href="#wd">World Cloud</a>
    <a href="#wd">Proporsi</a>
  </div>
</div>
"""

st.markdown(navbar_html, unsafe_allow_html=True)

df = pd.read_csv("preprocessing/output/data.csv")

# =========================================== Styling Text Box ======================================================================
st.markdown("""
    <style>
    div[data-testid="stVerticalBlock"] {

        border-radius: 12px;
        padding: 20px 20px 20px 20px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.08);
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# =========================================== Hapus Padding ======================================================================

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


# =========================================== ganti warna sidebar ======================================================================

st.markdown(
    """
    <style>
        [data-testid="stSidebar"] {
            background-color: #A07FE6; /* ganti dengan warna favorit */
            color: white;
        }
    </style>
    """,
    unsafe_allow_html=True
)

vectorizer = joblib.load("./models/tfidf_vectorizer.pkl")
model = joblib.load("./models/logreg_model.pkl")

# ================== PREDICT FUNCTION ==================
def predict_label(text):
    X = vectorizer.transform([text])
    y_pred = model.predict(X)[0]
    return y_pred

# st.line_chart(data)
# Simpan riwayat chat
if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:

    # Input pesan
    if user_input := st.chat_input("Ketik pesan..."):
        label = predict_label(user_input)
        st.session_state.messages.append((user_input, label))

    # with st.container(col):
    # Tampilkan riwayat
        for text, label in reversed(st.session_state.messages):
            if label == "positif" :
                st.success(text)
            if label == "netral" :
                st.warning(text)
            if label == "negatif" :
                st.error(text)
        # st.write(f"**{text}** → {label}")
# =========================================== end side bar ======================================================================


# ========================================================= BODY ==================================================================

# row1_col1, row1_col2 = st.columns([4])
# inject CSS untuk custom segmented control

# with row1_col1 :
options = ["Lapis Legit Spesial", "Kue Lapis Legit Kismis", 
           "Kue Lapis Surabaya", "Bolu Gulung", 
           "Pinggiran Kue Lapis" , "Kue Lapis Legit Spesial 17x17cm"]
selection = st.segmented_control(
    "Filter", options, selection_mode="single", key='s'
)

st.markdown(
    """
    <style>
    /* Warna tombol default */
    div[data-baseweb="segmented_control"] button {
        background-color: #f5f5f5;
        color: black;
        border-radius: 8px;
    }

    /* Warna tombol saat aktif */
    div[data-baseweb="segmented_control"] button[aria-checked="true"] {
        background-color: #2ecc71; /* hijau */
        color: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)
ket = '0'

df['date'] = df['date'].astype('datetime64[ns]')
df['month'] = df['date'].dt.month
df['year'] = df['date'].dt.year

df_group = df.groupby(['month','year'])['label'].value_counts()
df_group = df_group.reset_index()

if selection == "Lapis Legit Spesial" :
    ket = 'Lapis Legit Spesial Basah Harum Gurih Legit Halal'
    df_group = df[df['title'] == 'Lapis Legit Spesial Basah Harum Gurih Legit Halal'].groupby(['month','year'])['label'].value_counts()
    df_group = df_group.reset_index()

elif selection == "Kue Lapis Legit Kismis" :
    ket = 'Kue Lapis Legit Kismis 17x17 Makanan Camilan Enak Murah'
    df_group = df[df['title'] == 'Kue Lapis Legit Kismis 17x17 Makanan Camilan Enak Murah'].groupby(['month','year'])['label'].value_counts()
    df_group = df_group.reset_index()

elif selection == "Kue Lapis Surabaya" :
    ket = 'Kue Lapis Surabaya 22x22cm'
    df_group = df[df['title'] == 'Kue Lapis Surabaya 22x22cm'].groupby(['month','year'])['label'].value_counts()
    df_group = df_group.reset_index()

elif selection == "Bolu Gulung" :
    ket = 'Bolu Gulung Roll Cake Selai Strawberry'
    df_group = df[df['title'] == 'Bolu Gulung Roll Cake Selai Strawberry'].groupby(['month','year'])['label'].value_counts()
    df_group = df_group.reset_index()

elif selection == "Pinggiran Kue Lapis" :
    ket = 'Pinggiran Kue Lapis Legit 400gram'
    df_group = df[df['title'] == 'Pinggiran Kue Lapis Legit 400gram'].groupby(['month','year'])['label'].value_counts()
    df_group = df_group.reset_index()

elif selection == "Kue Lapis Legit Spesial 17x17cm" :
    ket = 'Kue Lapis Legit Spesial 17x17cm'
    df_group = df[df['title'] == 'Kue Lapis Legit Spesial 17x17cm'].groupby(['month','year'])['label'].value_counts()
    df_group = df_group.reset_index()
else :
    df_group = df.groupby(['month','year'])['label'].value_counts()
    df_group = df_group.reset_index()



# Gabungkan month dan year jadi satu kolom (timeline)
# Gabungkan month dan year jadi datetime
df_group["periode"] = pd.to_datetime(df_group["year"].astype(str) + "-" + df_group["month"].astype(str))

pivot_df = df_group.pivot_table(
    index="periode",
    columns="label",
    values="count",
    aggfunc="sum"
).reset_index().fillna(0)

# Urutkan periode
pivot_df = pivot_df.sort_values("periode")

colors = ["#F86A69","#F99C59","#A07FE6",  "#F9C80E", "#9B5DE5"]
# Plot
fig = go.Figure()
for i, label in enumerate (pivot_df.columns[1:]):
    fig.add_trace(go.Scatter(
        x=pivot_df["periode"],
        y=pivot_df[label],
        mode='lines+markers',
        name=label,
        fill='tozeroy',
        line=dict(shape='linear', width=2, color=colors[i % len(colors)]),
    ))

fig.update_layout(
    title="Analysis Sentiment",
    # xaxis_title="Month",
    # yaxis_title="Sales",
    template="simple_white",
    height=400,
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
)

# Tampilkan di Streamlit
st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})


navbar_html = """
<style>
.navbar {
  background: #F86A69;
  border-radius: 12px;
  padding: 12px 24px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  color: white;
  font-family: Arial, sans-serif;
  margin-bottom:3rem
}
.navbar .nav-links {
  display: flex;
  gap: 20px;
}
.navbar a {
  color: white;
  text-decoration: none;
  font-weight: 500;
  padding: 6px 12px;
  border-radius: 8px;
  transition: background 0.3s;
}
.navbar a:hover {
  background: rgba(255,255,255,0.2);
}
.brand {
  font-size: 20px;
  font-weight: bold;
}
</style>

<div class="navbar" id="wd">
  <div class="brand">Word Cloud & Proporsi Sentiment </div>
  
</div>
"""

st.markdown(navbar_html, unsafe_allow_html=True)

row2_col1, row2_col2 = st.columns([5,3])

with row2_col1:
    
    ket1 = '0'

    options1 = ["positif", 'negatif']
    selection1 = st.segmented_control(
        "Filter", options1, selection_mode="single", key='s1'
    )


    text = " ".join(df["comment_segmented"].astype(str))

    if ket != '0' :
        if selection1 :
            df_comment = df[(df['title'] == ket) & (df['label'] == selection1)]
            text = " ".join(df_comment["comment_segmented"].astype(str))
    else :
        if selection1 :
            df_comment = df[df['label'] == selection1]
            text = " ".join(df_comment["comment_segmented"].astype(str))
    

    def random_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
        colors = ["#A07FE6", "#F86A69", "#F99C59"]  # merah, biru, hijau
        return random.choice(colors)

    # Buat WordCloud
    wordcloud = WordCloud(width=800, height=400, background_color="white",color_func=random_color_func).generate(text)

    # Tampilkan
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation="bilinear")
    ax.axis("off")

    st.pyplot(fig)


with row2_col2 :
    df_group_pie = df['label'].value_counts()
    df_group_pie = df_group_pie.reset_index()

    if selection == "Lapis Legit Spesial" :
        ket = 'Lapis Legit Spesial Basah Harum Gurih Legit Halal'
        df_group_pie = df[df['title'] == 'Lapis Legit Spesial Basah Harum Gurih Legit Halal']['label'].value_counts()
        df_group_pie = df_group_pie.reset_index()

    elif selection == "Kue Lapis Legit Kismis" :
        ket = 'Kue Lapis Legit Kismis 17x17 Makanan Camilan Enak Murah'
        df_group_pie = df[df['title'] == 'Kue Lapis Legit Kismis 17x17 Makanan Camilan Enak Murah']['label'].value_counts()
        df_group_pie = df_group_pie.reset_index()

    elif selection == "Kue Lapis Surabaya" :
        ket = 'Kue Lapis Surabaya 22x22cm'
        df_group_pie = df[df['title'] == 'Kue Lapis Surabaya 22x22cm']['label'].value_counts()
        df_group_pie = df_group_pie.reset_index()

    elif selection == "Bolu Gulung" :
        ket = 'Bolu Gulung Roll Cake Selai Strawberry'
        df_group_pie = df[df['title'] == 'Bolu Gulung Roll Cake Selai Strawberry']['label'].value_counts()
        df_group_pie = df_group_pie.reset_index()

    elif selection == "Pinggiran Kue Lapis" :
        ket = 'Pinggiran Kue Lapis Legit 400gram'
        df_group_pie = df[df['title'] == 'Pinggiran Kue Lapis Legit 400gram']['label'].value_counts()
        df_group_pie = df_group_pie.reset_index()

    elif selection == "Kue Lapis Legit Spesial 17x17cm" :
        ket = 'Kue Lapis Legit Spesial 17x17cm'
        df_group_pie = df[df['title'] == 'Kue Lapis Legit Spesial 17x17cm']['label'].value_counts()
        df_group_pie = df_group_pie.reset_index()
    else :
        df_group_pie = df['label'].value_counts()
        df_group_pie = df_group_pie.reset_index()



    custom_colors = ['#A07FE6',  # hijau untuk positif
                 '#F86A69',  # kuning untuk netral
                 '#F99C59']
    # Pie chart
    fig = go.Figure(
        data=[
            go.Pie(
                labels=df_group_pie['label'],
                values=df_group_pie['count'],
                hole=0.3,  # opsional -> untuk donut chart
                pull=[0.05]*len(df_group_pie),  # tarik semua slice sedikit biar rapi
                marker=dict(colors=custom_colors)
            )
        ]
    )

    fig.update_layout(
        title="Proporsi Sentimen",
        showlegend=True
    )

    # Tampilkan di Streamlit (bukan fig.show())
    st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
