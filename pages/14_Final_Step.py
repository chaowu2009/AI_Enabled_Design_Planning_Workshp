import streamlit as st

from workshop_core import (
    configure_page,
    generate_and_save_all_outputs,
    init_session_state,
    render_generate_and_copy_buttons,
    render_header,
    render_sidebar,
    save_markdown,
)

configure_page("Step 14 - Final Step")
init_session_state()
render_header()
render_sidebar()

st.header("Step 14 — Final Step")
st.caption("This page combines step_1_output.md through step_13_output.md into the final output.")

step_outputs, step13_output, final_design_guide = generate_and_save_all_outputs()
render_generate_and_copy_buttons("step_14", step_outputs, step13_output, final_design_guide)

if "step_14_output_editor" not in st.session_state:
    st.session_state["step_14_output_editor"] = final_design_guide

edited_final_output = st.text_area(
    "Editable step_14_output.md (Final Output)",
    key="step_14_output_editor",
    height=520,
)

if edited_final_output != final_design_guide:
    save_markdown("step_14_output.md", edited_final_output)
    save_markdown("final_design_guide.md", edited_final_output)

with st.expander("Current generated final output preview"):
    st.code(final_design_guide, language="markdown")
