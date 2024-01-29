import random

import streamlit as st

st.set_page_config(page_title="Tamagemon", page_icon="🔥", layout="wide")

st.title("Tamagemon")

st.header("A Tamagotchi-Pokemon game for the web")
st.write("By Alex Goldman")

st.subheader("Guide")

st.write("""Welcome to Tamagemon!
		 This is a game where you can raise a Tamagotchi-Pokemon hybrid.
		 You can feed it, play with it, and train it to battle other Tamagemon.
		 You can also battle other Tamagemon yourself!""")