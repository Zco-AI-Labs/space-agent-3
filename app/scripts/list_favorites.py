import logging
from google.adk.tools.tool_context import ToolContext
import app.core.hubscape_adk

logger = logging.getLogger(__name__)

async def list_favorites(tool_context: ToolContext) -> dict:
    """
    Retrieves and displays the user's list of saved favorite NASA APOD pictures.
    """
    try:
        context = app.core.hubscape_adk.get_context()
        
        logger.info("Listing favorite APODs")
        favorites_list = context.list(scope="user", collection_name="favorites")
        
        # Sort favorites by date descending (newest first)
        sorted_favorites = sorted(
            favorites_list,
            key=lambda x: x.get("date", ""),
            reverse=True
        )
        
        rows = []
        for fav in sorted_favorites:
            date_str = fav.get("date")
            title_str = fav.get("title")
            
            rows.append({
                "date": date_str,
                "title": title_str,
                "actions": {
                    "type": "container",
                    "props": {
                        "className": "flex gap-2"
                    },
                    "children": [
                        {
                            "type": "button",
                            "props": {
                                "label": "View",
                                "actionUrl": f"agent://get_nasa_apod?date={date_str}",
                                "className": "text-indigo-600 dark:text-indigo-400 font-semibold text-xs bg-indigo-50 dark:bg-indigo-950/30 px-2 py-1 rounded hover:bg-indigo-100 dark:hover:bg-indigo-900/30 transition-colors"
                            }
                        },
                        {
                            "type": "button",
                            "props": {
                                "label": "Remove",
                                "actionUrl": f"agent://remove_favorite?date={date_str}",
                                "className": "text-red-600 dark:text-red-400 font-semibold text-xs bg-red-50 dark:bg-red-950/30 px-2 py-1 rounded hover:bg-red-100 dark:hover:bg-red-900/30 transition-colors"
                            }
                        }
                    ]
                }
            })
            
        # Register the favorites widget to display in the Chat UI
        context.show_widget("favorites_list", {"favorites_rows": rows})
        
        return {
            "status": "success",
            "count": len(sorted_favorites),
            "favorites": [
                {"date": f.get("date"), "title": f.get("title")} for f in sorted_favorites
            ]
        }
    except Exception as e:
        logger.error(f"Error listing favorite APODs: {e}", exc_info=True)
        return {
            "status": "error",
            "message": f"Failed to list favorites: {str(e)}"
        }
