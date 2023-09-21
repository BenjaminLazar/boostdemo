# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 08:34:36 2023

@author: Benjamin Lazar
"""

import streamlit as st

# Creating 3 columns layout. Adjust it if needed according to your app layout
col1, col2, col3 = st.columns(3)

# Using the middle column to insert the image
with col1:
    st.write('')  # Left side empty space

with col2:
    st.image("https://signite.fra1.digitaloceanspaces.com/a4740/117641/conversions/todai-1-thumb.png", width=200)
    st.image("casey_large.png", width=200)

with col3:
    st.write('')  # Right side empty space

st.markdown("<h1 style='text-align: center;'>Casey - An AI Demo</h1>", unsafe_allow_html=True)


import time

responses = ["Hi, how can i help you with market research today? remember I can search the web", """[google search: 'top five trends for sustainable tech products']: Sure! Based on recent articles and reports, the top five trends for sustainable tech products are: 
- Refillable Products.
- Reimaged Packaging.
- Supply Chain Transparency.
- Secondhand Options at Top Retailers.
- Waste-Reducing Peripherals.""", """Certainly! Here's some conclusions of 'Sustainable Tech: 2023 Outlook':
- Market Size & Growth: Expected to reach $50 billion by 2025 with a CAGR of 10%.
- Consumer Behavior: 70% of tech consumers are willing to pay a premium for eco-friendly products.
- Regulatory Landscape: New regulations in EU and NA favoring sustainable tech production and disposal.
- Challenges: Supply chain sustainability and tech lifespan are primary concerns.""",
"""Response: "Of course! Here's the drafted email:

To: benjamin.lazar@todai.ai

Subject: Insights on Sustainable Tech Market

Body:

Hi Benjamin,

I've been diving into the sustainable tech market landscape and wanted to share some insights:

Top Market Trends:

- Refillable Products.
- Reimaged Packaging.
- Supply Chain Transparency.
- Secondhand Options at Top Retailers.
- Waste-Reducing Peripherals.

Report Highlights from 'Sustainable Tech: 2023 Outlook':

- The market is projected to reach $50 billion by 2025.
- A significant 70% of consumers are ready to pay more for green tech.
- Both the EU and NA are rolling out favorable regulations.
- Main challenges include sustainable supply chains and product longevity.

Let's discuss how we can integrate these insights into our upcoming product strategy!

Best,
[Your Name]

Can I send it?""", "sent"
]

uploaded_files = st.file_uploader(" ", type="pdf")
process_button = st.button("Process PDF")

# Check if 'index' and 'conversation' are already in the session state
if 'index' not in st.session_state:
    st.session_state.index = 0
if 'conversation' not in st.session_state:
    st.session_state.conversation = []

# Start with a user input
user_input = st.chat_input("Enter your message")

time.sleep(3)

if user_input:
    # Add user's message to the conversation
    st.session_state.conversation.append(("user", user_input))

    # Add bot's response to the conversation
    st.session_state.conversation.append(("assistant", responses[st.session_state.index]))

    # Update the index
    st.session_state.index = (st.session_state.index + 1) % len(responses)

# Display the entire conversation
for speaker, message in st.session_state.conversation:
    with st.chat_message(speaker):
        st.write(message)