

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466347QKEEV%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJIMEYCIQD5Bj9Q4DeyixAb1LLsnCrnlVYN9ZTRXCoB6cOAyGxcqgIhAOWS7SM6Ue8qcmbLR5hXPHHnhIdOHBuWb1ZDykiNkRocKv8DCG4QABoMNjM3NDIzMTgzODA1Igx8Z0%2FBgDFzo80C6JIq3AN9EG4zy7e4M6yfA4se5MoHNj9VumOq9X%2B0TOBxEcqhebt7Dd6cxDFfD29qHGwZt6CrrC3TbRGWnyxX8WPfoNGj2t%2Fdm4%2BYfcYDpfe0TtIXW6bSc77ChosZ2mtPG23uxyZkrPu7jNZywSAXQuCdQrPz1PDBX4k72aQKpYWfRYcqGdcyQUFlyzYOBB2YbRTkwtJ8UvSaZGOgI%2Bwj0xphZelAYsCoaIxHQwx1HvCbR2i1Xi9N239QQw4BS88RjGWZEzVxsJBXrooEqaTW5U%2FROsLr4tA7k1ZLJYdud3eTEjC96LU8riox7JNuPgOf4vmRojZziAWAs6fTs9rYwIcmqhoDEFx1pcM3LE9MQWcXp3zSi0SIQJqjgVLEAE%2FqfISs42PATSjqS4TFTl%2F0A7mTsU62myPzKtCijHfQc9Ld%2BoikJPC9ObD58X55NCi%2BBP2wwlM0IoetIuOhA6Ga3zWzGyfXv1yQLbysF1JJlvCAzu2lOC43KxhAuS9ulsI6fFtNvMuD4LNI7TPV4TRct9NFLDQIWD8WjJYoZC2UuwWWx94xwU19WQnVmQeuS%2FI8DDv4CTk4Qx0TzSGKIEB%2B0vtQy%2FcPXvq2wKLOMxL55e0UHA2nG2NxUXvEh1PMExCogDCmoZa9BjqkAe5NTx96EkWWOo01hX%2F%2F0NeH5Wh4tk98blmiefqMQLRo%2FVuxUj%2Fuezh9atDc0CwTagDNc5uM1YyIW0TVqkkZZVXHVdQ%2BOuJgOol6L0ph6CSvIxfOjmu7TiHm17MpzkUAi7RzbqodQ9%2Biv%2Bs0k9T0HxXJ6YUuYuCtHI9c72HYA9gchhY1T7iHqSsgibXu%2FsmWkvfRWn1dcR9Nenq2vkMOuFgPVzbS&X-Amz-Signature=1a4c3e0c137fd34c9d95b29077190e9413de6e54fd38a5c200fc9b8bcb427afe&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466347QKEEV%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJIMEYCIQD5Bj9Q4DeyixAb1LLsnCrnlVYN9ZTRXCoB6cOAyGxcqgIhAOWS7SM6Ue8qcmbLR5hXPHHnhIdOHBuWb1ZDykiNkRocKv8DCG4QABoMNjM3NDIzMTgzODA1Igx8Z0%2FBgDFzo80C6JIq3AN9EG4zy7e4M6yfA4se5MoHNj9VumOq9X%2B0TOBxEcqhebt7Dd6cxDFfD29qHGwZt6CrrC3TbRGWnyxX8WPfoNGj2t%2Fdm4%2BYfcYDpfe0TtIXW6bSc77ChosZ2mtPG23uxyZkrPu7jNZywSAXQuCdQrPz1PDBX4k72aQKpYWfRYcqGdcyQUFlyzYOBB2YbRTkwtJ8UvSaZGOgI%2Bwj0xphZelAYsCoaIxHQwx1HvCbR2i1Xi9N239QQw4BS88RjGWZEzVxsJBXrooEqaTW5U%2FROsLr4tA7k1ZLJYdud3eTEjC96LU8riox7JNuPgOf4vmRojZziAWAs6fTs9rYwIcmqhoDEFx1pcM3LE9MQWcXp3zSi0SIQJqjgVLEAE%2FqfISs42PATSjqS4TFTl%2F0A7mTsU62myPzKtCijHfQc9Ld%2BoikJPC9ObD58X55NCi%2BBP2wwlM0IoetIuOhA6Ga3zWzGyfXv1yQLbysF1JJlvCAzu2lOC43KxhAuS9ulsI6fFtNvMuD4LNI7TPV4TRct9NFLDQIWD8WjJYoZC2UuwWWx94xwU19WQnVmQeuS%2FI8DDv4CTk4Qx0TzSGKIEB%2B0vtQy%2FcPXvq2wKLOMxL55e0UHA2nG2NxUXvEh1PMExCogDCmoZa9BjqkAe5NTx96EkWWOo01hX%2F%2F0NeH5Wh4tk98blmiefqMQLRo%2FVuxUj%2Fuezh9atDc0CwTagDNc5uM1YyIW0TVqkkZZVXHVdQ%2BOuJgOol6L0ph6CSvIxfOjmu7TiHm17MpzkUAi7RzbqodQ9%2Biv%2Bs0k9T0HxXJ6YUuYuCtHI9c72HYA9gchhY1T7iHqSsgibXu%2FsmWkvfRWn1dcR9Nenq2vkMOuFgPVzbS&X-Amz-Signature=0fc0ab2ba2d736509fea7379e26ba487ac67b65a01e6b65b9dd83bf2442e9d56&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466347QKEEV%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJIMEYCIQD5Bj9Q4DeyixAb1LLsnCrnlVYN9ZTRXCoB6cOAyGxcqgIhAOWS7SM6Ue8qcmbLR5hXPHHnhIdOHBuWb1ZDykiNkRocKv8DCG4QABoMNjM3NDIzMTgzODA1Igx8Z0%2FBgDFzo80C6JIq3AN9EG4zy7e4M6yfA4se5MoHNj9VumOq9X%2B0TOBxEcqhebt7Dd6cxDFfD29qHGwZt6CrrC3TbRGWnyxX8WPfoNGj2t%2Fdm4%2BYfcYDpfe0TtIXW6bSc77ChosZ2mtPG23uxyZkrPu7jNZywSAXQuCdQrPz1PDBX4k72aQKpYWfRYcqGdcyQUFlyzYOBB2YbRTkwtJ8UvSaZGOgI%2Bwj0xphZelAYsCoaIxHQwx1HvCbR2i1Xi9N239QQw4BS88RjGWZEzVxsJBXrooEqaTW5U%2FROsLr4tA7k1ZLJYdud3eTEjC96LU8riox7JNuPgOf4vmRojZziAWAs6fTs9rYwIcmqhoDEFx1pcM3LE9MQWcXp3zSi0SIQJqjgVLEAE%2FqfISs42PATSjqS4TFTl%2F0A7mTsU62myPzKtCijHfQc9Ld%2BoikJPC9ObD58X55NCi%2BBP2wwlM0IoetIuOhA6Ga3zWzGyfXv1yQLbysF1JJlvCAzu2lOC43KxhAuS9ulsI6fFtNvMuD4LNI7TPV4TRct9NFLDQIWD8WjJYoZC2UuwWWx94xwU19WQnVmQeuS%2FI8DDv4CTk4Qx0TzSGKIEB%2B0vtQy%2FcPXvq2wKLOMxL55e0UHA2nG2NxUXvEh1PMExCogDCmoZa9BjqkAe5NTx96EkWWOo01hX%2F%2F0NeH5Wh4tk98blmiefqMQLRo%2FVuxUj%2Fuezh9atDc0CwTagDNc5uM1YyIW0TVqkkZZVXHVdQ%2BOuJgOol6L0ph6CSvIxfOjmu7TiHm17MpzkUAi7RzbqodQ9%2Biv%2Bs0k9T0HxXJ6YUuYuCtHI9c72HYA9gchhY1T7iHqSsgibXu%2FsmWkvfRWn1dcR9Nenq2vkMOuFgPVzbS&X-Amz-Signature=5c1dd475005e9ac6c4b3108ed7550178f87da3f93e2d341263fe65e1dbbc1839&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XWXN3E5%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJHMEUCIG5MF7qxCLkPInrZzwoCzMjWC1zE%2FykvvXVaV2ml0vcGAiEAjX1CzcbmS%2BgVD%2F91dD11dkOPQBCnFTDJerVVKOcgRlYq%2FwMIbhAAGgw2Mzc0MjMxODM4MDUiDN2ll6KYWho3q8Y6oCrcA6Uy8WynBZpcN5M8XT%2F1O4W%2FARkzvHsB3xQx9WWfkMb%2BLHQ4tRDg8P%2BhHtK5i1AhsdcEz7PEDhz%2BKeQEDGmynfGYEIOHVdLV0aZEsSJemYKJ%2BAb8cuBt7l%2BaJCRPCcL4fs%2FFDrqc0qKHUvL6CaN73wkXXkf2kBuODuHc0k38aFRdkmiHZoIm4aGmKbBuvcAS%2F%2FnLLq4rsBgLCS3lgcAl9v1iluP0n6ystUuH8Xb4593vQMDOLczlg1XvzCGZaGk8AaAVIMJmtzIazbfhcIeZsstIM11f%2FpIdsz%2FX4tN2ulMxBhUX3fcv3XRXvH64dzZkz%2BqrhNl8sVnbpEV0e5YCsvDhJxK5l%2BQ2jyzybMDw5xuqLzYoc5madxgsgzHMiTpc%2F7t5rurS3uGpT3ye%2BBVFNpFfapwR4MwD7NHcI%2FrlJODZmc%2BCLau2IP4cHJd76RlomojESz1hXDKtElaGdF6cpYhRNF9bOGu9ZtmsqOT7UK3D1Yk6OinYCAH96xPNNYDokQgGNfald%2Bdr8xtOBkU2224qTHcPb%2BVwu%2Bp%2FLANc6Gk1xvUTFPyMtZAd6ZVdL%2BvV59z5noyhVpFI1e9174LJg%2BF6JGF%2B7HY2c5icQs%2FwRYZcNUnlPujfMbux%2BSjjMMGhlr0GOqUB90jl6W0nuOZkfSIQ5FHq7d%2BymkFVU77%2F8BONHE1sW6iJbDzFnINW%2BQeenAq9e5GiZZUI%2BE6h%2BwZT9R0SzMpP2LBl0ajCb%2Bgy8qBWnQxouuojYN9WAnkj1b7GqIVm7hlLUFS9LCj6KL2vN2U4Jp%2FLjVwv01u%2FB0ucL58lmwGXPmlKt8C%2BrhHEj76jnc8hv6uH6vMPh0Ck6%2BxxDUq%2BAVoZntapzb88&X-Amz-Signature=c7f4f3f69297372aee9254c6b03fa957994d3393c8df4a9e9b14e4581bb0c043&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666YLGAX7J%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJIMEYCIQCvmxXrZzoX%2Bg4ywpZkQ7%2BKfxwmEBPkBOrGxf37eb1q8QIhAMY8XWkxNtm1zveX%2BFimBke0%2Bt04gjM%2BZE8cOXDycT%2FHKv8DCG4QABoMNjM3NDIzMTgzODA1IgyWqczpf%2BQeM946QVAq3AMdCTrbFzlPhTbBzcIj2JZ37f%2FtFiLY%2BSP8xDgoR0a9Xai3lN5pp1jzD2W2gxO84LUWo%2FDdQoHEituOE532xs46wHJe0bhJsae2DFTpa6mRO8da2OGlqggO3%2FZh%2BbW2t4iychNYPOWUx4ojV%2B2nxC9W9I6EFZEU7y9rRsFmjcTppBxPXa1Hl2KCkAAkV5wOpF0XVge8xyW%2F3b2P9VBux0xhK26SnWlvhiFNl575x9pNUrSvoQ5QqfhtXqQTiUUdgXpLuo1Zvuk3MEgWxYpQbTTFQORSUOIPzuKnMHW0SZ4OtvJ0wzlbefCCql1l%2BGRjLna%2FfVzrJWVRN0R2m%2Fblpk9SGmXQZ2%2FtHJwPC%2BPefiYruwm3aV7ZGNUxkZxugY1%2BrUH94704%2BMEX7j3Bv%2F3FHHCAjWNDY4ycF7fZD1zfu1kNlaFZ6DpdjAkIbzmxpLJbWE1J6EHcrurC60wVzmeigGmMeBawx7UZkDbbXnoHOKue%2BMyCrqs%2Bnr%2FzNZERYFbA5o4bcwBsMW1LIW6h8JTSkq17ZmrOPqD5c6r56QhY5x%2FbXf3Qk4S4hcAT%2BD03ukG05ubnnYVwh1QKm625tUe6dc9faKkI5ihqNpqol4a4VfTtfummKpWEO3hMe9KjRzCvoZa9BjqkAfFPCuhqtsdnh3US%2BRrbaKIMTK431Dj9yG7szINcOgQaNCFJgceMJswN1juSOKK2XvycRibPzz%2BlKKTFjFRmLiWUrlm66vuegyDr3xOhZAYPosxHCkcXnXLofozazf%2BX%2BGfbnewUIHYxh99Wj036viTJnP6u%2FJl%2FYuh49QV%2Fu7XmhzcERjDPgLrKV1xp33wCqLXcb1I4mTqHGnNoYZvQBhQiczc6&X-Amz-Signature=134587e56694f2eb0849fa3b474ec78bf620263c5c2368848966e51438e35213&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466347QKEEV%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJIMEYCIQD5Bj9Q4DeyixAb1LLsnCrnlVYN9ZTRXCoB6cOAyGxcqgIhAOWS7SM6Ue8qcmbLR5hXPHHnhIdOHBuWb1ZDykiNkRocKv8DCG4QABoMNjM3NDIzMTgzODA1Igx8Z0%2FBgDFzo80C6JIq3AN9EG4zy7e4M6yfA4se5MoHNj9VumOq9X%2B0TOBxEcqhebt7Dd6cxDFfD29qHGwZt6CrrC3TbRGWnyxX8WPfoNGj2t%2Fdm4%2BYfcYDpfe0TtIXW6bSc77ChosZ2mtPG23uxyZkrPu7jNZywSAXQuCdQrPz1PDBX4k72aQKpYWfRYcqGdcyQUFlyzYOBB2YbRTkwtJ8UvSaZGOgI%2Bwj0xphZelAYsCoaIxHQwx1HvCbR2i1Xi9N239QQw4BS88RjGWZEzVxsJBXrooEqaTW5U%2FROsLr4tA7k1ZLJYdud3eTEjC96LU8riox7JNuPgOf4vmRojZziAWAs6fTs9rYwIcmqhoDEFx1pcM3LE9MQWcXp3zSi0SIQJqjgVLEAE%2FqfISs42PATSjqS4TFTl%2F0A7mTsU62myPzKtCijHfQc9Ld%2BoikJPC9ObD58X55NCi%2BBP2wwlM0IoetIuOhA6Ga3zWzGyfXv1yQLbysF1JJlvCAzu2lOC43KxhAuS9ulsI6fFtNvMuD4LNI7TPV4TRct9NFLDQIWD8WjJYoZC2UuwWWx94xwU19WQnVmQeuS%2FI8DDv4CTk4Qx0TzSGKIEB%2B0vtQy%2FcPXvq2wKLOMxL55e0UHA2nG2NxUXvEh1PMExCogDCmoZa9BjqkAe5NTx96EkWWOo01hX%2F%2F0NeH5Wh4tk98blmiefqMQLRo%2FVuxUj%2Fuezh9atDc0CwTagDNc5uM1YyIW0TVqkkZZVXHVdQ%2BOuJgOol6L0ph6CSvIxfOjmu7TiHm17MpzkUAi7RzbqodQ9%2Biv%2Bs0k9T0HxXJ6YUuYuCtHI9c72HYA9gchhY1T7iHqSsgibXu%2FsmWkvfRWn1dcR9Nenq2vkMOuFgPVzbS&X-Amz-Signature=ed3352084821c621ec8e8a4b5c4d6c074eb2341328528185bbab76419540f42e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466347QKEEV%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJIMEYCIQD5Bj9Q4DeyixAb1LLsnCrnlVYN9ZTRXCoB6cOAyGxcqgIhAOWS7SM6Ue8qcmbLR5hXPHHnhIdOHBuWb1ZDykiNkRocKv8DCG4QABoMNjM3NDIzMTgzODA1Igx8Z0%2FBgDFzo80C6JIq3AN9EG4zy7e4M6yfA4se5MoHNj9VumOq9X%2B0TOBxEcqhebt7Dd6cxDFfD29qHGwZt6CrrC3TbRGWnyxX8WPfoNGj2t%2Fdm4%2BYfcYDpfe0TtIXW6bSc77ChosZ2mtPG23uxyZkrPu7jNZywSAXQuCdQrPz1PDBX4k72aQKpYWfRYcqGdcyQUFlyzYOBB2YbRTkwtJ8UvSaZGOgI%2Bwj0xphZelAYsCoaIxHQwx1HvCbR2i1Xi9N239QQw4BS88RjGWZEzVxsJBXrooEqaTW5U%2FROsLr4tA7k1ZLJYdud3eTEjC96LU8riox7JNuPgOf4vmRojZziAWAs6fTs9rYwIcmqhoDEFx1pcM3LE9MQWcXp3zSi0SIQJqjgVLEAE%2FqfISs42PATSjqS4TFTl%2F0A7mTsU62myPzKtCijHfQc9Ld%2BoikJPC9ObD58X55NCi%2BBP2wwlM0IoetIuOhA6Ga3zWzGyfXv1yQLbysF1JJlvCAzu2lOC43KxhAuS9ulsI6fFtNvMuD4LNI7TPV4TRct9NFLDQIWD8WjJYoZC2UuwWWx94xwU19WQnVmQeuS%2FI8DDv4CTk4Qx0TzSGKIEB%2B0vtQy%2FcPXvq2wKLOMxL55e0UHA2nG2NxUXvEh1PMExCogDCmoZa9BjqkAe5NTx96EkWWOo01hX%2F%2F0NeH5Wh4tk98blmiefqMQLRo%2FVuxUj%2Fuezh9atDc0CwTagDNc5uM1YyIW0TVqkkZZVXHVdQ%2BOuJgOol6L0ph6CSvIxfOjmu7TiHm17MpzkUAi7RzbqodQ9%2Biv%2Bs0k9T0HxXJ6YUuYuCtHI9c72HYA9gchhY1T7iHqSsgibXu%2FsmWkvfRWn1dcR9Nenq2vkMOuFgPVzbS&X-Amz-Signature=48aaefe05313427377e23d88890ef6fb7f7b9d6b8a87cf3a53bdb6ce2544909d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466347QKEEV%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJIMEYCIQD5Bj9Q4DeyixAb1LLsnCrnlVYN9ZTRXCoB6cOAyGxcqgIhAOWS7SM6Ue8qcmbLR5hXPHHnhIdOHBuWb1ZDykiNkRocKv8DCG4QABoMNjM3NDIzMTgzODA1Igx8Z0%2FBgDFzo80C6JIq3AN9EG4zy7e4M6yfA4se5MoHNj9VumOq9X%2B0TOBxEcqhebt7Dd6cxDFfD29qHGwZt6CrrC3TbRGWnyxX8WPfoNGj2t%2Fdm4%2BYfcYDpfe0TtIXW6bSc77ChosZ2mtPG23uxyZkrPu7jNZywSAXQuCdQrPz1PDBX4k72aQKpYWfRYcqGdcyQUFlyzYOBB2YbRTkwtJ8UvSaZGOgI%2Bwj0xphZelAYsCoaIxHQwx1HvCbR2i1Xi9N239QQw4BS88RjGWZEzVxsJBXrooEqaTW5U%2FROsLr4tA7k1ZLJYdud3eTEjC96LU8riox7JNuPgOf4vmRojZziAWAs6fTs9rYwIcmqhoDEFx1pcM3LE9MQWcXp3zSi0SIQJqjgVLEAE%2FqfISs42PATSjqS4TFTl%2F0A7mTsU62myPzKtCijHfQc9Ld%2BoikJPC9ObD58X55NCi%2BBP2wwlM0IoetIuOhA6Ga3zWzGyfXv1yQLbysF1JJlvCAzu2lOC43KxhAuS9ulsI6fFtNvMuD4LNI7TPV4TRct9NFLDQIWD8WjJYoZC2UuwWWx94xwU19WQnVmQeuS%2FI8DDv4CTk4Qx0TzSGKIEB%2B0vtQy%2FcPXvq2wKLOMxL55e0UHA2nG2NxUXvEh1PMExCogDCmoZa9BjqkAe5NTx96EkWWOo01hX%2F%2F0NeH5Wh4tk98blmiefqMQLRo%2FVuxUj%2Fuezh9atDc0CwTagDNc5uM1YyIW0TVqkkZZVXHVdQ%2BOuJgOol6L0ph6CSvIxfOjmu7TiHm17MpzkUAi7RzbqodQ9%2Biv%2Bs0k9T0HxXJ6YUuYuCtHI9c72HYA9gchhY1T7iHqSsgibXu%2FsmWkvfRWn1dcR9Nenq2vkMOuFgPVzbS&X-Amz-Signature=614d0a04b0ec518d46d039a2f1d85b9ff9f80d12db971872c9b543e740d6825c&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466347QKEEV%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJIMEYCIQD5Bj9Q4DeyixAb1LLsnCrnlVYN9ZTRXCoB6cOAyGxcqgIhAOWS7SM6Ue8qcmbLR5hXPHHnhIdOHBuWb1ZDykiNkRocKv8DCG4QABoMNjM3NDIzMTgzODA1Igx8Z0%2FBgDFzo80C6JIq3AN9EG4zy7e4M6yfA4se5MoHNj9VumOq9X%2B0TOBxEcqhebt7Dd6cxDFfD29qHGwZt6CrrC3TbRGWnyxX8WPfoNGj2t%2Fdm4%2BYfcYDpfe0TtIXW6bSc77ChosZ2mtPG23uxyZkrPu7jNZywSAXQuCdQrPz1PDBX4k72aQKpYWfRYcqGdcyQUFlyzYOBB2YbRTkwtJ8UvSaZGOgI%2Bwj0xphZelAYsCoaIxHQwx1HvCbR2i1Xi9N239QQw4BS88RjGWZEzVxsJBXrooEqaTW5U%2FROsLr4tA7k1ZLJYdud3eTEjC96LU8riox7JNuPgOf4vmRojZziAWAs6fTs9rYwIcmqhoDEFx1pcM3LE9MQWcXp3zSi0SIQJqjgVLEAE%2FqfISs42PATSjqS4TFTl%2F0A7mTsU62myPzKtCijHfQc9Ld%2BoikJPC9ObD58X55NCi%2BBP2wwlM0IoetIuOhA6Ga3zWzGyfXv1yQLbysF1JJlvCAzu2lOC43KxhAuS9ulsI6fFtNvMuD4LNI7TPV4TRct9NFLDQIWD8WjJYoZC2UuwWWx94xwU19WQnVmQeuS%2FI8DDv4CTk4Qx0TzSGKIEB%2B0vtQy%2FcPXvq2wKLOMxL55e0UHA2nG2NxUXvEh1PMExCogDCmoZa9BjqkAe5NTx96EkWWOo01hX%2F%2F0NeH5Wh4tk98blmiefqMQLRo%2FVuxUj%2Fuezh9atDc0CwTagDNc5uM1YyIW0TVqkkZZVXHVdQ%2BOuJgOol6L0ph6CSvIxfOjmu7TiHm17MpzkUAi7RzbqodQ9%2Biv%2Bs0k9T0HxXJ6YUuYuCtHI9c72HYA9gchhY1T7iHqSsgibXu%2FsmWkvfRWn1dcR9Nenq2vkMOuFgPVzbS&X-Amz-Signature=6932b68d1dad9518d102303e8ae9da48df3c2d8d9d990adf6a7c928d5809fecb&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
