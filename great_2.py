from torch.utils.data.dataset import Dataset
import torch
from let_4 import NkDataSet
from let_2 import NkModel

#Data Load
csv_path = "./test.csv"

custom_dataset = NkDataSet(csv_path)

my_dataset_loader = torch.utils.data.DataLoader(dataset=custom_dataset,
                                                batch_size=1,
                                                shuffle=False,
                                                num_workers=1)
#model load
#input.hidden.output size

D_in = 30000#(100 * 100 * 3)
H = 1000
D_out = 2

model = NkModel(D_in,H,D_out)

#CrossEntronyLoss 를 사용
criterion = torch.nn.CrossEntropyLoss(reduction="sum")
optimizer = torch.optim.SGD(model.parameters(),lr=1e-4)#1/10000

for epoch in range(500):
    for i,data in enumerate(my_dataset_loader,0):
        # Forward pass: Compute predicted y by passing x to the model
        #fc 구조 이기 떄문에 일렬로 쫙피는 작업이 필요하다.
        images,label = data

        #그냥 이미지를 하면 에러가 난다. 데이터 shape이 일치하지 않아서
        #100 , 100 , 3
        images = images.view(1,30000)
        print(images.size())
        print("label is label",label)
        y_pred = model(images)
        print(y_pred.size())
        print(label.size())
        #compute and print loss
        loss = criterion(y_pred,label)
        print(epoch,loss.item())
        # zero gradients,perform a backward pass, and update the weights.
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()