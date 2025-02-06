

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZI4HGRAI%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062120Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIQCfTQZa9osattQsAQNAX9pz%2BR7OjGQvX52ciZ2NXzvO6gIgTrOaYtfc%2BWffpXflrWXuo1mDTdEwfzHAH6iLQj2ETbUq%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDJz8TSD8AMI3yS2syCrcA3ncCJ7ri7uibYYSIGxDQBbbpR1Inj8Sjd8jo2nQx7iD%2FE9yLJCA76JTBIcpp8gC3n0yiKr5O0fjTHnuLQ2HjILpB2z0X2YGGtePv8JTGdLSyHnVMBOACloiMqZAyPgvH7%2Bk9Gls5ysNoUOwAfexXg37Y8TUxv2EcriGngbI4gWSCu7IrAETfoHtKTC2BUNbN0R1la6GQT91Zjz%2Bl%2ByVogKlxAFQEhMSTslwlEdxdZQzWmIWe1CIm8JSpLy90H%2FuviL90EuLFo9Jqj%2BAOlFlNie3SsopIdBZvqVjZFFgd%2BVtIegLfq85kkzjB4iFpTNUupc3j0XndRfRZcHGKUcX5b4rAl3%2BdThcHCT3a2c7jalcegmsupG4TJ%2FsjcbSQcqRG2VcwmrCxVxMhqwWzzx2dkO95Ez7SyNabi8bSaWMlym40kZaY%2FUd2zQy4Mb8pRDfqYJ90sVMEMed3P4Y6Mmpm%2BBebXgrpdEU5Gu89%2FtnVXG8RZjFbK%2FGBr5nKWhUU%2Fd06J9YXZ3MLJVF83rwqLktwpbPswntU7h6RLN2%2BLHxyH5NYFnUurXkS9ybMG7KZ0HOGE8l6R2kUOYj6yrjOjbWNd%2B08%2FNBfW%2B2iCEjinH6KGYtg3eYZWy3WiI8dRsiMLKZkb0GOqUBYqg%2FmArGOzk0QS%2FDxygyLZwZB%2BMkybSGVI%2BSSO4Ew0zy%2BQ5WirE8DuQt1LFtfQlupjKhwKwWEufAj5f0bLQkzP5T%2Bil7v%2FNsKn5loRZ%2BMK60HspIs3nJOpdYbZq7%2BqbKZiZmpG7Vx6VaPzVtqD0dyEdK8jwV3XZkrLV%2FN%2FLuUOdpgSi%2BJITWuYHdycMRkfx2j3HpnqaMF5IAPWiCYnkfc8xWSnLm&X-Amz-Signature=ba6af66195b1b8d210b47abe475826aa2816c957391a0b8b77d0aa760d2676a0&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZI4HGRAI%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062120Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIQCfTQZa9osattQsAQNAX9pz%2BR7OjGQvX52ciZ2NXzvO6gIgTrOaYtfc%2BWffpXflrWXuo1mDTdEwfzHAH6iLQj2ETbUq%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDJz8TSD8AMI3yS2syCrcA3ncCJ7ri7uibYYSIGxDQBbbpR1Inj8Sjd8jo2nQx7iD%2FE9yLJCA76JTBIcpp8gC3n0yiKr5O0fjTHnuLQ2HjILpB2z0X2YGGtePv8JTGdLSyHnVMBOACloiMqZAyPgvH7%2Bk9Gls5ysNoUOwAfexXg37Y8TUxv2EcriGngbI4gWSCu7IrAETfoHtKTC2BUNbN0R1la6GQT91Zjz%2Bl%2ByVogKlxAFQEhMSTslwlEdxdZQzWmIWe1CIm8JSpLy90H%2FuviL90EuLFo9Jqj%2BAOlFlNie3SsopIdBZvqVjZFFgd%2BVtIegLfq85kkzjB4iFpTNUupc3j0XndRfRZcHGKUcX5b4rAl3%2BdThcHCT3a2c7jalcegmsupG4TJ%2FsjcbSQcqRG2VcwmrCxVxMhqwWzzx2dkO95Ez7SyNabi8bSaWMlym40kZaY%2FUd2zQy4Mb8pRDfqYJ90sVMEMed3P4Y6Mmpm%2BBebXgrpdEU5Gu89%2FtnVXG8RZjFbK%2FGBr5nKWhUU%2Fd06J9YXZ3MLJVF83rwqLktwpbPswntU7h6RLN2%2BLHxyH5NYFnUurXkS9ybMG7KZ0HOGE8l6R2kUOYj6yrjOjbWNd%2B08%2FNBfW%2B2iCEjinH6KGYtg3eYZWy3WiI8dRsiMLKZkb0GOqUBYqg%2FmArGOzk0QS%2FDxygyLZwZB%2BMkybSGVI%2BSSO4Ew0zy%2BQ5WirE8DuQt1LFtfQlupjKhwKwWEufAj5f0bLQkzP5T%2Bil7v%2FNsKn5loRZ%2BMK60HspIs3nJOpdYbZq7%2BqbKZiZmpG7Vx6VaPzVtqD0dyEdK8jwV3XZkrLV%2FN%2FLuUOdpgSi%2BJITWuYHdycMRkfx2j3HpnqaMF5IAPWiCYnkfc8xWSnLm&X-Amz-Signature=887fbe5bb123c9c73845f364f4e0576a826a216ba5a6abd068115053dfd21810&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZI4HGRAI%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062120Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIQCfTQZa9osattQsAQNAX9pz%2BR7OjGQvX52ciZ2NXzvO6gIgTrOaYtfc%2BWffpXflrWXuo1mDTdEwfzHAH6iLQj2ETbUq%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDJz8TSD8AMI3yS2syCrcA3ncCJ7ri7uibYYSIGxDQBbbpR1Inj8Sjd8jo2nQx7iD%2FE9yLJCA76JTBIcpp8gC3n0yiKr5O0fjTHnuLQ2HjILpB2z0X2YGGtePv8JTGdLSyHnVMBOACloiMqZAyPgvH7%2Bk9Gls5ysNoUOwAfexXg37Y8TUxv2EcriGngbI4gWSCu7IrAETfoHtKTC2BUNbN0R1la6GQT91Zjz%2Bl%2ByVogKlxAFQEhMSTslwlEdxdZQzWmIWe1CIm8JSpLy90H%2FuviL90EuLFo9Jqj%2BAOlFlNie3SsopIdBZvqVjZFFgd%2BVtIegLfq85kkzjB4iFpTNUupc3j0XndRfRZcHGKUcX5b4rAl3%2BdThcHCT3a2c7jalcegmsupG4TJ%2FsjcbSQcqRG2VcwmrCxVxMhqwWzzx2dkO95Ez7SyNabi8bSaWMlym40kZaY%2FUd2zQy4Mb8pRDfqYJ90sVMEMed3P4Y6Mmpm%2BBebXgrpdEU5Gu89%2FtnVXG8RZjFbK%2FGBr5nKWhUU%2Fd06J9YXZ3MLJVF83rwqLktwpbPswntU7h6RLN2%2BLHxyH5NYFnUurXkS9ybMG7KZ0HOGE8l6R2kUOYj6yrjOjbWNd%2B08%2FNBfW%2B2iCEjinH6KGYtg3eYZWy3WiI8dRsiMLKZkb0GOqUBYqg%2FmArGOzk0QS%2FDxygyLZwZB%2BMkybSGVI%2BSSO4Ew0zy%2BQ5WirE8DuQt1LFtfQlupjKhwKwWEufAj5f0bLQkzP5T%2Bil7v%2FNsKn5loRZ%2BMK60HspIs3nJOpdYbZq7%2BqbKZiZmpG7Vx6VaPzVtqD0dyEdK8jwV3XZkrLV%2FN%2FLuUOdpgSi%2BJITWuYHdycMRkfx2j3HpnqaMF5IAPWiCYnkfc8xWSnLm&X-Amz-Signature=ad2f8bec3326a69708f2929b58fd13a6f8d0ae2cf0e30c989ecddf55b7657625&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ZPD36QJ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062120Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIDMTtoJ94vU92%2Bgsb967xQuBBIXtvIDfHj8hr1h1hDXJAiEA3mu0dLsWV6FF9UiniuDuoeESGDbtDemx07zSC0XhY1kq%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDGEcc4UCqaNfWKejdircA2txy6UN9Jk0pxlp8POBL2XafYSC6J1pRz3lMzwdKv2ln7oU3a3Gi6f%2BtihsxmsESzNTOvK3vJr9W%2B5CgKVOiT8mUgZfeRJCgy9kaGa1rIpp21l4gB6USPCq9CLWoIoxC4sVoyYhJBAW1mXfilfXAnABFoLIHBYg1BoBfjxzyQJemuprO3Rk6kslM9YbnFPNniHMRqDSFzC0MIzceE%2BIhIeTwzKngB4TeaaxxY8CN5zpOQvZe9H%2Bca%2F3GKCBirN%2BrvJtRXsrXKdumxHUD5ML5LInBEqyFj3V0%2BFf9PBqIi36uLAhuCzEBLozmobcZdabtrOxq1tXcsOACrlx9ry6MgdQwTH0U6C4rEfSJEMmdRcwWe1MK5N5Ea9%2FMskaaIKufbD4ZfAB9xN4CBYJOx4YYMNu5pVCjAeUCw%2BTQMvFxtxxYbHDsRdwNhyZOTcBvLmzNtr7py%2BU%2B54Ni6cV03EwXpbidJeKedgQSWuYsO2RdPIUjCT%2BjSsZZ%2FUjxFPEJLLQN8iFdBDExqjP04llyO5zLH2RZiKZjneWtNB8oJdLsvxkunx1JXnuYr%2Fu6F4ZgcZHH3amzaQRbbTi7ttUlrlNc4HT62Nml5FnMtQJ5dLevEmsG3kUSqh0CbHGTggJMLKZkb0GOqUBOzPrdKZFaVgWbWHfoF3AUrCGn89QehBpIq%2BzBonxFxCm7VcVPEKlW6ocfXYgJBrubS3J5eyeaHP%2FN5BIHLF9nA4ySjQrw2AJzx0qu%2BpbHhI3dkaSdvZ3ydsLEUFTYT5rO7uFV53XeQHFvR9kHigYob2VnOvGeVyRIbyETyAbN5ZRdRuUPwtIja8aTTK5PuivMHOko%2BBsuF1Uemi2BQV%2FIM3amN%2FP&X-Amz-Signature=7e81c0e28866165c5107a99fc5e3afd372c942050f4acd896691af307aa435fa&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNP26UQN%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062125Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIAf5MsLKIzLC3xKLFYTGRwnbzu%2FpQYTBsEcW0LKQAO%2FnAiEA3aGP6JbuZgYbxploFK509IzsY009nsCb3pSD7BFJXC0q%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDMXBZ%2FzSAZDmlemKjSrcAyU3x1vlcUdhFcY2tDxGFg1kojlc9jeIb36CTenQD8cWQ874D4yWH8Ajo2L%2FRd8K3W2v3GVPwRkBAOmxLmB3wFOy7xGNk8gYWMUG3c9etCLVF8E7%2BkRs5jtdYl7oFkHYrUkVIw9PkuzQKPDATHOBnwG%2BAnlJxEQRTsHtY%2F6wHIQ5xKxriDnqFgSOPPxz%2BeT21SNRTX4UdMtvFQoPtx0IP73kdHvdKCv8spAnXgR4U855gvRmPYoEZ5OQLKei6Uhg%2FmpnbEDzStqI3p%2BviSMO9lVapMgnLsfIStF%2BfBmh9c9ksSytc%2BFzKP1nW2lt5Sdu6%2F2PNFz6doxtPMOsfHbSpPfiDadd%2BlGYWtpTeoqlK6SEgM%2FFMWmeB6JvL4tVkEjXab0s2Cqc20NzajlfCUSIGSYjcul8yz4NwaybxhwdIynF1Ed02nmkBymjVu5JFwQI9QvbwRS7vn8WAOW0tleeEssj8ebNO67g8BV4h1nS%2F7Ka7dSmx7mC7Pm3dFecZy9RFltL6YqzLRTKHFYqTEDrZJ7j0i%2BY7oMOriC6Z7tKIRJnyjM8fge4CqFfaiZDJ801PiPX8oXW%2FazUL7b%2Bt8eTgAKLJx6L5PK3FXvNBNhRoUJw1CQO%2FIbfKDlacUC1MMKZkb0GOqUByu%2BM96dwEjeAq5n6NLMrjM8rYCO6fVrO1XheahWVqE61EDFWftgrOv8EZ86KoksEpljRwqa2K1RSIDhhPQPQ9aK7m3Z5uSy0jM4QbdU07k6EFAfk%2FwqhmGQLnrrrqOi22Ng%2BqbM781bqNkcI%2B%2FDVbbHYFmg07LNchUL54eLLeW%2FYTrGYUJCtvnQtcPKhvmBNGsDm9nLgHMCO1qhROUPOT5r9rzaO&X-Amz-Signature=7ae81979920631d2e075202a63f142e7efca4415c2411f50fc521878b7a92384&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZI4HGRAI%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062120Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIQCfTQZa9osattQsAQNAX9pz%2BR7OjGQvX52ciZ2NXzvO6gIgTrOaYtfc%2BWffpXflrWXuo1mDTdEwfzHAH6iLQj2ETbUq%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDJz8TSD8AMI3yS2syCrcA3ncCJ7ri7uibYYSIGxDQBbbpR1Inj8Sjd8jo2nQx7iD%2FE9yLJCA76JTBIcpp8gC3n0yiKr5O0fjTHnuLQ2HjILpB2z0X2YGGtePv8JTGdLSyHnVMBOACloiMqZAyPgvH7%2Bk9Gls5ysNoUOwAfexXg37Y8TUxv2EcriGngbI4gWSCu7IrAETfoHtKTC2BUNbN0R1la6GQT91Zjz%2Bl%2ByVogKlxAFQEhMSTslwlEdxdZQzWmIWe1CIm8JSpLy90H%2FuviL90EuLFo9Jqj%2BAOlFlNie3SsopIdBZvqVjZFFgd%2BVtIegLfq85kkzjB4iFpTNUupc3j0XndRfRZcHGKUcX5b4rAl3%2BdThcHCT3a2c7jalcegmsupG4TJ%2FsjcbSQcqRG2VcwmrCxVxMhqwWzzx2dkO95Ez7SyNabi8bSaWMlym40kZaY%2FUd2zQy4Mb8pRDfqYJ90sVMEMed3P4Y6Mmpm%2BBebXgrpdEU5Gu89%2FtnVXG8RZjFbK%2FGBr5nKWhUU%2Fd06J9YXZ3MLJVF83rwqLktwpbPswntU7h6RLN2%2BLHxyH5NYFnUurXkS9ybMG7KZ0HOGE8l6R2kUOYj6yrjOjbWNd%2B08%2FNBfW%2B2iCEjinH6KGYtg3eYZWy3WiI8dRsiMLKZkb0GOqUBYqg%2FmArGOzk0QS%2FDxygyLZwZB%2BMkybSGVI%2BSSO4Ew0zy%2BQ5WirE8DuQt1LFtfQlupjKhwKwWEufAj5f0bLQkzP5T%2Bil7v%2FNsKn5loRZ%2BMK60HspIs3nJOpdYbZq7%2BqbKZiZmpG7Vx6VaPzVtqD0dyEdK8jwV3XZkrLV%2FN%2FLuUOdpgSi%2BJITWuYHdycMRkfx2j3HpnqaMF5IAPWiCYnkfc8xWSnLm&X-Amz-Signature=034450ba5d457733c2cef8074f68dcb315687f915c8093c51deaece742c3decc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZI4HGRAI%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062120Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIQCfTQZa9osattQsAQNAX9pz%2BR7OjGQvX52ciZ2NXzvO6gIgTrOaYtfc%2BWffpXflrWXuo1mDTdEwfzHAH6iLQj2ETbUq%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDJz8TSD8AMI3yS2syCrcA3ncCJ7ri7uibYYSIGxDQBbbpR1Inj8Sjd8jo2nQx7iD%2FE9yLJCA76JTBIcpp8gC3n0yiKr5O0fjTHnuLQ2HjILpB2z0X2YGGtePv8JTGdLSyHnVMBOACloiMqZAyPgvH7%2Bk9Gls5ysNoUOwAfexXg37Y8TUxv2EcriGngbI4gWSCu7IrAETfoHtKTC2BUNbN0R1la6GQT91Zjz%2Bl%2ByVogKlxAFQEhMSTslwlEdxdZQzWmIWe1CIm8JSpLy90H%2FuviL90EuLFo9Jqj%2BAOlFlNie3SsopIdBZvqVjZFFgd%2BVtIegLfq85kkzjB4iFpTNUupc3j0XndRfRZcHGKUcX5b4rAl3%2BdThcHCT3a2c7jalcegmsupG4TJ%2FsjcbSQcqRG2VcwmrCxVxMhqwWzzx2dkO95Ez7SyNabi8bSaWMlym40kZaY%2FUd2zQy4Mb8pRDfqYJ90sVMEMed3P4Y6Mmpm%2BBebXgrpdEU5Gu89%2FtnVXG8RZjFbK%2FGBr5nKWhUU%2Fd06J9YXZ3MLJVF83rwqLktwpbPswntU7h6RLN2%2BLHxyH5NYFnUurXkS9ybMG7KZ0HOGE8l6R2kUOYj6yrjOjbWNd%2B08%2FNBfW%2B2iCEjinH6KGYtg3eYZWy3WiI8dRsiMLKZkb0GOqUBYqg%2FmArGOzk0QS%2FDxygyLZwZB%2BMkybSGVI%2BSSO4Ew0zy%2BQ5WirE8DuQt1LFtfQlupjKhwKwWEufAj5f0bLQkzP5T%2Bil7v%2FNsKn5loRZ%2BMK60HspIs3nJOpdYbZq7%2BqbKZiZmpG7Vx6VaPzVtqD0dyEdK8jwV3XZkrLV%2FN%2FLuUOdpgSi%2BJITWuYHdycMRkfx2j3HpnqaMF5IAPWiCYnkfc8xWSnLm&X-Amz-Signature=7a56c55da0f8fb18f7f8ca07d531804b3ace9ddd1229bbbeda5f6c961295213d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZI4HGRAI%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062120Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIQCfTQZa9osattQsAQNAX9pz%2BR7OjGQvX52ciZ2NXzvO6gIgTrOaYtfc%2BWffpXflrWXuo1mDTdEwfzHAH6iLQj2ETbUq%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDJz8TSD8AMI3yS2syCrcA3ncCJ7ri7uibYYSIGxDQBbbpR1Inj8Sjd8jo2nQx7iD%2FE9yLJCA76JTBIcpp8gC3n0yiKr5O0fjTHnuLQ2HjILpB2z0X2YGGtePv8JTGdLSyHnVMBOACloiMqZAyPgvH7%2Bk9Gls5ysNoUOwAfexXg37Y8TUxv2EcriGngbI4gWSCu7IrAETfoHtKTC2BUNbN0R1la6GQT91Zjz%2Bl%2ByVogKlxAFQEhMSTslwlEdxdZQzWmIWe1CIm8JSpLy90H%2FuviL90EuLFo9Jqj%2BAOlFlNie3SsopIdBZvqVjZFFgd%2BVtIegLfq85kkzjB4iFpTNUupc3j0XndRfRZcHGKUcX5b4rAl3%2BdThcHCT3a2c7jalcegmsupG4TJ%2FsjcbSQcqRG2VcwmrCxVxMhqwWzzx2dkO95Ez7SyNabi8bSaWMlym40kZaY%2FUd2zQy4Mb8pRDfqYJ90sVMEMed3P4Y6Mmpm%2BBebXgrpdEU5Gu89%2FtnVXG8RZjFbK%2FGBr5nKWhUU%2Fd06J9YXZ3MLJVF83rwqLktwpbPswntU7h6RLN2%2BLHxyH5NYFnUurXkS9ybMG7KZ0HOGE8l6R2kUOYj6yrjOjbWNd%2B08%2FNBfW%2B2iCEjinH6KGYtg3eYZWy3WiI8dRsiMLKZkb0GOqUBYqg%2FmArGOzk0QS%2FDxygyLZwZB%2BMkybSGVI%2BSSO4Ew0zy%2BQ5WirE8DuQt1LFtfQlupjKhwKwWEufAj5f0bLQkzP5T%2Bil7v%2FNsKn5loRZ%2BMK60HspIs3nJOpdYbZq7%2BqbKZiZmpG7Vx6VaPzVtqD0dyEdK8jwV3XZkrLV%2FN%2FLuUOdpgSi%2BJITWuYHdycMRkfx2j3HpnqaMF5IAPWiCYnkfc8xWSnLm&X-Amz-Signature=dcff3a1b2a9ec3e59e56122a55db3f1f131dac5249cb852802fdcdebef1f1ee9&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZI4HGRAI%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062120Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIQCfTQZa9osattQsAQNAX9pz%2BR7OjGQvX52ciZ2NXzvO6gIgTrOaYtfc%2BWffpXflrWXuo1mDTdEwfzHAH6iLQj2ETbUq%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDJz8TSD8AMI3yS2syCrcA3ncCJ7ri7uibYYSIGxDQBbbpR1Inj8Sjd8jo2nQx7iD%2FE9yLJCA76JTBIcpp8gC3n0yiKr5O0fjTHnuLQ2HjILpB2z0X2YGGtePv8JTGdLSyHnVMBOACloiMqZAyPgvH7%2Bk9Gls5ysNoUOwAfexXg37Y8TUxv2EcriGngbI4gWSCu7IrAETfoHtKTC2BUNbN0R1la6GQT91Zjz%2Bl%2ByVogKlxAFQEhMSTslwlEdxdZQzWmIWe1CIm8JSpLy90H%2FuviL90EuLFo9Jqj%2BAOlFlNie3SsopIdBZvqVjZFFgd%2BVtIegLfq85kkzjB4iFpTNUupc3j0XndRfRZcHGKUcX5b4rAl3%2BdThcHCT3a2c7jalcegmsupG4TJ%2FsjcbSQcqRG2VcwmrCxVxMhqwWzzx2dkO95Ez7SyNabi8bSaWMlym40kZaY%2FUd2zQy4Mb8pRDfqYJ90sVMEMed3P4Y6Mmpm%2BBebXgrpdEU5Gu89%2FtnVXG8RZjFbK%2FGBr5nKWhUU%2Fd06J9YXZ3MLJVF83rwqLktwpbPswntU7h6RLN2%2BLHxyH5NYFnUurXkS9ybMG7KZ0HOGE8l6R2kUOYj6yrjOjbWNd%2B08%2FNBfW%2B2iCEjinH6KGYtg3eYZWy3WiI8dRsiMLKZkb0GOqUBYqg%2FmArGOzk0QS%2FDxygyLZwZB%2BMkybSGVI%2BSSO4Ew0zy%2BQ5WirE8DuQt1LFtfQlupjKhwKwWEufAj5f0bLQkzP5T%2Bil7v%2FNsKn5loRZ%2BMK60HspIs3nJOpdYbZq7%2BqbKZiZmpG7Vx6VaPzVtqD0dyEdK8jwV3XZkrLV%2FN%2FLuUOdpgSi%2BJITWuYHdycMRkfx2j3HpnqaMF5IAPWiCYnkfc8xWSnLm&X-Amz-Signature=4610359275831e4734c8b2149f9a2f384a394174634b9d601c70c9a8b6a84667&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
