

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UY3BXDY3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIDHie5vUwBQVuohwn6lI2dA2PJHiP9jvs%2BpGI%2FFxhjyiAiEAjqOKiNeGnPZO9SlcxyYH10h2YWnMVsXY%2FXdmobDFE4wq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDMhMTgpoEVQeg0Cy6ircA%2BTbHFxUMOB7jkUOG7rGkAXsdAiQPbbVydp5mWQLISxTlFuZNDC%2FkT6ja7UbnL3dEWGH9LpHW5XDXSDHXgiWvODn2ihqEGYVnhycvgMUb6gjZjH2ArwnBgaU0Sv9woyRq9d8Iec%2BnD1bFAAz%2BxG%2FfPCMBdV7RGeaAG%2BPoKI1N%2Fbgi%2BUthd0lCxx14RowU7Wl4g%2BgyEUu59Fo2OINErhnIvIQqk1M1qYb0GAJUQcdZQEWROdVO%2FP91B%2FVIvXGfLsT5uEopE19b6Vx6awkSOQFSFY%2BpNFfNHzDRXFxiBRQFpMJwgZKnINPBt1uBQSLqXnYvGwapusMFvct0Y%2FysbYr42YaIqwlBpRyE2O%2BlPkID1IRoj5piiK085xDDeq3W1KzlAhpcIdLgvPshUQC4ZznWT9TikHond%2BdKlLbLL1tT2dazyQ6TzhFygbsv3YW8CRODF7I5DxQK0v0LdG1xpcBqSnYkBTvMRqDvNgktLMdFAXmldWMcYjTOK9FtCcDXjMcc0E11T58Wh67HR7ivHpAmJYwK6ZzNQnsCQrMblsbdejMOC%2BJddfxcAUG1r3uquzBqFIoMaX5UGZjGcABS6QXc0rVVIMzlJ6gxt2dXA0tyftAQRkZBfmcbbWG68AsMKWalb0GOqUBqCaqbvL95lfzHnKhFbLplFoW%2BK0o7tZggzL8%2FXOORZeArFNha4lM95A4C%2B%2FcQqmm3nMwus7PV1yKRTkO3TAVWGQjnDZDNGIbPzkQzaNue2TFlfLVRbRWSWH10hruRuv0Sxw3I3f3FCRDaBZnYsSkjuFBNfHtdhDYW09druy0%2BDFqdSqskaOBnfLbXD1gkALPSskNuq0vJTGqo8TMOLGYnkytIHgf&X-Amz-Signature=7548b139e7a4c34620da0bacdc071cd4d02841fe365c11edbef468c984945d62&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UY3BXDY3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIDHie5vUwBQVuohwn6lI2dA2PJHiP9jvs%2BpGI%2FFxhjyiAiEAjqOKiNeGnPZO9SlcxyYH10h2YWnMVsXY%2FXdmobDFE4wq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDMhMTgpoEVQeg0Cy6ircA%2BTbHFxUMOB7jkUOG7rGkAXsdAiQPbbVydp5mWQLISxTlFuZNDC%2FkT6ja7UbnL3dEWGH9LpHW5XDXSDHXgiWvODn2ihqEGYVnhycvgMUb6gjZjH2ArwnBgaU0Sv9woyRq9d8Iec%2BnD1bFAAz%2BxG%2FfPCMBdV7RGeaAG%2BPoKI1N%2Fbgi%2BUthd0lCxx14RowU7Wl4g%2BgyEUu59Fo2OINErhnIvIQqk1M1qYb0GAJUQcdZQEWROdVO%2FP91B%2FVIvXGfLsT5uEopE19b6Vx6awkSOQFSFY%2BpNFfNHzDRXFxiBRQFpMJwgZKnINPBt1uBQSLqXnYvGwapusMFvct0Y%2FysbYr42YaIqwlBpRyE2O%2BlPkID1IRoj5piiK085xDDeq3W1KzlAhpcIdLgvPshUQC4ZznWT9TikHond%2BdKlLbLL1tT2dazyQ6TzhFygbsv3YW8CRODF7I5DxQK0v0LdG1xpcBqSnYkBTvMRqDvNgktLMdFAXmldWMcYjTOK9FtCcDXjMcc0E11T58Wh67HR7ivHpAmJYwK6ZzNQnsCQrMblsbdejMOC%2BJddfxcAUG1r3uquzBqFIoMaX5UGZjGcABS6QXc0rVVIMzlJ6gxt2dXA0tyftAQRkZBfmcbbWG68AsMKWalb0GOqUBqCaqbvL95lfzHnKhFbLplFoW%2BK0o7tZggzL8%2FXOORZeArFNha4lM95A4C%2B%2FcQqmm3nMwus7PV1yKRTkO3TAVWGQjnDZDNGIbPzkQzaNue2TFlfLVRbRWSWH10hruRuv0Sxw3I3f3FCRDaBZnYsSkjuFBNfHtdhDYW09druy0%2BDFqdSqskaOBnfLbXD1gkALPSskNuq0vJTGqo8TMOLGYnkytIHgf&X-Amz-Signature=a26f5e62bde9a714133c3738ce2060effe8974f5bcdd193581ffa8e6d683446f&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UY3BXDY3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIDHie5vUwBQVuohwn6lI2dA2PJHiP9jvs%2BpGI%2FFxhjyiAiEAjqOKiNeGnPZO9SlcxyYH10h2YWnMVsXY%2FXdmobDFE4wq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDMhMTgpoEVQeg0Cy6ircA%2BTbHFxUMOB7jkUOG7rGkAXsdAiQPbbVydp5mWQLISxTlFuZNDC%2FkT6ja7UbnL3dEWGH9LpHW5XDXSDHXgiWvODn2ihqEGYVnhycvgMUb6gjZjH2ArwnBgaU0Sv9woyRq9d8Iec%2BnD1bFAAz%2BxG%2FfPCMBdV7RGeaAG%2BPoKI1N%2Fbgi%2BUthd0lCxx14RowU7Wl4g%2BgyEUu59Fo2OINErhnIvIQqk1M1qYb0GAJUQcdZQEWROdVO%2FP91B%2FVIvXGfLsT5uEopE19b6Vx6awkSOQFSFY%2BpNFfNHzDRXFxiBRQFpMJwgZKnINPBt1uBQSLqXnYvGwapusMFvct0Y%2FysbYr42YaIqwlBpRyE2O%2BlPkID1IRoj5piiK085xDDeq3W1KzlAhpcIdLgvPshUQC4ZznWT9TikHond%2BdKlLbLL1tT2dazyQ6TzhFygbsv3YW8CRODF7I5DxQK0v0LdG1xpcBqSnYkBTvMRqDvNgktLMdFAXmldWMcYjTOK9FtCcDXjMcc0E11T58Wh67HR7ivHpAmJYwK6ZzNQnsCQrMblsbdejMOC%2BJddfxcAUG1r3uquzBqFIoMaX5UGZjGcABS6QXc0rVVIMzlJ6gxt2dXA0tyftAQRkZBfmcbbWG68AsMKWalb0GOqUBqCaqbvL95lfzHnKhFbLplFoW%2BK0o7tZggzL8%2FXOORZeArFNha4lM95A4C%2B%2FcQqmm3nMwus7PV1yKRTkO3TAVWGQjnDZDNGIbPzkQzaNue2TFlfLVRbRWSWH10hruRuv0Sxw3I3f3FCRDaBZnYsSkjuFBNfHtdhDYW09druy0%2BDFqdSqskaOBnfLbXD1gkALPSskNuq0vJTGqo8TMOLGYnkytIHgf&X-Amz-Signature=e19dde22c444e05ee6432f9e879cd2d2ba0b2cda22811612008e80edb68a1d16&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666MGLM3Y3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQDPI2vR3xz1mgxaH5JQFY%2Beel8cUK9DiQ8iu8G1EIDgbAIhAMZ%2Btdv6VnjgfVa1cocVjktss5WkVHjle4ybQkc1%2BmRvKv8DCGkQABoMNjM3NDIzMTgzODA1IgwmC9hxo7QMZTgfc40q3AOKtTQXdRE2ueKR0l4tWR1vYjmzLxFqiq9yce3Y5WhrFfhbYRLObeu%2F3UGjm3CSU7tzZkbNs3gx3HhbmjXCbryJUUPqX89zfrXyjwnkxuE3tl8ud8wAEKYrsh%2BRFnJAFHb%2BY7pIg6ByrkuusA9n3k%2BCl35%2BYC6ZYFCU11inHRiwUhzGuZe7sswEJuW9qUq5NXIEutXAH00L8gL52B4yIw98Q8SFcjeGjP22r6TddNW6RAeN7tj5notnjeZpxQSZAgR667sp1NIVJcej0XkhA%2BtpNMPpprUY2nl%2FI7hW8v%2Fw6%2F6mEwyaQsdbJdrlnIZuPIn2rvkdp97GXbcbSM41ZQeLN8I34shh3YLAy8SEG%2BLGq4YO4i1plbVrUPSfo337grFrgKiqNzS8BmF2%2BBM8PV8Fk%2BhCzVx2IOwskoye7fXoCxYF4d5sfFJHzBCWfFbYvsTG19LkAbdzTqvgVBNZ5RL8jOBFOIwTqyLsnRXB1Is4%2FUH6AOpfWmBnJwzilV78L9hZGcRxT5FZQhg%2B6SMigzxPHj%2FX%2BWES1WkTQvjHZp3%2B%2Bqm7XfPynQh%2FTy0RN2UlGG7gqonexfRsoQRL47MGtvns88GSaK%2BzefnhaiWKh7xRqDJRU61LHoAFHWVL7jD0mZW9BjqkASTwW9QDbkXlNKgyHPH1axZoFO2jFcuOI1fxa6zPi%2ByoZdEyi7JEMW2gKfEeM76GSQ6aVsdE%2B8HBwRf52wbGqT4s4OabONdtrAQdOscm6DG%2FdVYYOzeuEQV2gOJfyHN7UlCDYgKzsMt9%2BX%2B%2FLiQDUss7pLQbqv0U9Lknbps%2BrsDSRpoFyOpMv63H%2BSXwUTWjVNQjikF11ofYYJJKKT%2BXECGXUzii&X-Amz-Signature=7b0ec2b38cc423970f071a4ecd934e5c6d2adfee3c1b9cd8cbf5a0650a74ef74&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y5LQQADF%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024509Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJGMEQCIAmeQ1pxwjiIDgeK8EsroFU3ZKmP1uRqJCEOtRk5fHoSAiBstXHHFoSMikePSKXhKoMXhD4h1vCGiEHTeTuGtfpdfir%2FAwhpEAAaDDYzNzQyMzE4MzgwNSIM6fxkTV4ANoL3wspaKtwDfqIJp36IiMwHv3pthI4L%2B%2FDO7LeZETwMqL1b9fi97cP42KvSLR50OPG2%2FZ5vJp2aUHn016wJLNS1XJlQ2G4U%2Fw2JVlUCCsaLFrQPQMDOQQhxTp1g44gmRdl2%2F%2Bku7ls8JtL1wI0Q2ao1o9U4rcaVtYze5JWPCthrWRsNfLW0G7axP62dn37KVlPgfUJJXyMJw28JppuqyoZ4wCdxCmMSrUeZaR%2BhaMER4fGa%2F%2FoOybGLGvS5KoxAbfhmqikaku6Q6SDPZdMYF8FLZfV%2FtZF35gaWCju7KKoY0xJSYptrpM6CKRNteSzp6HlYPMKtuzLX5LiVT90SushyfDCxYEwo7LS4zOOk2Kjlz2tl0CSxuHDA2UvBftKmTOmEpsqDyMmT0jToDYh1HnCtKrBu4ptoZk3zGiVbgjZrbbaLZGS8cS%2FsGPGJjC08av2DXvYhwkVY%2BKKWYOPbiGheYbDa8xPeZY99oZWxbotGtFNMnPuExtmGmgjKekvCmuzSCFaW81F3eGOd6p18IchGSDrn6DBmFuLIMVSEi70WT93K5xpslGuwvrTGdtQvpFPMuHpgmFRHxt9OksrzHcYwaqWn%2BRE%2Ff15R%2BgZ8Sk1HKCNgESLGsfvA17tzkVD0juoF0Igw25mVvQY6pgH3ImOz3QJAbMizIj2GHh4JwQ2cK2Vg1%2B%2BcandTwrnZKcZdJB9gKd6t3h4Y32cAcuAboErf7GLq3ZHGOUsy9jMO0XBJxCz%2BBpWIBfhzoWwIPMZx7PNbmYiefUABGS7r4Luole3bJ3s%2Fp%2FcYSED9j9odmjVdTWDeYEoQirTdX6786LKEF9A%2FIo%2FoTaz4J9JL%2FAoRyN2jVxYdA9JJ%2B7Lg7x4bTURZnCJ0&X-Amz-Signature=1f28887e0740bb6ea368605615e47d34b107f29a7d153ac7f6a81d73dcc8a813&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UY3BXDY3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024509Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIDHie5vUwBQVuohwn6lI2dA2PJHiP9jvs%2BpGI%2FFxhjyiAiEAjqOKiNeGnPZO9SlcxyYH10h2YWnMVsXY%2FXdmobDFE4wq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDMhMTgpoEVQeg0Cy6ircA%2BTbHFxUMOB7jkUOG7rGkAXsdAiQPbbVydp5mWQLISxTlFuZNDC%2FkT6ja7UbnL3dEWGH9LpHW5XDXSDHXgiWvODn2ihqEGYVnhycvgMUb6gjZjH2ArwnBgaU0Sv9woyRq9d8Iec%2BnD1bFAAz%2BxG%2FfPCMBdV7RGeaAG%2BPoKI1N%2Fbgi%2BUthd0lCxx14RowU7Wl4g%2BgyEUu59Fo2OINErhnIvIQqk1M1qYb0GAJUQcdZQEWROdVO%2FP91B%2FVIvXGfLsT5uEopE19b6Vx6awkSOQFSFY%2BpNFfNHzDRXFxiBRQFpMJwgZKnINPBt1uBQSLqXnYvGwapusMFvct0Y%2FysbYr42YaIqwlBpRyE2O%2BlPkID1IRoj5piiK085xDDeq3W1KzlAhpcIdLgvPshUQC4ZznWT9TikHond%2BdKlLbLL1tT2dazyQ6TzhFygbsv3YW8CRODF7I5DxQK0v0LdG1xpcBqSnYkBTvMRqDvNgktLMdFAXmldWMcYjTOK9FtCcDXjMcc0E11T58Wh67HR7ivHpAmJYwK6ZzNQnsCQrMblsbdejMOC%2BJddfxcAUG1r3uquzBqFIoMaX5UGZjGcABS6QXc0rVVIMzlJ6gxt2dXA0tyftAQRkZBfmcbbWG68AsMKWalb0GOqUBqCaqbvL95lfzHnKhFbLplFoW%2BK0o7tZggzL8%2FXOORZeArFNha4lM95A4C%2B%2FcQqmm3nMwus7PV1yKRTkO3TAVWGQjnDZDNGIbPzkQzaNue2TFlfLVRbRWSWH10hruRuv0Sxw3I3f3FCRDaBZnYsSkjuFBNfHtdhDYW09druy0%2BDFqdSqskaOBnfLbXD1gkALPSskNuq0vJTGqo8TMOLGYnkytIHgf&X-Amz-Signature=8ec7d335ed4b4aa59aadc0aec6863cb1580731031c8a805df49a682dc31229fe&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UY3BXDY3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024509Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIDHie5vUwBQVuohwn6lI2dA2PJHiP9jvs%2BpGI%2FFxhjyiAiEAjqOKiNeGnPZO9SlcxyYH10h2YWnMVsXY%2FXdmobDFE4wq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDMhMTgpoEVQeg0Cy6ircA%2BTbHFxUMOB7jkUOG7rGkAXsdAiQPbbVydp5mWQLISxTlFuZNDC%2FkT6ja7UbnL3dEWGH9LpHW5XDXSDHXgiWvODn2ihqEGYVnhycvgMUb6gjZjH2ArwnBgaU0Sv9woyRq9d8Iec%2BnD1bFAAz%2BxG%2FfPCMBdV7RGeaAG%2BPoKI1N%2Fbgi%2BUthd0lCxx14RowU7Wl4g%2BgyEUu59Fo2OINErhnIvIQqk1M1qYb0GAJUQcdZQEWROdVO%2FP91B%2FVIvXGfLsT5uEopE19b6Vx6awkSOQFSFY%2BpNFfNHzDRXFxiBRQFpMJwgZKnINPBt1uBQSLqXnYvGwapusMFvct0Y%2FysbYr42YaIqwlBpRyE2O%2BlPkID1IRoj5piiK085xDDeq3W1KzlAhpcIdLgvPshUQC4ZznWT9TikHond%2BdKlLbLL1tT2dazyQ6TzhFygbsv3YW8CRODF7I5DxQK0v0LdG1xpcBqSnYkBTvMRqDvNgktLMdFAXmldWMcYjTOK9FtCcDXjMcc0E11T58Wh67HR7ivHpAmJYwK6ZzNQnsCQrMblsbdejMOC%2BJddfxcAUG1r3uquzBqFIoMaX5UGZjGcABS6QXc0rVVIMzlJ6gxt2dXA0tyftAQRkZBfmcbbWG68AsMKWalb0GOqUBqCaqbvL95lfzHnKhFbLplFoW%2BK0o7tZggzL8%2FXOORZeArFNha4lM95A4C%2B%2FcQqmm3nMwus7PV1yKRTkO3TAVWGQjnDZDNGIbPzkQzaNue2TFlfLVRbRWSWH10hruRuv0Sxw3I3f3FCRDaBZnYsSkjuFBNfHtdhDYW09druy0%2BDFqdSqskaOBnfLbXD1gkALPSskNuq0vJTGqo8TMOLGYnkytIHgf&X-Amz-Signature=ef23ac1b95e0d91124537af817da44912bd71e030b41dde9c0d8f8ba79849640&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UY3BXDY3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024509Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIDHie5vUwBQVuohwn6lI2dA2PJHiP9jvs%2BpGI%2FFxhjyiAiEAjqOKiNeGnPZO9SlcxyYH10h2YWnMVsXY%2FXdmobDFE4wq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDMhMTgpoEVQeg0Cy6ircA%2BTbHFxUMOB7jkUOG7rGkAXsdAiQPbbVydp5mWQLISxTlFuZNDC%2FkT6ja7UbnL3dEWGH9LpHW5XDXSDHXgiWvODn2ihqEGYVnhycvgMUb6gjZjH2ArwnBgaU0Sv9woyRq9d8Iec%2BnD1bFAAz%2BxG%2FfPCMBdV7RGeaAG%2BPoKI1N%2Fbgi%2BUthd0lCxx14RowU7Wl4g%2BgyEUu59Fo2OINErhnIvIQqk1M1qYb0GAJUQcdZQEWROdVO%2FP91B%2FVIvXGfLsT5uEopE19b6Vx6awkSOQFSFY%2BpNFfNHzDRXFxiBRQFpMJwgZKnINPBt1uBQSLqXnYvGwapusMFvct0Y%2FysbYr42YaIqwlBpRyE2O%2BlPkID1IRoj5piiK085xDDeq3W1KzlAhpcIdLgvPshUQC4ZznWT9TikHond%2BdKlLbLL1tT2dazyQ6TzhFygbsv3YW8CRODF7I5DxQK0v0LdG1xpcBqSnYkBTvMRqDvNgktLMdFAXmldWMcYjTOK9FtCcDXjMcc0E11T58Wh67HR7ivHpAmJYwK6ZzNQnsCQrMblsbdejMOC%2BJddfxcAUG1r3uquzBqFIoMaX5UGZjGcABS6QXc0rVVIMzlJ6gxt2dXA0tyftAQRkZBfmcbbWG68AsMKWalb0GOqUBqCaqbvL95lfzHnKhFbLplFoW%2BK0o7tZggzL8%2FXOORZeArFNha4lM95A4C%2B%2FcQqmm3nMwus7PV1yKRTkO3TAVWGQjnDZDNGIbPzkQzaNue2TFlfLVRbRWSWH10hruRuv0Sxw3I3f3FCRDaBZnYsSkjuFBNfHtdhDYW09druy0%2BDFqdSqskaOBnfLbXD1gkALPSskNuq0vJTGqo8TMOLGYnkytIHgf&X-Amz-Signature=dc11f5877cf5643be07618e49d2620ebfe5fb9d977e62f7083048585de3858cf&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UY3BXDY3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024509Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIDHie5vUwBQVuohwn6lI2dA2PJHiP9jvs%2BpGI%2FFxhjyiAiEAjqOKiNeGnPZO9SlcxyYH10h2YWnMVsXY%2FXdmobDFE4wq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDMhMTgpoEVQeg0Cy6ircA%2BTbHFxUMOB7jkUOG7rGkAXsdAiQPbbVydp5mWQLISxTlFuZNDC%2FkT6ja7UbnL3dEWGH9LpHW5XDXSDHXgiWvODn2ihqEGYVnhycvgMUb6gjZjH2ArwnBgaU0Sv9woyRq9d8Iec%2BnD1bFAAz%2BxG%2FfPCMBdV7RGeaAG%2BPoKI1N%2Fbgi%2BUthd0lCxx14RowU7Wl4g%2BgyEUu59Fo2OINErhnIvIQqk1M1qYb0GAJUQcdZQEWROdVO%2FP91B%2FVIvXGfLsT5uEopE19b6Vx6awkSOQFSFY%2BpNFfNHzDRXFxiBRQFpMJwgZKnINPBt1uBQSLqXnYvGwapusMFvct0Y%2FysbYr42YaIqwlBpRyE2O%2BlPkID1IRoj5piiK085xDDeq3W1KzlAhpcIdLgvPshUQC4ZznWT9TikHond%2BdKlLbLL1tT2dazyQ6TzhFygbsv3YW8CRODF7I5DxQK0v0LdG1xpcBqSnYkBTvMRqDvNgktLMdFAXmldWMcYjTOK9FtCcDXjMcc0E11T58Wh67HR7ivHpAmJYwK6ZzNQnsCQrMblsbdejMOC%2BJddfxcAUG1r3uquzBqFIoMaX5UGZjGcABS6QXc0rVVIMzlJ6gxt2dXA0tyftAQRkZBfmcbbWG68AsMKWalb0GOqUBqCaqbvL95lfzHnKhFbLplFoW%2BK0o7tZggzL8%2FXOORZeArFNha4lM95A4C%2B%2FcQqmm3nMwus7PV1yKRTkO3TAVWGQjnDZDNGIbPzkQzaNue2TFlfLVRbRWSWH10hruRuv0Sxw3I3f3FCRDaBZnYsSkjuFBNfHtdhDYW09druy0%2BDFqdSqskaOBnfLbXD1gkALPSskNuq0vJTGqo8TMOLGYnkytIHgf&X-Amz-Signature=5b654149cb4c02d40857e6f23db8edc9e194362b9e421f7294d67b05179d4b3b&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
