

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YDELSHQX%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJIMEYCIQCsxLWwwmkou7JmckC%2F0G%2F%2BkGSXy21X0NZ7djHjbBGx8QIhAMg7ATeVztQqBuKSBphOowAgY%2FQC%2B3iwZHHUXswn9pFnKogECIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw69c%2Fla0DAabPoKRoq3AP7VT3EI77O1mzLh71lQVq%2BUmYbOWKCav7JD%2BIay1IZFSK5dlto%2Fb0CYO9jSm99A8UjQyL4YHr%2FTkeasmaxp%2Fr24qphSsqWxWN2p6W38BQgaoLK%2Bl%2FVzO7a60l6Xw8TL3DIXyOH1h%2BQyYCIcN3nIbK0tyqPjRfXtk%2BVspmL%2Bx0jaNYPXj9xSyXL0zWcwE6s6tIN%2BtrZrfiOrTLdu4020omZ37QfEp5Cp0FsRGxdWJGl97xb%2F7Vdgbcf1mga73rYUimrwKOVEecGpbJwqwc%2Fia0tf0RqYPo4%2BUjy8Yd1RoD6ugdJ3EdVgri0Z3pw79P5UflSlKshlTEFuObwSG893LcuVzJfP3TVuYCsWmTRjxhG5ilm%2Fqdq5UckqMd4oucx3WFMTlhO9Dw2RfeEci1JK30fTvQY54ukBDtgyWiqV1KHidfK2unVx9q5otlRBuoVPx87JgoHDUdlRTmBHw4KBL%2FylwKzxvz%2FJs7xw%2FBcJAvFZZp2aeBTTDe7qc61GsomoMV5lBH3TFphNUIEQyx%2BzO%2FN5I3Z9n158BOn985Jakyhd0cSC07wq027L%2FABi63zFbQtNhrsymuVcExDRY2G3M%2BkZr9aeEDUUYPMyjPNjauI2wAVfKkP0iB1PeE%2FxTDM75u9BjqkAZ7nhFRWPZC8phwsOJKW8KSCI%2BsLOdnHvYjswcdyM5OJ%2BCdPVhqHfa1chu0oa1ImDWFyZXkXYJ%2BUq3cBzDrPuXXXr8Nsuju%2B4ISWNCSpIRO9rz5pCJu4qmNJr%2BqbluN3qEzfUl348UbuYZ17W6op6m9%2BbjCD7IaKM6luBTSJGiWa82lPvjQec42oxwbi6lKx0E1OzeyYu3bsavsv6wb8cvNGIBhA&X-Amz-Signature=999eba17792a9f8b0f310227ab7875ddada82326121f0c4ccdcde9b2d0f4bf34&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YDELSHQX%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJIMEYCIQCsxLWwwmkou7JmckC%2F0G%2F%2BkGSXy21X0NZ7djHjbBGx8QIhAMg7ATeVztQqBuKSBphOowAgY%2FQC%2B3iwZHHUXswn9pFnKogECIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw69c%2Fla0DAabPoKRoq3AP7VT3EI77O1mzLh71lQVq%2BUmYbOWKCav7JD%2BIay1IZFSK5dlto%2Fb0CYO9jSm99A8UjQyL4YHr%2FTkeasmaxp%2Fr24qphSsqWxWN2p6W38BQgaoLK%2Bl%2FVzO7a60l6Xw8TL3DIXyOH1h%2BQyYCIcN3nIbK0tyqPjRfXtk%2BVspmL%2Bx0jaNYPXj9xSyXL0zWcwE6s6tIN%2BtrZrfiOrTLdu4020omZ37QfEp5Cp0FsRGxdWJGl97xb%2F7Vdgbcf1mga73rYUimrwKOVEecGpbJwqwc%2Fia0tf0RqYPo4%2BUjy8Yd1RoD6ugdJ3EdVgri0Z3pw79P5UflSlKshlTEFuObwSG893LcuVzJfP3TVuYCsWmTRjxhG5ilm%2Fqdq5UckqMd4oucx3WFMTlhO9Dw2RfeEci1JK30fTvQY54ukBDtgyWiqV1KHidfK2unVx9q5otlRBuoVPx87JgoHDUdlRTmBHw4KBL%2FylwKzxvz%2FJs7xw%2FBcJAvFZZp2aeBTTDe7qc61GsomoMV5lBH3TFphNUIEQyx%2BzO%2FN5I3Z9n158BOn985Jakyhd0cSC07wq027L%2FABi63zFbQtNhrsymuVcExDRY2G3M%2BkZr9aeEDUUYPMyjPNjauI2wAVfKkP0iB1PeE%2FxTDM75u9BjqkAZ7nhFRWPZC8phwsOJKW8KSCI%2BsLOdnHvYjswcdyM5OJ%2BCdPVhqHfa1chu0oa1ImDWFyZXkXYJ%2BUq3cBzDrPuXXXr8Nsuju%2B4ISWNCSpIRO9rz5pCJu4qmNJr%2BqbluN3qEzfUl348UbuYZ17W6op6m9%2BbjCD7IaKM6luBTSJGiWa82lPvjQec42oxwbi6lKx0E1OzeyYu3bsavsv6wb8cvNGIBhA&X-Amz-Signature=5f279d64758baf9c0315290b892d89ab88f7b0c6b260d1132c02800c6aa49c30&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YDELSHQX%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJIMEYCIQCsxLWwwmkou7JmckC%2F0G%2F%2BkGSXy21X0NZ7djHjbBGx8QIhAMg7ATeVztQqBuKSBphOowAgY%2FQC%2B3iwZHHUXswn9pFnKogECIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw69c%2Fla0DAabPoKRoq3AP7VT3EI77O1mzLh71lQVq%2BUmYbOWKCav7JD%2BIay1IZFSK5dlto%2Fb0CYO9jSm99A8UjQyL4YHr%2FTkeasmaxp%2Fr24qphSsqWxWN2p6W38BQgaoLK%2Bl%2FVzO7a60l6Xw8TL3DIXyOH1h%2BQyYCIcN3nIbK0tyqPjRfXtk%2BVspmL%2Bx0jaNYPXj9xSyXL0zWcwE6s6tIN%2BtrZrfiOrTLdu4020omZ37QfEp5Cp0FsRGxdWJGl97xb%2F7Vdgbcf1mga73rYUimrwKOVEecGpbJwqwc%2Fia0tf0RqYPo4%2BUjy8Yd1RoD6ugdJ3EdVgri0Z3pw79P5UflSlKshlTEFuObwSG893LcuVzJfP3TVuYCsWmTRjxhG5ilm%2Fqdq5UckqMd4oucx3WFMTlhO9Dw2RfeEci1JK30fTvQY54ukBDtgyWiqV1KHidfK2unVx9q5otlRBuoVPx87JgoHDUdlRTmBHw4KBL%2FylwKzxvz%2FJs7xw%2FBcJAvFZZp2aeBTTDe7qc61GsomoMV5lBH3TFphNUIEQyx%2BzO%2FN5I3Z9n158BOn985Jakyhd0cSC07wq027L%2FABi63zFbQtNhrsymuVcExDRY2G3M%2BkZr9aeEDUUYPMyjPNjauI2wAVfKkP0iB1PeE%2FxTDM75u9BjqkAZ7nhFRWPZC8phwsOJKW8KSCI%2BsLOdnHvYjswcdyM5OJ%2BCdPVhqHfa1chu0oa1ImDWFyZXkXYJ%2BUq3cBzDrPuXXXr8Nsuju%2B4ISWNCSpIRO9rz5pCJu4qmNJr%2BqbluN3qEzfUl348UbuYZ17W6op6m9%2BbjCD7IaKM6luBTSJGiWa82lPvjQec42oxwbi6lKx0E1OzeyYu3bsavsv6wb8cvNGIBhA&X-Amz-Signature=711eb6654175635610085117398754398db9bc4119c648b479232a5364179af3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBUQMR6Y%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJGMEQCIE0fgj8XTd9otevqCipAkKsbscyX%2FqSiNlH7%2BmmDVVE9AiAwqB1ohtXHybHuLUDZpkikzjphweQBKsncPLP2MeJ9FiqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMCXjSyUQ7ABKkUJ2GKtwDSCuWwODfWVPHdisttQ5jx9W7yBAKPrM4Ppb90TBNE3%2BUHb9zjiOAkoZhXgL1bmJxY21lCfDechNaUn5BxItO5fhCg4dnqbWctJSOFoDlhRgWP6WCOHnrdJOCgTAMZI0EHyY%2BqS%2FHA0obbXLv1OH9MydlL5JfTpJZbQ2gfBm5faWgCiu8ETS0Fx24Gk2DuzUCoF5qA6atg75XuKxpn0i%2BqEzZlziSMjhar8Gmgpao6JdA%2FPPBW4TI5RzJ1vvQqPc%2Fs9GJZdDz87bYQElpKOvx%2BoQ413TjD0qF2qC68ReqUXmPEDyH%2BGN%2F8p0026VzoH5NFwv23T13b%2BwcomjaNnjIIFz7eCMpXpsUj54FYtVXMUWaknH%2BzqNwQa5qt3d1jXVwJzkvGiqeejGYYK%2B3vQJC9MyNoggz%2BSoGebCIih%2FXA9W99HO67g40a%2B%2FxifBXxlW5uXn3zXpsEPjgOYwjxncfPS%2BzeA0OpU0a6v7Qh%2Ba2cfjpDtI6OtkYyZFNC3YVI6kEV3w2xb8ts5GIvYwSAbk5Hf6ovI%2Bdlf1z5a5%2B3JQVnuAFWhRCo6CSlrS6xnTA7XKiYSvoM12cGahoQ%2BpJjgkqyOxrwLzvndesEvP3xBLkVy%2FGRkI%2BvsWc9R2H53cwo%2B%2BbvQY6pgFAyfWI%2BA%2FsUAeuKFi5wVxmd7hssxsnCC70qcvHE4KSc06ZiQzvOc%2FR7uX36jhzcG8%2BPLRchVJ2TTDpCoPKsOBkySudFYhcmDy3aWfHpS1yqQuRdHBhsDpViu%2FPJZToNtjpv9fq7Dpckb7bvROUrS6QPW1jpPd2Jac%2BOzqb%2FziGUyoGneeA6QYSNTe3GvVsti4hfpAQJyDiVe5dU5KVXoePlkndvWOA&X-Amz-Signature=34e5c053b65e73b6aafbc46507eb3032c75bf9898a27543af6ef730d1abb2919&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UPQBOXL3%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJHMEUCIDg8b1zQ8KLnmBqeQhwrCKEHmrO09tAEFeroHW0uMkCZAiEAxbh%2B9EhVY3j0Vd2CJIIi5kLonWt%2FQMvtedF%2B9v2eIuQqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH6CYKCiqC0xSb6mHCrcAw%2FAo0PzRvH7Vxk9AvV2Ez%2BgfMbjqAmpt5cbnOQ1ohMiDru7jlSJPbtmF%2FnsxbnPPk%2BHCxKabBmV9Sh9KaGkIl9nOVgxeFPQgprNa4RySYtYpv4xDOzbamjfM9vEegeYzZYRCKNn%2FzJUDlN4ekfbrzDgjMKkOUh6HR6S0yAoeAgQwIA5e1aDVGC9JOhpga%2BEhw6wPR0ui2AXGrryWRYEypliFrx0G1ivKEpvZOf1sVlL3qyH8Z7Mde7F%2Frnb7oDAbW5n0TNifqzXcibdgX%2B%2Bvfy9bbmDHkOSYUSLeuBAXajBeggVXWFQ7y4WdsJwpWDONHju8Drz5X8VebOVnCxr3Dpp%2FyW7KUlpxqzHboE3daCTMuKGMcqcJzKYczgsxEFCFNdLDWOpbZUqcY2sZ9vGt4G7Oikb47Zlq98xZFpBKc1k9fsi13anYaSoCunVqvCElWa3%2BpGWbwBDNOGIa0QyqQR5Z0tRRpddCLS46agSdAJ%2BFaouG9emDnTk%2B7E%2BwFngZZiU3iv9A6Ilj%2BG11xO71zRT44N7H9Uhi2Uqpd9g6wrEv48VgME1nXLlRdOzxbdCnR3LFDkj7q2wAlWJpMgxB0KXJq7zEvWcFDV32WzOxrp%2Bn87TiBpU7BuJO7OYMJ%2Fvm70GOqUBJX0Gesimj5YhYzf34ouJUyy%2Bi3uke%2FnBeCM8nht%2BYbPy7oNmq401wJCUmTzUFHz7yhtUOU1Uq0OHarW7yDoRTypow7%2BKUhAv9y2JWK6k%2BSOWFC%2Fxk%2F9MRmlAQN5wjztbokoq2FKjOvuatI1EbhrI8kvWsWrnt51zWydNfqR6RuWyYq6AmVPXyFCG6OvZb7TXnPV2XfMrmgjwHWyGkx%2BPCz7G%2FEu1&X-Amz-Signature=37f829e9042ca5a12204bcbf35f32fdb0e70963fcbe79fa7c044b544781bebee&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YDELSHQX%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJIMEYCIQCsxLWwwmkou7JmckC%2F0G%2F%2BkGSXy21X0NZ7djHjbBGx8QIhAMg7ATeVztQqBuKSBphOowAgY%2FQC%2B3iwZHHUXswn9pFnKogECIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw69c%2Fla0DAabPoKRoq3AP7VT3EI77O1mzLh71lQVq%2BUmYbOWKCav7JD%2BIay1IZFSK5dlto%2Fb0CYO9jSm99A8UjQyL4YHr%2FTkeasmaxp%2Fr24qphSsqWxWN2p6W38BQgaoLK%2Bl%2FVzO7a60l6Xw8TL3DIXyOH1h%2BQyYCIcN3nIbK0tyqPjRfXtk%2BVspmL%2Bx0jaNYPXj9xSyXL0zWcwE6s6tIN%2BtrZrfiOrTLdu4020omZ37QfEp5Cp0FsRGxdWJGl97xb%2F7Vdgbcf1mga73rYUimrwKOVEecGpbJwqwc%2Fia0tf0RqYPo4%2BUjy8Yd1RoD6ugdJ3EdVgri0Z3pw79P5UflSlKshlTEFuObwSG893LcuVzJfP3TVuYCsWmTRjxhG5ilm%2Fqdq5UckqMd4oucx3WFMTlhO9Dw2RfeEci1JK30fTvQY54ukBDtgyWiqV1KHidfK2unVx9q5otlRBuoVPx87JgoHDUdlRTmBHw4KBL%2FylwKzxvz%2FJs7xw%2FBcJAvFZZp2aeBTTDe7qc61GsomoMV5lBH3TFphNUIEQyx%2BzO%2FN5I3Z9n158BOn985Jakyhd0cSC07wq027L%2FABi63zFbQtNhrsymuVcExDRY2G3M%2BkZr9aeEDUUYPMyjPNjauI2wAVfKkP0iB1PeE%2FxTDM75u9BjqkAZ7nhFRWPZC8phwsOJKW8KSCI%2BsLOdnHvYjswcdyM5OJ%2BCdPVhqHfa1chu0oa1ImDWFyZXkXYJ%2BUq3cBzDrPuXXXr8Nsuju%2B4ISWNCSpIRO9rz5pCJu4qmNJr%2BqbluN3qEzfUl348UbuYZ17W6op6m9%2BbjCD7IaKM6luBTSJGiWa82lPvjQec42oxwbi6lKx0E1OzeyYu3bsavsv6wb8cvNGIBhA&X-Amz-Signature=2f7c9727f361cc22f6e909344b6021f24a0c3de5b9217a3f5a540493984004a7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YDELSHQX%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJIMEYCIQCsxLWwwmkou7JmckC%2F0G%2F%2BkGSXy21X0NZ7djHjbBGx8QIhAMg7ATeVztQqBuKSBphOowAgY%2FQC%2B3iwZHHUXswn9pFnKogECIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw69c%2Fla0DAabPoKRoq3AP7VT3EI77O1mzLh71lQVq%2BUmYbOWKCav7JD%2BIay1IZFSK5dlto%2Fb0CYO9jSm99A8UjQyL4YHr%2FTkeasmaxp%2Fr24qphSsqWxWN2p6W38BQgaoLK%2Bl%2FVzO7a60l6Xw8TL3DIXyOH1h%2BQyYCIcN3nIbK0tyqPjRfXtk%2BVspmL%2Bx0jaNYPXj9xSyXL0zWcwE6s6tIN%2BtrZrfiOrTLdu4020omZ37QfEp5Cp0FsRGxdWJGl97xb%2F7Vdgbcf1mga73rYUimrwKOVEecGpbJwqwc%2Fia0tf0RqYPo4%2BUjy8Yd1RoD6ugdJ3EdVgri0Z3pw79P5UflSlKshlTEFuObwSG893LcuVzJfP3TVuYCsWmTRjxhG5ilm%2Fqdq5UckqMd4oucx3WFMTlhO9Dw2RfeEci1JK30fTvQY54ukBDtgyWiqV1KHidfK2unVx9q5otlRBuoVPx87JgoHDUdlRTmBHw4KBL%2FylwKzxvz%2FJs7xw%2FBcJAvFZZp2aeBTTDe7qc61GsomoMV5lBH3TFphNUIEQyx%2BzO%2FN5I3Z9n158BOn985Jakyhd0cSC07wq027L%2FABi63zFbQtNhrsymuVcExDRY2G3M%2BkZr9aeEDUUYPMyjPNjauI2wAVfKkP0iB1PeE%2FxTDM75u9BjqkAZ7nhFRWPZC8phwsOJKW8KSCI%2BsLOdnHvYjswcdyM5OJ%2BCdPVhqHfa1chu0oa1ImDWFyZXkXYJ%2BUq3cBzDrPuXXXr8Nsuju%2B4ISWNCSpIRO9rz5pCJu4qmNJr%2BqbluN3qEzfUl348UbuYZ17W6op6m9%2BbjCD7IaKM6luBTSJGiWa82lPvjQec42oxwbi6lKx0E1OzeyYu3bsavsv6wb8cvNGIBhA&X-Amz-Signature=90b3cbe1363f879c9dec49943d1205a95bb63f2fcbeb6dab52ca68fdcdfa5fbe&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YDELSHQX%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJIMEYCIQCsxLWwwmkou7JmckC%2F0G%2F%2BkGSXy21X0NZ7djHjbBGx8QIhAMg7ATeVztQqBuKSBphOowAgY%2FQC%2B3iwZHHUXswn9pFnKogECIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw69c%2Fla0DAabPoKRoq3AP7VT3EI77O1mzLh71lQVq%2BUmYbOWKCav7JD%2BIay1IZFSK5dlto%2Fb0CYO9jSm99A8UjQyL4YHr%2FTkeasmaxp%2Fr24qphSsqWxWN2p6W38BQgaoLK%2Bl%2FVzO7a60l6Xw8TL3DIXyOH1h%2BQyYCIcN3nIbK0tyqPjRfXtk%2BVspmL%2Bx0jaNYPXj9xSyXL0zWcwE6s6tIN%2BtrZrfiOrTLdu4020omZ37QfEp5Cp0FsRGxdWJGl97xb%2F7Vdgbcf1mga73rYUimrwKOVEecGpbJwqwc%2Fia0tf0RqYPo4%2BUjy8Yd1RoD6ugdJ3EdVgri0Z3pw79P5UflSlKshlTEFuObwSG893LcuVzJfP3TVuYCsWmTRjxhG5ilm%2Fqdq5UckqMd4oucx3WFMTlhO9Dw2RfeEci1JK30fTvQY54ukBDtgyWiqV1KHidfK2unVx9q5otlRBuoVPx87JgoHDUdlRTmBHw4KBL%2FylwKzxvz%2FJs7xw%2FBcJAvFZZp2aeBTTDe7qc61GsomoMV5lBH3TFphNUIEQyx%2BzO%2FN5I3Z9n158BOn985Jakyhd0cSC07wq027L%2FABi63zFbQtNhrsymuVcExDRY2G3M%2BkZr9aeEDUUYPMyjPNjauI2wAVfKkP0iB1PeE%2FxTDM75u9BjqkAZ7nhFRWPZC8phwsOJKW8KSCI%2BsLOdnHvYjswcdyM5OJ%2BCdPVhqHfa1chu0oa1ImDWFyZXkXYJ%2BUq3cBzDrPuXXXr8Nsuju%2B4ISWNCSpIRO9rz5pCJu4qmNJr%2BqbluN3qEzfUl348UbuYZ17W6op6m9%2BbjCD7IaKM6luBTSJGiWa82lPvjQec42oxwbi6lKx0E1OzeyYu3bsavsv6wb8cvNGIBhA&X-Amz-Signature=00bfb85dd40ba9b03fb341325c07f6f4c4f06c89fc5c0cd3d0f87b27bb8a0f3a&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YDELSHQX%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJIMEYCIQCsxLWwwmkou7JmckC%2F0G%2F%2BkGSXy21X0NZ7djHjbBGx8QIhAMg7ATeVztQqBuKSBphOowAgY%2FQC%2B3iwZHHUXswn9pFnKogECIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw69c%2Fla0DAabPoKRoq3AP7VT3EI77O1mzLh71lQVq%2BUmYbOWKCav7JD%2BIay1IZFSK5dlto%2Fb0CYO9jSm99A8UjQyL4YHr%2FTkeasmaxp%2Fr24qphSsqWxWN2p6W38BQgaoLK%2Bl%2FVzO7a60l6Xw8TL3DIXyOH1h%2BQyYCIcN3nIbK0tyqPjRfXtk%2BVspmL%2Bx0jaNYPXj9xSyXL0zWcwE6s6tIN%2BtrZrfiOrTLdu4020omZ37QfEp5Cp0FsRGxdWJGl97xb%2F7Vdgbcf1mga73rYUimrwKOVEecGpbJwqwc%2Fia0tf0RqYPo4%2BUjy8Yd1RoD6ugdJ3EdVgri0Z3pw79P5UflSlKshlTEFuObwSG893LcuVzJfP3TVuYCsWmTRjxhG5ilm%2Fqdq5UckqMd4oucx3WFMTlhO9Dw2RfeEci1JK30fTvQY54ukBDtgyWiqV1KHidfK2unVx9q5otlRBuoVPx87JgoHDUdlRTmBHw4KBL%2FylwKzxvz%2FJs7xw%2FBcJAvFZZp2aeBTTDe7qc61GsomoMV5lBH3TFphNUIEQyx%2BzO%2FN5I3Z9n158BOn985Jakyhd0cSC07wq027L%2FABi63zFbQtNhrsymuVcExDRY2G3M%2BkZr9aeEDUUYPMyjPNjauI2wAVfKkP0iB1PeE%2FxTDM75u9BjqkAZ7nhFRWPZC8phwsOJKW8KSCI%2BsLOdnHvYjswcdyM5OJ%2BCdPVhqHfa1chu0oa1ImDWFyZXkXYJ%2BUq3cBzDrPuXXXr8Nsuju%2B4ISWNCSpIRO9rz5pCJu4qmNJr%2BqbluN3qEzfUl348UbuYZ17W6op6m9%2BbjCD7IaKM6luBTSJGiWa82lPvjQec42oxwbi6lKx0E1OzeyYu3bsavsv6wb8cvNGIBhA&X-Amz-Signature=ce0c80d1640d7eb9c7679134f8a935a374be420762856f76bf02e25013f49274&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
