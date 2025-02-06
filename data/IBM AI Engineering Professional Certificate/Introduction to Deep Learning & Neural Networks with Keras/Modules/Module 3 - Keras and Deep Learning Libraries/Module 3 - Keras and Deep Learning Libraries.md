

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROOKKRDH%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIAMuiB%2Bfw06d%2Biv7MgW1brHB1mxMb1BqqOQjL%2BImDt%2FNAiAFRZNS%2BHuXF3Xv%2FiFsG6pVQ6Y5bCrdPrU20CK4ezy0Fir%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMIT2K5UFvpy1ZNGgZKtwD2tjLFl%2Fb7GgrCt2ILrFWAOY9g6p13Mrcp%2FgtKlJTUzrUQm%2BJFRQjD0YfSkcgK2aaPctWEXOfqb1OBghERu9c3dT%2F7%2FtmzyVSmNAC9QJAxnslfGqumMBNdA6id5hTqsfIbZpjT%2FNd5lnZePGjshu1hHfvNUCdRw6mymYNTn1tq49ADuSz5WQKo8qf7ZzBR9FlmQYNU%2B0%2FxzNVwUpui%2F05PiUqcmZgAGc9eVqwJI2Id1NWOFBBmK39hcs0UWOSbLKgBlI1ekQL4HltQ8NA5gmMXLOfOxjvnrAujIJPp4SM1d2HY%2BIQ6rGB5SS%2B2OHGU5OzWp4k%2FEVbPD6cTOhvNF2vybyRgLCkZs%2BJhbN50qT5Ws%2B45XKPfR0mnM2qDmsmRqPZ%2Bj9LLziW8wBy0xa50kjoVDAqTthHg5BLg5zROQ0jY3x7zdclAwTI2uMLj%2BeZUBTHeFgySzyZ5OpC0qmif%2FVKOWYkh2y3FtqDRd70JLZfa6l4F0piWFPY7cV1GxEwRRpwO34MLFYQJuwIzEw1W5fatp4ZxlfZbn2aRAsSH2XIK4LPw2NLZ1r4sIxQua%2FJDYLHMLVgRtj4lmq9Z%2FOep45yNypYuWlQo3SwjtKn2EMLyKtGEfs%2FeaJYRZFOf5gw6%2BuRvQY6pgEt2%2B4QH5oS8IkKHJCY2OzhhrAuxhrY8tEEp%2F2CZ1eDtwEakjDeOouABdnqWazOK9wexGLgOcTuluoWPOGQnFsw0LrueFLr2npPrjTiKLwgDK1QwgsbALKa3wzLn7g4Q9Obj7Ypn1TN28AlKrbbPQbcx1sv5xxFsYvbCJHg2PLH8pVvsej3zTE4Q7nosbz1HZHj%2BxD29Vk5iJLb4YBSaezOzaxwUKhG&X-Amz-Signature=f442c8e86825a96e9e88298abede47a9776dfa89385229baba4b7e78c8f9ddbd&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROOKKRDH%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIAMuiB%2Bfw06d%2Biv7MgW1brHB1mxMb1BqqOQjL%2BImDt%2FNAiAFRZNS%2BHuXF3Xv%2FiFsG6pVQ6Y5bCrdPrU20CK4ezy0Fir%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMIT2K5UFvpy1ZNGgZKtwD2tjLFl%2Fb7GgrCt2ILrFWAOY9g6p13Mrcp%2FgtKlJTUzrUQm%2BJFRQjD0YfSkcgK2aaPctWEXOfqb1OBghERu9c3dT%2F7%2FtmzyVSmNAC9QJAxnslfGqumMBNdA6id5hTqsfIbZpjT%2FNd5lnZePGjshu1hHfvNUCdRw6mymYNTn1tq49ADuSz5WQKo8qf7ZzBR9FlmQYNU%2B0%2FxzNVwUpui%2F05PiUqcmZgAGc9eVqwJI2Id1NWOFBBmK39hcs0UWOSbLKgBlI1ekQL4HltQ8NA5gmMXLOfOxjvnrAujIJPp4SM1d2HY%2BIQ6rGB5SS%2B2OHGU5OzWp4k%2FEVbPD6cTOhvNF2vybyRgLCkZs%2BJhbN50qT5Ws%2B45XKPfR0mnM2qDmsmRqPZ%2Bj9LLziW8wBy0xa50kjoVDAqTthHg5BLg5zROQ0jY3x7zdclAwTI2uMLj%2BeZUBTHeFgySzyZ5OpC0qmif%2FVKOWYkh2y3FtqDRd70JLZfa6l4F0piWFPY7cV1GxEwRRpwO34MLFYQJuwIzEw1W5fatp4ZxlfZbn2aRAsSH2XIK4LPw2NLZ1r4sIxQua%2FJDYLHMLVgRtj4lmq9Z%2FOep45yNypYuWlQo3SwjtKn2EMLyKtGEfs%2FeaJYRZFOf5gw6%2BuRvQY6pgEt2%2B4QH5oS8IkKHJCY2OzhhrAuxhrY8tEEp%2F2CZ1eDtwEakjDeOouABdnqWazOK9wexGLgOcTuluoWPOGQnFsw0LrueFLr2npPrjTiKLwgDK1QwgsbALKa3wzLn7g4Q9Obj7Ypn1TN28AlKrbbPQbcx1sv5xxFsYvbCJHg2PLH8pVvsej3zTE4Q7nosbz1HZHj%2BxD29Vk5iJLb4YBSaezOzaxwUKhG&X-Amz-Signature=8afad3cd133c2f894648391c343830571cc40cf1a076467a9a1515638548887a&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROOKKRDH%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIAMuiB%2Bfw06d%2Biv7MgW1brHB1mxMb1BqqOQjL%2BImDt%2FNAiAFRZNS%2BHuXF3Xv%2FiFsG6pVQ6Y5bCrdPrU20CK4ezy0Fir%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMIT2K5UFvpy1ZNGgZKtwD2tjLFl%2Fb7GgrCt2ILrFWAOY9g6p13Mrcp%2FgtKlJTUzrUQm%2BJFRQjD0YfSkcgK2aaPctWEXOfqb1OBghERu9c3dT%2F7%2FtmzyVSmNAC9QJAxnslfGqumMBNdA6id5hTqsfIbZpjT%2FNd5lnZePGjshu1hHfvNUCdRw6mymYNTn1tq49ADuSz5WQKo8qf7ZzBR9FlmQYNU%2B0%2FxzNVwUpui%2F05PiUqcmZgAGc9eVqwJI2Id1NWOFBBmK39hcs0UWOSbLKgBlI1ekQL4HltQ8NA5gmMXLOfOxjvnrAujIJPp4SM1d2HY%2BIQ6rGB5SS%2B2OHGU5OzWp4k%2FEVbPD6cTOhvNF2vybyRgLCkZs%2BJhbN50qT5Ws%2B45XKPfR0mnM2qDmsmRqPZ%2Bj9LLziW8wBy0xa50kjoVDAqTthHg5BLg5zROQ0jY3x7zdclAwTI2uMLj%2BeZUBTHeFgySzyZ5OpC0qmif%2FVKOWYkh2y3FtqDRd70JLZfa6l4F0piWFPY7cV1GxEwRRpwO34MLFYQJuwIzEw1W5fatp4ZxlfZbn2aRAsSH2XIK4LPw2NLZ1r4sIxQua%2FJDYLHMLVgRtj4lmq9Z%2FOep45yNypYuWlQo3SwjtKn2EMLyKtGEfs%2FeaJYRZFOf5gw6%2BuRvQY6pgEt2%2B4QH5oS8IkKHJCY2OzhhrAuxhrY8tEEp%2F2CZ1eDtwEakjDeOouABdnqWazOK9wexGLgOcTuluoWPOGQnFsw0LrueFLr2npPrjTiKLwgDK1QwgsbALKa3wzLn7g4Q9Obj7Ypn1TN28AlKrbbPQbcx1sv5xxFsYvbCJHg2PLH8pVvsej3zTE4Q7nosbz1HZHj%2BxD29Vk5iJLb4YBSaezOzaxwUKhG&X-Amz-Signature=82aad19fd96355c73805aac36ea4a6f37c3a77ff20ffdb60180eb29852cd2ea6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPC5ODWV%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIGqqpTTp79vCR8xIEOImiPb7Pw24MWwbVccKErjfQRYyAiAIYm9636g3vFHPB27drqXBVB9GcPrl3yMeGNaQ5l%2FCXyr%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIM7m5Q9ErUauaIMksdKtwDIra4AnddZl13orzQLiMhxItQyx5WeYylMBez4lZAz%2FCk0N%2F8mYIJRGXjGTR0FZT%2FyEz2egZVQjiG6b5zw8fbVhsJ%2FY2l%2B12YrTwixRZ9jyOgbSzRovPJb1QXe3%2B0u9Y1r472kQ0%2FjNoR8s2YUEPs6%2B%2FbB5AydkeIOFwyXI9g0KX5ZGjj73qurAfSoJAvJbBymNvNKjKv%2Bjvys4VdJZ7jWxXm5jetLyK3AD78FtpkHty6Y%2FvrmUfxcsJwK%2BR26rWroozs2OMz%2FeRigfAYij9e4jBkotZur3qQiUqrwpw3hiuG9sXAD7iGln9biTasDKpcQJ4hkUrRD63uFxn2QVBPtvQo2Difve7k83iaQABUY5qhgEoQhtFZI3DbBrQRJjZJs9hhE3jKASiiJRjDwSx7dVl7g3b2KGx8vg%2FibxIoGVUSLKOnvIxHJUTJzhItZOY0gcxYoVByjrAfANuvnRwjuXWAXOIvk6rrsmG7u10KQbP9q6G80JyEXkMSzWgtL1LhB24xus0%2BHdCZte%2BKbbGXP875KPPcsCawNzfIw8wWc7LciC7XmtUaR0J2Oa39ogv2r%2BsoCzFgyR69bviGO%2Br0EUIz9XsqerHF6n93fF%2BKAceawRoAsYfWWvmo1vwwh%2ByRvQY6pgFLQb9ATp5pdxHgy63JU%2Fd2TbkVSB0M2yBdtf8thSLkL9IpRtY3QKeBBRAa%2BGXj7reJCBznlKxDnzshHTWFNl89fFZPomsM2TnwbpWKlC5q%2FDtkb228Qv0zNalYdtGKYrL7iXg0SszpJaJ86Bhb%2FiFFVyUmS0N2wwovPMMJYWSVv1AmydWlrJ65Efz%2Bg9HspPQsW2xasLa0KCvuM%2Bl28t6Xdf2Ui8M5&X-Amz-Signature=d123181f1f6d6b6840fd0e5ef1cc52925d8cedf2ad81381be0656ec89f5c5b6b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46632NX6JMX%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIBLpVGQsDAdIFhUOSkMP3H1UtP6jyVt1I0Xo4XEskU%2FlAiAz8FlVaz4TxsTbjjCSDePayHqSFLkGCfmaP1Ub0HAAzCr%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMnrKGRVU8WopBFYtmKtwDxcid%2B%2ByVpviCeT5Wte4WlPqfTtmkD4Da6NVUywFseVCosj8L9ulapZixFe%2FxQCII7OT9sW4hLD%2Fh3vPIGWhikPCLMiRb7ASQCqwffLE8%2BQsaf4BRopfj%2FCq1Ea4fTw5nyZx07V%2BsRvZ1hSc45I%2FBh9MwIs3F%2Bs3O2RI44btiyxbrmJLRUERMB%2FcMLeFbR5TD6dm0msac0F8nbbiLRkwV3miQS%2FcjqL0JOdSXtSscpuYLISBD%2FFtWRjc7PugyTrNmpoRMSYkfU66S4F2jsDPEgFzOfZvchGuqxBVK49yPSfCDob1vkO2f39Clq3B6QwoLOnE7Q%2FjiHyAlKmA1m8Y%2BDudp6ZLV5qmr9nA8FgZrjUZ2QEbNo00Qo8Beb3Gk9mDAZY5uOxSoai6oijdInc9deLaoWygpmoiu31qygN21vXnBh6rAQSzeqK57itTQ6sm%2FKXTakD6RlA%2F1yxJytERgz8Q78L1Hvddk5asfG5B2unDyKsPJmbCubcvCiqEadNn%2FWEFPv3leeHFTxkUYP0nsLyZackAOUnOddkXzlrwZ9uQRZYQuO%2FlIZKOlU3iL6SUXH%2Fh9aRuqCsf1Y5Kzj%2BVagZL152cVcB9ijSqOkK5I94EXJBaqWz%2Fo07m4qaswyuyRvQY6pgEUdmIQQkQODHT8h%2B8q7FbJwXP%2Fy4eYkIYQj6IqxvwTWcATW5AASndzmMVvJObvxkrwbD%2BsMuwgX%2BK2cz0Xpmu2RXXD0VuRjWFkXTuFIFauEx1T15tFGtvnWuXM4OvlIkRNT8lbgCryKFa5RT%2Bjeh3sYJWI8g2Sp%2BhOQk5bY0Y4dS%2Bjqdsvbx6YdC%2FZXiuEZMdP0mOXq9Xf4cMJVGfNhQMCWv8SCF%2BE&X-Amz-Signature=ed79bdcfb4596e06e7a8272e7746d5de9aab062423f91560f74ba655e4df1d9a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROOKKRDH%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIAMuiB%2Bfw06d%2Biv7MgW1brHB1mxMb1BqqOQjL%2BImDt%2FNAiAFRZNS%2BHuXF3Xv%2FiFsG6pVQ6Y5bCrdPrU20CK4ezy0Fir%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMIT2K5UFvpy1ZNGgZKtwD2tjLFl%2Fb7GgrCt2ILrFWAOY9g6p13Mrcp%2FgtKlJTUzrUQm%2BJFRQjD0YfSkcgK2aaPctWEXOfqb1OBghERu9c3dT%2F7%2FtmzyVSmNAC9QJAxnslfGqumMBNdA6id5hTqsfIbZpjT%2FNd5lnZePGjshu1hHfvNUCdRw6mymYNTn1tq49ADuSz5WQKo8qf7ZzBR9FlmQYNU%2B0%2FxzNVwUpui%2F05PiUqcmZgAGc9eVqwJI2Id1NWOFBBmK39hcs0UWOSbLKgBlI1ekQL4HltQ8NA5gmMXLOfOxjvnrAujIJPp4SM1d2HY%2BIQ6rGB5SS%2B2OHGU5OzWp4k%2FEVbPD6cTOhvNF2vybyRgLCkZs%2BJhbN50qT5Ws%2B45XKPfR0mnM2qDmsmRqPZ%2Bj9LLziW8wBy0xa50kjoVDAqTthHg5BLg5zROQ0jY3x7zdclAwTI2uMLj%2BeZUBTHeFgySzyZ5OpC0qmif%2FVKOWYkh2y3FtqDRd70JLZfa6l4F0piWFPY7cV1GxEwRRpwO34MLFYQJuwIzEw1W5fatp4ZxlfZbn2aRAsSH2XIK4LPw2NLZ1r4sIxQua%2FJDYLHMLVgRtj4lmq9Z%2FOep45yNypYuWlQo3SwjtKn2EMLyKtGEfs%2FeaJYRZFOf5gw6%2BuRvQY6pgEt2%2B4QH5oS8IkKHJCY2OzhhrAuxhrY8tEEp%2F2CZ1eDtwEakjDeOouABdnqWazOK9wexGLgOcTuluoWPOGQnFsw0LrueFLr2npPrjTiKLwgDK1QwgsbALKa3wzLn7g4Q9Obj7Ypn1TN28AlKrbbPQbcx1sv5xxFsYvbCJHg2PLH8pVvsej3zTE4Q7nosbz1HZHj%2BxD29Vk5iJLb4YBSaezOzaxwUKhG&X-Amz-Signature=952b452b9343f5560d5631b8c8657f926dd3cfc7771f59d22227ab58c4749c09&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROOKKRDH%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIAMuiB%2Bfw06d%2Biv7MgW1brHB1mxMb1BqqOQjL%2BImDt%2FNAiAFRZNS%2BHuXF3Xv%2FiFsG6pVQ6Y5bCrdPrU20CK4ezy0Fir%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMIT2K5UFvpy1ZNGgZKtwD2tjLFl%2Fb7GgrCt2ILrFWAOY9g6p13Mrcp%2FgtKlJTUzrUQm%2BJFRQjD0YfSkcgK2aaPctWEXOfqb1OBghERu9c3dT%2F7%2FtmzyVSmNAC9QJAxnslfGqumMBNdA6id5hTqsfIbZpjT%2FNd5lnZePGjshu1hHfvNUCdRw6mymYNTn1tq49ADuSz5WQKo8qf7ZzBR9FlmQYNU%2B0%2FxzNVwUpui%2F05PiUqcmZgAGc9eVqwJI2Id1NWOFBBmK39hcs0UWOSbLKgBlI1ekQL4HltQ8NA5gmMXLOfOxjvnrAujIJPp4SM1d2HY%2BIQ6rGB5SS%2B2OHGU5OzWp4k%2FEVbPD6cTOhvNF2vybyRgLCkZs%2BJhbN50qT5Ws%2B45XKPfR0mnM2qDmsmRqPZ%2Bj9LLziW8wBy0xa50kjoVDAqTthHg5BLg5zROQ0jY3x7zdclAwTI2uMLj%2BeZUBTHeFgySzyZ5OpC0qmif%2FVKOWYkh2y3FtqDRd70JLZfa6l4F0piWFPY7cV1GxEwRRpwO34MLFYQJuwIzEw1W5fatp4ZxlfZbn2aRAsSH2XIK4LPw2NLZ1r4sIxQua%2FJDYLHMLVgRtj4lmq9Z%2FOep45yNypYuWlQo3SwjtKn2EMLyKtGEfs%2FeaJYRZFOf5gw6%2BuRvQY6pgEt2%2B4QH5oS8IkKHJCY2OzhhrAuxhrY8tEEp%2F2CZ1eDtwEakjDeOouABdnqWazOK9wexGLgOcTuluoWPOGQnFsw0LrueFLr2npPrjTiKLwgDK1QwgsbALKa3wzLn7g4Q9Obj7Ypn1TN28AlKrbbPQbcx1sv5xxFsYvbCJHg2PLH8pVvsej3zTE4Q7nosbz1HZHj%2BxD29Vk5iJLb4YBSaezOzaxwUKhG&X-Amz-Signature=ad1cdf351601ff8f50881a677bd586d9401e9614205ba0903920df9f23bdae9d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROOKKRDH%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIAMuiB%2Bfw06d%2Biv7MgW1brHB1mxMb1BqqOQjL%2BImDt%2FNAiAFRZNS%2BHuXF3Xv%2FiFsG6pVQ6Y5bCrdPrU20CK4ezy0Fir%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMIT2K5UFvpy1ZNGgZKtwD2tjLFl%2Fb7GgrCt2ILrFWAOY9g6p13Mrcp%2FgtKlJTUzrUQm%2BJFRQjD0YfSkcgK2aaPctWEXOfqb1OBghERu9c3dT%2F7%2FtmzyVSmNAC9QJAxnslfGqumMBNdA6id5hTqsfIbZpjT%2FNd5lnZePGjshu1hHfvNUCdRw6mymYNTn1tq49ADuSz5WQKo8qf7ZzBR9FlmQYNU%2B0%2FxzNVwUpui%2F05PiUqcmZgAGc9eVqwJI2Id1NWOFBBmK39hcs0UWOSbLKgBlI1ekQL4HltQ8NA5gmMXLOfOxjvnrAujIJPp4SM1d2HY%2BIQ6rGB5SS%2B2OHGU5OzWp4k%2FEVbPD6cTOhvNF2vybyRgLCkZs%2BJhbN50qT5Ws%2B45XKPfR0mnM2qDmsmRqPZ%2Bj9LLziW8wBy0xa50kjoVDAqTthHg5BLg5zROQ0jY3x7zdclAwTI2uMLj%2BeZUBTHeFgySzyZ5OpC0qmif%2FVKOWYkh2y3FtqDRd70JLZfa6l4F0piWFPY7cV1GxEwRRpwO34MLFYQJuwIzEw1W5fatp4ZxlfZbn2aRAsSH2XIK4LPw2NLZ1r4sIxQua%2FJDYLHMLVgRtj4lmq9Z%2FOep45yNypYuWlQo3SwjtKn2EMLyKtGEfs%2FeaJYRZFOf5gw6%2BuRvQY6pgEt2%2B4QH5oS8IkKHJCY2OzhhrAuxhrY8tEEp%2F2CZ1eDtwEakjDeOouABdnqWazOK9wexGLgOcTuluoWPOGQnFsw0LrueFLr2npPrjTiKLwgDK1QwgsbALKa3wzLn7g4Q9Obj7Ypn1TN28AlKrbbPQbcx1sv5xxFsYvbCJHg2PLH8pVvsej3zTE4Q7nosbz1HZHj%2BxD29Vk5iJLb4YBSaezOzaxwUKhG&X-Amz-Signature=d8ec3e2e9f1631e2259890ac932b88ac3fd69524bd8608df31316beca2e3cf17&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROOKKRDH%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIAMuiB%2Bfw06d%2Biv7MgW1brHB1mxMb1BqqOQjL%2BImDt%2FNAiAFRZNS%2BHuXF3Xv%2FiFsG6pVQ6Y5bCrdPrU20CK4ezy0Fir%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMIT2K5UFvpy1ZNGgZKtwD2tjLFl%2Fb7GgrCt2ILrFWAOY9g6p13Mrcp%2FgtKlJTUzrUQm%2BJFRQjD0YfSkcgK2aaPctWEXOfqb1OBghERu9c3dT%2F7%2FtmzyVSmNAC9QJAxnslfGqumMBNdA6id5hTqsfIbZpjT%2FNd5lnZePGjshu1hHfvNUCdRw6mymYNTn1tq49ADuSz5WQKo8qf7ZzBR9FlmQYNU%2B0%2FxzNVwUpui%2F05PiUqcmZgAGc9eVqwJI2Id1NWOFBBmK39hcs0UWOSbLKgBlI1ekQL4HltQ8NA5gmMXLOfOxjvnrAujIJPp4SM1d2HY%2BIQ6rGB5SS%2B2OHGU5OzWp4k%2FEVbPD6cTOhvNF2vybyRgLCkZs%2BJhbN50qT5Ws%2B45XKPfR0mnM2qDmsmRqPZ%2Bj9LLziW8wBy0xa50kjoVDAqTthHg5BLg5zROQ0jY3x7zdclAwTI2uMLj%2BeZUBTHeFgySzyZ5OpC0qmif%2FVKOWYkh2y3FtqDRd70JLZfa6l4F0piWFPY7cV1GxEwRRpwO34MLFYQJuwIzEw1W5fatp4ZxlfZbn2aRAsSH2XIK4LPw2NLZ1r4sIxQua%2FJDYLHMLVgRtj4lmq9Z%2FOep45yNypYuWlQo3SwjtKn2EMLyKtGEfs%2FeaJYRZFOf5gw6%2BuRvQY6pgEt2%2B4QH5oS8IkKHJCY2OzhhrAuxhrY8tEEp%2F2CZ1eDtwEakjDeOouABdnqWazOK9wexGLgOcTuluoWPOGQnFsw0LrueFLr2npPrjTiKLwgDK1QwgsbALKa3wzLn7g4Q9Obj7Ypn1TN28AlKrbbPQbcx1sv5xxFsYvbCJHg2PLH8pVvsej3zTE4Q7nosbz1HZHj%2BxD29Vk5iJLb4YBSaezOzaxwUKhG&X-Amz-Signature=af840a32c3c8b37579a21e48d275f61d502754b930aa54cd0ada2a366ddca9cd&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
