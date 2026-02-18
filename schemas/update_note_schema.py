from typing import Any


UPDATE_NOTE_INPUT_SCHEMA: dict[str, Any] = {
    "type": "object",
    "additionalProperties": False,
    "required": ["id", "title", "content"],
    "properties": {
        "id": {"type": "string", "minLength": 1},
        "title": {"type": "string", "minLength": 1},
        "content": {"type": "string"},
    },
}

UPDATE_NOTE_OUTPUT_SCHEMA: dict[str, Any] = {
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
