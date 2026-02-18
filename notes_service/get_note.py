from typing import Any

from data.validations.validate_json_schema import validate_json_schema
from database.db import db_connection
from error.mcp_error import MCPError
from schemas.get_note_schema import GET_NOTE_INPUT_SCHEMA, GET_NOTE_OUTPUT_SCHEMA


def get_note(arguments: dict[str, Any]) -> dict[str, Any]:
    validate_json_schema(arguments, GET_NOTE_INPUT_SCHEMA)
    note_id = arguments["id"]

    with db_connection() as conn:
        row = conn.execute(
            "SELECT id, title, content, created_at FROM notes WHERE id = ?",
            (note_id,),
        ).fetchone()

    if row is None:
        raise MCPError(-32001, "Note not found", {"id": note_id})

    result = {
        "id": row["id"],
        "title": row["title"],
        "content": row["content"],
        "created_at": row["created_at"],
    }
    validate_json_schema(result, GET_NOTE_OUTPUT_SCHEMA)
    return result
