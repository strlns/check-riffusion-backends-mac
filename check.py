import torch
print("Checking cuda availability")
print(torch.cuda.is_available())

print("Checking mps availability")
print(torch.backends.mps.is_available())
