

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYMEXTTW%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIAhOYO5QI76sWA2p3SKIQ2SF7WW1DXpvwLfjSTWOK7oiAiA9E%2FAzQ4aIWxar6CID8229be6bP1qPKrWbX1wKe0TPRCqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMtkdKpEUe9XIjpxtOKtwDSYLER4SWzoWuo5NAJ2Kezth38felu36hWf8nyKvmV6cQsoJb%2F4b4KUwbYp1k5W5rwmB8QSvBxK6XYs5RjSZ0q%2B78wZqke%2FbY2Ksxx7U%2FWTpXwKDRn2EUf47v5NGOIAQn71tRy5gDnlWZSHlT1rtkoCj7OCleFXPzoeOwrb1qjNXGfU3U4DYblDcvYv1RQ77JkiKCuGeqNhsp5hcSURGl58Zu5jnkuk%2BsVyTPNEihVaY0tqT8UQmo5pNJ9xhthrNmr9STFGFdwIRiTTsJHZfSi%2B3pPh6sr2rquCuqJf9h9Y1iR9WbobejMflDt2YO51lsUhaXCnGQp80AnP8QDArAxvzoJ3DhNDW6Uc2pDAp1FSk3t%2F7lyMfVCBLiRqC7Mp5mI55WqpyAajw489i6q%2FG4g0nhYGZYZjBgvJK2OETyJpGf3OGhabrpodKymh6K78Y2coYEthak6aSfQiqVnfz2S%2BZnefmyLEQ91GKN0WjjclZhsFb0yISAd7w9ZrNBeXMUopTM%2FbYV28XL4YoeIFO7Sg8rLx1itwW3%2BkCOZl5%2BrlIpF6N4CEQq3OdbGMD8dYD1T9Kmq2FGeb1F9Zqo9wQPKXcNqGQ5PKEdGtEDM9fQS3fUe9KfILx5pj8FbHwwo46cvQY6pgG8XGPCmgrbq3ZNKojEiPEIJXMqXDZ29%2F7sD14yhBmO653d3dDqu4O7i5qM%2FyWTU9igauG9PAXcHXAmXrbn7eGylXZvtTigO4J%2BqV5peIR%2FBKi0X2Sj20qNB65SYAdP%2BEIrWL8gs%2FSRUy9zLe8Jlo4MiqR0He%2BNjS7av62MWwuIgWqViAt%2BeglJd1uriW146Z5Gx1%2BWZZtCqPO%2B5JEm4N08psGTDxYl&X-Amz-Signature=d805f698b3f76412630c8d01d5b1b0af9722be1150cf47374a48fe65cf0c8fe2&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYMEXTTW%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIAhOYO5QI76sWA2p3SKIQ2SF7WW1DXpvwLfjSTWOK7oiAiA9E%2FAzQ4aIWxar6CID8229be6bP1qPKrWbX1wKe0TPRCqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMtkdKpEUe9XIjpxtOKtwDSYLER4SWzoWuo5NAJ2Kezth38felu36hWf8nyKvmV6cQsoJb%2F4b4KUwbYp1k5W5rwmB8QSvBxK6XYs5RjSZ0q%2B78wZqke%2FbY2Ksxx7U%2FWTpXwKDRn2EUf47v5NGOIAQn71tRy5gDnlWZSHlT1rtkoCj7OCleFXPzoeOwrb1qjNXGfU3U4DYblDcvYv1RQ77JkiKCuGeqNhsp5hcSURGl58Zu5jnkuk%2BsVyTPNEihVaY0tqT8UQmo5pNJ9xhthrNmr9STFGFdwIRiTTsJHZfSi%2B3pPh6sr2rquCuqJf9h9Y1iR9WbobejMflDt2YO51lsUhaXCnGQp80AnP8QDArAxvzoJ3DhNDW6Uc2pDAp1FSk3t%2F7lyMfVCBLiRqC7Mp5mI55WqpyAajw489i6q%2FG4g0nhYGZYZjBgvJK2OETyJpGf3OGhabrpodKymh6K78Y2coYEthak6aSfQiqVnfz2S%2BZnefmyLEQ91GKN0WjjclZhsFb0yISAd7w9ZrNBeXMUopTM%2FbYV28XL4YoeIFO7Sg8rLx1itwW3%2BkCOZl5%2BrlIpF6N4CEQq3OdbGMD8dYD1T9Kmq2FGeb1F9Zqo9wQPKXcNqGQ5PKEdGtEDM9fQS3fUe9KfILx5pj8FbHwwo46cvQY6pgG8XGPCmgrbq3ZNKojEiPEIJXMqXDZ29%2F7sD14yhBmO653d3dDqu4O7i5qM%2FyWTU9igauG9PAXcHXAmXrbn7eGylXZvtTigO4J%2BqV5peIR%2FBKi0X2Sj20qNB65SYAdP%2BEIrWL8gs%2FSRUy9zLe8Jlo4MiqR0He%2BNjS7av62MWwuIgWqViAt%2BeglJd1uriW146Z5Gx1%2BWZZtCqPO%2B5JEm4N08psGTDxYl&X-Amz-Signature=6df4303db081a0475f84610e2d6d1e3ea20aa07ab784363460477f8ba5f95898&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYMEXTTW%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIAhOYO5QI76sWA2p3SKIQ2SF7WW1DXpvwLfjSTWOK7oiAiA9E%2FAzQ4aIWxar6CID8229be6bP1qPKrWbX1wKe0TPRCqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMtkdKpEUe9XIjpxtOKtwDSYLER4SWzoWuo5NAJ2Kezth38felu36hWf8nyKvmV6cQsoJb%2F4b4KUwbYp1k5W5rwmB8QSvBxK6XYs5RjSZ0q%2B78wZqke%2FbY2Ksxx7U%2FWTpXwKDRn2EUf47v5NGOIAQn71tRy5gDnlWZSHlT1rtkoCj7OCleFXPzoeOwrb1qjNXGfU3U4DYblDcvYv1RQ77JkiKCuGeqNhsp5hcSURGl58Zu5jnkuk%2BsVyTPNEihVaY0tqT8UQmo5pNJ9xhthrNmr9STFGFdwIRiTTsJHZfSi%2B3pPh6sr2rquCuqJf9h9Y1iR9WbobejMflDt2YO51lsUhaXCnGQp80AnP8QDArAxvzoJ3DhNDW6Uc2pDAp1FSk3t%2F7lyMfVCBLiRqC7Mp5mI55WqpyAajw489i6q%2FG4g0nhYGZYZjBgvJK2OETyJpGf3OGhabrpodKymh6K78Y2coYEthak6aSfQiqVnfz2S%2BZnefmyLEQ91GKN0WjjclZhsFb0yISAd7w9ZrNBeXMUopTM%2FbYV28XL4YoeIFO7Sg8rLx1itwW3%2BkCOZl5%2BrlIpF6N4CEQq3OdbGMD8dYD1T9Kmq2FGeb1F9Zqo9wQPKXcNqGQ5PKEdGtEDM9fQS3fUe9KfILx5pj8FbHwwo46cvQY6pgG8XGPCmgrbq3ZNKojEiPEIJXMqXDZ29%2F7sD14yhBmO653d3dDqu4O7i5qM%2FyWTU9igauG9PAXcHXAmXrbn7eGylXZvtTigO4J%2BqV5peIR%2FBKi0X2Sj20qNB65SYAdP%2BEIrWL8gs%2FSRUy9zLe8Jlo4MiqR0He%2BNjS7av62MWwuIgWqViAt%2BeglJd1uriW146Z5Gx1%2BWZZtCqPO%2B5JEm4N08psGTDxYl&X-Amz-Signature=494ecf1a5103beef02fe8fc51b9691e16d66023f6a00011332d3af824038323a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665CHVDX6J%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQDhu30oi4Aq%2FgIqFKReSkgS%2FFqs1eaE16hE0Dx0zlOVLQIgQq3ql7GNCi0DBO24rO4YBwSVUy4HRWHd8yNDKHSBRtgqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEc4NNsMxpNl4xD%2BFyrcA%2FIY0FmqVogrYYhdILLtxzRqCnjPocRDf2CPbaYKMp4GwJ9iw%2Bgr2kaWtTwUSRYBY8jYe%2BoiJcvrSdkFnQ0aO6BX1JD0ITjLEvqgoz2bwdni1RLND11aDeJBaiWWsWCAbrmMMH6eUqyIJvGhxr6RLMySdKazueVKS1kEnNsPhmF3dJBp89nl1t19dLDv64G%2F2WBY9bm6X0rkKQYl4Yh25QXAxFVZKW3hdF2Oa2nRQjE0J1HAxBm3KjaFFz85k%2BTUA5nAkaAerMbc2cgT801Txlug879DBdhuO47NlQsDMywcPnuz6UhyjciP1m%2FycYtB8SwNLyShqwJbpMK15rE55M60MeJTXmQ8fPVa1NgvmwrSaRcJz1sZb62pGMZOndm6C11q6Ro59RJWAMvV%2FnTIU%2FnnQnMb7YmiBOcWUn%2BGkij%2FxTYXjfvEiE4A8ikg0%2F5jFcmNsWx544jhbwGOVk7wxzPAOP9f5gag228suuw94CKYvX%2FC3bvY3TwEaKZWWziJAOebQACqm%2F8StG8JkxUaMol8UZ2FynlbrOfH%2FYGEnS9BAjwL5N8vDQeAecuP3IXyBVC3zdObppLt1%2FDnHKsGhouXvrYcY8lk%2BGNS3HOdARaqDGKohfmcLSTncEteMPGOnL0GOqUBL27UUXxulBmBiqqPziQjclpm%2BFnhzBbCKwric9TQdfZb1njprTK2rHmY%2Bi4taoMdGJU2ZPqGIBruuAjZGJWO3jacRkFKWT7JAYdrVJx%2FG594lM9HqdGWdKW6gri2%2FILWBQQoSll4DXyyblMmKlCwIOtBHHVI8WmIil5HDj8JkeqsA0tyx6yq%2FvCtmE%2BaKdJQHspRRnIjfSvBxI0jq%2BVZerG24m2N&X-Amz-Signature=d3c5a16eebe75ebcc825f3c663a2c3291147288340cf2a6939e7c513a2b2cdf2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TPUXE63%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIBWKK0qsBGBsfi1UinkR3fLfQ0SmBGO7RHq%2FCfiN6EhyAiAVVt1v2k5TZGJ%2FrDq%2FkMK5IDQF00ZMK97g6y4ESYMYyCqIBAiI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM7NKJkSOAy4IAL%2FvDKtwDTHd4mxJlj9nVWfyV6MtmoB8SACYNjnRMf282FG4XEvNkvxu%2F90NOfaUcDgzn0T5iQGCFW6NZr%2FY53ZT%2BdyQUUAcr4y90ETnP4ZWHfKb9JZddgjhHV6V1PuB5ONLFLZLXfJZ%2BEfMWIYcU9CdtvucC%2Fy8rPdu6V8vjhm%2BYV739LGHr6cZ9uckttF%2FM68a38a2DR%2F9gIkA2DelPvkEk6T6rJlvFMsD8AE0HmXoi4BTPWeso5etiPS4yeYm62WYY7f7CXXO0WlKQIAknSKRpjSdi0UGJ0SgD5HENSoR3tPD16BuIi%2FLlqQ75BhSFhDMd1IxVmXVl4g8yOYlHXyqBBAXRQmyMiz8FujoSB%2BuvczNeIjaqAFXDFpyyXLPRdOnz%2FayThTXWMciMJIFZhzI%2FA0iFd%2FHuOoAS59If0BN2H4z%2F8PtifZ6oh9IZyPnsSD%2BxJTTg40qwX5s8d0phx48uiptPEG%2F2rWjegvy2szLQuTa0lt2MRWHRRjpfRQIdVj09d%2BYQ2CV8JJyWa1XAbqn4IHHGLi7eY18lJUojKDB3frl4U90B56baIb7P5vbWION6XvaF8v1JMPSbC%2B6HZblEJb1xyl5m2yQOiSG9ukIirq%2B1NlJmlQC1GU%2F%2FTYjAl5Awro6cvQY6pgHctqMiHt6%2FuiJpIuyS5CIo%2BVbM60%2B%2BEN2eG412EAkFGPlY2VAs%2BpeV%2BVjkWa2MiktePiEgK5bkkGJea8BNsOYxmYJpKq1%2FX97oCduRePhHZEmy40kQ%2F4lVG7IDZ81D1f3do8tdPh%2BCSjTPD3cGtseitqyTCTsXJsm24sIiO8XlTJHDzset24TkqCqYdkwc03XVvJFmzslNsAvhsZ712M4GDPOKmWJk&X-Amz-Signature=6d4c47674d26450f319b329a191929aca1a5785290511e4086541a509aa9af2e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYMEXTTW%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIAhOYO5QI76sWA2p3SKIQ2SF7WW1DXpvwLfjSTWOK7oiAiA9E%2FAzQ4aIWxar6CID8229be6bP1qPKrWbX1wKe0TPRCqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMtkdKpEUe9XIjpxtOKtwDSYLER4SWzoWuo5NAJ2Kezth38felu36hWf8nyKvmV6cQsoJb%2F4b4KUwbYp1k5W5rwmB8QSvBxK6XYs5RjSZ0q%2B78wZqke%2FbY2Ksxx7U%2FWTpXwKDRn2EUf47v5NGOIAQn71tRy5gDnlWZSHlT1rtkoCj7OCleFXPzoeOwrb1qjNXGfU3U4DYblDcvYv1RQ77JkiKCuGeqNhsp5hcSURGl58Zu5jnkuk%2BsVyTPNEihVaY0tqT8UQmo5pNJ9xhthrNmr9STFGFdwIRiTTsJHZfSi%2B3pPh6sr2rquCuqJf9h9Y1iR9WbobejMflDt2YO51lsUhaXCnGQp80AnP8QDArAxvzoJ3DhNDW6Uc2pDAp1FSk3t%2F7lyMfVCBLiRqC7Mp5mI55WqpyAajw489i6q%2FG4g0nhYGZYZjBgvJK2OETyJpGf3OGhabrpodKymh6K78Y2coYEthak6aSfQiqVnfz2S%2BZnefmyLEQ91GKN0WjjclZhsFb0yISAd7w9ZrNBeXMUopTM%2FbYV28XL4YoeIFO7Sg8rLx1itwW3%2BkCOZl5%2BrlIpF6N4CEQq3OdbGMD8dYD1T9Kmq2FGeb1F9Zqo9wQPKXcNqGQ5PKEdGtEDM9fQS3fUe9KfILx5pj8FbHwwo46cvQY6pgG8XGPCmgrbq3ZNKojEiPEIJXMqXDZ29%2F7sD14yhBmO653d3dDqu4O7i5qM%2FyWTU9igauG9PAXcHXAmXrbn7eGylXZvtTigO4J%2BqV5peIR%2FBKi0X2Sj20qNB65SYAdP%2BEIrWL8gs%2FSRUy9zLe8Jlo4MiqR0He%2BNjS7av62MWwuIgWqViAt%2BeglJd1uriW146Z5Gx1%2BWZZtCqPO%2B5JEm4N08psGTDxYl&X-Amz-Signature=1edcf423f4b51a4ba5e85a7d9b669282b8380687e6cb0d5e439018c583a33772&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYMEXTTW%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIAhOYO5QI76sWA2p3SKIQ2SF7WW1DXpvwLfjSTWOK7oiAiA9E%2FAzQ4aIWxar6CID8229be6bP1qPKrWbX1wKe0TPRCqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMtkdKpEUe9XIjpxtOKtwDSYLER4SWzoWuo5NAJ2Kezth38felu36hWf8nyKvmV6cQsoJb%2F4b4KUwbYp1k5W5rwmB8QSvBxK6XYs5RjSZ0q%2B78wZqke%2FbY2Ksxx7U%2FWTpXwKDRn2EUf47v5NGOIAQn71tRy5gDnlWZSHlT1rtkoCj7OCleFXPzoeOwrb1qjNXGfU3U4DYblDcvYv1RQ77JkiKCuGeqNhsp5hcSURGl58Zu5jnkuk%2BsVyTPNEihVaY0tqT8UQmo5pNJ9xhthrNmr9STFGFdwIRiTTsJHZfSi%2B3pPh6sr2rquCuqJf9h9Y1iR9WbobejMflDt2YO51lsUhaXCnGQp80AnP8QDArAxvzoJ3DhNDW6Uc2pDAp1FSk3t%2F7lyMfVCBLiRqC7Mp5mI55WqpyAajw489i6q%2FG4g0nhYGZYZjBgvJK2OETyJpGf3OGhabrpodKymh6K78Y2coYEthak6aSfQiqVnfz2S%2BZnefmyLEQ91GKN0WjjclZhsFb0yISAd7w9ZrNBeXMUopTM%2FbYV28XL4YoeIFO7Sg8rLx1itwW3%2BkCOZl5%2BrlIpF6N4CEQq3OdbGMD8dYD1T9Kmq2FGeb1F9Zqo9wQPKXcNqGQ5PKEdGtEDM9fQS3fUe9KfILx5pj8FbHwwo46cvQY6pgG8XGPCmgrbq3ZNKojEiPEIJXMqXDZ29%2F7sD14yhBmO653d3dDqu4O7i5qM%2FyWTU9igauG9PAXcHXAmXrbn7eGylXZvtTigO4J%2BqV5peIR%2FBKi0X2Sj20qNB65SYAdP%2BEIrWL8gs%2FSRUy9zLe8Jlo4MiqR0He%2BNjS7av62MWwuIgWqViAt%2BeglJd1uriW146Z5Gx1%2BWZZtCqPO%2B5JEm4N08psGTDxYl&X-Amz-Signature=56f95fadd3f80b7a5379f7ed8c0fc76ae6dff65e46780ccf1c158421e5da82c9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYMEXTTW%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIAhOYO5QI76sWA2p3SKIQ2SF7WW1DXpvwLfjSTWOK7oiAiA9E%2FAzQ4aIWxar6CID8229be6bP1qPKrWbX1wKe0TPRCqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMtkdKpEUe9XIjpxtOKtwDSYLER4SWzoWuo5NAJ2Kezth38felu36hWf8nyKvmV6cQsoJb%2F4b4KUwbYp1k5W5rwmB8QSvBxK6XYs5RjSZ0q%2B78wZqke%2FbY2Ksxx7U%2FWTpXwKDRn2EUf47v5NGOIAQn71tRy5gDnlWZSHlT1rtkoCj7OCleFXPzoeOwrb1qjNXGfU3U4DYblDcvYv1RQ77JkiKCuGeqNhsp5hcSURGl58Zu5jnkuk%2BsVyTPNEihVaY0tqT8UQmo5pNJ9xhthrNmr9STFGFdwIRiTTsJHZfSi%2B3pPh6sr2rquCuqJf9h9Y1iR9WbobejMflDt2YO51lsUhaXCnGQp80AnP8QDArAxvzoJ3DhNDW6Uc2pDAp1FSk3t%2F7lyMfVCBLiRqC7Mp5mI55WqpyAajw489i6q%2FG4g0nhYGZYZjBgvJK2OETyJpGf3OGhabrpodKymh6K78Y2coYEthak6aSfQiqVnfz2S%2BZnefmyLEQ91GKN0WjjclZhsFb0yISAd7w9ZrNBeXMUopTM%2FbYV28XL4YoeIFO7Sg8rLx1itwW3%2BkCOZl5%2BrlIpF6N4CEQq3OdbGMD8dYD1T9Kmq2FGeb1F9Zqo9wQPKXcNqGQ5PKEdGtEDM9fQS3fUe9KfILx5pj8FbHwwo46cvQY6pgG8XGPCmgrbq3ZNKojEiPEIJXMqXDZ29%2F7sD14yhBmO653d3dDqu4O7i5qM%2FyWTU9igauG9PAXcHXAmXrbn7eGylXZvtTigO4J%2BqV5peIR%2FBKi0X2Sj20qNB65SYAdP%2BEIrWL8gs%2FSRUy9zLe8Jlo4MiqR0He%2BNjS7av62MWwuIgWqViAt%2BeglJd1uriW146Z5Gx1%2BWZZtCqPO%2B5JEm4N08psGTDxYl&X-Amz-Signature=5bfd4edc0f99c71db0742010e13f2c7a7a3ce63af462f42e18f189584a40bfdd&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYMEXTTW%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIAhOYO5QI76sWA2p3SKIQ2SF7WW1DXpvwLfjSTWOK7oiAiA9E%2FAzQ4aIWxar6CID8229be6bP1qPKrWbX1wKe0TPRCqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMtkdKpEUe9XIjpxtOKtwDSYLER4SWzoWuo5NAJ2Kezth38felu36hWf8nyKvmV6cQsoJb%2F4b4KUwbYp1k5W5rwmB8QSvBxK6XYs5RjSZ0q%2B78wZqke%2FbY2Ksxx7U%2FWTpXwKDRn2EUf47v5NGOIAQn71tRy5gDnlWZSHlT1rtkoCj7OCleFXPzoeOwrb1qjNXGfU3U4DYblDcvYv1RQ77JkiKCuGeqNhsp5hcSURGl58Zu5jnkuk%2BsVyTPNEihVaY0tqT8UQmo5pNJ9xhthrNmr9STFGFdwIRiTTsJHZfSi%2B3pPh6sr2rquCuqJf9h9Y1iR9WbobejMflDt2YO51lsUhaXCnGQp80AnP8QDArAxvzoJ3DhNDW6Uc2pDAp1FSk3t%2F7lyMfVCBLiRqC7Mp5mI55WqpyAajw489i6q%2FG4g0nhYGZYZjBgvJK2OETyJpGf3OGhabrpodKymh6K78Y2coYEthak6aSfQiqVnfz2S%2BZnefmyLEQ91GKN0WjjclZhsFb0yISAd7w9ZrNBeXMUopTM%2FbYV28XL4YoeIFO7Sg8rLx1itwW3%2BkCOZl5%2BrlIpF6N4CEQq3OdbGMD8dYD1T9Kmq2FGeb1F9Zqo9wQPKXcNqGQ5PKEdGtEDM9fQS3fUe9KfILx5pj8FbHwwo46cvQY6pgG8XGPCmgrbq3ZNKojEiPEIJXMqXDZ29%2F7sD14yhBmO653d3dDqu4O7i5qM%2FyWTU9igauG9PAXcHXAmXrbn7eGylXZvtTigO4J%2BqV5peIR%2FBKi0X2Sj20qNB65SYAdP%2BEIrWL8gs%2FSRUy9zLe8Jlo4MiqR0He%2BNjS7av62MWwuIgWqViAt%2BeglJd1uriW146Z5Gx1%2BWZZtCqPO%2B5JEm4N08psGTDxYl&X-Amz-Signature=10ab449a3573762aa872bb49350ed81e960f6847bc3f7d7e03398f9a02395ecd&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
