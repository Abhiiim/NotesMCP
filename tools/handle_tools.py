import json
from typing import Any, Optional
from data.validations.type_name import type_name
from error.mcp_error import MCPError
from tools.tool_definitions import TOOL_DEFINITIONS
from tools.tool_handlers import TOOL_HANDLERS


def handle_initialize(params: Optional[dict[str, Any]]) -> dict[str, Any]:
    if params is None:
        params = {}
    if not isinstance(params, dict):
        raise MCPError(
            -32602,
            "Invalid params",
            {"path": "$", "expected": "object", "actual": type_name(params)},
        )

    client_protocol = params.get("protocolVersion")
    protocol_version = client_protocol if isinstance(client_protocol, str) else "2025-03-26"
    return {
        "protocolVersion": protocol_version,
        "capabilities": {"tools": {}},
        "serverInfo": {"name": "notes-mcp", "version": "1.0.0"},
    }


def handle_tools_list(params: Optional[dict[str, Any]]) -> dict[str, Any]:
    if params is None:
        params = {}
    if not isinstance(params, dict):
        raise MCPError(
            -32602,
            "Invalid params",
            {"path": "$", "expected": "object", "actual": type_name(params)},
        )
    return {"tools": TOOL_DEFINITIONS}
    

def handle_tools_call(params: Optional[dict[str, Any]]) -> dict[str, Any]:
    if not isinstance(params, dict):
        raise MCPError(
            -32602,
            "Invalid params",
            {"path": "$", "expected": "object", "actual": type_name(params)},
        )

    name = params.get("name")
    if not isinstance(name, str) or not name:
        raise MCPError(
            -32602,
            "Invalid params",
            {"path": "$.name", "expected": "non-empty string", "actual": type_name(name)},
        )

    arguments = params.get("arguments", {})
    if arguments is None:
        arguments = {}
    if not isinstance(arguments, dict):
        raise MCPError(
            -32602,
            "Invalid params",
            {"path": "$.arguments", "expected": "object", "actual": type_name(arguments)},
        )

    handler = TOOL_HANDLERS.get(name)
    if handler is None:
        raise MCPError(-32602, "Unknown tool", {"tool": name})

    output = handler(arguments)
    return {
        "content": [{"type": "text", "text": json.dumps(output, ensure_ascii=False)}],
        "structuredContent": output,
    }


def handle_notification(message: dict[str, Any]) -> bool:
    method = message.get("method")
    if method == "notifications/initialized":
        return True
    if method == "exit":
        return False
    return True
