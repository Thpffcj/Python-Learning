import torch
import torch.nn as nn
import torch.optim as optim
import pandas as pd
import numpy as np
class Completor(nn.Module):
    def __init__(self):
        super(Completor,self).__init__()
        self.ll = nn.Linear(1,100)
        self.ll2 = nn.Linear(100,1)
        self.relu = nn.ReLU()
    def forward(self, input):
        return self.ll2(self.relu(self.ll(input)))

def train(model:Completor,criterion,optimizer:optim.Adam):
    data = pd.read_csv("Data/datahub/global-temp-annual_csv.csv")
    land = np.array(data["Land"].values)
    target = torch.tensor(land,dtype=torch.float).unsqueeze_(dim=1)
    year = np.array(range(1880-1880,2015-1880))

    train_data = torch.tensor(year,dtype=torch.float).unsqueeze_(dim=1)
    print(train_data.shape)
    print(target.shape)
    lenght = len(train_data)
    print(lenght)
    for i in range(lenght):
        optimizer.zero_grad()
        input = train_data[i]
        print(input)
        logits = model(input)
        loss = criterion(logits,target[i])
        loss.backward()
        optimizer.step()
        print(loss)

def prediction(model):
    year = torch.tensor(range(2015-1880,2045-1880),dtype=torch.float).unsqueeze_(dim=1)
    lengths = len(year)
    for i in range(lengths):
        print(model(year[i]).item())

if __name__ == "__main__":
    model = Completor()
    optimizer = optim.Adam(model.parameters(),lr=0.001)
    criterion = nn.MSELoss()
    for epoch in range(40):
        train(model,criterion,optimizer)
    prediction(model)