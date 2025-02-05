

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UEIUTW4N%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182015Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQCic2Fkt9SvVT%2B61RsTVhZijMXxYRbo7aPfTY0oVcT1VAIhAPQtW7okQurXDqFFCZco9vBS5Ojs4g%2F%2BA%2BEFdq6om2O%2FKv8DCEoQABoMNjM3NDIzMTgzODA1IgzaYOoTJs6bxGGFzdoq3AOxePKvNamD0%2BmGCm4sgDdkMjLFx3sfKz4Nb6xo1CnCBjiKQYU8dbIC4DJZZbn0bamLl%2FoRqBpLkIGTk0ElDYAVvZoVPvILXIQ705XQBow5evTlLO5h%2F%2BFA%2FeyoyszpxBptVBHsuc5vm9Eghq0OHA%2BbzQF63ocaReuNMy1HnN5PCiqWe1NB06UCWm03vF9muBDRsvyDe8O7d96QV7g10fH17gXp0gfRUlL9HXL%2BQXE%2B3l2xTQ6RVU2G2KTRIrHFBT2g5fIAAcx60owBL4WKiQDBHyo9Rys5niAXFBFFcyVMqMCFppBitTdnHbThnAFQuUbpymY7dU4JLfNz6%2BKg%2BEJKx8YxOGh8r6quFe%2FDvONmo%2Fa8lQYPSFBusl9jYZaispRxyo95yUQG4ivxrqKRoVvF9P5cyl3oHKkHHn%2FLOna4uhs03hpHp%2BbWkYZfdMW0ue%2BDebAS%2Fjaj95GoYM8qIqDzJ8rWXHnYB6l5tMnz7MN%2FRxsGKSarfz9mzGQ%2B7ldsd2L5wF5L33cNbTAAETBlTKvsda31%2BnPLqdngASC5bnD9x%2FLioM9RSRw8A9FZl%2FTkFlA3l440Gs3Ye5wt9PcdioaPw7majmMQ%2BlDIzc8R2FDwM0Lyt5ZrlXnLD38WfTDnuo69BjqkAeudhrEhdj88xY4eIGQ0Ejrl00htyAF4%2FA6kuf7p7QCJ5pS6e%2BRM%2B%2B70Jqin0fW5hCUg8IRVppeh2bfnyDZZBWGukfpG6Shy41OVHeMWcupgBzn1Ov0Ze8K1TuE2gLJLlCKHWUEgVe2nOMpaJ3eGB3vEGeV4H24DYOb2qo7s%2BwhpwA18t8hW3jcN%2Bx5%2Fb0r3bbEytfjuO9tzDkWvd7sm%2Fl4RaUSb&X-Amz-Signature=b0d9f194e4c0a2a55b2b50804d2bb0f10a00aaf468e38fa727b1780e69ca093f&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UEIUTW4N%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182015Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQCic2Fkt9SvVT%2B61RsTVhZijMXxYRbo7aPfTY0oVcT1VAIhAPQtW7okQurXDqFFCZco9vBS5Ojs4g%2F%2BA%2BEFdq6om2O%2FKv8DCEoQABoMNjM3NDIzMTgzODA1IgzaYOoTJs6bxGGFzdoq3AOxePKvNamD0%2BmGCm4sgDdkMjLFx3sfKz4Nb6xo1CnCBjiKQYU8dbIC4DJZZbn0bamLl%2FoRqBpLkIGTk0ElDYAVvZoVPvILXIQ705XQBow5evTlLO5h%2F%2BFA%2FeyoyszpxBptVBHsuc5vm9Eghq0OHA%2BbzQF63ocaReuNMy1HnN5PCiqWe1NB06UCWm03vF9muBDRsvyDe8O7d96QV7g10fH17gXp0gfRUlL9HXL%2BQXE%2B3l2xTQ6RVU2G2KTRIrHFBT2g5fIAAcx60owBL4WKiQDBHyo9Rys5niAXFBFFcyVMqMCFppBitTdnHbThnAFQuUbpymY7dU4JLfNz6%2BKg%2BEJKx8YxOGh8r6quFe%2FDvONmo%2Fa8lQYPSFBusl9jYZaispRxyo95yUQG4ivxrqKRoVvF9P5cyl3oHKkHHn%2FLOna4uhs03hpHp%2BbWkYZfdMW0ue%2BDebAS%2Fjaj95GoYM8qIqDzJ8rWXHnYB6l5tMnz7MN%2FRxsGKSarfz9mzGQ%2B7ldsd2L5wF5L33cNbTAAETBlTKvsda31%2BnPLqdngASC5bnD9x%2FLioM9RSRw8A9FZl%2FTkFlA3l440Gs3Ye5wt9PcdioaPw7majmMQ%2BlDIzc8R2FDwM0Lyt5ZrlXnLD38WfTDnuo69BjqkAeudhrEhdj88xY4eIGQ0Ejrl00htyAF4%2FA6kuf7p7QCJ5pS6e%2BRM%2B%2B70Jqin0fW5hCUg8IRVppeh2bfnyDZZBWGukfpG6Shy41OVHeMWcupgBzn1Ov0Ze8K1TuE2gLJLlCKHWUEgVe2nOMpaJ3eGB3vEGeV4H24DYOb2qo7s%2BwhpwA18t8hW3jcN%2Bx5%2Fb0r3bbEytfjuO9tzDkWvd7sm%2Fl4RaUSb&X-Amz-Signature=f5a6c8b1d55f44647cac7c84200b72a691f2f597e3cc68bcca98e0d73ee5d913&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UEIUTW4N%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182015Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQCic2Fkt9SvVT%2B61RsTVhZijMXxYRbo7aPfTY0oVcT1VAIhAPQtW7okQurXDqFFCZco9vBS5Ojs4g%2F%2BA%2BEFdq6om2O%2FKv8DCEoQABoMNjM3NDIzMTgzODA1IgzaYOoTJs6bxGGFzdoq3AOxePKvNamD0%2BmGCm4sgDdkMjLFx3sfKz4Nb6xo1CnCBjiKQYU8dbIC4DJZZbn0bamLl%2FoRqBpLkIGTk0ElDYAVvZoVPvILXIQ705XQBow5evTlLO5h%2F%2BFA%2FeyoyszpxBptVBHsuc5vm9Eghq0OHA%2BbzQF63ocaReuNMy1HnN5PCiqWe1NB06UCWm03vF9muBDRsvyDe8O7d96QV7g10fH17gXp0gfRUlL9HXL%2BQXE%2B3l2xTQ6RVU2G2KTRIrHFBT2g5fIAAcx60owBL4WKiQDBHyo9Rys5niAXFBFFcyVMqMCFppBitTdnHbThnAFQuUbpymY7dU4JLfNz6%2BKg%2BEJKx8YxOGh8r6quFe%2FDvONmo%2Fa8lQYPSFBusl9jYZaispRxyo95yUQG4ivxrqKRoVvF9P5cyl3oHKkHHn%2FLOna4uhs03hpHp%2BbWkYZfdMW0ue%2BDebAS%2Fjaj95GoYM8qIqDzJ8rWXHnYB6l5tMnz7MN%2FRxsGKSarfz9mzGQ%2B7ldsd2L5wF5L33cNbTAAETBlTKvsda31%2BnPLqdngASC5bnD9x%2FLioM9RSRw8A9FZl%2FTkFlA3l440Gs3Ye5wt9PcdioaPw7majmMQ%2BlDIzc8R2FDwM0Lyt5ZrlXnLD38WfTDnuo69BjqkAeudhrEhdj88xY4eIGQ0Ejrl00htyAF4%2FA6kuf7p7QCJ5pS6e%2BRM%2B%2B70Jqin0fW5hCUg8IRVppeh2bfnyDZZBWGukfpG6Shy41OVHeMWcupgBzn1Ov0Ze8K1TuE2gLJLlCKHWUEgVe2nOMpaJ3eGB3vEGeV4H24DYOb2qo7s%2BwhpwA18t8hW3jcN%2Bx5%2Fb0r3bbEytfjuO9tzDkWvd7sm%2Fl4RaUSb&X-Amz-Signature=c8ad756f18efd69144af3c1240b3c92a83b993774d6724e8672d88ef04d23b09&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UV2XE7YV%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182016Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIHdv9Z%2FeWkn5b%2B4uPmitij823yx6p%2F4YEXc%2FLdacpCdLAiEAs0LNw8UKmRLMxmAtdnLjGuHM3MpY%2FYNeGmVNW4nm%2Bfgq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDIKLyJWt1nLothHsCircA3efcbkW3p7%2BQzaIn9BLSOXS%2BWFBp%2Fe%2BKJgh0jYGyGQPZeT2NeX%2B9NX0l2943xZrnGJ0zLVKVkrN62tJ9SBLOfq%2FxlJHfG%2BOli5zYk%2FlMoDP5a9qaOXgcpVjasG5j6hWWELynMXE%2B%2B%2Bmh4AeKNOFj%2BtLbYgDKkcH3QQ9z2OlMUh%2B%2B53ab45WGTe0md1MG7nA4StwnnFDn8V6nLzyX7WNLY05FP7%2Bz%2B9Ap1%2B2daK2VrgGDV0xcO65Lsl%2FqiFuwTbk7H17KIbMZS9pa%2Bf1SXlbU94IZuzMC9ZonksBAQCOCOI2330Y%2FZCrrL9iDFFR%2FLNAxfbNoz0kfinFn2RUTmvGZxOfxvWzTyu7mTmiOUfmuh7TmoIBZsXSLbBdKO%2FrWWkSjXGYZOy6eZaeg%2BUuMUo4t%2BnZnR08ZdojTcFeL2%2BppP%2FTENo8WZiR5%2FI%2FmY7mRLKYhfMkwaOYs2Fldz6mqZlwhGofvz5PRv%2FpE%2FQRUjjuvXlcNaEL%2FFMs93F8wweozEX3bsGz842HUtmsApJPtgOS7PNyU4btiM5x%2Bkkb5AfBKd0QNYAUmWFb8EERFoxHGWAq%2Fzv0eDHFG94rTcsS5vGgRuMLYI8Fx0UhiZAGDLUUtTk6F%2FhHYMQYlp7jiWnpMPK6jr0GOqUBG16xQ9ujTEuPPxgi%2BY7e3f5deIGGe9XXOA%2FUNXowyWzYN6mgcAnSPjGkFm4YO48%2Flufl5otTl3pqE%2BxVbWVcz3kX8JDDcMfzksmmW%2B2jihGhYKZE7PH6BP5B19RPG%2F4v7%2FtXmhcwsSzObW92CqlptWIbzESUKao%2Bt6Gfmg7RdaFf1M%2Bs%2BE%2F%2F5%2FcBZwBAqcUUPm5BBYlsrgwMd2FeN%2FKVifPO4v0k&X-Amz-Signature=2f897072f80a862ea281f213438fbfe9b565ca82e474a67d3519961f9a9e3293&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TW3WQMKX%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182016Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIDLJmaW%2Fddxva0e46dUNTz5MZXl9qCJ%2B9w1rBARhaQxdAiEAtHojGpjJQByVgLUMFIBiYZ8%2FpIBQuJT39Qv1VXzPdiMq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDNn2bLPKZO2cwOXccSrcAzqd8LX9pMicJG3S07lXn3sVRphH%2FXg95U4BJwTQsD8EH1Zx8o6TGV%2FmFjWpCmnL8UBoTCN7iTSrNYg1tg%2Fa75IJiNJ%2FciHKGuzstd06D9M4eHO2Voj0CszZ3QzMSSC7dT3EBp%2B3IFSvsRkei07gkwCJ02OKI34PABPaMMZQdp6wL65dZonwhaSyQm%2FjbLDtSMMVnGISmtXE89ESTqoyb68VaPYl9aGeJYQsqNaw6bZcBHyQq2uo7jtD3NNZLDkjNo0mWt%2BofrXa4tXt%2Bp57bFK%2FkhJcnPK4JrpFtBf12vQ2xwAmxMfayJff%2BNp9OAdgallePFHuxwXdiKtBcE%2F%2BNMtClsMB4B9gEsvG7oLXnP89oTTPpquOfbc7KH1P151fPtQu%2FJkCzsgR4XuPJA0qgupxkF1U0UwYfPmtE6CY7gEXfbv4i1QmSXZyjHdwRbVZ1dgyzXsTwGjvidTMnRbeo8E0LtKb%2BAf345yZqVY5mwnWkKCoeVi%2FNsJ0K6vIr%2FRDNZOISzuPV4amZbScQYpEpiSK8qUL8%2Bj3Yk%2F8zBEavyuve%2B2IjrVwESoXNPBw9J9ghzPLalMETHbH%2FIKXWwaZC1gmvYPDJ0YSP93TlctN9CEJiwC03ZWGCAjie%2BdeMPK6jr0GOqUBvPRkjWgPmY4LhLJ0CCww%2BhjAT93D9YPIX08U4cYZkkF3J7ALjv0WiXLctcyC6lUf8HMS9ZrqumuXgwUkPdNVi4ueAI7TygzU8znornkgPXsxb4QNDwcz700fHMGD6u4jeIdeKPooNHV2bLNobVREof3zjIW%2FGvmOArs3gLAqmjA99bp%2BZgvSQPQTJA%2FYTIIOqjghYPOcNnjkjJX3FjdfHjleVHf%2B&X-Amz-Signature=a4266dbb2e3b14b73c200f230f14c0a3a0071a6701e4d3f597738f3f9e201dd2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UEIUTW4N%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182015Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQCic2Fkt9SvVT%2B61RsTVhZijMXxYRbo7aPfTY0oVcT1VAIhAPQtW7okQurXDqFFCZco9vBS5Ojs4g%2F%2BA%2BEFdq6om2O%2FKv8DCEoQABoMNjM3NDIzMTgzODA1IgzaYOoTJs6bxGGFzdoq3AOxePKvNamD0%2BmGCm4sgDdkMjLFx3sfKz4Nb6xo1CnCBjiKQYU8dbIC4DJZZbn0bamLl%2FoRqBpLkIGTk0ElDYAVvZoVPvILXIQ705XQBow5evTlLO5h%2F%2BFA%2FeyoyszpxBptVBHsuc5vm9Eghq0OHA%2BbzQF63ocaReuNMy1HnN5PCiqWe1NB06UCWm03vF9muBDRsvyDe8O7d96QV7g10fH17gXp0gfRUlL9HXL%2BQXE%2B3l2xTQ6RVU2G2KTRIrHFBT2g5fIAAcx60owBL4WKiQDBHyo9Rys5niAXFBFFcyVMqMCFppBitTdnHbThnAFQuUbpymY7dU4JLfNz6%2BKg%2BEJKx8YxOGh8r6quFe%2FDvONmo%2Fa8lQYPSFBusl9jYZaispRxyo95yUQG4ivxrqKRoVvF9P5cyl3oHKkHHn%2FLOna4uhs03hpHp%2BbWkYZfdMW0ue%2BDebAS%2Fjaj95GoYM8qIqDzJ8rWXHnYB6l5tMnz7MN%2FRxsGKSarfz9mzGQ%2B7ldsd2L5wF5L33cNbTAAETBlTKvsda31%2BnPLqdngASC5bnD9x%2FLioM9RSRw8A9FZl%2FTkFlA3l440Gs3Ye5wt9PcdioaPw7majmMQ%2BlDIzc8R2FDwM0Lyt5ZrlXnLD38WfTDnuo69BjqkAeudhrEhdj88xY4eIGQ0Ejrl00htyAF4%2FA6kuf7p7QCJ5pS6e%2BRM%2B%2B70Jqin0fW5hCUg8IRVppeh2bfnyDZZBWGukfpG6Shy41OVHeMWcupgBzn1Ov0Ze8K1TuE2gLJLlCKHWUEgVe2nOMpaJ3eGB3vEGeV4H24DYOb2qo7s%2BwhpwA18t8hW3jcN%2Bx5%2Fb0r3bbEytfjuO9tzDkWvd7sm%2Fl4RaUSb&X-Amz-Signature=06b80b820b690a1d93442fbca000ae1d16717853a10d3b8b99cfa0ab552b5d00&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UEIUTW4N%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182015Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQCic2Fkt9SvVT%2B61RsTVhZijMXxYRbo7aPfTY0oVcT1VAIhAPQtW7okQurXDqFFCZco9vBS5Ojs4g%2F%2BA%2BEFdq6om2O%2FKv8DCEoQABoMNjM3NDIzMTgzODA1IgzaYOoTJs6bxGGFzdoq3AOxePKvNamD0%2BmGCm4sgDdkMjLFx3sfKz4Nb6xo1CnCBjiKQYU8dbIC4DJZZbn0bamLl%2FoRqBpLkIGTk0ElDYAVvZoVPvILXIQ705XQBow5evTlLO5h%2F%2BFA%2FeyoyszpxBptVBHsuc5vm9Eghq0OHA%2BbzQF63ocaReuNMy1HnN5PCiqWe1NB06UCWm03vF9muBDRsvyDe8O7d96QV7g10fH17gXp0gfRUlL9HXL%2BQXE%2B3l2xTQ6RVU2G2KTRIrHFBT2g5fIAAcx60owBL4WKiQDBHyo9Rys5niAXFBFFcyVMqMCFppBitTdnHbThnAFQuUbpymY7dU4JLfNz6%2BKg%2BEJKx8YxOGh8r6quFe%2FDvONmo%2Fa8lQYPSFBusl9jYZaispRxyo95yUQG4ivxrqKRoVvF9P5cyl3oHKkHHn%2FLOna4uhs03hpHp%2BbWkYZfdMW0ue%2BDebAS%2Fjaj95GoYM8qIqDzJ8rWXHnYB6l5tMnz7MN%2FRxsGKSarfz9mzGQ%2B7ldsd2L5wF5L33cNbTAAETBlTKvsda31%2BnPLqdngASC5bnD9x%2FLioM9RSRw8A9FZl%2FTkFlA3l440Gs3Ye5wt9PcdioaPw7majmMQ%2BlDIzc8R2FDwM0Lyt5ZrlXnLD38WfTDnuo69BjqkAeudhrEhdj88xY4eIGQ0Ejrl00htyAF4%2FA6kuf7p7QCJ5pS6e%2BRM%2B%2B70Jqin0fW5hCUg8IRVppeh2bfnyDZZBWGukfpG6Shy41OVHeMWcupgBzn1Ov0Ze8K1TuE2gLJLlCKHWUEgVe2nOMpaJ3eGB3vEGeV4H24DYOb2qo7s%2BwhpwA18t8hW3jcN%2Bx5%2Fb0r3bbEytfjuO9tzDkWvd7sm%2Fl4RaUSb&X-Amz-Signature=71182be6c58be75f474a0e966f8eae53e289757bd7a521b838d3c85d643d0107&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UEIUTW4N%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182015Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQCic2Fkt9SvVT%2B61RsTVhZijMXxYRbo7aPfTY0oVcT1VAIhAPQtW7okQurXDqFFCZco9vBS5Ojs4g%2F%2BA%2BEFdq6om2O%2FKv8DCEoQABoMNjM3NDIzMTgzODA1IgzaYOoTJs6bxGGFzdoq3AOxePKvNamD0%2BmGCm4sgDdkMjLFx3sfKz4Nb6xo1CnCBjiKQYU8dbIC4DJZZbn0bamLl%2FoRqBpLkIGTk0ElDYAVvZoVPvILXIQ705XQBow5evTlLO5h%2F%2BFA%2FeyoyszpxBptVBHsuc5vm9Eghq0OHA%2BbzQF63ocaReuNMy1HnN5PCiqWe1NB06UCWm03vF9muBDRsvyDe8O7d96QV7g10fH17gXp0gfRUlL9HXL%2BQXE%2B3l2xTQ6RVU2G2KTRIrHFBT2g5fIAAcx60owBL4WKiQDBHyo9Rys5niAXFBFFcyVMqMCFppBitTdnHbThnAFQuUbpymY7dU4JLfNz6%2BKg%2BEJKx8YxOGh8r6quFe%2FDvONmo%2Fa8lQYPSFBusl9jYZaispRxyo95yUQG4ivxrqKRoVvF9P5cyl3oHKkHHn%2FLOna4uhs03hpHp%2BbWkYZfdMW0ue%2BDebAS%2Fjaj95GoYM8qIqDzJ8rWXHnYB6l5tMnz7MN%2FRxsGKSarfz9mzGQ%2B7ldsd2L5wF5L33cNbTAAETBlTKvsda31%2BnPLqdngASC5bnD9x%2FLioM9RSRw8A9FZl%2FTkFlA3l440Gs3Ye5wt9PcdioaPw7majmMQ%2BlDIzc8R2FDwM0Lyt5ZrlXnLD38WfTDnuo69BjqkAeudhrEhdj88xY4eIGQ0Ejrl00htyAF4%2FA6kuf7p7QCJ5pS6e%2BRM%2B%2B70Jqin0fW5hCUg8IRVppeh2bfnyDZZBWGukfpG6Shy41OVHeMWcupgBzn1Ov0Ze8K1TuE2gLJLlCKHWUEgVe2nOMpaJ3eGB3vEGeV4H24DYOb2qo7s%2BwhpwA18t8hW3jcN%2Bx5%2Fb0r3bbEytfjuO9tzDkWvd7sm%2Fl4RaUSb&X-Amz-Signature=24587fb66fc88651a4d5b8cb3c0ac75391b56bcb380e193eda2dd9df896683b2&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UEIUTW4N%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182015Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQCic2Fkt9SvVT%2B61RsTVhZijMXxYRbo7aPfTY0oVcT1VAIhAPQtW7okQurXDqFFCZco9vBS5Ojs4g%2F%2BA%2BEFdq6om2O%2FKv8DCEoQABoMNjM3NDIzMTgzODA1IgzaYOoTJs6bxGGFzdoq3AOxePKvNamD0%2BmGCm4sgDdkMjLFx3sfKz4Nb6xo1CnCBjiKQYU8dbIC4DJZZbn0bamLl%2FoRqBpLkIGTk0ElDYAVvZoVPvILXIQ705XQBow5evTlLO5h%2F%2BFA%2FeyoyszpxBptVBHsuc5vm9Eghq0OHA%2BbzQF63ocaReuNMy1HnN5PCiqWe1NB06UCWm03vF9muBDRsvyDe8O7d96QV7g10fH17gXp0gfRUlL9HXL%2BQXE%2B3l2xTQ6RVU2G2KTRIrHFBT2g5fIAAcx60owBL4WKiQDBHyo9Rys5niAXFBFFcyVMqMCFppBitTdnHbThnAFQuUbpymY7dU4JLfNz6%2BKg%2BEJKx8YxOGh8r6quFe%2FDvONmo%2Fa8lQYPSFBusl9jYZaispRxyo95yUQG4ivxrqKRoVvF9P5cyl3oHKkHHn%2FLOna4uhs03hpHp%2BbWkYZfdMW0ue%2BDebAS%2Fjaj95GoYM8qIqDzJ8rWXHnYB6l5tMnz7MN%2FRxsGKSarfz9mzGQ%2B7ldsd2L5wF5L33cNbTAAETBlTKvsda31%2BnPLqdngASC5bnD9x%2FLioM9RSRw8A9FZl%2FTkFlA3l440Gs3Ye5wt9PcdioaPw7majmMQ%2BlDIzc8R2FDwM0Lyt5ZrlXnLD38WfTDnuo69BjqkAeudhrEhdj88xY4eIGQ0Ejrl00htyAF4%2FA6kuf7p7QCJ5pS6e%2BRM%2B%2B70Jqin0fW5hCUg8IRVppeh2bfnyDZZBWGukfpG6Shy41OVHeMWcupgBzn1Ov0Ze8K1TuE2gLJLlCKHWUEgVe2nOMpaJ3eGB3vEGeV4H24DYOb2qo7s%2BwhpwA18t8hW3jcN%2Bx5%2Fb0r3bbEytfjuO9tzDkWvd7sm%2Fl4RaUSb&X-Amz-Signature=80ce39c39b05f2d27edd4b3276fc14682a43e5f9e18213c7dba18e17325be17b&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
