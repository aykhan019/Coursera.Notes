

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DRVDM3E%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011146Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG2i%2BBOcMoxcCIfgIMJWQt1M0l0kPgYTy3FDAUTCTXl5AiEAj3Y4cU8SdLttYKwPbqM8O03ZO2o6UipWIEO4PV1dEf8qiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDErLkgPuLyMvqS65MCrcA0AC23VO0HvasnBYtytU9bZdMAfdHz8y92d3ksAtHYQfO0780soab4fgSHo2Ea519JAYJvYj7VHvJ0iUBIDDgHGrjcB3VTP7eJQ27Z33V4qdInZKzCR0wzJj5V1eQ4bUTOB0TUB9ARG%2Bu77tEfLNVhbubuG26cuyc2cSF4w7GMb2geud068C0vjM%2BSkYF2AJtVncxArB1iBqL4MCZ1WUbp8eA49Fb3v2z%2ByOBp%2FLsT2fIvI%2FqxY38RwT11i6pEY7VzXx%2BuythrcatB88HAlKP5XjKTBckjk2%2F0V2QqEGDykJ4uYcECu20EmWAocW3XVJBdouQIGEVhF45gRjT4kp4JUbZ4QVadG2KtqKW%2ByIywBX7hYGFh3aLRkE65GSkLBLrmA5ORQqssemwApSYMDj0OCsmAJ0%2F0zYRQuGEViuT8xOgc06cGgq6B%2FzqMbtro%2BWWhBljKrrw0052faeMb2buwwQKi%2FBBjjt5oPWKcjeGwKg752M89aSELat0%2FoToFdMu6Enk5Fghdot91W9gC5%2BOjOq7pL29uj%2FqX7zT%2BuZHODZHXL2grT5n0KUKbwwv0ZKDryEKJ02iUVAF8ct5u%2BOTluDYvZeSE0d4KeJicfFnqWGB%2B%2BtEScqxIJW6G2KMM%2Fx%2BrwGOqUBS387YO%2BsSSBOLWKTz%2BAaizmyV6NIkdAiyD%2BiLSAhuQimfeZ7fNN2pwYzcMYvDPOBPHiinHfuBVWTl3yyC67GpyWX7Ihpg%2BjHvRSw1Ul16bhOPeOMoN%2FT4xe1XmizqlIN6mYNnLaezziH8gvzEXD8h0RUl%2B853t1%2BVrbA8JloIv0GYV8jjSrGde7j0PrJaS5bdDCWCMjXTWZNYMHdYDBNkt5%2FiYzM&X-Amz-Signature=00d470cd709e70e7425c2ab882271db4012c6428dc594afa29431094f6d39732&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DRVDM3E%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011146Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG2i%2BBOcMoxcCIfgIMJWQt1M0l0kPgYTy3FDAUTCTXl5AiEAj3Y4cU8SdLttYKwPbqM8O03ZO2o6UipWIEO4PV1dEf8qiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDErLkgPuLyMvqS65MCrcA0AC23VO0HvasnBYtytU9bZdMAfdHz8y92d3ksAtHYQfO0780soab4fgSHo2Ea519JAYJvYj7VHvJ0iUBIDDgHGrjcB3VTP7eJQ27Z33V4qdInZKzCR0wzJj5V1eQ4bUTOB0TUB9ARG%2Bu77tEfLNVhbubuG26cuyc2cSF4w7GMb2geud068C0vjM%2BSkYF2AJtVncxArB1iBqL4MCZ1WUbp8eA49Fb3v2z%2ByOBp%2FLsT2fIvI%2FqxY38RwT11i6pEY7VzXx%2BuythrcatB88HAlKP5XjKTBckjk2%2F0V2QqEGDykJ4uYcECu20EmWAocW3XVJBdouQIGEVhF45gRjT4kp4JUbZ4QVadG2KtqKW%2ByIywBX7hYGFh3aLRkE65GSkLBLrmA5ORQqssemwApSYMDj0OCsmAJ0%2F0zYRQuGEViuT8xOgc06cGgq6B%2FzqMbtro%2BWWhBljKrrw0052faeMb2buwwQKi%2FBBjjt5oPWKcjeGwKg752M89aSELat0%2FoToFdMu6Enk5Fghdot91W9gC5%2BOjOq7pL29uj%2FqX7zT%2BuZHODZHXL2grT5n0KUKbwwv0ZKDryEKJ02iUVAF8ct5u%2BOTluDYvZeSE0d4KeJicfFnqWGB%2B%2BtEScqxIJW6G2KMM%2Fx%2BrwGOqUBS387YO%2BsSSBOLWKTz%2BAaizmyV6NIkdAiyD%2BiLSAhuQimfeZ7fNN2pwYzcMYvDPOBPHiinHfuBVWTl3yyC67GpyWX7Ihpg%2BjHvRSw1Ul16bhOPeOMoN%2FT4xe1XmizqlIN6mYNnLaezziH8gvzEXD8h0RUl%2B853t1%2BVrbA8JloIv0GYV8jjSrGde7j0PrJaS5bdDCWCMjXTWZNYMHdYDBNkt5%2FiYzM&X-Amz-Signature=0d38b540f5941e4fd1186666b6c783507c02620add94966ec28b51f03453e690&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DRVDM3E%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011146Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG2i%2BBOcMoxcCIfgIMJWQt1M0l0kPgYTy3FDAUTCTXl5AiEAj3Y4cU8SdLttYKwPbqM8O03ZO2o6UipWIEO4PV1dEf8qiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDErLkgPuLyMvqS65MCrcA0AC23VO0HvasnBYtytU9bZdMAfdHz8y92d3ksAtHYQfO0780soab4fgSHo2Ea519JAYJvYj7VHvJ0iUBIDDgHGrjcB3VTP7eJQ27Z33V4qdInZKzCR0wzJj5V1eQ4bUTOB0TUB9ARG%2Bu77tEfLNVhbubuG26cuyc2cSF4w7GMb2geud068C0vjM%2BSkYF2AJtVncxArB1iBqL4MCZ1WUbp8eA49Fb3v2z%2ByOBp%2FLsT2fIvI%2FqxY38RwT11i6pEY7VzXx%2BuythrcatB88HAlKP5XjKTBckjk2%2F0V2QqEGDykJ4uYcECu20EmWAocW3XVJBdouQIGEVhF45gRjT4kp4JUbZ4QVadG2KtqKW%2ByIywBX7hYGFh3aLRkE65GSkLBLrmA5ORQqssemwApSYMDj0OCsmAJ0%2F0zYRQuGEViuT8xOgc06cGgq6B%2FzqMbtro%2BWWhBljKrrw0052faeMb2buwwQKi%2FBBjjt5oPWKcjeGwKg752M89aSELat0%2FoToFdMu6Enk5Fghdot91W9gC5%2BOjOq7pL29uj%2FqX7zT%2BuZHODZHXL2grT5n0KUKbwwv0ZKDryEKJ02iUVAF8ct5u%2BOTluDYvZeSE0d4KeJicfFnqWGB%2B%2BtEScqxIJW6G2KMM%2Fx%2BrwGOqUBS387YO%2BsSSBOLWKTz%2BAaizmyV6NIkdAiyD%2BiLSAhuQimfeZ7fNN2pwYzcMYvDPOBPHiinHfuBVWTl3yyC67GpyWX7Ihpg%2BjHvRSw1Ul16bhOPeOMoN%2FT4xe1XmizqlIN6mYNnLaezziH8gvzEXD8h0RUl%2B853t1%2BVrbA8JloIv0GYV8jjSrGde7j0PrJaS5bdDCWCMjXTWZNYMHdYDBNkt5%2FiYzM&X-Amz-Signature=41c7632d0245b348ec07b12638826f3efab32b1e0e1eaecec4adcfade6baef7e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZLTWR7PO%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIETt59W863jzqLBb4SKiPTntkMQHvhcIJDNTK1yNB7gqAiBrqC2Mf6cXc%2FjnDuUyLZaeDqykJpxwqVdHOqviEaV7KyqIBAjh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMDL7Ll3wyvJLTptsvKtwDklU93keYV7lc0Gzvo%2FyE%2BD8RrpM9phJ8oqgx59dVHOnEa5%2FK14Xh6FKf%2BhDbzJ25csqnEwvs0eLoLartxiucy%2B2sPhpgj9nIzxe8rLtfh1mGv8gDviOxCMmnpqjqJLWw7Pcx61eschf9QdxLdDg6Gkcv4AGBdDbGZ5dOOcAd1ofAMqQJu03mmVnts2%2FiqdoBP%2BsW6ZRkiCj%2FjZ0LrGngsV4cbz2TDCRllSmb9UBasZONWL%2FKucUIyESpFesTAjCqR3FuGVTilBnmgGLn687P5A%2F8pMglTSb0codlOQoY3%2Fjokca%2BKkzUoNw%2BjghyJ8BK4kvcd0Ax4RZC8R2aqKTw8McDQfu%2Brw%2BJSiB7QMNY10R7MkWKLjh79XGUfVzgl5qC726Kl2d59kt2q0MjWcLkR%2BxAjevjawJ00zzYz7vlMfxZ0xaM3pNuU8%2Fg7WgiurpjKO7Pt6jtrgX%2FKOh6h6Ls58xWFyhl%2BAan8EKEYQahM7gw9xrZ7pIeBCuT3yEKBtTZf%2BJfHYEL3lOBw4kqlW%2B2cKdv4GHtinT9mUCIgKQ12FEiFNC%2BA6ixgu%2FZhmLkhzcST7tgrlmBl8OpAyl6OTRtkrgEIutkL%2BVU4QS4McrVKob2M%2FSuf4N00YQ1NAkw9PH6vAY6pgHAyJ3KQy7SxiBvJTqJM6C%2BbAV5HwjSl2B5I%2FXtyDEpDkkgKxZos%2Fz6SY7o1b0pWccl7vp0IMjB2hF8ntTPxqCsccn2I6%2F5ZZLs7vgjkaaDwaQnRR12urEiN7Ek7bRUFp%2F9Lbl2eMqaeWRXZ92QWQPwOL0o91kUpw%2BmCO3YGKHANJGcyOJvK9TjPSGXiq5DYvchpEEaxrGok%2Bsl%2BrOG%2FwBAgr1d1Gmp&X-Amz-Signature=efcc150224f404a07318895108a33d193f9e39abc6f5c8c0f81de1a1d508e2d3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662RMMN3FW%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD8MSDCQg5UTYco5JzgPYX%2FJS%2F%2Bjnv%2Bkvr%2BHsfzZ7WO5QIhAMPqM%2BpehWZHzzzf2JPV9BeNWf1SZpfGY7BFRNZPEAcaKogECOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwXc81nmlHZVxSeoeIq3ANOjqvN%2FN5wm1VQ47qF1EPHRxDVjOh9u0r72KOrv%2BMTHOu2azcf4EoJJdgXLkQDmAzZw%2F%2BWsah3xxobAdIsJW7JLtJj4eOhssrpwd5Ih%2FUXW9KX0ihNAvb98oQ5cAk6PWR0jQ709KTns9FuGNMALyo7bfYlyn%2BxEPSiH7Fe8Y%2BycpCUeBxJ0frVvYsS%2BK9wke5AuuTKtWZiEBGiNfut%2BP9IuCagLRL7qwbYlVsOUAxzGbn0rWuCGDFflABSAHfABnq%2FJ74aUJEYA3m7Pz3sGN9lLIeNSam8QNAmGbFCi5ygwuD%2B38Piei7IbfKu7Unxgd5wLGoUsIOg6M1iJbdtVUjytUmePEqbQ11g9jjFFrDSo42%2BoyS6ytSAw1pNp3mlXT0crAXvgEWzSxAYInFIeGKUhv4X%2FTUf5z9Y9Ad1f5n61dNC3DR50UHV8NTWlkR3Mrur1AVjRvuqrKjZWjPdoj%2F3UJFVYVjhPJpkSAe97zGV75m4DDGjm%2BuLtK%2F43RU3NS41yp0XL9a4utEhwXgk1GT3BA9rwDTVHHNrJYRDnLHOnTu6fAdxWbvKewx8QGnHOA2uO%2B2r0CnCBZiswi1pGCiXvdtWAbOHhPcYSmo33zg9tdaqOQhsw3afMv0aYDD18fq8BjqkAZCOaFaL4I03UVSh5S8JFm6iomxWiXHexbsfn1ZKrHy9GG0Xffy5j77LUClsuBzF0cmoiFZBl0wFEizKCp6acwa00SKbhqSmP0mAmLGwDkxudVdN0ou5Ws%2B2CH0ffRT9YfdsuAkm9pRFVgd727LNzMyBPEwHrXceATVEDpoaXfw193k%2FdtjCE0TwHtM1E4NHaPTqpzmqFkwXIM3tD41JGbGZgD0S&X-Amz-Signature=f04a039e876f30e9878d2d13cf41b6be8022a4d0094ff3998618c2178ef126d9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DRVDM3E%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011146Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG2i%2BBOcMoxcCIfgIMJWQt1M0l0kPgYTy3FDAUTCTXl5AiEAj3Y4cU8SdLttYKwPbqM8O03ZO2o6UipWIEO4PV1dEf8qiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDErLkgPuLyMvqS65MCrcA0AC23VO0HvasnBYtytU9bZdMAfdHz8y92d3ksAtHYQfO0780soab4fgSHo2Ea519JAYJvYj7VHvJ0iUBIDDgHGrjcB3VTP7eJQ27Z33V4qdInZKzCR0wzJj5V1eQ4bUTOB0TUB9ARG%2Bu77tEfLNVhbubuG26cuyc2cSF4w7GMb2geud068C0vjM%2BSkYF2AJtVncxArB1iBqL4MCZ1WUbp8eA49Fb3v2z%2ByOBp%2FLsT2fIvI%2FqxY38RwT11i6pEY7VzXx%2BuythrcatB88HAlKP5XjKTBckjk2%2F0V2QqEGDykJ4uYcECu20EmWAocW3XVJBdouQIGEVhF45gRjT4kp4JUbZ4QVadG2KtqKW%2ByIywBX7hYGFh3aLRkE65GSkLBLrmA5ORQqssemwApSYMDj0OCsmAJ0%2F0zYRQuGEViuT8xOgc06cGgq6B%2FzqMbtro%2BWWhBljKrrw0052faeMb2buwwQKi%2FBBjjt5oPWKcjeGwKg752M89aSELat0%2FoToFdMu6Enk5Fghdot91W9gC5%2BOjOq7pL29uj%2FqX7zT%2BuZHODZHXL2grT5n0KUKbwwv0ZKDryEKJ02iUVAF8ct5u%2BOTluDYvZeSE0d4KeJicfFnqWGB%2B%2BtEScqxIJW6G2KMM%2Fx%2BrwGOqUBS387YO%2BsSSBOLWKTz%2BAaizmyV6NIkdAiyD%2BiLSAhuQimfeZ7fNN2pwYzcMYvDPOBPHiinHfuBVWTl3yyC67GpyWX7Ihpg%2BjHvRSw1Ul16bhOPeOMoN%2FT4xe1XmizqlIN6mYNnLaezziH8gvzEXD8h0RUl%2B853t1%2BVrbA8JloIv0GYV8jjSrGde7j0PrJaS5bdDCWCMjXTWZNYMHdYDBNkt5%2FiYzM&X-Amz-Signature=bc5b5761f83f4e856b0facc8de71378a58844a1b39ca1e216d2720e5cb79f40c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DRVDM3E%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011146Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG2i%2BBOcMoxcCIfgIMJWQt1M0l0kPgYTy3FDAUTCTXl5AiEAj3Y4cU8SdLttYKwPbqM8O03ZO2o6UipWIEO4PV1dEf8qiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDErLkgPuLyMvqS65MCrcA0AC23VO0HvasnBYtytU9bZdMAfdHz8y92d3ksAtHYQfO0780soab4fgSHo2Ea519JAYJvYj7VHvJ0iUBIDDgHGrjcB3VTP7eJQ27Z33V4qdInZKzCR0wzJj5V1eQ4bUTOB0TUB9ARG%2Bu77tEfLNVhbubuG26cuyc2cSF4w7GMb2geud068C0vjM%2BSkYF2AJtVncxArB1iBqL4MCZ1WUbp8eA49Fb3v2z%2ByOBp%2FLsT2fIvI%2FqxY38RwT11i6pEY7VzXx%2BuythrcatB88HAlKP5XjKTBckjk2%2F0V2QqEGDykJ4uYcECu20EmWAocW3XVJBdouQIGEVhF45gRjT4kp4JUbZ4QVadG2KtqKW%2ByIywBX7hYGFh3aLRkE65GSkLBLrmA5ORQqssemwApSYMDj0OCsmAJ0%2F0zYRQuGEViuT8xOgc06cGgq6B%2FzqMbtro%2BWWhBljKrrw0052faeMb2buwwQKi%2FBBjjt5oPWKcjeGwKg752M89aSELat0%2FoToFdMu6Enk5Fghdot91W9gC5%2BOjOq7pL29uj%2FqX7zT%2BuZHODZHXL2grT5n0KUKbwwv0ZKDryEKJ02iUVAF8ct5u%2BOTluDYvZeSE0d4KeJicfFnqWGB%2B%2BtEScqxIJW6G2KMM%2Fx%2BrwGOqUBS387YO%2BsSSBOLWKTz%2BAaizmyV6NIkdAiyD%2BiLSAhuQimfeZ7fNN2pwYzcMYvDPOBPHiinHfuBVWTl3yyC67GpyWX7Ihpg%2BjHvRSw1Ul16bhOPeOMoN%2FT4xe1XmizqlIN6mYNnLaezziH8gvzEXD8h0RUl%2B853t1%2BVrbA8JloIv0GYV8jjSrGde7j0PrJaS5bdDCWCMjXTWZNYMHdYDBNkt5%2FiYzM&X-Amz-Signature=47f2d8e953844d16af4926724d32a2ac68fdea3be5ea14d09c18a65cb0132616&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DRVDM3E%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011146Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG2i%2BBOcMoxcCIfgIMJWQt1M0l0kPgYTy3FDAUTCTXl5AiEAj3Y4cU8SdLttYKwPbqM8O03ZO2o6UipWIEO4PV1dEf8qiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDErLkgPuLyMvqS65MCrcA0AC23VO0HvasnBYtytU9bZdMAfdHz8y92d3ksAtHYQfO0780soab4fgSHo2Ea519JAYJvYj7VHvJ0iUBIDDgHGrjcB3VTP7eJQ27Z33V4qdInZKzCR0wzJj5V1eQ4bUTOB0TUB9ARG%2Bu77tEfLNVhbubuG26cuyc2cSF4w7GMb2geud068C0vjM%2BSkYF2AJtVncxArB1iBqL4MCZ1WUbp8eA49Fb3v2z%2ByOBp%2FLsT2fIvI%2FqxY38RwT11i6pEY7VzXx%2BuythrcatB88HAlKP5XjKTBckjk2%2F0V2QqEGDykJ4uYcECu20EmWAocW3XVJBdouQIGEVhF45gRjT4kp4JUbZ4QVadG2KtqKW%2ByIywBX7hYGFh3aLRkE65GSkLBLrmA5ORQqssemwApSYMDj0OCsmAJ0%2F0zYRQuGEViuT8xOgc06cGgq6B%2FzqMbtro%2BWWhBljKrrw0052faeMb2buwwQKi%2FBBjjt5oPWKcjeGwKg752M89aSELat0%2FoToFdMu6Enk5Fghdot91W9gC5%2BOjOq7pL29uj%2FqX7zT%2BuZHODZHXL2grT5n0KUKbwwv0ZKDryEKJ02iUVAF8ct5u%2BOTluDYvZeSE0d4KeJicfFnqWGB%2B%2BtEScqxIJW6G2KMM%2Fx%2BrwGOqUBS387YO%2BsSSBOLWKTz%2BAaizmyV6NIkdAiyD%2BiLSAhuQimfeZ7fNN2pwYzcMYvDPOBPHiinHfuBVWTl3yyC67GpyWX7Ihpg%2BjHvRSw1Ul16bhOPeOMoN%2FT4xe1XmizqlIN6mYNnLaezziH8gvzEXD8h0RUl%2B853t1%2BVrbA8JloIv0GYV8jjSrGde7j0PrJaS5bdDCWCMjXTWZNYMHdYDBNkt5%2FiYzM&X-Amz-Signature=62932fed14bcc2a8181794ad4f29da0cd6ac2283f4fbfe929cc8fd14d4588377&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DRVDM3E%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG2i%2BBOcMoxcCIfgIMJWQt1M0l0kPgYTy3FDAUTCTXl5AiEAj3Y4cU8SdLttYKwPbqM8O03ZO2o6UipWIEO4PV1dEf8qiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDErLkgPuLyMvqS65MCrcA0AC23VO0HvasnBYtytU9bZdMAfdHz8y92d3ksAtHYQfO0780soab4fgSHo2Ea519JAYJvYj7VHvJ0iUBIDDgHGrjcB3VTP7eJQ27Z33V4qdInZKzCR0wzJj5V1eQ4bUTOB0TUB9ARG%2Bu77tEfLNVhbubuG26cuyc2cSF4w7GMb2geud068C0vjM%2BSkYF2AJtVncxArB1iBqL4MCZ1WUbp8eA49Fb3v2z%2ByOBp%2FLsT2fIvI%2FqxY38RwT11i6pEY7VzXx%2BuythrcatB88HAlKP5XjKTBckjk2%2F0V2QqEGDykJ4uYcECu20EmWAocW3XVJBdouQIGEVhF45gRjT4kp4JUbZ4QVadG2KtqKW%2ByIywBX7hYGFh3aLRkE65GSkLBLrmA5ORQqssemwApSYMDj0OCsmAJ0%2F0zYRQuGEViuT8xOgc06cGgq6B%2FzqMbtro%2BWWhBljKrrw0052faeMb2buwwQKi%2FBBjjt5oPWKcjeGwKg752M89aSELat0%2FoToFdMu6Enk5Fghdot91W9gC5%2BOjOq7pL29uj%2FqX7zT%2BuZHODZHXL2grT5n0KUKbwwv0ZKDryEKJ02iUVAF8ct5u%2BOTluDYvZeSE0d4KeJicfFnqWGB%2B%2BtEScqxIJW6G2KMM%2Fx%2BrwGOqUBS387YO%2BsSSBOLWKTz%2BAaizmyV6NIkdAiyD%2BiLSAhuQimfeZ7fNN2pwYzcMYvDPOBPHiinHfuBVWTl3yyC67GpyWX7Ihpg%2BjHvRSw1Ul16bhOPeOMoN%2FT4xe1XmizqlIN6mYNnLaezziH8gvzEXD8h0RUl%2B853t1%2BVrbA8JloIv0GYV8jjSrGde7j0PrJaS5bdDCWCMjXTWZNYMHdYDBNkt5%2FiYzM&X-Amz-Signature=72c454f40ef326d5f8588479f990b172b5f728e2bf38b3e989de804ec0cf616c&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
