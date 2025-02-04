

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WIZGSPDC%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJGMEQCICDisg6kIh3WI1ThWBwg%2Bkp3h0Ibjr%2Fjw0Yoc3T48IODAiAOlPaSCDtaPLnPNKvlfS5C7AAEJ1QWQ%2B%2B2EFkysY8xbSr%2FAwg2EAAaDDYzNzQyMzE4MzgwNSIM2oSYOZcZyVCrII3nKtwDrz9b1d8wokqVzqFylj0uKQ87zozU8Vp2AX8OvBzC6TtszZhL6rB6ImcgeU13QtJ5eJzowwnmE84CsGOPqV0YWlc%2FUuGTYCmmHkwhVcepp6EGDDXu%2BKH69tlXdnpxhDUvbnmwDH8RVHRHq2wiaJ46OnVOYc3qpzVRxgwGgiSk7Ua0j86llwZ38uEnvsbWWa2PYXL%2BhPdqALecpNquEcPC3mZaiCs%2B7AyD9nOOrmeY2Sg07nM8%2BEusET11RwAUh2Jd4IKq5Omelq8YBhU0Avb%2FWylW5G3FTcolgCrUi79241QoP84znuI%2BIMjYrCnhoZjtDPC0CaAMi9He0kUUjKmEdoPMD9zsweL4%2FOVTXv8YXixBWzHSECDv3DcYG%2FmddmKy7nS0tHDFhAJbaZUYuT%2FyrD0DQwLxaGJV6pE3Zd3GhivGMyRsWyAbMYqaeGi9cQhnVsTs6FQZIjiJDf14J3xvoOswLjnFPdVrHtUOYq0rZA1t5nOMSC%2F2X1fNq2vHIWCqGp%2BjW6I8eLQxr0yLOFKWvhupIQNDUC4WS4oC1x4amzZkw0GwcBzVKkvlt%2B2cuw6hdVzr%2FZetOOfAmRe3%2FTpiUY4meQPVALnxb%2BKJqfpSVpDZUKa3Ge%2FT%2FYYiX20wzfyJvQY6pgH9497IOsR74k7Xl8yHG9ShJ2%2BdTbGohFa78f6w0d9a138z5Qyf%2BC4Y1Xn%2FIoHQMV%2Bf5ftaUAaj9zHC4k0JTG0KESR7u61S22BxjwcpSEc6qDRd3FtXdwYxD7FxSdXfVETeujA16d4iU1SjmnZLeSXhcWuuE09CpBUZFGyJAYszqDou5tPJGB%2FpfPtcTswl2k5%2FonhxZSA0FzfYVi6prAB8pj%2BwiniW&X-Amz-Signature=586fe9609f5542443c573a015f0b0f4232811bff06f69f849d442eb23ec25557&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WIZGSPDC%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJGMEQCICDisg6kIh3WI1ThWBwg%2Bkp3h0Ibjr%2Fjw0Yoc3T48IODAiAOlPaSCDtaPLnPNKvlfS5C7AAEJ1QWQ%2B%2B2EFkysY8xbSr%2FAwg2EAAaDDYzNzQyMzE4MzgwNSIM2oSYOZcZyVCrII3nKtwDrz9b1d8wokqVzqFylj0uKQ87zozU8Vp2AX8OvBzC6TtszZhL6rB6ImcgeU13QtJ5eJzowwnmE84CsGOPqV0YWlc%2FUuGTYCmmHkwhVcepp6EGDDXu%2BKH69tlXdnpxhDUvbnmwDH8RVHRHq2wiaJ46OnVOYc3qpzVRxgwGgiSk7Ua0j86llwZ38uEnvsbWWa2PYXL%2BhPdqALecpNquEcPC3mZaiCs%2B7AyD9nOOrmeY2Sg07nM8%2BEusET11RwAUh2Jd4IKq5Omelq8YBhU0Avb%2FWylW5G3FTcolgCrUi79241QoP84znuI%2BIMjYrCnhoZjtDPC0CaAMi9He0kUUjKmEdoPMD9zsweL4%2FOVTXv8YXixBWzHSECDv3DcYG%2FmddmKy7nS0tHDFhAJbaZUYuT%2FyrD0DQwLxaGJV6pE3Zd3GhivGMyRsWyAbMYqaeGi9cQhnVsTs6FQZIjiJDf14J3xvoOswLjnFPdVrHtUOYq0rZA1t5nOMSC%2F2X1fNq2vHIWCqGp%2BjW6I8eLQxr0yLOFKWvhupIQNDUC4WS4oC1x4amzZkw0GwcBzVKkvlt%2B2cuw6hdVzr%2FZetOOfAmRe3%2FTpiUY4meQPVALnxb%2BKJqfpSVpDZUKa3Ge%2FT%2FYYiX20wzfyJvQY6pgH9497IOsR74k7Xl8yHG9ShJ2%2BdTbGohFa78f6w0d9a138z5Qyf%2BC4Y1Xn%2FIoHQMV%2Bf5ftaUAaj9zHC4k0JTG0KESR7u61S22BxjwcpSEc6qDRd3FtXdwYxD7FxSdXfVETeujA16d4iU1SjmnZLeSXhcWuuE09CpBUZFGyJAYszqDou5tPJGB%2FpfPtcTswl2k5%2FonhxZSA0FzfYVi6prAB8pj%2BwiniW&X-Amz-Signature=6c63174c339672fd28b7c1e0f590ae2205b78d8bcabe4f29826dffe289464952&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WIZGSPDC%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJGMEQCICDisg6kIh3WI1ThWBwg%2Bkp3h0Ibjr%2Fjw0Yoc3T48IODAiAOlPaSCDtaPLnPNKvlfS5C7AAEJ1QWQ%2B%2B2EFkysY8xbSr%2FAwg2EAAaDDYzNzQyMzE4MzgwNSIM2oSYOZcZyVCrII3nKtwDrz9b1d8wokqVzqFylj0uKQ87zozU8Vp2AX8OvBzC6TtszZhL6rB6ImcgeU13QtJ5eJzowwnmE84CsGOPqV0YWlc%2FUuGTYCmmHkwhVcepp6EGDDXu%2BKH69tlXdnpxhDUvbnmwDH8RVHRHq2wiaJ46OnVOYc3qpzVRxgwGgiSk7Ua0j86llwZ38uEnvsbWWa2PYXL%2BhPdqALecpNquEcPC3mZaiCs%2B7AyD9nOOrmeY2Sg07nM8%2BEusET11RwAUh2Jd4IKq5Omelq8YBhU0Avb%2FWylW5G3FTcolgCrUi79241QoP84znuI%2BIMjYrCnhoZjtDPC0CaAMi9He0kUUjKmEdoPMD9zsweL4%2FOVTXv8YXixBWzHSECDv3DcYG%2FmddmKy7nS0tHDFhAJbaZUYuT%2FyrD0DQwLxaGJV6pE3Zd3GhivGMyRsWyAbMYqaeGi9cQhnVsTs6FQZIjiJDf14J3xvoOswLjnFPdVrHtUOYq0rZA1t5nOMSC%2F2X1fNq2vHIWCqGp%2BjW6I8eLQxr0yLOFKWvhupIQNDUC4WS4oC1x4amzZkw0GwcBzVKkvlt%2B2cuw6hdVzr%2FZetOOfAmRe3%2FTpiUY4meQPVALnxb%2BKJqfpSVpDZUKa3Ge%2FT%2FYYiX20wzfyJvQY6pgH9497IOsR74k7Xl8yHG9ShJ2%2BdTbGohFa78f6w0d9a138z5Qyf%2BC4Y1Xn%2FIoHQMV%2Bf5ftaUAaj9zHC4k0JTG0KESR7u61S22BxjwcpSEc6qDRd3FtXdwYxD7FxSdXfVETeujA16d4iU1SjmnZLeSXhcWuuE09CpBUZFGyJAYszqDou5tPJGB%2FpfPtcTswl2k5%2FonhxZSA0FzfYVi6prAB8pj%2BwiniW&X-Amz-Signature=c2a2c7677079e7431e3aa4c65a8639454a9cc7a30564f7899e0d421c83d726a7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TV3A2JVX%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJHMEUCIB3pIlbgGlnZVQ1qat8pwzEgDWkrk0sZZmqrRNR75JNVAiEAvq09ZZbP8RzWeRl0sPtCxSugGdGXdBemzvnGL%2Fxiu0Uq%2FwMINhAAGgw2Mzc0MjMxODM4MDUiDF7m9%2FEVwqdjwbrfFSrcA%2BTYNLFlnbPBOVl75bXuAXafZu9qOFTDVTiS2RwIuQsQcoC5aD0UiebhA7q98wvor5xb%2Becyaq6OoOR675p1ku%2BKNOCKrDrYWFZOmMj2CutD317Ii%2BNYKHkY5TDffRvx40c4yOrSwtzNFzAwYr8UmjWVRHLUJWs7ozxYg1%2BdrmMc1Vfu8hNEqjVutENT7PM%2BFv7W6hThL492G17C0uryAmcFv7ezFkMeq4kJfagzTPpQdby1HReVOKCbn%2BbjLSgwQpiu1DiVTVeuUPoeg2Blh%2FhMZhAO%2FADt62C6s200kzr%2BULY90RcOhx8skkbiWANLbgqQkWqiUp0TDY%2Fo3lH7bWwBe8Xz8yGxftnUONLoVBqxpKeyXcNDmQcKWvG5HwyBDjYz%2BkW71XHAQm7hEv6xA6965q4z1lHbKvzVvOjx77feEKvXrNhd%2F%2FHvl8ItRcCWv9osXMx8kBoHPHmGXPzsZRs7MUMW0faaIU2nhEpl28w5n0c8Lqy40ZwkvS%2BctL%2BlJSoJqKrCoCyfYgKKSs4bLEJ9%2FPPGDpJn1EHzbXQEfCrBp05HchhEEPC2lY4mxRR2gmCEAgsFqOw1dwd5aDhv%2BrUfH0Zh%2F2IkDtxM%2B7XfvVoMRmxmweQYV5umRaBfMNP8ib0GOqUBajFX5K%2BoCsAFf7M44TZaGNBTHsTmARycimFcezYLZzAIJ8xE06czYhXX6MTiEJ3gVQQoiTJxFwf%2B6YBuPBuewpr7OzhQegHA9F6uTV8czKwtXcoBEAwpup6zJrp6IQa3Gug4yAzyhXYV%2FPY93Wx93ugbsz%2B%2FWdCBiOYSvmogz46jzAD%2F4nB2MnOzqndH2QkXuK5ZSdntFzK0Q%2B%2B6Xj2VO2FQJl%2BS&X-Amz-Signature=201b54aed07fbef4f4050185276425ea507a8bb2debe46e42c3bc226daf8c51e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663C7QTIOU%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJHMEUCIQD2ZbN%2Bn7Om%2FrEDjhHJqU56qaqrdFFrW%2Bm65qX%2FcMgQnwIgG1sVjfA8zD1uIH5xsugVHsXd3ddC%2FPjRejiyZEsRtJcq%2FwMINhAAGgw2Mzc0MjMxODM4MDUiDJeUmLNY8qrp9eO6lircA7%2BVW7NLP%2BiuF01A72IMMZRCXQqmyG%2F8pXsY7qIHQ5CSMMBQLfxINdYhDEc4LMtUgGtylX7F7hUjtXv88DiRTZCmoBzhmRk67NW3c5J0%2FZT0qcqPAImJ3%2BLJWZcQKfCDt49wy%2BONjiDafEtbYpa1Oav4nc%2Buw%2BtpdNJ5UKploQpZ0964%2BQ0Z%2BTyljMDbUZ8t%2Bo07SDTr6ngm2EGX9DxBNcazo77v7LDHI37lmcenN2wzG%2B7ervLJTQzMPNOrLxB8pDiNJ8CT4EaDir0eAgicMft8P86bxrP7kGo6gGJ5OODBCrmcc0rWQvc2bRhTlexfV0aWcIiGM3orM0NTCtnKgJJkoTzLpPg0k8FOKO2CQEc0k%2FzOJIIqxPRT%2Bkzgxn6nv80aLWTYpSKs3cV7poEBhgsfvwpfKajBliBsDhr%2Bh5CIq%2F8cvwHK8tRJ8Ju2n8GNGqDiMWDDGEHhj2nx4T%2BBYOVAUwvou%2F4UMyA93TlOTVNjTDpvss81AojEXOXqB%2BpduufNq12WvR%2BZa8T7d0Q5bDvtrWWa%2F2iW%2FWWuDt7qzEBobk6m1Cr96XHVCpNkoj73lRo8v6skgHBmUFbJdG0vPICaszSCvPGRQslwEx4k5Ar5kAOkhuav%2FcM1b7n8MPn8ib0GOqUBp%2BK8iWLOTcHZskIIA%2FE5hyT3pS8D0oac%2FsXKIoHuhSPL0JZf07q0xuCd8HpZXMEKXKQzlgjcBNoPfpYmlTz4qKvaSGvCRKk4pP6ln%2F0dd47hRgrw96CR01PDj9WDpzypzETsItm5MFmXaTMS7IcOFtZKvIhbap49XPkCzf0sffJWsCeofQ9m34n%2BSABihN2GnD5Th3EKkhUkFQd%2B3Y9WolfqD4KU&X-Amz-Signature=f4e86336c1024b291afb2141f43907c0e109491ab76941e8b5da9f7015f2a2cb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WIZGSPDC%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJGMEQCICDisg6kIh3WI1ThWBwg%2Bkp3h0Ibjr%2Fjw0Yoc3T48IODAiAOlPaSCDtaPLnPNKvlfS5C7AAEJ1QWQ%2B%2B2EFkysY8xbSr%2FAwg2EAAaDDYzNzQyMzE4MzgwNSIM2oSYOZcZyVCrII3nKtwDrz9b1d8wokqVzqFylj0uKQ87zozU8Vp2AX8OvBzC6TtszZhL6rB6ImcgeU13QtJ5eJzowwnmE84CsGOPqV0YWlc%2FUuGTYCmmHkwhVcepp6EGDDXu%2BKH69tlXdnpxhDUvbnmwDH8RVHRHq2wiaJ46OnVOYc3qpzVRxgwGgiSk7Ua0j86llwZ38uEnvsbWWa2PYXL%2BhPdqALecpNquEcPC3mZaiCs%2B7AyD9nOOrmeY2Sg07nM8%2BEusET11RwAUh2Jd4IKq5Omelq8YBhU0Avb%2FWylW5G3FTcolgCrUi79241QoP84znuI%2BIMjYrCnhoZjtDPC0CaAMi9He0kUUjKmEdoPMD9zsweL4%2FOVTXv8YXixBWzHSECDv3DcYG%2FmddmKy7nS0tHDFhAJbaZUYuT%2FyrD0DQwLxaGJV6pE3Zd3GhivGMyRsWyAbMYqaeGi9cQhnVsTs6FQZIjiJDf14J3xvoOswLjnFPdVrHtUOYq0rZA1t5nOMSC%2F2X1fNq2vHIWCqGp%2BjW6I8eLQxr0yLOFKWvhupIQNDUC4WS4oC1x4amzZkw0GwcBzVKkvlt%2B2cuw6hdVzr%2FZetOOfAmRe3%2FTpiUY4meQPVALnxb%2BKJqfpSVpDZUKa3Ge%2FT%2FYYiX20wzfyJvQY6pgH9497IOsR74k7Xl8yHG9ShJ2%2BdTbGohFa78f6w0d9a138z5Qyf%2BC4Y1Xn%2FIoHQMV%2Bf5ftaUAaj9zHC4k0JTG0KESR7u61S22BxjwcpSEc6qDRd3FtXdwYxD7FxSdXfVETeujA16d4iU1SjmnZLeSXhcWuuE09CpBUZFGyJAYszqDou5tPJGB%2FpfPtcTswl2k5%2FonhxZSA0FzfYVi6prAB8pj%2BwiniW&X-Amz-Signature=c09cdc7c24e04020db9f91a7d44be59f145ed265be4e17103c582d25831b3555&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WIZGSPDC%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJGMEQCICDisg6kIh3WI1ThWBwg%2Bkp3h0Ibjr%2Fjw0Yoc3T48IODAiAOlPaSCDtaPLnPNKvlfS5C7AAEJ1QWQ%2B%2B2EFkysY8xbSr%2FAwg2EAAaDDYzNzQyMzE4MzgwNSIM2oSYOZcZyVCrII3nKtwDrz9b1d8wokqVzqFylj0uKQ87zozU8Vp2AX8OvBzC6TtszZhL6rB6ImcgeU13QtJ5eJzowwnmE84CsGOPqV0YWlc%2FUuGTYCmmHkwhVcepp6EGDDXu%2BKH69tlXdnpxhDUvbnmwDH8RVHRHq2wiaJ46OnVOYc3qpzVRxgwGgiSk7Ua0j86llwZ38uEnvsbWWa2PYXL%2BhPdqALecpNquEcPC3mZaiCs%2B7AyD9nOOrmeY2Sg07nM8%2BEusET11RwAUh2Jd4IKq5Omelq8YBhU0Avb%2FWylW5G3FTcolgCrUi79241QoP84znuI%2BIMjYrCnhoZjtDPC0CaAMi9He0kUUjKmEdoPMD9zsweL4%2FOVTXv8YXixBWzHSECDv3DcYG%2FmddmKy7nS0tHDFhAJbaZUYuT%2FyrD0DQwLxaGJV6pE3Zd3GhivGMyRsWyAbMYqaeGi9cQhnVsTs6FQZIjiJDf14J3xvoOswLjnFPdVrHtUOYq0rZA1t5nOMSC%2F2X1fNq2vHIWCqGp%2BjW6I8eLQxr0yLOFKWvhupIQNDUC4WS4oC1x4amzZkw0GwcBzVKkvlt%2B2cuw6hdVzr%2FZetOOfAmRe3%2FTpiUY4meQPVALnxb%2BKJqfpSVpDZUKa3Ge%2FT%2FYYiX20wzfyJvQY6pgH9497IOsR74k7Xl8yHG9ShJ2%2BdTbGohFa78f6w0d9a138z5Qyf%2BC4Y1Xn%2FIoHQMV%2Bf5ftaUAaj9zHC4k0JTG0KESR7u61S22BxjwcpSEc6qDRd3FtXdwYxD7FxSdXfVETeujA16d4iU1SjmnZLeSXhcWuuE09CpBUZFGyJAYszqDou5tPJGB%2FpfPtcTswl2k5%2FonhxZSA0FzfYVi6prAB8pj%2BwiniW&X-Amz-Signature=34427bef44f9a24decb5a10f7ba6ad4cdcdc07aa00bb82c6746ac741c1c090be&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WIZGSPDC%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJGMEQCICDisg6kIh3WI1ThWBwg%2Bkp3h0Ibjr%2Fjw0Yoc3T48IODAiAOlPaSCDtaPLnPNKvlfS5C7AAEJ1QWQ%2B%2B2EFkysY8xbSr%2FAwg2EAAaDDYzNzQyMzE4MzgwNSIM2oSYOZcZyVCrII3nKtwDrz9b1d8wokqVzqFylj0uKQ87zozU8Vp2AX8OvBzC6TtszZhL6rB6ImcgeU13QtJ5eJzowwnmE84CsGOPqV0YWlc%2FUuGTYCmmHkwhVcepp6EGDDXu%2BKH69tlXdnpxhDUvbnmwDH8RVHRHq2wiaJ46OnVOYc3qpzVRxgwGgiSk7Ua0j86llwZ38uEnvsbWWa2PYXL%2BhPdqALecpNquEcPC3mZaiCs%2B7AyD9nOOrmeY2Sg07nM8%2BEusET11RwAUh2Jd4IKq5Omelq8YBhU0Avb%2FWylW5G3FTcolgCrUi79241QoP84znuI%2BIMjYrCnhoZjtDPC0CaAMi9He0kUUjKmEdoPMD9zsweL4%2FOVTXv8YXixBWzHSECDv3DcYG%2FmddmKy7nS0tHDFhAJbaZUYuT%2FyrD0DQwLxaGJV6pE3Zd3GhivGMyRsWyAbMYqaeGi9cQhnVsTs6FQZIjiJDf14J3xvoOswLjnFPdVrHtUOYq0rZA1t5nOMSC%2F2X1fNq2vHIWCqGp%2BjW6I8eLQxr0yLOFKWvhupIQNDUC4WS4oC1x4amzZkw0GwcBzVKkvlt%2B2cuw6hdVzr%2FZetOOfAmRe3%2FTpiUY4meQPVALnxb%2BKJqfpSVpDZUKa3Ge%2FT%2FYYiX20wzfyJvQY6pgH9497IOsR74k7Xl8yHG9ShJ2%2BdTbGohFa78f6w0d9a138z5Qyf%2BC4Y1Xn%2FIoHQMV%2Bf5ftaUAaj9zHC4k0JTG0KESR7u61S22BxjwcpSEc6qDRd3FtXdwYxD7FxSdXfVETeujA16d4iU1SjmnZLeSXhcWuuE09CpBUZFGyJAYszqDou5tPJGB%2FpfPtcTswl2k5%2FonhxZSA0FzfYVi6prAB8pj%2BwiniW&X-Amz-Signature=68c7c138da0f99a2c69a9a136b2f8b21dfe2f008c4cbf7db15a32da0a84964db&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WIZGSPDC%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJGMEQCICDisg6kIh3WI1ThWBwg%2Bkp3h0Ibjr%2Fjw0Yoc3T48IODAiAOlPaSCDtaPLnPNKvlfS5C7AAEJ1QWQ%2B%2B2EFkysY8xbSr%2FAwg2EAAaDDYzNzQyMzE4MzgwNSIM2oSYOZcZyVCrII3nKtwDrz9b1d8wokqVzqFylj0uKQ87zozU8Vp2AX8OvBzC6TtszZhL6rB6ImcgeU13QtJ5eJzowwnmE84CsGOPqV0YWlc%2FUuGTYCmmHkwhVcepp6EGDDXu%2BKH69tlXdnpxhDUvbnmwDH8RVHRHq2wiaJ46OnVOYc3qpzVRxgwGgiSk7Ua0j86llwZ38uEnvsbWWa2PYXL%2BhPdqALecpNquEcPC3mZaiCs%2B7AyD9nOOrmeY2Sg07nM8%2BEusET11RwAUh2Jd4IKq5Omelq8YBhU0Avb%2FWylW5G3FTcolgCrUi79241QoP84znuI%2BIMjYrCnhoZjtDPC0CaAMi9He0kUUjKmEdoPMD9zsweL4%2FOVTXv8YXixBWzHSECDv3DcYG%2FmddmKy7nS0tHDFhAJbaZUYuT%2FyrD0DQwLxaGJV6pE3Zd3GhivGMyRsWyAbMYqaeGi9cQhnVsTs6FQZIjiJDf14J3xvoOswLjnFPdVrHtUOYq0rZA1t5nOMSC%2F2X1fNq2vHIWCqGp%2BjW6I8eLQxr0yLOFKWvhupIQNDUC4WS4oC1x4amzZkw0GwcBzVKkvlt%2B2cuw6hdVzr%2FZetOOfAmRe3%2FTpiUY4meQPVALnxb%2BKJqfpSVpDZUKa3Ge%2FT%2FYYiX20wzfyJvQY6pgH9497IOsR74k7Xl8yHG9ShJ2%2BdTbGohFa78f6w0d9a138z5Qyf%2BC4Y1Xn%2FIoHQMV%2Bf5ftaUAaj9zHC4k0JTG0KESR7u61S22BxjwcpSEc6qDRd3FtXdwYxD7FxSdXfVETeujA16d4iU1SjmnZLeSXhcWuuE09CpBUZFGyJAYszqDou5tPJGB%2FpfPtcTswl2k5%2FonhxZSA0FzfYVi6prAB8pj%2BwiniW&X-Amz-Signature=114dafb18c36963de49d9960aa25f3e921d8d032547c101c217225655d18e971&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
