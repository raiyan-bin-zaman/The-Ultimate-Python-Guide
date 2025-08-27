# 🔹 Python Core: Variables & Data Types (For ML/AI)

## 1. Variables

-   Think of a variable as a "box" that stores data.
-   You don't declare type (Python is *dynamically typed*).

``` python
x = 10        # int
y = 3.14      # float
name = "Raiyan"  # str
is_ai = True  # bool
```

✅ Best practice: - Use **snake_case** → `my_variable` - Keep names
**meaningful** → `learning_rate = 0.01`

------------------------------------------------------------------------

## 2. Data Types You MUST Master

### (a) Integers (`int`)

Whole numbers, positive/negative

``` python
epochs = 100   # training iterations
```

### (b) Floats (`float`)

Decimal numbers (very common in ML for weights, losses, probabilities)

``` python
learning_rate = 0.001
accuracy = 0.945
```

### (c) Strings (`str`)

Text data (useful for labels, NLP tasks)

``` python
model_name = "ResNet50"
greeting = f"Hello, {name}!"
```

💡 f-strings = best way to format.

### (d) Booleans (`bool`)

`True` or `False` (used in conditions, logic, filtering)

``` python
use_gpu = True
is_overfitting = False
```

------------------------------------------------------------------------

## 3. Quick Type Check

``` python
type(epochs)       # <class 'int'>
type(learning_rate) # <class 'float'>
```

------------------------------------------------------------------------

## 4. Type Casting (super important in ML)

Sometimes you need to **convert** types (e.g., dataset input).

``` python
int(3.9)     # 3
float(10)    # 10.0
str(42)      # "42"
bool(0)      # False
```

------------------------------------------------------------------------

## 5. Tiny Practice (ML-flavored 🧠)

``` python
# Store hyperparameters
epochs = 50
learning_rate = 0.01
optimizer = "Adam"
early_stop = True

print(f"Training {epochs} epochs with {optimizer} at lr={learning_rate}")
```

------------------------------------------------------------------------

🔥 **Mindset Tip:**\
Always connect variables & types with ML concepts (epochs, lr, accuracy,
labels, predictions). This way you'll *naturally reinforce* them.