from gw2apy.endpoints.endpoint import AuthenticatedAbstractEndpoint


class TokenInfo(AuthenticatedAbstractEndpoint):
    def __init__(self, client):
        super(TokenInfo, self).__init__(client=client)

        self.endpoint_path = "/v2/tokeninfo"
