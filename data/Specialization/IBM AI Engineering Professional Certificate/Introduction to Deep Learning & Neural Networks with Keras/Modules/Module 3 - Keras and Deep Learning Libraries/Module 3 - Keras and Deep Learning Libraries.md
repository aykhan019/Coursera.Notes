

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YXTCTGLV%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIFebHkjCGRODoUkBnTuExGCC1Qwboono6nLhIrgEeGN%2FAiA6K8dXDl9oT90apYsnQNvFYok2kG7m%2FRJC08klm7Q6eCqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMEAIuXtbGnSQ5XUwKKtwDo%2FORLCAxVMVDT2MOfY7loKtp0XDHdi1IykGoJ5aqsz%2FRMKgPeZwz%2FTT8OJtj3x3lRfBhvNP84EjJZuTim%2B19ZKYoUVwzyUJr52Q5SwulC0BiY4Pk6wA3%2BDuozv2VorDzjt5UKCMlvVPranyD1i5Em1FJsy6mw5HiMyAdxNgTZYnA%2FHu3kTb%2F468k%2FKbBU4D0XqvXDt0Delwdj74dZVn063eZkyaceHP7NVFMuzYoWgcwYRSMg%2BgRhlwf1Oh4bIhJ8%2BKpiL9Or3W3LoLWdDDM5Inrocl9RqJdVxi%2Bkdfm67kNu4wuqig9sR13L4DSOLfAcT1qzespwu%2Fp%2BhtK%2FSgS5Au6gMMNI8I9BgvJZ07Y%2BVnKbeEvRygdsmpQc8hYuLrRgq%2BGX%2FR%2FR41k6JVbxKDYPLiHQQfMIJge40jb6%2FeJEK%2B2cCTr0dREebkZuNuyQSuSjY8XkHjVc1NFM%2BgSYfkPpmVTIcbuZxR6g8XxXOtwc3EfGT6V2b2UmzWtLAp%2BtafhDpNL8DWTLafv%2BbJgTMnxF4zH4WYaybdW1zF2u%2BTOX6rc%2FBW1WI2JDR9E4rfGx72nZfIRH7BjYIJ07S9g00sNOxqSxF98cRBVzNoX7G0HdedhAAMbxI1K7rvOdrUwqrvmvAY6pgEePucjjWXN77bBYZcIFefBQT22JQdJsrlM6OY4nz2Q7pek1tiDmGUvwyoHU1Fhr7XF%2FuTbHhgL5ZHL8e%2BMWTuootn%2Bzl0Yvkl68JRfas7cqhZCHTxM7EXurieH4jqNM55F2rzVXnvu%2FzmtzDvug4GLQO4sxTUHnucE9Ysdwm0Eu48h6cko%2BKGtkCvFL4DN%2BRNyZl%2BbxL4fFUvyGVtlVIlViBE6d0pX&X-Amz-Signature=ac3c916f6ed09dc63d70e509a90aa59f0ad8bd6c5bc7fa2cf66e4180e5719fa5&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YXTCTGLV%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIFebHkjCGRODoUkBnTuExGCC1Qwboono6nLhIrgEeGN%2FAiA6K8dXDl9oT90apYsnQNvFYok2kG7m%2FRJC08klm7Q6eCqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMEAIuXtbGnSQ5XUwKKtwDo%2FORLCAxVMVDT2MOfY7loKtp0XDHdi1IykGoJ5aqsz%2FRMKgPeZwz%2FTT8OJtj3x3lRfBhvNP84EjJZuTim%2B19ZKYoUVwzyUJr52Q5SwulC0BiY4Pk6wA3%2BDuozv2VorDzjt5UKCMlvVPranyD1i5Em1FJsy6mw5HiMyAdxNgTZYnA%2FHu3kTb%2F468k%2FKbBU4D0XqvXDt0Delwdj74dZVn063eZkyaceHP7NVFMuzYoWgcwYRSMg%2BgRhlwf1Oh4bIhJ8%2BKpiL9Or3W3LoLWdDDM5Inrocl9RqJdVxi%2Bkdfm67kNu4wuqig9sR13L4DSOLfAcT1qzespwu%2Fp%2BhtK%2FSgS5Au6gMMNI8I9BgvJZ07Y%2BVnKbeEvRygdsmpQc8hYuLrRgq%2BGX%2FR%2FR41k6JVbxKDYPLiHQQfMIJge40jb6%2FeJEK%2B2cCTr0dREebkZuNuyQSuSjY8XkHjVc1NFM%2BgSYfkPpmVTIcbuZxR6g8XxXOtwc3EfGT6V2b2UmzWtLAp%2BtafhDpNL8DWTLafv%2BbJgTMnxF4zH4WYaybdW1zF2u%2BTOX6rc%2FBW1WI2JDR9E4rfGx72nZfIRH7BjYIJ07S9g00sNOxqSxF98cRBVzNoX7G0HdedhAAMbxI1K7rvOdrUwqrvmvAY6pgEePucjjWXN77bBYZcIFefBQT22JQdJsrlM6OY4nz2Q7pek1tiDmGUvwyoHU1Fhr7XF%2FuTbHhgL5ZHL8e%2BMWTuootn%2Bzl0Yvkl68JRfas7cqhZCHTxM7EXurieH4jqNM55F2rzVXnvu%2FzmtzDvug4GLQO4sxTUHnucE9Ysdwm0Eu48h6cko%2BKGtkCvFL4DN%2BRNyZl%2BbxL4fFUvyGVtlVIlViBE6d0pX&X-Amz-Signature=8b44717c5468dcd49c6f76ea1dfc3b97a5838eefc31ccaf7be4013e6594d4a2e&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YXTCTGLV%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIFebHkjCGRODoUkBnTuExGCC1Qwboono6nLhIrgEeGN%2FAiA6K8dXDl9oT90apYsnQNvFYok2kG7m%2FRJC08klm7Q6eCqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMEAIuXtbGnSQ5XUwKKtwDo%2FORLCAxVMVDT2MOfY7loKtp0XDHdi1IykGoJ5aqsz%2FRMKgPeZwz%2FTT8OJtj3x3lRfBhvNP84EjJZuTim%2B19ZKYoUVwzyUJr52Q5SwulC0BiY4Pk6wA3%2BDuozv2VorDzjt5UKCMlvVPranyD1i5Em1FJsy6mw5HiMyAdxNgTZYnA%2FHu3kTb%2F468k%2FKbBU4D0XqvXDt0Delwdj74dZVn063eZkyaceHP7NVFMuzYoWgcwYRSMg%2BgRhlwf1Oh4bIhJ8%2BKpiL9Or3W3LoLWdDDM5Inrocl9RqJdVxi%2Bkdfm67kNu4wuqig9sR13L4DSOLfAcT1qzespwu%2Fp%2BhtK%2FSgS5Au6gMMNI8I9BgvJZ07Y%2BVnKbeEvRygdsmpQc8hYuLrRgq%2BGX%2FR%2FR41k6JVbxKDYPLiHQQfMIJge40jb6%2FeJEK%2B2cCTr0dREebkZuNuyQSuSjY8XkHjVc1NFM%2BgSYfkPpmVTIcbuZxR6g8XxXOtwc3EfGT6V2b2UmzWtLAp%2BtafhDpNL8DWTLafv%2BbJgTMnxF4zH4WYaybdW1zF2u%2BTOX6rc%2FBW1WI2JDR9E4rfGx72nZfIRH7BjYIJ07S9g00sNOxqSxF98cRBVzNoX7G0HdedhAAMbxI1K7rvOdrUwqrvmvAY6pgEePucjjWXN77bBYZcIFefBQT22JQdJsrlM6OY4nz2Q7pek1tiDmGUvwyoHU1Fhr7XF%2FuTbHhgL5ZHL8e%2BMWTuootn%2Bzl0Yvkl68JRfas7cqhZCHTxM7EXurieH4jqNM55F2rzVXnvu%2FzmtzDvug4GLQO4sxTUHnucE9Ysdwm0Eu48h6cko%2BKGtkCvFL4DN%2BRNyZl%2BbxL4fFUvyGVtlVIlViBE6d0pX&X-Amz-Signature=c1627b8f4d239ce32be6403cdee9b13c2ea369c2e2a60cffff38c361a9a92e00&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666TFAJ3ZZ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQDYT0WoGFnplqFblN8yu4LSqqwjswuY6S7C7YJr4dmvWgIgTM%2F3OLtg7Mrqn2bMbBIl6uRktxyY1cHQjeYRay6v8WQqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDou13fikIHl%2BlBwsircAzbKjsrgfj9zBJbVccU6at8PhPXYwgP20%2FuyPQTVGn7AOZ3PyaG2M0imbCqBWbo7ESFvhIodu826%2FgoFkkeb%2FRqVYrUnzh42ubTunN4gIbthTR6ztd8VwV8IGUeBXTWo%2FgxmY7L9NNhQ8%2BLdtF2cTfXVt8%2FQRSb3N2oRrFV0Z1LnjgUfSnFUstXAIoFW6IASB57FRiF033kEgrQOGuVZCiFcXr%2FaxxL4sYAxvU76Jlv%2FHRZg1FH8SWVBGrlYqVnk5fLhUYfryUYbV0hmnVVnFn8VjLaWPJLPYd4ryvpKCP%2BfxciKZ6dFfQgZWGlAuhB8MZifKsXjPxnehyhUfGDfY9DBvhnMxlVTrbLiHh16KdFZLNR8HaYCHugFS18fW8SYZ1bv%2BaPgiPZMk0fWaesTjfBGx9Qm3ZxsqxU%2FzeoA2hWrbefifdtqCY0WqIl8kW7fYhSpRRtxMFtLFw6M%2BX4wN6qKbW0hvWVdVT51lCNbqqXSArsPF8sJN2YgSV2%2FcktNAMIQ3UM07NMywVG%2B5b%2Fa%2FgIDBOIzo%2BcBFECq1FPAbWd3JNlLmjxlYqGDEHA5kq4ekt2wTW6lvjyPhj4FukHXov5Oz%2BYC9tTm0ho6kP4l%2BWS%2F7CLOSm%2FKd%2FyrMfAnMJC75rwGOqUByCwb1YjXhA4WY36iH82LwFyjw9UKFEqj6KCsncKhuAQ5e0ntNMrV0CahpKZrkmPm6xe6ddmTCcJn%2Fi4PWNlTmpxNV%2Fa%2FdVakeQXs6uYtisIIBTaUdqRrxAel1jMWHFttjWTrZaR57VDQmMYlLgzQY2TpQSuZzOCsyzRpQ6RWqnUue9Z1%2FwAHZ3WexseibXRTMAG2eXfa9a3DhO02BH%2BCnAZH9tC0&X-Amz-Signature=d76f4de9cc5b985d08bac993ff08b5be7982cfef9bd365a8bb90357944d91ba3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SMZF7VBC%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIFSJJe1HgrfYku9ZlFxS3v8g4QV2fvBL%2FgusPiFJ9YgtAiEA4sQPYoAdbepyJBkK06vbMkQtw7ztrEwif%2BYMJcoghGYqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNHe9y%2FeJ8cpu1k4iCrcAyuYdHe2LrDa3xA7AK%2B1o5mCPwZQe0ZFubQKQwuu0ObeFnq31QaUY9uF2y%2FQVnWRD0q3qB%2FlkmLkNPH288jKaMrwvTKEyGrNjJUIo4X9SGVfduDgJclauD34wopDRInb76uMLSjkTfAchMdI2TDgrn%2F8ycCCNcedLauRssT7Ug5ketDyfxS%2Bfud0GThKn0770din5tXFA2gV1mQVlSfVuzIaAz3AoX4INyqNspaRLs9bo9B9yMjOwiVp%2FeosiYJaAtyvolPE2nDc0ozJlLcaavg7mARdtLTE7msJYVar8Amn4KKAKEIL%2F3zhlNfyo7qinkRYiC3HILI%2Bq9aytlc7y4aryFYVpO36kByx4KHrCN3cO7zNcVJ8mZnwbCMD7REZPYuLnRmesLsmHF8LZaN7ABPQ8tWXOtFYSgbcrK1FjptZabi%2FJec6sRV8idiQxbtPyZNTnlfhQtBDWogbvBsGOYfTY12r36uh1Os8oWVKwvhu9k%2Ftq19VuagnNrinJDocxcZOeiLp7q8j29EiQcfOIW%2Fen%2FyFK%2FL9ZQPem19%2B2EChOmBJAZpVAHAnOnLzU%2F8Z3LPEBd7aWcfXKbVQ6Rd6FHZ4ZZIAZRNCF4F%2BCorYUOQiweGMVwjXgSbvPQc8MIa75rwGOqUBAZuWKGXUEhXQ1l3QW0jQTzyPjTs33hiGkuzqDMv%2BKUY4F95E1nJlpqHlsPb%2FihCxgstsoSIzf9ZY8ai7M8cefMfqL8SvFz5z5VWwpVe9rdOQ1VSxU3fml%2FFT0HOO6GGWZg2BDJ6ieN2KGIM2frI%2FDNgquMm0YwsMQykFT6HNZ0dSXet7kLNngx%2FHWXvW9NaYxIjODEtF0dikw7%2BIiYufDqg58Xsv&X-Amz-Signature=ca21563d786125a9fe4ebd18760934be3a533c0d16abf5b5ffec00690e4f6c2a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YXTCTGLV%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIFebHkjCGRODoUkBnTuExGCC1Qwboono6nLhIrgEeGN%2FAiA6K8dXDl9oT90apYsnQNvFYok2kG7m%2FRJC08klm7Q6eCqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMEAIuXtbGnSQ5XUwKKtwDo%2FORLCAxVMVDT2MOfY7loKtp0XDHdi1IykGoJ5aqsz%2FRMKgPeZwz%2FTT8OJtj3x3lRfBhvNP84EjJZuTim%2B19ZKYoUVwzyUJr52Q5SwulC0BiY4Pk6wA3%2BDuozv2VorDzjt5UKCMlvVPranyD1i5Em1FJsy6mw5HiMyAdxNgTZYnA%2FHu3kTb%2F468k%2FKbBU4D0XqvXDt0Delwdj74dZVn063eZkyaceHP7NVFMuzYoWgcwYRSMg%2BgRhlwf1Oh4bIhJ8%2BKpiL9Or3W3LoLWdDDM5Inrocl9RqJdVxi%2Bkdfm67kNu4wuqig9sR13L4DSOLfAcT1qzespwu%2Fp%2BhtK%2FSgS5Au6gMMNI8I9BgvJZ07Y%2BVnKbeEvRygdsmpQc8hYuLrRgq%2BGX%2FR%2FR41k6JVbxKDYPLiHQQfMIJge40jb6%2FeJEK%2B2cCTr0dREebkZuNuyQSuSjY8XkHjVc1NFM%2BgSYfkPpmVTIcbuZxR6g8XxXOtwc3EfGT6V2b2UmzWtLAp%2BtafhDpNL8DWTLafv%2BbJgTMnxF4zH4WYaybdW1zF2u%2BTOX6rc%2FBW1WI2JDR9E4rfGx72nZfIRH7BjYIJ07S9g00sNOxqSxF98cRBVzNoX7G0HdedhAAMbxI1K7rvOdrUwqrvmvAY6pgEePucjjWXN77bBYZcIFefBQT22JQdJsrlM6OY4nz2Q7pek1tiDmGUvwyoHU1Fhr7XF%2FuTbHhgL5ZHL8e%2BMWTuootn%2Bzl0Yvkl68JRfas7cqhZCHTxM7EXurieH4jqNM55F2rzVXnvu%2FzmtzDvug4GLQO4sxTUHnucE9Ysdwm0Eu48h6cko%2BKGtkCvFL4DN%2BRNyZl%2BbxL4fFUvyGVtlVIlViBE6d0pX&X-Amz-Signature=fc8e94ce6fbc7712ba32215e50fe83b9c08a87a772fe743fafa69649744f225b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YXTCTGLV%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIFebHkjCGRODoUkBnTuExGCC1Qwboono6nLhIrgEeGN%2FAiA6K8dXDl9oT90apYsnQNvFYok2kG7m%2FRJC08klm7Q6eCqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMEAIuXtbGnSQ5XUwKKtwDo%2FORLCAxVMVDT2MOfY7loKtp0XDHdi1IykGoJ5aqsz%2FRMKgPeZwz%2FTT8OJtj3x3lRfBhvNP84EjJZuTim%2B19ZKYoUVwzyUJr52Q5SwulC0BiY4Pk6wA3%2BDuozv2VorDzjt5UKCMlvVPranyD1i5Em1FJsy6mw5HiMyAdxNgTZYnA%2FHu3kTb%2F468k%2FKbBU4D0XqvXDt0Delwdj74dZVn063eZkyaceHP7NVFMuzYoWgcwYRSMg%2BgRhlwf1Oh4bIhJ8%2BKpiL9Or3W3LoLWdDDM5Inrocl9RqJdVxi%2Bkdfm67kNu4wuqig9sR13L4DSOLfAcT1qzespwu%2Fp%2BhtK%2FSgS5Au6gMMNI8I9BgvJZ07Y%2BVnKbeEvRygdsmpQc8hYuLrRgq%2BGX%2FR%2FR41k6JVbxKDYPLiHQQfMIJge40jb6%2FeJEK%2B2cCTr0dREebkZuNuyQSuSjY8XkHjVc1NFM%2BgSYfkPpmVTIcbuZxR6g8XxXOtwc3EfGT6V2b2UmzWtLAp%2BtafhDpNL8DWTLafv%2BbJgTMnxF4zH4WYaybdW1zF2u%2BTOX6rc%2FBW1WI2JDR9E4rfGx72nZfIRH7BjYIJ07S9g00sNOxqSxF98cRBVzNoX7G0HdedhAAMbxI1K7rvOdrUwqrvmvAY6pgEePucjjWXN77bBYZcIFefBQT22JQdJsrlM6OY4nz2Q7pek1tiDmGUvwyoHU1Fhr7XF%2FuTbHhgL5ZHL8e%2BMWTuootn%2Bzl0Yvkl68JRfas7cqhZCHTxM7EXurieH4jqNM55F2rzVXnvu%2FzmtzDvug4GLQO4sxTUHnucE9Ysdwm0Eu48h6cko%2BKGtkCvFL4DN%2BRNyZl%2BbxL4fFUvyGVtlVIlViBE6d0pX&X-Amz-Signature=71331f3d4e4a525ee565c5a575c02338579ed6929b370a454cb5108e31a7462d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YXTCTGLV%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIFebHkjCGRODoUkBnTuExGCC1Qwboono6nLhIrgEeGN%2FAiA6K8dXDl9oT90apYsnQNvFYok2kG7m%2FRJC08klm7Q6eCqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMEAIuXtbGnSQ5XUwKKtwDo%2FORLCAxVMVDT2MOfY7loKtp0XDHdi1IykGoJ5aqsz%2FRMKgPeZwz%2FTT8OJtj3x3lRfBhvNP84EjJZuTim%2B19ZKYoUVwzyUJr52Q5SwulC0BiY4Pk6wA3%2BDuozv2VorDzjt5UKCMlvVPranyD1i5Em1FJsy6mw5HiMyAdxNgTZYnA%2FHu3kTb%2F468k%2FKbBU4D0XqvXDt0Delwdj74dZVn063eZkyaceHP7NVFMuzYoWgcwYRSMg%2BgRhlwf1Oh4bIhJ8%2BKpiL9Or3W3LoLWdDDM5Inrocl9RqJdVxi%2Bkdfm67kNu4wuqig9sR13L4DSOLfAcT1qzespwu%2Fp%2BhtK%2FSgS5Au6gMMNI8I9BgvJZ07Y%2BVnKbeEvRygdsmpQc8hYuLrRgq%2BGX%2FR%2FR41k6JVbxKDYPLiHQQfMIJge40jb6%2FeJEK%2B2cCTr0dREebkZuNuyQSuSjY8XkHjVc1NFM%2BgSYfkPpmVTIcbuZxR6g8XxXOtwc3EfGT6V2b2UmzWtLAp%2BtafhDpNL8DWTLafv%2BbJgTMnxF4zH4WYaybdW1zF2u%2BTOX6rc%2FBW1WI2JDR9E4rfGx72nZfIRH7BjYIJ07S9g00sNOxqSxF98cRBVzNoX7G0HdedhAAMbxI1K7rvOdrUwqrvmvAY6pgEePucjjWXN77bBYZcIFefBQT22JQdJsrlM6OY4nz2Q7pek1tiDmGUvwyoHU1Fhr7XF%2FuTbHhgL5ZHL8e%2BMWTuootn%2Bzl0Yvkl68JRfas7cqhZCHTxM7EXurieH4jqNM55F2rzVXnvu%2FzmtzDvug4GLQO4sxTUHnucE9Ysdwm0Eu48h6cko%2BKGtkCvFL4DN%2BRNyZl%2BbxL4fFUvyGVtlVIlViBE6d0pX&X-Amz-Signature=1626c607f1e79dfe0b917cf3766a0211fecd3ff14cc16a3695f5b985006771dd&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YXTCTGLV%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIFebHkjCGRODoUkBnTuExGCC1Qwboono6nLhIrgEeGN%2FAiA6K8dXDl9oT90apYsnQNvFYok2kG7m%2FRJC08klm7Q6eCqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMEAIuXtbGnSQ5XUwKKtwDo%2FORLCAxVMVDT2MOfY7loKtp0XDHdi1IykGoJ5aqsz%2FRMKgPeZwz%2FTT8OJtj3x3lRfBhvNP84EjJZuTim%2B19ZKYoUVwzyUJr52Q5SwulC0BiY4Pk6wA3%2BDuozv2VorDzjt5UKCMlvVPranyD1i5Em1FJsy6mw5HiMyAdxNgTZYnA%2FHu3kTb%2F468k%2FKbBU4D0XqvXDt0Delwdj74dZVn063eZkyaceHP7NVFMuzYoWgcwYRSMg%2BgRhlwf1Oh4bIhJ8%2BKpiL9Or3W3LoLWdDDM5Inrocl9RqJdVxi%2Bkdfm67kNu4wuqig9sR13L4DSOLfAcT1qzespwu%2Fp%2BhtK%2FSgS5Au6gMMNI8I9BgvJZ07Y%2BVnKbeEvRygdsmpQc8hYuLrRgq%2BGX%2FR%2FR41k6JVbxKDYPLiHQQfMIJge40jb6%2FeJEK%2B2cCTr0dREebkZuNuyQSuSjY8XkHjVc1NFM%2BgSYfkPpmVTIcbuZxR6g8XxXOtwc3EfGT6V2b2UmzWtLAp%2BtafhDpNL8DWTLafv%2BbJgTMnxF4zH4WYaybdW1zF2u%2BTOX6rc%2FBW1WI2JDR9E4rfGx72nZfIRH7BjYIJ07S9g00sNOxqSxF98cRBVzNoX7G0HdedhAAMbxI1K7rvOdrUwqrvmvAY6pgEePucjjWXN77bBYZcIFefBQT22JQdJsrlM6OY4nz2Q7pek1tiDmGUvwyoHU1Fhr7XF%2FuTbHhgL5ZHL8e%2BMWTuootn%2Bzl0Yvkl68JRfas7cqhZCHTxM7EXurieH4jqNM55F2rzVXnvu%2FzmtzDvug4GLQO4sxTUHnucE9Ysdwm0Eu48h6cko%2BKGtkCvFL4DN%2BRNyZl%2BbxL4fFUvyGVtlVIlViBE6d0pX&X-Amz-Signature=7e21e4cd5988ed8893853e3bf566c26fe47b13cc3bfe858b981f3fcde8ce7999&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
