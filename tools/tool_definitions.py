from typing import Any
from schemas.add_note_schema import ADD_NOTE_INPUT_SCHEMA, ADD_NOTE_OUTPUT_SCHEMA
from schemas.list_notes_schema import LIST_NOTES_INPUT_SCHEMA, LIST_NOTES_OUTPUT_SCHEMA
from schemas.search_notes_schema import SEARCH_NOTES_INPUT_SCHEMA, SEARCH_NOTES_OUTPUT_SCHEMA


TOOL_DEFINITIONS: list[dict[str, Any]] = [
    {
        "name": "add_note",
        "description": "Create and persist a new note.",
        "inputSchema": ADD_NOTE_INPUT_SCHEMA,
        "outputSchema": ADD_NOTE_OUTPUT_SCHEMA,
    },
    {
        "name": "list_notes",
        "description": "List all stored notes with minimal metadata.",
        "inputSchema": LIST_NOTES_INPUT_SCHEMA,
        "outputSchema": LIST_NOTES_OUTPUT_SCHEMA,
    },
    {
        "name": "search_notes",
        "description": "Search notes by keyword match over title and content.",
        "inputSchema": SEARCH_NOTES_INPUT_SCHEMA,
        "outputSchema": SEARCH_NOTES_OUTPUT_SCHEMA,
    },
]