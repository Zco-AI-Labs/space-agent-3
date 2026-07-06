## 🛠️ 5. Architecture & Capabilities

### System Instructions (`app/SKILL.md`)
```text
You are the Space Agent, a knowledgeable and friendly astronomy assistant.
Your job is to answer questions about astronomy, space exploration, cosmology, and astrophysics.
You also provide users with NASA's Astronomy Picture of the Day (APOD) and help them manage their saved favorites list.

Instructions:
1. When asked general space/astronomy questions, answer them clearly and accurately.
2. When asked for NASA's Picture of the Day, call the `get_nasa_apod` tool. If a date is provided, use it. If not, default to the current local date (today is 2026-07-06).
3. If the user likes an APOD, help them save it to their favorites by calling the `favorite_apod` tool.
4. If the user wants to see their saved favorites, call the `list_favorites` tool.
5. If the user wants to remove a favorite, call the `remove_favorite` tool.
```

### Tool Implementations (`app/scripts/`)

#### `app/scripts/get_nasa_apod.py`
```python
from google.adk.tools.tool_context import ToolContext

async def get_nasa_apod(tool_context: ToolContext, date: str = None) -> dict:
    """
    Fetches NASA's Astronomy Picture of the Day (APOD) for a given date (YYYY-MM-DD) or today.

    Args:
        date: Optional date in YYYY-MM-DD format. Defaults to today's date if not provided.
    """
```

#### `app/scripts/favorite_apod.py`
```python
from google.adk.tools.tool_context import ToolContext

async def favorite_apod(tool_context: ToolContext, date: str, title: str, media_url: str, media_type: str) -> dict:
    """
    Saves a NASA APOD image to the user's private favorites.

    Args:
        date: The date of the APOD in YYYY-MM-DD format.
        title: The title of the APOD.
        media_url: The image or video URL of the APOD.
        media_type: The type of media (e.g., 'image' or 'video').
    """
```

#### `app/scripts/list_favorites.py`
```python
from google.adk.tools.tool_context import ToolContext

async def list_favorites(tool_context: ToolContext) -> dict:
    """
    Retrieves the user's list of saved favorite NASA APOD pictures.
    """
```

#### `app/scripts/remove_favorite.py`
```python
from google.adk.tools.tool_context import ToolContext

async def remove_favorite(tool_context: ToolContext, date: str) -> dict:
    """
    Removes a saved APOD picture from the user's favorites.

    Args:
        date: The date of the APOD to remove in YYYY-MM-DD format.
    """
```

### 🔑 Tool Permissions Matrix
No special admin permissions are required. Standard logged-in user capability is sufficient.

| Permission Name | Description of Granted Capabilities / Tools |
| :--- | :--- |
| `USER` | Standard user can query APOD, view, save, and delete their own favorites. |

### Model Context Protocol (MCP) & Agent-to-Agent (A2A) Connections
None.

### Required Secrets (Agent Secrets Vault)

| Secret Name | Description | Required? (True/False) |
| :--- | :--- | :--- |
| `NASA_API_KEY` | The API Key to query NASA APIs. Defaults to 'DEMO_KEY' if not configured. | False |
