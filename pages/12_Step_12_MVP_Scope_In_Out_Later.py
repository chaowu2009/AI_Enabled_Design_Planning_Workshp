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

configure_page("Step 12 - MVP Scope In Out Later")
init_session_state()
render_header()
render_sidebar()

st.header("Step 12 — MVP Scope: In / Out / Later")
if st.button("Add a new scope bucket"):
    st.session_state.phases.append({"bucket": "In MVP", "items": "", "dependencies": "", "risks": "", "manual_workarounds": ""})

for i, phase in enumerate(st.session_state.phases):
    with st.container(border=True):
        st.subheader(f"Scope Bucket {i + 1}")
        c1, c2 = st.columns(2)
        with c1:
            phase["bucket"] = st.selectbox("Bucket", ["In MVP", "Out for now", "Later"], index=["In MVP", "Out for now", "Later"].index(phase["bucket"]), key=f"phase_bucket_{i}")
            phase["items"] = st.text_area("Items (one per line)", value=phase["items"], key=f"phase_items_{i}", height=100)
        with c2:
            phase["dependencies"] = st.text_area("Dependencies", value=phase["dependencies"], key=f"phase_dep_{i}", height=70)
            phase["risks"] = st.text_area("Risks", value=phase["risks"], key=f"phase_risk_{i}", height=70)
            phase["manual_workarounds"] = st.text_area("Manual workarounds allowed in MVP", value=phase["manual_workarounds"], key=f"phase_manual_{i}", height=70)

step_outputs, step13_output, final_design_guide = generate_and_save_all_outputs()
render_generate_and_copy_buttons("step_12", step_outputs, step13_output, final_design_guide)
render_step_output_editor(12, step_outputs[12])
