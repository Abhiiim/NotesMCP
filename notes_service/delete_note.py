from typing import Any

from data.validations.validate_json_schema import validate_json_schema
from database.db import db_connection
from error.mcp_error import MCPError
from schemas.delete_note_schema import DELETE_NOTE_INPUT_SCHEMA, DELETE_NOTE_OUTPUT_SCHEMA


def delete_note(arguments: dict[str, Any]) -> dict[str, Any]:
    validate_json_schema(arguments, DELETE_NOTE_INPUT_SCHEMA)
    note_id = arguments["id"]

    with db_connection() as conn:
        cursor = conn.execute("DELETE FROM notes WHERE id = ?", (note_id,))
        if cursor.rowcount == 0:
            raise MCPError(-32001, "Note not found", {"id": note_id})
        conn.commit()

    result = {"id": note_id}
    validate_json_schema(result, DELETE_NOTE_OUTPUT_SCHEMA)
    return result
