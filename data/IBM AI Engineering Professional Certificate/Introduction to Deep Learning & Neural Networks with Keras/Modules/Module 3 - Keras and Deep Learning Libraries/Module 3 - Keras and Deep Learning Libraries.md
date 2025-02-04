

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663YYFUWQ4%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJHMEUCIQDxhuWeelKCGiYFjsbMWfRXK8I1c466rZIaGvcoHVfCBAIgV%2BSkA%2F1uVWSL7AeflPHKNLzKQtfLrQU61YWRjGr7o2Yq%2FwMIIhAAGgw2Mzc0MjMxODM4MDUiDEsCRgFpyaJyR95WaircA8P5Pm0fdKmPNSa4bFDfNRStfHejXdQa5n3YU%2BzyMFsA8LJtQ4zVnx907oNh6Jnu%2BQq4BIL2tNZLGefdOd3NdwBsESsDmeoXjfHaAJ2ng5AQLyqRhR96koWp6Hq%2F4YtShGTr5a95CEoZEUPuo5mq%2B2wCSgub9s5eEWyeQ%2BoOaBAJw3CggMHpJZWGsMQ1l8PncIdDppF8ABIjj0KyCYTlObJ3JXTGEUDj6CQKGfp8B38BUTWKha7zLdTEKAEvDCYfmIb3CZ3A%2FCloC9q%2FI1o2Npv8%2FSXmx0IlTV4RT7CwHSPoadrQrqAXx7uvnDqbywwRgGOyp3lurKMso11Yl5G332wATtDHOkF2XEQmqsbCwPypz9feD9U4O4tdATnWpLDyxJAjemqFqwxCYeNFmxhCQyDDNvybuVJJjsItSlxPXk05LKY0AtnrqW4BiMCxla1QRFucHaAzjkSbbG3Ken9JOTEEnVlRVIHqQ3O3RWByLbMArkHltrSDnDJEwKMDI9NAA%2B17HYasbur8sqkGOOlGVBjGXqZ1yZfCukJziSxTW1xRgA%2FygyuyT3i9lfKfMt6ESiSirxyvyXEj1ennsnc1uOpjl5oVzi6T6e33c4CmRao%2FBUIYBIG1%2Fw4smI1IMO%2FMhb0GOqUBalWHF2SK%2F9%2F9KvNo0R2YdFhfKbRJLD7DBBCtNYjgUhjjIamcQ0JNKZ6qiVwcWJMJUA%2FD9vS0XTvp%2BSjlYrkmt0%2FCPCP5BK95UWj3yOmJUyEedQbGNlG195C%2BMH86widfTyfJrO%2F205HQs3BABPQi5vM68mWfNNs%2FeKZr04FrZzypNO5neshpynEOC%2BXGQaZg6hcKrrsKkIS9uVHse%2F9S%2BlkjtZUs&X-Amz-Signature=3e60ee78106ca9558088e81bc7042387b53dcc2743cec3bde10350550ff23e99&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663YYFUWQ4%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJHMEUCIQDxhuWeelKCGiYFjsbMWfRXK8I1c466rZIaGvcoHVfCBAIgV%2BSkA%2F1uVWSL7AeflPHKNLzKQtfLrQU61YWRjGr7o2Yq%2FwMIIhAAGgw2Mzc0MjMxODM4MDUiDEsCRgFpyaJyR95WaircA8P5Pm0fdKmPNSa4bFDfNRStfHejXdQa5n3YU%2BzyMFsA8LJtQ4zVnx907oNh6Jnu%2BQq4BIL2tNZLGefdOd3NdwBsESsDmeoXjfHaAJ2ng5AQLyqRhR96koWp6Hq%2F4YtShGTr5a95CEoZEUPuo5mq%2B2wCSgub9s5eEWyeQ%2BoOaBAJw3CggMHpJZWGsMQ1l8PncIdDppF8ABIjj0KyCYTlObJ3JXTGEUDj6CQKGfp8B38BUTWKha7zLdTEKAEvDCYfmIb3CZ3A%2FCloC9q%2FI1o2Npv8%2FSXmx0IlTV4RT7CwHSPoadrQrqAXx7uvnDqbywwRgGOyp3lurKMso11Yl5G332wATtDHOkF2XEQmqsbCwPypz9feD9U4O4tdATnWpLDyxJAjemqFqwxCYeNFmxhCQyDDNvybuVJJjsItSlxPXk05LKY0AtnrqW4BiMCxla1QRFucHaAzjkSbbG3Ken9JOTEEnVlRVIHqQ3O3RWByLbMArkHltrSDnDJEwKMDI9NAA%2B17HYasbur8sqkGOOlGVBjGXqZ1yZfCukJziSxTW1xRgA%2FygyuyT3i9lfKfMt6ESiSirxyvyXEj1ennsnc1uOpjl5oVzi6T6e33c4CmRao%2FBUIYBIG1%2Fw4smI1IMO%2FMhb0GOqUBalWHF2SK%2F9%2F9KvNo0R2YdFhfKbRJLD7DBBCtNYjgUhjjIamcQ0JNKZ6qiVwcWJMJUA%2FD9vS0XTvp%2BSjlYrkmt0%2FCPCP5BK95UWj3yOmJUyEedQbGNlG195C%2BMH86widfTyfJrO%2F205HQs3BABPQi5vM68mWfNNs%2FeKZr04FrZzypNO5neshpynEOC%2BXGQaZg6hcKrrsKkIS9uVHse%2F9S%2BlkjtZUs&X-Amz-Signature=3594014b9f94ee7b5893a9451fe3ca932c2eb52e5d4ce7b4570fbf26e98295d9&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663YYFUWQ4%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJHMEUCIQDxhuWeelKCGiYFjsbMWfRXK8I1c466rZIaGvcoHVfCBAIgV%2BSkA%2F1uVWSL7AeflPHKNLzKQtfLrQU61YWRjGr7o2Yq%2FwMIIhAAGgw2Mzc0MjMxODM4MDUiDEsCRgFpyaJyR95WaircA8P5Pm0fdKmPNSa4bFDfNRStfHejXdQa5n3YU%2BzyMFsA8LJtQ4zVnx907oNh6Jnu%2BQq4BIL2tNZLGefdOd3NdwBsESsDmeoXjfHaAJ2ng5AQLyqRhR96koWp6Hq%2F4YtShGTr5a95CEoZEUPuo5mq%2B2wCSgub9s5eEWyeQ%2BoOaBAJw3CggMHpJZWGsMQ1l8PncIdDppF8ABIjj0KyCYTlObJ3JXTGEUDj6CQKGfp8B38BUTWKha7zLdTEKAEvDCYfmIb3CZ3A%2FCloC9q%2FI1o2Npv8%2FSXmx0IlTV4RT7CwHSPoadrQrqAXx7uvnDqbywwRgGOyp3lurKMso11Yl5G332wATtDHOkF2XEQmqsbCwPypz9feD9U4O4tdATnWpLDyxJAjemqFqwxCYeNFmxhCQyDDNvybuVJJjsItSlxPXk05LKY0AtnrqW4BiMCxla1QRFucHaAzjkSbbG3Ken9JOTEEnVlRVIHqQ3O3RWByLbMArkHltrSDnDJEwKMDI9NAA%2B17HYasbur8sqkGOOlGVBjGXqZ1yZfCukJziSxTW1xRgA%2FygyuyT3i9lfKfMt6ESiSirxyvyXEj1ennsnc1uOpjl5oVzi6T6e33c4CmRao%2FBUIYBIG1%2Fw4smI1IMO%2FMhb0GOqUBalWHF2SK%2F9%2F9KvNo0R2YdFhfKbRJLD7DBBCtNYjgUhjjIamcQ0JNKZ6qiVwcWJMJUA%2FD9vS0XTvp%2BSjlYrkmt0%2FCPCP5BK95UWj3yOmJUyEedQbGNlG195C%2BMH86widfTyfJrO%2F205HQs3BABPQi5vM68mWfNNs%2FeKZr04FrZzypNO5neshpynEOC%2BXGQaZg6hcKrrsKkIS9uVHse%2F9S%2BlkjtZUs&X-Amz-Signature=90b94f953f5e3353c73ff6bbd35e83ca5f4969bebe1b61be33b110ac1fc58314&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DW2CWQC%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010833Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJIMEYCIQD%2BtLdmCjZPZJk5pCfftXP7aJr8esBU0y26yCTWU4zM%2BQIhALE%2BM6wpr8zU7RkbB846AXQz7ovWy5kd%2FY6D44GP3F9%2FKv8DCCIQABoMNjM3NDIzMTgzODA1IgzRVgBKokb0KdTd%2FWIq3AMu%2FNxRHNtl7AGs6r4UlFJZXJWKNMy36IWAC8s4PSTOqi6OI0Kr1GNU8OflKoNy5HObihffr1HB4fNJJ%2FmYCNIAHUdeSeMId82PKIY78aGs%2BhEItnijssrPgXgI0TeRLWiYxpQbjM%2BcXwz2VNQWpP5aYfXWz9jReGOjiwWlIiw7grlZJdbMRDlUJeBbJgBQWuYy5enfFxSkUfsOW%2BGwCArrlDckYHs%2BHAV89OIvdbsUfR09b%2Fp3C8wBKDF172JEOd6IpLrLLVCUhL7GGO3SGOrMrdKDMsl3FFYCfdHetBbY8dDvaCUg9iCoIb5yzPwGO3dUWTYQ94G5xP2oAKFO%2FHHrwJbQmf%2Fs8M%2FRfgQO%2FaDX6IQ296hiCGLMCTPrzOgoqAdiMEBBDSePgbyQ233%2BkQRtMO9cWcIu52Sc85wYfW%2FE0nW%2BNk8ktUyWPiAv6bfFdKHqOVtAl%2Br0cXNDLYDsVFuBwAgdgYlTCPjRvxGJxktwDy7%2BPcy10TTY12rQ9b8ibxsN5ZV5SU1atzgVU3j8ArJJwYUhLznjnk%2BKgL7KIxFP67wkB9hz7UmPKiYkW02MwBshKLF5hd9m%2BcsFTVUT91sc%2F3M6slxDC5xP5PS7Bpkcmpjn7ZaHyJrfEk4w5DDMzIW9BjqkAbizGJb4BkeMiL3InQ%2BAn0U3j64qwQS1OgodY%2BLkJcuA0N7M24aRyi%2FTIxCqC0lMdfS5WML4Sl0LWruKbnOGDwFCeN5zChvnt7wValTzVmb4XDaBJj2PZRqlTHsLx0RI7zUZapvxlg6%2FAO4WD3oghjR9p1eh5aTKqxlkn%2BGo0nDGHaurnNh2085Ve0uXKUft18jU60RZkpQr3AeruI0%2FuR22bhaK&X-Amz-Signature=c8765d079de232a294d3bd3a14c0cb753216046dbdf837532f44c96f3225ac59&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XO5VU4KC%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010833Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJIMEYCIQCW9JX2cegnRgBpIcnkJ5zcPIcKSc%2F2xu75LljIJkytVwIhAIDh4k7ZDUvWPlShxCuF0iXH2VC2yTDqlyUXO%2F6D4DaDKv8DCCIQABoMNjM3NDIzMTgzODA1Igzzw9Zqvo1g0Wxl0nwq3APDz0HbBiDa4hgS50oGeyAf4ocoW8IZhxnoc6sx4bY8PAgHgsw%2FgP4eAm7Ym1xA18Gfi4uYOIEG7PoOWdQXlvQKv98Jru%2BiCGy4MSZwV6Ak%2FTgrrejTaQCKR2prcLcFGds9F%2B7DjnGSnLQFKdIOEvFSyvt%2BiJ9rwpJukFiVMZ6xxexWtrwekW48U1x368bnEp6oB%2BXNRsPWqBLZja%2BUlgEublaLkNQMcGNrOvFZVpVZQZitFQkGlWkF0UOblkSCDifuBr4Gr7BeDujtB6BzAhJrzL8waoBO7erfUtlJJiLxKrrWdkvzR9Ovo0PxT0m0Y6B72F69Hzi2ANbfiiOMwRTuTfHvhqU4%2BewOqwZd3JXIF3p%2FRnjXATVNfBJ3J7yaTs8PY8tFhnpfVISWWO67E2lUfy6KKToCn4Ctn9M1eDN3qpXR3BRmIxq5SR%2FiQkXzef7UwuOiZLiYwZPKGKVLfkDAKltZWCO9A1J3huFxktXtoYpR5xhYO54JT8sAbjpnQPrRWDlDLaTEqAAmk2NG28hLyxkclGJ8BjtzjTS7mpixLrXbDViHiZi51DsJ240LT5XlGNgGCJX7zEu3kQZmJMhN1uxwlrsPZugtouNVpfsSwQYDEkIBrP6KaI9QTTDJzIW9BjqkAdVfs5b56h920zD4CjPOSetsYdjyNV%2FnvJ1CX6JfxCnFCc5CxE0FYvha0PeN8Aiwg3jwlp5FMqCb8HW97Qe83Rc2VEM9y1GnGlCDd9J%2F8Pv9026ApGusa%2FihoP40hpLQpubi3QwafVivHgQEEUuK4K7y%2F8G3uiGYBgUwJfoUCUB27t%2F%2ByEoBYXyScnMZVqk2Iz8JTxGCIk%2B2vKEtVmNGuRvsnDN9&X-Amz-Signature=0124609422d6547eba63e2a323e16ad506e4a78381b433b9c813cc289e0daae0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663YYFUWQ4%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJHMEUCIQDxhuWeelKCGiYFjsbMWfRXK8I1c466rZIaGvcoHVfCBAIgV%2BSkA%2F1uVWSL7AeflPHKNLzKQtfLrQU61YWRjGr7o2Yq%2FwMIIhAAGgw2Mzc0MjMxODM4MDUiDEsCRgFpyaJyR95WaircA8P5Pm0fdKmPNSa4bFDfNRStfHejXdQa5n3YU%2BzyMFsA8LJtQ4zVnx907oNh6Jnu%2BQq4BIL2tNZLGefdOd3NdwBsESsDmeoXjfHaAJ2ng5AQLyqRhR96koWp6Hq%2F4YtShGTr5a95CEoZEUPuo5mq%2B2wCSgub9s5eEWyeQ%2BoOaBAJw3CggMHpJZWGsMQ1l8PncIdDppF8ABIjj0KyCYTlObJ3JXTGEUDj6CQKGfp8B38BUTWKha7zLdTEKAEvDCYfmIb3CZ3A%2FCloC9q%2FI1o2Npv8%2FSXmx0IlTV4RT7CwHSPoadrQrqAXx7uvnDqbywwRgGOyp3lurKMso11Yl5G332wATtDHOkF2XEQmqsbCwPypz9feD9U4O4tdATnWpLDyxJAjemqFqwxCYeNFmxhCQyDDNvybuVJJjsItSlxPXk05LKY0AtnrqW4BiMCxla1QRFucHaAzjkSbbG3Ken9JOTEEnVlRVIHqQ3O3RWByLbMArkHltrSDnDJEwKMDI9NAA%2B17HYasbur8sqkGOOlGVBjGXqZ1yZfCukJziSxTW1xRgA%2FygyuyT3i9lfKfMt6ESiSirxyvyXEj1ennsnc1uOpjl5oVzi6T6e33c4CmRao%2FBUIYBIG1%2Fw4smI1IMO%2FMhb0GOqUBalWHF2SK%2F9%2F9KvNo0R2YdFhfKbRJLD7DBBCtNYjgUhjjIamcQ0JNKZ6qiVwcWJMJUA%2FD9vS0XTvp%2BSjlYrkmt0%2FCPCP5BK95UWj3yOmJUyEedQbGNlG195C%2BMH86widfTyfJrO%2F205HQs3BABPQi5vM68mWfNNs%2FeKZr04FrZzypNO5neshpynEOC%2BXGQaZg6hcKrrsKkIS9uVHse%2F9S%2BlkjtZUs&X-Amz-Signature=3ad3c8143f236caa7a35af91ca8621f2395f3effde44c7dd42cb61e94c2c468b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663YYFUWQ4%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJHMEUCIQDxhuWeelKCGiYFjsbMWfRXK8I1c466rZIaGvcoHVfCBAIgV%2BSkA%2F1uVWSL7AeflPHKNLzKQtfLrQU61YWRjGr7o2Yq%2FwMIIhAAGgw2Mzc0MjMxODM4MDUiDEsCRgFpyaJyR95WaircA8P5Pm0fdKmPNSa4bFDfNRStfHejXdQa5n3YU%2BzyMFsA8LJtQ4zVnx907oNh6Jnu%2BQq4BIL2tNZLGefdOd3NdwBsESsDmeoXjfHaAJ2ng5AQLyqRhR96koWp6Hq%2F4YtShGTr5a95CEoZEUPuo5mq%2B2wCSgub9s5eEWyeQ%2BoOaBAJw3CggMHpJZWGsMQ1l8PncIdDppF8ABIjj0KyCYTlObJ3JXTGEUDj6CQKGfp8B38BUTWKha7zLdTEKAEvDCYfmIb3CZ3A%2FCloC9q%2FI1o2Npv8%2FSXmx0IlTV4RT7CwHSPoadrQrqAXx7uvnDqbywwRgGOyp3lurKMso11Yl5G332wATtDHOkF2XEQmqsbCwPypz9feD9U4O4tdATnWpLDyxJAjemqFqwxCYeNFmxhCQyDDNvybuVJJjsItSlxPXk05LKY0AtnrqW4BiMCxla1QRFucHaAzjkSbbG3Ken9JOTEEnVlRVIHqQ3O3RWByLbMArkHltrSDnDJEwKMDI9NAA%2B17HYasbur8sqkGOOlGVBjGXqZ1yZfCukJziSxTW1xRgA%2FygyuyT3i9lfKfMt6ESiSirxyvyXEj1ennsnc1uOpjl5oVzi6T6e33c4CmRao%2FBUIYBIG1%2Fw4smI1IMO%2FMhb0GOqUBalWHF2SK%2F9%2F9KvNo0R2YdFhfKbRJLD7DBBCtNYjgUhjjIamcQ0JNKZ6qiVwcWJMJUA%2FD9vS0XTvp%2BSjlYrkmt0%2FCPCP5BK95UWj3yOmJUyEedQbGNlG195C%2BMH86widfTyfJrO%2F205HQs3BABPQi5vM68mWfNNs%2FeKZr04FrZzypNO5neshpynEOC%2BXGQaZg6hcKrrsKkIS9uVHse%2F9S%2BlkjtZUs&X-Amz-Signature=8690e0b27208edac595a32244e6e46a0e469e34eea4fb50ef810f835aab262a5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663YYFUWQ4%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJHMEUCIQDxhuWeelKCGiYFjsbMWfRXK8I1c466rZIaGvcoHVfCBAIgV%2BSkA%2F1uVWSL7AeflPHKNLzKQtfLrQU61YWRjGr7o2Yq%2FwMIIhAAGgw2Mzc0MjMxODM4MDUiDEsCRgFpyaJyR95WaircA8P5Pm0fdKmPNSa4bFDfNRStfHejXdQa5n3YU%2BzyMFsA8LJtQ4zVnx907oNh6Jnu%2BQq4BIL2tNZLGefdOd3NdwBsESsDmeoXjfHaAJ2ng5AQLyqRhR96koWp6Hq%2F4YtShGTr5a95CEoZEUPuo5mq%2B2wCSgub9s5eEWyeQ%2BoOaBAJw3CggMHpJZWGsMQ1l8PncIdDppF8ABIjj0KyCYTlObJ3JXTGEUDj6CQKGfp8B38BUTWKha7zLdTEKAEvDCYfmIb3CZ3A%2FCloC9q%2FI1o2Npv8%2FSXmx0IlTV4RT7CwHSPoadrQrqAXx7uvnDqbywwRgGOyp3lurKMso11Yl5G332wATtDHOkF2XEQmqsbCwPypz9feD9U4O4tdATnWpLDyxJAjemqFqwxCYeNFmxhCQyDDNvybuVJJjsItSlxPXk05LKY0AtnrqW4BiMCxla1QRFucHaAzjkSbbG3Ken9JOTEEnVlRVIHqQ3O3RWByLbMArkHltrSDnDJEwKMDI9NAA%2B17HYasbur8sqkGOOlGVBjGXqZ1yZfCukJziSxTW1xRgA%2FygyuyT3i9lfKfMt6ESiSirxyvyXEj1ennsnc1uOpjl5oVzi6T6e33c4CmRao%2FBUIYBIG1%2Fw4smI1IMO%2FMhb0GOqUBalWHF2SK%2F9%2F9KvNo0R2YdFhfKbRJLD7DBBCtNYjgUhjjIamcQ0JNKZ6qiVwcWJMJUA%2FD9vS0XTvp%2BSjlYrkmt0%2FCPCP5BK95UWj3yOmJUyEedQbGNlG195C%2BMH86widfTyfJrO%2F205HQs3BABPQi5vM68mWfNNs%2FeKZr04FrZzypNO5neshpynEOC%2BXGQaZg6hcKrrsKkIS9uVHse%2F9S%2BlkjtZUs&X-Amz-Signature=bd5bc58c258df41b230a99e6631fd2441231feab32dd40c4f1b131024f6b9495&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663YYFUWQ4%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJHMEUCIQDxhuWeelKCGiYFjsbMWfRXK8I1c466rZIaGvcoHVfCBAIgV%2BSkA%2F1uVWSL7AeflPHKNLzKQtfLrQU61YWRjGr7o2Yq%2FwMIIhAAGgw2Mzc0MjMxODM4MDUiDEsCRgFpyaJyR95WaircA8P5Pm0fdKmPNSa4bFDfNRStfHejXdQa5n3YU%2BzyMFsA8LJtQ4zVnx907oNh6Jnu%2BQq4BIL2tNZLGefdOd3NdwBsESsDmeoXjfHaAJ2ng5AQLyqRhR96koWp6Hq%2F4YtShGTr5a95CEoZEUPuo5mq%2B2wCSgub9s5eEWyeQ%2BoOaBAJw3CggMHpJZWGsMQ1l8PncIdDppF8ABIjj0KyCYTlObJ3JXTGEUDj6CQKGfp8B38BUTWKha7zLdTEKAEvDCYfmIb3CZ3A%2FCloC9q%2FI1o2Npv8%2FSXmx0IlTV4RT7CwHSPoadrQrqAXx7uvnDqbywwRgGOyp3lurKMso11Yl5G332wATtDHOkF2XEQmqsbCwPypz9feD9U4O4tdATnWpLDyxJAjemqFqwxCYeNFmxhCQyDDNvybuVJJjsItSlxPXk05LKY0AtnrqW4BiMCxla1QRFucHaAzjkSbbG3Ken9JOTEEnVlRVIHqQ3O3RWByLbMArkHltrSDnDJEwKMDI9NAA%2B17HYasbur8sqkGOOlGVBjGXqZ1yZfCukJziSxTW1xRgA%2FygyuyT3i9lfKfMt6ESiSirxyvyXEj1ennsnc1uOpjl5oVzi6T6e33c4CmRao%2FBUIYBIG1%2Fw4smI1IMO%2FMhb0GOqUBalWHF2SK%2F9%2F9KvNo0R2YdFhfKbRJLD7DBBCtNYjgUhjjIamcQ0JNKZ6qiVwcWJMJUA%2FD9vS0XTvp%2BSjlYrkmt0%2FCPCP5BK95UWj3yOmJUyEedQbGNlG195C%2BMH86widfTyfJrO%2F205HQs3BABPQi5vM68mWfNNs%2FeKZr04FrZzypNO5neshpynEOC%2BXGQaZg6hcKrrsKkIS9uVHse%2F9S%2BlkjtZUs&X-Amz-Signature=484dbe42e345c4753a551e63ae36e0be7ec2093e89b7efb2b3250592feca9420&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
