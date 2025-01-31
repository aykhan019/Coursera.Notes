

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YUPC2R6R%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICU9%2FyqfBa9xP%2Bdn4eZMP0V7xXIg90QdM%2F2DVuGxbLN1AiEAhHAe73PNsFvGXZYP2xfVBfhysUaBuVtP7a1nzaKD8ncqiAQIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEuZvPvr6%2FPFMnhYhyrcA0X3j49aPp2PCWgvc6XzNBVA5CF1XCE1PMt4pO2q0kpy5qxTzawZwY5kdAgua13d%2B6pAmSXPF4F6LAb7nseNJ%2BdwvnNpDBtuhz1BkhCDMxPYIJyIIqgqcSYpTf%2B4Usl6uC3zb5yr5wERF7vHG0vohcPb4y0oTmgS54ztiw3uwgdvpyHt2WK51wrD8wMQMgllBy2xgGZCsA0UvqfUXPghfk3D3YT7afX68mJ6VfNw6yNts%2BBjglsbrYD9ZJ30MREql4WXonH5MCggvrzeV5wQNZWYGGgSzxVJ0O6cpg2aK2gfcGGIFQsTDYwK5g2SC8t6ZPHVQvjMAnqiu3wBrxfDkWwa1cEW6v9LyGx92S6JIA2G0ZyXmxIzEcOONVT6l%2BTmQXpst6Z1bfJ3l2eT5HQFHg7wgtvkNBAyi8smujmKbLUCkkikYPokzpK84wBlMAn6bYwhUYOCNG0mM1weA2%2FTBvgyWVhenF3x3ac73S2YJ2LBhZqA3aVv52b4bzLhYYxovC8IjAOogaD7oXbWfezVrTpvFeC38HkOPNL5nSkAZmv3SaKrPPwzUAg2QfPTy%2BMbWUy9elokMJs%2F%2B4Wr7ErtfhX3N4dEvqjce2O76l6rzRMKiayDNaUXApZnC6WKMKms87wGOqUBTcDMVBf0lbAQKfm30C23ExDEXOUxTeSCWSx48B2lEhCvelcqQGxhzqd4U%2F1kZVVB5ESKe5v923JD9o%2Bis6unDnGqs65zG4S0iA4qtUglKrTeJFvAlT8FGtKRLW2GjqRG75jxlYjynOXUhh6fGIJw3V7O0h3YyNcYQN7tWsbuMTUB4RGcWiywofjkfBScvV6VygeleJPudOkFQ9cmAaaploag3pcT&X-Amz-Signature=df421d728c6f7f34565373c9ae226ec025b519531b4c49c8333fdd3cafaa6763&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YUPC2R6R%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICU9%2FyqfBa9xP%2Bdn4eZMP0V7xXIg90QdM%2F2DVuGxbLN1AiEAhHAe73PNsFvGXZYP2xfVBfhysUaBuVtP7a1nzaKD8ncqiAQIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEuZvPvr6%2FPFMnhYhyrcA0X3j49aPp2PCWgvc6XzNBVA5CF1XCE1PMt4pO2q0kpy5qxTzawZwY5kdAgua13d%2B6pAmSXPF4F6LAb7nseNJ%2BdwvnNpDBtuhz1BkhCDMxPYIJyIIqgqcSYpTf%2B4Usl6uC3zb5yr5wERF7vHG0vohcPb4y0oTmgS54ztiw3uwgdvpyHt2WK51wrD8wMQMgllBy2xgGZCsA0UvqfUXPghfk3D3YT7afX68mJ6VfNw6yNts%2BBjglsbrYD9ZJ30MREql4WXonH5MCggvrzeV5wQNZWYGGgSzxVJ0O6cpg2aK2gfcGGIFQsTDYwK5g2SC8t6ZPHVQvjMAnqiu3wBrxfDkWwa1cEW6v9LyGx92S6JIA2G0ZyXmxIzEcOONVT6l%2BTmQXpst6Z1bfJ3l2eT5HQFHg7wgtvkNBAyi8smujmKbLUCkkikYPokzpK84wBlMAn6bYwhUYOCNG0mM1weA2%2FTBvgyWVhenF3x3ac73S2YJ2LBhZqA3aVv52b4bzLhYYxovC8IjAOogaD7oXbWfezVrTpvFeC38HkOPNL5nSkAZmv3SaKrPPwzUAg2QfPTy%2BMbWUy9elokMJs%2F%2B4Wr7ErtfhX3N4dEvqjce2O76l6rzRMKiayDNaUXApZnC6WKMKms87wGOqUBTcDMVBf0lbAQKfm30C23ExDEXOUxTeSCWSx48B2lEhCvelcqQGxhzqd4U%2F1kZVVB5ESKe5v923JD9o%2Bis6unDnGqs65zG4S0iA4qtUglKrTeJFvAlT8FGtKRLW2GjqRG75jxlYjynOXUhh6fGIJw3V7O0h3YyNcYQN7tWsbuMTUB4RGcWiywofjkfBScvV6VygeleJPudOkFQ9cmAaaploag3pcT&X-Amz-Signature=b05920cf09867c02fe4ea56e8f90ebdc78dc67dbece3f859b2d0f08b6dda2ee6&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YUPC2R6R%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICU9%2FyqfBa9xP%2Bdn4eZMP0V7xXIg90QdM%2F2DVuGxbLN1AiEAhHAe73PNsFvGXZYP2xfVBfhysUaBuVtP7a1nzaKD8ncqiAQIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEuZvPvr6%2FPFMnhYhyrcA0X3j49aPp2PCWgvc6XzNBVA5CF1XCE1PMt4pO2q0kpy5qxTzawZwY5kdAgua13d%2B6pAmSXPF4F6LAb7nseNJ%2BdwvnNpDBtuhz1BkhCDMxPYIJyIIqgqcSYpTf%2B4Usl6uC3zb5yr5wERF7vHG0vohcPb4y0oTmgS54ztiw3uwgdvpyHt2WK51wrD8wMQMgllBy2xgGZCsA0UvqfUXPghfk3D3YT7afX68mJ6VfNw6yNts%2BBjglsbrYD9ZJ30MREql4WXonH5MCggvrzeV5wQNZWYGGgSzxVJ0O6cpg2aK2gfcGGIFQsTDYwK5g2SC8t6ZPHVQvjMAnqiu3wBrxfDkWwa1cEW6v9LyGx92S6JIA2G0ZyXmxIzEcOONVT6l%2BTmQXpst6Z1bfJ3l2eT5HQFHg7wgtvkNBAyi8smujmKbLUCkkikYPokzpK84wBlMAn6bYwhUYOCNG0mM1weA2%2FTBvgyWVhenF3x3ac73S2YJ2LBhZqA3aVv52b4bzLhYYxovC8IjAOogaD7oXbWfezVrTpvFeC38HkOPNL5nSkAZmv3SaKrPPwzUAg2QfPTy%2BMbWUy9elokMJs%2F%2B4Wr7ErtfhX3N4dEvqjce2O76l6rzRMKiayDNaUXApZnC6WKMKms87wGOqUBTcDMVBf0lbAQKfm30C23ExDEXOUxTeSCWSx48B2lEhCvelcqQGxhzqd4U%2F1kZVVB5ESKe5v923JD9o%2Bis6unDnGqs65zG4S0iA4qtUglKrTeJFvAlT8FGtKRLW2GjqRG75jxlYjynOXUhh6fGIJw3V7O0h3YyNcYQN7tWsbuMTUB4RGcWiywofjkfBScvV6VygeleJPudOkFQ9cmAaaploag3pcT&X-Amz-Signature=a05d1fd594755250b8cba59e65ea2f3772a79f302976697ed4b416e1a5d5c3d4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662L4IBQZE%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDdZWXfE5n2aFyCnodJdy4oQ5YzRRqB176q4CX%2B%2FfIoFAiEA%2FJOmvsDECgIZseHd%2F2AQz%2BiZeRdlUeh9LA9D7hfYzfAqiAQIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM9OO0OHaQszfTbaUyrcAziOBW2OsNJywWZofvgj0z%2BSL%2F0mH1Y%2BQwdN9iKSbZqBvA8OQaCYO4IfjFfiebzZG1PHhd2R5%2BQ5QqBkljggelWhXBR6dQUtLFCrPtKN9xb1OhkK5iOEOjSDq%2Fxhn98nbKuC9vh3DlDdMikXzUiUXsG0KJLBcMukfoZ8d5KIKHKF8XzKzU6UPnuWzpQXKF%2FbnNYEZJHJXagPhZgaiUEneDIhwmKilPY2BCQOK0%2BcnGXfxyj7q8bW8iY2fx%2Fk46YdbjxTp%2B3Yh%2FLMoNs1hTRWsyWcKdUdDrxXio5rhATRJvrCecVPxBZ0H2kqcXpaq0UTolGN4WnYZJiydI9tZGBnKv4rQSbTgj5IdWV%2FWsO7k1VEUDJz4Bp5RP8S3hbLe9CyLB8MUCsQ%2FY5NytBlhR5w3Cdg7DQeK7PQr7rgo69PK4BiuOJXGNBsGIJ9R3k9TxA08L5Zgq9fIi0j7I%2BsthgZQVa7%2FcXoSOGfgk4SYBMFWFIdxzP870LxP6IfVkVHI1QN0WXW%2FNHL38MLH5KQ5%2F5fsXargZO4bLUXCWL0s4yfzkBI7tANpNPAJJ%2BmyjMVXUwnI5iXe79n%2FKbYk6t8qvIsS6SLWgaIHk8FVq92D3T2WNCQoUNN8h%2F7PIsfMypyMNes87wGOqUBN88Bg%2BsB8lx0oyfrG7ykFPD8iKMpoO9UmU7sZ5FhqBHwOXwqqMoPrVVaMj8c36oVPNcDXu3dUBMBBqt8TRpbHotENJn8agbe7qzSLWDxUrESEiRhuJrJjGq2Yj1BGJn16t7BRrbfJJ6lOuyP9qWY8khOocRDf%2BI0aPoIbCD9hFYQXP8yS3lkc2Yg6Lb%2FDDIswy9LzinWSQZJNJ4GjBnPNqFlL5Bw&X-Amz-Signature=6f80844cf893c6961e67b7e4ff01e781b12bc9835ab68804aa9526012a660874&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WKD7AXZK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHdz4EQJ%2FsEBU5Ddnif%2F7l4rj6Xi7MZHvQjqVndhRuIyAiEA6x%2BpMo%2BiiAInCf22O8dXDVrNHuZz%2BalLJoZZlPPQEZkqiAQIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG6fNgCUlHjta3H%2FryrcA6GhTNyOphE1AXcAGPd1gpFkRHNyTAIfC5rehJwIkvj99%2BvSxgGC1S2V9L8UI4DhhtyaTzRFVzvTAy0zToTyGvn%2Bw%2FX0llFTYTal7z2EX4NdWFqeZeTwVdwhfSEFdVThwbtFXFdDbiJHSZiQP6HCkIL3rm3EOV3DS3sh9FwXQ%2F8jaddobEU9XVNi3cCPiV5nByTCIseNddDtFkA5%2FwjQkE5c5hU5lDlmMYqamZB07e%2F88esI65GvpQzMGrsGFvdrX39ceLxi1SSjVJaGLO9A11VQ3Rijg8zp%2F%2FeZALDfR41eH6UtHhb2l6JQyoFCQ6KeDjXtLBCUzZ%2BdT7C5uV0MTTf%2FSOhQuhuUYtxLJn94Z4kKvH9OHMyeyPyWi78nmL9CP12LOdkfz%2F3TBsLGF%2BwzmlgWCGIN%2FuyyOlV9ChD69esgA%2FKtghRCW5QUyJe3dvxk5TFSMCJxnARMqQ1umM6YDUXdAOuU5ccpQ4FGNbyVDDSBjv6TSHRwg0fqgqAeFfJO1VAwC49g%2FFH0FWvcEyTzSyxNT7AodkV%2Bk82c0LiMobHAMEg%2B%2B9eRQOoRYtx75rqHiE1K9PmaQz4%2FAU1d3Aoqujph2iD8%2FtddQShuKyQMwpeM9rWYtb%2BQn1mjFMncMKas87wGOqUBuQCvMLLTCIE2Csmr%2BrUGgICdmRef6vSex6rFfd6d1acECv5wWSO1PFhDA7yOVLyOvPilUr%2FN5xmtA0z%2BhDs3ENg69lcXbvK2hp7nRT9AnAnbY0ebg8ld%2BTviYu0rfwcs1t9PqE%2BC1d6NIWouRXJZrE3P1LC%2F317lBiGJUeeAUKfkaN66lbpJ9Ksdk0%2F%2BAWq5reI28IOgNF2r55ZG4M1rDHbc2wAm&X-Amz-Signature=47db927034cfb5fc046ff42f69e0bf7dd3062c63002372da09087003660ce995&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YUPC2R6R%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICU9%2FyqfBa9xP%2Bdn4eZMP0V7xXIg90QdM%2F2DVuGxbLN1AiEAhHAe73PNsFvGXZYP2xfVBfhysUaBuVtP7a1nzaKD8ncqiAQIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEuZvPvr6%2FPFMnhYhyrcA0X3j49aPp2PCWgvc6XzNBVA5CF1XCE1PMt4pO2q0kpy5qxTzawZwY5kdAgua13d%2B6pAmSXPF4F6LAb7nseNJ%2BdwvnNpDBtuhz1BkhCDMxPYIJyIIqgqcSYpTf%2B4Usl6uC3zb5yr5wERF7vHG0vohcPb4y0oTmgS54ztiw3uwgdvpyHt2WK51wrD8wMQMgllBy2xgGZCsA0UvqfUXPghfk3D3YT7afX68mJ6VfNw6yNts%2BBjglsbrYD9ZJ30MREql4WXonH5MCggvrzeV5wQNZWYGGgSzxVJ0O6cpg2aK2gfcGGIFQsTDYwK5g2SC8t6ZPHVQvjMAnqiu3wBrxfDkWwa1cEW6v9LyGx92S6JIA2G0ZyXmxIzEcOONVT6l%2BTmQXpst6Z1bfJ3l2eT5HQFHg7wgtvkNBAyi8smujmKbLUCkkikYPokzpK84wBlMAn6bYwhUYOCNG0mM1weA2%2FTBvgyWVhenF3x3ac73S2YJ2LBhZqA3aVv52b4bzLhYYxovC8IjAOogaD7oXbWfezVrTpvFeC38HkOPNL5nSkAZmv3SaKrPPwzUAg2QfPTy%2BMbWUy9elokMJs%2F%2B4Wr7ErtfhX3N4dEvqjce2O76l6rzRMKiayDNaUXApZnC6WKMKms87wGOqUBTcDMVBf0lbAQKfm30C23ExDEXOUxTeSCWSx48B2lEhCvelcqQGxhzqd4U%2F1kZVVB5ESKe5v923JD9o%2Bis6unDnGqs65zG4S0iA4qtUglKrTeJFvAlT8FGtKRLW2GjqRG75jxlYjynOXUhh6fGIJw3V7O0h3YyNcYQN7tWsbuMTUB4RGcWiywofjkfBScvV6VygeleJPudOkFQ9cmAaaploag3pcT&X-Amz-Signature=2967df968c15c5d2e9deeb555171f570e7cecda162099b372bffb2008114ae51&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YUPC2R6R%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICU9%2FyqfBa9xP%2Bdn4eZMP0V7xXIg90QdM%2F2DVuGxbLN1AiEAhHAe73PNsFvGXZYP2xfVBfhysUaBuVtP7a1nzaKD8ncqiAQIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEuZvPvr6%2FPFMnhYhyrcA0X3j49aPp2PCWgvc6XzNBVA5CF1XCE1PMt4pO2q0kpy5qxTzawZwY5kdAgua13d%2B6pAmSXPF4F6LAb7nseNJ%2BdwvnNpDBtuhz1BkhCDMxPYIJyIIqgqcSYpTf%2B4Usl6uC3zb5yr5wERF7vHG0vohcPb4y0oTmgS54ztiw3uwgdvpyHt2WK51wrD8wMQMgllBy2xgGZCsA0UvqfUXPghfk3D3YT7afX68mJ6VfNw6yNts%2BBjglsbrYD9ZJ30MREql4WXonH5MCggvrzeV5wQNZWYGGgSzxVJ0O6cpg2aK2gfcGGIFQsTDYwK5g2SC8t6ZPHVQvjMAnqiu3wBrxfDkWwa1cEW6v9LyGx92S6JIA2G0ZyXmxIzEcOONVT6l%2BTmQXpst6Z1bfJ3l2eT5HQFHg7wgtvkNBAyi8smujmKbLUCkkikYPokzpK84wBlMAn6bYwhUYOCNG0mM1weA2%2FTBvgyWVhenF3x3ac73S2YJ2LBhZqA3aVv52b4bzLhYYxovC8IjAOogaD7oXbWfezVrTpvFeC38HkOPNL5nSkAZmv3SaKrPPwzUAg2QfPTy%2BMbWUy9elokMJs%2F%2B4Wr7ErtfhX3N4dEvqjce2O76l6rzRMKiayDNaUXApZnC6WKMKms87wGOqUBTcDMVBf0lbAQKfm30C23ExDEXOUxTeSCWSx48B2lEhCvelcqQGxhzqd4U%2F1kZVVB5ESKe5v923JD9o%2Bis6unDnGqs65zG4S0iA4qtUglKrTeJFvAlT8FGtKRLW2GjqRG75jxlYjynOXUhh6fGIJw3V7O0h3YyNcYQN7tWsbuMTUB4RGcWiywofjkfBScvV6VygeleJPudOkFQ9cmAaaploag3pcT&X-Amz-Signature=17936897292a9fdae7a3952e96c524fb691244b7436b9de60f346c2ba02db1de&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YUPC2R6R%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICU9%2FyqfBa9xP%2Bdn4eZMP0V7xXIg90QdM%2F2DVuGxbLN1AiEAhHAe73PNsFvGXZYP2xfVBfhysUaBuVtP7a1nzaKD8ncqiAQIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEuZvPvr6%2FPFMnhYhyrcA0X3j49aPp2PCWgvc6XzNBVA5CF1XCE1PMt4pO2q0kpy5qxTzawZwY5kdAgua13d%2B6pAmSXPF4F6LAb7nseNJ%2BdwvnNpDBtuhz1BkhCDMxPYIJyIIqgqcSYpTf%2B4Usl6uC3zb5yr5wERF7vHG0vohcPb4y0oTmgS54ztiw3uwgdvpyHt2WK51wrD8wMQMgllBy2xgGZCsA0UvqfUXPghfk3D3YT7afX68mJ6VfNw6yNts%2BBjglsbrYD9ZJ30MREql4WXonH5MCggvrzeV5wQNZWYGGgSzxVJ0O6cpg2aK2gfcGGIFQsTDYwK5g2SC8t6ZPHVQvjMAnqiu3wBrxfDkWwa1cEW6v9LyGx92S6JIA2G0ZyXmxIzEcOONVT6l%2BTmQXpst6Z1bfJ3l2eT5HQFHg7wgtvkNBAyi8smujmKbLUCkkikYPokzpK84wBlMAn6bYwhUYOCNG0mM1weA2%2FTBvgyWVhenF3x3ac73S2YJ2LBhZqA3aVv52b4bzLhYYxovC8IjAOogaD7oXbWfezVrTpvFeC38HkOPNL5nSkAZmv3SaKrPPwzUAg2QfPTy%2BMbWUy9elokMJs%2F%2B4Wr7ErtfhX3N4dEvqjce2O76l6rzRMKiayDNaUXApZnC6WKMKms87wGOqUBTcDMVBf0lbAQKfm30C23ExDEXOUxTeSCWSx48B2lEhCvelcqQGxhzqd4U%2F1kZVVB5ESKe5v923JD9o%2Bis6unDnGqs65zG4S0iA4qtUglKrTeJFvAlT8FGtKRLW2GjqRG75jxlYjynOXUhh6fGIJw3V7O0h3YyNcYQN7tWsbuMTUB4RGcWiywofjkfBScvV6VygeleJPudOkFQ9cmAaaploag3pcT&X-Amz-Signature=ebbb1fe6ea800304be09bb76947e94cd38ebe535b2450b26cbb12a6fc57fa710&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YUPC2R6R%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICU9%2FyqfBa9xP%2Bdn4eZMP0V7xXIg90QdM%2F2DVuGxbLN1AiEAhHAe73PNsFvGXZYP2xfVBfhysUaBuVtP7a1nzaKD8ncqiAQIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEuZvPvr6%2FPFMnhYhyrcA0X3j49aPp2PCWgvc6XzNBVA5CF1XCE1PMt4pO2q0kpy5qxTzawZwY5kdAgua13d%2B6pAmSXPF4F6LAb7nseNJ%2BdwvnNpDBtuhz1BkhCDMxPYIJyIIqgqcSYpTf%2B4Usl6uC3zb5yr5wERF7vHG0vohcPb4y0oTmgS54ztiw3uwgdvpyHt2WK51wrD8wMQMgllBy2xgGZCsA0UvqfUXPghfk3D3YT7afX68mJ6VfNw6yNts%2BBjglsbrYD9ZJ30MREql4WXonH5MCggvrzeV5wQNZWYGGgSzxVJ0O6cpg2aK2gfcGGIFQsTDYwK5g2SC8t6ZPHVQvjMAnqiu3wBrxfDkWwa1cEW6v9LyGx92S6JIA2G0ZyXmxIzEcOONVT6l%2BTmQXpst6Z1bfJ3l2eT5HQFHg7wgtvkNBAyi8smujmKbLUCkkikYPokzpK84wBlMAn6bYwhUYOCNG0mM1weA2%2FTBvgyWVhenF3x3ac73S2YJ2LBhZqA3aVv52b4bzLhYYxovC8IjAOogaD7oXbWfezVrTpvFeC38HkOPNL5nSkAZmv3SaKrPPwzUAg2QfPTy%2BMbWUy9elokMJs%2F%2B4Wr7ErtfhX3N4dEvqjce2O76l6rzRMKiayDNaUXApZnC6WKMKms87wGOqUBTcDMVBf0lbAQKfm30C23ExDEXOUxTeSCWSx48B2lEhCvelcqQGxhzqd4U%2F1kZVVB5ESKe5v923JD9o%2Bis6unDnGqs65zG4S0iA4qtUglKrTeJFvAlT8FGtKRLW2GjqRG75jxlYjynOXUhh6fGIJw3V7O0h3YyNcYQN7tWsbuMTUB4RGcWiywofjkfBScvV6VygeleJPudOkFQ9cmAaaploag3pcT&X-Amz-Signature=85f633cd08e7e6be061351c6b5115e5fe3b4ca17e7950d2e07bb1597f096d6ee&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
