import streamlit as st
from streamlit.web import cli as stcli
from streamlit import runtime
import sys
from GraphColection.PayPlan import PayPlan_Graph
from langchain_community.document_loaders import TextLoader ,PyPDFLoader
from dotenv import load_dotenv
load_dotenv()

def Agent_reply():
    fattura_ = PyPDFLoader(r'C:\Users\PaulHernanAlarconPac\Desktop\Demo_PayPlan_Advisor\output\fattura.pdf ')
    fattura = fattura_.load()
    contratto = PyPDFLoader(r'C:\Users\PaulHernanAlarconPac\Desktop\Demo_PayPlan_Advisor\output\contratto.pdf')
    contratto = contratto.load()
    flow = PayPlan_Graph()
    State_flow = flow.invoke({'invoice':fattura,'documents':contratto})
    return  State_flow['answer']

def main():
    st.title('PayPlanGPT Advisor')
    st.write('Welcome to PayPlanGPT Advisor! Please fill out the form below to get started.')
    file = st.file_uploader('Carica il tuo contratto:', type=['pdf'],key='1',accept_multiple_files=False)
    
    file_ = st.file_uploader('Carica la tua fattura', type=['pdf'],key='2',accept_multiple_files=False)

    #Plan = st.selectbox('Select the type of pay plan to include in the analysis:', ['APPALTO', 'Plan 2', 'Plan 3'])

    Analyze_button = st.button('Analyze')
        
    with st.container():
        #st.header(Plan)
        if Analyze_button:
            with st.spinner('Analyzing...'):
                if file is not None:
                    contratto_byte = file.getvalue()
                    # Save the byte data as a new PDF file
                    with open('output/contratto.pdf', 'wb') as f:
                        f.write(contratto_byte)
                    # Create a new PDF file using the byte data
                    if file_ is not None:
                        fattura_byte = file_.getvalue()
                        with open('output/fattura.pdf', 'wb') as f:
                            f.write(fattura_byte)
                            finale_plane = Agent_reply()
                else:
                    st.write('Please upload a file to analyze.')
            with st.container(border=True):
                if finale_plane is not None:
                   st.markdown(finale_plane)
            
if __name__ == '__main__':
    if runtime.exists():
        main()
    else:
        sys.argv = ["streamlit", "run", "--server.enableXsrfProtection", "false", sys.argv[0]]
        sys.exit(stcli.main())