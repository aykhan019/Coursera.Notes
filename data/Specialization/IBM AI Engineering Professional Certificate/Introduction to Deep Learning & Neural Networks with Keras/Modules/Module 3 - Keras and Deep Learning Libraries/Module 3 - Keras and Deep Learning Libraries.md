

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635AYSJKX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDgyYyRT%2FDx7txG7NvZlHfxBYElfYmmVfbM7o5KXrwBawIgdo0tIDeU1%2FHAJw0pSoPAojNVs8bPSvmFQ4B5XgXoQ%2F0qiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPDiH0qRoHMr9jOp7ircA97YM%2F6Xfw0fkk6XNyAWnDKnHJ504zxgBo02CZhWE%2FSW6SXdn6J8Q8JEqtt2ysX1fXdsMkIa6AfTgessy2Dy0k0f6vMojJxcuTE5zwlmE6OMDRjHS%2F%2BEtGp32HxE%2FL851Rdl7LxqV5w9srLm6b4TpYPtoiwYoWMuM8ziNF1blf4Ui0W%2BR%2FsEm%2Bbz3DgU6sAm5ekPYRQ3ipQKNr6sYgL2R255LUHBdsVCUDQbGPal4RA53wiHnIr3LZ8%2Fwwdwijzi8moTF2mR95kMYTVEZwnEoku%2F0YDCTrpccP22HNbW6xvEYBRbP6efkmGG5Cx%2Bbszfw%2BbLveFMi9EvOSpPh18zdBTsf48MgIK8DnruGU2soc13dVBfnFPLD32L3x43lWUBiHKsFAzg9UGow5q5m4YWIieweLGGvIyIq0c1Gnn%2FbkXQVp5ur6%2FkIVM1KL33AIN480WL%2B0CP3yS%2Fl9830qqEVsMrXqSq9zFLuHNvNY0cXZl5IDSsNxnU%2BcHX8mOJ4dkTT8nWm%2FSAJwjmI%2BFik4bagmL0rMnqNN6lpVfrRBISX97qDJDX1qAO88hL60OhlIPqameQEyZZA92dMWk14z%2F0ad9jgclXRO1YOWhypvfI4YmLESLlBuEvLX07MARBMNCx67wGOqUBw0K4VeJ2XdWDiy1u%2FeEJ61Y9dG4EHg57ERddQuMuTMimjEClUCymoabKcWHn9JJ%2Fpr5OHpu2Pjs453ZOJdGrWhS8tMMjAIuHjgdijxsRJ9%2FJLGEXta3mGiYzbah54fTBABu42zAKw4P1%2FBLVoYfaaZVEJ08evWccf2FnwiYxIv1ls3SyUUcx6yVxXvaQnhlmQOVyHcFjvq%2FuKEhDA6XbByYsyu27&X-Amz-Signature=6f197dd938fd35de214a67d776c89e2fa9d47f95eb5a396558b524cda378b253&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635AYSJKX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDgyYyRT%2FDx7txG7NvZlHfxBYElfYmmVfbM7o5KXrwBawIgdo0tIDeU1%2FHAJw0pSoPAojNVs8bPSvmFQ4B5XgXoQ%2F0qiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPDiH0qRoHMr9jOp7ircA97YM%2F6Xfw0fkk6XNyAWnDKnHJ504zxgBo02CZhWE%2FSW6SXdn6J8Q8JEqtt2ysX1fXdsMkIa6AfTgessy2Dy0k0f6vMojJxcuTE5zwlmE6OMDRjHS%2F%2BEtGp32HxE%2FL851Rdl7LxqV5w9srLm6b4TpYPtoiwYoWMuM8ziNF1blf4Ui0W%2BR%2FsEm%2Bbz3DgU6sAm5ekPYRQ3ipQKNr6sYgL2R255LUHBdsVCUDQbGPal4RA53wiHnIr3LZ8%2Fwwdwijzi8moTF2mR95kMYTVEZwnEoku%2F0YDCTrpccP22HNbW6xvEYBRbP6efkmGG5Cx%2Bbszfw%2BbLveFMi9EvOSpPh18zdBTsf48MgIK8DnruGU2soc13dVBfnFPLD32L3x43lWUBiHKsFAzg9UGow5q5m4YWIieweLGGvIyIq0c1Gnn%2FbkXQVp5ur6%2FkIVM1KL33AIN480WL%2B0CP3yS%2Fl9830qqEVsMrXqSq9zFLuHNvNY0cXZl5IDSsNxnU%2BcHX8mOJ4dkTT8nWm%2FSAJwjmI%2BFik4bagmL0rMnqNN6lpVfrRBISX97qDJDX1qAO88hL60OhlIPqameQEyZZA92dMWk14z%2F0ad9jgclXRO1YOWhypvfI4YmLESLlBuEvLX07MARBMNCx67wGOqUBw0K4VeJ2XdWDiy1u%2FeEJ61Y9dG4EHg57ERddQuMuTMimjEClUCymoabKcWHn9JJ%2Fpr5OHpu2Pjs453ZOJdGrWhS8tMMjAIuHjgdijxsRJ9%2FJLGEXta3mGiYzbah54fTBABu42zAKw4P1%2FBLVoYfaaZVEJ08evWccf2FnwiYxIv1ls3SyUUcx6yVxXvaQnhlmQOVyHcFjvq%2FuKEhDA6XbByYsyu27&X-Amz-Signature=57a6411d29c1b58c7301545505b071beea97e6426a4f32b368399ea67e3557fd&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635AYSJKX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDgyYyRT%2FDx7txG7NvZlHfxBYElfYmmVfbM7o5KXrwBawIgdo0tIDeU1%2FHAJw0pSoPAojNVs8bPSvmFQ4B5XgXoQ%2F0qiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPDiH0qRoHMr9jOp7ircA97YM%2F6Xfw0fkk6XNyAWnDKnHJ504zxgBo02CZhWE%2FSW6SXdn6J8Q8JEqtt2ysX1fXdsMkIa6AfTgessy2Dy0k0f6vMojJxcuTE5zwlmE6OMDRjHS%2F%2BEtGp32HxE%2FL851Rdl7LxqV5w9srLm6b4TpYPtoiwYoWMuM8ziNF1blf4Ui0W%2BR%2FsEm%2Bbz3DgU6sAm5ekPYRQ3ipQKNr6sYgL2R255LUHBdsVCUDQbGPal4RA53wiHnIr3LZ8%2Fwwdwijzi8moTF2mR95kMYTVEZwnEoku%2F0YDCTrpccP22HNbW6xvEYBRbP6efkmGG5Cx%2Bbszfw%2BbLveFMi9EvOSpPh18zdBTsf48MgIK8DnruGU2soc13dVBfnFPLD32L3x43lWUBiHKsFAzg9UGow5q5m4YWIieweLGGvIyIq0c1Gnn%2FbkXQVp5ur6%2FkIVM1KL33AIN480WL%2B0CP3yS%2Fl9830qqEVsMrXqSq9zFLuHNvNY0cXZl5IDSsNxnU%2BcHX8mOJ4dkTT8nWm%2FSAJwjmI%2BFik4bagmL0rMnqNN6lpVfrRBISX97qDJDX1qAO88hL60OhlIPqameQEyZZA92dMWk14z%2F0ad9jgclXRO1YOWhypvfI4YmLESLlBuEvLX07MARBMNCx67wGOqUBw0K4VeJ2XdWDiy1u%2FeEJ61Y9dG4EHg57ERddQuMuTMimjEClUCymoabKcWHn9JJ%2Fpr5OHpu2Pjs453ZOJdGrWhS8tMMjAIuHjgdijxsRJ9%2FJLGEXta3mGiYzbah54fTBABu42zAKw4P1%2FBLVoYfaaZVEJ08evWccf2FnwiYxIv1ls3SyUUcx6yVxXvaQnhlmQOVyHcFjvq%2FuKEhDA6XbByYsyu27&X-Amz-Signature=12c90a2039400d2ea6008147f7f25363d18ec4667192048b20413e5f11ba72d0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDO4SL7F%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023934Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDU0GEhLfIwgB4pyjlK9Afdoep9GfyCCSMzrWgVU9wp9AiEAjO7Ka5qvzSxb9pqueIVTVzYq%2FLk2NLAB0CcwZp0KDGMqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPcMbLS7V5HTDbdWjircA%2B%2BPALtMniZIG73UFBWYrvgF8JG5ZwkI1uR94gV9p%2F%2FSq70s1%2FSc5Hj1uaYLUedbJVkmAF1IQV5uoFyxKhpvpMDnqeLz%2BzG82xhCQgFqcEXK%2BQe1rAL9gkL3EXRlltOyKxO8nrAPaNVxRA8gzcToVPak30R3lLnvzRixPS618AOIukhb9zNCH2k8MiC8jZS3vibm9p4fMS4kaBxEcNBeprbBkj1L02fzBqoQzsIsPtcouscaLOCZY4sxqRQMgkq1v3kKi7MVRNP0RuRsFNHq%2BIM8yIkKEDJt2IhXaRYSoXm%2F5T%2Bpf%2BOjXQDs1rfFkj55t3ygjgMWoxzqKmIt2TXNoqGM8XGaxP6%2BmjWjuJEEE8QPjp0bd6rWPiM4xPVJOQAlsCTK%2F%2B7NR3epAp1rUroZdhSci1U9CrYWVSkAVMnmQnCPc201bH3N2aFaDVI0C2KLgoR%2F6OYoOFl5Gt5t11IkIynO44I4NRWOJPIywcdgESZxwXaRDZWXS4bPND9iehLtlxc0zl%2FISQRwEnmdjs5uS07BhEcKgHiyUqTc767AvwFTY%2BywqvMoNuy9%2BNS6W4A7z00qrGrUOmBzJiRHLy4i9x9O96MJ87L%2F1LSBEwp1yTZeyvBIDkEm68qFLdJ%2BMI2y67wGOqUBsjdWyyD5dr%2Fg73FfMYUMZeHFlKnMvuoqskDxk8o0KfTuyv%2FtIfsO1yvi7NFF0y0xbvaQ%2B8RPztF6yDNGBpNuMTqvh1ZBpXXgy6JZd7F7EzS83ZvIj9v1q1isyf%2F5EsO01%2Fq0dyaq7bEfmj7j1WpgEFDyfRE%2Fs4A1JuDNRwWDXDKd30hT%2FnnHPQpXT2cW%2F74vsroxWUM8d43kEkUSdNgYMbp4F5NU&X-Amz-Signature=e522f0891af439fdfc19c2f0b5756c95e3018de894f62f52e0fce749825eb430&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664QT7ED6B%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCuZIU95uZFhLdRHJA%2BUDlJf94gfIs%2FHJ2DH8gSSi%2B24wIgdWOUyCIGssuNBJz0XDXKyJPaObMe%2Fatyq%2Bm6c5voDcYqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPDh2KDqrHh2LX1o5ircAwOqotdRnvGZso53iF%2BtxR9NQIHiMSck54%2FDgyq8FWQlcyRcaUYpeYC7ZB2HTsmAjJlMDpnSO%2FmfE69zR954R6hDlghLAMwsGUc2EF6ooF9J6NNPqf3iwP040ua6y3Fa52l6u6zirt5HKyqNwkoyPD%2B4RgvyDbO12bxlgAq%2Fpcp3dfmgFNb5N6JH7gVG5%2FC0Wj%2BBiL2v%2BdoR%2FfiMl6O7l5doUVjPh0dnIhXtYGciQXc06ANdiTgQZeF7gsW3izI0Z8QkLKhizag3APZ%2BBNgkFaXloOCWKgZPEMz1EUs8LsDyqZBtFwbxgxoP7CZtprEKK%2FvhMwSTtZEVMrQXp%2Fk9WGNuxbZRzQIsTcaA%2FNmocvgxrD1CAd%2Bapw61E4NpTuk5qTu2gKp46CA4TA%2F1TQ9yO87x9%2BgO02PT2OElB52aNLDY%2BuHg3FvldP7W5JBAKLm3hNNGyE4%2B4vfm2DK8AApuNkj5Zk8UzYtnzb0j7Fqr%2F600V3RhdWNIDa2AjGkQ4sK8VuahVTL5p7OMWQHSP4q4%2Be37ICnPG4Meo%2BCzJrBVjAJ1n%2FJV8WGFlQsMocLLEK%2B5qp4%2B8Vk9vkOHQrWmvBkzkXbxYSnba35pf55G17Pnnrhp8UzNi5hDQmWoyz2YMMWy67wGOqUB8SA7TjLnOuskWnamLgAs2JNh%2F9yZH7s%2F%2BIVdzGiAOMmUnMGQzq6UCzLxwhtz8UqJfNeIPWBO4fcBXYVf1X848RJ9LXuc82wKMnTjVLrRVYR027%2B%2BbNLvuF%2FNbwHY4nedIEJcem8tkLihseb1WKYcFu2xNVVnfdrXde%2BwWAVs8R6gbx5PLAUj7yHProBBAKffXU5zNn99p2BkpAOnZPkrYwOa2i2y&X-Amz-Signature=fe82d4254a257a51225f1c65f69e1529f69c81144f66ed7e76bc07868c998a72&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635AYSJKX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDgyYyRT%2FDx7txG7NvZlHfxBYElfYmmVfbM7o5KXrwBawIgdo0tIDeU1%2FHAJw0pSoPAojNVs8bPSvmFQ4B5XgXoQ%2F0qiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPDiH0qRoHMr9jOp7ircA97YM%2F6Xfw0fkk6XNyAWnDKnHJ504zxgBo02CZhWE%2FSW6SXdn6J8Q8JEqtt2ysX1fXdsMkIa6AfTgessy2Dy0k0f6vMojJxcuTE5zwlmE6OMDRjHS%2F%2BEtGp32HxE%2FL851Rdl7LxqV5w9srLm6b4TpYPtoiwYoWMuM8ziNF1blf4Ui0W%2BR%2FsEm%2Bbz3DgU6sAm5ekPYRQ3ipQKNr6sYgL2R255LUHBdsVCUDQbGPal4RA53wiHnIr3LZ8%2Fwwdwijzi8moTF2mR95kMYTVEZwnEoku%2F0YDCTrpccP22HNbW6xvEYBRbP6efkmGG5Cx%2Bbszfw%2BbLveFMi9EvOSpPh18zdBTsf48MgIK8DnruGU2soc13dVBfnFPLD32L3x43lWUBiHKsFAzg9UGow5q5m4YWIieweLGGvIyIq0c1Gnn%2FbkXQVp5ur6%2FkIVM1KL33AIN480WL%2B0CP3yS%2Fl9830qqEVsMrXqSq9zFLuHNvNY0cXZl5IDSsNxnU%2BcHX8mOJ4dkTT8nWm%2FSAJwjmI%2BFik4bagmL0rMnqNN6lpVfrRBISX97qDJDX1qAO88hL60OhlIPqameQEyZZA92dMWk14z%2F0ad9jgclXRO1YOWhypvfI4YmLESLlBuEvLX07MARBMNCx67wGOqUBw0K4VeJ2XdWDiy1u%2FeEJ61Y9dG4EHg57ERddQuMuTMimjEClUCymoabKcWHn9JJ%2Fpr5OHpu2Pjs453ZOJdGrWhS8tMMjAIuHjgdijxsRJ9%2FJLGEXta3mGiYzbah54fTBABu42zAKw4P1%2FBLVoYfaaZVEJ08evWccf2FnwiYxIv1ls3SyUUcx6yVxXvaQnhlmQOVyHcFjvq%2FuKEhDA6XbByYsyu27&X-Amz-Signature=64684451f30b0258f90b6ccdc16a5d8fcdbcde11a463836989d0cfa227cb8599&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635AYSJKX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDgyYyRT%2FDx7txG7NvZlHfxBYElfYmmVfbM7o5KXrwBawIgdo0tIDeU1%2FHAJw0pSoPAojNVs8bPSvmFQ4B5XgXoQ%2F0qiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPDiH0qRoHMr9jOp7ircA97YM%2F6Xfw0fkk6XNyAWnDKnHJ504zxgBo02CZhWE%2FSW6SXdn6J8Q8JEqtt2ysX1fXdsMkIa6AfTgessy2Dy0k0f6vMojJxcuTE5zwlmE6OMDRjHS%2F%2BEtGp32HxE%2FL851Rdl7LxqV5w9srLm6b4TpYPtoiwYoWMuM8ziNF1blf4Ui0W%2BR%2FsEm%2Bbz3DgU6sAm5ekPYRQ3ipQKNr6sYgL2R255LUHBdsVCUDQbGPal4RA53wiHnIr3LZ8%2Fwwdwijzi8moTF2mR95kMYTVEZwnEoku%2F0YDCTrpccP22HNbW6xvEYBRbP6efkmGG5Cx%2Bbszfw%2BbLveFMi9EvOSpPh18zdBTsf48MgIK8DnruGU2soc13dVBfnFPLD32L3x43lWUBiHKsFAzg9UGow5q5m4YWIieweLGGvIyIq0c1Gnn%2FbkXQVp5ur6%2FkIVM1KL33AIN480WL%2B0CP3yS%2Fl9830qqEVsMrXqSq9zFLuHNvNY0cXZl5IDSsNxnU%2BcHX8mOJ4dkTT8nWm%2FSAJwjmI%2BFik4bagmL0rMnqNN6lpVfrRBISX97qDJDX1qAO88hL60OhlIPqameQEyZZA92dMWk14z%2F0ad9jgclXRO1YOWhypvfI4YmLESLlBuEvLX07MARBMNCx67wGOqUBw0K4VeJ2XdWDiy1u%2FeEJ61Y9dG4EHg57ERddQuMuTMimjEClUCymoabKcWHn9JJ%2Fpr5OHpu2Pjs453ZOJdGrWhS8tMMjAIuHjgdijxsRJ9%2FJLGEXta3mGiYzbah54fTBABu42zAKw4P1%2FBLVoYfaaZVEJ08evWccf2FnwiYxIv1ls3SyUUcx6yVxXvaQnhlmQOVyHcFjvq%2FuKEhDA6XbByYsyu27&X-Amz-Signature=11c467aef672464b9aedb9345851c5f909f5b26bdd9c44dc9f5ead0cf8bd51a8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635AYSJKX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDgyYyRT%2FDx7txG7NvZlHfxBYElfYmmVfbM7o5KXrwBawIgdo0tIDeU1%2FHAJw0pSoPAojNVs8bPSvmFQ4B5XgXoQ%2F0qiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPDiH0qRoHMr9jOp7ircA97YM%2F6Xfw0fkk6XNyAWnDKnHJ504zxgBo02CZhWE%2FSW6SXdn6J8Q8JEqtt2ysX1fXdsMkIa6AfTgessy2Dy0k0f6vMojJxcuTE5zwlmE6OMDRjHS%2F%2BEtGp32HxE%2FL851Rdl7LxqV5w9srLm6b4TpYPtoiwYoWMuM8ziNF1blf4Ui0W%2BR%2FsEm%2Bbz3DgU6sAm5ekPYRQ3ipQKNr6sYgL2R255LUHBdsVCUDQbGPal4RA53wiHnIr3LZ8%2Fwwdwijzi8moTF2mR95kMYTVEZwnEoku%2F0YDCTrpccP22HNbW6xvEYBRbP6efkmGG5Cx%2Bbszfw%2BbLveFMi9EvOSpPh18zdBTsf48MgIK8DnruGU2soc13dVBfnFPLD32L3x43lWUBiHKsFAzg9UGow5q5m4YWIieweLGGvIyIq0c1Gnn%2FbkXQVp5ur6%2FkIVM1KL33AIN480WL%2B0CP3yS%2Fl9830qqEVsMrXqSq9zFLuHNvNY0cXZl5IDSsNxnU%2BcHX8mOJ4dkTT8nWm%2FSAJwjmI%2BFik4bagmL0rMnqNN6lpVfrRBISX97qDJDX1qAO88hL60OhlIPqameQEyZZA92dMWk14z%2F0ad9jgclXRO1YOWhypvfI4YmLESLlBuEvLX07MARBMNCx67wGOqUBw0K4VeJ2XdWDiy1u%2FeEJ61Y9dG4EHg57ERddQuMuTMimjEClUCymoabKcWHn9JJ%2Fpr5OHpu2Pjs453ZOJdGrWhS8tMMjAIuHjgdijxsRJ9%2FJLGEXta3mGiYzbah54fTBABu42zAKw4P1%2FBLVoYfaaZVEJ08evWccf2FnwiYxIv1ls3SyUUcx6yVxXvaQnhlmQOVyHcFjvq%2FuKEhDA6XbByYsyu27&X-Amz-Signature=a04303e02b0450ef670a43f27a228f394c68321c8509e6d7e127085a3d835c80&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635AYSJKX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDgyYyRT%2FDx7txG7NvZlHfxBYElfYmmVfbM7o5KXrwBawIgdo0tIDeU1%2FHAJw0pSoPAojNVs8bPSvmFQ4B5XgXoQ%2F0qiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPDiH0qRoHMr9jOp7ircA97YM%2F6Xfw0fkk6XNyAWnDKnHJ504zxgBo02CZhWE%2FSW6SXdn6J8Q8JEqtt2ysX1fXdsMkIa6AfTgessy2Dy0k0f6vMojJxcuTE5zwlmE6OMDRjHS%2F%2BEtGp32HxE%2FL851Rdl7LxqV5w9srLm6b4TpYPtoiwYoWMuM8ziNF1blf4Ui0W%2BR%2FsEm%2Bbz3DgU6sAm5ekPYRQ3ipQKNr6sYgL2R255LUHBdsVCUDQbGPal4RA53wiHnIr3LZ8%2Fwwdwijzi8moTF2mR95kMYTVEZwnEoku%2F0YDCTrpccP22HNbW6xvEYBRbP6efkmGG5Cx%2Bbszfw%2BbLveFMi9EvOSpPh18zdBTsf48MgIK8DnruGU2soc13dVBfnFPLD32L3x43lWUBiHKsFAzg9UGow5q5m4YWIieweLGGvIyIq0c1Gnn%2FbkXQVp5ur6%2FkIVM1KL33AIN480WL%2B0CP3yS%2Fl9830qqEVsMrXqSq9zFLuHNvNY0cXZl5IDSsNxnU%2BcHX8mOJ4dkTT8nWm%2FSAJwjmI%2BFik4bagmL0rMnqNN6lpVfrRBISX97qDJDX1qAO88hL60OhlIPqameQEyZZA92dMWk14z%2F0ad9jgclXRO1YOWhypvfI4YmLESLlBuEvLX07MARBMNCx67wGOqUBw0K4VeJ2XdWDiy1u%2FeEJ61Y9dG4EHg57ERddQuMuTMimjEClUCymoabKcWHn9JJ%2Fpr5OHpu2Pjs453ZOJdGrWhS8tMMjAIuHjgdijxsRJ9%2FJLGEXta3mGiYzbah54fTBABu42zAKw4P1%2FBLVoYfaaZVEJ08evWccf2FnwiYxIv1ls3SyUUcx6yVxXvaQnhlmQOVyHcFjvq%2FuKEhDA6XbByYsyu27&X-Amz-Signature=f992ccfad605196b2930aa24f31f7391cd40af11afdb416ee4e3b05a72749ac0&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
