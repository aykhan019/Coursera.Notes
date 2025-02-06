

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QLKKRSBD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIBgI66%2BiBp5Di03f6ONynZkDvxd1ykh5ktEI2fzYcT5vAiAybzuH8x1NyG66HXBpKgGy13IBbLDfz6rHMxZx98Kkxyr%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIMGfFjzbdYsOaFJEyKKtwDV%2F%2B3%2Bo5b9yNos5Gvq7VjWIvECRKtAWQgqxP0A0cvAmaWfqYreoSHGmogRvo7yL%2BBp3F1QqTY81h5Ko3Azqv2FuwJnW%2FL3TeRQY2znpn0OfaIM6n12OzDhZcdmmT1Qbslff%2FvZM141Rd1TDdKyx%2FajZs2Jfvy5pbpHNWvjgtkkGYBP2yJd0j4Uz0BIP65Lss3LHdI5jtmMBrC6pGHthfwgz%2BGJkYtmuyaL1icZ4ZeiWK%2BY5Je3AjnmeSrdbxQDfRX5AniJ%2B183xEXJlkJGZ59FSMDpaxm5jSrqRzZYreX6OMTKlYbvqTc%2FSi5xb5IpE1YRaoWvsXCzGm0mLZbS7vmDq9vh2Zh3ID8bu%2B0ejaL%2BRi0P2PPb0Eadzcu9MM05tdmEvJlkzEDnZKgCHU6FnFKEEI%2F7yPGZZ%2F5z2eoBQnuBVMRSx8c%2BuZRMpS3%2B7sVnVDXtm3CMPpvuzgYfZdKcBMMJ8ltBIHx9xvuoIeMI8t%2BlPMyJxlh%2BQ3sVKhhIoCOU2NstSii6Jb%2F7nC54zPpQhpqF9pneXBmkmi9C8PBJLmsEUAupfBd6DHp8%2Brg3Yi0ra5I%2B8CiuUcDDUjgTP3sdoRGEgVxxrLqD%2BoDJzZT0xFwLtj3p8vyHXxnSSB1GAcw0fuTvQY6pgE4PcrdMKroCH8JY39flQLORk8gtXS9qVyl6rctlO8XUG6kfGItGUZZCU0uJLP9ZbmsJ1Qe0%2FftNAaM6GXIYSC6vkSZLVEl8zdr7X3HuY4mk0MuxWlLy%2B4FY01qNNl5gZ8n%2F1soxAFnAVRkBuIkW3F5ohb6jleEw1C8wLBBRnIWMWbaaFG6rAfh5wax88RXCb1Rps7AUzUCGILAzo3O%2FOG6RPDqWY8t&X-Amz-Signature=928c0bf3b5b35e29c08c170bd0b49f0283d76cf514f116292df4b73061b8313b&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QLKKRSBD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIBgI66%2BiBp5Di03f6ONynZkDvxd1ykh5ktEI2fzYcT5vAiAybzuH8x1NyG66HXBpKgGy13IBbLDfz6rHMxZx98Kkxyr%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIMGfFjzbdYsOaFJEyKKtwDV%2F%2B3%2Bo5b9yNos5Gvq7VjWIvECRKtAWQgqxP0A0cvAmaWfqYreoSHGmogRvo7yL%2BBp3F1QqTY81h5Ko3Azqv2FuwJnW%2FL3TeRQY2znpn0OfaIM6n12OzDhZcdmmT1Qbslff%2FvZM141Rd1TDdKyx%2FajZs2Jfvy5pbpHNWvjgtkkGYBP2yJd0j4Uz0BIP65Lss3LHdI5jtmMBrC6pGHthfwgz%2BGJkYtmuyaL1icZ4ZeiWK%2BY5Je3AjnmeSrdbxQDfRX5AniJ%2B183xEXJlkJGZ59FSMDpaxm5jSrqRzZYreX6OMTKlYbvqTc%2FSi5xb5IpE1YRaoWvsXCzGm0mLZbS7vmDq9vh2Zh3ID8bu%2B0ejaL%2BRi0P2PPb0Eadzcu9MM05tdmEvJlkzEDnZKgCHU6FnFKEEI%2F7yPGZZ%2F5z2eoBQnuBVMRSx8c%2BuZRMpS3%2B7sVnVDXtm3CMPpvuzgYfZdKcBMMJ8ltBIHx9xvuoIeMI8t%2BlPMyJxlh%2BQ3sVKhhIoCOU2NstSii6Jb%2F7nC54zPpQhpqF9pneXBmkmi9C8PBJLmsEUAupfBd6DHp8%2Brg3Yi0ra5I%2B8CiuUcDDUjgTP3sdoRGEgVxxrLqD%2BoDJzZT0xFwLtj3p8vyHXxnSSB1GAcw0fuTvQY6pgE4PcrdMKroCH8JY39flQLORk8gtXS9qVyl6rctlO8XUG6kfGItGUZZCU0uJLP9ZbmsJ1Qe0%2FftNAaM6GXIYSC6vkSZLVEl8zdr7X3HuY4mk0MuxWlLy%2B4FY01qNNl5gZ8n%2F1soxAFnAVRkBuIkW3F5ohb6jleEw1C8wLBBRnIWMWbaaFG6rAfh5wax88RXCb1Rps7AUzUCGILAzo3O%2FOG6RPDqWY8t&X-Amz-Signature=df2a64ee605db20e0b29e9afae62e657d2a1058be57e08efe37b0649e79d945f&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QLKKRSBD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIBgI66%2BiBp5Di03f6ONynZkDvxd1ykh5ktEI2fzYcT5vAiAybzuH8x1NyG66HXBpKgGy13IBbLDfz6rHMxZx98Kkxyr%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIMGfFjzbdYsOaFJEyKKtwDV%2F%2B3%2Bo5b9yNos5Gvq7VjWIvECRKtAWQgqxP0A0cvAmaWfqYreoSHGmogRvo7yL%2BBp3F1QqTY81h5Ko3Azqv2FuwJnW%2FL3TeRQY2znpn0OfaIM6n12OzDhZcdmmT1Qbslff%2FvZM141Rd1TDdKyx%2FajZs2Jfvy5pbpHNWvjgtkkGYBP2yJd0j4Uz0BIP65Lss3LHdI5jtmMBrC6pGHthfwgz%2BGJkYtmuyaL1icZ4ZeiWK%2BY5Je3AjnmeSrdbxQDfRX5AniJ%2B183xEXJlkJGZ59FSMDpaxm5jSrqRzZYreX6OMTKlYbvqTc%2FSi5xb5IpE1YRaoWvsXCzGm0mLZbS7vmDq9vh2Zh3ID8bu%2B0ejaL%2BRi0P2PPb0Eadzcu9MM05tdmEvJlkzEDnZKgCHU6FnFKEEI%2F7yPGZZ%2F5z2eoBQnuBVMRSx8c%2BuZRMpS3%2B7sVnVDXtm3CMPpvuzgYfZdKcBMMJ8ltBIHx9xvuoIeMI8t%2BlPMyJxlh%2BQ3sVKhhIoCOU2NstSii6Jb%2F7nC54zPpQhpqF9pneXBmkmi9C8PBJLmsEUAupfBd6DHp8%2Brg3Yi0ra5I%2B8CiuUcDDUjgTP3sdoRGEgVxxrLqD%2BoDJzZT0xFwLtj3p8vyHXxnSSB1GAcw0fuTvQY6pgE4PcrdMKroCH8JY39flQLORk8gtXS9qVyl6rctlO8XUG6kfGItGUZZCU0uJLP9ZbmsJ1Qe0%2FftNAaM6GXIYSC6vkSZLVEl8zdr7X3HuY4mk0MuxWlLy%2B4FY01qNNl5gZ8n%2F1soxAFnAVRkBuIkW3F5ohb6jleEw1C8wLBBRnIWMWbaaFG6rAfh5wax88RXCb1Rps7AUzUCGILAzo3O%2FOG6RPDqWY8t&X-Amz-Signature=77efa008a7ad005b5adce813e8ca7980c40c7aa8faf8aeaed717789c3b836f1c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663EIN4VDT%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIQD3t%2BHEy77fWL%2BPNmWjGqgHycCHE3Wbg5mtoY3MWfZZVgIgMxL8tCzRtICHqkUlKm8zJTPXkKj3HGoL0fQFVUnBVycq%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDDLhnbaWuJw6KAM%2BRCrcA2ndccNFWvFe%2B1nTsFF4uy1Hwj6kdNIIWx3gn9b7AmKYemelvAZDc7z%2BSX2MOX5D88uVrXpYKviwBWuM%2FMwwiZmPvWj310tWI%2F5xVI%2Fi2Sl%2F9pcp8RMYcFK8VJ2RZtgkuwek2qfI7hRdOrvCDOc5fSuTghUizmf%2F5GBQOVyAFSljaLxPnZNlc%2BTb%2BTma58MYKsh%2B7Muae9%2F5Gxn9TaIsQ3849LxWh5qV%2B%2Bd1qyWvG%2BDrTx3KmV96LnR3zj3lP3cN%2BIvNmTCB2Zog9WL9r4p7nyL4X5%2BX75TBALj8gxOgFnzqIE1dHRlGPI2K%2FytKsyyCQjoCCWnmvQLw0e3ZeqlfFKb9dliquttAaH3hEmm1Wkh7EU%2F%2BABGviYj9yzgDlc3sc7pP1Gb1tRctQvpVUms0Z4cYWf665d68JccgBIZb%2FaMYLtHQwPOrPlpNRfebvogWpe9ptzTUf11SMHcupPSSV9qmEuksxr2ft2JKK98xC0wuQaFUH74hmvOJtBUo8tr%2F%2BUTZOPFH%2B7e0G2Us6AVrCn3YMTJ5kFRtr%2BHKow6DyMYOWurQIXaqe7ch78vlTdP5HV1Iyu73Ziad8Hb99dvaJueK6DFDZBBgnvugfKZg7b%2BHoDhM0JyQk29n6F5CMOv7k70GOqUBXRrZ8vJ27am%2BwKVtTeSm8dNn6bphUBC%2BaOxThfCeF4Cv14sIIsl3BWKxRbBkFsJbg4%2BI07sPm5wNRBgrUck6uf4uA2SfqAZdXiS3PT4Ln1dxZwqmJPG8H1m7zmY5v%2BWoClhsUcAtflwjQwzBQvvx1%2F1gJ5fsUDmTuzKUM6lRX8IRI%2BgLi59ETGmoHdBQvILi5yXUVpuBoVJmS3%2FhBXuoibG8OOjO&X-Amz-Signature=7f9edd5507bd30a9c1d90b2f0721820de6d3bc21c75730fd5cf8f1e2cc9a9c9a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGGSBSOG%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIGaOgGUITvysvj3JuMzUPZVLbbUE9sFGx91aMp1BZbhjAiAZ%2FTADJ5KM8uF%2FGe%2BOH4KxQXYB9AcRZmSwQU5Jddi19Sr%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIMlgJsgrucvltLnIsTKtwDyCoRZwjkKW8LlDYGyo8Nvdww7Qfje7B262hBO5Fj1oEn6tr5v2qhNEUrpp4sF1RxYp2eBhxs0eHi5QNYvzENCO422tyFSgC65HjYzNGBOZl8wzy9Xp3Vw4GZq1BgXwHtxh5wxDbIKiqwRLg91nlpvlLo%2FVFm5hDNeGlEUNiVAsP1CVxsQHblwuGvEIXkhHuW4eDkKG%2BTsQkoUfsLL5dg0Uj3L6jJpYt1C%2FalHjN62Hw1E8bj%2FeOLNXukZBEohQdp6af8ayEFpx%2BMGlj%2FqstZU8efgYR1DJqdzAD9S1h7MUTYDJJLFT2vDzt8kDpqHbY2%2BWiRS0sutUWF1haoYLUodBt5DcUGO2ISAOJQZ2QDziwVKXsJw8YXNNVHsyXCRk5C4oY28uSkRMwY6nwZ0S5WzheggUfKzgSl7CwnA%2Fy7LCx8t8O30WOcYApP4uCfqy2hvIuDkwZAu%2F2v8mQbZ2fJZOlI0K%2BI0Rcv90NM3JHd7yTtTnIAa%2BzThmKp%2FECIWHrDEf1EvjJvfJcAyFiRZdt6UjcMsCh5YolTB7AWgrc6uEBYVyXhzWlVVnCAjhk8loW2T30Liij3gUmO8KD%2BokRqVtAjRWlvFPkddN%2FzyjhIdPEg0PdpmOf9RJxzhN4w%2B%2FuTvQY6pgF98nGhZYp2d%2BkkEfH6A7py5pwOq9eEHcqtp5%2BBA8MSFCL0xOIMXIep%2FZQWdWPE1nzOYNnPHuoOC3x9EES3dixEZQFLGrK1QteUedGuAhHq%2FRrG0mmWfuZu9AeoO%2FmRKyxNNpF0O9BG7TRYfZXDeYd0Few52675pG%2F2UxjRuF6CaLDyumKPJTqB84zQcAW%2FYCdBZYYvKp0osp%2ByMXhuOXXrAxBbjKV%2F&X-Amz-Signature=f16f9b8b4f21ae95b56d304e90b28a8eff61cfd5551cf2066c28158d21eb39fb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QLKKRSBD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIBgI66%2BiBp5Di03f6ONynZkDvxd1ykh5ktEI2fzYcT5vAiAybzuH8x1NyG66HXBpKgGy13IBbLDfz6rHMxZx98Kkxyr%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIMGfFjzbdYsOaFJEyKKtwDV%2F%2B3%2Bo5b9yNos5Gvq7VjWIvECRKtAWQgqxP0A0cvAmaWfqYreoSHGmogRvo7yL%2BBp3F1QqTY81h5Ko3Azqv2FuwJnW%2FL3TeRQY2znpn0OfaIM6n12OzDhZcdmmT1Qbslff%2FvZM141Rd1TDdKyx%2FajZs2Jfvy5pbpHNWvjgtkkGYBP2yJd0j4Uz0BIP65Lss3LHdI5jtmMBrC6pGHthfwgz%2BGJkYtmuyaL1icZ4ZeiWK%2BY5Je3AjnmeSrdbxQDfRX5AniJ%2B183xEXJlkJGZ59FSMDpaxm5jSrqRzZYreX6OMTKlYbvqTc%2FSi5xb5IpE1YRaoWvsXCzGm0mLZbS7vmDq9vh2Zh3ID8bu%2B0ejaL%2BRi0P2PPb0Eadzcu9MM05tdmEvJlkzEDnZKgCHU6FnFKEEI%2F7yPGZZ%2F5z2eoBQnuBVMRSx8c%2BuZRMpS3%2B7sVnVDXtm3CMPpvuzgYfZdKcBMMJ8ltBIHx9xvuoIeMI8t%2BlPMyJxlh%2BQ3sVKhhIoCOU2NstSii6Jb%2F7nC54zPpQhpqF9pneXBmkmi9C8PBJLmsEUAupfBd6DHp8%2Brg3Yi0ra5I%2B8CiuUcDDUjgTP3sdoRGEgVxxrLqD%2BoDJzZT0xFwLtj3p8vyHXxnSSB1GAcw0fuTvQY6pgE4PcrdMKroCH8JY39flQLORk8gtXS9qVyl6rctlO8XUG6kfGItGUZZCU0uJLP9ZbmsJ1Qe0%2FftNAaM6GXIYSC6vkSZLVEl8zdr7X3HuY4mk0MuxWlLy%2B4FY01qNNl5gZ8n%2F1soxAFnAVRkBuIkW3F5ohb6jleEw1C8wLBBRnIWMWbaaFG6rAfh5wax88RXCb1Rps7AUzUCGILAzo3O%2FOG6RPDqWY8t&X-Amz-Signature=098ec2155ad78f89090b4fba464539960301aad94d17ed0a05421dac45086b13&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QLKKRSBD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIBgI66%2BiBp5Di03f6ONynZkDvxd1ykh5ktEI2fzYcT5vAiAybzuH8x1NyG66HXBpKgGy13IBbLDfz6rHMxZx98Kkxyr%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIMGfFjzbdYsOaFJEyKKtwDV%2F%2B3%2Bo5b9yNos5Gvq7VjWIvECRKtAWQgqxP0A0cvAmaWfqYreoSHGmogRvo7yL%2BBp3F1QqTY81h5Ko3Azqv2FuwJnW%2FL3TeRQY2znpn0OfaIM6n12OzDhZcdmmT1Qbslff%2FvZM141Rd1TDdKyx%2FajZs2Jfvy5pbpHNWvjgtkkGYBP2yJd0j4Uz0BIP65Lss3LHdI5jtmMBrC6pGHthfwgz%2BGJkYtmuyaL1icZ4ZeiWK%2BY5Je3AjnmeSrdbxQDfRX5AniJ%2B183xEXJlkJGZ59FSMDpaxm5jSrqRzZYreX6OMTKlYbvqTc%2FSi5xb5IpE1YRaoWvsXCzGm0mLZbS7vmDq9vh2Zh3ID8bu%2B0ejaL%2BRi0P2PPb0Eadzcu9MM05tdmEvJlkzEDnZKgCHU6FnFKEEI%2F7yPGZZ%2F5z2eoBQnuBVMRSx8c%2BuZRMpS3%2B7sVnVDXtm3CMPpvuzgYfZdKcBMMJ8ltBIHx9xvuoIeMI8t%2BlPMyJxlh%2BQ3sVKhhIoCOU2NstSii6Jb%2F7nC54zPpQhpqF9pneXBmkmi9C8PBJLmsEUAupfBd6DHp8%2Brg3Yi0ra5I%2B8CiuUcDDUjgTP3sdoRGEgVxxrLqD%2BoDJzZT0xFwLtj3p8vyHXxnSSB1GAcw0fuTvQY6pgE4PcrdMKroCH8JY39flQLORk8gtXS9qVyl6rctlO8XUG6kfGItGUZZCU0uJLP9ZbmsJ1Qe0%2FftNAaM6GXIYSC6vkSZLVEl8zdr7X3HuY4mk0MuxWlLy%2B4FY01qNNl5gZ8n%2F1soxAFnAVRkBuIkW3F5ohb6jleEw1C8wLBBRnIWMWbaaFG6rAfh5wax88RXCb1Rps7AUzUCGILAzo3O%2FOG6RPDqWY8t&X-Amz-Signature=02a157f55d7f0bdca8957da9ebf3c44db4be5ed06f4a207509f8f6821ce54983&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QLKKRSBD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIBgI66%2BiBp5Di03f6ONynZkDvxd1ykh5ktEI2fzYcT5vAiAybzuH8x1NyG66HXBpKgGy13IBbLDfz6rHMxZx98Kkxyr%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIMGfFjzbdYsOaFJEyKKtwDV%2F%2B3%2Bo5b9yNos5Gvq7VjWIvECRKtAWQgqxP0A0cvAmaWfqYreoSHGmogRvo7yL%2BBp3F1QqTY81h5Ko3Azqv2FuwJnW%2FL3TeRQY2znpn0OfaIM6n12OzDhZcdmmT1Qbslff%2FvZM141Rd1TDdKyx%2FajZs2Jfvy5pbpHNWvjgtkkGYBP2yJd0j4Uz0BIP65Lss3LHdI5jtmMBrC6pGHthfwgz%2BGJkYtmuyaL1icZ4ZeiWK%2BY5Je3AjnmeSrdbxQDfRX5AniJ%2B183xEXJlkJGZ59FSMDpaxm5jSrqRzZYreX6OMTKlYbvqTc%2FSi5xb5IpE1YRaoWvsXCzGm0mLZbS7vmDq9vh2Zh3ID8bu%2B0ejaL%2BRi0P2PPb0Eadzcu9MM05tdmEvJlkzEDnZKgCHU6FnFKEEI%2F7yPGZZ%2F5z2eoBQnuBVMRSx8c%2BuZRMpS3%2B7sVnVDXtm3CMPpvuzgYfZdKcBMMJ8ltBIHx9xvuoIeMI8t%2BlPMyJxlh%2BQ3sVKhhIoCOU2NstSii6Jb%2F7nC54zPpQhpqF9pneXBmkmi9C8PBJLmsEUAupfBd6DHp8%2Brg3Yi0ra5I%2B8CiuUcDDUjgTP3sdoRGEgVxxrLqD%2BoDJzZT0xFwLtj3p8vyHXxnSSB1GAcw0fuTvQY6pgE4PcrdMKroCH8JY39flQLORk8gtXS9qVyl6rctlO8XUG6kfGItGUZZCU0uJLP9ZbmsJ1Qe0%2FftNAaM6GXIYSC6vkSZLVEl8zdr7X3HuY4mk0MuxWlLy%2B4FY01qNNl5gZ8n%2F1soxAFnAVRkBuIkW3F5ohb6jleEw1C8wLBBRnIWMWbaaFG6rAfh5wax88RXCb1Rps7AUzUCGILAzo3O%2FOG6RPDqWY8t&X-Amz-Signature=67df4eca87e265d87f0fb19c74eff86cb960e7cb23125b77778beabc0e957ace&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QLKKRSBD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIBgI66%2BiBp5Di03f6ONynZkDvxd1ykh5ktEI2fzYcT5vAiAybzuH8x1NyG66HXBpKgGy13IBbLDfz6rHMxZx98Kkxyr%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIMGfFjzbdYsOaFJEyKKtwDV%2F%2B3%2Bo5b9yNos5Gvq7VjWIvECRKtAWQgqxP0A0cvAmaWfqYreoSHGmogRvo7yL%2BBp3F1QqTY81h5Ko3Azqv2FuwJnW%2FL3TeRQY2znpn0OfaIM6n12OzDhZcdmmT1Qbslff%2FvZM141Rd1TDdKyx%2FajZs2Jfvy5pbpHNWvjgtkkGYBP2yJd0j4Uz0BIP65Lss3LHdI5jtmMBrC6pGHthfwgz%2BGJkYtmuyaL1icZ4ZeiWK%2BY5Je3AjnmeSrdbxQDfRX5AniJ%2B183xEXJlkJGZ59FSMDpaxm5jSrqRzZYreX6OMTKlYbvqTc%2FSi5xb5IpE1YRaoWvsXCzGm0mLZbS7vmDq9vh2Zh3ID8bu%2B0ejaL%2BRi0P2PPb0Eadzcu9MM05tdmEvJlkzEDnZKgCHU6FnFKEEI%2F7yPGZZ%2F5z2eoBQnuBVMRSx8c%2BuZRMpS3%2B7sVnVDXtm3CMPpvuzgYfZdKcBMMJ8ltBIHx9xvuoIeMI8t%2BlPMyJxlh%2BQ3sVKhhIoCOU2NstSii6Jb%2F7nC54zPpQhpqF9pneXBmkmi9C8PBJLmsEUAupfBd6DHp8%2Brg3Yi0ra5I%2B8CiuUcDDUjgTP3sdoRGEgVxxrLqD%2BoDJzZT0xFwLtj3p8vyHXxnSSB1GAcw0fuTvQY6pgE4PcrdMKroCH8JY39flQLORk8gtXS9qVyl6rctlO8XUG6kfGItGUZZCU0uJLP9ZbmsJ1Qe0%2FftNAaM6GXIYSC6vkSZLVEl8zdr7X3HuY4mk0MuxWlLy%2B4FY01qNNl5gZ8n%2F1soxAFnAVRkBuIkW3F5ohb6jleEw1C8wLBBRnIWMWbaaFG6rAfh5wax88RXCb1Rps7AUzUCGILAzo3O%2FOG6RPDqWY8t&X-Amz-Signature=2beb8c81291ed993e8a51777649f0d9e16b2b9dfa6294fc79e12cc7074be9b25&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
