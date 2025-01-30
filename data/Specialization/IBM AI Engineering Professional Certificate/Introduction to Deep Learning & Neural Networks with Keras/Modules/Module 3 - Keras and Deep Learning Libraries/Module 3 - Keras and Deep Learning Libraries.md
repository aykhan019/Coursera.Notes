

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663W3LDFDE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC2sbHz%2Fbx6zEJSm8ENN1uKgJB6MRlBJ97zRul7WFUTdgIgXLTdMLjSoonxBplkdZOQ2Qf6LU6msAGfwgG%2BcYKov8IqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDErZOOtRjF15GDnXfSrcA9YXaVYKySJYzJgc8HTHbmiwem0k20jm3zFuRqPTcIXeAdZbQsd%2FKysMAsO6jkt9vEnF0UbpWmLVdoZWamUJhGfk56aX1M14YBxxTULviqaiGY49INKlo%2F79goH8NDb3MiAJp5v4tQjMfMovRxZsYkvUvq1mTtb2UkzcTBeYy5oGLuKT72ZI%2BUOlSYjydM2wf40eklr65c6J94vnhY3WPwydJqqc6EGxhUcWVJmyHr8aaH6OFSsfkw1PAthUNeD%2BQpys49rIciCM2BpkDwq0TeUARo9QeJEtZpdWpJ1nAaTARSl9H5AunqEvUHq%2BMNP%2B%2BwEAZQ2QXZ4EyKu8e8MIw78olH141AEMUOCqIj8VVGJ6FTafX7Z%2BCixi3tDdJyes4Roi%2BTHMQcSwOq4yFyFkSAW6EsFz14H2bxQiA9vjvK7VWDc6uFaC0ySwMnmO4gT%2F88nf7rsiKfdoYoYypoGrHYbqpUAkmnG6zYM0shmFaTBB8fbCzAAl8PIJ8zCW9UHX6YiOb3IcJIAtd66lyS4ItpL5RAGDUrgp66nLE9uijLelMPKxmP5rgdnR49gKMMuc2eN2PFcOcub3aYUJZp1nTAszZ4QLhEN1AAxC%2FaERORTF4ybLkeRpPz4yKjawMN6W67wGOqUBODk1XtmvZaIeZ85hnfekGBgsqWtGBt8Xy6d7zU7aA%2FdarU2rjZqr1tokh2wtc8MURa7feOdMBTX7gn%2F5ow2OQqbvxqXnSTqRNQmvHnsGrtS5IWCVlYW5oc27Jw32QhVUlW2ATULd11vCqits3CxEV9EB%2BXMcMoz8OSlU5Vny8uMJjK1%2B5qPPazwd3zS1A1zCbhBfFeRybX7oavbb2yBK1Tev3lU8&X-Amz-Signature=d4c322e167242ff0eafa90496611d9353b77481301fdd859b6d90bb442dfaec2&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663W3LDFDE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC2sbHz%2Fbx6zEJSm8ENN1uKgJB6MRlBJ97zRul7WFUTdgIgXLTdMLjSoonxBplkdZOQ2Qf6LU6msAGfwgG%2BcYKov8IqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDErZOOtRjF15GDnXfSrcA9YXaVYKySJYzJgc8HTHbmiwem0k20jm3zFuRqPTcIXeAdZbQsd%2FKysMAsO6jkt9vEnF0UbpWmLVdoZWamUJhGfk56aX1M14YBxxTULviqaiGY49INKlo%2F79goH8NDb3MiAJp5v4tQjMfMovRxZsYkvUvq1mTtb2UkzcTBeYy5oGLuKT72ZI%2BUOlSYjydM2wf40eklr65c6J94vnhY3WPwydJqqc6EGxhUcWVJmyHr8aaH6OFSsfkw1PAthUNeD%2BQpys49rIciCM2BpkDwq0TeUARo9QeJEtZpdWpJ1nAaTARSl9H5AunqEvUHq%2BMNP%2B%2BwEAZQ2QXZ4EyKu8e8MIw78olH141AEMUOCqIj8VVGJ6FTafX7Z%2BCixi3tDdJyes4Roi%2BTHMQcSwOq4yFyFkSAW6EsFz14H2bxQiA9vjvK7VWDc6uFaC0ySwMnmO4gT%2F88nf7rsiKfdoYoYypoGrHYbqpUAkmnG6zYM0shmFaTBB8fbCzAAl8PIJ8zCW9UHX6YiOb3IcJIAtd66lyS4ItpL5RAGDUrgp66nLE9uijLelMPKxmP5rgdnR49gKMMuc2eN2PFcOcub3aYUJZp1nTAszZ4QLhEN1AAxC%2FaERORTF4ybLkeRpPz4yKjawMN6W67wGOqUBODk1XtmvZaIeZ85hnfekGBgsqWtGBt8Xy6d7zU7aA%2FdarU2rjZqr1tokh2wtc8MURa7feOdMBTX7gn%2F5ow2OQqbvxqXnSTqRNQmvHnsGrtS5IWCVlYW5oc27Jw32QhVUlW2ATULd11vCqits3CxEV9EB%2BXMcMoz8OSlU5Vny8uMJjK1%2B5qPPazwd3zS1A1zCbhBfFeRybX7oavbb2yBK1Tev3lU8&X-Amz-Signature=4c72269ec2bbccf315a32d9b7b4dbc818cbf5316dd12869c36d0085c261c4973&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663W3LDFDE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC2sbHz%2Fbx6zEJSm8ENN1uKgJB6MRlBJ97zRul7WFUTdgIgXLTdMLjSoonxBplkdZOQ2Qf6LU6msAGfwgG%2BcYKov8IqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDErZOOtRjF15GDnXfSrcA9YXaVYKySJYzJgc8HTHbmiwem0k20jm3zFuRqPTcIXeAdZbQsd%2FKysMAsO6jkt9vEnF0UbpWmLVdoZWamUJhGfk56aX1M14YBxxTULviqaiGY49INKlo%2F79goH8NDb3MiAJp5v4tQjMfMovRxZsYkvUvq1mTtb2UkzcTBeYy5oGLuKT72ZI%2BUOlSYjydM2wf40eklr65c6J94vnhY3WPwydJqqc6EGxhUcWVJmyHr8aaH6OFSsfkw1PAthUNeD%2BQpys49rIciCM2BpkDwq0TeUARo9QeJEtZpdWpJ1nAaTARSl9H5AunqEvUHq%2BMNP%2B%2BwEAZQ2QXZ4EyKu8e8MIw78olH141AEMUOCqIj8VVGJ6FTafX7Z%2BCixi3tDdJyes4Roi%2BTHMQcSwOq4yFyFkSAW6EsFz14H2bxQiA9vjvK7VWDc6uFaC0ySwMnmO4gT%2F88nf7rsiKfdoYoYypoGrHYbqpUAkmnG6zYM0shmFaTBB8fbCzAAl8PIJ8zCW9UHX6YiOb3IcJIAtd66lyS4ItpL5RAGDUrgp66nLE9uijLelMPKxmP5rgdnR49gKMMuc2eN2PFcOcub3aYUJZp1nTAszZ4QLhEN1AAxC%2FaERORTF4ybLkeRpPz4yKjawMN6W67wGOqUBODk1XtmvZaIeZ85hnfekGBgsqWtGBt8Xy6d7zU7aA%2FdarU2rjZqr1tokh2wtc8MURa7feOdMBTX7gn%2F5ow2OQqbvxqXnSTqRNQmvHnsGrtS5IWCVlYW5oc27Jw32QhVUlW2ATULd11vCqits3CxEV9EB%2BXMcMoz8OSlU5Vny8uMJjK1%2B5qPPazwd3zS1A1zCbhBfFeRybX7oavbb2yBK1Tev3lU8&X-Amz-Signature=cf61536ce2c81530d06b915e19b583e9a651169febd97cc9a2aadad43e57fb69&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665H6XVLVL%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010715Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDRSknuDWCUQhSwIWROp%2BQUCE4SChebt1nP5gNDNIbu1QIhAObiPzKoMMxxh1nFR7nzEuveusTEXwGB4mva7rkyXGA%2FKogECJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxZaj2krLLs6oq3R38q3APryBt6UznwnbOtKZ%2BVNpYbvFGwLCBvC3QbrUAkRqESOvGPm4fy25WqpDp89iG4DWrGFbjVWVF0NTzWBIdBS9XXLCySWQypnDwKn0QDnwaBewov3tg5PD%2BCJKvxrvI52dBNNFtOuh%2FvLuA3YXrxbyltuNNX11uVvN63YDw0kxMlk3I97nT0Dk%2FkRDFFvHzdMU9wxgyemUfA0H5v14VGHSfjEnGnqIlwvKfymGfLKTE3kkbYBL3gfrgoA6rDChByfKK8Q64Tw40ATOeamKNGL3nzeLKroVPpe8gdH49%2BQUdwvoHQgo%2B5cORHo67slfsZI0w5HoODrCe0S8NkStsKvVMPtKD%2F4%2FVsq3B70jhiyZfxqj2SScBs3RCukqo2N1skSSMlG%2Bbrx%2Baa%2BPsYxH62R%2BB2yNGSAVPQbRwIpOdR%2BLRtu328yzmoVPobe%2FjHKBEGjLojWVgTR340fqdgu8KPuBTQS250nSMbjLc1wMQgQ4iEc9pHTaeCqwMOeoxvqXfDrM0LkmudKOxFf4tuTrRAEel%2FUf%2Bdn2TqKBdcsoAeO6%2FwH0xR3Iwis7ycpVWOHMJixaANWF2%2FJjBWapklP1pQbINn7IlRVS4Fcqm7zLNbgVsJ4jlpsL0ipnE0D134hDDQluu8BjqkAaANdal4RHF%2Bugqkch%2F7OKrFLcARLrudsqiXzXQo%2BfPiAl4eDiyi51irBJEZCamL9EXmptDnRHo708bf788tX3IR7WVcx5re6fuBmw%2B6eQn6G0CM%2F3YiD%2BT%2BPxMkCO%2BJTEIfbj%2ByXrgYt5Kkbla%2FVAamXb00iwws0aW4PcUVNIIvCi%2FKKTrNaT1BRcvNtIWbvCHXaDPbXagKD%2FLq3VZCXUq7ESiD&X-Amz-Signature=9594b7e6f58d01087a06e515d86203fef34294cc744964c5553a251c07da3372&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VDCXD4NM%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010715Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCWYLmmbMZvszP4aMeMlhVnh7NIfiDuKs2%2FRwZ5X3iXgQIhAO1VPpQYg%2FEwZn7ocMpSfWMnYzIJKSxS7sMq33jA8wKmKogECJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy7ow6yG6GyE%2Bewwjgq3AMGF%2BK9hXCjC6FnbOHXA2UL8ZyCR0s0Ot5DWrbDvEcQn%2BvmvLy4nK14QgXF0XE31tmNHHJl20B97p%2FhzHVGR5A7lBwJP1yozW9xZP9vAut03IZTkQJjd1cS7wVU1HpyZ7URhKkHuC98757jzYRbXUBZk5y6N29jWrD97AJpdN8JYgyYwAmCUvrN6hi%2F1gTtfBnSP4PUjuYFOhnRT6PiSFUHcDXHT3szeQsjus5B5XO13lzG0YO5TEXiwuI0n6SKv3d0eboQrB%2B7LbyXcE6fis131PfMyzDOhaW8ibGxf3xZRYHuoLttiJXgf7JMxecVM9cTNYZEsEP22U51Gequ5%2FVS8VaLS14citzvlj8PiE2%2BPFw6hLFUdrFsXo0d8ieLTLwPjXlCWcn0SkkKk8fiZ9jKMRSUKF0Vs4uo39AN6Zc9rZD0FIXsyVOxXojyZ5UTxmZK1LLBMOdjyjPKplpuYvT%2BZyar4z3KYPo4Q5XFu1RCe2dlDZMGAicW5LuiGH7XygSv3WIOiaMosjl1GAbDM6psPBx66YBrt%2Bzkbxr0pIwJ2LSv2SuOyAUBR8eniMlGULq1vEFZjclP6h%2BVjg5ubiKGwS9BVxdU3X7Kumi8xXZ5bnggCJ8d1Cyz5zUojDCjmOu8BjqkAT3ooytbsFm7mBNpGQhO%2BzxTuPEkomJ7TAWiPb2ObnO3pzNqDcYGZBQmLiv7mByGb5EBrDZ5qJbMlL04O%2BVKZFzHeW9krUIEAQ54TZe5RpvXQ64tB8FepPEOHLU1dOjasJHsjhkh8F%2Fg0y%2BfI7AezoTectMpYjUAn7PURV5U18CZ4KzY79Tt41Vx3v9yJPo5owri%2FLDhBlHiyOTGHMMQGnnIU8Z4&X-Amz-Signature=ec3a15b53d1df7f7d3b0fde96746266c19412baa24ca41cc1f6806003ebea2bb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663W3LDFDE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC2sbHz%2Fbx6zEJSm8ENN1uKgJB6MRlBJ97zRul7WFUTdgIgXLTdMLjSoonxBplkdZOQ2Qf6LU6msAGfwgG%2BcYKov8IqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDErZOOtRjF15GDnXfSrcA9YXaVYKySJYzJgc8HTHbmiwem0k20jm3zFuRqPTcIXeAdZbQsd%2FKysMAsO6jkt9vEnF0UbpWmLVdoZWamUJhGfk56aX1M14YBxxTULviqaiGY49INKlo%2F79goH8NDb3MiAJp5v4tQjMfMovRxZsYkvUvq1mTtb2UkzcTBeYy5oGLuKT72ZI%2BUOlSYjydM2wf40eklr65c6J94vnhY3WPwydJqqc6EGxhUcWVJmyHr8aaH6OFSsfkw1PAthUNeD%2BQpys49rIciCM2BpkDwq0TeUARo9QeJEtZpdWpJ1nAaTARSl9H5AunqEvUHq%2BMNP%2B%2BwEAZQ2QXZ4EyKu8e8MIw78olH141AEMUOCqIj8VVGJ6FTafX7Z%2BCixi3tDdJyes4Roi%2BTHMQcSwOq4yFyFkSAW6EsFz14H2bxQiA9vjvK7VWDc6uFaC0ySwMnmO4gT%2F88nf7rsiKfdoYoYypoGrHYbqpUAkmnG6zYM0shmFaTBB8fbCzAAl8PIJ8zCW9UHX6YiOb3IcJIAtd66lyS4ItpL5RAGDUrgp66nLE9uijLelMPKxmP5rgdnR49gKMMuc2eN2PFcOcub3aYUJZp1nTAszZ4QLhEN1AAxC%2FaERORTF4ybLkeRpPz4yKjawMN6W67wGOqUBODk1XtmvZaIeZ85hnfekGBgsqWtGBt8Xy6d7zU7aA%2FdarU2rjZqr1tokh2wtc8MURa7feOdMBTX7gn%2F5ow2OQqbvxqXnSTqRNQmvHnsGrtS5IWCVlYW5oc27Jw32QhVUlW2ATULd11vCqits3CxEV9EB%2BXMcMoz8OSlU5Vny8uMJjK1%2B5qPPazwd3zS1A1zCbhBfFeRybX7oavbb2yBK1Tev3lU8&X-Amz-Signature=f21f9f9b53ac4f8ad5718665da5153b4f1900754c891b9c9867eac8f5f6afa07&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663W3LDFDE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC2sbHz%2Fbx6zEJSm8ENN1uKgJB6MRlBJ97zRul7WFUTdgIgXLTdMLjSoonxBplkdZOQ2Qf6LU6msAGfwgG%2BcYKov8IqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDErZOOtRjF15GDnXfSrcA9YXaVYKySJYzJgc8HTHbmiwem0k20jm3zFuRqPTcIXeAdZbQsd%2FKysMAsO6jkt9vEnF0UbpWmLVdoZWamUJhGfk56aX1M14YBxxTULviqaiGY49INKlo%2F79goH8NDb3MiAJp5v4tQjMfMovRxZsYkvUvq1mTtb2UkzcTBeYy5oGLuKT72ZI%2BUOlSYjydM2wf40eklr65c6J94vnhY3WPwydJqqc6EGxhUcWVJmyHr8aaH6OFSsfkw1PAthUNeD%2BQpys49rIciCM2BpkDwq0TeUARo9QeJEtZpdWpJ1nAaTARSl9H5AunqEvUHq%2BMNP%2B%2BwEAZQ2QXZ4EyKu8e8MIw78olH141AEMUOCqIj8VVGJ6FTafX7Z%2BCixi3tDdJyes4Roi%2BTHMQcSwOq4yFyFkSAW6EsFz14H2bxQiA9vjvK7VWDc6uFaC0ySwMnmO4gT%2F88nf7rsiKfdoYoYypoGrHYbqpUAkmnG6zYM0shmFaTBB8fbCzAAl8PIJ8zCW9UHX6YiOb3IcJIAtd66lyS4ItpL5RAGDUrgp66nLE9uijLelMPKxmP5rgdnR49gKMMuc2eN2PFcOcub3aYUJZp1nTAszZ4QLhEN1AAxC%2FaERORTF4ybLkeRpPz4yKjawMN6W67wGOqUBODk1XtmvZaIeZ85hnfekGBgsqWtGBt8Xy6d7zU7aA%2FdarU2rjZqr1tokh2wtc8MURa7feOdMBTX7gn%2F5ow2OQqbvxqXnSTqRNQmvHnsGrtS5IWCVlYW5oc27Jw32QhVUlW2ATULd11vCqits3CxEV9EB%2BXMcMoz8OSlU5Vny8uMJjK1%2B5qPPazwd3zS1A1zCbhBfFeRybX7oavbb2yBK1Tev3lU8&X-Amz-Signature=9f918c4cea90f4edfda92a885ad73585eeb436482080a740543278912778ff7b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663W3LDFDE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC2sbHz%2Fbx6zEJSm8ENN1uKgJB6MRlBJ97zRul7WFUTdgIgXLTdMLjSoonxBplkdZOQ2Qf6LU6msAGfwgG%2BcYKov8IqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDErZOOtRjF15GDnXfSrcA9YXaVYKySJYzJgc8HTHbmiwem0k20jm3zFuRqPTcIXeAdZbQsd%2FKysMAsO6jkt9vEnF0UbpWmLVdoZWamUJhGfk56aX1M14YBxxTULviqaiGY49INKlo%2F79goH8NDb3MiAJp5v4tQjMfMovRxZsYkvUvq1mTtb2UkzcTBeYy5oGLuKT72ZI%2BUOlSYjydM2wf40eklr65c6J94vnhY3WPwydJqqc6EGxhUcWVJmyHr8aaH6OFSsfkw1PAthUNeD%2BQpys49rIciCM2BpkDwq0TeUARo9QeJEtZpdWpJ1nAaTARSl9H5AunqEvUHq%2BMNP%2B%2BwEAZQ2QXZ4EyKu8e8MIw78olH141AEMUOCqIj8VVGJ6FTafX7Z%2BCixi3tDdJyes4Roi%2BTHMQcSwOq4yFyFkSAW6EsFz14H2bxQiA9vjvK7VWDc6uFaC0ySwMnmO4gT%2F88nf7rsiKfdoYoYypoGrHYbqpUAkmnG6zYM0shmFaTBB8fbCzAAl8PIJ8zCW9UHX6YiOb3IcJIAtd66lyS4ItpL5RAGDUrgp66nLE9uijLelMPKxmP5rgdnR49gKMMuc2eN2PFcOcub3aYUJZp1nTAszZ4QLhEN1AAxC%2FaERORTF4ybLkeRpPz4yKjawMN6W67wGOqUBODk1XtmvZaIeZ85hnfekGBgsqWtGBt8Xy6d7zU7aA%2FdarU2rjZqr1tokh2wtc8MURa7feOdMBTX7gn%2F5ow2OQqbvxqXnSTqRNQmvHnsGrtS5IWCVlYW5oc27Jw32QhVUlW2ATULd11vCqits3CxEV9EB%2BXMcMoz8OSlU5Vny8uMJjK1%2B5qPPazwd3zS1A1zCbhBfFeRybX7oavbb2yBK1Tev3lU8&X-Amz-Signature=9bf085c5b78a298c3067b9e11ac062964b27b233bc7d8466a4e220d45e16f69e&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663W3LDFDE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC2sbHz%2Fbx6zEJSm8ENN1uKgJB6MRlBJ97zRul7WFUTdgIgXLTdMLjSoonxBplkdZOQ2Qf6LU6msAGfwgG%2BcYKov8IqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDErZOOtRjF15GDnXfSrcA9YXaVYKySJYzJgc8HTHbmiwem0k20jm3zFuRqPTcIXeAdZbQsd%2FKysMAsO6jkt9vEnF0UbpWmLVdoZWamUJhGfk56aX1M14YBxxTULviqaiGY49INKlo%2F79goH8NDb3MiAJp5v4tQjMfMovRxZsYkvUvq1mTtb2UkzcTBeYy5oGLuKT72ZI%2BUOlSYjydM2wf40eklr65c6J94vnhY3WPwydJqqc6EGxhUcWVJmyHr8aaH6OFSsfkw1PAthUNeD%2BQpys49rIciCM2BpkDwq0TeUARo9QeJEtZpdWpJ1nAaTARSl9H5AunqEvUHq%2BMNP%2B%2BwEAZQ2QXZ4EyKu8e8MIw78olH141AEMUOCqIj8VVGJ6FTafX7Z%2BCixi3tDdJyes4Roi%2BTHMQcSwOq4yFyFkSAW6EsFz14H2bxQiA9vjvK7VWDc6uFaC0ySwMnmO4gT%2F88nf7rsiKfdoYoYypoGrHYbqpUAkmnG6zYM0shmFaTBB8fbCzAAl8PIJ8zCW9UHX6YiOb3IcJIAtd66lyS4ItpL5RAGDUrgp66nLE9uijLelMPKxmP5rgdnR49gKMMuc2eN2PFcOcub3aYUJZp1nTAszZ4QLhEN1AAxC%2FaERORTF4ybLkeRpPz4yKjawMN6W67wGOqUBODk1XtmvZaIeZ85hnfekGBgsqWtGBt8Xy6d7zU7aA%2FdarU2rjZqr1tokh2wtc8MURa7feOdMBTX7gn%2F5ow2OQqbvxqXnSTqRNQmvHnsGrtS5IWCVlYW5oc27Jw32QhVUlW2ATULd11vCqits3CxEV9EB%2BXMcMoz8OSlU5Vny8uMJjK1%2B5qPPazwd3zS1A1zCbhBfFeRybX7oavbb2yBK1Tev3lU8&X-Amz-Signature=19312683461bb0aefbbb440b6d5a9b64af910c5687a0058ab88417c6e42aabcd&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
