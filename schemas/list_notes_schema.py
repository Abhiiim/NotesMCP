from typing import Any


LIST_NOTES_INPUT_SCHEMA: dict[str, Any] = {
    "type": "object",
    "additionalProperties": False,
    "properties": {},
}

LIST_NOTES_OUTPUT_SCHEMA: dict[str, Any] = {
    "type": "object",
    "additionalProperties": False,
    "required": ["notes"],
    "properties": {
        "notes": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "required": ["id", "title", "created_at"],
                "properties": {
                    "id": {"type": "string", "minLength": 1},
                    "title": {"type": "string", "minLength": 1},
                    "created_at": {"type": "string", "format": "date-time"},
                },
            },
        }
    },
}