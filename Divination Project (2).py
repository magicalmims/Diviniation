#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Normal Distribution


# In[12]:


from numpy.random import seed
from numpy.random import normal

#make this example reproducible
seed(1)

#generate sample of 200 values that follow a normal distribution 
print ("Enter number of trials you wish to use")
size=int(input())
data = normal(loc=0, scale=1, size=size)

#view first six values
data[0:5]



# In[13]:


import numpy as np

#find mean of sample
np.mean(data)


#find standard deviation of sample
np.std(data, ddof=1)


# In[14]:


import matplotlib.pyplot as plt
count, bins, ignored = plt.hist(data, 30)
plt.show()


# In[9]:


#Binomial Distribution
print("Enter the number of trials you wish to use")
n=int(input())


print("Enter the probability of success")
p=float(input())


# In[10]:


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


# In[11]:


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


#Poisson Distribution

# importing library
  
from scipy.stats import poisson 
    
numargs = poisson .numargs 
print ("Enter the variables")
a=int(input())
b=int(input())

rv = poisson (a, b) 
    
print ("RV : \n", rv)  


# In[ ]:



import numpy as np 
quantile = np.arange (0.01, 1, 0.1) 
  
# Random Variates 
R = poisson .rvs(a, b, size = 10) 
print ("Random Variates : \n", R) 
  
# PDF 
x = np.linspace(poisson.ppf(0.01, a, b),
                poisson.ppf(0.99, a, b), 10)
R = poisson.ppf(x, 1, 3)
print ("\nProbability Distribution : \n", R) 


# In[ ]:


import numpy as np 
import matplotlib.pyplot as plt 
     
distribution = np.linspace(0, np.minimum(rv.dist.b, 2)) 
print("Distribution : \n", distribution) 
     
plot = plt.plot(distribution, rv.ppf(distribution)) 


# In[ ]:





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


# In[ ]:





# In[ ]:




