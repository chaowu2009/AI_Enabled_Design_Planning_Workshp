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

configure_page("Step 4 - CRUD Matrix")
init_session_state()
render_header()
render_sidebar()

st.header("Step 4 — CRUD Matrix")
if st.button("Add a new CRUD item"):
    st.session_state.crud_items.append({"object_name": "", "create": "", "read": "", "update": "", "delete": "", "conditions": "", "soft_delete": False, "version_instead": False})

for i, crud in enumerate(st.session_state.crud_items):
    with st.container(border=True):
        st.subheader(f"CRUD Item {i + 1}")
        c1, c2 = st.columns(2)
        with c1:
            crud["object_name"] = st.text_input("Object name", value=crud["object_name"], key=f"crud_obj_{i}")
            crud["create"] = st.text_input("Who can create", value=crud["create"], key=f"crud_create_{i}")
            crud["read"] = st.text_input("Who can read", value=crud["read"], key=f"crud_read_{i}")
            crud["update"] = st.text_input("Who can update", value=crud["update"], key=f"crud_update_{i}")
        with c2:
            crud["delete"] = st.text_input("Who can delete", value=crud["delete"], key=f"crud_delete_{i}")
            crud["conditions"] = st.text_area("Conditional rules", value=crud["conditions"], key=f"crud_conditions_{i}", height=90)
            crud["soft_delete"] = st.checkbox("Soft delete only", value=crud["soft_delete"], key=f"crud_soft_{i}")
            crud["version_instead"] = st.checkbox("Version instead of update", value=crud["version_instead"], key=f"crud_version_{i}")

step_outputs, step13_output, final_design_guide = generate_and_save_all_outputs()
render_generate_and_copy_buttons("step_4", step_outputs, step13_output, final_design_guide)
render_step_output_editor(4, step_outputs[4])
