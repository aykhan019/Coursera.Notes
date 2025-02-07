

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V2RQIXNG%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201607Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIFNSF7rwA%2BCNNRdsuqovSQgRig3mO1tGtu3otg2oT%2FlKAiEAkZSVgd2LoyHY9FTKIFAx9DtHi8sschCUJOTsQP0qxfwq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDN0yCh66YSWl1Z7OnircA36YPA%2FMA1%2FO%2Bfvf1fqhwVgoIhRvsGw2%2BgVrWNBIuvweOj2IF1T4nce0v8ypoooM3agIPrk30RjfTfcUGFi%2F8WNHVoozXmQHPOLJpj2IL6ugSBg2uZ7OyeCK95u8HTaon1WHP1fU5wH9PY5Du%2BQesH97loU9oujd2ww8iA7GQFol8vkrwN0nRNgzNSAQVgD0XcReiHhkELliRIM%2BwGen8fyA0RAyEMEdIzZQalb5OxteAGuA2NzsDEExukUOFWYRcA1BBOBIMr5cQVlzkqKmLuWDGsYlQn%2F3CyHz37nCjzWvWphqa4ungJ%2BPj3uh9p%2B8QJ1PgssGnPxnEsoakyWxxkaQsxNIJ50MDUXw%2B9RksR8b3Y2R6AGxJ4ZhjUntsou42kjNxYqWfloafCmrlKB7hq1hphYV5egIaS3dY%2F2%2F74pZTNbuoqER%2BCouQCjPW%2FPA0qS8kFwB%2BKeVcd2kjgDFKpC1vPn1fX4gipcNcYk8n9YOYq5qQET6EhVSTNChC7%2B1AYIboZOTiSctBzkZdIs0Ehd6U9Toc58W%2Bnn9vjsiIAxBwpCr1a87vio981qbVRfudHA8h2phrTNBVuDD616rTG4vXizretX9Jk6OFAF6a51S31qNgl2bG4fjV5IrMI3Tmb0GOqUB1YJRohUkU9q3eBxU16X1DUaGMb4MSCAre2Jjbxgbqqep9qeLnDVHeayM%2BID66pYFAlJi4Zj2eDp2%2F0uAWKyVVhU98UxurrU0jgN19sQmCO7xIWivfUTPCn0kaFjQOt1jVfBpz25az%2F6rhkmkVUX3khgMmKNxpg4rnMvIteSHIjqPb5oWTOM56mZdfyCh1%2B30eyppR0Jz7S9TX0FfCKKWQ4u2HFV2&X-Amz-Signature=643747879b9314c8e1318069eb4aac0577e8aa6ae1e6a588949fc7b3bafae980&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V2RQIXNG%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201607Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIFNSF7rwA%2BCNNRdsuqovSQgRig3mO1tGtu3otg2oT%2FlKAiEAkZSVgd2LoyHY9FTKIFAx9DtHi8sschCUJOTsQP0qxfwq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDN0yCh66YSWl1Z7OnircA36YPA%2FMA1%2FO%2Bfvf1fqhwVgoIhRvsGw2%2BgVrWNBIuvweOj2IF1T4nce0v8ypoooM3agIPrk30RjfTfcUGFi%2F8WNHVoozXmQHPOLJpj2IL6ugSBg2uZ7OyeCK95u8HTaon1WHP1fU5wH9PY5Du%2BQesH97loU9oujd2ww8iA7GQFol8vkrwN0nRNgzNSAQVgD0XcReiHhkELliRIM%2BwGen8fyA0RAyEMEdIzZQalb5OxteAGuA2NzsDEExukUOFWYRcA1BBOBIMr5cQVlzkqKmLuWDGsYlQn%2F3CyHz37nCjzWvWphqa4ungJ%2BPj3uh9p%2B8QJ1PgssGnPxnEsoakyWxxkaQsxNIJ50MDUXw%2B9RksR8b3Y2R6AGxJ4ZhjUntsou42kjNxYqWfloafCmrlKB7hq1hphYV5egIaS3dY%2F2%2F74pZTNbuoqER%2BCouQCjPW%2FPA0qS8kFwB%2BKeVcd2kjgDFKpC1vPn1fX4gipcNcYk8n9YOYq5qQET6EhVSTNChC7%2B1AYIboZOTiSctBzkZdIs0Ehd6U9Toc58W%2Bnn9vjsiIAxBwpCr1a87vio981qbVRfudHA8h2phrTNBVuDD616rTG4vXizretX9Jk6OFAF6a51S31qNgl2bG4fjV5IrMI3Tmb0GOqUB1YJRohUkU9q3eBxU16X1DUaGMb4MSCAre2Jjbxgbqqep9qeLnDVHeayM%2BID66pYFAlJi4Zj2eDp2%2F0uAWKyVVhU98UxurrU0jgN19sQmCO7xIWivfUTPCn0kaFjQOt1jVfBpz25az%2F6rhkmkVUX3khgMmKNxpg4rnMvIteSHIjqPb5oWTOM56mZdfyCh1%2B30eyppR0Jz7S9TX0FfCKKWQ4u2HFV2&X-Amz-Signature=ef2aeaaa47bbb738f45e50be263b8a09dc833d046b9c0d1fbd13d813bfd72acc&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V2RQIXNG%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201607Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIFNSF7rwA%2BCNNRdsuqovSQgRig3mO1tGtu3otg2oT%2FlKAiEAkZSVgd2LoyHY9FTKIFAx9DtHi8sschCUJOTsQP0qxfwq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDN0yCh66YSWl1Z7OnircA36YPA%2FMA1%2FO%2Bfvf1fqhwVgoIhRvsGw2%2BgVrWNBIuvweOj2IF1T4nce0v8ypoooM3agIPrk30RjfTfcUGFi%2F8WNHVoozXmQHPOLJpj2IL6ugSBg2uZ7OyeCK95u8HTaon1WHP1fU5wH9PY5Du%2BQesH97loU9oujd2ww8iA7GQFol8vkrwN0nRNgzNSAQVgD0XcReiHhkELliRIM%2BwGen8fyA0RAyEMEdIzZQalb5OxteAGuA2NzsDEExukUOFWYRcA1BBOBIMr5cQVlzkqKmLuWDGsYlQn%2F3CyHz37nCjzWvWphqa4ungJ%2BPj3uh9p%2B8QJ1PgssGnPxnEsoakyWxxkaQsxNIJ50MDUXw%2B9RksR8b3Y2R6AGxJ4ZhjUntsou42kjNxYqWfloafCmrlKB7hq1hphYV5egIaS3dY%2F2%2F74pZTNbuoqER%2BCouQCjPW%2FPA0qS8kFwB%2BKeVcd2kjgDFKpC1vPn1fX4gipcNcYk8n9YOYq5qQET6EhVSTNChC7%2B1AYIboZOTiSctBzkZdIs0Ehd6U9Toc58W%2Bnn9vjsiIAxBwpCr1a87vio981qbVRfudHA8h2phrTNBVuDD616rTG4vXizretX9Jk6OFAF6a51S31qNgl2bG4fjV5IrMI3Tmb0GOqUB1YJRohUkU9q3eBxU16X1DUaGMb4MSCAre2Jjbxgbqqep9qeLnDVHeayM%2BID66pYFAlJi4Zj2eDp2%2F0uAWKyVVhU98UxurrU0jgN19sQmCO7xIWivfUTPCn0kaFjQOt1jVfBpz25az%2F6rhkmkVUX3khgMmKNxpg4rnMvIteSHIjqPb5oWTOM56mZdfyCh1%2B30eyppR0Jz7S9TX0FfCKKWQ4u2HFV2&X-Amz-Signature=b913245abaa56916a30b434a99e723dc81d0a34de036a0b317be333e16065a76&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GVAPJ5H%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIQCfGMsXAk6sQdujznhz0djB0IGhtHuqNlnEyGriVoj%2F7gIgTULzK%2FNumCI%2BTL1HMYUKAAdcAH3SM6w3o6TdKDGlSokq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDHOaWmmNAn01fQNXGircA02hz6XaHCeeI7taN%2BA3xObDrWJO4baQlaJecupkB%2Bpm9QXqvXeMuaAIdwmnyQBlJ09aJe2c1JhU6mb0DqTZrThUEsOF3uqAUspm9akvZaKtq%2BmAHpfIlKbudVZ4EzgJJCgQajDQddzWSaFxneIvpB8hIhZQVDkQ9zrf%2FkwHHiscJ4PXmQcm%2FG0w%2Fh4poj9A4c0hR0RPaVqsO4IuZCT7LTH2fkUVtd9vn%2F38NkjVuMQmFaibFhaIxZmkeMBFxyYQ%2BGv5sVMb2NiPQrldn1EaLfePnpURBxpyR98f3NH4gOwiXQpAd8W7h8D36Rc%2FkCEwvhdqSHUUBjb7i6bJ%2FB2ZXnki6E5lwS4ej6dNs2vEVUMQpIhilPgjgWf7Jtjk8BQhX9URKvzd72LvvGVocWgLMlCCH%2BaQQtgtbf2yUsyBVbVDNLaf%2FH%2BEdVaATwp4NVku5u55jFn0CQZQuphoP3IEwQi6H35WJNEK0NpCurzZ8kDJSHVxOm%2F%2BS7SJqxgrWUC%2F3VyB1TWl%2F421XkMCIzoEpOLzH0sOolQS7gvAU%2FertFYGn8u2iPs9EyT9nSKDUv3B%2FIIlJk%2Ft57unBlIE9G%2FnI1DdzNfAwCATj67ZqhNlF70FewBYBJI56ZUVMrATMK7Smb0GOqUB3XTSnKPBARL4NdMnAPGkqh8WiNyTCiSOWBGOInwR6ESQee95SMXOEa3h%2B1oH9SOY31Ekwapa9qT61CPBkBDLjgNWx%2Bd%2BHgxEWb2k2RHcHQcV5bc%2BD%2BI5hIJAzC8JpiYH2UTR8Z7zwPUMyFTbpcA9F%2BnoQ%2FMkzi4Lbz7V7c9r6%2FhD0QKH%2Fr7NO%2Fnsm3odn%2BzPFpzLvMbjPqfLjN0O%2BA13WsJUiMQE&X-Amz-Signature=a57bd99bd8b3a3b7d4db573a22f9ef05943f648bee9135bb3b630fd8214438e1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VEQPRYWB%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJGMEQCIBOZxjDo4raexhjqEDhCcs1FLdNCZkCkA78IuTjagESZAiAErin16lIX5DliKZT%2BJDvcZGBKiUuYeP0hSXVKSnRzvSr%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIMp2UbUEqrw4u1d06CKtwDY42vxandO5x6OSCYVnoyZlUfNyQMmZ7irCVigt8JzWIu2qUOtPrVXhFIcekpTTX6xNQbLFdXv9paFFHoAtngkWVjO1UYjeQKYLuS0KM0uM7fyO6%2FfbVUkOr0I9sOOO4qyILpUeQCoVN9bZF4hwpOc35Be2WD34aBnDFL5hjF5Cstbyx%2Fp3%2Bv33zKSsZZ%2FvZfLwqfrDOHptbej6IxVg7qUeG%2BZyoU5pRUbl0rPHGHNCiu8%2BYsPd1Fqe0gm6tbmc4GUUTeTwvPPQahL6UXVBBl5O5cEtaNFxAguIImNTGw8SwcPi7iG5DoS1meI9RCDy5kaEKx4bFbLJxbFtRU3sK2nWyx1xiPEQxO2%2BfadqebmUcdfvrpdFTY9Kg5lHHD5KG3FpnFDtqIjtYeckxUPCAhyCeS4MJhYgW4hAZ1K8tB3J1PC59xgWnPnePNBQ%2BUuG2sY2OilrW%2B3VTBta1dsigA4waFSv6pg8KbABlM0mWVGN6xDF32csZ2E6wKWOzBH86T0dvUWPe610lKGDhvFt1uiki%2BG6sf16myHl6jjl38NED6p2blN%2FpkundxtYDfHT9Z5kz4bUL3Dq7mD0GQB0c5dAWnCaKhWg0mv8f1X5dAjNmvgCfcaMpc6TlKEHIwwNKZvQY6pgH0anw%2FItuz4xy4YEU%2BQ80CY%2FUWp2kuJbfXTToEV0QPpUD5FJVNNIu6JP7M%2FiDj2PWabPPV7oAK1SURsM6Abua4PM6b8r4iXFPxeckThlipgl193WxKI2E1WHGWk7UN6g8krckT%2F%2BMfNzlhOIGWncB5AFbDKHv7qgUZufcAmoGWJbmZmNIpaBo8wj%2BgerR9yc4G2EsEBiwdQ1V8FHIaVmgD2ctdM2TM&X-Amz-Signature=f64a9949ee068f154d92e21fa17bcf7d951de636b1b029068012ab8eddf3f02d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V2RQIXNG%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201607Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIFNSF7rwA%2BCNNRdsuqovSQgRig3mO1tGtu3otg2oT%2FlKAiEAkZSVgd2LoyHY9FTKIFAx9DtHi8sschCUJOTsQP0qxfwq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDN0yCh66YSWl1Z7OnircA36YPA%2FMA1%2FO%2Bfvf1fqhwVgoIhRvsGw2%2BgVrWNBIuvweOj2IF1T4nce0v8ypoooM3agIPrk30RjfTfcUGFi%2F8WNHVoozXmQHPOLJpj2IL6ugSBg2uZ7OyeCK95u8HTaon1WHP1fU5wH9PY5Du%2BQesH97loU9oujd2ww8iA7GQFol8vkrwN0nRNgzNSAQVgD0XcReiHhkELliRIM%2BwGen8fyA0RAyEMEdIzZQalb5OxteAGuA2NzsDEExukUOFWYRcA1BBOBIMr5cQVlzkqKmLuWDGsYlQn%2F3CyHz37nCjzWvWphqa4ungJ%2BPj3uh9p%2B8QJ1PgssGnPxnEsoakyWxxkaQsxNIJ50MDUXw%2B9RksR8b3Y2R6AGxJ4ZhjUntsou42kjNxYqWfloafCmrlKB7hq1hphYV5egIaS3dY%2F2%2F74pZTNbuoqER%2BCouQCjPW%2FPA0qS8kFwB%2BKeVcd2kjgDFKpC1vPn1fX4gipcNcYk8n9YOYq5qQET6EhVSTNChC7%2B1AYIboZOTiSctBzkZdIs0Ehd6U9Toc58W%2Bnn9vjsiIAxBwpCr1a87vio981qbVRfudHA8h2phrTNBVuDD616rTG4vXizretX9Jk6OFAF6a51S31qNgl2bG4fjV5IrMI3Tmb0GOqUB1YJRohUkU9q3eBxU16X1DUaGMb4MSCAre2Jjbxgbqqep9qeLnDVHeayM%2BID66pYFAlJi4Zj2eDp2%2F0uAWKyVVhU98UxurrU0jgN19sQmCO7xIWivfUTPCn0kaFjQOt1jVfBpz25az%2F6rhkmkVUX3khgMmKNxpg4rnMvIteSHIjqPb5oWTOM56mZdfyCh1%2B30eyppR0Jz7S9TX0FfCKKWQ4u2HFV2&X-Amz-Signature=9535d7a2297bde8199aae31b0040fb87cb6976ab019c4ce1ba5cb00dee030c93&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V2RQIXNG%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201607Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIFNSF7rwA%2BCNNRdsuqovSQgRig3mO1tGtu3otg2oT%2FlKAiEAkZSVgd2LoyHY9FTKIFAx9DtHi8sschCUJOTsQP0qxfwq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDN0yCh66YSWl1Z7OnircA36YPA%2FMA1%2FO%2Bfvf1fqhwVgoIhRvsGw2%2BgVrWNBIuvweOj2IF1T4nce0v8ypoooM3agIPrk30RjfTfcUGFi%2F8WNHVoozXmQHPOLJpj2IL6ugSBg2uZ7OyeCK95u8HTaon1WHP1fU5wH9PY5Du%2BQesH97loU9oujd2ww8iA7GQFol8vkrwN0nRNgzNSAQVgD0XcReiHhkELliRIM%2BwGen8fyA0RAyEMEdIzZQalb5OxteAGuA2NzsDEExukUOFWYRcA1BBOBIMr5cQVlzkqKmLuWDGsYlQn%2F3CyHz37nCjzWvWphqa4ungJ%2BPj3uh9p%2B8QJ1PgssGnPxnEsoakyWxxkaQsxNIJ50MDUXw%2B9RksR8b3Y2R6AGxJ4ZhjUntsou42kjNxYqWfloafCmrlKB7hq1hphYV5egIaS3dY%2F2%2F74pZTNbuoqER%2BCouQCjPW%2FPA0qS8kFwB%2BKeVcd2kjgDFKpC1vPn1fX4gipcNcYk8n9YOYq5qQET6EhVSTNChC7%2B1AYIboZOTiSctBzkZdIs0Ehd6U9Toc58W%2Bnn9vjsiIAxBwpCr1a87vio981qbVRfudHA8h2phrTNBVuDD616rTG4vXizretX9Jk6OFAF6a51S31qNgl2bG4fjV5IrMI3Tmb0GOqUB1YJRohUkU9q3eBxU16X1DUaGMb4MSCAre2Jjbxgbqqep9qeLnDVHeayM%2BID66pYFAlJi4Zj2eDp2%2F0uAWKyVVhU98UxurrU0jgN19sQmCO7xIWivfUTPCn0kaFjQOt1jVfBpz25az%2F6rhkmkVUX3khgMmKNxpg4rnMvIteSHIjqPb5oWTOM56mZdfyCh1%2B30eyppR0Jz7S9TX0FfCKKWQ4u2HFV2&X-Amz-Signature=236cb30cb5aa641f6cb8471355279f00551fb555efdc63b3bc9a646a246cc618&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V2RQIXNG%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201607Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIFNSF7rwA%2BCNNRdsuqovSQgRig3mO1tGtu3otg2oT%2FlKAiEAkZSVgd2LoyHY9FTKIFAx9DtHi8sschCUJOTsQP0qxfwq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDN0yCh66YSWl1Z7OnircA36YPA%2FMA1%2FO%2Bfvf1fqhwVgoIhRvsGw2%2BgVrWNBIuvweOj2IF1T4nce0v8ypoooM3agIPrk30RjfTfcUGFi%2F8WNHVoozXmQHPOLJpj2IL6ugSBg2uZ7OyeCK95u8HTaon1WHP1fU5wH9PY5Du%2BQesH97loU9oujd2ww8iA7GQFol8vkrwN0nRNgzNSAQVgD0XcReiHhkELliRIM%2BwGen8fyA0RAyEMEdIzZQalb5OxteAGuA2NzsDEExukUOFWYRcA1BBOBIMr5cQVlzkqKmLuWDGsYlQn%2F3CyHz37nCjzWvWphqa4ungJ%2BPj3uh9p%2B8QJ1PgssGnPxnEsoakyWxxkaQsxNIJ50MDUXw%2B9RksR8b3Y2R6AGxJ4ZhjUntsou42kjNxYqWfloafCmrlKB7hq1hphYV5egIaS3dY%2F2%2F74pZTNbuoqER%2BCouQCjPW%2FPA0qS8kFwB%2BKeVcd2kjgDFKpC1vPn1fX4gipcNcYk8n9YOYq5qQET6EhVSTNChC7%2B1AYIboZOTiSctBzkZdIs0Ehd6U9Toc58W%2Bnn9vjsiIAxBwpCr1a87vio981qbVRfudHA8h2phrTNBVuDD616rTG4vXizretX9Jk6OFAF6a51S31qNgl2bG4fjV5IrMI3Tmb0GOqUB1YJRohUkU9q3eBxU16X1DUaGMb4MSCAre2Jjbxgbqqep9qeLnDVHeayM%2BID66pYFAlJi4Zj2eDp2%2F0uAWKyVVhU98UxurrU0jgN19sQmCO7xIWivfUTPCn0kaFjQOt1jVfBpz25az%2F6rhkmkVUX3khgMmKNxpg4rnMvIteSHIjqPb5oWTOM56mZdfyCh1%2B30eyppR0Jz7S9TX0FfCKKWQ4u2HFV2&X-Amz-Signature=5a547ad3a10cae0e2f82740b3c5ec7ebfca84d9c4050408361ab57986aefcd97&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V2RQIXNG%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201607Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIFNSF7rwA%2BCNNRdsuqovSQgRig3mO1tGtu3otg2oT%2FlKAiEAkZSVgd2LoyHY9FTKIFAx9DtHi8sschCUJOTsQP0qxfwq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDN0yCh66YSWl1Z7OnircA36YPA%2FMA1%2FO%2Bfvf1fqhwVgoIhRvsGw2%2BgVrWNBIuvweOj2IF1T4nce0v8ypoooM3agIPrk30RjfTfcUGFi%2F8WNHVoozXmQHPOLJpj2IL6ugSBg2uZ7OyeCK95u8HTaon1WHP1fU5wH9PY5Du%2BQesH97loU9oujd2ww8iA7GQFol8vkrwN0nRNgzNSAQVgD0XcReiHhkELliRIM%2BwGen8fyA0RAyEMEdIzZQalb5OxteAGuA2NzsDEExukUOFWYRcA1BBOBIMr5cQVlzkqKmLuWDGsYlQn%2F3CyHz37nCjzWvWphqa4ungJ%2BPj3uh9p%2B8QJ1PgssGnPxnEsoakyWxxkaQsxNIJ50MDUXw%2B9RksR8b3Y2R6AGxJ4ZhjUntsou42kjNxYqWfloafCmrlKB7hq1hphYV5egIaS3dY%2F2%2F74pZTNbuoqER%2BCouQCjPW%2FPA0qS8kFwB%2BKeVcd2kjgDFKpC1vPn1fX4gipcNcYk8n9YOYq5qQET6EhVSTNChC7%2B1AYIboZOTiSctBzkZdIs0Ehd6U9Toc58W%2Bnn9vjsiIAxBwpCr1a87vio981qbVRfudHA8h2phrTNBVuDD616rTG4vXizretX9Jk6OFAF6a51S31qNgl2bG4fjV5IrMI3Tmb0GOqUB1YJRohUkU9q3eBxU16X1DUaGMb4MSCAre2Jjbxgbqqep9qeLnDVHeayM%2BID66pYFAlJi4Zj2eDp2%2F0uAWKyVVhU98UxurrU0jgN19sQmCO7xIWivfUTPCn0kaFjQOt1jVfBpz25az%2F6rhkmkVUX3khgMmKNxpg4rnMvIteSHIjqPb5oWTOM56mZdfyCh1%2B30eyppR0Jz7S9TX0FfCKKWQ4u2HFV2&X-Amz-Signature=768d247bf917d820c310ea99eceb71fd9614f461ba08dbca173aa0417cb75776&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
