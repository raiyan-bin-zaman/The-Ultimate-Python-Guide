"""
ML Experiment Tracker
Learn: int, float, str, bool in one project
"""

# 1. Store hyperparameters (int, float, str, bool)
epochs = 10                     # int
learning_rate = 0.001           # float
optimizer = "Raiyan"            # str
use_gpu = True                  # bool

# 2. Track experiment info
experiment_name = "Image_Classifier_v1"
author = "Raiyan"
version = 1

print(f"|Running {experiment_name} by {author}, version {version}")
print(f"Optimizer: {optimizer}, LR={learning_rate}, GPU={use_gpu}")
print("-" * 40)

# 3. Simulate training loop (int + float)
accuracy = 0.50   # start float
loss = 1.0        # start float

for epoch in range(1, epochs + 1):   # int for loop
    # Fake training updates
    accuracy += 0.05
    loss -= 0.1

    # Boolean check
    is_good = accuracy > 0.8

    # Logging
    print(f"Epoch {epoch}/{epochs} | Acc: {accuracy:.2f} | Loss: {loss:.2f} | Good? {is_good}")

# 4. Final results
print("-" * 40)
summary = f"✅ Final Accuracy: {accuracy:.2f}, Final Loss: {loss:.2f}"
print(summary)
