

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665JHHJNYQ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJGMEQCID7TtxsAqgO1yKwVDxo8825xuigxj3FA3Tw4z6eY2wtJAiBQi3HAusOvTefXttjISwuV%2FcxPDAXYrVzI5PPAufYuGir%2FAwg3EAAaDDYzNzQyMzE4MzgwNSIMWzFm9m648whbIRRxKtwD%2F09ofGrEJD40I3FKn8ipMajTjTTIGU4TcSIaB9SZh7Lw1Mc4GNTnpEyAA4Jci7HNo%2BY1ZLG8HFQzUWEz%2FF2lg2XxRoJEfZUrwDuQg5E0%2BphWUnODWnE5RX%2Fk5FY9AMv0%2B6LfnAwMW84mfB66pytxmwHc55DS5BQJNmYtroO5ScItjq7IoB3m0Rewomgudfh7wQ5DaMz24K%2FOKYYGjylZbNnlrnEn%2BeSKq%2FF7V4Crd4HZ%2FeVAqdBeB0XakwUrrh4BIdIWbeu%2BU1T7UVTwqxmo9y4nuR0ztz1RSa5uPwP4zFogI2pjV0K07XMvgr8mde%2Fj5RTLG6g8BIItxolP9uX%2FgUtvRyRfhRPeAjrvXhHUSI4wrx%2FUAVz1NWDeq2%2BNz46P94CalHw4v4bGjEGy%2BWaNLdDUCvJRHQivev813CAOD76s0XOkqeHClr092uwslOyHffaVAsj48AkU1pRzlZOlQktvKmYrmDqqq7gzux7%2BJge1zUxUS%2BYCJ65TOjAgShEH0OnL5Ul9b9OvY6PstnO1432%2Bdv9QSqj1vVg9jfq9fwoXYWh6KOk1eDTUnaa00W43cUBnuhVP%2BtRaZ%2FguMfkT6b1l8Z7qgHRWr6tubL9LymJFQvJjHAo269J%2FbmAw45SKvQY6pgFjOUF5kTeGwwP9TlQLNTSaTzfEFrFjhUXICqnisN1mxWlIs3q7SsiVnAi473TMN0L8H7Y2LiTIPRKEKo%2BZq3I%2B10MKdfEyT9WWeEp3ZWVlUjiO7nUET10vsQ1x%2F41j41ga%2BEw4ZiSlut0s3rT2chaXTXJH5CIdM8BtdCe16qaEXRNk56yBln40ic%2FEHM3ZxWxyGrdG20aDdXs1zRDFQ2pTqNubPRFb&X-Amz-Signature=094a7581a2f621f7f354f3a11306db65ce1de868ecc842cc5cb592fcd8861276&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665JHHJNYQ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJGMEQCID7TtxsAqgO1yKwVDxo8825xuigxj3FA3Tw4z6eY2wtJAiBQi3HAusOvTefXttjISwuV%2FcxPDAXYrVzI5PPAufYuGir%2FAwg3EAAaDDYzNzQyMzE4MzgwNSIMWzFm9m648whbIRRxKtwD%2F09ofGrEJD40I3FKn8ipMajTjTTIGU4TcSIaB9SZh7Lw1Mc4GNTnpEyAA4Jci7HNo%2BY1ZLG8HFQzUWEz%2FF2lg2XxRoJEfZUrwDuQg5E0%2BphWUnODWnE5RX%2Fk5FY9AMv0%2B6LfnAwMW84mfB66pytxmwHc55DS5BQJNmYtroO5ScItjq7IoB3m0Rewomgudfh7wQ5DaMz24K%2FOKYYGjylZbNnlrnEn%2BeSKq%2FF7V4Crd4HZ%2FeVAqdBeB0XakwUrrh4BIdIWbeu%2BU1T7UVTwqxmo9y4nuR0ztz1RSa5uPwP4zFogI2pjV0K07XMvgr8mde%2Fj5RTLG6g8BIItxolP9uX%2FgUtvRyRfhRPeAjrvXhHUSI4wrx%2FUAVz1NWDeq2%2BNz46P94CalHw4v4bGjEGy%2BWaNLdDUCvJRHQivev813CAOD76s0XOkqeHClr092uwslOyHffaVAsj48AkU1pRzlZOlQktvKmYrmDqqq7gzux7%2BJge1zUxUS%2BYCJ65TOjAgShEH0OnL5Ul9b9OvY6PstnO1432%2Bdv9QSqj1vVg9jfq9fwoXYWh6KOk1eDTUnaa00W43cUBnuhVP%2BtRaZ%2FguMfkT6b1l8Z7qgHRWr6tubL9LymJFQvJjHAo269J%2FbmAw45SKvQY6pgFjOUF5kTeGwwP9TlQLNTSaTzfEFrFjhUXICqnisN1mxWlIs3q7SsiVnAi473TMN0L8H7Y2LiTIPRKEKo%2BZq3I%2B10MKdfEyT9WWeEp3ZWVlUjiO7nUET10vsQ1x%2F41j41ga%2BEw4ZiSlut0s3rT2chaXTXJH5CIdM8BtdCe16qaEXRNk56yBln40ic%2FEHM3ZxWxyGrdG20aDdXs1zRDFQ2pTqNubPRFb&X-Amz-Signature=68f77065c0a844b290d9f1c198c644cee22276e248a75fd13ec7499478cc24ac&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665JHHJNYQ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJGMEQCID7TtxsAqgO1yKwVDxo8825xuigxj3FA3Tw4z6eY2wtJAiBQi3HAusOvTefXttjISwuV%2FcxPDAXYrVzI5PPAufYuGir%2FAwg3EAAaDDYzNzQyMzE4MzgwNSIMWzFm9m648whbIRRxKtwD%2F09ofGrEJD40I3FKn8ipMajTjTTIGU4TcSIaB9SZh7Lw1Mc4GNTnpEyAA4Jci7HNo%2BY1ZLG8HFQzUWEz%2FF2lg2XxRoJEfZUrwDuQg5E0%2BphWUnODWnE5RX%2Fk5FY9AMv0%2B6LfnAwMW84mfB66pytxmwHc55DS5BQJNmYtroO5ScItjq7IoB3m0Rewomgudfh7wQ5DaMz24K%2FOKYYGjylZbNnlrnEn%2BeSKq%2FF7V4Crd4HZ%2FeVAqdBeB0XakwUrrh4BIdIWbeu%2BU1T7UVTwqxmo9y4nuR0ztz1RSa5uPwP4zFogI2pjV0K07XMvgr8mde%2Fj5RTLG6g8BIItxolP9uX%2FgUtvRyRfhRPeAjrvXhHUSI4wrx%2FUAVz1NWDeq2%2BNz46P94CalHw4v4bGjEGy%2BWaNLdDUCvJRHQivev813CAOD76s0XOkqeHClr092uwslOyHffaVAsj48AkU1pRzlZOlQktvKmYrmDqqq7gzux7%2BJge1zUxUS%2BYCJ65TOjAgShEH0OnL5Ul9b9OvY6PstnO1432%2Bdv9QSqj1vVg9jfq9fwoXYWh6KOk1eDTUnaa00W43cUBnuhVP%2BtRaZ%2FguMfkT6b1l8Z7qgHRWr6tubL9LymJFQvJjHAo269J%2FbmAw45SKvQY6pgFjOUF5kTeGwwP9TlQLNTSaTzfEFrFjhUXICqnisN1mxWlIs3q7SsiVnAi473TMN0L8H7Y2LiTIPRKEKo%2BZq3I%2B10MKdfEyT9WWeEp3ZWVlUjiO7nUET10vsQ1x%2F41j41ga%2BEw4ZiSlut0s3rT2chaXTXJH5CIdM8BtdCe16qaEXRNk56yBln40ic%2FEHM3ZxWxyGrdG20aDdXs1zRDFQ2pTqNubPRFb&X-Amz-Signature=51f922205439f905c1ae599d0945b3c8e220e688353496ab5d9caeb0298b0ce5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZR2NLLAW%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCIAfxzhYnKITNJ9j55qkHNU%2FBHrkkuS4%2BQQVJ2aFNcnYbAiEA%2BS3RCd2t6PjKD7zmKX1Kful9rfejD4kGFimWlEuuAHkq%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDLe%2BhYW2xTNgRC48LCrcA3748egqeVG1dyc2kKWgwUW7yijbIJ2qvlbrzLDoJ4l5Yb4A3QVfQUG24fkIdlIbR6xgWc8S%2BNaB4I%2BMlqQDPqV5PuecYKen%2FLsM7f0Gu4OXTkqXvG6DXkpQchjjWoVlz7tG%2BbKBIl0dNNMU21IjnwxfU4CZnjI%2BtT70DEJT2%2Bhmz98ERnYSBn8jt1A3XfjEiK3RckMkK8YSa%2B5CTR40dIVw16qmP7qYA%2Fq6RIfXpGQQS%2BnfSUshxezpNd1vu1mvigcOUJh9IZKtIbjMugax3Nvie%2F5Rw6xRgx%2F2ZuntZBsfS%2BLT9FlUiOazCF1DpdUdcGPVrR3V1S7ferRY52orW01spJ2CQ7Uaxy%2B2nsJnfNVQjO7srYxoGcugIPWzIORh9%2Fer%2BXIgQ05mxI%2BN9YxPJ%2ByKzJ9QozKdEmdezCxomkqh33eMXWr5DpJqox7TjkrwFy3pUjtP1eEck1IheJCkw5DZQ5uWKUQo9uuYUJTESOKUsv2rlqRgzaWU8PbeTHJv0Rkhs8vsU%2FHgEpfCGV7MA1tnW4S37h3mgSOF1uc1C%2FY75vtU6xzBuxVXvWCuo%2B5DWE4ADxdHJCfvSOZbwu1fkTjvpO7XbFlEhDeGFvvp6lSu9HpPKRNEZMII8eMqMIGUir0GOqUB4UiTJotHM27EOLYRItH4eaeU%2FK1QIK268gziSyBbmPbTyvOzO1Xem2qvcLThxERPHI9zHpsBSEAxkpKPAGD26hM5ZNmCs%2Bd5u9%2FOgWuITMlWn31%2FfGVVdQJtO%2B9rhQ2Ek4ChQx9b%2B%2BCl4astakpWCBC1cXN1w4pWaRbH84%2F5zROMSSm8pZK4MRLs51dV20v1wSJF%2FtNzn8yQY1eHD5CJx%2FHC4TFT&X-Amz-Signature=b7c989d6f1877d4f0773c40c64af470c5bf94bad1d74eb4b23f0fab558505c4d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46633FHDHD6%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJGMEQCIGMUBjkMH74%2Fhcc7sFoqUTUTVtoG6VgBa3rnSNwc9NImAiBNgBxjZQrRweN8lrTVWHeEee4tV93znknCqgEhik%2Ft5yr%2FAwg3EAAaDDYzNzQyMzE4MzgwNSIMxJ9wH%2Fkdr5V%2FNDEuKtwD0tnaPMHIMmYy3r8R0tHVT4rz%2BDK%2BtaysUNfppSTZiDN9LodOWrKOF%2B%2FR1%2FjZYpD7d1hRcuyXqKWGQN%2F4322O8fIq20pSHQesHHJ%2FSApHQ4EwHCU6vl1xLF8hCXAJtYxehhck3EsEwVIz3hboerq%2BvsCGKVT8MO9ndsOZtwf6AnDol5MW22G2WqO4IQQ5fh66Cd5HMbYDrmXjF0ktXDsVQHlSm0zokvRSE0D1j2gaEZuFFr2PR2E7l7C%2Bnp0ip3QnY7wQ8ahavgt0rtOpYwel7pcibSVrCfJZaXwi4FWm5YBfxqIf7sldfsyUVfw9b%2BCrvzPT%2BvnYTJaejel56gnUBeq0A2BGM5CJKiZG%2B%2BiNDtxMgcCNAoGzBSYuyGYGQ3uGhzlQ2JDxzABZHwLmc6%2FNHxvMm4f0JImGFLHatqyzbQAQN%2Fm%2F%2FQRJ1w4wc4oohF6oDGFhXye4aOtZoD4OwlYT%2F1arM7SdZsvmJWCHQMub%2BtWwySZC09X8y1hA7RgR4y2lybz43voDq4lLjky2i1LKvJQxCsCrLoN1I53ekbyiKflglwn9UCJ3417Y%2BuZ%2F%2Bxc%2Ff3JgDOpIyCvsIcMAAahluDPAQ%2FcxyOF0Zm2%2FE18fJFs4bJM5dO936uQw%2BIcw2pSKvQY6pgHWytUIv2Damlp6d3MHQ%2FFx2ugScTXSsXZEhamhSrcGf137xnb8YXDx8t%2FewjlcmISd%2BCfXySX3pmNJGpf8G46cJezCnYOCINrn9cp0nMaSGFy4xXHXqRDSBYWutT48L%2Blg5NgEF3yxWI1X2lBhLBuu8KgQAhqS%2Fa1EJzfytzqb6fBMACDuQfH12x76u4P0nBZFMmiq2rs6hG%2BnDwB7%2FIEpYwfXQd%2Bi&X-Amz-Signature=741ca50b7a9b3fe1cadd0b8ef877ff9f131130182ed0b9125bcf9bfa81e4884a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665JHHJNYQ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJGMEQCID7TtxsAqgO1yKwVDxo8825xuigxj3FA3Tw4z6eY2wtJAiBQi3HAusOvTefXttjISwuV%2FcxPDAXYrVzI5PPAufYuGir%2FAwg3EAAaDDYzNzQyMzE4MzgwNSIMWzFm9m648whbIRRxKtwD%2F09ofGrEJD40I3FKn8ipMajTjTTIGU4TcSIaB9SZh7Lw1Mc4GNTnpEyAA4Jci7HNo%2BY1ZLG8HFQzUWEz%2FF2lg2XxRoJEfZUrwDuQg5E0%2BphWUnODWnE5RX%2Fk5FY9AMv0%2B6LfnAwMW84mfB66pytxmwHc55DS5BQJNmYtroO5ScItjq7IoB3m0Rewomgudfh7wQ5DaMz24K%2FOKYYGjylZbNnlrnEn%2BeSKq%2FF7V4Crd4HZ%2FeVAqdBeB0XakwUrrh4BIdIWbeu%2BU1T7UVTwqxmo9y4nuR0ztz1RSa5uPwP4zFogI2pjV0K07XMvgr8mde%2Fj5RTLG6g8BIItxolP9uX%2FgUtvRyRfhRPeAjrvXhHUSI4wrx%2FUAVz1NWDeq2%2BNz46P94CalHw4v4bGjEGy%2BWaNLdDUCvJRHQivev813CAOD76s0XOkqeHClr092uwslOyHffaVAsj48AkU1pRzlZOlQktvKmYrmDqqq7gzux7%2BJge1zUxUS%2BYCJ65TOjAgShEH0OnL5Ul9b9OvY6PstnO1432%2Bdv9QSqj1vVg9jfq9fwoXYWh6KOk1eDTUnaa00W43cUBnuhVP%2BtRaZ%2FguMfkT6b1l8Z7qgHRWr6tubL9LymJFQvJjHAo269J%2FbmAw45SKvQY6pgFjOUF5kTeGwwP9TlQLNTSaTzfEFrFjhUXICqnisN1mxWlIs3q7SsiVnAi473TMN0L8H7Y2LiTIPRKEKo%2BZq3I%2B10MKdfEyT9WWeEp3ZWVlUjiO7nUET10vsQ1x%2F41j41ga%2BEw4ZiSlut0s3rT2chaXTXJH5CIdM8BtdCe16qaEXRNk56yBln40ic%2FEHM3ZxWxyGrdG20aDdXs1zRDFQ2pTqNubPRFb&X-Amz-Signature=f8d878a1ef42a481e7165fab267a80dd47cc148e5b8812bb5212d0e98e3e0fa5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665JHHJNYQ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJGMEQCID7TtxsAqgO1yKwVDxo8825xuigxj3FA3Tw4z6eY2wtJAiBQi3HAusOvTefXttjISwuV%2FcxPDAXYrVzI5PPAufYuGir%2FAwg3EAAaDDYzNzQyMzE4MzgwNSIMWzFm9m648whbIRRxKtwD%2F09ofGrEJD40I3FKn8ipMajTjTTIGU4TcSIaB9SZh7Lw1Mc4GNTnpEyAA4Jci7HNo%2BY1ZLG8HFQzUWEz%2FF2lg2XxRoJEfZUrwDuQg5E0%2BphWUnODWnE5RX%2Fk5FY9AMv0%2B6LfnAwMW84mfB66pytxmwHc55DS5BQJNmYtroO5ScItjq7IoB3m0Rewomgudfh7wQ5DaMz24K%2FOKYYGjylZbNnlrnEn%2BeSKq%2FF7V4Crd4HZ%2FeVAqdBeB0XakwUrrh4BIdIWbeu%2BU1T7UVTwqxmo9y4nuR0ztz1RSa5uPwP4zFogI2pjV0K07XMvgr8mde%2Fj5RTLG6g8BIItxolP9uX%2FgUtvRyRfhRPeAjrvXhHUSI4wrx%2FUAVz1NWDeq2%2BNz46P94CalHw4v4bGjEGy%2BWaNLdDUCvJRHQivev813CAOD76s0XOkqeHClr092uwslOyHffaVAsj48AkU1pRzlZOlQktvKmYrmDqqq7gzux7%2BJge1zUxUS%2BYCJ65TOjAgShEH0OnL5Ul9b9OvY6PstnO1432%2Bdv9QSqj1vVg9jfq9fwoXYWh6KOk1eDTUnaa00W43cUBnuhVP%2BtRaZ%2FguMfkT6b1l8Z7qgHRWr6tubL9LymJFQvJjHAo269J%2FbmAw45SKvQY6pgFjOUF5kTeGwwP9TlQLNTSaTzfEFrFjhUXICqnisN1mxWlIs3q7SsiVnAi473TMN0L8H7Y2LiTIPRKEKo%2BZq3I%2B10MKdfEyT9WWeEp3ZWVlUjiO7nUET10vsQ1x%2F41j41ga%2BEw4ZiSlut0s3rT2chaXTXJH5CIdM8BtdCe16qaEXRNk56yBln40ic%2FEHM3ZxWxyGrdG20aDdXs1zRDFQ2pTqNubPRFb&X-Amz-Signature=80642d3adc69f06d3fe362014f7b22da602723e5bf0a7048f7866ddbe259e6d2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665JHHJNYQ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJGMEQCID7TtxsAqgO1yKwVDxo8825xuigxj3FA3Tw4z6eY2wtJAiBQi3HAusOvTefXttjISwuV%2FcxPDAXYrVzI5PPAufYuGir%2FAwg3EAAaDDYzNzQyMzE4MzgwNSIMWzFm9m648whbIRRxKtwD%2F09ofGrEJD40I3FKn8ipMajTjTTIGU4TcSIaB9SZh7Lw1Mc4GNTnpEyAA4Jci7HNo%2BY1ZLG8HFQzUWEz%2FF2lg2XxRoJEfZUrwDuQg5E0%2BphWUnODWnE5RX%2Fk5FY9AMv0%2B6LfnAwMW84mfB66pytxmwHc55DS5BQJNmYtroO5ScItjq7IoB3m0Rewomgudfh7wQ5DaMz24K%2FOKYYGjylZbNnlrnEn%2BeSKq%2FF7V4Crd4HZ%2FeVAqdBeB0XakwUrrh4BIdIWbeu%2BU1T7UVTwqxmo9y4nuR0ztz1RSa5uPwP4zFogI2pjV0K07XMvgr8mde%2Fj5RTLG6g8BIItxolP9uX%2FgUtvRyRfhRPeAjrvXhHUSI4wrx%2FUAVz1NWDeq2%2BNz46P94CalHw4v4bGjEGy%2BWaNLdDUCvJRHQivev813CAOD76s0XOkqeHClr092uwslOyHffaVAsj48AkU1pRzlZOlQktvKmYrmDqqq7gzux7%2BJge1zUxUS%2BYCJ65TOjAgShEH0OnL5Ul9b9OvY6PstnO1432%2Bdv9QSqj1vVg9jfq9fwoXYWh6KOk1eDTUnaa00W43cUBnuhVP%2BtRaZ%2FguMfkT6b1l8Z7qgHRWr6tubL9LymJFQvJjHAo269J%2FbmAw45SKvQY6pgFjOUF5kTeGwwP9TlQLNTSaTzfEFrFjhUXICqnisN1mxWlIs3q7SsiVnAi473TMN0L8H7Y2LiTIPRKEKo%2BZq3I%2B10MKdfEyT9WWeEp3ZWVlUjiO7nUET10vsQ1x%2F41j41ga%2BEw4ZiSlut0s3rT2chaXTXJH5CIdM8BtdCe16qaEXRNk56yBln40ic%2FEHM3ZxWxyGrdG20aDdXs1zRDFQ2pTqNubPRFb&X-Amz-Signature=a83a933bc47a43ca70e402d49781d2b8af5013786239d273e778350d37b6fded&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665JHHJNYQ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJGMEQCID7TtxsAqgO1yKwVDxo8825xuigxj3FA3Tw4z6eY2wtJAiBQi3HAusOvTefXttjISwuV%2FcxPDAXYrVzI5PPAufYuGir%2FAwg3EAAaDDYzNzQyMzE4MzgwNSIMWzFm9m648whbIRRxKtwD%2F09ofGrEJD40I3FKn8ipMajTjTTIGU4TcSIaB9SZh7Lw1Mc4GNTnpEyAA4Jci7HNo%2BY1ZLG8HFQzUWEz%2FF2lg2XxRoJEfZUrwDuQg5E0%2BphWUnODWnE5RX%2Fk5FY9AMv0%2B6LfnAwMW84mfB66pytxmwHc55DS5BQJNmYtroO5ScItjq7IoB3m0Rewomgudfh7wQ5DaMz24K%2FOKYYGjylZbNnlrnEn%2BeSKq%2FF7V4Crd4HZ%2FeVAqdBeB0XakwUrrh4BIdIWbeu%2BU1T7UVTwqxmo9y4nuR0ztz1RSa5uPwP4zFogI2pjV0K07XMvgr8mde%2Fj5RTLG6g8BIItxolP9uX%2FgUtvRyRfhRPeAjrvXhHUSI4wrx%2FUAVz1NWDeq2%2BNz46P94CalHw4v4bGjEGy%2BWaNLdDUCvJRHQivev813CAOD76s0XOkqeHClr092uwslOyHffaVAsj48AkU1pRzlZOlQktvKmYrmDqqq7gzux7%2BJge1zUxUS%2BYCJ65TOjAgShEH0OnL5Ul9b9OvY6PstnO1432%2Bdv9QSqj1vVg9jfq9fwoXYWh6KOk1eDTUnaa00W43cUBnuhVP%2BtRaZ%2FguMfkT6b1l8Z7qgHRWr6tubL9LymJFQvJjHAo269J%2FbmAw45SKvQY6pgFjOUF5kTeGwwP9TlQLNTSaTzfEFrFjhUXICqnisN1mxWlIs3q7SsiVnAi473TMN0L8H7Y2LiTIPRKEKo%2BZq3I%2B10MKdfEyT9WWeEp3ZWVlUjiO7nUET10vsQ1x%2F41j41ga%2BEw4ZiSlut0s3rT2chaXTXJH5CIdM8BtdCe16qaEXRNk56yBln40ic%2FEHM3ZxWxyGrdG20aDdXs1zRDFQ2pTqNubPRFb&X-Amz-Signature=f3ebde1ebd6dc612c765ea2de52b21763dee31d958875abdc4ab1001e21d3a1c&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
