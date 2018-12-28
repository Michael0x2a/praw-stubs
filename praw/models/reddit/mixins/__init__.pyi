from ....const import API_PATH
from .editable import EditableMixin as EditableMixin
from .gildable import GildableMixin as GildableMixin
from .inboxable import InboxableMixin as InboxableMixin
from .inboxtoggleable import InboxToggleableMixin as InboxToggleableMixin
from .messageable import MessageableMixin as MessageableMixin
from .replyable import ReplyableMixin as ReplyableMixin
from .reportable import ReportableMixin as ReportableMixin
from .savable import SavableMixin as SavableMixin
from .votable import VotableMixin as VotableMixin

class ThingModerationMixin:
    def approve(self) -> None: ...
    def distinguish(self, how: str = ..., sticky: bool = ...) -> None: ...
    def ignore_reports(self) -> None: ...
    def remove(self, spam: bool = ...) -> None: ...
    def undistinguish(self) -> None: ...
    def unignore_reports(self) -> None: ...

class UserContentMixin(
    EditableMixin,
    GildableMixin,
    InboxToggleableMixin,
    ReplyableMixin,
    ReportableMixin,
    SavableMixin,
    VotableMixin,
): ...
