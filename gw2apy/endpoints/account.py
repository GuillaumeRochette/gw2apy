from gw2apy.endpoints.endpoint import AuthenticatedAbstractEndpoint


class Account(AuthenticatedAbstractEndpoint):
    def __init__(self, client):
        super(Account, self).__init__(client=client)

        self.endpoint_path = "/v2/account"


class AccountAchievements(AuthenticatedAbstractEndpoint):
    def __init__(self, client):
        super(AccountAchievements, self).__init__(client=client)

        self.endpoint_path = "/v2/account/achievements"


class AccountBank(AuthenticatedAbstractEndpoint):
    def __init__(self, client):
        super(AccountBank, self).__init__(client=client)

        self.endpoint_path = "/v2/account/bank"


class AccountBuildStorage(AuthenticatedAbstractEndpoint):
    def __init__(self, client):
        super(AccountBuildStorage, self).__init__(client=client)

        self.endpoint_path = "/v2/account/buildstorage"


class AccountDailyCrafting(AuthenticatedAbstractEndpoint):
    def __init__(self, client):
        super(AccountDailyCrafting, self).__init__(client=client)

        self.endpoint_path = "/v2/account/dailycrafting"


class AccountDungeons(AuthenticatedAbstractEndpoint):
    def __init__(self, client):
        super(AccountDungeons, self).__init__(client=client)

        self.endpoint_path = "/v2/account/dungeons"


class AccountDyes(AuthenticatedAbstractEndpoint):
    def __init__(self, client):
        super(AccountDyes, self).__init__(client=client)

        self.endpoint_path = "/v2/account/dyes"


class AccountEmotes(AuthenticatedAbstractEndpoint):
    def __init__(self, client):
        super(AccountEmotes, self).__init__(client=client)

        self.endpoint_path = "/v2/account/emotes"


class AccountFinishers(AuthenticatedAbstractEndpoint):
    def __init__(self, client):
        super(AccountFinishers, self).__init__(client=client)

        self.endpoint_path = "/v2/account/finishers"


class AccountGliders(AuthenticatedAbstractEndpoint):
    def __init__(self, client):
        super(AccountGliders, self).__init__(client=client)

        self.endpoint_path = "/v2/account/gliders"


class AccountHome(AuthenticatedAbstractEndpoint):
    def __init__(self, client, category: str):
        super(AccountHome, self).__init__(client=client)

        assert category in ["cats", "nodes"]
        self.endpoint_path = f"/v2/account/home/{category}"


class AccountHomeCats(AccountHome):
    def __init__(self, client):
        super(AccountHomeCats, self).__init__(
            client=client,
            category="cats",
        )


class AccountHomeNodes(AccountHome):
    def __init__(self, client):
        super(AccountHomeNodes, self).__init__(
            client=client,
            category="nodes",
        )


class AccountInventory(AuthenticatedAbstractEndpoint):
    def __init__(self, client):
        super(AccountInventory, self).__init__(client=client)

        self.endpoint_path = "/v2/account/inventory"


class AccountLuck(AuthenticatedAbstractEndpoint):
    def __init__(self, client):
        super(AccountLuck, self).__init__(client=client)

        self.endpoint_path = "/v2/account/luck"


class AccountMailCarriers(AuthenticatedAbstractEndpoint):
    def __init__(self, client):
        super(AccountMailCarriers, self).__init__(client=client)

        self.endpoint_path = "/v2/account/mailcarriers"


class AccountMapChests(AuthenticatedAbstractEndpoint):
    def __init__(self, client):
        super(AccountMapChests, self).__init__(client=client)

        self.endpoint_path = "/v2/account/mapchests"


class AccountMasteries(AuthenticatedAbstractEndpoint):
    def __init__(self, client):
        super(AccountMasteries, self).__init__(client=client)

        self.endpoint_path = "/v2/account/masteries"


class AccountMasteryPoints(AuthenticatedAbstractEndpoint):
    def __init__(self, client):
        super(AccountMasteryPoints, self).__init__(client=client)

        self.endpoint_path = "/v2/account/mastery/points"


class AccountMaterials(AuthenticatedAbstractEndpoint):
    def __init__(self, client):
        super(AccountMaterials, self).__init__(client=client)

        self.endpoint_path = "/v2/account/materials"


class AccountMinis(AuthenticatedAbstractEndpoint):
    def __init__(self, client):
        super(AccountMinis, self).__init__(client=client)

        self.endpoint_path = "/v2/account/minis"


class AccountMounts(AuthenticatedAbstractEndpoint):
    def __init__(self, client, category: str):
        super(AccountMounts, self).__init__(client=client)

        assert category in ["skins", "types"]
        self.endpoint_path = f"/v2/account/mounts/{category}"


class AccountMountsSkins(AccountMounts):
    def __init__(self, client):
        super(AccountMountsSkins, self).__init__(
            client=client,
            category="skins",
        )


class AccountMountsTypes(AccountMounts):
    def __init__(self, client):
        super(AccountMountsTypes, self).__init__(
            client=client,
            category="types",
        )


class AccountNovelties(AuthenticatedAbstractEndpoint):
    def __init__(self, client):
        super(AccountNovelties, self).__init__(client=client)

        self.endpoint_path = "/v2/account/novelties"


class AccountOutfits(AuthenticatedAbstractEndpoint):
    def __init__(self, client):
        super(AccountOutfits, self).__init__(client=client)

        self.endpoint_path = "/v2/account/outfits"


class AccountPvPHeroes(AuthenticatedAbstractEndpoint):
    def __init__(self, client):
        super(AccountPvPHeroes, self).__init__(client=client)

        self.endpoint_path = "/v2/account/pvp/heroes"


class AccountRaids(AuthenticatedAbstractEndpoint):
    def __init__(self, client):
        super(AccountRaids, self).__init__(client=client)

        self.endpoint_path = "/v2/account/raids"


class AccountRecipes(AuthenticatedAbstractEndpoint):
    def __init__(self, client):
        super(AccountRecipes, self).__init__(client=client)

        self.endpoint_path = "/v2/account/recipes"


class AccountSkins(AuthenticatedAbstractEndpoint):
    def __init__(self, client):
        super(AccountSkins, self).__init__(client=client)

        self.endpoint_path = "/v2/account/skins"


class AccountTitles(AuthenticatedAbstractEndpoint):
    def __init__(self, client):
        super(AccountTitles, self).__init__(client=client)

        self.endpoint_path = "/v2/account/titles"


class AccountWallet(AuthenticatedAbstractEndpoint):
    def __init__(self, client):
        super(AccountWallet, self).__init__(client=client)

        self.endpoint_path = "/v2/account/wallet"


class AccountWorldBosses(AuthenticatedAbstractEndpoint):
    def __init__(self, client):
        super(AccountWorldBosses, self).__init__(client=client)

        self.endpoint_path = "/v2/account/worldbosses"
