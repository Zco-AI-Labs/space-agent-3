import asyncio
import sys
import logging
from unittest.mock import MagicMock, patch
from google.adk.tools.tool_context import ToolContext

# Configure basic logging
logging.basicConfig(level=logging.INFO)

# Import tools
from app.scripts.get_nasa_apod import get_nasa_apod
from app.scripts.favorite_apod import favorite_apod
from app.scripts.list_favorites import list_favorites
from app.scripts.remove_favorite import remove_favorite

async def test_get_nasa_apod_image():
    # Setup mock RemoteContext
    with patch("app.core.hubscape_adk.get_context") as mock_get_context, \
         patch("httpx.AsyncClient.get") as mock_httpx_get:
        
        mock_context = MagicMock()
        mock_context.get_agent_secret.return_value = "TEST_KEY"
        mock_get_context.return_value = mock_context
        
        # Setup mock HTTP response for image
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "title": "The Pillars of Creation",
            "url": "https://apod.nasa.gov/image.jpg",
            "explanation": "Test explanation.",
            "media_type": "image"
        }
        mock_httpx_get.return_value = mock_response
        
        # Run tool
        tool_context = MagicMock(spec=ToolContext)
        res = await get_nasa_apod(tool_context, date="2026-07-06")
        
        # Assertions
        assert res["status"] == "success"
        assert res["title"] == "The Pillars of Creation"
        assert res["media_type"] == "image"
        
        # Verify widget was displayed
        mock_context.show_widget.assert_called_once_with(
            "apod_image_viewer",
            {
                "title": "The Pillars of Creation",
                "date": "2026-07-06",
                "media_url": "https://apod.nasa.gov/image.jpg",
                "explanation": "Test explanation.",
                "media_type": "image"
            }
        )

async def test_get_nasa_apod_video():
    # Setup mock RemoteContext
    with patch("app.core.hubscape_adk.get_context") as mock_get_context, \
         patch("httpx.AsyncClient.get") as mock_httpx_get:
         
        mock_context = MagicMock()
        mock_context.get_agent_secret.return_value = "TEST_KEY"
        mock_get_context.return_value = mock_context
        
        # Setup mock HTTP response for video
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "title": "Space Video",
            "url": "https://youtube.com/embed/123",
            "explanation": "Test video explanation.",
            "media_type": "video"
        }
        mock_httpx_get.return_value = mock_response
        
        # Run tool
        tool_context = MagicMock(spec=ToolContext)
        res = await get_nasa_apod(tool_context, date="2026-07-06")
        
        # Assertions
        assert res["status"] == "success"
        assert res["title"] == "Space Video"
        assert res["media_type"] == "video"
        
        # Verify video widget was displayed
        mock_context.show_widget.assert_called_once_with(
            "apod_video_viewer",
            {
                "title": "Space Video",
                "date": "2026-07-06",
                "media_url": "https://youtube.com/embed/123",
                "explanation": "Test video explanation.",
                "media_type": "video"
            }
        )

async def test_favorite_apod():
    # Setup mock context
    with patch("app.core.hubscape_adk.get_context") as mock_get_context:
        mock_context = MagicMock()
        mock_context.save.return_value = {"id": "fav_2026-07-06", "title": "Test"}
        mock_get_context.return_value = mock_context
        
        tool_context = MagicMock(spec=ToolContext)
        res = await favorite_apod(
            tool_context,
            date="2026-07-06",
            title="Test Title",
            media_url="https://apod.nasa.gov/image.jpg",
            media_type="image"
        )
        
        assert res["status"] == "success"
        mock_context.save.assert_called_once_with(
            scope="user",
            collection_name="favorites",
            doc_id="fav_2026-07-06",
            data={
                "id": "fav_2026-07-06",
                "date": "2026-07-06",
                "title": "Test Title",
                "media_url": "https://apod.nasa.gov/image.jpg",
                "media_type": "image"
            }
        )

async def test_list_favorites():
    # Setup mock context
    with patch("app.core.hubscape_adk.get_context") as mock_get_context:
        mock_context = MagicMock()
        mock_context.list.return_value = [
            {"date": "2026-07-05", "title": "Orion Nebula", "media_url": "url2", "media_type": "image"},
            {"date": "2026-07-06", "title": "Pillars of Creation", "media_url": "url1", "media_type": "image"}
        ]
        mock_get_context.return_value = mock_context
        
        tool_context = MagicMock(spec=ToolContext)
        res = await list_favorites(tool_context)
        
        assert res["status"] == "success"
        assert res["count"] == 2
        # Verify sorted output: newest date (07-06) first
        assert res["favorites"][0]["date"] == "2026-07-06"
        assert res["favorites"][1]["date"] == "2026-07-05"
        
        # Verify widget registration
        mock_context.show_widget.assert_called_once()
        args, kwargs = mock_context.show_widget.call_args
        assert args[0] == "favorites_list"
        assert len(args[1]["favorites_rows"]) == 2
        # Newest item first in rows
        assert args[1]["favorites_rows"][0]["date"] == "2026-07-06"

async def test_remove_favorite():
    # Setup mock context
    with patch("app.core.hubscape_adk.get_context") as mock_get_context:
        mock_context = MagicMock()
        mock_context.list.return_value = []
        mock_get_context.return_value = mock_context
        
        tool_context = MagicMock(spec=ToolContext)
        res = await remove_favorite(tool_context, date="2026-07-06")
        
        assert res["status"] == "success"
        mock_context.delete.assert_called_once_with(
            scope="user",
            collection_name="favorites",
            doc_id="fav_2026-07-06"
        )
        mock_context.list.assert_called_once_with(
            scope="user",
            collection_name="favorites"
        )

async def main():
    print("Executing Space Agent custom test suite...")
    tests = [
        ("test_get_nasa_apod_image", test_get_nasa_apod_image),
        ("test_get_nasa_apod_video", test_get_nasa_apod_video),
        ("test_favorite_apod", test_favorite_apod),
        ("test_list_favorites", test_list_favorites),
        ("test_remove_favorite", test_remove_favorite),
    ]
    
    passed_all = True
    for name, test_func in tests:
        try:
            print(f"Running {name}...", end="")
            await test_func()
            print(" PASSED")
        except Exception as e:
            print(f" FAILED\nError: {e}")
            passed_all = False
            
    if passed_all:
        print("\nAll tests completed successfully!")
        sys.exit(0)
    else:
        print("\nSome tests failed.")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())
