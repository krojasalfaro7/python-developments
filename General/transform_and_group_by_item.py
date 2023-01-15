import pprint


def transform_and_group_by_item(data: list, item_group: str) -> dict:
    data_transform = {}
    if len(data) > 1:
        for elem in data:
            if elem[item_group] in data_transform:
                data_transform[elem[item_group]].append(elem)
            else:
                data_transform[elem[item_group]] = [elem]
    elif len(data) == 1:
        data_transform[data[0][item_group]] = [data[0]]
    return data_transform


data = [
    {
        "name": "Pepito",
        "ciudad": "Caracas",
        "pais": "Venezuela",
        "edad": 25
    },
    {
        "name": "Maria",
        "ciudad": "Caracas",
        "pais": "Venezuela",
        "edad": 20
    },
    {
        "name": "Carlos",
        "ciudad": "Vargas",
        "pais": "Venezuela",
        "edad": 30
    },
    {
        "name": "ALberto",
        "ciudad": "Miranda",
        "pais": "Venezuela",
        "edad": 10
    },
    {
        "name": "Miriam",
        "ciudad": "Vargas",
        "pais": "Venezuela",
        "edad": 28
    },
        {
        "name": "Carlos",
        "ciudad": "Vargas",
        "pais": "Venezuela",
        "edad": 28
    }
]

print(pprint.pformat(transform_and_group_by_item(data=data, item_group='name')))
