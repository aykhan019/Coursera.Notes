

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XU3AISY6%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCIBGM2bYZ8LBBe%2B31LEpsA%2BJi2RQ%2FjNJISsceeJiAAXM9AiEA%2FCy0O3FfkeYsmauPMKteNVX3zETOICE%2Bx%2FbLN%2BADovMq%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDOgtdsLmZK7MfPTAXCrcA1zQnMsiW%2BNF9So%2FrxVj8Zs4cPFIuLkhsJ9VyQhgQEjDYcVlisJQoPwWTuKqaOVnruvy1PYiwP5zyyrJq0kyz23np9ZK6Q8vUnyNTSg9R2saaAjHFJAFVYKOYV6OAYbWz4mjXZIMcsw91TZJRo%2BoazcxFeJLOIh5uRLxysdjacw1eVOWbmHuwS6FaaELPUjAcJf5CPFAO7RpQhVS3t7DaPyU7oNLKssA8ZNkBN9XS0VG37qcxBN%2FL3Mzjh9d28AvQqbxVVVnhKE%2F5NdoO0ber3oB3OjpUIpxdthOcIY%2FyBiV0cq1s%2BAQiTWO4N9YNBfAwKCVRv4pu1rlA1cMiw3fs4bp2fP6IlwpZRaCqSy2aSSfFDyCXIZrqXGc%2BAEzjGsa7QqCnrnvb8JF57Rzgc%2B7G2hyymnqphs4PYwB5h4P5dGuixoGzc4OHSRH3kXFimO%2FzGSxb%2Bv0wcS7qkdvf3cwP%2FL9fp5lU0JMNmuu9e8mvJqSwOqFmxeYtU8yov4tBeywjOaX3SF6JLXVN8GIu73Yl8EFx4yZ5%2BuRhhwCvI9EXd7kG%2BaK%2Bme9uYH0DxzkvV%2FYAtB9U65KXNQ3dhqb6Tix0YpI5%2FrInfaZPgTH7ZIjLUaQeLBWjYOegMbZjHXuMKiUir0GOqUBz2Fd%2BE3FBPSJbKr07S1Js5OiA0gthlZd6J49hDe6zo09RVycjIk4K6SXc1%2FFSiIrZI88%2F2fh6OK5NGP%2FZNvaqEM1CFVIaf7R9jfGlKc0O6brLuwjNwz1df6RIkwGMNyecQToqo345GQPusmf9FnabY8o37xTAtmMA3kNrvLVo7ll7jlAa8ISGdZMlg5R4aa%2FsEgXBYNCIzvA3htaS0x3fDGgxT9G&X-Amz-Signature=9febfc68fe12159ea5f4bc9dc3939fdf3c8258a08f82224162bb61bc4ad27bb4&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XU3AISY6%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCIBGM2bYZ8LBBe%2B31LEpsA%2BJi2RQ%2FjNJISsceeJiAAXM9AiEA%2FCy0O3FfkeYsmauPMKteNVX3zETOICE%2Bx%2FbLN%2BADovMq%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDOgtdsLmZK7MfPTAXCrcA1zQnMsiW%2BNF9So%2FrxVj8Zs4cPFIuLkhsJ9VyQhgQEjDYcVlisJQoPwWTuKqaOVnruvy1PYiwP5zyyrJq0kyz23np9ZK6Q8vUnyNTSg9R2saaAjHFJAFVYKOYV6OAYbWz4mjXZIMcsw91TZJRo%2BoazcxFeJLOIh5uRLxysdjacw1eVOWbmHuwS6FaaELPUjAcJf5CPFAO7RpQhVS3t7DaPyU7oNLKssA8ZNkBN9XS0VG37qcxBN%2FL3Mzjh9d28AvQqbxVVVnhKE%2F5NdoO0ber3oB3OjpUIpxdthOcIY%2FyBiV0cq1s%2BAQiTWO4N9YNBfAwKCVRv4pu1rlA1cMiw3fs4bp2fP6IlwpZRaCqSy2aSSfFDyCXIZrqXGc%2BAEzjGsa7QqCnrnvb8JF57Rzgc%2B7G2hyymnqphs4PYwB5h4P5dGuixoGzc4OHSRH3kXFimO%2FzGSxb%2Bv0wcS7qkdvf3cwP%2FL9fp5lU0JMNmuu9e8mvJqSwOqFmxeYtU8yov4tBeywjOaX3SF6JLXVN8GIu73Yl8EFx4yZ5%2BuRhhwCvI9EXd7kG%2BaK%2Bme9uYH0DxzkvV%2FYAtB9U65KXNQ3dhqb6Tix0YpI5%2FrInfaZPgTH7ZIjLUaQeLBWjYOegMbZjHXuMKiUir0GOqUBz2Fd%2BE3FBPSJbKr07S1Js5OiA0gthlZd6J49hDe6zo09RVycjIk4K6SXc1%2FFSiIrZI88%2F2fh6OK5NGP%2FZNvaqEM1CFVIaf7R9jfGlKc0O6brLuwjNwz1df6RIkwGMNyecQToqo345GQPusmf9FnabY8o37xTAtmMA3kNrvLVo7ll7jlAa8ISGdZMlg5R4aa%2FsEgXBYNCIzvA3htaS0x3fDGgxT9G&X-Amz-Signature=6d8164e8a693a25a8c3863dde1bc534126b50ba7eae86cd1cc87a4b290f6319d&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XU3AISY6%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCIBGM2bYZ8LBBe%2B31LEpsA%2BJi2RQ%2FjNJISsceeJiAAXM9AiEA%2FCy0O3FfkeYsmauPMKteNVX3zETOICE%2Bx%2FbLN%2BADovMq%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDOgtdsLmZK7MfPTAXCrcA1zQnMsiW%2BNF9So%2FrxVj8Zs4cPFIuLkhsJ9VyQhgQEjDYcVlisJQoPwWTuKqaOVnruvy1PYiwP5zyyrJq0kyz23np9ZK6Q8vUnyNTSg9R2saaAjHFJAFVYKOYV6OAYbWz4mjXZIMcsw91TZJRo%2BoazcxFeJLOIh5uRLxysdjacw1eVOWbmHuwS6FaaELPUjAcJf5CPFAO7RpQhVS3t7DaPyU7oNLKssA8ZNkBN9XS0VG37qcxBN%2FL3Mzjh9d28AvQqbxVVVnhKE%2F5NdoO0ber3oB3OjpUIpxdthOcIY%2FyBiV0cq1s%2BAQiTWO4N9YNBfAwKCVRv4pu1rlA1cMiw3fs4bp2fP6IlwpZRaCqSy2aSSfFDyCXIZrqXGc%2BAEzjGsa7QqCnrnvb8JF57Rzgc%2B7G2hyymnqphs4PYwB5h4P5dGuixoGzc4OHSRH3kXFimO%2FzGSxb%2Bv0wcS7qkdvf3cwP%2FL9fp5lU0JMNmuu9e8mvJqSwOqFmxeYtU8yov4tBeywjOaX3SF6JLXVN8GIu73Yl8EFx4yZ5%2BuRhhwCvI9EXd7kG%2BaK%2Bme9uYH0DxzkvV%2FYAtB9U65KXNQ3dhqb6Tix0YpI5%2FrInfaZPgTH7ZIjLUaQeLBWjYOegMbZjHXuMKiUir0GOqUBz2Fd%2BE3FBPSJbKr07S1Js5OiA0gthlZd6J49hDe6zo09RVycjIk4K6SXc1%2FFSiIrZI88%2F2fh6OK5NGP%2FZNvaqEM1CFVIaf7R9jfGlKc0O6brLuwjNwz1df6RIkwGMNyecQToqo345GQPusmf9FnabY8o37xTAtmMA3kNrvLVo7ll7jlAa8ISGdZMlg5R4aa%2FsEgXBYNCIzvA3htaS0x3fDGgxT9G&X-Amz-Signature=438dd98d2f967f7f449eb3b0f8cfb16d964ac6062817e381d7d56580cc6e8854&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664437I6MK%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJGMEQCIAC89OTcAZOoCmfIooazF1%2B9B%2B5QNmjJv3zf%2BBZBCDdjAiBaVn6wIPUczISME3Ybj%2Fh8k5gDZivstZ2SwLDe1szDISr%2FAwg3EAAaDDYzNzQyMzE4MzgwNSIMcI3sX02EtTX0GO4sKtwDYuNkrlkn7kdyKOpbtbzv%2BVXsRp5QJGiV31sCzAodp10aFh7OjkSkVzWdyYcvEpBfiFwkkQIGW9SdaNqm%2B3Y6yHOiIEBjmEonFPR8iixaLBAUu2%2BZf7P3Qo8DBhdlWnC%2F8nn5CRPPapIOcErEDGKxgwGFA0jQtlMtsHMigH58%2BWSE62C5GFlUsQg12eBXGBj1baxV%2FEBL8czrng8utY5TPT8jn6SQtI3jTc18y7Do%2Be7XX2tuMfAxqWNWBnS8TgoQ9WcdsTlWZ4M7E072D65Q3ysSSyugWzlGWHwcWcv5Rm1YtVuCS11792fBbvOVaJ7LAVdf4f444yNvGlsY1plgIzqTE11tumibMbO3udmjRt063t73SNEdNVIW5RyTyk6e98TpsVxVTdZ9aFzhKMsbLLecbTpKIJKhxKUragbP%2FsD7jeGF661vhWp8eNgQ5pWfqF4JH3B6PmWIe9IRt3YnuTyZEriT%2FyJj7otupULuM4LjIt5naSUy8i%2BOZALtVw7x1hpMGefi%2FuBntqGneW2DvVeK%2Fb%2FvyqXcC4O69GSHw3SeIePqtIanxCZJkh0mj9G6Ov5LGyJdkjazrI6pT0N9gc0GnZglyr2CqKdwwwTTQlDH5YRhseurXIUeIIownJSKvQY6pgGZwe3oZC0eZlnGB4mf9yOa84fzBpFoWv2dLm5NkC%2BqF2ke8C1rKdGgEipoDhhuBa8XAmPxBYCDEdkOFEroDav7kchOP76WLjCR2dsPQ3knaX3H6RtM1T3onnX07oQ9dzAQxHOe05bnRqgd8jhMmyP%2FENQClw%2FF9mediUt5ihgV2NTWgcMlqZW%2BrdEGyOePrHWb0P67Pwjv9Jt%2FlIeJ7tK%2FAowfi5V0&X-Amz-Signature=1a90b03f82c19d607c789d979ac6a43bae71245a8bb6c80a81b082b649ddf523&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ZOAYMBR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCIQDqcQAh%2BBrkWkJjfVqHiAMJEuS4jyDGgBCdyt9UB4HhKwIgCcFTjEK8Zv5yQqE%2F822On4IR4t0C4j73OB9RPrYnqxUq%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDPREcJ0WnyxvefidySrcAymGIBKfcNNEVOvyE0CY4TUOGfONa1w04EuMtNtED%2FM3BBya9rMbt0xJ3xXd9rksKZEvGzik5USpycyroeKjnd0qxORjeicw%2FH5xVp%2F%2BLrcJt%2FcN4J6J%2BDBaFD75ZIHSLOmHNJVVU%2Fcj5MSgg22r%2BBHjBOZZJIJD%2BEFGCe8FowGaBpecpjJQLFP1Pfixxfh4MQez0iGlxK1E00d4sZco8DgToDxOWJJQEaR0B1o%2BQW8armyXiY%2BZnayujX39Acr5dFrcRkGFG7%2B5wdxe%2BA%2Bl4PU6yuGxNJyFT2H57IUiJwLJVGaTTOThBgc3nw9yI0a%2BzN8tGx1YyD4JvYhU9jufI8oKJgblplQ%2F7nks5Kc5MK6TV8UiT%2FF61GpqJIUtSDGT0HHeTw4EnS1yHtP15J4siJlnbo3YAOQFDzJ7KQ0Rp1mRLnL%2B6LVzZ4WWDfNrRwUvTlvOQuKlLMIeies7gygOfq1J%2BKoPwq7d8LzkyA%2BSsztzaw9f6MrU81zb6%2F6XDaev6QAM5dtkA%2Fl6HFeysAETaLRTOm%2B5yrnivs6DVeS0xw0RLc4ysVnK6MLwvmVvdmEoZ%2FCAjo2BthQCx46UVekf7MTRC8YmTSUgyU7ezEGQQi2d3YcdPGGpbOVgoIi7MIyUir0GOqUBNKb%2FiVASM29v2i7SdeE5p9t0Rixw2LHIw%2FZKnfYJfzIFMmXtDz7NTWnPYercyNmkejB2duxts%2BLg56Rq7s85yyCUeQNXm8ohAz29PX%2B3s9Ajzs3VIjYXcmfZJCbb8uTRWWDFMDAxi1Oi5GhnZ3qcdXFbkRRoXnxZfZXB375%2Bpp3zhu%2BDZXR1BGEWWc%2BC5GhKVccYT%2B5BU9q1zY7chgb8xQx7z7ke&X-Amz-Signature=8c9f810224cc7ecb3aee4acf88dc586dc923823746496308f57e6b98ef1a46fa&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XU3AISY6%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCIBGM2bYZ8LBBe%2B31LEpsA%2BJi2RQ%2FjNJISsceeJiAAXM9AiEA%2FCy0O3FfkeYsmauPMKteNVX3zETOICE%2Bx%2FbLN%2BADovMq%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDOgtdsLmZK7MfPTAXCrcA1zQnMsiW%2BNF9So%2FrxVj8Zs4cPFIuLkhsJ9VyQhgQEjDYcVlisJQoPwWTuKqaOVnruvy1PYiwP5zyyrJq0kyz23np9ZK6Q8vUnyNTSg9R2saaAjHFJAFVYKOYV6OAYbWz4mjXZIMcsw91TZJRo%2BoazcxFeJLOIh5uRLxysdjacw1eVOWbmHuwS6FaaELPUjAcJf5CPFAO7RpQhVS3t7DaPyU7oNLKssA8ZNkBN9XS0VG37qcxBN%2FL3Mzjh9d28AvQqbxVVVnhKE%2F5NdoO0ber3oB3OjpUIpxdthOcIY%2FyBiV0cq1s%2BAQiTWO4N9YNBfAwKCVRv4pu1rlA1cMiw3fs4bp2fP6IlwpZRaCqSy2aSSfFDyCXIZrqXGc%2BAEzjGsa7QqCnrnvb8JF57Rzgc%2B7G2hyymnqphs4PYwB5h4P5dGuixoGzc4OHSRH3kXFimO%2FzGSxb%2Bv0wcS7qkdvf3cwP%2FL9fp5lU0JMNmuu9e8mvJqSwOqFmxeYtU8yov4tBeywjOaX3SF6JLXVN8GIu73Yl8EFx4yZ5%2BuRhhwCvI9EXd7kG%2BaK%2Bme9uYH0DxzkvV%2FYAtB9U65KXNQ3dhqb6Tix0YpI5%2FrInfaZPgTH7ZIjLUaQeLBWjYOegMbZjHXuMKiUir0GOqUBz2Fd%2BE3FBPSJbKr07S1Js5OiA0gthlZd6J49hDe6zo09RVycjIk4K6SXc1%2FFSiIrZI88%2F2fh6OK5NGP%2FZNvaqEM1CFVIaf7R9jfGlKc0O6brLuwjNwz1df6RIkwGMNyecQToqo345GQPusmf9FnabY8o37xTAtmMA3kNrvLVo7ll7jlAa8ISGdZMlg5R4aa%2FsEgXBYNCIzvA3htaS0x3fDGgxT9G&X-Amz-Signature=04485587ba323b110c316c4ffade8de9021b3f679aef6059f46860e5dc2310a3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XU3AISY6%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCIBGM2bYZ8LBBe%2B31LEpsA%2BJi2RQ%2FjNJISsceeJiAAXM9AiEA%2FCy0O3FfkeYsmauPMKteNVX3zETOICE%2Bx%2FbLN%2BADovMq%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDOgtdsLmZK7MfPTAXCrcA1zQnMsiW%2BNF9So%2FrxVj8Zs4cPFIuLkhsJ9VyQhgQEjDYcVlisJQoPwWTuKqaOVnruvy1PYiwP5zyyrJq0kyz23np9ZK6Q8vUnyNTSg9R2saaAjHFJAFVYKOYV6OAYbWz4mjXZIMcsw91TZJRo%2BoazcxFeJLOIh5uRLxysdjacw1eVOWbmHuwS6FaaELPUjAcJf5CPFAO7RpQhVS3t7DaPyU7oNLKssA8ZNkBN9XS0VG37qcxBN%2FL3Mzjh9d28AvQqbxVVVnhKE%2F5NdoO0ber3oB3OjpUIpxdthOcIY%2FyBiV0cq1s%2BAQiTWO4N9YNBfAwKCVRv4pu1rlA1cMiw3fs4bp2fP6IlwpZRaCqSy2aSSfFDyCXIZrqXGc%2BAEzjGsa7QqCnrnvb8JF57Rzgc%2B7G2hyymnqphs4PYwB5h4P5dGuixoGzc4OHSRH3kXFimO%2FzGSxb%2Bv0wcS7qkdvf3cwP%2FL9fp5lU0JMNmuu9e8mvJqSwOqFmxeYtU8yov4tBeywjOaX3SF6JLXVN8GIu73Yl8EFx4yZ5%2BuRhhwCvI9EXd7kG%2BaK%2Bme9uYH0DxzkvV%2FYAtB9U65KXNQ3dhqb6Tix0YpI5%2FrInfaZPgTH7ZIjLUaQeLBWjYOegMbZjHXuMKiUir0GOqUBz2Fd%2BE3FBPSJbKr07S1Js5OiA0gthlZd6J49hDe6zo09RVycjIk4K6SXc1%2FFSiIrZI88%2F2fh6OK5NGP%2FZNvaqEM1CFVIaf7R9jfGlKc0O6brLuwjNwz1df6RIkwGMNyecQToqo345GQPusmf9FnabY8o37xTAtmMA3kNrvLVo7ll7jlAa8ISGdZMlg5R4aa%2FsEgXBYNCIzvA3htaS0x3fDGgxT9G&X-Amz-Signature=cf1299522bbb22c8cc1c63b10e10de05b8fe2ac1d0f5dcdfe613398b34548d75&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XU3AISY6%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCIBGM2bYZ8LBBe%2B31LEpsA%2BJi2RQ%2FjNJISsceeJiAAXM9AiEA%2FCy0O3FfkeYsmauPMKteNVX3zETOICE%2Bx%2FbLN%2BADovMq%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDOgtdsLmZK7MfPTAXCrcA1zQnMsiW%2BNF9So%2FrxVj8Zs4cPFIuLkhsJ9VyQhgQEjDYcVlisJQoPwWTuKqaOVnruvy1PYiwP5zyyrJq0kyz23np9ZK6Q8vUnyNTSg9R2saaAjHFJAFVYKOYV6OAYbWz4mjXZIMcsw91TZJRo%2BoazcxFeJLOIh5uRLxysdjacw1eVOWbmHuwS6FaaELPUjAcJf5CPFAO7RpQhVS3t7DaPyU7oNLKssA8ZNkBN9XS0VG37qcxBN%2FL3Mzjh9d28AvQqbxVVVnhKE%2F5NdoO0ber3oB3OjpUIpxdthOcIY%2FyBiV0cq1s%2BAQiTWO4N9YNBfAwKCVRv4pu1rlA1cMiw3fs4bp2fP6IlwpZRaCqSy2aSSfFDyCXIZrqXGc%2BAEzjGsa7QqCnrnvb8JF57Rzgc%2B7G2hyymnqphs4PYwB5h4P5dGuixoGzc4OHSRH3kXFimO%2FzGSxb%2Bv0wcS7qkdvf3cwP%2FL9fp5lU0JMNmuu9e8mvJqSwOqFmxeYtU8yov4tBeywjOaX3SF6JLXVN8GIu73Yl8EFx4yZ5%2BuRhhwCvI9EXd7kG%2BaK%2Bme9uYH0DxzkvV%2FYAtB9U65KXNQ3dhqb6Tix0YpI5%2FrInfaZPgTH7ZIjLUaQeLBWjYOegMbZjHXuMKiUir0GOqUBz2Fd%2BE3FBPSJbKr07S1Js5OiA0gthlZd6J49hDe6zo09RVycjIk4K6SXc1%2FFSiIrZI88%2F2fh6OK5NGP%2FZNvaqEM1CFVIaf7R9jfGlKc0O6brLuwjNwz1df6RIkwGMNyecQToqo345GQPusmf9FnabY8o37xTAtmMA3kNrvLVo7ll7jlAa8ISGdZMlg5R4aa%2FsEgXBYNCIzvA3htaS0x3fDGgxT9G&X-Amz-Signature=e0c7d4cee4fa229d38fb4e6735228342d78821398b70cbfefb69751144335693&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XU3AISY6%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCIBGM2bYZ8LBBe%2B31LEpsA%2BJi2RQ%2FjNJISsceeJiAAXM9AiEA%2FCy0O3FfkeYsmauPMKteNVX3zETOICE%2Bx%2FbLN%2BADovMq%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDOgtdsLmZK7MfPTAXCrcA1zQnMsiW%2BNF9So%2FrxVj8Zs4cPFIuLkhsJ9VyQhgQEjDYcVlisJQoPwWTuKqaOVnruvy1PYiwP5zyyrJq0kyz23np9ZK6Q8vUnyNTSg9R2saaAjHFJAFVYKOYV6OAYbWz4mjXZIMcsw91TZJRo%2BoazcxFeJLOIh5uRLxysdjacw1eVOWbmHuwS6FaaELPUjAcJf5CPFAO7RpQhVS3t7DaPyU7oNLKssA8ZNkBN9XS0VG37qcxBN%2FL3Mzjh9d28AvQqbxVVVnhKE%2F5NdoO0ber3oB3OjpUIpxdthOcIY%2FyBiV0cq1s%2BAQiTWO4N9YNBfAwKCVRv4pu1rlA1cMiw3fs4bp2fP6IlwpZRaCqSy2aSSfFDyCXIZrqXGc%2BAEzjGsa7QqCnrnvb8JF57Rzgc%2B7G2hyymnqphs4PYwB5h4P5dGuixoGzc4OHSRH3kXFimO%2FzGSxb%2Bv0wcS7qkdvf3cwP%2FL9fp5lU0JMNmuu9e8mvJqSwOqFmxeYtU8yov4tBeywjOaX3SF6JLXVN8GIu73Yl8EFx4yZ5%2BuRhhwCvI9EXd7kG%2BaK%2Bme9uYH0DxzkvV%2FYAtB9U65KXNQ3dhqb6Tix0YpI5%2FrInfaZPgTH7ZIjLUaQeLBWjYOegMbZjHXuMKiUir0GOqUBz2Fd%2BE3FBPSJbKr07S1Js5OiA0gthlZd6J49hDe6zo09RVycjIk4K6SXc1%2FFSiIrZI88%2F2fh6OK5NGP%2FZNvaqEM1CFVIaf7R9jfGlKc0O6brLuwjNwz1df6RIkwGMNyecQToqo345GQPusmf9FnabY8o37xTAtmMA3kNrvLVo7ll7jlAa8ISGdZMlg5R4aa%2FsEgXBYNCIzvA3htaS0x3fDGgxT9G&X-Amz-Signature=a0cf821ce03d98b564e79aa2fac755069e50057e662ff8fceb30350168ded5c1&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
