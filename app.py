import streamlit as st
import openai
#from huggingface_hub import InferenceClient

from apps import home #chatllm, 

class MultiApp:
    def __init__(self):
        self.apps = []
        self.active_app = None

    def add_app(self, title, func):
        """Adds a new application.
        Parameters
        ----------
        func:
            the python function to render this app.
        title:
            title of the app. Appears in the dropdown in the sidebar.
        """
        self.apps.append({
            "title": title,
            "function": func
        })

    def Initiate_default_Params(self):
        # Set default parameters
        st.session_state.ssPlatform = "Hugging Face"
        st.session_state.ssModel = "gpt-3.5-turbo"
        #st.session_state.ssAccess_Key = st.secrets["OPENAI_API_KEY"]
        st.session_state.ssTemperature = 0.5

        st.session_state["openai_params"] = {
            "engine": "text-davinci-003",
            "prompt": "",
            "temperature": 0.2, # Sampling temperature to use
            "max_tokens": 100, # Maximum number of tokens to generate in the completion
            "top_p": 1.0, # Alternative to sampling with temperature
            "frequency_penalty": 0.0, # How much to penalize new tokens based on their existing frequency
            "presence_penalty": 0.0, # How much to penalize new tokens based on whether they appear in the text so far
            "stop": None, # Up to 4 sequences where the API will stop generating further tokens
            "n": 1, # How many completions to generate for each prompt
            "stream": False, # Whether to stream back partial progress
            "logprobs": None, # Include the log probabilities on the logprobs most likely tokens
            "echo": False, # Echo back the prompt in addition to the completion
            "user": "avi" # A string which will be included in the model's metadata
        }
        #st.session_state["Hugging_Face_api"] = InferenceClient() 
        #st.session_state["openai_api"] =  openai


    def renderSidebar(self):
        
        st.sidebar.markdown("""
            <div style="text-align: center;  padding: 0px;"> 
            <img src="./app/static/aplogo.png" alt="Agile Primero Logo" style="width: 188px; height: 150px; border-radius: 10%; box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.2); margin-bottom: 20px;">
            </div>
            """, unsafe_allow_html=True)
        st.sidebar.expander("About Agile Primero Labs",expanded=False).markdown("""
            <div style="text-align: center;  padding: 0px;">
            <h1>AgilePrimero Labs</h1>
            <p>This site was developed by Agile Primero Team<br>for the benefit of the Human Kind</p>
           
            </div>
            """, unsafe_allow_html=True)
        self.active_app = st.sidebar.expander("Applications",expanded=True).radio(
            'Selected Application will be presented to the right.....',
            self.apps,
            format_func=lambda app: app['title'])
        with st.sidebar.expander("Chat Settings",expanded=False) :
            #st.sidebar.title("Settings")
            st.radio("Platform", ["Open A.I.", "Hugging Face"], key='ssPlatform')
            st.text_input("Model", key='ssModel')
            st.text_input("Access Key", type="password", key='ssAccess_Key')
            st.slider("Temperature", 0.0, 1.0, key='ssTemperature')  # Default value is 0.5
        with st.sidebar.expander("Audit Log",expanded=False) :
            st.write(st.session_state)


    def run(self):
        # app = st.sidebar.radio(
        if "isAppSrarting" not in st.session_state:
            self.Initiate_default_Params()
            st.session_state.isAppSrarting = False
        self.renderSidebar()
        self.active_app['function']()
        
        

app = MultiApp()

# Add all your application here
app.add_app("Home", home.app)
#app.add_app("Chat", chatllm.main)

#app.add_app("Model", model.app)
# The main app

app.run()
