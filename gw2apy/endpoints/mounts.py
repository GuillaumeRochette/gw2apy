from gw2apy.endpoints.endpoint import AbstractEndpoint


class Mounts(AbstractEndpoint):
    def __init__(self, client, category: str):
        super(Mounts, self).__init__(client=client)

        assert category in ["skins", "types"]
        self.endpoint_path = f"/v2/mounts/{category}"

        self.has_pages = True
        self.has_ids = True
        self.has_all_ids = True


class MountsSkins(Mounts):
    def __init__(self, client):
        super(MountsSkins, self).__init__(
            client=client,
            category="skins",
        )


class MountsTypes(Mounts):
    def __init__(self, client):
        super(MountsTypes, self).__init__(
            client=client,
            category="types",
        )
