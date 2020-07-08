# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class DigitalTwinModelsListOptions(Model):
    """Additional parameters for list operation.

    :param max_item_count: The maximum number of items to retrieve per
     request. The server may choose to return less than the requested max.
     Default value: -1 .
    :type max_item_count: int
    """

    _attribute_map = {
        'max_item_count': {'key': '', 'type': 'int'},
    }

    def __init__(self, *, max_item_count: int=-1, **kwargs) -> None:
        super(DigitalTwinModelsListOptions, self).__init__(**kwargs)
        self.max_item_count = max_item_count
