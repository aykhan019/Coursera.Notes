

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXUCMFT3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182039Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJIMEYCIQCGAu%2FBJTxGRrU0Ri%2BQCuW%2BNaYcln3cuRhO2KIrieUCnQIhAK6hJ1UaKABWRrjBpTBghCW5R3KAqgd0rpwAemuk%2FdiSKv8DCGIQABoMNjM3NDIzMTgzODA1IgxUdACQxgKrgisUtFgq3AOopUDvEhlHG6CGHyJqs6ODhOoWenX3%2FAu73ZwSvdnZV14E0jx40fBqaKkEC49gW3tU%2FgXkBekH5WFj6PDSjwIcske%2BasA0VqdTUlwp9Bo28jMTL9hb9aVFwqVJWKCHDzIyoHAJmJ6tDOTmuvV7zG0qd1niFJyY6pknYjwsxniX5MGOmeOp%2FWs3LmIIMovqngmaciBW%2FVFoOyzjK%2FhCDqHJB8%2BPWwy7I%2BXlMu3OuKGjqI5ypiubeZFKAxSnJpGcJvKi%2Fy1kjZQ%2B78QmvUvk0thFTIx2Y3bCo9UnxG4UhBS13FaJ4stQKaEngL51c7ivhL8katERfuonIuSZAVn5YsnrONdkuQq2uwOctPQxOqKN5LWHNufei9A7gm%2FodGWS5SCrpf5JUl8FEk9dWOVGA%2BKrxASPeB6yLMJtbuyDeRcPUzOTPtRWYi1r1CQusbBL2p%2FfulECr1%2Bw8ky%2FtAL8htvxQPi%2Bak848nLsrmKDRY1HgxDPI%2FjaOqXmo4lHcUdwQK6O4qVBPudm48F6lhDVOgmiD5wU%2B%2BTSMf65l%2FnVLR%2BncIU84y5UODaLHG4NU24MGTDfj9ZcoVTbyIzxp7Cea92eNY0WtvbMLF0152AOODHHOQKnDQPsgxAAYfWT1TCc0ZO9BjqkAd5nnGlHHS97eO%2BC3I5L1GcYTfPempYFhYER%2Bd1s0l0q3fTSzZcW11qyOYMJCD2ZScZZqFI6RQlyhmlp%2BUX8zrTfqxf7rNZenrPZkhnNDLYMvMMX%2FM%2Fbu43Kyysa6NEdGJn6FbKjmhManj3r1W2vjOIChT43bW8L2RbjC8X%2Fd2zXY5RjQKFb3OfQUi4%2Ba9PcCZR60OHLJbhlsZs8WljmgFb6Kykg&X-Amz-Signature=9db8344fad7d92e9664cf99ef60ee9c3b9777e0c6b732c2cfe9b29da7915ca1b&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXUCMFT3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182039Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJIMEYCIQCGAu%2FBJTxGRrU0Ri%2BQCuW%2BNaYcln3cuRhO2KIrieUCnQIhAK6hJ1UaKABWRrjBpTBghCW5R3KAqgd0rpwAemuk%2FdiSKv8DCGIQABoMNjM3NDIzMTgzODA1IgxUdACQxgKrgisUtFgq3AOopUDvEhlHG6CGHyJqs6ODhOoWenX3%2FAu73ZwSvdnZV14E0jx40fBqaKkEC49gW3tU%2FgXkBekH5WFj6PDSjwIcske%2BasA0VqdTUlwp9Bo28jMTL9hb9aVFwqVJWKCHDzIyoHAJmJ6tDOTmuvV7zG0qd1niFJyY6pknYjwsxniX5MGOmeOp%2FWs3LmIIMovqngmaciBW%2FVFoOyzjK%2FhCDqHJB8%2BPWwy7I%2BXlMu3OuKGjqI5ypiubeZFKAxSnJpGcJvKi%2Fy1kjZQ%2B78QmvUvk0thFTIx2Y3bCo9UnxG4UhBS13FaJ4stQKaEngL51c7ivhL8katERfuonIuSZAVn5YsnrONdkuQq2uwOctPQxOqKN5LWHNufei9A7gm%2FodGWS5SCrpf5JUl8FEk9dWOVGA%2BKrxASPeB6yLMJtbuyDeRcPUzOTPtRWYi1r1CQusbBL2p%2FfulECr1%2Bw8ky%2FtAL8htvxQPi%2Bak848nLsrmKDRY1HgxDPI%2FjaOqXmo4lHcUdwQK6O4qVBPudm48F6lhDVOgmiD5wU%2B%2BTSMf65l%2FnVLR%2BncIU84y5UODaLHG4NU24MGTDfj9ZcoVTbyIzxp7Cea92eNY0WtvbMLF0152AOODHHOQKnDQPsgxAAYfWT1TCc0ZO9BjqkAd5nnGlHHS97eO%2BC3I5L1GcYTfPempYFhYER%2Bd1s0l0q3fTSzZcW11qyOYMJCD2ZScZZqFI6RQlyhmlp%2BUX8zrTfqxf7rNZenrPZkhnNDLYMvMMX%2FM%2Fbu43Kyysa6NEdGJn6FbKjmhManj3r1W2vjOIChT43bW8L2RbjC8X%2Fd2zXY5RjQKFb3OfQUi4%2Ba9PcCZR60OHLJbhlsZs8WljmgFb6Kykg&X-Amz-Signature=b8b4d0826ceb39dffafc825d83b07ccdb976d084050346482f16275b4e9579a2&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXUCMFT3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182039Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJIMEYCIQCGAu%2FBJTxGRrU0Ri%2BQCuW%2BNaYcln3cuRhO2KIrieUCnQIhAK6hJ1UaKABWRrjBpTBghCW5R3KAqgd0rpwAemuk%2FdiSKv8DCGIQABoMNjM3NDIzMTgzODA1IgxUdACQxgKrgisUtFgq3AOopUDvEhlHG6CGHyJqs6ODhOoWenX3%2FAu73ZwSvdnZV14E0jx40fBqaKkEC49gW3tU%2FgXkBekH5WFj6PDSjwIcske%2BasA0VqdTUlwp9Bo28jMTL9hb9aVFwqVJWKCHDzIyoHAJmJ6tDOTmuvV7zG0qd1niFJyY6pknYjwsxniX5MGOmeOp%2FWs3LmIIMovqngmaciBW%2FVFoOyzjK%2FhCDqHJB8%2BPWwy7I%2BXlMu3OuKGjqI5ypiubeZFKAxSnJpGcJvKi%2Fy1kjZQ%2B78QmvUvk0thFTIx2Y3bCo9UnxG4UhBS13FaJ4stQKaEngL51c7ivhL8katERfuonIuSZAVn5YsnrONdkuQq2uwOctPQxOqKN5LWHNufei9A7gm%2FodGWS5SCrpf5JUl8FEk9dWOVGA%2BKrxASPeB6yLMJtbuyDeRcPUzOTPtRWYi1r1CQusbBL2p%2FfulECr1%2Bw8ky%2FtAL8htvxQPi%2Bak848nLsrmKDRY1HgxDPI%2FjaOqXmo4lHcUdwQK6O4qVBPudm48F6lhDVOgmiD5wU%2B%2BTSMf65l%2FnVLR%2BncIU84y5UODaLHG4NU24MGTDfj9ZcoVTbyIzxp7Cea92eNY0WtvbMLF0152AOODHHOQKnDQPsgxAAYfWT1TCc0ZO9BjqkAd5nnGlHHS97eO%2BC3I5L1GcYTfPempYFhYER%2Bd1s0l0q3fTSzZcW11qyOYMJCD2ZScZZqFI6RQlyhmlp%2BUX8zrTfqxf7rNZenrPZkhnNDLYMvMMX%2FM%2Fbu43Kyysa6NEdGJn6FbKjmhManj3r1W2vjOIChT43bW8L2RbjC8X%2Fd2zXY5RjQKFb3OfQUi4%2Ba9PcCZR60OHLJbhlsZs8WljmgFb6Kykg&X-Amz-Signature=c253ac145a54b069d62697bfed76034a0c8171257724881d76042e4ef7caa9ea&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46653IRLSRI%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182040Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIGAcF0livv9PD%2FlQRgVeUn6CFhcJ79Wgthc4pWEg4j1CAiEAzc6v2h9WR9kO1L%2BIOBOQgIOUoiOPuBfxME0Ph4QRtsEq%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDP8fGlopLx6GmYHX4SrcA%2Bdf%2F3bXByvzropMrr5CWqEeoLXcl5wqC4rQ2oaDNh7W5Tmo%2BjbGSbxVqebu9byrrSyZ%2F3k2AfJVghsF8S0wQjF9fiPE8hyK%2BdARR6DYzbOOSOzEWrs9uiOiHgV78giIgtBUKbwvmGYKLiM86Sqh4KDBWBMrsOfJAW%2F8cHwzhxaGrxNh%2B4xvbvForGE1CserdsOJ%2FL3jwILQlAy2IhqNgtBrHvU7BW81j47GRb%2BPSOXq8StgsGRZyTKrEhjfIlYifBF3F0pUWq09T5wJSlHcN4KubWZS8YtYxvUK913LJO7T2qwqUeRbZWHBoRcc1kIJshmUrp5wkkN3QAQYGfesPSY0KzLE36kGN2V7h7zvmIqqj2Q218W0V8oKAvEUlwTeTj59%2FfcySmu5IO4Rx0kbLJayRWoJSeb2g%2FM4C0BotwWCvYHtMoHYeVti%2BypMUWPlVVpg1NhPt3iPIXhxbIxZZrV3SfE%2FPu8Ad8ODCpTOauKLXACK8r2XZ7T2vsz%2BdgHpyhWhY00YSK9Pw8Y0aiZ8lnfSvvKZ%2BFO3D5Nun9BEJPTsP7x5IfX0iLZFNEGsTN7YQYaOwVh43LEavd1unCC1gg8Xe3n560UAQMGpKdWdkMoD9LDe82HAsQ8yTW%2FeMLDRk70GOqUBY7fFFnHBdsBkOm5I1fNWuBeFqZ9cGjh%2B2WR56wKrNJ5AWgbXkdowl%2FwBsaEsmFRZa5iMbE%2FhcibmKF80PHR4S%2FqN3F7W1wAVp%2B0mCkUWYh47FDHUydGWBk0v1FYyniHs2Dx3glqN2AsECFVCjB7FQNVAUtJ0IxTyXdsbKlgzrVWStmzyArngrtKJh2unhFbvhbPHEzN6b03qX2uh1GpEjbCR8hkI&X-Amz-Signature=7d423e9a45ab038d3857801260e3878fa0f04c3496b8c79a46fe0692eea847ff&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJ7I3BMW%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182040Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJIMEYCIQCn0LTBc4mWl20C6vhSiB43BHcpFXDW%2BtuJsUqxGYcNQAIhAKmHo7oemg9eyJIZiWlbX3iW70SOdnNvgT%2F5cKLEOHDkKv8DCGIQABoMNjM3NDIzMTgzODA1Igwrv1UtTPxzNHgc0BMq3APdXqA%2FOq85lyNpYzIn%2FYTR7n9fJOxAyus5lzeqIPe46MwZ37UJ4JUWInneYPvT9LfNNa%2B7RgpR4GJrhZRck0YU3geV7VrGbxEvDT2hWYzIOtDvMht3GzaLSHte4vO7iYQoy2s31aVaiz1Ahe%2F4VpQi7%2Bzaf7Thl19qHRS1BtDPg90x%2FqoEgb3EgdM77tp%2BuDa1yvuO5DyObGgON66Q37JewwSq%2FBm5EMPduvkltQt1GZ7jhNJx78CsUoW59Yo%2FuqAsF%2FDNT4taexEs%2FTTXpfnfqIHlNtODaU%2FXZDEeceP6hkug0qZMxoGe0ssc0oJ2r2NzgfVim9UiJYIMMgAqpt9LSIWtnEQYV1%2FyrHuhdwCq0of0%2B3bcX7FZXzvJY%2FrmRNH%2FJD77Nx%2Bq5Nnd9ZI1p3ZMlCXFhiZ5JYbe%2FO%2B5C3UUPVUvCwylId1qx2bjg5rdnNNwGR%2BkHfuATmhFDctrTzO9RMIE3wUZX4IfvxU6d1y9Ap5z8gWfb%2FCOu2MJ2bXsrbMiYac0fXDBUw3d9cEScNc8eHOOl319rOT5cuDazCUtX%2BsnVoJsY8lK7uIG4aXc4lanwvn3PAPDdl4Hgl61wxBbz95u2Aqy8si6fjRwBR9niCTbGP3MMCrxlxf1MjDT0ZO9BjqkAeF6rjpPKLARjwM1r%2FeD%2BVDTmMQ9wZObJ3akzgm%2B32aKX%2BMJkHrnmtEn7k2rc%2F6FRFHJFJCx%2B5SbMYiCasr11t3bvIgaJcj%2BqDYrICNRXjz52YZp7OvAbZhpC77u0c76Lxm%2FJ4XH4emabGQ%2BVp6GwLbVcmhhkNzavEr7uimRx1rb00WjZ3UzY5ZUessqJdkHCq%2B6fAiF8QQrl9vj9hOlgvxN7M%2FI&X-Amz-Signature=0e781a9482591ab7986b7163f8a2b91209369dab0fc00d8f621c73cf85a9aa3b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXUCMFT3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182039Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJIMEYCIQCGAu%2FBJTxGRrU0Ri%2BQCuW%2BNaYcln3cuRhO2KIrieUCnQIhAK6hJ1UaKABWRrjBpTBghCW5R3KAqgd0rpwAemuk%2FdiSKv8DCGIQABoMNjM3NDIzMTgzODA1IgxUdACQxgKrgisUtFgq3AOopUDvEhlHG6CGHyJqs6ODhOoWenX3%2FAu73ZwSvdnZV14E0jx40fBqaKkEC49gW3tU%2FgXkBekH5WFj6PDSjwIcske%2BasA0VqdTUlwp9Bo28jMTL9hb9aVFwqVJWKCHDzIyoHAJmJ6tDOTmuvV7zG0qd1niFJyY6pknYjwsxniX5MGOmeOp%2FWs3LmIIMovqngmaciBW%2FVFoOyzjK%2FhCDqHJB8%2BPWwy7I%2BXlMu3OuKGjqI5ypiubeZFKAxSnJpGcJvKi%2Fy1kjZQ%2B78QmvUvk0thFTIx2Y3bCo9UnxG4UhBS13FaJ4stQKaEngL51c7ivhL8katERfuonIuSZAVn5YsnrONdkuQq2uwOctPQxOqKN5LWHNufei9A7gm%2FodGWS5SCrpf5JUl8FEk9dWOVGA%2BKrxASPeB6yLMJtbuyDeRcPUzOTPtRWYi1r1CQusbBL2p%2FfulECr1%2Bw8ky%2FtAL8htvxQPi%2Bak848nLsrmKDRY1HgxDPI%2FjaOqXmo4lHcUdwQK6O4qVBPudm48F6lhDVOgmiD5wU%2B%2BTSMf65l%2FnVLR%2BncIU84y5UODaLHG4NU24MGTDfj9ZcoVTbyIzxp7Cea92eNY0WtvbMLF0152AOODHHOQKnDQPsgxAAYfWT1TCc0ZO9BjqkAd5nnGlHHS97eO%2BC3I5L1GcYTfPempYFhYER%2Bd1s0l0q3fTSzZcW11qyOYMJCD2ZScZZqFI6RQlyhmlp%2BUX8zrTfqxf7rNZenrPZkhnNDLYMvMMX%2FM%2Fbu43Kyysa6NEdGJn6FbKjmhManj3r1W2vjOIChT43bW8L2RbjC8X%2Fd2zXY5RjQKFb3OfQUi4%2Ba9PcCZR60OHLJbhlsZs8WljmgFb6Kykg&X-Amz-Signature=aa212003c91f6e56078e2be7bb71c44463fbfc56e6c5df22c9efe61971f6629e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXUCMFT3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182039Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJIMEYCIQCGAu%2FBJTxGRrU0Ri%2BQCuW%2BNaYcln3cuRhO2KIrieUCnQIhAK6hJ1UaKABWRrjBpTBghCW5R3KAqgd0rpwAemuk%2FdiSKv8DCGIQABoMNjM3NDIzMTgzODA1IgxUdACQxgKrgisUtFgq3AOopUDvEhlHG6CGHyJqs6ODhOoWenX3%2FAu73ZwSvdnZV14E0jx40fBqaKkEC49gW3tU%2FgXkBekH5WFj6PDSjwIcske%2BasA0VqdTUlwp9Bo28jMTL9hb9aVFwqVJWKCHDzIyoHAJmJ6tDOTmuvV7zG0qd1niFJyY6pknYjwsxniX5MGOmeOp%2FWs3LmIIMovqngmaciBW%2FVFoOyzjK%2FhCDqHJB8%2BPWwy7I%2BXlMu3OuKGjqI5ypiubeZFKAxSnJpGcJvKi%2Fy1kjZQ%2B78QmvUvk0thFTIx2Y3bCo9UnxG4UhBS13FaJ4stQKaEngL51c7ivhL8katERfuonIuSZAVn5YsnrONdkuQq2uwOctPQxOqKN5LWHNufei9A7gm%2FodGWS5SCrpf5JUl8FEk9dWOVGA%2BKrxASPeB6yLMJtbuyDeRcPUzOTPtRWYi1r1CQusbBL2p%2FfulECr1%2Bw8ky%2FtAL8htvxQPi%2Bak848nLsrmKDRY1HgxDPI%2FjaOqXmo4lHcUdwQK6O4qVBPudm48F6lhDVOgmiD5wU%2B%2BTSMf65l%2FnVLR%2BncIU84y5UODaLHG4NU24MGTDfj9ZcoVTbyIzxp7Cea92eNY0WtvbMLF0152AOODHHOQKnDQPsgxAAYfWT1TCc0ZO9BjqkAd5nnGlHHS97eO%2BC3I5L1GcYTfPempYFhYER%2Bd1s0l0q3fTSzZcW11qyOYMJCD2ZScZZqFI6RQlyhmlp%2BUX8zrTfqxf7rNZenrPZkhnNDLYMvMMX%2FM%2Fbu43Kyysa6NEdGJn6FbKjmhManj3r1W2vjOIChT43bW8L2RbjC8X%2Fd2zXY5RjQKFb3OfQUi4%2Ba9PcCZR60OHLJbhlsZs8WljmgFb6Kykg&X-Amz-Signature=313a8abf1aab7ae6014def227091781c06a806ca6b5f810f99e792cc6628dc1b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXUCMFT3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182039Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJIMEYCIQCGAu%2FBJTxGRrU0Ri%2BQCuW%2BNaYcln3cuRhO2KIrieUCnQIhAK6hJ1UaKABWRrjBpTBghCW5R3KAqgd0rpwAemuk%2FdiSKv8DCGIQABoMNjM3NDIzMTgzODA1IgxUdACQxgKrgisUtFgq3AOopUDvEhlHG6CGHyJqs6ODhOoWenX3%2FAu73ZwSvdnZV14E0jx40fBqaKkEC49gW3tU%2FgXkBekH5WFj6PDSjwIcske%2BasA0VqdTUlwp9Bo28jMTL9hb9aVFwqVJWKCHDzIyoHAJmJ6tDOTmuvV7zG0qd1niFJyY6pknYjwsxniX5MGOmeOp%2FWs3LmIIMovqngmaciBW%2FVFoOyzjK%2FhCDqHJB8%2BPWwy7I%2BXlMu3OuKGjqI5ypiubeZFKAxSnJpGcJvKi%2Fy1kjZQ%2B78QmvUvk0thFTIx2Y3bCo9UnxG4UhBS13FaJ4stQKaEngL51c7ivhL8katERfuonIuSZAVn5YsnrONdkuQq2uwOctPQxOqKN5LWHNufei9A7gm%2FodGWS5SCrpf5JUl8FEk9dWOVGA%2BKrxASPeB6yLMJtbuyDeRcPUzOTPtRWYi1r1CQusbBL2p%2FfulECr1%2Bw8ky%2FtAL8htvxQPi%2Bak848nLsrmKDRY1HgxDPI%2FjaOqXmo4lHcUdwQK6O4qVBPudm48F6lhDVOgmiD5wU%2B%2BTSMf65l%2FnVLR%2BncIU84y5UODaLHG4NU24MGTDfj9ZcoVTbyIzxp7Cea92eNY0WtvbMLF0152AOODHHOQKnDQPsgxAAYfWT1TCc0ZO9BjqkAd5nnGlHHS97eO%2BC3I5L1GcYTfPempYFhYER%2Bd1s0l0q3fTSzZcW11qyOYMJCD2ZScZZqFI6RQlyhmlp%2BUX8zrTfqxf7rNZenrPZkhnNDLYMvMMX%2FM%2Fbu43Kyysa6NEdGJn6FbKjmhManj3r1W2vjOIChT43bW8L2RbjC8X%2Fd2zXY5RjQKFb3OfQUi4%2Ba9PcCZR60OHLJbhlsZs8WljmgFb6Kykg&X-Amz-Signature=62eefba9c969ca84a94ec2f474db632bdda58587ee9ea461836ff33f94ec2d5a&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXUCMFT3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182039Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJIMEYCIQCGAu%2FBJTxGRrU0Ri%2BQCuW%2BNaYcln3cuRhO2KIrieUCnQIhAK6hJ1UaKABWRrjBpTBghCW5R3KAqgd0rpwAemuk%2FdiSKv8DCGIQABoMNjM3NDIzMTgzODA1IgxUdACQxgKrgisUtFgq3AOopUDvEhlHG6CGHyJqs6ODhOoWenX3%2FAu73ZwSvdnZV14E0jx40fBqaKkEC49gW3tU%2FgXkBekH5WFj6PDSjwIcske%2BasA0VqdTUlwp9Bo28jMTL9hb9aVFwqVJWKCHDzIyoHAJmJ6tDOTmuvV7zG0qd1niFJyY6pknYjwsxniX5MGOmeOp%2FWs3LmIIMovqngmaciBW%2FVFoOyzjK%2FhCDqHJB8%2BPWwy7I%2BXlMu3OuKGjqI5ypiubeZFKAxSnJpGcJvKi%2Fy1kjZQ%2B78QmvUvk0thFTIx2Y3bCo9UnxG4UhBS13FaJ4stQKaEngL51c7ivhL8katERfuonIuSZAVn5YsnrONdkuQq2uwOctPQxOqKN5LWHNufei9A7gm%2FodGWS5SCrpf5JUl8FEk9dWOVGA%2BKrxASPeB6yLMJtbuyDeRcPUzOTPtRWYi1r1CQusbBL2p%2FfulECr1%2Bw8ky%2FtAL8htvxQPi%2Bak848nLsrmKDRY1HgxDPI%2FjaOqXmo4lHcUdwQK6O4qVBPudm48F6lhDVOgmiD5wU%2B%2BTSMf65l%2FnVLR%2BncIU84y5UODaLHG4NU24MGTDfj9ZcoVTbyIzxp7Cea92eNY0WtvbMLF0152AOODHHOQKnDQPsgxAAYfWT1TCc0ZO9BjqkAd5nnGlHHS97eO%2BC3I5L1GcYTfPempYFhYER%2Bd1s0l0q3fTSzZcW11qyOYMJCD2ZScZZqFI6RQlyhmlp%2BUX8zrTfqxf7rNZenrPZkhnNDLYMvMMX%2FM%2Fbu43Kyysa6NEdGJn6FbKjmhManj3r1W2vjOIChT43bW8L2RbjC8X%2Fd2zXY5RjQKFb3OfQUi4%2Ba9PcCZR60OHLJbhlsZs8WljmgFb6Kykg&X-Amz-Signature=05df0450951e5226696adbd6834e21af8317c0dc2f92915a407fe3e3076a4587&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
