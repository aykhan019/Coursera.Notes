

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3UJKVSK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTjnch3Mh2pEGGXypOaxdrD9KNAnoUyGeSFlJvwKbILgIgKogVNYVz98ObSg9NLYzhrGG8STojuiBsrGavvpYS0EYqiAQIwP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJO836D4U9lYdgbuNircA6SIBr53b%2BWCCxY%2FUBCNttds8X3eXApWIzQAZuWp56F%2FMiQPIx6lC2l2PYFYpl09afMb4nsjbs%2FFhPdK26TKKXXwm7WutAZivqXCye9GIjVIpy%2BqPzK6dxr%2BZVFV2vJ0K%2Fs1qek22tK5wkTgg9%2FMsIWZ9XdpInRZdI3dYsqsnfzLGuMcNTdg4bPZsIweUhHqbxU5T10omT%2BAGWq9XmobulXZwsIJIwZJr7fo44uXcrE%2FCIboeCWlrFy%2B2pTTYR2UG8rbhZ0q72qquZ7k37drZIdOq8zHaA%2FiH4fjuF7JQQhof8SsHXbeGgugUzfUEgGZ71qtmZFhlRkHX7XiVEbw2dtlB1P9rhljDqZARvmZe0PqAmmsmz7A%2BhN%2BZt8ya38ORdidhfmDiiMzOIRElzRvBJPbomiOB4oUdRZsAIUszg%2FiWO0hTA8iAlCoTHRdhNMwRpkhxfmdr8zqsvOoOnWJpv2KLTUqSTBqgr1P14xu74scIqFbh9My1qELSxRJa3uhCCTuxUtWOmTTJE8XIVk9BiJwacCK19bAP6xtI3t4mJaTByaWBb15bUr1JpHudIDcKxxqtAU7DFteU%2BD3uygQMMg6ExbjfkffiC6yoFWo1Tz%2FbRymtBORQbZlilw9MLrI87wGOqUBrPwCxAuak55zzA7NgnXGEI1vp5vOF%2FE6C7GGakSkMm3A7Nch5bZloXODMO%2FdHacD14rgLnLyBp0WhIvfhcufxf3jyhIbJNuT2eJ%2FQYR%2BJmrjJTL36fq5jo0pkK%2FhSHcyQsrpetYZ%2BE%2BW8biS3lECGV1vNv92gIkA7Du1L9pjw575I0E0sxlZwGCH%2B0P8gV7wkbRFwz46F8VtKDIKhjarRjke4RkE&X-Amz-Signature=b82476cc956dccf4b63a4b2d244af0a6a3371e5e9123c24a567c3486f7aa7c7e&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3UJKVSK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTjnch3Mh2pEGGXypOaxdrD9KNAnoUyGeSFlJvwKbILgIgKogVNYVz98ObSg9NLYzhrGG8STojuiBsrGavvpYS0EYqiAQIwP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJO836D4U9lYdgbuNircA6SIBr53b%2BWCCxY%2FUBCNttds8X3eXApWIzQAZuWp56F%2FMiQPIx6lC2l2PYFYpl09afMb4nsjbs%2FFhPdK26TKKXXwm7WutAZivqXCye9GIjVIpy%2BqPzK6dxr%2BZVFV2vJ0K%2Fs1qek22tK5wkTgg9%2FMsIWZ9XdpInRZdI3dYsqsnfzLGuMcNTdg4bPZsIweUhHqbxU5T10omT%2BAGWq9XmobulXZwsIJIwZJr7fo44uXcrE%2FCIboeCWlrFy%2B2pTTYR2UG8rbhZ0q72qquZ7k37drZIdOq8zHaA%2FiH4fjuF7JQQhof8SsHXbeGgugUzfUEgGZ71qtmZFhlRkHX7XiVEbw2dtlB1P9rhljDqZARvmZe0PqAmmsmz7A%2BhN%2BZt8ya38ORdidhfmDiiMzOIRElzRvBJPbomiOB4oUdRZsAIUszg%2FiWO0hTA8iAlCoTHRdhNMwRpkhxfmdr8zqsvOoOnWJpv2KLTUqSTBqgr1P14xu74scIqFbh9My1qELSxRJa3uhCCTuxUtWOmTTJE8XIVk9BiJwacCK19bAP6xtI3t4mJaTByaWBb15bUr1JpHudIDcKxxqtAU7DFteU%2BD3uygQMMg6ExbjfkffiC6yoFWo1Tz%2FbRymtBORQbZlilw9MLrI87wGOqUBrPwCxAuak55zzA7NgnXGEI1vp5vOF%2FE6C7GGakSkMm3A7Nch5bZloXODMO%2FdHacD14rgLnLyBp0WhIvfhcufxf3jyhIbJNuT2eJ%2FQYR%2BJmrjJTL36fq5jo0pkK%2FhSHcyQsrpetYZ%2BE%2BW8biS3lECGV1vNv92gIkA7Du1L9pjw575I0E0sxlZwGCH%2B0P8gV7wkbRFwz46F8VtKDIKhjarRjke4RkE&X-Amz-Signature=e67d0be49586b2a76b63c9857b44524cd65233fa3ef724d37ed6e060bde29388&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3UJKVSK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTjnch3Mh2pEGGXypOaxdrD9KNAnoUyGeSFlJvwKbILgIgKogVNYVz98ObSg9NLYzhrGG8STojuiBsrGavvpYS0EYqiAQIwP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJO836D4U9lYdgbuNircA6SIBr53b%2BWCCxY%2FUBCNttds8X3eXApWIzQAZuWp56F%2FMiQPIx6lC2l2PYFYpl09afMb4nsjbs%2FFhPdK26TKKXXwm7WutAZivqXCye9GIjVIpy%2BqPzK6dxr%2BZVFV2vJ0K%2Fs1qek22tK5wkTgg9%2FMsIWZ9XdpInRZdI3dYsqsnfzLGuMcNTdg4bPZsIweUhHqbxU5T10omT%2BAGWq9XmobulXZwsIJIwZJr7fo44uXcrE%2FCIboeCWlrFy%2B2pTTYR2UG8rbhZ0q72qquZ7k37drZIdOq8zHaA%2FiH4fjuF7JQQhof8SsHXbeGgugUzfUEgGZ71qtmZFhlRkHX7XiVEbw2dtlB1P9rhljDqZARvmZe0PqAmmsmz7A%2BhN%2BZt8ya38ORdidhfmDiiMzOIRElzRvBJPbomiOB4oUdRZsAIUszg%2FiWO0hTA8iAlCoTHRdhNMwRpkhxfmdr8zqsvOoOnWJpv2KLTUqSTBqgr1P14xu74scIqFbh9My1qELSxRJa3uhCCTuxUtWOmTTJE8XIVk9BiJwacCK19bAP6xtI3t4mJaTByaWBb15bUr1JpHudIDcKxxqtAU7DFteU%2BD3uygQMMg6ExbjfkffiC6yoFWo1Tz%2FbRymtBORQbZlilw9MLrI87wGOqUBrPwCxAuak55zzA7NgnXGEI1vp5vOF%2FE6C7GGakSkMm3A7Nch5bZloXODMO%2FdHacD14rgLnLyBp0WhIvfhcufxf3jyhIbJNuT2eJ%2FQYR%2BJmrjJTL36fq5jo0pkK%2FhSHcyQsrpetYZ%2BE%2BW8biS3lECGV1vNv92gIkA7Du1L9pjw575I0E0sxlZwGCH%2B0P8gV7wkbRFwz46F8VtKDIKhjarRjke4RkE&X-Amz-Signature=9f37d406f86717e07781b3e032ac62d696f3433364e8103e36a1f6eb22454cf1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YWK6UP3Z%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151404Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGbpP5ik%2BK7K7izYWS6Xp29VPgiQneIdmtHRuGxy%2FHBJAiEAu4GMUbgymMGCL30zGOE6hzs8y1IYV%2FCNwvQacmYREjQqiAQIwP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKbP2E%2Fd15%2BhyVAYaCrcA89nAH2Ro7kV0oOLLazmsvmsbbkUizbzzPHIHPl7MeMAmY%2BCacpyixz0sKwvvyS1Qa%2FmsQhWlaxB4NLr1Jf%2BtBE9SD79kCrdtAZ1VXLe6WkEMl10NbI%2BZ%2BSRu0qpVj1H10JAMEhvF%2B2M11gIklYKqaGcvkb%2FuBVY9iz6FWHZ3ZMml4yyC%2FINn84jTswi3K7rIP3mGVXoUwRED3XdeddXup5tMmyZi%2BNtYrsqazajw0NgdyXKuV%2FlkmVVEniB%2B80zyWqwPY1x9DKj52vmsFR4fFMhTRzyS%2F4s1xRnpVuvx2YtkAFAZOh6cyBNfXZKRJR9li1WjoMcaQFVxkp9hnd6AtIoAhPxqJ6Js%2FYw52lJD8jiZdF1LfzqhvLzzTwMJBvAcPFnycBHBjzV2o6FL%2FwscXTeKalGwJJ7%2FDqUSlKcDmRZ45ZIs0SoGSkQ%2Bu%2BSwwSSm%2BK5xj0KfjJ%2F3Qvi8AXYUXeL%2FjeibuQcOW5wXMyOOwOovrsTpumj5tlnLwg2CGAFRnv8g78y1o0JZn%2BRhFv%2F7XMpJZY4CcU%2B87NhbVzP0O0WuYXfQIDytRoDw15ZF3XyEGg2qD%2BtVLejOho4TeD6fKytKNjiLceD%2FC0YrDpNrpdLGqOYXzpWdeRIkHuqMJPI87wGOqUBo72gidtSe4GI2t5gtGpTiov36hrTYDLb6IoyvWVFKUmJLn8dEj%2BNL28O886ES6Nc8kTf9fdeeD5uTSRHuoTof0Uf29DQoNHzUeQcoKNyXDbzB1Cwo9SFWgaAZmFUjjm8wJFCQlaOPhWXjyDLTkPBkINYcGNyqOeU9cWweyxpoCdryuzZD26b0a3R6sDaKkCwGbcK%2FOR7iBHGWuXRpvoVW%2BvaW9YG&X-Amz-Signature=86a214abe38cf0944c5498db8d27d6ca5d98d637163746caa94ce41e720aceea&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663VQ4BVJC%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151404Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH8GMZ5YF1fad%2BQInl7KYHz%2F2rtK7n1wuvSCNE%2B96D0wAiAQQSMc5LNkfXI9WSBhMBMWKRZNtSRyRv6kWZrPZ%2FLF6CqIBAjA%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMoKle3vvllp4fRLi1KtwDBojfGxopKG5KVETK%2B5%2FZhQo41Dbd0Aj6fTc0QooBzWYjRODSD85NhDOmkxWqHLJrJY7Nbr9PJHBM2oxKkIdZVl9s%2B0n3TNd4D1QyJ%2ByMDzcp7dUX38tFwuZYi8vf9rpqh9d1cSw1eoj2gTVT5nxTMG%2BDHCZLIGFN4qZfWTtDTlzS6IQ%2FH%2FYbZoUPoWY%2FM5%2BOiyEp5j2mfeo827G%2FlOuHgiCZjnf8np%2F6viyOKBfT%2BwiVeI7hQWh364LxoqRp0KgqSHYtqpCZ3j0NwyMpOS%2FQ4W4E6zgFL93Wr4WO6TrHglQ6h2x4cyQbmFJpvpyR%2FeTAjYuSlbV84K0ARRqrLcOXw2P2BnXw9qOqHlaGyqOTR74Ya2IWwSak3qiR%2F3COhicvexaaQpfrYAhNyYOq5gSVok%2FOOGF%2F%2Bd2XiQ8MK3pAlNOPPjGaI1gZiUPXl2TNnvIa3RSQJt%2BvgTuWheYpdpzd3fDWZmmQkmSH5afSCM4bx0Hv6aOdAC9ZYq%2FI0njKDShsVbriRPcYYMTKIeX2E7ES3SOAntz81%2BE03PqDoyFFKh3mRlIre9tJVKcNp6LGgTEzTd5o0UyyVKpwhIbIxC44BuH6b3i3vnRIA5RdOrSeTi7rHQ8ZCrlm9NGSEM0w%2FsfzvAY6pgFrPVm%2Fe4RKuXz0i5KoPDUyUcyuB%2BKikWhgezoXHJO0t242jUGhohVfAvt4iJjmTzwodM%2BBMCKzTUZj5GImVkazkcGK0i4rGkfZFgA7iB4UthOGWWSAxmU2DNBO0%2F3i%2FqPK3sQyAYvLgZB7SxupVsGhx0Wko8DGkGFaA2GWPNpDgpzHe%2Fpc4oHYBr3RCEg49%2B9ThvhBqVNxQ1DSsTwmLhFFf0NbVgEi&X-Amz-Signature=59bb7b1fd0570a9d2e874714e276ba294aacc18e42e43ea04d25140957db9ec6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3UJKVSK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTjnch3Mh2pEGGXypOaxdrD9KNAnoUyGeSFlJvwKbILgIgKogVNYVz98ObSg9NLYzhrGG8STojuiBsrGavvpYS0EYqiAQIwP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJO836D4U9lYdgbuNircA6SIBr53b%2BWCCxY%2FUBCNttds8X3eXApWIzQAZuWp56F%2FMiQPIx6lC2l2PYFYpl09afMb4nsjbs%2FFhPdK26TKKXXwm7WutAZivqXCye9GIjVIpy%2BqPzK6dxr%2BZVFV2vJ0K%2Fs1qek22tK5wkTgg9%2FMsIWZ9XdpInRZdI3dYsqsnfzLGuMcNTdg4bPZsIweUhHqbxU5T10omT%2BAGWq9XmobulXZwsIJIwZJr7fo44uXcrE%2FCIboeCWlrFy%2B2pTTYR2UG8rbhZ0q72qquZ7k37drZIdOq8zHaA%2FiH4fjuF7JQQhof8SsHXbeGgugUzfUEgGZ71qtmZFhlRkHX7XiVEbw2dtlB1P9rhljDqZARvmZe0PqAmmsmz7A%2BhN%2BZt8ya38ORdidhfmDiiMzOIRElzRvBJPbomiOB4oUdRZsAIUszg%2FiWO0hTA8iAlCoTHRdhNMwRpkhxfmdr8zqsvOoOnWJpv2KLTUqSTBqgr1P14xu74scIqFbh9My1qELSxRJa3uhCCTuxUtWOmTTJE8XIVk9BiJwacCK19bAP6xtI3t4mJaTByaWBb15bUr1JpHudIDcKxxqtAU7DFteU%2BD3uygQMMg6ExbjfkffiC6yoFWo1Tz%2FbRymtBORQbZlilw9MLrI87wGOqUBrPwCxAuak55zzA7NgnXGEI1vp5vOF%2FE6C7GGakSkMm3A7Nch5bZloXODMO%2FdHacD14rgLnLyBp0WhIvfhcufxf3jyhIbJNuT2eJ%2FQYR%2BJmrjJTL36fq5jo0pkK%2FhSHcyQsrpetYZ%2BE%2BW8biS3lECGV1vNv92gIkA7Du1L9pjw575I0E0sxlZwGCH%2B0P8gV7wkbRFwz46F8VtKDIKhjarRjke4RkE&X-Amz-Signature=831a8ee4585aadef74d7af1b83f38de362eaa39860447af6d2864641a695ecd8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3UJKVSK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTjnch3Mh2pEGGXypOaxdrD9KNAnoUyGeSFlJvwKbILgIgKogVNYVz98ObSg9NLYzhrGG8STojuiBsrGavvpYS0EYqiAQIwP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJO836D4U9lYdgbuNircA6SIBr53b%2BWCCxY%2FUBCNttds8X3eXApWIzQAZuWp56F%2FMiQPIx6lC2l2PYFYpl09afMb4nsjbs%2FFhPdK26TKKXXwm7WutAZivqXCye9GIjVIpy%2BqPzK6dxr%2BZVFV2vJ0K%2Fs1qek22tK5wkTgg9%2FMsIWZ9XdpInRZdI3dYsqsnfzLGuMcNTdg4bPZsIweUhHqbxU5T10omT%2BAGWq9XmobulXZwsIJIwZJr7fo44uXcrE%2FCIboeCWlrFy%2B2pTTYR2UG8rbhZ0q72qquZ7k37drZIdOq8zHaA%2FiH4fjuF7JQQhof8SsHXbeGgugUzfUEgGZ71qtmZFhlRkHX7XiVEbw2dtlB1P9rhljDqZARvmZe0PqAmmsmz7A%2BhN%2BZt8ya38ORdidhfmDiiMzOIRElzRvBJPbomiOB4oUdRZsAIUszg%2FiWO0hTA8iAlCoTHRdhNMwRpkhxfmdr8zqsvOoOnWJpv2KLTUqSTBqgr1P14xu74scIqFbh9My1qELSxRJa3uhCCTuxUtWOmTTJE8XIVk9BiJwacCK19bAP6xtI3t4mJaTByaWBb15bUr1JpHudIDcKxxqtAU7DFteU%2BD3uygQMMg6ExbjfkffiC6yoFWo1Tz%2FbRymtBORQbZlilw9MLrI87wGOqUBrPwCxAuak55zzA7NgnXGEI1vp5vOF%2FE6C7GGakSkMm3A7Nch5bZloXODMO%2FdHacD14rgLnLyBp0WhIvfhcufxf3jyhIbJNuT2eJ%2FQYR%2BJmrjJTL36fq5jo0pkK%2FhSHcyQsrpetYZ%2BE%2BW8biS3lECGV1vNv92gIkA7Du1L9pjw575I0E0sxlZwGCH%2B0P8gV7wkbRFwz46F8VtKDIKhjarRjke4RkE&X-Amz-Signature=e1d9317507d49a00a8cbfb4245ab04ffa72ae6b46dce7173dbe4c2326288c1b4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3UJKVSK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTjnch3Mh2pEGGXypOaxdrD9KNAnoUyGeSFlJvwKbILgIgKogVNYVz98ObSg9NLYzhrGG8STojuiBsrGavvpYS0EYqiAQIwP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJO836D4U9lYdgbuNircA6SIBr53b%2BWCCxY%2FUBCNttds8X3eXApWIzQAZuWp56F%2FMiQPIx6lC2l2PYFYpl09afMb4nsjbs%2FFhPdK26TKKXXwm7WutAZivqXCye9GIjVIpy%2BqPzK6dxr%2BZVFV2vJ0K%2Fs1qek22tK5wkTgg9%2FMsIWZ9XdpInRZdI3dYsqsnfzLGuMcNTdg4bPZsIweUhHqbxU5T10omT%2BAGWq9XmobulXZwsIJIwZJr7fo44uXcrE%2FCIboeCWlrFy%2B2pTTYR2UG8rbhZ0q72qquZ7k37drZIdOq8zHaA%2FiH4fjuF7JQQhof8SsHXbeGgugUzfUEgGZ71qtmZFhlRkHX7XiVEbw2dtlB1P9rhljDqZARvmZe0PqAmmsmz7A%2BhN%2BZt8ya38ORdidhfmDiiMzOIRElzRvBJPbomiOB4oUdRZsAIUszg%2FiWO0hTA8iAlCoTHRdhNMwRpkhxfmdr8zqsvOoOnWJpv2KLTUqSTBqgr1P14xu74scIqFbh9My1qELSxRJa3uhCCTuxUtWOmTTJE8XIVk9BiJwacCK19bAP6xtI3t4mJaTByaWBb15bUr1JpHudIDcKxxqtAU7DFteU%2BD3uygQMMg6ExbjfkffiC6yoFWo1Tz%2FbRymtBORQbZlilw9MLrI87wGOqUBrPwCxAuak55zzA7NgnXGEI1vp5vOF%2FE6C7GGakSkMm3A7Nch5bZloXODMO%2FdHacD14rgLnLyBp0WhIvfhcufxf3jyhIbJNuT2eJ%2FQYR%2BJmrjJTL36fq5jo0pkK%2FhSHcyQsrpetYZ%2BE%2BW8biS3lECGV1vNv92gIkA7Du1L9pjw575I0E0sxlZwGCH%2B0P8gV7wkbRFwz46F8VtKDIKhjarRjke4RkE&X-Amz-Signature=ef6a565e6dbc029c54aa2c2cd37507a71146603a70e0fb3eb8df2212aeeb3f75&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3UJKVSK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTjnch3Mh2pEGGXypOaxdrD9KNAnoUyGeSFlJvwKbILgIgKogVNYVz98ObSg9NLYzhrGG8STojuiBsrGavvpYS0EYqiAQIwP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJO836D4U9lYdgbuNircA6SIBr53b%2BWCCxY%2FUBCNttds8X3eXApWIzQAZuWp56F%2FMiQPIx6lC2l2PYFYpl09afMb4nsjbs%2FFhPdK26TKKXXwm7WutAZivqXCye9GIjVIpy%2BqPzK6dxr%2BZVFV2vJ0K%2Fs1qek22tK5wkTgg9%2FMsIWZ9XdpInRZdI3dYsqsnfzLGuMcNTdg4bPZsIweUhHqbxU5T10omT%2BAGWq9XmobulXZwsIJIwZJr7fo44uXcrE%2FCIboeCWlrFy%2B2pTTYR2UG8rbhZ0q72qquZ7k37drZIdOq8zHaA%2FiH4fjuF7JQQhof8SsHXbeGgugUzfUEgGZ71qtmZFhlRkHX7XiVEbw2dtlB1P9rhljDqZARvmZe0PqAmmsmz7A%2BhN%2BZt8ya38ORdidhfmDiiMzOIRElzRvBJPbomiOB4oUdRZsAIUszg%2FiWO0hTA8iAlCoTHRdhNMwRpkhxfmdr8zqsvOoOnWJpv2KLTUqSTBqgr1P14xu74scIqFbh9My1qELSxRJa3uhCCTuxUtWOmTTJE8XIVk9BiJwacCK19bAP6xtI3t4mJaTByaWBb15bUr1JpHudIDcKxxqtAU7DFteU%2BD3uygQMMg6ExbjfkffiC6yoFWo1Tz%2FbRymtBORQbZlilw9MLrI87wGOqUBrPwCxAuak55zzA7NgnXGEI1vp5vOF%2FE6C7GGakSkMm3A7Nch5bZloXODMO%2FdHacD14rgLnLyBp0WhIvfhcufxf3jyhIbJNuT2eJ%2FQYR%2BJmrjJTL36fq5jo0pkK%2FhSHcyQsrpetYZ%2BE%2BW8biS3lECGV1vNv92gIkA7Du1L9pjw575I0E0sxlZwGCH%2B0P8gV7wkbRFwz46F8VtKDIKhjarRjke4RkE&X-Amz-Signature=a3b02f7b708e15826c9b4098a5d9d81dc8b458f99bf497d8113dc4eae8872276&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
