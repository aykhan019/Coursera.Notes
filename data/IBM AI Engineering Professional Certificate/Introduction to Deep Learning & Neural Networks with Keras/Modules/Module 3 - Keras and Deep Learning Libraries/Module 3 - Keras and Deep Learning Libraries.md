

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSPVZWWK%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIHmEMO%2BwBVxpez6mFwcWBsQGsRlqmQwWa1a6tYkin%2Fj2AiEA1wmMXmr71fCLUGss6C6HVMCvnIlam18IqdFZTul%2Fw94q%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDAwB0rYohVvalJJ54SrcA8meDSZYn4PIskziuWJBkhkv7WzykztVJJtRWZVvBvTOBX8ByNVPGca%2FcYU5AZAYAP4EK2gB6kz6OTLm5%2BdCQ%2BYbQWP8PgykwN6r9RzRy0%2B7nUH1ePJJxGz2z4Lq404rwBxSnyju2VfGxeD3GEgJeJD9KHnYQwB09mxEJYQzYdAVFuGtk7Zk1PipdFmzEBNNElarGLOz8oZzig4W873YjA%2FiG7%2FRLr2lFFyhhroxDiWmSBPNKVgdwRgzjpfvYEvL4sFLbjONsuo0e9nCPxjV5EItCd5nhpam53vjhkI9wQlybXvBX%2F9wgUGqFqNVZbnznsoCxKAlParkKdgoH5%2FGSLvjB6tbE6dx3DvLPtlkJ6G0eBHKHs33XItYdH1yzANE9LJQmFVsgrjm8x6p7gs9W7MM5dwUx4GSot6%2F0C3ut04ffY9qJJD22TEDOpR9FUbYtZTmCd%2FZu5COYGKCaNLsDsjmFO2kCHZe%2FNkBCMclcnol6jOTKV1onjniD%2B%2F7ixf161ELOK%2Bgh2WV%2BwX%2FncN0CQoOIiHIaM5uS9h5%2F5vw31nO7AQc1m9Jl2yQgrsBD6Xux4tmdz%2FdvmW2yLF00DyLnXmhUqqxWvSwdsmo1c8JmcHGuktvNOqX9QvHns1NMKq4lL0GOqUBzS78R1rRG2McMTqaAhnZkQ7opbMtnjtkAyfKyn9WYZr%2FHiD6AEvS74J2xv%2BHrPjPQ6C%2BctlOFRi%2BisL%2BezFGwdVKetkiDwwjMXfUF68lPSeHk3NLzypa%2FQN4Put%2BgikqeSFR1vNKFRU8EA2QB4ZcaYeZeNpxj7BDcU7r%2BUSG9tYDSOinoDfVK1wYxlbHJ0UsCm2%2B%2BVWbHNXSGaAqOqeffbMLRL7L&X-Amz-Signature=51a9c699a2b3142a532bf1749e3123f416a7aede53afac38229f01bcdbf7b54d&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSPVZWWK%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIHmEMO%2BwBVxpez6mFwcWBsQGsRlqmQwWa1a6tYkin%2Fj2AiEA1wmMXmr71fCLUGss6C6HVMCvnIlam18IqdFZTul%2Fw94q%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDAwB0rYohVvalJJ54SrcA8meDSZYn4PIskziuWJBkhkv7WzykztVJJtRWZVvBvTOBX8ByNVPGca%2FcYU5AZAYAP4EK2gB6kz6OTLm5%2BdCQ%2BYbQWP8PgykwN6r9RzRy0%2B7nUH1ePJJxGz2z4Lq404rwBxSnyju2VfGxeD3GEgJeJD9KHnYQwB09mxEJYQzYdAVFuGtk7Zk1PipdFmzEBNNElarGLOz8oZzig4W873YjA%2FiG7%2FRLr2lFFyhhroxDiWmSBPNKVgdwRgzjpfvYEvL4sFLbjONsuo0e9nCPxjV5EItCd5nhpam53vjhkI9wQlybXvBX%2F9wgUGqFqNVZbnznsoCxKAlParkKdgoH5%2FGSLvjB6tbE6dx3DvLPtlkJ6G0eBHKHs33XItYdH1yzANE9LJQmFVsgrjm8x6p7gs9W7MM5dwUx4GSot6%2F0C3ut04ffY9qJJD22TEDOpR9FUbYtZTmCd%2FZu5COYGKCaNLsDsjmFO2kCHZe%2FNkBCMclcnol6jOTKV1onjniD%2B%2F7ixf161ELOK%2Bgh2WV%2BwX%2FncN0CQoOIiHIaM5uS9h5%2F5vw31nO7AQc1m9Jl2yQgrsBD6Xux4tmdz%2FdvmW2yLF00DyLnXmhUqqxWvSwdsmo1c8JmcHGuktvNOqX9QvHns1NMKq4lL0GOqUBzS78R1rRG2McMTqaAhnZkQ7opbMtnjtkAyfKyn9WYZr%2FHiD6AEvS74J2xv%2BHrPjPQ6C%2BctlOFRi%2BisL%2BezFGwdVKetkiDwwjMXfUF68lPSeHk3NLzypa%2FQN4Put%2BgikqeSFR1vNKFRU8EA2QB4ZcaYeZeNpxj7BDcU7r%2BUSG9tYDSOinoDfVK1wYxlbHJ0UsCm2%2B%2BVWbHNXSGaAqOqeffbMLRL7L&X-Amz-Signature=2e9476cf15c90b1ca86cbd7632e5f8267edd200a0a65a23f05adbf8e5af289f2&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSPVZWWK%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIHmEMO%2BwBVxpez6mFwcWBsQGsRlqmQwWa1a6tYkin%2Fj2AiEA1wmMXmr71fCLUGss6C6HVMCvnIlam18IqdFZTul%2Fw94q%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDAwB0rYohVvalJJ54SrcA8meDSZYn4PIskziuWJBkhkv7WzykztVJJtRWZVvBvTOBX8ByNVPGca%2FcYU5AZAYAP4EK2gB6kz6OTLm5%2BdCQ%2BYbQWP8PgykwN6r9RzRy0%2B7nUH1ePJJxGz2z4Lq404rwBxSnyju2VfGxeD3GEgJeJD9KHnYQwB09mxEJYQzYdAVFuGtk7Zk1PipdFmzEBNNElarGLOz8oZzig4W873YjA%2FiG7%2FRLr2lFFyhhroxDiWmSBPNKVgdwRgzjpfvYEvL4sFLbjONsuo0e9nCPxjV5EItCd5nhpam53vjhkI9wQlybXvBX%2F9wgUGqFqNVZbnznsoCxKAlParkKdgoH5%2FGSLvjB6tbE6dx3DvLPtlkJ6G0eBHKHs33XItYdH1yzANE9LJQmFVsgrjm8x6p7gs9W7MM5dwUx4GSot6%2F0C3ut04ffY9qJJD22TEDOpR9FUbYtZTmCd%2FZu5COYGKCaNLsDsjmFO2kCHZe%2FNkBCMclcnol6jOTKV1onjniD%2B%2F7ixf161ELOK%2Bgh2WV%2BwX%2FncN0CQoOIiHIaM5uS9h5%2F5vw31nO7AQc1m9Jl2yQgrsBD6Xux4tmdz%2FdvmW2yLF00DyLnXmhUqqxWvSwdsmo1c8JmcHGuktvNOqX9QvHns1NMKq4lL0GOqUBzS78R1rRG2McMTqaAhnZkQ7opbMtnjtkAyfKyn9WYZr%2FHiD6AEvS74J2xv%2BHrPjPQ6C%2BctlOFRi%2BisL%2BezFGwdVKetkiDwwjMXfUF68lPSeHk3NLzypa%2FQN4Put%2BgikqeSFR1vNKFRU8EA2QB4ZcaYeZeNpxj7BDcU7r%2BUSG9tYDSOinoDfVK1wYxlbHJ0UsCm2%2B%2BVWbHNXSGaAqOqeffbMLRL7L&X-Amz-Signature=028d1864ab24e231f9c9e9947286f371557db1e38f722087644acfcb9db14f8e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W3HXQMC6%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIATJJUiu8FiMFMREnnuTMppNjF6Vklj%2B%2BaDcfc3tJkHVAiEAwr5VQzP00z4KLSi9nLYhv7qlcwpJmIPwGCxB6dSPRSQq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDMKi54EBg5%2F1JeXYICrcAxo0IHIKTLuMtpYh4D1qz1v3i9PQMmykWTmxRxtWhUkT0evPifN%2BaucX%2BKkCTDlbHTs3UdmhLBLd0G%2FxlG%2FjmJeMJ%2BiBsHwjIvBcy8lvhkki2xXoMQJd7hpKZdC26tTd%2FGMSsNcmKCiwgrSqCd%2FiJSHK6F5Xje92H3uv3fqB4%2BRLWjubpbJSUMODLN4qkray2hN2iGVOC3t0sbNXbZGsNDNI9Gb64B%2FXv8KaR%2B8Okl5wF%2FsyiSx5Wd9c%2FNL2HP%2BJyymrwqf19SZ%2BuP2G9DI%2FGIQFfpUKLOF81caOQupJFhENMWnaf%2FXZ7ChThzyrUOmxme5C%2BRoe2WK96KiReOv5DmODQ2ay6RJ350V%2FSQeyWIs2quVZayx%2FgA%2B2DHR65R3Jy0I%2FS5LLFnzKshtyWRe6JrTdXtMSq6jRCMHVn1Qd3cxbbVaZDVWA%2BtIy%2B%2FOq6dqQKxfTSDupKtLZ7BjzFfpprbUKokIw4XyHto0V%2BxPzqpkDY%2FAyFP4thG1MrK7nZEJVJwSgHC80r6cgF4vy8WD09G9BrybeuG2HaM%2Fk%2F%2Bdh7Y4V7%2F4u91YUu8s47agn8bd4wPd%2FCybCLwT4YbEbmkeL%2Bm0Rvim7VggeJ1zUb4WYrrSqWivxlyRA76T%2B6Z%2BHMKO4lL0GOqUBP9sNeIN1VR4Xq6%2BmwP%2BPblfKU3VcgAIKOt4JSHrD9%2F1QPV0zJYwp6rJdueKT6RPCix80RA%2BuxgWi2AKLQNCM0qVJptluqhK4x5c2JsqH9nS6c5YW3d0bX%2Bkb7i2Mj8qCqoPM%2BAN7vXUG50bXtVCMvSZEpjOHPQUIGUKuVKRJN8ojm4V3fr%2FGS66bk1gzs4hpuMkvvq1Wg6%2FMJ7GZOOi7%2Fbfq%2BrF7&X-Amz-Signature=b248feb11e600730cd519407c582dc6323f574f521ca8839d825d70f2b18b60f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667NBC6AZH%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211354Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIQDm%2Bo1P2oYIancjr8u7GP1n1%2FUgYq8tOliYbSt%2Bpj9DjgIgANa%2BRbzWZIjcKuxpxPlh8OseEjXSMD%2Fo%2F5ASYLLdvFEq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDBVDLWDimaQn72UbtircAwHCGnNPBKnIpoHnvdGzglaf3ln4p%2Fn7fhxHtT0%2BzKNZn6zb1YmpIvMYj9mcOHH8hzPMVM1EFEtTPBKrydl6857Q57yPuYXFTsPdd2pm1wQHD0xkS51GlXfESuMmWJsAGQUuuWkfq2R8tNPPNSj7%2FpVpJ8FsBb4zAc%2BZwL5E%2FnUGxjyDTcIsQvBlX9zy56lo7c9J2xTMRpigOoM3c7htoXQ1miKoFl1z0MNugUducv%2FuG%2FJcC%2Fu9V%2F0NItKGj3kV%2FZai1agjqHJiDkIuz6falwv2VFAhhHBuSPTRYG3wjq5dw5u%2BF6na%2Fg0g3AagLX85eF5MnwDk%2FPFqARMRJo6K5Te1f9TbsH0UlF5d8DIUYD2P1oPnXfs3OARGGKZPzUow%2FOddEl10v7U%2BFDnbWQtwd3WxPoibYLY%2B4Yz99mycALk8mSy5FLmvyxT6fOOqZuGGm5Scp3A7JahsBZikR6gIwLD5FaYyZAILKzcy4da1K2%2B6U5GJWOqzNwR47UuPHr73voHcwN325XgBMrlCtRlC2Jh7bG6U0iZiWLR8n8BwNaVmzaXmm7ruk%2F%2Beggr%2BYKrT0sKbqwNI1xeNgXuGswkXnFL7hHFz6yUh0YNZ8IcNXM7HSGhfn9a5C3XqUX46MMy4lL0GOqUB3Dwwojo%2BHphyGE9KP9fmXW9RzmZ381lFqjybKciiN40cDdUh7yr%2F2UjEOwIIB3BrCQ8yDtCFLTvFK6x8AILQaLKKCnxZNPgaBuH5JZGJ9W%2F%2FDJChmSUKD0xy0O2B3akIUDj8P3dJ9CU2AoV4l7dZx6CAGpJOn3%2FVQzUWUceXdD8D5CaYnPkZ8c0ODWcC0GAR7V%2F4y8jgQAx4JwD9xYcDVumghm6Q&X-Amz-Signature=4dd3307eb62b9cd1d4736b4a7028a3d0c37708d0baeef64ac88c4dd1af6f7739&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSPVZWWK%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIHmEMO%2BwBVxpez6mFwcWBsQGsRlqmQwWa1a6tYkin%2Fj2AiEA1wmMXmr71fCLUGss6C6HVMCvnIlam18IqdFZTul%2Fw94q%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDAwB0rYohVvalJJ54SrcA8meDSZYn4PIskziuWJBkhkv7WzykztVJJtRWZVvBvTOBX8ByNVPGca%2FcYU5AZAYAP4EK2gB6kz6OTLm5%2BdCQ%2BYbQWP8PgykwN6r9RzRy0%2B7nUH1ePJJxGz2z4Lq404rwBxSnyju2VfGxeD3GEgJeJD9KHnYQwB09mxEJYQzYdAVFuGtk7Zk1PipdFmzEBNNElarGLOz8oZzig4W873YjA%2FiG7%2FRLr2lFFyhhroxDiWmSBPNKVgdwRgzjpfvYEvL4sFLbjONsuo0e9nCPxjV5EItCd5nhpam53vjhkI9wQlybXvBX%2F9wgUGqFqNVZbnznsoCxKAlParkKdgoH5%2FGSLvjB6tbE6dx3DvLPtlkJ6G0eBHKHs33XItYdH1yzANE9LJQmFVsgrjm8x6p7gs9W7MM5dwUx4GSot6%2F0C3ut04ffY9qJJD22TEDOpR9FUbYtZTmCd%2FZu5COYGKCaNLsDsjmFO2kCHZe%2FNkBCMclcnol6jOTKV1onjniD%2B%2F7ixf161ELOK%2Bgh2WV%2BwX%2FncN0CQoOIiHIaM5uS9h5%2F5vw31nO7AQc1m9Jl2yQgrsBD6Xux4tmdz%2FdvmW2yLF00DyLnXmhUqqxWvSwdsmo1c8JmcHGuktvNOqX9QvHns1NMKq4lL0GOqUBzS78R1rRG2McMTqaAhnZkQ7opbMtnjtkAyfKyn9WYZr%2FHiD6AEvS74J2xv%2BHrPjPQ6C%2BctlOFRi%2BisL%2BezFGwdVKetkiDwwjMXfUF68lPSeHk3NLzypa%2FQN4Put%2BgikqeSFR1vNKFRU8EA2QB4ZcaYeZeNpxj7BDcU7r%2BUSG9tYDSOinoDfVK1wYxlbHJ0UsCm2%2B%2BVWbHNXSGaAqOqeffbMLRL7L&X-Amz-Signature=48674e87c1e01f5327111213c34e569fea11c1e493b2c2a159338ec7e0bbcc65&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSPVZWWK%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIHmEMO%2BwBVxpez6mFwcWBsQGsRlqmQwWa1a6tYkin%2Fj2AiEA1wmMXmr71fCLUGss6C6HVMCvnIlam18IqdFZTul%2Fw94q%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDAwB0rYohVvalJJ54SrcA8meDSZYn4PIskziuWJBkhkv7WzykztVJJtRWZVvBvTOBX8ByNVPGca%2FcYU5AZAYAP4EK2gB6kz6OTLm5%2BdCQ%2BYbQWP8PgykwN6r9RzRy0%2B7nUH1ePJJxGz2z4Lq404rwBxSnyju2VfGxeD3GEgJeJD9KHnYQwB09mxEJYQzYdAVFuGtk7Zk1PipdFmzEBNNElarGLOz8oZzig4W873YjA%2FiG7%2FRLr2lFFyhhroxDiWmSBPNKVgdwRgzjpfvYEvL4sFLbjONsuo0e9nCPxjV5EItCd5nhpam53vjhkI9wQlybXvBX%2F9wgUGqFqNVZbnznsoCxKAlParkKdgoH5%2FGSLvjB6tbE6dx3DvLPtlkJ6G0eBHKHs33XItYdH1yzANE9LJQmFVsgrjm8x6p7gs9W7MM5dwUx4GSot6%2F0C3ut04ffY9qJJD22TEDOpR9FUbYtZTmCd%2FZu5COYGKCaNLsDsjmFO2kCHZe%2FNkBCMclcnol6jOTKV1onjniD%2B%2F7ixf161ELOK%2Bgh2WV%2BwX%2FncN0CQoOIiHIaM5uS9h5%2F5vw31nO7AQc1m9Jl2yQgrsBD6Xux4tmdz%2FdvmW2yLF00DyLnXmhUqqxWvSwdsmo1c8JmcHGuktvNOqX9QvHns1NMKq4lL0GOqUBzS78R1rRG2McMTqaAhnZkQ7opbMtnjtkAyfKyn9WYZr%2FHiD6AEvS74J2xv%2BHrPjPQ6C%2BctlOFRi%2BisL%2BezFGwdVKetkiDwwjMXfUF68lPSeHk3NLzypa%2FQN4Put%2BgikqeSFR1vNKFRU8EA2QB4ZcaYeZeNpxj7BDcU7r%2BUSG9tYDSOinoDfVK1wYxlbHJ0UsCm2%2B%2BVWbHNXSGaAqOqeffbMLRL7L&X-Amz-Signature=6779e555ebba0dbce602bdfc756f1dd0697318fc46e223c3d4fd21578f204db3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSPVZWWK%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIHmEMO%2BwBVxpez6mFwcWBsQGsRlqmQwWa1a6tYkin%2Fj2AiEA1wmMXmr71fCLUGss6C6HVMCvnIlam18IqdFZTul%2Fw94q%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDAwB0rYohVvalJJ54SrcA8meDSZYn4PIskziuWJBkhkv7WzykztVJJtRWZVvBvTOBX8ByNVPGca%2FcYU5AZAYAP4EK2gB6kz6OTLm5%2BdCQ%2BYbQWP8PgykwN6r9RzRy0%2B7nUH1ePJJxGz2z4Lq404rwBxSnyju2VfGxeD3GEgJeJD9KHnYQwB09mxEJYQzYdAVFuGtk7Zk1PipdFmzEBNNElarGLOz8oZzig4W873YjA%2FiG7%2FRLr2lFFyhhroxDiWmSBPNKVgdwRgzjpfvYEvL4sFLbjONsuo0e9nCPxjV5EItCd5nhpam53vjhkI9wQlybXvBX%2F9wgUGqFqNVZbnznsoCxKAlParkKdgoH5%2FGSLvjB6tbE6dx3DvLPtlkJ6G0eBHKHs33XItYdH1yzANE9LJQmFVsgrjm8x6p7gs9W7MM5dwUx4GSot6%2F0C3ut04ffY9qJJD22TEDOpR9FUbYtZTmCd%2FZu5COYGKCaNLsDsjmFO2kCHZe%2FNkBCMclcnol6jOTKV1onjniD%2B%2F7ixf161ELOK%2Bgh2WV%2BwX%2FncN0CQoOIiHIaM5uS9h5%2F5vw31nO7AQc1m9Jl2yQgrsBD6Xux4tmdz%2FdvmW2yLF00DyLnXmhUqqxWvSwdsmo1c8JmcHGuktvNOqX9QvHns1NMKq4lL0GOqUBzS78R1rRG2McMTqaAhnZkQ7opbMtnjtkAyfKyn9WYZr%2FHiD6AEvS74J2xv%2BHrPjPQ6C%2BctlOFRi%2BisL%2BezFGwdVKetkiDwwjMXfUF68lPSeHk3NLzypa%2FQN4Put%2BgikqeSFR1vNKFRU8EA2QB4ZcaYeZeNpxj7BDcU7r%2BUSG9tYDSOinoDfVK1wYxlbHJ0UsCm2%2B%2BVWbHNXSGaAqOqeffbMLRL7L&X-Amz-Signature=1276b5b68f0bcc308ddc6786a53ae34869056c82ec9d54300a296e445a5ff71f&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSPVZWWK%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIHmEMO%2BwBVxpez6mFwcWBsQGsRlqmQwWa1a6tYkin%2Fj2AiEA1wmMXmr71fCLUGss6C6HVMCvnIlam18IqdFZTul%2Fw94q%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDAwB0rYohVvalJJ54SrcA8meDSZYn4PIskziuWJBkhkv7WzykztVJJtRWZVvBvTOBX8ByNVPGca%2FcYU5AZAYAP4EK2gB6kz6OTLm5%2BdCQ%2BYbQWP8PgykwN6r9RzRy0%2B7nUH1ePJJxGz2z4Lq404rwBxSnyju2VfGxeD3GEgJeJD9KHnYQwB09mxEJYQzYdAVFuGtk7Zk1PipdFmzEBNNElarGLOz8oZzig4W873YjA%2FiG7%2FRLr2lFFyhhroxDiWmSBPNKVgdwRgzjpfvYEvL4sFLbjONsuo0e9nCPxjV5EItCd5nhpam53vjhkI9wQlybXvBX%2F9wgUGqFqNVZbnznsoCxKAlParkKdgoH5%2FGSLvjB6tbE6dx3DvLPtlkJ6G0eBHKHs33XItYdH1yzANE9LJQmFVsgrjm8x6p7gs9W7MM5dwUx4GSot6%2F0C3ut04ffY9qJJD22TEDOpR9FUbYtZTmCd%2FZu5COYGKCaNLsDsjmFO2kCHZe%2FNkBCMclcnol6jOTKV1onjniD%2B%2F7ixf161ELOK%2Bgh2WV%2BwX%2FncN0CQoOIiHIaM5uS9h5%2F5vw31nO7AQc1m9Jl2yQgrsBD6Xux4tmdz%2FdvmW2yLF00DyLnXmhUqqxWvSwdsmo1c8JmcHGuktvNOqX9QvHns1NMKq4lL0GOqUBzS78R1rRG2McMTqaAhnZkQ7opbMtnjtkAyfKyn9WYZr%2FHiD6AEvS74J2xv%2BHrPjPQ6C%2BctlOFRi%2BisL%2BezFGwdVKetkiDwwjMXfUF68lPSeHk3NLzypa%2FQN4Put%2BgikqeSFR1vNKFRU8EA2QB4ZcaYeZeNpxj7BDcU7r%2BUSG9tYDSOinoDfVK1wYxlbHJ0UsCm2%2B%2BVWbHNXSGaAqOqeffbMLRL7L&X-Amz-Signature=9bae1d205871224828673996bc3761f65c10b8de09f08bc2bce56a49df7ac219&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
