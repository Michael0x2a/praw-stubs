from ..const import API_PATH
from .base import PRAWBase
from .reddit.live import LiveThread
from .reddit.multi import Multireddit, Subreddit
from typing import Any, Optional, List, Iterator, Iterable 

class LiveHelper(PRAWBase):
    def __call__(self, id: str) -> LiveThread: ...
    def info(self, ids: List[str]) -> Iterator[LiveThread]: ...
    def create(self, title: str,
                     description: Optional[str] = ...,
                     nsfw: bool = ...,
                     resources: Optional[str] = ...,
                     ) -> LiveThread: ...
    def now(self) -> Optional[LiveThread]: ...

class MultiredditHelper(PRAWBase):
    def __call__(self, redditor: str, name: str) -> Multireddit: ...
    def create(self, display_name: str,
                     subreddits: Iterable[Subreddit],
                     description_md: Optional[str] = ...,
                     icon_name: Optional[str] = ...,
                     key_color: Optional[str] = ...,
                     visibility: str = ...,
                     weighting_scheme: str = ...,
                     ) -> Multireddit: ...

class SubredditHelper(PRAWBase):
    def __call__(self, display_name: str) -> Subreddit: ...
    def create(self, name: str,
                     title: Optional[str] = ...,
                     link_type: str = ...,
                     subreddit_type: str = ...,
                     wikimode: str = ...,
                     **other_settings: Any,
                     ) -> Subreddit: ...
