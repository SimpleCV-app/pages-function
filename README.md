# Pages

## 🧰 Usage

### GET /{page}

- Returns either the HTML page or a PDF file.

### GET /{page}/raw

- Returns the raw JSON page

**Response**

Sample `200` Response:

```json
{
  "views": 4,
  "type": "digital",
  "uid": "x",
  "published": true,
  "title": "Test Digital CV",
  "cover_letter": "Test Digital CV",
  "template": null,
  "ctr": 0,
  "$id": "x",
  "$createdAt": "2025-02-08T17:32:48.169+00:00",
  "$updatedAt": "2025-02-15T00:14:28.287+00:00",
  "$permissions": [
    "update(\"user:x\")",
    "delete(\"user:x\")",
    "read(\"user:x\")"
  ],
  "contact_details": [],
  "work_experience": [],
  "education": [],
  "skills": [],
  "reference": [],
  "$databaseId": "cvb-db0",
  "$collectionId": "pages"
}
```

## ⚙️ Configuration

| Setting           | Value                             |
| ----------------- |-----------------------------------|
| Runtime           | Python (3.12)                     |
| Entrypoint        | `src/main.py`                     |
| Build Commands    | `pip install -r requirements.txt` |
| Permissions       | `any`                             |
| Timeout (Seconds) | 15                                |

## 🔒 Environment Variables

| Environment Variable |
|----------------------|
| MAIN_DB_ID           |