from ...const import API_PATH, urljoin
from ...exceptions import APIException
from ...reddit import Reddit
from ..listing.generator import ListingGenerator
from ..listing.mixins import SubredditListingMixin
from ..util import permissions_string, stream_generator
from .base import RedditBase
from .comment import Comment
from .emoji import SubredditEmoji
from .mixins import MessageableMixin
from .modmail import ModmailConversation
from .widgets import SubredditWidgets
from .wikipage import WikiPage
from .redditor import Redditor
from .submission import Submission
from typing import Any, Optional, Iterator, Dict, Union, Set, List, Iterable, overload

class Subreddit(RedditBase, MessageableMixin, SubredditListingMixin):
    STR_FIELD: str = ...
    MESSAGE_PREFIX: str = ...
    @property
    def banned(self) -> SubredditRelationship: ...
    @property
    def contributor(self) -> ContributorRelationship: ...
    @property
    def emoji(self) -> SubredditEmoji: ...
    @property
    def filters(self) -> SubredditFilters: ...
    @property
    def flair(self) -> SubredditFlair: ...
    @property
    def mod(self) -> SubredditModeration: ...
    @property
    def moderator(self) -> ModeratorRelationship: ...
    @property
    def modmail(self) -> Modmail: ...
    @property
    def muted(self) -> SubredditRelationship: ...
    @property
    def quaran(self) -> SubredditQuarantine: ...
    @property
    def stream(self) -> SubredditStream: ...
    @property
    def stylesheet(self) -> SubredditStylesheet: ...
    @property
    def widgets(self) -> SubredditWidgets: ...
    @property
    def wiki(self) -> SubredditWiki: ...

    display_name: Any = ...

    def __init__(self, reddit: Reddit,
                       display_name: Optional[str] = ...,
                       _data: Optional[Dict[str, object]] = ...,
                       ) -> None: ...
    def random(self) -> Submission: ...
    def rules(self): ...
    def search(self, query: Any, sort: str = ..., syntax: str = ..., time_filter: str = ..., **generator_kwargs: Any): ...
    def sticky(self, number: int = ...) -> Submission: ...
    def submit(self, title: Any, selftext: Optional[Any] = ..., url: Optional[Any] = ..., flair_id: Optional[Any] = ..., flair_text: Optional[Any] = ..., resubmit: bool = ..., send_replies: bool = ...): ...
    def subscribe(self, other_subreddits: Optional[Any] = ...) -> None: ...
    def traffic(self): ...
    def unsubscribe(self, other_subreddits: Optional[Any] = ...) -> None: ...

class SubredditFilters:
    subreddit: Any = ...
    def __init__(self, subreddit: Any) -> None: ...
    def __iter__(self) -> None: ...
    def add(self, subreddit: Any) -> None: ...
    def remove(self, subreddit: Any) -> None: ...

class SubredditFlair:
    @property
    def link_templates(self): ...
    @property
    def templates(self): ...
    def __call__(self, redditor: Optional[Any] = ..., **generator_kwargs: Any): ...
    subreddit: Any = ...
    def __init__(self, subreddit: Any) -> None: ...
    def configure(self, position: str = ..., self_assign: bool = ..., link_position: str = ..., link_self_assign: bool = ..., **settings: Any) -> None: ...
    def delete(self, redditor: Any) -> None: ...
    def delete_all(self): ...
    def set(self, redditor: Optional[Any] = ..., text: str = ..., css_class: str = ...) -> None: ...
    def update(self, flair_list: Any, text: str = ..., css_class: str = ...): ...

class SubredditFlairTemplates:
    @staticmethod
    def flair_type(is_link: Any): ...
    subreddit: Any = ...
    def __init__(self, subreddit: Any) -> None: ...
    def delete(self, template_id: Any) -> None: ...
    def update(self, template_id: Any, text: Any, css_class: str = ..., text_editable: bool = ...) -> None: ...

class SubredditRedditorFlairTemplates(SubredditFlairTemplates):
    def __iter__(self) -> None: ...
    def add(self, text: Any, css_class: str = ..., text_editable: bool = ...) -> None: ...
    def clear(self) -> None: ...

class SubredditLinkFlairTemplates(SubredditFlairTemplates):
    def __iter__(self) -> None: ...
    def add(self, text: Any, css_class: str = ..., text_editable: bool = ...) -> None: ...
    def clear(self) -> None: ...

class SubredditModeration:
    subreddit: Subreddit = ...
    def __init__(self, subreddit: Subreddit) -> None: ...
    def accept_invite(self) -> None: ...

    # TODO: once literal types have landed, add overloads for "comments" and "submissions"
    def edited(self, only: Optional[str] = ...,
                     limit: int = ...,
                     params: Dict[str, str] = ...,
                     ) -> ListingGenerator[Union[Comment, Submission]]: ...
    def inbox(self, **generator_kwargs: Any): ...
    def log(self, action: Optional[Any] = ..., mod: Optional[Any] = ..., **generator_kwargs: Any): ...
    def modqueue(self, only: Optional[Any] = ..., **generator_kwargs: Any): ...
    # TODO: Same TODO about literal types
    def reports(self, only: None = ...,
                     limit: int = ...,
                     params: Dict[str, str] = ...,
                     ) -> ListingGenerator[Union[Comment, Submission]]: ...
    def settings(self): ...
    def spam(self, only: Optional[Any] = ..., **generator_kwargs: Any): ...
    def unmoderated(self, **generator_kwargs: Any): ...
    def unread(self, **generator_kwargs: Any): ...
    def update(self, **settings: Any): ...

class SubredditQuarantine:
    subreddit: Any = ...
    def __init__(self, subreddit: Any) -> None: ...
    def opt_in(self) -> None: ...
    def opt_out(self) -> None: ...

class SubredditRelationship:
    subreddit: Subreddit = ...
    relationship: str = ...

    def __call__(self, redditor: Optional[Redditor] = ..., 
                       limit: int = ...,
                       params: Dict[str, str] = ...) -> Iterable[Redditor]: ...
    def __init__(self, subreddit: Subreddit, relationship: str) -> None: ...
    def add(self, redditor: Union[str, Redditor], **other_settings: Any) -> None: ...
    def remove(self, redditor: Union[str, Redditor]) -> None: ...

class ContributorRelationship(SubredditRelationship):
    def leave(self) -> None: ...

class ModeratorRelationship(SubredditRelationship):
    PERMISSIONS: Set[str] = ...
    def __call__(self, redditor: Optional[Redditor] = ...,
                       limit: int = ...,
                       params: Dict[str, str] = ...,
                       ) -> List[Redditor]: ...
    def add(self, redditor: Union[str, Redditor],
                  permissions: Optional[List[str]] = ...,
                  **other_settings: Any,
                  ) -> None: ...
    def invite(self, redditor: Union[str, Redditor],
                     permissions: Optional[List[str]] = ...,
                     **other_settings: Any,
                     ) -> None: ...
    def leave(self) -> None: ...
    def remove_invite(self, redditor: Union[str, Redditor]) -> None: ...
    def update(self, redditor: Union[str, Redditor],
                     permissions: Optional[List[str]] = ...,
                     ) -> None: ...
    def update_invite(self, redditor: Union[str, Redditor],
                            permissions: Optional[List[str]] = ...,
                            ) -> None: ...

class Modmail:
    def __call__(self, id: Optional[Any] = ..., mark_read: bool = ...): ...
    subreddit: Any = ...
    def __init__(self, subreddit: Any) -> None: ...
    def bulk_read(self, other_subreddits: Optional[Any] = ..., state: Optional[Any] = ...): ...
    def conversations(self, after: Optional[Any] = ..., limit: Optional[Any] = ..., other_subreddits: Optional[Any] = ..., sort: Optional[Any] = ..., state: Optional[Any] = ...) -> None: ...
    def create(self, subject: Any, body: Any, recipient: Any, author_hidden: bool = ...): ...
    def subreddits(self) -> None: ...
    def unread_count(self): ...

class SubredditStream:
    subreddit: Any = ...
    def __init__(self, subreddit: Any) -> None: ...
    def comments(self, **stream_options: Any): ...
    def submissions(self, **stream_options: Any): ...

class SubredditStylesheet:
    JPEG_HEADER: bytes = ...
    def __call__(self): ...
    subreddit: Any = ...
    def __init__(self, subreddit: Any) -> None: ...
    def delete_header(self) -> None: ...
    def delete_image(self, name: Any) -> None: ...
    def delete_mobile_header(self) -> None: ...
    def delete_mobile_icon(self) -> None: ...
    def update(self, stylesheet: Any, reason: Optional[Any] = ...) -> None: ...
    def upload(self, name: Any, image_path: Any): ...
    def upload_header(self, image_path: Any): ...
    def upload_mobile_header(self, image_path: Any): ...
    def upload_mobile_icon(self, image_path: Any): ...

class SubredditWiki:
    banned: SubredditRelationship = ...
    contributor: SubredditRelationship = ...
    subreddit: Subreddit = ...

    def __getitem__(self, page_name: str) -> WikiPage: ...
    def __init__(self, subreddit: Subreddit) -> None: ...
    def __iter__(self) -> Iterator[WikiPage]: ...
    def create(self, name: Any, content: Any, reason: Optional[Any] = ..., **other_settings: Any): ...
    def revisions(self, **generator_kwargs: Any): ...
