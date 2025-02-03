

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U2P5QREQ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101604Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICV5JH21AykGf%2BvE%2FoN%2FJqTGbLxjrDcsKsmNDjGNywwiAiEA8TqTcTIJRjQVS1TmyJevmxgYfYIEK0HylGvdlnxFR%2B4q%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDKEQpq%2FOBJKTVTbVfSrcAx40%2BU7o1lwB9ItrmEm4uifnQ6gcoLTj%2F7qAmlWxlkSvW%2B2vrznlPvrSF%2BgqEax2w%2BkWVpeOU%2FlSgjwVFu9PzJ9m%2Btp60B1X%2B%2BO2FU0rHvxk1PsPqXwVH%2FiTqriVWpmVopPG3W3j%2FBtcwKjHOeyzFdO51VfjoKJkJq0DG1hiz%2Fb4CIJh9lfDzLZrZ44v77dUYvDRlOCINL98oYuh7pB1ms%2FHuGK%2F2N%2FoFpSCQmQipr8nPAtta%2BpmczHmGNRpkhoC1vmLTOaSgOIZa7Gbop01pB77lcI71rUStcDmuT2j31iInnkTu4KHrh2SENyFrxmRQO17ow5abn8%2FJAQO%2BKqI0zbSX%2B1uVXR2yBELhn8jNa9AYXyEDCgAeQnHlXTkH6syLKzitiTjlcN8M9Wo22ZeAkn8VRZI1IffJ%2BeNliHSc53lCJ0xQ%2FJbjyCQ77aVQAPRv2OZS3oOJ1ucUmjImU8kdvO8ef1liQlAu7vAOSiErWsrcZtQJD0V0RS%2FTY1J3Lkai2kOFchZcAmOnmgDpgXyxhuIa1mUlIGfbnQaw6o8FuQOkzyBgqSNL2J7jVHzpUiPAicyd%2BCibUMInuTSpdnnhXrNMzYIOODbN0wEFHABlXnyivUd0BLEVXx2ztOTMMPzgb0GOqUBtRKSUai5JPNeiHhDINVOEt3QzoYshE5jCdLRqdH%2BPahNjLD0S23PteYvNSmgNFxrIHo7KBui9vDZhCt3IObRCiMyQu3Qr0faLQEALqzfa0Plj0TltD0m7KVvRv3WanzEZv3k3660QyWJP62D7AH%2BTSiuJKzOYcvS98%2B8lDfa0M%2F0pfscZsecORn4hc8W6XUdmS4iMRBR%2Bwd02xW30DvqIv8haU0H&X-Amz-Signature=f65e031333f2b51e927187b2176b971b6318ddb92067e640970cad42752ed868&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U2P5QREQ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101604Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICV5JH21AykGf%2BvE%2FoN%2FJqTGbLxjrDcsKsmNDjGNywwiAiEA8TqTcTIJRjQVS1TmyJevmxgYfYIEK0HylGvdlnxFR%2B4q%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDKEQpq%2FOBJKTVTbVfSrcAx40%2BU7o1lwB9ItrmEm4uifnQ6gcoLTj%2F7qAmlWxlkSvW%2B2vrznlPvrSF%2BgqEax2w%2BkWVpeOU%2FlSgjwVFu9PzJ9m%2Btp60B1X%2B%2BO2FU0rHvxk1PsPqXwVH%2FiTqriVWpmVopPG3W3j%2FBtcwKjHOeyzFdO51VfjoKJkJq0DG1hiz%2Fb4CIJh9lfDzLZrZ44v77dUYvDRlOCINL98oYuh7pB1ms%2FHuGK%2F2N%2FoFpSCQmQipr8nPAtta%2BpmczHmGNRpkhoC1vmLTOaSgOIZa7Gbop01pB77lcI71rUStcDmuT2j31iInnkTu4KHrh2SENyFrxmRQO17ow5abn8%2FJAQO%2BKqI0zbSX%2B1uVXR2yBELhn8jNa9AYXyEDCgAeQnHlXTkH6syLKzitiTjlcN8M9Wo22ZeAkn8VRZI1IffJ%2BeNliHSc53lCJ0xQ%2FJbjyCQ77aVQAPRv2OZS3oOJ1ucUmjImU8kdvO8ef1liQlAu7vAOSiErWsrcZtQJD0V0RS%2FTY1J3Lkai2kOFchZcAmOnmgDpgXyxhuIa1mUlIGfbnQaw6o8FuQOkzyBgqSNL2J7jVHzpUiPAicyd%2BCibUMInuTSpdnnhXrNMzYIOODbN0wEFHABlXnyivUd0BLEVXx2ztOTMMPzgb0GOqUBtRKSUai5JPNeiHhDINVOEt3QzoYshE5jCdLRqdH%2BPahNjLD0S23PteYvNSmgNFxrIHo7KBui9vDZhCt3IObRCiMyQu3Qr0faLQEALqzfa0Plj0TltD0m7KVvRv3WanzEZv3k3660QyWJP62D7AH%2BTSiuJKzOYcvS98%2B8lDfa0M%2F0pfscZsecORn4hc8W6XUdmS4iMRBR%2Bwd02xW30DvqIv8haU0H&X-Amz-Signature=2abdd019c40dba375f54dc3a0842ff85df45918083c763d1ca2ceab53b3a40d5&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U2P5QREQ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101604Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICV5JH21AykGf%2BvE%2FoN%2FJqTGbLxjrDcsKsmNDjGNywwiAiEA8TqTcTIJRjQVS1TmyJevmxgYfYIEK0HylGvdlnxFR%2B4q%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDKEQpq%2FOBJKTVTbVfSrcAx40%2BU7o1lwB9ItrmEm4uifnQ6gcoLTj%2F7qAmlWxlkSvW%2B2vrznlPvrSF%2BgqEax2w%2BkWVpeOU%2FlSgjwVFu9PzJ9m%2Btp60B1X%2B%2BO2FU0rHvxk1PsPqXwVH%2FiTqriVWpmVopPG3W3j%2FBtcwKjHOeyzFdO51VfjoKJkJq0DG1hiz%2Fb4CIJh9lfDzLZrZ44v77dUYvDRlOCINL98oYuh7pB1ms%2FHuGK%2F2N%2FoFpSCQmQipr8nPAtta%2BpmczHmGNRpkhoC1vmLTOaSgOIZa7Gbop01pB77lcI71rUStcDmuT2j31iInnkTu4KHrh2SENyFrxmRQO17ow5abn8%2FJAQO%2BKqI0zbSX%2B1uVXR2yBELhn8jNa9AYXyEDCgAeQnHlXTkH6syLKzitiTjlcN8M9Wo22ZeAkn8VRZI1IffJ%2BeNliHSc53lCJ0xQ%2FJbjyCQ77aVQAPRv2OZS3oOJ1ucUmjImU8kdvO8ef1liQlAu7vAOSiErWsrcZtQJD0V0RS%2FTY1J3Lkai2kOFchZcAmOnmgDpgXyxhuIa1mUlIGfbnQaw6o8FuQOkzyBgqSNL2J7jVHzpUiPAicyd%2BCibUMInuTSpdnnhXrNMzYIOODbN0wEFHABlXnyivUd0BLEVXx2ztOTMMPzgb0GOqUBtRKSUai5JPNeiHhDINVOEt3QzoYshE5jCdLRqdH%2BPahNjLD0S23PteYvNSmgNFxrIHo7KBui9vDZhCt3IObRCiMyQu3Qr0faLQEALqzfa0Plj0TltD0m7KVvRv3WanzEZv3k3660QyWJP62D7AH%2BTSiuJKzOYcvS98%2B8lDfa0M%2F0pfscZsecORn4hc8W6XUdmS4iMRBR%2Bwd02xW30DvqIv8haU0H&X-Amz-Signature=ea8aff36bf50af7e44cfcd96419e2b5059decbb70d477869a424349ecd96e9e9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V2XV37OZ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101605Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC2O82n7DcQNQxJhRG%2BUawh96l1yISB4tnKKbFiOXPSBAiAGNcKTWLy7ffu%2BBbAfVqEi9jWQ0%2BNktbHNN050fj%2BppSr%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMjPOA1wCXFStCD%2FI1KtwDbt4aLEmovIJ2VUElTNsJz9an83kwux%2FNQE85NbiazwbfmqZ2sCkiZ0W84M9KSE03Q45N9jUpXW6nnM2oHQtZoWUMGHXxtHFocI49lyBiz1umVN4m5M9y94PYDvsTlrcpIIdJ%2F3WOUPnsKfBRJMrHuvo3zykN0ZxL%2FUN%2BPZyLwamkJxrzvU8hX%2BONeJnfs%2BJqOJd%2BK1zc6741KYn4aBOYE4BrQxJGioCM5qv2xVwyO9Le%2FGtvhbt6zYk5omo%2FwNgbesR%2FitGMl1y4v77km5wYQlH4BLsuiPiQB%2F3zM9MZ9R42noVDX2fQ7EnF2CuVNfD4Ay9kE4BqqMRyDpN%2FzO2HthNRzbMMr2ygZ1Onr7CUTUG7%2BT0RiYXveXTeg9FooByUNV9PTHgzJs4Eib92lutYxi5%2FQe7%2FpyabqDGJX66z7xJCi%2Fg82fL%2BapOLfn83L5QxQhF9%2FEVVpNcId65uDX8JgD8N1YeCLPz8kAUdgq2t%2FCHdnxlAB%2FfgbYT6he3yccG%2FTTEjDz89nZ8SP6xe8cM5nxlAtUB0gdu3w2Z1yLk1vJTBSmzZ3wcCp08ZTk5BLlmOveF05GLMLzlH2e4L2VWMgb8%2F0m%2Bj1L99ud62Hplzc8ZMKmb3RLEgfKVbq20wt%2FOBvQY6pgF2Kr7AVLNVJ%2Bv0nttu3i6f9il3i%2FPQbkEiutZointFHmwfyrjEk%2BxYQCJiwEu9RX1yjszv8zZCdOQRxhxxAF99hBXDNPGGytUGaG2ZwUkvzcZOlf2Gz1IYdQCLqTfXmQ5zNNj%2BoHi6wOdSI%2BM03x5ztY1bG4MGmv2D06p936TxJX3JgBWkW6kwBwKHv8P03StAef%2BO2tykW%2BEnSF7ys8KhOACtY9y0&X-Amz-Signature=133b055fce9aef32327f7c10a40a20c66a2ed75a5ee214fdd29fca91ee38eb56&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46632CGLWWL%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101605Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICbTpKtudT41%2Fm91rPjRezkkn7P%2BZSjtDWjSwJK2KSRqAiEAsPR%2Bq%2FBmqsgnrq7S2haTJMtHIW2phetrM26KsqbSJEMq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDOVat1%2B3HURMEOZ7KCrcA11YcnYK%2B8lmU4vWDT2HZSsb0WWRabwPrvMIn83F1XeKzB72B5VKAeh2JBYmE9phjj%2FhSd1o%2Favr4vGZH4llWZpsiTv6HgXcGC2Z8hOpeFAGgtwLnM5I%2BAoFU0IgY01c68DKz9ZmcVcXJQ4od8Sk7HHEe0333Z5XxjQm%2BL7VxJYIZO8FMFqITi7V1t8GZhHyViatWt353uqjehfvyvKrthVSOzAApn2fiiN4mE%2BUPqXbm1gIO2hq58bxbpLXklNrNUZWkDVY%2BTvP3AeZ2DWaDl%2BgxzurSNcjC29T93%2FAbCTNCQ%2B42w9xa%2F%2BW29KLpi%2FZ7a8h2j26T1gzXnrI74YuKP0Q2F061ijKESpMrVHycHiW3q1R2s391NZQGi6%2Fd7s3h4M5vwu7CKcBqKC0LLUg36QQreOrGnziTRPJ8c1M5JjN%2FHOwjRXN9a65946qTVap1nu4lRPZz3Mz7jazB3algDQvm0Sa30TlffVEf68ao%2BaTUCcx%2Bx6eyY4WucSXVQzW7KDelntJ1LzZNXIIL9zBv1mEAHqzvS5SOMf7poUlIzP%2BYn2aCruGt%2B4Oci8sHOu26jIU3iDtqa03rk6ALpKn9y71LaixEtxefe4IO0NpYkxnFuxF1%2Bkvh99tN9S6MIH0gb0GOqUBLUEbFNKD6QG5ybTpmEtHsnKk9vv%2By8uzJUFpgPXv8aqLJHHb9X7odZnVh09JcdYM%2FuNGa4cT2O%2Bw5mDMxwci83B6UfHV2w%2BzY4EwySRtIAaXuurcbHAHgBXKjAaPbeoCbONZsERHHRzdyj2ja1j5h24QF3kZ2GaFM4%2BZJmlhoy02NJUZWwaGkwiUQ9gZ6El1fyzzA93HjBdJWBA2eGyECzNiAZD%2B&X-Amz-Signature=51033c3a01daf334aa2cf404d93d75ad4621f8e820d1f8401b9e36b36a825db1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U2P5QREQ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101604Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICV5JH21AykGf%2BvE%2FoN%2FJqTGbLxjrDcsKsmNDjGNywwiAiEA8TqTcTIJRjQVS1TmyJevmxgYfYIEK0HylGvdlnxFR%2B4q%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDKEQpq%2FOBJKTVTbVfSrcAx40%2BU7o1lwB9ItrmEm4uifnQ6gcoLTj%2F7qAmlWxlkSvW%2B2vrznlPvrSF%2BgqEax2w%2BkWVpeOU%2FlSgjwVFu9PzJ9m%2Btp60B1X%2B%2BO2FU0rHvxk1PsPqXwVH%2FiTqriVWpmVopPG3W3j%2FBtcwKjHOeyzFdO51VfjoKJkJq0DG1hiz%2Fb4CIJh9lfDzLZrZ44v77dUYvDRlOCINL98oYuh7pB1ms%2FHuGK%2F2N%2FoFpSCQmQipr8nPAtta%2BpmczHmGNRpkhoC1vmLTOaSgOIZa7Gbop01pB77lcI71rUStcDmuT2j31iInnkTu4KHrh2SENyFrxmRQO17ow5abn8%2FJAQO%2BKqI0zbSX%2B1uVXR2yBELhn8jNa9AYXyEDCgAeQnHlXTkH6syLKzitiTjlcN8M9Wo22ZeAkn8VRZI1IffJ%2BeNliHSc53lCJ0xQ%2FJbjyCQ77aVQAPRv2OZS3oOJ1ucUmjImU8kdvO8ef1liQlAu7vAOSiErWsrcZtQJD0V0RS%2FTY1J3Lkai2kOFchZcAmOnmgDpgXyxhuIa1mUlIGfbnQaw6o8FuQOkzyBgqSNL2J7jVHzpUiPAicyd%2BCibUMInuTSpdnnhXrNMzYIOODbN0wEFHABlXnyivUd0BLEVXx2ztOTMMPzgb0GOqUBtRKSUai5JPNeiHhDINVOEt3QzoYshE5jCdLRqdH%2BPahNjLD0S23PteYvNSmgNFxrIHo7KBui9vDZhCt3IObRCiMyQu3Qr0faLQEALqzfa0Plj0TltD0m7KVvRv3WanzEZv3k3660QyWJP62D7AH%2BTSiuJKzOYcvS98%2B8lDfa0M%2F0pfscZsecORn4hc8W6XUdmS4iMRBR%2Bwd02xW30DvqIv8haU0H&X-Amz-Signature=2c2d2197ad9ff26d5af18cf48428fb671d00f8248d32a826a5f3170b6cab5da2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U2P5QREQ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101604Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICV5JH21AykGf%2BvE%2FoN%2FJqTGbLxjrDcsKsmNDjGNywwiAiEA8TqTcTIJRjQVS1TmyJevmxgYfYIEK0HylGvdlnxFR%2B4q%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDKEQpq%2FOBJKTVTbVfSrcAx40%2BU7o1lwB9ItrmEm4uifnQ6gcoLTj%2F7qAmlWxlkSvW%2B2vrznlPvrSF%2BgqEax2w%2BkWVpeOU%2FlSgjwVFu9PzJ9m%2Btp60B1X%2B%2BO2FU0rHvxk1PsPqXwVH%2FiTqriVWpmVopPG3W3j%2FBtcwKjHOeyzFdO51VfjoKJkJq0DG1hiz%2Fb4CIJh9lfDzLZrZ44v77dUYvDRlOCINL98oYuh7pB1ms%2FHuGK%2F2N%2FoFpSCQmQipr8nPAtta%2BpmczHmGNRpkhoC1vmLTOaSgOIZa7Gbop01pB77lcI71rUStcDmuT2j31iInnkTu4KHrh2SENyFrxmRQO17ow5abn8%2FJAQO%2BKqI0zbSX%2B1uVXR2yBELhn8jNa9AYXyEDCgAeQnHlXTkH6syLKzitiTjlcN8M9Wo22ZeAkn8VRZI1IffJ%2BeNliHSc53lCJ0xQ%2FJbjyCQ77aVQAPRv2OZS3oOJ1ucUmjImU8kdvO8ef1liQlAu7vAOSiErWsrcZtQJD0V0RS%2FTY1J3Lkai2kOFchZcAmOnmgDpgXyxhuIa1mUlIGfbnQaw6o8FuQOkzyBgqSNL2J7jVHzpUiPAicyd%2BCibUMInuTSpdnnhXrNMzYIOODbN0wEFHABlXnyivUd0BLEVXx2ztOTMMPzgb0GOqUBtRKSUai5JPNeiHhDINVOEt3QzoYshE5jCdLRqdH%2BPahNjLD0S23PteYvNSmgNFxrIHo7KBui9vDZhCt3IObRCiMyQu3Qr0faLQEALqzfa0Plj0TltD0m7KVvRv3WanzEZv3k3660QyWJP62D7AH%2BTSiuJKzOYcvS98%2B8lDfa0M%2F0pfscZsecORn4hc8W6XUdmS4iMRBR%2Bwd02xW30DvqIv8haU0H&X-Amz-Signature=1eab705fd8d3f6d7cc60ba7d893799fd2a79a0b942b1fcc6634da03a0fe24f59&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U2P5QREQ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101604Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICV5JH21AykGf%2BvE%2FoN%2FJqTGbLxjrDcsKsmNDjGNywwiAiEA8TqTcTIJRjQVS1TmyJevmxgYfYIEK0HylGvdlnxFR%2B4q%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDKEQpq%2FOBJKTVTbVfSrcAx40%2BU7o1lwB9ItrmEm4uifnQ6gcoLTj%2F7qAmlWxlkSvW%2B2vrznlPvrSF%2BgqEax2w%2BkWVpeOU%2FlSgjwVFu9PzJ9m%2Btp60B1X%2B%2BO2FU0rHvxk1PsPqXwVH%2FiTqriVWpmVopPG3W3j%2FBtcwKjHOeyzFdO51VfjoKJkJq0DG1hiz%2Fb4CIJh9lfDzLZrZ44v77dUYvDRlOCINL98oYuh7pB1ms%2FHuGK%2F2N%2FoFpSCQmQipr8nPAtta%2BpmczHmGNRpkhoC1vmLTOaSgOIZa7Gbop01pB77lcI71rUStcDmuT2j31iInnkTu4KHrh2SENyFrxmRQO17ow5abn8%2FJAQO%2BKqI0zbSX%2B1uVXR2yBELhn8jNa9AYXyEDCgAeQnHlXTkH6syLKzitiTjlcN8M9Wo22ZeAkn8VRZI1IffJ%2BeNliHSc53lCJ0xQ%2FJbjyCQ77aVQAPRv2OZS3oOJ1ucUmjImU8kdvO8ef1liQlAu7vAOSiErWsrcZtQJD0V0RS%2FTY1J3Lkai2kOFchZcAmOnmgDpgXyxhuIa1mUlIGfbnQaw6o8FuQOkzyBgqSNL2J7jVHzpUiPAicyd%2BCibUMInuTSpdnnhXrNMzYIOODbN0wEFHABlXnyivUd0BLEVXx2ztOTMMPzgb0GOqUBtRKSUai5JPNeiHhDINVOEt3QzoYshE5jCdLRqdH%2BPahNjLD0S23PteYvNSmgNFxrIHo7KBui9vDZhCt3IObRCiMyQu3Qr0faLQEALqzfa0Plj0TltD0m7KVvRv3WanzEZv3k3660QyWJP62D7AH%2BTSiuJKzOYcvS98%2B8lDfa0M%2F0pfscZsecORn4hc8W6XUdmS4iMRBR%2Bwd02xW30DvqIv8haU0H&X-Amz-Signature=2f225e98f0f45812f32278e5656bb695c7da64158f001683dd124769efd944a7&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U2P5QREQ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101604Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICV5JH21AykGf%2BvE%2FoN%2FJqTGbLxjrDcsKsmNDjGNywwiAiEA8TqTcTIJRjQVS1TmyJevmxgYfYIEK0HylGvdlnxFR%2B4q%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDKEQpq%2FOBJKTVTbVfSrcAx40%2BU7o1lwB9ItrmEm4uifnQ6gcoLTj%2F7qAmlWxlkSvW%2B2vrznlPvrSF%2BgqEax2w%2BkWVpeOU%2FlSgjwVFu9PzJ9m%2Btp60B1X%2B%2BO2FU0rHvxk1PsPqXwVH%2FiTqriVWpmVopPG3W3j%2FBtcwKjHOeyzFdO51VfjoKJkJq0DG1hiz%2Fb4CIJh9lfDzLZrZ44v77dUYvDRlOCINL98oYuh7pB1ms%2FHuGK%2F2N%2FoFpSCQmQipr8nPAtta%2BpmczHmGNRpkhoC1vmLTOaSgOIZa7Gbop01pB77lcI71rUStcDmuT2j31iInnkTu4KHrh2SENyFrxmRQO17ow5abn8%2FJAQO%2BKqI0zbSX%2B1uVXR2yBELhn8jNa9AYXyEDCgAeQnHlXTkH6syLKzitiTjlcN8M9Wo22ZeAkn8VRZI1IffJ%2BeNliHSc53lCJ0xQ%2FJbjyCQ77aVQAPRv2OZS3oOJ1ucUmjImU8kdvO8ef1liQlAu7vAOSiErWsrcZtQJD0V0RS%2FTY1J3Lkai2kOFchZcAmOnmgDpgXyxhuIa1mUlIGfbnQaw6o8FuQOkzyBgqSNL2J7jVHzpUiPAicyd%2BCibUMInuTSpdnnhXrNMzYIOODbN0wEFHABlXnyivUd0BLEVXx2ztOTMMPzgb0GOqUBtRKSUai5JPNeiHhDINVOEt3QzoYshE5jCdLRqdH%2BPahNjLD0S23PteYvNSmgNFxrIHo7KBui9vDZhCt3IObRCiMyQu3Qr0faLQEALqzfa0Plj0TltD0m7KVvRv3WanzEZv3k3660QyWJP62D7AH%2BTSiuJKzOYcvS98%2B8lDfa0M%2F0pfscZsecORn4hc8W6XUdmS4iMRBR%2Bwd02xW30DvqIv8haU0H&X-Amz-Signature=40ebee8aa9991b6d165291be9a9520fce779b258c8180a034320e9a1b9b5961b&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
