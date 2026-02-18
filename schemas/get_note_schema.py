from typing import Any


GET_NOTE_INPUT_SCHEMA: dict[str, Any] = {
    "type": "object",
    "additionalProperties": False,
    "required": ["id"],
    "properties": {
        "id": {"type": "string", "minLength": 1},
    },
}

GET_NOTE_OUTPUT_SCHEMA: dict[str, Any] = {
    "type": "object",
    "additionalProperties": False,
    "required": ["id", "title", "content", "created_at"],
    "properties": {
        "id": {"type": "string", "minLength": 1},
        "title": {"type": "string", "minLength": 1},
        "content": {"type": "string"},
        "created_at": {"type": "string", "format": "date-time"},
    },
}
