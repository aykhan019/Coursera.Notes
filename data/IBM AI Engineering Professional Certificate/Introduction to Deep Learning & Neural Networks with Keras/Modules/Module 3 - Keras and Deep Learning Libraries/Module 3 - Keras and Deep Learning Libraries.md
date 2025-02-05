

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46626PKALEQ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQCz0Cb52GDh7VWjPkroYAjjjnUKJpyfStIeKf5ql2nXjAIgYnN2ykMp4ro1BUVwOsk3%2FU7Osi4Q5GG%2BhTm0%2BaBbkSYq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDI9%2Fb9H9n7IPhGxqXircA8B1BjG5TL0X6mBbWFf38s3LVAIeqBjppDqtaa9eqSqZHdsHDGp8FFp8zKwTmbB0PKc0vCRiUXDEGesjBHt6P4xt6WYWYkInPh3WpyAUNdOZmaEOcmkqm3VSiicEi6IQ3UGB14JnV2uKObmBCa4%2Bpmr3H27b28OssD2PbhAvS45Y4cMopd0ZQZkYMdvBjSlYWSgSKFO1PezuzOSCySkqfQSc8sTj2MyPcYRrf6RD6EgfxLSfBn3eSvzqfEqeLFFjTj7eZgoywMait9pkTuAuzXRV3J7K8QxBnBNxTjErVapKPAqbBZTDILyRV4FwrYBzz6K0Pqiva55%2B6lIHW7q%2BUHkstfgH76gpqZeR1tLOeD9MLrI5mV5bABXQAp%2FW7N5KvEHWzNlNQA6Bz8b5g%2BQaD7QAH%2B1kDFBD4naUiYnFHLrCaDe9E7Qrn%2F15eF%2FDjby%2FpeluOpQMLs06j7sXZUYtAIZe9vzCvbj%2FbyNEfYqsuJNYEnPkl%2BM88PUQOgNtoAyJ%2BJ%2FUUXFbLMqwxK4Teixs6befZpZ6YxBFgEwqGMu1%2FrzInrMSuWpKm1LzxtTw7ttyJj43gZy5qTTBvYIpozKokDsY%2BInaqt6xIoQh0fs%2BJY54LxrahwRVTQiVNTBUMIm8jr0GOqUBgyTdHF9Mc2cQy6IS7px28IQTumZu1pVSPpulrrRnbl43eD7%2BFQH3y2sZ4PxTjY9pvg4SBEEQ%2FdrOG4thnHAjW7knOrgffJKN86LJaK52ehHOTZOpTa5Vkj%2BAT9%2B0r%2FYS1g%2F7zrGjWXdMfGv9ZmKMzOhlM4KpyZp1R%2B0gVRJ5Jh2GAO%2FnmY3u3BcbrBuBxBhs4Yn9yo1UGR2ttmVUWhtyIHfqPW2H&X-Amz-Signature=cfec8fa690669b8e4d6350d950a8dba03cca0b6cfa5d3e22407cae5115880315&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46626PKALEQ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQCz0Cb52GDh7VWjPkroYAjjjnUKJpyfStIeKf5ql2nXjAIgYnN2ykMp4ro1BUVwOsk3%2FU7Osi4Q5GG%2BhTm0%2BaBbkSYq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDI9%2Fb9H9n7IPhGxqXircA8B1BjG5TL0X6mBbWFf38s3LVAIeqBjppDqtaa9eqSqZHdsHDGp8FFp8zKwTmbB0PKc0vCRiUXDEGesjBHt6P4xt6WYWYkInPh3WpyAUNdOZmaEOcmkqm3VSiicEi6IQ3UGB14JnV2uKObmBCa4%2Bpmr3H27b28OssD2PbhAvS45Y4cMopd0ZQZkYMdvBjSlYWSgSKFO1PezuzOSCySkqfQSc8sTj2MyPcYRrf6RD6EgfxLSfBn3eSvzqfEqeLFFjTj7eZgoywMait9pkTuAuzXRV3J7K8QxBnBNxTjErVapKPAqbBZTDILyRV4FwrYBzz6K0Pqiva55%2B6lIHW7q%2BUHkstfgH76gpqZeR1tLOeD9MLrI5mV5bABXQAp%2FW7N5KvEHWzNlNQA6Bz8b5g%2BQaD7QAH%2B1kDFBD4naUiYnFHLrCaDe9E7Qrn%2F15eF%2FDjby%2FpeluOpQMLs06j7sXZUYtAIZe9vzCvbj%2FbyNEfYqsuJNYEnPkl%2BM88PUQOgNtoAyJ%2BJ%2FUUXFbLMqwxK4Teixs6befZpZ6YxBFgEwqGMu1%2FrzInrMSuWpKm1LzxtTw7ttyJj43gZy5qTTBvYIpozKokDsY%2BInaqt6xIoQh0fs%2BJY54LxrahwRVTQiVNTBUMIm8jr0GOqUBgyTdHF9Mc2cQy6IS7px28IQTumZu1pVSPpulrrRnbl43eD7%2BFQH3y2sZ4PxTjY9pvg4SBEEQ%2FdrOG4thnHAjW7knOrgffJKN86LJaK52ehHOTZOpTa5Vkj%2BAT9%2B0r%2FYS1g%2F7zrGjWXdMfGv9ZmKMzOhlM4KpyZp1R%2B0gVRJ5Jh2GAO%2FnmY3u3BcbrBuBxBhs4Yn9yo1UGR2ttmVUWhtyIHfqPW2H&X-Amz-Signature=673d850844401f2ab376f8ca6559e3d9187bd19034a453209cf7cb328d5fd49c&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46626PKALEQ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQCz0Cb52GDh7VWjPkroYAjjjnUKJpyfStIeKf5ql2nXjAIgYnN2ykMp4ro1BUVwOsk3%2FU7Osi4Q5GG%2BhTm0%2BaBbkSYq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDI9%2Fb9H9n7IPhGxqXircA8B1BjG5TL0X6mBbWFf38s3LVAIeqBjppDqtaa9eqSqZHdsHDGp8FFp8zKwTmbB0PKc0vCRiUXDEGesjBHt6P4xt6WYWYkInPh3WpyAUNdOZmaEOcmkqm3VSiicEi6IQ3UGB14JnV2uKObmBCa4%2Bpmr3H27b28OssD2PbhAvS45Y4cMopd0ZQZkYMdvBjSlYWSgSKFO1PezuzOSCySkqfQSc8sTj2MyPcYRrf6RD6EgfxLSfBn3eSvzqfEqeLFFjTj7eZgoywMait9pkTuAuzXRV3J7K8QxBnBNxTjErVapKPAqbBZTDILyRV4FwrYBzz6K0Pqiva55%2B6lIHW7q%2BUHkstfgH76gpqZeR1tLOeD9MLrI5mV5bABXQAp%2FW7N5KvEHWzNlNQA6Bz8b5g%2BQaD7QAH%2B1kDFBD4naUiYnFHLrCaDe9E7Qrn%2F15eF%2FDjby%2FpeluOpQMLs06j7sXZUYtAIZe9vzCvbj%2FbyNEfYqsuJNYEnPkl%2BM88PUQOgNtoAyJ%2BJ%2FUUXFbLMqwxK4Teixs6befZpZ6YxBFgEwqGMu1%2FrzInrMSuWpKm1LzxtTw7ttyJj43gZy5qTTBvYIpozKokDsY%2BInaqt6xIoQh0fs%2BJY54LxrahwRVTQiVNTBUMIm8jr0GOqUBgyTdHF9Mc2cQy6IS7px28IQTumZu1pVSPpulrrRnbl43eD7%2BFQH3y2sZ4PxTjY9pvg4SBEEQ%2FdrOG4thnHAjW7knOrgffJKN86LJaK52ehHOTZOpTa5Vkj%2BAT9%2B0r%2FYS1g%2F7zrGjWXdMfGv9ZmKMzOhlM4KpyZp1R%2B0gVRJ5Jh2GAO%2FnmY3u3BcbrBuBxBhs4Yn9yo1UGR2ttmVUWhtyIHfqPW2H&X-Amz-Signature=04836d290008667c1aef69e3cb1e3a6209e6f5a07fa0f1b6b367fc1c651db7d8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y255SKMX%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQCD8vfHSDxrQGWjtPOB3IU4CQLjcnAv8cmQ70BV5oCyrQIhAM%2BdnNj%2FU333AZnBnYWXDoF9ujzpJ1PSffSnAht4FYchKv8DCEoQABoMNjM3NDIzMTgzODA1Igw6R09sOs6AxMgnQT0q3ANs4bR8DHQoKVSSAygqb7lpFXCiml4EPPPQUIbCPitaCGQnX2mla4kZZfokV1Hetpn0%2FYOCw794oDEBSIzFL7lLA8yfF8i0woeMfU5vFUYtsRzx%2FKFrUkLDadf5rpP1Kg4C8YPYl6EXPS5cOTaUM3gH4YlSjoO6I%2B0D7NjPKGbsJh%2Ba9UcCCXMVNADbEUehRMyPXrpk1D7w8aMzIVKKRqDe5ljuXbgQKl%2BQP3EaokBSZOgLYGKAaLYiivSNHLOBfft%2FqC6%2F19gkAhwqcHapF%2BJJuSQFLeblAQYazrNjJk4tjqKDXIWnXsCiGmRi9RRrTqFfksHWYrft%2BPWn%2BRTAlch56PQC4qkJsmdcroh7n%2BSj5d6cgTi24lIc373ox09cX48%2B9SGLkOPjwj%2Bo1T2D%2BmF428pxMOl1dWP3gz%2Brtg0W2dqtXCUmZYPrYTMbwX8X5u5HXkWTRmSThe5afbKLbwobC9Xbhxs1wvk7VPn8QWm2WuMMiP3s2%2BZL2s%2FkxwaS7oXevxlODCVcGDOjqxFPhqZenZBLFhQ6dRv7Tv%2Bdgfmw3bmixXOF6uAkGTgS49IsTnWxyf1wg91FTVk2c%2F5Yzf80bx9a9NRYZ1kuy2SkeeVR9Bn6fnsnNstXl%2Bn70zDbuo69BjqkAcgAyNxr4gExuAFir2PmcdgB28F7DWTNRo0eBdqoKuCOUWC7ODiRetjYiEEYBjeyeB8yhYa8hoRp56cND9baqnHOPuzFokwAW6L%2BtIjUzsRONV17wgjok5HiLaa3pXcD%2F3Mf96SYzRAtC41weo8mm7CBjAbnWrWWnu86xu6RMeIjF6UOEPtE6nsG%2B4fB6mdmLF7pgz4XLERCbTZ2E4TDibxqCDqb&X-Amz-Signature=afffcef1cca707598d0e5642e0057725ab8265d49ddc9943f74e78eb70704ad6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGB6MCGB%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJGMEQCIDFJNNFaEw1GvC8RMfUuRFu%2F5fdlMLXbV7NukBXqIuE8AiAPhzg61bn6NO7ntebnQ7iM3XCZSxHZoufMLr4gqCpd6ir%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMFDQuxMSxEAXA9VBNKtwDFb6EJAI7wFGwF8g8HjzRlvLz4fhSnAzsrdQJL%2F%2FJ7dme2y5L2hc%2B14nw1e55CEyfL6Df47lWe%2B%2FjzaZkUeLCPaKXMmbjzXGYcOGPWGKLXRzxP7rRX6tPaF0B5tzAP7PFmEyESo79oHTafZDl90XIKSzLsBEN%2B%2BMeNavhUJBjRhmjdbtSYa8NHoNq0RhWhhD%2FX15uSF5D9GEJN5omzSwLBE3xdqiRCdnjlRqyjiRaUCrg6dogZjnG2lpLvQDlkL7jj8Vm%2FMlaGFD%2BJPkb7r%2Fsm1dU65Jq2zIQU1smLNUnUufhJ6uR%2BEdsFxWNu3SSuA7cShr%2B1ZFSsvEOnDMQMz5DRGRL0x6QCw1KA0whSZquBAABJX%2FKpfGv9dNWD%2BoevY%2FT%2BBZrSsikXwGg3o9tKRHXmvihysSZ%2Bx8r4WWpp7F0qKvDZMm7cSmMBvX%2B%2BubjhZo7HKd3JkCs%2FnOErYnGZ8LXD8JnuyOELH42a6VVGMlddcE8WL8Egw4P8rqaeLGvC0dKMHQxdsSbZ4fvgauEK67iFWhKvXa9F0hAxDtrTJSrSez2qV6dEargloZ2NF%2FaQRgmfipIUf9DqK6UYvjdn9rn9FoPgR2OYEAyqSPdfTGSYc8eBJ9Vmf98WLfE7lUwl7qOvQY6pgGSAkMhOOr6x3OanPJyhXf%2B65ZeLVnAdOdxNMzWbQqcwwsaURcpM1vhLhmL0oJ8Iy3LHgp2kP%2BAxqtKWr1LF6QfKlW57K9ATqiaExG9unZhfZEDmlJSY%2B5tjb4Od%2F7GLMefQZhQAYgy6ViJgn5RNsQYxZU1ua9Uk9i5Mr6N008dQFcvp5%2B5vLfLbjc%2BSg5kSPecR1bT8Bv5%2B6ZtQLujNDkgYBo97xpx&X-Amz-Signature=2edce31f106123d5d8daa2257672da8041d50a2485af91c5e77db68b17112e12&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46626PKALEQ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQCz0Cb52GDh7VWjPkroYAjjjnUKJpyfStIeKf5ql2nXjAIgYnN2ykMp4ro1BUVwOsk3%2FU7Osi4Q5GG%2BhTm0%2BaBbkSYq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDI9%2Fb9H9n7IPhGxqXircA8B1BjG5TL0X6mBbWFf38s3LVAIeqBjppDqtaa9eqSqZHdsHDGp8FFp8zKwTmbB0PKc0vCRiUXDEGesjBHt6P4xt6WYWYkInPh3WpyAUNdOZmaEOcmkqm3VSiicEi6IQ3UGB14JnV2uKObmBCa4%2Bpmr3H27b28OssD2PbhAvS45Y4cMopd0ZQZkYMdvBjSlYWSgSKFO1PezuzOSCySkqfQSc8sTj2MyPcYRrf6RD6EgfxLSfBn3eSvzqfEqeLFFjTj7eZgoywMait9pkTuAuzXRV3J7K8QxBnBNxTjErVapKPAqbBZTDILyRV4FwrYBzz6K0Pqiva55%2B6lIHW7q%2BUHkstfgH76gpqZeR1tLOeD9MLrI5mV5bABXQAp%2FW7N5KvEHWzNlNQA6Bz8b5g%2BQaD7QAH%2B1kDFBD4naUiYnFHLrCaDe9E7Qrn%2F15eF%2FDjby%2FpeluOpQMLs06j7sXZUYtAIZe9vzCvbj%2FbyNEfYqsuJNYEnPkl%2BM88PUQOgNtoAyJ%2BJ%2FUUXFbLMqwxK4Teixs6befZpZ6YxBFgEwqGMu1%2FrzInrMSuWpKm1LzxtTw7ttyJj43gZy5qTTBvYIpozKokDsY%2BInaqt6xIoQh0fs%2BJY54LxrahwRVTQiVNTBUMIm8jr0GOqUBgyTdHF9Mc2cQy6IS7px28IQTumZu1pVSPpulrrRnbl43eD7%2BFQH3y2sZ4PxTjY9pvg4SBEEQ%2FdrOG4thnHAjW7knOrgffJKN86LJaK52ehHOTZOpTa5Vkj%2BAT9%2B0r%2FYS1g%2F7zrGjWXdMfGv9ZmKMzOhlM4KpyZp1R%2B0gVRJ5Jh2GAO%2FnmY3u3BcbrBuBxBhs4Yn9yo1UGR2ttmVUWhtyIHfqPW2H&X-Amz-Signature=44bec3c4179fdbf0760ac07f7cf81718832633bfac843e9d3473b53bb395a383&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46626PKALEQ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQCz0Cb52GDh7VWjPkroYAjjjnUKJpyfStIeKf5ql2nXjAIgYnN2ykMp4ro1BUVwOsk3%2FU7Osi4Q5GG%2BhTm0%2BaBbkSYq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDI9%2Fb9H9n7IPhGxqXircA8B1BjG5TL0X6mBbWFf38s3LVAIeqBjppDqtaa9eqSqZHdsHDGp8FFp8zKwTmbB0PKc0vCRiUXDEGesjBHt6P4xt6WYWYkInPh3WpyAUNdOZmaEOcmkqm3VSiicEi6IQ3UGB14JnV2uKObmBCa4%2Bpmr3H27b28OssD2PbhAvS45Y4cMopd0ZQZkYMdvBjSlYWSgSKFO1PezuzOSCySkqfQSc8sTj2MyPcYRrf6RD6EgfxLSfBn3eSvzqfEqeLFFjTj7eZgoywMait9pkTuAuzXRV3J7K8QxBnBNxTjErVapKPAqbBZTDILyRV4FwrYBzz6K0Pqiva55%2B6lIHW7q%2BUHkstfgH76gpqZeR1tLOeD9MLrI5mV5bABXQAp%2FW7N5KvEHWzNlNQA6Bz8b5g%2BQaD7QAH%2B1kDFBD4naUiYnFHLrCaDe9E7Qrn%2F15eF%2FDjby%2FpeluOpQMLs06j7sXZUYtAIZe9vzCvbj%2FbyNEfYqsuJNYEnPkl%2BM88PUQOgNtoAyJ%2BJ%2FUUXFbLMqwxK4Teixs6befZpZ6YxBFgEwqGMu1%2FrzInrMSuWpKm1LzxtTw7ttyJj43gZy5qTTBvYIpozKokDsY%2BInaqt6xIoQh0fs%2BJY54LxrahwRVTQiVNTBUMIm8jr0GOqUBgyTdHF9Mc2cQy6IS7px28IQTumZu1pVSPpulrrRnbl43eD7%2BFQH3y2sZ4PxTjY9pvg4SBEEQ%2FdrOG4thnHAjW7knOrgffJKN86LJaK52ehHOTZOpTa5Vkj%2BAT9%2B0r%2FYS1g%2F7zrGjWXdMfGv9ZmKMzOhlM4KpyZp1R%2B0gVRJ5Jh2GAO%2FnmY3u3BcbrBuBxBhs4Yn9yo1UGR2ttmVUWhtyIHfqPW2H&X-Amz-Signature=cc16d49aa60ab4fd2f6aa67d9db34d99238c485752d78acdffacc5e3b8f881d4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46626PKALEQ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQCz0Cb52GDh7VWjPkroYAjjjnUKJpyfStIeKf5ql2nXjAIgYnN2ykMp4ro1BUVwOsk3%2FU7Osi4Q5GG%2BhTm0%2BaBbkSYq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDI9%2Fb9H9n7IPhGxqXircA8B1BjG5TL0X6mBbWFf38s3LVAIeqBjppDqtaa9eqSqZHdsHDGp8FFp8zKwTmbB0PKc0vCRiUXDEGesjBHt6P4xt6WYWYkInPh3WpyAUNdOZmaEOcmkqm3VSiicEi6IQ3UGB14JnV2uKObmBCa4%2Bpmr3H27b28OssD2PbhAvS45Y4cMopd0ZQZkYMdvBjSlYWSgSKFO1PezuzOSCySkqfQSc8sTj2MyPcYRrf6RD6EgfxLSfBn3eSvzqfEqeLFFjTj7eZgoywMait9pkTuAuzXRV3J7K8QxBnBNxTjErVapKPAqbBZTDILyRV4FwrYBzz6K0Pqiva55%2B6lIHW7q%2BUHkstfgH76gpqZeR1tLOeD9MLrI5mV5bABXQAp%2FW7N5KvEHWzNlNQA6Bz8b5g%2BQaD7QAH%2B1kDFBD4naUiYnFHLrCaDe9E7Qrn%2F15eF%2FDjby%2FpeluOpQMLs06j7sXZUYtAIZe9vzCvbj%2FbyNEfYqsuJNYEnPkl%2BM88PUQOgNtoAyJ%2BJ%2FUUXFbLMqwxK4Teixs6befZpZ6YxBFgEwqGMu1%2FrzInrMSuWpKm1LzxtTw7ttyJj43gZy5qTTBvYIpozKokDsY%2BInaqt6xIoQh0fs%2BJY54LxrahwRVTQiVNTBUMIm8jr0GOqUBgyTdHF9Mc2cQy6IS7px28IQTumZu1pVSPpulrrRnbl43eD7%2BFQH3y2sZ4PxTjY9pvg4SBEEQ%2FdrOG4thnHAjW7knOrgffJKN86LJaK52ehHOTZOpTa5Vkj%2BAT9%2B0r%2FYS1g%2F7zrGjWXdMfGv9ZmKMzOhlM4KpyZp1R%2B0gVRJ5Jh2GAO%2FnmY3u3BcbrBuBxBhs4Yn9yo1UGR2ttmVUWhtyIHfqPW2H&X-Amz-Signature=2fe0f5ab37577aa934ab41399f2240da00c029057b266c968ab84cbd11090493&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46626PKALEQ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQCz0Cb52GDh7VWjPkroYAjjjnUKJpyfStIeKf5ql2nXjAIgYnN2ykMp4ro1BUVwOsk3%2FU7Osi4Q5GG%2BhTm0%2BaBbkSYq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDI9%2Fb9H9n7IPhGxqXircA8B1BjG5TL0X6mBbWFf38s3LVAIeqBjppDqtaa9eqSqZHdsHDGp8FFp8zKwTmbB0PKc0vCRiUXDEGesjBHt6P4xt6WYWYkInPh3WpyAUNdOZmaEOcmkqm3VSiicEi6IQ3UGB14JnV2uKObmBCa4%2Bpmr3H27b28OssD2PbhAvS45Y4cMopd0ZQZkYMdvBjSlYWSgSKFO1PezuzOSCySkqfQSc8sTj2MyPcYRrf6RD6EgfxLSfBn3eSvzqfEqeLFFjTj7eZgoywMait9pkTuAuzXRV3J7K8QxBnBNxTjErVapKPAqbBZTDILyRV4FwrYBzz6K0Pqiva55%2B6lIHW7q%2BUHkstfgH76gpqZeR1tLOeD9MLrI5mV5bABXQAp%2FW7N5KvEHWzNlNQA6Bz8b5g%2BQaD7QAH%2B1kDFBD4naUiYnFHLrCaDe9E7Qrn%2F15eF%2FDjby%2FpeluOpQMLs06j7sXZUYtAIZe9vzCvbj%2FbyNEfYqsuJNYEnPkl%2BM88PUQOgNtoAyJ%2BJ%2FUUXFbLMqwxK4Teixs6befZpZ6YxBFgEwqGMu1%2FrzInrMSuWpKm1LzxtTw7ttyJj43gZy5qTTBvYIpozKokDsY%2BInaqt6xIoQh0fs%2BJY54LxrahwRVTQiVNTBUMIm8jr0GOqUBgyTdHF9Mc2cQy6IS7px28IQTumZu1pVSPpulrrRnbl43eD7%2BFQH3y2sZ4PxTjY9pvg4SBEEQ%2FdrOG4thnHAjW7knOrgffJKN86LJaK52ehHOTZOpTa5Vkj%2BAT9%2B0r%2FYS1g%2F7zrGjWXdMfGv9ZmKMzOhlM4KpyZp1R%2B0gVRJ5Jh2GAO%2FnmY3u3BcbrBuBxBhs4Yn9yo1UGR2ttmVUWhtyIHfqPW2H&X-Amz-Signature=ab87bae6c8a3b2b061d30eda8252d280ff87f9cdc7094aea5f72fa76763007e0&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
