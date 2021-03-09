from gw2apy.endpoints.endpoint import AbstractEndpoint


class Emblem(AbstractEndpoint):
    def __init__(self, client, category: str):
        super(Emblem, self).__init__(client=client)

        assert category in ["backgrounds", "foregrounds"]
        self.endpoint_path = f"/v2/emblem/{category}"

        self.has_pages = True
        self.has_ids = True


class EmblemBackgrounds(Emblem):
    def __init__(self, client):
        super(EmblemBackgrounds, self).__init__(
            client=client,
            category="backgrounds",
        )


class EmblemForegrounds(Emblem):
    def __init__(self, client):
        super(EmblemForegrounds, self).__init__(
            client=client,
            category="foregrounds",
        )
