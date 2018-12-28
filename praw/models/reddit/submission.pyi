# Stubs for praw.models.reddit.submission (Python 3.7)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.
#
# NOTE: Added partial stubs

from ...const import API_PATH, urljoin
from ...exceptions import ClientException
from ...reddit import Reddit
from ..comment_forest import CommentForest
from ..listing.mixins import SubmissionListingMixin
from .base import RedditBase
from .mixins import ThingModerationMixin, UserContentMixin
from .redditor import Redditor
from .subreddit import Subreddit
from typing import Any, Optional, List, Union, Tuple

class Submission(RedditBase, SubmissionListingMixin, UserContentMixin):
    STR_FIELD: str = ...
    @staticmethod
    def id_from_url(url: str) -> str: ...
    @property
    def comments(self) -> CommentForest: ...
    @property
    def flair(self) -> SubmissionFlair: ...
    @property
    def mod(self) -> SubmissionModeration: ...
    @property
    def shortlink(self) -> str: ...
    comment_limit: int = ...
    comment_sort: str = ...
    id: str = ...

    # Dynamically generated attributes
    author: Redditor = ...
    clicked: bool = ...
    created_utc: int = ...
    distinguished: bool = ...
    edited: bool = ...
    is_video: bool = ...
    link_flair_css_class: str = ...
    link_flair_text: str = ...
    locked: bool = ...
    num_comments: int = ...
    over_18: bool = ...
    permalink: str = ...
    score: int = ...
    selftext: str = ...
    stickied: bool = ...
    subreddit: Subreddit = ...
    subreddit_id: str = ...
    title: str = ...
    upvote_ratio: int = ...

    # Discovered attributes not mentioned directly in comments
    url: str = ...
    # Note: both mod_reports and user_reports actually are list-of-lists.
    # However, the inner list is more semantically closer to a tuple -- so we use that
    # so we can get more precise types.
    mod_reports: List[Tuple[str, str]] = ...
    user_reports: List[Tuple[str, int]] = ...
    def __init__(
        self,
        reddit: Reddit,
        id: Optional[str] = ...,
        url: Optional[str] = ...,
        _data: Optional[object] = ...,
    ) -> None: ...
    def mark_visited(self) -> None: ...
    def hide(self, other_submissions: Optional[List[Submission]] = ...) -> None: ...
    def unhide(self, other_submissions: Optional[List[Submission]] = ...) -> None: ...
    def crosspost(
        self,
        subreddit: Union[str, Subreddit],
        title: Optional[str] = ...,
        send_replies: bool = ...,
    ) -> Submission: ...

class SubmissionFlair:
    submission: Any = ...
    def __init__(self, submission: Any) -> None: ...
    def choices(self): ...
    def select(self, flair_template_id: Any, text: Optional[Any] = ...) -> None: ...

class SubmissionModeration(ThingModerationMixin):
    thing: Any = ...
    def __init__(self, submission: Any) -> None: ...
    def contest_mode(self, state: bool = ...) -> None: ...
    def flair(self, text: str = ..., css_class: str = ...) -> None: ...
    def lock(self) -> None: ...
    def nsfw(self) -> None: ...
    def sfw(self) -> None: ...
    def spoiler(self) -> None: ...
    def sticky(self, state: bool = ..., bottom: bool = ...): ...
    def suggested_sort(self, sort: str = ...) -> None: ...
    def unlock(self) -> None: ...
    def unspoiler(self) -> None: ...
