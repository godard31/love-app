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
    "When we have the exact same thought",
    "You make the best avacado toast",
    "You really upped the value of our home",
    "You make jokes about porch stealing",
    "myman quavious",
    "You have Great taste in house decor",
    "The way you lay on me at night",
    "You took me to yoga",
    "Red bathroom and candle",
    "No one wears a bodysuit like you do",
    "You love and laugh at my hooting and hollering",
    "my man ****** technologies",
    "You look cute as fuck in my shirts",
    "your cute ass ponytail",
    "You call my pa a turd",
    "We live together",
    "You cut my hair",
    "We don't have nearly enough time to do all the things we want to do together, we never will",
    "hammock",
    "bedtime routine",
    "You let me in the shower water when I am cold and sick",
    "one seasons resort and spa",
    "You take care of my sick ass",
    "orders weird cocunut milk",
    "You love a blue elephant sippy cup",
    "You bring me coffee in the morning",
    "We have blankets on the deck",
    "DUMPSTER",
    "You took me to tractor supply company",
    "You  got us Ikea furniture",
    "We pressure wash together",
    "Hundreds of feet of chain unravelling"
    
    # ... add all 50+ here, one per line ...
]


st.set_page_config(page_title="Things He Loves About me", page_icon="💕", layout="centered")
st.markdown("## 💕 Things He Loves About Me 💕")

if st.button("😍 Tell me something he loves about me", use_container_width=True):
    love = random.choice(things)
    st.markdown(f"**{love}** ❤️")
else:

    st.markdown("*Tap the button for a surprise!*")



