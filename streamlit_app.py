import streamlit as st
import qrcode
import io

# --- PAGE CONFIGURATION ---
# This sets the browser tab title and icon
st.set_page_config(page_title="QR Pro | Skincare Tech", page_icon="🛡️")

# --- CUSTOM CSS (The "Dark Blue" Theme) ---
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    stTextInput > div > div > input {
        background-color: #1b2635;
        color: white;
    }
    </style>
   """, unsafe_allow_html=True) # Change 'contents' to 'html'

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.title("📂 Navigation")
    page = st.radio("Go to:", ["Home", "About the Tech", "Contact"])
    st.markdown("---")

# --- LOGIC PER PAGE ---
if page == "Home":
    st.title("✨ Professional QR Generator")
    st.write("Turn your skincare product links into scannable codes instantly.")

    # The Input
    url = st.text_input("Enter your URL here:", placeholder="https://vincecare.com/...")
    if url:
        # The QR Logic
        qr = qrcode.QRCode(version=1, box_size=10, border=4)
        qr.add_data(url)
        qr.make(fit=True)

        # Using your "Memory Buffer" logic!
        img = qr.make_image(fill_color="#1b2635", back_color="white") # Dark blue QR!
        buf = io.BytesIO()
        img.save(buf, format="PNG")
        byte_im = buf.getvalue()

        # Displaying in columns for a cleaner look
        col1, col2 = st.columns(2)
        with col1:
            st.image(byte_im, caption="Generated QR Code")
        with col2:
            st.success("QR Code Generated successfully!")
            st.download_button(
                label="📥 Download PNG",
                data=byte_im,
                file_name="skincare_qr.png",
                mime="image/png"
            )


elif page == "About the Tech":
    st.title("📖 About this Project")
    st.write("""
    This app was built to bridge the gap between **Global Data Science** and **Pakistani Skincare**.
    It uses Python memory buffering to ensure fast, secure data handling without storing user information on a hard drive.
    """)

elif page == "Contact":
    st.title("📧 Get in Touch")
    st.write("Have a product you want audited? Reach out!")
    st.text_input("Your Email")
    st.text_area("Your Message")
    if st.button("Send Message"):
        st.balloons()
        st.success("Message 'sent' to the cloud!")
