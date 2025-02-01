

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WRCNDMV7%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBllrWaD3QphKQQrPWozmiEwEKkdIw9JOG7Z50v9CCZ7AiATNBWypb5pd3x2CopTvItDz%2Fx7ADc5NZzBXMCRGKuiPCqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlOzL9QJJ2xDYwBDZKtwDSu1TRhSFUorWa0EBbCZIhSfVvcxw39jz%2Fco28Ci4FpXJ4mjmJk5yJNjKIpM5K1l4RSaNCxk3AcxeuFxXeZ8yeJHBHjJQkOeftOv5b0bC3a75v3B4mEA8RURPNNFTGJ442kR8Z0o4IhAoL3i0jtkXhIeO8K%2FDeTYd8vB0v9TXZNW1puT6gA0LLp8x0nIKxCOgNC7K5HggJiD91ZJKTlGJ38rTG2j1iIO3dqZbNB6rbpxnhzUBcfIjEkJ4XkUWuo4AgJydvloGjFAk8tOSW4qxsUwu2asGIjrfxwxGqDTsOcZu5kQ4X6RNErjlBGAnBje3giRk0rfPn%2BJ9WG4kiB8nqtEkP8mvhNR9IFNVj54NFrtGwPNVpakiv86r8S7gs2V6l682xN5hQFeKV8bxl7KpPk7fh3P1gOwKm2%2BTMA%2BcQVv92DWL%2FDKDwwvNtlYZU341s4Yl8OtjUwPoKNk4C8SkfNKhPrM1j6xd0MCBTGgVI6denuun8tW4ouSyOlECzXxzytjV3lyux6YKMQoQypdWWC67XGWDy6P36YJUfR2VHMQBzn4wuRdE7iuPSA0y5w%2FEoPsquxUTd8CL2uKdP0Nb1k6Bl8ch6E3n1OUERKzocQJ3smYRmLinbAJweTcwmKT3vAY6pgE0e4znavtG170ybjxZVpMRH5vy0OLGrhJUNeL3kyNTVKFCk8PeRsbirp5Se3QQyyHMbNTrJ12DJ6AUFYlBWGtNMgALORuwseI7kPzBgAvGnDLcqW4SlsBRMp0bjGu4EHuNUVFdgw%2FpUeb%2Be%2Bw1f03X9TqgKrnwgbGg%2FPg2e%2FeMQ4CC8sJlV4xpSAHo7Lkvt2cOXmVuPEx%2BdcDhxBqj%2F1vkPC2t3erJ&X-Amz-Signature=cc7c40bc6f2419e89c3efea30d3cc53e9215459dbfa9b59c48064132f66fa802&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WRCNDMV7%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBllrWaD3QphKQQrPWozmiEwEKkdIw9JOG7Z50v9CCZ7AiATNBWypb5pd3x2CopTvItDz%2Fx7ADc5NZzBXMCRGKuiPCqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlOzL9QJJ2xDYwBDZKtwDSu1TRhSFUorWa0EBbCZIhSfVvcxw39jz%2Fco28Ci4FpXJ4mjmJk5yJNjKIpM5K1l4RSaNCxk3AcxeuFxXeZ8yeJHBHjJQkOeftOv5b0bC3a75v3B4mEA8RURPNNFTGJ442kR8Z0o4IhAoL3i0jtkXhIeO8K%2FDeTYd8vB0v9TXZNW1puT6gA0LLp8x0nIKxCOgNC7K5HggJiD91ZJKTlGJ38rTG2j1iIO3dqZbNB6rbpxnhzUBcfIjEkJ4XkUWuo4AgJydvloGjFAk8tOSW4qxsUwu2asGIjrfxwxGqDTsOcZu5kQ4X6RNErjlBGAnBje3giRk0rfPn%2BJ9WG4kiB8nqtEkP8mvhNR9IFNVj54NFrtGwPNVpakiv86r8S7gs2V6l682xN5hQFeKV8bxl7KpPk7fh3P1gOwKm2%2BTMA%2BcQVv92DWL%2FDKDwwvNtlYZU341s4Yl8OtjUwPoKNk4C8SkfNKhPrM1j6xd0MCBTGgVI6denuun8tW4ouSyOlECzXxzytjV3lyux6YKMQoQypdWWC67XGWDy6P36YJUfR2VHMQBzn4wuRdE7iuPSA0y5w%2FEoPsquxUTd8CL2uKdP0Nb1k6Bl8ch6E3n1OUERKzocQJ3smYRmLinbAJweTcwmKT3vAY6pgE0e4znavtG170ybjxZVpMRH5vy0OLGrhJUNeL3kyNTVKFCk8PeRsbirp5Se3QQyyHMbNTrJ12DJ6AUFYlBWGtNMgALORuwseI7kPzBgAvGnDLcqW4SlsBRMp0bjGu4EHuNUVFdgw%2FpUeb%2Be%2Bw1f03X9TqgKrnwgbGg%2FPg2e%2FeMQ4CC8sJlV4xpSAHo7Lkvt2cOXmVuPEx%2BdcDhxBqj%2F1vkPC2t3erJ&X-Amz-Signature=ee89199c307762a3c819fd5479067e2d592f458e8aabe1549687b9e55e98376e&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WRCNDMV7%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBllrWaD3QphKQQrPWozmiEwEKkdIw9JOG7Z50v9CCZ7AiATNBWypb5pd3x2CopTvItDz%2Fx7ADc5NZzBXMCRGKuiPCqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlOzL9QJJ2xDYwBDZKtwDSu1TRhSFUorWa0EBbCZIhSfVvcxw39jz%2Fco28Ci4FpXJ4mjmJk5yJNjKIpM5K1l4RSaNCxk3AcxeuFxXeZ8yeJHBHjJQkOeftOv5b0bC3a75v3B4mEA8RURPNNFTGJ442kR8Z0o4IhAoL3i0jtkXhIeO8K%2FDeTYd8vB0v9TXZNW1puT6gA0LLp8x0nIKxCOgNC7K5HggJiD91ZJKTlGJ38rTG2j1iIO3dqZbNB6rbpxnhzUBcfIjEkJ4XkUWuo4AgJydvloGjFAk8tOSW4qxsUwu2asGIjrfxwxGqDTsOcZu5kQ4X6RNErjlBGAnBje3giRk0rfPn%2BJ9WG4kiB8nqtEkP8mvhNR9IFNVj54NFrtGwPNVpakiv86r8S7gs2V6l682xN5hQFeKV8bxl7KpPk7fh3P1gOwKm2%2BTMA%2BcQVv92DWL%2FDKDwwvNtlYZU341s4Yl8OtjUwPoKNk4C8SkfNKhPrM1j6xd0MCBTGgVI6denuun8tW4ouSyOlECzXxzytjV3lyux6YKMQoQypdWWC67XGWDy6P36YJUfR2VHMQBzn4wuRdE7iuPSA0y5w%2FEoPsquxUTd8CL2uKdP0Nb1k6Bl8ch6E3n1OUERKzocQJ3smYRmLinbAJweTcwmKT3vAY6pgE0e4znavtG170ybjxZVpMRH5vy0OLGrhJUNeL3kyNTVKFCk8PeRsbirp5Se3QQyyHMbNTrJ12DJ6AUFYlBWGtNMgALORuwseI7kPzBgAvGnDLcqW4SlsBRMp0bjGu4EHuNUVFdgw%2FpUeb%2Be%2Bw1f03X9TqgKrnwgbGg%2FPg2e%2FeMQ4CC8sJlV4xpSAHo7Lkvt2cOXmVuPEx%2BdcDhxBqj%2F1vkPC2t3erJ&X-Amz-Signature=e73db9333a026543cc0494aa322e45b40b3f0f7c35dcdec81ae8e62fbb3cef35&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YWXJRO3H%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDBx0hzJi%2F48HblXkKKRy%2BVmVdlIreDOocpnIsKdxw5ZQIhAJ4NN9ospUKB2k1kLlWJQ%2BfbENoi2wTZdT8kwpxFMii2KogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwDPLBmMYsF73FT1z4q3AMviFc11bW1O5Pl1EkjIFET%2BlsE3m3EcR5XefNkCtBdzrAoQ4jDMLNpdpAzy9Css9Jr1wmzyEHbx6I3wFAmKZA0VNmLe%2FBTrKAjVFfanL4ayvoxl0xRPziPlYXGbVRXy59LhKBg6NY2GVWIu%2BV4x5y1oYdbkBv2SVydr592boe%2B9dR8u5js9bMahHBXIfLuey4y5MAzFjFDYfCLr%2B8KehALAbuNESXmBH%2B%2BY8DK54HAzpiHeuPJfyyyXqYo53LT7I4BJObhxnoOLhXlVmvNNY3m%2FM93AFzq85ZLuTRiVGB2UnRo9ird8JEdfI%2Bqifby9Pf9WSsqguWSd8WsymiBkYWJ%2FVePs0lVBHrPXnMPA4qnQwhQKifT8f2l3pdR6LZOqSuORqk29DDQ%2FBIXdEIwwWoFsgzDH0M1yY7n8uCV%2FKh%2BKBlV%2FQcwr9hhYclgWDG6jMyNb%2Bkqly%2F3rJD%2B9C1xjCCLP9o9Sw3y2FtI5VEOaO5c3gMFXAum8suDP6atcSaTo3kehbTgtf3jD7C49sm8BpR1EkENqu9IibiQLproAW9yurAU3h4hOIEW%2B5T5fC9nqo%2FvVOziiOM%2FSKZjThRNTJnHJc8jXIOAGy%2BvbLu78onqsrIQKhVuFB4Zb79mazDbpPe8BjqkAX4Zcw0bULwbxa0RnzhdzB7LKG6eXS6atfgDZ6cSwQlr0hIIF4Mv9JVR8iux2bVDldaeKsAj7yWAjbD7TE5EzzHyYWpuZLl31hCkCISgCRjVlu5ZMCi5uFbULD0O3vgl9BxYAmoz%2FQ%2FbSUIcDawjpIyeSzew6dQyWUtMaH4TW%2Flf25B%2B9ofAvg4LV1%2BrziUQc%2BQgp4IBRbG2Sgb9wFTElq5emtUQ&X-Amz-Signature=549cf9aefcd87f28875524d9a834aecd897737529e82adaebe767775f79f5b8c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QGCSGBUL%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDshUp86Y6qj48sLK8dsTGW2XJjHWt7pdJBLgS48OyJrgIhAOWa7dkDRXu2d3xbdell1Z7bpTBAYR6ejoZQYbZw5Cd6KogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzlwFiJ54qCruJWNKMq3AOQSV0T4dnKO1IgOqj0OSl%2FkqGIdnTDkKKnhowL9v34JDmzSZ8wFt4i46GdQyjZ5iZD6KgqsGzdKG4383bmqT5ZE1KMQsbW869b%2F6hNUnWJqmhE0xxab%2FeBGlyytnhEBrnllZ4JUUhFht5BoAT1G8Pbd78TMp5ZnBsYbZWgNzCXgLQTs0ukmALq2%2B9McQ%2FV2CmSPJhz042%2BeeDyHnkKL3ygc4NNBpVxyAeUN%2BkcYke%2FtDLiq9Tz95elxK9cgVAaSm6C%2BpprBEf%2BH8cen9NB2zpQh4eOU6h0UpYcRmgz58Ok1%2BNhUtW3ki0tiTE2OHm1DRefw00R9tDB2T78H6dF%2FafN6OJzgejBtyqBwMApbvdGo3DbsqQWMhcr%2FCQxAdtGhzikjviBZZOgQzMVS8%2FxUqmA0YMdBH4XsEvKeVBqRXpT7bG2rING3wpZnqGtwzM9%2FPOPQbEatvNEvs%2B7Ux1qg%2FV1mLtIR39i0QV09HvWaJqv7bL1Il1kc1DaZNc5HALBLAjLXE7Y%2BcRO269sRZQq6N8HOgRAjmpsb0j9x6dWRuGNj7nIBZc%2FCrrS1DP1iENzBInkdFxJ0kn%2BP1uJ39coyGZF9bQP%2FLmTNyOhMsXGNO05gnBK%2FvQDcZyiyK8tDTCjpPe8BjqkAXrH6Y6jhk4OB9oY4QYDc%2BFZs7XyinEq8IXp3MLQl8K%2Feae5OD1AJeu%2F88BDzdKc0oII6oTjt%2BJKFuQqAbE0nV4sN9JfEuZwhES8Ep9gDCoB0Lui4nzqVFWFT96ndubahDRx6Z6W6DswKhLBDmdq7eElhmoyC7lC10JyGhLo1ylhfMoIz1%2ByCiFM%2BMNQ9OL1b22n8NUAi37noLBk9SG5QKPiKbWj&X-Amz-Signature=e7019e434f5bb15756fa1a6205132a62baa9c48604f347fc12e500aa5a1593d4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WRCNDMV7%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBllrWaD3QphKQQrPWozmiEwEKkdIw9JOG7Z50v9CCZ7AiATNBWypb5pd3x2CopTvItDz%2Fx7ADc5NZzBXMCRGKuiPCqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlOzL9QJJ2xDYwBDZKtwDSu1TRhSFUorWa0EBbCZIhSfVvcxw39jz%2Fco28Ci4FpXJ4mjmJk5yJNjKIpM5K1l4RSaNCxk3AcxeuFxXeZ8yeJHBHjJQkOeftOv5b0bC3a75v3B4mEA8RURPNNFTGJ442kR8Z0o4IhAoL3i0jtkXhIeO8K%2FDeTYd8vB0v9TXZNW1puT6gA0LLp8x0nIKxCOgNC7K5HggJiD91ZJKTlGJ38rTG2j1iIO3dqZbNB6rbpxnhzUBcfIjEkJ4XkUWuo4AgJydvloGjFAk8tOSW4qxsUwu2asGIjrfxwxGqDTsOcZu5kQ4X6RNErjlBGAnBje3giRk0rfPn%2BJ9WG4kiB8nqtEkP8mvhNR9IFNVj54NFrtGwPNVpakiv86r8S7gs2V6l682xN5hQFeKV8bxl7KpPk7fh3P1gOwKm2%2BTMA%2BcQVv92DWL%2FDKDwwvNtlYZU341s4Yl8OtjUwPoKNk4C8SkfNKhPrM1j6xd0MCBTGgVI6denuun8tW4ouSyOlECzXxzytjV3lyux6YKMQoQypdWWC67XGWDy6P36YJUfR2VHMQBzn4wuRdE7iuPSA0y5w%2FEoPsquxUTd8CL2uKdP0Nb1k6Bl8ch6E3n1OUERKzocQJ3smYRmLinbAJweTcwmKT3vAY6pgE0e4znavtG170ybjxZVpMRH5vy0OLGrhJUNeL3kyNTVKFCk8PeRsbirp5Se3QQyyHMbNTrJ12DJ6AUFYlBWGtNMgALORuwseI7kPzBgAvGnDLcqW4SlsBRMp0bjGu4EHuNUVFdgw%2FpUeb%2Be%2Bw1f03X9TqgKrnwgbGg%2FPg2e%2FeMQ4CC8sJlV4xpSAHo7Lkvt2cOXmVuPEx%2BdcDhxBqj%2F1vkPC2t3erJ&X-Amz-Signature=bea2076acd28d48ff009605a1ed24b485304b53b1dbfa99d28d5518ca9e26dad&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WRCNDMV7%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBllrWaD3QphKQQrPWozmiEwEKkdIw9JOG7Z50v9CCZ7AiATNBWypb5pd3x2CopTvItDz%2Fx7ADc5NZzBXMCRGKuiPCqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlOzL9QJJ2xDYwBDZKtwDSu1TRhSFUorWa0EBbCZIhSfVvcxw39jz%2Fco28Ci4FpXJ4mjmJk5yJNjKIpM5K1l4RSaNCxk3AcxeuFxXeZ8yeJHBHjJQkOeftOv5b0bC3a75v3B4mEA8RURPNNFTGJ442kR8Z0o4IhAoL3i0jtkXhIeO8K%2FDeTYd8vB0v9TXZNW1puT6gA0LLp8x0nIKxCOgNC7K5HggJiD91ZJKTlGJ38rTG2j1iIO3dqZbNB6rbpxnhzUBcfIjEkJ4XkUWuo4AgJydvloGjFAk8tOSW4qxsUwu2asGIjrfxwxGqDTsOcZu5kQ4X6RNErjlBGAnBje3giRk0rfPn%2BJ9WG4kiB8nqtEkP8mvhNR9IFNVj54NFrtGwPNVpakiv86r8S7gs2V6l682xN5hQFeKV8bxl7KpPk7fh3P1gOwKm2%2BTMA%2BcQVv92DWL%2FDKDwwvNtlYZU341s4Yl8OtjUwPoKNk4C8SkfNKhPrM1j6xd0MCBTGgVI6denuun8tW4ouSyOlECzXxzytjV3lyux6YKMQoQypdWWC67XGWDy6P36YJUfR2VHMQBzn4wuRdE7iuPSA0y5w%2FEoPsquxUTd8CL2uKdP0Nb1k6Bl8ch6E3n1OUERKzocQJ3smYRmLinbAJweTcwmKT3vAY6pgE0e4znavtG170ybjxZVpMRH5vy0OLGrhJUNeL3kyNTVKFCk8PeRsbirp5Se3QQyyHMbNTrJ12DJ6AUFYlBWGtNMgALORuwseI7kPzBgAvGnDLcqW4SlsBRMp0bjGu4EHuNUVFdgw%2FpUeb%2Be%2Bw1f03X9TqgKrnwgbGg%2FPg2e%2FeMQ4CC8sJlV4xpSAHo7Lkvt2cOXmVuPEx%2BdcDhxBqj%2F1vkPC2t3erJ&X-Amz-Signature=83d39354cefe88f3607793743bf8705a9c8853a25dbfd0f1c20c0ef2af50066f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WRCNDMV7%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBllrWaD3QphKQQrPWozmiEwEKkdIw9JOG7Z50v9CCZ7AiATNBWypb5pd3x2CopTvItDz%2Fx7ADc5NZzBXMCRGKuiPCqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlOzL9QJJ2xDYwBDZKtwDSu1TRhSFUorWa0EBbCZIhSfVvcxw39jz%2Fco28Ci4FpXJ4mjmJk5yJNjKIpM5K1l4RSaNCxk3AcxeuFxXeZ8yeJHBHjJQkOeftOv5b0bC3a75v3B4mEA8RURPNNFTGJ442kR8Z0o4IhAoL3i0jtkXhIeO8K%2FDeTYd8vB0v9TXZNW1puT6gA0LLp8x0nIKxCOgNC7K5HggJiD91ZJKTlGJ38rTG2j1iIO3dqZbNB6rbpxnhzUBcfIjEkJ4XkUWuo4AgJydvloGjFAk8tOSW4qxsUwu2asGIjrfxwxGqDTsOcZu5kQ4X6RNErjlBGAnBje3giRk0rfPn%2BJ9WG4kiB8nqtEkP8mvhNR9IFNVj54NFrtGwPNVpakiv86r8S7gs2V6l682xN5hQFeKV8bxl7KpPk7fh3P1gOwKm2%2BTMA%2BcQVv92DWL%2FDKDwwvNtlYZU341s4Yl8OtjUwPoKNk4C8SkfNKhPrM1j6xd0MCBTGgVI6denuun8tW4ouSyOlECzXxzytjV3lyux6YKMQoQypdWWC67XGWDy6P36YJUfR2VHMQBzn4wuRdE7iuPSA0y5w%2FEoPsquxUTd8CL2uKdP0Nb1k6Bl8ch6E3n1OUERKzocQJ3smYRmLinbAJweTcwmKT3vAY6pgE0e4znavtG170ybjxZVpMRH5vy0OLGrhJUNeL3kyNTVKFCk8PeRsbirp5Se3QQyyHMbNTrJ12DJ6AUFYlBWGtNMgALORuwseI7kPzBgAvGnDLcqW4SlsBRMp0bjGu4EHuNUVFdgw%2FpUeb%2Be%2Bw1f03X9TqgKrnwgbGg%2FPg2e%2FeMQ4CC8sJlV4xpSAHo7Lkvt2cOXmVuPEx%2BdcDhxBqj%2F1vkPC2t3erJ&X-Amz-Signature=bd9a0cf9dc31c7d2b977d17af75fe59fce221b2818319bcf19f1a126c75a866f&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WRCNDMV7%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBllrWaD3QphKQQrPWozmiEwEKkdIw9JOG7Z50v9CCZ7AiATNBWypb5pd3x2CopTvItDz%2Fx7ADc5NZzBXMCRGKuiPCqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlOzL9QJJ2xDYwBDZKtwDSu1TRhSFUorWa0EBbCZIhSfVvcxw39jz%2Fco28Ci4FpXJ4mjmJk5yJNjKIpM5K1l4RSaNCxk3AcxeuFxXeZ8yeJHBHjJQkOeftOv5b0bC3a75v3B4mEA8RURPNNFTGJ442kR8Z0o4IhAoL3i0jtkXhIeO8K%2FDeTYd8vB0v9TXZNW1puT6gA0LLp8x0nIKxCOgNC7K5HggJiD91ZJKTlGJ38rTG2j1iIO3dqZbNB6rbpxnhzUBcfIjEkJ4XkUWuo4AgJydvloGjFAk8tOSW4qxsUwu2asGIjrfxwxGqDTsOcZu5kQ4X6RNErjlBGAnBje3giRk0rfPn%2BJ9WG4kiB8nqtEkP8mvhNR9IFNVj54NFrtGwPNVpakiv86r8S7gs2V6l682xN5hQFeKV8bxl7KpPk7fh3P1gOwKm2%2BTMA%2BcQVv92DWL%2FDKDwwvNtlYZU341s4Yl8OtjUwPoKNk4C8SkfNKhPrM1j6xd0MCBTGgVI6denuun8tW4ouSyOlECzXxzytjV3lyux6YKMQoQypdWWC67XGWDy6P36YJUfR2VHMQBzn4wuRdE7iuPSA0y5w%2FEoPsquxUTd8CL2uKdP0Nb1k6Bl8ch6E3n1OUERKzocQJ3smYRmLinbAJweTcwmKT3vAY6pgE0e4znavtG170ybjxZVpMRH5vy0OLGrhJUNeL3kyNTVKFCk8PeRsbirp5Se3QQyyHMbNTrJ12DJ6AUFYlBWGtNMgALORuwseI7kPzBgAvGnDLcqW4SlsBRMp0bjGu4EHuNUVFdgw%2FpUeb%2Be%2Bw1f03X9TqgKrnwgbGg%2FPg2e%2FeMQ4CC8sJlV4xpSAHo7Lkvt2cOXmVuPEx%2BdcDhxBqj%2F1vkPC2t3erJ&X-Amz-Signature=c30a9fa3e561a30e009a9eae5981389d1988ed96a706eb7ac237c859abad2b7c&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
