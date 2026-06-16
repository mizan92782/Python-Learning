from collections import Counter

| Function / Operation | Why it is used |
|---------------------|----------------|
| `Counter(iterable)` | Create frequency count from an iterable |
| `update(iterable)`  | Add new elements and update counts |
| `elements()`        | Return all elements expanded by their count |
| `most_common(n)`    | Get top n most frequent elements |
| `ctr[key] += n`     | Manually increase count of a key |
| `ctr[key] -= n`     | Manually decrease count of a key |
| `subtract(iterable)`| Subtract counts using another iterable or Counter |
| `ctr1 + ctr2`       | Add two Counters (merge frequencies) |
| `ctr1 - ctr2`       | Subtract counts (keep only positive results) |
| `ctr1 & ctr2`       | Intersection (minimum counts of common elements) |
| `ctr1 | ctr2`       | Union (maximum counts of each element) |
