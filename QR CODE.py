#!/usr/bin/env python
# coding: utf-8

# In[7]:


import qrcode
import streamlit as st
from PIL import Image

st.title('QR Code Generator')

data = st.text_input('Enter the link for which you want to create a QR code:', 'https://example.com')

if st.button('Generate QR Code'):
    # Generate QR code
    image = qrcode.make(data)
    
    # Save the QR code as an image file
    QR_file = 'QR.png'
    image.save(QR_file)
    
    # Open the saved image
    img = Image.open(QR_file)
    
    # Display the QR code using Streamlit
    st.image(img, caption='Generated QR Code')


# In[9]:


import subprocess
import threading
import time
import webbrowser

def run_streamlit_app(script_path):
    """Run the Streamlit app in a separate thread."""
    def target():
        subprocess.run(["streamlit", "run", script_path])
    
    # Start the Streamlit app in a new thread
    thread = threading.Thread(target=target)
    thread.start()
    time.sleep(5)  # Wait for the server to start
    
    # Open the Streamlit app in the default web browser
    webbrowser.open("http://localhost:8501")

# Path to the Streamlit script
script_path = 'qr_app.py'

# Run the Streamlit app
run_streamlit_app(script_path)


# In[ ]:




