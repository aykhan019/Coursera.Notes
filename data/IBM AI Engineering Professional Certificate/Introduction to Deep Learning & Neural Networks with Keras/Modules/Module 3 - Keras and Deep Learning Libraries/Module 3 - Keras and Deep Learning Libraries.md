

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WIJP33SV%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJGMEQCIFoqeeeGNYeOG1bCJjwAjQU3QjYTpkgGUvaWZJpmCccUAiAEkmCtVOXyp0BXWCnX7QTROxyAb20z4Vj6rENjwCr6rSr%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMtTaSXMzSci2TwbwsKtwDNIJ5ylvw5iMYF%2FJoUCQvGhff6%2BecfrMorgcL70cmvbzWgDb1Pdh25c0m2%2B1FZ5%2BsD9hJHTgfFWMFXzhdvVnxMagprlRk2xAdA8VoPYeYxAsFHe4bII4vbNSK4S2%2Fn0LNvN0NU5R11bPyr%2BhODNAQ1t6%2FyQao1hIprqNSC7tEKlYMlX5J%2FTeESIqOJM6AR2108IR2vj4BSCIaktqczUe%2Br2Rlitr%2FBvFb21MGIMPFHZIVuOzjrEHW%2BouaW553nDllDYU85E%2FkKZTDKHArNmal%2FXB6kqij5CTlQD7uEB8atONvhrye%2Fjb9f%2BaMZjrQZcKLFUS%2BDBZVzoX9b5KGzHyhItuGiBu9icQEPRfkaMT7ciN3r6SW%2FKF7zTNygMbnK4QABkla91I5kKwzEWmtxFYQ%2Bd08EWMShUZt%2BWdOrvXmJc1WGmy5JcOfLuoGPuO%2F6gHOszcXp8sCU3fd0xlERP8QzkDFdS8C9CcCBGeK%2Fq%2Fyp4aCuvuJzYGnhJt%2BUf8VOFdKWjVM3QID9AXry1%2FBjKRP1pYGhvGWw1TauzfNce%2Bu%2BccAZQpabesjREUzDfGCM4CXmky5QVpOtY%2F9JsTI2v9FgNvwLBVn4tJ96s5JhhEaCxlGC5GyDtYY1CTEm%2Bsw3OaHvQY6pgFtMuto7zerI0bbnZ7el4GHNTEipkp%2F5jmO2f8TwMgO4E9bB6gqGCLfjYXEy4QLU83i2bBZlsVYpinBIV5yVXbeOJSOnetA%2FcwwdAPV1NvPXXZKkHTEdtAn5e%2BUb7aVhz7XNZFzGxXfF6hS0einuDKfoYtAjkAqINX3Z7SKL2SfbfxyLHFVzWHL%2BYebIjIVzaFqkUpfvz8O6GNFYQkst%2B7KkI%2BwB%2Bv6&X-Amz-Signature=ffc29ef30d72eb201be5aae26e7efb8b5af7ffe3e61ecbb1d8650c2408a40d94&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WIJP33SV%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJGMEQCIFoqeeeGNYeOG1bCJjwAjQU3QjYTpkgGUvaWZJpmCccUAiAEkmCtVOXyp0BXWCnX7QTROxyAb20z4Vj6rENjwCr6rSr%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMtTaSXMzSci2TwbwsKtwDNIJ5ylvw5iMYF%2FJoUCQvGhff6%2BecfrMorgcL70cmvbzWgDb1Pdh25c0m2%2B1FZ5%2BsD9hJHTgfFWMFXzhdvVnxMagprlRk2xAdA8VoPYeYxAsFHe4bII4vbNSK4S2%2Fn0LNvN0NU5R11bPyr%2BhODNAQ1t6%2FyQao1hIprqNSC7tEKlYMlX5J%2FTeESIqOJM6AR2108IR2vj4BSCIaktqczUe%2Br2Rlitr%2FBvFb21MGIMPFHZIVuOzjrEHW%2BouaW553nDllDYU85E%2FkKZTDKHArNmal%2FXB6kqij5CTlQD7uEB8atONvhrye%2Fjb9f%2BaMZjrQZcKLFUS%2BDBZVzoX9b5KGzHyhItuGiBu9icQEPRfkaMT7ciN3r6SW%2FKF7zTNygMbnK4QABkla91I5kKwzEWmtxFYQ%2Bd08EWMShUZt%2BWdOrvXmJc1WGmy5JcOfLuoGPuO%2F6gHOszcXp8sCU3fd0xlERP8QzkDFdS8C9CcCBGeK%2Fq%2Fyp4aCuvuJzYGnhJt%2BUf8VOFdKWjVM3QID9AXry1%2FBjKRP1pYGhvGWw1TauzfNce%2Bu%2BccAZQpabesjREUzDfGCM4CXmky5QVpOtY%2F9JsTI2v9FgNvwLBVn4tJ96s5JhhEaCxlGC5GyDtYY1CTEm%2Bsw3OaHvQY6pgFtMuto7zerI0bbnZ7el4GHNTEipkp%2F5jmO2f8TwMgO4E9bB6gqGCLfjYXEy4QLU83i2bBZlsVYpinBIV5yVXbeOJSOnetA%2FcwwdAPV1NvPXXZKkHTEdtAn5e%2BUb7aVhz7XNZFzGxXfF6hS0einuDKfoYtAjkAqINX3Z7SKL2SfbfxyLHFVzWHL%2BYebIjIVzaFqkUpfvz8O6GNFYQkst%2B7KkI%2BwB%2Bv6&X-Amz-Signature=63405e18ac6b8f96be0608bc296dea7f61e7af75cc6d60ba5fe25274b2184e23&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WIJP33SV%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJGMEQCIFoqeeeGNYeOG1bCJjwAjQU3QjYTpkgGUvaWZJpmCccUAiAEkmCtVOXyp0BXWCnX7QTROxyAb20z4Vj6rENjwCr6rSr%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMtTaSXMzSci2TwbwsKtwDNIJ5ylvw5iMYF%2FJoUCQvGhff6%2BecfrMorgcL70cmvbzWgDb1Pdh25c0m2%2B1FZ5%2BsD9hJHTgfFWMFXzhdvVnxMagprlRk2xAdA8VoPYeYxAsFHe4bII4vbNSK4S2%2Fn0LNvN0NU5R11bPyr%2BhODNAQ1t6%2FyQao1hIprqNSC7tEKlYMlX5J%2FTeESIqOJM6AR2108IR2vj4BSCIaktqczUe%2Br2Rlitr%2FBvFb21MGIMPFHZIVuOzjrEHW%2BouaW553nDllDYU85E%2FkKZTDKHArNmal%2FXB6kqij5CTlQD7uEB8atONvhrye%2Fjb9f%2BaMZjrQZcKLFUS%2BDBZVzoX9b5KGzHyhItuGiBu9icQEPRfkaMT7ciN3r6SW%2FKF7zTNygMbnK4QABkla91I5kKwzEWmtxFYQ%2Bd08EWMShUZt%2BWdOrvXmJc1WGmy5JcOfLuoGPuO%2F6gHOszcXp8sCU3fd0xlERP8QzkDFdS8C9CcCBGeK%2Fq%2Fyp4aCuvuJzYGnhJt%2BUf8VOFdKWjVM3QID9AXry1%2FBjKRP1pYGhvGWw1TauzfNce%2Bu%2BccAZQpabesjREUzDfGCM4CXmky5QVpOtY%2F9JsTI2v9FgNvwLBVn4tJ96s5JhhEaCxlGC5GyDtYY1CTEm%2Bsw3OaHvQY6pgFtMuto7zerI0bbnZ7el4GHNTEipkp%2F5jmO2f8TwMgO4E9bB6gqGCLfjYXEy4QLU83i2bBZlsVYpinBIV5yVXbeOJSOnetA%2FcwwdAPV1NvPXXZKkHTEdtAn5e%2BUb7aVhz7XNZFzGxXfF6hS0einuDKfoYtAjkAqINX3Z7SKL2SfbfxyLHFVzWHL%2BYebIjIVzaFqkUpfvz8O6GNFYQkst%2B7KkI%2BwB%2Bv6&X-Amz-Signature=86028b81f48976d7c65a3f39a2945250517d3dcaf0c6d591652b60b029087cf5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46644JTCS77%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJIMEYCIQC3uMjeLRTVUD8x18xCZzckMzSWF6xTSJkyoK3xPVoFWAIhAObX1%2FEGtybbVLoOTqFET%2Fyj3rSncqeQkZQfdaqICPxZKv8DCCwQABoMNjM3NDIzMTgzODA1IgwjAn%2FtcPc25GIL8h4q3AMgN%2BmhffF%2BAD7fz%2FnR9Mmf65POSoAs7WdwlfkeojpzWndhjGGc0yxUk9b4FS%2FwORWHpvVMBVgYHPped1w%2BhBvxKbmGWnXvhStTvpZ8foZ1iMjJAqB2LQDZPgpScgzEtux4TjFBAZnPvQbQFLd2HMeJie6tST4REhF8%2BQ0iCmHuUu%2FlgGaVv%2FC1L7i1VnCfXZfoRNWoV8BolOVtaftclnfzWlMLwp5ZaiBGAeXsoBc3mVG3ZR%2BgUqcolrHU%2B4jr1Z9Y0foxCnWcEFkcuIgnKXTWHrZuNOiIFzLYa1KpMoIVvSC189kV2WXQp17GX4duOFUC4qElwCtvWodwol2nvreN8EABFKruA9gXvRPjkvotoXvwUhUrb5HecO4Li5V4z%2BDsEl0XBog%2BAIEWO8KDx%2F3%2Fyf9MvIKWR%2FAMeCOhk6%2FuvD7ku9hkmxtuKefPFHkuLfKkFeDndzgIUMoTYKln9BbA1qr%2BN0hkTWKyzzF3NYikiSmf10oM1ylPpWYVhlhE9ArX2ZZvPK2SUcNKvO6dyl0flQx%2B1C6TvlhmJZpDC9yJPToZPcrwCURIy3a7uOT9ybGucmSpAE7ZnemR%2FcET%2FSVTn8INjT%2Fjb2x%2FCSRWJrSrq2SFa4bhIymdYNkmIzCJ5oe9BjqkAQXSfS3T69wLDyjWb2E40qvOZ3aFKJsy6s7l9M6b4HcJVoJPFWvZ%2Bm%2BMVm8d4joggYXVgKEZEJBAJT2OBj7k48RAqA%2BgnmXpkcibJyzi4n2C5RDXUOsQp0Xac2MS3R%2FHKADuS4strO8I9zJ%2Fhw%2BybgDGM1rJwnINjbXdqvL6xP5L%2FXJNWDo69B2GE8f%2BvXpvrdpclyK15h43Bgg75izyzeHyvOp0&X-Amz-Signature=530886008d2aebe252384b49dc8a8090be9869dd2dacd79ac58b15fd057c1895&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U3MTUF2W%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJIMEYCIQDORhdvhvja9ZFXaKTANV%2BeYT1xLMVtmXUVASX1Fsi9%2BwIhAKY%2BM%2F5R%2FGC4EN39bpmgA%2BSu3H4vhSd71rSxFad1mNL%2FKv8DCCwQABoMNjM3NDIzMTgzODA1Igy9cYgFbuEKgJBejN0q3AMIcpa2RiTqvV61SeOxwwZKU7iIsxClxhpwCwZkeg4q3IIejxNEFr2%2FHJakZN2mMr4wDRpvTms8gs2CIksQsrOBbC9FwydfycvRpmSLp99y%2Fc8uk1yZXkrfNZylZV%2BWV13XIW3TIVpSxCYuj23KcEkSmfVJvmkEq2NA%2B75S4RGz6oH25dyoEHGD2yz%2FSGMJedx%2BSJV7ufR23%2BXdOdjfF42q4ReXclGwmKavwn5Mh5b0WSQUGOMiX%2Bd7Y82voGd299VZ0e7joW0wetnXHFzTm1R61rJh8fjuaQ4YMjbVy4wqs1iAi0PYdYQ373pZNII2Ry8g4r3aHsKV31N0M6dBMnNsu2zEupZ8knlZlL%2FO6ro6JTxARbEeXLjdFinZegimyCXs6y4K%2Fxm6vRD2aMfrL%2BgW121n8BJ1XC0l8%2B3wQmRhNUH%2F22fxHD1hkYJuac3yQ1RKlIC%2BA4oIaRwd4qd7nC1nCzk4lqRvC9IdoeKHodwxhAQ7nSkfTGBIL7TuxReG1Z9n7gMgGeEkhpF8mHNTVCtx7g3hBIt3YrLPKWN%2FFbECZ%2FgUbL8wRRt0PiX9Ixj6qW9Cgs9n%2FvxvnokWL1z1uQvlcA3g4ICzSu%2BRagawFeH2lnWtY3A6K84W3I809TCG5oe9BjqkAXrLl2c6wdcCnans8b%2Fgbi71gp%2F%2Ber5JihnhJXcc0YcXOncWVySB1wB8NR1UmURTM1HenR9lA3UkZh%2B%2FwyBJKLsYkTH7tKPSZthIJPDAVHVIiEx2lO%2BVqbuqe8xwSAdQi111KbGvBWsfox4lkzNU0e618EvlT%2BzXEZUgmjV1ml9BLCG4Dd6Fw%2FJy%2FYtCsfUOc8I8XSwj1P6YYhkv37RAtHYNNhuP&X-Amz-Signature=c56703c45992f367b97a3c6b16256e911d92a4bb91f92cabca69b0954e5a4604&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WIJP33SV%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJGMEQCIFoqeeeGNYeOG1bCJjwAjQU3QjYTpkgGUvaWZJpmCccUAiAEkmCtVOXyp0BXWCnX7QTROxyAb20z4Vj6rENjwCr6rSr%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMtTaSXMzSci2TwbwsKtwDNIJ5ylvw5iMYF%2FJoUCQvGhff6%2BecfrMorgcL70cmvbzWgDb1Pdh25c0m2%2B1FZ5%2BsD9hJHTgfFWMFXzhdvVnxMagprlRk2xAdA8VoPYeYxAsFHe4bII4vbNSK4S2%2Fn0LNvN0NU5R11bPyr%2BhODNAQ1t6%2FyQao1hIprqNSC7tEKlYMlX5J%2FTeESIqOJM6AR2108IR2vj4BSCIaktqczUe%2Br2Rlitr%2FBvFb21MGIMPFHZIVuOzjrEHW%2BouaW553nDllDYU85E%2FkKZTDKHArNmal%2FXB6kqij5CTlQD7uEB8atONvhrye%2Fjb9f%2BaMZjrQZcKLFUS%2BDBZVzoX9b5KGzHyhItuGiBu9icQEPRfkaMT7ciN3r6SW%2FKF7zTNygMbnK4QABkla91I5kKwzEWmtxFYQ%2Bd08EWMShUZt%2BWdOrvXmJc1WGmy5JcOfLuoGPuO%2F6gHOszcXp8sCU3fd0xlERP8QzkDFdS8C9CcCBGeK%2Fq%2Fyp4aCuvuJzYGnhJt%2BUf8VOFdKWjVM3QID9AXry1%2FBjKRP1pYGhvGWw1TauzfNce%2Bu%2BccAZQpabesjREUzDfGCM4CXmky5QVpOtY%2F9JsTI2v9FgNvwLBVn4tJ96s5JhhEaCxlGC5GyDtYY1CTEm%2Bsw3OaHvQY6pgFtMuto7zerI0bbnZ7el4GHNTEipkp%2F5jmO2f8TwMgO4E9bB6gqGCLfjYXEy4QLU83i2bBZlsVYpinBIV5yVXbeOJSOnetA%2FcwwdAPV1NvPXXZKkHTEdtAn5e%2BUb7aVhz7XNZFzGxXfF6hS0einuDKfoYtAjkAqINX3Z7SKL2SfbfxyLHFVzWHL%2BYebIjIVzaFqkUpfvz8O6GNFYQkst%2B7KkI%2BwB%2Bv6&X-Amz-Signature=50344ed943fe769fe5f5a1e06fdb8e8270c4356172621c39a5efbd3ea3a26df3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WIJP33SV%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJGMEQCIFoqeeeGNYeOG1bCJjwAjQU3QjYTpkgGUvaWZJpmCccUAiAEkmCtVOXyp0BXWCnX7QTROxyAb20z4Vj6rENjwCr6rSr%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMtTaSXMzSci2TwbwsKtwDNIJ5ylvw5iMYF%2FJoUCQvGhff6%2BecfrMorgcL70cmvbzWgDb1Pdh25c0m2%2B1FZ5%2BsD9hJHTgfFWMFXzhdvVnxMagprlRk2xAdA8VoPYeYxAsFHe4bII4vbNSK4S2%2Fn0LNvN0NU5R11bPyr%2BhODNAQ1t6%2FyQao1hIprqNSC7tEKlYMlX5J%2FTeESIqOJM6AR2108IR2vj4BSCIaktqczUe%2Br2Rlitr%2FBvFb21MGIMPFHZIVuOzjrEHW%2BouaW553nDllDYU85E%2FkKZTDKHArNmal%2FXB6kqij5CTlQD7uEB8atONvhrye%2Fjb9f%2BaMZjrQZcKLFUS%2BDBZVzoX9b5KGzHyhItuGiBu9icQEPRfkaMT7ciN3r6SW%2FKF7zTNygMbnK4QABkla91I5kKwzEWmtxFYQ%2Bd08EWMShUZt%2BWdOrvXmJc1WGmy5JcOfLuoGPuO%2F6gHOszcXp8sCU3fd0xlERP8QzkDFdS8C9CcCBGeK%2Fq%2Fyp4aCuvuJzYGnhJt%2BUf8VOFdKWjVM3QID9AXry1%2FBjKRP1pYGhvGWw1TauzfNce%2Bu%2BccAZQpabesjREUzDfGCM4CXmky5QVpOtY%2F9JsTI2v9FgNvwLBVn4tJ96s5JhhEaCxlGC5GyDtYY1CTEm%2Bsw3OaHvQY6pgFtMuto7zerI0bbnZ7el4GHNTEipkp%2F5jmO2f8TwMgO4E9bB6gqGCLfjYXEy4QLU83i2bBZlsVYpinBIV5yVXbeOJSOnetA%2FcwwdAPV1NvPXXZKkHTEdtAn5e%2BUb7aVhz7XNZFzGxXfF6hS0einuDKfoYtAjkAqINX3Z7SKL2SfbfxyLHFVzWHL%2BYebIjIVzaFqkUpfvz8O6GNFYQkst%2B7KkI%2BwB%2Bv6&X-Amz-Signature=f1d638a0155d1877e526bca934875fd29773b0bab1dff37d066fb077be815591&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WIJP33SV%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJGMEQCIFoqeeeGNYeOG1bCJjwAjQU3QjYTpkgGUvaWZJpmCccUAiAEkmCtVOXyp0BXWCnX7QTROxyAb20z4Vj6rENjwCr6rSr%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMtTaSXMzSci2TwbwsKtwDNIJ5ylvw5iMYF%2FJoUCQvGhff6%2BecfrMorgcL70cmvbzWgDb1Pdh25c0m2%2B1FZ5%2BsD9hJHTgfFWMFXzhdvVnxMagprlRk2xAdA8VoPYeYxAsFHe4bII4vbNSK4S2%2Fn0LNvN0NU5R11bPyr%2BhODNAQ1t6%2FyQao1hIprqNSC7tEKlYMlX5J%2FTeESIqOJM6AR2108IR2vj4BSCIaktqczUe%2Br2Rlitr%2FBvFb21MGIMPFHZIVuOzjrEHW%2BouaW553nDllDYU85E%2FkKZTDKHArNmal%2FXB6kqij5CTlQD7uEB8atONvhrye%2Fjb9f%2BaMZjrQZcKLFUS%2BDBZVzoX9b5KGzHyhItuGiBu9icQEPRfkaMT7ciN3r6SW%2FKF7zTNygMbnK4QABkla91I5kKwzEWmtxFYQ%2Bd08EWMShUZt%2BWdOrvXmJc1WGmy5JcOfLuoGPuO%2F6gHOszcXp8sCU3fd0xlERP8QzkDFdS8C9CcCBGeK%2Fq%2Fyp4aCuvuJzYGnhJt%2BUf8VOFdKWjVM3QID9AXry1%2FBjKRP1pYGhvGWw1TauzfNce%2Bu%2BccAZQpabesjREUzDfGCM4CXmky5QVpOtY%2F9JsTI2v9FgNvwLBVn4tJ96s5JhhEaCxlGC5GyDtYY1CTEm%2Bsw3OaHvQY6pgFtMuto7zerI0bbnZ7el4GHNTEipkp%2F5jmO2f8TwMgO4E9bB6gqGCLfjYXEy4QLU83i2bBZlsVYpinBIV5yVXbeOJSOnetA%2FcwwdAPV1NvPXXZKkHTEdtAn5e%2BUb7aVhz7XNZFzGxXfF6hS0einuDKfoYtAjkAqINX3Z7SKL2SfbfxyLHFVzWHL%2BYebIjIVzaFqkUpfvz8O6GNFYQkst%2B7KkI%2BwB%2Bv6&X-Amz-Signature=b8d9c2efec97e5f7e8e4ce772a9822ea56b4ddc7d371affc09865a9cddb999e8&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WIJP33SV%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJGMEQCIFoqeeeGNYeOG1bCJjwAjQU3QjYTpkgGUvaWZJpmCccUAiAEkmCtVOXyp0BXWCnX7QTROxyAb20z4Vj6rENjwCr6rSr%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMtTaSXMzSci2TwbwsKtwDNIJ5ylvw5iMYF%2FJoUCQvGhff6%2BecfrMorgcL70cmvbzWgDb1Pdh25c0m2%2B1FZ5%2BsD9hJHTgfFWMFXzhdvVnxMagprlRk2xAdA8VoPYeYxAsFHe4bII4vbNSK4S2%2Fn0LNvN0NU5R11bPyr%2BhODNAQ1t6%2FyQao1hIprqNSC7tEKlYMlX5J%2FTeESIqOJM6AR2108IR2vj4BSCIaktqczUe%2Br2Rlitr%2FBvFb21MGIMPFHZIVuOzjrEHW%2BouaW553nDllDYU85E%2FkKZTDKHArNmal%2FXB6kqij5CTlQD7uEB8atONvhrye%2Fjb9f%2BaMZjrQZcKLFUS%2BDBZVzoX9b5KGzHyhItuGiBu9icQEPRfkaMT7ciN3r6SW%2FKF7zTNygMbnK4QABkla91I5kKwzEWmtxFYQ%2Bd08EWMShUZt%2BWdOrvXmJc1WGmy5JcOfLuoGPuO%2F6gHOszcXp8sCU3fd0xlERP8QzkDFdS8C9CcCBGeK%2Fq%2Fyp4aCuvuJzYGnhJt%2BUf8VOFdKWjVM3QID9AXry1%2FBjKRP1pYGhvGWw1TauzfNce%2Bu%2BccAZQpabesjREUzDfGCM4CXmky5QVpOtY%2F9JsTI2v9FgNvwLBVn4tJ96s5JhhEaCxlGC5GyDtYY1CTEm%2Bsw3OaHvQY6pgFtMuto7zerI0bbnZ7el4GHNTEipkp%2F5jmO2f8TwMgO4E9bB6gqGCLfjYXEy4QLU83i2bBZlsVYpinBIV5yVXbeOJSOnetA%2FcwwdAPV1NvPXXZKkHTEdtAn5e%2BUb7aVhz7XNZFzGxXfF6hS0einuDKfoYtAjkAqINX3Z7SKL2SfbfxyLHFVzWHL%2BYebIjIVzaFqkUpfvz8O6GNFYQkst%2B7KkI%2BwB%2Bv6&X-Amz-Signature=a6c299727a7cbc158c0426cefcd79e592cc85058bfa11cc47fc4a8c256bf2e94&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
