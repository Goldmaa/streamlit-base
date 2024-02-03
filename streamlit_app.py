import streamlit as st
import extra_streamlit_components as stx
import streamlit_extras as stx2
from streamlit_login_auth_ui.widgets import __login__


st.set_page_config(
    page_title="Tamagemon", page_icon="🔥", layout="wide", initial_sidebar_state="collapsed"
)

__login__obj = __login__(auth_token=st.secrets["courier_api_key"],
                         company_name="WellyCompSci",
                         width=200, height=250,
                         logout_button_name='Logout', hide_menu_bool=False,
                         hide_footer_bool=False,
                         lottie_url='https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json')

LOGGED_IN = __login__obj.build_login_ui()

if LOGGED_IN == True:

    st.header("EncrypedCookieManager:")

    @st.cache_resource(experimental_allow_widgets=True)
    def get_manager():
        return stx.CookieManager()

    cookie_manager = get_manager()

    st.subheader("All Cookies:")
    cookies = cookie_manager.get_all()
    st.write(cookies)

    with open("_secret_auth_.json", "r") as f:
        data = f.read()
        st.write(data)

    # get user email
    print(st.experimental_user.get("email"))
