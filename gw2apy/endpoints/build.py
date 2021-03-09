from gw2apy.endpoints.endpoint import AbstractEndpoint


class Build(AbstractEndpoint):
    def __init__(self, client):
        super(Build, self).__init__(client=client)

        self.endpoint_path = "/v2/build"
