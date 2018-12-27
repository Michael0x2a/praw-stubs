# Stubs for praw.models.inbox (Python 3.7)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from ..const import API_PATH
from .base import PRAWBase
from .listing.generator import ListingGenerator
from .util import stream_generator
from typing import Any

class Inbox(PRAWBase):
    def all(self, **generator_kwargs: Any): ...
    def collapse(self, items: Any) -> None: ...
    def comment_replies(self, **generator_kwargs: Any): ...
    def mark_read(self, items: Any) -> None: ...
    def mark_unread(self, items: Any) -> None: ...
    def mentions(self, **generator_kwargs: Any): ...
    def message(self, message_id: Any): ...
    def messages(self, **generator_kwargs: Any): ...
    def sent(self, **generator_kwargs: Any): ...
    def stream(self, **stream_options: Any): ...
    def submission_replies(self, **generator_kwargs: Any): ...
    def uncollapse(self, items: Any) -> None: ...
    def unread(self, mark_read: bool = ..., **generator_kwargs: Any): ...