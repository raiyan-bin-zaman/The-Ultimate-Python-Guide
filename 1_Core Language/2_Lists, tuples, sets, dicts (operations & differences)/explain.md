# 🔹 Python Collections: Lists, Tuples, Sets, Dicts

## 1. **Lists**

-   **Ordered, mutable, allows duplicates**\
-   Best when: sequence of items may change (e.g., dataset rows,
    predictions).

``` python
nums = [1, 2, 2, 3]
nums.append(4)        # [1,2,2,3,4]
nums.remove(2)        # [1,2,3,4] (removes first 2)
nums[0] = 10          # [10,2,3,4]
```

✅ Use case in ML: storing feature vectors, predictions.

------------------------------------------------------------------------

## 2. **Tuples**

-   **Ordered, immutable, allows duplicates**\
-   Best when: data should not change (e.g., feature dimensions, fixed
    configs).

``` python
point = (2, 3)
x, y = point          # unpacking
```

✅ Safer than lists when you want **read-only data**.

------------------------------------------------------------------------

## 3. **Sets**

-   **Unordered, mutable, no duplicates**\
-   Best when: uniqueness matters (e.g., unique labels, vocab words).

``` python
labels = {1, 2, 2, 3}   # {1,2,3}
labels.add(4)           # {1,2,3,4}
labels.remove(1)        # {2,3,4}
```

🔹 Useful operations:

``` python
a = {1,2,3}; b = {3,4}
a | b   # union {1,2,3,4}
a & b   # intersection {3}
a - b   # difference {1,2}
```

✅ Great for **checking membership quickly**.

------------------------------------------------------------------------

## 4. **Dicts**

-   **Key-value pairs, unordered (Python 3.7+ preserves insertion
    order)**\
-   Best when: mapping between things (e.g., word → index, label →
    probability).

``` python
student = {"name":"Alice", "score":95}
student["score"]        # 95
student["age"] = 20     # add new key
for k,v in student.items():
    print(k,v)
```

✅ Core in ML: dataset mappings, model configs, JSON parsing.

------------------------------------------------------------------------

# 🔑 Quick Comparison
| Type  | Ordered | Mutable | Duplicates | Use Case                   |
| ----- | ------- | ------- | ---------- | -------------------------- |
| List  | ✅       | ✅       | ✅          | Sequences, predictions     |
| Tuple | ✅       | ❌       | ✅          | Fixed configs, coordinates |
| Set   | ❌       | ✅       | ❌          | Unique labels, vocab       |
| Dict  | ✅(3.7+) | ✅       | Keys: ❌    | Feature → value mappings   |


👉 Tip for ML/AI:\
- Use **lists** for batches, predictions.\
- Use **tuples** for fixed structures.\
- Use **sets** for unique labels or vocab.\
- Use **dicts** for mapping IDs, labels, configs.
