from typing import Callable, TypeVar, Dict

N = TypeVar('N', int, float)

def filter_dict_by_value(d: Dict[str, N], predicate: Callable[[N], bool]) -> Dict[str, N]:
    # Implement filtering logic here using a dictionary comprehension
    new_d={}
    d_values=list(filter(predicate, d.values()))

    for i in range(len(d_values)):
        for key,value in d.items():
            if d[key]==d_values[i]:
                new_d[key]=value

    return new_d
# Example usage:
print(filter_dict_by_value({"a":1, "b":2, "c":3}, lambda x: x > 1))
# Expected output: {"b":2, "c":3}
