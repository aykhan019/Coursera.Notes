

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663JVNGPRN%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081921Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIAGw1dAEYBItJcAwj3HVGFzGwE12jkOBWoN6meVenKZlAiEA1xNxfnwuP8bVbAUVgVQERhtTn4ROmbkOoS887WRC1Cgq%2FwMIWRAAGgw2Mzc0MjMxODM4MDUiDM0OiDjTqiJ6K0x%2BByrcAyC8wJ7GFAJkIlEH5iDmLoj8oz3YpasuaBTjDPL6Cj4O7bfqCNAcj63ptOnqDHLwel2yR2U1Q49LBVNWN%2F3O6AwKoCrM64p%2Bgvw3oT5jsvck%2Fq8LmpRovQm4xt8n5QsWu1x9hzoxKg2R6%2B%2Br2vfrpsAiEzbaPeItzdbqIiWZsN4Ef3V8Ij3nPwIn9Uc5hJ5UU52m9GwxdSj8fxY438XEdV7oOAhO9ecCj3WKX1VDlhuqi6rzFFfYD3mmZ%2B0QPwpJjgh45ZbsQ53l5jHAvWw40m5FJnXYVIt1vwPtO05u6hqxGImQ1LrGWViFo2rO%2BysL8cPJkMqefgzKr%2F61gn%2Fjj%2BqLgqvAhe9dI00dh%2Blw%2FSJ70%2Fuz9DHnvKlZss1CUuxZms9%2FweLWOsYH3DJyOfim9PE0VVbBZcGiNnN8ND5NJoHrB8TiAScUhgCKgj%2BAPdHLVjtR3lFBHc1OMrEc08yTCI4mHv%2FmSNlGiiiZY8KUUE2G3ZlwLOcXwOKVERcGDxNLnCxS39vex9quFeCRpgx8rVb9C9wViDNLL0OBzLWf%2FJBKEAruPdAPcimaMBEWOJ7L29s63AYAja4cNF7qKFnwKRJn3wJGTRXLuK5joiPq6LR6fUpYTeb%2Bbmhetde%2BMIbRkb0GOqUB5a%2BvJpIB2RhUrfjjGCVz%2BMnxzkHpAlGe18by%2FK6gIHv14RApaDQUk0%2Fk2on6BYA3VobKKwAnPze8%2BqELNvQ8xMz%2FNGe4ceEGzhTBmtITv9%2F3SwDDfTJJioBHPVu%2FRTAjXTxN5sP9wK5qnW4eHYkG%2B%2Bqq3ksmAsBujoT1LuPY5DTYAM1RnboLtN9ray%2BGSRowyxyYniGhLcX%2FJhDRJ1pUGKUF%2BZ5b&X-Amz-Signature=76cb55f356d5e237e65de9cbd6c02cb8b8cd2e95acdfa1319fb9d4c1ce61055d&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663JVNGPRN%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081921Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIAGw1dAEYBItJcAwj3HVGFzGwE12jkOBWoN6meVenKZlAiEA1xNxfnwuP8bVbAUVgVQERhtTn4ROmbkOoS887WRC1Cgq%2FwMIWRAAGgw2Mzc0MjMxODM4MDUiDM0OiDjTqiJ6K0x%2BByrcAyC8wJ7GFAJkIlEH5iDmLoj8oz3YpasuaBTjDPL6Cj4O7bfqCNAcj63ptOnqDHLwel2yR2U1Q49LBVNWN%2F3O6AwKoCrM64p%2Bgvw3oT5jsvck%2Fq8LmpRovQm4xt8n5QsWu1x9hzoxKg2R6%2B%2Br2vfrpsAiEzbaPeItzdbqIiWZsN4Ef3V8Ij3nPwIn9Uc5hJ5UU52m9GwxdSj8fxY438XEdV7oOAhO9ecCj3WKX1VDlhuqi6rzFFfYD3mmZ%2B0QPwpJjgh45ZbsQ53l5jHAvWw40m5FJnXYVIt1vwPtO05u6hqxGImQ1LrGWViFo2rO%2BysL8cPJkMqefgzKr%2F61gn%2Fjj%2BqLgqvAhe9dI00dh%2Blw%2FSJ70%2Fuz9DHnvKlZss1CUuxZms9%2FweLWOsYH3DJyOfim9PE0VVbBZcGiNnN8ND5NJoHrB8TiAScUhgCKgj%2BAPdHLVjtR3lFBHc1OMrEc08yTCI4mHv%2FmSNlGiiiZY8KUUE2G3ZlwLOcXwOKVERcGDxNLnCxS39vex9quFeCRpgx8rVb9C9wViDNLL0OBzLWf%2FJBKEAruPdAPcimaMBEWOJ7L29s63AYAja4cNF7qKFnwKRJn3wJGTRXLuK5joiPq6LR6fUpYTeb%2Bbmhetde%2BMIbRkb0GOqUB5a%2BvJpIB2RhUrfjjGCVz%2BMnxzkHpAlGe18by%2FK6gIHv14RApaDQUk0%2Fk2on6BYA3VobKKwAnPze8%2BqELNvQ8xMz%2FNGe4ceEGzhTBmtITv9%2F3SwDDfTJJioBHPVu%2FRTAjXTxN5sP9wK5qnW4eHYkG%2B%2Bqq3ksmAsBujoT1LuPY5DTYAM1RnboLtN9ray%2BGSRowyxyYniGhLcX%2FJhDRJ1pUGKUF%2BZ5b&X-Amz-Signature=64227274ad61ec41cfdc7bf48dc4aa6e536ffe6ee1d028cbee8f5bb1b3e1d45c&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663JVNGPRN%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081921Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIAGw1dAEYBItJcAwj3HVGFzGwE12jkOBWoN6meVenKZlAiEA1xNxfnwuP8bVbAUVgVQERhtTn4ROmbkOoS887WRC1Cgq%2FwMIWRAAGgw2Mzc0MjMxODM4MDUiDM0OiDjTqiJ6K0x%2BByrcAyC8wJ7GFAJkIlEH5iDmLoj8oz3YpasuaBTjDPL6Cj4O7bfqCNAcj63ptOnqDHLwel2yR2U1Q49LBVNWN%2F3O6AwKoCrM64p%2Bgvw3oT5jsvck%2Fq8LmpRovQm4xt8n5QsWu1x9hzoxKg2R6%2B%2Br2vfrpsAiEzbaPeItzdbqIiWZsN4Ef3V8Ij3nPwIn9Uc5hJ5UU52m9GwxdSj8fxY438XEdV7oOAhO9ecCj3WKX1VDlhuqi6rzFFfYD3mmZ%2B0QPwpJjgh45ZbsQ53l5jHAvWw40m5FJnXYVIt1vwPtO05u6hqxGImQ1LrGWViFo2rO%2BysL8cPJkMqefgzKr%2F61gn%2Fjj%2BqLgqvAhe9dI00dh%2Blw%2FSJ70%2Fuz9DHnvKlZss1CUuxZms9%2FweLWOsYH3DJyOfim9PE0VVbBZcGiNnN8ND5NJoHrB8TiAScUhgCKgj%2BAPdHLVjtR3lFBHc1OMrEc08yTCI4mHv%2FmSNlGiiiZY8KUUE2G3ZlwLOcXwOKVERcGDxNLnCxS39vex9quFeCRpgx8rVb9C9wViDNLL0OBzLWf%2FJBKEAruPdAPcimaMBEWOJ7L29s63AYAja4cNF7qKFnwKRJn3wJGTRXLuK5joiPq6LR6fUpYTeb%2Bbmhetde%2BMIbRkb0GOqUB5a%2BvJpIB2RhUrfjjGCVz%2BMnxzkHpAlGe18by%2FK6gIHv14RApaDQUk0%2Fk2on6BYA3VobKKwAnPze8%2BqELNvQ8xMz%2FNGe4ceEGzhTBmtITv9%2F3SwDDfTJJioBHPVu%2FRTAjXTxN5sP9wK5qnW4eHYkG%2B%2Bqq3ksmAsBujoT1LuPY5DTYAM1RnboLtN9ray%2BGSRowyxyYniGhLcX%2FJhDRJ1pUGKUF%2BZ5b&X-Amz-Signature=9f3749e4e5ecc7764d7a8a69ed264b737bbee28cfaa21b8cbee06c963146f3aa&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663EV5XWDS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQCn5rxWQ5Buf9T4AgMhnEuooEEU1I6L7aOyEWMkIZnB3AIgHglqdtDWu897bqJqcQpsBY02lYeQKk%2BgvDneGUJSSJAq%2FwMIWRAAGgw2Mzc0MjMxODM4MDUiDKivld6NzKDsfGevXyrcA2DUQeKeEFxFnrzhvDy9SKZ4eALcN09BpWWD8ime5m0Pm8Y3P8XdBiP9RnHHOojw4TNwsB%2Bn84JSkDdBQt%2BnEoNXcpzaeq06Q%2Fa8KSAAfX0EStggujr4W2rZAO%2B3fVmNEkf0Ig%2FWRDdnhN9MnAX2DCzbikYJ9OumfarU9SMnBmNDVkWz%2BZtWsA%2BOuDIvzC1tSeTDdkts5dwpybmUAh77gJK8tvDdq0%2BJlG%2BSIQa6q%2BBxKDqK0pb6pA6gauAVSINdBlmGY%2Bi9Ybxbm876S8WBIKuHknkGvIK2lW6SWZxIVWfDZEVZJF6pYDVkt%2Bc%2F%2BSSS0mcN%2Fkd3zRpUTY56bRI2BgtuZYp2T%2FCnWRn4nOefrBhwixyaoc3LJS4kuNEJHuUlSyscjTat2Hy5wEa6QsRAwEa5P%2FctsEGfCWKhkSiwrT8iOgKyybkGVs1NRRzBeQ156VuCjdIRwOqwt2%2Ffg6o8xZtceYzpQqYwAlBJGVAOdY7RfadVo25xsE82%2BFCLnFD2v84flFuW0G04xKubCi4E88YVNriPlzQFO2cpBqrIo7FBZdSEka55vJorilKkyGlmxmqJOtNEHkHVXWxazHLNGCD%2Bnj492%2FGCQ7K4MAXWau%2Foan3GP0GjimOn%2FP%2FsMMXRkb0GOqUBWp8MYjbQc3btmfyLrSgfHtQTe3%2FJS5NqbCGKkwK6BS8YqxXuDMRJt6mWzI077ZgQnHv%2FK3o7vbagnY1PTLxPpO%2BMsgMcjS8E%2F0qNuY2c69C2L7QfGftSi4%2BUfY2wTagEtzMgZEMg8LeutJlW66tWcWbpsA8undikexYCtJSlEoaKQqkrE5OyRGxbU4IQwlLaZN%2BAUy84dpm0lTADh6gECJkxPzB%2B&X-Amz-Signature=e01f713a60296b3e23eea78606e4f831db13510ca9e41094547172c2c31a2ef3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667CGDID4J%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCID8FC6Vr3ch8YibXQJNUOzVZW%2FoiXDJ1kfYxCZb4Hwq1AiEA8nZu2b494uzEXCtUeODywCOatTw0NI9GNdkm8Mc86sEq%2FwMIWRAAGgw2Mzc0MjMxODM4MDUiDMUlqVeR%2BdSaoGNCPSrcA9azpVeV51rfbHjbEu5JS2PEnZwS%2BM8NCUut2tX0H2Qw7HlP8wWXaDeVMmymGGN%2F74HnThzqp7kPUTZ6U7cJ1y0baqbCeQfe3m0g8R0d5gZBiF0Xtpz2lhL1KFB73CLu9P1KGbf4P9u9TViACp%2FrvaubJnja5PrcUblYhJ5fOK0Pc1bhL7IQHEhvqtal8KxxHVrrusqM4VmqYhTJFMmmT78dcXaXCQbvnHXkhbVyaO30HCClS4vQ4YtC7FoWJ7Z%2B77cSZ3JB5GtrrochJJUCAbK1wbL%2FSB15BiTul%2BhWznC%2F7TnJLhVn%2BY5121BjsD4dES%2BAdlTGVAliGbTpHGZE4rAov72thLw8VLCOCM37kI5A5MOIkwOh4cbxdZQTdwgp%2FPjKFkqLesloSmYEfMK%2BWfoaHx90rVIguc88og40fNdzfWjE5P2dkk5u9qtlL1JCg%2FzL3ZUoP4yPiqlS2oYqfgen6aULpecA5UR2UkP%2FyXZJwLNY54AqTXy2UbPPCY65CbI2YIo0TXFYBUYl9RmWl9HaruKPEiTpWQeQEzrt8Qn%2FwcZV0MsDXF3f6gh197n0OSRyKU6VCcw67J%2BTrQ7F90xouBC8%2FMA%2BlIc0odPvjCeQ7qXOvmh6fur5gHl4MMnRkb0GOqUBvQZFpDWb9Sh8n%2B5AjnsoM56YBm0oHTGECjINUZUKLx4c75mHTuJLcoaV4W8KhJ36e4oylkGzSgsBL9nGy9x0RRrUqR2J1M%2FQw6IDsdWIelN1O91hWY8DcXDJq8lSX%2Flvt0%2FXNv1oeStpiwrlQ9cLTrftHc683s8DnoJSRAV7fKG9TlcNP9uNGVZ3n7ndcgDIHN1l8YWEFX9Xyhg4RRrGyL9UoIr1&X-Amz-Signature=59a90793a601117181bbcce47f76b0c7db99ff3f94c71f0b39aed9d5f95f9371&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663JVNGPRN%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081921Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIAGw1dAEYBItJcAwj3HVGFzGwE12jkOBWoN6meVenKZlAiEA1xNxfnwuP8bVbAUVgVQERhtTn4ROmbkOoS887WRC1Cgq%2FwMIWRAAGgw2Mzc0MjMxODM4MDUiDM0OiDjTqiJ6K0x%2BByrcAyC8wJ7GFAJkIlEH5iDmLoj8oz3YpasuaBTjDPL6Cj4O7bfqCNAcj63ptOnqDHLwel2yR2U1Q49LBVNWN%2F3O6AwKoCrM64p%2Bgvw3oT5jsvck%2Fq8LmpRovQm4xt8n5QsWu1x9hzoxKg2R6%2B%2Br2vfrpsAiEzbaPeItzdbqIiWZsN4Ef3V8Ij3nPwIn9Uc5hJ5UU52m9GwxdSj8fxY438XEdV7oOAhO9ecCj3WKX1VDlhuqi6rzFFfYD3mmZ%2B0QPwpJjgh45ZbsQ53l5jHAvWw40m5FJnXYVIt1vwPtO05u6hqxGImQ1LrGWViFo2rO%2BysL8cPJkMqefgzKr%2F61gn%2Fjj%2BqLgqvAhe9dI00dh%2Blw%2FSJ70%2Fuz9DHnvKlZss1CUuxZms9%2FweLWOsYH3DJyOfim9PE0VVbBZcGiNnN8ND5NJoHrB8TiAScUhgCKgj%2BAPdHLVjtR3lFBHc1OMrEc08yTCI4mHv%2FmSNlGiiiZY8KUUE2G3ZlwLOcXwOKVERcGDxNLnCxS39vex9quFeCRpgx8rVb9C9wViDNLL0OBzLWf%2FJBKEAruPdAPcimaMBEWOJ7L29s63AYAja4cNF7qKFnwKRJn3wJGTRXLuK5joiPq6LR6fUpYTeb%2Bbmhetde%2BMIbRkb0GOqUB5a%2BvJpIB2RhUrfjjGCVz%2BMnxzkHpAlGe18by%2FK6gIHv14RApaDQUk0%2Fk2on6BYA3VobKKwAnPze8%2BqELNvQ8xMz%2FNGe4ceEGzhTBmtITv9%2F3SwDDfTJJioBHPVu%2FRTAjXTxN5sP9wK5qnW4eHYkG%2B%2Bqq3ksmAsBujoT1LuPY5DTYAM1RnboLtN9ray%2BGSRowyxyYniGhLcX%2FJhDRJ1pUGKUF%2BZ5b&X-Amz-Signature=ab71d00d3ab6029c0f3b0b9498a0903f14f2e69714c443b81a3fcbb76df05ac4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663JVNGPRN%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081921Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIAGw1dAEYBItJcAwj3HVGFzGwE12jkOBWoN6meVenKZlAiEA1xNxfnwuP8bVbAUVgVQERhtTn4ROmbkOoS887WRC1Cgq%2FwMIWRAAGgw2Mzc0MjMxODM4MDUiDM0OiDjTqiJ6K0x%2BByrcAyC8wJ7GFAJkIlEH5iDmLoj8oz3YpasuaBTjDPL6Cj4O7bfqCNAcj63ptOnqDHLwel2yR2U1Q49LBVNWN%2F3O6AwKoCrM64p%2Bgvw3oT5jsvck%2Fq8LmpRovQm4xt8n5QsWu1x9hzoxKg2R6%2B%2Br2vfrpsAiEzbaPeItzdbqIiWZsN4Ef3V8Ij3nPwIn9Uc5hJ5UU52m9GwxdSj8fxY438XEdV7oOAhO9ecCj3WKX1VDlhuqi6rzFFfYD3mmZ%2B0QPwpJjgh45ZbsQ53l5jHAvWw40m5FJnXYVIt1vwPtO05u6hqxGImQ1LrGWViFo2rO%2BysL8cPJkMqefgzKr%2F61gn%2Fjj%2BqLgqvAhe9dI00dh%2Blw%2FSJ70%2Fuz9DHnvKlZss1CUuxZms9%2FweLWOsYH3DJyOfim9PE0VVbBZcGiNnN8ND5NJoHrB8TiAScUhgCKgj%2BAPdHLVjtR3lFBHc1OMrEc08yTCI4mHv%2FmSNlGiiiZY8KUUE2G3ZlwLOcXwOKVERcGDxNLnCxS39vex9quFeCRpgx8rVb9C9wViDNLL0OBzLWf%2FJBKEAruPdAPcimaMBEWOJ7L29s63AYAja4cNF7qKFnwKRJn3wJGTRXLuK5joiPq6LR6fUpYTeb%2Bbmhetde%2BMIbRkb0GOqUB5a%2BvJpIB2RhUrfjjGCVz%2BMnxzkHpAlGe18by%2FK6gIHv14RApaDQUk0%2Fk2on6BYA3VobKKwAnPze8%2BqELNvQ8xMz%2FNGe4ceEGzhTBmtITv9%2F3SwDDfTJJioBHPVu%2FRTAjXTxN5sP9wK5qnW4eHYkG%2B%2Bqq3ksmAsBujoT1LuPY5DTYAM1RnboLtN9ray%2BGSRowyxyYniGhLcX%2FJhDRJ1pUGKUF%2BZ5b&X-Amz-Signature=c7d601775e9bda2fe8aece748b63f979c74496b6aa80b4b3633402c1bb8fc2d8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663JVNGPRN%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081921Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIAGw1dAEYBItJcAwj3HVGFzGwE12jkOBWoN6meVenKZlAiEA1xNxfnwuP8bVbAUVgVQERhtTn4ROmbkOoS887WRC1Cgq%2FwMIWRAAGgw2Mzc0MjMxODM4MDUiDM0OiDjTqiJ6K0x%2BByrcAyC8wJ7GFAJkIlEH5iDmLoj8oz3YpasuaBTjDPL6Cj4O7bfqCNAcj63ptOnqDHLwel2yR2U1Q49LBVNWN%2F3O6AwKoCrM64p%2Bgvw3oT5jsvck%2Fq8LmpRovQm4xt8n5QsWu1x9hzoxKg2R6%2B%2Br2vfrpsAiEzbaPeItzdbqIiWZsN4Ef3V8Ij3nPwIn9Uc5hJ5UU52m9GwxdSj8fxY438XEdV7oOAhO9ecCj3WKX1VDlhuqi6rzFFfYD3mmZ%2B0QPwpJjgh45ZbsQ53l5jHAvWw40m5FJnXYVIt1vwPtO05u6hqxGImQ1LrGWViFo2rO%2BysL8cPJkMqefgzKr%2F61gn%2Fjj%2BqLgqvAhe9dI00dh%2Blw%2FSJ70%2Fuz9DHnvKlZss1CUuxZms9%2FweLWOsYH3DJyOfim9PE0VVbBZcGiNnN8ND5NJoHrB8TiAScUhgCKgj%2BAPdHLVjtR3lFBHc1OMrEc08yTCI4mHv%2FmSNlGiiiZY8KUUE2G3ZlwLOcXwOKVERcGDxNLnCxS39vex9quFeCRpgx8rVb9C9wViDNLL0OBzLWf%2FJBKEAruPdAPcimaMBEWOJ7L29s63AYAja4cNF7qKFnwKRJn3wJGTRXLuK5joiPq6LR6fUpYTeb%2Bbmhetde%2BMIbRkb0GOqUB5a%2BvJpIB2RhUrfjjGCVz%2BMnxzkHpAlGe18by%2FK6gIHv14RApaDQUk0%2Fk2on6BYA3VobKKwAnPze8%2BqELNvQ8xMz%2FNGe4ceEGzhTBmtITv9%2F3SwDDfTJJioBHPVu%2FRTAjXTxN5sP9wK5qnW4eHYkG%2B%2Bqq3ksmAsBujoT1LuPY5DTYAM1RnboLtN9ray%2BGSRowyxyYniGhLcX%2FJhDRJ1pUGKUF%2BZ5b&X-Amz-Signature=d668353bdf29ea01f280d470349d2ab583f4ef90b8bed4017336f8b87f79f59f&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663JVNGPRN%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081921Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIAGw1dAEYBItJcAwj3HVGFzGwE12jkOBWoN6meVenKZlAiEA1xNxfnwuP8bVbAUVgVQERhtTn4ROmbkOoS887WRC1Cgq%2FwMIWRAAGgw2Mzc0MjMxODM4MDUiDM0OiDjTqiJ6K0x%2BByrcAyC8wJ7GFAJkIlEH5iDmLoj8oz3YpasuaBTjDPL6Cj4O7bfqCNAcj63ptOnqDHLwel2yR2U1Q49LBVNWN%2F3O6AwKoCrM64p%2Bgvw3oT5jsvck%2Fq8LmpRovQm4xt8n5QsWu1x9hzoxKg2R6%2B%2Br2vfrpsAiEzbaPeItzdbqIiWZsN4Ef3V8Ij3nPwIn9Uc5hJ5UU52m9GwxdSj8fxY438XEdV7oOAhO9ecCj3WKX1VDlhuqi6rzFFfYD3mmZ%2B0QPwpJjgh45ZbsQ53l5jHAvWw40m5FJnXYVIt1vwPtO05u6hqxGImQ1LrGWViFo2rO%2BysL8cPJkMqefgzKr%2F61gn%2Fjj%2BqLgqvAhe9dI00dh%2Blw%2FSJ70%2Fuz9DHnvKlZss1CUuxZms9%2FweLWOsYH3DJyOfim9PE0VVbBZcGiNnN8ND5NJoHrB8TiAScUhgCKgj%2BAPdHLVjtR3lFBHc1OMrEc08yTCI4mHv%2FmSNlGiiiZY8KUUE2G3ZlwLOcXwOKVERcGDxNLnCxS39vex9quFeCRpgx8rVb9C9wViDNLL0OBzLWf%2FJBKEAruPdAPcimaMBEWOJ7L29s63AYAja4cNF7qKFnwKRJn3wJGTRXLuK5joiPq6LR6fUpYTeb%2Bbmhetde%2BMIbRkb0GOqUB5a%2BvJpIB2RhUrfjjGCVz%2BMnxzkHpAlGe18by%2FK6gIHv14RApaDQUk0%2Fk2on6BYA3VobKKwAnPze8%2BqELNvQ8xMz%2FNGe4ceEGzhTBmtITv9%2F3SwDDfTJJioBHPVu%2FRTAjXTxN5sP9wK5qnW4eHYkG%2B%2Bqq3ksmAsBujoT1LuPY5DTYAM1RnboLtN9ray%2BGSRowyxyYniGhLcX%2FJhDRJ1pUGKUF%2BZ5b&X-Amz-Signature=e4adf22df23f670d5f28b6214cd34e2a07a023afcc00ff9cc5575f1a9c030ebd&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
