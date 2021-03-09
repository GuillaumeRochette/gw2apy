from typing import Iterable
import sys
from requests_futures.sessions import FuturesSession
from concurrent.futures import as_completed


class Client(object):
    def __init__(
        self,
        base_url: str = "https://api.guildwars2.com",
        schema_version: str = "2020-11-17T00:30:00.000Z",
        lang: str = "en",
        api_key: str = None,
        max_workers: int = 64,
        debug: bool = False,
    ):
        self.base_url = base_url
        self.schema_version = schema_version
        self.lang = lang

        self.api_key = api_key

        self.session = self.build_session(max_workers=max_workers)

        self.debug = debug

    def build_session(self, max_workers: int):
        session = FuturesSession(max_workers=max_workers)

        session.verify = True

        headers = {
            "User-Agent": "GuildWars2-API-Python-Wrapper",
            "Accept": "application/json",
            "Accept-Language": self.lang,
            "X-Schema-Version": self.schema_version,
        }

        if self.api_key is not None:
            headers["Authorization"] = f"Bearer {self.api_key}"

        session.headers.update(headers)
        return session

    def get(self, url: str):
        future = self.session.get(url, hooks={"response": JSONify})
        response = future.result()

        if self.debug:
            print(response.status_code, response.url, file=sys.stderr)

        return response

    def gets(self, urls: Iterable[str]):
        futures = [self.session.get(url, hooks={"response": JSONify}) for url in urls]
        responses = [future.result() for future in as_completed(futures)]

        if self.debug:
            for response in responses:
                print(response.status_code, response.url, file=sys.stderr)

        return responses


def JSONify(response, *args, **kwargs):
    response.data = response.json()
