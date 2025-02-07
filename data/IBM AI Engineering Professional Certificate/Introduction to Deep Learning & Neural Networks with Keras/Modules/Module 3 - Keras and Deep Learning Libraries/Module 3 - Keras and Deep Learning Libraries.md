

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJVUWCGT%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQDyILmfJFIyQg2WRPJOou22IKsShiXv7r2TspgbDfLsawIhAOP8xuxvZqORXnasWdQJCA0gs9x7oO4gHxVUDr94HX24Kv8DCHoQABoMNjM3NDIzMTgzODA1IgyObhAvbFG4vtMwkBoq3AMAootnJ5ipN16HKqxCWYIJLTImI05pNa%2BUKijJk2dM5ACwxOixjZQtBbYJRr5S243MrN5e5D%2FqAPO%2BLJvXAq0wEiXZTKR2d60WY4Jge2pJhamndmfrcR8unodG99fS23Zt5NcZzZXhytopJJ69eHRCglOMYYFQv10URAJwp5pNW4pkFOZJXgWZtS5ERTMJCWF8%2FwLjUv4lER2IlizUhQBl%2BeKgLKK%2BrMP0YqOzPNwSKk2AX9LCZjAEMOUGl4TYW6EzX4b531dfNXLMbxkSqMtZOJgO6o4KqOkQAwAb24HiLe1gsXtSeL6ERW27kzTURFiklDL%2FROJ%2BFXcER4opZdpKWeX4Xnc%2Fo5Xx%2FdOvBz%2BeXFd99IQ8sH%2FfMCluswoBu74rSys3U0fCfyKGKvNX7dERLvG8HBdDHjU4HWftHmeahRQsbZQuPeaOaY5fwAB45a5glSqO9Zpyx%2BwcdHZoLkTEKiDENwLwe%2FTPGHTrpZXruc5aUARyMWVl3Pxv3YenoxIiqkMOzEHrA4FGNluF2oDQt3RfZfcVPkr8yvm9AZ1RHlWSofkmRSkPKrhG58nT8CQx4onE8Rny0eywsDDyT2uxL0KpbY%2FNcvD2%2FlxzBjjQfKEwkmGOlfXJYnGHRDDH%2B5i9BjqkAUH%2F3htZp%2Fpz3BV6rQlAfs5xK9NHzwmVL4bYsB7amvnn%2BdtOYRFb%2BUVSh1UCEL1VIjyWwqdWvSIrp3ZCbY9eVfzJh6kAvQ5tFnrU8suk0Uploa2mWIOqCA%2FCieTqQ1rcF%2F2zFri5zmqgMAIJOMyU6rJGJOEZ6E2trEBHVZN0ebiEzv0PZSx7T0XO65VTPwcDW01PriNPbzjbqT1Xex0oEroPn2hh&X-Amz-Signature=805a5443e5b842d0cee448930f8fdbf298c60d9cb97a3b6b4e436697031c3125&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJVUWCGT%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQDyILmfJFIyQg2WRPJOou22IKsShiXv7r2TspgbDfLsawIhAOP8xuxvZqORXnasWdQJCA0gs9x7oO4gHxVUDr94HX24Kv8DCHoQABoMNjM3NDIzMTgzODA1IgyObhAvbFG4vtMwkBoq3AMAootnJ5ipN16HKqxCWYIJLTImI05pNa%2BUKijJk2dM5ACwxOixjZQtBbYJRr5S243MrN5e5D%2FqAPO%2BLJvXAq0wEiXZTKR2d60WY4Jge2pJhamndmfrcR8unodG99fS23Zt5NcZzZXhytopJJ69eHRCglOMYYFQv10URAJwp5pNW4pkFOZJXgWZtS5ERTMJCWF8%2FwLjUv4lER2IlizUhQBl%2BeKgLKK%2BrMP0YqOzPNwSKk2AX9LCZjAEMOUGl4TYW6EzX4b531dfNXLMbxkSqMtZOJgO6o4KqOkQAwAb24HiLe1gsXtSeL6ERW27kzTURFiklDL%2FROJ%2BFXcER4opZdpKWeX4Xnc%2Fo5Xx%2FdOvBz%2BeXFd99IQ8sH%2FfMCluswoBu74rSys3U0fCfyKGKvNX7dERLvG8HBdDHjU4HWftHmeahRQsbZQuPeaOaY5fwAB45a5glSqO9Zpyx%2BwcdHZoLkTEKiDENwLwe%2FTPGHTrpZXruc5aUARyMWVl3Pxv3YenoxIiqkMOzEHrA4FGNluF2oDQt3RfZfcVPkr8yvm9AZ1RHlWSofkmRSkPKrhG58nT8CQx4onE8Rny0eywsDDyT2uxL0KpbY%2FNcvD2%2FlxzBjjQfKEwkmGOlfXJYnGHRDDH%2B5i9BjqkAUH%2F3htZp%2Fpz3BV6rQlAfs5xK9NHzwmVL4bYsB7amvnn%2BdtOYRFb%2BUVSh1UCEL1VIjyWwqdWvSIrp3ZCbY9eVfzJh6kAvQ5tFnrU8suk0Uploa2mWIOqCA%2FCieTqQ1rcF%2F2zFri5zmqgMAIJOMyU6rJGJOEZ6E2trEBHVZN0ebiEzv0PZSx7T0XO65VTPwcDW01PriNPbzjbqT1Xex0oEroPn2hh&X-Amz-Signature=b8abc3a23a8b01e03d99908f5fa9e85b5e07fa254c8477cdd37d3c33fde43fbe&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJVUWCGT%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQDyILmfJFIyQg2WRPJOou22IKsShiXv7r2TspgbDfLsawIhAOP8xuxvZqORXnasWdQJCA0gs9x7oO4gHxVUDr94HX24Kv8DCHoQABoMNjM3NDIzMTgzODA1IgyObhAvbFG4vtMwkBoq3AMAootnJ5ipN16HKqxCWYIJLTImI05pNa%2BUKijJk2dM5ACwxOixjZQtBbYJRr5S243MrN5e5D%2FqAPO%2BLJvXAq0wEiXZTKR2d60WY4Jge2pJhamndmfrcR8unodG99fS23Zt5NcZzZXhytopJJ69eHRCglOMYYFQv10URAJwp5pNW4pkFOZJXgWZtS5ERTMJCWF8%2FwLjUv4lER2IlizUhQBl%2BeKgLKK%2BrMP0YqOzPNwSKk2AX9LCZjAEMOUGl4TYW6EzX4b531dfNXLMbxkSqMtZOJgO6o4KqOkQAwAb24HiLe1gsXtSeL6ERW27kzTURFiklDL%2FROJ%2BFXcER4opZdpKWeX4Xnc%2Fo5Xx%2FdOvBz%2BeXFd99IQ8sH%2FfMCluswoBu74rSys3U0fCfyKGKvNX7dERLvG8HBdDHjU4HWftHmeahRQsbZQuPeaOaY5fwAB45a5glSqO9Zpyx%2BwcdHZoLkTEKiDENwLwe%2FTPGHTrpZXruc5aUARyMWVl3Pxv3YenoxIiqkMOzEHrA4FGNluF2oDQt3RfZfcVPkr8yvm9AZ1RHlWSofkmRSkPKrhG58nT8CQx4onE8Rny0eywsDDyT2uxL0KpbY%2FNcvD2%2FlxzBjjQfKEwkmGOlfXJYnGHRDDH%2B5i9BjqkAUH%2F3htZp%2Fpz3BV6rQlAfs5xK9NHzwmVL4bYsB7amvnn%2BdtOYRFb%2BUVSh1UCEL1VIjyWwqdWvSIrp3ZCbY9eVfzJh6kAvQ5tFnrU8suk0Uploa2mWIOqCA%2FCieTqQ1rcF%2F2zFri5zmqgMAIJOMyU6rJGJOEZ6E2trEBHVZN0ebiEzv0PZSx7T0XO65VTPwcDW01PriNPbzjbqT1Xex0oEroPn2hh&X-Amz-Signature=4aad1976177b297742f94453db169f5f4ff8e44e8ce04713f13c2f0fe07cf256&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TRQGU3ZO%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIHUTKIUJ%2BjqbwZuiN3ij6%2Bcph8k2v%2B7Vz5MV9VDyp7YfAiEAr92gk3nX%2FgaxHtwXWk2Ye1Ew8FO4FuTea%2Bv%2FG8D02y4q%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDFdnU4Dp7SzUs6%2F6fyrcAwTlfNwbLOvGfZuiJAAiRQZQa4x4ZM9GwFJbETa2oaGAxTLRv5iYTNyjcyjrILfg1h%2Foral%2BaoX8k%2Fr0SbP1WRtIAGMqFO29hOf0%2FuUDLyTFYChGCRQc9tzRnr%2Fpjuyoih2bFisVniHhTYQqA1g2riWYtBOERwsIwYywUzxNQINdfKL9Kp7YyoKArQ4APeWtfHQqPJMdmhmWOL94dn9rbiIuXrE5FlBvcrApShqxsdbTnJlGrxVBb9Ds975APX7zexU3FdgXsohMKw7%2FeOzw%2BWVW%2BFoirUOddz51EPw2wwabmlTia%2FTkrTnY91FirMqJWsn0BYWRWrMqkDZa1wEaxQY5Dl68oXfqZCvZgjn6hxW6p%2F9b%2Ft1shTFtikCYZtacl%2B7WkeCv0uUFO424YBBzbEtMH4ABoHma9Lqlah0o%2B6cwaoSLMxDgeWOCHN%2FoneSCLduuXlyvF2ZmiKSHoTuEJpmj1LmILLuwWrIgY4o7MUS9EsKQdj2I7VTnVYV3IHJVbdIyywTZOEp3m7nAhlCMJV%2FlclwLnEl0kS5BdgKM3c4vvKe7LawRPQevocryGnbmZ8leO8rMUXN8PidfnhuE4Y%2F3aomQRBHT82tO1IMdQuZwFx4AmTZ67uiHOOyqMMb7mL0GOqUBvuytMnMOECatxEAEzAV5VdZd1fiSXpPZm%2BriuH088oGS2ZZRGfGwuPE2O90H5qE5RrZibricI2AiQN4ZGGXQqjFxivD2Dce63Cnxg2D2jyrzU5yWFxq0xvhT%2FfwKxXKdTDj83FittmldCmnjho%2F9cKi2H9OapZ4Z6BTcxFG1fsige8AQRHGbN10nrJDatlhQ%2FW3PIwpZP%2BMkIOdsVsqTg1e6ljLF&X-Amz-Signature=cf4ff5662a691c13aa243681071759915458205cbe169f5de1d6f9213720f019&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZT3ZN466%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQCUwYB0SrOzfou60AdTEwb7zBSXXzSaG4YYOEBrVr4mRgIhAOdjRNR4ZCPiYSQzkA6Ytyoj9ruA8kiyGjyLVSV%2FVs7IKv8DCHoQABoMNjM3NDIzMTgzODA1IgyRITMEYPtr5FkLKqIq3AM4WxdTSy9T8E7%2FyN8ovn2jxSGXCPrc0a2iMt8GNKf48%2BrE0HKcunCuO2dvZaWUjLXx9CTV6EIV%2FVUbFBSj99eyqRvoX6T6CX8ZJ6xokeCjhAdm%2FxYqc8QQ%2B5XbzpqMFBy3hZyfbzJgKnBvjsS1QbAJbuEhKMXrlEujtov3SdBKjll1I760J8TUgWUfON885vjyJfYXWn%2BaJR5Tq%2F7L84%2FChP9grHuQ3F5AVcqRA0okdWJLchwPpEQLR4o8kVsBGcI7mi75TOOQtaxNqFAqhwZH%2FBuGG3JuxWeD0LzSzXjBaQ9JIIGlwwAZAq2T8Ni%2Fs5tvHNWZlBSQdXzcXn5iQNC0hIgiuSmcPHaOhij0vL44%2Bc%2FV4IJ8VuF0JfXMTfG39KDE2AqsHBNJPvHZQlYxXqIqmNCJNsD7beQvUh7negXV5d6STBKXk30Vx%2FWfUkYYUb7Ue66ZLrHV4EuQru42H2Ch4AzM1NMzEwOTWuJK7Kz1kaz%2FvfX3lH2%2BQH9pP7Durwn0qzpZ%2FiPcOM%2BU%2B6VCMVQt1ebvGh%2B19yVW6XHvHkKKdCKzCJm3hrUazAJy5SIi%2Fjgf29kbGg7UqPUTKvBhlJnTxsVmpN4JD3sTvaFaL%2F07XcxdAs5aiM4jeM6HdjC2%2FJi9BjqkAci6zT7ibL%2F8Z3O%2BFzMSBAUibjy7yu1mzJL344l0NDACRLFaSW7PA7IARqsvONxq98g22h3WbGVabWBABdVW8JiFUJW3n7d8VrrAyVweA2qcL%2Fb1yodlf2ASg8javJUAr9la3%2B8zN1s08EvFJ2%2BTBV2Iafifh9pOCQw6kjGio1jpy6ofR%2BbEYPaFieU7JvcHs7AgBb506u5HCXX3P0%2Fh4euhw1ZC&X-Amz-Signature=6ef2a00dee3fb1f34b40b8b7be66e325f0f9bcc762bd2bf5f2f6a5974a0e29b8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJVUWCGT%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQDyILmfJFIyQg2WRPJOou22IKsShiXv7r2TspgbDfLsawIhAOP8xuxvZqORXnasWdQJCA0gs9x7oO4gHxVUDr94HX24Kv8DCHoQABoMNjM3NDIzMTgzODA1IgyObhAvbFG4vtMwkBoq3AMAootnJ5ipN16HKqxCWYIJLTImI05pNa%2BUKijJk2dM5ACwxOixjZQtBbYJRr5S243MrN5e5D%2FqAPO%2BLJvXAq0wEiXZTKR2d60WY4Jge2pJhamndmfrcR8unodG99fS23Zt5NcZzZXhytopJJ69eHRCglOMYYFQv10URAJwp5pNW4pkFOZJXgWZtS5ERTMJCWF8%2FwLjUv4lER2IlizUhQBl%2BeKgLKK%2BrMP0YqOzPNwSKk2AX9LCZjAEMOUGl4TYW6EzX4b531dfNXLMbxkSqMtZOJgO6o4KqOkQAwAb24HiLe1gsXtSeL6ERW27kzTURFiklDL%2FROJ%2BFXcER4opZdpKWeX4Xnc%2Fo5Xx%2FdOvBz%2BeXFd99IQ8sH%2FfMCluswoBu74rSys3U0fCfyKGKvNX7dERLvG8HBdDHjU4HWftHmeahRQsbZQuPeaOaY5fwAB45a5glSqO9Zpyx%2BwcdHZoLkTEKiDENwLwe%2FTPGHTrpZXruc5aUARyMWVl3Pxv3YenoxIiqkMOzEHrA4FGNluF2oDQt3RfZfcVPkr8yvm9AZ1RHlWSofkmRSkPKrhG58nT8CQx4onE8Rny0eywsDDyT2uxL0KpbY%2FNcvD2%2FlxzBjjQfKEwkmGOlfXJYnGHRDDH%2B5i9BjqkAUH%2F3htZp%2Fpz3BV6rQlAfs5xK9NHzwmVL4bYsB7amvnn%2BdtOYRFb%2BUVSh1UCEL1VIjyWwqdWvSIrp3ZCbY9eVfzJh6kAvQ5tFnrU8suk0Uploa2mWIOqCA%2FCieTqQ1rcF%2F2zFri5zmqgMAIJOMyU6rJGJOEZ6E2trEBHVZN0ebiEzv0PZSx7T0XO65VTPwcDW01PriNPbzjbqT1Xex0oEroPn2hh&X-Amz-Signature=eb0099a824361438dbbb5ad72ed4196fb3dd9619fb81a83443033dcb13ebd717&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJVUWCGT%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQDyILmfJFIyQg2WRPJOou22IKsShiXv7r2TspgbDfLsawIhAOP8xuxvZqORXnasWdQJCA0gs9x7oO4gHxVUDr94HX24Kv8DCHoQABoMNjM3NDIzMTgzODA1IgyObhAvbFG4vtMwkBoq3AMAootnJ5ipN16HKqxCWYIJLTImI05pNa%2BUKijJk2dM5ACwxOixjZQtBbYJRr5S243MrN5e5D%2FqAPO%2BLJvXAq0wEiXZTKR2d60WY4Jge2pJhamndmfrcR8unodG99fS23Zt5NcZzZXhytopJJ69eHRCglOMYYFQv10URAJwp5pNW4pkFOZJXgWZtS5ERTMJCWF8%2FwLjUv4lER2IlizUhQBl%2BeKgLKK%2BrMP0YqOzPNwSKk2AX9LCZjAEMOUGl4TYW6EzX4b531dfNXLMbxkSqMtZOJgO6o4KqOkQAwAb24HiLe1gsXtSeL6ERW27kzTURFiklDL%2FROJ%2BFXcER4opZdpKWeX4Xnc%2Fo5Xx%2FdOvBz%2BeXFd99IQ8sH%2FfMCluswoBu74rSys3U0fCfyKGKvNX7dERLvG8HBdDHjU4HWftHmeahRQsbZQuPeaOaY5fwAB45a5glSqO9Zpyx%2BwcdHZoLkTEKiDENwLwe%2FTPGHTrpZXruc5aUARyMWVl3Pxv3YenoxIiqkMOzEHrA4FGNluF2oDQt3RfZfcVPkr8yvm9AZ1RHlWSofkmRSkPKrhG58nT8CQx4onE8Rny0eywsDDyT2uxL0KpbY%2FNcvD2%2FlxzBjjQfKEwkmGOlfXJYnGHRDDH%2B5i9BjqkAUH%2F3htZp%2Fpz3BV6rQlAfs5xK9NHzwmVL4bYsB7amvnn%2BdtOYRFb%2BUVSh1UCEL1VIjyWwqdWvSIrp3ZCbY9eVfzJh6kAvQ5tFnrU8suk0Uploa2mWIOqCA%2FCieTqQ1rcF%2F2zFri5zmqgMAIJOMyU6rJGJOEZ6E2trEBHVZN0ebiEzv0PZSx7T0XO65VTPwcDW01PriNPbzjbqT1Xex0oEroPn2hh&X-Amz-Signature=433ca9191a7341d94a63ef68b3f382b92f72967852bc8f151bb39d7dbbd27451&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJVUWCGT%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQDyILmfJFIyQg2WRPJOou22IKsShiXv7r2TspgbDfLsawIhAOP8xuxvZqORXnasWdQJCA0gs9x7oO4gHxVUDr94HX24Kv8DCHoQABoMNjM3NDIzMTgzODA1IgyObhAvbFG4vtMwkBoq3AMAootnJ5ipN16HKqxCWYIJLTImI05pNa%2BUKijJk2dM5ACwxOixjZQtBbYJRr5S243MrN5e5D%2FqAPO%2BLJvXAq0wEiXZTKR2d60WY4Jge2pJhamndmfrcR8unodG99fS23Zt5NcZzZXhytopJJ69eHRCglOMYYFQv10URAJwp5pNW4pkFOZJXgWZtS5ERTMJCWF8%2FwLjUv4lER2IlizUhQBl%2BeKgLKK%2BrMP0YqOzPNwSKk2AX9LCZjAEMOUGl4TYW6EzX4b531dfNXLMbxkSqMtZOJgO6o4KqOkQAwAb24HiLe1gsXtSeL6ERW27kzTURFiklDL%2FROJ%2BFXcER4opZdpKWeX4Xnc%2Fo5Xx%2FdOvBz%2BeXFd99IQ8sH%2FfMCluswoBu74rSys3U0fCfyKGKvNX7dERLvG8HBdDHjU4HWftHmeahRQsbZQuPeaOaY5fwAB45a5glSqO9Zpyx%2BwcdHZoLkTEKiDENwLwe%2FTPGHTrpZXruc5aUARyMWVl3Pxv3YenoxIiqkMOzEHrA4FGNluF2oDQt3RfZfcVPkr8yvm9AZ1RHlWSofkmRSkPKrhG58nT8CQx4onE8Rny0eywsDDyT2uxL0KpbY%2FNcvD2%2FlxzBjjQfKEwkmGOlfXJYnGHRDDH%2B5i9BjqkAUH%2F3htZp%2Fpz3BV6rQlAfs5xK9NHzwmVL4bYsB7amvnn%2BdtOYRFb%2BUVSh1UCEL1VIjyWwqdWvSIrp3ZCbY9eVfzJh6kAvQ5tFnrU8suk0Uploa2mWIOqCA%2FCieTqQ1rcF%2F2zFri5zmqgMAIJOMyU6rJGJOEZ6E2trEBHVZN0ebiEzv0PZSx7T0XO65VTPwcDW01PriNPbzjbqT1Xex0oEroPn2hh&X-Amz-Signature=74779ce78a4d9e81fad5087ec4d7e18b3cb73f4f3ca8ffc10d395f2d06276abc&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJVUWCGT%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQDyILmfJFIyQg2WRPJOou22IKsShiXv7r2TspgbDfLsawIhAOP8xuxvZqORXnasWdQJCA0gs9x7oO4gHxVUDr94HX24Kv8DCHoQABoMNjM3NDIzMTgzODA1IgyObhAvbFG4vtMwkBoq3AMAootnJ5ipN16HKqxCWYIJLTImI05pNa%2BUKijJk2dM5ACwxOixjZQtBbYJRr5S243MrN5e5D%2FqAPO%2BLJvXAq0wEiXZTKR2d60WY4Jge2pJhamndmfrcR8unodG99fS23Zt5NcZzZXhytopJJ69eHRCglOMYYFQv10URAJwp5pNW4pkFOZJXgWZtS5ERTMJCWF8%2FwLjUv4lER2IlizUhQBl%2BeKgLKK%2BrMP0YqOzPNwSKk2AX9LCZjAEMOUGl4TYW6EzX4b531dfNXLMbxkSqMtZOJgO6o4KqOkQAwAb24HiLe1gsXtSeL6ERW27kzTURFiklDL%2FROJ%2BFXcER4opZdpKWeX4Xnc%2Fo5Xx%2FdOvBz%2BeXFd99IQ8sH%2FfMCluswoBu74rSys3U0fCfyKGKvNX7dERLvG8HBdDHjU4HWftHmeahRQsbZQuPeaOaY5fwAB45a5glSqO9Zpyx%2BwcdHZoLkTEKiDENwLwe%2FTPGHTrpZXruc5aUARyMWVl3Pxv3YenoxIiqkMOzEHrA4FGNluF2oDQt3RfZfcVPkr8yvm9AZ1RHlWSofkmRSkPKrhG58nT8CQx4onE8Rny0eywsDDyT2uxL0KpbY%2FNcvD2%2FlxzBjjQfKEwkmGOlfXJYnGHRDDH%2B5i9BjqkAUH%2F3htZp%2Fpz3BV6rQlAfs5xK9NHzwmVL4bYsB7amvnn%2BdtOYRFb%2BUVSh1UCEL1VIjyWwqdWvSIrp3ZCbY9eVfzJh6kAvQ5tFnrU8suk0Uploa2mWIOqCA%2FCieTqQ1rcF%2F2zFri5zmqgMAIJOMyU6rJGJOEZ6E2trEBHVZN0ebiEzv0PZSx7T0XO65VTPwcDW01PriNPbzjbqT1Xex0oEroPn2hh&X-Amz-Signature=6060222854e3a2b9aa49077a6e8880bfec904ea1be3e622f537b01d385a744ee&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
