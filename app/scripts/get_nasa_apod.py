import datetime
import logging
import httpx
from google.adk.tools.tool_context import ToolContext
import app.core.hubscape_adk

logger = logging.getLogger(__name__)

async def get_nasa_apod(tool_context: ToolContext, date: str = None) -> dict:
    """
    Fetches NASA's Astronomy Picture of the Day (APOD) for a given date or today.

    Args:
        date: Optional. The date in YYYY-MM-DD format. Defaults to today's date.
    """
    try:
        context = app.core.hubscape_adk.get_context()
        api_key = context.get_agent_secret("NASA_API_KEY") or "DEMO_KEY"

        if not date:
            date = datetime.date.today().isoformat()

        logger.info(f"Fetching NASA APOD for date: {date}")
        url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}&date={date}"

        async with httpx.AsyncClient() as client:
            response = await client.get(url, timeout=10.0)

        if response.status_code != 200:
            logger.error(f"NASA APOD API returned status {response.status_code}: {response.text}")
            return {
                "status": "error",
                "message": f"NASA API returned status code {response.status_code}."
            }

        data = response.json()
        title = data.get("title", "")
        media_url = data.get("url", "")
        explanation = data.get("explanation", "")
        media_type = data.get("media_type", "image")

        widget_data = {
            "title": title,
            "date": date,
            "media_url": media_url,
            "explanation": explanation,
            "media_type": media_type
        }

        # Choose widget template based on media type
        if media_type == "video":
            context.show_widget("apod_video_viewer", widget_data)
        else:
            context.show_widget("apod_image_viewer", widget_data)

        return {
            "status": "success",
            "date": date,
            "title": title,
            "media_url": media_url,
            "media_type": media_type,
            "explanation": explanation
        }

    except Exception as e:
        logger.error(f"Error fetching NASA APOD: {e}", exc_info=True)
        return {
            "status": "error",
            "message": f"Failed to fetch APOD: {str(e)}"
        }
