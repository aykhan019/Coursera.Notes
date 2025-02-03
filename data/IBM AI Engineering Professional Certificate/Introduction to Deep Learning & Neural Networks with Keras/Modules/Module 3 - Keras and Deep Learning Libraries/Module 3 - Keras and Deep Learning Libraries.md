

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QT43YKGR%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T171256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJGMEQCIAkM5LJkRznVbwjpY%2BTttSup01hh98hTyzkKk%2F9CKoUXAiBcAp8zCj0qKZvYYZr0W90vL23FrsNotlTgvmtm27SA3ir%2FAwgaEAAaDDYzNzQyMzE4MzgwNSIMwgam%2Fh1eVrF8WBMyKtwDTG0BbrKBxaPR5hCL7pbbDCj4T1PsRATMPAXdvNjU6Y0yUybbtnIZvRTQrO9J6U7paEfJvL0Lr%2Frifk8xH1aaLGgwsKMWrzFIrBsteryXfgcrr3aeqsr7Qr%2FYAv3fGuKF5gQrfFmKTmxK9Dz6ZuexZHeI%2B960zyrgP928iXGU5C13%2FrBv3LCxh9OIuoYbaOsafPbXVYF8O%2FhJ7FDQdAy4SvNeWskQIwoVcBxuK8VSm8LyNkYZ42EhlC1pq7CGh1kUVlR8eDyZq6xuV2tYR3jbkr%2BDYAXctxX%2BwNfCSPUbt6tOxqnUefFTSY2%2Fm0tI9EcmQenDW5w%2BWKrgB6IzCQyfBV6PtSLGHa%2BpY9lIiewwum0j5%2BsM1TkHMqX8kltZxED2AlZURx4qhIvG1wNhdEvllFjcfObiF3lYGTI29dmeTXWyJcHjJS1gdWbU5rFJxj6owYS7DN0uRTDsOcyy1%2F%2FkPBrcWbuWuAEKBpif%2Fa2FlEMDHWiAepu9MmMmw%2B5REemIUTbXEnKHyOHcFMQIrZhrTbct8HQFzZTmUd5zRTdC%2FPev9yTaW4Uswy6htygttlpQ6SojByOw8Bo77q5YUF10vyyt4%2BAEFxHyfh%2FLd2SnKXewfyYN193gcxO1GG0wg%2BaDvQY6pgFqAzhMFn8%2BjA57kMKFYGG3jsYh%2FNqcHctLLuQ9dDKnQDPRIn9nLCmyo5dwg5rttSC%2F3Hx668vyC3F9GL%2BT2pf4zJsdCJ6saTAucuAWlLksqYIkppbxqMiod1fPz%2FYo1eu5qrYjJnvRdbFHjTJDiXY9AF7nyDM5ccYKK0eh%2FbNHygh8Dq61jefisPCxL5%2FLgOd2KPTzmp271xIPO3qb%2FpTpFWKIJ7L7&X-Amz-Signature=555761c311399a07f003b68801c29592e67a6ec867af4fc3237219c90c72ce0e&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QT43YKGR%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T171255Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJGMEQCIAkM5LJkRznVbwjpY%2BTttSup01hh98hTyzkKk%2F9CKoUXAiBcAp8zCj0qKZvYYZr0W90vL23FrsNotlTgvmtm27SA3ir%2FAwgaEAAaDDYzNzQyMzE4MzgwNSIMwgam%2Fh1eVrF8WBMyKtwDTG0BbrKBxaPR5hCL7pbbDCj4T1PsRATMPAXdvNjU6Y0yUybbtnIZvRTQrO9J6U7paEfJvL0Lr%2Frifk8xH1aaLGgwsKMWrzFIrBsteryXfgcrr3aeqsr7Qr%2FYAv3fGuKF5gQrfFmKTmxK9Dz6ZuexZHeI%2B960zyrgP928iXGU5C13%2FrBv3LCxh9OIuoYbaOsafPbXVYF8O%2FhJ7FDQdAy4SvNeWskQIwoVcBxuK8VSm8LyNkYZ42EhlC1pq7CGh1kUVlR8eDyZq6xuV2tYR3jbkr%2BDYAXctxX%2BwNfCSPUbt6tOxqnUefFTSY2%2Fm0tI9EcmQenDW5w%2BWKrgB6IzCQyfBV6PtSLGHa%2BpY9lIiewwum0j5%2BsM1TkHMqX8kltZxED2AlZURx4qhIvG1wNhdEvllFjcfObiF3lYGTI29dmeTXWyJcHjJS1gdWbU5rFJxj6owYS7DN0uRTDsOcyy1%2F%2FkPBrcWbuWuAEKBpif%2Fa2FlEMDHWiAepu9MmMmw%2B5REemIUTbXEnKHyOHcFMQIrZhrTbct8HQFzZTmUd5zRTdC%2FPev9yTaW4Uswy6htygttlpQ6SojByOw8Bo77q5YUF10vyyt4%2BAEFxHyfh%2FLd2SnKXewfyYN193gcxO1GG0wg%2BaDvQY6pgFqAzhMFn8%2BjA57kMKFYGG3jsYh%2FNqcHctLLuQ9dDKnQDPRIn9nLCmyo5dwg5rttSC%2F3Hx668vyC3F9GL%2BT2pf4zJsdCJ6saTAucuAWlLksqYIkppbxqMiod1fPz%2FYo1eu5qrYjJnvRdbFHjTJDiXY9AF7nyDM5ccYKK0eh%2FbNHygh8Dq61jefisPCxL5%2FLgOd2KPTzmp271xIPO3qb%2FpTpFWKIJ7L7&X-Amz-Signature=5641cfec22e3dfa50e5e403db3ca3073cf970dd61a561db828eaacfbbb520e45&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QT43YKGR%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T171255Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJGMEQCIAkM5LJkRznVbwjpY%2BTttSup01hh98hTyzkKk%2F9CKoUXAiBcAp8zCj0qKZvYYZr0W90vL23FrsNotlTgvmtm27SA3ir%2FAwgaEAAaDDYzNzQyMzE4MzgwNSIMwgam%2Fh1eVrF8WBMyKtwDTG0BbrKBxaPR5hCL7pbbDCj4T1PsRATMPAXdvNjU6Y0yUybbtnIZvRTQrO9J6U7paEfJvL0Lr%2Frifk8xH1aaLGgwsKMWrzFIrBsteryXfgcrr3aeqsr7Qr%2FYAv3fGuKF5gQrfFmKTmxK9Dz6ZuexZHeI%2B960zyrgP928iXGU5C13%2FrBv3LCxh9OIuoYbaOsafPbXVYF8O%2FhJ7FDQdAy4SvNeWskQIwoVcBxuK8VSm8LyNkYZ42EhlC1pq7CGh1kUVlR8eDyZq6xuV2tYR3jbkr%2BDYAXctxX%2BwNfCSPUbt6tOxqnUefFTSY2%2Fm0tI9EcmQenDW5w%2BWKrgB6IzCQyfBV6PtSLGHa%2BpY9lIiewwum0j5%2BsM1TkHMqX8kltZxED2AlZURx4qhIvG1wNhdEvllFjcfObiF3lYGTI29dmeTXWyJcHjJS1gdWbU5rFJxj6owYS7DN0uRTDsOcyy1%2F%2FkPBrcWbuWuAEKBpif%2Fa2FlEMDHWiAepu9MmMmw%2B5REemIUTbXEnKHyOHcFMQIrZhrTbct8HQFzZTmUd5zRTdC%2FPev9yTaW4Uswy6htygttlpQ6SojByOw8Bo77q5YUF10vyyt4%2BAEFxHyfh%2FLd2SnKXewfyYN193gcxO1GG0wg%2BaDvQY6pgFqAzhMFn8%2BjA57kMKFYGG3jsYh%2FNqcHctLLuQ9dDKnQDPRIn9nLCmyo5dwg5rttSC%2F3Hx668vyC3F9GL%2BT2pf4zJsdCJ6saTAucuAWlLksqYIkppbxqMiod1fPz%2FYo1eu5qrYjJnvRdbFHjTJDiXY9AF7nyDM5ccYKK0eh%2FbNHygh8Dq61jefisPCxL5%2FLgOd2KPTzmp271xIPO3qb%2FpTpFWKIJ7L7&X-Amz-Signature=20bfc9db4a279a80bb2ab4e5d71efcd634f6c217cd2e1a49a20b97fc216ebb13&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UANYNXVK%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T171256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJHMEUCIQD7p%2FIzpAXFcbJIRrZAy8E6KLvFASNkcVP9w127XNoi6QIgOXxtT8K7A%2Bvek8cBVI4hu79He%2F%2BVG%2FBblIJWRCWWDwMq%2FwMIGhAAGgw2Mzc0MjMxODM4MDUiDBFjw2msj9pi1LEb5yrcA7v2G83vLSXwOWD%2BfcBIvP5EKULsQ5ElwlVuDVbwzbhQA%2FckFgKgBzHoauYcB6YV2b%2B8FNkG41BkVYW7WFcoTHgHZ2oWxgP%2BVpeiPtEf832BB8yv%2FiimMLHTPuyHPRNIzQyxtMpJrWYjnvATo7E%2FS0JVeABUILvGo0rgnIPAtkFGHPTpa8OxtSJ9ltwutpwkjZDkXupkF5wQctx7dlBuTIYtmkN91%2Fr4P86qCGGypgaJnDU%2Bk3JuKxWPiwr4iiymsC5zwVHA8VYGrgTEN94qXf0eBgDnM1UH%2FGCmKJtsBIiHKwVnbZ4IeQknHCuXjTSP4pEtEY6IzKm1YNmXnbNEGaJ2XPHc3qMGbuTLUdCKAR1yW7MAsiPDoMSMvTIOATEPpHqPhaijVylSdr2KhpX7ZCFIfqDMaF6jQNv9Ojkc9DJIxg4sawexpvtqIgRS93imLtFHXn5L2NW5poFQg6k8aiTasXhdJTD%2Bor8lwm7uSsMddUsYNcHS6BQaM65t1HK5rIl9gLpC%2BasEhdbfkW%2F3go5%2FRxyXJg5dX9s1uXWcrc9JB%2BSm8HSdq02id5OfofoDDxYrhXTK1e1lpgpi2Ri%2BeF%2BHIchTO4lhkEYELoYmlHXmtzcaUO%2FMuvNbUqEkMKDmg70GOqUBGa5aKsjj2YrU8vqLyp77FLxWYPeXHFJZo7%2FqCPg2VgsJL61BDVUSNH9YjgA9lzuwFLyxmG1iKfUysqZ28wswJXazAV4iBaCw3Sd5lVJO4MRZKQKBi17w0%2Ffv605vO8Wha657MbieucqHPxWuhZPuwXQvs7n4Ve4ht9QYVNVy%2FpJqRdQ9lQVrVAssZ%2F0PBIA%2B1i51AwDoOExAY8Dj4w5g%2FsR7pjxY&X-Amz-Signature=e430a85bbcc7c8bd0f1de4d9b123c75b85c8980cf3208e789bcd635fca34185f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJF6CZLR%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T171257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJIMEYCIQDJqzOAuUAADJX8y0j2BQVUy5UWUgafmd5Qy%2F34fUNJrwIhAIbBN3529pxCrylt%2BHxmnyzWyyf9QQsOhtGK4UEp9yD9Kv8DCBoQABoMNjM3NDIzMTgzODA1IgxGHmKq4Glo5VbvmXwq3AMTiKiwlMuKqEZmFfixivpZ4JjehPsGZjxfxuNOkS3jS2mV%2BIBm4LsGr%2FYAH8DWg9e5xEt99%2BLZy%2BH67BbvS3lLJxBpAs5ZTOqgqlNoiZqDPfrprGRCNWuV1AqgSE24Qn1ibmVXqe7UcID4Sh6cehKrYZPV26WstV%2FgsnOeg%2B6w2ZUClJP1Nt83OtndS%2FZ8yqWxzN4%2BjKm4GZWRH%2B4AaCE4wEpA8eJtmkMpi0JPGOMXQUvv8J3SGfWqSIjvx0ibjOWWIoaWMECB2C4R4JLeigMyBKosEpDuypkIRnMuFw74gsCMr9iSawiO2sPwYQ%2FGpZtlWxSAMjZyV7Vx1s9Dplf%2B2ydqrqamV7JBk9v6v%2BzOk9jOEMFWFJAZdudZ1%2B%2BupGycqwd1WdsWUgOoeeVRxIOD2%2FKyA0QOFcdXXO352QMt00F8QM1%2BpSUrJkEmJnZgIFzJdKgxvzRCkAsX1W6PpaHIVQ80AJf%2BFKxv0KAFxA9ODOiMEBHb5VsWlOViaK6ir%2BRm9KtHnSM7%2FkV%2BM26AWzd8OolRlmkZPBKO6mSiXNhDdkOt%2BRq4zQjCQJycUYGRzJMuU1h%2B4xJdh5Mlen3rJcG7DaCsen3YPGaQvXoZLV5y0U8OvhKX1CZn0S3EKjCA54O9BjqkAUq5LI%2Brn0LEwRS9reFhqQpW9jc9nDCdXYyqQh%2FP%2F%2B7pFyJk6guo9XwDn1FDgmqB1j7ozm2mmqVaQbbe6%2FOQelR39B6%2FNAA8bynMEQ7BOdKXB4d02kVBEoU2doz2KzLWW60SElKOE7d1DZDEYyp1cZBR%2BqoFtESkCp2rB1Lpu7L2xBgvj2RIT5QSTA1d6pTi7%2FcVoTGMCHNW6xIVa990gAkj6a%2BJ&X-Amz-Signature=e4ee8c8538d15d94619a0440c3f9ae47aa32a6982d07314d76c7cd1c3deee9bf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QT43YKGR%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T171256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJGMEQCIAkM5LJkRznVbwjpY%2BTttSup01hh98hTyzkKk%2F9CKoUXAiBcAp8zCj0qKZvYYZr0W90vL23FrsNotlTgvmtm27SA3ir%2FAwgaEAAaDDYzNzQyMzE4MzgwNSIMwgam%2Fh1eVrF8WBMyKtwDTG0BbrKBxaPR5hCL7pbbDCj4T1PsRATMPAXdvNjU6Y0yUybbtnIZvRTQrO9J6U7paEfJvL0Lr%2Frifk8xH1aaLGgwsKMWrzFIrBsteryXfgcrr3aeqsr7Qr%2FYAv3fGuKF5gQrfFmKTmxK9Dz6ZuexZHeI%2B960zyrgP928iXGU5C13%2FrBv3LCxh9OIuoYbaOsafPbXVYF8O%2FhJ7FDQdAy4SvNeWskQIwoVcBxuK8VSm8LyNkYZ42EhlC1pq7CGh1kUVlR8eDyZq6xuV2tYR3jbkr%2BDYAXctxX%2BwNfCSPUbt6tOxqnUefFTSY2%2Fm0tI9EcmQenDW5w%2BWKrgB6IzCQyfBV6PtSLGHa%2BpY9lIiewwum0j5%2BsM1TkHMqX8kltZxED2AlZURx4qhIvG1wNhdEvllFjcfObiF3lYGTI29dmeTXWyJcHjJS1gdWbU5rFJxj6owYS7DN0uRTDsOcyy1%2F%2FkPBrcWbuWuAEKBpif%2Fa2FlEMDHWiAepu9MmMmw%2B5REemIUTbXEnKHyOHcFMQIrZhrTbct8HQFzZTmUd5zRTdC%2FPev9yTaW4Uswy6htygttlpQ6SojByOw8Bo77q5YUF10vyyt4%2BAEFxHyfh%2FLd2SnKXewfyYN193gcxO1GG0wg%2BaDvQY6pgFqAzhMFn8%2BjA57kMKFYGG3jsYh%2FNqcHctLLuQ9dDKnQDPRIn9nLCmyo5dwg5rttSC%2F3Hx668vyC3F9GL%2BT2pf4zJsdCJ6saTAucuAWlLksqYIkppbxqMiod1fPz%2FYo1eu5qrYjJnvRdbFHjTJDiXY9AF7nyDM5ccYKK0eh%2FbNHygh8Dq61jefisPCxL5%2FLgOd2KPTzmp271xIPO3qb%2FpTpFWKIJ7L7&X-Amz-Signature=ac93349f45b51a393ec48d30e3d1e904f9306ff81eb9cb7229ca44cae9358c9c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QT43YKGR%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T171256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJGMEQCIAkM5LJkRznVbwjpY%2BTttSup01hh98hTyzkKk%2F9CKoUXAiBcAp8zCj0qKZvYYZr0W90vL23FrsNotlTgvmtm27SA3ir%2FAwgaEAAaDDYzNzQyMzE4MzgwNSIMwgam%2Fh1eVrF8WBMyKtwDTG0BbrKBxaPR5hCL7pbbDCj4T1PsRATMPAXdvNjU6Y0yUybbtnIZvRTQrO9J6U7paEfJvL0Lr%2Frifk8xH1aaLGgwsKMWrzFIrBsteryXfgcrr3aeqsr7Qr%2FYAv3fGuKF5gQrfFmKTmxK9Dz6ZuexZHeI%2B960zyrgP928iXGU5C13%2FrBv3LCxh9OIuoYbaOsafPbXVYF8O%2FhJ7FDQdAy4SvNeWskQIwoVcBxuK8VSm8LyNkYZ42EhlC1pq7CGh1kUVlR8eDyZq6xuV2tYR3jbkr%2BDYAXctxX%2BwNfCSPUbt6tOxqnUefFTSY2%2Fm0tI9EcmQenDW5w%2BWKrgB6IzCQyfBV6PtSLGHa%2BpY9lIiewwum0j5%2BsM1TkHMqX8kltZxED2AlZURx4qhIvG1wNhdEvllFjcfObiF3lYGTI29dmeTXWyJcHjJS1gdWbU5rFJxj6owYS7DN0uRTDsOcyy1%2F%2FkPBrcWbuWuAEKBpif%2Fa2FlEMDHWiAepu9MmMmw%2B5REemIUTbXEnKHyOHcFMQIrZhrTbct8HQFzZTmUd5zRTdC%2FPev9yTaW4Uswy6htygttlpQ6SojByOw8Bo77q5YUF10vyyt4%2BAEFxHyfh%2FLd2SnKXewfyYN193gcxO1GG0wg%2BaDvQY6pgFqAzhMFn8%2BjA57kMKFYGG3jsYh%2FNqcHctLLuQ9dDKnQDPRIn9nLCmyo5dwg5rttSC%2F3Hx668vyC3F9GL%2BT2pf4zJsdCJ6saTAucuAWlLksqYIkppbxqMiod1fPz%2FYo1eu5qrYjJnvRdbFHjTJDiXY9AF7nyDM5ccYKK0eh%2FbNHygh8Dq61jefisPCxL5%2FLgOd2KPTzmp271xIPO3qb%2FpTpFWKIJ7L7&X-Amz-Signature=8f6cd316da54e70bf41b8dee22d6929e173bb199f963b36a8e0aeecbf9a893b0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QT43YKGR%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T171256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJGMEQCIAkM5LJkRznVbwjpY%2BTttSup01hh98hTyzkKk%2F9CKoUXAiBcAp8zCj0qKZvYYZr0W90vL23FrsNotlTgvmtm27SA3ir%2FAwgaEAAaDDYzNzQyMzE4MzgwNSIMwgam%2Fh1eVrF8WBMyKtwDTG0BbrKBxaPR5hCL7pbbDCj4T1PsRATMPAXdvNjU6Y0yUybbtnIZvRTQrO9J6U7paEfJvL0Lr%2Frifk8xH1aaLGgwsKMWrzFIrBsteryXfgcrr3aeqsr7Qr%2FYAv3fGuKF5gQrfFmKTmxK9Dz6ZuexZHeI%2B960zyrgP928iXGU5C13%2FrBv3LCxh9OIuoYbaOsafPbXVYF8O%2FhJ7FDQdAy4SvNeWskQIwoVcBxuK8VSm8LyNkYZ42EhlC1pq7CGh1kUVlR8eDyZq6xuV2tYR3jbkr%2BDYAXctxX%2BwNfCSPUbt6tOxqnUefFTSY2%2Fm0tI9EcmQenDW5w%2BWKrgB6IzCQyfBV6PtSLGHa%2BpY9lIiewwum0j5%2BsM1TkHMqX8kltZxED2AlZURx4qhIvG1wNhdEvllFjcfObiF3lYGTI29dmeTXWyJcHjJS1gdWbU5rFJxj6owYS7DN0uRTDsOcyy1%2F%2FkPBrcWbuWuAEKBpif%2Fa2FlEMDHWiAepu9MmMmw%2B5REemIUTbXEnKHyOHcFMQIrZhrTbct8HQFzZTmUd5zRTdC%2FPev9yTaW4Uswy6htygttlpQ6SojByOw8Bo77q5YUF10vyyt4%2BAEFxHyfh%2FLd2SnKXewfyYN193gcxO1GG0wg%2BaDvQY6pgFqAzhMFn8%2BjA57kMKFYGG3jsYh%2FNqcHctLLuQ9dDKnQDPRIn9nLCmyo5dwg5rttSC%2F3Hx668vyC3F9GL%2BT2pf4zJsdCJ6saTAucuAWlLksqYIkppbxqMiod1fPz%2FYo1eu5qrYjJnvRdbFHjTJDiXY9AF7nyDM5ccYKK0eh%2FbNHygh8Dq61jefisPCxL5%2FLgOd2KPTzmp271xIPO3qb%2FpTpFWKIJ7L7&X-Amz-Signature=658669f3bc2e1b71ce7a53906077d44bae50756da4f4ca39feb15ad8f9b3ca09&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QT43YKGR%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T171256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJGMEQCIAkM5LJkRznVbwjpY%2BTttSup01hh98hTyzkKk%2F9CKoUXAiBcAp8zCj0qKZvYYZr0W90vL23FrsNotlTgvmtm27SA3ir%2FAwgaEAAaDDYzNzQyMzE4MzgwNSIMwgam%2Fh1eVrF8WBMyKtwDTG0BbrKBxaPR5hCL7pbbDCj4T1PsRATMPAXdvNjU6Y0yUybbtnIZvRTQrO9J6U7paEfJvL0Lr%2Frifk8xH1aaLGgwsKMWrzFIrBsteryXfgcrr3aeqsr7Qr%2FYAv3fGuKF5gQrfFmKTmxK9Dz6ZuexZHeI%2B960zyrgP928iXGU5C13%2FrBv3LCxh9OIuoYbaOsafPbXVYF8O%2FhJ7FDQdAy4SvNeWskQIwoVcBxuK8VSm8LyNkYZ42EhlC1pq7CGh1kUVlR8eDyZq6xuV2tYR3jbkr%2BDYAXctxX%2BwNfCSPUbt6tOxqnUefFTSY2%2Fm0tI9EcmQenDW5w%2BWKrgB6IzCQyfBV6PtSLGHa%2BpY9lIiewwum0j5%2BsM1TkHMqX8kltZxED2AlZURx4qhIvG1wNhdEvllFjcfObiF3lYGTI29dmeTXWyJcHjJS1gdWbU5rFJxj6owYS7DN0uRTDsOcyy1%2F%2FkPBrcWbuWuAEKBpif%2Fa2FlEMDHWiAepu9MmMmw%2B5REemIUTbXEnKHyOHcFMQIrZhrTbct8HQFzZTmUd5zRTdC%2FPev9yTaW4Uswy6htygttlpQ6SojByOw8Bo77q5YUF10vyyt4%2BAEFxHyfh%2FLd2SnKXewfyYN193gcxO1GG0wg%2BaDvQY6pgFqAzhMFn8%2BjA57kMKFYGG3jsYh%2FNqcHctLLuQ9dDKnQDPRIn9nLCmyo5dwg5rttSC%2F3Hx668vyC3F9GL%2BT2pf4zJsdCJ6saTAucuAWlLksqYIkppbxqMiod1fPz%2FYo1eu5qrYjJnvRdbFHjTJDiXY9AF7nyDM5ccYKK0eh%2FbNHygh8Dq61jefisPCxL5%2FLgOd2KPTzmp271xIPO3qb%2FpTpFWKIJ7L7&X-Amz-Signature=f4ff49b7bbad1e1948e960287779f091d4616e48de33e009b6bd7deab5d83132&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
