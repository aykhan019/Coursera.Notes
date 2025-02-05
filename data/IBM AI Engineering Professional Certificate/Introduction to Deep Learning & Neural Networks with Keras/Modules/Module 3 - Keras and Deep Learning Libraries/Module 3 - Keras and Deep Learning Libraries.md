

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667WL3M6KO%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQDSXQIvwYmowHtHRtG7k1PXSQla2BJSWNpBdM5r8y5%2F5wIhALuU4Z%2FtmruMNTE6cYscKiU%2FUm3olRu1bIbeU5FFa%2FQGKv8DCEQQABoMNjM3NDIzMTgzODA1IgyPmL9LpOcFTt8kg6gq3APAvHokWVLBXdBBxHv46cDvFpiOeyVsSEBbuVzuv%2FD2TALJF8hSSUVlyXr0RAUCiZEykZJzRcT90wLa1Eu9WF9PaT088Zm7OcDDOYeLCG9BhjBPvYimWFUhk%2FqUzfvSKm%2BJrsjNBkq2vOqHdg2leW%2FFbGoNW3lBihV2OHr%2BxaPM5URVZ4CogOoACyxtoKNLPzUfp9VHXpnacdIWXaVT8Mh%2FZM%2BdJ5%2BVfMNm7t8SoREMLvNBnuNGUFyS%2Fs3z%2BREMHjmBMrJiaLgu07B%2FfLrVJALINkTHDEMX5zohK7djl6pxWVBHAZJHcQZNuSFi9ytTY9%2BHXF3ifrkB%2Ft7Cvx2XaGQEDTY8RVwYDaOstxkwEJ5lwpw8jNuVTtfxeB4HOUQi2VIhjfKiq4RHTvsNEAct8XPqyhoLxfNnY5JgA%2BuIzsApqCvNXoAoiObffWm%2BC9y5l9G%2B9EMADNkGG0QDD65eWm88c%2BsdxhQVdjkhlRe9AziNbUKDQTXpOVgzaja27YJJQH%2BtiCBrz3a5YuquwvLTGt8mUqDJnGkUH7%2FJrlElBOa%2FtGqT%2Bp5a5aKnfnLrEy1xQKO1%2Bi8u8YaExgDLLkn4S6SY18XsJgiXopCewZiWiQTUrrgSjHZxyuISyGErKTCejI29BjqkAeXr%2BRcvC6u5ogs4m03iER8UsH6qtBbUOJ%2BjnyISrmk4hbzPf%2F0p%2F4ouNADdnMK4loC6m%2FTIJnClJOrzm8o0JR5u4C0sTC3MKIh4eQmgYafcxtn1DimWV2ZZ0Je6SAczn1W7BBqcqCZIL1h4lQozKQjqdC6Mse9f%2Fd20Ph59EFS5tcJmQ0b1rFpObcfT%2F0n28npPNZ1ymlA32GdR9UIwcCOqjdDN&X-Amz-Signature=0d5a0b336c1de05e7926361c66976641111cd6d504628b17198f62ff590c4bbc&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667WL3M6KO%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQDSXQIvwYmowHtHRtG7k1PXSQla2BJSWNpBdM5r8y5%2F5wIhALuU4Z%2FtmruMNTE6cYscKiU%2FUm3olRu1bIbeU5FFa%2FQGKv8DCEQQABoMNjM3NDIzMTgzODA1IgyPmL9LpOcFTt8kg6gq3APAvHokWVLBXdBBxHv46cDvFpiOeyVsSEBbuVzuv%2FD2TALJF8hSSUVlyXr0RAUCiZEykZJzRcT90wLa1Eu9WF9PaT088Zm7OcDDOYeLCG9BhjBPvYimWFUhk%2FqUzfvSKm%2BJrsjNBkq2vOqHdg2leW%2FFbGoNW3lBihV2OHr%2BxaPM5URVZ4CogOoACyxtoKNLPzUfp9VHXpnacdIWXaVT8Mh%2FZM%2BdJ5%2BVfMNm7t8SoREMLvNBnuNGUFyS%2Fs3z%2BREMHjmBMrJiaLgu07B%2FfLrVJALINkTHDEMX5zohK7djl6pxWVBHAZJHcQZNuSFi9ytTY9%2BHXF3ifrkB%2Ft7Cvx2XaGQEDTY8RVwYDaOstxkwEJ5lwpw8jNuVTtfxeB4HOUQi2VIhjfKiq4RHTvsNEAct8XPqyhoLxfNnY5JgA%2BuIzsApqCvNXoAoiObffWm%2BC9y5l9G%2B9EMADNkGG0QDD65eWm88c%2BsdxhQVdjkhlRe9AziNbUKDQTXpOVgzaja27YJJQH%2BtiCBrz3a5YuquwvLTGt8mUqDJnGkUH7%2FJrlElBOa%2FtGqT%2Bp5a5aKnfnLrEy1xQKO1%2Bi8u8YaExgDLLkn4S6SY18XsJgiXopCewZiWiQTUrrgSjHZxyuISyGErKTCejI29BjqkAeXr%2BRcvC6u5ogs4m03iER8UsH6qtBbUOJ%2BjnyISrmk4hbzPf%2F0p%2F4ouNADdnMK4loC6m%2FTIJnClJOrzm8o0JR5u4C0sTC3MKIh4eQmgYafcxtn1DimWV2ZZ0Je6SAczn1W7BBqcqCZIL1h4lQozKQjqdC6Mse9f%2Fd20Ph59EFS5tcJmQ0b1rFpObcfT%2F0n28npPNZ1ymlA32GdR9UIwcCOqjdDN&X-Amz-Signature=7e7fa09d78ace24b8a7ac394538e4dba3c5adc214708b15387ae75d1ff59b007&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667WL3M6KO%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQDSXQIvwYmowHtHRtG7k1PXSQla2BJSWNpBdM5r8y5%2F5wIhALuU4Z%2FtmruMNTE6cYscKiU%2FUm3olRu1bIbeU5FFa%2FQGKv8DCEQQABoMNjM3NDIzMTgzODA1IgyPmL9LpOcFTt8kg6gq3APAvHokWVLBXdBBxHv46cDvFpiOeyVsSEBbuVzuv%2FD2TALJF8hSSUVlyXr0RAUCiZEykZJzRcT90wLa1Eu9WF9PaT088Zm7OcDDOYeLCG9BhjBPvYimWFUhk%2FqUzfvSKm%2BJrsjNBkq2vOqHdg2leW%2FFbGoNW3lBihV2OHr%2BxaPM5URVZ4CogOoACyxtoKNLPzUfp9VHXpnacdIWXaVT8Mh%2FZM%2BdJ5%2BVfMNm7t8SoREMLvNBnuNGUFyS%2Fs3z%2BREMHjmBMrJiaLgu07B%2FfLrVJALINkTHDEMX5zohK7djl6pxWVBHAZJHcQZNuSFi9ytTY9%2BHXF3ifrkB%2Ft7Cvx2XaGQEDTY8RVwYDaOstxkwEJ5lwpw8jNuVTtfxeB4HOUQi2VIhjfKiq4RHTvsNEAct8XPqyhoLxfNnY5JgA%2BuIzsApqCvNXoAoiObffWm%2BC9y5l9G%2B9EMADNkGG0QDD65eWm88c%2BsdxhQVdjkhlRe9AziNbUKDQTXpOVgzaja27YJJQH%2BtiCBrz3a5YuquwvLTGt8mUqDJnGkUH7%2FJrlElBOa%2FtGqT%2Bp5a5aKnfnLrEy1xQKO1%2Bi8u8YaExgDLLkn4S6SY18XsJgiXopCewZiWiQTUrrgSjHZxyuISyGErKTCejI29BjqkAeXr%2BRcvC6u5ogs4m03iER8UsH6qtBbUOJ%2BjnyISrmk4hbzPf%2F0p%2F4ouNADdnMK4loC6m%2FTIJnClJOrzm8o0JR5u4C0sTC3MKIh4eQmgYafcxtn1DimWV2ZZ0Je6SAczn1W7BBqcqCZIL1h4lQozKQjqdC6Mse9f%2Fd20Ph59EFS5tcJmQ0b1rFpObcfT%2F0n28npPNZ1ymlA32GdR9UIwcCOqjdDN&X-Amz-Signature=3d0d38bd632e95de643fede4cb8f6e9c0b657f2e0a65569196977fc6cbb0b401&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XIKJZKB4%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQDSUPQfWtaWHwV%2BPeUP03rV8cjhWMl6bpA3X7L25hRm4gIhAJKEqk9AIOZ85pL3q%2BgSXX9Ff00VdmLYnEuF1nyhtxBgKv8DCEQQABoMNjM3NDIzMTgzODA1IgxTGY3ku6Q3%2Bl67ojYq3APF%2Be%2FIiVcqBmpDQQ4o%2BofNzMS01TuoAE0XymD3vJ8hFXGHn73YiEQhe6XMkTphVDgmD7jwo%2FKdwWmXLqzFyI0JNN8rC0ksrrYe6RPNE08llAxknxkVTaDoJo5btitmnp7BqVsN9AKoohY6E4PycTQZwEEA6JzEB6W5JLmpFHcaXKaIiYg9hNH18m8hSFOP64JAMrkto18J4Ac2CIeRMiW%2BV%2FC8%2FhBXrTbHxXo%2Fd8TT9VfgqUQZ5VfR%2BWdZmAXF4JAhfedQPE%2F6Xqd96CZ84ctXuqVRzQcmbYT36NMRynDPmeFL9ivMP9Xl%2BAkdzoRDh2eJHpTCSEZ7DNrIjAp%2B3bn5EMg6pIFuEP%2FWAGrHM16X6X4o%2F99pin7ETMtdej8WZhHZmlP%2BdLNdhtHBtu2fpTnPuH8uRFezA9e2y8jYohlt2B5GRPvFwcjo02npKTjY5tYoy%2BYxWrR1IjFi6wXQVeOxtwonhpW6RUFFqvmgCdSZQTcMmVXw1BNgX2IBjFrNrtPsiTfE88PGsbDvQa3KYG4eLoZX%2Fv2I3khrAPxrtrVXTbT4w01Th6N7mFtS3Bi82RpQdoj9MXYSV8sxW82PyfhLrar2JgipGxNKslP5CtCanLcy0p8xS6w36OwTbDD9io29BjqkAVBCSCVQTEsoNzs8M9b%2FZHZ%2FY2fiD4H32S83UvN6O6FUbQ5dCd%2FdLJmzJTLfsDMauuCF4TTyOZzv8XMW1hqIEZQjTowanWdXm27zSbtGTR2wKCe9myJ0zxfG%2BnzGn1OxnO7JP%2BaoUn4%2BzDuv3KITY8%2Bd14HSchOSeHIfcGxNtPRKfDYiG22sSSooI%2BcL%2F9MJYEH8LPFvBav1b8%2FWF2PaYuLb7ygI&X-Amz-Signature=213dc25d2a5c66dba847ac3622c04726344dd71223c3738789f56b6d576119f4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ZFJ6QLK%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIQCHOyA9t6FkraiOxxY7btfd47Ccg3uMsyU0dkZOKXxVRQIgcPVcKCv%2BRwxViY5SN1f%2BOM8ZAVaqiZF0Qz5mSxMyzEQq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDPJMitI9zJHJ96Wo8yrcA0BWLI%2BTojcb%2FEQCkNzNa%2B2BoexyHAwxHLskLCvq5chbSNyhNls7jyZmtc7ldnfh96mRmtAs6ZWaKzgwxc%2Feo0HH93Y%2F6YyrgHtyl9MTTomBJQ16OTHd61w%2B63hwAJh2r030SraiHIpj3EuQqYGVjgqVAjND0lAgTNk2pfJ%2FccVwwVv%2FucMmWX5GDEkV0Fz2o7W0WL97I5XVo1q41Z6sEUkbeoed2bXfCHtTq1a%2FtLKG2VPts7QjEIaOCC1sfLbClX%2FLZlpgbSyRjqcEus8xnYQF3YxMGYCmzZ5GQ6jxSKi%2BwrqKy%2FdN5MmG7Kg%2BIsr85lMbGEFbhE2xQVeRessGgHGfvRnbiQXdbQHxF6Ms23l4JLD3cOEs%2BiOazaC8HxcT2U7OQpy7f9O2vMi0%2FluMmsi7fz4MowXMZcj%2FYtgHZsDw9PwJvaw4836lWNfKNfbdH%2BqnDyxL7LERrzLU8TFXbIL4hFjxijE8L4404SpKFFHvCtBOrszzgRUCKlR%2B2C8D84L3NO4FyoOa%2BnFhFb%2Bjc3H6SfaZXd27BE66pGFUc5eImkW3Dl4%2FCgaI66Tf8so5D1K61iFdHSd1v6IylBryNfQzHYAtKY%2FyV8TcXgZxFeP2OeF47UFlAYnJ8aR9MJyLjb0GOqUBAwYJtFqWgObhLKMPcrQPXIs6DXJsUCINIFTAHkoOfokydOM8Iu5dkToph4Z34OqArBzuV%2F5Bkb%2F651foXCxOTWqeMVN1BIPX%2FowOabQW4RjCe8SllwmO2eYn2Iq99C1zoSci1sQ8Ori5bSTX0N%2BWxbUQXLSfw%2BUbi5edR%2BDVXMLdmK%2FiyYyh2l8zTiKjlXN23ORT8xzLewY9xOe6XD0hdPucEJA%2B&X-Amz-Signature=7d1b4d627a58e1a160b26468e10524db08dfddccf0e694f355479c2f7d9dd93b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667WL3M6KO%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQDSXQIvwYmowHtHRtG7k1PXSQla2BJSWNpBdM5r8y5%2F5wIhALuU4Z%2FtmruMNTE6cYscKiU%2FUm3olRu1bIbeU5FFa%2FQGKv8DCEQQABoMNjM3NDIzMTgzODA1IgyPmL9LpOcFTt8kg6gq3APAvHokWVLBXdBBxHv46cDvFpiOeyVsSEBbuVzuv%2FD2TALJF8hSSUVlyXr0RAUCiZEykZJzRcT90wLa1Eu9WF9PaT088Zm7OcDDOYeLCG9BhjBPvYimWFUhk%2FqUzfvSKm%2BJrsjNBkq2vOqHdg2leW%2FFbGoNW3lBihV2OHr%2BxaPM5URVZ4CogOoACyxtoKNLPzUfp9VHXpnacdIWXaVT8Mh%2FZM%2BdJ5%2BVfMNm7t8SoREMLvNBnuNGUFyS%2Fs3z%2BREMHjmBMrJiaLgu07B%2FfLrVJALINkTHDEMX5zohK7djl6pxWVBHAZJHcQZNuSFi9ytTY9%2BHXF3ifrkB%2Ft7Cvx2XaGQEDTY8RVwYDaOstxkwEJ5lwpw8jNuVTtfxeB4HOUQi2VIhjfKiq4RHTvsNEAct8XPqyhoLxfNnY5JgA%2BuIzsApqCvNXoAoiObffWm%2BC9y5l9G%2B9EMADNkGG0QDD65eWm88c%2BsdxhQVdjkhlRe9AziNbUKDQTXpOVgzaja27YJJQH%2BtiCBrz3a5YuquwvLTGt8mUqDJnGkUH7%2FJrlElBOa%2FtGqT%2Bp5a5aKnfnLrEy1xQKO1%2Bi8u8YaExgDLLkn4S6SY18XsJgiXopCewZiWiQTUrrgSjHZxyuISyGErKTCejI29BjqkAeXr%2BRcvC6u5ogs4m03iER8UsH6qtBbUOJ%2BjnyISrmk4hbzPf%2F0p%2F4ouNADdnMK4loC6m%2FTIJnClJOrzm8o0JR5u4C0sTC3MKIh4eQmgYafcxtn1DimWV2ZZ0Je6SAczn1W7BBqcqCZIL1h4lQozKQjqdC6Mse9f%2Fd20Ph59EFS5tcJmQ0b1rFpObcfT%2F0n28npPNZ1ymlA32GdR9UIwcCOqjdDN&X-Amz-Signature=72b028d2ec8707a33d0b0a70c3920aa90609910734d011946c9ec29eb573aa09&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667WL3M6KO%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQDSXQIvwYmowHtHRtG7k1PXSQla2BJSWNpBdM5r8y5%2F5wIhALuU4Z%2FtmruMNTE6cYscKiU%2FUm3olRu1bIbeU5FFa%2FQGKv8DCEQQABoMNjM3NDIzMTgzODA1IgyPmL9LpOcFTt8kg6gq3APAvHokWVLBXdBBxHv46cDvFpiOeyVsSEBbuVzuv%2FD2TALJF8hSSUVlyXr0RAUCiZEykZJzRcT90wLa1Eu9WF9PaT088Zm7OcDDOYeLCG9BhjBPvYimWFUhk%2FqUzfvSKm%2BJrsjNBkq2vOqHdg2leW%2FFbGoNW3lBihV2OHr%2BxaPM5URVZ4CogOoACyxtoKNLPzUfp9VHXpnacdIWXaVT8Mh%2FZM%2BdJ5%2BVfMNm7t8SoREMLvNBnuNGUFyS%2Fs3z%2BREMHjmBMrJiaLgu07B%2FfLrVJALINkTHDEMX5zohK7djl6pxWVBHAZJHcQZNuSFi9ytTY9%2BHXF3ifrkB%2Ft7Cvx2XaGQEDTY8RVwYDaOstxkwEJ5lwpw8jNuVTtfxeB4HOUQi2VIhjfKiq4RHTvsNEAct8XPqyhoLxfNnY5JgA%2BuIzsApqCvNXoAoiObffWm%2BC9y5l9G%2B9EMADNkGG0QDD65eWm88c%2BsdxhQVdjkhlRe9AziNbUKDQTXpOVgzaja27YJJQH%2BtiCBrz3a5YuquwvLTGt8mUqDJnGkUH7%2FJrlElBOa%2FtGqT%2Bp5a5aKnfnLrEy1xQKO1%2Bi8u8YaExgDLLkn4S6SY18XsJgiXopCewZiWiQTUrrgSjHZxyuISyGErKTCejI29BjqkAeXr%2BRcvC6u5ogs4m03iER8UsH6qtBbUOJ%2BjnyISrmk4hbzPf%2F0p%2F4ouNADdnMK4loC6m%2FTIJnClJOrzm8o0JR5u4C0sTC3MKIh4eQmgYafcxtn1DimWV2ZZ0Je6SAczn1W7BBqcqCZIL1h4lQozKQjqdC6Mse9f%2Fd20Ph59EFS5tcJmQ0b1rFpObcfT%2F0n28npPNZ1ymlA32GdR9UIwcCOqjdDN&X-Amz-Signature=e644f1f76aa3bdf8be028ab0efafb43f82616f57895a2d6ab141108c066857c8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667WL3M6KO%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQDSXQIvwYmowHtHRtG7k1PXSQla2BJSWNpBdM5r8y5%2F5wIhALuU4Z%2FtmruMNTE6cYscKiU%2FUm3olRu1bIbeU5FFa%2FQGKv8DCEQQABoMNjM3NDIzMTgzODA1IgyPmL9LpOcFTt8kg6gq3APAvHokWVLBXdBBxHv46cDvFpiOeyVsSEBbuVzuv%2FD2TALJF8hSSUVlyXr0RAUCiZEykZJzRcT90wLa1Eu9WF9PaT088Zm7OcDDOYeLCG9BhjBPvYimWFUhk%2FqUzfvSKm%2BJrsjNBkq2vOqHdg2leW%2FFbGoNW3lBihV2OHr%2BxaPM5URVZ4CogOoACyxtoKNLPzUfp9VHXpnacdIWXaVT8Mh%2FZM%2BdJ5%2BVfMNm7t8SoREMLvNBnuNGUFyS%2Fs3z%2BREMHjmBMrJiaLgu07B%2FfLrVJALINkTHDEMX5zohK7djl6pxWVBHAZJHcQZNuSFi9ytTY9%2BHXF3ifrkB%2Ft7Cvx2XaGQEDTY8RVwYDaOstxkwEJ5lwpw8jNuVTtfxeB4HOUQi2VIhjfKiq4RHTvsNEAct8XPqyhoLxfNnY5JgA%2BuIzsApqCvNXoAoiObffWm%2BC9y5l9G%2B9EMADNkGG0QDD65eWm88c%2BsdxhQVdjkhlRe9AziNbUKDQTXpOVgzaja27YJJQH%2BtiCBrz3a5YuquwvLTGt8mUqDJnGkUH7%2FJrlElBOa%2FtGqT%2Bp5a5aKnfnLrEy1xQKO1%2Bi8u8YaExgDLLkn4S6SY18XsJgiXopCewZiWiQTUrrgSjHZxyuISyGErKTCejI29BjqkAeXr%2BRcvC6u5ogs4m03iER8UsH6qtBbUOJ%2BjnyISrmk4hbzPf%2F0p%2F4ouNADdnMK4loC6m%2FTIJnClJOrzm8o0JR5u4C0sTC3MKIh4eQmgYafcxtn1DimWV2ZZ0Je6SAczn1W7BBqcqCZIL1h4lQozKQjqdC6Mse9f%2Fd20Ph59EFS5tcJmQ0b1rFpObcfT%2F0n28npPNZ1ymlA32GdR9UIwcCOqjdDN&X-Amz-Signature=9e25f5d6f88e5dae4f721c9dcb9f78505f6788649c9657e68cefc915ec001b2b&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667WL3M6KO%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQDSXQIvwYmowHtHRtG7k1PXSQla2BJSWNpBdM5r8y5%2F5wIhALuU4Z%2FtmruMNTE6cYscKiU%2FUm3olRu1bIbeU5FFa%2FQGKv8DCEQQABoMNjM3NDIzMTgzODA1IgyPmL9LpOcFTt8kg6gq3APAvHokWVLBXdBBxHv46cDvFpiOeyVsSEBbuVzuv%2FD2TALJF8hSSUVlyXr0RAUCiZEykZJzRcT90wLa1Eu9WF9PaT088Zm7OcDDOYeLCG9BhjBPvYimWFUhk%2FqUzfvSKm%2BJrsjNBkq2vOqHdg2leW%2FFbGoNW3lBihV2OHr%2BxaPM5URVZ4CogOoACyxtoKNLPzUfp9VHXpnacdIWXaVT8Mh%2FZM%2BdJ5%2BVfMNm7t8SoREMLvNBnuNGUFyS%2Fs3z%2BREMHjmBMrJiaLgu07B%2FfLrVJALINkTHDEMX5zohK7djl6pxWVBHAZJHcQZNuSFi9ytTY9%2BHXF3ifrkB%2Ft7Cvx2XaGQEDTY8RVwYDaOstxkwEJ5lwpw8jNuVTtfxeB4HOUQi2VIhjfKiq4RHTvsNEAct8XPqyhoLxfNnY5JgA%2BuIzsApqCvNXoAoiObffWm%2BC9y5l9G%2B9EMADNkGG0QDD65eWm88c%2BsdxhQVdjkhlRe9AziNbUKDQTXpOVgzaja27YJJQH%2BtiCBrz3a5YuquwvLTGt8mUqDJnGkUH7%2FJrlElBOa%2FtGqT%2Bp5a5aKnfnLrEy1xQKO1%2Bi8u8YaExgDLLkn4S6SY18XsJgiXopCewZiWiQTUrrgSjHZxyuISyGErKTCejI29BjqkAeXr%2BRcvC6u5ogs4m03iER8UsH6qtBbUOJ%2BjnyISrmk4hbzPf%2F0p%2F4ouNADdnMK4loC6m%2FTIJnClJOrzm8o0JR5u4C0sTC3MKIh4eQmgYafcxtn1DimWV2ZZ0Je6SAczn1W7BBqcqCZIL1h4lQozKQjqdC6Mse9f%2Fd20Ph59EFS5tcJmQ0b1rFpObcfT%2F0n28npPNZ1ymlA32GdR9UIwcCOqjdDN&X-Amz-Signature=e3ea59d5b9ba2000fb689a33b382cfce2d47664614b3b0874be13bfd14d4f580&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
