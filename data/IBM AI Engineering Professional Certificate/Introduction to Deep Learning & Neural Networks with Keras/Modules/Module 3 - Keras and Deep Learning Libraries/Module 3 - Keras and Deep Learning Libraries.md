

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VEHHMVXQ%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQCqZapSDi7guKF%2BSxaPLJGO%2FrUx3wh2OtME5cBZHZpllQIgaWOutJvba9YLTNQALuE6SzH0vZNOJrFgGT6SzJT8774q%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDAZvbDpeHHS%2FJDh84ircA5OEI7zPvDwafV%2FEbHRlrxQQN5P%2Brl5PkMDw%2Bm%2BY342g5Av44ySUsmkGPBgpjERI6BWx4ILWXCRBSiZJbDonni7%2FMOJJO4owlfzlyIbjxwbbmund1MxhoMTvK56JsgLGtncYcIrl0QVhUOl%2F%2BGmDQlpZiBq7A40z9x4ErvQW5ffuTWm4E%2BkCNv%2BJ4gW3HMwB%2FCUoQDW96%2F3kdnAZtpjRysizl3zRmW3RPa1FXICddG06sIdtw9mM6CZkZuwWjCFJ2FueuNuJ5Nqj53mNElWVoyet8XwT%2Fht2PvRKGhsYjM3MGzx0ZHyVjW8lA4JuKw7GIllBt%2BHeWZhJAs%2FyjBj2SHOridjfxlft4Lz9Ng9l9Y%2FlAGAqBcclG1KirYD%2BszfSafD8o%2B9NPDxPEdQ%2B65qreVsGIVst33UB1HE8xMqQal%2F0PD%2Bio4pTpCxoovHK9vudz%2BD7fUf3x%2FZ4RZcsI7JVjtsBUBxsIixTLEp8tikZnadL24AV4oeUzXeS7t0mJEaufrqX2NQb7MzvvN%2BNoU%2BFXSSetSmfTiFHyqH5VDvKiyIyfytIoPzrVsRtDf8aTQZdOpZ8jeo4u9ZsQQ7tw1JUKzMyiHeh76dszFr69wJnDRl%2BCPSsoYIrp0wdSsdQMLjkxL0GOqUBQ5BYEJSjLFygM9lAcu4Yl%2FbOKizwU9%2FqdGSm4fBqkHbbvcVXGEo7egOPLuZcXIOZ0Gh90q7LskL7V6udpsn6tpBcJ2aNs50XhrBSZjsCuZZJ8ES9qz4bcVePW1PjprJg9YfD7N9fZ3g2NSvUF79G%2Fa7EuaRr%2Fpg%2BT1Ugb4etYLLMu9F8nuENjR%2FQiK1z3jB1cxRLxUHeydK0fXsU%2BtL6V4%2FedzfB&X-Amz-Signature=c12c022d7762466be0357f426cfcd539f20b8290e45e04f30f957e4e0f802f78&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VEHHMVXQ%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQCqZapSDi7guKF%2BSxaPLJGO%2FrUx3wh2OtME5cBZHZpllQIgaWOutJvba9YLTNQALuE6SzH0vZNOJrFgGT6SzJT8774q%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDAZvbDpeHHS%2FJDh84ircA5OEI7zPvDwafV%2FEbHRlrxQQN5P%2Brl5PkMDw%2Bm%2BY342g5Av44ySUsmkGPBgpjERI6BWx4ILWXCRBSiZJbDonni7%2FMOJJO4owlfzlyIbjxwbbmund1MxhoMTvK56JsgLGtncYcIrl0QVhUOl%2F%2BGmDQlpZiBq7A40z9x4ErvQW5ffuTWm4E%2BkCNv%2BJ4gW3HMwB%2FCUoQDW96%2F3kdnAZtpjRysizl3zRmW3RPa1FXICddG06sIdtw9mM6CZkZuwWjCFJ2FueuNuJ5Nqj53mNElWVoyet8XwT%2Fht2PvRKGhsYjM3MGzx0ZHyVjW8lA4JuKw7GIllBt%2BHeWZhJAs%2FyjBj2SHOridjfxlft4Lz9Ng9l9Y%2FlAGAqBcclG1KirYD%2BszfSafD8o%2B9NPDxPEdQ%2B65qreVsGIVst33UB1HE8xMqQal%2F0PD%2Bio4pTpCxoovHK9vudz%2BD7fUf3x%2FZ4RZcsI7JVjtsBUBxsIixTLEp8tikZnadL24AV4oeUzXeS7t0mJEaufrqX2NQb7MzvvN%2BNoU%2BFXSSetSmfTiFHyqH5VDvKiyIyfytIoPzrVsRtDf8aTQZdOpZ8jeo4u9ZsQQ7tw1JUKzMyiHeh76dszFr69wJnDRl%2BCPSsoYIrp0wdSsdQMLjkxL0GOqUBQ5BYEJSjLFygM9lAcu4Yl%2FbOKizwU9%2FqdGSm4fBqkHbbvcVXGEo7egOPLuZcXIOZ0Gh90q7LskL7V6udpsn6tpBcJ2aNs50XhrBSZjsCuZZJ8ES9qz4bcVePW1PjprJg9YfD7N9fZ3g2NSvUF79G%2Fa7EuaRr%2Fpg%2BT1Ugb4etYLLMu9F8nuENjR%2FQiK1z3jB1cxRLxUHeydK0fXsU%2BtL6V4%2FedzfB&X-Amz-Signature=7cfd04d20e379d79e19b337019957646d59f6d4714b010c722d7bd9e27b4ef2d&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VEHHMVXQ%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQCqZapSDi7guKF%2BSxaPLJGO%2FrUx3wh2OtME5cBZHZpllQIgaWOutJvba9YLTNQALuE6SzH0vZNOJrFgGT6SzJT8774q%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDAZvbDpeHHS%2FJDh84ircA5OEI7zPvDwafV%2FEbHRlrxQQN5P%2Brl5PkMDw%2Bm%2BY342g5Av44ySUsmkGPBgpjERI6BWx4ILWXCRBSiZJbDonni7%2FMOJJO4owlfzlyIbjxwbbmund1MxhoMTvK56JsgLGtncYcIrl0QVhUOl%2F%2BGmDQlpZiBq7A40z9x4ErvQW5ffuTWm4E%2BkCNv%2BJ4gW3HMwB%2FCUoQDW96%2F3kdnAZtpjRysizl3zRmW3RPa1FXICddG06sIdtw9mM6CZkZuwWjCFJ2FueuNuJ5Nqj53mNElWVoyet8XwT%2Fht2PvRKGhsYjM3MGzx0ZHyVjW8lA4JuKw7GIllBt%2BHeWZhJAs%2FyjBj2SHOridjfxlft4Lz9Ng9l9Y%2FlAGAqBcclG1KirYD%2BszfSafD8o%2B9NPDxPEdQ%2B65qreVsGIVst33UB1HE8xMqQal%2F0PD%2Bio4pTpCxoovHK9vudz%2BD7fUf3x%2FZ4RZcsI7JVjtsBUBxsIixTLEp8tikZnadL24AV4oeUzXeS7t0mJEaufrqX2NQb7MzvvN%2BNoU%2BFXSSetSmfTiFHyqH5VDvKiyIyfytIoPzrVsRtDf8aTQZdOpZ8jeo4u9ZsQQ7tw1JUKzMyiHeh76dszFr69wJnDRl%2BCPSsoYIrp0wdSsdQMLjkxL0GOqUBQ5BYEJSjLFygM9lAcu4Yl%2FbOKizwU9%2FqdGSm4fBqkHbbvcVXGEo7egOPLuZcXIOZ0Gh90q7LskL7V6udpsn6tpBcJ2aNs50XhrBSZjsCuZZJ8ES9qz4bcVePW1PjprJg9YfD7N9fZ3g2NSvUF79G%2Fa7EuaRr%2Fpg%2BT1Ugb4etYLLMu9F8nuENjR%2FQiK1z3jB1cxRLxUHeydK0fXsU%2BtL6V4%2FedzfB&X-Amz-Signature=6d541b9aed215baf24c97928a70d02695cd6d8446d63db1fb140e49b13983903&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPZOLBD7%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004206Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIBMWQbvU1LntOx%2B1uSMh6hWgYN6ESeQSLIcMEsAJPqTaAiEAvwTpYOzNzBqwgpunt3QUVtE60s6YhRTsTRwQBbtHAukq%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDDPeHJbc3iqFn7nFdCrcAywBa0eraGfeoFWf6ZCsCNlYzSTsgSO%2BNijoMCv4a26hoK90sSJQrn1VqBxpAB0PENnU6Y8trSlqWXufQyEkKkHrDoJVJcQXIQX7T5RTLQpk1WPC4tFs7KJr0RXO%2FGX8V1eXQKo8eSk%2B5LE%2BFK5UDiV3DT6QAoSPVIgwB%2BALWm6zs%2Fd0bhTkbTckZK2ljFnJQWl8y2238AL4DYC2Ml9uPnGRrjSkeT%2FtCDqh%2BcvfHhbnFpdVtv%2Fd4ARhKQ1g10aW5Tt7vRogRyHBT2NT1ZKIYr1hXuE8G9bwzwDMg%2B60Jlwab9KPwWjJETwsM0HkS1Tjqh38EZ3A6BqBHcqX0Alg3s8S9gx54SyFPorj6ZefHsjsERDrDFuT78mzEx8rftC9pFkkqAUHN3RYHZa1bfRAS2CQUAvLIC8pU65dsAX4c7c%2B8%2FyNARhdsgdAYkgPiTDWX3c7FG43Ht25T5w2UFCi1QgByEaM7obQm9utezsLaZPu3kV%2F0C3ZAnH7%2F0BJ%2Bki8tUXpD%2B8S1erRmfyibCwJsPno5eTIMVbqDAeeZmAIBnO3klNDAx%2B8aewvOUUURMhhTlIVu8OWwhp9cGfOcdDD69xE2sQ78XvmbMq8MRnynQiY2XUjgmOInGupA2nyMPXlxL0GOqUBDqF77b6v%2Fi4th0Jf3yB14kZryyCehysyzRbWaYVWB1X00batxW4cWO0ooRAB9itEOA62lS5stnD0S4OWfzqK6gEQ3Cqn0fkPOZU69b8khDErrWAR50I2VpxbhvHYgjVVlZegAabtLHm4Jeh6CUsMb9AkFOheD%2Flh6qDx3colnKAu1QGp9cbzmDVYP59b4hLnAOcw5W6boqVSkeHqwb%2BO8s0fLxHl&X-Amz-Signature=37d926b50f5f0bdb512726c3545ca00d4bb910dbbb642da75ef4e6cfbc4dbab8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677YNMR4S%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004206Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJIMEYCIQDFsq76%2BmSx%2FdFPdg4IQ0fEMoZ%2FoeTZz43k45lMoenSDQIhAIA8f5%2BHYPk5OyOhqojn652FwnLw6xC%2BJUEmdbqLs%2F3CKv8DCFIQABoMNjM3NDIzMTgzODA1IgyaQiWaQTjc%2FSvuR4Aq3AOAXVPndZ75gBEfJyLE444vOcorRqBZivrLw5FpEqbH0SwkNivgm5a%2Bn6CFRXpJbv7risUBcakLLOSmEdJ0rgxiqY4AFUac2j9H%2F7Ou3SvOEMnXEgyoVim6%2FZy4hQjkVXlJmlNDm8BVWTq2oAm%2BglV0v5ow1V637R53PcqF7xF1iwUVhgckDZsoanCZIbheePb8GnnS70mmh9ZzDPo0G3N%2FeBkwVsHa7p49I9w4oPXUk0ow0w%2FycrYE5q4VrMcvIbdJHvKHpUObpwY8AtOA%2FZL2nrwLycKVmAJg6AAiCFn%2BgXHm%2BNzx0WA5B5nS5%2BUFUZaXe0rEHphCzMNNfsdEMlcGJaW0bFksfgAlwdPbH1O8JDoGNYI6OwvWrMsuyl4RPiqoRMkyusW3qz4jpsY3uXuvoLajkjAnIbCGq%2BFNtFBLGRt43V50FgYEOF4J%2FcDOhmPT0snTLSYNEgSY0CrzFjcANzWM7mmNGGBeCHvhnFbZZP0cNI4XgmaUV4tsuD9hbQcE%2FNOT9F%2BadJI9gDCVIU4jMeQ%2FDnD0CidEUWE9k1U%2FobkXxM8FqHKoExdJFogYFfC8I3OnR7iQPCCF8u2bd3t9JdaGd1HzHGfHIEUOUI8xPWg6cpi3Aiife%2F8FzDD65MS9BjqkASkDGiXIx2G6s77ETu9O706uT4v5ml9DJjlAw7%2Bwuy1XHe8%2BhGXaCA5FkEy4kmr6d0vlbeBGs5OvfGXg4dGRQB8Lt2joh77Zub4N2o9VElBguLvEdg%2BbLj6Tmevt6XFk5o%2B%2FvFA7RgpQ4XfSwKofCBUahVdtpYHtiU2U9BNfxN9OkRAgKhMVo%2Fqv1E0hdhUc7WgAKkmEtsz6jJpiu3foYXG3Wh5H&X-Amz-Signature=72a0d1946853eca56528cd2bed0353f7edf706f45cbdafbf465926c9dbccc0d3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VEHHMVXQ%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQCqZapSDi7guKF%2BSxaPLJGO%2FrUx3wh2OtME5cBZHZpllQIgaWOutJvba9YLTNQALuE6SzH0vZNOJrFgGT6SzJT8774q%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDAZvbDpeHHS%2FJDh84ircA5OEI7zPvDwafV%2FEbHRlrxQQN5P%2Brl5PkMDw%2Bm%2BY342g5Av44ySUsmkGPBgpjERI6BWx4ILWXCRBSiZJbDonni7%2FMOJJO4owlfzlyIbjxwbbmund1MxhoMTvK56JsgLGtncYcIrl0QVhUOl%2F%2BGmDQlpZiBq7A40z9x4ErvQW5ffuTWm4E%2BkCNv%2BJ4gW3HMwB%2FCUoQDW96%2F3kdnAZtpjRysizl3zRmW3RPa1FXICddG06sIdtw9mM6CZkZuwWjCFJ2FueuNuJ5Nqj53mNElWVoyet8XwT%2Fht2PvRKGhsYjM3MGzx0ZHyVjW8lA4JuKw7GIllBt%2BHeWZhJAs%2FyjBj2SHOridjfxlft4Lz9Ng9l9Y%2FlAGAqBcclG1KirYD%2BszfSafD8o%2B9NPDxPEdQ%2B65qreVsGIVst33UB1HE8xMqQal%2F0PD%2Bio4pTpCxoovHK9vudz%2BD7fUf3x%2FZ4RZcsI7JVjtsBUBxsIixTLEp8tikZnadL24AV4oeUzXeS7t0mJEaufrqX2NQb7MzvvN%2BNoU%2BFXSSetSmfTiFHyqH5VDvKiyIyfytIoPzrVsRtDf8aTQZdOpZ8jeo4u9ZsQQ7tw1JUKzMyiHeh76dszFr69wJnDRl%2BCPSsoYIrp0wdSsdQMLjkxL0GOqUBQ5BYEJSjLFygM9lAcu4Yl%2FbOKizwU9%2FqdGSm4fBqkHbbvcVXGEo7egOPLuZcXIOZ0Gh90q7LskL7V6udpsn6tpBcJ2aNs50XhrBSZjsCuZZJ8ES9qz4bcVePW1PjprJg9YfD7N9fZ3g2NSvUF79G%2Fa7EuaRr%2Fpg%2BT1Ugb4etYLLMu9F8nuENjR%2FQiK1z3jB1cxRLxUHeydK0fXsU%2BtL6V4%2FedzfB&X-Amz-Signature=8a5812ef80a3e66c712f5761243d8cf20f844a1069b65683ca63c550008e0d20&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VEHHMVXQ%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQCqZapSDi7guKF%2BSxaPLJGO%2FrUx3wh2OtME5cBZHZpllQIgaWOutJvba9YLTNQALuE6SzH0vZNOJrFgGT6SzJT8774q%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDAZvbDpeHHS%2FJDh84ircA5OEI7zPvDwafV%2FEbHRlrxQQN5P%2Brl5PkMDw%2Bm%2BY342g5Av44ySUsmkGPBgpjERI6BWx4ILWXCRBSiZJbDonni7%2FMOJJO4owlfzlyIbjxwbbmund1MxhoMTvK56JsgLGtncYcIrl0QVhUOl%2F%2BGmDQlpZiBq7A40z9x4ErvQW5ffuTWm4E%2BkCNv%2BJ4gW3HMwB%2FCUoQDW96%2F3kdnAZtpjRysizl3zRmW3RPa1FXICddG06sIdtw9mM6CZkZuwWjCFJ2FueuNuJ5Nqj53mNElWVoyet8XwT%2Fht2PvRKGhsYjM3MGzx0ZHyVjW8lA4JuKw7GIllBt%2BHeWZhJAs%2FyjBj2SHOridjfxlft4Lz9Ng9l9Y%2FlAGAqBcclG1KirYD%2BszfSafD8o%2B9NPDxPEdQ%2B65qreVsGIVst33UB1HE8xMqQal%2F0PD%2Bio4pTpCxoovHK9vudz%2BD7fUf3x%2FZ4RZcsI7JVjtsBUBxsIixTLEp8tikZnadL24AV4oeUzXeS7t0mJEaufrqX2NQb7MzvvN%2BNoU%2BFXSSetSmfTiFHyqH5VDvKiyIyfytIoPzrVsRtDf8aTQZdOpZ8jeo4u9ZsQQ7tw1JUKzMyiHeh76dszFr69wJnDRl%2BCPSsoYIrp0wdSsdQMLjkxL0GOqUBQ5BYEJSjLFygM9lAcu4Yl%2FbOKizwU9%2FqdGSm4fBqkHbbvcVXGEo7egOPLuZcXIOZ0Gh90q7LskL7V6udpsn6tpBcJ2aNs50XhrBSZjsCuZZJ8ES9qz4bcVePW1PjprJg9YfD7N9fZ3g2NSvUF79G%2Fa7EuaRr%2Fpg%2BT1Ugb4etYLLMu9F8nuENjR%2FQiK1z3jB1cxRLxUHeydK0fXsU%2BtL6V4%2FedzfB&X-Amz-Signature=f5e782c13030fbc921556bf4cf32b46440e68ce7cac7c31cdec8bd863a7bd182&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VEHHMVXQ%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQCqZapSDi7guKF%2BSxaPLJGO%2FrUx3wh2OtME5cBZHZpllQIgaWOutJvba9YLTNQALuE6SzH0vZNOJrFgGT6SzJT8774q%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDAZvbDpeHHS%2FJDh84ircA5OEI7zPvDwafV%2FEbHRlrxQQN5P%2Brl5PkMDw%2Bm%2BY342g5Av44ySUsmkGPBgpjERI6BWx4ILWXCRBSiZJbDonni7%2FMOJJO4owlfzlyIbjxwbbmund1MxhoMTvK56JsgLGtncYcIrl0QVhUOl%2F%2BGmDQlpZiBq7A40z9x4ErvQW5ffuTWm4E%2BkCNv%2BJ4gW3HMwB%2FCUoQDW96%2F3kdnAZtpjRysizl3zRmW3RPa1FXICddG06sIdtw9mM6CZkZuwWjCFJ2FueuNuJ5Nqj53mNElWVoyet8XwT%2Fht2PvRKGhsYjM3MGzx0ZHyVjW8lA4JuKw7GIllBt%2BHeWZhJAs%2FyjBj2SHOridjfxlft4Lz9Ng9l9Y%2FlAGAqBcclG1KirYD%2BszfSafD8o%2B9NPDxPEdQ%2B65qreVsGIVst33UB1HE8xMqQal%2F0PD%2Bio4pTpCxoovHK9vudz%2BD7fUf3x%2FZ4RZcsI7JVjtsBUBxsIixTLEp8tikZnadL24AV4oeUzXeS7t0mJEaufrqX2NQb7MzvvN%2BNoU%2BFXSSetSmfTiFHyqH5VDvKiyIyfytIoPzrVsRtDf8aTQZdOpZ8jeo4u9ZsQQ7tw1JUKzMyiHeh76dszFr69wJnDRl%2BCPSsoYIrp0wdSsdQMLjkxL0GOqUBQ5BYEJSjLFygM9lAcu4Yl%2FbOKizwU9%2FqdGSm4fBqkHbbvcVXGEo7egOPLuZcXIOZ0Gh90q7LskL7V6udpsn6tpBcJ2aNs50XhrBSZjsCuZZJ8ES9qz4bcVePW1PjprJg9YfD7N9fZ3g2NSvUF79G%2Fa7EuaRr%2Fpg%2BT1Ugb4etYLLMu9F8nuENjR%2FQiK1z3jB1cxRLxUHeydK0fXsU%2BtL6V4%2FedzfB&X-Amz-Signature=1977a940f66b5417c05ea02e798c87b9fc5a6b9beaef31b256b201639990cf36&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VEHHMVXQ%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQCqZapSDi7guKF%2BSxaPLJGO%2FrUx3wh2OtME5cBZHZpllQIgaWOutJvba9YLTNQALuE6SzH0vZNOJrFgGT6SzJT8774q%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDAZvbDpeHHS%2FJDh84ircA5OEI7zPvDwafV%2FEbHRlrxQQN5P%2Brl5PkMDw%2Bm%2BY342g5Av44ySUsmkGPBgpjERI6BWx4ILWXCRBSiZJbDonni7%2FMOJJO4owlfzlyIbjxwbbmund1MxhoMTvK56JsgLGtncYcIrl0QVhUOl%2F%2BGmDQlpZiBq7A40z9x4ErvQW5ffuTWm4E%2BkCNv%2BJ4gW3HMwB%2FCUoQDW96%2F3kdnAZtpjRysizl3zRmW3RPa1FXICddG06sIdtw9mM6CZkZuwWjCFJ2FueuNuJ5Nqj53mNElWVoyet8XwT%2Fht2PvRKGhsYjM3MGzx0ZHyVjW8lA4JuKw7GIllBt%2BHeWZhJAs%2FyjBj2SHOridjfxlft4Lz9Ng9l9Y%2FlAGAqBcclG1KirYD%2BszfSafD8o%2B9NPDxPEdQ%2B65qreVsGIVst33UB1HE8xMqQal%2F0PD%2Bio4pTpCxoovHK9vudz%2BD7fUf3x%2FZ4RZcsI7JVjtsBUBxsIixTLEp8tikZnadL24AV4oeUzXeS7t0mJEaufrqX2NQb7MzvvN%2BNoU%2BFXSSetSmfTiFHyqH5VDvKiyIyfytIoPzrVsRtDf8aTQZdOpZ8jeo4u9ZsQQ7tw1JUKzMyiHeh76dszFr69wJnDRl%2BCPSsoYIrp0wdSsdQMLjkxL0GOqUBQ5BYEJSjLFygM9lAcu4Yl%2FbOKizwU9%2FqdGSm4fBqkHbbvcVXGEo7egOPLuZcXIOZ0Gh90q7LskL7V6udpsn6tpBcJ2aNs50XhrBSZjsCuZZJ8ES9qz4bcVePW1PjprJg9YfD7N9fZ3g2NSvUF79G%2Fa7EuaRr%2Fpg%2BT1Ugb4etYLLMu9F8nuENjR%2FQiK1z3jB1cxRLxUHeydK0fXsU%2BtL6V4%2FedzfB&X-Amz-Signature=249d513ac6336f67911fa93c7c56e5cb37bef02785dd41ef575b56f1afcb0e32&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
