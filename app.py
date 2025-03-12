import streamlit as st
from src.anonymizer import anonymize_message

# Streamlit UI Styling
st.markdown("""
    <style>
    /* Main App Background */
    .stApp {
        background-color: #1A1A2E;  /* Deep dark violet */
        color: #E0E0E0;  /* Light text for readability */
    }

    /* Header Styling */
    h1, h2, h3 {
        color: #BB86FC !important;  /* Light violet for headers */
    }

    /* Input Box Styling */
    .stTextArea textarea {
        background-color: #2A2A3D !important;  /* Dark violet input background */
        color: #E0E0E0 !important;  /* Light text */
        border: 1px solid #BB86FC !important;  /* Violet border */
        border-radius: 10px !important;
        padding: 10px !important;
    }

    /* Button Styling */
    .stButton button {
        background-color: #BB86FC !important;  /* Violet button */
        color: #1A1A2E !important;  /* Dark text */
        border-radius: 10px;
        padding: 10px 20px;
        border: none;
        font-weight: bold;
    }

    /* Success Message Styling */
    .stSuccess {
        background-color: #2A2A3D !important;  /* Dark violet background */
        border: 1px solid #BB86FC !important;  /* Violet border */
        color: #E0E0E0 !important;  /* Light text */
        border-radius: 10px;
        padding: 15px;
    }

    /* Spinner Styling */
    .stSpinner div {
        color: #BB86FC !important;  /* Violet spinner */
    }

    /* Footer Styling */
    .footer {
        text-align: center;
        color: #BB86FC;
        margin-top: 30px;
    }
    </style>
    """, unsafe_allow_html=True)

# App Title and Description
st.title("🔒 Identity Protection in Online Communication")
st.markdown("""
    Welcome to the **Identity Protection Tool**! This app helps you anonymize user identities in online communication by replacing real names with pseudonyms. 
    Simply enter your message below, and the app will generate an anonymized version for you.
    """)
st.markdown("---")

# User Input Section
st.markdown("### ✍️ Enter Your Message")
user_message = st.text_area(
    "Type your message here:",
    placeholder="Example: Hello, my name is John Doe and I live in New York.",
    height=150
)

# Anonymize Button
if st.button("Anonymize"):
    if user_message.strip():  # Check if the input is not empty
        with st.spinner("Anonymizing your message..."):
            anonymized_message = anonymize_message(user_message)
        st.success("✅ Message anonymized successfully!")
        st.markdown("---")
        st.markdown("### 🎭 Anonymized Message")
        st.write(anonymized_message)
    else:
        st.error("⚠️ Please enter a message to anonymize.")

# Footer
st.markdown("---")
st.markdown("""
    <div class="footer">
        <p>Powered by Streamlit | © 2023 Identity Protection Tool</p>
    </div>
    """, unsafe_allow_html=True)