

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QFLXYHMI%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH4aCXVzLXdlc3QtMiJIMEYCIQCLOMwNf6mRtpVCIz7OZehgqH5q%2Ft5diwaU8at5Jg7zwgIhAPzRV7gKDHleX4ORtk9woUK4KIKTdcjdl3KjWkcExsBuKogECIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy1PaBWIKAQBPEDzXkq3AOZ0zAWXpQAwpFo5FVFdMst5Xny8hc5Yp2ad3kawdY%2BkG66dd90jIpP0cDlHrMoA%2BoHRgU%2B6HUVQ%2FJbG7C7xSvjDov%2FeEZ9Vokc4qudhaAeMKxQN3X5RQjWvgN%2FSZyFeEuxEPa7TmCiMSqmHgQdz4YJOQxKkDiekMnbJrV2i%2FtoZrLmI2JNV2HBWZUuGYBG6us%2Bd11%2BM3fOt2y00LYcpYFUq6pqYrUm2%2BqaxcTNlO3M5%2BaiycDalu0%2FFakSD9WwgnZc32tEWDzNUDuBgtQ%2F%2FvMNHwR%2FB0eWCkp%2FCJ2%2Frb80bsvwya9pmwuw%2B%2BFwtS9JLswN7537xb%2FCSeJ443r6L2gp50s%2BtK8MLGIXS%2BmqGgl7wJ%2FlF1rMUNQbVYAkf8Fjf9rx0qxGSztAw%2BOt2L%2B32qOIqO6V%2B7hKlGzZNqsTorm33sC5tqp8C8WJDt2asRTLIrbrQD0CFkzEtsH5Q2Pb%2BTK0HxOyIihgkfqmuZmHJvRBmRtxumdQZEjr9FA%2FZC3Km42K56%2Bp4czxKygbyFAbhnAmvyXIRAg%2BZ0fQ0sA1zVrqkFSI3exoXfC%2BUbUpx7POjfine%2F%2BoFkoDBIYFnKkLh9X9pZ4vd%2BEwpv1%2Fq691dQoBU9EQd0uaruSmN1ETAjD9j%2Be8BjqkAWQd1kmBE4G5HqW05ehxYl3SsuUz7eTRyPkO652hGk4ebdwVh17IfK16TZOgU5igpYtKMJupVenRxMoIh1YqQFSYS4Yu%2FAfUTYTSGRdGY%2BKFkly%2FKW3DoNbVguS8v3Tjb8LIIah2Ji18Aph75DvaqIZsfHSpvwkD6h7hGeKlByf8T%2BFuseWhlV0iCTajljqZL6kWA7%2F9ecURZ88dp9zOPhiwPdKy&X-Amz-Signature=5acfdbe95cbd977cd9437be967163f3dc76dc404ca5b4a6593035c43aa5293ff&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QFLXYHMI%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062011Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH4aCXVzLXdlc3QtMiJIMEYCIQCLOMwNf6mRtpVCIz7OZehgqH5q%2Ft5diwaU8at5Jg7zwgIhAPzRV7gKDHleX4ORtk9woUK4KIKTdcjdl3KjWkcExsBuKogECIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy1PaBWIKAQBPEDzXkq3AOZ0zAWXpQAwpFo5FVFdMst5Xny8hc5Yp2ad3kawdY%2BkG66dd90jIpP0cDlHrMoA%2BoHRgU%2B6HUVQ%2FJbG7C7xSvjDov%2FeEZ9Vokc4qudhaAeMKxQN3X5RQjWvgN%2FSZyFeEuxEPa7TmCiMSqmHgQdz4YJOQxKkDiekMnbJrV2i%2FtoZrLmI2JNV2HBWZUuGYBG6us%2Bd11%2BM3fOt2y00LYcpYFUq6pqYrUm2%2BqaxcTNlO3M5%2BaiycDalu0%2FFakSD9WwgnZc32tEWDzNUDuBgtQ%2F%2FvMNHwR%2FB0eWCkp%2FCJ2%2Frb80bsvwya9pmwuw%2B%2BFwtS9JLswN7537xb%2FCSeJ443r6L2gp50s%2BtK8MLGIXS%2BmqGgl7wJ%2FlF1rMUNQbVYAkf8Fjf9rx0qxGSztAw%2BOt2L%2B32qOIqO6V%2B7hKlGzZNqsTorm33sC5tqp8C8WJDt2asRTLIrbrQD0CFkzEtsH5Q2Pb%2BTK0HxOyIihgkfqmuZmHJvRBmRtxumdQZEjr9FA%2FZC3Km42K56%2Bp4czxKygbyFAbhnAmvyXIRAg%2BZ0fQ0sA1zVrqkFSI3exoXfC%2BUbUpx7POjfine%2F%2BoFkoDBIYFnKkLh9X9pZ4vd%2BEwpv1%2Fq691dQoBU9EQd0uaruSmN1ETAjD9j%2Be8BjqkAWQd1kmBE4G5HqW05ehxYl3SsuUz7eTRyPkO652hGk4ebdwVh17IfK16TZOgU5igpYtKMJupVenRxMoIh1YqQFSYS4Yu%2FAfUTYTSGRdGY%2BKFkly%2FKW3DoNbVguS8v3Tjb8LIIah2Ji18Aph75DvaqIZsfHSpvwkD6h7hGeKlByf8T%2BFuseWhlV0iCTajljqZL6kWA7%2F9ecURZ88dp9zOPhiwPdKy&X-Amz-Signature=fce32406e45bc82deb7fe50f7ee82abb186528fbf4428f6ffd147fa1b6054e69&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QFLXYHMI%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062011Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH4aCXVzLXdlc3QtMiJIMEYCIQCLOMwNf6mRtpVCIz7OZehgqH5q%2Ft5diwaU8at5Jg7zwgIhAPzRV7gKDHleX4ORtk9woUK4KIKTdcjdl3KjWkcExsBuKogECIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy1PaBWIKAQBPEDzXkq3AOZ0zAWXpQAwpFo5FVFdMst5Xny8hc5Yp2ad3kawdY%2BkG66dd90jIpP0cDlHrMoA%2BoHRgU%2B6HUVQ%2FJbG7C7xSvjDov%2FeEZ9Vokc4qudhaAeMKxQN3X5RQjWvgN%2FSZyFeEuxEPa7TmCiMSqmHgQdz4YJOQxKkDiekMnbJrV2i%2FtoZrLmI2JNV2HBWZUuGYBG6us%2Bd11%2BM3fOt2y00LYcpYFUq6pqYrUm2%2BqaxcTNlO3M5%2BaiycDalu0%2FFakSD9WwgnZc32tEWDzNUDuBgtQ%2F%2FvMNHwR%2FB0eWCkp%2FCJ2%2Frb80bsvwya9pmwuw%2B%2BFwtS9JLswN7537xb%2FCSeJ443r6L2gp50s%2BtK8MLGIXS%2BmqGgl7wJ%2FlF1rMUNQbVYAkf8Fjf9rx0qxGSztAw%2BOt2L%2B32qOIqO6V%2B7hKlGzZNqsTorm33sC5tqp8C8WJDt2asRTLIrbrQD0CFkzEtsH5Q2Pb%2BTK0HxOyIihgkfqmuZmHJvRBmRtxumdQZEjr9FA%2FZC3Km42K56%2Bp4czxKygbyFAbhnAmvyXIRAg%2BZ0fQ0sA1zVrqkFSI3exoXfC%2BUbUpx7POjfine%2F%2BoFkoDBIYFnKkLh9X9pZ4vd%2BEwpv1%2Fq691dQoBU9EQd0uaruSmN1ETAjD9j%2Be8BjqkAWQd1kmBE4G5HqW05ehxYl3SsuUz7eTRyPkO652hGk4ebdwVh17IfK16TZOgU5igpYtKMJupVenRxMoIh1YqQFSYS4Yu%2FAfUTYTSGRdGY%2BKFkly%2FKW3DoNbVguS8v3Tjb8LIIah2Ji18Aph75DvaqIZsfHSpvwkD6h7hGeKlByf8T%2BFuseWhlV0iCTajljqZL6kWA7%2F9ecURZ88dp9zOPhiwPdKy&X-Amz-Signature=b8ec79ce30d926f7abc25c6ce7c71f3ad8b554e91dec6cab8d2ccfcbba360ead&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663SN4YX5W%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQDj8Uw4Il35rvwzhqy%2FnpyTAZ2%2FnGjrFstEgaLPXuhAzQIgXc2GF56XGw6QJku%2Fj6WRYX3VL%2BQGU7Rm8%2ByLo0ImjgIqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOtQ%2FOWtgk9zVKNHEyrcA62mp9QlM50xASiLLJA7BXODg0C4IcJwQ%2Bbz4bTMPqj0llCM1DQXs34O2NANYvSHeYHRjA75hpfH3Erh9ZcaRaIFDUg%2F%2BuFaSphWaVrIGSdFwAnIl6ouX5p6zqsoN33hVn3bzAyfb2IEx5h8sYpJ8Y02eGXyReGcIX0FDF%2FlHwR%2BSuZRUbE4WMGL9CyEKZb6AVhA7G%2FeTjh30iJ%2BtngZHaKwxlIyE2SeMTPC%2B%2F%2FCADx8LbeneUcyJTKwHAoGvWbjw7j0HROpWo2CN%2BJOkso7M3bmJ6%2BB7Vw1QiBGK%2B7DlZTRGLkGqAYFbhfWg0kfNrAUI0YubwAJ0RgGjljmOiIEtLnhWalYvT3%2B3TqVU5Iu5y8ukX3S86dZv2arLdWf%2BSAR6dioSh%2BonMw7ZizTf5E4xD23ljA%2FGS7qpiwY195QVzX0mF9iT67VxUKmJsCeeYXP%2By%2FMA8znx7BZDOerMpnkkul0n7w0u%2F360GFjS0rXVNKtKuC2ipqSuVxDDm0yNFFNAaqeaW%2B%2Byqoh%2BLNSs7IcQGS50SUJPLw1rC6cqcRwk5rLfJjcY7lE1ptYIVqv7N2VIk6CRr%2BHus9oZuU40JGYecbCGyU4va3szZuaqzPcGNFgcESBiuHg27LZGUqiMPG65rwGOqUBc5l6qW51i0wJPXq8Do6oA0g6Rf11oTWLqNeKi9T9a2kJu4yiwVj%2B9Ji%2FZ5xtmwO89P4Sm4%2BB49LBZYNihDbSStaATB06iaqUIn5jW%2BxW4snGaysruncLYEjzxS6Nl7%2BPLF1vuDKb66aZl1Kcc4G4KBQJjL5732W8Zo%2F4GBgqpntT0%2FVzh0Qx5vkSpC6ILyR5wuiPrHcUXq%2Fr4vJDDtS5R%2BkvWKG8&X-Amz-Signature=1f2b47987eb4573ed37dfde42ed4e753724da0e4bf1e434547d8980542559b6f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TY5KNEJN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH4aCXVzLXdlc3QtMiJHMEUCIQC7vC6lu4QdFNuFkMtGhoJOT8jZVGNNz7nAMT1T2X6SjQIgEjD%2FsG51YW89cu9tBdVXrLOaW2FnzhdYzmUSGHNTQX4qiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBJfzkvbHVgMHYIqHCrcA3ieF2udhC5JUcaH1Zqttii7RegM9cAHRB8Y%2BgPUTC1sm9a5q7u2f815dDMCEPM6WaGThAXP1yTHxHsA6Jkt3q%2FxDO%2FkcIZSHXkB0V2xaeg6RC7%2FRTo3ZKJ1ytoXTs9RA%2FESJbL3n8Q%2BSmfPwoba3Ne57056NLUC3zX%2B07BE60ZSqxI1mNM3vPv%2FiMgkggkzkyVm60VsVKc9mhYXxlh6KU021re%2F1FlQK%2FrDHc1KoxmZYS0QDfzBuone73nDOWLy1ms7ZykLqo2ZNS4CH2UAuUO1qaYKbh7YmY0CLZM%2BeTu498XoYIUZP2KpFpKxX03BgRDasUnSkRmqYqJIG2%2BKy4fSjlTMFmc%2FuXUBotyZMRAB34n%2FeL7nIyDvaLMkc0gyrpvoU5uIr2JSOcn%2FBXv7Z0XjRsY8C7M1KECPbH%2FyS%2BPA0HWLhvDBhYec04ExMPKxYW4ZUBT5Xj86NVe%2B8AQR8vkGsvJnhAkCU%2F4FyN%2FYE8bnOmAY5ErtcnDj7dv0uxWxHQaM33g18s1Ky4uQOcPoMdCMtGL75%2B%2FZG%2BtDZTUxXxOZf4xjBywXfCM8AY7wLVLxH4sPSrNRRIk5tMNlvxHqZBNFrw9H9wIv73HRWHuT4bHQ9XFqVdntax2UMONhMIaQ57wGOqUBCrTY6KXENJfWOqEL7u6PnfltjMxWJdpabsoXhxmvHw%2BZ6XBTIV8L0H6hU7SX%2BaSSu59uKZPMrACCRMHc6zF5WMtnYjS8jGXR2X6zmSuHVLMGhhFr9a62D19LhZUOFjPqSW%2FgPBMlRAOqBN7zvMBtRgYBSN6y5git2cwAJQno10YAJaEmowyl64adEGXXzpRHRnGo8JLCQ4p4G7VlxhezEiJ4tjBw&X-Amz-Signature=5b990373a8896053a2d35bc2f54114df849850af0507ed7264f055a3dad003cc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QFLXYHMI%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH4aCXVzLXdlc3QtMiJIMEYCIQCLOMwNf6mRtpVCIz7OZehgqH5q%2Ft5diwaU8at5Jg7zwgIhAPzRV7gKDHleX4ORtk9woUK4KIKTdcjdl3KjWkcExsBuKogECIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy1PaBWIKAQBPEDzXkq3AOZ0zAWXpQAwpFo5FVFdMst5Xny8hc5Yp2ad3kawdY%2BkG66dd90jIpP0cDlHrMoA%2BoHRgU%2B6HUVQ%2FJbG7C7xSvjDov%2FeEZ9Vokc4qudhaAeMKxQN3X5RQjWvgN%2FSZyFeEuxEPa7TmCiMSqmHgQdz4YJOQxKkDiekMnbJrV2i%2FtoZrLmI2JNV2HBWZUuGYBG6us%2Bd11%2BM3fOt2y00LYcpYFUq6pqYrUm2%2BqaxcTNlO3M5%2BaiycDalu0%2FFakSD9WwgnZc32tEWDzNUDuBgtQ%2F%2FvMNHwR%2FB0eWCkp%2FCJ2%2Frb80bsvwya9pmwuw%2B%2BFwtS9JLswN7537xb%2FCSeJ443r6L2gp50s%2BtK8MLGIXS%2BmqGgl7wJ%2FlF1rMUNQbVYAkf8Fjf9rx0qxGSztAw%2BOt2L%2B32qOIqO6V%2B7hKlGzZNqsTorm33sC5tqp8C8WJDt2asRTLIrbrQD0CFkzEtsH5Q2Pb%2BTK0HxOyIihgkfqmuZmHJvRBmRtxumdQZEjr9FA%2FZC3Km42K56%2Bp4czxKygbyFAbhnAmvyXIRAg%2BZ0fQ0sA1zVrqkFSI3exoXfC%2BUbUpx7POjfine%2F%2BoFkoDBIYFnKkLh9X9pZ4vd%2BEwpv1%2Fq691dQoBU9EQd0uaruSmN1ETAjD9j%2Be8BjqkAWQd1kmBE4G5HqW05ehxYl3SsuUz7eTRyPkO652hGk4ebdwVh17IfK16TZOgU5igpYtKMJupVenRxMoIh1YqQFSYS4Yu%2FAfUTYTSGRdGY%2BKFkly%2FKW3DoNbVguS8v3Tjb8LIIah2Ji18Aph75DvaqIZsfHSpvwkD6h7hGeKlByf8T%2BFuseWhlV0iCTajljqZL6kWA7%2F9ecURZ88dp9zOPhiwPdKy&X-Amz-Signature=83e83498cf62756be123afad32258fdeead746a4f708289a10bafbd7a8e310e2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QFLXYHMI%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH4aCXVzLXdlc3QtMiJIMEYCIQCLOMwNf6mRtpVCIz7OZehgqH5q%2Ft5diwaU8at5Jg7zwgIhAPzRV7gKDHleX4ORtk9woUK4KIKTdcjdl3KjWkcExsBuKogECIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy1PaBWIKAQBPEDzXkq3AOZ0zAWXpQAwpFo5FVFdMst5Xny8hc5Yp2ad3kawdY%2BkG66dd90jIpP0cDlHrMoA%2BoHRgU%2B6HUVQ%2FJbG7C7xSvjDov%2FeEZ9Vokc4qudhaAeMKxQN3X5RQjWvgN%2FSZyFeEuxEPa7TmCiMSqmHgQdz4YJOQxKkDiekMnbJrV2i%2FtoZrLmI2JNV2HBWZUuGYBG6us%2Bd11%2BM3fOt2y00LYcpYFUq6pqYrUm2%2BqaxcTNlO3M5%2BaiycDalu0%2FFakSD9WwgnZc32tEWDzNUDuBgtQ%2F%2FvMNHwR%2FB0eWCkp%2FCJ2%2Frb80bsvwya9pmwuw%2B%2BFwtS9JLswN7537xb%2FCSeJ443r6L2gp50s%2BtK8MLGIXS%2BmqGgl7wJ%2FlF1rMUNQbVYAkf8Fjf9rx0qxGSztAw%2BOt2L%2B32qOIqO6V%2B7hKlGzZNqsTorm33sC5tqp8C8WJDt2asRTLIrbrQD0CFkzEtsH5Q2Pb%2BTK0HxOyIihgkfqmuZmHJvRBmRtxumdQZEjr9FA%2FZC3Km42K56%2Bp4czxKygbyFAbhnAmvyXIRAg%2BZ0fQ0sA1zVrqkFSI3exoXfC%2BUbUpx7POjfine%2F%2BoFkoDBIYFnKkLh9X9pZ4vd%2BEwpv1%2Fq691dQoBU9EQd0uaruSmN1ETAjD9j%2Be8BjqkAWQd1kmBE4G5HqW05ehxYl3SsuUz7eTRyPkO652hGk4ebdwVh17IfK16TZOgU5igpYtKMJupVenRxMoIh1YqQFSYS4Yu%2FAfUTYTSGRdGY%2BKFkly%2FKW3DoNbVguS8v3Tjb8LIIah2Ji18Aph75DvaqIZsfHSpvwkD6h7hGeKlByf8T%2BFuseWhlV0iCTajljqZL6kWA7%2F9ecURZ88dp9zOPhiwPdKy&X-Amz-Signature=4d050d26bc0a4ae46975a23c6511015a8a7e83566691cf0238e5f28d792d79d4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QFLXYHMI%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH4aCXVzLXdlc3QtMiJIMEYCIQCLOMwNf6mRtpVCIz7OZehgqH5q%2Ft5diwaU8at5Jg7zwgIhAPzRV7gKDHleX4ORtk9woUK4KIKTdcjdl3KjWkcExsBuKogECIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy1PaBWIKAQBPEDzXkq3AOZ0zAWXpQAwpFo5FVFdMst5Xny8hc5Yp2ad3kawdY%2BkG66dd90jIpP0cDlHrMoA%2BoHRgU%2B6HUVQ%2FJbG7C7xSvjDov%2FeEZ9Vokc4qudhaAeMKxQN3X5RQjWvgN%2FSZyFeEuxEPa7TmCiMSqmHgQdz4YJOQxKkDiekMnbJrV2i%2FtoZrLmI2JNV2HBWZUuGYBG6us%2Bd11%2BM3fOt2y00LYcpYFUq6pqYrUm2%2BqaxcTNlO3M5%2BaiycDalu0%2FFakSD9WwgnZc32tEWDzNUDuBgtQ%2F%2FvMNHwR%2FB0eWCkp%2FCJ2%2Frb80bsvwya9pmwuw%2B%2BFwtS9JLswN7537xb%2FCSeJ443r6L2gp50s%2BtK8MLGIXS%2BmqGgl7wJ%2FlF1rMUNQbVYAkf8Fjf9rx0qxGSztAw%2BOt2L%2B32qOIqO6V%2B7hKlGzZNqsTorm33sC5tqp8C8WJDt2asRTLIrbrQD0CFkzEtsH5Q2Pb%2BTK0HxOyIihgkfqmuZmHJvRBmRtxumdQZEjr9FA%2FZC3Km42K56%2Bp4czxKygbyFAbhnAmvyXIRAg%2BZ0fQ0sA1zVrqkFSI3exoXfC%2BUbUpx7POjfine%2F%2BoFkoDBIYFnKkLh9X9pZ4vd%2BEwpv1%2Fq691dQoBU9EQd0uaruSmN1ETAjD9j%2Be8BjqkAWQd1kmBE4G5HqW05ehxYl3SsuUz7eTRyPkO652hGk4ebdwVh17IfK16TZOgU5igpYtKMJupVenRxMoIh1YqQFSYS4Yu%2FAfUTYTSGRdGY%2BKFkly%2FKW3DoNbVguS8v3Tjb8LIIah2Ji18Aph75DvaqIZsfHSpvwkD6h7hGeKlByf8T%2BFuseWhlV0iCTajljqZL6kWA7%2F9ecURZ88dp9zOPhiwPdKy&X-Amz-Signature=06d11d5c48bb8369f8d56b45f32ec7a5acd078d3b44e02339b4ef7d84a58daec&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QFLXYHMI%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH4aCXVzLXdlc3QtMiJIMEYCIQCLOMwNf6mRtpVCIz7OZehgqH5q%2Ft5diwaU8at5Jg7zwgIhAPzRV7gKDHleX4ORtk9woUK4KIKTdcjdl3KjWkcExsBuKogECIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy1PaBWIKAQBPEDzXkq3AOZ0zAWXpQAwpFo5FVFdMst5Xny8hc5Yp2ad3kawdY%2BkG66dd90jIpP0cDlHrMoA%2BoHRgU%2B6HUVQ%2FJbG7C7xSvjDov%2FeEZ9Vokc4qudhaAeMKxQN3X5RQjWvgN%2FSZyFeEuxEPa7TmCiMSqmHgQdz4YJOQxKkDiekMnbJrV2i%2FtoZrLmI2JNV2HBWZUuGYBG6us%2Bd11%2BM3fOt2y00LYcpYFUq6pqYrUm2%2BqaxcTNlO3M5%2BaiycDalu0%2FFakSD9WwgnZc32tEWDzNUDuBgtQ%2F%2FvMNHwR%2FB0eWCkp%2FCJ2%2Frb80bsvwya9pmwuw%2B%2BFwtS9JLswN7537xb%2FCSeJ443r6L2gp50s%2BtK8MLGIXS%2BmqGgl7wJ%2FlF1rMUNQbVYAkf8Fjf9rx0qxGSztAw%2BOt2L%2B32qOIqO6V%2B7hKlGzZNqsTorm33sC5tqp8C8WJDt2asRTLIrbrQD0CFkzEtsH5Q2Pb%2BTK0HxOyIihgkfqmuZmHJvRBmRtxumdQZEjr9FA%2FZC3Km42K56%2Bp4czxKygbyFAbhnAmvyXIRAg%2BZ0fQ0sA1zVrqkFSI3exoXfC%2BUbUpx7POjfine%2F%2BoFkoDBIYFnKkLh9X9pZ4vd%2BEwpv1%2Fq691dQoBU9EQd0uaruSmN1ETAjD9j%2Be8BjqkAWQd1kmBE4G5HqW05ehxYl3SsuUz7eTRyPkO652hGk4ebdwVh17IfK16TZOgU5igpYtKMJupVenRxMoIh1YqQFSYS4Yu%2FAfUTYTSGRdGY%2BKFkly%2FKW3DoNbVguS8v3Tjb8LIIah2Ji18Aph75DvaqIZsfHSpvwkD6h7hGeKlByf8T%2BFuseWhlV0iCTajljqZL6kWA7%2F9ecURZ88dp9zOPhiwPdKy&X-Amz-Signature=eea8253ee437cd5a513979c0856ac2fa1fead71919a26b6ddc36158a49587e23&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
