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

configure_page("Step 3 - MVP Core Business Objects")
init_session_state()
render_header()
render_sidebar()

st.header("Step 3 — MVP Core Business Objects")
if st.button("Add a new business object"):
    st.session_state.objects.append({"name": "", "purpose": "", "owner": "", "existing_or_new": "Existing", "minimum_fields": ""})

for i, obj in enumerate(st.session_state.objects):
    with st.container(border=True):
        st.subheader(f"Business Object {i + 1}")
        c1, c2 = st.columns(2)
        with c1:
            obj["name"] = st.text_input("Object name", value=obj["name"], key=f"obj_name_{i}")
            obj["purpose"] = st.text_input("Purpose", value=obj["purpose"], key=f"obj_purpose_{i}")
            obj["owner"] = st.text_input("Owner", value=obj["owner"], key=f"obj_owner_{i}")
        with c2:
            obj["existing_or_new"] = st.selectbox("Existing or new", ["Existing", "New"], index=0 if obj["existing_or_new"] == "Existing" else 1, key=f"obj_existing_{i}")
            obj["minimum_fields"] = st.text_area("Minimum fields needed now", value=obj["minimum_fields"], key=f"obj_fields_{i}", height=90)

step_outputs, step13_output, final_design_guide = generate_and_save_all_outputs()
render_generate_and_copy_buttons("step_3", step_outputs, step13_output, final_design_guide)
render_step_output_editor(3, step_outputs[3])
