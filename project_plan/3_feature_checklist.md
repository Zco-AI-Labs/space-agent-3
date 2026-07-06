## 📂 3. Feature Checklist & Interaction Modes

### Feature 1: Astronomy Q&A
*   **Description:** Answers general astronomy, astrophysics, planetary science, and space exploration questions using the model's knowledge.
*   **Visual Interaction Mode:**
    *   *Trigger:* User asks a space-related question in the chat interface (e.g., "Why is Mars red?").
    *   *UI Rendered:* Standard conversational message response.
    *   *Form Actions:* None.
*   **Non-Visual Interaction Mode (SMS/Voice Fallback):**
    *   *SMS Transcript Flow:* User texts: "Why is Mars red?" -> Agent texts back a concise answer.
    *   *Voice/Phone Flow:* User speaks: "Why is Mars red?" -> Agent responds verbally with a concise, easy-to-understand explanation.
    *   *Natural Language Parameters Extracted:* `question`
*   **Acceptance Criteria (Given-When-Then):**
    *   *Scenario A (Happy Path):*
        *   **GIVEN** the user asks a valid astronomy question,
        *   **WHEN** the agent processes the prompt,
        *   **THEN** the model answers accurately using its space science knowledge base.

---

### Feature 2: Get NASA Picture of the Day (APOD)
*   **Description:** Fetches NASA's Astronomy Picture of the Day (APOD) for a given date or today, displaying the image/video, title, and educational explanation.
*   **Visual Interaction Mode:**
    *   *Trigger:* User asks "Show me the picture of the day" or "Show NASA APOD for 2025-12-25".
    *   *UI Rendered:* Renders a custom APOD widget (title, media preview, explanation description, date, and a "Favorite" action button).
    *   *Form Actions:* Click "Favorite" button to trigger saving the picture.
*   **Non-Visual Interaction Mode (SMS/Voice Fallback):**
    *   *SMS Transcript Flow:* User texts: "Show picture of the day" -> Agent texts: "NASA's Picture of the Day (2026-07-06): 'The Pillars of Creation'. Image link: https://apod.nasa.gov/... Description: ..."
    *   *Voice/Phone Flow:* User speaks: "What is today's picture of the day?" -> Agent says: "Today's picture is called 'The Pillars of Creation'. It shows star-forming regions in the Eagle Nebula. Would you like me to read the full description?"
    *   *Natural Language Parameters Extracted:* `date` (optional, default to today)
*   **Acceptance Criteria (Given-When-Then):**
    *   *Scenario A (Happy Path):*
        *   **GIVEN** the NASA APOD API is accessible and the date is valid,
        *   **WHEN** the user requests the APOD,
        *   **THEN** the agent calls the NASA API, retrieves the metadata, and renders the APOD widget showing the title, media, and description.
    *   *Scenario B (API Error / Rate Limit):*
        *   **GIVEN** the NASA APOD API fails or returns a rate limit error,
        *   **WHEN** the user requests the APOD,
        *   **THEN** the agent falls back to a descriptive error message and offers to try again later.

---

### Feature 3: Manage Favorite APODs
*   **Description:** Allows users to save specific APOD images to their private `user` scope database and view their saved list.
*   **Visual Interaction Mode:**
    *   *Trigger:* User clicks "Favorite" on an APOD card, or says "Save this picture", or "Show my favorites".
    *   *UI Rendered:* Displays a favorites list widget containing a table or card grid of saved APODs.
    *   *Form Actions:* Click on a favorite row to re-view it, or click a "Remove" button to delete it from favorites.
*   **Non-Visual Interaction Mode (SMS/Voice Fallback):**
    *   *SMS Transcript Flow:* User texts: "Show favorites" -> Agent texts: "Here are your saved favorites: 1. 2026-07-05: The Orion Nebula. 2. 2026-07-01: Jupiter's Storms."
    *   *Voice/Phone Flow:* User speaks: "List my favorite pictures" -> Agent says: "You have 2 saved favorites: The Orion Nebula from July 5th, and Jupiter's Storms from July 1st. Would you like details on one of them?"
    *   *Natural Language Parameters Extracted:* `action` (save/list/remove), `date` (for save/remove)
*   **Acceptance Criteria (Given-When-Then):**
    *   *Scenario A (Happy Path):*
        *   **GIVEN** a valid APOD date and title,
        *   **WHEN** the user saves it,
        *   **THEN** the agent writes it to Firestore under the user's private agent data scope and displays a success confirmation.
