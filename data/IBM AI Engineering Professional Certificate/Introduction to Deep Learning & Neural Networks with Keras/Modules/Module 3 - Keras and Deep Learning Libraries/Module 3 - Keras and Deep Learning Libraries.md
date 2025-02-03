

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466URRUNNGZ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB5CMsseVn7GOcg3KTCtUgaXKz6GfyyL2Tdt%2F8t1AGcXAiEAk22goTmW3KCZahkvSru9XBizPwNtrekmz%2Fta91NYk98qiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDv7664rm%2FyQ0zfoAyrcA%2FOsz2n1deceKjn3DLeKK0zluHvIRr81QwCnlyHQdy2gHpvf7eH4YmJ1EolFmHPT1ou2jsLx%2BIn2akUDTWg%2Bjy%2FJqGxVw6bY69fWbl%2FS3IUD5HoaOrqTlXfWq0FEniGMwPubtUvz89faeG1pVIEtieNI64o7O2cjWSCvDf62r7y%2BmLhliDm2aE5xvEx%2FIqhufv9GiQtVvMujJCRW9lD8noGvfXl3bv8J6HjUbX7L%2BgL1DiW%2Fw5mwQcSqEkBiNzQUUaQ9yf%2FSQG5dFXHQCRlFzJqMdBdeVIYlo8EgbiBHiPmPlE2P0X4uPulFWT8QW%2F4KHqzYGPhsQeSFS2cxPTBdY73k23Yq8r34Q0ZfRK0VkI1fXhn9nQ4PBAw6xktBPostsWG0Ca5x9D7mCs%2FZW8kM4NsDWdoCN3d4mBuulqsfzTvtZ8wqy2dgzPTXQBA67B%2FBUIySo1XLiM8XCULuvR%2B0tr%2FKe2IOhZVQ1WBxd2zBjOW6xzramZVASy646Pykrp6xGvXbCqQY6Zf4y%2F4JBl%2B2QVOwMAgI9kH5VgcqE6geC1vNuYF71ArsWc%2BeZ4T%2FTnNkls2CVbW9xiZZiFOhgq3kDIU8jmdnjze8ehChlxvEjn304oOjkh4F%2BfOugoBaMJHl%2F7wGOqUBuDgs2kCehGyC8q0ZOks2oy55fjcdkhYr3OeqCGEqYJbSeGakqBQRPTR8etBelCtaxDxPvuZDpsdezm6oHf9CohxtLU4%2FMWVapFET34i9TdNK5i5IIbpG9OJyZcJU7p4doE9uURMGK55tHpExb%2FE29NuJgTTz8J71zi2d8B2oORcp6W%2FeRjdf5ozeRzkdqGLDfNom9SPy0s5i75ZablqtwsMc24Wo&X-Amz-Signature=0f23e640ab2a8d4bdb5a86bb5ba6e54d00166669598805e1d85cf7fb1987ac09&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466URRUNNGZ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB5CMsseVn7GOcg3KTCtUgaXKz6GfyyL2Tdt%2F8t1AGcXAiEAk22goTmW3KCZahkvSru9XBizPwNtrekmz%2Fta91NYk98qiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDv7664rm%2FyQ0zfoAyrcA%2FOsz2n1deceKjn3DLeKK0zluHvIRr81QwCnlyHQdy2gHpvf7eH4YmJ1EolFmHPT1ou2jsLx%2BIn2akUDTWg%2Bjy%2FJqGxVw6bY69fWbl%2FS3IUD5HoaOrqTlXfWq0FEniGMwPubtUvz89faeG1pVIEtieNI64o7O2cjWSCvDf62r7y%2BmLhliDm2aE5xvEx%2FIqhufv9GiQtVvMujJCRW9lD8noGvfXl3bv8J6HjUbX7L%2BgL1DiW%2Fw5mwQcSqEkBiNzQUUaQ9yf%2FSQG5dFXHQCRlFzJqMdBdeVIYlo8EgbiBHiPmPlE2P0X4uPulFWT8QW%2F4KHqzYGPhsQeSFS2cxPTBdY73k23Yq8r34Q0ZfRK0VkI1fXhn9nQ4PBAw6xktBPostsWG0Ca5x9D7mCs%2FZW8kM4NsDWdoCN3d4mBuulqsfzTvtZ8wqy2dgzPTXQBA67B%2FBUIySo1XLiM8XCULuvR%2B0tr%2FKe2IOhZVQ1WBxd2zBjOW6xzramZVASy646Pykrp6xGvXbCqQY6Zf4y%2F4JBl%2B2QVOwMAgI9kH5VgcqE6geC1vNuYF71ArsWc%2BeZ4T%2FTnNkls2CVbW9xiZZiFOhgq3kDIU8jmdnjze8ehChlxvEjn304oOjkh4F%2BfOugoBaMJHl%2F7wGOqUBuDgs2kCehGyC8q0ZOks2oy55fjcdkhYr3OeqCGEqYJbSeGakqBQRPTR8etBelCtaxDxPvuZDpsdezm6oHf9CohxtLU4%2FMWVapFET34i9TdNK5i5IIbpG9OJyZcJU7p4doE9uURMGK55tHpExb%2FE29NuJgTTz8J71zi2d8B2oORcp6W%2FeRjdf5ozeRzkdqGLDfNom9SPy0s5i75ZablqtwsMc24Wo&X-Amz-Signature=891e1989aab9fc145e609b3f74c45224608f4c3a233eadb9d4dbee711906ae6e&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466URRUNNGZ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB5CMsseVn7GOcg3KTCtUgaXKz6GfyyL2Tdt%2F8t1AGcXAiEAk22goTmW3KCZahkvSru9XBizPwNtrekmz%2Fta91NYk98qiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDv7664rm%2FyQ0zfoAyrcA%2FOsz2n1deceKjn3DLeKK0zluHvIRr81QwCnlyHQdy2gHpvf7eH4YmJ1EolFmHPT1ou2jsLx%2BIn2akUDTWg%2Bjy%2FJqGxVw6bY69fWbl%2FS3IUD5HoaOrqTlXfWq0FEniGMwPubtUvz89faeG1pVIEtieNI64o7O2cjWSCvDf62r7y%2BmLhliDm2aE5xvEx%2FIqhufv9GiQtVvMujJCRW9lD8noGvfXl3bv8J6HjUbX7L%2BgL1DiW%2Fw5mwQcSqEkBiNzQUUaQ9yf%2FSQG5dFXHQCRlFzJqMdBdeVIYlo8EgbiBHiPmPlE2P0X4uPulFWT8QW%2F4KHqzYGPhsQeSFS2cxPTBdY73k23Yq8r34Q0ZfRK0VkI1fXhn9nQ4PBAw6xktBPostsWG0Ca5x9D7mCs%2FZW8kM4NsDWdoCN3d4mBuulqsfzTvtZ8wqy2dgzPTXQBA67B%2FBUIySo1XLiM8XCULuvR%2B0tr%2FKe2IOhZVQ1WBxd2zBjOW6xzramZVASy646Pykrp6xGvXbCqQY6Zf4y%2F4JBl%2B2QVOwMAgI9kH5VgcqE6geC1vNuYF71ArsWc%2BeZ4T%2FTnNkls2CVbW9xiZZiFOhgq3kDIU8jmdnjze8ehChlxvEjn304oOjkh4F%2BfOugoBaMJHl%2F7wGOqUBuDgs2kCehGyC8q0ZOks2oy55fjcdkhYr3OeqCGEqYJbSeGakqBQRPTR8etBelCtaxDxPvuZDpsdezm6oHf9CohxtLU4%2FMWVapFET34i9TdNK5i5IIbpG9OJyZcJU7p4doE9uURMGK55tHpExb%2FE29NuJgTTz8J71zi2d8B2oORcp6W%2FeRjdf5ozeRzkdqGLDfNom9SPy0s5i75ZablqtwsMc24Wo&X-Amz-Signature=edefff7c2803af1483fdd0a65b093f34421154a57f929321444cc5cbbfab67a6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QXAJPH3J%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCqDjXltfp6ctLKQAirW6izWkr96jCxh7tEkZ4BPpQDOQIhAJ6be5nxisWXPwYCUlDhiFAydPA4%2F3FndiYryWh8ohWrKogECPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy6yHRh57qFVpJdwKwq3AOvOZrq3Ksc1X4vxgNVBH08541EZgfJxiriHuJC2rwcyKD%2FcH4sMbveVEwmOcVIFK8ZynemKJI6tzema9dJ%2BfEpbpfiU1nCuLygDxTOFXEvVW7EO2q43L7vjibGlg6n3UOjyicSmkdX%2BywHtGfkyDq2qoT3uUevoWQAAaaoxEi1F39iJhwjahoIzcJBWaCVZM3MTXC0HuMFA5TnEmo1%2B16BLN1cQdiiJl4fraerJ7Y7Tvj0aiHxIt4T%2B%2F2w7ssu6in%2FyCiGC2aqQf7QWmCzk1p%2FECJ6Sb6HsRwZnDamPKJl08WKwXXmqNGU6yvAsAh1O02W5Pl%2F7x1WSG%2FFWWjbCeKduLFOVhP5PKWqHfa5BnpkIKCp1tYdsW6BrhmXXhY5rzQgC09s3aTFhnpLUaJxiOJIPir4qqlaBgqE5alRHzZMAxnp%2BMDFHEClstovM1CIwP4CTPEJ8ABX27cpTl1aPt%2BxDfgfNzD7FMWBL%2B4EkhszbWZV2j7EIPrlPMf7yZRxJQqwTT02KAxSknav3HLvXKFlJT3vc4NcUz2yJxjCFS5bY0gdREP%2Ft%2FG%2F3KuXLv14gR45shGXP3vKxJCNGzCE4c5eMlW7R259VYfCBAngELpTaKda4k0X40Vk5vLkLTDA5f%2B8BjqkASoniNyfSgw11qhZg4mPQBnNVKu2aPQsTAeqQ70IxzTM7KTccwmdsYMmitGNbafDvhRlTpEk1%2Ba8wQz2%2FFlaF6BIGetAlrbttM1qQ7ecw8HrD%2FA9tjaeOKRiE%2BgQCUbkl5h1G9ql3rCEerZVlnuV5UPAa4X6rkRfM0SPFmQKfX17PTS97QNQywzf11VTFVxujAfHhQ34l%2B0kRF7OjTJDCaXSWgOc&X-Amz-Signature=bd178ba07fdba8d13d5becf50d9bb884fe933e0a2b2c4c10329860345a47e05a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SE6AOMJO%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFnR5%2FqwSmULrBaYnUIh5eMCkHuhqYptHP00jJMIU4kKAiEAho4v3Ggpgw67Q03vcb%2B0kFA1RI8iys%2BPAcT246Pw5pIqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG5nhVr9ZDex1eT0%2BircAxdCmaByg080XHCDqvVnMYXSIFmLSqkWq4doi1yiHG%2BbTZhkpIoB4x4mwB37MYlPq9R7wqIMGrdqulMHcebuAQBywkxc7MTr0t8JnqqUtsz0pY0%2BOEWX%2FNM8IwIerpkFQvQRc5HBj9CENjL500ROfGNuDnflE%2F8U8xAm4e0USozdjpdm%2FiQtLV8K6PGYd71jUu8UOPcbJQ4DoOCE9TAgeu7uSlmt2PrxvvPLsFpqWI6SzFJQvPjKeSEMDA5tl3re4FYD6k6sWxye8TJL%2BMEHpEXkrFYXJ2H1j4FI%2BlWaQWqwHooDwGaXKkbs4wJjRjIpN8tlETyrWMp%2BDKJLFegKsyCOSTaeygmyPhfqvDEZnwgCO2N3q6gDQQ6Emv9E3M6hAEO5Cf8xy0IfI09Ur6wMeBsyXwUK7qisSKOaPpUf1Kyj4ss1JpN70zhhuvzZTLF13gF8%2Fl4snvAUF3m%2BbG1RYCdSxfTxFal1SFoToh4HdG8OtPBFh4jtBtpt8FUThOP2DhNbzKF6Up%2BSDn2OkaGiF%2FEoTmdHlItUGVcnarPj0FXu%2BdERpgu6%2Fp6I9KctWE5b2zTgfIAe1ZBAHcyftM1r5%2FSDFUDMU%2FBluHJWT7CBRMWexfdulQYJBeYPyIteMJz3%2F7wGOqUB8H9DGSPBGnU5HGHdYv6k6HAnArO7o8WUuNrUQAoRYb9Y4hqb1kIab5TyTp4eTi9myhwngabKNJmTkKHD9FJDJ3h0C1Eg5UTbToq4mJzZwl7pSxSvRkWBS5OdKhsKim5tzRN0%2B0RJht1ZOZEZy0yy50T6xv1uDYXfJfXLK%2F5JPUx3npZ1pDy6VGDpr8Uz2N4AMwkxkmXao0u0HDygLXvFD2L88Caj&X-Amz-Signature=89c30267422a0000eb2c89c1918472ff11ab099bb900e52144ab93e2c0313dcb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466URRUNNGZ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB5CMsseVn7GOcg3KTCtUgaXKz6GfyyL2Tdt%2F8t1AGcXAiEAk22goTmW3KCZahkvSru9XBizPwNtrekmz%2Fta91NYk98qiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDv7664rm%2FyQ0zfoAyrcA%2FOsz2n1deceKjn3DLeKK0zluHvIRr81QwCnlyHQdy2gHpvf7eH4YmJ1EolFmHPT1ou2jsLx%2BIn2akUDTWg%2Bjy%2FJqGxVw6bY69fWbl%2FS3IUD5HoaOrqTlXfWq0FEniGMwPubtUvz89faeG1pVIEtieNI64o7O2cjWSCvDf62r7y%2BmLhliDm2aE5xvEx%2FIqhufv9GiQtVvMujJCRW9lD8noGvfXl3bv8J6HjUbX7L%2BgL1DiW%2Fw5mwQcSqEkBiNzQUUaQ9yf%2FSQG5dFXHQCRlFzJqMdBdeVIYlo8EgbiBHiPmPlE2P0X4uPulFWT8QW%2F4KHqzYGPhsQeSFS2cxPTBdY73k23Yq8r34Q0ZfRK0VkI1fXhn9nQ4PBAw6xktBPostsWG0Ca5x9D7mCs%2FZW8kM4NsDWdoCN3d4mBuulqsfzTvtZ8wqy2dgzPTXQBA67B%2FBUIySo1XLiM8XCULuvR%2B0tr%2FKe2IOhZVQ1WBxd2zBjOW6xzramZVASy646Pykrp6xGvXbCqQY6Zf4y%2F4JBl%2B2QVOwMAgI9kH5VgcqE6geC1vNuYF71ArsWc%2BeZ4T%2FTnNkls2CVbW9xiZZiFOhgq3kDIU8jmdnjze8ehChlxvEjn304oOjkh4F%2BfOugoBaMJHl%2F7wGOqUBuDgs2kCehGyC8q0ZOks2oy55fjcdkhYr3OeqCGEqYJbSeGakqBQRPTR8etBelCtaxDxPvuZDpsdezm6oHf9CohxtLU4%2FMWVapFET34i9TdNK5i5IIbpG9OJyZcJU7p4doE9uURMGK55tHpExb%2FE29NuJgTTz8J71zi2d8B2oORcp6W%2FeRjdf5ozeRzkdqGLDfNom9SPy0s5i75ZablqtwsMc24Wo&X-Amz-Signature=cd61dffce9e98ade69d7078f903abdbb30000a2e92adb55ed624be973d4c4349&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466URRUNNGZ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB5CMsseVn7GOcg3KTCtUgaXKz6GfyyL2Tdt%2F8t1AGcXAiEAk22goTmW3KCZahkvSru9XBizPwNtrekmz%2Fta91NYk98qiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDv7664rm%2FyQ0zfoAyrcA%2FOsz2n1deceKjn3DLeKK0zluHvIRr81QwCnlyHQdy2gHpvf7eH4YmJ1EolFmHPT1ou2jsLx%2BIn2akUDTWg%2Bjy%2FJqGxVw6bY69fWbl%2FS3IUD5HoaOrqTlXfWq0FEniGMwPubtUvz89faeG1pVIEtieNI64o7O2cjWSCvDf62r7y%2BmLhliDm2aE5xvEx%2FIqhufv9GiQtVvMujJCRW9lD8noGvfXl3bv8J6HjUbX7L%2BgL1DiW%2Fw5mwQcSqEkBiNzQUUaQ9yf%2FSQG5dFXHQCRlFzJqMdBdeVIYlo8EgbiBHiPmPlE2P0X4uPulFWT8QW%2F4KHqzYGPhsQeSFS2cxPTBdY73k23Yq8r34Q0ZfRK0VkI1fXhn9nQ4PBAw6xktBPostsWG0Ca5x9D7mCs%2FZW8kM4NsDWdoCN3d4mBuulqsfzTvtZ8wqy2dgzPTXQBA67B%2FBUIySo1XLiM8XCULuvR%2B0tr%2FKe2IOhZVQ1WBxd2zBjOW6xzramZVASy646Pykrp6xGvXbCqQY6Zf4y%2F4JBl%2B2QVOwMAgI9kH5VgcqE6geC1vNuYF71ArsWc%2BeZ4T%2FTnNkls2CVbW9xiZZiFOhgq3kDIU8jmdnjze8ehChlxvEjn304oOjkh4F%2BfOugoBaMJHl%2F7wGOqUBuDgs2kCehGyC8q0ZOks2oy55fjcdkhYr3OeqCGEqYJbSeGakqBQRPTR8etBelCtaxDxPvuZDpsdezm6oHf9CohxtLU4%2FMWVapFET34i9TdNK5i5IIbpG9OJyZcJU7p4doE9uURMGK55tHpExb%2FE29NuJgTTz8J71zi2d8B2oORcp6W%2FeRjdf5ozeRzkdqGLDfNom9SPy0s5i75ZablqtwsMc24Wo&X-Amz-Signature=f7de47102bffae1b0294c5377497f0cfe35af9c773921c23f0ece62db8a5ea15&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466URRUNNGZ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB5CMsseVn7GOcg3KTCtUgaXKz6GfyyL2Tdt%2F8t1AGcXAiEAk22goTmW3KCZahkvSru9XBizPwNtrekmz%2Fta91NYk98qiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDv7664rm%2FyQ0zfoAyrcA%2FOsz2n1deceKjn3DLeKK0zluHvIRr81QwCnlyHQdy2gHpvf7eH4YmJ1EolFmHPT1ou2jsLx%2BIn2akUDTWg%2Bjy%2FJqGxVw6bY69fWbl%2FS3IUD5HoaOrqTlXfWq0FEniGMwPubtUvz89faeG1pVIEtieNI64o7O2cjWSCvDf62r7y%2BmLhliDm2aE5xvEx%2FIqhufv9GiQtVvMujJCRW9lD8noGvfXl3bv8J6HjUbX7L%2BgL1DiW%2Fw5mwQcSqEkBiNzQUUaQ9yf%2FSQG5dFXHQCRlFzJqMdBdeVIYlo8EgbiBHiPmPlE2P0X4uPulFWT8QW%2F4KHqzYGPhsQeSFS2cxPTBdY73k23Yq8r34Q0ZfRK0VkI1fXhn9nQ4PBAw6xktBPostsWG0Ca5x9D7mCs%2FZW8kM4NsDWdoCN3d4mBuulqsfzTvtZ8wqy2dgzPTXQBA67B%2FBUIySo1XLiM8XCULuvR%2B0tr%2FKe2IOhZVQ1WBxd2zBjOW6xzramZVASy646Pykrp6xGvXbCqQY6Zf4y%2F4JBl%2B2QVOwMAgI9kH5VgcqE6geC1vNuYF71ArsWc%2BeZ4T%2FTnNkls2CVbW9xiZZiFOhgq3kDIU8jmdnjze8ehChlxvEjn304oOjkh4F%2BfOugoBaMJHl%2F7wGOqUBuDgs2kCehGyC8q0ZOks2oy55fjcdkhYr3OeqCGEqYJbSeGakqBQRPTR8etBelCtaxDxPvuZDpsdezm6oHf9CohxtLU4%2FMWVapFET34i9TdNK5i5IIbpG9OJyZcJU7p4doE9uURMGK55tHpExb%2FE29NuJgTTz8J71zi2d8B2oORcp6W%2FeRjdf5ozeRzkdqGLDfNom9SPy0s5i75ZablqtwsMc24Wo&X-Amz-Signature=04a59548fb76b1a437961a03fe50f3b0162ad9bed279edaeb4a95b98ace85726&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466URRUNNGZ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB5CMsseVn7GOcg3KTCtUgaXKz6GfyyL2Tdt%2F8t1AGcXAiEAk22goTmW3KCZahkvSru9XBizPwNtrekmz%2Fta91NYk98qiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDv7664rm%2FyQ0zfoAyrcA%2FOsz2n1deceKjn3DLeKK0zluHvIRr81QwCnlyHQdy2gHpvf7eH4YmJ1EolFmHPT1ou2jsLx%2BIn2akUDTWg%2Bjy%2FJqGxVw6bY69fWbl%2FS3IUD5HoaOrqTlXfWq0FEniGMwPubtUvz89faeG1pVIEtieNI64o7O2cjWSCvDf62r7y%2BmLhliDm2aE5xvEx%2FIqhufv9GiQtVvMujJCRW9lD8noGvfXl3bv8J6HjUbX7L%2BgL1DiW%2Fw5mwQcSqEkBiNzQUUaQ9yf%2FSQG5dFXHQCRlFzJqMdBdeVIYlo8EgbiBHiPmPlE2P0X4uPulFWT8QW%2F4KHqzYGPhsQeSFS2cxPTBdY73k23Yq8r34Q0ZfRK0VkI1fXhn9nQ4PBAw6xktBPostsWG0Ca5x9D7mCs%2FZW8kM4NsDWdoCN3d4mBuulqsfzTvtZ8wqy2dgzPTXQBA67B%2FBUIySo1XLiM8XCULuvR%2B0tr%2FKe2IOhZVQ1WBxd2zBjOW6xzramZVASy646Pykrp6xGvXbCqQY6Zf4y%2F4JBl%2B2QVOwMAgI9kH5VgcqE6geC1vNuYF71ArsWc%2BeZ4T%2FTnNkls2CVbW9xiZZiFOhgq3kDIU8jmdnjze8ehChlxvEjn304oOjkh4F%2BfOugoBaMJHl%2F7wGOqUBuDgs2kCehGyC8q0ZOks2oy55fjcdkhYr3OeqCGEqYJbSeGakqBQRPTR8etBelCtaxDxPvuZDpsdezm6oHf9CohxtLU4%2FMWVapFET34i9TdNK5i5IIbpG9OJyZcJU7p4doE9uURMGK55tHpExb%2FE29NuJgTTz8J71zi2d8B2oORcp6W%2FeRjdf5ozeRzkdqGLDfNom9SPy0s5i75ZablqtwsMc24Wo&X-Amz-Signature=d960b5322dd5c34768622e78c8417fc1bcadcc0c28875fc14172937880532c08&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
