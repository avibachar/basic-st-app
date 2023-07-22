
import streamlit as st


def app():
    
    
    st.markdown(create_html(), unsafe_allow_html=True)
    


def create_html():
    theColor = "#E29C04"
    logo = "./app/static/aplogo.png"
    caption = "Agile Primero Labs"
    line1 = f'<span style="color: {theColor}; font-weight: bold;">Human Excellence</span> is about striving to become better every day'
    line2 = f"A celebration of our <span style='color: {theColor}; font-weight: bold;'>potential to grow</span>, adapt,"
    line3 = f"And create a <span style='color: {theColor}; font-weight: bold;'>brighter future</span>"
    

    html = f"""
    <div style="text-align: center; padding: 20px; border-radius: 15px; background: #F5F5F5; box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);">
        <img src="{logo}" alt="Logo" style="width: 250px; height: 200px; border-radius: 10%; box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.2); margin-bottom: 20px;">
        <div>
            <h1>{caption}</h1>
        </div>
        <div>
            <p style="font-size: 1.2em; font-style: italic;">{line1}</p>
            <p style="font-size: 1.2em; font-style: italic;">{line2}</p>
            <p style="font-size: 1.2em; font-style: italic;">{line3}</p>
        </div>
    </div>
    """
    return html


