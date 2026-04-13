import os
import json
import torch
import torch.nn as nn

DATA_DIR = "data/processed"
MODEL_PATH = "model.pt"
PREDICTIONS_PATH = "predictions.json"

test_images, test_labels = torch.load(os.path.join(DATA_DIR, "test.pt"))

class SimpleCNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = nn.Conv2d(1, 8, kernel_size=3)
        self.pool = nn.MaxPool2d(2)
        self.fc = nn.Linear(8 * 13 * 13, 10)

    def forward(self, x):
        x = self.pool(torch.relu(self.conv(x)))
        x = x.view(x.size(0), -1)
        x = self.fc(x)
        return x

model = SimpleCNN()
model.load_state_dict(torch.load(MODEL_PATH, map_location=torch.device("cpu")))
model.eval()

with torch.no_grad():
    outputs = model(test_images)
    predictions = torch.argmax(outputs, dim=1)

results = []
for i in range(len(predictions)):
    results.append({
        "index": int(i),
        "true_label": int(test_labels[i]),
        "predicted_label": int(predictions[i])
    })

with open(PREDICTIONS_PATH, "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2)

print(f"Predictions saved to {PREDICTIONS_PATH}")