

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664LJ6QKJG%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIGVkgQMQHfuAcAM%2BCxt5dWQKdXIwOL2SZPq%2F69om3TQBAiAt9CcurY686%2Buzuw9stUdtAd71JhI%2B%2B9cc7X%2F2uuLBSCr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMwhgFQSbqEkLNYXwOKtwDcZ5Rq%2FvqYJyxtx%2Fruiz%2FzNIxt4WeWQp4XXGKhy5ooBLPFg6NYuzXZxNRgQSWLQ0e8Mf%2F6DUjU7doDdgWSWDXNAwzKqRwBhSnq%2FDlNyrU6j9I9fviDDjUitef3JIeMA1LQjXG5qEdyz4DxIaamckhQRDbAU6nIeAuCilO5j0Nn%2BNprAHIa6oy9FDUAm5Mnt4i%2FJ%2FOJMQzoVAaYZCkgEmqixgO3S4Sq2Qlwirh%2B784mPSigHh7pEQfFJUP1Bg5AB%2FOGJS4qqrLawujvaaLRXBKTjXAn7bCIT9xz%2F0FqxHS8Wbt8blI6xqmbClnJXpnp3pHAIRB2gxhzhIrkKvcXRKOOo9oNEqbj1cWYteWVP4LeLqNY7jVTJiCJDdJBu6Ag4esG3m82887%2BGoz6rzXWeA5vPtjrbXT2eeL%2FKOzqbGvk0%2B%2FdbvSA8YituQADEzFmzZviKXgrgLmL2AFY8%2FjOSNYyjmxTnbvUUHZEY%2Fuh9EKcxFQY01xf96SuBHyjXUkJ3FgAFP9yXC2mG0AFEWWsdkm8nCmMBX2a52WZR697mzYNbTme2TmU3SJESQDXVTs8DIqkZ6DA4ljTFbT42lJKhnde7sQjzfu5JROJEz%2FszSKBQiz6Z6W76HJg0LYu7cw87qOvQY6pgEuYSTOpyZ3GjyjXr8tD5E0M4NkKmy0%2FV85%2BjcaUcseMZkrP9A9fNqDohuL4yL1srjCXKdm6%2F26qBy9DxqyJgJ5KRAxTWXT%2BKb0541KTrgubnuRRpvMuT9wi4uF44WaQpSFK2GrT0ZBIoM4lxj6mbVQGr%2BjBu1htSOijA6KIOrn8pKRU%2BEjSGFNakmtAtoJjRoR6vPOkh9QsuQcJIwSXLOc7lRp%2FzdD&X-Amz-Signature=277c4bdc5a312df08eb7a7d8032dcdafd661c85f83144357aa0d82026a55b991&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664LJ6QKJG%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIGVkgQMQHfuAcAM%2BCxt5dWQKdXIwOL2SZPq%2F69om3TQBAiAt9CcurY686%2Buzuw9stUdtAd71JhI%2B%2B9cc7X%2F2uuLBSCr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMwhgFQSbqEkLNYXwOKtwDcZ5Rq%2FvqYJyxtx%2Fruiz%2FzNIxt4WeWQp4XXGKhy5ooBLPFg6NYuzXZxNRgQSWLQ0e8Mf%2F6DUjU7doDdgWSWDXNAwzKqRwBhSnq%2FDlNyrU6j9I9fviDDjUitef3JIeMA1LQjXG5qEdyz4DxIaamckhQRDbAU6nIeAuCilO5j0Nn%2BNprAHIa6oy9FDUAm5Mnt4i%2FJ%2FOJMQzoVAaYZCkgEmqixgO3S4Sq2Qlwirh%2B784mPSigHh7pEQfFJUP1Bg5AB%2FOGJS4qqrLawujvaaLRXBKTjXAn7bCIT9xz%2F0FqxHS8Wbt8blI6xqmbClnJXpnp3pHAIRB2gxhzhIrkKvcXRKOOo9oNEqbj1cWYteWVP4LeLqNY7jVTJiCJDdJBu6Ag4esG3m82887%2BGoz6rzXWeA5vPtjrbXT2eeL%2FKOzqbGvk0%2B%2FdbvSA8YituQADEzFmzZviKXgrgLmL2AFY8%2FjOSNYyjmxTnbvUUHZEY%2Fuh9EKcxFQY01xf96SuBHyjXUkJ3FgAFP9yXC2mG0AFEWWsdkm8nCmMBX2a52WZR697mzYNbTme2TmU3SJESQDXVTs8DIqkZ6DA4ljTFbT42lJKhnde7sQjzfu5JROJEz%2FszSKBQiz6Z6W76HJg0LYu7cw87qOvQY6pgEuYSTOpyZ3GjyjXr8tD5E0M4NkKmy0%2FV85%2BjcaUcseMZkrP9A9fNqDohuL4yL1srjCXKdm6%2F26qBy9DxqyJgJ5KRAxTWXT%2BKb0541KTrgubnuRRpvMuT9wi4uF44WaQpSFK2GrT0ZBIoM4lxj6mbVQGr%2BjBu1htSOijA6KIOrn8pKRU%2BEjSGFNakmtAtoJjRoR6vPOkh9QsuQcJIwSXLOc7lRp%2FzdD&X-Amz-Signature=350d5292ff0517c19daab4159fc0512b21f8048e0cb940e71dceada2f8e46978&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664LJ6QKJG%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIGVkgQMQHfuAcAM%2BCxt5dWQKdXIwOL2SZPq%2F69om3TQBAiAt9CcurY686%2Buzuw9stUdtAd71JhI%2B%2B9cc7X%2F2uuLBSCr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMwhgFQSbqEkLNYXwOKtwDcZ5Rq%2FvqYJyxtx%2Fruiz%2FzNIxt4WeWQp4XXGKhy5ooBLPFg6NYuzXZxNRgQSWLQ0e8Mf%2F6DUjU7doDdgWSWDXNAwzKqRwBhSnq%2FDlNyrU6j9I9fviDDjUitef3JIeMA1LQjXG5qEdyz4DxIaamckhQRDbAU6nIeAuCilO5j0Nn%2BNprAHIa6oy9FDUAm5Mnt4i%2FJ%2FOJMQzoVAaYZCkgEmqixgO3S4Sq2Qlwirh%2B784mPSigHh7pEQfFJUP1Bg5AB%2FOGJS4qqrLawujvaaLRXBKTjXAn7bCIT9xz%2F0FqxHS8Wbt8blI6xqmbClnJXpnp3pHAIRB2gxhzhIrkKvcXRKOOo9oNEqbj1cWYteWVP4LeLqNY7jVTJiCJDdJBu6Ag4esG3m82887%2BGoz6rzXWeA5vPtjrbXT2eeL%2FKOzqbGvk0%2B%2FdbvSA8YituQADEzFmzZviKXgrgLmL2AFY8%2FjOSNYyjmxTnbvUUHZEY%2Fuh9EKcxFQY01xf96SuBHyjXUkJ3FgAFP9yXC2mG0AFEWWsdkm8nCmMBX2a52WZR697mzYNbTme2TmU3SJESQDXVTs8DIqkZ6DA4ljTFbT42lJKhnde7sQjzfu5JROJEz%2FszSKBQiz6Z6W76HJg0LYu7cw87qOvQY6pgEuYSTOpyZ3GjyjXr8tD5E0M4NkKmy0%2FV85%2BjcaUcseMZkrP9A9fNqDohuL4yL1srjCXKdm6%2F26qBy9DxqyJgJ5KRAxTWXT%2BKb0541KTrgubnuRRpvMuT9wi4uF44WaQpSFK2GrT0ZBIoM4lxj6mbVQGr%2BjBu1htSOijA6KIOrn8pKRU%2BEjSGFNakmtAtoJjRoR6vPOkh9QsuQcJIwSXLOc7lRp%2FzdD&X-Amz-Signature=c41cd8cd1dac42f2918674e1039ec5727877ed6bddf7272a8faf61aed718073a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664XAZIJDH%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQDTFB4x4IO8B7QkRg0veiDuWh6zaMMhKnJgDQB4%2FssdDAIhAPjHgLZ6sB9Bpw%2FOBDqVGXDrJPCK0wOI24%2BmT8RJoiCFKv8DCEoQABoMNjM3NDIzMTgzODA1IgwJesTbklAVhg4Hppkq3AM3hO%2FAJYQUzOMnNalWiUWnXJ%2FQhm9cBCHd%2FUS0sACneSx2Jn0erJkjzOHmav18wKhkcuqDVowwsoYY1FPivZ24OVeXaoFPhvS1DlkcNbv8Tj47zB2dZSZh8zoRFnIFWDpsGUbyYMySH6GkwKGmVKaCaIHA4pXSzxFb0%2Fp%2B7SesaySMMwpViKpTYrc8j8LVNdXgdNubTY7vEOkDLPcQAmi2XknSpD%2Fwl%2B3eVD4qCu9wtWdtkqwZKCnLE2kXsctrKRtRAHPHYu4j9aw0OiEijGBEA1dgAN0P7VeCNE4esfi5y4liGDSbfRUGx22xI8bY85fbwNnqHrWgIIy0aUF8DChFHC%2BvqaQZX0yeXUKJBr3ePPTU6S2ZR%2FYHsj2Oir0qUqdaa72lYa9NXHZEngjiErIE2O3alWACYX579pojybtLxkCigHRcr%2FIAOZFT1j3%2FtEQWboi%2Fry5BTGfD6wG5arcmiVoJvW1y8pQjnjvnDILQukxLKu1ePSEQhAAKDax7GSWBtnPLYCW5naa0oWtoxzmSF3hhZ%2FqhJ2y4y4TCAgOQ3tJWESFIkQCeExdpcBS5FGgeSkP7qBmYr6L2EjoFzEbJe02ZMxN1P%2FrXSLUe%2BeErgq%2BVQ4RDjYFqerW08zDnuo69BjqkAWrnjbQVUiwyJzVD%2FsQLI1MRPECex5qTGqQ7JMJpt3KdWp6e3WetFIVnUB4YEJJ7BCYcVS4P2QIL%2BiTlcPrbKR8YC%2B0REirE3xVGUVnPPF2ez8paDJNGpvbTOXWGhIccTt6eZdjMzTlsVmbuRIR%2Fe78N2POr%2BJH%2BiexD84D%2F1mUJ92b9yQdU0e5hfuLO5YoHDENTftFHqyKsiKmWrGlWo53WqHZ%2F&X-Amz-Signature=c2e8aaae86df5efa48f5983ff2df04b1d72ce2e4176488fe3ea08408647ca4e6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UAV54D4Q%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJGMEQCIFLwa%2BmhOJr4NaiHozYA4hecMvKpd%2FpI7WLeqkGrDapyAiBSsk%2BIVKTPMlKqheg8IBx4w%2FI8GzUIZf0seLkTmLeuVir%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMgHMd4KDGEChaBXreKtwDetaumh%2F%2BO9rJMASSe6r8RXWYL602yigJbrw4iCUd5bjjraQRQq3OA9U6SdDzEhWi5IBROa7zu%2FLoMI6%2Bn533vEnOB9C1IOq4beP99wTOvzHIVZFq%2BX4YJLQba4Ex3GXTloQv1Gjc%2FBlNlcCLkP0ibmh4pF6nqvBqTuX1rIhT%2FTH1HA0s5GSh5n%2BA03Cj2R%2Bs5%2BDA1aLwSDepqcYQpZAcjFrsFyObOoTzkVtaOUX8ZmxlUt4PDE7ZIqD3QBRTg1HXThanNsBSIucDUUFFizlCf4%2FtQOt06OZh3WVDnNSq7SAbRmtC0h5vFDCB7AiNDyo2Yh%2F8TycZI7doBMJsVtZTEK%2FrA0V9zVXOs6qHbx09anOI4e2dlPqr1BVPttrJ9oIqHYMGy7Gs%2BBZJg8tf%2FY4b1nUizBU%2FxppAnn1Lxyw7i8RKw0S3%2BgyFuBrcnRAjB9k9xopW%2FwOMCBnViK%2BQ6NCnnFS5NNNmlFQBCr4kb5GfYjS5APCJK3nveyBsGQL5HP%2F%2FfQcp8w5rf5FbtVTtCsC3P5u4AHSwRcsnLQljlbbFL8zOfydWWHqxPgYMWvSPxO%2F6QErNFIdWTxUejgDWhx3VdaRM8r7k88POOX07NQKihCbX9EBOyqTalbLZqb4wmLqOvQY6pgE2sDa3g0h1%2BznYBAdGuvWllV93wKerOU5UWVbAnf%2BCzL56urNP5zHaYLfypRbsRremOEZQFTweqYqda902OgwKfCwPZ8RP03HT1CApdI5qKOBlvvTd2L%2BIXQ%2FBj35Dnj9VzErm4F6Ta0nJhPow1Sy3Y%2BM9XYeC6Qfo1rpnuXJ3hROToW129DppRiPouYaIuhjUglxIrDvj62e%2FPvyfHdhBeQrwESAI&X-Amz-Signature=aa7aa4459fb795286ebc2f565beb8e90137a591e5b417ff81b04e1481850f411&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664LJ6QKJG%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIGVkgQMQHfuAcAM%2BCxt5dWQKdXIwOL2SZPq%2F69om3TQBAiAt9CcurY686%2Buzuw9stUdtAd71JhI%2B%2B9cc7X%2F2uuLBSCr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMwhgFQSbqEkLNYXwOKtwDcZ5Rq%2FvqYJyxtx%2Fruiz%2FzNIxt4WeWQp4XXGKhy5ooBLPFg6NYuzXZxNRgQSWLQ0e8Mf%2F6DUjU7doDdgWSWDXNAwzKqRwBhSnq%2FDlNyrU6j9I9fviDDjUitef3JIeMA1LQjXG5qEdyz4DxIaamckhQRDbAU6nIeAuCilO5j0Nn%2BNprAHIa6oy9FDUAm5Mnt4i%2FJ%2FOJMQzoVAaYZCkgEmqixgO3S4Sq2Qlwirh%2B784mPSigHh7pEQfFJUP1Bg5AB%2FOGJS4qqrLawujvaaLRXBKTjXAn7bCIT9xz%2F0FqxHS8Wbt8blI6xqmbClnJXpnp3pHAIRB2gxhzhIrkKvcXRKOOo9oNEqbj1cWYteWVP4LeLqNY7jVTJiCJDdJBu6Ag4esG3m82887%2BGoz6rzXWeA5vPtjrbXT2eeL%2FKOzqbGvk0%2B%2FdbvSA8YituQADEzFmzZviKXgrgLmL2AFY8%2FjOSNYyjmxTnbvUUHZEY%2Fuh9EKcxFQY01xf96SuBHyjXUkJ3FgAFP9yXC2mG0AFEWWsdkm8nCmMBX2a52WZR697mzYNbTme2TmU3SJESQDXVTs8DIqkZ6DA4ljTFbT42lJKhnde7sQjzfu5JROJEz%2FszSKBQiz6Z6W76HJg0LYu7cw87qOvQY6pgEuYSTOpyZ3GjyjXr8tD5E0M4NkKmy0%2FV85%2BjcaUcseMZkrP9A9fNqDohuL4yL1srjCXKdm6%2F26qBy9DxqyJgJ5KRAxTWXT%2BKb0541KTrgubnuRRpvMuT9wi4uF44WaQpSFK2GrT0ZBIoM4lxj6mbVQGr%2BjBu1htSOijA6KIOrn8pKRU%2BEjSGFNakmtAtoJjRoR6vPOkh9QsuQcJIwSXLOc7lRp%2FzdD&X-Amz-Signature=216bb636446daca8b41686d6f9d7fbe358ee2c22d0f524fc8424baa855a60592&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664LJ6QKJG%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIGVkgQMQHfuAcAM%2BCxt5dWQKdXIwOL2SZPq%2F69om3TQBAiAt9CcurY686%2Buzuw9stUdtAd71JhI%2B%2B9cc7X%2F2uuLBSCr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMwhgFQSbqEkLNYXwOKtwDcZ5Rq%2FvqYJyxtx%2Fruiz%2FzNIxt4WeWQp4XXGKhy5ooBLPFg6NYuzXZxNRgQSWLQ0e8Mf%2F6DUjU7doDdgWSWDXNAwzKqRwBhSnq%2FDlNyrU6j9I9fviDDjUitef3JIeMA1LQjXG5qEdyz4DxIaamckhQRDbAU6nIeAuCilO5j0Nn%2BNprAHIa6oy9FDUAm5Mnt4i%2FJ%2FOJMQzoVAaYZCkgEmqixgO3S4Sq2Qlwirh%2B784mPSigHh7pEQfFJUP1Bg5AB%2FOGJS4qqrLawujvaaLRXBKTjXAn7bCIT9xz%2F0FqxHS8Wbt8blI6xqmbClnJXpnp3pHAIRB2gxhzhIrkKvcXRKOOo9oNEqbj1cWYteWVP4LeLqNY7jVTJiCJDdJBu6Ag4esG3m82887%2BGoz6rzXWeA5vPtjrbXT2eeL%2FKOzqbGvk0%2B%2FdbvSA8YituQADEzFmzZviKXgrgLmL2AFY8%2FjOSNYyjmxTnbvUUHZEY%2Fuh9EKcxFQY01xf96SuBHyjXUkJ3FgAFP9yXC2mG0AFEWWsdkm8nCmMBX2a52WZR697mzYNbTme2TmU3SJESQDXVTs8DIqkZ6DA4ljTFbT42lJKhnde7sQjzfu5JROJEz%2FszSKBQiz6Z6W76HJg0LYu7cw87qOvQY6pgEuYSTOpyZ3GjyjXr8tD5E0M4NkKmy0%2FV85%2BjcaUcseMZkrP9A9fNqDohuL4yL1srjCXKdm6%2F26qBy9DxqyJgJ5KRAxTWXT%2BKb0541KTrgubnuRRpvMuT9wi4uF44WaQpSFK2GrT0ZBIoM4lxj6mbVQGr%2BjBu1htSOijA6KIOrn8pKRU%2BEjSGFNakmtAtoJjRoR6vPOkh9QsuQcJIwSXLOc7lRp%2FzdD&X-Amz-Signature=bb794cc07ac1ceddfd090ff4d4e120d4fafb8dad8b391f2faa4b175aaccf9fed&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664LJ6QKJG%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIGVkgQMQHfuAcAM%2BCxt5dWQKdXIwOL2SZPq%2F69om3TQBAiAt9CcurY686%2Buzuw9stUdtAd71JhI%2B%2B9cc7X%2F2uuLBSCr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMwhgFQSbqEkLNYXwOKtwDcZ5Rq%2FvqYJyxtx%2Fruiz%2FzNIxt4WeWQp4XXGKhy5ooBLPFg6NYuzXZxNRgQSWLQ0e8Mf%2F6DUjU7doDdgWSWDXNAwzKqRwBhSnq%2FDlNyrU6j9I9fviDDjUitef3JIeMA1LQjXG5qEdyz4DxIaamckhQRDbAU6nIeAuCilO5j0Nn%2BNprAHIa6oy9FDUAm5Mnt4i%2FJ%2FOJMQzoVAaYZCkgEmqixgO3S4Sq2Qlwirh%2B784mPSigHh7pEQfFJUP1Bg5AB%2FOGJS4qqrLawujvaaLRXBKTjXAn7bCIT9xz%2F0FqxHS8Wbt8blI6xqmbClnJXpnp3pHAIRB2gxhzhIrkKvcXRKOOo9oNEqbj1cWYteWVP4LeLqNY7jVTJiCJDdJBu6Ag4esG3m82887%2BGoz6rzXWeA5vPtjrbXT2eeL%2FKOzqbGvk0%2B%2FdbvSA8YituQADEzFmzZviKXgrgLmL2AFY8%2FjOSNYyjmxTnbvUUHZEY%2Fuh9EKcxFQY01xf96SuBHyjXUkJ3FgAFP9yXC2mG0AFEWWsdkm8nCmMBX2a52WZR697mzYNbTme2TmU3SJESQDXVTs8DIqkZ6DA4ljTFbT42lJKhnde7sQjzfu5JROJEz%2FszSKBQiz6Z6W76HJg0LYu7cw87qOvQY6pgEuYSTOpyZ3GjyjXr8tD5E0M4NkKmy0%2FV85%2BjcaUcseMZkrP9A9fNqDohuL4yL1srjCXKdm6%2F26qBy9DxqyJgJ5KRAxTWXT%2BKb0541KTrgubnuRRpvMuT9wi4uF44WaQpSFK2GrT0ZBIoM4lxj6mbVQGr%2BjBu1htSOijA6KIOrn8pKRU%2BEjSGFNakmtAtoJjRoR6vPOkh9QsuQcJIwSXLOc7lRp%2FzdD&X-Amz-Signature=e787623afa319d0aadc45548465ab68707527909f2efd2da4393f6a2d56be149&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664LJ6QKJG%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIGVkgQMQHfuAcAM%2BCxt5dWQKdXIwOL2SZPq%2F69om3TQBAiAt9CcurY686%2Buzuw9stUdtAd71JhI%2B%2B9cc7X%2F2uuLBSCr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMwhgFQSbqEkLNYXwOKtwDcZ5Rq%2FvqYJyxtx%2Fruiz%2FzNIxt4WeWQp4XXGKhy5ooBLPFg6NYuzXZxNRgQSWLQ0e8Mf%2F6DUjU7doDdgWSWDXNAwzKqRwBhSnq%2FDlNyrU6j9I9fviDDjUitef3JIeMA1LQjXG5qEdyz4DxIaamckhQRDbAU6nIeAuCilO5j0Nn%2BNprAHIa6oy9FDUAm5Mnt4i%2FJ%2FOJMQzoVAaYZCkgEmqixgO3S4Sq2Qlwirh%2B784mPSigHh7pEQfFJUP1Bg5AB%2FOGJS4qqrLawujvaaLRXBKTjXAn7bCIT9xz%2F0FqxHS8Wbt8blI6xqmbClnJXpnp3pHAIRB2gxhzhIrkKvcXRKOOo9oNEqbj1cWYteWVP4LeLqNY7jVTJiCJDdJBu6Ag4esG3m82887%2BGoz6rzXWeA5vPtjrbXT2eeL%2FKOzqbGvk0%2B%2FdbvSA8YituQADEzFmzZviKXgrgLmL2AFY8%2FjOSNYyjmxTnbvUUHZEY%2Fuh9EKcxFQY01xf96SuBHyjXUkJ3FgAFP9yXC2mG0AFEWWsdkm8nCmMBX2a52WZR697mzYNbTme2TmU3SJESQDXVTs8DIqkZ6DA4ljTFbT42lJKhnde7sQjzfu5JROJEz%2FszSKBQiz6Z6W76HJg0LYu7cw87qOvQY6pgEuYSTOpyZ3GjyjXr8tD5E0M4NkKmy0%2FV85%2BjcaUcseMZkrP9A9fNqDohuL4yL1srjCXKdm6%2F26qBy9DxqyJgJ5KRAxTWXT%2BKb0541KTrgubnuRRpvMuT9wi4uF44WaQpSFK2GrT0ZBIoM4lxj6mbVQGr%2BjBu1htSOijA6KIOrn8pKRU%2BEjSGFNakmtAtoJjRoR6vPOkh9QsuQcJIwSXLOc7lRp%2FzdD&X-Amz-Signature=6cf8ca0e0a9ed8f470abbb44d2cf5cbb12c2137e72169d3486795cffd43cd6fc&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
