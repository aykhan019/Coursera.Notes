

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RY6QPE7S%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJGMEQCIEqYhjYd82ExI%2FhYHhJbF8QUbfJS7bhtggAEoNrmGIeSAiBogbhhLDmSZPsq74lI0xDcg%2Ffn8%2BZvOnxeuJ2X1dtzxCqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrzQlqVUPRKIUcre%2BKtwDFrE%2FDuPCSEeRYdNbwT5aPmomJSoffhG%2FRij61cgEKvztwMHCn0C2%2Fczy9MoD3J05eQPytEYlLk9b%2Fa%2FPc%2FAcVZRQC9pwYqOkGDyfk81iElsdBO51sIZv9pEZlZsIKiCRnDg0Ipu3ikHj18lVJ5GZfk52ozlwCwuCkwTAtT6BISgSikRKO2Nqo7X2zWSIjj0p4BDUfOXvonTG8iMzBDI8CzYHvmwh9Ydw7h%2BsPuzndBJaGuThgDpij8UQBUUNv0k3c9Te1aDVEMSq4ODod%2F1NV7NSRU9hvm3jX0RTkVRi32TvrMO%2BFiyGFIXMfn%2FxlT%2F8e1WaWcT%2BcNft4KpHHZ3k3hCUXHc0SHQYK79T0RJ6HMRoVgdEv6RU9rpHtrKDXaKHniQYeZSJP2h%2BesmBNxH4FGg0fd3h2nDOhtICWvb5uhwasTawM3wMHP8U8LebXsN%2BFTKuoeYJzYjEST7ufZfSMr%2FcaDKjKUp6%2Fz3UIroX23DC9%2F13k05KTf%2BHdER%2BG7enGSOua1Rki3YQQDRY4OODt7rsJou2r%2F71P1JZMbhv2WtTBimepLrR3fkxXD16miFm%2FXPvQEGI9rCQtAukaVSuULWbC3TT8V4QbQmZcWt%2BfIJjEIo1FV71E9me6DMwmp2ivwY6pgHk2%2BP5br1z%2B%2Flu8ceqWZIeIeYpWavCKv%2BwbO7hLcziv9y%2Fmz3zYABUyyvIqSVA67I7yrZEZ8g0ZwPgsPYsF0Z2P9fzydPbsc39TV25dpRj29EyaPrl2oGEgz95ZQDzM9DoCBbuXH4GhOPNBTP1ANoZ5Sexo2r8U7FnK0%2BpNd0gNYFB%2BedoUOLyg0t6hMQNyExQjiNrFytV27JWzE8Ex2oxDjf6EMZL&X-Amz-Signature=51b7cdd8ff8a648b9cfed7d4a980718b6b4d65bd05c7ee4851df15243005dcfd&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RY6QPE7S%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJGMEQCIEqYhjYd82ExI%2FhYHhJbF8QUbfJS7bhtggAEoNrmGIeSAiBogbhhLDmSZPsq74lI0xDcg%2Ffn8%2BZvOnxeuJ2X1dtzxCqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrzQlqVUPRKIUcre%2BKtwDFrE%2FDuPCSEeRYdNbwT5aPmomJSoffhG%2FRij61cgEKvztwMHCn0C2%2Fczy9MoD3J05eQPytEYlLk9b%2Fa%2FPc%2FAcVZRQC9pwYqOkGDyfk81iElsdBO51sIZv9pEZlZsIKiCRnDg0Ipu3ikHj18lVJ5GZfk52ozlwCwuCkwTAtT6BISgSikRKO2Nqo7X2zWSIjj0p4BDUfOXvonTG8iMzBDI8CzYHvmwh9Ydw7h%2BsPuzndBJaGuThgDpij8UQBUUNv0k3c9Te1aDVEMSq4ODod%2F1NV7NSRU9hvm3jX0RTkVRi32TvrMO%2BFiyGFIXMfn%2FxlT%2F8e1WaWcT%2BcNft4KpHHZ3k3hCUXHc0SHQYK79T0RJ6HMRoVgdEv6RU9rpHtrKDXaKHniQYeZSJP2h%2BesmBNxH4FGg0fd3h2nDOhtICWvb5uhwasTawM3wMHP8U8LebXsN%2BFTKuoeYJzYjEST7ufZfSMr%2FcaDKjKUp6%2Fz3UIroX23DC9%2F13k05KTf%2BHdER%2BG7enGSOua1Rki3YQQDRY4OODt7rsJou2r%2F71P1JZMbhv2WtTBimepLrR3fkxXD16miFm%2FXPvQEGI9rCQtAukaVSuULWbC3TT8V4QbQmZcWt%2BfIJjEIo1FV71E9me6DMwmp2ivwY6pgHk2%2BP5br1z%2B%2Flu8ceqWZIeIeYpWavCKv%2BwbO7hLcziv9y%2Fmz3zYABUyyvIqSVA67I7yrZEZ8g0ZwPgsPYsF0Z2P9fzydPbsc39TV25dpRj29EyaPrl2oGEgz95ZQDzM9DoCBbuXH4GhOPNBTP1ANoZ5Sexo2r8U7FnK0%2BpNd0gNYFB%2BedoUOLyg0t6hMQNyExQjiNrFytV27JWzE8Ex2oxDjf6EMZL&X-Amz-Signature=3f76816c6fe1586eab3fd268f33aa2665664d63b70aef28c3100fce3186d79ba&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RY6QPE7S%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJGMEQCIEqYhjYd82ExI%2FhYHhJbF8QUbfJS7bhtggAEoNrmGIeSAiBogbhhLDmSZPsq74lI0xDcg%2Ffn8%2BZvOnxeuJ2X1dtzxCqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrzQlqVUPRKIUcre%2BKtwDFrE%2FDuPCSEeRYdNbwT5aPmomJSoffhG%2FRij61cgEKvztwMHCn0C2%2Fczy9MoD3J05eQPytEYlLk9b%2Fa%2FPc%2FAcVZRQC9pwYqOkGDyfk81iElsdBO51sIZv9pEZlZsIKiCRnDg0Ipu3ikHj18lVJ5GZfk52ozlwCwuCkwTAtT6BISgSikRKO2Nqo7X2zWSIjj0p4BDUfOXvonTG8iMzBDI8CzYHvmwh9Ydw7h%2BsPuzndBJaGuThgDpij8UQBUUNv0k3c9Te1aDVEMSq4ODod%2F1NV7NSRU9hvm3jX0RTkVRi32TvrMO%2BFiyGFIXMfn%2FxlT%2F8e1WaWcT%2BcNft4KpHHZ3k3hCUXHc0SHQYK79T0RJ6HMRoVgdEv6RU9rpHtrKDXaKHniQYeZSJP2h%2BesmBNxH4FGg0fd3h2nDOhtICWvb5uhwasTawM3wMHP8U8LebXsN%2BFTKuoeYJzYjEST7ufZfSMr%2FcaDKjKUp6%2Fz3UIroX23DC9%2F13k05KTf%2BHdER%2BG7enGSOua1Rki3YQQDRY4OODt7rsJou2r%2F71P1JZMbhv2WtTBimepLrR3fkxXD16miFm%2FXPvQEGI9rCQtAukaVSuULWbC3TT8V4QbQmZcWt%2BfIJjEIo1FV71E9me6DMwmp2ivwY6pgHk2%2BP5br1z%2B%2Flu8ceqWZIeIeYpWavCKv%2BwbO7hLcziv9y%2Fmz3zYABUyyvIqSVA67I7yrZEZ8g0ZwPgsPYsF0Z2P9fzydPbsc39TV25dpRj29EyaPrl2oGEgz95ZQDzM9DoCBbuXH4GhOPNBTP1ANoZ5Sexo2r8U7FnK0%2BpNd0gNYFB%2BedoUOLyg0t6hMQNyExQjiNrFytV27JWzE8Ex2oxDjf6EMZL&X-Amz-Signature=89b43ed6636dfaa12a17cc4f63b530afe8cd5d0fb23744b0a0baea73d887c333&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ZXROMXO%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004516Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJGMEQCH0wjDxZ9Z7CpNEMnfgl15Ewp0G9172rr3Npt%2BvuTNVECIQCQ5emCVcHMiaeEaoQd3sZrddZkFUq80a6VwLiJYIDQfSqIBAiC%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMQnJpvigIcwwVV43TKtwD%2BfBkOdR%2BCTpk4zlmb2Q3ou1d0oo9tn3UoCYixS%2FEU81o90Up%2F95SJ%2F8XDMeYpu4TendYPPXffn8mnDvbdQLkCBVP8hnw2d3GMWemBj%2FgwxMNjwJw4W3%2Bg%2Bn9I%2FB%2FWOUjd3EPMUXk6boucRZWzcC%2BhYN%2BPhTDzl13oR5q2s1sBJYnMYhCmYND8%2BoMZUcwgZZutNtkh3qtMpKMYsCAn%2BHsF3a1SJ0d%2BM7LDcFP%2BL5RkZZilSKg4j1GJkfZ61dp%2BpU1f9pqnKZGSjmi71Guk5STihBGOmpAvDEqoEKyGW0kNvSv7AlNUJrEmDLxFQHaejNAbFav9DRmQXnQDZLJqiqEJV0GEpJEcHzrPfe%2BoVsWCXaYTuRMhyVnGg1xIsfuxnMz7H0ngr8TqliKfViw6wHKvBS3nwcSLlNmuRo9eX3LPUs9pxkhXpM7xz7ji8ursR6ILuZipyQeNgW7%2FTysXqFSTDMsImk%2F%2F3GJ2vPJelYHpI4Dg7qrnzj9kQFHLYKZLzxwGod8C%2FHHo1D8967nViPpOlQtdMTWUJzts53LWFflazxb9ZBPOE4Eqem1no4XmSUC4JIv0t0cTo8UO68jCAwYGxnXoCO%2FY24mXhssAAqqUVh5F2%2Bvc2tH17doUOAwk6GivwY6pgGmYYxO9eQArwnoK0DOK67AQcN67uoaoXk%2BTaYPaZ%2FsqGLLn%2BoiLpbJdMl9K1bdMIwWT7WG5SRNcj4Uyh2wFeJRdq3SV5dcXR8uJkc7cJgVoeKhlpyZCAepyvnmQAiBENKrUcobZNy4Rc4PnjT92PpM42TeYVtn31wUGoXX1b7dgz0kwEnAv4x3XiqL2zsMAUpbGtEFwT918kP8lAWkIPiZY7RROoTy&X-Amz-Signature=bd3210ec878dfc112f270549efd7b53660474a850ebd61f327479e659cfc9ddc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YXG57E3O%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIQDUpk%2BmJ09AffUSeuOyHQGCHDga4vP%2BMhhE4mLt9v%2BVfgIgDyBi9IetLLrH92Dk6K18eRsHiq1pZ2W2lyBWqBkgBzcqiAQIgP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLMJVEMJnMqEh2yIUircA82L3z7bcU5zUpE6h1GL0r5SetXCavy323AzvaXUkedZ%2Bgut5V3nz1L8RvCWXydtty9NsIY875HOJVBe%2FeXB3RJgkm%2FDg3OOHuessKgiIo1WpA1z7bSiWdeczJvqcncjQxXfwkkPEQeHrfhZPtIkD9dMBiyzN1JDcPabbb6ZCGFWi1rFHf0rfOyqUI3K%2BiVBQA9UvvhOob5vzruZpkl%2B2uquUlIbC8aq7SEonj0ISCpdVdZmfA7ehhcvKo6TezXnNiGwHlYVtxGGL1P%2BxZ05Kw%2BVZVmFK1Fnx8qa00g9qq5KJejFQh9DQHVBsngSUE9g5bsmaNHdmZgTlpTgV3x7Cb6EpAv9vAWybdMsakqIGXg16ZchI5cP39VsDexFdveUd1M2rBYZ0LYHAY3%2BAsLptBdY8SuVJQsQdeHmuJbYZJEyuLLdSfkuGdfWVTjvZLt%2B%2BFAZkcjZRsVE82Eqdy6t6Y1TJaNNEn%2F3dWbL8zgMF2AnWvS1tynBfF33uPJj1G2DLZOg%2FXJWitOytBDBZNUcg5s%2BW8AZEUyNrhzdk3iUQQ%2Bf9IylK2HLQVMQxcu%2BkgVUZdy0qqsyACaqH6ikZ4umIDxi0RZ0vMB8%2BBQl6%2B%2BpWO%2B%2FhVgR%2FqeNYgcSJkamMJ78ob8GOqUBHCPB4NLDCgcOuBpemD8pnexEpK3eAwNpT7XYRNAV34M4mSS7i%2FxKyxqws3mpiMODyMUiPV1vHYgLL07WBm8LVt3avF2MnbmBUZpphaaaKep%2Bx1XeXzWjaQvLy27d9E3e20xrG4oFVCt6XEbWhjwROnCqZDvFB2dwLqdNWYy7T9LBtKLvpvqcGsB0zshX8JJyAP%2FIaIEKtI7voVCuoeZ93DbWGBFk&X-Amz-Signature=c9c6c31b31337b8ce33bbbccf7feae95a3d6de51745484ba1c048300ce09d0fb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RY6QPE7S%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJGMEQCIEqYhjYd82ExI%2FhYHhJbF8QUbfJS7bhtggAEoNrmGIeSAiBogbhhLDmSZPsq74lI0xDcg%2Ffn8%2BZvOnxeuJ2X1dtzxCqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrzQlqVUPRKIUcre%2BKtwDFrE%2FDuPCSEeRYdNbwT5aPmomJSoffhG%2FRij61cgEKvztwMHCn0C2%2Fczy9MoD3J05eQPytEYlLk9b%2Fa%2FPc%2FAcVZRQC9pwYqOkGDyfk81iElsdBO51sIZv9pEZlZsIKiCRnDg0Ipu3ikHj18lVJ5GZfk52ozlwCwuCkwTAtT6BISgSikRKO2Nqo7X2zWSIjj0p4BDUfOXvonTG8iMzBDI8CzYHvmwh9Ydw7h%2BsPuzndBJaGuThgDpij8UQBUUNv0k3c9Te1aDVEMSq4ODod%2F1NV7NSRU9hvm3jX0RTkVRi32TvrMO%2BFiyGFIXMfn%2FxlT%2F8e1WaWcT%2BcNft4KpHHZ3k3hCUXHc0SHQYK79T0RJ6HMRoVgdEv6RU9rpHtrKDXaKHniQYeZSJP2h%2BesmBNxH4FGg0fd3h2nDOhtICWvb5uhwasTawM3wMHP8U8LebXsN%2BFTKuoeYJzYjEST7ufZfSMr%2FcaDKjKUp6%2Fz3UIroX23DC9%2F13k05KTf%2BHdER%2BG7enGSOua1Rki3YQQDRY4OODt7rsJou2r%2F71P1JZMbhv2WtTBimepLrR3fkxXD16miFm%2FXPvQEGI9rCQtAukaVSuULWbC3TT8V4QbQmZcWt%2BfIJjEIo1FV71E9me6DMwmp2ivwY6pgHk2%2BP5br1z%2B%2Flu8ceqWZIeIeYpWavCKv%2BwbO7hLcziv9y%2Fmz3zYABUyyvIqSVA67I7yrZEZ8g0ZwPgsPYsF0Z2P9fzydPbsc39TV25dpRj29EyaPrl2oGEgz95ZQDzM9DoCBbuXH4GhOPNBTP1ANoZ5Sexo2r8U7FnK0%2BpNd0gNYFB%2BedoUOLyg0t6hMQNyExQjiNrFytV27JWzE8Ex2oxDjf6EMZL&X-Amz-Signature=fcaace226399f644116af3c422702e24c2ee90eefd99eb9e5b6b871872e39c6b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RY6QPE7S%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJGMEQCIEqYhjYd82ExI%2FhYHhJbF8QUbfJS7bhtggAEoNrmGIeSAiBogbhhLDmSZPsq74lI0xDcg%2Ffn8%2BZvOnxeuJ2X1dtzxCqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrzQlqVUPRKIUcre%2BKtwDFrE%2FDuPCSEeRYdNbwT5aPmomJSoffhG%2FRij61cgEKvztwMHCn0C2%2Fczy9MoD3J05eQPytEYlLk9b%2Fa%2FPc%2FAcVZRQC9pwYqOkGDyfk81iElsdBO51sIZv9pEZlZsIKiCRnDg0Ipu3ikHj18lVJ5GZfk52ozlwCwuCkwTAtT6BISgSikRKO2Nqo7X2zWSIjj0p4BDUfOXvonTG8iMzBDI8CzYHvmwh9Ydw7h%2BsPuzndBJaGuThgDpij8UQBUUNv0k3c9Te1aDVEMSq4ODod%2F1NV7NSRU9hvm3jX0RTkVRi32TvrMO%2BFiyGFIXMfn%2FxlT%2F8e1WaWcT%2BcNft4KpHHZ3k3hCUXHc0SHQYK79T0RJ6HMRoVgdEv6RU9rpHtrKDXaKHniQYeZSJP2h%2BesmBNxH4FGg0fd3h2nDOhtICWvb5uhwasTawM3wMHP8U8LebXsN%2BFTKuoeYJzYjEST7ufZfSMr%2FcaDKjKUp6%2Fz3UIroX23DC9%2F13k05KTf%2BHdER%2BG7enGSOua1Rki3YQQDRY4OODt7rsJou2r%2F71P1JZMbhv2WtTBimepLrR3fkxXD16miFm%2FXPvQEGI9rCQtAukaVSuULWbC3TT8V4QbQmZcWt%2BfIJjEIo1FV71E9me6DMwmp2ivwY6pgHk2%2BP5br1z%2B%2Flu8ceqWZIeIeYpWavCKv%2BwbO7hLcziv9y%2Fmz3zYABUyyvIqSVA67I7yrZEZ8g0ZwPgsPYsF0Z2P9fzydPbsc39TV25dpRj29EyaPrl2oGEgz95ZQDzM9DoCBbuXH4GhOPNBTP1ANoZ5Sexo2r8U7FnK0%2BpNd0gNYFB%2BedoUOLyg0t6hMQNyExQjiNrFytV27JWzE8Ex2oxDjf6EMZL&X-Amz-Signature=6b63c28e737bd1c6b51dd1431793e6f3deab24297661b1699ba256b8ff8153a9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RY6QPE7S%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJGMEQCIEqYhjYd82ExI%2FhYHhJbF8QUbfJS7bhtggAEoNrmGIeSAiBogbhhLDmSZPsq74lI0xDcg%2Ffn8%2BZvOnxeuJ2X1dtzxCqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrzQlqVUPRKIUcre%2BKtwDFrE%2FDuPCSEeRYdNbwT5aPmomJSoffhG%2FRij61cgEKvztwMHCn0C2%2Fczy9MoD3J05eQPytEYlLk9b%2Fa%2FPc%2FAcVZRQC9pwYqOkGDyfk81iElsdBO51sIZv9pEZlZsIKiCRnDg0Ipu3ikHj18lVJ5GZfk52ozlwCwuCkwTAtT6BISgSikRKO2Nqo7X2zWSIjj0p4BDUfOXvonTG8iMzBDI8CzYHvmwh9Ydw7h%2BsPuzndBJaGuThgDpij8UQBUUNv0k3c9Te1aDVEMSq4ODod%2F1NV7NSRU9hvm3jX0RTkVRi32TvrMO%2BFiyGFIXMfn%2FxlT%2F8e1WaWcT%2BcNft4KpHHZ3k3hCUXHc0SHQYK79T0RJ6HMRoVgdEv6RU9rpHtrKDXaKHniQYeZSJP2h%2BesmBNxH4FGg0fd3h2nDOhtICWvb5uhwasTawM3wMHP8U8LebXsN%2BFTKuoeYJzYjEST7ufZfSMr%2FcaDKjKUp6%2Fz3UIroX23DC9%2F13k05KTf%2BHdER%2BG7enGSOua1Rki3YQQDRY4OODt7rsJou2r%2F71P1JZMbhv2WtTBimepLrR3fkxXD16miFm%2FXPvQEGI9rCQtAukaVSuULWbC3TT8V4QbQmZcWt%2BfIJjEIo1FV71E9me6DMwmp2ivwY6pgHk2%2BP5br1z%2B%2Flu8ceqWZIeIeYpWavCKv%2BwbO7hLcziv9y%2Fmz3zYABUyyvIqSVA67I7yrZEZ8g0ZwPgsPYsF0Z2P9fzydPbsc39TV25dpRj29EyaPrl2oGEgz95ZQDzM9DoCBbuXH4GhOPNBTP1ANoZ5Sexo2r8U7FnK0%2BpNd0gNYFB%2BedoUOLyg0t6hMQNyExQjiNrFytV27JWzE8Ex2oxDjf6EMZL&X-Amz-Signature=cec516ac300bdc763771d3df4ed532cbae8aafbd6f998f74b53b1295f65790fe&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RY6QPE7S%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJGMEQCIEqYhjYd82ExI%2FhYHhJbF8QUbfJS7bhtggAEoNrmGIeSAiBogbhhLDmSZPsq74lI0xDcg%2Ffn8%2BZvOnxeuJ2X1dtzxCqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrzQlqVUPRKIUcre%2BKtwDFrE%2FDuPCSEeRYdNbwT5aPmomJSoffhG%2FRij61cgEKvztwMHCn0C2%2Fczy9MoD3J05eQPytEYlLk9b%2Fa%2FPc%2FAcVZRQC9pwYqOkGDyfk81iElsdBO51sIZv9pEZlZsIKiCRnDg0Ipu3ikHj18lVJ5GZfk52ozlwCwuCkwTAtT6BISgSikRKO2Nqo7X2zWSIjj0p4BDUfOXvonTG8iMzBDI8CzYHvmwh9Ydw7h%2BsPuzndBJaGuThgDpij8UQBUUNv0k3c9Te1aDVEMSq4ODod%2F1NV7NSRU9hvm3jX0RTkVRi32TvrMO%2BFiyGFIXMfn%2FxlT%2F8e1WaWcT%2BcNft4KpHHZ3k3hCUXHc0SHQYK79T0RJ6HMRoVgdEv6RU9rpHtrKDXaKHniQYeZSJP2h%2BesmBNxH4FGg0fd3h2nDOhtICWvb5uhwasTawM3wMHP8U8LebXsN%2BFTKuoeYJzYjEST7ufZfSMr%2FcaDKjKUp6%2Fz3UIroX23DC9%2F13k05KTf%2BHdER%2BG7enGSOua1Rki3YQQDRY4OODt7rsJou2r%2F71P1JZMbhv2WtTBimepLrR3fkxXD16miFm%2FXPvQEGI9rCQtAukaVSuULWbC3TT8V4QbQmZcWt%2BfIJjEIo1FV71E9me6DMwmp2ivwY6pgHk2%2BP5br1z%2B%2Flu8ceqWZIeIeYpWavCKv%2BwbO7hLcziv9y%2Fmz3zYABUyyvIqSVA67I7yrZEZ8g0ZwPgsPYsF0Z2P9fzydPbsc39TV25dpRj29EyaPrl2oGEgz95ZQDzM9DoCBbuXH4GhOPNBTP1ANoZ5Sexo2r8U7FnK0%2BpNd0gNYFB%2BedoUOLyg0t6hMQNyExQjiNrFytV27JWzE8Ex2oxDjf6EMZL&X-Amz-Signature=c7f0ca9b4e6639d1cb63b69d9f35278f1937d59299df01ff6f88572fb0fad550&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
