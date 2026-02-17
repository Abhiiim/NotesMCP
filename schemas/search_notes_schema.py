from typing import Any


SEARCH_NOTES_INPUT_SCHEMA: dict[str, Any] = {
    "type": "object",
    "additionalProperties": False,
    "required": ["query"],
    "properties": {
        "query": {"type": "string", "minLength": 1},
    },
}

SEARCH_NOTES_OUTPUT_SCHEMA: dict[str, Any] = {
    "type": "object",
    "additionalProperties": False,
    "required": ["results"],
    "properties": {
        "results": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "required": ["id", "title", "snippet"],
                "properties": {
                    "id": {"type": "string", "minLength": 1},
                    "title": {"type": "string", "minLength": 1},
                    "snippet": {"type": "string"},
                },
            },
        }
    },
}