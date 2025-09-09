import streamlit as st

# Hide default menu and footer
st.set_page_config(page_title="VerdaX - AI Trade Platform", layout="wide")

# Hero section
st.title("🌍 VerdaX — AI-powered Trade Platform")
st.subheader("Simplifying exports, logistics, compliance, and buyer access for PNG cooperatives.")

st.markdown("#### 🚀 Empowering cooperatives, buyers, and logistics partners with AI-driven trade tools.")

if st.button("👉 Get Started"):
    st.switch_page("pages/login.py")  # later when login is built

st.markdown("---")

# Features section
st.header("✨ Key Features")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.subheader("For Cooperatives")
    st.write("List products, access global buyers, and manage compliance with ease.")

with col2:
    st.subheader("For Buyers")
    st.write("Source verified, sustainable commodities directly from cooperatives.")

with col3:
    st.subheader("For Transport Partners")
    st.write("Access logistics jobs, ensure transparency, and grow your network.")

with col4:
    st.subheader("For Admins")
    st.write("Oversee compliance, track contracts, and enable climate credits.")

st.markdown("---")

# How it works
st.header("🔄 How It Works")
steps = [
    "📦 **List Products** – Coops create export-ready listings",
    "🌐 **Connect Buyers** – Buyers browse and order sustainably",
    "🚚 **Arrange Transport** – Logistics partners claim jobs",
    "✅ **Stay Compliant** – Automatic docs & reporting"
]
for step in steps:
    st.markdown(f"- {step}")

st.markdown("---")

# Vision / Impact
st.header("🌱 Our Impact")
st.info("AI-driven trade + climate credits = sustainable growth for PNG cooperatives.")

st.metric("Cooperatives Onboarded", "0 (MVP)", "+ soon")
st.metric("Buyers Connected", "0 (MVP)", "+ soon")
st.metric("CO₂ Saved", "0 kg", "coming soon")

# Footer
st.markdown("---")
st.write("© 2025 VerdaX Technologies | [GitHub Repo](https://github.com/VerdaX-Technologies/VerdaX)")
