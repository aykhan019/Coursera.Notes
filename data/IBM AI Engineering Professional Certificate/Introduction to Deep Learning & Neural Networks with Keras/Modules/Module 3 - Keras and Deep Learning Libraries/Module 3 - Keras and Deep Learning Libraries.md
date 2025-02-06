

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667TZAQHYI%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJGMEQCIERxUxvXGgxEUKP5Di4Qs85PCnCY4uBwC%2FyphBGx4J9KAiAd7USQ7VKrtjXHDu5Auy%2B6J7JVBgzaYSBkW4u3VPbO%2Fir%2FAwhdEAAaDDYzNzQyMzE4MzgwNSIMQ3R9zg9VrzKZeeXrKtwD%2FLgbCZD%2FQqb82PMcMU2hp6QWTr2m7v7nsU5aU68cqij9ib48nsWRUk6%2FjC3uZQ%2FWGElmdLylIcYjIrOTxC2C48KW04D61Xgtn4p91sUsfbBgBQCAtlYk8p5oGiu7f2bA43y7XaZOQlTTz75hXtIVnYM3Gd%2B44YI31OK%2BUQNveyKeQ8RWIz1ptW5EWBRB%2FjklPAAslHe0VEo5V0foj%2Bg3k6n5EyQKOasWPK6HGQUe07dW1J6VITEEZuw5FoI2rVS0DP1cxxPNI9ueCZZtujmV5tA65sEk5f0wl3OiYDpEiJlzsdqeU1qowo%2FAFy%2FJylU8jVqztoF4UtMrI7%2B9chfC0jxvT63dpu5mQ%2B%2BOA5BH7blqbHKbA7534ioklSiHEGetMVuSwWchjaD8jxE8yvRrE6JA8t%2F4AZZ0WW9CTP6kYpuMmEEtF2vIomB5%2BYS0TLl5IIVObFhaRXFUTM9QdptD9z7l8la93JGSHwqtQ49GxjNjjcSBpHeRyKZYQHDapAbzsAeUSo3QlqKyph6%2B9MOS%2BSjED6JVKRMeBj8ZFnSiVjyfFU1cQ8%2BpKslBMKrEKeBtMrNp9hr0xD7C%2BoA4V2HSMD1LhRevrmnLeRgACfZDcpiNM1%2BAwc%2B6k1B5jYkw5cOSvQY6pgHGpfPrJ%2FDXeLp%2F2Z26t8iO3CERCXBdY5neGWCx0HwyaMEA5H6gyO8DPCpsyHaU41AETYJzBN%2FPqT33WWGWXYjT7yiFInv%2BqLcAtmq33sf6ank8XEM8%2FBdsYqj2L7WF7M76h9uMzFSlstlhMhu295ERugCeG93aT%2B%2BoPaWnc6TQtXWkZXwGPlya%2B%2Bsz0A2e0Kz9SP6bsTYXa4QtrHsaPxQ%2F7nbB59Wu&X-Amz-Signature=9613cc6768be401b5f37f96b0ccf76a78c7eb77918da6bd016fb19bc42561ec4&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667TZAQHYI%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJGMEQCIERxUxvXGgxEUKP5Di4Qs85PCnCY4uBwC%2FyphBGx4J9KAiAd7USQ7VKrtjXHDu5Auy%2B6J7JVBgzaYSBkW4u3VPbO%2Fir%2FAwhdEAAaDDYzNzQyMzE4MzgwNSIMQ3R9zg9VrzKZeeXrKtwD%2FLgbCZD%2FQqb82PMcMU2hp6QWTr2m7v7nsU5aU68cqij9ib48nsWRUk6%2FjC3uZQ%2FWGElmdLylIcYjIrOTxC2C48KW04D61Xgtn4p91sUsfbBgBQCAtlYk8p5oGiu7f2bA43y7XaZOQlTTz75hXtIVnYM3Gd%2B44YI31OK%2BUQNveyKeQ8RWIz1ptW5EWBRB%2FjklPAAslHe0VEo5V0foj%2Bg3k6n5EyQKOasWPK6HGQUe07dW1J6VITEEZuw5FoI2rVS0DP1cxxPNI9ueCZZtujmV5tA65sEk5f0wl3OiYDpEiJlzsdqeU1qowo%2FAFy%2FJylU8jVqztoF4UtMrI7%2B9chfC0jxvT63dpu5mQ%2B%2BOA5BH7blqbHKbA7534ioklSiHEGetMVuSwWchjaD8jxE8yvRrE6JA8t%2F4AZZ0WW9CTP6kYpuMmEEtF2vIomB5%2BYS0TLl5IIVObFhaRXFUTM9QdptD9z7l8la93JGSHwqtQ49GxjNjjcSBpHeRyKZYQHDapAbzsAeUSo3QlqKyph6%2B9MOS%2BSjED6JVKRMeBj8ZFnSiVjyfFU1cQ8%2BpKslBMKrEKeBtMrNp9hr0xD7C%2BoA4V2HSMD1LhRevrmnLeRgACfZDcpiNM1%2BAwc%2B6k1B5jYkw5cOSvQY6pgHGpfPrJ%2FDXeLp%2F2Z26t8iO3CERCXBdY5neGWCx0HwyaMEA5H6gyO8DPCpsyHaU41AETYJzBN%2FPqT33WWGWXYjT7yiFInv%2BqLcAtmq33sf6ank8XEM8%2FBdsYqj2L7WF7M76h9uMzFSlstlhMhu295ERugCeG93aT%2B%2BoPaWnc6TQtXWkZXwGPlya%2B%2Bsz0A2e0Kz9SP6bsTYXa4QtrHsaPxQ%2F7nbB59Wu&X-Amz-Signature=852faebe7b706ce7e1b0354910080fb4f8f1f0fffcd1a23ebb53cb5d69155026&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667TZAQHYI%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJGMEQCIERxUxvXGgxEUKP5Di4Qs85PCnCY4uBwC%2FyphBGx4J9KAiAd7USQ7VKrtjXHDu5Auy%2B6J7JVBgzaYSBkW4u3VPbO%2Fir%2FAwhdEAAaDDYzNzQyMzE4MzgwNSIMQ3R9zg9VrzKZeeXrKtwD%2FLgbCZD%2FQqb82PMcMU2hp6QWTr2m7v7nsU5aU68cqij9ib48nsWRUk6%2FjC3uZQ%2FWGElmdLylIcYjIrOTxC2C48KW04D61Xgtn4p91sUsfbBgBQCAtlYk8p5oGiu7f2bA43y7XaZOQlTTz75hXtIVnYM3Gd%2B44YI31OK%2BUQNveyKeQ8RWIz1ptW5EWBRB%2FjklPAAslHe0VEo5V0foj%2Bg3k6n5EyQKOasWPK6HGQUe07dW1J6VITEEZuw5FoI2rVS0DP1cxxPNI9ueCZZtujmV5tA65sEk5f0wl3OiYDpEiJlzsdqeU1qowo%2FAFy%2FJylU8jVqztoF4UtMrI7%2B9chfC0jxvT63dpu5mQ%2B%2BOA5BH7blqbHKbA7534ioklSiHEGetMVuSwWchjaD8jxE8yvRrE6JA8t%2F4AZZ0WW9CTP6kYpuMmEEtF2vIomB5%2BYS0TLl5IIVObFhaRXFUTM9QdptD9z7l8la93JGSHwqtQ49GxjNjjcSBpHeRyKZYQHDapAbzsAeUSo3QlqKyph6%2B9MOS%2BSjED6JVKRMeBj8ZFnSiVjyfFU1cQ8%2BpKslBMKrEKeBtMrNp9hr0xD7C%2BoA4V2HSMD1LhRevrmnLeRgACfZDcpiNM1%2BAwc%2B6k1B5jYkw5cOSvQY6pgHGpfPrJ%2FDXeLp%2F2Z26t8iO3CERCXBdY5neGWCx0HwyaMEA5H6gyO8DPCpsyHaU41AETYJzBN%2FPqT33WWGWXYjT7yiFInv%2BqLcAtmq33sf6ank8XEM8%2FBdsYqj2L7WF7M76h9uMzFSlstlhMhu295ERugCeG93aT%2B%2BoPaWnc6TQtXWkZXwGPlya%2B%2Bsz0A2e0Kz9SP6bsTYXa4QtrHsaPxQ%2F7nbB59Wu&X-Amz-Signature=534e3631f4c4bf6d8e3049b0429faca5bfad444bb2930f020f0bc8bc5cc97ddb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USSYHTLE%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJIMEYCIQDwYNhnExxV0yqtsyJgJ1rkBzXNhOuBrc%2B%2Fkfplxo3vDAIhANVuP%2B35T2uHUtTDARYouglQm5YBAM0MKMlMTB5aYhvBKv8DCF0QABoMNjM3NDIzMTgzODA1Igw3ANy6TNDsSnjs238q3AMA6yGykXPMo0ba4bSDBVJqCfyy1QMfEi7Pgo9pPuzxFWiwJW7iSojIxVwTQvI1bZEr4GTsuZgthD4sjXfqCmFDGVf9NwfXt7rpaIKE8cyshb%2F5dNSgHLDU6na%2B0FeiC7cyYjjQ37D4Xtgpbo6RGe0cmDI2%2BqYnQC%2FCc0%2BH2Z6vagcT3dzrbgLkA%2B%2B827ToPEUuQKgpXCL0V2eHyEL%2FkNVYShJeS1UanclBCAq9F6pu%2Fy4QaoKqyw1J%2Fs6vaa9L8NoK034LzY4HGuYXue%2BNePa%2FoAyOYmDzMNDBk8wNujHhcq8phle1RUbmimvUaUU2GYnK2dVnyj413SwKumqcAyMBky7T5kAMZqKTyHYGSh%2FrNYlxXfsux%2BIIggD0Jxvc42X1NavIsSjJhXwAKMVQGRINe6HNcB%2F%2FQVq2n68UTOVqZQWhOBvmQnsHEeFH4Nazsk4C8%2F1Rlg8GXeB0x75AWBKLiJMwgBn4j1AX550JRTIbqxaQOUTsS4BJWWrZ%2F8EsjiuJDsGaUCWf9iNg3zknb0vyCg7Y9%2FJwaWMujGV8jIHLr%2BeThwSh0OGtfXruQqZeUDvOjNO%2BaZj1kruDL2ebjFAf8%2FQxllw%2F7AwsB6wCrAD164ZDwAkGGnCD03sEsjCrxJK9BjqkAXoNPKUUHIcz6ZpQfR3OBBbiEZWEJYir%2BFUAGk3WvzyAz%2FBEQxkE3Dc7BCRLwgW0uMnpz8QB1RtKX7ONWPX%2B4g%2BsYM4CMbafOdbI9j%2B%2FJ9gdxIZYbYFERCPD2BRv7EAYJrxAXPWFni%2FoIH94g9P1HWK4YB248ziDXd%2FfRvIQmGQQZAznTcPk%2B5ub%2ByMF8IL1LHfL3%2Fsf%2FsRZhlll1cx0VzJt3R60&X-Amz-Signature=3259908a110f5e658f9f7eed82dc34d010a1f574801102aca288505f91fdbb5b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z3T3P2EV%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQDuamvDhwQVgT8P679pOro1LHHU7Q1KjGgEHs5Tz4QZzgIgRICplDTvJMtkxZifVVIxdrhZEZrsPN21pqiGwLJWNCEq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDCMqp%2FGxYdAwGxOxYyrcA%2BYiww2dUIkCrLQmnS0JCUKTQPbfsMTL%2F3CAdZAIW%2BC5kV%2FTcC%2BQQNKmQ9gead%2FlhX76yY4emnjJ4A9OBwOJjYMYwekb%2FcgF6BTDKCNKF2r0wmMfr2NuzanRt802iegygPmKoCgyoBEsfHrQLy%2BD126i%2BFr5LYEhlCVYpBu%2FoduX7er5YdbYkDn3G9nCIcYScStyeAxrIhAdj9%2BXEuo97N5vQ9PmaUTzHvLZGWgPfuYIlbIuZAJtyt9k7vV5bLwP4Wl0WKY2AxxS5omQ3br7UKnxWkSviKnzQcPF2PlURkAexN6f6Q5dm5pY65VDCf5j2utWc4CjXqZfemCV6xMk%2BjEMVSpdosHCEKIfqoRzyrkI5x3BAvEu9%2FsHJYHShGiVQNrLZfQ6wgRIpFFBVa7b5u6Nk%2BCNSyAItzhISFDFzXVZoCV6mHxjP4ODbO%2B2wa2IxpX1J0hiF8KDlEfZx8eIk2v3mJ6GvWOU%2F6HGsgWLArJQt9Nrvhiy1TReg0R%2BLHLSDFzTnj1%2By0reFgIHnfUjZacIBNn7%2B3AyPlp0DSYqQFr%2BYs99lDUmz091RKvWdq0o2y4dPgqq3Lba%2BCkuvNHatZ%2FF3X0WeKWMG%2FVC8p3vD6JAJLrcJoi4HaosveISMILEkr0GOqUBI0aCQeyv4c4agAvqC0R9himAtL9YIcNbz%2FzrH252GI3z6ktg0dm3WZuyXaSGptohp8cBDDpU1qoNSgKCjf88PhhYremgvd8YHchevd8hJlSKf751FGz%2Bh7CktGgg5VpmBN%2Fj5krPs3w0Q85igSlioKa0USijp%2FM6ItABaSkZ6jdlNDRw6FU7ByN2cEjh6FGw%2B4MgYk84gRKOpXZtczHXS03m6%2FjE&X-Amz-Signature=77f1f942c7513bf96b5830e2b3afa1df004ef952bd6c30249ecf43fa88365f94&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667TZAQHYI%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJGMEQCIERxUxvXGgxEUKP5Di4Qs85PCnCY4uBwC%2FyphBGx4J9KAiAd7USQ7VKrtjXHDu5Auy%2B6J7JVBgzaYSBkW4u3VPbO%2Fir%2FAwhdEAAaDDYzNzQyMzE4MzgwNSIMQ3R9zg9VrzKZeeXrKtwD%2FLgbCZD%2FQqb82PMcMU2hp6QWTr2m7v7nsU5aU68cqij9ib48nsWRUk6%2FjC3uZQ%2FWGElmdLylIcYjIrOTxC2C48KW04D61Xgtn4p91sUsfbBgBQCAtlYk8p5oGiu7f2bA43y7XaZOQlTTz75hXtIVnYM3Gd%2B44YI31OK%2BUQNveyKeQ8RWIz1ptW5EWBRB%2FjklPAAslHe0VEo5V0foj%2Bg3k6n5EyQKOasWPK6HGQUe07dW1J6VITEEZuw5FoI2rVS0DP1cxxPNI9ueCZZtujmV5tA65sEk5f0wl3OiYDpEiJlzsdqeU1qowo%2FAFy%2FJylU8jVqztoF4UtMrI7%2B9chfC0jxvT63dpu5mQ%2B%2BOA5BH7blqbHKbA7534ioklSiHEGetMVuSwWchjaD8jxE8yvRrE6JA8t%2F4AZZ0WW9CTP6kYpuMmEEtF2vIomB5%2BYS0TLl5IIVObFhaRXFUTM9QdptD9z7l8la93JGSHwqtQ49GxjNjjcSBpHeRyKZYQHDapAbzsAeUSo3QlqKyph6%2B9MOS%2BSjED6JVKRMeBj8ZFnSiVjyfFU1cQ8%2BpKslBMKrEKeBtMrNp9hr0xD7C%2BoA4V2HSMD1LhRevrmnLeRgACfZDcpiNM1%2BAwc%2B6k1B5jYkw5cOSvQY6pgHGpfPrJ%2FDXeLp%2F2Z26t8iO3CERCXBdY5neGWCx0HwyaMEA5H6gyO8DPCpsyHaU41AETYJzBN%2FPqT33WWGWXYjT7yiFInv%2BqLcAtmq33sf6ank8XEM8%2FBdsYqj2L7WF7M76h9uMzFSlstlhMhu295ERugCeG93aT%2B%2BoPaWnc6TQtXWkZXwGPlya%2B%2Bsz0A2e0Kz9SP6bsTYXa4QtrHsaPxQ%2F7nbB59Wu&X-Amz-Signature=8538d447a3a0998ece843ed20f077cc3574b79759b2ae7f4e6bc9035c87ec4b7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667TZAQHYI%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJGMEQCIERxUxvXGgxEUKP5Di4Qs85PCnCY4uBwC%2FyphBGx4J9KAiAd7USQ7VKrtjXHDu5Auy%2B6J7JVBgzaYSBkW4u3VPbO%2Fir%2FAwhdEAAaDDYzNzQyMzE4MzgwNSIMQ3R9zg9VrzKZeeXrKtwD%2FLgbCZD%2FQqb82PMcMU2hp6QWTr2m7v7nsU5aU68cqij9ib48nsWRUk6%2FjC3uZQ%2FWGElmdLylIcYjIrOTxC2C48KW04D61Xgtn4p91sUsfbBgBQCAtlYk8p5oGiu7f2bA43y7XaZOQlTTz75hXtIVnYM3Gd%2B44YI31OK%2BUQNveyKeQ8RWIz1ptW5EWBRB%2FjklPAAslHe0VEo5V0foj%2Bg3k6n5EyQKOasWPK6HGQUe07dW1J6VITEEZuw5FoI2rVS0DP1cxxPNI9ueCZZtujmV5tA65sEk5f0wl3OiYDpEiJlzsdqeU1qowo%2FAFy%2FJylU8jVqztoF4UtMrI7%2B9chfC0jxvT63dpu5mQ%2B%2BOA5BH7blqbHKbA7534ioklSiHEGetMVuSwWchjaD8jxE8yvRrE6JA8t%2F4AZZ0WW9CTP6kYpuMmEEtF2vIomB5%2BYS0TLl5IIVObFhaRXFUTM9QdptD9z7l8la93JGSHwqtQ49GxjNjjcSBpHeRyKZYQHDapAbzsAeUSo3QlqKyph6%2B9MOS%2BSjED6JVKRMeBj8ZFnSiVjyfFU1cQ8%2BpKslBMKrEKeBtMrNp9hr0xD7C%2BoA4V2HSMD1LhRevrmnLeRgACfZDcpiNM1%2BAwc%2B6k1B5jYkw5cOSvQY6pgHGpfPrJ%2FDXeLp%2F2Z26t8iO3CERCXBdY5neGWCx0HwyaMEA5H6gyO8DPCpsyHaU41AETYJzBN%2FPqT33WWGWXYjT7yiFInv%2BqLcAtmq33sf6ank8XEM8%2FBdsYqj2L7WF7M76h9uMzFSlstlhMhu295ERugCeG93aT%2B%2BoPaWnc6TQtXWkZXwGPlya%2B%2Bsz0A2e0Kz9SP6bsTYXa4QtrHsaPxQ%2F7nbB59Wu&X-Amz-Signature=cc00eda101b447c7da47bd249018c168a697c344ea94e6568018fccd2f56e0c7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667TZAQHYI%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJGMEQCIERxUxvXGgxEUKP5Di4Qs85PCnCY4uBwC%2FyphBGx4J9KAiAd7USQ7VKrtjXHDu5Auy%2B6J7JVBgzaYSBkW4u3VPbO%2Fir%2FAwhdEAAaDDYzNzQyMzE4MzgwNSIMQ3R9zg9VrzKZeeXrKtwD%2FLgbCZD%2FQqb82PMcMU2hp6QWTr2m7v7nsU5aU68cqij9ib48nsWRUk6%2FjC3uZQ%2FWGElmdLylIcYjIrOTxC2C48KW04D61Xgtn4p91sUsfbBgBQCAtlYk8p5oGiu7f2bA43y7XaZOQlTTz75hXtIVnYM3Gd%2B44YI31OK%2BUQNveyKeQ8RWIz1ptW5EWBRB%2FjklPAAslHe0VEo5V0foj%2Bg3k6n5EyQKOasWPK6HGQUe07dW1J6VITEEZuw5FoI2rVS0DP1cxxPNI9ueCZZtujmV5tA65sEk5f0wl3OiYDpEiJlzsdqeU1qowo%2FAFy%2FJylU8jVqztoF4UtMrI7%2B9chfC0jxvT63dpu5mQ%2B%2BOA5BH7blqbHKbA7534ioklSiHEGetMVuSwWchjaD8jxE8yvRrE6JA8t%2F4AZZ0WW9CTP6kYpuMmEEtF2vIomB5%2BYS0TLl5IIVObFhaRXFUTM9QdptD9z7l8la93JGSHwqtQ49GxjNjjcSBpHeRyKZYQHDapAbzsAeUSo3QlqKyph6%2B9MOS%2BSjED6JVKRMeBj8ZFnSiVjyfFU1cQ8%2BpKslBMKrEKeBtMrNp9hr0xD7C%2BoA4V2HSMD1LhRevrmnLeRgACfZDcpiNM1%2BAwc%2B6k1B5jYkw5cOSvQY6pgHGpfPrJ%2FDXeLp%2F2Z26t8iO3CERCXBdY5neGWCx0HwyaMEA5H6gyO8DPCpsyHaU41AETYJzBN%2FPqT33WWGWXYjT7yiFInv%2BqLcAtmq33sf6ank8XEM8%2FBdsYqj2L7WF7M76h9uMzFSlstlhMhu295ERugCeG93aT%2B%2BoPaWnc6TQtXWkZXwGPlya%2B%2Bsz0A2e0Kz9SP6bsTYXa4QtrHsaPxQ%2F7nbB59Wu&X-Amz-Signature=211901282e16092fc0079611f345e2695e0e0ce8e321454217bf182e6deadf04&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667TZAQHYI%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJGMEQCIERxUxvXGgxEUKP5Di4Qs85PCnCY4uBwC%2FyphBGx4J9KAiAd7USQ7VKrtjXHDu5Auy%2B6J7JVBgzaYSBkW4u3VPbO%2Fir%2FAwhdEAAaDDYzNzQyMzE4MzgwNSIMQ3R9zg9VrzKZeeXrKtwD%2FLgbCZD%2FQqb82PMcMU2hp6QWTr2m7v7nsU5aU68cqij9ib48nsWRUk6%2FjC3uZQ%2FWGElmdLylIcYjIrOTxC2C48KW04D61Xgtn4p91sUsfbBgBQCAtlYk8p5oGiu7f2bA43y7XaZOQlTTz75hXtIVnYM3Gd%2B44YI31OK%2BUQNveyKeQ8RWIz1ptW5EWBRB%2FjklPAAslHe0VEo5V0foj%2Bg3k6n5EyQKOasWPK6HGQUe07dW1J6VITEEZuw5FoI2rVS0DP1cxxPNI9ueCZZtujmV5tA65sEk5f0wl3OiYDpEiJlzsdqeU1qowo%2FAFy%2FJylU8jVqztoF4UtMrI7%2B9chfC0jxvT63dpu5mQ%2B%2BOA5BH7blqbHKbA7534ioklSiHEGetMVuSwWchjaD8jxE8yvRrE6JA8t%2F4AZZ0WW9CTP6kYpuMmEEtF2vIomB5%2BYS0TLl5IIVObFhaRXFUTM9QdptD9z7l8la93JGSHwqtQ49GxjNjjcSBpHeRyKZYQHDapAbzsAeUSo3QlqKyph6%2B9MOS%2BSjED6JVKRMeBj8ZFnSiVjyfFU1cQ8%2BpKslBMKrEKeBtMrNp9hr0xD7C%2BoA4V2HSMD1LhRevrmnLeRgACfZDcpiNM1%2BAwc%2B6k1B5jYkw5cOSvQY6pgHGpfPrJ%2FDXeLp%2F2Z26t8iO3CERCXBdY5neGWCx0HwyaMEA5H6gyO8DPCpsyHaU41AETYJzBN%2FPqT33WWGWXYjT7yiFInv%2BqLcAtmq33sf6ank8XEM8%2FBdsYqj2L7WF7M76h9uMzFSlstlhMhu295ERugCeG93aT%2B%2BoPaWnc6TQtXWkZXwGPlya%2B%2Bsz0A2e0Kz9SP6bsTYXa4QtrHsaPxQ%2F7nbB59Wu&X-Amz-Signature=db104d23f96fb67cc59db4c93539c62e0fab068b70122c3d3227174b8fc6d00d&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
