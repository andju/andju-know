---
published: true
---
# Python Collections

| **Name**                                                                                              | Type     | **Mutable** | **Ordered** | **Compares Order** |      **Hashable**      | **Comments**                                |
| ----------------------------------------------------------------------------------------------------- | -------- | :---------: | :---------: | :----------------: | :--------------------: | ------------------------------------------- |
| [list](https://docs.python.org/3/library/stdtypes.html#list)                                          | sequence |     Yes     |     Yes     |        Yes         |           No           |                                             |
| [tuple](https://docs.python.org/3/library/stdtypes.html#tuples)                                       | sequence |     No      |     Yes     |        Yes         |          Yes           |                                             |
| [set](https://docs.python.org/3/library/stdtypes.html#set)                                            | set      |     Yes     |     No      |         -          |           No           |                                             |
| [frozenset](https://docs.python.org/3/library/stdtypes.html#frozenset)                                | set      |     No      |     No      |         -          |          Yes           |                                             |
| [dict](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)                            | mapping  |     Yes     | Yes (>=3.7) |         No         |           No           |                                             |
| [collections.deque](https://docs.python.org/3/library/collections.html#collections.deque)             | sequence |     Yes     |     Yes     |                    |           No           | Fast pop and append on begin/end            |
| [collections.Counter](https://docs.python.org/3/library/collections.html#counter-objects)             | mapping  |     Yes     |     No      |         -          |           No           | Counting hashable Objects                   |
| [dataclasses.dataclass](https://docs.python.org/3/library/dataclasses.html)                           | mapping  |     Yes     |     Yes     |                    |       If frozen        |                                             |
| [collections.defaultdict](https://docs.python.org/3/library/collections.html#collections.defaultdict) | mapping  |     Yes     |             |                    |           No           | Adds value of function for non-existing key |
| [typing.NamedTuple](https://docs.python.org/3/library/typing.html#typing.NamedTuple)                  | mapping  |     No      |     Yes     |                    | Depends on the content |                                             |