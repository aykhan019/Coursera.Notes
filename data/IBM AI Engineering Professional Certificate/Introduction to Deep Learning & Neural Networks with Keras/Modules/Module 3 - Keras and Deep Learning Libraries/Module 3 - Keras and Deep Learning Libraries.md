

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U4GFSXEG%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJGMEQCIDEOapZmLGKAHdV1lVMJQ1tL6rJBSU1GJP7Y9cV7qjz9AiBmTtxUe46W5g4dC2QTFvgu%2FhbhYFiwiZiQPQeNx7uK3ir%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIM5zEBAQb1wWUSOMtCKtwDoLjDpVN%2BUFemhgAyCAXsyCCFmQDFfXy4R9CwGenFhD8w81givBtRUtcDk3BMgxsl7ETRJRCOxN51uOhJl8Wjs5XSnQ0r2GtNQRH%2FAjJ2XGyt5NKAdUAB96i8OEO%2FR%2FG34PK5va6zpYawCVzytmhaGOssD18TQzw%2Bl1hfqh%2FDQf9qgYCzAFRGPDsIzju1QggUSJRF2iahRqkFxeJoy8woYXpp5GnZ425YFqRVn0IwobXYIHI0AiRnJDWMrWLQuutvvD8zTUGwCQCbwnvOOL42D58u32WpDL33hHBugXFpSYUzSdaLxLWqoLfP%2F0%2F%2F9DaMdoW7bZ39B9ZH8l%2F89%2BNRuQry5WBa4t7xyqxQ84hmyJH%2BPLZwBOh%2F85Bk0k7EbVfe%2Bxatyo%2F9bXr%2FVI9CeoUxXCZcnKaLeIdPj8E8MGFkSkYlKteGb3ro4kVcHAuORW%2BhR42izAnBtUh38Y1z3CfNekOqvxpjF%2Fu8slW%2B3HHzuNvsiyQE8nfvYaZfPleHwc48JuC4GWnHrAkatK7z9X%2FkfdIXbpz4cpGVgUMaV8F4r%2B1cXWhi%2F2f5xDLbSs4hpHNHFH3elGHeRutw3pgz78oGSe8CkK6mYhLsNElWOCDCeLPDw%2F1xBGDS%2FpRBBRQwzdGTvQY6pgFL0tbN2JRcNzznl%2B6uJefmrBumlyUvGo6V%2BNFYnuBxwLc4LidYpWEabGxjmy0W0am5r4js5sQBm4er4goHJdcjKVfnXpDQRM1fzIyfYOIZZ07aTM6QvIjCwBlojhM3%2BHSii9P1qrH%2BS6xhqRv%2FudxykB%2FV5jkKr926nNbdAhf69fz4PcVDqUoI2IqClVtN2UgR8eKRYlEJHhvaiEHjZ0CmWW9Cet%2FD&X-Amz-Signature=51d18289e56932b643fa249bb10d13a6f11f170824e8c144d91b4bb8314c7502&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U4GFSXEG%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJGMEQCIDEOapZmLGKAHdV1lVMJQ1tL6rJBSU1GJP7Y9cV7qjz9AiBmTtxUe46W5g4dC2QTFvgu%2FhbhYFiwiZiQPQeNx7uK3ir%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIM5zEBAQb1wWUSOMtCKtwDoLjDpVN%2BUFemhgAyCAXsyCCFmQDFfXy4R9CwGenFhD8w81givBtRUtcDk3BMgxsl7ETRJRCOxN51uOhJl8Wjs5XSnQ0r2GtNQRH%2FAjJ2XGyt5NKAdUAB96i8OEO%2FR%2FG34PK5va6zpYawCVzytmhaGOssD18TQzw%2Bl1hfqh%2FDQf9qgYCzAFRGPDsIzju1QggUSJRF2iahRqkFxeJoy8woYXpp5GnZ425YFqRVn0IwobXYIHI0AiRnJDWMrWLQuutvvD8zTUGwCQCbwnvOOL42D58u32WpDL33hHBugXFpSYUzSdaLxLWqoLfP%2F0%2F%2F9DaMdoW7bZ39B9ZH8l%2F89%2BNRuQry5WBa4t7xyqxQ84hmyJH%2BPLZwBOh%2F85Bk0k7EbVfe%2Bxatyo%2F9bXr%2FVI9CeoUxXCZcnKaLeIdPj8E8MGFkSkYlKteGb3ro4kVcHAuORW%2BhR42izAnBtUh38Y1z3CfNekOqvxpjF%2Fu8slW%2B3HHzuNvsiyQE8nfvYaZfPleHwc48JuC4GWnHrAkatK7z9X%2FkfdIXbpz4cpGVgUMaV8F4r%2B1cXWhi%2F2f5xDLbSs4hpHNHFH3elGHeRutw3pgz78oGSe8CkK6mYhLsNElWOCDCeLPDw%2F1xBGDS%2FpRBBRQwzdGTvQY6pgFL0tbN2JRcNzznl%2B6uJefmrBumlyUvGo6V%2BNFYnuBxwLc4LidYpWEabGxjmy0W0am5r4js5sQBm4er4goHJdcjKVfnXpDQRM1fzIyfYOIZZ07aTM6QvIjCwBlojhM3%2BHSii9P1qrH%2BS6xhqRv%2FudxykB%2FV5jkKr926nNbdAhf69fz4PcVDqUoI2IqClVtN2UgR8eKRYlEJHhvaiEHjZ0CmWW9Cet%2FD&X-Amz-Signature=2ce9f85b1cffe783f22d3fb6941068b1f69993d90369aac9eb125570c5cd5ff5&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U4GFSXEG%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJGMEQCIDEOapZmLGKAHdV1lVMJQ1tL6rJBSU1GJP7Y9cV7qjz9AiBmTtxUe46W5g4dC2QTFvgu%2FhbhYFiwiZiQPQeNx7uK3ir%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIM5zEBAQb1wWUSOMtCKtwDoLjDpVN%2BUFemhgAyCAXsyCCFmQDFfXy4R9CwGenFhD8w81givBtRUtcDk3BMgxsl7ETRJRCOxN51uOhJl8Wjs5XSnQ0r2GtNQRH%2FAjJ2XGyt5NKAdUAB96i8OEO%2FR%2FG34PK5va6zpYawCVzytmhaGOssD18TQzw%2Bl1hfqh%2FDQf9qgYCzAFRGPDsIzju1QggUSJRF2iahRqkFxeJoy8woYXpp5GnZ425YFqRVn0IwobXYIHI0AiRnJDWMrWLQuutvvD8zTUGwCQCbwnvOOL42D58u32WpDL33hHBugXFpSYUzSdaLxLWqoLfP%2F0%2F%2F9DaMdoW7bZ39B9ZH8l%2F89%2BNRuQry5WBa4t7xyqxQ84hmyJH%2BPLZwBOh%2F85Bk0k7EbVfe%2Bxatyo%2F9bXr%2FVI9CeoUxXCZcnKaLeIdPj8E8MGFkSkYlKteGb3ro4kVcHAuORW%2BhR42izAnBtUh38Y1z3CfNekOqvxpjF%2Fu8slW%2B3HHzuNvsiyQE8nfvYaZfPleHwc48JuC4GWnHrAkatK7z9X%2FkfdIXbpz4cpGVgUMaV8F4r%2B1cXWhi%2F2f5xDLbSs4hpHNHFH3elGHeRutw3pgz78oGSe8CkK6mYhLsNElWOCDCeLPDw%2F1xBGDS%2FpRBBRQwzdGTvQY6pgFL0tbN2JRcNzznl%2B6uJefmrBumlyUvGo6V%2BNFYnuBxwLc4LidYpWEabGxjmy0W0am5r4js5sQBm4er4goHJdcjKVfnXpDQRM1fzIyfYOIZZ07aTM6QvIjCwBlojhM3%2BHSii9P1qrH%2BS6xhqRv%2FudxykB%2FV5jkKr926nNbdAhf69fz4PcVDqUoI2IqClVtN2UgR8eKRYlEJHhvaiEHjZ0CmWW9Cet%2FD&X-Amz-Signature=2df3f8d7b6e9953b94b6d6b49c7ae8f4579f3a5dc4e8fb2e88ade83ba7916c01&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666MEKX7F3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJGMEQCIAQri1K9psQ89DVeZQNUvX73oz7R6Xru5f5JRNvb%2FB7dAiBBDgRptcNzDYS5wVJ4vkohKphQLOJg16aB%2BvQ9xbLhiyr%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIMth9xTN836nrJQSy0KtwDAYHY13M5wkXBCGXoExJy98FL70Rah0EeE9DyjrsJrjzgPsZ%2FxCnO4QyH%2FWwmi8wgw90%2BOvYjcLxkTi%2BAZhbCzWqP8OUKmqpMN2R2Gnde3AteqP2AbGTfExiZny0I9hXhKqO0JiPrAtnhcTOuAQq%2Braxoc0RTUS3Py4xnWMmcq017Gt6q%2FjfbZ%2FdNe94fbkWdidzT3TQQANg%2Fr0DZU9dgg9D0g0PN6yRTgDu0Tffn2e474IqqJO7%2F7%2BJ8EzXdahK978JWbyTLFhGzMYTDyZfXunecevUe6Of54fXEgv5tLlTc3VArjQb4v5OB3WWW6GvO4Fmv82yaiMVZTlf01ebWYvhjpWb2WHbb4NOhj2aoHXnlKXwLz1gfMhKmmuNpa9fEftc1Qi4BDLQM4DfxL%2FSZ3UnNvKD284njTQ38B%2BHKfwadf6vD9MaNRQ%2Bnc4vnrPjpjVlMu9BSynmzwYrnWIGUtIp6xXKSJeHv00PRa07pIQojairQwN6KHJ2sRrUF2SYo6vB6IXkJLSLdpagWsHiEVGQYAWhFvx7JLUsZ4aZzPiUKbwC2MxIpESt6ye9n2Fltx9Wu%2FlNw8CGfRbj5%2FDTd7D1kdpry0wY1jZT%2BdXyz2PTc67gZWcTawEC%2BAE0w39GTvQY6pgH5QsRVjxUr1SHhZ%2FFaTQr%2BePjL%2B8GLpQNCimrxLzl1fAEci%2B3ftY5EOKb0hjoX84nMZmETBWLNaWIGlQv1E6EgVQfT4qgqZWOHZD6cdu9XEj6FqniPnn4%2F66fscCHQ78Fd%2B08%2B2NxPS7ZmZBIq%2BroySRtYAA%2BP1agjMk9Pyg1NocyTELG88K4aw%2BvmaNvjtUnkhXyMf1bDv36RZI5JMbGjQF%2BX4T79&X-Amz-Signature=f2508d30b2889cba663536adf84789d128d040c0700850af9b854a2fa5db1f57&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662RROEJC2%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIQCnTDFsjRgzZRIU9QF3pIOrVkDUcxgQa%2Fl9YqR6kadgbAIgIX4dToenXtoeYGAbrbG9zNn6AzBNWS%2B0teRwzW7upqEq%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDLyJovp5VCyT5t%2FIwSrcAzo92bGmySiNMN1XB4Clgq2DC89cPAIONZh8xohFiix9azN0ylkarn9o3cZ2Jas6gXWUwX7mOgzuGoYHguF2WWzSR%2BDHSLxbDHy8%2BMNpVzpci4NukXVohyjoTk3PFXyRjqDGe8%2FFmtRlAHOHhfCz8ArcItjgg6rrDuN4Hkhdmup6188kFcJk8WXDU2F3ws5dc06mjGzBa7MS0WPqb8S5eCSj02nRDa%2Bb0nt1P1PFiBO2JjrlYtgK43T6O6%2Bcva6n%2BJ20rPqeUT1dv5jfWcQdCHmVlpFW8a1AAXrraodFNmqpe7hhlL9PtVerveE6TFStxBdzS%2BPOy8wV6y3yYnuep9DFmtRpYxsv5KkvdHfum6Xp9WTVCvp4arAFWXZ146IgQW01qobilkj89JTscZLSXqYxoZCigZls9MGQ6jThLooPtawHdzTH877Xbdo88qP1QpAKJeIlNYDj4p%2BJNPPULRkG2uHZE8jQil7C6ELe7VEpNBH9axNlNy7SijrlnP%2B7Hsd2%2Fseh1raAzw938NfW0AAau8YXYWhLtKR6WntUWygmbeWgKkmbBFuGb4GPgSmuNnM%2B3ufKhufawjMByKinN0J3JKBRd6noFBdqB7uAIMSBMJANPUXsc4ApD1QqMObSk70GOqUB7mFY%2B3gDMExY5zllhWkQyHc4g%2FLHVtA8OagGs0AC6ZS91evKXuxVwGBlFFNcVvZQlDD2M33DNnv7pRMTuDzCvA4dmO72rldLTKHIMV5VeXKSxoC5CI50hSUKeWw9MO5SwB4kA7jW0GghXd3CB7vnKGHGAms85rGHX4DmYk7TFLT%2FJ1XKdKrEMcJptc1iAIk%2BFnpa5PbTJDW3K5jB4FMb0f1jh8%2Fd&X-Amz-Signature=589dd5c70c64a3b80b426fb2ce3c4ac8592e0de437f2ef0d8bcbed368fea66d6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U4GFSXEG%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJGMEQCIDEOapZmLGKAHdV1lVMJQ1tL6rJBSU1GJP7Y9cV7qjz9AiBmTtxUe46W5g4dC2QTFvgu%2FhbhYFiwiZiQPQeNx7uK3ir%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIM5zEBAQb1wWUSOMtCKtwDoLjDpVN%2BUFemhgAyCAXsyCCFmQDFfXy4R9CwGenFhD8w81givBtRUtcDk3BMgxsl7ETRJRCOxN51uOhJl8Wjs5XSnQ0r2GtNQRH%2FAjJ2XGyt5NKAdUAB96i8OEO%2FR%2FG34PK5va6zpYawCVzytmhaGOssD18TQzw%2Bl1hfqh%2FDQf9qgYCzAFRGPDsIzju1QggUSJRF2iahRqkFxeJoy8woYXpp5GnZ425YFqRVn0IwobXYIHI0AiRnJDWMrWLQuutvvD8zTUGwCQCbwnvOOL42D58u32WpDL33hHBugXFpSYUzSdaLxLWqoLfP%2F0%2F%2F9DaMdoW7bZ39B9ZH8l%2F89%2BNRuQry5WBa4t7xyqxQ84hmyJH%2BPLZwBOh%2F85Bk0k7EbVfe%2Bxatyo%2F9bXr%2FVI9CeoUxXCZcnKaLeIdPj8E8MGFkSkYlKteGb3ro4kVcHAuORW%2BhR42izAnBtUh38Y1z3CfNekOqvxpjF%2Fu8slW%2B3HHzuNvsiyQE8nfvYaZfPleHwc48JuC4GWnHrAkatK7z9X%2FkfdIXbpz4cpGVgUMaV8F4r%2B1cXWhi%2F2f5xDLbSs4hpHNHFH3elGHeRutw3pgz78oGSe8CkK6mYhLsNElWOCDCeLPDw%2F1xBGDS%2FpRBBRQwzdGTvQY6pgFL0tbN2JRcNzznl%2B6uJefmrBumlyUvGo6V%2BNFYnuBxwLc4LidYpWEabGxjmy0W0am5r4js5sQBm4er4goHJdcjKVfnXpDQRM1fzIyfYOIZZ07aTM6QvIjCwBlojhM3%2BHSii9P1qrH%2BS6xhqRv%2FudxykB%2FV5jkKr926nNbdAhf69fz4PcVDqUoI2IqClVtN2UgR8eKRYlEJHhvaiEHjZ0CmWW9Cet%2FD&X-Amz-Signature=4afc215329809d867329184fd081bdb61b0a5577132d234fc828090ac3abdd99&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U4GFSXEG%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJGMEQCIDEOapZmLGKAHdV1lVMJQ1tL6rJBSU1GJP7Y9cV7qjz9AiBmTtxUe46W5g4dC2QTFvgu%2FhbhYFiwiZiQPQeNx7uK3ir%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIM5zEBAQb1wWUSOMtCKtwDoLjDpVN%2BUFemhgAyCAXsyCCFmQDFfXy4R9CwGenFhD8w81givBtRUtcDk3BMgxsl7ETRJRCOxN51uOhJl8Wjs5XSnQ0r2GtNQRH%2FAjJ2XGyt5NKAdUAB96i8OEO%2FR%2FG34PK5va6zpYawCVzytmhaGOssD18TQzw%2Bl1hfqh%2FDQf9qgYCzAFRGPDsIzju1QggUSJRF2iahRqkFxeJoy8woYXpp5GnZ425YFqRVn0IwobXYIHI0AiRnJDWMrWLQuutvvD8zTUGwCQCbwnvOOL42D58u32WpDL33hHBugXFpSYUzSdaLxLWqoLfP%2F0%2F%2F9DaMdoW7bZ39B9ZH8l%2F89%2BNRuQry5WBa4t7xyqxQ84hmyJH%2BPLZwBOh%2F85Bk0k7EbVfe%2Bxatyo%2F9bXr%2FVI9CeoUxXCZcnKaLeIdPj8E8MGFkSkYlKteGb3ro4kVcHAuORW%2BhR42izAnBtUh38Y1z3CfNekOqvxpjF%2Fu8slW%2B3HHzuNvsiyQE8nfvYaZfPleHwc48JuC4GWnHrAkatK7z9X%2FkfdIXbpz4cpGVgUMaV8F4r%2B1cXWhi%2F2f5xDLbSs4hpHNHFH3elGHeRutw3pgz78oGSe8CkK6mYhLsNElWOCDCeLPDw%2F1xBGDS%2FpRBBRQwzdGTvQY6pgFL0tbN2JRcNzznl%2B6uJefmrBumlyUvGo6V%2BNFYnuBxwLc4LidYpWEabGxjmy0W0am5r4js5sQBm4er4goHJdcjKVfnXpDQRM1fzIyfYOIZZ07aTM6QvIjCwBlojhM3%2BHSii9P1qrH%2BS6xhqRv%2FudxykB%2FV5jkKr926nNbdAhf69fz4PcVDqUoI2IqClVtN2UgR8eKRYlEJHhvaiEHjZ0CmWW9Cet%2FD&X-Amz-Signature=9b18e6cfb3e5c3226d2b89d31c4fa05dfdefa90904b9b040d1cbed8e088b9f44&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U4GFSXEG%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJGMEQCIDEOapZmLGKAHdV1lVMJQ1tL6rJBSU1GJP7Y9cV7qjz9AiBmTtxUe46W5g4dC2QTFvgu%2FhbhYFiwiZiQPQeNx7uK3ir%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIM5zEBAQb1wWUSOMtCKtwDoLjDpVN%2BUFemhgAyCAXsyCCFmQDFfXy4R9CwGenFhD8w81givBtRUtcDk3BMgxsl7ETRJRCOxN51uOhJl8Wjs5XSnQ0r2GtNQRH%2FAjJ2XGyt5NKAdUAB96i8OEO%2FR%2FG34PK5va6zpYawCVzytmhaGOssD18TQzw%2Bl1hfqh%2FDQf9qgYCzAFRGPDsIzju1QggUSJRF2iahRqkFxeJoy8woYXpp5GnZ425YFqRVn0IwobXYIHI0AiRnJDWMrWLQuutvvD8zTUGwCQCbwnvOOL42D58u32WpDL33hHBugXFpSYUzSdaLxLWqoLfP%2F0%2F%2F9DaMdoW7bZ39B9ZH8l%2F89%2BNRuQry5WBa4t7xyqxQ84hmyJH%2BPLZwBOh%2F85Bk0k7EbVfe%2Bxatyo%2F9bXr%2FVI9CeoUxXCZcnKaLeIdPj8E8MGFkSkYlKteGb3ro4kVcHAuORW%2BhR42izAnBtUh38Y1z3CfNekOqvxpjF%2Fu8slW%2B3HHzuNvsiyQE8nfvYaZfPleHwc48JuC4GWnHrAkatK7z9X%2FkfdIXbpz4cpGVgUMaV8F4r%2B1cXWhi%2F2f5xDLbSs4hpHNHFH3elGHeRutw3pgz78oGSe8CkK6mYhLsNElWOCDCeLPDw%2F1xBGDS%2FpRBBRQwzdGTvQY6pgFL0tbN2JRcNzznl%2B6uJefmrBumlyUvGo6V%2BNFYnuBxwLc4LidYpWEabGxjmy0W0am5r4js5sQBm4er4goHJdcjKVfnXpDQRM1fzIyfYOIZZ07aTM6QvIjCwBlojhM3%2BHSii9P1qrH%2BS6xhqRv%2FudxykB%2FV5jkKr926nNbdAhf69fz4PcVDqUoI2IqClVtN2UgR8eKRYlEJHhvaiEHjZ0CmWW9Cet%2FD&X-Amz-Signature=dd4a3e43f3118e7349ac4f1161f82b56aa3e55297acf9f9a79a9752d489cf6e4&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U4GFSXEG%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJGMEQCIDEOapZmLGKAHdV1lVMJQ1tL6rJBSU1GJP7Y9cV7qjz9AiBmTtxUe46W5g4dC2QTFvgu%2FhbhYFiwiZiQPQeNx7uK3ir%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIM5zEBAQb1wWUSOMtCKtwDoLjDpVN%2BUFemhgAyCAXsyCCFmQDFfXy4R9CwGenFhD8w81givBtRUtcDk3BMgxsl7ETRJRCOxN51uOhJl8Wjs5XSnQ0r2GtNQRH%2FAjJ2XGyt5NKAdUAB96i8OEO%2FR%2FG34PK5va6zpYawCVzytmhaGOssD18TQzw%2Bl1hfqh%2FDQf9qgYCzAFRGPDsIzju1QggUSJRF2iahRqkFxeJoy8woYXpp5GnZ425YFqRVn0IwobXYIHI0AiRnJDWMrWLQuutvvD8zTUGwCQCbwnvOOL42D58u32WpDL33hHBugXFpSYUzSdaLxLWqoLfP%2F0%2F%2F9DaMdoW7bZ39B9ZH8l%2F89%2BNRuQry5WBa4t7xyqxQ84hmyJH%2BPLZwBOh%2F85Bk0k7EbVfe%2Bxatyo%2F9bXr%2FVI9CeoUxXCZcnKaLeIdPj8E8MGFkSkYlKteGb3ro4kVcHAuORW%2BhR42izAnBtUh38Y1z3CfNekOqvxpjF%2Fu8slW%2B3HHzuNvsiyQE8nfvYaZfPleHwc48JuC4GWnHrAkatK7z9X%2FkfdIXbpz4cpGVgUMaV8F4r%2B1cXWhi%2F2f5xDLbSs4hpHNHFH3elGHeRutw3pgz78oGSe8CkK6mYhLsNElWOCDCeLPDw%2F1xBGDS%2FpRBBRQwzdGTvQY6pgFL0tbN2JRcNzznl%2B6uJefmrBumlyUvGo6V%2BNFYnuBxwLc4LidYpWEabGxjmy0W0am5r4js5sQBm4er4goHJdcjKVfnXpDQRM1fzIyfYOIZZ07aTM6QvIjCwBlojhM3%2BHSii9P1qrH%2BS6xhqRv%2FudxykB%2FV5jkKr926nNbdAhf69fz4PcVDqUoI2IqClVtN2UgR8eKRYlEJHhvaiEHjZ0CmWW9Cet%2FD&X-Amz-Signature=682dab4602f5db101d0246242375f9c546d8f8cac31a20e09bb64f59664a8a03&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
