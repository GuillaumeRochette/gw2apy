from gw2apy.endpoints.endpoint import AbstractEndpoint


class Recipes(AbstractEndpoint):
    def __init__(self, client):
        super(Recipes, self).__init__(client=client)

        self.endpoint_path = "/v2/recipes"

        self.has_pages = True
        self.has_ids = True


class RecipesSearch(AbstractEndpoint):
    def __init__(self, client):
        super(RecipesSearch, self).__init__(client=client)

        self.endpoint_path = "/v2/recipes/search"

    def get(self, **kwargs):
        input = kwargs.get("input")
        output = kwargs.get("output")

        c_input = input is not None
        c_output = output is not None

        c = c_input != c_output
        assert c, "Must provide either 'input' or 'output' exclusively."

        if c_input:
            path = f"?input={input}"
        else:
            path = f"?output={output}"
        return super(RecipesSearch, self).get(path=path)
