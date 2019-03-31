# -*- coding: utf-8 -*-
from torch.utils.data.dataset import Dataset
import torch
from great_4 import Cnn_Model
from great_3 import NkDataSet

#train_test.py
def train(my_dataset_loader,model,criterion,optimizer,epoch):
    model.train()

    for i, data in enumerate(my_dataset_loader,0):
        # Forward pass: Compute predicted y by passing x to the model

        # fc 구조이기 때문에 일렬로 쫙피는 작업이 필요하다.
        images, label = data

        y_pred = model(images)

        #compute and print loss
        loss = criterion(y_pred,label)

        print(epoch, loss.item())

        # Zero gradients, perform a backward pass, and update the weights.
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

def test(my_dataset_loader, model, criterion, epoch):
    model.eval()
    for i, data in enumerate(my_dataset_loader,0):
        # Forward pass: Compute predicted y by passing x to the model
        # fc 구조이기 떄문에 일렬로 쫙피는 작업이 필요하다.

        images, label = data
        # 그냥 images를 하면 에러가 난다. 데이터 shape이 일치하지 않아서
        y_pred = model(images)
        # Compute and print loss
        loss = criterion(y_pred,label)

        print(epoch,loss.item())

#Data Load

csv_path = './test.csv'
custom_dataset = NkDataSet(csv_path)

my_dataset_loader = torch.utils.data.DataLoader(dataset=custom_dataset,
                                                batch_size=2,
                                                shuffle=False,
                                                num_workers=1)

#test set 만들기
#test data set 만들어 줘야 한다.
#Model Load
#input,hiddn,output size

model = Cnn_Model()

#CrossEntropyLoss 를 사용
criterion = torch.nn.CrossEntropyLoss(reduction='sum')
optimizer = torch.optim.SGD(model.parameters(), lr=1e-4)

for epoch in range(500):
    print("epoch",epoch)

    train(my_dataset_loader,model,criterion,optimizer,epoch)
    test(my_dataset_loader,model,criterion,epoch)


