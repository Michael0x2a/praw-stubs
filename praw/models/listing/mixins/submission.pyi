from ....const import API_PATH
from ...base import PRAWBase
from ...reddit.submission import Submission
from ..generator import ListingGenerator
from typing import Optional, Dict

class SubmissionListingMixin(PRAWBase):
    def duplicates(
        self, limit: int = ..., params: Optional[Dict[str, str]] = ...
    ) -> ListingGenerator[Submission]: ...
