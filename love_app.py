import streamlit as st
import random

things = [
    "You always smell good",  
    "You are stunningly beautiful",
    "Cheek kisses",
    "Your eyes in the sunlight",
    "You have the best dog in the world",
    "You laugh at my poop jokes",
    "You are so soft all the time",
    "You make the best mac n cheese",
    "You bring me weed and get high with me",
    "You pluck my hairs",
    "The way you breathe when you are asleep and it relaxes me",
    "You dress so cute",
    "Your lips and teeth when you laugh",
    "You are a sandwich master",
    "Your hairbrained schemes",
    "When you rub my neck when I drive",
    "Your AI emojis",
    "Your hair is soft, long, and glorious",
    "Great socks",
    # ... add all 50+ here, one per line ...
]


st.set_page_config(page_title="Things He Loves About me", page_icon="💕", layout="centered")
st.markdown("## 💕 Things He Loves About Me 💕")

if st.button("😍 Tell me something he loves about me", use_container_width=True):
    love = random.choice(things)
    st.markdown(f"**{love}** ❤️")
else:

    st.markdown("*Tap the button for a surprise!*")


