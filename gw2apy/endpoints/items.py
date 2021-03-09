from gw2apy.endpoints.endpoint import AbstractEndpoint


class Items(AbstractEndpoint):
    def __init__(self, client):
        super(Items, self).__init__(client=client)

        self.endpoint_path = "/v2/items"

        self.has_pages = True
        self.has_ids = True
