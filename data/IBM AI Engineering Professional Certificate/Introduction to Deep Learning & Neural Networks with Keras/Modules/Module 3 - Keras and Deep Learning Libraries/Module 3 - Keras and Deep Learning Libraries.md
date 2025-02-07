

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XDCHU46A%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T122855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJHMEUCIEp%2BRdqBpPJDgYl%2FLlWXZ99FHiW8QXl4B3VMO3ngPnReAiEAya4vDNqVxAlg7gOMTk%2FoJCTpjQn4wwKTpaNy96Z%2BHscq%2FwMIdRAAGgw2Mzc0MjMxODM4MDUiDIWwRZ8NPro49sXThCrcA1cbtkp9n4j%2BQRiZ87bPVo7v4sYTVvOjl20YPt8Ojb9mVMKSLmYkwEYOYgV5kCmKuCPV8V9yq312BGuIFd8tax8aMGiZRWER2fn2wQm5NCo8hNCLU1oFwazktw%2FqlZVzenOdFiHYiFKZRZVxAiadsF9YyGQQ5%2BdQxXlhEAji1fgy%2B6Xs6vwiI9xJYKAedAs6mGx4tB62JDomT%2FihFM%2FK%2BOIinAbqhvhRUFzoGNvRQ0DieZH4OTnyg7KDcBsA0Tx9Orr0M%2BhvWAhie0Lsdi7eBMgHS34Polbq9kRYwJhYJHAQFksM3710r%2BO52tCPP5ZFiV3C%2Fb40%2BNFi4bwSsFXs8oY%2BKamdXY9ds9HNJyV4drQgla4UaoDBHyAsRPpao7pUBTE%2FrpZUMVcEooU%2FCdJYeo7YTJSD9qAaYZLoavXJ5GzlzN2scTBNMgUY%2FHeDTDX%2BgHUpQ4c%2FCYL3KyBqgPdeK9yX2Rxl1%2B6XAyOmclJmRXz9WjAzj6ZZzMr2TlH2OEXBar8a7dlXii%2B%2FllFnqQMLbyhMEtfj8c1Koe0sf7z7XOoOv%2BxEjtIx%2BhPgnyVLHolFtpqAaif3hK3nitxc%2FzTHSehPmtSXUobOIg0epQf7BEk%2FfY%2FpOBg4pgygRNL1MNLwl70GOqUBLjiadap743NIBEi14UCC9b%2FuAWY%2Bw4gGh3LJV5wYKPlP4OI1E3xrYNlyo6eB2Y%2F8fqUbXYDXoOEXmurqc3PdsV5o1fNxD%2F3IebgpKa%2F2Rl788BhHagRjTPWgDsx6xhYu073GVwM6Xp7b45xaoVfPc%2FPalXnytUjoyoFQnwJVoQ%2BMwBEJw5YOvBO5zmAeq%2BUrvkeUyd7sYE65Pa%2F9x2zCfx%2Bk5GVo&X-Amz-Signature=3ea5a18fba39bee65f3ae1def760fe453c5e6458515700e092dea2439850dfac&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XDCHU46A%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T122855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJHMEUCIEp%2BRdqBpPJDgYl%2FLlWXZ99FHiW8QXl4B3VMO3ngPnReAiEAya4vDNqVxAlg7gOMTk%2FoJCTpjQn4wwKTpaNy96Z%2BHscq%2FwMIdRAAGgw2Mzc0MjMxODM4MDUiDIWwRZ8NPro49sXThCrcA1cbtkp9n4j%2BQRiZ87bPVo7v4sYTVvOjl20YPt8Ojb9mVMKSLmYkwEYOYgV5kCmKuCPV8V9yq312BGuIFd8tax8aMGiZRWER2fn2wQm5NCo8hNCLU1oFwazktw%2FqlZVzenOdFiHYiFKZRZVxAiadsF9YyGQQ5%2BdQxXlhEAji1fgy%2B6Xs6vwiI9xJYKAedAs6mGx4tB62JDomT%2FihFM%2FK%2BOIinAbqhvhRUFzoGNvRQ0DieZH4OTnyg7KDcBsA0Tx9Orr0M%2BhvWAhie0Lsdi7eBMgHS34Polbq9kRYwJhYJHAQFksM3710r%2BO52tCPP5ZFiV3C%2Fb40%2BNFi4bwSsFXs8oY%2BKamdXY9ds9HNJyV4drQgla4UaoDBHyAsRPpao7pUBTE%2FrpZUMVcEooU%2FCdJYeo7YTJSD9qAaYZLoavXJ5GzlzN2scTBNMgUY%2FHeDTDX%2BgHUpQ4c%2FCYL3KyBqgPdeK9yX2Rxl1%2B6XAyOmclJmRXz9WjAzj6ZZzMr2TlH2OEXBar8a7dlXii%2B%2FllFnqQMLbyhMEtfj8c1Koe0sf7z7XOoOv%2BxEjtIx%2BhPgnyVLHolFtpqAaif3hK3nitxc%2FzTHSehPmtSXUobOIg0epQf7BEk%2FfY%2FpOBg4pgygRNL1MNLwl70GOqUBLjiadap743NIBEi14UCC9b%2FuAWY%2Bw4gGh3LJV5wYKPlP4OI1E3xrYNlyo6eB2Y%2F8fqUbXYDXoOEXmurqc3PdsV5o1fNxD%2F3IebgpKa%2F2Rl788BhHagRjTPWgDsx6xhYu073GVwM6Xp7b45xaoVfPc%2FPalXnytUjoyoFQnwJVoQ%2BMwBEJw5YOvBO5zmAeq%2BUrvkeUyd7sYE65Pa%2F9x2zCfx%2Bk5GVo&X-Amz-Signature=d63ba95c0a1fa0fb29ee95f97f9b0f652adf6ba413f6e330b90c45df39a8b160&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XDCHU46A%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T122855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJHMEUCIEp%2BRdqBpPJDgYl%2FLlWXZ99FHiW8QXl4B3VMO3ngPnReAiEAya4vDNqVxAlg7gOMTk%2FoJCTpjQn4wwKTpaNy96Z%2BHscq%2FwMIdRAAGgw2Mzc0MjMxODM4MDUiDIWwRZ8NPro49sXThCrcA1cbtkp9n4j%2BQRiZ87bPVo7v4sYTVvOjl20YPt8Ojb9mVMKSLmYkwEYOYgV5kCmKuCPV8V9yq312BGuIFd8tax8aMGiZRWER2fn2wQm5NCo8hNCLU1oFwazktw%2FqlZVzenOdFiHYiFKZRZVxAiadsF9YyGQQ5%2BdQxXlhEAji1fgy%2B6Xs6vwiI9xJYKAedAs6mGx4tB62JDomT%2FihFM%2FK%2BOIinAbqhvhRUFzoGNvRQ0DieZH4OTnyg7KDcBsA0Tx9Orr0M%2BhvWAhie0Lsdi7eBMgHS34Polbq9kRYwJhYJHAQFksM3710r%2BO52tCPP5ZFiV3C%2Fb40%2BNFi4bwSsFXs8oY%2BKamdXY9ds9HNJyV4drQgla4UaoDBHyAsRPpao7pUBTE%2FrpZUMVcEooU%2FCdJYeo7YTJSD9qAaYZLoavXJ5GzlzN2scTBNMgUY%2FHeDTDX%2BgHUpQ4c%2FCYL3KyBqgPdeK9yX2Rxl1%2B6XAyOmclJmRXz9WjAzj6ZZzMr2TlH2OEXBar8a7dlXii%2B%2FllFnqQMLbyhMEtfj8c1Koe0sf7z7XOoOv%2BxEjtIx%2BhPgnyVLHolFtpqAaif3hK3nitxc%2FzTHSehPmtSXUobOIg0epQf7BEk%2FfY%2FpOBg4pgygRNL1MNLwl70GOqUBLjiadap743NIBEi14UCC9b%2FuAWY%2Bw4gGh3LJV5wYKPlP4OI1E3xrYNlyo6eB2Y%2F8fqUbXYDXoOEXmurqc3PdsV5o1fNxD%2F3IebgpKa%2F2Rl788BhHagRjTPWgDsx6xhYu073GVwM6Xp7b45xaoVfPc%2FPalXnytUjoyoFQnwJVoQ%2BMwBEJw5YOvBO5zmAeq%2BUrvkeUyd7sYE65Pa%2F9x2zCfx%2Bk5GVo&X-Amz-Signature=421edd839ac9c8d36cc0e5bc8cf274fb2c970b999f4f3f141238a3a3f789c6be&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664A44RFED%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T122856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJGMEQCIECyNinN3cfux%2BSK3Nj9m0%2FNKJ4jx6btwfDaMhZ3ed1fAiB7ac8VWqQf9Dr%2FKdsBTdokrFWlAnBfT22Gx2Rs0v6w3yr%2FAwh1EAAaDDYzNzQyMzE4MzgwNSIMgOaUej%2FMyZkFw%2BSkKtwD%2FboB1ntxEbWtRS%2FOiTnRogOlQ%2FaCLW7eZGQY2jpak6PVZkDhGkuGJa8i4uOwFy29L6PkVaTaKdfh6wSzBE9Xbzff0GRLA%2BvMOtwD1tgP5MTb4%2Fttb7R4UsTADP2aDmTyLV3ot6BLSoIjQszY5qIIOf4qwETXpeyvkiji0zCZZovh4Hz%2BluTApKZpBgA58suP8iqxrcjbImdqijPm%2Bvd65FBREY5uEs4c1G86LpEXedES9tSttQEiRfjeviVjahFjyYuIVwOrvtwcCgyFXYKp0NvhMTmPcL0MHcZwWEP8TblRuMxOzExSXzNY9Qe6wcc1QAwO3ysor2KRLMq4F1K8R8ituLRmAgjd7Xp5csurlZc4Uuhy2409NZ841xCEYvmvIHZuLch1PdR%2BWePFMpYT%2Bx%2FpMlUo9mbubXkrqPuXaP9%2FOWHADHMyRFLI%2FiMmKHGjX0nuiD%2BHf%2BAFkytmE4U2aPNjPsZpqev6sXZbQuIxhDQLyJblAyifINLGWinenNcNBbURAtdwFfmUHNWGdHQXydJTlmsy6XJB28x5%2BR%2B5SvRm4TQZMdxOQ6PuysvaidlbPBcAckOc2qbBz%2FFhGdWPgWp%2FCA24TSQ8lebAtUgqs5mw4l8nC8wiDCyiSq0wmvCXvQY6pgFJOGc6PWKmT1%2B2llI95FCuMYjdD4YcgJsn0KQAyIHMZg7GcPKXrVJ19%2BZqHba5flXH1hMbnmzxRSVRe6Ma61Cdk39Et8vkB0vJ8zeBHEYwAWHCJqyC1cfgNq%2Br9CEJmr5dZb%2B%2B5n3WuyhM%2F7JSQfFuL958el4pl9xES7HwgKEmGHLgyPYq%2B9W8L2wYW2FLBF%2B%2FXpNwVudmKc8Ep8lTGotkLLArDBRl&X-Amz-Signature=f3befc40b853b43d3fae2a096a7ad3caf092d21f5000c7424f1bd0fcc6a7d34f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664HHCQIZN%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T122856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJHMEUCIQDvar97lh5GqGQl6ISvyiT5JDiZerTFv5hDK43hHoZ63AIgPKdGx7mB49I7sAYK55GA1i7kTDHvKWKTdd6okLRu5%2BQq%2FwMIdRAAGgw2Mzc0MjMxODM4MDUiDEUAEMuIuVbtr3l9ISrcA1e5aTnu5by4u%2FWR5lwHnm8s%2BmBZaB9ktwRQqG9FZvWv7eVKQpKi4V%2FGwFu0wP%2FtlI1l0PU1wuykdrFVZaGXH4X1ocOepdsqPnP1xuiYuDbFKquC6pq3YmtoI%2BapxlP0zJ4%2FDStHzVzCgS7YpCpdN%2BSpqWxZkGDGKVVnPd2RtZjyef5%2BiAd%2FA%2F6d8mBTzTmv%2BitUBAfevzlUh5ei792%2BwoyMFzXj9zNNQ%2B0RounmxDrl8zGj0pLJ%2FvVAPaVcjACPGlpLT%2BQGEkSqRXybICYOFPi%2B2PJNPSMrEZnqSpJkYvsbUjq9bft5qhbNbtLiOVj47f2Ra66zIne5nCEbMiHvHLJCzd3feeZvw2%2Bm4KorQuVfvLaKGHK4HGTCX0%2BoEfvAEDLp3lSFOo7EfOKIMDyl%2BCf8VnXG5stZSxRhaY3n%2F16Zq5Y50ZeLhEkjdz0SW4Dst91EuAjX198IfEsFtyNKkTxUMViKW0pBPVscHjgkykHZt9wpxKr1qeueBK0M3Q7xAGGhnQyMCpJMkB5uYaBsdqEA5uoABi7Db32UhYWcYl6I2VFLLucWp6A%2BO9MwqjtiiHu0lNd8KsI7QasW9dbAIwYEd1YA1aA0C5bHP57GtlugMl1EHkAfHZ18cWfxMLHvl70GOqUBVhqj0jCY7MZKiGq556nMTA%2F7AFnwZWzeRhjgV5Lu8yWIdssfxUgOlMmuOmJecDFo%2Fjojh%2FChKJj2kKlQHbR1kQ4ax%2B0SfCu5%2FChcvOWa90daJq2ZnsCdU1ciNkp16PSKSBAdu60edCp4N49UNXr8YfhPb06e4lZ5u%2BSJ2%2B6XaBgYQ01MjUH2YfR0NIUMFg5rHmrvWhcAnyzeY0beJ0uOSRsixEW4&X-Amz-Signature=c6d79cd85eb76ec9b316a33b3ec8eb50bf8f49c342051af39542340c5e6eae6f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XDCHU46A%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T122855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJHMEUCIEp%2BRdqBpPJDgYl%2FLlWXZ99FHiW8QXl4B3VMO3ngPnReAiEAya4vDNqVxAlg7gOMTk%2FoJCTpjQn4wwKTpaNy96Z%2BHscq%2FwMIdRAAGgw2Mzc0MjMxODM4MDUiDIWwRZ8NPro49sXThCrcA1cbtkp9n4j%2BQRiZ87bPVo7v4sYTVvOjl20YPt8Ojb9mVMKSLmYkwEYOYgV5kCmKuCPV8V9yq312BGuIFd8tax8aMGiZRWER2fn2wQm5NCo8hNCLU1oFwazktw%2FqlZVzenOdFiHYiFKZRZVxAiadsF9YyGQQ5%2BdQxXlhEAji1fgy%2B6Xs6vwiI9xJYKAedAs6mGx4tB62JDomT%2FihFM%2FK%2BOIinAbqhvhRUFzoGNvRQ0DieZH4OTnyg7KDcBsA0Tx9Orr0M%2BhvWAhie0Lsdi7eBMgHS34Polbq9kRYwJhYJHAQFksM3710r%2BO52tCPP5ZFiV3C%2Fb40%2BNFi4bwSsFXs8oY%2BKamdXY9ds9HNJyV4drQgla4UaoDBHyAsRPpao7pUBTE%2FrpZUMVcEooU%2FCdJYeo7YTJSD9qAaYZLoavXJ5GzlzN2scTBNMgUY%2FHeDTDX%2BgHUpQ4c%2FCYL3KyBqgPdeK9yX2Rxl1%2B6XAyOmclJmRXz9WjAzj6ZZzMr2TlH2OEXBar8a7dlXii%2B%2FllFnqQMLbyhMEtfj8c1Koe0sf7z7XOoOv%2BxEjtIx%2BhPgnyVLHolFtpqAaif3hK3nitxc%2FzTHSehPmtSXUobOIg0epQf7BEk%2FfY%2FpOBg4pgygRNL1MNLwl70GOqUBLjiadap743NIBEi14UCC9b%2FuAWY%2Bw4gGh3LJV5wYKPlP4OI1E3xrYNlyo6eB2Y%2F8fqUbXYDXoOEXmurqc3PdsV5o1fNxD%2F3IebgpKa%2F2Rl788BhHagRjTPWgDsx6xhYu073GVwM6Xp7b45xaoVfPc%2FPalXnytUjoyoFQnwJVoQ%2BMwBEJw5YOvBO5zmAeq%2BUrvkeUyd7sYE65Pa%2F9x2zCfx%2Bk5GVo&X-Amz-Signature=815d2adfd94d0d3fb3843384b78ed6b3e36208cb72f53029efaf3df7213fbe0a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XDCHU46A%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T122855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJHMEUCIEp%2BRdqBpPJDgYl%2FLlWXZ99FHiW8QXl4B3VMO3ngPnReAiEAya4vDNqVxAlg7gOMTk%2FoJCTpjQn4wwKTpaNy96Z%2BHscq%2FwMIdRAAGgw2Mzc0MjMxODM4MDUiDIWwRZ8NPro49sXThCrcA1cbtkp9n4j%2BQRiZ87bPVo7v4sYTVvOjl20YPt8Ojb9mVMKSLmYkwEYOYgV5kCmKuCPV8V9yq312BGuIFd8tax8aMGiZRWER2fn2wQm5NCo8hNCLU1oFwazktw%2FqlZVzenOdFiHYiFKZRZVxAiadsF9YyGQQ5%2BdQxXlhEAji1fgy%2B6Xs6vwiI9xJYKAedAs6mGx4tB62JDomT%2FihFM%2FK%2BOIinAbqhvhRUFzoGNvRQ0DieZH4OTnyg7KDcBsA0Tx9Orr0M%2BhvWAhie0Lsdi7eBMgHS34Polbq9kRYwJhYJHAQFksM3710r%2BO52tCPP5ZFiV3C%2Fb40%2BNFi4bwSsFXs8oY%2BKamdXY9ds9HNJyV4drQgla4UaoDBHyAsRPpao7pUBTE%2FrpZUMVcEooU%2FCdJYeo7YTJSD9qAaYZLoavXJ5GzlzN2scTBNMgUY%2FHeDTDX%2BgHUpQ4c%2FCYL3KyBqgPdeK9yX2Rxl1%2B6XAyOmclJmRXz9WjAzj6ZZzMr2TlH2OEXBar8a7dlXii%2B%2FllFnqQMLbyhMEtfj8c1Koe0sf7z7XOoOv%2BxEjtIx%2BhPgnyVLHolFtpqAaif3hK3nitxc%2FzTHSehPmtSXUobOIg0epQf7BEk%2FfY%2FpOBg4pgygRNL1MNLwl70GOqUBLjiadap743NIBEi14UCC9b%2FuAWY%2Bw4gGh3LJV5wYKPlP4OI1E3xrYNlyo6eB2Y%2F8fqUbXYDXoOEXmurqc3PdsV5o1fNxD%2F3IebgpKa%2F2Rl788BhHagRjTPWgDsx6xhYu073GVwM6Xp7b45xaoVfPc%2FPalXnytUjoyoFQnwJVoQ%2BMwBEJw5YOvBO5zmAeq%2BUrvkeUyd7sYE65Pa%2F9x2zCfx%2Bk5GVo&X-Amz-Signature=298cc2c0b8c2b88f03cb5245ebe736d59c9ed002608a0668be422016438db490&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XDCHU46A%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T122855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJHMEUCIEp%2BRdqBpPJDgYl%2FLlWXZ99FHiW8QXl4B3VMO3ngPnReAiEAya4vDNqVxAlg7gOMTk%2FoJCTpjQn4wwKTpaNy96Z%2BHscq%2FwMIdRAAGgw2Mzc0MjMxODM4MDUiDIWwRZ8NPro49sXThCrcA1cbtkp9n4j%2BQRiZ87bPVo7v4sYTVvOjl20YPt8Ojb9mVMKSLmYkwEYOYgV5kCmKuCPV8V9yq312BGuIFd8tax8aMGiZRWER2fn2wQm5NCo8hNCLU1oFwazktw%2FqlZVzenOdFiHYiFKZRZVxAiadsF9YyGQQ5%2BdQxXlhEAji1fgy%2B6Xs6vwiI9xJYKAedAs6mGx4tB62JDomT%2FihFM%2FK%2BOIinAbqhvhRUFzoGNvRQ0DieZH4OTnyg7KDcBsA0Tx9Orr0M%2BhvWAhie0Lsdi7eBMgHS34Polbq9kRYwJhYJHAQFksM3710r%2BO52tCPP5ZFiV3C%2Fb40%2BNFi4bwSsFXs8oY%2BKamdXY9ds9HNJyV4drQgla4UaoDBHyAsRPpao7pUBTE%2FrpZUMVcEooU%2FCdJYeo7YTJSD9qAaYZLoavXJ5GzlzN2scTBNMgUY%2FHeDTDX%2BgHUpQ4c%2FCYL3KyBqgPdeK9yX2Rxl1%2B6XAyOmclJmRXz9WjAzj6ZZzMr2TlH2OEXBar8a7dlXii%2B%2FllFnqQMLbyhMEtfj8c1Koe0sf7z7XOoOv%2BxEjtIx%2BhPgnyVLHolFtpqAaif3hK3nitxc%2FzTHSehPmtSXUobOIg0epQf7BEk%2FfY%2FpOBg4pgygRNL1MNLwl70GOqUBLjiadap743NIBEi14UCC9b%2FuAWY%2Bw4gGh3LJV5wYKPlP4OI1E3xrYNlyo6eB2Y%2F8fqUbXYDXoOEXmurqc3PdsV5o1fNxD%2F3IebgpKa%2F2Rl788BhHagRjTPWgDsx6xhYu073GVwM6Xp7b45xaoVfPc%2FPalXnytUjoyoFQnwJVoQ%2BMwBEJw5YOvBO5zmAeq%2BUrvkeUyd7sYE65Pa%2F9x2zCfx%2Bk5GVo&X-Amz-Signature=433048f39f1c6c8455e810db61c0bdd6f69b490cf1c1148017fad7b06ad5022d&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XDCHU46A%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T122855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJHMEUCIEp%2BRdqBpPJDgYl%2FLlWXZ99FHiW8QXl4B3VMO3ngPnReAiEAya4vDNqVxAlg7gOMTk%2FoJCTpjQn4wwKTpaNy96Z%2BHscq%2FwMIdRAAGgw2Mzc0MjMxODM4MDUiDIWwRZ8NPro49sXThCrcA1cbtkp9n4j%2BQRiZ87bPVo7v4sYTVvOjl20YPt8Ojb9mVMKSLmYkwEYOYgV5kCmKuCPV8V9yq312BGuIFd8tax8aMGiZRWER2fn2wQm5NCo8hNCLU1oFwazktw%2FqlZVzenOdFiHYiFKZRZVxAiadsF9YyGQQ5%2BdQxXlhEAji1fgy%2B6Xs6vwiI9xJYKAedAs6mGx4tB62JDomT%2FihFM%2FK%2BOIinAbqhvhRUFzoGNvRQ0DieZH4OTnyg7KDcBsA0Tx9Orr0M%2BhvWAhie0Lsdi7eBMgHS34Polbq9kRYwJhYJHAQFksM3710r%2BO52tCPP5ZFiV3C%2Fb40%2BNFi4bwSsFXs8oY%2BKamdXY9ds9HNJyV4drQgla4UaoDBHyAsRPpao7pUBTE%2FrpZUMVcEooU%2FCdJYeo7YTJSD9qAaYZLoavXJ5GzlzN2scTBNMgUY%2FHeDTDX%2BgHUpQ4c%2FCYL3KyBqgPdeK9yX2Rxl1%2B6XAyOmclJmRXz9WjAzj6ZZzMr2TlH2OEXBar8a7dlXii%2B%2FllFnqQMLbyhMEtfj8c1Koe0sf7z7XOoOv%2BxEjtIx%2BhPgnyVLHolFtpqAaif3hK3nitxc%2FzTHSehPmtSXUobOIg0epQf7BEk%2FfY%2FpOBg4pgygRNL1MNLwl70GOqUBLjiadap743NIBEi14UCC9b%2FuAWY%2Bw4gGh3LJV5wYKPlP4OI1E3xrYNlyo6eB2Y%2F8fqUbXYDXoOEXmurqc3PdsV5o1fNxD%2F3IebgpKa%2F2Rl788BhHagRjTPWgDsx6xhYu073GVwM6Xp7b45xaoVfPc%2FPalXnytUjoyoFQnwJVoQ%2BMwBEJw5YOvBO5zmAeq%2BUrvkeUyd7sYE65Pa%2F9x2zCfx%2Bk5GVo&X-Amz-Signature=e35fda7b0cfbe972f87bd6cfa5e9b709a554866b551625b8ad65d82b824ef378&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
