

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WRBTLRM6%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC37VP2bx%2BZUYBixqaL%2BTJHvL5qeiTFAT9kV8LEindmKAIgG7twRviQSJHLBa7ZJX0wm%2BHJbKzcHuhgjRifj4WZ1nYq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDPdtATzaZuhEpSSFcyrcA5x5HTMI8oUuLrtdO%2FJxM545V4mvQNnerBUZrhIzK3dNu4sFWXI%2FTmJ2q1lsw87UbFR32T%2BDizSlcYiWvHBnpUf2Do6yuB4Do8Z7mSce2rBp8JMvTb8VymJt2S9d3uwhf3L1d2NrRaoHgbbOnVkzcwguJCAQZKP3x8javJVl8RLl6uJqFHgYx4ba%2BhASN7Lw6RNhg18%2B0L5DNDSs%2BsY6Qlq2fEDJnt7xP%2Bdm%2BO4pp5FtuvTc08OAqCECSwfPuRJetkZwPKJc9u3lJFhLC7ZhcaN%2Ffl7C6YE52959AbetODeIjWX6EPPGUXP9bXVCU1XMUkRpOnieMOeY%2FFeJJ5Bl4VBmWc%2Fg3QLk5i7D9TBPg8L1xFOAksvvBmcV0gxjojsPJEYRO8I16Jb2ivPaCuW5zwiZOOWR4shvnWRmyilY7VU%2FoUWnmRRb5ZOdpyK36Ls2OusjRZoeVFZazrqOUDknY8Fijr%2Bxrg1x7bLB2Aqzu0RX%2BCufh0eKCSXbL1h03w2Tro6%2F0SFs1yGO10MiFbH8OGF6RiJlijN5aPs3%2Fi1PC6ZMMWE8zNUOzQWFYeINnVgYQxUtjQ4Jby7KhKV%2B5PeKntaWqBeRvBcJSFDckbdNCsciwA8qKX8IZqZF03HoMM%2Fzgb0GOqUBCue7wZQvM%2FQcVOFTFA1Q0yrn%2F433J3QcNmpTm%2BKLuKlLi7%2B50gDSfpM34z0W1UkV9PEgA4zEGow2KhviY6c2ii%2FA1kShH00UhbNMolB1cuB74SpR3aTcK9TveYNN8bEQGn8qEclQ8S8OoJKumt3LENrc7m0ayC633P%2FyDLIcr1McZ4GA2XO5JhOBIZd4HJ1mwCX8BoDqhsyWxdG%2B0h3JuvETiEqV&X-Amz-Signature=a618b640970fd9c16b31cb01d79f6678bfc47e02b18841d8f95ef4947ff5b2d3&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WRBTLRM6%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC37VP2bx%2BZUYBixqaL%2BTJHvL5qeiTFAT9kV8LEindmKAIgG7twRviQSJHLBa7ZJX0wm%2BHJbKzcHuhgjRifj4WZ1nYq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDPdtATzaZuhEpSSFcyrcA5x5HTMI8oUuLrtdO%2FJxM545V4mvQNnerBUZrhIzK3dNu4sFWXI%2FTmJ2q1lsw87UbFR32T%2BDizSlcYiWvHBnpUf2Do6yuB4Do8Z7mSce2rBp8JMvTb8VymJt2S9d3uwhf3L1d2NrRaoHgbbOnVkzcwguJCAQZKP3x8javJVl8RLl6uJqFHgYx4ba%2BhASN7Lw6RNhg18%2B0L5DNDSs%2BsY6Qlq2fEDJnt7xP%2Bdm%2BO4pp5FtuvTc08OAqCECSwfPuRJetkZwPKJc9u3lJFhLC7ZhcaN%2Ffl7C6YE52959AbetODeIjWX6EPPGUXP9bXVCU1XMUkRpOnieMOeY%2FFeJJ5Bl4VBmWc%2Fg3QLk5i7D9TBPg8L1xFOAksvvBmcV0gxjojsPJEYRO8I16Jb2ivPaCuW5zwiZOOWR4shvnWRmyilY7VU%2FoUWnmRRb5ZOdpyK36Ls2OusjRZoeVFZazrqOUDknY8Fijr%2Bxrg1x7bLB2Aqzu0RX%2BCufh0eKCSXbL1h03w2Tro6%2F0SFs1yGO10MiFbH8OGF6RiJlijN5aPs3%2Fi1PC6ZMMWE8zNUOzQWFYeINnVgYQxUtjQ4Jby7KhKV%2B5PeKntaWqBeRvBcJSFDckbdNCsciwA8qKX8IZqZF03HoMM%2Fzgb0GOqUBCue7wZQvM%2FQcVOFTFA1Q0yrn%2F433J3QcNmpTm%2BKLuKlLi7%2B50gDSfpM34z0W1UkV9PEgA4zEGow2KhviY6c2ii%2FA1kShH00UhbNMolB1cuB74SpR3aTcK9TveYNN8bEQGn8qEclQ8S8OoJKumt3LENrc7m0ayC633P%2FyDLIcr1McZ4GA2XO5JhOBIZd4HJ1mwCX8BoDqhsyWxdG%2B0h3JuvETiEqV&X-Amz-Signature=b9301137050c6f259dc12fa3b4a5864743929e5269068bf580e82a3feca27973&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WRBTLRM6%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC37VP2bx%2BZUYBixqaL%2BTJHvL5qeiTFAT9kV8LEindmKAIgG7twRviQSJHLBa7ZJX0wm%2BHJbKzcHuhgjRifj4WZ1nYq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDPdtATzaZuhEpSSFcyrcA5x5HTMI8oUuLrtdO%2FJxM545V4mvQNnerBUZrhIzK3dNu4sFWXI%2FTmJ2q1lsw87UbFR32T%2BDizSlcYiWvHBnpUf2Do6yuB4Do8Z7mSce2rBp8JMvTb8VymJt2S9d3uwhf3L1d2NrRaoHgbbOnVkzcwguJCAQZKP3x8javJVl8RLl6uJqFHgYx4ba%2BhASN7Lw6RNhg18%2B0L5DNDSs%2BsY6Qlq2fEDJnt7xP%2Bdm%2BO4pp5FtuvTc08OAqCECSwfPuRJetkZwPKJc9u3lJFhLC7ZhcaN%2Ffl7C6YE52959AbetODeIjWX6EPPGUXP9bXVCU1XMUkRpOnieMOeY%2FFeJJ5Bl4VBmWc%2Fg3QLk5i7D9TBPg8L1xFOAksvvBmcV0gxjojsPJEYRO8I16Jb2ivPaCuW5zwiZOOWR4shvnWRmyilY7VU%2FoUWnmRRb5ZOdpyK36Ls2OusjRZoeVFZazrqOUDknY8Fijr%2Bxrg1x7bLB2Aqzu0RX%2BCufh0eKCSXbL1h03w2Tro6%2F0SFs1yGO10MiFbH8OGF6RiJlijN5aPs3%2Fi1PC6ZMMWE8zNUOzQWFYeINnVgYQxUtjQ4Jby7KhKV%2B5PeKntaWqBeRvBcJSFDckbdNCsciwA8qKX8IZqZF03HoMM%2Fzgb0GOqUBCue7wZQvM%2FQcVOFTFA1Q0yrn%2F433J3QcNmpTm%2BKLuKlLi7%2B50gDSfpM34z0W1UkV9PEgA4zEGow2KhviY6c2ii%2FA1kShH00UhbNMolB1cuB74SpR3aTcK9TveYNN8bEQGn8qEclQ8S8OoJKumt3LENrc7m0ayC633P%2FyDLIcr1McZ4GA2XO5JhOBIZd4HJ1mwCX8BoDqhsyWxdG%2B0h3JuvETiEqV&X-Amz-Signature=77a5ca8293a649ecfe3b160a023246f3b4bffd699205781cd43dbdd0338d710b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664EERCJHX%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF5zvTaqpTCbPzXCIUsUmdToFmPuYQfDW5FBmVJNk%2BmuAiEAo54AdEzroLigfffyO6A12uE7fUH4HYzPC6RBOEMByvwq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDDbBgi5BuNFV7YfIMCrcA63FQGtcrUwVHxg21AVsFPeHULmuV%2FHtLfS909gaIqMrc5%2BIpNsCs4aQczkouE0o1yBSUiTSdwEjCmdckGmoooTX1hoJI1c4bgeRZDLBYn2k6vDwe91oF%2FFtP2iHbsL9dZdQPKb4g5VPCLhDops5vesR7PPIFM4jHTVh9eRTC2pc9IzyVm0D5YC4uS7xXNPLDheFoc3Lsef4Le9enV%2BTF2SKTyo9oFGMB1ole2OFR9ybEu1bFz4TUBvrFNapKFqvKL62fGqp8C7aBZ38J5i5yMVQGf0ZkUInI3dDuQwh%2F1KXGFQEPKM7zktXFqCnR7bWCBaNCiAZwXRM0v8f7exFUDdARwnY86QkNfLK8ICdOeFa64Eq61MaMsLFAfh1jOrHMPOuMZ3pIj3GP6HTzOvkgDcCf1cNqpb7jtbHznZdaeHL%2B5qgoFAOduRClHzq2Tmkx9F2Q73JqZzYWa77wP7lvP6xlaIlWGPtd%2BbVw9Hc53TqH%2F8KbbRZm4Isc0UErVZUMLCIM%2Fv2wZNR%2BSbKnCEDamlgqoaSItcqzwg15b0ZcD5iMiasyC%2BHMZ8VLZTAGOGbA5lDZsmCpZBiM1dpo93pCDbLA%2Boce0ASUulD5xaBY1f6PssHeyZ7KBI5Tc1yMLnzgb0GOqUBXUZPxZzMgSoffs1ekuQh8irf%2BEzsSelXdMi%2FYsPGSS7JoHNrMw4MlrEmO5RnlcZoClC6ONCstsJGZ%2BZejd4%2FdljbVZujTQCK4ZCD%2FqhPwWXLVjbu7j67dIId%2BUkBUG%2B8ksbDfH8jA8%2FpN4S8eHs%2BlNMKtC2maWIhxa%2Fssyxu1VDM%2FEL2zW5dgzzhhUuv9Nc%2BDZQ2PlFKPP%2BeN5BJueYXnhzgTYC%2B&X-Amz-Signature=0c480e328e53631853e2d974acc299dc8b10e531f4dada7d91f0fbbac48f5640&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ORI5JPN%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICCbSqWOPiHUfp3kXWl5WKD%2F5h%2Fo78aUXxsbRvC5AlloAiBof%2BuHAxazbL1S9ZS2zj9TCyke5o6UPFCu4x6HjnxJESr%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMQ3C31ySO7KT8YBdfKtwDt5Bk52AgXRgTN3qfYFBymZAXzPXN4ST%2BILg%2FKR5zGhi%2BHSITGKktVk%2FoUAT56U%2BTfEzIJ2YnrmQrupFvJ6WYuktnNgDLcoxspUT3rjeDVEoHp51AVRs3WqLzJ2AcVg0oNc4QV6vIjsBOD1LIaQRrUROYq1bPyX9mzbLsl5VUSPqSN6bnFeRdmOVtcBH6tjgMuj0Wyovbqf22hdk1UKkNNJvvWKrgO4ubVqvH9Pe2T6epspZ5XYwe3b3MyNyXYHIwUuR2btdmI3JVR8F5vZ2LA1PcBl%2FyQXaidtoDFA0KKL9f8XWYwuECAChJAU1sm39yUG6WE8VwgoiRWNElMlDmlPzxN5aEVehUGOl2qIGXsnzhjHqlP%2FCNH9i1ieSP3BRWPkFf33abagsJwcwpi6FAGrWxFaTWn99hNFtK%2FmEBfAU7uj%2BcbFELvS%2BdsFwTFjLTXRMEnNPr8J7OHjEzxiBdPxFDmN%2FcumppTgWL%2Fz9p3tBnJUW5ZEY1Qb6DVJqq00mmg41bn0zoduDcgPSNhk1NQkwnJzAnjltVxHJOsx2KsrGy5D3RiJ2QNyzyh0YiW0F8BusQuQCMW%2Fp9FD9UI5y9ifhd2zgffN36kdx6nGgaFp2yQNK%2B%2B80XnZGfCU8w8PKBvQY6pgHSaSbhx5xbZ8lPULluLbYBiqt4QN%2BucBIn8XcfJlIkLhMYXWmkZ8rVvMgPcymrWHSpVT4%2Fo2a1kg5kXfjJsD8DQa0EcG8c2zbjidCZJatoaMrq3odqV%2BMBcrP786aZgBkn%2F1dCtgpaNALpTAdVBSAlgcjL8jTjB8Nr%2FId%2F0cT0c2pS6NqDUslLyHqVaoMG%2BSpFJ4pCU%2FycW%2FdvoJpQQ%2BpP2hruvCh6&X-Amz-Signature=b486157ad049ec9b6d6b45bbf062b0808be189f255bd1065633f822b8facdffd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WRBTLRM6%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC37VP2bx%2BZUYBixqaL%2BTJHvL5qeiTFAT9kV8LEindmKAIgG7twRviQSJHLBa7ZJX0wm%2BHJbKzcHuhgjRifj4WZ1nYq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDPdtATzaZuhEpSSFcyrcA5x5HTMI8oUuLrtdO%2FJxM545V4mvQNnerBUZrhIzK3dNu4sFWXI%2FTmJ2q1lsw87UbFR32T%2BDizSlcYiWvHBnpUf2Do6yuB4Do8Z7mSce2rBp8JMvTb8VymJt2S9d3uwhf3L1d2NrRaoHgbbOnVkzcwguJCAQZKP3x8javJVl8RLl6uJqFHgYx4ba%2BhASN7Lw6RNhg18%2B0L5DNDSs%2BsY6Qlq2fEDJnt7xP%2Bdm%2BO4pp5FtuvTc08OAqCECSwfPuRJetkZwPKJc9u3lJFhLC7ZhcaN%2Ffl7C6YE52959AbetODeIjWX6EPPGUXP9bXVCU1XMUkRpOnieMOeY%2FFeJJ5Bl4VBmWc%2Fg3QLk5i7D9TBPg8L1xFOAksvvBmcV0gxjojsPJEYRO8I16Jb2ivPaCuW5zwiZOOWR4shvnWRmyilY7VU%2FoUWnmRRb5ZOdpyK36Ls2OusjRZoeVFZazrqOUDknY8Fijr%2Bxrg1x7bLB2Aqzu0RX%2BCufh0eKCSXbL1h03w2Tro6%2F0SFs1yGO10MiFbH8OGF6RiJlijN5aPs3%2Fi1PC6ZMMWE8zNUOzQWFYeINnVgYQxUtjQ4Jby7KhKV%2B5PeKntaWqBeRvBcJSFDckbdNCsciwA8qKX8IZqZF03HoMM%2Fzgb0GOqUBCue7wZQvM%2FQcVOFTFA1Q0yrn%2F433J3QcNmpTm%2BKLuKlLi7%2B50gDSfpM34z0W1UkV9PEgA4zEGow2KhviY6c2ii%2FA1kShH00UhbNMolB1cuB74SpR3aTcK9TveYNN8bEQGn8qEclQ8S8OoJKumt3LENrc7m0ayC633P%2FyDLIcr1McZ4GA2XO5JhOBIZd4HJ1mwCX8BoDqhsyWxdG%2B0h3JuvETiEqV&X-Amz-Signature=3cd69ee6f4dfa3414f8dfd386ad0abe5a587351c14c03a4d086ed9e0e5cf13ce&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WRBTLRM6%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC37VP2bx%2BZUYBixqaL%2BTJHvL5qeiTFAT9kV8LEindmKAIgG7twRviQSJHLBa7ZJX0wm%2BHJbKzcHuhgjRifj4WZ1nYq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDPdtATzaZuhEpSSFcyrcA5x5HTMI8oUuLrtdO%2FJxM545V4mvQNnerBUZrhIzK3dNu4sFWXI%2FTmJ2q1lsw87UbFR32T%2BDizSlcYiWvHBnpUf2Do6yuB4Do8Z7mSce2rBp8JMvTb8VymJt2S9d3uwhf3L1d2NrRaoHgbbOnVkzcwguJCAQZKP3x8javJVl8RLl6uJqFHgYx4ba%2BhASN7Lw6RNhg18%2B0L5DNDSs%2BsY6Qlq2fEDJnt7xP%2Bdm%2BO4pp5FtuvTc08OAqCECSwfPuRJetkZwPKJc9u3lJFhLC7ZhcaN%2Ffl7C6YE52959AbetODeIjWX6EPPGUXP9bXVCU1XMUkRpOnieMOeY%2FFeJJ5Bl4VBmWc%2Fg3QLk5i7D9TBPg8L1xFOAksvvBmcV0gxjojsPJEYRO8I16Jb2ivPaCuW5zwiZOOWR4shvnWRmyilY7VU%2FoUWnmRRb5ZOdpyK36Ls2OusjRZoeVFZazrqOUDknY8Fijr%2Bxrg1x7bLB2Aqzu0RX%2BCufh0eKCSXbL1h03w2Tro6%2F0SFs1yGO10MiFbH8OGF6RiJlijN5aPs3%2Fi1PC6ZMMWE8zNUOzQWFYeINnVgYQxUtjQ4Jby7KhKV%2B5PeKntaWqBeRvBcJSFDckbdNCsciwA8qKX8IZqZF03HoMM%2Fzgb0GOqUBCue7wZQvM%2FQcVOFTFA1Q0yrn%2F433J3QcNmpTm%2BKLuKlLi7%2B50gDSfpM34z0W1UkV9PEgA4zEGow2KhviY6c2ii%2FA1kShH00UhbNMolB1cuB74SpR3aTcK9TveYNN8bEQGn8qEclQ8S8OoJKumt3LENrc7m0ayC633P%2FyDLIcr1McZ4GA2XO5JhOBIZd4HJ1mwCX8BoDqhsyWxdG%2B0h3JuvETiEqV&X-Amz-Signature=56cb5f6417a1fd54f186a18daf65a42c3932b70dfbf519881554c3a1efd63b10&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WRBTLRM6%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC37VP2bx%2BZUYBixqaL%2BTJHvL5qeiTFAT9kV8LEindmKAIgG7twRviQSJHLBa7ZJX0wm%2BHJbKzcHuhgjRifj4WZ1nYq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDPdtATzaZuhEpSSFcyrcA5x5HTMI8oUuLrtdO%2FJxM545V4mvQNnerBUZrhIzK3dNu4sFWXI%2FTmJ2q1lsw87UbFR32T%2BDizSlcYiWvHBnpUf2Do6yuB4Do8Z7mSce2rBp8JMvTb8VymJt2S9d3uwhf3L1d2NrRaoHgbbOnVkzcwguJCAQZKP3x8javJVl8RLl6uJqFHgYx4ba%2BhASN7Lw6RNhg18%2B0L5DNDSs%2BsY6Qlq2fEDJnt7xP%2Bdm%2BO4pp5FtuvTc08OAqCECSwfPuRJetkZwPKJc9u3lJFhLC7ZhcaN%2Ffl7C6YE52959AbetODeIjWX6EPPGUXP9bXVCU1XMUkRpOnieMOeY%2FFeJJ5Bl4VBmWc%2Fg3QLk5i7D9TBPg8L1xFOAksvvBmcV0gxjojsPJEYRO8I16Jb2ivPaCuW5zwiZOOWR4shvnWRmyilY7VU%2FoUWnmRRb5ZOdpyK36Ls2OusjRZoeVFZazrqOUDknY8Fijr%2Bxrg1x7bLB2Aqzu0RX%2BCufh0eKCSXbL1h03w2Tro6%2F0SFs1yGO10MiFbH8OGF6RiJlijN5aPs3%2Fi1PC6ZMMWE8zNUOzQWFYeINnVgYQxUtjQ4Jby7KhKV%2B5PeKntaWqBeRvBcJSFDckbdNCsciwA8qKX8IZqZF03HoMM%2Fzgb0GOqUBCue7wZQvM%2FQcVOFTFA1Q0yrn%2F433J3QcNmpTm%2BKLuKlLi7%2B50gDSfpM34z0W1UkV9PEgA4zEGow2KhviY6c2ii%2FA1kShH00UhbNMolB1cuB74SpR3aTcK9TveYNN8bEQGn8qEclQ8S8OoJKumt3LENrc7m0ayC633P%2FyDLIcr1McZ4GA2XO5JhOBIZd4HJ1mwCX8BoDqhsyWxdG%2B0h3JuvETiEqV&X-Amz-Signature=5702550cfc1b35598b29cfdbbc370dc7346e39d6b8e261e4988fd6e8d35504b9&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WRBTLRM6%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC37VP2bx%2BZUYBixqaL%2BTJHvL5qeiTFAT9kV8LEindmKAIgG7twRviQSJHLBa7ZJX0wm%2BHJbKzcHuhgjRifj4WZ1nYq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDPdtATzaZuhEpSSFcyrcA5x5HTMI8oUuLrtdO%2FJxM545V4mvQNnerBUZrhIzK3dNu4sFWXI%2FTmJ2q1lsw87UbFR32T%2BDizSlcYiWvHBnpUf2Do6yuB4Do8Z7mSce2rBp8JMvTb8VymJt2S9d3uwhf3L1d2NrRaoHgbbOnVkzcwguJCAQZKP3x8javJVl8RLl6uJqFHgYx4ba%2BhASN7Lw6RNhg18%2B0L5DNDSs%2BsY6Qlq2fEDJnt7xP%2Bdm%2BO4pp5FtuvTc08OAqCECSwfPuRJetkZwPKJc9u3lJFhLC7ZhcaN%2Ffl7C6YE52959AbetODeIjWX6EPPGUXP9bXVCU1XMUkRpOnieMOeY%2FFeJJ5Bl4VBmWc%2Fg3QLk5i7D9TBPg8L1xFOAksvvBmcV0gxjojsPJEYRO8I16Jb2ivPaCuW5zwiZOOWR4shvnWRmyilY7VU%2FoUWnmRRb5ZOdpyK36Ls2OusjRZoeVFZazrqOUDknY8Fijr%2Bxrg1x7bLB2Aqzu0RX%2BCufh0eKCSXbL1h03w2Tro6%2F0SFs1yGO10MiFbH8OGF6RiJlijN5aPs3%2Fi1PC6ZMMWE8zNUOzQWFYeINnVgYQxUtjQ4Jby7KhKV%2B5PeKntaWqBeRvBcJSFDckbdNCsciwA8qKX8IZqZF03HoMM%2Fzgb0GOqUBCue7wZQvM%2FQcVOFTFA1Q0yrn%2F433J3QcNmpTm%2BKLuKlLi7%2B50gDSfpM34z0W1UkV9PEgA4zEGow2KhviY6c2ii%2FA1kShH00UhbNMolB1cuB74SpR3aTcK9TveYNN8bEQGn8qEclQ8S8OoJKumt3LENrc7m0ayC633P%2FyDLIcr1McZ4GA2XO5JhOBIZd4HJ1mwCX8BoDqhsyWxdG%2B0h3JuvETiEqV&X-Amz-Signature=845552de2636f2111530e79cf0c3b6a84e645c22b06bb0379c1f9005ac478b64&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
