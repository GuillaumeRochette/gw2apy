from gw2apy.endpoints.endpoint import AuthenticatedAbstractEndpoint


class Characters(AuthenticatedAbstractEndpoint):
    def __init__(self, client):
        super(Characters, self).__init__(client=client)

        self.endpoint_path = "/v2/characters"

        self.has_pages = True
        self.has_ids = True
        self.has_all_ids = True


class CharactersSubEndpoint(AuthenticatedAbstractEndpoint):
    def __init__(self, client, category: str):
        super(CharactersSubEndpoint, self).__init__(client=client)

        assert category in [
            "backstory",
            "core",
            "crafting",
            "equipment",
            "heropoints",
            "inventory",
            "recipes",
            "sab",
            "skills",
            "specializations",
            "training",
        ]
        self.endpoint_path = f"/v2/characters"
        self.category = category

    def get(self, character_name: str):
        path = f"/{character_name}/{self.category}"
        return super(CharactersSubEndpoint, self).get(path=path)


class CharactersBackstory(CharactersSubEndpoint):
    def __init__(self, client):
        super(CharactersBackstory, self).__init__(
            client=client,
            category="backstory",
        )


class CharactersCore(CharactersSubEndpoint):
    def __init__(self, client):
        super(CharactersCore, self).__init__(
            client=client,
            category="core",
        )


class CharactersCrafting(CharactersSubEndpoint):
    def __init__(self, client):
        super(CharactersCrafting, self).__init__(
            client=client,
            category="crafting",
        )


class CharactersEquipment(CharactersSubEndpoint):
    def __init__(self, client):
        super(CharactersEquipment, self).__init__(
            client=client,
            category="equipment",
        )


class CharactersHeroPoints(CharactersSubEndpoint):
    def __init__(self, client):
        super(CharactersHeroPoints, self).__init__(
            client=client,
            category="heropoints",
        )


class CharactersInventory(CharactersSubEndpoint):
    def __init__(self, client):
        super(CharactersInventory, self).__init__(
            client=client,
            category="inventory",
        )


class CharactersRecipes(CharactersSubEndpoint):
    def __init__(self, client):
        super(CharactersRecipes, self).__init__(
            client=client,
            category="recipes",
        )


class CharactersSAB(CharactersSubEndpoint):
    def __init__(self, client):
        super(CharactersSAB, self).__init__(
            client=client,
            category="sab",
        )


class CharactersSkills(CharactersSubEndpoint):
    def __init__(self, client):
        super(CharactersSkills, self).__init__(
            client=client,
            category="skills",
        )


class CharactersSpecializations(CharactersSubEndpoint):
    def __init__(self, client):
        super(CharactersSpecializations, self).__init__(
            client=client,
            category="specializations",
        )


class CharactersTraining(CharactersSubEndpoint):
    def __init__(self, client):
        super(CharactersTraining, self).__init__(
            client=client,
            category="training",
        )
