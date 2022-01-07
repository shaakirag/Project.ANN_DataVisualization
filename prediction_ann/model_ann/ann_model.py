import torch
import torch.nn as nn

class ANN_Model(nn.Module):
    def __init__(self,input_features,hidden1,hidden2,out_features=2):
        super().__init__()
        # Creating dense connected layers
        self.f_connected1=nn.Linear(input_features,hidden1)
        self.f_connected2=nn.Linear(hidden1,hidden2)
        self.out=nn.Linear(hidden2,out_features)
    def forward(self,x):
        x=F.relu(self.f_connected1(x))
        x=F.relu(self.f_connected2(x))
        x=self.out(x)
        return x

def modeling(df):
    pass

# Spitting data into train and test
def df_split(df, label):
    # independent features
    X=df.drop(label,axis=1).values
    #dependent features
    y=df[label].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    return [X,y,X_train,X_test,y_train, y_test]

# Creating tensors
def create_tensor_input(array):
    return torch.FloatTensor(array)

def create_tensor_output(array):
    return torch.LongTensor(array)