# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class QueryResult(Model):
    """The results of a query operation and an optional continuation token.

    :param items: The query results.
    :type items: list[object]
    :param continuation_token: A token which can be used to construct a new
     QuerySpecification to retrieve the next set of results.
    :type continuation_token: str
    """

    _attribute_map = {
        'items': {'key': 'items', 'type': '[object]'},
        'continuation_token': {'key': 'continuationToken', 'type': 'str'},
    }

    def __init__(self, *, items=None, continuation_token: str=None, **kwargs) -> None:
        super(QueryResult, self).__init__(**kwargs)
        self.items = items
        self.continuation_token = continuation_token