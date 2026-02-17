from typing import Any


ADD_NOTE_INPUT_SCHEMA: dict[str, Any] = {
    "type": "object",
    "additionalProperties": False,
    "required": ["title", "content"],
    "properties": {
        "title": {"type": "string", "minLength": 1},
        "content": {"type": "string"},
    },
}

ADD_NOTE_OUTPUT_SCHEMA: dict[str, Any] = {
    "type": "object",
    "additionalProperties": False,
    "required": ["id", "created_at"],
    "properties": {
        "id": {"type": "string", "minLength": 1},
        "created_at": {"type": "string", "format": "date-time"},
    },
}