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

configure_page("Step 2 - Roles and Access")
init_session_state()
render_header()
render_sidebar()

st.header("Step 2 — Roles and Access")
if st.button("Add a new role"):
    st.session_state.roles.append({
        "role_name": "",
        "responsibility": "",
        "can_see": "",
        "can_create": "",
        "can_update": "",
        "can_delete": "",
        "can_approve": "",
        "restrictions": "",
        "notes": "",
    })

for i, role in enumerate(st.session_state.roles):
    with st.container(border=True):
        st.subheader(f"Role {i + 1}")
        c1, c2 = st.columns(2)
        with c1:
            role["role_name"] = st.text_input("Role name", value=role["role_name"], key=f"role_name_{i}")
            role["responsibility"] = st.text_input("Main responsibility", value=role["responsibility"], key=f"role_resp_{i}")
            role["can_see"] = st.text_input("Can see", value=role["can_see"], key=f"role_see_{i}")
            role["can_create"] = st.text_input("Can create", value=role["can_create"], key=f"role_create_{i}")
            role["can_update"] = st.text_input("Can update", value=role["can_update"], key=f"role_update_{i}")
        with c2:
            role["can_delete"] = st.text_input("Can delete", value=role["can_delete"], key=f"role_delete_{i}")
            role["can_approve"] = st.text_input("Can approve", value=role["can_approve"], key=f"role_approve_{i}")
            role["restrictions"] = st.text_input("Restrictions", value=role["restrictions"], key=f"role_restrict_{i}")
            role["notes"] = st.text_input("Notes", value=role["notes"], key=f"role_notes_{i}")

step_outputs, step13_output, final_design_guide = generate_and_save_all_outputs()
render_generate_and_copy_buttons("step_2", step_outputs, step13_output, final_design_guide)
render_step_output_editor(2, step_outputs[2])
