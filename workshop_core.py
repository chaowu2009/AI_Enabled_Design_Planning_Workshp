import json
from pathlib import Path
from textwrap import dedent

import streamlit as st
import streamlit.components.v1 as components

OUTPUT_DIR = Path("generated_steps")
OUTPUT_DIR.mkdir(exist_ok=True)
TOTAL_STEPS = 14

WORKSHOP_RULES_MD = """
- Focus on MVP only
- Extend existing code; avoid rewrites
- Keep decisions short and explicit
- Separate Now / Keep Flexible / Later
- Make outputs usable for team discussion and Copilot prompts
"""


def configure_page(page_title: str):
    st.set_page_config(page_title=page_title, page_icon="🧭", layout="wide")


def render_header():
    st.title("🧭 MVP SaaS Design Workshop")
    st.caption("Interactive team design flow for CRUD/MVC SaaS products, optimized for MVP planning, code reuse, and GitHub Copilot handoff.")


def render_sidebar():
    with st.sidebar:
        st.header("Workshop Rules")
        st.markdown(WORKSHOP_RULES_MD)


def save_markdown(filename: str, content: str) -> Path:
    path = OUTPUT_DIR / filename
    path.write_text(content, encoding="utf-8")
    return path


def _override_key(step_num: int) -> str:
    return f"step_{step_num}_output_override"


def _editor_key(step_num: int) -> str:
    return f"step_{step_num}_output_editor"


def _get_effective_step_output(step_num: int, generated_output: str) -> str:
    override = st.session_state.get(_override_key(step_num), "")
    if isinstance(override, str) and override.strip():
        return override

    editor_value = st.session_state.get(_editor_key(step_num), "")
    if isinstance(editor_value, str) and editor_value.strip():
        return editor_value

    return generated_output


def _clear_all_output_overrides():
    for step_num in range(1, TOTAL_STEPS + 1):
        st.session_state.pop(_override_key(step_num), None)
        st.session_state.pop(_editor_key(step_num), None)


def _build_copy_payload(step_outputs: dict[int, str], step13_output: str, final_design_guide: str) -> str:
    parts = []
    for i in range(1, 13):
        parts.append(f"=== step_{i}_output.md ===")
        parts.append(step_outputs[i].rstrip())
        parts.append("")
    parts.append("=== step_13_output.md ===")
    parts.append(step13_output.rstrip())
    parts.append("")
    parts.append("=== step_14_output.md ===")
    parts.append(final_design_guide.rstrip())
    parts.append("")
    parts.append("=== final_design_guide.md ===")
    parts.append(final_design_guide.rstrip())
    return "\n".join(parts).strip() + "\n"


def render_generate_and_copy_buttons(page_key: str, step_outputs: dict[int, str], step13_output: str, final_design_guide: str):
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("Generate", key=f"generate_all_{page_key}", use_container_width=True):
            _clear_all_output_overrides()
            st.rerun()
    with col2:
        payload = _build_copy_payload(step_outputs, step13_output, final_design_guide)
        button_id = f"copy_all_{page_key}"
        status_id = f"copy_status_{page_key}"
        components.html(
            f"""
            <div style=\"display:flex;align-items:center;gap:8px;\"> 
              <button id=\"{button_id}\" style=\"width:100%;padding:0.5rem 0.75rem;border-radius:0.5rem;border:1px solid #d1d5db;background:#ffffff;cursor:pointer;\">Copy</button>
              <span id=\"{status_id}\" style=\"font-size:0.85rem;color:#6b7280;\"></span>
            </div>
            <script>
              const text = {json.dumps(payload)};
              const button = document.getElementById({json.dumps(button_id)});
              const status = document.getElementById({json.dumps(status_id)});
              if (button) {{
                button.addEventListener('click', async () => {{
                  try {{
                    await navigator.clipboard.writeText(text);
                    if (status) status.textContent = 'Copied';
                  }} catch (error) {{
                    if (status) status.textContent = 'Copy blocked by browser';
                  }}
                }});
              }}
            </script>
            """,
            height=56,
        )


def render_step_output_editor(step_num: int, current_output: str):
    editor_key = _editor_key(step_num)
    if editor_key not in st.session_state:
        st.session_state[editor_key] = current_output

    edited_output = st.text_area(
        f"Editable step_{step_num}_output.md",
        key=editor_key,
        height=360,
    )

    if edited_output != current_output:
        st.session_state[_override_key(step_num)] = edited_output
        save_markdown(f"step_{step_num}_output.md", edited_output)


def yes_no(value: bool) -> str:
    return "Yes" if value else "No"


def bullets(items):
    cleaned = [str(x).strip() for x in items if str(x).strip()]
    return "\n".join(f"- {item}" for item in cleaned) if cleaned else "- [Add here]"


def numbered(items):
    cleaned = [str(x).strip() for x in items if str(x).strip()]
    return "\n".join(f"{i}. {item}" for i, item in enumerate(cleaned, 1)) if cleaned else "1. [Add here]"


def text_or_placeholder(value: str) -> str:
    return value.strip() if value and value.strip() else "[Add here]"


def text_list(value: str):
    return [line.strip() for line in value.splitlines() if line.strip()]


def item_card_md(title: str, required: dict, optional: dict | None = None) -> str:
    parts = [f"## {title}", "### Required"]
    for key, value in required.items():
        parts.append(f"- **{key}:** {text_or_placeholder(value)}")
    if optional:
        parts.append("")
        parts.append("### Optional")
        for key, value in optional.items():
            parts.append(f"- **{key}:** {text_or_placeholder(value)}")
    return "\n".join(parts)


def build_step_file(step_num: int, title: str, intro: str, team_decision: str, mvp_only: str, reuse_existing: str, copilot_handoff: str) -> str:
    return dedent(
        f"""
        # Step {step_num} Output - {title}

        {intro}

        ## Team Decision
        {team_decision}

        ## MVP Only
        {mvp_only}

        ## Reuse Existing Code
        {reuse_existing}

        ## Copilot Handoff
        {copilot_handoff}
        """
    ).strip() + "\n"


def assemble_final_guide(step_outputs: dict[int, str]) -> str:
    parts = ["# Final MVP Design Guide", ""]
    parts.append("This guide compiles all step outputs into one MVP-focused design reference for team discussion and GitHub Copilot-assisted implementation.")
    parts.append("")
    for i in range(1, 14):
        content = step_outputs.get(i, "").strip()
        if content:
            title_line = content.splitlines()[0].replace("# ", "")
            body = "\n".join(content.splitlines()[2:])
        else:
            title_line = f"Step {i} Output"
            body = "[Not generated yet]"
        parts.append(f"---\n\n{title_line}\n")
        parts.append(body)
        parts.append("")
    return "\n".join(parts).strip() + "\n"


def ensure_list_state(key: str, default_item: dict):
    if key not in st.session_state:
        st.session_state[key] = [default_item.copy()]


def init_session_state():
    ensure_list_state(
        "roles",
        {
            "role_name": "",
            "responsibility": "",
            "can_see": "",
            "can_create": "",
            "can_update": "",
            "can_delete": "",
            "can_approve": "",
            "restrictions": "",
            "notes": "",
        },
    )
    ensure_list_state(
        "objects",
        {"name": "", "purpose": "", "owner": "", "existing_or_new": "Existing", "minimum_fields": ""},
    )
    ensure_list_state(
        "crud_items",
        {"object_name": "", "create": "", "read": "", "update": "", "delete": "", "conditions": "", "soft_delete": False, "version_instead": False},
    )
    ensure_list_state(
        "workflows",
        {"name": "", "trigger": "", "actor": "", "preconditions": "", "steps": "", "objects_touched": "", "result": "", "failure_cases": "", "manual_steps": ""},
    )
    ensure_list_state(
        "mvc_items",
        {"function_name": "", "models": "", "view": "", "controller": "", "reuse_code": "", "new_addition": "", "rewrite_needed": False},
    )
    ensure_list_state(
        "pages",
        {"page_name": "", "purpose": "", "main_user": "", "data_shown": "", "actions_shown": "", "visible_roles": "", "hidden_roles": "", "reuse_template": False, "new_page": False},
    )
    ensure_list_state(
        "models",
        {"model_name": "", "primary_key": "", "required_fields": "", "relationships": "", "validations": "", "audit_fields": "", "extend_existing": False, "new_model": False},
    )
    ensure_list_state(
        "controllers",
        {"controller_name": "", "responsibility": "", "routes": "", "permission_checks": "", "business_rules": "", "validation_rules": "", "extend_existing": False, "new_controller": False},
    )
    ensure_list_state(
        "ai_features",
        {"feature_name": "", "problem_solved": "", "trigger": "", "input_data": "", "output_shown": "", "user_verify": "", "page_controller": "", "guardrails": "", "fallback": ""},
    )
    ensure_list_state(
        "phases",
        {"bucket": "In MVP", "items": "", "dependencies": "", "risks": "", "manual_workarounds": ""},
    )


def build_step1_output() -> str:
    system_name = st.session_state.get("s1_system_name", "")
    one_line_purpose = st.session_state.get("s1_purpose", "")
    primary_users = st.session_state.get("s1_users", "")
    main_problem = st.session_state.get("s1_problem", "")
    top_goals = st.session_state.get("s1_goals", "")
    constraints = st.session_state.get("s1_constraints", "")
    out_of_scope = st.session_state.get("s1_out_of_scope", "")
    build_now = st.session_state.get("s1_build_now", "")
    do_not_build_now = st.session_state.get("s1_do_not_build", "")

    step1_team = dedent(
        f"""
        - **System name:** {text_or_placeholder(system_name)}
        - **One-line purpose:** {text_or_placeholder(one_line_purpose)}
        - **Primary users:** {text_or_placeholder(primary_users)}
        - **Main problem:** {text_or_placeholder(main_problem)}
        - **Top goals:**
        {bullets(text_list(top_goals))}
        - **Constraints:**
        {bullets(text_list(constraints))}
        - **Out of scope:**
        {bullets(text_list(out_of_scope))}
        """
    ).strip()
    step1_mvp = dedent(
        f"""
        - **Build now:**
        {bullets(text_list(build_now))}
        - **Do not build now:**
        {bullets(text_list(do_not_build_now))}
        """
    ).strip()
    step1_reuse = "- Reuse current product boundaries and existing working modules where possible. Do not broaden scope just because a future idea exists."
    step1_copilot = dedent(
        f"""
        - Product: {text_or_placeholder(system_name)}
        - MVP purpose: {text_or_placeholder(one_line_purpose)}
        - Primary users: {text_or_placeholder(primary_users)}
        - Must build now:
        {bullets(text_list(build_now))}
        - Exclude for MVP:
        {bullets(text_list(do_not_build_now))}
        """
    ).strip()
    return build_step_file(1, "MVP Product Overview", "Align the team on the MVP target before designing details.", step1_team, step1_mvp, step1_reuse, step1_copilot)


def build_step2_output() -> str:
    role_team_blocks = []
    role_copilot_blocks = []
    for role in st.session_state.roles:
        title = f"Role: {text_or_placeholder(role['role_name'])}"
        role_team_blocks.append(item_card_md(title, {
            "Main responsibility": role["responsibility"],
            "Can see": role["can_see"],
            "Can create": role["can_create"],
            "Can update": role["can_update"],
            "Can delete": role["can_delete"],
            "Can approve": role["can_approve"],
        }, {
            "Restrictions": role["restrictions"],
            "Notes": role["notes"],
        }))
        role_copilot_blocks.append(dedent(f"""
        - Role: {text_or_placeholder(role['role_name'])}
        - Can read: {text_or_placeholder(role['can_see'])}
        - Can create: {text_or_placeholder(role['can_create'])}
        - Can update: {text_or_placeholder(role['can_update'])}
        - Can delete: {text_or_placeholder(role['can_delete'])}
        - Can approve: {text_or_placeholder(role['can_approve'])}
        - Restrictions: {text_or_placeholder(role['restrictions'])}
        """).strip())

    return build_step_file(
        2,
        "Roles and Access",
        "Define only the minimum roles needed for MVP.",
        "\n\n".join(role_team_blocks) if role_team_blocks else "[Add here]",
        "- Keep roles minimal for launch. Prefer simple access rules and avoid granular permission design unless truly needed.",
        "- Extend current access model where possible. Avoid rewriting working authorization flows just to make them cleaner.",
        "\n\n".join(role_copilot_blocks) if role_copilot_blocks else "[Add here]",
    )


def build_step3_output() -> str:
    obj_team = []
    obj_copilot = []
    for obj in st.session_state.objects:
        obj_team.append(item_card_md(f"Object: {text_or_placeholder(obj['name'])}", {
            "Purpose": obj["purpose"],
            "Owner": obj["owner"],
            "Existing or new": obj["existing_or_new"],
            "Minimum fields needed now": obj["minimum_fields"],
        }))
        obj_copilot.append(dedent(f"""
        - Object: {text_or_placeholder(obj['name'])}
        - Purpose: {text_or_placeholder(obj['purpose'])}
        - Owner: {text_or_placeholder(obj['owner'])}
        - Existing or new: {text_or_placeholder(obj['existing_or_new'])}
        - Minimum fields: {text_or_placeholder(obj['minimum_fields'])}
        """).strip())

    return build_step_file(
        3,
        "MVP Core Business Objects",
        "Define the smallest set of objects needed to support the MVP workflows.",
        "\n\n".join(obj_team),
        "- Only include objects truly needed for launch. Do not introduce entities just because they may be useful later.",
        "- Reuse existing models and concepts where possible. Extend rather than redesign.",
        "\n\n".join(obj_copilot),
    )


def build_step4_output() -> str:
    crud_team = []
    crud_copilot = []
    for crud in st.session_state.crud_items:
        crud_team.append(item_card_md(f"Object: {text_or_placeholder(crud['object_name'])}", {
            "Create": crud["create"],
            "Read": crud["read"],
            "Update": crud["update"],
            "Delete": crud["delete"],
        }, {
            "Conditional rules": crud["conditions"],
            "Soft delete only": yes_no(crud["soft_delete"]),
            "Version instead of update": yes_no(crud["version_instead"]),
        }))
        crud_copilot.append(dedent(f"""
        - Object: {text_or_placeholder(crud['object_name'])}
        - Create: {text_or_placeholder(crud['create'])}
        - Read: {text_or_placeholder(crud['read'])}
        - Update: {text_or_placeholder(crud['update'])}
        - Delete: {text_or_placeholder(crud['delete'])}
        - Conditions: {text_or_placeholder(crud['conditions'])}
        - Soft delete only: {yes_no(crud['soft_delete'])}
        - Version instead of update: {yes_no(crud['version_instead'])}
        """).strip())

    return build_step_file(
        4,
        "CRUD Matrix",
        "Make object-level access rules explicit before implementation starts.",
        "\n\n".join(crud_team),
        "- Keep CRUD simple for MVP. Remove risky delete behavior if not required for launch.",
        "- Reuse the current permission structure where possible. Do not refactor authorization broadly unless it blocks MVP.",
        "\n\n".join(crud_copilot),
    )


def build_step5_output() -> str:
    wf_team = []
    wf_copilot = []
    for wf in st.session_state.workflows:
        wf_team.append(item_card_md(f"Workflow: {text_or_placeholder(wf['name'])}", {
            "Trigger": wf["trigger"],
            "Actor": wf["actor"],
            "Preconditions": wf["preconditions"],
            "Main steps": numbered(text_list(wf["steps"])),
            "Objects touched": bullets(text_list(wf["objects_touched"])),
            "Result": wf["result"],
        }, {
            "Failure cases": bullets(text_list(wf["failure_cases"])),
            "Manual steps allowed for MVP": wf["manual_steps"],
        }))
        wf_copilot.append(dedent(f"""
        - Workflow: {text_or_placeholder(wf['name'])}
        - Trigger: {text_or_placeholder(wf['trigger'])}
        - Actor: {text_or_placeholder(wf['actor'])}
        - Preconditions: {text_or_placeholder(wf['preconditions'])}
        - Steps:
        {numbered(text_list(wf['steps']))}
        - Result: {text_or_placeholder(wf['result'])}
        - Failure cases:
        {bullets(text_list(wf['failure_cases']))}
        """).strip())

    return build_step_file(
        5,
        "MVP Core Workflows",
        "Document only the few workflows required for launch.",
        "\n\n".join(wf_team),
        "- Keep workflows minimal. Allow simple manual workarounds where that reduces MVP complexity.",
        "- Fit workflows into the current product shape. Avoid redesigning flow orchestration unless current flow blocks MVP.",
        "\n\n".join(wf_copilot),
    )


def build_step6_output() -> str:
    mvc_team = []
    mvc_copilot = []
    for mvc in st.session_state.mvc_items:
        mvc_team.append(item_card_md(f"Function: {text_or_placeholder(mvc['function_name'])}", {
            "Model(s)": mvc["models"],
            "View/Page": mvc["view"],
            "Controller/Action": mvc["controller"],
        }, {
            "Existing code to reuse": mvc["reuse_code"],
            "New addition needed": mvc["new_addition"],
            "Rewrite needed": yes_no(mvc["rewrite_needed"]),
        }))
        mvc_copilot.append(dedent(f"""
        - Function: {text_or_placeholder(mvc['function_name'])}
        - Models: {text_or_placeholder(mvc['models'])}
        - View: {text_or_placeholder(mvc['view'])}
        - Controller: {text_or_placeholder(mvc['controller'])}
        - Reuse existing code: {text_or_placeholder(mvc['reuse_code'])}
        - Add new code: {text_or_placeholder(mvc['new_addition'])}
        - Rewrite needed: {yes_no(mvc['rewrite_needed'])}
        """).strip())

    return build_step_file(
        6,
        "MVC Mapping",
        "Map business functions to models, views, and controllers for implementation planning.",
        "\n\n".join(mvc_team),
        "- Keep changes additive. Use current MVC shape where possible and default rewrite to no.",
        "- Extend stable code paths rather than replacing them. Reuse controllers, templates, and models when practical.",
        "\n\n".join(mvc_copilot),
    )


def build_step7_output() -> str:
    page_team = []
    page_copilot = []
    for page in st.session_state.pages:
        page_team.append(item_card_md(f"Page: {text_or_placeholder(page['page_name'])}", {
            "Purpose": page["purpose"],
            "Main user": page["main_user"],
            "Data shown": page["data_shown"],
            "Actions shown": page["actions_shown"],
            "Visible roles": page["visible_roles"],
            "Hidden roles": page["hidden_roles"],
        }, {
            "Reuse existing template/page": yes_no(page["reuse_template"]),
            "New page needed": yes_no(page["new_page"]),
        }))
        page_copilot.append(dedent(f"""
        - Page: {text_or_placeholder(page['page_name'])}
        - Purpose: {text_or_placeholder(page['purpose'])}
        - Main user: {text_or_placeholder(page['main_user'])}
        - Data shown: {text_or_placeholder(page['data_shown'])}
        - Actions shown: {text_or_placeholder(page['actions_shown'])}
        - Visible roles: {text_or_placeholder(page['visible_roles'])}
        - Reuse existing template: {yes_no(page['reuse_template'])}
        - New page needed: {yes_no(page['new_page'])}
        """).strip())

    return build_step_file(
        7,
        "MVP Pages / Views",
        "Define only the screens required for MVP and keep UI scope tight.",
        "\n\n".join(page_team),
        "- Prefer extending current pages over introducing new screens. Keep page count minimal for launch.",
        "- Reuse current templates and view patterns where possible. Avoid visual rewrites unrelated to MVP needs.",
        "\n\n".join(page_copilot),
    )


def build_step8_output() -> str:
    model_team = []
    model_copilot = []
    for model in st.session_state.models:
        model_team.append(item_card_md(f"Model: {text_or_placeholder(model['model_name'])}", {
            "Primary key": model["primary_key"],
            "Required fields": bullets(text_list(model["required_fields"])),
            "Relationships": model["relationships"],
            "Validations": model["validations"],
        }, {
            "Timestamps / audit fields": model["audit_fields"],
            "Extend existing model": yes_no(model["extend_existing"]),
            "New model needed": yes_no(model["new_model"]),
        }))
        model_copilot.append(dedent(f"""
        - Model: {text_or_placeholder(model['model_name'])}
        - Primary key: {text_or_placeholder(model['primary_key'])}
        - Required fields:
        {bullets(text_list(model['required_fields']))}
        - Relationships: {text_or_placeholder(model['relationships'])}
        - Validations: {text_or_placeholder(model['validations'])}
        - Extend existing model: {yes_no(model['extend_existing'])}
        - New model needed: {yes_no(model['new_model'])}
        """).strip())

    return build_step_file(
        8,
        "MVP Data Model",
        "Define only the minimum persistent data structure required for launch.",
        "\n\n".join(model_team),
        "- Keep schema small but clean. Include only fields required for MVP while leaving room for later growth.",
        "- Extend current models before creating new ones, unless a new entity is clearly required.",
        "\n\n".join(model_copilot),
    )


def build_step9_output() -> str:
    ctrl_team = []
    ctrl_copilot = []
    for ctrl in st.session_state.controllers:
        ctrl_team.append(item_card_md(f"Controller: {text_or_placeholder(ctrl['controller_name'])}", {
            "Main responsibility": ctrl["responsibility"],
            "Main routes/actions": ctrl["routes"],
            "Permission checks": ctrl["permission_checks"],
            "Business rules": ctrl["business_rules"],
            "Validation rules": ctrl["validation_rules"],
        }, {
            "Extend existing controller": yes_no(ctrl["extend_existing"]),
            "New controller needed": yes_no(ctrl["new_controller"]),
        }))
        ctrl_copilot.append(dedent(f"""
        - Controller: {text_or_placeholder(ctrl['controller_name'])}
        - Responsibility: {text_or_placeholder(ctrl['responsibility'])}
        - Routes/actions: {text_or_placeholder(ctrl['routes'])}
        - Permission checks: {text_or_placeholder(ctrl['permission_checks'])}
        - Business rules: {text_or_placeholder(ctrl['business_rules'])}
        - Validation rules: {text_or_placeholder(ctrl['validation_rules'])}
        - Extend existing controller: {yes_no(ctrl['extend_existing'])}
        - New controller needed: {yes_no(ctrl['new_controller'])}
        """).strip())

    return build_step_file(
        9,
        "Controllers and Business Rules",
        "Define the minimum request handling and rule enforcement needed for MVP.",
        "\n\n".join(ctrl_team),
        "- Keep controllers focused. Centralize permission logic where possible and avoid spreading role checks everywhere.",
        "- Extend current controllers/modules rather than replacing them. Add only the logic required for MVP behavior.",
        "\n\n".join(ctrl_copilot),
    )


def build_step10_output() -> str:
    ai_team = []
    ai_copilot = []
    for ai in st.session_state.ai_features:
        ai_team.append(item_card_md(f"AI Feature: {text_or_placeholder(ai['feature_name'])}", {
            "Problem solved": ai["problem_solved"],
            "Trigger": ai["trigger"],
            "Input data": ai["input_data"],
            "Output shown": ai["output_shown"],
            "User must verify": ai["user_verify"],
        }, {
            "Page / controller involved": ai["page_controller"],
            "Guardrails": ai["guardrails"],
            "Fallback if AI fails": ai["fallback"],
        }))
        ai_copilot.append(dedent(f"""
        - AI feature: {text_or_placeholder(ai['feature_name'])}
        - Problem solved: {text_or_placeholder(ai['problem_solved'])}
        - Trigger: {text_or_placeholder(ai['trigger'])}
        - Input data: {text_or_placeholder(ai['input_data'])}
        - Output shown: {text_or_placeholder(ai['output_shown'])}
        - User verifies: {text_or_placeholder(ai['user_verify'])}
        - Guardrails: {text_or_placeholder(ai['guardrails'])}
        - Fallback: {text_or_placeholder(ai['fallback'])}
        """).strip())

    return build_step_file(
        10,
        "MVP AI Features",
        "Keep AI narrow, optional, and reviewable by users.",
        "\n\n".join(ai_team),
        "- Only keep AI features that add real MVP value. No AI feature should break the core workflow if disabled.",
        "- Integrate AI without forcing rewrites to existing workflow logic. Prefer optional entry points and clear fallbacks.",
        "\n\n".join(ai_copilot),
    )


def build_step11_output() -> str:
    frontend = st.session_state.get("s11_frontend", "")
    backend = st.session_state.get("s11_backend", "")
    database = st.session_state.get("s11_database", "")
    file_storage = st.session_state.get("s11_storage", "")
    auth = st.session_state.get("s11_auth", "")
    authorization = st.session_state.get("s11_authz", "")
    search = st.session_state.get("s11_search", "")
    logging_audit = st.session_state.get("s11_logging", "")
    reuse_modules = st.session_state.get("s11_reuse", "")
    new_modules = st.session_state.get("s11_new", "")
    areas_not_to_touch = st.session_state.get("s11_no_touch", "")
    rewrite_needed_11 = st.session_state.get("s11_rewrite", False)
    naming_conventions = st.session_state.get("s11_naming", "")

    step11_team = dedent(f"""
    - **Front end:** {text_or_placeholder(frontend)}
    - **Back end:** {text_or_placeholder(backend)}
    - **Database:** {text_or_placeholder(database)}
    - **File storage:** {text_or_placeholder(file_storage)}
    - **Authentication:** {text_or_placeholder(auth)}
    - **Authorization:** {text_or_placeholder(authorization)}
    - **Search:** {text_or_placeholder(search)}
    - **Logging / audit:** {text_or_placeholder(logging_audit)}
    - **Existing modules to reuse:**
    {bullets(text_list(reuse_modules))}
    - **New modules to add:**
    {bullets(text_list(new_modules))}
    - **Areas not to touch:** {text_or_placeholder(areas_not_to_touch)}
    - **Rewrite needed:** {yes_no(rewrite_needed_11)}
    - **Naming conventions / where new code should go:** {text_or_placeholder(naming_conventions)}
    """).strip()

    step11_mvp = "- Keep architecture simple. Design for MVP enhancement, not platform redesign. No broad refactors unless they truly block MVP."
    step11_reuse = "- Reuse existing modules, conventions, and deployment assumptions where possible. Add only what is needed for launch."
    step11_copilot = dedent(f"""
    - Front end: {text_or_placeholder(frontend)}
    - Back end: {text_or_placeholder(backend)}
    - Database: {text_or_placeholder(database)}
    - Storage: {text_or_placeholder(file_storage)}
    - Auth: {text_or_placeholder(auth)}
    - Authorization: {text_or_placeholder(authorization)}
    - Search: {text_or_placeholder(search)}
    - Logging/audit: {text_or_placeholder(logging_audit)}
    - Reuse modules:
    {bullets(text_list(reuse_modules))}
    - Add modules:
    {bullets(text_list(new_modules))}
    - Do not touch: {text_or_placeholder(areas_not_to_touch)}
    """).strip()

    return build_step_file(11, "MVP Technical Architecture", "Define how the MVP fits into the current system without unnecessary redesign.", step11_team, step11_mvp, step11_reuse, step11_copilot)


def build_step12_output() -> str:
    phase_team = []
    phase_copilot = []
    for phase in st.session_state.phases:
        phase_team.append(item_card_md(f"Bucket: {text_or_placeholder(phase['bucket'])}", {
            "Items": bullets(text_list(phase["items"])),
            "Dependencies": phase["dependencies"],
            "Risks": phase["risks"],
        }, {
            "Manual workarounds allowed in MVP": phase["manual_workarounds"],
        }))
        phase_copilot.append(dedent(f"""
        - Bucket: {text_or_placeholder(phase['bucket'])}
        - Items:
        {bullets(text_list(phase['items']))}
        - Dependencies: {text_or_placeholder(phase['dependencies'])}
        - Risks: {text_or_placeholder(phase['risks'])}
        - Manual workarounds: {text_or_placeholder(phase['manual_workarounds'])}
        """).strip())

    return build_step_file(
        12,
        "MVP Scope: In / Out / Later",
        "Control scope tightly and record what is intentionally deferred.",
        "\n\n".join(phase_team),
        "- If it is not required for launch, move it out of MVP. Preserve future ideas, but do not convert them into current commitments.",
        "- Reuse current functionality where that avoids new scope. Do not create replacement work just to make the architecture cleaner.",
        "\n\n".join(phase_copilot),
    )


def build_step13_output() -> str:
    assumptions = st.session_state.get("s13_assumptions", "")
    open_questions = st.session_state.get("s13_questions", "")
    implementation_slices = st.session_state.get("s13_slices", "")

    step13_team = dedent(f"""
    - Compile steps 1 through 12 into one clean MVP design guide.
    - Keep names, roles, objects, pages, and rules consistent.
    - Confirm the design remains MVP-focused.
    - Confirm rewrite proposals are minimized and justified.
    - Assumptions: {text_or_placeholder(assumptions)}
    - Open questions: {text_or_placeholder(open_questions)}
    """).strip()
    step13_mvp = "- Final guide should be concise, MVP-focused, and discussion-ready. It should separate current scope from deferred ideas."
    step13_reuse = "- Final guide should preserve the minimal-change strategy: extend existing code, avoid broad rewrites, and clearly mark untouched areas."
    step13_copilot = dedent(f"""
    - Final implementation slices:
    {bullets(text_list(implementation_slices))}
    - Use previous step outputs as the source of truth for prompts.
    - Keep task slices small and explicit.
    """).strip()

    return build_step_file(13, "Final Design Guide Assembly", "Combine all prior outputs into one team-ready and Copilot-ready guide.", step13_team, step13_mvp, step13_reuse, step13_copilot)


def generate_and_save_all_outputs() -> tuple[dict[int, str], str, str]:
    generated_step_outputs = {
        1: build_step1_output(),
        2: build_step2_output(),
        3: build_step3_output(),
        4: build_step4_output(),
        5: build_step5_output(),
        6: build_step6_output(),
        7: build_step7_output(),
        8: build_step8_output(),
        9: build_step9_output(),
        10: build_step10_output(),
        11: build_step11_output(),
        12: build_step12_output(),
    }

    step_outputs = {i: _get_effective_step_output(i, generated_step_outputs[i]) for i in range(1, 13)}
    for i in range(1, 13):
        save_markdown(f"step_{i}_output.md", step_outputs[i])

    generated_step13_output = build_step13_output()
    step13_output = _get_effective_step_output(13, generated_step13_output)
    save_markdown("step_13_output.md", step13_output)

    final_design_guide = assemble_final_guide({**step_outputs, 13: step13_output})
    save_markdown("final_design_guide.md", final_design_guide)
    save_markdown("step_14_output.md", final_design_guide)

    return step_outputs, step13_output, final_design_guide


def render_downloads_and_debug(step_outputs: dict[int, str], step13_output: str, final_design_guide: str):
    st.header("Downloads")
    for i in range(1, TOTAL_STEPS + 1):
        if i <= 12:
            content = step_outputs[i]
        elif i == 13:
            content = step13_output
        else:
            content = final_design_guide
        st.download_button(
            f"Download step_{i}_output.md",
            content,
            file_name=f"step_{i}_output.md",
            mime="text/markdown",
            key=f"download_step_{i}",
        )

    st.download_button(
        "Download final_design_guide.md",
        final_design_guide,
        file_name="final_design_guide.md",
        mime="text/markdown",
        key="download_final_guide",
    )

    with st.expander("Preview session data"):
        st.json({
            "roles": st.session_state.roles,
            "objects": st.session_state.objects,
            "crud_items": st.session_state.crud_items,
            "workflows": st.session_state.workflows,
            "mvc_items": st.session_state.mvc_items,
            "pages": st.session_state.pages,
            "models": st.session_state.models,
            "controllers": st.session_state.controllers,
            "ai_features": st.session_state.ai_features,
            "scope_buckets": st.session_state.phases,
        })
