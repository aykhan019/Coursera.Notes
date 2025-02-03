

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3PE34MQ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141424Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCy6PnZoyxkrCc3LIKUvYfG9jIlmhVqQVT9X8aqaNzyUQIgfuzJvWtTnuPy0XuNmSVZl2lnIuPeEp6FMphZ1C8Xv%2BUq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDFGfrzDm7IRL3Dw8syrcA0t26kW8pkZVc8UYH77Erah5pLry9f%2BPXtS3Lz7NPnmLQZTI0tbsfI%2B4Ps%2BT77I%2B6wNX%2BX8mgCR3RSvpC%2FtILqRrAba5qFj%2FR64oYVQ8ibyHNxpM7NuX39k4llUV7XJ%2F9BPPTfxusr13rv6cvR%2FC2Dgawr8gMTQbliLMMOey7RzNiwsZF0NOl84XPq3NbW7oJ76ZZMYqm4bqtxYzkvewO7LpyXtxTdBu9EUhEKeRjoRmdgWgOQgecOSyd3BDJBlnY4nhecnKBZ7b9QkmG31AX%2F8SPk%2BVVio72U4ty9LPgOyukjb3TBWcYIZM%2BWbpE%2BHALXtsbt3DD2kruEBz2wJejeRMBsJjtQ10qzz%2FUz32zkKyaND2M8JgB0cp8JcqU9M1eWp8YzuFamvtxAsPwOiYLWQ4lX79x301FTqk9XTHlxVXMMWK3sfZPZ0Qm3QR8TtRV4owe3R2YY30L%2BIPB1FNCR0zOo7dLsGclxT3Dpr%2BcvHGZok7NGWIr7YoOSZbgS%2F6SqNi1OgVrlYfg%2BtEZQWoMe%2FAiRdWoZ%2BdqK%2F44Z260ZvFruoPK0D4Zl4xNZK71fO6Rzqf1UIM1sGlsOp1Z66eUOxRShkwKTG897r%2FmVAA1JdtqdQYIdgcyCOlT5W0MJ%2BNg70GOqUBlDMLMc%2BrvW9FrITBax2opl2CFf9iV3jDY4fdyV1PCSWVj7K%2FyIia72z5RaySa%2B%2F5DxbLwLJnUXxFqLVsH3Ax%2BYFDhXPilLomkt7T7V92380BcWdb%2BjrlBK3KUpDCqVkeuQbRG%2B2wColp8y17Z2OWcTCxbbQCSmkRR80qLd3BR9gUUWQdeMg0clJT%2FkxcXVf7YrzfZKb%2FxUqSBy3d%2FCHnDpD07D8k&X-Amz-Signature=1428d201bc162fe27735a481ff3ccdd2ae5efd858409f06624304c3e62a28df6&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3PE34MQ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141424Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCy6PnZoyxkrCc3LIKUvYfG9jIlmhVqQVT9X8aqaNzyUQIgfuzJvWtTnuPy0XuNmSVZl2lnIuPeEp6FMphZ1C8Xv%2BUq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDFGfrzDm7IRL3Dw8syrcA0t26kW8pkZVc8UYH77Erah5pLry9f%2BPXtS3Lz7NPnmLQZTI0tbsfI%2B4Ps%2BT77I%2B6wNX%2BX8mgCR3RSvpC%2FtILqRrAba5qFj%2FR64oYVQ8ibyHNxpM7NuX39k4llUV7XJ%2F9BPPTfxusr13rv6cvR%2FC2Dgawr8gMTQbliLMMOey7RzNiwsZF0NOl84XPq3NbW7oJ76ZZMYqm4bqtxYzkvewO7LpyXtxTdBu9EUhEKeRjoRmdgWgOQgecOSyd3BDJBlnY4nhecnKBZ7b9QkmG31AX%2F8SPk%2BVVio72U4ty9LPgOyukjb3TBWcYIZM%2BWbpE%2BHALXtsbt3DD2kruEBz2wJejeRMBsJjtQ10qzz%2FUz32zkKyaND2M8JgB0cp8JcqU9M1eWp8YzuFamvtxAsPwOiYLWQ4lX79x301FTqk9XTHlxVXMMWK3sfZPZ0Qm3QR8TtRV4owe3R2YY30L%2BIPB1FNCR0zOo7dLsGclxT3Dpr%2BcvHGZok7NGWIr7YoOSZbgS%2F6SqNi1OgVrlYfg%2BtEZQWoMe%2FAiRdWoZ%2BdqK%2F44Z260ZvFruoPK0D4Zl4xNZK71fO6Rzqf1UIM1sGlsOp1Z66eUOxRShkwKTG897r%2FmVAA1JdtqdQYIdgcyCOlT5W0MJ%2BNg70GOqUBlDMLMc%2BrvW9FrITBax2opl2CFf9iV3jDY4fdyV1PCSWVj7K%2FyIia72z5RaySa%2B%2F5DxbLwLJnUXxFqLVsH3Ax%2BYFDhXPilLomkt7T7V92380BcWdb%2BjrlBK3KUpDCqVkeuQbRG%2B2wColp8y17Z2OWcTCxbbQCSmkRR80qLd3BR9gUUWQdeMg0clJT%2FkxcXVf7YrzfZKb%2FxUqSBy3d%2FCHnDpD07D8k&X-Amz-Signature=3ee51f4b3fc5e951a8a4cb9f590f548137d8e8989a754de8da278ad4d2fcf9ac&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3PE34MQ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141424Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCy6PnZoyxkrCc3LIKUvYfG9jIlmhVqQVT9X8aqaNzyUQIgfuzJvWtTnuPy0XuNmSVZl2lnIuPeEp6FMphZ1C8Xv%2BUq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDFGfrzDm7IRL3Dw8syrcA0t26kW8pkZVc8UYH77Erah5pLry9f%2BPXtS3Lz7NPnmLQZTI0tbsfI%2B4Ps%2BT77I%2B6wNX%2BX8mgCR3RSvpC%2FtILqRrAba5qFj%2FR64oYVQ8ibyHNxpM7NuX39k4llUV7XJ%2F9BPPTfxusr13rv6cvR%2FC2Dgawr8gMTQbliLMMOey7RzNiwsZF0NOl84XPq3NbW7oJ76ZZMYqm4bqtxYzkvewO7LpyXtxTdBu9EUhEKeRjoRmdgWgOQgecOSyd3BDJBlnY4nhecnKBZ7b9QkmG31AX%2F8SPk%2BVVio72U4ty9LPgOyukjb3TBWcYIZM%2BWbpE%2BHALXtsbt3DD2kruEBz2wJejeRMBsJjtQ10qzz%2FUz32zkKyaND2M8JgB0cp8JcqU9M1eWp8YzuFamvtxAsPwOiYLWQ4lX79x301FTqk9XTHlxVXMMWK3sfZPZ0Qm3QR8TtRV4owe3R2YY30L%2BIPB1FNCR0zOo7dLsGclxT3Dpr%2BcvHGZok7NGWIr7YoOSZbgS%2F6SqNi1OgVrlYfg%2BtEZQWoMe%2FAiRdWoZ%2BdqK%2F44Z260ZvFruoPK0D4Zl4xNZK71fO6Rzqf1UIM1sGlsOp1Z66eUOxRShkwKTG897r%2FmVAA1JdtqdQYIdgcyCOlT5W0MJ%2BNg70GOqUBlDMLMc%2BrvW9FrITBax2opl2CFf9iV3jDY4fdyV1PCSWVj7K%2FyIia72z5RaySa%2B%2F5DxbLwLJnUXxFqLVsH3Ax%2BYFDhXPilLomkt7T7V92380BcWdb%2BjrlBK3KUpDCqVkeuQbRG%2B2wColp8y17Z2OWcTCxbbQCSmkRR80qLd3BR9gUUWQdeMg0clJT%2FkxcXVf7YrzfZKb%2FxUqSBy3d%2FCHnDpD07D8k&X-Amz-Signature=735946fa8a4add2ec47fe326aeb3a86a69c0ecdaf749a5b2061185fed2f1b5af&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPZ2TSRE%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141425Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCLfSKFtv29ynfH9MvEfwe508W2X3iWvRpVlRVaAysbewIhALTQl9U%2B5JhpMplo7J6fkz3DRHvksHkkII021mYmV%2BX4Kv8DCBcQABoMNjM3NDIzMTgzODA1Igz%2BAjFlTgnZmdjcDJsq3AOIt5q%2FlYdLmU9M%2FH%2BCbCwZJUOKkSeoDV%2F%2F5CGao%2BtPlsEhBq%2FuxBBaB2mt8HQe1gS0hsdV4Kf4afSY1FHFIRScFH3aHV5mNpuirD5iQchVdN%2FBCktQ6aNpTgskZmblBVHpsev%2Bv2TnR8eKlHovpEcwSGbAmMuZwgVnBkiLMdrjdLyrGJIPqnGmCBY2SYZt9ZpiNR0F%2FWREq8y4wB5hK5hjs1GGf5qDYGZ0nD3twGO6Z%2BGx9ejXJoD3T%2FZHYIiorL2zZIRMJI7Efdq6dlSM9mGLdm15OFrqJJFsLyHzALhKMg6FdWWefArDg72sfjw0T70f%2B9v7a64PhtkmS%2BryLrpkg4l7CWtreqAPeLAY7bjAJSFbqqeRadWI3OipFBMaJr3887v%2F66DR%2BhviOAtLug8dLIUE1JrOqGodmvblDbvG8mG7JpJePP9zA9O%2B8faAR%2Fd4nbFbR8XrAiVeGYgcVXON38W6sfqw4pUWY8txL9zoQKLf%2FFalgOw5q%2BS0YHRy28fmLfG2y2YH8%2FP0awCSYVkPpITenPBaVeSftWA8VeKRJIvixRLQOoDH3epp6b%2FLHS%2FMv5YSV6S885B66yCx4%2BrYTS5P6oODh%2FdcEXHutrYbo1xNVtFSqmDJJo4cQTDkjYO9BjqkAcoEUStjQgsetDdc4PvpIcMPXCHQ2WipnacD%2BHeWdNmv0%2FszlQZ6sKwPanC7llH5jgmx5GrxTMSnJ712LKyjwHkBC1i%2FYRP8dUxb9dnyYCZBMzWGXF%2B7nkY%2BaxnApxAOmqtep%2BjYQJYfQJOz8LOxv%2BD0AAe6VfAIjG%2BJ3mNyiLHuoUwtYHRuH5Ij%2Buq3n0U2RAKdXYPuA7pi8k%2FwUL7W7OcB3Dfi&X-Amz-Signature=1e5a9a46b34de859eceda4db784584a43307df1a4cab6a6ec8a9f4c245eab10b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YLKS3A7Q%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141428Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC7irSITGfsMM4fWeHobnDud7SG17TLu3YjQHPXrPDjFAIgOUL3pBeR029%2B%2FwepxEzLCM0wxUY4YwwFP5dkfbt2DnEq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDAg0SIJmiLQPzNjE8ircA9KAuT5bvhF8mGr6DB7fkTiHSlACUQCUxfkQEIvbefbM0pyg5wKpP7TgWBmVgP0vInv%2B3z5kcCgYOczSb2KIKWHVM8P9%2Bev6fR%2FWLQ%2BoYL8077aAiBtyh2umFhDF43Cf%2BPkLpy%2FmrPcmLONdyk0R7bowwWydpv1x3ctl3Fbil%2FYB5Xu34OHEE7PAda8gZ6wyQ3bPumqurd3BJKQ45dxbBuHG7hqWjhX%2FRYpTu1LpnIFu%2F5a%2FlQZu1oey0WsUwbMm62hjW7LOeLUPn%2BY93VRwB%2FfkEgkXYiEu48KnRg%2FYb83KD0dugF%2BMat6D859U4svv0k1pI8Sge4UqZ0mVrbDS7rhJ6ktqiAc63DGhnUCjL23IAe%2BSdBD9PH0kfzRcNG8x86YWrA5D5bYxfxAQ7KCR3tui0i7PPEtqJeVk9CCbEdnKjQJNPnz7jLKMqSEkNMgOrGLQiX9W3ViubRZF%2B82H1KkLFrU00VMIGbyBSVmC2MmLcBmzhN%2FsahxamMbwdFEWRkx3QGX27J3BaxBvstlXwyLrrCBqXZr3FvJ4xkfY1hfK55wQBfVTpg0l2qELYu3bM7US8uQPm8IfgoXGbI%2BkyoRmui%2FOwtslG28nAC8X1VTDtrYBnNldqGgis%2FANMOKNg70GOqUBBv%2FAcPppo7XPj9eiPvoYLP7ud%2FoYBCKNmpG1PDyUPbCaew7uz570xxhFEkRixJQWN9cJla1XdyjXbDuOlU%2BroRZvpb3UU6%2F1Qdhf57Y1b0Uy9tULKKQVHbnd8C%2FrNm6X5TRlcE7M5wn%2BSB65ud1EPyOsD0WV6fyNEBno9pZGYtA4m9ihQ1W9Dz8YAKPl%2B5IZOxsJyxrbV5co6BvHbY7lCNembKq4&X-Amz-Signature=ff6fdb7b9fe7ef10a12b53d47d6f53ee54bd76dffff1d27efe8b91fdf0ee4496&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3PE34MQ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141424Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCy6PnZoyxkrCc3LIKUvYfG9jIlmhVqQVT9X8aqaNzyUQIgfuzJvWtTnuPy0XuNmSVZl2lnIuPeEp6FMphZ1C8Xv%2BUq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDFGfrzDm7IRL3Dw8syrcA0t26kW8pkZVc8UYH77Erah5pLry9f%2BPXtS3Lz7NPnmLQZTI0tbsfI%2B4Ps%2BT77I%2B6wNX%2BX8mgCR3RSvpC%2FtILqRrAba5qFj%2FR64oYVQ8ibyHNxpM7NuX39k4llUV7XJ%2F9BPPTfxusr13rv6cvR%2FC2Dgawr8gMTQbliLMMOey7RzNiwsZF0NOl84XPq3NbW7oJ76ZZMYqm4bqtxYzkvewO7LpyXtxTdBu9EUhEKeRjoRmdgWgOQgecOSyd3BDJBlnY4nhecnKBZ7b9QkmG31AX%2F8SPk%2BVVio72U4ty9LPgOyukjb3TBWcYIZM%2BWbpE%2BHALXtsbt3DD2kruEBz2wJejeRMBsJjtQ10qzz%2FUz32zkKyaND2M8JgB0cp8JcqU9M1eWp8YzuFamvtxAsPwOiYLWQ4lX79x301FTqk9XTHlxVXMMWK3sfZPZ0Qm3QR8TtRV4owe3R2YY30L%2BIPB1FNCR0zOo7dLsGclxT3Dpr%2BcvHGZok7NGWIr7YoOSZbgS%2F6SqNi1OgVrlYfg%2BtEZQWoMe%2FAiRdWoZ%2BdqK%2F44Z260ZvFruoPK0D4Zl4xNZK71fO6Rzqf1UIM1sGlsOp1Z66eUOxRShkwKTG897r%2FmVAA1JdtqdQYIdgcyCOlT5W0MJ%2BNg70GOqUBlDMLMc%2BrvW9FrITBax2opl2CFf9iV3jDY4fdyV1PCSWVj7K%2FyIia72z5RaySa%2B%2F5DxbLwLJnUXxFqLVsH3Ax%2BYFDhXPilLomkt7T7V92380BcWdb%2BjrlBK3KUpDCqVkeuQbRG%2B2wColp8y17Z2OWcTCxbbQCSmkRR80qLd3BR9gUUWQdeMg0clJT%2FkxcXVf7YrzfZKb%2FxUqSBy3d%2FCHnDpD07D8k&X-Amz-Signature=767eeb86f523338f74d1b25a42351cca4b00390cf49e17c4897372e12ba20828&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3PE34MQ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141424Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCy6PnZoyxkrCc3LIKUvYfG9jIlmhVqQVT9X8aqaNzyUQIgfuzJvWtTnuPy0XuNmSVZl2lnIuPeEp6FMphZ1C8Xv%2BUq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDFGfrzDm7IRL3Dw8syrcA0t26kW8pkZVc8UYH77Erah5pLry9f%2BPXtS3Lz7NPnmLQZTI0tbsfI%2B4Ps%2BT77I%2B6wNX%2BX8mgCR3RSvpC%2FtILqRrAba5qFj%2FR64oYVQ8ibyHNxpM7NuX39k4llUV7XJ%2F9BPPTfxusr13rv6cvR%2FC2Dgawr8gMTQbliLMMOey7RzNiwsZF0NOl84XPq3NbW7oJ76ZZMYqm4bqtxYzkvewO7LpyXtxTdBu9EUhEKeRjoRmdgWgOQgecOSyd3BDJBlnY4nhecnKBZ7b9QkmG31AX%2F8SPk%2BVVio72U4ty9LPgOyukjb3TBWcYIZM%2BWbpE%2BHALXtsbt3DD2kruEBz2wJejeRMBsJjtQ10qzz%2FUz32zkKyaND2M8JgB0cp8JcqU9M1eWp8YzuFamvtxAsPwOiYLWQ4lX79x301FTqk9XTHlxVXMMWK3sfZPZ0Qm3QR8TtRV4owe3R2YY30L%2BIPB1FNCR0zOo7dLsGclxT3Dpr%2BcvHGZok7NGWIr7YoOSZbgS%2F6SqNi1OgVrlYfg%2BtEZQWoMe%2FAiRdWoZ%2BdqK%2F44Z260ZvFruoPK0D4Zl4xNZK71fO6Rzqf1UIM1sGlsOp1Z66eUOxRShkwKTG897r%2FmVAA1JdtqdQYIdgcyCOlT5W0MJ%2BNg70GOqUBlDMLMc%2BrvW9FrITBax2opl2CFf9iV3jDY4fdyV1PCSWVj7K%2FyIia72z5RaySa%2B%2F5DxbLwLJnUXxFqLVsH3Ax%2BYFDhXPilLomkt7T7V92380BcWdb%2BjrlBK3KUpDCqVkeuQbRG%2B2wColp8y17Z2OWcTCxbbQCSmkRR80qLd3BR9gUUWQdeMg0clJT%2FkxcXVf7YrzfZKb%2FxUqSBy3d%2FCHnDpD07D8k&X-Amz-Signature=c42cde3372c3a233cbd01efa780408b7906cedaca602974da473666db5b37306&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3PE34MQ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141424Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCy6PnZoyxkrCc3LIKUvYfG9jIlmhVqQVT9X8aqaNzyUQIgfuzJvWtTnuPy0XuNmSVZl2lnIuPeEp6FMphZ1C8Xv%2BUq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDFGfrzDm7IRL3Dw8syrcA0t26kW8pkZVc8UYH77Erah5pLry9f%2BPXtS3Lz7NPnmLQZTI0tbsfI%2B4Ps%2BT77I%2B6wNX%2BX8mgCR3RSvpC%2FtILqRrAba5qFj%2FR64oYVQ8ibyHNxpM7NuX39k4llUV7XJ%2F9BPPTfxusr13rv6cvR%2FC2Dgawr8gMTQbliLMMOey7RzNiwsZF0NOl84XPq3NbW7oJ76ZZMYqm4bqtxYzkvewO7LpyXtxTdBu9EUhEKeRjoRmdgWgOQgecOSyd3BDJBlnY4nhecnKBZ7b9QkmG31AX%2F8SPk%2BVVio72U4ty9LPgOyukjb3TBWcYIZM%2BWbpE%2BHALXtsbt3DD2kruEBz2wJejeRMBsJjtQ10qzz%2FUz32zkKyaND2M8JgB0cp8JcqU9M1eWp8YzuFamvtxAsPwOiYLWQ4lX79x301FTqk9XTHlxVXMMWK3sfZPZ0Qm3QR8TtRV4owe3R2YY30L%2BIPB1FNCR0zOo7dLsGclxT3Dpr%2BcvHGZok7NGWIr7YoOSZbgS%2F6SqNi1OgVrlYfg%2BtEZQWoMe%2FAiRdWoZ%2BdqK%2F44Z260ZvFruoPK0D4Zl4xNZK71fO6Rzqf1UIM1sGlsOp1Z66eUOxRShkwKTG897r%2FmVAA1JdtqdQYIdgcyCOlT5W0MJ%2BNg70GOqUBlDMLMc%2BrvW9FrITBax2opl2CFf9iV3jDY4fdyV1PCSWVj7K%2FyIia72z5RaySa%2B%2F5DxbLwLJnUXxFqLVsH3Ax%2BYFDhXPilLomkt7T7V92380BcWdb%2BjrlBK3KUpDCqVkeuQbRG%2B2wColp8y17Z2OWcTCxbbQCSmkRR80qLd3BR9gUUWQdeMg0clJT%2FkxcXVf7YrzfZKb%2FxUqSBy3d%2FCHnDpD07D8k&X-Amz-Signature=5e4799fdeb230e906009bfb57d1ac9d9b64ef2ace928ec2ab3a969d74c94ff45&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3PE34MQ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141424Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCy6PnZoyxkrCc3LIKUvYfG9jIlmhVqQVT9X8aqaNzyUQIgfuzJvWtTnuPy0XuNmSVZl2lnIuPeEp6FMphZ1C8Xv%2BUq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDFGfrzDm7IRL3Dw8syrcA0t26kW8pkZVc8UYH77Erah5pLry9f%2BPXtS3Lz7NPnmLQZTI0tbsfI%2B4Ps%2BT77I%2B6wNX%2BX8mgCR3RSvpC%2FtILqRrAba5qFj%2FR64oYVQ8ibyHNxpM7NuX39k4llUV7XJ%2F9BPPTfxusr13rv6cvR%2FC2Dgawr8gMTQbliLMMOey7RzNiwsZF0NOl84XPq3NbW7oJ76ZZMYqm4bqtxYzkvewO7LpyXtxTdBu9EUhEKeRjoRmdgWgOQgecOSyd3BDJBlnY4nhecnKBZ7b9QkmG31AX%2F8SPk%2BVVio72U4ty9LPgOyukjb3TBWcYIZM%2BWbpE%2BHALXtsbt3DD2kruEBz2wJejeRMBsJjtQ10qzz%2FUz32zkKyaND2M8JgB0cp8JcqU9M1eWp8YzuFamvtxAsPwOiYLWQ4lX79x301FTqk9XTHlxVXMMWK3sfZPZ0Qm3QR8TtRV4owe3R2YY30L%2BIPB1FNCR0zOo7dLsGclxT3Dpr%2BcvHGZok7NGWIr7YoOSZbgS%2F6SqNi1OgVrlYfg%2BtEZQWoMe%2FAiRdWoZ%2BdqK%2F44Z260ZvFruoPK0D4Zl4xNZK71fO6Rzqf1UIM1sGlsOp1Z66eUOxRShkwKTG897r%2FmVAA1JdtqdQYIdgcyCOlT5W0MJ%2BNg70GOqUBlDMLMc%2BrvW9FrITBax2opl2CFf9iV3jDY4fdyV1PCSWVj7K%2FyIia72z5RaySa%2B%2F5DxbLwLJnUXxFqLVsH3Ax%2BYFDhXPilLomkt7T7V92380BcWdb%2BjrlBK3KUpDCqVkeuQbRG%2B2wColp8y17Z2OWcTCxbbQCSmkRR80qLd3BR9gUUWQdeMg0clJT%2FkxcXVf7YrzfZKb%2FxUqSBy3d%2FCHnDpD07D8k&X-Amz-Signature=b10870d723d79fffee55a8fe3d749c77404e471d87783659b0f62cc977b93483&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
