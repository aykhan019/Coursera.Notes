

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TCJ5C6YC%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA0Gqfs2kfhLSnwU2EpsTdCeEOGgoOgyNAI0eQRdA6VCAiAt6rFQgOe3zD9dobRfVc2HPIPAwShEDwpbcA8CZkOAnCqIBAiX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM6L2aHROIWGDCgfmWKtwD1hMVW81FGwui5u9mRn457vEUP2ztRyEBeyzqnKUhjM1MoyLbFlpVTVFFVwKeUiF%2FJT8E5tcBvzmLorOzy77ATwzb2mOnylsadkseVxNXztMOWajlzPhe1oLd2nJdxQpiPgPyTbFRyqBKnifOYmIPUZmwN41VD2wIxIKw6kZxCDadQkvbR0yDK0rmS858YsynPX32KrcDjNy6iV7LemMM2rOtK7AQ%2Bd1mQSz9fC5OurTLUKELKLxok8ohyx6ji8DFhTLy2Vlz1cuZeboc9oqo4oTc4nM%2FCFVqmqvSxrPh0pZ4ND3U0SsH9Em1t6j934qmn3eBx0M5T22Dnk%2BRdCvNiSNRVAbbrsRBgHmqQdpmlYPU06PMf6phFxFFt641dSbiAKrp3yK0tKhGbnHQ7qnvCXyUCsdlNcNUPwLTgM8%2B%2Fph5sIkCMAXJHIBeIHM1QPQ15CC33ioXxCdKjPyNQzqeJRvphGYjOHa%2BX%2B%2BzgwtcrBPaAPxglnEB%2Fsc6e922RkNUvSfRdN8XtVgQI76wwaOfsTWEKfWu9c1wlYW%2Fm7itjr%2Bkmsvi%2FTxgI%2FUZFd7P2BICKgqfqSKWUIXQqUXZbV8WQZmk%2Bie31h4Nqjbd6YpVysEe%2Bw0pNDqifKTQgaIwrcbqvAY6pgGoxAWhwnmAk7Pg3dc7rrlmqMG5uGzQaj6XqsPUTOwQViHxtid0gMGlk45ueEBaJ0aq1gV3gUAESn2Qt1tVFn%2FQA9VaesMpPwvCVNoSfc5sprPPI6g5dcwUzZclXz8TWkoIlHmYKv%2F6V3qIOi2d69%2BozqbJhhH1UDc1gnWm9aFZEa4Op3D6Eolli7hRHkGsXNuvIzUoiXn2Zvfuy60dFCLpv%2Fh2bmsR&X-Amz-Signature=1c5340df0cbb70938556adb681c430af3d4bbc8145652856171ffe1794f51b65&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TCJ5C6YC%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA0Gqfs2kfhLSnwU2EpsTdCeEOGgoOgyNAI0eQRdA6VCAiAt6rFQgOe3zD9dobRfVc2HPIPAwShEDwpbcA8CZkOAnCqIBAiX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM6L2aHROIWGDCgfmWKtwD1hMVW81FGwui5u9mRn457vEUP2ztRyEBeyzqnKUhjM1MoyLbFlpVTVFFVwKeUiF%2FJT8E5tcBvzmLorOzy77ATwzb2mOnylsadkseVxNXztMOWajlzPhe1oLd2nJdxQpiPgPyTbFRyqBKnifOYmIPUZmwN41VD2wIxIKw6kZxCDadQkvbR0yDK0rmS858YsynPX32KrcDjNy6iV7LemMM2rOtK7AQ%2Bd1mQSz9fC5OurTLUKELKLxok8ohyx6ji8DFhTLy2Vlz1cuZeboc9oqo4oTc4nM%2FCFVqmqvSxrPh0pZ4ND3U0SsH9Em1t6j934qmn3eBx0M5T22Dnk%2BRdCvNiSNRVAbbrsRBgHmqQdpmlYPU06PMf6phFxFFt641dSbiAKrp3yK0tKhGbnHQ7qnvCXyUCsdlNcNUPwLTgM8%2B%2Fph5sIkCMAXJHIBeIHM1QPQ15CC33ioXxCdKjPyNQzqeJRvphGYjOHa%2BX%2B%2BzgwtcrBPaAPxglnEB%2Fsc6e922RkNUvSfRdN8XtVgQI76wwaOfsTWEKfWu9c1wlYW%2Fm7itjr%2Bkmsvi%2FTxgI%2FUZFd7P2BICKgqfqSKWUIXQqUXZbV8WQZmk%2Bie31h4Nqjbd6YpVysEe%2Bw0pNDqifKTQgaIwrcbqvAY6pgGoxAWhwnmAk7Pg3dc7rrlmqMG5uGzQaj6XqsPUTOwQViHxtid0gMGlk45ueEBaJ0aq1gV3gUAESn2Qt1tVFn%2FQA9VaesMpPwvCVNoSfc5sprPPI6g5dcwUzZclXz8TWkoIlHmYKv%2F6V3qIOi2d69%2BozqbJhhH1UDc1gnWm9aFZEa4Op3D6Eolli7hRHkGsXNuvIzUoiXn2Zvfuy60dFCLpv%2Fh2bmsR&X-Amz-Signature=e8c1244faaa596d42976bf816b56cfc45747eebde5f9629038d3803f89df8b3f&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TCJ5C6YC%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA0Gqfs2kfhLSnwU2EpsTdCeEOGgoOgyNAI0eQRdA6VCAiAt6rFQgOe3zD9dobRfVc2HPIPAwShEDwpbcA8CZkOAnCqIBAiX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM6L2aHROIWGDCgfmWKtwD1hMVW81FGwui5u9mRn457vEUP2ztRyEBeyzqnKUhjM1MoyLbFlpVTVFFVwKeUiF%2FJT8E5tcBvzmLorOzy77ATwzb2mOnylsadkseVxNXztMOWajlzPhe1oLd2nJdxQpiPgPyTbFRyqBKnifOYmIPUZmwN41VD2wIxIKw6kZxCDadQkvbR0yDK0rmS858YsynPX32KrcDjNy6iV7LemMM2rOtK7AQ%2Bd1mQSz9fC5OurTLUKELKLxok8ohyx6ji8DFhTLy2Vlz1cuZeboc9oqo4oTc4nM%2FCFVqmqvSxrPh0pZ4ND3U0SsH9Em1t6j934qmn3eBx0M5T22Dnk%2BRdCvNiSNRVAbbrsRBgHmqQdpmlYPU06PMf6phFxFFt641dSbiAKrp3yK0tKhGbnHQ7qnvCXyUCsdlNcNUPwLTgM8%2B%2Fph5sIkCMAXJHIBeIHM1QPQ15CC33ioXxCdKjPyNQzqeJRvphGYjOHa%2BX%2B%2BzgwtcrBPaAPxglnEB%2Fsc6e922RkNUvSfRdN8XtVgQI76wwaOfsTWEKfWu9c1wlYW%2Fm7itjr%2Bkmsvi%2FTxgI%2FUZFd7P2BICKgqfqSKWUIXQqUXZbV8WQZmk%2Bie31h4Nqjbd6YpVysEe%2Bw0pNDqifKTQgaIwrcbqvAY6pgGoxAWhwnmAk7Pg3dc7rrlmqMG5uGzQaj6XqsPUTOwQViHxtid0gMGlk45ueEBaJ0aq1gV3gUAESn2Qt1tVFn%2FQA9VaesMpPwvCVNoSfc5sprPPI6g5dcwUzZclXz8TWkoIlHmYKv%2F6V3qIOi2d69%2BozqbJhhH1UDc1gnWm9aFZEa4Op3D6Eolli7hRHkGsXNuvIzUoiXn2Zvfuy60dFCLpv%2Fh2bmsR&X-Amz-Signature=912aece84fedec4d59cdc7ecf63cff3c416359b611128105aff4f31918562a6d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZYEM5CLG%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEP%2FGE2BvdzgLJeGEL71NRCDX%2FdT8VuJEynUNmLFkl%2FfAiEA6VsoLdDylwiNL55ODYg%2FO5QV4m9ShSkzAANUGh8ReNAqiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMuSCMaHjAEiIzYeqSrcA3OYSKKgSG7itM2762B6a%2BKWHKtwSCSNDncBumpWtfHQdikfczptESF5YFpsqZXRMCTdbKTGl2ZDaCZHjs0o3PjwyJ17iyWYXdcGp6ZzMUJlgZW9n1JaZm9Y5VMtLRZcwtnMkASFkVPqApbhOp%2BmjmHPmlABCjPvJGvEXDo3%2F7w3m6JZWoTxnVy8G49DGycxaoaIQ8KddRIciPr0hDO%2B94o0woZCrpaQz7KKgHwZZNBitvcFrISKpwexkkhXTl3ej3tXOnD6J41%2BZ1e0qKSYM6uiDvv5aR1RnOyyjMdKzExprXfQ8Nm3U32b%2FBDa59IDPRItTmqJ0aKZoiU6H%2FCj2L%2FWwL%2Bi87VC9R9laULdlpSBgWVBlXi2GNMEJ1lAa%2BVlYPrCjiRMyax95AUlfwLmj4DqiI3aRoggnnBlExGBA0Hu6DAzwSkKqph3dr3RcTc1nWqv18c1BBjnI2KJYaUcaArdKLSkKWDaSkiXaVsbpnjPdDd3kimS90K43OST1ZVBJcGVBx8th7nUYtp6AN8x3tlg9sy5CVxzYNtDIkE8kLaN6Sml2ViM7omhC1yHv9KaGyXcZg0re%2FfDsLFfeQsAX1HPjKahzirenbDXg2WP65zwMkx0Gbrwuu%2BpiBaAMOrF6rwGOqUBgsi8VSIdrBEBiLXD9GWyIq%2FJWa0ejwVjlKLz2Puv9Jx3dkenGujAGF17swjRik1uij8k6SKW%2FdcyndU4uZTKj9oLW4myltaQIwFXNlyxwVJCuh84HBDKMipIde5%2FBL%2BKNCihEBdKH120BQ1UftbRAU1DtVUVcTjYaoOtrhqPpU0KGKOW1tGhgxRCnCLkkMYltSWHU58piB%2FPjV9TScjT8y%2F0kJaf&X-Amz-Signature=d147b6ba45224d9f3f56a3a37817cf99febc03091ecfe2c6f4555fe7c7b63637&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662HWGPGYG%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEhgooiO%2BbtlXyiPgQzt9Ji9QvdfG6D8n1I%2FZOG97c41AiEAwUgAPmKcFl31IgK43UmitfjWtD3dC8LaKnEp8q4XttcqiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKkC6Ohmwy08XgUiCCrcAy%2B0cymixf7%2BIi25otb2%2FrighBcRAXs9%2Bb6zQfYobMkQ77gBGuL9Rvq2chB6Z3%2BTprPnfaskNgk8wa2ZHVwH%2BkLfK5v5DrD%2FCaJnadIbZuQe2YE%2FTQkpdXeHnqFav2qrGHrNN5NKNS1rDK74Qv7NlJL0LKZI4lvNN%2BhjHMq7ngtIws8Vt%2FXxIsRbX9lLgWLABD6EQHfuH4YV4C%2BK0W0ITbr7M1cM8%2FnwjZ%2BKGuGOv0zenLauPmyoCf%2B5neXk6tOaldyjG5CZxROfZcB6FGUAHO3ylGWD8MA060l%2FWSwL4c9mVlo3RRojIpq5vAfeCKy2MN%2BYTcEH5X7PV0EW3SyxZngtlZcPA%2F1HebnNu00W7REgm32k4l6dgX8lJfpomMYI0SaVeSthypSJsnsojgdhmkoS4iYHnCWxnRhsOfYdE20Pu4%2BLIe%2BYdBbwnnjb%2Bbl11mKNXLUvyk%2Bk1eghxVjy8NaPIgVDWqdtDObU6GAfZ%2Fl9z%2FEf8b%2B2ty1GB03v9mf%2B0a%2BMQxzzfMbEyhogblKCCVY6uGf4Bi%2BBwt1WhLroWzjw8HA%2F6s5YQKLDWVjMwZZ7tKIR0eaOSZHJSaalBGz55zIfYgthZN7Wfa%2F7DNxZlPWtYLezJ%2FLp7pFgf8%2FCMNrF6rwGOqUB1YXiZdGhYtQBCMsPGdvT4vE04Ytub7CxmRIAt9gdda8DozVtB7OCreuHK1GVRYZ3pli%2B6K7M6oPx0PYVtenljtxNkwBNTIc6wR29E5oUpeKf1pp9Q3Jm3kdKJGyja%2FVT3Xb7%2BXXwV37erMz%2FDpKrzzsGzE7BfN6F5vwdkEGT1FNCK%2BNCSuUihIxc13XQ9JBt9mtHx%2FT%2BDkCLvw2qaHBD4iHbCzro&X-Amz-Signature=be3f96402296d15cbb7656347524e3e10200d8ab9841d3c7c6ad20d5fb7dc5f0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TCJ5C6YC%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA0Gqfs2kfhLSnwU2EpsTdCeEOGgoOgyNAI0eQRdA6VCAiAt6rFQgOe3zD9dobRfVc2HPIPAwShEDwpbcA8CZkOAnCqIBAiX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM6L2aHROIWGDCgfmWKtwD1hMVW81FGwui5u9mRn457vEUP2ztRyEBeyzqnKUhjM1MoyLbFlpVTVFFVwKeUiF%2FJT8E5tcBvzmLorOzy77ATwzb2mOnylsadkseVxNXztMOWajlzPhe1oLd2nJdxQpiPgPyTbFRyqBKnifOYmIPUZmwN41VD2wIxIKw6kZxCDadQkvbR0yDK0rmS858YsynPX32KrcDjNy6iV7LemMM2rOtK7AQ%2Bd1mQSz9fC5OurTLUKELKLxok8ohyx6ji8DFhTLy2Vlz1cuZeboc9oqo4oTc4nM%2FCFVqmqvSxrPh0pZ4ND3U0SsH9Em1t6j934qmn3eBx0M5T22Dnk%2BRdCvNiSNRVAbbrsRBgHmqQdpmlYPU06PMf6phFxFFt641dSbiAKrp3yK0tKhGbnHQ7qnvCXyUCsdlNcNUPwLTgM8%2B%2Fph5sIkCMAXJHIBeIHM1QPQ15CC33ioXxCdKjPyNQzqeJRvphGYjOHa%2BX%2B%2BzgwtcrBPaAPxglnEB%2Fsc6e922RkNUvSfRdN8XtVgQI76wwaOfsTWEKfWu9c1wlYW%2Fm7itjr%2Bkmsvi%2FTxgI%2FUZFd7P2BICKgqfqSKWUIXQqUXZbV8WQZmk%2Bie31h4Nqjbd6YpVysEe%2Bw0pNDqifKTQgaIwrcbqvAY6pgGoxAWhwnmAk7Pg3dc7rrlmqMG5uGzQaj6XqsPUTOwQViHxtid0gMGlk45ueEBaJ0aq1gV3gUAESn2Qt1tVFn%2FQA9VaesMpPwvCVNoSfc5sprPPI6g5dcwUzZclXz8TWkoIlHmYKv%2F6V3qIOi2d69%2BozqbJhhH1UDc1gnWm9aFZEa4Op3D6Eolli7hRHkGsXNuvIzUoiXn2Zvfuy60dFCLpv%2Fh2bmsR&X-Amz-Signature=5ffb7723cb13580e89b464b58ac442e79ed5224c397da643ff6075b284b9d17d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TCJ5C6YC%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA0Gqfs2kfhLSnwU2EpsTdCeEOGgoOgyNAI0eQRdA6VCAiAt6rFQgOe3zD9dobRfVc2HPIPAwShEDwpbcA8CZkOAnCqIBAiX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM6L2aHROIWGDCgfmWKtwD1hMVW81FGwui5u9mRn457vEUP2ztRyEBeyzqnKUhjM1MoyLbFlpVTVFFVwKeUiF%2FJT8E5tcBvzmLorOzy77ATwzb2mOnylsadkseVxNXztMOWajlzPhe1oLd2nJdxQpiPgPyTbFRyqBKnifOYmIPUZmwN41VD2wIxIKw6kZxCDadQkvbR0yDK0rmS858YsynPX32KrcDjNy6iV7LemMM2rOtK7AQ%2Bd1mQSz9fC5OurTLUKELKLxok8ohyx6ji8DFhTLy2Vlz1cuZeboc9oqo4oTc4nM%2FCFVqmqvSxrPh0pZ4ND3U0SsH9Em1t6j934qmn3eBx0M5T22Dnk%2BRdCvNiSNRVAbbrsRBgHmqQdpmlYPU06PMf6phFxFFt641dSbiAKrp3yK0tKhGbnHQ7qnvCXyUCsdlNcNUPwLTgM8%2B%2Fph5sIkCMAXJHIBeIHM1QPQ15CC33ioXxCdKjPyNQzqeJRvphGYjOHa%2BX%2B%2BzgwtcrBPaAPxglnEB%2Fsc6e922RkNUvSfRdN8XtVgQI76wwaOfsTWEKfWu9c1wlYW%2Fm7itjr%2Bkmsvi%2FTxgI%2FUZFd7P2BICKgqfqSKWUIXQqUXZbV8WQZmk%2Bie31h4Nqjbd6YpVysEe%2Bw0pNDqifKTQgaIwrcbqvAY6pgGoxAWhwnmAk7Pg3dc7rrlmqMG5uGzQaj6XqsPUTOwQViHxtid0gMGlk45ueEBaJ0aq1gV3gUAESn2Qt1tVFn%2FQA9VaesMpPwvCVNoSfc5sprPPI6g5dcwUzZclXz8TWkoIlHmYKv%2F6V3qIOi2d69%2BozqbJhhH1UDc1gnWm9aFZEa4Op3D6Eolli7hRHkGsXNuvIzUoiXn2Zvfuy60dFCLpv%2Fh2bmsR&X-Amz-Signature=e41fcf4d0ad53561987e1a15ad7b1b182b5701965c192baba0731d21e01fd875&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TCJ5C6YC%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA0Gqfs2kfhLSnwU2EpsTdCeEOGgoOgyNAI0eQRdA6VCAiAt6rFQgOe3zD9dobRfVc2HPIPAwShEDwpbcA8CZkOAnCqIBAiX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM6L2aHROIWGDCgfmWKtwD1hMVW81FGwui5u9mRn457vEUP2ztRyEBeyzqnKUhjM1MoyLbFlpVTVFFVwKeUiF%2FJT8E5tcBvzmLorOzy77ATwzb2mOnylsadkseVxNXztMOWajlzPhe1oLd2nJdxQpiPgPyTbFRyqBKnifOYmIPUZmwN41VD2wIxIKw6kZxCDadQkvbR0yDK0rmS858YsynPX32KrcDjNy6iV7LemMM2rOtK7AQ%2Bd1mQSz9fC5OurTLUKELKLxok8ohyx6ji8DFhTLy2Vlz1cuZeboc9oqo4oTc4nM%2FCFVqmqvSxrPh0pZ4ND3U0SsH9Em1t6j934qmn3eBx0M5T22Dnk%2BRdCvNiSNRVAbbrsRBgHmqQdpmlYPU06PMf6phFxFFt641dSbiAKrp3yK0tKhGbnHQ7qnvCXyUCsdlNcNUPwLTgM8%2B%2Fph5sIkCMAXJHIBeIHM1QPQ15CC33ioXxCdKjPyNQzqeJRvphGYjOHa%2BX%2B%2BzgwtcrBPaAPxglnEB%2Fsc6e922RkNUvSfRdN8XtVgQI76wwaOfsTWEKfWu9c1wlYW%2Fm7itjr%2Bkmsvi%2FTxgI%2FUZFd7P2BICKgqfqSKWUIXQqUXZbV8WQZmk%2Bie31h4Nqjbd6YpVysEe%2Bw0pNDqifKTQgaIwrcbqvAY6pgGoxAWhwnmAk7Pg3dc7rrlmqMG5uGzQaj6XqsPUTOwQViHxtid0gMGlk45ueEBaJ0aq1gV3gUAESn2Qt1tVFn%2FQA9VaesMpPwvCVNoSfc5sprPPI6g5dcwUzZclXz8TWkoIlHmYKv%2F6V3qIOi2d69%2BozqbJhhH1UDc1gnWm9aFZEa4Op3D6Eolli7hRHkGsXNuvIzUoiXn2Zvfuy60dFCLpv%2Fh2bmsR&X-Amz-Signature=ed4e08a4e5a53bc7acf8ad4d25b4589365ba8b034159875b726401e8ed6f7fbf&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TCJ5C6YC%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA0Gqfs2kfhLSnwU2EpsTdCeEOGgoOgyNAI0eQRdA6VCAiAt6rFQgOe3zD9dobRfVc2HPIPAwShEDwpbcA8CZkOAnCqIBAiX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM6L2aHROIWGDCgfmWKtwD1hMVW81FGwui5u9mRn457vEUP2ztRyEBeyzqnKUhjM1MoyLbFlpVTVFFVwKeUiF%2FJT8E5tcBvzmLorOzy77ATwzb2mOnylsadkseVxNXztMOWajlzPhe1oLd2nJdxQpiPgPyTbFRyqBKnifOYmIPUZmwN41VD2wIxIKw6kZxCDadQkvbR0yDK0rmS858YsynPX32KrcDjNy6iV7LemMM2rOtK7AQ%2Bd1mQSz9fC5OurTLUKELKLxok8ohyx6ji8DFhTLy2Vlz1cuZeboc9oqo4oTc4nM%2FCFVqmqvSxrPh0pZ4ND3U0SsH9Em1t6j934qmn3eBx0M5T22Dnk%2BRdCvNiSNRVAbbrsRBgHmqQdpmlYPU06PMf6phFxFFt641dSbiAKrp3yK0tKhGbnHQ7qnvCXyUCsdlNcNUPwLTgM8%2B%2Fph5sIkCMAXJHIBeIHM1QPQ15CC33ioXxCdKjPyNQzqeJRvphGYjOHa%2BX%2B%2BzgwtcrBPaAPxglnEB%2Fsc6e922RkNUvSfRdN8XtVgQI76wwaOfsTWEKfWu9c1wlYW%2Fm7itjr%2Bkmsvi%2FTxgI%2FUZFd7P2BICKgqfqSKWUIXQqUXZbV8WQZmk%2Bie31h4Nqjbd6YpVysEe%2Bw0pNDqifKTQgaIwrcbqvAY6pgGoxAWhwnmAk7Pg3dc7rrlmqMG5uGzQaj6XqsPUTOwQViHxtid0gMGlk45ueEBaJ0aq1gV3gUAESn2Qt1tVFn%2FQA9VaesMpPwvCVNoSfc5sprPPI6g5dcwUzZclXz8TWkoIlHmYKv%2F6V3qIOi2d69%2BozqbJhhH1UDc1gnWm9aFZEa4Op3D6Eolli7hRHkGsXNuvIzUoiXn2Zvfuy60dFCLpv%2Fh2bmsR&X-Amz-Signature=68cf17949decda8d26b3ec7a8893fbc4b5231ca6b77f920797afa47028c0128c&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
