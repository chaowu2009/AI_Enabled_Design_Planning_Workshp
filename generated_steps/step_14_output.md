# Final MVP Design Guide

This guide compiles all step outputs into one MVP-focused design reference for team discussion and GitHub Copilot-assisted implementation.

---

Step 1 Output - MVP Product Overview

        Align the team on the MVP target before designing details.

        ## Team Decision
        - **System name:** [Add here]
- **One-line purpose:** [Add here]
- **Primary users:** [Add here]
- **Main problem:** [Add here]
- **Top goals:**
- [Add here]
- **Constraints:**
- [Add here]
- **Out of scope:**
- [Add here]

        ## MVP Only
        - **Build now:**
- [Add here]
- **Do not build now:**
- [Add here]

        ## Reuse Existing Code
        - Reuse current product boundaries and existing working modules where possible. Do not broaden scope just because a future idea exists.

        ## Copilot Handoff
        - Product: [Add here]
- MVP purpose: [Add here]
- Primary users: [Add here]
- Must build now:
- [Add here]
- Exclude for MVP:
- [Add here]

---

Step 2 Output - Roles and Access

        Define only the minimum roles needed for MVP.

        ## Team Decision
        ## Role: [Add here]
### Required
- **Main responsibility:** [Add here]
- **Can see:** [Add here]
- **Can create:** [Add here]
- **Can update:** [Add here]
- **Can delete:** [Add here]
- **Can approve:** [Add here]

### Optional
- **Restrictions:** [Add here]
- **Notes:** [Add here]

        ## MVP Only
        - Keep roles minimal for launch. Prefer simple access rules and avoid granular permission design unless truly needed.

        ## Reuse Existing Code
        - Extend current access model where possible. Avoid rewriting working authorization flows just to make them cleaner.

        ## Copilot Handoff
        - Role: [Add here]
- Can read: [Add here]
- Can create: [Add here]
- Can update: [Add here]
- Can delete: [Add here]
- Can approve: [Add here]
- Restrictions: [Add here]

---

Step 3 Output - MVP Core Business Objects

        Define the smallest set of objects needed to support the MVP workflows.

        ## Team Decision
        ## Object: [Add here]
### Required
- **Purpose:** [Add here]
- **Owner:** [Add here]
- **Existing or new:** Existing
- **Minimum fields needed now:** [Add here]

        ## MVP Only
        - Only include objects truly needed for launch. Do not introduce entities just because they may be useful later.

        ## Reuse Existing Code
        - Reuse existing models and concepts where possible. Extend rather than redesign.

        ## Copilot Handoff
        - Object: [Add here]
- Purpose: [Add here]
- Owner: [Add here]
- Existing or new: Existing
- Minimum fields: [Add here]

---

Step 4 Output - CRUD Matrix

        Make object-level access rules explicit before implementation starts.

        ## Team Decision
        ## Object: [Add here]
### Required
- **Create:** [Add here]
- **Read:** [Add here]
- **Update:** [Add here]
- **Delete:** [Add here]

### Optional
- **Conditional rules:** [Add here]
- **Soft delete only:** No
- **Version instead of update:** No

        ## MVP Only
        - Keep CRUD simple for MVP. Remove risky delete behavior if not required for launch.

        ## Reuse Existing Code
        - Reuse the current permission structure where possible. Do not refactor authorization broadly unless it blocks MVP.

        ## Copilot Handoff
        - Object: [Add here]
- Create: [Add here]
- Read: [Add here]
- Update: [Add here]
- Delete: [Add here]
- Conditions: [Add here]
- Soft delete only: No
- Version instead of update: No

---

Step 5 Output - MVP Core Workflows

        Document only the few workflows required for launch.

        ## Team Decision
        ## Workflow: [Add here]
### Required
- **Trigger:** [Add here]
- **Actor:** [Add here]
- **Preconditions:** [Add here]
- **Main steps:** 1. [Add here]
- **Objects touched:** - [Add here]
- **Result:** [Add here]

### Optional
- **Failure cases:** - [Add here]
- **Manual steps allowed for MVP:** [Add here]

        ## MVP Only
        - Keep workflows minimal. Allow simple manual workarounds where that reduces MVP complexity.

        ## Reuse Existing Code
        - Fit workflows into the current product shape. Avoid redesigning flow orchestration unless current flow blocks MVP.

        ## Copilot Handoff
        - Workflow: [Add here]
- Trigger: [Add here]
- Actor: [Add here]
- Preconditions: [Add here]
- Steps:
1. [Add here]
- Result: [Add here]
- Failure cases:
- [Add here]

---

Step 6 Output - MVC Mapping

        Map business functions to models, views, and controllers for implementation planning.

        ## Team Decision
        ## Function: [Add here]
### Required
- **Model(s):** [Add here]
- **View/Page:** [Add here]
- **Controller/Action:** [Add here]

### Optional
- **Existing code to reuse:** [Add here]
- **New addition needed:** [Add here]
- **Rewrite needed:** No

        ## MVP Only
        - Keep changes additive. Use current MVC shape where possible and default rewrite to no.

        ## Reuse Existing Code
        - Extend stable code paths rather than replacing them. Reuse controllers, templates, and models when practical.

        ## Copilot Handoff
        - Function: [Add here]
- Models: [Add here]
- View: [Add here]
- Controller: [Add here]
- Reuse existing code: [Add here]
- Add new code: [Add here]
- Rewrite needed: No

---

Step 7 Output - MVP Pages / Views

        Define only the screens required for MVP and keep UI scope tight.

        ## Team Decision
        ## Page: [Add here]
### Required
- **Purpose:** [Add here]
- **Main user:** [Add here]
- **Data shown:** [Add here]
- **Actions shown:** [Add here]
- **Visible roles:** [Add here]
- **Hidden roles:** [Add here]

### Optional
- **Reuse existing template/page:** No
- **New page needed:** No

        ## MVP Only
        - Prefer extending current pages over introducing new screens. Keep page count minimal for launch.

        ## Reuse Existing Code
        - Reuse current templates and view patterns where possible. Avoid visual rewrites unrelated to MVP needs.

        ## Copilot Handoff
        - Page: [Add here]
- Purpose: [Add here]
- Main user: [Add here]
- Data shown: [Add here]
- Actions shown: [Add here]
- Visible roles: [Add here]
- Reuse existing template: No
- New page needed: No

---

Step 8 Output - MVP Data Model

        Define only the minimum persistent data structure required for launch.

        ## Team Decision
        ## Model: [Add here]
### Required
- **Primary key:** [Add here]
- **Required fields:** - [Add here]
- **Relationships:** [Add here]
- **Validations:** [Add here]

### Optional
- **Timestamps / audit fields:** [Add here]
- **Extend existing model:** No
- **New model needed:** No

        ## MVP Only
        - Keep schema small but clean. Include only fields required for MVP while leaving room for later growth.

        ## Reuse Existing Code
        - Extend current models before creating new ones, unless a new entity is clearly required.

        ## Copilot Handoff
        - Model: [Add here]
- Primary key: [Add here]
- Required fields:
- [Add here]
- Relationships: [Add here]
- Validations: [Add here]
- Extend existing model: No
- New model needed: No

---

Step 9 Output - Controllers and Business Rules

        Define the minimum request handling and rule enforcement needed for MVP.

        ## Team Decision
        ## Controller: [Add here]
### Required
- **Main responsibility:** [Add here]
- **Main routes/actions:** [Add here]
- **Permission checks:** [Add here]
- **Business rules:** [Add here]
- **Validation rules:** [Add here]

### Optional
- **Extend existing controller:** No
- **New controller needed:** No

        ## MVP Only
        - Keep controllers focused. Centralize permission logic where possible and avoid spreading role checks everywhere.

        ## Reuse Existing Code
        - Extend current controllers/modules rather than replacing them. Add only the logic required for MVP behavior.

        ## Copilot Handoff
        - Controller: [Add here]
- Responsibility: [Add here]
- Routes/actions: [Add here]
- Permission checks: [Add here]
- Business rules: [Add here]
- Validation rules: [Add here]
- Extend existing controller: No
- New controller needed: No

---

Step 10 Output - MVP AI Features

        Keep AI narrow, optional, and reviewable by users.

        ## Team Decision
        ## AI Feature: [Add here]
### Required
- **Problem solved:** [Add here]
- **Trigger:** [Add here]
- **Input data:** [Add here]
- **Output shown:** [Add here]
- **User must verify:** [Add here]

### Optional
- **Page / controller involved:** [Add here]
- **Guardrails:** [Add here]
- **Fallback if AI fails:** [Add here]

        ## MVP Only
        - Only keep AI features that add real MVP value. No AI feature should break the core workflow if disabled.

        ## Reuse Existing Code
        - Integrate AI without forcing rewrites to existing workflow logic. Prefer optional entry points and clear fallbacks.

        ## Copilot Handoff
        - AI feature: [Add here]
- Problem solved: [Add here]
- Trigger: [Add here]
- Input data: [Add here]
- Output shown: [Add here]
- User verifies: [Add here]
- Guardrails: [Add here]
- Fallback: [Add here]

---

Step 11 Output - MVP Technical Architecture

        Define how the MVP fits into the current system without unnecessary redesign.

        ## Team Decision
        - **Front end:** [Add here]
- **Back end:** [Add here]
- **Database:** [Add here]
- **File storage:** [Add here]
- **Authentication:** [Add here]
- **Authorization:** [Add here]
- **Search:** [Add here]
- **Logging / audit:** [Add here]
- **Existing modules to reuse:**
- [Add here]
- **New modules to add:**
- [Add here]
- **Areas not to touch:** [Add here]
- **Rewrite needed:** No
- **Naming conventions / where new code should go:** [Add here]

        ## MVP Only
        - Keep architecture simple. Design for MVP enhancement, not platform redesign. No broad refactors unless they truly block MVP.

        ## Reuse Existing Code
        - Reuse existing modules, conventions, and deployment assumptions where possible. Add only what is needed for launch.

        ## Copilot Handoff
        - Front end: [Add here]
- Back end: [Add here]
- Database: [Add here]
- Storage: [Add here]
- Auth: [Add here]
- Authorization: [Add here]
- Search: [Add here]
- Logging/audit: [Add here]
- Reuse modules:
- [Add here]
- Add modules:
- [Add here]
- Do not touch: [Add here]

---

Step 12 Output - MVP Scope: In / Out / Later

        Control scope tightly and record what is intentionally deferred.

        ## Team Decision
        ## Bucket: In MVP
### Required
- **Items:** - [Add here]
- **Dependencies:** [Add here]
- **Risks:** [Add here]

### Optional
- **Manual workarounds allowed in MVP:** [Add here]

        ## MVP Only
        - If it is not required for launch, move it out of MVP. Preserve future ideas, but do not convert them into current commitments.

        ## Reuse Existing Code
        - Reuse current functionality where that avoids new scope. Do not create replacement work just to make the architecture cleaner.

        ## Copilot Handoff
        - Bucket: In MVP
- Items:
- [Add here]
- Dependencies: [Add here]
- Risks: [Add here]
- Manual workarounds: [Add here]

---

Step 13 Output - Final Design Guide Assembly

        Combine all prior outputs into one team-ready and Copilot-ready guide.

        ## Team Decision
        - Compile steps 1 through 12 into one clean MVP design guide.
- Keep names, roles, objects, pages, and rules consistent.
- Confirm the design remains MVP-focused.
- Confirm rewrite proposals are minimized and justified.
- Assumptions: [Add here]
- Open questions: [Add here]

        ## MVP Only
        - Final guide should be concise, MVP-focused, and discussion-ready. It should separate current scope from deferred ideas.

        ## Reuse Existing Code
        - Final guide should preserve the minimal-change strategy: extend existing code, avoid broad rewrites, and clearly mark untouched areas.

        ## Copilot Handoff
        - Final implementation slices:
- [Add here]
- Use previous step outputs as the source of truth for prompts.
- Keep task slices small and explicit.
