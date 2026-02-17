from pathlib import Path
import sqlite3

from error.mcp_error import MCPError

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
DB_PATH = DATA_DIR / "notes.db"


def sandboxed_path(path: Path) -> Path:
    resolved = path.resolve()
    if resolved == PROJECT_ROOT or PROJECT_ROOT in resolved.parents:
        return resolved
    raise MCPError(
        -32000,
        "Path outside project sandbox",
        {"path": str(path), "resolved": str(resolved)},
    )


def ensure_database() -> None:
    sandboxed_path(DATA_DIR).mkdir(parents=True, exist_ok=True)
    db_path = sandboxed_path(DB_PATH)
    with sqlite3.connect(db_path) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS notes (
                id TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
            """
        )
        conn.commit()


def db_connection() -> sqlite3.Connection:
    ensure_database()
    conn = sqlite3.connect(sandboxed_path(DB_PATH))
    conn.row_factory = sqlite3.Row
    return conn
