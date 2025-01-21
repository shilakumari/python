from typing import TypeVar, Generic
T=TypeVar('T')
class Box(Generic[T]):
    def __init__(self, content:T):
        self.content=content

b1=Box(10)
print(b1.content)

b1=Box([1,2,3])
print(b1.content)

b1=Box(["1","a","d"])
print(b1.content)