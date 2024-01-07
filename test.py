import json
from types import SimpleNamespace

obj = {
    "key" : "test"
}

if hasattr(obj, 'key'):
     print("----- signupHandler :: ", obj["token"])

obj_ns = SimpleNamespace(**obj)

# Access the value using dot notation
print(type(obj_ns))  # Output: test
print(obj_ns.key)  # Output: test