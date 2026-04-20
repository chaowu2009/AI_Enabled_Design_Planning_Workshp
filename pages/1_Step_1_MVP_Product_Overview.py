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

configure_page("Step 1 - MVP Product Overview")
init_session_state()
render_header()
render_sidebar()

st.header("Step 1 — MVP Product Overview")
col1, col2 = st.columns(2)
with col1:
    st.text_input("System name", key="s1_system_name")
    st.text_input("One-line purpose", key="s1_purpose")
    st.text_input("Primary users", key="s1_users")
    st.text_area("Main problem", key="s1_problem", height=100)
with col2:
    st.text_area("Top goals (one per line)", key="s1_goals", height=100)
    st.text_area("Constraints (one per line)", key="s1_constraints", height=100)
    st.text_area("Out of scope (one per line)", key="s1_out_of_scope", height=100)

st.text_area("Build now", key="s1_build_now", height=80)
st.text_area("Do not build now", key="s1_do_not_build", height=80)

step_outputs, step13_output, final_design_guide = generate_and_save_all_outputs()
render_generate_and_copy_buttons("step_1", step_outputs, step13_output, final_design_guide)
render_step_output_editor(1, step_outputs[1])
