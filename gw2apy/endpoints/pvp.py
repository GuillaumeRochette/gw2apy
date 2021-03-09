from gw2apy.endpoints.endpoint import AbstractEndpoint


class PvP(AbstractEndpoint):
    def __init__(self, client, category: str):
        super(PvP, self).__init__(client=client)

        assert category in [
            "amulets",
            "games",
            "heroes",
            "ranks",
            "seasons",
            "standings",
            "stats",
        ]
        self.endpoint_path = f"/v2/pvp/{category}"

        self.has_pages = True
        self.has_ids = True
        self.has_all_ids = True


class PvPAmulets(PvP):
    def __init__(self, client):
        super(PvPAmulets, self).__init__(
            client=client,
            category="amulets",
        )


class PvPGames(PvP):
    def __init__(self, client):
        assert client.api_key is not None
        super(PvPGames, self).__init__(
            client=client,
            category="games",
        )


class PvPHeroes(PvP):
    def __init__(self, client):
        super(PvPHeroes, self).__init__(
            client=client,
            category="heroes",
        )


class PvPRanks(PvP):
    def __init__(self, client):
        super(PvPRanks, self).__init__(
            client=client,
            category="ranks",
        )


class PvPSeasons(PvP):
    def __init__(self, client):
        super(PvPSeasons, self).__init__(
            client=client,
            category="seasons",
        )


class PvPStandings(PvP):
    def __init__(self, client):
        assert client.api_key
        super(PvPStandings, self).__init__(
            client=client,
            category="standings",
        )


class PvPStats(PvP):
    def __init__(self, client):
        assert client.api_key
        super(PvPStats, self).__init__(
            client=client,
            category="stats",
        )
