from gw2apy.endpoints.endpoint import AbstractEndpoint


class MapChests(AbstractEndpoint):
    def __init__(self, client):
        super(MapChests, self).__init__(client=client)

        self.endpoint_path = "/v2/mapchests"

        self.has_pages = True
        self.has_ids = True
        self.has_all_ids = True
