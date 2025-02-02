

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ZA74G2A%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171241Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHJmMN6m50vZZ0GJbv3rVooQvZeASXNHQaterv8zMLYmAiA7xga7AXXKkIa6fzAt%2BT8jAYoM5bdPXcpIiphixsDscyqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMoQtHowVowavjbYTzKtwDrY%2BgnrZJsfEW6ydeZ0cw%2FUuxJjuRr7Ykp69tb73fGvdU8qXatr74kot0D2qQJphjYwYbhNAfQr4yRnB3AOHSj4N6dG243ASAeEJjC9paDGWlP2CJXHd%2BxesHxt5K4dMw2eOFXe8jDDeexo8QLuAvZETiSqaCDFh%2FR9ExN72WKsa6eHjLNrIrpR7BiLJ1Xvxo96igxbwwhT6ogxEeg%2FfYUcC%2FgjSD1R%2BI99EJ6Nj%2FfpkujrCFQ8CggmlUYCT9dp30cTXkedNs5sTUluScHQoNBACrDNZtOVeo9CsQNl6R0lLUpWNyl%2BNvgDREE%2FDzkFYoc6Eb3rj6ODSZhoHH%2B8Y47PRdlHs6FCBzyU6iJu9aecV0EiaFdl60gnlTxpAyBKnnyEOLmG0GaY9SYxp31acYyUOUA7%2BBwmNLCt%2Bz1ImHr%2Fw1c26uIZYLEANIIvpmZ74bwYdcp14vNeCAz2CfS7b%2FA3nx%2B3zw5%2B7xJPNppYqW1%2BuKMeRk4WuirrsDmnfulKJq1MnR%2FUfHm0KowrP721jfW3lJmtEYe8ve0sL2ypi8yxlHZK0gYPm2Z7eKEWAh2PY118NeXgGdV2SVhFgjPcEU9BOxXrftySkHk5GXT%2FelDSyGMOxxAJT%2B%2B%2Bxpx8kw5Lj9vAY6pgG7IbHeUcR%2BYuHRsjPa5wGKLDtZB6j1ToFMki1BBNW15mUhX%2BCsOORutfWonIvupzoZH0ZMuoJn1M3Ln8skBNO%2FiGV0UQQyjAZyylESiAeg4VNQdI8YsQBa6QLtrkvpTehlfHH3pC1SeqwDR3VUmlVAmOBdTK4ErgyxMQpAIP5tg6j%2BXFU7GIz2FYSmQcjo6IrShxKH8loBUxnkpo9%2F2T16DCQlKF9x&X-Amz-Signature=9973f0024d04cfdf28da07a0a93858db4e86c819ad87f3793fa40dd6c94b49ef&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ZA74G2A%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171241Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHJmMN6m50vZZ0GJbv3rVooQvZeASXNHQaterv8zMLYmAiA7xga7AXXKkIa6fzAt%2BT8jAYoM5bdPXcpIiphixsDscyqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMoQtHowVowavjbYTzKtwDrY%2BgnrZJsfEW6ydeZ0cw%2FUuxJjuRr7Ykp69tb73fGvdU8qXatr74kot0D2qQJphjYwYbhNAfQr4yRnB3AOHSj4N6dG243ASAeEJjC9paDGWlP2CJXHd%2BxesHxt5K4dMw2eOFXe8jDDeexo8QLuAvZETiSqaCDFh%2FR9ExN72WKsa6eHjLNrIrpR7BiLJ1Xvxo96igxbwwhT6ogxEeg%2FfYUcC%2FgjSD1R%2BI99EJ6Nj%2FfpkujrCFQ8CggmlUYCT9dp30cTXkedNs5sTUluScHQoNBACrDNZtOVeo9CsQNl6R0lLUpWNyl%2BNvgDREE%2FDzkFYoc6Eb3rj6ODSZhoHH%2B8Y47PRdlHs6FCBzyU6iJu9aecV0EiaFdl60gnlTxpAyBKnnyEOLmG0GaY9SYxp31acYyUOUA7%2BBwmNLCt%2Bz1ImHr%2Fw1c26uIZYLEANIIvpmZ74bwYdcp14vNeCAz2CfS7b%2FA3nx%2B3zw5%2B7xJPNppYqW1%2BuKMeRk4WuirrsDmnfulKJq1MnR%2FUfHm0KowrP721jfW3lJmtEYe8ve0sL2ypi8yxlHZK0gYPm2Z7eKEWAh2PY118NeXgGdV2SVhFgjPcEU9BOxXrftySkHk5GXT%2FelDSyGMOxxAJT%2B%2B%2Bxpx8kw5Lj9vAY6pgG7IbHeUcR%2BYuHRsjPa5wGKLDtZB6j1ToFMki1BBNW15mUhX%2BCsOORutfWonIvupzoZH0ZMuoJn1M3Ln8skBNO%2FiGV0UQQyjAZyylESiAeg4VNQdI8YsQBa6QLtrkvpTehlfHH3pC1SeqwDR3VUmlVAmOBdTK4ErgyxMQpAIP5tg6j%2BXFU7GIz2FYSmQcjo6IrShxKH8loBUxnkpo9%2F2T16DCQlKF9x&X-Amz-Signature=74c0da0e35b6ad92f0341a1214c0e36623e750980925905ba4254143d476286a&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ZA74G2A%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171241Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHJmMN6m50vZZ0GJbv3rVooQvZeASXNHQaterv8zMLYmAiA7xga7AXXKkIa6fzAt%2BT8jAYoM5bdPXcpIiphixsDscyqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMoQtHowVowavjbYTzKtwDrY%2BgnrZJsfEW6ydeZ0cw%2FUuxJjuRr7Ykp69tb73fGvdU8qXatr74kot0D2qQJphjYwYbhNAfQr4yRnB3AOHSj4N6dG243ASAeEJjC9paDGWlP2CJXHd%2BxesHxt5K4dMw2eOFXe8jDDeexo8QLuAvZETiSqaCDFh%2FR9ExN72WKsa6eHjLNrIrpR7BiLJ1Xvxo96igxbwwhT6ogxEeg%2FfYUcC%2FgjSD1R%2BI99EJ6Nj%2FfpkujrCFQ8CggmlUYCT9dp30cTXkedNs5sTUluScHQoNBACrDNZtOVeo9CsQNl6R0lLUpWNyl%2BNvgDREE%2FDzkFYoc6Eb3rj6ODSZhoHH%2B8Y47PRdlHs6FCBzyU6iJu9aecV0EiaFdl60gnlTxpAyBKnnyEOLmG0GaY9SYxp31acYyUOUA7%2BBwmNLCt%2Bz1ImHr%2Fw1c26uIZYLEANIIvpmZ74bwYdcp14vNeCAz2CfS7b%2FA3nx%2B3zw5%2B7xJPNppYqW1%2BuKMeRk4WuirrsDmnfulKJq1MnR%2FUfHm0KowrP721jfW3lJmtEYe8ve0sL2ypi8yxlHZK0gYPm2Z7eKEWAh2PY118NeXgGdV2SVhFgjPcEU9BOxXrftySkHk5GXT%2FelDSyGMOxxAJT%2B%2B%2Bxpx8kw5Lj9vAY6pgG7IbHeUcR%2BYuHRsjPa5wGKLDtZB6j1ToFMki1BBNW15mUhX%2BCsOORutfWonIvupzoZH0ZMuoJn1M3Ln8skBNO%2FiGV0UQQyjAZyylESiAeg4VNQdI8YsQBa6QLtrkvpTehlfHH3pC1SeqwDR3VUmlVAmOBdTK4ErgyxMQpAIP5tg6j%2BXFU7GIz2FYSmQcjo6IrShxKH8loBUxnkpo9%2F2T16DCQlKF9x&X-Amz-Signature=9c9f1e6cea2217a588348bee33979365fbebcf5e376627fec4d99690a50f80f8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XOUVNOXM%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171241Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICX6%2BOWnUL%2BkOMe35O4m7ciGBVOhB4krdxvPPH3gm0LLAiBl5ZnWrs2rkDL8XoDS%2Fx1QNuI6DbtClCYwzaGl8%2Bq%2BASqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM1gE7tE%2FovthTGBWPKtwDj2%2FcXbFhORNGyDITZfrsYCMgALsWBzIRibE7SPdM%2FU0JpB2DShwts6rOKGRrejV30XvUub7KUR36dm0zSCYN6ZLeaRt%2FWJ77%2B4xdecNFoxJ%2FZBDfJ0zE8YpH0OqXqCoMSMYPA9QBpje8ETqvbxwPWPMHt3qNrq2iSZcQD8ZxsyCIlJn6vXpJYSed0XnXYFOn9WJ3R2g7B64LmcqAai4a%2Ft%2BtgYJ5VlfMuzwQyXuYJpeELUPpvzo0jd9wues31f0bHfgv0Q4%2Ft6vhezVwzS9uEibPqdAgdV8KcE91exYSdYPld88p62XvIGFoy0QeAbaYp67D1XLs8DjiLuZDu%2BcnvcOFltwzg96SYAOwz7CidJEc%2FVa8jFh50oDajXTFAGBBGy%2BC9C6Xcwzj2uCTnEUVJ6iGkQIo5Da6H0Sj4pNXDgRPyJJnXZY5E0s8r7GabCpuPohdeMbZwXQqESvhfLdNmS2eTVK4lzrPa0BmhrA%2B8jMSu%2FvDWW0oCfMcUXSWonKHSpm4Ao%2FjoUEfHLwf973Z9T%2FVaEocxk55V2k6nKONSOXpKroS7UzZG9ELpvJBDrZy7X6NCFbzfDrjarabf%2FPFRHsQYE%2Bc7a4cIkJ61Uxf2dnODD8u5hDxMpNujyIwo8L9vAY6pgHAZrBqvq7um7jhN1mQ%2FA8jju1nz9Szjoi%2BWM%2FOoP%2FVZ95kCg%2FrcfyFSt2k84Bkj7MtplHOPmjFx2uC4H%2BN0A278PUPdbRx9sG2cbrydWUAsYArxv%2FWDnbG7%2FGO8ppal5dQi7%2FU2Pz%2BIYBS0zwGLMdJTuKWCmUaiVz%2FRVjykW8bJp9U9FxONdxm7kdwQJi%2BtkQ7lFEnVKOGLhBKY1LeIDP17hYcW5A%2F&X-Amz-Signature=6f3ec5fa8301521a7079d75a383a74b3ff1f9b04c3531d01c27b44397487f254&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662R56JVQD%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171242Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBAcFG4C4qUWDTouTaQ0rP3St0ymyjj2uW3dUZS8sgUXAiBbrv%2FnEyz4GtEAGILvynm0QUvL5bc2kk7pEAyTY9KsnCqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMug0ABNr61Ir365e6KtwDw5nGvoBwoKrH21xoWUYOdEQ4lYBpq6V5MizeLhQHnWhyJw7Xqh%2Bw8T09Qnmdu1aiOis8BBrKBomrTTvTeCwEJ1pba4dS0Sy20Md8l5RiN%2FSSdnF8irVous21W6qOIEuGyTCD77IZCAGVFhCZ4dooZiylN2ftsMFLT2EDwuqjy0Fx2yUEHkEgtQth8VGpNJCcEERusInmAN1Z8pW8OMhj%2Bv1TpwdoeuhdzCWjhexC1tnhT26Ua0NMTRRaMBGKwW%2Fn61wNfNsFuNHqKbiWt%2F1ygBm2XobXER2kvdKYLFBI4e4aco1Bvx99s%2FK9e4GN8SB3WKMNz%2FWe8sQ3macG3Sw6lh3ZDqJQ4rH5VOMomfTAl%2FjYaBSt05wXz85ubPrSLRs%2BjlDe9ximBjN%2FTaYvhBChoz7Gd5QytOG3l%2BUoEmdIiiKAGKXmClQ1ShBduUV%2BgXyjug6b7uLJmGJ5I0W3LbkSGn6Q8A9hfnhu8KqBdk5zetSKbhOmAOcPYhlp99lxTLcjArmYfTgcctZFZyOYoKbKUb9sIx1yVx3yQx9N2F70h38GxP6ATzJ1x0kE58ziSwpLvmudL4RyDAzyhK3GGY%2FlMYCtP%2F18H1QLyKA1hQZWGJJT0jGFYBXiuIN0sUkwmLr9vAY6pgEbO17rREgBTJesKi2xqfHxrOQ36YppqFeJWf5VQP2n7Il%2FUyOC3DFy9nKYKJLzMf8kDqrO9iXDYjSc77kTv1ijIFR3H%2BAA9OHRhgqE6iBxsMN0IYaZksX%2Bz9j%2FyccvQTKT0xQ0qFWG6KZyhyfo6WSE8RWs29Vfph5pE7yE3vk9iTM3EfbpHAdEhB3QhfSzf%2Bx3VACpczcOsA7%2F2l0nU%2B3rWHNSST9W&X-Amz-Signature=b118ad23299f67d6f5424e8108d5ea42fdbfa38f80906283eb5ec75a8775eaf3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ZA74G2A%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171241Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHJmMN6m50vZZ0GJbv3rVooQvZeASXNHQaterv8zMLYmAiA7xga7AXXKkIa6fzAt%2BT8jAYoM5bdPXcpIiphixsDscyqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMoQtHowVowavjbYTzKtwDrY%2BgnrZJsfEW6ydeZ0cw%2FUuxJjuRr7Ykp69tb73fGvdU8qXatr74kot0D2qQJphjYwYbhNAfQr4yRnB3AOHSj4N6dG243ASAeEJjC9paDGWlP2CJXHd%2BxesHxt5K4dMw2eOFXe8jDDeexo8QLuAvZETiSqaCDFh%2FR9ExN72WKsa6eHjLNrIrpR7BiLJ1Xvxo96igxbwwhT6ogxEeg%2FfYUcC%2FgjSD1R%2BI99EJ6Nj%2FfpkujrCFQ8CggmlUYCT9dp30cTXkedNs5sTUluScHQoNBACrDNZtOVeo9CsQNl6R0lLUpWNyl%2BNvgDREE%2FDzkFYoc6Eb3rj6ODSZhoHH%2B8Y47PRdlHs6FCBzyU6iJu9aecV0EiaFdl60gnlTxpAyBKnnyEOLmG0GaY9SYxp31acYyUOUA7%2BBwmNLCt%2Bz1ImHr%2Fw1c26uIZYLEANIIvpmZ74bwYdcp14vNeCAz2CfS7b%2FA3nx%2B3zw5%2B7xJPNppYqW1%2BuKMeRk4WuirrsDmnfulKJq1MnR%2FUfHm0KowrP721jfW3lJmtEYe8ve0sL2ypi8yxlHZK0gYPm2Z7eKEWAh2PY118NeXgGdV2SVhFgjPcEU9BOxXrftySkHk5GXT%2FelDSyGMOxxAJT%2B%2B%2Bxpx8kw5Lj9vAY6pgG7IbHeUcR%2BYuHRsjPa5wGKLDtZB6j1ToFMki1BBNW15mUhX%2BCsOORutfWonIvupzoZH0ZMuoJn1M3Ln8skBNO%2FiGV0UQQyjAZyylESiAeg4VNQdI8YsQBa6QLtrkvpTehlfHH3pC1SeqwDR3VUmlVAmOBdTK4ErgyxMQpAIP5tg6j%2BXFU7GIz2FYSmQcjo6IrShxKH8loBUxnkpo9%2F2T16DCQlKF9x&X-Amz-Signature=c6b9f0d67810ba5d84bde31d1183ae389089f5b8ecd422c6f562faed033c485d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ZA74G2A%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171241Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHJmMN6m50vZZ0GJbv3rVooQvZeASXNHQaterv8zMLYmAiA7xga7AXXKkIa6fzAt%2BT8jAYoM5bdPXcpIiphixsDscyqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMoQtHowVowavjbYTzKtwDrY%2BgnrZJsfEW6ydeZ0cw%2FUuxJjuRr7Ykp69tb73fGvdU8qXatr74kot0D2qQJphjYwYbhNAfQr4yRnB3AOHSj4N6dG243ASAeEJjC9paDGWlP2CJXHd%2BxesHxt5K4dMw2eOFXe8jDDeexo8QLuAvZETiSqaCDFh%2FR9ExN72WKsa6eHjLNrIrpR7BiLJ1Xvxo96igxbwwhT6ogxEeg%2FfYUcC%2FgjSD1R%2BI99EJ6Nj%2FfpkujrCFQ8CggmlUYCT9dp30cTXkedNs5sTUluScHQoNBACrDNZtOVeo9CsQNl6R0lLUpWNyl%2BNvgDREE%2FDzkFYoc6Eb3rj6ODSZhoHH%2B8Y47PRdlHs6FCBzyU6iJu9aecV0EiaFdl60gnlTxpAyBKnnyEOLmG0GaY9SYxp31acYyUOUA7%2BBwmNLCt%2Bz1ImHr%2Fw1c26uIZYLEANIIvpmZ74bwYdcp14vNeCAz2CfS7b%2FA3nx%2B3zw5%2B7xJPNppYqW1%2BuKMeRk4WuirrsDmnfulKJq1MnR%2FUfHm0KowrP721jfW3lJmtEYe8ve0sL2ypi8yxlHZK0gYPm2Z7eKEWAh2PY118NeXgGdV2SVhFgjPcEU9BOxXrftySkHk5GXT%2FelDSyGMOxxAJT%2B%2B%2Bxpx8kw5Lj9vAY6pgG7IbHeUcR%2BYuHRsjPa5wGKLDtZB6j1ToFMki1BBNW15mUhX%2BCsOORutfWonIvupzoZH0ZMuoJn1M3Ln8skBNO%2FiGV0UQQyjAZyylESiAeg4VNQdI8YsQBa6QLtrkvpTehlfHH3pC1SeqwDR3VUmlVAmOBdTK4ErgyxMQpAIP5tg6j%2BXFU7GIz2FYSmQcjo6IrShxKH8loBUxnkpo9%2F2T16DCQlKF9x&X-Amz-Signature=0e897d72bbef1ef376bb0b76022d21f500601afc3e14ecbfa3415995b9268931&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ZA74G2A%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171241Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHJmMN6m50vZZ0GJbv3rVooQvZeASXNHQaterv8zMLYmAiA7xga7AXXKkIa6fzAt%2BT8jAYoM5bdPXcpIiphixsDscyqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMoQtHowVowavjbYTzKtwDrY%2BgnrZJsfEW6ydeZ0cw%2FUuxJjuRr7Ykp69tb73fGvdU8qXatr74kot0D2qQJphjYwYbhNAfQr4yRnB3AOHSj4N6dG243ASAeEJjC9paDGWlP2CJXHd%2BxesHxt5K4dMw2eOFXe8jDDeexo8QLuAvZETiSqaCDFh%2FR9ExN72WKsa6eHjLNrIrpR7BiLJ1Xvxo96igxbwwhT6ogxEeg%2FfYUcC%2FgjSD1R%2BI99EJ6Nj%2FfpkujrCFQ8CggmlUYCT9dp30cTXkedNs5sTUluScHQoNBACrDNZtOVeo9CsQNl6R0lLUpWNyl%2BNvgDREE%2FDzkFYoc6Eb3rj6ODSZhoHH%2B8Y47PRdlHs6FCBzyU6iJu9aecV0EiaFdl60gnlTxpAyBKnnyEOLmG0GaY9SYxp31acYyUOUA7%2BBwmNLCt%2Bz1ImHr%2Fw1c26uIZYLEANIIvpmZ74bwYdcp14vNeCAz2CfS7b%2FA3nx%2B3zw5%2B7xJPNppYqW1%2BuKMeRk4WuirrsDmnfulKJq1MnR%2FUfHm0KowrP721jfW3lJmtEYe8ve0sL2ypi8yxlHZK0gYPm2Z7eKEWAh2PY118NeXgGdV2SVhFgjPcEU9BOxXrftySkHk5GXT%2FelDSyGMOxxAJT%2B%2B%2Bxpx8kw5Lj9vAY6pgG7IbHeUcR%2BYuHRsjPa5wGKLDtZB6j1ToFMki1BBNW15mUhX%2BCsOORutfWonIvupzoZH0ZMuoJn1M3Ln8skBNO%2FiGV0UQQyjAZyylESiAeg4VNQdI8YsQBa6QLtrkvpTehlfHH3pC1SeqwDR3VUmlVAmOBdTK4ErgyxMQpAIP5tg6j%2BXFU7GIz2FYSmQcjo6IrShxKH8loBUxnkpo9%2F2T16DCQlKF9x&X-Amz-Signature=ce8d25cf98d7c0e124818fd83262a170dce9f87547689cc1d3afc827b4438198&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ZA74G2A%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171241Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHJmMN6m50vZZ0GJbv3rVooQvZeASXNHQaterv8zMLYmAiA7xga7AXXKkIa6fzAt%2BT8jAYoM5bdPXcpIiphixsDscyqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMoQtHowVowavjbYTzKtwDrY%2BgnrZJsfEW6ydeZ0cw%2FUuxJjuRr7Ykp69tb73fGvdU8qXatr74kot0D2qQJphjYwYbhNAfQr4yRnB3AOHSj4N6dG243ASAeEJjC9paDGWlP2CJXHd%2BxesHxt5K4dMw2eOFXe8jDDeexo8QLuAvZETiSqaCDFh%2FR9ExN72WKsa6eHjLNrIrpR7BiLJ1Xvxo96igxbwwhT6ogxEeg%2FfYUcC%2FgjSD1R%2BI99EJ6Nj%2FfpkujrCFQ8CggmlUYCT9dp30cTXkedNs5sTUluScHQoNBACrDNZtOVeo9CsQNl6R0lLUpWNyl%2BNvgDREE%2FDzkFYoc6Eb3rj6ODSZhoHH%2B8Y47PRdlHs6FCBzyU6iJu9aecV0EiaFdl60gnlTxpAyBKnnyEOLmG0GaY9SYxp31acYyUOUA7%2BBwmNLCt%2Bz1ImHr%2Fw1c26uIZYLEANIIvpmZ74bwYdcp14vNeCAz2CfS7b%2FA3nx%2B3zw5%2B7xJPNppYqW1%2BuKMeRk4WuirrsDmnfulKJq1MnR%2FUfHm0KowrP721jfW3lJmtEYe8ve0sL2ypi8yxlHZK0gYPm2Z7eKEWAh2PY118NeXgGdV2SVhFgjPcEU9BOxXrftySkHk5GXT%2FelDSyGMOxxAJT%2B%2B%2Bxpx8kw5Lj9vAY6pgG7IbHeUcR%2BYuHRsjPa5wGKLDtZB6j1ToFMki1BBNW15mUhX%2BCsOORutfWonIvupzoZH0ZMuoJn1M3Ln8skBNO%2FiGV0UQQyjAZyylESiAeg4VNQdI8YsQBa6QLtrkvpTehlfHH3pC1SeqwDR3VUmlVAmOBdTK4ErgyxMQpAIP5tg6j%2BXFU7GIz2FYSmQcjo6IrShxKH8loBUxnkpo9%2F2T16DCQlKF9x&X-Amz-Signature=49d7568c3505376e9cadd7238282df0f01204311827eacb21b41881e7b16babc&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
