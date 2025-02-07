

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W2PLWK4P%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQC3VjmSMtqsSzTA3URJWzmBMPxdpWtxcR5qAWM2NwiOOQIhAPRNjwE6Ou7SBpUE%2Bq4jrkzTp8zpEeczg4NmL5oaqmJsKv8DCGkQABoMNjM3NDIzMTgzODA1IgxW5%2FMpDdNRFoGjKNwq3AOHMYpPK0MqvXYdPPdtAvdfdSSsVq5Te4W6LMqtd6kZ9y2tbroov2Yv%2BEGp1kg0m4PALPm28BqDlmg5TfkMUD47oMwJb27lfv9pDH3Kxb3ZVT4LpiuO1ONWMWjaowLbRWz8GvZHAoBTWsT0wP26Ls7jPjOcgAm3z%2Fh1G2AWUjbsvUyOqGgG0PhJ0fogEBhA%2BhTvEBiV22Q%2FOfLBfhqEM0VkddpqvIFWzO584LLSsFL0G33cZhQwt%2BSWkQg6OXtrcwAFx%2BRkh%2B5y8zayR6ViKgSoWmmedo81IXtGYuvFsmd5QsuCUQw5Pf7mxqJJ9IpuAAi9k7uMKq2%2FkpxPDd1%2FA5keBfoQN2pwcbCuf4dD3GXeT%2FXebBRwK4vfc%2BZrONTugtxlbttze3Du%2FPRQuUpKIg5WZRiqimyojR9Kpem71WiGpc55XOCEKZ0Djn7UBgCs1sRpRvyX2JN0SeDOVIq4FU5Qudolo90p8wFlgNL46WZunFJULbGV%2FQ2q0Xd5dGVtUUM8C4%2FwpbxDD3nEPdCQiZ8NL%2BW00uqm4HCSGaMkQr0oLpGK82dgkcieGCRElTz2F43NI5IxbIUInE1qXEHscEz93cDfF874S4ACQ%2F5%2BBYRejt7IPvCr7%2F2%2Bque5%2FjCPmpW9BjqkAQK8m8St%2B%2BnZt06wD%2FBxUyV6REZOJcVLXDUEB2jcNdhtrktV75tUCXF8K0xtsKGVRWnzqjPivcpAFxyF%2BbMf2nZ3MQfsPg%2FT3ykT3ysvuc4Rc9c1VObv%2FUf0QLbAq1Hyz0j4NzvDI5hEV7F%2FJ66K3h9gg6CDgkDGBkweks3%2B7xHk1QiYiViZuPw4Ef2k14AgfQ8b%2Buora3r%2B4Q03%2FjQypiXbAXmO&X-Amz-Signature=30e3a3cd1a39022683164290243bf4a0a749a67fee879216de04cfeb10b32d40&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W2PLWK4P%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQC3VjmSMtqsSzTA3URJWzmBMPxdpWtxcR5qAWM2NwiOOQIhAPRNjwE6Ou7SBpUE%2Bq4jrkzTp8zpEeczg4NmL5oaqmJsKv8DCGkQABoMNjM3NDIzMTgzODA1IgxW5%2FMpDdNRFoGjKNwq3AOHMYpPK0MqvXYdPPdtAvdfdSSsVq5Te4W6LMqtd6kZ9y2tbroov2Yv%2BEGp1kg0m4PALPm28BqDlmg5TfkMUD47oMwJb27lfv9pDH3Kxb3ZVT4LpiuO1ONWMWjaowLbRWz8GvZHAoBTWsT0wP26Ls7jPjOcgAm3z%2Fh1G2AWUjbsvUyOqGgG0PhJ0fogEBhA%2BhTvEBiV22Q%2FOfLBfhqEM0VkddpqvIFWzO584LLSsFL0G33cZhQwt%2BSWkQg6OXtrcwAFx%2BRkh%2B5y8zayR6ViKgSoWmmedo81IXtGYuvFsmd5QsuCUQw5Pf7mxqJJ9IpuAAi9k7uMKq2%2FkpxPDd1%2FA5keBfoQN2pwcbCuf4dD3GXeT%2FXebBRwK4vfc%2BZrONTugtxlbttze3Du%2FPRQuUpKIg5WZRiqimyojR9Kpem71WiGpc55XOCEKZ0Djn7UBgCs1sRpRvyX2JN0SeDOVIq4FU5Qudolo90p8wFlgNL46WZunFJULbGV%2FQ2q0Xd5dGVtUUM8C4%2FwpbxDD3nEPdCQiZ8NL%2BW00uqm4HCSGaMkQr0oLpGK82dgkcieGCRElTz2F43NI5IxbIUInE1qXEHscEz93cDfF874S4ACQ%2F5%2BBYRejt7IPvCr7%2F2%2Bque5%2FjCPmpW9BjqkAQK8m8St%2B%2BnZt06wD%2FBxUyV6REZOJcVLXDUEB2jcNdhtrktV75tUCXF8K0xtsKGVRWnzqjPivcpAFxyF%2BbMf2nZ3MQfsPg%2FT3ykT3ysvuc4Rc9c1VObv%2FUf0QLbAq1Hyz0j4NzvDI5hEV7F%2FJ66K3h9gg6CDgkDGBkweks3%2B7xHk1QiYiViZuPw4Ef2k14AgfQ8b%2Buora3r%2B4Q03%2FjQypiXbAXmO&X-Amz-Signature=88596019cdefb7aa1bf3076ededc86ad1aaafd8436b67866774ede8a68f79a15&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W2PLWK4P%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQC3VjmSMtqsSzTA3URJWzmBMPxdpWtxcR5qAWM2NwiOOQIhAPRNjwE6Ou7SBpUE%2Bq4jrkzTp8zpEeczg4NmL5oaqmJsKv8DCGkQABoMNjM3NDIzMTgzODA1IgxW5%2FMpDdNRFoGjKNwq3AOHMYpPK0MqvXYdPPdtAvdfdSSsVq5Te4W6LMqtd6kZ9y2tbroov2Yv%2BEGp1kg0m4PALPm28BqDlmg5TfkMUD47oMwJb27lfv9pDH3Kxb3ZVT4LpiuO1ONWMWjaowLbRWz8GvZHAoBTWsT0wP26Ls7jPjOcgAm3z%2Fh1G2AWUjbsvUyOqGgG0PhJ0fogEBhA%2BhTvEBiV22Q%2FOfLBfhqEM0VkddpqvIFWzO584LLSsFL0G33cZhQwt%2BSWkQg6OXtrcwAFx%2BRkh%2B5y8zayR6ViKgSoWmmedo81IXtGYuvFsmd5QsuCUQw5Pf7mxqJJ9IpuAAi9k7uMKq2%2FkpxPDd1%2FA5keBfoQN2pwcbCuf4dD3GXeT%2FXebBRwK4vfc%2BZrONTugtxlbttze3Du%2FPRQuUpKIg5WZRiqimyojR9Kpem71WiGpc55XOCEKZ0Djn7UBgCs1sRpRvyX2JN0SeDOVIq4FU5Qudolo90p8wFlgNL46WZunFJULbGV%2FQ2q0Xd5dGVtUUM8C4%2FwpbxDD3nEPdCQiZ8NL%2BW00uqm4HCSGaMkQr0oLpGK82dgkcieGCRElTz2F43NI5IxbIUInE1qXEHscEz93cDfF874S4ACQ%2F5%2BBYRejt7IPvCr7%2F2%2Bque5%2FjCPmpW9BjqkAQK8m8St%2B%2BnZt06wD%2FBxUyV6REZOJcVLXDUEB2jcNdhtrktV75tUCXF8K0xtsKGVRWnzqjPivcpAFxyF%2BbMf2nZ3MQfsPg%2FT3ykT3ysvuc4Rc9c1VObv%2FUf0QLbAq1Hyz0j4NzvDI5hEV7F%2FJ66K3h9gg6CDgkDGBkweks3%2B7xHk1QiYiViZuPw4Ef2k14AgfQ8b%2Buora3r%2B4Q03%2FjQypiXbAXmO&X-Amz-Signature=e9f169f00e0beb20e0666880c8e2330555fd875c6db5fb463eeb2860beb310d7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WFIYPQA%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIHgLBTfOxvpTjYvQ%2FI4y6yN98r65syrSPttwRnjmKtyUAiEA0GQuoYSk1V9ImzSf5Q8f6xJ81XN7w%2Bp8Gtnb8s9Kww8q%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDP1aE8igVDNDRQMfHyrcA7CsSOps%2BYGeQ0NWx%2Bv1G7tQz9NHWj3trGxYClvEnlSZjVJUV5ojOYa5iLc2aLM8ciN65V0BopXIbzt6et2c90C8Fx2F7WubVj23kKy2Jm2paEavyIaGIJz6Tt6q3e37LH8ouQ3P35s546eHBnqe4D%2FfEgTOde4ip9QONXAwYjQhS8PFpLZC7K8uTGmL9CXvup4OuEpq6ywGUFlqGgpxtlcYS6YouedJ9jGe3l1DQM266tA5VfpGBIiJ0iBMTsXSHAw6KbMXQeyntWFBkyzdsc7uzALY1oaqJI%2FYN6FzezHS%2FSCV7VszZIos%2BrZetcKEeOTJuMkSlV9u0puI4cD6jX%2F49BAV%2BRPa5pTk%2B26DMfxKvEewv%2BgIbsMsTR2e16wDOyRv6pYZmLzKRfIdSV7VZS%2FQyyV0EgBePTxtZ1ud1Ch0Uz%2F0SnCmpFQQlZB8E%2F6I%2Fa9gxD2wNn%2F6CAUg7rv4iPeEWIiFvzjy1beinUNG0PbpGnCbHLdIqJEoSdYfFkRu5VJ4EJOaFYNTijtrtt1to%2FooM3hU%2BNp6oZFaQU%2BYH8SsEO%2F6Wb85o6UjQ3SkgjIBR8A51yzuoKVWES%2BLNWTIvfQd7I1tUvUuimbUBOKKumKyWjBWBA9qcsL9r3K9MLOalb0GOqUBoKrxrbbPQUapllitHUBtHXmOo7IR2l8IbmbRcZ5srVVnMnE9fs4nhTEtgXGZ3qjuEMuRoVlunoCjz%2Bu05pew9OL%2B5j5p4oAfz7hB9Y60MUKvAg%2F48RVyfdckN5TSx5IEzA4aJH58mI7Zm5UxH14nK6q027PujmYSygd9cPM%2FaAAYZGFf27J%2Bvu2lY05Bp8LlMBTr2dxgtyK%2F0Iano0CQWtc6VUBH&X-Amz-Signature=08c8f8b69bca5e171b9f3ddf20260855d7f1305a9e40f74c3bc9aca6e5847be2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664JMAGOSX%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQCGWuTWJEJAViLuiAoYlh2ByHPljgh4TTDsqAIQod0yrAIhAM9Y9WHnuH1v7l7NnF9KGD5ye63vzlpg6jKJ9eH9v%2Bq7Kv8DCGkQABoMNjM3NDIzMTgzODA1IgyRex01GVjZGdzWwvQq3AP%2FXQrdMYsTzvDd%2BjvsUnUM7MBDpRsgNwX4XkgejFdE0qdC0AF4%2BAA87u%2FbrZYpqtOC3DyceexIrfmzN7qelVS1w3xvlTAVikBtvLK9mLc8%2FOo1zQhFdfqumtYTqNNY9ND9Fq%2FdZVePMKA37ws4c4nabxYBeGAlJEr5UO5TGewLUk3HsPrltgFCZ1LRa8orqz%2BVux6X%2F2Quf%2BDo6kfzDGggimslnbRI4QsPjc5bY4H86j%2F748y%2FWMIrI4vm1mv9rWXwBoMFhQxMmIqeuHqSRcWlMv%2FmfWu5ayIkhRbpvGgc6REGyvsqjr41SIjeA508EUZWzIXX3wlmmNHzAN2wp7ZPJuRAEwpUsiXjFCDMKICsj13Ou06uC3c6HWZNbI%2Bc%2Bmf5FMfFKKz16B%2F87uS2WheDhc2%2FRIjwqDN4AKqOK12Ra1Irkn%2BSc%2BiR4HePrOceSC6OuY9Gi9UMPRxuCyvS2%2Ff7pO7cldM%2F5DqSrTWKRvRLMVH%2FX3BEkn3wt3zFHpy2oGDkU6K%2Fo%2Bs2mu2qM%2FJC01xrmDdfrD3O4StTpB2KOk8Ymi1NaqlsyQ%2FblOvv05lY1EThpFr837RJPdMZk1qgpTsQ%2B4NyMDusZ1g8%2B1%2FrPIu%2Bo4CZ0nTNwcq1HNFJPzDkmZW9BjqkAZ4FVjueyY2f%2BIsJtkBk8C%2BZFUcO4dGA2K2DgEu5XGuuEeyrhka7wmmTpMffd9yJ38grnDrtYwNJfSaqRM7T6m45tH%2FSOMDs%2BGBDsChwC1t6N1WRfmRp0%2BpvFVqqW9f7KXNeoWrajH8sr6kYX4PX2JAk6ABcJd7gDqeaXIs6UNUg7FFKU7riWJaRADkTZdLRMA4e69jgTUoq5W6oTxmeKBu%2FR5o7&X-Amz-Signature=7ff7a032db01dc2d49cc787ea8f7feb85649d07d52714e749216e564c5eba526&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W2PLWK4P%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQC3VjmSMtqsSzTA3URJWzmBMPxdpWtxcR5qAWM2NwiOOQIhAPRNjwE6Ou7SBpUE%2Bq4jrkzTp8zpEeczg4NmL5oaqmJsKv8DCGkQABoMNjM3NDIzMTgzODA1IgxW5%2FMpDdNRFoGjKNwq3AOHMYpPK0MqvXYdPPdtAvdfdSSsVq5Te4W6LMqtd6kZ9y2tbroov2Yv%2BEGp1kg0m4PALPm28BqDlmg5TfkMUD47oMwJb27lfv9pDH3Kxb3ZVT4LpiuO1ONWMWjaowLbRWz8GvZHAoBTWsT0wP26Ls7jPjOcgAm3z%2Fh1G2AWUjbsvUyOqGgG0PhJ0fogEBhA%2BhTvEBiV22Q%2FOfLBfhqEM0VkddpqvIFWzO584LLSsFL0G33cZhQwt%2BSWkQg6OXtrcwAFx%2BRkh%2B5y8zayR6ViKgSoWmmedo81IXtGYuvFsmd5QsuCUQw5Pf7mxqJJ9IpuAAi9k7uMKq2%2FkpxPDd1%2FA5keBfoQN2pwcbCuf4dD3GXeT%2FXebBRwK4vfc%2BZrONTugtxlbttze3Du%2FPRQuUpKIg5WZRiqimyojR9Kpem71WiGpc55XOCEKZ0Djn7UBgCs1sRpRvyX2JN0SeDOVIq4FU5Qudolo90p8wFlgNL46WZunFJULbGV%2FQ2q0Xd5dGVtUUM8C4%2FwpbxDD3nEPdCQiZ8NL%2BW00uqm4HCSGaMkQr0oLpGK82dgkcieGCRElTz2F43NI5IxbIUInE1qXEHscEz93cDfF874S4ACQ%2F5%2BBYRejt7IPvCr7%2F2%2Bque5%2FjCPmpW9BjqkAQK8m8St%2B%2BnZt06wD%2FBxUyV6REZOJcVLXDUEB2jcNdhtrktV75tUCXF8K0xtsKGVRWnzqjPivcpAFxyF%2BbMf2nZ3MQfsPg%2FT3ykT3ysvuc4Rc9c1VObv%2FUf0QLbAq1Hyz0j4NzvDI5hEV7F%2FJ66K3h9gg6CDgkDGBkweks3%2B7xHk1QiYiViZuPw4Ef2k14AgfQ8b%2Buora3r%2B4Q03%2FjQypiXbAXmO&X-Amz-Signature=149ce8540266398ac563a4316e9af93937729e0c0c643bc4575b4ee8cc3da356&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W2PLWK4P%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQC3VjmSMtqsSzTA3URJWzmBMPxdpWtxcR5qAWM2NwiOOQIhAPRNjwE6Ou7SBpUE%2Bq4jrkzTp8zpEeczg4NmL5oaqmJsKv8DCGkQABoMNjM3NDIzMTgzODA1IgxW5%2FMpDdNRFoGjKNwq3AOHMYpPK0MqvXYdPPdtAvdfdSSsVq5Te4W6LMqtd6kZ9y2tbroov2Yv%2BEGp1kg0m4PALPm28BqDlmg5TfkMUD47oMwJb27lfv9pDH3Kxb3ZVT4LpiuO1ONWMWjaowLbRWz8GvZHAoBTWsT0wP26Ls7jPjOcgAm3z%2Fh1G2AWUjbsvUyOqGgG0PhJ0fogEBhA%2BhTvEBiV22Q%2FOfLBfhqEM0VkddpqvIFWzO584LLSsFL0G33cZhQwt%2BSWkQg6OXtrcwAFx%2BRkh%2B5y8zayR6ViKgSoWmmedo81IXtGYuvFsmd5QsuCUQw5Pf7mxqJJ9IpuAAi9k7uMKq2%2FkpxPDd1%2FA5keBfoQN2pwcbCuf4dD3GXeT%2FXebBRwK4vfc%2BZrONTugtxlbttze3Du%2FPRQuUpKIg5WZRiqimyojR9Kpem71WiGpc55XOCEKZ0Djn7UBgCs1sRpRvyX2JN0SeDOVIq4FU5Qudolo90p8wFlgNL46WZunFJULbGV%2FQ2q0Xd5dGVtUUM8C4%2FwpbxDD3nEPdCQiZ8NL%2BW00uqm4HCSGaMkQr0oLpGK82dgkcieGCRElTz2F43NI5IxbIUInE1qXEHscEz93cDfF874S4ACQ%2F5%2BBYRejt7IPvCr7%2F2%2Bque5%2FjCPmpW9BjqkAQK8m8St%2B%2BnZt06wD%2FBxUyV6REZOJcVLXDUEB2jcNdhtrktV75tUCXF8K0xtsKGVRWnzqjPivcpAFxyF%2BbMf2nZ3MQfsPg%2FT3ykT3ysvuc4Rc9c1VObv%2FUf0QLbAq1Hyz0j4NzvDI5hEV7F%2FJ66K3h9gg6CDgkDGBkweks3%2B7xHk1QiYiViZuPw4Ef2k14AgfQ8b%2Buora3r%2B4Q03%2FjQypiXbAXmO&X-Amz-Signature=bcb6cef910a56903f770a8c1b5bf137bd1854ffd7bbfd3099a581f3041b92f4c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W2PLWK4P%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQC3VjmSMtqsSzTA3URJWzmBMPxdpWtxcR5qAWM2NwiOOQIhAPRNjwE6Ou7SBpUE%2Bq4jrkzTp8zpEeczg4NmL5oaqmJsKv8DCGkQABoMNjM3NDIzMTgzODA1IgxW5%2FMpDdNRFoGjKNwq3AOHMYpPK0MqvXYdPPdtAvdfdSSsVq5Te4W6LMqtd6kZ9y2tbroov2Yv%2BEGp1kg0m4PALPm28BqDlmg5TfkMUD47oMwJb27lfv9pDH3Kxb3ZVT4LpiuO1ONWMWjaowLbRWz8GvZHAoBTWsT0wP26Ls7jPjOcgAm3z%2Fh1G2AWUjbsvUyOqGgG0PhJ0fogEBhA%2BhTvEBiV22Q%2FOfLBfhqEM0VkddpqvIFWzO584LLSsFL0G33cZhQwt%2BSWkQg6OXtrcwAFx%2BRkh%2B5y8zayR6ViKgSoWmmedo81IXtGYuvFsmd5QsuCUQw5Pf7mxqJJ9IpuAAi9k7uMKq2%2FkpxPDd1%2FA5keBfoQN2pwcbCuf4dD3GXeT%2FXebBRwK4vfc%2BZrONTugtxlbttze3Du%2FPRQuUpKIg5WZRiqimyojR9Kpem71WiGpc55XOCEKZ0Djn7UBgCs1sRpRvyX2JN0SeDOVIq4FU5Qudolo90p8wFlgNL46WZunFJULbGV%2FQ2q0Xd5dGVtUUM8C4%2FwpbxDD3nEPdCQiZ8NL%2BW00uqm4HCSGaMkQr0oLpGK82dgkcieGCRElTz2F43NI5IxbIUInE1qXEHscEz93cDfF874S4ACQ%2F5%2BBYRejt7IPvCr7%2F2%2Bque5%2FjCPmpW9BjqkAQK8m8St%2B%2BnZt06wD%2FBxUyV6REZOJcVLXDUEB2jcNdhtrktV75tUCXF8K0xtsKGVRWnzqjPivcpAFxyF%2BbMf2nZ3MQfsPg%2FT3ykT3ysvuc4Rc9c1VObv%2FUf0QLbAq1Hyz0j4NzvDI5hEV7F%2FJ66K3h9gg6CDgkDGBkweks3%2B7xHk1QiYiViZuPw4Ef2k14AgfQ8b%2Buora3r%2B4Q03%2FjQypiXbAXmO&X-Amz-Signature=a8b37d3b146897d146cc86a9e39149bdb03627c34a3a06c94503c7cc47df154e&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W2PLWK4P%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQC3VjmSMtqsSzTA3URJWzmBMPxdpWtxcR5qAWM2NwiOOQIhAPRNjwE6Ou7SBpUE%2Bq4jrkzTp8zpEeczg4NmL5oaqmJsKv8DCGkQABoMNjM3NDIzMTgzODA1IgxW5%2FMpDdNRFoGjKNwq3AOHMYpPK0MqvXYdPPdtAvdfdSSsVq5Te4W6LMqtd6kZ9y2tbroov2Yv%2BEGp1kg0m4PALPm28BqDlmg5TfkMUD47oMwJb27lfv9pDH3Kxb3ZVT4LpiuO1ONWMWjaowLbRWz8GvZHAoBTWsT0wP26Ls7jPjOcgAm3z%2Fh1G2AWUjbsvUyOqGgG0PhJ0fogEBhA%2BhTvEBiV22Q%2FOfLBfhqEM0VkddpqvIFWzO584LLSsFL0G33cZhQwt%2BSWkQg6OXtrcwAFx%2BRkh%2B5y8zayR6ViKgSoWmmedo81IXtGYuvFsmd5QsuCUQw5Pf7mxqJJ9IpuAAi9k7uMKq2%2FkpxPDd1%2FA5keBfoQN2pwcbCuf4dD3GXeT%2FXebBRwK4vfc%2BZrONTugtxlbttze3Du%2FPRQuUpKIg5WZRiqimyojR9Kpem71WiGpc55XOCEKZ0Djn7UBgCs1sRpRvyX2JN0SeDOVIq4FU5Qudolo90p8wFlgNL46WZunFJULbGV%2FQ2q0Xd5dGVtUUM8C4%2FwpbxDD3nEPdCQiZ8NL%2BW00uqm4HCSGaMkQr0oLpGK82dgkcieGCRElTz2F43NI5IxbIUInE1qXEHscEz93cDfF874S4ACQ%2F5%2BBYRejt7IPvCr7%2F2%2Bque5%2FjCPmpW9BjqkAQK8m8St%2B%2BnZt06wD%2FBxUyV6REZOJcVLXDUEB2jcNdhtrktV75tUCXF8K0xtsKGVRWnzqjPivcpAFxyF%2BbMf2nZ3MQfsPg%2FT3ykT3ysvuc4Rc9c1VObv%2FUf0QLbAq1Hyz0j4NzvDI5hEV7F%2FJ66K3h9gg6CDgkDGBkweks3%2B7xHk1QiYiViZuPw4Ef2k14AgfQ8b%2Buora3r%2B4Q03%2FjQypiXbAXmO&X-Amz-Signature=ee7855ad031cf4ab45172395104fcbdbf70725534ee80b2d576331d1a086fbb2&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
