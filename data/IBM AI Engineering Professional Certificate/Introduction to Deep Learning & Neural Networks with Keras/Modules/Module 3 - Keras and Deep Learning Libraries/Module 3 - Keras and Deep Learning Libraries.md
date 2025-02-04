

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y5G3KH7N%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJHMEUCID6%2FT7YvH3D%2B02TRwuAke9g3XwXLgSOkhKN9aslDq8dNAiEArh5p7KtZoRSZia%2BUmFS7VGnlh7igWLEOXLnuRUc5m1Yq%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDBapKsa8DiRSpwisuircA4G3zTsFTCGf7h88x4rmSLPksSdUwr3XeTYPUnsNOSxLJFbwCQhTnNwT97scP8BVcv6YokE%2BjpX5c7%2B6tkDmbNDK%2BN6cvYfm42DyU0JyRM6pj9SSAYojmO3ZZuGvKZC9iws7RKPD183Flw0oQAEu%2BoCSmPSOUHrqH2MZy7Nh4r0C1HKlv3VIvlAATbNu5xyCm1QtpBBGurC%2F2ZhdV9lNVfzmLB%2FJNz80c7fmXp8kOQ6woS2pgHDNboxluhcHJTaiNsZ83V2xL4oyMjnvHAOKhDzGxoT9OaQwKiUyqVb%2B8Zy02ES9RsGGLL%2FYCuyc2vyhkrX6RjRbPOWlpzrHMgbapLgtamqINgoWtYDHujcRqayIbZNZO%2B8i06gAPBN9A%2FJkwTPWxR4BirxgSJ6EJSkvX9XxoK92k74A0%2BruJVxuifQEw7B4OmpLaZwgvt26C2xdRgczQ7hA9%2BEIDPmLlf4JqqsKdeKLdPlZtxynPDTDPXoPYdwtgWK7fGi%2Bel1zQHmKUiVVRbXu1UtOWbXD4RELTHCap7l5hxAF%2BBgpq%2FWcNZ6W3qDsmxfJE0pEToaQUlD0p30OmjB5rE4hjyh%2Fm8QZCYpUaWa40CFQTd3daP4p%2F%2FLeHIo4w5b0Np6hFOFkMK69ib0GOqUBGNHTRf4WgbrnKGTbX8RBBRSQgQfkKPSIGn4M2hHJW5SN6kFJIOGkhwHV4VPvgULAm6qhsDgYVO5dhZglaFFZ18AMvuSwb1DAvRmG55jCo0NtQTl7CxwBjgf2wQM84r7fvToQfX3ybMv4pkyoIzL2%2BcTK4cv0HPCC9Fjzs6XL%2BUxxAymT4qDFxVjRMEPyWjsE38AsAKzsGoFsUf0n7bVQCzduyklf&X-Amz-Signature=1fe5b1eab925bd98a4f08e661d687770c577a506485bd5ffc017a8e232341099&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y5G3KH7N%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJHMEUCID6%2FT7YvH3D%2B02TRwuAke9g3XwXLgSOkhKN9aslDq8dNAiEArh5p7KtZoRSZia%2BUmFS7VGnlh7igWLEOXLnuRUc5m1Yq%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDBapKsa8DiRSpwisuircA4G3zTsFTCGf7h88x4rmSLPksSdUwr3XeTYPUnsNOSxLJFbwCQhTnNwT97scP8BVcv6YokE%2BjpX5c7%2B6tkDmbNDK%2BN6cvYfm42DyU0JyRM6pj9SSAYojmO3ZZuGvKZC9iws7RKPD183Flw0oQAEu%2BoCSmPSOUHrqH2MZy7Nh4r0C1HKlv3VIvlAATbNu5xyCm1QtpBBGurC%2F2ZhdV9lNVfzmLB%2FJNz80c7fmXp8kOQ6woS2pgHDNboxluhcHJTaiNsZ83V2xL4oyMjnvHAOKhDzGxoT9OaQwKiUyqVb%2B8Zy02ES9RsGGLL%2FYCuyc2vyhkrX6RjRbPOWlpzrHMgbapLgtamqINgoWtYDHujcRqayIbZNZO%2B8i06gAPBN9A%2FJkwTPWxR4BirxgSJ6EJSkvX9XxoK92k74A0%2BruJVxuifQEw7B4OmpLaZwgvt26C2xdRgczQ7hA9%2BEIDPmLlf4JqqsKdeKLdPlZtxynPDTDPXoPYdwtgWK7fGi%2Bel1zQHmKUiVVRbXu1UtOWbXD4RELTHCap7l5hxAF%2BBgpq%2FWcNZ6W3qDsmxfJE0pEToaQUlD0p30OmjB5rE4hjyh%2Fm8QZCYpUaWa40CFQTd3daP4p%2F%2FLeHIo4w5b0Np6hFOFkMK69ib0GOqUBGNHTRf4WgbrnKGTbX8RBBRSQgQfkKPSIGn4M2hHJW5SN6kFJIOGkhwHV4VPvgULAm6qhsDgYVO5dhZglaFFZ18AMvuSwb1DAvRmG55jCo0NtQTl7CxwBjgf2wQM84r7fvToQfX3ybMv4pkyoIzL2%2BcTK4cv0HPCC9Fjzs6XL%2BUxxAymT4qDFxVjRMEPyWjsE38AsAKzsGoFsUf0n7bVQCzduyklf&X-Amz-Signature=ad1acae434136491c18d573213c2352ef2c2800644c4ce417628beb78397fdbe&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y5G3KH7N%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJHMEUCID6%2FT7YvH3D%2B02TRwuAke9g3XwXLgSOkhKN9aslDq8dNAiEArh5p7KtZoRSZia%2BUmFS7VGnlh7igWLEOXLnuRUc5m1Yq%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDBapKsa8DiRSpwisuircA4G3zTsFTCGf7h88x4rmSLPksSdUwr3XeTYPUnsNOSxLJFbwCQhTnNwT97scP8BVcv6YokE%2BjpX5c7%2B6tkDmbNDK%2BN6cvYfm42DyU0JyRM6pj9SSAYojmO3ZZuGvKZC9iws7RKPD183Flw0oQAEu%2BoCSmPSOUHrqH2MZy7Nh4r0C1HKlv3VIvlAATbNu5xyCm1QtpBBGurC%2F2ZhdV9lNVfzmLB%2FJNz80c7fmXp8kOQ6woS2pgHDNboxluhcHJTaiNsZ83V2xL4oyMjnvHAOKhDzGxoT9OaQwKiUyqVb%2B8Zy02ES9RsGGLL%2FYCuyc2vyhkrX6RjRbPOWlpzrHMgbapLgtamqINgoWtYDHujcRqayIbZNZO%2B8i06gAPBN9A%2FJkwTPWxR4BirxgSJ6EJSkvX9XxoK92k74A0%2BruJVxuifQEw7B4OmpLaZwgvt26C2xdRgczQ7hA9%2BEIDPmLlf4JqqsKdeKLdPlZtxynPDTDPXoPYdwtgWK7fGi%2Bel1zQHmKUiVVRbXu1UtOWbXD4RELTHCap7l5hxAF%2BBgpq%2FWcNZ6W3qDsmxfJE0pEToaQUlD0p30OmjB5rE4hjyh%2Fm8QZCYpUaWa40CFQTd3daP4p%2F%2FLeHIo4w5b0Np6hFOFkMK69ib0GOqUBGNHTRf4WgbrnKGTbX8RBBRSQgQfkKPSIGn4M2hHJW5SN6kFJIOGkhwHV4VPvgULAm6qhsDgYVO5dhZglaFFZ18AMvuSwb1DAvRmG55jCo0NtQTl7CxwBjgf2wQM84r7fvToQfX3ybMv4pkyoIzL2%2BcTK4cv0HPCC9Fjzs6XL%2BUxxAymT4qDFxVjRMEPyWjsE38AsAKzsGoFsUf0n7bVQCzduyklf&X-Amz-Signature=4bec3947558624851d48112325af6f088ac071d208aca09a14aefafb7c56180b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666X4OUWYM%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJHMEUCIQCe2YN2VYayVFuKsQE8rq9Aqv%2BaNUUpKIKj2N80M2rk9AIgZiiS6xWGeyPpaV0lxXvCFtSVHChx5TXfAho7UP2vLEoq%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDL1qNEXT%2BNOheg3X2yrcA7nfFziBwtTEdg8W%2BuK9ZM9pnyoiNtreQG%2FMNm8%2B%2B%2F8WpyMk2DZnlUJuk9HeGsYdTmqXKlr75dnJes%2FXz6nnV%2FyAZVRtkTTVsra7CnoA%2F93xgn8ZbBYehRHhG17Mz29TcwloHpFkM6OWneGNq2FVHtyN2esBIdxYDQ%2BZYXORfWAjOVygqmwwm7%2FZihWiJIGi%2Bofcrip93xcNsIEx%2Fyd3wRc48kClK5eu7c%2F%2FDDzxt11QZHVbevHm5C52yzWAUwzKyll1NQz5g%2BEfkSp%2B%2FHPH6ylJzRlRmm4mxdcR92GQ1yHvzkCgxEL2tA%2FeYY8ImZmISMz%2FCppsjkeyLHazzcmpZ%2BCAkhyRRvoFleDRN8aTczKxjZzkwGOcCgyvGZW982A0k%2BDyF8%2FqW9VIIrFnyXcXC4Vjy5Q8kQrl1ULeCIcKGN0PU1qTFxDIPdivV5LCdmEwlTy2KcYqTJocEHAUiGeR1X%2Bd%2FJv1yV7lrYWceukONfEelocP0YVWuYuV7ZHcOcbrd3lMlqOyeYqK74AoCMtnrMMAtPKcD8JdkB%2B6etwvMmf1%2BTGV0z6xfhj8yehnnM9u1Qq1zt4RgknNhN9xY%2BJjQUFgau%2FQoPaw3sJFlYmIBlcRfRDWl4Fl12Jn5sh3MPy8ib0GOqUBH1Vhb0bQXertISFF9tSQGi5ds%2BYepwnTOnSD%2FsPv2A5f2HgfsmRTKvvFhE6pm9X%2BiTo%2FOZIE17Wq1vg%2B4R177mqzZYzudcUjctyjOXUTmUNvcvM1rJ6t7SsfuzRDcp6PxXzl2rIeoXHAoaY8qYCtIx9TQb6EDNclN0gi4QreLZ6yb4qxreCIbbFHfm%2F%2BsJ%2Fd9NrBfV26JSZCf8vC0vuyKjwpFicV&X-Amz-Signature=6215b31ee5a99a6b2b49c19327fa6b8c46622c080b6edb05ec650e409abd4045&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WDAEVJLW%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJHMEUCIQD29k8J4cDGs96Y2VX5s9GamfpMTFFZbW8hB8PJQizn0QIgQmjwEDOpVY0wby7rJ1Yd5Xming2f0VIeaKnN2bfd%2Bgwq%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDCqEZENBeSisYqip9CrcA%2F%2B7d9%2FFgmTxhU59AkDqJA8Jeh6e355roDoSbQfBvLwzqEhJ6W7Ix1JHn%2BR6tvhKKCHobrtAWoO4eUEP5%2BPoc92ji8bHH7VXoOX1uv0C5Ycwc%2BeXBIZfC51N7Bk519vsBPbn2gbYh1AWC1mVt4sG92MXPmER3rH%2B8xZM7SgCgXmeOSvdPtNLfEzvW%2B2E4qjrzdImsql6yBn23XbJ%2F4OKp3uFJe379824yEMWZUeYUSz2tIFgZhKLjw4LIX6yGNdRQFrHOo9dTo7qA8iVtwRXsc2VsROxBy2dcrivCKTPzSVSs9VfMkrGDm40UpDlD85Gq3rNi7RHE4A0FcIBtrTTTrHmv7b1ARNrRg4Atx10svmSaBSgFKGs8CJNz9qE2e9%2FHy8lMXXOEUeBJ4gRhDQZ37JyrNHLEoSnHRTWWvHnLpeHWdgsWNJh8fSmLfQCu6fNJLMAmlDjP4QpuVibGGLXXN%2Fut0LE1r9K9BoOZNYu181f9UrNJHyPvyXDDSeCRdsnQ%2FFE1NfEVVSA5Ttyv4VartWyk1lsl30tPeb3FnpD9ZI2wHS5%2BUKR3mBDx%2BVJFf7kzASmKmAyAfcBer%2FhUlAERaycVvfap%2BHOgUoecFsM%2FXDlV7VVaAVs7GxM9it8MLi9ib0GOqUBU1t007lVxk5yCMrZuqZavuLv0zb3Ad%2BSvUIIysotYJ55n9Osus5qECwr7UZ8qIUSFIHhw1%2Fvm%2FQvGG960HfwW9GhDL8pLaS%2F6%2BXbaI56KNAzV0uUkypNV30i5qudZJYrOlNnjECKmTHeBR4HMjHuAbf408C9sVxYzbXHOU5wb1U2g%2FhlDw36nF0NB1lBoTq%2BSJt75mm2Tj2SeFA7wSUew2gckIkF&X-Amz-Signature=0ec8bd2ac4fb98b34e2bf70b404b03e024b5715a03ec570755597abd8bf8c3a5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y5G3KH7N%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJHMEUCID6%2FT7YvH3D%2B02TRwuAke9g3XwXLgSOkhKN9aslDq8dNAiEArh5p7KtZoRSZia%2BUmFS7VGnlh7igWLEOXLnuRUc5m1Yq%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDBapKsa8DiRSpwisuircA4G3zTsFTCGf7h88x4rmSLPksSdUwr3XeTYPUnsNOSxLJFbwCQhTnNwT97scP8BVcv6YokE%2BjpX5c7%2B6tkDmbNDK%2BN6cvYfm42DyU0JyRM6pj9SSAYojmO3ZZuGvKZC9iws7RKPD183Flw0oQAEu%2BoCSmPSOUHrqH2MZy7Nh4r0C1HKlv3VIvlAATbNu5xyCm1QtpBBGurC%2F2ZhdV9lNVfzmLB%2FJNz80c7fmXp8kOQ6woS2pgHDNboxluhcHJTaiNsZ83V2xL4oyMjnvHAOKhDzGxoT9OaQwKiUyqVb%2B8Zy02ES9RsGGLL%2FYCuyc2vyhkrX6RjRbPOWlpzrHMgbapLgtamqINgoWtYDHujcRqayIbZNZO%2B8i06gAPBN9A%2FJkwTPWxR4BirxgSJ6EJSkvX9XxoK92k74A0%2BruJVxuifQEw7B4OmpLaZwgvt26C2xdRgczQ7hA9%2BEIDPmLlf4JqqsKdeKLdPlZtxynPDTDPXoPYdwtgWK7fGi%2Bel1zQHmKUiVVRbXu1UtOWbXD4RELTHCap7l5hxAF%2BBgpq%2FWcNZ6W3qDsmxfJE0pEToaQUlD0p30OmjB5rE4hjyh%2Fm8QZCYpUaWa40CFQTd3daP4p%2F%2FLeHIo4w5b0Np6hFOFkMK69ib0GOqUBGNHTRf4WgbrnKGTbX8RBBRSQgQfkKPSIGn4M2hHJW5SN6kFJIOGkhwHV4VPvgULAm6qhsDgYVO5dhZglaFFZ18AMvuSwb1DAvRmG55jCo0NtQTl7CxwBjgf2wQM84r7fvToQfX3ybMv4pkyoIzL2%2BcTK4cv0HPCC9Fjzs6XL%2BUxxAymT4qDFxVjRMEPyWjsE38AsAKzsGoFsUf0n7bVQCzduyklf&X-Amz-Signature=2af92963270d93fabd196b0e978a27f0eefd665611d57df60073e82092bb2490&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y5G3KH7N%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJHMEUCID6%2FT7YvH3D%2B02TRwuAke9g3XwXLgSOkhKN9aslDq8dNAiEArh5p7KtZoRSZia%2BUmFS7VGnlh7igWLEOXLnuRUc5m1Yq%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDBapKsa8DiRSpwisuircA4G3zTsFTCGf7h88x4rmSLPksSdUwr3XeTYPUnsNOSxLJFbwCQhTnNwT97scP8BVcv6YokE%2BjpX5c7%2B6tkDmbNDK%2BN6cvYfm42DyU0JyRM6pj9SSAYojmO3ZZuGvKZC9iws7RKPD183Flw0oQAEu%2BoCSmPSOUHrqH2MZy7Nh4r0C1HKlv3VIvlAATbNu5xyCm1QtpBBGurC%2F2ZhdV9lNVfzmLB%2FJNz80c7fmXp8kOQ6woS2pgHDNboxluhcHJTaiNsZ83V2xL4oyMjnvHAOKhDzGxoT9OaQwKiUyqVb%2B8Zy02ES9RsGGLL%2FYCuyc2vyhkrX6RjRbPOWlpzrHMgbapLgtamqINgoWtYDHujcRqayIbZNZO%2B8i06gAPBN9A%2FJkwTPWxR4BirxgSJ6EJSkvX9XxoK92k74A0%2BruJVxuifQEw7B4OmpLaZwgvt26C2xdRgczQ7hA9%2BEIDPmLlf4JqqsKdeKLdPlZtxynPDTDPXoPYdwtgWK7fGi%2Bel1zQHmKUiVVRbXu1UtOWbXD4RELTHCap7l5hxAF%2BBgpq%2FWcNZ6W3qDsmxfJE0pEToaQUlD0p30OmjB5rE4hjyh%2Fm8QZCYpUaWa40CFQTd3daP4p%2F%2FLeHIo4w5b0Np6hFOFkMK69ib0GOqUBGNHTRf4WgbrnKGTbX8RBBRSQgQfkKPSIGn4M2hHJW5SN6kFJIOGkhwHV4VPvgULAm6qhsDgYVO5dhZglaFFZ18AMvuSwb1DAvRmG55jCo0NtQTl7CxwBjgf2wQM84r7fvToQfX3ybMv4pkyoIzL2%2BcTK4cv0HPCC9Fjzs6XL%2BUxxAymT4qDFxVjRMEPyWjsE38AsAKzsGoFsUf0n7bVQCzduyklf&X-Amz-Signature=891d9d691eae9d73f6708b65c8a19feb1d459b02a26043e1dbff363a3ae2fce3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y5G3KH7N%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJHMEUCID6%2FT7YvH3D%2B02TRwuAke9g3XwXLgSOkhKN9aslDq8dNAiEArh5p7KtZoRSZia%2BUmFS7VGnlh7igWLEOXLnuRUc5m1Yq%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDBapKsa8DiRSpwisuircA4G3zTsFTCGf7h88x4rmSLPksSdUwr3XeTYPUnsNOSxLJFbwCQhTnNwT97scP8BVcv6YokE%2BjpX5c7%2B6tkDmbNDK%2BN6cvYfm42DyU0JyRM6pj9SSAYojmO3ZZuGvKZC9iws7RKPD183Flw0oQAEu%2BoCSmPSOUHrqH2MZy7Nh4r0C1HKlv3VIvlAATbNu5xyCm1QtpBBGurC%2F2ZhdV9lNVfzmLB%2FJNz80c7fmXp8kOQ6woS2pgHDNboxluhcHJTaiNsZ83V2xL4oyMjnvHAOKhDzGxoT9OaQwKiUyqVb%2B8Zy02ES9RsGGLL%2FYCuyc2vyhkrX6RjRbPOWlpzrHMgbapLgtamqINgoWtYDHujcRqayIbZNZO%2B8i06gAPBN9A%2FJkwTPWxR4BirxgSJ6EJSkvX9XxoK92k74A0%2BruJVxuifQEw7B4OmpLaZwgvt26C2xdRgczQ7hA9%2BEIDPmLlf4JqqsKdeKLdPlZtxynPDTDPXoPYdwtgWK7fGi%2Bel1zQHmKUiVVRbXu1UtOWbXD4RELTHCap7l5hxAF%2BBgpq%2FWcNZ6W3qDsmxfJE0pEToaQUlD0p30OmjB5rE4hjyh%2Fm8QZCYpUaWa40CFQTd3daP4p%2F%2FLeHIo4w5b0Np6hFOFkMK69ib0GOqUBGNHTRf4WgbrnKGTbX8RBBRSQgQfkKPSIGn4M2hHJW5SN6kFJIOGkhwHV4VPvgULAm6qhsDgYVO5dhZglaFFZ18AMvuSwb1DAvRmG55jCo0NtQTl7CxwBjgf2wQM84r7fvToQfX3ybMv4pkyoIzL2%2BcTK4cv0HPCC9Fjzs6XL%2BUxxAymT4qDFxVjRMEPyWjsE38AsAKzsGoFsUf0n7bVQCzduyklf&X-Amz-Signature=365d82a9ee2b4dcdd01dd51fb8be10ad920f7616316db3882c050a21ac57b4f0&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y5G3KH7N%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJHMEUCID6%2FT7YvH3D%2B02TRwuAke9g3XwXLgSOkhKN9aslDq8dNAiEArh5p7KtZoRSZia%2BUmFS7VGnlh7igWLEOXLnuRUc5m1Yq%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDBapKsa8DiRSpwisuircA4G3zTsFTCGf7h88x4rmSLPksSdUwr3XeTYPUnsNOSxLJFbwCQhTnNwT97scP8BVcv6YokE%2BjpX5c7%2B6tkDmbNDK%2BN6cvYfm42DyU0JyRM6pj9SSAYojmO3ZZuGvKZC9iws7RKPD183Flw0oQAEu%2BoCSmPSOUHrqH2MZy7Nh4r0C1HKlv3VIvlAATbNu5xyCm1QtpBBGurC%2F2ZhdV9lNVfzmLB%2FJNz80c7fmXp8kOQ6woS2pgHDNboxluhcHJTaiNsZ83V2xL4oyMjnvHAOKhDzGxoT9OaQwKiUyqVb%2B8Zy02ES9RsGGLL%2FYCuyc2vyhkrX6RjRbPOWlpzrHMgbapLgtamqINgoWtYDHujcRqayIbZNZO%2B8i06gAPBN9A%2FJkwTPWxR4BirxgSJ6EJSkvX9XxoK92k74A0%2BruJVxuifQEw7B4OmpLaZwgvt26C2xdRgczQ7hA9%2BEIDPmLlf4JqqsKdeKLdPlZtxynPDTDPXoPYdwtgWK7fGi%2Bel1zQHmKUiVVRbXu1UtOWbXD4RELTHCap7l5hxAF%2BBgpq%2FWcNZ6W3qDsmxfJE0pEToaQUlD0p30OmjB5rE4hjyh%2Fm8QZCYpUaWa40CFQTd3daP4p%2F%2FLeHIo4w5b0Np6hFOFkMK69ib0GOqUBGNHTRf4WgbrnKGTbX8RBBRSQgQfkKPSIGn4M2hHJW5SN6kFJIOGkhwHV4VPvgULAm6qhsDgYVO5dhZglaFFZ18AMvuSwb1DAvRmG55jCo0NtQTl7CxwBjgf2wQM84r7fvToQfX3ybMv4pkyoIzL2%2BcTK4cv0HPCC9Fjzs6XL%2BUxxAymT4qDFxVjRMEPyWjsE38AsAKzsGoFsUf0n7bVQCzduyklf&X-Amz-Signature=805717fd2bf26f8947fbf82cb8502eab2af59f464e6a6f0f2fb7a01d3570fc84&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
