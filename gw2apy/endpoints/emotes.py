from gw2apy.endpoints.endpoint import AbstractEndpoint


class Emotes(AbstractEndpoint):
    def __init__(self, client):
        super(Emotes, self).__init__(client=client)

        self.endpoint_path = "/v2/emotes"

        self.has_pages = True
        self.has_ids = True
        self.has_all_ids = True
