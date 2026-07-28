data = {"a": 1, "b": 2}
data["a"] += data.get("c", 3)
print(data["a"])