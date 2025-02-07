

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ASY3JKS%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIFoveM2EHqkY6O6R6ZBAuo8PvK6jp1R1Yq4YcfPsAkxfAiEAoiBzMOZMe4NvzuZx0VBai8vQyHGFp11HS7NyF7Oohvkq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDGs2GeWsIuAC76VBsircA7QyN8djg%2BLuY9BjagJOzUlx%2B%2BdyppqdSGRrGiNFR7DeRc%2Bmw3tta6L3%2FyC3fvWUu%2BQgzIKP0LtCX9HGiqIhTkpuWC2DAc9CTON1y9a0A%2F5jDe3agbc1oqkJ5%2F46jcCSNKD5HxnMkqbWe0flp4ARpIk9ayvcz6EKwL2erbIUnqfdfDD3PqCjIfDqU1FjULaKw14P9vvXVF%2FHFkBor8pF3HDZUtXjdaHSmXAdu7pj700P%2Ba%2FbUs1rBStr3OmI2ECFsmRWH%2FGZVHzhHo8JVCbZALKaD3aT6RhHZyQrb6RZrtzsMNB1K0aW0%2F2PG4kT5G3LHetI8gvQTEckyFS7kj105oD%2FCgqqdPh2MWlG3aRnE%2FRaWGy2buuRAopRFd7O%2F4xoAF2kN94DqgcnQqJbodNsGlTDCaX5Gd%2FsN44hDbv9mv5CyIfBj6XsqEGcPm%2FK15EJdUDudFnerJSsdFr8Vp5doUqVRT8rOVJvUj188NOf4oLUuGUb3AwyuvxfT2azLW3j0qlHfEeYzQWdROdYmyaqk9mz5xkE7VwP9JuZ9jQzsS9w8JMMdntg%2BX6Duy41y1Dh8fDfdq5PzEXz3trf%2Bwi%2F2LsMzqAnWbEAnLzed2%2FzQwommyaHmYsOA%2FKNXfwVMNH%2Bmb0GOqUB%2F1jaQm1hCXeb8cuIOEM49f2tbkTDg6ej8hWKXDF%2FxEpA6Fvhw6fQGtY%2F9fKZ1JFoPXUWbuMcqIWRuN1we%2FyCGZJkXPLtDfXA3J95zX3K3DjNLwpthYdet3quKZUTv142%2FCWkP3ZouTrZ6CiSJyBh1XR9%2BGwAiZT5PHujfNu96BLPPfYVTc0gQspyutypTgIqeGrLDzNkJV0dPe723xVGaTdrh%2Fz9&X-Amz-Signature=b705dd14dab154c82ddbcf2e201cdc4d659c9901b4e5ee20383c4334c328b0b2&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ASY3JKS%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIFoveM2EHqkY6O6R6ZBAuo8PvK6jp1R1Yq4YcfPsAkxfAiEAoiBzMOZMe4NvzuZx0VBai8vQyHGFp11HS7NyF7Oohvkq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDGs2GeWsIuAC76VBsircA7QyN8djg%2BLuY9BjagJOzUlx%2B%2BdyppqdSGRrGiNFR7DeRc%2Bmw3tta6L3%2FyC3fvWUu%2BQgzIKP0LtCX9HGiqIhTkpuWC2DAc9CTON1y9a0A%2F5jDe3agbc1oqkJ5%2F46jcCSNKD5HxnMkqbWe0flp4ARpIk9ayvcz6EKwL2erbIUnqfdfDD3PqCjIfDqU1FjULaKw14P9vvXVF%2FHFkBor8pF3HDZUtXjdaHSmXAdu7pj700P%2Ba%2FbUs1rBStr3OmI2ECFsmRWH%2FGZVHzhHo8JVCbZALKaD3aT6RhHZyQrb6RZrtzsMNB1K0aW0%2F2PG4kT5G3LHetI8gvQTEckyFS7kj105oD%2FCgqqdPh2MWlG3aRnE%2FRaWGy2buuRAopRFd7O%2F4xoAF2kN94DqgcnQqJbodNsGlTDCaX5Gd%2FsN44hDbv9mv5CyIfBj6XsqEGcPm%2FK15EJdUDudFnerJSsdFr8Vp5doUqVRT8rOVJvUj188NOf4oLUuGUb3AwyuvxfT2azLW3j0qlHfEeYzQWdROdYmyaqk9mz5xkE7VwP9JuZ9jQzsS9w8JMMdntg%2BX6Duy41y1Dh8fDfdq5PzEXz3trf%2Bwi%2F2LsMzqAnWbEAnLzed2%2FzQwommyaHmYsOA%2FKNXfwVMNH%2Bmb0GOqUB%2F1jaQm1hCXeb8cuIOEM49f2tbkTDg6ej8hWKXDF%2FxEpA6Fvhw6fQGtY%2F9fKZ1JFoPXUWbuMcqIWRuN1we%2FyCGZJkXPLtDfXA3J95zX3K3DjNLwpthYdet3quKZUTv142%2FCWkP3ZouTrZ6CiSJyBh1XR9%2BGwAiZT5PHujfNu96BLPPfYVTc0gQspyutypTgIqeGrLDzNkJV0dPe723xVGaTdrh%2Fz9&X-Amz-Signature=fc7f3a1f963ec58e26c2c35b5a17dbc45bfc940503f0f0574c3fe42c34af646e&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ASY3JKS%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIFoveM2EHqkY6O6R6ZBAuo8PvK6jp1R1Yq4YcfPsAkxfAiEAoiBzMOZMe4NvzuZx0VBai8vQyHGFp11HS7NyF7Oohvkq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDGs2GeWsIuAC76VBsircA7QyN8djg%2BLuY9BjagJOzUlx%2B%2BdyppqdSGRrGiNFR7DeRc%2Bmw3tta6L3%2FyC3fvWUu%2BQgzIKP0LtCX9HGiqIhTkpuWC2DAc9CTON1y9a0A%2F5jDe3agbc1oqkJ5%2F46jcCSNKD5HxnMkqbWe0flp4ARpIk9ayvcz6EKwL2erbIUnqfdfDD3PqCjIfDqU1FjULaKw14P9vvXVF%2FHFkBor8pF3HDZUtXjdaHSmXAdu7pj700P%2Ba%2FbUs1rBStr3OmI2ECFsmRWH%2FGZVHzhHo8JVCbZALKaD3aT6RhHZyQrb6RZrtzsMNB1K0aW0%2F2PG4kT5G3LHetI8gvQTEckyFS7kj105oD%2FCgqqdPh2MWlG3aRnE%2FRaWGy2buuRAopRFd7O%2F4xoAF2kN94DqgcnQqJbodNsGlTDCaX5Gd%2FsN44hDbv9mv5CyIfBj6XsqEGcPm%2FK15EJdUDudFnerJSsdFr8Vp5doUqVRT8rOVJvUj188NOf4oLUuGUb3AwyuvxfT2azLW3j0qlHfEeYzQWdROdYmyaqk9mz5xkE7VwP9JuZ9jQzsS9w8JMMdntg%2BX6Duy41y1Dh8fDfdq5PzEXz3trf%2Bwi%2F2LsMzqAnWbEAnLzed2%2FzQwommyaHmYsOA%2FKNXfwVMNH%2Bmb0GOqUB%2F1jaQm1hCXeb8cuIOEM49f2tbkTDg6ej8hWKXDF%2FxEpA6Fvhw6fQGtY%2F9fKZ1JFoPXUWbuMcqIWRuN1we%2FyCGZJkXPLtDfXA3J95zX3K3DjNLwpthYdet3quKZUTv142%2FCWkP3ZouTrZ6CiSJyBh1XR9%2BGwAiZT5PHujfNu96BLPPfYVTc0gQspyutypTgIqeGrLDzNkJV0dPe723xVGaTdrh%2Fz9&X-Amz-Signature=add9e3092b5142e8495fe2aecbab3dda5cb67635f16f837bb2b7231c10f11d41&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663IVB3RTP%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJGMEQCIBmI8AFKqCO1pZeIQ3oKQaFIsNeLlLsLBjDGw6npe5L4AiAoYxmlrIskDc8nHzKuLou8WIXJpizs6lrjE14AMBxfiCr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMkamTMsZi3I8c%2FtxQKtwDgSUtnSSKU5iXup2h8iJFR9Yl3iWd7I%2FORjfoWCu8zsub9gQQRx8mb4JtXzKCjgUJShRGsvwy11Qg%2BYBb071czvTR8xjYF6EV%2BUQpNIbmmmCuuS4YoJ8e7%2B%2BkieclUXOtzVpTCpSDtCsG2X36%2BeCCtXgOhSym4AmhxGt8NX3v9ZRnUUqVIkQbWy5nCSweO9cVoxF6%2F395%2B%2B1V2KFEoyQ%2BqMHsXy4GZLZbr2Kio6i2k99yxoMxG0v4Lx7HSw7wMfEtjqTLLDcqslje252kIqL3EAZN4GRCW1zFJuBMZsYyhimZI%2Fcl83rcN5tDyoTlf6VKpPXgxvENvy3vYsHwlldDkUlYFh1Xh3w6JJmAT%2BS83GpNxm%2Fdwwe00K8EXtiSTaHpE205s6nky1MuTL3f748iu%2FT7kzRicIOsInmPLTlSWyImxVkWzw9xXpqgHzCu37JJw%2F0aBl%2FEubzhnVYd6G6AMzgq6YkPqjd6IWQ2CflAwVNn4yebswGncRbKa8hxisqnsMAhHvjW86NL1xXizxaBuPPGBhrCAcTjEd8PRfN%2Fk1Bo%2BK41lHtjksMb9%2B4LUqPejbXSutkg22CkS%2FZOAK1agIRyYCp2fGjHe1GIGhxv4gwyX0UILrGUDZ0YVe4wyv6ZvQY6pgEFK3xPJcBaW1piBW86HQahqwCH7%2BfKawnj8T5xbaTuyDZ3HFFC7HlQhFGJjbXyQCszSLWoE98OjW5X3nfYFVWaNgdmilp4T6QejUAQwMjzoqN64fNnOmud3fLd79W2TJT9xT91V1MTkIvJIYIYCwoiX10Qv8BuKpX4Tv0OwcEcyuDZgIt6CTcr3O1mAWfENt%2F%2B0QDFMGC%2FXuM%2BkbClCn5Ix7ScmviZ&X-Amz-Signature=a590237bd368b1ab97815f4bffee56d6166e302de3f5f2f23bc48e0a151f1128&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667S246YKM%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJIMEYCIQDES1%2Fgdtl9pN7YepX82H3Hc1e3jJez7zizZoTO096SjgIhAJOPvj%2BBcz1kipOZVU0COyINBB8bYzzwcWRNHsGgZzHpKv8DCH8QABoMNjM3NDIzMTgzODA1IgwGsW61KM%2BpRwIZZuAq3AOuUVc23gLOrz%2FljC1H0Im9wicpJDCUHzZ8EPOHtFfGmtDXrn94cWfYzvjhuOoKC7tDJtPQW4HXJBhhMyjvOzipm1OMtJPYR%2FckgMorFasCLV3Oe94XjbFuCuuByYoFiyOJGxmXFEh51lTDC8GRtZiyz9Lc7rFmTboeHt7VJWudcckiVGTzM1wb50Jb8EH4lGk5L%2B0PkGrxkVI2Xd4QGzoTcbpDEd%2FWiexSyf5B5mSVzo1wiaJyrothgPWJmyjeqIeDPg3KCLUFpF8sYcC1XzZpixP905dI4EMPHabihY7uatqI2QG7zSm3ltemyd86VW%2B%2FUYx5cnurVSU8loIarLq65KbO4hqSI%2FXpCWDfyT9N79MmlqbIGxW0wlPQfrJbqkYDkUJugxG9QLgyz670r3Ub90cfqxd8hfTB47J5XaIJzkhG%2BtZavMptbXIQYAj9McD1kvfgi6ElzR1EPC3QuoNt7xdhEea%2FB6%2BTrzcjg9A5WwlvhxbtXWBjyZI3WmZdc7Er5MS7nARwllTYjAgV6DztitcR%2Burr%2FH3%2F023Y5%2Bx7Cl1PRSZf2CcGHSLcrimMkYisgLl8U5Odb286xp%2BS6DI97SiMwgxCsSngd4i3LlK9Shgm%2B0wZ9WlCPOxlHzCe%2Fpm9BjqkAZvdIJcZSqn7X02ajvAUy%2B%2FxK6ty7CeYtJwpFjoex8YPI860eHm4L2tA2jo9eJZgh6TDr9O2DBgdFPOE%2BA92WeZV2AIltcs%2Bvw7ZQ%2BlPKYSwp6DnztQmVxOke351w6QOLJsm9MRgT4gSMMsxN9SObjnvyHtMnMrvvF8EbTaKTCFoc0tOVudf%2B4F5vthJ1PcF0ZyWmblKR4A3g1E04GwCzPQ9wMoN&X-Amz-Signature=5571ee1d599c4e715077c0360cb5d4a9b600a65c91616a0542314fc4a6e86091&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ASY3JKS%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIFoveM2EHqkY6O6R6ZBAuo8PvK6jp1R1Yq4YcfPsAkxfAiEAoiBzMOZMe4NvzuZx0VBai8vQyHGFp11HS7NyF7Oohvkq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDGs2GeWsIuAC76VBsircA7QyN8djg%2BLuY9BjagJOzUlx%2B%2BdyppqdSGRrGiNFR7DeRc%2Bmw3tta6L3%2FyC3fvWUu%2BQgzIKP0LtCX9HGiqIhTkpuWC2DAc9CTON1y9a0A%2F5jDe3agbc1oqkJ5%2F46jcCSNKD5HxnMkqbWe0flp4ARpIk9ayvcz6EKwL2erbIUnqfdfDD3PqCjIfDqU1FjULaKw14P9vvXVF%2FHFkBor8pF3HDZUtXjdaHSmXAdu7pj700P%2Ba%2FbUs1rBStr3OmI2ECFsmRWH%2FGZVHzhHo8JVCbZALKaD3aT6RhHZyQrb6RZrtzsMNB1K0aW0%2F2PG4kT5G3LHetI8gvQTEckyFS7kj105oD%2FCgqqdPh2MWlG3aRnE%2FRaWGy2buuRAopRFd7O%2F4xoAF2kN94DqgcnQqJbodNsGlTDCaX5Gd%2FsN44hDbv9mv5CyIfBj6XsqEGcPm%2FK15EJdUDudFnerJSsdFr8Vp5doUqVRT8rOVJvUj188NOf4oLUuGUb3AwyuvxfT2azLW3j0qlHfEeYzQWdROdYmyaqk9mz5xkE7VwP9JuZ9jQzsS9w8JMMdntg%2BX6Duy41y1Dh8fDfdq5PzEXz3trf%2Bwi%2F2LsMzqAnWbEAnLzed2%2FzQwommyaHmYsOA%2FKNXfwVMNH%2Bmb0GOqUB%2F1jaQm1hCXeb8cuIOEM49f2tbkTDg6ej8hWKXDF%2FxEpA6Fvhw6fQGtY%2F9fKZ1JFoPXUWbuMcqIWRuN1we%2FyCGZJkXPLtDfXA3J95zX3K3DjNLwpthYdet3quKZUTv142%2FCWkP3ZouTrZ6CiSJyBh1XR9%2BGwAiZT5PHujfNu96BLPPfYVTc0gQspyutypTgIqeGrLDzNkJV0dPe723xVGaTdrh%2Fz9&X-Amz-Signature=b5b9820681c0bbcbefb5d9cfa71376ca81f59d8fd7d77d8fd5afb79469e96d44&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ASY3JKS%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIFoveM2EHqkY6O6R6ZBAuo8PvK6jp1R1Yq4YcfPsAkxfAiEAoiBzMOZMe4NvzuZx0VBai8vQyHGFp11HS7NyF7Oohvkq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDGs2GeWsIuAC76VBsircA7QyN8djg%2BLuY9BjagJOzUlx%2B%2BdyppqdSGRrGiNFR7DeRc%2Bmw3tta6L3%2FyC3fvWUu%2BQgzIKP0LtCX9HGiqIhTkpuWC2DAc9CTON1y9a0A%2F5jDe3agbc1oqkJ5%2F46jcCSNKD5HxnMkqbWe0flp4ARpIk9ayvcz6EKwL2erbIUnqfdfDD3PqCjIfDqU1FjULaKw14P9vvXVF%2FHFkBor8pF3HDZUtXjdaHSmXAdu7pj700P%2Ba%2FbUs1rBStr3OmI2ECFsmRWH%2FGZVHzhHo8JVCbZALKaD3aT6RhHZyQrb6RZrtzsMNB1K0aW0%2F2PG4kT5G3LHetI8gvQTEckyFS7kj105oD%2FCgqqdPh2MWlG3aRnE%2FRaWGy2buuRAopRFd7O%2F4xoAF2kN94DqgcnQqJbodNsGlTDCaX5Gd%2FsN44hDbv9mv5CyIfBj6XsqEGcPm%2FK15EJdUDudFnerJSsdFr8Vp5doUqVRT8rOVJvUj188NOf4oLUuGUb3AwyuvxfT2azLW3j0qlHfEeYzQWdROdYmyaqk9mz5xkE7VwP9JuZ9jQzsS9w8JMMdntg%2BX6Duy41y1Dh8fDfdq5PzEXz3trf%2Bwi%2F2LsMzqAnWbEAnLzed2%2FzQwommyaHmYsOA%2FKNXfwVMNH%2Bmb0GOqUB%2F1jaQm1hCXeb8cuIOEM49f2tbkTDg6ej8hWKXDF%2FxEpA6Fvhw6fQGtY%2F9fKZ1JFoPXUWbuMcqIWRuN1we%2FyCGZJkXPLtDfXA3J95zX3K3DjNLwpthYdet3quKZUTv142%2FCWkP3ZouTrZ6CiSJyBh1XR9%2BGwAiZT5PHujfNu96BLPPfYVTc0gQspyutypTgIqeGrLDzNkJV0dPe723xVGaTdrh%2Fz9&X-Amz-Signature=161b11b5a5a2626b44a5c047143ecdce2965ec9a651279f98c2bba4725e9c604&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ASY3JKS%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIFoveM2EHqkY6O6R6ZBAuo8PvK6jp1R1Yq4YcfPsAkxfAiEAoiBzMOZMe4NvzuZx0VBai8vQyHGFp11HS7NyF7Oohvkq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDGs2GeWsIuAC76VBsircA7QyN8djg%2BLuY9BjagJOzUlx%2B%2BdyppqdSGRrGiNFR7DeRc%2Bmw3tta6L3%2FyC3fvWUu%2BQgzIKP0LtCX9HGiqIhTkpuWC2DAc9CTON1y9a0A%2F5jDe3agbc1oqkJ5%2F46jcCSNKD5HxnMkqbWe0flp4ARpIk9ayvcz6EKwL2erbIUnqfdfDD3PqCjIfDqU1FjULaKw14P9vvXVF%2FHFkBor8pF3HDZUtXjdaHSmXAdu7pj700P%2Ba%2FbUs1rBStr3OmI2ECFsmRWH%2FGZVHzhHo8JVCbZALKaD3aT6RhHZyQrb6RZrtzsMNB1K0aW0%2F2PG4kT5G3LHetI8gvQTEckyFS7kj105oD%2FCgqqdPh2MWlG3aRnE%2FRaWGy2buuRAopRFd7O%2F4xoAF2kN94DqgcnQqJbodNsGlTDCaX5Gd%2FsN44hDbv9mv5CyIfBj6XsqEGcPm%2FK15EJdUDudFnerJSsdFr8Vp5doUqVRT8rOVJvUj188NOf4oLUuGUb3AwyuvxfT2azLW3j0qlHfEeYzQWdROdYmyaqk9mz5xkE7VwP9JuZ9jQzsS9w8JMMdntg%2BX6Duy41y1Dh8fDfdq5PzEXz3trf%2Bwi%2F2LsMzqAnWbEAnLzed2%2FzQwommyaHmYsOA%2FKNXfwVMNH%2Bmb0GOqUB%2F1jaQm1hCXeb8cuIOEM49f2tbkTDg6ej8hWKXDF%2FxEpA6Fvhw6fQGtY%2F9fKZ1JFoPXUWbuMcqIWRuN1we%2FyCGZJkXPLtDfXA3J95zX3K3DjNLwpthYdet3quKZUTv142%2FCWkP3ZouTrZ6CiSJyBh1XR9%2BGwAiZT5PHujfNu96BLPPfYVTc0gQspyutypTgIqeGrLDzNkJV0dPe723xVGaTdrh%2Fz9&X-Amz-Signature=3a21731ab7513dae0fcd762399ebcbe86678bb80237df3f0fdb433a1a74a3280&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ASY3JKS%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIFoveM2EHqkY6O6R6ZBAuo8PvK6jp1R1Yq4YcfPsAkxfAiEAoiBzMOZMe4NvzuZx0VBai8vQyHGFp11HS7NyF7Oohvkq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDGs2GeWsIuAC76VBsircA7QyN8djg%2BLuY9BjagJOzUlx%2B%2BdyppqdSGRrGiNFR7DeRc%2Bmw3tta6L3%2FyC3fvWUu%2BQgzIKP0LtCX9HGiqIhTkpuWC2DAc9CTON1y9a0A%2F5jDe3agbc1oqkJ5%2F46jcCSNKD5HxnMkqbWe0flp4ARpIk9ayvcz6EKwL2erbIUnqfdfDD3PqCjIfDqU1FjULaKw14P9vvXVF%2FHFkBor8pF3HDZUtXjdaHSmXAdu7pj700P%2Ba%2FbUs1rBStr3OmI2ECFsmRWH%2FGZVHzhHo8JVCbZALKaD3aT6RhHZyQrb6RZrtzsMNB1K0aW0%2F2PG4kT5G3LHetI8gvQTEckyFS7kj105oD%2FCgqqdPh2MWlG3aRnE%2FRaWGy2buuRAopRFd7O%2F4xoAF2kN94DqgcnQqJbodNsGlTDCaX5Gd%2FsN44hDbv9mv5CyIfBj6XsqEGcPm%2FK15EJdUDudFnerJSsdFr8Vp5doUqVRT8rOVJvUj188NOf4oLUuGUb3AwyuvxfT2azLW3j0qlHfEeYzQWdROdYmyaqk9mz5xkE7VwP9JuZ9jQzsS9w8JMMdntg%2BX6Duy41y1Dh8fDfdq5PzEXz3trf%2Bwi%2F2LsMzqAnWbEAnLzed2%2FzQwommyaHmYsOA%2FKNXfwVMNH%2Bmb0GOqUB%2F1jaQm1hCXeb8cuIOEM49f2tbkTDg6ej8hWKXDF%2FxEpA6Fvhw6fQGtY%2F9fKZ1JFoPXUWbuMcqIWRuN1we%2FyCGZJkXPLtDfXA3J95zX3K3DjNLwpthYdet3quKZUTv142%2FCWkP3ZouTrZ6CiSJyBh1XR9%2BGwAiZT5PHujfNu96BLPPfYVTc0gQspyutypTgIqeGrLDzNkJV0dPe723xVGaTdrh%2Fz9&X-Amz-Signature=acdc32d16972d2086ad97de051deefaf5c3f0c0a9bf16441b3063f1f3e7d7f25&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
