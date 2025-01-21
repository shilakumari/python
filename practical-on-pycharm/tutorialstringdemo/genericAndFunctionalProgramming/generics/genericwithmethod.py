from typing import TypeVar
T=TypeVar('T')
def get_first(items:list[T])->T:
    return items[0]
l=[1,23,34]
print(get_first(l))