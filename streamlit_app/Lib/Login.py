import streamlit as st
from lib.supabase_client import get_client, get_profile

st.title("🔐 Login / Signup")
sb = get_client()
me = get_profile(sb)

if me:
    st.success(f"Already signed in: {me['email']} ({me['role']})")
    if st.button("Sign out"):
        sb.auth.sign_out()
        st.rerun()
else:
    tab1, tab2 = st.tabs(["Login","Signup"])

    with tab1:
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            try:
                sb.auth.sign_in_with_password({"email": email, "password": password})
                st.success("Logged in.")
                st.rerun()
            except Exception as e:
                st.error(str(e))

    with tab2:
        email2 = st.text_input("New email", key="e2")
        pwd2 = st.text_input("New password", type="password", key="p2")
        role = st.selectbox("Initial role (admin may change later)", ["buyer","coop","transporter"])
        full_name = st.text_input("Full name (optional)")
        if st.button("Create account"):
            try:
                sb.auth.sign_up({"email": email2, "password": pwd2})
                st.info("Check your email to confirm. After confirmation, ask admin to set your role in profiles.")
                # Optional: try to set full_name immediately after confirmation in a later step.
            except Exception as e:
                st.error(str(e))
