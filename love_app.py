import streamlit as st
import random

things = [
    "You always smell good",  
    "You are stunningly beautiful",
    "Cheek kisses",
    "Your eyes in the sunlight"
    # ... add all 50+ here, one per line ...
]

st.set_page_config(page_title="Things He Loves About me", page_icon="💕", layout="centered")
st.markdown("## 💕 Things He Loves About Me 💕")

if st.button("😍 Tell me something he loves about me", use_container_width=True):
    love = random.choice(things)
    st.markdown(f"**{love}** ❤️")
else:
    st.markdown("*Tap the button for a surprise!*")