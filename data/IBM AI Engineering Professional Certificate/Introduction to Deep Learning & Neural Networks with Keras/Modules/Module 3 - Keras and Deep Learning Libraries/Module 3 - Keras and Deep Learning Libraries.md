

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVFFV7VV%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIClJSucCdYGpkv2ZiWRZJ7g18jVESytqkxwLxKNChhVVAiBylS%2FqELoWGrYg9R0yMzj3slzT6%2FMQph%2BWA69V1g7jnSr%2FAwghEAAaDDYzNzQyMzE4MzgwNSIMmYWvOiQuehInLSO9KtwDZavVCHWP01vC6dfgYnoYRJI2qcr2WTX9CS4O7RpTompDIrPMFq2rzX5ywm9e69VlU46JjwSDFfxX9roC6iE7ELMEern3L3iR%2FCgGG%2B5KuHnklgIWUGTkvlpHfhCKsQ25ZOdH8HdYgCVLFX7DHlJrEml12YJ9%2FF62fBq4Te0Upq1whba9Zn2Mqk2a%2BmV2fGqycCCN78g7vgoeznrbLRHR6xanDLrWP6MtNXA0VKOOl4RtIaaD5CUvKGFWO8RJX0B%2FrJ2tSiUlY%2Fql8Ix2cE5JbG%2BpCeegTf7%2BigUmNqquk%2FAL4WYocqDdlEUlSlUJ9jEkBLZqnLdc7bcStCkBUFe62kS8aEjmJWva%2Fey5swJB8uFkTdCaj5U%2FVbupIZynGpFiuYvFoNJpgyN19%2FonUW5jtlePZEzisD3HJ7W6k21nrettyyBC8M%2BSjtrZ4KGJcse8o8WQsU0YmNNN9ldGtxG7wtOu2BZgsCZkOIMHZIRqbhQ9hZhvJlOk1zpneSO161tD%2FX5n7WKm2FW4vY9mfPBOIaSQEjXUhT6BC5oRV6H98xb2Nlg%2B7yohshhNibNxJSnsQoCA9tFo08%2BLiFSPQtGLefl%2FTFjNJH4eXmdo9W%2BQbDCFgKGxfA8rvntwJ7Iw6KLYvgY6pgF4PcNJdJ1K9GBQXi512LEtGNqvet%2B9CEyTvugnup6lXe5E7xEG02H0k9xQrhcAOK1p8GJCWoDaHuCbXSFWKyex%2Bs6C1KNF93C2dG5rzLSw2mHObJNI%2BV%2B0l5AshMzm%2Bx7pIOmmj6NsSho4ZPMOB0ONbJt1eIc9Jl5Qr8t%2BBjql5v1FnTy8m5V6cudUBn2bJFVPAEe%2Fj1Hj0wkfPjfelt6QIjresnw3&X-Amz-Signature=16c1cea5cb25962958a2326b09d5a8cb3db07f2dbc0aa7cb8190727fc8fffb3d&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVFFV7VV%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIClJSucCdYGpkv2ZiWRZJ7g18jVESytqkxwLxKNChhVVAiBylS%2FqELoWGrYg9R0yMzj3slzT6%2FMQph%2BWA69V1g7jnSr%2FAwghEAAaDDYzNzQyMzE4MzgwNSIMmYWvOiQuehInLSO9KtwDZavVCHWP01vC6dfgYnoYRJI2qcr2WTX9CS4O7RpTompDIrPMFq2rzX5ywm9e69VlU46JjwSDFfxX9roC6iE7ELMEern3L3iR%2FCgGG%2B5KuHnklgIWUGTkvlpHfhCKsQ25ZOdH8HdYgCVLFX7DHlJrEml12YJ9%2FF62fBq4Te0Upq1whba9Zn2Mqk2a%2BmV2fGqycCCN78g7vgoeznrbLRHR6xanDLrWP6MtNXA0VKOOl4RtIaaD5CUvKGFWO8RJX0B%2FrJ2tSiUlY%2Fql8Ix2cE5JbG%2BpCeegTf7%2BigUmNqquk%2FAL4WYocqDdlEUlSlUJ9jEkBLZqnLdc7bcStCkBUFe62kS8aEjmJWva%2Fey5swJB8uFkTdCaj5U%2FVbupIZynGpFiuYvFoNJpgyN19%2FonUW5jtlePZEzisD3HJ7W6k21nrettyyBC8M%2BSjtrZ4KGJcse8o8WQsU0YmNNN9ldGtxG7wtOu2BZgsCZkOIMHZIRqbhQ9hZhvJlOk1zpneSO161tD%2FX5n7WKm2FW4vY9mfPBOIaSQEjXUhT6BC5oRV6H98xb2Nlg%2B7yohshhNibNxJSnsQoCA9tFo08%2BLiFSPQtGLefl%2FTFjNJH4eXmdo9W%2BQbDCFgKGxfA8rvntwJ7Iw6KLYvgY6pgF4PcNJdJ1K9GBQXi512LEtGNqvet%2B9CEyTvugnup6lXe5E7xEG02H0k9xQrhcAOK1p8GJCWoDaHuCbXSFWKyex%2Bs6C1KNF93C2dG5rzLSw2mHObJNI%2BV%2B0l5AshMzm%2Bx7pIOmmj6NsSho4ZPMOB0ONbJt1eIc9Jl5Qr8t%2BBjql5v1FnTy8m5V6cudUBn2bJFVPAEe%2Fj1Hj0wkfPjfelt6QIjresnw3&X-Amz-Signature=6f807573280ba7143b90e52939d374023af0b891a735311f0731b4ac7bb12020&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVFFV7VV%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIClJSucCdYGpkv2ZiWRZJ7g18jVESytqkxwLxKNChhVVAiBylS%2FqELoWGrYg9R0yMzj3slzT6%2FMQph%2BWA69V1g7jnSr%2FAwghEAAaDDYzNzQyMzE4MzgwNSIMmYWvOiQuehInLSO9KtwDZavVCHWP01vC6dfgYnoYRJI2qcr2WTX9CS4O7RpTompDIrPMFq2rzX5ywm9e69VlU46JjwSDFfxX9roC6iE7ELMEern3L3iR%2FCgGG%2B5KuHnklgIWUGTkvlpHfhCKsQ25ZOdH8HdYgCVLFX7DHlJrEml12YJ9%2FF62fBq4Te0Upq1whba9Zn2Mqk2a%2BmV2fGqycCCN78g7vgoeznrbLRHR6xanDLrWP6MtNXA0VKOOl4RtIaaD5CUvKGFWO8RJX0B%2FrJ2tSiUlY%2Fql8Ix2cE5JbG%2BpCeegTf7%2BigUmNqquk%2FAL4WYocqDdlEUlSlUJ9jEkBLZqnLdc7bcStCkBUFe62kS8aEjmJWva%2Fey5swJB8uFkTdCaj5U%2FVbupIZynGpFiuYvFoNJpgyN19%2FonUW5jtlePZEzisD3HJ7W6k21nrettyyBC8M%2BSjtrZ4KGJcse8o8WQsU0YmNNN9ldGtxG7wtOu2BZgsCZkOIMHZIRqbhQ9hZhvJlOk1zpneSO161tD%2FX5n7WKm2FW4vY9mfPBOIaSQEjXUhT6BC5oRV6H98xb2Nlg%2B7yohshhNibNxJSnsQoCA9tFo08%2BLiFSPQtGLefl%2FTFjNJH4eXmdo9W%2BQbDCFgKGxfA8rvntwJ7Iw6KLYvgY6pgF4PcNJdJ1K9GBQXi512LEtGNqvet%2B9CEyTvugnup6lXe5E7xEG02H0k9xQrhcAOK1p8GJCWoDaHuCbXSFWKyex%2Bs6C1KNF93C2dG5rzLSw2mHObJNI%2BV%2B0l5AshMzm%2Bx7pIOmmj6NsSho4ZPMOB0ONbJt1eIc9Jl5Qr8t%2BBjql5v1FnTy8m5V6cudUBn2bJFVPAEe%2Fj1Hj0wkfPjfelt6QIjresnw3&X-Amz-Signature=13ac3d43a4407b4098fa4ddf551fd89ee23fbe7a67c05f43dee3a7bc635fd1dd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZWOM7ITW%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCg2GXDMweX9qFkbdeM91ZxdZfyuqE8NtkyC%2FxqZbplGQIhAOVmghn17KoII9akT6bU9wiUU5YkfGJgxnVKrioegNR7Kv8DCCAQABoMNjM3NDIzMTgzODA1IgwRvoSec5c3AwbyDKQq3APJCZQhmJK5ekhlfWep8JsgCkIKHCd4ThkEzIrzINp6V%2FRF30Kn6KEtCnT7xBNbOBsrBdW%2BblgZUcYS19Go5iBknCX1qXE2aQDX4aJSOE50GOD4C5uahG9Vcn%2BQ6c781SnY5mMM9v7SpzWGiqRZxHSWj4KpPcd6PzhJ1M4FAxEpe%2FGh8QFmsikuj945KWbS%2B54aM10fXeCUptwEk4X78SWRUs5GCohG1N0%2FUyNYcM1FJv5UML%2BmIYJ%2FddZxRDVfto9WEMX%2FZKpq3uw9kpN6VA2hjGJ7ErBp1N2d%2Fsn1wtt1HcJmiGPObhCs0zEMXqE8CJzK8Yd7fbWAfd69bhOGL3BzsqgttywmEA7JFBphmm1pYAh%2FLQKQcPZLZeG9eJbv6wwJNpSzyjnl%2BnGN%2FyRtgojBDefKv%2ByJOkaeaEcaC5V8xaWqy4n7ViD0p9ntN2yRh2wrV9tq3cjJQ6RW6obICxiIMmrl2WsMaa50HvPimuhB5MYVlJp0YRWksRDqTox%2BPSzL2tLZcQnvzE9%2BfiruqOfCY1u47PiqVM%2Bcp2FW38RthpUn8nBqdAmC3Dz8101cVfkBhNXpi%2ByRYwLXs3QVbmBMr1NLnwYRd%2FwgkqfyTukAzYt0TSvVytjDwnysCzDi%2F9e%2BBjqkAeAf1X8kBB7yPROoCfrFKkY8pLgwDhLvHs1nI%2BkU435SZ2WKKE3LKFvzIIqIstKzB77s6R%2F2%2BQfxEKl7QuQQcj83TDl%2FUfXbEXg6YKq1fu1D7yqJyVRvQufZGkpauKZt7iHgRRRDjh%2Bbo4NsIHWFzZbfNN9Ibxa2uVJJT8zOxHOaum%2FlDd%2F%2B%2BNkudhGmrb7g5wA7XTjK4aVT7ApHoCtJxj11ayCH&X-Amz-Signature=956b4b316f40288e7bc60f1a5a2c0dcc9b51a443e3b323c6f4287a284ee8a751&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOSDVC4F%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCNDpJvZgR%2F3gNpa6nA8EV%2Fs3YM84aiiWhtUHlmyJt7BwIhAJq3ZS5Ap9DlsTLY0bcw36NlKFqA0HS0KsIwC64g7imgKv8DCB8QABoMNjM3NDIzMTgzODA1IgwgSGOkgdvNVaR0iBYq3AMf8TS0TegzoFUHxvw3Zyl94FCoaAW0uvu0Hy1K9P3MLsSOe0t1mW1r53ZOGiE7oR1yjZKt%2B8suGfcwnVt6pep619xI5woLKD%2FqHKH4sqMnAFpUkFV56kNWS0OYDAITmSEXentzEpuWemSNUHoD2iLbqP7WmweAu6%2FrA2ghddwJpkvAnavVt6A9gqr74S8EmhBPNCscnQNb1viegozt4RklrrZIt9yYIufn1G1sXsXUayBS30bqifaVSsVw%2Bx0aksnlxisXo%2FOKGm7FJ4pCDYuQGV5hrNR%2FzP9Ww1MXdPcZfV4mpN1Q41NZeGsK2VOu5O3g%2BRYYObNpcO%2F5%2B%2BAMByOnYPFSQRyxUc9E8uSo8ZOz0e7woVkYkx2817S8oE0%2BHXQILw914VK63N7TSa126vl47U%2BU3yQWlLpteKT7tRM0f%2FnYMmlG4qEV%2BH0Mgp5VFweiF6AaGO3omuPDJi6Apw08Y3oacMWq6kHAhLXghMwQ%2FWc6rEloDLuJz8Tcacbp58%2F%2Fe7DxddzC1c0vp3gT7Av7cxiuWmhpafj7rEPyBeLUdPAvHo8YiQW7sZIi4g7aFvXCTtR6OTLX%2FR2rQ9gKPugQ3xtENzkd%2BxWJl1f64bS0JSL9oTKi50ZY1Tf5fzC0%2F9e%2BBjqkAe9it1ya5KJavRH%2BV6VPf39dPEYk391BtZDD5EuMdtn9LSUU7kFU1FODJ3Aoyw2GDbJb1aGpeo1%2BHuCrQOISNMGKgW%2FBdAYoLwTulW2OVEaQ2vfTo%2BTF2XbZC5yEQh3SzbJy9%2FROI8xnTiFgvntT%2FskHJRbCp91MazXGbj9zqquGdq064aFAU31BOPs6r4lV0ViIFj6p5ffeeBO9xLjA14g9R24o&X-Amz-Signature=cedff51dad648a56f10b6865e3ee4f138dda5fb5c8cfdb7191522bf3247f57c3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVFFV7VV%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIClJSucCdYGpkv2ZiWRZJ7g18jVESytqkxwLxKNChhVVAiBylS%2FqELoWGrYg9R0yMzj3slzT6%2FMQph%2BWA69V1g7jnSr%2FAwghEAAaDDYzNzQyMzE4MzgwNSIMmYWvOiQuehInLSO9KtwDZavVCHWP01vC6dfgYnoYRJI2qcr2WTX9CS4O7RpTompDIrPMFq2rzX5ywm9e69VlU46JjwSDFfxX9roC6iE7ELMEern3L3iR%2FCgGG%2B5KuHnklgIWUGTkvlpHfhCKsQ25ZOdH8HdYgCVLFX7DHlJrEml12YJ9%2FF62fBq4Te0Upq1whba9Zn2Mqk2a%2BmV2fGqycCCN78g7vgoeznrbLRHR6xanDLrWP6MtNXA0VKOOl4RtIaaD5CUvKGFWO8RJX0B%2FrJ2tSiUlY%2Fql8Ix2cE5JbG%2BpCeegTf7%2BigUmNqquk%2FAL4WYocqDdlEUlSlUJ9jEkBLZqnLdc7bcStCkBUFe62kS8aEjmJWva%2Fey5swJB8uFkTdCaj5U%2FVbupIZynGpFiuYvFoNJpgyN19%2FonUW5jtlePZEzisD3HJ7W6k21nrettyyBC8M%2BSjtrZ4KGJcse8o8WQsU0YmNNN9ldGtxG7wtOu2BZgsCZkOIMHZIRqbhQ9hZhvJlOk1zpneSO161tD%2FX5n7WKm2FW4vY9mfPBOIaSQEjXUhT6BC5oRV6H98xb2Nlg%2B7yohshhNibNxJSnsQoCA9tFo08%2BLiFSPQtGLefl%2FTFjNJH4eXmdo9W%2BQbDCFgKGxfA8rvntwJ7Iw6KLYvgY6pgF4PcNJdJ1K9GBQXi512LEtGNqvet%2B9CEyTvugnup6lXe5E7xEG02H0k9xQrhcAOK1p8GJCWoDaHuCbXSFWKyex%2Bs6C1KNF93C2dG5rzLSw2mHObJNI%2BV%2B0l5AshMzm%2Bx7pIOmmj6NsSho4ZPMOB0ONbJt1eIc9Jl5Qr8t%2BBjql5v1FnTy8m5V6cudUBn2bJFVPAEe%2Fj1Hj0wkfPjfelt6QIjresnw3&X-Amz-Signature=598d0c1bf9a2967eeb06aee861590d85f5d2d8022d34ca43e005f1940577d008&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVFFV7VV%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIClJSucCdYGpkv2ZiWRZJ7g18jVESytqkxwLxKNChhVVAiBylS%2FqELoWGrYg9R0yMzj3slzT6%2FMQph%2BWA69V1g7jnSr%2FAwghEAAaDDYzNzQyMzE4MzgwNSIMmYWvOiQuehInLSO9KtwDZavVCHWP01vC6dfgYnoYRJI2qcr2WTX9CS4O7RpTompDIrPMFq2rzX5ywm9e69VlU46JjwSDFfxX9roC6iE7ELMEern3L3iR%2FCgGG%2B5KuHnklgIWUGTkvlpHfhCKsQ25ZOdH8HdYgCVLFX7DHlJrEml12YJ9%2FF62fBq4Te0Upq1whba9Zn2Mqk2a%2BmV2fGqycCCN78g7vgoeznrbLRHR6xanDLrWP6MtNXA0VKOOl4RtIaaD5CUvKGFWO8RJX0B%2FrJ2tSiUlY%2Fql8Ix2cE5JbG%2BpCeegTf7%2BigUmNqquk%2FAL4WYocqDdlEUlSlUJ9jEkBLZqnLdc7bcStCkBUFe62kS8aEjmJWva%2Fey5swJB8uFkTdCaj5U%2FVbupIZynGpFiuYvFoNJpgyN19%2FonUW5jtlePZEzisD3HJ7W6k21nrettyyBC8M%2BSjtrZ4KGJcse8o8WQsU0YmNNN9ldGtxG7wtOu2BZgsCZkOIMHZIRqbhQ9hZhvJlOk1zpneSO161tD%2FX5n7WKm2FW4vY9mfPBOIaSQEjXUhT6BC5oRV6H98xb2Nlg%2B7yohshhNibNxJSnsQoCA9tFo08%2BLiFSPQtGLefl%2FTFjNJH4eXmdo9W%2BQbDCFgKGxfA8rvntwJ7Iw6KLYvgY6pgF4PcNJdJ1K9GBQXi512LEtGNqvet%2B9CEyTvugnup6lXe5E7xEG02H0k9xQrhcAOK1p8GJCWoDaHuCbXSFWKyex%2Bs6C1KNF93C2dG5rzLSw2mHObJNI%2BV%2B0l5AshMzm%2Bx7pIOmmj6NsSho4ZPMOB0ONbJt1eIc9Jl5Qr8t%2BBjql5v1FnTy8m5V6cudUBn2bJFVPAEe%2Fj1Hj0wkfPjfelt6QIjresnw3&X-Amz-Signature=63fe6e83e9c5a83ba5f62e0344955bf85384eaac84d1b5d0d1eb1ef60d1cbf22&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVFFV7VV%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIClJSucCdYGpkv2ZiWRZJ7g18jVESytqkxwLxKNChhVVAiBylS%2FqELoWGrYg9R0yMzj3slzT6%2FMQph%2BWA69V1g7jnSr%2FAwghEAAaDDYzNzQyMzE4MzgwNSIMmYWvOiQuehInLSO9KtwDZavVCHWP01vC6dfgYnoYRJI2qcr2WTX9CS4O7RpTompDIrPMFq2rzX5ywm9e69VlU46JjwSDFfxX9roC6iE7ELMEern3L3iR%2FCgGG%2B5KuHnklgIWUGTkvlpHfhCKsQ25ZOdH8HdYgCVLFX7DHlJrEml12YJ9%2FF62fBq4Te0Upq1whba9Zn2Mqk2a%2BmV2fGqycCCN78g7vgoeznrbLRHR6xanDLrWP6MtNXA0VKOOl4RtIaaD5CUvKGFWO8RJX0B%2FrJ2tSiUlY%2Fql8Ix2cE5JbG%2BpCeegTf7%2BigUmNqquk%2FAL4WYocqDdlEUlSlUJ9jEkBLZqnLdc7bcStCkBUFe62kS8aEjmJWva%2Fey5swJB8uFkTdCaj5U%2FVbupIZynGpFiuYvFoNJpgyN19%2FonUW5jtlePZEzisD3HJ7W6k21nrettyyBC8M%2BSjtrZ4KGJcse8o8WQsU0YmNNN9ldGtxG7wtOu2BZgsCZkOIMHZIRqbhQ9hZhvJlOk1zpneSO161tD%2FX5n7WKm2FW4vY9mfPBOIaSQEjXUhT6BC5oRV6H98xb2Nlg%2B7yohshhNibNxJSnsQoCA9tFo08%2BLiFSPQtGLefl%2FTFjNJH4eXmdo9W%2BQbDCFgKGxfA8rvntwJ7Iw6KLYvgY6pgF4PcNJdJ1K9GBQXi512LEtGNqvet%2B9CEyTvugnup6lXe5E7xEG02H0k9xQrhcAOK1p8GJCWoDaHuCbXSFWKyex%2Bs6C1KNF93C2dG5rzLSw2mHObJNI%2BV%2B0l5AshMzm%2Bx7pIOmmj6NsSho4ZPMOB0ONbJt1eIc9Jl5Qr8t%2BBjql5v1FnTy8m5V6cudUBn2bJFVPAEe%2Fj1Hj0wkfPjfelt6QIjresnw3&X-Amz-Signature=40bfbd6beacd2dc1d4a2c728a1ea0615c77c50a17ceabe04ed1b2799f097caf2&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVFFV7VV%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIClJSucCdYGpkv2ZiWRZJ7g18jVESytqkxwLxKNChhVVAiBylS%2FqELoWGrYg9R0yMzj3slzT6%2FMQph%2BWA69V1g7jnSr%2FAwghEAAaDDYzNzQyMzE4MzgwNSIMmYWvOiQuehInLSO9KtwDZavVCHWP01vC6dfgYnoYRJI2qcr2WTX9CS4O7RpTompDIrPMFq2rzX5ywm9e69VlU46JjwSDFfxX9roC6iE7ELMEern3L3iR%2FCgGG%2B5KuHnklgIWUGTkvlpHfhCKsQ25ZOdH8HdYgCVLFX7DHlJrEml12YJ9%2FF62fBq4Te0Upq1whba9Zn2Mqk2a%2BmV2fGqycCCN78g7vgoeznrbLRHR6xanDLrWP6MtNXA0VKOOl4RtIaaD5CUvKGFWO8RJX0B%2FrJ2tSiUlY%2Fql8Ix2cE5JbG%2BpCeegTf7%2BigUmNqquk%2FAL4WYocqDdlEUlSlUJ9jEkBLZqnLdc7bcStCkBUFe62kS8aEjmJWva%2Fey5swJB8uFkTdCaj5U%2FVbupIZynGpFiuYvFoNJpgyN19%2FonUW5jtlePZEzisD3HJ7W6k21nrettyyBC8M%2BSjtrZ4KGJcse8o8WQsU0YmNNN9ldGtxG7wtOu2BZgsCZkOIMHZIRqbhQ9hZhvJlOk1zpneSO161tD%2FX5n7WKm2FW4vY9mfPBOIaSQEjXUhT6BC5oRV6H98xb2Nlg%2B7yohshhNibNxJSnsQoCA9tFo08%2BLiFSPQtGLefl%2FTFjNJH4eXmdo9W%2BQbDCFgKGxfA8rvntwJ7Iw6KLYvgY6pgF4PcNJdJ1K9GBQXi512LEtGNqvet%2B9CEyTvugnup6lXe5E7xEG02H0k9xQrhcAOK1p8GJCWoDaHuCbXSFWKyex%2Bs6C1KNF93C2dG5rzLSw2mHObJNI%2BV%2B0l5AshMzm%2Bx7pIOmmj6NsSho4ZPMOB0ONbJt1eIc9Jl5Qr8t%2BBjql5v1FnTy8m5V6cudUBn2bJFVPAEe%2Fj1Hj0wkfPjfelt6QIjresnw3&X-Amz-Signature=b7974d07d030b62f327c423a1203c0a031231482dc0c904fc9583ed2b66851dd&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
