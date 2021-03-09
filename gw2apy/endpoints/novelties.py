from gw2apy.endpoints.endpoint import AbstractEndpoint


class Novelties(AbstractEndpoint):
    def __init__(self, client):
        super(Novelties, self).__init__(client=client)

        self.endpoint_path = "/v2/novelties"

        self.has_pages = True
        self.has_ids = True
        self.has_all_ids = True
