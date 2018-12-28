# Stubs for praw.models.reddit.live (Python 3.7)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from ...const import API_PATH
from ..list.redditor import RedditorList
from ..listing.generator import ListingGenerator
from .base import RedditBase
from .redditor import Redditor
from typing import Any, Optional

class LiveContributorRelationship:
    def __call__(self): ...
    thread: Any = ...
    def __init__(self, thread: Any) -> None: ...
    def accept_invite(self) -> None: ...
    def invite(self, redditor: Any, permissions: Optional[Any] = ...) -> None: ...
    def leave(self) -> None: ...
    def remove(self, redditor: Any) -> None: ...
    def remove_invite(self, redditor: Any) -> None: ...
    def update(self, redditor: Any, permissions: Optional[Any] = ...) -> None: ...
    def update_invite(
        self, redditor: Any, permissions: Optional[Any] = ...
    ) -> None: ...

class LiveThread(RedditBase):
    STR_FIELD: str = ...
    @property
    def contrib(self): ...
    @property
    def contributor(self): ...
    def __eq__(self, other: Any): ...
    def __getitem__(self, update_id: Any): ...
    def __hash__(self): ...
    id: Any = ...
    def __init__(
        self, reddit: Any, id: Optional[Any] = ..., _data: Optional[Any] = ...
    ) -> None: ...
    def discussions(self, **generator_kwargs: Any): ...
    def report(self, type: Any) -> None: ...
    def updates(self, **generator_kwargs: Any) -> None: ...

class LiveThreadContribution:
    thread: Any = ...
    def __init__(self, thread: Any) -> None: ...
    def add(self, body: Any) -> None: ...
    def close(self) -> None: ...
    def update(
        self,
        title: Optional[Any] = ...,
        description: Optional[Any] = ...,
        nsfw: Optional[Any] = ...,
        resources: Optional[Any] = ...,
        **other_settings: Any,
    ): ...

class LiveUpdate(RedditBase):
    STR_FIELD: str = ...
    @property
    def contrib(self): ...
    @property
    def thread(self): ...
    id: Any = ...
    def __init__(
        self,
        reddit: Any,
        thread_id: Optional[Any] = ...,
        update_id: Optional[Any] = ...,
        _data: Optional[Any] = ...,
    ) -> None: ...
    def __setattr__(self, attribute: Any, value: Any) -> None: ...

class LiveUpdateContribution:
    update: Any = ...
    def __init__(self, update: Any) -> None: ...
    def remove(self) -> None: ...
    def strike(self) -> None: ...
