

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T25X5GCB%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJHMEUCIQCToiTjIhQMjZRoBOU4QMHgryrcIhNUpfxI86axxH9YaAIgV%2BYotMkf7v4S%2BFsekSWC8YWmCWolV7eKtwZRUCjK1zAq%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDARM1dqz%2BwazTQyP9CrcAz2MRQtG3%2BjqUUEz9l%2BskM9t2xZZ%2FuE8%2BTi%2B2HUjQiwLAv8QdC0ZvLGkrWhYJukH97H2qMJZIq68f240FWQmPiEtauo10PRLVP1OdyKeRMbY3b3ik77LX0F0fbIDR5Hw5sOXVFIdBArrpzlG5yF%2FkJYGyWqYwsntOaxl199MXlzADAXGVu9BjR0dBsB3K6hs%2FISj0f49m32UiX1TXQQZY943fMAQgKqqbFt3EZA%2B8mE73dP4ivQ%2B4Duk8OXxF1cbr1lnpk%2BsBaSl%2BWde8WS94wDX2j6cFUV%2B7xXOBl2WgLYg1kuEKGP17O0%2F9u42wBUlFIXQ4NdUmJP4%2BjVa3i0%2B50cV0IcC7X3G81K7Omu89JstSb04052%2FlMZQYu9RYHIH1ViXFbJTHEpT%2FKYy5J4TB0Q1RH5%2FG5jB%2BZsXS8HCerbpwXR7cJknkABTjcNIbhL8ifOKZ65N3fcltSMXjf%2BaFexYnPivtWZ0Rrm09EOfTCxWxk25WaQ9kwUqrHMrUj1m%2Fl8ASFIONVwPxFH4iiRvTcD9PrjrjxIG%2FxhPONo1rUgJ%2FB%2FlBpcyXUHGiycrk%2FCPXt%2BXBMt6Hd5cuy79bd0sC7W2GGHuUPTlJ6LLW3Wsj42gh3ozvi2FWTo9v307MMC0kb0GOqUBYUguy%2F27kefYtMgKtvQ0L48TPoklaYGLV9lhJWkPgyGaS9kkms946Z18dbtyfqtcVABdmI6%2FVHimytqzVMqEq%2FdJiMaHZ4EQ4oKpAQEmGLOD5hSJbxBEkhTK5d%2BVXWGibq64BaBysl1C27b7hrbGBlRJZo%2BW2ukDdyxFeheOO1Xr6uFLAk3fqRdVha627vIgzVlnnZejp6dNtEBmYmIR%2Bjv%2FMInZ&X-Amz-Signature=16ad305e45c369c3af24e9af00a3de03faced05349b16670f62e07f2a6e6508a&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T25X5GCB%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJHMEUCIQCToiTjIhQMjZRoBOU4QMHgryrcIhNUpfxI86axxH9YaAIgV%2BYotMkf7v4S%2BFsekSWC8YWmCWolV7eKtwZRUCjK1zAq%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDARM1dqz%2BwazTQyP9CrcAz2MRQtG3%2BjqUUEz9l%2BskM9t2xZZ%2FuE8%2BTi%2B2HUjQiwLAv8QdC0ZvLGkrWhYJukH97H2qMJZIq68f240FWQmPiEtauo10PRLVP1OdyKeRMbY3b3ik77LX0F0fbIDR5Hw5sOXVFIdBArrpzlG5yF%2FkJYGyWqYwsntOaxl199MXlzADAXGVu9BjR0dBsB3K6hs%2FISj0f49m32UiX1TXQQZY943fMAQgKqqbFt3EZA%2B8mE73dP4ivQ%2B4Duk8OXxF1cbr1lnpk%2BsBaSl%2BWde8WS94wDX2j6cFUV%2B7xXOBl2WgLYg1kuEKGP17O0%2F9u42wBUlFIXQ4NdUmJP4%2BjVa3i0%2B50cV0IcC7X3G81K7Omu89JstSb04052%2FlMZQYu9RYHIH1ViXFbJTHEpT%2FKYy5J4TB0Q1RH5%2FG5jB%2BZsXS8HCerbpwXR7cJknkABTjcNIbhL8ifOKZ65N3fcltSMXjf%2BaFexYnPivtWZ0Rrm09EOfTCxWxk25WaQ9kwUqrHMrUj1m%2Fl8ASFIONVwPxFH4iiRvTcD9PrjrjxIG%2FxhPONo1rUgJ%2FB%2FlBpcyXUHGiycrk%2FCPXt%2BXBMt6Hd5cuy79bd0sC7W2GGHuUPTlJ6LLW3Wsj42gh3ozvi2FWTo9v307MMC0kb0GOqUBYUguy%2F27kefYtMgKtvQ0L48TPoklaYGLV9lhJWkPgyGaS9kkms946Z18dbtyfqtcVABdmI6%2FVHimytqzVMqEq%2FdJiMaHZ4EQ4oKpAQEmGLOD5hSJbxBEkhTK5d%2BVXWGibq64BaBysl1C27b7hrbGBlRJZo%2BW2ukDdyxFeheOO1Xr6uFLAk3fqRdVha627vIgzVlnnZejp6dNtEBmYmIR%2Bjv%2FMInZ&X-Amz-Signature=d26c5e9bf79f0743f4918d57e942d52ec0bf364e0e0a1c4b66e4bf1b35d96334&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T25X5GCB%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJHMEUCIQCToiTjIhQMjZRoBOU4QMHgryrcIhNUpfxI86axxH9YaAIgV%2BYotMkf7v4S%2BFsekSWC8YWmCWolV7eKtwZRUCjK1zAq%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDARM1dqz%2BwazTQyP9CrcAz2MRQtG3%2BjqUUEz9l%2BskM9t2xZZ%2FuE8%2BTi%2B2HUjQiwLAv8QdC0ZvLGkrWhYJukH97H2qMJZIq68f240FWQmPiEtauo10PRLVP1OdyKeRMbY3b3ik77LX0F0fbIDR5Hw5sOXVFIdBArrpzlG5yF%2FkJYGyWqYwsntOaxl199MXlzADAXGVu9BjR0dBsB3K6hs%2FISj0f49m32UiX1TXQQZY943fMAQgKqqbFt3EZA%2B8mE73dP4ivQ%2B4Duk8OXxF1cbr1lnpk%2BsBaSl%2BWde8WS94wDX2j6cFUV%2B7xXOBl2WgLYg1kuEKGP17O0%2F9u42wBUlFIXQ4NdUmJP4%2BjVa3i0%2B50cV0IcC7X3G81K7Omu89JstSb04052%2FlMZQYu9RYHIH1ViXFbJTHEpT%2FKYy5J4TB0Q1RH5%2FG5jB%2BZsXS8HCerbpwXR7cJknkABTjcNIbhL8ifOKZ65N3fcltSMXjf%2BaFexYnPivtWZ0Rrm09EOfTCxWxk25WaQ9kwUqrHMrUj1m%2Fl8ASFIONVwPxFH4iiRvTcD9PrjrjxIG%2FxhPONo1rUgJ%2FB%2FlBpcyXUHGiycrk%2FCPXt%2BXBMt6Hd5cuy79bd0sC7W2GGHuUPTlJ6LLW3Wsj42gh3ozvi2FWTo9v307MMC0kb0GOqUBYUguy%2F27kefYtMgKtvQ0L48TPoklaYGLV9lhJWkPgyGaS9kkms946Z18dbtyfqtcVABdmI6%2FVHimytqzVMqEq%2FdJiMaHZ4EQ4oKpAQEmGLOD5hSJbxBEkhTK5d%2BVXWGibq64BaBysl1C27b7hrbGBlRJZo%2BW2ukDdyxFeheOO1Xr6uFLAk3fqRdVha627vIgzVlnnZejp6dNtEBmYmIR%2Bjv%2FMInZ&X-Amz-Signature=bc0bf95cffc3e565fe3fee894bd77ffbc5800445da7c7011d67e3ca6b8bd69c2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663WXPWZZN%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJHMEUCICu8HLmsCM8DNZCIuX5%2Bu%2FT9P339cEydfdNYg10LmdWJAiEA%2BC1WcZj5RyGl%2FacIvj2dZ9kpFHUl6Evv9UVO6tfcDC4q%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDK1%2F2dDh4qtSza9MTyrcAx2XRhQuJnwGNyvxn56xIf7C5tYHaCJ0cOKCP79mNb6%2FR7%2B5eiGWO6Y58%2BrWjxT%2FRGVEvNwvm3fysqejeUy5wTp00sueKKLAH1rN1N6VwhVQg%2FI0HiEtKGnq0kQZNVzBzGcWWnb2iC5aJuJDSHOK%2FPMEs1Wms9t8AE8JOa%2FxFs9eeMkVCUe78ePmTHoy2d1zrW8jPtAQJCMj%2FpQBMggXlWtwZx5ITfxmQxchlGWqq3aPqGdKCRyVXKcpwkCfp7%2BBLM%2Flc9VbZh%2Fk41MG3oCoKymbrETocZw2SrTzI6T9vkCV9gsXQLIw9B5wO%2BVcac1f%2BbK9B4F7AfSBc8owataEzw8kHa%2BLWxThQldZ1fRLQgEPIFMdNFoIZkM%2BeafQVxaQh19unQhsRAge%2BgxOFLv4%2Fgi%2ByfqQwaO3jY90vlBok2yrQCH48o%2FA%2FFoGibGOwRLu3DQg%2FXBRlxG0VLlhg8hIYcVSnlNfGhjAX6HkzxUPkEXgYrQrpzpM64zdOtDov6apyOFN836gSPb1d5IQ7KOshxMHUQrA6Pw5Ry5pDCQJIJf39Ua%2FDfeHeR79IaF32qSWnIvMFDLrpMI6kk4KV7n7%2BwyEEB49VDX%2Fh6h0HdWPlTgvWxwHTdRUHoLE51X3MM%2B1kb0GOqUBxQTd0PXIOaGWK%2B%2BL11vwHzCe%2FVHnQVl3WqafuiR2y%2F5md%2Fhl82SCLHqLKZ6k84sygZsZT0ohaj8g4EVx2OqdBMsil5oL8FlqHyJH3SPvYCsCKOBMOYyDlz%2BWGz21%2B0u50gMr5lKbUjxwz1b%2BOGxAV2gQJAMSW09ZCGYz7H4rDm6Ei4%2BIms4Lu8cFzep249eR2E7iQg53J%2FmvLnk5w82Swtg8OOcC&X-Amz-Signature=003a19cc62e2f023ca79999e86a0d65ac2bd7862be6a32f6a9bc5e143a9186a8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YQFWQPSK%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJHMEUCIFauLTOI9UHhnGmdCZvH5o6a8zFszXJ%2FE5VAhhsB%2FoUHAiEA1xmT5%2BW1hfVfUwZXmObKJNxNLm7oIRNpCGwz6docrngq%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDLj2scq%2BdKagUbhuLircA48ElvpXfQaaXEzpCz2dsbaJQhShTnWV5kjx108crIgyIPFNQUBgFRPsnFTSsnHEamIEbEiOMfAQoSeSIa3C1aNFhF7BxpOcpm7zvF9TOu7yIPyra1mU%2BiGiy6ZyVq9CnrRT6fcM6M7o56cY8gisaJBxw6zLrmkk%2FmG0hFioxEnOhIkKM8gtdTjTPWzclcv1EMY2iiRuSyzI%2FHw0C8LlzlDbbvoJ2SGH9IIz%2FgvfR8Emb0HVnp3XU7hc241rQyBtEqB6PB86%2BYL8W%2F51yK1mWNCMjPqmf1RVGopzWIMvU6Jg%2FSQWM0GGQdpzmh%2F0IgjdAFLBLbZqEgS19Xyb%2FV5fu91lenP9%2FR0teaTXCDJdm9log6Ur3qbhvuoazSnViWcamqqC0Erak22OuvoTvQRhSok98nJ4Mgqgiytjzuyc9NDiV586e1W%2FmrTzlAc8nFs7%2BGfMzlBrbVVDf%2FAHPrk1Wl477V8ZQxAmu4mJ1ybAr2SgOdGm15GJHhAjUXBoIW9JcsTg3rucaDjTYKE2lSNKUo4q4Vh5Gm68ginQVV3sbB1ney1gU1jki64CBKK4G6BAfn%2FslTlSPhgHLMleSCkHzRQxKkhda83vt5uNrlohC2NVyAjnDpIZoBWxoS9fMMC0kb0GOqUBiwathAhstILNG8oOt3k6V%2BuTwBvhxui4sUpsXQrAZaU7dQSsNxlOcyRY9%2FpgPaQLn7fYJ%2BWEkk3A6X28p2VQ%2F3cF6bz%2FLPpvPVvKCxjfN755FpokWaf4akkLSJ9lmHDPn3rr3%2F6guE6TG7u5LEcD2ytBf891KXemWF9ZN%2FjZFzP%2F4DzLzkZ4gasZLZbi9WeSl%2Fhw3TsY4qACJz8ZBSzv5fie8N7H&X-Amz-Signature=d8201b2db8fafb151b2193083aea0c1afb51870235e0530d5f435a7761b7513f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T25X5GCB%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJHMEUCIQCToiTjIhQMjZRoBOU4QMHgryrcIhNUpfxI86axxH9YaAIgV%2BYotMkf7v4S%2BFsekSWC8YWmCWolV7eKtwZRUCjK1zAq%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDARM1dqz%2BwazTQyP9CrcAz2MRQtG3%2BjqUUEz9l%2BskM9t2xZZ%2FuE8%2BTi%2B2HUjQiwLAv8QdC0ZvLGkrWhYJukH97H2qMJZIq68f240FWQmPiEtauo10PRLVP1OdyKeRMbY3b3ik77LX0F0fbIDR5Hw5sOXVFIdBArrpzlG5yF%2FkJYGyWqYwsntOaxl199MXlzADAXGVu9BjR0dBsB3K6hs%2FISj0f49m32UiX1TXQQZY943fMAQgKqqbFt3EZA%2B8mE73dP4ivQ%2B4Duk8OXxF1cbr1lnpk%2BsBaSl%2BWde8WS94wDX2j6cFUV%2B7xXOBl2WgLYg1kuEKGP17O0%2F9u42wBUlFIXQ4NdUmJP4%2BjVa3i0%2B50cV0IcC7X3G81K7Omu89JstSb04052%2FlMZQYu9RYHIH1ViXFbJTHEpT%2FKYy5J4TB0Q1RH5%2FG5jB%2BZsXS8HCerbpwXR7cJknkABTjcNIbhL8ifOKZ65N3fcltSMXjf%2BaFexYnPivtWZ0Rrm09EOfTCxWxk25WaQ9kwUqrHMrUj1m%2Fl8ASFIONVwPxFH4iiRvTcD9PrjrjxIG%2FxhPONo1rUgJ%2FB%2FlBpcyXUHGiycrk%2FCPXt%2BXBMt6Hd5cuy79bd0sC7W2GGHuUPTlJ6LLW3Wsj42gh3ozvi2FWTo9v307MMC0kb0GOqUBYUguy%2F27kefYtMgKtvQ0L48TPoklaYGLV9lhJWkPgyGaS9kkms946Z18dbtyfqtcVABdmI6%2FVHimytqzVMqEq%2FdJiMaHZ4EQ4oKpAQEmGLOD5hSJbxBEkhTK5d%2BVXWGibq64BaBysl1C27b7hrbGBlRJZo%2BW2ukDdyxFeheOO1Xr6uFLAk3fqRdVha627vIgzVlnnZejp6dNtEBmYmIR%2Bjv%2FMInZ&X-Amz-Signature=daa6dab5672f147bf18ad6d469f5547d63a96cf4526e22a2c88c60a513e62a61&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T25X5GCB%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJHMEUCIQCToiTjIhQMjZRoBOU4QMHgryrcIhNUpfxI86axxH9YaAIgV%2BYotMkf7v4S%2BFsekSWC8YWmCWolV7eKtwZRUCjK1zAq%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDARM1dqz%2BwazTQyP9CrcAz2MRQtG3%2BjqUUEz9l%2BskM9t2xZZ%2FuE8%2BTi%2B2HUjQiwLAv8QdC0ZvLGkrWhYJukH97H2qMJZIq68f240FWQmPiEtauo10PRLVP1OdyKeRMbY3b3ik77LX0F0fbIDR5Hw5sOXVFIdBArrpzlG5yF%2FkJYGyWqYwsntOaxl199MXlzADAXGVu9BjR0dBsB3K6hs%2FISj0f49m32UiX1TXQQZY943fMAQgKqqbFt3EZA%2B8mE73dP4ivQ%2B4Duk8OXxF1cbr1lnpk%2BsBaSl%2BWde8WS94wDX2j6cFUV%2B7xXOBl2WgLYg1kuEKGP17O0%2F9u42wBUlFIXQ4NdUmJP4%2BjVa3i0%2B50cV0IcC7X3G81K7Omu89JstSb04052%2FlMZQYu9RYHIH1ViXFbJTHEpT%2FKYy5J4TB0Q1RH5%2FG5jB%2BZsXS8HCerbpwXR7cJknkABTjcNIbhL8ifOKZ65N3fcltSMXjf%2BaFexYnPivtWZ0Rrm09EOfTCxWxk25WaQ9kwUqrHMrUj1m%2Fl8ASFIONVwPxFH4iiRvTcD9PrjrjxIG%2FxhPONo1rUgJ%2FB%2FlBpcyXUHGiycrk%2FCPXt%2BXBMt6Hd5cuy79bd0sC7W2GGHuUPTlJ6LLW3Wsj42gh3ozvi2FWTo9v307MMC0kb0GOqUBYUguy%2F27kefYtMgKtvQ0L48TPoklaYGLV9lhJWkPgyGaS9kkms946Z18dbtyfqtcVABdmI6%2FVHimytqzVMqEq%2FdJiMaHZ4EQ4oKpAQEmGLOD5hSJbxBEkhTK5d%2BVXWGibq64BaBysl1C27b7hrbGBlRJZo%2BW2ukDdyxFeheOO1Xr6uFLAk3fqRdVha627vIgzVlnnZejp6dNtEBmYmIR%2Bjv%2FMInZ&X-Amz-Signature=7c708f03d25aa0ef09cae8ac0d025bb7819a2b37559f08fc0c58f23ec760cd47&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T25X5GCB%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJHMEUCIQCToiTjIhQMjZRoBOU4QMHgryrcIhNUpfxI86axxH9YaAIgV%2BYotMkf7v4S%2BFsekSWC8YWmCWolV7eKtwZRUCjK1zAq%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDARM1dqz%2BwazTQyP9CrcAz2MRQtG3%2BjqUUEz9l%2BskM9t2xZZ%2FuE8%2BTi%2B2HUjQiwLAv8QdC0ZvLGkrWhYJukH97H2qMJZIq68f240FWQmPiEtauo10PRLVP1OdyKeRMbY3b3ik77LX0F0fbIDR5Hw5sOXVFIdBArrpzlG5yF%2FkJYGyWqYwsntOaxl199MXlzADAXGVu9BjR0dBsB3K6hs%2FISj0f49m32UiX1TXQQZY943fMAQgKqqbFt3EZA%2B8mE73dP4ivQ%2B4Duk8OXxF1cbr1lnpk%2BsBaSl%2BWde8WS94wDX2j6cFUV%2B7xXOBl2WgLYg1kuEKGP17O0%2F9u42wBUlFIXQ4NdUmJP4%2BjVa3i0%2B50cV0IcC7X3G81K7Omu89JstSb04052%2FlMZQYu9RYHIH1ViXFbJTHEpT%2FKYy5J4TB0Q1RH5%2FG5jB%2BZsXS8HCerbpwXR7cJknkABTjcNIbhL8ifOKZ65N3fcltSMXjf%2BaFexYnPivtWZ0Rrm09EOfTCxWxk25WaQ9kwUqrHMrUj1m%2Fl8ASFIONVwPxFH4iiRvTcD9PrjrjxIG%2FxhPONo1rUgJ%2FB%2FlBpcyXUHGiycrk%2FCPXt%2BXBMt6Hd5cuy79bd0sC7W2GGHuUPTlJ6LLW3Wsj42gh3ozvi2FWTo9v307MMC0kb0GOqUBYUguy%2F27kefYtMgKtvQ0L48TPoklaYGLV9lhJWkPgyGaS9kkms946Z18dbtyfqtcVABdmI6%2FVHimytqzVMqEq%2FdJiMaHZ4EQ4oKpAQEmGLOD5hSJbxBEkhTK5d%2BVXWGibq64BaBysl1C27b7hrbGBlRJZo%2BW2ukDdyxFeheOO1Xr6uFLAk3fqRdVha627vIgzVlnnZejp6dNtEBmYmIR%2Bjv%2FMInZ&X-Amz-Signature=44abaa12fb69329611c4b3f5b0deeafed2dbb42f6acae7e5bd2216747e445e4e&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T25X5GCB%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJHMEUCIQCToiTjIhQMjZRoBOU4QMHgryrcIhNUpfxI86axxH9YaAIgV%2BYotMkf7v4S%2BFsekSWC8YWmCWolV7eKtwZRUCjK1zAq%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDARM1dqz%2BwazTQyP9CrcAz2MRQtG3%2BjqUUEz9l%2BskM9t2xZZ%2FuE8%2BTi%2B2HUjQiwLAv8QdC0ZvLGkrWhYJukH97H2qMJZIq68f240FWQmPiEtauo10PRLVP1OdyKeRMbY3b3ik77LX0F0fbIDR5Hw5sOXVFIdBArrpzlG5yF%2FkJYGyWqYwsntOaxl199MXlzADAXGVu9BjR0dBsB3K6hs%2FISj0f49m32UiX1TXQQZY943fMAQgKqqbFt3EZA%2B8mE73dP4ivQ%2B4Duk8OXxF1cbr1lnpk%2BsBaSl%2BWde8WS94wDX2j6cFUV%2B7xXOBl2WgLYg1kuEKGP17O0%2F9u42wBUlFIXQ4NdUmJP4%2BjVa3i0%2B50cV0IcC7X3G81K7Omu89JstSb04052%2FlMZQYu9RYHIH1ViXFbJTHEpT%2FKYy5J4TB0Q1RH5%2FG5jB%2BZsXS8HCerbpwXR7cJknkABTjcNIbhL8ifOKZ65N3fcltSMXjf%2BaFexYnPivtWZ0Rrm09EOfTCxWxk25WaQ9kwUqrHMrUj1m%2Fl8ASFIONVwPxFH4iiRvTcD9PrjrjxIG%2FxhPONo1rUgJ%2FB%2FlBpcyXUHGiycrk%2FCPXt%2BXBMt6Hd5cuy79bd0sC7W2GGHuUPTlJ6LLW3Wsj42gh3ozvi2FWTo9v307MMC0kb0GOqUBYUguy%2F27kefYtMgKtvQ0L48TPoklaYGLV9lhJWkPgyGaS9kkms946Z18dbtyfqtcVABdmI6%2FVHimytqzVMqEq%2FdJiMaHZ4EQ4oKpAQEmGLOD5hSJbxBEkhTK5d%2BVXWGibq64BaBysl1C27b7hrbGBlRJZo%2BW2ukDdyxFeheOO1Xr6uFLAk3fqRdVha627vIgzVlnnZejp6dNtEBmYmIR%2Bjv%2FMInZ&X-Amz-Signature=db000e3d61c0f1f1f0d2c7a6663b39baaadb9b40f6912069f06d70ba2f875908&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
