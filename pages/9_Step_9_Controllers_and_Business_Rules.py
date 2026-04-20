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

configure_page("Step 9 - Controllers and Business Rules")
init_session_state()
render_header()
render_sidebar()

st.header("Step 9 — Controllers and Business Rules")
if st.button("Add a new controller/module"):
    st.session_state.controllers.append({"controller_name": "", "responsibility": "", "routes": "", "permission_checks": "", "business_rules": "", "validation_rules": "", "extend_existing": False, "new_controller": False})

for i, ctrl in enumerate(st.session_state.controllers):
    with st.container(border=True):
        st.subheader(f"Controller / Module {i + 1}")
        c1, c2 = st.columns(2)
        with c1:
            ctrl["controller_name"] = st.text_input("Controller name", value=ctrl["controller_name"], key=f"ctrl_name_{i}")
            ctrl["responsibility"] = st.text_input("Main responsibility", value=ctrl["responsibility"], key=f"ctrl_resp_{i}")
            ctrl["routes"] = st.text_area("Main routes/actions", value=ctrl["routes"], key=f"ctrl_routes_{i}", height=90)
        with c2:
            ctrl["permission_checks"] = st.text_area("Permission checks", value=ctrl["permission_checks"], key=f"ctrl_perm_{i}", height=80)
            ctrl["business_rules"] = st.text_area("Business rules", value=ctrl["business_rules"], key=f"ctrl_rules_{i}", height=90)
            ctrl["validation_rules"] = st.text_area("Validation rules", value=ctrl["validation_rules"], key=f"ctrl_val_{i}", height=80)
            ctrl["extend_existing"] = st.checkbox("Extend existing controller", value=ctrl["extend_existing"], key=f"ctrl_extend_{i}")
            ctrl["new_controller"] = st.checkbox("New controller needed", value=ctrl["new_controller"], key=f"ctrl_new_{i}")

step_outputs, step13_output, final_design_guide = generate_and_save_all_outputs()
render_generate_and_copy_buttons("step_9", step_outputs, step13_output, final_design_guide)
render_step_output_editor(9, step_outputs[9])
