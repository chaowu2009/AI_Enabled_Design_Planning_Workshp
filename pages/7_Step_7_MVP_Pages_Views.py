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

configure_page("Step 7 - MVP Pages and Views")
init_session_state()
render_header()
render_sidebar()

st.header("Step 7 — MVP Pages / Views")
if st.button("Add a new page"):
    st.session_state.pages.append({"page_name": "", "purpose": "", "main_user": "", "data_shown": "", "actions_shown": "", "visible_roles": "", "hidden_roles": "", "reuse_template": False, "new_page": False})

for i, page in enumerate(st.session_state.pages):
    with st.container(border=True):
        st.subheader(f"Page {i + 1}")
        c1, c2 = st.columns(2)
        with c1:
            page["page_name"] = st.text_input("Page name", value=page["page_name"], key=f"page_name_{i}")
            page["purpose"] = st.text_input("Purpose", value=page["purpose"], key=f"page_purpose_{i}")
            page["main_user"] = st.text_input("Main user", value=page["main_user"], key=f"page_user_{i}")
            page["data_shown"] = st.text_area("Data shown", value=page["data_shown"], key=f"page_data_{i}", height=90)
        with c2:
            page["actions_shown"] = st.text_area("Actions shown", value=page["actions_shown"], key=f"page_actions_{i}", height=90)
            page["visible_roles"] = st.text_input("Visible roles", value=page["visible_roles"], key=f"page_visible_{i}")
            page["hidden_roles"] = st.text_input("Hidden roles", value=page["hidden_roles"], key=f"page_hidden_{i}")
            page["reuse_template"] = st.checkbox("Reuse existing template/page", value=page["reuse_template"], key=f"page_reuse_{i}")
            page["new_page"] = st.checkbox("New page needed", value=page["new_page"], key=f"page_new_{i}")

step_outputs, step13_output, final_design_guide = generate_and_save_all_outputs()
render_generate_and_copy_buttons("step_7", step_outputs, step13_output, final_design_guide)
render_step_output_editor(7, step_outputs[7])
