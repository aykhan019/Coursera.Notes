

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OZZZJGU%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081912Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJIMEYCIQCZoPe1UTYOobjgMArAezbrSnIuBxRioMJZi1vqgjZ6%2FwIhAMmnJ5g2oWXNod5x%2B0207%2BDbHo7TTHdXy8vb3xnPlcT9Kv8DCCkQABoMNjM3NDIzMTgzODA1IgyN4pG%2FV%2FjmS9tx%2Fm8q3AMa3HkUiM6qqGRIO2LMezAvioLMVolmh5bfU13RvDDKYmKeto%2FrOmleR%2BDiDbR7EcpbcWYkN07r%2BGi8YRQRi4t3pYjxoR6U1oy8DlliTf6WtdvI%2BPXpfJTJ6aCL2cxnWpFNlIxNMtZfq1YKDQgYiI1ASs1P0BYzsgCBCr6%2BzilXeN%2BDDDZTS3SiuzjekphJNH%2FdXVc%2Fbj%2FtSDpPHDN%2FSayFjhDHXrgjYWOXxOHAru10vKpfbe9gScwWZ5eoh%2BYg3BXOa6QKhauyq16UieUCW2hHOqJzCYRjF7TkbUEYPeS%2B03D8DTsJRpLB6PTzT7M6ZgaaCLoKO1dbaTEt8odrzuZR017LUjlzLrJliItv8Rx8jezJrSv%2BsQhDMDc7TUZh8Pw65C0gttrK%2BdfIG2s3x9jm4jTzZeeAAkgrqLlU2zCnrrIN%2FZOCfcLyIcNkbjlIDJrc3XRxBmUsfIhnw3zQvtXdmcDQI9pwlKV8VicpTy0a83KDFOQf2ZmrP1Zfz4nwBUIE9tQ43RQkavImwApNZSzjjtJYWA9FM0TRHdfIExQcGzgJplutqjrDflTewLoIxrayeQT4xKTxQLQdl%2FnefFyolZC8sjTzjXtLDypwGldblIsBRQUO0poPYFUo4TD4kYe9BjqkAcergc0AM6MGDfbdk8eTYdSkIta%2F7ZdjybqaIFzSMkcUtLzHUztgx8ftaYW2hRVwCLz7XVAaIEAZBZ1%2BX%2BAVtrQMaXyTzJYdHrGN%2FU3s0lofkZ7cFUAxb1p3icwLpyNsoXcMoDLKaRf81szOV92wAxjP6maeg9Ef654kuQgDN33Dik0BTsap%2F8SXVOHuDb5BEyay2aSWikmBKLB8eXYmuebm2qqp&X-Amz-Signature=887e7baa7d453992e04128866f0eaaec75d06bd0600500518524d76c5d542545&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OZZZJGU%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081912Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJIMEYCIQCZoPe1UTYOobjgMArAezbrSnIuBxRioMJZi1vqgjZ6%2FwIhAMmnJ5g2oWXNod5x%2B0207%2BDbHo7TTHdXy8vb3xnPlcT9Kv8DCCkQABoMNjM3NDIzMTgzODA1IgyN4pG%2FV%2FjmS9tx%2Fm8q3AMa3HkUiM6qqGRIO2LMezAvioLMVolmh5bfU13RvDDKYmKeto%2FrOmleR%2BDiDbR7EcpbcWYkN07r%2BGi8YRQRi4t3pYjxoR6U1oy8DlliTf6WtdvI%2BPXpfJTJ6aCL2cxnWpFNlIxNMtZfq1YKDQgYiI1ASs1P0BYzsgCBCr6%2BzilXeN%2BDDDZTS3SiuzjekphJNH%2FdXVc%2Fbj%2FtSDpPHDN%2FSayFjhDHXrgjYWOXxOHAru10vKpfbe9gScwWZ5eoh%2BYg3BXOa6QKhauyq16UieUCW2hHOqJzCYRjF7TkbUEYPeS%2B03D8DTsJRpLB6PTzT7M6ZgaaCLoKO1dbaTEt8odrzuZR017LUjlzLrJliItv8Rx8jezJrSv%2BsQhDMDc7TUZh8Pw65C0gttrK%2BdfIG2s3x9jm4jTzZeeAAkgrqLlU2zCnrrIN%2FZOCfcLyIcNkbjlIDJrc3XRxBmUsfIhnw3zQvtXdmcDQI9pwlKV8VicpTy0a83KDFOQf2ZmrP1Zfz4nwBUIE9tQ43RQkavImwApNZSzjjtJYWA9FM0TRHdfIExQcGzgJplutqjrDflTewLoIxrayeQT4xKTxQLQdl%2FnefFyolZC8sjTzjXtLDypwGldblIsBRQUO0poPYFUo4TD4kYe9BjqkAcergc0AM6MGDfbdk8eTYdSkIta%2F7ZdjybqaIFzSMkcUtLzHUztgx8ftaYW2hRVwCLz7XVAaIEAZBZ1%2BX%2BAVtrQMaXyTzJYdHrGN%2FU3s0lofkZ7cFUAxb1p3icwLpyNsoXcMoDLKaRf81szOV92wAxjP6maeg9Ef654kuQgDN33Dik0BTsap%2F8SXVOHuDb5BEyay2aSWikmBKLB8eXYmuebm2qqp&X-Amz-Signature=c6c216303c7d3a5c7245f5d95fcc752c98a2e92989866303deae28a4525263a3&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OZZZJGU%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081912Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJIMEYCIQCZoPe1UTYOobjgMArAezbrSnIuBxRioMJZi1vqgjZ6%2FwIhAMmnJ5g2oWXNod5x%2B0207%2BDbHo7TTHdXy8vb3xnPlcT9Kv8DCCkQABoMNjM3NDIzMTgzODA1IgyN4pG%2FV%2FjmS9tx%2Fm8q3AMa3HkUiM6qqGRIO2LMezAvioLMVolmh5bfU13RvDDKYmKeto%2FrOmleR%2BDiDbR7EcpbcWYkN07r%2BGi8YRQRi4t3pYjxoR6U1oy8DlliTf6WtdvI%2BPXpfJTJ6aCL2cxnWpFNlIxNMtZfq1YKDQgYiI1ASs1P0BYzsgCBCr6%2BzilXeN%2BDDDZTS3SiuzjekphJNH%2FdXVc%2Fbj%2FtSDpPHDN%2FSayFjhDHXrgjYWOXxOHAru10vKpfbe9gScwWZ5eoh%2BYg3BXOa6QKhauyq16UieUCW2hHOqJzCYRjF7TkbUEYPeS%2B03D8DTsJRpLB6PTzT7M6ZgaaCLoKO1dbaTEt8odrzuZR017LUjlzLrJliItv8Rx8jezJrSv%2BsQhDMDc7TUZh8Pw65C0gttrK%2BdfIG2s3x9jm4jTzZeeAAkgrqLlU2zCnrrIN%2FZOCfcLyIcNkbjlIDJrc3XRxBmUsfIhnw3zQvtXdmcDQI9pwlKV8VicpTy0a83KDFOQf2ZmrP1Zfz4nwBUIE9tQ43RQkavImwApNZSzjjtJYWA9FM0TRHdfIExQcGzgJplutqjrDflTewLoIxrayeQT4xKTxQLQdl%2FnefFyolZC8sjTzjXtLDypwGldblIsBRQUO0poPYFUo4TD4kYe9BjqkAcergc0AM6MGDfbdk8eTYdSkIta%2F7ZdjybqaIFzSMkcUtLzHUztgx8ftaYW2hRVwCLz7XVAaIEAZBZ1%2BX%2BAVtrQMaXyTzJYdHrGN%2FU3s0lofkZ7cFUAxb1p3icwLpyNsoXcMoDLKaRf81szOV92wAxjP6maeg9Ef654kuQgDN33Dik0BTsap%2F8SXVOHuDb5BEyay2aSWikmBKLB8eXYmuebm2qqp&X-Amz-Signature=c1744e1cab7d5d6b6d02a9f24cfa3fb19726ab8f12ef24e15c3fca6214abea0f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KAYUBBV%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJHMEUCIHJC4WZmJZClV2UkV5CFXchiu%2Bprf2zL1mQsLuzVpKjzAiEA4lDj%2FApNS0%2FFk84%2F8DCsd8i0edzUY6Y%2BFQDgWIZ105Yq%2FwMIKRAAGgw2Mzc0MjMxODM4MDUiDAxJnzOqbuvtAuY2circA0WMQfJ0Qk%2BQAPLrMV3uM2gFZMrM705v9ylYa1tczyvXP8ix5ZSejN3e856ii5Zj4BHBcsX%2BUuXC998ygnwnHI7EUzGK5c76hsMpUcj5M03Ed%2BCPMU6d14fwg4ikW9wjIPLTJqdKLdTjMKQ7pXuKbypBuHRywEz7chB89Bkn1cGV6w1xFFZ8AntKQtnYC1T%2F1UrheYbdtS811oijZ0o7enT%2FXtWeiaXKCBwloOJLsIE20zhiUgIQfON01ZadbnHjRsj3vyDseJM92%2F7pyjqs5xSYos4txM9VTLIiqUDonteyKWzsU%2BmsqYg7XLeM2d3YZPJDcta6DUy1p9dcMZTFAetrC6c7MkdUjzWvWFX3mo4Sb7m3bXug3ygYiqXQmt2iuppk9P0EDAMX%2Fhsta0pWjVE8CT2bcaEEsY5w8YVPk4iJ%2BEGDfedLtweDLeNjqtIDVS5cFNvI5l4xaQAB2tCsev3Qx3o9Pj9GoElSVXzfFJCJj%2BhJZ4yfNmySfUvyPnUxQOlczvMw4sflwXnsRH05Aauls5N6EAfGkby5ms783Hn71ZnHABTNn86yLlinerJ2GM19MGdxX4S0d2TtjhUBn%2FyXxpZtLK4LAm62GtQjaoLeRfPS9yXVVJBJJH5mMJ%2BRh70GOqUBEJxAMPDDNz2GLPCXeW%2BrUUNvIyepIFn%2BjX%2BKi9adQDkUyNjrTFDDTD7P6xwYSPDaqdq%2BiZcHv9wF6gxbZyQPZhf%2Bgu4xkJmEdFkuCzlQjejXhJQT9uFw8mxSGDWFOJ89Afq%2Fs8iSW5hnfZ8teVjfTQSyqYyouVhxOiAGb8d4YmtvRaKFFDA4YwltUEUJHLNZ92F9r1dWlHBIqrTCX5zD4ABKBdP0&X-Amz-Signature=3d8b03d6e52e24687d5701ba7fad176c80af17a4efa39c4bd6854dc01b1d2b22&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYTZWHLN%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJIMEYCIQDOgEVaUfVeQl%2BNvTQonUP1ZDSi%2BgIBVAoUx0J8Yi5GYQIhAKGUO5VC4KuhXqUzf%2BTFDntDghEAdLGg4EsX%2Fvgb44lvKv8DCCkQABoMNjM3NDIzMTgzODA1IgwNA8mZqO%2BAvfSgzfIq3AOhgDqdaYku0rpRd7J0h%2FsK8IVBY%2Fx%2BFif8uV9sBT1k6abOPB24Lbh%2BA40Scfpxt2JYPc3USjpPrqmCclPrAZ9vK1D0kwB8utPtXCUsrLy3WbzWOewwWXyFUWgWDPnST2OjQvYa02CxrtTGWI7NIg8tgwo7yI51qSlxFenmGcnwmgtoKqvD8OBgbHbDtBxDvdOA3UpKw%2FeLteT1QzsUg6IBk65pJUJCpJw6eR7MkADX5T3gz7trsrPBRj39XNOPyJin0DmxUy15wmSD18%2BEDRCdaSS6dgT98eaveo%2F4H%2B4njMiA5mzh%2FlzIazhJdrtBq0%2BRKHZcvwge%2BMYvpASZYSvmUyfoLD0YnYQPQ9ILiRamPkEceNYZffhqoWZfZSKOqdu6%2FpT%2B0jbB3sh572ZHng4zd61IPOP0Hjo%2FY4QUdW5wRRb6MTbV1MgPD%2FkGz%2FQ3bH62nmNVzTdtupVfthCZk7zvx0Gsx7YLAK0sVyxYHWBRg8t8rdFuIgMfRrZtkbKI0wOCc0uyGYiwlue5m1go4kPME6i60gV3HCRQ6uYM9Ri%2FpjCxBHnAF6Rf9Kxq07nPNUbiCq6GZusLyFdPnP8cMCJG4y7jKqVQXevnQbYZ43%2BMmT9%2BwUWCJldeIHunETDAkYe9BjqkAfWBBCtZEnbeJq5arIRDdedYlI5siOcEl2ayqxKN7xDEXnJjjn0mfBDyP1tb5VwUzBegrlW7jNIk9wBokqkCh3pMzBvtfE0XMvK5YR46Hh%2FTaihoC3lCTgtiMLyZeMpC1mhrlf084hJnmsbVyeS6hxeHjH1GocR7YcnqOJdyCDlTGasbCupO3qDyG3E7GGFNJHUeLe6uyuP1IdmxVt7OUhQ5cwVD&X-Amz-Signature=23dca374508bad2793bf8bb97d347999e8666f7e03af12426c29391c037655da&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OZZZJGU%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081912Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJIMEYCIQCZoPe1UTYOobjgMArAezbrSnIuBxRioMJZi1vqgjZ6%2FwIhAMmnJ5g2oWXNod5x%2B0207%2BDbHo7TTHdXy8vb3xnPlcT9Kv8DCCkQABoMNjM3NDIzMTgzODA1IgyN4pG%2FV%2FjmS9tx%2Fm8q3AMa3HkUiM6qqGRIO2LMezAvioLMVolmh5bfU13RvDDKYmKeto%2FrOmleR%2BDiDbR7EcpbcWYkN07r%2BGi8YRQRi4t3pYjxoR6U1oy8DlliTf6WtdvI%2BPXpfJTJ6aCL2cxnWpFNlIxNMtZfq1YKDQgYiI1ASs1P0BYzsgCBCr6%2BzilXeN%2BDDDZTS3SiuzjekphJNH%2FdXVc%2Fbj%2FtSDpPHDN%2FSayFjhDHXrgjYWOXxOHAru10vKpfbe9gScwWZ5eoh%2BYg3BXOa6QKhauyq16UieUCW2hHOqJzCYRjF7TkbUEYPeS%2B03D8DTsJRpLB6PTzT7M6ZgaaCLoKO1dbaTEt8odrzuZR017LUjlzLrJliItv8Rx8jezJrSv%2BsQhDMDc7TUZh8Pw65C0gttrK%2BdfIG2s3x9jm4jTzZeeAAkgrqLlU2zCnrrIN%2FZOCfcLyIcNkbjlIDJrc3XRxBmUsfIhnw3zQvtXdmcDQI9pwlKV8VicpTy0a83KDFOQf2ZmrP1Zfz4nwBUIE9tQ43RQkavImwApNZSzjjtJYWA9FM0TRHdfIExQcGzgJplutqjrDflTewLoIxrayeQT4xKTxQLQdl%2FnefFyolZC8sjTzjXtLDypwGldblIsBRQUO0poPYFUo4TD4kYe9BjqkAcergc0AM6MGDfbdk8eTYdSkIta%2F7ZdjybqaIFzSMkcUtLzHUztgx8ftaYW2hRVwCLz7XVAaIEAZBZ1%2BX%2BAVtrQMaXyTzJYdHrGN%2FU3s0lofkZ7cFUAxb1p3icwLpyNsoXcMoDLKaRf81szOV92wAxjP6maeg9Ef654kuQgDN33Dik0BTsap%2F8SXVOHuDb5BEyay2aSWikmBKLB8eXYmuebm2qqp&X-Amz-Signature=49f36942f014ffb3719ccb7f0438d0a5713e581d10679b70cff4868a0f78c27d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OZZZJGU%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081912Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJIMEYCIQCZoPe1UTYOobjgMArAezbrSnIuBxRioMJZi1vqgjZ6%2FwIhAMmnJ5g2oWXNod5x%2B0207%2BDbHo7TTHdXy8vb3xnPlcT9Kv8DCCkQABoMNjM3NDIzMTgzODA1IgyN4pG%2FV%2FjmS9tx%2Fm8q3AMa3HkUiM6qqGRIO2LMezAvioLMVolmh5bfU13RvDDKYmKeto%2FrOmleR%2BDiDbR7EcpbcWYkN07r%2BGi8YRQRi4t3pYjxoR6U1oy8DlliTf6WtdvI%2BPXpfJTJ6aCL2cxnWpFNlIxNMtZfq1YKDQgYiI1ASs1P0BYzsgCBCr6%2BzilXeN%2BDDDZTS3SiuzjekphJNH%2FdXVc%2Fbj%2FtSDpPHDN%2FSayFjhDHXrgjYWOXxOHAru10vKpfbe9gScwWZ5eoh%2BYg3BXOa6QKhauyq16UieUCW2hHOqJzCYRjF7TkbUEYPeS%2B03D8DTsJRpLB6PTzT7M6ZgaaCLoKO1dbaTEt8odrzuZR017LUjlzLrJliItv8Rx8jezJrSv%2BsQhDMDc7TUZh8Pw65C0gttrK%2BdfIG2s3x9jm4jTzZeeAAkgrqLlU2zCnrrIN%2FZOCfcLyIcNkbjlIDJrc3XRxBmUsfIhnw3zQvtXdmcDQI9pwlKV8VicpTy0a83KDFOQf2ZmrP1Zfz4nwBUIE9tQ43RQkavImwApNZSzjjtJYWA9FM0TRHdfIExQcGzgJplutqjrDflTewLoIxrayeQT4xKTxQLQdl%2FnefFyolZC8sjTzjXtLDypwGldblIsBRQUO0poPYFUo4TD4kYe9BjqkAcergc0AM6MGDfbdk8eTYdSkIta%2F7ZdjybqaIFzSMkcUtLzHUztgx8ftaYW2hRVwCLz7XVAaIEAZBZ1%2BX%2BAVtrQMaXyTzJYdHrGN%2FU3s0lofkZ7cFUAxb1p3icwLpyNsoXcMoDLKaRf81szOV92wAxjP6maeg9Ef654kuQgDN33Dik0BTsap%2F8SXVOHuDb5BEyay2aSWikmBKLB8eXYmuebm2qqp&X-Amz-Signature=0d34a533407e2a80f2ae1616bd156a8b5e706406aa034d301c2ff8a0deb4b12c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OZZZJGU%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081912Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJIMEYCIQCZoPe1UTYOobjgMArAezbrSnIuBxRioMJZi1vqgjZ6%2FwIhAMmnJ5g2oWXNod5x%2B0207%2BDbHo7TTHdXy8vb3xnPlcT9Kv8DCCkQABoMNjM3NDIzMTgzODA1IgyN4pG%2FV%2FjmS9tx%2Fm8q3AMa3HkUiM6qqGRIO2LMezAvioLMVolmh5bfU13RvDDKYmKeto%2FrOmleR%2BDiDbR7EcpbcWYkN07r%2BGi8YRQRi4t3pYjxoR6U1oy8DlliTf6WtdvI%2BPXpfJTJ6aCL2cxnWpFNlIxNMtZfq1YKDQgYiI1ASs1P0BYzsgCBCr6%2BzilXeN%2BDDDZTS3SiuzjekphJNH%2FdXVc%2Fbj%2FtSDpPHDN%2FSayFjhDHXrgjYWOXxOHAru10vKpfbe9gScwWZ5eoh%2BYg3BXOa6QKhauyq16UieUCW2hHOqJzCYRjF7TkbUEYPeS%2B03D8DTsJRpLB6PTzT7M6ZgaaCLoKO1dbaTEt8odrzuZR017LUjlzLrJliItv8Rx8jezJrSv%2BsQhDMDc7TUZh8Pw65C0gttrK%2BdfIG2s3x9jm4jTzZeeAAkgrqLlU2zCnrrIN%2FZOCfcLyIcNkbjlIDJrc3XRxBmUsfIhnw3zQvtXdmcDQI9pwlKV8VicpTy0a83KDFOQf2ZmrP1Zfz4nwBUIE9tQ43RQkavImwApNZSzjjtJYWA9FM0TRHdfIExQcGzgJplutqjrDflTewLoIxrayeQT4xKTxQLQdl%2FnefFyolZC8sjTzjXtLDypwGldblIsBRQUO0poPYFUo4TD4kYe9BjqkAcergc0AM6MGDfbdk8eTYdSkIta%2F7ZdjybqaIFzSMkcUtLzHUztgx8ftaYW2hRVwCLz7XVAaIEAZBZ1%2BX%2BAVtrQMaXyTzJYdHrGN%2FU3s0lofkZ7cFUAxb1p3icwLpyNsoXcMoDLKaRf81szOV92wAxjP6maeg9Ef654kuQgDN33Dik0BTsap%2F8SXVOHuDb5BEyay2aSWikmBKLB8eXYmuebm2qqp&X-Amz-Signature=4fada4854c04820eeb9e047b4b6bd78b0f7fb49e1d470e95505213570ffc9224&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OZZZJGU%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081912Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJIMEYCIQCZoPe1UTYOobjgMArAezbrSnIuBxRioMJZi1vqgjZ6%2FwIhAMmnJ5g2oWXNod5x%2B0207%2BDbHo7TTHdXy8vb3xnPlcT9Kv8DCCkQABoMNjM3NDIzMTgzODA1IgyN4pG%2FV%2FjmS9tx%2Fm8q3AMa3HkUiM6qqGRIO2LMezAvioLMVolmh5bfU13RvDDKYmKeto%2FrOmleR%2BDiDbR7EcpbcWYkN07r%2BGi8YRQRi4t3pYjxoR6U1oy8DlliTf6WtdvI%2BPXpfJTJ6aCL2cxnWpFNlIxNMtZfq1YKDQgYiI1ASs1P0BYzsgCBCr6%2BzilXeN%2BDDDZTS3SiuzjekphJNH%2FdXVc%2Fbj%2FtSDpPHDN%2FSayFjhDHXrgjYWOXxOHAru10vKpfbe9gScwWZ5eoh%2BYg3BXOa6QKhauyq16UieUCW2hHOqJzCYRjF7TkbUEYPeS%2B03D8DTsJRpLB6PTzT7M6ZgaaCLoKO1dbaTEt8odrzuZR017LUjlzLrJliItv8Rx8jezJrSv%2BsQhDMDc7TUZh8Pw65C0gttrK%2BdfIG2s3x9jm4jTzZeeAAkgrqLlU2zCnrrIN%2FZOCfcLyIcNkbjlIDJrc3XRxBmUsfIhnw3zQvtXdmcDQI9pwlKV8VicpTy0a83KDFOQf2ZmrP1Zfz4nwBUIE9tQ43RQkavImwApNZSzjjtJYWA9FM0TRHdfIExQcGzgJplutqjrDflTewLoIxrayeQT4xKTxQLQdl%2FnefFyolZC8sjTzjXtLDypwGldblIsBRQUO0poPYFUo4TD4kYe9BjqkAcergc0AM6MGDfbdk8eTYdSkIta%2F7ZdjybqaIFzSMkcUtLzHUztgx8ftaYW2hRVwCLz7XVAaIEAZBZ1%2BX%2BAVtrQMaXyTzJYdHrGN%2FU3s0lofkZ7cFUAxb1p3icwLpyNsoXcMoDLKaRf81szOV92wAxjP6maeg9Ef654kuQgDN33Dik0BTsap%2F8SXVOHuDb5BEyay2aSWikmBKLB8eXYmuebm2qqp&X-Amz-Signature=a24abd910c9b0da0c1d9efa68917e10f84aaec8ffa9040563f2678621335c4f5&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
