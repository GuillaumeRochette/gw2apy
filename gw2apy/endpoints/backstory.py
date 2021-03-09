from gw2apy.endpoints.endpoint import AbstractEndpoint


class Backstory(AbstractEndpoint):
    def __init__(self, client, category: str):
        super(Backstory, self).__init__(client=client)

        assert category in ["answers", "questions"]
        self.endpoint_path = f"/v2/backstory/{category}"

        self.has_pages = True
        self.has_ids = True
        self.has_all_ids = True


class BackstoryAnswers(Backstory):
    def __init__(self, client):
        super(BackstoryAnswers, self).__init__(
            client=client,
            category="answers",
        )


class BackstoryQuestions(Backstory):
    def __init__(self, client):
        super(BackstoryQuestions, self).__init__(
            client=client,
            category="questions",
        )
