

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQPERYRG%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081757Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJFMEMCH2kGMZK4J58ioOtwPExplc8irgIDzHJDQ8ySQQo%2BMp4CICMgda5QSraNeaZcE6%2FMTQd1hG0RSnVsxzZM4cxQ1QKjKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz0tAnzt%2FYncYxZMjQq3AP418ZG1pIesTGtj1lFMiZb%2F4DCFd1jzoODfW4oxw9MBtqFUiRjOIUoknRkXMqlmQESbsh35QF4UiWoXcAw%2F%2FytBJrgXhY0%2BbwSEvuxNafivK0fSMW0JLycQpJ2JUgtX3GweaR9mJeMsc92okbxY8LJP%2Bf2yYm5ip6909r%2BhhfWUJt4mfvv8bE7TmWMF7%2BktdA5uzlxVJ6LLiw%2Fv351D6DaNMJBUU2L9wod2krOqmU870KfP2fo8mzYy8k5ANEZruhltFssDwofbU4Azh4f0wCufe8Wx%2FbCkX6cxdHcUxnEItOK8by70kyirlH1IxSnvNR3abZxe9JLS2Fn%2BQ5Gh%2BbvXOIQ8h7pGNCcGzUHN3uk8h3R8igX3LZwxZ%2FAFObBq4Jmb8RFt1XLBu7RpM7hQHpWgoZg%2Fvm6Nv27D6xd4t8xmBkzPv5mTLLwENfQhrQW6Fzljmlv35ig1uZ76xG8xVk0bu30q%2BQtCfpMDN8E6ZfkPddckefpiTge5HUZnjrAuuGnwCC5RQN7RglhBMOQAeNn14BnXhBMz8wyx6otYoJj%2BJy6EMAibFYu28c7yYtM%2BbSHwFF9MR1ybmf3xRbOtlbr91ztAKu%2FziceIl%2BgPNENu3F6WzWBh0dsGyhCWjDPjpy9BjqnAdLi2tJgifwOlt%2BdcqfS42QpvNa8lhqv5%2BL1eMW2y4mhCsuB5wV%2BsI9NNPAK67sC7GeIS0%2B5BeecVC9eIr94Cn5yvXHQYBgyzxQCUzHJpPOIi8oRiqlSBoMfujbjjNRGnq4iFVF1JlMzhjVMFlq%2BqQgq5xa%2BCqyI8SwTMpIuUtd%2BWDFUNJA9J2bttWq7bTndWzC6pFMHjLtQTDxouLgyZJwj82BOjSbd&X-Amz-Signature=e41399bcf2cc9f09a26b837a9052b2f7a51f36b26c68230645386e8191b1608d&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQPERYRG%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081757Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJFMEMCH2kGMZK4J58ioOtwPExplc8irgIDzHJDQ8ySQQo%2BMp4CICMgda5QSraNeaZcE6%2FMTQd1hG0RSnVsxzZM4cxQ1QKjKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz0tAnzt%2FYncYxZMjQq3AP418ZG1pIesTGtj1lFMiZb%2F4DCFd1jzoODfW4oxw9MBtqFUiRjOIUoknRkXMqlmQESbsh35QF4UiWoXcAw%2F%2FytBJrgXhY0%2BbwSEvuxNafivK0fSMW0JLycQpJ2JUgtX3GweaR9mJeMsc92okbxY8LJP%2Bf2yYm5ip6909r%2BhhfWUJt4mfvv8bE7TmWMF7%2BktdA5uzlxVJ6LLiw%2Fv351D6DaNMJBUU2L9wod2krOqmU870KfP2fo8mzYy8k5ANEZruhltFssDwofbU4Azh4f0wCufe8Wx%2FbCkX6cxdHcUxnEItOK8by70kyirlH1IxSnvNR3abZxe9JLS2Fn%2BQ5Gh%2BbvXOIQ8h7pGNCcGzUHN3uk8h3R8igX3LZwxZ%2FAFObBq4Jmb8RFt1XLBu7RpM7hQHpWgoZg%2Fvm6Nv27D6xd4t8xmBkzPv5mTLLwENfQhrQW6Fzljmlv35ig1uZ76xG8xVk0bu30q%2BQtCfpMDN8E6ZfkPddckefpiTge5HUZnjrAuuGnwCC5RQN7RglhBMOQAeNn14BnXhBMz8wyx6otYoJj%2BJy6EMAibFYu28c7yYtM%2BbSHwFF9MR1ybmf3xRbOtlbr91ztAKu%2FziceIl%2BgPNENu3F6WzWBh0dsGyhCWjDPjpy9BjqnAdLi2tJgifwOlt%2BdcqfS42QpvNa8lhqv5%2BL1eMW2y4mhCsuB5wV%2BsI9NNPAK67sC7GeIS0%2B5BeecVC9eIr94Cn5yvXHQYBgyzxQCUzHJpPOIi8oRiqlSBoMfujbjjNRGnq4iFVF1JlMzhjVMFlq%2BqQgq5xa%2BCqyI8SwTMpIuUtd%2BWDFUNJA9J2bttWq7bTndWzC6pFMHjLtQTDxouLgyZJwj82BOjSbd&X-Amz-Signature=7be04dc169d94681d3bf5acba934effa0c366c8f81aff3d9543393bd4e4266a0&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQPERYRG%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081757Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJFMEMCH2kGMZK4J58ioOtwPExplc8irgIDzHJDQ8ySQQo%2BMp4CICMgda5QSraNeaZcE6%2FMTQd1hG0RSnVsxzZM4cxQ1QKjKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz0tAnzt%2FYncYxZMjQq3AP418ZG1pIesTGtj1lFMiZb%2F4DCFd1jzoODfW4oxw9MBtqFUiRjOIUoknRkXMqlmQESbsh35QF4UiWoXcAw%2F%2FytBJrgXhY0%2BbwSEvuxNafivK0fSMW0JLycQpJ2JUgtX3GweaR9mJeMsc92okbxY8LJP%2Bf2yYm5ip6909r%2BhhfWUJt4mfvv8bE7TmWMF7%2BktdA5uzlxVJ6LLiw%2Fv351D6DaNMJBUU2L9wod2krOqmU870KfP2fo8mzYy8k5ANEZruhltFssDwofbU4Azh4f0wCufe8Wx%2FbCkX6cxdHcUxnEItOK8by70kyirlH1IxSnvNR3abZxe9JLS2Fn%2BQ5Gh%2BbvXOIQ8h7pGNCcGzUHN3uk8h3R8igX3LZwxZ%2FAFObBq4Jmb8RFt1XLBu7RpM7hQHpWgoZg%2Fvm6Nv27D6xd4t8xmBkzPv5mTLLwENfQhrQW6Fzljmlv35ig1uZ76xG8xVk0bu30q%2BQtCfpMDN8E6ZfkPddckefpiTge5HUZnjrAuuGnwCC5RQN7RglhBMOQAeNn14BnXhBMz8wyx6otYoJj%2BJy6EMAibFYu28c7yYtM%2BbSHwFF9MR1ybmf3xRbOtlbr91ztAKu%2FziceIl%2BgPNENu3F6WzWBh0dsGyhCWjDPjpy9BjqnAdLi2tJgifwOlt%2BdcqfS42QpvNa8lhqv5%2BL1eMW2y4mhCsuB5wV%2BsI9NNPAK67sC7GeIS0%2B5BeecVC9eIr94Cn5yvXHQYBgyzxQCUzHJpPOIi8oRiqlSBoMfujbjjNRGnq4iFVF1JlMzhjVMFlq%2BqQgq5xa%2BCqyI8SwTMpIuUtd%2BWDFUNJA9J2bttWq7bTndWzC6pFMHjLtQTDxouLgyZJwj82BOjSbd&X-Amz-Signature=999222d0445b3d008c17d7e7f75d4a04388dd286039eddcb3518987c79a49b06&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RRNSM5UI%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081758Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIHzzDV6iPCc%2FZ63SZscfMv1u27zipg9leRfI3Q8bMwLEAiEAnzBRPVVZ0amKSoFkNlqzkk3JcjlFwc%2F%2FVGKIEdf3KfUqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGaG3hq%2BjkXvp%2FSGvyrcA7bkjp%2FcLG%2BrjAKrPZEnTDz1ZIS5k%2FC28uu9lO%2BpNY8EkttHPINTZKKnRBEikP7AYP6oTn%2FvenEaWKZ6VlyJwurbbprrM33wrhSn10xxQqEdY8DK7xEggwBX1i1CXzoNMtmzBLXaT8qLpGqkLd66yIjn%2FIWNrY0Os37ksqXG0c5engGj7hPk6LaUo56ZuVs0RdZ457q93GGIx6QONBYrQhWakJPWDYZGWziNtbGrQYOkjR%2Bk1GMLjXKG6Qrfet92qdKuthP1sbTPRfa0sXyYs7QdeRyWtxvVa9GtX3RenFPS%2FeXY4%2FZAoi2AvL%2FqU%2BegkLMR5uUxByBh9tKy%2FV6oX3KF2TONIqdpZ38D9e0xJWd21RnLLvg9RUidqW8G6GIc9lkDgoNTqZNvz%2FZRj0GJoAg01tRIvbjkR%2FN0bbf%2BSHn6gDh%2BrP1sNB%2B%2BoP5QP9H08hqnnq46XQFgXHjMhjPRGB75bKq5lYUbG3XLO0CnD9isztNto9EDWMnZpQsceHCKqHY%2B5pA%2FUAQTNyDq2WkyiC21U3cMFEERVbsB%2BGzHTlC5LmuxXVR8a1bdBs%2BZI1muTPoJwwBZ7wkCFcnyv8ojz0fg7IcUc4rUKVMSask9vrZ4SMeWVXeNgvpvTdWvMIqOnL0GOqUBnxxSLPAKv4abAzJ6FX2ric1zi8Yt1sYk%2BpgiU8PqjGQ2lEuO1ZGYLbvljq2Pxo0U9zHBtl%2BxssL4ZTq1iD9WohwOLvHkGHfgvOu9CF9XBBITRPLL5Qj29RpoWfq5Uy4XhUoYkysChi1ncDh962btPbLwa4sR8x8BRaaYsVBZojP3tEq4Wx3k6GQvX%2Bno4hTMdYpRoN7Gx7QPSmEtF%2BOZM4sF5Xur&X-Amz-Signature=edb339e6e8472395f24419b06225f25cf5045d8408eec903497100e5657e8c0b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662QRRML6%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081758Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJIMEYCIQD3pmgcyZ9CcDXpPQolRLkV8%2FHX%2BCrEwYPCyTs0KG8J%2FAIhANHmtT4DkQYLEOjlVQrnqXup%2BFDM7hzvEhvmO%2BM6pwGCKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwD4%2FBKlfYsvHM5wR4q3AP2lD7mMPW%2BVe1dsWdF1ehsVRwcQJBT2ivjKZGSI89eKv2jRSOoEdyeKcaqz%2FWkbl37R4gjWC32GYOT61G3dBMDrlIP59tvPQ3pEaqIYjajf2aEH0Av6mnmWY%2FElCoKx4HdP9hZa9i3VLYm6xvKe9MdM6pWO8EU47BPVzxHD6ArXb8aslrG4vJbjZQPJaCr8I0B5qhQV2VaVIYtRIkFD92Br4DeQ4FzKkW5h%2FtWlUIArc%2FzF84vtW7P6mxA4YPpgHFGX287NdjjHAeQgqqhONANewMBy2FaQNNTPdINNSqBY9FKcNlGfUkVS8y2Gxq7ne2fDUv83KCdnWLmk2qNIPC1bYNn3SLl2l61%2FaWscAI6QkP8vG15KaHajes3vs8HSjMztsGE5VjSuwS%2FjdVKqC7xoQTIgW%2BLsEpLMnXe7Ma5Kna33WnwBluFcL%2F4jlxGETOW8G%2FlETk9TDtUHbGUQnOIRfv1wP5ywp7DR%2Bx7ouCyud6rFoF4PXtqdB%2BcK5AXLYHMjeWzuo%2BJAtQoG6h62LDhYWEXbwQMebNNN4GmtEecGXoSa%2FIY7Od646RVKSmqZbZWFysjD77dLwnDfdd9uJrsgncwr2SMwfL1IPqbXnSDHeKfT1WmvwkC%2BPu42zDOjpy9BjqkAdYVgySByJgBDvaKX2QS53VBSLB3CtsT7%2BPfPQB%2FL3mZc37%2BeD2CyR8NJyD79ns3c%2BMbxcCyMIlsOiU9zcz%2BTtVscGcINjD0oT79gtTwG0Gl8MZ%2Bh%2B%2FH3NHadVCZHvsCBV1BicHKw2lwttWVSlZz8wkidVkjZv3Y6DijOOMkTEVw%2FgTTuAmHyWDB5QZoyP7BEIz54PNjjZhLlONgVHqEOmaUc9eR&X-Amz-Signature=93d7bafea9a8073389268af10f4f06fd8d0cb691fc3c82a535ac49cc7c3259b3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQPERYRG%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081757Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJFMEMCH2kGMZK4J58ioOtwPExplc8irgIDzHJDQ8ySQQo%2BMp4CICMgda5QSraNeaZcE6%2FMTQd1hG0RSnVsxzZM4cxQ1QKjKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz0tAnzt%2FYncYxZMjQq3AP418ZG1pIesTGtj1lFMiZb%2F4DCFd1jzoODfW4oxw9MBtqFUiRjOIUoknRkXMqlmQESbsh35QF4UiWoXcAw%2F%2FytBJrgXhY0%2BbwSEvuxNafivK0fSMW0JLycQpJ2JUgtX3GweaR9mJeMsc92okbxY8LJP%2Bf2yYm5ip6909r%2BhhfWUJt4mfvv8bE7TmWMF7%2BktdA5uzlxVJ6LLiw%2Fv351D6DaNMJBUU2L9wod2krOqmU870KfP2fo8mzYy8k5ANEZruhltFssDwofbU4Azh4f0wCufe8Wx%2FbCkX6cxdHcUxnEItOK8by70kyirlH1IxSnvNR3abZxe9JLS2Fn%2BQ5Gh%2BbvXOIQ8h7pGNCcGzUHN3uk8h3R8igX3LZwxZ%2FAFObBq4Jmb8RFt1XLBu7RpM7hQHpWgoZg%2Fvm6Nv27D6xd4t8xmBkzPv5mTLLwENfQhrQW6Fzljmlv35ig1uZ76xG8xVk0bu30q%2BQtCfpMDN8E6ZfkPddckefpiTge5HUZnjrAuuGnwCC5RQN7RglhBMOQAeNn14BnXhBMz8wyx6otYoJj%2BJy6EMAibFYu28c7yYtM%2BbSHwFF9MR1ybmf3xRbOtlbr91ztAKu%2FziceIl%2BgPNENu3F6WzWBh0dsGyhCWjDPjpy9BjqnAdLi2tJgifwOlt%2BdcqfS42QpvNa8lhqv5%2BL1eMW2y4mhCsuB5wV%2BsI9NNPAK67sC7GeIS0%2B5BeecVC9eIr94Cn5yvXHQYBgyzxQCUzHJpPOIi8oRiqlSBoMfujbjjNRGnq4iFVF1JlMzhjVMFlq%2BqQgq5xa%2BCqyI8SwTMpIuUtd%2BWDFUNJA9J2bttWq7bTndWzC6pFMHjLtQTDxouLgyZJwj82BOjSbd&X-Amz-Signature=41da161203d83d41372afd1c9bb6e6b489577d5211275c45d5c23f2310beec55&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQPERYRG%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081757Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJFMEMCH2kGMZK4J58ioOtwPExplc8irgIDzHJDQ8ySQQo%2BMp4CICMgda5QSraNeaZcE6%2FMTQd1hG0RSnVsxzZM4cxQ1QKjKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz0tAnzt%2FYncYxZMjQq3AP418ZG1pIesTGtj1lFMiZb%2F4DCFd1jzoODfW4oxw9MBtqFUiRjOIUoknRkXMqlmQESbsh35QF4UiWoXcAw%2F%2FytBJrgXhY0%2BbwSEvuxNafivK0fSMW0JLycQpJ2JUgtX3GweaR9mJeMsc92okbxY8LJP%2Bf2yYm5ip6909r%2BhhfWUJt4mfvv8bE7TmWMF7%2BktdA5uzlxVJ6LLiw%2Fv351D6DaNMJBUU2L9wod2krOqmU870KfP2fo8mzYy8k5ANEZruhltFssDwofbU4Azh4f0wCufe8Wx%2FbCkX6cxdHcUxnEItOK8by70kyirlH1IxSnvNR3abZxe9JLS2Fn%2BQ5Gh%2BbvXOIQ8h7pGNCcGzUHN3uk8h3R8igX3LZwxZ%2FAFObBq4Jmb8RFt1XLBu7RpM7hQHpWgoZg%2Fvm6Nv27D6xd4t8xmBkzPv5mTLLwENfQhrQW6Fzljmlv35ig1uZ76xG8xVk0bu30q%2BQtCfpMDN8E6ZfkPddckefpiTge5HUZnjrAuuGnwCC5RQN7RglhBMOQAeNn14BnXhBMz8wyx6otYoJj%2BJy6EMAibFYu28c7yYtM%2BbSHwFF9MR1ybmf3xRbOtlbr91ztAKu%2FziceIl%2BgPNENu3F6WzWBh0dsGyhCWjDPjpy9BjqnAdLi2tJgifwOlt%2BdcqfS42QpvNa8lhqv5%2BL1eMW2y4mhCsuB5wV%2BsI9NNPAK67sC7GeIS0%2B5BeecVC9eIr94Cn5yvXHQYBgyzxQCUzHJpPOIi8oRiqlSBoMfujbjjNRGnq4iFVF1JlMzhjVMFlq%2BqQgq5xa%2BCqyI8SwTMpIuUtd%2BWDFUNJA9J2bttWq7bTndWzC6pFMHjLtQTDxouLgyZJwj82BOjSbd&X-Amz-Signature=e60cc75fc58c3e64ccc9e2c078f2da09112aa81b6f735d483405bec1201ae457&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQPERYRG%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081757Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJFMEMCH2kGMZK4J58ioOtwPExplc8irgIDzHJDQ8ySQQo%2BMp4CICMgda5QSraNeaZcE6%2FMTQd1hG0RSnVsxzZM4cxQ1QKjKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz0tAnzt%2FYncYxZMjQq3AP418ZG1pIesTGtj1lFMiZb%2F4DCFd1jzoODfW4oxw9MBtqFUiRjOIUoknRkXMqlmQESbsh35QF4UiWoXcAw%2F%2FytBJrgXhY0%2BbwSEvuxNafivK0fSMW0JLycQpJ2JUgtX3GweaR9mJeMsc92okbxY8LJP%2Bf2yYm5ip6909r%2BhhfWUJt4mfvv8bE7TmWMF7%2BktdA5uzlxVJ6LLiw%2Fv351D6DaNMJBUU2L9wod2krOqmU870KfP2fo8mzYy8k5ANEZruhltFssDwofbU4Azh4f0wCufe8Wx%2FbCkX6cxdHcUxnEItOK8by70kyirlH1IxSnvNR3abZxe9JLS2Fn%2BQ5Gh%2BbvXOIQ8h7pGNCcGzUHN3uk8h3R8igX3LZwxZ%2FAFObBq4Jmb8RFt1XLBu7RpM7hQHpWgoZg%2Fvm6Nv27D6xd4t8xmBkzPv5mTLLwENfQhrQW6Fzljmlv35ig1uZ76xG8xVk0bu30q%2BQtCfpMDN8E6ZfkPddckefpiTge5HUZnjrAuuGnwCC5RQN7RglhBMOQAeNn14BnXhBMz8wyx6otYoJj%2BJy6EMAibFYu28c7yYtM%2BbSHwFF9MR1ybmf3xRbOtlbr91ztAKu%2FziceIl%2BgPNENu3F6WzWBh0dsGyhCWjDPjpy9BjqnAdLi2tJgifwOlt%2BdcqfS42QpvNa8lhqv5%2BL1eMW2y4mhCsuB5wV%2BsI9NNPAK67sC7GeIS0%2B5BeecVC9eIr94Cn5yvXHQYBgyzxQCUzHJpPOIi8oRiqlSBoMfujbjjNRGnq4iFVF1JlMzhjVMFlq%2BqQgq5xa%2BCqyI8SwTMpIuUtd%2BWDFUNJA9J2bttWq7bTndWzC6pFMHjLtQTDxouLgyZJwj82BOjSbd&X-Amz-Signature=bc3a8b482ac205a141ae447ac715697f804bfe191a36cb142f7e5e33704b8204&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQPERYRG%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081757Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJFMEMCH2kGMZK4J58ioOtwPExplc8irgIDzHJDQ8ySQQo%2BMp4CICMgda5QSraNeaZcE6%2FMTQd1hG0RSnVsxzZM4cxQ1QKjKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz0tAnzt%2FYncYxZMjQq3AP418ZG1pIesTGtj1lFMiZb%2F4DCFd1jzoODfW4oxw9MBtqFUiRjOIUoknRkXMqlmQESbsh35QF4UiWoXcAw%2F%2FytBJrgXhY0%2BbwSEvuxNafivK0fSMW0JLycQpJ2JUgtX3GweaR9mJeMsc92okbxY8LJP%2Bf2yYm5ip6909r%2BhhfWUJt4mfvv8bE7TmWMF7%2BktdA5uzlxVJ6LLiw%2Fv351D6DaNMJBUU2L9wod2krOqmU870KfP2fo8mzYy8k5ANEZruhltFssDwofbU4Azh4f0wCufe8Wx%2FbCkX6cxdHcUxnEItOK8by70kyirlH1IxSnvNR3abZxe9JLS2Fn%2BQ5Gh%2BbvXOIQ8h7pGNCcGzUHN3uk8h3R8igX3LZwxZ%2FAFObBq4Jmb8RFt1XLBu7RpM7hQHpWgoZg%2Fvm6Nv27D6xd4t8xmBkzPv5mTLLwENfQhrQW6Fzljmlv35ig1uZ76xG8xVk0bu30q%2BQtCfpMDN8E6ZfkPddckefpiTge5HUZnjrAuuGnwCC5RQN7RglhBMOQAeNn14BnXhBMz8wyx6otYoJj%2BJy6EMAibFYu28c7yYtM%2BbSHwFF9MR1ybmf3xRbOtlbr91ztAKu%2FziceIl%2BgPNENu3F6WzWBh0dsGyhCWjDPjpy9BjqnAdLi2tJgifwOlt%2BdcqfS42QpvNa8lhqv5%2BL1eMW2y4mhCsuB5wV%2BsI9NNPAK67sC7GeIS0%2B5BeecVC9eIr94Cn5yvXHQYBgyzxQCUzHJpPOIi8oRiqlSBoMfujbjjNRGnq4iFVF1JlMzhjVMFlq%2BqQgq5xa%2BCqyI8SwTMpIuUtd%2BWDFUNJA9J2bttWq7bTndWzC6pFMHjLtQTDxouLgyZJwj82BOjSbd&X-Amz-Signature=eac9252f75c670a2dc9888c648e135f65499534517d4525a3c3ae2a753d1cbae&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
