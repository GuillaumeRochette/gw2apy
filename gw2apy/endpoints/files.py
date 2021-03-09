from gw2apy.endpoints.endpoint import AbstractEndpoint


class Files(AbstractEndpoint):
    def __init__(self, client):
        super(Files, self).__init__(client=client)

        self.endpoint_path = "/v2/files"

        self.has_pages = True
        self.has_ids = True
        self.has_all_ids = True
