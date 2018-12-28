from ....const import API_PATH
from ..subreddit import Subreddit
from typing import Union

class MessageableMixin:
    def message(self,
                subject: str,
                message: str,
                from_subreddit: Union[None, str, Subreddit] = ...,
                ) -> None: ...
