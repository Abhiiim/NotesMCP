from dataclasses import dataclass
from typing import Any


@dataclass
class MCPError(Exception):
    code: int
    message: str
    data: dict[str, Any] | None = None

    def to_error_object(self) -> dict[str, Any]:
        error: dict[str, Any] = {"code": self.code, "message": self.message}
        if self.data is not None:
            error["data"] = self.data
        return error