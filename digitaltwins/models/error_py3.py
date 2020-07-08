# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Error(Model):
    """Error definition.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar code: Service specific error code which serves as the substatus for
     the HTTP error code.
    :vartype code: str
    :ivar message: A human-readable representation of the error.
    :vartype message: str
    :ivar details: Internal error details.
    :vartype details: list[~digitaltwins.models.Error]
    :param innererror: An object containing more specific information than the
     current object about the error.
    :type innererror: ~digitaltwins.models.InnerError
    """

    _validation = {
        'code': {'readonly': True},
        'message': {'readonly': True},
        'details': {'readonly': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'details': {'key': 'details', 'type': '[Error]'},
        'innererror': {'key': 'innererror', 'type': 'InnerError'},
    }

    def __init__(self, *, innererror=None, **kwargs) -> None:
        super(Error, self).__init__(**kwargs)
        self.code = None
        self.message = None
        self.details = None
        self.innererror = innererror
