from gw2apy.endpoints.endpoint import AuthenticatedAbstractEndpoint


class Guild(AuthenticatedAbstractEndpoint):
    def __init__(self, client):
        super(Guild, self).__init__(client=client)

        self.endpoint_path = f"/v2/guild"

    def get(self, **kwargs):
        search = kwargs.get("search")

        c_search = search is not None

        if c_search:
            path = f"?search={search}"
            return super(Guild, self).get(path=path)
        else:
            return super(Guild, self).get(kwargs=kwargs)
