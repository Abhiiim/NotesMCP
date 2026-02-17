from typing import Any
import uuid
from data.validations.validate_json_schema import validate_json_schema
from database.db import db_connection
from schemas.add_note_schema import ADD_NOTE_INPUT_SCHEMA, ADD_NOTE_OUTPUT_SCHEMA
from utils.time_utils import current_timestamp


def add_note(arguments: dict[str, Any]) -> dict[str, Any]:
    validate_json_schema(arguments, ADD_NOTE_INPUT_SCHEMA)

    note_id = str(uuid.uuid4())
    created_at = current_timestamp()
    title = arguments["title"]
    content = arguments["content"]

    with db_connection() as conn:
        conn.execute(
            "INSERT INTO notes (id, title, content, created_at) VALUES (?, ?, ?, ?)",
            (note_id, title, content, created_at),
        )
        conn.commit()

    result = {"id": note_id, "created_at": created_at}
    validate_json_schema(result, ADD_NOTE_OUTPUT_SCHEMA)
    return result
