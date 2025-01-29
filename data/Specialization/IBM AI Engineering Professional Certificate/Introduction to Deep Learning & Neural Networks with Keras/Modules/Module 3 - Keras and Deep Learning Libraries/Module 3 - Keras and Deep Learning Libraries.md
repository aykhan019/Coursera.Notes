

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYS7VHL6%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCHH7brwNLjIRgB43H6BX8bR5BalMf69Ym9P0HShnFfJwIgeL2I8Lkl4rl3LaYwkyTzoBtbHbBqCD0xiro09M23ek8qiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ9Bfve84cHVuW1w6SrcA%2FCslKNSPQxxTxxNTTvl6aZbi0qtfZq3bn0rxmUSvGzR8Ep7oIPnpQu8EfzcMqtb8bxZJuzZnERQTR0DH9YX8%2FIEsgkJHfPF6F7mlSj68FIvYIO%2FzPdAhK2kBj6Tj3jf3WLs1aJ7%2BKS1F0n6wnlJtcxoWdkdzRn8Uzm6DuFtsraQn1rNAr4uMzoxcFf4ZdbOsbVUZ0a6lAaLdhmBcH%2B7KWlxkSGeCRs8lYDDTCpUmikbyNtA9QhgXtFpBaT4ia4wa7N70HWBgqyaiWfpAU2hKZzToh1vNXoCe11FPiOyeXhU4m8DyPKnRqtI97DCXYXjuxJk3ah1UOS24JC9hc%2Fl8fE05OF%2BQ%2BOFm0taBVMj14RSf8Gkph4eIGPPE9v3ol0fsNIuUXTKesC5ReqMml948g2v9FxnNSwNPA7itIS4lonqUqRWl7ay%2BQyLZF4it9N4I11v%2FAC5sFWEHIFF8SFRYgx7xHVDTVwsk%2Bo2wrW8q1FQxliaaTyEfblUSbF9ep51c8A6pdeohNzGgT9aOsClsdeLVSG96fPnQJwwJZtI8DoWpWXpuodq39cc4437bHZpHiWv4DR4B559bHYKoDH9uutjHojone7xOGIEGWbH6bjudyiBdXpAJFh%2FGzMVMK316bwGOqUBK%2BDh29V8WYHWLaDHgz48CIk5BTFoYGuWXk91DANH52Fkt0Gl5MQRwPuAedYz2MxqbPBqYu%2BtjBLS7owgIQf13sDIjEb5AvWI5R9uRWKkKM9rM5Oquirk7A0uVfIYy3hcmO%2BPdRhSUsmiabhfee95Wbru1SB4%2FfT7U%2BBfUjOc7DdTYaJAWl1zEKzeQrj7A%2F4Lt1o8010rHQ7geRS75sNnNNLAFI3p&X-Amz-Signature=340e79c116e9817f29c45373a2a545c23508151e459d5b597d3ff4b75afbdb8c&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYS7VHL6%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCHH7brwNLjIRgB43H6BX8bR5BalMf69Ym9P0HShnFfJwIgeL2I8Lkl4rl3LaYwkyTzoBtbHbBqCD0xiro09M23ek8qiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ9Bfve84cHVuW1w6SrcA%2FCslKNSPQxxTxxNTTvl6aZbi0qtfZq3bn0rxmUSvGzR8Ep7oIPnpQu8EfzcMqtb8bxZJuzZnERQTR0DH9YX8%2FIEsgkJHfPF6F7mlSj68FIvYIO%2FzPdAhK2kBj6Tj3jf3WLs1aJ7%2BKS1F0n6wnlJtcxoWdkdzRn8Uzm6DuFtsraQn1rNAr4uMzoxcFf4ZdbOsbVUZ0a6lAaLdhmBcH%2B7KWlxkSGeCRs8lYDDTCpUmikbyNtA9QhgXtFpBaT4ia4wa7N70HWBgqyaiWfpAU2hKZzToh1vNXoCe11FPiOyeXhU4m8DyPKnRqtI97DCXYXjuxJk3ah1UOS24JC9hc%2Fl8fE05OF%2BQ%2BOFm0taBVMj14RSf8Gkph4eIGPPE9v3ol0fsNIuUXTKesC5ReqMml948g2v9FxnNSwNPA7itIS4lonqUqRWl7ay%2BQyLZF4it9N4I11v%2FAC5sFWEHIFF8SFRYgx7xHVDTVwsk%2Bo2wrW8q1FQxliaaTyEfblUSbF9ep51c8A6pdeohNzGgT9aOsClsdeLVSG96fPnQJwwJZtI8DoWpWXpuodq39cc4437bHZpHiWv4DR4B559bHYKoDH9uutjHojone7xOGIEGWbH6bjudyiBdXpAJFh%2FGzMVMK316bwGOqUBK%2BDh29V8WYHWLaDHgz48CIk5BTFoYGuWXk91DANH52Fkt0Gl5MQRwPuAedYz2MxqbPBqYu%2BtjBLS7owgIQf13sDIjEb5AvWI5R9uRWKkKM9rM5Oquirk7A0uVfIYy3hcmO%2BPdRhSUsmiabhfee95Wbru1SB4%2FfT7U%2BBfUjOc7DdTYaJAWl1zEKzeQrj7A%2F4Lt1o8010rHQ7geRS75sNnNNLAFI3p&X-Amz-Signature=eae63371f29e4f2b03598db92b4e7e0c89045fc3ddd2c0a02a74e4f5c8438b55&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYS7VHL6%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCHH7brwNLjIRgB43H6BX8bR5BalMf69Ym9P0HShnFfJwIgeL2I8Lkl4rl3LaYwkyTzoBtbHbBqCD0xiro09M23ek8qiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ9Bfve84cHVuW1w6SrcA%2FCslKNSPQxxTxxNTTvl6aZbi0qtfZq3bn0rxmUSvGzR8Ep7oIPnpQu8EfzcMqtb8bxZJuzZnERQTR0DH9YX8%2FIEsgkJHfPF6F7mlSj68FIvYIO%2FzPdAhK2kBj6Tj3jf3WLs1aJ7%2BKS1F0n6wnlJtcxoWdkdzRn8Uzm6DuFtsraQn1rNAr4uMzoxcFf4ZdbOsbVUZ0a6lAaLdhmBcH%2B7KWlxkSGeCRs8lYDDTCpUmikbyNtA9QhgXtFpBaT4ia4wa7N70HWBgqyaiWfpAU2hKZzToh1vNXoCe11FPiOyeXhU4m8DyPKnRqtI97DCXYXjuxJk3ah1UOS24JC9hc%2Fl8fE05OF%2BQ%2BOFm0taBVMj14RSf8Gkph4eIGPPE9v3ol0fsNIuUXTKesC5ReqMml948g2v9FxnNSwNPA7itIS4lonqUqRWl7ay%2BQyLZF4it9N4I11v%2FAC5sFWEHIFF8SFRYgx7xHVDTVwsk%2Bo2wrW8q1FQxliaaTyEfblUSbF9ep51c8A6pdeohNzGgT9aOsClsdeLVSG96fPnQJwwJZtI8DoWpWXpuodq39cc4437bHZpHiWv4DR4B559bHYKoDH9uutjHojone7xOGIEGWbH6bjudyiBdXpAJFh%2FGzMVMK316bwGOqUBK%2BDh29V8WYHWLaDHgz48CIk5BTFoYGuWXk91DANH52Fkt0Gl5MQRwPuAedYz2MxqbPBqYu%2BtjBLS7owgIQf13sDIjEb5AvWI5R9uRWKkKM9rM5Oquirk7A0uVfIYy3hcmO%2BPdRhSUsmiabhfee95Wbru1SB4%2FfT7U%2BBfUjOc7DdTYaJAWl1zEKzeQrj7A%2F4Lt1o8010rHQ7geRS75sNnNNLAFI3p&X-Amz-Signature=f13a8eb38d3e1f5cb003e798f2e4ca342a0bc56990dd00d874b8ccb5cfdc030a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667YHUX62Q%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201546Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDcfuyy2Pvu%2FSULKGupptCrgUipSXOWVbyinHN%2FHUpYDQIhAOHtj2B%2BQuRm3nldHxaDcjrIb498i4fa2utp0biB5AP2KogECJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgziP7cXXcl%2Fdsltnvsq3ANtW5L2lDqbYvfDI2hw%2B3rvHYlbZJ7utZmBi1odxlhVOAX3y2tYTJtAEioOFT5Mwck1QWQnFQ7mDGKmzTY0LDf7AUGgyClfyKJ2a71CIkf058KLh6VdMjj4loU4366PxNfzenqtFBbEKlP7KeMJsPs8irXwP2WWBOSB4cm6TJQoyYbtuJhPTOmN%2F%2BnBr8lb1c5GpORf04TtsxsEYWfzFahC7tcBoNqW8SzJjTUYYXvTtwf5dddzYUsBeG940%2BSDb0G1MA3Z4fUSzIGGUefWYGpVvkmK1SjiW61%2FtymFKXydgB3lOzOt%2F4gS1ZbHF%2FpkO4cXG5SKI7bHBpbNpjQpPmb2EHWipe30FrScCxYPeiBQ3wow1lqufcDbT0v%2BXODz2NMAoNWj%2BQ5XbbweJEiohs5FO49QgG9VWPo%2FX8IDTFZlTf%2BdR5CURcbrpD3g3W7lqszqQPM00UTmvgv%2FzXcHmzgYjhuhn%2Bpn3UclWpTZBfZka7VPpHNRohZh8pFT7Dz015awRdU7Ns2GZECmPKuO5dU4dkKyEg2hhM76OtvrdKCUNF1S6ZsgbzE6hV2NcpJFWLawjNNKrj%2BcyINNCk3n4SyfjdSbMDIvvk8a07BD20F5EqBByORHCz34PdFSmTCU9em8BjqkAUqiSGStjfNXiSsU4WbseSjMdzndVMNqRqxm0i6%2FFFE8WAKW0IZuSi87iNeuBZsnoIHZtZNp%2FBHD1eSYNU4xBp3LMBlSeYHkSbdO8c8WnqpeWEJdGi4%2BtVhA%2Fy9X2tbVit88gpiFds%2Buw1xEjgmUQHnHVu%2BBB1C1uSlGpQ4Zr1JGK6Tq6ax%2FnTJwdd2qaIiSH0PZDm6nsO5tI52HWFgMXfKwXlAU&X-Amz-Signature=07d485926dd8ac7cd43ce7abc768e613a2045eb676c207ad63782b13d6e0b5b5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUSQGT2O%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201546Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAzSg0kR0jLXkwwN7tVKQNoVR8iYFviMFodTbltpUdIYAiEAtfcOrmCB35nq%2F3h%2FIiSb8G4bmzi6ZDfebBDSl7RTNLcqiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAcGeE1V5cRlKewrEyrcA2MVfjoDr644FjHG4aX%2Fz18ZCBEa%2Fy7AzpaXskyQFqKuwHlKoNqdtxrpZSUe7xqtLYWBQt%2Bp%2B0mIllkTBkiqNBQSSgeqoRqtu0%2B8%2FDo%2FMpJXsmA1wucclJX4MeDAxFFvmifN65UFUJADrQy6vtTsAM6dsr7h4BAXzQ7NQdJTrXhCx5B7DtpYk1fY27IR18wTeUp3YlPypUPpdMV0ckSktzIfyyOIA1EKF0WrALZBfA5ABf7lMTrwW0%2Fyhdxp0yZ4sfPnt3aCk3DtUwqxdYiGjSAc8vk4Twzb3%2Bd4Oa2qWJANUZNaNJkjsf%2BNqpcjUBPFgL%2F5KFcnTru4v0V4tczpvsEEQYQS4FtsNAHybj7RFsSanxaQ5dNgDYPlGzydeilBr580GlZTim5Rmmi%2BnRcO0ZO6AW68K%2Ff2uleTlCEFCXWr5bvxAU%2F0xIsmRdnhfi69UocwGbIsBqJ%2BrPdV09LoAiHp4Uz4%2F%2BMEXTauGdwjCKBhMhjxZGEIVyZpPtRg7aNppqBlNVfO3STXSVapnjLBsajo61nO1plihIfVN%2BeHH0MEiqVa2shau7f%2BryzxLeAIe20MQv4TPaBLTj%2F%2F4VOQioostLbzfKDCVI40VBVWxcbsZlbpxXyjPAiYx1%2BoMK316bwGOqUBo1pI2B0BpXa3U92Nj1nz2mIsR3efBBdeBYWDoEzTI9bWFFCqjIVanKpPHnnpqhGTkGeRjdXUpDFqPCPv%2F2nOD5AG%2FWgEl4fvfcuw1jkeT5Qn7yXGtVnwThMQPoshVoAtmbFL723YHQyOT430kdH4cSd8Wylw3W6I2TXv09v8rydVNgCEjV9eXmjx%2B%2FBHlvvXEZg5ghL6EKZCZCCI%2BF3xWFUhNLim&X-Amz-Signature=14f7ffc5932ba7603ec9c0c16c64614a0ed858084e2e73b617ea09ca3fa88aaf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYS7VHL6%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCHH7brwNLjIRgB43H6BX8bR5BalMf69Ym9P0HShnFfJwIgeL2I8Lkl4rl3LaYwkyTzoBtbHbBqCD0xiro09M23ek8qiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ9Bfve84cHVuW1w6SrcA%2FCslKNSPQxxTxxNTTvl6aZbi0qtfZq3bn0rxmUSvGzR8Ep7oIPnpQu8EfzcMqtb8bxZJuzZnERQTR0DH9YX8%2FIEsgkJHfPF6F7mlSj68FIvYIO%2FzPdAhK2kBj6Tj3jf3WLs1aJ7%2BKS1F0n6wnlJtcxoWdkdzRn8Uzm6DuFtsraQn1rNAr4uMzoxcFf4ZdbOsbVUZ0a6lAaLdhmBcH%2B7KWlxkSGeCRs8lYDDTCpUmikbyNtA9QhgXtFpBaT4ia4wa7N70HWBgqyaiWfpAU2hKZzToh1vNXoCe11FPiOyeXhU4m8DyPKnRqtI97DCXYXjuxJk3ah1UOS24JC9hc%2Fl8fE05OF%2BQ%2BOFm0taBVMj14RSf8Gkph4eIGPPE9v3ol0fsNIuUXTKesC5ReqMml948g2v9FxnNSwNPA7itIS4lonqUqRWl7ay%2BQyLZF4it9N4I11v%2FAC5sFWEHIFF8SFRYgx7xHVDTVwsk%2Bo2wrW8q1FQxliaaTyEfblUSbF9ep51c8A6pdeohNzGgT9aOsClsdeLVSG96fPnQJwwJZtI8DoWpWXpuodq39cc4437bHZpHiWv4DR4B559bHYKoDH9uutjHojone7xOGIEGWbH6bjudyiBdXpAJFh%2FGzMVMK316bwGOqUBK%2BDh29V8WYHWLaDHgz48CIk5BTFoYGuWXk91DANH52Fkt0Gl5MQRwPuAedYz2MxqbPBqYu%2BtjBLS7owgIQf13sDIjEb5AvWI5R9uRWKkKM9rM5Oquirk7A0uVfIYy3hcmO%2BPdRhSUsmiabhfee95Wbru1SB4%2FfT7U%2BBfUjOc7DdTYaJAWl1zEKzeQrj7A%2F4Lt1o8010rHQ7geRS75sNnNNLAFI3p&X-Amz-Signature=836598b8a9aa8f4c797854047c4d95f02375e9e4eecb644d6413a0d7fdcdd3d9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYS7VHL6%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCHH7brwNLjIRgB43H6BX8bR5BalMf69Ym9P0HShnFfJwIgeL2I8Lkl4rl3LaYwkyTzoBtbHbBqCD0xiro09M23ek8qiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ9Bfve84cHVuW1w6SrcA%2FCslKNSPQxxTxxNTTvl6aZbi0qtfZq3bn0rxmUSvGzR8Ep7oIPnpQu8EfzcMqtb8bxZJuzZnERQTR0DH9YX8%2FIEsgkJHfPF6F7mlSj68FIvYIO%2FzPdAhK2kBj6Tj3jf3WLs1aJ7%2BKS1F0n6wnlJtcxoWdkdzRn8Uzm6DuFtsraQn1rNAr4uMzoxcFf4ZdbOsbVUZ0a6lAaLdhmBcH%2B7KWlxkSGeCRs8lYDDTCpUmikbyNtA9QhgXtFpBaT4ia4wa7N70HWBgqyaiWfpAU2hKZzToh1vNXoCe11FPiOyeXhU4m8DyPKnRqtI97DCXYXjuxJk3ah1UOS24JC9hc%2Fl8fE05OF%2BQ%2BOFm0taBVMj14RSf8Gkph4eIGPPE9v3ol0fsNIuUXTKesC5ReqMml948g2v9FxnNSwNPA7itIS4lonqUqRWl7ay%2BQyLZF4it9N4I11v%2FAC5sFWEHIFF8SFRYgx7xHVDTVwsk%2Bo2wrW8q1FQxliaaTyEfblUSbF9ep51c8A6pdeohNzGgT9aOsClsdeLVSG96fPnQJwwJZtI8DoWpWXpuodq39cc4437bHZpHiWv4DR4B559bHYKoDH9uutjHojone7xOGIEGWbH6bjudyiBdXpAJFh%2FGzMVMK316bwGOqUBK%2BDh29V8WYHWLaDHgz48CIk5BTFoYGuWXk91DANH52Fkt0Gl5MQRwPuAedYz2MxqbPBqYu%2BtjBLS7owgIQf13sDIjEb5AvWI5R9uRWKkKM9rM5Oquirk7A0uVfIYy3hcmO%2BPdRhSUsmiabhfee95Wbru1SB4%2FfT7U%2BBfUjOc7DdTYaJAWl1zEKzeQrj7A%2F4Lt1o8010rHQ7geRS75sNnNNLAFI3p&X-Amz-Signature=46fdb8ce591f29e083993fbf66211bf53ce2bf0eabc82a561398c29f621e31b0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYS7VHL6%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCHH7brwNLjIRgB43H6BX8bR5BalMf69Ym9P0HShnFfJwIgeL2I8Lkl4rl3LaYwkyTzoBtbHbBqCD0xiro09M23ek8qiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ9Bfve84cHVuW1w6SrcA%2FCslKNSPQxxTxxNTTvl6aZbi0qtfZq3bn0rxmUSvGzR8Ep7oIPnpQu8EfzcMqtb8bxZJuzZnERQTR0DH9YX8%2FIEsgkJHfPF6F7mlSj68FIvYIO%2FzPdAhK2kBj6Tj3jf3WLs1aJ7%2BKS1F0n6wnlJtcxoWdkdzRn8Uzm6DuFtsraQn1rNAr4uMzoxcFf4ZdbOsbVUZ0a6lAaLdhmBcH%2B7KWlxkSGeCRs8lYDDTCpUmikbyNtA9QhgXtFpBaT4ia4wa7N70HWBgqyaiWfpAU2hKZzToh1vNXoCe11FPiOyeXhU4m8DyPKnRqtI97DCXYXjuxJk3ah1UOS24JC9hc%2Fl8fE05OF%2BQ%2BOFm0taBVMj14RSf8Gkph4eIGPPE9v3ol0fsNIuUXTKesC5ReqMml948g2v9FxnNSwNPA7itIS4lonqUqRWl7ay%2BQyLZF4it9N4I11v%2FAC5sFWEHIFF8SFRYgx7xHVDTVwsk%2Bo2wrW8q1FQxliaaTyEfblUSbF9ep51c8A6pdeohNzGgT9aOsClsdeLVSG96fPnQJwwJZtI8DoWpWXpuodq39cc4437bHZpHiWv4DR4B559bHYKoDH9uutjHojone7xOGIEGWbH6bjudyiBdXpAJFh%2FGzMVMK316bwGOqUBK%2BDh29V8WYHWLaDHgz48CIk5BTFoYGuWXk91DANH52Fkt0Gl5MQRwPuAedYz2MxqbPBqYu%2BtjBLS7owgIQf13sDIjEb5AvWI5R9uRWKkKM9rM5Oquirk7A0uVfIYy3hcmO%2BPdRhSUsmiabhfee95Wbru1SB4%2FfT7U%2BBfUjOc7DdTYaJAWl1zEKzeQrj7A%2F4Lt1o8010rHQ7geRS75sNnNNLAFI3p&X-Amz-Signature=dc931e29a09fdeaa5c550ecaa26004c09bdea66f2f86097dba3029e9e20387bc&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYS7VHL6%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCHH7brwNLjIRgB43H6BX8bR5BalMf69Ym9P0HShnFfJwIgeL2I8Lkl4rl3LaYwkyTzoBtbHbBqCD0xiro09M23ek8qiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ9Bfve84cHVuW1w6SrcA%2FCslKNSPQxxTxxNTTvl6aZbi0qtfZq3bn0rxmUSvGzR8Ep7oIPnpQu8EfzcMqtb8bxZJuzZnERQTR0DH9YX8%2FIEsgkJHfPF6F7mlSj68FIvYIO%2FzPdAhK2kBj6Tj3jf3WLs1aJ7%2BKS1F0n6wnlJtcxoWdkdzRn8Uzm6DuFtsraQn1rNAr4uMzoxcFf4ZdbOsbVUZ0a6lAaLdhmBcH%2B7KWlxkSGeCRs8lYDDTCpUmikbyNtA9QhgXtFpBaT4ia4wa7N70HWBgqyaiWfpAU2hKZzToh1vNXoCe11FPiOyeXhU4m8DyPKnRqtI97DCXYXjuxJk3ah1UOS24JC9hc%2Fl8fE05OF%2BQ%2BOFm0taBVMj14RSf8Gkph4eIGPPE9v3ol0fsNIuUXTKesC5ReqMml948g2v9FxnNSwNPA7itIS4lonqUqRWl7ay%2BQyLZF4it9N4I11v%2FAC5sFWEHIFF8SFRYgx7xHVDTVwsk%2Bo2wrW8q1FQxliaaTyEfblUSbF9ep51c8A6pdeohNzGgT9aOsClsdeLVSG96fPnQJwwJZtI8DoWpWXpuodq39cc4437bHZpHiWv4DR4B559bHYKoDH9uutjHojone7xOGIEGWbH6bjudyiBdXpAJFh%2FGzMVMK316bwGOqUBK%2BDh29V8WYHWLaDHgz48CIk5BTFoYGuWXk91DANH52Fkt0Gl5MQRwPuAedYz2MxqbPBqYu%2BtjBLS7owgIQf13sDIjEb5AvWI5R9uRWKkKM9rM5Oquirk7A0uVfIYy3hcmO%2BPdRhSUsmiabhfee95Wbru1SB4%2FfT7U%2BBfUjOc7DdTYaJAWl1zEKzeQrj7A%2F4Lt1o8010rHQ7geRS75sNnNNLAFI3p&X-Amz-Signature=bdc999628254058c185ed1bb6aff20943d5da26ef48c560f5bcf1e99ee4146ae&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
