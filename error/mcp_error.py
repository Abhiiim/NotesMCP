from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class MCPError(Exception):
    code: int
    message: str
    data: Optional[dict[str, Any]] = None

    def to_error_object(self) -> dict[str, Any]:
        error: dict[str, Any] = {"code": self.code, "message": self.message}
        if self.data is not None:
            error["data"] = self.data
        return error
