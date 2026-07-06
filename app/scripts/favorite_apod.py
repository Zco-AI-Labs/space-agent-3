import logging
from google.adk.tools.tool_context import ToolContext
import app.core.hubscape_adk

logger = logging.getLogger(__name__)

async def favorite_apod(tool_context: ToolContext, date: str, title: str, media_url: str, media_type: str) -> dict:
    """
    Saves an Astronomy Picture of the Day (APOD) to the user's favorites.

    Args:
        date: The date of the APOD (YYYY-MM-DD).
        title: The title of the APOD.
        media_url: The image or video URL.
        media_type: The type of media ('image' or 'video').
    """
    try:
        context = app.core.hubscape_adk.get_context()
        
        doc_id = f"fav_{date}"
        data = {
            "id": doc_id,
            "date": date,
            "title": title,
            "media_url": media_url,
            "media_type": media_type
        }
        
        logger.info(f"Saving APOD to favorites: {doc_id}")
        saved_data = context.save(
            scope="user",
            collection_name="favorites",
            doc_id=doc_id,
            data=data
        )
        
        return {
            "status": "success",
            "message": f"Saved '{title}' to your favorites!",
            "favorite": saved_data
        }
    except Exception as e:
        logger.error(f"Error saving favorite APOD: {e}", exc_info=True)
        return {
            "status": "error",
            "message": f"Failed to save to favorites: {str(e)}"
        }
