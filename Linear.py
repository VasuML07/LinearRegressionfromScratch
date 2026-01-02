#inputs and outputs for linear resgression (actual)
x_data = [1, 2, 3, 4, 5]      
y_data = [10000, 8000, 6000, 4000, 2000] 
m = 0
c = 0
L = 0.01
epochs = 1800
n = len(x_data)
#cost function is defined as mse E =1/n * sum(yi - (mxi + c))**2
for i in range(epochs):
    #finding gradient descentss
    D_m = 0
    D_c = 0
    for j in range(n):
        x = x_data[j]
        y = y_data[j]
        y_pred = m*x+c
        D_m += (-2/n)*x*(y-y_pred)
        D_c += (-2/n)*(y-y_pred)
    #updating parameters
    m = m - L*D_m
    c = c - L*D_c
print(f"final slope is {m} and final intercept is {c}")
prediction = m*3+c
print(f"Prediction for input 3 is {prediction}")
