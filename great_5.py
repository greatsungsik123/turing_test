from torch.utils.data.dataset import Dataset
import torch
from great_4 import Cnn_Model
from great_3 import NkDataSet

csv_path = "test.csv"

custom_dataset = NkDataSet(csv_path)

my_dataset_loader = torch.utils.data.DataLoader(dataset=custom_dataset,
                                                batch_size=2,
                                                shuffle=False,
                                                num_workers=2)
model = Cnn_Model()

criterion = torch.nn.CrossEntropyLoss(reduction="sum")
optimizer = torch.optim.SGD(model.parameters(),lr=1e-4)

for t in range(500):
    for i,data in enumerate(my_dataset_loader,0):
        images,label = data
        y_pred = model(images)

        print(y_pred)
        print(label)

        loss = criterion(y_pred,label.long())

        print(t,loss.item())

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()