import streamlit as st

from workshop_core import (
    configure_page,
    generate_and_save_all_outputs,
    init_session_state,
    render_generate_and_copy_buttons,
    render_header,
    render_sidebar,
    render_step_output_editor,
)

configure_page("Step 11 - MVP Technical Architecture")
init_session_state()
render_header()
render_sidebar()

st.header("Step 11 — MVP Technical Architecture")
arch_col1, arch_col2 = st.columns(2)
with arch_col1:
    st.text_input("Front end", key="s11_frontend")
    st.text_input("Back end", key="s11_backend")
    st.text_input("Database", key="s11_database")
    st.text_input("File storage", key="s11_storage")
    st.text_input("Authentication", key="s11_auth")
with arch_col2:
    st.text_input("Authorization", key="s11_authz")
    st.text_input("Search", key="s11_search")
    st.text_input("Logging / audit", key="s11_logging")
    st.text_area("Existing modules to reuse (one per line)", key="s11_reuse", height=100)
    st.text_area("New modules to add (one per line)", key="s11_new", height=100)

st.text_area("Areas not to touch", key="s11_no_touch", height=80)
st.checkbox("Rewrite needed", key="s11_rewrite")
st.text_area("Naming conventions / where new code should go", key="s11_naming", height=80)

step_outputs, step13_output, final_design_guide = generate_and_save_all_outputs()
render_generate_and_copy_buttons("step_11", step_outputs, step13_output, final_design_guide)
render_step_output_editor(11, step_outputs[11])
