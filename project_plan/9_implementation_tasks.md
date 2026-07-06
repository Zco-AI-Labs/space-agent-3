## 📋 9. Implementation Tasks

### Phase 1: Configuration & Metadata
- [ ] Initialize name and description in `app/agent.py`.
- [ ] Ensure name metadata in `pyproject.toml` and `agents-cli-manifest.yaml` are synced to `"space-agent"`.

### Phase 2: Business Logic & Tool Implementation
- [ ] Initialize system instructions inside `app/SKILL.md`.
- [ ] Implement `app/scripts/get_nasa_apod.py` to query the NASA APOD API, handle errors, and show the `apod_viewer` widget.
- [ ] Implement `app/scripts/favorite_apod.py` to save the selected picture details to user-scoped Firestore.
- [ ] Implement `app/scripts/list_favorites.py` to retrieve and format favorites as table rows for the `favorites_list` widget.
- [ ] Implement `app/scripts/remove_favorite.py` to remove a specific date from the user's favorites in Firestore.
- [ ] Register all new tools in `app/agent.py`.

### Phase 3: UI/Widgets Definition
- [ ] Create `app/core/widgets/apod_viewer.json` with the Indigo-themed detail card.
- [ ] Create `app/core/widgets/favorites_list.json` with the Indigo-themed data table.

### Phase 4: Verification & Testing
- [ ] Write pytest test cases under `tests/unit/` to verify each tool function in isolation (mocking `ToolContext` and the NASA API).
- [ ] Run the local sandbox tool `hubscape-adk` to verify chat interactions and visual widgets.
