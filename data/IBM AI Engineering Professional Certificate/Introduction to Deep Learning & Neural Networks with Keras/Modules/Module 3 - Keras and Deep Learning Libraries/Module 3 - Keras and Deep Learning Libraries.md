

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNY2BBG7%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQCJEs4YsITG6w9U8Dofof3tMooO4XdDsTmy5rp%2FEOk4FAIhAOtLc3UXcQpGyRIBwZOb0QJh0J4vJy0nyrWjI3ScVe6tKv8DCCYQABoMNjM3NDIzMTgzODA1IgwuMJjfU3h0gn1s4sEq3AOmo0IQAVrHja6ih1Ha2%2FvTWuOCEmT%2BZpUdEJ6LH46qRjK2wCM4MGiwdZo0G8DaGlHnsJE0F%2FO%2F2YiXUHM7UydDb5L5ilTCibpGV3Oxcq8%2F%2BYtlNy6TVsm7rY2HibRz1I%2Bsl%2B63PJ%2F7dKMI1wuhR4snnJ%2BG4xDEGLlCvJnJCQ555tPYsitW21lz%2FvrmfLFvM64m%2B6gifDNpeizpOpVkdSVQ4BiWcdtW7r7MQ4R55lyVSbW6ol%2BEYCRYa0FUvhevNLPJwY2JafzcblB0A%2F1D1fM9bSKL7J1PwLBK14T%2Fasc0qKN8KDMY9VxUmnlq5jPIwIUWG%2BFDF8Gk2eiHJCochRlkYgDod%2BxFvuSS88LYR82fT%2BlCeIszUF5ytnMyS6wOqaQDdP8CNT4xJTkQ%2BW8PtBVSKaSqgmUmWQ8VNgx5Wdi9doPw6Elocrqj0OR1x1%2BW6PpKjf6ThsDERkEjOstWBc09Gjw1QB%2BpDd2HnwANsZDWdfsWTK%2F%2FLeDvSDJY2onGzWsYrTxRltKyXKXb4ezoLZdluLuhV0ZfDgUaAR%2F6M%2Bqlr01Jx2Z3N6lUo9ExRM0avT3QXH7pgizGr%2FMzGYEyxO1RkVQnhXusfH8wUTDTciEHpdA8c0ZWyXk6U4wyFjCMv4a9BjqkAQ6t4nVOsFTXkJ6xx40WSA6xVbri6ejlzkeRPFzAVjRlC2Gs4n99%2FL2IiX2frGzRTVPSYacCL9vENOCT1gvMaaqRLJzIJIcR5lBp6kP98vdqch0jtiJt9%2FsfeUQ0531l4MFtvmLlvy%2BGMdVa3h6KZtxGu4cFXbqerRXhaVYAwLI%2F9VC3KGqqEkGE4YFsUu4snKHdiiMS%2FkjkMksPvVr%2F6%2FNjhbot&X-Amz-Signature=9dbcb57d659930da5b3608a94f632a20a7797579a4ca5bcfc3281f3cb34e5d11&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNY2BBG7%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQCJEs4YsITG6w9U8Dofof3tMooO4XdDsTmy5rp%2FEOk4FAIhAOtLc3UXcQpGyRIBwZOb0QJh0J4vJy0nyrWjI3ScVe6tKv8DCCYQABoMNjM3NDIzMTgzODA1IgwuMJjfU3h0gn1s4sEq3AOmo0IQAVrHja6ih1Ha2%2FvTWuOCEmT%2BZpUdEJ6LH46qRjK2wCM4MGiwdZo0G8DaGlHnsJE0F%2FO%2F2YiXUHM7UydDb5L5ilTCibpGV3Oxcq8%2F%2BYtlNy6TVsm7rY2HibRz1I%2Bsl%2B63PJ%2F7dKMI1wuhR4snnJ%2BG4xDEGLlCvJnJCQ555tPYsitW21lz%2FvrmfLFvM64m%2B6gifDNpeizpOpVkdSVQ4BiWcdtW7r7MQ4R55lyVSbW6ol%2BEYCRYa0FUvhevNLPJwY2JafzcblB0A%2F1D1fM9bSKL7J1PwLBK14T%2Fasc0qKN8KDMY9VxUmnlq5jPIwIUWG%2BFDF8Gk2eiHJCochRlkYgDod%2BxFvuSS88LYR82fT%2BlCeIszUF5ytnMyS6wOqaQDdP8CNT4xJTkQ%2BW8PtBVSKaSqgmUmWQ8VNgx5Wdi9doPw6Elocrqj0OR1x1%2BW6PpKjf6ThsDERkEjOstWBc09Gjw1QB%2BpDd2HnwANsZDWdfsWTK%2F%2FLeDvSDJY2onGzWsYrTxRltKyXKXb4ezoLZdluLuhV0ZfDgUaAR%2F6M%2Bqlr01Jx2Z3N6lUo9ExRM0avT3QXH7pgizGr%2FMzGYEyxO1RkVQnhXusfH8wUTDTciEHpdA8c0ZWyXk6U4wyFjCMv4a9BjqkAQ6t4nVOsFTXkJ6xx40WSA6xVbri6ejlzkeRPFzAVjRlC2Gs4n99%2FL2IiX2frGzRTVPSYacCL9vENOCT1gvMaaqRLJzIJIcR5lBp6kP98vdqch0jtiJt9%2FsfeUQ0531l4MFtvmLlvy%2BGMdVa3h6KZtxGu4cFXbqerRXhaVYAwLI%2F9VC3KGqqEkGE4YFsUu4snKHdiiMS%2FkjkMksPvVr%2F6%2FNjhbot&X-Amz-Signature=378c41f86f4241fd4fce0b39501436937dbec1766b6c0d4b2790ec721b40e374&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNY2BBG7%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQCJEs4YsITG6w9U8Dofof3tMooO4XdDsTmy5rp%2FEOk4FAIhAOtLc3UXcQpGyRIBwZOb0QJh0J4vJy0nyrWjI3ScVe6tKv8DCCYQABoMNjM3NDIzMTgzODA1IgwuMJjfU3h0gn1s4sEq3AOmo0IQAVrHja6ih1Ha2%2FvTWuOCEmT%2BZpUdEJ6LH46qRjK2wCM4MGiwdZo0G8DaGlHnsJE0F%2FO%2F2YiXUHM7UydDb5L5ilTCibpGV3Oxcq8%2F%2BYtlNy6TVsm7rY2HibRz1I%2Bsl%2B63PJ%2F7dKMI1wuhR4snnJ%2BG4xDEGLlCvJnJCQ555tPYsitW21lz%2FvrmfLFvM64m%2B6gifDNpeizpOpVkdSVQ4BiWcdtW7r7MQ4R55lyVSbW6ol%2BEYCRYa0FUvhevNLPJwY2JafzcblB0A%2F1D1fM9bSKL7J1PwLBK14T%2Fasc0qKN8KDMY9VxUmnlq5jPIwIUWG%2BFDF8Gk2eiHJCochRlkYgDod%2BxFvuSS88LYR82fT%2BlCeIszUF5ytnMyS6wOqaQDdP8CNT4xJTkQ%2BW8PtBVSKaSqgmUmWQ8VNgx5Wdi9doPw6Elocrqj0OR1x1%2BW6PpKjf6ThsDERkEjOstWBc09Gjw1QB%2BpDd2HnwANsZDWdfsWTK%2F%2FLeDvSDJY2onGzWsYrTxRltKyXKXb4ezoLZdluLuhV0ZfDgUaAR%2F6M%2Bqlr01Jx2Z3N6lUo9ExRM0avT3QXH7pgizGr%2FMzGYEyxO1RkVQnhXusfH8wUTDTciEHpdA8c0ZWyXk6U4wyFjCMv4a9BjqkAQ6t4nVOsFTXkJ6xx40WSA6xVbri6ejlzkeRPFzAVjRlC2Gs4n99%2FL2IiX2frGzRTVPSYacCL9vENOCT1gvMaaqRLJzIJIcR5lBp6kP98vdqch0jtiJt9%2FsfeUQ0531l4MFtvmLlvy%2BGMdVa3h6KZtxGu4cFXbqerRXhaVYAwLI%2F9VC3KGqqEkGE4YFsUu4snKHdiiMS%2FkjkMksPvVr%2F6%2FNjhbot&X-Amz-Signature=d479d9a3c19e20d126eb5360f297277698b8434360b49138b8b3e3bfb66d40f6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USM6IOPC%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJIMEYCIQCJdEuTBWV5VYq19t990u4i0f%2Fc9F1S4xLbHli7d1jlXwIhAP9an2kaYIDvt1Fb1wdBVcDf%2FG3TYEX9cPb69t%2BKm5%2BSKv8DCCcQABoMNjM3NDIzMTgzODA1IgyrUqjVOccGjyU5mk0q3AOl%2B6C03Y9XK1SBAD8h%2FGqcELXQuyUlcmcFLbDQ5SBuWkaduh1kgi3DzPcRZwHADU%2BPqJkQxgBPky8%2BgdnBmkfiuQ%2BkX0aVGpi%2BqNAVIlUpMtZrzxWsJby4bhf9BL3k%2BipNbd0Tz5hO71pgu3uzHcYNdZiwdl6une%2BBL59hLrGWbmxugU11InqqNlaQVVYxhr7ISrww92FJdkKQRX1p82fOrKgV48bfDKAy9la828QmmpVUfTk%2B03IQsMdRKyqoby2n9GeEdOdDTHVOdMXoAcmgJC6iGBfsJsVK6e7ZQ1JwhyJHSmKCfIK06DctQX89YuDjeD3K5mz3oU6yYDHZE36QBohxz6rPNbqeS3wDipmkdI1z86M4%2BqHlGWPLPvNt6qx4ENlFgE%2BoBIqlZs3WuR48LgdgnHw2GjufXFauU%2BquwafzXrOT9NSgz3zFnEOaFIHlnjAxEbAd6GPq7VhTjsvlkAHvWm9iX0gT7SgrwsPSbVzdLnTeZl1T8p2ShFvOCFSyXr%2F1vtfJ0mUtzciFTxUAuIss746dWNXNlZPGGFeZkmDhdCAAAbsrMeMLPzMHX%2FCTOPECWhs1p7lfeL0ksv8n4SrpX%2BCQdldYks7p7f0OOmsWXl9lLIoFgG6FxDCJ4oa9BjqkASrKolzVINNGO67SFlXPPHstFNt0l4cE6FrjBL1Hd6Xg1fu9W51vlSR82Ev9qF1eR6dzRcHHMGeQCzMxQhtEY8y9U1Eov%2Bo1iVUqbBy8hn8wq%2FMqGT6tWhjpKOz%2BueAOcdlu2fFq9ZMKespfCjelFgEpXoaH%2Fu6tqGDVCfEJD%2BkAhDMePtAaXCByOpUb4yLhFpujwjCUv9cnE9TclOw5ma7JLpTb&X-Amz-Signature=a70f84f14b4a216de4cef6f354175e30600d2f1c61c8f8fd154690d8a6ce7f90&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664GEQQMOZ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQCFrC1yWyYZfISEc%2By1mGyebadH5UwoS7VcI7RaRZKeSgIhAItxs%2FlqAF%2Fcdj6vjFuigJIVwqUFxypLaIz1z79DPUBaKv8DCCYQABoMNjM3NDIzMTgzODA1IgySJyK1m8HNviQKNvQq3AOGg9Sl0yVW%2BAk0N8bNLOSK7ge7rHDZTbhbm3%2F5ckxWhnoZUqCbhaUQljFoTSHidvwXuM7bDY2%2FWM1PNkaIfWeFiT5oparmkgC2uSmA83WXxXEGvV2%2BqFnbHLUrAyVyHX3bjyMfZM4jcP%2Fz9YQV4v7G%2Bk8LwgObgIsVTmOtHhruPY0pNKy9cWUcFKPPFd%2F1tuOs9e8VQouPHrjgbCXf1u1AbPHLwmWzC7%2Bvah2%2ByEfxga44ZBfPLV4yLWRfPPLT1TDUJ6TgGoHseePKR73G%2B8nfbhg12j3yS3hBOYPsCZgD%2FVupvX%2FiCeaLdH2Te5fVYpxJRqBepoYjp3PZnPZvkHVBaM0NmlQRVyyRYU4fKcyTSnjqLAp5f3uIvLkMF25hCxHSAf9T7ohaJN1rdpUgdO9b8%2FEGoUE3s5TYiWikE%2F5OHRK14cWitoe%2FKdpM0yl6QUKwMKv4uOJ9tCdOkddxg6oJF2PJZJsFv5jfTmbAeIbPDNQ9WT7SO7Wf%2BuRueGgbwjonH5zyhiri9FF9C4kWoVPPfPSrD8Fjhk018yEpoNPXw8ZHPfBVvNolmjxj82p007orvqK6w7Szm8MupeBZG9FIrc5bvg8wb%2FvTOX2otoywgenIgHCY6nSW5FCc8jCUv4a9BjqkAbyjfnjv%2B%2FJTyOk4V9t8r096QXPUh25NbJYCci9Hu6V62sPbu9TLlTk1R3vAlhBICDkQa5hgk3Il0ykjbvMBtgaIahf2qq6c7LBVfh1Lt8cZqtZM6WzsRUYJSqa2WMsP5vtTRO5OvFzP%2F2bBPRIY9xZqXk0LhixH3vRBueaD4ZfbN0at%2BFh%2BDJRVln5PEtsToi44XcANNnV6XCw73EvJLBDwGWoa&X-Amz-Signature=d1eb6ab707ba2262720e5c1846b4d2a006ff7da415c203b2f8dd8d967a0bffef&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNY2BBG7%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQCJEs4YsITG6w9U8Dofof3tMooO4XdDsTmy5rp%2FEOk4FAIhAOtLc3UXcQpGyRIBwZOb0QJh0J4vJy0nyrWjI3ScVe6tKv8DCCYQABoMNjM3NDIzMTgzODA1IgwuMJjfU3h0gn1s4sEq3AOmo0IQAVrHja6ih1Ha2%2FvTWuOCEmT%2BZpUdEJ6LH46qRjK2wCM4MGiwdZo0G8DaGlHnsJE0F%2FO%2F2YiXUHM7UydDb5L5ilTCibpGV3Oxcq8%2F%2BYtlNy6TVsm7rY2HibRz1I%2Bsl%2B63PJ%2F7dKMI1wuhR4snnJ%2BG4xDEGLlCvJnJCQ555tPYsitW21lz%2FvrmfLFvM64m%2B6gifDNpeizpOpVkdSVQ4BiWcdtW7r7MQ4R55lyVSbW6ol%2BEYCRYa0FUvhevNLPJwY2JafzcblB0A%2F1D1fM9bSKL7J1PwLBK14T%2Fasc0qKN8KDMY9VxUmnlq5jPIwIUWG%2BFDF8Gk2eiHJCochRlkYgDod%2BxFvuSS88LYR82fT%2BlCeIszUF5ytnMyS6wOqaQDdP8CNT4xJTkQ%2BW8PtBVSKaSqgmUmWQ8VNgx5Wdi9doPw6Elocrqj0OR1x1%2BW6PpKjf6ThsDERkEjOstWBc09Gjw1QB%2BpDd2HnwANsZDWdfsWTK%2F%2FLeDvSDJY2onGzWsYrTxRltKyXKXb4ezoLZdluLuhV0ZfDgUaAR%2F6M%2Bqlr01Jx2Z3N6lUo9ExRM0avT3QXH7pgizGr%2FMzGYEyxO1RkVQnhXusfH8wUTDTciEHpdA8c0ZWyXk6U4wyFjCMv4a9BjqkAQ6t4nVOsFTXkJ6xx40WSA6xVbri6ejlzkeRPFzAVjRlC2Gs4n99%2FL2IiX2frGzRTVPSYacCL9vENOCT1gvMaaqRLJzIJIcR5lBp6kP98vdqch0jtiJt9%2FsfeUQ0531l4MFtvmLlvy%2BGMdVa3h6KZtxGu4cFXbqerRXhaVYAwLI%2F9VC3KGqqEkGE4YFsUu4snKHdiiMS%2FkjkMksPvVr%2F6%2FNjhbot&X-Amz-Signature=85513b20abf45a799b894283c7104af4cc8dcb5b43d39ad8403605d51b78ef6b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNY2BBG7%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQCJEs4YsITG6w9U8Dofof3tMooO4XdDsTmy5rp%2FEOk4FAIhAOtLc3UXcQpGyRIBwZOb0QJh0J4vJy0nyrWjI3ScVe6tKv8DCCYQABoMNjM3NDIzMTgzODA1IgwuMJjfU3h0gn1s4sEq3AOmo0IQAVrHja6ih1Ha2%2FvTWuOCEmT%2BZpUdEJ6LH46qRjK2wCM4MGiwdZo0G8DaGlHnsJE0F%2FO%2F2YiXUHM7UydDb5L5ilTCibpGV3Oxcq8%2F%2BYtlNy6TVsm7rY2HibRz1I%2Bsl%2B63PJ%2F7dKMI1wuhR4snnJ%2BG4xDEGLlCvJnJCQ555tPYsitW21lz%2FvrmfLFvM64m%2B6gifDNpeizpOpVkdSVQ4BiWcdtW7r7MQ4R55lyVSbW6ol%2BEYCRYa0FUvhevNLPJwY2JafzcblB0A%2F1D1fM9bSKL7J1PwLBK14T%2Fasc0qKN8KDMY9VxUmnlq5jPIwIUWG%2BFDF8Gk2eiHJCochRlkYgDod%2BxFvuSS88LYR82fT%2BlCeIszUF5ytnMyS6wOqaQDdP8CNT4xJTkQ%2BW8PtBVSKaSqgmUmWQ8VNgx5Wdi9doPw6Elocrqj0OR1x1%2BW6PpKjf6ThsDERkEjOstWBc09Gjw1QB%2BpDd2HnwANsZDWdfsWTK%2F%2FLeDvSDJY2onGzWsYrTxRltKyXKXb4ezoLZdluLuhV0ZfDgUaAR%2F6M%2Bqlr01Jx2Z3N6lUo9ExRM0avT3QXH7pgizGr%2FMzGYEyxO1RkVQnhXusfH8wUTDTciEHpdA8c0ZWyXk6U4wyFjCMv4a9BjqkAQ6t4nVOsFTXkJ6xx40WSA6xVbri6ejlzkeRPFzAVjRlC2Gs4n99%2FL2IiX2frGzRTVPSYacCL9vENOCT1gvMaaqRLJzIJIcR5lBp6kP98vdqch0jtiJt9%2FsfeUQ0531l4MFtvmLlvy%2BGMdVa3h6KZtxGu4cFXbqerRXhaVYAwLI%2F9VC3KGqqEkGE4YFsUu4snKHdiiMS%2FkjkMksPvVr%2F6%2FNjhbot&X-Amz-Signature=6110e367a84802f92ce742b90e8578fbd527f777de87beffedac14bfcd9e6404&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNY2BBG7%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQCJEs4YsITG6w9U8Dofof3tMooO4XdDsTmy5rp%2FEOk4FAIhAOtLc3UXcQpGyRIBwZOb0QJh0J4vJy0nyrWjI3ScVe6tKv8DCCYQABoMNjM3NDIzMTgzODA1IgwuMJjfU3h0gn1s4sEq3AOmo0IQAVrHja6ih1Ha2%2FvTWuOCEmT%2BZpUdEJ6LH46qRjK2wCM4MGiwdZo0G8DaGlHnsJE0F%2FO%2F2YiXUHM7UydDb5L5ilTCibpGV3Oxcq8%2F%2BYtlNy6TVsm7rY2HibRz1I%2Bsl%2B63PJ%2F7dKMI1wuhR4snnJ%2BG4xDEGLlCvJnJCQ555tPYsitW21lz%2FvrmfLFvM64m%2B6gifDNpeizpOpVkdSVQ4BiWcdtW7r7MQ4R55lyVSbW6ol%2BEYCRYa0FUvhevNLPJwY2JafzcblB0A%2F1D1fM9bSKL7J1PwLBK14T%2Fasc0qKN8KDMY9VxUmnlq5jPIwIUWG%2BFDF8Gk2eiHJCochRlkYgDod%2BxFvuSS88LYR82fT%2BlCeIszUF5ytnMyS6wOqaQDdP8CNT4xJTkQ%2BW8PtBVSKaSqgmUmWQ8VNgx5Wdi9doPw6Elocrqj0OR1x1%2BW6PpKjf6ThsDERkEjOstWBc09Gjw1QB%2BpDd2HnwANsZDWdfsWTK%2F%2FLeDvSDJY2onGzWsYrTxRltKyXKXb4ezoLZdluLuhV0ZfDgUaAR%2F6M%2Bqlr01Jx2Z3N6lUo9ExRM0avT3QXH7pgizGr%2FMzGYEyxO1RkVQnhXusfH8wUTDTciEHpdA8c0ZWyXk6U4wyFjCMv4a9BjqkAQ6t4nVOsFTXkJ6xx40WSA6xVbri6ejlzkeRPFzAVjRlC2Gs4n99%2FL2IiX2frGzRTVPSYacCL9vENOCT1gvMaaqRLJzIJIcR5lBp6kP98vdqch0jtiJt9%2FsfeUQ0531l4MFtvmLlvy%2BGMdVa3h6KZtxGu4cFXbqerRXhaVYAwLI%2F9VC3KGqqEkGE4YFsUu4snKHdiiMS%2FkjkMksPvVr%2F6%2FNjhbot&X-Amz-Signature=91d68b7d95bbfab18ce429c1534e7da3764d188900ffacf158fbe40f7af0fb01&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNY2BBG7%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQCJEs4YsITG6w9U8Dofof3tMooO4XdDsTmy5rp%2FEOk4FAIhAOtLc3UXcQpGyRIBwZOb0QJh0J4vJy0nyrWjI3ScVe6tKv8DCCYQABoMNjM3NDIzMTgzODA1IgwuMJjfU3h0gn1s4sEq3AOmo0IQAVrHja6ih1Ha2%2FvTWuOCEmT%2BZpUdEJ6LH46qRjK2wCM4MGiwdZo0G8DaGlHnsJE0F%2FO%2F2YiXUHM7UydDb5L5ilTCibpGV3Oxcq8%2F%2BYtlNy6TVsm7rY2HibRz1I%2Bsl%2B63PJ%2F7dKMI1wuhR4snnJ%2BG4xDEGLlCvJnJCQ555tPYsitW21lz%2FvrmfLFvM64m%2B6gifDNpeizpOpVkdSVQ4BiWcdtW7r7MQ4R55lyVSbW6ol%2BEYCRYa0FUvhevNLPJwY2JafzcblB0A%2F1D1fM9bSKL7J1PwLBK14T%2Fasc0qKN8KDMY9VxUmnlq5jPIwIUWG%2BFDF8Gk2eiHJCochRlkYgDod%2BxFvuSS88LYR82fT%2BlCeIszUF5ytnMyS6wOqaQDdP8CNT4xJTkQ%2BW8PtBVSKaSqgmUmWQ8VNgx5Wdi9doPw6Elocrqj0OR1x1%2BW6PpKjf6ThsDERkEjOstWBc09Gjw1QB%2BpDd2HnwANsZDWdfsWTK%2F%2FLeDvSDJY2onGzWsYrTxRltKyXKXb4ezoLZdluLuhV0ZfDgUaAR%2F6M%2Bqlr01Jx2Z3N6lUo9ExRM0avT3QXH7pgizGr%2FMzGYEyxO1RkVQnhXusfH8wUTDTciEHpdA8c0ZWyXk6U4wyFjCMv4a9BjqkAQ6t4nVOsFTXkJ6xx40WSA6xVbri6ejlzkeRPFzAVjRlC2Gs4n99%2FL2IiX2frGzRTVPSYacCL9vENOCT1gvMaaqRLJzIJIcR5lBp6kP98vdqch0jtiJt9%2FsfeUQ0531l4MFtvmLlvy%2BGMdVa3h6KZtxGu4cFXbqerRXhaVYAwLI%2F9VC3KGqqEkGE4YFsUu4snKHdiiMS%2FkjkMksPvVr%2F6%2FNjhbot&X-Amz-Signature=d947eb854f072317ea54edaa9325e748f8a46f04866c8604b9ff798f3b30cd77&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
