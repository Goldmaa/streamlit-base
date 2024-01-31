import streamlit as st
import streamlit_extras as stx
import streamlit_authenticator as stauth

import json
from pathlib import Path

st.set_page_config(page_title="Tamagemon", page_icon="🔥", layout="wide")


left, right = st.columns([3, 2])

def register():
	proceed = False
	logins = Path("logins.json")
	with open(logins, "r") as f:
		data = json.load(f)
		if data.get("username") is not None:
			st.error("Username already exists")
		else:
			proceed = True
		f.close()
	if proceed:
		hashed_password = stauth.Hasher(password).generate()
		st.success("Successfully registered")

logging_in = False
registering = False
with st.sidebar:
	if st.button("Login"):
		logging_in = True
	elif st.button("Register"):
		registering = True
		with st.form("register"):
			username = st.text_input("Username", key="username")
			email = st.text_input("Email", key="email")
			password = st.text_input("Password", type="password", key="password")
			registered = st.form_submit_button("Register", on_click=register)