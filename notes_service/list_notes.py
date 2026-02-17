from typing import Any

from data.validations.validate_json_schema import validate_json_schema
from database.db import db_connection
from schemas.list_notes_schema import LIST_NOTES_INPUT_SCHEMA, LIST_NOTES_OUTPUT_SCHEMA


def list_notes(arguments: dict[str, Any]) -> dict[str, Any]:
    validate_json_schema(arguments, LIST_NOTES_INPUT_SCHEMA)

    with db_connection() as conn:
        rows = conn.execute(
            "SELECT id, title, created_at FROM notes ORDER BY created_at ASC, id ASC"
        ).fetchall()

    result = {
        "notes": [
            {"id": row["id"], "title": row["title"], "created_at": row["created_at"]}
            for row in rows
        ]
    }
    validate_json_schema(result, LIST_NOTES_OUTPUT_SCHEMA)
    return result
