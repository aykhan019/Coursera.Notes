

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QWVMIEWE%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIQD7BvZYRtXnsyFBSt4LeDG4FVpl4%2B6H3Rfs963mxYSOrgIgRBmG5kRniEW5hT7wA49dI2UbmRnaCJST2pGO02squsEq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDKFo5CAzjVX98fmkoCrcAzxRqWmHhzN7jgP%2B41fQ7JBjNsRjmqg12iDDk7SKwbfqYySEPletcU2bDbnKhuNOy%2Bk87yKbbSZxJMygrk1%2BYhpVK3Ax286VvwK6ZtB7NJtj3zVxwU8lFJ0w0F0fkLaQ%2FtTgYEFCsjNfXv5X8nB9D6FuYdJqQOM37QFHzgE2JGyNW7oyVYQtDYKfK8U2l4cO2dNu3bnxhYsQbehuIlz093ffu%2Fd53JclsW4dXTaDBMiLoyAv9ERzkc7veGEKwVExH3N%2FicFFsjMUZgk%2BNrxMfQQjN8FzKvdksd%2B2OxzijDgf7SObfl1l7yzM3SG4iPnv%2F7r4q0iweCI1Kl3FXqpEiwi1exYYvPsjVfJPPFD%2BK2mTrbvkt4C4H5GXB21OJLCJHZj92i0u60BiONuUDVatcfMlYZLpz6Q96dhIybGrJAoXrcDTZQR0TFNLb49IKmk4RKfJ9Ekx2va%2ByYYpY9euPkbNm9ti2x%2BjrW29v9ntZkvlCyr1fnHjIvbCN7pD0T37OsIF8QF1wuxpLLeaamrQACRQecbp8TfwucPDZzap6mH2WraW0gGWHXM5KqoiSVybbsUiEl%2BAWEyrXZkruLfaQATOXrWY8K%2FXvUj8czHQGDZsdkt%2B0M%2F19dM6eL%2BgMNzKh70GOqUBUZipbpxGMmj%2BTHMgrU5jFJamYi8kpqdmWrAKX3EUgpug8a5ByVp8slVszF5rLVEGp90gP3VedS7Rq6vp6nC0I2BHyGIuIndJcHHEM7kU%2BCBHPh78BqFQZZu2OrMics%2F1hUlgXC9uWsgebr5FOaffPPyDp9iSuHe8J1ZViWbw6b9MqfyB3fGaLs3hQH1jOs4Gib59j%2BuvrGVuT3dH1nkVwd%2FIG5wJ&X-Amz-Signature=fa99257b84f63af5166cc18845fef75ccc780620cb01e2230c0dc0f636a86392&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QWVMIEWE%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIQD7BvZYRtXnsyFBSt4LeDG4FVpl4%2B6H3Rfs963mxYSOrgIgRBmG5kRniEW5hT7wA49dI2UbmRnaCJST2pGO02squsEq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDKFo5CAzjVX98fmkoCrcAzxRqWmHhzN7jgP%2B41fQ7JBjNsRjmqg12iDDk7SKwbfqYySEPletcU2bDbnKhuNOy%2Bk87yKbbSZxJMygrk1%2BYhpVK3Ax286VvwK6ZtB7NJtj3zVxwU8lFJ0w0F0fkLaQ%2FtTgYEFCsjNfXv5X8nB9D6FuYdJqQOM37QFHzgE2JGyNW7oyVYQtDYKfK8U2l4cO2dNu3bnxhYsQbehuIlz093ffu%2Fd53JclsW4dXTaDBMiLoyAv9ERzkc7veGEKwVExH3N%2FicFFsjMUZgk%2BNrxMfQQjN8FzKvdksd%2B2OxzijDgf7SObfl1l7yzM3SG4iPnv%2F7r4q0iweCI1Kl3FXqpEiwi1exYYvPsjVfJPPFD%2BK2mTrbvkt4C4H5GXB21OJLCJHZj92i0u60BiONuUDVatcfMlYZLpz6Q96dhIybGrJAoXrcDTZQR0TFNLb49IKmk4RKfJ9Ekx2va%2ByYYpY9euPkbNm9ti2x%2BjrW29v9ntZkvlCyr1fnHjIvbCN7pD0T37OsIF8QF1wuxpLLeaamrQACRQecbp8TfwucPDZzap6mH2WraW0gGWHXM5KqoiSVybbsUiEl%2BAWEyrXZkruLfaQATOXrWY8K%2FXvUj8czHQGDZsdkt%2B0M%2F19dM6eL%2BgMNzKh70GOqUBUZipbpxGMmj%2BTHMgrU5jFJamYi8kpqdmWrAKX3EUgpug8a5ByVp8slVszF5rLVEGp90gP3VedS7Rq6vp6nC0I2BHyGIuIndJcHHEM7kU%2BCBHPh78BqFQZZu2OrMics%2F1hUlgXC9uWsgebr5FOaffPPyDp9iSuHe8J1ZViWbw6b9MqfyB3fGaLs3hQH1jOs4Gib59j%2BuvrGVuT3dH1nkVwd%2FIG5wJ&X-Amz-Signature=994f8a7cf09a8de081a47ba36146c37c1526e86724a16c0fe90cdc0ea6f6eee5&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QWVMIEWE%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIQD7BvZYRtXnsyFBSt4LeDG4FVpl4%2B6H3Rfs963mxYSOrgIgRBmG5kRniEW5hT7wA49dI2UbmRnaCJST2pGO02squsEq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDKFo5CAzjVX98fmkoCrcAzxRqWmHhzN7jgP%2B41fQ7JBjNsRjmqg12iDDk7SKwbfqYySEPletcU2bDbnKhuNOy%2Bk87yKbbSZxJMygrk1%2BYhpVK3Ax286VvwK6ZtB7NJtj3zVxwU8lFJ0w0F0fkLaQ%2FtTgYEFCsjNfXv5X8nB9D6FuYdJqQOM37QFHzgE2JGyNW7oyVYQtDYKfK8U2l4cO2dNu3bnxhYsQbehuIlz093ffu%2Fd53JclsW4dXTaDBMiLoyAv9ERzkc7veGEKwVExH3N%2FicFFsjMUZgk%2BNrxMfQQjN8FzKvdksd%2B2OxzijDgf7SObfl1l7yzM3SG4iPnv%2F7r4q0iweCI1Kl3FXqpEiwi1exYYvPsjVfJPPFD%2BK2mTrbvkt4C4H5GXB21OJLCJHZj92i0u60BiONuUDVatcfMlYZLpz6Q96dhIybGrJAoXrcDTZQR0TFNLb49IKmk4RKfJ9Ekx2va%2ByYYpY9euPkbNm9ti2x%2BjrW29v9ntZkvlCyr1fnHjIvbCN7pD0T37OsIF8QF1wuxpLLeaamrQACRQecbp8TfwucPDZzap6mH2WraW0gGWHXM5KqoiSVybbsUiEl%2BAWEyrXZkruLfaQATOXrWY8K%2FXvUj8czHQGDZsdkt%2B0M%2F19dM6eL%2BgMNzKh70GOqUBUZipbpxGMmj%2BTHMgrU5jFJamYi8kpqdmWrAKX3EUgpug8a5ByVp8slVszF5rLVEGp90gP3VedS7Rq6vp6nC0I2BHyGIuIndJcHHEM7kU%2BCBHPh78BqFQZZu2OrMics%2F1hUlgXC9uWsgebr5FOaffPPyDp9iSuHe8J1ZViWbw6b9MqfyB3fGaLs3hQH1jOs4Gib59j%2BuvrGVuT3dH1nkVwd%2FIG5wJ&X-Amz-Signature=4e2a450b0a8de922cc584af1be737ddad011d871a892502eaf6d0bf1bd7b5927&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIEXAZEG%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIDuSbtG%2FqN%2Bdr7VEnqNKRwIFpvLB%2BRtfaDAo5f3Kvd0zAiEAm4NaBx5IC8%2B5%2F0yZd9jDh8UH7uza%2B7j%2F2MS%2BjroGClwq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDPPi8mV47QOvZ0UV3yrcAzxxbKUPtf3FSHV03gSw8ht05chzIv7Hn%2B7suXn1Lr5%2FgKaVxS1LK69mL%2FpszV3WoJGLd7c%2BoN8d%2B2gI9Is%2FA9tBn6M%2B4BQUV4%2B1rn3fOUIQ1FxthaOfJMrSaneML%2BMnPs3M0wPqXliA0SnxT0cky4nO4nXSgxRwzXufXMW14UkNQkkGpKi9yS%2B%2FTaZcOd8yuLIpFdkfbu03Q8k8RXKEIcBP7%2FjTYuNFPP2Um8CkCcw2tUFyHKKqECAJeCInAlZ4efw1jCBXfloNfktqJglHHsGIhkXusgVZN6jmJBftPX2OVPyAJSuvrDgPGTXGzs642AfioR%2FtTuuz8%2FyyJBeFqr0vJzwwWxf0JTfFUAc3s3IMaJoQz8EsRRkCXxEpzc2vNXetkGJF%2BARYdeKgQP56JrHauztCXH6NNDwXOffjC8nTLn9SzsbSnXzube15ytqY0BR5nSEzK1uX2juYFn5p0lXm%2BQtXARqiejoQCt1RTVO6hzXOyBn81dcK%2FPleOdItNbZOxoSaLAR%2B6kfuvzIheHHYZYnkZlG65JHFiZtDHIjF1L6zSHp3RB1%2FAxe4aeXXXZz2Yz5vtFQW1jOzVT%2BdTS8KzEBYf9tK0uMCBbkpSHO994kkYDaNhX%2BqYgM0MP7Kh70GOqUB1vb%2BXAb3uFQp43ZpLw%2BLgdbU81Qe7q1oHM1ti2C2eoNWDqt69GaAklP2ZMYOKH363iUgmwWd4O9YtyghGOYfURGBP%2B0KmXjMO1T9cO8cJ3H4QbmH6OghKcE0hxTchGFyJfl1IVBpZ%2F2h0UCPg3e82I%2B6XUJxrD1SWs%2FkfRN5DLzovBfiSVI%2BTqGyYtuBR%2B26WQY9rHkTXH1qbnkTMoluIw2oIXxG&X-Amz-Signature=bc987f468056b9bb6a7863dcbd99cae023cf2c73b0c0bbb5d93152edac026bbb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQKLPC4O%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJIMEYCIQCLQJE%2FiGukXYUs5rmFrvNI7%2BRzv2a1JRbCrG1wiA5CCwIhAJr2ZtATD8DNKYIywlv4I8SVGVRIx07E3AAPHKKf5zdUKv8DCCsQABoMNjM3NDIzMTgzODA1Igx22S6MshgoQcMNtoYq3APUkPQTkBfcr80%2BFS3ySIl5bY0AsdY0urGDU9DWdInJncrLx52TUjgCyYnEoWZCrjwTh1jyraFhaeNhWRZzhihpP5cWDWpHY4ASJNuQYDolFBd5U8Bx5wc1f5GAohFx6P88A%2BB7tIPgjR0yaaVFdT%2FGBclVzoeMdFhmDnFg5pBpeqAh9q3L%2FEcpUxtIcQ2Be3Ae%2B26zt9RVZT6LNITFYs9wgwnPXquiKd3eyppC%2FqmVrhHve5EEv3QbE3%2FnyL0rr9qhH%2BzWKkH5sr%2Fh8M49%2Fe%2FmdA%2FQn%2B3MeyrWpRGJTy%2B%2BZjtkLBTlPwqe2d3cPL11L5RQv5AP1pBo%2B3bWynRgHp3PLsiComH9hSmnpoxNaDvpn4VL%2BnfK8YSBQpGAkPX5xt6XyPwzseUABMq3nyWaHe1C%2Bb70x4Bv1FqUJXnIYkaw%2FBX2vsqBO5b0fTDNcUXRwawWJTlzbJlQgQXZw6759fkmvyNEYOuU1t4SwST9nsF%2BfVcCqnHGVz%2FoTldPY3i%2FoKDFE21qgCUl5%2BVCwWkt3dtajb%2B%2FOuRJrhwUc9L7ugqwPeqB3F%2BpOgkpllWmKw%2B5q%2BOR5oGtM%2FIhMHNrVrF4%2Ft9ZGVtiPQ1FxyyxmTtaKVC0wxpDHe7E49NeXyzGEjCsyoe9BjqkAbEoO6siYD9znqsqipMFui5Sbmts7rIoElpw7QEqSLg4LmRFkYnGlQXmdG%2BA0E5cYE%2F4S%2BBir3hhlnblGpaBWse8auRgkZF9mKO7mXJC4Vhu7Ps7VNBCP%2FzQ0ieym5LaEccWwF3sbB1YkIuoQ1Cuc%2B2cOqK3CF%2Fn0%2B%2B6%2F2HYHG00Ex7zxtcnQUFqieEHDto2oDIQT9iR2VlzO0txEQzxvGuwNPee&X-Amz-Signature=1190c935a5b377bf78e7a20670c4f7e4fe7c398f96d20c39cc696e5046f9c561&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QWVMIEWE%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIQD7BvZYRtXnsyFBSt4LeDG4FVpl4%2B6H3Rfs963mxYSOrgIgRBmG5kRniEW5hT7wA49dI2UbmRnaCJST2pGO02squsEq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDKFo5CAzjVX98fmkoCrcAzxRqWmHhzN7jgP%2B41fQ7JBjNsRjmqg12iDDk7SKwbfqYySEPletcU2bDbnKhuNOy%2Bk87yKbbSZxJMygrk1%2BYhpVK3Ax286VvwK6ZtB7NJtj3zVxwU8lFJ0w0F0fkLaQ%2FtTgYEFCsjNfXv5X8nB9D6FuYdJqQOM37QFHzgE2JGyNW7oyVYQtDYKfK8U2l4cO2dNu3bnxhYsQbehuIlz093ffu%2Fd53JclsW4dXTaDBMiLoyAv9ERzkc7veGEKwVExH3N%2FicFFsjMUZgk%2BNrxMfQQjN8FzKvdksd%2B2OxzijDgf7SObfl1l7yzM3SG4iPnv%2F7r4q0iweCI1Kl3FXqpEiwi1exYYvPsjVfJPPFD%2BK2mTrbvkt4C4H5GXB21OJLCJHZj92i0u60BiONuUDVatcfMlYZLpz6Q96dhIybGrJAoXrcDTZQR0TFNLb49IKmk4RKfJ9Ekx2va%2ByYYpY9euPkbNm9ti2x%2BjrW29v9ntZkvlCyr1fnHjIvbCN7pD0T37OsIF8QF1wuxpLLeaamrQACRQecbp8TfwucPDZzap6mH2WraW0gGWHXM5KqoiSVybbsUiEl%2BAWEyrXZkruLfaQATOXrWY8K%2FXvUj8czHQGDZsdkt%2B0M%2F19dM6eL%2BgMNzKh70GOqUBUZipbpxGMmj%2BTHMgrU5jFJamYi8kpqdmWrAKX3EUgpug8a5ByVp8slVszF5rLVEGp90gP3VedS7Rq6vp6nC0I2BHyGIuIndJcHHEM7kU%2BCBHPh78BqFQZZu2OrMics%2F1hUlgXC9uWsgebr5FOaffPPyDp9iSuHe8J1ZViWbw6b9MqfyB3fGaLs3hQH1jOs4Gib59j%2BuvrGVuT3dH1nkVwd%2FIG5wJ&X-Amz-Signature=c8b9769859af6b7bf41b6e7de3ac8290f75996eb163dbf637cf99e41e6cc32c2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QWVMIEWE%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIQD7BvZYRtXnsyFBSt4LeDG4FVpl4%2B6H3Rfs963mxYSOrgIgRBmG5kRniEW5hT7wA49dI2UbmRnaCJST2pGO02squsEq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDKFo5CAzjVX98fmkoCrcAzxRqWmHhzN7jgP%2B41fQ7JBjNsRjmqg12iDDk7SKwbfqYySEPletcU2bDbnKhuNOy%2Bk87yKbbSZxJMygrk1%2BYhpVK3Ax286VvwK6ZtB7NJtj3zVxwU8lFJ0w0F0fkLaQ%2FtTgYEFCsjNfXv5X8nB9D6FuYdJqQOM37QFHzgE2JGyNW7oyVYQtDYKfK8U2l4cO2dNu3bnxhYsQbehuIlz093ffu%2Fd53JclsW4dXTaDBMiLoyAv9ERzkc7veGEKwVExH3N%2FicFFsjMUZgk%2BNrxMfQQjN8FzKvdksd%2B2OxzijDgf7SObfl1l7yzM3SG4iPnv%2F7r4q0iweCI1Kl3FXqpEiwi1exYYvPsjVfJPPFD%2BK2mTrbvkt4C4H5GXB21OJLCJHZj92i0u60BiONuUDVatcfMlYZLpz6Q96dhIybGrJAoXrcDTZQR0TFNLb49IKmk4RKfJ9Ekx2va%2ByYYpY9euPkbNm9ti2x%2BjrW29v9ntZkvlCyr1fnHjIvbCN7pD0T37OsIF8QF1wuxpLLeaamrQACRQecbp8TfwucPDZzap6mH2WraW0gGWHXM5KqoiSVybbsUiEl%2BAWEyrXZkruLfaQATOXrWY8K%2FXvUj8czHQGDZsdkt%2B0M%2F19dM6eL%2BgMNzKh70GOqUBUZipbpxGMmj%2BTHMgrU5jFJamYi8kpqdmWrAKX3EUgpug8a5ByVp8slVszF5rLVEGp90gP3VedS7Rq6vp6nC0I2BHyGIuIndJcHHEM7kU%2BCBHPh78BqFQZZu2OrMics%2F1hUlgXC9uWsgebr5FOaffPPyDp9iSuHe8J1ZViWbw6b9MqfyB3fGaLs3hQH1jOs4Gib59j%2BuvrGVuT3dH1nkVwd%2FIG5wJ&X-Amz-Signature=b2eb44a0f70017b051a497238a96f07df867f9f801397f26705cce9fab30fdc3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QWVMIEWE%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIQD7BvZYRtXnsyFBSt4LeDG4FVpl4%2B6H3Rfs963mxYSOrgIgRBmG5kRniEW5hT7wA49dI2UbmRnaCJST2pGO02squsEq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDKFo5CAzjVX98fmkoCrcAzxRqWmHhzN7jgP%2B41fQ7JBjNsRjmqg12iDDk7SKwbfqYySEPletcU2bDbnKhuNOy%2Bk87yKbbSZxJMygrk1%2BYhpVK3Ax286VvwK6ZtB7NJtj3zVxwU8lFJ0w0F0fkLaQ%2FtTgYEFCsjNfXv5X8nB9D6FuYdJqQOM37QFHzgE2JGyNW7oyVYQtDYKfK8U2l4cO2dNu3bnxhYsQbehuIlz093ffu%2Fd53JclsW4dXTaDBMiLoyAv9ERzkc7veGEKwVExH3N%2FicFFsjMUZgk%2BNrxMfQQjN8FzKvdksd%2B2OxzijDgf7SObfl1l7yzM3SG4iPnv%2F7r4q0iweCI1Kl3FXqpEiwi1exYYvPsjVfJPPFD%2BK2mTrbvkt4C4H5GXB21OJLCJHZj92i0u60BiONuUDVatcfMlYZLpz6Q96dhIybGrJAoXrcDTZQR0TFNLb49IKmk4RKfJ9Ekx2va%2ByYYpY9euPkbNm9ti2x%2BjrW29v9ntZkvlCyr1fnHjIvbCN7pD0T37OsIF8QF1wuxpLLeaamrQACRQecbp8TfwucPDZzap6mH2WraW0gGWHXM5KqoiSVybbsUiEl%2BAWEyrXZkruLfaQATOXrWY8K%2FXvUj8czHQGDZsdkt%2B0M%2F19dM6eL%2BgMNzKh70GOqUBUZipbpxGMmj%2BTHMgrU5jFJamYi8kpqdmWrAKX3EUgpug8a5ByVp8slVszF5rLVEGp90gP3VedS7Rq6vp6nC0I2BHyGIuIndJcHHEM7kU%2BCBHPh78BqFQZZu2OrMics%2F1hUlgXC9uWsgebr5FOaffPPyDp9iSuHe8J1ZViWbw6b9MqfyB3fGaLs3hQH1jOs4Gib59j%2BuvrGVuT3dH1nkVwd%2FIG5wJ&X-Amz-Signature=aba9271acbf02b365685ed42b5ecf68266ec90cae090267bab0ed2bc23b8593c&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QWVMIEWE%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIQD7BvZYRtXnsyFBSt4LeDG4FVpl4%2B6H3Rfs963mxYSOrgIgRBmG5kRniEW5hT7wA49dI2UbmRnaCJST2pGO02squsEq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDKFo5CAzjVX98fmkoCrcAzxRqWmHhzN7jgP%2B41fQ7JBjNsRjmqg12iDDk7SKwbfqYySEPletcU2bDbnKhuNOy%2Bk87yKbbSZxJMygrk1%2BYhpVK3Ax286VvwK6ZtB7NJtj3zVxwU8lFJ0w0F0fkLaQ%2FtTgYEFCsjNfXv5X8nB9D6FuYdJqQOM37QFHzgE2JGyNW7oyVYQtDYKfK8U2l4cO2dNu3bnxhYsQbehuIlz093ffu%2Fd53JclsW4dXTaDBMiLoyAv9ERzkc7veGEKwVExH3N%2FicFFsjMUZgk%2BNrxMfQQjN8FzKvdksd%2B2OxzijDgf7SObfl1l7yzM3SG4iPnv%2F7r4q0iweCI1Kl3FXqpEiwi1exYYvPsjVfJPPFD%2BK2mTrbvkt4C4H5GXB21OJLCJHZj92i0u60BiONuUDVatcfMlYZLpz6Q96dhIybGrJAoXrcDTZQR0TFNLb49IKmk4RKfJ9Ekx2va%2ByYYpY9euPkbNm9ti2x%2BjrW29v9ntZkvlCyr1fnHjIvbCN7pD0T37OsIF8QF1wuxpLLeaamrQACRQecbp8TfwucPDZzap6mH2WraW0gGWHXM5KqoiSVybbsUiEl%2BAWEyrXZkruLfaQATOXrWY8K%2FXvUj8czHQGDZsdkt%2B0M%2F19dM6eL%2BgMNzKh70GOqUBUZipbpxGMmj%2BTHMgrU5jFJamYi8kpqdmWrAKX3EUgpug8a5ByVp8slVszF5rLVEGp90gP3VedS7Rq6vp6nC0I2BHyGIuIndJcHHEM7kU%2BCBHPh78BqFQZZu2OrMics%2F1hUlgXC9uWsgebr5FOaffPPyDp9iSuHe8J1ZViWbw6b9MqfyB3fGaLs3hQH1jOs4Gib59j%2BuvrGVuT3dH1nkVwd%2FIG5wJ&X-Amz-Signature=ab39e965808b4c3e5536033088e527e4856c7a6218812234dbf9c9962fb90ef6&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
