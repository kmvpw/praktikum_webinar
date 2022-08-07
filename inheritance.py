class Mydict(dict):
    def get(self, key, default = 0):
        return dict.get(self, key, default)

a = dict(a=1, b=2)
b = Mydict(a=1, b=2)

b["c"] = 4























print(f'dict: {a.get("v")}')
print("-------")
print(f'Mydict: {b.get("v")}')
