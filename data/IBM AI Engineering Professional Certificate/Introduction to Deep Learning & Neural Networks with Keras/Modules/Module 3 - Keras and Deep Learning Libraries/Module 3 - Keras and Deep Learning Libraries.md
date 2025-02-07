

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RNNF4EBE%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211313Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJGMEQCIFTUoUP7Jr1oBSRvyWxW6lIE1g41SU8tsG%2FUKi2xLNL7AiAH%2FupGl4HYAifWRQCfQKJx0jRLmzTt%2BiMALPFrdKEHfCr%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIMfmR1FFeRc3Ml201xKtwDTD8SUtNaqf345LJAKZAr1jnMRLNnqV1fHRmViv6gpWhhLpNGhmO0GB%2FjEyvISETLIg4W5Uwvsuvu5F5Xmg5OVS3zfCNDIPp4XLkfqom%2Fqa9eRT6YQmkqzakl%2BWj3hh0Ku7%2BfTnjADzMU0dLfr6UeAxEqbQqHj2mwu3NXeb6wcxUEEmQ7rK1TgQQSPM6dhzZFOeGC8kv8qcBb64gcGm82RAB242IEHdNFihpsSlIjPslKr5XtUjnaUxH7fQIFa%2FH2VsvLyumuRDLBBILEV99HhHG8NRToxLVdLvG8WI%2F75%2Fws7LAAi3JVj0TYO5mSyQB349CAc3OZBsHv5ikoSRybSBsHf5M85edhukuIeLoIDNTUHoJkqnyMKBYNWYygRvpd8Hdj12HYks8nphJJMVBBbIT9%2BS8Or4797gXYyhNAVVTLQIDUy0fL1pv0ervv0kuEPrS3XQ6J%2BPKKCn0yY9Lc1we6JCTq%2BPgOlkJMWdDC0TFLZmxGNMoGlFCYY6DWv%2FPiSay3k%2FPUZd23Lnw7%2BJKCTr7OB6xw9moZjnMNkiJXq7DI9LOrF9NqUQb%2F8eSZBU31VEXOjYY7vG%2FrHpZxST9zQJKfy0KKGehi7SRbkA1oGSe1gIdH8H7fz86Pb4ownNKZvQY6pgFZN%2Fr7aAIMTwqeJq%2F2ooaYDVZ%2B8Mz6BUnUVGDe77NyEFuhtWuT4%2Bj%2B%2F%2F5TMEvc39YsjFQyCSW7uq2%2BjoVniPPAyLK8aionZX39EI%2FOiRgyBcHj4wRPB3CpQYFWgj3QimzsXmSSbKfkdlnR0qUA07%2BWWPquWf%2FRZ7az98pfYDBPNngPqCjdzSWWkKWruRSpl6cUr%2FOgoTtTgZIt3hvTSstXciCCTcls&X-Amz-Signature=1b3fedaae0127a8785b146b2ff7bfa2953684358071c7619823126ca60b785c6&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RNNF4EBE%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211313Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJGMEQCIFTUoUP7Jr1oBSRvyWxW6lIE1g41SU8tsG%2FUKi2xLNL7AiAH%2FupGl4HYAifWRQCfQKJx0jRLmzTt%2BiMALPFrdKEHfCr%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIMfmR1FFeRc3Ml201xKtwDTD8SUtNaqf345LJAKZAr1jnMRLNnqV1fHRmViv6gpWhhLpNGhmO0GB%2FjEyvISETLIg4W5Uwvsuvu5F5Xmg5OVS3zfCNDIPp4XLkfqom%2Fqa9eRT6YQmkqzakl%2BWj3hh0Ku7%2BfTnjADzMU0dLfr6UeAxEqbQqHj2mwu3NXeb6wcxUEEmQ7rK1TgQQSPM6dhzZFOeGC8kv8qcBb64gcGm82RAB242IEHdNFihpsSlIjPslKr5XtUjnaUxH7fQIFa%2FH2VsvLyumuRDLBBILEV99HhHG8NRToxLVdLvG8WI%2F75%2Fws7LAAi3JVj0TYO5mSyQB349CAc3OZBsHv5ikoSRybSBsHf5M85edhukuIeLoIDNTUHoJkqnyMKBYNWYygRvpd8Hdj12HYks8nphJJMVBBbIT9%2BS8Or4797gXYyhNAVVTLQIDUy0fL1pv0ervv0kuEPrS3XQ6J%2BPKKCn0yY9Lc1we6JCTq%2BPgOlkJMWdDC0TFLZmxGNMoGlFCYY6DWv%2FPiSay3k%2FPUZd23Lnw7%2BJKCTr7OB6xw9moZjnMNkiJXq7DI9LOrF9NqUQb%2F8eSZBU31VEXOjYY7vG%2FrHpZxST9zQJKfy0KKGehi7SRbkA1oGSe1gIdH8H7fz86Pb4ownNKZvQY6pgFZN%2Fr7aAIMTwqeJq%2F2ooaYDVZ%2B8Mz6BUnUVGDe77NyEFuhtWuT4%2Bj%2B%2F%2F5TMEvc39YsjFQyCSW7uq2%2BjoVniPPAyLK8aionZX39EI%2FOiRgyBcHj4wRPB3CpQYFWgj3QimzsXmSSbKfkdlnR0qUA07%2BWWPquWf%2FRZ7az98pfYDBPNngPqCjdzSWWkKWruRSpl6cUr%2FOgoTtTgZIt3hvTSstXciCCTcls&X-Amz-Signature=bffafb7f20e93c5181cc5dbd8a658276a64460029d30c493107ad880d870795c&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RNNF4EBE%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211313Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJGMEQCIFTUoUP7Jr1oBSRvyWxW6lIE1g41SU8tsG%2FUKi2xLNL7AiAH%2FupGl4HYAifWRQCfQKJx0jRLmzTt%2BiMALPFrdKEHfCr%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIMfmR1FFeRc3Ml201xKtwDTD8SUtNaqf345LJAKZAr1jnMRLNnqV1fHRmViv6gpWhhLpNGhmO0GB%2FjEyvISETLIg4W5Uwvsuvu5F5Xmg5OVS3zfCNDIPp4XLkfqom%2Fqa9eRT6YQmkqzakl%2BWj3hh0Ku7%2BfTnjADzMU0dLfr6UeAxEqbQqHj2mwu3NXeb6wcxUEEmQ7rK1TgQQSPM6dhzZFOeGC8kv8qcBb64gcGm82RAB242IEHdNFihpsSlIjPslKr5XtUjnaUxH7fQIFa%2FH2VsvLyumuRDLBBILEV99HhHG8NRToxLVdLvG8WI%2F75%2Fws7LAAi3JVj0TYO5mSyQB349CAc3OZBsHv5ikoSRybSBsHf5M85edhukuIeLoIDNTUHoJkqnyMKBYNWYygRvpd8Hdj12HYks8nphJJMVBBbIT9%2BS8Or4797gXYyhNAVVTLQIDUy0fL1pv0ervv0kuEPrS3XQ6J%2BPKKCn0yY9Lc1we6JCTq%2BPgOlkJMWdDC0TFLZmxGNMoGlFCYY6DWv%2FPiSay3k%2FPUZd23Lnw7%2BJKCTr7OB6xw9moZjnMNkiJXq7DI9LOrF9NqUQb%2F8eSZBU31VEXOjYY7vG%2FrHpZxST9zQJKfy0KKGehi7SRbkA1oGSe1gIdH8H7fz86Pb4ownNKZvQY6pgFZN%2Fr7aAIMTwqeJq%2F2ooaYDVZ%2B8Mz6BUnUVGDe77NyEFuhtWuT4%2Bj%2B%2F%2F5TMEvc39YsjFQyCSW7uq2%2BjoVniPPAyLK8aionZX39EI%2FOiRgyBcHj4wRPB3CpQYFWgj3QimzsXmSSbKfkdlnR0qUA07%2BWWPquWf%2FRZ7az98pfYDBPNngPqCjdzSWWkKWruRSpl6cUr%2FOgoTtTgZIt3hvTSstXciCCTcls&X-Amz-Signature=e79975b5095da1844104654ed4cec94f3ddd430f83943694201047dbbedf4648&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VOHG6NTA%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211315Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIEkCezd5w7cBKvl8Ua%2FVupFj2QeKi1yqXJAfY8ks3HgTAiEAn2Brqdj47KKLJ2ALMvl22BxQ18fOBHZQU5o75C5piHwq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDJnvBxcjt1OQh%2FbdQCrcA4eFPCqyWT9lEU84PgFqNhM4xQH7Zdif5rsLOHwShuNdgv68RwJbPtwqcaTXlggyG8MQzIeXNKBnFrpInbMBndqQMCiEhp%2FxwB%2F0R5CdWp4NlUhIaIYcKH7z2ueeS7StWdAuYU2DahA7nvveBPp%2B2yc4pBA%2BpUzWrew5Qy6Cid06cdY3UZh5hcj4yggkDC2QSbsvi7EpujvxQfpAYkm1PEFYZkPslqQTac0jXFCHauxnnZlmA%2FS1pasV3Ad4%2BaYGdtR%2BmlSdKEsh4s%2BtvYtxhM6NjvCCi54%2BY3lICh4JP0%2BTHf5PO4FkiSyAn0SSN9tDWUAPyBN%2BUHUfhzQUAM1PvO%2BFIzhEFzNo%2BSu0Q64DV8iIK%2Bk11rOVZhV%2BPp69UQpvZk2JSG%2FJnkB%2FP1iic%2FkeZpM%2B7YpFuqAhzR%2B2sU223ot1nAgqDDl0XJVRa%2Fvk%2Fu9hViHdLIAgjef71gmuvcPiJOVhgLNagIh8q054oNIj2htvGJEZyHOFQD6s1mhowh4PGrbCaRJIUDLYFw1aT0Uy9EJQSq3ElIUR1Cp2%2B04b6hgNwSUARKhkK4bglg%2F83F%2FU3kFax%2FIM3DcRwVRISOHaJqLck253fduwAewdvPuCQnOOTjmRmyzJnUeJ7BhZMMTSmb0GOqUBEAF%2Fr%2B1RvJodEjFL%2FdD1lpMx60FscoP4wgPi4BQL8rLYi2EIN1KfhFVlsiXAJdG3UFyvleOW9K%2FomJS2JnZlyfb4jARMsQYn10PAGfpzWRaQY8ick2lgF6tFQl85ij67yQgsoh71tJZ7rd5j4E6kbXW5Rc40sLgifuaBXTta8%2FGeL04bxTLBaxJQhEbtuSicfeQ4OW%2FzIYGKnQPKwD9pO6RGr895&X-Amz-Signature=418b9045486d66cb0295cb8135fdb83080a1e4a55b43019084828940b2f4eb43&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QUCCD3QU%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIQCZUWpM10vDwpGE46ODcxJ%2FFx5a2GujND1sWnjiqJYHZAIgN7fc4tUEplwtoKucH04xZYdpne8NoA%2F75GTRQsngV%2Bwq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDIBUpZXlK1P85wX9TyrcA%2FQDRVvH3AXiPCrM4Ktz%2F7%2Bdqmk%2F7H3jStSN44xzHkgilzVgM6%2B0QGMkELBBUjCw%2FZuan2B09RDPS1Htb%2Fu6wiNxBYynOgQayePyXWXAutrtTAle%2BklsgT4LCZT6lYdlxQoxfvbSvTwdL0RjGWhG0unAVWYIaarGtHKZpdFXsyNRVmoNi7ZXpcB5Tm8939QTIQvAsbcalHN%2FTnduJKH3RE3jW%2FXo3l%2B%2FSXYeiE719OO5OOuDfPLCzkFCsDDT4r8j74%2FHJT6ya9SStBvaBy%2FKqYOoK07x5OtRJpX88CCKYdJvtMd11LGK%2FHJ1aOedehWK8%2FLvaB8K9QExAEej3mmOKhoaM8eo%2BQnrWthucPPBj4VihsMV67Rl9Sx01JkHR%2F3QdiJBaL%2FcSfoR09lXOgqmUKRNl%2BLwTKPnvARKMzm4l7XF2C73cSyWv8He7OOvbSZVPuMbkbBFwoIGB%2Bf%2BJQsewHotmaSaQTzNAFAn8PlcUH%2FhiOSxByH2OMvhj12JSI0njWgFv1kxz991r16F9Sld0qQzSLX8vR2B1dqIYE58W3sbNRccmLUsE8qpbbw%2Fyhf1NPfRFI5WMBotkwm8FpX%2B6du6nj0IuQAgg0LKH%2FZOb4DEA%2BIAUzPsxcCnNGmCMKLTmb0GOqUBS3G%2FkFldqrnFkuZdFvuA11nymeduEPS%2B%2BCfiMG1mHu6sWHYHOvtn%2BagyMNGqBBUIzYeSBj8%2FN7Y0vM%2FjEFAU54T2Ui5H%2F8CHqZwiqpBiOqHNvynzN8GyMNRHCkejmrG%2BG9MLoVyDj%2FG2tNAUhNcuz%2FWOCFMwctWtVQt1yccgDHgO%2BblMB%2Bo0BKdgxGYzFcfiCTSi2XxRETbTLmqM9FJ%2BNS64I%2FOh&X-Amz-Signature=7a5eb049f7cdf5bcc1b4aea7c3835db5fc67fdc00f308051f468676c7a7fc452&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RNNF4EBE%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211313Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJGMEQCIFTUoUP7Jr1oBSRvyWxW6lIE1g41SU8tsG%2FUKi2xLNL7AiAH%2FupGl4HYAifWRQCfQKJx0jRLmzTt%2BiMALPFrdKEHfCr%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIMfmR1FFeRc3Ml201xKtwDTD8SUtNaqf345LJAKZAr1jnMRLNnqV1fHRmViv6gpWhhLpNGhmO0GB%2FjEyvISETLIg4W5Uwvsuvu5F5Xmg5OVS3zfCNDIPp4XLkfqom%2Fqa9eRT6YQmkqzakl%2BWj3hh0Ku7%2BfTnjADzMU0dLfr6UeAxEqbQqHj2mwu3NXeb6wcxUEEmQ7rK1TgQQSPM6dhzZFOeGC8kv8qcBb64gcGm82RAB242IEHdNFihpsSlIjPslKr5XtUjnaUxH7fQIFa%2FH2VsvLyumuRDLBBILEV99HhHG8NRToxLVdLvG8WI%2F75%2Fws7LAAi3JVj0TYO5mSyQB349CAc3OZBsHv5ikoSRybSBsHf5M85edhukuIeLoIDNTUHoJkqnyMKBYNWYygRvpd8Hdj12HYks8nphJJMVBBbIT9%2BS8Or4797gXYyhNAVVTLQIDUy0fL1pv0ervv0kuEPrS3XQ6J%2BPKKCn0yY9Lc1we6JCTq%2BPgOlkJMWdDC0TFLZmxGNMoGlFCYY6DWv%2FPiSay3k%2FPUZd23Lnw7%2BJKCTr7OB6xw9moZjnMNkiJXq7DI9LOrF9NqUQb%2F8eSZBU31VEXOjYY7vG%2FrHpZxST9zQJKfy0KKGehi7SRbkA1oGSe1gIdH8H7fz86Pb4ownNKZvQY6pgFZN%2Fr7aAIMTwqeJq%2F2ooaYDVZ%2B8Mz6BUnUVGDe77NyEFuhtWuT4%2Bj%2B%2F%2F5TMEvc39YsjFQyCSW7uq2%2BjoVniPPAyLK8aionZX39EI%2FOiRgyBcHj4wRPB3CpQYFWgj3QimzsXmSSbKfkdlnR0qUA07%2BWWPquWf%2FRZ7az98pfYDBPNngPqCjdzSWWkKWruRSpl6cUr%2FOgoTtTgZIt3hvTSstXciCCTcls&X-Amz-Signature=e8c5f3e09324fa7e96fef7e0a82250a1f6ed7805e1b2baee27bf0765e6eb82b6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RNNF4EBE%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211313Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJGMEQCIFTUoUP7Jr1oBSRvyWxW6lIE1g41SU8tsG%2FUKi2xLNL7AiAH%2FupGl4HYAifWRQCfQKJx0jRLmzTt%2BiMALPFrdKEHfCr%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIMfmR1FFeRc3Ml201xKtwDTD8SUtNaqf345LJAKZAr1jnMRLNnqV1fHRmViv6gpWhhLpNGhmO0GB%2FjEyvISETLIg4W5Uwvsuvu5F5Xmg5OVS3zfCNDIPp4XLkfqom%2Fqa9eRT6YQmkqzakl%2BWj3hh0Ku7%2BfTnjADzMU0dLfr6UeAxEqbQqHj2mwu3NXeb6wcxUEEmQ7rK1TgQQSPM6dhzZFOeGC8kv8qcBb64gcGm82RAB242IEHdNFihpsSlIjPslKr5XtUjnaUxH7fQIFa%2FH2VsvLyumuRDLBBILEV99HhHG8NRToxLVdLvG8WI%2F75%2Fws7LAAi3JVj0TYO5mSyQB349CAc3OZBsHv5ikoSRybSBsHf5M85edhukuIeLoIDNTUHoJkqnyMKBYNWYygRvpd8Hdj12HYks8nphJJMVBBbIT9%2BS8Or4797gXYyhNAVVTLQIDUy0fL1pv0ervv0kuEPrS3XQ6J%2BPKKCn0yY9Lc1we6JCTq%2BPgOlkJMWdDC0TFLZmxGNMoGlFCYY6DWv%2FPiSay3k%2FPUZd23Lnw7%2BJKCTr7OB6xw9moZjnMNkiJXq7DI9LOrF9NqUQb%2F8eSZBU31VEXOjYY7vG%2FrHpZxST9zQJKfy0KKGehi7SRbkA1oGSe1gIdH8H7fz86Pb4ownNKZvQY6pgFZN%2Fr7aAIMTwqeJq%2F2ooaYDVZ%2B8Mz6BUnUVGDe77NyEFuhtWuT4%2Bj%2B%2F%2F5TMEvc39YsjFQyCSW7uq2%2BjoVniPPAyLK8aionZX39EI%2FOiRgyBcHj4wRPB3CpQYFWgj3QimzsXmSSbKfkdlnR0qUA07%2BWWPquWf%2FRZ7az98pfYDBPNngPqCjdzSWWkKWruRSpl6cUr%2FOgoTtTgZIt3hvTSstXciCCTcls&X-Amz-Signature=bdc25d5c1996a56e7cbd99f17f1b8db053b5e3935eb49e1f0acdcbc4490e27ee&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RNNF4EBE%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211313Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJGMEQCIFTUoUP7Jr1oBSRvyWxW6lIE1g41SU8tsG%2FUKi2xLNL7AiAH%2FupGl4HYAifWRQCfQKJx0jRLmzTt%2BiMALPFrdKEHfCr%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIMfmR1FFeRc3Ml201xKtwDTD8SUtNaqf345LJAKZAr1jnMRLNnqV1fHRmViv6gpWhhLpNGhmO0GB%2FjEyvISETLIg4W5Uwvsuvu5F5Xmg5OVS3zfCNDIPp4XLkfqom%2Fqa9eRT6YQmkqzakl%2BWj3hh0Ku7%2BfTnjADzMU0dLfr6UeAxEqbQqHj2mwu3NXeb6wcxUEEmQ7rK1TgQQSPM6dhzZFOeGC8kv8qcBb64gcGm82RAB242IEHdNFihpsSlIjPslKr5XtUjnaUxH7fQIFa%2FH2VsvLyumuRDLBBILEV99HhHG8NRToxLVdLvG8WI%2F75%2Fws7LAAi3JVj0TYO5mSyQB349CAc3OZBsHv5ikoSRybSBsHf5M85edhukuIeLoIDNTUHoJkqnyMKBYNWYygRvpd8Hdj12HYks8nphJJMVBBbIT9%2BS8Or4797gXYyhNAVVTLQIDUy0fL1pv0ervv0kuEPrS3XQ6J%2BPKKCn0yY9Lc1we6JCTq%2BPgOlkJMWdDC0TFLZmxGNMoGlFCYY6DWv%2FPiSay3k%2FPUZd23Lnw7%2BJKCTr7OB6xw9moZjnMNkiJXq7DI9LOrF9NqUQb%2F8eSZBU31VEXOjYY7vG%2FrHpZxST9zQJKfy0KKGehi7SRbkA1oGSe1gIdH8H7fz86Pb4ownNKZvQY6pgFZN%2Fr7aAIMTwqeJq%2F2ooaYDVZ%2B8Mz6BUnUVGDe77NyEFuhtWuT4%2Bj%2B%2F%2F5TMEvc39YsjFQyCSW7uq2%2BjoVniPPAyLK8aionZX39EI%2FOiRgyBcHj4wRPB3CpQYFWgj3QimzsXmSSbKfkdlnR0qUA07%2BWWPquWf%2FRZ7az98pfYDBPNngPqCjdzSWWkKWruRSpl6cUr%2FOgoTtTgZIt3hvTSstXciCCTcls&X-Amz-Signature=9949eda91b6c237ec42ce07bc9006b20c57831a9377f53d4cf2b4df4884d9d5f&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RNNF4EBE%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211313Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJGMEQCIFTUoUP7Jr1oBSRvyWxW6lIE1g41SU8tsG%2FUKi2xLNL7AiAH%2FupGl4HYAifWRQCfQKJx0jRLmzTt%2BiMALPFrdKEHfCr%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIMfmR1FFeRc3Ml201xKtwDTD8SUtNaqf345LJAKZAr1jnMRLNnqV1fHRmViv6gpWhhLpNGhmO0GB%2FjEyvISETLIg4W5Uwvsuvu5F5Xmg5OVS3zfCNDIPp4XLkfqom%2Fqa9eRT6YQmkqzakl%2BWj3hh0Ku7%2BfTnjADzMU0dLfr6UeAxEqbQqHj2mwu3NXeb6wcxUEEmQ7rK1TgQQSPM6dhzZFOeGC8kv8qcBb64gcGm82RAB242IEHdNFihpsSlIjPslKr5XtUjnaUxH7fQIFa%2FH2VsvLyumuRDLBBILEV99HhHG8NRToxLVdLvG8WI%2F75%2Fws7LAAi3JVj0TYO5mSyQB349CAc3OZBsHv5ikoSRybSBsHf5M85edhukuIeLoIDNTUHoJkqnyMKBYNWYygRvpd8Hdj12HYks8nphJJMVBBbIT9%2BS8Or4797gXYyhNAVVTLQIDUy0fL1pv0ervv0kuEPrS3XQ6J%2BPKKCn0yY9Lc1we6JCTq%2BPgOlkJMWdDC0TFLZmxGNMoGlFCYY6DWv%2FPiSay3k%2FPUZd23Lnw7%2BJKCTr7OB6xw9moZjnMNkiJXq7DI9LOrF9NqUQb%2F8eSZBU31VEXOjYY7vG%2FrHpZxST9zQJKfy0KKGehi7SRbkA1oGSe1gIdH8H7fz86Pb4ownNKZvQY6pgFZN%2Fr7aAIMTwqeJq%2F2ooaYDVZ%2B8Mz6BUnUVGDe77NyEFuhtWuT4%2Bj%2B%2F%2F5TMEvc39YsjFQyCSW7uq2%2BjoVniPPAyLK8aionZX39EI%2FOiRgyBcHj4wRPB3CpQYFWgj3QimzsXmSSbKfkdlnR0qUA07%2BWWPquWf%2FRZ7az98pfYDBPNngPqCjdzSWWkKWruRSpl6cUr%2FOgoTtTgZIt3hvTSstXciCCTcls&X-Amz-Signature=a8f40a68f9b0c883bfcbd7c49a8506b8fe0214a487eebfb97a6ce274370ce777&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
