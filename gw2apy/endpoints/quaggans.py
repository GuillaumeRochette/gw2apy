from gw2apy.endpoints.endpoint import AbstractEndpoint


class Quaggans(AbstractEndpoint):
    def __init__(self, client):
        super(Quaggans, self).__init__(client=client)

        self.endpoint_path = "/v2/quaggans"

        self.has_pages = True
        self.has_ids = True
        self.has_all_ids = True
