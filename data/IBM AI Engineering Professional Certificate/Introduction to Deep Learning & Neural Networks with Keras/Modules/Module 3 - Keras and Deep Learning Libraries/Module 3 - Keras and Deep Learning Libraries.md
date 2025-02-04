

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665AJTTLIY%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJGMEQCIFfGB9Hwt1PxC4wwtgO9bQ6noOPqDfll0Evx8eFDb%2FSFAiACXoWbRoZyX%2FVvZebwUUqJswcTJOwo3zPxFgFiaVXitCr%2FAwguEAAaDDYzNzQyMzE4MzgwNSIMaT9NNnOGcVeMb9R9KtwDquO5D43Gi5K%2FUpXxMcrUaujbZ2k3lsyswwZZqYUKGsTP7SFvc5bLmFR7BAOCbC7UaHlxPd2bZ2K8KSMqejb79tI583R3g6F%2F1XZKzYM2ajOktp3KCYiWnQPo2%2F9kGEmNy%2FIoEY6VPbr%2BZ6Shdu4o2WvzH9ZClh0ZHnW0%2F2Ts0sh1FmofvGNJ0wW0BZrWE%2FYvNDDPOcDkIOOLJ%2BIExIfgq%2F3HJfuxxVw2LWDHV3WkJh27zh2X0oPQLx8hfT%2FNie1wdMt4GagP50F0q8yrPvk7RJzQ53SR0BhsgF98r5IENxBeAh%2FKg%2FJ7%2FIOXIWq8sG49fvg3%2FxPZEPtKqnzQTvOU9LYoHgtvJOB8XoeOUWsC9itmXIb9MItvhH8120gX9sG8vIXopxT2lMpYVHKSeNINqzdYstdpvmbK59SoHjGg998tbneHNKo4vMLk9L6nu9r%2Bu6690uccKhn9b26WM6E7zbH%2BvQhNsl9wjlVj%2Fy3lMyybP37yR1rPmCdOLLFfEMqhxB2saBSIviLT%2F%2BfFKKzOeq8nYtbRtFzNMIXpZC%2BGIUv4TfF7DXEn6%2BUDINYnmfPy9Bk8uT%2FKV7I9%2B6JGpqv3x3iA6gc9dWfWnckSXyskgxq71ZWxqzFKr6RbHQcwmJ6IvQY6pgGvdJXPtNKjNHTnpMtwx56U4u%2FHF86NssQGRAhk%2FjxlX7gOUGLG%2BYhZ28nU8%2FCMwuLFlF2ZdzkEnRGK%2B0AQOFaU8ZPTHp%2FvsMhPG5kmD62wGAyBHEtGKXcmrNQHh97NQ%2Fy7tcsPY30mB2PVangYzrnJeCEr83wt8dZ3%2FSktfL7apCbuYM4FlZaFCnJjeSkLAsRvznv4gt8eogjGu4rYaFTm4crbmi2F&X-Amz-Signature=ab92e139face5781edba876dacc16ccda28ce3dc4474d8b93c591aa9760a5928&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665AJTTLIY%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJGMEQCIFfGB9Hwt1PxC4wwtgO9bQ6noOPqDfll0Evx8eFDb%2FSFAiACXoWbRoZyX%2FVvZebwUUqJswcTJOwo3zPxFgFiaVXitCr%2FAwguEAAaDDYzNzQyMzE4MzgwNSIMaT9NNnOGcVeMb9R9KtwDquO5D43Gi5K%2FUpXxMcrUaujbZ2k3lsyswwZZqYUKGsTP7SFvc5bLmFR7BAOCbC7UaHlxPd2bZ2K8KSMqejb79tI583R3g6F%2F1XZKzYM2ajOktp3KCYiWnQPo2%2F9kGEmNy%2FIoEY6VPbr%2BZ6Shdu4o2WvzH9ZClh0ZHnW0%2F2Ts0sh1FmofvGNJ0wW0BZrWE%2FYvNDDPOcDkIOOLJ%2BIExIfgq%2F3HJfuxxVw2LWDHV3WkJh27zh2X0oPQLx8hfT%2FNie1wdMt4GagP50F0q8yrPvk7RJzQ53SR0BhsgF98r5IENxBeAh%2FKg%2FJ7%2FIOXIWq8sG49fvg3%2FxPZEPtKqnzQTvOU9LYoHgtvJOB8XoeOUWsC9itmXIb9MItvhH8120gX9sG8vIXopxT2lMpYVHKSeNINqzdYstdpvmbK59SoHjGg998tbneHNKo4vMLk9L6nu9r%2Bu6690uccKhn9b26WM6E7zbH%2BvQhNsl9wjlVj%2Fy3lMyybP37yR1rPmCdOLLFfEMqhxB2saBSIviLT%2F%2BfFKKzOeq8nYtbRtFzNMIXpZC%2BGIUv4TfF7DXEn6%2BUDINYnmfPy9Bk8uT%2FKV7I9%2B6JGpqv3x3iA6gc9dWfWnckSXyskgxq71ZWxqzFKr6RbHQcwmJ6IvQY6pgGvdJXPtNKjNHTnpMtwx56U4u%2FHF86NssQGRAhk%2FjxlX7gOUGLG%2BYhZ28nU8%2FCMwuLFlF2ZdzkEnRGK%2B0AQOFaU8ZPTHp%2FvsMhPG5kmD62wGAyBHEtGKXcmrNQHh97NQ%2Fy7tcsPY30mB2PVangYzrnJeCEr83wt8dZ3%2FSktfL7apCbuYM4FlZaFCnJjeSkLAsRvznv4gt8eogjGu4rYaFTm4crbmi2F&X-Amz-Signature=7ff2a21b628e8bcec2f1be14ad4307e7f40d75d01f17736315aea8b03a1a0d0f&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665AJTTLIY%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJGMEQCIFfGB9Hwt1PxC4wwtgO9bQ6noOPqDfll0Evx8eFDb%2FSFAiACXoWbRoZyX%2FVvZebwUUqJswcTJOwo3zPxFgFiaVXitCr%2FAwguEAAaDDYzNzQyMzE4MzgwNSIMaT9NNnOGcVeMb9R9KtwDquO5D43Gi5K%2FUpXxMcrUaujbZ2k3lsyswwZZqYUKGsTP7SFvc5bLmFR7BAOCbC7UaHlxPd2bZ2K8KSMqejb79tI583R3g6F%2F1XZKzYM2ajOktp3KCYiWnQPo2%2F9kGEmNy%2FIoEY6VPbr%2BZ6Shdu4o2WvzH9ZClh0ZHnW0%2F2Ts0sh1FmofvGNJ0wW0BZrWE%2FYvNDDPOcDkIOOLJ%2BIExIfgq%2F3HJfuxxVw2LWDHV3WkJh27zh2X0oPQLx8hfT%2FNie1wdMt4GagP50F0q8yrPvk7RJzQ53SR0BhsgF98r5IENxBeAh%2FKg%2FJ7%2FIOXIWq8sG49fvg3%2FxPZEPtKqnzQTvOU9LYoHgtvJOB8XoeOUWsC9itmXIb9MItvhH8120gX9sG8vIXopxT2lMpYVHKSeNINqzdYstdpvmbK59SoHjGg998tbneHNKo4vMLk9L6nu9r%2Bu6690uccKhn9b26WM6E7zbH%2BvQhNsl9wjlVj%2Fy3lMyybP37yR1rPmCdOLLFfEMqhxB2saBSIviLT%2F%2BfFKKzOeq8nYtbRtFzNMIXpZC%2BGIUv4TfF7DXEn6%2BUDINYnmfPy9Bk8uT%2FKV7I9%2B6JGpqv3x3iA6gc9dWfWnckSXyskgxq71ZWxqzFKr6RbHQcwmJ6IvQY6pgGvdJXPtNKjNHTnpMtwx56U4u%2FHF86NssQGRAhk%2FjxlX7gOUGLG%2BYhZ28nU8%2FCMwuLFlF2ZdzkEnRGK%2B0AQOFaU8ZPTHp%2FvsMhPG5kmD62wGAyBHEtGKXcmrNQHh97NQ%2Fy7tcsPY30mB2PVangYzrnJeCEr83wt8dZ3%2FSktfL7apCbuYM4FlZaFCnJjeSkLAsRvznv4gt8eogjGu4rYaFTm4crbmi2F&X-Amz-Signature=8c34e01fd49d6b866d28e3351cbd3a4703c9a786310d96471cecc23c0c5c06b8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZI22DAMT%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJHMEUCICFBJUWe312wip2RU1Nsn3oG4qNqJTYKKVxqiF42EhUmAiEA%2FBWMXiTjltYtN%2BvNmw06YEiN%2Fk69iOLmPx%2BS0VFWBHUq%2FwMILhAAGgw2Mzc0MjMxODM4MDUiDM3Mz%2FCxpTE4J%2FZ4iircAwEQaKzY%2Bi8JogFTHEWE0HG9LZUNSe3m5AjD%2FOvCoEWrZNPjDZ8H%2BlI6s0EyWgdH6GQNk8CGoQm3NWc9K%2FHh389JMrMaXV48F07tUBhC%2Fqt0q9%2FkcoINAOkQQoLMSZQDSy6U0R2Y6F8YdnEclGl7Qj4jhJ%2FAJJCGo%2BErNUhRD3bnkrF2BDvpCPCG7wiEgijRkhpCTbGBb41pU5WSHR6YnXi8YHNuvFOdPEwcDraBPxCpYgKpEsAwpQYGM8ablB9aPR0xGwmp0UPp78rXy2mrPghsmwM2H5BmIzFIXkVdnGwgNJCDuJdovVgMEiVyYq28DjORSuqNsPNulr9Al2%2F5vNj%2B3iuboiBH1yvz8fqb7f676mWqlS6o8fJxo%2FLfzAG6M8M7ZIy0NF%2BIzOhds5kRgzh8elavzkJt0RTy2HVut6b09Vuj4BFiLNChELfast%2B5pDPUUD2YZhVvnyLKsyfurnwegOxWB5VkNf463xhT7WNW4qngd7OVM2PvwNnzJhtyV9drRBhRDx%2BAuhUEuiY2z8vA81G9dwu8EToNitTQdUirgOGz8%2Bgo843PXoDA8FK9IHuG%2BUtMs7o1jTwtkBAjMeOJeeqh1ufYIR0%2BagztTgou%2BGk%2BgKext%2BF6tEGEMJmeiL0GOqUBek4M0d0IzxzTtdL9kTF4Jea%2BxkN9de1Ve1rjoTTiaZuPtkJC6oBIGS1uQmAMEAv95VjO6r89narGQ5aYwIns8WFoid9CUXqL%2FOw26a8LX8q4oOh2TfB6DwG0G6wN9U%2BzMM1YFQlQTsHqiyZRWSLeH3RGd%2BW7fdv6cgqNegOo1hZKuJlfpFW1EXHuyBZzif35tS7qZ%2B6oHkBJa7TkRFEXiWRwFy0e&X-Amz-Signature=06b4ba30b78aff8274f9713067e1b5c71421e0111309cad6b4216096801fe8e4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UKB352ZI%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJHMEUCIEIrQXLSCvwXC9HwIA33%2BSKgjDJjuF9hQwgKBI1rIdOXAiEA5l%2B1rUTYh%2FfjfYf0F4cD9uNPhEyLAw2qM44%2BxuQp50sq%2FwMILhAAGgw2Mzc0MjMxODM4MDUiDMiaRxHkpAh95XHxECrcA35i7nEhCX58zP92CzyPYIFPpO%2BlgphMVkk6B8KSt8S%2BkEom7HtC%2BzfVl%2B47hr8iHxhGTdUq0yR0oFijRznBCbziVJRaDTEYIEUofjruOHdVnciHopJXsOQ0bwQAQTwW%2FtkufacjCfmCVOkzbkOfkIJxL5PDe2HgYvSoFO0ReqNJAjc38q6Zbu5yaJQM4orU2uDr6%2FHBbZxvD6yPBBVg65oRbuGEGY72PGyW9XInMrIa72dpGW05aX%2FuFVENS87e753U2ki58EIT7GVDBxLaB2MhkUoW6IStSbVYskGFHOW0aAeMFJg%2FszEO057ZnqHLdd2C3Ted7d8VXHsp8OiHWo1%2BuGyqhLpxZlrPkRa1bY5TqUrBBiEbV1wdICUOfcZfeLLbyC7g6D1NS67%2FxnzCBeM3RTm8mOc%2B0M%2B%2BEX75zgHNQDe%2FwLVIUu6QusexD7yTPiY%2B%2Bd3JBMMID%2Fkn3AVjrQZJvHe0ikcIY7QSgjmdiRw%2FtrRhJqtIlUAOcnHoACBcSXurq3mAaAgHxx1yox4t7hUPFA0qRS6vo9sT7OIU6azBwoTpyqXSurQAaIccLWwv3jqXYsT8WE3F4vF9N791C11Z59jM0BiGVP2ypOOIxZoBZ1b6%2BkcH1Z08b%2Bs5MIueiL0GOqUBsqD%2F%2F7LSug7K42lGyG4wZ8IR6Qsbp4A1%2BSDa4FPBqZPBx29YCOEcCydYNklMsYEUkJ25wCc8q2g8hdUYcW43SiPxr3uQkxl1nk0MvY%2FPDwXsRsslSb1ih3Uiop%2FtwNrkW%2FMDpk2jesyVjDpQ%2Fgjy8yWHsTdxPpwx5a8A54U6IVQJ9sYLx3F9egr7PtSdHMXKobfgjz4JZ4GU6ZsRu9zIf3wEWWW8&X-Amz-Signature=b4bebd61acff04edca6575244f47a2bdbf4c2c2fa08a708f1ee36fffa988d3f1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665AJTTLIY%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJGMEQCIFfGB9Hwt1PxC4wwtgO9bQ6noOPqDfll0Evx8eFDb%2FSFAiACXoWbRoZyX%2FVvZebwUUqJswcTJOwo3zPxFgFiaVXitCr%2FAwguEAAaDDYzNzQyMzE4MzgwNSIMaT9NNnOGcVeMb9R9KtwDquO5D43Gi5K%2FUpXxMcrUaujbZ2k3lsyswwZZqYUKGsTP7SFvc5bLmFR7BAOCbC7UaHlxPd2bZ2K8KSMqejb79tI583R3g6F%2F1XZKzYM2ajOktp3KCYiWnQPo2%2F9kGEmNy%2FIoEY6VPbr%2BZ6Shdu4o2WvzH9ZClh0ZHnW0%2F2Ts0sh1FmofvGNJ0wW0BZrWE%2FYvNDDPOcDkIOOLJ%2BIExIfgq%2F3HJfuxxVw2LWDHV3WkJh27zh2X0oPQLx8hfT%2FNie1wdMt4GagP50F0q8yrPvk7RJzQ53SR0BhsgF98r5IENxBeAh%2FKg%2FJ7%2FIOXIWq8sG49fvg3%2FxPZEPtKqnzQTvOU9LYoHgtvJOB8XoeOUWsC9itmXIb9MItvhH8120gX9sG8vIXopxT2lMpYVHKSeNINqzdYstdpvmbK59SoHjGg998tbneHNKo4vMLk9L6nu9r%2Bu6690uccKhn9b26WM6E7zbH%2BvQhNsl9wjlVj%2Fy3lMyybP37yR1rPmCdOLLFfEMqhxB2saBSIviLT%2F%2BfFKKzOeq8nYtbRtFzNMIXpZC%2BGIUv4TfF7DXEn6%2BUDINYnmfPy9Bk8uT%2FKV7I9%2B6JGpqv3x3iA6gc9dWfWnckSXyskgxq71ZWxqzFKr6RbHQcwmJ6IvQY6pgGvdJXPtNKjNHTnpMtwx56U4u%2FHF86NssQGRAhk%2FjxlX7gOUGLG%2BYhZ28nU8%2FCMwuLFlF2ZdzkEnRGK%2B0AQOFaU8ZPTHp%2FvsMhPG5kmD62wGAyBHEtGKXcmrNQHh97NQ%2Fy7tcsPY30mB2PVangYzrnJeCEr83wt8dZ3%2FSktfL7apCbuYM4FlZaFCnJjeSkLAsRvznv4gt8eogjGu4rYaFTm4crbmi2F&X-Amz-Signature=1354d34e0f43973170cf6799bb39dee87692ad329e6cd449918756e2e789940f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665AJTTLIY%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJGMEQCIFfGB9Hwt1PxC4wwtgO9bQ6noOPqDfll0Evx8eFDb%2FSFAiACXoWbRoZyX%2FVvZebwUUqJswcTJOwo3zPxFgFiaVXitCr%2FAwguEAAaDDYzNzQyMzE4MzgwNSIMaT9NNnOGcVeMb9R9KtwDquO5D43Gi5K%2FUpXxMcrUaujbZ2k3lsyswwZZqYUKGsTP7SFvc5bLmFR7BAOCbC7UaHlxPd2bZ2K8KSMqejb79tI583R3g6F%2F1XZKzYM2ajOktp3KCYiWnQPo2%2F9kGEmNy%2FIoEY6VPbr%2BZ6Shdu4o2WvzH9ZClh0ZHnW0%2F2Ts0sh1FmofvGNJ0wW0BZrWE%2FYvNDDPOcDkIOOLJ%2BIExIfgq%2F3HJfuxxVw2LWDHV3WkJh27zh2X0oPQLx8hfT%2FNie1wdMt4GagP50F0q8yrPvk7RJzQ53SR0BhsgF98r5IENxBeAh%2FKg%2FJ7%2FIOXIWq8sG49fvg3%2FxPZEPtKqnzQTvOU9LYoHgtvJOB8XoeOUWsC9itmXIb9MItvhH8120gX9sG8vIXopxT2lMpYVHKSeNINqzdYstdpvmbK59SoHjGg998tbneHNKo4vMLk9L6nu9r%2Bu6690uccKhn9b26WM6E7zbH%2BvQhNsl9wjlVj%2Fy3lMyybP37yR1rPmCdOLLFfEMqhxB2saBSIviLT%2F%2BfFKKzOeq8nYtbRtFzNMIXpZC%2BGIUv4TfF7DXEn6%2BUDINYnmfPy9Bk8uT%2FKV7I9%2B6JGpqv3x3iA6gc9dWfWnckSXyskgxq71ZWxqzFKr6RbHQcwmJ6IvQY6pgGvdJXPtNKjNHTnpMtwx56U4u%2FHF86NssQGRAhk%2FjxlX7gOUGLG%2BYhZ28nU8%2FCMwuLFlF2ZdzkEnRGK%2B0AQOFaU8ZPTHp%2FvsMhPG5kmD62wGAyBHEtGKXcmrNQHh97NQ%2Fy7tcsPY30mB2PVangYzrnJeCEr83wt8dZ3%2FSktfL7apCbuYM4FlZaFCnJjeSkLAsRvznv4gt8eogjGu4rYaFTm4crbmi2F&X-Amz-Signature=86e351eb1de2228b03a7efd50ad866e5af9b36c92eccfa100b48316db475928f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665AJTTLIY%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJGMEQCIFfGB9Hwt1PxC4wwtgO9bQ6noOPqDfll0Evx8eFDb%2FSFAiACXoWbRoZyX%2FVvZebwUUqJswcTJOwo3zPxFgFiaVXitCr%2FAwguEAAaDDYzNzQyMzE4MzgwNSIMaT9NNnOGcVeMb9R9KtwDquO5D43Gi5K%2FUpXxMcrUaujbZ2k3lsyswwZZqYUKGsTP7SFvc5bLmFR7BAOCbC7UaHlxPd2bZ2K8KSMqejb79tI583R3g6F%2F1XZKzYM2ajOktp3KCYiWnQPo2%2F9kGEmNy%2FIoEY6VPbr%2BZ6Shdu4o2WvzH9ZClh0ZHnW0%2F2Ts0sh1FmofvGNJ0wW0BZrWE%2FYvNDDPOcDkIOOLJ%2BIExIfgq%2F3HJfuxxVw2LWDHV3WkJh27zh2X0oPQLx8hfT%2FNie1wdMt4GagP50F0q8yrPvk7RJzQ53SR0BhsgF98r5IENxBeAh%2FKg%2FJ7%2FIOXIWq8sG49fvg3%2FxPZEPtKqnzQTvOU9LYoHgtvJOB8XoeOUWsC9itmXIb9MItvhH8120gX9sG8vIXopxT2lMpYVHKSeNINqzdYstdpvmbK59SoHjGg998tbneHNKo4vMLk9L6nu9r%2Bu6690uccKhn9b26WM6E7zbH%2BvQhNsl9wjlVj%2Fy3lMyybP37yR1rPmCdOLLFfEMqhxB2saBSIviLT%2F%2BfFKKzOeq8nYtbRtFzNMIXpZC%2BGIUv4TfF7DXEn6%2BUDINYnmfPy9Bk8uT%2FKV7I9%2B6JGpqv3x3iA6gc9dWfWnckSXyskgxq71ZWxqzFKr6RbHQcwmJ6IvQY6pgGvdJXPtNKjNHTnpMtwx56U4u%2FHF86NssQGRAhk%2FjxlX7gOUGLG%2BYhZ28nU8%2FCMwuLFlF2ZdzkEnRGK%2B0AQOFaU8ZPTHp%2FvsMhPG5kmD62wGAyBHEtGKXcmrNQHh97NQ%2Fy7tcsPY30mB2PVangYzrnJeCEr83wt8dZ3%2FSktfL7apCbuYM4FlZaFCnJjeSkLAsRvznv4gt8eogjGu4rYaFTm4crbmi2F&X-Amz-Signature=428d3e1119376ab62d45c3c358bb29a7d41b2bc2349a0ee4699b5a148de6ffe2&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665AJTTLIY%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJGMEQCIFfGB9Hwt1PxC4wwtgO9bQ6noOPqDfll0Evx8eFDb%2FSFAiACXoWbRoZyX%2FVvZebwUUqJswcTJOwo3zPxFgFiaVXitCr%2FAwguEAAaDDYzNzQyMzE4MzgwNSIMaT9NNnOGcVeMb9R9KtwDquO5D43Gi5K%2FUpXxMcrUaujbZ2k3lsyswwZZqYUKGsTP7SFvc5bLmFR7BAOCbC7UaHlxPd2bZ2K8KSMqejb79tI583R3g6F%2F1XZKzYM2ajOktp3KCYiWnQPo2%2F9kGEmNy%2FIoEY6VPbr%2BZ6Shdu4o2WvzH9ZClh0ZHnW0%2F2Ts0sh1FmofvGNJ0wW0BZrWE%2FYvNDDPOcDkIOOLJ%2BIExIfgq%2F3HJfuxxVw2LWDHV3WkJh27zh2X0oPQLx8hfT%2FNie1wdMt4GagP50F0q8yrPvk7RJzQ53SR0BhsgF98r5IENxBeAh%2FKg%2FJ7%2FIOXIWq8sG49fvg3%2FxPZEPtKqnzQTvOU9LYoHgtvJOB8XoeOUWsC9itmXIb9MItvhH8120gX9sG8vIXopxT2lMpYVHKSeNINqzdYstdpvmbK59SoHjGg998tbneHNKo4vMLk9L6nu9r%2Bu6690uccKhn9b26WM6E7zbH%2BvQhNsl9wjlVj%2Fy3lMyybP37yR1rPmCdOLLFfEMqhxB2saBSIviLT%2F%2BfFKKzOeq8nYtbRtFzNMIXpZC%2BGIUv4TfF7DXEn6%2BUDINYnmfPy9Bk8uT%2FKV7I9%2B6JGpqv3x3iA6gc9dWfWnckSXyskgxq71ZWxqzFKr6RbHQcwmJ6IvQY6pgGvdJXPtNKjNHTnpMtwx56U4u%2FHF86NssQGRAhk%2FjxlX7gOUGLG%2BYhZ28nU8%2FCMwuLFlF2ZdzkEnRGK%2B0AQOFaU8ZPTHp%2FvsMhPG5kmD62wGAyBHEtGKXcmrNQHh97NQ%2Fy7tcsPY30mB2PVangYzrnJeCEr83wt8dZ3%2FSktfL7apCbuYM4FlZaFCnJjeSkLAsRvznv4gt8eogjGu4rYaFTm4crbmi2F&X-Amz-Signature=67fa42eea1f466df57d9d0cf651237d76bf6240ae496c255338aa65eafa520c8&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
