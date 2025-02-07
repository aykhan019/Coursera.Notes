

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZYU2UUG3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJIMEYCIQDYl2mIH0zFB4gw98OD5OUossT5IPq%2FdLJXq%2FDJsGJiWgIhAIfIB%2F5CWji%2Ftbc5teUYwa3cvs7n1rbYUBzeb4loXQULKv8DCG8QABoMNjM3NDIzMTgzODA1IgwV2Wzu0VhrEGpvdNMq3API9Z7%2F8w3qSoRCSGBSfYjCy3JPX%2BC22McNMPkIFvkvPk9TfMQuK3%2BpdYSyZhdC%2FLy0aNJUihCg275%2Btmq%2FIOT5JJ614JVdTpt0jEFXPa8xDvQZKRx9qPBNtlaVm6Zh8obz0uSA3L%2BWuCIghkeI%2FpD5oi1nFQaN84tP%2BJjsvDKOiNj0Jpo%2FK02VQg5s2z6h3yxTZ8NtysHDMuuh099QJMv4h43%2Fz406cUy7hE%2BxVTQAd6rTigpM%2B%2BBGlOsXst6SzeHF6S9cDOIVPZnRoH8Cah7kUJsAU6EUIWAICkKR1rmwv5JS0%2Fy35xpT%2FlFOO%2BxfsmOXg5axnYlxTDraqkJ3tqxldT5yv12%2BQMvSu9i%2BklaP6Xcd%2BzIORG4Q%2FUUzLv%2BdIZ8HqXbp1QOJ3pKV%2BfNvRrWRUtkfjK%2BcAu%2FvxyrP44d2O0pevuuboYFdb6rhgtEBro7DBHqG7CMatQB5ai%2F5RpkNpPdBjxGgwI2xjLMVw3dVF%2Bbq4SAYCnDEjAmv9sX6wtnEdiyxg%2BZWMZS5rD0UM82WkUWQfLdulCKz5R8aVdNg5BX5uceBvAlAXrWuj5uZ7PQGP45T8BDSMOPB3YlZDkE4En9rGM%2BuGYKa%2B71HxR0kRcNHY0YKPLr0kZaXzzCBv5a9BjqkATY604mv1F7G3eFMkp4JzERPn5Lki%2B%2F7%2BSa0BRNsNhdKeK6CGncvFipoKX6G92XvV5hW%2BsbP1YDui9OzWe8JptsmOt2z2%2FszV14MYBSPPKfBIp1gHTTSdicQGOKjFtUZ44Mcv3vUeoLP7xdVgueGjEQpTrMsslmzbolRYYaGY%2FsDUGTkcKRVPns7EP3%2FE1DLnS9AINBJ8pJxE%2FDLCQ4%2FLXENGpL2&X-Amz-Signature=42f9762ed4ed14b870f885ad2a6dd8c5398519f64154b515cdafe54d3e4d65c9&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZYU2UUG3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJIMEYCIQDYl2mIH0zFB4gw98OD5OUossT5IPq%2FdLJXq%2FDJsGJiWgIhAIfIB%2F5CWji%2Ftbc5teUYwa3cvs7n1rbYUBzeb4loXQULKv8DCG8QABoMNjM3NDIzMTgzODA1IgwV2Wzu0VhrEGpvdNMq3API9Z7%2F8w3qSoRCSGBSfYjCy3JPX%2BC22McNMPkIFvkvPk9TfMQuK3%2BpdYSyZhdC%2FLy0aNJUihCg275%2Btmq%2FIOT5JJ614JVdTpt0jEFXPa8xDvQZKRx9qPBNtlaVm6Zh8obz0uSA3L%2BWuCIghkeI%2FpD5oi1nFQaN84tP%2BJjsvDKOiNj0Jpo%2FK02VQg5s2z6h3yxTZ8NtysHDMuuh099QJMv4h43%2Fz406cUy7hE%2BxVTQAd6rTigpM%2B%2BBGlOsXst6SzeHF6S9cDOIVPZnRoH8Cah7kUJsAU6EUIWAICkKR1rmwv5JS0%2Fy35xpT%2FlFOO%2BxfsmOXg5axnYlxTDraqkJ3tqxldT5yv12%2BQMvSu9i%2BklaP6Xcd%2BzIORG4Q%2FUUzLv%2BdIZ8HqXbp1QOJ3pKV%2BfNvRrWRUtkfjK%2BcAu%2FvxyrP44d2O0pevuuboYFdb6rhgtEBro7DBHqG7CMatQB5ai%2F5RpkNpPdBjxGgwI2xjLMVw3dVF%2Bbq4SAYCnDEjAmv9sX6wtnEdiyxg%2BZWMZS5rD0UM82WkUWQfLdulCKz5R8aVdNg5BX5uceBvAlAXrWuj5uZ7PQGP45T8BDSMOPB3YlZDkE4En9rGM%2BuGYKa%2B71HxR0kRcNHY0YKPLr0kZaXzzCBv5a9BjqkATY604mv1F7G3eFMkp4JzERPn5Lki%2B%2F7%2BSa0BRNsNhdKeK6CGncvFipoKX6G92XvV5hW%2BsbP1YDui9OzWe8JptsmOt2z2%2FszV14MYBSPPKfBIp1gHTTSdicQGOKjFtUZ44Mcv3vUeoLP7xdVgueGjEQpTrMsslmzbolRYYaGY%2FsDUGTkcKRVPns7EP3%2FE1DLnS9AINBJ8pJxE%2FDLCQ4%2FLXENGpL2&X-Amz-Signature=1a93b1337541f3b03a1001bb54b09504624c840b2eca5cd8162dab3c965efaf4&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZYU2UUG3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJIMEYCIQDYl2mIH0zFB4gw98OD5OUossT5IPq%2FdLJXq%2FDJsGJiWgIhAIfIB%2F5CWji%2Ftbc5teUYwa3cvs7n1rbYUBzeb4loXQULKv8DCG8QABoMNjM3NDIzMTgzODA1IgwV2Wzu0VhrEGpvdNMq3API9Z7%2F8w3qSoRCSGBSfYjCy3JPX%2BC22McNMPkIFvkvPk9TfMQuK3%2BpdYSyZhdC%2FLy0aNJUihCg275%2Btmq%2FIOT5JJ614JVdTpt0jEFXPa8xDvQZKRx9qPBNtlaVm6Zh8obz0uSA3L%2BWuCIghkeI%2FpD5oi1nFQaN84tP%2BJjsvDKOiNj0Jpo%2FK02VQg5s2z6h3yxTZ8NtysHDMuuh099QJMv4h43%2Fz406cUy7hE%2BxVTQAd6rTigpM%2B%2BBGlOsXst6SzeHF6S9cDOIVPZnRoH8Cah7kUJsAU6EUIWAICkKR1rmwv5JS0%2Fy35xpT%2FlFOO%2BxfsmOXg5axnYlxTDraqkJ3tqxldT5yv12%2BQMvSu9i%2BklaP6Xcd%2BzIORG4Q%2FUUzLv%2BdIZ8HqXbp1QOJ3pKV%2BfNvRrWRUtkfjK%2BcAu%2FvxyrP44d2O0pevuuboYFdb6rhgtEBro7DBHqG7CMatQB5ai%2F5RpkNpPdBjxGgwI2xjLMVw3dVF%2Bbq4SAYCnDEjAmv9sX6wtnEdiyxg%2BZWMZS5rD0UM82WkUWQfLdulCKz5R8aVdNg5BX5uceBvAlAXrWuj5uZ7PQGP45T8BDSMOPB3YlZDkE4En9rGM%2BuGYKa%2B71HxR0kRcNHY0YKPLr0kZaXzzCBv5a9BjqkATY604mv1F7G3eFMkp4JzERPn5Lki%2B%2F7%2BSa0BRNsNhdKeK6CGncvFipoKX6G92XvV5hW%2BsbP1YDui9OzWe8JptsmOt2z2%2FszV14MYBSPPKfBIp1gHTTSdicQGOKjFtUZ44Mcv3vUeoLP7xdVgueGjEQpTrMsslmzbolRYYaGY%2FsDUGTkcKRVPns7EP3%2FE1DLnS9AINBJ8pJxE%2FDLCQ4%2FLXENGpL2&X-Amz-Signature=c230d3fe9b7073fa9f7d683d76decb01d57893793a97b73b681c93bc7f54799e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QK3NT52C%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJHMEUCIA3frmULcD6VndUI8vURY%2BfwFK%2FfzLkID8a2H1zwP3JRAiEA7%2Bzlv2hUpHsfcz0qJcRfb7Fx9%2FUaiPNXiqe5uELu0NAq%2FwMIbxAAGgw2Mzc0MjMxODM4MDUiDOAe8AGuV5qo7Wu6yyrcAxR50Ot1q%2FL5pMnXBGNLZuDVBK38kZ7087eQsmGmSUW9EcdfMF5MqixsU1DBkLwy07OgIYZGFsFPFTe3%2BHbNMaqUzBlvWahgl1R2y6%2BnU4EHKzIhiMxtYi0cxozG%2FxkFcTpOFcVj%2Ba5Nfy9J3yIT4SnWLUWWOQNffXXinrlRyGZZeCHdY2rqvpWIKleODO5Io1mPWTpRkyorev0rzvcGoTRosXYOP%2FucK9DJV9sKRMlpf2i1ywMiauYOJxEe0kd6nsl%2F5Vp9hm9CgVZ%2FeN7b9RQUZN7Nk8QnCkemMDF40YrCo8TYhK3GlucrUDlramwnKuR1p2%2Fb33G6%2FPfI%2F7V0lmj6YtPH3KbvukSR0RAcVbNvC0XiI%2BpC%2FiqoMx%2BKJ4U5qsvUAI6BocwTtoovq%2FPuKwbgs6HXkH7m1szF5XFw5q%2FVvMQHxO57dYT5InYTK%2FZTu%2FfWY5Yb%2FZZAbAAiPLr2QKId2DK5p1lHRbNIu6jdIS3rzGtYJYCSOUKUNXn1anRQ1XYuQdtZbjjFISbGI5SWy6XTp9U%2B1zFjQ3H1BdUWBABNIUkzRwmY8%2FzOBC5Sn6GfsmxDnbnojBGxOMFGh0SZde7BccOKBGBTi8DvSH0kK%2FI1gJyhHXV1w47C3I4iMOu%2Blr0GOqUBRkNRM%2BXjxeLJ%2BouU3kMGg7pXOXi9oiVhUHWFlafKqupjhoMd0gRPct1hvfWhepJTFUIdysM%2FSm1l%2BOSOarIU74jXR6frv7EwjYPQ16uIDL%2B%2Ben3A36x3tUaSlElXA3wc4M%2BR7wtz2N8RL8mekPqawBEeNV3K2HlA1Y%2FOXL8WsYyfd9%2BZBxlxq%2F9XYZoV6lRGCVjJ5gutgggtXgpbl3qI59rPxLJg&X-Amz-Signature=934f108079f32afda3a8a11974b20b2edfc605da61db7b1bad34f3e9e1db2dee&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SJXCNCG3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJGMEQCIFs7BM3I%2FKRCbto6Gc%2Fknul%2BfYE4b%2FmMizyd8KQzCiTXAiA209R9uVVL4R7JgWIHXPooqlpabEAmrJkN0XueSp9omir%2FAwhvEAAaDDYzNzQyMzE4MzgwNSIM4hIpuUNtYq7Eoct4KtwDj8wnYcvV0baVxBYI9hZjndrzEIcCcd2%2Bj18w6UJzwjdpyiWlWHUaWNLy7oVeXPrwyK1GlKhcUZuTY%2BdgXXW3ReX8ZGjqzAjKgo34WNRABtJSSU1S2ci6qmBmwmPuOY%2BFTxBmAUQuhDPtrXia9fkXow5hHgGLbRqv4T3pV7Fjb8Z9uKpzC%2FHE%2BgsfBVtiYGzEymuf4n8jL0Pp0ZaRDQT7QWeyxR25yJOPRljGcuhYZFaWziCCsLnT1zRCa76X1tsyqzisC3X9lusQ9q9pV3ZVAzsEWQ06%2BcpH8csNo3gIR%2F1qzzL4ucDbbZ%2BiWEjbirfLgvAs5oDgvxxOQeUn8W%2B514p%2F77F3BHRLxFfnWGgLVvA%2B9CPH29bbMxwAJMaeUs2XAwA975v0OZb2SNNtyyAq53Zd9b0nXLwcDaFVI5%2FO8dUSvP6I39AAEqeq8J5Wv5PXVs32Jglf%2FOQfwAu%2Bpmpx6RRq3Vys8WRX6KD3lCpLksCgqhyOb6xlKbEfZEG8DvXbSpSfssGWnOJFJQsrwR3CH8aD0Rw8Wj%2BLmni0mctzzX4NmJZODMzNrkPlR%2BWr1l%2BV1G7%2FNRr2lubA%2FyrTvQ1xPg%2FDcIQowkX2a1UXjpwlYI%2Fz0znK%2FvXWTduaHX0wz7%2BWvQY6pgEPJphOvyLuzk3wC9Tq6aAGUP5bmz0zW%2BBqnjv5g8KrRkBGhnsXUIOsrt%2BhpMPqikEYpd8NDVyM9TLmdTjG2lZcA0gOlmfn5y%2BK4C%2FhomMBA%2FZGcSU0i7oAeMuFxlLJaZVbrmyTi4lY0BDtOVJ08yX8cRwGpiMspiP3iQvidjtWQdwq6uMBgvx%2BbAiVzI3Oj59%2F%2Fhn1FGXvmYhGZY%2FRXqFdonX0Np%2Bo&X-Amz-Signature=309f88e9d07a8ad05b9dd8b32d686062f38e4aebf0dec6e70e01c88aae6b78bf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZYU2UUG3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJIMEYCIQDYl2mIH0zFB4gw98OD5OUossT5IPq%2FdLJXq%2FDJsGJiWgIhAIfIB%2F5CWji%2Ftbc5teUYwa3cvs7n1rbYUBzeb4loXQULKv8DCG8QABoMNjM3NDIzMTgzODA1IgwV2Wzu0VhrEGpvdNMq3API9Z7%2F8w3qSoRCSGBSfYjCy3JPX%2BC22McNMPkIFvkvPk9TfMQuK3%2BpdYSyZhdC%2FLy0aNJUihCg275%2Btmq%2FIOT5JJ614JVdTpt0jEFXPa8xDvQZKRx9qPBNtlaVm6Zh8obz0uSA3L%2BWuCIghkeI%2FpD5oi1nFQaN84tP%2BJjsvDKOiNj0Jpo%2FK02VQg5s2z6h3yxTZ8NtysHDMuuh099QJMv4h43%2Fz406cUy7hE%2BxVTQAd6rTigpM%2B%2BBGlOsXst6SzeHF6S9cDOIVPZnRoH8Cah7kUJsAU6EUIWAICkKR1rmwv5JS0%2Fy35xpT%2FlFOO%2BxfsmOXg5axnYlxTDraqkJ3tqxldT5yv12%2BQMvSu9i%2BklaP6Xcd%2BzIORG4Q%2FUUzLv%2BdIZ8HqXbp1QOJ3pKV%2BfNvRrWRUtkfjK%2BcAu%2FvxyrP44d2O0pevuuboYFdb6rhgtEBro7DBHqG7CMatQB5ai%2F5RpkNpPdBjxGgwI2xjLMVw3dVF%2Bbq4SAYCnDEjAmv9sX6wtnEdiyxg%2BZWMZS5rD0UM82WkUWQfLdulCKz5R8aVdNg5BX5uceBvAlAXrWuj5uZ7PQGP45T8BDSMOPB3YlZDkE4En9rGM%2BuGYKa%2B71HxR0kRcNHY0YKPLr0kZaXzzCBv5a9BjqkATY604mv1F7G3eFMkp4JzERPn5Lki%2B%2F7%2BSa0BRNsNhdKeK6CGncvFipoKX6G92XvV5hW%2BsbP1YDui9OzWe8JptsmOt2z2%2FszV14MYBSPPKfBIp1gHTTSdicQGOKjFtUZ44Mcv3vUeoLP7xdVgueGjEQpTrMsslmzbolRYYaGY%2FsDUGTkcKRVPns7EP3%2FE1DLnS9AINBJ8pJxE%2FDLCQ4%2FLXENGpL2&X-Amz-Signature=2fabca648a5773c4e2926038c2421688f571c441b8fc35f7385369f83e90f78b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZYU2UUG3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJIMEYCIQDYl2mIH0zFB4gw98OD5OUossT5IPq%2FdLJXq%2FDJsGJiWgIhAIfIB%2F5CWji%2Ftbc5teUYwa3cvs7n1rbYUBzeb4loXQULKv8DCG8QABoMNjM3NDIzMTgzODA1IgwV2Wzu0VhrEGpvdNMq3API9Z7%2F8w3qSoRCSGBSfYjCy3JPX%2BC22McNMPkIFvkvPk9TfMQuK3%2BpdYSyZhdC%2FLy0aNJUihCg275%2Btmq%2FIOT5JJ614JVdTpt0jEFXPa8xDvQZKRx9qPBNtlaVm6Zh8obz0uSA3L%2BWuCIghkeI%2FpD5oi1nFQaN84tP%2BJjsvDKOiNj0Jpo%2FK02VQg5s2z6h3yxTZ8NtysHDMuuh099QJMv4h43%2Fz406cUy7hE%2BxVTQAd6rTigpM%2B%2BBGlOsXst6SzeHF6S9cDOIVPZnRoH8Cah7kUJsAU6EUIWAICkKR1rmwv5JS0%2Fy35xpT%2FlFOO%2BxfsmOXg5axnYlxTDraqkJ3tqxldT5yv12%2BQMvSu9i%2BklaP6Xcd%2BzIORG4Q%2FUUzLv%2BdIZ8HqXbp1QOJ3pKV%2BfNvRrWRUtkfjK%2BcAu%2FvxyrP44d2O0pevuuboYFdb6rhgtEBro7DBHqG7CMatQB5ai%2F5RpkNpPdBjxGgwI2xjLMVw3dVF%2Bbq4SAYCnDEjAmv9sX6wtnEdiyxg%2BZWMZS5rD0UM82WkUWQfLdulCKz5R8aVdNg5BX5uceBvAlAXrWuj5uZ7PQGP45T8BDSMOPB3YlZDkE4En9rGM%2BuGYKa%2B71HxR0kRcNHY0YKPLr0kZaXzzCBv5a9BjqkATY604mv1F7G3eFMkp4JzERPn5Lki%2B%2F7%2BSa0BRNsNhdKeK6CGncvFipoKX6G92XvV5hW%2BsbP1YDui9OzWe8JptsmOt2z2%2FszV14MYBSPPKfBIp1gHTTSdicQGOKjFtUZ44Mcv3vUeoLP7xdVgueGjEQpTrMsslmzbolRYYaGY%2FsDUGTkcKRVPns7EP3%2FE1DLnS9AINBJ8pJxE%2FDLCQ4%2FLXENGpL2&X-Amz-Signature=bf1b6bd6bd71c10864f99b129900a032d51c6c2892ec83a0b92fd96859303065&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZYU2UUG3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJIMEYCIQDYl2mIH0zFB4gw98OD5OUossT5IPq%2FdLJXq%2FDJsGJiWgIhAIfIB%2F5CWji%2Ftbc5teUYwa3cvs7n1rbYUBzeb4loXQULKv8DCG8QABoMNjM3NDIzMTgzODA1IgwV2Wzu0VhrEGpvdNMq3API9Z7%2F8w3qSoRCSGBSfYjCy3JPX%2BC22McNMPkIFvkvPk9TfMQuK3%2BpdYSyZhdC%2FLy0aNJUihCg275%2Btmq%2FIOT5JJ614JVdTpt0jEFXPa8xDvQZKRx9qPBNtlaVm6Zh8obz0uSA3L%2BWuCIghkeI%2FpD5oi1nFQaN84tP%2BJjsvDKOiNj0Jpo%2FK02VQg5s2z6h3yxTZ8NtysHDMuuh099QJMv4h43%2Fz406cUy7hE%2BxVTQAd6rTigpM%2B%2BBGlOsXst6SzeHF6S9cDOIVPZnRoH8Cah7kUJsAU6EUIWAICkKR1rmwv5JS0%2Fy35xpT%2FlFOO%2BxfsmOXg5axnYlxTDraqkJ3tqxldT5yv12%2BQMvSu9i%2BklaP6Xcd%2BzIORG4Q%2FUUzLv%2BdIZ8HqXbp1QOJ3pKV%2BfNvRrWRUtkfjK%2BcAu%2FvxyrP44d2O0pevuuboYFdb6rhgtEBro7DBHqG7CMatQB5ai%2F5RpkNpPdBjxGgwI2xjLMVw3dVF%2Bbq4SAYCnDEjAmv9sX6wtnEdiyxg%2BZWMZS5rD0UM82WkUWQfLdulCKz5R8aVdNg5BX5uceBvAlAXrWuj5uZ7PQGP45T8BDSMOPB3YlZDkE4En9rGM%2BuGYKa%2B71HxR0kRcNHY0YKPLr0kZaXzzCBv5a9BjqkATY604mv1F7G3eFMkp4JzERPn5Lki%2B%2F7%2BSa0BRNsNhdKeK6CGncvFipoKX6G92XvV5hW%2BsbP1YDui9OzWe8JptsmOt2z2%2FszV14MYBSPPKfBIp1gHTTSdicQGOKjFtUZ44Mcv3vUeoLP7xdVgueGjEQpTrMsslmzbolRYYaGY%2FsDUGTkcKRVPns7EP3%2FE1DLnS9AINBJ8pJxE%2FDLCQ4%2FLXENGpL2&X-Amz-Signature=75211a40046c856031725a8b7409e93cc7946b7920320ba7e3b3cd3914238b95&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZYU2UUG3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJIMEYCIQDYl2mIH0zFB4gw98OD5OUossT5IPq%2FdLJXq%2FDJsGJiWgIhAIfIB%2F5CWji%2Ftbc5teUYwa3cvs7n1rbYUBzeb4loXQULKv8DCG8QABoMNjM3NDIzMTgzODA1IgwV2Wzu0VhrEGpvdNMq3API9Z7%2F8w3qSoRCSGBSfYjCy3JPX%2BC22McNMPkIFvkvPk9TfMQuK3%2BpdYSyZhdC%2FLy0aNJUihCg275%2Btmq%2FIOT5JJ614JVdTpt0jEFXPa8xDvQZKRx9qPBNtlaVm6Zh8obz0uSA3L%2BWuCIghkeI%2FpD5oi1nFQaN84tP%2BJjsvDKOiNj0Jpo%2FK02VQg5s2z6h3yxTZ8NtysHDMuuh099QJMv4h43%2Fz406cUy7hE%2BxVTQAd6rTigpM%2B%2BBGlOsXst6SzeHF6S9cDOIVPZnRoH8Cah7kUJsAU6EUIWAICkKR1rmwv5JS0%2Fy35xpT%2FlFOO%2BxfsmOXg5axnYlxTDraqkJ3tqxldT5yv12%2BQMvSu9i%2BklaP6Xcd%2BzIORG4Q%2FUUzLv%2BdIZ8HqXbp1QOJ3pKV%2BfNvRrWRUtkfjK%2BcAu%2FvxyrP44d2O0pevuuboYFdb6rhgtEBro7DBHqG7CMatQB5ai%2F5RpkNpPdBjxGgwI2xjLMVw3dVF%2Bbq4SAYCnDEjAmv9sX6wtnEdiyxg%2BZWMZS5rD0UM82WkUWQfLdulCKz5R8aVdNg5BX5uceBvAlAXrWuj5uZ7PQGP45T8BDSMOPB3YlZDkE4En9rGM%2BuGYKa%2B71HxR0kRcNHY0YKPLr0kZaXzzCBv5a9BjqkATY604mv1F7G3eFMkp4JzERPn5Lki%2B%2F7%2BSa0BRNsNhdKeK6CGncvFipoKX6G92XvV5hW%2BsbP1YDui9OzWe8JptsmOt2z2%2FszV14MYBSPPKfBIp1gHTTSdicQGOKjFtUZ44Mcv3vUeoLP7xdVgueGjEQpTrMsslmzbolRYYaGY%2FsDUGTkcKRVPns7EP3%2FE1DLnS9AINBJ8pJxE%2FDLCQ4%2FLXENGpL2&X-Amz-Signature=d66920ce4296e5b4d4f8a59c9f5470a88b5b9234a7077a0c3af630d950c9e328&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
