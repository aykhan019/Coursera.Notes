

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z7O4ZCO7%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041713Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC%2BHI2GhAgWtOIAkn1DWj43sj8bad4rtaWLQLrzx1XOJQIhAPpwgSFzS8HjQMm7YsJJPx6qmp%2B4zTH%2BeeNRGh2vVBOFKogECMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxliubUYcKk6P3TV4cq3APQ5JXSaaYU270OHYyBmWkvv3Q04a7DtdikNBLGfN6sp8A0EjsXGI8Ma5q3HGWwECxQGqJbRZb172YWIPcoLBmMczUpiMYrLjnvnP0fVd0aQapHTWYdD0rho2h9idh5cL%2BK0E7vhhJaHSAY0UU9%2B%2B%2BY1eUCUOb4BjHV%2BO%2BIDeKNUS0YdCV3uN46f3CfRjVGtk17ChKDvFS2RFo5XiP9xuRib6EN%2FZy8ZIHiQXbOTtRCsA7HBQ2YlTqK%2BY2MSEC2mersjhsusEEDTMSa6N%2FeU2OD9QKCOPzurmpFlpsy2WH0rslacvu7%2BhNxN61L4rG2xJlkyoGhYqFp2cC9ECdkD2lDqR%2FssPsWLbsUa0TxkgRZOgBeN69odmbu2i488HrHWgZNGcCpVxkstZ5OWHkeW4dp9ozEl8kbc2TKOJQG2Te808mftd3oY4hbDg0C8XHwtmqVxvCKepkfg1nPdVT3XT%2BesfowR3U0fF%2FVWqBFImjl9felTbHFo7m93FF61mmDX%2BUro5fDsiBZlVi%2BXe5oIOJkK2iLnAXcmoxmqRK3iXoX9gAh0a2rqpqZZpSUDnu2GnhkRzzNRIMdcsqIw9B2kk9iSbcKsZKuAGs9ewbvsAHAhzQyS275UipqsE0ryzDKpfa8BjqkASt4sVhYGVHqzB3d8xpD9w%2F9MGVrSEngnP%2FAswLDZH4DLlBDSFk3qvin%2FyEC8%2Ft9crdYamEVxW4TabGbMFt2SDMTLrDG2LmpXN7ps154cMOg%2FJkvAnkBYRrKF%2FFb0mWjagxqebe7bhr4l3C1gBnLzYyWNVezRID7Yu62abc1T%2BM%2BI5LgljG5LvpVtltDV4MPXTFi3mq0fGrhqmjacYQhg05j2ntw&X-Amz-Signature=86876a6b463f8cf84be1364f40fa37fb964f52a5531b2f0b38c71d528dbc1a8a&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z7O4ZCO7%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041712Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC%2BHI2GhAgWtOIAkn1DWj43sj8bad4rtaWLQLrzx1XOJQIhAPpwgSFzS8HjQMm7YsJJPx6qmp%2B4zTH%2BeeNRGh2vVBOFKogECMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxliubUYcKk6P3TV4cq3APQ5JXSaaYU270OHYyBmWkvv3Q04a7DtdikNBLGfN6sp8A0EjsXGI8Ma5q3HGWwECxQGqJbRZb172YWIPcoLBmMczUpiMYrLjnvnP0fVd0aQapHTWYdD0rho2h9idh5cL%2BK0E7vhhJaHSAY0UU9%2B%2B%2BY1eUCUOb4BjHV%2BO%2BIDeKNUS0YdCV3uN46f3CfRjVGtk17ChKDvFS2RFo5XiP9xuRib6EN%2FZy8ZIHiQXbOTtRCsA7HBQ2YlTqK%2BY2MSEC2mersjhsusEEDTMSa6N%2FeU2OD9QKCOPzurmpFlpsy2WH0rslacvu7%2BhNxN61L4rG2xJlkyoGhYqFp2cC9ECdkD2lDqR%2FssPsWLbsUa0TxkgRZOgBeN69odmbu2i488HrHWgZNGcCpVxkstZ5OWHkeW4dp9ozEl8kbc2TKOJQG2Te808mftd3oY4hbDg0C8XHwtmqVxvCKepkfg1nPdVT3XT%2BesfowR3U0fF%2FVWqBFImjl9felTbHFo7m93FF61mmDX%2BUro5fDsiBZlVi%2BXe5oIOJkK2iLnAXcmoxmqRK3iXoX9gAh0a2rqpqZZpSUDnu2GnhkRzzNRIMdcsqIw9B2kk9iSbcKsZKuAGs9ewbvsAHAhzQyS275UipqsE0ryzDKpfa8BjqkASt4sVhYGVHqzB3d8xpD9w%2F9MGVrSEngnP%2FAswLDZH4DLlBDSFk3qvin%2FyEC8%2Ft9crdYamEVxW4TabGbMFt2SDMTLrDG2LmpXN7ps154cMOg%2FJkvAnkBYRrKF%2FFb0mWjagxqebe7bhr4l3C1gBnLzYyWNVezRID7Yu62abc1T%2BM%2BI5LgljG5LvpVtltDV4MPXTFi3mq0fGrhqmjacYQhg05j2ntw&X-Amz-Signature=03f93bacbcdb70c7f33921ab129812a7298e136a715bc315737d005a1c2f60b3&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z7O4ZCO7%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041713Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC%2BHI2GhAgWtOIAkn1DWj43sj8bad4rtaWLQLrzx1XOJQIhAPpwgSFzS8HjQMm7YsJJPx6qmp%2B4zTH%2BeeNRGh2vVBOFKogECMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxliubUYcKk6P3TV4cq3APQ5JXSaaYU270OHYyBmWkvv3Q04a7DtdikNBLGfN6sp8A0EjsXGI8Ma5q3HGWwECxQGqJbRZb172YWIPcoLBmMczUpiMYrLjnvnP0fVd0aQapHTWYdD0rho2h9idh5cL%2BK0E7vhhJaHSAY0UU9%2B%2B%2BY1eUCUOb4BjHV%2BO%2BIDeKNUS0YdCV3uN46f3CfRjVGtk17ChKDvFS2RFo5XiP9xuRib6EN%2FZy8ZIHiQXbOTtRCsA7HBQ2YlTqK%2BY2MSEC2mersjhsusEEDTMSa6N%2FeU2OD9QKCOPzurmpFlpsy2WH0rslacvu7%2BhNxN61L4rG2xJlkyoGhYqFp2cC9ECdkD2lDqR%2FssPsWLbsUa0TxkgRZOgBeN69odmbu2i488HrHWgZNGcCpVxkstZ5OWHkeW4dp9ozEl8kbc2TKOJQG2Te808mftd3oY4hbDg0C8XHwtmqVxvCKepkfg1nPdVT3XT%2BesfowR3U0fF%2FVWqBFImjl9felTbHFo7m93FF61mmDX%2BUro5fDsiBZlVi%2BXe5oIOJkK2iLnAXcmoxmqRK3iXoX9gAh0a2rqpqZZpSUDnu2GnhkRzzNRIMdcsqIw9B2kk9iSbcKsZKuAGs9ewbvsAHAhzQyS275UipqsE0ryzDKpfa8BjqkASt4sVhYGVHqzB3d8xpD9w%2F9MGVrSEngnP%2FAswLDZH4DLlBDSFk3qvin%2FyEC8%2Ft9crdYamEVxW4TabGbMFt2SDMTLrDG2LmpXN7ps154cMOg%2FJkvAnkBYRrKF%2FFb0mWjagxqebe7bhr4l3C1gBnLzYyWNVezRID7Yu62abc1T%2BM%2BI5LgljG5LvpVtltDV4MPXTFi3mq0fGrhqmjacYQhg05j2ntw&X-Amz-Signature=bd0297ca28c8a21f15ea11855ec219336de9b6ec45e6d2063fab2cbab15d97b1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UMDPZR2P%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041713Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFqw00H%2FzxpMUyDRmWyNeDaZCfWVXWSt5O71T4b8PuMaAiEA73G7A3nOE2VfK7l7aD%2FUQ7EHoZzQdwV%2Fh8c3Nv5DM70qiAQIzP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBOoPsWz9RFGsWhcWSrcAyTqRV6IJSZd2pXOoqis%2Fsi9BQHocsxBJNIIMxE%2F7Nv4oArw2DpKsc29kgHUYAyAByalTFyJG74fdSs44MVZMQ57m3vUQ4uMDjyPzWlgKx3KVQr5COYlotSRFrHXc4fWR6d53TeI774907izCac0UHIDiZiAxMLaZEQX4nid2o654YYDEjAzetYH6YtNlfSMdzUKGWvUSpSJyU%2BzqvtMOVnFYPoMZwux7PIkt8Y3RlUJRj7WDqVhL1DPwUv8NhiqtjGG%2BC4dbIwarA9N01csuQFDjnOB8hn%2FX%2FiRsCLGEzzDONcMP0hKCiFDvkH33vf6dbnfmDhGVAoAPYlUMOb3K3nVmEKLP37s2n4BNm4NuH5XdYNoOhNKBnswip92iLzY8FNkaz7DR%2BoaXQEEF1v1hGZ7yxWogfS%2BWWCsLbM7AVtEFnvzu6FzgR0k%2B%2FqRsdfBrG8xG7LKlHAWut2TDe%2Be%2FOYtZ%2Fj9qRJdcJo0wM%2FwR0WEDpt3Aszl2z1I32IN2i5PkUgIEuR7UnpII0hQIefgTRebXTs9NPehnAk%2FtEnsxUwIK0kAWCnnz%2FG0FHYT%2BfkFMOrXGVplSw%2BE8mua2n%2FwnlRJ9vNUf08TRePs7zyDXeTmGoUAnmuythAvp6MmMKOm9rwGOqUBGfXJWWnlp3cj5s%2BWPLi11FSkgC3K7MfieUNJWsi%2FasSzWpDNTST3zYM%2BM26pQdIXXPpSyprho5L9StNuegewXpxMcfKXLLdWLF4nOhQdZ9jW5iuON8CvF5D3DUkoXFA93kgc5YYq6GLlZOLcUjyRfrlF7C39msjcdz7yBLb8JljaBc99AmgJWAktwJRw7wNylLwzOIJez%2FD9qFKP5TBksSjBcbv0&X-Amz-Signature=7b05398e25c22d027ee21ba50594da7060521c9025d5a6bb28af4c382124a295&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJLTWAKD%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041713Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDsGIaAya%2FINY6EiFSJPI6xqYmDeoFBCh55Q%2B0BoWFEBAIgCx%2B%2FsCgVv0QREzcHGy041oY8DW7znOiuT56VfDBAPqAqiAQIzP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGbNPV8%2B%2FRtJUYLXqCrcA8j2No0PiC7gZBHqoAvjH6woIE25P6836wNyV4hylnSRDbZQhY0xFaPg5yZesEWReGleemSgk%2BfUUodkJnYAB0GbhBIvwBPKoBERyLbxTy51RwYPQhHNWFJOcVbBrUJv49h1aSteuLVRqZN3rrh99hoNLayNzNlHKBkZlbz3ygjoGfW9Q7mspbaTfiNsfKUm6DqWv8gP72mzX0sGZn9cidiXiIB9CgJXhlD8IIVz2HfZE7pUP8y3SbdXQz%2FAk6KvumFinwqqVgv4MtXOudmdGEb8gCkMvdPGZgux%2BwO7k5EGR7wMys%2BHUOTmSMv7ju4k05x73kvw%2BcE92eq71lLyALzwjkbFVhtf4vPfH7vfC2y3XE6RDYxAoVK%2BZlQYSo7f%2Fl759NQ6Jvfo%2BoLF3MdoU54Bfp5F7niOjWGF83Uj7nLIXwRBdwqlOAgJDNZnlN4E%2Bb%2B8f5B2HeZ4ewG%2BevB8s7kGn4UbOJ0u%2F2V%2FMN4FNjNPGud6elcuaJFm%2Br9W5GwTQP7NTYoe6JznLcUr9Md50DysUbhjl2rnsGz%2Fua2ldIrI7YtwLANR%2FfBqm2En7ANZtvqtnpSi9lZCwyFLVmtIkjda2w2GdrMpdfYTJOSQXmMgRQJ0oRgTSm6GSTuiMMGm9rwGOqUBHTWMkuiFYZys1b7uXC5IGnGgl%2FVooWG4oKpVsyUih1Xl%2FQFlA35JgpLHSBrHgaB8fw0I3v0Ouj9RKUodbtOWkgy9r6mX2uCr5JU8dtdZV4hfu%2B3%2BwzIy1khtbr%2BIRCzatpGG6Cdcbx7Yshmpt3bpMVmOqHYdR9nRphd3vCzCXelYhUFKKqMcGoyr4qJ5vaDZ%2FsBAzVYLpUeJ%2FM0%2BxhnllPYfSvO9&X-Amz-Signature=f2ef21ac309eba61115a82d40d19fe12dc8d2c277eb7b145f447642052696e42&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z7O4ZCO7%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041713Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC%2BHI2GhAgWtOIAkn1DWj43sj8bad4rtaWLQLrzx1XOJQIhAPpwgSFzS8HjQMm7YsJJPx6qmp%2B4zTH%2BeeNRGh2vVBOFKogECMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxliubUYcKk6P3TV4cq3APQ5JXSaaYU270OHYyBmWkvv3Q04a7DtdikNBLGfN6sp8A0EjsXGI8Ma5q3HGWwECxQGqJbRZb172YWIPcoLBmMczUpiMYrLjnvnP0fVd0aQapHTWYdD0rho2h9idh5cL%2BK0E7vhhJaHSAY0UU9%2B%2B%2BY1eUCUOb4BjHV%2BO%2BIDeKNUS0YdCV3uN46f3CfRjVGtk17ChKDvFS2RFo5XiP9xuRib6EN%2FZy8ZIHiQXbOTtRCsA7HBQ2YlTqK%2BY2MSEC2mersjhsusEEDTMSa6N%2FeU2OD9QKCOPzurmpFlpsy2WH0rslacvu7%2BhNxN61L4rG2xJlkyoGhYqFp2cC9ECdkD2lDqR%2FssPsWLbsUa0TxkgRZOgBeN69odmbu2i488HrHWgZNGcCpVxkstZ5OWHkeW4dp9ozEl8kbc2TKOJQG2Te808mftd3oY4hbDg0C8XHwtmqVxvCKepkfg1nPdVT3XT%2BesfowR3U0fF%2FVWqBFImjl9felTbHFo7m93FF61mmDX%2BUro5fDsiBZlVi%2BXe5oIOJkK2iLnAXcmoxmqRK3iXoX9gAh0a2rqpqZZpSUDnu2GnhkRzzNRIMdcsqIw9B2kk9iSbcKsZKuAGs9ewbvsAHAhzQyS275UipqsE0ryzDKpfa8BjqkASt4sVhYGVHqzB3d8xpD9w%2F9MGVrSEngnP%2FAswLDZH4DLlBDSFk3qvin%2FyEC8%2Ft9crdYamEVxW4TabGbMFt2SDMTLrDG2LmpXN7ps154cMOg%2FJkvAnkBYRrKF%2FFb0mWjagxqebe7bhr4l3C1gBnLzYyWNVezRID7Yu62abc1T%2BM%2BI5LgljG5LvpVtltDV4MPXTFi3mq0fGrhqmjacYQhg05j2ntw&X-Amz-Signature=59a714afae2d038254be89647042a34908e00e5b3bfc19cc05860404167ecb98&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z7O4ZCO7%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041713Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC%2BHI2GhAgWtOIAkn1DWj43sj8bad4rtaWLQLrzx1XOJQIhAPpwgSFzS8HjQMm7YsJJPx6qmp%2B4zTH%2BeeNRGh2vVBOFKogECMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxliubUYcKk6P3TV4cq3APQ5JXSaaYU270OHYyBmWkvv3Q04a7DtdikNBLGfN6sp8A0EjsXGI8Ma5q3HGWwECxQGqJbRZb172YWIPcoLBmMczUpiMYrLjnvnP0fVd0aQapHTWYdD0rho2h9idh5cL%2BK0E7vhhJaHSAY0UU9%2B%2B%2BY1eUCUOb4BjHV%2BO%2BIDeKNUS0YdCV3uN46f3CfRjVGtk17ChKDvFS2RFo5XiP9xuRib6EN%2FZy8ZIHiQXbOTtRCsA7HBQ2YlTqK%2BY2MSEC2mersjhsusEEDTMSa6N%2FeU2OD9QKCOPzurmpFlpsy2WH0rslacvu7%2BhNxN61L4rG2xJlkyoGhYqFp2cC9ECdkD2lDqR%2FssPsWLbsUa0TxkgRZOgBeN69odmbu2i488HrHWgZNGcCpVxkstZ5OWHkeW4dp9ozEl8kbc2TKOJQG2Te808mftd3oY4hbDg0C8XHwtmqVxvCKepkfg1nPdVT3XT%2BesfowR3U0fF%2FVWqBFImjl9felTbHFo7m93FF61mmDX%2BUro5fDsiBZlVi%2BXe5oIOJkK2iLnAXcmoxmqRK3iXoX9gAh0a2rqpqZZpSUDnu2GnhkRzzNRIMdcsqIw9B2kk9iSbcKsZKuAGs9ewbvsAHAhzQyS275UipqsE0ryzDKpfa8BjqkASt4sVhYGVHqzB3d8xpD9w%2F9MGVrSEngnP%2FAswLDZH4DLlBDSFk3qvin%2FyEC8%2Ft9crdYamEVxW4TabGbMFt2SDMTLrDG2LmpXN7ps154cMOg%2FJkvAnkBYRrKF%2FFb0mWjagxqebe7bhr4l3C1gBnLzYyWNVezRID7Yu62abc1T%2BM%2BI5LgljG5LvpVtltDV4MPXTFi3mq0fGrhqmjacYQhg05j2ntw&X-Amz-Signature=518b580ca480f9ff7b90f36e7ad742920152c8709ef8812d9ad90a446ac599ea&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z7O4ZCO7%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041713Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC%2BHI2GhAgWtOIAkn1DWj43sj8bad4rtaWLQLrzx1XOJQIhAPpwgSFzS8HjQMm7YsJJPx6qmp%2B4zTH%2BeeNRGh2vVBOFKogECMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxliubUYcKk6P3TV4cq3APQ5JXSaaYU270OHYyBmWkvv3Q04a7DtdikNBLGfN6sp8A0EjsXGI8Ma5q3HGWwECxQGqJbRZb172YWIPcoLBmMczUpiMYrLjnvnP0fVd0aQapHTWYdD0rho2h9idh5cL%2BK0E7vhhJaHSAY0UU9%2B%2B%2BY1eUCUOb4BjHV%2BO%2BIDeKNUS0YdCV3uN46f3CfRjVGtk17ChKDvFS2RFo5XiP9xuRib6EN%2FZy8ZIHiQXbOTtRCsA7HBQ2YlTqK%2BY2MSEC2mersjhsusEEDTMSa6N%2FeU2OD9QKCOPzurmpFlpsy2WH0rslacvu7%2BhNxN61L4rG2xJlkyoGhYqFp2cC9ECdkD2lDqR%2FssPsWLbsUa0TxkgRZOgBeN69odmbu2i488HrHWgZNGcCpVxkstZ5OWHkeW4dp9ozEl8kbc2TKOJQG2Te808mftd3oY4hbDg0C8XHwtmqVxvCKepkfg1nPdVT3XT%2BesfowR3U0fF%2FVWqBFImjl9felTbHFo7m93FF61mmDX%2BUro5fDsiBZlVi%2BXe5oIOJkK2iLnAXcmoxmqRK3iXoX9gAh0a2rqpqZZpSUDnu2GnhkRzzNRIMdcsqIw9B2kk9iSbcKsZKuAGs9ewbvsAHAhzQyS275UipqsE0ryzDKpfa8BjqkASt4sVhYGVHqzB3d8xpD9w%2F9MGVrSEngnP%2FAswLDZH4DLlBDSFk3qvin%2FyEC8%2Ft9crdYamEVxW4TabGbMFt2SDMTLrDG2LmpXN7ps154cMOg%2FJkvAnkBYRrKF%2FFb0mWjagxqebe7bhr4l3C1gBnLzYyWNVezRID7Yu62abc1T%2BM%2BI5LgljG5LvpVtltDV4MPXTFi3mq0fGrhqmjacYQhg05j2ntw&X-Amz-Signature=3112b3af302f95af8055114d106dde4c257d453836b09cef516ebdaef921b210&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z7O4ZCO7%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041713Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC%2BHI2GhAgWtOIAkn1DWj43sj8bad4rtaWLQLrzx1XOJQIhAPpwgSFzS8HjQMm7YsJJPx6qmp%2B4zTH%2BeeNRGh2vVBOFKogECMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxliubUYcKk6P3TV4cq3APQ5JXSaaYU270OHYyBmWkvv3Q04a7DtdikNBLGfN6sp8A0EjsXGI8Ma5q3HGWwECxQGqJbRZb172YWIPcoLBmMczUpiMYrLjnvnP0fVd0aQapHTWYdD0rho2h9idh5cL%2BK0E7vhhJaHSAY0UU9%2B%2B%2BY1eUCUOb4BjHV%2BO%2BIDeKNUS0YdCV3uN46f3CfRjVGtk17ChKDvFS2RFo5XiP9xuRib6EN%2FZy8ZIHiQXbOTtRCsA7HBQ2YlTqK%2BY2MSEC2mersjhsusEEDTMSa6N%2FeU2OD9QKCOPzurmpFlpsy2WH0rslacvu7%2BhNxN61L4rG2xJlkyoGhYqFp2cC9ECdkD2lDqR%2FssPsWLbsUa0TxkgRZOgBeN69odmbu2i488HrHWgZNGcCpVxkstZ5OWHkeW4dp9ozEl8kbc2TKOJQG2Te808mftd3oY4hbDg0C8XHwtmqVxvCKepkfg1nPdVT3XT%2BesfowR3U0fF%2FVWqBFImjl9felTbHFo7m93FF61mmDX%2BUro5fDsiBZlVi%2BXe5oIOJkK2iLnAXcmoxmqRK3iXoX9gAh0a2rqpqZZpSUDnu2GnhkRzzNRIMdcsqIw9B2kk9iSbcKsZKuAGs9ewbvsAHAhzQyS275UipqsE0ryzDKpfa8BjqkASt4sVhYGVHqzB3d8xpD9w%2F9MGVrSEngnP%2FAswLDZH4DLlBDSFk3qvin%2FyEC8%2Ft9crdYamEVxW4TabGbMFt2SDMTLrDG2LmpXN7ps154cMOg%2FJkvAnkBYRrKF%2FFb0mWjagxqebe7bhr4l3C1gBnLzYyWNVezRID7Yu62abc1T%2BM%2BI5LgljG5LvpVtltDV4MPXTFi3mq0fGrhqmjacYQhg05j2ntw&X-Amz-Signature=bdc3e074070e7c7ccbd99878ba9c7618cbb37463042b48c4713ef2d6af8943ac&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
