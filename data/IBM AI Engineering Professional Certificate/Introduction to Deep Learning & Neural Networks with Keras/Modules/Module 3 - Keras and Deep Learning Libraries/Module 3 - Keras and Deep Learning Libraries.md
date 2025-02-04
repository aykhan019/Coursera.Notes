

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RK3FVMBD%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031719Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJGMEQCICBYyx%2BL8mbK3iVkRrfcHZbD5PfnR5YVxl2NSzlBJQB%2BAiBenzIlLpyFwLmhewamCliLDPak60aomrdKFUrNnI%2F8GSr%2FAwgkEAAaDDYzNzQyMzE4MzgwNSIMFn6eZ8ha6LDL8UqSKtwDYBrzXnRgNpRHoAnlixZpanSeDLNJVtyJJ9Pjf6%2BV0HnXauyQAK%2BnFOmlbmpke%2FK%2Fi8Pvvaqd3VjOOcDw6vNwcE5H6TNgo8NFrDUN2fSZKF9rJz%2FyPcmfE%2F2azS0J9aNDmayP6RKPP7JlMNw%2FpusYJS0Z2y2znLjUNmApAnm6deeAcwdNOsVSWtvE3iWjNXUb6y9pPow7v4zq6bH0bdQOARF1XNo0yArjU30NGl%2FHeU8f9t4vTqLJjqZewRgriuRhqF9V8B%2FDoZeMHwMax6ajHBOJ1%2BfqCcWitsCidsX7qX8X52aL9nwwaGqzwLE4zbyGyFmUePz1JcoTbI0kn7AG0rjYnPbmhsoT4KK6RbWYFoODME1njf7p4ZxhGkDBkBX4idvRGfIGzMA8V2bR66BcXeU2BdzH46O%2BksGCwfjtoVsRbGuy0kCqKSXrcnrmpYMqVug74wVxkHw5m8C0iajL1zL%2BYl6qlc%2FpZRHP7RxI4072%2FFnWoJk5VCzhVjg0r0Q3s7yYdVIGsAfN%2F8d5Avog8cdXiqP5YCybk%2BLZTv2uN84pU25jA6o0WfCnt%2BiqP9Fob02J3GR75H%2FK5%2BSKVSBUQT4bqoZJI2av8MPjE%2F8DM4ZlHT0Lczn6sR4o2OIw5ISGvQY6pgGfOVAFvWCOu5S%2Fqg32sFZCG3Ia%2BYKxeAKqhS%2BWgDC741L3ekJPJuLd%2FOaJFLCdT1TryxayL8KnB%2BOntL5o0pw403umUVtzdMGAe6mSfGOQVcyCsOwFwwPGbs5rODsVMoeursKwnKQ99%2BMKAWaFGEDKjFUXtBXxy0mfU1%2BOGhY34IWAKCLU5RHNvqZGNRxSIr2%2F5esPHHM%2FwaiHa0i8I6nkspG0my3q&X-Amz-Signature=c69b53a6c605565f3c84325873fd6840e112bd41de443d89e206cb5b389279f8&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RK3FVMBD%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031719Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJGMEQCICBYyx%2BL8mbK3iVkRrfcHZbD5PfnR5YVxl2NSzlBJQB%2BAiBenzIlLpyFwLmhewamCliLDPak60aomrdKFUrNnI%2F8GSr%2FAwgkEAAaDDYzNzQyMzE4MzgwNSIMFn6eZ8ha6LDL8UqSKtwDYBrzXnRgNpRHoAnlixZpanSeDLNJVtyJJ9Pjf6%2BV0HnXauyQAK%2BnFOmlbmpke%2FK%2Fi8Pvvaqd3VjOOcDw6vNwcE5H6TNgo8NFrDUN2fSZKF9rJz%2FyPcmfE%2F2azS0J9aNDmayP6RKPP7JlMNw%2FpusYJS0Z2y2znLjUNmApAnm6deeAcwdNOsVSWtvE3iWjNXUb6y9pPow7v4zq6bH0bdQOARF1XNo0yArjU30NGl%2FHeU8f9t4vTqLJjqZewRgriuRhqF9V8B%2FDoZeMHwMax6ajHBOJ1%2BfqCcWitsCidsX7qX8X52aL9nwwaGqzwLE4zbyGyFmUePz1JcoTbI0kn7AG0rjYnPbmhsoT4KK6RbWYFoODME1njf7p4ZxhGkDBkBX4idvRGfIGzMA8V2bR66BcXeU2BdzH46O%2BksGCwfjtoVsRbGuy0kCqKSXrcnrmpYMqVug74wVxkHw5m8C0iajL1zL%2BYl6qlc%2FpZRHP7RxI4072%2FFnWoJk5VCzhVjg0r0Q3s7yYdVIGsAfN%2F8d5Avog8cdXiqP5YCybk%2BLZTv2uN84pU25jA6o0WfCnt%2BiqP9Fob02J3GR75H%2FK5%2BSKVSBUQT4bqoZJI2av8MPjE%2F8DM4ZlHT0Lczn6sR4o2OIw5ISGvQY6pgGfOVAFvWCOu5S%2Fqg32sFZCG3Ia%2BYKxeAKqhS%2BWgDC741L3ekJPJuLd%2FOaJFLCdT1TryxayL8KnB%2BOntL5o0pw403umUVtzdMGAe6mSfGOQVcyCsOwFwwPGbs5rODsVMoeursKwnKQ99%2BMKAWaFGEDKjFUXtBXxy0mfU1%2BOGhY34IWAKCLU5RHNvqZGNRxSIr2%2F5esPHHM%2FwaiHa0i8I6nkspG0my3q&X-Amz-Signature=6de2cbc89bb00af9aedb95384ec6026007870b2c39d990fa4fcbcff322b1767e&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RK3FVMBD%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJGMEQCICBYyx%2BL8mbK3iVkRrfcHZbD5PfnR5YVxl2NSzlBJQB%2BAiBenzIlLpyFwLmhewamCliLDPak60aomrdKFUrNnI%2F8GSr%2FAwgkEAAaDDYzNzQyMzE4MzgwNSIMFn6eZ8ha6LDL8UqSKtwDYBrzXnRgNpRHoAnlixZpanSeDLNJVtyJJ9Pjf6%2BV0HnXauyQAK%2BnFOmlbmpke%2FK%2Fi8Pvvaqd3VjOOcDw6vNwcE5H6TNgo8NFrDUN2fSZKF9rJz%2FyPcmfE%2F2azS0J9aNDmayP6RKPP7JlMNw%2FpusYJS0Z2y2znLjUNmApAnm6deeAcwdNOsVSWtvE3iWjNXUb6y9pPow7v4zq6bH0bdQOARF1XNo0yArjU30NGl%2FHeU8f9t4vTqLJjqZewRgriuRhqF9V8B%2FDoZeMHwMax6ajHBOJ1%2BfqCcWitsCidsX7qX8X52aL9nwwaGqzwLE4zbyGyFmUePz1JcoTbI0kn7AG0rjYnPbmhsoT4KK6RbWYFoODME1njf7p4ZxhGkDBkBX4idvRGfIGzMA8V2bR66BcXeU2BdzH46O%2BksGCwfjtoVsRbGuy0kCqKSXrcnrmpYMqVug74wVxkHw5m8C0iajL1zL%2BYl6qlc%2FpZRHP7RxI4072%2FFnWoJk5VCzhVjg0r0Q3s7yYdVIGsAfN%2F8d5Avog8cdXiqP5YCybk%2BLZTv2uN84pU25jA6o0WfCnt%2BiqP9Fob02J3GR75H%2FK5%2BSKVSBUQT4bqoZJI2av8MPjE%2F8DM4ZlHT0Lczn6sR4o2OIw5ISGvQY6pgGfOVAFvWCOu5S%2Fqg32sFZCG3Ia%2BYKxeAKqhS%2BWgDC741L3ekJPJuLd%2FOaJFLCdT1TryxayL8KnB%2BOntL5o0pw403umUVtzdMGAe6mSfGOQVcyCsOwFwwPGbs5rODsVMoeursKwnKQ99%2BMKAWaFGEDKjFUXtBXxy0mfU1%2BOGhY34IWAKCLU5RHNvqZGNRxSIr2%2F5esPHHM%2FwaiHa0i8I6nkspG0my3q&X-Amz-Signature=0ed86767284b9955fbcb71fe8eb7d017d220f1f56fb4ba4077b90c720fe2123a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667677QTSG%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJHMEUCIHSwgh6DavML%2BSUciRbNrfFy3s6r0ioLS%2B9dOIp6MUWgAiEAy12ZpnABJvvLunhQfRrmvLFRmgQSZID1Jboh7hH%2BYoEq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDOWO1QbNQEO1673dACrcA3%2B3WEc8FVpXC0hjktQh13eJGPDEpOPR80Ex%2BfXnUePKLYpxER8SHggNhjp73W%2B9VQToduLTiw3vZBeJfRatriQIBKmG7pzgXb50jCi%2BMwTAf1urz4F4oZ%2BaDWlu9fOCyPnSho886H0Z864bD9IHR0wfbNJ3kMNx%2FH5shPeedj6jUleCCvr%2Ffv3OmVPalIDGlkBph3lKSdDhYjK3eZ8QeTMCUR85vtnTyRzDt27CFoVEzk2IDBVDb5gnpvTsUkUv%2FVqfVtxcfp2tGRN3cBbjWswfwLXFqmo89wUmN8GLdNIVhilLoB0YDiYLJU5UgEeISOGgmnoJz4SeGhbEAof%2FUyQ1Hg%2FrUDyzm%2FuIDlJdd14hX35%2FnMl3UC4%2Ba7%2FUPIxP%2FO4BK5KT8HxhGublUshMk%2B1nchDzCvh2MPtmg%2BgBbzXTjuELZtvl%2FMLBukMxxpq1d8imt67A%2Ftn8OFVMDKpE1VShvfPnEUvS%2B93wxTs7K5HeIH6L8VajzuzSqzAOUwz3bBDyaZ0TK82ykFdV4lCJTFq%2FZgFjFwIryjxF2l9r5E1aCl%2BXak%2BFUJiZB7DDxxgNU1wvDpJzg5i1sC6o0QZN4YocJXYrNPofgd1BQEwlEb3A9jsm38U4HGjrIDS%2BMLWFhr0GOqUB291BeeHQCvBY8wb%2BnvR%2FFjDIV6J4vmiI%2Fx0Iep1Puf958sU%2BCd%2BhpqCLPsPje6EP19slc64PRZAETdhYahIoQTBFPGCnO%2BX27tzEA1inonBKr1N4hyWrQVejvWbSJkOmMFdGSNNvDwd9yUy%2FSjNi77I9K6nNTn5adARN%2BqREqsWWFNC1%2FGt3xWyIQy66yB%2FGsrLOLIWsY5LjJ74fyOESKem4vm2u&X-Amz-Signature=f173cd16a6ffa19e1a32ece1244af5d640a73c7c1fe608a38638520b3210b732&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YM3WCN7I%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJHMEUCIQC2hTqT%2B2%2FXrqvHUaXdtF4zEjztjrpSsva78FcbLJQ76gIgaUp%2BUSE2FiQ8dyoJowHs3sg4FNWEgRBlE9aImAjvhcUq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDFV28nLB3IFzkCJfVCrcA8%2FJbXHHC%2FzQdADNrQLAaEVf5mEl96oyFUDYZ8SM4Inr8BSCQtn6lONYzt18GEJfFGAFU2cj64JdA12Q%2BfiQosy19AP9cUuTp75%2FdzoA7WM%2B0CM12jYTU98c6FSrrw2MT8QJ%2FeISNf%2B9GKdL3CgFkIqKbckwgpJpPODsbH3%2BmbdlGz0gswft5WZ4DtG5G4Rn6xGD9TxyBmq%2FCI9j6Kuj2QNY8s0VlAFuTz8zC4nlBtNo12EP5mmK8x00N3d%2BpLr0Acj3Jx%2BGQ6wwiIl%2FTezP7AQrUJ6cUjvYyYF9y5KvQhHRB6%2FaKzU%2BtB5RhwtykBiWoa8V8Kb5Nji8D5qJRvgxW5kf5Fo2gwSYKLnqB%2BzW1CdyAgnOPo1pIddwxJEaoiUW9YYVSXOMbothhd%2Bk6%2F%2BMTw7DNnjfbS3wCQzUHnSTS6aMZKOo2fRSiXAaXZxzEtsWvIms916pe4R5r5w7vu17KSRbdBLXnlUs4mzZmo81p5HBdPtBliX%2FBqSgNguAza1AhXM9lMNjAbm02Uhb2sCz6fmtE8KWbo0Mh7mVuqt3SZEcYrKMi0JY5GRLDgolOCP4aS4sijw8bmn6wBeaJ1Qk8NHUETOtGW3otI3wgIFyylmEby1JYVCCRDfwBG9iMJaFhr0GOqUBASwJuU%2BmP2w48HUyXKhv9iVJpQdNkvPPcBPZbjasI%2FLshpHd1fF%2FkKR5WxZmq5opS%2Fn%2BtRBjdHfQhXKbyqDWkqfSPFrjM%2FiI76Mop5Ax4dLetm2KLwkVQi0r8JbuBg64YAayvVNqCORj12CHHCQGgEJGcOWIol%2BDWDjWsG2ZvQNsHBhCXuOc9hlRwpEV8s6ijAJCBIcHVAIvwFwV3DtHSNVdKN2s&X-Amz-Signature=3679bc41c02b30171ebddbf15dbf987040a0593321f292110089d92c889908a9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RK3FVMBD%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJGMEQCICBYyx%2BL8mbK3iVkRrfcHZbD5PfnR5YVxl2NSzlBJQB%2BAiBenzIlLpyFwLmhewamCliLDPak60aomrdKFUrNnI%2F8GSr%2FAwgkEAAaDDYzNzQyMzE4MzgwNSIMFn6eZ8ha6LDL8UqSKtwDYBrzXnRgNpRHoAnlixZpanSeDLNJVtyJJ9Pjf6%2BV0HnXauyQAK%2BnFOmlbmpke%2FK%2Fi8Pvvaqd3VjOOcDw6vNwcE5H6TNgo8NFrDUN2fSZKF9rJz%2FyPcmfE%2F2azS0J9aNDmayP6RKPP7JlMNw%2FpusYJS0Z2y2znLjUNmApAnm6deeAcwdNOsVSWtvE3iWjNXUb6y9pPow7v4zq6bH0bdQOARF1XNo0yArjU30NGl%2FHeU8f9t4vTqLJjqZewRgriuRhqF9V8B%2FDoZeMHwMax6ajHBOJ1%2BfqCcWitsCidsX7qX8X52aL9nwwaGqzwLE4zbyGyFmUePz1JcoTbI0kn7AG0rjYnPbmhsoT4KK6RbWYFoODME1njf7p4ZxhGkDBkBX4idvRGfIGzMA8V2bR66BcXeU2BdzH46O%2BksGCwfjtoVsRbGuy0kCqKSXrcnrmpYMqVug74wVxkHw5m8C0iajL1zL%2BYl6qlc%2FpZRHP7RxI4072%2FFnWoJk5VCzhVjg0r0Q3s7yYdVIGsAfN%2F8d5Avog8cdXiqP5YCybk%2BLZTv2uN84pU25jA6o0WfCnt%2BiqP9Fob02J3GR75H%2FK5%2BSKVSBUQT4bqoZJI2av8MPjE%2F8DM4ZlHT0Lczn6sR4o2OIw5ISGvQY6pgGfOVAFvWCOu5S%2Fqg32sFZCG3Ia%2BYKxeAKqhS%2BWgDC741L3ekJPJuLd%2FOaJFLCdT1TryxayL8KnB%2BOntL5o0pw403umUVtzdMGAe6mSfGOQVcyCsOwFwwPGbs5rODsVMoeursKwnKQ99%2BMKAWaFGEDKjFUXtBXxy0mfU1%2BOGhY34IWAKCLU5RHNvqZGNRxSIr2%2F5esPHHM%2FwaiHa0i8I6nkspG0my3q&X-Amz-Signature=1d29275aae53b7fca87be89d27886814435ea1f92ad2d1becbd3bf7374cf90d2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RK3FVMBD%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJGMEQCICBYyx%2BL8mbK3iVkRrfcHZbD5PfnR5YVxl2NSzlBJQB%2BAiBenzIlLpyFwLmhewamCliLDPak60aomrdKFUrNnI%2F8GSr%2FAwgkEAAaDDYzNzQyMzE4MzgwNSIMFn6eZ8ha6LDL8UqSKtwDYBrzXnRgNpRHoAnlixZpanSeDLNJVtyJJ9Pjf6%2BV0HnXauyQAK%2BnFOmlbmpke%2FK%2Fi8Pvvaqd3VjOOcDw6vNwcE5H6TNgo8NFrDUN2fSZKF9rJz%2FyPcmfE%2F2azS0J9aNDmayP6RKPP7JlMNw%2FpusYJS0Z2y2znLjUNmApAnm6deeAcwdNOsVSWtvE3iWjNXUb6y9pPow7v4zq6bH0bdQOARF1XNo0yArjU30NGl%2FHeU8f9t4vTqLJjqZewRgriuRhqF9V8B%2FDoZeMHwMax6ajHBOJ1%2BfqCcWitsCidsX7qX8X52aL9nwwaGqzwLE4zbyGyFmUePz1JcoTbI0kn7AG0rjYnPbmhsoT4KK6RbWYFoODME1njf7p4ZxhGkDBkBX4idvRGfIGzMA8V2bR66BcXeU2BdzH46O%2BksGCwfjtoVsRbGuy0kCqKSXrcnrmpYMqVug74wVxkHw5m8C0iajL1zL%2BYl6qlc%2FpZRHP7RxI4072%2FFnWoJk5VCzhVjg0r0Q3s7yYdVIGsAfN%2F8d5Avog8cdXiqP5YCybk%2BLZTv2uN84pU25jA6o0WfCnt%2BiqP9Fob02J3GR75H%2FK5%2BSKVSBUQT4bqoZJI2av8MPjE%2F8DM4ZlHT0Lczn6sR4o2OIw5ISGvQY6pgGfOVAFvWCOu5S%2Fqg32sFZCG3Ia%2BYKxeAKqhS%2BWgDC741L3ekJPJuLd%2FOaJFLCdT1TryxayL8KnB%2BOntL5o0pw403umUVtzdMGAe6mSfGOQVcyCsOwFwwPGbs5rODsVMoeursKwnKQ99%2BMKAWaFGEDKjFUXtBXxy0mfU1%2BOGhY34IWAKCLU5RHNvqZGNRxSIr2%2F5esPHHM%2FwaiHa0i8I6nkspG0my3q&X-Amz-Signature=44a477540487ec0a69b6a7f8562412b7b70c7d0857ef23ba9f975824219b5164&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RK3FVMBD%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJGMEQCICBYyx%2BL8mbK3iVkRrfcHZbD5PfnR5YVxl2NSzlBJQB%2BAiBenzIlLpyFwLmhewamCliLDPak60aomrdKFUrNnI%2F8GSr%2FAwgkEAAaDDYzNzQyMzE4MzgwNSIMFn6eZ8ha6LDL8UqSKtwDYBrzXnRgNpRHoAnlixZpanSeDLNJVtyJJ9Pjf6%2BV0HnXauyQAK%2BnFOmlbmpke%2FK%2Fi8Pvvaqd3VjOOcDw6vNwcE5H6TNgo8NFrDUN2fSZKF9rJz%2FyPcmfE%2F2azS0J9aNDmayP6RKPP7JlMNw%2FpusYJS0Z2y2znLjUNmApAnm6deeAcwdNOsVSWtvE3iWjNXUb6y9pPow7v4zq6bH0bdQOARF1XNo0yArjU30NGl%2FHeU8f9t4vTqLJjqZewRgriuRhqF9V8B%2FDoZeMHwMax6ajHBOJ1%2BfqCcWitsCidsX7qX8X52aL9nwwaGqzwLE4zbyGyFmUePz1JcoTbI0kn7AG0rjYnPbmhsoT4KK6RbWYFoODME1njf7p4ZxhGkDBkBX4idvRGfIGzMA8V2bR66BcXeU2BdzH46O%2BksGCwfjtoVsRbGuy0kCqKSXrcnrmpYMqVug74wVxkHw5m8C0iajL1zL%2BYl6qlc%2FpZRHP7RxI4072%2FFnWoJk5VCzhVjg0r0Q3s7yYdVIGsAfN%2F8d5Avog8cdXiqP5YCybk%2BLZTv2uN84pU25jA6o0WfCnt%2BiqP9Fob02J3GR75H%2FK5%2BSKVSBUQT4bqoZJI2av8MPjE%2F8DM4ZlHT0Lczn6sR4o2OIw5ISGvQY6pgGfOVAFvWCOu5S%2Fqg32sFZCG3Ia%2BYKxeAKqhS%2BWgDC741L3ekJPJuLd%2FOaJFLCdT1TryxayL8KnB%2BOntL5o0pw403umUVtzdMGAe6mSfGOQVcyCsOwFwwPGbs5rODsVMoeursKwnKQ99%2BMKAWaFGEDKjFUXtBXxy0mfU1%2BOGhY34IWAKCLU5RHNvqZGNRxSIr2%2F5esPHHM%2FwaiHa0i8I6nkspG0my3q&X-Amz-Signature=8ebfc4c30ac406e6c01e1d296dc9cec601a068c33ae9a300ea2c0513054f09cf&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RK3FVMBD%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJGMEQCICBYyx%2BL8mbK3iVkRrfcHZbD5PfnR5YVxl2NSzlBJQB%2BAiBenzIlLpyFwLmhewamCliLDPak60aomrdKFUrNnI%2F8GSr%2FAwgkEAAaDDYzNzQyMzE4MzgwNSIMFn6eZ8ha6LDL8UqSKtwDYBrzXnRgNpRHoAnlixZpanSeDLNJVtyJJ9Pjf6%2BV0HnXauyQAK%2BnFOmlbmpke%2FK%2Fi8Pvvaqd3VjOOcDw6vNwcE5H6TNgo8NFrDUN2fSZKF9rJz%2FyPcmfE%2F2azS0J9aNDmayP6RKPP7JlMNw%2FpusYJS0Z2y2znLjUNmApAnm6deeAcwdNOsVSWtvE3iWjNXUb6y9pPow7v4zq6bH0bdQOARF1XNo0yArjU30NGl%2FHeU8f9t4vTqLJjqZewRgriuRhqF9V8B%2FDoZeMHwMax6ajHBOJ1%2BfqCcWitsCidsX7qX8X52aL9nwwaGqzwLE4zbyGyFmUePz1JcoTbI0kn7AG0rjYnPbmhsoT4KK6RbWYFoODME1njf7p4ZxhGkDBkBX4idvRGfIGzMA8V2bR66BcXeU2BdzH46O%2BksGCwfjtoVsRbGuy0kCqKSXrcnrmpYMqVug74wVxkHw5m8C0iajL1zL%2BYl6qlc%2FpZRHP7RxI4072%2FFnWoJk5VCzhVjg0r0Q3s7yYdVIGsAfN%2F8d5Avog8cdXiqP5YCybk%2BLZTv2uN84pU25jA6o0WfCnt%2BiqP9Fob02J3GR75H%2FK5%2BSKVSBUQT4bqoZJI2av8MPjE%2F8DM4ZlHT0Lczn6sR4o2OIw5ISGvQY6pgGfOVAFvWCOu5S%2Fqg32sFZCG3Ia%2BYKxeAKqhS%2BWgDC741L3ekJPJuLd%2FOaJFLCdT1TryxayL8KnB%2BOntL5o0pw403umUVtzdMGAe6mSfGOQVcyCsOwFwwPGbs5rODsVMoeursKwnKQ99%2BMKAWaFGEDKjFUXtBXxy0mfU1%2BOGhY34IWAKCLU5RHNvqZGNRxSIr2%2F5esPHHM%2FwaiHa0i8I6nkspG0my3q&X-Amz-Signature=01acaf715f39779be2c23aed5818d16bf5c1dde92e1b4d5576ad0f686d7ac9a1&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
