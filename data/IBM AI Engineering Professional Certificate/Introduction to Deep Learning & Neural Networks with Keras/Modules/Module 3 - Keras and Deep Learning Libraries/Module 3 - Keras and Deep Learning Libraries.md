

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHKQC24I%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJIMEYCIQDW7g0frnS57Tpf5y69UqAfOMSQKRhq74u3w3xuBPuYGwIhAMt0L14QOWUpzqRWcuO%2FUIxYaHUw6fBZYlYQLBgwJJQuKv8DCHAQABoMNjM3NDIzMTgzODA1IgyECEjymb%2BwxMopHdMq3AOY0GafRQoD0ERVaRN2TZUlP0IqYK%2FRtAS7u7xy8Z%2BwX22Pz4aBRxRFvK0II9GZO7hOoCtOzO5JEeDcwVhJbl9t%2Fa3YJp4VwdzupzjSxsGmLUYxoZe0SGkC85VZLdZl4H2YWkWKA29nk4ho8BNgxf0d982FA2qlB6ffs1yKPDn%2FBShHQ4GdAh6ny1%2BGOAs9yC5kV5MokIwZHguk%2FV9GwE1SE%2FKtpbu%2BDwbSxsaaFsOXTw4jOQYjXrFS1LnB38%2FGEdrBJ8AgsZcKGsYTG%2BjWLnYL5yDthKFYk33xc3ld7JFf8J2y6RKtQD9wUGEkrKLqzWX5uDZujsoqJzVY98%2BRcQmmE%2FjueRRHcxcsOoTAzDDzIS%2B4xW8r5jjvcHzkFE9tARjzzaE6GFFmILLLswHFsd6dTMiIPYDLgpf311NUa%2BP732cdk%2BrMj%2Fxo3Hf2wZnreU8jBTLvjfo8GR3xpYlzfTkBrLapGWco%2BBV3B4HmhQTpXe5U7xCV8bW8fDHFJ8Eq2nOiuIWQkx70NNbujLmU7OgIt4c0%2FJZ00tuCATbrQWp7CgnS5Sldc2Sdt7fqfobzfACCa079UfWXwh3NWFXpOSbC6%2BoWIM%2FRrCmHoG2eooPX9GJjgEZP9gYzwgHItzDV3Ja9BjqkAVJyOGX55lefGgqX7evaSXJgfLnk6ImjwNVYSuZAdcnd9RSo6Pn5TBwrMsaKM17wPQOuztB7nuQ5G1vxzuXD%2FL1Jkq8rwRm34A%2BcZl2DlhWhuVJVXiuG7jxft8yE4iWnXOUGBVZQWEdRPOEBQiN8hh%2BSn7C550LOuO4%2FbAtDs%2BEloVGELHGqh8mHDKGd2v2O67htaRlzisxOaP3BygNZ4vcXdpHg&X-Amz-Signature=f4d770c26ed83e43f68ebe1ca000a5b88d1a27761547a0d4dab439e472c6e089&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHKQC24I%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJIMEYCIQDW7g0frnS57Tpf5y69UqAfOMSQKRhq74u3w3xuBPuYGwIhAMt0L14QOWUpzqRWcuO%2FUIxYaHUw6fBZYlYQLBgwJJQuKv8DCHAQABoMNjM3NDIzMTgzODA1IgyECEjymb%2BwxMopHdMq3AOY0GafRQoD0ERVaRN2TZUlP0IqYK%2FRtAS7u7xy8Z%2BwX22Pz4aBRxRFvK0II9GZO7hOoCtOzO5JEeDcwVhJbl9t%2Fa3YJp4VwdzupzjSxsGmLUYxoZe0SGkC85VZLdZl4H2YWkWKA29nk4ho8BNgxf0d982FA2qlB6ffs1yKPDn%2FBShHQ4GdAh6ny1%2BGOAs9yC5kV5MokIwZHguk%2FV9GwE1SE%2FKtpbu%2BDwbSxsaaFsOXTw4jOQYjXrFS1LnB38%2FGEdrBJ8AgsZcKGsYTG%2BjWLnYL5yDthKFYk33xc3ld7JFf8J2y6RKtQD9wUGEkrKLqzWX5uDZujsoqJzVY98%2BRcQmmE%2FjueRRHcxcsOoTAzDDzIS%2B4xW8r5jjvcHzkFE9tARjzzaE6GFFmILLLswHFsd6dTMiIPYDLgpf311NUa%2BP732cdk%2BrMj%2Fxo3Hf2wZnreU8jBTLvjfo8GR3xpYlzfTkBrLapGWco%2BBV3B4HmhQTpXe5U7xCV8bW8fDHFJ8Eq2nOiuIWQkx70NNbujLmU7OgIt4c0%2FJZ00tuCATbrQWp7CgnS5Sldc2Sdt7fqfobzfACCa079UfWXwh3NWFXpOSbC6%2BoWIM%2FRrCmHoG2eooPX9GJjgEZP9gYzwgHItzDV3Ja9BjqkAVJyOGX55lefGgqX7evaSXJgfLnk6ImjwNVYSuZAdcnd9RSo6Pn5TBwrMsaKM17wPQOuztB7nuQ5G1vxzuXD%2FL1Jkq8rwRm34A%2BcZl2DlhWhuVJVXiuG7jxft8yE4iWnXOUGBVZQWEdRPOEBQiN8hh%2BSn7C550LOuO4%2FbAtDs%2BEloVGELHGqh8mHDKGd2v2O67htaRlzisxOaP3BygNZ4vcXdpHg&X-Amz-Signature=e9c3a41b9e536f769ab01a51e65d5cd929f7c356f98fdc5296b1302b5c01323b&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHKQC24I%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJIMEYCIQDW7g0frnS57Tpf5y69UqAfOMSQKRhq74u3w3xuBPuYGwIhAMt0L14QOWUpzqRWcuO%2FUIxYaHUw6fBZYlYQLBgwJJQuKv8DCHAQABoMNjM3NDIzMTgzODA1IgyECEjymb%2BwxMopHdMq3AOY0GafRQoD0ERVaRN2TZUlP0IqYK%2FRtAS7u7xy8Z%2BwX22Pz4aBRxRFvK0II9GZO7hOoCtOzO5JEeDcwVhJbl9t%2Fa3YJp4VwdzupzjSxsGmLUYxoZe0SGkC85VZLdZl4H2YWkWKA29nk4ho8BNgxf0d982FA2qlB6ffs1yKPDn%2FBShHQ4GdAh6ny1%2BGOAs9yC5kV5MokIwZHguk%2FV9GwE1SE%2FKtpbu%2BDwbSxsaaFsOXTw4jOQYjXrFS1LnB38%2FGEdrBJ8AgsZcKGsYTG%2BjWLnYL5yDthKFYk33xc3ld7JFf8J2y6RKtQD9wUGEkrKLqzWX5uDZujsoqJzVY98%2BRcQmmE%2FjueRRHcxcsOoTAzDDzIS%2B4xW8r5jjvcHzkFE9tARjzzaE6GFFmILLLswHFsd6dTMiIPYDLgpf311NUa%2BP732cdk%2BrMj%2Fxo3Hf2wZnreU8jBTLvjfo8GR3xpYlzfTkBrLapGWco%2BBV3B4HmhQTpXe5U7xCV8bW8fDHFJ8Eq2nOiuIWQkx70NNbujLmU7OgIt4c0%2FJZ00tuCATbrQWp7CgnS5Sldc2Sdt7fqfobzfACCa079UfWXwh3NWFXpOSbC6%2BoWIM%2FRrCmHoG2eooPX9GJjgEZP9gYzwgHItzDV3Ja9BjqkAVJyOGX55lefGgqX7evaSXJgfLnk6ImjwNVYSuZAdcnd9RSo6Pn5TBwrMsaKM17wPQOuztB7nuQ5G1vxzuXD%2FL1Jkq8rwRm34A%2BcZl2DlhWhuVJVXiuG7jxft8yE4iWnXOUGBVZQWEdRPOEBQiN8hh%2BSn7C550LOuO4%2FbAtDs%2BEloVGELHGqh8mHDKGd2v2O67htaRlzisxOaP3BygNZ4vcXdpHg&X-Amz-Signature=f478943bcff41c0edf2d4cd7c127dc4df9701df044279252cc08f51125e845f1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LH2JJC5%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071347Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJHMEUCIQCB12IkIVQv2rj87ir2d2hBnF1OrojjKOvYG6KX%2F7nwsgIgZSxpKqUr8rbvpvFkyGtZ76NYPXev%2BKNP8hLqigkaPrgq%2FwMIcBAAGgw2Mzc0MjMxODM4MDUiDDzh04oy0dPiI6GAxSrcA6GPUrjC6i8qeILdGFqfDfccHQnSbDLEboTNKFe80T1gEHNxY0c4pVLOhBAb%2Fn4G4jGBy%2FRbty6INQ%2Bmgov19tavfV%2F%2FjpHqIgZ9J7JrdKcjukPymk8Xdh5HdtIFUjKHVuOGGC4g789urSk6xvChp223JlytBt526X0pPs8agUFbjBvLzOkm%2BHOBj0fsWCFNuQSYstsLjxEEkidgzvPfJlpEC7BGbNIc7ua92IXb57UfC2m18f%2BAjBZqskptpT%2FzbGMNceBEWN00qdlQkz0wNikFSAdIPpFy7AeC%2FFeyLzGrfvZUZeII3YOvgvrryKXf140DY%2B8R9ng1mCjX0vQ7QW%2B0gmQnlpbFbQ%2Fr%2FD0%2FEbfCv5HzP78yL%2F4%2FNc0%2Foqs2fC2ATtGwKUkg9KWGGNsE4Ev%2FYKQwcdDZQmMyHCtZQq6kg2vz9QKrXiZmoQ1IB%2Bfkf2nEBM80AF3Kf%2FczQkyeh7KlMpDeYRJGJ0DsUwnA28Ev2g9Bcspk%2Br3C%2FNeMiupjGO%2Bm966QdASIVXzIVCZhQ6oyNfZGPltj9pgnCVGV4gXWDF8XXRJPqgukLrHNwyNZBKNZ%2FliAAjqyk9jiEdzMiHaZTyIYu4CBq22iJ8OPQG4b%2Bg3Wazgg3qXhwfQ%2FMJXdlr0GOqUBvskveI67UYMnxc4BHz1OmvKpffyeIucKeClsxlcXxnTfJJuT4P7%2B63Gdoft5icgp%2FYb3mpMeHkYjl8vymxGP%2FlsaA1AOd0JLiy6ZCkpG2OUk%2FS2Fn9PM1u4xneSX7o5u2Ff0ZWcRJFJ5u0X%2F%2BMdAogVnfWP1Dqirujtnl3RyPGfqhs8GHCRirPLsyg91Ec6vhZfwbRzWR3DWDq6Lixw2BYJK8xBO&X-Amz-Signature=8b93acd89a8934ed949f723e73ad2b0f7b20e4579dae34c67530b1854eef8c07&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VOX45FDX%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071346Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJHMEUCIF46xbkjs6FyEi6Pd3wWXM4dPul8mABOXqMLL%2FZCEzcHAiEA3KSvB9B2xG53xozfTRsDZ6yOxK47e2GcHpC3CcOWsxUq%2FwMIcBAAGgw2Mzc0MjMxODM4MDUiDBH3A1jjg15JlylodircA%2FJNH5HSMmz1xqqOeWqHQ%2FgW5OfX%2F5serWoMzqBD2atG27pY9G3UEIfbN3MsEWtuHFq0giXIci0kxCy8q9y9AYYZj%2Bm8h9CTjHaTDsIPnJUdhN8R%2FR8FySE5VxQ%2BksgQ87rZ0iLEUO7G7RG63BG1%2FHZPx2Pmhve00uWXZ8zk24TI6ueGF%2FOzbXDqDKQwR%2BfzJNLPIvlXXzfcy4XHK8hs5xwxofmeF9112uhvTwZl4lXweKBdXHDOKCElSiQAAzxhQeL0hH5alm0WGEbV4ZLiXrWFdptIsvt2zNOFRTqHchdafua25Op5szTPml12eQJEyu7a0Q68MKo3RKRisTTYXwIaiwaJlb08q%2B8UP3Is06w9AR1MR%2BUfMkSSyk2eCuDxgIcbJSZQtVgMRpxVbKJjfY3UGmFa9VvcvylTy6RV7rRJX8OS%2BOGlUpJ%2B2PpyujpwNTSnWHdnpz4SMXjTHxzu9dL7j0lgNwRvKS033nt8l9SSnnkvpZiYwtpZHW7WTlkR2tI0UuVaWFAi5BdxrLerba3GfXMO8%2FUg3mdgQN0KI5UUXKiBDst%2BNVbqCrAvF1DZKV51E3oAPn1iuEHEbhCu6iPqLhqTKrUJm1uzsd2PX%2ByE%2BSF9zpbI%2BfWz6kXGMPfdlr0GOqUB8Ey6eRNZQnBRnRdfE9%2FvImaAxt0x9YnZvqt4AroX6oHrJy4VDIfIz5meJ6e4yNtmC%2FNEEQ%2FDjNdouDysV8t474ddKLJQKF6q0r2gmEUWTM1k158xIB%2BsUZcX%2B4nHRaJXm8JBZ5xf3eyZ1moUyYJAH1PPSYas8ByW%2F7BpBgvAnbI0cWaWuu2wcZJ4drnEwUoDGydB8PaZXEV59eIXAvwD4h%2FTTL%2BY&X-Amz-Signature=b76dfe6508c665d98af4bf55fde2e4f351e3904a6dcea5a391f32f1427ae53bf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHKQC24I%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071346Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJIMEYCIQDW7g0frnS57Tpf5y69UqAfOMSQKRhq74u3w3xuBPuYGwIhAMt0L14QOWUpzqRWcuO%2FUIxYaHUw6fBZYlYQLBgwJJQuKv8DCHAQABoMNjM3NDIzMTgzODA1IgyECEjymb%2BwxMopHdMq3AOY0GafRQoD0ERVaRN2TZUlP0IqYK%2FRtAS7u7xy8Z%2BwX22Pz4aBRxRFvK0II9GZO7hOoCtOzO5JEeDcwVhJbl9t%2Fa3YJp4VwdzupzjSxsGmLUYxoZe0SGkC85VZLdZl4H2YWkWKA29nk4ho8BNgxf0d982FA2qlB6ffs1yKPDn%2FBShHQ4GdAh6ny1%2BGOAs9yC5kV5MokIwZHguk%2FV9GwE1SE%2FKtpbu%2BDwbSxsaaFsOXTw4jOQYjXrFS1LnB38%2FGEdrBJ8AgsZcKGsYTG%2BjWLnYL5yDthKFYk33xc3ld7JFf8J2y6RKtQD9wUGEkrKLqzWX5uDZujsoqJzVY98%2BRcQmmE%2FjueRRHcxcsOoTAzDDzIS%2B4xW8r5jjvcHzkFE9tARjzzaE6GFFmILLLswHFsd6dTMiIPYDLgpf311NUa%2BP732cdk%2BrMj%2Fxo3Hf2wZnreU8jBTLvjfo8GR3xpYlzfTkBrLapGWco%2BBV3B4HmhQTpXe5U7xCV8bW8fDHFJ8Eq2nOiuIWQkx70NNbujLmU7OgIt4c0%2FJZ00tuCATbrQWp7CgnS5Sldc2Sdt7fqfobzfACCa079UfWXwh3NWFXpOSbC6%2BoWIM%2FRrCmHoG2eooPX9GJjgEZP9gYzwgHItzDV3Ja9BjqkAVJyOGX55lefGgqX7evaSXJgfLnk6ImjwNVYSuZAdcnd9RSo6Pn5TBwrMsaKM17wPQOuztB7nuQ5G1vxzuXD%2FL1Jkq8rwRm34A%2BcZl2DlhWhuVJVXiuG7jxft8yE4iWnXOUGBVZQWEdRPOEBQiN8hh%2BSn7C550LOuO4%2FbAtDs%2BEloVGELHGqh8mHDKGd2v2O67htaRlzisxOaP3BygNZ4vcXdpHg&X-Amz-Signature=61048f769b2ed4a07324f595c37d1298282a85afe28b9cce8979185118bde5ba&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHKQC24I%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071346Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJIMEYCIQDW7g0frnS57Tpf5y69UqAfOMSQKRhq74u3w3xuBPuYGwIhAMt0L14QOWUpzqRWcuO%2FUIxYaHUw6fBZYlYQLBgwJJQuKv8DCHAQABoMNjM3NDIzMTgzODA1IgyECEjymb%2BwxMopHdMq3AOY0GafRQoD0ERVaRN2TZUlP0IqYK%2FRtAS7u7xy8Z%2BwX22Pz4aBRxRFvK0II9GZO7hOoCtOzO5JEeDcwVhJbl9t%2Fa3YJp4VwdzupzjSxsGmLUYxoZe0SGkC85VZLdZl4H2YWkWKA29nk4ho8BNgxf0d982FA2qlB6ffs1yKPDn%2FBShHQ4GdAh6ny1%2BGOAs9yC5kV5MokIwZHguk%2FV9GwE1SE%2FKtpbu%2BDwbSxsaaFsOXTw4jOQYjXrFS1LnB38%2FGEdrBJ8AgsZcKGsYTG%2BjWLnYL5yDthKFYk33xc3ld7JFf8J2y6RKtQD9wUGEkrKLqzWX5uDZujsoqJzVY98%2BRcQmmE%2FjueRRHcxcsOoTAzDDzIS%2B4xW8r5jjvcHzkFE9tARjzzaE6GFFmILLLswHFsd6dTMiIPYDLgpf311NUa%2BP732cdk%2BrMj%2Fxo3Hf2wZnreU8jBTLvjfo8GR3xpYlzfTkBrLapGWco%2BBV3B4HmhQTpXe5U7xCV8bW8fDHFJ8Eq2nOiuIWQkx70NNbujLmU7OgIt4c0%2FJZ00tuCATbrQWp7CgnS5Sldc2Sdt7fqfobzfACCa079UfWXwh3NWFXpOSbC6%2BoWIM%2FRrCmHoG2eooPX9GJjgEZP9gYzwgHItzDV3Ja9BjqkAVJyOGX55lefGgqX7evaSXJgfLnk6ImjwNVYSuZAdcnd9RSo6Pn5TBwrMsaKM17wPQOuztB7nuQ5G1vxzuXD%2FL1Jkq8rwRm34A%2BcZl2DlhWhuVJVXiuG7jxft8yE4iWnXOUGBVZQWEdRPOEBQiN8hh%2BSn7C550LOuO4%2FbAtDs%2BEloVGELHGqh8mHDKGd2v2O67htaRlzisxOaP3BygNZ4vcXdpHg&X-Amz-Signature=16900fadbc2b580e2195bffaaa64fb64a800cba8f25bc7175c548889172b54d3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHKQC24I%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071346Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJIMEYCIQDW7g0frnS57Tpf5y69UqAfOMSQKRhq74u3w3xuBPuYGwIhAMt0L14QOWUpzqRWcuO%2FUIxYaHUw6fBZYlYQLBgwJJQuKv8DCHAQABoMNjM3NDIzMTgzODA1IgyECEjymb%2BwxMopHdMq3AOY0GafRQoD0ERVaRN2TZUlP0IqYK%2FRtAS7u7xy8Z%2BwX22Pz4aBRxRFvK0II9GZO7hOoCtOzO5JEeDcwVhJbl9t%2Fa3YJp4VwdzupzjSxsGmLUYxoZe0SGkC85VZLdZl4H2YWkWKA29nk4ho8BNgxf0d982FA2qlB6ffs1yKPDn%2FBShHQ4GdAh6ny1%2BGOAs9yC5kV5MokIwZHguk%2FV9GwE1SE%2FKtpbu%2BDwbSxsaaFsOXTw4jOQYjXrFS1LnB38%2FGEdrBJ8AgsZcKGsYTG%2BjWLnYL5yDthKFYk33xc3ld7JFf8J2y6RKtQD9wUGEkrKLqzWX5uDZujsoqJzVY98%2BRcQmmE%2FjueRRHcxcsOoTAzDDzIS%2B4xW8r5jjvcHzkFE9tARjzzaE6GFFmILLLswHFsd6dTMiIPYDLgpf311NUa%2BP732cdk%2BrMj%2Fxo3Hf2wZnreU8jBTLvjfo8GR3xpYlzfTkBrLapGWco%2BBV3B4HmhQTpXe5U7xCV8bW8fDHFJ8Eq2nOiuIWQkx70NNbujLmU7OgIt4c0%2FJZ00tuCATbrQWp7CgnS5Sldc2Sdt7fqfobzfACCa079UfWXwh3NWFXpOSbC6%2BoWIM%2FRrCmHoG2eooPX9GJjgEZP9gYzwgHItzDV3Ja9BjqkAVJyOGX55lefGgqX7evaSXJgfLnk6ImjwNVYSuZAdcnd9RSo6Pn5TBwrMsaKM17wPQOuztB7nuQ5G1vxzuXD%2FL1Jkq8rwRm34A%2BcZl2DlhWhuVJVXiuG7jxft8yE4iWnXOUGBVZQWEdRPOEBQiN8hh%2BSn7C550LOuO4%2FbAtDs%2BEloVGELHGqh8mHDKGd2v2O67htaRlzisxOaP3BygNZ4vcXdpHg&X-Amz-Signature=9c6941561d5c1a5a7fa2fbeaecd3d21f46d07228cf6b8c262c0445a57077a938&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHKQC24I%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071346Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJIMEYCIQDW7g0frnS57Tpf5y69UqAfOMSQKRhq74u3w3xuBPuYGwIhAMt0L14QOWUpzqRWcuO%2FUIxYaHUw6fBZYlYQLBgwJJQuKv8DCHAQABoMNjM3NDIzMTgzODA1IgyECEjymb%2BwxMopHdMq3AOY0GafRQoD0ERVaRN2TZUlP0IqYK%2FRtAS7u7xy8Z%2BwX22Pz4aBRxRFvK0II9GZO7hOoCtOzO5JEeDcwVhJbl9t%2Fa3YJp4VwdzupzjSxsGmLUYxoZe0SGkC85VZLdZl4H2YWkWKA29nk4ho8BNgxf0d982FA2qlB6ffs1yKPDn%2FBShHQ4GdAh6ny1%2BGOAs9yC5kV5MokIwZHguk%2FV9GwE1SE%2FKtpbu%2BDwbSxsaaFsOXTw4jOQYjXrFS1LnB38%2FGEdrBJ8AgsZcKGsYTG%2BjWLnYL5yDthKFYk33xc3ld7JFf8J2y6RKtQD9wUGEkrKLqzWX5uDZujsoqJzVY98%2BRcQmmE%2FjueRRHcxcsOoTAzDDzIS%2B4xW8r5jjvcHzkFE9tARjzzaE6GFFmILLLswHFsd6dTMiIPYDLgpf311NUa%2BP732cdk%2BrMj%2Fxo3Hf2wZnreU8jBTLvjfo8GR3xpYlzfTkBrLapGWco%2BBV3B4HmhQTpXe5U7xCV8bW8fDHFJ8Eq2nOiuIWQkx70NNbujLmU7OgIt4c0%2FJZ00tuCATbrQWp7CgnS5Sldc2Sdt7fqfobzfACCa079UfWXwh3NWFXpOSbC6%2BoWIM%2FRrCmHoG2eooPX9GJjgEZP9gYzwgHItzDV3Ja9BjqkAVJyOGX55lefGgqX7evaSXJgfLnk6ImjwNVYSuZAdcnd9RSo6Pn5TBwrMsaKM17wPQOuztB7nuQ5G1vxzuXD%2FL1Jkq8rwRm34A%2BcZl2DlhWhuVJVXiuG7jxft8yE4iWnXOUGBVZQWEdRPOEBQiN8hh%2BSn7C550LOuO4%2FbAtDs%2BEloVGELHGqh8mHDKGd2v2O67htaRlzisxOaP3BygNZ4vcXdpHg&X-Amz-Signature=948fc749fc4d81cebaf748f9fe3048e182489f94bc3e5ad71d09db283a84d1d1&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
