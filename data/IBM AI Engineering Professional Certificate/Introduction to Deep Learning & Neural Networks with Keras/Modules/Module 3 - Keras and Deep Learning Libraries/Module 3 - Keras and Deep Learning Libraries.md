

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46664QLWCMZ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIBY6T%2BHQg6ntGumtgLU6qVfYN5BxLreyQq0DImH1SCO7AiEArJoxX6fT7Y7hUZZ4cR5D9KdvOw3oHRPkgH%2FUjCCpR5wq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDGs3TizIUAquCE9uIircA3NdHKLxwSytY1lQxzXCQtAYHYidfdIcuFALGyfTOcjNwl0swKIJDy%2BzH4ZoBGEFgkZFxAnMpRrM71yAiIz46SzHuz8ltkOdEtWWhoNpkPTwSEeIZ8EPHDh8qfNUu8OZIlilE5YkW7WNa284Hk4PT4YN1qeJG5zanffNOqm5EU%2BE%2B%2FwmAmtVAedFRUbnySClcICnGfDR7e8H%2BipCHFnpklpArUKiRLMzPUA%2Fk3sbri%2F6x%2BDSObk5PkwDDVvm6O9gO%2Bdfb4F2k1nWC5Ym7jZUsaluN8F%2FQ3Z7efqBAbBsk0Aquy0qHqOBnWwHMrr8wja2VoLKB5RA9pXP9GmAYuZ70r5pWKmNF%2FGVtQbgyNBGk0DMqIb48jFe7v71JDQvpGKQAWxCJkMar7UbRe5DP0M4SS%2BKFHdqsrDijZJ2AGKCUedbZ%2BGKHmHg9hxySl9LL%2FC26EDUGTWTXVtTMmATmhMCyBsdjITZmUGbK%2BD2k%2FszUBWnBamqsVUXDfN2b3eWbZcLog8SnDAcL5tcP5hPh%2FQx2MM3412303I%2FMc1nXoQX2pccqS36%2F%2BanWTYrnJCZWW4ym%2FEHZxjaB2VeXBlqhhVKGsUoQ2aYipX4FMI14E0cchkDtWDN9d%2BkPCnHYcayMKqLmL0GOqUBuKm8e%2FN3m8aP86%2FuTvNofLWolGcEyjkHHKHP3wt7FUBfW9X30LpoynMrY7NzQCAsiiZIVzZ0k%2BoL0qk13%2Frlca6e2q6ZZhK7cOKarO%2FoJ5UtnUeTltymdXFQYgWBd0pEFwOMIlqJmkxZX86igARNTK1v%2FA4K8f2ohXfAIWgEknQ1w5IKuZ%2BA8Wool6svKH81saszb3%2FX1GcCw9tealu%2BSq9yR9Fs&X-Amz-Signature=f399c7004e12da96f132ca41719e713d565175e5a6098d1d2507011e74ad4810&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46664QLWCMZ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIBY6T%2BHQg6ntGumtgLU6qVfYN5BxLreyQq0DImH1SCO7AiEArJoxX6fT7Y7hUZZ4cR5D9KdvOw3oHRPkgH%2FUjCCpR5wq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDGs3TizIUAquCE9uIircA3NdHKLxwSytY1lQxzXCQtAYHYidfdIcuFALGyfTOcjNwl0swKIJDy%2BzH4ZoBGEFgkZFxAnMpRrM71yAiIz46SzHuz8ltkOdEtWWhoNpkPTwSEeIZ8EPHDh8qfNUu8OZIlilE5YkW7WNa284Hk4PT4YN1qeJG5zanffNOqm5EU%2BE%2B%2FwmAmtVAedFRUbnySClcICnGfDR7e8H%2BipCHFnpklpArUKiRLMzPUA%2Fk3sbri%2F6x%2BDSObk5PkwDDVvm6O9gO%2Bdfb4F2k1nWC5Ym7jZUsaluN8F%2FQ3Z7efqBAbBsk0Aquy0qHqOBnWwHMrr8wja2VoLKB5RA9pXP9GmAYuZ70r5pWKmNF%2FGVtQbgyNBGk0DMqIb48jFe7v71JDQvpGKQAWxCJkMar7UbRe5DP0M4SS%2BKFHdqsrDijZJ2AGKCUedbZ%2BGKHmHg9hxySl9LL%2FC26EDUGTWTXVtTMmATmhMCyBsdjITZmUGbK%2BD2k%2FszUBWnBamqsVUXDfN2b3eWbZcLog8SnDAcL5tcP5hPh%2FQx2MM3412303I%2FMc1nXoQX2pccqS36%2F%2BanWTYrnJCZWW4ym%2FEHZxjaB2VeXBlqhhVKGsUoQ2aYipX4FMI14E0cchkDtWDN9d%2BkPCnHYcayMKqLmL0GOqUBuKm8e%2FN3m8aP86%2FuTvNofLWolGcEyjkHHKHP3wt7FUBfW9X30LpoynMrY7NzQCAsiiZIVzZ0k%2BoL0qk13%2Frlca6e2q6ZZhK7cOKarO%2FoJ5UtnUeTltymdXFQYgWBd0pEFwOMIlqJmkxZX86igARNTK1v%2FA4K8f2ohXfAIWgEknQ1w5IKuZ%2BA8Wool6svKH81saszb3%2FX1GcCw9tealu%2BSq9yR9Fs&X-Amz-Signature=ea02b2779019d9a1f1332d6b7ec78df5956c7654c00388d9d2b94ea1d12399d8&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46664QLWCMZ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIBY6T%2BHQg6ntGumtgLU6qVfYN5BxLreyQq0DImH1SCO7AiEArJoxX6fT7Y7hUZZ4cR5D9KdvOw3oHRPkgH%2FUjCCpR5wq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDGs3TizIUAquCE9uIircA3NdHKLxwSytY1lQxzXCQtAYHYidfdIcuFALGyfTOcjNwl0swKIJDy%2BzH4ZoBGEFgkZFxAnMpRrM71yAiIz46SzHuz8ltkOdEtWWhoNpkPTwSEeIZ8EPHDh8qfNUu8OZIlilE5YkW7WNa284Hk4PT4YN1qeJG5zanffNOqm5EU%2BE%2B%2FwmAmtVAedFRUbnySClcICnGfDR7e8H%2BipCHFnpklpArUKiRLMzPUA%2Fk3sbri%2F6x%2BDSObk5PkwDDVvm6O9gO%2Bdfb4F2k1nWC5Ym7jZUsaluN8F%2FQ3Z7efqBAbBsk0Aquy0qHqOBnWwHMrr8wja2VoLKB5RA9pXP9GmAYuZ70r5pWKmNF%2FGVtQbgyNBGk0DMqIb48jFe7v71JDQvpGKQAWxCJkMar7UbRe5DP0M4SS%2BKFHdqsrDijZJ2AGKCUedbZ%2BGKHmHg9hxySl9LL%2FC26EDUGTWTXVtTMmATmhMCyBsdjITZmUGbK%2BD2k%2FszUBWnBamqsVUXDfN2b3eWbZcLog8SnDAcL5tcP5hPh%2FQx2MM3412303I%2FMc1nXoQX2pccqS36%2F%2BanWTYrnJCZWW4ym%2FEHZxjaB2VeXBlqhhVKGsUoQ2aYipX4FMI14E0cchkDtWDN9d%2BkPCnHYcayMKqLmL0GOqUBuKm8e%2FN3m8aP86%2FuTvNofLWolGcEyjkHHKHP3wt7FUBfW9X30LpoynMrY7NzQCAsiiZIVzZ0k%2BoL0qk13%2Frlca6e2q6ZZhK7cOKarO%2FoJ5UtnUeTltymdXFQYgWBd0pEFwOMIlqJmkxZX86igARNTK1v%2FA4K8f2ohXfAIWgEknQ1w5IKuZ%2BA8Wool6svKH81saszb3%2FX1GcCw9tealu%2BSq9yR9Fs&X-Amz-Signature=e243de4d96c2cd52bca6e64e81cccc2d3c0fa1e46638c51479312102e3eb104a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YO5MUZO4%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJIMEYCIQDUM1pWkMfx8vZdXvdjlMxQy%2BoT7hfau1E2UG4HcWobHwIhAOc5Qim%2B%2B8QIPadj%2BXg5oq7mjVeTOBR%2FrZdEdA7gZ6oNKv8DCHYQABoMNjM3NDIzMTgzODA1IgwHKjUVQdzjPvXOVIAq3AOphuoVYXagCncYUpp3tM3Su4jDyBrlf5L7sy6R7C%2FstFJHm764JLvyFG17e1Rk%2B%2FnpTgqfo6uO1Z82lbq7HKs8BSYhcjyh569nn4go%2BVOGE%2Bd5lyt0iYMtf8FUiFEDunS%2F66sbIpIUIWGJ8zgoKPH%2FLnhtUNiXKeELSD8h8%2B4ZB%2BUJQPmyO8yh3O1rV%2Fmf8HIV0TJ%2B46%2Bu%2FN9zPKH0WP1Bv6Dmb%2BKOaakjgHZCamJaLA6eZMTOgCx1t2KHlvR%2Fdi8clvu0xXtCpsEfu0IA0dLfZD5Wh3v%2BOriWutw8BCXZZNE%2FWHvWKgr95WvYwTBZdDsi88IxKNgriGSgS39vYPOqb9%2F2CopgkgSadiW7Ugt%2Bs5MUHcXWFMcEINyarJVSEe19NujHGsqbOJhNdyvOm8O4TWdx57Ed%2Bl%2F5o6fgui%2BzKl12ZPYEdcttRpqBtjmNmVLUv4Z82s8Msi1QSsOFlw%2BeS5FV6Wm749gOurw9P4yI8w%2Fp4nURQII19jT6R5P47qEYMuJtQ37I37i2QV%2Bsk3wxKaHyUxXzmbTMA6%2BtbR4q1jiOOyGuK6so39cXHoGFAJTgh3qK9bgGmsyTls0oOfrNC2FSumAjmajo5BHfzHwKgA7zvHT6RgCZFvd9OzCei5i9BjqkAfBxCAZppCYIn4j03a7Ag8q8Q74aW7zsbDrVj6fkgUDWBb56zZscyJAKyj0AHytXNZtf1H8MCPYV7w31GFwyc3io%2BFhE8xWqstlC5Z2cB%2FxDWFxmf9S4BjYx7W9yk5sysvF6LiOs%2BXZyQPu86%2FhwPcDQ6VS3%2BbeZSpapee3HIG9zt0KzAeO9odVbRelT0eGUss0i5YFgOS%2BOxULgP2viSsoCTSnO&X-Amz-Signature=5494c90a20c8cceb63155cdc7483c3f2825156049e6648dbdcc9def403bf50a4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W3KOAFXF%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJIMEYCIQDdfc0OGrDHhgT6mbHFDgY%2Bw%2FRWP6dTgYjmlksHlSo6vgIhAOzuYYkc3%2F04cdu24c6lgswa5CE%2FSkB6vch5KGI8uVQeKv8DCHYQABoMNjM3NDIzMTgzODA1IgyHDorgJO%2Fg4q88pXgq3AMiCCTJZK19%2FlWaPZlWvNQFU%2BUpEwKFk1zwtKLrF1nLS2FoqdIjKRWdYoFjY4R00KZI3zH4jgRLw8LECsOhP1LaoSBkR%2BK2A%2FvX9kUCRVJpRtIjKEOA5r%2FV6bukWODQchudA8ND0md%2F8ROpfSAKkPmrk5OSq8mavrC%2FFSYujasxgvyaqnwcLL15HIkYYMKBNMuIt0QirPEbbqXz8ZafXQlPmwLqdsQrkqZbTM1vg%2FV7A2Bbtzu1OZBXXXa0ELT4eH9mUM5qwewpHcD6V4B27dzoOjwN6EFSO7HeQl%2B2QF4Sl26AQZ12inaACxv56YQQ7yOMlvO10qf1X1oPzOcYGSv0xD8TdxprnmjTfKwRZsw68YjBb5L0aaZASkxS4xDOsJwThk9JHqQ019rNjjjpm2WZQE5VKanJ0jHI319NyPUwPPUBVAocoNB%2BnmudII8jnMeJ3oTgsFzKBUda9IE8qDoaOvvF33OTXRSSTmBzQfvfSs%2Fl0Uss7%2Fhy1tHK7udDD1DN%2F9lxJhHlTYI5h8w9GMcWucby%2FAWF6rHn1kuP4R8fPHG0VxhXUFCWv2mlj0of9IXEQ%2BQfgK16K0PnVqr9kQR18RWihm23I6r%2B5dmNfFBbs3MfILdkfl4iDGPV%2FjCMi5i9BjqkAUZCAUAUVEeP6nzGA7JCgFgZPIVcykmMMBMUKuqJ%2Bv09kOfNVpIew9aOX9VHLnjm94REqxa%2FKcqmbxwcbEBoavK%2FtwxQKOCXWYWlXpRoxUNj9lhAp7H%2BvXjtFOFygefPNusH6UMsbvYbUxjaIkVzH%2FwldLmI1YSwD7QqCFDnpwJtsY6A7MiSkAM%2BDBvJUA15fFdmdosF1m5BWlgbaK6BvjPe7Ewh&X-Amz-Signature=b33d2c823d0ebf6d7b17d85904c6bee2369eb760ae8df31f192827e495bdfb66&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46664QLWCMZ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIBY6T%2BHQg6ntGumtgLU6qVfYN5BxLreyQq0DImH1SCO7AiEArJoxX6fT7Y7hUZZ4cR5D9KdvOw3oHRPkgH%2FUjCCpR5wq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDGs3TizIUAquCE9uIircA3NdHKLxwSytY1lQxzXCQtAYHYidfdIcuFALGyfTOcjNwl0swKIJDy%2BzH4ZoBGEFgkZFxAnMpRrM71yAiIz46SzHuz8ltkOdEtWWhoNpkPTwSEeIZ8EPHDh8qfNUu8OZIlilE5YkW7WNa284Hk4PT4YN1qeJG5zanffNOqm5EU%2BE%2B%2FwmAmtVAedFRUbnySClcICnGfDR7e8H%2BipCHFnpklpArUKiRLMzPUA%2Fk3sbri%2F6x%2BDSObk5PkwDDVvm6O9gO%2Bdfb4F2k1nWC5Ym7jZUsaluN8F%2FQ3Z7efqBAbBsk0Aquy0qHqOBnWwHMrr8wja2VoLKB5RA9pXP9GmAYuZ70r5pWKmNF%2FGVtQbgyNBGk0DMqIb48jFe7v71JDQvpGKQAWxCJkMar7UbRe5DP0M4SS%2BKFHdqsrDijZJ2AGKCUedbZ%2BGKHmHg9hxySl9LL%2FC26EDUGTWTXVtTMmATmhMCyBsdjITZmUGbK%2BD2k%2FszUBWnBamqsVUXDfN2b3eWbZcLog8SnDAcL5tcP5hPh%2FQx2MM3412303I%2FMc1nXoQX2pccqS36%2F%2BanWTYrnJCZWW4ym%2FEHZxjaB2VeXBlqhhVKGsUoQ2aYipX4FMI14E0cchkDtWDN9d%2BkPCnHYcayMKqLmL0GOqUBuKm8e%2FN3m8aP86%2FuTvNofLWolGcEyjkHHKHP3wt7FUBfW9X30LpoynMrY7NzQCAsiiZIVzZ0k%2BoL0qk13%2Frlca6e2q6ZZhK7cOKarO%2FoJ5UtnUeTltymdXFQYgWBd0pEFwOMIlqJmkxZX86igARNTK1v%2FA4K8f2ohXfAIWgEknQ1w5IKuZ%2BA8Wool6svKH81saszb3%2FX1GcCw9tealu%2BSq9yR9Fs&X-Amz-Signature=803d9c81b0473bef9baab04fc33a4bbe2a2c012c2b0ec4140a26a5221ba3239e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46664QLWCMZ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIBY6T%2BHQg6ntGumtgLU6qVfYN5BxLreyQq0DImH1SCO7AiEArJoxX6fT7Y7hUZZ4cR5D9KdvOw3oHRPkgH%2FUjCCpR5wq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDGs3TizIUAquCE9uIircA3NdHKLxwSytY1lQxzXCQtAYHYidfdIcuFALGyfTOcjNwl0swKIJDy%2BzH4ZoBGEFgkZFxAnMpRrM71yAiIz46SzHuz8ltkOdEtWWhoNpkPTwSEeIZ8EPHDh8qfNUu8OZIlilE5YkW7WNa284Hk4PT4YN1qeJG5zanffNOqm5EU%2BE%2B%2FwmAmtVAedFRUbnySClcICnGfDR7e8H%2BipCHFnpklpArUKiRLMzPUA%2Fk3sbri%2F6x%2BDSObk5PkwDDVvm6O9gO%2Bdfb4F2k1nWC5Ym7jZUsaluN8F%2FQ3Z7efqBAbBsk0Aquy0qHqOBnWwHMrr8wja2VoLKB5RA9pXP9GmAYuZ70r5pWKmNF%2FGVtQbgyNBGk0DMqIb48jFe7v71JDQvpGKQAWxCJkMar7UbRe5DP0M4SS%2BKFHdqsrDijZJ2AGKCUedbZ%2BGKHmHg9hxySl9LL%2FC26EDUGTWTXVtTMmATmhMCyBsdjITZmUGbK%2BD2k%2FszUBWnBamqsVUXDfN2b3eWbZcLog8SnDAcL5tcP5hPh%2FQx2MM3412303I%2FMc1nXoQX2pccqS36%2F%2BanWTYrnJCZWW4ym%2FEHZxjaB2VeXBlqhhVKGsUoQ2aYipX4FMI14E0cchkDtWDN9d%2BkPCnHYcayMKqLmL0GOqUBuKm8e%2FN3m8aP86%2FuTvNofLWolGcEyjkHHKHP3wt7FUBfW9X30LpoynMrY7NzQCAsiiZIVzZ0k%2BoL0qk13%2Frlca6e2q6ZZhK7cOKarO%2FoJ5UtnUeTltymdXFQYgWBd0pEFwOMIlqJmkxZX86igARNTK1v%2FA4K8f2ohXfAIWgEknQ1w5IKuZ%2BA8Wool6svKH81saszb3%2FX1GcCw9tealu%2BSq9yR9Fs&X-Amz-Signature=0cb21010d9f9ba8b96bd77444ec1f3682ff9d5df2a3fd3cab9280bdaf5b17508&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46664QLWCMZ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIBY6T%2BHQg6ntGumtgLU6qVfYN5BxLreyQq0DImH1SCO7AiEArJoxX6fT7Y7hUZZ4cR5D9KdvOw3oHRPkgH%2FUjCCpR5wq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDGs3TizIUAquCE9uIircA3NdHKLxwSytY1lQxzXCQtAYHYidfdIcuFALGyfTOcjNwl0swKIJDy%2BzH4ZoBGEFgkZFxAnMpRrM71yAiIz46SzHuz8ltkOdEtWWhoNpkPTwSEeIZ8EPHDh8qfNUu8OZIlilE5YkW7WNa284Hk4PT4YN1qeJG5zanffNOqm5EU%2BE%2B%2FwmAmtVAedFRUbnySClcICnGfDR7e8H%2BipCHFnpklpArUKiRLMzPUA%2Fk3sbri%2F6x%2BDSObk5PkwDDVvm6O9gO%2Bdfb4F2k1nWC5Ym7jZUsaluN8F%2FQ3Z7efqBAbBsk0Aquy0qHqOBnWwHMrr8wja2VoLKB5RA9pXP9GmAYuZ70r5pWKmNF%2FGVtQbgyNBGk0DMqIb48jFe7v71JDQvpGKQAWxCJkMar7UbRe5DP0M4SS%2BKFHdqsrDijZJ2AGKCUedbZ%2BGKHmHg9hxySl9LL%2FC26EDUGTWTXVtTMmATmhMCyBsdjITZmUGbK%2BD2k%2FszUBWnBamqsVUXDfN2b3eWbZcLog8SnDAcL5tcP5hPh%2FQx2MM3412303I%2FMc1nXoQX2pccqS36%2F%2BanWTYrnJCZWW4ym%2FEHZxjaB2VeXBlqhhVKGsUoQ2aYipX4FMI14E0cchkDtWDN9d%2BkPCnHYcayMKqLmL0GOqUBuKm8e%2FN3m8aP86%2FuTvNofLWolGcEyjkHHKHP3wt7FUBfW9X30LpoynMrY7NzQCAsiiZIVzZ0k%2BoL0qk13%2Frlca6e2q6ZZhK7cOKarO%2FoJ5UtnUeTltymdXFQYgWBd0pEFwOMIlqJmkxZX86igARNTK1v%2FA4K8f2ohXfAIWgEknQ1w5IKuZ%2BA8Wool6svKH81saszb3%2FX1GcCw9tealu%2BSq9yR9Fs&X-Amz-Signature=106feb019b6c9cf2e2d018ab226b7ffda340e4ca5b6467f20f1383e3a684a614&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46664QLWCMZ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIBY6T%2BHQg6ntGumtgLU6qVfYN5BxLreyQq0DImH1SCO7AiEArJoxX6fT7Y7hUZZ4cR5D9KdvOw3oHRPkgH%2FUjCCpR5wq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDGs3TizIUAquCE9uIircA3NdHKLxwSytY1lQxzXCQtAYHYidfdIcuFALGyfTOcjNwl0swKIJDy%2BzH4ZoBGEFgkZFxAnMpRrM71yAiIz46SzHuz8ltkOdEtWWhoNpkPTwSEeIZ8EPHDh8qfNUu8OZIlilE5YkW7WNa284Hk4PT4YN1qeJG5zanffNOqm5EU%2BE%2B%2FwmAmtVAedFRUbnySClcICnGfDR7e8H%2BipCHFnpklpArUKiRLMzPUA%2Fk3sbri%2F6x%2BDSObk5PkwDDVvm6O9gO%2Bdfb4F2k1nWC5Ym7jZUsaluN8F%2FQ3Z7efqBAbBsk0Aquy0qHqOBnWwHMrr8wja2VoLKB5RA9pXP9GmAYuZ70r5pWKmNF%2FGVtQbgyNBGk0DMqIb48jFe7v71JDQvpGKQAWxCJkMar7UbRe5DP0M4SS%2BKFHdqsrDijZJ2AGKCUedbZ%2BGKHmHg9hxySl9LL%2FC26EDUGTWTXVtTMmATmhMCyBsdjITZmUGbK%2BD2k%2FszUBWnBamqsVUXDfN2b3eWbZcLog8SnDAcL5tcP5hPh%2FQx2MM3412303I%2FMc1nXoQX2pccqS36%2F%2BanWTYrnJCZWW4ym%2FEHZxjaB2VeXBlqhhVKGsUoQ2aYipX4FMI14E0cchkDtWDN9d%2BkPCnHYcayMKqLmL0GOqUBuKm8e%2FN3m8aP86%2FuTvNofLWolGcEyjkHHKHP3wt7FUBfW9X30LpoynMrY7NzQCAsiiZIVzZ0k%2BoL0qk13%2Frlca6e2q6ZZhK7cOKarO%2FoJ5UtnUeTltymdXFQYgWBd0pEFwOMIlqJmkxZX86igARNTK1v%2FA4K8f2ohXfAIWgEknQ1w5IKuZ%2BA8Wool6svKH81saszb3%2FX1GcCw9tealu%2BSq9yR9Fs&X-Amz-Signature=ce798485b19e30e39bfe7424070f99baec5705d037eec0b5fd9daa6411f7f1d4&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
