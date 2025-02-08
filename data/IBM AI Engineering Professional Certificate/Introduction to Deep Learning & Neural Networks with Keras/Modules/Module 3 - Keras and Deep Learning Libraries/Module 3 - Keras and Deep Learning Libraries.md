

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WVP26U2O%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041703Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCIEPc94JEPXRy79edoZCyIjGMbkZ8eFMw%2FE%2FjUB8%2BJ3N%2FAiBx%2BCxq%2BgOfCGbH5kUAVZa3l6O5JCyRj61raw8kKddCRCqIBAiF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMforw3nTa32gGTNaXKtwDAeFlEO0rrU4DF%2FvPc2bIqJw%2BktZJd7Qyj7kUPVUIu%2BOUZufkLFtVoBee%2BHHZ3HalY5F2pmlzfIn9Znh8dbVs3AwODRx98WsJQXhnKCiyzK5LsZMhtj288GNGOr54Oyqx7%2FDFXqloEyFqcuL%2BrjeoJHN3Stgil5s6wsaN2UFWmYtB7ZNPeapIsCp8Cuxj5X6rhDEmYjKRkx%2BCfOK34Z3P6E7yfwaFMfG4t7Yz%2Fw5i6btMNy7TpNS5HLymMIAVLyuRT9omRz1gah40P%2BcfMury7a%2FuZcfGi9nMu0ZbxGRyZKTGLhAMAqozt0xT4ZgCmPFUXR3QBICs5n4tI03pPEKs3OfGne1lVdOhUKWRJtYgJZOWJT%2FyEPumOb1UbdtTT1yXZwNO4grEEEuFI6FiEdzcGPZrgv3xfKDv9LuLnJ5mCAMtzdZECM0%2FPjohnVqX%2FQPXbfPZ5cqb83SLdFWnQUR76r1BOabbaLxES6pajtCU%2FwbLoU0ENb4DuxhXIrcGDbHRIYVT6zD5aLnFL4%2Bih061fqtBTdRrX4hnl1u2kfFtQYhCelOc7jATm0oFIPbMNh76wDuO%2B58PSPRpPoKUceWF7IwvU402mzwKJZmVHuvGI%2BgR5%2FWXD6YIcX7B6pAwlrKbvQY6pgG%2B5PGCwfE7J%2BY9fCwK%2FhEfDt6ADC5rJwZflPgLHH7WRPCGL2%2FLCGFUbW8EwioCkpX%2B0Lt5E%2Bbl6QD43rX029JMwgTSZb7gWRMlHSUlwobWEuzgzmI7n3WhEKTAZUI66k0FE2Br%2F5p8Pao%2FcPDvLbb4n5taXZf01om1v3UYe9tdsxF5XzskXKCFqcM5osNa8%2FhVFYpFPbVsZKop7Q5sQQVakVUbOFIQ&X-Amz-Signature=c2078e006faf21d852f3096eaf2dcb11c3f39f631a925219458476d22862bb7c&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WVP26U2O%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041703Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCIEPc94JEPXRy79edoZCyIjGMbkZ8eFMw%2FE%2FjUB8%2BJ3N%2FAiBx%2BCxq%2BgOfCGbH5kUAVZa3l6O5JCyRj61raw8kKddCRCqIBAiF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMforw3nTa32gGTNaXKtwDAeFlEO0rrU4DF%2FvPc2bIqJw%2BktZJd7Qyj7kUPVUIu%2BOUZufkLFtVoBee%2BHHZ3HalY5F2pmlzfIn9Znh8dbVs3AwODRx98WsJQXhnKCiyzK5LsZMhtj288GNGOr54Oyqx7%2FDFXqloEyFqcuL%2BrjeoJHN3Stgil5s6wsaN2UFWmYtB7ZNPeapIsCp8Cuxj5X6rhDEmYjKRkx%2BCfOK34Z3P6E7yfwaFMfG4t7Yz%2Fw5i6btMNy7TpNS5HLymMIAVLyuRT9omRz1gah40P%2BcfMury7a%2FuZcfGi9nMu0ZbxGRyZKTGLhAMAqozt0xT4ZgCmPFUXR3QBICs5n4tI03pPEKs3OfGne1lVdOhUKWRJtYgJZOWJT%2FyEPumOb1UbdtTT1yXZwNO4grEEEuFI6FiEdzcGPZrgv3xfKDv9LuLnJ5mCAMtzdZECM0%2FPjohnVqX%2FQPXbfPZ5cqb83SLdFWnQUR76r1BOabbaLxES6pajtCU%2FwbLoU0ENb4DuxhXIrcGDbHRIYVT6zD5aLnFL4%2Bih061fqtBTdRrX4hnl1u2kfFtQYhCelOc7jATm0oFIPbMNh76wDuO%2B58PSPRpPoKUceWF7IwvU402mzwKJZmVHuvGI%2BgR5%2FWXD6YIcX7B6pAwlrKbvQY6pgG%2B5PGCwfE7J%2BY9fCwK%2FhEfDt6ADC5rJwZflPgLHH7WRPCGL2%2FLCGFUbW8EwioCkpX%2B0Lt5E%2Bbl6QD43rX029JMwgTSZb7gWRMlHSUlwobWEuzgzmI7n3WhEKTAZUI66k0FE2Br%2F5p8Pao%2FcPDvLbb4n5taXZf01om1v3UYe9tdsxF5XzskXKCFqcM5osNa8%2FhVFYpFPbVsZKop7Q5sQQVakVUbOFIQ&X-Amz-Signature=a7ed1ef5f409abe3147c11755e853a9fd29ccc3c667cb8466451ce24e4939b36&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WVP26U2O%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041703Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCIEPc94JEPXRy79edoZCyIjGMbkZ8eFMw%2FE%2FjUB8%2BJ3N%2FAiBx%2BCxq%2BgOfCGbH5kUAVZa3l6O5JCyRj61raw8kKddCRCqIBAiF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMforw3nTa32gGTNaXKtwDAeFlEO0rrU4DF%2FvPc2bIqJw%2BktZJd7Qyj7kUPVUIu%2BOUZufkLFtVoBee%2BHHZ3HalY5F2pmlzfIn9Znh8dbVs3AwODRx98WsJQXhnKCiyzK5LsZMhtj288GNGOr54Oyqx7%2FDFXqloEyFqcuL%2BrjeoJHN3Stgil5s6wsaN2UFWmYtB7ZNPeapIsCp8Cuxj5X6rhDEmYjKRkx%2BCfOK34Z3P6E7yfwaFMfG4t7Yz%2Fw5i6btMNy7TpNS5HLymMIAVLyuRT9omRz1gah40P%2BcfMury7a%2FuZcfGi9nMu0ZbxGRyZKTGLhAMAqozt0xT4ZgCmPFUXR3QBICs5n4tI03pPEKs3OfGne1lVdOhUKWRJtYgJZOWJT%2FyEPumOb1UbdtTT1yXZwNO4grEEEuFI6FiEdzcGPZrgv3xfKDv9LuLnJ5mCAMtzdZECM0%2FPjohnVqX%2FQPXbfPZ5cqb83SLdFWnQUR76r1BOabbaLxES6pajtCU%2FwbLoU0ENb4DuxhXIrcGDbHRIYVT6zD5aLnFL4%2Bih061fqtBTdRrX4hnl1u2kfFtQYhCelOc7jATm0oFIPbMNh76wDuO%2B58PSPRpPoKUceWF7IwvU402mzwKJZmVHuvGI%2BgR5%2FWXD6YIcX7B6pAwlrKbvQY6pgG%2B5PGCwfE7J%2BY9fCwK%2FhEfDt6ADC5rJwZflPgLHH7WRPCGL2%2FLCGFUbW8EwioCkpX%2B0Lt5E%2Bbl6QD43rX029JMwgTSZb7gWRMlHSUlwobWEuzgzmI7n3WhEKTAZUI66k0FE2Br%2F5p8Pao%2FcPDvLbb4n5taXZf01om1v3UYe9tdsxF5XzskXKCFqcM5osNa8%2FhVFYpFPbVsZKop7Q5sQQVakVUbOFIQ&X-Amz-Signature=dc3b503c5736e341b65dccd0f35ca10d49b38d7d366e5d4108d73b7bd360ccaa&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VTQQGHHJ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041704Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIFKudvAuOitp25ZY7EomMEfwTjQib%2Fba1S8Vb73sizjBAiEA1eJuq%2FEty2hW3U0Pf4WtZOVeYZLiSLG9Lb4i1%2FkfQdAqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCnMIHZ%2FxCwiwPiYNyrcA1ZzqwStJi6Sbrt7Zt6BhQg8xho5l0DziRl7pDg5%2BzPORC%2FilYmLTYeJqk2UNy8pIST45hbDe2Ea5KVLWHsUIHsygvXV3sKG1YPVda%2FstAuKnjOlzsONTgVJW%2Fm1JhMiuVzIhvrgRiWSVo9HOzXYlYU41h0exCWxg00HJLDRh%2F6%2FpoRLasj3Bcptg5%2BODhcbc03zoWdSdZUW0HvVqeqyM8RqdiQZUR8GUf1Oia4VcaTkY813mcAN0gouRhTwNNY6w4RP%2F%2BlAUkSo5wlWJe9ef4l0i6zIxWLjRn6rUvhoyq1oGBDE4VPuoktTXzWXZIKRqTh%2Fq7J%2FZW2HMSoEc%2FYJBT21QSpEYH3hnaRi5AQIcKa58tl86PmxUfmACNcIqsUvCBNCkiXl%2FXDT6OgIoUaea0b%2FpxZMAR57vBECrTtrt3MuyjKf1msdYc3%2FzdSFhOHPCs5cXt3dHxpEuJex4KCnTsB4e2SYAc88JsyQ14Ph91Dovv29ZdJE%2FUhqrySYfXzYq3VqhWCn8TG%2BchQnoDKHN8GaMo%2BrgoSmwcTM7dA6NQ6IWfsaq9I3%2F8Id%2BRudQja48%2FN%2FANM5ywLPpzTLo2q7PrGkCqkYE%2BeM92ATAmeK7mt5JQBb4KiHguCYIaFzMNuym70GOqUBmKhJ%2Bgs7w8tZ8N9oW3PZ8%2FqW7SRJnsNUrQgcvzPC%2BPiM%2FEpCELHaO8tVZb9Kw%2FJQV9pZ1FJo5z9PIwdMjMc0Oq6j3vX9ZszwqFLSHxA%2FtIdZqSnH8sUxy74ums707%2Bt%2BodQAW7YfPT2o0ZXfhqRUhaue9Pp9YphMwApO7bbM%2FWF3Y%2F0eRo5iL%2FJ7pZK9IAPfKDOgi7fEcIqpyqlxDf3F4X4DNDZG&X-Amz-Signature=f83ba53677ecd114d3f5887ca6d6dbb1d4953fee55410bc6edae466338a81b69&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMFSIFKP%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041704Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCIF5MnaVoreYOBem3QLzv0m2LN%2BUCghIyRu3nujeuu7tMAiBWWxaF5curG1od8oarRZpC59voRBD0c5tGALln788qGyqIBAiF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMdRecnLFl49vHrqj8KtwDNhufOR18mBxWR2LzTZERCZN%2BhDFE3Vs%2FJTalYkaT2uRM6QFCVUqFlfNRvs5Ae%2FBYTfV%2BZhGJ%2B1cV2hHOVoL3v7nuI6A1Zq1E5SNpnHLtNQ88da2XGQSiRs7LrvViBQ%2BbgLDT5YDcXW9Vgog6jeiMxYcTNX5aEXQOFsk5tHfPN9akkYLLToge6MXyIVN7aAtLcXS6vu3kTs0DZDHLGuLG1Obma6rRsR7rzsOA0EcEgX2soN%2B21Zsj14hGawViAVuRXwD1L5HNjmzRCpGk0K4kU43hcS6OxMBW7FyxDzBPSUr%2FmUrD2jfGuTTiaVZGjbek5rupeOuQgdkrRcoOtdb5Q%2BRmaqJM79UojEnLmkjvwQX7LaZZvkxpuPl1y5l35XX8IJj9SI70HOQW94%2BQELaQi974v24ToN8nNAk6mrfOJjqzM%2BvFb6riQ3%2BSfqwP9dfJ1pBT%2FSJtQfeogaH%2BluhCbRe8S5gOUhZNfgIJda%2BhG9X5XDKXmhUllGWh4bVUrESaoJkcWXwin3r5sy2lzjVQa4DMai1cDEzSEWrwikbG6iEmKozPmhHkNlVENyyQkzex4idJnipmKuUZ4OGaBYK47KLkjzY61EuA%2Bw%2BKAuLDzL1Lj0gpSV%2FTmIpbaY8w3bKbvQY6pgHCHkBTupouHJkPmtDIzjxoU9Qi3kAuNztMcvRk%2F%2FQbB%2FClA0njJZX%2FkhGlqV2cHiMOJ%2F7nspJS2Q15wFbRi4NNXt%2BLhDTW9KZrmQ%2BetjPj3jWXrLeui8Z%2F1W3eF5lSQhqgRKhmvDugHGxX0ccywA1J4lvKTipYOX4o%2BtxR3AmZ2lT8VJZLyTdnx0%2BfOi6fjsyY1Ibs3ZPKeL0lBJQ%2BrvQaJu4SE85G&X-Amz-Signature=6e9b3df6bea79c9884db04a4e10b727a456ea8a840426fd3ded0060dffa01c10&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WVP26U2O%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041703Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCIEPc94JEPXRy79edoZCyIjGMbkZ8eFMw%2FE%2FjUB8%2BJ3N%2FAiBx%2BCxq%2BgOfCGbH5kUAVZa3l6O5JCyRj61raw8kKddCRCqIBAiF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMforw3nTa32gGTNaXKtwDAeFlEO0rrU4DF%2FvPc2bIqJw%2BktZJd7Qyj7kUPVUIu%2BOUZufkLFtVoBee%2BHHZ3HalY5F2pmlzfIn9Znh8dbVs3AwODRx98WsJQXhnKCiyzK5LsZMhtj288GNGOr54Oyqx7%2FDFXqloEyFqcuL%2BrjeoJHN3Stgil5s6wsaN2UFWmYtB7ZNPeapIsCp8Cuxj5X6rhDEmYjKRkx%2BCfOK34Z3P6E7yfwaFMfG4t7Yz%2Fw5i6btMNy7TpNS5HLymMIAVLyuRT9omRz1gah40P%2BcfMury7a%2FuZcfGi9nMu0ZbxGRyZKTGLhAMAqozt0xT4ZgCmPFUXR3QBICs5n4tI03pPEKs3OfGne1lVdOhUKWRJtYgJZOWJT%2FyEPumOb1UbdtTT1yXZwNO4grEEEuFI6FiEdzcGPZrgv3xfKDv9LuLnJ5mCAMtzdZECM0%2FPjohnVqX%2FQPXbfPZ5cqb83SLdFWnQUR76r1BOabbaLxES6pajtCU%2FwbLoU0ENb4DuxhXIrcGDbHRIYVT6zD5aLnFL4%2Bih061fqtBTdRrX4hnl1u2kfFtQYhCelOc7jATm0oFIPbMNh76wDuO%2B58PSPRpPoKUceWF7IwvU402mzwKJZmVHuvGI%2BgR5%2FWXD6YIcX7B6pAwlrKbvQY6pgG%2B5PGCwfE7J%2BY9fCwK%2FhEfDt6ADC5rJwZflPgLHH7WRPCGL2%2FLCGFUbW8EwioCkpX%2B0Lt5E%2Bbl6QD43rX029JMwgTSZb7gWRMlHSUlwobWEuzgzmI7n3WhEKTAZUI66k0FE2Br%2F5p8Pao%2FcPDvLbb4n5taXZf01om1v3UYe9tdsxF5XzskXKCFqcM5osNa8%2FhVFYpFPbVsZKop7Q5sQQVakVUbOFIQ&X-Amz-Signature=25cc37279862b6b44b278fa02d9f42b00d29b2d545c72b7b295f4dfec93ec883&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WVP26U2O%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041703Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCIEPc94JEPXRy79edoZCyIjGMbkZ8eFMw%2FE%2FjUB8%2BJ3N%2FAiBx%2BCxq%2BgOfCGbH5kUAVZa3l6O5JCyRj61raw8kKddCRCqIBAiF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMforw3nTa32gGTNaXKtwDAeFlEO0rrU4DF%2FvPc2bIqJw%2BktZJd7Qyj7kUPVUIu%2BOUZufkLFtVoBee%2BHHZ3HalY5F2pmlzfIn9Znh8dbVs3AwODRx98WsJQXhnKCiyzK5LsZMhtj288GNGOr54Oyqx7%2FDFXqloEyFqcuL%2BrjeoJHN3Stgil5s6wsaN2UFWmYtB7ZNPeapIsCp8Cuxj5X6rhDEmYjKRkx%2BCfOK34Z3P6E7yfwaFMfG4t7Yz%2Fw5i6btMNy7TpNS5HLymMIAVLyuRT9omRz1gah40P%2BcfMury7a%2FuZcfGi9nMu0ZbxGRyZKTGLhAMAqozt0xT4ZgCmPFUXR3QBICs5n4tI03pPEKs3OfGne1lVdOhUKWRJtYgJZOWJT%2FyEPumOb1UbdtTT1yXZwNO4grEEEuFI6FiEdzcGPZrgv3xfKDv9LuLnJ5mCAMtzdZECM0%2FPjohnVqX%2FQPXbfPZ5cqb83SLdFWnQUR76r1BOabbaLxES6pajtCU%2FwbLoU0ENb4DuxhXIrcGDbHRIYVT6zD5aLnFL4%2Bih061fqtBTdRrX4hnl1u2kfFtQYhCelOc7jATm0oFIPbMNh76wDuO%2B58PSPRpPoKUceWF7IwvU402mzwKJZmVHuvGI%2BgR5%2FWXD6YIcX7B6pAwlrKbvQY6pgG%2B5PGCwfE7J%2BY9fCwK%2FhEfDt6ADC5rJwZflPgLHH7WRPCGL2%2FLCGFUbW8EwioCkpX%2B0Lt5E%2Bbl6QD43rX029JMwgTSZb7gWRMlHSUlwobWEuzgzmI7n3WhEKTAZUI66k0FE2Br%2F5p8Pao%2FcPDvLbb4n5taXZf01om1v3UYe9tdsxF5XzskXKCFqcM5osNa8%2FhVFYpFPbVsZKop7Q5sQQVakVUbOFIQ&X-Amz-Signature=1e7fc322cf03729c456c50d48e8c057d2876eaab284873b09d78e73d4248a68e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WVP26U2O%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041703Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCIEPc94JEPXRy79edoZCyIjGMbkZ8eFMw%2FE%2FjUB8%2BJ3N%2FAiBx%2BCxq%2BgOfCGbH5kUAVZa3l6O5JCyRj61raw8kKddCRCqIBAiF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMforw3nTa32gGTNaXKtwDAeFlEO0rrU4DF%2FvPc2bIqJw%2BktZJd7Qyj7kUPVUIu%2BOUZufkLFtVoBee%2BHHZ3HalY5F2pmlzfIn9Znh8dbVs3AwODRx98WsJQXhnKCiyzK5LsZMhtj288GNGOr54Oyqx7%2FDFXqloEyFqcuL%2BrjeoJHN3Stgil5s6wsaN2UFWmYtB7ZNPeapIsCp8Cuxj5X6rhDEmYjKRkx%2BCfOK34Z3P6E7yfwaFMfG4t7Yz%2Fw5i6btMNy7TpNS5HLymMIAVLyuRT9omRz1gah40P%2BcfMury7a%2FuZcfGi9nMu0ZbxGRyZKTGLhAMAqozt0xT4ZgCmPFUXR3QBICs5n4tI03pPEKs3OfGne1lVdOhUKWRJtYgJZOWJT%2FyEPumOb1UbdtTT1yXZwNO4grEEEuFI6FiEdzcGPZrgv3xfKDv9LuLnJ5mCAMtzdZECM0%2FPjohnVqX%2FQPXbfPZ5cqb83SLdFWnQUR76r1BOabbaLxES6pajtCU%2FwbLoU0ENb4DuxhXIrcGDbHRIYVT6zD5aLnFL4%2Bih061fqtBTdRrX4hnl1u2kfFtQYhCelOc7jATm0oFIPbMNh76wDuO%2B58PSPRpPoKUceWF7IwvU402mzwKJZmVHuvGI%2BgR5%2FWXD6YIcX7B6pAwlrKbvQY6pgG%2B5PGCwfE7J%2BY9fCwK%2FhEfDt6ADC5rJwZflPgLHH7WRPCGL2%2FLCGFUbW8EwioCkpX%2B0Lt5E%2Bbl6QD43rX029JMwgTSZb7gWRMlHSUlwobWEuzgzmI7n3WhEKTAZUI66k0FE2Br%2F5p8Pao%2FcPDvLbb4n5taXZf01om1v3UYe9tdsxF5XzskXKCFqcM5osNa8%2FhVFYpFPbVsZKop7Q5sQQVakVUbOFIQ&X-Amz-Signature=42eb9fcb44b303846f7ca658643f6b719b0aff91543e70fc798d48cabd09df3c&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WVP26U2O%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041703Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCIEPc94JEPXRy79edoZCyIjGMbkZ8eFMw%2FE%2FjUB8%2BJ3N%2FAiBx%2BCxq%2BgOfCGbH5kUAVZa3l6O5JCyRj61raw8kKddCRCqIBAiF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMforw3nTa32gGTNaXKtwDAeFlEO0rrU4DF%2FvPc2bIqJw%2BktZJd7Qyj7kUPVUIu%2BOUZufkLFtVoBee%2BHHZ3HalY5F2pmlzfIn9Znh8dbVs3AwODRx98WsJQXhnKCiyzK5LsZMhtj288GNGOr54Oyqx7%2FDFXqloEyFqcuL%2BrjeoJHN3Stgil5s6wsaN2UFWmYtB7ZNPeapIsCp8Cuxj5X6rhDEmYjKRkx%2BCfOK34Z3P6E7yfwaFMfG4t7Yz%2Fw5i6btMNy7TpNS5HLymMIAVLyuRT9omRz1gah40P%2BcfMury7a%2FuZcfGi9nMu0ZbxGRyZKTGLhAMAqozt0xT4ZgCmPFUXR3QBICs5n4tI03pPEKs3OfGne1lVdOhUKWRJtYgJZOWJT%2FyEPumOb1UbdtTT1yXZwNO4grEEEuFI6FiEdzcGPZrgv3xfKDv9LuLnJ5mCAMtzdZECM0%2FPjohnVqX%2FQPXbfPZ5cqb83SLdFWnQUR76r1BOabbaLxES6pajtCU%2FwbLoU0ENb4DuxhXIrcGDbHRIYVT6zD5aLnFL4%2Bih061fqtBTdRrX4hnl1u2kfFtQYhCelOc7jATm0oFIPbMNh76wDuO%2B58PSPRpPoKUceWF7IwvU402mzwKJZmVHuvGI%2BgR5%2FWXD6YIcX7B6pAwlrKbvQY6pgG%2B5PGCwfE7J%2BY9fCwK%2FhEfDt6ADC5rJwZflPgLHH7WRPCGL2%2FLCGFUbW8EwioCkpX%2B0Lt5E%2Bbl6QD43rX029JMwgTSZb7gWRMlHSUlwobWEuzgzmI7n3WhEKTAZUI66k0FE2Br%2F5p8Pao%2FcPDvLbb4n5taXZf01om1v3UYe9tdsxF5XzskXKCFqcM5osNa8%2FhVFYpFPbVsZKop7Q5sQQVakVUbOFIQ&X-Amz-Signature=f148d2161ffe0a1e3e751cbb8755f6245badb4478a91fa7e71eaf3426730f501&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
