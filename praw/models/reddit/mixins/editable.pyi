from ....const import API_PATH
from typing import TypeVar

_T = TypeVar("_T", bound=EditableMixin)

class EditableMixin:
    def delete(self) -> None: ...
    def edit(self: _T, body: str) -> _T: ...
