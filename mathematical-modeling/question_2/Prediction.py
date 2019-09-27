import torch
import torch.nn as nn
import torch.optim as optim
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def weights_init(m):
    classname = m.__class__.__name__
    if classname.find("Linear")!=-1:
        torch.nn.init.xavier_normal_(m.weight.data)

class Predictor(nn.Module):
    def __init__(self):
        super(Predictor,self).__init__()
        self.ll = nn.Linear(5,100)
        self.out = nn.Linear(100,1)
        self.relu = nn.ReLU()

    def forward(self, input):
        return self.out(self.relu(self.ll(input)))

def load_data(train_file,target_file):
    train_df = pd.read_csv(train_file)
    target_df = pd.read_csv(target_file)
    #Year,Land,Land and Ocean,N Hem,S Hem
    train_df = train_df[["Year","Land","Land and Ocean","N Hem","S Hem"]]
    train_df["Year"] = pd.to_datetime(train_df["Year"]).dt.year #将时间转为年
    target_df = target_df[["Year","Mean"]]
    target_df = target_df.groupby("Year").mean()
    target_df = target_df.reset_index()
    target_df["Year"]-=1880
    train_df["Year"]-=1880
    train_df.sort_values(by="Year", ascending=False)
    target_df.sort_values(by="Year",ascending=False)
    print(train_df)
    print(target_df)
    train_data = np.array(train_df.values)
    target_data = np.array(target_df["Mean"].values)
    train_data = torch.tensor(train_data,dtype=torch.float)
    target_data = torch.tensor(target_data[:-2],dtype=torch.float)
    return train_data,target_data

def train(model,train_data,target_data,criterion,optimizer:optim.Adam):
    optimizer.zero_grad()
    logits = model(train_data)
    loss = criterion(logits,target_data)
    loss.backward()
    optimizer.step()
    return loss
def train_iters(model,train_set,target_set,epoches=100,print_every=10,lr=0.01):
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(),lr=lr)
    #拆分训练和测试数据
    test_input = train_set[-10:]
    test_target = target_set[-10:]
    train_set = train_set[:-10]
    target_set = target_set[:-10]
    lenghts = len(train_set)
    total_loss = []
    loss = 0
    current_iters = 0

    for epoch in range(epoches):
        for i in range(lenghts):
            train_data = train_set[i]
            target_data = target_set[i]
            loss += train(model,train_data,target_data,criterion,optimizer)

            if current_iters % print_every == 0:
                print("loss:",loss/print_every)
                total_loss.append(loss/print_every)
                loss = 0
            current_iters += 1
    #预测
    print("------now we begin predicting:------")
    for i in range(10):
        input = test_input[i]
        label = test_target[i]
        logits = model(input)
        print("label: ",label.item(),"logits: ",logits.item())
    print(lenghts)
    x = np.arange(1,epoches*lenghts,print_every)
    print(len(x))
    print(len(total_loss))
    plt.plot(x, total_loss)
    plt.show()


if __name__ == "__main__":
    model = Predictor()
    model.apply(weights_init)
    train_data,target_data = load_data("Data/datahub/global-temp-annual_csv.csv","Data/datahub/annual_csv.csv")
    print(train_data)
    print(target_data)
    train_iters(model,train_data,target_data)

# tmp = pd.read_csv("Data/datahub/global-temp-annual_csv.csv")
# print(pd.to_datetime(tmp["Year"]).dt.year)