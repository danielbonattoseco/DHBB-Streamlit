import streamlit as st
import datetime

def validate_dates():
    """Valida os campos de data para impedir que datas impossíveis sejam inseridas."""

    if "data_nascimento" not in st.session_state: 
        st.session_state['data_nascimento'] = None
    if "data_falecimento" not in st.session_state: 
        st.session_state['data_falecimento'] = None
    if isinstance(st.session_state.data_nascimento, datetime.date) and isinstance(st.session_state.data_falecimento, datetime.date):
        if st.session_state.data_nascimento >= st.session_state.data_falecimento:
            st.toast("A data de falecimento não pode ser menor que a data de nascimento.", icon="⚠️")
            st.session_state['data_falecimento'] = None