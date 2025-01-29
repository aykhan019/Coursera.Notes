

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTXBOFM3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIGgJFetu3WLPDuJNr%2BOXoEnWeBP%2BZVn6HSGymBN5NJarAiEAx2Jpl%2BOAeIydCEywMg6A6e8r%2F%2B9FTPupK4DxDTDhCAYqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHzW%2Bgy5lq2BGO5GJyrcA0EMwcTrHTgro1AR%2ByNLGajDphlt9MygLRZCnmE9dn7cktkt4dPhPR7OVckLWp2wVpY4zMkMl9xEMJ26vyhA4aPlEkLUJo%2BGtRY2okv3Q56B73kBKqTZe%2B3eLLm04hZijAvfTJAps0NK4xJVRIPU8JL65pdtPAlU78pWXQYcxhQ5B36jNDbjnkO1%2B6zjDy%2FGWz1ANxbQ5aWybVtxrigDJI%2FkmuRiVl6E2Mwdp5rTxpEgknecA4Jk4UTIMsogTnls08KNPWdwDoubxqdZtBuzngtcSHOTiKkzza9VMRdzDxwVImhOHudm9YdPYzqv9LgXiGZ6T%2B0gfqBAIZ%2Bc3v6WG9zrmLCJerIs7mXjNNNEjXQqeAD%2FgblxkajmnQqDJ9jd8NpfGOAkSFcofMGRjXenzcssS48JgIGQGCr9cV2f2gEwfeBbMl8%2BHykdFVn1SVjSGAFbouuMrlXGS0xYJHSAWK14hl62OOatRO0FWXtF6tkvEsTZjrUSSFEV5mWjZ1yuMOGJCCuSusKUGJ%2Fj0J2r6GKxxWdQrc%2B2KgNxLB64OvGuTD9u1xvLObzSdpeGpTwciaRuobQ41f%2BRpU4U7ZvAtWtqkd3RlK%2FUKwsI1UHPcdLQMN%2BW20ewW%2B5rNgYFMLqQ57wGOqUBzNYbD5rabA73%2FqSEferFad1QLieuMKwSelc7m5XDs0WMr01711ZsjUFUmhON2JDgdTjoIhsqPjS2lwAAKLVb9idR04xgIUA73IzDVjkNcICLd9Sgqzp8VrNXAKI3wRFGLzJwBrVQKk6OTa%2BdwkJOZoIl9eXhRlX%2F2ydVgllETrzxnw4mXQJGGI30DNucGjovW1N5XC2GywEdOxrk1%2BEtzozCvP17&X-Amz-Signature=eabe5a72ce1564944d077a94c4cf307f17a61b04b3c5bca804674b8cc4a4dc75&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTXBOFM3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIGgJFetu3WLPDuJNr%2BOXoEnWeBP%2BZVn6HSGymBN5NJarAiEAx2Jpl%2BOAeIydCEywMg6A6e8r%2F%2B9FTPupK4DxDTDhCAYqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHzW%2Bgy5lq2BGO5GJyrcA0EMwcTrHTgro1AR%2ByNLGajDphlt9MygLRZCnmE9dn7cktkt4dPhPR7OVckLWp2wVpY4zMkMl9xEMJ26vyhA4aPlEkLUJo%2BGtRY2okv3Q56B73kBKqTZe%2B3eLLm04hZijAvfTJAps0NK4xJVRIPU8JL65pdtPAlU78pWXQYcxhQ5B36jNDbjnkO1%2B6zjDy%2FGWz1ANxbQ5aWybVtxrigDJI%2FkmuRiVl6E2Mwdp5rTxpEgknecA4Jk4UTIMsogTnls08KNPWdwDoubxqdZtBuzngtcSHOTiKkzza9VMRdzDxwVImhOHudm9YdPYzqv9LgXiGZ6T%2B0gfqBAIZ%2Bc3v6WG9zrmLCJerIs7mXjNNNEjXQqeAD%2FgblxkajmnQqDJ9jd8NpfGOAkSFcofMGRjXenzcssS48JgIGQGCr9cV2f2gEwfeBbMl8%2BHykdFVn1SVjSGAFbouuMrlXGS0xYJHSAWK14hl62OOatRO0FWXtF6tkvEsTZjrUSSFEV5mWjZ1yuMOGJCCuSusKUGJ%2Fj0J2r6GKxxWdQrc%2B2KgNxLB64OvGuTD9u1xvLObzSdpeGpTwciaRuobQ41f%2BRpU4U7ZvAtWtqkd3RlK%2FUKwsI1UHPcdLQMN%2BW20ewW%2B5rNgYFMLqQ57wGOqUBzNYbD5rabA73%2FqSEferFad1QLieuMKwSelc7m5XDs0WMr01711ZsjUFUmhON2JDgdTjoIhsqPjS2lwAAKLVb9idR04xgIUA73IzDVjkNcICLd9Sgqzp8VrNXAKI3wRFGLzJwBrVQKk6OTa%2BdwkJOZoIl9eXhRlX%2F2ydVgllETrzxnw4mXQJGGI30DNucGjovW1N5XC2GywEdOxrk1%2BEtzozCvP17&X-Amz-Signature=c7766c92bab71cfc116df6aa7032ba802466529e4820d24e64a5379ee1edc0d0&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTXBOFM3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIGgJFetu3WLPDuJNr%2BOXoEnWeBP%2BZVn6HSGymBN5NJarAiEAx2Jpl%2BOAeIydCEywMg6A6e8r%2F%2B9FTPupK4DxDTDhCAYqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHzW%2Bgy5lq2BGO5GJyrcA0EMwcTrHTgro1AR%2ByNLGajDphlt9MygLRZCnmE9dn7cktkt4dPhPR7OVckLWp2wVpY4zMkMl9xEMJ26vyhA4aPlEkLUJo%2BGtRY2okv3Q56B73kBKqTZe%2B3eLLm04hZijAvfTJAps0NK4xJVRIPU8JL65pdtPAlU78pWXQYcxhQ5B36jNDbjnkO1%2B6zjDy%2FGWz1ANxbQ5aWybVtxrigDJI%2FkmuRiVl6E2Mwdp5rTxpEgknecA4Jk4UTIMsogTnls08KNPWdwDoubxqdZtBuzngtcSHOTiKkzza9VMRdzDxwVImhOHudm9YdPYzqv9LgXiGZ6T%2B0gfqBAIZ%2Bc3v6WG9zrmLCJerIs7mXjNNNEjXQqeAD%2FgblxkajmnQqDJ9jd8NpfGOAkSFcofMGRjXenzcssS48JgIGQGCr9cV2f2gEwfeBbMl8%2BHykdFVn1SVjSGAFbouuMrlXGS0xYJHSAWK14hl62OOatRO0FWXtF6tkvEsTZjrUSSFEV5mWjZ1yuMOGJCCuSusKUGJ%2Fj0J2r6GKxxWdQrc%2B2KgNxLB64OvGuTD9u1xvLObzSdpeGpTwciaRuobQ41f%2BRpU4U7ZvAtWtqkd3RlK%2FUKwsI1UHPcdLQMN%2BW20ewW%2B5rNgYFMLqQ57wGOqUBzNYbD5rabA73%2FqSEferFad1QLieuMKwSelc7m5XDs0WMr01711ZsjUFUmhON2JDgdTjoIhsqPjS2lwAAKLVb9idR04xgIUA73IzDVjkNcICLd9Sgqzp8VrNXAKI3wRFGLzJwBrVQKk6OTa%2BdwkJOZoIl9eXhRlX%2F2ydVgllETrzxnw4mXQJGGI30DNucGjovW1N5XC2GywEdOxrk1%2BEtzozCvP17&X-Amz-Signature=788093ed48980e2047a96c6450e3100ed4d81816c531b3b61dbfcb7a8a163ddc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UY3T3IXN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJIMEYCIQDSBpakauSI3AkQZpCGfkq6EJ%2BdAAIjQXza5gzgY%2B5vJwIhAOcoOfijOJf%2BxxDnmkJF4EsYiiIxGzfHRGajVyMgVhKCKogECIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwnZH7xlTPEobRAoI4q3AN97N0GXBApl0IXTIBqrH8omdZ61Vb9H4RmXmC43aA9Mjvl8fD4lE8tyIRzuZni%2BhL367iLJ2hTKrD1D4fqYiTO48okdDTcy4J%2BCHki%2BR2%2FWgIKmZorW1LAN5bKUQ0O7enWJ5SzCXgG1pS4Jn66SLjlB9cZe4lQNo9fwI0PUin0brbZyuOU4E%2FS4KXsur8%2FyCChbr37ZvEggmkYdy2zMqCiU0aytpYNYVPXdzoggydnAJL7Q51sCPtXobcN%2BxABnBJVvqGnqKS0AWphP6oHHpjqiQO56sHijTH4HGMUVRoAY1BR%2BZotXrT8bdKWabmSQnpnHkIPuUUf%2F4nYM932E92W%2BJRLMLKkOVgGzKxRhWpwCf%2BjMi6Uf8R76gJ8P9Jw%2FBy%2F1RErk5v%2FgZ5RTMXFocDxs75LXZaNrITd5%2BCtXEAYnZFThc5e8mJur%2B3ZEC0Zju%2BGw7oRf1xM%2FU8ksdEU2VnzwBaYZVo13133XipOq%2BZPiN7dz6avu6f16cONTufvRJBof%2B8%2FRjOHK7Mkvia2X%2FPyNKK4wdWFUUWRLZO9a%2B5oxF1zisK4suT%2FkQbHzzMa4%2FHoHWi5OgBfzMZsGU%2FYsbODeXdJMx03XClYsSsSKH8fhtaURQjHmKvQCLhjKTDXkOe8BjqkAWri81iZo9DuxncFhu9JId9nGSlmpkGaIZ82eAIenYPdkgqptstpifsbBgeeGv9ZLdFTRkIUIXxWkAbKZdu2TnhQCvFwrqn8bYW%2F0ith0HCM3n1XRtf7hFDZo1W04EqNe8LvpBNIIGtTMmmZHaUouxIeVqFb0KCSvPj1oyVPu2rR9g3V6zSb2LV5tfXfZE9p2%2FqfNNwc0n6hTAvz6ViUWdcqYfDr&X-Amz-Signature=1c80c86a15c469e2c922370da360aa309b99d850e749f9894a70736d24bf0314&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667YWJUX4Y%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIQDeeR0%2FG2601XON%2BwNK4ernNNOmfX%2BNooSHiM8MApCumQIgMHWG12vGMFR7Ps%2B%2FeEgUx9ZulLyCxZDSAYFE8UFXr50qiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL28dBNHXKK2NRGY2ircAw0Pgy4mUN%2FOclNDmT27NUldLAGST1FMMl0pME0suK4NcZlu%2BdHPD%2Bgc16EcnKStNrAyq%2Fc48MkkFIO5KVxzARkRptxO%2FcW89DdTuOkMxNOxwIMjwbJhXbuNVwSk%2BbfEBMezJ7EXDVgfoBwBoniBejusKoQtmH8pYLGIbiYqE8fRRU9cz%2BIQtzse1grM2jOkPx0ZKZ92dRoqEgW3p8adnqEhNvdXhMsXzMaB6w53DPy%2Ft%2BGSqtguePOY5kGGGfc%2Fogw09XVVEuYR3FE498OCmb7p03ws98QXssCEnr4NdWI3NLFwXAm4Z6svdBrSNlwxgI8ThLFHrrYMPjW5FkJ6GOj8f7i8ohxJyMhKr4JWxcOprY37%2BPaKpS8KCR%2FN13RsHrOO451ewsknChG79xkLPxgm4tOovwnzp5VTWwwGJQyjffWB2jr5esXYMQdSGc67L0IjMQnHQ2AmA%2FYvJSO4IrNzeVwhlRRwlSjnZjOe5JiT3OxVL%2FQxFvzJZHEoqkIzuXnRhrZ9fSnNcjUQ1sN1nTg%2B6Ui6jmTcyis4Gzu%2FYgaq7%2FKOFEzUpDFebXbGjxqT8h7hEC0wO5huFPSjIyfEesdK2XrUpqgnzvYSahfd8aRx%2Bwvd4helaIG4Unp1MJeQ57wGOqUByg%2FPQjeSVKNp%2F3PKz%2B%2BorSxkkB14%2FNMDeRlUt2St8Pkg5CHjnHuEMtVw1EgC0ZRH8bJwbGxPEazqwMIp4XggWgS5E%2Bi%2FSIXC7vq7L2%2B7xwR6SUN9riI72vgf6fng9BAcXZ78f0pS27rB1d2V3ssTei%2Fz%2BxIv5EjybJ5%2FvFTrQXE4r8GLj2T%2By1lproGDqnoidg%2FEqM49nUwmuI29NMQY9IAbV4Q3&X-Amz-Signature=6720b058f3fc1bb38081c9f9c43303bad28938a65936a4a06af668c4cf896401&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTXBOFM3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIGgJFetu3WLPDuJNr%2BOXoEnWeBP%2BZVn6HSGymBN5NJarAiEAx2Jpl%2BOAeIydCEywMg6A6e8r%2F%2B9FTPupK4DxDTDhCAYqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHzW%2Bgy5lq2BGO5GJyrcA0EMwcTrHTgro1AR%2ByNLGajDphlt9MygLRZCnmE9dn7cktkt4dPhPR7OVckLWp2wVpY4zMkMl9xEMJ26vyhA4aPlEkLUJo%2BGtRY2okv3Q56B73kBKqTZe%2B3eLLm04hZijAvfTJAps0NK4xJVRIPU8JL65pdtPAlU78pWXQYcxhQ5B36jNDbjnkO1%2B6zjDy%2FGWz1ANxbQ5aWybVtxrigDJI%2FkmuRiVl6E2Mwdp5rTxpEgknecA4Jk4UTIMsogTnls08KNPWdwDoubxqdZtBuzngtcSHOTiKkzza9VMRdzDxwVImhOHudm9YdPYzqv9LgXiGZ6T%2B0gfqBAIZ%2Bc3v6WG9zrmLCJerIs7mXjNNNEjXQqeAD%2FgblxkajmnQqDJ9jd8NpfGOAkSFcofMGRjXenzcssS48JgIGQGCr9cV2f2gEwfeBbMl8%2BHykdFVn1SVjSGAFbouuMrlXGS0xYJHSAWK14hl62OOatRO0FWXtF6tkvEsTZjrUSSFEV5mWjZ1yuMOGJCCuSusKUGJ%2Fj0J2r6GKxxWdQrc%2B2KgNxLB64OvGuTD9u1xvLObzSdpeGpTwciaRuobQ41f%2BRpU4U7ZvAtWtqkd3RlK%2FUKwsI1UHPcdLQMN%2BW20ewW%2B5rNgYFMLqQ57wGOqUBzNYbD5rabA73%2FqSEferFad1QLieuMKwSelc7m5XDs0WMr01711ZsjUFUmhON2JDgdTjoIhsqPjS2lwAAKLVb9idR04xgIUA73IzDVjkNcICLd9Sgqzp8VrNXAKI3wRFGLzJwBrVQKk6OTa%2BdwkJOZoIl9eXhRlX%2F2ydVgllETrzxnw4mXQJGGI30DNucGjovW1N5XC2GywEdOxrk1%2BEtzozCvP17&X-Amz-Signature=abcd3d47499aab74719967542b15582eec7d230659b79a99867f548c7a780267&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTXBOFM3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIGgJFetu3WLPDuJNr%2BOXoEnWeBP%2BZVn6HSGymBN5NJarAiEAx2Jpl%2BOAeIydCEywMg6A6e8r%2F%2B9FTPupK4DxDTDhCAYqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHzW%2Bgy5lq2BGO5GJyrcA0EMwcTrHTgro1AR%2ByNLGajDphlt9MygLRZCnmE9dn7cktkt4dPhPR7OVckLWp2wVpY4zMkMl9xEMJ26vyhA4aPlEkLUJo%2BGtRY2okv3Q56B73kBKqTZe%2B3eLLm04hZijAvfTJAps0NK4xJVRIPU8JL65pdtPAlU78pWXQYcxhQ5B36jNDbjnkO1%2B6zjDy%2FGWz1ANxbQ5aWybVtxrigDJI%2FkmuRiVl6E2Mwdp5rTxpEgknecA4Jk4UTIMsogTnls08KNPWdwDoubxqdZtBuzngtcSHOTiKkzza9VMRdzDxwVImhOHudm9YdPYzqv9LgXiGZ6T%2B0gfqBAIZ%2Bc3v6WG9zrmLCJerIs7mXjNNNEjXQqeAD%2FgblxkajmnQqDJ9jd8NpfGOAkSFcofMGRjXenzcssS48JgIGQGCr9cV2f2gEwfeBbMl8%2BHykdFVn1SVjSGAFbouuMrlXGS0xYJHSAWK14hl62OOatRO0FWXtF6tkvEsTZjrUSSFEV5mWjZ1yuMOGJCCuSusKUGJ%2Fj0J2r6GKxxWdQrc%2B2KgNxLB64OvGuTD9u1xvLObzSdpeGpTwciaRuobQ41f%2BRpU4U7ZvAtWtqkd3RlK%2FUKwsI1UHPcdLQMN%2BW20ewW%2B5rNgYFMLqQ57wGOqUBzNYbD5rabA73%2FqSEferFad1QLieuMKwSelc7m5XDs0WMr01711ZsjUFUmhON2JDgdTjoIhsqPjS2lwAAKLVb9idR04xgIUA73IzDVjkNcICLd9Sgqzp8VrNXAKI3wRFGLzJwBrVQKk6OTa%2BdwkJOZoIl9eXhRlX%2F2ydVgllETrzxnw4mXQJGGI30DNucGjovW1N5XC2GywEdOxrk1%2BEtzozCvP17&X-Amz-Signature=db5dee30476e15f410271bf360e67a069646046ff1135236f30de49d40ea4648&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTXBOFM3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIGgJFetu3WLPDuJNr%2BOXoEnWeBP%2BZVn6HSGymBN5NJarAiEAx2Jpl%2BOAeIydCEywMg6A6e8r%2F%2B9FTPupK4DxDTDhCAYqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHzW%2Bgy5lq2BGO5GJyrcA0EMwcTrHTgro1AR%2ByNLGajDphlt9MygLRZCnmE9dn7cktkt4dPhPR7OVckLWp2wVpY4zMkMl9xEMJ26vyhA4aPlEkLUJo%2BGtRY2okv3Q56B73kBKqTZe%2B3eLLm04hZijAvfTJAps0NK4xJVRIPU8JL65pdtPAlU78pWXQYcxhQ5B36jNDbjnkO1%2B6zjDy%2FGWz1ANxbQ5aWybVtxrigDJI%2FkmuRiVl6E2Mwdp5rTxpEgknecA4Jk4UTIMsogTnls08KNPWdwDoubxqdZtBuzngtcSHOTiKkzza9VMRdzDxwVImhOHudm9YdPYzqv9LgXiGZ6T%2B0gfqBAIZ%2Bc3v6WG9zrmLCJerIs7mXjNNNEjXQqeAD%2FgblxkajmnQqDJ9jd8NpfGOAkSFcofMGRjXenzcssS48JgIGQGCr9cV2f2gEwfeBbMl8%2BHykdFVn1SVjSGAFbouuMrlXGS0xYJHSAWK14hl62OOatRO0FWXtF6tkvEsTZjrUSSFEV5mWjZ1yuMOGJCCuSusKUGJ%2Fj0J2r6GKxxWdQrc%2B2KgNxLB64OvGuTD9u1xvLObzSdpeGpTwciaRuobQ41f%2BRpU4U7ZvAtWtqkd3RlK%2FUKwsI1UHPcdLQMN%2BW20ewW%2B5rNgYFMLqQ57wGOqUBzNYbD5rabA73%2FqSEferFad1QLieuMKwSelc7m5XDs0WMr01711ZsjUFUmhON2JDgdTjoIhsqPjS2lwAAKLVb9idR04xgIUA73IzDVjkNcICLd9Sgqzp8VrNXAKI3wRFGLzJwBrVQKk6OTa%2BdwkJOZoIl9eXhRlX%2F2ydVgllETrzxnw4mXQJGGI30DNucGjovW1N5XC2GywEdOxrk1%2BEtzozCvP17&X-Amz-Signature=73ea9e387c182e6334de14e3661d4d927ff11c79870383fc3c983090bd2a0722&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTXBOFM3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIGgJFetu3WLPDuJNr%2BOXoEnWeBP%2BZVn6HSGymBN5NJarAiEAx2Jpl%2BOAeIydCEywMg6A6e8r%2F%2B9FTPupK4DxDTDhCAYqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHzW%2Bgy5lq2BGO5GJyrcA0EMwcTrHTgro1AR%2ByNLGajDphlt9MygLRZCnmE9dn7cktkt4dPhPR7OVckLWp2wVpY4zMkMl9xEMJ26vyhA4aPlEkLUJo%2BGtRY2okv3Q56B73kBKqTZe%2B3eLLm04hZijAvfTJAps0NK4xJVRIPU8JL65pdtPAlU78pWXQYcxhQ5B36jNDbjnkO1%2B6zjDy%2FGWz1ANxbQ5aWybVtxrigDJI%2FkmuRiVl6E2Mwdp5rTxpEgknecA4Jk4UTIMsogTnls08KNPWdwDoubxqdZtBuzngtcSHOTiKkzza9VMRdzDxwVImhOHudm9YdPYzqv9LgXiGZ6T%2B0gfqBAIZ%2Bc3v6WG9zrmLCJerIs7mXjNNNEjXQqeAD%2FgblxkajmnQqDJ9jd8NpfGOAkSFcofMGRjXenzcssS48JgIGQGCr9cV2f2gEwfeBbMl8%2BHykdFVn1SVjSGAFbouuMrlXGS0xYJHSAWK14hl62OOatRO0FWXtF6tkvEsTZjrUSSFEV5mWjZ1yuMOGJCCuSusKUGJ%2Fj0J2r6GKxxWdQrc%2B2KgNxLB64OvGuTD9u1xvLObzSdpeGpTwciaRuobQ41f%2BRpU4U7ZvAtWtqkd3RlK%2FUKwsI1UHPcdLQMN%2BW20ewW%2B5rNgYFMLqQ57wGOqUBzNYbD5rabA73%2FqSEferFad1QLieuMKwSelc7m5XDs0WMr01711ZsjUFUmhON2JDgdTjoIhsqPjS2lwAAKLVb9idR04xgIUA73IzDVjkNcICLd9Sgqzp8VrNXAKI3wRFGLzJwBrVQKk6OTa%2BdwkJOZoIl9eXhRlX%2F2ydVgllETrzxnw4mXQJGGI30DNucGjovW1N5XC2GywEdOxrk1%2BEtzozCvP17&X-Amz-Signature=256e0a693c5d05085e8d06ab0e838e7bda8687dcf45daa06b1b6f408276a59f9&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
