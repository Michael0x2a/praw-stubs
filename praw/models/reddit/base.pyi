from ...const import API_PATH, urlparse
from ...exceptions import ClientException, PRAWException
from ...reddit import Reddit
from ..base import PRAWBase
from typing import Any

class RedditBase(PRAWBase):
    def __init__(self, reddit: Reddit, _data: object) -> None: ...

    @property
    def fullname(self) -> str: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __getattr__(self, attribute: object) -> Any: ...
    def __hash__(self) -> int: ...
