

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WEV6ER4K%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211233Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCZ8F97EG1dnD7cYr72rEakNHye2uv6i9GuKXAdNq1%2FAgIgZUTkLhbZHBPSooKQ3Wj5IqS8tAE63FnMmgNTDsnv0LEqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDInXXn4UDal5qMCAICrcA0JagKdrOBCYbo%2Bqm%2BccP7flZn0e6MtA527sYjjaPchdu5ikojuDOyLqxADQeIzW1TWadG1gDamwIC9QUvg70lVbNONO12U1%2FKS7LwVm%2BZQm94W604ppkBCDZG4xxA3NJsayA52zIafiYA%2BvizivW%2BSmPKK7CaG10k5LhtSNsO9VqAUrnbAWdJoc8BCkYHuK55%2B0v%2F7OAdFiiHqFwuQyevZZ4k4p85AObga9bDx0F%2BM8zrmWxg4hiYDp8WWLhgN%2BO4z6MgTOI3w%2BUvZM8Pp17TEFhCszuXMU5f3Csny7TL0uW7ayBb%2BVgdgGf8SloCWd7F2tBKVVQ%2B27LyWLtyQOs8uHTUzJHzcgzMwLmhdZhUol8rxJme4EAy3wLk94TOC%2F%2B0zkvRrPVdh0ztZJIxpeuBBGydCZrU1a3M8JphisQ81zL1OezdIS4rhL0yvXB23s9ZHI5Fupyyxzp1dDDk43L6JMowVpEGOiuMQNWbTYM%2BXVzuW6TqGEXa7%2FPc2huDidtzaGIKLJjsuNTa91gpshaNXP%2FK4t2XhRL3ov5tve1hPnpEATPtMElop0%2FI9Mo7bagcHbyEPCcCyZsTREQHV4Y66alnItjH%2B7uViY9y8Ml3jXt1As3jTKLFQOQ5LjMKXl%2FrwGOqUBoCMIFTBGR2c3AYBI5lcBfgOq075CC4Bm3I8P11hXCXAtgzRnH1yvZyawsdxyiTCJvVyVPwUU8wup4ipa6VNhJCK3gjXHSMOLOtJJR19LZxZzZAGu8x4PkDmNeY7kb2eBsz5NPaPxERtfpnPUfkVJwW2RIo5uGOXpHE4U%2F2UZRL3wF8rn1xcAGkeKFLRLJKnZLXYJcdIwMFwm2FlFRafe2FClg80M&X-Amz-Signature=1ab5087c626bbcd36fde80c247e78447bc55f257a2d1c735850a0f76855e988b&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WEV6ER4K%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211232Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCZ8F97EG1dnD7cYr72rEakNHye2uv6i9GuKXAdNq1%2FAgIgZUTkLhbZHBPSooKQ3Wj5IqS8tAE63FnMmgNTDsnv0LEqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDInXXn4UDal5qMCAICrcA0JagKdrOBCYbo%2Bqm%2BccP7flZn0e6MtA527sYjjaPchdu5ikojuDOyLqxADQeIzW1TWadG1gDamwIC9QUvg70lVbNONO12U1%2FKS7LwVm%2BZQm94W604ppkBCDZG4xxA3NJsayA52zIafiYA%2BvizivW%2BSmPKK7CaG10k5LhtSNsO9VqAUrnbAWdJoc8BCkYHuK55%2B0v%2F7OAdFiiHqFwuQyevZZ4k4p85AObga9bDx0F%2BM8zrmWxg4hiYDp8WWLhgN%2BO4z6MgTOI3w%2BUvZM8Pp17TEFhCszuXMU5f3Csny7TL0uW7ayBb%2BVgdgGf8SloCWd7F2tBKVVQ%2B27LyWLtyQOs8uHTUzJHzcgzMwLmhdZhUol8rxJme4EAy3wLk94TOC%2F%2B0zkvRrPVdh0ztZJIxpeuBBGydCZrU1a3M8JphisQ81zL1OezdIS4rhL0yvXB23s9ZHI5Fupyyxzp1dDDk43L6JMowVpEGOiuMQNWbTYM%2BXVzuW6TqGEXa7%2FPc2huDidtzaGIKLJjsuNTa91gpshaNXP%2FK4t2XhRL3ov5tve1hPnpEATPtMElop0%2FI9Mo7bagcHbyEPCcCyZsTREQHV4Y66alnItjH%2B7uViY9y8Ml3jXt1As3jTKLFQOQ5LjMKXl%2FrwGOqUBoCMIFTBGR2c3AYBI5lcBfgOq075CC4Bm3I8P11hXCXAtgzRnH1yvZyawsdxyiTCJvVyVPwUU8wup4ipa6VNhJCK3gjXHSMOLOtJJR19LZxZzZAGu8x4PkDmNeY7kb2eBsz5NPaPxERtfpnPUfkVJwW2RIo5uGOXpHE4U%2F2UZRL3wF8rn1xcAGkeKFLRLJKnZLXYJcdIwMFwm2FlFRafe2FClg80M&X-Amz-Signature=cd570f062ff28a172b4e2303209df879b7df17ed3dcc6784e28c4fd21251430a&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WEV6ER4K%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211233Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCZ8F97EG1dnD7cYr72rEakNHye2uv6i9GuKXAdNq1%2FAgIgZUTkLhbZHBPSooKQ3Wj5IqS8tAE63FnMmgNTDsnv0LEqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDInXXn4UDal5qMCAICrcA0JagKdrOBCYbo%2Bqm%2BccP7flZn0e6MtA527sYjjaPchdu5ikojuDOyLqxADQeIzW1TWadG1gDamwIC9QUvg70lVbNONO12U1%2FKS7LwVm%2BZQm94W604ppkBCDZG4xxA3NJsayA52zIafiYA%2BvizivW%2BSmPKK7CaG10k5LhtSNsO9VqAUrnbAWdJoc8BCkYHuK55%2B0v%2F7OAdFiiHqFwuQyevZZ4k4p85AObga9bDx0F%2BM8zrmWxg4hiYDp8WWLhgN%2BO4z6MgTOI3w%2BUvZM8Pp17TEFhCszuXMU5f3Csny7TL0uW7ayBb%2BVgdgGf8SloCWd7F2tBKVVQ%2B27LyWLtyQOs8uHTUzJHzcgzMwLmhdZhUol8rxJme4EAy3wLk94TOC%2F%2B0zkvRrPVdh0ztZJIxpeuBBGydCZrU1a3M8JphisQ81zL1OezdIS4rhL0yvXB23s9ZHI5Fupyyxzp1dDDk43L6JMowVpEGOiuMQNWbTYM%2BXVzuW6TqGEXa7%2FPc2huDidtzaGIKLJjsuNTa91gpshaNXP%2FK4t2XhRL3ov5tve1hPnpEATPtMElop0%2FI9Mo7bagcHbyEPCcCyZsTREQHV4Y66alnItjH%2B7uViY9y8Ml3jXt1As3jTKLFQOQ5LjMKXl%2FrwGOqUBoCMIFTBGR2c3AYBI5lcBfgOq075CC4Bm3I8P11hXCXAtgzRnH1yvZyawsdxyiTCJvVyVPwUU8wup4ipa6VNhJCK3gjXHSMOLOtJJR19LZxZzZAGu8x4PkDmNeY7kb2eBsz5NPaPxERtfpnPUfkVJwW2RIo5uGOXpHE4U%2F2UZRL3wF8rn1xcAGkeKFLRLJKnZLXYJcdIwMFwm2FlFRafe2FClg80M&X-Amz-Signature=b1342e347d3ee169202235452c42e45c7bd0dc440adb540e4c1785886adbf114&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6LSAZK7%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211233Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCoCnimzWUj2qw4eANfwP2aUPAGKMlCfNue3fhNlv5aTwIhAPOAeJjbYbwE%2BYeG2WCPr%2FPIQeSLvrXEiQhQh7PIlY7UKogECPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz1pg2xUKhHc2LNRckq3APwq4lQ7%2F2D0HXzWT6PVpLs4LohWNsKrb1VWRRNtsGV7t7lkq1WZY8wUVER78f6nRUXfvTpSjtfTqpPDvva6C7rZc5PZW8G853BTERDt5TKg2S96Uoeb%2FDE9Q34l5AU6ls8EVpiTcZ%2BP3oo18fkyAepGNG5xWkQkP611ldeOl1xPbggP19wWwUNX4hnJw590sa9Fkd8apJ%2BJkYjU4MnYO2dyA6ZDjzd5oAkFfz4O7r4MYrQAJtqDbThUVK1smaNsOyDDJ9TFcEe6MlGZdh8pAKiqro4Y10PMzZT9XS9AxTFZPFZNhjWHJyeelBF7d3rpBU6bajrSiTh0IjLWaDBx3e3aNwKLZF%2FA3Q8feZiGmcj%2FccCoK7oPInQIvUCIOQ%2B8%2BZtQCIQAsVvLnCbuQsrXvPGPELlYHq%2BavlS61m5Mdjl2FifGu1yLb66CUc1LrVBYfzQOPObTIVXmVPp5h0Qg%2BuNGALYmXSHf%2F7ZrzxIFmTYkyeLsvPZs2ijjzTsthc9ZyWp15LaPb4F3Sxg0Iytr1pv7QpxGhFurG3VB9O5F%2FE2rcPdFn789qwIBpq%2BZMTZEkRjGtVSXXrlZzThtQr4cUlf6ZYqvw4N%2BfabG4ptHlLSdMeKidXM9xq6wGyVGzDQgP%2B8BjqkAUNBbMgeL9U6EIp7R8YlwL7v3KBdWSJbi62C%2BazC5wnBjhXNrw3rPdeDS2NClLj6ixqDzt9bKLmAEhJdDM6UufAl1TpAuCx7zWr5WsOalwV%2FXBHX4IpJExoGujGP%2Fmu30BXN1OVJgFpoarHKFZj2sf5OaZWU2QXEgAq5ejEbRhS1vgq9AfuzGNp0MU5RoRkdYjY%2BaUj11SghT4icbwVmfaNhqdSh&X-Amz-Signature=608f22d75a695d2c7ca1677aca97d2b0289040dbe144aa0a259dbb60dac68c19&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TFVAVBNM%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211233Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEIC9hkHxanv7khj%2FMzLff42iA5aA1fg1Wz85T0Ij4CNAiBZQlAD1WA4LiaAV40vphmRjXTwlHzwmzyrPdYt%2BLKKIiqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTNljm6Cno6L8hZkWKtwD%2FU9%2BEVhNndiH8abFPWKo0ZnVituCqAj6UZqovhsDQRhqIYxSND5kuzdEyo5KiAq9bOqDJ7djnpygOwDgGDQhaZkfYYyTAeH4eUbbkzegSh8VQJjVIhVZQIZu8wXjXZTWkvy%2FsojxPNkvi%2F%2FIWTsiTKagqUeRE4hrKZv3e%2FZxHFY0wQxFEWRZvMP%2FSpa8JLtfsJ1g12oIM%2FKh%2FL11kaH5O7YFIXI2ktzZ7agMQfCyrvgzyThL%2Bybjg%2BYJg8GSSpLOXBBk6SyZpuBOw6wITzQIC4vy4Q2lBXIDgwiiK2hofA6fvT%2FkTTB%2B%2FeWah3agNiBJh12lkxGWeOAymScK4hLHhIy2YLIw9DrklbXNhssEAwkDESm3awv6oQdLzLGGfd8TRTj1n%2BiWW84HKp4j3YsbTEcLVWb0HVkj7wBp%2B%2Bngr03SggspiqG9A4EuciafgSbTOoOnKYzRTHVI8W7knzsaaWZCoiiRLj736y6%2Fr38ydwmei2QR7FDeyQVjQtA7z8uiCz76B3ToVYdhFj1wgMs9Sy%2BxezOKUQk4qpg6E5996DUrcw90BTpVfsDY9YF5x9fNZwx1O26utFTJB9W5fF%2Fa0dedOtrPrSjCt1eWtK8HC6pNW7bWEhptwlHtIgAwnuL%2BvAY6pgGu8TDFx8RGQLFz3QORAKzRRxL0DUaGRLHgWEC16lrThJdA7yM4FSCV9TqAKc8dMW0a1c2ihNWtOlHf9Uy8XhrBimEnenT%2FaobiCYHb%2BY123lz9e8W5C%2FeddSAgigmmnQ6G4O%2FuG37vGdXLnchmlUnGhXnv2nvk8q62X4nTdKbb3LP%2BO8%2FErhaU2ngB0l7d8WrCRN69m3gA3dRCfFw7u%2FuH%2Boun8VsF&X-Amz-Signature=0e6e5038780d7deb6a3dc49a288d6f4334169b8e9d41fe7cf34d9aea8cd845a4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WEV6ER4K%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211233Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCZ8F97EG1dnD7cYr72rEakNHye2uv6i9GuKXAdNq1%2FAgIgZUTkLhbZHBPSooKQ3Wj5IqS8tAE63FnMmgNTDsnv0LEqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDInXXn4UDal5qMCAICrcA0JagKdrOBCYbo%2Bqm%2BccP7flZn0e6MtA527sYjjaPchdu5ikojuDOyLqxADQeIzW1TWadG1gDamwIC9QUvg70lVbNONO12U1%2FKS7LwVm%2BZQm94W604ppkBCDZG4xxA3NJsayA52zIafiYA%2BvizivW%2BSmPKK7CaG10k5LhtSNsO9VqAUrnbAWdJoc8BCkYHuK55%2B0v%2F7OAdFiiHqFwuQyevZZ4k4p85AObga9bDx0F%2BM8zrmWxg4hiYDp8WWLhgN%2BO4z6MgTOI3w%2BUvZM8Pp17TEFhCszuXMU5f3Csny7TL0uW7ayBb%2BVgdgGf8SloCWd7F2tBKVVQ%2B27LyWLtyQOs8uHTUzJHzcgzMwLmhdZhUol8rxJme4EAy3wLk94TOC%2F%2B0zkvRrPVdh0ztZJIxpeuBBGydCZrU1a3M8JphisQ81zL1OezdIS4rhL0yvXB23s9ZHI5Fupyyxzp1dDDk43L6JMowVpEGOiuMQNWbTYM%2BXVzuW6TqGEXa7%2FPc2huDidtzaGIKLJjsuNTa91gpshaNXP%2FK4t2XhRL3ov5tve1hPnpEATPtMElop0%2FI9Mo7bagcHbyEPCcCyZsTREQHV4Y66alnItjH%2B7uViY9y8Ml3jXt1As3jTKLFQOQ5LjMKXl%2FrwGOqUBoCMIFTBGR2c3AYBI5lcBfgOq075CC4Bm3I8P11hXCXAtgzRnH1yvZyawsdxyiTCJvVyVPwUU8wup4ipa6VNhJCK3gjXHSMOLOtJJR19LZxZzZAGu8x4PkDmNeY7kb2eBsz5NPaPxERtfpnPUfkVJwW2RIo5uGOXpHE4U%2F2UZRL3wF8rn1xcAGkeKFLRLJKnZLXYJcdIwMFwm2FlFRafe2FClg80M&X-Amz-Signature=ea3ee80e5a8b15a5e50ca4a3d0ab66588e3544a7370acf17d7ded6a2e8d038e1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WEV6ER4K%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211233Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCZ8F97EG1dnD7cYr72rEakNHye2uv6i9GuKXAdNq1%2FAgIgZUTkLhbZHBPSooKQ3Wj5IqS8tAE63FnMmgNTDsnv0LEqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDInXXn4UDal5qMCAICrcA0JagKdrOBCYbo%2Bqm%2BccP7flZn0e6MtA527sYjjaPchdu5ikojuDOyLqxADQeIzW1TWadG1gDamwIC9QUvg70lVbNONO12U1%2FKS7LwVm%2BZQm94W604ppkBCDZG4xxA3NJsayA52zIafiYA%2BvizivW%2BSmPKK7CaG10k5LhtSNsO9VqAUrnbAWdJoc8BCkYHuK55%2B0v%2F7OAdFiiHqFwuQyevZZ4k4p85AObga9bDx0F%2BM8zrmWxg4hiYDp8WWLhgN%2BO4z6MgTOI3w%2BUvZM8Pp17TEFhCszuXMU5f3Csny7TL0uW7ayBb%2BVgdgGf8SloCWd7F2tBKVVQ%2B27LyWLtyQOs8uHTUzJHzcgzMwLmhdZhUol8rxJme4EAy3wLk94TOC%2F%2B0zkvRrPVdh0ztZJIxpeuBBGydCZrU1a3M8JphisQ81zL1OezdIS4rhL0yvXB23s9ZHI5Fupyyxzp1dDDk43L6JMowVpEGOiuMQNWbTYM%2BXVzuW6TqGEXa7%2FPc2huDidtzaGIKLJjsuNTa91gpshaNXP%2FK4t2XhRL3ov5tve1hPnpEATPtMElop0%2FI9Mo7bagcHbyEPCcCyZsTREQHV4Y66alnItjH%2B7uViY9y8Ml3jXt1As3jTKLFQOQ5LjMKXl%2FrwGOqUBoCMIFTBGR2c3AYBI5lcBfgOq075CC4Bm3I8P11hXCXAtgzRnH1yvZyawsdxyiTCJvVyVPwUU8wup4ipa6VNhJCK3gjXHSMOLOtJJR19LZxZzZAGu8x4PkDmNeY7kb2eBsz5NPaPxERtfpnPUfkVJwW2RIo5uGOXpHE4U%2F2UZRL3wF8rn1xcAGkeKFLRLJKnZLXYJcdIwMFwm2FlFRafe2FClg80M&X-Amz-Signature=dbaeeec6151cb243db34254fc96ab24d63794713581af43f744cbf038daf262c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WEV6ER4K%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211233Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCZ8F97EG1dnD7cYr72rEakNHye2uv6i9GuKXAdNq1%2FAgIgZUTkLhbZHBPSooKQ3Wj5IqS8tAE63FnMmgNTDsnv0LEqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDInXXn4UDal5qMCAICrcA0JagKdrOBCYbo%2Bqm%2BccP7flZn0e6MtA527sYjjaPchdu5ikojuDOyLqxADQeIzW1TWadG1gDamwIC9QUvg70lVbNONO12U1%2FKS7LwVm%2BZQm94W604ppkBCDZG4xxA3NJsayA52zIafiYA%2BvizivW%2BSmPKK7CaG10k5LhtSNsO9VqAUrnbAWdJoc8BCkYHuK55%2B0v%2F7OAdFiiHqFwuQyevZZ4k4p85AObga9bDx0F%2BM8zrmWxg4hiYDp8WWLhgN%2BO4z6MgTOI3w%2BUvZM8Pp17TEFhCszuXMU5f3Csny7TL0uW7ayBb%2BVgdgGf8SloCWd7F2tBKVVQ%2B27LyWLtyQOs8uHTUzJHzcgzMwLmhdZhUol8rxJme4EAy3wLk94TOC%2F%2B0zkvRrPVdh0ztZJIxpeuBBGydCZrU1a3M8JphisQ81zL1OezdIS4rhL0yvXB23s9ZHI5Fupyyxzp1dDDk43L6JMowVpEGOiuMQNWbTYM%2BXVzuW6TqGEXa7%2FPc2huDidtzaGIKLJjsuNTa91gpshaNXP%2FK4t2XhRL3ov5tve1hPnpEATPtMElop0%2FI9Mo7bagcHbyEPCcCyZsTREQHV4Y66alnItjH%2B7uViY9y8Ml3jXt1As3jTKLFQOQ5LjMKXl%2FrwGOqUBoCMIFTBGR2c3AYBI5lcBfgOq075CC4Bm3I8P11hXCXAtgzRnH1yvZyawsdxyiTCJvVyVPwUU8wup4ipa6VNhJCK3gjXHSMOLOtJJR19LZxZzZAGu8x4PkDmNeY7kb2eBsz5NPaPxERtfpnPUfkVJwW2RIo5uGOXpHE4U%2F2UZRL3wF8rn1xcAGkeKFLRLJKnZLXYJcdIwMFwm2FlFRafe2FClg80M&X-Amz-Signature=f16a5b2d1f83487a9f74cea2b3eb0fca0790d3b63c17095659643cfb76e823e0&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WEV6ER4K%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211233Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCZ8F97EG1dnD7cYr72rEakNHye2uv6i9GuKXAdNq1%2FAgIgZUTkLhbZHBPSooKQ3Wj5IqS8tAE63FnMmgNTDsnv0LEqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDInXXn4UDal5qMCAICrcA0JagKdrOBCYbo%2Bqm%2BccP7flZn0e6MtA527sYjjaPchdu5ikojuDOyLqxADQeIzW1TWadG1gDamwIC9QUvg70lVbNONO12U1%2FKS7LwVm%2BZQm94W604ppkBCDZG4xxA3NJsayA52zIafiYA%2BvizivW%2BSmPKK7CaG10k5LhtSNsO9VqAUrnbAWdJoc8BCkYHuK55%2B0v%2F7OAdFiiHqFwuQyevZZ4k4p85AObga9bDx0F%2BM8zrmWxg4hiYDp8WWLhgN%2BO4z6MgTOI3w%2BUvZM8Pp17TEFhCszuXMU5f3Csny7TL0uW7ayBb%2BVgdgGf8SloCWd7F2tBKVVQ%2B27LyWLtyQOs8uHTUzJHzcgzMwLmhdZhUol8rxJme4EAy3wLk94TOC%2F%2B0zkvRrPVdh0ztZJIxpeuBBGydCZrU1a3M8JphisQ81zL1OezdIS4rhL0yvXB23s9ZHI5Fupyyxzp1dDDk43L6JMowVpEGOiuMQNWbTYM%2BXVzuW6TqGEXa7%2FPc2huDidtzaGIKLJjsuNTa91gpshaNXP%2FK4t2XhRL3ov5tve1hPnpEATPtMElop0%2FI9Mo7bagcHbyEPCcCyZsTREQHV4Y66alnItjH%2B7uViY9y8Ml3jXt1As3jTKLFQOQ5LjMKXl%2FrwGOqUBoCMIFTBGR2c3AYBI5lcBfgOq075CC4Bm3I8P11hXCXAtgzRnH1yvZyawsdxyiTCJvVyVPwUU8wup4ipa6VNhJCK3gjXHSMOLOtJJR19LZxZzZAGu8x4PkDmNeY7kb2eBsz5NPaPxERtfpnPUfkVJwW2RIo5uGOXpHE4U%2F2UZRL3wF8rn1xcAGkeKFLRLJKnZLXYJcdIwMFwm2FlFRafe2FClg80M&X-Amz-Signature=7d707bd31a537a951b721155cd9aab8d9a12fcb55dbf1b4584d7b58c642e2e4f&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
