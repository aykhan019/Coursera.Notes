

# Module 3: Keras and Deep Learning Libraries
## Deep Learning Libraries and Frameworks
### Overview
Deep learning frameworks offer various functionalities for building, training, and deploying machine learning models. Below are some of the most popular libraries and their key features.
#### Popular Deep Learning Libraries
1. **TensorFlow**
2. **PyTorch**
3. **Keras**
4. **Theano**
### 1. TensorFlow
#### Description
TensorFlow is the most widely used deep learning library, developed by Google and released in 2015. It is mainly used in production and large-scale projects. TensorFlow supports a vast range of tools for deep learning and has an active community contributing to its continuous development.
#### Features
- High scalability for production
- Support for deployment on multiple platforms
- Large, active community
*Additional Note:* GitHub link for TensorFlow -  
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667X3C6SQA%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJIMEYCIQDLptCpZWRQ56AdIp0aOUor09rOaYqn194wlfRM9hx0TgIhANSv18yuza511iD3wZFWi4Y%2BSUw4S7R9Wx4r47POSyU8Kv8DCEkQABoMNjM3NDIzMTgzODA1IgzlYrmpLzbOe5EbFT0q3APjNtSK1VXnN6DQ0Qcf6clKglOX7xUbJCPT3V8%2Bb16tyX7UyHAIMQ6n4MGJcK0%2FBtIsGx0Ohoj8tlmmOnzJ%2BZLOYSZbYabWWz4IIT61%2BbyCXAMGKqie6S3shKRmr4AJVDIu3Ag1EF8aNIVQRHFxbq5dwlmcOa0Asnvndc0fX1ytojBydrb5iUnj6L1Hd2%2B3YDCwd3oprZZQmHwp%2FJ5gL5s0atdjXKsv6H0rCJKVJGXQJohNfXvTKfpdFeSlPVkn58KdW3o5prK0tJSHcVnOCUV2MiR%2F40XEwldrMvJ4tSoouD%2FCNtLorpO3XVTC6j7PX4oDr%2FvNOOr%2FhqDdbOlNRM6TTWR%2FGc%2FEsnqQ5b5GvxBdJrAhlxvOezp%2B%2BjTjjKdHSJlkNEbg2hi%2Fo8e7nigCNGH280I3KQVt39se6eOpGLS3VV3Z%2Bo8qZqJFZjn8wCspun%2FKQ1dyrkxPCDwrKo5O9XmK5s5z2k1OwwVu6bC3sYOBtvG550sJB70t7PxTtNCRZfU12%2BlyBx2op5aeSdb218l67lwU%2BIDmuwQQtt5KohbVHpzevJrTtzsf8JzB36lOsJEuFAxW%2B6YOXONu3h3XC6yN%2BUcGDQ9hYvrtYgMd68ehabJSlJL5j6uW5viRITC7nY69BjqkAWlA9u6n%2F7d6D5CrwtRvAK1HQS7m08seS%2B993Nak20Mut0Mf7WdBKmfIbWEHCRDmtLzTSU8iCalntz%2BGURuucznWjtsEp3OD2Tqo%2B4BiMlT1hXRGiTSgfauc6BpXWJmvYtqDO83QpXuDD5BPxGklFqaeQYOOwrcPWq3S7LT%2Fjph7oTCM4Ihv1pbB39HUztHW8Z76hWoBWD5BN7KQUxMsox8Y8%2Buo&X-Amz-Signature=6383ea82649234ec95d8f428fa2b606f0f66fad1c64580471aff4418069b2b69&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667X3C6SQA%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJIMEYCIQDLptCpZWRQ56AdIp0aOUor09rOaYqn194wlfRM9hx0TgIhANSv18yuza511iD3wZFWi4Y%2BSUw4S7R9Wx4r47POSyU8Kv8DCEkQABoMNjM3NDIzMTgzODA1IgzlYrmpLzbOe5EbFT0q3APjNtSK1VXnN6DQ0Qcf6clKglOX7xUbJCPT3V8%2Bb16tyX7UyHAIMQ6n4MGJcK0%2FBtIsGx0Ohoj8tlmmOnzJ%2BZLOYSZbYabWWz4IIT61%2BbyCXAMGKqie6S3shKRmr4AJVDIu3Ag1EF8aNIVQRHFxbq5dwlmcOa0Asnvndc0fX1ytojBydrb5iUnj6L1Hd2%2B3YDCwd3oprZZQmHwp%2FJ5gL5s0atdjXKsv6H0rCJKVJGXQJohNfXvTKfpdFeSlPVkn58KdW3o5prK0tJSHcVnOCUV2MiR%2F40XEwldrMvJ4tSoouD%2FCNtLorpO3XVTC6j7PX4oDr%2FvNOOr%2FhqDdbOlNRM6TTWR%2FGc%2FEsnqQ5b5GvxBdJrAhlxvOezp%2B%2BjTjjKdHSJlkNEbg2hi%2Fo8e7nigCNGH280I3KQVt39se6eOpGLS3VV3Z%2Bo8qZqJFZjn8wCspun%2FKQ1dyrkxPCDwrKo5O9XmK5s5z2k1OwwVu6bC3sYOBtvG550sJB70t7PxTtNCRZfU12%2BlyBx2op5aeSdb218l67lwU%2BIDmuwQQtt5KohbVHpzevJrTtzsf8JzB36lOsJEuFAxW%2B6YOXONu3h3XC6yN%2BUcGDQ9hYvrtYgMd68ehabJSlJL5j6uW5viRITC7nY69BjqkAWlA9u6n%2F7d6D5CrwtRvAK1HQS7m08seS%2B993Nak20Mut0Mf7WdBKmfIbWEHCRDmtLzTSU8iCalntz%2BGURuucznWjtsEp3OD2Tqo%2B4BiMlT1hXRGiTSgfauc6BpXWJmvYtqDO83QpXuDD5BPxGklFqaeQYOOwrcPWq3S7LT%2Fjph7oTCM4Ihv1pbB39HUztHW8Z76hWoBWD5BN7KQUxMsox8Y8%2Buo&X-Amz-Signature=2e3017a6ac333b93fffdd2274ce38be075cf7bfb71e7bfcfdde2d47d530a94a8&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667X3C6SQA%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJIMEYCIQDLptCpZWRQ56AdIp0aOUor09rOaYqn194wlfRM9hx0TgIhANSv18yuza511iD3wZFWi4Y%2BSUw4S7R9Wx4r47POSyU8Kv8DCEkQABoMNjM3NDIzMTgzODA1IgzlYrmpLzbOe5EbFT0q3APjNtSK1VXnN6DQ0Qcf6clKglOX7xUbJCPT3V8%2Bb16tyX7UyHAIMQ6n4MGJcK0%2FBtIsGx0Ohoj8tlmmOnzJ%2BZLOYSZbYabWWz4IIT61%2BbyCXAMGKqie6S3shKRmr4AJVDIu3Ag1EF8aNIVQRHFxbq5dwlmcOa0Asnvndc0fX1ytojBydrb5iUnj6L1Hd2%2B3YDCwd3oprZZQmHwp%2FJ5gL5s0atdjXKsv6H0rCJKVJGXQJohNfXvTKfpdFeSlPVkn58KdW3o5prK0tJSHcVnOCUV2MiR%2F40XEwldrMvJ4tSoouD%2FCNtLorpO3XVTC6j7PX4oDr%2FvNOOr%2FhqDdbOlNRM6TTWR%2FGc%2FEsnqQ5b5GvxBdJrAhlxvOezp%2B%2BjTjjKdHSJlkNEbg2hi%2Fo8e7nigCNGH280I3KQVt39se6eOpGLS3VV3Z%2Bo8qZqJFZjn8wCspun%2FKQ1dyrkxPCDwrKo5O9XmK5s5z2k1OwwVu6bC3sYOBtvG550sJB70t7PxTtNCRZfU12%2BlyBx2op5aeSdb218l67lwU%2BIDmuwQQtt5KohbVHpzevJrTtzsf8JzB36lOsJEuFAxW%2B6YOXONu3h3XC6yN%2BUcGDQ9hYvrtYgMd68ehabJSlJL5j6uW5viRITC7nY69BjqkAWlA9u6n%2F7d6D5CrwtRvAK1HQS7m08seS%2B993Nak20Mut0Mf7WdBKmfIbWEHCRDmtLzTSU8iCalntz%2BGURuucznWjtsEp3OD2Tqo%2B4BiMlT1hXRGiTSgfauc6BpXWJmvYtqDO83QpXuDD5BPxGklFqaeQYOOwrcPWq3S7LT%2Fjph7oTCM4Ihv1pbB39HUztHW8Z76hWoBWD5BN7KQUxMsox8Y8%2Buo&X-Amz-Signature=00300c0386ce1af96a0b8b45920a32a2703631e205c9ff2943ef703b18404865&X-Amz-SignedHeaders=host&x-id=GetObject)
### Comparison of Libraries
- **TensorFlow**: Best for large-scale production environments.
- **PyTorch**: Ideal for research and academic settings.
- **Keras**: Preferred for beginners and fast prototyping.
### Summary
Deep learning libraries provide the foundation for building and optimizing neural networks. TensorFlow, PyTorch, and Keras are widely used, each suited for different applications depending on production needs, flexibility, and ease of use.
- **TensorFlow**: Developed by Google, TensorFlow is a deep learning library in Python. It is widely used in both research and production. TensorFlow supports static computational graphs and offers flexibility for large-scale machine learning tasks.
- **PyTorch**: Developed by Facebook, PyTorch is a deep learning library in Python known for its dynamic computational graph and ease of use, particularly in research and experimentation. PyTorch has gained significant popularity in academic settings and is often preferred for building custom deep learning models.
- **Keras**: Keras is a high-level deep learning library written in Python. It acts as an API that runs on top of lower-level libraries like TensorFlow. Keras is known for its simplicity and ease of use, making it a great choice for beginners in deep learning.
- **Theano**: Theano is a deep learning library built in Python. It was one of the first libraries in this field, developed by the Montreal Institute for Learning Algorithms. While it was powerful for earlier deep learning development, it is now largely deprecated and no longer actively maintained.
___
## Building Regression Models with Keras
### Overview of Keras Library
The Keras library is a high-level API for building and training deep learning models. It simplifies the process of developing neural networks and can run on top of other deep learning libraries like TensorFlow.
### Importing and Using Keras
5. **Importing Keras:**
	- Import the Keras library and check the backend:
```python
import keras
print("Keras Backend:", keras.backend.backend())
```
	- The output will display the backend used, typically TensorFlow.
6. **Preparing the Data:**
	- Example data consists of the compressive strength of concrete samples based on their ingredients. The data is organized in a pandas DataFrame named `concrete_data`.
	- Split the DataFrame into predictors and target variables:
```python
predictors = concrete_data[['cement', 'slag', 'flyash', 'water', 'superplasticizer', 'coarseaggregate', 'fineaggregate']]
target = concrete_data['strength']
```
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RAEHDI3J%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161848Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIQCMDf8KBgpCqVHS3yWF25iTneR4kD32ag1fs5LPQFXg8wIgMzN8A7nSDMltNwkd21xFh8GEzAETet4G5qNJw9CWfWsq%2FwMISBAAGgw2Mzc0MjMxODM4MDUiDICtUo%2FviIvJNvC6CSrcA9epeMQTviHPYrzqG0I%2FMQKK6%2F%2FsPuUCK9ivWE72Mh%2FQWGYJHtaepnU8khw%2B1nRCm8xmUjNynMwd0QnZAwZdVEmAgHbrlNRUFxnCPWxeDDBHZsEtR%2FCQr8mqkAK88cT%2FrmPQMCJLWBZ7JZa8ObCh%2FqnxMnOvsT29aI8PGIuGNp12G%2FjNPhMETg1krCwvaxbKeF5YAh9ov0Y2tY13Smlrhq4%2Fj6XQmPX0ChQaSyu2%2B6wSuha8JGuzz5tiX2bvKD8e3iEkb9Z7pK6j5Vn7325%2FDisB4xSLOR0vGOLzy9jJIaqILuYQ7koAd4ebxDJtzgZ9SFpAeQdrGOl%2BMxp%2FxHiI9TMo9TpwNm4Bp5Y3hvQyB8aK00qNqfqPHdhfOyVfFz5qILHpyWjTZTyzlBpCSqAjgREgkr2XrrmNC%2Bi84fQQNOe%2B2lZJ8q%2FmTF%2FTX%2FIzDfC%2FLBUEASIg24M8926dJkbgarudVB9bvSnK5DV3RXTeem86EWCjYg82uQJRVlfItYqWSULQfP1V9NX3Hp8l2lWaT9wlp0pGQOFcjg0zUI4SMIobMoZC9fsJ61Fyh5sDrZA24INBYD5cNFuYxpcXWFdrlxSTIq5bSVxJdKhYsladJUVbkMEaV2phAPiN%2FtINMN6Ajr0GOqUBlZOXfMB1FjijBB%2Bh%2B8MfFUog%2B262YOxYhmud8tl9ZS6HRs08Z6%2B0VOJ9Gm9uBMQA09RqajjzgFeSRz8ClTFV6jMeeHso5SfH68%2BQGLwMGf9osqJHGVdA2RW01AdQkGiM9Cko1C6G2bW3%2BV4KoaMqnFIVYpBYekMl%2Bu71RKoNBdv23xxsdKNezKDf7gmOL%2BDVvOX7doFHvjYzzkHyu4WZqkUbRWld&X-Amz-Signature=19b6b768b631bd0d7661e603698ad769c58648e10c341b3b85b0afd65fb070b6&X-Amz-SignedHeaders=host&x-id=GetObject)
### Building a Regression Model
7. **Creating the Model:**
	- Import necessary modules:
```python
from keras.models import Sequential
from keras.layers import Dense
```
	- **Classes:**
		- `**Sequential**`** Model**: A linear stack of layers where you add layers sequentially.
		- `**Dense**`** Layer**: A fully connected layer in the network where each neuron in the layer is connected to every neuron in the previous layer.
	- Initialize the Sequential model:
```python
model = Sequential()
```
8. **Adding Layers:**
	- Add hidden and output layers:
```python
model.add(Dense(5, input_shape=(8,), activation='relu'))
model.add(Dense(5, activation='relu'))
model.add(Dense(1))
```
	- **Parameters Explained:**
		- `**Dense(units, input_shape=None, activation=None)**`:
			- `units`: Number of neurons in the layer.
			- `input_shape`: Shape of input data (only needed for the first layer). For example, `input_shape=(8,)` indicates 8 features.
			- `activation`: Activation function used by the layer. 'relu' is used for hidden layers, and no activation function is specified for the output layer to allow continuous output.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666GPKHDWZ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161847Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJHMEUCIQDZzvbDyDEZQ1ssGK4J0354SxLoklNhM4PTtU07cek5dAIgAZNsfsyRvDurU68jmEYJg2l6q4Ok01wcQzx5Eyba3CEq%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDINQeA5TKv1qdz7CKSrcA5NxXG95MKTE%2FuQ5iSifE0nFM02Kr3QD2QNxhEZWq%2Btc6a2XPQgZMqUOR0Bgrm6W%2FzbW2FjmWNugdLHJ%2BLK%2BcCW9zBTc3BfiZTvbeA2acszK9NAqPBTYd4hkQiucCHwl6XiQOSVwBKF1pLYRPdsxEC2wKEVb8iahFGlqS2xcaSae7np8tX%2ByOiAFIlmVqDo%2BCIxSkpaUEIEbJQCEnBNm3DHIOlO2CJ%2FcwXUA0d1nuaod1wHSidj6gIxmMSbfXtjWZ1npMGd3Th0IgHQcqG4PyKOlYTkvc7WNWb5%2BhBNs9NTxzYq%2FCIEFrbNzIpWgqUOB6FhNw3qQWz8APkHMd4aA97JuF3dcdvhVp025HvLlG3DGVlUe97rZC4mmbhDqAw5PLadRo%2B%2F2PPg2YPWE9Av63OUwNvqg3AO9smDXoCoQFCx9UNqYumx29zGuiJhSmv0pmhWPjFShI9xlps0HyYNmyA0fF%2FpuYkhuTotS351VcsuqKU8Yi4TckW3NPQf9xonwNNl9LJK%2BgKc2dVSrDC5OYLDoJb9KbP71ZY2jKqEFE4h3SAes%2FZcze0l%2FOYPCYkB93hR886ou%2BO7ID5gsknF1IqwfPyEo8YkAF9PpIzoFvR37sdFsvB6N8H0S5x7FMMSdjr0GOqUBJPNxDQ3Oz9WGgEM%2F91qx9E%2BrzbsdzOJ7S7eNuuXZwEcZaGuGjugRdCIQFVVdSR7SU7fCFgRhkElIDgvtUl50zGiJ7U8MWbOgWpDonHNDjIXSdXjHplbFN6Sh82jHYR70BmvWF%2FXKMH6nDxYe9frV4cizUgp2nA1IziKqUqlvyt%2Fpjxe%2FL18QvLAFLBwvLN2zcdrTdSLpoI4BtPlaM4L%2FDxb3RaSZ&X-Amz-Signature=0c8891bca74d855da40fc99870e6d79b2df46a75c387b53d3714c172bbdb32e8&X-Amz-SignedHeaders=host&x-id=GetObject)
9. **Compiling the Model:**
	- Define the optimizer and loss function:
```python
model.compile(optimizer='adam', loss='mean_squared_error')
```
	- **Parameters Explained:**
		- `**optimizer**`: Optimization algorithm used for training. 'adam' is an adaptive optimizer that adjusts the learning rate during training (itself).
		- `**loss**`: Loss function used to measure the difference between predicted and actual values. 'mean_squared_error' is used for regression tasks.
10. **Training the Model:**
	- Fit the model to the data:
```python
model.fit(predictors, target, epochs=100)
```
	- **Parameters Explained:**
		- `**predictors**`: Input data (features).
		- `**target**`: Output data (labels).
		- `**epochs**`: Number of iterations over the entire training data.
11. **Making Predictions:**
	- Use the model to predict new data:
```python
predictions = model.predict(new_data)
```
	- **Parameters Explained:**
		- `**new_data**`: New input data for which predictions are to be made.
		- `**predictions**`: The output from the model for the new data.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667X3C6SQA%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161847Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJIMEYCIQDLptCpZWRQ56AdIp0aOUor09rOaYqn194wlfRM9hx0TgIhANSv18yuza511iD3wZFWi4Y%2BSUw4S7R9Wx4r47POSyU8Kv8DCEkQABoMNjM3NDIzMTgzODA1IgzlYrmpLzbOe5EbFT0q3APjNtSK1VXnN6DQ0Qcf6clKglOX7xUbJCPT3V8%2Bb16tyX7UyHAIMQ6n4MGJcK0%2FBtIsGx0Ohoj8tlmmOnzJ%2BZLOYSZbYabWWz4IIT61%2BbyCXAMGKqie6S3shKRmr4AJVDIu3Ag1EF8aNIVQRHFxbq5dwlmcOa0Asnvndc0fX1ytojBydrb5iUnj6L1Hd2%2B3YDCwd3oprZZQmHwp%2FJ5gL5s0atdjXKsv6H0rCJKVJGXQJohNfXvTKfpdFeSlPVkn58KdW3o5prK0tJSHcVnOCUV2MiR%2F40XEwldrMvJ4tSoouD%2FCNtLorpO3XVTC6j7PX4oDr%2FvNOOr%2FhqDdbOlNRM6TTWR%2FGc%2FEsnqQ5b5GvxBdJrAhlxvOezp%2B%2BjTjjKdHSJlkNEbg2hi%2Fo8e7nigCNGH280I3KQVt39se6eOpGLS3VV3Z%2Bo8qZqJFZjn8wCspun%2FKQ1dyrkxPCDwrKo5O9XmK5s5z2k1OwwVu6bC3sYOBtvG550sJB70t7PxTtNCRZfU12%2BlyBx2op5aeSdb218l67lwU%2BIDmuwQQtt5KohbVHpzevJrTtzsf8JzB36lOsJEuFAxW%2B6YOXONu3h3XC6yN%2BUcGDQ9hYvrtYgMd68ehabJSlJL5j6uW5viRITC7nY69BjqkAWlA9u6n%2F7d6D5CrwtRvAK1HQS7m08seS%2B993Nak20Mut0Mf7WdBKmfIbWEHCRDmtLzTSU8iCalntz%2BGURuucznWjtsEp3OD2Tqo%2B4BiMlT1hXRGiTSgfauc6BpXWJmvYtqDO83QpXuDD5BPxGklFqaeQYOOwrcPWq3S7LT%2Fjph7oTCM4Ihv1pbB39HUztHW8Z76hWoBWD5BN7KQUxMsox8Y8%2Buo&X-Amz-Signature=f80847a946ab51780a1e90387d4483d046b431e01b4e5700a1febb97390444f3&X-Amz-SignedHeaders=host&x-id=GetObject)
### Conclusion
Keras simplifies the process of building and training neural networks. For regression tasks, a basic model can be built with just a few lines of code, making it accessible and efficient for rapid development. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.

*Additional Notes:*
Keras Activation Functions: [https://keras.io/activations/](https://keras.io/activations/)
Keras Models: [https://keras.io/models/about-keras-models/#about-keras-models](https://keras.io/models/about-keras-models/#about-keras-models)
Keras Optimizers: [https://keras.io/optimizers/](https://keras.io/optimizers/)
Keras Metrics: [https://keras.io/metrics/](https://keras.io/metrics/)
___
## Building Classification Models with Keras
### **Overview of Classification with Keras**
The Keras library is a high-level API for building and training deep learning models. In this example, Keras is used to build a classification model that predicts whether purchasing a car is a good choice based on the car's attributes.
**Setting Up Keras**
12. **Importing Necessary Libraries**:
	- Import the Keras library, the Sequential model, and the Dense layer:
```python
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical
```
13. **Preparing the Data**:
	- Example dataset: `car_data`, cleaned and one-hot encoded. The dataset includes features such as price, maintenance cost, and capacity.
	- Split the dataset into predictors and target variables:
```python
predictors = car_data[['price_high', 'price_medium', 'price_low',
                       'maint_high', 'maint_medium', 'maint_low',
                       'capacity_two', 'capacity_more']]
target = car_data['decision']
```
	- **Transforming the Target Variable**:
		- Convert the target variable into one-hot encoded format using `to_categorical`:
```python
target = to_categorical(target)
```
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667X3C6SQA%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161847Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJIMEYCIQDLptCpZWRQ56AdIp0aOUor09rOaYqn194wlfRM9hx0TgIhANSv18yuza511iD3wZFWi4Y%2BSUw4S7R9Wx4r47POSyU8Kv8DCEkQABoMNjM3NDIzMTgzODA1IgzlYrmpLzbOe5EbFT0q3APjNtSK1VXnN6DQ0Qcf6clKglOX7xUbJCPT3V8%2Bb16tyX7UyHAIMQ6n4MGJcK0%2FBtIsGx0Ohoj8tlmmOnzJ%2BZLOYSZbYabWWz4IIT61%2BbyCXAMGKqie6S3shKRmr4AJVDIu3Ag1EF8aNIVQRHFxbq5dwlmcOa0Asnvndc0fX1ytojBydrb5iUnj6L1Hd2%2B3YDCwd3oprZZQmHwp%2FJ5gL5s0atdjXKsv6H0rCJKVJGXQJohNfXvTKfpdFeSlPVkn58KdW3o5prK0tJSHcVnOCUV2MiR%2F40XEwldrMvJ4tSoouD%2FCNtLorpO3XVTC6j7PX4oDr%2FvNOOr%2FhqDdbOlNRM6TTWR%2FGc%2FEsnqQ5b5GvxBdJrAhlxvOezp%2B%2BjTjjKdHSJlkNEbg2hi%2Fo8e7nigCNGH280I3KQVt39se6eOpGLS3VV3Z%2Bo8qZqJFZjn8wCspun%2FKQ1dyrkxPCDwrKo5O9XmK5s5z2k1OwwVu6bC3sYOBtvG550sJB70t7PxTtNCRZfU12%2BlyBx2op5aeSdb218l67lwU%2BIDmuwQQtt5KohbVHpzevJrTtzsf8JzB36lOsJEuFAxW%2B6YOXONu3h3XC6yN%2BUcGDQ9hYvrtYgMd68ehabJSlJL5j6uW5viRITC7nY69BjqkAWlA9u6n%2F7d6D5CrwtRvAK1HQS7m08seS%2B993Nak20Mut0Mf7WdBKmfIbWEHCRDmtLzTSU8iCalntz%2BGURuucznWjtsEp3OD2Tqo%2B4BiMlT1hXRGiTSgfauc6BpXWJmvYtqDO83QpXuDD5BPxGklFqaeQYOOwrcPWq3S7LT%2Fjph7oTCM4Ihv1pbB39HUztHW8Z76hWoBWD5BN7KQUxMsox8Y8%2Buo&X-Amz-Signature=daf16ba3afd170c713c63eefd2548bcda402d04a3ad5436108fa78830b0c3795&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Building a Classification Model**
14. **Creating the Model**:
	- Initialize the Sequential model:
```python
model = Sequential()
```
15. **Adding Layers**:
	- Add hidden and output layers:
```python
model.add(Dense(5, input_shape=(8,), activation='relu'))
model.add(Dense(5, activation='relu'))
model.add(Dense(4, activation='softmax'))
```
**Parameters Explained**:
	- `Dense(units, input_shape=None, activation=None)`:
		- **units**: Number of neurons in the layer.
		- **input_shape**: Shape of input data (only needed for the first layer). For example, `input_shape=(8,)` indicates 8 features.
		- **activation**: Activation function used by the layer. 'relu' is used for hidden layers, and 'softmax' is used for the output layer to provide probabilities for each class.
16. **Compiling the Model**:
	- Define the optimizer and loss function:
```python
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
```
**Parameters Explained**:
	- `optimizer`: Optimization algorithm used for training. 'adam' is an adaptive optimizer that adjusts the learning rate during training.
	- `loss`: Loss function used to measure the difference between predicted and actual values. 'categorical_crossentropy' is used for multi-class classification tasks.
	- `metrics`: Evaluation metric used to measure model performance. 'accuracy' is a built-in metric in Keras.
17. **Training the Model**:
	- Fit the model to the data:
```python
model.fit(predictors, target, epochs=100)
```
**Parameters Explained**:
	- `**predictors**`: Input data (features).
	- `**target**`: Output data (labels).
	- `**epochs**`: Number of iterations over the entire training data.
18. **Making Predictions**:
	- Use the model to predict new data:
```python
predictions = model.predict(new_data)
```
**Parameters Explained**:
	- `**new_data**`: New input data for which predictions are to be made.
	- `**predictions**`: The output from the model for the new data. Each prediction will be a probability distribution over the classes.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667X3C6SQA%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161847Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJIMEYCIQDLptCpZWRQ56AdIp0aOUor09rOaYqn194wlfRM9hx0TgIhANSv18yuza511iD3wZFWi4Y%2BSUw4S7R9Wx4r47POSyU8Kv8DCEkQABoMNjM3NDIzMTgzODA1IgzlYrmpLzbOe5EbFT0q3APjNtSK1VXnN6DQ0Qcf6clKglOX7xUbJCPT3V8%2Bb16tyX7UyHAIMQ6n4MGJcK0%2FBtIsGx0Ohoj8tlmmOnzJ%2BZLOYSZbYabWWz4IIT61%2BbyCXAMGKqie6S3shKRmr4AJVDIu3Ag1EF8aNIVQRHFxbq5dwlmcOa0Asnvndc0fX1ytojBydrb5iUnj6L1Hd2%2B3YDCwd3oprZZQmHwp%2FJ5gL5s0atdjXKsv6H0rCJKVJGXQJohNfXvTKfpdFeSlPVkn58KdW3o5prK0tJSHcVnOCUV2MiR%2F40XEwldrMvJ4tSoouD%2FCNtLorpO3XVTC6j7PX4oDr%2FvNOOr%2FhqDdbOlNRM6TTWR%2FGc%2FEsnqQ5b5GvxBdJrAhlxvOezp%2B%2BjTjjKdHSJlkNEbg2hi%2Fo8e7nigCNGH280I3KQVt39se6eOpGLS3VV3Z%2Bo8qZqJFZjn8wCspun%2FKQ1dyrkxPCDwrKo5O9XmK5s5z2k1OwwVu6bC3sYOBtvG550sJB70t7PxTtNCRZfU12%2BlyBx2op5aeSdb218l67lwU%2BIDmuwQQtt5KohbVHpzevJrTtzsf8JzB36lOsJEuFAxW%2B6YOXONu3h3XC6yN%2BUcGDQ9hYvrtYgMd68ehabJSlJL5j6uW5viRITC7nY69BjqkAWlA9u6n%2F7d6D5CrwtRvAK1HQS7m08seS%2B993Nak20Mut0Mf7WdBKmfIbWEHCRDmtLzTSU8iCalntz%2BGURuucznWjtsEp3OD2Tqo%2B4BiMlT1hXRGiTSgfauc6BpXWJmvYtqDO83QpXuDD5BPxGklFqaeQYOOwrcPWq3S7LT%2Fjph7oTCM4Ihv1pbB39HUztHW8Z76hWoBWD5BN7KQUxMsox8Y8%2Buo&X-Amz-Signature=f6e23dbedbc1b447bce46605aea7f4610a421eb41426db0b0e4528feeb458c3c&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667X3C6SQA%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161847Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJIMEYCIQDLptCpZWRQ56AdIp0aOUor09rOaYqn194wlfRM9hx0TgIhANSv18yuza511iD3wZFWi4Y%2BSUw4S7R9Wx4r47POSyU8Kv8DCEkQABoMNjM3NDIzMTgzODA1IgzlYrmpLzbOe5EbFT0q3APjNtSK1VXnN6DQ0Qcf6clKglOX7xUbJCPT3V8%2Bb16tyX7UyHAIMQ6n4MGJcK0%2FBtIsGx0Ohoj8tlmmOnzJ%2BZLOYSZbYabWWz4IIT61%2BbyCXAMGKqie6S3shKRmr4AJVDIu3Ag1EF8aNIVQRHFxbq5dwlmcOa0Asnvndc0fX1ytojBydrb5iUnj6L1Hd2%2B3YDCwd3oprZZQmHwp%2FJ5gL5s0atdjXKsv6H0rCJKVJGXQJohNfXvTKfpdFeSlPVkn58KdW3o5prK0tJSHcVnOCUV2MiR%2F40XEwldrMvJ4tSoouD%2FCNtLorpO3XVTC6j7PX4oDr%2FvNOOr%2FhqDdbOlNRM6TTWR%2FGc%2FEsnqQ5b5GvxBdJrAhlxvOezp%2B%2BjTjjKdHSJlkNEbg2hi%2Fo8e7nigCNGH280I3KQVt39se6eOpGLS3VV3Z%2Bo8qZqJFZjn8wCspun%2FKQ1dyrkxPCDwrKo5O9XmK5s5z2k1OwwVu6bC3sYOBtvG550sJB70t7PxTtNCRZfU12%2BlyBx2op5aeSdb218l67lwU%2BIDmuwQQtt5KohbVHpzevJrTtzsf8JzB36lOsJEuFAxW%2B6YOXONu3h3XC6yN%2BUcGDQ9hYvrtYgMd68ehabJSlJL5j6uW5viRITC7nY69BjqkAWlA9u6n%2F7d6D5CrwtRvAK1HQS7m08seS%2B993Nak20Mut0Mf7WdBKmfIbWEHCRDmtLzTSU8iCalntz%2BGURuucznWjtsEp3OD2Tqo%2B4BiMlT1hXRGiTSgfauc6BpXWJmvYtqDO83QpXuDD5BPxGklFqaeQYOOwrcPWq3S7LT%2Fjph7oTCM4Ihv1pbB39HUztHW8Z76hWoBWD5BN7KQUxMsox8Y8%2Buo&X-Amz-Signature=f35ad758e942640a63138f290a74782ebe1c9cdd28bc2e1576dced6cb5e1428f&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
