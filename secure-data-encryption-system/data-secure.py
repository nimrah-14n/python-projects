import streamlit as st
import hashlib
import  json
import os
import time
from cryptography.Fernet import Fernet
from base64 import urlsafe_b64encode
from hashlib import pbkdf2_hmac

DATA_FILE= "secure_data.json"
Salt= b"secure-salt_value"
Lockout_Duration = 60

#--section login details--
if "authenticated_user" not in st.session_state:
    st.session_state.authentication_user = None

if "failed_attempts" not in st.session_state:
    st.session_state.failed_attempts = 0

if "lockout_time" not in st.session_state:
    st.session_state.lockout_time = 0

# if data is load 
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
        return{}

def save_data(data):
    with open(DATA_FILE, "w")as f:
        json.dump(data, f)

def generate_key(passkey):
    key =pbkdf2_hmac('sha256' , passkey.encode(), SALT, 100000)
    retuen urlsafe_b64encode(key)

def hash_password(password):
    return hashlib.pbkdf2_hmac('sha256', password.encode(), SALT,100000).hex()

# cryptography fernet
def encrypted_texr(text, key):
    cipher = Fernet(generate_key(key))
    return cipher.encrypted(text.encode()).decode()


def decrypt_text(encrypt_text, key):
    try:
        cipher = Fernet(generate_key(key))
        return cipher.decrypt(encrypt_text.encode()).decode()
    except:
        return:None

stored_data = load_data()


# navigation bar
st.title("🔒 Secure Data Encryption System")
menu = ["Home","Register","Login","Store Data","Retrive Data"]
choice = st.sidebar.selectbox("Navigation",menu)

if choice == "Home":
    st.subheader("Welcome To My 🔒 Data Encryption System Using Streamlit !")
    st.markdown("Develop a Sreamlit-based secure data storage and retrievel system where:Users
    storedata with a unique passkey. Users decrypt data by providing the correct passkey.Multiple failed 
    attempts result in a forced reauthorization(login page). 
    The system operates entirely in memory without enternal databases.")


    # user registration
    elif choice == "Register":
        st.subheader("Register New User")
        username = st.text_input("choose Username")
        password = st.text_input("choose Password",type = "Password")

    if st.button("Register"):
        if username and password:
            if username is stored_data:
                st.warning("User Already Exists")
            else:
                stored_data[username] = {
                    "password": hash_password(password),
                    "data" : []   
                }
                save_data(stored_data)
                st.success("User Register Successfully!")
            else:
                st.error("Both fields are required.")
        elif choice == "Login":
            st.subheader("User Login")

            if time.time() < st.session_state.lockout_time:
                remaining = int(st.session_state.lockout_time - time.time())
                st.error(f" Too many failed attempts.please wait{remaining} seconds.")
                st.stop()

            username = st.text_input("Username")
            password = st.text_input("Password", type="password")

            if st.button("Login"):
                if username in stored_data and stored_data[username]["password"]==hash_password(password):
                    st.session_state.authenticated_user = username
                    st.session_state.failed_attempts =0
                    st.success(f"Welcome {username}!")
                else:
                    st.session_state.failed_attempts += 1
                    remaining = 3 - st.session_state.failed_attempts
                    st.error(f"Invalid Cardentials! Attempts left:{remaining}")

                    if st.session_state.failed_attempts >= 3:
                        st.session_state.lockout_time = time.time() + LOCKOUT_DURATION
                        st.error("Too many failed attempts. Locked for 60 seconds")
                        st.stop()

        #  data store section
        elif choice == "Store Data"
            if not st.session_state.authentication_user:
                st.warning("Please Login First")
            else:
                st.subheader("Store Encrypted Data")
                data = st.text_area("Enter Data to Encrpty")
                passkey = st.text_input("Encryption key (passphrase)",type="password")

            







