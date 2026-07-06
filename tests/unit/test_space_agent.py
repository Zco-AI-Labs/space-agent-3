import pytest
from unittest.mock import AsyncMock, MagicMock, patch
import datetime

# Mock the context before importing tools
from google.adk.tools.tool_context import ToolContext
import app.core.hubscape_adk

# Import tools
from app.scripts.get_nasa_apod import get_nasa_apod
from app.scripts.favorite_apod import favorite_apod
from app.scripts.list_favorites import list_favorites
from app.scripts.remove_favorite import remove_favorite

@pytest.mark.asyncio
@patch("httpx.AsyncClient.get")
@patch("app.core.hubscape_adk.get_context")
async def test_get_nasa_apod_image(mock_get_context, mock_httpx_get):
    # Setup mock RemoteContext
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

@pytest.mark.asyncio
@patch("httpx.AsyncClient.get")
@patch("app.core.hubscape_adk.get_context")
async def test_get_nasa_apod_video(mock_get_context, mock_httpx_get):
    # Setup mock RemoteContext
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

@pytest.mark.asyncio
@patch("app.core.hubscape_adk.get_context")
async def test_favorite_apod(mock_get_context):
    # Setup mock context
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

@pytest.mark.asyncio
@patch("app.core.hubscape_adk.get_context")
async def test_list_favorites(mock_get_context):
    # Setup mock context
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

@pytest.mark.asyncio
@patch("app.core.hubscape_adk.get_context")
async def test_remove_favorite(mock_get_context):
    # Setup mock context
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
