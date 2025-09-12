from supabase import create_client, Client
import streamlit as st

@st.cache_resource
def get_client() -> Client:
    url = st.secrets["supabase"]["url"]
    key = st.secrets["supabase"]["key"]
    return create_client(url, key)

def get_session(sb: Client):
    try:
        return sb.auth.get_session().session
    except Exception:
        return None

def get_profile(sb: Client):
    sess = get_session(sb)
    if not sess:
        return None
    uid = sess.user.id
    out = sb.table("profiles").select("id,email,role,coop_id,transporter_id,full_name").eq("id", uid).single().execute()
    return out.data if out.data else None

