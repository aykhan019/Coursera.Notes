

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ULR2ZPDC%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111102Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIGNT5k1w9ZJ1nvFSrhSNnqAY93hXjx9SPjeCWNCwCtFdAiBd7r3856uLi7i6GF3G4tgKkGZRehOiSkh7ghbnXc76eSqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMKuxyJLjaPn%2FyLT9yKtwDymkHlYl%2Fmr1jxdR9G9T06LMgeWXs5IchM1T2JGEMHWhcx83mgaJ09GpXW%2FWgL%2Bw2NOzh1H%2FuBBf%2Ba8OBNarjPyCJ6ZZwvaidlScnrtDLBY79bJdIWhTI1NMjGOe7y8EmUk4aFRwCYdLKiA12lJN7OBAMciIBkg%2FlBwHlyrdSm6Pz7Ky5IxMxhKEwBm94I29RtZ7ECpxxXi89bZ2%2FYOcXou5nQbS3WizXKfL3lj0bqnMSFAfONgeiysUBBUXiRtN7piz8EhFkItz1SN2MBWA9%2B05JQ%2BUhSd9WpnMmEeSbHTf1hfR5ADtDPVgv%2Fi7Jj6uVYo2TolEI3KGWOvcvWAONZH3wqPwmt9YREQn8jQgDkIg%2Bg%2FIbI%2FB8QVJzizqhMAyNHPbqzf1QnB7JXfYCpTfZLVAxnDFnm%2B7ukq73uGovZTNFOJ%2FX2lrqWAMMMJRf%2FPEINbU5ArGAMmqC9icIMMXrsYdO9%2FF3DUTUaXQtAp4aEM8q%2B%2FrRbvLaBCP8ClWzU%2F7XCnhwyFO7O9Aq2fCf%2FScDmaodvMQ2W8XhZSVjFS%2FSEeCxf79YhULoDhjBEW%2BY9Z47KKnTG1UfXDspIidLhll4rs3HjmQ9vzVDMR3eL7xNDMUDv43uXE8C9xJojjowh46cvQY6pgGZtfc%2BR29MizAaGkf4TTUTeVKayvt2LZmuR8eU55lEWtAXNpwYHtQTRxRfcGFQch0gsMwhWnFrtpy1UCSRFdA0fQv0oAzKTqGtwvfOhhbbXT4ScnX2nVJ%2FH8wjr7zfslYDYbdgxznSy1rCdOYrtJQvmZ7hrf3Sbs0WPsc0LucFoq2%2BQJKFlPKC48Krc4KtYb3yUrEM0tqnKksRqpZy7Eh%2BcGOD1Yvo&X-Amz-Signature=708f617e61eda9e4750ee6a2a2800d708d772134f5eb7ee3e3724968c66a65d0&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ULR2ZPDC%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111102Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIGNT5k1w9ZJ1nvFSrhSNnqAY93hXjx9SPjeCWNCwCtFdAiBd7r3856uLi7i6GF3G4tgKkGZRehOiSkh7ghbnXc76eSqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMKuxyJLjaPn%2FyLT9yKtwDymkHlYl%2Fmr1jxdR9G9T06LMgeWXs5IchM1T2JGEMHWhcx83mgaJ09GpXW%2FWgL%2Bw2NOzh1H%2FuBBf%2Ba8OBNarjPyCJ6ZZwvaidlScnrtDLBY79bJdIWhTI1NMjGOe7y8EmUk4aFRwCYdLKiA12lJN7OBAMciIBkg%2FlBwHlyrdSm6Pz7Ky5IxMxhKEwBm94I29RtZ7ECpxxXi89bZ2%2FYOcXou5nQbS3WizXKfL3lj0bqnMSFAfONgeiysUBBUXiRtN7piz8EhFkItz1SN2MBWA9%2B05JQ%2BUhSd9WpnMmEeSbHTf1hfR5ADtDPVgv%2Fi7Jj6uVYo2TolEI3KGWOvcvWAONZH3wqPwmt9YREQn8jQgDkIg%2Bg%2FIbI%2FB8QVJzizqhMAyNHPbqzf1QnB7JXfYCpTfZLVAxnDFnm%2B7ukq73uGovZTNFOJ%2FX2lrqWAMMMJRf%2FPEINbU5ArGAMmqC9icIMMXrsYdO9%2FF3DUTUaXQtAp4aEM8q%2B%2FrRbvLaBCP8ClWzU%2F7XCnhwyFO7O9Aq2fCf%2FScDmaodvMQ2W8XhZSVjFS%2FSEeCxf79YhULoDhjBEW%2BY9Z47KKnTG1UfXDspIidLhll4rs3HjmQ9vzVDMR3eL7xNDMUDv43uXE8C9xJojjowh46cvQY6pgGZtfc%2BR29MizAaGkf4TTUTeVKayvt2LZmuR8eU55lEWtAXNpwYHtQTRxRfcGFQch0gsMwhWnFrtpy1UCSRFdA0fQv0oAzKTqGtwvfOhhbbXT4ScnX2nVJ%2FH8wjr7zfslYDYbdgxznSy1rCdOYrtJQvmZ7hrf3Sbs0WPsc0LucFoq2%2BQJKFlPKC48Krc4KtYb3yUrEM0tqnKksRqpZy7Eh%2BcGOD1Yvo&X-Amz-Signature=ec70d4a10a5b3f3f968c2588e09fc7fa0b749ffaaf0e16a9030a5d54a7c1caf8&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ULR2ZPDC%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111102Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIGNT5k1w9ZJ1nvFSrhSNnqAY93hXjx9SPjeCWNCwCtFdAiBd7r3856uLi7i6GF3G4tgKkGZRehOiSkh7ghbnXc76eSqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMKuxyJLjaPn%2FyLT9yKtwDymkHlYl%2Fmr1jxdR9G9T06LMgeWXs5IchM1T2JGEMHWhcx83mgaJ09GpXW%2FWgL%2Bw2NOzh1H%2FuBBf%2Ba8OBNarjPyCJ6ZZwvaidlScnrtDLBY79bJdIWhTI1NMjGOe7y8EmUk4aFRwCYdLKiA12lJN7OBAMciIBkg%2FlBwHlyrdSm6Pz7Ky5IxMxhKEwBm94I29RtZ7ECpxxXi89bZ2%2FYOcXou5nQbS3WizXKfL3lj0bqnMSFAfONgeiysUBBUXiRtN7piz8EhFkItz1SN2MBWA9%2B05JQ%2BUhSd9WpnMmEeSbHTf1hfR5ADtDPVgv%2Fi7Jj6uVYo2TolEI3KGWOvcvWAONZH3wqPwmt9YREQn8jQgDkIg%2Bg%2FIbI%2FB8QVJzizqhMAyNHPbqzf1QnB7JXfYCpTfZLVAxnDFnm%2B7ukq73uGovZTNFOJ%2FX2lrqWAMMMJRf%2FPEINbU5ArGAMmqC9icIMMXrsYdO9%2FF3DUTUaXQtAp4aEM8q%2B%2FrRbvLaBCP8ClWzU%2F7XCnhwyFO7O9Aq2fCf%2FScDmaodvMQ2W8XhZSVjFS%2FSEeCxf79YhULoDhjBEW%2BY9Z47KKnTG1UfXDspIidLhll4rs3HjmQ9vzVDMR3eL7xNDMUDv43uXE8C9xJojjowh46cvQY6pgGZtfc%2BR29MizAaGkf4TTUTeVKayvt2LZmuR8eU55lEWtAXNpwYHtQTRxRfcGFQch0gsMwhWnFrtpy1UCSRFdA0fQv0oAzKTqGtwvfOhhbbXT4ScnX2nVJ%2FH8wjr7zfslYDYbdgxznSy1rCdOYrtJQvmZ7hrf3Sbs0WPsc0LucFoq2%2BQJKFlPKC48Krc4KtYb3yUrEM0tqnKksRqpZy7Eh%2BcGOD1Yvo&X-Amz-Signature=ac62cce7c480d58d834d75aceef81bc908655e6a3917b2258cc1a3af78216301&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667D6V7MJ2%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQCiU8d1FM8cMHRyCib8G29J6lpWVtpmPjFLi2nLdw9KSAIgVsKbyZ%2FwJi7Xl%2FWslCeqJ9NA3HIw%2FxSZNOYKvr1Y2lQqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFCp959WB65WjfY0gyrcA1oa6tkYF%2FMAPitPrTetruemhrMKiAJoFEosXeDbQDtSpW2vHAX%2Br3bD4gxsCCLC6k7iN2HDKG5OPu4oaWI4MCQkVW%2FgHbnud8jKhb1QJ9mQ4r0v2%2BBXXrz9ulmVBcUPkW%2FqCg5vj1CZ4sg2THUnEpsVHXOo6B8KwTAgDr3sez9SVkLqA0Y0REKJTbESyOznokrvCk1ufEPHchNnDEi2jcFy0o42WbNlDTLl3Bb6abykWKd302%2FYjLtMtnMibqPLb5iQfqiM4uXzJzSBecXYOv1vhPsT8QKjiHu2rHT9c%2BIhnHPVC%2Fb2dRrb15UX4gi%2BUPZNp0%2FG2QIwyjgFctlVr8o3hSDlRlWZRv3Aoww1RdFJMl%2BgUVDNfdzMEH%2Bis6o1d%2BSfD4xMCSLLUGnJOy%2FygtvTPkhh0mdtUsRnp%2Bu3whf9LkcfNH%2BOYVzCNStr4GIhXS%2F%2FZ2xcUT3lkmWHqONid5JwjP0FUb9tZbKzyBEna%2B5oKR9pHYZrHQovUMHq%2BciKYXBtlbWzuZmXUZG4ye1bGF5EBaU5zByJpKMMr8ZZnzevPkvsfI5Jpga5szPUqaCWyQMF9EQAnZ9LdebN1KjhC4B%2BSu3AoXmGhc885V16piWG7uN1lVhhzHoj6Cc8MOqNnL0GOqUBt1yxsgEEPfwaXqBa%2B%2F8F1vwbYZveIWVluhZ9kdDPkalzXaLFbsoE5gI%2BUpi50sZVtKVyRhzUoVuB18PUgPB48uQxIaR1Qsk5SYVbyjnno1ybaeA%2FqkwSTAMabhTtRvJ94Ab5CMQkwFNpbD3i8afULTqwOg%2BMWo0XbljXF4%2BZN%2F84AIp%2BHtY5NOiC7gjwGuh0Ami0Iuel2iy6CoDEiCAdrIROJIAV&X-Amz-Signature=46f3a753df2ec17a052b60b518069b877c429513bd71e3a3443641716451bdb2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XLBC4TER%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQD02PJIrO%2FD8vystIznOALDmikyALf0jNkbAiU6OTAG%2FAIgP8YnORMEC3C9ohlJ8FMQvJxssHJ%2FRr74Vh9r6%2FTZ8WsqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFlrBcDd2bz4N0jL%2BCrcA6VqbfFHCIvaIjC6%2Bbg6rXojqqvLgISFz%2FbzowoCLXJVY%2FURtVeE2hUq9XJzxJUHJVG7e2Ykj2L128V7QLRRjMCM0VziXco%2B1NdgVXpc9ujLlumdVwnbvH9%2F1U%2BrqKkHzbBlGEOBuecs8IMjfkCLJvaUDKYz6Xwjuj0bg4%2FSO%2FN%2F8sR4OB%2FeUSVEw%2FF1n2pigc%2BYXVZP0zj5UHWFfOhuNHmcLpMP71YFcFxgUEW%2BBbCn6TYFmeQ01hulWdWfBTObj6AtDcfBAzbbGU%2Fc6wJKj4dJRn%2BSOqHkvrgYWufUoF3MyEUMDChRenerlX0RnVeIF9dzs%2F2k6wQ7jddBEydrRYTzvvtKXU8gWc%2FWBi5%2FhLRbpSn0z9qatgoPTuDN8S5UTaWXxvzkzR4Vr4IumeddWvBGcmnBrTdqtswmTSig%2Fmw%2F4%2FNrpRl4v7VsK5FiOKroShwLtG2STEpgFkBHREE4ktpU9U2zgIqqEQxSw21d9wj6XS%2BQ4nauGTbJG1R1h43pw9auNCNtCnlnvSPE1Zbi808K0kW2vaaX5plO8YtsWi8%2FvRce%2FiC6CqwplzojfcrORpaZ2Oa1UNkBo7d%2FPl9D3GyKYQpYKxlaj6AXHqY4eCoS8FWaXHuNZfSJaN4ZMOuNnL0GOqUBDbDp4vR2MEols5EL9OopZkLt4xoo3RxQSILxpZPpLB%2B6b9Iyi3JrCv%2BVe1rsj1V9WR526vm7tY0Us0IjD%2BrT%2FbXI31%2BY%2FM0BycwaE0hmasZCcXatz6ZpV%2F0er2%2Fk3XbZsMK0vmYprrg2369zyp8i9Qnvk0osJRpS8k3AiSOpvZfoo18ulh2GgursdCJCLbv60bqkEv%2BtPbpUq6IhcTCkA6gXSPFy&X-Amz-Signature=16cf4a82e41b462b6a995dea4ccfc689b2285ba9de7940d5f9bca097f3ff1a3d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ULR2ZPDC%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111102Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIGNT5k1w9ZJ1nvFSrhSNnqAY93hXjx9SPjeCWNCwCtFdAiBd7r3856uLi7i6GF3G4tgKkGZRehOiSkh7ghbnXc76eSqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMKuxyJLjaPn%2FyLT9yKtwDymkHlYl%2Fmr1jxdR9G9T06LMgeWXs5IchM1T2JGEMHWhcx83mgaJ09GpXW%2FWgL%2Bw2NOzh1H%2FuBBf%2Ba8OBNarjPyCJ6ZZwvaidlScnrtDLBY79bJdIWhTI1NMjGOe7y8EmUk4aFRwCYdLKiA12lJN7OBAMciIBkg%2FlBwHlyrdSm6Pz7Ky5IxMxhKEwBm94I29RtZ7ECpxxXi89bZ2%2FYOcXou5nQbS3WizXKfL3lj0bqnMSFAfONgeiysUBBUXiRtN7piz8EhFkItz1SN2MBWA9%2B05JQ%2BUhSd9WpnMmEeSbHTf1hfR5ADtDPVgv%2Fi7Jj6uVYo2TolEI3KGWOvcvWAONZH3wqPwmt9YREQn8jQgDkIg%2Bg%2FIbI%2FB8QVJzizqhMAyNHPbqzf1QnB7JXfYCpTfZLVAxnDFnm%2B7ukq73uGovZTNFOJ%2FX2lrqWAMMMJRf%2FPEINbU5ArGAMmqC9icIMMXrsYdO9%2FF3DUTUaXQtAp4aEM8q%2B%2FrRbvLaBCP8ClWzU%2F7XCnhwyFO7O9Aq2fCf%2FScDmaodvMQ2W8XhZSVjFS%2FSEeCxf79YhULoDhjBEW%2BY9Z47KKnTG1UfXDspIidLhll4rs3HjmQ9vzVDMR3eL7xNDMUDv43uXE8C9xJojjowh46cvQY6pgGZtfc%2BR29MizAaGkf4TTUTeVKayvt2LZmuR8eU55lEWtAXNpwYHtQTRxRfcGFQch0gsMwhWnFrtpy1UCSRFdA0fQv0oAzKTqGtwvfOhhbbXT4ScnX2nVJ%2FH8wjr7zfslYDYbdgxznSy1rCdOYrtJQvmZ7hrf3Sbs0WPsc0LucFoq2%2BQJKFlPKC48Krc4KtYb3yUrEM0tqnKksRqpZy7Eh%2BcGOD1Yvo&X-Amz-Signature=61fd020fe55cc57052a6e0d9868f5d6fadeb1193f2ef0958a7f4e275cf76db3e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ULR2ZPDC%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111102Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIGNT5k1w9ZJ1nvFSrhSNnqAY93hXjx9SPjeCWNCwCtFdAiBd7r3856uLi7i6GF3G4tgKkGZRehOiSkh7ghbnXc76eSqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMKuxyJLjaPn%2FyLT9yKtwDymkHlYl%2Fmr1jxdR9G9T06LMgeWXs5IchM1T2JGEMHWhcx83mgaJ09GpXW%2FWgL%2Bw2NOzh1H%2FuBBf%2Ba8OBNarjPyCJ6ZZwvaidlScnrtDLBY79bJdIWhTI1NMjGOe7y8EmUk4aFRwCYdLKiA12lJN7OBAMciIBkg%2FlBwHlyrdSm6Pz7Ky5IxMxhKEwBm94I29RtZ7ECpxxXi89bZ2%2FYOcXou5nQbS3WizXKfL3lj0bqnMSFAfONgeiysUBBUXiRtN7piz8EhFkItz1SN2MBWA9%2B05JQ%2BUhSd9WpnMmEeSbHTf1hfR5ADtDPVgv%2Fi7Jj6uVYo2TolEI3KGWOvcvWAONZH3wqPwmt9YREQn8jQgDkIg%2Bg%2FIbI%2FB8QVJzizqhMAyNHPbqzf1QnB7JXfYCpTfZLVAxnDFnm%2B7ukq73uGovZTNFOJ%2FX2lrqWAMMMJRf%2FPEINbU5ArGAMmqC9icIMMXrsYdO9%2FF3DUTUaXQtAp4aEM8q%2B%2FrRbvLaBCP8ClWzU%2F7XCnhwyFO7O9Aq2fCf%2FScDmaodvMQ2W8XhZSVjFS%2FSEeCxf79YhULoDhjBEW%2BY9Z47KKnTG1UfXDspIidLhll4rs3HjmQ9vzVDMR3eL7xNDMUDv43uXE8C9xJojjowh46cvQY6pgGZtfc%2BR29MizAaGkf4TTUTeVKayvt2LZmuR8eU55lEWtAXNpwYHtQTRxRfcGFQch0gsMwhWnFrtpy1UCSRFdA0fQv0oAzKTqGtwvfOhhbbXT4ScnX2nVJ%2FH8wjr7zfslYDYbdgxznSy1rCdOYrtJQvmZ7hrf3Sbs0WPsc0LucFoq2%2BQJKFlPKC48Krc4KtYb3yUrEM0tqnKksRqpZy7Eh%2BcGOD1Yvo&X-Amz-Signature=e783d3a42a04a8a3effd55c3573fe2190859e20c79976cbf4e113240467ebfb4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ULR2ZPDC%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111102Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIGNT5k1w9ZJ1nvFSrhSNnqAY93hXjx9SPjeCWNCwCtFdAiBd7r3856uLi7i6GF3G4tgKkGZRehOiSkh7ghbnXc76eSqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMKuxyJLjaPn%2FyLT9yKtwDymkHlYl%2Fmr1jxdR9G9T06LMgeWXs5IchM1T2JGEMHWhcx83mgaJ09GpXW%2FWgL%2Bw2NOzh1H%2FuBBf%2Ba8OBNarjPyCJ6ZZwvaidlScnrtDLBY79bJdIWhTI1NMjGOe7y8EmUk4aFRwCYdLKiA12lJN7OBAMciIBkg%2FlBwHlyrdSm6Pz7Ky5IxMxhKEwBm94I29RtZ7ECpxxXi89bZ2%2FYOcXou5nQbS3WizXKfL3lj0bqnMSFAfONgeiysUBBUXiRtN7piz8EhFkItz1SN2MBWA9%2B05JQ%2BUhSd9WpnMmEeSbHTf1hfR5ADtDPVgv%2Fi7Jj6uVYo2TolEI3KGWOvcvWAONZH3wqPwmt9YREQn8jQgDkIg%2Bg%2FIbI%2FB8QVJzizqhMAyNHPbqzf1QnB7JXfYCpTfZLVAxnDFnm%2B7ukq73uGovZTNFOJ%2FX2lrqWAMMMJRf%2FPEINbU5ArGAMmqC9icIMMXrsYdO9%2FF3DUTUaXQtAp4aEM8q%2B%2FrRbvLaBCP8ClWzU%2F7XCnhwyFO7O9Aq2fCf%2FScDmaodvMQ2W8XhZSVjFS%2FSEeCxf79YhULoDhjBEW%2BY9Z47KKnTG1UfXDspIidLhll4rs3HjmQ9vzVDMR3eL7xNDMUDv43uXE8C9xJojjowh46cvQY6pgGZtfc%2BR29MizAaGkf4TTUTeVKayvt2LZmuR8eU55lEWtAXNpwYHtQTRxRfcGFQch0gsMwhWnFrtpy1UCSRFdA0fQv0oAzKTqGtwvfOhhbbXT4ScnX2nVJ%2FH8wjr7zfslYDYbdgxznSy1rCdOYrtJQvmZ7hrf3Sbs0WPsc0LucFoq2%2BQJKFlPKC48Krc4KtYb3yUrEM0tqnKksRqpZy7Eh%2BcGOD1Yvo&X-Amz-Signature=808cd2f00f513185639bc4ee5db5d78e57ddbc3ba8fc2ee996a6681e36bb6bc7&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ULR2ZPDC%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111102Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIGNT5k1w9ZJ1nvFSrhSNnqAY93hXjx9SPjeCWNCwCtFdAiBd7r3856uLi7i6GF3G4tgKkGZRehOiSkh7ghbnXc76eSqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMKuxyJLjaPn%2FyLT9yKtwDymkHlYl%2Fmr1jxdR9G9T06LMgeWXs5IchM1T2JGEMHWhcx83mgaJ09GpXW%2FWgL%2Bw2NOzh1H%2FuBBf%2Ba8OBNarjPyCJ6ZZwvaidlScnrtDLBY79bJdIWhTI1NMjGOe7y8EmUk4aFRwCYdLKiA12lJN7OBAMciIBkg%2FlBwHlyrdSm6Pz7Ky5IxMxhKEwBm94I29RtZ7ECpxxXi89bZ2%2FYOcXou5nQbS3WizXKfL3lj0bqnMSFAfONgeiysUBBUXiRtN7piz8EhFkItz1SN2MBWA9%2B05JQ%2BUhSd9WpnMmEeSbHTf1hfR5ADtDPVgv%2Fi7Jj6uVYo2TolEI3KGWOvcvWAONZH3wqPwmt9YREQn8jQgDkIg%2Bg%2FIbI%2FB8QVJzizqhMAyNHPbqzf1QnB7JXfYCpTfZLVAxnDFnm%2B7ukq73uGovZTNFOJ%2FX2lrqWAMMMJRf%2FPEINbU5ArGAMmqC9icIMMXrsYdO9%2FF3DUTUaXQtAp4aEM8q%2B%2FrRbvLaBCP8ClWzU%2F7XCnhwyFO7O9Aq2fCf%2FScDmaodvMQ2W8XhZSVjFS%2FSEeCxf79YhULoDhjBEW%2BY9Z47KKnTG1UfXDspIidLhll4rs3HjmQ9vzVDMR3eL7xNDMUDv43uXE8C9xJojjowh46cvQY6pgGZtfc%2BR29MizAaGkf4TTUTeVKayvt2LZmuR8eU55lEWtAXNpwYHtQTRxRfcGFQch0gsMwhWnFrtpy1UCSRFdA0fQv0oAzKTqGtwvfOhhbbXT4ScnX2nVJ%2FH8wjr7zfslYDYbdgxznSy1rCdOYrtJQvmZ7hrf3Sbs0WPsc0LucFoq2%2BQJKFlPKC48Krc4KtYb3yUrEM0tqnKksRqpZy7Eh%2BcGOD1Yvo&X-Amz-Signature=45437c8691b7da10c09cc4b56814014f449b65eed4d314f2290698762e96d12c&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
