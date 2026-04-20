import streamlit as st

from workshop_core import (
    configure_page,
    generate_and_save_all_outputs,
    init_session_state,
    render_header,
    render_sidebar,
)

configure_page("AI-Enabled SAAS Design Workshop")
init_session_state()
render_sidebar()

st.title("🧭 AI-Enabled SAAS Design Workshop")
st.caption("Interactive team design flow for CRUD/MVC SaaS products, optimized for MVP planning, code reuse, and GitHub Copilot handoff.")

st.header("Workshop Overview")
st.markdown(
    """
## Why This Workshop?

Building SaaS products at scale requires careful upfront design decisions. This workshop helps teams:
- **Align on MVP scope** without getting lost in future possibilities
- **Reuse existing code** instead of starting from scratch
- **Make explicit design decisions** that are easy to communicate and implement
- **Prepare work for AI-assisted development** using GitHub Copilot or similar tools

## What You'll Design

Over 14 guided steps, you'll document:
1. **Product Definition** – System name, purpose, users, goals, and constraints
2. **Access Control** – Roles, permissions, and authorization rules
3. **Core Objects** – Business entities needed for the MVP
4. **CRUD Operations** – Who can create, read, update, delete each object
5. **Workflows** – Key business processes and their steps
6. **MVC Mapping** – How functions map to models, views, and controllers
7. **Pages/Views** – Screens needed for MVP
8. **Data Model** – Database schema and relationships
9. **Controllers** – Business logic, validation, and permission enforcement
10. **AI Features** – Optional AI-assisted functionality
11. **Technical Architecture** – Tech stack and existing modules to reuse
12. **Scope Management** – Clear In/Out/Later categorization
13. **Final Assembly** – Assumptions, questions, and implementation slices
14. **Combined Output** – All 13 steps merged into one final design guide

## How to Use This Workshop

### For Each Step:
1. **Fill in the form fields** on the step page with your team's decisions
2. **Edit the generated output** if needed – your edits are preserved
3. **Use Generate** to rebuild outputs from form inputs (clears manual edits)
4. **Use Copy** to copy all generated content to clipboard

### Key Principles:
- **MVP-First**: Build now; defer future ideas
- **Reuse, Don't Rewrite**: Extend existing code and patterns
- **Explicit & Short**: Keep decisions clear and concise
- **Copilot-Ready**: Outputs are formatted for AI-assisted implementation

### Workflow:
- Steps 1–13 capture team decisions
- Step 14 combines all 13 outputs into the final design guide
- Download or copy your final guide for team discussion and development

Use the Streamlit multipage navigation in the sidebar to step through each page.
"""
)

step_outputs, step13_output, final_design_guide = generate_and_save_all_outputs()

with st.expander("Quick previews"):
    st.subheader("Step 1 - MVP Product Overview")
    st.code(step_outputs[1], language="markdown")
    st.subheader("Step 14 - Final Step (Combined Output)")
    st.code(final_design_guide, language="markdown")
