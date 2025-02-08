

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6L7372W%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131615Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJIMEYCIQCA%2BGYK%2Ffb4DmqLgBLVNxQIceLLZMNxCWICY7yc5onuBgIhAOz%2BbuzRFEnJ%2Bab7TfTqS8OBztDS1wGauaasQSrzRe31KogECI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxXuQTw2LIyj6KEWacq3AOslP4QEPfmduD2owSTnPCUwjqohoGL7ZpdMGAbsrFjk5xOA5NdA1PV9XiSWpwyEWA168JpybinWV%2FN2fVPuyEvkr6AfAJgBekl%2FLgcV5S6eWxKgpAAamaFmhMeTurl6os6o62euuKRB491xdmq7dYqOyLchj7SbWM1OJhjumaQRX6BqPcec3c7gHtZ8VAZE8Xl0zgGdhi6NOHA4ycvZX1jSq%2F0LPuWRfFZPgZWKhMMOl2leg0zIKbpPQbAa%2FB%2FA8v%2B%2BJnF8LvW9qho5Efrt7ihYs0doX2reSq4hzC6TaXA4O57c9WBnzOPnTr2B9PxqtNH5ixYbowBkyn4JjVz2%2FSkBVmWTGnuU5WVXDichlRTx61YM%2FJ6j94Qw2Ishr1xEKvfLwDpw2UThyJorXQwTC03E%2F%2BYfnZyDW5jflVLgYgpnkJEiOjzd338vsWq73poTlSQ%2FMtmJsLrYHCBjJG7Qu2vYDNH8kHEbxYpp861JRFa0ytUwfYpOjYiqtU%2BiG7cifaOA3FEaZw0fOocR3vlUECKst3VwkRzYurYyoJIe6mlSkwQynrr%2FO2KkzMfUI%2BF0NAI5uv4537YMuHzco8pdQ0l7cX2x1j2usEOOon6Iy63XQ6mV3opyx4A1J%2F5IjChhZ29BjqkAXe69lELAewrX931QCyFsalvfk71i2GYHzJIC%2FQj2N39pPWrioHQz4t0DEkjnfbPwBYiZTzu9h5QLlo1QyATLQKmsCXw9gpppEim%2BztNLcRbxxoCZOhf95%2Bg5Gfp2WcIKNLzOjjfmC4vyVAAj1cvmQLFRe37dOaabpDNZtHnfw6fUUypfoSqHouNxYUT17f0QA0lfPdnyktW6a4JBreNRd7g%2FzOl&X-Amz-Signature=35d3af0b6fd44993a24963e98ff4023710eb698d5b55b3635b2959b1742ae569&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6L7372W%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131615Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJIMEYCIQCA%2BGYK%2Ffb4DmqLgBLVNxQIceLLZMNxCWICY7yc5onuBgIhAOz%2BbuzRFEnJ%2Bab7TfTqS8OBztDS1wGauaasQSrzRe31KogECI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxXuQTw2LIyj6KEWacq3AOslP4QEPfmduD2owSTnPCUwjqohoGL7ZpdMGAbsrFjk5xOA5NdA1PV9XiSWpwyEWA168JpybinWV%2FN2fVPuyEvkr6AfAJgBekl%2FLgcV5S6eWxKgpAAamaFmhMeTurl6os6o62euuKRB491xdmq7dYqOyLchj7SbWM1OJhjumaQRX6BqPcec3c7gHtZ8VAZE8Xl0zgGdhi6NOHA4ycvZX1jSq%2F0LPuWRfFZPgZWKhMMOl2leg0zIKbpPQbAa%2FB%2FA8v%2B%2BJnF8LvW9qho5Efrt7ihYs0doX2reSq4hzC6TaXA4O57c9WBnzOPnTr2B9PxqtNH5ixYbowBkyn4JjVz2%2FSkBVmWTGnuU5WVXDichlRTx61YM%2FJ6j94Qw2Ishr1xEKvfLwDpw2UThyJorXQwTC03E%2F%2BYfnZyDW5jflVLgYgpnkJEiOjzd338vsWq73poTlSQ%2FMtmJsLrYHCBjJG7Qu2vYDNH8kHEbxYpp861JRFa0ytUwfYpOjYiqtU%2BiG7cifaOA3FEaZw0fOocR3vlUECKst3VwkRzYurYyoJIe6mlSkwQynrr%2FO2KkzMfUI%2BF0NAI5uv4537YMuHzco8pdQ0l7cX2x1j2usEOOon6Iy63XQ6mV3opyx4A1J%2F5IjChhZ29BjqkAXe69lELAewrX931QCyFsalvfk71i2GYHzJIC%2FQj2N39pPWrioHQz4t0DEkjnfbPwBYiZTzu9h5QLlo1QyATLQKmsCXw9gpppEim%2BztNLcRbxxoCZOhf95%2Bg5Gfp2WcIKNLzOjjfmC4vyVAAj1cvmQLFRe37dOaabpDNZtHnfw6fUUypfoSqHouNxYUT17f0QA0lfPdnyktW6a4JBreNRd7g%2FzOl&X-Amz-Signature=bb6325950ab2a324b5d765ed5b45ce0fea22284182e9114f7645acbecfc59271&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6L7372W%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131615Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJIMEYCIQCA%2BGYK%2Ffb4DmqLgBLVNxQIceLLZMNxCWICY7yc5onuBgIhAOz%2BbuzRFEnJ%2Bab7TfTqS8OBztDS1wGauaasQSrzRe31KogECI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxXuQTw2LIyj6KEWacq3AOslP4QEPfmduD2owSTnPCUwjqohoGL7ZpdMGAbsrFjk5xOA5NdA1PV9XiSWpwyEWA168JpybinWV%2FN2fVPuyEvkr6AfAJgBekl%2FLgcV5S6eWxKgpAAamaFmhMeTurl6os6o62euuKRB491xdmq7dYqOyLchj7SbWM1OJhjumaQRX6BqPcec3c7gHtZ8VAZE8Xl0zgGdhi6NOHA4ycvZX1jSq%2F0LPuWRfFZPgZWKhMMOl2leg0zIKbpPQbAa%2FB%2FA8v%2B%2BJnF8LvW9qho5Efrt7ihYs0doX2reSq4hzC6TaXA4O57c9WBnzOPnTr2B9PxqtNH5ixYbowBkyn4JjVz2%2FSkBVmWTGnuU5WVXDichlRTx61YM%2FJ6j94Qw2Ishr1xEKvfLwDpw2UThyJorXQwTC03E%2F%2BYfnZyDW5jflVLgYgpnkJEiOjzd338vsWq73poTlSQ%2FMtmJsLrYHCBjJG7Qu2vYDNH8kHEbxYpp861JRFa0ytUwfYpOjYiqtU%2BiG7cifaOA3FEaZw0fOocR3vlUECKst3VwkRzYurYyoJIe6mlSkwQynrr%2FO2KkzMfUI%2BF0NAI5uv4537YMuHzco8pdQ0l7cX2x1j2usEOOon6Iy63XQ6mV3opyx4A1J%2F5IjChhZ29BjqkAXe69lELAewrX931QCyFsalvfk71i2GYHzJIC%2FQj2N39pPWrioHQz4t0DEkjnfbPwBYiZTzu9h5QLlo1QyATLQKmsCXw9gpppEim%2BztNLcRbxxoCZOhf95%2Bg5Gfp2WcIKNLzOjjfmC4vyVAAj1cvmQLFRe37dOaabpDNZtHnfw6fUUypfoSqHouNxYUT17f0QA0lfPdnyktW6a4JBreNRd7g%2FzOl&X-Amz-Signature=a0562bdfd8d516fefd4e9af652e1f9388e999f2da35aeb5b024385dd32f39075&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V57FRY44%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131616Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIB1z%2B12Pgb7Gbv5mz%2B9QngL9HkbtbliohWuVUYhTFePZAiA%2BdxDZXjNum6AF%2BbbUEAmIRpX8lKRwTI9YdqSe84XEyCqIBAiN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMJDOeo1KC7tDOLL3YKtwDput7r2nXlWVsBvjbVGQoaPmHOJOXxo7i1LHGRqW5UmwPt3AsNGzL5tACGSWNAZzXJT4f6jOLAaAkh8OEU8pwnkcp2wXLl2uFj1hRk67Bh4A7ZX9wk9R%2FByvj1cdcqTsZ5HICIyMmn3v4p0xMuJi%2BXnT5efzhsZF1hafmdC6vGNLgbpYKkXxk6IfCMuSWV7362phhApWlMHB9OGcrN%2BCyP314AiAVyD43ySau1cX8gP7Tp2W6vTdD2DWoRIIYM1YjD4eHbBKfDe%2BGIKPg0WC5eDXsgr4WopSpp1mEMcCIobUkiaoslX7tRriek4fJAa%2FiAJp0RExB3yBUwFxRaX1KHchi9hbsbdzAfEt7XlOHgdSNeri4aX9pbwY69%2FN8hQsPYjOP6y9RzYUXRR73UPWNeQomGm0medBoHvXiR8kOKDK91jTt5veXIXXp9mtTrHeKDpGDADdY1PWl%2BuRf%2FGvc68WgBp%2FtiHLwiWbLnx7jgv0NRW9d%2BWRgMUPdmn9x66tGMQnoc8jZqukOl8KZ%2FjwDZVZ2QwEnmDKY79%2FuNRbqrXp%2Ffgr6sN1zxhiU3N1zumh0C%2BqiXkyR01zn2qNHXYccNnQvm3oB9Mybuu9teB2HSsrRA1pS1LxCZ6qm55EwqYWdvQY6pgHINwytq2Ig1C84BJzLxh7dcdg3jV8Ek9jYzqbmn%2FrjECDVpqEmN%2FzKOZxPS0%2FfLtxgRQXIZHfpGMeWBwrKh40mv7bBPnFjTaVbbbu8AvS5zADrMJ95xSlw3vuzVRK%2Byrucjl4viHt1NbUqaWpjPoTZqTXEcuIaoMy%2Fn157uEawG7xRrc%2Fnt8I33Dpamga2M8BFQUKgETUUODS0%2FQjzAB1vAnW16Z1h&X-Amz-Signature=248f0c37ed656422ec2669d0e194d0f81e06b0b8605688278681c6d610a21b8b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663H4KOELZ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131616Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIEuETUYpShTG0lgtNFS35ZExEjHtMGMKiAIikn%2BGkBR8AiEAnsQimjstmuXsvIHS66UsHQnv9LGzm%2FcgBqHrUjExsroqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDEcRzJC6tQppCbgDircA5oc3bRCx59rCMfjOXNsgqkh7lA%2FzsHdViiz7dPl3EMDxbHAmIWs57vCTGLaMMWNSX73EjEjL0PIiGZHU9OU7nTk7YQtRYiZJAXr%2BErjrFr%2FJByJNtEIu5j2saK6s%2FOGrWeJAE6TLNfbILcaEcZFiczBKE1pDOt3ruHSP5YLwiWJ65goJwGRimAp%2FyHS0VW0N1xAlgLx6phC0z3zlqdv7B8X6sBS%2Fz%2Bs6x2hfD1GfYo75nCPp8oLHj2fileCmZMOFAdU%2B8fCplEcuUKcfID1f2zgVQbCDBdMcQBn4MM30O55oyo%2Bq3bKpLQONeRRfm%2B3nfQih0ahbSK9o5JbFFzXdYq50izT7bMmeaeOwpHI%2FJ2TyFn7kL3mbMsJ3CBoo6anYXk%2B4Biq%2B9c4wVdL%2B0FtnwvWkdHS%2FDgqXXDbdo3OkeO9AVcEndYWUxK6ALG%2BLjbEgUnSPAnewV0fI8MCVPtmXisNjzJwEC1gJcugW2ZoT5vkh%2FNMTSCMuiVRxZdLCAZnRGYKgTRF7TQ1o1H2fpQ4TKdQXULnEOf%2FcjUrCToYAj3FkUh6xKgFQSqYWFPxgf1YbJKxyc7btIBmjYEu758%2BkCmKXy4Ablgt6YW4ek8NoKgSLqTeMcsVns%2BwPdNbMKKFnb0GOqUBPA19kxuQIgBVHqcJcKfan3uSTb1ZrtdvMV%2BhGtegpoN5lbWKhug5c4Sh2iqBkWU4JdstxCT9HhA%2Bu0lYvkx9wCThnHr5SXGOMQ4VX%2Bn3qKvJjFCcQHuRce52KEaG42iKaMeVCuikMnYGTx4GmMfi5%2BkcEyuDA5R94wxDdEdZ6yCJlFdKAFGdkbSIjpI8Bz7b92FWjgNotmmUup8u8C5XjLd5UNNk&X-Amz-Signature=8c86efc4456afb6bcb9dcfd2c2e3299fbe335beea90acf2a9ffadd5a627aa3d4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6L7372W%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131615Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJIMEYCIQCA%2BGYK%2Ffb4DmqLgBLVNxQIceLLZMNxCWICY7yc5onuBgIhAOz%2BbuzRFEnJ%2Bab7TfTqS8OBztDS1wGauaasQSrzRe31KogECI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxXuQTw2LIyj6KEWacq3AOslP4QEPfmduD2owSTnPCUwjqohoGL7ZpdMGAbsrFjk5xOA5NdA1PV9XiSWpwyEWA168JpybinWV%2FN2fVPuyEvkr6AfAJgBekl%2FLgcV5S6eWxKgpAAamaFmhMeTurl6os6o62euuKRB491xdmq7dYqOyLchj7SbWM1OJhjumaQRX6BqPcec3c7gHtZ8VAZE8Xl0zgGdhi6NOHA4ycvZX1jSq%2F0LPuWRfFZPgZWKhMMOl2leg0zIKbpPQbAa%2FB%2FA8v%2B%2BJnF8LvW9qho5Efrt7ihYs0doX2reSq4hzC6TaXA4O57c9WBnzOPnTr2B9PxqtNH5ixYbowBkyn4JjVz2%2FSkBVmWTGnuU5WVXDichlRTx61YM%2FJ6j94Qw2Ishr1xEKvfLwDpw2UThyJorXQwTC03E%2F%2BYfnZyDW5jflVLgYgpnkJEiOjzd338vsWq73poTlSQ%2FMtmJsLrYHCBjJG7Qu2vYDNH8kHEbxYpp861JRFa0ytUwfYpOjYiqtU%2BiG7cifaOA3FEaZw0fOocR3vlUECKst3VwkRzYurYyoJIe6mlSkwQynrr%2FO2KkzMfUI%2BF0NAI5uv4537YMuHzco8pdQ0l7cX2x1j2usEOOon6Iy63XQ6mV3opyx4A1J%2F5IjChhZ29BjqkAXe69lELAewrX931QCyFsalvfk71i2GYHzJIC%2FQj2N39pPWrioHQz4t0DEkjnfbPwBYiZTzu9h5QLlo1QyATLQKmsCXw9gpppEim%2BztNLcRbxxoCZOhf95%2Bg5Gfp2WcIKNLzOjjfmC4vyVAAj1cvmQLFRe37dOaabpDNZtHnfw6fUUypfoSqHouNxYUT17f0QA0lfPdnyktW6a4JBreNRd7g%2FzOl&X-Amz-Signature=cbe3b7ed2f476d31560a7873dbff25793e76f245b63134105eec660f6c1e556e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6L7372W%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131615Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJIMEYCIQCA%2BGYK%2Ffb4DmqLgBLVNxQIceLLZMNxCWICY7yc5onuBgIhAOz%2BbuzRFEnJ%2Bab7TfTqS8OBztDS1wGauaasQSrzRe31KogECI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxXuQTw2LIyj6KEWacq3AOslP4QEPfmduD2owSTnPCUwjqohoGL7ZpdMGAbsrFjk5xOA5NdA1PV9XiSWpwyEWA168JpybinWV%2FN2fVPuyEvkr6AfAJgBekl%2FLgcV5S6eWxKgpAAamaFmhMeTurl6os6o62euuKRB491xdmq7dYqOyLchj7SbWM1OJhjumaQRX6BqPcec3c7gHtZ8VAZE8Xl0zgGdhi6NOHA4ycvZX1jSq%2F0LPuWRfFZPgZWKhMMOl2leg0zIKbpPQbAa%2FB%2FA8v%2B%2BJnF8LvW9qho5Efrt7ihYs0doX2reSq4hzC6TaXA4O57c9WBnzOPnTr2B9PxqtNH5ixYbowBkyn4JjVz2%2FSkBVmWTGnuU5WVXDichlRTx61YM%2FJ6j94Qw2Ishr1xEKvfLwDpw2UThyJorXQwTC03E%2F%2BYfnZyDW5jflVLgYgpnkJEiOjzd338vsWq73poTlSQ%2FMtmJsLrYHCBjJG7Qu2vYDNH8kHEbxYpp861JRFa0ytUwfYpOjYiqtU%2BiG7cifaOA3FEaZw0fOocR3vlUECKst3VwkRzYurYyoJIe6mlSkwQynrr%2FO2KkzMfUI%2BF0NAI5uv4537YMuHzco8pdQ0l7cX2x1j2usEOOon6Iy63XQ6mV3opyx4A1J%2F5IjChhZ29BjqkAXe69lELAewrX931QCyFsalvfk71i2GYHzJIC%2FQj2N39pPWrioHQz4t0DEkjnfbPwBYiZTzu9h5QLlo1QyATLQKmsCXw9gpppEim%2BztNLcRbxxoCZOhf95%2Bg5Gfp2WcIKNLzOjjfmC4vyVAAj1cvmQLFRe37dOaabpDNZtHnfw6fUUypfoSqHouNxYUT17f0QA0lfPdnyktW6a4JBreNRd7g%2FzOl&X-Amz-Signature=bcfe1a649bc53937be5df21353f772537a2fe4b201866fc9ec54ecdf19fe660d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6L7372W%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131615Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJIMEYCIQCA%2BGYK%2Ffb4DmqLgBLVNxQIceLLZMNxCWICY7yc5onuBgIhAOz%2BbuzRFEnJ%2Bab7TfTqS8OBztDS1wGauaasQSrzRe31KogECI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxXuQTw2LIyj6KEWacq3AOslP4QEPfmduD2owSTnPCUwjqohoGL7ZpdMGAbsrFjk5xOA5NdA1PV9XiSWpwyEWA168JpybinWV%2FN2fVPuyEvkr6AfAJgBekl%2FLgcV5S6eWxKgpAAamaFmhMeTurl6os6o62euuKRB491xdmq7dYqOyLchj7SbWM1OJhjumaQRX6BqPcec3c7gHtZ8VAZE8Xl0zgGdhi6NOHA4ycvZX1jSq%2F0LPuWRfFZPgZWKhMMOl2leg0zIKbpPQbAa%2FB%2FA8v%2B%2BJnF8LvW9qho5Efrt7ihYs0doX2reSq4hzC6TaXA4O57c9WBnzOPnTr2B9PxqtNH5ixYbowBkyn4JjVz2%2FSkBVmWTGnuU5WVXDichlRTx61YM%2FJ6j94Qw2Ishr1xEKvfLwDpw2UThyJorXQwTC03E%2F%2BYfnZyDW5jflVLgYgpnkJEiOjzd338vsWq73poTlSQ%2FMtmJsLrYHCBjJG7Qu2vYDNH8kHEbxYpp861JRFa0ytUwfYpOjYiqtU%2BiG7cifaOA3FEaZw0fOocR3vlUECKst3VwkRzYurYyoJIe6mlSkwQynrr%2FO2KkzMfUI%2BF0NAI5uv4537YMuHzco8pdQ0l7cX2x1j2usEOOon6Iy63XQ6mV3opyx4A1J%2F5IjChhZ29BjqkAXe69lELAewrX931QCyFsalvfk71i2GYHzJIC%2FQj2N39pPWrioHQz4t0DEkjnfbPwBYiZTzu9h5QLlo1QyATLQKmsCXw9gpppEim%2BztNLcRbxxoCZOhf95%2Bg5Gfp2WcIKNLzOjjfmC4vyVAAj1cvmQLFRe37dOaabpDNZtHnfw6fUUypfoSqHouNxYUT17f0QA0lfPdnyktW6a4JBreNRd7g%2FzOl&X-Amz-Signature=010f882cc9c124a904256d15991682605c111ade92aff70a48d0069799a0e3cb&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6L7372W%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131615Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJIMEYCIQCA%2BGYK%2Ffb4DmqLgBLVNxQIceLLZMNxCWICY7yc5onuBgIhAOz%2BbuzRFEnJ%2Bab7TfTqS8OBztDS1wGauaasQSrzRe31KogECI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxXuQTw2LIyj6KEWacq3AOslP4QEPfmduD2owSTnPCUwjqohoGL7ZpdMGAbsrFjk5xOA5NdA1PV9XiSWpwyEWA168JpybinWV%2FN2fVPuyEvkr6AfAJgBekl%2FLgcV5S6eWxKgpAAamaFmhMeTurl6os6o62euuKRB491xdmq7dYqOyLchj7SbWM1OJhjumaQRX6BqPcec3c7gHtZ8VAZE8Xl0zgGdhi6NOHA4ycvZX1jSq%2F0LPuWRfFZPgZWKhMMOl2leg0zIKbpPQbAa%2FB%2FA8v%2B%2BJnF8LvW9qho5Efrt7ihYs0doX2reSq4hzC6TaXA4O57c9WBnzOPnTr2B9PxqtNH5ixYbowBkyn4JjVz2%2FSkBVmWTGnuU5WVXDichlRTx61YM%2FJ6j94Qw2Ishr1xEKvfLwDpw2UThyJorXQwTC03E%2F%2BYfnZyDW5jflVLgYgpnkJEiOjzd338vsWq73poTlSQ%2FMtmJsLrYHCBjJG7Qu2vYDNH8kHEbxYpp861JRFa0ytUwfYpOjYiqtU%2BiG7cifaOA3FEaZw0fOocR3vlUECKst3VwkRzYurYyoJIe6mlSkwQynrr%2FO2KkzMfUI%2BF0NAI5uv4537YMuHzco8pdQ0l7cX2x1j2usEOOon6Iy63XQ6mV3opyx4A1J%2F5IjChhZ29BjqkAXe69lELAewrX931QCyFsalvfk71i2GYHzJIC%2FQj2N39pPWrioHQz4t0DEkjnfbPwBYiZTzu9h5QLlo1QyATLQKmsCXw9gpppEim%2BztNLcRbxxoCZOhf95%2Bg5Gfp2WcIKNLzOjjfmC4vyVAAj1cvmQLFRe37dOaabpDNZtHnfw6fUUypfoSqHouNxYUT17f0QA0lfPdnyktW6a4JBreNRd7g%2FzOl&X-Amz-Signature=09a01700d623cd83e88adaf5eb49dc66c7726c1a42ef01a889126f7d782d7980&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
