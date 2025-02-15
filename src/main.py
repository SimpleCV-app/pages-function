from appwrite.client import Client
import os

from appwrite.exception import AppwriteException
from appwrite.services.databases import Databases


def page_json(db: Databases, page: str):
    result = db.get_document(
        database_id=os.environ["MAIN_DB_ID"],
        collection_id='pages',
        document_id=page,
    )

    if result["published"] or result["type"] == "physical":
        db.update_document(
            database_id=os.environ["MAIN_DB_ID"],
            collection_id='pages',
            document_id=page,
            data={
                "views": result["views"] + 1
            }
        )

        return result
    else:
        raise AppwriteException("Document with requested ID not available.")


# This Appwrite function will be executed every time your function is triggered
def main(context):
    # You can use the Appwrite SDK to interact with other services
    # For this example, we're using the Users service
    client = (
        Client()
        .set_endpoint(os.environ["APPWRITE_FUNCTION_API_ENDPOINT"])
        .set_project(os.environ["APPWRITE_FUNCTION_PROJECT_ID"])
        .set_key(context.req.headers["x-appwrite-key"])
    )
    databases = Databases(client)

    path = context.req.path.split("/")
    path.pop(0)
    page_id = path[0]
    action = None

    try:
        page = page_json(databases, page_id)
    except AppwriteException:
        return context.res.json(
            {
                "error": "no_page",
                "description": "No page could be found",
                "code": 404
            },
            404
        )

    try:
        action = path[1]
    except IndexError:
        pass

    if page_id == "favicon.ico":
        return context.res.empty()

    if action is None:
        return context.res.text(page_id)
    elif action == "raw":
        try:
            return context.res.json(page)
        except AppwriteException:
            return context.res.jso
    else:
        return context.res.json(
            {
                "error": "no_action",
                "description": "No action could be found",
                "code": 404
            },
            404
        )

