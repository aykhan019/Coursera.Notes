

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QI7NGNCN%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQCwMvEKCCzff84n2ll9gPjVVOYTaIJ9bF%2BbXp1FvU7SqwIgCnhMJ5vn%2FgrmrhbPwvre3CYoIz4I6NsLoDZAUMY0mt0q%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDBUWjnGCEq2mGkuVCyrcA0EqCI0CdPIvL9UUFADskCuzXYsZNgtAR8hduCNkKg0X3COunfo8CU93Zs%2BfRRnERBo7%2Fh3knmHIaFRSmAZNtEFtcTpYUlJaPpC1h6apNx9RDA8kDEZ%2BaYSTTcQ1WaepwxhhaaunBfdAW0j9h%2BdUwGhz8%2BHwwF1KHPp0ELJ1QxQg%2BnqhPRFEVDL3jvs5wHaanlR%2Br2WqhO6V9n5Wd3XofrLHMzAPXYP%2BiWibv7Jy3S0HCZU5lpKFdZhsP%2FXa1eLsHPJtw8DV%2BsEy8GI0FekidBAUFtOJ1m2Ek0U12J0qPw5jzS5vykKp47Re548LUa5hLB2OeEwPWCuVw0KbMvH7SclZWirn7JSLvhQ%2BjBW3LSy%2Fmf8d%2BL3grUbvVJqj1I1oa%2B4vWrMXQ9lekJ%2B6z7pDWKaCpCoBgRNMrUY3hqU623SmURAW5DoOTvqmZdbwq1dgO8bdWuQFLLFGcYzk6LQBp1VgSncBdoU%2BPNG31iLiYFcOF7gZGBWbWml6F3KK2sKDNlEXUY4HaGwr215q0lrFTOd%2FOa%2Bu6HZQOT0ISXJh%2Bn13cmjTifEUwISCkPbGP6bItcyoPmDMeN4wPJ6djR2uPkD9V8PCwxJD6sdZ6jPj8I5Y3WpGmrfSNQmkLnbmMLb5lr0GOqUBbam73yJlXdv%2Fdfuv2MBh3NYh1KpkqZzcevNWzXIh63qBhFIIKltxCw%2BBM%2FvHn3y4SA8bCVRHii1MwRGia0jMSBROX%2BE5TFakAaEmvdspbbQAoWtIWR7OAyR5OQlRIrGN7mNgm9FAlzKNPNBzgqYXiwCj4aNBSKK5LB2dwlnWtsYUElg%2FllSDeWe6ZGseRhJeLQmrFIJYU8nhnuYgD34XPY8fpyJ3&X-Amz-Signature=d639f423834846f068aa6a94aa91a628a845f6f319e84ab7f6a8d343322336c4&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QI7NGNCN%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQCwMvEKCCzff84n2ll9gPjVVOYTaIJ9bF%2BbXp1FvU7SqwIgCnhMJ5vn%2FgrmrhbPwvre3CYoIz4I6NsLoDZAUMY0mt0q%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDBUWjnGCEq2mGkuVCyrcA0EqCI0CdPIvL9UUFADskCuzXYsZNgtAR8hduCNkKg0X3COunfo8CU93Zs%2BfRRnERBo7%2Fh3knmHIaFRSmAZNtEFtcTpYUlJaPpC1h6apNx9RDA8kDEZ%2BaYSTTcQ1WaepwxhhaaunBfdAW0j9h%2BdUwGhz8%2BHwwF1KHPp0ELJ1QxQg%2BnqhPRFEVDL3jvs5wHaanlR%2Br2WqhO6V9n5Wd3XofrLHMzAPXYP%2BiWibv7Jy3S0HCZU5lpKFdZhsP%2FXa1eLsHPJtw8DV%2BsEy8GI0FekidBAUFtOJ1m2Ek0U12J0qPw5jzS5vykKp47Re548LUa5hLB2OeEwPWCuVw0KbMvH7SclZWirn7JSLvhQ%2BjBW3LSy%2Fmf8d%2BL3grUbvVJqj1I1oa%2B4vWrMXQ9lekJ%2B6z7pDWKaCpCoBgRNMrUY3hqU623SmURAW5DoOTvqmZdbwq1dgO8bdWuQFLLFGcYzk6LQBp1VgSncBdoU%2BPNG31iLiYFcOF7gZGBWbWml6F3KK2sKDNlEXUY4HaGwr215q0lrFTOd%2FOa%2Bu6HZQOT0ISXJh%2Bn13cmjTifEUwISCkPbGP6bItcyoPmDMeN4wPJ6djR2uPkD9V8PCwxJD6sdZ6jPj8I5Y3WpGmrfSNQmkLnbmMLb5lr0GOqUBbam73yJlXdv%2Fdfuv2MBh3NYh1KpkqZzcevNWzXIh63qBhFIIKltxCw%2BBM%2FvHn3y4SA8bCVRHii1MwRGia0jMSBROX%2BE5TFakAaEmvdspbbQAoWtIWR7OAyR5OQlRIrGN7mNgm9FAlzKNPNBzgqYXiwCj4aNBSKK5LB2dwlnWtsYUElg%2FllSDeWe6ZGseRhJeLQmrFIJYU8nhnuYgD34XPY8fpyJ3&X-Amz-Signature=4bfb90de475acb9073cab05690d994d173640162e633f063ddeb18064c84f501&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QI7NGNCN%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQCwMvEKCCzff84n2ll9gPjVVOYTaIJ9bF%2BbXp1FvU7SqwIgCnhMJ5vn%2FgrmrhbPwvre3CYoIz4I6NsLoDZAUMY0mt0q%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDBUWjnGCEq2mGkuVCyrcA0EqCI0CdPIvL9UUFADskCuzXYsZNgtAR8hduCNkKg0X3COunfo8CU93Zs%2BfRRnERBo7%2Fh3knmHIaFRSmAZNtEFtcTpYUlJaPpC1h6apNx9RDA8kDEZ%2BaYSTTcQ1WaepwxhhaaunBfdAW0j9h%2BdUwGhz8%2BHwwF1KHPp0ELJ1QxQg%2BnqhPRFEVDL3jvs5wHaanlR%2Br2WqhO6V9n5Wd3XofrLHMzAPXYP%2BiWibv7Jy3S0HCZU5lpKFdZhsP%2FXa1eLsHPJtw8DV%2BsEy8GI0FekidBAUFtOJ1m2Ek0U12J0qPw5jzS5vykKp47Re548LUa5hLB2OeEwPWCuVw0KbMvH7SclZWirn7JSLvhQ%2BjBW3LSy%2Fmf8d%2BL3grUbvVJqj1I1oa%2B4vWrMXQ9lekJ%2B6z7pDWKaCpCoBgRNMrUY3hqU623SmURAW5DoOTvqmZdbwq1dgO8bdWuQFLLFGcYzk6LQBp1VgSncBdoU%2BPNG31iLiYFcOF7gZGBWbWml6F3KK2sKDNlEXUY4HaGwr215q0lrFTOd%2FOa%2Bu6HZQOT0ISXJh%2Bn13cmjTifEUwISCkPbGP6bItcyoPmDMeN4wPJ6djR2uPkD9V8PCwxJD6sdZ6jPj8I5Y3WpGmrfSNQmkLnbmMLb5lr0GOqUBbam73yJlXdv%2Fdfuv2MBh3NYh1KpkqZzcevNWzXIh63qBhFIIKltxCw%2BBM%2FvHn3y4SA8bCVRHii1MwRGia0jMSBROX%2BE5TFakAaEmvdspbbQAoWtIWR7OAyR5OQlRIrGN7mNgm9FAlzKNPNBzgqYXiwCj4aNBSKK5LB2dwlnWtsYUElg%2FllSDeWe6ZGseRhJeLQmrFIJYU8nhnuYgD34XPY8fpyJ3&X-Amz-Signature=ca0bdc47d0837b1962ef61c00c36e39081503427dce34b34d7dd8095853a1e79&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RURZZHNZ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIBf7ERmt%2F0NvS%2F%2FLoVRkjTJ1bDRq5myt6rA4qmVUVEimAiAanVmoYReBDJYtgb0DxdJDqdg15FxlAVYzC4XCUvlwfyr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIMw00E5ConZNK30RzdKtwDIH%2FD4UoXLoAsWm7F1mD5MO9wmhZwBLSysx76tww3O%2FkhlrvXz%2B4YWkDbabFPgTTeHCasw1s8gV%2FU50tQR1SfcKmrmU9tDoBrX0N7hgUQVZOtYKFU1AYNXq1IerQDXIFJQ9pc2qtX5eCQZ2TFd5kMlAbUcd0BbpxLjycBYj4tN4z%2B6g642ukASFsb9I%2FN9eCT78SB2bLTKB8jx%2BqEt%2FaB0kTWD%2F%2BHW11BatA4HoETgvbvCBYZxP11An7WOayjQsC62dC980niD2mjLet6S1UsywvwKNRAMZ7kDEzYQbyvUG7KKWuDpN9cAl9BbJNurNhecFSVWdOSB1o81%2F750j6Mi%2B9fLYy3MQLLANsBpUIb5EA9ewisiRYcnBGE5MWLaigZHBFiSOM3uhsqOuHb%2FkTme2Y%2BoNPVCcCXxx55SpCKR70KO6cUMn48TZiTyWG1uHT3jXOQXTipaMfK2aoDGOQJDVC9efFCe6Z0roKcYV82saiZShCQY9DR%2FXw3UHM6qc9OlLzC%2BRzZTGiF%2BvZMBzkio61p1wLnAkrradRT6one2h2OkvnpcS%2F6taViHs0i80VaOinZZZdTXlgBptbrRS%2BOBaAyJFgTy0mkDEoHJOO1BYflskbfoEBG0h1AUuMwwPmWvQY6pgF6vMlrF0ypS5R9R8FSnIjqFhHA%2FDsv%2FzWUGf%2FPuJ03iDFjRQWlA4BbRhG42qGadXhIBL5yeZzhySVG3V4AFZW1jPZr8ISg7pioHkO2RAKflKFOYVB0iYXIBPHWMw%2BQ6f7KWeVPTEgWEtyjgaAsKqEJmkpFvYYv2OSmohN7BPAbLGkWrPxnP9X%2Bn4VKxJq8h7aW9483LIXk%2Fba4pRgZfQAwyab4VpWK&X-Amz-Signature=d0271f9685e495e1db8c89785090884cdd0000532ad6d6232bfa77b6cd6fc043&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46653J6F63T%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJIMEYCIQCylKPoSg68Lqu0yo6NjcVz8BQin91Wxdeajw3dHQtqpgIhAKxguSIDJ8E1C%2Bkvbmkp2wZ4w5%2BlsIdjBV%2BNwZTIizmKKv8DCHEQABoMNjM3NDIzMTgzODA1Igy24XNCWyHkCBlEkVcq3AO9ryUU1qz%2Fts9R6Irpiej%2B%2FnpcN%2FbuRTyyokpIGv006tprMN1XKtUZA36vETZc0CkLH5LuJW%2BXLEmdmVXzxCiJDfAuLYAQNdmNdkri9ZLEXfjLQxG4QWlTYRfaXHZQiYdCq3InixJonfpsuR6qShryCTE06w%2FAuDNc3qhMv7EZH8ZdBCepHZ5KDnGKNO4f7XSua0Yy8QJWH8Dz%2Bb7cO0%2BC1TBW8N9jRpyKItd2p8K1K6wuCg6nsyrWnJEf5QPNuNIzAUu2aXmJoffnCbpAhw14vBswdR%2BYGFRjcYFyXJacKS4hP3QLboHJA0433lRnzSMv6FedwYqsXyll%2F2MTNSJLAV3YVnoh3lQUY9Tc2pR5Swdekwo5whLMOOGUsDfHJIR196XIqnyH7pVRrENevb8f37abr%2FbW68XAJtPsk%2F3ziXq9snLfQvKGsJWMKtdyzjm8ijL1VRPp6LaubIVn2yBhSdzCFH3PNCNhkizGtw1r3HjCpwOy%2ByO%2F9yLc1wgLoeTm%2BgLkC3FGXAi2AVxV00WoXE9Eb6EgGTDTaMwWJo4G33YekCmos3Eid5OUpH7koq34UzqLN3vmPhiA2WeigEAXL8ZvyNLtK6uCwbak5zrLzZOsEC2Xh%2F8qCe4G1TC3%2BZa9BjqkATlsBwcR%2BC8IqUkg%2FmnMd85D3pTKbd9Du5qt1k9KmtBaSG4u1Bolz%2FMT6jqOw0UkpMe8e8jGGJX6y6WkfLgFEoNI%2BSbJnvxomuq7j64PiZstxlzOTIZsJHyTDHI4DBzxwJZsjAX1AinKaL7iyQQOTSiFgJpx09zrYyPf0fXoK6SV6DrzIzdxXWfiv0gDO8dMtbRYp21i5LEGo0VnYcGTkiowXZDR&X-Amz-Signature=f42a1abb6c774fea103c0fa3547a7ba1ed8dbb9ef711911c1b121664d640cb74&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QI7NGNCN%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQCwMvEKCCzff84n2ll9gPjVVOYTaIJ9bF%2BbXp1FvU7SqwIgCnhMJ5vn%2FgrmrhbPwvre3CYoIz4I6NsLoDZAUMY0mt0q%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDBUWjnGCEq2mGkuVCyrcA0EqCI0CdPIvL9UUFADskCuzXYsZNgtAR8hduCNkKg0X3COunfo8CU93Zs%2BfRRnERBo7%2Fh3knmHIaFRSmAZNtEFtcTpYUlJaPpC1h6apNx9RDA8kDEZ%2BaYSTTcQ1WaepwxhhaaunBfdAW0j9h%2BdUwGhz8%2BHwwF1KHPp0ELJ1QxQg%2BnqhPRFEVDL3jvs5wHaanlR%2Br2WqhO6V9n5Wd3XofrLHMzAPXYP%2BiWibv7Jy3S0HCZU5lpKFdZhsP%2FXa1eLsHPJtw8DV%2BsEy8GI0FekidBAUFtOJ1m2Ek0U12J0qPw5jzS5vykKp47Re548LUa5hLB2OeEwPWCuVw0KbMvH7SclZWirn7JSLvhQ%2BjBW3LSy%2Fmf8d%2BL3grUbvVJqj1I1oa%2B4vWrMXQ9lekJ%2B6z7pDWKaCpCoBgRNMrUY3hqU623SmURAW5DoOTvqmZdbwq1dgO8bdWuQFLLFGcYzk6LQBp1VgSncBdoU%2BPNG31iLiYFcOF7gZGBWbWml6F3KK2sKDNlEXUY4HaGwr215q0lrFTOd%2FOa%2Bu6HZQOT0ISXJh%2Bn13cmjTifEUwISCkPbGP6bItcyoPmDMeN4wPJ6djR2uPkD9V8PCwxJD6sdZ6jPj8I5Y3WpGmrfSNQmkLnbmMLb5lr0GOqUBbam73yJlXdv%2Fdfuv2MBh3NYh1KpkqZzcevNWzXIh63qBhFIIKltxCw%2BBM%2FvHn3y4SA8bCVRHii1MwRGia0jMSBROX%2BE5TFakAaEmvdspbbQAoWtIWR7OAyR5OQlRIrGN7mNgm9FAlzKNPNBzgqYXiwCj4aNBSKK5LB2dwlnWtsYUElg%2FllSDeWe6ZGseRhJeLQmrFIJYU8nhnuYgD34XPY8fpyJ3&X-Amz-Signature=17c82737361ef0742fa7eeb0c328ffbf81de1d69cfb0e4e6916c2b7058fb835a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QI7NGNCN%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQCwMvEKCCzff84n2ll9gPjVVOYTaIJ9bF%2BbXp1FvU7SqwIgCnhMJ5vn%2FgrmrhbPwvre3CYoIz4I6NsLoDZAUMY0mt0q%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDBUWjnGCEq2mGkuVCyrcA0EqCI0CdPIvL9UUFADskCuzXYsZNgtAR8hduCNkKg0X3COunfo8CU93Zs%2BfRRnERBo7%2Fh3knmHIaFRSmAZNtEFtcTpYUlJaPpC1h6apNx9RDA8kDEZ%2BaYSTTcQ1WaepwxhhaaunBfdAW0j9h%2BdUwGhz8%2BHwwF1KHPp0ELJ1QxQg%2BnqhPRFEVDL3jvs5wHaanlR%2Br2WqhO6V9n5Wd3XofrLHMzAPXYP%2BiWibv7Jy3S0HCZU5lpKFdZhsP%2FXa1eLsHPJtw8DV%2BsEy8GI0FekidBAUFtOJ1m2Ek0U12J0qPw5jzS5vykKp47Re548LUa5hLB2OeEwPWCuVw0KbMvH7SclZWirn7JSLvhQ%2BjBW3LSy%2Fmf8d%2BL3grUbvVJqj1I1oa%2B4vWrMXQ9lekJ%2B6z7pDWKaCpCoBgRNMrUY3hqU623SmURAW5DoOTvqmZdbwq1dgO8bdWuQFLLFGcYzk6LQBp1VgSncBdoU%2BPNG31iLiYFcOF7gZGBWbWml6F3KK2sKDNlEXUY4HaGwr215q0lrFTOd%2FOa%2Bu6HZQOT0ISXJh%2Bn13cmjTifEUwISCkPbGP6bItcyoPmDMeN4wPJ6djR2uPkD9V8PCwxJD6sdZ6jPj8I5Y3WpGmrfSNQmkLnbmMLb5lr0GOqUBbam73yJlXdv%2Fdfuv2MBh3NYh1KpkqZzcevNWzXIh63qBhFIIKltxCw%2BBM%2FvHn3y4SA8bCVRHii1MwRGia0jMSBROX%2BE5TFakAaEmvdspbbQAoWtIWR7OAyR5OQlRIrGN7mNgm9FAlzKNPNBzgqYXiwCj4aNBSKK5LB2dwlnWtsYUElg%2FllSDeWe6ZGseRhJeLQmrFIJYU8nhnuYgD34XPY8fpyJ3&X-Amz-Signature=d6d65b0b574e90a81b35a24b1cab4ef26593e976add28d54aa90d208325052c6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QI7NGNCN%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQCwMvEKCCzff84n2ll9gPjVVOYTaIJ9bF%2BbXp1FvU7SqwIgCnhMJ5vn%2FgrmrhbPwvre3CYoIz4I6NsLoDZAUMY0mt0q%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDBUWjnGCEq2mGkuVCyrcA0EqCI0CdPIvL9UUFADskCuzXYsZNgtAR8hduCNkKg0X3COunfo8CU93Zs%2BfRRnERBo7%2Fh3knmHIaFRSmAZNtEFtcTpYUlJaPpC1h6apNx9RDA8kDEZ%2BaYSTTcQ1WaepwxhhaaunBfdAW0j9h%2BdUwGhz8%2BHwwF1KHPp0ELJ1QxQg%2BnqhPRFEVDL3jvs5wHaanlR%2Br2WqhO6V9n5Wd3XofrLHMzAPXYP%2BiWibv7Jy3S0HCZU5lpKFdZhsP%2FXa1eLsHPJtw8DV%2BsEy8GI0FekidBAUFtOJ1m2Ek0U12J0qPw5jzS5vykKp47Re548LUa5hLB2OeEwPWCuVw0KbMvH7SclZWirn7JSLvhQ%2BjBW3LSy%2Fmf8d%2BL3grUbvVJqj1I1oa%2B4vWrMXQ9lekJ%2B6z7pDWKaCpCoBgRNMrUY3hqU623SmURAW5DoOTvqmZdbwq1dgO8bdWuQFLLFGcYzk6LQBp1VgSncBdoU%2BPNG31iLiYFcOF7gZGBWbWml6F3KK2sKDNlEXUY4HaGwr215q0lrFTOd%2FOa%2Bu6HZQOT0ISXJh%2Bn13cmjTifEUwISCkPbGP6bItcyoPmDMeN4wPJ6djR2uPkD9V8PCwxJD6sdZ6jPj8I5Y3WpGmrfSNQmkLnbmMLb5lr0GOqUBbam73yJlXdv%2Fdfuv2MBh3NYh1KpkqZzcevNWzXIh63qBhFIIKltxCw%2BBM%2FvHn3y4SA8bCVRHii1MwRGia0jMSBROX%2BE5TFakAaEmvdspbbQAoWtIWR7OAyR5OQlRIrGN7mNgm9FAlzKNPNBzgqYXiwCj4aNBSKK5LB2dwlnWtsYUElg%2FllSDeWe6ZGseRhJeLQmrFIJYU8nhnuYgD34XPY8fpyJ3&X-Amz-Signature=fb7b1628a65a15910ef84832177dda1bbefc0d66e829b5fe3596b4764c0ccd31&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QI7NGNCN%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQCwMvEKCCzff84n2ll9gPjVVOYTaIJ9bF%2BbXp1FvU7SqwIgCnhMJ5vn%2FgrmrhbPwvre3CYoIz4I6NsLoDZAUMY0mt0q%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDBUWjnGCEq2mGkuVCyrcA0EqCI0CdPIvL9UUFADskCuzXYsZNgtAR8hduCNkKg0X3COunfo8CU93Zs%2BfRRnERBo7%2Fh3knmHIaFRSmAZNtEFtcTpYUlJaPpC1h6apNx9RDA8kDEZ%2BaYSTTcQ1WaepwxhhaaunBfdAW0j9h%2BdUwGhz8%2BHwwF1KHPp0ELJ1QxQg%2BnqhPRFEVDL3jvs5wHaanlR%2Br2WqhO6V9n5Wd3XofrLHMzAPXYP%2BiWibv7Jy3S0HCZU5lpKFdZhsP%2FXa1eLsHPJtw8DV%2BsEy8GI0FekidBAUFtOJ1m2Ek0U12J0qPw5jzS5vykKp47Re548LUa5hLB2OeEwPWCuVw0KbMvH7SclZWirn7JSLvhQ%2BjBW3LSy%2Fmf8d%2BL3grUbvVJqj1I1oa%2B4vWrMXQ9lekJ%2B6z7pDWKaCpCoBgRNMrUY3hqU623SmURAW5DoOTvqmZdbwq1dgO8bdWuQFLLFGcYzk6LQBp1VgSncBdoU%2BPNG31iLiYFcOF7gZGBWbWml6F3KK2sKDNlEXUY4HaGwr215q0lrFTOd%2FOa%2Bu6HZQOT0ISXJh%2Bn13cmjTifEUwISCkPbGP6bItcyoPmDMeN4wPJ6djR2uPkD9V8PCwxJD6sdZ6jPj8I5Y3WpGmrfSNQmkLnbmMLb5lr0GOqUBbam73yJlXdv%2Fdfuv2MBh3NYh1KpkqZzcevNWzXIh63qBhFIIKltxCw%2BBM%2FvHn3y4SA8bCVRHii1MwRGia0jMSBROX%2BE5TFakAaEmvdspbbQAoWtIWR7OAyR5OQlRIrGN7mNgm9FAlzKNPNBzgqYXiwCj4aNBSKK5LB2dwlnWtsYUElg%2FllSDeWe6ZGseRhJeLQmrFIJYU8nhnuYgD34XPY8fpyJ3&X-Amz-Signature=1572708c06ef25fdef7b47db3c9a83742a114496bd06aa978f4c90ca353591a2&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
