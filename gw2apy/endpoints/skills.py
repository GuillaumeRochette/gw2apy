from gw2apy.endpoints.endpoint import AbstractEndpoint


class Skills(AbstractEndpoint):
    def __init__(self, client):
        super(Skills, self).__init__(client=client)

        self.endpoint_path = "/v2/skills"

        self.has_pages = True
        self.has_ids = True
        self.has_all_ids = True
