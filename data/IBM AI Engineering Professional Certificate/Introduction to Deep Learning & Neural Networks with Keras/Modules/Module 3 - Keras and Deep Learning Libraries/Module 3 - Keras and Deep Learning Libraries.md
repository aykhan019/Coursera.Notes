

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5GCH2JO%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJHMEUCIF2z%2F7nn9xxfZw2b2WQvqVYrDWUdWw5bCZ0FzkBzbPkNAiEAtyOo5loy0KA04d%2BEBlLKKAktUma1DofKAw3yYCsveecq%2FwMILxAAGgw2Mzc0MjMxODM4MDUiDHd7S5%2FeK4lu63VSnyrcA40F4GBZrektyNc75ExwEykh1bAScJpJVI0h2Y2frC7aRVdt%2B0cRvgGA6M72TqVo1ipm1Wm2zBWeD5iIbBECoIjo5HCxEG0p6WHzcM%2FnpexiF%2BWRXQKj7nuzr7F%2BsK%2B7mAAFxWED%2F3AnzDy%2B33vTE%2BjGnuKKmZq5Go20jK6E1kHW4iX3b0ax3rSOBebYEg4IQUwC5rpFO6TdTG6blaFZOXaLQwaClHz4lUAIhOxfqOyh4xj0%2BV7hN2YxmE1Fyt7PV2Sxm1QTHIHBQ4mI3bdyN6u%2BxGytQH8vY8inwTRgzNNR673fHzpstrayL0p36FtAYld9WMTTHJk%2F7Mr6057fDVRPD85St9VXmeiD8fQLPfw6rS1sSZ3oL1wnOfU6WKRB4cWtgLAMdS9tt5kZQekmGLnMhj8RvTh8NKqdJztg6ZaOb2thvSsxLjDm94AlQRE5B%2Fo4iMMJ6kZgzn6T8lMEg0n07Tq0lhkyTlemqatahmAZQgEL4r6PofV3vQFJSlGxIvWfbDnUYBx19lTNA9pqnxguQqCrUTKjRX4K5c%2BCJNJLDDFoadgIQ%2BqZXtyqs%2FpV%2BZbTZCQMgB2UM1weqFMO3TAzjDH4XAsCyhb5Zytw6hgviQHD4t%2BiyEclg48VMNa8iL0GOqUBXsXo4kfEFgXOvWoq6irRUhctYQlpTVDxWoWFQy0PXrywxQxf8HhcfogruYSTbyMSjxY4oXGV5hb7F8y5rX0vSrHumB0sWKZcG9qSn0Is7QUJj737twUwBQZ8jOfFnqemNchDuyAkKevUuuyw4IpRo0dfFcZ39wirZpdlwtmcvZGMWa0Hazp6XcY8Q2no4b%2Fnb1lTnVQnlrgzkc%2BR7QkYh4ICzWQD&X-Amz-Signature=70432ebed359987a79f69a7a8f9634ed1a9bdb55a92d65df8d1fb4a9de9c055d&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5GCH2JO%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJHMEUCIF2z%2F7nn9xxfZw2b2WQvqVYrDWUdWw5bCZ0FzkBzbPkNAiEAtyOo5loy0KA04d%2BEBlLKKAktUma1DofKAw3yYCsveecq%2FwMILxAAGgw2Mzc0MjMxODM4MDUiDHd7S5%2FeK4lu63VSnyrcA40F4GBZrektyNc75ExwEykh1bAScJpJVI0h2Y2frC7aRVdt%2B0cRvgGA6M72TqVo1ipm1Wm2zBWeD5iIbBECoIjo5HCxEG0p6WHzcM%2FnpexiF%2BWRXQKj7nuzr7F%2BsK%2B7mAAFxWED%2F3AnzDy%2B33vTE%2BjGnuKKmZq5Go20jK6E1kHW4iX3b0ax3rSOBebYEg4IQUwC5rpFO6TdTG6blaFZOXaLQwaClHz4lUAIhOxfqOyh4xj0%2BV7hN2YxmE1Fyt7PV2Sxm1QTHIHBQ4mI3bdyN6u%2BxGytQH8vY8inwTRgzNNR673fHzpstrayL0p36FtAYld9WMTTHJk%2F7Mr6057fDVRPD85St9VXmeiD8fQLPfw6rS1sSZ3oL1wnOfU6WKRB4cWtgLAMdS9tt5kZQekmGLnMhj8RvTh8NKqdJztg6ZaOb2thvSsxLjDm94AlQRE5B%2Fo4iMMJ6kZgzn6T8lMEg0n07Tq0lhkyTlemqatahmAZQgEL4r6PofV3vQFJSlGxIvWfbDnUYBx19lTNA9pqnxguQqCrUTKjRX4K5c%2BCJNJLDDFoadgIQ%2BqZXtyqs%2FpV%2BZbTZCQMgB2UM1weqFMO3TAzjDH4XAsCyhb5Zytw6hgviQHD4t%2BiyEclg48VMNa8iL0GOqUBXsXo4kfEFgXOvWoq6irRUhctYQlpTVDxWoWFQy0PXrywxQxf8HhcfogruYSTbyMSjxY4oXGV5hb7F8y5rX0vSrHumB0sWKZcG9qSn0Is7QUJj737twUwBQZ8jOfFnqemNchDuyAkKevUuuyw4IpRo0dfFcZ39wirZpdlwtmcvZGMWa0Hazp6XcY8Q2no4b%2Fnb1lTnVQnlrgzkc%2BR7QkYh4ICzWQD&X-Amz-Signature=0a3f8372e4868910c8d77d8d440f9b851d5f8bdfaca8f3d34b5bad12170d4c56&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5GCH2JO%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJHMEUCIF2z%2F7nn9xxfZw2b2WQvqVYrDWUdWw5bCZ0FzkBzbPkNAiEAtyOo5loy0KA04d%2BEBlLKKAktUma1DofKAw3yYCsveecq%2FwMILxAAGgw2Mzc0MjMxODM4MDUiDHd7S5%2FeK4lu63VSnyrcA40F4GBZrektyNc75ExwEykh1bAScJpJVI0h2Y2frC7aRVdt%2B0cRvgGA6M72TqVo1ipm1Wm2zBWeD5iIbBECoIjo5HCxEG0p6WHzcM%2FnpexiF%2BWRXQKj7nuzr7F%2BsK%2B7mAAFxWED%2F3AnzDy%2B33vTE%2BjGnuKKmZq5Go20jK6E1kHW4iX3b0ax3rSOBebYEg4IQUwC5rpFO6TdTG6blaFZOXaLQwaClHz4lUAIhOxfqOyh4xj0%2BV7hN2YxmE1Fyt7PV2Sxm1QTHIHBQ4mI3bdyN6u%2BxGytQH8vY8inwTRgzNNR673fHzpstrayL0p36FtAYld9WMTTHJk%2F7Mr6057fDVRPD85St9VXmeiD8fQLPfw6rS1sSZ3oL1wnOfU6WKRB4cWtgLAMdS9tt5kZQekmGLnMhj8RvTh8NKqdJztg6ZaOb2thvSsxLjDm94AlQRE5B%2Fo4iMMJ6kZgzn6T8lMEg0n07Tq0lhkyTlemqatahmAZQgEL4r6PofV3vQFJSlGxIvWfbDnUYBx19lTNA9pqnxguQqCrUTKjRX4K5c%2BCJNJLDDFoadgIQ%2BqZXtyqs%2FpV%2BZbTZCQMgB2UM1weqFMO3TAzjDH4XAsCyhb5Zytw6hgviQHD4t%2BiyEclg48VMNa8iL0GOqUBXsXo4kfEFgXOvWoq6irRUhctYQlpTVDxWoWFQy0PXrywxQxf8HhcfogruYSTbyMSjxY4oXGV5hb7F8y5rX0vSrHumB0sWKZcG9qSn0Is7QUJj737twUwBQZ8jOfFnqemNchDuyAkKevUuuyw4IpRo0dfFcZ39wirZpdlwtmcvZGMWa0Hazp6XcY8Q2no4b%2Fnb1lTnVQnlrgzkc%2BR7QkYh4ICzWQD&X-Amz-Signature=777c59a05489eb3d363f2f12dca35e8fc8afa4bbb1b852a1fe375945b6c8dd89&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZPP2MN6S%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJGMEQCIGBbJCA0u43oL75a8L7u3Oa0qgdo9RvNP95Xk0DMc9UVAiBphV0gmC80TtV9Zk1a3K8Me2H3RV%2BXnUTsRe7gt3gBKSr%2FAwgvEAAaDDYzNzQyMzE4MzgwNSIM1ER35TaDw1db0aBGKtwDlnm%2BvRITqzuunKQY4qkmFBJcB29YCbewcnwXt2A1Vqeng2MRZWWRhLE1GN4S4CWqwLflmNq4eytFi75GxJZ%2B94F67bPdPqDi3CaK8%2FEOltMX7oHLc8da8BUUmky3Q0PmjfuP8uhQaMRj1Ggxp69SvcknSRpkq5UAlgvMYvQ2GJnRCHoqODxwKdXCD5B7Lss9XlczNu%2B1Tw2WimpQl5roiCAzDoY%2Bw3VLudo6Ef%2Fd1iDCuIu8I97y16OSy3QCSL2X5pkT9Z7pZQVbqFhnQ6nlq82HAhRMgBMfhG%2FbSm2cxxnxCphuOl%2BXcsC0j2HnECqN5JGIpuIn4U5pIKfG05fnyXzBb1oI84BrcwzpFuh95N6WYoz3irldun3rbr0zoG%2BFCOUjzXKRhOrEa%2Fw3WknmOfiX18AB%2FspEdZvqRsDMa0exn7DTYvD%2BbyrxyLmlFTjJsznzEfELm14CB3SZqT%2Bs0djxQHHZrYO7r2ZUf5MKtTgq4Pm9lD1xT8oa5U7Dv9IhMvUr5K8gg1xcslw8CNX3ckgg1ElYQLvC6Euji2ShvUIuFlPsm6%2Bj3ZFwh6AWVWgP3%2FI6xtBo9QOpN5iYF35q7lU%2FqIYN4KDDosgG73j6JJH0WCTVXyiGrlHHgKow3ryIvQY6pgG4VgWXeu1rXKw40GRh5bPoXd9IfxQlUNDSNLT%2Bvc8PF6xQ021u%2F9AA12ghQxyNndF37FNCa8alA3EsyEJlI3qqNfjTEr05yf2ob%2FaT845IR9BriXOkHWl7552vUh8ZbNx1Mr53OowcuhUfdMentU6e%2BeugP%2BxAi1Dy4S77tcQ7nd1GPEl7yeRc8sDMn1Smhb%2F%2Buz86rNJgShEFsOkiZlay0lOucBqr&X-Amz-Signature=ba7424a4d8a5344c3d2e0bdd2f7124a89eb961b60fe86b95a25d0a0094c81d00&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNYCOQIH%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJIMEYCIQCF7Rhv%2BJiTSj9afdc65jaFxl1gjtnfWhJQx%2BYEzQOU1wIhAKGIExICJRMvepnnD6GXXxl6d92%2B9%2FrDa%2F5xvhCFog11Kv8DCC8QABoMNjM3NDIzMTgzODA1IgwVzpGbAXsE0H7Mng4q3APtTrZg%2B0VkhRsJdzPcOx6Hh5kcmBcH27lrGvdz6PtdL8fH8XHeeV6ndO1F%2F9cKJy%2BwxDwF8s6SlUjTPgmel23KVd7TOy71gQJgnv1V2zyEgY9w%2BmDDbK%2FQ3MQrQvNIE8az5NJIFPPswYDoJoVZNqZTFQx%2F3IDl2Rp2TLc%2BfThUGfUrXP8TytZeaUzY9tOotkcL%2FM5PS6NKE8MjNCqlKpBIbp7yCHk%2BSdJ6fXs69Fev7jip5B2M%2Bb6dT7mTy%2BasAflYEh0NDg3HgCjiU2zuFd3BVjjZlgfzu5D74jAy%2BPccS6oo5%2Bsla8Fm80Wc0ZIglI40r2IcxBucm0RsY5SE5NRtcQ%2FPhvOJO4IOKPSoTJOcxCbXhUaMRX4jAdkiQvuvqKfozfQrS3e2Rp9DSzSAqq5%2BLDCnce8p3p8CW8h0WalsLOHnxBmfyBX%2BLTynxSacsJVPuGp6n8%2BjIHpPIyqxq64TaB5r2cGzbvEhNtUhZ8y9ce8ENSYwVj4K7cW7sVwifJQd2L838%2B6IiP8pWx03pcU10w1Hgodqg%2BOLnfQKRC1HJvkV38olM3yZWxChqs%2FEW5WP4lKLD7wBPk2VlOOKZv46CHtBXWjW64vdMi3qGztzSK5VP8pxYAdOVg1KuDDAvYi9BjqkATvEvaupqNbAkvEZZAOLLzrtWyPmBEGr9OD%2FaFbCSz%2FcOnQlqpqjhpN%2Fm3wgxO2DUjFuYmIGIM%2BdSyZh9HO0HB%2BXcoYymZ5HohmSGO5D5oEkL0TcMq1EfHm0zO7ITQAwnMqZT9PlgqnPfX4qoz27wkZNlrFlzPkIjOiFrsnjHSEOKaVtaBmcmSD7CeS2ca6baDBsfwcpUtpcady1x3N6XBbfnBlt&X-Amz-Signature=a1b01d3d9c460246e498f1b8ff85dbc8baeb3334b75b7ce4ee0e107b3f5ec361&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5GCH2JO%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJHMEUCIF2z%2F7nn9xxfZw2b2WQvqVYrDWUdWw5bCZ0FzkBzbPkNAiEAtyOo5loy0KA04d%2BEBlLKKAktUma1DofKAw3yYCsveecq%2FwMILxAAGgw2Mzc0MjMxODM4MDUiDHd7S5%2FeK4lu63VSnyrcA40F4GBZrektyNc75ExwEykh1bAScJpJVI0h2Y2frC7aRVdt%2B0cRvgGA6M72TqVo1ipm1Wm2zBWeD5iIbBECoIjo5HCxEG0p6WHzcM%2FnpexiF%2BWRXQKj7nuzr7F%2BsK%2B7mAAFxWED%2F3AnzDy%2B33vTE%2BjGnuKKmZq5Go20jK6E1kHW4iX3b0ax3rSOBebYEg4IQUwC5rpFO6TdTG6blaFZOXaLQwaClHz4lUAIhOxfqOyh4xj0%2BV7hN2YxmE1Fyt7PV2Sxm1QTHIHBQ4mI3bdyN6u%2BxGytQH8vY8inwTRgzNNR673fHzpstrayL0p36FtAYld9WMTTHJk%2F7Mr6057fDVRPD85St9VXmeiD8fQLPfw6rS1sSZ3oL1wnOfU6WKRB4cWtgLAMdS9tt5kZQekmGLnMhj8RvTh8NKqdJztg6ZaOb2thvSsxLjDm94AlQRE5B%2Fo4iMMJ6kZgzn6T8lMEg0n07Tq0lhkyTlemqatahmAZQgEL4r6PofV3vQFJSlGxIvWfbDnUYBx19lTNA9pqnxguQqCrUTKjRX4K5c%2BCJNJLDDFoadgIQ%2BqZXtyqs%2FpV%2BZbTZCQMgB2UM1weqFMO3TAzjDH4XAsCyhb5Zytw6hgviQHD4t%2BiyEclg48VMNa8iL0GOqUBXsXo4kfEFgXOvWoq6irRUhctYQlpTVDxWoWFQy0PXrywxQxf8HhcfogruYSTbyMSjxY4oXGV5hb7F8y5rX0vSrHumB0sWKZcG9qSn0Is7QUJj737twUwBQZ8jOfFnqemNchDuyAkKevUuuyw4IpRo0dfFcZ39wirZpdlwtmcvZGMWa0Hazp6XcY8Q2no4b%2Fnb1lTnVQnlrgzkc%2BR7QkYh4ICzWQD&X-Amz-Signature=fc2b53f83f68ea32b10a7a8a9d3e5fcc64960f8a202c018dddb3c2f4b31564b8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5GCH2JO%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJHMEUCIF2z%2F7nn9xxfZw2b2WQvqVYrDWUdWw5bCZ0FzkBzbPkNAiEAtyOo5loy0KA04d%2BEBlLKKAktUma1DofKAw3yYCsveecq%2FwMILxAAGgw2Mzc0MjMxODM4MDUiDHd7S5%2FeK4lu63VSnyrcA40F4GBZrektyNc75ExwEykh1bAScJpJVI0h2Y2frC7aRVdt%2B0cRvgGA6M72TqVo1ipm1Wm2zBWeD5iIbBECoIjo5HCxEG0p6WHzcM%2FnpexiF%2BWRXQKj7nuzr7F%2BsK%2B7mAAFxWED%2F3AnzDy%2B33vTE%2BjGnuKKmZq5Go20jK6E1kHW4iX3b0ax3rSOBebYEg4IQUwC5rpFO6TdTG6blaFZOXaLQwaClHz4lUAIhOxfqOyh4xj0%2BV7hN2YxmE1Fyt7PV2Sxm1QTHIHBQ4mI3bdyN6u%2BxGytQH8vY8inwTRgzNNR673fHzpstrayL0p36FtAYld9WMTTHJk%2F7Mr6057fDVRPD85St9VXmeiD8fQLPfw6rS1sSZ3oL1wnOfU6WKRB4cWtgLAMdS9tt5kZQekmGLnMhj8RvTh8NKqdJztg6ZaOb2thvSsxLjDm94AlQRE5B%2Fo4iMMJ6kZgzn6T8lMEg0n07Tq0lhkyTlemqatahmAZQgEL4r6PofV3vQFJSlGxIvWfbDnUYBx19lTNA9pqnxguQqCrUTKjRX4K5c%2BCJNJLDDFoadgIQ%2BqZXtyqs%2FpV%2BZbTZCQMgB2UM1weqFMO3TAzjDH4XAsCyhb5Zytw6hgviQHD4t%2BiyEclg48VMNa8iL0GOqUBXsXo4kfEFgXOvWoq6irRUhctYQlpTVDxWoWFQy0PXrywxQxf8HhcfogruYSTbyMSjxY4oXGV5hb7F8y5rX0vSrHumB0sWKZcG9qSn0Is7QUJj737twUwBQZ8jOfFnqemNchDuyAkKevUuuyw4IpRo0dfFcZ39wirZpdlwtmcvZGMWa0Hazp6XcY8Q2no4b%2Fnb1lTnVQnlrgzkc%2BR7QkYh4ICzWQD&X-Amz-Signature=57a3338a131bdcd3f3da48c8c65cff8aaa8abd12fd8dcf24574643d5c053d2c7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5GCH2JO%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJHMEUCIF2z%2F7nn9xxfZw2b2WQvqVYrDWUdWw5bCZ0FzkBzbPkNAiEAtyOo5loy0KA04d%2BEBlLKKAktUma1DofKAw3yYCsveecq%2FwMILxAAGgw2Mzc0MjMxODM4MDUiDHd7S5%2FeK4lu63VSnyrcA40F4GBZrektyNc75ExwEykh1bAScJpJVI0h2Y2frC7aRVdt%2B0cRvgGA6M72TqVo1ipm1Wm2zBWeD5iIbBECoIjo5HCxEG0p6WHzcM%2FnpexiF%2BWRXQKj7nuzr7F%2BsK%2B7mAAFxWED%2F3AnzDy%2B33vTE%2BjGnuKKmZq5Go20jK6E1kHW4iX3b0ax3rSOBebYEg4IQUwC5rpFO6TdTG6blaFZOXaLQwaClHz4lUAIhOxfqOyh4xj0%2BV7hN2YxmE1Fyt7PV2Sxm1QTHIHBQ4mI3bdyN6u%2BxGytQH8vY8inwTRgzNNR673fHzpstrayL0p36FtAYld9WMTTHJk%2F7Mr6057fDVRPD85St9VXmeiD8fQLPfw6rS1sSZ3oL1wnOfU6WKRB4cWtgLAMdS9tt5kZQekmGLnMhj8RvTh8NKqdJztg6ZaOb2thvSsxLjDm94AlQRE5B%2Fo4iMMJ6kZgzn6T8lMEg0n07Tq0lhkyTlemqatahmAZQgEL4r6PofV3vQFJSlGxIvWfbDnUYBx19lTNA9pqnxguQqCrUTKjRX4K5c%2BCJNJLDDFoadgIQ%2BqZXtyqs%2FpV%2BZbTZCQMgB2UM1weqFMO3TAzjDH4XAsCyhb5Zytw6hgviQHD4t%2BiyEclg48VMNa8iL0GOqUBXsXo4kfEFgXOvWoq6irRUhctYQlpTVDxWoWFQy0PXrywxQxf8HhcfogruYSTbyMSjxY4oXGV5hb7F8y5rX0vSrHumB0sWKZcG9qSn0Is7QUJj737twUwBQZ8jOfFnqemNchDuyAkKevUuuyw4IpRo0dfFcZ39wirZpdlwtmcvZGMWa0Hazp6XcY8Q2no4b%2Fnb1lTnVQnlrgzkc%2BR7QkYh4ICzWQD&X-Amz-Signature=8c26210166548d96aebc2223bcb7fc5bdd157cc4f208e819c167bd81a35fe3a3&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5GCH2JO%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJHMEUCIF2z%2F7nn9xxfZw2b2WQvqVYrDWUdWw5bCZ0FzkBzbPkNAiEAtyOo5loy0KA04d%2BEBlLKKAktUma1DofKAw3yYCsveecq%2FwMILxAAGgw2Mzc0MjMxODM4MDUiDHd7S5%2FeK4lu63VSnyrcA40F4GBZrektyNc75ExwEykh1bAScJpJVI0h2Y2frC7aRVdt%2B0cRvgGA6M72TqVo1ipm1Wm2zBWeD5iIbBECoIjo5HCxEG0p6WHzcM%2FnpexiF%2BWRXQKj7nuzr7F%2BsK%2B7mAAFxWED%2F3AnzDy%2B33vTE%2BjGnuKKmZq5Go20jK6E1kHW4iX3b0ax3rSOBebYEg4IQUwC5rpFO6TdTG6blaFZOXaLQwaClHz4lUAIhOxfqOyh4xj0%2BV7hN2YxmE1Fyt7PV2Sxm1QTHIHBQ4mI3bdyN6u%2BxGytQH8vY8inwTRgzNNR673fHzpstrayL0p36FtAYld9WMTTHJk%2F7Mr6057fDVRPD85St9VXmeiD8fQLPfw6rS1sSZ3oL1wnOfU6WKRB4cWtgLAMdS9tt5kZQekmGLnMhj8RvTh8NKqdJztg6ZaOb2thvSsxLjDm94AlQRE5B%2Fo4iMMJ6kZgzn6T8lMEg0n07Tq0lhkyTlemqatahmAZQgEL4r6PofV3vQFJSlGxIvWfbDnUYBx19lTNA9pqnxguQqCrUTKjRX4K5c%2BCJNJLDDFoadgIQ%2BqZXtyqs%2FpV%2BZbTZCQMgB2UM1weqFMO3TAzjDH4XAsCyhb5Zytw6hgviQHD4t%2BiyEclg48VMNa8iL0GOqUBXsXo4kfEFgXOvWoq6irRUhctYQlpTVDxWoWFQy0PXrywxQxf8HhcfogruYSTbyMSjxY4oXGV5hb7F8y5rX0vSrHumB0sWKZcG9qSn0Is7QUJj737twUwBQZ8jOfFnqemNchDuyAkKevUuuyw4IpRo0dfFcZ39wirZpdlwtmcvZGMWa0Hazp6XcY8Q2no4b%2Fnb1lTnVQnlrgzkc%2BR7QkYh4ICzWQD&X-Amz-Signature=1b9d1bc536816baf20f4f7709c2a119d00398aca112a8fe7d9a845b86acef976&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
