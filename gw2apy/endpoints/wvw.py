from gw2apy.endpoints.endpoint import AbstractEndpoint


class WvW(AbstractEndpoint):
    def __init__(self, client, category: str):
        super(WvW, self).__init__(client=client)

        assert category in [
            "abilities",
            "matches",
            "objectives",
            "ranks",
            "upgrades",
        ]
        self.endpoint_path = f"/v2/wvw/{category}"

        self.has_pages = True
        self.has_ids = True
        self.has_all_ids = True


class WvWAbilities(WvW):
    def __init__(self, client):
        super(WvWAbilities, self).__init__(
            client=client,
            category="abilities",
        )


class WvWMatches(WvW):
    def __init__(self, client):
        super(WvWMatches, self).__init__(
            client=client,
            category="matches",
        )


class WvWObjectives(WvW):
    def __init__(self, client):
        super(WvWObjectives, self).__init__(
            client=client,
            category="objectives",
        )


class WvWRanks(WvW):
    def __init__(self, client):
        super(WvWRanks, self).__init__(
            client=client,
            category="ranks",
        )


class WvWUpgrades(WvW):
    def __init__(self, client):
        super(WvWUpgrades, self).__init__(
            client=client,
            category="upgrades",
        )
