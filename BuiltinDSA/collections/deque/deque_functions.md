# Python `collections.deque` Functions

  --------------------------------------------------------------------------
  Function Name            Example                   Explanation
  ------------------------ ------------------------- -----------------------
  `deque(iterable)`        `dq = deque([1,2,3])`     Create a deque from an
                                                     iterable.

  `append(x)`              `dq.append(4)`            Add an element to the
                                                     right end.

  `appendleft(x)`          `dq.appendleft(0)`        Add an element to the
                                                     left end.

  `pop()`                  `dq.pop()`                Remove and return the
                                                     rightmost element.

  `popleft()`              `dq.popleft()`            Remove and return the
                                                     leftmost element.

  `extend(iterable)`       `dq.extend([4,5])`        Add multiple elements
                                                     to the right end.

  `extendleft(iterable)`   `dq.extendleft([0,-1])`   Add multiple elements
                                                     to the left end (in
                                                     reverse order).

  `clear()`                `dq.clear()`              Remove all elements
                                                     from the deque.

  `copy()`                 `new_dq = dq.copy()`      Return a shallow copy
                                                     of the deque.

  `count(x)`               `dq.count(2)`             Count occurrences of a
                                                     value.

  `index(x)`               `dq.index(2)`             Return the index of the
                                                     first occurrence.

  `insert(i, x)`           `dq.insert(1, 99)`        Insert an element at a
                                                     specific position.

  `remove(x)`              `dq.remove(2)`            Remove the first
                                                     occurrence of a value.

  `reverse()`              `dq.reverse()`            Reverse the elements in
                                                     place.

  `rotate(n)`              `dq.rotate(2)`            Rotate right by `n`
                                                     steps.

  `rotate(-n)`             `dq.rotate(-2)`           Rotate left by `n`
                                                     steps.

  `maxlen`                 `dq.maxlen`               Return the maximum size
                                                     of the deque.

  `len(dq)`                `len(dq)`                 Return the number of
                                                     elements.

  `in`                     `2 in dq`                 Check membership in the
                                                     deque.

  Iteration                `for x in dq:`            Iterate through
                                                     elements.

  Indexing                 `dq[0]`                   Access an element by
                                                     index.

  Assignment               `dq[0] = 10`              Modify an element by
                                                     index.

  Deletion                 `del dq[0]`               Delete an element by
                                                     index.
  --------------------------------------------------------------------------

## Example

``` python
from collections import deque

dq = deque([1, 2, 3])

dq.append(4)
dq.appendleft(0)
dq.pop()
dq.popleft()

print(dq)
```
