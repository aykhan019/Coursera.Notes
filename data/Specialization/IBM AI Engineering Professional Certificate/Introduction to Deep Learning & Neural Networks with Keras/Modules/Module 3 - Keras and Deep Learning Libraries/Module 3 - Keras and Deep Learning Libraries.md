

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SD4QJAN3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBoNWap253coWoKSz5QgBJmGiYDCcdXypzLTFI9VzyeOAiEAxAAFGRGkGYdBURKd2kZcQknHmzQVntWddsjFAcrYUdUqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKHtlytDS8KqomQviircA1otGMPmIvGcBT5CVJgxSevkCEpWKZpVhHbRXcD%2BSCiy2qpIUJNP4KjkjE%2B1X%2FQ5obiTFfd4HFUHuaaH3jHQk6OgEkj1tN08dfQhvsV12C4sfxbPzei0OxwfTYeyAYoyjqHNRzPK3TSYTuKIie2ZQhCaMlFiFTa4cTkXZ%2BZsE26c2VNXEGiIOhqCZEmio2kFn4O8DRaxmPjblw1x2QIYfjoO5pHPf%2FSNBAHH2A8m4R6Eo4v4PZeBHpZk7mH61GyZUQ6zkGiKHGvQatyim9UHBRAp5XKABhKwdtCt69e9lU67xWgiP%2BRMxwFV3IzAUlldBWI%2BuJrqSpACya23Cs2lLsXrTVSuqbYrKulp0%2BoOQ%2BHTEimsDSI3tv72CIgJVVfbB9WQbzLz4SaMTSuiaGJ57VcHa%2BgpXG2YgZpo9zKFXe836mj5iMilsadlCKViJ2fxoIRR8JZhHv5WuDY0E8M%2FToXJL6LUmURmJqdv0O4prKjXUlZ6XjhBnP7I03BTGGTVW2pHw0Y4gBX7wi12jASe52Gpi36I9fw0%2F%2FuQg5TiCYYpqHc56dkoF2%2F%2FrpBvA3paNnmm%2BDaDHu%2FEIftwvEhjGoHWh07g9OrcXWzysSjHPzYit9x5I5bZnZcFOTVvMOCD6bwGOqUBv8zIy2dv0eErms%2BsMfzTjn%2BMU1S8Dyh%2BNnc2S8BV74JGO4Rle6%2FNmONmn6D57Cz3HpSj3VC4V77FfABnFAYu0YniX0q3U7xoR9xEULrOtGtwveUETthnwMMdu86Mr68Gv8ARXR%2FYPP3t9LF5bNvUiwtMPogM90djPrJxVJ8caUTu4O9PKFay4iDBkZpImGDXTKUJ4OlH7BfazjiMPW44fGkLZ7dC&X-Amz-Signature=34aa162ffe52b14b236999a05277ee68b6a9d3c0ddb57a382ea7dc5c2af44547&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SD4QJAN3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBoNWap253coWoKSz5QgBJmGiYDCcdXypzLTFI9VzyeOAiEAxAAFGRGkGYdBURKd2kZcQknHmzQVntWddsjFAcrYUdUqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKHtlytDS8KqomQviircA1otGMPmIvGcBT5CVJgxSevkCEpWKZpVhHbRXcD%2BSCiy2qpIUJNP4KjkjE%2B1X%2FQ5obiTFfd4HFUHuaaH3jHQk6OgEkj1tN08dfQhvsV12C4sfxbPzei0OxwfTYeyAYoyjqHNRzPK3TSYTuKIie2ZQhCaMlFiFTa4cTkXZ%2BZsE26c2VNXEGiIOhqCZEmio2kFn4O8DRaxmPjblw1x2QIYfjoO5pHPf%2FSNBAHH2A8m4R6Eo4v4PZeBHpZk7mH61GyZUQ6zkGiKHGvQatyim9UHBRAp5XKABhKwdtCt69e9lU67xWgiP%2BRMxwFV3IzAUlldBWI%2BuJrqSpACya23Cs2lLsXrTVSuqbYrKulp0%2BoOQ%2BHTEimsDSI3tv72CIgJVVfbB9WQbzLz4SaMTSuiaGJ57VcHa%2BgpXG2YgZpo9zKFXe836mj5iMilsadlCKViJ2fxoIRR8JZhHv5WuDY0E8M%2FToXJL6LUmURmJqdv0O4prKjXUlZ6XjhBnP7I03BTGGTVW2pHw0Y4gBX7wi12jASe52Gpi36I9fw0%2F%2FuQg5TiCYYpqHc56dkoF2%2F%2FrpBvA3paNnmm%2BDaDHu%2FEIftwvEhjGoHWh07g9OrcXWzysSjHPzYit9x5I5bZnZcFOTVvMOCD6bwGOqUBv8zIy2dv0eErms%2BsMfzTjn%2BMU1S8Dyh%2BNnc2S8BV74JGO4Rle6%2FNmONmn6D57Cz3HpSj3VC4V77FfABnFAYu0YniX0q3U7xoR9xEULrOtGtwveUETthnwMMdu86Mr68Gv8ARXR%2FYPP3t9LF5bNvUiwtMPogM90djPrJxVJ8caUTu4O9PKFay4iDBkZpImGDXTKUJ4OlH7BfazjiMPW44fGkLZ7dC&X-Amz-Signature=11049dbbbf517b1654a5c750c29acbd13eea8a0d19e12731e17b7c9fcd931e46&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SD4QJAN3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBoNWap253coWoKSz5QgBJmGiYDCcdXypzLTFI9VzyeOAiEAxAAFGRGkGYdBURKd2kZcQknHmzQVntWddsjFAcrYUdUqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKHtlytDS8KqomQviircA1otGMPmIvGcBT5CVJgxSevkCEpWKZpVhHbRXcD%2BSCiy2qpIUJNP4KjkjE%2B1X%2FQ5obiTFfd4HFUHuaaH3jHQk6OgEkj1tN08dfQhvsV12C4sfxbPzei0OxwfTYeyAYoyjqHNRzPK3TSYTuKIie2ZQhCaMlFiFTa4cTkXZ%2BZsE26c2VNXEGiIOhqCZEmio2kFn4O8DRaxmPjblw1x2QIYfjoO5pHPf%2FSNBAHH2A8m4R6Eo4v4PZeBHpZk7mH61GyZUQ6zkGiKHGvQatyim9UHBRAp5XKABhKwdtCt69e9lU67xWgiP%2BRMxwFV3IzAUlldBWI%2BuJrqSpACya23Cs2lLsXrTVSuqbYrKulp0%2BoOQ%2BHTEimsDSI3tv72CIgJVVfbB9WQbzLz4SaMTSuiaGJ57VcHa%2BgpXG2YgZpo9zKFXe836mj5iMilsadlCKViJ2fxoIRR8JZhHv5WuDY0E8M%2FToXJL6LUmURmJqdv0O4prKjXUlZ6XjhBnP7I03BTGGTVW2pHw0Y4gBX7wi12jASe52Gpi36I9fw0%2F%2FuQg5TiCYYpqHc56dkoF2%2F%2FrpBvA3paNnmm%2BDaDHu%2FEIftwvEhjGoHWh07g9OrcXWzysSjHPzYit9x5I5bZnZcFOTVvMOCD6bwGOqUBv8zIy2dv0eErms%2BsMfzTjn%2BMU1S8Dyh%2BNnc2S8BV74JGO4Rle6%2FNmONmn6D57Cz3HpSj3VC4V77FfABnFAYu0YniX0q3U7xoR9xEULrOtGtwveUETthnwMMdu86Mr68Gv8ARXR%2FYPP3t9LF5bNvUiwtMPogM90djPrJxVJ8caUTu4O9PKFay4iDBkZpImGDXTKUJ4OlH7BfazjiMPW44fGkLZ7dC&X-Amz-Signature=ce7372f9e0595c5fa6a4b159a17df08eff9debe46697a6fdf903d0bfbd5a531b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZIII53G5%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCeZR8hWUEdW7Zq%2BUJhf%2BtP6YDqM%2FYNRb3EYnIGsc6MbAIgZykkW2wy0aKDCpsAgHKDehF37j7M6vdUNCeowEhhFF4qiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGUjHZx7bMpFGUNy2CrcA%2FF%2FWEYEfHkZg9swgjwe9WmOcXE29vb94%2Fpuge9dws9YCtdbwPwQ%2FbICthzDbPL0luDwwDEk1LJXybPkgdoWFK6tzS9mNDj7ps00eMQOGgJaFtpkCKXApVVxQjt3TKZPgcTv97tQhjpRJtIPDW2NzQIMMbIctiOVjpJzefOasvFbrzd9HGYCwP%2BojZS0CJxaTdsmuTXbc33DJKnq8s%2FaHgoNsILxdM6Nz1g%2FLGkORSBgj7LrAaFo%2BV6bLNJAi%2FaO2xE2GwyPZ%2Fpp2KB0C4zHFkL%2ByFeW9zgVQq53cxmSJbC3pDnkFuwcnGYLJEQnUO2ASwu4%2FnK3oqthU%2FPljRRls9p9tHBQgjZtwwmu0DkkDdDDRSrM%2BCJHrP0agMIOEzM1UPM6pLNStQZWWM%2FrZUg2bqh7ENMPous8T3Gv%2BlpviWeQ0ICgQ0IR2wgLt25n%2F0sTMjzN3PvjU1%2FLfj4MbDbl42xH92wEWkr08AzvdLIU3sST%2B4U0RvxO7tNXVqMy1XleppY0Rk4ZmKjGV32d1DaKqQcZcuzR6M%2B1gxPFfRgq%2BhI6ptFkSsjUHCpTzeQFOrl8PSV%2BVOb3ll4ZFVvjx8O8krt8ZDHiIpNBjB9O1li3iNnm6eAuuojHvV0SbdD5MOmD6bwGOqUBlMIDVYUibtGrqsDWDc7M0o%2BMTXXwGb7dO12EIwKvbTGUgZ0cMNn8g331q6G2VTWEZYspuFYlRZVBfLlNHHwGfHsv%2B%2FiPe6KcPNN7Sfs1hX89HqTCCLHEX%2B9%2Fg5pNWpvhR50woxEhivn%2BXUiNAMLWro80zP1XSHA2WGgVMXko%2BhgNYh%2F2fLxV%2FOYTqAti%2BsN4G%2Bv4hgf9LNfaEXjTLiGnDDU1UVCl&X-Amz-Signature=5a735c2d7bb048459ff5f80be64fa06e23d642071cc7e061317b6aa26b1b2aca&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666JSWW2CL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGmryJWIcpPMY7O6d13m9MB3dE%2B2l%2B2IqtJA%2F%2BIfipHbAiBCFni7lQN9Z5kFeSVeC9ec5U6xUaHk3E3gxSddkrKflyqIBAiQ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM885KnVUWE2vNUbCZKtwDtcHED7htBFdSYcSeJQfftCdwBxMg1H%2FNdHd6mI5xuMulS10UF0JFAfyEcQmi84TODqbHldvZRVjR766801b6Xa7KwaQzIGLsf1xjdtZ%2FrFXGMT0VJgTG3DHSWPpPaTK2IAgRlMW1SvdimsR47ttN9hIMBXZe8yhCd6sCyP1ybsIJL3cEFlGW9Z0or%2F%2BzExugJ5emPlRmWBeOeWMjr5hBCmKv94RhEwJjY3QHwL8qIoC0TZtd8o5GOYVrYtAfV1%2Fy7I%2BDoYCRS%2B7iaDj9DTwOQ2wpas2ZaTvRNteGf%2B5%2F36aQZDi7TE7pU0PK4pttnLtdj9lMt9%2Bsg1ifRTYcFtqkXYucNQmdyXxJAllRJypeqKEIOcCYMnHx1A43bMXnwu4i5NifwittQLwI6VTeElg7stdz36U26Rc1cMOB5a%2F00jTBV8ROVcQnz9dSUFqqiROmDhhVlZaQa24zUbV82LNcVOulj0laxGVXqCAVBioJVqEHhgrpDreS%2FGZDO%2B9JWqSL6E8dKOZ2cr9zdAxYOuKlXZHBDpYHad8EFYiXZESlYnjF8Eg7tzgIxDuaC03vUZAlw22DVZsKnt4ORHMUK81%2BX18D8pcfxPLEbvIm3c6SGiOwKnR8MwNyKXSJO5MwmoTpvAY6pgHEs3O2wxu12pTXWtQi48Jax9b68xtgUSepWMiNI4Ix1g72BEcrTu7Fx4FujY9BXITxDSBugJtOA1qq3zSbryB91c0j%2BtfzE3sRQPQIx9vbSHYnpxZoyU8LCywTT%2ByNQTGNs2b4ndbCk%2Bo8FBZXDwmzYuSQN9lQU1Qeqy1%2F0RGqViY9aSI5sIKzGuVOMV%2BTnjTE4e5A77TvSbkH%2FODYePobKgf2BsMA&X-Amz-Signature=c7bbf654ee1cd24a455912a3ea0f410ca348349939290d4fcce84e86757af553&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SD4QJAN3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBoNWap253coWoKSz5QgBJmGiYDCcdXypzLTFI9VzyeOAiEAxAAFGRGkGYdBURKd2kZcQknHmzQVntWddsjFAcrYUdUqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKHtlytDS8KqomQviircA1otGMPmIvGcBT5CVJgxSevkCEpWKZpVhHbRXcD%2BSCiy2qpIUJNP4KjkjE%2B1X%2FQ5obiTFfd4HFUHuaaH3jHQk6OgEkj1tN08dfQhvsV12C4sfxbPzei0OxwfTYeyAYoyjqHNRzPK3TSYTuKIie2ZQhCaMlFiFTa4cTkXZ%2BZsE26c2VNXEGiIOhqCZEmio2kFn4O8DRaxmPjblw1x2QIYfjoO5pHPf%2FSNBAHH2A8m4R6Eo4v4PZeBHpZk7mH61GyZUQ6zkGiKHGvQatyim9UHBRAp5XKABhKwdtCt69e9lU67xWgiP%2BRMxwFV3IzAUlldBWI%2BuJrqSpACya23Cs2lLsXrTVSuqbYrKulp0%2BoOQ%2BHTEimsDSI3tv72CIgJVVfbB9WQbzLz4SaMTSuiaGJ57VcHa%2BgpXG2YgZpo9zKFXe836mj5iMilsadlCKViJ2fxoIRR8JZhHv5WuDY0E8M%2FToXJL6LUmURmJqdv0O4prKjXUlZ6XjhBnP7I03BTGGTVW2pHw0Y4gBX7wi12jASe52Gpi36I9fw0%2F%2FuQg5TiCYYpqHc56dkoF2%2F%2FrpBvA3paNnmm%2BDaDHu%2FEIftwvEhjGoHWh07g9OrcXWzysSjHPzYit9x5I5bZnZcFOTVvMOCD6bwGOqUBv8zIy2dv0eErms%2BsMfzTjn%2BMU1S8Dyh%2BNnc2S8BV74JGO4Rle6%2FNmONmn6D57Cz3HpSj3VC4V77FfABnFAYu0YniX0q3U7xoR9xEULrOtGtwveUETthnwMMdu86Mr68Gv8ARXR%2FYPP3t9LF5bNvUiwtMPogM90djPrJxVJ8caUTu4O9PKFay4iDBkZpImGDXTKUJ4OlH7BfazjiMPW44fGkLZ7dC&X-Amz-Signature=3f6de0fcea6bfa0981f944abadff6a391bb845d6cc8ed7d10cd5f67b2c5a85de&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SD4QJAN3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBoNWap253coWoKSz5QgBJmGiYDCcdXypzLTFI9VzyeOAiEAxAAFGRGkGYdBURKd2kZcQknHmzQVntWddsjFAcrYUdUqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKHtlytDS8KqomQviircA1otGMPmIvGcBT5CVJgxSevkCEpWKZpVhHbRXcD%2BSCiy2qpIUJNP4KjkjE%2B1X%2FQ5obiTFfd4HFUHuaaH3jHQk6OgEkj1tN08dfQhvsV12C4sfxbPzei0OxwfTYeyAYoyjqHNRzPK3TSYTuKIie2ZQhCaMlFiFTa4cTkXZ%2BZsE26c2VNXEGiIOhqCZEmio2kFn4O8DRaxmPjblw1x2QIYfjoO5pHPf%2FSNBAHH2A8m4R6Eo4v4PZeBHpZk7mH61GyZUQ6zkGiKHGvQatyim9UHBRAp5XKABhKwdtCt69e9lU67xWgiP%2BRMxwFV3IzAUlldBWI%2BuJrqSpACya23Cs2lLsXrTVSuqbYrKulp0%2BoOQ%2BHTEimsDSI3tv72CIgJVVfbB9WQbzLz4SaMTSuiaGJ57VcHa%2BgpXG2YgZpo9zKFXe836mj5iMilsadlCKViJ2fxoIRR8JZhHv5WuDY0E8M%2FToXJL6LUmURmJqdv0O4prKjXUlZ6XjhBnP7I03BTGGTVW2pHw0Y4gBX7wi12jASe52Gpi36I9fw0%2F%2FuQg5TiCYYpqHc56dkoF2%2F%2FrpBvA3paNnmm%2BDaDHu%2FEIftwvEhjGoHWh07g9OrcXWzysSjHPzYit9x5I5bZnZcFOTVvMOCD6bwGOqUBv8zIy2dv0eErms%2BsMfzTjn%2BMU1S8Dyh%2BNnc2S8BV74JGO4Rle6%2FNmONmn6D57Cz3HpSj3VC4V77FfABnFAYu0YniX0q3U7xoR9xEULrOtGtwveUETthnwMMdu86Mr68Gv8ARXR%2FYPP3t9LF5bNvUiwtMPogM90djPrJxVJ8caUTu4O9PKFay4iDBkZpImGDXTKUJ4OlH7BfazjiMPW44fGkLZ7dC&X-Amz-Signature=0f4afea610a4195283e4c62904f14ad161df936815542ee88fc2c7ba7979bf05&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SD4QJAN3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBoNWap253coWoKSz5QgBJmGiYDCcdXypzLTFI9VzyeOAiEAxAAFGRGkGYdBURKd2kZcQknHmzQVntWddsjFAcrYUdUqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKHtlytDS8KqomQviircA1otGMPmIvGcBT5CVJgxSevkCEpWKZpVhHbRXcD%2BSCiy2qpIUJNP4KjkjE%2B1X%2FQ5obiTFfd4HFUHuaaH3jHQk6OgEkj1tN08dfQhvsV12C4sfxbPzei0OxwfTYeyAYoyjqHNRzPK3TSYTuKIie2ZQhCaMlFiFTa4cTkXZ%2BZsE26c2VNXEGiIOhqCZEmio2kFn4O8DRaxmPjblw1x2QIYfjoO5pHPf%2FSNBAHH2A8m4R6Eo4v4PZeBHpZk7mH61GyZUQ6zkGiKHGvQatyim9UHBRAp5XKABhKwdtCt69e9lU67xWgiP%2BRMxwFV3IzAUlldBWI%2BuJrqSpACya23Cs2lLsXrTVSuqbYrKulp0%2BoOQ%2BHTEimsDSI3tv72CIgJVVfbB9WQbzLz4SaMTSuiaGJ57VcHa%2BgpXG2YgZpo9zKFXe836mj5iMilsadlCKViJ2fxoIRR8JZhHv5WuDY0E8M%2FToXJL6LUmURmJqdv0O4prKjXUlZ6XjhBnP7I03BTGGTVW2pHw0Y4gBX7wi12jASe52Gpi36I9fw0%2F%2FuQg5TiCYYpqHc56dkoF2%2F%2FrpBvA3paNnmm%2BDaDHu%2FEIftwvEhjGoHWh07g9OrcXWzysSjHPzYit9x5I5bZnZcFOTVvMOCD6bwGOqUBv8zIy2dv0eErms%2BsMfzTjn%2BMU1S8Dyh%2BNnc2S8BV74JGO4Rle6%2FNmONmn6D57Cz3HpSj3VC4V77FfABnFAYu0YniX0q3U7xoR9xEULrOtGtwveUETthnwMMdu86Mr68Gv8ARXR%2FYPP3t9LF5bNvUiwtMPogM90djPrJxVJ8caUTu4O9PKFay4iDBkZpImGDXTKUJ4OlH7BfazjiMPW44fGkLZ7dC&X-Amz-Signature=ea841d904f39007d66f9f33c5f321de06018ffcd0e297eb62856f1ffe184b493&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SD4QJAN3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBoNWap253coWoKSz5QgBJmGiYDCcdXypzLTFI9VzyeOAiEAxAAFGRGkGYdBURKd2kZcQknHmzQVntWddsjFAcrYUdUqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKHtlytDS8KqomQviircA1otGMPmIvGcBT5CVJgxSevkCEpWKZpVhHbRXcD%2BSCiy2qpIUJNP4KjkjE%2B1X%2FQ5obiTFfd4HFUHuaaH3jHQk6OgEkj1tN08dfQhvsV12C4sfxbPzei0OxwfTYeyAYoyjqHNRzPK3TSYTuKIie2ZQhCaMlFiFTa4cTkXZ%2BZsE26c2VNXEGiIOhqCZEmio2kFn4O8DRaxmPjblw1x2QIYfjoO5pHPf%2FSNBAHH2A8m4R6Eo4v4PZeBHpZk7mH61GyZUQ6zkGiKHGvQatyim9UHBRAp5XKABhKwdtCt69e9lU67xWgiP%2BRMxwFV3IzAUlldBWI%2BuJrqSpACya23Cs2lLsXrTVSuqbYrKulp0%2BoOQ%2BHTEimsDSI3tv72CIgJVVfbB9WQbzLz4SaMTSuiaGJ57VcHa%2BgpXG2YgZpo9zKFXe836mj5iMilsadlCKViJ2fxoIRR8JZhHv5WuDY0E8M%2FToXJL6LUmURmJqdv0O4prKjXUlZ6XjhBnP7I03BTGGTVW2pHw0Y4gBX7wi12jASe52Gpi36I9fw0%2F%2FuQg5TiCYYpqHc56dkoF2%2F%2FrpBvA3paNnmm%2BDaDHu%2FEIftwvEhjGoHWh07g9OrcXWzysSjHPzYit9x5I5bZnZcFOTVvMOCD6bwGOqUBv8zIy2dv0eErms%2BsMfzTjn%2BMU1S8Dyh%2BNnc2S8BV74JGO4Rle6%2FNmONmn6D57Cz3HpSj3VC4V77FfABnFAYu0YniX0q3U7xoR9xEULrOtGtwveUETthnwMMdu86Mr68Gv8ARXR%2FYPP3t9LF5bNvUiwtMPogM90djPrJxVJ8caUTu4O9PKFay4iDBkZpImGDXTKUJ4OlH7BfazjiMPW44fGkLZ7dC&X-Amz-Signature=34923db1eed552b61e1f9619631650c7011f9da9de982533fcff4b4adffc9050&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
