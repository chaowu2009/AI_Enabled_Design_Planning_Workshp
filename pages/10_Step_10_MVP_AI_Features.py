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

configure_page("Step 10 - MVP AI Features")
init_session_state()
render_header()
render_sidebar()

st.header("Step 10 — MVP AI Features")
if st.button("Add a new AI feature"):
    st.session_state.ai_features.append({"feature_name": "", "problem_solved": "", "trigger": "", "input_data": "", "output_shown": "", "user_verify": "", "page_controller": "", "guardrails": "", "fallback": ""})

for i, ai in enumerate(st.session_state.ai_features):
    with st.container(border=True):
        st.subheader(f"AI Feature {i + 1}")
        c1, c2 = st.columns(2)
        with c1:
            ai["feature_name"] = st.text_input("Feature name", value=ai["feature_name"], key=f"ai_name_{i}")
            ai["problem_solved"] = st.text_input("Problem solved", value=ai["problem_solved"], key=f"ai_problem_{i}")
            ai["trigger"] = st.text_input("Trigger", value=ai["trigger"], key=f"ai_trigger_{i}")
            ai["input_data"] = st.text_area("Input data", value=ai["input_data"], key=f"ai_input_{i}", height=80)
            ai["output_shown"] = st.text_area("Output shown", value=ai["output_shown"], key=f"ai_output_{i}", height=80)
        with c2:
            ai["user_verify"] = st.text_area("What user must verify", value=ai["user_verify"], key=f"ai_verify_{i}", height=80)
            ai["page_controller"] = st.text_input("Page / controller involved", value=ai["page_controller"], key=f"ai_pagectrl_{i}")
            ai["guardrails"] = st.text_area("Guardrails", value=ai["guardrails"], key=f"ai_guard_{i}", height=80)
            ai["fallback"] = st.text_area("Fallback if AI fails", value=ai["fallback"], key=f"ai_fallback_{i}", height=80)

step_outputs, step13_output, final_design_guide = generate_and_save_all_outputs()
render_generate_and_copy_buttons("step_10", step_outputs, step13_output, final_design_guide)
render_step_output_editor(10, step_outputs[10])
