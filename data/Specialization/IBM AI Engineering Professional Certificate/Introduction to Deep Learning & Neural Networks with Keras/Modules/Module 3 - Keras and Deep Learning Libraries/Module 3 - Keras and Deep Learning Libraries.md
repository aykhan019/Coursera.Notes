

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WPLTXSGL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJHMEUCIQCbAhLEdqWtml6XK5XW7RD1qrlnWE58IrjQPk%2FwAYcOGAIgDZCw3fyXrRAc7%2BTorSl4Do0fKc2v%2BBLm9ZORb%2BROvOIqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNDDdZfYYgRedjNDjircA2b3O8ZOJCxmDrEuty0gQaW3k5WiVlsoSWR%2BqWE1IwHLfwKfRqPUsOYw0oYtP0qfeSoW5z7UdGntHpQdokDdmmgHFuSHqBRXN6Sl3nXml6pGVL8IHy6OeTZNIkTihhhjSjfprtHwgb6Fnf55nexZhIDDIyvu399bjGIh1p9mkHQOhPPF8pYvcF6edsV0oqq4iWk%2BG0%2BsJ%2BQZtzRSEisu2lpJ07tU76%2FNHLxo3%2BCNQ6M1NrnPiSRe1s3WSMthG9DqoeCUdqiNTQGGHAij5xuD8o6pbxwcwkUIOFGNa1qdJpzKxDOUyQisGM9aG463AhXdxMoPz%2B17VvDjrMBmuNKPnsBLrui2Prq%2BwgBzFuH5bhUgg%2BHhR7y3qkteUL7t40t5ebstZiLXQDRK0edpQDU2xk2uqD5esIJcLfIGm7v4cXqPfKdba%2BnUE3mg8Z3OWg0EdlP4DFKSnCOEihfNJVDpHBGYlw2D7yVjBMr8NnBxRunJUGxmqCsrv5s5Ii7a4R%2B0KGK1MfI6b4n7CpDZV6FQyyadDc2bc2pzIWusU%2BFPVmbRMcEJRtSLEp802NtPMRVDVQExwuUHAYNR2FLC6L%2FhRuJ6%2BvrZB2Oyt4w%2FciARYeNwLdUGsqWIj4W7yNblMO7n5bwGOqUB33PcwyKqihhW8HFsfj0Ar2c2KAPzM6tpIfsZZx7z1D7Ts9BPAqRgSqL00FLO%2BR2ob5O%2FfiMNueybdc%2FNRWUkYzsXsKJdnvOZrg5B5%2FBn4Td1XcAuHBvp4vG%2FWxhpDkTwFZc4%2B%2FuzKneMK71f8ID4fB2d3kbYnpV1eSq16iqLp0NooKo7f6fC0WjB7O00R%2Bez676QP5m%2B4BtrLObi5oSCYiA%2BEzZR&X-Amz-Signature=51f29549cf229baf885c98435ce760287a6bed3fd1a7b9011424408e740c177a&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WPLTXSGL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJHMEUCIQCbAhLEdqWtml6XK5XW7RD1qrlnWE58IrjQPk%2FwAYcOGAIgDZCw3fyXrRAc7%2BTorSl4Do0fKc2v%2BBLm9ZORb%2BROvOIqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNDDdZfYYgRedjNDjircA2b3O8ZOJCxmDrEuty0gQaW3k5WiVlsoSWR%2BqWE1IwHLfwKfRqPUsOYw0oYtP0qfeSoW5z7UdGntHpQdokDdmmgHFuSHqBRXN6Sl3nXml6pGVL8IHy6OeTZNIkTihhhjSjfprtHwgb6Fnf55nexZhIDDIyvu399bjGIh1p9mkHQOhPPF8pYvcF6edsV0oqq4iWk%2BG0%2BsJ%2BQZtzRSEisu2lpJ07tU76%2FNHLxo3%2BCNQ6M1NrnPiSRe1s3WSMthG9DqoeCUdqiNTQGGHAij5xuD8o6pbxwcwkUIOFGNa1qdJpzKxDOUyQisGM9aG463AhXdxMoPz%2B17VvDjrMBmuNKPnsBLrui2Prq%2BwgBzFuH5bhUgg%2BHhR7y3qkteUL7t40t5ebstZiLXQDRK0edpQDU2xk2uqD5esIJcLfIGm7v4cXqPfKdba%2BnUE3mg8Z3OWg0EdlP4DFKSnCOEihfNJVDpHBGYlw2D7yVjBMr8NnBxRunJUGxmqCsrv5s5Ii7a4R%2B0KGK1MfI6b4n7CpDZV6FQyyadDc2bc2pzIWusU%2BFPVmbRMcEJRtSLEp802NtPMRVDVQExwuUHAYNR2FLC6L%2FhRuJ6%2BvrZB2Oyt4w%2FciARYeNwLdUGsqWIj4W7yNblMO7n5bwGOqUB33PcwyKqihhW8HFsfj0Ar2c2KAPzM6tpIfsZZx7z1D7Ts9BPAqRgSqL00FLO%2BR2ob5O%2FfiMNueybdc%2FNRWUkYzsXsKJdnvOZrg5B5%2FBn4Td1XcAuHBvp4vG%2FWxhpDkTwFZc4%2B%2FuzKneMK71f8ID4fB2d3kbYnpV1eSq16iqLp0NooKo7f6fC0WjB7O00R%2Bez676QP5m%2B4BtrLObi5oSCYiA%2BEzZR&X-Amz-Signature=90dc8d96478c7958f6ea6db9a2c206fba4c8234d056ae8927775929df63a019b&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WPLTXSGL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJHMEUCIQCbAhLEdqWtml6XK5XW7RD1qrlnWE58IrjQPk%2FwAYcOGAIgDZCw3fyXrRAc7%2BTorSl4Do0fKc2v%2BBLm9ZORb%2BROvOIqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNDDdZfYYgRedjNDjircA2b3O8ZOJCxmDrEuty0gQaW3k5WiVlsoSWR%2BqWE1IwHLfwKfRqPUsOYw0oYtP0qfeSoW5z7UdGntHpQdokDdmmgHFuSHqBRXN6Sl3nXml6pGVL8IHy6OeTZNIkTihhhjSjfprtHwgb6Fnf55nexZhIDDIyvu399bjGIh1p9mkHQOhPPF8pYvcF6edsV0oqq4iWk%2BG0%2BsJ%2BQZtzRSEisu2lpJ07tU76%2FNHLxo3%2BCNQ6M1NrnPiSRe1s3WSMthG9DqoeCUdqiNTQGGHAij5xuD8o6pbxwcwkUIOFGNa1qdJpzKxDOUyQisGM9aG463AhXdxMoPz%2B17VvDjrMBmuNKPnsBLrui2Prq%2BwgBzFuH5bhUgg%2BHhR7y3qkteUL7t40t5ebstZiLXQDRK0edpQDU2xk2uqD5esIJcLfIGm7v4cXqPfKdba%2BnUE3mg8Z3OWg0EdlP4DFKSnCOEihfNJVDpHBGYlw2D7yVjBMr8NnBxRunJUGxmqCsrv5s5Ii7a4R%2B0KGK1MfI6b4n7CpDZV6FQyyadDc2bc2pzIWusU%2BFPVmbRMcEJRtSLEp802NtPMRVDVQExwuUHAYNR2FLC6L%2FhRuJ6%2BvrZB2Oyt4w%2FciARYeNwLdUGsqWIj4W7yNblMO7n5bwGOqUB33PcwyKqihhW8HFsfj0Ar2c2KAPzM6tpIfsZZx7z1D7Ts9BPAqRgSqL00FLO%2BR2ob5O%2FfiMNueybdc%2FNRWUkYzsXsKJdnvOZrg5B5%2FBn4Td1XcAuHBvp4vG%2FWxhpDkTwFZc4%2B%2FuzKneMK71f8ID4fB2d3kbYnpV1eSq16iqLp0NooKo7f6fC0WjB7O00R%2Bez676QP5m%2B4BtrLObi5oSCYiA%2BEzZR&X-Amz-Signature=5c0636303dc3bec836341269f6ddd22a9d855325b5c27aa38734d14a7116e0f2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WD4ZDDAF%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010810Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJHMEUCIAQlP21maJV9vFCymEMZsxPXf6g3G9moLwO2qOui40VvAiEA54yAsk1IjT4eBs2sFg1rjUPtpnchesrPRDU3qNKz30kqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGWssWMj70mp%2FNenhyrcA8cWO2HIKjzxodMC1CmG%2F0rS2YZH2YsIwws%2FZZl%2F9zBlHqwvPDBO2o0L5gCxebLjrIBh6xoA7yCPL%2FeNMv4NJvPo5nJt070UTPb2VTYOu%2FLe5OuUfAzkPFb77RZxzw%2FAFZdPCqjZAlqyqhz3opzFOo0M1spT%2BlJZ8ToXg7GtSz8BqhEFV6Qd8vLKo5DcCyi%2BV2q0N8URqmIOLokkcjaLa6uoghH1LOy1BnLHddtfBP31UbIW5pLewAq5qnGvJsK7HvXU%2BDEm4awyKZ9mvapTK4DL%2ByLBvYBbUr7Px0hgjFOkxF4g3KH8i5ZodvXO1kXiBmE01Nk12vbwpWCyidah5uouvzHgiL%2FFnaUeoyjc20yWoYap%2Bqe2N9GF0NMUm4Bl2LISL0lhhuL4VsZ2jAo1EfbCtlNYLUotIiepIwv9y1a4KXGRarKRyIHFUY6rOVX5A0O%2FPBYwBWRqsXbSxSp3EV%2BGODCSY9fUds10RRgEq0Fe0wK8kil%2FPhoV4A%2Bgbe68ojYH%2BJz1nRJtOksk3JEZ46kH8myE1rKOYjGuWii54PirUfCQFBmjgghttpX6A54pCNuQRhgj6G8jxQhcHHohhddR2WSpflV4Kg0wTqlLRV%2B5N0cz4CDtaHDhmBkPMIno5bwGOqUBfh61560K3rb7suWqGCNpFRLtHASUpvYKoStzycXHMbsaq3LPB0W2%2BdiJ4rI%2BPox%2Fm8yiqiDey179ynwzlk0mVT%2Bq5Lr4oJ0OiRoUgghuf4%2F9KJcKhyw%2BoGUhoJ40lG7s6c1KCLDTn4eC3eknU3hotV1NhoFL%2FkXBkYenwEFB8xJD4DpO0y869SkmhoHZ2ghHL5J82m4udEuKW6mpaEt%2FrypnDGwl&X-Amz-Signature=a0754886bb73593fe4dd5b4ccbd063908062a6cd5b4d3da5c841f7a7d7252e4a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WGIMJOB6%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010810Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJGMEQCIFmRV1oZqIrxciU2hNT39Mn7LdmB08HhyxS4E2%2FkupenAiBQDP2OPJPll%2FmYOKZqgzjJ0SP6%2FSGDxVDN8wbU0vA69yqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2BAeLMjY9Dlx4QsncKtwDH7Dxe%2FjbS%2FwNTl%2FULxT4idjmZRTWh2biEg0CNeXrOq%2BV%2BFEMQKVU%2F0NUaLaYlLixLW%2BI0LXZKiyCo4taqyJ5U27%2FpHtki3qFUYM%2BK3LKR6VcdN4n4FES8cXVYwuq4DQXWE2BdIlTTzDrrA648ymu1RA5xli3MrUFdM4P3Zb7c0b6Kr3QhLx1JbaCOLd3RsiE47TZf%2ByqaVupMu%2BZ%2B99epdRf3OQioGwnc%2FYzAwhCH7D52p14TPVOGydMb3ppUq%2F%2FfuEfLiW776YSOZw4LBBUBTcwFO%2BA7yAAyjhzKGPst6jz2bEc6jYWKdrgU2t%2BnO7JTYtSUCLQFxhMevrcOafKk7fBMI270RWwSv%2BVyeZNNXIUvGOhPCwzZU5HsH02ODQOrtBcmtKfNc2F8jcXqqD4ZU64T3bUmNM0Mdroxb8AtQziZb5IukDOeHMaFtJ70v4yta0pAsCnRbrKXV5xpnN3bfMnmWmWqa3xDYTtZss9OlExR7QTVGrKzcMHCmlXbLUMGK%2BnY%2FKlxYrgM63Q1nTXSWqsZA22%2F9Cg27aAQLEgYuTltxWfv5GcI3E7CZmQHwGlDJE4%2FrDxwpD3vlgsGLZKoIX9alltXlWD2gCitQVZA3cUa41ULCerab7oMbcw4uflvAY6pgEqrqHMKF%2FWjZsA0l1AVgUk5iEjdYhU%2Bhoa8ZYYLBeutaZxhL7Mf6qULR8yUPbdgfoT1IQ%2FPD3Ii%2BVNa5EQ%2BacmRSCpqlCwk1lqgZ1d2gJfRyEu3MOvRjjtCwcFVvwc58CP7blYmrKE2NPNYPyIdzDqssHE66FtfLpDAJAZZn0SWG7EOnQUCJlQqxVzAO%2BoOnhkgctnvxkdwmX%2FJ69jVLILRSEcU1Ui&X-Amz-Signature=c81d54216bc86cfc06b6f26a5d829d805ea6d926d7b24fa46c57adaa0502bb00&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WPLTXSGL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJHMEUCIQCbAhLEdqWtml6XK5XW7RD1qrlnWE58IrjQPk%2FwAYcOGAIgDZCw3fyXrRAc7%2BTorSl4Do0fKc2v%2BBLm9ZORb%2BROvOIqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNDDdZfYYgRedjNDjircA2b3O8ZOJCxmDrEuty0gQaW3k5WiVlsoSWR%2BqWE1IwHLfwKfRqPUsOYw0oYtP0qfeSoW5z7UdGntHpQdokDdmmgHFuSHqBRXN6Sl3nXml6pGVL8IHy6OeTZNIkTihhhjSjfprtHwgb6Fnf55nexZhIDDIyvu399bjGIh1p9mkHQOhPPF8pYvcF6edsV0oqq4iWk%2BG0%2BsJ%2BQZtzRSEisu2lpJ07tU76%2FNHLxo3%2BCNQ6M1NrnPiSRe1s3WSMthG9DqoeCUdqiNTQGGHAij5xuD8o6pbxwcwkUIOFGNa1qdJpzKxDOUyQisGM9aG463AhXdxMoPz%2B17VvDjrMBmuNKPnsBLrui2Prq%2BwgBzFuH5bhUgg%2BHhR7y3qkteUL7t40t5ebstZiLXQDRK0edpQDU2xk2uqD5esIJcLfIGm7v4cXqPfKdba%2BnUE3mg8Z3OWg0EdlP4DFKSnCOEihfNJVDpHBGYlw2D7yVjBMr8NnBxRunJUGxmqCsrv5s5Ii7a4R%2B0KGK1MfI6b4n7CpDZV6FQyyadDc2bc2pzIWusU%2BFPVmbRMcEJRtSLEp802NtPMRVDVQExwuUHAYNR2FLC6L%2FhRuJ6%2BvrZB2Oyt4w%2FciARYeNwLdUGsqWIj4W7yNblMO7n5bwGOqUB33PcwyKqihhW8HFsfj0Ar2c2KAPzM6tpIfsZZx7z1D7Ts9BPAqRgSqL00FLO%2BR2ob5O%2FfiMNueybdc%2FNRWUkYzsXsKJdnvOZrg5B5%2FBn4Td1XcAuHBvp4vG%2FWxhpDkTwFZc4%2B%2FuzKneMK71f8ID4fB2d3kbYnpV1eSq16iqLp0NooKo7f6fC0WjB7O00R%2Bez676QP5m%2B4BtrLObi5oSCYiA%2BEzZR&X-Amz-Signature=44afaaae40c56591c57f9571d274261972d8c7cddbaae6a6113df133100bafda&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WPLTXSGL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJHMEUCIQCbAhLEdqWtml6XK5XW7RD1qrlnWE58IrjQPk%2FwAYcOGAIgDZCw3fyXrRAc7%2BTorSl4Do0fKc2v%2BBLm9ZORb%2BROvOIqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNDDdZfYYgRedjNDjircA2b3O8ZOJCxmDrEuty0gQaW3k5WiVlsoSWR%2BqWE1IwHLfwKfRqPUsOYw0oYtP0qfeSoW5z7UdGntHpQdokDdmmgHFuSHqBRXN6Sl3nXml6pGVL8IHy6OeTZNIkTihhhjSjfprtHwgb6Fnf55nexZhIDDIyvu399bjGIh1p9mkHQOhPPF8pYvcF6edsV0oqq4iWk%2BG0%2BsJ%2BQZtzRSEisu2lpJ07tU76%2FNHLxo3%2BCNQ6M1NrnPiSRe1s3WSMthG9DqoeCUdqiNTQGGHAij5xuD8o6pbxwcwkUIOFGNa1qdJpzKxDOUyQisGM9aG463AhXdxMoPz%2B17VvDjrMBmuNKPnsBLrui2Prq%2BwgBzFuH5bhUgg%2BHhR7y3qkteUL7t40t5ebstZiLXQDRK0edpQDU2xk2uqD5esIJcLfIGm7v4cXqPfKdba%2BnUE3mg8Z3OWg0EdlP4DFKSnCOEihfNJVDpHBGYlw2D7yVjBMr8NnBxRunJUGxmqCsrv5s5Ii7a4R%2B0KGK1MfI6b4n7CpDZV6FQyyadDc2bc2pzIWusU%2BFPVmbRMcEJRtSLEp802NtPMRVDVQExwuUHAYNR2FLC6L%2FhRuJ6%2BvrZB2Oyt4w%2FciARYeNwLdUGsqWIj4W7yNblMO7n5bwGOqUB33PcwyKqihhW8HFsfj0Ar2c2KAPzM6tpIfsZZx7z1D7Ts9BPAqRgSqL00FLO%2BR2ob5O%2FfiMNueybdc%2FNRWUkYzsXsKJdnvOZrg5B5%2FBn4Td1XcAuHBvp4vG%2FWxhpDkTwFZc4%2B%2FuzKneMK71f8ID4fB2d3kbYnpV1eSq16iqLp0NooKo7f6fC0WjB7O00R%2Bez676QP5m%2B4BtrLObi5oSCYiA%2BEzZR&X-Amz-Signature=e7019bc35a3051ef511eea94691564bd7705265eef7a9046214f7f2c9e010d74&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WPLTXSGL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJHMEUCIQCbAhLEdqWtml6XK5XW7RD1qrlnWE58IrjQPk%2FwAYcOGAIgDZCw3fyXrRAc7%2BTorSl4Do0fKc2v%2BBLm9ZORb%2BROvOIqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNDDdZfYYgRedjNDjircA2b3O8ZOJCxmDrEuty0gQaW3k5WiVlsoSWR%2BqWE1IwHLfwKfRqPUsOYw0oYtP0qfeSoW5z7UdGntHpQdokDdmmgHFuSHqBRXN6Sl3nXml6pGVL8IHy6OeTZNIkTihhhjSjfprtHwgb6Fnf55nexZhIDDIyvu399bjGIh1p9mkHQOhPPF8pYvcF6edsV0oqq4iWk%2BG0%2BsJ%2BQZtzRSEisu2lpJ07tU76%2FNHLxo3%2BCNQ6M1NrnPiSRe1s3WSMthG9DqoeCUdqiNTQGGHAij5xuD8o6pbxwcwkUIOFGNa1qdJpzKxDOUyQisGM9aG463AhXdxMoPz%2B17VvDjrMBmuNKPnsBLrui2Prq%2BwgBzFuH5bhUgg%2BHhR7y3qkteUL7t40t5ebstZiLXQDRK0edpQDU2xk2uqD5esIJcLfIGm7v4cXqPfKdba%2BnUE3mg8Z3OWg0EdlP4DFKSnCOEihfNJVDpHBGYlw2D7yVjBMr8NnBxRunJUGxmqCsrv5s5Ii7a4R%2B0KGK1MfI6b4n7CpDZV6FQyyadDc2bc2pzIWusU%2BFPVmbRMcEJRtSLEp802NtPMRVDVQExwuUHAYNR2FLC6L%2FhRuJ6%2BvrZB2Oyt4w%2FciARYeNwLdUGsqWIj4W7yNblMO7n5bwGOqUB33PcwyKqihhW8HFsfj0Ar2c2KAPzM6tpIfsZZx7z1D7Ts9BPAqRgSqL00FLO%2BR2ob5O%2FfiMNueybdc%2FNRWUkYzsXsKJdnvOZrg5B5%2FBn4Td1XcAuHBvp4vG%2FWxhpDkTwFZc4%2B%2FuzKneMK71f8ID4fB2d3kbYnpV1eSq16iqLp0NooKo7f6fC0WjB7O00R%2Bez676QP5m%2B4BtrLObi5oSCYiA%2BEzZR&X-Amz-Signature=b2e3b19944867042e523c43dfae6188f03f650a9dfcd0c3fb39f172866961f83&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WPLTXSGL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJHMEUCIQCbAhLEdqWtml6XK5XW7RD1qrlnWE58IrjQPk%2FwAYcOGAIgDZCw3fyXrRAc7%2BTorSl4Do0fKc2v%2BBLm9ZORb%2BROvOIqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNDDdZfYYgRedjNDjircA2b3O8ZOJCxmDrEuty0gQaW3k5WiVlsoSWR%2BqWE1IwHLfwKfRqPUsOYw0oYtP0qfeSoW5z7UdGntHpQdokDdmmgHFuSHqBRXN6Sl3nXml6pGVL8IHy6OeTZNIkTihhhjSjfprtHwgb6Fnf55nexZhIDDIyvu399bjGIh1p9mkHQOhPPF8pYvcF6edsV0oqq4iWk%2BG0%2BsJ%2BQZtzRSEisu2lpJ07tU76%2FNHLxo3%2BCNQ6M1NrnPiSRe1s3WSMthG9DqoeCUdqiNTQGGHAij5xuD8o6pbxwcwkUIOFGNa1qdJpzKxDOUyQisGM9aG463AhXdxMoPz%2B17VvDjrMBmuNKPnsBLrui2Prq%2BwgBzFuH5bhUgg%2BHhR7y3qkteUL7t40t5ebstZiLXQDRK0edpQDU2xk2uqD5esIJcLfIGm7v4cXqPfKdba%2BnUE3mg8Z3OWg0EdlP4DFKSnCOEihfNJVDpHBGYlw2D7yVjBMr8NnBxRunJUGxmqCsrv5s5Ii7a4R%2B0KGK1MfI6b4n7CpDZV6FQyyadDc2bc2pzIWusU%2BFPVmbRMcEJRtSLEp802NtPMRVDVQExwuUHAYNR2FLC6L%2FhRuJ6%2BvrZB2Oyt4w%2FciARYeNwLdUGsqWIj4W7yNblMO7n5bwGOqUB33PcwyKqihhW8HFsfj0Ar2c2KAPzM6tpIfsZZx7z1D7Ts9BPAqRgSqL00FLO%2BR2ob5O%2FfiMNueybdc%2FNRWUkYzsXsKJdnvOZrg5B5%2FBn4Td1XcAuHBvp4vG%2FWxhpDkTwFZc4%2B%2FuzKneMK71f8ID4fB2d3kbYnpV1eSq16iqLp0NooKo7f6fC0WjB7O00R%2Bez676QP5m%2B4BtrLObi5oSCYiA%2BEzZR&X-Amz-Signature=23e4aa0fd0d94559d123c3ffdb8b21fac2c90db7fed54bbf9bec3c1bbd30d547&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
