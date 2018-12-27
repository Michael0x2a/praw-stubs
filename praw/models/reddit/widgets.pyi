# Stubs for praw.models.reddit.widgets (Python 3.7)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from ...const import API_PATH
from ..base import PRAWBase
from ..list.base import BaseList
from typing import Any

class Button(PRAWBase): ...
class Image(PRAWBase): ...
class ImageData(PRAWBase): ...
class MenuLink(PRAWBase): ...

class Submenu(BaseList):
    CHILD_ATTRIBUTE: str = ...

class SubredditWidgets(PRAWBase):
    @property
    def id_card(self): ...
    @property
    def items(self): ...
    @property
    def moderators_widget(self): ...
    @property
    def sidebar(self): ...
    @property
    def topbar(self): ...
    def refresh(self) -> None: ...
    def __getattr__(self, attr: Any): ...
    subreddit: Any = ...
    progressive_images: bool = ...
    def __init__(self, subreddit: Any) -> None: ...

class Widget(PRAWBase):
    def __eq__(self, other: Any): ...

class ButtonWidget(Widget, BaseList):
    CHILD_ATTRIBUTE: str = ...

class Calendar(Widget): ...

class CommunityList(Widget, BaseList):
    CHILD_ATTRIBUTE: str = ...

class CustomWidget(Widget):
    def __init__(self, reddit: Any, _data: Any) -> None: ...

class IDCard(Widget): ...

class ImageWidget(Widget, BaseList):
    CHILD_ATTRIBUTE: str = ...

class Menu(Widget, BaseList):
    CHILD_ATTRIBUTE: str = ...

class ModeratorsWidget(Widget, BaseList):
    CHILD_ATTRIBUTE: str = ...

class RulesWidget(Widget, BaseList):
    CHILD_ATTRIBUTE: str = ...

class TextArea(Widget): ...