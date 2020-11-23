from alpaca_client.alpaca_serving.client import *
from alpaca_server.alpaca_model.pytorchAPI import *
x_train, y_train = utils.load_data_and_labels('com.bio')#vlsp
sent = x_train[0:64]#300036
label = y_train[0:64]
print(len(x_train))

ac = AlpacaClient()
print("ac loaded")
ac.initiate(38)#25
print("ac init")
ac.online_learning(sent,label,epoch=20, batch=64)#1 500 34 10 35 100 32 -> 300000*100=30 trieu
print("learned")

