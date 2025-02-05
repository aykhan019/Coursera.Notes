

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667FW6FVZW%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQDukirVx0nIeAjKMGArYAaNUdB1r1cx7uxyJUBGdgdu4gIhANnqtU%2BYRH%2FNpUZhny4p0gINIsVf36jFZ7%2F356uPaRRiKv8DCEQQABoMNjM3NDIzMTgzODA1Igw%2BQxoEgnt2XoRgrdEq3AN2FqPKhLbkk19R3QrARJnVULH14GJZ6z7Hfs6vdhOx3WrjUEFkhZbizSoModTDckG36FCjui3dQ54W%2BmHGk54cFYZRpgOD2PFcaiBLWI8eJiyZYS%2B6Wp7moEapQLwCwJtSC4loOOt8Y5lVxwI7DMffI1hioI9%2BZq1IzkkXqjksv%2BcFi%2BSlWb0oCWDs%2FauAAsc415Iu7%2FHbNLcHX0EHrsD7MuAZDG%2FYRh9zx1pY99fV%2BnMDGOpcx88X6xlQhR2QRcx823eUryArKOeftXEUW4tKTt%2BiS%2FloMSE6VqX9Yr4PYisMZnYq%2F%2B8dGVsMZA9ONw96H7mNbjfhtHFTglqrEfbliGchD18l0LowzrPJCNV%2Bu9oAziaW0QeiFZ8%2FqVdJ6zZzWEYsvNaXeRjYEGaKXKg1yjsmM4VvvgniosyrW7AD2WErhq7HBzumn88bFejxa3yiWnv7OUD8hX9teALEmnRCG6mWgv6FyJbKqTdcTGg119z5iS5OeuL8WU059570uxoVlCBH4vHadQYpqrANcK0pmubPhHbY%2FscVVHSVTo5hQG35SjBUZxkSAXFyXZz1kYktQHK4kXsxBovH71aBvMqxfgZbwAgpf7pTAk8CrBzgidteH1EtUZ99b%2BE8WDDeio29BjqkAUtGYg8cqRnHXSJv82SLl1CDsSocDlQLBbKTv3NDk5XEmyI%2F3kLbQ%2BGbqJll6BFIv03xhif0K3coTD0WlTwdqkLkhua1V2BGGTak4O3EK217EZhwWu2xHU55cUNQ48m0n05ACRsPYEvV28yVF44p4wydvzJTZQJTpNt8lWtVswLwFwT%2BIuUeC5MdJ6GFEdOXt8dpkCzbuBEniqC31OOJlWSShkgA&X-Amz-Signature=ee4d387bc688ad346ec7f9dfcd8f858bb15dd539d2c62c1d8d2663a672b0f377&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667FW6FVZW%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQDukirVx0nIeAjKMGArYAaNUdB1r1cx7uxyJUBGdgdu4gIhANnqtU%2BYRH%2FNpUZhny4p0gINIsVf36jFZ7%2F356uPaRRiKv8DCEQQABoMNjM3NDIzMTgzODA1Igw%2BQxoEgnt2XoRgrdEq3AN2FqPKhLbkk19R3QrARJnVULH14GJZ6z7Hfs6vdhOx3WrjUEFkhZbizSoModTDckG36FCjui3dQ54W%2BmHGk54cFYZRpgOD2PFcaiBLWI8eJiyZYS%2B6Wp7moEapQLwCwJtSC4loOOt8Y5lVxwI7DMffI1hioI9%2BZq1IzkkXqjksv%2BcFi%2BSlWb0oCWDs%2FauAAsc415Iu7%2FHbNLcHX0EHrsD7MuAZDG%2FYRh9zx1pY99fV%2BnMDGOpcx88X6xlQhR2QRcx823eUryArKOeftXEUW4tKTt%2BiS%2FloMSE6VqX9Yr4PYisMZnYq%2F%2B8dGVsMZA9ONw96H7mNbjfhtHFTglqrEfbliGchD18l0LowzrPJCNV%2Bu9oAziaW0QeiFZ8%2FqVdJ6zZzWEYsvNaXeRjYEGaKXKg1yjsmM4VvvgniosyrW7AD2WErhq7HBzumn88bFejxa3yiWnv7OUD8hX9teALEmnRCG6mWgv6FyJbKqTdcTGg119z5iS5OeuL8WU059570uxoVlCBH4vHadQYpqrANcK0pmubPhHbY%2FscVVHSVTo5hQG35SjBUZxkSAXFyXZz1kYktQHK4kXsxBovH71aBvMqxfgZbwAgpf7pTAk8CrBzgidteH1EtUZ99b%2BE8WDDeio29BjqkAUtGYg8cqRnHXSJv82SLl1CDsSocDlQLBbKTv3NDk5XEmyI%2F3kLbQ%2BGbqJll6BFIv03xhif0K3coTD0WlTwdqkLkhua1V2BGGTak4O3EK217EZhwWu2xHU55cUNQ48m0n05ACRsPYEvV28yVF44p4wydvzJTZQJTpNt8lWtVswLwFwT%2BIuUeC5MdJ6GFEdOXt8dpkCzbuBEniqC31OOJlWSShkgA&X-Amz-Signature=c645faff8095805983937bfa17df46be0b72461e787ad9e9f453dfcc9f2f9e76&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667FW6FVZW%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQDukirVx0nIeAjKMGArYAaNUdB1r1cx7uxyJUBGdgdu4gIhANnqtU%2BYRH%2FNpUZhny4p0gINIsVf36jFZ7%2F356uPaRRiKv8DCEQQABoMNjM3NDIzMTgzODA1Igw%2BQxoEgnt2XoRgrdEq3AN2FqPKhLbkk19R3QrARJnVULH14GJZ6z7Hfs6vdhOx3WrjUEFkhZbizSoModTDckG36FCjui3dQ54W%2BmHGk54cFYZRpgOD2PFcaiBLWI8eJiyZYS%2B6Wp7moEapQLwCwJtSC4loOOt8Y5lVxwI7DMffI1hioI9%2BZq1IzkkXqjksv%2BcFi%2BSlWb0oCWDs%2FauAAsc415Iu7%2FHbNLcHX0EHrsD7MuAZDG%2FYRh9zx1pY99fV%2BnMDGOpcx88X6xlQhR2QRcx823eUryArKOeftXEUW4tKTt%2BiS%2FloMSE6VqX9Yr4PYisMZnYq%2F%2B8dGVsMZA9ONw96H7mNbjfhtHFTglqrEfbliGchD18l0LowzrPJCNV%2Bu9oAziaW0QeiFZ8%2FqVdJ6zZzWEYsvNaXeRjYEGaKXKg1yjsmM4VvvgniosyrW7AD2WErhq7HBzumn88bFejxa3yiWnv7OUD8hX9teALEmnRCG6mWgv6FyJbKqTdcTGg119z5iS5OeuL8WU059570uxoVlCBH4vHadQYpqrANcK0pmubPhHbY%2FscVVHSVTo5hQG35SjBUZxkSAXFyXZz1kYktQHK4kXsxBovH71aBvMqxfgZbwAgpf7pTAk8CrBzgidteH1EtUZ99b%2BE8WDDeio29BjqkAUtGYg8cqRnHXSJv82SLl1CDsSocDlQLBbKTv3NDk5XEmyI%2F3kLbQ%2BGbqJll6BFIv03xhif0K3coTD0WlTwdqkLkhua1V2BGGTak4O3EK217EZhwWu2xHU55cUNQ48m0n05ACRsPYEvV28yVF44p4wydvzJTZQJTpNt8lWtVswLwFwT%2BIuUeC5MdJ6GFEdOXt8dpkCzbuBEniqC31OOJlWSShkgA&X-Amz-Signature=ebb0fa8b237cfe4b3cf2e850ec257bc59f091f35f01680189931271900bd5177&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UN7MKCE6%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIQCnEkho%2Byek1PaHmLek%2FN%2FW1iPaUB2f%2FevUu4yzAoeVOgIgGryxhQsxcgPhHKcHmahahBrJGZ1TeCqtD6hWD8YaV14q%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDE7nGKsPhSVhWtLuuircA2MYuh6ygp5clq7BwxQvqqRpBfHwZiJdxIXkOP%2FkXrM%2FCqPqOMLlWuNKhXOmrK6WwGDFkZ%2B9EC01%2BlNNoGf3zGhHN%2B35FZTVB4M4V%2Bb8gVT0K779Nj%2BziAbKsABrOrne8STha54LbY%2BuSmSRTv9dd3sRDH%2Fv5bYc%2BvZE0Ng27RC1y%2Fv65tYY6g15438%2B7eCpHNNoAeI15eHrtJQFaSdvrD4bY%2BDWslcVSGt4TTjKSrsymXlJwTV09l%2BMvW24cvrVaPE9awxehIl87%2B9b6UbqJz67fR1WJGaIylpQW0%2B57%2FV4Dg73iPSm%2FGw3qtD9GIcSsuABZuWZZekoKgkH7jsbY99zb6RgM24YgoTr6%2ByQNTfbhzhiVSVWuXJ5NeqQpgkqzXzfQEORNZmYw1MWu7lX6Poh%2FYBHYwW5srJVJDOMpjn9V9OcSpmz4PtHJ627dnxxbSD1k3VhNWDtVkr7%2FhOOxnQQ%2B%2FIXZ%2BitvQhliNNQZ9KqxIbY%2FXA5aSu1BQC%2FPAg1%2F%2FTu56BqLkxSzCLXYyxUmP4UCM945ix4KrRdO2McQW6olUAMwwhKMhz745Na1Rj9iK8wey0o8Q7%2FWR3jrNUPLu62NdxH%2B%2BFrZnc74v9pI0lill9WVj5UghrrvVPaMNWKjb0GOqUBCqsOUihrO%2BelzH7QHrY%2BocB1oUYrqWY9M1%2BM7aZ4nKDb0nHS6ai06tpLDt6fFnM9yEVWCMxczBH%2FNv6un6fT%2F5l2WS0DVrnwQfzVf50npq19x9XxW0snD2CpQC0n%2BvweIHjrsJvrwDMSZHqLCKbOclurQIVjcXNI4U4gWNUwPhoGGYZzwSaKHDGKSW0SrlaQTmCk6PWzr8gyD1zjhBmk0ucOQj5m&X-Amz-Signature=392e4243b232a348e5cecb169e31bec9ebab2528ff0fef948dd03c44723f01fe&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZV2CM53R%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJGMEQCIFd16ikSg5tJMJTL7PipHaEgmJ9zBQAbXKUefI48Jo1BAiB%2F%2FrEzfxGKyNLYcV2TthGNccDjE19TDLmj3NgIF3x6Jir%2FAwhEEAAaDDYzNzQyMzE4MzgwNSIM0nNYw5VyAbf0ktwcKtwDyKugvkrEoBoMT5afF4UD6xvED4gNeHCsq6xQ3SVQM6Hc%2F8GaNbUHQxY6S4EEND60lwZCT7UaMhD4qgu6VddeY5vHYWVGCSXFhGexTD%2B3QC2TqWTs%2FZSpcAzzUWX8BMnzGDjKRkjUuHPNlIsfJU7ivQ3wW72xPgEcas88oDENfWS%2FlExj5os1ZZbgqKR3ObMKbnwCawxe76Tyota5eetPOS1AaGFbMcrnadqnNVOFBJvrb%2FjBaKvRCzEciiGjTNo33fheXur%2FiuAlshDBc7oqzUAXXRMtQbQ4%2BAvEh6W1%2FFJxzZQVV%2BjoDJ8ho85vUoVmoqds%2B6zzrs%2FPFu3vCqbLJ1cJzjS8HbfacKufy2XxHVQQI32BYKN8HZrcMRwxNu%2BHXhZ9iWCWC5NGJc%2BB2gq5iPRkpecjFpGVE9tHTZnyKinxs%2F7Q%2B3CxeHfaB29A057ZfBRvXArRFd6iOg73o9ji7z3SJxyYvmDLWalpBvr%2FxCmCNDEDmNKX4Uj%2BmCEFiHGucvrHdnpxkCm0ra16e4h%2BZNNc5pH6DxOZBXudhYapz%2BcQ7NybASVBkdZsFPERFeWd91chqh11lIUiabH9kWqTqgg1FHTxQSOuNRF95ffya8rXGJcrNeXVXm6IzIUwrIuNvQY6pgGwFdH%2FxJnmOUCH4vnG7chaUOLAiS6rBWUX%2BOQcdD9UIbTCNJuHuCJx1ec40uJNFkFino8M9MfQ%2BaOU8hnfsuAaQuZ4MPqANQ9kQTHhtiRAWu0wwu6pGeXU7Y%2FhpL0hhZyFf0Ir%2FX%2Fz0JK52BQaBJS6X3E%2BzckxuNBj%2FGQRQnZcrBJcKz2EviQ3IyLwF7bU44fvIaq1FuKRzOIScAZHgpOElMXPTBhZ&X-Amz-Signature=994f7b2eaf3ebf03faeae3cbaa34ae288f8f5245e94fdcdc0086d0ad55a4a931&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667FW6FVZW%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQDukirVx0nIeAjKMGArYAaNUdB1r1cx7uxyJUBGdgdu4gIhANnqtU%2BYRH%2FNpUZhny4p0gINIsVf36jFZ7%2F356uPaRRiKv8DCEQQABoMNjM3NDIzMTgzODA1Igw%2BQxoEgnt2XoRgrdEq3AN2FqPKhLbkk19R3QrARJnVULH14GJZ6z7Hfs6vdhOx3WrjUEFkhZbizSoModTDckG36FCjui3dQ54W%2BmHGk54cFYZRpgOD2PFcaiBLWI8eJiyZYS%2B6Wp7moEapQLwCwJtSC4loOOt8Y5lVxwI7DMffI1hioI9%2BZq1IzkkXqjksv%2BcFi%2BSlWb0oCWDs%2FauAAsc415Iu7%2FHbNLcHX0EHrsD7MuAZDG%2FYRh9zx1pY99fV%2BnMDGOpcx88X6xlQhR2QRcx823eUryArKOeftXEUW4tKTt%2BiS%2FloMSE6VqX9Yr4PYisMZnYq%2F%2B8dGVsMZA9ONw96H7mNbjfhtHFTglqrEfbliGchD18l0LowzrPJCNV%2Bu9oAziaW0QeiFZ8%2FqVdJ6zZzWEYsvNaXeRjYEGaKXKg1yjsmM4VvvgniosyrW7AD2WErhq7HBzumn88bFejxa3yiWnv7OUD8hX9teALEmnRCG6mWgv6FyJbKqTdcTGg119z5iS5OeuL8WU059570uxoVlCBH4vHadQYpqrANcK0pmubPhHbY%2FscVVHSVTo5hQG35SjBUZxkSAXFyXZz1kYktQHK4kXsxBovH71aBvMqxfgZbwAgpf7pTAk8CrBzgidteH1EtUZ99b%2BE8WDDeio29BjqkAUtGYg8cqRnHXSJv82SLl1CDsSocDlQLBbKTv3NDk5XEmyI%2F3kLbQ%2BGbqJll6BFIv03xhif0K3coTD0WlTwdqkLkhua1V2BGGTak4O3EK217EZhwWu2xHU55cUNQ48m0n05ACRsPYEvV28yVF44p4wydvzJTZQJTpNt8lWtVswLwFwT%2BIuUeC5MdJ6GFEdOXt8dpkCzbuBEniqC31OOJlWSShkgA&X-Amz-Signature=baf3e128a4668391911a027b435008ac8cafb0b9ff8da9387f79f23e3e759a0c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667FW6FVZW%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQDukirVx0nIeAjKMGArYAaNUdB1r1cx7uxyJUBGdgdu4gIhANnqtU%2BYRH%2FNpUZhny4p0gINIsVf36jFZ7%2F356uPaRRiKv8DCEQQABoMNjM3NDIzMTgzODA1Igw%2BQxoEgnt2XoRgrdEq3AN2FqPKhLbkk19R3QrARJnVULH14GJZ6z7Hfs6vdhOx3WrjUEFkhZbizSoModTDckG36FCjui3dQ54W%2BmHGk54cFYZRpgOD2PFcaiBLWI8eJiyZYS%2B6Wp7moEapQLwCwJtSC4loOOt8Y5lVxwI7DMffI1hioI9%2BZq1IzkkXqjksv%2BcFi%2BSlWb0oCWDs%2FauAAsc415Iu7%2FHbNLcHX0EHrsD7MuAZDG%2FYRh9zx1pY99fV%2BnMDGOpcx88X6xlQhR2QRcx823eUryArKOeftXEUW4tKTt%2BiS%2FloMSE6VqX9Yr4PYisMZnYq%2F%2B8dGVsMZA9ONw96H7mNbjfhtHFTglqrEfbliGchD18l0LowzrPJCNV%2Bu9oAziaW0QeiFZ8%2FqVdJ6zZzWEYsvNaXeRjYEGaKXKg1yjsmM4VvvgniosyrW7AD2WErhq7HBzumn88bFejxa3yiWnv7OUD8hX9teALEmnRCG6mWgv6FyJbKqTdcTGg119z5iS5OeuL8WU059570uxoVlCBH4vHadQYpqrANcK0pmubPhHbY%2FscVVHSVTo5hQG35SjBUZxkSAXFyXZz1kYktQHK4kXsxBovH71aBvMqxfgZbwAgpf7pTAk8CrBzgidteH1EtUZ99b%2BE8WDDeio29BjqkAUtGYg8cqRnHXSJv82SLl1CDsSocDlQLBbKTv3NDk5XEmyI%2F3kLbQ%2BGbqJll6BFIv03xhif0K3coTD0WlTwdqkLkhua1V2BGGTak4O3EK217EZhwWu2xHU55cUNQ48m0n05ACRsPYEvV28yVF44p4wydvzJTZQJTpNt8lWtVswLwFwT%2BIuUeC5MdJ6GFEdOXt8dpkCzbuBEniqC31OOJlWSShkgA&X-Amz-Signature=c6ed8ae9f8e6f248cc6c21bf8b2c2eb556a30c5ec8c1faf03e0feb9c54a4241d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667FW6FVZW%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQDukirVx0nIeAjKMGArYAaNUdB1r1cx7uxyJUBGdgdu4gIhANnqtU%2BYRH%2FNpUZhny4p0gINIsVf36jFZ7%2F356uPaRRiKv8DCEQQABoMNjM3NDIzMTgzODA1Igw%2BQxoEgnt2XoRgrdEq3AN2FqPKhLbkk19R3QrARJnVULH14GJZ6z7Hfs6vdhOx3WrjUEFkhZbizSoModTDckG36FCjui3dQ54W%2BmHGk54cFYZRpgOD2PFcaiBLWI8eJiyZYS%2B6Wp7moEapQLwCwJtSC4loOOt8Y5lVxwI7DMffI1hioI9%2BZq1IzkkXqjksv%2BcFi%2BSlWb0oCWDs%2FauAAsc415Iu7%2FHbNLcHX0EHrsD7MuAZDG%2FYRh9zx1pY99fV%2BnMDGOpcx88X6xlQhR2QRcx823eUryArKOeftXEUW4tKTt%2BiS%2FloMSE6VqX9Yr4PYisMZnYq%2F%2B8dGVsMZA9ONw96H7mNbjfhtHFTglqrEfbliGchD18l0LowzrPJCNV%2Bu9oAziaW0QeiFZ8%2FqVdJ6zZzWEYsvNaXeRjYEGaKXKg1yjsmM4VvvgniosyrW7AD2WErhq7HBzumn88bFejxa3yiWnv7OUD8hX9teALEmnRCG6mWgv6FyJbKqTdcTGg119z5iS5OeuL8WU059570uxoVlCBH4vHadQYpqrANcK0pmubPhHbY%2FscVVHSVTo5hQG35SjBUZxkSAXFyXZz1kYktQHK4kXsxBovH71aBvMqxfgZbwAgpf7pTAk8CrBzgidteH1EtUZ99b%2BE8WDDeio29BjqkAUtGYg8cqRnHXSJv82SLl1CDsSocDlQLBbKTv3NDk5XEmyI%2F3kLbQ%2BGbqJll6BFIv03xhif0K3coTD0WlTwdqkLkhua1V2BGGTak4O3EK217EZhwWu2xHU55cUNQ48m0n05ACRsPYEvV28yVF44p4wydvzJTZQJTpNt8lWtVswLwFwT%2BIuUeC5MdJ6GFEdOXt8dpkCzbuBEniqC31OOJlWSShkgA&X-Amz-Signature=da8e65a9ba695890870cedb18875e93e06a5cb7041b0243bcf3d3fb344dd7672&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667FW6FVZW%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQDukirVx0nIeAjKMGArYAaNUdB1r1cx7uxyJUBGdgdu4gIhANnqtU%2BYRH%2FNpUZhny4p0gINIsVf36jFZ7%2F356uPaRRiKv8DCEQQABoMNjM3NDIzMTgzODA1Igw%2BQxoEgnt2XoRgrdEq3AN2FqPKhLbkk19R3QrARJnVULH14GJZ6z7Hfs6vdhOx3WrjUEFkhZbizSoModTDckG36FCjui3dQ54W%2BmHGk54cFYZRpgOD2PFcaiBLWI8eJiyZYS%2B6Wp7moEapQLwCwJtSC4loOOt8Y5lVxwI7DMffI1hioI9%2BZq1IzkkXqjksv%2BcFi%2BSlWb0oCWDs%2FauAAsc415Iu7%2FHbNLcHX0EHrsD7MuAZDG%2FYRh9zx1pY99fV%2BnMDGOpcx88X6xlQhR2QRcx823eUryArKOeftXEUW4tKTt%2BiS%2FloMSE6VqX9Yr4PYisMZnYq%2F%2B8dGVsMZA9ONw96H7mNbjfhtHFTglqrEfbliGchD18l0LowzrPJCNV%2Bu9oAziaW0QeiFZ8%2FqVdJ6zZzWEYsvNaXeRjYEGaKXKg1yjsmM4VvvgniosyrW7AD2WErhq7HBzumn88bFejxa3yiWnv7OUD8hX9teALEmnRCG6mWgv6FyJbKqTdcTGg119z5iS5OeuL8WU059570uxoVlCBH4vHadQYpqrANcK0pmubPhHbY%2FscVVHSVTo5hQG35SjBUZxkSAXFyXZz1kYktQHK4kXsxBovH71aBvMqxfgZbwAgpf7pTAk8CrBzgidteH1EtUZ99b%2BE8WDDeio29BjqkAUtGYg8cqRnHXSJv82SLl1CDsSocDlQLBbKTv3NDk5XEmyI%2F3kLbQ%2BGbqJll6BFIv03xhif0K3coTD0WlTwdqkLkhua1V2BGGTak4O3EK217EZhwWu2xHU55cUNQ48m0n05ACRsPYEvV28yVF44p4wydvzJTZQJTpNt8lWtVswLwFwT%2BIuUeC5MdJ6GFEdOXt8dpkCzbuBEniqC31OOJlWSShkgA&X-Amz-Signature=745513b1c0cad03ec0e7a09208220fa7efb34017ec12d2f8abbec7ab5cf10ca0&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
