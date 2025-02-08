

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBFYT26C%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010733Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJHMEUCIAqIy6xD5O2ZfSGKmEZ003z0N57f39fhIK8gEjmFNznEAiEAriNXXcpTCcFOrCe%2BV56ATmqueP81j2JKb3OFu3T%2FoFQqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOo3NEnAljAvgZPTAyrcAwuuzEeW%2FKsnw%2FC2Mq2agQiCZbqASnD8nkG7dgonJO%2BAsA2w9XkSGzMDFkzvwNGXK2fHw8UhPn31u5ktwzEnXhhXVgQBR40%2BqD7U0dz%2FV%2FSsglXNF4gu%2FXXUhGkYBXMraXBqzFKMQkAcloUa94ky2heYVAlQ0FOg2dSVnt6On76ZNPo331e%2BnwFOm3bHx0YtHgQJF41oMYYXGnoKLir64LnRt2SPmABPNBi6RQP5yHJh0xg6S34S%2BbS8GZ%2FcAfhgjEQ6ABW6b6WM5sxruZderIHNBfN0Mct04vN60I9bMW%2BDRbkWQ2by9JR9a9nbMkSizNVltYMpGhg9Jz1BIEElBwnAvcDD%2FLczdJeeme0WLNBP2ZHRBzt6If5uCJy5NI0LgNbzJeCqq%2FI6P%2Fe%2BVOumhg6Jj1B7uOMa%2FDRvMHdyP4DmwNJTomCBoH8PmFNBwmd07%2FhklyExr8usXlsoltXkJQtQQ5XP%2Fw9iM3AB1w3RT%2FNXWL5VFHeecjqZlkeGNmRDsdM4TWvcGoYmo%2FC3tMoJDAJKMZagiieoYfg2wMZAIFRTHbGB1antXMj7G0FlZABuwlfv8dz7IXuLHpD7z570NHz%2FCptm9rB2Ryyg0UFB9SiW6Zy0uZdJE0LfrFJRMP%2B%2Bmr0GOqUBmxEBJM2IGAFssll0vQK9dfYe1znhpHkzuRfcTBCShaNU0cIll43IB9lTJfn5YwWy4TWzDGDYB87PQvSgRx1jLb%2BOq4oVM7u5SuTPkCcE6TUBLdkhErhBx012T5sZPyj8%2Bl81ze%2Bmh00pfhO7GbLb9DxV7CVDCErukE%2FFDDhbpQKRe%2B4zfyWE%2FsAFUlOMEGHVPM0merS%2FN3Vbb6JDuIoHKnzvOfEn&X-Amz-Signature=5f89566434befd5aca5a3f26293ecdd536d1f2b96424e09e40c272640f05a4e5&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBFYT26C%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010733Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJHMEUCIAqIy6xD5O2ZfSGKmEZ003z0N57f39fhIK8gEjmFNznEAiEAriNXXcpTCcFOrCe%2BV56ATmqueP81j2JKb3OFu3T%2FoFQqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOo3NEnAljAvgZPTAyrcAwuuzEeW%2FKsnw%2FC2Mq2agQiCZbqASnD8nkG7dgonJO%2BAsA2w9XkSGzMDFkzvwNGXK2fHw8UhPn31u5ktwzEnXhhXVgQBR40%2BqD7U0dz%2FV%2FSsglXNF4gu%2FXXUhGkYBXMraXBqzFKMQkAcloUa94ky2heYVAlQ0FOg2dSVnt6On76ZNPo331e%2BnwFOm3bHx0YtHgQJF41oMYYXGnoKLir64LnRt2SPmABPNBi6RQP5yHJh0xg6S34S%2BbS8GZ%2FcAfhgjEQ6ABW6b6WM5sxruZderIHNBfN0Mct04vN60I9bMW%2BDRbkWQ2by9JR9a9nbMkSizNVltYMpGhg9Jz1BIEElBwnAvcDD%2FLczdJeeme0WLNBP2ZHRBzt6If5uCJy5NI0LgNbzJeCqq%2FI6P%2Fe%2BVOumhg6Jj1B7uOMa%2FDRvMHdyP4DmwNJTomCBoH8PmFNBwmd07%2FhklyExr8usXlsoltXkJQtQQ5XP%2Fw9iM3AB1w3RT%2FNXWL5VFHeecjqZlkeGNmRDsdM4TWvcGoYmo%2FC3tMoJDAJKMZagiieoYfg2wMZAIFRTHbGB1antXMj7G0FlZABuwlfv8dz7IXuLHpD7z570NHz%2FCptm9rB2Ryyg0UFB9SiW6Zy0uZdJE0LfrFJRMP%2B%2Bmr0GOqUBmxEBJM2IGAFssll0vQK9dfYe1znhpHkzuRfcTBCShaNU0cIll43IB9lTJfn5YwWy4TWzDGDYB87PQvSgRx1jLb%2BOq4oVM7u5SuTPkCcE6TUBLdkhErhBx012T5sZPyj8%2Bl81ze%2Bmh00pfhO7GbLb9DxV7CVDCErukE%2FFDDhbpQKRe%2B4zfyWE%2FsAFUlOMEGHVPM0merS%2FN3Vbb6JDuIoHKnzvOfEn&X-Amz-Signature=115beb8b8f15a8aa45bc8615dc05f14e83bcd2f1785c43df65ab95f3c4949dfe&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBFYT26C%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010733Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJHMEUCIAqIy6xD5O2ZfSGKmEZ003z0N57f39fhIK8gEjmFNznEAiEAriNXXcpTCcFOrCe%2BV56ATmqueP81j2JKb3OFu3T%2FoFQqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOo3NEnAljAvgZPTAyrcAwuuzEeW%2FKsnw%2FC2Mq2agQiCZbqASnD8nkG7dgonJO%2BAsA2w9XkSGzMDFkzvwNGXK2fHw8UhPn31u5ktwzEnXhhXVgQBR40%2BqD7U0dz%2FV%2FSsglXNF4gu%2FXXUhGkYBXMraXBqzFKMQkAcloUa94ky2heYVAlQ0FOg2dSVnt6On76ZNPo331e%2BnwFOm3bHx0YtHgQJF41oMYYXGnoKLir64LnRt2SPmABPNBi6RQP5yHJh0xg6S34S%2BbS8GZ%2FcAfhgjEQ6ABW6b6WM5sxruZderIHNBfN0Mct04vN60I9bMW%2BDRbkWQ2by9JR9a9nbMkSizNVltYMpGhg9Jz1BIEElBwnAvcDD%2FLczdJeeme0WLNBP2ZHRBzt6If5uCJy5NI0LgNbzJeCqq%2FI6P%2Fe%2BVOumhg6Jj1B7uOMa%2FDRvMHdyP4DmwNJTomCBoH8PmFNBwmd07%2FhklyExr8usXlsoltXkJQtQQ5XP%2Fw9iM3AB1w3RT%2FNXWL5VFHeecjqZlkeGNmRDsdM4TWvcGoYmo%2FC3tMoJDAJKMZagiieoYfg2wMZAIFRTHbGB1antXMj7G0FlZABuwlfv8dz7IXuLHpD7z570NHz%2FCptm9rB2Ryyg0UFB9SiW6Zy0uZdJE0LfrFJRMP%2B%2Bmr0GOqUBmxEBJM2IGAFssll0vQK9dfYe1znhpHkzuRfcTBCShaNU0cIll43IB9lTJfn5YwWy4TWzDGDYB87PQvSgRx1jLb%2BOq4oVM7u5SuTPkCcE6TUBLdkhErhBx012T5sZPyj8%2Bl81ze%2Bmh00pfhO7GbLb9DxV7CVDCErukE%2FFDDhbpQKRe%2B4zfyWE%2FsAFUlOMEGHVPM0merS%2FN3Vbb6JDuIoHKnzvOfEn&X-Amz-Signature=671f880a4593bdbad35f19d18bb972167dd0e6c0d79f9ca620cce73d1d76d566&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S42FWNTK%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010733Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJGMEQCIFp7aOdNu2DDPUKFu7CiVVTuHLUtj%2FRkzt7Rqpt9UeNmAiAossjGGU%2B1i4PZPV1inzQL8f%2FfnMWbVGwi3hVXQKF2YSqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMAHUVN%2FZbMgHOACHEKtwDz1mNKsrERd2LYmTkO%2B81%2FfoF7b%2B4D1bMFGVbKjgcdCpu0zn8nvT1kcuJPaJ%2F9D1hwn5dhCrpjuKwa52ghua9T1UKy3Dkv7M6O8WMpIXqqiSDNTSRaR2wSA9jI%2BrQ0AdU%2FMIMc4TibDWl9Hc2wdDWJhtQDJ3JC%2Bc3umYEUBtX8dGOSfvS%2BrTK2QkUBCRnpZcFT8d%2BIDE1N2LIvwiA%2F35RsFTtV31FTQnF6nicVu2lcbOunvjfQFX%2F5L%2B%2B5K7WdmLxC1xLxgeF8Ix1yR7fzUohaCm3Bf1HmBtaxMVJzkDcaC76VIUrtaHQV1yNz1PvS8D3iIy92SF5PWgq8otlOfcadejmiggXNzyXSzcm3Sl0qGrNfUQ1vXVap3OpyRj3K8lh%2BNo8JFKDNpbpWCgbseWpO1uuD26EezNPvBaSELWlTpQ9i%2FH0DkPltnIuUTY%2FMxELI90xXwJ%2B1vvYcLETJYhb8JKvMTquihoSr80Q%2BqwQAsArJEJCb2dPfdy9%2B1Vsvv4nsPqwaOn1Ux%2FtJndaoCpDvJPpcDWvCVISpDNCSmF0P5PQQSnvCj%2FZsU%2FlCHoJWXv%2BCT%2BhtVzK72d%2FU%2FHdtgdFnAnA3CIbpX1sCv4ABaltGF2JQ%2BdXccIY9HNBbrcw7b6avQY6pgH4k6pJhrQ%2BYXjgVJ%2FePouqV4PlpdrMM444qzAriM32%2F7K05BroWL5ZML38nj1FIjZg1qOXjCVGv8SY%2BglbrYQGl9z7iDV7KNxWyCD%2BIZW%2BTO04txxT7IQSFnZRJGegRqZj7IWzzRl3X5pCicgEP874pChgyPZCjL3GtON%2FKC9DayZQ9a0vyyZL3y70mzQ1PpFlpCM6HyqpQiix7SS0FyRpBmRYEEmZ&X-Amz-Signature=9b9ddbe4273296ec6379bd83cb28d2b047303b0aa30bf9bd12874ca03d632e48&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNROYXA7%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010740Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJGMEQCICs%2FZwQeMkDfSHYvvPfRXHlUh1Fz9hNoPCsPpir1w%2FfMAiAv4%2FpUjcLDn%2FlyWM%2Bo%2BKdcBLhyOa7AdRQGmPNGSifNPCqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMEdiO5aOuUZWcdQHIKtwD3epOfC1DvkmqVXrJ65oP7WmwNUlgCjlx%2BmKPP5LMjLAX10cOlVKcUt8tYWAAdUZ6q8Mcx%2FY8icTCbocepOrZ33GYJz1vDgpO7%2FCj7XVxFEducH3bxc4zdVI9Gq1RWTAp81Mg%2B46G3qHddxbLkwqaDtkynZZZNZ0AXROsrdw%2BB2O2SgkSNkwq3A9aopKS5QNQEzvzeMldnJKmADntyd9xdEs8Okr0R69wT9TRhAumNwZfP5fPvPFwd%2FmvYruEbcF7h0YenHJFXqo%2B1sT3IWrwDCXAaPL%2BJjt3jLy%2FT9Eh%2FUKgSO8p54uxW%2BB8S0tJGK7Wq5jcSRmx0l9MhEUgDHsNJFhCMS9d0t4XMtlsv7kXBpoo05eZx0%2BV7tt4bMNHbXXB5AbMYKH2OZeTO6UBV%2FR4ihUjkUXM63NQTXCRs1%2F%2FwTj0kN2GYuowMeRVhTrhX0paMNY8%2BOV%2FSDIhfikLt0kMR0QiyyYTAM%2BMFJPLCqajCHNIvSyhw2sUiEIwJW3BkkXrUBmLn6sAtbcgQ%2B2bSV%2Fv2ZpFrLM8u038PGk0M4hjo1iVqPm0dRJA6lg1xt7wdpoFqMHoNwrJJWIhcDfooy9F5hvDzHKfCIu5wjT81%2B2E9jEAWsm7EpQ8ulOjDggwwr6avQY6pgFpRKx456B8RT2%2B5phCEHb62igIfW5eUdnPRInTRaZwJnq52I9tD9POfxSRi6JlKy9KRD6ke4eZfs4VPBtviaec0lBre9ihJC6L5Zzq9HIHX4HRWvjCdAvmeORYkvAfR4dDyDxFdlMQMo8i7AX5FhrfaqsAfPeDMN%2BLUNpgXSM8Hnw5yaJCqhPnhwlB0RR8b0iom8sLSwlXFi%2FK9ZS0FL7kU7sxN3wH&X-Amz-Signature=de243bf4fa40f98a36ff6f00ef01c312c29a76938c1775fc38767a4e82f74a06&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBFYT26C%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010733Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJHMEUCIAqIy6xD5O2ZfSGKmEZ003z0N57f39fhIK8gEjmFNznEAiEAriNXXcpTCcFOrCe%2BV56ATmqueP81j2JKb3OFu3T%2FoFQqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOo3NEnAljAvgZPTAyrcAwuuzEeW%2FKsnw%2FC2Mq2agQiCZbqASnD8nkG7dgonJO%2BAsA2w9XkSGzMDFkzvwNGXK2fHw8UhPn31u5ktwzEnXhhXVgQBR40%2BqD7U0dz%2FV%2FSsglXNF4gu%2FXXUhGkYBXMraXBqzFKMQkAcloUa94ky2heYVAlQ0FOg2dSVnt6On76ZNPo331e%2BnwFOm3bHx0YtHgQJF41oMYYXGnoKLir64LnRt2SPmABPNBi6RQP5yHJh0xg6S34S%2BbS8GZ%2FcAfhgjEQ6ABW6b6WM5sxruZderIHNBfN0Mct04vN60I9bMW%2BDRbkWQ2by9JR9a9nbMkSizNVltYMpGhg9Jz1BIEElBwnAvcDD%2FLczdJeeme0WLNBP2ZHRBzt6If5uCJy5NI0LgNbzJeCqq%2FI6P%2Fe%2BVOumhg6Jj1B7uOMa%2FDRvMHdyP4DmwNJTomCBoH8PmFNBwmd07%2FhklyExr8usXlsoltXkJQtQQ5XP%2Fw9iM3AB1w3RT%2FNXWL5VFHeecjqZlkeGNmRDsdM4TWvcGoYmo%2FC3tMoJDAJKMZagiieoYfg2wMZAIFRTHbGB1antXMj7G0FlZABuwlfv8dz7IXuLHpD7z570NHz%2FCptm9rB2Ryyg0UFB9SiW6Zy0uZdJE0LfrFJRMP%2B%2Bmr0GOqUBmxEBJM2IGAFssll0vQK9dfYe1znhpHkzuRfcTBCShaNU0cIll43IB9lTJfn5YwWy4TWzDGDYB87PQvSgRx1jLb%2BOq4oVM7u5SuTPkCcE6TUBLdkhErhBx012T5sZPyj8%2Bl81ze%2Bmh00pfhO7GbLb9DxV7CVDCErukE%2FFDDhbpQKRe%2B4zfyWE%2FsAFUlOMEGHVPM0merS%2FN3Vbb6JDuIoHKnzvOfEn&X-Amz-Signature=3baf22c64d1af6d7af4b459e356a4c259c768ae20ac691eccf71c8919e412703&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBFYT26C%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010733Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJHMEUCIAqIy6xD5O2ZfSGKmEZ003z0N57f39fhIK8gEjmFNznEAiEAriNXXcpTCcFOrCe%2BV56ATmqueP81j2JKb3OFu3T%2FoFQqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOo3NEnAljAvgZPTAyrcAwuuzEeW%2FKsnw%2FC2Mq2agQiCZbqASnD8nkG7dgonJO%2BAsA2w9XkSGzMDFkzvwNGXK2fHw8UhPn31u5ktwzEnXhhXVgQBR40%2BqD7U0dz%2FV%2FSsglXNF4gu%2FXXUhGkYBXMraXBqzFKMQkAcloUa94ky2heYVAlQ0FOg2dSVnt6On76ZNPo331e%2BnwFOm3bHx0YtHgQJF41oMYYXGnoKLir64LnRt2SPmABPNBi6RQP5yHJh0xg6S34S%2BbS8GZ%2FcAfhgjEQ6ABW6b6WM5sxruZderIHNBfN0Mct04vN60I9bMW%2BDRbkWQ2by9JR9a9nbMkSizNVltYMpGhg9Jz1BIEElBwnAvcDD%2FLczdJeeme0WLNBP2ZHRBzt6If5uCJy5NI0LgNbzJeCqq%2FI6P%2Fe%2BVOumhg6Jj1B7uOMa%2FDRvMHdyP4DmwNJTomCBoH8PmFNBwmd07%2FhklyExr8usXlsoltXkJQtQQ5XP%2Fw9iM3AB1w3RT%2FNXWL5VFHeecjqZlkeGNmRDsdM4TWvcGoYmo%2FC3tMoJDAJKMZagiieoYfg2wMZAIFRTHbGB1antXMj7G0FlZABuwlfv8dz7IXuLHpD7z570NHz%2FCptm9rB2Ryyg0UFB9SiW6Zy0uZdJE0LfrFJRMP%2B%2Bmr0GOqUBmxEBJM2IGAFssll0vQK9dfYe1znhpHkzuRfcTBCShaNU0cIll43IB9lTJfn5YwWy4TWzDGDYB87PQvSgRx1jLb%2BOq4oVM7u5SuTPkCcE6TUBLdkhErhBx012T5sZPyj8%2Bl81ze%2Bmh00pfhO7GbLb9DxV7CVDCErukE%2FFDDhbpQKRe%2B4zfyWE%2FsAFUlOMEGHVPM0merS%2FN3Vbb6JDuIoHKnzvOfEn&X-Amz-Signature=4c5b154adfb8c1b7a03ec1ac93aa2162d7db2167ce78f83d4c413c3461482716&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBFYT26C%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010733Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJHMEUCIAqIy6xD5O2ZfSGKmEZ003z0N57f39fhIK8gEjmFNznEAiEAriNXXcpTCcFOrCe%2BV56ATmqueP81j2JKb3OFu3T%2FoFQqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOo3NEnAljAvgZPTAyrcAwuuzEeW%2FKsnw%2FC2Mq2agQiCZbqASnD8nkG7dgonJO%2BAsA2w9XkSGzMDFkzvwNGXK2fHw8UhPn31u5ktwzEnXhhXVgQBR40%2BqD7U0dz%2FV%2FSsglXNF4gu%2FXXUhGkYBXMraXBqzFKMQkAcloUa94ky2heYVAlQ0FOg2dSVnt6On76ZNPo331e%2BnwFOm3bHx0YtHgQJF41oMYYXGnoKLir64LnRt2SPmABPNBi6RQP5yHJh0xg6S34S%2BbS8GZ%2FcAfhgjEQ6ABW6b6WM5sxruZderIHNBfN0Mct04vN60I9bMW%2BDRbkWQ2by9JR9a9nbMkSizNVltYMpGhg9Jz1BIEElBwnAvcDD%2FLczdJeeme0WLNBP2ZHRBzt6If5uCJy5NI0LgNbzJeCqq%2FI6P%2Fe%2BVOumhg6Jj1B7uOMa%2FDRvMHdyP4DmwNJTomCBoH8PmFNBwmd07%2FhklyExr8usXlsoltXkJQtQQ5XP%2Fw9iM3AB1w3RT%2FNXWL5VFHeecjqZlkeGNmRDsdM4TWvcGoYmo%2FC3tMoJDAJKMZagiieoYfg2wMZAIFRTHbGB1antXMj7G0FlZABuwlfv8dz7IXuLHpD7z570NHz%2FCptm9rB2Ryyg0UFB9SiW6Zy0uZdJE0LfrFJRMP%2B%2Bmr0GOqUBmxEBJM2IGAFssll0vQK9dfYe1znhpHkzuRfcTBCShaNU0cIll43IB9lTJfn5YwWy4TWzDGDYB87PQvSgRx1jLb%2BOq4oVM7u5SuTPkCcE6TUBLdkhErhBx012T5sZPyj8%2Bl81ze%2Bmh00pfhO7GbLb9DxV7CVDCErukE%2FFDDhbpQKRe%2B4zfyWE%2FsAFUlOMEGHVPM0merS%2FN3Vbb6JDuIoHKnzvOfEn&X-Amz-Signature=1cbc400c6ca68fad6e38c0a848a117967e4be15d42b19bdb80d86cb15f876f2b&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBFYT26C%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010733Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJHMEUCIAqIy6xD5O2ZfSGKmEZ003z0N57f39fhIK8gEjmFNznEAiEAriNXXcpTCcFOrCe%2BV56ATmqueP81j2JKb3OFu3T%2FoFQqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOo3NEnAljAvgZPTAyrcAwuuzEeW%2FKsnw%2FC2Mq2agQiCZbqASnD8nkG7dgonJO%2BAsA2w9XkSGzMDFkzvwNGXK2fHw8UhPn31u5ktwzEnXhhXVgQBR40%2BqD7U0dz%2FV%2FSsglXNF4gu%2FXXUhGkYBXMraXBqzFKMQkAcloUa94ky2heYVAlQ0FOg2dSVnt6On76ZNPo331e%2BnwFOm3bHx0YtHgQJF41oMYYXGnoKLir64LnRt2SPmABPNBi6RQP5yHJh0xg6S34S%2BbS8GZ%2FcAfhgjEQ6ABW6b6WM5sxruZderIHNBfN0Mct04vN60I9bMW%2BDRbkWQ2by9JR9a9nbMkSizNVltYMpGhg9Jz1BIEElBwnAvcDD%2FLczdJeeme0WLNBP2ZHRBzt6If5uCJy5NI0LgNbzJeCqq%2FI6P%2Fe%2BVOumhg6Jj1B7uOMa%2FDRvMHdyP4DmwNJTomCBoH8PmFNBwmd07%2FhklyExr8usXlsoltXkJQtQQ5XP%2Fw9iM3AB1w3RT%2FNXWL5VFHeecjqZlkeGNmRDsdM4TWvcGoYmo%2FC3tMoJDAJKMZagiieoYfg2wMZAIFRTHbGB1antXMj7G0FlZABuwlfv8dz7IXuLHpD7z570NHz%2FCptm9rB2Ryyg0UFB9SiW6Zy0uZdJE0LfrFJRMP%2B%2Bmr0GOqUBmxEBJM2IGAFssll0vQK9dfYe1znhpHkzuRfcTBCShaNU0cIll43IB9lTJfn5YwWy4TWzDGDYB87PQvSgRx1jLb%2BOq4oVM7u5SuTPkCcE6TUBLdkhErhBx012T5sZPyj8%2Bl81ze%2Bmh00pfhO7GbLb9DxV7CVDCErukE%2FFDDhbpQKRe%2B4zfyWE%2FsAFUlOMEGHVPM0merS%2FN3Vbb6JDuIoHKnzvOfEn&X-Amz-Signature=9fb36b806c39a82681dce7cf4b4a731cacab1a1cc00ce153cf4229718e56b7f7&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
