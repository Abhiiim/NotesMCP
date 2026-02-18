from typing import Any

from data.validations.validate_json_schema import validate_json_schema
from database.db import db_connection
from error.mcp_error import MCPError
from schemas.update_note_schema import UPDATE_NOTE_INPUT_SCHEMA, UPDATE_NOTE_OUTPUT_SCHEMA


def update_note(arguments: dict[str, Any]) -> dict[str, Any]:
    validate_json_schema(arguments, UPDATE_NOTE_INPUT_SCHEMA)

    note_id = arguments["id"]
    title = arguments["title"]
    content = arguments["content"]

    with db_connection() as conn:
        cursor = conn.execute(
            "UPDATE notes SET title = ?, content = ? WHERE id = ?",
            (title, content, note_id),
        )
        if cursor.rowcount == 0:
            raise MCPError(-32001, "Note not found", {"id": note_id})

        row = conn.execute(
            "SELECT id, title, content, created_at FROM notes WHERE id = ?",
            (note_id,),
        ).fetchone()
        conn.commit()

    if row is None:
        raise MCPError(-32603, "Internal error", {"reason": "Updated note missing"})

    result = {
        "id": row["id"],
        "title": row["title"],
        "content": row["content"],
        "created_at": row["created_at"],
    }
    validate_json_schema(result, UPDATE_NOTE_OUTPUT_SCHEMA)
    return result
