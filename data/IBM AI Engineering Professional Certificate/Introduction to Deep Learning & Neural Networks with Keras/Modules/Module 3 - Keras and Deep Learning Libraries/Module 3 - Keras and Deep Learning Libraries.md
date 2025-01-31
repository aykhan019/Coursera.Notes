

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LSL4WGL%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCKNvMGlLdrouqmW8rexQBh5hwcNegIC2EPGyzlt37ZLQIgU2LfCcbtF54M%2FYtMldvE4OCunHAD%2FN8CepoHKw3ORyIqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEBqx5XcIXKD8z4dTircA3SGQ5oE95YB905nJcq1e8kMVr4JufrZSW5r6zpXdhiBg8jsI4ntcG1972CP3QscVwmrUehOWCJH4NuhMWr3PR8TQAQa5l5YKMrEWDb7CiAqOSBXRySkopf9sG%2FR5qKFDdpYY83bDGb%2BpSlLe8ct7dURtq0KKvx8FT3PjRd2ch40OtqbETuhTUvBYFmHcPjMEUT91Q6A90EH12FxBiO5Uus2jZE%2BbKiN5gl%2BAL2fEnT4Bjr5SrS3f%2FCnhV1SGoP5NacJPvaN9OamExz9TcIaLxSBQ5leJ8vntbNLNTlMHa%2FT3h5w60BfIJ63cdVSK%2FJOYKKIkWwC5CmWSXXbhl35LfzcNDznH3XjesM%2B4KimOPwupR7hUbTmAE1TXGkr4vfXCyxHplNKjVLl9Q2cGOqKEUPeq0MH4wxcsF9bjCXdMU7cj6UnqFWMmuwrWvm325JbWi%2BCbsyeOQWMLUQJRH3sSfpQQcKz8QD9XaHCqzLflbR4GsC6By1xojgUI5pBGAA1heJo8Pm1oqLvEq%2FZ17xr%2FXh7i%2FOCuxKOrUM2CuNMMQ3MDIVEYMVL5CZEcL3LQBau11oTYK2PjI32EEfrX9AVUPcMmNXtkfqQggUUEEM6NvekRsPRi%2FPBywJoWsGCMPzq87wGOqUBJSzcuKI%2FWuL8U%2F3VLk3oybzBSFsr1sGY4j8jdJDHTk2Srlv9VNw%2Baw8C3eh9PmqK%2BFl%2BMCJmBKhNDnc08J%2FpsD4z4msNB0z3zp%2Ffi6D0qNtC%2FzHYHooRnSjhz1j6eU7zsWH3ObyRwVZJnliaP11hB8J1CF6S4QaxGh13IHO8pDBxTZ%2BI7yB9KJC3SQt8bxOcuAANV2HNS1bfI6MtoJpd02NzJrIC&X-Amz-Signature=e010070dc2e007720fac52865426bf318c7a59316bf6223e2bd754a60d4b488a&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LSL4WGL%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCKNvMGlLdrouqmW8rexQBh5hwcNegIC2EPGyzlt37ZLQIgU2LfCcbtF54M%2FYtMldvE4OCunHAD%2FN8CepoHKw3ORyIqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEBqx5XcIXKD8z4dTircA3SGQ5oE95YB905nJcq1e8kMVr4JufrZSW5r6zpXdhiBg8jsI4ntcG1972CP3QscVwmrUehOWCJH4NuhMWr3PR8TQAQa5l5YKMrEWDb7CiAqOSBXRySkopf9sG%2FR5qKFDdpYY83bDGb%2BpSlLe8ct7dURtq0KKvx8FT3PjRd2ch40OtqbETuhTUvBYFmHcPjMEUT91Q6A90EH12FxBiO5Uus2jZE%2BbKiN5gl%2BAL2fEnT4Bjr5SrS3f%2FCnhV1SGoP5NacJPvaN9OamExz9TcIaLxSBQ5leJ8vntbNLNTlMHa%2FT3h5w60BfIJ63cdVSK%2FJOYKKIkWwC5CmWSXXbhl35LfzcNDznH3XjesM%2B4KimOPwupR7hUbTmAE1TXGkr4vfXCyxHplNKjVLl9Q2cGOqKEUPeq0MH4wxcsF9bjCXdMU7cj6UnqFWMmuwrWvm325JbWi%2BCbsyeOQWMLUQJRH3sSfpQQcKz8QD9XaHCqzLflbR4GsC6By1xojgUI5pBGAA1heJo8Pm1oqLvEq%2FZ17xr%2FXh7i%2FOCuxKOrUM2CuNMMQ3MDIVEYMVL5CZEcL3LQBau11oTYK2PjI32EEfrX9AVUPcMmNXtkfqQggUUEEM6NvekRsPRi%2FPBywJoWsGCMPzq87wGOqUBJSzcuKI%2FWuL8U%2F3VLk3oybzBSFsr1sGY4j8jdJDHTk2Srlv9VNw%2Baw8C3eh9PmqK%2BFl%2BMCJmBKhNDnc08J%2FpsD4z4msNB0z3zp%2Ffi6D0qNtC%2FzHYHooRnSjhz1j6eU7zsWH3ObyRwVZJnliaP11hB8J1CF6S4QaxGh13IHO8pDBxTZ%2BI7yB9KJC3SQt8bxOcuAANV2HNS1bfI6MtoJpd02NzJrIC&X-Amz-Signature=8c12821d4d1c6bad5fe939b37208f1d8732ffe532adc4b6469569913dcff5619&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LSL4WGL%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCKNvMGlLdrouqmW8rexQBh5hwcNegIC2EPGyzlt37ZLQIgU2LfCcbtF54M%2FYtMldvE4OCunHAD%2FN8CepoHKw3ORyIqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEBqx5XcIXKD8z4dTircA3SGQ5oE95YB905nJcq1e8kMVr4JufrZSW5r6zpXdhiBg8jsI4ntcG1972CP3QscVwmrUehOWCJH4NuhMWr3PR8TQAQa5l5YKMrEWDb7CiAqOSBXRySkopf9sG%2FR5qKFDdpYY83bDGb%2BpSlLe8ct7dURtq0KKvx8FT3PjRd2ch40OtqbETuhTUvBYFmHcPjMEUT91Q6A90EH12FxBiO5Uus2jZE%2BbKiN5gl%2BAL2fEnT4Bjr5SrS3f%2FCnhV1SGoP5NacJPvaN9OamExz9TcIaLxSBQ5leJ8vntbNLNTlMHa%2FT3h5w60BfIJ63cdVSK%2FJOYKKIkWwC5CmWSXXbhl35LfzcNDznH3XjesM%2B4KimOPwupR7hUbTmAE1TXGkr4vfXCyxHplNKjVLl9Q2cGOqKEUPeq0MH4wxcsF9bjCXdMU7cj6UnqFWMmuwrWvm325JbWi%2BCbsyeOQWMLUQJRH3sSfpQQcKz8QD9XaHCqzLflbR4GsC6By1xojgUI5pBGAA1heJo8Pm1oqLvEq%2FZ17xr%2FXh7i%2FOCuxKOrUM2CuNMMQ3MDIVEYMVL5CZEcL3LQBau11oTYK2PjI32EEfrX9AVUPcMmNXtkfqQggUUEEM6NvekRsPRi%2FPBywJoWsGCMPzq87wGOqUBJSzcuKI%2FWuL8U%2F3VLk3oybzBSFsr1sGY4j8jdJDHTk2Srlv9VNw%2Baw8C3eh9PmqK%2BFl%2BMCJmBKhNDnc08J%2FpsD4z4msNB0z3zp%2Ffi6D0qNtC%2FzHYHooRnSjhz1j6eU7zsWH3ObyRwVZJnliaP11hB8J1CF6S4QaxGh13IHO8pDBxTZ%2BI7yB9KJC3SQt8bxOcuAANV2HNS1bfI6MtoJpd02NzJrIC&X-Amz-Signature=f95ab8a7ceb0986241acb5f3e1b23a2f75cce5c647f204d2b063afec12aef55b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665OUKBPHT%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDRL%2BkP7pHbHQkO5OQ5XN6HbRCpoQJNLbhw%2Bt4am4fj1AiAzMZ5y6OJOK11Kqi378Fn7sgqc2TmM1vf%2BUQN9KiM15iqIBAjC%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2BKwxrfntcnZNW9nMKtwDfkkpmY9q%2BOFlAr3OA96yrT8Ysa0CtIVw0PD31RAZKX4PkccLa15SuCSlyWMFqhZbyYjVqRjK8oepcWpAneLomTvBLa8MQBdNnxWaLF9Gh4KOOf5MrCjNIYre52GlPqjx75ouDHSVkSAdvdyRjfaD7rdDlrSf58uWHfXwfEpgn3L9HuYP%2BPaIQMAiQ3L4gFoNS0Ij1yzOdSEge62olMzc8qLIw12IzsxTdzJYexJkVXhs0Y287rNwNWAVmNTMHZbjNTSW%2FxEOaVvkn2%2FJ86nredAnIzjwOinswttBjlsj9qsxbzaXklx7rAcI%2BJBn7LKmK97s4nwHZnzzMd6kLHaYD8%2FhAP55gO7U3YCcdcN628vDpP9itd18FQsg4gx9EhMb0vWA44ClsDFP7%2FStX2AkZPii53qsl1HpgQNGX13%2FC09dSfIJ%2FZbqOsgDefsYWNbV3hCMPdWeOKrog0k4C0lcnNeOh7tMXKH%2BhYqj8Ek8Hve2AsD1yaPiQo6QjVV3M9O2YlUKjw4l78ChKJvsvphOZFsJcEGE3AkCL8gBy4v0rDq13MFCoJVSxor5BkNm%2Fk1peQDmeLPj3OoYcN%2F7bMoEJnD6KUf6FskIkiZgEsSYEOtMu7u%2FHj2og8mFhWIwroj0vAY6pgF4sLar93YfyzgmYAcccc%2BXZYqcoHhWECn1vy5Wa5YYiekCHiJjViAv5LE%2BYCZBa7KyyVQ0GnfHF3Z5Wa85gK8AOUzuGPBghomLrKrz6TbH9DuLHe18vz47qVggsv0BmEGVKawl2CmgYNXwGVF4FQ2YKDLOFuHxbDgOd0fw%2BiJNeLOqHZokoc0XhDUy0t2JUQtPSDqRkEyKV4dC7hLsCv2DsfxjBG9e&X-Amz-Signature=7005bd7859dbb38dbfa5c73e3757a40434591021d9f80ff556b01f71ff2fc3dd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YEYJGPDO%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGE7SuVtFaS44GW2ACHA0UtrBkTnePrnf1tz4Us6sIEIAiAg2YRrCyNp7kFd3VxT3B8rCAAGMv2XzJ1U%2B%2Bds0e0NRiqIBAjB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsY%2Ft2xQ521aO1MuJKtwDo9gLDJXOktybdZ5DuGsZ%2F%2FsSS5zajqp4QeLQLu4puCAQhl7DAhp2DwunxvEVyrpqgiIRJRL%2FvCpCgTPKRoHKF%2BpsT4EgPH4Us6WvU8xA9IyL3%2FVrRdPp7mz45VqO%2Bbr7z6iP6r%2F6KyVvvgpqefYDKIuJA813Rpi34tSWifszsQfBRIU2EOUFRtvNuKNtKUMqHv9iomUn4xjNHapBJrFAeQb3YRGppJBlLrQ4J7d%2FW0o7YjidYGu3pdyiAZNRQBY4saIjSyEBeUTPABdndRursdS5%2FKLMGwQqTh1l3y2y8VqvSMj8F1YehYAQrZmViLa69TQu%2FpT3DlIn8AR%2F%2Bh5%2BzXfhexmgop3XELdECal0OYMJEU01Xh%2FmKB7%2FdgNuxqw1jwVy5eJVqptBzbvdetGTyQGvZuFQdDt%2F8goIxOBKIqMua4p7%2BgtFQNGIBZIMLn3sngrHObPxA9WluzH2WoPsr8aMSqRHbeumW%2F6SoBUaLN1xDesPpwTYmTvZyGOPH9FEPBL9xtf%2B9Z7Bwlc2zcluNXV6X5kwhwmxQpIGCnpBDsJFWcjnNAq%2BZ6qvXtt%2FGkRcaZ7%2B5WdqQlAKUiYHJeoaYKcQqNd3wNEat5YUg5dsBI5MxDsizAQUp%2By44fYwtevzvAY6pgFeP4UcRWIXpUvB52izP4oZpnetwN3cF11u9O8M1zUKnfYOzaiw2Gc27pFTeDCzkhFL76R4VKEduiNTULyU1JtyH9cEyMLupFv3BjaQ9ufI20lsBGbdnAL%2FHkjebFgbZpTJRxZWDnoJKOAK%2BR7cDM9iCVIHOXviSTK4TEYcOz4cr91OyrkOEr7c7%2FoerEyOx2N1KL6GSvPvDGWfR1qb4G5sb8gmU5%2Fz&X-Amz-Signature=b02fae5609db0c2d2aee8bd39f382c482394b520f256eda73b6b9f9b027f6476&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LSL4WGL%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCKNvMGlLdrouqmW8rexQBh5hwcNegIC2EPGyzlt37ZLQIgU2LfCcbtF54M%2FYtMldvE4OCunHAD%2FN8CepoHKw3ORyIqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEBqx5XcIXKD8z4dTircA3SGQ5oE95YB905nJcq1e8kMVr4JufrZSW5r6zpXdhiBg8jsI4ntcG1972CP3QscVwmrUehOWCJH4NuhMWr3PR8TQAQa5l5YKMrEWDb7CiAqOSBXRySkopf9sG%2FR5qKFDdpYY83bDGb%2BpSlLe8ct7dURtq0KKvx8FT3PjRd2ch40OtqbETuhTUvBYFmHcPjMEUT91Q6A90EH12FxBiO5Uus2jZE%2BbKiN5gl%2BAL2fEnT4Bjr5SrS3f%2FCnhV1SGoP5NacJPvaN9OamExz9TcIaLxSBQ5leJ8vntbNLNTlMHa%2FT3h5w60BfIJ63cdVSK%2FJOYKKIkWwC5CmWSXXbhl35LfzcNDznH3XjesM%2B4KimOPwupR7hUbTmAE1TXGkr4vfXCyxHplNKjVLl9Q2cGOqKEUPeq0MH4wxcsF9bjCXdMU7cj6UnqFWMmuwrWvm325JbWi%2BCbsyeOQWMLUQJRH3sSfpQQcKz8QD9XaHCqzLflbR4GsC6By1xojgUI5pBGAA1heJo8Pm1oqLvEq%2FZ17xr%2FXh7i%2FOCuxKOrUM2CuNMMQ3MDIVEYMVL5CZEcL3LQBau11oTYK2PjI32EEfrX9AVUPcMmNXtkfqQggUUEEM6NvekRsPRi%2FPBywJoWsGCMPzq87wGOqUBJSzcuKI%2FWuL8U%2F3VLk3oybzBSFsr1sGY4j8jdJDHTk2Srlv9VNw%2Baw8C3eh9PmqK%2BFl%2BMCJmBKhNDnc08J%2FpsD4z4msNB0z3zp%2Ffi6D0qNtC%2FzHYHooRnSjhz1j6eU7zsWH3ObyRwVZJnliaP11hB8J1CF6S4QaxGh13IHO8pDBxTZ%2BI7yB9KJC3SQt8bxOcuAANV2HNS1bfI6MtoJpd02NzJrIC&X-Amz-Signature=dc00d73bbf0e8c68758793b512bd078c50d4b25a77f46df5d934d7483802963c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LSL4WGL%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCKNvMGlLdrouqmW8rexQBh5hwcNegIC2EPGyzlt37ZLQIgU2LfCcbtF54M%2FYtMldvE4OCunHAD%2FN8CepoHKw3ORyIqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEBqx5XcIXKD8z4dTircA3SGQ5oE95YB905nJcq1e8kMVr4JufrZSW5r6zpXdhiBg8jsI4ntcG1972CP3QscVwmrUehOWCJH4NuhMWr3PR8TQAQa5l5YKMrEWDb7CiAqOSBXRySkopf9sG%2FR5qKFDdpYY83bDGb%2BpSlLe8ct7dURtq0KKvx8FT3PjRd2ch40OtqbETuhTUvBYFmHcPjMEUT91Q6A90EH12FxBiO5Uus2jZE%2BbKiN5gl%2BAL2fEnT4Bjr5SrS3f%2FCnhV1SGoP5NacJPvaN9OamExz9TcIaLxSBQ5leJ8vntbNLNTlMHa%2FT3h5w60BfIJ63cdVSK%2FJOYKKIkWwC5CmWSXXbhl35LfzcNDznH3XjesM%2B4KimOPwupR7hUbTmAE1TXGkr4vfXCyxHplNKjVLl9Q2cGOqKEUPeq0MH4wxcsF9bjCXdMU7cj6UnqFWMmuwrWvm325JbWi%2BCbsyeOQWMLUQJRH3sSfpQQcKz8QD9XaHCqzLflbR4GsC6By1xojgUI5pBGAA1heJo8Pm1oqLvEq%2FZ17xr%2FXh7i%2FOCuxKOrUM2CuNMMQ3MDIVEYMVL5CZEcL3LQBau11oTYK2PjI32EEfrX9AVUPcMmNXtkfqQggUUEEM6NvekRsPRi%2FPBywJoWsGCMPzq87wGOqUBJSzcuKI%2FWuL8U%2F3VLk3oybzBSFsr1sGY4j8jdJDHTk2Srlv9VNw%2Baw8C3eh9PmqK%2BFl%2BMCJmBKhNDnc08J%2FpsD4z4msNB0z3zp%2Ffi6D0qNtC%2FzHYHooRnSjhz1j6eU7zsWH3ObyRwVZJnliaP11hB8J1CF6S4QaxGh13IHO8pDBxTZ%2BI7yB9KJC3SQt8bxOcuAANV2HNS1bfI6MtoJpd02NzJrIC&X-Amz-Signature=f2ac864e167db31d0ae64be2425692bcbd6e51bb037bfa95c503bbef594ecf30&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LSL4WGL%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCKNvMGlLdrouqmW8rexQBh5hwcNegIC2EPGyzlt37ZLQIgU2LfCcbtF54M%2FYtMldvE4OCunHAD%2FN8CepoHKw3ORyIqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEBqx5XcIXKD8z4dTircA3SGQ5oE95YB905nJcq1e8kMVr4JufrZSW5r6zpXdhiBg8jsI4ntcG1972CP3QscVwmrUehOWCJH4NuhMWr3PR8TQAQa5l5YKMrEWDb7CiAqOSBXRySkopf9sG%2FR5qKFDdpYY83bDGb%2BpSlLe8ct7dURtq0KKvx8FT3PjRd2ch40OtqbETuhTUvBYFmHcPjMEUT91Q6A90EH12FxBiO5Uus2jZE%2BbKiN5gl%2BAL2fEnT4Bjr5SrS3f%2FCnhV1SGoP5NacJPvaN9OamExz9TcIaLxSBQ5leJ8vntbNLNTlMHa%2FT3h5w60BfIJ63cdVSK%2FJOYKKIkWwC5CmWSXXbhl35LfzcNDznH3XjesM%2B4KimOPwupR7hUbTmAE1TXGkr4vfXCyxHplNKjVLl9Q2cGOqKEUPeq0MH4wxcsF9bjCXdMU7cj6UnqFWMmuwrWvm325JbWi%2BCbsyeOQWMLUQJRH3sSfpQQcKz8QD9XaHCqzLflbR4GsC6By1xojgUI5pBGAA1heJo8Pm1oqLvEq%2FZ17xr%2FXh7i%2FOCuxKOrUM2CuNMMQ3MDIVEYMVL5CZEcL3LQBau11oTYK2PjI32EEfrX9AVUPcMmNXtkfqQggUUEEM6NvekRsPRi%2FPBywJoWsGCMPzq87wGOqUBJSzcuKI%2FWuL8U%2F3VLk3oybzBSFsr1sGY4j8jdJDHTk2Srlv9VNw%2Baw8C3eh9PmqK%2BFl%2BMCJmBKhNDnc08J%2FpsD4z4msNB0z3zp%2Ffi6D0qNtC%2FzHYHooRnSjhz1j6eU7zsWH3ObyRwVZJnliaP11hB8J1CF6S4QaxGh13IHO8pDBxTZ%2BI7yB9KJC3SQt8bxOcuAANV2HNS1bfI6MtoJpd02NzJrIC&X-Amz-Signature=16f096cffa0effa04e732a949a7dd48096c1eb7fe0ca07a613ad8cc1053d62cb&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LSL4WGL%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCKNvMGlLdrouqmW8rexQBh5hwcNegIC2EPGyzlt37ZLQIgU2LfCcbtF54M%2FYtMldvE4OCunHAD%2FN8CepoHKw3ORyIqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEBqx5XcIXKD8z4dTircA3SGQ5oE95YB905nJcq1e8kMVr4JufrZSW5r6zpXdhiBg8jsI4ntcG1972CP3QscVwmrUehOWCJH4NuhMWr3PR8TQAQa5l5YKMrEWDb7CiAqOSBXRySkopf9sG%2FR5qKFDdpYY83bDGb%2BpSlLe8ct7dURtq0KKvx8FT3PjRd2ch40OtqbETuhTUvBYFmHcPjMEUT91Q6A90EH12FxBiO5Uus2jZE%2BbKiN5gl%2BAL2fEnT4Bjr5SrS3f%2FCnhV1SGoP5NacJPvaN9OamExz9TcIaLxSBQ5leJ8vntbNLNTlMHa%2FT3h5w60BfIJ63cdVSK%2FJOYKKIkWwC5CmWSXXbhl35LfzcNDznH3XjesM%2B4KimOPwupR7hUbTmAE1TXGkr4vfXCyxHplNKjVLl9Q2cGOqKEUPeq0MH4wxcsF9bjCXdMU7cj6UnqFWMmuwrWvm325JbWi%2BCbsyeOQWMLUQJRH3sSfpQQcKz8QD9XaHCqzLflbR4GsC6By1xojgUI5pBGAA1heJo8Pm1oqLvEq%2FZ17xr%2FXh7i%2FOCuxKOrUM2CuNMMQ3MDIVEYMVL5CZEcL3LQBau11oTYK2PjI32EEfrX9AVUPcMmNXtkfqQggUUEEM6NvekRsPRi%2FPBywJoWsGCMPzq87wGOqUBJSzcuKI%2FWuL8U%2F3VLk3oybzBSFsr1sGY4j8jdJDHTk2Srlv9VNw%2Baw8C3eh9PmqK%2BFl%2BMCJmBKhNDnc08J%2FpsD4z4msNB0z3zp%2Ffi6D0qNtC%2FzHYHooRnSjhz1j6eU7zsWH3ObyRwVZJnliaP11hB8J1CF6S4QaxGh13IHO8pDBxTZ%2BI7yB9KJC3SQt8bxOcuAANV2HNS1bfI6MtoJpd02NzJrIC&X-Amz-Signature=a57b1a8a76162c253ea8c477695e8c660a881773880b4ab9fbf58f341ff77934&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
