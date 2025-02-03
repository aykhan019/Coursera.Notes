

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USB5XCYI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDfEH5ypfdfD9HnsUQKHSQIaUByo7fQn%2FeXXR53g%2BxO%2FgIhAMFGl9mQ76GSHLV%2BT9C%2FECmfg4oZg2QTrqtU7PE72eQtKv8DCBYQABoMNjM3NDIzMTgzODA1IgyuVone4oYIj4NkrZ4q3APgcpRBNcOGD3aHqrQYLLeOtuOxZchYSkE7%2BdjNuXRXAoqfOg%2Bhb8t03l3YNU4lO%2B46BG74qXb6pamip4doAa5PmoiOWuSSIJmWSzZ4Z8zKn5NNLo7oiEjOiVFJrjJZtsgHock%2B%2FVSY0yiOWSoQUYkEHn5ymYzynqjT6Bj4mX%2FH1KEi%2Fu1TeIjelFv1NM8vmvaZTKc%2FpJ4l0TlXMmW9iyqrqiHBwDNiIPxr00AF4VGOxk%2Ber5QNVeUZiS83TylRdV8Vn1qm7lKQ80OGNNvcs33yBBH%2BXe%2BzTB1i1HJG70A%2Bgm1AOaGs7tHP6uaAq2T2c06HWKnPT9MSf%2Byg9IXyHNBkfqE8QycNvxkfw14ixzW5i3utHCd7reVnk%2FBNlQBsx8f5mwrdcuz194%2BSXHrhghmvUhcoQ1FDkLjlh5MTSo707ArJbecDIt2BYdiG84FE2gYm%2BWXbZKYQHqj0rzQgLUDV%2FBXPcKPgSSCYdhJfir0aWtt3CJIWfoJ%2FsEb%2FkqjvQQfxChPctoYHsLWa3Uv%2BagvcKCktOZDh80tFSxAoeS75xBCbOtjxZJUj4Mv56DiKVOOQeYngQrFQwM3waDKbE5Tid0Q0AcbCGkuOpbutYrqLtJghTxXJWdCjL5dFuTCD8YK9BjqkASkBz4qVIZulek3mpISU7vYW5DkNoklzX4IJ9teB46pLVUH3kbdnsZ5Zz6ld1RmTnDVetdhkT31jK8GKvqPcnqX8Ruy27YPjnSPTFLdFYbHqnS4EA6YRRXcPyZXyM3ZdxxrazPCt6b4AJcNJVtzxryP911tB0sSOU8PzAk12%2FWkggvf5DC6eig5kOqlhbW3aTZt3OyWssQo3XRpGleegkevuFjz8&X-Amz-Signature=e6b6092e75fa0f78cc8f497e201cfda0e87b1e3e42e8c5f926f674b37e942532&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USB5XCYI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDfEH5ypfdfD9HnsUQKHSQIaUByo7fQn%2FeXXR53g%2BxO%2FgIhAMFGl9mQ76GSHLV%2BT9C%2FECmfg4oZg2QTrqtU7PE72eQtKv8DCBYQABoMNjM3NDIzMTgzODA1IgyuVone4oYIj4NkrZ4q3APgcpRBNcOGD3aHqrQYLLeOtuOxZchYSkE7%2BdjNuXRXAoqfOg%2Bhb8t03l3YNU4lO%2B46BG74qXb6pamip4doAa5PmoiOWuSSIJmWSzZ4Z8zKn5NNLo7oiEjOiVFJrjJZtsgHock%2B%2FVSY0yiOWSoQUYkEHn5ymYzynqjT6Bj4mX%2FH1KEi%2Fu1TeIjelFv1NM8vmvaZTKc%2FpJ4l0TlXMmW9iyqrqiHBwDNiIPxr00AF4VGOxk%2Ber5QNVeUZiS83TylRdV8Vn1qm7lKQ80OGNNvcs33yBBH%2BXe%2BzTB1i1HJG70A%2Bgm1AOaGs7tHP6uaAq2T2c06HWKnPT9MSf%2Byg9IXyHNBkfqE8QycNvxkfw14ixzW5i3utHCd7reVnk%2FBNlQBsx8f5mwrdcuz194%2BSXHrhghmvUhcoQ1FDkLjlh5MTSo707ArJbecDIt2BYdiG84FE2gYm%2BWXbZKYQHqj0rzQgLUDV%2FBXPcKPgSSCYdhJfir0aWtt3CJIWfoJ%2FsEb%2FkqjvQQfxChPctoYHsLWa3Uv%2BagvcKCktOZDh80tFSxAoeS75xBCbOtjxZJUj4Mv56DiKVOOQeYngQrFQwM3waDKbE5Tid0Q0AcbCGkuOpbutYrqLtJghTxXJWdCjL5dFuTCD8YK9BjqkASkBz4qVIZulek3mpISU7vYW5DkNoklzX4IJ9teB46pLVUH3kbdnsZ5Zz6ld1RmTnDVetdhkT31jK8GKvqPcnqX8Ruy27YPjnSPTFLdFYbHqnS4EA6YRRXcPyZXyM3ZdxxrazPCt6b4AJcNJVtzxryP911tB0sSOU8PzAk12%2FWkggvf5DC6eig5kOqlhbW3aTZt3OyWssQo3XRpGleegkevuFjz8&X-Amz-Signature=29f30735a620ef7fcad160c64cf22c4420dad78eab82e40df1cab7b1d38f018a&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USB5XCYI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDfEH5ypfdfD9HnsUQKHSQIaUByo7fQn%2FeXXR53g%2BxO%2FgIhAMFGl9mQ76GSHLV%2BT9C%2FECmfg4oZg2QTrqtU7PE72eQtKv8DCBYQABoMNjM3NDIzMTgzODA1IgyuVone4oYIj4NkrZ4q3APgcpRBNcOGD3aHqrQYLLeOtuOxZchYSkE7%2BdjNuXRXAoqfOg%2Bhb8t03l3YNU4lO%2B46BG74qXb6pamip4doAa5PmoiOWuSSIJmWSzZ4Z8zKn5NNLo7oiEjOiVFJrjJZtsgHock%2B%2FVSY0yiOWSoQUYkEHn5ymYzynqjT6Bj4mX%2FH1KEi%2Fu1TeIjelFv1NM8vmvaZTKc%2FpJ4l0TlXMmW9iyqrqiHBwDNiIPxr00AF4VGOxk%2Ber5QNVeUZiS83TylRdV8Vn1qm7lKQ80OGNNvcs33yBBH%2BXe%2BzTB1i1HJG70A%2Bgm1AOaGs7tHP6uaAq2T2c06HWKnPT9MSf%2Byg9IXyHNBkfqE8QycNvxkfw14ixzW5i3utHCd7reVnk%2FBNlQBsx8f5mwrdcuz194%2BSXHrhghmvUhcoQ1FDkLjlh5MTSo707ArJbecDIt2BYdiG84FE2gYm%2BWXbZKYQHqj0rzQgLUDV%2FBXPcKPgSSCYdhJfir0aWtt3CJIWfoJ%2FsEb%2FkqjvQQfxChPctoYHsLWa3Uv%2BagvcKCktOZDh80tFSxAoeS75xBCbOtjxZJUj4Mv56DiKVOOQeYngQrFQwM3waDKbE5Tid0Q0AcbCGkuOpbutYrqLtJghTxXJWdCjL5dFuTCD8YK9BjqkASkBz4qVIZulek3mpISU7vYW5DkNoklzX4IJ9teB46pLVUH3kbdnsZ5Zz6ld1RmTnDVetdhkT31jK8GKvqPcnqX8Ruy27YPjnSPTFLdFYbHqnS4EA6YRRXcPyZXyM3ZdxxrazPCt6b4AJcNJVtzxryP911tB0sSOU8PzAk12%2FWkggvf5DC6eig5kOqlhbW3aTZt3OyWssQo3XRpGleegkevuFjz8&X-Amz-Signature=52b19dabe5bef2e3d41d89e2d7b0b5f4b24eb01870366d1fc7900e131eb50a62&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GLP4RDV%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAO3bnzHvwMgS71diNSH1brYTJhVFtvyzkCirwU8n26sAiBvMUFAbcxn6ssLy%2FdWJpbk7B5hPiHCMoiJIuwgRHGERCr%2FAwgWEAAaDDYzNzQyMzE4MzgwNSIMPd%2FzRbYJF3yN7qZbKtwDVYCNrNW1u%2BInJZy154MO%2B%2FHOiG3yPhq%2FMWDG9vro8C3jdDvls5Xw9fvyKrzmMqZoy28MHbxXJXz%2BSK7unn9S1c4cwnftDVof%2BsKumtf4psvGDjZyfO%2B1XPf1bViVr6gH%2BluYb2Vl8HusdmgN1G%2BDAp%2BB%2B2FzosCwNvaDO%2BOUT%2Faeu3FJjH0KS5kWubYTgE7obeog5zjgKz5ptqL87VKmwQLxQuZajgZgtou6%2BaWkdhunnOD%2F%2Fz9XJtykiZP4%2BpjHrGbcGN3Qe1bYbNihg8gHlSczm58KlVgyO1orDJde5W8lARJDTGuZyHhwwEuvC%2BK6rr6NTfGXPzmvC7VWJgqdY5jGYEf5wTj2uUs%2BtF254J3YS662AGWbDgAcjbvA%2F%2BNy0zAnlSESzy6EzmR7yYYCBwV%2FUIlyFPqprNK6W0o3h678o9Ihsuew8%2Fc6jSabvJeZC5rdV4%2FIpUYwWvEvX0yghFQGZTq5ETwU%2BXMJKD4qOUyzUbrzJRmPVBKake%2FUOQo7cHIzEXMhr%2BbBXgt%2BZ6VV24EcgoVkqJs5gV8SkYeKIoMWfffS2QX84xKJ66rhC3uFmqjgNZCDhvd4rn17ldIWAzRIr9ag1z6vrWiKU4Oh0ybWZTr64B6YutmvWMMwo%2FGCvQY6pgEDybi56O5y1jqrvrJwhI4HIPLzRvnSIzp2Af6k5DMCcpXI1FQcU7WCk7djNrlagHE5kR6zs6Z%2BWveJZaPZDRhjwFzaIwqnjXjMrJXghKxAokO2XFg3zROy9FIvqketqM0%2FujfjZMypVjwIyrMnFsKy1BdgRgShqOX20H5amFHX5qs%2F%2FRkjRsfkdmeNNofAOZNQ80RW6Lcfpajpxbzvf2asXC6JDohg&X-Amz-Signature=28e8fcdaaeca78b5ecf732f32f1c4dca143850e5cfa969d3f513209d370b405c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQGNEUI7%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132021Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBW2Z%2BEx5mCgL2NX%2FFaay%2BPeMKwPPD5iovI5yeJMxp5ZAiEA3Lm2%2BGFKRoQG8YYJcu38FzL4YTDwbMJvz3lpV5lue4Eq%2FwMIFhAAGgw2Mzc0MjMxODM4MDUiDFs6PnMH34n24hFPDyrcAypapvH6IK3DTlqN9c9CwSphi6odUquqy%2F6T2za5nm6AWOcPLCLdvWvTS%2FzgbH3bSU2g3fL6NNR%2BCRQsoE5SGzc5FLqE9lEld%2B0vXa7Axd42PMYkpVPnfw4gBl%2Fn73oPlSD4wsTf3fon3Tv43vgywoVzeGEh%2FuK%2B5WfyzybepQs0BHENNJuTxDLBhwHwSUgNe24%2F5Mt2qT27HLx8KGV1muQh%2FfBmf8V4rZhMPxxPxdrykaVvwO2583VCJJQrK83a2ldkUFYqHcXH2RC7RN4P2hDQYns2CPg%2FWJKI4afr6VzZb2YrpnsgBSuCkILfP9fih8KtQkdS2%2F9qEgfASyuPPO841tUoFN9dqfK3R%2BTgw3X%2F6tfnJbnrKpF7eTqTN7KuGube0bIfMP0f8msF8Q2d5fuN5cgqC36e31GpI6VYaAUIr6ha68I9bz1o8Q5hhFfg%2BUjmTPmJhAD3bpYxHU3ZQXs%2FBdVm9nEarbqAMyQPXyxDtU86iDuTEcuWGGo4BuXT4xV24XNkCeOAbFhM6U59YCPcA0oPPR0aPDcpK%2FCkcIu52QICXDdIIGS%2FVcjX74pK5CXvh12ag2TnSre2bbauUwPNlEq6jJ7itceVqN7Y3%2BxJcJ262QzFeYeXVFQoMJjygr0GOqUBwRTRYP0CNWlDL5lxCQmPF%2F%2FDB2QTSL6C4hEfQg2IWRew07vE%2BJtBqvPyS3%2B4WD6zq0WRX7D6%2BMnCWVL102NqPfr3eRCcxQA0O%2F5JGWhjyvNo7yrnMXpnPKE6eQ0t%2FN49SA6YN9IEenIs3oLVKfbSG8zJo8Pz6FcPhEcS0uirAVInkvEKkZ4OuhkahLCHjFXbIsQpuXqbka%2FJida5yI9GGepOnQIn&X-Amz-Signature=cd9ad055c3536dd2432cdb3eb59a3d3ac56a8218c2f9b315ef0864473bf83aac&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USB5XCYI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDfEH5ypfdfD9HnsUQKHSQIaUByo7fQn%2FeXXR53g%2BxO%2FgIhAMFGl9mQ76GSHLV%2BT9C%2FECmfg4oZg2QTrqtU7PE72eQtKv8DCBYQABoMNjM3NDIzMTgzODA1IgyuVone4oYIj4NkrZ4q3APgcpRBNcOGD3aHqrQYLLeOtuOxZchYSkE7%2BdjNuXRXAoqfOg%2Bhb8t03l3YNU4lO%2B46BG74qXb6pamip4doAa5PmoiOWuSSIJmWSzZ4Z8zKn5NNLo7oiEjOiVFJrjJZtsgHock%2B%2FVSY0yiOWSoQUYkEHn5ymYzynqjT6Bj4mX%2FH1KEi%2Fu1TeIjelFv1NM8vmvaZTKc%2FpJ4l0TlXMmW9iyqrqiHBwDNiIPxr00AF4VGOxk%2Ber5QNVeUZiS83TylRdV8Vn1qm7lKQ80OGNNvcs33yBBH%2BXe%2BzTB1i1HJG70A%2Bgm1AOaGs7tHP6uaAq2T2c06HWKnPT9MSf%2Byg9IXyHNBkfqE8QycNvxkfw14ixzW5i3utHCd7reVnk%2FBNlQBsx8f5mwrdcuz194%2BSXHrhghmvUhcoQ1FDkLjlh5MTSo707ArJbecDIt2BYdiG84FE2gYm%2BWXbZKYQHqj0rzQgLUDV%2FBXPcKPgSSCYdhJfir0aWtt3CJIWfoJ%2FsEb%2FkqjvQQfxChPctoYHsLWa3Uv%2BagvcKCktOZDh80tFSxAoeS75xBCbOtjxZJUj4Mv56DiKVOOQeYngQrFQwM3waDKbE5Tid0Q0AcbCGkuOpbutYrqLtJghTxXJWdCjL5dFuTCD8YK9BjqkASkBz4qVIZulek3mpISU7vYW5DkNoklzX4IJ9teB46pLVUH3kbdnsZ5Zz6ld1RmTnDVetdhkT31jK8GKvqPcnqX8Ruy27YPjnSPTFLdFYbHqnS4EA6YRRXcPyZXyM3ZdxxrazPCt6b4AJcNJVtzxryP911tB0sSOU8PzAk12%2FWkggvf5DC6eig5kOqlhbW3aTZt3OyWssQo3XRpGleegkevuFjz8&X-Amz-Signature=49cbc4ee2d11b11e6c2e9dca73b8ac53b5d955bafa4f76ce71cfa1188105d1df&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USB5XCYI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDfEH5ypfdfD9HnsUQKHSQIaUByo7fQn%2FeXXR53g%2BxO%2FgIhAMFGl9mQ76GSHLV%2BT9C%2FECmfg4oZg2QTrqtU7PE72eQtKv8DCBYQABoMNjM3NDIzMTgzODA1IgyuVone4oYIj4NkrZ4q3APgcpRBNcOGD3aHqrQYLLeOtuOxZchYSkE7%2BdjNuXRXAoqfOg%2Bhb8t03l3YNU4lO%2B46BG74qXb6pamip4doAa5PmoiOWuSSIJmWSzZ4Z8zKn5NNLo7oiEjOiVFJrjJZtsgHock%2B%2FVSY0yiOWSoQUYkEHn5ymYzynqjT6Bj4mX%2FH1KEi%2Fu1TeIjelFv1NM8vmvaZTKc%2FpJ4l0TlXMmW9iyqrqiHBwDNiIPxr00AF4VGOxk%2Ber5QNVeUZiS83TylRdV8Vn1qm7lKQ80OGNNvcs33yBBH%2BXe%2BzTB1i1HJG70A%2Bgm1AOaGs7tHP6uaAq2T2c06HWKnPT9MSf%2Byg9IXyHNBkfqE8QycNvxkfw14ixzW5i3utHCd7reVnk%2FBNlQBsx8f5mwrdcuz194%2BSXHrhghmvUhcoQ1FDkLjlh5MTSo707ArJbecDIt2BYdiG84FE2gYm%2BWXbZKYQHqj0rzQgLUDV%2FBXPcKPgSSCYdhJfir0aWtt3CJIWfoJ%2FsEb%2FkqjvQQfxChPctoYHsLWa3Uv%2BagvcKCktOZDh80tFSxAoeS75xBCbOtjxZJUj4Mv56DiKVOOQeYngQrFQwM3waDKbE5Tid0Q0AcbCGkuOpbutYrqLtJghTxXJWdCjL5dFuTCD8YK9BjqkASkBz4qVIZulek3mpISU7vYW5DkNoklzX4IJ9teB46pLVUH3kbdnsZ5Zz6ld1RmTnDVetdhkT31jK8GKvqPcnqX8Ruy27YPjnSPTFLdFYbHqnS4EA6YRRXcPyZXyM3ZdxxrazPCt6b4AJcNJVtzxryP911tB0sSOU8PzAk12%2FWkggvf5DC6eig5kOqlhbW3aTZt3OyWssQo3XRpGleegkevuFjz8&X-Amz-Signature=6d8afe7cbe9aabd4233cb2ca5f8fb91d3ff6ea0aa05a224c3c8bf012029ae662&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USB5XCYI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDfEH5ypfdfD9HnsUQKHSQIaUByo7fQn%2FeXXR53g%2BxO%2FgIhAMFGl9mQ76GSHLV%2BT9C%2FECmfg4oZg2QTrqtU7PE72eQtKv8DCBYQABoMNjM3NDIzMTgzODA1IgyuVone4oYIj4NkrZ4q3APgcpRBNcOGD3aHqrQYLLeOtuOxZchYSkE7%2BdjNuXRXAoqfOg%2Bhb8t03l3YNU4lO%2B46BG74qXb6pamip4doAa5PmoiOWuSSIJmWSzZ4Z8zKn5NNLo7oiEjOiVFJrjJZtsgHock%2B%2FVSY0yiOWSoQUYkEHn5ymYzynqjT6Bj4mX%2FH1KEi%2Fu1TeIjelFv1NM8vmvaZTKc%2FpJ4l0TlXMmW9iyqrqiHBwDNiIPxr00AF4VGOxk%2Ber5QNVeUZiS83TylRdV8Vn1qm7lKQ80OGNNvcs33yBBH%2BXe%2BzTB1i1HJG70A%2Bgm1AOaGs7tHP6uaAq2T2c06HWKnPT9MSf%2Byg9IXyHNBkfqE8QycNvxkfw14ixzW5i3utHCd7reVnk%2FBNlQBsx8f5mwrdcuz194%2BSXHrhghmvUhcoQ1FDkLjlh5MTSo707ArJbecDIt2BYdiG84FE2gYm%2BWXbZKYQHqj0rzQgLUDV%2FBXPcKPgSSCYdhJfir0aWtt3CJIWfoJ%2FsEb%2FkqjvQQfxChPctoYHsLWa3Uv%2BagvcKCktOZDh80tFSxAoeS75xBCbOtjxZJUj4Mv56DiKVOOQeYngQrFQwM3waDKbE5Tid0Q0AcbCGkuOpbutYrqLtJghTxXJWdCjL5dFuTCD8YK9BjqkASkBz4qVIZulek3mpISU7vYW5DkNoklzX4IJ9teB46pLVUH3kbdnsZ5Zz6ld1RmTnDVetdhkT31jK8GKvqPcnqX8Ruy27YPjnSPTFLdFYbHqnS4EA6YRRXcPyZXyM3ZdxxrazPCt6b4AJcNJVtzxryP911tB0sSOU8PzAk12%2FWkggvf5DC6eig5kOqlhbW3aTZt3OyWssQo3XRpGleegkevuFjz8&X-Amz-Signature=d7038eb0e42df585d84a90dc5b78d16f179811037f4f27632a31e77b92160b6e&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USB5XCYI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDfEH5ypfdfD9HnsUQKHSQIaUByo7fQn%2FeXXR53g%2BxO%2FgIhAMFGl9mQ76GSHLV%2BT9C%2FECmfg4oZg2QTrqtU7PE72eQtKv8DCBYQABoMNjM3NDIzMTgzODA1IgyuVone4oYIj4NkrZ4q3APgcpRBNcOGD3aHqrQYLLeOtuOxZchYSkE7%2BdjNuXRXAoqfOg%2Bhb8t03l3YNU4lO%2B46BG74qXb6pamip4doAa5PmoiOWuSSIJmWSzZ4Z8zKn5NNLo7oiEjOiVFJrjJZtsgHock%2B%2FVSY0yiOWSoQUYkEHn5ymYzynqjT6Bj4mX%2FH1KEi%2Fu1TeIjelFv1NM8vmvaZTKc%2FpJ4l0TlXMmW9iyqrqiHBwDNiIPxr00AF4VGOxk%2Ber5QNVeUZiS83TylRdV8Vn1qm7lKQ80OGNNvcs33yBBH%2BXe%2BzTB1i1HJG70A%2Bgm1AOaGs7tHP6uaAq2T2c06HWKnPT9MSf%2Byg9IXyHNBkfqE8QycNvxkfw14ixzW5i3utHCd7reVnk%2FBNlQBsx8f5mwrdcuz194%2BSXHrhghmvUhcoQ1FDkLjlh5MTSo707ArJbecDIt2BYdiG84FE2gYm%2BWXbZKYQHqj0rzQgLUDV%2FBXPcKPgSSCYdhJfir0aWtt3CJIWfoJ%2FsEb%2FkqjvQQfxChPctoYHsLWa3Uv%2BagvcKCktOZDh80tFSxAoeS75xBCbOtjxZJUj4Mv56DiKVOOQeYngQrFQwM3waDKbE5Tid0Q0AcbCGkuOpbutYrqLtJghTxXJWdCjL5dFuTCD8YK9BjqkASkBz4qVIZulek3mpISU7vYW5DkNoklzX4IJ9teB46pLVUH3kbdnsZ5Zz6ld1RmTnDVetdhkT31jK8GKvqPcnqX8Ruy27YPjnSPTFLdFYbHqnS4EA6YRRXcPyZXyM3ZdxxrazPCt6b4AJcNJVtzxryP911tB0sSOU8PzAk12%2FWkggvf5DC6eig5kOqlhbW3aTZt3OyWssQo3XRpGleegkevuFjz8&X-Amz-Signature=6399d1a04712d9b9345a481c1f1e2cd0e926b195e91da8e3a7980b9c0a37ecf1&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
