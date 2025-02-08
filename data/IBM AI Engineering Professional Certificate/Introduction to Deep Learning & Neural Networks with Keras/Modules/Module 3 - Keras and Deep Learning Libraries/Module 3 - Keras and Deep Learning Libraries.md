

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBPVL6CM%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIDNwEuJqMPKsLYzC6VO%2BJhIP5QOx9spK2%2BgCWuxJq7HdAiEAm8IJjeEdoFr5sdg7MZXWF1wnBacQCGLfo0gyRyU4CzYqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHCJnqVagrOERfIWTircA4M%2FWZzjcuXtksN%2BKINUXqglRVE%2FhEPFG26FfW16ok7Gq1L9kk5WPvlaWIKECXmhUKHOD3bIx0SGKPYA2VWLOv924vsTCrwEl5xNIWfe7ZUa2uJ6d40%2FvBRhhLmHz2p6AAlw%2BFPdq%2BgLTxI9NTTgCLL4ISNMTQypjVKinT5R5XV2PCbHFmtvIbP9zrZkoF0V7%2FdQSq%2FiABILm7ms1gJvUuNZk4m%2BV%2BUAznpNToSR6JVRaPD%2FFHpBVN0Zc0ZThH59hutCmBAcXkbekSief0wjfICzAhTjM0qW0GvBEhz6MIHxgKJgxx91MC2kSDHOYV7EWNXQZp3p2mcen8eKCi0%2Fjx0dthmcCDkGshxkJsEAcgMLcu1Qg3AeSxwdlAC0dDg2n%2FAVGVejfCxC0re0CNlkMzn5kUKQODdjl3G%2FHQgG7PrQPRF8ahltMTOYsKgYIPXn4i%2FBeyvU1iobBIusX7fmCTTasfRrq3cobNU7f%2FfJEoCArHTsKeLCke2V4HfDh3fxvz1oa45st6QBG%2FlCcZ4ktqEgznvWFCi%2BUwiiv3E%2FOY03O9hWKf693vCt0EI0KnTP7hxlLWhaDXkQmWjMvRZ0keeZRFefKHQUBxixhCvcbOyvFU4Z4iTaSjROue%2BvMNmOnL0GOqUBjKRlRknJw5AOzzNACEbDmBlySBf1OBH6olNwNnQsTxSWZP95NjOWb0gjeqqUoFOTdQE46jV5BKp8Aduh29SWrhcxmSWL1yljdxRydOGavx3sR4lFaeE93QLSUI4CZ56iwksycIbQU59NxO3HjqGIGla72CmQwHQJMrepJ0wIP%2F%2Bk3qPRe%2B8YTEgHZ5EtZyXtHamqQ288Ep9lWXdmrTjMBvOqcAcQ&X-Amz-Signature=b8b3bf570144abc3bb608e7f163d6d3e7ef0cbb5761bcb55be0ef2058dbca25b&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBPVL6CM%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIDNwEuJqMPKsLYzC6VO%2BJhIP5QOx9spK2%2BgCWuxJq7HdAiEAm8IJjeEdoFr5sdg7MZXWF1wnBacQCGLfo0gyRyU4CzYqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHCJnqVagrOERfIWTircA4M%2FWZzjcuXtksN%2BKINUXqglRVE%2FhEPFG26FfW16ok7Gq1L9kk5WPvlaWIKECXmhUKHOD3bIx0SGKPYA2VWLOv924vsTCrwEl5xNIWfe7ZUa2uJ6d40%2FvBRhhLmHz2p6AAlw%2BFPdq%2BgLTxI9NTTgCLL4ISNMTQypjVKinT5R5XV2PCbHFmtvIbP9zrZkoF0V7%2FdQSq%2FiABILm7ms1gJvUuNZk4m%2BV%2BUAznpNToSR6JVRaPD%2FFHpBVN0Zc0ZThH59hutCmBAcXkbekSief0wjfICzAhTjM0qW0GvBEhz6MIHxgKJgxx91MC2kSDHOYV7EWNXQZp3p2mcen8eKCi0%2Fjx0dthmcCDkGshxkJsEAcgMLcu1Qg3AeSxwdlAC0dDg2n%2FAVGVejfCxC0re0CNlkMzn5kUKQODdjl3G%2FHQgG7PrQPRF8ahltMTOYsKgYIPXn4i%2FBeyvU1iobBIusX7fmCTTasfRrq3cobNU7f%2FfJEoCArHTsKeLCke2V4HfDh3fxvz1oa45st6QBG%2FlCcZ4ktqEgznvWFCi%2BUwiiv3E%2FOY03O9hWKf693vCt0EI0KnTP7hxlLWhaDXkQmWjMvRZ0keeZRFefKHQUBxixhCvcbOyvFU4Z4iTaSjROue%2BvMNmOnL0GOqUBjKRlRknJw5AOzzNACEbDmBlySBf1OBH6olNwNnQsTxSWZP95NjOWb0gjeqqUoFOTdQE46jV5BKp8Aduh29SWrhcxmSWL1yljdxRydOGavx3sR4lFaeE93QLSUI4CZ56iwksycIbQU59NxO3HjqGIGla72CmQwHQJMrepJ0wIP%2F%2Bk3qPRe%2B8YTEgHZ5EtZyXtHamqQ288Ep9lWXdmrTjMBvOqcAcQ&X-Amz-Signature=afed270204c502b7947b2d25f7f0aafcf9091cdd9de1f9b03ecef20e19b55d32&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBPVL6CM%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIDNwEuJqMPKsLYzC6VO%2BJhIP5QOx9spK2%2BgCWuxJq7HdAiEAm8IJjeEdoFr5sdg7MZXWF1wnBacQCGLfo0gyRyU4CzYqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHCJnqVagrOERfIWTircA4M%2FWZzjcuXtksN%2BKINUXqglRVE%2FhEPFG26FfW16ok7Gq1L9kk5WPvlaWIKECXmhUKHOD3bIx0SGKPYA2VWLOv924vsTCrwEl5xNIWfe7ZUa2uJ6d40%2FvBRhhLmHz2p6AAlw%2BFPdq%2BgLTxI9NTTgCLL4ISNMTQypjVKinT5R5XV2PCbHFmtvIbP9zrZkoF0V7%2FdQSq%2FiABILm7ms1gJvUuNZk4m%2BV%2BUAznpNToSR6JVRaPD%2FFHpBVN0Zc0ZThH59hutCmBAcXkbekSief0wjfICzAhTjM0qW0GvBEhz6MIHxgKJgxx91MC2kSDHOYV7EWNXQZp3p2mcen8eKCi0%2Fjx0dthmcCDkGshxkJsEAcgMLcu1Qg3AeSxwdlAC0dDg2n%2FAVGVejfCxC0re0CNlkMzn5kUKQODdjl3G%2FHQgG7PrQPRF8ahltMTOYsKgYIPXn4i%2FBeyvU1iobBIusX7fmCTTasfRrq3cobNU7f%2FfJEoCArHTsKeLCke2V4HfDh3fxvz1oa45st6QBG%2FlCcZ4ktqEgznvWFCi%2BUwiiv3E%2FOY03O9hWKf693vCt0EI0KnTP7hxlLWhaDXkQmWjMvRZ0keeZRFefKHQUBxixhCvcbOyvFU4Z4iTaSjROue%2BvMNmOnL0GOqUBjKRlRknJw5AOzzNACEbDmBlySBf1OBH6olNwNnQsTxSWZP95NjOWb0gjeqqUoFOTdQE46jV5BKp8Aduh29SWrhcxmSWL1yljdxRydOGavx3sR4lFaeE93QLSUI4CZ56iwksycIbQU59NxO3HjqGIGla72CmQwHQJMrepJ0wIP%2F%2Bk3qPRe%2B8YTEgHZ5EtZyXtHamqQ288Ep9lWXdmrTjMBvOqcAcQ&X-Amz-Signature=270bca9c8be2f3756de92b3dbe773c4c7ea94a461ab26b0bdf9312689cb3da29&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SN7GLGIL%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCICPxEiikgLUIyXtvvDtoIMQXkKvUvPYacMfyuTjU1t9JAiAK9EzrllZZuSIdLdi62NOJ826Uq1JIqi0JuiA%2FE1mLLyqIBAiI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2%2FuZRymjLgo5WAoaKtwDS2zP2Le8DETa7%2Fk7lyFYLsT8ZuvyoNaOjoufBVFPGQFKbRpoaUzMgwkiT%2F3sche1N1JxrLgJTNMzqq0NSj%2BaCH4Ky53USaX2tCQNAh6L%2BojMbtVYInobCnh230%2BsAdz1JUiS0%2FhpDMSzBmf%2BV%2BD05eOcQCYxWfMkbokvYSrz9qT2ts%2BNqokRNGpe0THp3bgr0PfPwnc5IwWwU46UfreBm3oATM11P9iq%2BT53R4mfzeZDqonMHgYgP6eInc9ncZrC7Gv5zzFASnVB2eiLAyhM2MgZ5efDzm0L2JnpQMu8%2BncaB4TuzHBdPUdP9iG9Af7%2FPUBeC3d%2BOZE8YocXAZmWZqFFnGbFhrJ260Njxv2M0RZ1UhoG0J4Ez2440gefhdqixoaX2%2BWDPhnv37oQJaSB8b6YjahuQHShOzNfjCnN4h6dbhLWs%2FdMeqcshaqyHIi%2BYRqFpg9vW0dXyeHgcIUxVJftEXqaEP0f4aG1ut6f1ZhuCbK741I32tgtifH3qcuBjYJU5vGZPzismmwcAL%2FeCx82I%2Fu8tE2GYYcTw%2Fh7lMU2jtdqB0Wlfu0o8Kae2NjuE%2FMmtGI%2BKYm%2B01DDSwgVQN%2BhI7d9fwvx7kc4Ew6bj0eBBdWhtYzeFW%2FrGZIwio6cvQY6pgH5KY4uWiOf9kYHRY5bNPT%2BQEi7bZedOo49B%2BtAyLhTk9bXsXDWP0JX7mqaVoHNvW8IheatH%2FiXIUM50XaiRkCOvqahXmBADokAB%2BSJdWa5P7CDsRu8rr9zusHNgOOLFSmUjv0ZawKaFCZjBzwAaWx3di6roAG332nIBpjskHJnzWnfgPOiUfJUvIgV0zEn9%2B%2BKg4PH2NRRLH6hyCJXCu%2Bc77sN32%2Fo&X-Amz-Signature=c8c1f1b9b86a383a8474aa33b724592e653c7a5d7390f583814947dac7e3659f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QLAGKIW%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQCsdpPI8S90AB80C1uEqsOQMpbD6wbz7VRr4ZAQh7eDMQIgSCWpNzXSAVjLqwYuFBT7QDJN9uAy4p7z0OG36C4OSDYqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIZGkf27TvkzNpTe0ircAxeFPqtfjzxLWiL6gpsWleUHQNRrPsthVIA%2BG1IJrwQvRHKXQYquEy28pIDt55o5EQUd%2B9hU2Ybf7wrdNOvGVPfgSehZFlCrHJ34JFyDpT9ZqahtBa8FMpiNLdUWa9%2BTJaCdiWfAvwaPmkTE36IYNuarCwNoWmKIfx9iQwX57WFOLw6qYPOT0jQRVuczfhLC7sSlLL%2FXIy8yHi5GCv2MB480f1OST6eX4aEnZT9W%2Fhe4L6%2FkqRyEzSeYYWCFJvoCDrAGfiRjmINU%2BxpB%2BKTln4Qrf0uve0i48vEWvWEPIVjkqXaGrvKYLrSor%2FwzBm4fxjfa6LMP1DRMhOQmvaJ%2B%2BfEToB0RdveKttPBvlm%2FQu0q8cp91b8vb5DclWL4VLVWcuJ%2BcTwAYsLpnVFLb56NEh0oCThjTL33KI7X1J8fSIOZ1iNc2eGIzpx4z0UW0pFPrrwXpOL9HcXPD%2FodiU4tBfqy3bpfgL19sWhiBA9jGzPZ7%2BvjZd0Jkxw9WldXvn1F0bQnSvUEU8XpcVULeZIgHE6%2BHYqJkjlz5Qyaeii0MKhJ4GEwSh8q4ADTDg5BelFA5zW1UHvctYwGQwG6opcI7%2BglWQ8XUHiSRNiqtHATqkcdQNxzqL6%2BugDwXLoSMPONnL0GOqUBI01c0OkE0E8Fcz%2BNwDFHUOlxb8tDIkWUpomKNGxY%2BIBKamZmIMdomS%2Bw39lrgQDVLqQ1WFLuvHiZnRr6LaD2K9X%2FYrPrTw31Z8m48PVHs81pINN%2FuEti37WNckd8xr59dfTDlthfU9NIcbL3UuC9e78JujjbQVT9vmTTCcQ8c2ElJnqH39pY5klN35dSNrJAC3YSS75y%2BNicWvn1D684CT1kLhUs&X-Amz-Signature=396fe7a9b636c809a1ebc8b47970f225ff097b21eccd9ad561793220ae624674&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBPVL6CM%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIDNwEuJqMPKsLYzC6VO%2BJhIP5QOx9spK2%2BgCWuxJq7HdAiEAm8IJjeEdoFr5sdg7MZXWF1wnBacQCGLfo0gyRyU4CzYqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHCJnqVagrOERfIWTircA4M%2FWZzjcuXtksN%2BKINUXqglRVE%2FhEPFG26FfW16ok7Gq1L9kk5WPvlaWIKECXmhUKHOD3bIx0SGKPYA2VWLOv924vsTCrwEl5xNIWfe7ZUa2uJ6d40%2FvBRhhLmHz2p6AAlw%2BFPdq%2BgLTxI9NTTgCLL4ISNMTQypjVKinT5R5XV2PCbHFmtvIbP9zrZkoF0V7%2FdQSq%2FiABILm7ms1gJvUuNZk4m%2BV%2BUAznpNToSR6JVRaPD%2FFHpBVN0Zc0ZThH59hutCmBAcXkbekSief0wjfICzAhTjM0qW0GvBEhz6MIHxgKJgxx91MC2kSDHOYV7EWNXQZp3p2mcen8eKCi0%2Fjx0dthmcCDkGshxkJsEAcgMLcu1Qg3AeSxwdlAC0dDg2n%2FAVGVejfCxC0re0CNlkMzn5kUKQODdjl3G%2FHQgG7PrQPRF8ahltMTOYsKgYIPXn4i%2FBeyvU1iobBIusX7fmCTTasfRrq3cobNU7f%2FfJEoCArHTsKeLCke2V4HfDh3fxvz1oa45st6QBG%2FlCcZ4ktqEgznvWFCi%2BUwiiv3E%2FOY03O9hWKf693vCt0EI0KnTP7hxlLWhaDXkQmWjMvRZ0keeZRFefKHQUBxixhCvcbOyvFU4Z4iTaSjROue%2BvMNmOnL0GOqUBjKRlRknJw5AOzzNACEbDmBlySBf1OBH6olNwNnQsTxSWZP95NjOWb0gjeqqUoFOTdQE46jV5BKp8Aduh29SWrhcxmSWL1yljdxRydOGavx3sR4lFaeE93QLSUI4CZ56iwksycIbQU59NxO3HjqGIGla72CmQwHQJMrepJ0wIP%2F%2Bk3qPRe%2B8YTEgHZ5EtZyXtHamqQ288Ep9lWXdmrTjMBvOqcAcQ&X-Amz-Signature=f3ec53e162505bc8c7f23841dc746ee90b4fd190d6873adac2f89fe24c97d206&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBPVL6CM%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIDNwEuJqMPKsLYzC6VO%2BJhIP5QOx9spK2%2BgCWuxJq7HdAiEAm8IJjeEdoFr5sdg7MZXWF1wnBacQCGLfo0gyRyU4CzYqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHCJnqVagrOERfIWTircA4M%2FWZzjcuXtksN%2BKINUXqglRVE%2FhEPFG26FfW16ok7Gq1L9kk5WPvlaWIKECXmhUKHOD3bIx0SGKPYA2VWLOv924vsTCrwEl5xNIWfe7ZUa2uJ6d40%2FvBRhhLmHz2p6AAlw%2BFPdq%2BgLTxI9NTTgCLL4ISNMTQypjVKinT5R5XV2PCbHFmtvIbP9zrZkoF0V7%2FdQSq%2FiABILm7ms1gJvUuNZk4m%2BV%2BUAznpNToSR6JVRaPD%2FFHpBVN0Zc0ZThH59hutCmBAcXkbekSief0wjfICzAhTjM0qW0GvBEhz6MIHxgKJgxx91MC2kSDHOYV7EWNXQZp3p2mcen8eKCi0%2Fjx0dthmcCDkGshxkJsEAcgMLcu1Qg3AeSxwdlAC0dDg2n%2FAVGVejfCxC0re0CNlkMzn5kUKQODdjl3G%2FHQgG7PrQPRF8ahltMTOYsKgYIPXn4i%2FBeyvU1iobBIusX7fmCTTasfRrq3cobNU7f%2FfJEoCArHTsKeLCke2V4HfDh3fxvz1oa45st6QBG%2FlCcZ4ktqEgznvWFCi%2BUwiiv3E%2FOY03O9hWKf693vCt0EI0KnTP7hxlLWhaDXkQmWjMvRZ0keeZRFefKHQUBxixhCvcbOyvFU4Z4iTaSjROue%2BvMNmOnL0GOqUBjKRlRknJw5AOzzNACEbDmBlySBf1OBH6olNwNnQsTxSWZP95NjOWb0gjeqqUoFOTdQE46jV5BKp8Aduh29SWrhcxmSWL1yljdxRydOGavx3sR4lFaeE93QLSUI4CZ56iwksycIbQU59NxO3HjqGIGla72CmQwHQJMrepJ0wIP%2F%2Bk3qPRe%2B8YTEgHZ5EtZyXtHamqQ288Ep9lWXdmrTjMBvOqcAcQ&X-Amz-Signature=10c445f3d17dafcbee0cbf9c7f38f5a2a79f1114540168ce8521a77bd21cde3b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBPVL6CM%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIDNwEuJqMPKsLYzC6VO%2BJhIP5QOx9spK2%2BgCWuxJq7HdAiEAm8IJjeEdoFr5sdg7MZXWF1wnBacQCGLfo0gyRyU4CzYqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHCJnqVagrOERfIWTircA4M%2FWZzjcuXtksN%2BKINUXqglRVE%2FhEPFG26FfW16ok7Gq1L9kk5WPvlaWIKECXmhUKHOD3bIx0SGKPYA2VWLOv924vsTCrwEl5xNIWfe7ZUa2uJ6d40%2FvBRhhLmHz2p6AAlw%2BFPdq%2BgLTxI9NTTgCLL4ISNMTQypjVKinT5R5XV2PCbHFmtvIbP9zrZkoF0V7%2FdQSq%2FiABILm7ms1gJvUuNZk4m%2BV%2BUAznpNToSR6JVRaPD%2FFHpBVN0Zc0ZThH59hutCmBAcXkbekSief0wjfICzAhTjM0qW0GvBEhz6MIHxgKJgxx91MC2kSDHOYV7EWNXQZp3p2mcen8eKCi0%2Fjx0dthmcCDkGshxkJsEAcgMLcu1Qg3AeSxwdlAC0dDg2n%2FAVGVejfCxC0re0CNlkMzn5kUKQODdjl3G%2FHQgG7PrQPRF8ahltMTOYsKgYIPXn4i%2FBeyvU1iobBIusX7fmCTTasfRrq3cobNU7f%2FfJEoCArHTsKeLCke2V4HfDh3fxvz1oa45st6QBG%2FlCcZ4ktqEgznvWFCi%2BUwiiv3E%2FOY03O9hWKf693vCt0EI0KnTP7hxlLWhaDXkQmWjMvRZ0keeZRFefKHQUBxixhCvcbOyvFU4Z4iTaSjROue%2BvMNmOnL0GOqUBjKRlRknJw5AOzzNACEbDmBlySBf1OBH6olNwNnQsTxSWZP95NjOWb0gjeqqUoFOTdQE46jV5BKp8Aduh29SWrhcxmSWL1yljdxRydOGavx3sR4lFaeE93QLSUI4CZ56iwksycIbQU59NxO3HjqGIGla72CmQwHQJMrepJ0wIP%2F%2Bk3qPRe%2B8YTEgHZ5EtZyXtHamqQ288Ep9lWXdmrTjMBvOqcAcQ&X-Amz-Signature=a764c7f3f7845b0a672af28959b4a46fdd57428bf3beb364bd4c4736250480c5&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBPVL6CM%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIDNwEuJqMPKsLYzC6VO%2BJhIP5QOx9spK2%2BgCWuxJq7HdAiEAm8IJjeEdoFr5sdg7MZXWF1wnBacQCGLfo0gyRyU4CzYqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHCJnqVagrOERfIWTircA4M%2FWZzjcuXtksN%2BKINUXqglRVE%2FhEPFG26FfW16ok7Gq1L9kk5WPvlaWIKECXmhUKHOD3bIx0SGKPYA2VWLOv924vsTCrwEl5xNIWfe7ZUa2uJ6d40%2FvBRhhLmHz2p6AAlw%2BFPdq%2BgLTxI9NTTgCLL4ISNMTQypjVKinT5R5XV2PCbHFmtvIbP9zrZkoF0V7%2FdQSq%2FiABILm7ms1gJvUuNZk4m%2BV%2BUAznpNToSR6JVRaPD%2FFHpBVN0Zc0ZThH59hutCmBAcXkbekSief0wjfICzAhTjM0qW0GvBEhz6MIHxgKJgxx91MC2kSDHOYV7EWNXQZp3p2mcen8eKCi0%2Fjx0dthmcCDkGshxkJsEAcgMLcu1Qg3AeSxwdlAC0dDg2n%2FAVGVejfCxC0re0CNlkMzn5kUKQODdjl3G%2FHQgG7PrQPRF8ahltMTOYsKgYIPXn4i%2FBeyvU1iobBIusX7fmCTTasfRrq3cobNU7f%2FfJEoCArHTsKeLCke2V4HfDh3fxvz1oa45st6QBG%2FlCcZ4ktqEgznvWFCi%2BUwiiv3E%2FOY03O9hWKf693vCt0EI0KnTP7hxlLWhaDXkQmWjMvRZ0keeZRFefKHQUBxixhCvcbOyvFU4Z4iTaSjROue%2BvMNmOnL0GOqUBjKRlRknJw5AOzzNACEbDmBlySBf1OBH6olNwNnQsTxSWZP95NjOWb0gjeqqUoFOTdQE46jV5BKp8Aduh29SWrhcxmSWL1yljdxRydOGavx3sR4lFaeE93QLSUI4CZ56iwksycIbQU59NxO3HjqGIGla72CmQwHQJMrepJ0wIP%2F%2Bk3qPRe%2B8YTEgHZ5EtZyXtHamqQ288Ep9lWXdmrTjMBvOqcAcQ&X-Amz-Signature=17eb7e5ac7bda21e7a183bf25886fc94fcd781595284abdfa3172255a0cadb40&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
