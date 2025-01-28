

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663X7WUYH%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIGMJwmR%2BQ%2FwMZ5slDNJrcsO9ebbFItvgIys54ZuLYTJPAiEAjC3F%2BCwgTBC65Ika35hq9rbo4rq2oEneicdqFOntXdgq%2FwMIfBAAGgw2Mzc0MjMxODM4MDUiDAvcsKSggoSMqxmUrircAwV0NaDjwZWyY2oGf4bJL3WYS6CyVuG60V8QE%2BhuAfDP8uxd0nX9kvGiXDM2ixnkVZqCdCtCSg5PGhqA3eTbE90T%2BiA0bf6m9X3YIRdZqFHOBLkOAwXWAh7oeI4aDJ8Hp4DxnbCEx8bZgtkpLV3xXefRZwM5nr24FS%2B%2FYyWz4u6hOjCvXCvMwvzHZEqUrMzXa%2B1E1koxUkNuzeFLneVP1v3DA13gk3s9H7EQexKqHH14wxmqUX1EZhyi8%2B8qCmk6hHHt2mNhw6wkLehZxAZU05XpotkNXXCLX7lXboexoWvnzrF7M48cOaex6o3mS10UqB2IEeHlfklGUNmMFag2nW%2FoEHFqmI4b%2BQyGC6IbK%2BkyCUfDIrkqoNeODUHOABE5mfRAKaHtmfWRwDFxRyJn%2FI6hx06Y1oGSk4X32xfQt4rzF%2FsVJMDaBLWGcTYmp3CVy29fxshHz1mC9%2BgJ0DSWxcEU81jXV94kub%2F77sLItQCoaaqup6hl5U2ZlO3c%2B5rnAT81s2DUkMSMEfXZxbvNSISfz2UyShwjHnMqvB1%2FOBe%2F1BfJFUrNpPJxuWXtRqCZS%2FXV9IccCQAJ2hMn2GvyMg2ldMuinRMwj%2BHr%2BZSgAI9vuyOfHraUnJ0NsZezMLrh5LwGOqUBXiXRluqwedw8VsPM1iDkUynVmMaHlCYzeBXDYTaHmt4Wz8uuSXArUVhk4avFlkzyx76zX5tEJaBj86W1ho9apQeKx9g0ER3%2FAPSlVbj8p2XUbWNd3NHmMX0EKMKLrOSZFt6yYgiNnMRzbUUrnhSMfOEawRm%2Bxlfps%2FUdYr96pM7ejhDCl1EJqoeI%2BvtvrUOQXyLHdlJ6ptXEuEHsWiKXrNmyc%2FQ9&X-Amz-Signature=2be0e9be7c314eacb31807c3f1750a8b606968d26f269d9f1ea595ad92a23414&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663X7WUYH%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIGMJwmR%2BQ%2FwMZ5slDNJrcsO9ebbFItvgIys54ZuLYTJPAiEAjC3F%2BCwgTBC65Ika35hq9rbo4rq2oEneicdqFOntXdgq%2FwMIfBAAGgw2Mzc0MjMxODM4MDUiDAvcsKSggoSMqxmUrircAwV0NaDjwZWyY2oGf4bJL3WYS6CyVuG60V8QE%2BhuAfDP8uxd0nX9kvGiXDM2ixnkVZqCdCtCSg5PGhqA3eTbE90T%2BiA0bf6m9X3YIRdZqFHOBLkOAwXWAh7oeI4aDJ8Hp4DxnbCEx8bZgtkpLV3xXefRZwM5nr24FS%2B%2FYyWz4u6hOjCvXCvMwvzHZEqUrMzXa%2B1E1koxUkNuzeFLneVP1v3DA13gk3s9H7EQexKqHH14wxmqUX1EZhyi8%2B8qCmk6hHHt2mNhw6wkLehZxAZU05XpotkNXXCLX7lXboexoWvnzrF7M48cOaex6o3mS10UqB2IEeHlfklGUNmMFag2nW%2FoEHFqmI4b%2BQyGC6IbK%2BkyCUfDIrkqoNeODUHOABE5mfRAKaHtmfWRwDFxRyJn%2FI6hx06Y1oGSk4X32xfQt4rzF%2FsVJMDaBLWGcTYmp3CVy29fxshHz1mC9%2BgJ0DSWxcEU81jXV94kub%2F77sLItQCoaaqup6hl5U2ZlO3c%2B5rnAT81s2DUkMSMEfXZxbvNSISfz2UyShwjHnMqvB1%2FOBe%2F1BfJFUrNpPJxuWXtRqCZS%2FXV9IccCQAJ2hMn2GvyMg2ldMuinRMwj%2BHr%2BZSgAI9vuyOfHraUnJ0NsZezMLrh5LwGOqUBXiXRluqwedw8VsPM1iDkUynVmMaHlCYzeBXDYTaHmt4Wz8uuSXArUVhk4avFlkzyx76zX5tEJaBj86W1ho9apQeKx9g0ER3%2FAPSlVbj8p2XUbWNd3NHmMX0EKMKLrOSZFt6yYgiNnMRzbUUrnhSMfOEawRm%2Bxlfps%2FUdYr96pM7ejhDCl1EJqoeI%2BvtvrUOQXyLHdlJ6ptXEuEHsWiKXrNmyc%2FQ9&X-Amz-Signature=0b29cb9cc86ac5d75b324c8242c3a3df938bfdd549f05d8be67ba4185e87884e&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663X7WUYH%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIGMJwmR%2BQ%2FwMZ5slDNJrcsO9ebbFItvgIys54ZuLYTJPAiEAjC3F%2BCwgTBC65Ika35hq9rbo4rq2oEneicdqFOntXdgq%2FwMIfBAAGgw2Mzc0MjMxODM4MDUiDAvcsKSggoSMqxmUrircAwV0NaDjwZWyY2oGf4bJL3WYS6CyVuG60V8QE%2BhuAfDP8uxd0nX9kvGiXDM2ixnkVZqCdCtCSg5PGhqA3eTbE90T%2BiA0bf6m9X3YIRdZqFHOBLkOAwXWAh7oeI4aDJ8Hp4DxnbCEx8bZgtkpLV3xXefRZwM5nr24FS%2B%2FYyWz4u6hOjCvXCvMwvzHZEqUrMzXa%2B1E1koxUkNuzeFLneVP1v3DA13gk3s9H7EQexKqHH14wxmqUX1EZhyi8%2B8qCmk6hHHt2mNhw6wkLehZxAZU05XpotkNXXCLX7lXboexoWvnzrF7M48cOaex6o3mS10UqB2IEeHlfklGUNmMFag2nW%2FoEHFqmI4b%2BQyGC6IbK%2BkyCUfDIrkqoNeODUHOABE5mfRAKaHtmfWRwDFxRyJn%2FI6hx06Y1oGSk4X32xfQt4rzF%2FsVJMDaBLWGcTYmp3CVy29fxshHz1mC9%2BgJ0DSWxcEU81jXV94kub%2F77sLItQCoaaqup6hl5U2ZlO3c%2B5rnAT81s2DUkMSMEfXZxbvNSISfz2UyShwjHnMqvB1%2FOBe%2F1BfJFUrNpPJxuWXtRqCZS%2FXV9IccCQAJ2hMn2GvyMg2ldMuinRMwj%2BHr%2BZSgAI9vuyOfHraUnJ0NsZezMLrh5LwGOqUBXiXRluqwedw8VsPM1iDkUynVmMaHlCYzeBXDYTaHmt4Wz8uuSXArUVhk4avFlkzyx76zX5tEJaBj86W1ho9apQeKx9g0ER3%2FAPSlVbj8p2XUbWNd3NHmMX0EKMKLrOSZFt6yYgiNnMRzbUUrnhSMfOEawRm%2Bxlfps%2FUdYr96pM7ejhDCl1EJqoeI%2BvtvrUOQXyLHdlJ6ptXEuEHsWiKXrNmyc%2FQ9&X-Amz-Signature=416dac5cba828fe782155d6e349ae7efe6f6030ec9895d2ef7de22ece7e00177&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GIX6KND%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIB7B00l1cPFawXLDYerJbXeeUTn1Kh%2FmOoQ4p1vynNz6AiEA5ce08x8Lj9edyUPAocPxt7DSIa0QjNwEZssHBp0GErYq%2FwMIfBAAGgw2Mzc0MjMxODM4MDUiDAZsB4j%2F%2BMXVDoUfvyrcA0hyZEbgePEvcnFQSi7YlWxGcC42%2B6I4E4881XMO0lTjHLb7D0C5bLjkRvgDE6jfOOHi0ihKSxtT6Zzau39H0oVXUqN9s1IUR7yLS1e6YblsYZNQYlYS%2Big5RliKld9GUGUXYcIGxJWsykJnskJnRcIVbYqkGB%2BMd1yEBhhK4wdN1diLh7Y4axoQ4HOYUcylcSrK9%2BbjmoPq4gUN7lyd2ptOt8r2WkQA1hzLyj8L6ZKLq3A43LIlH26PTYWvI3saV5OfwpV0BBorbvJUgSysJYS9eaNQLbHmTBTocQeH%2F829t48n6ShrmSTcizKKxp4FB5ZAdfFalRTkRCk9JUdwqmHBpVdv4O3rHIXVqIzwIUZh%2FyHYuXGuCMX2aPYVl9rrmsfmA%2FJYy2tOKVYCGKNl%2FQGOmYX7ZAQAsVUI9YA6Nwaaf9XU%2FMbdwyvHQIOq3Y3nYpuRf28bz0PZq%2FWh9go6ZSoEirE2cmFZxmww503KTk5bkmHSRxhZhC3yHSmzC8HdQnZ%2FB2iEobqRLFgYFTLzmsm6LhuTvR0iqOtk4h8nLxGqDUFmOwIzQzEVfG2CuWNKOCgPFab2Xi2GCaEMYEZZC1pP1ed2nLAhtTAtD2DZYKuYiBiAmXe2qIVPsfglMOPd5LwGOqUBFAxZFw6kHMbH1OD62AWQs6zzxJsGRcYdGt5hBaJzEQ2DDF5iIcyPY%2B7WrHOsRYPoTxEtHere%2FGfbrkaG3QwFrXisqMf%2Bg621kCT3itrv3%2Bo6bibZMbTasloL5zFvfTfyirs%2FHyH%2BZyQ7m0ERulBqHFLJ5PBk2pxmSBcuThDaxv2yFKsI4i5U%2FStpwVMpsQu%2BxJ61ysgvlJwASv9hMbdS8Nq1pcJW&X-Amz-Signature=77a40f210ebc14e846dd9e3f1eade30492c8063ba03615b9bb58832ac23fe8e3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662RPW5QJB%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIBMISEBPFbe%2Bo2DZeuXKUh6fLWXEMlAGmdakM9f1EDECAiBN1nWrUEufXEIrV9l1aJl6xeF%2FR73QtyU9xmnOdIUbfCr%2FAwh8EAAaDDYzNzQyMzE4MzgwNSIMRHhxXJ5lapUQboQgKtwDuDnY8uvPnX6kqc9WhbbpBTGZlydMZQFhdKMaPSIjUZ0vBRdpPDVNmynZgfffriHFH%2BurHr28SXeVxbBlfdD93Uq9zKaDMa33pAz2PdVLZ%2FgzS62or9DjCiopGou7kuDLGe%2FGXq41nqw1Bii6NYpW0JfK5s8B46Sks8Y0nUPfR8vbqrqO%2BB4oekKPiDi9YstqjQHpJqltmIFoBFtPJAuJdD0L2NmSpMc90q7%2BkXPGQa1qQYHWVWUCB2RhqHBELNcJ54P6HGH7zhW%2F7G05Ohk2z1LDyxtaLZyjfH9RCJ0%2FHaNzN%2BCBs7grKvPvnwyickrFNZgMiKLFWq228BeOhc943%2BvtRiFFPpvtRbKEpm7aeyg%2FQllsTfQX2yyFM44b2mcNcazKyT9lYNNEgxI8fTwpv0HL5Sg7q7aJoFbnkuivYhRZLQRfuNFFp2%2Fkjk8%2Fsb%2BnxhOOccswg7Y7TCgkmMQJCgWpE3HX5wgx4dnysHEOUHtpNnQSMtIAX7%2BOdIaJADStp3xHBaXQmdbxVtfdIsvqG4XPu02mh%2BmNlAyAD9vSF%2BsN9aAu4%2FhnT46IzB%2Fclw7A2m%2BviaS1LYdlO1rrAhynOJ%2F5iXlCc6EoXs7Vz%2B%2FMBUHQmF%2FpWt7%2BXmnzJAcw9uLkvAY6pgGW4H%2FK9xAElifYtwrmssT%2BzAI%2FXrvla4G02cd7jqreJpaiEn1DU54poWK7iZGYjo1feGlaI9N%2BUyOG8wXCyKNklPKSnn1OcC9D%2Fn952gXPzoxOlHPloHevRD3OIzwmPajqPUx9uN1vnJAvZhC2No649H%2Fe6atokNNMXuUWfuw06MiLyh4oNvt3yTInELgtgIXa%2BDfZR2l4SsO%2Fyj793LDgKngkk2n0&X-Amz-Signature=2161d1725e5b52428034c6b3b92cae721c2bdc9241033494d25c6d1febc2291c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663X7WUYH%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIGMJwmR%2BQ%2FwMZ5slDNJrcsO9ebbFItvgIys54ZuLYTJPAiEAjC3F%2BCwgTBC65Ika35hq9rbo4rq2oEneicdqFOntXdgq%2FwMIfBAAGgw2Mzc0MjMxODM4MDUiDAvcsKSggoSMqxmUrircAwV0NaDjwZWyY2oGf4bJL3WYS6CyVuG60V8QE%2BhuAfDP8uxd0nX9kvGiXDM2ixnkVZqCdCtCSg5PGhqA3eTbE90T%2BiA0bf6m9X3YIRdZqFHOBLkOAwXWAh7oeI4aDJ8Hp4DxnbCEx8bZgtkpLV3xXefRZwM5nr24FS%2B%2FYyWz4u6hOjCvXCvMwvzHZEqUrMzXa%2B1E1koxUkNuzeFLneVP1v3DA13gk3s9H7EQexKqHH14wxmqUX1EZhyi8%2B8qCmk6hHHt2mNhw6wkLehZxAZU05XpotkNXXCLX7lXboexoWvnzrF7M48cOaex6o3mS10UqB2IEeHlfklGUNmMFag2nW%2FoEHFqmI4b%2BQyGC6IbK%2BkyCUfDIrkqoNeODUHOABE5mfRAKaHtmfWRwDFxRyJn%2FI6hx06Y1oGSk4X32xfQt4rzF%2FsVJMDaBLWGcTYmp3CVy29fxshHz1mC9%2BgJ0DSWxcEU81jXV94kub%2F77sLItQCoaaqup6hl5U2ZlO3c%2B5rnAT81s2DUkMSMEfXZxbvNSISfz2UyShwjHnMqvB1%2FOBe%2F1BfJFUrNpPJxuWXtRqCZS%2FXV9IccCQAJ2hMn2GvyMg2ldMuinRMwj%2BHr%2BZSgAI9vuyOfHraUnJ0NsZezMLrh5LwGOqUBXiXRluqwedw8VsPM1iDkUynVmMaHlCYzeBXDYTaHmt4Wz8uuSXArUVhk4avFlkzyx76zX5tEJaBj86W1ho9apQeKx9g0ER3%2FAPSlVbj8p2XUbWNd3NHmMX0EKMKLrOSZFt6yYgiNnMRzbUUrnhSMfOEawRm%2Bxlfps%2FUdYr96pM7ejhDCl1EJqoeI%2BvtvrUOQXyLHdlJ6ptXEuEHsWiKXrNmyc%2FQ9&X-Amz-Signature=ddb66f985777ead61e1d1863318bbffb5ea2da27980e77f483640b98f630e575&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663X7WUYH%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIGMJwmR%2BQ%2FwMZ5slDNJrcsO9ebbFItvgIys54ZuLYTJPAiEAjC3F%2BCwgTBC65Ika35hq9rbo4rq2oEneicdqFOntXdgq%2FwMIfBAAGgw2Mzc0MjMxODM4MDUiDAvcsKSggoSMqxmUrircAwV0NaDjwZWyY2oGf4bJL3WYS6CyVuG60V8QE%2BhuAfDP8uxd0nX9kvGiXDM2ixnkVZqCdCtCSg5PGhqA3eTbE90T%2BiA0bf6m9X3YIRdZqFHOBLkOAwXWAh7oeI4aDJ8Hp4DxnbCEx8bZgtkpLV3xXefRZwM5nr24FS%2B%2FYyWz4u6hOjCvXCvMwvzHZEqUrMzXa%2B1E1koxUkNuzeFLneVP1v3DA13gk3s9H7EQexKqHH14wxmqUX1EZhyi8%2B8qCmk6hHHt2mNhw6wkLehZxAZU05XpotkNXXCLX7lXboexoWvnzrF7M48cOaex6o3mS10UqB2IEeHlfklGUNmMFag2nW%2FoEHFqmI4b%2BQyGC6IbK%2BkyCUfDIrkqoNeODUHOABE5mfRAKaHtmfWRwDFxRyJn%2FI6hx06Y1oGSk4X32xfQt4rzF%2FsVJMDaBLWGcTYmp3CVy29fxshHz1mC9%2BgJ0DSWxcEU81jXV94kub%2F77sLItQCoaaqup6hl5U2ZlO3c%2B5rnAT81s2DUkMSMEfXZxbvNSISfz2UyShwjHnMqvB1%2FOBe%2F1BfJFUrNpPJxuWXtRqCZS%2FXV9IccCQAJ2hMn2GvyMg2ldMuinRMwj%2BHr%2BZSgAI9vuyOfHraUnJ0NsZezMLrh5LwGOqUBXiXRluqwedw8VsPM1iDkUynVmMaHlCYzeBXDYTaHmt4Wz8uuSXArUVhk4avFlkzyx76zX5tEJaBj86W1ho9apQeKx9g0ER3%2FAPSlVbj8p2XUbWNd3NHmMX0EKMKLrOSZFt6yYgiNnMRzbUUrnhSMfOEawRm%2Bxlfps%2FUdYr96pM7ejhDCl1EJqoeI%2BvtvrUOQXyLHdlJ6ptXEuEHsWiKXrNmyc%2FQ9&X-Amz-Signature=fb10d50baad10043da170588c51d0ebe61838a60145dd8878c535a5534f87710&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663X7WUYH%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIGMJwmR%2BQ%2FwMZ5slDNJrcsO9ebbFItvgIys54ZuLYTJPAiEAjC3F%2BCwgTBC65Ika35hq9rbo4rq2oEneicdqFOntXdgq%2FwMIfBAAGgw2Mzc0MjMxODM4MDUiDAvcsKSggoSMqxmUrircAwV0NaDjwZWyY2oGf4bJL3WYS6CyVuG60V8QE%2BhuAfDP8uxd0nX9kvGiXDM2ixnkVZqCdCtCSg5PGhqA3eTbE90T%2BiA0bf6m9X3YIRdZqFHOBLkOAwXWAh7oeI4aDJ8Hp4DxnbCEx8bZgtkpLV3xXefRZwM5nr24FS%2B%2FYyWz4u6hOjCvXCvMwvzHZEqUrMzXa%2B1E1koxUkNuzeFLneVP1v3DA13gk3s9H7EQexKqHH14wxmqUX1EZhyi8%2B8qCmk6hHHt2mNhw6wkLehZxAZU05XpotkNXXCLX7lXboexoWvnzrF7M48cOaex6o3mS10UqB2IEeHlfklGUNmMFag2nW%2FoEHFqmI4b%2BQyGC6IbK%2BkyCUfDIrkqoNeODUHOABE5mfRAKaHtmfWRwDFxRyJn%2FI6hx06Y1oGSk4X32xfQt4rzF%2FsVJMDaBLWGcTYmp3CVy29fxshHz1mC9%2BgJ0DSWxcEU81jXV94kub%2F77sLItQCoaaqup6hl5U2ZlO3c%2B5rnAT81s2DUkMSMEfXZxbvNSISfz2UyShwjHnMqvB1%2FOBe%2F1BfJFUrNpPJxuWXtRqCZS%2FXV9IccCQAJ2hMn2GvyMg2ldMuinRMwj%2BHr%2BZSgAI9vuyOfHraUnJ0NsZezMLrh5LwGOqUBXiXRluqwedw8VsPM1iDkUynVmMaHlCYzeBXDYTaHmt4Wz8uuSXArUVhk4avFlkzyx76zX5tEJaBj86W1ho9apQeKx9g0ER3%2FAPSlVbj8p2XUbWNd3NHmMX0EKMKLrOSZFt6yYgiNnMRzbUUrnhSMfOEawRm%2Bxlfps%2FUdYr96pM7ejhDCl1EJqoeI%2BvtvrUOQXyLHdlJ6ptXEuEHsWiKXrNmyc%2FQ9&X-Amz-Signature=16f3be9b270fb9c870e0d49f5f7c397328c398581016b506b14f9fa7653770b6&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663X7WUYH%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIGMJwmR%2BQ%2FwMZ5slDNJrcsO9ebbFItvgIys54ZuLYTJPAiEAjC3F%2BCwgTBC65Ika35hq9rbo4rq2oEneicdqFOntXdgq%2FwMIfBAAGgw2Mzc0MjMxODM4MDUiDAvcsKSggoSMqxmUrircAwV0NaDjwZWyY2oGf4bJL3WYS6CyVuG60V8QE%2BhuAfDP8uxd0nX9kvGiXDM2ixnkVZqCdCtCSg5PGhqA3eTbE90T%2BiA0bf6m9X3YIRdZqFHOBLkOAwXWAh7oeI4aDJ8Hp4DxnbCEx8bZgtkpLV3xXefRZwM5nr24FS%2B%2FYyWz4u6hOjCvXCvMwvzHZEqUrMzXa%2B1E1koxUkNuzeFLneVP1v3DA13gk3s9H7EQexKqHH14wxmqUX1EZhyi8%2B8qCmk6hHHt2mNhw6wkLehZxAZU05XpotkNXXCLX7lXboexoWvnzrF7M48cOaex6o3mS10UqB2IEeHlfklGUNmMFag2nW%2FoEHFqmI4b%2BQyGC6IbK%2BkyCUfDIrkqoNeODUHOABE5mfRAKaHtmfWRwDFxRyJn%2FI6hx06Y1oGSk4X32xfQt4rzF%2FsVJMDaBLWGcTYmp3CVy29fxshHz1mC9%2BgJ0DSWxcEU81jXV94kub%2F77sLItQCoaaqup6hl5U2ZlO3c%2B5rnAT81s2DUkMSMEfXZxbvNSISfz2UyShwjHnMqvB1%2FOBe%2F1BfJFUrNpPJxuWXtRqCZS%2FXV9IccCQAJ2hMn2GvyMg2ldMuinRMwj%2BHr%2BZSgAI9vuyOfHraUnJ0NsZezMLrh5LwGOqUBXiXRluqwedw8VsPM1iDkUynVmMaHlCYzeBXDYTaHmt4Wz8uuSXArUVhk4avFlkzyx76zX5tEJaBj86W1ho9apQeKx9g0ER3%2FAPSlVbj8p2XUbWNd3NHmMX0EKMKLrOSZFt6yYgiNnMRzbUUrnhSMfOEawRm%2Bxlfps%2FUdYr96pM7ejhDCl1EJqoeI%2BvtvrUOQXyLHdlJ6ptXEuEHsWiKXrNmyc%2FQ9&X-Amz-Signature=03807e1a13ec237a285b6be8a0ddc90d35a8702aed0632875a1734985fc86343&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
