

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4BAHZ3P%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T191231Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJGMEQCIB6b%2FYgO7QMJOVQVAQiuZ3s0pPPT2NAb8kYter4YQ1GSAiAVRrhi8Gj1ls3JDGfnmucC0aKtG9YmhbCEkSTzOQ4lSir%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMwQOkuHWmPbjdRZaEKtwDTPKr2hPpv9LKe6HjxOrN0N72f%2BPsdBBh2MH47QjyjzI6GvCz2FDB8ksSUJAqXtjW0rSG8zIB0DLImQ%2BaQCNkk3vT0YUsxe2rn5sO6i1jM9YQzpIQschXS7F%2BU8zmqZCLAG8PYScfXdb2ibfTxA2JK9Yw9nYurejq2bQMIAAA08WYaysCjb5W6AXGcV7a1jFMGq0x%2FtbtVc8F2Nz%2Fqd6ZDj%2F%2B9JiY4YVgOzAN5KEyVXNdDxcW9fhKthBjvrsVgxnjr5HY8s460WaRxjybFPA1s56ptl5CRBNjSyiChCRN16n9hh%2BI7TiSeG62ZmLj%2FYINDGEOEJfekvflewZ1oTJFsPeObP5tNPuSxb%2BVDYLBVTXFX7P47r%2FVFFjoeMoJt4kADtXNftLZ9Ah39q1JzbEbRAttK8DAQ%2FzHt%2Bq5gaxWcXBJj9ULgqNG5qGPJAXnt35%2FaTts5QelP2px6Fw000pztezJJQCp%2FfWOMITwbBltTPhKIQK2aw%2BLSC4QhSBkBUW3NCiUV7JtXHRzzBLNxcONucU0IGuHVvvHDVdZBRXC5%2BHYbAAZIBwQf4kgS0Jj0h%2Bj6YlHpTqjWsDPnqLbLLY%2FfonoB4bfeLOmu6LSp2gps8YSpcvywP24WnkGcyowobqOvQY6pgGVXMRFcM2hP88FJwhOh9UDkD7OyMiWgL0gwbGZ5AFWrTRZcknvavjSON4lzBYgkgs3Hd%2BeTPseVMoACYjfMoChOxcqBaqo2Ub2YtrFlYqvXv1tuun4kITNu1bSlfE0hE5IvypkY2v9gS6rFNMugbiG%2FeC8CXyA7%2B4YKhAtl8lcoIhnEql2qTmmNZlUxv9J82cejehkLgdf3ZYWPuFiMcvCqPZFPwtv&X-Amz-Signature=76b09ef8d4c57af1e108b21eef28273c07e163b6d22359726b18191cc2cc2d06&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4BAHZ3P%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T191231Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJGMEQCIB6b%2FYgO7QMJOVQVAQiuZ3s0pPPT2NAb8kYter4YQ1GSAiAVRrhi8Gj1ls3JDGfnmucC0aKtG9YmhbCEkSTzOQ4lSir%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMwQOkuHWmPbjdRZaEKtwDTPKr2hPpv9LKe6HjxOrN0N72f%2BPsdBBh2MH47QjyjzI6GvCz2FDB8ksSUJAqXtjW0rSG8zIB0DLImQ%2BaQCNkk3vT0YUsxe2rn5sO6i1jM9YQzpIQschXS7F%2BU8zmqZCLAG8PYScfXdb2ibfTxA2JK9Yw9nYurejq2bQMIAAA08WYaysCjb5W6AXGcV7a1jFMGq0x%2FtbtVc8F2Nz%2Fqd6ZDj%2F%2B9JiY4YVgOzAN5KEyVXNdDxcW9fhKthBjvrsVgxnjr5HY8s460WaRxjybFPA1s56ptl5CRBNjSyiChCRN16n9hh%2BI7TiSeG62ZmLj%2FYINDGEOEJfekvflewZ1oTJFsPeObP5tNPuSxb%2BVDYLBVTXFX7P47r%2FVFFjoeMoJt4kADtXNftLZ9Ah39q1JzbEbRAttK8DAQ%2FzHt%2Bq5gaxWcXBJj9ULgqNG5qGPJAXnt35%2FaTts5QelP2px6Fw000pztezJJQCp%2FfWOMITwbBltTPhKIQK2aw%2BLSC4QhSBkBUW3NCiUV7JtXHRzzBLNxcONucU0IGuHVvvHDVdZBRXC5%2BHYbAAZIBwQf4kgS0Jj0h%2Bj6YlHpTqjWsDPnqLbLLY%2FfonoB4bfeLOmu6LSp2gps8YSpcvywP24WnkGcyowobqOvQY6pgGVXMRFcM2hP88FJwhOh9UDkD7OyMiWgL0gwbGZ5AFWrTRZcknvavjSON4lzBYgkgs3Hd%2BeTPseVMoACYjfMoChOxcqBaqo2Ub2YtrFlYqvXv1tuun4kITNu1bSlfE0hE5IvypkY2v9gS6rFNMugbiG%2FeC8CXyA7%2B4YKhAtl8lcoIhnEql2qTmmNZlUxv9J82cejehkLgdf3ZYWPuFiMcvCqPZFPwtv&X-Amz-Signature=378ddaf96d72c4ca08ffe071393047b23df1500b439873279d62d2c864a5b6f5&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4BAHZ3P%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T191231Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJGMEQCIB6b%2FYgO7QMJOVQVAQiuZ3s0pPPT2NAb8kYter4YQ1GSAiAVRrhi8Gj1ls3JDGfnmucC0aKtG9YmhbCEkSTzOQ4lSir%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMwQOkuHWmPbjdRZaEKtwDTPKr2hPpv9LKe6HjxOrN0N72f%2BPsdBBh2MH47QjyjzI6GvCz2FDB8ksSUJAqXtjW0rSG8zIB0DLImQ%2BaQCNkk3vT0YUsxe2rn5sO6i1jM9YQzpIQschXS7F%2BU8zmqZCLAG8PYScfXdb2ibfTxA2JK9Yw9nYurejq2bQMIAAA08WYaysCjb5W6AXGcV7a1jFMGq0x%2FtbtVc8F2Nz%2Fqd6ZDj%2F%2B9JiY4YVgOzAN5KEyVXNdDxcW9fhKthBjvrsVgxnjr5HY8s460WaRxjybFPA1s56ptl5CRBNjSyiChCRN16n9hh%2BI7TiSeG62ZmLj%2FYINDGEOEJfekvflewZ1oTJFsPeObP5tNPuSxb%2BVDYLBVTXFX7P47r%2FVFFjoeMoJt4kADtXNftLZ9Ah39q1JzbEbRAttK8DAQ%2FzHt%2Bq5gaxWcXBJj9ULgqNG5qGPJAXnt35%2FaTts5QelP2px6Fw000pztezJJQCp%2FfWOMITwbBltTPhKIQK2aw%2BLSC4QhSBkBUW3NCiUV7JtXHRzzBLNxcONucU0IGuHVvvHDVdZBRXC5%2BHYbAAZIBwQf4kgS0Jj0h%2Bj6YlHpTqjWsDPnqLbLLY%2FfonoB4bfeLOmu6LSp2gps8YSpcvywP24WnkGcyowobqOvQY6pgGVXMRFcM2hP88FJwhOh9UDkD7OyMiWgL0gwbGZ5AFWrTRZcknvavjSON4lzBYgkgs3Hd%2BeTPseVMoACYjfMoChOxcqBaqo2Ub2YtrFlYqvXv1tuun4kITNu1bSlfE0hE5IvypkY2v9gS6rFNMugbiG%2FeC8CXyA7%2B4YKhAtl8lcoIhnEql2qTmmNZlUxv9J82cejehkLgdf3ZYWPuFiMcvCqPZFPwtv&X-Amz-Signature=dce1043a8f652297fa4403f9d4c692548aa1e173b36a58f9ed078ae0e3bb9d92&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X7LAAPOT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T191232Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIDjzAZulBblU7YGL1CqAddZ9YDq6I0pYQbdlKkxYsWdeAiADQkCPK%2ByrWzETkcNPr2ZHZ8TfXjowUqz8x4AoLVC0sCr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMnSHJBIqbssLntpNjKtwDbnUj%2FWkdq0RrwpnLL5Gcvnuu%2BVCfFv%2BiO1uAendwMa2yCdzs67VWg5qV7DDom9RBwY1dNO7SEMuC8NbYzRq2AOMV34hp229O8XyFYf8n3VsDYcirtjtGNaad1eNRw4XRJ6bM%2F5riQv7jAKNnwMQ2VPVBog6Lzyzy0%2FiINokvUA8O2kV7Pu%2FKGECajf11KA8nok2oELQ%2BRx%2FY%2BRUjSvgJYnNJ23qFNllOZhOXfXo%2ByBLIaCJz4FUsethStSNdOaeoXaoaxRwoNY8n%2FC3ecJaFVhSY8q5CDZALtiY3y1pB9kI8IjMgX8GFvJDnkNkXjXgkq0BKt0sqwdMbiMaqyXKFjCoNTkk%2BKL578ngeX%2FyGrFc46yEf%2F32WPkj855S9DJ8a1hFZgQolxfM%2BPghYmbS0GyF50CB7fiWex2B1hsF8frhZIIo91raiRON%2BIf0Pv2mZsUftctlYTDW2vm2BZ1GJ6RkLjY9Yp3WKRf0YRCfV9wmwNZSvWPbZLr7HYwmLrrNd8lOZ%2Frt6MxlemmuHA7qL5N%2FM%2FVoDT%2FUOlwLBKZ4XmcilpRK3sk7TbezgrmspfM5W3vX%2F01SNyW6F%2FmvahsVh4Tp30Y%2F2BEGiB8Ow8CHLhXGDy8wHNKXEgt9RC44wrLuOvQY6pgESz34cju%2Bm%2F5jcKgXMXkghHRZCo%2BOnBBRAJ3kklxky7MY7ApKzQy9QiEvjgky%2BDNFvFm9m5Ms26eB6kzzLxluWCiApNLsP%2F6Vxq93v6MMOZAyhCtOzLDVca4DwLfbwYAK0FTsExIIESyE6JIXXKDg8sR9RQFFq9%2BGB9bwODLtdbMNywCK9TH2YiuV410mhsQedN5mpZkvOvZGDg8GbE3ZFpXa6xok%2B&X-Amz-Signature=07f950bfb6d7de11acd182c3b007a99410998e53867eadb675bcb43fff6e90c0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJYOPRVO%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T191231Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQCnKTWcTgZufZxLXCzmpbMhq3r4yQleOoQO9xlCPSAU6AIgQby9Q2h967cN5SGKpbLZQtV%2BJXcww2w%2F%2Bjmc39LBEuAq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDF5KtCa7%2Bs%2B0170%2FcSrcA%2BmdOcu2B%2FZk5sEnOyAeXEcSeioDoFJ%2FU3GC0BWd4V5YiNfQrGfeRmVqrnoOBYRNoMOioCZI%2F5oPdNaAoN8QcQ%2FnTDJIJqKdYPBeK5cAjLTdd3NgMr2KR9y8MXwPGRdlcvfevH8ildOEgzLIpu%2BwNICYnQlP1q9hCxFwaU3nVHdMOMnNBkKRCbIoGc9QXvO54mFSBNMbuJcYBkiUvKsEGjJwW3nXvTF0A7nzhD86jApvg2177OSzBj2bGeYuL83YRqv7KfutB%2B1puhOA99WZbGVu%2Fwa4vuuc9tJb4bRkxGjym2BsrTLBENkbZv7XAar2%2BgJ9W8eJJPvYLYnaVCgZvh863ZNv7mfD0wRIqY0gceZow7LRZcx5Ut%2BHLjX4caduh5C95aP7dYVQmvUMw%2F10%2FBmDqGXFZWxX0qW6Rw7l4uTDzCMJ0oldt4%2B5sYMOC4GLeQ12Yf8qewiITHtG5lpJggwxXZP7MrEuMyfJPJ%2FlJaF9HD2kLmCeSiwA6yxnDhrL9kL1g4IJmAzXGPCmuBwQl1%2F9K%2F%2B5G43zCLBl7HOM7GbTyyNTHtj6m%2BldXy2tQ%2BgbJtdAriuyXbExLjmPwzFH1iHZq67%2F5%2FTcmtzd0FnuhymmBGsTPDCF2FRUB0PkMNG6jr0GOqUB27xhYmOEbgInW%2FGE%2Fwpyr7G01Jf9eEmapkR6if0Bu0oc3WyBGffwBeyFfAOf8tJB0LaInQ3PlZUEZNA8MWc%2F3BIn1stf%2FGfYKOVaQlvfrMBuE7pZTDjqHkf28bncY3I8ZaNBFWLghVq0ZnF7fzttauftlqjsk%2FTUt6faL16kOXowDkCqNCOSv6HpvUkDNKt3rj5G%2BjIUOBU4DOfJ%2BJ4%2BtEfLfL%2FP&X-Amz-Signature=8dd2ca2c567fec47d73d574decc1e984a3492bf3a60b0700555aeeebc0660c14&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4BAHZ3P%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T191231Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJGMEQCIB6b%2FYgO7QMJOVQVAQiuZ3s0pPPT2NAb8kYter4YQ1GSAiAVRrhi8Gj1ls3JDGfnmucC0aKtG9YmhbCEkSTzOQ4lSir%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMwQOkuHWmPbjdRZaEKtwDTPKr2hPpv9LKe6HjxOrN0N72f%2BPsdBBh2MH47QjyjzI6GvCz2FDB8ksSUJAqXtjW0rSG8zIB0DLImQ%2BaQCNkk3vT0YUsxe2rn5sO6i1jM9YQzpIQschXS7F%2BU8zmqZCLAG8PYScfXdb2ibfTxA2JK9Yw9nYurejq2bQMIAAA08WYaysCjb5W6AXGcV7a1jFMGq0x%2FtbtVc8F2Nz%2Fqd6ZDj%2F%2B9JiY4YVgOzAN5KEyVXNdDxcW9fhKthBjvrsVgxnjr5HY8s460WaRxjybFPA1s56ptl5CRBNjSyiChCRN16n9hh%2BI7TiSeG62ZmLj%2FYINDGEOEJfekvflewZ1oTJFsPeObP5tNPuSxb%2BVDYLBVTXFX7P47r%2FVFFjoeMoJt4kADtXNftLZ9Ah39q1JzbEbRAttK8DAQ%2FzHt%2Bq5gaxWcXBJj9ULgqNG5qGPJAXnt35%2FaTts5QelP2px6Fw000pztezJJQCp%2FfWOMITwbBltTPhKIQK2aw%2BLSC4QhSBkBUW3NCiUV7JtXHRzzBLNxcONucU0IGuHVvvHDVdZBRXC5%2BHYbAAZIBwQf4kgS0Jj0h%2Bj6YlHpTqjWsDPnqLbLLY%2FfonoB4bfeLOmu6LSp2gps8YSpcvywP24WnkGcyowobqOvQY6pgGVXMRFcM2hP88FJwhOh9UDkD7OyMiWgL0gwbGZ5AFWrTRZcknvavjSON4lzBYgkgs3Hd%2BeTPseVMoACYjfMoChOxcqBaqo2Ub2YtrFlYqvXv1tuun4kITNu1bSlfE0hE5IvypkY2v9gS6rFNMugbiG%2FeC8CXyA7%2B4YKhAtl8lcoIhnEql2qTmmNZlUxv9J82cejehkLgdf3ZYWPuFiMcvCqPZFPwtv&X-Amz-Signature=8326f443e489c3fffa44b8ae4e0ec4588747929fb0f1bcb75016152b5991963f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4BAHZ3P%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T191231Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJGMEQCIB6b%2FYgO7QMJOVQVAQiuZ3s0pPPT2NAb8kYter4YQ1GSAiAVRrhi8Gj1ls3JDGfnmucC0aKtG9YmhbCEkSTzOQ4lSir%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMwQOkuHWmPbjdRZaEKtwDTPKr2hPpv9LKe6HjxOrN0N72f%2BPsdBBh2MH47QjyjzI6GvCz2FDB8ksSUJAqXtjW0rSG8zIB0DLImQ%2BaQCNkk3vT0YUsxe2rn5sO6i1jM9YQzpIQschXS7F%2BU8zmqZCLAG8PYScfXdb2ibfTxA2JK9Yw9nYurejq2bQMIAAA08WYaysCjb5W6AXGcV7a1jFMGq0x%2FtbtVc8F2Nz%2Fqd6ZDj%2F%2B9JiY4YVgOzAN5KEyVXNdDxcW9fhKthBjvrsVgxnjr5HY8s460WaRxjybFPA1s56ptl5CRBNjSyiChCRN16n9hh%2BI7TiSeG62ZmLj%2FYINDGEOEJfekvflewZ1oTJFsPeObP5tNPuSxb%2BVDYLBVTXFX7P47r%2FVFFjoeMoJt4kADtXNftLZ9Ah39q1JzbEbRAttK8DAQ%2FzHt%2Bq5gaxWcXBJj9ULgqNG5qGPJAXnt35%2FaTts5QelP2px6Fw000pztezJJQCp%2FfWOMITwbBltTPhKIQK2aw%2BLSC4QhSBkBUW3NCiUV7JtXHRzzBLNxcONucU0IGuHVvvHDVdZBRXC5%2BHYbAAZIBwQf4kgS0Jj0h%2Bj6YlHpTqjWsDPnqLbLLY%2FfonoB4bfeLOmu6LSp2gps8YSpcvywP24WnkGcyowobqOvQY6pgGVXMRFcM2hP88FJwhOh9UDkD7OyMiWgL0gwbGZ5AFWrTRZcknvavjSON4lzBYgkgs3Hd%2BeTPseVMoACYjfMoChOxcqBaqo2Ub2YtrFlYqvXv1tuun4kITNu1bSlfE0hE5IvypkY2v9gS6rFNMugbiG%2FeC8CXyA7%2B4YKhAtl8lcoIhnEql2qTmmNZlUxv9J82cejehkLgdf3ZYWPuFiMcvCqPZFPwtv&X-Amz-Signature=d870abb72c1a30833c53beb04a5edc776c1b3e477fb56770fbbfbad630c5c0f1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4BAHZ3P%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T191231Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJGMEQCIB6b%2FYgO7QMJOVQVAQiuZ3s0pPPT2NAb8kYter4YQ1GSAiAVRrhi8Gj1ls3JDGfnmucC0aKtG9YmhbCEkSTzOQ4lSir%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMwQOkuHWmPbjdRZaEKtwDTPKr2hPpv9LKe6HjxOrN0N72f%2BPsdBBh2MH47QjyjzI6GvCz2FDB8ksSUJAqXtjW0rSG8zIB0DLImQ%2BaQCNkk3vT0YUsxe2rn5sO6i1jM9YQzpIQschXS7F%2BU8zmqZCLAG8PYScfXdb2ibfTxA2JK9Yw9nYurejq2bQMIAAA08WYaysCjb5W6AXGcV7a1jFMGq0x%2FtbtVc8F2Nz%2Fqd6ZDj%2F%2B9JiY4YVgOzAN5KEyVXNdDxcW9fhKthBjvrsVgxnjr5HY8s460WaRxjybFPA1s56ptl5CRBNjSyiChCRN16n9hh%2BI7TiSeG62ZmLj%2FYINDGEOEJfekvflewZ1oTJFsPeObP5tNPuSxb%2BVDYLBVTXFX7P47r%2FVFFjoeMoJt4kADtXNftLZ9Ah39q1JzbEbRAttK8DAQ%2FzHt%2Bq5gaxWcXBJj9ULgqNG5qGPJAXnt35%2FaTts5QelP2px6Fw000pztezJJQCp%2FfWOMITwbBltTPhKIQK2aw%2BLSC4QhSBkBUW3NCiUV7JtXHRzzBLNxcONucU0IGuHVvvHDVdZBRXC5%2BHYbAAZIBwQf4kgS0Jj0h%2Bj6YlHpTqjWsDPnqLbLLY%2FfonoB4bfeLOmu6LSp2gps8YSpcvywP24WnkGcyowobqOvQY6pgGVXMRFcM2hP88FJwhOh9UDkD7OyMiWgL0gwbGZ5AFWrTRZcknvavjSON4lzBYgkgs3Hd%2BeTPseVMoACYjfMoChOxcqBaqo2Ub2YtrFlYqvXv1tuun4kITNu1bSlfE0hE5IvypkY2v9gS6rFNMugbiG%2FeC8CXyA7%2B4YKhAtl8lcoIhnEql2qTmmNZlUxv9J82cejehkLgdf3ZYWPuFiMcvCqPZFPwtv&X-Amz-Signature=13d3030ac8676496ca9058a9fcf9fd5fecbdf0255396cdd66f15a7cc14b2ca26&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4BAHZ3P%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T191231Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJGMEQCIB6b%2FYgO7QMJOVQVAQiuZ3s0pPPT2NAb8kYter4YQ1GSAiAVRrhi8Gj1ls3JDGfnmucC0aKtG9YmhbCEkSTzOQ4lSir%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMwQOkuHWmPbjdRZaEKtwDTPKr2hPpv9LKe6HjxOrN0N72f%2BPsdBBh2MH47QjyjzI6GvCz2FDB8ksSUJAqXtjW0rSG8zIB0DLImQ%2BaQCNkk3vT0YUsxe2rn5sO6i1jM9YQzpIQschXS7F%2BU8zmqZCLAG8PYScfXdb2ibfTxA2JK9Yw9nYurejq2bQMIAAA08WYaysCjb5W6AXGcV7a1jFMGq0x%2FtbtVc8F2Nz%2Fqd6ZDj%2F%2B9JiY4YVgOzAN5KEyVXNdDxcW9fhKthBjvrsVgxnjr5HY8s460WaRxjybFPA1s56ptl5CRBNjSyiChCRN16n9hh%2BI7TiSeG62ZmLj%2FYINDGEOEJfekvflewZ1oTJFsPeObP5tNPuSxb%2BVDYLBVTXFX7P47r%2FVFFjoeMoJt4kADtXNftLZ9Ah39q1JzbEbRAttK8DAQ%2FzHt%2Bq5gaxWcXBJj9ULgqNG5qGPJAXnt35%2FaTts5QelP2px6Fw000pztezJJQCp%2FfWOMITwbBltTPhKIQK2aw%2BLSC4QhSBkBUW3NCiUV7JtXHRzzBLNxcONucU0IGuHVvvHDVdZBRXC5%2BHYbAAZIBwQf4kgS0Jj0h%2Bj6YlHpTqjWsDPnqLbLLY%2FfonoB4bfeLOmu6LSp2gps8YSpcvywP24WnkGcyowobqOvQY6pgGVXMRFcM2hP88FJwhOh9UDkD7OyMiWgL0gwbGZ5AFWrTRZcknvavjSON4lzBYgkgs3Hd%2BeTPseVMoACYjfMoChOxcqBaqo2Ub2YtrFlYqvXv1tuun4kITNu1bSlfE0hE5IvypkY2v9gS6rFNMugbiG%2FeC8CXyA7%2B4YKhAtl8lcoIhnEql2qTmmNZlUxv9J82cejehkLgdf3ZYWPuFiMcvCqPZFPwtv&X-Amz-Signature=f92936bce06f116617aff74d5600c038166f921d38c4b9a0f21ef2c65229f8b5&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
