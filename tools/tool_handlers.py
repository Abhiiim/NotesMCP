from typing import Any, Callable

from notes_service.add_note import add_note
from notes_service.list_notes import list_notes
from notes_service.search_notes import search_notes


TOOL_HANDLERS: dict[str, Callable[[dict[str, Any]], dict[str, Any]]] = {
    "add_note": add_note,
    "list_notes": list_notes,
    "search_notes": search_notes,
}
