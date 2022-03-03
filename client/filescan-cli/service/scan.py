import os
import json
from typing import Optional
from common.config import API_KEY, USER_AGENT
from core.http import HttpRequests
from core.logger import Logger
from common.utils import run_safe
from .endpoints import get_endpoint, FILE_SCAN, GET_SCAN_REPORTS
from .report import Report


class Scan():
    """Scan a file"""

    def __init__(self):
        self.http_client = HttpRequests()
        self.logger = Logger()
        self.report = Report()
        self.headers = {
            'X-Api-Key': API_KEY,
            'accept': 'application/json',
            'User-Agent': USER_AGENT
        }


    async def upload(
        self,
        file: Optional[str],
        link: Optional[str],
        desc: str,
        tags: str,
        prop_tags: bool,
        password: str,
        is_private: bool
    ):
        """Upload a file for scanning"""

        if file:
            name = os.path.basename(file)
        else:
            name = link[link.rindex('/') + 1:]

        result = await run_safe(
            self.http_client.post_file,
            get_endpoint(FILE_SCAN),
            self.headers,
            {
                'name': name,
                'path': file,
                'link': link,
                'extra': {
                    'description': desc,
                    'tags': tags,
                    'propagate_tags': f'{prop_tags}',
                    'password': password,
                    'is_private': f'{is_private}'
                }
            }
        )

        return json.loads(result)
