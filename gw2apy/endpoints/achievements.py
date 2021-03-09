from gw2apy.endpoints.endpoint import AbstractEndpoint


class Achievements(AbstractEndpoint):
    def __init__(self, client):
        super(Achievements, self).__init__(client=client)

        self.endpoint_path = "/v2/achievements"

        self.has_pages = True
        self.has_ids = True


class AchievementsCategories(AbstractEndpoint):
    def __init__(self, client):
        super(AchievementsCategories, self).__init__(client=client)

        self.endpoint_path = "/v2/achievements/categories"

        self.has_pages = True
        self.has_ids = True
        self.has_all_ids = True


class AchievementsDaily(AbstractEndpoint):
    def __init__(self, client):
        super(AchievementsDaily, self).__init__(client=client)

        self.endpoint_path = "/v2/achievements/daily"


class AchievementsDailyTomorrow(AbstractEndpoint):
    def __init__(self, client):
        super(AchievementsDailyTomorrow, self).__init__(client=client)

        self.endpoint_path = "/v2/achievements/daily/tomorrow"


class AchievementsGroups(AbstractEndpoint):
    def __init__(self, client):
        super(AchievementsGroups, self).__init__(client=client)

        self.endpoint_path = "/v2/achievements/groups"

        self.has_pages = True
        self.has_ids = True
        self.has_all_ids = True
