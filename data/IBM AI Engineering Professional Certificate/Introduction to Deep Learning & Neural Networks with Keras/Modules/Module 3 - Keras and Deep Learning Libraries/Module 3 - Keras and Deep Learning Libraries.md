

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TINOPOVD%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJHMEUCIFCam%2F6JjbkPSftgP8PfU3QcebDuQ1H7KwOaFds5izkeAiEA5FJErM5WGPSjOXavuvXH8QvkRtJ%2FvOf3RF5UJm4LZnoq%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDGhCGJu%2FJ6Vj5H%2FqXCrcAzaVwgfrvd42Rpz18jx7MRay6zeQAdVrX07xPMhIuVxATE4UY6XZhZKlagGEaZNi9c%2BOwPTzJ2DpFbJKZ2LlGwLGy9XhCUOr%2BL6cRJksQLeIhPT4NphckB6q3D5kiPFrKDjEvis5%2F3NQx%2F046PnJjtIk6V37KTX8rLlJPXxQzfMJMIAp2u1isDwqhzw4hVBiq8IZMaKZcZzTEycGWUqaXg9DSrHD%2F65ApA0w57xNir6XaH6CQXrdaEhFC12CODlFTyJXC2HHJoTo5L%2FvBDG8P3t%2FoRGHi5DiFv5bKqDYZBbKlaG2Z9EmVC4uO8Qx5GNrjCytkGNMON9JtiFjS1fCRUC3Lvps5nOacuKo9WmcioLaX7yJat%2BOiGJHlvv%2F0UjbnRYONFs9bPUJ8mSCJbg9xiFxzELTTTcKGDUnp74tSEs%2B4T%2Brnp31%2BVcIvs9r1rpiDmoLvVtYF2n2squYHxLtwu0vD5CBCnCM3RcDriSWfFrF8hy3rdulC2QOB%2F1LVS3OzwZD3AcLUz5Iayhb%2B6CCY3F3asxhT87SZUJkLbl5KF0ddGRz5XjeKWkOIXyrcGCpf5WJp%2BbqBZRvLoz%2BNvz5%2FYStjOlfdRN%2FGfo7%2FXhUCv2LMZwMf7qITv%2BRZLwIMPWzjL0GOqUBt4HAyKVS3Dm20dvIXAqWMpopUYC4Dd7CliwroDHY7NDr7SxvySR37msTmPe9WC%2BaA99RB5Jkt63SJ4plKHxx5NSPe%2B3V36cVciRrOvlNSEb1TXx9WjwT9QF4kMm9mkZX%2FNHwFoKO0NAUEMZr9BQhZ%2B93G0OY1amvF2HlBvOPtZi2t%2FbL7C2SMq3yWTr9B6qodJPmZV09%2FknlVCpAOievCuldTKEo&X-Amz-Signature=1adc929660c9c42298e0d8c132db66f198efb5297f7313d448e4fe846164fd6a&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TINOPOVD%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJHMEUCIFCam%2F6JjbkPSftgP8PfU3QcebDuQ1H7KwOaFds5izkeAiEA5FJErM5WGPSjOXavuvXH8QvkRtJ%2FvOf3RF5UJm4LZnoq%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDGhCGJu%2FJ6Vj5H%2FqXCrcAzaVwgfrvd42Rpz18jx7MRay6zeQAdVrX07xPMhIuVxATE4UY6XZhZKlagGEaZNi9c%2BOwPTzJ2DpFbJKZ2LlGwLGy9XhCUOr%2BL6cRJksQLeIhPT4NphckB6q3D5kiPFrKDjEvis5%2F3NQx%2F046PnJjtIk6V37KTX8rLlJPXxQzfMJMIAp2u1isDwqhzw4hVBiq8IZMaKZcZzTEycGWUqaXg9DSrHD%2F65ApA0w57xNir6XaH6CQXrdaEhFC12CODlFTyJXC2HHJoTo5L%2FvBDG8P3t%2FoRGHi5DiFv5bKqDYZBbKlaG2Z9EmVC4uO8Qx5GNrjCytkGNMON9JtiFjS1fCRUC3Lvps5nOacuKo9WmcioLaX7yJat%2BOiGJHlvv%2F0UjbnRYONFs9bPUJ8mSCJbg9xiFxzELTTTcKGDUnp74tSEs%2B4T%2Brnp31%2BVcIvs9r1rpiDmoLvVtYF2n2squYHxLtwu0vD5CBCnCM3RcDriSWfFrF8hy3rdulC2QOB%2F1LVS3OzwZD3AcLUz5Iayhb%2B6CCY3F3asxhT87SZUJkLbl5KF0ddGRz5XjeKWkOIXyrcGCpf5WJp%2BbqBZRvLoz%2BNvz5%2FYStjOlfdRN%2FGfo7%2FXhUCv2LMZwMf7qITv%2BRZLwIMPWzjL0GOqUBt4HAyKVS3Dm20dvIXAqWMpopUYC4Dd7CliwroDHY7NDr7SxvySR37msTmPe9WC%2BaA99RB5Jkt63SJ4plKHxx5NSPe%2B3V36cVciRrOvlNSEb1TXx9WjwT9QF4kMm9mkZX%2FNHwFoKO0NAUEMZr9BQhZ%2B93G0OY1amvF2HlBvOPtZi2t%2FbL7C2SMq3yWTr9B6qodJPmZV09%2FknlVCpAOievCuldTKEo&X-Amz-Signature=45b9ad275e9bb733146b1713bdd879b9a78c7963473bdd9747bb38c4f3d2f146&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TINOPOVD%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJHMEUCIFCam%2F6JjbkPSftgP8PfU3QcebDuQ1H7KwOaFds5izkeAiEA5FJErM5WGPSjOXavuvXH8QvkRtJ%2FvOf3RF5UJm4LZnoq%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDGhCGJu%2FJ6Vj5H%2FqXCrcAzaVwgfrvd42Rpz18jx7MRay6zeQAdVrX07xPMhIuVxATE4UY6XZhZKlagGEaZNi9c%2BOwPTzJ2DpFbJKZ2LlGwLGy9XhCUOr%2BL6cRJksQLeIhPT4NphckB6q3D5kiPFrKDjEvis5%2F3NQx%2F046PnJjtIk6V37KTX8rLlJPXxQzfMJMIAp2u1isDwqhzw4hVBiq8IZMaKZcZzTEycGWUqaXg9DSrHD%2F65ApA0w57xNir6XaH6CQXrdaEhFC12CODlFTyJXC2HHJoTo5L%2FvBDG8P3t%2FoRGHi5DiFv5bKqDYZBbKlaG2Z9EmVC4uO8Qx5GNrjCytkGNMON9JtiFjS1fCRUC3Lvps5nOacuKo9WmcioLaX7yJat%2BOiGJHlvv%2F0UjbnRYONFs9bPUJ8mSCJbg9xiFxzELTTTcKGDUnp74tSEs%2B4T%2Brnp31%2BVcIvs9r1rpiDmoLvVtYF2n2squYHxLtwu0vD5CBCnCM3RcDriSWfFrF8hy3rdulC2QOB%2F1LVS3OzwZD3AcLUz5Iayhb%2B6CCY3F3asxhT87SZUJkLbl5KF0ddGRz5XjeKWkOIXyrcGCpf5WJp%2BbqBZRvLoz%2BNvz5%2FYStjOlfdRN%2FGfo7%2FXhUCv2LMZwMf7qITv%2BRZLwIMPWzjL0GOqUBt4HAyKVS3Dm20dvIXAqWMpopUYC4Dd7CliwroDHY7NDr7SxvySR37msTmPe9WC%2BaA99RB5Jkt63SJ4plKHxx5NSPe%2B3V36cVciRrOvlNSEb1TXx9WjwT9QF4kMm9mkZX%2FNHwFoKO0NAUEMZr9BQhZ%2B93G0OY1amvF2HlBvOPtZi2t%2FbL7C2SMq3yWTr9B6qodJPmZV09%2FknlVCpAOievCuldTKEo&X-Amz-Signature=3f18ce84817fe38e61976f5351ca0a797072648c2a5e1076bd01a07d2f2ed1bc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662AOG7LYN%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJHMEUCIQDWm3LA2HRYORidD2M8FBQ8uWWRC%2FEjeOVorsuRlO%2BJzAIgCDDWEE64bB12cVC2y2Hb7Gegovyxf27rlZ6OLk88cngq%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDPsgqsSFtfiRg2ezpSrcA6WjqGK8mpz1xD5R6bgHTaT88m2jVdAAVYa4GBbXbqm2Bwr10t4dYohSshUekMpINi4bVTEorrxjl9hFdTSZEJh1zoSYTvRGU4qouM4MEdv%2B4SRkRVpxgGDd2PIhFcrXTe4Rh1H2bfDyvC4LiVqYN469pzA4Pd%2BD4djebZVDOZszTzJleFksyKPNZBMjrXGX9fJSTHnCWnPb%2FSpmUM91CPNb0YrtlikIOdp8y8VmGOrvfs97ndIbeQts%2Fp7pE7nfI%2BVNdpBIKR5wr2xfWCGr7c39DvdQCysVW%2BBxsuciLoHavTr%2FlT21SOhUPAVqxDOwo4%2BoBGv26UeTxh0gyPl2%2BvOUBPGU%2FlcdqXcmsM5A%2FE7f7uu5dJWYYPMTmVplTMdZ%2BrDGRiX7eDNlsfFGk7B0wZknHCoto22DgvXMtyz1oo5g%2F3TzxRd9G33yab1qiT6yTZe4ZC7QpdVVZqdF8x%2FVV8%2FRSLbC8mjplkwO6G%2B3ngUH1CyMKW1O22fI8W0QRHG6U7vnvN83S%2FDhGA8%2BJyMFNLX7NJoB%2FUmvfHotnBApA4BRvHlSRKvh5JNk2C10FY6fg%2BQ8ycbJ%2FbmJ43nR4BGoKrl65LJ5%2F8nghF27cGeraXxwuj7CnuEcJ2ry9E4VMJazjL0GOqUBzAu%2BqjaPH0BSaG6fhj%2FXru2ta%2BwrubDa4Ccs%2BGXzsNH4a88070ZAFajtotPAuk14Z3YoMu5jFpQP0L4z45nN6UhfrJyCqr7GIeuiiishd3lM95yAjVNz5mIFRNNW%2B55W6ebDJO0duGP6EaSfPw5BpDUI3%2FWRmn7TLzN6vy%2F4etJQje1E6WDU%2F7osxK%2FnL%2Ff%2BRQBJWRSTW4VVZwY5dkpDbvplYKWv&X-Amz-Signature=6e5ce560970bdb8aaee242a16f29d665049b480dbef41ab918583dbace25b409&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QKQ7XICT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJIMEYCIQD0WOXPw72lugeQGrPguCF3n6k3kvO9Z3H5yn97vTsbygIhALuagMA6GRleOE%2F6om3mSfrEWylRUm%2FPKFmdYqCr3xl2Kv8DCEEQABoMNjM3NDIzMTgzODA1Igz6Xhms%2F2Km603OkFMq3AMtCeBaeUA0rLwJgWUC4ASv%2FsiQw07%2Bcpx3zzr%2BN9WI7uBz2k6r6q1PkCe6xvIdWxSVc81txsAE3miIwNuboQ1oTk6X8fshsKvR%2BtFdFH7TjksAAGaH94qKRL3u%2Fz6YSSApEh%2B5yA1%2FzhnLikmnA2LQPENGPBQjBbGQ8ldIX9jI45P0FQEOu%2BOeULeyf%2FFKGFREraZGcDPE%2FcYJ%2BWd1wXjcT4xpOe1z5eOzdWZrTLHuZuhaIy4BNntuRN8KnI5hndr8f8%2F4Fp5DcWY%2FXVbeNM7IGGG1o2Y1fDYUv1ZkC1cKK%2BBXoW2Qq89u%2BXSIBoeieeTJ8%2BfDZNEdL%2F1rLO18xS4mBMft4muKoonny9iyIh7bsa9629aeW8ccrdazmR1SBDR0nQo%2BoKl2BKE6JWFjUc6UAcwP9%2FeYZ1bcWNx%2BWEXaoHmCVM8Rumfn0hPGIqRnKr8dmTl7EgNIvQ%2FrZZWA69m0Yj452QgQiDgBqsLvDqpfx0BeXmqbxY7MtYxyewpRDiZHLEKFjb1A5bWVuy5Je8J1kZmAF%2Fa2UnBT0OlmW%2Bp4qFT0R6nCnamAAbSGcjfW6wB6psURQSUjG6nRkke5vZWhB3VRCfCq9AbMi4pMajojhEAWmxB6UmkBMAEQfTDjs4y9BjqkARneMCgZcVo3wO%2BmIhliX2WP2ruQYoSlj14jDrKisHwBFuaJDbwBLgYW3AeTbYrM3%2BJxP8CpuocwhlbJT6iOYa1W61FC6RLhaN0TRoN%2FiZj%2FZnIKG5zPc9y3zv%2FNiGUsaoUQlR4LVyLCqakGfrDoqFJLQqKaqzTSNh4AajVffa5SUfKBkLP5I4n9Ut9sva%2F2rm8MflbVbSGvWn4l5rr7XTBhusyq&X-Amz-Signature=2797fcc80fbe8e9c2e758fec4a48ea44d414864fe953de3bd56098b13e5de00e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TINOPOVD%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJHMEUCIFCam%2F6JjbkPSftgP8PfU3QcebDuQ1H7KwOaFds5izkeAiEA5FJErM5WGPSjOXavuvXH8QvkRtJ%2FvOf3RF5UJm4LZnoq%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDGhCGJu%2FJ6Vj5H%2FqXCrcAzaVwgfrvd42Rpz18jx7MRay6zeQAdVrX07xPMhIuVxATE4UY6XZhZKlagGEaZNi9c%2BOwPTzJ2DpFbJKZ2LlGwLGy9XhCUOr%2BL6cRJksQLeIhPT4NphckB6q3D5kiPFrKDjEvis5%2F3NQx%2F046PnJjtIk6V37KTX8rLlJPXxQzfMJMIAp2u1isDwqhzw4hVBiq8IZMaKZcZzTEycGWUqaXg9DSrHD%2F65ApA0w57xNir6XaH6CQXrdaEhFC12CODlFTyJXC2HHJoTo5L%2FvBDG8P3t%2FoRGHi5DiFv5bKqDYZBbKlaG2Z9EmVC4uO8Qx5GNrjCytkGNMON9JtiFjS1fCRUC3Lvps5nOacuKo9WmcioLaX7yJat%2BOiGJHlvv%2F0UjbnRYONFs9bPUJ8mSCJbg9xiFxzELTTTcKGDUnp74tSEs%2B4T%2Brnp31%2BVcIvs9r1rpiDmoLvVtYF2n2squYHxLtwu0vD5CBCnCM3RcDriSWfFrF8hy3rdulC2QOB%2F1LVS3OzwZD3AcLUz5Iayhb%2B6CCY3F3asxhT87SZUJkLbl5KF0ddGRz5XjeKWkOIXyrcGCpf5WJp%2BbqBZRvLoz%2BNvz5%2FYStjOlfdRN%2FGfo7%2FXhUCv2LMZwMf7qITv%2BRZLwIMPWzjL0GOqUBt4HAyKVS3Dm20dvIXAqWMpopUYC4Dd7CliwroDHY7NDr7SxvySR37msTmPe9WC%2BaA99RB5Jkt63SJ4plKHxx5NSPe%2B3V36cVciRrOvlNSEb1TXx9WjwT9QF4kMm9mkZX%2FNHwFoKO0NAUEMZr9BQhZ%2B93G0OY1amvF2HlBvOPtZi2t%2FbL7C2SMq3yWTr9B6qodJPmZV09%2FknlVCpAOievCuldTKEo&X-Amz-Signature=c362eee5e73c9870a4378b674e09cc3776983e38f99a0b07797543a29e220751&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TINOPOVD%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJHMEUCIFCam%2F6JjbkPSftgP8PfU3QcebDuQ1H7KwOaFds5izkeAiEA5FJErM5WGPSjOXavuvXH8QvkRtJ%2FvOf3RF5UJm4LZnoq%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDGhCGJu%2FJ6Vj5H%2FqXCrcAzaVwgfrvd42Rpz18jx7MRay6zeQAdVrX07xPMhIuVxATE4UY6XZhZKlagGEaZNi9c%2BOwPTzJ2DpFbJKZ2LlGwLGy9XhCUOr%2BL6cRJksQLeIhPT4NphckB6q3D5kiPFrKDjEvis5%2F3NQx%2F046PnJjtIk6V37KTX8rLlJPXxQzfMJMIAp2u1isDwqhzw4hVBiq8IZMaKZcZzTEycGWUqaXg9DSrHD%2F65ApA0w57xNir6XaH6CQXrdaEhFC12CODlFTyJXC2HHJoTo5L%2FvBDG8P3t%2FoRGHi5DiFv5bKqDYZBbKlaG2Z9EmVC4uO8Qx5GNrjCytkGNMON9JtiFjS1fCRUC3Lvps5nOacuKo9WmcioLaX7yJat%2BOiGJHlvv%2F0UjbnRYONFs9bPUJ8mSCJbg9xiFxzELTTTcKGDUnp74tSEs%2B4T%2Brnp31%2BVcIvs9r1rpiDmoLvVtYF2n2squYHxLtwu0vD5CBCnCM3RcDriSWfFrF8hy3rdulC2QOB%2F1LVS3OzwZD3AcLUz5Iayhb%2B6CCY3F3asxhT87SZUJkLbl5KF0ddGRz5XjeKWkOIXyrcGCpf5WJp%2BbqBZRvLoz%2BNvz5%2FYStjOlfdRN%2FGfo7%2FXhUCv2LMZwMf7qITv%2BRZLwIMPWzjL0GOqUBt4HAyKVS3Dm20dvIXAqWMpopUYC4Dd7CliwroDHY7NDr7SxvySR37msTmPe9WC%2BaA99RB5Jkt63SJ4plKHxx5NSPe%2B3V36cVciRrOvlNSEb1TXx9WjwT9QF4kMm9mkZX%2FNHwFoKO0NAUEMZr9BQhZ%2B93G0OY1amvF2HlBvOPtZi2t%2FbL7C2SMq3yWTr9B6qodJPmZV09%2FknlVCpAOievCuldTKEo&X-Amz-Signature=0d2820c596b31de500ce606dbcc302b348924f96c33295ad94b7fe40d8335c89&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TINOPOVD%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJHMEUCIFCam%2F6JjbkPSftgP8PfU3QcebDuQ1H7KwOaFds5izkeAiEA5FJErM5WGPSjOXavuvXH8QvkRtJ%2FvOf3RF5UJm4LZnoq%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDGhCGJu%2FJ6Vj5H%2FqXCrcAzaVwgfrvd42Rpz18jx7MRay6zeQAdVrX07xPMhIuVxATE4UY6XZhZKlagGEaZNi9c%2BOwPTzJ2DpFbJKZ2LlGwLGy9XhCUOr%2BL6cRJksQLeIhPT4NphckB6q3D5kiPFrKDjEvis5%2F3NQx%2F046PnJjtIk6V37KTX8rLlJPXxQzfMJMIAp2u1isDwqhzw4hVBiq8IZMaKZcZzTEycGWUqaXg9DSrHD%2F65ApA0w57xNir6XaH6CQXrdaEhFC12CODlFTyJXC2HHJoTo5L%2FvBDG8P3t%2FoRGHi5DiFv5bKqDYZBbKlaG2Z9EmVC4uO8Qx5GNrjCytkGNMON9JtiFjS1fCRUC3Lvps5nOacuKo9WmcioLaX7yJat%2BOiGJHlvv%2F0UjbnRYONFs9bPUJ8mSCJbg9xiFxzELTTTcKGDUnp74tSEs%2B4T%2Brnp31%2BVcIvs9r1rpiDmoLvVtYF2n2squYHxLtwu0vD5CBCnCM3RcDriSWfFrF8hy3rdulC2QOB%2F1LVS3OzwZD3AcLUz5Iayhb%2B6CCY3F3asxhT87SZUJkLbl5KF0ddGRz5XjeKWkOIXyrcGCpf5WJp%2BbqBZRvLoz%2BNvz5%2FYStjOlfdRN%2FGfo7%2FXhUCv2LMZwMf7qITv%2BRZLwIMPWzjL0GOqUBt4HAyKVS3Dm20dvIXAqWMpopUYC4Dd7CliwroDHY7NDr7SxvySR37msTmPe9WC%2BaA99RB5Jkt63SJ4plKHxx5NSPe%2B3V36cVciRrOvlNSEb1TXx9WjwT9QF4kMm9mkZX%2FNHwFoKO0NAUEMZr9BQhZ%2B93G0OY1amvF2HlBvOPtZi2t%2FbL7C2SMq3yWTr9B6qodJPmZV09%2FknlVCpAOievCuldTKEo&X-Amz-Signature=339c4806a8d2d4b595d01ac27169dbf4f310107e90177b467c207f8f2cf5f17c&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TINOPOVD%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJHMEUCIFCam%2F6JjbkPSftgP8PfU3QcebDuQ1H7KwOaFds5izkeAiEA5FJErM5WGPSjOXavuvXH8QvkRtJ%2FvOf3RF5UJm4LZnoq%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDGhCGJu%2FJ6Vj5H%2FqXCrcAzaVwgfrvd42Rpz18jx7MRay6zeQAdVrX07xPMhIuVxATE4UY6XZhZKlagGEaZNi9c%2BOwPTzJ2DpFbJKZ2LlGwLGy9XhCUOr%2BL6cRJksQLeIhPT4NphckB6q3D5kiPFrKDjEvis5%2F3NQx%2F046PnJjtIk6V37KTX8rLlJPXxQzfMJMIAp2u1isDwqhzw4hVBiq8IZMaKZcZzTEycGWUqaXg9DSrHD%2F65ApA0w57xNir6XaH6CQXrdaEhFC12CODlFTyJXC2HHJoTo5L%2FvBDG8P3t%2FoRGHi5DiFv5bKqDYZBbKlaG2Z9EmVC4uO8Qx5GNrjCytkGNMON9JtiFjS1fCRUC3Lvps5nOacuKo9WmcioLaX7yJat%2BOiGJHlvv%2F0UjbnRYONFs9bPUJ8mSCJbg9xiFxzELTTTcKGDUnp74tSEs%2B4T%2Brnp31%2BVcIvs9r1rpiDmoLvVtYF2n2squYHxLtwu0vD5CBCnCM3RcDriSWfFrF8hy3rdulC2QOB%2F1LVS3OzwZD3AcLUz5Iayhb%2B6CCY3F3asxhT87SZUJkLbl5KF0ddGRz5XjeKWkOIXyrcGCpf5WJp%2BbqBZRvLoz%2BNvz5%2FYStjOlfdRN%2FGfo7%2FXhUCv2LMZwMf7qITv%2BRZLwIMPWzjL0GOqUBt4HAyKVS3Dm20dvIXAqWMpopUYC4Dd7CliwroDHY7NDr7SxvySR37msTmPe9WC%2BaA99RB5Jkt63SJ4plKHxx5NSPe%2B3V36cVciRrOvlNSEb1TXx9WjwT9QF4kMm9mkZX%2FNHwFoKO0NAUEMZr9BQhZ%2B93G0OY1amvF2HlBvOPtZi2t%2FbL7C2SMq3yWTr9B6qodJPmZV09%2FknlVCpAOievCuldTKEo&X-Amz-Signature=799dfb3cb54bdce53cbf1405da8204b714ca13f9b90df9be583ce5b31502c811&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
