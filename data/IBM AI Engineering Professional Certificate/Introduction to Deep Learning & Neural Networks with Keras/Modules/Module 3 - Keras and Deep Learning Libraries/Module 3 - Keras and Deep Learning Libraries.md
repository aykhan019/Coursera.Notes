

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664EB2UMQN%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJIMEYCIQDbWeaWV1Crn2yQOzAgKemrRkS%2FYZkwETNnwQQ0JG4FxwIhAJkkjSe6yV2vMdOG%2BATzdoMG0Y8WzULIyOBappi6UIr4Kv8DCHkQABoMNjM3NDIzMTgzODA1Igx%2FNuVG355HYF4NM0Aq3AMeaEr3J4EVI88iWhw0cQgDSm8wB5pfRiRVcoFkunfTezLAhPlYAZrLDpLWHOf0yqcsjSy1LKV3mw3lkQilmxE9FHEw5FxVk6T4RSNu8S3b%2BERqpxl8jOhVDcM7orBf2i9TLITcN6ZjoWUMKU5VThrATmzYleB1wAtl%2FP7ntOLekBqzIv8pI1zXViRY6g8m66WLUofQl4FInq1XXzlMcCFrLwZAeRC0S%2F5Vp7tpk%2BKTH4ZRXQ7ukpkrKBNytvqgTPMVS6h2wfl2Nfr3udrB3qH4IjDGRtRNuJtDMSF6aKg8AaC6RZL84MvUveo7zmiebBr0ZsgqPNBwhxvJekjANeYRl5monRsM8v6lyyGIPTI8TVI9mD6nBCRK4K7Y4n7sJwJQLp9ZWvKMJwTHKHCjjo3%2FXNdjORlfoFTKnYdDfwsW2Ir8LsZiiW5WmDrU%2BY%2BVOz7API7plgN6AYv2ub5Nb8pHaQ4FGCPcmzkn8Q%2FGbklDXJftNDoGE25MxY8Olmjo6aTLu3kpj5NFtUhhWGsIfcIRbfxf7OkcIZiyRJ%2B%2FMUUhaqlASTR36779tsX%2FwK3TSrgQe4jPN74BYdy3iJ1xWxrJe6SS0urptN6ZbjMLgxLNQyRqS7GsbaepGlrWwTCx4Ji9BjqkAfRJHuQ1MgftLvvGeStAJSAChAuGpD2ECs5J1Ymxq1UNL50up4ucg3w%2Fwdqyg789pmnBEEHqMEgJVqqtB4VjlNqrB5uFqfZXi0l1mWxWhRzdoepvqenKt156RpffJ4EmxldLUGE%2BZC4RgW1xZicDaYc0VxTdbcK27qkZb0vySbLwK%2Bsf4Ojt5oQL08QkRanyl22ZrdbMKrotrP4KjnjONSqHLAiN&X-Amz-Signature=c50000b8d99172bd7beeee9af2fd74d813e62c1f976bf77d68ca8c0f5d239df0&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664EB2UMQN%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJIMEYCIQDbWeaWV1Crn2yQOzAgKemrRkS%2FYZkwETNnwQQ0JG4FxwIhAJkkjSe6yV2vMdOG%2BATzdoMG0Y8WzULIyOBappi6UIr4Kv8DCHkQABoMNjM3NDIzMTgzODA1Igx%2FNuVG355HYF4NM0Aq3AMeaEr3J4EVI88iWhw0cQgDSm8wB5pfRiRVcoFkunfTezLAhPlYAZrLDpLWHOf0yqcsjSy1LKV3mw3lkQilmxE9FHEw5FxVk6T4RSNu8S3b%2BERqpxl8jOhVDcM7orBf2i9TLITcN6ZjoWUMKU5VThrATmzYleB1wAtl%2FP7ntOLekBqzIv8pI1zXViRY6g8m66WLUofQl4FInq1XXzlMcCFrLwZAeRC0S%2F5Vp7tpk%2BKTH4ZRXQ7ukpkrKBNytvqgTPMVS6h2wfl2Nfr3udrB3qH4IjDGRtRNuJtDMSF6aKg8AaC6RZL84MvUveo7zmiebBr0ZsgqPNBwhxvJekjANeYRl5monRsM8v6lyyGIPTI8TVI9mD6nBCRK4K7Y4n7sJwJQLp9ZWvKMJwTHKHCjjo3%2FXNdjORlfoFTKnYdDfwsW2Ir8LsZiiW5WmDrU%2BY%2BVOz7API7plgN6AYv2ub5Nb8pHaQ4FGCPcmzkn8Q%2FGbklDXJftNDoGE25MxY8Olmjo6aTLu3kpj5NFtUhhWGsIfcIRbfxf7OkcIZiyRJ%2B%2FMUUhaqlASTR36779tsX%2FwK3TSrgQe4jPN74BYdy3iJ1xWxrJe6SS0urptN6ZbjMLgxLNQyRqS7GsbaepGlrWwTCx4Ji9BjqkAfRJHuQ1MgftLvvGeStAJSAChAuGpD2ECs5J1Ymxq1UNL50up4ucg3w%2Fwdqyg789pmnBEEHqMEgJVqqtB4VjlNqrB5uFqfZXi0l1mWxWhRzdoepvqenKt156RpffJ4EmxldLUGE%2BZC4RgW1xZicDaYc0VxTdbcK27qkZb0vySbLwK%2Bsf4Ojt5oQL08QkRanyl22ZrdbMKrotrP4KjnjONSqHLAiN&X-Amz-Signature=8c5ee56da087ff4d56586bd63aa4c497ac1ab386ec052f7c0d348dd5e7b50b5b&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664EB2UMQN%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJIMEYCIQDbWeaWV1Crn2yQOzAgKemrRkS%2FYZkwETNnwQQ0JG4FxwIhAJkkjSe6yV2vMdOG%2BATzdoMG0Y8WzULIyOBappi6UIr4Kv8DCHkQABoMNjM3NDIzMTgzODA1Igx%2FNuVG355HYF4NM0Aq3AMeaEr3J4EVI88iWhw0cQgDSm8wB5pfRiRVcoFkunfTezLAhPlYAZrLDpLWHOf0yqcsjSy1LKV3mw3lkQilmxE9FHEw5FxVk6T4RSNu8S3b%2BERqpxl8jOhVDcM7orBf2i9TLITcN6ZjoWUMKU5VThrATmzYleB1wAtl%2FP7ntOLekBqzIv8pI1zXViRY6g8m66WLUofQl4FInq1XXzlMcCFrLwZAeRC0S%2F5Vp7tpk%2BKTH4ZRXQ7ukpkrKBNytvqgTPMVS6h2wfl2Nfr3udrB3qH4IjDGRtRNuJtDMSF6aKg8AaC6RZL84MvUveo7zmiebBr0ZsgqPNBwhxvJekjANeYRl5monRsM8v6lyyGIPTI8TVI9mD6nBCRK4K7Y4n7sJwJQLp9ZWvKMJwTHKHCjjo3%2FXNdjORlfoFTKnYdDfwsW2Ir8LsZiiW5WmDrU%2BY%2BVOz7API7plgN6AYv2ub5Nb8pHaQ4FGCPcmzkn8Q%2FGbklDXJftNDoGE25MxY8Olmjo6aTLu3kpj5NFtUhhWGsIfcIRbfxf7OkcIZiyRJ%2B%2FMUUhaqlASTR36779tsX%2FwK3TSrgQe4jPN74BYdy3iJ1xWxrJe6SS0urptN6ZbjMLgxLNQyRqS7GsbaepGlrWwTCx4Ji9BjqkAfRJHuQ1MgftLvvGeStAJSAChAuGpD2ECs5J1Ymxq1UNL50up4ucg3w%2Fwdqyg789pmnBEEHqMEgJVqqtB4VjlNqrB5uFqfZXi0l1mWxWhRzdoepvqenKt156RpffJ4EmxldLUGE%2BZC4RgW1xZicDaYc0VxTdbcK27qkZb0vySbLwK%2Bsf4Ojt5oQL08QkRanyl22ZrdbMKrotrP4KjnjONSqHLAiN&X-Amz-Signature=bb6068354cbf74ec69e3d2390b266fc36bf9126385ff9778c3a36b97303169d7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623PAZXXD%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJHMEUCIAkauzmU01cYlC3GgLr88yt%2FSfgs0xvr9dzhL1ybgYBHAiEAsqqdd%2Bj6XdvaBogb3Qe0AivqB9wa3wWO%2FSYb3QrV3Rkq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDNUhlPd5cMxpMUVLSircA3LZlVQSshQtAoqi1aF4CDgvLFp44gHQWIs7x9p%2FwlLRorFSrKQ%2BGmvee5tvqS4FdtnK0EE10o7ak%2B6NQQM2UyMPefwMlY3l16tGx6WHuGFUfXAvYW0fBDR1DLl39AiA%2B%2BzIof2fao%2Bs6DX6W6d%2Fg0tR6hsVGWDWlDjUvTA0T2ARhtDxyfLqC8emv2E7MC4DHGjH6ctc8dpqlAkpQHw%2BKNpGW9qwUh%2FyZHtvJ5hKNEGsFUcx8SHsQ2%2BC%2BRqLai6A%2BsIcyd8LJCYLYuunDA4TFKhW%2BkUa04hJAxoWq6IXS6nrQegR7cNR4L6LDz8Cof3jRsZkSni%2F%2BqiQgtRAe%2Bh%2BUYbXqq89aIJCyuoxxwBFlWwVcJByxg6nkKEnAiGB7%2BuoSy6FmiZuhi3lu9mRU9IQ8aQ1UafV%2B0WWec%2BkOMyvle6Evf7jXFQOymJfvKuoj6cMXx7RNSzvKnw8eHAMz6FBlNWJTkzEvwqtUrexW2c0lp88OMheu6otJhUULes0HnJmyyj7tKf2M15MDpSXWzqOzC6hHQDNJuP%2Bay7e5m1K9dP1VhEDHSmtWybrPbInkaW1ac80jptu2gKzZGD6w0tOAHJfd5RzCwwD5zMj31TcgKiyzo9W8MjTu0UElJgbMP7fmL0GOqUBYp%2FrEEVYVqz1NHr5S8lc7ENCclfAWoJP%2B9pFlVgwpbWoDnv12rC%2FDQxSMV73k6I2BkytQJtqj2dbr04Qb4JcR%2FtxjcwtSzkstF3J0OOwRM03s3HoQrdKAVG4Fttq2mErgxMafUPtDMBTJhcTsCSiPXphG0KZdyj1N14aRD%2Bo2HAFAOXZ%2F7QYxBMLzZcZevwbHhQz1NBsYpDgFUHVWlaWuZBxqh9H&X-Amz-Signature=eae6e7e826293373fa06dc07e0e5562cff830228118adfdc76838dbeb12638ec&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VBLEUWPM%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJIMEYCIQCtmJvjt4oBnk3YKV%2FNOHJnv6VmC8UrxcUCVC%2B50ZROEAIhAJorkg6N%2BiGqQ5aMMXPyKSh771xWPlhRQxvTUBZufERrKv8DCHkQABoMNjM3NDIzMTgzODA1Igzo0FVL3RJUdXpIk50q3AOBH4JGBCY6AaeGRctZqdzGawPbbIO4Fs17Jkmgv8cJL5%2FT85nN5sT9z6fGrw18D%2FHnZZmp9O0mNq4FfCvdqJ7GJJ3wArL0KHM0S4s4dLDsF6nBBKTYpSUwqaJw%2BOWztDEhQ3dR600%2F9NSRMc13zfBX4T4T3wUg40zuGtHkV5zWEVqz%2F4KkAmHCyMPfNczJxHkC1XE2uyWt2CqhbIX76QVkU9AUZfDS3FUh9D1aSH33soDLz4toFIWVQHZYQ2lZM40zFyyHbFiOd5BJMA0fnhir596ta6NrNmGihrJjh1a2C5gFpnt7Y8D4%2BLZ%2B7%2BXCzOvimq7%2Fsx0u7Em547KGVU1iKZCbDHHGRDtJ5DXtahOcJUgPvJ5pyDS8xzhEQvCs3YPriLRVueIijXIHMSLeEHJOJ%2BBmkHnXUh6qUe3KjDiM%2FSm1WlTsn2sZohupu4OaZL9Gmp8BXvj8hva9Unn8OknZSjP%2BhH3CqVBEYLbmbXa2dB%2FCBTxMa6QGUAjfdBydBliwFVCer5jlVYqnjlSpTHDPSiQc%2FcTOIeCJoYsP5dcaG0zUllpoqUFBoxyBwh%2BslpyUqdkPwnsddBLLZkzh%2B390sTvUr36qL16WB1Qic8Od2FgRC1lzriMi%2BOHNojD235i9BjqkAX%2FB%2FMJcD1vse6JOqzsiXLksDis6YpTqH7XphHHPKy4lVkwUrJXm8Er2%2FiYm6oo6FVF1uqAKI8Yiq0T0ZeDevaKBY4eoxLdq1YWJWr9r0XS6zJ75ctXjr8Uq7ln5WRSy0UcBc0JgX%2BSVFWWR%2B4g0cY1%2BL5TGB1mRLSXdplC6faBHA%2FLULBEjR6m%2Bh908%2Fi3uJTBX9xd9Qq1Mm%2BhyehzM9Z6GYjGT&X-Amz-Signature=fdd6201ff2a295cae0ef10e167c3b14fca418c0ddb12919bfe1314be5a77adb1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664EB2UMQN%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJIMEYCIQDbWeaWV1Crn2yQOzAgKemrRkS%2FYZkwETNnwQQ0JG4FxwIhAJkkjSe6yV2vMdOG%2BATzdoMG0Y8WzULIyOBappi6UIr4Kv8DCHkQABoMNjM3NDIzMTgzODA1Igx%2FNuVG355HYF4NM0Aq3AMeaEr3J4EVI88iWhw0cQgDSm8wB5pfRiRVcoFkunfTezLAhPlYAZrLDpLWHOf0yqcsjSy1LKV3mw3lkQilmxE9FHEw5FxVk6T4RSNu8S3b%2BERqpxl8jOhVDcM7orBf2i9TLITcN6ZjoWUMKU5VThrATmzYleB1wAtl%2FP7ntOLekBqzIv8pI1zXViRY6g8m66WLUofQl4FInq1XXzlMcCFrLwZAeRC0S%2F5Vp7tpk%2BKTH4ZRXQ7ukpkrKBNytvqgTPMVS6h2wfl2Nfr3udrB3qH4IjDGRtRNuJtDMSF6aKg8AaC6RZL84MvUveo7zmiebBr0ZsgqPNBwhxvJekjANeYRl5monRsM8v6lyyGIPTI8TVI9mD6nBCRK4K7Y4n7sJwJQLp9ZWvKMJwTHKHCjjo3%2FXNdjORlfoFTKnYdDfwsW2Ir8LsZiiW5WmDrU%2BY%2BVOz7API7plgN6AYv2ub5Nb8pHaQ4FGCPcmzkn8Q%2FGbklDXJftNDoGE25MxY8Olmjo6aTLu3kpj5NFtUhhWGsIfcIRbfxf7OkcIZiyRJ%2B%2FMUUhaqlASTR36779tsX%2FwK3TSrgQe4jPN74BYdy3iJ1xWxrJe6SS0urptN6ZbjMLgxLNQyRqS7GsbaepGlrWwTCx4Ji9BjqkAfRJHuQ1MgftLvvGeStAJSAChAuGpD2ECs5J1Ymxq1UNL50up4ucg3w%2Fwdqyg789pmnBEEHqMEgJVqqtB4VjlNqrB5uFqfZXi0l1mWxWhRzdoepvqenKt156RpffJ4EmxldLUGE%2BZC4RgW1xZicDaYc0VxTdbcK27qkZb0vySbLwK%2Bsf4Ojt5oQL08QkRanyl22ZrdbMKrotrP4KjnjONSqHLAiN&X-Amz-Signature=d6d9018d11a9163d6254564f1ada6459eb72b78fcdb39dc446fa5cb1f038376a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664EB2UMQN%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJIMEYCIQDbWeaWV1Crn2yQOzAgKemrRkS%2FYZkwETNnwQQ0JG4FxwIhAJkkjSe6yV2vMdOG%2BATzdoMG0Y8WzULIyOBappi6UIr4Kv8DCHkQABoMNjM3NDIzMTgzODA1Igx%2FNuVG355HYF4NM0Aq3AMeaEr3J4EVI88iWhw0cQgDSm8wB5pfRiRVcoFkunfTezLAhPlYAZrLDpLWHOf0yqcsjSy1LKV3mw3lkQilmxE9FHEw5FxVk6T4RSNu8S3b%2BERqpxl8jOhVDcM7orBf2i9TLITcN6ZjoWUMKU5VThrATmzYleB1wAtl%2FP7ntOLekBqzIv8pI1zXViRY6g8m66WLUofQl4FInq1XXzlMcCFrLwZAeRC0S%2F5Vp7tpk%2BKTH4ZRXQ7ukpkrKBNytvqgTPMVS6h2wfl2Nfr3udrB3qH4IjDGRtRNuJtDMSF6aKg8AaC6RZL84MvUveo7zmiebBr0ZsgqPNBwhxvJekjANeYRl5monRsM8v6lyyGIPTI8TVI9mD6nBCRK4K7Y4n7sJwJQLp9ZWvKMJwTHKHCjjo3%2FXNdjORlfoFTKnYdDfwsW2Ir8LsZiiW5WmDrU%2BY%2BVOz7API7plgN6AYv2ub5Nb8pHaQ4FGCPcmzkn8Q%2FGbklDXJftNDoGE25MxY8Olmjo6aTLu3kpj5NFtUhhWGsIfcIRbfxf7OkcIZiyRJ%2B%2FMUUhaqlASTR36779tsX%2FwK3TSrgQe4jPN74BYdy3iJ1xWxrJe6SS0urptN6ZbjMLgxLNQyRqS7GsbaepGlrWwTCx4Ji9BjqkAfRJHuQ1MgftLvvGeStAJSAChAuGpD2ECs5J1Ymxq1UNL50up4ucg3w%2Fwdqyg789pmnBEEHqMEgJVqqtB4VjlNqrB5uFqfZXi0l1mWxWhRzdoepvqenKt156RpffJ4EmxldLUGE%2BZC4RgW1xZicDaYc0VxTdbcK27qkZb0vySbLwK%2Bsf4Ojt5oQL08QkRanyl22ZrdbMKrotrP4KjnjONSqHLAiN&X-Amz-Signature=2ea7a5b7cb2b5d1c0cf4f6bddf651bc230b0c1f38a4562c3e5356c18a9a681da&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664EB2UMQN%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJIMEYCIQDbWeaWV1Crn2yQOzAgKemrRkS%2FYZkwETNnwQQ0JG4FxwIhAJkkjSe6yV2vMdOG%2BATzdoMG0Y8WzULIyOBappi6UIr4Kv8DCHkQABoMNjM3NDIzMTgzODA1Igx%2FNuVG355HYF4NM0Aq3AMeaEr3J4EVI88iWhw0cQgDSm8wB5pfRiRVcoFkunfTezLAhPlYAZrLDpLWHOf0yqcsjSy1LKV3mw3lkQilmxE9FHEw5FxVk6T4RSNu8S3b%2BERqpxl8jOhVDcM7orBf2i9TLITcN6ZjoWUMKU5VThrATmzYleB1wAtl%2FP7ntOLekBqzIv8pI1zXViRY6g8m66WLUofQl4FInq1XXzlMcCFrLwZAeRC0S%2F5Vp7tpk%2BKTH4ZRXQ7ukpkrKBNytvqgTPMVS6h2wfl2Nfr3udrB3qH4IjDGRtRNuJtDMSF6aKg8AaC6RZL84MvUveo7zmiebBr0ZsgqPNBwhxvJekjANeYRl5monRsM8v6lyyGIPTI8TVI9mD6nBCRK4K7Y4n7sJwJQLp9ZWvKMJwTHKHCjjo3%2FXNdjORlfoFTKnYdDfwsW2Ir8LsZiiW5WmDrU%2BY%2BVOz7API7plgN6AYv2ub5Nb8pHaQ4FGCPcmzkn8Q%2FGbklDXJftNDoGE25MxY8Olmjo6aTLu3kpj5NFtUhhWGsIfcIRbfxf7OkcIZiyRJ%2B%2FMUUhaqlASTR36779tsX%2FwK3TSrgQe4jPN74BYdy3iJ1xWxrJe6SS0urptN6ZbjMLgxLNQyRqS7GsbaepGlrWwTCx4Ji9BjqkAfRJHuQ1MgftLvvGeStAJSAChAuGpD2ECs5J1Ymxq1UNL50up4ucg3w%2Fwdqyg789pmnBEEHqMEgJVqqtB4VjlNqrB5uFqfZXi0l1mWxWhRzdoepvqenKt156RpffJ4EmxldLUGE%2BZC4RgW1xZicDaYc0VxTdbcK27qkZb0vySbLwK%2Bsf4Ojt5oQL08QkRanyl22ZrdbMKrotrP4KjnjONSqHLAiN&X-Amz-Signature=2ea0c013ca1e2b1102fd50ef1785f698ffe438f39e08ddc42be9ac8301664be2&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664EB2UMQN%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJIMEYCIQDbWeaWV1Crn2yQOzAgKemrRkS%2FYZkwETNnwQQ0JG4FxwIhAJkkjSe6yV2vMdOG%2BATzdoMG0Y8WzULIyOBappi6UIr4Kv8DCHkQABoMNjM3NDIzMTgzODA1Igx%2FNuVG355HYF4NM0Aq3AMeaEr3J4EVI88iWhw0cQgDSm8wB5pfRiRVcoFkunfTezLAhPlYAZrLDpLWHOf0yqcsjSy1LKV3mw3lkQilmxE9FHEw5FxVk6T4RSNu8S3b%2BERqpxl8jOhVDcM7orBf2i9TLITcN6ZjoWUMKU5VThrATmzYleB1wAtl%2FP7ntOLekBqzIv8pI1zXViRY6g8m66WLUofQl4FInq1XXzlMcCFrLwZAeRC0S%2F5Vp7tpk%2BKTH4ZRXQ7ukpkrKBNytvqgTPMVS6h2wfl2Nfr3udrB3qH4IjDGRtRNuJtDMSF6aKg8AaC6RZL84MvUveo7zmiebBr0ZsgqPNBwhxvJekjANeYRl5monRsM8v6lyyGIPTI8TVI9mD6nBCRK4K7Y4n7sJwJQLp9ZWvKMJwTHKHCjjo3%2FXNdjORlfoFTKnYdDfwsW2Ir8LsZiiW5WmDrU%2BY%2BVOz7API7plgN6AYv2ub5Nb8pHaQ4FGCPcmzkn8Q%2FGbklDXJftNDoGE25MxY8Olmjo6aTLu3kpj5NFtUhhWGsIfcIRbfxf7OkcIZiyRJ%2B%2FMUUhaqlASTR36779tsX%2FwK3TSrgQe4jPN74BYdy3iJ1xWxrJe6SS0urptN6ZbjMLgxLNQyRqS7GsbaepGlrWwTCx4Ji9BjqkAfRJHuQ1MgftLvvGeStAJSAChAuGpD2ECs5J1Ymxq1UNL50up4ucg3w%2Fwdqyg789pmnBEEHqMEgJVqqtB4VjlNqrB5uFqfZXi0l1mWxWhRzdoepvqenKt156RpffJ4EmxldLUGE%2BZC4RgW1xZicDaYc0VxTdbcK27qkZb0vySbLwK%2Bsf4Ojt5oQL08QkRanyl22ZrdbMKrotrP4KjnjONSqHLAiN&X-Amz-Signature=5195e64922c381e7b7dad7e48ef27d285a001b08eb7dce0e88e0b04ba60d91e6&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
