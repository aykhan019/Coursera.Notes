

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q43QXG5T%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041747Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIQChMxJt4a6saALfifaDAJTI4nAKHZF178MQ6cXjp8sh%2BAIgc2JVGQ0JSQailOqta%2FIN89WP6N2OHWjC%2FhSOhmQ50H8q%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDMb%2F2Zv%2F2vBsONaX%2FCrcA3orAL4hdTtYXEJ8dCrXygRIJITMMu9XpNUUhHkTKeyRGe%2FicU7fQrBdNjEtsPNJfavq7DNyS44Up8VX1R3OoCNjnxmhPWjlUTbdYJPFiYdlG999dTqyRiCOOVK1wj0eUDaLM%2FBFFwHs1o2Yb3y6yFi1xFzblI9mJaRYfes0eznMRalsRPgZC4ODKwAYceXrG9isWPWTFRzHviA%2BWZGqyYXHKqATqkfZ1W%2BcbACZ8k3eMnUMFVsmhCxuFvWscMnzQC6DKXtxh5PNrZyGBg2uBOz3VRcOCOGrM%2B59W9J%2Fn06CO1pkA58XJOGJ1eqXdTT3k63ODstEByYABJgd7kOxGXFnivvSQTaFfqrHQhhZ8sUH8%2F3hEgCK7NhIMt6VZ1AOswEqgeyzoL83B%2B7rMLQHcpfmkf66%2Bw3mYf8SlPzD0UtY0%2Fd0zVhZPN%2BFwoj%2FulrJoZH7hf%2F0xNiMMc14NWM%2FX5qFAHlhSfH4cwjZMFv2%2Bd8Nsccled0LVFbDakewbuFLJUNsKo00uZvVX1e03pe68%2BiiKFm5QFXoG%2BfAFiRavof2GtXNBWAIg6xtBoXdlykNyS3uH21M00EH5kvJnb6mqJ5UgpynV2WFiwYxH7LSKIIEwn3cwk5lSqUMGj6WMLzfkL0GOqUBCA9QZPMr%2Fw5E4tPiyaLi0chnwVQUZoWwOXnAYf8UhepUfQ%2BRE%2FeG6xour8U8YpbVdHS4oYtNZMovb%2B%2B1kY%2BxFH%2FkVjvVv1ITLW78d61%2BppOdps7C7r6weQfBZhUtZSdaIP744uHy5TPe0HZq9kxltqf5ai%2F0Wcd7V5IYbn2r%2FpP1dzKM5s9awsyWwjMtM%2FTY%2BqxRwBiqyyBvXZMmjOAgrPL5HA6%2F&X-Amz-Signature=867a8656d6c642ec00550ceb2dfbc4a523e0e25c12dc75dd4ce43e8a3789567e&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q43QXG5T%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041747Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIQChMxJt4a6saALfifaDAJTI4nAKHZF178MQ6cXjp8sh%2BAIgc2JVGQ0JSQailOqta%2FIN89WP6N2OHWjC%2FhSOhmQ50H8q%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDMb%2F2Zv%2F2vBsONaX%2FCrcA3orAL4hdTtYXEJ8dCrXygRIJITMMu9XpNUUhHkTKeyRGe%2FicU7fQrBdNjEtsPNJfavq7DNyS44Up8VX1R3OoCNjnxmhPWjlUTbdYJPFiYdlG999dTqyRiCOOVK1wj0eUDaLM%2FBFFwHs1o2Yb3y6yFi1xFzblI9mJaRYfes0eznMRalsRPgZC4ODKwAYceXrG9isWPWTFRzHviA%2BWZGqyYXHKqATqkfZ1W%2BcbACZ8k3eMnUMFVsmhCxuFvWscMnzQC6DKXtxh5PNrZyGBg2uBOz3VRcOCOGrM%2B59W9J%2Fn06CO1pkA58XJOGJ1eqXdTT3k63ODstEByYABJgd7kOxGXFnivvSQTaFfqrHQhhZ8sUH8%2F3hEgCK7NhIMt6VZ1AOswEqgeyzoL83B%2B7rMLQHcpfmkf66%2Bw3mYf8SlPzD0UtY0%2Fd0zVhZPN%2BFwoj%2FulrJoZH7hf%2F0xNiMMc14NWM%2FX5qFAHlhSfH4cwjZMFv2%2Bd8Nsccled0LVFbDakewbuFLJUNsKo00uZvVX1e03pe68%2BiiKFm5QFXoG%2BfAFiRavof2GtXNBWAIg6xtBoXdlykNyS3uH21M00EH5kvJnb6mqJ5UgpynV2WFiwYxH7LSKIIEwn3cwk5lSqUMGj6WMLzfkL0GOqUBCA9QZPMr%2Fw5E4tPiyaLi0chnwVQUZoWwOXnAYf8UhepUfQ%2BRE%2FeG6xour8U8YpbVdHS4oYtNZMovb%2B%2B1kY%2BxFH%2FkVjvVv1ITLW78d61%2BppOdps7C7r6weQfBZhUtZSdaIP744uHy5TPe0HZq9kxltqf5ai%2F0Wcd7V5IYbn2r%2FpP1dzKM5s9awsyWwjMtM%2FTY%2BqxRwBiqyyBvXZMmjOAgrPL5HA6%2F&X-Amz-Signature=7e237fa3fb79576bd517aaa3a4fc19422b50f14fac9658d98fa0fda693773a5f&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q43QXG5T%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041747Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIQChMxJt4a6saALfifaDAJTI4nAKHZF178MQ6cXjp8sh%2BAIgc2JVGQ0JSQailOqta%2FIN89WP6N2OHWjC%2FhSOhmQ50H8q%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDMb%2F2Zv%2F2vBsONaX%2FCrcA3orAL4hdTtYXEJ8dCrXygRIJITMMu9XpNUUhHkTKeyRGe%2FicU7fQrBdNjEtsPNJfavq7DNyS44Up8VX1R3OoCNjnxmhPWjlUTbdYJPFiYdlG999dTqyRiCOOVK1wj0eUDaLM%2FBFFwHs1o2Yb3y6yFi1xFzblI9mJaRYfes0eznMRalsRPgZC4ODKwAYceXrG9isWPWTFRzHviA%2BWZGqyYXHKqATqkfZ1W%2BcbACZ8k3eMnUMFVsmhCxuFvWscMnzQC6DKXtxh5PNrZyGBg2uBOz3VRcOCOGrM%2B59W9J%2Fn06CO1pkA58XJOGJ1eqXdTT3k63ODstEByYABJgd7kOxGXFnivvSQTaFfqrHQhhZ8sUH8%2F3hEgCK7NhIMt6VZ1AOswEqgeyzoL83B%2B7rMLQHcpfmkf66%2Bw3mYf8SlPzD0UtY0%2Fd0zVhZPN%2BFwoj%2FulrJoZH7hf%2F0xNiMMc14NWM%2FX5qFAHlhSfH4cwjZMFv2%2Bd8Nsccled0LVFbDakewbuFLJUNsKo00uZvVX1e03pe68%2BiiKFm5QFXoG%2BfAFiRavof2GtXNBWAIg6xtBoXdlykNyS3uH21M00EH5kvJnb6mqJ5UgpynV2WFiwYxH7LSKIIEwn3cwk5lSqUMGj6WMLzfkL0GOqUBCA9QZPMr%2Fw5E4tPiyaLi0chnwVQUZoWwOXnAYf8UhepUfQ%2BRE%2FeG6xour8U8YpbVdHS4oYtNZMovb%2B%2B1kY%2BxFH%2FkVjvVv1ITLW78d61%2BppOdps7C7r6weQfBZhUtZSdaIP744uHy5TPe0HZq9kxltqf5ai%2F0Wcd7V5IYbn2r%2FpP1dzKM5s9awsyWwjMtM%2FTY%2BqxRwBiqyyBvXZMmjOAgrPL5HA6%2F&X-Amz-Signature=35a9db85d996b3b293772b2a7109766aed39f9d0af0d1202e86ffbd23d453165&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYCTYHC6%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041748Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJIMEYCIQCRArLV6NWTY4HQIDRybWPjeM5ZzCDNiKJ%2FbKE%2FJiVwaQIhAMltL%2FXNgFBaTjuEg36xpA0LBlFUn6SQhyWbSFQtQ5ZxKv8DCFUQABoMNjM3NDIzMTgzODA1Igyo%2FOk0%2F66FqDhL1Ocq3AMjCM5TzapWWNJecXzXV2kV2x%2Bj1u%2BpXxvtSwwvlAZLljM1l1%2B%2Btykyn5lgzoKr6a6vM%2Bvj5EZlLQHrlqCe8iWxr2%2F540wf%2Fa71wYLQ1hFs6O%2FhCurJ1YHOZJBUgXbfSt7aXLkVDvDtLKPpHtyYWxjGE3aH6IljpJ2POsmEz5%2F%2BWCTai%2BnGTNhhddP06%2BX8x5wa4j99JKP6viwdLCrYpM4i34kSDWPepZfyzXmunIzufhqXaLEhmyjpyBvsJzJLQQFIO6rVIiyC5dK%2BcCzD1ORv3BESEmnbO%2BBoJzI%2FF8AyuEV78GLbWzrax8tEWDrVYG3MaXRcpFCH1BEmKGXRfZDERGXSMVtn8sLUUkQA50MFSmpE0QaBdVPeBSo3YOeHNxjMm9OlmWKpJAKqRg0YSithSRYHsF0BND4nJdc5LvW4gnxt%2Fyu%2FoWRrai0wnxRqPAvDU%2F1wYMfr0vSqtkC6S1uW7pgKB5bgW0jc5%2BkJwgtdAWaj9BBAbekuUMZVSrExcbYsuVGjumvfBTMc6JltX79OqSqS460lWpZ7v7GmJgmhhcI%2FBfSVSW0NDcNzq%2Fh%2BZt%2FkMk36GeEGZS3Ekl7Pfj4jYvQ7PCATjExofvLU7ye7Cowtth8OeDPHXoct%2FTC835C9BjqkAb4MbLGGjFnjsG361tuQpnbEG%2FDxKVd5zlH%2Bocy355fZWzLT%2BLaHgplchWpCnnn6fR9GK11sBXnaiwMCLZHjOFoRG0K0hBKLrq9nrfSA9u1amX6v7McGaxRteQfogecAnZxaMHG4o%2FXf4vhibjy4FQKbdYV8inRcMrznE2l14aEW%2BW5UaOrKDEeaseYHVpKFondnJfTUZgcmXJGhX2PSJ92A5i4x&X-Amz-Signature=72503224374e55676d825ef18ff25bd93ed005d1bce79daf01759738704798ad&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q4XNY2BL%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041748Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIQCZIVMdT9LwgTx8llOnejX%2BjxJq92Zk1I51MMZBFMryxAIgKuWQ7Jmn3Z7Gb5jOb9tFjG7Fmr2TRB8AjgKWFuJic3wq%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDId4o2NV7Hqxxh7RdircA6i%2BsCzP7YTfb3LNaI%2FhlxMB6K7XcwIzP4oB8EbzAgR54QkkSiajXKHr8nbiaUWH%2FVErLRtDFaTBSaolLepmQBrOZHr2a1KWpkIcvRNF8c1Kqz9jwnh%2BDJ3gVWh9MmJOZXpj%2F9T5dT91EBi8rxbO8YuXaytSS1wVG9tAeWk3rjQ%2FHW3SkgM4IWOKsgDsNaypsgx71sjce5q1spr7GOkjCVq1o%2Fdn9V1xWDX1IZAnLMrni91n92cvro%2BzDNZsOEWBGSRx5%2BH%2Ff3NDhQqmb9JHESZcNJF0BPv2%2FxKr8TIDaJ8RyLMm5QviZbfXN4BCWgedk%2B8YrUHtv9DLNLFev%2Fa%2F273qJz%2FCdBIvl8eBGcq%2Bq6vnd4elX7AbLyBV%2BTZ7JVZ9etjuLhkQkXSuuXFDn4Xp4ck5DgPRNRFzdGuvvhA3pw96BfZ%2BLWppXcfSVLgwjYhZ6pNwpDrfMIAQtcC0c2px9MZtyqhN5RbIS6AaWP1efw4BJS0besogJos4Cjft%2F3hjK7F6yVTvrTKMlYEwnTXZTbAGTVAoHl80jR2VH5PvHX9NMNYP2TWZeZ9%2BGL5yELk8UmHAzdq%2B53d%2F5Ffbopyh8pStc2qMYDWTQdVsZm7yuzmrmZbFusT2mPr%2BHg%2F8MLffkL0GOqUBSU%2FNUF946EtBreSSqN7Tt%2Fe%2FcXe4EtmK4jXQcbnANRopRDM%2B6cHCxU4LEjvKbjO3qqXIoKhvnoOjPpRqz%2BrCzRzrgKVX9yhmyD1lL4TMiBM%2FZw2fKQzMVIAKynRu2Y%2B0ZUTTz1H0nzaNFDXMIcbjHiKdcMbVvzquPtbf1BqK5DE%2BocF1mF%2FBRvEZNYrEQ3PtBDD0J1RsfeYnP1l084k6KRvzFmaY&X-Amz-Signature=9da200ebff405d4aa682701df0f1db18d366219cde1cd3a8839e20396bd79de5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q43QXG5T%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041747Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIQChMxJt4a6saALfifaDAJTI4nAKHZF178MQ6cXjp8sh%2BAIgc2JVGQ0JSQailOqta%2FIN89WP6N2OHWjC%2FhSOhmQ50H8q%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDMb%2F2Zv%2F2vBsONaX%2FCrcA3orAL4hdTtYXEJ8dCrXygRIJITMMu9XpNUUhHkTKeyRGe%2FicU7fQrBdNjEtsPNJfavq7DNyS44Up8VX1R3OoCNjnxmhPWjlUTbdYJPFiYdlG999dTqyRiCOOVK1wj0eUDaLM%2FBFFwHs1o2Yb3y6yFi1xFzblI9mJaRYfes0eznMRalsRPgZC4ODKwAYceXrG9isWPWTFRzHviA%2BWZGqyYXHKqATqkfZ1W%2BcbACZ8k3eMnUMFVsmhCxuFvWscMnzQC6DKXtxh5PNrZyGBg2uBOz3VRcOCOGrM%2B59W9J%2Fn06CO1pkA58XJOGJ1eqXdTT3k63ODstEByYABJgd7kOxGXFnivvSQTaFfqrHQhhZ8sUH8%2F3hEgCK7NhIMt6VZ1AOswEqgeyzoL83B%2B7rMLQHcpfmkf66%2Bw3mYf8SlPzD0UtY0%2Fd0zVhZPN%2BFwoj%2FulrJoZH7hf%2F0xNiMMc14NWM%2FX5qFAHlhSfH4cwjZMFv2%2Bd8Nsccled0LVFbDakewbuFLJUNsKo00uZvVX1e03pe68%2BiiKFm5QFXoG%2BfAFiRavof2GtXNBWAIg6xtBoXdlykNyS3uH21M00EH5kvJnb6mqJ5UgpynV2WFiwYxH7LSKIIEwn3cwk5lSqUMGj6WMLzfkL0GOqUBCA9QZPMr%2Fw5E4tPiyaLi0chnwVQUZoWwOXnAYf8UhepUfQ%2BRE%2FeG6xour8U8YpbVdHS4oYtNZMovb%2B%2B1kY%2BxFH%2FkVjvVv1ITLW78d61%2BppOdps7C7r6weQfBZhUtZSdaIP744uHy5TPe0HZq9kxltqf5ai%2F0Wcd7V5IYbn2r%2FpP1dzKM5s9awsyWwjMtM%2FTY%2BqxRwBiqyyBvXZMmjOAgrPL5HA6%2F&X-Amz-Signature=d05da48e8cf54f482498568572256d2e3d5d943d341a15ec589694993fa0d109&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q43QXG5T%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041747Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIQChMxJt4a6saALfifaDAJTI4nAKHZF178MQ6cXjp8sh%2BAIgc2JVGQ0JSQailOqta%2FIN89WP6N2OHWjC%2FhSOhmQ50H8q%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDMb%2F2Zv%2F2vBsONaX%2FCrcA3orAL4hdTtYXEJ8dCrXygRIJITMMu9XpNUUhHkTKeyRGe%2FicU7fQrBdNjEtsPNJfavq7DNyS44Up8VX1R3OoCNjnxmhPWjlUTbdYJPFiYdlG999dTqyRiCOOVK1wj0eUDaLM%2FBFFwHs1o2Yb3y6yFi1xFzblI9mJaRYfes0eznMRalsRPgZC4ODKwAYceXrG9isWPWTFRzHviA%2BWZGqyYXHKqATqkfZ1W%2BcbACZ8k3eMnUMFVsmhCxuFvWscMnzQC6DKXtxh5PNrZyGBg2uBOz3VRcOCOGrM%2B59W9J%2Fn06CO1pkA58XJOGJ1eqXdTT3k63ODstEByYABJgd7kOxGXFnivvSQTaFfqrHQhhZ8sUH8%2F3hEgCK7NhIMt6VZ1AOswEqgeyzoL83B%2B7rMLQHcpfmkf66%2Bw3mYf8SlPzD0UtY0%2Fd0zVhZPN%2BFwoj%2FulrJoZH7hf%2F0xNiMMc14NWM%2FX5qFAHlhSfH4cwjZMFv2%2Bd8Nsccled0LVFbDakewbuFLJUNsKo00uZvVX1e03pe68%2BiiKFm5QFXoG%2BfAFiRavof2GtXNBWAIg6xtBoXdlykNyS3uH21M00EH5kvJnb6mqJ5UgpynV2WFiwYxH7LSKIIEwn3cwk5lSqUMGj6WMLzfkL0GOqUBCA9QZPMr%2Fw5E4tPiyaLi0chnwVQUZoWwOXnAYf8UhepUfQ%2BRE%2FeG6xour8U8YpbVdHS4oYtNZMovb%2B%2B1kY%2BxFH%2FkVjvVv1ITLW78d61%2BppOdps7C7r6weQfBZhUtZSdaIP744uHy5TPe0HZq9kxltqf5ai%2F0Wcd7V5IYbn2r%2FpP1dzKM5s9awsyWwjMtM%2FTY%2BqxRwBiqyyBvXZMmjOAgrPL5HA6%2F&X-Amz-Signature=e2a2ec3cabe18bb5cdc3b67ab186861d2a5ffe78db4771c1e8819c8e4dd9bcfd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q43QXG5T%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041747Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIQChMxJt4a6saALfifaDAJTI4nAKHZF178MQ6cXjp8sh%2BAIgc2JVGQ0JSQailOqta%2FIN89WP6N2OHWjC%2FhSOhmQ50H8q%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDMb%2F2Zv%2F2vBsONaX%2FCrcA3orAL4hdTtYXEJ8dCrXygRIJITMMu9XpNUUhHkTKeyRGe%2FicU7fQrBdNjEtsPNJfavq7DNyS44Up8VX1R3OoCNjnxmhPWjlUTbdYJPFiYdlG999dTqyRiCOOVK1wj0eUDaLM%2FBFFwHs1o2Yb3y6yFi1xFzblI9mJaRYfes0eznMRalsRPgZC4ODKwAYceXrG9isWPWTFRzHviA%2BWZGqyYXHKqATqkfZ1W%2BcbACZ8k3eMnUMFVsmhCxuFvWscMnzQC6DKXtxh5PNrZyGBg2uBOz3VRcOCOGrM%2B59W9J%2Fn06CO1pkA58XJOGJ1eqXdTT3k63ODstEByYABJgd7kOxGXFnivvSQTaFfqrHQhhZ8sUH8%2F3hEgCK7NhIMt6VZ1AOswEqgeyzoL83B%2B7rMLQHcpfmkf66%2Bw3mYf8SlPzD0UtY0%2Fd0zVhZPN%2BFwoj%2FulrJoZH7hf%2F0xNiMMc14NWM%2FX5qFAHlhSfH4cwjZMFv2%2Bd8Nsccled0LVFbDakewbuFLJUNsKo00uZvVX1e03pe68%2BiiKFm5QFXoG%2BfAFiRavof2GtXNBWAIg6xtBoXdlykNyS3uH21M00EH5kvJnb6mqJ5UgpynV2WFiwYxH7LSKIIEwn3cwk5lSqUMGj6WMLzfkL0GOqUBCA9QZPMr%2Fw5E4tPiyaLi0chnwVQUZoWwOXnAYf8UhepUfQ%2BRE%2FeG6xour8U8YpbVdHS4oYtNZMovb%2B%2B1kY%2BxFH%2FkVjvVv1ITLW78d61%2BppOdps7C7r6weQfBZhUtZSdaIP744uHy5TPe0HZq9kxltqf5ai%2F0Wcd7V5IYbn2r%2FpP1dzKM5s9awsyWwjMtM%2FTY%2BqxRwBiqyyBvXZMmjOAgrPL5HA6%2F&X-Amz-Signature=86c2c722ca377c0eef39fa2e423fcffc5289eeeffa1f6f80d13509290a651055&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q43QXG5T%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041747Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIQChMxJt4a6saALfifaDAJTI4nAKHZF178MQ6cXjp8sh%2BAIgc2JVGQ0JSQailOqta%2FIN89WP6N2OHWjC%2FhSOhmQ50H8q%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDMb%2F2Zv%2F2vBsONaX%2FCrcA3orAL4hdTtYXEJ8dCrXygRIJITMMu9XpNUUhHkTKeyRGe%2FicU7fQrBdNjEtsPNJfavq7DNyS44Up8VX1R3OoCNjnxmhPWjlUTbdYJPFiYdlG999dTqyRiCOOVK1wj0eUDaLM%2FBFFwHs1o2Yb3y6yFi1xFzblI9mJaRYfes0eznMRalsRPgZC4ODKwAYceXrG9isWPWTFRzHviA%2BWZGqyYXHKqATqkfZ1W%2BcbACZ8k3eMnUMFVsmhCxuFvWscMnzQC6DKXtxh5PNrZyGBg2uBOz3VRcOCOGrM%2B59W9J%2Fn06CO1pkA58XJOGJ1eqXdTT3k63ODstEByYABJgd7kOxGXFnivvSQTaFfqrHQhhZ8sUH8%2F3hEgCK7NhIMt6VZ1AOswEqgeyzoL83B%2B7rMLQHcpfmkf66%2Bw3mYf8SlPzD0UtY0%2Fd0zVhZPN%2BFwoj%2FulrJoZH7hf%2F0xNiMMc14NWM%2FX5qFAHlhSfH4cwjZMFv2%2Bd8Nsccled0LVFbDakewbuFLJUNsKo00uZvVX1e03pe68%2BiiKFm5QFXoG%2BfAFiRavof2GtXNBWAIg6xtBoXdlykNyS3uH21M00EH5kvJnb6mqJ5UgpynV2WFiwYxH7LSKIIEwn3cwk5lSqUMGj6WMLzfkL0GOqUBCA9QZPMr%2Fw5E4tPiyaLi0chnwVQUZoWwOXnAYf8UhepUfQ%2BRE%2FeG6xour8U8YpbVdHS4oYtNZMovb%2B%2B1kY%2BxFH%2FkVjvVv1ITLW78d61%2BppOdps7C7r6weQfBZhUtZSdaIP744uHy5TPe0HZq9kxltqf5ai%2F0Wcd7V5IYbn2r%2FpP1dzKM5s9awsyWwjMtM%2FTY%2BqxRwBiqyyBvXZMmjOAgrPL5HA6%2F&X-Amz-Signature=3a45e99ef01a1325593683909a90b93e3de852d4dddbb79881b2592fc0215541&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
