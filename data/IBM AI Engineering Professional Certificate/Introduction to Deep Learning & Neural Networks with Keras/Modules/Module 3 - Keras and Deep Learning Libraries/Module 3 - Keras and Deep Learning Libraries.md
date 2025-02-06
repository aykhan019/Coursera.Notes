

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YNVOAJ3N%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJIMEYCIQD%2FYrECIHbJrv908AzjpZNm2Yf5Z4kXI1DKHPajlU5HhwIhANcGFxYRi79eBHjUBTDeMpVqJdlkPknUS03iTQk498GoKv8DCGAQABoMNjM3NDIzMTgzODA1IgxkOSBN%2BvNTDqK5lnEq3APrOHpZau%2F2lbuncAozR2M62LHy5bdCbl4wzZlhmHejpRwN2ciWcSaykAw55cyvgxEEohbnlqpQ%2BoSDL5K70etPxnPb%2F2p9Nq6lIIydqOARKZgGrNZ9TxFehxlyldrL2j9cBxQEKFhHV1i8xG4RggF57GN7qwGxNEdHVKlm%2FpDr1IfCtdzD4j7pfSOa6jjqiR8%2Fb0knL0rM9KUrvX5UQBbg9e9pgZ6mM32tV2vyq4yDyqZuO3JKJRe9pB0msBRyLXLh%2FHGoXtS3n2eyZMMQfheQQzt8LU5DeFWurTgkidLkJIhb6QURHPw%2FATzapBLzNwof5sraHGPgHko2amA%2BAwwFJbgC2KT7H%2F635xtyYWcfcv4aBsU8KdzLuyNhq4AxgM9CsaZ6loa27y%2F8TZyD%2FAYpqclBTv3M6i8MP0FuAKCmS9jZodruNQxqJgylUO3rKOIC7hR7arVZG8Onw1vIa20sAnS23%2BorjgKI%2B6qy2Hgb5sxTBZvuWIaNFH6s%2BpT49SDcLOtr5lCnGR%2BKHmHtTRqC9KCqqLxaRYj48vf5865ymevN7aQk6SmFABlngwY%2BmHD2mszWGVqyYXACz8VxpN517RSQTHv6RCKLfS3PLAuiWoOZVIU6xuwWYvvphDC2nJO9BjqkAXBshmFSRkIMBwVGpatINkbGkR1nZDtu3z9jDeY0AYvNub0mEW%2BZZ5bIaaypZGcgqv0lsIsC%2FswI5NhqJ3S1KtR%2BmnWLxADRgB7kuJ6UkPYL3u1BqGYeQHgx3Eg4HhZ39he4DljjJBecI5Rjf4fPBnRwTSHMk3zPbQFLJEFLZukV2Cinn%2BiIVz%2Fb2gLdp5ODuDa%2BvnH5Tlz0Blk%2FZlRExypA2JFP&X-Amz-Signature=9cc87a41036972c5ff6ba98a3fff97340978059e5c4c57ba540bc6d2f639f4f1&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YNVOAJ3N%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJIMEYCIQD%2FYrECIHbJrv908AzjpZNm2Yf5Z4kXI1DKHPajlU5HhwIhANcGFxYRi79eBHjUBTDeMpVqJdlkPknUS03iTQk498GoKv8DCGAQABoMNjM3NDIzMTgzODA1IgxkOSBN%2BvNTDqK5lnEq3APrOHpZau%2F2lbuncAozR2M62LHy5bdCbl4wzZlhmHejpRwN2ciWcSaykAw55cyvgxEEohbnlqpQ%2BoSDL5K70etPxnPb%2F2p9Nq6lIIydqOARKZgGrNZ9TxFehxlyldrL2j9cBxQEKFhHV1i8xG4RggF57GN7qwGxNEdHVKlm%2FpDr1IfCtdzD4j7pfSOa6jjqiR8%2Fb0knL0rM9KUrvX5UQBbg9e9pgZ6mM32tV2vyq4yDyqZuO3JKJRe9pB0msBRyLXLh%2FHGoXtS3n2eyZMMQfheQQzt8LU5DeFWurTgkidLkJIhb6QURHPw%2FATzapBLzNwof5sraHGPgHko2amA%2BAwwFJbgC2KT7H%2F635xtyYWcfcv4aBsU8KdzLuyNhq4AxgM9CsaZ6loa27y%2F8TZyD%2FAYpqclBTv3M6i8MP0FuAKCmS9jZodruNQxqJgylUO3rKOIC7hR7arVZG8Onw1vIa20sAnS23%2BorjgKI%2B6qy2Hgb5sxTBZvuWIaNFH6s%2BpT49SDcLOtr5lCnGR%2BKHmHtTRqC9KCqqLxaRYj48vf5865ymevN7aQk6SmFABlngwY%2BmHD2mszWGVqyYXACz8VxpN517RSQTHv6RCKLfS3PLAuiWoOZVIU6xuwWYvvphDC2nJO9BjqkAXBshmFSRkIMBwVGpatINkbGkR1nZDtu3z9jDeY0AYvNub0mEW%2BZZ5bIaaypZGcgqv0lsIsC%2FswI5NhqJ3S1KtR%2BmnWLxADRgB7kuJ6UkPYL3u1BqGYeQHgx3Eg4HhZ39he4DljjJBecI5Rjf4fPBnRwTSHMk3zPbQFLJEFLZukV2Cinn%2BiIVz%2Fb2gLdp5ODuDa%2BvnH5Tlz0Blk%2FZlRExypA2JFP&X-Amz-Signature=48c17464e1cb5d24e7321348dcb45c68dc1adb0ca01e005cf851115187e9bfa8&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YNVOAJ3N%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJIMEYCIQD%2FYrECIHbJrv908AzjpZNm2Yf5Z4kXI1DKHPajlU5HhwIhANcGFxYRi79eBHjUBTDeMpVqJdlkPknUS03iTQk498GoKv8DCGAQABoMNjM3NDIzMTgzODA1IgxkOSBN%2BvNTDqK5lnEq3APrOHpZau%2F2lbuncAozR2M62LHy5bdCbl4wzZlhmHejpRwN2ciWcSaykAw55cyvgxEEohbnlqpQ%2BoSDL5K70etPxnPb%2F2p9Nq6lIIydqOARKZgGrNZ9TxFehxlyldrL2j9cBxQEKFhHV1i8xG4RggF57GN7qwGxNEdHVKlm%2FpDr1IfCtdzD4j7pfSOa6jjqiR8%2Fb0knL0rM9KUrvX5UQBbg9e9pgZ6mM32tV2vyq4yDyqZuO3JKJRe9pB0msBRyLXLh%2FHGoXtS3n2eyZMMQfheQQzt8LU5DeFWurTgkidLkJIhb6QURHPw%2FATzapBLzNwof5sraHGPgHko2amA%2BAwwFJbgC2KT7H%2F635xtyYWcfcv4aBsU8KdzLuyNhq4AxgM9CsaZ6loa27y%2F8TZyD%2FAYpqclBTv3M6i8MP0FuAKCmS9jZodruNQxqJgylUO3rKOIC7hR7arVZG8Onw1vIa20sAnS23%2BorjgKI%2B6qy2Hgb5sxTBZvuWIaNFH6s%2BpT49SDcLOtr5lCnGR%2BKHmHtTRqC9KCqqLxaRYj48vf5865ymevN7aQk6SmFABlngwY%2BmHD2mszWGVqyYXACz8VxpN517RSQTHv6RCKLfS3PLAuiWoOZVIU6xuwWYvvphDC2nJO9BjqkAXBshmFSRkIMBwVGpatINkbGkR1nZDtu3z9jDeY0AYvNub0mEW%2BZZ5bIaaypZGcgqv0lsIsC%2FswI5NhqJ3S1KtR%2BmnWLxADRgB7kuJ6UkPYL3u1BqGYeQHgx3Eg4HhZ39he4DljjJBecI5Rjf4fPBnRwTSHMk3zPbQFLJEFLZukV2Cinn%2BiIVz%2Fb2gLdp5ODuDa%2BvnH5Tlz0Blk%2FZlRExypA2JFP&X-Amz-Signature=ec5984c914b95afcbfc3f48b8243b0c3bf717c9874996657f15e81b7870034f9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666FBVU6SB%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCICAbNeQ1lBd62agyOGONAQq3uPBkKWR5UeRirNqiouSZAiEAs%2F1Hhq9xwG4hv%2BOlmVtk3%2FMS7exG0t%2FtixwWfdVK6l0q%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDIE%2FuSUO2PwX3TyWVircAx9RmsG2fAjQW0dZgqiqb8mz6YSO46JqLROS3gkRextPMdN0QodKz6FDU9dVG4A2dUlN%2BM4Y5zXA1OEFfpqw81CFtEgl11oeisNI6PmhwLeIrVWrlVTPU3q5CIVAP1WiZXpvea1GdPc%2FCVbBolbR8%2FFmwnUzVNBcV1lXwjg5MiWxxTjyEYXf%2Fq5whQGEVN2XAQa1cFThreux969ReB%2Fn%2FCX7DWSQoFt1gUngEGzPNdZLBTfHmsiE0m7OkCfUlSbF0XVwI57uAITQBgcn4JZA6y6nR%2FSBDChKdntYm0aJ1Cm8SFD3rNq4yWn4Ls%2B2q4nvoRagoA1MHbblg5YtlsvXWjjArkQYiWPuaLyAJSYCr3%2B%2BIkL%2F3ElbLwT5aG9mwAFjMN9fwh%2FVNnDGrSIP9neZNaFQQ6MJyi6FMeWloYJD10Bj7oTYOK6ftqziARg9dAuiYQPWp5Z3yMvq1kbHxnehFB7W4qE0DadeFzTQaap6JvqWWWR%2B5sQfu%2F9pI81%2F3XdXqHi5daU8IoOh%2B2RCVvHPZL9aGmaEDKddM9%2BygApspO0B0%2Bpt1ui5VvzUijTe1NeT4bWP8Z567sTQAxHhTSKbvhlcPJNTGrVoUeScbQfDsVkqnvDi%2Fb5QFijzX7gzMKyck70GOqUBkU4FviOBRPmWu5tUpH9hVM0Eqm2iAkLXPLGtbiWX9FrzaCfVRMu75aN4JsPWdxjbtFgtms7CV9idIJzAmw0hEM2CzM3BFcnf%2FQojOk01xtBkmgiZXb%2BuWG5ZxcF3qUGe4BAN95we6KsOeCfETKR9pOdkiqxu0NFbZa0gXfKca%2Fk12qZokGtFf9UJ1%2Bvusq8DyWTW76cpexEux%2BA3jfWL5J4%2BT5Cs&X-Amz-Signature=d9df4c3ed0ba05fc7238c2cd6147a035940d32db5e7bd9889ffe46ddca2472ec&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RSRU3CJB%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJIMEYCIQCJ1JsVc2tEFvesfXaovsPInpN8FzMLRdCwS28qbsI7%2BwIhAMGE4JrCMSEbUShsQiJGukK7SyNHrxImyF9xcbel3QAQKv8DCGAQABoMNjM3NDIzMTgzODA1IgzFLJPwPNcMpz4GR2Eq3AMqPBkTp5HmU%2BjX6yLloldDwa5YQeUcLgR77IZTFDz5F8GtLxotT91b9siFOp%2BN6MBKqCNvGXai3ONdaofaRgjPkXmG18TY6PKNZTfvgV%2F8LAk%2B7ZfHirtcSSe%2BvyTXq%2FAXB%2B3Wdt6NF9mjXyVNXrYw%2BuDXunu56llVwZ8qnrZ6xC%2B91LFUMu%2Fg84w5jNLnkUhb4IgLi0GCQMP94e8AinlLb82i%2B2T3BsItAvLFtXFqm%2FsjvVwNVDuUIWkwRatPxI6ZWraGaAtKU%2FHWKVJnkXqGzMVeWiwKWY%2BXa5HyyE1KTJSIouICuZJe3GP%2BamtBw9HhvDOsVdur7z%2FFCp%2BkLompERzN8eGkU%2BevGM%2BNFcPJ7ceDGlGAjwP0b5fVNQKH5uEK0w135Spml818RD9KZ4fYdOlAz%2FCxiQR8vL9bCBZUWM1yzdj3v%2B2EaWmzKdIGHzhs4WE9icykntBIfyrylmPRcCo%2F3KgWkh%2FrhNdcgxdf3D824uG20jWRDQG0MKphcoYTahrfxPt5hHRFNk26jMgRqfOwytxo8BQDL6u0zIztV3pBbm8TYyzbBlcvwIVwXxVUCXXU4DWHfG85WSCy4DO%2FTgWw7y%2FP99LzJJmHgGCJqbCIMu%2F%2BekfF0ovcdTDEnJO9BjqkAf%2Fz1ktf2lCUobWVlpZtj02hNzUg25OTAT%2BLpcUXGKMbk62zS%2FfnQLyZ5%2FzodCyO0FqaAdbJD8ZwlxfI6a0Av5fS7AD0tsV22X8fx%2BFU0eWG55R2k%2BS9Myct%2BLeoTCsf3cC%2FVr7dXRfbLm4H7piS4c9KjMHSeOylBdmKM0FdI22QFZTcD9TBRDar4xMOiOAIhprBOd0XBmI%2FKZvDJQ54rudS3Epc&X-Amz-Signature=6653750ace504bb61006e79bde4101bb26026287c7d537da6dd080d3c43290b0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YNVOAJ3N%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJIMEYCIQD%2FYrECIHbJrv908AzjpZNm2Yf5Z4kXI1DKHPajlU5HhwIhANcGFxYRi79eBHjUBTDeMpVqJdlkPknUS03iTQk498GoKv8DCGAQABoMNjM3NDIzMTgzODA1IgxkOSBN%2BvNTDqK5lnEq3APrOHpZau%2F2lbuncAozR2M62LHy5bdCbl4wzZlhmHejpRwN2ciWcSaykAw55cyvgxEEohbnlqpQ%2BoSDL5K70etPxnPb%2F2p9Nq6lIIydqOARKZgGrNZ9TxFehxlyldrL2j9cBxQEKFhHV1i8xG4RggF57GN7qwGxNEdHVKlm%2FpDr1IfCtdzD4j7pfSOa6jjqiR8%2Fb0knL0rM9KUrvX5UQBbg9e9pgZ6mM32tV2vyq4yDyqZuO3JKJRe9pB0msBRyLXLh%2FHGoXtS3n2eyZMMQfheQQzt8LU5DeFWurTgkidLkJIhb6QURHPw%2FATzapBLzNwof5sraHGPgHko2amA%2BAwwFJbgC2KT7H%2F635xtyYWcfcv4aBsU8KdzLuyNhq4AxgM9CsaZ6loa27y%2F8TZyD%2FAYpqclBTv3M6i8MP0FuAKCmS9jZodruNQxqJgylUO3rKOIC7hR7arVZG8Onw1vIa20sAnS23%2BorjgKI%2B6qy2Hgb5sxTBZvuWIaNFH6s%2BpT49SDcLOtr5lCnGR%2BKHmHtTRqC9KCqqLxaRYj48vf5865ymevN7aQk6SmFABlngwY%2BmHD2mszWGVqyYXACz8VxpN517RSQTHv6RCKLfS3PLAuiWoOZVIU6xuwWYvvphDC2nJO9BjqkAXBshmFSRkIMBwVGpatINkbGkR1nZDtu3z9jDeY0AYvNub0mEW%2BZZ5bIaaypZGcgqv0lsIsC%2FswI5NhqJ3S1KtR%2BmnWLxADRgB7kuJ6UkPYL3u1BqGYeQHgx3Eg4HhZ39he4DljjJBecI5Rjf4fPBnRwTSHMk3zPbQFLJEFLZukV2Cinn%2BiIVz%2Fb2gLdp5ODuDa%2BvnH5Tlz0Blk%2FZlRExypA2JFP&X-Amz-Signature=4da97e1ac17d87af4dc6dd8232055696f90879587992dc9409035b4a105d987e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YNVOAJ3N%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJIMEYCIQD%2FYrECIHbJrv908AzjpZNm2Yf5Z4kXI1DKHPajlU5HhwIhANcGFxYRi79eBHjUBTDeMpVqJdlkPknUS03iTQk498GoKv8DCGAQABoMNjM3NDIzMTgzODA1IgxkOSBN%2BvNTDqK5lnEq3APrOHpZau%2F2lbuncAozR2M62LHy5bdCbl4wzZlhmHejpRwN2ciWcSaykAw55cyvgxEEohbnlqpQ%2BoSDL5K70etPxnPb%2F2p9Nq6lIIydqOARKZgGrNZ9TxFehxlyldrL2j9cBxQEKFhHV1i8xG4RggF57GN7qwGxNEdHVKlm%2FpDr1IfCtdzD4j7pfSOa6jjqiR8%2Fb0knL0rM9KUrvX5UQBbg9e9pgZ6mM32tV2vyq4yDyqZuO3JKJRe9pB0msBRyLXLh%2FHGoXtS3n2eyZMMQfheQQzt8LU5DeFWurTgkidLkJIhb6QURHPw%2FATzapBLzNwof5sraHGPgHko2amA%2BAwwFJbgC2KT7H%2F635xtyYWcfcv4aBsU8KdzLuyNhq4AxgM9CsaZ6loa27y%2F8TZyD%2FAYpqclBTv3M6i8MP0FuAKCmS9jZodruNQxqJgylUO3rKOIC7hR7arVZG8Onw1vIa20sAnS23%2BorjgKI%2B6qy2Hgb5sxTBZvuWIaNFH6s%2BpT49SDcLOtr5lCnGR%2BKHmHtTRqC9KCqqLxaRYj48vf5865ymevN7aQk6SmFABlngwY%2BmHD2mszWGVqyYXACz8VxpN517RSQTHv6RCKLfS3PLAuiWoOZVIU6xuwWYvvphDC2nJO9BjqkAXBshmFSRkIMBwVGpatINkbGkR1nZDtu3z9jDeY0AYvNub0mEW%2BZZ5bIaaypZGcgqv0lsIsC%2FswI5NhqJ3S1KtR%2BmnWLxADRgB7kuJ6UkPYL3u1BqGYeQHgx3Eg4HhZ39he4DljjJBecI5Rjf4fPBnRwTSHMk3zPbQFLJEFLZukV2Cinn%2BiIVz%2Fb2gLdp5ODuDa%2BvnH5Tlz0Blk%2FZlRExypA2JFP&X-Amz-Signature=afa39d778d1bb320a3f91799ccd5496e770dcdc8cf1751b5abf8baabf7d3e532&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YNVOAJ3N%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJIMEYCIQD%2FYrECIHbJrv908AzjpZNm2Yf5Z4kXI1DKHPajlU5HhwIhANcGFxYRi79eBHjUBTDeMpVqJdlkPknUS03iTQk498GoKv8DCGAQABoMNjM3NDIzMTgzODA1IgxkOSBN%2BvNTDqK5lnEq3APrOHpZau%2F2lbuncAozR2M62LHy5bdCbl4wzZlhmHejpRwN2ciWcSaykAw55cyvgxEEohbnlqpQ%2BoSDL5K70etPxnPb%2F2p9Nq6lIIydqOARKZgGrNZ9TxFehxlyldrL2j9cBxQEKFhHV1i8xG4RggF57GN7qwGxNEdHVKlm%2FpDr1IfCtdzD4j7pfSOa6jjqiR8%2Fb0knL0rM9KUrvX5UQBbg9e9pgZ6mM32tV2vyq4yDyqZuO3JKJRe9pB0msBRyLXLh%2FHGoXtS3n2eyZMMQfheQQzt8LU5DeFWurTgkidLkJIhb6QURHPw%2FATzapBLzNwof5sraHGPgHko2amA%2BAwwFJbgC2KT7H%2F635xtyYWcfcv4aBsU8KdzLuyNhq4AxgM9CsaZ6loa27y%2F8TZyD%2FAYpqclBTv3M6i8MP0FuAKCmS9jZodruNQxqJgylUO3rKOIC7hR7arVZG8Onw1vIa20sAnS23%2BorjgKI%2B6qy2Hgb5sxTBZvuWIaNFH6s%2BpT49SDcLOtr5lCnGR%2BKHmHtTRqC9KCqqLxaRYj48vf5865ymevN7aQk6SmFABlngwY%2BmHD2mszWGVqyYXACz8VxpN517RSQTHv6RCKLfS3PLAuiWoOZVIU6xuwWYvvphDC2nJO9BjqkAXBshmFSRkIMBwVGpatINkbGkR1nZDtu3z9jDeY0AYvNub0mEW%2BZZ5bIaaypZGcgqv0lsIsC%2FswI5NhqJ3S1KtR%2BmnWLxADRgB7kuJ6UkPYL3u1BqGYeQHgx3Eg4HhZ39he4DljjJBecI5Rjf4fPBnRwTSHMk3zPbQFLJEFLZukV2Cinn%2BiIVz%2Fb2gLdp5ODuDa%2BvnH5Tlz0Blk%2FZlRExypA2JFP&X-Amz-Signature=1fc33978397d7ca784c46a636f59f846161755bd60c8b57022e4c08f130307d3&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YNVOAJ3N%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJIMEYCIQD%2FYrECIHbJrv908AzjpZNm2Yf5Z4kXI1DKHPajlU5HhwIhANcGFxYRi79eBHjUBTDeMpVqJdlkPknUS03iTQk498GoKv8DCGAQABoMNjM3NDIzMTgzODA1IgxkOSBN%2BvNTDqK5lnEq3APrOHpZau%2F2lbuncAozR2M62LHy5bdCbl4wzZlhmHejpRwN2ciWcSaykAw55cyvgxEEohbnlqpQ%2BoSDL5K70etPxnPb%2F2p9Nq6lIIydqOARKZgGrNZ9TxFehxlyldrL2j9cBxQEKFhHV1i8xG4RggF57GN7qwGxNEdHVKlm%2FpDr1IfCtdzD4j7pfSOa6jjqiR8%2Fb0knL0rM9KUrvX5UQBbg9e9pgZ6mM32tV2vyq4yDyqZuO3JKJRe9pB0msBRyLXLh%2FHGoXtS3n2eyZMMQfheQQzt8LU5DeFWurTgkidLkJIhb6QURHPw%2FATzapBLzNwof5sraHGPgHko2amA%2BAwwFJbgC2KT7H%2F635xtyYWcfcv4aBsU8KdzLuyNhq4AxgM9CsaZ6loa27y%2F8TZyD%2FAYpqclBTv3M6i8MP0FuAKCmS9jZodruNQxqJgylUO3rKOIC7hR7arVZG8Onw1vIa20sAnS23%2BorjgKI%2B6qy2Hgb5sxTBZvuWIaNFH6s%2BpT49SDcLOtr5lCnGR%2BKHmHtTRqC9KCqqLxaRYj48vf5865ymevN7aQk6SmFABlngwY%2BmHD2mszWGVqyYXACz8VxpN517RSQTHv6RCKLfS3PLAuiWoOZVIU6xuwWYvvphDC2nJO9BjqkAXBshmFSRkIMBwVGpatINkbGkR1nZDtu3z9jDeY0AYvNub0mEW%2BZZ5bIaaypZGcgqv0lsIsC%2FswI5NhqJ3S1KtR%2BmnWLxADRgB7kuJ6UkPYL3u1BqGYeQHgx3Eg4HhZ39he4DljjJBecI5Rjf4fPBnRwTSHMk3zPbQFLJEFLZukV2Cinn%2BiIVz%2Fb2gLdp5ODuDa%2BvnH5Tlz0Blk%2FZlRExypA2JFP&X-Amz-Signature=95e758726cc8f579ad3eb8ab4529ebeaa2f0c4e1f4ca01e995de21908b027d88&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
