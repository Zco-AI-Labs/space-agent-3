## 💾 6. Data Architecture & DB Schemas

We will store user-scoped favorites in Firestore.

### Collection: `favorites`
*   **Scope:** `user`
*   **Document ID Format:** `fav_{date}` (e.g. `fav_2026-07-06`)

#### Fields Table
| Field Name | Type | Description | Mandatory / Optional |
| :--- | :--- | :--- | :--- |
| `id` | `String` | Document ID duplicated in payload (`fav_{date}`) | Mandatory |
| `date` | `String` | The date of the APOD (YYYY-MM-DD) | Mandatory |
| `title` | `String` | The title of the APOD | Mandatory |
| `media_url` | `String` | The URL of the image or video | Mandatory |
| `media_type` | `String` | The type of media ('image' or 'video') | Mandatory |
| `created_at` | `Timestamp` | Injected automatically by context helpers | Mandatory |
| `created_by` | `String` | Injected automatically by context helpers | Mandatory |
| `updated_at` | `Timestamp` | Injected automatically by context helpers | Mandatory |
| `updated_by` | `String` | Injected automatically by context helpers | Mandatory |
| `version` | `Integer` | Injected automatically by context helpers | Mandatory |
