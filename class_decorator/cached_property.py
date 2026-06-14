from functools import cached_property

class Data:

    @cached_property
    def heavy_task(self):
        print("Computing...")
        total = sum(range(1000000))
        return total


d = Data()

print(d.heavy_task)  # computed
print(d.heavy_task)  # cached, no recomputation