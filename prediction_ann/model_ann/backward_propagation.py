from all_libs import *
from prediction_ann import *

# Backward Propagation-- Define the loss_function,define the optimizer
# User input for learning rate (0.01) 0.01 is the recommended value
def back_prop(model, lr, epochs, X_train, y_train):
    loss_function = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(),lr=lr)

    final_losses = []
    results = []
    for i in range(epochs):
        i = i + 1
        y_pred = model.forward(X_train)
        loss = loss_function(y_pred,y_train)
        final_losses.append(loss)
        if i % 10 == 1:
            results.append([i,loss.item()])
            #print("Epoch number: {} and the loss : {}".format())
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    return [results, final_losses]

# Plot the loss function
def plot_loss(epochs, final_losses, x, y):
    plt.pyplot.plot(range(epochs), final_losses)
    plt.pyplot.ylabel(y)
    plt.pyplot.xlabel(x)
    plt.pyplot.show()