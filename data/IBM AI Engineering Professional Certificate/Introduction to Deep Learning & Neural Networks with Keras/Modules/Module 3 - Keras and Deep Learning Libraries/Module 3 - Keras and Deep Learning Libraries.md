

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YNCKVHCI%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCIQD8inLpl1kfWQMnex7Pww9N7DWQs7BzKRY3I21wsCdFzQIgOSgSnWrc1VIJFT1J%2F4Sv%2Bl1oczcidX4X8mjhsxWVp4oq%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDLjO%2BXwpPyIKLhMqzyrcA6Ug8%2BBugl2hd4r4YzV7b8D1Kd6ZbsbKyNoc4ryfDDMDuTrUtfuYmhjlxpt2apCIjYX5YuqyzEQVUxQj4k0hnvEx6S1lu2I%2FfRut2ZX18ACYLhi4bnlpNZKI%2FdjTnf6d3UpkkfaigIBkrL6uoKLhgNh9J1ZjlGutLpITPoDdRsaBe1wkJnTm241iN9RA6onfjUtZ%2BBKlm5wb1OzLJpjHD%2FqJOJeLKukECLczg%2Fu7%2FTkrAUC05gSnUgoN4Zy0NJVMWB0NRlbhbu7PaA9W5wTecjOnICx4fuTjnzEGE45lSrxOAe8KcUp0KvgZledoXsClt%2BWDrFi4%2BfVU84LFPucTFY0jIL8anhNkk3ncKztcSyeSwtCNEI1aztjkNVzmJTMppDq9BQMbRpn7X43%2F7xKYXipSdj4kM%2Fd8%2ByhSduDWRMuO1SdKSFDrDo7S3U8ekTb%2FGevDl4WuFtjTLuIGWh4XmhIedKONFgzFkY35Fyu2HaFs6aul4ZG8BGm9omqk9%2Fikarj5KdJrdj0ZmAXwZn507yTb4WsplRxttSkbvs%2BYWzxhIP5WFKPBQqCwXJcTo6meHj4TUUyc31GANVg%2BnGRtYAHNPIl%2FSZD%2BFjxsDuokCBLS%2BuCAqGkN%2BKcTuz4CMLvvjL0GOqUB9BDgOZXw22NdM0PUHf%2Fk34ATHDISWtS4NBc2AnFXyjTCNJWq4tZmK2DnYJdp5y8JNVY%2BmmoUisVLM6l0Q4cxMCkHTuV59X%2BM7jtrR8vH8KZ3FomyD1louvaIx1zRAMFokcqPZcUWxAqQgdbrEr2ckspXobDjI9pUX9MpJSksx76bfsY64AFCxj8%2Fe4RQ4PC5q6OPEruHifpa3Q5X1cNTK9Sfa8bE&X-Amz-Signature=9727c5e42b46e8f3d9394838fde5519674ee28b826c2a048f875ee31229fd755&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YNCKVHCI%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCIQD8inLpl1kfWQMnex7Pww9N7DWQs7BzKRY3I21wsCdFzQIgOSgSnWrc1VIJFT1J%2F4Sv%2Bl1oczcidX4X8mjhsxWVp4oq%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDLjO%2BXwpPyIKLhMqzyrcA6Ug8%2BBugl2hd4r4YzV7b8D1Kd6ZbsbKyNoc4ryfDDMDuTrUtfuYmhjlxpt2apCIjYX5YuqyzEQVUxQj4k0hnvEx6S1lu2I%2FfRut2ZX18ACYLhi4bnlpNZKI%2FdjTnf6d3UpkkfaigIBkrL6uoKLhgNh9J1ZjlGutLpITPoDdRsaBe1wkJnTm241iN9RA6onfjUtZ%2BBKlm5wb1OzLJpjHD%2FqJOJeLKukECLczg%2Fu7%2FTkrAUC05gSnUgoN4Zy0NJVMWB0NRlbhbu7PaA9W5wTecjOnICx4fuTjnzEGE45lSrxOAe8KcUp0KvgZledoXsClt%2BWDrFi4%2BfVU84LFPucTFY0jIL8anhNkk3ncKztcSyeSwtCNEI1aztjkNVzmJTMppDq9BQMbRpn7X43%2F7xKYXipSdj4kM%2Fd8%2ByhSduDWRMuO1SdKSFDrDo7S3U8ekTb%2FGevDl4WuFtjTLuIGWh4XmhIedKONFgzFkY35Fyu2HaFs6aul4ZG8BGm9omqk9%2Fikarj5KdJrdj0ZmAXwZn507yTb4WsplRxttSkbvs%2BYWzxhIP5WFKPBQqCwXJcTo6meHj4TUUyc31GANVg%2BnGRtYAHNPIl%2FSZD%2BFjxsDuokCBLS%2BuCAqGkN%2BKcTuz4CMLvvjL0GOqUB9BDgOZXw22NdM0PUHf%2Fk34ATHDISWtS4NBc2AnFXyjTCNJWq4tZmK2DnYJdp5y8JNVY%2BmmoUisVLM6l0Q4cxMCkHTuV59X%2BM7jtrR8vH8KZ3FomyD1louvaIx1zRAMFokcqPZcUWxAqQgdbrEr2ckspXobDjI9pUX9MpJSksx76bfsY64AFCxj8%2Fe4RQ4PC5q6OPEruHifpa3Q5X1cNTK9Sfa8bE&X-Amz-Signature=c2c2a7ff9cde2fc6f63e0d35317212160a2b12df9a70ffacacef6e23c09cf7ac&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YNCKVHCI%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCIQD8inLpl1kfWQMnex7Pww9N7DWQs7BzKRY3I21wsCdFzQIgOSgSnWrc1VIJFT1J%2F4Sv%2Bl1oczcidX4X8mjhsxWVp4oq%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDLjO%2BXwpPyIKLhMqzyrcA6Ug8%2BBugl2hd4r4YzV7b8D1Kd6ZbsbKyNoc4ryfDDMDuTrUtfuYmhjlxpt2apCIjYX5YuqyzEQVUxQj4k0hnvEx6S1lu2I%2FfRut2ZX18ACYLhi4bnlpNZKI%2FdjTnf6d3UpkkfaigIBkrL6uoKLhgNh9J1ZjlGutLpITPoDdRsaBe1wkJnTm241iN9RA6onfjUtZ%2BBKlm5wb1OzLJpjHD%2FqJOJeLKukECLczg%2Fu7%2FTkrAUC05gSnUgoN4Zy0NJVMWB0NRlbhbu7PaA9W5wTecjOnICx4fuTjnzEGE45lSrxOAe8KcUp0KvgZledoXsClt%2BWDrFi4%2BfVU84LFPucTFY0jIL8anhNkk3ncKztcSyeSwtCNEI1aztjkNVzmJTMppDq9BQMbRpn7X43%2F7xKYXipSdj4kM%2Fd8%2ByhSduDWRMuO1SdKSFDrDo7S3U8ekTb%2FGevDl4WuFtjTLuIGWh4XmhIedKONFgzFkY35Fyu2HaFs6aul4ZG8BGm9omqk9%2Fikarj5KdJrdj0ZmAXwZn507yTb4WsplRxttSkbvs%2BYWzxhIP5WFKPBQqCwXJcTo6meHj4TUUyc31GANVg%2BnGRtYAHNPIl%2FSZD%2BFjxsDuokCBLS%2BuCAqGkN%2BKcTuz4CMLvvjL0GOqUB9BDgOZXw22NdM0PUHf%2Fk34ATHDISWtS4NBc2AnFXyjTCNJWq4tZmK2DnYJdp5y8JNVY%2BmmoUisVLM6l0Q4cxMCkHTuV59X%2BM7jtrR8vH8KZ3FomyD1louvaIx1zRAMFokcqPZcUWxAqQgdbrEr2ckspXobDjI9pUX9MpJSksx76bfsY64AFCxj8%2Fe4RQ4PC5q6OPEruHifpa3Q5X1cNTK9Sfa8bE&X-Amz-Signature=e0bd4dd9a6904d67a39d9e44786c255cfa93b780ec5fe4ee7b609c4c0c3d4a4e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y5UTUJD2%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCIBDNvS3Ckmac0pBEVHa1pMn6%2F8hjLSEvIHCaDTM2Q4%2FuAiEAoFw%2BG5S8%2BoOi23Ts3yRIkgb3tgRQXl6zuJtFMos2PoIq%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDNgHIQJYk2D4l2s7TSrcA4L00fOCn3k1yXT%2Fz0p1B4a%2FEFbXpS9x0rzkTBabvKHrHjQtwFK5TiHGxZ5EzZPDEpsIIzTcjwYJNcV%2FxLFaPznS5lCFRT9dnugOfZD68Dvbwpq3OOeaRrT1ja0GS1ntWb%2FaqklvxwbxnmSc%2BtJ341E7nd8r4SCsnVW%2FJ4b27zMcSMm0piMAfMUnlNDI5lae%2Bd8rJzlZvX%2BuJGaQDN9aJUlBg1EpfTFtkDdA6IPcS8q702hXCkzE35uCDtxxeFUWWPFyt9AaQaG9E066h92M7r0f0xBsbP2SyN6FHrFMJNL9HuKi9C%2FQMxtzqc63hVWXPA0y7jYdFmnyAfGUS%2BomHGjG8HukootLPEU0l%2Bi0Y2T5YTFVlbfBUf%2BsZuWvpgHgkAlTC5Ejs9ppAbxYyC7EQHuljw4F0ayHip5cm2Yo3AHK5l%2BmBmY%2Bup8pXlaLlvj3N4w9RC7Byz%2B7sSq9WAw7Ey%2BQyX2ZpPc%2FiZ4jAWFlU%2B3tkfidp5Q1dqLNLuryFRhA%2F6Cdoez8hRNGdBo9%2FKiTe2MSc3YY17KozmArHAI%2BXI0WlTpJ064kQKW%2BEgcd3UMBtl4U%2FBOviHF4f%2BzUkP28%2BWsHOhNHTG76Wr57rs9817pE3%2FTxPGm158S3X57qMNXvjL0GOqUBw1CK4%2BE46I0ELB88CITK0UNz8nhTQfvDrrqFDT5L%2FalF5JhlLj6zmK4ts%2By5HDZv0OM7Y6wRciec5AAgWTgAcfUGk7E8l2ErqRFiPYyCefLrB5%2FSIbzZ3Ev%2BilS1KPiNWfWfxxdcja7GKUyx8k8YX8np9hKTyyAZKDGt6WbqwKkIFAgO6%2FJoqtQXDRc7Pyp4D1f1LHUePwBNFYfTY94upd3TooKe&X-Amz-Signature=00d1a97e2223c1ab754c72f92df8fad96303792a34e3be0f58477915a5102dca&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UKTXPYDX%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJIMEYCIQCcOmhrBoYUK358%2BzBZVLkhoHXOMZ1dyWx2Cbhj6icYZgIhAN7HML6m%2Bof%2BFw1%2FpiUWVJiwMsXbWWaLdtUEk8abTSNIKv8DCEMQABoMNjM3NDIzMTgzODA1Igy4En8sOZaMPhJPHk0q3AMiCgcTbM61uOz%2BAktSdzrfo42QdvxMasBEryxshxP2ezFCrLIRp0y31KJVrT2tFuTBzsc9Q7z%2BGBL7dsybcXGFw3wWZgE%2BiXMouX7eeMos44yJaunLrCgiuJQpVTQNx4KZCqDtk9bvuEW0o5T6t%2FQs7TRiIFY8mLF6qBySwHU6c524u93MtBuLXzTXtUcs6bQzFsOLE6kgIA2IbvkvsAB1XT%2BYr%2FcUlmtOYQddq6fHnl9uuJbAORhOgUct6UPISUL1GRze%2FPNvdHB%2BVfyEb1y9RhZoJjwTeuaykXB49KW4ulY2EOkNTwq4pSDwewU%2Bs9o2TS%2BssT3pzHstEld055w3PsFij6srHJ5HDg1fpAWyNokvCduQLhjupDmwx2PDswBnY9rOlvw1iKjZK%2BG5vIoyMWSg2epl0UBHqBS1QN2Ltm%2F09w3hWenzLvE6emDk61tPoLBdtPtj6EWYXzadQoRUrdAtI1lGbZ61gPDRXE7CtTUxtweSGgdMB85AJ8D4RZE82ePXctyL7Mh9Z%2BGJ0059IuZzILqFFr3ie%2BhhYMBJehMynszGnsAN5DoDwZdbHTz2mCkDCRCwfDtB5aUkZJPMty0eDgw2ZG%2BgMev%2BHD6Xgp7mhM1X6mfOJHPVgDCX74y9BjqkAS0%2Fph8NXAse8kxnNgzIQBu5W7WSF0E6T6%2F5hxZGihUE5KV0Te4%2FsQARCECRZWCFoySDW%2FNzrRLX8hwBP4AVVDAaJGUTYbjzrIcfeWIO%2F88IT4KfQbLmqpJlCfBy%2BIdMc%2BZ3Siyw4b4CTwOWUZmeVvA81AG%2FVn488NotQt8Q%2BDy3pt8mCEArYhlYyDEqfSvSltrsdkrZSuitvjuLyVCtRgeEWwKg&X-Amz-Signature=b9c50dd30cf0028de4534e423242c46676f3838674dc10cfcf224623089f6ad5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YNCKVHCI%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCIQD8inLpl1kfWQMnex7Pww9N7DWQs7BzKRY3I21wsCdFzQIgOSgSnWrc1VIJFT1J%2F4Sv%2Bl1oczcidX4X8mjhsxWVp4oq%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDLjO%2BXwpPyIKLhMqzyrcA6Ug8%2BBugl2hd4r4YzV7b8D1Kd6ZbsbKyNoc4ryfDDMDuTrUtfuYmhjlxpt2apCIjYX5YuqyzEQVUxQj4k0hnvEx6S1lu2I%2FfRut2ZX18ACYLhi4bnlpNZKI%2FdjTnf6d3UpkkfaigIBkrL6uoKLhgNh9J1ZjlGutLpITPoDdRsaBe1wkJnTm241iN9RA6onfjUtZ%2BBKlm5wb1OzLJpjHD%2FqJOJeLKukECLczg%2Fu7%2FTkrAUC05gSnUgoN4Zy0NJVMWB0NRlbhbu7PaA9W5wTecjOnICx4fuTjnzEGE45lSrxOAe8KcUp0KvgZledoXsClt%2BWDrFi4%2BfVU84LFPucTFY0jIL8anhNkk3ncKztcSyeSwtCNEI1aztjkNVzmJTMppDq9BQMbRpn7X43%2F7xKYXipSdj4kM%2Fd8%2ByhSduDWRMuO1SdKSFDrDo7S3U8ekTb%2FGevDl4WuFtjTLuIGWh4XmhIedKONFgzFkY35Fyu2HaFs6aul4ZG8BGm9omqk9%2Fikarj5KdJrdj0ZmAXwZn507yTb4WsplRxttSkbvs%2BYWzxhIP5WFKPBQqCwXJcTo6meHj4TUUyc31GANVg%2BnGRtYAHNPIl%2FSZD%2BFjxsDuokCBLS%2BuCAqGkN%2BKcTuz4CMLvvjL0GOqUB9BDgOZXw22NdM0PUHf%2Fk34ATHDISWtS4NBc2AnFXyjTCNJWq4tZmK2DnYJdp5y8JNVY%2BmmoUisVLM6l0Q4cxMCkHTuV59X%2BM7jtrR8vH8KZ3FomyD1louvaIx1zRAMFokcqPZcUWxAqQgdbrEr2ckspXobDjI9pUX9MpJSksx76bfsY64AFCxj8%2Fe4RQ4PC5q6OPEruHifpa3Q5X1cNTK9Sfa8bE&X-Amz-Signature=3493a7b024d1f68eab79f55a58387d31a99eda3d7cb35c5bd80432b798e7d834&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YNCKVHCI%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCIQD8inLpl1kfWQMnex7Pww9N7DWQs7BzKRY3I21wsCdFzQIgOSgSnWrc1VIJFT1J%2F4Sv%2Bl1oczcidX4X8mjhsxWVp4oq%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDLjO%2BXwpPyIKLhMqzyrcA6Ug8%2BBugl2hd4r4YzV7b8D1Kd6ZbsbKyNoc4ryfDDMDuTrUtfuYmhjlxpt2apCIjYX5YuqyzEQVUxQj4k0hnvEx6S1lu2I%2FfRut2ZX18ACYLhi4bnlpNZKI%2FdjTnf6d3UpkkfaigIBkrL6uoKLhgNh9J1ZjlGutLpITPoDdRsaBe1wkJnTm241iN9RA6onfjUtZ%2BBKlm5wb1OzLJpjHD%2FqJOJeLKukECLczg%2Fu7%2FTkrAUC05gSnUgoN4Zy0NJVMWB0NRlbhbu7PaA9W5wTecjOnICx4fuTjnzEGE45lSrxOAe8KcUp0KvgZledoXsClt%2BWDrFi4%2BfVU84LFPucTFY0jIL8anhNkk3ncKztcSyeSwtCNEI1aztjkNVzmJTMppDq9BQMbRpn7X43%2F7xKYXipSdj4kM%2Fd8%2ByhSduDWRMuO1SdKSFDrDo7S3U8ekTb%2FGevDl4WuFtjTLuIGWh4XmhIedKONFgzFkY35Fyu2HaFs6aul4ZG8BGm9omqk9%2Fikarj5KdJrdj0ZmAXwZn507yTb4WsplRxttSkbvs%2BYWzxhIP5WFKPBQqCwXJcTo6meHj4TUUyc31GANVg%2BnGRtYAHNPIl%2FSZD%2BFjxsDuokCBLS%2BuCAqGkN%2BKcTuz4CMLvvjL0GOqUB9BDgOZXw22NdM0PUHf%2Fk34ATHDISWtS4NBc2AnFXyjTCNJWq4tZmK2DnYJdp5y8JNVY%2BmmoUisVLM6l0Q4cxMCkHTuV59X%2BM7jtrR8vH8KZ3FomyD1louvaIx1zRAMFokcqPZcUWxAqQgdbrEr2ckspXobDjI9pUX9MpJSksx76bfsY64AFCxj8%2Fe4RQ4PC5q6OPEruHifpa3Q5X1cNTK9Sfa8bE&X-Amz-Signature=061dd203bbfed2d8102b64f77dbeaf53aa84ad1524dc0e4ac949084b949c680e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YNCKVHCI%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCIQD8inLpl1kfWQMnex7Pww9N7DWQs7BzKRY3I21wsCdFzQIgOSgSnWrc1VIJFT1J%2F4Sv%2Bl1oczcidX4X8mjhsxWVp4oq%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDLjO%2BXwpPyIKLhMqzyrcA6Ug8%2BBugl2hd4r4YzV7b8D1Kd6ZbsbKyNoc4ryfDDMDuTrUtfuYmhjlxpt2apCIjYX5YuqyzEQVUxQj4k0hnvEx6S1lu2I%2FfRut2ZX18ACYLhi4bnlpNZKI%2FdjTnf6d3UpkkfaigIBkrL6uoKLhgNh9J1ZjlGutLpITPoDdRsaBe1wkJnTm241iN9RA6onfjUtZ%2BBKlm5wb1OzLJpjHD%2FqJOJeLKukECLczg%2Fu7%2FTkrAUC05gSnUgoN4Zy0NJVMWB0NRlbhbu7PaA9W5wTecjOnICx4fuTjnzEGE45lSrxOAe8KcUp0KvgZledoXsClt%2BWDrFi4%2BfVU84LFPucTFY0jIL8anhNkk3ncKztcSyeSwtCNEI1aztjkNVzmJTMppDq9BQMbRpn7X43%2F7xKYXipSdj4kM%2Fd8%2ByhSduDWRMuO1SdKSFDrDo7S3U8ekTb%2FGevDl4WuFtjTLuIGWh4XmhIedKONFgzFkY35Fyu2HaFs6aul4ZG8BGm9omqk9%2Fikarj5KdJrdj0ZmAXwZn507yTb4WsplRxttSkbvs%2BYWzxhIP5WFKPBQqCwXJcTo6meHj4TUUyc31GANVg%2BnGRtYAHNPIl%2FSZD%2BFjxsDuokCBLS%2BuCAqGkN%2BKcTuz4CMLvvjL0GOqUB9BDgOZXw22NdM0PUHf%2Fk34ATHDISWtS4NBc2AnFXyjTCNJWq4tZmK2DnYJdp5y8JNVY%2BmmoUisVLM6l0Q4cxMCkHTuV59X%2BM7jtrR8vH8KZ3FomyD1louvaIx1zRAMFokcqPZcUWxAqQgdbrEr2ckspXobDjI9pUX9MpJSksx76bfsY64AFCxj8%2Fe4RQ4PC5q6OPEruHifpa3Q5X1cNTK9Sfa8bE&X-Amz-Signature=4f30afe722bb1ff87ac239363daa2a2a7825e53ee0415888114f1ada5eb2b094&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YNCKVHCI%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCIQD8inLpl1kfWQMnex7Pww9N7DWQs7BzKRY3I21wsCdFzQIgOSgSnWrc1VIJFT1J%2F4Sv%2Bl1oczcidX4X8mjhsxWVp4oq%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDLjO%2BXwpPyIKLhMqzyrcA6Ug8%2BBugl2hd4r4YzV7b8D1Kd6ZbsbKyNoc4ryfDDMDuTrUtfuYmhjlxpt2apCIjYX5YuqyzEQVUxQj4k0hnvEx6S1lu2I%2FfRut2ZX18ACYLhi4bnlpNZKI%2FdjTnf6d3UpkkfaigIBkrL6uoKLhgNh9J1ZjlGutLpITPoDdRsaBe1wkJnTm241iN9RA6onfjUtZ%2BBKlm5wb1OzLJpjHD%2FqJOJeLKukECLczg%2Fu7%2FTkrAUC05gSnUgoN4Zy0NJVMWB0NRlbhbu7PaA9W5wTecjOnICx4fuTjnzEGE45lSrxOAe8KcUp0KvgZledoXsClt%2BWDrFi4%2BfVU84LFPucTFY0jIL8anhNkk3ncKztcSyeSwtCNEI1aztjkNVzmJTMppDq9BQMbRpn7X43%2F7xKYXipSdj4kM%2Fd8%2ByhSduDWRMuO1SdKSFDrDo7S3U8ekTb%2FGevDl4WuFtjTLuIGWh4XmhIedKONFgzFkY35Fyu2HaFs6aul4ZG8BGm9omqk9%2Fikarj5KdJrdj0ZmAXwZn507yTb4WsplRxttSkbvs%2BYWzxhIP5WFKPBQqCwXJcTo6meHj4TUUyc31GANVg%2BnGRtYAHNPIl%2FSZD%2BFjxsDuokCBLS%2BuCAqGkN%2BKcTuz4CMLvvjL0GOqUB9BDgOZXw22NdM0PUHf%2Fk34ATHDISWtS4NBc2AnFXyjTCNJWq4tZmK2DnYJdp5y8JNVY%2BmmoUisVLM6l0Q4cxMCkHTuV59X%2BM7jtrR8vH8KZ3FomyD1louvaIx1zRAMFokcqPZcUWxAqQgdbrEr2ckspXobDjI9pUX9MpJSksx76bfsY64AFCxj8%2Fe4RQ4PC5q6OPEruHifpa3Q5X1cNTK9Sfa8bE&X-Amz-Signature=9630423ddb31e69cb6472509c04a7914e5f9051b97bc820e0357931c0ebd3270&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
