

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y5FKY2Z5%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQCPaVqQ7SjWyHHaSudsb939B7tsltrsvfLE%2BO873HC3GwIgDCAvd7Ftx33AmxeQzen%2BGImJCgtNKJlbK63hHuV0wW0q%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDDG9kgjPIQXjJdov7yrcA5LWnisQ7FGUxdRiGbS%2BoI9FQLTGfZqxpzsKuKFFnfCAWlqVDmllFXDjT6Wzzx7Eqd0qdN6OV0eqsCW7otOkxCkoetEFS9t4FMl7q60J91z2f5dvzka9cgkzuZ1mGQiuGuYv0EaNJrtORlxeoGJCXp21HWCm6j9%2BNuBLefZ%2BrTUtHPMEUmP8354%2FHFi37ciPFIYTeaDSKzndBKbwpb1HKeLsrOoSAlZlGlQToTeAi94pC9FuUoNiQSdqzzWhaKzHNsdLzReYBD0MsngTQBgo1tz%2FUZ%2BinCIUNeJU4pC1QhNcv9tbpWSTecTlJNXzls35emtoobPzX4LddPVQ9MBzxGcnHWTZG%2FbDSmPcf5WNrUK8VlaA7yAe6MGfVPWjz%2FrkRcB%2BNZFVsdypWyx8NoAak6rL7wGoZfY005u%2BhyTOS83t6oxQtY2Umz4te9eDFVhrYZzNWfLsgSE8GkumT5haTgMddFNpbw%2FXRRzWGTy1OHN8dzKJErH51GHu6LefuM2BoFyF68uYCCz32LaZAHsBF4oSVmskENhJeyTT6PKqAYeSQb5iB9OSDIUql1HI%2F5JNxBHXnvOFSQv2XDzMrrtGdbfoe4KyNgYsJgGO8riGMgaxVCm%2B4skPF1bW5xCXMMv5lr0GOqUBHBylif6NIFlczpsz%2Bcj8fSFLoCsb0kk%2BuCVzX0Qtm%2FPrvqcKgNf5lzMpN9dcu63OFc97dDZoCLXtR1lRRzQnkSQEDa2JT0UKEKGSxLko9KGjBpfWFJsXA9ZajUt%2Fv3GjpBNIUWpkrhlfUM2ElCTGGDuZ9LLCrH4blVCkUbYqpWnI%2B9FMwipcS%2BeEEBaY%2BJcHfAFmjiGr20X2i75uNAjK6VGJKkyS&X-Amz-Signature=7a23d87c06fba400fff3999407f537f584e3c40fb2f6b352b0e3316b8aa50539&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y5FKY2Z5%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQCPaVqQ7SjWyHHaSudsb939B7tsltrsvfLE%2BO873HC3GwIgDCAvd7Ftx33AmxeQzen%2BGImJCgtNKJlbK63hHuV0wW0q%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDDG9kgjPIQXjJdov7yrcA5LWnisQ7FGUxdRiGbS%2BoI9FQLTGfZqxpzsKuKFFnfCAWlqVDmllFXDjT6Wzzx7Eqd0qdN6OV0eqsCW7otOkxCkoetEFS9t4FMl7q60J91z2f5dvzka9cgkzuZ1mGQiuGuYv0EaNJrtORlxeoGJCXp21HWCm6j9%2BNuBLefZ%2BrTUtHPMEUmP8354%2FHFi37ciPFIYTeaDSKzndBKbwpb1HKeLsrOoSAlZlGlQToTeAi94pC9FuUoNiQSdqzzWhaKzHNsdLzReYBD0MsngTQBgo1tz%2FUZ%2BinCIUNeJU4pC1QhNcv9tbpWSTecTlJNXzls35emtoobPzX4LddPVQ9MBzxGcnHWTZG%2FbDSmPcf5WNrUK8VlaA7yAe6MGfVPWjz%2FrkRcB%2BNZFVsdypWyx8NoAak6rL7wGoZfY005u%2BhyTOS83t6oxQtY2Umz4te9eDFVhrYZzNWfLsgSE8GkumT5haTgMddFNpbw%2FXRRzWGTy1OHN8dzKJErH51GHu6LefuM2BoFyF68uYCCz32LaZAHsBF4oSVmskENhJeyTT6PKqAYeSQb5iB9OSDIUql1HI%2F5JNxBHXnvOFSQv2XDzMrrtGdbfoe4KyNgYsJgGO8riGMgaxVCm%2B4skPF1bW5xCXMMv5lr0GOqUBHBylif6NIFlczpsz%2Bcj8fSFLoCsb0kk%2BuCVzX0Qtm%2FPrvqcKgNf5lzMpN9dcu63OFc97dDZoCLXtR1lRRzQnkSQEDa2JT0UKEKGSxLko9KGjBpfWFJsXA9ZajUt%2Fv3GjpBNIUWpkrhlfUM2ElCTGGDuZ9LLCrH4blVCkUbYqpWnI%2B9FMwipcS%2BeEEBaY%2BJcHfAFmjiGr20X2i75uNAjK6VGJKkyS&X-Amz-Signature=aaa8ce16e14c8bdb336210ebe80f9bac3397d612988a43f32e551529d0d69f66&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y5FKY2Z5%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQCPaVqQ7SjWyHHaSudsb939B7tsltrsvfLE%2BO873HC3GwIgDCAvd7Ftx33AmxeQzen%2BGImJCgtNKJlbK63hHuV0wW0q%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDDG9kgjPIQXjJdov7yrcA5LWnisQ7FGUxdRiGbS%2BoI9FQLTGfZqxpzsKuKFFnfCAWlqVDmllFXDjT6Wzzx7Eqd0qdN6OV0eqsCW7otOkxCkoetEFS9t4FMl7q60J91z2f5dvzka9cgkzuZ1mGQiuGuYv0EaNJrtORlxeoGJCXp21HWCm6j9%2BNuBLefZ%2BrTUtHPMEUmP8354%2FHFi37ciPFIYTeaDSKzndBKbwpb1HKeLsrOoSAlZlGlQToTeAi94pC9FuUoNiQSdqzzWhaKzHNsdLzReYBD0MsngTQBgo1tz%2FUZ%2BinCIUNeJU4pC1QhNcv9tbpWSTecTlJNXzls35emtoobPzX4LddPVQ9MBzxGcnHWTZG%2FbDSmPcf5WNrUK8VlaA7yAe6MGfVPWjz%2FrkRcB%2BNZFVsdypWyx8NoAak6rL7wGoZfY005u%2BhyTOS83t6oxQtY2Umz4te9eDFVhrYZzNWfLsgSE8GkumT5haTgMddFNpbw%2FXRRzWGTy1OHN8dzKJErH51GHu6LefuM2BoFyF68uYCCz32LaZAHsBF4oSVmskENhJeyTT6PKqAYeSQb5iB9OSDIUql1HI%2F5JNxBHXnvOFSQv2XDzMrrtGdbfoe4KyNgYsJgGO8riGMgaxVCm%2B4skPF1bW5xCXMMv5lr0GOqUBHBylif6NIFlczpsz%2Bcj8fSFLoCsb0kk%2BuCVzX0Qtm%2FPrvqcKgNf5lzMpN9dcu63OFc97dDZoCLXtR1lRRzQnkSQEDa2JT0UKEKGSxLko9KGjBpfWFJsXA9ZajUt%2Fv3GjpBNIUWpkrhlfUM2ElCTGGDuZ9LLCrH4blVCkUbYqpWnI%2B9FMwipcS%2BeEEBaY%2BJcHfAFmjiGr20X2i75uNAjK6VGJKkyS&X-Amz-Signature=09705b8f0c13bc9343486ae0476399454ba13a48f04a22f12d56fa4b3ab0108c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664UKZIPGA%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCICKhOFblpDf24HxBUqpAyifOpUXi2UNg1NwYwuHwvXpJAiAZE4dDRHlUj3c3GfPPKCKd2H7cwzhsbCcC4jlpwhtJBSr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIMxP15EfVN1HiRrNPQKtwDvssvp%2Fw9THBnveriTmXWWvkM91WB%2BNBv4Cv7gbtPhcrwPd6y0f8N2PiSLeTi4cd5E%2Ft8BylxRkboncRskvqRn%2FKZfM6gx%2F6fjBApWli1k59Df%2FMgqh9XDtbHLBbvUvcRQ3bPejbnfZiz3XowbHPO%2BjytVRwxMt6NHF%2BS9AjDzE0icvOOEr7RBkq%2FNAa4Dr%2BCSu5lcRxJpkmTRjCNXB%2BCI4gcr1%2F9bYsTGdYjvC2pB%2B0UrVF5QUa1vYFZWiBP1j91eCmB2rO6Ti0kRv2ASYiW%2BzAH6j7Dv1t%2FbsoMLHfeHNgzSKEe%2B2ShjdyUCd1ZC6kZW1DgTZDs2J1sf6B4GE%2BTZhfLrdigIPvBpiRnoGSqXGVMA5S6TDtASe6E4bMHswe85xGUJpmKuRWxpc5br5Ubls0Uy9dFtiU1V%2B0NbyrL188ixekfImRWzONUJNhxI%2Fg9DX6bHmBobwlSa81fEB9YFw2mpLI96VBVdg63LJFLyxhFMyT9HwKdM18zRXEHn%2BmMIR8niL%2BX9avIVq6t6r9CbPTun0x%2B7jN%2BiO0pQkYTqSMbHU81CQ8nC%2FaQEhXMGLc4NzreW0DCWcYuBkYLeSTtrZP3wtzhmCE2NRvI3e6nyoRicnUmbpnDBjW3sVAwufmWvQY6pgG%2FjKyw7mCCII8berrhSOe7LGfxjgOuZAMN7hiiGTQpfDTzzKq5USbrUtLczGdrDRdF5clgXhSlUuF1oLwvBg1Um8rTYsLqHjvNkuw9vHHa9jqqBRS2TMlyRZkT9Oc8sVNOcEZMqZzDNyLLlYY2YlI7RmH5naC2Q9lf0aG1%2F8QkrDMJXWO%2F%2FKZjkWugWlQbh4ULpwp5IIv1p6Ubcgjq0cYQci0X3NMQ&X-Amz-Signature=c283d8b4aabf6cacf22c911645667acce091c191cb6f79157a0f261936268627&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LVBHZIP%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQDWL4czZELPDraatpNHgPAyYImX9wwl%2BBYV2yd45%2BRWtwIgcSjy%2FOx%2F4ZQsA9fF5QlQwYr8M8QrVUoLDDwYvMFeK94q%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDFYubOaoGOLzh%2BDeyCrcAwUkVAFyWGDF78e7kBBfYgSaY0jxp0zTVsmJj%2F2l4kv%2Fr5DS0e2iz3tZAummwoqwk0kyWgKyZxud%2BrNOienziajXmNajd7qqVQSgdEAIGD3bFJWQhm0SnDwsYqjmzq5k5vc%2FqE2%2FBRoSn9aRwrBiXc5OqfpbjH1vlquFJErQUBq7okhNQ2EFs9qciJ%2BYU6DGUDahVAQ8%2FZsE3KUyPGA73UrUsQuJFQsR1rC6bvPK1Oti36%2Fdd1UyReryeMwBYyeHLqM1lfevXE9cNgbn5PQqQGpSiJywkx5UVQ4AC%2ByAjw6xa0KrSRajIl2wK9o9Qy7uW2WGTamaXnMxPkyjv6yJ1wEOrefHYDjyW6CyOClbYiAgYPLMdSMS6s5d%2FqNVbmeomnqAPbIUsV%2FIDZt7SPjnk66q%2Ftoc3vM6gVrco0syWAdmqnxHwXkaUJ9LBDLGTNfMxy96tphLqvbF%2BvJBXAjjT2y0VUPFfRqwXSlSxoC5TjbIUt8fuINtjucbETZqXDG09XRHA%2FOAUji2HrvJAqxlB%2BfBr%2FxQ6NOgFgsBBYCzviwcNg%2BXsx%2Bi4p3%2Fx2%2BsKog6RcOVsiWIRrhWdjHzrcRvLtVzp3UdSKeniDosvZpq0pgoZ7zBNIVC3MhopHobMPv5lr0GOqUBzN8eCtgTv%2FQYuCrcpqoXs3TbWwSwx3ucji9DoNIXysCES18U5kBEXjfFNUWUk3Y64m1hnr3952hU%2BAP6dcnTBR5w8QdMr3JDllmqABnbd5oxDF3htqB1UwIoMFcwJXo9htjRuxEG69FrFiI4fjuKtjkk4XWxsnGee6nf%2BGGIRPD7ojkjA3R1ESFl3x%2FpDLW2tJSAFHMEKB65jnJdE5o9qqeCPu%2BA&X-Amz-Signature=7195bd9c257e702fd475aae974e730e7ec179edbc9bee712ba1417d7c81e4aeb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y5FKY2Z5%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQCPaVqQ7SjWyHHaSudsb939B7tsltrsvfLE%2BO873HC3GwIgDCAvd7Ftx33AmxeQzen%2BGImJCgtNKJlbK63hHuV0wW0q%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDDG9kgjPIQXjJdov7yrcA5LWnisQ7FGUxdRiGbS%2BoI9FQLTGfZqxpzsKuKFFnfCAWlqVDmllFXDjT6Wzzx7Eqd0qdN6OV0eqsCW7otOkxCkoetEFS9t4FMl7q60J91z2f5dvzka9cgkzuZ1mGQiuGuYv0EaNJrtORlxeoGJCXp21HWCm6j9%2BNuBLefZ%2BrTUtHPMEUmP8354%2FHFi37ciPFIYTeaDSKzndBKbwpb1HKeLsrOoSAlZlGlQToTeAi94pC9FuUoNiQSdqzzWhaKzHNsdLzReYBD0MsngTQBgo1tz%2FUZ%2BinCIUNeJU4pC1QhNcv9tbpWSTecTlJNXzls35emtoobPzX4LddPVQ9MBzxGcnHWTZG%2FbDSmPcf5WNrUK8VlaA7yAe6MGfVPWjz%2FrkRcB%2BNZFVsdypWyx8NoAak6rL7wGoZfY005u%2BhyTOS83t6oxQtY2Umz4te9eDFVhrYZzNWfLsgSE8GkumT5haTgMddFNpbw%2FXRRzWGTy1OHN8dzKJErH51GHu6LefuM2BoFyF68uYCCz32LaZAHsBF4oSVmskENhJeyTT6PKqAYeSQb5iB9OSDIUql1HI%2F5JNxBHXnvOFSQv2XDzMrrtGdbfoe4KyNgYsJgGO8riGMgaxVCm%2B4skPF1bW5xCXMMv5lr0GOqUBHBylif6NIFlczpsz%2Bcj8fSFLoCsb0kk%2BuCVzX0Qtm%2FPrvqcKgNf5lzMpN9dcu63OFc97dDZoCLXtR1lRRzQnkSQEDa2JT0UKEKGSxLko9KGjBpfWFJsXA9ZajUt%2Fv3GjpBNIUWpkrhlfUM2ElCTGGDuZ9LLCrH4blVCkUbYqpWnI%2B9FMwipcS%2BeEEBaY%2BJcHfAFmjiGr20X2i75uNAjK6VGJKkyS&X-Amz-Signature=013c22c655cd464c94bbff94da324e25397736917bb01d33e17bdf8faf37feb0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y5FKY2Z5%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQCPaVqQ7SjWyHHaSudsb939B7tsltrsvfLE%2BO873HC3GwIgDCAvd7Ftx33AmxeQzen%2BGImJCgtNKJlbK63hHuV0wW0q%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDDG9kgjPIQXjJdov7yrcA5LWnisQ7FGUxdRiGbS%2BoI9FQLTGfZqxpzsKuKFFnfCAWlqVDmllFXDjT6Wzzx7Eqd0qdN6OV0eqsCW7otOkxCkoetEFS9t4FMl7q60J91z2f5dvzka9cgkzuZ1mGQiuGuYv0EaNJrtORlxeoGJCXp21HWCm6j9%2BNuBLefZ%2BrTUtHPMEUmP8354%2FHFi37ciPFIYTeaDSKzndBKbwpb1HKeLsrOoSAlZlGlQToTeAi94pC9FuUoNiQSdqzzWhaKzHNsdLzReYBD0MsngTQBgo1tz%2FUZ%2BinCIUNeJU4pC1QhNcv9tbpWSTecTlJNXzls35emtoobPzX4LddPVQ9MBzxGcnHWTZG%2FbDSmPcf5WNrUK8VlaA7yAe6MGfVPWjz%2FrkRcB%2BNZFVsdypWyx8NoAak6rL7wGoZfY005u%2BhyTOS83t6oxQtY2Umz4te9eDFVhrYZzNWfLsgSE8GkumT5haTgMddFNpbw%2FXRRzWGTy1OHN8dzKJErH51GHu6LefuM2BoFyF68uYCCz32LaZAHsBF4oSVmskENhJeyTT6PKqAYeSQb5iB9OSDIUql1HI%2F5JNxBHXnvOFSQv2XDzMrrtGdbfoe4KyNgYsJgGO8riGMgaxVCm%2B4skPF1bW5xCXMMv5lr0GOqUBHBylif6NIFlczpsz%2Bcj8fSFLoCsb0kk%2BuCVzX0Qtm%2FPrvqcKgNf5lzMpN9dcu63OFc97dDZoCLXtR1lRRzQnkSQEDa2JT0UKEKGSxLko9KGjBpfWFJsXA9ZajUt%2Fv3GjpBNIUWpkrhlfUM2ElCTGGDuZ9LLCrH4blVCkUbYqpWnI%2B9FMwipcS%2BeEEBaY%2BJcHfAFmjiGr20X2i75uNAjK6VGJKkyS&X-Amz-Signature=2a045b65a4f4f7b894937c05175db3345f14a213a66a3fa5f19cf74fc8230f60&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y5FKY2Z5%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQCPaVqQ7SjWyHHaSudsb939B7tsltrsvfLE%2BO873HC3GwIgDCAvd7Ftx33AmxeQzen%2BGImJCgtNKJlbK63hHuV0wW0q%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDDG9kgjPIQXjJdov7yrcA5LWnisQ7FGUxdRiGbS%2BoI9FQLTGfZqxpzsKuKFFnfCAWlqVDmllFXDjT6Wzzx7Eqd0qdN6OV0eqsCW7otOkxCkoetEFS9t4FMl7q60J91z2f5dvzka9cgkzuZ1mGQiuGuYv0EaNJrtORlxeoGJCXp21HWCm6j9%2BNuBLefZ%2BrTUtHPMEUmP8354%2FHFi37ciPFIYTeaDSKzndBKbwpb1HKeLsrOoSAlZlGlQToTeAi94pC9FuUoNiQSdqzzWhaKzHNsdLzReYBD0MsngTQBgo1tz%2FUZ%2BinCIUNeJU4pC1QhNcv9tbpWSTecTlJNXzls35emtoobPzX4LddPVQ9MBzxGcnHWTZG%2FbDSmPcf5WNrUK8VlaA7yAe6MGfVPWjz%2FrkRcB%2BNZFVsdypWyx8NoAak6rL7wGoZfY005u%2BhyTOS83t6oxQtY2Umz4te9eDFVhrYZzNWfLsgSE8GkumT5haTgMddFNpbw%2FXRRzWGTy1OHN8dzKJErH51GHu6LefuM2BoFyF68uYCCz32LaZAHsBF4oSVmskENhJeyTT6PKqAYeSQb5iB9OSDIUql1HI%2F5JNxBHXnvOFSQv2XDzMrrtGdbfoe4KyNgYsJgGO8riGMgaxVCm%2B4skPF1bW5xCXMMv5lr0GOqUBHBylif6NIFlczpsz%2Bcj8fSFLoCsb0kk%2BuCVzX0Qtm%2FPrvqcKgNf5lzMpN9dcu63OFc97dDZoCLXtR1lRRzQnkSQEDa2JT0UKEKGSxLko9KGjBpfWFJsXA9ZajUt%2Fv3GjpBNIUWpkrhlfUM2ElCTGGDuZ9LLCrH4blVCkUbYqpWnI%2B9FMwipcS%2BeEEBaY%2BJcHfAFmjiGr20X2i75uNAjK6VGJKkyS&X-Amz-Signature=39919552e4ad4d09e34395d45689d8c92492cbba1e76ccf9920d434abf791329&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y5FKY2Z5%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQCPaVqQ7SjWyHHaSudsb939B7tsltrsvfLE%2BO873HC3GwIgDCAvd7Ftx33AmxeQzen%2BGImJCgtNKJlbK63hHuV0wW0q%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDDG9kgjPIQXjJdov7yrcA5LWnisQ7FGUxdRiGbS%2BoI9FQLTGfZqxpzsKuKFFnfCAWlqVDmllFXDjT6Wzzx7Eqd0qdN6OV0eqsCW7otOkxCkoetEFS9t4FMl7q60J91z2f5dvzka9cgkzuZ1mGQiuGuYv0EaNJrtORlxeoGJCXp21HWCm6j9%2BNuBLefZ%2BrTUtHPMEUmP8354%2FHFi37ciPFIYTeaDSKzndBKbwpb1HKeLsrOoSAlZlGlQToTeAi94pC9FuUoNiQSdqzzWhaKzHNsdLzReYBD0MsngTQBgo1tz%2FUZ%2BinCIUNeJU4pC1QhNcv9tbpWSTecTlJNXzls35emtoobPzX4LddPVQ9MBzxGcnHWTZG%2FbDSmPcf5WNrUK8VlaA7yAe6MGfVPWjz%2FrkRcB%2BNZFVsdypWyx8NoAak6rL7wGoZfY005u%2BhyTOS83t6oxQtY2Umz4te9eDFVhrYZzNWfLsgSE8GkumT5haTgMddFNpbw%2FXRRzWGTy1OHN8dzKJErH51GHu6LefuM2BoFyF68uYCCz32LaZAHsBF4oSVmskENhJeyTT6PKqAYeSQb5iB9OSDIUql1HI%2F5JNxBHXnvOFSQv2XDzMrrtGdbfoe4KyNgYsJgGO8riGMgaxVCm%2B4skPF1bW5xCXMMv5lr0GOqUBHBylif6NIFlczpsz%2Bcj8fSFLoCsb0kk%2BuCVzX0Qtm%2FPrvqcKgNf5lzMpN9dcu63OFc97dDZoCLXtR1lRRzQnkSQEDa2JT0UKEKGSxLko9KGjBpfWFJsXA9ZajUt%2Fv3GjpBNIUWpkrhlfUM2ElCTGGDuZ9LLCrH4blVCkUbYqpWnI%2B9FMwipcS%2BeEEBaY%2BJcHfAFmjiGr20X2i75uNAjK6VGJKkyS&X-Amz-Signature=d95577abe5ae919e409fa8427fa3f6ce6f6ac1b36768cfb8268cd60fd17410b4&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
