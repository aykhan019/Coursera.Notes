

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJQKAATU%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201644Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIGqCHWbjfS01QvEeuyV7cXxCDW219Ij7S%2FafmUSU8yBkAiAO408N6oaf%2FjQuxF65P0npARw7cnG%2FIleFjYN0Yza4cir%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMSYdeFohxcXBmANQXKtwDkmSwSirualkHxPRpwmipQhX4%2B9Kwbl93GsPwYG0s%2B0GGTcfF8htP%2FA2vaJw2HdKp%2FG29Xjyd9BCd1mPAavJmDPQ335%2FQ5EcfiuGo7qFNmIuk%2Fcd5JtIYKIsysa%2FWnsiVIyK62ybxA3zcvV1JB44NGSZy5%2FrWlkNz7EoN%2BDHpYDwhnMqYIxQzisYQ2TWpc2CJDZWvXnvxVeftUqfPNmxq72uK6PWocSNGMfxAoTifp5VSR907RX1YDh3kP9GbAAm3hOaXZm9rnsQSJunivql6OX%2Btk8yWLjpAj6hb7f13c3pXJAhhKM6D6GNk0qWSdjTphczspk2Q6Iw1yeGIBprwOK64r3eUIcyRPvS1cyRaIEuoDkrzLqc5fGlQdgVYNMhNblxPdpoMWCGGUOF1Bjpbd7vcJbQZJ3q9AScj2oseIWAn2qUj%2BLE4n9i0ArZB0pYNgoa0fOp5zNhrO8uitAy2bNyyson3uKaoJ5AM4x%2BJggq7zdfbAhnAN1NG0t0zR%2B6xkMOyxKL4KDtQu2YrGAS9TxXNmc86lMpO%2FqC8f3NN%2FMXosjwGdI0YpJS4GciJlC6TodOkjrupoGX%2Bnol1JC3NSBug2V%2BiKIHt62mEvXwQl70cRWK8Yq0WWRHouecw5bqOvQY6pgF5qNiHB4X5RgghTB6mlYtDCSehJPiVcJJacdaqNya8U93fMREileHd3IUhO6yI6LPILqv1jmz8T4r2cH4FcrpW2sxb8OQlhZNw94Y1ctIVFyWnxR%2FOjwjVwXRue%2B1hJiPKZv%2BTHWy1FI6nw7rBkPGaV3JacHNfTeU7hk55dI6s4bv8Ic89XKeFVQ%2Fs%2BQoT0fgnPwDUndxCCO6y9SemyBwzw8dr2Cyb&X-Amz-Signature=e641932cb457c7d83ad7a24dbc5a9c27c06bfb74c96563640f557c76bb6773c2&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJQKAATU%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201644Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIGqCHWbjfS01QvEeuyV7cXxCDW219Ij7S%2FafmUSU8yBkAiAO408N6oaf%2FjQuxF65P0npARw7cnG%2FIleFjYN0Yza4cir%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMSYdeFohxcXBmANQXKtwDkmSwSirualkHxPRpwmipQhX4%2B9Kwbl93GsPwYG0s%2B0GGTcfF8htP%2FA2vaJw2HdKp%2FG29Xjyd9BCd1mPAavJmDPQ335%2FQ5EcfiuGo7qFNmIuk%2Fcd5JtIYKIsysa%2FWnsiVIyK62ybxA3zcvV1JB44NGSZy5%2FrWlkNz7EoN%2BDHpYDwhnMqYIxQzisYQ2TWpc2CJDZWvXnvxVeftUqfPNmxq72uK6PWocSNGMfxAoTifp5VSR907RX1YDh3kP9GbAAm3hOaXZm9rnsQSJunivql6OX%2Btk8yWLjpAj6hb7f13c3pXJAhhKM6D6GNk0qWSdjTphczspk2Q6Iw1yeGIBprwOK64r3eUIcyRPvS1cyRaIEuoDkrzLqc5fGlQdgVYNMhNblxPdpoMWCGGUOF1Bjpbd7vcJbQZJ3q9AScj2oseIWAn2qUj%2BLE4n9i0ArZB0pYNgoa0fOp5zNhrO8uitAy2bNyyson3uKaoJ5AM4x%2BJggq7zdfbAhnAN1NG0t0zR%2B6xkMOyxKL4KDtQu2YrGAS9TxXNmc86lMpO%2FqC8f3NN%2FMXosjwGdI0YpJS4GciJlC6TodOkjrupoGX%2Bnol1JC3NSBug2V%2BiKIHt62mEvXwQl70cRWK8Yq0WWRHouecw5bqOvQY6pgF5qNiHB4X5RgghTB6mlYtDCSehJPiVcJJacdaqNya8U93fMREileHd3IUhO6yI6LPILqv1jmz8T4r2cH4FcrpW2sxb8OQlhZNw94Y1ctIVFyWnxR%2FOjwjVwXRue%2B1hJiPKZv%2BTHWy1FI6nw7rBkPGaV3JacHNfTeU7hk55dI6s4bv8Ic89XKeFVQ%2Fs%2BQoT0fgnPwDUndxCCO6y9SemyBwzw8dr2Cyb&X-Amz-Signature=9bd24f9ad00c2b656955e8c4ba6bd382d047333d2304c154addf6e818e0ac852&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJQKAATU%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201644Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIGqCHWbjfS01QvEeuyV7cXxCDW219Ij7S%2FafmUSU8yBkAiAO408N6oaf%2FjQuxF65P0npARw7cnG%2FIleFjYN0Yza4cir%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMSYdeFohxcXBmANQXKtwDkmSwSirualkHxPRpwmipQhX4%2B9Kwbl93GsPwYG0s%2B0GGTcfF8htP%2FA2vaJw2HdKp%2FG29Xjyd9BCd1mPAavJmDPQ335%2FQ5EcfiuGo7qFNmIuk%2Fcd5JtIYKIsysa%2FWnsiVIyK62ybxA3zcvV1JB44NGSZy5%2FrWlkNz7EoN%2BDHpYDwhnMqYIxQzisYQ2TWpc2CJDZWvXnvxVeftUqfPNmxq72uK6PWocSNGMfxAoTifp5VSR907RX1YDh3kP9GbAAm3hOaXZm9rnsQSJunivql6OX%2Btk8yWLjpAj6hb7f13c3pXJAhhKM6D6GNk0qWSdjTphczspk2Q6Iw1yeGIBprwOK64r3eUIcyRPvS1cyRaIEuoDkrzLqc5fGlQdgVYNMhNblxPdpoMWCGGUOF1Bjpbd7vcJbQZJ3q9AScj2oseIWAn2qUj%2BLE4n9i0ArZB0pYNgoa0fOp5zNhrO8uitAy2bNyyson3uKaoJ5AM4x%2BJggq7zdfbAhnAN1NG0t0zR%2B6xkMOyxKL4KDtQu2YrGAS9TxXNmc86lMpO%2FqC8f3NN%2FMXosjwGdI0YpJS4GciJlC6TodOkjrupoGX%2Bnol1JC3NSBug2V%2BiKIHt62mEvXwQl70cRWK8Yq0WWRHouecw5bqOvQY6pgF5qNiHB4X5RgghTB6mlYtDCSehJPiVcJJacdaqNya8U93fMREileHd3IUhO6yI6LPILqv1jmz8T4r2cH4FcrpW2sxb8OQlhZNw94Y1ctIVFyWnxR%2FOjwjVwXRue%2B1hJiPKZv%2BTHWy1FI6nw7rBkPGaV3JacHNfTeU7hk55dI6s4bv8Ic89XKeFVQ%2Fs%2BQoT0fgnPwDUndxCCO6y9SemyBwzw8dr2Cyb&X-Amz-Signature=a44f92a3b0908e4b868326815ee0f3b4c253d5ffaa0d667903100d62829cba93&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q4XJXBKS%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201645Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIGBGv8H6d1MP3qLZEnTCOVLneTwXrK1w3BkEBekuaxz2AiAkZaJpyDGQJZPlXfjs92bTkbgNQBXbGx9vgUZrJE1q%2Fir%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIM%2BFyik%2F6fwbJe09bFKtwDZ6HKeQgdO0LslNGT%2Feci06LWmeEnsEsykXwPrgrQNXdnk3HPsSBFwA26lGX5XI6EMcOaFjdQJpui5bpLNe0ylFhkHxUXXMLCyahu%2FHJFIz1okkEb15WG%2B%2Fxg5xdGYOQ9%2Bk2Y6SEQjUey16c8qTfC3NuhtuhJvFaT9jCFaKlMVUJt%2FhRCjG83QMrKIa4IVnTAmNwP2ypRhVD1DWF%2BLUGOG3mqv0Omm8NjkzPqRHxJsgWxnhPMByanM%2FBWNYWCMWWuVNoWNMCobR%2FZdi0LDr1eNvBdEBMV%2FOw9DCm%2BEbuE6C5%2FyCFMsXs7CzSSH6wEm9Yq8ks%2BX%2BaQnKdraBHCSpPugR7fRghmPbv5vEdNKMImuepYaicBUIzVuviGppuJwa6Xol0uqZmWlIdyWQlE5r6hMbLcmIe0cHctWWY5nhzyrzrJ8asITgTArRHLiJNj59NPGXpyzBloICqLl5qMr%2BeyCxp%2BoWW%2FgFP6r%2BziUZlmHifopYQ0CvrQ%2BJS%2Bkanfa3QO%2F97Yn1%2FEO1myJR5bK2X2YILrbPFj%2Fffs2ZnH06OIwYHjphpDlPBOSWlRQn5ac97UaRsBrnJSuPtZri0hewuJtpXU%2FlfsSnAq4lVPDOlLj97A9WG73JweWXl6tpswibyOvQY6pgGRXUSlPVd3WcjpjIUc7q%2F58Dr1FdrgE4V5WJmOtGOp9jjdaxd3GSRv7lfGPcawg8VkvzRTz1g1W2mCDQJbwH8eOrz8ObPANTf3Z6R%2FzSf%2FmsqsiiEiszP0Mub83X2TAdD1S3wOr8JAPOHeldI4eap4KfumIV%2BCHrfm8xRmm0BPRbCTzmyvhFFKJXSL%2BK1F2B6i2LwBNkM9IAq8Gbm%2BlpfczF0EkNxe&X-Amz-Signature=6ac14034d46cb5809b9fc1c7a31b118cd42c77b29f0d768211c4f1973c422032&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZX6NY5UY%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201645Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQDEnskG4iCQAb%2FhcMhVOJjitIV420t1UcTcUUQFpXHGBwIgb9VN9VILevzhaOkViaI7wC%2BmWEO%2BHYZZ1zzxT6rbdsEq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDII6CIThHQIKVlqH3CrcA3%2BS4GeYRekMb3jiX23siCn5o2VgMYgpzVKKp1gYxENcA7jHRpeZOP1bVZTwbtAV91c79lRan2dzg3hc72h%2B0PLa%2FMRtb8uKb9wXWqhdMmjdY7bbq8o%2BiMM72Q%2F4zMDUjy08ll9KQxD%2BlWKZ%2FozBIuK2ccLcb782NBYKV%2FK4TbpwQiR9nRJPOYZicD6t6MBYU3TFQIy16Pb4Jc9COHwE2awxHhZcn%2B%2FIEq1g%2F1JWA0P5yTc8sxurS3HqN1AbFxMuUUGjVy3Xk6WHoFGpX20grd9A5vi9UwtbU2tyD5GnGR9a6chUSrgFwFw5x59SuFnleVsYHwVnpXrSfgZqmYqbeup6WGx1%2FxzYDkdL42p7XawuIBi%2FlCJQaBCdRPyW5E8GgSoIaeq9BZCYAY%2F3uqJjKe%2BdFevF%2BC%2Bd8MPS2wh7nsMp9818HaFStBR1xozZ4foiDxfNddio0ov9dfUOUJMCgbJp6WAn2P7Bi%2B5cKXDlhh0EA0wMESg3tWYw3%2FUVXGD0FhZTwTxKyqxTYSRJ%2B5t%2BpFE%2BZdcOOtG%2BB9TRFd9WKy8%2Bxz4dVfIs307C2r6YBIgvzpFgkZsfykGR7B5ob83fUsddGee2iJXNxGwJnXFLOaQx1t8PPI8BMzPdf30NMKa6jr0GOqUBVCRTsez%2FYZemuSK0VD6j8zkefFir78OgRfQwjaNyQbK2ACrc3H66PyGQQiRSi1O4XunbiCIHNNplt7kZnW3M9R96x85iMdxIvHjnDLyQWic3HymTkiUw3QurgR2cc5Qof55XBQ4vYpDfVEiz7y93bfWIdafT6IKd5c02rR8pihg1ztRaVMDFSWeoUYDfWApbSX1VXa6iqW7Th%2FU0fu8%2BohgB3K0J&X-Amz-Signature=d536454fc271845e8ab96ffbaa32fc2ad44b0d486121462bedd037822826f367&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJQKAATU%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201644Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIGqCHWbjfS01QvEeuyV7cXxCDW219Ij7S%2FafmUSU8yBkAiAO408N6oaf%2FjQuxF65P0npARw7cnG%2FIleFjYN0Yza4cir%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMSYdeFohxcXBmANQXKtwDkmSwSirualkHxPRpwmipQhX4%2B9Kwbl93GsPwYG0s%2B0GGTcfF8htP%2FA2vaJw2HdKp%2FG29Xjyd9BCd1mPAavJmDPQ335%2FQ5EcfiuGo7qFNmIuk%2Fcd5JtIYKIsysa%2FWnsiVIyK62ybxA3zcvV1JB44NGSZy5%2FrWlkNz7EoN%2BDHpYDwhnMqYIxQzisYQ2TWpc2CJDZWvXnvxVeftUqfPNmxq72uK6PWocSNGMfxAoTifp5VSR907RX1YDh3kP9GbAAm3hOaXZm9rnsQSJunivql6OX%2Btk8yWLjpAj6hb7f13c3pXJAhhKM6D6GNk0qWSdjTphczspk2Q6Iw1yeGIBprwOK64r3eUIcyRPvS1cyRaIEuoDkrzLqc5fGlQdgVYNMhNblxPdpoMWCGGUOF1Bjpbd7vcJbQZJ3q9AScj2oseIWAn2qUj%2BLE4n9i0ArZB0pYNgoa0fOp5zNhrO8uitAy2bNyyson3uKaoJ5AM4x%2BJggq7zdfbAhnAN1NG0t0zR%2B6xkMOyxKL4KDtQu2YrGAS9TxXNmc86lMpO%2FqC8f3NN%2FMXosjwGdI0YpJS4GciJlC6TodOkjrupoGX%2Bnol1JC3NSBug2V%2BiKIHt62mEvXwQl70cRWK8Yq0WWRHouecw5bqOvQY6pgF5qNiHB4X5RgghTB6mlYtDCSehJPiVcJJacdaqNya8U93fMREileHd3IUhO6yI6LPILqv1jmz8T4r2cH4FcrpW2sxb8OQlhZNw94Y1ctIVFyWnxR%2FOjwjVwXRue%2B1hJiPKZv%2BTHWy1FI6nw7rBkPGaV3JacHNfTeU7hk55dI6s4bv8Ic89XKeFVQ%2Fs%2BQoT0fgnPwDUndxCCO6y9SemyBwzw8dr2Cyb&X-Amz-Signature=c434cdcba0b59a3a9fe9e630ea2dd23db60d29a079f7cc2850d8c144efa36f66&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJQKAATU%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201644Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIGqCHWbjfS01QvEeuyV7cXxCDW219Ij7S%2FafmUSU8yBkAiAO408N6oaf%2FjQuxF65P0npARw7cnG%2FIleFjYN0Yza4cir%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMSYdeFohxcXBmANQXKtwDkmSwSirualkHxPRpwmipQhX4%2B9Kwbl93GsPwYG0s%2B0GGTcfF8htP%2FA2vaJw2HdKp%2FG29Xjyd9BCd1mPAavJmDPQ335%2FQ5EcfiuGo7qFNmIuk%2Fcd5JtIYKIsysa%2FWnsiVIyK62ybxA3zcvV1JB44NGSZy5%2FrWlkNz7EoN%2BDHpYDwhnMqYIxQzisYQ2TWpc2CJDZWvXnvxVeftUqfPNmxq72uK6PWocSNGMfxAoTifp5VSR907RX1YDh3kP9GbAAm3hOaXZm9rnsQSJunivql6OX%2Btk8yWLjpAj6hb7f13c3pXJAhhKM6D6GNk0qWSdjTphczspk2Q6Iw1yeGIBprwOK64r3eUIcyRPvS1cyRaIEuoDkrzLqc5fGlQdgVYNMhNblxPdpoMWCGGUOF1Bjpbd7vcJbQZJ3q9AScj2oseIWAn2qUj%2BLE4n9i0ArZB0pYNgoa0fOp5zNhrO8uitAy2bNyyson3uKaoJ5AM4x%2BJggq7zdfbAhnAN1NG0t0zR%2B6xkMOyxKL4KDtQu2YrGAS9TxXNmc86lMpO%2FqC8f3NN%2FMXosjwGdI0YpJS4GciJlC6TodOkjrupoGX%2Bnol1JC3NSBug2V%2BiKIHt62mEvXwQl70cRWK8Yq0WWRHouecw5bqOvQY6pgF5qNiHB4X5RgghTB6mlYtDCSehJPiVcJJacdaqNya8U93fMREileHd3IUhO6yI6LPILqv1jmz8T4r2cH4FcrpW2sxb8OQlhZNw94Y1ctIVFyWnxR%2FOjwjVwXRue%2B1hJiPKZv%2BTHWy1FI6nw7rBkPGaV3JacHNfTeU7hk55dI6s4bv8Ic89XKeFVQ%2Fs%2BQoT0fgnPwDUndxCCO6y9SemyBwzw8dr2Cyb&X-Amz-Signature=02a20bb53c63fc475093d7df6d02ccf95323f3c96c7bc4af61e7581b5cfc40bd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJQKAATU%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201644Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIGqCHWbjfS01QvEeuyV7cXxCDW219Ij7S%2FafmUSU8yBkAiAO408N6oaf%2FjQuxF65P0npARw7cnG%2FIleFjYN0Yza4cir%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMSYdeFohxcXBmANQXKtwDkmSwSirualkHxPRpwmipQhX4%2B9Kwbl93GsPwYG0s%2B0GGTcfF8htP%2FA2vaJw2HdKp%2FG29Xjyd9BCd1mPAavJmDPQ335%2FQ5EcfiuGo7qFNmIuk%2Fcd5JtIYKIsysa%2FWnsiVIyK62ybxA3zcvV1JB44NGSZy5%2FrWlkNz7EoN%2BDHpYDwhnMqYIxQzisYQ2TWpc2CJDZWvXnvxVeftUqfPNmxq72uK6PWocSNGMfxAoTifp5VSR907RX1YDh3kP9GbAAm3hOaXZm9rnsQSJunivql6OX%2Btk8yWLjpAj6hb7f13c3pXJAhhKM6D6GNk0qWSdjTphczspk2Q6Iw1yeGIBprwOK64r3eUIcyRPvS1cyRaIEuoDkrzLqc5fGlQdgVYNMhNblxPdpoMWCGGUOF1Bjpbd7vcJbQZJ3q9AScj2oseIWAn2qUj%2BLE4n9i0ArZB0pYNgoa0fOp5zNhrO8uitAy2bNyyson3uKaoJ5AM4x%2BJggq7zdfbAhnAN1NG0t0zR%2B6xkMOyxKL4KDtQu2YrGAS9TxXNmc86lMpO%2FqC8f3NN%2FMXosjwGdI0YpJS4GciJlC6TodOkjrupoGX%2Bnol1JC3NSBug2V%2BiKIHt62mEvXwQl70cRWK8Yq0WWRHouecw5bqOvQY6pgF5qNiHB4X5RgghTB6mlYtDCSehJPiVcJJacdaqNya8U93fMREileHd3IUhO6yI6LPILqv1jmz8T4r2cH4FcrpW2sxb8OQlhZNw94Y1ctIVFyWnxR%2FOjwjVwXRue%2B1hJiPKZv%2BTHWy1FI6nw7rBkPGaV3JacHNfTeU7hk55dI6s4bv8Ic89XKeFVQ%2Fs%2BQoT0fgnPwDUndxCCO6y9SemyBwzw8dr2Cyb&X-Amz-Signature=bf882b4863b52b716475faa9c831428bd334ce4c7be32e0d8ea5d99a3c0f659f&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJQKAATU%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201644Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIGqCHWbjfS01QvEeuyV7cXxCDW219Ij7S%2FafmUSU8yBkAiAO408N6oaf%2FjQuxF65P0npARw7cnG%2FIleFjYN0Yza4cir%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMSYdeFohxcXBmANQXKtwDkmSwSirualkHxPRpwmipQhX4%2B9Kwbl93GsPwYG0s%2B0GGTcfF8htP%2FA2vaJw2HdKp%2FG29Xjyd9BCd1mPAavJmDPQ335%2FQ5EcfiuGo7qFNmIuk%2Fcd5JtIYKIsysa%2FWnsiVIyK62ybxA3zcvV1JB44NGSZy5%2FrWlkNz7EoN%2BDHpYDwhnMqYIxQzisYQ2TWpc2CJDZWvXnvxVeftUqfPNmxq72uK6PWocSNGMfxAoTifp5VSR907RX1YDh3kP9GbAAm3hOaXZm9rnsQSJunivql6OX%2Btk8yWLjpAj6hb7f13c3pXJAhhKM6D6GNk0qWSdjTphczspk2Q6Iw1yeGIBprwOK64r3eUIcyRPvS1cyRaIEuoDkrzLqc5fGlQdgVYNMhNblxPdpoMWCGGUOF1Bjpbd7vcJbQZJ3q9AScj2oseIWAn2qUj%2BLE4n9i0ArZB0pYNgoa0fOp5zNhrO8uitAy2bNyyson3uKaoJ5AM4x%2BJggq7zdfbAhnAN1NG0t0zR%2B6xkMOyxKL4KDtQu2YrGAS9TxXNmc86lMpO%2FqC8f3NN%2FMXosjwGdI0YpJS4GciJlC6TodOkjrupoGX%2Bnol1JC3NSBug2V%2BiKIHt62mEvXwQl70cRWK8Yq0WWRHouecw5bqOvQY6pgF5qNiHB4X5RgghTB6mlYtDCSehJPiVcJJacdaqNya8U93fMREileHd3IUhO6yI6LPILqv1jmz8T4r2cH4FcrpW2sxb8OQlhZNw94Y1ctIVFyWnxR%2FOjwjVwXRue%2B1hJiPKZv%2BTHWy1FI6nw7rBkPGaV3JacHNfTeU7hk55dI6s4bv8Ic89XKeFVQ%2Fs%2BQoT0fgnPwDUndxCCO6y9SemyBwzw8dr2Cyb&X-Amz-Signature=4dce97640e243cf7ab7e7e0bdf22d0c4731cddfe615d1318e9359c3dc2acad07&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
