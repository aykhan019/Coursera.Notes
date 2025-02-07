

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466425H2AQO%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIAEim%2Bx6P7q6VmXKXAqZljOX2hBg1IPgcOMfUON6Tzp3AiEAklwcnsH8IYEnNS8qykl%2F8ObkrSBY3DDzcjD2CxiN1%2FYq%2FwMIeBAAGgw2Mzc0MjMxODM4MDUiDADJZ82z9ZRHo48PLCrcA9BsWQbjw7iz3epnK082WS9rsb6EL081kf80HU8cW5IuHU%2Bwmtkv8ES7UQtd0wnG3XYRG4T7jTGTDNN0fB%2BtaY2eZR5OTy1PrYn7xFqKE3TGH6iyaC4ihfZwehXCMh0JbKAwCCJHoTmo2%2BvgMaNiPPqTqt2nQw6loYeOSwtdGWNxpSZBIl5jzXUStQN4Cy5GNxWg3%2BHQOzyOFnO5JmIuXlebSN%2FxesjbQWFo%2FwXnd9B2H9%2Biy68xlDHgHVIuk02TuPS3TTZtN3JEgBrwDKfidvVnC6z7GpB%2Bh31vFquLIVU7rUVv8sPzrp%2FPd9ZeNaSoYP%2BaLMl1BaNjxe1brHbrv%2FdN6d4SEWRl7ok8c%2FDAw5pOM5%2BqKWqOYW18tTGWhqASXilizzAA7nrL2SkQSX0crIN1g%2FG2MAD0qQE%2F4fxvT8mue3QCHTW2EXcKpDCpc9W8hGESxGE%2BD1XY2Rq4FNdeAYvfqrm%2B%2F8oeXYog9bG3zmHorgQ5HnsqsnUr495npioacZsrxby9oAgQfxJIovi1A6NF5Ue%2Fspun4rIPJhT%2FeBGAAiBI5TRWI5yelGfsXK7DpDKWtMrpFYYSlTpC88bubObODfaVxKwrWNmvELSkG9%2BSyBvEz78QmSRlNmEuMIDEmL0GOqUBpvEYlAqtOAf37qbLE3pyP6BNQQG8Ct77B%2BVb0tKxfEaVQg7ldU3bDP9wMOrf0T14KsKq4akmg8Ooi9RvhH9AEj22OeqAKT8Fe21%2BeMhGtEHKN8OUywcIrCHm9caWLwMvkkQ8ZwgPGqWbseNwM%2FIWqcJxavYN%2FhkUfsLairH1iT1Q4fCSx%2Faoqfu1ywl9vWZoiQE45iIe7CeV4tv5EoTx9LHZxOxI&X-Amz-Signature=be9826e8b9b29ec242fd6ea56c8e3ddb99000f274d9a88471934b722789c13f0&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466425H2AQO%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIAEim%2Bx6P7q6VmXKXAqZljOX2hBg1IPgcOMfUON6Tzp3AiEAklwcnsH8IYEnNS8qykl%2F8ObkrSBY3DDzcjD2CxiN1%2FYq%2FwMIeBAAGgw2Mzc0MjMxODM4MDUiDADJZ82z9ZRHo48PLCrcA9BsWQbjw7iz3epnK082WS9rsb6EL081kf80HU8cW5IuHU%2Bwmtkv8ES7UQtd0wnG3XYRG4T7jTGTDNN0fB%2BtaY2eZR5OTy1PrYn7xFqKE3TGH6iyaC4ihfZwehXCMh0JbKAwCCJHoTmo2%2BvgMaNiPPqTqt2nQw6loYeOSwtdGWNxpSZBIl5jzXUStQN4Cy5GNxWg3%2BHQOzyOFnO5JmIuXlebSN%2FxesjbQWFo%2FwXnd9B2H9%2Biy68xlDHgHVIuk02TuPS3TTZtN3JEgBrwDKfidvVnC6z7GpB%2Bh31vFquLIVU7rUVv8sPzrp%2FPd9ZeNaSoYP%2BaLMl1BaNjxe1brHbrv%2FdN6d4SEWRl7ok8c%2FDAw5pOM5%2BqKWqOYW18tTGWhqASXilizzAA7nrL2SkQSX0crIN1g%2FG2MAD0qQE%2F4fxvT8mue3QCHTW2EXcKpDCpc9W8hGESxGE%2BD1XY2Rq4FNdeAYvfqrm%2B%2F8oeXYog9bG3zmHorgQ5HnsqsnUr495npioacZsrxby9oAgQfxJIovi1A6NF5Ue%2Fspun4rIPJhT%2FeBGAAiBI5TRWI5yelGfsXK7DpDKWtMrpFYYSlTpC88bubObODfaVxKwrWNmvELSkG9%2BSyBvEz78QmSRlNmEuMIDEmL0GOqUBpvEYlAqtOAf37qbLE3pyP6BNQQG8Ct77B%2BVb0tKxfEaVQg7ldU3bDP9wMOrf0T14KsKq4akmg8Ooi9RvhH9AEj22OeqAKT8Fe21%2BeMhGtEHKN8OUywcIrCHm9caWLwMvkkQ8ZwgPGqWbseNwM%2FIWqcJxavYN%2FhkUfsLairH1iT1Q4fCSx%2Faoqfu1ywl9vWZoiQE45iIe7CeV4tv5EoTx9LHZxOxI&X-Amz-Signature=82cc45449c3ec9989b0856a7d35959f816417a7a8c6a9e8efa7865808a8a9e43&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466425H2AQO%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIAEim%2Bx6P7q6VmXKXAqZljOX2hBg1IPgcOMfUON6Tzp3AiEAklwcnsH8IYEnNS8qykl%2F8ObkrSBY3DDzcjD2CxiN1%2FYq%2FwMIeBAAGgw2Mzc0MjMxODM4MDUiDADJZ82z9ZRHo48PLCrcA9BsWQbjw7iz3epnK082WS9rsb6EL081kf80HU8cW5IuHU%2Bwmtkv8ES7UQtd0wnG3XYRG4T7jTGTDNN0fB%2BtaY2eZR5OTy1PrYn7xFqKE3TGH6iyaC4ihfZwehXCMh0JbKAwCCJHoTmo2%2BvgMaNiPPqTqt2nQw6loYeOSwtdGWNxpSZBIl5jzXUStQN4Cy5GNxWg3%2BHQOzyOFnO5JmIuXlebSN%2FxesjbQWFo%2FwXnd9B2H9%2Biy68xlDHgHVIuk02TuPS3TTZtN3JEgBrwDKfidvVnC6z7GpB%2Bh31vFquLIVU7rUVv8sPzrp%2FPd9ZeNaSoYP%2BaLMl1BaNjxe1brHbrv%2FdN6d4SEWRl7ok8c%2FDAw5pOM5%2BqKWqOYW18tTGWhqASXilizzAA7nrL2SkQSX0crIN1g%2FG2MAD0qQE%2F4fxvT8mue3QCHTW2EXcKpDCpc9W8hGESxGE%2BD1XY2Rq4FNdeAYvfqrm%2B%2F8oeXYog9bG3zmHorgQ5HnsqsnUr495npioacZsrxby9oAgQfxJIovi1A6NF5Ue%2Fspun4rIPJhT%2FeBGAAiBI5TRWI5yelGfsXK7DpDKWtMrpFYYSlTpC88bubObODfaVxKwrWNmvELSkG9%2BSyBvEz78QmSRlNmEuMIDEmL0GOqUBpvEYlAqtOAf37qbLE3pyP6BNQQG8Ct77B%2BVb0tKxfEaVQg7ldU3bDP9wMOrf0T14KsKq4akmg8Ooi9RvhH9AEj22OeqAKT8Fe21%2BeMhGtEHKN8OUywcIrCHm9caWLwMvkkQ8ZwgPGqWbseNwM%2FIWqcJxavYN%2FhkUfsLairH1iT1Q4fCSx%2Faoqfu1ywl9vWZoiQE45iIe7CeV4tv5EoTx9LHZxOxI&X-Amz-Signature=3eb641d83af8d956ccc2760c71338482ec320cc07b9cceb3baf68cf9e1c20d68&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UM2AA7FG%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIAi%2FDXVCoDq6oxOp9id0z95%2FSkbJxSKiPX9c8RWg2hR5AiEA0NipXvSQIZjItouf4Yf7Cea9oMfI2FDX%2BigX5UzzKEUq%2FwMIeBAAGgw2Mzc0MjMxODM4MDUiDF%2F0Uy3p8ov5AwmwFircA8Znu%2FWr%2BDNfbQcQl7JRAkbsz4Q2TI4dMLRBwWtIzn9ouyL9Ff2s4WrInsBRhw%2B2uT1yTZ%2B%2FU0O9JNsPEVBXLDQUHREkBmbDbULD4%2F8Wuo4GBpFJMCcT5S8igdPgCS7k6Cby2Su%2BlA9OSzs4mBtzr9aiNv52g3fjOHBsgUcMvjlObKSNhDsT93Aize2Dt%2Bpfa3Osoia31CzS%2FQ%2B2u06KoXnPkPcArgIT9G45ggYuHynb7jiStOwBFRyL%2Bhgf0znH8GC0McGpd6usEu%2B6%2FcAaYiiYTvSZzLGRR0Y6ugqs0dzkt9CM7queLB%2BYE%2Fih41fmEBPhQWsD08v9azRQB4jz8CCFmE8kF0aqo1OJsNR5hKDtMwyz3i1YmioZ9xS9WoPznAc8m5PoZhimFxgCgY6HniRxZ3IjwOZDuKT2Og34b3UuB%2FTpMMspxFKh7PRwqCdcop80VPM4XdQGZFOVKeRD%2B3BNO%2BVCIq8hCzMoyeaXDe5hJFykBi6%2FWaMoGSY3GfnCKWYm0HhaaYJQH85yP8betn0PDI3bQzde0bqmSo99tL2Lmef1DNQBuzvKCzVuOplKW7K2s3Qz9mPMk7gFdjGIT8wPvvtOv5ltivM2UvAMBgLxXizFt%2FpuCtsiX8izMI%2FEmL0GOqUB3qStf2KHTXvzQKIh%2BEOUyno7vsaliggL9krxpouTEDZVDHebTZGCJxd1rrjj66sHeFOJmtyNS8QyGyt4iqycqw5SY1XA6JgLopwS2IZkqWp%2BK2eSbgG6duwSH%2BEAxllXYXYRNHIhu9JU2qsp8yTj5tnirMw%2FTAIGnEZc1YMB%2Bi4PpJ9jr5a7mFPdXc2eArjLibXUOpxCV%2Fb04AAkbo37w4eHiALH&X-Amz-Signature=c418d96fc16e6bf549099b5ba79de6eb501a0ae1493c43ca99c03a1b0492802c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665FS32YYL%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQC4x6oYFqtFmg0ggqUMz2yBN3endSkyI0%2B1tHPjnqdWBwIhAOqFVaQLoVzURgN6aXjcOM1hB6TyisVcaUW3u5cLz5qpKv8DCHgQABoMNjM3NDIzMTgzODA1Igz7DyHXPeKN%2B5pP02Qq3AObNUU5JrAE8myAPXZ%2Br00DiaMg7qd1i28qi46uXmmMUujSfPz5EdlX5Nnla4vYmKljn2MWfH9grUhlaObeR5kVpszmfXRo%2Fbts22e1aOyJf7xkPrx9k%2BlWDPMg3buxg%2ByHBOgZJbOK%2Bg%2B4n%2B8hqqaDmgleodcl2xQXYhj%2BfkkV2y2ChPcYP13np6aQIXIvC2AlRYlA1vt7R7oZmJ%2B8g8a0LEXkTfwd%2FavSnU0b6POMRiZxEx%2BkroG6FZy02qBeVW6hDDNE4c70WSI9FOXvMgbCJqAUZG48g9KCa9fqBQsapTg%2FDoMq3yz4ZkORTEnMiTLhMj3r54FRnnt%2F46Q49nHzVAypXfH3rrWryfGXuqqyE%2BzI1Oy4bA5OqvZ5sNE9gdoXXvzNQrZ68%2FnmGSH3hiZ6wWaYwXb%2BODiVWVhVyjV3eKyT5ToguvnuWGwKWN79Ldf3br%2BeWdYbSy5k2iaS0%2FrVPd3ZXZSdIx1rf%2Fv4WxrGPLbr%2BEs6uZB5eNyBAqc654whPlCq96QO9%2FmAcpz5Z9LJB3J%2BvMCOzDx4KYC9QoNjT5OXLlNWtndBrejzye4PFUKMqZLIjFxVJjKovNqR94SMFSWOFVOd2NLmN7%2Bpy7oJZlGuaG7IrwNMQwtJnDDcw5i9BjqkARr2X8%2B2aOUATNLVab2%2BQbHwIGBNvN%2BuNRAKpSrClMUAbPN4aken0FklKaQe%2FlFU8M5ztH%2Bq1Qup41gOQ3WPW%2Fdtj41dGdCizXcvS2JvsTVVGSj4w8Jgp7zlPnKZjrUP%2BuaWpFAn9wn%2FXNmAK4i7iRrb8A0j2wnd%2FuJ6P9Yy1WptKI0%2Bsh81CstgdtZ016VB0nOGfgDGV9%2BhZBoIhng86OxOWi6I&X-Amz-Signature=92caaa2ccca26e8fc4f711c5f651cb629305538e0600f72a408c8de26caf98c1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466425H2AQO%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIAEim%2Bx6P7q6VmXKXAqZljOX2hBg1IPgcOMfUON6Tzp3AiEAklwcnsH8IYEnNS8qykl%2F8ObkrSBY3DDzcjD2CxiN1%2FYq%2FwMIeBAAGgw2Mzc0MjMxODM4MDUiDADJZ82z9ZRHo48PLCrcA9BsWQbjw7iz3epnK082WS9rsb6EL081kf80HU8cW5IuHU%2Bwmtkv8ES7UQtd0wnG3XYRG4T7jTGTDNN0fB%2BtaY2eZR5OTy1PrYn7xFqKE3TGH6iyaC4ihfZwehXCMh0JbKAwCCJHoTmo2%2BvgMaNiPPqTqt2nQw6loYeOSwtdGWNxpSZBIl5jzXUStQN4Cy5GNxWg3%2BHQOzyOFnO5JmIuXlebSN%2FxesjbQWFo%2FwXnd9B2H9%2Biy68xlDHgHVIuk02TuPS3TTZtN3JEgBrwDKfidvVnC6z7GpB%2Bh31vFquLIVU7rUVv8sPzrp%2FPd9ZeNaSoYP%2BaLMl1BaNjxe1brHbrv%2FdN6d4SEWRl7ok8c%2FDAw5pOM5%2BqKWqOYW18tTGWhqASXilizzAA7nrL2SkQSX0crIN1g%2FG2MAD0qQE%2F4fxvT8mue3QCHTW2EXcKpDCpc9W8hGESxGE%2BD1XY2Rq4FNdeAYvfqrm%2B%2F8oeXYog9bG3zmHorgQ5HnsqsnUr495npioacZsrxby9oAgQfxJIovi1A6NF5Ue%2Fspun4rIPJhT%2FeBGAAiBI5TRWI5yelGfsXK7DpDKWtMrpFYYSlTpC88bubObODfaVxKwrWNmvELSkG9%2BSyBvEz78QmSRlNmEuMIDEmL0GOqUBpvEYlAqtOAf37qbLE3pyP6BNQQG8Ct77B%2BVb0tKxfEaVQg7ldU3bDP9wMOrf0T14KsKq4akmg8Ooi9RvhH9AEj22OeqAKT8Fe21%2BeMhGtEHKN8OUywcIrCHm9caWLwMvkkQ8ZwgPGqWbseNwM%2FIWqcJxavYN%2FhkUfsLairH1iT1Q4fCSx%2Faoqfu1ywl9vWZoiQE45iIe7CeV4tv5EoTx9LHZxOxI&X-Amz-Signature=bbe03cdce345aaed93e758aefe23cb93a20662aec5ac3d3c9c56d94f0e54757c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466425H2AQO%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIAEim%2Bx6P7q6VmXKXAqZljOX2hBg1IPgcOMfUON6Tzp3AiEAklwcnsH8IYEnNS8qykl%2F8ObkrSBY3DDzcjD2CxiN1%2FYq%2FwMIeBAAGgw2Mzc0MjMxODM4MDUiDADJZ82z9ZRHo48PLCrcA9BsWQbjw7iz3epnK082WS9rsb6EL081kf80HU8cW5IuHU%2Bwmtkv8ES7UQtd0wnG3XYRG4T7jTGTDNN0fB%2BtaY2eZR5OTy1PrYn7xFqKE3TGH6iyaC4ihfZwehXCMh0JbKAwCCJHoTmo2%2BvgMaNiPPqTqt2nQw6loYeOSwtdGWNxpSZBIl5jzXUStQN4Cy5GNxWg3%2BHQOzyOFnO5JmIuXlebSN%2FxesjbQWFo%2FwXnd9B2H9%2Biy68xlDHgHVIuk02TuPS3TTZtN3JEgBrwDKfidvVnC6z7GpB%2Bh31vFquLIVU7rUVv8sPzrp%2FPd9ZeNaSoYP%2BaLMl1BaNjxe1brHbrv%2FdN6d4SEWRl7ok8c%2FDAw5pOM5%2BqKWqOYW18tTGWhqASXilizzAA7nrL2SkQSX0crIN1g%2FG2MAD0qQE%2F4fxvT8mue3QCHTW2EXcKpDCpc9W8hGESxGE%2BD1XY2Rq4FNdeAYvfqrm%2B%2F8oeXYog9bG3zmHorgQ5HnsqsnUr495npioacZsrxby9oAgQfxJIovi1A6NF5Ue%2Fspun4rIPJhT%2FeBGAAiBI5TRWI5yelGfsXK7DpDKWtMrpFYYSlTpC88bubObODfaVxKwrWNmvELSkG9%2BSyBvEz78QmSRlNmEuMIDEmL0GOqUBpvEYlAqtOAf37qbLE3pyP6BNQQG8Ct77B%2BVb0tKxfEaVQg7ldU3bDP9wMOrf0T14KsKq4akmg8Ooi9RvhH9AEj22OeqAKT8Fe21%2BeMhGtEHKN8OUywcIrCHm9caWLwMvkkQ8ZwgPGqWbseNwM%2FIWqcJxavYN%2FhkUfsLairH1iT1Q4fCSx%2Faoqfu1ywl9vWZoiQE45iIe7CeV4tv5EoTx9LHZxOxI&X-Amz-Signature=aef801e1197dbd039b2073b59fd6b1d5953374274272f798c28c2794a60aa2d6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466425H2AQO%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIAEim%2Bx6P7q6VmXKXAqZljOX2hBg1IPgcOMfUON6Tzp3AiEAklwcnsH8IYEnNS8qykl%2F8ObkrSBY3DDzcjD2CxiN1%2FYq%2FwMIeBAAGgw2Mzc0MjMxODM4MDUiDADJZ82z9ZRHo48PLCrcA9BsWQbjw7iz3epnK082WS9rsb6EL081kf80HU8cW5IuHU%2Bwmtkv8ES7UQtd0wnG3XYRG4T7jTGTDNN0fB%2BtaY2eZR5OTy1PrYn7xFqKE3TGH6iyaC4ihfZwehXCMh0JbKAwCCJHoTmo2%2BvgMaNiPPqTqt2nQw6loYeOSwtdGWNxpSZBIl5jzXUStQN4Cy5GNxWg3%2BHQOzyOFnO5JmIuXlebSN%2FxesjbQWFo%2FwXnd9B2H9%2Biy68xlDHgHVIuk02TuPS3TTZtN3JEgBrwDKfidvVnC6z7GpB%2Bh31vFquLIVU7rUVv8sPzrp%2FPd9ZeNaSoYP%2BaLMl1BaNjxe1brHbrv%2FdN6d4SEWRl7ok8c%2FDAw5pOM5%2BqKWqOYW18tTGWhqASXilizzAA7nrL2SkQSX0crIN1g%2FG2MAD0qQE%2F4fxvT8mue3QCHTW2EXcKpDCpc9W8hGESxGE%2BD1XY2Rq4FNdeAYvfqrm%2B%2F8oeXYog9bG3zmHorgQ5HnsqsnUr495npioacZsrxby9oAgQfxJIovi1A6NF5Ue%2Fspun4rIPJhT%2FeBGAAiBI5TRWI5yelGfsXK7DpDKWtMrpFYYSlTpC88bubObODfaVxKwrWNmvELSkG9%2BSyBvEz78QmSRlNmEuMIDEmL0GOqUBpvEYlAqtOAf37qbLE3pyP6BNQQG8Ct77B%2BVb0tKxfEaVQg7ldU3bDP9wMOrf0T14KsKq4akmg8Ooi9RvhH9AEj22OeqAKT8Fe21%2BeMhGtEHKN8OUywcIrCHm9caWLwMvkkQ8ZwgPGqWbseNwM%2FIWqcJxavYN%2FhkUfsLairH1iT1Q4fCSx%2Faoqfu1ywl9vWZoiQE45iIe7CeV4tv5EoTx9LHZxOxI&X-Amz-Signature=3baed3bfe6109e6085b091dfd5c2b45c6edd94fb92e1f99c9ff24e80389c62c8&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466425H2AQO%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIAEim%2Bx6P7q6VmXKXAqZljOX2hBg1IPgcOMfUON6Tzp3AiEAklwcnsH8IYEnNS8qykl%2F8ObkrSBY3DDzcjD2CxiN1%2FYq%2FwMIeBAAGgw2Mzc0MjMxODM4MDUiDADJZ82z9ZRHo48PLCrcA9BsWQbjw7iz3epnK082WS9rsb6EL081kf80HU8cW5IuHU%2Bwmtkv8ES7UQtd0wnG3XYRG4T7jTGTDNN0fB%2BtaY2eZR5OTy1PrYn7xFqKE3TGH6iyaC4ihfZwehXCMh0JbKAwCCJHoTmo2%2BvgMaNiPPqTqt2nQw6loYeOSwtdGWNxpSZBIl5jzXUStQN4Cy5GNxWg3%2BHQOzyOFnO5JmIuXlebSN%2FxesjbQWFo%2FwXnd9B2H9%2Biy68xlDHgHVIuk02TuPS3TTZtN3JEgBrwDKfidvVnC6z7GpB%2Bh31vFquLIVU7rUVv8sPzrp%2FPd9ZeNaSoYP%2BaLMl1BaNjxe1brHbrv%2FdN6d4SEWRl7ok8c%2FDAw5pOM5%2BqKWqOYW18tTGWhqASXilizzAA7nrL2SkQSX0crIN1g%2FG2MAD0qQE%2F4fxvT8mue3QCHTW2EXcKpDCpc9W8hGESxGE%2BD1XY2Rq4FNdeAYvfqrm%2B%2F8oeXYog9bG3zmHorgQ5HnsqsnUr495npioacZsrxby9oAgQfxJIovi1A6NF5Ue%2Fspun4rIPJhT%2FeBGAAiBI5TRWI5yelGfsXK7DpDKWtMrpFYYSlTpC88bubObODfaVxKwrWNmvELSkG9%2BSyBvEz78QmSRlNmEuMIDEmL0GOqUBpvEYlAqtOAf37qbLE3pyP6BNQQG8Ct77B%2BVb0tKxfEaVQg7ldU3bDP9wMOrf0T14KsKq4akmg8Ooi9RvhH9AEj22OeqAKT8Fe21%2BeMhGtEHKN8OUywcIrCHm9caWLwMvkkQ8ZwgPGqWbseNwM%2FIWqcJxavYN%2FhkUfsLairH1iT1Q4fCSx%2Faoqfu1ywl9vWZoiQE45iIe7CeV4tv5EoTx9LHZxOxI&X-Amz-Signature=cb6b2e8d9abcee4fe3682f35b720ca530fa064abc5467f0a5958b04e340319ce&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
