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

configure_page("Step 6 - MVC Mapping")
init_session_state()
render_header()
render_sidebar()

st.header("Step 6 — MVC Mapping")
if st.button("Add a new MVC mapping"):
    st.session_state.mvc_items.append({"function_name": "", "models": "", "view": "", "controller": "", "reuse_code": "", "new_addition": "", "rewrite_needed": False})

for i, mvc in enumerate(st.session_state.mvc_items):
    with st.container(border=True):
        st.subheader(f"MVC Mapping {i + 1}")
        c1, c2 = st.columns(2)
        with c1:
            mvc["function_name"] = st.text_input("Function name", value=mvc["function_name"], key=f"mvc_func_{i}")
            mvc["models"] = st.text_input("Model(s)", value=mvc["models"], key=f"mvc_models_{i}")
            mvc["view"] = st.text_input("View/Page", value=mvc["view"], key=f"mvc_view_{i}")
            mvc["controller"] = st.text_input("Controller/Action", value=mvc["controller"], key=f"mvc_controller_{i}")
        with c2:
            mvc["reuse_code"] = st.text_area("Existing code to reuse", value=mvc["reuse_code"], key=f"mvc_reuse_{i}", height=90)
            mvc["new_addition"] = st.text_area("New addition needed", value=mvc["new_addition"], key=f"mvc_new_{i}", height=90)
            mvc["rewrite_needed"] = st.checkbox("Rewrite needed", value=mvc["rewrite_needed"], key=f"mvc_rewrite_{i}")

step_outputs, step13_output, final_design_guide = generate_and_save_all_outputs()
render_generate_and_copy_buttons("step_6", step_outputs, step13_output, final_design_guide)
render_step_output_editor(6, step_outputs[6])
