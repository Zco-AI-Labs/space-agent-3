import logging
from google.adk.tools.tool_context import ToolContext
import app.core.hubscape_adk
from app.scripts.list_favorites import list_favorites

logger = logging.getLogger(__name__)

async def remove_favorite(tool_context: ToolContext, date: str) -> dict:
    """
    Removes a saved APOD picture from the user's favorites.

    Args:
        date: The date of the APOD to remove (YYYY-MM-DD).
    """
    try:
        context = app.core.hubscape_adk.get_context()
        doc_id = f"fav_{date}"
        
        logger.info(f"Removing APOD from favorites: {doc_id}")
        context.delete(
            scope="user",
            collection_name="favorites",
            doc_id=doc_id
        )
        
        # Automatically refresh the favorites list widget to provide immediate feedback
        await list_favorites(tool_context)
        
        return {
            "status": "success",
            "message": f"Successfully removed the favorite for date {date}."
        }
    except Exception as e:
        logger.error(f"Error removing favorite APOD: {e}", exc_info=True)
        return {
            "status": "error",
            "message": f"Failed to remove favorite: {str(e)}"
        }
