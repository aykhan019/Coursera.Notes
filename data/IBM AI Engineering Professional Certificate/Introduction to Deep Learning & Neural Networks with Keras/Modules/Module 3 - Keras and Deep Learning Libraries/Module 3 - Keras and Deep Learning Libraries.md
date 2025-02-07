

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YALO5NXC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031921Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIFtNJfD%2Bfesvz%2FpNIj99bWz1a3LbloUGmwlB4FndmHbwAiEA%2FCx5IYCSoJNJlkhQOD4iYt4GQI27gJUOkyYhFvqa%2B9kq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDBB4BMcmqjArYDtUGircAzvSR9YXg9%2F3%2BYASGGbJdKpNmGusFMMObA1Tgr2FOaIqVYS3qgE8ix%2BKsuQqEiOcIQWW3McIXfp6S8%2FquOOYbZ3z96dy1IJJ7nkJ7sEzE9fApPj8W%2FJq0Sff401wUUzVHbimpLqT3ZombQE3fOgbooG7Ldsjsbj%2BsQqW6R2m0YmVDjxaG50CuOg4ZIMGxp%2BybaBVfU%2FffCgbs0uwg1AiE%2F5fmeQVblCShlw3hYlvm1ckg%2BhZWmsd74ndEwFZZXFgnoha1z5qlj%2BEYEzUg5mOvGplKcMonwwjNGRNn3EDUBqnh7wXT%2BAI%2B6IlM5ifASA5LKo7BbycL8Lq3Sc7RuOAMvQbpuxBuPoIdPQq1oCajSuINpskvXbwjjBu%2B8VCXdogKyFpmEQR4NvnsRGwew1T1y1so0lqT3GUK7ybusJmY1%2FXamResjuFMCKL7GYXhd%2BCCjf6s%2FlQ7iuOBT9ZUzZJMaxmAC0Y3pud93l3H4yLr2QBKMVyt8WnmJLv%2FuFakIAz8fB6WjCXB8C2wTy31PPIRwM14pK2Iys5e%2BRU7d1II8wKe4bqTWgh5G6IgCU8hDB%2F%2BaW9ln18CAo3SDdOr2FO5kKBQgCgj75jTtxqk0sglxROv2hZ9U2FzRvWfpFHMNiZlb0GOqUBfkoXvrOLE6A4ZtcJxMzvCanwCwj%2FX%2BJZB5R8R2f7HjRXsdmRpGg53tKaMhV2rofqYcjAezfQ42thzJara7V2QWtTdMLC8pSsFwQzRNpHyyUk1xsQcv6lqH8aW6ryo7hw1VL08r%2FIdHPwzuhSl7VM1Gd4vbPRGSa%2FNr2uahv%2BoilNF9yOCzJmX8PobOHFRJWppqbBqh5NPLFFUkDUw1dCxl01%2BIno&X-Amz-Signature=526dca039ff5fa524b89752d46108023e616c16734b5320b482ab1211dbc0edf&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YALO5NXC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031921Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIFtNJfD%2Bfesvz%2FpNIj99bWz1a3LbloUGmwlB4FndmHbwAiEA%2FCx5IYCSoJNJlkhQOD4iYt4GQI27gJUOkyYhFvqa%2B9kq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDBB4BMcmqjArYDtUGircAzvSR9YXg9%2F3%2BYASGGbJdKpNmGusFMMObA1Tgr2FOaIqVYS3qgE8ix%2BKsuQqEiOcIQWW3McIXfp6S8%2FquOOYbZ3z96dy1IJJ7nkJ7sEzE9fApPj8W%2FJq0Sff401wUUzVHbimpLqT3ZombQE3fOgbooG7Ldsjsbj%2BsQqW6R2m0YmVDjxaG50CuOg4ZIMGxp%2BybaBVfU%2FffCgbs0uwg1AiE%2F5fmeQVblCShlw3hYlvm1ckg%2BhZWmsd74ndEwFZZXFgnoha1z5qlj%2BEYEzUg5mOvGplKcMonwwjNGRNn3EDUBqnh7wXT%2BAI%2B6IlM5ifASA5LKo7BbycL8Lq3Sc7RuOAMvQbpuxBuPoIdPQq1oCajSuINpskvXbwjjBu%2B8VCXdogKyFpmEQR4NvnsRGwew1T1y1so0lqT3GUK7ybusJmY1%2FXamResjuFMCKL7GYXhd%2BCCjf6s%2FlQ7iuOBT9ZUzZJMaxmAC0Y3pud93l3H4yLr2QBKMVyt8WnmJLv%2FuFakIAz8fB6WjCXB8C2wTy31PPIRwM14pK2Iys5e%2BRU7d1II8wKe4bqTWgh5G6IgCU8hDB%2F%2BaW9ln18CAo3SDdOr2FO5kKBQgCgj75jTtxqk0sglxROv2hZ9U2FzRvWfpFHMNiZlb0GOqUBfkoXvrOLE6A4ZtcJxMzvCanwCwj%2FX%2BJZB5R8R2f7HjRXsdmRpGg53tKaMhV2rofqYcjAezfQ42thzJara7V2QWtTdMLC8pSsFwQzRNpHyyUk1xsQcv6lqH8aW6ryo7hw1VL08r%2FIdHPwzuhSl7VM1Gd4vbPRGSa%2FNr2uahv%2BoilNF9yOCzJmX8PobOHFRJWppqbBqh5NPLFFUkDUw1dCxl01%2BIno&X-Amz-Signature=605271c7b58a2055df16bba0f96fb4a29528bdcf8e9c1bb8f0822abb83eca79f&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YALO5NXC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031921Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIFtNJfD%2Bfesvz%2FpNIj99bWz1a3LbloUGmwlB4FndmHbwAiEA%2FCx5IYCSoJNJlkhQOD4iYt4GQI27gJUOkyYhFvqa%2B9kq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDBB4BMcmqjArYDtUGircAzvSR9YXg9%2F3%2BYASGGbJdKpNmGusFMMObA1Tgr2FOaIqVYS3qgE8ix%2BKsuQqEiOcIQWW3McIXfp6S8%2FquOOYbZ3z96dy1IJJ7nkJ7sEzE9fApPj8W%2FJq0Sff401wUUzVHbimpLqT3ZombQE3fOgbooG7Ldsjsbj%2BsQqW6R2m0YmVDjxaG50CuOg4ZIMGxp%2BybaBVfU%2FffCgbs0uwg1AiE%2F5fmeQVblCShlw3hYlvm1ckg%2BhZWmsd74ndEwFZZXFgnoha1z5qlj%2BEYEzUg5mOvGplKcMonwwjNGRNn3EDUBqnh7wXT%2BAI%2B6IlM5ifASA5LKo7BbycL8Lq3Sc7RuOAMvQbpuxBuPoIdPQq1oCajSuINpskvXbwjjBu%2B8VCXdogKyFpmEQR4NvnsRGwew1T1y1so0lqT3GUK7ybusJmY1%2FXamResjuFMCKL7GYXhd%2BCCjf6s%2FlQ7iuOBT9ZUzZJMaxmAC0Y3pud93l3H4yLr2QBKMVyt8WnmJLv%2FuFakIAz8fB6WjCXB8C2wTy31PPIRwM14pK2Iys5e%2BRU7d1II8wKe4bqTWgh5G6IgCU8hDB%2F%2BaW9ln18CAo3SDdOr2FO5kKBQgCgj75jTtxqk0sglxROv2hZ9U2FzRvWfpFHMNiZlb0GOqUBfkoXvrOLE6A4ZtcJxMzvCanwCwj%2FX%2BJZB5R8R2f7HjRXsdmRpGg53tKaMhV2rofqYcjAezfQ42thzJara7V2QWtTdMLC8pSsFwQzRNpHyyUk1xsQcv6lqH8aW6ryo7hw1VL08r%2FIdHPwzuhSl7VM1Gd4vbPRGSa%2FNr2uahv%2BoilNF9yOCzJmX8PobOHFRJWppqbBqh5NPLFFUkDUw1dCxl01%2BIno&X-Amz-Signature=94c0830985092c3cd56e132807357070a6915b353dbb9936be0f28edbc994640&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRU36NJG%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJGMEQCIC4PFKi2stTu%2FWguMf7TFlHkLPCLhIcyxUHy7uzi6J1GAiAlO5OBQOHrEG19t6My1C1Rfb7dTbON0x67%2F9f6DVvkwSr%2FAwhpEAAaDDYzNzQyMzE4MzgwNSIMjj0P%2BweRxLfdcFiJKtwDiMkGvv9W5IJIQotGXhfA594hgsu5hbIfe3cq8U8D5F%2Bs6N90elqIrQkLXWiRaXVD3dX7uTBuB25ZMRQGmFKQ0966NdxAeOH3oe5jX8Zyp3jLa%2BeBeZ89LTcO2mORiubWoOx6%2BL5zLbVFwdTg45qs5oEFsp%2BMh0j8FsRDNWUNAzUB%2Fm9IykuJZo8d6%2B%2FFSvAiGy676j%2B8CTNoItaWdffD6xsVqKvvCaLoFdkT9l2dj0La2OpXbETMWf3S2KbnyZUC1pBlW9QG0vudBCzor2conpQLluB6aqmy%2FxmYeLEVl%2BdxjqkC0QTTwwXMcK%2BTBhJPchWpcmdfUW%2B3sU5QBG3uBven%2B1yYw%2FpjIXnsr34Svp3E%2B9b4ckjRWN6Klo058c%2FOzR5U08jmmCdvkk%2Bqas72UmAh20hUOYkWZ9pgR8X0jEuoodAe5e7pbk9VRQF4MHm81OkNWWjHf9NojQBd9iKKtFv4T0v3xBwcet02pzzTDh%2FpwipPJcFOncaJURKWfceKryrDwQ5SAJHmVdXT8hbv1c%2BijTlboSzLbovSY%2FRiVJCkyQrWidx9uPGDghyEkURBI1Hgs1dQVukLGSOxtcG3zmsY6%2FCiy%2FtODVVso01dN09WmcHe6oqXYPXOkRAw7pmVvQY6pgFcw%2F3%2Ba%2FgcwaomCBozfCS0ixZyDH1Hf8%2B8bSEW9DUjR%2BaL8b2wkDIk%2FvMZ7%2Fup4sMTYlDumKEcPJhKeJ%2F64UJFhZYezx76b3r9XGqoB6mi1irjOthtzbuD2MvO3wIf60TLLG9O%2FqQzZognz3Tqh5cAWAwZ3ahrOzBNgMfayBUlPelF%2BkU86dvgIXYyU6L6r9JOn7enKIfxvlUSJCe%2FcRFDD%2FQ0w0nT&X-Amz-Signature=6690fdce942477f446b918a434f463a271a226df98c5f6c95313a6c423785bb4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WO4PJPAE%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIQD0odwqAHJX%2FHUfz0Bs6im8zNayUASr5SLqVTeCJNX2AwIgFBLvVSTDC8%2FqESk628DcQM1SdVyfOu66ogYcXhC2G60q%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDE8pUT8wI1KeeXvLVyrcAzvlMthQ1nGBzgtU262cCf6mQb5fSWpuDp4aB8fDa6DWLDeRXn82qtBg0n6QyJVBvPSXwlFHKze7swv1zU1s9TCf3LsCh7gLbGe6xpd6gGDDqPRi%2FkO8bY%2B9VqdlK3%2F5V2M4holCsgW4UO9At8OG8lTrpTUYSbqzz6vED8Q4AT%2Fb%2B%2Bmqpna6tzxzhft4j2k%2FVGqGLwthAqx9Vlx2C7HBBCus7H6kTuEuYnAwnU%2BkQCMv9yVd45yk4TP3TxuZZScOxXQyYznU5yJqzxRZ372f389QLv%2FoIiDrLPpB4YMP5DueM3iojv9WwIdRBtEC7tpL4%2Bktd0kUWLCRXfBqq%2FuJjLYLU2Kr7sp%2FAD0RAw9%2FO7hUj%2Bmgw9UhI271TKN7skI5bcPyRKD3gePESUc6P8oRztiC9HuREg%2B58wAoffjiN86p0ffup4KFclInvzxbEJBS8%2BGuKom6sP16dO3YIec5ps1jgOnUkvfXW97%2BPJ%2Bdju0VbQA4aFwfs4dOmaZWToyfjV4tqiWIRqlb5ThRK4BWbum7ot%2Bin5Thv2pO7Sq4nEU6Uuk1LH%2BxA%2BM98XeM1ifYirnt8cka0HvlfNRYw8eYrXP6RXvGiSwMC1rQmjdLkmyTECoYil5Z4zcYyLBQMNqZlb0GOqUBC%2BAOwhxVYhVk4Y33t2yJ%2FUX7JY6k94I3GnqBqPGvYEPapvqOKXmYpJSD6lBpSxLNVtpO7ieRWPT3Qbtck7rh%2BdCHJVb%2BZavetFtPIRDiSuIVAAHUTWDcgNsgtKmQXoWEY8v14sliKpfx2STDhKvDczct9nvTT0ONCv8D66cE2q7O7DVKg2pISEzBrCJAzOi74K2L5gU3pL9ccPgpUUdpJ64PECxN&X-Amz-Signature=072876a3acfcbf7409c350e9ca2686ccb2bf6821a2b833ef18909667e97dcbcf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YALO5NXC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031921Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIFtNJfD%2Bfesvz%2FpNIj99bWz1a3LbloUGmwlB4FndmHbwAiEA%2FCx5IYCSoJNJlkhQOD4iYt4GQI27gJUOkyYhFvqa%2B9kq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDBB4BMcmqjArYDtUGircAzvSR9YXg9%2F3%2BYASGGbJdKpNmGusFMMObA1Tgr2FOaIqVYS3qgE8ix%2BKsuQqEiOcIQWW3McIXfp6S8%2FquOOYbZ3z96dy1IJJ7nkJ7sEzE9fApPj8W%2FJq0Sff401wUUzVHbimpLqT3ZombQE3fOgbooG7Ldsjsbj%2BsQqW6R2m0YmVDjxaG50CuOg4ZIMGxp%2BybaBVfU%2FffCgbs0uwg1AiE%2F5fmeQVblCShlw3hYlvm1ckg%2BhZWmsd74ndEwFZZXFgnoha1z5qlj%2BEYEzUg5mOvGplKcMonwwjNGRNn3EDUBqnh7wXT%2BAI%2B6IlM5ifASA5LKo7BbycL8Lq3Sc7RuOAMvQbpuxBuPoIdPQq1oCajSuINpskvXbwjjBu%2B8VCXdogKyFpmEQR4NvnsRGwew1T1y1so0lqT3GUK7ybusJmY1%2FXamResjuFMCKL7GYXhd%2BCCjf6s%2FlQ7iuOBT9ZUzZJMaxmAC0Y3pud93l3H4yLr2QBKMVyt8WnmJLv%2FuFakIAz8fB6WjCXB8C2wTy31PPIRwM14pK2Iys5e%2BRU7d1II8wKe4bqTWgh5G6IgCU8hDB%2F%2BaW9ln18CAo3SDdOr2FO5kKBQgCgj75jTtxqk0sglxROv2hZ9U2FzRvWfpFHMNiZlb0GOqUBfkoXvrOLE6A4ZtcJxMzvCanwCwj%2FX%2BJZB5R8R2f7HjRXsdmRpGg53tKaMhV2rofqYcjAezfQ42thzJara7V2QWtTdMLC8pSsFwQzRNpHyyUk1xsQcv6lqH8aW6ryo7hw1VL08r%2FIdHPwzuhSl7VM1Gd4vbPRGSa%2FNr2uahv%2BoilNF9yOCzJmX8PobOHFRJWppqbBqh5NPLFFUkDUw1dCxl01%2BIno&X-Amz-Signature=4ac32be7896fb869e75a3f771f9863a36caf28f5f7e24dbfc5c1641e1bc6447b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YALO5NXC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031921Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIFtNJfD%2Bfesvz%2FpNIj99bWz1a3LbloUGmwlB4FndmHbwAiEA%2FCx5IYCSoJNJlkhQOD4iYt4GQI27gJUOkyYhFvqa%2B9kq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDBB4BMcmqjArYDtUGircAzvSR9YXg9%2F3%2BYASGGbJdKpNmGusFMMObA1Tgr2FOaIqVYS3qgE8ix%2BKsuQqEiOcIQWW3McIXfp6S8%2FquOOYbZ3z96dy1IJJ7nkJ7sEzE9fApPj8W%2FJq0Sff401wUUzVHbimpLqT3ZombQE3fOgbooG7Ldsjsbj%2BsQqW6R2m0YmVDjxaG50CuOg4ZIMGxp%2BybaBVfU%2FffCgbs0uwg1AiE%2F5fmeQVblCShlw3hYlvm1ckg%2BhZWmsd74ndEwFZZXFgnoha1z5qlj%2BEYEzUg5mOvGplKcMonwwjNGRNn3EDUBqnh7wXT%2BAI%2B6IlM5ifASA5LKo7BbycL8Lq3Sc7RuOAMvQbpuxBuPoIdPQq1oCajSuINpskvXbwjjBu%2B8VCXdogKyFpmEQR4NvnsRGwew1T1y1so0lqT3GUK7ybusJmY1%2FXamResjuFMCKL7GYXhd%2BCCjf6s%2FlQ7iuOBT9ZUzZJMaxmAC0Y3pud93l3H4yLr2QBKMVyt8WnmJLv%2FuFakIAz8fB6WjCXB8C2wTy31PPIRwM14pK2Iys5e%2BRU7d1II8wKe4bqTWgh5G6IgCU8hDB%2F%2BaW9ln18CAo3SDdOr2FO5kKBQgCgj75jTtxqk0sglxROv2hZ9U2FzRvWfpFHMNiZlb0GOqUBfkoXvrOLE6A4ZtcJxMzvCanwCwj%2FX%2BJZB5R8R2f7HjRXsdmRpGg53tKaMhV2rofqYcjAezfQ42thzJara7V2QWtTdMLC8pSsFwQzRNpHyyUk1xsQcv6lqH8aW6ryo7hw1VL08r%2FIdHPwzuhSl7VM1Gd4vbPRGSa%2FNr2uahv%2BoilNF9yOCzJmX8PobOHFRJWppqbBqh5NPLFFUkDUw1dCxl01%2BIno&X-Amz-Signature=4fdf3cf49851d7e154fe6ed5118e71ae36ad0d6fa2a22b0ea89364168d004f8c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YALO5NXC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031921Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIFtNJfD%2Bfesvz%2FpNIj99bWz1a3LbloUGmwlB4FndmHbwAiEA%2FCx5IYCSoJNJlkhQOD4iYt4GQI27gJUOkyYhFvqa%2B9kq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDBB4BMcmqjArYDtUGircAzvSR9YXg9%2F3%2BYASGGbJdKpNmGusFMMObA1Tgr2FOaIqVYS3qgE8ix%2BKsuQqEiOcIQWW3McIXfp6S8%2FquOOYbZ3z96dy1IJJ7nkJ7sEzE9fApPj8W%2FJq0Sff401wUUzVHbimpLqT3ZombQE3fOgbooG7Ldsjsbj%2BsQqW6R2m0YmVDjxaG50CuOg4ZIMGxp%2BybaBVfU%2FffCgbs0uwg1AiE%2F5fmeQVblCShlw3hYlvm1ckg%2BhZWmsd74ndEwFZZXFgnoha1z5qlj%2BEYEzUg5mOvGplKcMonwwjNGRNn3EDUBqnh7wXT%2BAI%2B6IlM5ifASA5LKo7BbycL8Lq3Sc7RuOAMvQbpuxBuPoIdPQq1oCajSuINpskvXbwjjBu%2B8VCXdogKyFpmEQR4NvnsRGwew1T1y1so0lqT3GUK7ybusJmY1%2FXamResjuFMCKL7GYXhd%2BCCjf6s%2FlQ7iuOBT9ZUzZJMaxmAC0Y3pud93l3H4yLr2QBKMVyt8WnmJLv%2FuFakIAz8fB6WjCXB8C2wTy31PPIRwM14pK2Iys5e%2BRU7d1II8wKe4bqTWgh5G6IgCU8hDB%2F%2BaW9ln18CAo3SDdOr2FO5kKBQgCgj75jTtxqk0sglxROv2hZ9U2FzRvWfpFHMNiZlb0GOqUBfkoXvrOLE6A4ZtcJxMzvCanwCwj%2FX%2BJZB5R8R2f7HjRXsdmRpGg53tKaMhV2rofqYcjAezfQ42thzJara7V2QWtTdMLC8pSsFwQzRNpHyyUk1xsQcv6lqH8aW6ryo7hw1VL08r%2FIdHPwzuhSl7VM1Gd4vbPRGSa%2FNr2uahv%2BoilNF9yOCzJmX8PobOHFRJWppqbBqh5NPLFFUkDUw1dCxl01%2BIno&X-Amz-Signature=259c24a6cc4625581a86da23d49095b84786355febbe177afcd8bdf0f4805aa1&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YALO5NXC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031921Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIFtNJfD%2Bfesvz%2FpNIj99bWz1a3LbloUGmwlB4FndmHbwAiEA%2FCx5IYCSoJNJlkhQOD4iYt4GQI27gJUOkyYhFvqa%2B9kq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDBB4BMcmqjArYDtUGircAzvSR9YXg9%2F3%2BYASGGbJdKpNmGusFMMObA1Tgr2FOaIqVYS3qgE8ix%2BKsuQqEiOcIQWW3McIXfp6S8%2FquOOYbZ3z96dy1IJJ7nkJ7sEzE9fApPj8W%2FJq0Sff401wUUzVHbimpLqT3ZombQE3fOgbooG7Ldsjsbj%2BsQqW6R2m0YmVDjxaG50CuOg4ZIMGxp%2BybaBVfU%2FffCgbs0uwg1AiE%2F5fmeQVblCShlw3hYlvm1ckg%2BhZWmsd74ndEwFZZXFgnoha1z5qlj%2BEYEzUg5mOvGplKcMonwwjNGRNn3EDUBqnh7wXT%2BAI%2B6IlM5ifASA5LKo7BbycL8Lq3Sc7RuOAMvQbpuxBuPoIdPQq1oCajSuINpskvXbwjjBu%2B8VCXdogKyFpmEQR4NvnsRGwew1T1y1so0lqT3GUK7ybusJmY1%2FXamResjuFMCKL7GYXhd%2BCCjf6s%2FlQ7iuOBT9ZUzZJMaxmAC0Y3pud93l3H4yLr2QBKMVyt8WnmJLv%2FuFakIAz8fB6WjCXB8C2wTy31PPIRwM14pK2Iys5e%2BRU7d1II8wKe4bqTWgh5G6IgCU8hDB%2F%2BaW9ln18CAo3SDdOr2FO5kKBQgCgj75jTtxqk0sglxROv2hZ9U2FzRvWfpFHMNiZlb0GOqUBfkoXvrOLE6A4ZtcJxMzvCanwCwj%2FX%2BJZB5R8R2f7HjRXsdmRpGg53tKaMhV2rofqYcjAezfQ42thzJara7V2QWtTdMLC8pSsFwQzRNpHyyUk1xsQcv6lqH8aW6ryo7hw1VL08r%2FIdHPwzuhSl7VM1Gd4vbPRGSa%2FNr2uahv%2BoilNF9yOCzJmX8PobOHFRJWppqbBqh5NPLFFUkDUw1dCxl01%2BIno&X-Amz-Signature=8e2789c7805d931154bf3a8fe201ed2b4b7c5ce30abdc5055d27de3067e4240d&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
