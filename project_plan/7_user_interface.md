## 🎨 7. User Interface & Widgets Specification

We will define two Lego UI widgets:
1. `apod_viewer`: To display the Astronomy Picture of the Day.
2. `favorites_list`: To display the user's saved favorites.

### Widget 1: `apod_viewer`
*   **Type:** Detail Card
*   **Theme Token Default:** `indigo`
*   **Layout JSON Structure:**
```json
{
  "type": "container",
  "props": {
    "className": "flex flex-col gap-4 p-4 bg-slate-50 dark:bg-slate-900 rounded-xl border border-slate-200 dark:border-slate-800"
  },
  "children": [
    {
      "type": "text",
      "props": {
        "text": "{{title}}",
        "className": "text-xl font-bold text-slate-900 dark:text-white"
      }
    },
    {
      "type": "text",
      "props": {
        "text": "Date: {{date}}",
        "className": "text-xs text-slate-500 dark:text-slate-400 font-medium"
      }
    },
    {
      "type": "image",
      "props": {
        "src": "{{media_url}}",
        "alt": "{{title}}",
        "className": "w-full max-h-[400px] object-cover rounded-lg border border-slate-100 dark:border-slate-800"
      }
    },
    {
      "type": "text",
      "props": {
        "text": "{{explanation}}",
        "className": "text-sm text-slate-700 dark:text-slate-300 leading-relaxed"
      }
    },
    {
      "type": "button",
      "props": {
        "label": "Save to Favorites",
        "actionUrl": "agent://favorite_apod?date={{date}}&title={{title}}&media_url={{media_url}}&media_type={{media_type}}",
        "className": "bg-indigo-600 hover:bg-indigo-700 text-white px-4 py-2 rounded-lg font-medium transition-colors"
      }
    }
  ]
}
```

---

### Widget 2: `favorites_list`
*   **Type:** Data Table
*   **Theme Token Default:** `indigo`
*   **Layout JSON Structure:**
```json
{
  "type": "container",
  "props": {
    "className": "flex flex-col gap-4 p-4 bg-slate-50 dark:bg-slate-900 rounded-xl border border-slate-200 dark:border-slate-800"
  },
  "children": [
    {
      "type": "text",
      "props": {
        "text": "Your Favorite Space Pictures",
        "className": "text-lg font-bold text-slate-900 dark:text-white"
      }
    },
    {
      "type": "table",
      "props": {
        "paginated": true,
        "pageSize": 5,
        "columns": [
          { "key": "date", "name": "Date", "width": "25%" },
          { "key": "title", "name": "Title", "width": "50%" },
          { "key": "actions", "name": "Actions", "width": "25%" }
        ],
        "rows": "{{favorites_rows}}"
      }
    }
  ]
}
```
*Note: `favorites_rows` will be a dynamically constructed list of rows in python, where each row contains the fields `date`, `title`, and custom action buttons nested in `actions` to re-view or remove that favorite.*
