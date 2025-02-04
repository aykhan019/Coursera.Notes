

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XLQW56I%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIBcNx1JVdhs4AAT1skOkXrUcgdNP3fjF%2FQ7TV0tAMUn0AiEA2t4Uo0bDB4qx9zcpPf%2F6ksimlVrD%2F%2B5a2VY5MdtmIIMq%2FwMIMxAAGgw2Mzc0MjMxODM4MDUiDCTTB4ZORs0yI%2BQsBSrcA8oReswkhqPZ4HjQJxODClnUL%2FmcRotUxnEBny8kj9zFgOSJWB7NTnS9%2BhOXIAjCnJHUrUMiOpM%2FlkWppLcgrIncM41WeDwmGAIyClvxyl1gY%2BpSTXhNv2ZoZSMgPxOns3tDvW5v4ew3%2FVnetN2shGsV42xycXpCeAUYaIrMJuDJhMpAAjgZlcYAHerVYijGyYp6lxojjpkrAzW%2BC0%2FloUPVNoUMv5RV5oW4W%2BDNYpCSTXRKN6iQgeRloeeggld3Zgk%2FmLoPd1QY19jNcsiHGST9NY0myU8mGFBj%2FFw6fSiCSnodD9OXUWagk1rzOV%2FJAM0Likgw86vh3sJDT0TmSIBjM8w2idRp%2BL7Q2E4rUK5lfaLvP%2BTfg%2F7Ix7LfhS4NJ5xmASIKBcvclLRUnDLIPQdeH9%2FnIIJEc2KuWZNhDe1b7MJyzzNwj68lboW75jL4pKsijrmg4Ly%2FzOE9FwdmUSG8v0sdJjNywgv4Kg3SAtOGgPX3zFrPz8zlMlwGHFTHDIGZZyLkkWhln32UdElY9MHE37Hewqd9YIie1OaTDRLdz2C%2BqRdP%2B8dZc57Cz4BqBPGoFMpyIfLjDVtwQ6VCudbKg1vVOJbdNfZJHFCs1CENHdUFCNaR0twhS%2BdVMLuhib0GOqUBAcGsBHsuQsD%2FgwlqV5xEO7ZEQ7Ax9DlyZKTdYIBp71%2FRkiFUaI2p4L%2FAFmLxkocsOTlpYb8i%2BJit9tjgtdiRghKQnFi9M4V4PJJZsNq%2Fu%2FHLxTrcT1SncovQTqBix2How7%2Fke%2BGnH3ZcadB6UdlCKgIiEZZGGEugUzmdTLgHwW0Sjf0hqp5ffObUBqnXAsXIubxxxTSgxsjbWVZjYUVP%2FRfaao3C&X-Amz-Signature=d8db5cc56b81e425a7c537e886f9e02eaf2b282dedde96dbd7de58d75462ed84&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XLQW56I%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIBcNx1JVdhs4AAT1skOkXrUcgdNP3fjF%2FQ7TV0tAMUn0AiEA2t4Uo0bDB4qx9zcpPf%2F6ksimlVrD%2F%2B5a2VY5MdtmIIMq%2FwMIMxAAGgw2Mzc0MjMxODM4MDUiDCTTB4ZORs0yI%2BQsBSrcA8oReswkhqPZ4HjQJxODClnUL%2FmcRotUxnEBny8kj9zFgOSJWB7NTnS9%2BhOXIAjCnJHUrUMiOpM%2FlkWppLcgrIncM41WeDwmGAIyClvxyl1gY%2BpSTXhNv2ZoZSMgPxOns3tDvW5v4ew3%2FVnetN2shGsV42xycXpCeAUYaIrMJuDJhMpAAjgZlcYAHerVYijGyYp6lxojjpkrAzW%2BC0%2FloUPVNoUMv5RV5oW4W%2BDNYpCSTXRKN6iQgeRloeeggld3Zgk%2FmLoPd1QY19jNcsiHGST9NY0myU8mGFBj%2FFw6fSiCSnodD9OXUWagk1rzOV%2FJAM0Likgw86vh3sJDT0TmSIBjM8w2idRp%2BL7Q2E4rUK5lfaLvP%2BTfg%2F7Ix7LfhS4NJ5xmASIKBcvclLRUnDLIPQdeH9%2FnIIJEc2KuWZNhDe1b7MJyzzNwj68lboW75jL4pKsijrmg4Ly%2FzOE9FwdmUSG8v0sdJjNywgv4Kg3SAtOGgPX3zFrPz8zlMlwGHFTHDIGZZyLkkWhln32UdElY9MHE37Hewqd9YIie1OaTDRLdz2C%2BqRdP%2B8dZc57Cz4BqBPGoFMpyIfLjDVtwQ6VCudbKg1vVOJbdNfZJHFCs1CENHdUFCNaR0twhS%2BdVMLuhib0GOqUBAcGsBHsuQsD%2FgwlqV5xEO7ZEQ7Ax9DlyZKTdYIBp71%2FRkiFUaI2p4L%2FAFmLxkocsOTlpYb8i%2BJit9tjgtdiRghKQnFi9M4V4PJJZsNq%2Fu%2FHLxTrcT1SncovQTqBix2How7%2Fke%2BGnH3ZcadB6UdlCKgIiEZZGGEugUzmdTLgHwW0Sjf0hqp5ffObUBqnXAsXIubxxxTSgxsjbWVZjYUVP%2FRfaao3C&X-Amz-Signature=430bb202bea9fc788cfede7668bd7bdfe46cddace04dcfaacce6c6fa698679b4&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XLQW56I%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIBcNx1JVdhs4AAT1skOkXrUcgdNP3fjF%2FQ7TV0tAMUn0AiEA2t4Uo0bDB4qx9zcpPf%2F6ksimlVrD%2F%2B5a2VY5MdtmIIMq%2FwMIMxAAGgw2Mzc0MjMxODM4MDUiDCTTB4ZORs0yI%2BQsBSrcA8oReswkhqPZ4HjQJxODClnUL%2FmcRotUxnEBny8kj9zFgOSJWB7NTnS9%2BhOXIAjCnJHUrUMiOpM%2FlkWppLcgrIncM41WeDwmGAIyClvxyl1gY%2BpSTXhNv2ZoZSMgPxOns3tDvW5v4ew3%2FVnetN2shGsV42xycXpCeAUYaIrMJuDJhMpAAjgZlcYAHerVYijGyYp6lxojjpkrAzW%2BC0%2FloUPVNoUMv5RV5oW4W%2BDNYpCSTXRKN6iQgeRloeeggld3Zgk%2FmLoPd1QY19jNcsiHGST9NY0myU8mGFBj%2FFw6fSiCSnodD9OXUWagk1rzOV%2FJAM0Likgw86vh3sJDT0TmSIBjM8w2idRp%2BL7Q2E4rUK5lfaLvP%2BTfg%2F7Ix7LfhS4NJ5xmASIKBcvclLRUnDLIPQdeH9%2FnIIJEc2KuWZNhDe1b7MJyzzNwj68lboW75jL4pKsijrmg4Ly%2FzOE9FwdmUSG8v0sdJjNywgv4Kg3SAtOGgPX3zFrPz8zlMlwGHFTHDIGZZyLkkWhln32UdElY9MHE37Hewqd9YIie1OaTDRLdz2C%2BqRdP%2B8dZc57Cz4BqBPGoFMpyIfLjDVtwQ6VCudbKg1vVOJbdNfZJHFCs1CENHdUFCNaR0twhS%2BdVMLuhib0GOqUBAcGsBHsuQsD%2FgwlqV5xEO7ZEQ7Ax9DlyZKTdYIBp71%2FRkiFUaI2p4L%2FAFmLxkocsOTlpYb8i%2BJit9tjgtdiRghKQnFi9M4V4PJJZsNq%2Fu%2FHLxTrcT1SncovQTqBix2How7%2Fke%2BGnH3ZcadB6UdlCKgIiEZZGGEugUzmdTLgHwW0Sjf0hqp5ffObUBqnXAsXIubxxxTSgxsjbWVZjYUVP%2FRfaao3C&X-Amz-Signature=43f96c1f0ab939ae75cea5132e7052ebf25c8994953a8f1a03de107598b8cf01&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666DRZAUHR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJIMEYCIQC2V23m2Z19YjwFVMUfP3p0YAFucD1aJf0QriefIhwvOwIhAPb1ZDXprvRBOIiD4P%2By%2Bkh06FkqZRKy0gQI8TzCevzEKv8DCDMQABoMNjM3NDIzMTgzODA1IgyNPq2avaqUnprGl7Uq3AMa859Oc1v4ukahD4nG2wyj7fU4tfzcSmEZvaJ0%2FGDC1SUyobS98mVem4NOPZrKQsec%2FG6u18AhflZeuRXkH1jhuc%2FM7OyMdA9hwl6yVl7J3lJ%2Bu%2BT1KZ7h7PtQpQl%2BpIR%2BykfRs5kKG46QEkz1TKUkyvprKM%2BTcpsvAmOQPoNMvCNSafRh0UMo0%2BBjhdurxYq3e4M%2F%2ByR7QPNL1nYpLVPLUik8V3z%2Fx67NbcqmcR00OqU89%2B05i7ZyqOme3UBIFg28azncgqx%2BIivCH4TUI6MCYs3RfC26gsix2fIedWARCQ%2FW0erTlYcg5hip5UNN686Rbp1jah7jZ%2BmKXp4Op%2FOr4Uo%2FF2HWxRVSKSVVOULvITRXU5vkdhwJcgD9aI9inAHcajVX5muH3Tkm6TNcvUg%2BBqhMGzewZnNAm%2Fdh0l4yUFG3c3t0D5CTsPmFaO8%2FE5%2BoXYHk9FbcBZHpYiOuBThDzQ3LXib%2FGaFYkRD9VG6xwehzujOlCAyykIW3khyZgNQZPNGFnfcdA%2BosOShoSl72ci4%2FR1lYGJ7Egk4xlvc7mvNWJeewC%2B9OEV2Jc3aFWOp0wdE6O6T0PkAU%2Fa1EUckBx89CyJISwZfb9XvUgvxdqZ3OWi2k0%2BrOCKlnWTDZoIm9BjqkAVLGJ3gan391SlRs2NukP%2B53pHfIRhCyIZeVPsMJhzsRNZXU%2FZYsKRBm5J5gMI1TzYn0ipGhm0Z1%2FXuUTONZxuzyzwWCToQ%2F4U%2F5249M9uE4KgYH%2BCTgixtdUsom3IR6GGyJKh16bKR%2B5uNHT2rcsSeUYZ12FampWpeuVorBeEs5Fx%2FwqEa2j0PHWDgZ2chb2nf%2BKmTMYwIbVRwmvDo9qs1THH0E&X-Amz-Signature=85761ff9e535d4a735cd65fccf47f32e061069c5c11fa4b36f70a951316bf504&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666V7XHLC3%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJGMEQCIH2QhxsDzKsEAlGsdwkXjr6Odd2Hid01Ie%2FkQNVQ0PTKAiBxErahedqydKU4NhtebNsCFJNRTDSlD16xSuynzJaY2ir%2FAwgzEAAaDDYzNzQyMzE4MzgwNSIMsWundXQoK3X%2B9zNcKtwDgncjzD4EeyHKBvDX5DP063RwMEnKc5cc57cetAEK6VlZ0xOtNwcnF2SrA1iFN5nd6aZV%2BOvddaLIuzwEvPiKnYuxOVmA19cg2lrUXYj5pYyCK%2FRbMA5lSJJ%2B1eTEMwVzW4%2BX%2FqtEE93VVAEA43BeaNM5jrDzHOzwIwkIofMDxsJIv4gb3vhytF1Hq1J74P8rQPH%2BJTUYCMCZLFd88hEnayrtys3j2UQmpXtKqAhWuXVJ2Irz2C8Wwg%2Ffs0taGezL8W04R4DmPT1kk7okoUsgdG4vtzeF8XfeWYq0U0bGKhIKF%2BH3olrX4o%2FMC9fGdvH%2FufovKv4JS2qYThjuL7jUDKbdUg%2FrrCVm2ToaTYgoopWp4PvRYiGCUDqXXG%2B452BPT0RmSTlERL9kwdAaTKE4HSjFVQU%2Fsctl8lFzCbqi%2FEDwA%2F1ifnwX4%2BHk2LyHdf2lJhHZFc641ir3vwq3bBZBfR1Jc5gq8NO7D13HUFwv7SQpX3i%2FLAUmdl4HwFvwbXvK%2FUq0PiiVpWaWqF5HXqdTBkgyBqt9rUX%2BQdBnL8XxIB02cDsIUIkd8ZFB6u9yQ8lzUjNg4jy7I1H16ZNi9iWLmYJSor%2BpzusTg8UksN3dtiDDViW9bChhhZXpD6cwpKGJvQY6pgGsVD5bcBIJaQfdcgP4SnWMS9pPYjAaMolKpSurJK0rg7HUGG4YKaT7x%2B8sRPbabN72UNy15AZekibN2aelEzWxuowmrlD94j1m6gJpdu7GN4ANDM0mKv89BU%2BewR%2BlgikOcGzL279joi9ZWo4VG1J7vEy0osu1Y1ojZXyl1mj6ZheSEPn%2BB9jE5S9cU4J0TzmnTaZLzpkvVxHunjZNhZjDqWewu1Jg&X-Amz-Signature=0bbd235037d6663e671c0208f7d7be03180bd36c4af2def3e53c742ec92acb0b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XLQW56I%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIBcNx1JVdhs4AAT1skOkXrUcgdNP3fjF%2FQ7TV0tAMUn0AiEA2t4Uo0bDB4qx9zcpPf%2F6ksimlVrD%2F%2B5a2VY5MdtmIIMq%2FwMIMxAAGgw2Mzc0MjMxODM4MDUiDCTTB4ZORs0yI%2BQsBSrcA8oReswkhqPZ4HjQJxODClnUL%2FmcRotUxnEBny8kj9zFgOSJWB7NTnS9%2BhOXIAjCnJHUrUMiOpM%2FlkWppLcgrIncM41WeDwmGAIyClvxyl1gY%2BpSTXhNv2ZoZSMgPxOns3tDvW5v4ew3%2FVnetN2shGsV42xycXpCeAUYaIrMJuDJhMpAAjgZlcYAHerVYijGyYp6lxojjpkrAzW%2BC0%2FloUPVNoUMv5RV5oW4W%2BDNYpCSTXRKN6iQgeRloeeggld3Zgk%2FmLoPd1QY19jNcsiHGST9NY0myU8mGFBj%2FFw6fSiCSnodD9OXUWagk1rzOV%2FJAM0Likgw86vh3sJDT0TmSIBjM8w2idRp%2BL7Q2E4rUK5lfaLvP%2BTfg%2F7Ix7LfhS4NJ5xmASIKBcvclLRUnDLIPQdeH9%2FnIIJEc2KuWZNhDe1b7MJyzzNwj68lboW75jL4pKsijrmg4Ly%2FzOE9FwdmUSG8v0sdJjNywgv4Kg3SAtOGgPX3zFrPz8zlMlwGHFTHDIGZZyLkkWhln32UdElY9MHE37Hewqd9YIie1OaTDRLdz2C%2BqRdP%2B8dZc57Cz4BqBPGoFMpyIfLjDVtwQ6VCudbKg1vVOJbdNfZJHFCs1CENHdUFCNaR0twhS%2BdVMLuhib0GOqUBAcGsBHsuQsD%2FgwlqV5xEO7ZEQ7Ax9DlyZKTdYIBp71%2FRkiFUaI2p4L%2FAFmLxkocsOTlpYb8i%2BJit9tjgtdiRghKQnFi9M4V4PJJZsNq%2Fu%2FHLxTrcT1SncovQTqBix2How7%2Fke%2BGnH3ZcadB6UdlCKgIiEZZGGEugUzmdTLgHwW0Sjf0hqp5ffObUBqnXAsXIubxxxTSgxsjbWVZjYUVP%2FRfaao3C&X-Amz-Signature=98442b238ef66e660658b8caf1f7ad54a066a3b40086e4eebdea4b10dbcab4a1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XLQW56I%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIBcNx1JVdhs4AAT1skOkXrUcgdNP3fjF%2FQ7TV0tAMUn0AiEA2t4Uo0bDB4qx9zcpPf%2F6ksimlVrD%2F%2B5a2VY5MdtmIIMq%2FwMIMxAAGgw2Mzc0MjMxODM4MDUiDCTTB4ZORs0yI%2BQsBSrcA8oReswkhqPZ4HjQJxODClnUL%2FmcRotUxnEBny8kj9zFgOSJWB7NTnS9%2BhOXIAjCnJHUrUMiOpM%2FlkWppLcgrIncM41WeDwmGAIyClvxyl1gY%2BpSTXhNv2ZoZSMgPxOns3tDvW5v4ew3%2FVnetN2shGsV42xycXpCeAUYaIrMJuDJhMpAAjgZlcYAHerVYijGyYp6lxojjpkrAzW%2BC0%2FloUPVNoUMv5RV5oW4W%2BDNYpCSTXRKN6iQgeRloeeggld3Zgk%2FmLoPd1QY19jNcsiHGST9NY0myU8mGFBj%2FFw6fSiCSnodD9OXUWagk1rzOV%2FJAM0Likgw86vh3sJDT0TmSIBjM8w2idRp%2BL7Q2E4rUK5lfaLvP%2BTfg%2F7Ix7LfhS4NJ5xmASIKBcvclLRUnDLIPQdeH9%2FnIIJEc2KuWZNhDe1b7MJyzzNwj68lboW75jL4pKsijrmg4Ly%2FzOE9FwdmUSG8v0sdJjNywgv4Kg3SAtOGgPX3zFrPz8zlMlwGHFTHDIGZZyLkkWhln32UdElY9MHE37Hewqd9YIie1OaTDRLdz2C%2BqRdP%2B8dZc57Cz4BqBPGoFMpyIfLjDVtwQ6VCudbKg1vVOJbdNfZJHFCs1CENHdUFCNaR0twhS%2BdVMLuhib0GOqUBAcGsBHsuQsD%2FgwlqV5xEO7ZEQ7Ax9DlyZKTdYIBp71%2FRkiFUaI2p4L%2FAFmLxkocsOTlpYb8i%2BJit9tjgtdiRghKQnFi9M4V4PJJZsNq%2Fu%2FHLxTrcT1SncovQTqBix2How7%2Fke%2BGnH3ZcadB6UdlCKgIiEZZGGEugUzmdTLgHwW0Sjf0hqp5ffObUBqnXAsXIubxxxTSgxsjbWVZjYUVP%2FRfaao3C&X-Amz-Signature=25cfcebebbb7cc175566c97dc5c528f5e4c80c640932d93e3b067ab834f43065&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XLQW56I%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIBcNx1JVdhs4AAT1skOkXrUcgdNP3fjF%2FQ7TV0tAMUn0AiEA2t4Uo0bDB4qx9zcpPf%2F6ksimlVrD%2F%2B5a2VY5MdtmIIMq%2FwMIMxAAGgw2Mzc0MjMxODM4MDUiDCTTB4ZORs0yI%2BQsBSrcA8oReswkhqPZ4HjQJxODClnUL%2FmcRotUxnEBny8kj9zFgOSJWB7NTnS9%2BhOXIAjCnJHUrUMiOpM%2FlkWppLcgrIncM41WeDwmGAIyClvxyl1gY%2BpSTXhNv2ZoZSMgPxOns3tDvW5v4ew3%2FVnetN2shGsV42xycXpCeAUYaIrMJuDJhMpAAjgZlcYAHerVYijGyYp6lxojjpkrAzW%2BC0%2FloUPVNoUMv5RV5oW4W%2BDNYpCSTXRKN6iQgeRloeeggld3Zgk%2FmLoPd1QY19jNcsiHGST9NY0myU8mGFBj%2FFw6fSiCSnodD9OXUWagk1rzOV%2FJAM0Likgw86vh3sJDT0TmSIBjM8w2idRp%2BL7Q2E4rUK5lfaLvP%2BTfg%2F7Ix7LfhS4NJ5xmASIKBcvclLRUnDLIPQdeH9%2FnIIJEc2KuWZNhDe1b7MJyzzNwj68lboW75jL4pKsijrmg4Ly%2FzOE9FwdmUSG8v0sdJjNywgv4Kg3SAtOGgPX3zFrPz8zlMlwGHFTHDIGZZyLkkWhln32UdElY9MHE37Hewqd9YIie1OaTDRLdz2C%2BqRdP%2B8dZc57Cz4BqBPGoFMpyIfLjDVtwQ6VCudbKg1vVOJbdNfZJHFCs1CENHdUFCNaR0twhS%2BdVMLuhib0GOqUBAcGsBHsuQsD%2FgwlqV5xEO7ZEQ7Ax9DlyZKTdYIBp71%2FRkiFUaI2p4L%2FAFmLxkocsOTlpYb8i%2BJit9tjgtdiRghKQnFi9M4V4PJJZsNq%2Fu%2FHLxTrcT1SncovQTqBix2How7%2Fke%2BGnH3ZcadB6UdlCKgIiEZZGGEugUzmdTLgHwW0Sjf0hqp5ffObUBqnXAsXIubxxxTSgxsjbWVZjYUVP%2FRfaao3C&X-Amz-Signature=53e8e459fa08dbb05980b91ee95414100a83fbdf2610eeb84794875f7b5a0dd4&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XLQW56I%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIBcNx1JVdhs4AAT1skOkXrUcgdNP3fjF%2FQ7TV0tAMUn0AiEA2t4Uo0bDB4qx9zcpPf%2F6ksimlVrD%2F%2B5a2VY5MdtmIIMq%2FwMIMxAAGgw2Mzc0MjMxODM4MDUiDCTTB4ZORs0yI%2BQsBSrcA8oReswkhqPZ4HjQJxODClnUL%2FmcRotUxnEBny8kj9zFgOSJWB7NTnS9%2BhOXIAjCnJHUrUMiOpM%2FlkWppLcgrIncM41WeDwmGAIyClvxyl1gY%2BpSTXhNv2ZoZSMgPxOns3tDvW5v4ew3%2FVnetN2shGsV42xycXpCeAUYaIrMJuDJhMpAAjgZlcYAHerVYijGyYp6lxojjpkrAzW%2BC0%2FloUPVNoUMv5RV5oW4W%2BDNYpCSTXRKN6iQgeRloeeggld3Zgk%2FmLoPd1QY19jNcsiHGST9NY0myU8mGFBj%2FFw6fSiCSnodD9OXUWagk1rzOV%2FJAM0Likgw86vh3sJDT0TmSIBjM8w2idRp%2BL7Q2E4rUK5lfaLvP%2BTfg%2F7Ix7LfhS4NJ5xmASIKBcvclLRUnDLIPQdeH9%2FnIIJEc2KuWZNhDe1b7MJyzzNwj68lboW75jL4pKsijrmg4Ly%2FzOE9FwdmUSG8v0sdJjNywgv4Kg3SAtOGgPX3zFrPz8zlMlwGHFTHDIGZZyLkkWhln32UdElY9MHE37Hewqd9YIie1OaTDRLdz2C%2BqRdP%2B8dZc57Cz4BqBPGoFMpyIfLjDVtwQ6VCudbKg1vVOJbdNfZJHFCs1CENHdUFCNaR0twhS%2BdVMLuhib0GOqUBAcGsBHsuQsD%2FgwlqV5xEO7ZEQ7Ax9DlyZKTdYIBp71%2FRkiFUaI2p4L%2FAFmLxkocsOTlpYb8i%2BJit9tjgtdiRghKQnFi9M4V4PJJZsNq%2Fu%2FHLxTrcT1SncovQTqBix2How7%2Fke%2BGnH3ZcadB6UdlCKgIiEZZGGEugUzmdTLgHwW0Sjf0hqp5ffObUBqnXAsXIubxxxTSgxsjbWVZjYUVP%2FRfaao3C&X-Amz-Signature=c4abe88c3017be468ded33cd4052988f1dd8a5902e7d724cb99db0ad1213944a&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
