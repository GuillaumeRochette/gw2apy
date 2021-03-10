from typing import Dict, Iterable, Union
from concurrent.futures import as_completed

from requests_futures.sessions import FuturesSession
from ratelimit import limits, sleep_and_retry


class Client(object):
    def __init__(
        self,
        api_key: str = None,
        base_url: str = "https://api.guildwars2.com",
        schema_version: str = "2020-11-17T00:30:00.000Z",
        lang: str = "en",
        proxy: Dict[str, str] = None,
        verify: Union[bool, str] = True,
        max_workers: int = 256,
    ):
        self.api_key = api_key
        self.base_url = base_url
        self.schema_version = schema_version
        self.lang = lang
        self.proxy = proxy
        self.verify = verify
        self.max_workers = max_workers

        self.session = self._build_session()

    def _build_session(self):
        session = FuturesSession(max_workers=self.max_workers)

        headers = {
            "User-Agent": "GuildWars2-API-Python-Wrapper",
            "Accept": "application/json",
            "Accept-Language": self.lang,
            "X-Schema-Version": self.schema_version,
        }
        if self.api_key is not None:
            headers["Authorization"] = f"Bearer {self.api_key}"
        session.headers.update(headers)

        session.verify = self.verify

        if self.proxy is not None:
            session.proxies.update(self.proxy)

        return session

    def get(self, url: str):
        future = self._get(url=url)
        response = future.result()
        return response

    def gets(self, urls: Iterable[str]):
        futures = [self._get(url=url) for url in urls]
        responses = [future.result() for future in as_completed(futures)]
        return responses

    @sleep_and_retry
    @limits(calls=600, period=60)
    def _get(self, url: str):
        future = self.session.get(url=url, hooks={"response": _JSONify})
        return future


def _JSONify(response, *args, **kwargs):
    response.data = response.json()
