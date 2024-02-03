import streamlit as st
import extra_streamlit_components as stx
import streamlit_extras as stx2
from streamlit_login_auth_ui.widgets import __login__

# Check run mode:
if st.experimental_user.get("email") == "test@example.com":
    mode = "dev"
else:
    mode = "prod"

print("Mode:", mode)

# Define page title:
page_title = ""
if page_title == "":
    raise ValueError("Please define a page title in streamlit_app.py.")

st.set_page_config(
    page_title=page_title, page_icon="🔥", layout="wide", initial_sidebar_state="collapsed"
)


# Check for API key:
try:
    st.secrets["courier_api_key"]
except KeyError:
    raise ValueError("No 'courier_api_key' secret found: define this in .streamlit/secrets.toml")

# Check for admin email:
try:
    st.secrets["admin_email"]
except KeyError:
    raise ValueError("No 'admin_email' secret found: define this in .streamlit/secrets.toml")

# Define company name:
company_name = ""
if company_name == "":
    raise ValueError("Please define a company name in streamlit_app.py.")

__login__obj = __login__(auth_token=st.secrets["courier_api_key"],
                         company_name=company_name,
                         width=200, height=250,
                         logout_button_name='Logout', hide_menu_bool=False,
                         hide_footer_bool=False,
                         lottie_url='https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json')

LOGGED_IN = __login__obj.build_login_ui()

if LOGGED_IN == True:

    if mode == "dev":
        user_email = st.secrets["admin_email"]
    elif mode == "prod":
        user_email = st.experimental_user.get("email")
    else:
        raise ValueError("Unknown mode")

    st.write(f"Hello {user_email}!")

    st.header("EncrypedCookieManager:")

    @st.cache_resource(experimental_allow_widgets=True)
    def get_manager():
        return stx.CookieManager()

    cookie_manager = get_manager()

    st.subheader("All Cookies:")
    cookies = cookie_manager.get_all()
    st.write(cookies)