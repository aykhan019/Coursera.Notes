

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R34OABEK%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJHMEUCIEgSHjfZUfjgvdTJwxv0jrC%2B8CCmpGBvbSym0arfVBL1AiEArVqRrf%2FgOxh%2BJe5D5fUjp06O2KpJOb5HSgQ1qWx5l3Qq%2FwMIHRAAGgw2Mzc0MjMxODM4MDUiDH9V%2Bg4dX0vqU%2F1uVyrcA8FN1sBNKrnx1M1vRlk8hYqSNnOS4jeVRRI%2B5tuNIeQ1AkvhFlHvwOo2xYle1oA6ryrexE5CPtFNNjrIUoquSZFUGONJjKC6CCR500EZ2O2u0aEmXSo%2Fe%2BygoBA3yTopUIaK%2Bf2fcplQO7DcEe8za7M36388M%2Fa60xI%2BNeR2bRd%2B%2Bkh%2B4EUn6e03E%2Fme9pKiCwvhBeIDTZ6sI6l7%2FgsfNGi%2FfUwREC3F45sZL6xmXxAyUNqHHDFOw2wdUR1DsKsjpCt7%2BVQ3et4YCAuUsCT%2BJydcapxMLk1BmeW5Hm15HvI1hNCsbw1X7BzkeuM54D4%2FuzB%2B6XXNWpAvnDmTYfcbXc5vdUn9bNpYmtrrhfAyJqgR4NpdfZRGD6jOP3S6ofZbzhWjaefsRFarE%2FzPhkzNJkxxrqrQUa4gp3LgRTwqY1uQiCj7FFj4GlgqCYKOGYUlPrpGpnIHraK1vBIPohMqnsGROpEZ8LyvlYDsozEb7moUqwwQBSLEbAFSZ9Hl3VsQCz%2BVANHxLjhBWvdWZP62YWVzJwxOatx8TpC%2BMW2%2BMzpFu8ZJ3%2Fi3hiEY6TC5vDVbcM4dLr2KPaNzj2Plet0XLMWsX84QoXYARNpFDORUwwkIpR1F6bt7CiZdCYfMMJ%2B9hL0GOqUBUKj7IgpyL2k6Ihx5dJm8c0kY1VFFOZnhTxj252aGjfJJG5SPcM2ey%2F0ICA9pA67QLMW46N3MOMNTCiVC57%2Fe4R9TwJPkm%2BfyjBKUqyhBz6HpZWnNrr5C%2FJx%2B0krzAlqnxMasS0X7AnU1vcGBviIxli5%2FG9ldJxEa9OfPPAOXqc6GuOZuILnsDajVq6nN3oQw0KEH9aJNJCuBf%2Fg35kp0QLNuEicZ&X-Amz-Signature=a7c76f39ad381fbef5ec50401ac8077a5a4d7e19b7d16dc7e3cabf00b388aa19&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R34OABEK%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJHMEUCIEgSHjfZUfjgvdTJwxv0jrC%2B8CCmpGBvbSym0arfVBL1AiEArVqRrf%2FgOxh%2BJe5D5fUjp06O2KpJOb5HSgQ1qWx5l3Qq%2FwMIHRAAGgw2Mzc0MjMxODM4MDUiDH9V%2Bg4dX0vqU%2F1uVyrcA8FN1sBNKrnx1M1vRlk8hYqSNnOS4jeVRRI%2B5tuNIeQ1AkvhFlHvwOo2xYle1oA6ryrexE5CPtFNNjrIUoquSZFUGONJjKC6CCR500EZ2O2u0aEmXSo%2Fe%2BygoBA3yTopUIaK%2Bf2fcplQO7DcEe8za7M36388M%2Fa60xI%2BNeR2bRd%2B%2Bkh%2B4EUn6e03E%2Fme9pKiCwvhBeIDTZ6sI6l7%2FgsfNGi%2FfUwREC3F45sZL6xmXxAyUNqHHDFOw2wdUR1DsKsjpCt7%2BVQ3et4YCAuUsCT%2BJydcapxMLk1BmeW5Hm15HvI1hNCsbw1X7BzkeuM54D4%2FuzB%2B6XXNWpAvnDmTYfcbXc5vdUn9bNpYmtrrhfAyJqgR4NpdfZRGD6jOP3S6ofZbzhWjaefsRFarE%2FzPhkzNJkxxrqrQUa4gp3LgRTwqY1uQiCj7FFj4GlgqCYKOGYUlPrpGpnIHraK1vBIPohMqnsGROpEZ8LyvlYDsozEb7moUqwwQBSLEbAFSZ9Hl3VsQCz%2BVANHxLjhBWvdWZP62YWVzJwxOatx8TpC%2BMW2%2BMzpFu8ZJ3%2Fi3hiEY6TC5vDVbcM4dLr2KPaNzj2Plet0XLMWsX84QoXYARNpFDORUwwkIpR1F6bt7CiZdCYfMMJ%2B9hL0GOqUBUKj7IgpyL2k6Ihx5dJm8c0kY1VFFOZnhTxj252aGjfJJG5SPcM2ey%2F0ICA9pA67QLMW46N3MOMNTCiVC57%2Fe4R9TwJPkm%2BfyjBKUqyhBz6HpZWnNrr5C%2FJx%2B0krzAlqnxMasS0X7AnU1vcGBviIxli5%2FG9ldJxEa9OfPPAOXqc6GuOZuILnsDajVq6nN3oQw0KEH9aJNJCuBf%2Fg35kp0QLNuEicZ&X-Amz-Signature=4d5bbb6619d95b72508d0b5b3a082e1b669ea8f5c3c79836b8b734ad3bee4d52&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R34OABEK%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJHMEUCIEgSHjfZUfjgvdTJwxv0jrC%2B8CCmpGBvbSym0arfVBL1AiEArVqRrf%2FgOxh%2BJe5D5fUjp06O2KpJOb5HSgQ1qWx5l3Qq%2FwMIHRAAGgw2Mzc0MjMxODM4MDUiDH9V%2Bg4dX0vqU%2F1uVyrcA8FN1sBNKrnx1M1vRlk8hYqSNnOS4jeVRRI%2B5tuNIeQ1AkvhFlHvwOo2xYle1oA6ryrexE5CPtFNNjrIUoquSZFUGONJjKC6CCR500EZ2O2u0aEmXSo%2Fe%2BygoBA3yTopUIaK%2Bf2fcplQO7DcEe8za7M36388M%2Fa60xI%2BNeR2bRd%2B%2Bkh%2B4EUn6e03E%2Fme9pKiCwvhBeIDTZ6sI6l7%2FgsfNGi%2FfUwREC3F45sZL6xmXxAyUNqHHDFOw2wdUR1DsKsjpCt7%2BVQ3et4YCAuUsCT%2BJydcapxMLk1BmeW5Hm15HvI1hNCsbw1X7BzkeuM54D4%2FuzB%2B6XXNWpAvnDmTYfcbXc5vdUn9bNpYmtrrhfAyJqgR4NpdfZRGD6jOP3S6ofZbzhWjaefsRFarE%2FzPhkzNJkxxrqrQUa4gp3LgRTwqY1uQiCj7FFj4GlgqCYKOGYUlPrpGpnIHraK1vBIPohMqnsGROpEZ8LyvlYDsozEb7moUqwwQBSLEbAFSZ9Hl3VsQCz%2BVANHxLjhBWvdWZP62YWVzJwxOatx8TpC%2BMW2%2BMzpFu8ZJ3%2Fi3hiEY6TC5vDVbcM4dLr2KPaNzj2Plet0XLMWsX84QoXYARNpFDORUwwkIpR1F6bt7CiZdCYfMMJ%2B9hL0GOqUBUKj7IgpyL2k6Ihx5dJm8c0kY1VFFOZnhTxj252aGjfJJG5SPcM2ey%2F0ICA9pA67QLMW46N3MOMNTCiVC57%2Fe4R9TwJPkm%2BfyjBKUqyhBz6HpZWnNrr5C%2FJx%2B0krzAlqnxMasS0X7AnU1vcGBviIxli5%2FG9ldJxEa9OfPPAOXqc6GuOZuILnsDajVq6nN3oQw0KEH9aJNJCuBf%2Fg35kp0QLNuEicZ&X-Amz-Signature=44b3aa5c7f9460bd1b0a82e39e0e1fdbb5c0f369208d28c9d50c46b4e1082b07&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663M6RJEGH%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJIMEYCIQCzNEN3zKLjRS4%2BKqpY68ihC8HVAiCPWTDouek%2BGil2iAIhANvLDB74jEXHe6gWyhUzkWhsYHNXLb2iD8abSkAe5HzdKv8DCB0QABoMNjM3NDIzMTgzODA1Igxas%2BdU1w9hX56gOpkq3AMdJNavLr0ZaH9afO7aBMXLP%2FCxI2K3iF7zEXujXwtl1lj93KQBe57AtOhV%2FOuwr0NNySoXGatMsyzXspIwiU2FpwqCpi5iZkCo0htHhnnCnmW8SN9em0FW%2F7y6K8jDPShI2EY5IBsuLFoFiu5wXFABSVySBms0ximhoMXa5UUl84BJrpV4EndawLdfbG%2FAyFI9DW1zeLSVKcUhf9rsHIj0UdssFaYkCAk25sLULdcaXDpr2DqM8EmrgHh3d%2BVji%2BgQ6aU2tidKAKf93yD6YvMFnBMxxIfSe9B10oW9Gof%2FkLnb1D%2Bvv0%2FSII99pcdjxdcsOkdRWjgSFU%2FPF6Ai77PpQJvg9RoxZfZbLKrR12RRphhITvdHqbrTPw5i8G12%2BnQKQrIyq8i2ws1kXnb3%2BamERHJBlcR28egODX%2FC0FBMklznI2JoPJFpNYUIiiy6d1ek08An6NjBMt%2FlfepNWyy%2FsGZa7%2BXTWLc8DYrJ5z2ws74o94H9v4FThh7ZPAAr%2BymwZ6HjMDyz3CTDqynnL4QMFTiOBh2GSCcFmTtk9tZ1cvvVRkan7xjtFAJPp%2BEpX8EKgdmZOEmq4ha%2FcOR2nsyf%2B7j4UaOZee7w1GmR5FWwsZ9uGxHYzGLy4s1KqDDzvIS9BjqkAaIN56i8Nj7V%2B%2FsWEonGNPMyD8VjkEnJVAmsXMt%2BS3aH7WfsPN0F5TF4eXldX8hYn8D5FgrZV0CCvt7uoWt8mo30TEgXu5gOpQBtT3LXy0w58%2Bz%2BZOHS8uNsbvSRNSZQ4EXZRrE%2BTQ4tmWdWcNtSORn9M3aGAMFOWjEESRmMwtn9gpmyZCvlZvKqAhm4yeOSRCSZjrGBY%2B8I24mYPgvR%2Fnj%2BLckE&X-Amz-Signature=c5da46c0e60de173967696455e9b4cf51e36e9be2e8a85494c9c8a22f92cc4db&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RLM4RI5B%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJIMEYCIQCFvmf3vlsXIWXmjIsgdbo7BFnzdJ1Gt5mXERL2Y0Zc5AIhALuywOgms2HqIZnXw7xL%2FuLpVgEnwfVxpFcZjdRlf7R8Kv8DCB0QABoMNjM3NDIzMTgzODA1IgwtD1jBfFnFSEipXnsq3AME2JM1UkiJ9IfOp4cBRdcEhN%2BZv6xrm7aTx1n7oz6Xwll5bDpLjAWzNdG5xUQ5Y6QgIb2MKQx%2ByOL4HpCR37824Rm2orBYj3XnDrb52yl6%2FgB4GYziQ%2Bwzm9LeYzm5M62EwLU3BU4pDmrro5kM9o%2BkslmDwGpwHG7%2FToo5Idg9g0dD50VlIawWKgx1WS5Z6bhGaGF6UDDtqq7Ok4InGEXHd7qoNWNYwZKy%2F616%2BDcfKV4HvSmVyGT9diB60a5Eumq2PE8e0EBO1hAyEggi%2FnIY6lwPMgiGB7F0hVUT4HLLEuVSL%2FKsiHuqAXG12s6ZExInQhsXcpj5DetT%2BNqKPz5L4ei7RacrLlB0lCL0gXvgi8lv1ZaBp2F%2FpF5qvtx7Z7o%2BinBMZBroKRwqPXobx3e%2BhKRpvkOL5wpW0ufr8a6rSTDJafTfTYoHyjUXKwHpbYuTfre%2FxqYVADfMAtPn70sapp1tG%2FvwuKdbmRlQIfqW0YlClJB7S7PEBmE9Msw1jquwgWtumQFgiZvt0Ssn0Be0szpIk8EPIgoi8EN0G8kmab6C1%2FSbY0z5X26LoJaQzYNTWwvO6g4eudneHJ4bEnkifloI1Wqu%2F3HXnKz8eK%2BTCh1zYGqBir6TZkXj2zCdvYS9BjqkAWg%2FweirpN31Dzbq6U%2B%2BpIB8b3LsrWlU22kP9datZV3N7SlIksgFKHsrTYQBVfe%2BrHDTp6Sk6XGHgJA4hXUOHqRi%2FbTfff4JidLC8cLn0tdaVAzl39Laj15y9GmilNs%2BvsQp%2B05%2FUgFxsL2iGb%2BTxc3MVRWzZb1XYaWPAtINh22KrjYrXcXMaRlcYiFaeuSn1geOMQL32tsDngZrMeBDbqMG3D%2FN&X-Amz-Signature=3b9199028a3c02ef63a3df78cc4aa7e05aac4507dde567c73fac9c5402317ff8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R34OABEK%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJHMEUCIEgSHjfZUfjgvdTJwxv0jrC%2B8CCmpGBvbSym0arfVBL1AiEArVqRrf%2FgOxh%2BJe5D5fUjp06O2KpJOb5HSgQ1qWx5l3Qq%2FwMIHRAAGgw2Mzc0MjMxODM4MDUiDH9V%2Bg4dX0vqU%2F1uVyrcA8FN1sBNKrnx1M1vRlk8hYqSNnOS4jeVRRI%2B5tuNIeQ1AkvhFlHvwOo2xYle1oA6ryrexE5CPtFNNjrIUoquSZFUGONJjKC6CCR500EZ2O2u0aEmXSo%2Fe%2BygoBA3yTopUIaK%2Bf2fcplQO7DcEe8za7M36388M%2Fa60xI%2BNeR2bRd%2B%2Bkh%2B4EUn6e03E%2Fme9pKiCwvhBeIDTZ6sI6l7%2FgsfNGi%2FfUwREC3F45sZL6xmXxAyUNqHHDFOw2wdUR1DsKsjpCt7%2BVQ3et4YCAuUsCT%2BJydcapxMLk1BmeW5Hm15HvI1hNCsbw1X7BzkeuM54D4%2FuzB%2B6XXNWpAvnDmTYfcbXc5vdUn9bNpYmtrrhfAyJqgR4NpdfZRGD6jOP3S6ofZbzhWjaefsRFarE%2FzPhkzNJkxxrqrQUa4gp3LgRTwqY1uQiCj7FFj4GlgqCYKOGYUlPrpGpnIHraK1vBIPohMqnsGROpEZ8LyvlYDsozEb7moUqwwQBSLEbAFSZ9Hl3VsQCz%2BVANHxLjhBWvdWZP62YWVzJwxOatx8TpC%2BMW2%2BMzpFu8ZJ3%2Fi3hiEY6TC5vDVbcM4dLr2KPaNzj2Plet0XLMWsX84QoXYARNpFDORUwwkIpR1F6bt7CiZdCYfMMJ%2B9hL0GOqUBUKj7IgpyL2k6Ihx5dJm8c0kY1VFFOZnhTxj252aGjfJJG5SPcM2ey%2F0ICA9pA67QLMW46N3MOMNTCiVC57%2Fe4R9TwJPkm%2BfyjBKUqyhBz6HpZWnNrr5C%2FJx%2B0krzAlqnxMasS0X7AnU1vcGBviIxli5%2FG9ldJxEa9OfPPAOXqc6GuOZuILnsDajVq6nN3oQw0KEH9aJNJCuBf%2Fg35kp0QLNuEicZ&X-Amz-Signature=f497702b838e924c71292281ad6311a6c0d4a105d62c9d8523b5fc8d3bed4c9b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R34OABEK%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJHMEUCIEgSHjfZUfjgvdTJwxv0jrC%2B8CCmpGBvbSym0arfVBL1AiEArVqRrf%2FgOxh%2BJe5D5fUjp06O2KpJOb5HSgQ1qWx5l3Qq%2FwMIHRAAGgw2Mzc0MjMxODM4MDUiDH9V%2Bg4dX0vqU%2F1uVyrcA8FN1sBNKrnx1M1vRlk8hYqSNnOS4jeVRRI%2B5tuNIeQ1AkvhFlHvwOo2xYle1oA6ryrexE5CPtFNNjrIUoquSZFUGONJjKC6CCR500EZ2O2u0aEmXSo%2Fe%2BygoBA3yTopUIaK%2Bf2fcplQO7DcEe8za7M36388M%2Fa60xI%2BNeR2bRd%2B%2Bkh%2B4EUn6e03E%2Fme9pKiCwvhBeIDTZ6sI6l7%2FgsfNGi%2FfUwREC3F45sZL6xmXxAyUNqHHDFOw2wdUR1DsKsjpCt7%2BVQ3et4YCAuUsCT%2BJydcapxMLk1BmeW5Hm15HvI1hNCsbw1X7BzkeuM54D4%2FuzB%2B6XXNWpAvnDmTYfcbXc5vdUn9bNpYmtrrhfAyJqgR4NpdfZRGD6jOP3S6ofZbzhWjaefsRFarE%2FzPhkzNJkxxrqrQUa4gp3LgRTwqY1uQiCj7FFj4GlgqCYKOGYUlPrpGpnIHraK1vBIPohMqnsGROpEZ8LyvlYDsozEb7moUqwwQBSLEbAFSZ9Hl3VsQCz%2BVANHxLjhBWvdWZP62YWVzJwxOatx8TpC%2BMW2%2BMzpFu8ZJ3%2Fi3hiEY6TC5vDVbcM4dLr2KPaNzj2Plet0XLMWsX84QoXYARNpFDORUwwkIpR1F6bt7CiZdCYfMMJ%2B9hL0GOqUBUKj7IgpyL2k6Ihx5dJm8c0kY1VFFOZnhTxj252aGjfJJG5SPcM2ey%2F0ICA9pA67QLMW46N3MOMNTCiVC57%2Fe4R9TwJPkm%2BfyjBKUqyhBz6HpZWnNrr5C%2FJx%2B0krzAlqnxMasS0X7AnU1vcGBviIxli5%2FG9ldJxEa9OfPPAOXqc6GuOZuILnsDajVq6nN3oQw0KEH9aJNJCuBf%2Fg35kp0QLNuEicZ&X-Amz-Signature=b58ff0707c09927f8628f039ec126afbb4322cc6e0a4fc71a852c0f4b6548254&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R34OABEK%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJHMEUCIEgSHjfZUfjgvdTJwxv0jrC%2B8CCmpGBvbSym0arfVBL1AiEArVqRrf%2FgOxh%2BJe5D5fUjp06O2KpJOb5HSgQ1qWx5l3Qq%2FwMIHRAAGgw2Mzc0MjMxODM4MDUiDH9V%2Bg4dX0vqU%2F1uVyrcA8FN1sBNKrnx1M1vRlk8hYqSNnOS4jeVRRI%2B5tuNIeQ1AkvhFlHvwOo2xYle1oA6ryrexE5CPtFNNjrIUoquSZFUGONJjKC6CCR500EZ2O2u0aEmXSo%2Fe%2BygoBA3yTopUIaK%2Bf2fcplQO7DcEe8za7M36388M%2Fa60xI%2BNeR2bRd%2B%2Bkh%2B4EUn6e03E%2Fme9pKiCwvhBeIDTZ6sI6l7%2FgsfNGi%2FfUwREC3F45sZL6xmXxAyUNqHHDFOw2wdUR1DsKsjpCt7%2BVQ3et4YCAuUsCT%2BJydcapxMLk1BmeW5Hm15HvI1hNCsbw1X7BzkeuM54D4%2FuzB%2B6XXNWpAvnDmTYfcbXc5vdUn9bNpYmtrrhfAyJqgR4NpdfZRGD6jOP3S6ofZbzhWjaefsRFarE%2FzPhkzNJkxxrqrQUa4gp3LgRTwqY1uQiCj7FFj4GlgqCYKOGYUlPrpGpnIHraK1vBIPohMqnsGROpEZ8LyvlYDsozEb7moUqwwQBSLEbAFSZ9Hl3VsQCz%2BVANHxLjhBWvdWZP62YWVzJwxOatx8TpC%2BMW2%2BMzpFu8ZJ3%2Fi3hiEY6TC5vDVbcM4dLr2KPaNzj2Plet0XLMWsX84QoXYARNpFDORUwwkIpR1F6bt7CiZdCYfMMJ%2B9hL0GOqUBUKj7IgpyL2k6Ihx5dJm8c0kY1VFFOZnhTxj252aGjfJJG5SPcM2ey%2F0ICA9pA67QLMW46N3MOMNTCiVC57%2Fe4R9TwJPkm%2BfyjBKUqyhBz6HpZWnNrr5C%2FJx%2B0krzAlqnxMasS0X7AnU1vcGBviIxli5%2FG9ldJxEa9OfPPAOXqc6GuOZuILnsDajVq6nN3oQw0KEH9aJNJCuBf%2Fg35kp0QLNuEicZ&X-Amz-Signature=b3ca38098260133da7d3b8329c42cc580b5a3dcb5d482422f5b05e22a5917c06&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R34OABEK%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJHMEUCIEgSHjfZUfjgvdTJwxv0jrC%2B8CCmpGBvbSym0arfVBL1AiEArVqRrf%2FgOxh%2BJe5D5fUjp06O2KpJOb5HSgQ1qWx5l3Qq%2FwMIHRAAGgw2Mzc0MjMxODM4MDUiDH9V%2Bg4dX0vqU%2F1uVyrcA8FN1sBNKrnx1M1vRlk8hYqSNnOS4jeVRRI%2B5tuNIeQ1AkvhFlHvwOo2xYle1oA6ryrexE5CPtFNNjrIUoquSZFUGONJjKC6CCR500EZ2O2u0aEmXSo%2Fe%2BygoBA3yTopUIaK%2Bf2fcplQO7DcEe8za7M36388M%2Fa60xI%2BNeR2bRd%2B%2Bkh%2B4EUn6e03E%2Fme9pKiCwvhBeIDTZ6sI6l7%2FgsfNGi%2FfUwREC3F45sZL6xmXxAyUNqHHDFOw2wdUR1DsKsjpCt7%2BVQ3et4YCAuUsCT%2BJydcapxMLk1BmeW5Hm15HvI1hNCsbw1X7BzkeuM54D4%2FuzB%2B6XXNWpAvnDmTYfcbXc5vdUn9bNpYmtrrhfAyJqgR4NpdfZRGD6jOP3S6ofZbzhWjaefsRFarE%2FzPhkzNJkxxrqrQUa4gp3LgRTwqY1uQiCj7FFj4GlgqCYKOGYUlPrpGpnIHraK1vBIPohMqnsGROpEZ8LyvlYDsozEb7moUqwwQBSLEbAFSZ9Hl3VsQCz%2BVANHxLjhBWvdWZP62YWVzJwxOatx8TpC%2BMW2%2BMzpFu8ZJ3%2Fi3hiEY6TC5vDVbcM4dLr2KPaNzj2Plet0XLMWsX84QoXYARNpFDORUwwkIpR1F6bt7CiZdCYfMMJ%2B9hL0GOqUBUKj7IgpyL2k6Ihx5dJm8c0kY1VFFOZnhTxj252aGjfJJG5SPcM2ey%2F0ICA9pA67QLMW46N3MOMNTCiVC57%2Fe4R9TwJPkm%2BfyjBKUqyhBz6HpZWnNrr5C%2FJx%2B0krzAlqnxMasS0X7AnU1vcGBviIxli5%2FG9ldJxEa9OfPPAOXqc6GuOZuILnsDajVq6nN3oQw0KEH9aJNJCuBf%2Fg35kp0QLNuEicZ&X-Amz-Signature=0e34eaba26c16095f15d0ae23cc0b18fc5cb5f252e39217cea3f35082e05db0d&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
