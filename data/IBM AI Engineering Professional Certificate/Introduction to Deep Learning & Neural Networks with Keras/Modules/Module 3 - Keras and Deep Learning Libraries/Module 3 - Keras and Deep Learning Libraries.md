

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RRATHSVF%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T141358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJIMEYCIQDMsb6o%2F3SN1g0jnXeng74g25WPY2OP%2BPV%2FGlv%2B0RDhEgIhANZhAiWAgo7TmboyhV1YFHCJVODrPTuIukXdxXXWTywVKv8DCC8QABoMNjM3NDIzMTgzODA1IgxFB4JA2RjCPxNL%2FLYq3AN4k68ijthTjP6d43koOmyzlJKes9vV5XzH60g1ggSR7O%2FiXkotmUKiY2iHYCHtkmpjjWltRPFOJelvq5zoNu6cLAlswlsdAp1sDzO8rTT%2FtQ9FxbWdfMSVOeJVYdoSWa4N%2BM8DtZAarfo2lZhVtvatFfJqruw0H3uXuNuA8AaZHNu%2FcLQvCsl9eqRqdLXA7Dwfxbqs1POrAm%2BC4KKfxdtXQnSwWb1wNOnSoAqSg2iSKtyZNwBVG%2Funiiz%2BiLKzc%2F7HLJmFpKJGkD8ufTHX2lRo%2FGOmnoMsYaJi4EcfnX%2BEyt%2Fw0pH0uIsTv3pIbSaxP4RAohcWa8xcULfQTakcAZnE2c7NaozTI2%2FR3JgzytQxsAxe19DBLSRquin6tk2a0FYTcYlTz0oM7twN4JNXBp93CuPYy%2BWfz1s%2FRYz9wjEV9liy9PhneXo3ab0elXlh4i9LolhAudZNDqWga2Gtx9aWblyexEd8yEHA7jq0dZnnr5YGWLZLjv3iuWpJspPVLN1g6ZVHyiVbuKeZDYnWcIipkqseJNFlwfrixs4eyTp8PemW2ZH01VhEYRexXwSvM2ctcCgp4bAr0YGRUy02fSuGJKm772%2BM21LVpS%2BhcyHRiyu1CvfUb6rsUeMDqjDRvIi9BjqkAahS70fIPXkglHaf4ABbUXAoRbc4FWqW1o4V5pVboQYfKZGQB9KxdfmoHk%2FxMG1cNJgmPFKk7qOVHzG3R14K3Tr6rftGpEawNhMEbRY0YVKROaAxca57rSMeN0R7OpmFT%2FOjSkdzta6CfJ5uWJvNLfNzsCv%2B1%2FryFMNinDXLP8QLvBDUShkYPD%2BXxu8SQcBu%2BdLDwMJaK6HR%2FPB%2BeREioAqNoWkw&X-Amz-Signature=4107849035619ab35c464577df58a08211a8bdf7601f41dbf89da7280658d6a7&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RRATHSVF%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T141358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJIMEYCIQDMsb6o%2F3SN1g0jnXeng74g25WPY2OP%2BPV%2FGlv%2B0RDhEgIhANZhAiWAgo7TmboyhV1YFHCJVODrPTuIukXdxXXWTywVKv8DCC8QABoMNjM3NDIzMTgzODA1IgxFB4JA2RjCPxNL%2FLYq3AN4k68ijthTjP6d43koOmyzlJKes9vV5XzH60g1ggSR7O%2FiXkotmUKiY2iHYCHtkmpjjWltRPFOJelvq5zoNu6cLAlswlsdAp1sDzO8rTT%2FtQ9FxbWdfMSVOeJVYdoSWa4N%2BM8DtZAarfo2lZhVtvatFfJqruw0H3uXuNuA8AaZHNu%2FcLQvCsl9eqRqdLXA7Dwfxbqs1POrAm%2BC4KKfxdtXQnSwWb1wNOnSoAqSg2iSKtyZNwBVG%2Funiiz%2BiLKzc%2F7HLJmFpKJGkD8ufTHX2lRo%2FGOmnoMsYaJi4EcfnX%2BEyt%2Fw0pH0uIsTv3pIbSaxP4RAohcWa8xcULfQTakcAZnE2c7NaozTI2%2FR3JgzytQxsAxe19DBLSRquin6tk2a0FYTcYlTz0oM7twN4JNXBp93CuPYy%2BWfz1s%2FRYz9wjEV9liy9PhneXo3ab0elXlh4i9LolhAudZNDqWga2Gtx9aWblyexEd8yEHA7jq0dZnnr5YGWLZLjv3iuWpJspPVLN1g6ZVHyiVbuKeZDYnWcIipkqseJNFlwfrixs4eyTp8PemW2ZH01VhEYRexXwSvM2ctcCgp4bAr0YGRUy02fSuGJKm772%2BM21LVpS%2BhcyHRiyu1CvfUb6rsUeMDqjDRvIi9BjqkAahS70fIPXkglHaf4ABbUXAoRbc4FWqW1o4V5pVboQYfKZGQB9KxdfmoHk%2FxMG1cNJgmPFKk7qOVHzG3R14K3Tr6rftGpEawNhMEbRY0YVKROaAxca57rSMeN0R7OpmFT%2FOjSkdzta6CfJ5uWJvNLfNzsCv%2B1%2FryFMNinDXLP8QLvBDUShkYPD%2BXxu8SQcBu%2BdLDwMJaK6HR%2FPB%2BeREioAqNoWkw&X-Amz-Signature=02ab2e9457e23e49ea8206a450743d93558e71eb7cf15ee2e86b05b876b68ea9&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RRATHSVF%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T141358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJIMEYCIQDMsb6o%2F3SN1g0jnXeng74g25WPY2OP%2BPV%2FGlv%2B0RDhEgIhANZhAiWAgo7TmboyhV1YFHCJVODrPTuIukXdxXXWTywVKv8DCC8QABoMNjM3NDIzMTgzODA1IgxFB4JA2RjCPxNL%2FLYq3AN4k68ijthTjP6d43koOmyzlJKes9vV5XzH60g1ggSR7O%2FiXkotmUKiY2iHYCHtkmpjjWltRPFOJelvq5zoNu6cLAlswlsdAp1sDzO8rTT%2FtQ9FxbWdfMSVOeJVYdoSWa4N%2BM8DtZAarfo2lZhVtvatFfJqruw0H3uXuNuA8AaZHNu%2FcLQvCsl9eqRqdLXA7Dwfxbqs1POrAm%2BC4KKfxdtXQnSwWb1wNOnSoAqSg2iSKtyZNwBVG%2Funiiz%2BiLKzc%2F7HLJmFpKJGkD8ufTHX2lRo%2FGOmnoMsYaJi4EcfnX%2BEyt%2Fw0pH0uIsTv3pIbSaxP4RAohcWa8xcULfQTakcAZnE2c7NaozTI2%2FR3JgzytQxsAxe19DBLSRquin6tk2a0FYTcYlTz0oM7twN4JNXBp93CuPYy%2BWfz1s%2FRYz9wjEV9liy9PhneXo3ab0elXlh4i9LolhAudZNDqWga2Gtx9aWblyexEd8yEHA7jq0dZnnr5YGWLZLjv3iuWpJspPVLN1g6ZVHyiVbuKeZDYnWcIipkqseJNFlwfrixs4eyTp8PemW2ZH01VhEYRexXwSvM2ctcCgp4bAr0YGRUy02fSuGJKm772%2BM21LVpS%2BhcyHRiyu1CvfUb6rsUeMDqjDRvIi9BjqkAahS70fIPXkglHaf4ABbUXAoRbc4FWqW1o4V5pVboQYfKZGQB9KxdfmoHk%2FxMG1cNJgmPFKk7qOVHzG3R14K3Tr6rftGpEawNhMEbRY0YVKROaAxca57rSMeN0R7OpmFT%2FOjSkdzta6CfJ5uWJvNLfNzsCv%2B1%2FryFMNinDXLP8QLvBDUShkYPD%2BXxu8SQcBu%2BdLDwMJaK6HR%2FPB%2BeREioAqNoWkw&X-Amz-Signature=d5123ea31bdb01f06deda3ce4017296bc5beee3e4ba897768ba5010d3bbf9044&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJBM2X4R%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T141358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJIMEYCIQDEskFQqe5uH8mg3Ai0Jek2RuFF9K6hpsAWzl33y1zKggIhAKgMMiuvw1HF52%2F9fI%2BhjfkxlB%2BHTe9h8Z6kVKybQEoQKv8DCC8QABoMNjM3NDIzMTgzODA1Igztzg5JygJspgr2kzwq3AM4Jcc%2FM31PuhrbuL3wFilzcd%2BWqMk0Nk60TKcuoWEZc5zAspyqaX26VeyNObOULuQE1LkO8MPh4xUio8ibnPoDmljiMg2yd19p6jcwP6Zfyz4Pol8mCNcPju3ZaQ3rg5B36IwzfoUxbjd2LbgqLo%2FFyxJ4qtV9k0vR%2Bp49sAt6ntAUnT3y123cTnscA8M29cPitQ586vM6YyUAa%2FdnEWmhCgZS8wewRWF%2BBmaW0jOMa15bhwf%2Baw8gH7WW6xSea5tDe7Tf4WfDS22N6AF1M4NngaAULezbps4hqGxdhQA1S50AcjFean8m0m%2FPHxtL5Ua1AVph6F8yoSNU%2FWqztQKvaHVx6A%2FYpZZQc9WhSyPjNXOV5yEEjp8LuG1Dv%2Frx3CwAMcow4byz%2F1LXo7XHX2ONPbgQO4rbNo8Eyy6jYL3VWYe97ZO4iJfId849hHl7JKeczA77W3iHoQDJZxIGIu%2BTst7oeVWLVWCUssl3oo8lqvungzMY74VcSiPkIQohNKJxJLnhHrd%2BstHqQMishx%2FaFjU3gmn4wMIm56KpTIbjDqhdt7sqqNaYxKDhUGZs4Ya9vBVXMn4iJj%2BkDddCfiqpdnsnUDOqOwBMmiDJbWCy%2FXqG8Funcw1WitJ1kDDpvIi9BjqkARhn5%2BfJoIFYVDcurUzPHS%2Bj0zuEIOy9mBPs8wwwQoiVYXKaUBvAtx8zGckAE%2BA%2BWCbOgLi1yXGqdFSkK33OAQ%2BmKWKYKJlCCRl068GIL41eTDnnTku4F59gqIXaro0PiaCd%2F%2BOOLxQgvOKOJbmUakPi7LGWOnys%2FeHtwprV4iSwifUfxDG90JqT19V%2FSgqbjukeaGs1lx2s8Z30ikisZW3ifaRv&X-Amz-Signature=af386c35af4cc03f924abada6a4b63e8796f4266d81467092db9a81aef91d8d3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QOQIV6IB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T141358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJGMEQCICk2rDlfq9yNFBvYZwAdqEAf7%2FFDBTzrf8u9CSWUV8osAiBVM4CNoR10w%2F%2BxadkzE2zYWVHwPukhtZxsu5eEO8vfTyr%2FAwgvEAAaDDYzNzQyMzE4MzgwNSIMOaeKA2kEbfNdzEqFKtwDh7iJwItwjZj8LMmKn845Jb856LAuhuDW9cTAb9FlRhCAw1BnWsmbl5qlSUR4o5dAykrQZgt6IARyQq8CE5BG%2FK72XT9VqTDbxjH7za2zzuA%2BClsVo6kZlbwX2BXExF3cMUmDd9EUIkAcdbVut9b5TyBOy0wZCRVFX4cpDLNWlpDf08MZJqFEmmMBqcjvsEBzh%2Bu8AmmnlgX6O8D77JtfgMt%2Fj8q4A9e0GF6tDbjn2M%2BXIKx6Gjs8SJAAR0sXZ34f%2F4nM5X6tp6jGhLPyuQgw1wxJOL7ecBGS5LDWTrgR4a79GBlrr5QFF2iCAMbGG9Troo3WfN25nBfod7G%2Fpi7I15H04wXIExsjwM89L6Dpnl%2BLtVTF4a6btaO73CXkov0vAIISbZ13ritczjiE23QGcfXTbU1tSYCfmdTlkTmVnvXqC8Sg8wMDeMO9vD4sILwrFmmXy1gufh5uLewu7H%2FSEkN665RJfVAuaqru0BPHdO1gRXT7hAm1LWL7PUkmYDDoVOJuuYDPSeKTv8b0XeXfA9tszindrrTntBw91P5d46kARXDapWP9GUnLAq%2FaZ7oobIPgyUGjwOk%2Bbp3C%2FUh0j2Ez086XvnQuhpp%2BfsrqvY6beweQpNAUxuPbPUUwkb2IvQY6pgEfB72hAwQ5lNLqgi941Tql7bPDH4yddXAZFZZAQkhmCzqZvgHWbW5SICg1AYGJ5EM4uZ%2FzqdCQhDVxUFwSrRb7JdPpZ%2BXjSx2%2FnG2dP415EjrxzyECZPlMhVZUgq3vS1FtyeMMAfGwmU4RyIwQy%2FOc1Kry3UcVDbixfA6fb05RR9mvh%2BS4lxc%2BJIM6CXR5GeXmrq3PXcvpWahiIgdFxmX8ethImjB8&X-Amz-Signature=bd2c9b9ebdd999eb024f365f5c62996e17ea88fe5be97b6d86c55f1a3b46cbc1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RRATHSVF%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T141358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJIMEYCIQDMsb6o%2F3SN1g0jnXeng74g25WPY2OP%2BPV%2FGlv%2B0RDhEgIhANZhAiWAgo7TmboyhV1YFHCJVODrPTuIukXdxXXWTywVKv8DCC8QABoMNjM3NDIzMTgzODA1IgxFB4JA2RjCPxNL%2FLYq3AN4k68ijthTjP6d43koOmyzlJKes9vV5XzH60g1ggSR7O%2FiXkotmUKiY2iHYCHtkmpjjWltRPFOJelvq5zoNu6cLAlswlsdAp1sDzO8rTT%2FtQ9FxbWdfMSVOeJVYdoSWa4N%2BM8DtZAarfo2lZhVtvatFfJqruw0H3uXuNuA8AaZHNu%2FcLQvCsl9eqRqdLXA7Dwfxbqs1POrAm%2BC4KKfxdtXQnSwWb1wNOnSoAqSg2iSKtyZNwBVG%2Funiiz%2BiLKzc%2F7HLJmFpKJGkD8ufTHX2lRo%2FGOmnoMsYaJi4EcfnX%2BEyt%2Fw0pH0uIsTv3pIbSaxP4RAohcWa8xcULfQTakcAZnE2c7NaozTI2%2FR3JgzytQxsAxe19DBLSRquin6tk2a0FYTcYlTz0oM7twN4JNXBp93CuPYy%2BWfz1s%2FRYz9wjEV9liy9PhneXo3ab0elXlh4i9LolhAudZNDqWga2Gtx9aWblyexEd8yEHA7jq0dZnnr5YGWLZLjv3iuWpJspPVLN1g6ZVHyiVbuKeZDYnWcIipkqseJNFlwfrixs4eyTp8PemW2ZH01VhEYRexXwSvM2ctcCgp4bAr0YGRUy02fSuGJKm772%2BM21LVpS%2BhcyHRiyu1CvfUb6rsUeMDqjDRvIi9BjqkAahS70fIPXkglHaf4ABbUXAoRbc4FWqW1o4V5pVboQYfKZGQB9KxdfmoHk%2FxMG1cNJgmPFKk7qOVHzG3R14K3Tr6rftGpEawNhMEbRY0YVKROaAxca57rSMeN0R7OpmFT%2FOjSkdzta6CfJ5uWJvNLfNzsCv%2B1%2FryFMNinDXLP8QLvBDUShkYPD%2BXxu8SQcBu%2BdLDwMJaK6HR%2FPB%2BeREioAqNoWkw&X-Amz-Signature=58326da0d83be12593c07b41e659bef5dcd98c2e37adae2ecbda3fc3130a5351&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RRATHSVF%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T141358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJIMEYCIQDMsb6o%2F3SN1g0jnXeng74g25WPY2OP%2BPV%2FGlv%2B0RDhEgIhANZhAiWAgo7TmboyhV1YFHCJVODrPTuIukXdxXXWTywVKv8DCC8QABoMNjM3NDIzMTgzODA1IgxFB4JA2RjCPxNL%2FLYq3AN4k68ijthTjP6d43koOmyzlJKes9vV5XzH60g1ggSR7O%2FiXkotmUKiY2iHYCHtkmpjjWltRPFOJelvq5zoNu6cLAlswlsdAp1sDzO8rTT%2FtQ9FxbWdfMSVOeJVYdoSWa4N%2BM8DtZAarfo2lZhVtvatFfJqruw0H3uXuNuA8AaZHNu%2FcLQvCsl9eqRqdLXA7Dwfxbqs1POrAm%2BC4KKfxdtXQnSwWb1wNOnSoAqSg2iSKtyZNwBVG%2Funiiz%2BiLKzc%2F7HLJmFpKJGkD8ufTHX2lRo%2FGOmnoMsYaJi4EcfnX%2BEyt%2Fw0pH0uIsTv3pIbSaxP4RAohcWa8xcULfQTakcAZnE2c7NaozTI2%2FR3JgzytQxsAxe19DBLSRquin6tk2a0FYTcYlTz0oM7twN4JNXBp93CuPYy%2BWfz1s%2FRYz9wjEV9liy9PhneXo3ab0elXlh4i9LolhAudZNDqWga2Gtx9aWblyexEd8yEHA7jq0dZnnr5YGWLZLjv3iuWpJspPVLN1g6ZVHyiVbuKeZDYnWcIipkqseJNFlwfrixs4eyTp8PemW2ZH01VhEYRexXwSvM2ctcCgp4bAr0YGRUy02fSuGJKm772%2BM21LVpS%2BhcyHRiyu1CvfUb6rsUeMDqjDRvIi9BjqkAahS70fIPXkglHaf4ABbUXAoRbc4FWqW1o4V5pVboQYfKZGQB9KxdfmoHk%2FxMG1cNJgmPFKk7qOVHzG3R14K3Tr6rftGpEawNhMEbRY0YVKROaAxca57rSMeN0R7OpmFT%2FOjSkdzta6CfJ5uWJvNLfNzsCv%2B1%2FryFMNinDXLP8QLvBDUShkYPD%2BXxu8SQcBu%2BdLDwMJaK6HR%2FPB%2BeREioAqNoWkw&X-Amz-Signature=8ed423a03016c4bf750121dc9ca5074f1187c49b847411fe7ac331821f20672d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RRATHSVF%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T141358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJIMEYCIQDMsb6o%2F3SN1g0jnXeng74g25WPY2OP%2BPV%2FGlv%2B0RDhEgIhANZhAiWAgo7TmboyhV1YFHCJVODrPTuIukXdxXXWTywVKv8DCC8QABoMNjM3NDIzMTgzODA1IgxFB4JA2RjCPxNL%2FLYq3AN4k68ijthTjP6d43koOmyzlJKes9vV5XzH60g1ggSR7O%2FiXkotmUKiY2iHYCHtkmpjjWltRPFOJelvq5zoNu6cLAlswlsdAp1sDzO8rTT%2FtQ9FxbWdfMSVOeJVYdoSWa4N%2BM8DtZAarfo2lZhVtvatFfJqruw0H3uXuNuA8AaZHNu%2FcLQvCsl9eqRqdLXA7Dwfxbqs1POrAm%2BC4KKfxdtXQnSwWb1wNOnSoAqSg2iSKtyZNwBVG%2Funiiz%2BiLKzc%2F7HLJmFpKJGkD8ufTHX2lRo%2FGOmnoMsYaJi4EcfnX%2BEyt%2Fw0pH0uIsTv3pIbSaxP4RAohcWa8xcULfQTakcAZnE2c7NaozTI2%2FR3JgzytQxsAxe19DBLSRquin6tk2a0FYTcYlTz0oM7twN4JNXBp93CuPYy%2BWfz1s%2FRYz9wjEV9liy9PhneXo3ab0elXlh4i9LolhAudZNDqWga2Gtx9aWblyexEd8yEHA7jq0dZnnr5YGWLZLjv3iuWpJspPVLN1g6ZVHyiVbuKeZDYnWcIipkqseJNFlwfrixs4eyTp8PemW2ZH01VhEYRexXwSvM2ctcCgp4bAr0YGRUy02fSuGJKm772%2BM21LVpS%2BhcyHRiyu1CvfUb6rsUeMDqjDRvIi9BjqkAahS70fIPXkglHaf4ABbUXAoRbc4FWqW1o4V5pVboQYfKZGQB9KxdfmoHk%2FxMG1cNJgmPFKk7qOVHzG3R14K3Tr6rftGpEawNhMEbRY0YVKROaAxca57rSMeN0R7OpmFT%2FOjSkdzta6CfJ5uWJvNLfNzsCv%2B1%2FryFMNinDXLP8QLvBDUShkYPD%2BXxu8SQcBu%2BdLDwMJaK6HR%2FPB%2BeREioAqNoWkw&X-Amz-Signature=161e5e769c46289e1fc1f2fd1a320a9d505ad1c10a556969211e91d837980134&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RRATHSVF%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T141358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJIMEYCIQDMsb6o%2F3SN1g0jnXeng74g25WPY2OP%2BPV%2FGlv%2B0RDhEgIhANZhAiWAgo7TmboyhV1YFHCJVODrPTuIukXdxXXWTywVKv8DCC8QABoMNjM3NDIzMTgzODA1IgxFB4JA2RjCPxNL%2FLYq3AN4k68ijthTjP6d43koOmyzlJKes9vV5XzH60g1ggSR7O%2FiXkotmUKiY2iHYCHtkmpjjWltRPFOJelvq5zoNu6cLAlswlsdAp1sDzO8rTT%2FtQ9FxbWdfMSVOeJVYdoSWa4N%2BM8DtZAarfo2lZhVtvatFfJqruw0H3uXuNuA8AaZHNu%2FcLQvCsl9eqRqdLXA7Dwfxbqs1POrAm%2BC4KKfxdtXQnSwWb1wNOnSoAqSg2iSKtyZNwBVG%2Funiiz%2BiLKzc%2F7HLJmFpKJGkD8ufTHX2lRo%2FGOmnoMsYaJi4EcfnX%2BEyt%2Fw0pH0uIsTv3pIbSaxP4RAohcWa8xcULfQTakcAZnE2c7NaozTI2%2FR3JgzytQxsAxe19DBLSRquin6tk2a0FYTcYlTz0oM7twN4JNXBp93CuPYy%2BWfz1s%2FRYz9wjEV9liy9PhneXo3ab0elXlh4i9LolhAudZNDqWga2Gtx9aWblyexEd8yEHA7jq0dZnnr5YGWLZLjv3iuWpJspPVLN1g6ZVHyiVbuKeZDYnWcIipkqseJNFlwfrixs4eyTp8PemW2ZH01VhEYRexXwSvM2ctcCgp4bAr0YGRUy02fSuGJKm772%2BM21LVpS%2BhcyHRiyu1CvfUb6rsUeMDqjDRvIi9BjqkAahS70fIPXkglHaf4ABbUXAoRbc4FWqW1o4V5pVboQYfKZGQB9KxdfmoHk%2FxMG1cNJgmPFKk7qOVHzG3R14K3Tr6rftGpEawNhMEbRY0YVKROaAxca57rSMeN0R7OpmFT%2FOjSkdzta6CfJ5uWJvNLfNzsCv%2B1%2FryFMNinDXLP8QLvBDUShkYPD%2BXxu8SQcBu%2BdLDwMJaK6HR%2FPB%2BeREioAqNoWkw&X-Amz-Signature=74c8d22f133ea1eabe2b71bb88fecbc3f4f05c1302e70364897ffd89d13e94a2&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
