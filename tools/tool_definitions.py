from typing import Any
from schemas.add_note_schema import ADD_NOTE_INPUT_SCHEMA, ADD_NOTE_OUTPUT_SCHEMA
from schemas.delete_note_schema import DELETE_NOTE_INPUT_SCHEMA, DELETE_NOTE_OUTPUT_SCHEMA
from schemas.get_note_schema import GET_NOTE_INPUT_SCHEMA, GET_NOTE_OUTPUT_SCHEMA
from schemas.list_notes_schema import LIST_NOTES_INPUT_SCHEMA, LIST_NOTES_OUTPUT_SCHEMA
from schemas.search_notes_schema import SEARCH_NOTES_INPUT_SCHEMA, SEARCH_NOTES_OUTPUT_SCHEMA
from schemas.update_note_schema import UPDATE_NOTE_INPUT_SCHEMA, UPDATE_NOTE_OUTPUT_SCHEMA


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
    {
        "name": "get_note",
        "description": "Fetch a single note by id.",
        "inputSchema": GET_NOTE_INPUT_SCHEMA,
        "outputSchema": GET_NOTE_OUTPUT_SCHEMA,
    },
    {
        "name": "update_note",
        "description": "Update title and content for an existing note by id.",
        "inputSchema": UPDATE_NOTE_INPUT_SCHEMA,
        "outputSchema": UPDATE_NOTE_OUTPUT_SCHEMA,
    },
    {
        "name": "delete_note",
        "description": "Delete an existing note by id.",
        "inputSchema": DELETE_NOTE_INPUT_SCHEMA,
        "outputSchema": DELETE_NOTE_OUTPUT_SCHEMA,
    },
]
