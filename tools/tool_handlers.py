from typing import Any, Callable

from notes_service.add_note import add_note
from notes_service.delete_note import delete_note
from notes_service.get_note import get_note
from notes_service.list_notes import list_notes
from notes_service.search_notes import search_notes
from notes_service.update_note import update_note


TOOL_HANDLERS: dict[str, Callable[[dict[str, Any]], dict[str, Any]]] = {
    "add_note": add_note,
    "list_notes": list_notes,
    "search_notes": search_notes,
    "get_note": get_note,
    "update_note": update_note,
    "delete_note": delete_note,
}
