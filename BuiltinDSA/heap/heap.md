# heapq — Quick Reference

A heap queue (priority queue) gives quick access to the smallest element. Python's `heapq` module implements a **min-heap** — the smallest element is always at index `0`.

```python
import heapq
li = [25, 20, 34, 23, 66, 33, 15, 30, 40]
heapq.heapify(li)  # → [15, 20, 33, 23, 66, 34, 25, 30, 40]
```

---

## Functions

| Function | Description | Example |
|---|---|---|
| `heapq.heapify(list)` | Converts a list into a min-heap **in-place** (O(n)) | `heapq.heapify(li)` |
| `heapq.heappush(heap, item)` | Pushes a new item onto the heap, maintaining heap order | `heapq.heappush(li, 44)` |
| `heapq.heappop(heap)` | Pops and returns the **smallest** element | `heapq.heappop(li)` → `15` |
| `heapq.heappushpop(heap, item)` | Pushes item then pops the smallest (faster than push + pop) | `heapq.heappushpop(li, 5)` |
| `heapq.heapreplace(heap, item)` | Pops smallest then pushes item (heap must be non-empty) | `heapq.heapreplace(li, 10)` |
| `heapq.nlargest(n, iterable)` | Returns `n` largest elements as a list | `heapq.nlargest(3, li)` |
| `heapq.nsmallest(n, iterable)` | Returns `n` smallest elements as a list | `heapq.nsmallest(4, li)` |
| `heapq.merge(*iterables)` | Merges multiple sorted iterables into one sorted iterator | `heapq.merge([1,3], [2,4])` |

---

## Max-Heap Trick

Python only supports min-heap. To simulate a **max-heap**, negate the values:

```python
li = [25, 20, 34]
max_heap = [-x for x in li]
heapq.heapify(max_heap)
print(-heapq.heappop(max_heap))  # → 34 (largest)
```

---

## heappushpop vs heapreplace

| | `heappushpop` | `heapreplace` |
|---|---|---|
| Push first, then pop? | Yes | No — pops first, then pushes |
| Works on empty heap? | Yes | No |
| Use when | item may be smallest | heap is guaranteed non-empty |

---

## When to Use Heap

| Use Case | Why |
|---|---|
| Priority queue | Always access the min/max in O(log n) |
| Dijkstra's / A* algorithm | Efficient shortest path |
| Top N elements | `nlargest` / `nsmallest` faster than full sort for small N |
| Dynamic sorted data | Avoid re-sorting after each insertion |
