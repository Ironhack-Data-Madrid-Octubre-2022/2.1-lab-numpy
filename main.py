
#1. Import the NUMPY package under the name np.
​
In [50]:

 pip install numpy
Requirement already satisfied: numpy in ./opt/anaconda3/envs/clase/lib/python3.7/site-packages (1.21.6)
Note: you may need to restart the kernel to use updated packages.
In [51]:

import numpy as np
In [52]:

#2. Print the NUMPY version and the configuration.
In [53]:

print (np)
<module 'numpy' from '/Users/juliasabatel/opt/anaconda3/envs/clase/lib/python3.7/site-packages/numpy/__init__.py'>
In [54]:

#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?
​
​
In [55]:

a=np.random.random((2,3,5))
a
Out[55]:
array([[[0.09805094, 0.33452595, 0.89556609, 0.15946618, 0.566006  ],
        [0.46438521, 0.56460118, 0.64698772, 0.34594894, 0.85119773],
        [0.99192679, 0.8592228 , 0.38152472, 0.0102846 , 0.59499676]],

       [[0.5343884 , 0.9150317 , 0.64921451, 0.03092255, 0.1195699 ],
        [0.58614263, 0.7621857 , 0.20996442, 0.23287925, 0.30275722],
        [0.53391071, 0.34608085, 0.71750088, 0.32920375, 0.45728385]]])
In [56]:

#4. Print a.
In [57]:

print(a)
[[[0.09805094 0.33452595 0.89556609 0.15946618 0.566006  ]
  [0.46438521 0.56460118 0.64698772 0.34594894 0.85119773]
  [0.99192679 0.8592228  0.38152472 0.0102846  0.59499676]]

 [[0.5343884  0.9150317  0.64921451 0.03092255 0.1195699 ]
  [0.58614263 0.7621857  0.20996442 0.23287925 0.30275722]
  [0.53391071 0.34608085 0.71750088 0.32920375 0.45728385]]]
In [58]:

#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"
​
​
In [59]:

b=np.random.random((5,2,3))
b
Out[59]:
array([[[0.00221699, 0.48975945, 0.30052191],
        [0.91538232, 0.95625603, 0.04993202]],

       [[0.36041228, 0.71160583, 0.2482526 ],
        [0.21779437, 0.83578473, 0.97587637]],

       [[0.43708648, 0.55380346, 0.14498033],
        [0.28145831, 0.31308049, 0.12152859]],

       [[0.30876579, 0.95629261, 0.56206939],
        [0.69175317, 0.93081765, 0.42652305]],

       [[0.23413649, 0.98182547, 0.75213045],
        [0.84522089, 0.41605695, 0.6029215 ]]])
In [60]:

b=np.ones((5,2,3))
In [61]:

#6. Print b.
​
​
In [62]:

print(b)
[[[1. 1. 1.]
  [1. 1. 1.]]

 [[1. 1. 1.]
  [1. 1. 1.]]

 [[1. 1. 1.]
  [1. 1. 1.]]

 [[1. 1. 1.]
  [1. 1. 1.]]

 [[1. 1. 1.]
  [1. 1. 1.]]]
In [63]:

#7. Do a and b have the same size? How do you prove that in Python code?
In [67]:

np.size(a) == np.size(b)
Out[67]:
True
In [68]:

#8. Are you able to add a and b? Why or why not?
In [78]:

np.add(a,b)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
/var/folders/41/xnksc3m541lchdrncpcngj8r0000gn/T/ipykernel_35335/116260056.py in <module>
----> 1 np.add(a,b)

ValueError: operands could not be broadcast together with shapes (2,3,5) (5,2,3) 

In [71]:

a + b
print('shape a:', a.shape, '//', 'shape b:', b.shape)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
/var/folders/41/xnksc3m541lchdrncpcngj8r0000gn/T/ipykernel_35335/2781038548.py in <module>
----> 1 a + b
      2 print('shape a:', a.shape, '//', 'shape b:', b.shape)

ValueError: operands could not be broadcast together with shapes (2,3,5) (5,2,3) 

In [72]:

#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".
In [73]:

c = np.reshape(b,(2,3,5))
In [74]:

c
Out[74]:
array([[[1., 1., 1., 1., 1.],
        [1., 1., 1., 1., 1.],
        [1., 1., 1., 1., 1.]],

       [[1., 1., 1., 1., 1.],
        [1., 1., 1., 1., 1.],
        [1., 1., 1., 1., 1.]]])
In [75]:

#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?
In [76]:

 d = a + c
print(d)
[[[1.09805094 1.33452595 1.89556609 1.15946618 1.566006  ]
  [1.46438521 1.56460118 1.64698772 1.34594894 1.85119773]
  [1.99192679 1.8592228  1.38152472 1.0102846  1.59499676]]

 [[1.5343884  1.9150317  1.64921451 1.03092255 1.1195699 ]
  [1.58614263 1.7621857  1.20996442 1.23287925 1.30275722]
  [1.53391071 1.34608085 1.71750088 1.32920375 1.45728385]]]
In [44]:

#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.
In [79]:

print(a)
print(d)
​
#La diferencia es porque a la matriz d se le ha sumado el valor 1
[[[0.09805094 0.33452595 0.89556609 0.15946618 0.566006  ]
  [0.46438521 0.56460118 0.64698772 0.34594894 0.85119773]
  [0.99192679 0.8592228  0.38152472 0.0102846  0.59499676]]

 [[0.5343884  0.9150317  0.64921451 0.03092255 0.1195699 ]
  [0.58614263 0.7621857  0.20996442 0.23287925 0.30275722]
  [0.53391071 0.34608085 0.71750088 0.32920375 0.45728385]]]
[[[1.09805094 1.33452595 1.89556609 1.15946618 1.566006  ]
  [1.46438521 1.56460118 1.64698772 1.34594894 1.85119773]
  [1.99192679 1.8592228  1.38152472 1.0102846  1.59499676]]

 [[1.5343884  1.9150317  1.64921451 1.03092255 1.1195699 ]
  [1.58614263 1.7621857  1.20996442 1.23287925 1.30275722]
  [1.53391071 1.34608085 1.71750088 1.32920375 1.45728385]]]
In [80]:

#12. Multiply a and c. Assign the result to e.
In [81]:

e = a*c
In [82]:

e
Out[82]:
array([[[0.09805094, 0.33452595, 0.89556609, 0.15946618, 0.566006  ],
        [0.46438521, 0.56460118, 0.64698772, 0.34594894, 0.85119773],
        [0.99192679, 0.8592228 , 0.38152472, 0.0102846 , 0.59499676]],

       [[0.5343884 , 0.9150317 , 0.64921451, 0.03092255, 0.1195699 ],
        [0.58614263, 0.7621857 , 0.20996442, 0.23287925, 0.30275722],
        [0.53391071, 0.34608085, 0.71750088, 0.32920375, 0.45728385]]])
In [83]:

​
#13. Does e equal to a? Why or why not?
In [85]:

e == a #si es igual
Out[85]:
array([[[ True,  True,  True,  True,  True],
        [ True,  True,  True,  True,  True],
        [ True,  True,  True,  True,  True]],

       [[ True,  True,  True,  True,  True],
        [ True,  True,  True,  True,  True],
        [ True,  True,  True,  True,  True]]])
In [86]:

np.size(e) == np.size(a)
Out[86]:
True
In [89]:

np.array_equal(a,e)
Out[89]:
True
In [87]:

#si es igual porque no se alteran los números
In [88]:

#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"
In [92]:

d_max = d.max()
d_min = d.min()
d_mean = d.mean()
​
print( d_max, d_min, d_mean)
​
1.9919267915410868 1.0102846031809969 1.483057597701119
In [93]:

#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.
In [94]:

f = np.empty((2,3,5))
f
Out[94]:
array([[[0.09805094, 0.33452595, 0.89556609, 0.15946618, 0.566006  ],
        [0.46438521, 0.56460118, 0.64698772, 0.34594894, 0.85119773],
        [0.99192679, 0.8592228 , 0.38152472, 0.0102846 , 0.59499676]],

       [[0.5343884 , 0.9150317 , 0.64921451, 0.03092255, 0.1195699 ],
        [0.58614263, 0.7621857 , 0.20996442, 0.23287925, 0.30275722],
        [0.53391071, 0.34608085, 0.71750088, 0.32920375, 0.45728385]]])
In [99]:

"""
​
16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.
    
​
"""
Out[99]:
"\n\n16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.\nIf a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.\nIf a value equals to d_mean, assign 50 to the corresponding value in f.\nAssign 0 to the corresponding value(s) in f for d_min in d.\nAssign 100 to the corresponding value(s) in f for d_max in d.\nIn the end, f should have only the following values: 0, 25, 50, 75, and 100.\nNote: you don't have to use Numpy in this question.\n    \n\n"
In [129]:

f = np.where((d>d_min)&(d<d_mean),
             25, 
             np.where(d== d_mean,
                      50,
                      np.where(d==d_min,
                        0,
                         np.where(d== d_max, 100,75))))
f
Out[129]:
array([[[ 25,  25,  75,  25,  75],
        [ 25,  75,  75,  25,  75],
        [100,  75,  25,   0,  75]],

       [[ 75,  75,  75,  25,  25],
        [ 75,  75,  25,  25,  25],
        [ 75,  25,  75,  25,  25]]])
In [117]:

"""
#17. Print d and f. Do you have your expected f?
For instance, if your d is:
array([[[1.85836099, 1.67064465, 1.62576044, 1.40243961, 1.88454931],
        [1.75354326, 1.69403643, 1.36729252, 1.61415071, 1.12104981],
        [1.72201435, 1.1862918 , 1.87078449, 1.7726778 , 1.88180042]],
​
       [[1.44747908, 1.31673383, 1.02000951, 1.52218947, 1.97066381],
        [1.79129243, 1.74983003, 1.96028037, 1.85166831, 1.65450881],
        [1.18068344, 1.9587381 , 1.00656599, 1.93402165, 1.73514584]]])
​
Your f should be:
array([[[ 75.,  75.,  75.,  25.,  75.],
        [ 75.,  75.,  25.,  25.,  25.],
        [ 75.,  25.,  75.,  75.,  75.]],
​
       [[ 25.,  25.,  25.,  25., 100.],
        [ 75.,  75.,  75.,  75.,  75.],
        [ 25.,  75.,   0.,  75.,  75.]]])
"""
​
​
Out[117]:
'\n#17. Print d and f. Do you have your expected f?\nFor instance, if your d is:\narray([[[1.85836099, 1.67064465, 1.62576044, 1.40243961, 1.88454931],\n        [1.75354326, 1.69403643, 1.36729252, 1.61415071, 1.12104981],\n        [1.72201435, 1.1862918 , 1.87078449, 1.7726778 , 1.88180042]],\n\n       [[1.44747908, 1.31673383, 1.02000951, 1.52218947, 1.97066381],\n        [1.79129243, 1.74983003, 1.96028037, 1.85166831, 1.65450881],\n        [1.18068344, 1.9587381 , 1.00656599, 1.93402165, 1.73514584]]])\n\nYour f should be:\narray([[[ 75.,  75.,  75.,  25.,  75.],\n        [ 75.,  75.,  25.,  25.,  25.],\n        [ 75.,  25.,  75.,  75.,  75.]],\n\n       [[ 25.,  25.,  25.,  25., 100.],\n        [ 75.,  75.,  75.,  75.,  75.],\n        [ 25.,  75.,   0.,  75.,  75.]]])\n'
In [130]:

print(d)
print(f)
​
[[[1.09805094 1.33452595 1.89556609 1.15946618 1.566006  ]
  [1.46438521 1.56460118 1.64698772 1.34594894 1.85119773]
  [1.99192679 1.8592228  1.38152472 1.0102846  1.59499676]]

 [[1.5343884  1.9150317  1.64921451 1.03092255 1.1195699 ]
  [1.58614263 1.7621857  1.20996442 1.23287925 1.30275722]
  [1.53391071 1.34608085 1.71750088 1.32920375 1.45728385]]]
[[[ 25  25  75  25  75]
  [ 25  75  75  25  75]
  [100  75  25   0  75]]

 [[ 75  75  75  25  25]
  [ 75  75  25  25  25]
  [ 75  25  75  25  25]]]
"""
#18. Bonus question: instead of using numbers (i.e. 0, 25, 50, 75, and 100), how to use string values 
("A", "B", "C", "D", and "E") to label the array elements? You are expecting the result to be:
array([[[ 'D',  'D',  'D',  'B',  'D'],
        [ 'D',  'D',  'B',  'B',  'B'],
        [ 'D',  'B',  'D',  'D',  'D']],

       [[ 'B',  'B',  'B',  'B',  'E'],
        [ 'D',  'D',  'D',  'D',  'D'],
        [ 'B',  'D',   'A',  'D', 'D']]])
Again, you don't need Numpy in this question.
"""