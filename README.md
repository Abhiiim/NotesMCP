# Notes MCP

Tool-only MCP server that provides persistent notes storage via SQLite.

## What it exposes

- `add_note`
- `list_notes`
- `get_note`
- `update_note`
- `delete_note`
- `search_notes`

No resources and no prompts are exposed.

## Run

```bash
python3.11 /Users/akeshibh/Desktop/NotesMCP/server.py
```

The server stores data at:

`/Users/akeshibh/Desktop/NotesMCP/data/notes.db`

## Tool schemas

`add_note` input:

```json
{
  "type": "object",
  "additionalProperties": false,
  "required": ["title", "content"],
  "properties": {
    "title": { "type": "string", "minLength": 1 },
    "content": { "type": "string" }
  }
}
```

`add_note` output:

```json
{
  "type": "object",
  "additionalProperties": false,
  "required": ["id", "created_at"],
  "properties": {
    "id": { "type": "string", "minLength": 1 },
    "created_at": { "type": "string", "format": "date-time" }
  }
}
```

`list_notes` input:

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {}
}
```

`list_notes` output:

```json
{
  "type": "object",
  "additionalProperties": false,
  "required": ["notes"],
  "properties": {
    "notes": {
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": ["id", "title", "created_at"],
        "properties": {
          "id": { "type": "string", "minLength": 1 },
          "title": { "type": "string", "minLength": 1 },
          "created_at": { "type": "string", "format": "date-time" }
        }
      }
    }
  }
}
```

`search_notes` input:

```json
{
  "type": "object",
  "additionalProperties": false,
  "required": ["query"],
  "properties": {
    "query": { "type": "string", "minLength": 1 }
  }
}
```

`search_notes` output:

```json
{
  "type": "object",
  "additionalProperties": false,
  "required": ["results"],
  "properties": {
    "results": {
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": ["id", "title", "snippet"],
        "properties": {
          "id": { "type": "string", "minLength": 1 },
          "title": { "type": "string", "minLength": 1 },
          "snippet": { "type": "string" }
        }
      }
    }
  }
}
```

`get_note` input:

```json
{
  "type": "object",
  "additionalProperties": false,
  "required": ["id"],
  "properties": {
    "id": { "type": "string", "minLength": 1 }
  }
}
```

`get_note` output:

```json
{
  "type": "object",
  "additionalProperties": false,
  "required": ["id", "title", "content", "created_at"],
  "properties": {
    "id": { "type": "string", "minLength": 1 },
    "title": { "type": "string", "minLength": 1 },
    "content": { "type": "string" },
    "created_at": { "type": "string", "format": "date-time" }
  }
}
```

`update_note` input:

```json
{
  "type": "object",
  "additionalProperties": false,
  "required": ["id", "title", "content"],
  "properties": {
    "id": { "type": "string", "minLength": 1 },
    "title": { "type": "string", "minLength": 1 },
    "content": { "type": "string" }
  }
}
```

`update_note` output:

```json
{
  "type": "object",
  "additionalProperties": false,
  "required": ["id", "title", "content", "created_at"],
  "properties": {
    "id": { "type": "string", "minLength": 1 },
    "title": { "type": "string", "minLength": 1 },
    "content": { "type": "string" },
    "created_at": { "type": "string", "format": "date-time" }
  }
}
```

`delete_note` input:

```json
{
  "type": "object",
  "additionalProperties": false,
  "required": ["id"],
  "properties": {
    "id": { "type": "string", "minLength": 1 }
  }
}
```

`delete_note` output:

```json
{
  "type": "object",
  "additionalProperties": false,
  "required": ["id"],
  "properties": {
    "id": { "type": "string", "minLength": 1 }
  }
}
```

## Behavior and constraints

- The server is stateless between requests except for SQLite persistence.
- Search is deterministic and sorted by `created_at`, then `id`.
- File storage is sandboxed to this project directory.
- Validation failures and protocol failures are returned as structured JSON-RPC/MCP errors.
