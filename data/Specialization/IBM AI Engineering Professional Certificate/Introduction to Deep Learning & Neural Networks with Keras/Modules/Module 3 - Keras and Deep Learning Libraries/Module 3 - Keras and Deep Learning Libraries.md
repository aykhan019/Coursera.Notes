

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646Q6XCVF%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIQCbIDcRmRuWjMYlfQwMxA1mE5qgWyZ%2BBvxeWc%2B4zEwcQgIgFHEW%2FOt%2B6944EJQtkf%2Bto8eaXUOpkh5A0qHfluOwmxAq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDOsm%2FaT3NKAxNYSl%2BCrcA3B0YFTXzj%2FcyCH0W1%2FQNK%2FC7nBlZDM4vZY%2BxuE9TGrvcBxBadnsr796p2ewpns5gIA3NWvVnEY9avtgsZHu59KxK%2BhTBeejurqL8i%2FpDEQpI%2Fj7jJsrbtTjGiYK4C7Xb3zgaXvgjPXodm%2BAuM9SVXOP3skplWrJczfquNXinpLyx0LNrMRXlOdsE3kDnxWs38y1UUeWlxxAyxx9kDmcdr0DA6USxnmTX2tYNzb09bXFDdQHamAt2vnQY4w4p%2FDkOxZwoX9V4Zkv1CKkmT1Yxk6s6zN1e%2FgxmqmkuXBmE57izeHk%2FGTvQBz0k8LiUwmZ%2FoIQVTXyYeJc3%2BB%2F1AzZ5EgxnDtsQwWpdUYq4qDkQ6xuo8pa67QL9Ds5FeCTATbTrbmShSUOwwGfWOLjoB033IImlUD%2B7Fio5%2Fvqdi8cDWrwwWdx%2BHzU3QpGYdPb1tWSgVVk5AWFdqxepzYgjODWtfNK5ReyPVNY3YJhFuZMlAbVkdwP2%2FAdRlDn2%2FF%2BUgcAo0JuRwxvXEMWs8T2E8bcWyzr%2FQhOtYzSAPvEpz3JAQIBTbCqGh9eq3pdSNjTyY1L8somZujUbm7prGbZl7XzS6mtkYRatc6SWGta70U0TXEUcY1TmoC9%2FGTYuZe2MPSU5bwGOqUBUNJEzuYi679TETP7XAckhdwXDJ0K5W1PXfuRm1o8hIUaDnpZLzJMmeNO7L5YuAdNk0reqwYzae5yYom%2Bfvp77MUgKdSNRDuxL6fixg3WY3NQtqIEWsypKLl9xNWX52qrDATbvS2tUunh8Un7i9PwqaxubNTcMlE5gpar%2Bg9c6VuZTpaCm%2B1p16XN9sWUjbmFApf3wmSM4jzqLk0wZA4481fzBGOb&X-Amz-Signature=3d5401d0f090ce1a52e6d0908388be681d47ea9dbecba18be93144a916615c89&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646Q6XCVF%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIQCbIDcRmRuWjMYlfQwMxA1mE5qgWyZ%2BBvxeWc%2B4zEwcQgIgFHEW%2FOt%2B6944EJQtkf%2Bto8eaXUOpkh5A0qHfluOwmxAq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDOsm%2FaT3NKAxNYSl%2BCrcA3B0YFTXzj%2FcyCH0W1%2FQNK%2FC7nBlZDM4vZY%2BxuE9TGrvcBxBadnsr796p2ewpns5gIA3NWvVnEY9avtgsZHu59KxK%2BhTBeejurqL8i%2FpDEQpI%2Fj7jJsrbtTjGiYK4C7Xb3zgaXvgjPXodm%2BAuM9SVXOP3skplWrJczfquNXinpLyx0LNrMRXlOdsE3kDnxWs38y1UUeWlxxAyxx9kDmcdr0DA6USxnmTX2tYNzb09bXFDdQHamAt2vnQY4w4p%2FDkOxZwoX9V4Zkv1CKkmT1Yxk6s6zN1e%2FgxmqmkuXBmE57izeHk%2FGTvQBz0k8LiUwmZ%2FoIQVTXyYeJc3%2BB%2F1AzZ5EgxnDtsQwWpdUYq4qDkQ6xuo8pa67QL9Ds5FeCTATbTrbmShSUOwwGfWOLjoB033IImlUD%2B7Fio5%2Fvqdi8cDWrwwWdx%2BHzU3QpGYdPb1tWSgVVk5AWFdqxepzYgjODWtfNK5ReyPVNY3YJhFuZMlAbVkdwP2%2FAdRlDn2%2FF%2BUgcAo0JuRwxvXEMWs8T2E8bcWyzr%2FQhOtYzSAPvEpz3JAQIBTbCqGh9eq3pdSNjTyY1L8somZujUbm7prGbZl7XzS6mtkYRatc6SWGta70U0TXEUcY1TmoC9%2FGTYuZe2MPSU5bwGOqUBUNJEzuYi679TETP7XAckhdwXDJ0K5W1PXfuRm1o8hIUaDnpZLzJMmeNO7L5YuAdNk0reqwYzae5yYom%2Bfvp77MUgKdSNRDuxL6fixg3WY3NQtqIEWsypKLl9xNWX52qrDATbvS2tUunh8Un7i9PwqaxubNTcMlE5gpar%2Bg9c6VuZTpaCm%2B1p16XN9sWUjbmFApf3wmSM4jzqLk0wZA4481fzBGOb&X-Amz-Signature=881e691524c6257b938c3331a253c33a795f6814b96af386eaaaa63293cdae8e&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646Q6XCVF%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIQCbIDcRmRuWjMYlfQwMxA1mE5qgWyZ%2BBvxeWc%2B4zEwcQgIgFHEW%2FOt%2B6944EJQtkf%2Bto8eaXUOpkh5A0qHfluOwmxAq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDOsm%2FaT3NKAxNYSl%2BCrcA3B0YFTXzj%2FcyCH0W1%2FQNK%2FC7nBlZDM4vZY%2BxuE9TGrvcBxBadnsr796p2ewpns5gIA3NWvVnEY9avtgsZHu59KxK%2BhTBeejurqL8i%2FpDEQpI%2Fj7jJsrbtTjGiYK4C7Xb3zgaXvgjPXodm%2BAuM9SVXOP3skplWrJczfquNXinpLyx0LNrMRXlOdsE3kDnxWs38y1UUeWlxxAyxx9kDmcdr0DA6USxnmTX2tYNzb09bXFDdQHamAt2vnQY4w4p%2FDkOxZwoX9V4Zkv1CKkmT1Yxk6s6zN1e%2FgxmqmkuXBmE57izeHk%2FGTvQBz0k8LiUwmZ%2FoIQVTXyYeJc3%2BB%2F1AzZ5EgxnDtsQwWpdUYq4qDkQ6xuo8pa67QL9Ds5FeCTATbTrbmShSUOwwGfWOLjoB033IImlUD%2B7Fio5%2Fvqdi8cDWrwwWdx%2BHzU3QpGYdPb1tWSgVVk5AWFdqxepzYgjODWtfNK5ReyPVNY3YJhFuZMlAbVkdwP2%2FAdRlDn2%2FF%2BUgcAo0JuRwxvXEMWs8T2E8bcWyzr%2FQhOtYzSAPvEpz3JAQIBTbCqGh9eq3pdSNjTyY1L8somZujUbm7prGbZl7XzS6mtkYRatc6SWGta70U0TXEUcY1TmoC9%2FGTYuZe2MPSU5bwGOqUBUNJEzuYi679TETP7XAckhdwXDJ0K5W1PXfuRm1o8hIUaDnpZLzJMmeNO7L5YuAdNk0reqwYzae5yYom%2Bfvp77MUgKdSNRDuxL6fixg3WY3NQtqIEWsypKLl9xNWX52qrDATbvS2tUunh8Un7i9PwqaxubNTcMlE5gpar%2Bg9c6VuZTpaCm%2B1p16XN9sWUjbmFApf3wmSM4jzqLk0wZA4481fzBGOb&X-Amz-Signature=cb75e4bee4299c380a61a9233760a1db665a062b7140551b9d0a355932f91613&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SIEMH3G3%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIQDDamvAraRGk67AI2veA%2Bfc7bJ8ohMdySRoagjrbludKAIgD2R%2BqsU6RyKEdMVPG8HeptuIs%2FupWpRPQ5F0JsgqNm4q%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDGMiVp9jatptHc6xFyrcAwLqVASziZjOQ1WMZfy1o75494pCpIrEOuTEj85kt9OlyNub5BimxE5JLMVgHp2kormIrj6fQIEa85EGEq4zqyRyMjxvXSn9%2FDizXnA17e3bSentqipxUOfxBnZmy8aW08HA1fpYz8PbdQzcFCk%2FtPbkFGVm2hkT%2F0t5ij58MXnjImz8IWx6lVL5j3OeHHYzAf48lf7aEvBos0L5GgX7nzWdJ0Ij0823Q4oi3mBYqoGNJRXNaZNQExBO9vJyUIwwQELFDsetMrVyVcVOVvaQLb%2FPdgSp3iJ7WcatmXwfxKoWBh%2B%2BxSd7RxRVYnRSv1hgIu%2FG04YSbumun7jGomJ0Ts%2FDa4AdMGCYZUxaGHCTV1sE9RVUlf1I7TStjZiOSmNM%2FlX1oIm6PoUX50vHCkCttDV6nU0%2FD5jWBPMZnAGUZVvZR0SC%2B8nnch%2F%2BVZtF0FR1J%2FRxwaNvODzScEjsDdM83g0pgyFaX%2FYoTxQkATb0YQ8wyup1manjlMG0RzPRu0JqE6%2BTGM%2B%2FO4TYlLyp09ipiTchFWjjJb5gYfWPUtxCEuvRZdZ3TG6u3MwyB3SMYnmREoZzWzBwCm74yZ67IbBKxw6UTcCGGeeqbMAdaLmh5Iqu2URkumk%2Bp3QemgwQMPmU5bwGOqUBboj0khfhQ80Q15T35XiSBM4PP99LTqplOszYfOK2gnm9XMYyiuaesixPrIymZvhBC2lW2RGa8SX12pegW%2F6T5lrxY4nKtYszIyipBkyLDYUkbWiB7P8HL2kTGMg2mOnhDmZ4V7T2JbtUBImf0xUyg6PBTTy%2FE2BqXb4W06QIdMB0PDywVGhvFjoWm6Vox9eFha%2Fd29Pqik%2FPCL188PnkurPugNZy&X-Amz-Signature=9a4cb17678c1a82bdefcaa9f1eaddbf41e1be313e9bfc7c50be8b2d85023288e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666PMARNRY%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIFHFgQv9RwTLvKHZP%2BdRGdn8XNihejveJnCCSwyJ0Nd5AiEAqH5xIA3dutKJR3zgafaaLymNS1hzatZ0j1zNaQ2%2Fvd0q%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDIIkY6VdEIYFvV7sDircA9ksHnvyi3X3cxhuOw%2FLw9J0NEu9RSFqk%2BKt7ET67JYdzo95u9%2FinKOyhop3HaNY64%2FEb8dAfcbgdTM9%2BurnYl%2B6bKf%2BbgMSrDLUFE2BvgBy6cYODut2JmajI3LpHQYM8btsigSVFiH34hxXK%2B6IUcpk2PyuxT%2BVFOStXoBuktD6ElxyicgnUKs5Ha%2FgdumQYX69NvWeY6m1LqtN618Y7V78r7WLM%2Ff19vbhhIo8F68Cu58wwo%2FxNsUDcEsShnu3pIb7l8jaLiUWh3Vrs5JFG8XEwAuvCpotc3coa%2BJdOT8uQZmCdJIgdfpVzxWhELbpAa9zt4L1SVm3WPwIFkkrdVneTuCC9rC6kFxxFNNKl%2Bl6001Vc7mRayiehnGD7Mgfabp%2BTN3kxrdQpfgEqggXfzNiq19pM6fcjvywCGyOuw0gqDWrMZz4cSyfwiMRZXiKwjwIQ1PbvFhWy5sWlyXeNh1R28HdJaD0v%2FZNPUzTDMhjQLhDk13pXoMHtjWXn%2BCkxs1vgMaoHGVbibZ2T22iAzay5g1InSAeAYFatsFlsax1KTAeS%2Fq2HYAuO2oNII8lZ9HetJxqaIHPFbGXsFmo%2Bn3riyikOEp9zmTWe5fYzZErd2qYoOiV1TKjlxmLMM6U5bwGOqUBmp7zBP7wBDCmuwwzfoT8NR3FdrL%2BosafMe0I98ihS%2B5DuBh8fQZAx9AO2C84zSq4SelMtz7gZz9wwXWQ4FxHSipSkVdUcu%2BxpuoyysSr1Rbq9NbEnwdq4O%2BFo8ESRYj5oVjx9LnBye8L6r0ln5CWE8ekkwM6Q3rDFfAUZJ2p1UMzEaUnoGQOJQwFjECnPWmt3UVtnsO8Cdweof5dqLuloGo6xXl6&X-Amz-Signature=903fa2ae9278d3b17f80a34584f28fb0fa67521caf9cf5f0b94db278e501c7bb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646Q6XCVF%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIQCbIDcRmRuWjMYlfQwMxA1mE5qgWyZ%2BBvxeWc%2B4zEwcQgIgFHEW%2FOt%2B6944EJQtkf%2Bto8eaXUOpkh5A0qHfluOwmxAq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDOsm%2FaT3NKAxNYSl%2BCrcA3B0YFTXzj%2FcyCH0W1%2FQNK%2FC7nBlZDM4vZY%2BxuE9TGrvcBxBadnsr796p2ewpns5gIA3NWvVnEY9avtgsZHu59KxK%2BhTBeejurqL8i%2FpDEQpI%2Fj7jJsrbtTjGiYK4C7Xb3zgaXvgjPXodm%2BAuM9SVXOP3skplWrJczfquNXinpLyx0LNrMRXlOdsE3kDnxWs38y1UUeWlxxAyxx9kDmcdr0DA6USxnmTX2tYNzb09bXFDdQHamAt2vnQY4w4p%2FDkOxZwoX9V4Zkv1CKkmT1Yxk6s6zN1e%2FgxmqmkuXBmE57izeHk%2FGTvQBz0k8LiUwmZ%2FoIQVTXyYeJc3%2BB%2F1AzZ5EgxnDtsQwWpdUYq4qDkQ6xuo8pa67QL9Ds5FeCTATbTrbmShSUOwwGfWOLjoB033IImlUD%2B7Fio5%2Fvqdi8cDWrwwWdx%2BHzU3QpGYdPb1tWSgVVk5AWFdqxepzYgjODWtfNK5ReyPVNY3YJhFuZMlAbVkdwP2%2FAdRlDn2%2FF%2BUgcAo0JuRwxvXEMWs8T2E8bcWyzr%2FQhOtYzSAPvEpz3JAQIBTbCqGh9eq3pdSNjTyY1L8somZujUbm7prGbZl7XzS6mtkYRatc6SWGta70U0TXEUcY1TmoC9%2FGTYuZe2MPSU5bwGOqUBUNJEzuYi679TETP7XAckhdwXDJ0K5W1PXfuRm1o8hIUaDnpZLzJMmeNO7L5YuAdNk0reqwYzae5yYom%2Bfvp77MUgKdSNRDuxL6fixg3WY3NQtqIEWsypKLl9xNWX52qrDATbvS2tUunh8Un7i9PwqaxubNTcMlE5gpar%2Bg9c6VuZTpaCm%2B1p16XN9sWUjbmFApf3wmSM4jzqLk0wZA4481fzBGOb&X-Amz-Signature=1d2b0e713205963c95e163166d87a4c64dfa85ab4d5651f3d030055730a74ff5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646Q6XCVF%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIQCbIDcRmRuWjMYlfQwMxA1mE5qgWyZ%2BBvxeWc%2B4zEwcQgIgFHEW%2FOt%2B6944EJQtkf%2Bto8eaXUOpkh5A0qHfluOwmxAq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDOsm%2FaT3NKAxNYSl%2BCrcA3B0YFTXzj%2FcyCH0W1%2FQNK%2FC7nBlZDM4vZY%2BxuE9TGrvcBxBadnsr796p2ewpns5gIA3NWvVnEY9avtgsZHu59KxK%2BhTBeejurqL8i%2FpDEQpI%2Fj7jJsrbtTjGiYK4C7Xb3zgaXvgjPXodm%2BAuM9SVXOP3skplWrJczfquNXinpLyx0LNrMRXlOdsE3kDnxWs38y1UUeWlxxAyxx9kDmcdr0DA6USxnmTX2tYNzb09bXFDdQHamAt2vnQY4w4p%2FDkOxZwoX9V4Zkv1CKkmT1Yxk6s6zN1e%2FgxmqmkuXBmE57izeHk%2FGTvQBz0k8LiUwmZ%2FoIQVTXyYeJc3%2BB%2F1AzZ5EgxnDtsQwWpdUYq4qDkQ6xuo8pa67QL9Ds5FeCTATbTrbmShSUOwwGfWOLjoB033IImlUD%2B7Fio5%2Fvqdi8cDWrwwWdx%2BHzU3QpGYdPb1tWSgVVk5AWFdqxepzYgjODWtfNK5ReyPVNY3YJhFuZMlAbVkdwP2%2FAdRlDn2%2FF%2BUgcAo0JuRwxvXEMWs8T2E8bcWyzr%2FQhOtYzSAPvEpz3JAQIBTbCqGh9eq3pdSNjTyY1L8somZujUbm7prGbZl7XzS6mtkYRatc6SWGta70U0TXEUcY1TmoC9%2FGTYuZe2MPSU5bwGOqUBUNJEzuYi679TETP7XAckhdwXDJ0K5W1PXfuRm1o8hIUaDnpZLzJMmeNO7L5YuAdNk0reqwYzae5yYom%2Bfvp77MUgKdSNRDuxL6fixg3WY3NQtqIEWsypKLl9xNWX52qrDATbvS2tUunh8Un7i9PwqaxubNTcMlE5gpar%2Bg9c6VuZTpaCm%2B1p16XN9sWUjbmFApf3wmSM4jzqLk0wZA4481fzBGOb&X-Amz-Signature=cd9c420ab6edf38dd41aebc8feed27dcff783dd5cc1290669c1b39620ee8d65c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646Q6XCVF%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIQCbIDcRmRuWjMYlfQwMxA1mE5qgWyZ%2BBvxeWc%2B4zEwcQgIgFHEW%2FOt%2B6944EJQtkf%2Bto8eaXUOpkh5A0qHfluOwmxAq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDOsm%2FaT3NKAxNYSl%2BCrcA3B0YFTXzj%2FcyCH0W1%2FQNK%2FC7nBlZDM4vZY%2BxuE9TGrvcBxBadnsr796p2ewpns5gIA3NWvVnEY9avtgsZHu59KxK%2BhTBeejurqL8i%2FpDEQpI%2Fj7jJsrbtTjGiYK4C7Xb3zgaXvgjPXodm%2BAuM9SVXOP3skplWrJczfquNXinpLyx0LNrMRXlOdsE3kDnxWs38y1UUeWlxxAyxx9kDmcdr0DA6USxnmTX2tYNzb09bXFDdQHamAt2vnQY4w4p%2FDkOxZwoX9V4Zkv1CKkmT1Yxk6s6zN1e%2FgxmqmkuXBmE57izeHk%2FGTvQBz0k8LiUwmZ%2FoIQVTXyYeJc3%2BB%2F1AzZ5EgxnDtsQwWpdUYq4qDkQ6xuo8pa67QL9Ds5FeCTATbTrbmShSUOwwGfWOLjoB033IImlUD%2B7Fio5%2Fvqdi8cDWrwwWdx%2BHzU3QpGYdPb1tWSgVVk5AWFdqxepzYgjODWtfNK5ReyPVNY3YJhFuZMlAbVkdwP2%2FAdRlDn2%2FF%2BUgcAo0JuRwxvXEMWs8T2E8bcWyzr%2FQhOtYzSAPvEpz3JAQIBTbCqGh9eq3pdSNjTyY1L8somZujUbm7prGbZl7XzS6mtkYRatc6SWGta70U0TXEUcY1TmoC9%2FGTYuZe2MPSU5bwGOqUBUNJEzuYi679TETP7XAckhdwXDJ0K5W1PXfuRm1o8hIUaDnpZLzJMmeNO7L5YuAdNk0reqwYzae5yYom%2Bfvp77MUgKdSNRDuxL6fixg3WY3NQtqIEWsypKLl9xNWX52qrDATbvS2tUunh8Un7i9PwqaxubNTcMlE5gpar%2Bg9c6VuZTpaCm%2B1p16XN9sWUjbmFApf3wmSM4jzqLk0wZA4481fzBGOb&X-Amz-Signature=3bb308b3556f2f5a0c83231f660eb8463244e5fd30e6e99d5328bbc3b1b1e730&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646Q6XCVF%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIQCbIDcRmRuWjMYlfQwMxA1mE5qgWyZ%2BBvxeWc%2B4zEwcQgIgFHEW%2FOt%2B6944EJQtkf%2Bto8eaXUOpkh5A0qHfluOwmxAq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDOsm%2FaT3NKAxNYSl%2BCrcA3B0YFTXzj%2FcyCH0W1%2FQNK%2FC7nBlZDM4vZY%2BxuE9TGrvcBxBadnsr796p2ewpns5gIA3NWvVnEY9avtgsZHu59KxK%2BhTBeejurqL8i%2FpDEQpI%2Fj7jJsrbtTjGiYK4C7Xb3zgaXvgjPXodm%2BAuM9SVXOP3skplWrJczfquNXinpLyx0LNrMRXlOdsE3kDnxWs38y1UUeWlxxAyxx9kDmcdr0DA6USxnmTX2tYNzb09bXFDdQHamAt2vnQY4w4p%2FDkOxZwoX9V4Zkv1CKkmT1Yxk6s6zN1e%2FgxmqmkuXBmE57izeHk%2FGTvQBz0k8LiUwmZ%2FoIQVTXyYeJc3%2BB%2F1AzZ5EgxnDtsQwWpdUYq4qDkQ6xuo8pa67QL9Ds5FeCTATbTrbmShSUOwwGfWOLjoB033IImlUD%2B7Fio5%2Fvqdi8cDWrwwWdx%2BHzU3QpGYdPb1tWSgVVk5AWFdqxepzYgjODWtfNK5ReyPVNY3YJhFuZMlAbVkdwP2%2FAdRlDn2%2FF%2BUgcAo0JuRwxvXEMWs8T2E8bcWyzr%2FQhOtYzSAPvEpz3JAQIBTbCqGh9eq3pdSNjTyY1L8somZujUbm7prGbZl7XzS6mtkYRatc6SWGta70U0TXEUcY1TmoC9%2FGTYuZe2MPSU5bwGOqUBUNJEzuYi679TETP7XAckhdwXDJ0K5W1PXfuRm1o8hIUaDnpZLzJMmeNO7L5YuAdNk0reqwYzae5yYom%2Bfvp77MUgKdSNRDuxL6fixg3WY3NQtqIEWsypKLl9xNWX52qrDATbvS2tUunh8Un7i9PwqaxubNTcMlE5gpar%2Bg9c6VuZTpaCm%2B1p16XN9sWUjbmFApf3wmSM4jzqLk0wZA4481fzBGOb&X-Amz-Signature=6ba482874c18965e418b72fafd546b1dfbe0470c2d8e16bf2f96e58397f7e4e4&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
