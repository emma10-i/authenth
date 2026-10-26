import streamlit as st
import time

# Set up page configuration
st.set_page_config(page_title="Secure Login", page_icon="🔒", layout="centered")

# Custom CSS for a clean, modern UI
st.markdown("""
    <style>
    .main {
        background-color: #f9f9f9;
    }
    div.stButton > button:first-child {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        font-weight: bold;
        padding: 0.5rem 2rem;
        border-radius: 8px;
        border: none;
        width: 100%;
        transition: 0.3s;
    }
    div.stButton > button:first-child:hover {
        background-color: #45a049;
        border: none;
    }
    .auth-header {
        text-align: center;
        margin-bottom: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state variables for authentication tracking
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "auth_page" not in st.session_state:
    st.session_state.auth_page = "Login"

# Mock credentials database
USER_CREDENTIALS = {
    "admin": "password123",
    "user@example.com": "securepass"
}

def login_user(username, password):
    if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
        st.session_state.authenticated = True
        st.session_state.username = username
        st.rerun()
    else:
        st.error("❌ Invalid username or password")

def register_user(username, password, confirm_password):
    if not username or not password:
        st.error("⚠️ Fields cannot be empty")
    elif password != confirm_password:
        st.error("⚠️ Passwords do not match")
    elif username in USER_CREDENTIALS:
        st.error("⚠️ Username already exists")
    else:
        USER_CREDENTIALS[username] = password
        st.success("🎉 Registration successful! Please log in.")
        time.sleep(1)
        st.session_state.auth_page = "Login"
        st.rerun()

# --- APP ROUTING ---

# 1. Dashboard / Authenticated view
if st.session_state.authenticated:
    st.title(f"👋 Welcome back, {st.session_state.username}!")
    st.subheader("Your Secure Dashboard")
    st.write("You have successfully authenticated using Streamlit Session State.")
    
    st.info("💡 Tip: Refreshing or hitting rerun maintains your state. Clicking Logout clears it.")
    
    if st.button("Log Out"):
        st.session_state.authenticated = False
        st.session_state.username = None
        st.rerun()

# 2. Authentication flow (Login / Sign Up)
else:
    # Header area
    st.markdown("<div class='auth-header'><h1>🔒 Secure Gateway</h1><p>Sign in to access your portal</p></div>", unsafe_allow_html=True)
    
    # Toggle tabs for Login and Sign Up
    tab_login, tab_signup = st.tabs(["🔑 Sign In", "📝 Create Account"])
    
    with tab_login:
        with st.form("login_form", clear_on_submit=False):
            username = st.text_input("Username or Email Address", placeholder="e.g., admin")
            password = st.text_input("Password", type="password", placeholder="••••••••")
            submit_btn = st.form_submit_button("Sign In")
            
            if submit_btn:
                login_user(username, password)
                
    with tab_signup:
        with st.form("signup_form", clear_on_submit=False):
            new_username = st.text_input("Choose Username / Email", placeholder="e.g., user@example.com")
            new_password = st.text_input("Choose Password", type="password", placeholder="••••••••")
            confirm_password = st.text_input("Confirm Password", type="password", placeholder="••••••••")
            signup_btn = st.form_submit_button("Register Account")
            
            if signup_btn:
                register_user(new_username, new_password, confirm_password)
