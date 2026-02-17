#!/usr/bin/env python3
"""Notes MCP server.

Implements a tool-only MCP server with SQLite-backed persistence.
"""

from __future__ import annotations

import json
import sys
from typing import Any

from error.mcp_error import MCPError
from data.validations.type_name import type_name
from database.db import ensure_database
from tools.handle_tools import handle_initialize, handle_notification, handle_tools_list, handle_tools_call


JSONRPC_VERSION = "2.0"


def dispatch(method: str, params: dict[str, Any] | None) -> dict[str, Any]:
    if method == "initialize":
        return handle_initialize(params)
    if method == "tools/list":
        return handle_tools_list(params)
    if method == "tools/call":
        return handle_tools_call(params)
    if method == "ping":
        return {}
    if method == "shutdown":
        return {}
    if method in {"resources/list", "prompts/list"}:
        raise MCPError(-32601, "Method not found", {"method": method})
    raise MCPError(-32601, "Method not found", {"method": method})


def write_json(payload: dict[str, Any]) -> None:
    sys.stdout.write(json.dumps(payload) + "\n")
    sys.stdout.flush()


def main() -> None:
    ensure_database()

    running = True
    while running:
        line = sys.stdin.readline()
        if line == "":
            break

        line = line.strip()
        if not line:
            continue

        try:
            message = json.loads(line)
        except json.JSONDecodeError as exc:
            write_json(
                {
                    "jsonrpc": JSONRPC_VERSION,
                    "id": None,
                    "error": MCPError(-32700, "Parse error", {"details": str(exc)}).to_error_object(),
                }
            )
            continue

        if not isinstance(message, dict):
            write_json(
                {
                    "jsonrpc": JSONRPC_VERSION,
                    "id": None,
                    "error": MCPError(-32600, "Invalid Request").to_error_object(),
                }
            )
            continue

        is_notification = "id" not in message
        if is_notification:
            running = handle_notification(message)
            continue

        request_id = message.get("id")

        try:
            if message.get("jsonrpc") != JSONRPC_VERSION:
                raise MCPError(-32600, "Invalid Request", {"reason": "jsonrpc must be 2.0"})

            method = message.get("method")
            if not isinstance(method, str):
                raise MCPError(
                    -32600,
                    "Invalid Request",
                    {"path": "$.method", "expected": "string", "actual": type_name(method)},
                )

            params = message.get("params")
            result = dispatch(method, params)
            write_json({"jsonrpc": JSONRPC_VERSION, "id": request_id, "result": result})
        except MCPError as exc:
            write_json({"jsonrpc": JSONRPC_VERSION, "id": request_id, "error": exc.to_error_object()})
        except Exception as exc:  # pragma: no cover
            write_json(
                {
                    "jsonrpc": JSONRPC_VERSION,
                    "id": request_id,
                    "error": MCPError(-32603, "Internal error", {"details": str(exc)}).to_error_object(),
                }
            )


if __name__ == "__main__":
    main()
