

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZWLOBQ6%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIQDolpPKyfODHwOSq3%2FnqlEo3KFU62arOGV31sht1uaRWgIgeNSepgTGL4THkR3WL9vVhPW8rw8Vnn9lN%2FJX%2BylXPP8q%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDJnsJp0xgjQMUogihircA8zdBcG8CBmLGnQ7rZC%2BM8qircBoNJaq2G9fwcaRS9IvNI0TGwa86mjVVAOXOAx3eP8e916OJyEfGXLpz85quLUdszcIhl5DOga0SezAF3cY4NhCf7Hd7RFbzB%2B2xfVyGtQDNvCALAYrovxxLC49fiPF0zGOEcE4pavIhNrXBnSLbQ6BywXpm94p%2BaY53E9DmVzXcB9I1VgSyUpxDBeL%2BRiS3DCiQG1R25vgu%2Bd%2BnEZcKDY%2B%2FRFUdY1AsxZHf9CPoo%2BdFEBHUoifs0XHqfum2oeExDYYjeRqynNHlro7lSdBmy8MKnhd%2F6RtoNWhEVVDFzsowx8bh0m7JCPw62T1L%2BXatc8ZysMBhVsC4jqij078qIGb%2Bf%2BhmlT%2FfnU1IVFRRhrR%2BT5QWqewPlmA5gnwL2QT6tpPm7kYV%2BacSHBGg9zH%2Fr6sCKH%2FnKRjVkqQSgNrupYIWkQ1KUtInAE6hBFXG3HVD9rW5txesc4oAKprCRiHLBJShUURHK9KD32HwXkEqolfRH%2FJYHxDCKqBRxHVQwPV6aoD%2FA94ulO9dGBNuiy8idM6hMnHrFD9KSTLcWLseOmFcmhOGCWRCAcEoXVGrJv5jRmyfM%2FZoGvWV2eVCY18oBDfNk2RzVZ8PbA6MJLrj70GOqUBE7gwW4zzgc4NMN0BK6LT3g9BGPO%2BFQroyfPOzzeVjsozE55zc9AydRgZuiP7o0aFbYkOlxU9GUMAlUJ1zu7TD86s3z3c7HYeyj5AAz7bN%2FXbnYOaytkRTHhQgUJfB%2F%2BqiTGXUEAwOcRN0D33oKJDU7T6zrqyt9hCZnzpxzKYjNJ8wL9g1Zwgo1v9FDywH670%2FT2GrlsTlan4DDJXxBsh8NyKtsfN&X-Amz-Signature=3cc927d65ab4f5b3ec732804ccd07780f134d5809c05ef7cc714129e3ea43c30&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZWLOBQ6%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIQDolpPKyfODHwOSq3%2FnqlEo3KFU62arOGV31sht1uaRWgIgeNSepgTGL4THkR3WL9vVhPW8rw8Vnn9lN%2FJX%2BylXPP8q%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDJnsJp0xgjQMUogihircA8zdBcG8CBmLGnQ7rZC%2BM8qircBoNJaq2G9fwcaRS9IvNI0TGwa86mjVVAOXOAx3eP8e916OJyEfGXLpz85quLUdszcIhl5DOga0SezAF3cY4NhCf7Hd7RFbzB%2B2xfVyGtQDNvCALAYrovxxLC49fiPF0zGOEcE4pavIhNrXBnSLbQ6BywXpm94p%2BaY53E9DmVzXcB9I1VgSyUpxDBeL%2BRiS3DCiQG1R25vgu%2Bd%2BnEZcKDY%2B%2FRFUdY1AsxZHf9CPoo%2BdFEBHUoifs0XHqfum2oeExDYYjeRqynNHlro7lSdBmy8MKnhd%2F6RtoNWhEVVDFzsowx8bh0m7JCPw62T1L%2BXatc8ZysMBhVsC4jqij078qIGb%2Bf%2BhmlT%2FfnU1IVFRRhrR%2BT5QWqewPlmA5gnwL2QT6tpPm7kYV%2BacSHBGg9zH%2Fr6sCKH%2FnKRjVkqQSgNrupYIWkQ1KUtInAE6hBFXG3HVD9rW5txesc4oAKprCRiHLBJShUURHK9KD32HwXkEqolfRH%2FJYHxDCKqBRxHVQwPV6aoD%2FA94ulO9dGBNuiy8idM6hMnHrFD9KSTLcWLseOmFcmhOGCWRCAcEoXVGrJv5jRmyfM%2FZoGvWV2eVCY18oBDfNk2RzVZ8PbA6MJLrj70GOqUBE7gwW4zzgc4NMN0BK6LT3g9BGPO%2BFQroyfPOzzeVjsozE55zc9AydRgZuiP7o0aFbYkOlxU9GUMAlUJ1zu7TD86s3z3c7HYeyj5AAz7bN%2FXbnYOaytkRTHhQgUJfB%2F%2BqiTGXUEAwOcRN0D33oKJDU7T6zrqyt9hCZnzpxzKYjNJ8wL9g1Zwgo1v9FDywH670%2FT2GrlsTlan4DDJXxBsh8NyKtsfN&X-Amz-Signature=b574c4f27b02847d4ef14bf0e8349c65c6242d528bbd1a0888c3e93bba93cc16&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZWLOBQ6%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIQDolpPKyfODHwOSq3%2FnqlEo3KFU62arOGV31sht1uaRWgIgeNSepgTGL4THkR3WL9vVhPW8rw8Vnn9lN%2FJX%2BylXPP8q%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDJnsJp0xgjQMUogihircA8zdBcG8CBmLGnQ7rZC%2BM8qircBoNJaq2G9fwcaRS9IvNI0TGwa86mjVVAOXOAx3eP8e916OJyEfGXLpz85quLUdszcIhl5DOga0SezAF3cY4NhCf7Hd7RFbzB%2B2xfVyGtQDNvCALAYrovxxLC49fiPF0zGOEcE4pavIhNrXBnSLbQ6BywXpm94p%2BaY53E9DmVzXcB9I1VgSyUpxDBeL%2BRiS3DCiQG1R25vgu%2Bd%2BnEZcKDY%2B%2FRFUdY1AsxZHf9CPoo%2BdFEBHUoifs0XHqfum2oeExDYYjeRqynNHlro7lSdBmy8MKnhd%2F6RtoNWhEVVDFzsowx8bh0m7JCPw62T1L%2BXatc8ZysMBhVsC4jqij078qIGb%2Bf%2BhmlT%2FfnU1IVFRRhrR%2BT5QWqewPlmA5gnwL2QT6tpPm7kYV%2BacSHBGg9zH%2Fr6sCKH%2FnKRjVkqQSgNrupYIWkQ1KUtInAE6hBFXG3HVD9rW5txesc4oAKprCRiHLBJShUURHK9KD32HwXkEqolfRH%2FJYHxDCKqBRxHVQwPV6aoD%2FA94ulO9dGBNuiy8idM6hMnHrFD9KSTLcWLseOmFcmhOGCWRCAcEoXVGrJv5jRmyfM%2FZoGvWV2eVCY18oBDfNk2RzVZ8PbA6MJLrj70GOqUBE7gwW4zzgc4NMN0BK6LT3g9BGPO%2BFQroyfPOzzeVjsozE55zc9AydRgZuiP7o0aFbYkOlxU9GUMAlUJ1zu7TD86s3z3c7HYeyj5AAz7bN%2FXbnYOaytkRTHhQgUJfB%2F%2BqiTGXUEAwOcRN0D33oKJDU7T6zrqyt9hCZnzpxzKYjNJ8wL9g1Zwgo1v9FDywH670%2FT2GrlsTlan4DDJXxBsh8NyKtsfN&X-Amz-Signature=cff1a1746ef4f78b13e10c96c810e6e93dc73b5fe54167c825293a4ace0b21f6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5PXEYLG%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T031814Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQCi8Dqm4HHahAnWzEdhpE6zDEHn0u2kBvsCq6Nq6A%2FoiAIhAPbQdywLeHDbcv44Xg8ZytBoAEZsV6Fv%2FJimR%2BBC6OM6Kv8DCFEQABoMNjM3NDIzMTgzODA1IgzcgzZ0QIjjHSpvDb0q3AM3N3QF6tyPlPMfl1W7tEU0FqgE0NGVrGSaYv6W3wY%2BwHa%2Fwgk2P9Z%2Fo6LVk555wo7lri8iz1AhQYWeOj4cyX01fhzYVa%2FA89%2Bf2P03K%2F2LSG3OKpAScxgH1veTVDrDJ3FNR%2B7GYul8AvA53fv1Sr7kbsRVvkr5TVeLW4tEuRHbWJsuveJHSvRJLlJMSedBOFeo8LR9xmf1b8XiTycaIEcq%2F9xT8yGwnFdunFYqd8s1i5knM%2FYfoy8BUBxbeXsIo2jzzZSZEJnG9tse3xMgZaJmmb2P%2B2StK%2FJhtbfNPOOID7spqH4nlZ9YulFJK0CvPaGKWs4RudyBBeeEaBoqKIwIBsXY8iZcKdOKDINzVdP2JMLro0jpva1bPHZ7ZJiigMZ96e7jvyM1gvymZ3NZaK72dRCCLKQ6nG%2FsrzQkpMsrsK5PF1pbxauTTN%2FFtOqWEOr5dwoL8fTCJB4ur6aDp1itJCRtBzNQZ1ViBiDSsG%2F50xoFLEHHZwKnFMhGeB9t6KltWUmCcxKbGhYnKTzf70Ir5jlsTN7s9frV4xCfZEGlqj15N%2FkM6vGBglL5wZH0QCulOu2s6Wgdhz4Yg1pLWNoK09vmhWy%2FxAJ04%2BO9rnmZAP1PM6hdE6clAKkZfDDV6o%2B9BjqkAaEHm52XOtx1GNGHiSOIZ8wkENlamtSF3oMLn%2BizfnYeCaOfBRTH%2F4kHDSD2Vb8D8f%2FXRQND6Zu6HsFFatgnqD5i1J3RUZgcG1hEr4UR8%2BhBLdvoCbctWCfR3noKA36bJYW1mFo92hQhOmcpqvaG928V0IpOr%2FztIHEtQR9xDpB4uxFdYM%2B7nk%2B4w2GtqrlXJVPb%2BXAMVIYp6P26ugpmZhSj7XNN&X-Amz-Signature=eef7e028199112811e2f9f3a1c883da80438f1be2f575c028edddc071dd16add&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TXB5CSQA%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T031813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIBzW5JjuXK76sSHZfwsg%2F9CIEIifbon3Kz5b7cZb9LY2AiEA6w%2BSWjrj20HoVARRK%2F8pbXle1eCIOyoockhbbK8tbSQq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDM%2F9Xj07YHGQSZqDRSrcA%2FK8uy77Yf%2FsMG1tnIal8mEYwAd3C8nphLgX0ZTZGNLsVBSK1i%2BSo2mSoJuDakXWaDSns%2BH1XOBysrbFMcdbnf%2FGnI3lqsymoC5%2BVPERJtoOWrx71FtymYsO9Qk2zSCRhrPIF0BeWn%2BdlhMG8gM1Xed4Ho6DBzCaciUUUkxKpFI1QcrIElA8b0iDpeS%2Fr3wvm6AvzHhIMTieAhs6rZMaLY0pKxMoqtMu8dR%2BPAi7R1Otn%2FqjnRDYj6oDm2c07DmZN1d1RqcnmUe1ttT1sSGo3XJ6vgh7WdvMzSzsa7O8Rqxk3jkYll%2BiRhwJfuG5hVOdnZVZJtXsm6OBMobgTFIL%2BIYJQMyT9ew1h%2BAjaDQW7q10Gc%2BTzPcCyr2QIYQUbPe7WSvmErGNkTXwrghvbegkjFwjoSSF%2BWeGVsRbvqk2dnITjnxgvniG3efLCv7WVEHDGSdAESyFAM5ea%2BNhypE3MHsqCj3JyLvJ%2FSjcSN45HDgy1cztC8XtsNsl0MPUO7PV3htLGrSznckRWCDyoGzzyndRIBxBPhSPFuwjxox%2BTTuArwRHZVzrHb0PcfRVizaQ%2F0P03SIpZ1d3d2j0SbDNT6N7J5L%2BVJVHRKsw4jTJ%2FirJrrPIrxA0z4sZmXGyMJjrj70GOqUBwkOTuzWQgzmgYTLZl0oZeanoiea4uhAHlkMEIBOwmlvOb8buPd60CgtEc7tH%2B6%2B34yfEzXCPZeRPMpvYiT9ISpZTg%2F0QkzRe06vsECywZAjca23k6%2FVi%2Bjzh0G%2BvbwIiF54pcConH9NwNC62wtOTtYk3i0PV0gcWuTSvrRSYrNtAIvbGZNnOnLKIrHWW%2BMagCSKMr47ied2OwX9TbhmRF4PQSIq%2B&X-Amz-Signature=420cae9841371108c002701b909a1e5e020f68b7b69ba9061488141e66a99042&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZWLOBQ6%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIQDolpPKyfODHwOSq3%2FnqlEo3KFU62arOGV31sht1uaRWgIgeNSepgTGL4THkR3WL9vVhPW8rw8Vnn9lN%2FJX%2BylXPP8q%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDJnsJp0xgjQMUogihircA8zdBcG8CBmLGnQ7rZC%2BM8qircBoNJaq2G9fwcaRS9IvNI0TGwa86mjVVAOXOAx3eP8e916OJyEfGXLpz85quLUdszcIhl5DOga0SezAF3cY4NhCf7Hd7RFbzB%2B2xfVyGtQDNvCALAYrovxxLC49fiPF0zGOEcE4pavIhNrXBnSLbQ6BywXpm94p%2BaY53E9DmVzXcB9I1VgSyUpxDBeL%2BRiS3DCiQG1R25vgu%2Bd%2BnEZcKDY%2B%2FRFUdY1AsxZHf9CPoo%2BdFEBHUoifs0XHqfum2oeExDYYjeRqynNHlro7lSdBmy8MKnhd%2F6RtoNWhEVVDFzsowx8bh0m7JCPw62T1L%2BXatc8ZysMBhVsC4jqij078qIGb%2Bf%2BhmlT%2FfnU1IVFRRhrR%2BT5QWqewPlmA5gnwL2QT6tpPm7kYV%2BacSHBGg9zH%2Fr6sCKH%2FnKRjVkqQSgNrupYIWkQ1KUtInAE6hBFXG3HVD9rW5txesc4oAKprCRiHLBJShUURHK9KD32HwXkEqolfRH%2FJYHxDCKqBRxHVQwPV6aoD%2FA94ulO9dGBNuiy8idM6hMnHrFD9KSTLcWLseOmFcmhOGCWRCAcEoXVGrJv5jRmyfM%2FZoGvWV2eVCY18oBDfNk2RzVZ8PbA6MJLrj70GOqUBE7gwW4zzgc4NMN0BK6LT3g9BGPO%2BFQroyfPOzzeVjsozE55zc9AydRgZuiP7o0aFbYkOlxU9GUMAlUJ1zu7TD86s3z3c7HYeyj5AAz7bN%2FXbnYOaytkRTHhQgUJfB%2F%2BqiTGXUEAwOcRN0D33oKJDU7T6zrqyt9hCZnzpxzKYjNJ8wL9g1Zwgo1v9FDywH670%2FT2GrlsTlan4DDJXxBsh8NyKtsfN&X-Amz-Signature=73112d2a3d9af8eab0b9f7b15d209bd3e81785bb743ab5f64a61d8c97391f66c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZWLOBQ6%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIQDolpPKyfODHwOSq3%2FnqlEo3KFU62arOGV31sht1uaRWgIgeNSepgTGL4THkR3WL9vVhPW8rw8Vnn9lN%2FJX%2BylXPP8q%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDJnsJp0xgjQMUogihircA8zdBcG8CBmLGnQ7rZC%2BM8qircBoNJaq2G9fwcaRS9IvNI0TGwa86mjVVAOXOAx3eP8e916OJyEfGXLpz85quLUdszcIhl5DOga0SezAF3cY4NhCf7Hd7RFbzB%2B2xfVyGtQDNvCALAYrovxxLC49fiPF0zGOEcE4pavIhNrXBnSLbQ6BywXpm94p%2BaY53E9DmVzXcB9I1VgSyUpxDBeL%2BRiS3DCiQG1R25vgu%2Bd%2BnEZcKDY%2B%2FRFUdY1AsxZHf9CPoo%2BdFEBHUoifs0XHqfum2oeExDYYjeRqynNHlro7lSdBmy8MKnhd%2F6RtoNWhEVVDFzsowx8bh0m7JCPw62T1L%2BXatc8ZysMBhVsC4jqij078qIGb%2Bf%2BhmlT%2FfnU1IVFRRhrR%2BT5QWqewPlmA5gnwL2QT6tpPm7kYV%2BacSHBGg9zH%2Fr6sCKH%2FnKRjVkqQSgNrupYIWkQ1KUtInAE6hBFXG3HVD9rW5txesc4oAKprCRiHLBJShUURHK9KD32HwXkEqolfRH%2FJYHxDCKqBRxHVQwPV6aoD%2FA94ulO9dGBNuiy8idM6hMnHrFD9KSTLcWLseOmFcmhOGCWRCAcEoXVGrJv5jRmyfM%2FZoGvWV2eVCY18oBDfNk2RzVZ8PbA6MJLrj70GOqUBE7gwW4zzgc4NMN0BK6LT3g9BGPO%2BFQroyfPOzzeVjsozE55zc9AydRgZuiP7o0aFbYkOlxU9GUMAlUJ1zu7TD86s3z3c7HYeyj5AAz7bN%2FXbnYOaytkRTHhQgUJfB%2F%2BqiTGXUEAwOcRN0D33oKJDU7T6zrqyt9hCZnzpxzKYjNJ8wL9g1Zwgo1v9FDywH670%2FT2GrlsTlan4DDJXxBsh8NyKtsfN&X-Amz-Signature=bed2f6085fd4d712e9f8a6f67ac84e3c644ad81d88c7dbebb6f567dc926c7e29&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZWLOBQ6%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIQDolpPKyfODHwOSq3%2FnqlEo3KFU62arOGV31sht1uaRWgIgeNSepgTGL4THkR3WL9vVhPW8rw8Vnn9lN%2FJX%2BylXPP8q%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDJnsJp0xgjQMUogihircA8zdBcG8CBmLGnQ7rZC%2BM8qircBoNJaq2G9fwcaRS9IvNI0TGwa86mjVVAOXOAx3eP8e916OJyEfGXLpz85quLUdszcIhl5DOga0SezAF3cY4NhCf7Hd7RFbzB%2B2xfVyGtQDNvCALAYrovxxLC49fiPF0zGOEcE4pavIhNrXBnSLbQ6BywXpm94p%2BaY53E9DmVzXcB9I1VgSyUpxDBeL%2BRiS3DCiQG1R25vgu%2Bd%2BnEZcKDY%2B%2FRFUdY1AsxZHf9CPoo%2BdFEBHUoifs0XHqfum2oeExDYYjeRqynNHlro7lSdBmy8MKnhd%2F6RtoNWhEVVDFzsowx8bh0m7JCPw62T1L%2BXatc8ZysMBhVsC4jqij078qIGb%2Bf%2BhmlT%2FfnU1IVFRRhrR%2BT5QWqewPlmA5gnwL2QT6tpPm7kYV%2BacSHBGg9zH%2Fr6sCKH%2FnKRjVkqQSgNrupYIWkQ1KUtInAE6hBFXG3HVD9rW5txesc4oAKprCRiHLBJShUURHK9KD32HwXkEqolfRH%2FJYHxDCKqBRxHVQwPV6aoD%2FA94ulO9dGBNuiy8idM6hMnHrFD9KSTLcWLseOmFcmhOGCWRCAcEoXVGrJv5jRmyfM%2FZoGvWV2eVCY18oBDfNk2RzVZ8PbA6MJLrj70GOqUBE7gwW4zzgc4NMN0BK6LT3g9BGPO%2BFQroyfPOzzeVjsozE55zc9AydRgZuiP7o0aFbYkOlxU9GUMAlUJ1zu7TD86s3z3c7HYeyj5AAz7bN%2FXbnYOaytkRTHhQgUJfB%2F%2BqiTGXUEAwOcRN0D33oKJDU7T6zrqyt9hCZnzpxzKYjNJ8wL9g1Zwgo1v9FDywH670%2FT2GrlsTlan4DDJXxBsh8NyKtsfN&X-Amz-Signature=792973bb14564167ea3ea8fa3453dcde49b346dd7ed61096f9a45273ee474ecc&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZWLOBQ6%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIQDolpPKyfODHwOSq3%2FnqlEo3KFU62arOGV31sht1uaRWgIgeNSepgTGL4THkR3WL9vVhPW8rw8Vnn9lN%2FJX%2BylXPP8q%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDJnsJp0xgjQMUogihircA8zdBcG8CBmLGnQ7rZC%2BM8qircBoNJaq2G9fwcaRS9IvNI0TGwa86mjVVAOXOAx3eP8e916OJyEfGXLpz85quLUdszcIhl5DOga0SezAF3cY4NhCf7Hd7RFbzB%2B2xfVyGtQDNvCALAYrovxxLC49fiPF0zGOEcE4pavIhNrXBnSLbQ6BywXpm94p%2BaY53E9DmVzXcB9I1VgSyUpxDBeL%2BRiS3DCiQG1R25vgu%2Bd%2BnEZcKDY%2B%2FRFUdY1AsxZHf9CPoo%2BdFEBHUoifs0XHqfum2oeExDYYjeRqynNHlro7lSdBmy8MKnhd%2F6RtoNWhEVVDFzsowx8bh0m7JCPw62T1L%2BXatc8ZysMBhVsC4jqij078qIGb%2Bf%2BhmlT%2FfnU1IVFRRhrR%2BT5QWqewPlmA5gnwL2QT6tpPm7kYV%2BacSHBGg9zH%2Fr6sCKH%2FnKRjVkqQSgNrupYIWkQ1KUtInAE6hBFXG3HVD9rW5txesc4oAKprCRiHLBJShUURHK9KD32HwXkEqolfRH%2FJYHxDCKqBRxHVQwPV6aoD%2FA94ulO9dGBNuiy8idM6hMnHrFD9KSTLcWLseOmFcmhOGCWRCAcEoXVGrJv5jRmyfM%2FZoGvWV2eVCY18oBDfNk2RzVZ8PbA6MJLrj70GOqUBE7gwW4zzgc4NMN0BK6LT3g9BGPO%2BFQroyfPOzzeVjsozE55zc9AydRgZuiP7o0aFbYkOlxU9GUMAlUJ1zu7TD86s3z3c7HYeyj5AAz7bN%2FXbnYOaytkRTHhQgUJfB%2F%2BqiTGXUEAwOcRN0D33oKJDU7T6zrqyt9hCZnzpxzKYjNJ8wL9g1Zwgo1v9FDywH670%2FT2GrlsTlan4DDJXxBsh8NyKtsfN&X-Amz-Signature=b6f3ea1426c47c3f9204d8462b288f2ac8aaa285f9d9b09dfbae36b65b6afc5e&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
