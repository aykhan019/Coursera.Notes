

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665XDRGXRW%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJGMEQCIE5tz84UMYAs8gnnN1MfQisjkptgW41Mqz1ld0AnDOIpAiBcaYBL7LgNXGrIzqKO%2FTQbPBR2%2FySP213SMr6iPWhEhSr%2FAwhdEAAaDDYzNzQyMzE4MzgwNSIMSJqMQJkKbRwa8oOQKtwDljF3AmI%2FsM9JIglb5aNVZZmoGcIp8MTkJ9xtN8%2BodpmEpIL%2FZW%2F5rnoRHL%2BMPelQC3lSdtwEG5tJFh%2F2ZowPEUF5vqxcp0284MpIXeLIBtJmb8PKZnWQPmdWpv%2F%2FDx8Vbkvzud7kL6i6v7mQ6f%2BhxdfFzYKJHMIwkGdSB3PU9uy9AdpZDlSodeAk8zHZnREf9Dp%2B3b2AaalexUgV%2FQewZYBicW28t8itoSWuLHa6dqP4birqQ6e11%2Fcao6Ne2yonqNtizEIXeXJmiGJZCvLrL9p69qzeD9AgN4Y%2BCQTahh7vHy%2BQjbCDdRbPDhUUQ3bfEO017KUotP7TQhIdhrGdzQhJluCiRmm1PgHq97m4zTq5r%2FHFUVEoVQev%2Bv0fJjP3%2F125KaAOnraZFnENZPG%2Fg1%2FtCsNn4VlJyOH7U73AakIPr86hNst%2FshskPW2NM2LI2b3zPeo5vNAnwz40kP%2FQat3c%2FLfVoZe4usDIjW3fsk2CWRUYuOZhuYpDaeSSGtliNLvuOKNPs%2BJukpkF2fdiLAHUMLk2SufjxMHNGskf5IWmjl99mLOKjCRy8Z9gwX5v171NqJIQOdfvr9tKcwi4XxqAa0FYFMcltRaQ6cFwFWcCMN2qB2lkhkONbFkwt8OSvQY6pgGI0%2BQ26OjnrLAQT6vCloSuvYcLa2KaexrNaE5tCKPx7Sia8K48tI3JoCUKu2wlRaHhGLXWFMFqH4sKyjpYF0wM0%2Fo31%2BmlFURNDxGMCPNtEKZCJdMVWRcLfTQ6uz8XmeqECpIXtt%2BKKGtpqsLvfG0SCTP7Rf9aFXjJThYx2YaU9v0fbHrPnfiXfJmwql%2BpZOIMOwzRkIHQQGGwlQUIMCNjL2CZMzFP&X-Amz-Signature=1174e3ad1e193e435c4b7676397e22cc0ce1609d6824763a268a8e932a94bd96&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665XDRGXRW%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJGMEQCIE5tz84UMYAs8gnnN1MfQisjkptgW41Mqz1ld0AnDOIpAiBcaYBL7LgNXGrIzqKO%2FTQbPBR2%2FySP213SMr6iPWhEhSr%2FAwhdEAAaDDYzNzQyMzE4MzgwNSIMSJqMQJkKbRwa8oOQKtwDljF3AmI%2FsM9JIglb5aNVZZmoGcIp8MTkJ9xtN8%2BodpmEpIL%2FZW%2F5rnoRHL%2BMPelQC3lSdtwEG5tJFh%2F2ZowPEUF5vqxcp0284MpIXeLIBtJmb8PKZnWQPmdWpv%2F%2FDx8Vbkvzud7kL6i6v7mQ6f%2BhxdfFzYKJHMIwkGdSB3PU9uy9AdpZDlSodeAk8zHZnREf9Dp%2B3b2AaalexUgV%2FQewZYBicW28t8itoSWuLHa6dqP4birqQ6e11%2Fcao6Ne2yonqNtizEIXeXJmiGJZCvLrL9p69qzeD9AgN4Y%2BCQTahh7vHy%2BQjbCDdRbPDhUUQ3bfEO017KUotP7TQhIdhrGdzQhJluCiRmm1PgHq97m4zTq5r%2FHFUVEoVQev%2Bv0fJjP3%2F125KaAOnraZFnENZPG%2Fg1%2FtCsNn4VlJyOH7U73AakIPr86hNst%2FshskPW2NM2LI2b3zPeo5vNAnwz40kP%2FQat3c%2FLfVoZe4usDIjW3fsk2CWRUYuOZhuYpDaeSSGtliNLvuOKNPs%2BJukpkF2fdiLAHUMLk2SufjxMHNGskf5IWmjl99mLOKjCRy8Z9gwX5v171NqJIQOdfvr9tKcwi4XxqAa0FYFMcltRaQ6cFwFWcCMN2qB2lkhkONbFkwt8OSvQY6pgGI0%2BQ26OjnrLAQT6vCloSuvYcLa2KaexrNaE5tCKPx7Sia8K48tI3JoCUKu2wlRaHhGLXWFMFqH4sKyjpYF0wM0%2Fo31%2BmlFURNDxGMCPNtEKZCJdMVWRcLfTQ6uz8XmeqECpIXtt%2BKKGtpqsLvfG0SCTP7Rf9aFXjJThYx2YaU9v0fbHrPnfiXfJmwql%2BpZOIMOwzRkIHQQGGwlQUIMCNjL2CZMzFP&X-Amz-Signature=1ce5f8cce9552a076a60fd15e3661bd5f3e841afebeb8558386c412a9d6dcd17&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665XDRGXRW%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJGMEQCIE5tz84UMYAs8gnnN1MfQisjkptgW41Mqz1ld0AnDOIpAiBcaYBL7LgNXGrIzqKO%2FTQbPBR2%2FySP213SMr6iPWhEhSr%2FAwhdEAAaDDYzNzQyMzE4MzgwNSIMSJqMQJkKbRwa8oOQKtwDljF3AmI%2FsM9JIglb5aNVZZmoGcIp8MTkJ9xtN8%2BodpmEpIL%2FZW%2F5rnoRHL%2BMPelQC3lSdtwEG5tJFh%2F2ZowPEUF5vqxcp0284MpIXeLIBtJmb8PKZnWQPmdWpv%2F%2FDx8Vbkvzud7kL6i6v7mQ6f%2BhxdfFzYKJHMIwkGdSB3PU9uy9AdpZDlSodeAk8zHZnREf9Dp%2B3b2AaalexUgV%2FQewZYBicW28t8itoSWuLHa6dqP4birqQ6e11%2Fcao6Ne2yonqNtizEIXeXJmiGJZCvLrL9p69qzeD9AgN4Y%2BCQTahh7vHy%2BQjbCDdRbPDhUUQ3bfEO017KUotP7TQhIdhrGdzQhJluCiRmm1PgHq97m4zTq5r%2FHFUVEoVQev%2Bv0fJjP3%2F125KaAOnraZFnENZPG%2Fg1%2FtCsNn4VlJyOH7U73AakIPr86hNst%2FshskPW2NM2LI2b3zPeo5vNAnwz40kP%2FQat3c%2FLfVoZe4usDIjW3fsk2CWRUYuOZhuYpDaeSSGtliNLvuOKNPs%2BJukpkF2fdiLAHUMLk2SufjxMHNGskf5IWmjl99mLOKjCRy8Z9gwX5v171NqJIQOdfvr9tKcwi4XxqAa0FYFMcltRaQ6cFwFWcCMN2qB2lkhkONbFkwt8OSvQY6pgGI0%2BQ26OjnrLAQT6vCloSuvYcLa2KaexrNaE5tCKPx7Sia8K48tI3JoCUKu2wlRaHhGLXWFMFqH4sKyjpYF0wM0%2Fo31%2BmlFURNDxGMCPNtEKZCJdMVWRcLfTQ6uz8XmeqECpIXtt%2BKKGtpqsLvfG0SCTP7Rf9aFXjJThYx2YaU9v0fbHrPnfiXfJmwql%2BpZOIMOwzRkIHQQGGwlQUIMCNjL2CZMzFP&X-Amz-Signature=5f212043a26e209f17fd74c975991c33e67406599f981a5235f321daf100e457&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y67JX2FB%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQCtgIkBhbWYW%2F2H%2FMY9Ew4vlF1S2uBnKWOkR%2FGxrr7JPgIgdCN3sxCfRXhTDMwqxcFXgSHuUgn27s9JLSjVnigz02Qq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDOwvhq7jLfrEcA7KHyrcA8Rr%2BrGWhzkcacozuGf%2FXiitGfm5EVx6FSlD6yV1tMrs4GYd0J9Qpw6n2Tbmrpyybkx7uePqSJcfGMwzqmHXvh3DsxUUVwVfaUg9z0W9M8aP%2F%2FI76LzRrlOYv5RpHM7Lm5Ou0gr9%2FpwBDuaA24M1BlbS22hKShCO8AcvKY0y%2Bzofa%2FloEm4aOkvB2EOEslgQdX1z8DvFxPd1WXnXj5TEHVBh4xXDTxRXy%2BJtco8IQCXkF10lST%2BeNnQFLvO59Ogm8GX78mrkU9LPYLBkI0%2FN7Ubq30S%2BUqFUMh8Cipv5pDSS%2FnVoesyopeg7wTkr9DbedKRvOA8JwpQtKiP%2F2WEtb8bVifTZL2aU2anb319%2F0FZwl%2FdF6oDJJg8sf7CkRkJq41JzmXuqyoOXR5iFHLbcCKpKixd0H%2F62qD0i%2F4kj0aJFpmdlgUIQWg1N1mO%2B3Vn1Cq2lNI156WC1CKObXYeoyKcghViPsgGF%2FjoBxWqc%2FKQCIp4NI7id3ycUKKGjtGkZy5o55EJ6jeNrbJhgS2dmZcZ2U2OFoTJe2R18avJ0f5hPFyncEpWdl%2F%2B%2FwcHyMao8%2BWaOR01AiOU8VADXZrVmu93CVLffS%2B1YMP6hC4h7QV4YbRAuN5p3jbML4XotMOzDkr0GOqUB1JLYx4MswnmB78peJO9A7ViUUjHgNQ%2FuzhNpkF6bHwzxQS0DTTx9jqJliqkJ942yXZ2R29hycFkjV0A0ma5XJ8VwQ%2F5aT7VQC3U2e9xykQ6IqWOvjx4BPb9ZmFa%2BE8F%2FjAqnKoHTBY050PLMbhBr974au%2BiOt0mpYGKbZo9UzJ9OETHcRGvh%2BYlocCve5VYZV%2B7KQrPhU3IPy6YFLkN9rkr4tsdI&X-Amz-Signature=29f54774c997ec9479dd8c06a05676e8a87dd06ba348d86e70805e2d9591fa9a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46652VWNBOJ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJIMEYCIQC2JvAk%2FjWVQ0fS%2B5jQGlOMYqO7oT6Kud8plzy%2Fn99%2FZwIhANGlro1r4zgECYBPOcqiUCHGwvUlXaZYvCPMb3%2BtBNHCKv8DCF0QABoMNjM3NDIzMTgzODA1Igz3DH2DskcvmEgZ67Eq3ANjuJCy79huJEgRcritayEVsyU9M6eYcDJ3Dg8cxn4AjUIFvpFlCSXu%2BEZfvHYuWkDw1ZJyDjT1VVj5I2gqcpsmSsBr7EB5LGmLYq8ln8MbIsCpI8cSV8LJ2%2B9EwRg9FR%2BSipCKQTBHn5XuDuks2igdbYdIhMm3vNLKgrvRh3%2FAGLxRWfRRlrPCOIvVW4HfLvzS7%2FYVpLhWFLm2ZL70hKuyc7991he9qyI%2BUuaHh7jejiyGMiNmc12baI4jE9YrgsPo%2Brjl1RVgzFWOcyvIVMG1x5Prdu8tq9MWrynUCXfru8COMv%2BNwuzMDJGlOVCYlRJgKhllSGYLCyN8uN5HzZELQIEKc8fZ%2Bk%2F4tqFmEA4Z06p8kyk6WiwoFon8C6wh9Xqn97b9RiYk6rLF6VQy8WJSAixfGqxFyg7R9W05KDDuu6T%2F6%2B3tDZEG3Xd1TBoUmf55QQ5rJZmwN3ElrCWV7t0YGhpMTD4UB5fq2f6eGIG%2FlGe26c2W2QJ8%2FFBrdxaKIdQTFIijHxupNES8QUNNMWspzkyZHTQIAaizg4%2B%2B8QqtH9GCEHszuR85E2k7PEyJSDGz%2F7viOu6IDvhnyEnLFx%2BGnOuNX%2FsqDks%2FugA3ilCE2gLYpNdXfVDwy0ey6zDCw5K9BjqkAaIymfCBsgVcwwObadOaqI3By1pRUS4Rpim3kl%2BlA0dZTXkkoYJNHg4CTjK37BjsDYFlXYH5fl8ji4S3NdfphmxqxZu9A5T3%2BL3Wnjpsf4VwxCxu4L4y%2Fes57rNhlfbuNfhyBW5GaaPJgrAJrxBQXZJRD5Y6FSyIQ%2B0K5vx8F9U3GpjPBsWkzEEvgvBJ9OocPRmDcKqX59g2ed%2BK0tsr5aRa3RMH&X-Amz-Signature=4717aa44de17381c7c261b606f13612e4d1de97ec232319fb0f25eda39c0727d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665XDRGXRW%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJGMEQCIE5tz84UMYAs8gnnN1MfQisjkptgW41Mqz1ld0AnDOIpAiBcaYBL7LgNXGrIzqKO%2FTQbPBR2%2FySP213SMr6iPWhEhSr%2FAwhdEAAaDDYzNzQyMzE4MzgwNSIMSJqMQJkKbRwa8oOQKtwDljF3AmI%2FsM9JIglb5aNVZZmoGcIp8MTkJ9xtN8%2BodpmEpIL%2FZW%2F5rnoRHL%2BMPelQC3lSdtwEG5tJFh%2F2ZowPEUF5vqxcp0284MpIXeLIBtJmb8PKZnWQPmdWpv%2F%2FDx8Vbkvzud7kL6i6v7mQ6f%2BhxdfFzYKJHMIwkGdSB3PU9uy9AdpZDlSodeAk8zHZnREf9Dp%2B3b2AaalexUgV%2FQewZYBicW28t8itoSWuLHa6dqP4birqQ6e11%2Fcao6Ne2yonqNtizEIXeXJmiGJZCvLrL9p69qzeD9AgN4Y%2BCQTahh7vHy%2BQjbCDdRbPDhUUQ3bfEO017KUotP7TQhIdhrGdzQhJluCiRmm1PgHq97m4zTq5r%2FHFUVEoVQev%2Bv0fJjP3%2F125KaAOnraZFnENZPG%2Fg1%2FtCsNn4VlJyOH7U73AakIPr86hNst%2FshskPW2NM2LI2b3zPeo5vNAnwz40kP%2FQat3c%2FLfVoZe4usDIjW3fsk2CWRUYuOZhuYpDaeSSGtliNLvuOKNPs%2BJukpkF2fdiLAHUMLk2SufjxMHNGskf5IWmjl99mLOKjCRy8Z9gwX5v171NqJIQOdfvr9tKcwi4XxqAa0FYFMcltRaQ6cFwFWcCMN2qB2lkhkONbFkwt8OSvQY6pgGI0%2BQ26OjnrLAQT6vCloSuvYcLa2KaexrNaE5tCKPx7Sia8K48tI3JoCUKu2wlRaHhGLXWFMFqH4sKyjpYF0wM0%2Fo31%2BmlFURNDxGMCPNtEKZCJdMVWRcLfTQ6uz8XmeqECpIXtt%2BKKGtpqsLvfG0SCTP7Rf9aFXjJThYx2YaU9v0fbHrPnfiXfJmwql%2BpZOIMOwzRkIHQQGGwlQUIMCNjL2CZMzFP&X-Amz-Signature=2871d98259b7ba35132a5639cc011a24c1f50659c80f77b307f6ec68904da568&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665XDRGXRW%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJGMEQCIE5tz84UMYAs8gnnN1MfQisjkptgW41Mqz1ld0AnDOIpAiBcaYBL7LgNXGrIzqKO%2FTQbPBR2%2FySP213SMr6iPWhEhSr%2FAwhdEAAaDDYzNzQyMzE4MzgwNSIMSJqMQJkKbRwa8oOQKtwDljF3AmI%2FsM9JIglb5aNVZZmoGcIp8MTkJ9xtN8%2BodpmEpIL%2FZW%2F5rnoRHL%2BMPelQC3lSdtwEG5tJFh%2F2ZowPEUF5vqxcp0284MpIXeLIBtJmb8PKZnWQPmdWpv%2F%2FDx8Vbkvzud7kL6i6v7mQ6f%2BhxdfFzYKJHMIwkGdSB3PU9uy9AdpZDlSodeAk8zHZnREf9Dp%2B3b2AaalexUgV%2FQewZYBicW28t8itoSWuLHa6dqP4birqQ6e11%2Fcao6Ne2yonqNtizEIXeXJmiGJZCvLrL9p69qzeD9AgN4Y%2BCQTahh7vHy%2BQjbCDdRbPDhUUQ3bfEO017KUotP7TQhIdhrGdzQhJluCiRmm1PgHq97m4zTq5r%2FHFUVEoVQev%2Bv0fJjP3%2F125KaAOnraZFnENZPG%2Fg1%2FtCsNn4VlJyOH7U73AakIPr86hNst%2FshskPW2NM2LI2b3zPeo5vNAnwz40kP%2FQat3c%2FLfVoZe4usDIjW3fsk2CWRUYuOZhuYpDaeSSGtliNLvuOKNPs%2BJukpkF2fdiLAHUMLk2SufjxMHNGskf5IWmjl99mLOKjCRy8Z9gwX5v171NqJIQOdfvr9tKcwi4XxqAa0FYFMcltRaQ6cFwFWcCMN2qB2lkhkONbFkwt8OSvQY6pgGI0%2BQ26OjnrLAQT6vCloSuvYcLa2KaexrNaE5tCKPx7Sia8K48tI3JoCUKu2wlRaHhGLXWFMFqH4sKyjpYF0wM0%2Fo31%2BmlFURNDxGMCPNtEKZCJdMVWRcLfTQ6uz8XmeqECpIXtt%2BKKGtpqsLvfG0SCTP7Rf9aFXjJThYx2YaU9v0fbHrPnfiXfJmwql%2BpZOIMOwzRkIHQQGGwlQUIMCNjL2CZMzFP&X-Amz-Signature=d9722416185e609a8ec26383678cfcbf763263e981b65ffe270c125f857fff8a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665XDRGXRW%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJGMEQCIE5tz84UMYAs8gnnN1MfQisjkptgW41Mqz1ld0AnDOIpAiBcaYBL7LgNXGrIzqKO%2FTQbPBR2%2FySP213SMr6iPWhEhSr%2FAwhdEAAaDDYzNzQyMzE4MzgwNSIMSJqMQJkKbRwa8oOQKtwDljF3AmI%2FsM9JIglb5aNVZZmoGcIp8MTkJ9xtN8%2BodpmEpIL%2FZW%2F5rnoRHL%2BMPelQC3lSdtwEG5tJFh%2F2ZowPEUF5vqxcp0284MpIXeLIBtJmb8PKZnWQPmdWpv%2F%2FDx8Vbkvzud7kL6i6v7mQ6f%2BhxdfFzYKJHMIwkGdSB3PU9uy9AdpZDlSodeAk8zHZnREf9Dp%2B3b2AaalexUgV%2FQewZYBicW28t8itoSWuLHa6dqP4birqQ6e11%2Fcao6Ne2yonqNtizEIXeXJmiGJZCvLrL9p69qzeD9AgN4Y%2BCQTahh7vHy%2BQjbCDdRbPDhUUQ3bfEO017KUotP7TQhIdhrGdzQhJluCiRmm1PgHq97m4zTq5r%2FHFUVEoVQev%2Bv0fJjP3%2F125KaAOnraZFnENZPG%2Fg1%2FtCsNn4VlJyOH7U73AakIPr86hNst%2FshskPW2NM2LI2b3zPeo5vNAnwz40kP%2FQat3c%2FLfVoZe4usDIjW3fsk2CWRUYuOZhuYpDaeSSGtliNLvuOKNPs%2BJukpkF2fdiLAHUMLk2SufjxMHNGskf5IWmjl99mLOKjCRy8Z9gwX5v171NqJIQOdfvr9tKcwi4XxqAa0FYFMcltRaQ6cFwFWcCMN2qB2lkhkONbFkwt8OSvQY6pgGI0%2BQ26OjnrLAQT6vCloSuvYcLa2KaexrNaE5tCKPx7Sia8K48tI3JoCUKu2wlRaHhGLXWFMFqH4sKyjpYF0wM0%2Fo31%2BmlFURNDxGMCPNtEKZCJdMVWRcLfTQ6uz8XmeqECpIXtt%2BKKGtpqsLvfG0SCTP7Rf9aFXjJThYx2YaU9v0fbHrPnfiXfJmwql%2BpZOIMOwzRkIHQQGGwlQUIMCNjL2CZMzFP&X-Amz-Signature=aa59e71b2b9b2cce3301c6b8b4dcd903a51f454f01e38f58824ca47a4f1a05c3&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665XDRGXRW%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJGMEQCIE5tz84UMYAs8gnnN1MfQisjkptgW41Mqz1ld0AnDOIpAiBcaYBL7LgNXGrIzqKO%2FTQbPBR2%2FySP213SMr6iPWhEhSr%2FAwhdEAAaDDYzNzQyMzE4MzgwNSIMSJqMQJkKbRwa8oOQKtwDljF3AmI%2FsM9JIglb5aNVZZmoGcIp8MTkJ9xtN8%2BodpmEpIL%2FZW%2F5rnoRHL%2BMPelQC3lSdtwEG5tJFh%2F2ZowPEUF5vqxcp0284MpIXeLIBtJmb8PKZnWQPmdWpv%2F%2FDx8Vbkvzud7kL6i6v7mQ6f%2BhxdfFzYKJHMIwkGdSB3PU9uy9AdpZDlSodeAk8zHZnREf9Dp%2B3b2AaalexUgV%2FQewZYBicW28t8itoSWuLHa6dqP4birqQ6e11%2Fcao6Ne2yonqNtizEIXeXJmiGJZCvLrL9p69qzeD9AgN4Y%2BCQTahh7vHy%2BQjbCDdRbPDhUUQ3bfEO017KUotP7TQhIdhrGdzQhJluCiRmm1PgHq97m4zTq5r%2FHFUVEoVQev%2Bv0fJjP3%2F125KaAOnraZFnENZPG%2Fg1%2FtCsNn4VlJyOH7U73AakIPr86hNst%2FshskPW2NM2LI2b3zPeo5vNAnwz40kP%2FQat3c%2FLfVoZe4usDIjW3fsk2CWRUYuOZhuYpDaeSSGtliNLvuOKNPs%2BJukpkF2fdiLAHUMLk2SufjxMHNGskf5IWmjl99mLOKjCRy8Z9gwX5v171NqJIQOdfvr9tKcwi4XxqAa0FYFMcltRaQ6cFwFWcCMN2qB2lkhkONbFkwt8OSvQY6pgGI0%2BQ26OjnrLAQT6vCloSuvYcLa2KaexrNaE5tCKPx7Sia8K48tI3JoCUKu2wlRaHhGLXWFMFqH4sKyjpYF0wM0%2Fo31%2BmlFURNDxGMCPNtEKZCJdMVWRcLfTQ6uz8XmeqECpIXtt%2BKKGtpqsLvfG0SCTP7Rf9aFXjJThYx2YaU9v0fbHrPnfiXfJmwql%2BpZOIMOwzRkIHQQGGwlQUIMCNjL2CZMzFP&X-Amz-Signature=bf153c0d61cd92f51ae40f055430e0edf11411e7bcce88e0815b8a663bf70577&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
