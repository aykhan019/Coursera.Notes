

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TSETRUTZ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJGMEQCIEiIt46SWttQQdtN4dUcNZEXo8W3o8pB5yMs4F0HT1keAiB4Fc3AGGodWDZxPqEyhijXiv4Y%2F8vFY2%2FgthNuJSEfoyr%2FAwgjEAAaDDYzNzQyMzE4MzgwNSIMLuXw34Dvb5TMt0mvKtwDpW96EoO4USlvW4TyNYT8caLTf%2FvhjvshEoDc%2BUpR2MpicU2fQOhM8RCB3gQHk88VqrvzN5f5LmO%2BROTlPbAbrOLsYGqK6MrEPGw1g0v4CYr%2FN%2FHg5%2BXcOfUYlHI42gecNuiUshHfmYBVnamj2%2BjMSgqWV3OTwX4%2FIfEiqNXmth3hfzQGy20%2BsyUDxFzc677FviHUK%2BRQq9pyVoWgrXeqraMNfiHiemmgIlB4wOy%2BQ%2FUokCH8VWj8V3TtTCdH4QF74VweMOOQI27o2hNq7ds3H8G2DVPyijr9%2B9C5QBewZwmFfqEWaKNJ5nzM1Atc3vkM5Ub9TRn0ONn97dtdAMbY7bmLTZwQvROBbnj5fYrdG9FmYtx8l6Ng%2B5URGi1uyqFEtE8XeFeTjl%2FREEB0jctci3KHgsu%2BpCDFHsOhAHXSgfEzsU4yFLFTIidpqt6FEpCFYj%2FILxO2AydDlT7cW3qfP9rf1jUJvCN4ZzXb8us1jMV0Aigi1c%2Fcaw1aOiGXMiUS4AydXTjFH%2FMoVVZgFP%2FEP6W87qnzIDD%2BvOAPoVZEGe4%2FIrVXe16izhQkkzj%2FGBE11Z31EJHxYF9sKRr9at9M6f9ZWsO0jWGsm3kudtZMr06x6tnY5lX2IaGnOU0wpuqFvQY6pgFyfMo5Q6zku%2BQ%2BSgFmWNkhZByxoqQjs%2FZjoXLV4HhcHgwWikfHPIbypCr%2FDTP9cs7OqHn9rlrHxCVdoFFGXmykPcsVAx8nYS2k%2B%2FfKLwPxM4l66BIx4QTecxkZzGWmBd08zxODToFyolw7Bp5XjNlo4zO5Bq5Z1AoQzRRM%2B0hv8D4dp34vAry4A8YN8hxGR9gwmCmGVMsmeRUSM5ec0D2pXrlOYSbc&X-Amz-Signature=1d383fc6b3f113d27542088e26d549378391776851cde31f6e5317dc2042aab2&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TSETRUTZ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJGMEQCIEiIt46SWttQQdtN4dUcNZEXo8W3o8pB5yMs4F0HT1keAiB4Fc3AGGodWDZxPqEyhijXiv4Y%2F8vFY2%2FgthNuJSEfoyr%2FAwgjEAAaDDYzNzQyMzE4MzgwNSIMLuXw34Dvb5TMt0mvKtwDpW96EoO4USlvW4TyNYT8caLTf%2FvhjvshEoDc%2BUpR2MpicU2fQOhM8RCB3gQHk88VqrvzN5f5LmO%2BROTlPbAbrOLsYGqK6MrEPGw1g0v4CYr%2FN%2FHg5%2BXcOfUYlHI42gecNuiUshHfmYBVnamj2%2BjMSgqWV3OTwX4%2FIfEiqNXmth3hfzQGy20%2BsyUDxFzc677FviHUK%2BRQq9pyVoWgrXeqraMNfiHiemmgIlB4wOy%2BQ%2FUokCH8VWj8V3TtTCdH4QF74VweMOOQI27o2hNq7ds3H8G2DVPyijr9%2B9C5QBewZwmFfqEWaKNJ5nzM1Atc3vkM5Ub9TRn0ONn97dtdAMbY7bmLTZwQvROBbnj5fYrdG9FmYtx8l6Ng%2B5URGi1uyqFEtE8XeFeTjl%2FREEB0jctci3KHgsu%2BpCDFHsOhAHXSgfEzsU4yFLFTIidpqt6FEpCFYj%2FILxO2AydDlT7cW3qfP9rf1jUJvCN4ZzXb8us1jMV0Aigi1c%2Fcaw1aOiGXMiUS4AydXTjFH%2FMoVVZgFP%2FEP6W87qnzIDD%2BvOAPoVZEGe4%2FIrVXe16izhQkkzj%2FGBE11Z31EJHxYF9sKRr9at9M6f9ZWsO0jWGsm3kudtZMr06x6tnY5lX2IaGnOU0wpuqFvQY6pgFyfMo5Q6zku%2BQ%2BSgFmWNkhZByxoqQjs%2FZjoXLV4HhcHgwWikfHPIbypCr%2FDTP9cs7OqHn9rlrHxCVdoFFGXmykPcsVAx8nYS2k%2B%2FfKLwPxM4l66BIx4QTecxkZzGWmBd08zxODToFyolw7Bp5XjNlo4zO5Bq5Z1AoQzRRM%2B0hv8D4dp34vAry4A8YN8hxGR9gwmCmGVMsmeRUSM5ec0D2pXrlOYSbc&X-Amz-Signature=97c5277c694be926828743d65efcca827456c17d18f2a6f1e28810b33dffb53a&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TSETRUTZ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJGMEQCIEiIt46SWttQQdtN4dUcNZEXo8W3o8pB5yMs4F0HT1keAiB4Fc3AGGodWDZxPqEyhijXiv4Y%2F8vFY2%2FgthNuJSEfoyr%2FAwgjEAAaDDYzNzQyMzE4MzgwNSIMLuXw34Dvb5TMt0mvKtwDpW96EoO4USlvW4TyNYT8caLTf%2FvhjvshEoDc%2BUpR2MpicU2fQOhM8RCB3gQHk88VqrvzN5f5LmO%2BROTlPbAbrOLsYGqK6MrEPGw1g0v4CYr%2FN%2FHg5%2BXcOfUYlHI42gecNuiUshHfmYBVnamj2%2BjMSgqWV3OTwX4%2FIfEiqNXmth3hfzQGy20%2BsyUDxFzc677FviHUK%2BRQq9pyVoWgrXeqraMNfiHiemmgIlB4wOy%2BQ%2FUokCH8VWj8V3TtTCdH4QF74VweMOOQI27o2hNq7ds3H8G2DVPyijr9%2B9C5QBewZwmFfqEWaKNJ5nzM1Atc3vkM5Ub9TRn0ONn97dtdAMbY7bmLTZwQvROBbnj5fYrdG9FmYtx8l6Ng%2B5URGi1uyqFEtE8XeFeTjl%2FREEB0jctci3KHgsu%2BpCDFHsOhAHXSgfEzsU4yFLFTIidpqt6FEpCFYj%2FILxO2AydDlT7cW3qfP9rf1jUJvCN4ZzXb8us1jMV0Aigi1c%2Fcaw1aOiGXMiUS4AydXTjFH%2FMoVVZgFP%2FEP6W87qnzIDD%2BvOAPoVZEGe4%2FIrVXe16izhQkkzj%2FGBE11Z31EJHxYF9sKRr9at9M6f9ZWsO0jWGsm3kudtZMr06x6tnY5lX2IaGnOU0wpuqFvQY6pgFyfMo5Q6zku%2BQ%2BSgFmWNkhZByxoqQjs%2FZjoXLV4HhcHgwWikfHPIbypCr%2FDTP9cs7OqHn9rlrHxCVdoFFGXmykPcsVAx8nYS2k%2B%2FfKLwPxM4l66BIx4QTecxkZzGWmBd08zxODToFyolw7Bp5XjNlo4zO5Bq5Z1AoQzRRM%2B0hv8D4dp34vAry4A8YN8hxGR9gwmCmGVMsmeRUSM5ec0D2pXrlOYSbc&X-Amz-Signature=b5931f829548cfb6c41ca2f0b0462b691d86daff6052e5f13c9c5d567e3a27d1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R5FIB3JR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024136Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJGMEQCIDinMLEb0QUZGGqVpjC9UXap3uDcURjqysJaIIHPaR7vAiAGnf%2Fatm5EGXpJ98X8n4%2BWQTsp3dwR2La7BPOUNKyDcir%2FAwgjEAAaDDYzNzQyMzE4MzgwNSIMhQdHvW3UGDk8kpbHKtwDdHawxQN24eCtO0YEhB2lDL2dQiB%2Bn2mTVlgWl6tsRTI2eAAjNI6nEuk%2FqH6Dw0q3SR5DbWoysUeydWRhtOO2OFAaq5l83CqMHwl5njWjdRhbNyelGSIpSdSOhLNcqS0mrgj7c8z5gWOIQrKkbWjiIH%2BJwfgWC4Je1u4gwHiAhT%2BIVT0ktPR4QlT9brpKPDhYKzx6dPNzgMLSQv6%2FXNC%2BXrVrZD39byvHz8DoiLzjgFM%2BecpewyZ2C7nFoELKbkRlREQot%2BCgDlgo4MydSzVcDwvyrEWhnEUFm5t28wBfQj0beVp1PTDzLptPOSwkfZGUXylLYHOgve0KUEWwwkO8LpsmjGVpGjfNreqtw6V%2Fn3GNlLhIHd8HYFdxza5Sos6FMJWLVwr1dJjo0Zb6j%2FQUwFdXUAKo9MAw7%2BP%2B1LtbedckoUM9jCn1O4y1c6q63tdBqGZnCPYa%2FQfhb1dIfyZahPQkv6i6jFx%2BfK7iEGnNHH3LWql3NNjeL4K1xYVEPQZkmP%2FXTzaEzuyNjpcfP3MwbvVS2aBWOafHiMvEBNkfubUxDvqu8UvSvkU9JsfytDMYloXCR6JX%2FgjV9cWasyY%2F6Yo%2Fxy3mC5aSCKESPdiG6dIaSKSH7f1uAoeGf3wwnemFvQY6pgGxQc%2FzBdl%2F6LBXgQZpPerTAJWNm7UVPEN%2BeirO6Oa6pjYCzC1jDazpJl8hgGTgVNVcnVsnjl6vlhcFT2ry4iVLWszDY2DpWvJIihS1bPV4dz2DpxLtXrHqv8T1Dlu5sQoEXzG5Hv0KIRF4monB9CGhQHDZ8Od457UTwmJsjKA3IF5%2BYtmIF9%2FN2yg0Kg7rHkt9VmQotvHzgm%2BzAcuF19wM3po4BCS%2B&X-Amz-Signature=4831fa2f6a33ee2b701f4d9f157b218bfe95dd1e786a92d3ea3a82efe3de7097&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W3FBEOTJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024136Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJGMEQCIEGMWqYIOpkqiSjXzRz4MtfrKvIDi7BUE%2BXWgyJ2y%2BZ6AiA7TKZcsaCgFx2oNiFPnrHYfcUbMHt%2FcK5nw5aBtOSDLir%2FAwgjEAAaDDYzNzQyMzE4MzgwNSIMJE3Lb3hhwzsfaj1VKtwDORzmUZ8VFPW92hXbcXZkWGixj9fETznrBQWaSB2esRuYm89KfFaZtEbHrb%2FnjHVEiFHxBMIysrZTfRdzUeJP0LCd9ThhAvrOMc%2F2Afp6AB6bnTA9C4Mn5MHqsjoER7rojEhW5N8KaWmHo1qYLzpnppJ7Ntc2bYH0uszGuddm4t5yLPrAXtSo2XHOOyhQ7p%2Bc3cusAY6%2BgLsQh%2BZRT0eWP0nrK5oklE3iZhE7b0tGU3GsFSsTJMWIg%2Fzz%2BCc%2B%2Ff6Jb%2Fm4%2FZyw9Xuwn79iJh9yy%2BmDmB3Qq6SeJUp5%2BYsNb7TB8kqOFoH2HaSRiDvCCreUBKAZa5K0rF%2Bwq%2FWGfCev7S5bztesqBzT1ukAm2DBfTCYGsIRl8rtBeeOTVIQ3T6imD7BjyKJv31T6gOsPsEaKnswtxE2LgzXkLjAr20lKpkSWukmk7Aq1jWBi0w%2Bh%2F3zxQPdaNy80Jt2Spl4bgnY63AAWVge%2B3OJByzvcLCjIYEhMrVrcnutPvKMMTVc3N2RWX%2Ft60Hg72WY7b2dthFoyS4yWJwAfaKftPW8zog1ZXeOaVx5s8O7ys3Te%2BpuHksxafii2xn5F4ekke6GIZ05yz7QNf7X0r92iaJDF3kE%2FGkGliJEehy8IeNUO54wiumFvQY6pgEg607%2Bc4OcaF0fSI2uu2WCSsZvE91U55928tvDC8MEzWVzUMtVi0eh6WjNc1YWrhXeheaV3vbBQ%2Bp8OLxSCclNk%2FS%2BxHyfG%2FYKwj7HTa%2BPWCMjF%2BlAeZyDIq4UIhojFPvNMgX90McMNT7qW3iPwjq5htnsALU9qbK3%2BeDZ41CV6Ewxh6ImirdG7wonJjBnL3cTfzHstn6%2BkVhwuNA1%2BQ7e9DbnWsBz&X-Amz-Signature=c7407cf8208214f518ba7e9769859c494caecd23d0f6d9d8881a5cdcef4c2983&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TSETRUTZ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJGMEQCIEiIt46SWttQQdtN4dUcNZEXo8W3o8pB5yMs4F0HT1keAiB4Fc3AGGodWDZxPqEyhijXiv4Y%2F8vFY2%2FgthNuJSEfoyr%2FAwgjEAAaDDYzNzQyMzE4MzgwNSIMLuXw34Dvb5TMt0mvKtwDpW96EoO4USlvW4TyNYT8caLTf%2FvhjvshEoDc%2BUpR2MpicU2fQOhM8RCB3gQHk88VqrvzN5f5LmO%2BROTlPbAbrOLsYGqK6MrEPGw1g0v4CYr%2FN%2FHg5%2BXcOfUYlHI42gecNuiUshHfmYBVnamj2%2BjMSgqWV3OTwX4%2FIfEiqNXmth3hfzQGy20%2BsyUDxFzc677FviHUK%2BRQq9pyVoWgrXeqraMNfiHiemmgIlB4wOy%2BQ%2FUokCH8VWj8V3TtTCdH4QF74VweMOOQI27o2hNq7ds3H8G2DVPyijr9%2B9C5QBewZwmFfqEWaKNJ5nzM1Atc3vkM5Ub9TRn0ONn97dtdAMbY7bmLTZwQvROBbnj5fYrdG9FmYtx8l6Ng%2B5URGi1uyqFEtE8XeFeTjl%2FREEB0jctci3KHgsu%2BpCDFHsOhAHXSgfEzsU4yFLFTIidpqt6FEpCFYj%2FILxO2AydDlT7cW3qfP9rf1jUJvCN4ZzXb8us1jMV0Aigi1c%2Fcaw1aOiGXMiUS4AydXTjFH%2FMoVVZgFP%2FEP6W87qnzIDD%2BvOAPoVZEGe4%2FIrVXe16izhQkkzj%2FGBE11Z31EJHxYF9sKRr9at9M6f9ZWsO0jWGsm3kudtZMr06x6tnY5lX2IaGnOU0wpuqFvQY6pgFyfMo5Q6zku%2BQ%2BSgFmWNkhZByxoqQjs%2FZjoXLV4HhcHgwWikfHPIbypCr%2FDTP9cs7OqHn9rlrHxCVdoFFGXmykPcsVAx8nYS2k%2B%2FfKLwPxM4l66BIx4QTecxkZzGWmBd08zxODToFyolw7Bp5XjNlo4zO5Bq5Z1AoQzRRM%2B0hv8D4dp34vAry4A8YN8hxGR9gwmCmGVMsmeRUSM5ec0D2pXrlOYSbc&X-Amz-Signature=1a36aec3cfa2e4b7ca32aeb20567e6210dcfe29ec7f12cc9e7ad1279f1b6c3db&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TSETRUTZ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJGMEQCIEiIt46SWttQQdtN4dUcNZEXo8W3o8pB5yMs4F0HT1keAiB4Fc3AGGodWDZxPqEyhijXiv4Y%2F8vFY2%2FgthNuJSEfoyr%2FAwgjEAAaDDYzNzQyMzE4MzgwNSIMLuXw34Dvb5TMt0mvKtwDpW96EoO4USlvW4TyNYT8caLTf%2FvhjvshEoDc%2BUpR2MpicU2fQOhM8RCB3gQHk88VqrvzN5f5LmO%2BROTlPbAbrOLsYGqK6MrEPGw1g0v4CYr%2FN%2FHg5%2BXcOfUYlHI42gecNuiUshHfmYBVnamj2%2BjMSgqWV3OTwX4%2FIfEiqNXmth3hfzQGy20%2BsyUDxFzc677FviHUK%2BRQq9pyVoWgrXeqraMNfiHiemmgIlB4wOy%2BQ%2FUokCH8VWj8V3TtTCdH4QF74VweMOOQI27o2hNq7ds3H8G2DVPyijr9%2B9C5QBewZwmFfqEWaKNJ5nzM1Atc3vkM5Ub9TRn0ONn97dtdAMbY7bmLTZwQvROBbnj5fYrdG9FmYtx8l6Ng%2B5URGi1uyqFEtE8XeFeTjl%2FREEB0jctci3KHgsu%2BpCDFHsOhAHXSgfEzsU4yFLFTIidpqt6FEpCFYj%2FILxO2AydDlT7cW3qfP9rf1jUJvCN4ZzXb8us1jMV0Aigi1c%2Fcaw1aOiGXMiUS4AydXTjFH%2FMoVVZgFP%2FEP6W87qnzIDD%2BvOAPoVZEGe4%2FIrVXe16izhQkkzj%2FGBE11Z31EJHxYF9sKRr9at9M6f9ZWsO0jWGsm3kudtZMr06x6tnY5lX2IaGnOU0wpuqFvQY6pgFyfMo5Q6zku%2BQ%2BSgFmWNkhZByxoqQjs%2FZjoXLV4HhcHgwWikfHPIbypCr%2FDTP9cs7OqHn9rlrHxCVdoFFGXmykPcsVAx8nYS2k%2B%2FfKLwPxM4l66BIx4QTecxkZzGWmBd08zxODToFyolw7Bp5XjNlo4zO5Bq5Z1AoQzRRM%2B0hv8D4dp34vAry4A8YN8hxGR9gwmCmGVMsmeRUSM5ec0D2pXrlOYSbc&X-Amz-Signature=6e66db147db3ee456f1edef5c99000d247927d5ed7aead644f49aa817de4ad0f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TSETRUTZ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJGMEQCIEiIt46SWttQQdtN4dUcNZEXo8W3o8pB5yMs4F0HT1keAiB4Fc3AGGodWDZxPqEyhijXiv4Y%2F8vFY2%2FgthNuJSEfoyr%2FAwgjEAAaDDYzNzQyMzE4MzgwNSIMLuXw34Dvb5TMt0mvKtwDpW96EoO4USlvW4TyNYT8caLTf%2FvhjvshEoDc%2BUpR2MpicU2fQOhM8RCB3gQHk88VqrvzN5f5LmO%2BROTlPbAbrOLsYGqK6MrEPGw1g0v4CYr%2FN%2FHg5%2BXcOfUYlHI42gecNuiUshHfmYBVnamj2%2BjMSgqWV3OTwX4%2FIfEiqNXmth3hfzQGy20%2BsyUDxFzc677FviHUK%2BRQq9pyVoWgrXeqraMNfiHiemmgIlB4wOy%2BQ%2FUokCH8VWj8V3TtTCdH4QF74VweMOOQI27o2hNq7ds3H8G2DVPyijr9%2B9C5QBewZwmFfqEWaKNJ5nzM1Atc3vkM5Ub9TRn0ONn97dtdAMbY7bmLTZwQvROBbnj5fYrdG9FmYtx8l6Ng%2B5URGi1uyqFEtE8XeFeTjl%2FREEB0jctci3KHgsu%2BpCDFHsOhAHXSgfEzsU4yFLFTIidpqt6FEpCFYj%2FILxO2AydDlT7cW3qfP9rf1jUJvCN4ZzXb8us1jMV0Aigi1c%2Fcaw1aOiGXMiUS4AydXTjFH%2FMoVVZgFP%2FEP6W87qnzIDD%2BvOAPoVZEGe4%2FIrVXe16izhQkkzj%2FGBE11Z31EJHxYF9sKRr9at9M6f9ZWsO0jWGsm3kudtZMr06x6tnY5lX2IaGnOU0wpuqFvQY6pgFyfMo5Q6zku%2BQ%2BSgFmWNkhZByxoqQjs%2FZjoXLV4HhcHgwWikfHPIbypCr%2FDTP9cs7OqHn9rlrHxCVdoFFGXmykPcsVAx8nYS2k%2B%2FfKLwPxM4l66BIx4QTecxkZzGWmBd08zxODToFyolw7Bp5XjNlo4zO5Bq5Z1AoQzRRM%2B0hv8D4dp34vAry4A8YN8hxGR9gwmCmGVMsmeRUSM5ec0D2pXrlOYSbc&X-Amz-Signature=00058fd1ddfaf2f2f2fe0a3aef63f2306e8c1664fd92af96db83f793d92d1845&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TSETRUTZ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJGMEQCIEiIt46SWttQQdtN4dUcNZEXo8W3o8pB5yMs4F0HT1keAiB4Fc3AGGodWDZxPqEyhijXiv4Y%2F8vFY2%2FgthNuJSEfoyr%2FAwgjEAAaDDYzNzQyMzE4MzgwNSIMLuXw34Dvb5TMt0mvKtwDpW96EoO4USlvW4TyNYT8caLTf%2FvhjvshEoDc%2BUpR2MpicU2fQOhM8RCB3gQHk88VqrvzN5f5LmO%2BROTlPbAbrOLsYGqK6MrEPGw1g0v4CYr%2FN%2FHg5%2BXcOfUYlHI42gecNuiUshHfmYBVnamj2%2BjMSgqWV3OTwX4%2FIfEiqNXmth3hfzQGy20%2BsyUDxFzc677FviHUK%2BRQq9pyVoWgrXeqraMNfiHiemmgIlB4wOy%2BQ%2FUokCH8VWj8V3TtTCdH4QF74VweMOOQI27o2hNq7ds3H8G2DVPyijr9%2B9C5QBewZwmFfqEWaKNJ5nzM1Atc3vkM5Ub9TRn0ONn97dtdAMbY7bmLTZwQvROBbnj5fYrdG9FmYtx8l6Ng%2B5URGi1uyqFEtE8XeFeTjl%2FREEB0jctci3KHgsu%2BpCDFHsOhAHXSgfEzsU4yFLFTIidpqt6FEpCFYj%2FILxO2AydDlT7cW3qfP9rf1jUJvCN4ZzXb8us1jMV0Aigi1c%2Fcaw1aOiGXMiUS4AydXTjFH%2FMoVVZgFP%2FEP6W87qnzIDD%2BvOAPoVZEGe4%2FIrVXe16izhQkkzj%2FGBE11Z31EJHxYF9sKRr9at9M6f9ZWsO0jWGsm3kudtZMr06x6tnY5lX2IaGnOU0wpuqFvQY6pgFyfMo5Q6zku%2BQ%2BSgFmWNkhZByxoqQjs%2FZjoXLV4HhcHgwWikfHPIbypCr%2FDTP9cs7OqHn9rlrHxCVdoFFGXmykPcsVAx8nYS2k%2B%2FfKLwPxM4l66BIx4QTecxkZzGWmBd08zxODToFyolw7Bp5XjNlo4zO5Bq5Z1AoQzRRM%2B0hv8D4dp34vAry4A8YN8hxGR9gwmCmGVMsmeRUSM5ec0D2pXrlOYSbc&X-Amz-Signature=6aff9c88ec07ab7640b5aee66556b3416e9c8d483d61a63de375e302f6cf64b3&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
