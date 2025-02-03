

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666PUURMMX%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDRn4NcIGm8bcx2byXBIYo1KpZBB9nwHy2oYRmlOlivgAIhAPYDPYp6GcW%2FJvf5X6r521x%2B780ABxapS1DWfC51uZECKv8DCBcQABoMNjM3NDIzMTgzODA1IgyDlV3yR6FHgzE0gaEq3ANeuW3BW%2FA94fpVRLV9KHyp7hkz4Tr5U13gUDAtQBu6zFC%2FX8rc6mU8jVM0y9U6jlmfoXk2RVVvxJUJN%2BBpRBkJU8teMwZ4mHJf%2Fpohvk4KlM2qFe8PyDNxmLteWrBjLIdpGwhCZA2ttSKhDhXgz2X79NLAvo%2BjMDifOTlnJ0ROfhzI%2BirR2HIaoqHDuuAIC%2B%2ByJjbcu2UQY1eUiwMHKuT9hbodvXmAZGIGOeWviayw7fnJ68bCtJFrQw%2B8cqmt33asfxW6j0DCfzR4SgTXfcfwN7RlaNKm80l77KzsbuXdPvHwsXyvXodf5UpGVR6VlRkFIgAfEYT3bM%2BLnrbZAnA4RtZV2Czr8JYur2fwUbY25EmQOtIX508%2Bn4mYfAXIswvgOwKlcmU4hX6FIB2Q8EByAj%2BDXV2KALdgKd44F3os9zfDaFKCpVoJjN5AKX8IxDg8%2FcwdfHDwQuQmvZU%2F%2F8%2Bapym46GFa4%2Fhg6B1i6dtVnDnbGeClqvnn2wxC3XwhOE45ZN602I6SVYaU269jSHysb6G1%2B0SoDA75Q91fUMsWUGUNGjODhnY4HHZhx2UwQwpyR5QhixwwRw9GidF2SUXG9FIU97le4le6NHNrq2w00Flf1%2FQNX%2FZVQ1dqTjDujYO9BjqkAceCCZnFw0wOlq7Q5%2FmzOanVXJ3xpKi5PQ9P2wFu6JxiFt48EGGb%2BsiQ4bPFfYgDfWweQz4aNHpK8lwmkLv6q5RHeT3Dhl3Tst0XXSQO3VvCp0GJ3g%2BvkgVLSLT883gUVszSTaTsMGd6gn%2FJULvSjdY3TfDilvMp%2Bx2UOHWCUKReqp%2Bp%2BwJyI154VsoRvJIntjtD%2BlQvU8xXtLUhJpVQBRhIr1Kq&X-Amz-Signature=381571ecd24f757e01c9e4b3ebff5236e26065d9ac7d8dd2f7e4e4231932ce1b&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666PUURMMX%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDRn4NcIGm8bcx2byXBIYo1KpZBB9nwHy2oYRmlOlivgAIhAPYDPYp6GcW%2FJvf5X6r521x%2B780ABxapS1DWfC51uZECKv8DCBcQABoMNjM3NDIzMTgzODA1IgyDlV3yR6FHgzE0gaEq3ANeuW3BW%2FA94fpVRLV9KHyp7hkz4Tr5U13gUDAtQBu6zFC%2FX8rc6mU8jVM0y9U6jlmfoXk2RVVvxJUJN%2BBpRBkJU8teMwZ4mHJf%2Fpohvk4KlM2qFe8PyDNxmLteWrBjLIdpGwhCZA2ttSKhDhXgz2X79NLAvo%2BjMDifOTlnJ0ROfhzI%2BirR2HIaoqHDuuAIC%2B%2ByJjbcu2UQY1eUiwMHKuT9hbodvXmAZGIGOeWviayw7fnJ68bCtJFrQw%2B8cqmt33asfxW6j0DCfzR4SgTXfcfwN7RlaNKm80l77KzsbuXdPvHwsXyvXodf5UpGVR6VlRkFIgAfEYT3bM%2BLnrbZAnA4RtZV2Czr8JYur2fwUbY25EmQOtIX508%2Bn4mYfAXIswvgOwKlcmU4hX6FIB2Q8EByAj%2BDXV2KALdgKd44F3os9zfDaFKCpVoJjN5AKX8IxDg8%2FcwdfHDwQuQmvZU%2F%2F8%2Bapym46GFa4%2Fhg6B1i6dtVnDnbGeClqvnn2wxC3XwhOE45ZN602I6SVYaU269jSHysb6G1%2B0SoDA75Q91fUMsWUGUNGjODhnY4HHZhx2UwQwpyR5QhixwwRw9GidF2SUXG9FIU97le4le6NHNrq2w00Flf1%2FQNX%2FZVQ1dqTjDujYO9BjqkAceCCZnFw0wOlq7Q5%2FmzOanVXJ3xpKi5PQ9P2wFu6JxiFt48EGGb%2BsiQ4bPFfYgDfWweQz4aNHpK8lwmkLv6q5RHeT3Dhl3Tst0XXSQO3VvCp0GJ3g%2BvkgVLSLT883gUVszSTaTsMGd6gn%2FJULvSjdY3TfDilvMp%2Bx2UOHWCUKReqp%2Bp%2BwJyI154VsoRvJIntjtD%2BlQvU8xXtLUhJpVQBRhIr1Kq&X-Amz-Signature=d2fed9b8672b972df3a66c4788f1989d34e299224b4f9c3069a4c29818102c5a&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666PUURMMX%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDRn4NcIGm8bcx2byXBIYo1KpZBB9nwHy2oYRmlOlivgAIhAPYDPYp6GcW%2FJvf5X6r521x%2B780ABxapS1DWfC51uZECKv8DCBcQABoMNjM3NDIzMTgzODA1IgyDlV3yR6FHgzE0gaEq3ANeuW3BW%2FA94fpVRLV9KHyp7hkz4Tr5U13gUDAtQBu6zFC%2FX8rc6mU8jVM0y9U6jlmfoXk2RVVvxJUJN%2BBpRBkJU8teMwZ4mHJf%2Fpohvk4KlM2qFe8PyDNxmLteWrBjLIdpGwhCZA2ttSKhDhXgz2X79NLAvo%2BjMDifOTlnJ0ROfhzI%2BirR2HIaoqHDuuAIC%2B%2ByJjbcu2UQY1eUiwMHKuT9hbodvXmAZGIGOeWviayw7fnJ68bCtJFrQw%2B8cqmt33asfxW6j0DCfzR4SgTXfcfwN7RlaNKm80l77KzsbuXdPvHwsXyvXodf5UpGVR6VlRkFIgAfEYT3bM%2BLnrbZAnA4RtZV2Czr8JYur2fwUbY25EmQOtIX508%2Bn4mYfAXIswvgOwKlcmU4hX6FIB2Q8EByAj%2BDXV2KALdgKd44F3os9zfDaFKCpVoJjN5AKX8IxDg8%2FcwdfHDwQuQmvZU%2F%2F8%2Bapym46GFa4%2Fhg6B1i6dtVnDnbGeClqvnn2wxC3XwhOE45ZN602I6SVYaU269jSHysb6G1%2B0SoDA75Q91fUMsWUGUNGjODhnY4HHZhx2UwQwpyR5QhixwwRw9GidF2SUXG9FIU97le4le6NHNrq2w00Flf1%2FQNX%2FZVQ1dqTjDujYO9BjqkAceCCZnFw0wOlq7Q5%2FmzOanVXJ3xpKi5PQ9P2wFu6JxiFt48EGGb%2BsiQ4bPFfYgDfWweQz4aNHpK8lwmkLv6q5RHeT3Dhl3Tst0XXSQO3VvCp0GJ3g%2BvkgVLSLT883gUVszSTaTsMGd6gn%2FJULvSjdY3TfDilvMp%2Bx2UOHWCUKReqp%2Bp%2BwJyI154VsoRvJIntjtD%2BlQvU8xXtLUhJpVQBRhIr1Kq&X-Amz-Signature=6815ec0d83bb7fe360f57a4d7764f393e586f5b0643610b49998a478ad240b83&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666Z36TKSV%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC6acrcG9bXG1i9hKYiw4YW%2BngPlg0V7dXuV4kpCPT5MgIgaZ3N5zWl8Cw45PTQFINS5FcXapA113W5ClHndPHMjNwq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDCq2DBNHqSSRqjHR2ircAzOSFxw%2F%2BQrNM1vY9gWTJnoeeWPDGsZXKFUoZX%2BdaIo2PmYVRRDnsJXBhAeufDhqRnJowP3HT7jh9RdZmzKiT5kZajUje%2BToUm2ijc9wT3H%2BbUDwCV4UwkIEI7azJYw4KfLx5OhD1iCkc2mKAI1bi15YlX3jvZUJr7AD1BvlUO5JIJ2j1iIopsqLLw9JhtPnBlvfBN0kCDBxkwIImKQvPcOZMvBb1WQ085bwV3zdmX4dGGk5ZM%2B6YQW5oj39Kn4ASVbyLPW3tIZSupnv9ncOm%2B%2F4466ejggn9ffw8ZsyLqCsVnpXNcfuLjdqBLRwgcCeAmrAd7XaoTYq5ATl7XjM2HZu%2FvZzmoGFhkGScdhnhGwJOboLmg7MxmyCCzJZ3D33%2FmuThiGCy0nZddnVy%2B7nN%2FpXvs7j1Xu3toECS7cQEk5ZZSWwEBuchEqnW2NMajAvrg8S32dwfrmoLACHFrGqlDhpJjUWzDZp%2BukR0WoFeqqlCnGp%2BF1z0bNF8%2FaMJoMTsTuh0DYGiEPDzfZgZ8kP07Qh2TRHb35UT0mi1qAypiMhBw5UBH2JC3vrI1MBQrc4KWc3cdn0YmjLdNY8iMVPbzPd0lC7k4l6Ial5r2h0dDmW%2B6vcfdN6%2Bjw0ThFSMM2Ng70GOqUBPLDtifcSN8P010sW1obEqp%2Ft5zNcq8IRHU7tuMO7P1tZVnxRFtVxKlry6cMqMSib3uwmztSfDNL%2FXkD2sqIY1zFUmka7ttojNISuVg%2FQPeh33u%2BPfioMoN5vKgVhmew08cTalOu5TaDP7nsV1VY5Bhdzu%2F57HbYJudP0cEzq6Rw97ad08tGbJqy9wgupCyx4ef8SNT4JyWECjKZywelJLqdk12oO&X-Amz-Signature=05332c76e33f258e61eb4423119e3683a6d4990c9a0b6a392a0f22cb01a8df68&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664W43XZYR%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC21fyCVOKk1d5smZ6d1CbnpUFtRLJxKb6m8lv%2Bvj9GBgIhAKlvdBoVAVQ7s%2Bfqr42pDb6AvzuzTmlqpTw9m6xRIqxRKv8DCBcQABoMNjM3NDIzMTgzODA1Igz9KIc4xk7P%2BfM5UlIq3AP79qLLgxA%2Bxhlk%2B0sY7zn4u7V7rn8yNgz8t7chJ5pxIQdeNATQP20VQd%2FdahoXCRIWyXFz3fqorhHUAIw%2BUu233Fc32H6yBBYgjkL9ycfiLTxrN80lJ0p3RIns0QGxFdVuZ56iXx8jvbyT3VrGZSE6dDLDAhIf7j2KIkFThB%2F%2FyAGp9UyE9%2FLEaDHfc4UzJkYrgIpRL9OrFMpfiqLh0CqFZtw0l8qDFWNCWsaaKC%2FKZNhEVbz6S6tz%2F%2BgAT63AfC6m6paR1G%2FZqAdHqvacmCOnYrph1d34vkhXyBlYlCKCf6fD1AGs6RWo2xcRzW1mky7MxKhY3Zbi7cHVDQiL15HAUM2fNPa5ixgvg4nUOzIPt%2FFISG%2BC798%2F%2BUT%2FziEM6h0x78Sfv017sm66IjKGt9u%2BBzB4SqasW4%2FbYcsCZF5ELYORURYGbvAcOQavHKq4b8gEM%2FBdLASwOZbiMaWS18VPq0NWIoV42QU5R5bbhGQpueZfWHrGtgkdH%2FNLCXjTLZiz0jU%2B0eNiBK%2FwXhe9MuJKfgXULld9Ql04GQO0zWPdb9vIg9299jNl1b%2BPJIPVfH7TS7wuvmISl6Ru5ug9Bwx3lXuE20aN9ZEgvjaEq0BHfWn0%2FhMrfereyswrbjCrjYO9BjqkAYdTQpi7jMr4OsvMyndJjE%2Fvnsmvb0AJxojj5vXgx07jI6rT%2FQ%2FXzHtDqwKHy4At%2FM14BGzojC%2BhNsDK%2FJVWXMOJas5d%2FlBBrx32L0PSkFRbwNq4e7eQsWi6rXxdIJVAxD3ZvghdSGdR2Vsy46RnSNuGvAV5keQn%2Fpj7QkYzy%2Fa3e2aZ%2BJFtKYAANTNVAaUjg9U68zzNFv%2FgfVwA0%2BxNv5FcPihX&X-Amz-Signature=d358162939eec9a46bd346ffe8aececc677aba1240dc4eea46959f6444670378&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666PUURMMX%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDRn4NcIGm8bcx2byXBIYo1KpZBB9nwHy2oYRmlOlivgAIhAPYDPYp6GcW%2FJvf5X6r521x%2B780ABxapS1DWfC51uZECKv8DCBcQABoMNjM3NDIzMTgzODA1IgyDlV3yR6FHgzE0gaEq3ANeuW3BW%2FA94fpVRLV9KHyp7hkz4Tr5U13gUDAtQBu6zFC%2FX8rc6mU8jVM0y9U6jlmfoXk2RVVvxJUJN%2BBpRBkJU8teMwZ4mHJf%2Fpohvk4KlM2qFe8PyDNxmLteWrBjLIdpGwhCZA2ttSKhDhXgz2X79NLAvo%2BjMDifOTlnJ0ROfhzI%2BirR2HIaoqHDuuAIC%2B%2ByJjbcu2UQY1eUiwMHKuT9hbodvXmAZGIGOeWviayw7fnJ68bCtJFrQw%2B8cqmt33asfxW6j0DCfzR4SgTXfcfwN7RlaNKm80l77KzsbuXdPvHwsXyvXodf5UpGVR6VlRkFIgAfEYT3bM%2BLnrbZAnA4RtZV2Czr8JYur2fwUbY25EmQOtIX508%2Bn4mYfAXIswvgOwKlcmU4hX6FIB2Q8EByAj%2BDXV2KALdgKd44F3os9zfDaFKCpVoJjN5AKX8IxDg8%2FcwdfHDwQuQmvZU%2F%2F8%2Bapym46GFa4%2Fhg6B1i6dtVnDnbGeClqvnn2wxC3XwhOE45ZN602I6SVYaU269jSHysb6G1%2B0SoDA75Q91fUMsWUGUNGjODhnY4HHZhx2UwQwpyR5QhixwwRw9GidF2SUXG9FIU97le4le6NHNrq2w00Flf1%2FQNX%2FZVQ1dqTjDujYO9BjqkAceCCZnFw0wOlq7Q5%2FmzOanVXJ3xpKi5PQ9P2wFu6JxiFt48EGGb%2BsiQ4bPFfYgDfWweQz4aNHpK8lwmkLv6q5RHeT3Dhl3Tst0XXSQO3VvCp0GJ3g%2BvkgVLSLT883gUVszSTaTsMGd6gn%2FJULvSjdY3TfDilvMp%2Bx2UOHWCUKReqp%2Bp%2BwJyI154VsoRvJIntjtD%2BlQvU8xXtLUhJpVQBRhIr1Kq&X-Amz-Signature=a369510994caa2c11b5ed13eb4dc2239b821ac67fe17928c434c376e6e144446&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666PUURMMX%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDRn4NcIGm8bcx2byXBIYo1KpZBB9nwHy2oYRmlOlivgAIhAPYDPYp6GcW%2FJvf5X6r521x%2B780ABxapS1DWfC51uZECKv8DCBcQABoMNjM3NDIzMTgzODA1IgyDlV3yR6FHgzE0gaEq3ANeuW3BW%2FA94fpVRLV9KHyp7hkz4Tr5U13gUDAtQBu6zFC%2FX8rc6mU8jVM0y9U6jlmfoXk2RVVvxJUJN%2BBpRBkJU8teMwZ4mHJf%2Fpohvk4KlM2qFe8PyDNxmLteWrBjLIdpGwhCZA2ttSKhDhXgz2X79NLAvo%2BjMDifOTlnJ0ROfhzI%2BirR2HIaoqHDuuAIC%2B%2ByJjbcu2UQY1eUiwMHKuT9hbodvXmAZGIGOeWviayw7fnJ68bCtJFrQw%2B8cqmt33asfxW6j0DCfzR4SgTXfcfwN7RlaNKm80l77KzsbuXdPvHwsXyvXodf5UpGVR6VlRkFIgAfEYT3bM%2BLnrbZAnA4RtZV2Czr8JYur2fwUbY25EmQOtIX508%2Bn4mYfAXIswvgOwKlcmU4hX6FIB2Q8EByAj%2BDXV2KALdgKd44F3os9zfDaFKCpVoJjN5AKX8IxDg8%2FcwdfHDwQuQmvZU%2F%2F8%2Bapym46GFa4%2Fhg6B1i6dtVnDnbGeClqvnn2wxC3XwhOE45ZN602I6SVYaU269jSHysb6G1%2B0SoDA75Q91fUMsWUGUNGjODhnY4HHZhx2UwQwpyR5QhixwwRw9GidF2SUXG9FIU97le4le6NHNrq2w00Flf1%2FQNX%2FZVQ1dqTjDujYO9BjqkAceCCZnFw0wOlq7Q5%2FmzOanVXJ3xpKi5PQ9P2wFu6JxiFt48EGGb%2BsiQ4bPFfYgDfWweQz4aNHpK8lwmkLv6q5RHeT3Dhl3Tst0XXSQO3VvCp0GJ3g%2BvkgVLSLT883gUVszSTaTsMGd6gn%2FJULvSjdY3TfDilvMp%2Bx2UOHWCUKReqp%2Bp%2BwJyI154VsoRvJIntjtD%2BlQvU8xXtLUhJpVQBRhIr1Kq&X-Amz-Signature=00618989f5f3716ca1a16c0371445be4568426cf0c7d542f5ba3bc4ee7f61509&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666PUURMMX%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDRn4NcIGm8bcx2byXBIYo1KpZBB9nwHy2oYRmlOlivgAIhAPYDPYp6GcW%2FJvf5X6r521x%2B780ABxapS1DWfC51uZECKv8DCBcQABoMNjM3NDIzMTgzODA1IgyDlV3yR6FHgzE0gaEq3ANeuW3BW%2FA94fpVRLV9KHyp7hkz4Tr5U13gUDAtQBu6zFC%2FX8rc6mU8jVM0y9U6jlmfoXk2RVVvxJUJN%2BBpRBkJU8teMwZ4mHJf%2Fpohvk4KlM2qFe8PyDNxmLteWrBjLIdpGwhCZA2ttSKhDhXgz2X79NLAvo%2BjMDifOTlnJ0ROfhzI%2BirR2HIaoqHDuuAIC%2B%2ByJjbcu2UQY1eUiwMHKuT9hbodvXmAZGIGOeWviayw7fnJ68bCtJFrQw%2B8cqmt33asfxW6j0DCfzR4SgTXfcfwN7RlaNKm80l77KzsbuXdPvHwsXyvXodf5UpGVR6VlRkFIgAfEYT3bM%2BLnrbZAnA4RtZV2Czr8JYur2fwUbY25EmQOtIX508%2Bn4mYfAXIswvgOwKlcmU4hX6FIB2Q8EByAj%2BDXV2KALdgKd44F3os9zfDaFKCpVoJjN5AKX8IxDg8%2FcwdfHDwQuQmvZU%2F%2F8%2Bapym46GFa4%2Fhg6B1i6dtVnDnbGeClqvnn2wxC3XwhOE45ZN602I6SVYaU269jSHysb6G1%2B0SoDA75Q91fUMsWUGUNGjODhnY4HHZhx2UwQwpyR5QhixwwRw9GidF2SUXG9FIU97le4le6NHNrq2w00Flf1%2FQNX%2FZVQ1dqTjDujYO9BjqkAceCCZnFw0wOlq7Q5%2FmzOanVXJ3xpKi5PQ9P2wFu6JxiFt48EGGb%2BsiQ4bPFfYgDfWweQz4aNHpK8lwmkLv6q5RHeT3Dhl3Tst0XXSQO3VvCp0GJ3g%2BvkgVLSLT883gUVszSTaTsMGd6gn%2FJULvSjdY3TfDilvMp%2Bx2UOHWCUKReqp%2Bp%2BwJyI154VsoRvJIntjtD%2BlQvU8xXtLUhJpVQBRhIr1Kq&X-Amz-Signature=da4ac72c646496d17971c9e8820c39f5e9bec770d4bcd0131e5cc185dc4038bd&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666PUURMMX%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDRn4NcIGm8bcx2byXBIYo1KpZBB9nwHy2oYRmlOlivgAIhAPYDPYp6GcW%2FJvf5X6r521x%2B780ABxapS1DWfC51uZECKv8DCBcQABoMNjM3NDIzMTgzODA1IgyDlV3yR6FHgzE0gaEq3ANeuW3BW%2FA94fpVRLV9KHyp7hkz4Tr5U13gUDAtQBu6zFC%2FX8rc6mU8jVM0y9U6jlmfoXk2RVVvxJUJN%2BBpRBkJU8teMwZ4mHJf%2Fpohvk4KlM2qFe8PyDNxmLteWrBjLIdpGwhCZA2ttSKhDhXgz2X79NLAvo%2BjMDifOTlnJ0ROfhzI%2BirR2HIaoqHDuuAIC%2B%2ByJjbcu2UQY1eUiwMHKuT9hbodvXmAZGIGOeWviayw7fnJ68bCtJFrQw%2B8cqmt33asfxW6j0DCfzR4SgTXfcfwN7RlaNKm80l77KzsbuXdPvHwsXyvXodf5UpGVR6VlRkFIgAfEYT3bM%2BLnrbZAnA4RtZV2Czr8JYur2fwUbY25EmQOtIX508%2Bn4mYfAXIswvgOwKlcmU4hX6FIB2Q8EByAj%2BDXV2KALdgKd44F3os9zfDaFKCpVoJjN5AKX8IxDg8%2FcwdfHDwQuQmvZU%2F%2F8%2Bapym46GFa4%2Fhg6B1i6dtVnDnbGeClqvnn2wxC3XwhOE45ZN602I6SVYaU269jSHysb6G1%2B0SoDA75Q91fUMsWUGUNGjODhnY4HHZhx2UwQwpyR5QhixwwRw9GidF2SUXG9FIU97le4le6NHNrq2w00Flf1%2FQNX%2FZVQ1dqTjDujYO9BjqkAceCCZnFw0wOlq7Q5%2FmzOanVXJ3xpKi5PQ9P2wFu6JxiFt48EGGb%2BsiQ4bPFfYgDfWweQz4aNHpK8lwmkLv6q5RHeT3Dhl3Tst0XXSQO3VvCp0GJ3g%2BvkgVLSLT883gUVszSTaTsMGd6gn%2FJULvSjdY3TfDilvMp%2Bx2UOHWCUKReqp%2Bp%2BwJyI154VsoRvJIntjtD%2BlQvU8xXtLUhJpVQBRhIr1Kq&X-Amz-Signature=3c8c2184fba6090f82c4e81c78fa4db8805c81dc920ba4ff3699632f8598d689&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
