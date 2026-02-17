from typing import Any
from data.validations.validate_json_schema import validate_json_schema
from database.db import db_connection
from schemas.search_notes_schema import SEARCH_NOTES_INPUT_SCHEMA, SEARCH_NOTES_OUTPUT_SCHEMA


def search_notes(arguments: dict[str, Any]) -> dict[str, Any]:
    validate_json_schema(arguments, SEARCH_NOTES_INPUT_SCHEMA)
    query = arguments["query"]

    with db_connection() as conn:
        rows = conn.execute(
            """
            SELECT id, title, content
            FROM notes
            WHERE instr(lower(title), lower(?)) > 0
               OR instr(lower(content), lower(?)) > 0
            ORDER BY created_at ASC, id ASC
            """,
            (query, query),
        ).fetchall()

    result = {
        "results": [
            {
                "id": row["id"],
                "title": row["title"],
                "snippet": make_snippet(row["title"], row["content"], query),
            }
            for row in rows
        ]
    }
    validate_json_schema(result, SEARCH_NOTES_OUTPUT_SCHEMA)
    return result


def make_snippet(title: str, content: str, query: str) -> str:
    combined = f"{title}\n{content}".strip()
    if not combined:
        return ""

    query_lower = query.lower()
    idx = combined.lower().find(query_lower)
    if idx < 0:
        idx = 0
    start = max(0, idx - 40)
    end = min(len(combined), idx + len(query) + 80)
    snippet = combined[start:end].replace("\n", " ").strip()
    if start > 0:
        snippet = f"...{snippet}"
    if end < len(combined):
        snippet = f"{snippet}..."
    return snippet
