# queue.Queue Methods (Quick Reference)

| Function           | Why Use It                                           | Usage Example   |
| ------------------ | ---------------------------------------------------- | --------------- |
| `Queue(maxsize=0)` | Create a queue (FIFO). maxsize=0 means infinite size | `q = Queue()`   |
| `q.put(item)`      | Add an item to the queue                             | `q.put(10)`     |
| `q.get()`          | Remove and return first item (FIFO dequeue)          | `x = q.get()`   |
| `q.empty()`        | Check if queue has no items                          | `q.empty()`     |
| `q.full()`         | Check if queue reached max size                      | `q.full()`      |
| `q.qsize()`        | Get approximate number of items                      | `q.qsize()`     |
| `q.task_done()`    | Mark a retrieved task as completed                   | `q.task_done()` |
| `q.join()`         | Block until all tasks are processed                  | `q.join()`      |

---

# Quick Pattern Example

```python
from queue import Queue

q = Queue()

q.put(1)
q.put(2)

print(q.get())
print(q.qsize())
```
