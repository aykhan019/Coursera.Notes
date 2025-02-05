

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TKRVSE2M%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJHMEUCIG4EJSqbaaSEApFz49%2B02BBguX5fEMdChezDhpx4FBjyAiEAz06%2B7bbZtIZIdtVRzHdCWsASHd93n%2BfhA5KnX5mjFZQq%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDCmJOE0B0vcEtLX0bCrcAxuuB3enae%2FaK56SplCCxQtgJAfyT4CUNQ5fADu7ETuuZWQrsl84PE%2BhIvTBG5JvkIwn0JKOJzKHvfd8bIZ8VNFt%2FWDQqmgfAk6pBiXNLMG6YzSsm1HK7OmM1uavrF3xvw01O47LIGxPTtrLY%2F8rnHon5Jz6jfK5uEdf6HbsHCY0kDuMljGurAw5Ixm4i7iSiwkyWCYqhQmO94YoDwioglLfb8jj%2ByoFiJ4r1i8%2BZszSSJtkrCSp1hfSN5VImc84ddEpXA7EVDBG62e6q4TJB7wB8XKwfOj7YmZhToAA5ksLIaGarDiPwaVBzhLhfVsRjnIGaZhm44TkVzW5B9%2FhlYClvEvdAq%2Bw3%2BsktUa%2FOuxNeYTDj2NEZElhIirNzeM2tctwjy16WHEEg6ZBzEjeNhPHjAkFhFMHiROJE8CeDE%2B7OsL8JtQRK5tRdJVYgqk7cb1mdvFrGU%2BZbLaqq%2F4zJ8dsaIbKO%2BTz9z5JGuDPOUlLFr0JUzDoNjBGNC08EV8QDbGezzUYOwqROpnMTG8Dondjh0gFKY%2FOO20kTHPH8YHArL811Zr6YyOj%2BSllEWXo%2BmR4Waziuc%2FGjms6mFjZ2IaBgYFP8JDD3aZ3yB2n0%2FnR6sfulrbjYFxyLsaVMOmdjr0GOqUB7NkX0k6%2FpneGkVrYZD2kLtVXsAkBTJ5AG2cKomN6gGHzKjrxq4pqaJE7PwjGbjoalOVgAiVhuq%2FyjUpL1fJt%2B0Gdx%2BvwSK9mdR1C0zbRjEixLKPpD3HCaLpl%2FdDjeHUEI9zWi86OoQzSDImcK4Yj1pQrn2xre2i41kiwRxvFJoStONhOwuwbMrB4M4kh6dKZ3eBFv%2BIyYZlE7DWOA%2BuUmDu65U5%2B&X-Amz-Signature=10dec6466c17c7560581620cb18a76e1895ff78adb82db49da789fd3546c6c42&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TKRVSE2M%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJHMEUCIG4EJSqbaaSEApFz49%2B02BBguX5fEMdChezDhpx4FBjyAiEAz06%2B7bbZtIZIdtVRzHdCWsASHd93n%2BfhA5KnX5mjFZQq%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDCmJOE0B0vcEtLX0bCrcAxuuB3enae%2FaK56SplCCxQtgJAfyT4CUNQ5fADu7ETuuZWQrsl84PE%2BhIvTBG5JvkIwn0JKOJzKHvfd8bIZ8VNFt%2FWDQqmgfAk6pBiXNLMG6YzSsm1HK7OmM1uavrF3xvw01O47LIGxPTtrLY%2F8rnHon5Jz6jfK5uEdf6HbsHCY0kDuMljGurAw5Ixm4i7iSiwkyWCYqhQmO94YoDwioglLfb8jj%2ByoFiJ4r1i8%2BZszSSJtkrCSp1hfSN5VImc84ddEpXA7EVDBG62e6q4TJB7wB8XKwfOj7YmZhToAA5ksLIaGarDiPwaVBzhLhfVsRjnIGaZhm44TkVzW5B9%2FhlYClvEvdAq%2Bw3%2BsktUa%2FOuxNeYTDj2NEZElhIirNzeM2tctwjy16WHEEg6ZBzEjeNhPHjAkFhFMHiROJE8CeDE%2B7OsL8JtQRK5tRdJVYgqk7cb1mdvFrGU%2BZbLaqq%2F4zJ8dsaIbKO%2BTz9z5JGuDPOUlLFr0JUzDoNjBGNC08EV8QDbGezzUYOwqROpnMTG8Dondjh0gFKY%2FOO20kTHPH8YHArL811Zr6YyOj%2BSllEWXo%2BmR4Waziuc%2FGjms6mFjZ2IaBgYFP8JDD3aZ3yB2n0%2FnR6sfulrbjYFxyLsaVMOmdjr0GOqUB7NkX0k6%2FpneGkVrYZD2kLtVXsAkBTJ5AG2cKomN6gGHzKjrxq4pqaJE7PwjGbjoalOVgAiVhuq%2FyjUpL1fJt%2B0Gdx%2BvwSK9mdR1C0zbRjEixLKPpD3HCaLpl%2FdDjeHUEI9zWi86OoQzSDImcK4Yj1pQrn2xre2i41kiwRxvFJoStONhOwuwbMrB4M4kh6dKZ3eBFv%2BIyYZlE7DWOA%2BuUmDu65U5%2B&X-Amz-Signature=cd1d79acb38a937d85a6ba6def42f72e4497f14dd7836c199f6d6aa67125aa4e&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TKRVSE2M%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJHMEUCIG4EJSqbaaSEApFz49%2B02BBguX5fEMdChezDhpx4FBjyAiEAz06%2B7bbZtIZIdtVRzHdCWsASHd93n%2BfhA5KnX5mjFZQq%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDCmJOE0B0vcEtLX0bCrcAxuuB3enae%2FaK56SplCCxQtgJAfyT4CUNQ5fADu7ETuuZWQrsl84PE%2BhIvTBG5JvkIwn0JKOJzKHvfd8bIZ8VNFt%2FWDQqmgfAk6pBiXNLMG6YzSsm1HK7OmM1uavrF3xvw01O47LIGxPTtrLY%2F8rnHon5Jz6jfK5uEdf6HbsHCY0kDuMljGurAw5Ixm4i7iSiwkyWCYqhQmO94YoDwioglLfb8jj%2ByoFiJ4r1i8%2BZszSSJtkrCSp1hfSN5VImc84ddEpXA7EVDBG62e6q4TJB7wB8XKwfOj7YmZhToAA5ksLIaGarDiPwaVBzhLhfVsRjnIGaZhm44TkVzW5B9%2FhlYClvEvdAq%2Bw3%2BsktUa%2FOuxNeYTDj2NEZElhIirNzeM2tctwjy16WHEEg6ZBzEjeNhPHjAkFhFMHiROJE8CeDE%2B7OsL8JtQRK5tRdJVYgqk7cb1mdvFrGU%2BZbLaqq%2F4zJ8dsaIbKO%2BTz9z5JGuDPOUlLFr0JUzDoNjBGNC08EV8QDbGezzUYOwqROpnMTG8Dondjh0gFKY%2FOO20kTHPH8YHArL811Zr6YyOj%2BSllEWXo%2BmR4Waziuc%2FGjms6mFjZ2IaBgYFP8JDD3aZ3yB2n0%2FnR6sfulrbjYFxyLsaVMOmdjr0GOqUB7NkX0k6%2FpneGkVrYZD2kLtVXsAkBTJ5AG2cKomN6gGHzKjrxq4pqaJE7PwjGbjoalOVgAiVhuq%2FyjUpL1fJt%2B0Gdx%2BvwSK9mdR1C0zbRjEixLKPpD3HCaLpl%2FdDjeHUEI9zWi86OoQzSDImcK4Yj1pQrn2xre2i41kiwRxvFJoStONhOwuwbMrB4M4kh6dKZ3eBFv%2BIyYZlE7DWOA%2BuUmDu65U5%2B&X-Amz-Signature=88415d38aa498b68f87cf206a013d40b498dd74251dbf50a8bd172d6320c4d09&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XS74ZA5I%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJHMEUCIAl3%2BJa8trzhzZD61qGrdcg%2Ff20xQKaEecmh3auFE%2B2qAiEAuAWsudc%2BNw7o2bf4Cd68J%2F8EPP5ONf9IIpSSd%2BZQpw8q%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDI3PW2GFzp3bu5vckyrcAzAe%2FPhapjhjD%2FAZNwS%2BgJG3fJWpUWvtiiAZMm%2F7Rl7j8mkbU0GtxUKi%2BEsj1aeMtHC0eEXP9hDXs8JjjveabEr7ag%2B6SVk29BdY6hH2Tl2hGemNLBcN4e3Pqo%2Fno%2FnEB0PblkMX8u0oRNhgMWMjMBYZyTenKpCr5sIhUd2ecimcZqxsJspzUxaicnComYwGAlioGpFgvf6W0QWMnmOlxLYnX2L%2BMR2uatL1hgO2sP7c9i4imqx1ylpceDIjiF6fLeu0iwMtH7RA6hnSDPlfyQGsu4Oz7j%2Fi9xY7eWSbxsnDDSk3vCUrr3Ma9ikwxWwfxxxjE1AYgqtTc6vWGHAfZpa30K1u42vtp4G7PFbJAYglAjZxqXXi2jNi3FkXgw2ygFUC5ta0dHOQyHSKJWg%2FqN%2ByODTmjjpjdA0QQeGOjUmIWkzgI%2BIrzNMu6sTNyl3ZJCzONElXt9HjbcwC2vhDLT4VQM7Utd9GHCjs0KdaYf1BCyQr5ASVG2pch4IhQE%2FIRdbWOVxwHJAsiDf%2FlpDB7fEmwGXo1BNN%2FzqNNQsPQk%2FbIMUzQyy4eobrF%2FzG4eey%2B7REzzmlxvwv3AiLVUq9Wq%2FAMuOL0IYJ4LAwnfpbSIu%2FmaRN9MGufkTMNDQSMJ2djr0GOqUB%2BL4BF5zJ3vzZRELFYXi2in8w6pyVyrKKqpGaEi5Y0LJjjg03M1EQ1GBTe4GrusHmOLDlxj6u2uXhdxIJnomPn2v1GDY4g4LEPcHWUycNqK8%2Fx7xGNBBw05N3qmZQeVh9pX7ILVAbZub%2FgMhrjwcWT8krBox0bLYnjBTp3pGc5dRhmZQkqdbmQnZ%2F4b38UICxUztNEwl1V1Iwow5B4zxFF%2B8C6SoK&X-Amz-Signature=86e3348b2ccc7c53efaf6a4c9e8f9992436aa61ecd1e6e966651e4920101993c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WP2U3D4S%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJHMEUCIAyVAEaafgizQN%2B1BWNIg5qk%2FL3DlzExsKu294y2HgKjAiEAsmJ8o8mo%2B2G4baKyO%2BJYeAzLc5aku7Wa80q5NhUSEOYq%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDGl2yWWO7N6%2B%2BbE81SrcA%2FanHoXAaCk8kgZQFQQ2107puEKXdZ2VfOxK9VyC%2BNFGIqy5nLoEvUCYeerPrqrJotzzZsk2TzYcTweUSZ0GcgivXKQuWof%2F7VP1K3EkEk4XYCyZiEiHEwiTZjffHSmDvb47w%2BMIM%2FCTfhbkNDiYtFhVj3D48qKGx19xKvtfGyAsWAeL9BCb4ubFvox0%2FOjLgJ6lLIYN9bIsd8VlsdkNS7aC%2BXd8KBAU2VlG5eBW9jd6tpirpnU4bhenvBLcJIrt3Cj49N5H47qQ5jtn3qsLC%2BlWOktpOXkyKhO9IETFsWMT7YPKGB2hkgMRw9VXxiwa%2BBfP9XXwrVS9yRpICr1vE7P1yhNzhCLE8EFpJE5WdZTNNxpkleNUjJ%2FjAXkh%2BpI5AsfMGI9Rd8hJ1vkxRJMEtQyQ0aoukDvwFPCRdWJsDMG2ANeOJxmDCZM4Xex1d5BXJJ71gCR77RM6bWS5KwTj49fEHn43iHlR%2BE5C7il0CXrQ4uhRVHH8eCx70fLPQnHbc9KYSibpB4XzefkePEtoRouyTF%2FL4wFSWNXvPiIrkJEC%2F8x2e0%2BeiyhB9UOSP296AJQSy%2BQQUMUAu9smotsBoKaW4NeWVHf8fVJ6SPkpDWeUHzl3wEzQIE0zMcjIMOadjr0GOqUBuaeP4To9IiwuHaPCGsfCVwvssV%2B4td3EO9DLhiuv0zgyUTR7fxTfHWLTWV4vW0ejPB1MGlPEGZoOwIxY3xbAI8X%2FSz%2FLILAj4Z49eou7DuchyyY3ZoAUHgoC0bNhBTyhb806Zsog4IX9ZcKmvFi9jlrwMpUMT2TXbhm5bMCiTFTQ3fYjc9ZfXGbrdQeacresaKki3n6FlHwxnoAgG7asYEA5bzTp&X-Amz-Signature=55b186c36500226e33533ec9d0147a9529cb8c55f85b7a8d6c597637bb738b6e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TKRVSE2M%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJHMEUCIG4EJSqbaaSEApFz49%2B02BBguX5fEMdChezDhpx4FBjyAiEAz06%2B7bbZtIZIdtVRzHdCWsASHd93n%2BfhA5KnX5mjFZQq%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDCmJOE0B0vcEtLX0bCrcAxuuB3enae%2FaK56SplCCxQtgJAfyT4CUNQ5fADu7ETuuZWQrsl84PE%2BhIvTBG5JvkIwn0JKOJzKHvfd8bIZ8VNFt%2FWDQqmgfAk6pBiXNLMG6YzSsm1HK7OmM1uavrF3xvw01O47LIGxPTtrLY%2F8rnHon5Jz6jfK5uEdf6HbsHCY0kDuMljGurAw5Ixm4i7iSiwkyWCYqhQmO94YoDwioglLfb8jj%2ByoFiJ4r1i8%2BZszSSJtkrCSp1hfSN5VImc84ddEpXA7EVDBG62e6q4TJB7wB8XKwfOj7YmZhToAA5ksLIaGarDiPwaVBzhLhfVsRjnIGaZhm44TkVzW5B9%2FhlYClvEvdAq%2Bw3%2BsktUa%2FOuxNeYTDj2NEZElhIirNzeM2tctwjy16WHEEg6ZBzEjeNhPHjAkFhFMHiROJE8CeDE%2B7OsL8JtQRK5tRdJVYgqk7cb1mdvFrGU%2BZbLaqq%2F4zJ8dsaIbKO%2BTz9z5JGuDPOUlLFr0JUzDoNjBGNC08EV8QDbGezzUYOwqROpnMTG8Dondjh0gFKY%2FOO20kTHPH8YHArL811Zr6YyOj%2BSllEWXo%2BmR4Waziuc%2FGjms6mFjZ2IaBgYFP8JDD3aZ3yB2n0%2FnR6sfulrbjYFxyLsaVMOmdjr0GOqUB7NkX0k6%2FpneGkVrYZD2kLtVXsAkBTJ5AG2cKomN6gGHzKjrxq4pqaJE7PwjGbjoalOVgAiVhuq%2FyjUpL1fJt%2B0Gdx%2BvwSK9mdR1C0zbRjEixLKPpD3HCaLpl%2FdDjeHUEI9zWi86OoQzSDImcK4Yj1pQrn2xre2i41kiwRxvFJoStONhOwuwbMrB4M4kh6dKZ3eBFv%2BIyYZlE7DWOA%2BuUmDu65U5%2B&X-Amz-Signature=856d1b5eb127ae370a188f7fceb82f023512ee80beabbf1286de1b10961a3708&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TKRVSE2M%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJHMEUCIG4EJSqbaaSEApFz49%2B02BBguX5fEMdChezDhpx4FBjyAiEAz06%2B7bbZtIZIdtVRzHdCWsASHd93n%2BfhA5KnX5mjFZQq%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDCmJOE0B0vcEtLX0bCrcAxuuB3enae%2FaK56SplCCxQtgJAfyT4CUNQ5fADu7ETuuZWQrsl84PE%2BhIvTBG5JvkIwn0JKOJzKHvfd8bIZ8VNFt%2FWDQqmgfAk6pBiXNLMG6YzSsm1HK7OmM1uavrF3xvw01O47LIGxPTtrLY%2F8rnHon5Jz6jfK5uEdf6HbsHCY0kDuMljGurAw5Ixm4i7iSiwkyWCYqhQmO94YoDwioglLfb8jj%2ByoFiJ4r1i8%2BZszSSJtkrCSp1hfSN5VImc84ddEpXA7EVDBG62e6q4TJB7wB8XKwfOj7YmZhToAA5ksLIaGarDiPwaVBzhLhfVsRjnIGaZhm44TkVzW5B9%2FhlYClvEvdAq%2Bw3%2BsktUa%2FOuxNeYTDj2NEZElhIirNzeM2tctwjy16WHEEg6ZBzEjeNhPHjAkFhFMHiROJE8CeDE%2B7OsL8JtQRK5tRdJVYgqk7cb1mdvFrGU%2BZbLaqq%2F4zJ8dsaIbKO%2BTz9z5JGuDPOUlLFr0JUzDoNjBGNC08EV8QDbGezzUYOwqROpnMTG8Dondjh0gFKY%2FOO20kTHPH8YHArL811Zr6YyOj%2BSllEWXo%2BmR4Waziuc%2FGjms6mFjZ2IaBgYFP8JDD3aZ3yB2n0%2FnR6sfulrbjYFxyLsaVMOmdjr0GOqUB7NkX0k6%2FpneGkVrYZD2kLtVXsAkBTJ5AG2cKomN6gGHzKjrxq4pqaJE7PwjGbjoalOVgAiVhuq%2FyjUpL1fJt%2B0Gdx%2BvwSK9mdR1C0zbRjEixLKPpD3HCaLpl%2FdDjeHUEI9zWi86OoQzSDImcK4Yj1pQrn2xre2i41kiwRxvFJoStONhOwuwbMrB4M4kh6dKZ3eBFv%2BIyYZlE7DWOA%2BuUmDu65U5%2B&X-Amz-Signature=a33b11a44ab69bf4fc199a09e63743340b93f95df853ee3152734e1d23a1a281&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TKRVSE2M%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJHMEUCIG4EJSqbaaSEApFz49%2B02BBguX5fEMdChezDhpx4FBjyAiEAz06%2B7bbZtIZIdtVRzHdCWsASHd93n%2BfhA5KnX5mjFZQq%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDCmJOE0B0vcEtLX0bCrcAxuuB3enae%2FaK56SplCCxQtgJAfyT4CUNQ5fADu7ETuuZWQrsl84PE%2BhIvTBG5JvkIwn0JKOJzKHvfd8bIZ8VNFt%2FWDQqmgfAk6pBiXNLMG6YzSsm1HK7OmM1uavrF3xvw01O47LIGxPTtrLY%2F8rnHon5Jz6jfK5uEdf6HbsHCY0kDuMljGurAw5Ixm4i7iSiwkyWCYqhQmO94YoDwioglLfb8jj%2ByoFiJ4r1i8%2BZszSSJtkrCSp1hfSN5VImc84ddEpXA7EVDBG62e6q4TJB7wB8XKwfOj7YmZhToAA5ksLIaGarDiPwaVBzhLhfVsRjnIGaZhm44TkVzW5B9%2FhlYClvEvdAq%2Bw3%2BsktUa%2FOuxNeYTDj2NEZElhIirNzeM2tctwjy16WHEEg6ZBzEjeNhPHjAkFhFMHiROJE8CeDE%2B7OsL8JtQRK5tRdJVYgqk7cb1mdvFrGU%2BZbLaqq%2F4zJ8dsaIbKO%2BTz9z5JGuDPOUlLFr0JUzDoNjBGNC08EV8QDbGezzUYOwqROpnMTG8Dondjh0gFKY%2FOO20kTHPH8YHArL811Zr6YyOj%2BSllEWXo%2BmR4Waziuc%2FGjms6mFjZ2IaBgYFP8JDD3aZ3yB2n0%2FnR6sfulrbjYFxyLsaVMOmdjr0GOqUB7NkX0k6%2FpneGkVrYZD2kLtVXsAkBTJ5AG2cKomN6gGHzKjrxq4pqaJE7PwjGbjoalOVgAiVhuq%2FyjUpL1fJt%2B0Gdx%2BvwSK9mdR1C0zbRjEixLKPpD3HCaLpl%2FdDjeHUEI9zWi86OoQzSDImcK4Yj1pQrn2xre2i41kiwRxvFJoStONhOwuwbMrB4M4kh6dKZ3eBFv%2BIyYZlE7DWOA%2BuUmDu65U5%2B&X-Amz-Signature=c8803f4597d4c2252e79193c0e1a58fd1040dbec9aeaee4ed4fe25dc6170dfc4&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TKRVSE2M%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJHMEUCIG4EJSqbaaSEApFz49%2B02BBguX5fEMdChezDhpx4FBjyAiEAz06%2B7bbZtIZIdtVRzHdCWsASHd93n%2BfhA5KnX5mjFZQq%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDCmJOE0B0vcEtLX0bCrcAxuuB3enae%2FaK56SplCCxQtgJAfyT4CUNQ5fADu7ETuuZWQrsl84PE%2BhIvTBG5JvkIwn0JKOJzKHvfd8bIZ8VNFt%2FWDQqmgfAk6pBiXNLMG6YzSsm1HK7OmM1uavrF3xvw01O47LIGxPTtrLY%2F8rnHon5Jz6jfK5uEdf6HbsHCY0kDuMljGurAw5Ixm4i7iSiwkyWCYqhQmO94YoDwioglLfb8jj%2ByoFiJ4r1i8%2BZszSSJtkrCSp1hfSN5VImc84ddEpXA7EVDBG62e6q4TJB7wB8XKwfOj7YmZhToAA5ksLIaGarDiPwaVBzhLhfVsRjnIGaZhm44TkVzW5B9%2FhlYClvEvdAq%2Bw3%2BsktUa%2FOuxNeYTDj2NEZElhIirNzeM2tctwjy16WHEEg6ZBzEjeNhPHjAkFhFMHiROJE8CeDE%2B7OsL8JtQRK5tRdJVYgqk7cb1mdvFrGU%2BZbLaqq%2F4zJ8dsaIbKO%2BTz9z5JGuDPOUlLFr0JUzDoNjBGNC08EV8QDbGezzUYOwqROpnMTG8Dondjh0gFKY%2FOO20kTHPH8YHArL811Zr6YyOj%2BSllEWXo%2BmR4Waziuc%2FGjms6mFjZ2IaBgYFP8JDD3aZ3yB2n0%2FnR6sfulrbjYFxyLsaVMOmdjr0GOqUB7NkX0k6%2FpneGkVrYZD2kLtVXsAkBTJ5AG2cKomN6gGHzKjrxq4pqaJE7PwjGbjoalOVgAiVhuq%2FyjUpL1fJt%2B0Gdx%2BvwSK9mdR1C0zbRjEixLKPpD3HCaLpl%2FdDjeHUEI9zWi86OoQzSDImcK4Yj1pQrn2xre2i41kiwRxvFJoStONhOwuwbMrB4M4kh6dKZ3eBFv%2BIyYZlE7DWOA%2BuUmDu65U5%2B&X-Amz-Signature=ea7e213825d4fcccea38c5858a266b5ebaac8074f8f886ae2909a6dcc607c360&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
