import sys
import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor
import time


import matplotlib.pyplot as plt


if "--check" in sys.argv:
    if torch.cuda.is_available():
        print(f"CUDA {torch.version.cuda} @ {torch.cuda.get_device_name(0)}\n",
              f"Capability: {torch.cuda.get_device_capability()}" )
    else:
        print("CPU only")
    exit()


BATCH_SIZE = 4 # each element in dataloader return BATCH_SIZE features(images?) and labels

# download datasets and create dataloader
training_data = datasets.FashionMNIST(
    root="data",
    train=True,
    download=True,
    transform=ToTensor(),
)
train_dataloader = DataLoader(training_data, batch_size=BATCH_SIZE)

test_data = datasets.FashionMNIST(
    root="data",
    train=False,
    download=True,
    transform=ToTensor(),
)
test_dataloader = DataLoader(test_data, batch_size=BATCH_SIZE)





for X, y in test_dataloader:
    print(f"Shape of X [N, C, H, W]: {X.shape}")
    print(f"Shape of y: {y.shape} {y.dtype}")
    break

device = ("cpu")


n_feat_l1 = 512
n_feat_l2 = 512

class NeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.flatten = nn.Flatten() # 2D -> 1D
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(28*28, n_feat_l1),
            nn.ReLU(),
            nn.Linear(n_feat_l1, n_feat_l2),
            nn.ReLU(),
            nn.Linear(n_feat_l2, 10)
        )

    def forward(self, x):
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits

model = NeuralNetwork().to(device)
print(model)

loss_fn = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=1e-3)

def train(dataloader, model, loss_fn, optimizer):
    size = len(dataloader.dataset)
    model.train()
    for batch, (X, y) in enumerate(dataloader):
        X, y = X.to(device), y.to(device)

        # prediction error
        pred = model(X)
        loss = loss_fn(pred, y)

        # backpropagate
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()

        if batch % 100 == 0:
            loss, current = loss.item(), (batch + 1) * len(X)
            # print(f"loss: {loss:>7f} [{current:>5d}/{size:>5d}]")


def test(dataloader, model, loss_fn):
    size = len(dataloader.dataset)
    num_batches = len(dataloader)
    model.eval()
    test_loss, correct = 0, 0
    with torch.no_grad():
        for X, y in dataloader:
            X, y = X.to(device), y.to(device)
            pred = model(X)
            test_loss += loss_fn(pred, y).item()
            correct += (pred.argmax(1) == y).type(torch.float).sum().item()
    test_loss /= num_batches
    correct /= size
    # print(f"accuracy: {(100*correct):>0.1f}%, avg loss: {test_loss:>8f}")
    return (100*correct), test_loss




# TRAIN
epochs = 1
test_res = [f"l1 features: {n_feat_l1}\n", 
            f"l2 features: {n_feat_l2}\n", 
            f"epochs: {epochs}\n",
            f"device: {device}\n"]
if "--train" in sys.argv:
    for t in range(epochs):
        print(f"epoch {t+1}")
        start = time.time()
        train(train_dataloader, model, loss_fn, optimizer)
        end = time.time()
        acc, lss = test(test_dataloader, model, loss_fn)
        test_res.append(f"acc: {acc:.2f}, lss: {lss:.2f}, time: {(end-start):.3f}\n")
        print(test_res[-1])
    print("DONE")
    torch.save(model.state_dict(), "model.pth")

    with open('test_restults', 'a') as tr:
        test_res.append("\n-------\n")
        for i in test_res:
            tr.writelines(i)

# LOADING MODEL
if "--load" in sys.argv:
    model = NeuralNetwork().to(device)
    model.load_state_dict(torch.load("model.pth"))

classes = [
    "T-shirt/top",
    "Trouser",
    "Pullover",
    "Dress",
    "Coat",
    "Sandal",
    "Shirt",
    "Sneaker",
    "Bag",
    "Ankle boot",
]


image, label = training_data[0]  # Get the first image and label
plt.imshow(image.permute(1, 2, 0))  # Permute the axes to fit the format expected by matplotlib
plt.title(f"Label: {classes[label]}")
plt.savefig(f'img.png')

model.eval()
x, y = test_data[10][0], test_data[10][1]
with torch.no_grad():
    x = x.to(device)
    pred = model(x)
    predicted, actual = classes[pred[0].argmax(0)], classes[y]
    print(f'Predicted: "{predicted}", Actual: "{actual}"')

# ok
