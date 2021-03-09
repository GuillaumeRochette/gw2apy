from gw2apy.endpoints.endpoint import AbstractEndpoint


class Skins(AbstractEndpoint):
    def __init__(self, client):
        super(Skins, self).__init__(client=client)

        self.endpoint_path = "/v2/skins"

        self.has_pages = True
        self.has_ids = True
