

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466433GNFB7%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQDwn2NyjzYNg2GB%2FVz9d%2BA%2BypHhD5OyijEPpuhv2vZKxAIhAN2qQqaTFOwGNyPrwnY8H4uoqjAvDb629nS6oFnLeHxiKv8DCFEQABoMNjM3NDIzMTgzODA1Igwi7P18Q7aitlcCYwMq3AM4VVGBJufZpfcObQhFubWFEj5QQLWjntT%2BGR%2FE%2B45%2BSLATPd7jke88ya2ADbnSoKBCvxOuuaVRCI6o2ZR9SrLJsZYGEjk7ox7QuYoPGVQr5%2BWbENdCZAH4PB2OMLCbStOnnpy0UTUEc4R1XlrfAVgI0t8mKrdJ8gt%2BcLzfWvO0D8rADSVRWazPgCB%2FFBrO4volQyP164ozJC2uM7dmgHqMmuR4V2%2B4QYUCf2JwXD16xHXFDrEox0D%2FbrqY5JFp%2FMhHzg0E9Xqstkd6AxLpCjL1DfRMsc7httZWET87AJiz7jRs6F8PT70J1UUXUPUqTNYmzI7nsppvxI9v9NxAbaOQN5pVYZctycB3tNMv0o4ahF9XTMxB1aGOYaBBsrXTuS93V%2FcvrLW6jpMZEP4NLNMIbz30%2FFHge%2FjW6g707dCBGbYY8H6SouebAS1%2FwUX5MNwZYS5aQh5uTRs1An5dOCwmaKAkQb4NnaQXluBhyorSsHA1raLnZvHiwGg%2FCCc4URKDrKRvVTcKLu8Cx04muHjRi18RVFbW9i1BFTINeW30V%2BmrKAgc3uTbLMqp72VWuznEhsxkgCIHeDBcMyRGbKrWyS08mpxlOvI%2Byq%2BHh5pq77lyD%2B%2FvIvPwfH2IfDDQ6o%2B9BjqkAd%2F%2FTiDHp7pc8OJf8brcIliu67vOdBL73dgWvJhQDLqInrk9ybNGapsgBLXIqkkDS6jQrUUbZTTHF2A7wasErJEVRg4rqFFOmTKG%2BliFqCROK9KQsOMj6GbRb0WFzWZnxQpgbO8cKDj1fgYMYBxRKx88IzBfVA%2Fog0ECQy3WBMycUdcM4vwGjvLssBctE68VPOdaqCGpQmluyb6WrVpIlPMJwrTI&X-Amz-Signature=a7e6e2f28cda42049133b42bb32463f4750e2f48762eb04f7ae2ef1ecce6ba8a&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466433GNFB7%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQDwn2NyjzYNg2GB%2FVz9d%2BA%2BypHhD5OyijEPpuhv2vZKxAIhAN2qQqaTFOwGNyPrwnY8H4uoqjAvDb629nS6oFnLeHxiKv8DCFEQABoMNjM3NDIzMTgzODA1Igwi7P18Q7aitlcCYwMq3AM4VVGBJufZpfcObQhFubWFEj5QQLWjntT%2BGR%2FE%2B45%2BSLATPd7jke88ya2ADbnSoKBCvxOuuaVRCI6o2ZR9SrLJsZYGEjk7ox7QuYoPGVQr5%2BWbENdCZAH4PB2OMLCbStOnnpy0UTUEc4R1XlrfAVgI0t8mKrdJ8gt%2BcLzfWvO0D8rADSVRWazPgCB%2FFBrO4volQyP164ozJC2uM7dmgHqMmuR4V2%2B4QYUCf2JwXD16xHXFDrEox0D%2FbrqY5JFp%2FMhHzg0E9Xqstkd6AxLpCjL1DfRMsc7httZWET87AJiz7jRs6F8PT70J1UUXUPUqTNYmzI7nsppvxI9v9NxAbaOQN5pVYZctycB3tNMv0o4ahF9XTMxB1aGOYaBBsrXTuS93V%2FcvrLW6jpMZEP4NLNMIbz30%2FFHge%2FjW6g707dCBGbYY8H6SouebAS1%2FwUX5MNwZYS5aQh5uTRs1An5dOCwmaKAkQb4NnaQXluBhyorSsHA1raLnZvHiwGg%2FCCc4URKDrKRvVTcKLu8Cx04muHjRi18RVFbW9i1BFTINeW30V%2BmrKAgc3uTbLMqp72VWuznEhsxkgCIHeDBcMyRGbKrWyS08mpxlOvI%2Byq%2BHh5pq77lyD%2B%2FvIvPwfH2IfDDQ6o%2B9BjqkAd%2F%2FTiDHp7pc8OJf8brcIliu67vOdBL73dgWvJhQDLqInrk9ybNGapsgBLXIqkkDS6jQrUUbZTTHF2A7wasErJEVRg4rqFFOmTKG%2BliFqCROK9KQsOMj6GbRb0WFzWZnxQpgbO8cKDj1fgYMYBxRKx88IzBfVA%2Fog0ECQy3WBMycUdcM4vwGjvLssBctE68VPOdaqCGpQmluyb6WrVpIlPMJwrTI&X-Amz-Signature=6f2b902e1acc9b46a7cc51647945508c7875dd79f44153bd7fbfbb7c419f265e&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466433GNFB7%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQDwn2NyjzYNg2GB%2FVz9d%2BA%2BypHhD5OyijEPpuhv2vZKxAIhAN2qQqaTFOwGNyPrwnY8H4uoqjAvDb629nS6oFnLeHxiKv8DCFEQABoMNjM3NDIzMTgzODA1Igwi7P18Q7aitlcCYwMq3AM4VVGBJufZpfcObQhFubWFEj5QQLWjntT%2BGR%2FE%2B45%2BSLATPd7jke88ya2ADbnSoKBCvxOuuaVRCI6o2ZR9SrLJsZYGEjk7ox7QuYoPGVQr5%2BWbENdCZAH4PB2OMLCbStOnnpy0UTUEc4R1XlrfAVgI0t8mKrdJ8gt%2BcLzfWvO0D8rADSVRWazPgCB%2FFBrO4volQyP164ozJC2uM7dmgHqMmuR4V2%2B4QYUCf2JwXD16xHXFDrEox0D%2FbrqY5JFp%2FMhHzg0E9Xqstkd6AxLpCjL1DfRMsc7httZWET87AJiz7jRs6F8PT70J1UUXUPUqTNYmzI7nsppvxI9v9NxAbaOQN5pVYZctycB3tNMv0o4ahF9XTMxB1aGOYaBBsrXTuS93V%2FcvrLW6jpMZEP4NLNMIbz30%2FFHge%2FjW6g707dCBGbYY8H6SouebAS1%2FwUX5MNwZYS5aQh5uTRs1An5dOCwmaKAkQb4NnaQXluBhyorSsHA1raLnZvHiwGg%2FCCc4URKDrKRvVTcKLu8Cx04muHjRi18RVFbW9i1BFTINeW30V%2BmrKAgc3uTbLMqp72VWuznEhsxkgCIHeDBcMyRGbKrWyS08mpxlOvI%2Byq%2BHh5pq77lyD%2B%2FvIvPwfH2IfDDQ6o%2B9BjqkAd%2F%2FTiDHp7pc8OJf8brcIliu67vOdBL73dgWvJhQDLqInrk9ybNGapsgBLXIqkkDS6jQrUUbZTTHF2A7wasErJEVRg4rqFFOmTKG%2BliFqCROK9KQsOMj6GbRb0WFzWZnxQpgbO8cKDj1fgYMYBxRKx88IzBfVA%2Fog0ECQy3WBMycUdcM4vwGjvLssBctE68VPOdaqCGpQmluyb6WrVpIlPMJwrTI&X-Amz-Signature=7e21a4fc22676b5fc788165880c1873ade35262dbf2051dbe1f441afc42dc5e0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664VTDN2A7%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJGMEQCIBjHO1YAC2ZXoye7C4lKAT8TDKiW0WiADUxLuWFWuC%2F5AiBBcsJ6SMxTb09x27lEhAxS2YhQhQr2q%2F2JkJjlido4fSr%2FAwhREAAaDDYzNzQyMzE4MzgwNSIMYq6iNa0chUwPeHPSKtwDzBXfeCtwpO0tKdBXzC4RV8Lj6aIGd84oeMnB0iOk%2BvSIEjYKUev%2FmKAuh9WP6d9kwtIGypb5kNFjYcCu%2F39CCd5%2FIfVdv2XUdFZQTxraX3IZ5S85j5Y9Q5kTpzaZIgOP6IZtl2s2YvM42MXApyEaZ02NRN5oyt6RaENYO%2Br1PLyFqUIu5TYBD8owhDN%2F57JHiymJiqjLUsMnoaKhs85RYgPQgrQz8d%2FTwvyz0Er8BYPaChC2e8dscaFq58t%2FB9KIF1UYI3ocCXkNKymsE7LJGR9ILeml6YVbW9t%2BzR9jfre2CpULtQsZHje4EjHDKMX6Lc1Ddp93WHt85cHd3emKfuP4colbtTi1JcQD%2FWl14xi3aJFa4McvrZ2qxCPJ6guJkG2dD39lt7zn%2FIOGT0AcHamdpGHEQ6G6pmik5b2AATo8Yz9OV43YKoMJ%2FMQe5i%2F2IFTuCkf5uqo9LKPsHdCSoMZBbpAd99p5eUZx4kYtZ41eHJlE33mRJEwW0KxQ2JDJQB%2FsTTcMM0SZ6s4z%2FHTtQMdFp8VFyLlppIFtauORohnHC3R33Ep0iSNN3cHdvg2AZA8xe2yxxe0DR3c1oU0%2FIRp5uztKJdO%2FfdA29yQbfgh7ThteXaZz4OySdUgwieuPvQY6pgH%2Fjl5MLB%2BxLGU1Wu%2FUV4P8SP2BV7GV6JgbxcJzsRLcDaudi9YPc9t99qXMxA05O%2F1MgL4%2BgNbokcqxIUWY%2FoS6EfMkSa9qxjYNZMcBaVx1Ruz6UdEW%2BsXKxBWuM6nswHzx5Vj2BM%2B8qQW6kGGWMtmVqy8k7YEVhL7wdYsnHTP2pfd5kpdz5RzNVuR6Pn8c9JSZJrHCsT9hWkOMXIP20R2M3KR%2BlflQ&X-Amz-Signature=bb875943066ffac82dda65e373f309494f1db870b704b95745f5ce292af0076d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGTWZUTA%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJGMEQCICaiWMyL5HYbNO%2Bs83dimCn3lTmvxuHupVIfPfFYG4utAiBNcHbSfw2%2FZF3hx7r1iphdPpM1myLh5XLYFlhy%2BiiqYyr%2FAwhREAAaDDYzNzQyMzE4MzgwNSIMMILS3tatI%2B6M15FmKtwDMpDEo3VxmYpuSRC7%2BSvl1ycC4ga3oe0JXrfrVKVCzSNkfvWSWwq1TkQFbhmxzLjt31G0Hf4RYMfpPed6eqth%2Bkx2vil8p87FVJEk3iUiiLwu3ihB7B7Y%2FraaiQtBIKlJDB%2Fhd%2BzaHT1JVXowdBBTMUIcM5OqkRPI036hHe0RRLItGbWMhrjB7GjyDd3dsanmech1J7CDi7N2oTt15FW5PvqnvNpz101o%2BL%2BDg63gHJ5ApLq6HCsBzlJJ%2FZLb7IOqXrmf8PTINY%2FmFGRN%2BzQl8DP2FLVHjNWmsDSHunKYjSzO2LsON54GKFazjlfbzFPhsC%2FjnmxiglKffCPyRhhEZIqukdd5A3j%2FdPu1Fnhrys0u3wXoGW0hDS93VQh7iEV6VnVqH7zjuxSJFBTr43RJVuZ2A%2FVwdgXzArhHDpfkPf2%2Fmoaou1u9jvNb5N8GWdc8U2w0YWL2Q68bZbxdFf%2BzAsWQBp4AIiGLP7JBHAA0BKBiIu3zEBGL1WQjR8%2FhWj2EZGgyuB%2FiGYnhv1TMi2G2jPdEaHC8yleDAMqtBJQgURHTCrS%2FO2z5TlPC3Rs32T3IYTs%2FK2DT267eXYhywQY6M5IMQo5HH3C8HLKAiA03Q0etnt6K4RJlGqNFbzsw8eqPvQY6pgGg%2B9Xjz2x85nFgKq910%2BZJj8tFszz4RKhnqQ23RFfHO3f4hP%2BpJ8eRgpEoTEHFRbXt90t%2B5AKNcOMLFzkY7NrMu9r0x5KzS9bW4rS5byJ7qokS66YKtzseqhiUhpFW%2F1z%2BTN3BDgdZbFsWczts36PUsvO3%2BpVBqI%2FCgWtns0o67IritCnzSTeqAB2zgTzIaAMqfMNkO52AHS2UjNAM55V3UShx347p&X-Amz-Signature=d7e307319e87fcad2d1b52e353c90e35cd6b113f4d129f75775ab95140e06786&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466433GNFB7%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQDwn2NyjzYNg2GB%2FVz9d%2BA%2BypHhD5OyijEPpuhv2vZKxAIhAN2qQqaTFOwGNyPrwnY8H4uoqjAvDb629nS6oFnLeHxiKv8DCFEQABoMNjM3NDIzMTgzODA1Igwi7P18Q7aitlcCYwMq3AM4VVGBJufZpfcObQhFubWFEj5QQLWjntT%2BGR%2FE%2B45%2BSLATPd7jke88ya2ADbnSoKBCvxOuuaVRCI6o2ZR9SrLJsZYGEjk7ox7QuYoPGVQr5%2BWbENdCZAH4PB2OMLCbStOnnpy0UTUEc4R1XlrfAVgI0t8mKrdJ8gt%2BcLzfWvO0D8rADSVRWazPgCB%2FFBrO4volQyP164ozJC2uM7dmgHqMmuR4V2%2B4QYUCf2JwXD16xHXFDrEox0D%2FbrqY5JFp%2FMhHzg0E9Xqstkd6AxLpCjL1DfRMsc7httZWET87AJiz7jRs6F8PT70J1UUXUPUqTNYmzI7nsppvxI9v9NxAbaOQN5pVYZctycB3tNMv0o4ahF9XTMxB1aGOYaBBsrXTuS93V%2FcvrLW6jpMZEP4NLNMIbz30%2FFHge%2FjW6g707dCBGbYY8H6SouebAS1%2FwUX5MNwZYS5aQh5uTRs1An5dOCwmaKAkQb4NnaQXluBhyorSsHA1raLnZvHiwGg%2FCCc4URKDrKRvVTcKLu8Cx04muHjRi18RVFbW9i1BFTINeW30V%2BmrKAgc3uTbLMqp72VWuznEhsxkgCIHeDBcMyRGbKrWyS08mpxlOvI%2Byq%2BHh5pq77lyD%2B%2FvIvPwfH2IfDDQ6o%2B9BjqkAd%2F%2FTiDHp7pc8OJf8brcIliu67vOdBL73dgWvJhQDLqInrk9ybNGapsgBLXIqkkDS6jQrUUbZTTHF2A7wasErJEVRg4rqFFOmTKG%2BliFqCROK9KQsOMj6GbRb0WFzWZnxQpgbO8cKDj1fgYMYBxRKx88IzBfVA%2Fog0ECQy3WBMycUdcM4vwGjvLssBctE68VPOdaqCGpQmluyb6WrVpIlPMJwrTI&X-Amz-Signature=709d24e6f88f183c1efa6ccffe71f6b578e30baadc7c29c2c6775adb786119ab&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466433GNFB7%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQDwn2NyjzYNg2GB%2FVz9d%2BA%2BypHhD5OyijEPpuhv2vZKxAIhAN2qQqaTFOwGNyPrwnY8H4uoqjAvDb629nS6oFnLeHxiKv8DCFEQABoMNjM3NDIzMTgzODA1Igwi7P18Q7aitlcCYwMq3AM4VVGBJufZpfcObQhFubWFEj5QQLWjntT%2BGR%2FE%2B45%2BSLATPd7jke88ya2ADbnSoKBCvxOuuaVRCI6o2ZR9SrLJsZYGEjk7ox7QuYoPGVQr5%2BWbENdCZAH4PB2OMLCbStOnnpy0UTUEc4R1XlrfAVgI0t8mKrdJ8gt%2BcLzfWvO0D8rADSVRWazPgCB%2FFBrO4volQyP164ozJC2uM7dmgHqMmuR4V2%2B4QYUCf2JwXD16xHXFDrEox0D%2FbrqY5JFp%2FMhHzg0E9Xqstkd6AxLpCjL1DfRMsc7httZWET87AJiz7jRs6F8PT70J1UUXUPUqTNYmzI7nsppvxI9v9NxAbaOQN5pVYZctycB3tNMv0o4ahF9XTMxB1aGOYaBBsrXTuS93V%2FcvrLW6jpMZEP4NLNMIbz30%2FFHge%2FjW6g707dCBGbYY8H6SouebAS1%2FwUX5MNwZYS5aQh5uTRs1An5dOCwmaKAkQb4NnaQXluBhyorSsHA1raLnZvHiwGg%2FCCc4URKDrKRvVTcKLu8Cx04muHjRi18RVFbW9i1BFTINeW30V%2BmrKAgc3uTbLMqp72VWuznEhsxkgCIHeDBcMyRGbKrWyS08mpxlOvI%2Byq%2BHh5pq77lyD%2B%2FvIvPwfH2IfDDQ6o%2B9BjqkAd%2F%2FTiDHp7pc8OJf8brcIliu67vOdBL73dgWvJhQDLqInrk9ybNGapsgBLXIqkkDS6jQrUUbZTTHF2A7wasErJEVRg4rqFFOmTKG%2BliFqCROK9KQsOMj6GbRb0WFzWZnxQpgbO8cKDj1fgYMYBxRKx88IzBfVA%2Fog0ECQy3WBMycUdcM4vwGjvLssBctE68VPOdaqCGpQmluyb6WrVpIlPMJwrTI&X-Amz-Signature=d0b1b25faf242cd0b701e201a1d8b7f8670b35d79ebebcd85cbf2ef6fd8aeaed&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466433GNFB7%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQDwn2NyjzYNg2GB%2FVz9d%2BA%2BypHhD5OyijEPpuhv2vZKxAIhAN2qQqaTFOwGNyPrwnY8H4uoqjAvDb629nS6oFnLeHxiKv8DCFEQABoMNjM3NDIzMTgzODA1Igwi7P18Q7aitlcCYwMq3AM4VVGBJufZpfcObQhFubWFEj5QQLWjntT%2BGR%2FE%2B45%2BSLATPd7jke88ya2ADbnSoKBCvxOuuaVRCI6o2ZR9SrLJsZYGEjk7ox7QuYoPGVQr5%2BWbENdCZAH4PB2OMLCbStOnnpy0UTUEc4R1XlrfAVgI0t8mKrdJ8gt%2BcLzfWvO0D8rADSVRWazPgCB%2FFBrO4volQyP164ozJC2uM7dmgHqMmuR4V2%2B4QYUCf2JwXD16xHXFDrEox0D%2FbrqY5JFp%2FMhHzg0E9Xqstkd6AxLpCjL1DfRMsc7httZWET87AJiz7jRs6F8PT70J1UUXUPUqTNYmzI7nsppvxI9v9NxAbaOQN5pVYZctycB3tNMv0o4ahF9XTMxB1aGOYaBBsrXTuS93V%2FcvrLW6jpMZEP4NLNMIbz30%2FFHge%2FjW6g707dCBGbYY8H6SouebAS1%2FwUX5MNwZYS5aQh5uTRs1An5dOCwmaKAkQb4NnaQXluBhyorSsHA1raLnZvHiwGg%2FCCc4URKDrKRvVTcKLu8Cx04muHjRi18RVFbW9i1BFTINeW30V%2BmrKAgc3uTbLMqp72VWuznEhsxkgCIHeDBcMyRGbKrWyS08mpxlOvI%2Byq%2BHh5pq77lyD%2B%2FvIvPwfH2IfDDQ6o%2B9BjqkAd%2F%2FTiDHp7pc8OJf8brcIliu67vOdBL73dgWvJhQDLqInrk9ybNGapsgBLXIqkkDS6jQrUUbZTTHF2A7wasErJEVRg4rqFFOmTKG%2BliFqCROK9KQsOMj6GbRb0WFzWZnxQpgbO8cKDj1fgYMYBxRKx88IzBfVA%2Fog0ECQy3WBMycUdcM4vwGjvLssBctE68VPOdaqCGpQmluyb6WrVpIlPMJwrTI&X-Amz-Signature=2adf2f849faf5a83e0f6a6a8175d1e7398b1b8178a0b422dcd2f6ed8e8f42529&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466433GNFB7%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQDwn2NyjzYNg2GB%2FVz9d%2BA%2BypHhD5OyijEPpuhv2vZKxAIhAN2qQqaTFOwGNyPrwnY8H4uoqjAvDb629nS6oFnLeHxiKv8DCFEQABoMNjM3NDIzMTgzODA1Igwi7P18Q7aitlcCYwMq3AM4VVGBJufZpfcObQhFubWFEj5QQLWjntT%2BGR%2FE%2B45%2BSLATPd7jke88ya2ADbnSoKBCvxOuuaVRCI6o2ZR9SrLJsZYGEjk7ox7QuYoPGVQr5%2BWbENdCZAH4PB2OMLCbStOnnpy0UTUEc4R1XlrfAVgI0t8mKrdJ8gt%2BcLzfWvO0D8rADSVRWazPgCB%2FFBrO4volQyP164ozJC2uM7dmgHqMmuR4V2%2B4QYUCf2JwXD16xHXFDrEox0D%2FbrqY5JFp%2FMhHzg0E9Xqstkd6AxLpCjL1DfRMsc7httZWET87AJiz7jRs6F8PT70J1UUXUPUqTNYmzI7nsppvxI9v9NxAbaOQN5pVYZctycB3tNMv0o4ahF9XTMxB1aGOYaBBsrXTuS93V%2FcvrLW6jpMZEP4NLNMIbz30%2FFHge%2FjW6g707dCBGbYY8H6SouebAS1%2FwUX5MNwZYS5aQh5uTRs1An5dOCwmaKAkQb4NnaQXluBhyorSsHA1raLnZvHiwGg%2FCCc4URKDrKRvVTcKLu8Cx04muHjRi18RVFbW9i1BFTINeW30V%2BmrKAgc3uTbLMqp72VWuznEhsxkgCIHeDBcMyRGbKrWyS08mpxlOvI%2Byq%2BHh5pq77lyD%2B%2FvIvPwfH2IfDDQ6o%2B9BjqkAd%2F%2FTiDHp7pc8OJf8brcIliu67vOdBL73dgWvJhQDLqInrk9ybNGapsgBLXIqkkDS6jQrUUbZTTHF2A7wasErJEVRg4rqFFOmTKG%2BliFqCROK9KQsOMj6GbRb0WFzWZnxQpgbO8cKDj1fgYMYBxRKx88IzBfVA%2Fog0ECQy3WBMycUdcM4vwGjvLssBctE68VPOdaqCGpQmluyb6WrVpIlPMJwrTI&X-Amz-Signature=10fd6a3a0de0aa2d35ebfc0afcc83de54a601f521ff552ac585051338c708d94&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
