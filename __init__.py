# from typing import Dict, Any, Iterator, Optional
# from collections import abc
# from types import FunctionType
# import inspect


# class DynamicScope(abc.Mapping):
#     def __init__(self):
#         self.env: Dict[str, Optional[Any]] = {}
#     def __len__(self):
#         return len(self.env)
#     def __getitem__(self, key):
#         if key not in self.env:
#             raise NameError(f"Name '{key}' is not defined.")
#         return self.env[key]
#     def __iter__(self):
#         return self.env.__iter__()
#     def __setitem__(self, key, value):
#         self.env[key] = value
#     def __delitem__(self,key):
#         del self.env[key]
#     def __contains__(self, value: str):
#         return self.env.__contains__(value)

# def get_dynamic_re() -> DynamicScope:
#     dre = DynamicScope()
#     stack_info = inspect.stack()
#     for frame_info in stack_info[1:]:
#         frame = frame_info.frame
#         free_vars = set(frame.f_code.co_freevars)
#         for key, value in frame.f_locals.items():
#             if key not in dre and key not in free_vars:
#                 dre[key] = value
#     return dre


from typing import Dict, Any, Optional
from collections import abc
import inspect


class DynamicScope(abc.Mapping):
    def __init__(self):
        self.env: Dict[str, Optional[Any]] = {}

    # __getitem__ from version 1
    def __getitem__(self, key):
        if key not in self.env:
            raise NameError(f"Name '{key}' is not defined.")
        return self.env[key]

    # All other methods from version 2
    def __contains__(self, value: str):
        return self.env.__contains__(value)

    def __len__(self) -> int:
        return len(self.env)

    def __iter__(self):
        return self.env.__iter__()

    def __setitem__(self, key, value):
        self.env[key] = value

    def __delitem__(self, key):
        del self.env[key]


# get_dynamic_re from version 1
def get_dynamic_re() -> DynamicScope:
    dre = DynamicScope()
    stack_info = inspect.stack()
    for frame_info in stack_info[1:]:
        frame = frame_info.frame
        free_vars = set(frame.f_code.co_freevars)
        for key, value in frame.f_locals.items():
            if key not in dre and key not in free_vars:
                dre[key] = value
    return dre