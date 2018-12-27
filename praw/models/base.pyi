from typing import TypeVar, Type, Dict, Optional
from ..reddit import Reddit

_T = TypeVar('_T')

class PRAWBase:
    @classmethod
    def parse(cls: Type[_T], data: Dict[str, object], reddit: Reddit) -> _T: ...
    def __init__(self, reddit: Reddit, _data: Optional[Dict[str, object]]) -> None: ...
