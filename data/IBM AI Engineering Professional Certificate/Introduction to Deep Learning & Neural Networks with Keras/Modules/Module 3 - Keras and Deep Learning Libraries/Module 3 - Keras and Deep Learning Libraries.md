

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ZGM2YEJ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJGMEQCIH2NgS6dpps4tI3NH9QYN49F%2BsLSCKYN1DE%2FPpPZQ%2BkdAiAeL4Dt4mODTQHTUur6t1kpOrIDzVfZiB7orU%2FMdWlufir%2FAwhREAAaDDYzNzQyMzE4MzgwNSIMGhuFQUyOEsSDXU37KtwDeq5dZBnRkXoCfC%2BU4N3E2j2BrpQ2Rqt2FzvbBJmcO3AqofRcSCVWzfhC%2B3psdO1CyM1V9OeutNxeqfxkDO%2FhThdbNXP%2FNeNB2IsM8TehXiz5j31WQN6Yn9fBrmkZ2liRE3hyqwhm7iNYI%2BuwdAhskDmCsqBqAsX6w4F5xwWV7DGg068GyL7XeM4gWAIyhu92%2BqC2O4DDfj9kI3OUTQ%2BqfTgqooFu21QyGWvGKpzChXwtdpUNQKo5L%2BKejCNKXk6uhzhy2C7rB%2F7bdUIPmgxXlTCxnqb3IWyFDBGjYmW0yIkdUImcVOMcnlYQPofAUJbbM%2F3itBeoQLfjTM7O3uOvQdGiqXFAYSBtCYEbq8CbfU1VUZP5ElfhypowpOZXwb1cFvhRJvkGwpqUJAnGKjnFBlAppO5KEhX7fd1Qr9blPppq%2FRMyUnRhiUqcKqUiyxCWM4efMkrLcgEqmjVLvchSTIKSY1RDRm%2FpsfZYHEqeKoUMnm7RJGm3En5Dk9tJdSwWIJDAZeIHLGUBFvuNB6HvnMauM9Ss2GCdkduUdox9iHr05J7Y%2FbG6kH5PlHseIk7dhyRZISY2yqNF%2B44U3rpyvoLc2WJdpcetLtp91p4ClPHXFhbz%2F4HyUM3NQWAwzOqPvQY6pgEFl4KtS5RIMpVwz8v%2FVf4vniYL%2FDWL3Tvj9P0QaMczoRGLED1jDAyuEvFeD3SL3GwynmgVQm0L%2FT5Mqxi8d5ag2sgVwIKvg%2F%2FH%2BCLLRr8cItmDmYZdUGfUfoevL%2FgGe%2F9lGd2y9PcHniABomS5FjUcBfUgGc%2Fn19BBztnswUg%2FlJJM2x20LOyAgNmGprCO2bmc5xwd5LMUH4m4MVmoifkC%2FRB5xu4g&X-Amz-Signature=2748bf4b9a00329872a161363f787cbece0ef963f3fd52c111e9364c010ce0f1&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ZGM2YEJ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJGMEQCIH2NgS6dpps4tI3NH9QYN49F%2BsLSCKYN1DE%2FPpPZQ%2BkdAiAeL4Dt4mODTQHTUur6t1kpOrIDzVfZiB7orU%2FMdWlufir%2FAwhREAAaDDYzNzQyMzE4MzgwNSIMGhuFQUyOEsSDXU37KtwDeq5dZBnRkXoCfC%2BU4N3E2j2BrpQ2Rqt2FzvbBJmcO3AqofRcSCVWzfhC%2B3psdO1CyM1V9OeutNxeqfxkDO%2FhThdbNXP%2FNeNB2IsM8TehXiz5j31WQN6Yn9fBrmkZ2liRE3hyqwhm7iNYI%2BuwdAhskDmCsqBqAsX6w4F5xwWV7DGg068GyL7XeM4gWAIyhu92%2BqC2O4DDfj9kI3OUTQ%2BqfTgqooFu21QyGWvGKpzChXwtdpUNQKo5L%2BKejCNKXk6uhzhy2C7rB%2F7bdUIPmgxXlTCxnqb3IWyFDBGjYmW0yIkdUImcVOMcnlYQPofAUJbbM%2F3itBeoQLfjTM7O3uOvQdGiqXFAYSBtCYEbq8CbfU1VUZP5ElfhypowpOZXwb1cFvhRJvkGwpqUJAnGKjnFBlAppO5KEhX7fd1Qr9blPppq%2FRMyUnRhiUqcKqUiyxCWM4efMkrLcgEqmjVLvchSTIKSY1RDRm%2FpsfZYHEqeKoUMnm7RJGm3En5Dk9tJdSwWIJDAZeIHLGUBFvuNB6HvnMauM9Ss2GCdkduUdox9iHr05J7Y%2FbG6kH5PlHseIk7dhyRZISY2yqNF%2B44U3rpyvoLc2WJdpcetLtp91p4ClPHXFhbz%2F4HyUM3NQWAwzOqPvQY6pgEFl4KtS5RIMpVwz8v%2FVf4vniYL%2FDWL3Tvj9P0QaMczoRGLED1jDAyuEvFeD3SL3GwynmgVQm0L%2FT5Mqxi8d5ag2sgVwIKvg%2F%2FH%2BCLLRr8cItmDmYZdUGfUfoevL%2FgGe%2F9lGd2y9PcHniABomS5FjUcBfUgGc%2Fn19BBztnswUg%2FlJJM2x20LOyAgNmGprCO2bmc5xwd5LMUH4m4MVmoifkC%2FRB5xu4g&X-Amz-Signature=4d1b37f9f4fe0b54631fca4cae53e524ad6950a54f1c955cfd25ee10fca04422&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ZGM2YEJ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJGMEQCIH2NgS6dpps4tI3NH9QYN49F%2BsLSCKYN1DE%2FPpPZQ%2BkdAiAeL4Dt4mODTQHTUur6t1kpOrIDzVfZiB7orU%2FMdWlufir%2FAwhREAAaDDYzNzQyMzE4MzgwNSIMGhuFQUyOEsSDXU37KtwDeq5dZBnRkXoCfC%2BU4N3E2j2BrpQ2Rqt2FzvbBJmcO3AqofRcSCVWzfhC%2B3psdO1CyM1V9OeutNxeqfxkDO%2FhThdbNXP%2FNeNB2IsM8TehXiz5j31WQN6Yn9fBrmkZ2liRE3hyqwhm7iNYI%2BuwdAhskDmCsqBqAsX6w4F5xwWV7DGg068GyL7XeM4gWAIyhu92%2BqC2O4DDfj9kI3OUTQ%2BqfTgqooFu21QyGWvGKpzChXwtdpUNQKo5L%2BKejCNKXk6uhzhy2C7rB%2F7bdUIPmgxXlTCxnqb3IWyFDBGjYmW0yIkdUImcVOMcnlYQPofAUJbbM%2F3itBeoQLfjTM7O3uOvQdGiqXFAYSBtCYEbq8CbfU1VUZP5ElfhypowpOZXwb1cFvhRJvkGwpqUJAnGKjnFBlAppO5KEhX7fd1Qr9blPppq%2FRMyUnRhiUqcKqUiyxCWM4efMkrLcgEqmjVLvchSTIKSY1RDRm%2FpsfZYHEqeKoUMnm7RJGm3En5Dk9tJdSwWIJDAZeIHLGUBFvuNB6HvnMauM9Ss2GCdkduUdox9iHr05J7Y%2FbG6kH5PlHseIk7dhyRZISY2yqNF%2B44U3rpyvoLc2WJdpcetLtp91p4ClPHXFhbz%2F4HyUM3NQWAwzOqPvQY6pgEFl4KtS5RIMpVwz8v%2FVf4vniYL%2FDWL3Tvj9P0QaMczoRGLED1jDAyuEvFeD3SL3GwynmgVQm0L%2FT5Mqxi8d5ag2sgVwIKvg%2F%2FH%2BCLLRr8cItmDmYZdUGfUfoevL%2FgGe%2F9lGd2y9PcHniABomS5FjUcBfUgGc%2Fn19BBztnswUg%2FlJJM2x20LOyAgNmGprCO2bmc5xwd5LMUH4m4MVmoifkC%2FRB5xu4g&X-Amz-Signature=fc67a78e31bc5c296670308928909411c14e6c0d1dac335aa55bad8d3f48cc93&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ZGM2YEJ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJGMEQCIH2NgS6dpps4tI3NH9QYN49F%2BsLSCKYN1DE%2FPpPZQ%2BkdAiAeL4Dt4mODTQHTUur6t1kpOrIDzVfZiB7orU%2FMdWlufir%2FAwhREAAaDDYzNzQyMzE4MzgwNSIMGhuFQUyOEsSDXU37KtwDeq5dZBnRkXoCfC%2BU4N3E2j2BrpQ2Rqt2FzvbBJmcO3AqofRcSCVWzfhC%2B3psdO1CyM1V9OeutNxeqfxkDO%2FhThdbNXP%2FNeNB2IsM8TehXiz5j31WQN6Yn9fBrmkZ2liRE3hyqwhm7iNYI%2BuwdAhskDmCsqBqAsX6w4F5xwWV7DGg068GyL7XeM4gWAIyhu92%2BqC2O4DDfj9kI3OUTQ%2BqfTgqooFu21QyGWvGKpzChXwtdpUNQKo5L%2BKejCNKXk6uhzhy2C7rB%2F7bdUIPmgxXlTCxnqb3IWyFDBGjYmW0yIkdUImcVOMcnlYQPofAUJbbM%2F3itBeoQLfjTM7O3uOvQdGiqXFAYSBtCYEbq8CbfU1VUZP5ElfhypowpOZXwb1cFvhRJvkGwpqUJAnGKjnFBlAppO5KEhX7fd1Qr9blPppq%2FRMyUnRhiUqcKqUiyxCWM4efMkrLcgEqmjVLvchSTIKSY1RDRm%2FpsfZYHEqeKoUMnm7RJGm3En5Dk9tJdSwWIJDAZeIHLGUBFvuNB6HvnMauM9Ss2GCdkduUdox9iHr05J7Y%2FbG6kH5PlHseIk7dhyRZISY2yqNF%2B44U3rpyvoLc2WJdpcetLtp91p4ClPHXFhbz%2F4HyUM3NQWAwzOqPvQY6pgEFl4KtS5RIMpVwz8v%2FVf4vniYL%2FDWL3Tvj9P0QaMczoRGLED1jDAyuEvFeD3SL3GwynmgVQm0L%2FT5Mqxi8d5ag2sgVwIKvg%2F%2FH%2BCLLRr8cItmDmYZdUGfUfoevL%2FgGe%2F9lGd2y9PcHniABomS5FjUcBfUgGc%2Fn19BBztnswUg%2FlJJM2x20LOyAgNmGprCO2bmc5xwd5LMUH4m4MVmoifkC%2FRB5xu4g&X-Amz-Signature=098d33fea2bf21adc6c90b4165c5467de14a35ead7afdc97002b49a91ddf28f8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V65J4JK2%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIQDNPIINphNGwQmfKCZPQmWxp72ic6%2FiWFHft5OrrRj65AIgEZWExYyDhIEMeOJ5DRLt8h6UZJ4n3rfk4HATAlGuoyMq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDOwAsyIl%2Bz4Ay9gj4yrcA103T0T0KjTl%2FgWQtDOtBi%2BAA50efmBPMi4qaxUSAhXBuIDh1YZQpa6OHEqIcAdtclof01%2BYHfHjaEPdVHHj34VW%2BeTqiHY8hbNYR%2FUfB%2B3K5vsDJnp7xdxyY4U2KUzk4ApvuJDnV%2B04kqy%2FBEQau0MaUd6S67Aer%2FCmSxfVALufR61zIOR3XU4%2B74ZGlezwicFdI9q2kc4cHoe376qL49YqgGmfVO0pkfvwVtZDnPJ8DoHnVhw4EDpW4bNsds3htUJJ1FlMe8df68veoyZpqYlRLZrXqHm2Sbx2FFK3w28tnkBCPyhEB9GtHERHnHmKMdVrl2qpxKy7enxgLUv9970QHV4Gmk1Aki1xmw%2BTUj0HwsxjHozlH8bWtbCA6BdCfAYmdfBjf8e7I62NWG4b7kgvesCmh3RlAqAXamLW89fzNUxjb%2BjKNautq3BsRaupMMZnEv%2BdnwWPL30BmtpQ1J813w8obETRSUEN8FQ821jwWLYX3u2L2P5cd9TMP4qPt1%2BSDoRkJSExhtH84KDdiXZt1LAXDinCI5i8tWm7VGhfU%2FpxK%2B8jg4V6XmzU7HyYfeRngemHH2w1B64a1Bc%2FSi8BKLBGpyFXC4KVHzTlx0m69kVc1xDBjoYpw4mBMN3qj70GOqUB4vG5xHMjJaBfQF%2BiFvU%2FmSLZ17s0lknd1Db5Wy6UWPMMewNRf7vhbEycS6KaueLMqqKMuPFF4%2Faed4tGt5KJ%2FKqphqjqTNuF%2Bgjb6Co%2BSsXTiAfIR7026RHuNicE67EjzOOqcRYLEoy6prvm79onUyV6XMw6yZhv5tnTqOO2UcQcqN4E%2Fvi3hV2YbqQ9%2FuVaFy%2F5tgta%2Fbud8Yoh8xIcfzpFPCw7&X-Amz-Signature=3f23b3461a795546eac0a111bb0eb8b6f3bbbcc19bb65030f373a1bd44cdaf85&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ZGM2YEJ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJGMEQCIH2NgS6dpps4tI3NH9QYN49F%2BsLSCKYN1DE%2FPpPZQ%2BkdAiAeL4Dt4mODTQHTUur6t1kpOrIDzVfZiB7orU%2FMdWlufir%2FAwhREAAaDDYzNzQyMzE4MzgwNSIMGhuFQUyOEsSDXU37KtwDeq5dZBnRkXoCfC%2BU4N3E2j2BrpQ2Rqt2FzvbBJmcO3AqofRcSCVWzfhC%2B3psdO1CyM1V9OeutNxeqfxkDO%2FhThdbNXP%2FNeNB2IsM8TehXiz5j31WQN6Yn9fBrmkZ2liRE3hyqwhm7iNYI%2BuwdAhskDmCsqBqAsX6w4F5xwWV7DGg068GyL7XeM4gWAIyhu92%2BqC2O4DDfj9kI3OUTQ%2BqfTgqooFu21QyGWvGKpzChXwtdpUNQKo5L%2BKejCNKXk6uhzhy2C7rB%2F7bdUIPmgxXlTCxnqb3IWyFDBGjYmW0yIkdUImcVOMcnlYQPofAUJbbM%2F3itBeoQLfjTM7O3uOvQdGiqXFAYSBtCYEbq8CbfU1VUZP5ElfhypowpOZXwb1cFvhRJvkGwpqUJAnGKjnFBlAppO5KEhX7fd1Qr9blPppq%2FRMyUnRhiUqcKqUiyxCWM4efMkrLcgEqmjVLvchSTIKSY1RDRm%2FpsfZYHEqeKoUMnm7RJGm3En5Dk9tJdSwWIJDAZeIHLGUBFvuNB6HvnMauM9Ss2GCdkduUdox9iHr05J7Y%2FbG6kH5PlHseIk7dhyRZISY2yqNF%2B44U3rpyvoLc2WJdpcetLtp91p4ClPHXFhbz%2F4HyUM3NQWAwzOqPvQY6pgEFl4KtS5RIMpVwz8v%2FVf4vniYL%2FDWL3Tvj9P0QaMczoRGLED1jDAyuEvFeD3SL3GwynmgVQm0L%2FT5Mqxi8d5ag2sgVwIKvg%2F%2FH%2BCLLRr8cItmDmYZdUGfUfoevL%2FgGe%2F9lGd2y9PcHniABomS5FjUcBfUgGc%2Fn19BBztnswUg%2FlJJM2x20LOyAgNmGprCO2bmc5xwd5LMUH4m4MVmoifkC%2FRB5xu4g&X-Amz-Signature=b74adf94f339b9518e07b0b9b91feb28ed62f8bb60925814f4004dad20308d36&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ZGM2YEJ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJGMEQCIH2NgS6dpps4tI3NH9QYN49F%2BsLSCKYN1DE%2FPpPZQ%2BkdAiAeL4Dt4mODTQHTUur6t1kpOrIDzVfZiB7orU%2FMdWlufir%2FAwhREAAaDDYzNzQyMzE4MzgwNSIMGhuFQUyOEsSDXU37KtwDeq5dZBnRkXoCfC%2BU4N3E2j2BrpQ2Rqt2FzvbBJmcO3AqofRcSCVWzfhC%2B3psdO1CyM1V9OeutNxeqfxkDO%2FhThdbNXP%2FNeNB2IsM8TehXiz5j31WQN6Yn9fBrmkZ2liRE3hyqwhm7iNYI%2BuwdAhskDmCsqBqAsX6w4F5xwWV7DGg068GyL7XeM4gWAIyhu92%2BqC2O4DDfj9kI3OUTQ%2BqfTgqooFu21QyGWvGKpzChXwtdpUNQKo5L%2BKejCNKXk6uhzhy2C7rB%2F7bdUIPmgxXlTCxnqb3IWyFDBGjYmW0yIkdUImcVOMcnlYQPofAUJbbM%2F3itBeoQLfjTM7O3uOvQdGiqXFAYSBtCYEbq8CbfU1VUZP5ElfhypowpOZXwb1cFvhRJvkGwpqUJAnGKjnFBlAppO5KEhX7fd1Qr9blPppq%2FRMyUnRhiUqcKqUiyxCWM4efMkrLcgEqmjVLvchSTIKSY1RDRm%2FpsfZYHEqeKoUMnm7RJGm3En5Dk9tJdSwWIJDAZeIHLGUBFvuNB6HvnMauM9Ss2GCdkduUdox9iHr05J7Y%2FbG6kH5PlHseIk7dhyRZISY2yqNF%2B44U3rpyvoLc2WJdpcetLtp91p4ClPHXFhbz%2F4HyUM3NQWAwzOqPvQY6pgEFl4KtS5RIMpVwz8v%2FVf4vniYL%2FDWL3Tvj9P0QaMczoRGLED1jDAyuEvFeD3SL3GwynmgVQm0L%2FT5Mqxi8d5ag2sgVwIKvg%2F%2FH%2BCLLRr8cItmDmYZdUGfUfoevL%2FgGe%2F9lGd2y9PcHniABomS5FjUcBfUgGc%2Fn19BBztnswUg%2FlJJM2x20LOyAgNmGprCO2bmc5xwd5LMUH4m4MVmoifkC%2FRB5xu4g&X-Amz-Signature=c7b3d48e4f6681737c56a15183716488a00f2aea19e7795ba0ff30546d315431&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ZGM2YEJ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJGMEQCIH2NgS6dpps4tI3NH9QYN49F%2BsLSCKYN1DE%2FPpPZQ%2BkdAiAeL4Dt4mODTQHTUur6t1kpOrIDzVfZiB7orU%2FMdWlufir%2FAwhREAAaDDYzNzQyMzE4MzgwNSIMGhuFQUyOEsSDXU37KtwDeq5dZBnRkXoCfC%2BU4N3E2j2BrpQ2Rqt2FzvbBJmcO3AqofRcSCVWzfhC%2B3psdO1CyM1V9OeutNxeqfxkDO%2FhThdbNXP%2FNeNB2IsM8TehXiz5j31WQN6Yn9fBrmkZ2liRE3hyqwhm7iNYI%2BuwdAhskDmCsqBqAsX6w4F5xwWV7DGg068GyL7XeM4gWAIyhu92%2BqC2O4DDfj9kI3OUTQ%2BqfTgqooFu21QyGWvGKpzChXwtdpUNQKo5L%2BKejCNKXk6uhzhy2C7rB%2F7bdUIPmgxXlTCxnqb3IWyFDBGjYmW0yIkdUImcVOMcnlYQPofAUJbbM%2F3itBeoQLfjTM7O3uOvQdGiqXFAYSBtCYEbq8CbfU1VUZP5ElfhypowpOZXwb1cFvhRJvkGwpqUJAnGKjnFBlAppO5KEhX7fd1Qr9blPppq%2FRMyUnRhiUqcKqUiyxCWM4efMkrLcgEqmjVLvchSTIKSY1RDRm%2FpsfZYHEqeKoUMnm7RJGm3En5Dk9tJdSwWIJDAZeIHLGUBFvuNB6HvnMauM9Ss2GCdkduUdox9iHr05J7Y%2FbG6kH5PlHseIk7dhyRZISY2yqNF%2B44U3rpyvoLc2WJdpcetLtp91p4ClPHXFhbz%2F4HyUM3NQWAwzOqPvQY6pgEFl4KtS5RIMpVwz8v%2FVf4vniYL%2FDWL3Tvj9P0QaMczoRGLED1jDAyuEvFeD3SL3GwynmgVQm0L%2FT5Mqxi8d5ag2sgVwIKvg%2F%2FH%2BCLLRr8cItmDmYZdUGfUfoevL%2FgGe%2F9lGd2y9PcHniABomS5FjUcBfUgGc%2Fn19BBztnswUg%2FlJJM2x20LOyAgNmGprCO2bmc5xwd5LMUH4m4MVmoifkC%2FRB5xu4g&X-Amz-Signature=bd783261c0e52f3a001bd999feb278a35f2fa214b275bbd6e7f723617aa33771&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ZGM2YEJ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJGMEQCIH2NgS6dpps4tI3NH9QYN49F%2BsLSCKYN1DE%2FPpPZQ%2BkdAiAeL4Dt4mODTQHTUur6t1kpOrIDzVfZiB7orU%2FMdWlufir%2FAwhREAAaDDYzNzQyMzE4MzgwNSIMGhuFQUyOEsSDXU37KtwDeq5dZBnRkXoCfC%2BU4N3E2j2BrpQ2Rqt2FzvbBJmcO3AqofRcSCVWzfhC%2B3psdO1CyM1V9OeutNxeqfxkDO%2FhThdbNXP%2FNeNB2IsM8TehXiz5j31WQN6Yn9fBrmkZ2liRE3hyqwhm7iNYI%2BuwdAhskDmCsqBqAsX6w4F5xwWV7DGg068GyL7XeM4gWAIyhu92%2BqC2O4DDfj9kI3OUTQ%2BqfTgqooFu21QyGWvGKpzChXwtdpUNQKo5L%2BKejCNKXk6uhzhy2C7rB%2F7bdUIPmgxXlTCxnqb3IWyFDBGjYmW0yIkdUImcVOMcnlYQPofAUJbbM%2F3itBeoQLfjTM7O3uOvQdGiqXFAYSBtCYEbq8CbfU1VUZP5ElfhypowpOZXwb1cFvhRJvkGwpqUJAnGKjnFBlAppO5KEhX7fd1Qr9blPppq%2FRMyUnRhiUqcKqUiyxCWM4efMkrLcgEqmjVLvchSTIKSY1RDRm%2FpsfZYHEqeKoUMnm7RJGm3En5Dk9tJdSwWIJDAZeIHLGUBFvuNB6HvnMauM9Ss2GCdkduUdox9iHr05J7Y%2FbG6kH5PlHseIk7dhyRZISY2yqNF%2B44U3rpyvoLc2WJdpcetLtp91p4ClPHXFhbz%2F4HyUM3NQWAwzOqPvQY6pgEFl4KtS5RIMpVwz8v%2FVf4vniYL%2FDWL3Tvj9P0QaMczoRGLED1jDAyuEvFeD3SL3GwynmgVQm0L%2FT5Mqxi8d5ag2sgVwIKvg%2F%2FH%2BCLLRr8cItmDmYZdUGfUfoevL%2FgGe%2F9lGd2y9PcHniABomS5FjUcBfUgGc%2Fn19BBztnswUg%2FlJJM2x20LOyAgNmGprCO2bmc5xwd5LMUH4m4MVmoifkC%2FRB5xu4g&X-Amz-Signature=795bf671f3dc5fb5b121cb25267b41c7b83ed012df3fa8df49781e38785f1208&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
