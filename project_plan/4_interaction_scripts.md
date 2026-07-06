## 💬 4. Interaction Scripts & Conversational Flows

### Scenario 1: Fetching and Saving NASA's Picture of the Day

#### Flow A: Visual Path (Chat UI with widgets)
*   **User:** "Show me today's picture of the day."
*   **Agent (Behind the Scenes):** Calls tool `get_nasa_apod` with arguments `{"date": "2026-07-06"}`.
*   **Agent UI Rendered:** Displays Widget `apod_viewer` with the NASA APOD data.
*   **Agent Message:** "Here is today's NASA Astronomy Picture of the Day: **The Pillars of Creation**."
*   **User clicks button:** Clicks the "Favorite" button on the card.
*   **Agent (Behind the Scenes):** Calls tool `favorite_apod` with arguments `{"date": "2026-07-06", "title": "The Pillars of Creation", "media_url": "https://apod.nasa.gov/apod/image/2607/pillars_heritage.jpg", "media_type": "image"}`.
*   **Agent Message:** "Successfully added 'The Pillars of Creation' to your favorites!"

#### Flow B: Non-Visual SMS Path (No-UI, Text Only)
*   **User (SMS):** "Show me today's picture of the day."
*   **Agent (Behind the Scenes):** Calls tool `get_nasa_apod` with arguments `{"date": "2026-07-06"}`.
*   **Agent Text Reply:** "NASA's Astronomy Picture of the Day (2026-07-06): 'The Pillars of Creation'. Image URL: https://apod.nasa.gov/apod/image/2607/pillars_heritage.jpg. Explanation: These stellar pillars are in the Eagle Nebula. Reply 'favorite 2026-07-06' to save it to your favorites."

#### Flow C: Non-Visual Voice Path (No-UI, Spoken Phone Call)
*   **User (Voice):** "What is today's picture of the day?"
*   **Agent (Behind the Scenes):** Calls tool `get_nasa_apod` with arguments `{"date": "2026-07-06"}`.
*   **Agent Speech Reply:** "Today's astronomy picture of the day is titled, 'The Pillars of Creation'. It depicts columns of interstellar gas and dust in the Eagle Nebula where new stars are forming. Would you like me to save this to your favorites?"

---

### Scenario 2: Viewing Favorites

#### Flow A: Visual Path (Chat UI with widgets)
*   **User:** "Show my favorites."
*   **Agent (Behind the Scenes):** Calls tool `list_favorites`.
*   **Agent UI Rendered:** Displays Widget `favorites_list` showing a table of saved pictures.
*   **Agent Message:** "Here are your saved NASA pictures of the day."

#### Flow B: Non-Visual SMS Path (No-UI, Text Only)
*   **User (SMS):** "show my favorites"
*   **Agent (Behind the Scenes):** Calls tool `list_favorites`.
*   **Agent Text Reply:** "Your saved favorites:\n- 2026-07-06: The Pillars of Creation\n- 2026-07-05: The Orion Nebula"

#### Flow C: Non-Visual Voice Path (No-UI, Spoken Phone Call)
*   **User (Voice):** "Read my favorites."
*   **Agent (Behind the Scenes):** Calls tool `list_favorites`.
*   **Agent Speech Reply:** "You have two saved favorites. The first is The Pillars of Creation from July sixth, and the second is The Orion Nebula from July fifth. Would you like details on either of these?"
