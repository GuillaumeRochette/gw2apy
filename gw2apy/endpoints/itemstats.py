from gw2apy.endpoints.endpoint import AbstractEndpoint


class ItemStats(AbstractEndpoint):
    def __init__(self, client):
        super(ItemStats, self).__init__(client=client)

        self.endpoint_path = "/v2/itemstats"

        self.has_pages = True
        self.has_ids = True
        self.has_all_ids = True
