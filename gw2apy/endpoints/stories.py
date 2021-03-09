from gw2apy.endpoints.endpoint import AbstractEndpoint


class Stories(AbstractEndpoint):
    def __init__(self, client):
        super(Stories, self).__init__(client=client)

        self.endpoint_path = "/v2/stories"

        self.has_pages = True
        self.has_ids = True
        self.has_all_ids = True


class StoriesSeasons(AbstractEndpoint):
    def __init__(self, client):
        super(StoriesSeasons, self).__init__(client=client)

        self.endpoint_path = "/v2/stories/seasons"

        self.has_pages = True
        self.has_ids = True
        self.has_all_ids = True
