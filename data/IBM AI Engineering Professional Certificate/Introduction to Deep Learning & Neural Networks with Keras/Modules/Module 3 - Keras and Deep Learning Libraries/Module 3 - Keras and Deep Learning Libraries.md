

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZX7KKYY%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCIC1UdtXA9zPBiJv8SnOsa6l88rtbm%2BWJpjJDLnnpIUnaAiAVE8HM9bSXvENB3ohQGDff%2F5Zmf2F3F4S%2FD3fbdZLdLyr%2FAwgxEAAaDDYzNzQyMzE4MzgwNSIMsw7DoeszkvY7qLrcKtwDIV8%2B3%2F9zHwxiJy2F5%2FynEzqo0cqhsd%2BJecdQ7323Uui%2B4W5NT46MnBwNHtPo6axLwZvwLxNu44pCkbPOOfckfHQPtdfdhEtGjSB1F9TeCl%2BIIpvgwnt5OHHcW%2FtGWNlXmZfpUSu7b8VCb081cIezoZcU4XgjJzSQDGIkDEHTR82CTcTCsuMPNURbsBfR1j15M%2FL3poQIcbJ6aeMwW0tpU%2FXYp7VJKnlRUfu9YBFTGtjk5uWkK7bMyzu9jxhDsy6JiOPXjB%2BxWhi6uD6%2BhK9B8KPOjGV6d%2Bk7wnWi9aMqmxdehl1REphfbiN5CHKIqet3%2BAIAEfM52v0Im7Zp9r5jX71gGyWembOIqUe7qk8jzSjfP5h%2F7mGjFDZzkMPArEkIKWd%2Buu5dUWmMCTyFsdeC8TNlBkh7Lp8qi1ziRYTUCBNjNUIQeOyhiOs3GPsR1JJ6x8j63tHMt6vMIT1A0M3CQQj8kRr1UOr79MrRE9PTwhFGskrTdNryiCf%2BtvWqNIDvbkHmrzba926kIznmXyAvS5EV3pv53ACAA8kD%2BXWD3Y31ISGeYe3QsecYJh8h7eKuAkqz0GKVr5qNbMsur3JmWm6qm1z92pQPwT6uqR%2BckVBqt9mUjyMRALdB%2BnYwr%2BiIvQY6pgGtDpOdQLFBRVzR70sNGuOw0wGi73ZFmCHmQ47ZDeKQl5S4tLeiQTneRqS%2FONND6F%2F8%2FAGEiRBLqewMsug%2FHMwf8iakBYNYWtF3csC%2F%2FNr%2Fy0sviOIfdkx2E5nuf9QVndD%2B61eBN0eNrGQwLz2MaFhtLqOOFw34YdOuEKwOGH7OxZVJSbAMelxXGnFuR1jhAi579v%2BPuvUqSKxXMitoXQD0kUA%2FTl%2Bs&X-Amz-Signature=cf7d0d28b92fc7c5ebccb61b2d0d8008421ba4a965759bcd02cc291c46b3434b&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZX7KKYY%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCIC1UdtXA9zPBiJv8SnOsa6l88rtbm%2BWJpjJDLnnpIUnaAiAVE8HM9bSXvENB3ohQGDff%2F5Zmf2F3F4S%2FD3fbdZLdLyr%2FAwgxEAAaDDYzNzQyMzE4MzgwNSIMsw7DoeszkvY7qLrcKtwDIV8%2B3%2F9zHwxiJy2F5%2FynEzqo0cqhsd%2BJecdQ7323Uui%2B4W5NT46MnBwNHtPo6axLwZvwLxNu44pCkbPOOfckfHQPtdfdhEtGjSB1F9TeCl%2BIIpvgwnt5OHHcW%2FtGWNlXmZfpUSu7b8VCb081cIezoZcU4XgjJzSQDGIkDEHTR82CTcTCsuMPNURbsBfR1j15M%2FL3poQIcbJ6aeMwW0tpU%2FXYp7VJKnlRUfu9YBFTGtjk5uWkK7bMyzu9jxhDsy6JiOPXjB%2BxWhi6uD6%2BhK9B8KPOjGV6d%2Bk7wnWi9aMqmxdehl1REphfbiN5CHKIqet3%2BAIAEfM52v0Im7Zp9r5jX71gGyWembOIqUe7qk8jzSjfP5h%2F7mGjFDZzkMPArEkIKWd%2Buu5dUWmMCTyFsdeC8TNlBkh7Lp8qi1ziRYTUCBNjNUIQeOyhiOs3GPsR1JJ6x8j63tHMt6vMIT1A0M3CQQj8kRr1UOr79MrRE9PTwhFGskrTdNryiCf%2BtvWqNIDvbkHmrzba926kIznmXyAvS5EV3pv53ACAA8kD%2BXWD3Y31ISGeYe3QsecYJh8h7eKuAkqz0GKVr5qNbMsur3JmWm6qm1z92pQPwT6uqR%2BckVBqt9mUjyMRALdB%2BnYwr%2BiIvQY6pgGtDpOdQLFBRVzR70sNGuOw0wGi73ZFmCHmQ47ZDeKQl5S4tLeiQTneRqS%2FONND6F%2F8%2FAGEiRBLqewMsug%2FHMwf8iakBYNYWtF3csC%2F%2FNr%2Fy0sviOIfdkx2E5nuf9QVndD%2B61eBN0eNrGQwLz2MaFhtLqOOFw34YdOuEKwOGH7OxZVJSbAMelxXGnFuR1jhAi579v%2BPuvUqSKxXMitoXQD0kUA%2FTl%2Bs&X-Amz-Signature=78579a4d88e753a2e1edaf0add7ff243ac6f044973a93e5fd3e250e38698e898&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZX7KKYY%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCIC1UdtXA9zPBiJv8SnOsa6l88rtbm%2BWJpjJDLnnpIUnaAiAVE8HM9bSXvENB3ohQGDff%2F5Zmf2F3F4S%2FD3fbdZLdLyr%2FAwgxEAAaDDYzNzQyMzE4MzgwNSIMsw7DoeszkvY7qLrcKtwDIV8%2B3%2F9zHwxiJy2F5%2FynEzqo0cqhsd%2BJecdQ7323Uui%2B4W5NT46MnBwNHtPo6axLwZvwLxNu44pCkbPOOfckfHQPtdfdhEtGjSB1F9TeCl%2BIIpvgwnt5OHHcW%2FtGWNlXmZfpUSu7b8VCb081cIezoZcU4XgjJzSQDGIkDEHTR82CTcTCsuMPNURbsBfR1j15M%2FL3poQIcbJ6aeMwW0tpU%2FXYp7VJKnlRUfu9YBFTGtjk5uWkK7bMyzu9jxhDsy6JiOPXjB%2BxWhi6uD6%2BhK9B8KPOjGV6d%2Bk7wnWi9aMqmxdehl1REphfbiN5CHKIqet3%2BAIAEfM52v0Im7Zp9r5jX71gGyWembOIqUe7qk8jzSjfP5h%2F7mGjFDZzkMPArEkIKWd%2Buu5dUWmMCTyFsdeC8TNlBkh7Lp8qi1ziRYTUCBNjNUIQeOyhiOs3GPsR1JJ6x8j63tHMt6vMIT1A0M3CQQj8kRr1UOr79MrRE9PTwhFGskrTdNryiCf%2BtvWqNIDvbkHmrzba926kIznmXyAvS5EV3pv53ACAA8kD%2BXWD3Y31ISGeYe3QsecYJh8h7eKuAkqz0GKVr5qNbMsur3JmWm6qm1z92pQPwT6uqR%2BckVBqt9mUjyMRALdB%2BnYwr%2BiIvQY6pgGtDpOdQLFBRVzR70sNGuOw0wGi73ZFmCHmQ47ZDeKQl5S4tLeiQTneRqS%2FONND6F%2F8%2FAGEiRBLqewMsug%2FHMwf8iakBYNYWtF3csC%2F%2FNr%2Fy0sviOIfdkx2E5nuf9QVndD%2B61eBN0eNrGQwLz2MaFhtLqOOFw34YdOuEKwOGH7OxZVJSbAMelxXGnFuR1jhAi579v%2BPuvUqSKxXMitoXQD0kUA%2FTl%2Bs&X-Amz-Signature=a48296eebb43b266efe167fe8e0dbbd837e7d3cc134693076ec6e39797f6e9d0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WUQP6HPM%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCIHldHw4dqynTgVwcR4E4eGTsuaQwbUJi9hu3QoburMP6AiASQQOodgUF2riGEnJx2BBxIk1vjgZF8189mobAXVY3aCr%2FAwgxEAAaDDYzNzQyMzE4MzgwNSIMvsZSDI1EsE7jYIT%2FKtwDELCgXOtKMpZY6O8cn3u7XXBEjQnHxtR54R1ONUoLcfY6II%2BcEEshBea7lnYVXH5tESEWtVnMnDxSAk14jVKsEaZc0T%2Fb36UMyW2JiDRJqSGhSZB%2FuGzZMdvQdEZWJnoa%2FEcCJJKeqiLyyiGhTaWnwYplvWbWx3baCC%2BDY8LOZ0%2F9fGuHx6ZJlQSCJSdfl88wi3%2BfuLQuKpKo%2BvxwMS70SeKF8YbJcEwShgNazF1%2BZLON4GVg8IzQjgeId0EddezBVAVAU12H7uXUMDMADDgtXyXdgSlOo88nN16AGJbD8aR5OAfWEs30cL9UontTLzQCHJwyMMbQL2CqPeNnhNSgh0IHtjx9sHyoOwzZHWpVvweC2CFeTU9hy3sqT%2FG%2BL2OdE1CQuqyQehR%2Bkzek7LsR3LzCHeaeqF8PaO80Yob9cjF3g7ACfvp7LNv5aZX5JxsH1qfHtd6p23BkB3xS7vwhtjsiUhGO%2BOnM4u9N0dyGNjFSYrcZiZvWnNuZ2C8puEfARvMWtymqxO4hZijtw6JQO9Xn63f5eTeorJsJsAsUeNvwfiE00AaiLbtEKg72PrDbLzQ4eUF%2BQjuZeeuWvKmrfYOzUUH3tpE9iH5m%2BMqrpon%2B6BHfSg2RE2kksuow2OaIvQY6pgHIlmWV2WjasftRT3j%2B%2BChJ1MPNZommNGqoh%2Fv8m%2BmYgBrvN6GBpwlAJaX4peLuyz5nbdTfN3%2BdY6YDkTFiTMv4ft5YBCKuMQXJD3tCZPk5GbiyFN0a5horI4jvgnVdE0km2hqb%2BayRaYLjMgoMF5WGVetJ2scRpatA1LcnSi28TVjlVN6H%2FRVrDMFtQeF%2BgJANMtvtPCsgKeMCw1%2BoWHlfVja5A7Zv&X-Amz-Signature=e1e81610927584ef9107bc9f88dc92e581c0ba811e799fcb3323b48830bd3562&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W2OPWIRP%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIQCi3S2e8zAbDmv7WhNS4o7c3F0vqIw4rJXuJ3Dv1QiQWQIgD%2FMAH4As%2FaVQV6vg3VDdUpJ7N2GWIRMvxCWwajvgfL0q%2FwMIMRAAGgw2Mzc0MjMxODM4MDUiDCJ5C0i%2Bn%2F1hlkzhHircA4CVUGZSNO%2BM0VdjwXgWu%2BBaSswnVsz0uEqg5CyYESnUKe0gbZXRrJy944fXvuyyPNjAdd6njCY1uwW13MEBOgclFEvJCCimV1dOshcMZks%2FCQyxaTj1DCG2PPSNDc%2B%2FU2gQwIRhN6FTVUbVPOf98KYeovhjdruDczmTRu%2ByV06JhdJZAH8UbZVQ30wVZdP9IrCErZbmaoAe8HxzGQnLaUIrYNXCpzhFjAtTgJfzDod%2FI0nlUIsba16AYT74lsCsOapv0qj16Tx%2FdN6gRmUsKaPJ8PIwquwiwg%2Brhty68cxCnmG61foG%2FlV31e%2Bu8H1%2F7lwSw9Z%2FkXD%2FZTOay9fRT7fQ93URWiS4fGCUJ2xzRI0ZH7%2BAIUpL9eKoNYXpLx5DiT5e%2F6PjSetbZo6UHpJ6OqDfhZBAss4CpGM9hFqY7aU4%2BjgWHYRh1yuAc5LQkbbAzjc%2FkXH%2F8y89Y%2Fa4t%2FhjsWeFPb0wpcWcs0q%2FWfUlTILQjJZVejzW669f7S00UrJOfhE8s4G%2B6FfQck9za%2Fk%2B534nHt2nZ2tEsC9P6smCqcARn3RcGiMZCDZ8%2B1q%2BQ5L3lW85p%2F8wybFk%2BwuzFDSBJo2fNsLJvUyz7QVp7l9LiFpVo2EJSUCE0E7echIaMPfmiL0GOqUBpWi2Q4462YgVMSB3qpidUPJleFZPdYivEo46cvCf0u%2FDtRDfX%2BhC5BhTzpAF92S0eS6ERJwaOU4%2FjxCwUS8tzUoWkn63mSWvRt3KfmtHOQW%2BH%2Br%2FEa3VqceDJxgO8GvTWtKHmvmQwaacGpvAS1wt4jWvt2YHJF4%2B5JHUWDdo3p0K0cDemR5SbD7vZlxX1oMG%2FnHFTMRGaSP7fcUNBAdoKDCTxcWT&X-Amz-Signature=9b6637f6ba84af7351b3b3c763bed28f8a1d9574f55189236dcf2065a06c21dd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZX7KKYY%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCIC1UdtXA9zPBiJv8SnOsa6l88rtbm%2BWJpjJDLnnpIUnaAiAVE8HM9bSXvENB3ohQGDff%2F5Zmf2F3F4S%2FD3fbdZLdLyr%2FAwgxEAAaDDYzNzQyMzE4MzgwNSIMsw7DoeszkvY7qLrcKtwDIV8%2B3%2F9zHwxiJy2F5%2FynEzqo0cqhsd%2BJecdQ7323Uui%2B4W5NT46MnBwNHtPo6axLwZvwLxNu44pCkbPOOfckfHQPtdfdhEtGjSB1F9TeCl%2BIIpvgwnt5OHHcW%2FtGWNlXmZfpUSu7b8VCb081cIezoZcU4XgjJzSQDGIkDEHTR82CTcTCsuMPNURbsBfR1j15M%2FL3poQIcbJ6aeMwW0tpU%2FXYp7VJKnlRUfu9YBFTGtjk5uWkK7bMyzu9jxhDsy6JiOPXjB%2BxWhi6uD6%2BhK9B8KPOjGV6d%2Bk7wnWi9aMqmxdehl1REphfbiN5CHKIqet3%2BAIAEfM52v0Im7Zp9r5jX71gGyWembOIqUe7qk8jzSjfP5h%2F7mGjFDZzkMPArEkIKWd%2Buu5dUWmMCTyFsdeC8TNlBkh7Lp8qi1ziRYTUCBNjNUIQeOyhiOs3GPsR1JJ6x8j63tHMt6vMIT1A0M3CQQj8kRr1UOr79MrRE9PTwhFGskrTdNryiCf%2BtvWqNIDvbkHmrzba926kIznmXyAvS5EV3pv53ACAA8kD%2BXWD3Y31ISGeYe3QsecYJh8h7eKuAkqz0GKVr5qNbMsur3JmWm6qm1z92pQPwT6uqR%2BckVBqt9mUjyMRALdB%2BnYwr%2BiIvQY6pgGtDpOdQLFBRVzR70sNGuOw0wGi73ZFmCHmQ47ZDeKQl5S4tLeiQTneRqS%2FONND6F%2F8%2FAGEiRBLqewMsug%2FHMwf8iakBYNYWtF3csC%2F%2FNr%2Fy0sviOIfdkx2E5nuf9QVndD%2B61eBN0eNrGQwLz2MaFhtLqOOFw34YdOuEKwOGH7OxZVJSbAMelxXGnFuR1jhAi579v%2BPuvUqSKxXMitoXQD0kUA%2FTl%2Bs&X-Amz-Signature=e717e3af68b69b4f035853c97e661e0d97ac4ea825484900abeeecfcc90a82ef&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZX7KKYY%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCIC1UdtXA9zPBiJv8SnOsa6l88rtbm%2BWJpjJDLnnpIUnaAiAVE8HM9bSXvENB3ohQGDff%2F5Zmf2F3F4S%2FD3fbdZLdLyr%2FAwgxEAAaDDYzNzQyMzE4MzgwNSIMsw7DoeszkvY7qLrcKtwDIV8%2B3%2F9zHwxiJy2F5%2FynEzqo0cqhsd%2BJecdQ7323Uui%2B4W5NT46MnBwNHtPo6axLwZvwLxNu44pCkbPOOfckfHQPtdfdhEtGjSB1F9TeCl%2BIIpvgwnt5OHHcW%2FtGWNlXmZfpUSu7b8VCb081cIezoZcU4XgjJzSQDGIkDEHTR82CTcTCsuMPNURbsBfR1j15M%2FL3poQIcbJ6aeMwW0tpU%2FXYp7VJKnlRUfu9YBFTGtjk5uWkK7bMyzu9jxhDsy6JiOPXjB%2BxWhi6uD6%2BhK9B8KPOjGV6d%2Bk7wnWi9aMqmxdehl1REphfbiN5CHKIqet3%2BAIAEfM52v0Im7Zp9r5jX71gGyWembOIqUe7qk8jzSjfP5h%2F7mGjFDZzkMPArEkIKWd%2Buu5dUWmMCTyFsdeC8TNlBkh7Lp8qi1ziRYTUCBNjNUIQeOyhiOs3GPsR1JJ6x8j63tHMt6vMIT1A0M3CQQj8kRr1UOr79MrRE9PTwhFGskrTdNryiCf%2BtvWqNIDvbkHmrzba926kIznmXyAvS5EV3pv53ACAA8kD%2BXWD3Y31ISGeYe3QsecYJh8h7eKuAkqz0GKVr5qNbMsur3JmWm6qm1z92pQPwT6uqR%2BckVBqt9mUjyMRALdB%2BnYwr%2BiIvQY6pgGtDpOdQLFBRVzR70sNGuOw0wGi73ZFmCHmQ47ZDeKQl5S4tLeiQTneRqS%2FONND6F%2F8%2FAGEiRBLqewMsug%2FHMwf8iakBYNYWtF3csC%2F%2FNr%2Fy0sviOIfdkx2E5nuf9QVndD%2B61eBN0eNrGQwLz2MaFhtLqOOFw34YdOuEKwOGH7OxZVJSbAMelxXGnFuR1jhAi579v%2BPuvUqSKxXMitoXQD0kUA%2FTl%2Bs&X-Amz-Signature=51a7b63eb56b37264671b1b48933ab280f6094fd28aa04962fde185336dc87ff&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZX7KKYY%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCIC1UdtXA9zPBiJv8SnOsa6l88rtbm%2BWJpjJDLnnpIUnaAiAVE8HM9bSXvENB3ohQGDff%2F5Zmf2F3F4S%2FD3fbdZLdLyr%2FAwgxEAAaDDYzNzQyMzE4MzgwNSIMsw7DoeszkvY7qLrcKtwDIV8%2B3%2F9zHwxiJy2F5%2FynEzqo0cqhsd%2BJecdQ7323Uui%2B4W5NT46MnBwNHtPo6axLwZvwLxNu44pCkbPOOfckfHQPtdfdhEtGjSB1F9TeCl%2BIIpvgwnt5OHHcW%2FtGWNlXmZfpUSu7b8VCb081cIezoZcU4XgjJzSQDGIkDEHTR82CTcTCsuMPNURbsBfR1j15M%2FL3poQIcbJ6aeMwW0tpU%2FXYp7VJKnlRUfu9YBFTGtjk5uWkK7bMyzu9jxhDsy6JiOPXjB%2BxWhi6uD6%2BhK9B8KPOjGV6d%2Bk7wnWi9aMqmxdehl1REphfbiN5CHKIqet3%2BAIAEfM52v0Im7Zp9r5jX71gGyWembOIqUe7qk8jzSjfP5h%2F7mGjFDZzkMPArEkIKWd%2Buu5dUWmMCTyFsdeC8TNlBkh7Lp8qi1ziRYTUCBNjNUIQeOyhiOs3GPsR1JJ6x8j63tHMt6vMIT1A0M3CQQj8kRr1UOr79MrRE9PTwhFGskrTdNryiCf%2BtvWqNIDvbkHmrzba926kIznmXyAvS5EV3pv53ACAA8kD%2BXWD3Y31ISGeYe3QsecYJh8h7eKuAkqz0GKVr5qNbMsur3JmWm6qm1z92pQPwT6uqR%2BckVBqt9mUjyMRALdB%2BnYwr%2BiIvQY6pgGtDpOdQLFBRVzR70sNGuOw0wGi73ZFmCHmQ47ZDeKQl5S4tLeiQTneRqS%2FONND6F%2F8%2FAGEiRBLqewMsug%2FHMwf8iakBYNYWtF3csC%2F%2FNr%2Fy0sviOIfdkx2E5nuf9QVndD%2B61eBN0eNrGQwLz2MaFhtLqOOFw34YdOuEKwOGH7OxZVJSbAMelxXGnFuR1jhAi579v%2BPuvUqSKxXMitoXQD0kUA%2FTl%2Bs&X-Amz-Signature=9743aca03a1e477f4069b6b092ba2a00b908b806fdadf22c1206c61726dc961b&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZX7KKYY%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCIC1UdtXA9zPBiJv8SnOsa6l88rtbm%2BWJpjJDLnnpIUnaAiAVE8HM9bSXvENB3ohQGDff%2F5Zmf2F3F4S%2FD3fbdZLdLyr%2FAwgxEAAaDDYzNzQyMzE4MzgwNSIMsw7DoeszkvY7qLrcKtwDIV8%2B3%2F9zHwxiJy2F5%2FynEzqo0cqhsd%2BJecdQ7323Uui%2B4W5NT46MnBwNHtPo6axLwZvwLxNu44pCkbPOOfckfHQPtdfdhEtGjSB1F9TeCl%2BIIpvgwnt5OHHcW%2FtGWNlXmZfpUSu7b8VCb081cIezoZcU4XgjJzSQDGIkDEHTR82CTcTCsuMPNURbsBfR1j15M%2FL3poQIcbJ6aeMwW0tpU%2FXYp7VJKnlRUfu9YBFTGtjk5uWkK7bMyzu9jxhDsy6JiOPXjB%2BxWhi6uD6%2BhK9B8KPOjGV6d%2Bk7wnWi9aMqmxdehl1REphfbiN5CHKIqet3%2BAIAEfM52v0Im7Zp9r5jX71gGyWembOIqUe7qk8jzSjfP5h%2F7mGjFDZzkMPArEkIKWd%2Buu5dUWmMCTyFsdeC8TNlBkh7Lp8qi1ziRYTUCBNjNUIQeOyhiOs3GPsR1JJ6x8j63tHMt6vMIT1A0M3CQQj8kRr1UOr79MrRE9PTwhFGskrTdNryiCf%2BtvWqNIDvbkHmrzba926kIznmXyAvS5EV3pv53ACAA8kD%2BXWD3Y31ISGeYe3QsecYJh8h7eKuAkqz0GKVr5qNbMsur3JmWm6qm1z92pQPwT6uqR%2BckVBqt9mUjyMRALdB%2BnYwr%2BiIvQY6pgGtDpOdQLFBRVzR70sNGuOw0wGi73ZFmCHmQ47ZDeKQl5S4tLeiQTneRqS%2FONND6F%2F8%2FAGEiRBLqewMsug%2FHMwf8iakBYNYWtF3csC%2F%2FNr%2Fy0sviOIfdkx2E5nuf9QVndD%2B61eBN0eNrGQwLz2MaFhtLqOOFw34YdOuEKwOGH7OxZVJSbAMelxXGnFuR1jhAi579v%2BPuvUqSKxXMitoXQD0kUA%2FTl%2Bs&X-Amz-Signature=f0c8977f2af79cca4fcd588ceb103f06ca78276a0f0ba70529d62303b8f19e05&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
