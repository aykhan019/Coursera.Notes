

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664REGHLO7%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJIMEYCIQD4M9oqbSHhgqrvSpnNdwCHRTb%2BasKUHqQ7Q3BqpiN6%2BwIhAIDLNzLI9DwJfswRQpQ%2BRVIxHIXCvvp%2Fd2SUtPZ3DLP8Kv8DCGMQABoMNjM3NDIzMTgzODA1IgyW%2FqxOQmGimK9Mmb0q3AOgXokv74y%2FVzM%2Bp%2F2bDnAsKj97uDelUB3LFmbALneDySEbMwRnhc7ulb9LB2XKclMcTBSmhim9I7G36uV06Qar2%2BrRpBeWCkLISbNncKMzWm%2FILtOeGVD9yciqFIMPk5huo%2B4CEcReyCPG%2FxZIvtkJR8PyFELPN0pkPJ2SnftUF0%2B11eKBCOIDnOlMqeYFJT59JFh4TI1fq0olAXA%2BrtdsXx3Fdnw63T%2F1%2BP7h620RUUG0oHbdHUa2GQrNrjd3D2o8GJx5INaVrzEePe6sBa2Ah%2Fko6wd9snuB5fACJTsbXyKt9qGSVbt5JHfWSn4yk6o0RrQs%2BvSlDs4Ao18wFTbZfIGZSTv%2FM8jh0FIK8FKf9RSLdurrhS0zUHvmLABrvFodmi6erRSVsk8isrUieCsv8WD0Qn6k%2FcoFZP9t0bFmHVa%2FOYVRMIfUrqaZXBCSgOkOCd4HEf3NuKmh2347h%2BtGbU0bmZwaGF2h3C1HMwjrim%2B4EShX8E%2BmPMgI4weS0qplDy1QsmShNTIwRqZffkBEG3I1MhvzybqXBGvKKMZZEfC3ZNL8OOFac0WCwXZVH4%2B3KvDcXbjFRqUA3%2B8jLhU7F4Ehtqvv4tbdtXXJIblJUgZL2Io7Lt8ohuq08jDY%2B5O9BjqkAb%2Bvzyb7e9wICDCIJIJtPGngw8gFCZ7OBOkUKTLmrk8kvS%2Fwnma3ft86VWKKZx0Rgr5AJZdDQPYHAQN3lhxv3jefd2oEzKlU1Q69U0uNkt5Ixa4Pc3KWY84Up%2F1epnnnWDTOlbC7BxglugXjyJkWJ7hCmbbo57Sb32K5PdPWovpPcUNASvSlcgzZPOJUnfsnsZtXAoOFKYP40MXqS0hRc5diznbb&X-Amz-Signature=ba04240a0caafcc1dbad616989106774e06d801822b912d8df9f773ddd2123fe&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664REGHLO7%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJIMEYCIQD4M9oqbSHhgqrvSpnNdwCHRTb%2BasKUHqQ7Q3BqpiN6%2BwIhAIDLNzLI9DwJfswRQpQ%2BRVIxHIXCvvp%2Fd2SUtPZ3DLP8Kv8DCGMQABoMNjM3NDIzMTgzODA1IgyW%2FqxOQmGimK9Mmb0q3AOgXokv74y%2FVzM%2Bp%2F2bDnAsKj97uDelUB3LFmbALneDySEbMwRnhc7ulb9LB2XKclMcTBSmhim9I7G36uV06Qar2%2BrRpBeWCkLISbNncKMzWm%2FILtOeGVD9yciqFIMPk5huo%2B4CEcReyCPG%2FxZIvtkJR8PyFELPN0pkPJ2SnftUF0%2B11eKBCOIDnOlMqeYFJT59JFh4TI1fq0olAXA%2BrtdsXx3Fdnw63T%2F1%2BP7h620RUUG0oHbdHUa2GQrNrjd3D2o8GJx5INaVrzEePe6sBa2Ah%2Fko6wd9snuB5fACJTsbXyKt9qGSVbt5JHfWSn4yk6o0RrQs%2BvSlDs4Ao18wFTbZfIGZSTv%2FM8jh0FIK8FKf9RSLdurrhS0zUHvmLABrvFodmi6erRSVsk8isrUieCsv8WD0Qn6k%2FcoFZP9t0bFmHVa%2FOYVRMIfUrqaZXBCSgOkOCd4HEf3NuKmh2347h%2BtGbU0bmZwaGF2h3C1HMwjrim%2B4EShX8E%2BmPMgI4weS0qplDy1QsmShNTIwRqZffkBEG3I1MhvzybqXBGvKKMZZEfC3ZNL8OOFac0WCwXZVH4%2B3KvDcXbjFRqUA3%2B8jLhU7F4Ehtqvv4tbdtXXJIblJUgZL2Io7Lt8ohuq08jDY%2B5O9BjqkAb%2Bvzyb7e9wICDCIJIJtPGngw8gFCZ7OBOkUKTLmrk8kvS%2Fwnma3ft86VWKKZx0Rgr5AJZdDQPYHAQN3lhxv3jefd2oEzKlU1Q69U0uNkt5Ixa4Pc3KWY84Up%2F1epnnnWDTOlbC7BxglugXjyJkWJ7hCmbbo57Sb32K5PdPWovpPcUNASvSlcgzZPOJUnfsnsZtXAoOFKYP40MXqS0hRc5diznbb&X-Amz-Signature=ccfdb15cf319cdddd809094a7cee7f14f5512bb1523fe83d85bc48ad65176b90&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664REGHLO7%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJIMEYCIQD4M9oqbSHhgqrvSpnNdwCHRTb%2BasKUHqQ7Q3BqpiN6%2BwIhAIDLNzLI9DwJfswRQpQ%2BRVIxHIXCvvp%2Fd2SUtPZ3DLP8Kv8DCGMQABoMNjM3NDIzMTgzODA1IgyW%2FqxOQmGimK9Mmb0q3AOgXokv74y%2FVzM%2Bp%2F2bDnAsKj97uDelUB3LFmbALneDySEbMwRnhc7ulb9LB2XKclMcTBSmhim9I7G36uV06Qar2%2BrRpBeWCkLISbNncKMzWm%2FILtOeGVD9yciqFIMPk5huo%2B4CEcReyCPG%2FxZIvtkJR8PyFELPN0pkPJ2SnftUF0%2B11eKBCOIDnOlMqeYFJT59JFh4TI1fq0olAXA%2BrtdsXx3Fdnw63T%2F1%2BP7h620RUUG0oHbdHUa2GQrNrjd3D2o8GJx5INaVrzEePe6sBa2Ah%2Fko6wd9snuB5fACJTsbXyKt9qGSVbt5JHfWSn4yk6o0RrQs%2BvSlDs4Ao18wFTbZfIGZSTv%2FM8jh0FIK8FKf9RSLdurrhS0zUHvmLABrvFodmi6erRSVsk8isrUieCsv8WD0Qn6k%2FcoFZP9t0bFmHVa%2FOYVRMIfUrqaZXBCSgOkOCd4HEf3NuKmh2347h%2BtGbU0bmZwaGF2h3C1HMwjrim%2B4EShX8E%2BmPMgI4weS0qplDy1QsmShNTIwRqZffkBEG3I1MhvzybqXBGvKKMZZEfC3ZNL8OOFac0WCwXZVH4%2B3KvDcXbjFRqUA3%2B8jLhU7F4Ehtqvv4tbdtXXJIblJUgZL2Io7Lt8ohuq08jDY%2B5O9BjqkAb%2Bvzyb7e9wICDCIJIJtPGngw8gFCZ7OBOkUKTLmrk8kvS%2Fwnma3ft86VWKKZx0Rgr5AJZdDQPYHAQN3lhxv3jefd2oEzKlU1Q69U0uNkt5Ixa4Pc3KWY84Up%2F1epnnnWDTOlbC7BxglugXjyJkWJ7hCmbbo57Sb32K5PdPWovpPcUNASvSlcgzZPOJUnfsnsZtXAoOFKYP40MXqS0hRc5diznbb&X-Amz-Signature=e65ede4def4f904df3605c68b908d7e75cf87bb109fa587fa1f1734c1707b1a8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOVE7ECL%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIA6YZK61TCDkGjveflUan4UBy%2FSdh%2B5U3BlJKKl%2FdelvAiEAoT7HusBlD0%2FucM9fsAmhcdcN4y6TlpTF1ExNJszTeT0q%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDDY8mBTZTpcevFH0%2BircA4RX5wgovDTUpdgN%2FemIes70oaVNFlLFL%2Br0UAmYJq9KM8Ldy3Gmk05VrJ06rNw8nnMLYaZk4LH5TXR5hyVYCn8Cv2z%2F4lyGSyLhdMGx07ZR2MCE4Iz3OOmFf5CMTzqI175GF09EQSVI%2BFB0Qq0xmGfzQ%2FgdHb8cSzkCuMbwfE0zd05dgte9TjNyGy1gfT5hQFmqw%2BU98FNZZ35yLGcKkPfMrpFx6f5vuKyW0Tz8a3%2FKOcxCBEmRiqRtzhvSjccwYsbgwdp2BSYE25jLj%2FTv1oVvdMMBv%2BiEfMoPn5wqyJ6oyRftqexEn%2F33uisjj7zgxq%2FsdQSoBY%2BBAJ0vDlscCcT6mDBeXK0Bvm59o0hScEb4B4q9ONXfViiHsV92ADAxDcFgXyRFEYJk86iUZ6gU%2Fqr%2Fz2sYq6GuPUQVSyXH4KseL9uKI3aXDdmHGEmpMQBehWrN%2BDc%2Bz%2FSX0YyD0d065fhq1JchDWTqdCk971mupCmEOAzRMMkcIWqc3n0jE9172NmQlz8lYAXq7Bmwblb8F3tCzvrMJNjz80%2BMm8ApmAE7yxkGtvgTp7JhLSwQc%2BklpcXoUVJ14QcWFhEemsZ21mrOwE54R2yVCZG47WYDnkawmPehHJMGt1kG3%2BKcMOP7k70GOqUB0AzvLkQYkq5%2B%2B5J8fpMrNJdKYBfZSkIFKXtN%2Fm3rroO3OfLDizLKaOj5bO4dU9pKy3K7EEAzNdYnXGd16a%2F4Nd7QPMJDcuVXRpnF6JeFC8n5glqne9MNK9xB%2F50PCoqeVl0IN9LsVaLoVibMyzlOekmfMQ8S8Q6qY7hJyZtL4pX8XGsvn3pDiEwbvraOlStz6dr02CrdWF5908fL2SJhvd0s1fw5&X-Amz-Signature=e3bc8bfeb623c0e48dd48733e2cb08c34479c877d68e2286aadde22df96f9adb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663EIN4VDT%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191146Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIQD3t%2BHEy77fWL%2BPNmWjGqgHycCHE3Wbg5mtoY3MWfZZVgIgMxL8tCzRtICHqkUlKm8zJTPXkKj3HGoL0fQFVUnBVycq%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDDLhnbaWuJw6KAM%2BRCrcA2ndccNFWvFe%2B1nTsFF4uy1Hwj6kdNIIWx3gn9b7AmKYemelvAZDc7z%2BSX2MOX5D88uVrXpYKviwBWuM%2FMwwiZmPvWj310tWI%2F5xVI%2Fi2Sl%2F9pcp8RMYcFK8VJ2RZtgkuwek2qfI7hRdOrvCDOc5fSuTghUizmf%2F5GBQOVyAFSljaLxPnZNlc%2BTb%2BTma58MYKsh%2B7Muae9%2F5Gxn9TaIsQ3849LxWh5qV%2B%2Bd1qyWvG%2BDrTx3KmV96LnR3zj3lP3cN%2BIvNmTCB2Zog9WL9r4p7nyL4X5%2BX75TBALj8gxOgFnzqIE1dHRlGPI2K%2FytKsyyCQjoCCWnmvQLw0e3ZeqlfFKb9dliquttAaH3hEmm1Wkh7EU%2F%2BABGviYj9yzgDlc3sc7pP1Gb1tRctQvpVUms0Z4cYWf665d68JccgBIZb%2FaMYLtHQwPOrPlpNRfebvogWpe9ptzTUf11SMHcupPSSV9qmEuksxr2ft2JKK98xC0wuQaFUH74hmvOJtBUo8tr%2F%2BUTZOPFH%2B7e0G2Us6AVrCn3YMTJ5kFRtr%2BHKow6DyMYOWurQIXaqe7ch78vlTdP5HV1Iyu73Ziad8Hb99dvaJueK6DFDZBBgnvugfKZg7b%2BHoDhM0JyQk29n6F5CMOv7k70GOqUBXRrZ8vJ27am%2BwKVtTeSm8dNn6bphUBC%2BaOxThfCeF4Cv14sIIsl3BWKxRbBkFsJbg4%2BI07sPm5wNRBgrUck6uf4uA2SfqAZdXiS3PT4Ln1dxZwqmJPG8H1m7zmY5v%2BWoClhsUcAtflwjQwzBQvvx1%2F1gJ5fsUDmTuzKUM6lRX8IRI%2BgLi59ETGmoHdBQvILi5yXUVpuBoVJmS3%2FhBXuoibG8OOjO&X-Amz-Signature=b3ba11e1872123e51b3c5249ab6cfe57d0bab546aafbd59d7b5f615e9453db80&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664REGHLO7%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJIMEYCIQD4M9oqbSHhgqrvSpnNdwCHRTb%2BasKUHqQ7Q3BqpiN6%2BwIhAIDLNzLI9DwJfswRQpQ%2BRVIxHIXCvvp%2Fd2SUtPZ3DLP8Kv8DCGMQABoMNjM3NDIzMTgzODA1IgyW%2FqxOQmGimK9Mmb0q3AOgXokv74y%2FVzM%2Bp%2F2bDnAsKj97uDelUB3LFmbALneDySEbMwRnhc7ulb9LB2XKclMcTBSmhim9I7G36uV06Qar2%2BrRpBeWCkLISbNncKMzWm%2FILtOeGVD9yciqFIMPk5huo%2B4CEcReyCPG%2FxZIvtkJR8PyFELPN0pkPJ2SnftUF0%2B11eKBCOIDnOlMqeYFJT59JFh4TI1fq0olAXA%2BrtdsXx3Fdnw63T%2F1%2BP7h620RUUG0oHbdHUa2GQrNrjd3D2o8GJx5INaVrzEePe6sBa2Ah%2Fko6wd9snuB5fACJTsbXyKt9qGSVbt5JHfWSn4yk6o0RrQs%2BvSlDs4Ao18wFTbZfIGZSTv%2FM8jh0FIK8FKf9RSLdurrhS0zUHvmLABrvFodmi6erRSVsk8isrUieCsv8WD0Qn6k%2FcoFZP9t0bFmHVa%2FOYVRMIfUrqaZXBCSgOkOCd4HEf3NuKmh2347h%2BtGbU0bmZwaGF2h3C1HMwjrim%2B4EShX8E%2BmPMgI4weS0qplDy1QsmShNTIwRqZffkBEG3I1MhvzybqXBGvKKMZZEfC3ZNL8OOFac0WCwXZVH4%2B3KvDcXbjFRqUA3%2B8jLhU7F4Ehtqvv4tbdtXXJIblJUgZL2Io7Lt8ohuq08jDY%2B5O9BjqkAb%2Bvzyb7e9wICDCIJIJtPGngw8gFCZ7OBOkUKTLmrk8kvS%2Fwnma3ft86VWKKZx0Rgr5AJZdDQPYHAQN3lhxv3jefd2oEzKlU1Q69U0uNkt5Ixa4Pc3KWY84Up%2F1epnnnWDTOlbC7BxglugXjyJkWJ7hCmbbo57Sb32K5PdPWovpPcUNASvSlcgzZPOJUnfsnsZtXAoOFKYP40MXqS0hRc5diznbb&X-Amz-Signature=505999a987ef374f5777a4c978e289818fc5bb4018bb772240ae845ff15525e9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664REGHLO7%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJIMEYCIQD4M9oqbSHhgqrvSpnNdwCHRTb%2BasKUHqQ7Q3BqpiN6%2BwIhAIDLNzLI9DwJfswRQpQ%2BRVIxHIXCvvp%2Fd2SUtPZ3DLP8Kv8DCGMQABoMNjM3NDIzMTgzODA1IgyW%2FqxOQmGimK9Mmb0q3AOgXokv74y%2FVzM%2Bp%2F2bDnAsKj97uDelUB3LFmbALneDySEbMwRnhc7ulb9LB2XKclMcTBSmhim9I7G36uV06Qar2%2BrRpBeWCkLISbNncKMzWm%2FILtOeGVD9yciqFIMPk5huo%2B4CEcReyCPG%2FxZIvtkJR8PyFELPN0pkPJ2SnftUF0%2B11eKBCOIDnOlMqeYFJT59JFh4TI1fq0olAXA%2BrtdsXx3Fdnw63T%2F1%2BP7h620RUUG0oHbdHUa2GQrNrjd3D2o8GJx5INaVrzEePe6sBa2Ah%2Fko6wd9snuB5fACJTsbXyKt9qGSVbt5JHfWSn4yk6o0RrQs%2BvSlDs4Ao18wFTbZfIGZSTv%2FM8jh0FIK8FKf9RSLdurrhS0zUHvmLABrvFodmi6erRSVsk8isrUieCsv8WD0Qn6k%2FcoFZP9t0bFmHVa%2FOYVRMIfUrqaZXBCSgOkOCd4HEf3NuKmh2347h%2BtGbU0bmZwaGF2h3C1HMwjrim%2B4EShX8E%2BmPMgI4weS0qplDy1QsmShNTIwRqZffkBEG3I1MhvzybqXBGvKKMZZEfC3ZNL8OOFac0WCwXZVH4%2B3KvDcXbjFRqUA3%2B8jLhU7F4Ehtqvv4tbdtXXJIblJUgZL2Io7Lt8ohuq08jDY%2B5O9BjqkAb%2Bvzyb7e9wICDCIJIJtPGngw8gFCZ7OBOkUKTLmrk8kvS%2Fwnma3ft86VWKKZx0Rgr5AJZdDQPYHAQN3lhxv3jefd2oEzKlU1Q69U0uNkt5Ixa4Pc3KWY84Up%2F1epnnnWDTOlbC7BxglugXjyJkWJ7hCmbbo57Sb32K5PdPWovpPcUNASvSlcgzZPOJUnfsnsZtXAoOFKYP40MXqS0hRc5diznbb&X-Amz-Signature=9284d4246a38f0ea59712bedf6fffeb4212bf28050348d027387401ca6295c34&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664REGHLO7%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJIMEYCIQD4M9oqbSHhgqrvSpnNdwCHRTb%2BasKUHqQ7Q3BqpiN6%2BwIhAIDLNzLI9DwJfswRQpQ%2BRVIxHIXCvvp%2Fd2SUtPZ3DLP8Kv8DCGMQABoMNjM3NDIzMTgzODA1IgyW%2FqxOQmGimK9Mmb0q3AOgXokv74y%2FVzM%2Bp%2F2bDnAsKj97uDelUB3LFmbALneDySEbMwRnhc7ulb9LB2XKclMcTBSmhim9I7G36uV06Qar2%2BrRpBeWCkLISbNncKMzWm%2FILtOeGVD9yciqFIMPk5huo%2B4CEcReyCPG%2FxZIvtkJR8PyFELPN0pkPJ2SnftUF0%2B11eKBCOIDnOlMqeYFJT59JFh4TI1fq0olAXA%2BrtdsXx3Fdnw63T%2F1%2BP7h620RUUG0oHbdHUa2GQrNrjd3D2o8GJx5INaVrzEePe6sBa2Ah%2Fko6wd9snuB5fACJTsbXyKt9qGSVbt5JHfWSn4yk6o0RrQs%2BvSlDs4Ao18wFTbZfIGZSTv%2FM8jh0FIK8FKf9RSLdurrhS0zUHvmLABrvFodmi6erRSVsk8isrUieCsv8WD0Qn6k%2FcoFZP9t0bFmHVa%2FOYVRMIfUrqaZXBCSgOkOCd4HEf3NuKmh2347h%2BtGbU0bmZwaGF2h3C1HMwjrim%2B4EShX8E%2BmPMgI4weS0qplDy1QsmShNTIwRqZffkBEG3I1MhvzybqXBGvKKMZZEfC3ZNL8OOFac0WCwXZVH4%2B3KvDcXbjFRqUA3%2B8jLhU7F4Ehtqvv4tbdtXXJIblJUgZL2Io7Lt8ohuq08jDY%2B5O9BjqkAb%2Bvzyb7e9wICDCIJIJtPGngw8gFCZ7OBOkUKTLmrk8kvS%2Fwnma3ft86VWKKZx0Rgr5AJZdDQPYHAQN3lhxv3jefd2oEzKlU1Q69U0uNkt5Ixa4Pc3KWY84Up%2F1epnnnWDTOlbC7BxglugXjyJkWJ7hCmbbo57Sb32K5PdPWovpPcUNASvSlcgzZPOJUnfsnsZtXAoOFKYP40MXqS0hRc5diznbb&X-Amz-Signature=e1802e56ec15b241482405194b42ed4d56b0c0cb8f321100d95f45013db762ef&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664REGHLO7%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJIMEYCIQD4M9oqbSHhgqrvSpnNdwCHRTb%2BasKUHqQ7Q3BqpiN6%2BwIhAIDLNzLI9DwJfswRQpQ%2BRVIxHIXCvvp%2Fd2SUtPZ3DLP8Kv8DCGMQABoMNjM3NDIzMTgzODA1IgyW%2FqxOQmGimK9Mmb0q3AOgXokv74y%2FVzM%2Bp%2F2bDnAsKj97uDelUB3LFmbALneDySEbMwRnhc7ulb9LB2XKclMcTBSmhim9I7G36uV06Qar2%2BrRpBeWCkLISbNncKMzWm%2FILtOeGVD9yciqFIMPk5huo%2B4CEcReyCPG%2FxZIvtkJR8PyFELPN0pkPJ2SnftUF0%2B11eKBCOIDnOlMqeYFJT59JFh4TI1fq0olAXA%2BrtdsXx3Fdnw63T%2F1%2BP7h620RUUG0oHbdHUa2GQrNrjd3D2o8GJx5INaVrzEePe6sBa2Ah%2Fko6wd9snuB5fACJTsbXyKt9qGSVbt5JHfWSn4yk6o0RrQs%2BvSlDs4Ao18wFTbZfIGZSTv%2FM8jh0FIK8FKf9RSLdurrhS0zUHvmLABrvFodmi6erRSVsk8isrUieCsv8WD0Qn6k%2FcoFZP9t0bFmHVa%2FOYVRMIfUrqaZXBCSgOkOCd4HEf3NuKmh2347h%2BtGbU0bmZwaGF2h3C1HMwjrim%2B4EShX8E%2BmPMgI4weS0qplDy1QsmShNTIwRqZffkBEG3I1MhvzybqXBGvKKMZZEfC3ZNL8OOFac0WCwXZVH4%2B3KvDcXbjFRqUA3%2B8jLhU7F4Ehtqvv4tbdtXXJIblJUgZL2Io7Lt8ohuq08jDY%2B5O9BjqkAb%2Bvzyb7e9wICDCIJIJtPGngw8gFCZ7OBOkUKTLmrk8kvS%2Fwnma3ft86VWKKZx0Rgr5AJZdDQPYHAQN3lhxv3jefd2oEzKlU1Q69U0uNkt5Ixa4Pc3KWY84Up%2F1epnnnWDTOlbC7BxglugXjyJkWJ7hCmbbo57Sb32K5PdPWovpPcUNASvSlcgzZPOJUnfsnsZtXAoOFKYP40MXqS0hRc5diznbb&X-Amz-Signature=48b44a19efc6e79cce2fd79ec51a69dda6c3eb0057f44e759aa2d85b2d52be94&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
