

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46665SSW5RP%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQDjyuYijHXA3e%2Bm5WzPp27GY5VzlqhBFf%2BvxO95umq5wwIgVjkgqV2FFoZ15kamfuIxFM7xEccSWsBOIOpvDml2Umsq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDD7%2Fy6Oz1pbR5iczRircAwrT01KWtxaM%2B2Zy9zDUnjFJNW6r9i7x6sdzzMR9X7cFpETTpXwMWIvQ%2F%2FKzdWBjJgx6sdgsGF9JpXaVaYlnzQo1ANPsYob6Q3zm31yo9hxLaw5HcVD620jpiBEoH%2FpCYBzsdCP5fgm%2FwQIRdgn2wyHbkyMLtTsPlxtM6JnPjYTAw9BfjmrEqKHqlYTl3PQfMcY5vG9OIMN20HYunH%2FaZ7uDL%2FOBbPY5%2FTNL2HVNsjNEs2DxnqbKKFbF3mqAtio8garS202opqTbTCmkz7qM1fCMQIdnGKrwAW8FNqtlk4GQt%2FczZToUUDDJxWJhTpfs51HDbs23DfTrrk8gsB7nk0TYIBePLPZ8%2FtyiCruNP1lzakQQjQLMPamDeZ4xcuFoFMDaKDl7anRZfHuRqrx82qzerrwQPbgnF61%2Bk4d1bumQjxNNgwKWq4VjyGoNjbQlFpnFdR3X3U79zGgTB8DCbMkraa6SfxkVgGxpqHwCGoBpVhVqFzWELiybGIAXcaHQ21%2Fr7K2rezJvrpn86%2BNBpRx5QJHwFSaVkU%2FIpwGQXatL0%2BmpzTPxEVbrU1DeNFfYh1Wa8KNQYuJUIPMy5wqUZ9jOoHdum9gHE2t2mbQprUXE0LwO3JrDC%2B7za%2BAjMKzskb0GOqUBQW1AfACxwsCYJecGQT2kmWdGxZbS4GT9ITIqqeFyzBXIGyewrKmqxl0Oae6R%2FIehnEi2X975Gkb%2FyhMmOztutyNdPuDpDhoQtpcoU6ByV2LTN%2Fcy8oPtMWKgy0aJFSeUjYJTh0rXUTRwKIW8qOy6q9HSaEgBUEFxRP8PTLDqgROT6LsDZBovf5YSkrvROn55hfzfHD505HmCHmVPd%2BhUzMPHLbja&X-Amz-Signature=e07383e7f1b96bbf2ef516632ebfe4d6f74af03eb98d3586396ec67cd5c239d0&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46665SSW5RP%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQDjyuYijHXA3e%2Bm5WzPp27GY5VzlqhBFf%2BvxO95umq5wwIgVjkgqV2FFoZ15kamfuIxFM7xEccSWsBOIOpvDml2Umsq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDD7%2Fy6Oz1pbR5iczRircAwrT01KWtxaM%2B2Zy9zDUnjFJNW6r9i7x6sdzzMR9X7cFpETTpXwMWIvQ%2F%2FKzdWBjJgx6sdgsGF9JpXaVaYlnzQo1ANPsYob6Q3zm31yo9hxLaw5HcVD620jpiBEoH%2FpCYBzsdCP5fgm%2FwQIRdgn2wyHbkyMLtTsPlxtM6JnPjYTAw9BfjmrEqKHqlYTl3PQfMcY5vG9OIMN20HYunH%2FaZ7uDL%2FOBbPY5%2FTNL2HVNsjNEs2DxnqbKKFbF3mqAtio8garS202opqTbTCmkz7qM1fCMQIdnGKrwAW8FNqtlk4GQt%2FczZToUUDDJxWJhTpfs51HDbs23DfTrrk8gsB7nk0TYIBePLPZ8%2FtyiCruNP1lzakQQjQLMPamDeZ4xcuFoFMDaKDl7anRZfHuRqrx82qzerrwQPbgnF61%2Bk4d1bumQjxNNgwKWq4VjyGoNjbQlFpnFdR3X3U79zGgTB8DCbMkraa6SfxkVgGxpqHwCGoBpVhVqFzWELiybGIAXcaHQ21%2Fr7K2rezJvrpn86%2BNBpRx5QJHwFSaVkU%2FIpwGQXatL0%2BmpzTPxEVbrU1DeNFfYh1Wa8KNQYuJUIPMy5wqUZ9jOoHdum9gHE2t2mbQprUXE0LwO3JrDC%2B7za%2BAjMKzskb0GOqUBQW1AfACxwsCYJecGQT2kmWdGxZbS4GT9ITIqqeFyzBXIGyewrKmqxl0Oae6R%2FIehnEi2X975Gkb%2FyhMmOztutyNdPuDpDhoQtpcoU6ByV2LTN%2Fcy8oPtMWKgy0aJFSeUjYJTh0rXUTRwKIW8qOy6q9HSaEgBUEFxRP8PTLDqgROT6LsDZBovf5YSkrvROn55hfzfHD505HmCHmVPd%2BhUzMPHLbja&X-Amz-Signature=28fdb8bb9793e55f3bb86414ac139ca3a493e7548a1c5686dcde7fb22cb7dcac&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46665SSW5RP%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQDjyuYijHXA3e%2Bm5WzPp27GY5VzlqhBFf%2BvxO95umq5wwIgVjkgqV2FFoZ15kamfuIxFM7xEccSWsBOIOpvDml2Umsq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDD7%2Fy6Oz1pbR5iczRircAwrT01KWtxaM%2B2Zy9zDUnjFJNW6r9i7x6sdzzMR9X7cFpETTpXwMWIvQ%2F%2FKzdWBjJgx6sdgsGF9JpXaVaYlnzQo1ANPsYob6Q3zm31yo9hxLaw5HcVD620jpiBEoH%2FpCYBzsdCP5fgm%2FwQIRdgn2wyHbkyMLtTsPlxtM6JnPjYTAw9BfjmrEqKHqlYTl3PQfMcY5vG9OIMN20HYunH%2FaZ7uDL%2FOBbPY5%2FTNL2HVNsjNEs2DxnqbKKFbF3mqAtio8garS202opqTbTCmkz7qM1fCMQIdnGKrwAW8FNqtlk4GQt%2FczZToUUDDJxWJhTpfs51HDbs23DfTrrk8gsB7nk0TYIBePLPZ8%2FtyiCruNP1lzakQQjQLMPamDeZ4xcuFoFMDaKDl7anRZfHuRqrx82qzerrwQPbgnF61%2Bk4d1bumQjxNNgwKWq4VjyGoNjbQlFpnFdR3X3U79zGgTB8DCbMkraa6SfxkVgGxpqHwCGoBpVhVqFzWELiybGIAXcaHQ21%2Fr7K2rezJvrpn86%2BNBpRx5QJHwFSaVkU%2FIpwGQXatL0%2BmpzTPxEVbrU1DeNFfYh1Wa8KNQYuJUIPMy5wqUZ9jOoHdum9gHE2t2mbQprUXE0LwO3JrDC%2B7za%2BAjMKzskb0GOqUBQW1AfACxwsCYJecGQT2kmWdGxZbS4GT9ITIqqeFyzBXIGyewrKmqxl0Oae6R%2FIehnEi2X975Gkb%2FyhMmOztutyNdPuDpDhoQtpcoU6ByV2LTN%2Fcy8oPtMWKgy0aJFSeUjYJTh0rXUTRwKIW8qOy6q9HSaEgBUEFxRP8PTLDqgROT6LsDZBovf5YSkrvROn55hfzfHD505HmCHmVPd%2BhUzMPHLbja&X-Amz-Signature=147de12ff3038b44fb0b3ca88d9237bff3cf65f09c9c27f219b4b1e8169416e1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USEH3NJ6%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIHfAimR7o3VAXI1YdJw6Kp0Dn85tHraW0jaiNQdXrsoCAiB%2Fh9K9%2BMIaxbhKs%2B8LesQbDk1l%2BuTK7E5bC5%2BpLSsZ6Sr%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIM50ISYF7X1ErqwV23KtwDUPRRDYdf0V2mMzu1unqtLI0SuMrMWJMJijpC%2FfBXnU%2B6z9KF75bmiFmxLkgg%2FX2GJLARoC24pvX9u8G8ChqQQpyCKRXqhGxD4rnUEFqdkJ7XF9CM7C2MFSvceHnoMuvMwApsp%2Fj20lQMld5JMPbPH%2BpxFswIknyftN6iVBHLZudqx8hxEWBzYF5eZ9Uqv%2FaH5o8dlbqEioGyMT1AtRs2Zq8wy183Fyq5ZHshZ7qduOScNHMyJv1TBzEy1lK3CX0HxxxeGOyOd4GczwFXRnvpCMdJZnhj9T6Ag05s5Ph%2BOJ3bOeUT7wrGLULsM%2FLYTToJa0b7INoXzv8rBPUUaEl%2BR2%2BU0XHAHAi57mvs6Ug30P3CqFYEiVMG%2BaoztFuHilnTTA5G4apXXNodhFsb7KQehA%2BMlszFhaGKtT8ZEnezYcZcSr%2FnvItGG58MHG255hryIbP2dHtJp3oDhOGOcQP995jG5QW1lUUgP3XpfbqZh55SemkGRzsSk3T917S5899W9%2FgtxkeCCB4JzpGVHc1oQ3NelmEutP7rEaiwqc38WkVVEGgz0A%2Fn0n8Phh%2F7T6J%2FjbVQCoffItlVB7pbChyAo4oYQ5XibyVXoIwgRwDQf5Okll22j7FAYEqmGlsw3%2BuRvQY6pgEX6Vcx%2BwfRw2hsVuYOEItLJcIGpL7Xupy1B8ioJJE%2FgssBUL9CyaUm49XNzsDn0WpknL101kl30kE1fUME3yCKyvfh2KAyfromXmxC9%2F0II%2BuH8PixlhO%2BMNpF2Ianf46jZ7mUyBEZM8uv1e7fR0i9H7opSB7vW7L6QkzVESVLL9%2BKZMLkfVQhGFkfzX%2BEIwOrH5Xhh1yNLZRvnfvkJOqH17fHIIbm&X-Amz-Signature=c750a21832593a757023a50a110f536a98816908f0a22f13eb75c9eb4127e9ea&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TZ6QCWRC%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQC2irAIEqLaI4dIGuqOEutRSnfASrYvDAGKMLSeA%2BRs2AIhAOL1EDjiLTcnKidlfjGnpWVhdoPJ2AOBVqro9NEjNDsrKv8DCFoQABoMNjM3NDIzMTgzODA1IgwTiOAXPEj8sNzQQakq3AObCnyRTdhV1kYTWolplaleLlN9TvMqSipmI%2BXBahF0UflYdXRWKOg9DR1DwvJjInc0LSc9%2ByeQFzIxaY1GBtyE%2F10Wn5gZi8nsawU1gqDHYJZW71OnhZ%2B1Tkv2Qr8XjS28q1Z9KkYxujKQbIWZCl0wtRDN%2F6f7phO9Rs0p%2FeVvlLIv5t2C9DEHdw96dXvPdCDceeYtuPlbJ%2FDVaV9IKHW6ttFUk4PKATUTMmIs5akWZ8E51gL93UdzhnTQaNUSJXfyQS68JmWMhjelN9Qf2XaSs5wpF8vg2CnPEgZcUjEfsq7TRX%2F2FMCiyHIMPObZY3Kpu%2FAd486CZe0CCLj8iR5om3TQPRwx%2BAKq2QcEDMAc5JDAhGhyiD0q7B3g7yr5Mt7EvQIc%2BtV7fZDwd%2FT7PabRubIpwf%2FguzrT6MvKLil%2BbMniYF4hqi6Yh%2FDWTx24Sfx01fFY5mpY0JUMloSmBHsdTM3grHPPRTWjrBjT4U9KTg5krsFa5eEyTG2JrmfB83Q%2BvLFW03xOj5wT0dQc9uf4BD7BqXvanfCdbPA8mNPSUeNVX10EcGBMJkk9ruVthqhhgsIXtZSZn4LMDeLgTXbWctOQfWkrugZlAJqN5EwgRT2vYeFFYLPez4XkFzCG7JG9BjqkASPZCMc1zP7qdr812McT6%2B8T86czsZj8YXJovYsgNjRwVj45kFshl5JRE%2BbBTp%2FLzPCBhJgTmwfc%2FzRwe6nvoaSf%2BAMavaAsPKoupG2Vpy8XDPLUUXZX6WcnP3feEo3AkLUR%2Bg53RsNwF%2FFBx3UgccJwgHixJmhhbLORJXcbx8S2hT87srMUiDEbYcFSc4gM8lHULZJ%2FcUa%2BZTcSyeZxVGV5xRat&X-Amz-Signature=8a4d5e1137afe85e7f0aefd6821087273335085af13ca23b5992bc0210bea0bd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46665SSW5RP%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQDjyuYijHXA3e%2Bm5WzPp27GY5VzlqhBFf%2BvxO95umq5wwIgVjkgqV2FFoZ15kamfuIxFM7xEccSWsBOIOpvDml2Umsq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDD7%2Fy6Oz1pbR5iczRircAwrT01KWtxaM%2B2Zy9zDUnjFJNW6r9i7x6sdzzMR9X7cFpETTpXwMWIvQ%2F%2FKzdWBjJgx6sdgsGF9JpXaVaYlnzQo1ANPsYob6Q3zm31yo9hxLaw5HcVD620jpiBEoH%2FpCYBzsdCP5fgm%2FwQIRdgn2wyHbkyMLtTsPlxtM6JnPjYTAw9BfjmrEqKHqlYTl3PQfMcY5vG9OIMN20HYunH%2FaZ7uDL%2FOBbPY5%2FTNL2HVNsjNEs2DxnqbKKFbF3mqAtio8garS202opqTbTCmkz7qM1fCMQIdnGKrwAW8FNqtlk4GQt%2FczZToUUDDJxWJhTpfs51HDbs23DfTrrk8gsB7nk0TYIBePLPZ8%2FtyiCruNP1lzakQQjQLMPamDeZ4xcuFoFMDaKDl7anRZfHuRqrx82qzerrwQPbgnF61%2Bk4d1bumQjxNNgwKWq4VjyGoNjbQlFpnFdR3X3U79zGgTB8DCbMkraa6SfxkVgGxpqHwCGoBpVhVqFzWELiybGIAXcaHQ21%2Fr7K2rezJvrpn86%2BNBpRx5QJHwFSaVkU%2FIpwGQXatL0%2BmpzTPxEVbrU1DeNFfYh1Wa8KNQYuJUIPMy5wqUZ9jOoHdum9gHE2t2mbQprUXE0LwO3JrDC%2B7za%2BAjMKzskb0GOqUBQW1AfACxwsCYJecGQT2kmWdGxZbS4GT9ITIqqeFyzBXIGyewrKmqxl0Oae6R%2FIehnEi2X975Gkb%2FyhMmOztutyNdPuDpDhoQtpcoU6ByV2LTN%2Fcy8oPtMWKgy0aJFSeUjYJTh0rXUTRwKIW8qOy6q9HSaEgBUEFxRP8PTLDqgROT6LsDZBovf5YSkrvROn55hfzfHD505HmCHmVPd%2BhUzMPHLbja&X-Amz-Signature=ce0cb78f80035d9f4869cede57ff75a134c04766cf6bada7fc7756cfd3d06340&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46665SSW5RP%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQDjyuYijHXA3e%2Bm5WzPp27GY5VzlqhBFf%2BvxO95umq5wwIgVjkgqV2FFoZ15kamfuIxFM7xEccSWsBOIOpvDml2Umsq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDD7%2Fy6Oz1pbR5iczRircAwrT01KWtxaM%2B2Zy9zDUnjFJNW6r9i7x6sdzzMR9X7cFpETTpXwMWIvQ%2F%2FKzdWBjJgx6sdgsGF9JpXaVaYlnzQo1ANPsYob6Q3zm31yo9hxLaw5HcVD620jpiBEoH%2FpCYBzsdCP5fgm%2FwQIRdgn2wyHbkyMLtTsPlxtM6JnPjYTAw9BfjmrEqKHqlYTl3PQfMcY5vG9OIMN20HYunH%2FaZ7uDL%2FOBbPY5%2FTNL2HVNsjNEs2DxnqbKKFbF3mqAtio8garS202opqTbTCmkz7qM1fCMQIdnGKrwAW8FNqtlk4GQt%2FczZToUUDDJxWJhTpfs51HDbs23DfTrrk8gsB7nk0TYIBePLPZ8%2FtyiCruNP1lzakQQjQLMPamDeZ4xcuFoFMDaKDl7anRZfHuRqrx82qzerrwQPbgnF61%2Bk4d1bumQjxNNgwKWq4VjyGoNjbQlFpnFdR3X3U79zGgTB8DCbMkraa6SfxkVgGxpqHwCGoBpVhVqFzWELiybGIAXcaHQ21%2Fr7K2rezJvrpn86%2BNBpRx5QJHwFSaVkU%2FIpwGQXatL0%2BmpzTPxEVbrU1DeNFfYh1Wa8KNQYuJUIPMy5wqUZ9jOoHdum9gHE2t2mbQprUXE0LwO3JrDC%2B7za%2BAjMKzskb0GOqUBQW1AfACxwsCYJecGQT2kmWdGxZbS4GT9ITIqqeFyzBXIGyewrKmqxl0Oae6R%2FIehnEi2X975Gkb%2FyhMmOztutyNdPuDpDhoQtpcoU6ByV2LTN%2Fcy8oPtMWKgy0aJFSeUjYJTh0rXUTRwKIW8qOy6q9HSaEgBUEFxRP8PTLDqgROT6LsDZBovf5YSkrvROn55hfzfHD505HmCHmVPd%2BhUzMPHLbja&X-Amz-Signature=67899272735fd391d5edfdb4d5116d7b1b0712300cd89af58abdbf1d28044170&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46665SSW5RP%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQDjyuYijHXA3e%2Bm5WzPp27GY5VzlqhBFf%2BvxO95umq5wwIgVjkgqV2FFoZ15kamfuIxFM7xEccSWsBOIOpvDml2Umsq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDD7%2Fy6Oz1pbR5iczRircAwrT01KWtxaM%2B2Zy9zDUnjFJNW6r9i7x6sdzzMR9X7cFpETTpXwMWIvQ%2F%2FKzdWBjJgx6sdgsGF9JpXaVaYlnzQo1ANPsYob6Q3zm31yo9hxLaw5HcVD620jpiBEoH%2FpCYBzsdCP5fgm%2FwQIRdgn2wyHbkyMLtTsPlxtM6JnPjYTAw9BfjmrEqKHqlYTl3PQfMcY5vG9OIMN20HYunH%2FaZ7uDL%2FOBbPY5%2FTNL2HVNsjNEs2DxnqbKKFbF3mqAtio8garS202opqTbTCmkz7qM1fCMQIdnGKrwAW8FNqtlk4GQt%2FczZToUUDDJxWJhTpfs51HDbs23DfTrrk8gsB7nk0TYIBePLPZ8%2FtyiCruNP1lzakQQjQLMPamDeZ4xcuFoFMDaKDl7anRZfHuRqrx82qzerrwQPbgnF61%2Bk4d1bumQjxNNgwKWq4VjyGoNjbQlFpnFdR3X3U79zGgTB8DCbMkraa6SfxkVgGxpqHwCGoBpVhVqFzWELiybGIAXcaHQ21%2Fr7K2rezJvrpn86%2BNBpRx5QJHwFSaVkU%2FIpwGQXatL0%2BmpzTPxEVbrU1DeNFfYh1Wa8KNQYuJUIPMy5wqUZ9jOoHdum9gHE2t2mbQprUXE0LwO3JrDC%2B7za%2BAjMKzskb0GOqUBQW1AfACxwsCYJecGQT2kmWdGxZbS4GT9ITIqqeFyzBXIGyewrKmqxl0Oae6R%2FIehnEi2X975Gkb%2FyhMmOztutyNdPuDpDhoQtpcoU6ByV2LTN%2Fcy8oPtMWKgy0aJFSeUjYJTh0rXUTRwKIW8qOy6q9HSaEgBUEFxRP8PTLDqgROT6LsDZBovf5YSkrvROn55hfzfHD505HmCHmVPd%2BhUzMPHLbja&X-Amz-Signature=597db8e2fc55e34f252397193717466bf94d2a930ff2b011a6d56722a33efe4e&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46665SSW5RP%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQDjyuYijHXA3e%2Bm5WzPp27GY5VzlqhBFf%2BvxO95umq5wwIgVjkgqV2FFoZ15kamfuIxFM7xEccSWsBOIOpvDml2Umsq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDD7%2Fy6Oz1pbR5iczRircAwrT01KWtxaM%2B2Zy9zDUnjFJNW6r9i7x6sdzzMR9X7cFpETTpXwMWIvQ%2F%2FKzdWBjJgx6sdgsGF9JpXaVaYlnzQo1ANPsYob6Q3zm31yo9hxLaw5HcVD620jpiBEoH%2FpCYBzsdCP5fgm%2FwQIRdgn2wyHbkyMLtTsPlxtM6JnPjYTAw9BfjmrEqKHqlYTl3PQfMcY5vG9OIMN20HYunH%2FaZ7uDL%2FOBbPY5%2FTNL2HVNsjNEs2DxnqbKKFbF3mqAtio8garS202opqTbTCmkz7qM1fCMQIdnGKrwAW8FNqtlk4GQt%2FczZToUUDDJxWJhTpfs51HDbs23DfTrrk8gsB7nk0TYIBePLPZ8%2FtyiCruNP1lzakQQjQLMPamDeZ4xcuFoFMDaKDl7anRZfHuRqrx82qzerrwQPbgnF61%2Bk4d1bumQjxNNgwKWq4VjyGoNjbQlFpnFdR3X3U79zGgTB8DCbMkraa6SfxkVgGxpqHwCGoBpVhVqFzWELiybGIAXcaHQ21%2Fr7K2rezJvrpn86%2BNBpRx5QJHwFSaVkU%2FIpwGQXatL0%2BmpzTPxEVbrU1DeNFfYh1Wa8KNQYuJUIPMy5wqUZ9jOoHdum9gHE2t2mbQprUXE0LwO3JrDC%2B7za%2BAjMKzskb0GOqUBQW1AfACxwsCYJecGQT2kmWdGxZbS4GT9ITIqqeFyzBXIGyewrKmqxl0Oae6R%2FIehnEi2X975Gkb%2FyhMmOztutyNdPuDpDhoQtpcoU6ByV2LTN%2Fcy8oPtMWKgy0aJFSeUjYJTh0rXUTRwKIW8qOy6q9HSaEgBUEFxRP8PTLDqgROT6LsDZBovf5YSkrvROn55hfzfHD505HmCHmVPd%2BhUzMPHLbja&X-Amz-Signature=780d4c0ccb662f59c39512ff7324470edcd1cb576a20a3ef9b3d7f908faa540e&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
