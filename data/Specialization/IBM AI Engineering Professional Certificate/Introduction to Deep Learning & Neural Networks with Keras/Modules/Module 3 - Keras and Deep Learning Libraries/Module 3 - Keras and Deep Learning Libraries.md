

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ZG774TQ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211327Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID2Evqzo3MV6SVgGxE5n6CN3HLLZRhDpnPtIJGORaOcLAiATvQZZRepnZYwW15KMKtrfw70ZO9JE4GO81HL79YYwlCqIBAiu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMDBwJb7I7fupdo6JJKtwDnCr%2BGFzIX3SK6q7PG31eZSBiy0Z0BiOgh08BB8B6VEr5Io23J9528da4XwqCPcFL4aVGr0RbbkeRyBNsZnKxchPEmV09bUhzSI2e8rDXJrCpziY26LSlmtZ2tApVka%2FtdB%2BCGUme3ii1gQcyocMO2uBIc6%2BZJ9G%2FgAx1%2FWS675dWYhQLhn7HVTL%2FfxpDMmmzBIKQrHm1oy0XhGZce65FVeitg3aaWjfbZri915BNi92T%2BAd26wzIP%2F%2FqhP9TlTCsNb6NwKxaZ5FVpQNaWiWtco2uJ36MXkuYUVVBI11kyCOcZ6X%2BoL1463OUZglcMBb4gemT035QUD6YOuuhSCXiPsbUYG9qdpNICTQPIYtMNnedcxCqqMGxiqCETslB5EtGyShliwjiDu6UxNu%2FX1IvHUhlfe%2Fi9fGMHMCJN5I5sCtinVXddfK7cT%2BePguiEbHznB58K5Ou27PV3vkjTCsimeOvuCZnqs5wk7o2KebduwewkrPMEjX8PBikhPp%2BpU1z3lmawhPSLcwdRcDRz3MugsdvFWDjh2wLMM3UgxwzgGIIvtyLwS2T%2Fifdwfnm5z7ObungJSBx9qorsUfpi4WVeYg%2FU1zSeXtXOT69bCvhCS0eNIZmTFOnJnJ1GEgwmMXvvAY6pgE1UyOMndLVnbc8VufkxtcPd81e9TEbPuVapcCNcydB50rD48FQbDPMnUcwgmgUAEWw%2B725C7vUEgBs7z8OkEQGjpCmkWKz4xHgzXjg1E7c3%2FFzAVxDgw0zmBGJFdfxDcB6Nqs7G0lvOGs%2FDyadCggbcAsVFw6ClqRSRuw0e0p9X3aShG7i7iwhXVSuiGKHRCosRYASsDpY00%2BZumX15odhIx%2BfoL4i&X-Amz-Signature=7d09d170ec9fbf0e19559f5aa32c4cfe3d15e4569f8c724de408810ef8a9cc7f&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ZG774TQ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211327Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID2Evqzo3MV6SVgGxE5n6CN3HLLZRhDpnPtIJGORaOcLAiATvQZZRepnZYwW15KMKtrfw70ZO9JE4GO81HL79YYwlCqIBAiu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMDBwJb7I7fupdo6JJKtwDnCr%2BGFzIX3SK6q7PG31eZSBiy0Z0BiOgh08BB8B6VEr5Io23J9528da4XwqCPcFL4aVGr0RbbkeRyBNsZnKxchPEmV09bUhzSI2e8rDXJrCpziY26LSlmtZ2tApVka%2FtdB%2BCGUme3ii1gQcyocMO2uBIc6%2BZJ9G%2FgAx1%2FWS675dWYhQLhn7HVTL%2FfxpDMmmzBIKQrHm1oy0XhGZce65FVeitg3aaWjfbZri915BNi92T%2BAd26wzIP%2F%2FqhP9TlTCsNb6NwKxaZ5FVpQNaWiWtco2uJ36MXkuYUVVBI11kyCOcZ6X%2BoL1463OUZglcMBb4gemT035QUD6YOuuhSCXiPsbUYG9qdpNICTQPIYtMNnedcxCqqMGxiqCETslB5EtGyShliwjiDu6UxNu%2FX1IvHUhlfe%2Fi9fGMHMCJN5I5sCtinVXddfK7cT%2BePguiEbHznB58K5Ou27PV3vkjTCsimeOvuCZnqs5wk7o2KebduwewkrPMEjX8PBikhPp%2BpU1z3lmawhPSLcwdRcDRz3MugsdvFWDjh2wLMM3UgxwzgGIIvtyLwS2T%2Fifdwfnm5z7ObungJSBx9qorsUfpi4WVeYg%2FU1zSeXtXOT69bCvhCS0eNIZmTFOnJnJ1GEgwmMXvvAY6pgE1UyOMndLVnbc8VufkxtcPd81e9TEbPuVapcCNcydB50rD48FQbDPMnUcwgmgUAEWw%2B725C7vUEgBs7z8OkEQGjpCmkWKz4xHgzXjg1E7c3%2FFzAVxDgw0zmBGJFdfxDcB6Nqs7G0lvOGs%2FDyadCggbcAsVFw6ClqRSRuw0e0p9X3aShG7i7iwhXVSuiGKHRCosRYASsDpY00%2BZumX15odhIx%2BfoL4i&X-Amz-Signature=b405d4346ad01a719034a5d1c4d34e8324ae9c8003210865ed5f3aa260872488&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ZG774TQ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211327Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID2Evqzo3MV6SVgGxE5n6CN3HLLZRhDpnPtIJGORaOcLAiATvQZZRepnZYwW15KMKtrfw70ZO9JE4GO81HL79YYwlCqIBAiu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMDBwJb7I7fupdo6JJKtwDnCr%2BGFzIX3SK6q7PG31eZSBiy0Z0BiOgh08BB8B6VEr5Io23J9528da4XwqCPcFL4aVGr0RbbkeRyBNsZnKxchPEmV09bUhzSI2e8rDXJrCpziY26LSlmtZ2tApVka%2FtdB%2BCGUme3ii1gQcyocMO2uBIc6%2BZJ9G%2FgAx1%2FWS675dWYhQLhn7HVTL%2FfxpDMmmzBIKQrHm1oy0XhGZce65FVeitg3aaWjfbZri915BNi92T%2BAd26wzIP%2F%2FqhP9TlTCsNb6NwKxaZ5FVpQNaWiWtco2uJ36MXkuYUVVBI11kyCOcZ6X%2BoL1463OUZglcMBb4gemT035QUD6YOuuhSCXiPsbUYG9qdpNICTQPIYtMNnedcxCqqMGxiqCETslB5EtGyShliwjiDu6UxNu%2FX1IvHUhlfe%2Fi9fGMHMCJN5I5sCtinVXddfK7cT%2BePguiEbHznB58K5Ou27PV3vkjTCsimeOvuCZnqs5wk7o2KebduwewkrPMEjX8PBikhPp%2BpU1z3lmawhPSLcwdRcDRz3MugsdvFWDjh2wLMM3UgxwzgGIIvtyLwS2T%2Fifdwfnm5z7ObungJSBx9qorsUfpi4WVeYg%2FU1zSeXtXOT69bCvhCS0eNIZmTFOnJnJ1GEgwmMXvvAY6pgE1UyOMndLVnbc8VufkxtcPd81e9TEbPuVapcCNcydB50rD48FQbDPMnUcwgmgUAEWw%2B725C7vUEgBs7z8OkEQGjpCmkWKz4xHgzXjg1E7c3%2FFzAVxDgw0zmBGJFdfxDcB6Nqs7G0lvOGs%2FDyadCggbcAsVFw6ClqRSRuw0e0p9X3aShG7i7iwhXVSuiGKHRCosRYASsDpY00%2BZumX15odhIx%2BfoL4i&X-Amz-Signature=5d391c92e7f38674b756df86da325ceba96ba415cb7568133e128415e9dc2a32&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664NWNX5ZU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211328Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCnKRG2I0zUNN6c%2BEFlUmJ1Yr5AJyWpCA8JrLieGZFYrwIgME0YIES2PnA5m9VuU88RQ6X4kPi5KJAQW5MUmEbFBC8qiAQIrv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDELovK9wqbh18gfmCCrcA%2BPYX3QXTrAQq9lI3AT8V9BqiAXjKj0Ej8yziKXu0KdERh4oP9EYKWEm1%2BYWvaDJEVyH3pY8mvTHSZDpmeTGwgR04DNFveEaXwugwxBF7y7SCjvbFQzlEWrmlyCSM%2FBpGIaDbSGAP%2F17DRfSqpimBgDc6qtoljRy1mLxi3NhDE6AkG7ISAoXSCXUH9BZjBm0q27op44SRYjlncyiKzxCSf2j0Xr%2BUt6Y%2B5jbV4NU4TCtaDOwmAM6qV3uKH5VUOiZ1VET%2Fe%2Fa8XrNNMGcT81OHSDIphw8u3eMhXMGnImvu7zKyDgUzmkmLt0icq9PNbfrEUJgHYADWwePiSJXjjoNQnmoDxTgm36d0u5XE8WlPZ6zmLtrxhKs0kUfyNCf3H1yrCFx6PMnIpNgyzOxT97oLl77VvR5Kiq%2FyWCvefQNn4kkZ6p%2FbyXyiU7cag25a0AoU1MATnscjfopCeVE1IzGifwLC8B%2BeulCEpIbccApj2IWG%2BXAvYf75qdTaPy2g9OS2l0ikuuV2pdfE6ZFW4N3wwZXGDwlVE5fqsjXtcqgxs3FL%2BM0HnKAMdNdkIAnZPd%2BGRsovh7P%2B8BfkQ1MJp5%2B0Yh5u0cpMstGHIlBrLnFyQHN1VH2pgeLrIzzeDGgMMfF77wGOqUBgxwqugtJweXeir5DocU7E1mGyiqqczprwA9xfL5nQJsuzL7VCMxdSC5LKVTk5WU8Ah15oqOBLL51WRBK5kGxrFFLcOh8atWi0EmcYId5E1OzRKroPQO3Tp7aU7n7ZzhKkJ3Om%2BWotjn267sAQQZpK2RaO%2Fm9AUNayX4rcA3PXX4gbqwBbQT7Sr1%2BYHqcVGe3u%2B3CwZ9DZeXJ6qItbZMFnnnimA%2FG&X-Amz-Signature=1285a00c7d1cf3c67890909430d07a37369be1be9ea3f9f1dd6db60e7db0aff1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRZDSMDW%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211328Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE9Z3r8mEsEu7Ry4wHdYAjxwgQ0fNstf4lF6yQ7QA0LmAiBM7%2BLxn%2BEcd82NwVyVTDdcGQtnJmeZY2zZ6KbELQhONCqIBAiu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2F%2FNH%2BGozeXu9PI6%2BKtwDkaPSfhkGvOAIvMOxvTmhujj14xFz3n5B%2Ff3GbUqgOMASXXcWk4mWgB%2BjGqmtB9Hd2HJmYUl0YQtfWTu3H0azt%2F0K8othpUO0E%2FpPX06ucsVX9PFi74bejbviRMUmVN0ANLO0WSD7kJtWZzp9fHzJkgs8IzsHn0slylBvsFMej%2FNHNX0Q8q9IjsEhIbWtswtAOT2ypnBfMWxXTNol%2F6EX1HPgVFoTj%2FgAnHOw5If71DW6of49k0Eq6pWQv6sa%2Ff84lcVWVAnX2cUP1PEOMNmGAsmKJRSmj%2BmpEEFVxA4%2FzZhGjekA%2BEPQpbHcCIlxUtUsZssUYXOSAiUY7OuR0NYLRKp%2FX81TR%2B9IH5o9Ck4WUz3AU8ryuwJ%2Bg4xwiD2c8dIr8oVkCGdgJk%2Bi6sUoNUy9ipPVIsVm679mwmmF0Q8l1iLsTQKgRZeZesNaFXOGiBgBRjsxNY%2FxcthxnQaEHcjy7fTbs8yVBpYRwSeGrcT9xY%2BBa6n7nAIaIuVcgKphgmWMA7FTTf7SYp8SUkdB0FtZEWQHhV%2FjrmayPYmRCRewTOsEeJOWztn2OUw7zztr3q7mzT5nlZTI603f32FaEJL6Hd%2FCg6UIsdXNbO4%2Bny08g2OTaFzyESu%2BDWxy158wysXvvAY6pgHBt8stnTf9rbd1n1l4jkTkZ2amvcbGjteSNeS469g3Evmxbt%2FN%2BHoWrMrPRxes3ZWyVFmvtqN%2FMDNk8aFmcV0b41uER33Ir0fLPOJ7xY4aiDBJqk8tiWcklxGyPLyoMrgKO7vuSiZ%2BBPNKhHJDQgxpJBHA92YkoWUD%2FfPbqzuy9gnkTaqXITVROdY4XZu%2BWPquh%2FshLkNudtpsYJOgEJXsP4e9VufC&X-Amz-Signature=92b574800a03b7d70eb1fb52a69c222c6da8fbd5d3ab12f58d700f314ebf32da&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ZG774TQ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211327Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID2Evqzo3MV6SVgGxE5n6CN3HLLZRhDpnPtIJGORaOcLAiATvQZZRepnZYwW15KMKtrfw70ZO9JE4GO81HL79YYwlCqIBAiu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMDBwJb7I7fupdo6JJKtwDnCr%2BGFzIX3SK6q7PG31eZSBiy0Z0BiOgh08BB8B6VEr5Io23J9528da4XwqCPcFL4aVGr0RbbkeRyBNsZnKxchPEmV09bUhzSI2e8rDXJrCpziY26LSlmtZ2tApVka%2FtdB%2BCGUme3ii1gQcyocMO2uBIc6%2BZJ9G%2FgAx1%2FWS675dWYhQLhn7HVTL%2FfxpDMmmzBIKQrHm1oy0XhGZce65FVeitg3aaWjfbZri915BNi92T%2BAd26wzIP%2F%2FqhP9TlTCsNb6NwKxaZ5FVpQNaWiWtco2uJ36MXkuYUVVBI11kyCOcZ6X%2BoL1463OUZglcMBb4gemT035QUD6YOuuhSCXiPsbUYG9qdpNICTQPIYtMNnedcxCqqMGxiqCETslB5EtGyShliwjiDu6UxNu%2FX1IvHUhlfe%2Fi9fGMHMCJN5I5sCtinVXddfK7cT%2BePguiEbHznB58K5Ou27PV3vkjTCsimeOvuCZnqs5wk7o2KebduwewkrPMEjX8PBikhPp%2BpU1z3lmawhPSLcwdRcDRz3MugsdvFWDjh2wLMM3UgxwzgGIIvtyLwS2T%2Fifdwfnm5z7ObungJSBx9qorsUfpi4WVeYg%2FU1zSeXtXOT69bCvhCS0eNIZmTFOnJnJ1GEgwmMXvvAY6pgE1UyOMndLVnbc8VufkxtcPd81e9TEbPuVapcCNcydB50rD48FQbDPMnUcwgmgUAEWw%2B725C7vUEgBs7z8OkEQGjpCmkWKz4xHgzXjg1E7c3%2FFzAVxDgw0zmBGJFdfxDcB6Nqs7G0lvOGs%2FDyadCggbcAsVFw6ClqRSRuw0e0p9X3aShG7i7iwhXVSuiGKHRCosRYASsDpY00%2BZumX15odhIx%2BfoL4i&X-Amz-Signature=769ee86fa85b5d0d290f71f031f87d9e0ff2baee0d4d20fac880d79eaccea68c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ZG774TQ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211327Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID2Evqzo3MV6SVgGxE5n6CN3HLLZRhDpnPtIJGORaOcLAiATvQZZRepnZYwW15KMKtrfw70ZO9JE4GO81HL79YYwlCqIBAiu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMDBwJb7I7fupdo6JJKtwDnCr%2BGFzIX3SK6q7PG31eZSBiy0Z0BiOgh08BB8B6VEr5Io23J9528da4XwqCPcFL4aVGr0RbbkeRyBNsZnKxchPEmV09bUhzSI2e8rDXJrCpziY26LSlmtZ2tApVka%2FtdB%2BCGUme3ii1gQcyocMO2uBIc6%2BZJ9G%2FgAx1%2FWS675dWYhQLhn7HVTL%2FfxpDMmmzBIKQrHm1oy0XhGZce65FVeitg3aaWjfbZri915BNi92T%2BAd26wzIP%2F%2FqhP9TlTCsNb6NwKxaZ5FVpQNaWiWtco2uJ36MXkuYUVVBI11kyCOcZ6X%2BoL1463OUZglcMBb4gemT035QUD6YOuuhSCXiPsbUYG9qdpNICTQPIYtMNnedcxCqqMGxiqCETslB5EtGyShliwjiDu6UxNu%2FX1IvHUhlfe%2Fi9fGMHMCJN5I5sCtinVXddfK7cT%2BePguiEbHznB58K5Ou27PV3vkjTCsimeOvuCZnqs5wk7o2KebduwewkrPMEjX8PBikhPp%2BpU1z3lmawhPSLcwdRcDRz3MugsdvFWDjh2wLMM3UgxwzgGIIvtyLwS2T%2Fifdwfnm5z7ObungJSBx9qorsUfpi4WVeYg%2FU1zSeXtXOT69bCvhCS0eNIZmTFOnJnJ1GEgwmMXvvAY6pgE1UyOMndLVnbc8VufkxtcPd81e9TEbPuVapcCNcydB50rD48FQbDPMnUcwgmgUAEWw%2B725C7vUEgBs7z8OkEQGjpCmkWKz4xHgzXjg1E7c3%2FFzAVxDgw0zmBGJFdfxDcB6Nqs7G0lvOGs%2FDyadCggbcAsVFw6ClqRSRuw0e0p9X3aShG7i7iwhXVSuiGKHRCosRYASsDpY00%2BZumX15odhIx%2BfoL4i&X-Amz-Signature=2d962e21c9713164b1956b5fa7d8e27dcbbbe8437d8053c6da84382e8ad8ab45&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ZG774TQ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211327Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID2Evqzo3MV6SVgGxE5n6CN3HLLZRhDpnPtIJGORaOcLAiATvQZZRepnZYwW15KMKtrfw70ZO9JE4GO81HL79YYwlCqIBAiu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMDBwJb7I7fupdo6JJKtwDnCr%2BGFzIX3SK6q7PG31eZSBiy0Z0BiOgh08BB8B6VEr5Io23J9528da4XwqCPcFL4aVGr0RbbkeRyBNsZnKxchPEmV09bUhzSI2e8rDXJrCpziY26LSlmtZ2tApVka%2FtdB%2BCGUme3ii1gQcyocMO2uBIc6%2BZJ9G%2FgAx1%2FWS675dWYhQLhn7HVTL%2FfxpDMmmzBIKQrHm1oy0XhGZce65FVeitg3aaWjfbZri915BNi92T%2BAd26wzIP%2F%2FqhP9TlTCsNb6NwKxaZ5FVpQNaWiWtco2uJ36MXkuYUVVBI11kyCOcZ6X%2BoL1463OUZglcMBb4gemT035QUD6YOuuhSCXiPsbUYG9qdpNICTQPIYtMNnedcxCqqMGxiqCETslB5EtGyShliwjiDu6UxNu%2FX1IvHUhlfe%2Fi9fGMHMCJN5I5sCtinVXddfK7cT%2BePguiEbHznB58K5Ou27PV3vkjTCsimeOvuCZnqs5wk7o2KebduwewkrPMEjX8PBikhPp%2BpU1z3lmawhPSLcwdRcDRz3MugsdvFWDjh2wLMM3UgxwzgGIIvtyLwS2T%2Fifdwfnm5z7ObungJSBx9qorsUfpi4WVeYg%2FU1zSeXtXOT69bCvhCS0eNIZmTFOnJnJ1GEgwmMXvvAY6pgE1UyOMndLVnbc8VufkxtcPd81e9TEbPuVapcCNcydB50rD48FQbDPMnUcwgmgUAEWw%2B725C7vUEgBs7z8OkEQGjpCmkWKz4xHgzXjg1E7c3%2FFzAVxDgw0zmBGJFdfxDcB6Nqs7G0lvOGs%2FDyadCggbcAsVFw6ClqRSRuw0e0p9X3aShG7i7iwhXVSuiGKHRCosRYASsDpY00%2BZumX15odhIx%2BfoL4i&X-Amz-Signature=0ed74bfd7bdf445611264fd8d9c836b606705f2f0569e33e5bffe80d975c7fbf&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ZG774TQ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211327Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID2Evqzo3MV6SVgGxE5n6CN3HLLZRhDpnPtIJGORaOcLAiATvQZZRepnZYwW15KMKtrfw70ZO9JE4GO81HL79YYwlCqIBAiu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMDBwJb7I7fupdo6JJKtwDnCr%2BGFzIX3SK6q7PG31eZSBiy0Z0BiOgh08BB8B6VEr5Io23J9528da4XwqCPcFL4aVGr0RbbkeRyBNsZnKxchPEmV09bUhzSI2e8rDXJrCpziY26LSlmtZ2tApVka%2FtdB%2BCGUme3ii1gQcyocMO2uBIc6%2BZJ9G%2FgAx1%2FWS675dWYhQLhn7HVTL%2FfxpDMmmzBIKQrHm1oy0XhGZce65FVeitg3aaWjfbZri915BNi92T%2BAd26wzIP%2F%2FqhP9TlTCsNb6NwKxaZ5FVpQNaWiWtco2uJ36MXkuYUVVBI11kyCOcZ6X%2BoL1463OUZglcMBb4gemT035QUD6YOuuhSCXiPsbUYG9qdpNICTQPIYtMNnedcxCqqMGxiqCETslB5EtGyShliwjiDu6UxNu%2FX1IvHUhlfe%2Fi9fGMHMCJN5I5sCtinVXddfK7cT%2BePguiEbHznB58K5Ou27PV3vkjTCsimeOvuCZnqs5wk7o2KebduwewkrPMEjX8PBikhPp%2BpU1z3lmawhPSLcwdRcDRz3MugsdvFWDjh2wLMM3UgxwzgGIIvtyLwS2T%2Fifdwfnm5z7ObungJSBx9qorsUfpi4WVeYg%2FU1zSeXtXOT69bCvhCS0eNIZmTFOnJnJ1GEgwmMXvvAY6pgE1UyOMndLVnbc8VufkxtcPd81e9TEbPuVapcCNcydB50rD48FQbDPMnUcwgmgUAEWw%2B725C7vUEgBs7z8OkEQGjpCmkWKz4xHgzXjg1E7c3%2FFzAVxDgw0zmBGJFdfxDcB6Nqs7G0lvOGs%2FDyadCggbcAsVFw6ClqRSRuw0e0p9X3aShG7i7iwhXVSuiGKHRCosRYASsDpY00%2BZumX15odhIx%2BfoL4i&X-Amz-Signature=a8337dbdbb1cf7afb2ada0470ede8ab02a79e4a7692b2bf55dd104355945cd10&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
