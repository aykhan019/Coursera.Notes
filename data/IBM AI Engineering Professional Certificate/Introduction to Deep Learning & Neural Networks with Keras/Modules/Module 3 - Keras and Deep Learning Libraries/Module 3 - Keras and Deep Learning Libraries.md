

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YEGG3U2J%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJIMEYCIQCj9Dm4v%2BPkGayX4vW0VnqKXNmFvxwykCrFwD3yBwX2vgIhAI0xjFez9mBDCJFC5QLGwjwYkaeJzAFrRnTA3yj50jgKKv8DCEcQABoMNjM3NDIzMTgzODA1IgyQFU1cU%2F4OQPp4YDcq3AMVRCzM8YpqG9%2B8qMNyjgpUPzBHk0oxDt4koSmrODR2oN5bthsPTeBu9sfNkQEeVnzWKEtZ7CAPjqs5mt1h4tQE3M%2Fi9sKcTxmXC1vDZK9M0r0G%2FUaw8r1R1dL3dZeHSfsi1rT8DqYkfO07F9IRWLgsxX29%2F%2B61xRCu6D02%2Bc2Pw67FsmtZclG8IKkTK2eUVUAWl91glXhiQBVjRMD%2BhcwowDxWD%2BX7djfPGmK5o9OT2oGHLr9QfbQ%2F1deH8dtwfp%2FbhT1wzzVR6GqYreWpKrLoD6M182q%2FIu9ZqAarTNs%2BYwGtt7rsq234neJlSSbj8%2FEpqPSagDHilv6%2BBk0C9nLw5QmSyecQei16k1EE6n9QBlOIc7YdYkprPeYcHtk06uPfRCXTqJ5AkqR5UxhBA02ZT4xuF1HGs1qQfMVnyfEXg2osPgE6BLXthy3V9zcTSFgODqdbWa%2B6XO6otVBoJP5G31kUgsDfTssWkm55KUNKhJ%2BExNv912%2FZtyfEOw%2B8tniHnvSkHWrhEXJgi8Lqnx7r3RFJFuO9BUV2IqCppKk3eFhkdPeeaECMA2E8bM4rzQEQVhjPTkiWxWKmHog2uL9Sy5tqSdckNs2CZAxDqFNRstehaqchZQjyCFQNrzD54429BjqkAeYAjH1C2OGgA%2BXHdvqLJAmKRcirR5UBw2Z4%2B%2Bc%2Bw7W1cnmJO%2FcPJuWut928vcmFvHZgXOlgCUXZAI6v8oozJsjM1t4HM3yELVjQC6pZsdDDIXYfpwK0xs%2BLIEE5ufJjRRqID%2B001uu8%2BwuShtQs6MYqNlFud4ihV499%2B4etkvnV7Umj9KERxLCWFKnaDA8jg4YfOcGp3JYpUeQh8pylXgrmlldz&X-Amz-Signature=18f7385f186d8efe8d1330d4aff46680819a659d1b6a758ca323facc092080d8&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YEGG3U2J%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJIMEYCIQCj9Dm4v%2BPkGayX4vW0VnqKXNmFvxwykCrFwD3yBwX2vgIhAI0xjFez9mBDCJFC5QLGwjwYkaeJzAFrRnTA3yj50jgKKv8DCEcQABoMNjM3NDIzMTgzODA1IgyQFU1cU%2F4OQPp4YDcq3AMVRCzM8YpqG9%2B8qMNyjgpUPzBHk0oxDt4koSmrODR2oN5bthsPTeBu9sfNkQEeVnzWKEtZ7CAPjqs5mt1h4tQE3M%2Fi9sKcTxmXC1vDZK9M0r0G%2FUaw8r1R1dL3dZeHSfsi1rT8DqYkfO07F9IRWLgsxX29%2F%2B61xRCu6D02%2Bc2Pw67FsmtZclG8IKkTK2eUVUAWl91glXhiQBVjRMD%2BhcwowDxWD%2BX7djfPGmK5o9OT2oGHLr9QfbQ%2F1deH8dtwfp%2FbhT1wzzVR6GqYreWpKrLoD6M182q%2FIu9ZqAarTNs%2BYwGtt7rsq234neJlSSbj8%2FEpqPSagDHilv6%2BBk0C9nLw5QmSyecQei16k1EE6n9QBlOIc7YdYkprPeYcHtk06uPfRCXTqJ5AkqR5UxhBA02ZT4xuF1HGs1qQfMVnyfEXg2osPgE6BLXthy3V9zcTSFgODqdbWa%2B6XO6otVBoJP5G31kUgsDfTssWkm55KUNKhJ%2BExNv912%2FZtyfEOw%2B8tniHnvSkHWrhEXJgi8Lqnx7r3RFJFuO9BUV2IqCppKk3eFhkdPeeaECMA2E8bM4rzQEQVhjPTkiWxWKmHog2uL9Sy5tqSdckNs2CZAxDqFNRstehaqchZQjyCFQNrzD54429BjqkAeYAjH1C2OGgA%2BXHdvqLJAmKRcirR5UBw2Z4%2B%2Bc%2Bw7W1cnmJO%2FcPJuWut928vcmFvHZgXOlgCUXZAI6v8oozJsjM1t4HM3yELVjQC6pZsdDDIXYfpwK0xs%2BLIEE5ufJjRRqID%2B001uu8%2BwuShtQs6MYqNlFud4ihV499%2B4etkvnV7Umj9KERxLCWFKnaDA8jg4YfOcGp3JYpUeQh8pylXgrmlldz&X-Amz-Signature=e7d6a36c1a4529bfbd262149f9e07ca727b613d2a1a23b8715a09ea53ded9744&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YEGG3U2J%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJIMEYCIQCj9Dm4v%2BPkGayX4vW0VnqKXNmFvxwykCrFwD3yBwX2vgIhAI0xjFez9mBDCJFC5QLGwjwYkaeJzAFrRnTA3yj50jgKKv8DCEcQABoMNjM3NDIzMTgzODA1IgyQFU1cU%2F4OQPp4YDcq3AMVRCzM8YpqG9%2B8qMNyjgpUPzBHk0oxDt4koSmrODR2oN5bthsPTeBu9sfNkQEeVnzWKEtZ7CAPjqs5mt1h4tQE3M%2Fi9sKcTxmXC1vDZK9M0r0G%2FUaw8r1R1dL3dZeHSfsi1rT8DqYkfO07F9IRWLgsxX29%2F%2B61xRCu6D02%2Bc2Pw67FsmtZclG8IKkTK2eUVUAWl91glXhiQBVjRMD%2BhcwowDxWD%2BX7djfPGmK5o9OT2oGHLr9QfbQ%2F1deH8dtwfp%2FbhT1wzzVR6GqYreWpKrLoD6M182q%2FIu9ZqAarTNs%2BYwGtt7rsq234neJlSSbj8%2FEpqPSagDHilv6%2BBk0C9nLw5QmSyecQei16k1EE6n9QBlOIc7YdYkprPeYcHtk06uPfRCXTqJ5AkqR5UxhBA02ZT4xuF1HGs1qQfMVnyfEXg2osPgE6BLXthy3V9zcTSFgODqdbWa%2B6XO6otVBoJP5G31kUgsDfTssWkm55KUNKhJ%2BExNv912%2FZtyfEOw%2B8tniHnvSkHWrhEXJgi8Lqnx7r3RFJFuO9BUV2IqCppKk3eFhkdPeeaECMA2E8bM4rzQEQVhjPTkiWxWKmHog2uL9Sy5tqSdckNs2CZAxDqFNRstehaqchZQjyCFQNrzD54429BjqkAeYAjH1C2OGgA%2BXHdvqLJAmKRcirR5UBw2Z4%2B%2Bc%2Bw7W1cnmJO%2FcPJuWut928vcmFvHZgXOlgCUXZAI6v8oozJsjM1t4HM3yELVjQC6pZsdDDIXYfpwK0xs%2BLIEE5ufJjRRqID%2B001uu8%2BwuShtQs6MYqNlFud4ihV499%2B4etkvnV7Umj9KERxLCWFKnaDA8jg4YfOcGp3JYpUeQh8pylXgrmlldz&X-Amz-Signature=0ce41002dc9725d5a67babc32076ec5737c9ba0173436fb3729816352e26e761&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XFSPYFDY%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIDuTOQqr9q9sBi2XunKlZZ6FTJn6EksPgeclcsiWvkFWAiEA5iiqUVR%2FwqxeSPWGS4bTJuyfnt7h5sQmR7alnpijF4Uq%2FwMISBAAGgw2Mzc0MjMxODM4MDUiDHfWr5GvGuNsODaJCCrcA4rGVFQcYGtfn5%2FPJhrRKT1Cq8Hc6ImdumTvLo77eUoSUlY7QLjkhkRlZuEes52%2BdfjS9Hf%2B7Y5KxxMG0bvO%2BLbK%2Bh1ZCjLBgCoE%2BoRPq2WZaEmkD3t9Pr9%2BStudGuroWvyCAAI2MHDcs4HoTEDvotj2BUJfwDYxxsU3i%2BKcGdb9mdEooApEk%2B4pDVy65Mp4nzZt06KeehXCYXe2Zk3eOmuoGj5iQQNXlcPMBLsk3WSDvfPFJJ2Q8l9Cg%2F0vOF219L%2Bpuf1He4O41QrwGjma%2BGVtvOzyG7F7wcQsLi9Q1%2FTrDzqzNp1RGmYmejHnQbuefJjzX03OTdl2dt2fuQTCbPUAv8LOkSYq84LvZ%2Bo3A0N0yyGEcvOnPc7vW79wVc0WTvCIs9rj8oSwhvK7g%2FzaJI1YdP0CtlIZ4Ag0oX8kUDQ2GBZIXq%2BEOr%2BQ%2F5bw19E2XPIZQMH2olB46%2F3DEmv04%2BJzSY4BL15O9K5v8vETDUnRkwp2WTORcFXUXqhI61zAd1MuECpnf7qcvyusT3szR5VtlA5WJmKGITDtsRG3qYDnHZpcmsNUtlZcIvelwFoqe12LB9UMtMIl5mGf4KdSCulv%2FiEKoi2jkuVWb1qnnL6NEhuNWfJ3UGxkjSyPMMCAjr0GOqUBe8dnInvPQ0pl1F1DGbyzzNluT6lnQi4BIIhaRrKJS5E1THmojgIXa%2BdQK8WLN%2FsMPO6%2F1TFdeM8wefkgVOxiyMomFW0A6%2B7T%2F%2FvcqZUK8yAxUYP%2BtVeuu3eQMJXVEbfEG%2FobF48L4fWHxRlmF%2BfIQoTmcUSsAQsyo6VLpXdraEj2G2Z4r1mZvcKhqQy%2Fw%2BbfjuVU%2BepLCClOTLcdK5NZcEOyEzvl&X-Amz-Signature=a140be84bbfb6105cf863a82446577b5acb5512ca90a0d44cd62fc098c98aff3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664D7BLZPZ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJHMEUCIQD8ihlU3N7OdFmX%2BK20uLUiQmpn67b9naj6kuKHadXybwIgNgbmwbXwNQyQmAjn%2FrS33FKpH3x99EL2A0hkPw2%2Fdw0q%2FwMIRxAAGgw2Mzc0MjMxODM4MDUiDJX7Q8KH0L%2BC%2B%2FBQ6CrcA7CfWRoHEE1Cei5slVS%2F5X9BrObvMzPOnrXgjfx%2Bn4pxTTQEcbacT9RvUIzxvgQRNO%2F2yV0%2BFr3vKRrk8Uek6yZ3FqUZ7EaHlOXZYg%2BSGikUW4nbqB8ikXlG%2B%2FLCe9xniExq%2BRZ2DCF7n4Fu5PanH84qJ8MetNE%2BIZfO0yXv8OZ8EGNMjjW%2FQjjgS%2Bm60FQF%2BoXGw8FlHyqdlU7nWZBifjG5Q1z2AXcSlFE3dxpffLrV%2F7zdju9yxRvjF5z%2B%2F1trOdDhsAA4zl3zVPyHjvqHHnapEsphNmLfgAAPdQhgnWemNCbKQGgUfaSvj826U9MN0eA22LOMoru67k%2B4QsmVWlEq1HH9Z%2FcyxObolvc%2BXmoT0vE1jrJ6Nq4lmTmQkaWIUv6q5KDfkMbnvExI2Okdyly5ZcVr9%2BSiFiTgDHglHBLuaH8O3PtR8NhwamgFTXGhokFK8zSdDn5%2FbVOg7Z2IDxFKhRvploIykREjEeb6Y%2BBSyINxsJcbR8y3J%2FHbqaSuX%2B7lUpUyEK7jbxh0XclAEpundRwa200AY2%2F8o%2FosQ8X2Q0C7j%2FcGMTcto7Y5S%2F%2FkuItJTZcCS%2BFZV5Z8j4pwaoXTca4ZtvRRXQblwGZXWFuTxaIjUCLE7giD%2Fhw9MK3kjb0GOqUBp1M%2FTPqkaDByhoM57vhSAUP7JOGGzayK7Oml0RYHnhpvRp6AHHlVyhqbPh8Xl1knnFrWDtQh5c%2B4u77cJLqnmxItGw6%2BSJ5tCGj0otawvBVcKZnFXfKuf2zkjNTX1wwQEjrYGZqsOzeV4AWZEksONEErTxEFaGWk5a3jIMVcXM33%2BxcyxKzz6JjNgxAjfmByyVTyEYg%2FOOkBgTLCxIrG7Z5RtguF&X-Amz-Signature=977bf01f57109953cb30e5d464f498821e72af3ff5da22dd00e77015d712fe5f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YEGG3U2J%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJIMEYCIQCj9Dm4v%2BPkGayX4vW0VnqKXNmFvxwykCrFwD3yBwX2vgIhAI0xjFez9mBDCJFC5QLGwjwYkaeJzAFrRnTA3yj50jgKKv8DCEcQABoMNjM3NDIzMTgzODA1IgyQFU1cU%2F4OQPp4YDcq3AMVRCzM8YpqG9%2B8qMNyjgpUPzBHk0oxDt4koSmrODR2oN5bthsPTeBu9sfNkQEeVnzWKEtZ7CAPjqs5mt1h4tQE3M%2Fi9sKcTxmXC1vDZK9M0r0G%2FUaw8r1R1dL3dZeHSfsi1rT8DqYkfO07F9IRWLgsxX29%2F%2B61xRCu6D02%2Bc2Pw67FsmtZclG8IKkTK2eUVUAWl91glXhiQBVjRMD%2BhcwowDxWD%2BX7djfPGmK5o9OT2oGHLr9QfbQ%2F1deH8dtwfp%2FbhT1wzzVR6GqYreWpKrLoD6M182q%2FIu9ZqAarTNs%2BYwGtt7rsq234neJlSSbj8%2FEpqPSagDHilv6%2BBk0C9nLw5QmSyecQei16k1EE6n9QBlOIc7YdYkprPeYcHtk06uPfRCXTqJ5AkqR5UxhBA02ZT4xuF1HGs1qQfMVnyfEXg2osPgE6BLXthy3V9zcTSFgODqdbWa%2B6XO6otVBoJP5G31kUgsDfTssWkm55KUNKhJ%2BExNv912%2FZtyfEOw%2B8tniHnvSkHWrhEXJgi8Lqnx7r3RFJFuO9BUV2IqCppKk3eFhkdPeeaECMA2E8bM4rzQEQVhjPTkiWxWKmHog2uL9Sy5tqSdckNs2CZAxDqFNRstehaqchZQjyCFQNrzD54429BjqkAeYAjH1C2OGgA%2BXHdvqLJAmKRcirR5UBw2Z4%2B%2Bc%2Bw7W1cnmJO%2FcPJuWut928vcmFvHZgXOlgCUXZAI6v8oozJsjM1t4HM3yELVjQC6pZsdDDIXYfpwK0xs%2BLIEE5ufJjRRqID%2B001uu8%2BwuShtQs6MYqNlFud4ihV499%2B4etkvnV7Umj9KERxLCWFKnaDA8jg4YfOcGp3JYpUeQh8pylXgrmlldz&X-Amz-Signature=135c1941a23d431f797233c3b73da9889c5a5e6efd72d75599acdfad2a7bbdab&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YEGG3U2J%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJIMEYCIQCj9Dm4v%2BPkGayX4vW0VnqKXNmFvxwykCrFwD3yBwX2vgIhAI0xjFez9mBDCJFC5QLGwjwYkaeJzAFrRnTA3yj50jgKKv8DCEcQABoMNjM3NDIzMTgzODA1IgyQFU1cU%2F4OQPp4YDcq3AMVRCzM8YpqG9%2B8qMNyjgpUPzBHk0oxDt4koSmrODR2oN5bthsPTeBu9sfNkQEeVnzWKEtZ7CAPjqs5mt1h4tQE3M%2Fi9sKcTxmXC1vDZK9M0r0G%2FUaw8r1R1dL3dZeHSfsi1rT8DqYkfO07F9IRWLgsxX29%2F%2B61xRCu6D02%2Bc2Pw67FsmtZclG8IKkTK2eUVUAWl91glXhiQBVjRMD%2BhcwowDxWD%2BX7djfPGmK5o9OT2oGHLr9QfbQ%2F1deH8dtwfp%2FbhT1wzzVR6GqYreWpKrLoD6M182q%2FIu9ZqAarTNs%2BYwGtt7rsq234neJlSSbj8%2FEpqPSagDHilv6%2BBk0C9nLw5QmSyecQei16k1EE6n9QBlOIc7YdYkprPeYcHtk06uPfRCXTqJ5AkqR5UxhBA02ZT4xuF1HGs1qQfMVnyfEXg2osPgE6BLXthy3V9zcTSFgODqdbWa%2B6XO6otVBoJP5G31kUgsDfTssWkm55KUNKhJ%2BExNv912%2FZtyfEOw%2B8tniHnvSkHWrhEXJgi8Lqnx7r3RFJFuO9BUV2IqCppKk3eFhkdPeeaECMA2E8bM4rzQEQVhjPTkiWxWKmHog2uL9Sy5tqSdckNs2CZAxDqFNRstehaqchZQjyCFQNrzD54429BjqkAeYAjH1C2OGgA%2BXHdvqLJAmKRcirR5UBw2Z4%2B%2Bc%2Bw7W1cnmJO%2FcPJuWut928vcmFvHZgXOlgCUXZAI6v8oozJsjM1t4HM3yELVjQC6pZsdDDIXYfpwK0xs%2BLIEE5ufJjRRqID%2B001uu8%2BwuShtQs6MYqNlFud4ihV499%2B4etkvnV7Umj9KERxLCWFKnaDA8jg4YfOcGp3JYpUeQh8pylXgrmlldz&X-Amz-Signature=5415f5708026883073354259a7910b251cf54ffb4a72b9122572d57ef501d8de&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YEGG3U2J%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJIMEYCIQCj9Dm4v%2BPkGayX4vW0VnqKXNmFvxwykCrFwD3yBwX2vgIhAI0xjFez9mBDCJFC5QLGwjwYkaeJzAFrRnTA3yj50jgKKv8DCEcQABoMNjM3NDIzMTgzODA1IgyQFU1cU%2F4OQPp4YDcq3AMVRCzM8YpqG9%2B8qMNyjgpUPzBHk0oxDt4koSmrODR2oN5bthsPTeBu9sfNkQEeVnzWKEtZ7CAPjqs5mt1h4tQE3M%2Fi9sKcTxmXC1vDZK9M0r0G%2FUaw8r1R1dL3dZeHSfsi1rT8DqYkfO07F9IRWLgsxX29%2F%2B61xRCu6D02%2Bc2Pw67FsmtZclG8IKkTK2eUVUAWl91glXhiQBVjRMD%2BhcwowDxWD%2BX7djfPGmK5o9OT2oGHLr9QfbQ%2F1deH8dtwfp%2FbhT1wzzVR6GqYreWpKrLoD6M182q%2FIu9ZqAarTNs%2BYwGtt7rsq234neJlSSbj8%2FEpqPSagDHilv6%2BBk0C9nLw5QmSyecQei16k1EE6n9QBlOIc7YdYkprPeYcHtk06uPfRCXTqJ5AkqR5UxhBA02ZT4xuF1HGs1qQfMVnyfEXg2osPgE6BLXthy3V9zcTSFgODqdbWa%2B6XO6otVBoJP5G31kUgsDfTssWkm55KUNKhJ%2BExNv912%2FZtyfEOw%2B8tniHnvSkHWrhEXJgi8Lqnx7r3RFJFuO9BUV2IqCppKk3eFhkdPeeaECMA2E8bM4rzQEQVhjPTkiWxWKmHog2uL9Sy5tqSdckNs2CZAxDqFNRstehaqchZQjyCFQNrzD54429BjqkAeYAjH1C2OGgA%2BXHdvqLJAmKRcirR5UBw2Z4%2B%2Bc%2Bw7W1cnmJO%2FcPJuWut928vcmFvHZgXOlgCUXZAI6v8oozJsjM1t4HM3yELVjQC6pZsdDDIXYfpwK0xs%2BLIEE5ufJjRRqID%2B001uu8%2BwuShtQs6MYqNlFud4ihV499%2B4etkvnV7Umj9KERxLCWFKnaDA8jg4YfOcGp3JYpUeQh8pylXgrmlldz&X-Amz-Signature=9b496a281fce8ecb61720a80146de276220876cc1c98d5d44a9bbf0a95eae5d8&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YEGG3U2J%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJIMEYCIQCj9Dm4v%2BPkGayX4vW0VnqKXNmFvxwykCrFwD3yBwX2vgIhAI0xjFez9mBDCJFC5QLGwjwYkaeJzAFrRnTA3yj50jgKKv8DCEcQABoMNjM3NDIzMTgzODA1IgyQFU1cU%2F4OQPp4YDcq3AMVRCzM8YpqG9%2B8qMNyjgpUPzBHk0oxDt4koSmrODR2oN5bthsPTeBu9sfNkQEeVnzWKEtZ7CAPjqs5mt1h4tQE3M%2Fi9sKcTxmXC1vDZK9M0r0G%2FUaw8r1R1dL3dZeHSfsi1rT8DqYkfO07F9IRWLgsxX29%2F%2B61xRCu6D02%2Bc2Pw67FsmtZclG8IKkTK2eUVUAWl91glXhiQBVjRMD%2BhcwowDxWD%2BX7djfPGmK5o9OT2oGHLr9QfbQ%2F1deH8dtwfp%2FbhT1wzzVR6GqYreWpKrLoD6M182q%2FIu9ZqAarTNs%2BYwGtt7rsq234neJlSSbj8%2FEpqPSagDHilv6%2BBk0C9nLw5QmSyecQei16k1EE6n9QBlOIc7YdYkprPeYcHtk06uPfRCXTqJ5AkqR5UxhBA02ZT4xuF1HGs1qQfMVnyfEXg2osPgE6BLXthy3V9zcTSFgODqdbWa%2B6XO6otVBoJP5G31kUgsDfTssWkm55KUNKhJ%2BExNv912%2FZtyfEOw%2B8tniHnvSkHWrhEXJgi8Lqnx7r3RFJFuO9BUV2IqCppKk3eFhkdPeeaECMA2E8bM4rzQEQVhjPTkiWxWKmHog2uL9Sy5tqSdckNs2CZAxDqFNRstehaqchZQjyCFQNrzD54429BjqkAeYAjH1C2OGgA%2BXHdvqLJAmKRcirR5UBw2Z4%2B%2Bc%2Bw7W1cnmJO%2FcPJuWut928vcmFvHZgXOlgCUXZAI6v8oozJsjM1t4HM3yELVjQC6pZsdDDIXYfpwK0xs%2BLIEE5ufJjRRqID%2B001uu8%2BwuShtQs6MYqNlFud4ihV499%2B4etkvnV7Umj9KERxLCWFKnaDA8jg4YfOcGp3JYpUeQh8pylXgrmlldz&X-Amz-Signature=559b597be8958b1ec3a9844343cb40d563ecaa8585992107ac5e3925ff8a97ca&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
