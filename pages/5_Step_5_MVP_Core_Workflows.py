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

configure_page("Step 5 - MVP Core Workflows")
init_session_state()
render_header()
render_sidebar()

st.header("Step 5 — MVP Core Workflows")
if st.button("Add a new workflow"):
    st.session_state.workflows.append({"name": "", "trigger": "", "actor": "", "preconditions": "", "steps": "", "objects_touched": "", "result": "", "failure_cases": "", "manual_steps": ""})

for i, wf in enumerate(st.session_state.workflows):
    with st.container(border=True):
        st.subheader(f"Workflow {i + 1}")
        c1, c2 = st.columns(2)
        with c1:
            wf["name"] = st.text_input("Workflow name", value=wf["name"], key=f"wf_name_{i}")
            wf["trigger"] = st.text_input("Trigger", value=wf["trigger"], key=f"wf_trigger_{i}")
            wf["actor"] = st.text_input("Actor", value=wf["actor"], key=f"wf_actor_{i}")
            wf["preconditions"] = st.text_area("Preconditions", value=wf["preconditions"], key=f"wf_pre_{i}", height=80)
            wf["steps"] = st.text_area("Main steps (one per line)", value=wf["steps"], key=f"wf_steps_{i}", height=120)
        with c2:
            wf["objects_touched"] = st.text_area("Objects touched (one per line)", value=wf["objects_touched"], key=f"wf_obj_{i}", height=80)
            wf["result"] = st.text_input("Result", value=wf["result"], key=f"wf_result_{i}")
            wf["failure_cases"] = st.text_area("Failure cases (one per line)", value=wf["failure_cases"], key=f"wf_fail_{i}", height=90)
            wf["manual_steps"] = st.text_area("Manual steps allowed for MVP", value=wf["manual_steps"], key=f"wf_manual_{i}", height=70)

step_outputs, step13_output, final_design_guide = generate_and_save_all_outputs()
render_generate_and_copy_buttons("step_5", step_outputs, step13_output, final_design_guide)
render_step_output_editor(5, step_outputs[5])
