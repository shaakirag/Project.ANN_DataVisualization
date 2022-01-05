import torch

def prediction(model, new_data):
    new_data = torch.tensor(new_data)
    return model(new_data).argmax().item()