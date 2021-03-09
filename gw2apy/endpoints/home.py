from gw2apy.endpoints.endpoint import AbstractEndpoint


class Home(AbstractEndpoint):
    def __init__(self, client, category: str):
        super(Home, self).__init__(client=client)

        assert category in ["cats", "nodes"]
        self.endpoint_path = f"/v2/home/{category}"

        self.has_pages = True
        self.has_ids = True
        self.has_all_ids = True


class HomeCats(Home):
    def __init__(self, client):
        super(HomeCats, self).__init__(
            client=client,
            category="cats",
        )


class HomeNodes(Home):
    def __init__(self, client):
        super(HomeNodes, self).__init__(
            client=client,
            category="nodes",
        )
