from gw2apy.endpoints.endpoint import AbstractEndpoint, AuthenticatedAbstractEndpoint


class CommerceDelivery(AuthenticatedAbstractEndpoint):
    def __init__(self, client):
        super(CommerceDelivery, self).__init__(client=client)

        self.endpoint_path = "/v2/commerce/delivery"

        self.has_pages = True


class CommerceExchange(AbstractEndpoint):
    def __init__(self, client, currency: str):
        super(CommerceExchange, self).__init__(client=client)

        assert currency in ["coins", "gems"]
        self.endpoint_path = f"/v2/commerce/exchange/{currency}"

    def get(self, quantity: int):
        assert quantity >= 0
        path = f"?quantity={quantity}"
        return super(CommerceExchange, self).get(path=path)


class CommerceExchangeGems(CommerceExchange):
    def __init__(self, client):
        super(CommerceExchangeGems, self).__init__(
            client=client,
            currency="gems",
        )


class CommerceExchangeCoins(CommerceExchange):
    def __init__(self, client):
        super(CommerceExchangeCoins, self).__init__(
            client=client,
            currency="coins",
        )


class CommerceListings(AbstractEndpoint):
    def __init__(self, client):
        super(CommerceListings, self).__init__(client=client)

        self.endpoint_path = "/v2/commerce/listings"

        self.has_pages = True
        self.has_ids = True


class CommercePrices(AbstractEndpoint):
    def __init__(self, client):
        super(CommercePrices, self).__init__(client=client)

        self.endpoint_path = "/v2/commerce/prices"

        self.has_pages = True
        self.has_ids = True


class CommerceTransaction(AuthenticatedAbstractEndpoint):
    def __init__(self, client, category: str, order: str):
        super(CommerceTransaction, self).__init__(client=client)

        assert category in ["current", "history"]
        assert order in ["buys", "sells"]
        self.endpoint_path = f"/v2/commerce/transactions/{category}/{order}"


class CommerceTransactionCurrentBuys(CommerceTransaction):
    def __init__(self, client):
        super(CommerceTransactionCurrentBuys, self).__init__(
            client=client,
            category="current",
            order="buys",
        )


class CommerceTransactionCurrentSells(CommerceTransaction):
    def __init__(self, client):
        super(CommerceTransactionCurrentSells, self).__init__(
            client=client,
            category="current",
            order="sells",
        )


class CommerceTransactionHistoryBuys(CommerceTransaction):
    def __init__(self, client):
        super(CommerceTransactionHistoryBuys, self).__init__(
            client=client,
            category="history",
            order="buys",
        )


class CommerceTransactionHistorySells(CommerceTransaction):
    def __init__(self, client):
        super(CommerceTransactionHistorySells, self).__init__(
            client=client,
            category="history",
            order="sells",
        )
