

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YZ3GCLJA%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIQCAgHcGL6R90U%2BGIuik9l%2FbmLaesZHeQF%2F18kb%2BO0xlJwIgHro7pjBSfoJ6qi3I7jeB9awS63igisjPXBMvUuRS3d4q%2FwMIGxAAGgw2Mzc0MjMxODM4MDUiDM6ahXKdI0Er26xSfSrcA%2BB2tAAzrEObxdqS%2F7YaAeVGsccEonCPjryu5hw330ESTWFgpaSEbYutghxOups93L%2BxCkeGgYfP2dv1ulZvZ6ctQN%2BY19bHpuXMtb2N5fEE7ZFdeGLNyBOl6txQ5cimFO7YzP7AbxBSWPMMga9gMK2dXRRe0zfPS9dTvUeMeU3mKgLFtNvfe2M%2BXjciauGmPammDLga%2FMnihVbnw3YSg3NTko5%2BfKyLmtc2mDk58XEF0Rv%2FhRFvhJ38mxip4gNtofUDYMa%2FQX%2FxEMRX9OcgWy4cJZDlrhVYK7Pd7%2BqAavmZOhuPcVXprsiNxbvTQT0Aq23UtkuEd%2FNHQgVPlX51MWsbJrV2z%2Fv33gaCh%2BHoxzzHVBocUbCXsQnuWICHHrEMYkRTs3EwLGbiXimvCAoPECXdV%2F9YjNtjHo4%2BfeP%2Bw0lr%2BKATesd5QxBRlE7AxSuWG3t06SM0PnNvRMPGPvWGy5mpIaTw6KAI2fpVvRATvrxwER9qREnmLwjIDggLfbN0SafGpvLRoLmdIJIsSkStoWHTTShp700lddtj2%2B6DAsdgm4cNw33H8z1H4W0Sa4AnsQWQr%2BgmLdD3eclu3p2pyzHD5JyCjepYbywWeNTxwdjig9zTS2kaQVUvfZn8MNSDhL0GOqUBUHtGc69pCawM4FWMhrQjjT9%2BndA39FPQShFklc6p9qMHQgwcIr4JYbo%2FsfSjtqgPHxVt%2BQh4SZ7b4vs6UFaNoEWaIjy60cTlYWsNTCnF4ZeAXeQpR6daN5iEvcxzR%2FtDBbu54bcdd4BpfwKvLbAJRPE8w0%2FnlYkjVCDr9v9USjnSTE8p9LkEmbGuV7%2BNKXQaxQgjNVirZhrKvYDQuqPfk6yaS2ID&X-Amz-Signature=938030bf62d682417eb1198e6c30348830a97855d5e987362a3915120e26f1d5&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YZ3GCLJA%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIQCAgHcGL6R90U%2BGIuik9l%2FbmLaesZHeQF%2F18kb%2BO0xlJwIgHro7pjBSfoJ6qi3I7jeB9awS63igisjPXBMvUuRS3d4q%2FwMIGxAAGgw2Mzc0MjMxODM4MDUiDM6ahXKdI0Er26xSfSrcA%2BB2tAAzrEObxdqS%2F7YaAeVGsccEonCPjryu5hw330ESTWFgpaSEbYutghxOups93L%2BxCkeGgYfP2dv1ulZvZ6ctQN%2BY19bHpuXMtb2N5fEE7ZFdeGLNyBOl6txQ5cimFO7YzP7AbxBSWPMMga9gMK2dXRRe0zfPS9dTvUeMeU3mKgLFtNvfe2M%2BXjciauGmPammDLga%2FMnihVbnw3YSg3NTko5%2BfKyLmtc2mDk58XEF0Rv%2FhRFvhJ38mxip4gNtofUDYMa%2FQX%2FxEMRX9OcgWy4cJZDlrhVYK7Pd7%2BqAavmZOhuPcVXprsiNxbvTQT0Aq23UtkuEd%2FNHQgVPlX51MWsbJrV2z%2Fv33gaCh%2BHoxzzHVBocUbCXsQnuWICHHrEMYkRTs3EwLGbiXimvCAoPECXdV%2F9YjNtjHo4%2BfeP%2Bw0lr%2BKATesd5QxBRlE7AxSuWG3t06SM0PnNvRMPGPvWGy5mpIaTw6KAI2fpVvRATvrxwER9qREnmLwjIDggLfbN0SafGpvLRoLmdIJIsSkStoWHTTShp700lddtj2%2B6DAsdgm4cNw33H8z1H4W0Sa4AnsQWQr%2BgmLdD3eclu3p2pyzHD5JyCjepYbywWeNTxwdjig9zTS2kaQVUvfZn8MNSDhL0GOqUBUHtGc69pCawM4FWMhrQjjT9%2BndA39FPQShFklc6p9qMHQgwcIr4JYbo%2FsfSjtqgPHxVt%2BQh4SZ7b4vs6UFaNoEWaIjy60cTlYWsNTCnF4ZeAXeQpR6daN5iEvcxzR%2FtDBbu54bcdd4BpfwKvLbAJRPE8w0%2FnlYkjVCDr9v9USjnSTE8p9LkEmbGuV7%2BNKXQaxQgjNVirZhrKvYDQuqPfk6yaS2ID&X-Amz-Signature=f3aa0ce21d5799f2edac585267b9cecf58ac3d27ba341968b14e03df69b555f1&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YZ3GCLJA%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIQCAgHcGL6R90U%2BGIuik9l%2FbmLaesZHeQF%2F18kb%2BO0xlJwIgHro7pjBSfoJ6qi3I7jeB9awS63igisjPXBMvUuRS3d4q%2FwMIGxAAGgw2Mzc0MjMxODM4MDUiDM6ahXKdI0Er26xSfSrcA%2BB2tAAzrEObxdqS%2F7YaAeVGsccEonCPjryu5hw330ESTWFgpaSEbYutghxOups93L%2BxCkeGgYfP2dv1ulZvZ6ctQN%2BY19bHpuXMtb2N5fEE7ZFdeGLNyBOl6txQ5cimFO7YzP7AbxBSWPMMga9gMK2dXRRe0zfPS9dTvUeMeU3mKgLFtNvfe2M%2BXjciauGmPammDLga%2FMnihVbnw3YSg3NTko5%2BfKyLmtc2mDk58XEF0Rv%2FhRFvhJ38mxip4gNtofUDYMa%2FQX%2FxEMRX9OcgWy4cJZDlrhVYK7Pd7%2BqAavmZOhuPcVXprsiNxbvTQT0Aq23UtkuEd%2FNHQgVPlX51MWsbJrV2z%2Fv33gaCh%2BHoxzzHVBocUbCXsQnuWICHHrEMYkRTs3EwLGbiXimvCAoPECXdV%2F9YjNtjHo4%2BfeP%2Bw0lr%2BKATesd5QxBRlE7AxSuWG3t06SM0PnNvRMPGPvWGy5mpIaTw6KAI2fpVvRATvrxwER9qREnmLwjIDggLfbN0SafGpvLRoLmdIJIsSkStoWHTTShp700lddtj2%2B6DAsdgm4cNw33H8z1H4W0Sa4AnsQWQr%2BgmLdD3eclu3p2pyzHD5JyCjepYbywWeNTxwdjig9zTS2kaQVUvfZn8MNSDhL0GOqUBUHtGc69pCawM4FWMhrQjjT9%2BndA39FPQShFklc6p9qMHQgwcIr4JYbo%2FsfSjtqgPHxVt%2BQh4SZ7b4vs6UFaNoEWaIjy60cTlYWsNTCnF4ZeAXeQpR6daN5iEvcxzR%2FtDBbu54bcdd4BpfwKvLbAJRPE8w0%2FnlYkjVCDr9v9USjnSTE8p9LkEmbGuV7%2BNKXQaxQgjNVirZhrKvYDQuqPfk6yaS2ID&X-Amz-Signature=42b6d5f0c437e103130c42b1202074f6462f162bf288f7cc676096157538d70d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNEKHOIL%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJGMEQCIHQ%2BfYTCb33nck2L6L%2FGl9rtF1tdH6dkWzYNg%2F0oyM7sAiBqxzUu2AJKtW32PV1bJrrgTFqRK8pQY01rW%2BC4DC0dwCr%2FAwgbEAAaDDYzNzQyMzE4MzgwNSIMoUZs10ANtNOFH7ieKtwDJMZf8KfRAVx8xcEPcQaOPFXSnykrAmeXUArtiR36VqxnOsF8hbGPIGRYRi8DYbUq9Rb1tl3Mg0uNdX1oTLem14HGO9BnvAkcGo%2BTm4So4jz5SGvUZmnVY2T0JXSMcO15VycbE%2BzRkizEChdwvrbEdj%2FgkCaKSUO8DZ8YeDNxn18uTYvNRt0DdocC4oqYD2FQSrVdhSejPc%2BgODdmXOA8BSPSrLEibMdHCB8zfyPjj7kOFq3chPsuLln1SUMJ06fPVsuFNffBwrxhJrflkd6QN5ibl8Ue3hb8RtYixfqyyj%2FbE1c1WREt85fN74ELFikCpCvrMFKKqJGequKevHYB86MOcdL%2Bm23kLkqCZdnsd2V4ZrWRT0T1Iasw4a4CMU%2BDFpD4i9StAqsa7bhz9FHgNYaz%2Fb5UgZ3Az6wlqWb5iIZ4KfWJENh4I%2BrPDtKNUxg4HsTDV5YQy8veXlpvvKTc0yXNXqmdvG613B%2F5CRL7z96gV%2FR08PIMzQSBa5RN1fgTMVJ5iUiuuswDkv1Uch4zGo8jCebGurjQ6xtex1Gvpq01hlIWY%2FUcJ4KUrGr0hxmpW4OM3uGI8yV5jkWB%2FwG0spAv03D%2F61jZwluVyraMsoIUosgQWA5Igfu5Ld8wy4OEvQY6pgFOJkajeHWFMvHkMcaYD3D%2B%2BAyTwuCQPdhz4%2Blrjbb1GynmOovnG9K20wOuTnvfrKN77%2B0ZFB2GxPnz19Yb2daFaAq6zJaHEPdW0U1SKTPCSL1p0eubNIQ3moVIlTkx3k48w0NH8CmaXZfXbzHfOMVIhDGTaVozxZu1okLQ3AmrMs334XjLTNZmP2IO2plvUPikuyZBFbREynFYB3e5HtZEAYxqZ51f&X-Amz-Signature=2ee86c2bbda6ea04dc7552f5fb46cb6d99a9211c217dba4d1e459877654592de&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QTT4V64%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJIMEYCIQCnHgdSOPUSZhZ8kNUkxAPQkpHhDcCdsY4suaUQ2H9jdQIhAJZ2rpBeewbl6pSa3lHqTbbEhMiGZMOp%2B0wEG10Mp2AJKv8DCBsQABoMNjM3NDIzMTgzODA1IgymHRu3YIr9zrIwjPsq3AM1oykgkIKRMaBdwnifu2q0OE17pgzIrfblkK9XUmHgV2vCrvOW3VcHGRHhBO48h853xmQpwZ5ULngL00OXB1kdZpfryfvJ6k44YbyUswPSN3mFRQkOjxScm7HVVn25M4LuuYb7f9Cp%2FEKT6A706w%2F6eD3pZMly2g%2B2Oo9Pzy2WINEWWPFwgTyF5jve7%2F0HCczWlbbpGjyIIo0BHxM84hYCJ2bUB3xSajCpmi6LZD09R5bCfi4670irEQeA4S4ls1oXGEuRxqbH%2BYdTTzm2akwYe%2BLXT5ejRfILrFVNcRZgeV4LxhKGCEXd0yUNoiY8Ut4lJ%2F6eNIeQ7DaVOarbxbPTs43Qcn1UdIc7V42LaurO2KLXwIYr6758z2BfQzDKHADnxi7Juvt7obfLKwflvoOHtFEO0gw97OE%2FE51bwQCPgLa6rxVsV8e7YXW%2FAhf%2Bij3UtizxHQQ0ijIJY%2BG7xnkAw5%2FvpRAgZlgu0id63tDievHzRWgpANl7OD%2BRim4CjzKWVpo7imXqjdTEnn1YjETzdOcaLNIg3eOtR%2BhQg9%2FJ2HfglImJhPHPE%2BnCg%2Bh%2BNXx54vZQodvgpH9aeoookYyTAmTjD%2FoI3Xi%2Bf7tqt5943WZNmdpeL08Bt9oVSDCfg4S9BjqkAZYyveegQfpNEg7MKSMuAOVTxrJbwXo8z7VQpLZuvS%2Fu6dsdACWXuOLNjlnaBu3%2FkvvFBgyP%2FYWxmPZcwUkqWr8%2BoTdIpWPLZsYgv1MLpPDXJdX73i5egdF7jzzqYkQIcx7MnSxYO6otjgfUwsn743G6e%2Fl%2FizoIH34BkKHR9OOZxxmPdqI%2BFQhEm%2F%2F8IMvZFT7DdDi2Bq5m7VByrtKAL9%2BvU0Ru&X-Amz-Signature=a55eda80487613d45b210b947f46404635e06a6514d3924354185f211feb1129&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YZ3GCLJA%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIQCAgHcGL6R90U%2BGIuik9l%2FbmLaesZHeQF%2F18kb%2BO0xlJwIgHro7pjBSfoJ6qi3I7jeB9awS63igisjPXBMvUuRS3d4q%2FwMIGxAAGgw2Mzc0MjMxODM4MDUiDM6ahXKdI0Er26xSfSrcA%2BB2tAAzrEObxdqS%2F7YaAeVGsccEonCPjryu5hw330ESTWFgpaSEbYutghxOups93L%2BxCkeGgYfP2dv1ulZvZ6ctQN%2BY19bHpuXMtb2N5fEE7ZFdeGLNyBOl6txQ5cimFO7YzP7AbxBSWPMMga9gMK2dXRRe0zfPS9dTvUeMeU3mKgLFtNvfe2M%2BXjciauGmPammDLga%2FMnihVbnw3YSg3NTko5%2BfKyLmtc2mDk58XEF0Rv%2FhRFvhJ38mxip4gNtofUDYMa%2FQX%2FxEMRX9OcgWy4cJZDlrhVYK7Pd7%2BqAavmZOhuPcVXprsiNxbvTQT0Aq23UtkuEd%2FNHQgVPlX51MWsbJrV2z%2Fv33gaCh%2BHoxzzHVBocUbCXsQnuWICHHrEMYkRTs3EwLGbiXimvCAoPECXdV%2F9YjNtjHo4%2BfeP%2Bw0lr%2BKATesd5QxBRlE7AxSuWG3t06SM0PnNvRMPGPvWGy5mpIaTw6KAI2fpVvRATvrxwER9qREnmLwjIDggLfbN0SafGpvLRoLmdIJIsSkStoWHTTShp700lddtj2%2B6DAsdgm4cNw33H8z1H4W0Sa4AnsQWQr%2BgmLdD3eclu3p2pyzHD5JyCjepYbywWeNTxwdjig9zTS2kaQVUvfZn8MNSDhL0GOqUBUHtGc69pCawM4FWMhrQjjT9%2BndA39FPQShFklc6p9qMHQgwcIr4JYbo%2FsfSjtqgPHxVt%2BQh4SZ7b4vs6UFaNoEWaIjy60cTlYWsNTCnF4ZeAXeQpR6daN5iEvcxzR%2FtDBbu54bcdd4BpfwKvLbAJRPE8w0%2FnlYkjVCDr9v9USjnSTE8p9LkEmbGuV7%2BNKXQaxQgjNVirZhrKvYDQuqPfk6yaS2ID&X-Amz-Signature=2be33e60ced13c1b09787c5b9eaf3b177b8134af6a9d60e5619ddd7efc032ebf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YZ3GCLJA%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIQCAgHcGL6R90U%2BGIuik9l%2FbmLaesZHeQF%2F18kb%2BO0xlJwIgHro7pjBSfoJ6qi3I7jeB9awS63igisjPXBMvUuRS3d4q%2FwMIGxAAGgw2Mzc0MjMxODM4MDUiDM6ahXKdI0Er26xSfSrcA%2BB2tAAzrEObxdqS%2F7YaAeVGsccEonCPjryu5hw330ESTWFgpaSEbYutghxOups93L%2BxCkeGgYfP2dv1ulZvZ6ctQN%2BY19bHpuXMtb2N5fEE7ZFdeGLNyBOl6txQ5cimFO7YzP7AbxBSWPMMga9gMK2dXRRe0zfPS9dTvUeMeU3mKgLFtNvfe2M%2BXjciauGmPammDLga%2FMnihVbnw3YSg3NTko5%2BfKyLmtc2mDk58XEF0Rv%2FhRFvhJ38mxip4gNtofUDYMa%2FQX%2FxEMRX9OcgWy4cJZDlrhVYK7Pd7%2BqAavmZOhuPcVXprsiNxbvTQT0Aq23UtkuEd%2FNHQgVPlX51MWsbJrV2z%2Fv33gaCh%2BHoxzzHVBocUbCXsQnuWICHHrEMYkRTs3EwLGbiXimvCAoPECXdV%2F9YjNtjHo4%2BfeP%2Bw0lr%2BKATesd5QxBRlE7AxSuWG3t06SM0PnNvRMPGPvWGy5mpIaTw6KAI2fpVvRATvrxwER9qREnmLwjIDggLfbN0SafGpvLRoLmdIJIsSkStoWHTTShp700lddtj2%2B6DAsdgm4cNw33H8z1H4W0Sa4AnsQWQr%2BgmLdD3eclu3p2pyzHD5JyCjepYbywWeNTxwdjig9zTS2kaQVUvfZn8MNSDhL0GOqUBUHtGc69pCawM4FWMhrQjjT9%2BndA39FPQShFklc6p9qMHQgwcIr4JYbo%2FsfSjtqgPHxVt%2BQh4SZ7b4vs6UFaNoEWaIjy60cTlYWsNTCnF4ZeAXeQpR6daN5iEvcxzR%2FtDBbu54bcdd4BpfwKvLbAJRPE8w0%2FnlYkjVCDr9v9USjnSTE8p9LkEmbGuV7%2BNKXQaxQgjNVirZhrKvYDQuqPfk6yaS2ID&X-Amz-Signature=96ffcbe447b613a787ee082749552598b5c49142d50933bd901eb9498de20bbd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YZ3GCLJA%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIQCAgHcGL6R90U%2BGIuik9l%2FbmLaesZHeQF%2F18kb%2BO0xlJwIgHro7pjBSfoJ6qi3I7jeB9awS63igisjPXBMvUuRS3d4q%2FwMIGxAAGgw2Mzc0MjMxODM4MDUiDM6ahXKdI0Er26xSfSrcA%2BB2tAAzrEObxdqS%2F7YaAeVGsccEonCPjryu5hw330ESTWFgpaSEbYutghxOups93L%2BxCkeGgYfP2dv1ulZvZ6ctQN%2BY19bHpuXMtb2N5fEE7ZFdeGLNyBOl6txQ5cimFO7YzP7AbxBSWPMMga9gMK2dXRRe0zfPS9dTvUeMeU3mKgLFtNvfe2M%2BXjciauGmPammDLga%2FMnihVbnw3YSg3NTko5%2BfKyLmtc2mDk58XEF0Rv%2FhRFvhJ38mxip4gNtofUDYMa%2FQX%2FxEMRX9OcgWy4cJZDlrhVYK7Pd7%2BqAavmZOhuPcVXprsiNxbvTQT0Aq23UtkuEd%2FNHQgVPlX51MWsbJrV2z%2Fv33gaCh%2BHoxzzHVBocUbCXsQnuWICHHrEMYkRTs3EwLGbiXimvCAoPECXdV%2F9YjNtjHo4%2BfeP%2Bw0lr%2BKATesd5QxBRlE7AxSuWG3t06SM0PnNvRMPGPvWGy5mpIaTw6KAI2fpVvRATvrxwER9qREnmLwjIDggLfbN0SafGpvLRoLmdIJIsSkStoWHTTShp700lddtj2%2B6DAsdgm4cNw33H8z1H4W0Sa4AnsQWQr%2BgmLdD3eclu3p2pyzHD5JyCjepYbywWeNTxwdjig9zTS2kaQVUvfZn8MNSDhL0GOqUBUHtGc69pCawM4FWMhrQjjT9%2BndA39FPQShFklc6p9qMHQgwcIr4JYbo%2FsfSjtqgPHxVt%2BQh4SZ7b4vs6UFaNoEWaIjy60cTlYWsNTCnF4ZeAXeQpR6daN5iEvcxzR%2FtDBbu54bcdd4BpfwKvLbAJRPE8w0%2FnlYkjVCDr9v9USjnSTE8p9LkEmbGuV7%2BNKXQaxQgjNVirZhrKvYDQuqPfk6yaS2ID&X-Amz-Signature=be72a1f8667736c22b14db3b592d360d16ec5a8814a42ba810c7621d1e262ce8&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YZ3GCLJA%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIQCAgHcGL6R90U%2BGIuik9l%2FbmLaesZHeQF%2F18kb%2BO0xlJwIgHro7pjBSfoJ6qi3I7jeB9awS63igisjPXBMvUuRS3d4q%2FwMIGxAAGgw2Mzc0MjMxODM4MDUiDM6ahXKdI0Er26xSfSrcA%2BB2tAAzrEObxdqS%2F7YaAeVGsccEonCPjryu5hw330ESTWFgpaSEbYutghxOups93L%2BxCkeGgYfP2dv1ulZvZ6ctQN%2BY19bHpuXMtb2N5fEE7ZFdeGLNyBOl6txQ5cimFO7YzP7AbxBSWPMMga9gMK2dXRRe0zfPS9dTvUeMeU3mKgLFtNvfe2M%2BXjciauGmPammDLga%2FMnihVbnw3YSg3NTko5%2BfKyLmtc2mDk58XEF0Rv%2FhRFvhJ38mxip4gNtofUDYMa%2FQX%2FxEMRX9OcgWy4cJZDlrhVYK7Pd7%2BqAavmZOhuPcVXprsiNxbvTQT0Aq23UtkuEd%2FNHQgVPlX51MWsbJrV2z%2Fv33gaCh%2BHoxzzHVBocUbCXsQnuWICHHrEMYkRTs3EwLGbiXimvCAoPECXdV%2F9YjNtjHo4%2BfeP%2Bw0lr%2BKATesd5QxBRlE7AxSuWG3t06SM0PnNvRMPGPvWGy5mpIaTw6KAI2fpVvRATvrxwER9qREnmLwjIDggLfbN0SafGpvLRoLmdIJIsSkStoWHTTShp700lddtj2%2B6DAsdgm4cNw33H8z1H4W0Sa4AnsQWQr%2BgmLdD3eclu3p2pyzHD5JyCjepYbywWeNTxwdjig9zTS2kaQVUvfZn8MNSDhL0GOqUBUHtGc69pCawM4FWMhrQjjT9%2BndA39FPQShFklc6p9qMHQgwcIr4JYbo%2FsfSjtqgPHxVt%2BQh4SZ7b4vs6UFaNoEWaIjy60cTlYWsNTCnF4ZeAXeQpR6daN5iEvcxzR%2FtDBbu54bcdd4BpfwKvLbAJRPE8w0%2FnlYkjVCDr9v9USjnSTE8p9LkEmbGuV7%2BNKXQaxQgjNVirZhrKvYDQuqPfk6yaS2ID&X-Amz-Signature=c21c509fd0184051e5dc938f384a4f37de9e6bef9a1b245756cbbe0e530bc489&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
