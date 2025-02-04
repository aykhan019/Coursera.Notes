

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y2ZRCONJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJGMEQCIDDaqqmLgsMWHZ1RhWRb8H29wJXFYr62GNFIts8Pm%2BDSAiAq9UUvWvRYAjUdODe46csr%2FjBMiRoB%2BRXcvqcam%2FVTlSr%2FAwg1EAAaDDYzNzQyMzE4MzgwNSIMnWjJYmBVdPgKslTeKtwDhza%2Fl2Csujiir7ZXx0PVDm73m6fMgJRFnn8tvJqJIQTEdg2tZe%2B0%2FEBp2Qm3ftDNUpa2Lt2f5ZqNGoXG5H%2BsEmeT4jREzmSfn1MdbIVOa38oYHXZaXQhWFcW2gYW4dtwAFdGlI7XqyPwP%2BoAYeJsAkDSmfa4uqQk%2Byui9s5LYReFKgWWPhv8nuwSoangfwfOfdxBw3HfZcmAvq28LwqgT3BLIvfNOV%2FJWwBOPcicAHzjrRgMnvR%2BnxI6kY0aeI5GFqb1UqauriWeyHFA%2Fj61dd%2BJiVG4MGTAdTQdlWOryaksKTs%2BbNs5c%2Fzz5eVSLqjafaKKQPMIqinVLD%2BYnj50rTLPkvw%2FXSaTDWxQDLVOUrMeAzAqV3ykFDpvB6hoEKf20MxIoel3gCYe0FVcv19xWDeftczEoz2Yle0s2hmhKaYr61xfU1nMu19pgbeNcPlikcfT5vrxJYeopTR0d1ziwMJt4I3N2W5RrGzL9ytzZlAsHcN43km2Z1eKCCLxlpm1MylLcAwiH%2F9H2BUr7iDmsNoVzOqV4dMpHH8PeP%2BnhWg9bmIXmNf3M%2B6eOptIjzkMXnR00L1fCI%2BB8kxyEzqBhBBWiY53IqQsImVrb5Z5U6hquCzzEYbT6Iy9InYw8dyJvQY6pgGqJ9onYvyjrfuVPHVIYTZOUijfBx3UQF3Wsoc%2B2ar9YWhXtrp3CydGJl%2Bl6fkS0FE2yOWM9R385VYNd5bhh36qL%2BCBu0X78UgTMnLWotK%2FaM7PC5llPDWu0fn6upGX7yI%2BY%2BnWE7INKUtFjwAUDQ1VvQ%2F%2FKA6C5nLCNr%2Fw%2BQw0hAN57AYqAFOlkwgwdd1O3mjeYvNiBhv0k5OmCJDIIrw4dbp1NqmZ&X-Amz-Signature=a4fe116a62c3cca0965301b1f2408a8d8e5aeb6279ae62706a4e140295678dcf&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y2ZRCONJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJGMEQCIDDaqqmLgsMWHZ1RhWRb8H29wJXFYr62GNFIts8Pm%2BDSAiAq9UUvWvRYAjUdODe46csr%2FjBMiRoB%2BRXcvqcam%2FVTlSr%2FAwg1EAAaDDYzNzQyMzE4MzgwNSIMnWjJYmBVdPgKslTeKtwDhza%2Fl2Csujiir7ZXx0PVDm73m6fMgJRFnn8tvJqJIQTEdg2tZe%2B0%2FEBp2Qm3ftDNUpa2Lt2f5ZqNGoXG5H%2BsEmeT4jREzmSfn1MdbIVOa38oYHXZaXQhWFcW2gYW4dtwAFdGlI7XqyPwP%2BoAYeJsAkDSmfa4uqQk%2Byui9s5LYReFKgWWPhv8nuwSoangfwfOfdxBw3HfZcmAvq28LwqgT3BLIvfNOV%2FJWwBOPcicAHzjrRgMnvR%2BnxI6kY0aeI5GFqb1UqauriWeyHFA%2Fj61dd%2BJiVG4MGTAdTQdlWOryaksKTs%2BbNs5c%2Fzz5eVSLqjafaKKQPMIqinVLD%2BYnj50rTLPkvw%2FXSaTDWxQDLVOUrMeAzAqV3ykFDpvB6hoEKf20MxIoel3gCYe0FVcv19xWDeftczEoz2Yle0s2hmhKaYr61xfU1nMu19pgbeNcPlikcfT5vrxJYeopTR0d1ziwMJt4I3N2W5RrGzL9ytzZlAsHcN43km2Z1eKCCLxlpm1MylLcAwiH%2F9H2BUr7iDmsNoVzOqV4dMpHH8PeP%2BnhWg9bmIXmNf3M%2B6eOptIjzkMXnR00L1fCI%2BB8kxyEzqBhBBWiY53IqQsImVrb5Z5U6hquCzzEYbT6Iy9InYw8dyJvQY6pgGqJ9onYvyjrfuVPHVIYTZOUijfBx3UQF3Wsoc%2B2ar9YWhXtrp3CydGJl%2Bl6fkS0FE2yOWM9R385VYNd5bhh36qL%2BCBu0X78UgTMnLWotK%2FaM7PC5llPDWu0fn6upGX7yI%2BY%2BnWE7INKUtFjwAUDQ1VvQ%2F%2FKA6C5nLCNr%2Fw%2BQw0hAN57AYqAFOlkwgwdd1O3mjeYvNiBhv0k5OmCJDIIrw4dbp1NqmZ&X-Amz-Signature=8d6bfc58dfe3b800a9b286552307aed89b3fea0f9a87435a6eb933ef453395c1&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y2ZRCONJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJGMEQCIDDaqqmLgsMWHZ1RhWRb8H29wJXFYr62GNFIts8Pm%2BDSAiAq9UUvWvRYAjUdODe46csr%2FjBMiRoB%2BRXcvqcam%2FVTlSr%2FAwg1EAAaDDYzNzQyMzE4MzgwNSIMnWjJYmBVdPgKslTeKtwDhza%2Fl2Csujiir7ZXx0PVDm73m6fMgJRFnn8tvJqJIQTEdg2tZe%2B0%2FEBp2Qm3ftDNUpa2Lt2f5ZqNGoXG5H%2BsEmeT4jREzmSfn1MdbIVOa38oYHXZaXQhWFcW2gYW4dtwAFdGlI7XqyPwP%2BoAYeJsAkDSmfa4uqQk%2Byui9s5LYReFKgWWPhv8nuwSoangfwfOfdxBw3HfZcmAvq28LwqgT3BLIvfNOV%2FJWwBOPcicAHzjrRgMnvR%2BnxI6kY0aeI5GFqb1UqauriWeyHFA%2Fj61dd%2BJiVG4MGTAdTQdlWOryaksKTs%2BbNs5c%2Fzz5eVSLqjafaKKQPMIqinVLD%2BYnj50rTLPkvw%2FXSaTDWxQDLVOUrMeAzAqV3ykFDpvB6hoEKf20MxIoel3gCYe0FVcv19xWDeftczEoz2Yle0s2hmhKaYr61xfU1nMu19pgbeNcPlikcfT5vrxJYeopTR0d1ziwMJt4I3N2W5RrGzL9ytzZlAsHcN43km2Z1eKCCLxlpm1MylLcAwiH%2F9H2BUr7iDmsNoVzOqV4dMpHH8PeP%2BnhWg9bmIXmNf3M%2B6eOptIjzkMXnR00L1fCI%2BB8kxyEzqBhBBWiY53IqQsImVrb5Z5U6hquCzzEYbT6Iy9InYw8dyJvQY6pgGqJ9onYvyjrfuVPHVIYTZOUijfBx3UQF3Wsoc%2B2ar9YWhXtrp3CydGJl%2Bl6fkS0FE2yOWM9R385VYNd5bhh36qL%2BCBu0X78UgTMnLWotK%2FaM7PC5llPDWu0fn6upGX7yI%2BY%2BnWE7INKUtFjwAUDQ1VvQ%2F%2FKA6C5nLCNr%2Fw%2BQw0hAN57AYqAFOlkwgwdd1O3mjeYvNiBhv0k5OmCJDIIrw4dbp1NqmZ&X-Amz-Signature=7fb65e3a7be96176cde78dc4fda2aadb1f73c2affaa4b9bdb3efcd4a82e7df7f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y6GBXKYD%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJGMEQCIHASz15BzZiql7wI4MXrYXewkBnYoxNmrIg%2FeNlfSVx1AiAexkJ3YfR0Yuz08lyWRtuE6x4ctNfj6WQ19hLcT2OUTyr%2FAwg1EAAaDDYzNzQyMzE4MzgwNSIMxI8bh55Nl5P3doEJKtwDRTDTGE8ZLp5lFYEYdDDSYq5zdEBC%2FsIG84%2FON3XK1uiQayM%2FN4CcIu5bMvs7KxULZ%2FbgoGUWKj%2FntYy3CRm2OURRw%2FuPxQw91RZvG1%2F0BWbeEZYu%2FRQA4kPs4HkFWbNJXxr7KvUAJDzX7EaPTAIQF6Pl87CKLfKASK730LXpa5VZsZyP3GL%2B0C1iqarwZYxhbutkrHWGFsxXgHXybLct0gVBzYk%2FHPM3d1sZHmAXKqPVUFpcSoYQrygBJDP3pICEYTc6I408iPa5m1iaKaMNq%2B0vfIuTdV8xsx3L63Bt%2BJcPfl14PEERXbyJZ81tT39k2Sn0uA%2BZDlFj0T1CdS77mdlJkXEquZ%2B8MmK6qnist1TSKJIVfRg3jQq4oBiu4T%2FPYi5Dq5TI40CFvCLrqKIqffPpg4cWNYs9VAhNXA4ULh6TqWXH4V94a8zxa4YiLcXcfJxwEkb%2BmPA82VtBLcog9TTvDKP3eTPol2su8hMt9QMAouQQMyHmn3C5qg4gEmSwLdDJ2HeuvdUCFc3bQDQtmtWuAf41n%2BY5pk4OsoFisMcMHeVGF45amzUB0H4EH3os5r5E41snlWbSuyhu5KnGWasXeILkEs7jffX%2B282vJuqQmUSWbi4uU%2FPtdGcwk92JvQY6pgHvuSPK3NKKycQxL7mqz1boJyaFqo%2FzTGO0jGvE0%2FRNucKHI%2BFC3lpb%2FrEbmaF42K1Rl3FS9LtiQX0Hn0yDNOWGf9yOVLBNodBxYSXBa%2Fgzc%2BoFhFm3%2FDaDVbGpwiC9Me2VzShoWvHpglDfW37TTDgsag%2FQ6UJ3MBQytYpaZGs7kzwqVOyJhyUTThcAefa0GXPKKTHWuhWcIryre34pVGl%2BuKBkEygN&X-Amz-Signature=9b92d2ddb470b6c113fc1bc9cfa1dd5775244e4e011a4ae7826156ce47ef5be0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y2ZRCONJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJGMEQCIDDaqqmLgsMWHZ1RhWRb8H29wJXFYr62GNFIts8Pm%2BDSAiAq9UUvWvRYAjUdODe46csr%2FjBMiRoB%2BRXcvqcam%2FVTlSr%2FAwg1EAAaDDYzNzQyMzE4MzgwNSIMnWjJYmBVdPgKslTeKtwDhza%2Fl2Csujiir7ZXx0PVDm73m6fMgJRFnn8tvJqJIQTEdg2tZe%2B0%2FEBp2Qm3ftDNUpa2Lt2f5ZqNGoXG5H%2BsEmeT4jREzmSfn1MdbIVOa38oYHXZaXQhWFcW2gYW4dtwAFdGlI7XqyPwP%2BoAYeJsAkDSmfa4uqQk%2Byui9s5LYReFKgWWPhv8nuwSoangfwfOfdxBw3HfZcmAvq28LwqgT3BLIvfNOV%2FJWwBOPcicAHzjrRgMnvR%2BnxI6kY0aeI5GFqb1UqauriWeyHFA%2Fj61dd%2BJiVG4MGTAdTQdlWOryaksKTs%2BbNs5c%2Fzz5eVSLqjafaKKQPMIqinVLD%2BYnj50rTLPkvw%2FXSaTDWxQDLVOUrMeAzAqV3ykFDpvB6hoEKf20MxIoel3gCYe0FVcv19xWDeftczEoz2Yle0s2hmhKaYr61xfU1nMu19pgbeNcPlikcfT5vrxJYeopTR0d1ziwMJt4I3N2W5RrGzL9ytzZlAsHcN43km2Z1eKCCLxlpm1MylLcAwiH%2F9H2BUr7iDmsNoVzOqV4dMpHH8PeP%2BnhWg9bmIXmNf3M%2B6eOptIjzkMXnR00L1fCI%2BB8kxyEzqBhBBWiY53IqQsImVrb5Z5U6hquCzzEYbT6Iy9InYw8dyJvQY6pgGqJ9onYvyjrfuVPHVIYTZOUijfBx3UQF3Wsoc%2B2ar9YWhXtrp3CydGJl%2Bl6fkS0FE2yOWM9R385VYNd5bhh36qL%2BCBu0X78UgTMnLWotK%2FaM7PC5llPDWu0fn6upGX7yI%2BY%2BnWE7INKUtFjwAUDQ1VvQ%2F%2FKA6C5nLCNr%2Fw%2BQw0hAN57AYqAFOlkwgwdd1O3mjeYvNiBhv0k5OmCJDIIrw4dbp1NqmZ&X-Amz-Signature=30f4c4aa602aecfe0950679d8c404a506589a0125efc87d3653b361e3680addf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y2ZRCONJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJGMEQCIDDaqqmLgsMWHZ1RhWRb8H29wJXFYr62GNFIts8Pm%2BDSAiAq9UUvWvRYAjUdODe46csr%2FjBMiRoB%2BRXcvqcam%2FVTlSr%2FAwg1EAAaDDYzNzQyMzE4MzgwNSIMnWjJYmBVdPgKslTeKtwDhza%2Fl2Csujiir7ZXx0PVDm73m6fMgJRFnn8tvJqJIQTEdg2tZe%2B0%2FEBp2Qm3ftDNUpa2Lt2f5ZqNGoXG5H%2BsEmeT4jREzmSfn1MdbIVOa38oYHXZaXQhWFcW2gYW4dtwAFdGlI7XqyPwP%2BoAYeJsAkDSmfa4uqQk%2Byui9s5LYReFKgWWPhv8nuwSoangfwfOfdxBw3HfZcmAvq28LwqgT3BLIvfNOV%2FJWwBOPcicAHzjrRgMnvR%2BnxI6kY0aeI5GFqb1UqauriWeyHFA%2Fj61dd%2BJiVG4MGTAdTQdlWOryaksKTs%2BbNs5c%2Fzz5eVSLqjafaKKQPMIqinVLD%2BYnj50rTLPkvw%2FXSaTDWxQDLVOUrMeAzAqV3ykFDpvB6hoEKf20MxIoel3gCYe0FVcv19xWDeftczEoz2Yle0s2hmhKaYr61xfU1nMu19pgbeNcPlikcfT5vrxJYeopTR0d1ziwMJt4I3N2W5RrGzL9ytzZlAsHcN43km2Z1eKCCLxlpm1MylLcAwiH%2F9H2BUr7iDmsNoVzOqV4dMpHH8PeP%2BnhWg9bmIXmNf3M%2B6eOptIjzkMXnR00L1fCI%2BB8kxyEzqBhBBWiY53IqQsImVrb5Z5U6hquCzzEYbT6Iy9InYw8dyJvQY6pgGqJ9onYvyjrfuVPHVIYTZOUijfBx3UQF3Wsoc%2B2ar9YWhXtrp3CydGJl%2Bl6fkS0FE2yOWM9R385VYNd5bhh36qL%2BCBu0X78UgTMnLWotK%2FaM7PC5llPDWu0fn6upGX7yI%2BY%2BnWE7INKUtFjwAUDQ1VvQ%2F%2FKA6C5nLCNr%2Fw%2BQw0hAN57AYqAFOlkwgwdd1O3mjeYvNiBhv0k5OmCJDIIrw4dbp1NqmZ&X-Amz-Signature=f0a013265473f086d13fd4a5cc3f3e7f2d0244f5d639d4727d8d511c8a1f88da&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y2ZRCONJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJGMEQCIDDaqqmLgsMWHZ1RhWRb8H29wJXFYr62GNFIts8Pm%2BDSAiAq9UUvWvRYAjUdODe46csr%2FjBMiRoB%2BRXcvqcam%2FVTlSr%2FAwg1EAAaDDYzNzQyMzE4MzgwNSIMnWjJYmBVdPgKslTeKtwDhza%2Fl2Csujiir7ZXx0PVDm73m6fMgJRFnn8tvJqJIQTEdg2tZe%2B0%2FEBp2Qm3ftDNUpa2Lt2f5ZqNGoXG5H%2BsEmeT4jREzmSfn1MdbIVOa38oYHXZaXQhWFcW2gYW4dtwAFdGlI7XqyPwP%2BoAYeJsAkDSmfa4uqQk%2Byui9s5LYReFKgWWPhv8nuwSoangfwfOfdxBw3HfZcmAvq28LwqgT3BLIvfNOV%2FJWwBOPcicAHzjrRgMnvR%2BnxI6kY0aeI5GFqb1UqauriWeyHFA%2Fj61dd%2BJiVG4MGTAdTQdlWOryaksKTs%2BbNs5c%2Fzz5eVSLqjafaKKQPMIqinVLD%2BYnj50rTLPkvw%2FXSaTDWxQDLVOUrMeAzAqV3ykFDpvB6hoEKf20MxIoel3gCYe0FVcv19xWDeftczEoz2Yle0s2hmhKaYr61xfU1nMu19pgbeNcPlikcfT5vrxJYeopTR0d1ziwMJt4I3N2W5RrGzL9ytzZlAsHcN43km2Z1eKCCLxlpm1MylLcAwiH%2F9H2BUr7iDmsNoVzOqV4dMpHH8PeP%2BnhWg9bmIXmNf3M%2B6eOptIjzkMXnR00L1fCI%2BB8kxyEzqBhBBWiY53IqQsImVrb5Z5U6hquCzzEYbT6Iy9InYw8dyJvQY6pgGqJ9onYvyjrfuVPHVIYTZOUijfBx3UQF3Wsoc%2B2ar9YWhXtrp3CydGJl%2Bl6fkS0FE2yOWM9R385VYNd5bhh36qL%2BCBu0X78UgTMnLWotK%2FaM7PC5llPDWu0fn6upGX7yI%2BY%2BnWE7INKUtFjwAUDQ1VvQ%2F%2FKA6C5nLCNr%2Fw%2BQw0hAN57AYqAFOlkwgwdd1O3mjeYvNiBhv0k5OmCJDIIrw4dbp1NqmZ&X-Amz-Signature=51fab59a2b712dbc41d93aa8fa4f92d0df45570ac05ac26c09c110691a558d4d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y2ZRCONJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJGMEQCIDDaqqmLgsMWHZ1RhWRb8H29wJXFYr62GNFIts8Pm%2BDSAiAq9UUvWvRYAjUdODe46csr%2FjBMiRoB%2BRXcvqcam%2FVTlSr%2FAwg1EAAaDDYzNzQyMzE4MzgwNSIMnWjJYmBVdPgKslTeKtwDhza%2Fl2Csujiir7ZXx0PVDm73m6fMgJRFnn8tvJqJIQTEdg2tZe%2B0%2FEBp2Qm3ftDNUpa2Lt2f5ZqNGoXG5H%2BsEmeT4jREzmSfn1MdbIVOa38oYHXZaXQhWFcW2gYW4dtwAFdGlI7XqyPwP%2BoAYeJsAkDSmfa4uqQk%2Byui9s5LYReFKgWWPhv8nuwSoangfwfOfdxBw3HfZcmAvq28LwqgT3BLIvfNOV%2FJWwBOPcicAHzjrRgMnvR%2BnxI6kY0aeI5GFqb1UqauriWeyHFA%2Fj61dd%2BJiVG4MGTAdTQdlWOryaksKTs%2BbNs5c%2Fzz5eVSLqjafaKKQPMIqinVLD%2BYnj50rTLPkvw%2FXSaTDWxQDLVOUrMeAzAqV3ykFDpvB6hoEKf20MxIoel3gCYe0FVcv19xWDeftczEoz2Yle0s2hmhKaYr61xfU1nMu19pgbeNcPlikcfT5vrxJYeopTR0d1ziwMJt4I3N2W5RrGzL9ytzZlAsHcN43km2Z1eKCCLxlpm1MylLcAwiH%2F9H2BUr7iDmsNoVzOqV4dMpHH8PeP%2BnhWg9bmIXmNf3M%2B6eOptIjzkMXnR00L1fCI%2BB8kxyEzqBhBBWiY53IqQsImVrb5Z5U6hquCzzEYbT6Iy9InYw8dyJvQY6pgGqJ9onYvyjrfuVPHVIYTZOUijfBx3UQF3Wsoc%2B2ar9YWhXtrp3CydGJl%2Bl6fkS0FE2yOWM9R385VYNd5bhh36qL%2BCBu0X78UgTMnLWotK%2FaM7PC5llPDWu0fn6upGX7yI%2BY%2BnWE7INKUtFjwAUDQ1VvQ%2F%2FKA6C5nLCNr%2Fw%2BQw0hAN57AYqAFOlkwgwdd1O3mjeYvNiBhv0k5OmCJDIIrw4dbp1NqmZ&X-Amz-Signature=83d1f8687a583687905399b66a8cbea599f15380e3db57b27395900021155f56&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y2ZRCONJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJGMEQCIDDaqqmLgsMWHZ1RhWRb8H29wJXFYr62GNFIts8Pm%2BDSAiAq9UUvWvRYAjUdODe46csr%2FjBMiRoB%2BRXcvqcam%2FVTlSr%2FAwg1EAAaDDYzNzQyMzE4MzgwNSIMnWjJYmBVdPgKslTeKtwDhza%2Fl2Csujiir7ZXx0PVDm73m6fMgJRFnn8tvJqJIQTEdg2tZe%2B0%2FEBp2Qm3ftDNUpa2Lt2f5ZqNGoXG5H%2BsEmeT4jREzmSfn1MdbIVOa38oYHXZaXQhWFcW2gYW4dtwAFdGlI7XqyPwP%2BoAYeJsAkDSmfa4uqQk%2Byui9s5LYReFKgWWPhv8nuwSoangfwfOfdxBw3HfZcmAvq28LwqgT3BLIvfNOV%2FJWwBOPcicAHzjrRgMnvR%2BnxI6kY0aeI5GFqb1UqauriWeyHFA%2Fj61dd%2BJiVG4MGTAdTQdlWOryaksKTs%2BbNs5c%2Fzz5eVSLqjafaKKQPMIqinVLD%2BYnj50rTLPkvw%2FXSaTDWxQDLVOUrMeAzAqV3ykFDpvB6hoEKf20MxIoel3gCYe0FVcv19xWDeftczEoz2Yle0s2hmhKaYr61xfU1nMu19pgbeNcPlikcfT5vrxJYeopTR0d1ziwMJt4I3N2W5RrGzL9ytzZlAsHcN43km2Z1eKCCLxlpm1MylLcAwiH%2F9H2BUr7iDmsNoVzOqV4dMpHH8PeP%2BnhWg9bmIXmNf3M%2B6eOptIjzkMXnR00L1fCI%2BB8kxyEzqBhBBWiY53IqQsImVrb5Z5U6hquCzzEYbT6Iy9InYw8dyJvQY6pgGqJ9onYvyjrfuVPHVIYTZOUijfBx3UQF3Wsoc%2B2ar9YWhXtrp3CydGJl%2Bl6fkS0FE2yOWM9R385VYNd5bhh36qL%2BCBu0X78UgTMnLWotK%2FaM7PC5llPDWu0fn6upGX7yI%2BY%2BnWE7INKUtFjwAUDQ1VvQ%2F%2FKA6C5nLCNr%2Fw%2BQw0hAN57AYqAFOlkwgwdd1O3mjeYvNiBhv0k5OmCJDIIrw4dbp1NqmZ&X-Amz-Signature=f30cef7d1a93ab84a9c141066ed7f6afbb32d674dfff45624d4197191119b5cf&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
