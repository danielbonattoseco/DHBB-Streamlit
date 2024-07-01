import streamlit as st

button_col, other_col = st.columns([1, 3])

# Definindo o JavaScript inline
custom_js = """
<script>
document.addEventListener("DOMContentLoaded", function() {
    // Seleciona todos os checkboxes dentro de colunas
    const checkboxes = document.querySelectorAll('[data-testid=column] [type=checkbox]');
    
    // Itera sobre cada checkbox
    checkboxes.forEach(function(checkbox) {
        // Verifica se a chave (key) contém 'seletor_data'
        if (checkbox.getAttribute('key').includes('seletor_data')) {
            // Aplica o estilo para os checkboxes desejados
            checkbox.parentElement.style.gap = '0rem';
        }
    });
});
</script>
"""

# Aplicando o JavaScript
st.markdown(custom_js, unsafe_allow_html=True)

# Layout dos checkboxes
with button_col:
    st.markdown("*Modified gap:*")
    st.checkbox("text", key="seletor_data_1")
    st.checkbox("text1", key="seletor_data_2")
    st.checkbox("text2", key="not_this")

with other_col:
    st.markdown("*Unmodified gap:*")
    st.checkbox("text4")
    st.checkbox("text5")
    st.checkbox("text6")
