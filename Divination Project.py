#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Binomial Distribution
print("Enter the number of trials you wish to use")
n=int(input())


print("Enter the probability of success")
p=float(input())


# In[ ]:


#Simulation
from scipy.stats import binom


# defining the list of r values
r_values = list(range(n + 1))
# obtaining the mean and variance 
mean, var = binom.stats(n, p)
# list of pmf values
dist = [binom.pmf(r, n, p) for r in r_values ]
# printing the table
print("r\tp(r)")
for i in range(n + 1):
    print(str(r_values[i]) + "\t" + str(dist[i]))
# printing mean and variance
print("mean = "+str(mean))
print("variance = "+str(var))


# In[ ]:


#Graphing the Output
from scipy.stats import binom
import matplotlib.pyplot as plt
# setting the values
# of n and p

# defining list of r values
r_values = list(range(n + 1))
# list of pmf values
dist = [binom.pmf(r, n, p) for r in r_values ]
# plotting the graph 
plt.bar(r_values, dist)
plt.show()


# In[ ]:


#Traingular Distribution


# importing library
  
from scipy.stats import triang 
    
numargs = triang .numargs 
print ("Enter the average")
a=int(input())

rv = triang (a) 
    
print ("RV : \n", rv)  


# In[ ]:


# importing library
import numpy as np 
quantile = np.arange (0.01, 1, 0.1) 
  
# Random Variates 

R = triang .rvs(0.158, size = 10) 
print ("Random Variates : \n", R) 
  
# PDF 
x = np.linspace(0, 5, 10) 
R = triang.pdf(x, 1)
print ("\nProbability Distribution : \n", R) 


# In[ ]:


#Graphing the Triangular Distribution
import numpy as np 
import matplotlib.pyplot as plt 
     
distribution = np.linspace(0, np.minimum(rv.dist.b, 3)) 
print("Distribution : \n", distribution) 
     
plot = plt.plot(distribution, rv.pdf(distribution)) 

