

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XVZJUBA3%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDOpeAwvMtfX7wq3WKA%2BrYuVbOxok4tfR8JO8UVKvcvhwIhAPKXyJMSzkPOPMjI2pUKYZ%2ByTQxNDH4%2B5MWzwKA5hd%2BnKogECLz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwfjQSyn7Jgu3676YYq3AP%2FT2Txi88wSFQrRHxG1fIUaLfMwFeMdUF1rhbdmclUs37lRVZPmnqwZTPtMZF6HBqBop%2B%2FOcjcZpGGUuLFT%2FMAkNrSybiUdj11TIL9k8seS%2BmNWyQ1H1Ovk5HNEHejQY5b79jGvdTwkysIFjj98AxfeOoA3xj8diajYOv89bAmOOlNNEM56OxBaPT6ta94Bo3gSQTkw7hG5hOAg8vMIilO3ByfodsXKpAk1lyflfxdUUmon5cE4%2FlwKGF4AVvtdl6MAo1nuI7SDFa%2BNmnQtYwhKfErh8dOym8Y%2FcV9mTbcUzJp7dXx71vBx3HmkaAabM7ivUPQB4JniaE3w%2B%2F4UBswe3vfNqxq%2FUeVdgcp%2FLkSfj8%2FHENBuP71JUVVBTXQiiLgl8SSnrEHgvEa56uxf3HFE3bdKAwG15vBLmCvdZ94zT%2BuJZ92IPmx89xKIt3TfKRtwJTIUp5VquWfPZDnayb78C3QHD896uE0qh4U7%2FcxIaiweIFFqvWjYBZCfUXEOQsNNCpPSnD1rLoRETrQB8ocN%2Frn6IqFjluYuIxKh4GIH1DIgaseFzz1Fbs92GBo0P8ekGoF4%2BTOm4bVNwW%2FkkCx6%2Fcouw6mDYBiFqEbNzAcRyectrurxCjC4fk6JTC61vK8BjqkAe7sRPkqRbwAbWxg6LwRQXebXHh0avQLCVck9sFYEZlf5Qst79vkef6MDowjEDSLKdhG5CwlKQwDzl0YKiaxENCBNPbjE8TBgMlSqjpyW62my8i1S2FpN0yiH%2Fy4g1%2FgMD5snlIwlGrvb3wJutby1esOzS%2BRBRc4IVrUzagJRNu08gxrK3fjX%2BHCtP6Wdk8NfviLjFK35HBfokC07n0esa7JZ0VH&X-Amz-Signature=f54c521b56f003a53e4dda9fd8d9adf31ed4084f35899038ec068451ec236ff8&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XVZJUBA3%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDOpeAwvMtfX7wq3WKA%2BrYuVbOxok4tfR8JO8UVKvcvhwIhAPKXyJMSzkPOPMjI2pUKYZ%2ByTQxNDH4%2B5MWzwKA5hd%2BnKogECLz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwfjQSyn7Jgu3676YYq3AP%2FT2Txi88wSFQrRHxG1fIUaLfMwFeMdUF1rhbdmclUs37lRVZPmnqwZTPtMZF6HBqBop%2B%2FOcjcZpGGUuLFT%2FMAkNrSybiUdj11TIL9k8seS%2BmNWyQ1H1Ovk5HNEHejQY5b79jGvdTwkysIFjj98AxfeOoA3xj8diajYOv89bAmOOlNNEM56OxBaPT6ta94Bo3gSQTkw7hG5hOAg8vMIilO3ByfodsXKpAk1lyflfxdUUmon5cE4%2FlwKGF4AVvtdl6MAo1nuI7SDFa%2BNmnQtYwhKfErh8dOym8Y%2FcV9mTbcUzJp7dXx71vBx3HmkaAabM7ivUPQB4JniaE3w%2B%2F4UBswe3vfNqxq%2FUeVdgcp%2FLkSfj8%2FHENBuP71JUVVBTXQiiLgl8SSnrEHgvEa56uxf3HFE3bdKAwG15vBLmCvdZ94zT%2BuJZ92IPmx89xKIt3TfKRtwJTIUp5VquWfPZDnayb78C3QHD896uE0qh4U7%2FcxIaiweIFFqvWjYBZCfUXEOQsNNCpPSnD1rLoRETrQB8ocN%2Frn6IqFjluYuIxKh4GIH1DIgaseFzz1Fbs92GBo0P8ekGoF4%2BTOm4bVNwW%2FkkCx6%2Fcouw6mDYBiFqEbNzAcRyectrurxCjC4fk6JTC61vK8BjqkAe7sRPkqRbwAbWxg6LwRQXebXHh0avQLCVck9sFYEZlf5Qst79vkef6MDowjEDSLKdhG5CwlKQwDzl0YKiaxENCBNPbjE8TBgMlSqjpyW62my8i1S2FpN0yiH%2Fy4g1%2FgMD5snlIwlGrvb3wJutby1esOzS%2BRBRc4IVrUzagJRNu08gxrK3fjX%2BHCtP6Wdk8NfviLjFK35HBfokC07n0esa7JZ0VH&X-Amz-Signature=cfc3f47b14aea469e9a6446db07aa8a8990445471c7a24a42150254b6134eb46&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XVZJUBA3%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDOpeAwvMtfX7wq3WKA%2BrYuVbOxok4tfR8JO8UVKvcvhwIhAPKXyJMSzkPOPMjI2pUKYZ%2ByTQxNDH4%2B5MWzwKA5hd%2BnKogECLz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwfjQSyn7Jgu3676YYq3AP%2FT2Txi88wSFQrRHxG1fIUaLfMwFeMdUF1rhbdmclUs37lRVZPmnqwZTPtMZF6HBqBop%2B%2FOcjcZpGGUuLFT%2FMAkNrSybiUdj11TIL9k8seS%2BmNWyQ1H1Ovk5HNEHejQY5b79jGvdTwkysIFjj98AxfeOoA3xj8diajYOv89bAmOOlNNEM56OxBaPT6ta94Bo3gSQTkw7hG5hOAg8vMIilO3ByfodsXKpAk1lyflfxdUUmon5cE4%2FlwKGF4AVvtdl6MAo1nuI7SDFa%2BNmnQtYwhKfErh8dOym8Y%2FcV9mTbcUzJp7dXx71vBx3HmkaAabM7ivUPQB4JniaE3w%2B%2F4UBswe3vfNqxq%2FUeVdgcp%2FLkSfj8%2FHENBuP71JUVVBTXQiiLgl8SSnrEHgvEa56uxf3HFE3bdKAwG15vBLmCvdZ94zT%2BuJZ92IPmx89xKIt3TfKRtwJTIUp5VquWfPZDnayb78C3QHD896uE0qh4U7%2FcxIaiweIFFqvWjYBZCfUXEOQsNNCpPSnD1rLoRETrQB8ocN%2Frn6IqFjluYuIxKh4GIH1DIgaseFzz1Fbs92GBo0P8ekGoF4%2BTOm4bVNwW%2FkkCx6%2Fcouw6mDYBiFqEbNzAcRyectrurxCjC4fk6JTC61vK8BjqkAe7sRPkqRbwAbWxg6LwRQXebXHh0avQLCVck9sFYEZlf5Qst79vkef6MDowjEDSLKdhG5CwlKQwDzl0YKiaxENCBNPbjE8TBgMlSqjpyW62my8i1S2FpN0yiH%2Fy4g1%2FgMD5snlIwlGrvb3wJutby1esOzS%2BRBRc4IVrUzagJRNu08gxrK3fjX%2BHCtP6Wdk8NfviLjFK35HBfokC07n0esa7JZ0VH&X-Amz-Signature=d863c7c9b6b1e3bc39561a1bdc681b36a4d30a188d008f24eff8e1a22c6795e9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YDWZY7TK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDVgDgU0biTQtMDFJbiPwD%2Bf1Kkwv7hGikj33EZhFtkhAIhAOHptcSsw%2BmvuYp7A0akkbyrgDkGfSlR92zbLOuZVrVDKogECLz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzLXDfbHuGvEYMQyJcq3ANMAhVd6Uh0aTkLSv2cz4rak%2Fg09vq%2FggkuZClAXiU3SMun7NllypG2%2Bmxi9553k6vbbe4F89A2Cv6tP0jxuStMnG%2BizKHFNBPAyfMcGgIxygnDadatEgOiVFk%2BHt8dG8L6IenO0w%2BWNmjyvfHe5xscjme6a7snaYWEXrGWLsRieVMi9WCPv55Cc6rX8OQvP%2BRy5J%2BZRU%2F%2BBuAh9T7ekHYIPB710LOPy0ivga%2BtORPd8g%2BqYloo3vXsN1XcAh%2B0BPNJIlw2sNL4Y6%2F5gdAXfRVPcqUJiu4efmIIqv4iZUBF%2FrfWDifGf4Q9MErxteFYIgXzQp9kkzZlCln65Cgv1V%2BdJCUwmpmSYAkF%2BQRJDCAlN91OjJ8HRjrF5VEWep7SuxbnGpnTYMCbM27crVju0b6xN4nXt%2BREQUvyZYRF8sgNm6nBgHaKp5KEAiChS7kJUeRa65vW7ikopSQyjdGkKL1bxo11dJa9jPMDrsdldwopO%2BbR0aNiapEM0KvAAnj8CeYjjnRkUJLQ9cNAhSCG4vLYutBZoaJRKAOylZ2nF%2F%2Fj76Y4gvuXOCiolI%2FUMFrRW6hDW4OjZLo5Xq%2BdKzNbT4tQkfkJAbUBSSezi6VqoID2eoCX6x4AhFGlMZC%2BIzDw1vK8BjqkAZecHyhYVgDsD5xmT7oWEMUhiiS9lTmVAw8gXR4c8n6ILiWH5CPjgQzuUDL3gHziazt6usyaT9QgL1UjvyyihY7ieMP1LhH3BVmrT51z%2FY%2FjgdSQIIlMsA0oHCGY9UvKTom41XSYCbs4sMcZI5rD7PaviY0YaFAs%2FXnpQDbSRSoEdwnEaxJ0y3TG8MOmZ8lTFQjauc%2B8ckXF8kvMxsMD26r9H1Ag&X-Amz-Signature=ab52a7c030802957aca5a0a6b97fc65f2c5edc219b0f974c3f31ca4e803744fd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QAIM74VM%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCP%2FSkVbUTnufiJzjMtsYU%2FypnZJHmAptL04dceskGMngIhAN%2Bc%2FuYZyGEQTJXbnNL1KIaLU6T%2FT4eIy1MWZlimwqYQKogECLz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzawFSN3zHhEAKDHTsq3AM3AtOJRFjkjCnR5iXVIquT5jv3StVgpoUO6sKXKK6rPJqDQquHEppSjlT3iVR0CGg1a8EndS80btO%2B1ZUsYOzVcMmDzLYD8CQkymka0dfLbYwNOqZgygrEHMqdzYzycCyWHD1fFMyqJJGJkK%2BAkaZ%2FuW%2BOUUI7pOk1MZY0L4ph4JMT1oShi48kuONn53VljqTwkT66vcAIX6tRIa1SCIOylJgPWx%2Bt9v8D3AJ6H49hJ%2FjIG6OLVQsVNw7qg5bRtX3x%2FHCExdwj8FWWKhjIHZR4Zwgmq6Qlru%2Biwwh1n1Suo%2FqEvfIkxHHlOGkskVAE6%2BQ%2FzLrs5J6mE8bTvcUYjwNPaCCx%2BadJIb07EiDKSqY5n1TlYlfLUlVxe6rTzU%2F0qH2ww39qJAg6OBKEKCMw7Jc3z3RCQ7HVOCh%2B2%2Fx%2FMpKzc%2BPbJfEh824VTBHIt31%2BgjzTe8AOpFyrjYkboD4gm%2BSXGc160dbl3zkN566GpQfkzjnazJ6Yz4TL0N%2BDLy%2FxTy7BlNrGfHpubCSIu1%2Fr7RQHt5YoCgu5eBeDajhj4Ir3%2BRi%2BZWgYeNk%2F4BMoj3vKzBgcLuLEa%2FbJzjrw78ocgDGmANbJNWIeFHvls1%2F9h2sm8MFqiEkGZtrLvJfgXTCt1%2FK8BjqkASOz6i9995702SZNV%2B9CbbNapSB3CGNtCXLPrvbAwLvJU%2BSMtMKN8obInRXm8lbYOWAIxQXsFLqv6%2BuCECs45zxyP%2F5yjc6Uj0vKuSnq9kX9Haj8yjyDflXKUiLikZUljmVwU1%2Bkm4kTZg7uj9UkXxXWtOi1RISfaFPTngnmcOr6u2ZZ01NXNbfX%2B8OjTKAes6LxqPsI8NWhZTRnDVbAyirDTu%2Fo&X-Amz-Signature=e13aaf77c748463f422f16126c6974ed2147e38c4f7a6cce99d9e606d52a086b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XVZJUBA3%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDOpeAwvMtfX7wq3WKA%2BrYuVbOxok4tfR8JO8UVKvcvhwIhAPKXyJMSzkPOPMjI2pUKYZ%2ByTQxNDH4%2B5MWzwKA5hd%2BnKogECLz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwfjQSyn7Jgu3676YYq3AP%2FT2Txi88wSFQrRHxG1fIUaLfMwFeMdUF1rhbdmclUs37lRVZPmnqwZTPtMZF6HBqBop%2B%2FOcjcZpGGUuLFT%2FMAkNrSybiUdj11TIL9k8seS%2BmNWyQ1H1Ovk5HNEHejQY5b79jGvdTwkysIFjj98AxfeOoA3xj8diajYOv89bAmOOlNNEM56OxBaPT6ta94Bo3gSQTkw7hG5hOAg8vMIilO3ByfodsXKpAk1lyflfxdUUmon5cE4%2FlwKGF4AVvtdl6MAo1nuI7SDFa%2BNmnQtYwhKfErh8dOym8Y%2FcV9mTbcUzJp7dXx71vBx3HmkaAabM7ivUPQB4JniaE3w%2B%2F4UBswe3vfNqxq%2FUeVdgcp%2FLkSfj8%2FHENBuP71JUVVBTXQiiLgl8SSnrEHgvEa56uxf3HFE3bdKAwG15vBLmCvdZ94zT%2BuJZ92IPmx89xKIt3TfKRtwJTIUp5VquWfPZDnayb78C3QHD896uE0qh4U7%2FcxIaiweIFFqvWjYBZCfUXEOQsNNCpPSnD1rLoRETrQB8ocN%2Frn6IqFjluYuIxKh4GIH1DIgaseFzz1Fbs92GBo0P8ekGoF4%2BTOm4bVNwW%2FkkCx6%2Fcouw6mDYBiFqEbNzAcRyectrurxCjC4fk6JTC61vK8BjqkAe7sRPkqRbwAbWxg6LwRQXebXHh0avQLCVck9sFYEZlf5Qst79vkef6MDowjEDSLKdhG5CwlKQwDzl0YKiaxENCBNPbjE8TBgMlSqjpyW62my8i1S2FpN0yiH%2Fy4g1%2FgMD5snlIwlGrvb3wJutby1esOzS%2BRBRc4IVrUzagJRNu08gxrK3fjX%2BHCtP6Wdk8NfviLjFK35HBfokC07n0esa7JZ0VH&X-Amz-Signature=0d05935d4c9f461b743df271d19140e072b406aad609f0cb86329b6e181a33ed&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XVZJUBA3%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDOpeAwvMtfX7wq3WKA%2BrYuVbOxok4tfR8JO8UVKvcvhwIhAPKXyJMSzkPOPMjI2pUKYZ%2ByTQxNDH4%2B5MWzwKA5hd%2BnKogECLz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwfjQSyn7Jgu3676YYq3AP%2FT2Txi88wSFQrRHxG1fIUaLfMwFeMdUF1rhbdmclUs37lRVZPmnqwZTPtMZF6HBqBop%2B%2FOcjcZpGGUuLFT%2FMAkNrSybiUdj11TIL9k8seS%2BmNWyQ1H1Ovk5HNEHejQY5b79jGvdTwkysIFjj98AxfeOoA3xj8diajYOv89bAmOOlNNEM56OxBaPT6ta94Bo3gSQTkw7hG5hOAg8vMIilO3ByfodsXKpAk1lyflfxdUUmon5cE4%2FlwKGF4AVvtdl6MAo1nuI7SDFa%2BNmnQtYwhKfErh8dOym8Y%2FcV9mTbcUzJp7dXx71vBx3HmkaAabM7ivUPQB4JniaE3w%2B%2F4UBswe3vfNqxq%2FUeVdgcp%2FLkSfj8%2FHENBuP71JUVVBTXQiiLgl8SSnrEHgvEa56uxf3HFE3bdKAwG15vBLmCvdZ94zT%2BuJZ92IPmx89xKIt3TfKRtwJTIUp5VquWfPZDnayb78C3QHD896uE0qh4U7%2FcxIaiweIFFqvWjYBZCfUXEOQsNNCpPSnD1rLoRETrQB8ocN%2Frn6IqFjluYuIxKh4GIH1DIgaseFzz1Fbs92GBo0P8ekGoF4%2BTOm4bVNwW%2FkkCx6%2Fcouw6mDYBiFqEbNzAcRyectrurxCjC4fk6JTC61vK8BjqkAe7sRPkqRbwAbWxg6LwRQXebXHh0avQLCVck9sFYEZlf5Qst79vkef6MDowjEDSLKdhG5CwlKQwDzl0YKiaxENCBNPbjE8TBgMlSqjpyW62my8i1S2FpN0yiH%2Fy4g1%2FgMD5snlIwlGrvb3wJutby1esOzS%2BRBRc4IVrUzagJRNu08gxrK3fjX%2BHCtP6Wdk8NfviLjFK35HBfokC07n0esa7JZ0VH&X-Amz-Signature=eac53a06f243eb4c59a0dbed072bd31ac09911b31d7eb2a65ffb19ebf1575c18&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XVZJUBA3%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDOpeAwvMtfX7wq3WKA%2BrYuVbOxok4tfR8JO8UVKvcvhwIhAPKXyJMSzkPOPMjI2pUKYZ%2ByTQxNDH4%2B5MWzwKA5hd%2BnKogECLz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwfjQSyn7Jgu3676YYq3AP%2FT2Txi88wSFQrRHxG1fIUaLfMwFeMdUF1rhbdmclUs37lRVZPmnqwZTPtMZF6HBqBop%2B%2FOcjcZpGGUuLFT%2FMAkNrSybiUdj11TIL9k8seS%2BmNWyQ1H1Ovk5HNEHejQY5b79jGvdTwkysIFjj98AxfeOoA3xj8diajYOv89bAmOOlNNEM56OxBaPT6ta94Bo3gSQTkw7hG5hOAg8vMIilO3ByfodsXKpAk1lyflfxdUUmon5cE4%2FlwKGF4AVvtdl6MAo1nuI7SDFa%2BNmnQtYwhKfErh8dOym8Y%2FcV9mTbcUzJp7dXx71vBx3HmkaAabM7ivUPQB4JniaE3w%2B%2F4UBswe3vfNqxq%2FUeVdgcp%2FLkSfj8%2FHENBuP71JUVVBTXQiiLgl8SSnrEHgvEa56uxf3HFE3bdKAwG15vBLmCvdZ94zT%2BuJZ92IPmx89xKIt3TfKRtwJTIUp5VquWfPZDnayb78C3QHD896uE0qh4U7%2FcxIaiweIFFqvWjYBZCfUXEOQsNNCpPSnD1rLoRETrQB8ocN%2Frn6IqFjluYuIxKh4GIH1DIgaseFzz1Fbs92GBo0P8ekGoF4%2BTOm4bVNwW%2FkkCx6%2Fcouw6mDYBiFqEbNzAcRyectrurxCjC4fk6JTC61vK8BjqkAe7sRPkqRbwAbWxg6LwRQXebXHh0avQLCVck9sFYEZlf5Qst79vkef6MDowjEDSLKdhG5CwlKQwDzl0YKiaxENCBNPbjE8TBgMlSqjpyW62my8i1S2FpN0yiH%2Fy4g1%2FgMD5snlIwlGrvb3wJutby1esOzS%2BRBRc4IVrUzagJRNu08gxrK3fjX%2BHCtP6Wdk8NfviLjFK35HBfokC07n0esa7JZ0VH&X-Amz-Signature=66cf6f8266affaaa5060689c0f6d2720da9216f4251cf92542077bea3cbd2a42&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XVZJUBA3%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDOpeAwvMtfX7wq3WKA%2BrYuVbOxok4tfR8JO8UVKvcvhwIhAPKXyJMSzkPOPMjI2pUKYZ%2ByTQxNDH4%2B5MWzwKA5hd%2BnKogECLz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwfjQSyn7Jgu3676YYq3AP%2FT2Txi88wSFQrRHxG1fIUaLfMwFeMdUF1rhbdmclUs37lRVZPmnqwZTPtMZF6HBqBop%2B%2FOcjcZpGGUuLFT%2FMAkNrSybiUdj11TIL9k8seS%2BmNWyQ1H1Ovk5HNEHejQY5b79jGvdTwkysIFjj98AxfeOoA3xj8diajYOv89bAmOOlNNEM56OxBaPT6ta94Bo3gSQTkw7hG5hOAg8vMIilO3ByfodsXKpAk1lyflfxdUUmon5cE4%2FlwKGF4AVvtdl6MAo1nuI7SDFa%2BNmnQtYwhKfErh8dOym8Y%2FcV9mTbcUzJp7dXx71vBx3HmkaAabM7ivUPQB4JniaE3w%2B%2F4UBswe3vfNqxq%2FUeVdgcp%2FLkSfj8%2FHENBuP71JUVVBTXQiiLgl8SSnrEHgvEa56uxf3HFE3bdKAwG15vBLmCvdZ94zT%2BuJZ92IPmx89xKIt3TfKRtwJTIUp5VquWfPZDnayb78C3QHD896uE0qh4U7%2FcxIaiweIFFqvWjYBZCfUXEOQsNNCpPSnD1rLoRETrQB8ocN%2Frn6IqFjluYuIxKh4GIH1DIgaseFzz1Fbs92GBo0P8ekGoF4%2BTOm4bVNwW%2FkkCx6%2Fcouw6mDYBiFqEbNzAcRyectrurxCjC4fk6JTC61vK8BjqkAe7sRPkqRbwAbWxg6LwRQXebXHh0avQLCVck9sFYEZlf5Qst79vkef6MDowjEDSLKdhG5CwlKQwDzl0YKiaxENCBNPbjE8TBgMlSqjpyW62my8i1S2FpN0yiH%2Fy4g1%2FgMD5snlIwlGrvb3wJutby1esOzS%2BRBRc4IVrUzagJRNu08gxrK3fjX%2BHCtP6Wdk8NfviLjFK35HBfokC07n0esa7JZ0VH&X-Amz-Signature=e8146a4d01f1c4a3caafe3f7468f02ac0c537c3d29416c7800d903003eb17e6f&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
