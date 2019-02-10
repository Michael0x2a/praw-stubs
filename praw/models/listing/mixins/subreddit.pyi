from typing import Optional, Dict

from ....reddit import Reddit
from ...base import PRAWBase
from ..generator import ListingGenerator
from ...reddit.subreddit import Subreddit
from ...reddit.comment import Comment
from .base import BaseListingMixin
from .gilded import GildedListingMixin
from .rising import RisingListingMixin

class SubredditListingMixin(BaseListingMixin, GildedListingMixin, RisingListingMixin):
    @property
    def comments(self) -> CommentHelper: ...
    def __init__(self, Reddit: Reddit, _data: Optional[Dict[str, object]]) -> None: ...

class CommentHelper(PRAWBase):
    subreddit: Subreddit = ...
    def __init__(self, subreddit: Subreddit) -> None: ...
    def __call__(
        self, only: Optional[str] = ..., limit: int = ..., params: Dict[str, str] = ...
    ) -> ListingGenerator[Comment]: ...
    # Note: this class has a 'gilded()' method, but it's deprecated.
