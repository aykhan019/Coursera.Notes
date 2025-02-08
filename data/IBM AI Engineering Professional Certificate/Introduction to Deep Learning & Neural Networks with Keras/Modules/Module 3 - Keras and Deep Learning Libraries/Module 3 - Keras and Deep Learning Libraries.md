

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466THZL5CV3%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJHMEUCIBjU1WA9MJZH9YE3wYGMGUITYM0pH23pcXnR4uGdWukJAiEA8IKgV9QKVeMFckoCUqDbVNsZupMWywTMF%2BHYgXaHW0IqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL%2FkX%2ByvuEx8UbyhnSrcA7syqL0eMaCDXe7Ibf5ErbVVgrmXDoX0fQ9UlksiqIay5zq%2BB17PjiQgq5F8TV1ikwrpAac1B6nJ7%2BIFy42HKRpu1XPa2EYJRFn9DLYFyQY%2FPn3%2FQfXj6gUQINN46biB2Y19mn4cO4sw5Hs%2BV0tPkSHW2jh016wk0ea35AwRC08wX3MXDmh8pULBdfkzoXlyfByGPBadaCQFSxh08xfyzuLs24g8kI65ONOCkhUQ23eXqbpaSqq0EaygXfEk9oEfHCSnhYZDmG%2Fs5J0Orb9tUCciFodeqeDTAKRx2nb0pZBWjPgcnmssm%2B7roTkDwX%2Bi5psXvXMN0WtRhAngiGmUWVGPdhD2OpsoCGivKGzv9E4lID8vxEA20NSd7Bacr7uuhqmCODeBd3WoDBfUlmFFEKb4V7p61R0W1OIe2BofR30hHKEkC%2B88yfbtOkQeVJOeWgdWwFUoCqIreFh9LA0%2FaeU9Rvb9Cw%2FomwMb0ChxcdsywsBD5ZRC%2FJFQuqOlvPZi7JKauwEXAP0%2FX7runaF%2BFM%2FCQpqWdH2ljpFY5OWgdaw8NZ1A0DJ36hHcc4wHO1iObJMocU3FZfrwY2XvvMWYtFbjAK3MqGKabpsnE4IIm5uJT%2BXOrIoJ5rsRb55oMMLUm70GOqUBQza2VYrR3OBe6FkCgkZBrfQsCqsqmOntVkQqV1hEXKjVdfEqdSP1U%2Bw97hy%2BBqyfoczag9Eug9tkopHRE%2BFhxsx6dCzzY01nYq863rZYgKfiU9fnDT9k0wmESnwndYWe%2Fuu5wyXWPtzxe2fJDMxWPO57PO8D6HFwLjp2g67o4irL8x2dklf1ngE1U0l4i7iQPM1k%2F2VFvSCVGtCnS8SL%2BgbXvFUJ&X-Amz-Signature=397cc81b95ea8f4de8e9fe372aa23fc3fd931af061379d28fea7e556be0d9b25&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466THZL5CV3%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJHMEUCIBjU1WA9MJZH9YE3wYGMGUITYM0pH23pcXnR4uGdWukJAiEA8IKgV9QKVeMFckoCUqDbVNsZupMWywTMF%2BHYgXaHW0IqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL%2FkX%2ByvuEx8UbyhnSrcA7syqL0eMaCDXe7Ibf5ErbVVgrmXDoX0fQ9UlksiqIay5zq%2BB17PjiQgq5F8TV1ikwrpAac1B6nJ7%2BIFy42HKRpu1XPa2EYJRFn9DLYFyQY%2FPn3%2FQfXj6gUQINN46biB2Y19mn4cO4sw5Hs%2BV0tPkSHW2jh016wk0ea35AwRC08wX3MXDmh8pULBdfkzoXlyfByGPBadaCQFSxh08xfyzuLs24g8kI65ONOCkhUQ23eXqbpaSqq0EaygXfEk9oEfHCSnhYZDmG%2Fs5J0Orb9tUCciFodeqeDTAKRx2nb0pZBWjPgcnmssm%2B7roTkDwX%2Bi5psXvXMN0WtRhAngiGmUWVGPdhD2OpsoCGivKGzv9E4lID8vxEA20NSd7Bacr7uuhqmCODeBd3WoDBfUlmFFEKb4V7p61R0W1OIe2BofR30hHKEkC%2B88yfbtOkQeVJOeWgdWwFUoCqIreFh9LA0%2FaeU9Rvb9Cw%2FomwMb0ChxcdsywsBD5ZRC%2FJFQuqOlvPZi7JKauwEXAP0%2FX7runaF%2BFM%2FCQpqWdH2ljpFY5OWgdaw8NZ1A0DJ36hHcc4wHO1iObJMocU3FZfrwY2XvvMWYtFbjAK3MqGKabpsnE4IIm5uJT%2BXOrIoJ5rsRb55oMMLUm70GOqUBQza2VYrR3OBe6FkCgkZBrfQsCqsqmOntVkQqV1hEXKjVdfEqdSP1U%2Bw97hy%2BBqyfoczag9Eug9tkopHRE%2BFhxsx6dCzzY01nYq863rZYgKfiU9fnDT9k0wmESnwndYWe%2Fuu5wyXWPtzxe2fJDMxWPO57PO8D6HFwLjp2g67o4irL8x2dklf1ngE1U0l4i7iQPM1k%2F2VFvSCVGtCnS8SL%2BgbXvFUJ&X-Amz-Signature=9332605cc5efb7c54ac977efdc87b6bdf1f86cd8a5bfe627861140dc4aba9cf2&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466THZL5CV3%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJHMEUCIBjU1WA9MJZH9YE3wYGMGUITYM0pH23pcXnR4uGdWukJAiEA8IKgV9QKVeMFckoCUqDbVNsZupMWywTMF%2BHYgXaHW0IqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL%2FkX%2ByvuEx8UbyhnSrcA7syqL0eMaCDXe7Ibf5ErbVVgrmXDoX0fQ9UlksiqIay5zq%2BB17PjiQgq5F8TV1ikwrpAac1B6nJ7%2BIFy42HKRpu1XPa2EYJRFn9DLYFyQY%2FPn3%2FQfXj6gUQINN46biB2Y19mn4cO4sw5Hs%2BV0tPkSHW2jh016wk0ea35AwRC08wX3MXDmh8pULBdfkzoXlyfByGPBadaCQFSxh08xfyzuLs24g8kI65ONOCkhUQ23eXqbpaSqq0EaygXfEk9oEfHCSnhYZDmG%2Fs5J0Orb9tUCciFodeqeDTAKRx2nb0pZBWjPgcnmssm%2B7roTkDwX%2Bi5psXvXMN0WtRhAngiGmUWVGPdhD2OpsoCGivKGzv9E4lID8vxEA20NSd7Bacr7uuhqmCODeBd3WoDBfUlmFFEKb4V7p61R0W1OIe2BofR30hHKEkC%2B88yfbtOkQeVJOeWgdWwFUoCqIreFh9LA0%2FaeU9Rvb9Cw%2FomwMb0ChxcdsywsBD5ZRC%2FJFQuqOlvPZi7JKauwEXAP0%2FX7runaF%2BFM%2FCQpqWdH2ljpFY5OWgdaw8NZ1A0DJ36hHcc4wHO1iObJMocU3FZfrwY2XvvMWYtFbjAK3MqGKabpsnE4IIm5uJT%2BXOrIoJ5rsRb55oMMLUm70GOqUBQza2VYrR3OBe6FkCgkZBrfQsCqsqmOntVkQqV1hEXKjVdfEqdSP1U%2Bw97hy%2BBqyfoczag9Eug9tkopHRE%2BFhxsx6dCzzY01nYq863rZYgKfiU9fnDT9k0wmESnwndYWe%2Fuu5wyXWPtzxe2fJDMxWPO57PO8D6HFwLjp2g67o4irL8x2dklf1ngE1U0l4i7iQPM1k%2F2VFvSCVGtCnS8SL%2BgbXvFUJ&X-Amz-Signature=efa6459929c9bfa97505c7bf0674e78094e556eafc4923452ef4a21ad03f137e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46675ZJ5VSU%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJGMEQCIDhBwZ7WVSTU8OPvEvi4Cie98C9v1AIylOLYEIOsRMEgAiB7ccH1jqZ8In9urEI%2BVfs7R4RFO0XdjOzsheGjhJzANyqIBAiG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMOn3pyxhfG9rYO00tKtwDpgObQ6Q3iJIdOEBwNeQDLf%2B3f4liBpfpY4sUsR60grj6JL4kYMhwduRRBmRKv4vHaEzjQIAilTpdI3%2BUIbn5%2FUraoDAdtS%2BP%2FZuzZQcqDe7LCrZ0vLEM6zoyqugPZr4w6MWlCFVz8bY0tDbd8dZnl8wlUVjNHeGvMIXrrULq3oMQJchxpvBLe3WtQ9vyOQbRVuRDAQjyH7spxOEXWMjKds3U06AWC8QxQsqCycuqkNNc7%2BqoCTBig9tQ9F3oB78Nha2IssSYACpXPJ6qLu8TbO5OAUS%2FaJWoNPYPTdwFv69%2BgvW4UyvZ7layiHbfe%2BjskREbNj9IxsAOvOdlCVcdvY6f71oYR%2BUDuCySqi0fGzIFQ%2B2CMy%2FVfeGZG%2B1L86ktibb3QYd2lCguyfaKWJD%2BEiVHfMmX%2FmrKA2BrX3nS%2FSlT%2BG2tGdQ5xDGSR%2FKB2pGRjbuge6PfnHqja8Q3JmUj7ANlNRRmLTHS%2BrkzykXWHPBjPr4zDKgyxkmO3SGoMefHBapW1Ft%2BZQNFHDjXtWJ9beR14XOW5n9rG9u37PlYPeLHzyLsQOM1BMtBe5iPfhGarKhVI1FAQWhAvxzdvgldsx2Qpq2ms68PBnN39HFY8JSVJ9vmPlIqJIDNabYw4tSbvQY6pgF1WB6hErraVSFpp%2BDCtLlk5kaWwme6A1Y%2FG2CCEiDYy4%2BHpv8dcA41MSHeKOJKYEq2QOCay9v5l92NdODxJZKcDqkdR%2BtHqY%2BCe6c%2BRG2dQ9mnMAvCUsgwKycbjgK3%2FhkQ5skju5eeccxhWKD%2FLGm3ZZOyLCRFMQPh07D3NF%2Fx8%2BnowRhC80K%2B4ds5g0d%2FViRCp83C4J2u%2BhVoojcdsAkgTz5oQ%2BB3&X-Amz-Signature=787b503953d4066bd00ced9476c57b0c1ffe5a1e58a67c2384fe3b737f8dce2b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LOP4PE5%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJHMEUCIQDbf40TJh91NRya3qpConx0JSNMtRy1H3HRHNDViJ1IXAIgGI1BuKiRftkOfHyxEkm64MEOP5%2BHJgPFM0P7oACFlCMqiAQIhv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHySV9W5OMqp8zj8BSrcA0J08zVDmuWsw2uN2%2FJZiiA0Qj%2F%2FX%2FZKCAaSvQgf%2FpmprsHCY5Dp8c1finX6QLkMILluX6q6vVWbmJ6ofCDPwAZZzt1aNq86y5PCq64MNPgu2oX1t3cXEC89M45TYZ%2BshG3AP5GpAnqxlGz1jdKOiz12%2BU8CVobQ966qysqQDWHzhxEHnrSA9ExGHDr3XN%2FDgEeX350SgEKhGac2qZsUaQapiU5%2FRWEQ80HdAmcUXMtn%2B%2FY1Lfixle9r4cSW0kCPzzQwvq9VFtcTlVIX1OSJxHNDPOzQvl1pHt8rEjr6fIOdEybqyftDI45RJeCv2RC5UzyqWPrEOWJ0juwhfbjt1zx18MCl2aN1LcgtydCPjbqpcJe%2FYKmKbxx8YCZruoP%2B4y2aym4F3DYKInedkNJhA8OTKOUMZ8%2FHF%2BbhxlKus%2Bsjs8nuX4Md%2FMUrPlYyIbHk7Rx%2FohK7wN0GpjwUJqqSpgjnhYDR5D7VJC3KtQHBpu26Ec0dKNVRVEMdo4BXv3Yzt2v6Xfcq3SkvKMPvrP7zn4OkTuy7XGiFa5jnnvRatn9aOvU8eYGEjZtK7Sl1BvQD9Df%2BkyPBdQAFxS%2BYWaeLFmG1CBZx4sjQrx9VjGvaaaqwhQbUrzEsHhcpn2LFMLTUm70GOqUBmZ2TJ%2F9NHFKcjFp59dCAe3rkX9GDsgdkCBvuEK0oWMUks0ZHsl0NyJC03KNgpnc8H8AOTY4ByCPwfYgkTWgccBsfGvrPSDJVzmW5pginiaDgYNSec6%2BF2TTtZ%2Fe6ftDl3EBvJjtfNElUsLaoQ%2Fmi%2FpkBl1rwX2ewZ2vhFq5rRUBvCcUv%2BVvEUIdChkZA2cjSH%2FScWhI42QBfS7XXZVtDHIvpC8b9&X-Amz-Signature=c5cf26f158b66bf6d624a313e2cfe64fc842b483672b6a5cb19838e9d3c50c77&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466THZL5CV3%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJHMEUCIBjU1WA9MJZH9YE3wYGMGUITYM0pH23pcXnR4uGdWukJAiEA8IKgV9QKVeMFckoCUqDbVNsZupMWywTMF%2BHYgXaHW0IqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL%2FkX%2ByvuEx8UbyhnSrcA7syqL0eMaCDXe7Ibf5ErbVVgrmXDoX0fQ9UlksiqIay5zq%2BB17PjiQgq5F8TV1ikwrpAac1B6nJ7%2BIFy42HKRpu1XPa2EYJRFn9DLYFyQY%2FPn3%2FQfXj6gUQINN46biB2Y19mn4cO4sw5Hs%2BV0tPkSHW2jh016wk0ea35AwRC08wX3MXDmh8pULBdfkzoXlyfByGPBadaCQFSxh08xfyzuLs24g8kI65ONOCkhUQ23eXqbpaSqq0EaygXfEk9oEfHCSnhYZDmG%2Fs5J0Orb9tUCciFodeqeDTAKRx2nb0pZBWjPgcnmssm%2B7roTkDwX%2Bi5psXvXMN0WtRhAngiGmUWVGPdhD2OpsoCGivKGzv9E4lID8vxEA20NSd7Bacr7uuhqmCODeBd3WoDBfUlmFFEKb4V7p61R0W1OIe2BofR30hHKEkC%2B88yfbtOkQeVJOeWgdWwFUoCqIreFh9LA0%2FaeU9Rvb9Cw%2FomwMb0ChxcdsywsBD5ZRC%2FJFQuqOlvPZi7JKauwEXAP0%2FX7runaF%2BFM%2FCQpqWdH2ljpFY5OWgdaw8NZ1A0DJ36hHcc4wHO1iObJMocU3FZfrwY2XvvMWYtFbjAK3MqGKabpsnE4IIm5uJT%2BXOrIoJ5rsRb55oMMLUm70GOqUBQza2VYrR3OBe6FkCgkZBrfQsCqsqmOntVkQqV1hEXKjVdfEqdSP1U%2Bw97hy%2BBqyfoczag9Eug9tkopHRE%2BFhxsx6dCzzY01nYq863rZYgKfiU9fnDT9k0wmESnwndYWe%2Fuu5wyXWPtzxe2fJDMxWPO57PO8D6HFwLjp2g67o4irL8x2dklf1ngE1U0l4i7iQPM1k%2F2VFvSCVGtCnS8SL%2BgbXvFUJ&X-Amz-Signature=cd59eb7a5648ec86942d76c196b4afa69d564d883cb7f094bf07dc481ca7f532&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466THZL5CV3%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJHMEUCIBjU1WA9MJZH9YE3wYGMGUITYM0pH23pcXnR4uGdWukJAiEA8IKgV9QKVeMFckoCUqDbVNsZupMWywTMF%2BHYgXaHW0IqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL%2FkX%2ByvuEx8UbyhnSrcA7syqL0eMaCDXe7Ibf5ErbVVgrmXDoX0fQ9UlksiqIay5zq%2BB17PjiQgq5F8TV1ikwrpAac1B6nJ7%2BIFy42HKRpu1XPa2EYJRFn9DLYFyQY%2FPn3%2FQfXj6gUQINN46biB2Y19mn4cO4sw5Hs%2BV0tPkSHW2jh016wk0ea35AwRC08wX3MXDmh8pULBdfkzoXlyfByGPBadaCQFSxh08xfyzuLs24g8kI65ONOCkhUQ23eXqbpaSqq0EaygXfEk9oEfHCSnhYZDmG%2Fs5J0Orb9tUCciFodeqeDTAKRx2nb0pZBWjPgcnmssm%2B7roTkDwX%2Bi5psXvXMN0WtRhAngiGmUWVGPdhD2OpsoCGivKGzv9E4lID8vxEA20NSd7Bacr7uuhqmCODeBd3WoDBfUlmFFEKb4V7p61R0W1OIe2BofR30hHKEkC%2B88yfbtOkQeVJOeWgdWwFUoCqIreFh9LA0%2FaeU9Rvb9Cw%2FomwMb0ChxcdsywsBD5ZRC%2FJFQuqOlvPZi7JKauwEXAP0%2FX7runaF%2BFM%2FCQpqWdH2ljpFY5OWgdaw8NZ1A0DJ36hHcc4wHO1iObJMocU3FZfrwY2XvvMWYtFbjAK3MqGKabpsnE4IIm5uJT%2BXOrIoJ5rsRb55oMMLUm70GOqUBQza2VYrR3OBe6FkCgkZBrfQsCqsqmOntVkQqV1hEXKjVdfEqdSP1U%2Bw97hy%2BBqyfoczag9Eug9tkopHRE%2BFhxsx6dCzzY01nYq863rZYgKfiU9fnDT9k0wmESnwndYWe%2Fuu5wyXWPtzxe2fJDMxWPO57PO8D6HFwLjp2g67o4irL8x2dklf1ngE1U0l4i7iQPM1k%2F2VFvSCVGtCnS8SL%2BgbXvFUJ&X-Amz-Signature=3e91076bd3be542307a9621b69b740cccaffaa2f5d1b635901e17b766e367083&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466THZL5CV3%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJHMEUCIBjU1WA9MJZH9YE3wYGMGUITYM0pH23pcXnR4uGdWukJAiEA8IKgV9QKVeMFckoCUqDbVNsZupMWywTMF%2BHYgXaHW0IqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL%2FkX%2ByvuEx8UbyhnSrcA7syqL0eMaCDXe7Ibf5ErbVVgrmXDoX0fQ9UlksiqIay5zq%2BB17PjiQgq5F8TV1ikwrpAac1B6nJ7%2BIFy42HKRpu1XPa2EYJRFn9DLYFyQY%2FPn3%2FQfXj6gUQINN46biB2Y19mn4cO4sw5Hs%2BV0tPkSHW2jh016wk0ea35AwRC08wX3MXDmh8pULBdfkzoXlyfByGPBadaCQFSxh08xfyzuLs24g8kI65ONOCkhUQ23eXqbpaSqq0EaygXfEk9oEfHCSnhYZDmG%2Fs5J0Orb9tUCciFodeqeDTAKRx2nb0pZBWjPgcnmssm%2B7roTkDwX%2Bi5psXvXMN0WtRhAngiGmUWVGPdhD2OpsoCGivKGzv9E4lID8vxEA20NSd7Bacr7uuhqmCODeBd3WoDBfUlmFFEKb4V7p61R0W1OIe2BofR30hHKEkC%2B88yfbtOkQeVJOeWgdWwFUoCqIreFh9LA0%2FaeU9Rvb9Cw%2FomwMb0ChxcdsywsBD5ZRC%2FJFQuqOlvPZi7JKauwEXAP0%2FX7runaF%2BFM%2FCQpqWdH2ljpFY5OWgdaw8NZ1A0DJ36hHcc4wHO1iObJMocU3FZfrwY2XvvMWYtFbjAK3MqGKabpsnE4IIm5uJT%2BXOrIoJ5rsRb55oMMLUm70GOqUBQza2VYrR3OBe6FkCgkZBrfQsCqsqmOntVkQqV1hEXKjVdfEqdSP1U%2Bw97hy%2BBqyfoczag9Eug9tkopHRE%2BFhxsx6dCzzY01nYq863rZYgKfiU9fnDT9k0wmESnwndYWe%2Fuu5wyXWPtzxe2fJDMxWPO57PO8D6HFwLjp2g67o4irL8x2dklf1ngE1U0l4i7iQPM1k%2F2VFvSCVGtCnS8SL%2BgbXvFUJ&X-Amz-Signature=d8a0ca946a65fe2c491762ed53614084a67a201123aa1bf409b4f6419daff656&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466THZL5CV3%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJHMEUCIBjU1WA9MJZH9YE3wYGMGUITYM0pH23pcXnR4uGdWukJAiEA8IKgV9QKVeMFckoCUqDbVNsZupMWywTMF%2BHYgXaHW0IqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL%2FkX%2ByvuEx8UbyhnSrcA7syqL0eMaCDXe7Ibf5ErbVVgrmXDoX0fQ9UlksiqIay5zq%2BB17PjiQgq5F8TV1ikwrpAac1B6nJ7%2BIFy42HKRpu1XPa2EYJRFn9DLYFyQY%2FPn3%2FQfXj6gUQINN46biB2Y19mn4cO4sw5Hs%2BV0tPkSHW2jh016wk0ea35AwRC08wX3MXDmh8pULBdfkzoXlyfByGPBadaCQFSxh08xfyzuLs24g8kI65ONOCkhUQ23eXqbpaSqq0EaygXfEk9oEfHCSnhYZDmG%2Fs5J0Orb9tUCciFodeqeDTAKRx2nb0pZBWjPgcnmssm%2B7roTkDwX%2Bi5psXvXMN0WtRhAngiGmUWVGPdhD2OpsoCGivKGzv9E4lID8vxEA20NSd7Bacr7uuhqmCODeBd3WoDBfUlmFFEKb4V7p61R0W1OIe2BofR30hHKEkC%2B88yfbtOkQeVJOeWgdWwFUoCqIreFh9LA0%2FaeU9Rvb9Cw%2FomwMb0ChxcdsywsBD5ZRC%2FJFQuqOlvPZi7JKauwEXAP0%2FX7runaF%2BFM%2FCQpqWdH2ljpFY5OWgdaw8NZ1A0DJ36hHcc4wHO1iObJMocU3FZfrwY2XvvMWYtFbjAK3MqGKabpsnE4IIm5uJT%2BXOrIoJ5rsRb55oMMLUm70GOqUBQza2VYrR3OBe6FkCgkZBrfQsCqsqmOntVkQqV1hEXKjVdfEqdSP1U%2Bw97hy%2BBqyfoczag9Eug9tkopHRE%2BFhxsx6dCzzY01nYq863rZYgKfiU9fnDT9k0wmESnwndYWe%2Fuu5wyXWPtzxe2fJDMxWPO57PO8D6HFwLjp2g67o4irL8x2dklf1ngE1U0l4i7iQPM1k%2F2VFvSCVGtCnS8SL%2BgbXvFUJ&X-Amz-Signature=e992522ee609bef3c8f7c9b37c8896f41c2392da499c6f37c9973d70f2d08b16&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
