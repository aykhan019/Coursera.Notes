

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OFCHQSX%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132013Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIBcQPqstF%2FSaNCXnDo%2FDPBXJJxxsdZ0kPeDCd%2FTy4apNAiEAu4%2Fto3rA03SvML5fyW%2BJf%2FYdaBrCsjc9fbC5XPOuh%2FIq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDJon%2FfR2sdyuAjb0zSrcA8iXHsR%2FhYXl7WUzYBn594HQGeuI1NHI5lRbdiay%2F74dDZv7%2FP1BBj8T1gFt5bY%2BQFbdArA8XXC90Yq0ChevHnERmViJ7wXa2WSNLCJpmHEnCWgyCOCiQJoZtMFLUYsOYDcIoBqbVNjsDmDC1bmb7iZOk9tmAxRK1kPhYS9m8jkBwoWmPUqFMXw0kXAlCCIY1CmD%2BrmcgIWP18%2Bjx8G3W0C4CC5%2B5He1%2FzLPYrEdg05A7VKpqNjvUHnCtaiYNapv7Re9Y5nG56DDfzt5NUzJNMgn5Q6l8ymY5mPIgjU1C9HYAb5qR%2FXlMeS3yDy%2Bt%2Bc3zHc92ZKU6LdvQ7zxO0JcWBTGuHdXiTUvKMgfqtUMiZ%2B275Mc2UU9wN8eckT9VXXUU9xLmAC4PtOtuWe5ACS9EtVmLjmv9vEU8S1TkfxgBEmAloGkHaN1RLjd0L%2B1z%2BQVwVZ3rhwhJM6n4WDnSwpXl77uiwSKqF%2Fc5V7n%2FsJ5FoVe7n4GnxQFdmtVQunP26XGzN6STOgDo8OOF7dp2oVJEauWxSsNCwEaBRAno9JEKX430yfYCXesELVYMrOMIUUYklCnTTLT8osJm9wH3BXDsQKE5Q3mxPUm5UU7uiHr9Dm3W%2FQKZYxSe%2FsCpiEwMPOKmL0GOqUBozFzzJ9b4iJ1L8FpOscRSxIsWnXkgfFdDtIQWNiuq0vvvMbk1xPHuiI%2FqYKF3on5PlkkTT4%2BEf%2Bz4aurv544c1k0hf1mMMhazOqIElwM8Dpsor4tzK4x0VUrjwrxb5o5RFuscYS0tkiLBIN7G3gZGQGWZUB7z%2BymirQfk6qGPVbpNqukHVmKexWFaP5aj6l78QRzhZ00vstFNLulkgynptyaVX%2Ba&X-Amz-Signature=3051869fa6f807f45937eb7a83c45afc919b1b86ca5457055c27aa824ac12c64&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OFCHQSX%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132013Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIBcQPqstF%2FSaNCXnDo%2FDPBXJJxxsdZ0kPeDCd%2FTy4apNAiEAu4%2Fto3rA03SvML5fyW%2BJf%2FYdaBrCsjc9fbC5XPOuh%2FIq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDJon%2FfR2sdyuAjb0zSrcA8iXHsR%2FhYXl7WUzYBn594HQGeuI1NHI5lRbdiay%2F74dDZv7%2FP1BBj8T1gFt5bY%2BQFbdArA8XXC90Yq0ChevHnERmViJ7wXa2WSNLCJpmHEnCWgyCOCiQJoZtMFLUYsOYDcIoBqbVNjsDmDC1bmb7iZOk9tmAxRK1kPhYS9m8jkBwoWmPUqFMXw0kXAlCCIY1CmD%2BrmcgIWP18%2Bjx8G3W0C4CC5%2B5He1%2FzLPYrEdg05A7VKpqNjvUHnCtaiYNapv7Re9Y5nG56DDfzt5NUzJNMgn5Q6l8ymY5mPIgjU1C9HYAb5qR%2FXlMeS3yDy%2Bt%2Bc3zHc92ZKU6LdvQ7zxO0JcWBTGuHdXiTUvKMgfqtUMiZ%2B275Mc2UU9wN8eckT9VXXUU9xLmAC4PtOtuWe5ACS9EtVmLjmv9vEU8S1TkfxgBEmAloGkHaN1RLjd0L%2B1z%2BQVwVZ3rhwhJM6n4WDnSwpXl77uiwSKqF%2Fc5V7n%2FsJ5FoVe7n4GnxQFdmtVQunP26XGzN6STOgDo8OOF7dp2oVJEauWxSsNCwEaBRAno9JEKX430yfYCXesELVYMrOMIUUYklCnTTLT8osJm9wH3BXDsQKE5Q3mxPUm5UU7uiHr9Dm3W%2FQKZYxSe%2FsCpiEwMPOKmL0GOqUBozFzzJ9b4iJ1L8FpOscRSxIsWnXkgfFdDtIQWNiuq0vvvMbk1xPHuiI%2FqYKF3on5PlkkTT4%2BEf%2Bz4aurv544c1k0hf1mMMhazOqIElwM8Dpsor4tzK4x0VUrjwrxb5o5RFuscYS0tkiLBIN7G3gZGQGWZUB7z%2BymirQfk6qGPVbpNqukHVmKexWFaP5aj6l78QRzhZ00vstFNLulkgynptyaVX%2Ba&X-Amz-Signature=bd8984ed2bffcc43575efe61d5f028c5e160ac1296580a212b125e1cb1abf368&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OFCHQSX%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132013Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIBcQPqstF%2FSaNCXnDo%2FDPBXJJxxsdZ0kPeDCd%2FTy4apNAiEAu4%2Fto3rA03SvML5fyW%2BJf%2FYdaBrCsjc9fbC5XPOuh%2FIq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDJon%2FfR2sdyuAjb0zSrcA8iXHsR%2FhYXl7WUzYBn594HQGeuI1NHI5lRbdiay%2F74dDZv7%2FP1BBj8T1gFt5bY%2BQFbdArA8XXC90Yq0ChevHnERmViJ7wXa2WSNLCJpmHEnCWgyCOCiQJoZtMFLUYsOYDcIoBqbVNjsDmDC1bmb7iZOk9tmAxRK1kPhYS9m8jkBwoWmPUqFMXw0kXAlCCIY1CmD%2BrmcgIWP18%2Bjx8G3W0C4CC5%2B5He1%2FzLPYrEdg05A7VKpqNjvUHnCtaiYNapv7Re9Y5nG56DDfzt5NUzJNMgn5Q6l8ymY5mPIgjU1C9HYAb5qR%2FXlMeS3yDy%2Bt%2Bc3zHc92ZKU6LdvQ7zxO0JcWBTGuHdXiTUvKMgfqtUMiZ%2B275Mc2UU9wN8eckT9VXXUU9xLmAC4PtOtuWe5ACS9EtVmLjmv9vEU8S1TkfxgBEmAloGkHaN1RLjd0L%2B1z%2BQVwVZ3rhwhJM6n4WDnSwpXl77uiwSKqF%2Fc5V7n%2FsJ5FoVe7n4GnxQFdmtVQunP26XGzN6STOgDo8OOF7dp2oVJEauWxSsNCwEaBRAno9JEKX430yfYCXesELVYMrOMIUUYklCnTTLT8osJm9wH3BXDsQKE5Q3mxPUm5UU7uiHr9Dm3W%2FQKZYxSe%2FsCpiEwMPOKmL0GOqUBozFzzJ9b4iJ1L8FpOscRSxIsWnXkgfFdDtIQWNiuq0vvvMbk1xPHuiI%2FqYKF3on5PlkkTT4%2BEf%2Bz4aurv544c1k0hf1mMMhazOqIElwM8Dpsor4tzK4x0VUrjwrxb5o5RFuscYS0tkiLBIN7G3gZGQGWZUB7z%2BymirQfk6qGPVbpNqukHVmKexWFaP5aj6l78QRzhZ00vstFNLulkgynptyaVX%2Ba&X-Amz-Signature=3d026847d0c79737e3b8826de5d8d6e793a8550ac89acb00bd0f9ab4873d2839&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466765J3T2O%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCIBJoVfRmYDsqcaByEWkV7PBv1jLFgFPlzfauA5EV4cHoAiAeYUcn7%2B8V0nj21A%2FdiAPeaFzCg7Pu%2Fe6O1pymeBME%2Bir%2FAwh2EAAaDDYzNzQyMzE4MzgwNSIMSuvLrHe%2BmCsLJRP5KtwDUpLJypQYNyCGFIcZbC82FqxoQwAuQjrUcnN8U3aHz9zTOJ1fNqJG2PibhlQmG7y6Oviy3jGR6OzxWYAxo4YuEwZ%2FTHeazSJbhF%2BznQBIlwG70eicIUr8p2ltA7ciiV%2BdkPvds15sloQpj0Em4VQMcaw83uYq1un549Za8PGvSjjfTUqY10%2F7RJ0FR2d4%2B8iUpMl2NogLQCjNLhlXCEz2bU9tr%2Bd5DVr0Vv3DDtc4%2B1HCD1uOCfgiUDPSG3urSnApMZQjQng6K7NT3I6iJE9X9notlRrzwMZ5BKQDvyL9rA9dZZdw0IPA0ipRe54pH8XoJoSpZ2tdeuITIEEc%2B%2B9PCEvfHDRXjMF46QSd9c7eTQnUQmmOxVFIpJtH6mn8x7M8SsKnm4HmNXFS1%2BzBgFC%2B4L%2FilaaMpmxFa%2B%2Bd7%2Fj8fA2Ftl7b6cplbDcYDtmI7KKIkOEabyul3IhDGrLhZFYwv46HAJ5dULXCJD3nLhfxLE5yNgdyzBOQAtCWaRAV1vAyzx2U2AsMvJvreObxaSNT97419WQBXZJf%2FyMlP5%2FdROQA6LdShe37%2BckELlrRcMuQfVFEdeG%2FrE8zchTKkp4ZlZxNiw1bX9Lri7HHwHqHxXuUr7oXuKaeuAOT%2BrMwi4uYvQY6pgEvQgy0TXzjD22bo9XEGscGGi4cKsII1hOQiq8%2Bm7iAuOIB%2Bni8dsY%2Bl5i5DLHAUuJ%2F7XU5JFT2lbv%2FreuRn1t56dk8%2FQNPYQAzCwQn%2B8xSUFvKn7rK8Xwz%2BmGLERHlddgWyaBhgSswbGL2z4Fxth2urXSxwlqM0xpmJ72cGkfk3zzwLmjCFEhOMbcPhmWABr%2FWLDfOZ1pTduPMk80Vab4HgIAlO%2Bdm&X-Amz-Signature=f6cced8b153cbd59d17ffc2a67d004cc52fad1fb686af6b7b67794dbd3fb6590&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WWGURFQS%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJIMEYCIQCmAltcHrrHW4Edn4W9%2BHKfbEqWAiwvx6ICb6fcEpUxCwIhAI%2FzEwfPDW1aGgdAw%2FKbv11gaxXg3TaeUZ5cwvkybGWAKv8DCHYQABoMNjM3NDIzMTgzODA1Igwql6LthXlgdGRbvagq3ANe6uOUPI%2Fuxjqd5Sa%2BEK76nXFLusmFlKEfHqwyxI%2FQeT2%2Bk%2FXsvnaxeZv4lMI3SCQn%2BVwkirJ6TS4ngwDfZbXYbmov7BqhaGVKHUFt2yu9sIRlw8s62aMsEsdU89qcX2Fbn8dU1Nor0fIHkfJYlSFfbIeTnpg8CUcEWMnKDuD4O1P4UYtY5QvC39iJSGSpwEjHzo3lJS9039bKBzOmdGrMLtgwcv5%2BA9YdkzMcTQ26FaRK1otWtkcflG3vxKos%2FYRJuo%2B0gd8aT0fPViROsfG9OkNMNdAS9R6K4BtyE7vcEeyXaBKF7PBY1YLhtIGpyUGYxZqqaJJYnp4TU2lLpLHvIQFazQJgA%2BqQt%2FCfS23UdSHwBczUWb8Kl1izELa%2B%2B2EP3eSboMdlpASookgGl8HYcj4vjZJZkCD6ah9TztgqYwH24T8nU45KYphjKN8pVDS01iOxuk6d2UVjB9kw8QCNYabQVZtUebGZ6gHIGjaj4kKKeVMLplfLo7EdRDNi%2FEGKEh6M84Fffp3Vhr77llyDYFD0L6QlGhNFjRAnPYN2hhOHjbG%2BtlqD6NxrrjIiaO%2BRF9RokYKJ%2FJPtSlhnZvNVbh297%2BeV%2BwOd933C6k5NWGN6l9ro5HA9XrZS%2FTCHi5i9BjqkAYKa1BurqOafC4hPzMCbOLi6le%2BCl4DQ2lvo8y0wKbjXPXEzIZxV%2BDc1r2m1%2FB88JuyBfrG%2BQCiFs6ciE8s2kJq1tvoz%2BjvKRiBPXRwjJTIg0fPymKHXV6CuUwG%2FYRG9JYd1onJBbtOVLGI5al1NXqF46KUZ3Mpfe34UQp0bRgQJDbPc6IEAVNp47B7kEqHdQ%2F38uxsppXueh1TLB3F%2FQOsbaL1P&X-Amz-Signature=33d1a3e1da0b324e465e54b11dd8e88fea9fe52ba21bdfe2e5728af2de39c2eb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OFCHQSX%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132013Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIBcQPqstF%2FSaNCXnDo%2FDPBXJJxxsdZ0kPeDCd%2FTy4apNAiEAu4%2Fto3rA03SvML5fyW%2BJf%2FYdaBrCsjc9fbC5XPOuh%2FIq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDJon%2FfR2sdyuAjb0zSrcA8iXHsR%2FhYXl7WUzYBn594HQGeuI1NHI5lRbdiay%2F74dDZv7%2FP1BBj8T1gFt5bY%2BQFbdArA8XXC90Yq0ChevHnERmViJ7wXa2WSNLCJpmHEnCWgyCOCiQJoZtMFLUYsOYDcIoBqbVNjsDmDC1bmb7iZOk9tmAxRK1kPhYS9m8jkBwoWmPUqFMXw0kXAlCCIY1CmD%2BrmcgIWP18%2Bjx8G3W0C4CC5%2B5He1%2FzLPYrEdg05A7VKpqNjvUHnCtaiYNapv7Re9Y5nG56DDfzt5NUzJNMgn5Q6l8ymY5mPIgjU1C9HYAb5qR%2FXlMeS3yDy%2Bt%2Bc3zHc92ZKU6LdvQ7zxO0JcWBTGuHdXiTUvKMgfqtUMiZ%2B275Mc2UU9wN8eckT9VXXUU9xLmAC4PtOtuWe5ACS9EtVmLjmv9vEU8S1TkfxgBEmAloGkHaN1RLjd0L%2B1z%2BQVwVZ3rhwhJM6n4WDnSwpXl77uiwSKqF%2Fc5V7n%2FsJ5FoVe7n4GnxQFdmtVQunP26XGzN6STOgDo8OOF7dp2oVJEauWxSsNCwEaBRAno9JEKX430yfYCXesELVYMrOMIUUYklCnTTLT8osJm9wH3BXDsQKE5Q3mxPUm5UU7uiHr9Dm3W%2FQKZYxSe%2FsCpiEwMPOKmL0GOqUBozFzzJ9b4iJ1L8FpOscRSxIsWnXkgfFdDtIQWNiuq0vvvMbk1xPHuiI%2FqYKF3on5PlkkTT4%2BEf%2Bz4aurv544c1k0hf1mMMhazOqIElwM8Dpsor4tzK4x0VUrjwrxb5o5RFuscYS0tkiLBIN7G3gZGQGWZUB7z%2BymirQfk6qGPVbpNqukHVmKexWFaP5aj6l78QRzhZ00vstFNLulkgynptyaVX%2Ba&X-Amz-Signature=0bf92eabb6768f9c9b2faafd63a7320bde81e7f19a6ae690663812ee48232ca0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OFCHQSX%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132013Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIBcQPqstF%2FSaNCXnDo%2FDPBXJJxxsdZ0kPeDCd%2FTy4apNAiEAu4%2Fto3rA03SvML5fyW%2BJf%2FYdaBrCsjc9fbC5XPOuh%2FIq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDJon%2FfR2sdyuAjb0zSrcA8iXHsR%2FhYXl7WUzYBn594HQGeuI1NHI5lRbdiay%2F74dDZv7%2FP1BBj8T1gFt5bY%2BQFbdArA8XXC90Yq0ChevHnERmViJ7wXa2WSNLCJpmHEnCWgyCOCiQJoZtMFLUYsOYDcIoBqbVNjsDmDC1bmb7iZOk9tmAxRK1kPhYS9m8jkBwoWmPUqFMXw0kXAlCCIY1CmD%2BrmcgIWP18%2Bjx8G3W0C4CC5%2B5He1%2FzLPYrEdg05A7VKpqNjvUHnCtaiYNapv7Re9Y5nG56DDfzt5NUzJNMgn5Q6l8ymY5mPIgjU1C9HYAb5qR%2FXlMeS3yDy%2Bt%2Bc3zHc92ZKU6LdvQ7zxO0JcWBTGuHdXiTUvKMgfqtUMiZ%2B275Mc2UU9wN8eckT9VXXUU9xLmAC4PtOtuWe5ACS9EtVmLjmv9vEU8S1TkfxgBEmAloGkHaN1RLjd0L%2B1z%2BQVwVZ3rhwhJM6n4WDnSwpXl77uiwSKqF%2Fc5V7n%2FsJ5FoVe7n4GnxQFdmtVQunP26XGzN6STOgDo8OOF7dp2oVJEauWxSsNCwEaBRAno9JEKX430yfYCXesELVYMrOMIUUYklCnTTLT8osJm9wH3BXDsQKE5Q3mxPUm5UU7uiHr9Dm3W%2FQKZYxSe%2FsCpiEwMPOKmL0GOqUBozFzzJ9b4iJ1L8FpOscRSxIsWnXkgfFdDtIQWNiuq0vvvMbk1xPHuiI%2FqYKF3on5PlkkTT4%2BEf%2Bz4aurv544c1k0hf1mMMhazOqIElwM8Dpsor4tzK4x0VUrjwrxb5o5RFuscYS0tkiLBIN7G3gZGQGWZUB7z%2BymirQfk6qGPVbpNqukHVmKexWFaP5aj6l78QRzhZ00vstFNLulkgynptyaVX%2Ba&X-Amz-Signature=bc56cdfdc657e401255fc80028978b997333e1c7a79c0384c62874f8ef5a3315&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OFCHQSX%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132013Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIBcQPqstF%2FSaNCXnDo%2FDPBXJJxxsdZ0kPeDCd%2FTy4apNAiEAu4%2Fto3rA03SvML5fyW%2BJf%2FYdaBrCsjc9fbC5XPOuh%2FIq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDJon%2FfR2sdyuAjb0zSrcA8iXHsR%2FhYXl7WUzYBn594HQGeuI1NHI5lRbdiay%2F74dDZv7%2FP1BBj8T1gFt5bY%2BQFbdArA8XXC90Yq0ChevHnERmViJ7wXa2WSNLCJpmHEnCWgyCOCiQJoZtMFLUYsOYDcIoBqbVNjsDmDC1bmb7iZOk9tmAxRK1kPhYS9m8jkBwoWmPUqFMXw0kXAlCCIY1CmD%2BrmcgIWP18%2Bjx8G3W0C4CC5%2B5He1%2FzLPYrEdg05A7VKpqNjvUHnCtaiYNapv7Re9Y5nG56DDfzt5NUzJNMgn5Q6l8ymY5mPIgjU1C9HYAb5qR%2FXlMeS3yDy%2Bt%2Bc3zHc92ZKU6LdvQ7zxO0JcWBTGuHdXiTUvKMgfqtUMiZ%2B275Mc2UU9wN8eckT9VXXUU9xLmAC4PtOtuWe5ACS9EtVmLjmv9vEU8S1TkfxgBEmAloGkHaN1RLjd0L%2B1z%2BQVwVZ3rhwhJM6n4WDnSwpXl77uiwSKqF%2Fc5V7n%2FsJ5FoVe7n4GnxQFdmtVQunP26XGzN6STOgDo8OOF7dp2oVJEauWxSsNCwEaBRAno9JEKX430yfYCXesELVYMrOMIUUYklCnTTLT8osJm9wH3BXDsQKE5Q3mxPUm5UU7uiHr9Dm3W%2FQKZYxSe%2FsCpiEwMPOKmL0GOqUBozFzzJ9b4iJ1L8FpOscRSxIsWnXkgfFdDtIQWNiuq0vvvMbk1xPHuiI%2FqYKF3on5PlkkTT4%2BEf%2Bz4aurv544c1k0hf1mMMhazOqIElwM8Dpsor4tzK4x0VUrjwrxb5o5RFuscYS0tkiLBIN7G3gZGQGWZUB7z%2BymirQfk6qGPVbpNqukHVmKexWFaP5aj6l78QRzhZ00vstFNLulkgynptyaVX%2Ba&X-Amz-Signature=8176c48f6845b197fff8c5368a52de55c91554ce777e45142ba3ddfa287b8445&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OFCHQSX%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132013Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIBcQPqstF%2FSaNCXnDo%2FDPBXJJxxsdZ0kPeDCd%2FTy4apNAiEAu4%2Fto3rA03SvML5fyW%2BJf%2FYdaBrCsjc9fbC5XPOuh%2FIq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDJon%2FfR2sdyuAjb0zSrcA8iXHsR%2FhYXl7WUzYBn594HQGeuI1NHI5lRbdiay%2F74dDZv7%2FP1BBj8T1gFt5bY%2BQFbdArA8XXC90Yq0ChevHnERmViJ7wXa2WSNLCJpmHEnCWgyCOCiQJoZtMFLUYsOYDcIoBqbVNjsDmDC1bmb7iZOk9tmAxRK1kPhYS9m8jkBwoWmPUqFMXw0kXAlCCIY1CmD%2BrmcgIWP18%2Bjx8G3W0C4CC5%2B5He1%2FzLPYrEdg05A7VKpqNjvUHnCtaiYNapv7Re9Y5nG56DDfzt5NUzJNMgn5Q6l8ymY5mPIgjU1C9HYAb5qR%2FXlMeS3yDy%2Bt%2Bc3zHc92ZKU6LdvQ7zxO0JcWBTGuHdXiTUvKMgfqtUMiZ%2B275Mc2UU9wN8eckT9VXXUU9xLmAC4PtOtuWe5ACS9EtVmLjmv9vEU8S1TkfxgBEmAloGkHaN1RLjd0L%2B1z%2BQVwVZ3rhwhJM6n4WDnSwpXl77uiwSKqF%2Fc5V7n%2FsJ5FoVe7n4GnxQFdmtVQunP26XGzN6STOgDo8OOF7dp2oVJEauWxSsNCwEaBRAno9JEKX430yfYCXesELVYMrOMIUUYklCnTTLT8osJm9wH3BXDsQKE5Q3mxPUm5UU7uiHr9Dm3W%2FQKZYxSe%2FsCpiEwMPOKmL0GOqUBozFzzJ9b4iJ1L8FpOscRSxIsWnXkgfFdDtIQWNiuq0vvvMbk1xPHuiI%2FqYKF3on5PlkkTT4%2BEf%2Bz4aurv544c1k0hf1mMMhazOqIElwM8Dpsor4tzK4x0VUrjwrxb5o5RFuscYS0tkiLBIN7G3gZGQGWZUB7z%2BymirQfk6qGPVbpNqukHVmKexWFaP5aj6l78QRzhZ00vstFNLulkgynptyaVX%2Ba&X-Amz-Signature=710aecc860bd52d58748497660181790f810d95b62368a8d17c1210741708a48&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
