import sys
from typing import Dict

__version__: str = ...

API_PATH: Dict[str, str]
JPEG_HEADER: bytes
MAX_IMAGE_SIZE: int
MIN_PNG_SIZE: int
MIN_JPEG_SIZE: int
PNG_HEADER: bytes
USER_AGENT_FORMAT: str

if sys.version_info < (3, 0):
    import ConfigParser as configparser
    from urlparse import urljoin as urljoin, urlparse as urlparse
else:
    import configparser as configparser
    from urllib.parse import urljoin as urljoin, urlparse as urlparse
