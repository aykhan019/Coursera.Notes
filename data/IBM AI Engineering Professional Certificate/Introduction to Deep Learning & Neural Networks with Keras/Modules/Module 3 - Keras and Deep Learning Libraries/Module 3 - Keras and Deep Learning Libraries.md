

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBZBUEDK%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJGMEQCIB%2BJlUxyISliaEyvD6E%2BMVvgsyQD0KlR5BCqmyOZI289AiB68k2Lg9nTxE9E8AS3Nw2FGhKquOIcDok1TqWNNCO%2BDSr%2FAwhWEAAaDDYzNzQyMzE4MzgwNSIMl7YbO9mYt4MbjdJsKtwDs0Iu6%2BrPL51zceNiTKGqvCbLPWBXWBAlIH6WCSa3PpxFUf9vEsDnmrst7mSNVZzKdg0jYB%2BYBv8aOwr0p5MjPwI6vn8FB8R4IkzCW4cXHNFKn5GOO7RIA52Uyym7JGPM1pbqe5ivG5MllsyTDCpud9D9wg8toXRtpcO6deMWCAQFFIQVtMRt372Z5OD7PKIsS8Wb%2BFToPPnkyimu0FYfvqVlXb7qwlG9SFJ5VPQJ84SjRt7ha7oHzthrK6N6yjSeMeJoTQWvcASwJb4ykw6QximhoBsp7pg%2FDQTNOyFGqsp4hk3yuTF5SgnmDkM1hRaQJamR%2FU0tuTcYMALXWZ%2FzoQIgV2fBp3Xw5A3bv0ssK6%2FNDlJsL%2Fkg3c54%2FubqMjTVzIaQEdrVxOYSfy2q11kdTpU2pEHj06BwSnRqoFrH041znjaALIfhof%2By3XOIw%2B4h4WfFF6lyiiQu0n2P46%2FflSLK%2BiPyAMLeD%2BKHENZprK8heUJy7WlPYfApD9QM4VaQflxFaNK9xBynZwPtxV30tNoLkTbU3ws%2FEGydeGeEBcuImb%2BnYFDCGGawOvcsd4gU47blq%2FQ6FliyQquppLv7EkYZxLf6K7BGCOCfjb%2BEoN2XsimXiwSFw3R%2FkyAwsvyQvQY6pgEVr5D0UL2gPiMuJzhsRBPCv7H%2FbocRhl8JH2NHBYEqRLMDJTFVWc96lwvW6WJLY8R19JUPWQvHH7F8JFVpGQkFrG%2BPwbUT%2BBtdc9eGxBv1zZXgRorfiCkXJd0kz8WdIlgb%2BxX7LOZld24HXEqbvlKywGCTGJwsRuRm397Wx%2F9nScHfdjddl9fQpaD01BEvop4AZsx7baVR3wYfzHcHMvlgm1qdBJhg&X-Amz-Signature=e0b3d86749e328d91e37f1fcfeb9d434e1aae6d996cf678daeb13d034a294761&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBZBUEDK%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJGMEQCIB%2BJlUxyISliaEyvD6E%2BMVvgsyQD0KlR5BCqmyOZI289AiB68k2Lg9nTxE9E8AS3Nw2FGhKquOIcDok1TqWNNCO%2BDSr%2FAwhWEAAaDDYzNzQyMzE4MzgwNSIMl7YbO9mYt4MbjdJsKtwDs0Iu6%2BrPL51zceNiTKGqvCbLPWBXWBAlIH6WCSa3PpxFUf9vEsDnmrst7mSNVZzKdg0jYB%2BYBv8aOwr0p5MjPwI6vn8FB8R4IkzCW4cXHNFKn5GOO7RIA52Uyym7JGPM1pbqe5ivG5MllsyTDCpud9D9wg8toXRtpcO6deMWCAQFFIQVtMRt372Z5OD7PKIsS8Wb%2BFToPPnkyimu0FYfvqVlXb7qwlG9SFJ5VPQJ84SjRt7ha7oHzthrK6N6yjSeMeJoTQWvcASwJb4ykw6QximhoBsp7pg%2FDQTNOyFGqsp4hk3yuTF5SgnmDkM1hRaQJamR%2FU0tuTcYMALXWZ%2FzoQIgV2fBp3Xw5A3bv0ssK6%2FNDlJsL%2Fkg3c54%2FubqMjTVzIaQEdrVxOYSfy2q11kdTpU2pEHj06BwSnRqoFrH041znjaALIfhof%2By3XOIw%2B4h4WfFF6lyiiQu0n2P46%2FflSLK%2BiPyAMLeD%2BKHENZprK8heUJy7WlPYfApD9QM4VaQflxFaNK9xBynZwPtxV30tNoLkTbU3ws%2FEGydeGeEBcuImb%2BnYFDCGGawOvcsd4gU47blq%2FQ6FliyQquppLv7EkYZxLf6K7BGCOCfjb%2BEoN2XsimXiwSFw3R%2FkyAwsvyQvQY6pgEVr5D0UL2gPiMuJzhsRBPCv7H%2FbocRhl8JH2NHBYEqRLMDJTFVWc96lwvW6WJLY8R19JUPWQvHH7F8JFVpGQkFrG%2BPwbUT%2BBtdc9eGxBv1zZXgRorfiCkXJd0kz8WdIlgb%2BxX7LOZld24HXEqbvlKywGCTGJwsRuRm397Wx%2F9nScHfdjddl9fQpaD01BEvop4AZsx7baVR3wYfzHcHMvlgm1qdBJhg&X-Amz-Signature=5277246c0a71e0d7949bccf615398f9c5f0e24dde272b3458c4b52c31f569977&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBZBUEDK%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJGMEQCIB%2BJlUxyISliaEyvD6E%2BMVvgsyQD0KlR5BCqmyOZI289AiB68k2Lg9nTxE9E8AS3Nw2FGhKquOIcDok1TqWNNCO%2BDSr%2FAwhWEAAaDDYzNzQyMzE4MzgwNSIMl7YbO9mYt4MbjdJsKtwDs0Iu6%2BrPL51zceNiTKGqvCbLPWBXWBAlIH6WCSa3PpxFUf9vEsDnmrst7mSNVZzKdg0jYB%2BYBv8aOwr0p5MjPwI6vn8FB8R4IkzCW4cXHNFKn5GOO7RIA52Uyym7JGPM1pbqe5ivG5MllsyTDCpud9D9wg8toXRtpcO6deMWCAQFFIQVtMRt372Z5OD7PKIsS8Wb%2BFToPPnkyimu0FYfvqVlXb7qwlG9SFJ5VPQJ84SjRt7ha7oHzthrK6N6yjSeMeJoTQWvcASwJb4ykw6QximhoBsp7pg%2FDQTNOyFGqsp4hk3yuTF5SgnmDkM1hRaQJamR%2FU0tuTcYMALXWZ%2FzoQIgV2fBp3Xw5A3bv0ssK6%2FNDlJsL%2Fkg3c54%2FubqMjTVzIaQEdrVxOYSfy2q11kdTpU2pEHj06BwSnRqoFrH041znjaALIfhof%2By3XOIw%2B4h4WfFF6lyiiQu0n2P46%2FflSLK%2BiPyAMLeD%2BKHENZprK8heUJy7WlPYfApD9QM4VaQflxFaNK9xBynZwPtxV30tNoLkTbU3ws%2FEGydeGeEBcuImb%2BnYFDCGGawOvcsd4gU47blq%2FQ6FliyQquppLv7EkYZxLf6K7BGCOCfjb%2BEoN2XsimXiwSFw3R%2FkyAwsvyQvQY6pgEVr5D0UL2gPiMuJzhsRBPCv7H%2FbocRhl8JH2NHBYEqRLMDJTFVWc96lwvW6WJLY8R19JUPWQvHH7F8JFVpGQkFrG%2BPwbUT%2BBtdc9eGxBv1zZXgRorfiCkXJd0kz8WdIlgb%2BxX7LOZld24HXEqbvlKywGCTGJwsRuRm397Wx%2F9nScHfdjddl9fQpaD01BEvop4AZsx7baVR3wYfzHcHMvlgm1qdBJhg&X-Amz-Signature=bc5fa742716868a3c796528cefbf56e6464df6f6a5c7e896dfdf4c057ec0561f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466STNQV4EO%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJHMEUCICaEOuaFeN0yHxIC5Pr9%2FERbnCaem89onrhtEh6Mw5TXAiEA2um1lbSVgmAN5UQ5XKu7abIlBINgcukTLaTT%2F6nxitQq%2FwMIVhAAGgw2Mzc0MjMxODM4MDUiDIsvzEsX3D%2BWTCK92yrcA3p8iaeaSgyiRwbDnE16taeXVS4dxjfrD85LjpWdV%2FiB6b1S6RxQQyMH5nFmOgcahkVo9dZd2Og30ZgR7OY%2BOlPwyojm3CGhoBAPGPFc0kizph%2FtzBMsKeD1jxtv8DV0iQruCLx3FgCaTs6ZFpCOAf6ApM2KLLFJ8wHV6hXeTbIG6d4h64EoUKGmsz7a9WX2EfhTV%2BDnaMRYu0X%2BsRl%2F8xVuHcOjRKsSdTEt2aioFmGwMvBrynXIldZeif0XSiv%2FUU8Us%2BV%2BgjYXFABB6N2tnVrWoqzh9brL4RTGOC2MFDxeC2sqM1jg9sqDnfoDUtCBk2sUufBmcaZzYIHLAleYm8e5pBQhIOhDN5BseWDQFQ9eOMe5%2FAufg%2BkyJHL9Inb9U9wSAgPw9bATzro2A%2FabTEiA34mdmkro0UfOMJykAflKZUROfVQmV0OXbuyHt3g1qwIDTANgBSgoI3QamK%2BjiUuzXjS5HHG1S0F9InG%2BVPoHnApaQO6RAHaFBs8zeycdtQGwKfaoihpHTVjyJHKUl2jzYE%2BtqI9kyAhm%2Bp7YzRY70eRWwc1%2F6Hy8wnCr%2BKht2%2ByZvfXL0k2ZFSnWQAGOEORtES8kA4jeGcNl43PrveoPzdGrwSZw%2FcatW4GBMPj7kL0GOqUB2FnOi9fT1TvRig%2B%2FXIcVs1NlTD5GNgeLwYdZcg8WufRz31BFnoVsLyhigEsCoa2%2FLs76mOeJ%2BOVaWCTwwhoqmiKjJ7hRJHOIvY0klUEyFgCjEWsdsZfGmITBeRYxrK7EHok6AVgEgPYayo3%2FsijC6isQOrV1leQnIdNSo73VEi47U9wrt395EM1dde7ooIru15Y6fkRrANLUbOb1ofNbMkCAn85K&X-Amz-Signature=dd7e049489c0db779b70b5e80366405dbb7168b705a89c67f4e7d00b996ebc00&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XKTHZQIA%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJIMEYCIQCkwuIEyNZ0gZeTTkD6SzlVAePJUSqKhZWCxBfeQjFFWAIhAMNIAG4wYDTFt6H1C%2FUIYdnLoNCV0mFurZgb0vaPif6ZKv8DCFYQABoMNjM3NDIzMTgzODA1IgzlF4H55pn3qdywL7Eq3APb5P0DMpEWVF%2F%2BI5CUUQm9W5oNIP0%2FEqr%2FyPvNdGGQ0Nwjt3B85bDvRD8z4HRViTX707iXUf7bkuM%2FHdT7j3gkv6h0LgRrwbWmB%2FaJXdMAXi%2FCNI5LQiXdPMkc41XK1pMH5jcVMmIicfnr7EmMNqm6kcAzy39LoRuy%2BzeF5vP%2BDnN1k1mu2z9B%2BrTsd4Up%2F%2BhIbQzx9S4gcNsRspGG%2BVR5GEAXQJ5P11O63Z2DyXm0w5T72kMD%2F4DLtyb9rdvEWf9GquDWkQS4kaVMw3iYsxTrbldJqS%2BPf8vw80OnvZ02GnGgbF4acO1rwQOwypzwXr9WortcZaPUEotv4biKFyOwaZdAEBs09DpKEH%2FHgLkPr0Ksc9vcLXUJCZOzbwmFHhY5AaPL%2F%2FOQU%2BjMX2q8MX543dnOWvAlQKLsBNKBRESd2F9vn%2FWrFj4W4V6Fju1JKUl3DyL%2F9v5OmOebhK9v4ZcszLnjXvGDfy48gPGlJjxmpys4D1JuUj9ZWillhKr4qmigQLngxQ2rzRUuws4aGNZ7eEUfI5G%2BgJ8KezeOErVYT7mZIewn49W4CqzcJO3p7tYHnawZZdtXE8gfNFhU0b%2BBYc1FZXFN87ulyLg7FXE%2B46DQDxA6uDuG%2BK3wODCf%2FJC9BjqkAdZR4jNDgKd0mkzqU01Z64LBpG1TLxlrVIq1EXpt6iQJZ%2BzYgQHq9%2Fp3Lbh9gXpErSW3yDnknfxoTuVW%2F9Jd4r8buvdF5LD8zM2GDt59%2F%2BnAe8luVoxeeCQb85sjjbkSEOrTRhBVywXMLK3H178B4wPTCdt2XNqT4IEbF6QGIelyrM4cDo4aCquMAjgbaV11Ym3lxV35EuLY3g7eyCLsimRpUCDD&X-Amz-Signature=788f260557d3ce48db9c3cc109ede848bb546b4996932dcfb5ea346834f53609&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBZBUEDK%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJGMEQCIB%2BJlUxyISliaEyvD6E%2BMVvgsyQD0KlR5BCqmyOZI289AiB68k2Lg9nTxE9E8AS3Nw2FGhKquOIcDok1TqWNNCO%2BDSr%2FAwhWEAAaDDYzNzQyMzE4MzgwNSIMl7YbO9mYt4MbjdJsKtwDs0Iu6%2BrPL51zceNiTKGqvCbLPWBXWBAlIH6WCSa3PpxFUf9vEsDnmrst7mSNVZzKdg0jYB%2BYBv8aOwr0p5MjPwI6vn8FB8R4IkzCW4cXHNFKn5GOO7RIA52Uyym7JGPM1pbqe5ivG5MllsyTDCpud9D9wg8toXRtpcO6deMWCAQFFIQVtMRt372Z5OD7PKIsS8Wb%2BFToPPnkyimu0FYfvqVlXb7qwlG9SFJ5VPQJ84SjRt7ha7oHzthrK6N6yjSeMeJoTQWvcASwJb4ykw6QximhoBsp7pg%2FDQTNOyFGqsp4hk3yuTF5SgnmDkM1hRaQJamR%2FU0tuTcYMALXWZ%2FzoQIgV2fBp3Xw5A3bv0ssK6%2FNDlJsL%2Fkg3c54%2FubqMjTVzIaQEdrVxOYSfy2q11kdTpU2pEHj06BwSnRqoFrH041znjaALIfhof%2By3XOIw%2B4h4WfFF6lyiiQu0n2P46%2FflSLK%2BiPyAMLeD%2BKHENZprK8heUJy7WlPYfApD9QM4VaQflxFaNK9xBynZwPtxV30tNoLkTbU3ws%2FEGydeGeEBcuImb%2BnYFDCGGawOvcsd4gU47blq%2FQ6FliyQquppLv7EkYZxLf6K7BGCOCfjb%2BEoN2XsimXiwSFw3R%2FkyAwsvyQvQY6pgEVr5D0UL2gPiMuJzhsRBPCv7H%2FbocRhl8JH2NHBYEqRLMDJTFVWc96lwvW6WJLY8R19JUPWQvHH7F8JFVpGQkFrG%2BPwbUT%2BBtdc9eGxBv1zZXgRorfiCkXJd0kz8WdIlgb%2BxX7LOZld24HXEqbvlKywGCTGJwsRuRm397Wx%2F9nScHfdjddl9fQpaD01BEvop4AZsx7baVR3wYfzHcHMvlgm1qdBJhg&X-Amz-Signature=5152947c7a7fac7c5e36cab7b3aea07067510f18124fe825658a1d3a4fdfadf7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBZBUEDK%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJGMEQCIB%2BJlUxyISliaEyvD6E%2BMVvgsyQD0KlR5BCqmyOZI289AiB68k2Lg9nTxE9E8AS3Nw2FGhKquOIcDok1TqWNNCO%2BDSr%2FAwhWEAAaDDYzNzQyMzE4MzgwNSIMl7YbO9mYt4MbjdJsKtwDs0Iu6%2BrPL51zceNiTKGqvCbLPWBXWBAlIH6WCSa3PpxFUf9vEsDnmrst7mSNVZzKdg0jYB%2BYBv8aOwr0p5MjPwI6vn8FB8R4IkzCW4cXHNFKn5GOO7RIA52Uyym7JGPM1pbqe5ivG5MllsyTDCpud9D9wg8toXRtpcO6deMWCAQFFIQVtMRt372Z5OD7PKIsS8Wb%2BFToPPnkyimu0FYfvqVlXb7qwlG9SFJ5VPQJ84SjRt7ha7oHzthrK6N6yjSeMeJoTQWvcASwJb4ykw6QximhoBsp7pg%2FDQTNOyFGqsp4hk3yuTF5SgnmDkM1hRaQJamR%2FU0tuTcYMALXWZ%2FzoQIgV2fBp3Xw5A3bv0ssK6%2FNDlJsL%2Fkg3c54%2FubqMjTVzIaQEdrVxOYSfy2q11kdTpU2pEHj06BwSnRqoFrH041znjaALIfhof%2By3XOIw%2B4h4WfFF6lyiiQu0n2P46%2FflSLK%2BiPyAMLeD%2BKHENZprK8heUJy7WlPYfApD9QM4VaQflxFaNK9xBynZwPtxV30tNoLkTbU3ws%2FEGydeGeEBcuImb%2BnYFDCGGawOvcsd4gU47blq%2FQ6FliyQquppLv7EkYZxLf6K7BGCOCfjb%2BEoN2XsimXiwSFw3R%2FkyAwsvyQvQY6pgEVr5D0UL2gPiMuJzhsRBPCv7H%2FbocRhl8JH2NHBYEqRLMDJTFVWc96lwvW6WJLY8R19JUPWQvHH7F8JFVpGQkFrG%2BPwbUT%2BBtdc9eGxBv1zZXgRorfiCkXJd0kz8WdIlgb%2BxX7LOZld24HXEqbvlKywGCTGJwsRuRm397Wx%2F9nScHfdjddl9fQpaD01BEvop4AZsx7baVR3wYfzHcHMvlgm1qdBJhg&X-Amz-Signature=6f4936aabc3022352e25d553b7f24da5cac9ba24866ad5d960b5d7e6f0e5884b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBZBUEDK%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJGMEQCIB%2BJlUxyISliaEyvD6E%2BMVvgsyQD0KlR5BCqmyOZI289AiB68k2Lg9nTxE9E8AS3Nw2FGhKquOIcDok1TqWNNCO%2BDSr%2FAwhWEAAaDDYzNzQyMzE4MzgwNSIMl7YbO9mYt4MbjdJsKtwDs0Iu6%2BrPL51zceNiTKGqvCbLPWBXWBAlIH6WCSa3PpxFUf9vEsDnmrst7mSNVZzKdg0jYB%2BYBv8aOwr0p5MjPwI6vn8FB8R4IkzCW4cXHNFKn5GOO7RIA52Uyym7JGPM1pbqe5ivG5MllsyTDCpud9D9wg8toXRtpcO6deMWCAQFFIQVtMRt372Z5OD7PKIsS8Wb%2BFToPPnkyimu0FYfvqVlXb7qwlG9SFJ5VPQJ84SjRt7ha7oHzthrK6N6yjSeMeJoTQWvcASwJb4ykw6QximhoBsp7pg%2FDQTNOyFGqsp4hk3yuTF5SgnmDkM1hRaQJamR%2FU0tuTcYMALXWZ%2FzoQIgV2fBp3Xw5A3bv0ssK6%2FNDlJsL%2Fkg3c54%2FubqMjTVzIaQEdrVxOYSfy2q11kdTpU2pEHj06BwSnRqoFrH041znjaALIfhof%2By3XOIw%2B4h4WfFF6lyiiQu0n2P46%2FflSLK%2BiPyAMLeD%2BKHENZprK8heUJy7WlPYfApD9QM4VaQflxFaNK9xBynZwPtxV30tNoLkTbU3ws%2FEGydeGeEBcuImb%2BnYFDCGGawOvcsd4gU47blq%2FQ6FliyQquppLv7EkYZxLf6K7BGCOCfjb%2BEoN2XsimXiwSFw3R%2FkyAwsvyQvQY6pgEVr5D0UL2gPiMuJzhsRBPCv7H%2FbocRhl8JH2NHBYEqRLMDJTFVWc96lwvW6WJLY8R19JUPWQvHH7F8JFVpGQkFrG%2BPwbUT%2BBtdc9eGxBv1zZXgRorfiCkXJd0kz8WdIlgb%2BxX7LOZld24HXEqbvlKywGCTGJwsRuRm397Wx%2F9nScHfdjddl9fQpaD01BEvop4AZsx7baVR3wYfzHcHMvlgm1qdBJhg&X-Amz-Signature=0e769ffc3feb5c42353b3255f81ed28327d4861957a9ab1e227f770d82b61e47&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBZBUEDK%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJGMEQCIB%2BJlUxyISliaEyvD6E%2BMVvgsyQD0KlR5BCqmyOZI289AiB68k2Lg9nTxE9E8AS3Nw2FGhKquOIcDok1TqWNNCO%2BDSr%2FAwhWEAAaDDYzNzQyMzE4MzgwNSIMl7YbO9mYt4MbjdJsKtwDs0Iu6%2BrPL51zceNiTKGqvCbLPWBXWBAlIH6WCSa3PpxFUf9vEsDnmrst7mSNVZzKdg0jYB%2BYBv8aOwr0p5MjPwI6vn8FB8R4IkzCW4cXHNFKn5GOO7RIA52Uyym7JGPM1pbqe5ivG5MllsyTDCpud9D9wg8toXRtpcO6deMWCAQFFIQVtMRt372Z5OD7PKIsS8Wb%2BFToPPnkyimu0FYfvqVlXb7qwlG9SFJ5VPQJ84SjRt7ha7oHzthrK6N6yjSeMeJoTQWvcASwJb4ykw6QximhoBsp7pg%2FDQTNOyFGqsp4hk3yuTF5SgnmDkM1hRaQJamR%2FU0tuTcYMALXWZ%2FzoQIgV2fBp3Xw5A3bv0ssK6%2FNDlJsL%2Fkg3c54%2FubqMjTVzIaQEdrVxOYSfy2q11kdTpU2pEHj06BwSnRqoFrH041znjaALIfhof%2By3XOIw%2B4h4WfFF6lyiiQu0n2P46%2FflSLK%2BiPyAMLeD%2BKHENZprK8heUJy7WlPYfApD9QM4VaQflxFaNK9xBynZwPtxV30tNoLkTbU3ws%2FEGydeGeEBcuImb%2BnYFDCGGawOvcsd4gU47blq%2FQ6FliyQquppLv7EkYZxLf6K7BGCOCfjb%2BEoN2XsimXiwSFw3R%2FkyAwsvyQvQY6pgEVr5D0UL2gPiMuJzhsRBPCv7H%2FbocRhl8JH2NHBYEqRLMDJTFVWc96lwvW6WJLY8R19JUPWQvHH7F8JFVpGQkFrG%2BPwbUT%2BBtdc9eGxBv1zZXgRorfiCkXJd0kz8WdIlgb%2BxX7LOZld24HXEqbvlKywGCTGJwsRuRm397Wx%2F9nScHfdjddl9fQpaD01BEvop4AZsx7baVR3wYfzHcHMvlgm1qdBJhg&X-Amz-Signature=6105cea72d0b6b89b9080d5c1b215a1e53681cab302a3a577fdcd6d328eae661&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
