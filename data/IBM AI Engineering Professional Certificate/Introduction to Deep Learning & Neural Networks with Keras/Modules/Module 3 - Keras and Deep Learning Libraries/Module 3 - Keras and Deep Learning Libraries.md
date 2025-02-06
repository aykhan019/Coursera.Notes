

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QYJMYCEL%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIEmvjuODMtGgRr2d8pvpKH61UnamgxmWfsxHT8aP2YEnAiEA3NOXblE6beCG0WhnbmdZloFzJxbnZfDqo16orDpwJ2Mq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDH0H6dcOJpsp9Sk3bSrcAzA9j2Bvg1CnOrtX%2BLs2%2FamIMZppHEwui0LAeYw9JBfq7D%2FsPk8QPpeAqo0sbT%2FO%2Fx2ZQmLMoJN3mpigcNAiWZFtTI6BAB9yoxfCNo5Fgv605UBfXx2ipobOnx%2FwXu769Q%2FZ6lz5KnM4PLjVz8gyi4LjWM6WAMhtT07bDE%2B0zYaewIuAn14jR0D8amMQPqX0OIjTfSGzmA43LJ%2F1e40U6fvHMC%2FsLI2xcvtsTpMOJH0%2BAGJ%2FILgEf7MS7Qqzacpq%2BzQQowL9hnrp1TMy%2FogmZVHr9x4hwibzU%2B8vzpbV%2BVNynCD720RTIDdFCCb1sgJi9nwVkQOQdzOCSPozBf7y%2FrGFX8mktFQtnc%2BnJtTw47kOJZaRtPZqCGu1KKNHieiuAhqKkrVpW9XqufUIi0P2AvJWZYtbwPFougMVowaFxFObHudeJzuQUP19LPqUPj2%2F3D2666D8eICmxu3%2BgEnGb5Ot%2FcULFf6WxSd6aEw2Mol4tMZJkrdWt9SSzlvPjDxN4flV0v254xARCYmwLEXoy0yWfEbYUhRoJ1N9z0vv5mviL3MiW7Gs%2Bvkyggtn5CYaJKPqAiOLvFQdvQ%2FP3HHiC6f18S1URf3hEERIpFZvwvw5dUTqhuO9LnuHckCoMPe3lL0GOqUBcvq4zNe1LMOZ2xzFG%2FyiKmwiYYRB7anLlCO5wOZoz9tCs8BuXqxWjbwSKuk7Tp%2FTtefHMwepoaAVruAtGqNwyOKfbUB6tfn6FhM6duInoPoBlH%2FmntSBOscUREPoQJI%2BgBXRLFtw0vo7QhZf0yNURdW2HNLt9FhytBZaWf8PPiRzaz1oQnEr%2FYoVixSBuGWed0%2Br3JykFO4Y%2BDQLF5%2BD5l6nGf0v&X-Amz-Signature=edd33a12d24a69dcdff9c8cf0a470b898036c8d16c120ec80f2c19c0adcf32fb&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QYJMYCEL%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIEmvjuODMtGgRr2d8pvpKH61UnamgxmWfsxHT8aP2YEnAiEA3NOXblE6beCG0WhnbmdZloFzJxbnZfDqo16orDpwJ2Mq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDH0H6dcOJpsp9Sk3bSrcAzA9j2Bvg1CnOrtX%2BLs2%2FamIMZppHEwui0LAeYw9JBfq7D%2FsPk8QPpeAqo0sbT%2FO%2Fx2ZQmLMoJN3mpigcNAiWZFtTI6BAB9yoxfCNo5Fgv605UBfXx2ipobOnx%2FwXu769Q%2FZ6lz5KnM4PLjVz8gyi4LjWM6WAMhtT07bDE%2B0zYaewIuAn14jR0D8amMQPqX0OIjTfSGzmA43LJ%2F1e40U6fvHMC%2FsLI2xcvtsTpMOJH0%2BAGJ%2FILgEf7MS7Qqzacpq%2BzQQowL9hnrp1TMy%2FogmZVHr9x4hwibzU%2B8vzpbV%2BVNynCD720RTIDdFCCb1sgJi9nwVkQOQdzOCSPozBf7y%2FrGFX8mktFQtnc%2BnJtTw47kOJZaRtPZqCGu1KKNHieiuAhqKkrVpW9XqufUIi0P2AvJWZYtbwPFougMVowaFxFObHudeJzuQUP19LPqUPj2%2F3D2666D8eICmxu3%2BgEnGb5Ot%2FcULFf6WxSd6aEw2Mol4tMZJkrdWt9SSzlvPjDxN4flV0v254xARCYmwLEXoy0yWfEbYUhRoJ1N9z0vv5mviL3MiW7Gs%2Bvkyggtn5CYaJKPqAiOLvFQdvQ%2FP3HHiC6f18S1URf3hEERIpFZvwvw5dUTqhuO9LnuHckCoMPe3lL0GOqUBcvq4zNe1LMOZ2xzFG%2FyiKmwiYYRB7anLlCO5wOZoz9tCs8BuXqxWjbwSKuk7Tp%2FTtefHMwepoaAVruAtGqNwyOKfbUB6tfn6FhM6duInoPoBlH%2FmntSBOscUREPoQJI%2BgBXRLFtw0vo7QhZf0yNURdW2HNLt9FhytBZaWf8PPiRzaz1oQnEr%2FYoVixSBuGWed0%2Br3JykFO4Y%2BDQLF5%2BD5l6nGf0v&X-Amz-Signature=389ee3fca3c30673fcbc8f866b35eec6954287ca99f66797cbe25649474616b0&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QYJMYCEL%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIEmvjuODMtGgRr2d8pvpKH61UnamgxmWfsxHT8aP2YEnAiEA3NOXblE6beCG0WhnbmdZloFzJxbnZfDqo16orDpwJ2Mq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDH0H6dcOJpsp9Sk3bSrcAzA9j2Bvg1CnOrtX%2BLs2%2FamIMZppHEwui0LAeYw9JBfq7D%2FsPk8QPpeAqo0sbT%2FO%2Fx2ZQmLMoJN3mpigcNAiWZFtTI6BAB9yoxfCNo5Fgv605UBfXx2ipobOnx%2FwXu769Q%2FZ6lz5KnM4PLjVz8gyi4LjWM6WAMhtT07bDE%2B0zYaewIuAn14jR0D8amMQPqX0OIjTfSGzmA43LJ%2F1e40U6fvHMC%2FsLI2xcvtsTpMOJH0%2BAGJ%2FILgEf7MS7Qqzacpq%2BzQQowL9hnrp1TMy%2FogmZVHr9x4hwibzU%2B8vzpbV%2BVNynCD720RTIDdFCCb1sgJi9nwVkQOQdzOCSPozBf7y%2FrGFX8mktFQtnc%2BnJtTw47kOJZaRtPZqCGu1KKNHieiuAhqKkrVpW9XqufUIi0P2AvJWZYtbwPFougMVowaFxFObHudeJzuQUP19LPqUPj2%2F3D2666D8eICmxu3%2BgEnGb5Ot%2FcULFf6WxSd6aEw2Mol4tMZJkrdWt9SSzlvPjDxN4flV0v254xARCYmwLEXoy0yWfEbYUhRoJ1N9z0vv5mviL3MiW7Gs%2Bvkyggtn5CYaJKPqAiOLvFQdvQ%2FP3HHiC6f18S1URf3hEERIpFZvwvw5dUTqhuO9LnuHckCoMPe3lL0GOqUBcvq4zNe1LMOZ2xzFG%2FyiKmwiYYRB7anLlCO5wOZoz9tCs8BuXqxWjbwSKuk7Tp%2FTtefHMwepoaAVruAtGqNwyOKfbUB6tfn6FhM6duInoPoBlH%2FmntSBOscUREPoQJI%2BgBXRLFtw0vo7QhZf0yNURdW2HNLt9FhytBZaWf8PPiRzaz1oQnEr%2FYoVixSBuGWed0%2Br3JykFO4Y%2BDQLF5%2BD5l6nGf0v&X-Amz-Signature=52ee51edc0dbee7f32203236860c5c61ae8332eae48639d13d495641b1c7ba7e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMZNRB77%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221415Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJGMEQCIFTx5EOK%2FsyDCjiUcsTiEenohRl5iPQylmBpJDdXQnoRAiAfSWQiro3IPN3E5V%2BQIG5hIMOLM7unnxWZqbbAfwqV5ir%2FAwhmEAAaDDYzNzQyMzE4MzgwNSIMJ4Mmp7XHxdW2RCeUKtwDZEAN%2BgvIpCcvQboBUVuULVLmCkz6zh5L8XuiIOhjtJRTDEyZs%2BYt%2FsLV%2FLcX2bkzLU4mntbjAtLy2zPvD%2Fdydl2GHkt0g7f2t%2FJhYMMXKlHWnkOQmQK%2F30vCw52gj%2B1cj4RCgNlWyWGqtvgJlQNRzA6yqWCanKM4xC6xtG7HUE52YtZcBDCNLISl6AvoqAzLS4syDlrwfzwIJjQmfLcDvP8S823j7KHcOc70tlmCAAlTXCCoRwbxu9v3S3PLRi1sj1dLgzUejxSRkO%2FXj9kbIj7KiA3NwWIGf5UPK8Z11aZt1Pj57zfMFhLONJiJFdVVPNac%2F5TMbmrJ053CsZhJqK%2BSBaE61pv3rxmz26yJBOMJqojOGxOY6v7OZHgnB9i2hsas4HTzdseCew7xEiq6o5Dbp6mHmX5CKWYJrY8TwwwWnod9eSU1l%2B9hfcxWoMp6b%2B05A71jGevw8YmY0erduqwSy4%2Ffx6RPWtQboA5w4tswGUimZ1jTbMgnXxMWwIIv%2FC5toiOzc65LOSNe7PJrdrML1Alj10MyKz146utKdcje4JNwIJkr4B3JS08Eoba%2FP7gwcFvvx70PQnBTH%2FfXEfyvrWuRJ8Uo1BogGlklPnsc8G5xeKwJ5d2bolQw47eUvQY6pgElZJHSFgv5XwwcuBftrcilcvbAVQNEwB1fTjb2KOV5TeP73bpNqPRPPlEunN3iDqQsOAxCqabHM6%2B%2FcDEX%2BX%2BPSU5XZ9Q%2FX%2BHHE10V4eqAtNcifwx8cWlIoysGTILyASsPN8XOX49M4coiUh3PYZh93lVfZw1GCI1NZwiJgE6i%2FAz%2FBY42HASXPOpIwHENeB9UmBsFk6X13hQXeHKSE4TXkOcynGO8&X-Amz-Signature=4e7bad5b64bf2e58c040552e23d90689a665ec77c196ec1d2b24c814cc6bf108&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665Z6MOZPH%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221412Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJGMEQCIAWiLfohYAP6ohC6rUV45G4E2wLfQouu0osa2H%2FV5egKAiAPFVe9rgj%2BlXiKAnd9c%2Fmcd8prV16pI4RtEG55EGBuzyr%2FAwhmEAAaDDYzNzQyMzE4MzgwNSIMs2nrlI629QKK%2BTMrKtwDzi9%2FHVKEps0loLfuI2H0NknAM9SBSkjkO%2BdztGyhFpNcGVramQGkoEl6vfAcUsSjCMrLYreoZefkZ2aqN%2FnVDh3OFh9MQtzlzKX%2BaauG4F%2Bisjn6JiGFB5nXV0LGCnaZ5oFGpLqKv2i5vaoBSLtb52DgGRnjtY9HTR%2BMErHkGZ%2BMsdS2BIc5ekI%2FIuJBKhIhoAwYFRxWNeTE7B5RCnGxa9LVeXFW2IWH2CrcjP10dbf5VX5bphu669EG6FpVyyGK1P0cBMTZUfW7YGBJOfi3JWd8fWFyhcK7ZGHLRTxkucJfyLqYeprJ0j3ZuZYVg3aWBlvrK3OoubW7r9oe3Agpuk1lBFT5r5NpWGUDNgXjRI42RoiHoc%2BDAMXMNqA6cD9dHrC5nrRmeUjZZkvGynTZTDHiIanGVPPDFEYe4u7Jddj0CNw20T1h%2BPJjjzL0cXzf8S4L17I5yHRi0Jg2GoMpkNquUythemudjdtollxOm7zuMaq6uTca0wRaa8Irf9BSEA4XdlZFdDUjfQo2qWJegZCIiP0Qi22PR7IR3EJNS%2FHxnUyXDYMYjezK1nafFH3WH4o8BLIP%2BdecR56ojKZo0xVJzt%2FEsCEJb%2B%2By3kimlWMMOxUPODjwOHjU%2FlYwxbiUvQY6pgHfrd0fI8bMhC9y%2Fe8T7GkuqUk1NZNlZ4DGoTOIFGYt48F50Fv7QEU4br3szcOlv8Dlw3t3CvDx6Mho98VCA0aeLniaPL%2BT68RHDVhMCPSOTYJPyVyMcloaL%2BC3YXNKt3mrn9PYmMvlt9Tyt0mH2rbherT9l6nskQwATI8H75aWHxhkXtTcNvM%2B%2F8p%2BwNsKH5W9qPLNFENz4MwoJSA1Ux4eKuw2hTJm&X-Amz-Signature=4b829b28c9ca22c52fc225fc4a1bc7db440b08f5fc6d19df767555d0d6c67063&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QYJMYCEL%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIEmvjuODMtGgRr2d8pvpKH61UnamgxmWfsxHT8aP2YEnAiEA3NOXblE6beCG0WhnbmdZloFzJxbnZfDqo16orDpwJ2Mq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDH0H6dcOJpsp9Sk3bSrcAzA9j2Bvg1CnOrtX%2BLs2%2FamIMZppHEwui0LAeYw9JBfq7D%2FsPk8QPpeAqo0sbT%2FO%2Fx2ZQmLMoJN3mpigcNAiWZFtTI6BAB9yoxfCNo5Fgv605UBfXx2ipobOnx%2FwXu769Q%2FZ6lz5KnM4PLjVz8gyi4LjWM6WAMhtT07bDE%2B0zYaewIuAn14jR0D8amMQPqX0OIjTfSGzmA43LJ%2F1e40U6fvHMC%2FsLI2xcvtsTpMOJH0%2BAGJ%2FILgEf7MS7Qqzacpq%2BzQQowL9hnrp1TMy%2FogmZVHr9x4hwibzU%2B8vzpbV%2BVNynCD720RTIDdFCCb1sgJi9nwVkQOQdzOCSPozBf7y%2FrGFX8mktFQtnc%2BnJtTw47kOJZaRtPZqCGu1KKNHieiuAhqKkrVpW9XqufUIi0P2AvJWZYtbwPFougMVowaFxFObHudeJzuQUP19LPqUPj2%2F3D2666D8eICmxu3%2BgEnGb5Ot%2FcULFf6WxSd6aEw2Mol4tMZJkrdWt9SSzlvPjDxN4flV0v254xARCYmwLEXoy0yWfEbYUhRoJ1N9z0vv5mviL3MiW7Gs%2Bvkyggtn5CYaJKPqAiOLvFQdvQ%2FP3HHiC6f18S1URf3hEERIpFZvwvw5dUTqhuO9LnuHckCoMPe3lL0GOqUBcvq4zNe1LMOZ2xzFG%2FyiKmwiYYRB7anLlCO5wOZoz9tCs8BuXqxWjbwSKuk7Tp%2FTtefHMwepoaAVruAtGqNwyOKfbUB6tfn6FhM6duInoPoBlH%2FmntSBOscUREPoQJI%2BgBXRLFtw0vo7QhZf0yNURdW2HNLt9FhytBZaWf8PPiRzaz1oQnEr%2FYoVixSBuGWed0%2Br3JykFO4Y%2BDQLF5%2BD5l6nGf0v&X-Amz-Signature=245019fbf1bd21e9c44383bdf91e64727be4163d945f3dc0df133477e011f9ac&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QYJMYCEL%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIEmvjuODMtGgRr2d8pvpKH61UnamgxmWfsxHT8aP2YEnAiEA3NOXblE6beCG0WhnbmdZloFzJxbnZfDqo16orDpwJ2Mq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDH0H6dcOJpsp9Sk3bSrcAzA9j2Bvg1CnOrtX%2BLs2%2FamIMZppHEwui0LAeYw9JBfq7D%2FsPk8QPpeAqo0sbT%2FO%2Fx2ZQmLMoJN3mpigcNAiWZFtTI6BAB9yoxfCNo5Fgv605UBfXx2ipobOnx%2FwXu769Q%2FZ6lz5KnM4PLjVz8gyi4LjWM6WAMhtT07bDE%2B0zYaewIuAn14jR0D8amMQPqX0OIjTfSGzmA43LJ%2F1e40U6fvHMC%2FsLI2xcvtsTpMOJH0%2BAGJ%2FILgEf7MS7Qqzacpq%2BzQQowL9hnrp1TMy%2FogmZVHr9x4hwibzU%2B8vzpbV%2BVNynCD720RTIDdFCCb1sgJi9nwVkQOQdzOCSPozBf7y%2FrGFX8mktFQtnc%2BnJtTw47kOJZaRtPZqCGu1KKNHieiuAhqKkrVpW9XqufUIi0P2AvJWZYtbwPFougMVowaFxFObHudeJzuQUP19LPqUPj2%2F3D2666D8eICmxu3%2BgEnGb5Ot%2FcULFf6WxSd6aEw2Mol4tMZJkrdWt9SSzlvPjDxN4flV0v254xARCYmwLEXoy0yWfEbYUhRoJ1N9z0vv5mviL3MiW7Gs%2Bvkyggtn5CYaJKPqAiOLvFQdvQ%2FP3HHiC6f18S1URf3hEERIpFZvwvw5dUTqhuO9LnuHckCoMPe3lL0GOqUBcvq4zNe1LMOZ2xzFG%2FyiKmwiYYRB7anLlCO5wOZoz9tCs8BuXqxWjbwSKuk7Tp%2FTtefHMwepoaAVruAtGqNwyOKfbUB6tfn6FhM6duInoPoBlH%2FmntSBOscUREPoQJI%2BgBXRLFtw0vo7QhZf0yNURdW2HNLt9FhytBZaWf8PPiRzaz1oQnEr%2FYoVixSBuGWed0%2Br3JykFO4Y%2BDQLF5%2BD5l6nGf0v&X-Amz-Signature=7cb586b6d67c6ab82c0fc839a8c54b78e616fc960fcf566c8493720dfd25e09c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QYJMYCEL%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIEmvjuODMtGgRr2d8pvpKH61UnamgxmWfsxHT8aP2YEnAiEA3NOXblE6beCG0WhnbmdZloFzJxbnZfDqo16orDpwJ2Mq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDH0H6dcOJpsp9Sk3bSrcAzA9j2Bvg1CnOrtX%2BLs2%2FamIMZppHEwui0LAeYw9JBfq7D%2FsPk8QPpeAqo0sbT%2FO%2Fx2ZQmLMoJN3mpigcNAiWZFtTI6BAB9yoxfCNo5Fgv605UBfXx2ipobOnx%2FwXu769Q%2FZ6lz5KnM4PLjVz8gyi4LjWM6WAMhtT07bDE%2B0zYaewIuAn14jR0D8amMQPqX0OIjTfSGzmA43LJ%2F1e40U6fvHMC%2FsLI2xcvtsTpMOJH0%2BAGJ%2FILgEf7MS7Qqzacpq%2BzQQowL9hnrp1TMy%2FogmZVHr9x4hwibzU%2B8vzpbV%2BVNynCD720RTIDdFCCb1sgJi9nwVkQOQdzOCSPozBf7y%2FrGFX8mktFQtnc%2BnJtTw47kOJZaRtPZqCGu1KKNHieiuAhqKkrVpW9XqufUIi0P2AvJWZYtbwPFougMVowaFxFObHudeJzuQUP19LPqUPj2%2F3D2666D8eICmxu3%2BgEnGb5Ot%2FcULFf6WxSd6aEw2Mol4tMZJkrdWt9SSzlvPjDxN4flV0v254xARCYmwLEXoy0yWfEbYUhRoJ1N9z0vv5mviL3MiW7Gs%2Bvkyggtn5CYaJKPqAiOLvFQdvQ%2FP3HHiC6f18S1URf3hEERIpFZvwvw5dUTqhuO9LnuHckCoMPe3lL0GOqUBcvq4zNe1LMOZ2xzFG%2FyiKmwiYYRB7anLlCO5wOZoz9tCs8BuXqxWjbwSKuk7Tp%2FTtefHMwepoaAVruAtGqNwyOKfbUB6tfn6FhM6duInoPoBlH%2FmntSBOscUREPoQJI%2BgBXRLFtw0vo7QhZf0yNURdW2HNLt9FhytBZaWf8PPiRzaz1oQnEr%2FYoVixSBuGWed0%2Br3JykFO4Y%2BDQLF5%2BD5l6nGf0v&X-Amz-Signature=94a9fed6a03e9884008afb1466a9a813d9d7f3cc299dd31f1ca5e321c6f126d9&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QYJMYCEL%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIEmvjuODMtGgRr2d8pvpKH61UnamgxmWfsxHT8aP2YEnAiEA3NOXblE6beCG0WhnbmdZloFzJxbnZfDqo16orDpwJ2Mq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDH0H6dcOJpsp9Sk3bSrcAzA9j2Bvg1CnOrtX%2BLs2%2FamIMZppHEwui0LAeYw9JBfq7D%2FsPk8QPpeAqo0sbT%2FO%2Fx2ZQmLMoJN3mpigcNAiWZFtTI6BAB9yoxfCNo5Fgv605UBfXx2ipobOnx%2FwXu769Q%2FZ6lz5KnM4PLjVz8gyi4LjWM6WAMhtT07bDE%2B0zYaewIuAn14jR0D8amMQPqX0OIjTfSGzmA43LJ%2F1e40U6fvHMC%2FsLI2xcvtsTpMOJH0%2BAGJ%2FILgEf7MS7Qqzacpq%2BzQQowL9hnrp1TMy%2FogmZVHr9x4hwibzU%2B8vzpbV%2BVNynCD720RTIDdFCCb1sgJi9nwVkQOQdzOCSPozBf7y%2FrGFX8mktFQtnc%2BnJtTw47kOJZaRtPZqCGu1KKNHieiuAhqKkrVpW9XqufUIi0P2AvJWZYtbwPFougMVowaFxFObHudeJzuQUP19LPqUPj2%2F3D2666D8eICmxu3%2BgEnGb5Ot%2FcULFf6WxSd6aEw2Mol4tMZJkrdWt9SSzlvPjDxN4flV0v254xARCYmwLEXoy0yWfEbYUhRoJ1N9z0vv5mviL3MiW7Gs%2Bvkyggtn5CYaJKPqAiOLvFQdvQ%2FP3HHiC6f18S1URf3hEERIpFZvwvw5dUTqhuO9LnuHckCoMPe3lL0GOqUBcvq4zNe1LMOZ2xzFG%2FyiKmwiYYRB7anLlCO5wOZoz9tCs8BuXqxWjbwSKuk7Tp%2FTtefHMwepoaAVruAtGqNwyOKfbUB6tfn6FhM6duInoPoBlH%2FmntSBOscUREPoQJI%2BgBXRLFtw0vo7QhZf0yNURdW2HNLt9FhytBZaWf8PPiRzaz1oQnEr%2FYoVixSBuGWed0%2Br3JykFO4Y%2BDQLF5%2BD5l6nGf0v&X-Amz-Signature=71ed487cd5d74a3d066a335382e867e73bc164e5bbe696dab3f8b833f69236f0&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
