import matplotlib.pyplot as plt
import random
def desired_val(x_min,x_max):
    return random.randint(x_min,x_max)

def generate_plot(x_min,x_max):
    arr=[desired_val(x_min,x_max) for _ in range(20)]
   
    m=(x_max-x_min)
   
    y=[]
    for i in arr:
        val=((m*i)+x_min)
       
        y.append(val)


  
    plt.plot(y,arr)
    plt.ylabel('some numbers')
    plt.show()

    
x_min=int(input("Enter minimum val "))
x_max=int(input("Enter maximum val "))
generate_plot(x_min,x_max)