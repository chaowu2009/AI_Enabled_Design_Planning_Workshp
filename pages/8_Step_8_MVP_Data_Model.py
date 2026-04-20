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

configure_page("Step 8 - MVP Data Model")
init_session_state()
render_header()
render_sidebar()

st.header("Step 8 — MVP Data Model")
if st.button("Add a new model"):
    st.session_state.models.append({"model_name": "", "primary_key": "", "required_fields": "", "relationships": "", "validations": "", "audit_fields": "", "extend_existing": False, "new_model": False})

for i, model in enumerate(st.session_state.models):
    with st.container(border=True):
        st.subheader(f"Model {i + 1}")
        c1, c2 = st.columns(2)
        with c1:
            model["model_name"] = st.text_input("Model name", value=model["model_name"], key=f"model_name_{i}")
            model["primary_key"] = st.text_input("Primary key", value=model["primary_key"], key=f"model_pk_{i}")
            model["required_fields"] = st.text_area("Required fields (one per line)", value=model["required_fields"], key=f"model_fields_{i}", height=100)
            model["relationships"] = st.text_area("Relationships", value=model["relationships"], key=f"model_rel_{i}", height=80)
        with c2:
            model["validations"] = st.text_area("Validations", value=model["validations"], key=f"model_val_{i}", height=90)
            model["audit_fields"] = st.text_area("Timestamps / audit fields", value=model["audit_fields"], key=f"model_audit_{i}", height=90)
            model["extend_existing"] = st.checkbox("Extend existing model", value=model["extend_existing"], key=f"model_extend_{i}")
            model["new_model"] = st.checkbox("New model needed", value=model["new_model"], key=f"model_new_{i}")

step_outputs, step13_output, final_design_guide = generate_and_save_all_outputs()
render_generate_and_copy_buttons("step_8", step_outputs, step13_output, final_design_guide)
render_step_output_editor(8, step_outputs[8])
