

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664AEY5WT3%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIE9BYlVH7V%2BrBfyBrcHO9ju7lW5rya5Op%2BBS5b6miBPkAiEAiNkMN67qugkG%2BS%2FEPWPx6QEQ491ERg%2Fo4wXvWhszn0Aq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDPvhNYRIrLBwoMD1IircA%2FgimbKGS24M77tWEiUUzmY%2FQfXVNAoYuOVyElARZLtr3C%2F3f6DKkrLVFEmzOGUeJRoeWMb8oE2RG93bA0gEfe%2B3dM6sw8kGd7svExsvTpdW4LkEIi8g7bWRT6uc%2FiFbqgMSFHdk%2F8cP5waHXi3dP8jEzYiydDVJACeJRZ8gBTxAXFSNSNuW6G8LQttBMwCepQKTbDEfkrkX0ewKui5h4kvFCxgjMG39FRCbHYZsngio4JRC%2B6I0IA0NiEAqAtQkmZ3uFppZ3XUasAV1NCs34ksCMlZuyHgwUqN0j2X6yO7TfiE0J0Zzf116kzUzTxpvyeEB6wCfJzkg%2BRCs9Q%2FZgfOdvEyQL3EztfUjhrZC1fb4rAC9vgctAQJE9ffA0npy9%2BUZs%2BBppXsc2s5cl3G%2FSRfQdQqTFCVwxDhYdbjLWWOOHQij%2FL%2FyXpIs3Mc90zWiRnuklbsErb16ri0LkwJ6skm5EhX8Xbokj4KJ1MvokAfeAR8IUN5tzOGdm77WmlTfdKygAjJ10dTjpvvIBKB0Owbp81Dj4EqniogHZtRfbeUkBXKn7V6PMRb%2B%2Bdt3AhJ4TLTf1%2FANKXxTd7MQ9sMSLp%2FP1Fg6%2FcoI7EaFo%2F9KNqkdVc1UQ2x8uWOcxf18MNyhhr0GOqUBHwnPuVX14e2Ytn0dN%2B8S8OZOB5YvICPJGeeTGP7BhvV1irDu9CFolO8CP23IhDgf4CbJvR7yZWYG28H1lzqGLtWGpOLw2EExs4KbcDXpWPQZagvmMloKAbzpgfnHvOJOBWY00tubz%2B83BZmJCfoW%2FJ%2Bx8tYC0xFYWMBI1Zlc1h6RCOS94Y7yNHyunnsqZaEEW6vbWng%2F2lGDrXLyTyowo0NG8%2Bvf&X-Amz-Signature=5f54a6ce6f90ccf6ee68d962ac1652e31878cfe3a5ac9d147b227cc517288725&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664AEY5WT3%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIE9BYlVH7V%2BrBfyBrcHO9ju7lW5rya5Op%2BBS5b6miBPkAiEAiNkMN67qugkG%2BS%2FEPWPx6QEQ491ERg%2Fo4wXvWhszn0Aq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDPvhNYRIrLBwoMD1IircA%2FgimbKGS24M77tWEiUUzmY%2FQfXVNAoYuOVyElARZLtr3C%2F3f6DKkrLVFEmzOGUeJRoeWMb8oE2RG93bA0gEfe%2B3dM6sw8kGd7svExsvTpdW4LkEIi8g7bWRT6uc%2FiFbqgMSFHdk%2F8cP5waHXi3dP8jEzYiydDVJACeJRZ8gBTxAXFSNSNuW6G8LQttBMwCepQKTbDEfkrkX0ewKui5h4kvFCxgjMG39FRCbHYZsngio4JRC%2B6I0IA0NiEAqAtQkmZ3uFppZ3XUasAV1NCs34ksCMlZuyHgwUqN0j2X6yO7TfiE0J0Zzf116kzUzTxpvyeEB6wCfJzkg%2BRCs9Q%2FZgfOdvEyQL3EztfUjhrZC1fb4rAC9vgctAQJE9ffA0npy9%2BUZs%2BBppXsc2s5cl3G%2FSRfQdQqTFCVwxDhYdbjLWWOOHQij%2FL%2FyXpIs3Mc90zWiRnuklbsErb16ri0LkwJ6skm5EhX8Xbokj4KJ1MvokAfeAR8IUN5tzOGdm77WmlTfdKygAjJ10dTjpvvIBKB0Owbp81Dj4EqniogHZtRfbeUkBXKn7V6PMRb%2B%2Bdt3AhJ4TLTf1%2FANKXxTd7MQ9sMSLp%2FP1Fg6%2FcoI7EaFo%2F9KNqkdVc1UQ2x8uWOcxf18MNyhhr0GOqUBHwnPuVX14e2Ytn0dN%2B8S8OZOB5YvICPJGeeTGP7BhvV1irDu9CFolO8CP23IhDgf4CbJvR7yZWYG28H1lzqGLtWGpOLw2EExs4KbcDXpWPQZagvmMloKAbzpgfnHvOJOBWY00tubz%2B83BZmJCfoW%2FJ%2Bx8tYC0xFYWMBI1Zlc1h6RCOS94Y7yNHyunnsqZaEEW6vbWng%2F2lGDrXLyTyowo0NG8%2Bvf&X-Amz-Signature=17cdbc404a763c36833cc5a183bd1a42cdf08dd3f080f154522285ed1b31562c&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664AEY5WT3%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIE9BYlVH7V%2BrBfyBrcHO9ju7lW5rya5Op%2BBS5b6miBPkAiEAiNkMN67qugkG%2BS%2FEPWPx6QEQ491ERg%2Fo4wXvWhszn0Aq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDPvhNYRIrLBwoMD1IircA%2FgimbKGS24M77tWEiUUzmY%2FQfXVNAoYuOVyElARZLtr3C%2F3f6DKkrLVFEmzOGUeJRoeWMb8oE2RG93bA0gEfe%2B3dM6sw8kGd7svExsvTpdW4LkEIi8g7bWRT6uc%2FiFbqgMSFHdk%2F8cP5waHXi3dP8jEzYiydDVJACeJRZ8gBTxAXFSNSNuW6G8LQttBMwCepQKTbDEfkrkX0ewKui5h4kvFCxgjMG39FRCbHYZsngio4JRC%2B6I0IA0NiEAqAtQkmZ3uFppZ3XUasAV1NCs34ksCMlZuyHgwUqN0j2X6yO7TfiE0J0Zzf116kzUzTxpvyeEB6wCfJzkg%2BRCs9Q%2FZgfOdvEyQL3EztfUjhrZC1fb4rAC9vgctAQJE9ffA0npy9%2BUZs%2BBppXsc2s5cl3G%2FSRfQdQqTFCVwxDhYdbjLWWOOHQij%2FL%2FyXpIs3Mc90zWiRnuklbsErb16ri0LkwJ6skm5EhX8Xbokj4KJ1MvokAfeAR8IUN5tzOGdm77WmlTfdKygAjJ10dTjpvvIBKB0Owbp81Dj4EqniogHZtRfbeUkBXKn7V6PMRb%2B%2Bdt3AhJ4TLTf1%2FANKXxTd7MQ9sMSLp%2FP1Fg6%2FcoI7EaFo%2F9KNqkdVc1UQ2x8uWOcxf18MNyhhr0GOqUBHwnPuVX14e2Ytn0dN%2B8S8OZOB5YvICPJGeeTGP7BhvV1irDu9CFolO8CP23IhDgf4CbJvR7yZWYG28H1lzqGLtWGpOLw2EExs4KbcDXpWPQZagvmMloKAbzpgfnHvOJOBWY00tubz%2B83BZmJCfoW%2FJ%2Bx8tYC0xFYWMBI1Zlc1h6RCOS94Y7yNHyunnsqZaEEW6vbWng%2F2lGDrXLyTyowo0NG8%2Bvf&X-Amz-Signature=90c3d3b3fa9359412598000af2bb68aa3ff940393863bd31b6ffb6dda3198dd1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665OG27YPL%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041721Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQDChnrgpm4q3bwNA6nFDu5Rf8VaqBX0CHZu4oCtovc2EgIgL2Z8EfY5bDlte3PIrL5M3VYijFAjff%2FfZewI7Wz2Cecq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDNQYq0g4c1eSIndGMCrcA473L21JcVY6IvvXVaWxL%2FnqNpwCPt4UOsgCIpACGlAkgvgzQz8XJIDWRCL8WbXBwUlxXvOm%2FOO9fL4U8TcRrW1NKyQUaHMycdE8yNJLo26IUYEebeyS3mukpXBRSHxma7BLdHkglOjBFuoGWaPE4eI%2BiXpBEFCHTAMFS2GML1r7Iwc7ujurUl2A%2FL%2BEHv1vwiqv9nKUOfvzif4jAQKJgqFJKwB%2FF%2B3HZx2leUVNXEDOBEupk2Y9pYrNyNqA2xfDUs8KKJpri4%2FZyttmaWEOZTU3F%2BFGTNc7tLjV%2B538RYWl46nUoJ7uEKD42jGMFnMs9zb6swZdetndVu4TRUGEHw8MzQmwJiznGOCPjkyANlSj1ucbmzpZUMteNn7r5niZ%2FHN3UKeiZaK0uayqmPRNKlfL6NvlQyIJAxHrLd2hwCU3sH6wA6lsvknS1YH96h%2FIcs4EAaXGSyHF8n%2F0z5mHgZmOXYa4X6U8h1b%2Bv0wkC11BSXICizSasOiUR3NnTmWSWYjjD41KS5%2Fn%2Fs%2FcbQ0PKi4AQPMuiT2IlGiQBe9nifXKk6qhz2pvZvvJlU8%2BGatUDRhDecL7bPCuEFOIUNTVfzSGN1HITtxX8dQVzatDVHuXWH0IqFNXVt%2F7DLANMJaihr0GOqUBj0yGtDbrzMJBq9n90fDk2i7CBwXlJIisDSpJ4WDz28%2BgaTs9EofPps%2F5kawWI9Fiuz0%2BjC0bO2ofs4TfnHJvY78qtIeeWuC9DK5X5Ao8cr8%2FxTUfCacyxczk3WZch2jzU7SGPhmGmnvX2%2FzMZJ9hiInq5TtGiNHpKlWvkG2Hbm%2Fpq5pdMDsdsEEneQ2dx2WpG6tbRGJ44Nsm9eEDsr4zOLUFRZXc&X-Amz-Signature=92f6bbdb65e305d5301dfa94381410d614c14d3a053b1a60f5119f774fd39877&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466REG7BHJV%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041721Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQDBbcmzIiVRSv5IZ5oy64OaTDo7e85XtxqMBQuxmqvZPQIgcA19qfSRrphEf3FsYZeZJS8MIQVeOmImpjxnTCKejAwq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDLaB6vnP4%2BHbQBIAWyrcA0ZjRwzm5R95FX8wGb2JG5iVhqPoEOtW6aUrCQcQ8FXEXavHYX%2Bi5K7wZBVpbKVFAxuUvDo0mRKuHxE3yIXt3V2J7S7it%2FquiwMBgbX37CWut1Vxzb7ujsiOLj5f1sT%2B6CK3jdhMM%2FMCXstusPdCQYHx%2FyxlsO1xcfezk3Sx%2B%2BzuwaeZR7YMFb%2BJE9wBu92kCMWBmqf6u1oWwwUQblbRcwlBIIJiSbRu5HDehrWU0nYwUr%2BaVffAxzmmMizwAuynf94l6TUrS%2B5xHMCjevi%2BpzbYt4C9wKUlMR5%2FIPtCR1dwptefYaHs3NuI0LcIXcAuQkOVyqgiaqNhksLpSO5ON1nOSBA%2F%2BSXWfFgW5NWUBufKk59ilUCz1agUX415KnZxgdgCeRtLS2ZxySCFwyH79%2BHhB9NDoKMzMzh7E79VWHFzd03DWp%2Fnhx5340JrfNkX6DzKHV6Himf7EgSax9bwmZEEWkxeaXdfcBYuKXFD%2Brd8VlqdJuAPOOeKOiwjDy5UjaVT5Q76Iwr96s1wF7n2bbvXHIZQYwDbQnzDjIATWBEAaYCJW9Pq9dtua8h0BRVYFMUpH86Vj0N4fjS3GXBlX0Jf4MQrYtRt0irFy%2BCo%2FSnRGH63i6DXdOXPkSz%2BMP6hhr0GOqUBkGDdQVmxfZ7gkf9PM2OrbISEruoM1XGJXbED5oeq5H18pV1AIfV3nCvoEUCV8C42BVcIufnWkzhbXYk1%2FNo5jFkXSJyskbvB9TqEVy9QnaCC7%2BrFi0QVNKtDR7ixVgpfBKWVHTlhBDx6aGaJ2hovu70OoTXKCJtb7oA65gV4%2BfB%2F3dAujROSkZsmbmvCgh927HK6ngrYRlOmdf6YMX2Jv%2FbYR8Pp&X-Amz-Signature=fc685779bd85d8a269765798462cf8f46498f1cf630cb691e2afde7520cd2c68&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664AEY5WT3%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIE9BYlVH7V%2BrBfyBrcHO9ju7lW5rya5Op%2BBS5b6miBPkAiEAiNkMN67qugkG%2BS%2FEPWPx6QEQ491ERg%2Fo4wXvWhszn0Aq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDPvhNYRIrLBwoMD1IircA%2FgimbKGS24M77tWEiUUzmY%2FQfXVNAoYuOVyElARZLtr3C%2F3f6DKkrLVFEmzOGUeJRoeWMb8oE2RG93bA0gEfe%2B3dM6sw8kGd7svExsvTpdW4LkEIi8g7bWRT6uc%2FiFbqgMSFHdk%2F8cP5waHXi3dP8jEzYiydDVJACeJRZ8gBTxAXFSNSNuW6G8LQttBMwCepQKTbDEfkrkX0ewKui5h4kvFCxgjMG39FRCbHYZsngio4JRC%2B6I0IA0NiEAqAtQkmZ3uFppZ3XUasAV1NCs34ksCMlZuyHgwUqN0j2X6yO7TfiE0J0Zzf116kzUzTxpvyeEB6wCfJzkg%2BRCs9Q%2FZgfOdvEyQL3EztfUjhrZC1fb4rAC9vgctAQJE9ffA0npy9%2BUZs%2BBppXsc2s5cl3G%2FSRfQdQqTFCVwxDhYdbjLWWOOHQij%2FL%2FyXpIs3Mc90zWiRnuklbsErb16ri0LkwJ6skm5EhX8Xbokj4KJ1MvokAfeAR8IUN5tzOGdm77WmlTfdKygAjJ10dTjpvvIBKB0Owbp81Dj4EqniogHZtRfbeUkBXKn7V6PMRb%2B%2Bdt3AhJ4TLTf1%2FANKXxTd7MQ9sMSLp%2FP1Fg6%2FcoI7EaFo%2F9KNqkdVc1UQ2x8uWOcxf18MNyhhr0GOqUBHwnPuVX14e2Ytn0dN%2B8S8OZOB5YvICPJGeeTGP7BhvV1irDu9CFolO8CP23IhDgf4CbJvR7yZWYG28H1lzqGLtWGpOLw2EExs4KbcDXpWPQZagvmMloKAbzpgfnHvOJOBWY00tubz%2B83BZmJCfoW%2FJ%2Bx8tYC0xFYWMBI1Zlc1h6RCOS94Y7yNHyunnsqZaEEW6vbWng%2F2lGDrXLyTyowo0NG8%2Bvf&X-Amz-Signature=213d738c8e011e3ca00b0b7bb89a724d50906565b9767e9762cbc729ec35514b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664AEY5WT3%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIE9BYlVH7V%2BrBfyBrcHO9ju7lW5rya5Op%2BBS5b6miBPkAiEAiNkMN67qugkG%2BS%2FEPWPx6QEQ491ERg%2Fo4wXvWhszn0Aq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDPvhNYRIrLBwoMD1IircA%2FgimbKGS24M77tWEiUUzmY%2FQfXVNAoYuOVyElARZLtr3C%2F3f6DKkrLVFEmzOGUeJRoeWMb8oE2RG93bA0gEfe%2B3dM6sw8kGd7svExsvTpdW4LkEIi8g7bWRT6uc%2FiFbqgMSFHdk%2F8cP5waHXi3dP8jEzYiydDVJACeJRZ8gBTxAXFSNSNuW6G8LQttBMwCepQKTbDEfkrkX0ewKui5h4kvFCxgjMG39FRCbHYZsngio4JRC%2B6I0IA0NiEAqAtQkmZ3uFppZ3XUasAV1NCs34ksCMlZuyHgwUqN0j2X6yO7TfiE0J0Zzf116kzUzTxpvyeEB6wCfJzkg%2BRCs9Q%2FZgfOdvEyQL3EztfUjhrZC1fb4rAC9vgctAQJE9ffA0npy9%2BUZs%2BBppXsc2s5cl3G%2FSRfQdQqTFCVwxDhYdbjLWWOOHQij%2FL%2FyXpIs3Mc90zWiRnuklbsErb16ri0LkwJ6skm5EhX8Xbokj4KJ1MvokAfeAR8IUN5tzOGdm77WmlTfdKygAjJ10dTjpvvIBKB0Owbp81Dj4EqniogHZtRfbeUkBXKn7V6PMRb%2B%2Bdt3AhJ4TLTf1%2FANKXxTd7MQ9sMSLp%2FP1Fg6%2FcoI7EaFo%2F9KNqkdVc1UQ2x8uWOcxf18MNyhhr0GOqUBHwnPuVX14e2Ytn0dN%2B8S8OZOB5YvICPJGeeTGP7BhvV1irDu9CFolO8CP23IhDgf4CbJvR7yZWYG28H1lzqGLtWGpOLw2EExs4KbcDXpWPQZagvmMloKAbzpgfnHvOJOBWY00tubz%2B83BZmJCfoW%2FJ%2Bx8tYC0xFYWMBI1Zlc1h6RCOS94Y7yNHyunnsqZaEEW6vbWng%2F2lGDrXLyTyowo0NG8%2Bvf&X-Amz-Signature=8d728351448fc1f53075f55ceb83c75f94a931fe0f48df1333e60a98e7bccf7a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664AEY5WT3%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIE9BYlVH7V%2BrBfyBrcHO9ju7lW5rya5Op%2BBS5b6miBPkAiEAiNkMN67qugkG%2BS%2FEPWPx6QEQ491ERg%2Fo4wXvWhszn0Aq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDPvhNYRIrLBwoMD1IircA%2FgimbKGS24M77tWEiUUzmY%2FQfXVNAoYuOVyElARZLtr3C%2F3f6DKkrLVFEmzOGUeJRoeWMb8oE2RG93bA0gEfe%2B3dM6sw8kGd7svExsvTpdW4LkEIi8g7bWRT6uc%2FiFbqgMSFHdk%2F8cP5waHXi3dP8jEzYiydDVJACeJRZ8gBTxAXFSNSNuW6G8LQttBMwCepQKTbDEfkrkX0ewKui5h4kvFCxgjMG39FRCbHYZsngio4JRC%2B6I0IA0NiEAqAtQkmZ3uFppZ3XUasAV1NCs34ksCMlZuyHgwUqN0j2X6yO7TfiE0J0Zzf116kzUzTxpvyeEB6wCfJzkg%2BRCs9Q%2FZgfOdvEyQL3EztfUjhrZC1fb4rAC9vgctAQJE9ffA0npy9%2BUZs%2BBppXsc2s5cl3G%2FSRfQdQqTFCVwxDhYdbjLWWOOHQij%2FL%2FyXpIs3Mc90zWiRnuklbsErb16ri0LkwJ6skm5EhX8Xbokj4KJ1MvokAfeAR8IUN5tzOGdm77WmlTfdKygAjJ10dTjpvvIBKB0Owbp81Dj4EqniogHZtRfbeUkBXKn7V6PMRb%2B%2Bdt3AhJ4TLTf1%2FANKXxTd7MQ9sMSLp%2FP1Fg6%2FcoI7EaFo%2F9KNqkdVc1UQ2x8uWOcxf18MNyhhr0GOqUBHwnPuVX14e2Ytn0dN%2B8S8OZOB5YvICPJGeeTGP7BhvV1irDu9CFolO8CP23IhDgf4CbJvR7yZWYG28H1lzqGLtWGpOLw2EExs4KbcDXpWPQZagvmMloKAbzpgfnHvOJOBWY00tubz%2B83BZmJCfoW%2FJ%2Bx8tYC0xFYWMBI1Zlc1h6RCOS94Y7yNHyunnsqZaEEW6vbWng%2F2lGDrXLyTyowo0NG8%2Bvf&X-Amz-Signature=c6c335af9d7562ff7f82e1322cd8cca1e01cf75e65d8fbfe7080464af5542680&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664AEY5WT3%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIE9BYlVH7V%2BrBfyBrcHO9ju7lW5rya5Op%2BBS5b6miBPkAiEAiNkMN67qugkG%2BS%2FEPWPx6QEQ491ERg%2Fo4wXvWhszn0Aq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDPvhNYRIrLBwoMD1IircA%2FgimbKGS24M77tWEiUUzmY%2FQfXVNAoYuOVyElARZLtr3C%2F3f6DKkrLVFEmzOGUeJRoeWMb8oE2RG93bA0gEfe%2B3dM6sw8kGd7svExsvTpdW4LkEIi8g7bWRT6uc%2FiFbqgMSFHdk%2F8cP5waHXi3dP8jEzYiydDVJACeJRZ8gBTxAXFSNSNuW6G8LQttBMwCepQKTbDEfkrkX0ewKui5h4kvFCxgjMG39FRCbHYZsngio4JRC%2B6I0IA0NiEAqAtQkmZ3uFppZ3XUasAV1NCs34ksCMlZuyHgwUqN0j2X6yO7TfiE0J0Zzf116kzUzTxpvyeEB6wCfJzkg%2BRCs9Q%2FZgfOdvEyQL3EztfUjhrZC1fb4rAC9vgctAQJE9ffA0npy9%2BUZs%2BBppXsc2s5cl3G%2FSRfQdQqTFCVwxDhYdbjLWWOOHQij%2FL%2FyXpIs3Mc90zWiRnuklbsErb16ri0LkwJ6skm5EhX8Xbokj4KJ1MvokAfeAR8IUN5tzOGdm77WmlTfdKygAjJ10dTjpvvIBKB0Owbp81Dj4EqniogHZtRfbeUkBXKn7V6PMRb%2B%2Bdt3AhJ4TLTf1%2FANKXxTd7MQ9sMSLp%2FP1Fg6%2FcoI7EaFo%2F9KNqkdVc1UQ2x8uWOcxf18MNyhhr0GOqUBHwnPuVX14e2Ytn0dN%2B8S8OZOB5YvICPJGeeTGP7BhvV1irDu9CFolO8CP23IhDgf4CbJvR7yZWYG28H1lzqGLtWGpOLw2EExs4KbcDXpWPQZagvmMloKAbzpgfnHvOJOBWY00tubz%2B83BZmJCfoW%2FJ%2Bx8tYC0xFYWMBI1Zlc1h6RCOS94Y7yNHyunnsqZaEEW6vbWng%2F2lGDrXLyTyowo0NG8%2Bvf&X-Amz-Signature=6ea5f06c73138901c06cee288d059ef970833c635ef91d9664480f09b4cc956a&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
