

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663A24IWDD%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCcuds67q767fhJyZO2gYBL8lksJpMszNWTuffMzSsiHgIhAMHceu05d3ck9FgFmCJFPhl78Hk1kSPBkLTRrx4ZNLHFKv8DCDkQABoMNjM3NDIzMTgzODA1Igwjbjtkom57FKExzXoq3AMZMBvJOXZZppCfWtX%2BkD45NWi7L7NrnuqN%2BcNXL54Cqjnhc22jO6F23Ruw%2BvBaZDcpZR64%2B4XHuTE%2BeF6fbpgV%2FyufUEoaBoSIgdfBnS3oZuc9c9kJHEf1F55O%2FOjQcPnoJSjY8SXOQufwfmfcWFucpnw6lLt%2BcgiO23d6LnTc0AlIPAOuHC13WA3TUbBq09X6BBA1oKTputxLtL2QXrt1qpPwf1aU9oajFA5%2F0AG8lFz544rWR1Lpb%2BITS%2FUjMK2Zwf90k%2BoxkhW%2FIXBdvM993CFOWeV6GQxdo2fvCEClZ6VFJLi0MfG4PPGHheeuZkl%2F9A17ClL8%2Bm4wS1vi4OLAjxvYlQ3NQ8wuu3KUViZMASHnwq4Ha%2BCNvtqXLOLlpP8toFF4Uc7ZJ9GHcSjmElb0c8yjdfsQsf7orBlTjJ925NwyXD1dHDuTfK8W9qwrHuJJcuIFoaOerhKO%2B3Juhqi9Fb0FwCFkbfVVJWZMiTZMHZMJfvoIwsZzr6rExzunRC%2F%2FYC4jWytsOKVMihxaOi%2Fl05%2FWn%2BOBAXFVeCeniHMYuGOMR7h8fMDktfcpWVY%2FEHeSHWFydxeUa8ErBUNZNUv49fgKqGSOlkk%2Bgr7ZIxxflktdSQAR2otjkT%2FhPTD8zIq9BjqkAW5flUak8mfCjDj9BnWOCRH6j5xUo67OG28oCZfqzUB%2B4%2F5gf%2FcLUKhzTC3YfWADSZ6H9XXDYXDaeanw63VD84DH%2B1kjqwHIIxRXwiviP9APbvSmdlWEm%2F8BBmACp4QyGnRpRIrHWekuBD9qWftz9abENL6%2FgOzRiRIIjmgAqN%2BKRs8gKnxhGIqSHaA3%2BTGZfFUAoMjSbIyNZBPZSASLcVbjBhGU&X-Amz-Signature=3d509d8de2416e8b8319fd0c89c2b7ef367aff2d50839524c0afbe303a0f80b2&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663A24IWDD%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCcuds67q767fhJyZO2gYBL8lksJpMszNWTuffMzSsiHgIhAMHceu05d3ck9FgFmCJFPhl78Hk1kSPBkLTRrx4ZNLHFKv8DCDkQABoMNjM3NDIzMTgzODA1Igwjbjtkom57FKExzXoq3AMZMBvJOXZZppCfWtX%2BkD45NWi7L7NrnuqN%2BcNXL54Cqjnhc22jO6F23Ruw%2BvBaZDcpZR64%2B4XHuTE%2BeF6fbpgV%2FyufUEoaBoSIgdfBnS3oZuc9c9kJHEf1F55O%2FOjQcPnoJSjY8SXOQufwfmfcWFucpnw6lLt%2BcgiO23d6LnTc0AlIPAOuHC13WA3TUbBq09X6BBA1oKTputxLtL2QXrt1qpPwf1aU9oajFA5%2F0AG8lFz544rWR1Lpb%2BITS%2FUjMK2Zwf90k%2BoxkhW%2FIXBdvM993CFOWeV6GQxdo2fvCEClZ6VFJLi0MfG4PPGHheeuZkl%2F9A17ClL8%2Bm4wS1vi4OLAjxvYlQ3NQ8wuu3KUViZMASHnwq4Ha%2BCNvtqXLOLlpP8toFF4Uc7ZJ9GHcSjmElb0c8yjdfsQsf7orBlTjJ925NwyXD1dHDuTfK8W9qwrHuJJcuIFoaOerhKO%2B3Juhqi9Fb0FwCFkbfVVJWZMiTZMHZMJfvoIwsZzr6rExzunRC%2F%2FYC4jWytsOKVMihxaOi%2Fl05%2FWn%2BOBAXFVeCeniHMYuGOMR7h8fMDktfcpWVY%2FEHeSHWFydxeUa8ErBUNZNUv49fgKqGSOlkk%2Bgr7ZIxxflktdSQAR2otjkT%2FhPTD8zIq9BjqkAW5flUak8mfCjDj9BnWOCRH6j5xUo67OG28oCZfqzUB%2B4%2F5gf%2FcLUKhzTC3YfWADSZ6H9XXDYXDaeanw63VD84DH%2B1kjqwHIIxRXwiviP9APbvSmdlWEm%2F8BBmACp4QyGnRpRIrHWekuBD9qWftz9abENL6%2FgOzRiRIIjmgAqN%2BKRs8gKnxhGIqSHaA3%2BTGZfFUAoMjSbIyNZBPZSASLcVbjBhGU&X-Amz-Signature=00285185d4e37854a1d9785aa6b5280e34adf594a0365ffa3b04aca88d7867e3&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663A24IWDD%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCcuds67q767fhJyZO2gYBL8lksJpMszNWTuffMzSsiHgIhAMHceu05d3ck9FgFmCJFPhl78Hk1kSPBkLTRrx4ZNLHFKv8DCDkQABoMNjM3NDIzMTgzODA1Igwjbjtkom57FKExzXoq3AMZMBvJOXZZppCfWtX%2BkD45NWi7L7NrnuqN%2BcNXL54Cqjnhc22jO6F23Ruw%2BvBaZDcpZR64%2B4XHuTE%2BeF6fbpgV%2FyufUEoaBoSIgdfBnS3oZuc9c9kJHEf1F55O%2FOjQcPnoJSjY8SXOQufwfmfcWFucpnw6lLt%2BcgiO23d6LnTc0AlIPAOuHC13WA3TUbBq09X6BBA1oKTputxLtL2QXrt1qpPwf1aU9oajFA5%2F0AG8lFz544rWR1Lpb%2BITS%2FUjMK2Zwf90k%2BoxkhW%2FIXBdvM993CFOWeV6GQxdo2fvCEClZ6VFJLi0MfG4PPGHheeuZkl%2F9A17ClL8%2Bm4wS1vi4OLAjxvYlQ3NQ8wuu3KUViZMASHnwq4Ha%2BCNvtqXLOLlpP8toFF4Uc7ZJ9GHcSjmElb0c8yjdfsQsf7orBlTjJ925NwyXD1dHDuTfK8W9qwrHuJJcuIFoaOerhKO%2B3Juhqi9Fb0FwCFkbfVVJWZMiTZMHZMJfvoIwsZzr6rExzunRC%2F%2FYC4jWytsOKVMihxaOi%2Fl05%2FWn%2BOBAXFVeCeniHMYuGOMR7h8fMDktfcpWVY%2FEHeSHWFydxeUa8ErBUNZNUv49fgKqGSOlkk%2Bgr7ZIxxflktdSQAR2otjkT%2FhPTD8zIq9BjqkAW5flUak8mfCjDj9BnWOCRH6j5xUo67OG28oCZfqzUB%2B4%2F5gf%2FcLUKhzTC3YfWADSZ6H9XXDYXDaeanw63VD84DH%2B1kjqwHIIxRXwiviP9APbvSmdlWEm%2F8BBmACp4QyGnRpRIrHWekuBD9qWftz9abENL6%2FgOzRiRIIjmgAqN%2BKRs8gKnxhGIqSHaA3%2BTGZfFUAoMjSbIyNZBPZSASLcVbjBhGU&X-Amz-Signature=255a7d249ad1f4829d93f71780e2ecf917c6f4dfde814caeff2bfe2e46579555&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y7XWG4T3%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041753Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCICj0b4NZwrkqIo030X%2B7joLtCSR%2F7ofyX5ywXu0Ip1usAiEAnf4mpkzuKjPGfoasVXzoQeKn4aU6g5XO7HAp1HTQd6Iq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDBYO4cXijZEmDZavpCrcA9lCa%2BYVwVz%2BuDjbAiyXJKkWPqSYOos85BOE%2FidBhp2BWKYH15b47z5JSeRVedLbWvjqJ0TKhsk5VAMEmcldq9GSTzM2ME9yhYix230RB%2ByVYBrDR%2BEWdewkFpqnc0ywUAwd%2BN74Rnw1QXE1uzahW8HlDJd38w1ebWG2aV0KQ9kIFXEP%2B%2BABC9G7Q154r5Z%2BE7FGny%2Fmsj5a2DEV5eK9M1THUZHItjZlX1koFhenwa4qa7JF7%2FDOPa6xa%2Bbv9ncB%2BkO%2BLtTEWzjpW0RnzDnmBpLwU7bVUAgskXnbEJNPFOjGQXbvQ6ScPJ%2BiA8yXHxhkE%2FKJQT2zEb4zU9nyzNZZLbnCbgubZjSdIyCYicRr0h3%2BqDZpS9aDYVH44vSd80GhjuRrapscfSbi%2FfFoIeky79Vas9pwWskXGIrg8bekmc7dIVb8hS%2BNz6RhFSlxrDRklt%2FKRwX6de%2BqyegK0sEezzMm%2BiiV%2BuOvrGDxv5lMTY1xiN%2F7ggX%2BwQzMRR90%2Fh7%2BcVpISTy4J3zwMT1jB8hCXJy%2Bk6Yk%2FbWTbNlagsFUGcKRAQJakMBGPdxmAbn9HMt9AmtU7JE3GvvnVkQggtpvhUFP6Z0pEruP8zDyNdEn77%2FOWWE6KILp6JdXENq0MOXMir0GOqUBUdzNqZumGZQEgmH88nHtTHHe5%2FWsQ%2B3h67uSQZ%2FG6Op8OsGJ5oD9Nob6EVBtJFDLDXdL5XLffJYX%2Bqq%2FT0FFrBt8dXZdLAPLO%2BavfbKH1RaVjSH6pZD6AG3svataIKjAJjXScvDoQVwylIour8psaPHK1Gk%2Fvegx5IIYfmmjPMEN4WZgrsn%2F%2BuGfHPdgM5wEPIIjAJQrBADCBNmDpsy56zUh1DDO&X-Amz-Signature=bccb08ab42e8d68d22e0cb1957b1661b6da0952fcb9447acccf8389ad37e6277&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665OAPBR3Z%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041753Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCICtobceKcLo4O4Yg86%2FhMYtL2LZWo3f45x%2F91bNYFd4EAiEA%2B2N7w71odLBtXvntIgaWkG4IZ2qnk2wfjbClGFyvrhIq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDIm%2FANKwqnhZgT%2Fy1CrcA1sHUvTNYEFOwUU%2F%2Fmo6jTCAfaV%2B5R%2FOrFZjHrFxoclD4vNHeQwk2L3CEWxyegCHqptf5tgBFwCKs1KLZEZ0GbXY6DWPD9gWPfI8Q%2F6M2Z8ro9iWR8CZPxaph53FRX4s3kPaLORaScKxdW46%2BlFsoR5xHJ1YxspyB8EXmHYBi2xYNdADg32NnV856P3F3DtMAEa5JvDaagC5jfCxd1m21QDmYrARBI0r363aVj427obfNfAqcYGfmFp5z5dPWt389auxA4ZFfBIxKq7JziKvVimq1x95%2BpnxftEmcvp4inpAV9Lepq6syEQMdh3g0k82JXbJ9hrRK%2BOr1hs3LLeiTzuuXTAcf8MyVJVgib5wraCXu%2BpP8pqtMUQcMYCvp%2FJII4Zz2JGYDR3gDBbxRG4by0NioFEGkMFqdGhUJfb0G5AyFHLsE1yUuihgcktIE9%2FMpmC2mOb2gSb4PEJENfMNgATFNyHPxdjFc8aJC9c7Hx5JABBdj%2B9AnaTqJ7J1c1Lqg3GFvzBmsspLjacu5tN66lY9GkG2%2F7t3DA0l55TLjOGNzU%2BcEq%2BB2Cq0Mslnq68KKEnrf%2F3ehDWB%2FjdnMJQMdr3PJfUTpidMIFlOBk9J6bgFP7IoqZZGOR3ikvi0MLXNir0GOqUBJbM4Bp51%2Bl441mtbw9sxoGhZVDZZwZtwSC08ne3VSAg03qYGyFQxMcYAs7%2FFw1MwzXpdRLdA2V2qTxt%2B8WKON3dBdDeDfGVAhCeFEconoFvd%2BgpAOGRWzv9nJkcFj1hvaCzs7jR%2B7CA6GnGKpuoUzM%2FeTpMk00%2BZfLtCoWbZ15x87mUUD2BeLSj4EO57ZOwqW2iB8ql4ZUvbpP5Ss%2FVt991RlhMq&X-Amz-Signature=1b991f33a12a7ae5c5071fccf50afe438ede5313cfd4b558cbab00668cce969b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663A24IWDD%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCcuds67q767fhJyZO2gYBL8lksJpMszNWTuffMzSsiHgIhAMHceu05d3ck9FgFmCJFPhl78Hk1kSPBkLTRrx4ZNLHFKv8DCDkQABoMNjM3NDIzMTgzODA1Igwjbjtkom57FKExzXoq3AMZMBvJOXZZppCfWtX%2BkD45NWi7L7NrnuqN%2BcNXL54Cqjnhc22jO6F23Ruw%2BvBaZDcpZR64%2B4XHuTE%2BeF6fbpgV%2FyufUEoaBoSIgdfBnS3oZuc9c9kJHEf1F55O%2FOjQcPnoJSjY8SXOQufwfmfcWFucpnw6lLt%2BcgiO23d6LnTc0AlIPAOuHC13WA3TUbBq09X6BBA1oKTputxLtL2QXrt1qpPwf1aU9oajFA5%2F0AG8lFz544rWR1Lpb%2BITS%2FUjMK2Zwf90k%2BoxkhW%2FIXBdvM993CFOWeV6GQxdo2fvCEClZ6VFJLi0MfG4PPGHheeuZkl%2F9A17ClL8%2Bm4wS1vi4OLAjxvYlQ3NQ8wuu3KUViZMASHnwq4Ha%2BCNvtqXLOLlpP8toFF4Uc7ZJ9GHcSjmElb0c8yjdfsQsf7orBlTjJ925NwyXD1dHDuTfK8W9qwrHuJJcuIFoaOerhKO%2B3Juhqi9Fb0FwCFkbfVVJWZMiTZMHZMJfvoIwsZzr6rExzunRC%2F%2FYC4jWytsOKVMihxaOi%2Fl05%2FWn%2BOBAXFVeCeniHMYuGOMR7h8fMDktfcpWVY%2FEHeSHWFydxeUa8ErBUNZNUv49fgKqGSOlkk%2Bgr7ZIxxflktdSQAR2otjkT%2FhPTD8zIq9BjqkAW5flUak8mfCjDj9BnWOCRH6j5xUo67OG28oCZfqzUB%2B4%2F5gf%2FcLUKhzTC3YfWADSZ6H9XXDYXDaeanw63VD84DH%2B1kjqwHIIxRXwiviP9APbvSmdlWEm%2F8BBmACp4QyGnRpRIrHWekuBD9qWftz9abENL6%2FgOzRiRIIjmgAqN%2BKRs8gKnxhGIqSHaA3%2BTGZfFUAoMjSbIyNZBPZSASLcVbjBhGU&X-Amz-Signature=8c2428be43914ebf80c94d901d69eeaa6c5fd15c9611e6004eb78dde5eb4adfa&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663A24IWDD%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCcuds67q767fhJyZO2gYBL8lksJpMszNWTuffMzSsiHgIhAMHceu05d3ck9FgFmCJFPhl78Hk1kSPBkLTRrx4ZNLHFKv8DCDkQABoMNjM3NDIzMTgzODA1Igwjbjtkom57FKExzXoq3AMZMBvJOXZZppCfWtX%2BkD45NWi7L7NrnuqN%2BcNXL54Cqjnhc22jO6F23Ruw%2BvBaZDcpZR64%2B4XHuTE%2BeF6fbpgV%2FyufUEoaBoSIgdfBnS3oZuc9c9kJHEf1F55O%2FOjQcPnoJSjY8SXOQufwfmfcWFucpnw6lLt%2BcgiO23d6LnTc0AlIPAOuHC13WA3TUbBq09X6BBA1oKTputxLtL2QXrt1qpPwf1aU9oajFA5%2F0AG8lFz544rWR1Lpb%2BITS%2FUjMK2Zwf90k%2BoxkhW%2FIXBdvM993CFOWeV6GQxdo2fvCEClZ6VFJLi0MfG4PPGHheeuZkl%2F9A17ClL8%2Bm4wS1vi4OLAjxvYlQ3NQ8wuu3KUViZMASHnwq4Ha%2BCNvtqXLOLlpP8toFF4Uc7ZJ9GHcSjmElb0c8yjdfsQsf7orBlTjJ925NwyXD1dHDuTfK8W9qwrHuJJcuIFoaOerhKO%2B3Juhqi9Fb0FwCFkbfVVJWZMiTZMHZMJfvoIwsZzr6rExzunRC%2F%2FYC4jWytsOKVMihxaOi%2Fl05%2FWn%2BOBAXFVeCeniHMYuGOMR7h8fMDktfcpWVY%2FEHeSHWFydxeUa8ErBUNZNUv49fgKqGSOlkk%2Bgr7ZIxxflktdSQAR2otjkT%2FhPTD8zIq9BjqkAW5flUak8mfCjDj9BnWOCRH6j5xUo67OG28oCZfqzUB%2B4%2F5gf%2FcLUKhzTC3YfWADSZ6H9XXDYXDaeanw63VD84DH%2B1kjqwHIIxRXwiviP9APbvSmdlWEm%2F8BBmACp4QyGnRpRIrHWekuBD9qWftz9abENL6%2FgOzRiRIIjmgAqN%2BKRs8gKnxhGIqSHaA3%2BTGZfFUAoMjSbIyNZBPZSASLcVbjBhGU&X-Amz-Signature=95ea5b9eb8381a61362c5fd4024c58d88d1d51e574357af5658ec8d0913f590c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663A24IWDD%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCcuds67q767fhJyZO2gYBL8lksJpMszNWTuffMzSsiHgIhAMHceu05d3ck9FgFmCJFPhl78Hk1kSPBkLTRrx4ZNLHFKv8DCDkQABoMNjM3NDIzMTgzODA1Igwjbjtkom57FKExzXoq3AMZMBvJOXZZppCfWtX%2BkD45NWi7L7NrnuqN%2BcNXL54Cqjnhc22jO6F23Ruw%2BvBaZDcpZR64%2B4XHuTE%2BeF6fbpgV%2FyufUEoaBoSIgdfBnS3oZuc9c9kJHEf1F55O%2FOjQcPnoJSjY8SXOQufwfmfcWFucpnw6lLt%2BcgiO23d6LnTc0AlIPAOuHC13WA3TUbBq09X6BBA1oKTputxLtL2QXrt1qpPwf1aU9oajFA5%2F0AG8lFz544rWR1Lpb%2BITS%2FUjMK2Zwf90k%2BoxkhW%2FIXBdvM993CFOWeV6GQxdo2fvCEClZ6VFJLi0MfG4PPGHheeuZkl%2F9A17ClL8%2Bm4wS1vi4OLAjxvYlQ3NQ8wuu3KUViZMASHnwq4Ha%2BCNvtqXLOLlpP8toFF4Uc7ZJ9GHcSjmElb0c8yjdfsQsf7orBlTjJ925NwyXD1dHDuTfK8W9qwrHuJJcuIFoaOerhKO%2B3Juhqi9Fb0FwCFkbfVVJWZMiTZMHZMJfvoIwsZzr6rExzunRC%2F%2FYC4jWytsOKVMihxaOi%2Fl05%2FWn%2BOBAXFVeCeniHMYuGOMR7h8fMDktfcpWVY%2FEHeSHWFydxeUa8ErBUNZNUv49fgKqGSOlkk%2Bgr7ZIxxflktdSQAR2otjkT%2FhPTD8zIq9BjqkAW5flUak8mfCjDj9BnWOCRH6j5xUo67OG28oCZfqzUB%2B4%2F5gf%2FcLUKhzTC3YfWADSZ6H9XXDYXDaeanw63VD84DH%2B1kjqwHIIxRXwiviP9APbvSmdlWEm%2F8BBmACp4QyGnRpRIrHWekuBD9qWftz9abENL6%2FgOzRiRIIjmgAqN%2BKRs8gKnxhGIqSHaA3%2BTGZfFUAoMjSbIyNZBPZSASLcVbjBhGU&X-Amz-Signature=25f541bc548cedd2ffa6424862242bee28fd911d9c8b0aea132bcda3ac5fcb70&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663A24IWDD%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCcuds67q767fhJyZO2gYBL8lksJpMszNWTuffMzSsiHgIhAMHceu05d3ck9FgFmCJFPhl78Hk1kSPBkLTRrx4ZNLHFKv8DCDkQABoMNjM3NDIzMTgzODA1Igwjbjtkom57FKExzXoq3AMZMBvJOXZZppCfWtX%2BkD45NWi7L7NrnuqN%2BcNXL54Cqjnhc22jO6F23Ruw%2BvBaZDcpZR64%2B4XHuTE%2BeF6fbpgV%2FyufUEoaBoSIgdfBnS3oZuc9c9kJHEf1F55O%2FOjQcPnoJSjY8SXOQufwfmfcWFucpnw6lLt%2BcgiO23d6LnTc0AlIPAOuHC13WA3TUbBq09X6BBA1oKTputxLtL2QXrt1qpPwf1aU9oajFA5%2F0AG8lFz544rWR1Lpb%2BITS%2FUjMK2Zwf90k%2BoxkhW%2FIXBdvM993CFOWeV6GQxdo2fvCEClZ6VFJLi0MfG4PPGHheeuZkl%2F9A17ClL8%2Bm4wS1vi4OLAjxvYlQ3NQ8wuu3KUViZMASHnwq4Ha%2BCNvtqXLOLlpP8toFF4Uc7ZJ9GHcSjmElb0c8yjdfsQsf7orBlTjJ925NwyXD1dHDuTfK8W9qwrHuJJcuIFoaOerhKO%2B3Juhqi9Fb0FwCFkbfVVJWZMiTZMHZMJfvoIwsZzr6rExzunRC%2F%2FYC4jWytsOKVMihxaOi%2Fl05%2FWn%2BOBAXFVeCeniHMYuGOMR7h8fMDktfcpWVY%2FEHeSHWFydxeUa8ErBUNZNUv49fgKqGSOlkk%2Bgr7ZIxxflktdSQAR2otjkT%2FhPTD8zIq9BjqkAW5flUak8mfCjDj9BnWOCRH6j5xUo67OG28oCZfqzUB%2B4%2F5gf%2FcLUKhzTC3YfWADSZ6H9XXDYXDaeanw63VD84DH%2B1kjqwHIIxRXwiviP9APbvSmdlWEm%2F8BBmACp4QyGnRpRIrHWekuBD9qWftz9abENL6%2FgOzRiRIIjmgAqN%2BKRs8gKnxhGIqSHaA3%2BTGZfFUAoMjSbIyNZBPZSASLcVbjBhGU&X-Amz-Signature=dfb0fe43711f1b5640d3867b504d3a41b596183e36687880be064cb070523b41&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
