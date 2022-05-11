import numpy as np
import matplotlib.pyplot as plt 

x = np.array([1,2,3,4])
y = np.array([6,9,2,5])

def interpol(y,x,k=0, res=[],aux=[]):
    for i in range(len(y)-1):
        aux = []
        for j in range(len(y)-1):
            r = ((y[j+1]-y[j])/(x[j+k+1]-x[j]))
            aux.append(r)
        y = aux.copy()
        k+=1
        res.append(y[0])
        del aux
    return res

def pred(res,pred,resp,prediction=[],aux=1):
    for j in range(len(res)):
        aux *= (pred-x[j])
        resp +=  aux*res[j]
    return resp
def interation(array,s,y,prediction = []):
    for i in array:
        prediction.append(pred(res=s, pred=i, resp=y[0]))
    return prediction
        
s = interpol(y, x)
pred_n = np.array(interation(x,s,y))
pred_2 = np.array(interation([5,6,7,8], s, y))

# Sort values: 

pred_n = np.sort(pred_n)
x = np.sort(x)
y = np.sort(y)
 
 # Graf
 
plt.scatter(x, y, label='Value')
plt.plot(x,pred_n, color='red',label='Prediction')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid()
plt.savefig(fname='Figure_1')
plt.show()

