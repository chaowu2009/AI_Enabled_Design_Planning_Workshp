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

configure_page("Step 13 - Final Design Guide Assembly")
init_session_state()
render_header()
render_sidebar()

st.header("Step 13 — Final Design Guide Assembly")
st.text_area("Assumptions", key="s13_assumptions", height=90)
st.text_area("Open questions", key="s13_questions", height=90)
st.text_area("Implementation slices for Copilot (one per line)", key="s13_slices", height=100)

step_outputs, step13_output, final_design_guide = generate_and_save_all_outputs()
render_generate_and_copy_buttons("step_13", step_outputs, step13_output, final_design_guide)
render_step_output_editor(13, step13_output)

with st.expander("Preview final_design_guide.md"):
    st.code(final_design_guide, language="markdown")
