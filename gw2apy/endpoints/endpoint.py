from itertools import chain


class AbstractEndpoint(object):
    def __init__(self, client):
        self.client = client

        self.endpoint_path = None

        self.has_pages = False
        self.has_ids = False
        self.has_all_ids = False

        self.max_page_size = 200

    def endpoint(self):
        response = self._endpoint()
        return response.data

    def path(self, path):
        response = self._path(path=path)
        return response.data

    def id(self, id):
        assert self.has_ids, f"{self.__class__} does not have ids."
        response = self._id(id=id)
        return response.data

    def page(self, page, page_size=None):
        assert self.has_pages, f"{self.__class__} does not have pages."
        response = self._page(page=page, page_size=page_size)
        return response.data

    def ids(self, ids):
        assert self.has_ids, f"{self.__class__} does not have ids."
        responses = self._ids(ids=ids)
        return flatten([response.data for response in responses])

    def pages(self, pages, page_size=None):
        assert self.has_pages, f"{self.__class__} does not have pages."
        responses = self._pages(pages=pages, page_size=page_size)
        return flatten([response.data for response in responses])

    def all(self):
        c = self.has_ids or self.has_pages
        assert c, f"{self.__class__} does not have ids nor pages."
        if self.has_all_ids:
            response = self._all()
            return response.data
        elif self.has_pages:
            responses = self._all_by_pages()
            return flatten([response.data for response in responses])
        else:
            responses = self._all_by_ids()
            return flatten([response.data for response in responses])

    def get(self, **kwargs):
        path = kwargs.get("path")
        id = kwargs.get("id")
        page = kwargs.get("page")
        ids = kwargs.get("ids")
        pages = kwargs.get("pages")
        page_size = kwargs.get("page_size")

        c_path = path is not None
        c_id = id is not None
        c_page = page is not None
        c_ids = ids is not None
        c_pages = pages is not None
        c_page_size = page_size is not None

        c = (c_path + c_id + c_page + c_ids + c_pages) > 1
        assert not c, "'path', 'id', 'page', 'ids', 'pages' are to be used separately."
        c = c_page_size and not (c_page or c_pages)
        assert not c, "'page_size' cannot be used without 'page' or 'pages'."

        if c_path:
            return self.path(path=path)
        elif c_id:
            return self.id(id=id)
        elif c_page:
            return self.page(page=page, page_size=page_size)
        elif c_ids:
            if ids != "all":
                return self.ids(ids=ids)
            else:
                return self.all()
        elif c_pages:
            return self.pages(pages=pages, page_size=page_size)
        else:
            return self.endpoint()

    def _endpoint(self):
        url = self._endpoint_base_url()
        response = self.client.get(url=url)
        return response

    def _path(self, path):
        suffix = f"{path}"
        url = self._endpoint_base_url() + suffix
        response = self.client.get(url=url)
        return response

    def _id(self, id):
        suffix = f"?id={id}"
        url = self._endpoint_base_url() + suffix
        response = self.client.get(url=url)
        return response

    def _page(self, page, page_size=None):
        if page_size is None:
            page_size = self.max_page_size
        assert 0 <= page_size <= self.max_page_size

        suffix = f"?page={page}&page_size={page_size}"
        url = self._endpoint_base_url() + suffix
        response = self.client.get(url=url)
        return response

    def _ids(self, ids):
        chunked_ids = [c for c in chunk(ids, self.max_page_size)]
        suffixes = [f"?ids={','.join(map(str, c))}" for c in chunked_ids]
        urls = [self._endpoint_base_url() + suffix for suffix in suffixes]
        responses = self.client.gets(urls=urls)
        return responses

    def _pages(self, pages, page_size=None):
        if page_size is None:
            page_size = self.max_page_size
        assert 0 <= page_size <= self.max_page_size

        suffixes = [f"?page={page}&page_size={page_size}" for page in pages]
        urls = [self._endpoint_base_url() + suffix for suffix in suffixes]
        responses = self.client.gets(urls=urls)
        return responses

    def _all(self):
        suffix = "?ids=all"
        url = self._endpoint_base_url() + suffix
        response = self.client.get(url=url)
        return response

    def _all_by_ids(self):
        response = self._endpoint()
        ids = response.data
        response = self._ids(ids=ids)
        return response

    def _all_by_pages(self):
        first_response = self._page(page=0)
        num_pages = int(first_response.headers["X-Page-Total"])
        remaining_responses = self._pages(pages=range(1, num_pages))
        return [first_response] + remaining_responses

    def _endpoint_base_url(self):
        return self.client.base_url + self.endpoint_path


class AuthenticatedAbstractEndpoint(AbstractEndpoint):
    def __init__(self, client):
        assert client.api_key is not None
        super(AuthenticatedAbstractEndpoint, self).__init__(client=client)


def chunk(l, n):
    for i in range(0, len(l), n):
        yield l[i : i + n]


def flatten(l):
    return list(chain(*l))
