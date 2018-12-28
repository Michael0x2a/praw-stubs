from typing import List, Optional, Generic, TypeVar, Set, Any

_T = TypeVar("_T")

class BoundedSet(Generic[_T]):
    max_items: int = ...
    def __init__(self, max_items: int) -> None: ...
    def __contains__(self, item: object) -> bool: ...
    def add(self, item: _T) -> None: ...

class ExponentialCounter:
    def __init__(self, max_counter: float) -> None: ...
    def counter(self) -> float: ...
    def reset(self) -> None: ...

def permissions_string(
    permissions: Optional[List[str]], known_permissions: Set[str]
) -> str: ...
def stream_generator(
    function: Any,
    pause_after: Optional[int] = ...,
    skip_existing: bool = ...,
    attribute_name: str = ...,
) -> None: ...
