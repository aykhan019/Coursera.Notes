

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPBSHYOQ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T024310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCfsJFg6JDb6yTi6MNx82QA4O2JvuC3QiMbKPuzMvTQ4AIhAIke%2FPGWOiUWIpqlxcsGaxLmIXfxZswLstNfjTyTLAE3Kv8DCDkQABoMNjM3NDIzMTgzODA1IgxA1aSmywiQZV1aEJkq3ANeKNrF%2FEJ1ptjPC8gWo8sfce0C20XXvMPnbBzCVjalspjeMdmCo35FMSTqwYQDWDdfvRqVVI0j3MCcTsoEVGVWI%2Baf1lpHFeHqEyULeCYtQoTOflQme2RjME7ovcF95jt0b7j1Na5FAUwm2q1JLQ9QAUzmq%2BleS0JxZEQGRAhp606shzxm0siHxrb0I9dtufwWY7PzQVnInnZHyAtql27f9dIcL0jZ59a9RLwwMSERL9Td1O3tIB67s%2Bi%2FyDy9ARcv2j8lZe9jUwf9L8szmj2l%2FsIkwsnu66Scl3IeJrH7Yyjc4jggL1LU9e8gKVkBvLJeCz0MuOQXjNf5HEQFDt%2Fiq1IX682YnIRFZbtw5QinapzhqrpFyxqCu4ZMq1y4Dz6WsiQnW%2BDwHyGWTepucHziuk3%2BBE3uPOm7SArAI%2BX45UINBB7kEoXVOpErnRx1CwTAvoTEwfKAM%2BhfQMl%2BayWBGZzcOfGcetn0%2B%2BAcCvrnP8B0%2BY%2FTqosav9vRnmjaXcytHERKjjnaUCeVK%2FAgw97HCYqNaPpJ6sTQ8fBaZtqRyan1nQ2O9wmbq4E4bw95gLBQ6Cuc%2BMT%2FGbJY9h%2F0d2NUnoIk5gzV3FGUO21ARJOj7eGcDYw7aKNjch%2FUQDCkzYq9BjqkAfDiaqlhf%2FcZ6YaM3sY1yqnSSvJxv5PFF0MJ5SK44Lg7OBDMpOKOOnR%2B%2BCovNHY4UsGEy6Na6YVpfqAWVKvkyzJy29xrdhtlldWoB5LdxczcEOyRoRjKF5JkObMRMDeDUfwUT9JhQjCo16Je8BvK1BpyCR7W7r7ji1R96%2F3QOHoB8YAXZWCEI3jBSoMzy4FuHEe%2Bk5Z8gKO%2BXb1FkKxFTn8XPMUb&X-Amz-Signature=880fc3dc89ef6b380ebc68292e2394aa5f14fb1ae72d568f2f9f7133bb8d28dd&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPBSHYOQ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T024310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCfsJFg6JDb6yTi6MNx82QA4O2JvuC3QiMbKPuzMvTQ4AIhAIke%2FPGWOiUWIpqlxcsGaxLmIXfxZswLstNfjTyTLAE3Kv8DCDkQABoMNjM3NDIzMTgzODA1IgxA1aSmywiQZV1aEJkq3ANeKNrF%2FEJ1ptjPC8gWo8sfce0C20XXvMPnbBzCVjalspjeMdmCo35FMSTqwYQDWDdfvRqVVI0j3MCcTsoEVGVWI%2Baf1lpHFeHqEyULeCYtQoTOflQme2RjME7ovcF95jt0b7j1Na5FAUwm2q1JLQ9QAUzmq%2BleS0JxZEQGRAhp606shzxm0siHxrb0I9dtufwWY7PzQVnInnZHyAtql27f9dIcL0jZ59a9RLwwMSERL9Td1O3tIB67s%2Bi%2FyDy9ARcv2j8lZe9jUwf9L8szmj2l%2FsIkwsnu66Scl3IeJrH7Yyjc4jggL1LU9e8gKVkBvLJeCz0MuOQXjNf5HEQFDt%2Fiq1IX682YnIRFZbtw5QinapzhqrpFyxqCu4ZMq1y4Dz6WsiQnW%2BDwHyGWTepucHziuk3%2BBE3uPOm7SArAI%2BX45UINBB7kEoXVOpErnRx1CwTAvoTEwfKAM%2BhfQMl%2BayWBGZzcOfGcetn0%2B%2BAcCvrnP8B0%2BY%2FTqosav9vRnmjaXcytHERKjjnaUCeVK%2FAgw97HCYqNaPpJ6sTQ8fBaZtqRyan1nQ2O9wmbq4E4bw95gLBQ6Cuc%2BMT%2FGbJY9h%2F0d2NUnoIk5gzV3FGUO21ARJOj7eGcDYw7aKNjch%2FUQDCkzYq9BjqkAfDiaqlhf%2FcZ6YaM3sY1yqnSSvJxv5PFF0MJ5SK44Lg7OBDMpOKOOnR%2B%2BCovNHY4UsGEy6Na6YVpfqAWVKvkyzJy29xrdhtlldWoB5LdxczcEOyRoRjKF5JkObMRMDeDUfwUT9JhQjCo16Je8BvK1BpyCR7W7r7ji1R96%2F3QOHoB8YAXZWCEI3jBSoMzy4FuHEe%2Bk5Z8gKO%2BXb1FkKxFTn8XPMUb&X-Amz-Signature=3057d6f84dccd5261068b414509abbc3792affb75bb722a6a32c84bd4ed545c0&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPBSHYOQ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T024310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCfsJFg6JDb6yTi6MNx82QA4O2JvuC3QiMbKPuzMvTQ4AIhAIke%2FPGWOiUWIpqlxcsGaxLmIXfxZswLstNfjTyTLAE3Kv8DCDkQABoMNjM3NDIzMTgzODA1IgxA1aSmywiQZV1aEJkq3ANeKNrF%2FEJ1ptjPC8gWo8sfce0C20XXvMPnbBzCVjalspjeMdmCo35FMSTqwYQDWDdfvRqVVI0j3MCcTsoEVGVWI%2Baf1lpHFeHqEyULeCYtQoTOflQme2RjME7ovcF95jt0b7j1Na5FAUwm2q1JLQ9QAUzmq%2BleS0JxZEQGRAhp606shzxm0siHxrb0I9dtufwWY7PzQVnInnZHyAtql27f9dIcL0jZ59a9RLwwMSERL9Td1O3tIB67s%2Bi%2FyDy9ARcv2j8lZe9jUwf9L8szmj2l%2FsIkwsnu66Scl3IeJrH7Yyjc4jggL1LU9e8gKVkBvLJeCz0MuOQXjNf5HEQFDt%2Fiq1IX682YnIRFZbtw5QinapzhqrpFyxqCu4ZMq1y4Dz6WsiQnW%2BDwHyGWTepucHziuk3%2BBE3uPOm7SArAI%2BX45UINBB7kEoXVOpErnRx1CwTAvoTEwfKAM%2BhfQMl%2BayWBGZzcOfGcetn0%2B%2BAcCvrnP8B0%2BY%2FTqosav9vRnmjaXcytHERKjjnaUCeVK%2FAgw97HCYqNaPpJ6sTQ8fBaZtqRyan1nQ2O9wmbq4E4bw95gLBQ6Cuc%2BMT%2FGbJY9h%2F0d2NUnoIk5gzV3FGUO21ARJOj7eGcDYw7aKNjch%2FUQDCkzYq9BjqkAfDiaqlhf%2FcZ6YaM3sY1yqnSSvJxv5PFF0MJ5SK44Lg7OBDMpOKOOnR%2B%2BCovNHY4UsGEy6Na6YVpfqAWVKvkyzJy29xrdhtlldWoB5LdxczcEOyRoRjKF5JkObMRMDeDUfwUT9JhQjCo16Je8BvK1BpyCR7W7r7ji1R96%2F3QOHoB8YAXZWCEI3jBSoMzy4FuHEe%2Bk5Z8gKO%2BXb1FkKxFTn8XPMUb&X-Amz-Signature=95fdaddfaff9d2e73dbd3150d5a2bb844beeb5a865b66489f27b157c0929a1d7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W7OKHBFM%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T024311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIEiajMIp6ug1JVlYsxf%2BdfUURRLbgxn6D6%2FTWmy9yK8ZAiBq6%2FOjOxXrNOdjGtnYEgnmLobJJDG30VJMreHM0MjLxir%2FAwg5EAAaDDYzNzQyMzE4MzgwNSIMqDY7P1rI3qFEqqZ3KtwDsRZcSYUeT1AWpF6TIVkWazvRM9iUycWv%2Fshw58%2Bod04JDBqbqO1znZUPYRAGTI2VPsaygd6AGAW6w6gMHKAsranUNj6qKu1vMpVZBjuc8Jai0CwqTmRkXqIOiNIMOH%2B7AE1rv6owLQQappLT8dgDIpnbdyviWXSSmjuUwtWQjFXDtvd3Za8hvMuP00gKanVCCybgZBNbE5yrWg5F8kRTC%2BAmpKm1ln6flkQSOQgz9petyM3Bu9%2Fp7aA%2F7fXwSyabgPhOw4%2Bciy8I%2FszZbsp6f88pi2kyFg0umLI8LPusIdiLyJcr2ZQCtAjqPazTAnDtRi3nfITV3acZHTyObyl6df%2FAuz1diiidw2jUfJnhq30REAZuwTGT7BOGHWgBLx7tlUfYuSqVGi%2BNFHiBf8CQR6nXurO6XNWSr3v9vUOzdiBM78A93tLDLCSzhUGkgldjJAvSD1D7UdV5GeJHz0s4fqnGBaI7xtPFi7FQYUCoo79WpZqUfYbPwustA6qAbrjZvolTG5kW5xSnjLnJ9UhavtjoCNm15mNawCs8qsmt4baIGwr09w95fbWTdaASLLgtLREsweuhmrXRxngYsOPbz0Q2x4ejKw%2FXMSsHRIEEYlvlEgAmrcML1CKvhbMwpM2KvQY6pgFrsZ2NQ7B1J9o%2BuUzf7qfuzLy8%2BwgnnNQU5oN%2B4Vt3dBNCTkrgyUHuBWWX6mYcakIqu%2F%2BlCZv66c0ZLiC4o%2FsKoTOANDP6NGgph2q6rwVa9TZo1MB%2BfxhM2KUxH0L8%2F5u12kKzfoAxfr7QSHiGuyTbxmFQntOzvj2B44%2Fg%2BpNYixbNkeXoq4GevZBZJitb%2F6Dk7n3h%2FEtLxVMKCzIrRNDS4Z%2B5yEPM&X-Amz-Signature=2ecb34daa8f1d5934aa1dc53045878c4a551ac6851193fc5d2148491e61c03a1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R4QBXBWQ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T024311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIE4W7uI3s1VV40LrWQDWK2gCUAoRwA5Mh56K%2Fnk2RvopAiEA%2FM8RO6wb7zFI67s6XKQ8Qizgv3UJgNBU6a%2FTY3B8VBUq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDE3zlR6L7pii5jLUEircA7IMsL%2F%2FvAkJ8t0iN7IHJ%2BUzH5MtoiRkOP3PQSI0tFg4N%2F1MCC4yHSSQEXJLgkb8njUN%2FEhEdwyjd0M3%2Fd1Vcq2wf9TyqwBJLbfgyjsLkDS6Un1zw9OaV4E1XLQDv%2BsTUkmb3nxG7vSbDBryKzk9i4%2FabxLk1YdjKJHY7ZpnJ5SrzcH2mIELh3HGB9yxU4znoz%2F6uAu%2F9T0DBzUey6AW6sMFMp6FhDWYLZB8iIFi9ZfQcHv894azlHYaZpDjsOAVGOgFpSIJPmiTl6zW2WHTiA1TOzIG1DjHw6edOtrNHm7KYJ4ZB5y3qd5aUlcg0jGwDoDxzjrXZqaKR2NGofKs0%2FKRQUd49HDdlO61tq7sVTUxhgwe%2FHBdnvLu4JHl51iQSmnVjWnUOikicJ0ujCqccwvRJT6p4pRuaL1YY0sEUczDBa04OOQDrRptXadYcMVDGUlc9llZW3YD52PAjqkDB9PgLHrB9jRx8m%2BDJKVG0rGZFu4N9rsUUPagxYkm6XneSEfmHT4MNeGiKsQ1u3Zfdtxq8PcrWz4ZVz4tLJEHUlIoEaZ6foA4JOfaF6esPnykUBX%2BqeKB6nLQUPH3mamgs6z4%2FaW40GlbDVr5II28xLCjyB5ey%2Bu%2FJ%2Fr4CeWwMPrMir0GOqUBqBrKHKhJv459wm0G9ABsdQhwZrgb3maabKIpiBRIjqJe%2BG3Z2y%2FNNsHysCp9Qym4N6rwXzjTIbozJqkB0zYQCCaikpPjWO7%2B9aKEmotHobnLqoXxiLkvi1xM%2Fy9w32I8MHROnFIq8Xh%2FkVDhJ0D3zTBO6CfRGBS6R3wLgMGLbCz%2B0fx0fKYrklVldH7zimWVLL%2BTKmu5vzboCUQOn9mulpT%2FeJmb&X-Amz-Signature=5afb77c9479b28886dcd27a386094599ece3109fb7f6be6ff4c613ac26545fb3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPBSHYOQ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T024310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCfsJFg6JDb6yTi6MNx82QA4O2JvuC3QiMbKPuzMvTQ4AIhAIke%2FPGWOiUWIpqlxcsGaxLmIXfxZswLstNfjTyTLAE3Kv8DCDkQABoMNjM3NDIzMTgzODA1IgxA1aSmywiQZV1aEJkq3ANeKNrF%2FEJ1ptjPC8gWo8sfce0C20XXvMPnbBzCVjalspjeMdmCo35FMSTqwYQDWDdfvRqVVI0j3MCcTsoEVGVWI%2Baf1lpHFeHqEyULeCYtQoTOflQme2RjME7ovcF95jt0b7j1Na5FAUwm2q1JLQ9QAUzmq%2BleS0JxZEQGRAhp606shzxm0siHxrb0I9dtufwWY7PzQVnInnZHyAtql27f9dIcL0jZ59a9RLwwMSERL9Td1O3tIB67s%2Bi%2FyDy9ARcv2j8lZe9jUwf9L8szmj2l%2FsIkwsnu66Scl3IeJrH7Yyjc4jggL1LU9e8gKVkBvLJeCz0MuOQXjNf5HEQFDt%2Fiq1IX682YnIRFZbtw5QinapzhqrpFyxqCu4ZMq1y4Dz6WsiQnW%2BDwHyGWTepucHziuk3%2BBE3uPOm7SArAI%2BX45UINBB7kEoXVOpErnRx1CwTAvoTEwfKAM%2BhfQMl%2BayWBGZzcOfGcetn0%2B%2BAcCvrnP8B0%2BY%2FTqosav9vRnmjaXcytHERKjjnaUCeVK%2FAgw97HCYqNaPpJ6sTQ8fBaZtqRyan1nQ2O9wmbq4E4bw95gLBQ6Cuc%2BMT%2FGbJY9h%2F0d2NUnoIk5gzV3FGUO21ARJOj7eGcDYw7aKNjch%2FUQDCkzYq9BjqkAfDiaqlhf%2FcZ6YaM3sY1yqnSSvJxv5PFF0MJ5SK44Lg7OBDMpOKOOnR%2B%2BCovNHY4UsGEy6Na6YVpfqAWVKvkyzJy29xrdhtlldWoB5LdxczcEOyRoRjKF5JkObMRMDeDUfwUT9JhQjCo16Je8BvK1BpyCR7W7r7ji1R96%2F3QOHoB8YAXZWCEI3jBSoMzy4FuHEe%2Bk5Z8gKO%2BXb1FkKxFTn8XPMUb&X-Amz-Signature=ed4dcbed832ce33ad54fa084425b60391d2ea02fef3a5fa520c4120d7e0feca5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPBSHYOQ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T024311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCfsJFg6JDb6yTi6MNx82QA4O2JvuC3QiMbKPuzMvTQ4AIhAIke%2FPGWOiUWIpqlxcsGaxLmIXfxZswLstNfjTyTLAE3Kv8DCDkQABoMNjM3NDIzMTgzODA1IgxA1aSmywiQZV1aEJkq3ANeKNrF%2FEJ1ptjPC8gWo8sfce0C20XXvMPnbBzCVjalspjeMdmCo35FMSTqwYQDWDdfvRqVVI0j3MCcTsoEVGVWI%2Baf1lpHFeHqEyULeCYtQoTOflQme2RjME7ovcF95jt0b7j1Na5FAUwm2q1JLQ9QAUzmq%2BleS0JxZEQGRAhp606shzxm0siHxrb0I9dtufwWY7PzQVnInnZHyAtql27f9dIcL0jZ59a9RLwwMSERL9Td1O3tIB67s%2Bi%2FyDy9ARcv2j8lZe9jUwf9L8szmj2l%2FsIkwsnu66Scl3IeJrH7Yyjc4jggL1LU9e8gKVkBvLJeCz0MuOQXjNf5HEQFDt%2Fiq1IX682YnIRFZbtw5QinapzhqrpFyxqCu4ZMq1y4Dz6WsiQnW%2BDwHyGWTepucHziuk3%2BBE3uPOm7SArAI%2BX45UINBB7kEoXVOpErnRx1CwTAvoTEwfKAM%2BhfQMl%2BayWBGZzcOfGcetn0%2B%2BAcCvrnP8B0%2BY%2FTqosav9vRnmjaXcytHERKjjnaUCeVK%2FAgw97HCYqNaPpJ6sTQ8fBaZtqRyan1nQ2O9wmbq4E4bw95gLBQ6Cuc%2BMT%2FGbJY9h%2F0d2NUnoIk5gzV3FGUO21ARJOj7eGcDYw7aKNjch%2FUQDCkzYq9BjqkAfDiaqlhf%2FcZ6YaM3sY1yqnSSvJxv5PFF0MJ5SK44Lg7OBDMpOKOOnR%2B%2BCovNHY4UsGEy6Na6YVpfqAWVKvkyzJy29xrdhtlldWoB5LdxczcEOyRoRjKF5JkObMRMDeDUfwUT9JhQjCo16Je8BvK1BpyCR7W7r7ji1R96%2F3QOHoB8YAXZWCEI3jBSoMzy4FuHEe%2Bk5Z8gKO%2BXb1FkKxFTn8XPMUb&X-Amz-Signature=338c99b8dd82e2cbd4290ba55a00bd76ce4309d5be3c690e364dfbe48c3c072f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPBSHYOQ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T024310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCfsJFg6JDb6yTi6MNx82QA4O2JvuC3QiMbKPuzMvTQ4AIhAIke%2FPGWOiUWIpqlxcsGaxLmIXfxZswLstNfjTyTLAE3Kv8DCDkQABoMNjM3NDIzMTgzODA1IgxA1aSmywiQZV1aEJkq3ANeKNrF%2FEJ1ptjPC8gWo8sfce0C20XXvMPnbBzCVjalspjeMdmCo35FMSTqwYQDWDdfvRqVVI0j3MCcTsoEVGVWI%2Baf1lpHFeHqEyULeCYtQoTOflQme2RjME7ovcF95jt0b7j1Na5FAUwm2q1JLQ9QAUzmq%2BleS0JxZEQGRAhp606shzxm0siHxrb0I9dtufwWY7PzQVnInnZHyAtql27f9dIcL0jZ59a9RLwwMSERL9Td1O3tIB67s%2Bi%2FyDy9ARcv2j8lZe9jUwf9L8szmj2l%2FsIkwsnu66Scl3IeJrH7Yyjc4jggL1LU9e8gKVkBvLJeCz0MuOQXjNf5HEQFDt%2Fiq1IX682YnIRFZbtw5QinapzhqrpFyxqCu4ZMq1y4Dz6WsiQnW%2BDwHyGWTepucHziuk3%2BBE3uPOm7SArAI%2BX45UINBB7kEoXVOpErnRx1CwTAvoTEwfKAM%2BhfQMl%2BayWBGZzcOfGcetn0%2B%2BAcCvrnP8B0%2BY%2FTqosav9vRnmjaXcytHERKjjnaUCeVK%2FAgw97HCYqNaPpJ6sTQ8fBaZtqRyan1nQ2O9wmbq4E4bw95gLBQ6Cuc%2BMT%2FGbJY9h%2F0d2NUnoIk5gzV3FGUO21ARJOj7eGcDYw7aKNjch%2FUQDCkzYq9BjqkAfDiaqlhf%2FcZ6YaM3sY1yqnSSvJxv5PFF0MJ5SK44Lg7OBDMpOKOOnR%2B%2BCovNHY4UsGEy6Na6YVpfqAWVKvkyzJy29xrdhtlldWoB5LdxczcEOyRoRjKF5JkObMRMDeDUfwUT9JhQjCo16Je8BvK1BpyCR7W7r7ji1R96%2F3QOHoB8YAXZWCEI3jBSoMzy4FuHEe%2Bk5Z8gKO%2BXb1FkKxFTn8XPMUb&X-Amz-Signature=ad696eb1b8ade91cf4320f19512c4eff1a8bf7d730cd323042ee967451023794&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPBSHYOQ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T024311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCfsJFg6JDb6yTi6MNx82QA4O2JvuC3QiMbKPuzMvTQ4AIhAIke%2FPGWOiUWIpqlxcsGaxLmIXfxZswLstNfjTyTLAE3Kv8DCDkQABoMNjM3NDIzMTgzODA1IgxA1aSmywiQZV1aEJkq3ANeKNrF%2FEJ1ptjPC8gWo8sfce0C20XXvMPnbBzCVjalspjeMdmCo35FMSTqwYQDWDdfvRqVVI0j3MCcTsoEVGVWI%2Baf1lpHFeHqEyULeCYtQoTOflQme2RjME7ovcF95jt0b7j1Na5FAUwm2q1JLQ9QAUzmq%2BleS0JxZEQGRAhp606shzxm0siHxrb0I9dtufwWY7PzQVnInnZHyAtql27f9dIcL0jZ59a9RLwwMSERL9Td1O3tIB67s%2Bi%2FyDy9ARcv2j8lZe9jUwf9L8szmj2l%2FsIkwsnu66Scl3IeJrH7Yyjc4jggL1LU9e8gKVkBvLJeCz0MuOQXjNf5HEQFDt%2Fiq1IX682YnIRFZbtw5QinapzhqrpFyxqCu4ZMq1y4Dz6WsiQnW%2BDwHyGWTepucHziuk3%2BBE3uPOm7SArAI%2BX45UINBB7kEoXVOpErnRx1CwTAvoTEwfKAM%2BhfQMl%2BayWBGZzcOfGcetn0%2B%2BAcCvrnP8B0%2BY%2FTqosav9vRnmjaXcytHERKjjnaUCeVK%2FAgw97HCYqNaPpJ6sTQ8fBaZtqRyan1nQ2O9wmbq4E4bw95gLBQ6Cuc%2BMT%2FGbJY9h%2F0d2NUnoIk5gzV3FGUO21ARJOj7eGcDYw7aKNjch%2FUQDCkzYq9BjqkAfDiaqlhf%2FcZ6YaM3sY1yqnSSvJxv5PFF0MJ5SK44Lg7OBDMpOKOOnR%2B%2BCovNHY4UsGEy6Na6YVpfqAWVKvkyzJy29xrdhtlldWoB5LdxczcEOyRoRjKF5JkObMRMDeDUfwUT9JhQjCo16Je8BvK1BpyCR7W7r7ji1R96%2F3QOHoB8YAXZWCEI3jBSoMzy4FuHEe%2Bk5Z8gKO%2BXb1FkKxFTn8XPMUb&X-Amz-Signature=eb6f4b880d0acec7fdfa8883867455dc027068d7a319d0d6d63731a5e0d6f46f&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
