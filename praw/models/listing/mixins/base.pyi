from ....const import urljoin
from ...base import PRAWBase
from ...reddit.submission import Submission
from ..generator import ListingGenerator
from typing import Set, Optional, Dict

class BaseListingMixin(PRAWBase):
    VALID_TIME_FILTERS: Set[str] = ...
    def controversial(self, time_filter: str = ...,
                            limit: int = ...,
                            params: Optional[Dict[str, str]] = ...,
                            ) -> ListingGenerator[Submission]: ...
    def hot(self, limit: int = ...,
                  params: Optional[Dict[str, str]] = ...,
                  ) -> ListingGenerator[Submission]: ...
    def new(self, limit: int = ...,
                  params: Optional[Dict[str, str]] = ...,
                  ) -> ListingGenerator[Submission]: ...
    def top(self, time_filter: str = ...,
                  limit: int = ...,
                  params: Optional[Dict[str, str]] = ...,
                  ) -> ListingGenerator[Submission]: ...
