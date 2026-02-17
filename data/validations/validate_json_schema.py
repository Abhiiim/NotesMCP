from typing import Any
from datetime import datetime
from data.validations.type_name import type_name
from error.mcp_error import MCPError


def validate_json_schema(instance: Any, schema: dict[str, Any], path: str = "$") -> None:
    expected_type = schema.get("type")
    if expected_type == "object":
        if not isinstance(instance, dict):
            raise MCPError(
                -32602,
                "Invalid params",
                {"path": path, "expected": "object", "actual": type_name(instance)},
            )

        required = schema.get("required", [])
        missing = [field for field in required if field not in instance]
        if missing:
            raise MCPError(
                -32602,
                "Invalid params",
                {"path": path, "missing": missing},
            )

        properties = schema.get("properties", {})
        additional_properties = schema.get("additionalProperties", True)

        if additional_properties is False:
            extras = sorted(key for key in instance if key not in properties)
            if extras:
                raise MCPError(
                    -32602,
                    "Invalid params",
                    {"path": path, "unexpected": extras},
                )

        for key, value in instance.items():
            if key in properties:
                validate_json_schema(value, properties[key], f"{path}.{key}")

    elif expected_type == "array":
        if not isinstance(instance, list):
            raise MCPError(
                -32602,
                "Invalid params",
                {"path": path, "expected": "array", "actual": type_name(instance)},
            )
        item_schema = schema.get("items")
        if item_schema is not None:
            for idx, item in enumerate(instance):
                validate_json_schema(item, item_schema, f"{path}[{idx}]")

    elif expected_type == "string":
        if not isinstance(instance, str):
            raise MCPError(
                -32602,
                "Invalid params",
                {"path": path, "expected": "string", "actual": type_name(instance)},
            )

        min_length = schema.get("minLength")
        if min_length is not None and len(instance) < min_length:
            raise MCPError(
                -32602,
                "Invalid params",
                {"path": path, "minLength": min_length, "actualLength": len(instance)},
            )

        if schema.get("format") == "date-time":
            try:
                datetime.fromisoformat(instance.replace("Z", "+00:00"))
            except ValueError as exc:
                raise MCPError(
                    -32602,
                    "Invalid params",
                    {"path": path, "format": "date-time", "value": instance},
                ) from exc

    else:
        raise MCPError(
            -32603,
            "Server configuration error",
            {"path": path, "unsupportedSchemaType": expected_type},
        )
