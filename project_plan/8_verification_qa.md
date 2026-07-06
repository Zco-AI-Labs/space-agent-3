## 🧪 8. Verification & QA Plan

We will test the Space Agent's behavior both using automated pytest suites and manual runs.

### Automated Tests
Run the test suite using pytest under the `uv` tool:
```bash
uv run pytest tests/
```

### Manual Verification Checklist
1.  `[ ]` **Q&A verification:** Query the agent on basic astronomy topics (e.g. "What is a light year?") and verify it answers accurately in natural language.
2.  `[ ]` **APOD retrieval verification:** Request today's APOD and verify the agent calls the NASA API, fetches the data, and displays the `apod_viewer` widget.
3.  `[ ]` **APOD specific date verification:** Request APOD for a specific valid date (e.g., "Show APOD for 2025-10-10") and verify it renders the correct card for that date.
4.  `[ ]` **Save Favorite verification:** Click the "Save to Favorites" button on an APOD widget, then check that the item is saved to user-scoped Firestore.
5.  `[ ]` **List Favorites verification:** Request "show favorites" and verify the `favorites_list` widget shows the saved entries.
6.  `[ ]` **Delete Favorite verification:** Delete an item from the favorites list and verify it is removed from Firestore.
7.  `[ ]` **SMS and Voice verification:** Verify that requests made on text-only channels receive plain-text messages instead of failing or displaying JSON formats.
