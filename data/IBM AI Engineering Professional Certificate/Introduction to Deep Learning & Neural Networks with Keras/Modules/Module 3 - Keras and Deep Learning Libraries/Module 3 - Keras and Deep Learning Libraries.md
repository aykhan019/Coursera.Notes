

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TAPD4WNS%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIDyPILq1vL7DtKDhDqIT5JJzHUw%2BFyF5rWwSGZ9bK%2FxOAiEAvnjwzzQoQxK124qCbUTbF%2FHVVF5Vorng%2FtQp8%2B6b1Egq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDKnk21KWa0QmGLVgaSrcA4l%2FDRm1UsiUnbiUOC%2F3G4zir7qvWS4He0XBnEBrjaTkRcAAcjSUEHKZiruK6il6JUF2w0E56N7AVMiYrpOx464zwsfe7ve6JGHf9Ay3TFKo9MwrI4Gw3ijopRtKtgwdJEeGNM42U1a6k0ilMfDehZh3O9yhArGyNzNitbAwgEE8zy9a6fHA2xrtb4F3uO%2FcRJCRz13eGkrku9%2BAz7mzPBcz2vAi7D6Pf7fEpvksWMlJuDv1IK5jxxEsoUVHL6cXe8Qy%2B8NgeRmfWbRoiIJ5BcQaCkyPfxUoGKLodxHfdcsu5dxAeVjZ7EIAeHCPQlQrvk4ULlSNiPZKMivkzHNpau4q2DqDh0o3N5zxV6HpQtoiftXq4Sk2wTKa0Eqvv45B3qq0bdygIkeC0Wb7do240A%2Bu0rvnJ9xL6yy5vU75TLrmUvhZkXMIqt5G4wOrs%2BbWW%2FNsAJo%2F68WVOb78QkxytYDRQsDuTHiyXo1twl1qXZ1IO%2FTjJEdIedqHi4%2BDdZKVFaMqHvp4Bm8XlgcySNHUjJIQPUqhrnFU83mN6NxeX6FpyDHcMzgbXqAzOxjZlRwBk6YncNPytfQhp3npi2LkWEgd%2BIWrvYdj%2BVzTr3Jw%2FrdYFjH9uCnR%2B6VfFcBEMO2ps74GOqUBQzhsHf8oyUIILeuXBBSjde2QT%2F9y3t0qs2ZzSDTEGbXG6yDbjDfRoo1Ri%2BrOYVyRi41k3YtGDqe0ShHijaIS8hGvIeKc0RRu3%2FaXpTIqokRR4m8lWd7oTSOKGmqZuo4QMDw2sowHh1DLLNsya0%2FWP7TIjQq39JZuFu8yJHOisAunHdU%2FlG6mdr5UbicKcpDbpgoUDJGOc%2F8C%2FFY8zg7lhLVmp4wj&X-Amz-Signature=94f8a263c5aa8f87ce03b2b73e4912b06b519e2f43c2ec7a7b193b74cbae4f7d&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TAPD4WNS%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIDyPILq1vL7DtKDhDqIT5JJzHUw%2BFyF5rWwSGZ9bK%2FxOAiEAvnjwzzQoQxK124qCbUTbF%2FHVVF5Vorng%2FtQp8%2B6b1Egq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDKnk21KWa0QmGLVgaSrcA4l%2FDRm1UsiUnbiUOC%2F3G4zir7qvWS4He0XBnEBrjaTkRcAAcjSUEHKZiruK6il6JUF2w0E56N7AVMiYrpOx464zwsfe7ve6JGHf9Ay3TFKo9MwrI4Gw3ijopRtKtgwdJEeGNM42U1a6k0ilMfDehZh3O9yhArGyNzNitbAwgEE8zy9a6fHA2xrtb4F3uO%2FcRJCRz13eGkrku9%2BAz7mzPBcz2vAi7D6Pf7fEpvksWMlJuDv1IK5jxxEsoUVHL6cXe8Qy%2B8NgeRmfWbRoiIJ5BcQaCkyPfxUoGKLodxHfdcsu5dxAeVjZ7EIAeHCPQlQrvk4ULlSNiPZKMivkzHNpau4q2DqDh0o3N5zxV6HpQtoiftXq4Sk2wTKa0Eqvv45B3qq0bdygIkeC0Wb7do240A%2Bu0rvnJ9xL6yy5vU75TLrmUvhZkXMIqt5G4wOrs%2BbWW%2FNsAJo%2F68WVOb78QkxytYDRQsDuTHiyXo1twl1qXZ1IO%2FTjJEdIedqHi4%2BDdZKVFaMqHvp4Bm8XlgcySNHUjJIQPUqhrnFU83mN6NxeX6FpyDHcMzgbXqAzOxjZlRwBk6YncNPytfQhp3npi2LkWEgd%2BIWrvYdj%2BVzTr3Jw%2FrdYFjH9uCnR%2B6VfFcBEMO2ps74GOqUBQzhsHf8oyUIILeuXBBSjde2QT%2F9y3t0qs2ZzSDTEGbXG6yDbjDfRoo1Ri%2BrOYVyRi41k3YtGDqe0ShHijaIS8hGvIeKc0RRu3%2FaXpTIqokRR4m8lWd7oTSOKGmqZuo4QMDw2sowHh1DLLNsya0%2FWP7TIjQq39JZuFu8yJHOisAunHdU%2FlG6mdr5UbicKcpDbpgoUDJGOc%2F8C%2FFY8zg7lhLVmp4wj&X-Amz-Signature=9e336c1b554619944abc28de4a37cba27f2aaa240b7b69d9781b73d50df2cf49&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TAPD4WNS%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIDyPILq1vL7DtKDhDqIT5JJzHUw%2BFyF5rWwSGZ9bK%2FxOAiEAvnjwzzQoQxK124qCbUTbF%2FHVVF5Vorng%2FtQp8%2B6b1Egq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDKnk21KWa0QmGLVgaSrcA4l%2FDRm1UsiUnbiUOC%2F3G4zir7qvWS4He0XBnEBrjaTkRcAAcjSUEHKZiruK6il6JUF2w0E56N7AVMiYrpOx464zwsfe7ve6JGHf9Ay3TFKo9MwrI4Gw3ijopRtKtgwdJEeGNM42U1a6k0ilMfDehZh3O9yhArGyNzNitbAwgEE8zy9a6fHA2xrtb4F3uO%2FcRJCRz13eGkrku9%2BAz7mzPBcz2vAi7D6Pf7fEpvksWMlJuDv1IK5jxxEsoUVHL6cXe8Qy%2B8NgeRmfWbRoiIJ5BcQaCkyPfxUoGKLodxHfdcsu5dxAeVjZ7EIAeHCPQlQrvk4ULlSNiPZKMivkzHNpau4q2DqDh0o3N5zxV6HpQtoiftXq4Sk2wTKa0Eqvv45B3qq0bdygIkeC0Wb7do240A%2Bu0rvnJ9xL6yy5vU75TLrmUvhZkXMIqt5G4wOrs%2BbWW%2FNsAJo%2F68WVOb78QkxytYDRQsDuTHiyXo1twl1qXZ1IO%2FTjJEdIedqHi4%2BDdZKVFaMqHvp4Bm8XlgcySNHUjJIQPUqhrnFU83mN6NxeX6FpyDHcMzgbXqAzOxjZlRwBk6YncNPytfQhp3npi2LkWEgd%2BIWrvYdj%2BVzTr3Jw%2FrdYFjH9uCnR%2B6VfFcBEMO2ps74GOqUBQzhsHf8oyUIILeuXBBSjde2QT%2F9y3t0qs2ZzSDTEGbXG6yDbjDfRoo1Ri%2BrOYVyRi41k3YtGDqe0ShHijaIS8hGvIeKc0RRu3%2FaXpTIqokRR4m8lWd7oTSOKGmqZuo4QMDw2sowHh1DLLNsya0%2FWP7TIjQq39JZuFu8yJHOisAunHdU%2FlG6mdr5UbicKcpDbpgoUDJGOc%2F8C%2FFY8zg7lhLVmp4wj&X-Amz-Signature=9fc8130fb281a3521a6196d55f88382304983857ccc513545ea6e1fd8d1902b3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VNCHV6FQ%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003533Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQDedQd%2B4ZCS1pw4AK9LzpZ1td9uM5pqt0wunQstG9P%2FkQIhAJeNVT1zLa9myx1asO44yQJAdmnz8ygsc7gwX2YIodeeKv8DCGkQABoMNjM3NDIzMTgzODA1IgzKDshxow0f0IDHAFQq3ANSarXQWbS6jownXOXFDiNgC5Fdc31GSgtizqR7%2BeptxCRTDg9XHQbNkXJ89uQmQYSvol4jpJKndkL7GJwy2JxrzFVRnHEfFPq2Sg0DC4gSAa19%2Fw6ptevaoBNBqkeWTBpaVTx1Fr3p8P05it8YzH3RP4X23q7nvRrR3jrUFPgLSHIaLbSXxRq0q262TR1fT1AZIbZjEW%2Fu2MsScZwzEYmgCXoykPy5RPz%2BVtttHQxIUmXWBOcS48i4mE3Jj59A5hW76hjbeV0O5FxlKfmCe4ESgPwBkMtu1exI%2FFjHB8DaTaYV2XlZnaU7FLEQu0z58iID3f1kbkpnnbcsSJ0rCV4JUjMJsqs%2BHzEF1%2Fgwk%2BtJpAKyP68jKo23%2BnSar%2FodWOFzOSmcmjABXnyQEOTz2Nda3IeS7gTa8UJ5n%2FSCQi5tT6fFNmjjHg5%2FSUWwxB3wc%2Bj02ZuOaqwXCjT7ogdRoFZ%2F8iz%2BUZQZAAJxyeRzjWX%2F9KskklYn0Px6qNpguojL%2BkG4Jvd40zQHToH8LwAx3W264dJL9WFVVeH6%2BCzCEwgjdxSBUPzEn3bOAK9uxFb2yMXguLinYhVEAeO59dQ0Kt%2Fb0wFgTiEfTLneBGiediBh3iB1qx5ZNAIka0fIOzDkqbO%2BBjqkAVtC26iLBjQCO%2BmPiP8eG6VL4liei%2FX6C3xgzRS9oRsLPLbPxQVRJk%2FwsMgo40gUIEPz1QfkaqEaZ1TPYpGqdK%2BDA0yJg%2BxnVAlHDrDDr692IGLazuFKV9x6uc9U9dk%2Fzula%2BjHW2ZWknX8VmRoomw2bHXAFsBn7ECB4O6139klyWo3ef1yqm4pXkUkfHMvDgPeQ675hNnZrgWPBDKelXxG7oHjC&X-Amz-Signature=1e444c68ce72cec85eb514e384bf3d9dc70c3da9f7ef213e6b0da08f92768294&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WUT6DROG%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003533Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIBwpR4IwPIUCfAGJYvv7dL%2B%2BzzSwr%2BzTiccQ4xwtuoRfAiBwOAoeXLMvMQHkOScQWasF12wW0pZHRqGkZKrtqdMpfyr%2FAwhpEAAaDDYzNzQyMzE4MzgwNSIMW9hg4CNS2G2qGu14KtwDgXxFZQ2XcPYOr%2FbEdZ6Rxdaehxvp278noxWJADQ%2FDOYN2eeXmc7nJ4MhRrUMsyXq3%2BaayrQuHEORBZo2StSoi58Ppi9RUuubxlrCFFy1Z1A8VMdz7Plja0cyq7EWR2YNu7X2DWw4cCMmum%2FL8tKFJ71nwTSFAsOFX763z6%2F%2FDmb%2F9DKl9unVN4EebaL7x4SXnqAs4lTmo7r8Z77kvKPGr6nJTNy78ESTRffjXGbBXjGUUFeLTmMyM1KYE566%2FjuBrF87%2FesNhJhGm2lZvssKL9uuk6ZBzZxzZ3BA9V3YKHESisQbCw%2F9jPMWgxucATL1VY%2BT%2BSY8cRGS41x6MiiasqN6kH43kASkSXtf59oqgHdsjqyyR8pQKSjqJeL35rmnmfW%2B5rAPPJ3wNEArNGhjpmvXcp5p1dAujzyCvmoYcktTn5r65pZigyR7M2ta8jvalSn2ey56nqFRO76%2BIKjR0%2BLZqLlprB%2FUtc8hl%2BATSFP16rzLUc2b8rV%2BoDRqwMZuu9Ex7vlE3OSe2gpZGhLE91tJtx%2BrfoUUFwlMiM7ZHD0RbV8xBzcbkUCx5PFNzV%2BnyevVPviRVj9uY7614SgUZ%2FWmkujin5a%2FPz2oMvlFQIihMqNUzMfOoFxMrywwvKmzvgY6pgEaxKBVP6IMjIxZ4Gsn141USASZq9GX%2Bju0fsxxG%2BK81aIg3pBX2Py3anSiwMJfuUOZEj5915C33s3joVE3wnaihyF40doYk7ILwmM4PCoCUwFB9cwZnrtIvQ%2Fs9qnV%2BhD5o6%2Fd73J7cK3cPEuctccUkhVk%2FFMYk7bzQ0qA%2FMRztTWoa2FJ%2BmoUdy0d7d0DcKX7a6MGOJEpihof3VBPDdXnmnoReCDg&X-Amz-Signature=e9550ebb55ca0ea8354227be812c6114bb52de6ae7c06611c68df3f08327b83d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TAPD4WNS%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIDyPILq1vL7DtKDhDqIT5JJzHUw%2BFyF5rWwSGZ9bK%2FxOAiEAvnjwzzQoQxK124qCbUTbF%2FHVVF5Vorng%2FtQp8%2B6b1Egq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDKnk21KWa0QmGLVgaSrcA4l%2FDRm1UsiUnbiUOC%2F3G4zir7qvWS4He0XBnEBrjaTkRcAAcjSUEHKZiruK6il6JUF2w0E56N7AVMiYrpOx464zwsfe7ve6JGHf9Ay3TFKo9MwrI4Gw3ijopRtKtgwdJEeGNM42U1a6k0ilMfDehZh3O9yhArGyNzNitbAwgEE8zy9a6fHA2xrtb4F3uO%2FcRJCRz13eGkrku9%2BAz7mzPBcz2vAi7D6Pf7fEpvksWMlJuDv1IK5jxxEsoUVHL6cXe8Qy%2B8NgeRmfWbRoiIJ5BcQaCkyPfxUoGKLodxHfdcsu5dxAeVjZ7EIAeHCPQlQrvk4ULlSNiPZKMivkzHNpau4q2DqDh0o3N5zxV6HpQtoiftXq4Sk2wTKa0Eqvv45B3qq0bdygIkeC0Wb7do240A%2Bu0rvnJ9xL6yy5vU75TLrmUvhZkXMIqt5G4wOrs%2BbWW%2FNsAJo%2F68WVOb78QkxytYDRQsDuTHiyXo1twl1qXZ1IO%2FTjJEdIedqHi4%2BDdZKVFaMqHvp4Bm8XlgcySNHUjJIQPUqhrnFU83mN6NxeX6FpyDHcMzgbXqAzOxjZlRwBk6YncNPytfQhp3npi2LkWEgd%2BIWrvYdj%2BVzTr3Jw%2FrdYFjH9uCnR%2B6VfFcBEMO2ps74GOqUBQzhsHf8oyUIILeuXBBSjde2QT%2F9y3t0qs2ZzSDTEGbXG6yDbjDfRoo1Ri%2BrOYVyRi41k3YtGDqe0ShHijaIS8hGvIeKc0RRu3%2FaXpTIqokRR4m8lWd7oTSOKGmqZuo4QMDw2sowHh1DLLNsya0%2FWP7TIjQq39JZuFu8yJHOisAunHdU%2FlG6mdr5UbicKcpDbpgoUDJGOc%2F8C%2FFY8zg7lhLVmp4wj&X-Amz-Signature=22fa77aa13d78cc0084acd28c4a7c16f23b561187d3b4ac24945d1e50003b11d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TAPD4WNS%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIDyPILq1vL7DtKDhDqIT5JJzHUw%2BFyF5rWwSGZ9bK%2FxOAiEAvnjwzzQoQxK124qCbUTbF%2FHVVF5Vorng%2FtQp8%2B6b1Egq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDKnk21KWa0QmGLVgaSrcA4l%2FDRm1UsiUnbiUOC%2F3G4zir7qvWS4He0XBnEBrjaTkRcAAcjSUEHKZiruK6il6JUF2w0E56N7AVMiYrpOx464zwsfe7ve6JGHf9Ay3TFKo9MwrI4Gw3ijopRtKtgwdJEeGNM42U1a6k0ilMfDehZh3O9yhArGyNzNitbAwgEE8zy9a6fHA2xrtb4F3uO%2FcRJCRz13eGkrku9%2BAz7mzPBcz2vAi7D6Pf7fEpvksWMlJuDv1IK5jxxEsoUVHL6cXe8Qy%2B8NgeRmfWbRoiIJ5BcQaCkyPfxUoGKLodxHfdcsu5dxAeVjZ7EIAeHCPQlQrvk4ULlSNiPZKMivkzHNpau4q2DqDh0o3N5zxV6HpQtoiftXq4Sk2wTKa0Eqvv45B3qq0bdygIkeC0Wb7do240A%2Bu0rvnJ9xL6yy5vU75TLrmUvhZkXMIqt5G4wOrs%2BbWW%2FNsAJo%2F68WVOb78QkxytYDRQsDuTHiyXo1twl1qXZ1IO%2FTjJEdIedqHi4%2BDdZKVFaMqHvp4Bm8XlgcySNHUjJIQPUqhrnFU83mN6NxeX6FpyDHcMzgbXqAzOxjZlRwBk6YncNPytfQhp3npi2LkWEgd%2BIWrvYdj%2BVzTr3Jw%2FrdYFjH9uCnR%2B6VfFcBEMO2ps74GOqUBQzhsHf8oyUIILeuXBBSjde2QT%2F9y3t0qs2ZzSDTEGbXG6yDbjDfRoo1Ri%2BrOYVyRi41k3YtGDqe0ShHijaIS8hGvIeKc0RRu3%2FaXpTIqokRR4m8lWd7oTSOKGmqZuo4QMDw2sowHh1DLLNsya0%2FWP7TIjQq39JZuFu8yJHOisAunHdU%2FlG6mdr5UbicKcpDbpgoUDJGOc%2F8C%2FFY8zg7lhLVmp4wj&X-Amz-Signature=eeaee0065498994070b00746cbe447821621bcff3d75ac900b62491a0393bd39&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TAPD4WNS%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIDyPILq1vL7DtKDhDqIT5JJzHUw%2BFyF5rWwSGZ9bK%2FxOAiEAvnjwzzQoQxK124qCbUTbF%2FHVVF5Vorng%2FtQp8%2B6b1Egq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDKnk21KWa0QmGLVgaSrcA4l%2FDRm1UsiUnbiUOC%2F3G4zir7qvWS4He0XBnEBrjaTkRcAAcjSUEHKZiruK6il6JUF2w0E56N7AVMiYrpOx464zwsfe7ve6JGHf9Ay3TFKo9MwrI4Gw3ijopRtKtgwdJEeGNM42U1a6k0ilMfDehZh3O9yhArGyNzNitbAwgEE8zy9a6fHA2xrtb4F3uO%2FcRJCRz13eGkrku9%2BAz7mzPBcz2vAi7D6Pf7fEpvksWMlJuDv1IK5jxxEsoUVHL6cXe8Qy%2B8NgeRmfWbRoiIJ5BcQaCkyPfxUoGKLodxHfdcsu5dxAeVjZ7EIAeHCPQlQrvk4ULlSNiPZKMivkzHNpau4q2DqDh0o3N5zxV6HpQtoiftXq4Sk2wTKa0Eqvv45B3qq0bdygIkeC0Wb7do240A%2Bu0rvnJ9xL6yy5vU75TLrmUvhZkXMIqt5G4wOrs%2BbWW%2FNsAJo%2F68WVOb78QkxytYDRQsDuTHiyXo1twl1qXZ1IO%2FTjJEdIedqHi4%2BDdZKVFaMqHvp4Bm8XlgcySNHUjJIQPUqhrnFU83mN6NxeX6FpyDHcMzgbXqAzOxjZlRwBk6YncNPytfQhp3npi2LkWEgd%2BIWrvYdj%2BVzTr3Jw%2FrdYFjH9uCnR%2B6VfFcBEMO2ps74GOqUBQzhsHf8oyUIILeuXBBSjde2QT%2F9y3t0qs2ZzSDTEGbXG6yDbjDfRoo1Ri%2BrOYVyRi41k3YtGDqe0ShHijaIS8hGvIeKc0RRu3%2FaXpTIqokRR4m8lWd7oTSOKGmqZuo4QMDw2sowHh1DLLNsya0%2FWP7TIjQq39JZuFu8yJHOisAunHdU%2FlG6mdr5UbicKcpDbpgoUDJGOc%2F8C%2FFY8zg7lhLVmp4wj&X-Amz-Signature=b27f608230cd33f76510ff96064cae0a5e02d2ca033e0d236f37fb51fa7a18c4&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TAPD4WNS%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIDyPILq1vL7DtKDhDqIT5JJzHUw%2BFyF5rWwSGZ9bK%2FxOAiEAvnjwzzQoQxK124qCbUTbF%2FHVVF5Vorng%2FtQp8%2B6b1Egq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDKnk21KWa0QmGLVgaSrcA4l%2FDRm1UsiUnbiUOC%2F3G4zir7qvWS4He0XBnEBrjaTkRcAAcjSUEHKZiruK6il6JUF2w0E56N7AVMiYrpOx464zwsfe7ve6JGHf9Ay3TFKo9MwrI4Gw3ijopRtKtgwdJEeGNM42U1a6k0ilMfDehZh3O9yhArGyNzNitbAwgEE8zy9a6fHA2xrtb4F3uO%2FcRJCRz13eGkrku9%2BAz7mzPBcz2vAi7D6Pf7fEpvksWMlJuDv1IK5jxxEsoUVHL6cXe8Qy%2B8NgeRmfWbRoiIJ5BcQaCkyPfxUoGKLodxHfdcsu5dxAeVjZ7EIAeHCPQlQrvk4ULlSNiPZKMivkzHNpau4q2DqDh0o3N5zxV6HpQtoiftXq4Sk2wTKa0Eqvv45B3qq0bdygIkeC0Wb7do240A%2Bu0rvnJ9xL6yy5vU75TLrmUvhZkXMIqt5G4wOrs%2BbWW%2FNsAJo%2F68WVOb78QkxytYDRQsDuTHiyXo1twl1qXZ1IO%2FTjJEdIedqHi4%2BDdZKVFaMqHvp4Bm8XlgcySNHUjJIQPUqhrnFU83mN6NxeX6FpyDHcMzgbXqAzOxjZlRwBk6YncNPytfQhp3npi2LkWEgd%2BIWrvYdj%2BVzTr3Jw%2FrdYFjH9uCnR%2B6VfFcBEMO2ps74GOqUBQzhsHf8oyUIILeuXBBSjde2QT%2F9y3t0qs2ZzSDTEGbXG6yDbjDfRoo1Ri%2BrOYVyRi41k3YtGDqe0ShHijaIS8hGvIeKc0RRu3%2FaXpTIqokRR4m8lWd7oTSOKGmqZuo4QMDw2sowHh1DLLNsya0%2FWP7TIjQq39JZuFu8yJHOisAunHdU%2FlG6mdr5UbicKcpDbpgoUDJGOc%2F8C%2FFY8zg7lhLVmp4wj&X-Amz-Signature=1e9d8b073c195495e08328dcff5d657cc60287afe64a0d446c46d99f41247b67&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
