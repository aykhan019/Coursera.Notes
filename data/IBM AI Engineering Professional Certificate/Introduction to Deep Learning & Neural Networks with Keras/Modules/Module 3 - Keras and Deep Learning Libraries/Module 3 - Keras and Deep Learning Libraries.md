

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46626PKALEQ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQCz0Cb52GDh7VWjPkroYAjjjnUKJpyfStIeKf5ql2nXjAIgYnN2ykMp4ro1BUVwOsk3%2FU7Osi4Q5GG%2BhTm0%2BaBbkSYq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDI9%2Fb9H9n7IPhGxqXircA8B1BjG5TL0X6mBbWFf38s3LVAIeqBjppDqtaa9eqSqZHdsHDGp8FFp8zKwTmbB0PKc0vCRiUXDEGesjBHt6P4xt6WYWYkInPh3WpyAUNdOZmaEOcmkqm3VSiicEi6IQ3UGB14JnV2uKObmBCa4%2Bpmr3H27b28OssD2PbhAvS45Y4cMopd0ZQZkYMdvBjSlYWSgSKFO1PezuzOSCySkqfQSc8sTj2MyPcYRrf6RD6EgfxLSfBn3eSvzqfEqeLFFjTj7eZgoywMait9pkTuAuzXRV3J7K8QxBnBNxTjErVapKPAqbBZTDILyRV4FwrYBzz6K0Pqiva55%2B6lIHW7q%2BUHkstfgH76gpqZeR1tLOeD9MLrI5mV5bABXQAp%2FW7N5KvEHWzNlNQA6Bz8b5g%2BQaD7QAH%2B1kDFBD4naUiYnFHLrCaDe9E7Qrn%2F15eF%2FDjby%2FpeluOpQMLs06j7sXZUYtAIZe9vzCvbj%2FbyNEfYqsuJNYEnPkl%2BM88PUQOgNtoAyJ%2BJ%2FUUXFbLMqwxK4Teixs6befZpZ6YxBFgEwqGMu1%2FrzInrMSuWpKm1LzxtTw7ttyJj43gZy5qTTBvYIpozKokDsY%2BInaqt6xIoQh0fs%2BJY54LxrahwRVTQiVNTBUMIm8jr0GOqUBgyTdHF9Mc2cQy6IS7px28IQTumZu1pVSPpulrrRnbl43eD7%2BFQH3y2sZ4PxTjY9pvg4SBEEQ%2FdrOG4thnHAjW7knOrgffJKN86LJaK52ehHOTZOpTa5Vkj%2BAT9%2B0r%2FYS1g%2F7zrGjWXdMfGv9ZmKMzOhlM4KpyZp1R%2B0gVRJ5Jh2GAO%2FnmY3u3BcbrBuBxBhs4Yn9yo1UGR2ttmVUWhtyIHfqPW2H&X-Amz-Signature=381f6de63d8ea5e50e16b3c6d24f1aa93b78166ce5f2912a2d8cf1f0eea6b092&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46626PKALEQ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQCz0Cb52GDh7VWjPkroYAjjjnUKJpyfStIeKf5ql2nXjAIgYnN2ykMp4ro1BUVwOsk3%2FU7Osi4Q5GG%2BhTm0%2BaBbkSYq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDI9%2Fb9H9n7IPhGxqXircA8B1BjG5TL0X6mBbWFf38s3LVAIeqBjppDqtaa9eqSqZHdsHDGp8FFp8zKwTmbB0PKc0vCRiUXDEGesjBHt6P4xt6WYWYkInPh3WpyAUNdOZmaEOcmkqm3VSiicEi6IQ3UGB14JnV2uKObmBCa4%2Bpmr3H27b28OssD2PbhAvS45Y4cMopd0ZQZkYMdvBjSlYWSgSKFO1PezuzOSCySkqfQSc8sTj2MyPcYRrf6RD6EgfxLSfBn3eSvzqfEqeLFFjTj7eZgoywMait9pkTuAuzXRV3J7K8QxBnBNxTjErVapKPAqbBZTDILyRV4FwrYBzz6K0Pqiva55%2B6lIHW7q%2BUHkstfgH76gpqZeR1tLOeD9MLrI5mV5bABXQAp%2FW7N5KvEHWzNlNQA6Bz8b5g%2BQaD7QAH%2B1kDFBD4naUiYnFHLrCaDe9E7Qrn%2F15eF%2FDjby%2FpeluOpQMLs06j7sXZUYtAIZe9vzCvbj%2FbyNEfYqsuJNYEnPkl%2BM88PUQOgNtoAyJ%2BJ%2FUUXFbLMqwxK4Teixs6befZpZ6YxBFgEwqGMu1%2FrzInrMSuWpKm1LzxtTw7ttyJj43gZy5qTTBvYIpozKokDsY%2BInaqt6xIoQh0fs%2BJY54LxrahwRVTQiVNTBUMIm8jr0GOqUBgyTdHF9Mc2cQy6IS7px28IQTumZu1pVSPpulrrRnbl43eD7%2BFQH3y2sZ4PxTjY9pvg4SBEEQ%2FdrOG4thnHAjW7knOrgffJKN86LJaK52ehHOTZOpTa5Vkj%2BAT9%2B0r%2FYS1g%2F7zrGjWXdMfGv9ZmKMzOhlM4KpyZp1R%2B0gVRJ5Jh2GAO%2FnmY3u3BcbrBuBxBhs4Yn9yo1UGR2ttmVUWhtyIHfqPW2H&X-Amz-Signature=f80c538f57717a33b7f356a158a8d64f2814ccc3698a0a75fe96555ae057680b&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46626PKALEQ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQCz0Cb52GDh7VWjPkroYAjjjnUKJpyfStIeKf5ql2nXjAIgYnN2ykMp4ro1BUVwOsk3%2FU7Osi4Q5GG%2BhTm0%2BaBbkSYq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDI9%2Fb9H9n7IPhGxqXircA8B1BjG5TL0X6mBbWFf38s3LVAIeqBjppDqtaa9eqSqZHdsHDGp8FFp8zKwTmbB0PKc0vCRiUXDEGesjBHt6P4xt6WYWYkInPh3WpyAUNdOZmaEOcmkqm3VSiicEi6IQ3UGB14JnV2uKObmBCa4%2Bpmr3H27b28OssD2PbhAvS45Y4cMopd0ZQZkYMdvBjSlYWSgSKFO1PezuzOSCySkqfQSc8sTj2MyPcYRrf6RD6EgfxLSfBn3eSvzqfEqeLFFjTj7eZgoywMait9pkTuAuzXRV3J7K8QxBnBNxTjErVapKPAqbBZTDILyRV4FwrYBzz6K0Pqiva55%2B6lIHW7q%2BUHkstfgH76gpqZeR1tLOeD9MLrI5mV5bABXQAp%2FW7N5KvEHWzNlNQA6Bz8b5g%2BQaD7QAH%2B1kDFBD4naUiYnFHLrCaDe9E7Qrn%2F15eF%2FDjby%2FpeluOpQMLs06j7sXZUYtAIZe9vzCvbj%2FbyNEfYqsuJNYEnPkl%2BM88PUQOgNtoAyJ%2BJ%2FUUXFbLMqwxK4Teixs6befZpZ6YxBFgEwqGMu1%2FrzInrMSuWpKm1LzxtTw7ttyJj43gZy5qTTBvYIpozKokDsY%2BInaqt6xIoQh0fs%2BJY54LxrahwRVTQiVNTBUMIm8jr0GOqUBgyTdHF9Mc2cQy6IS7px28IQTumZu1pVSPpulrrRnbl43eD7%2BFQH3y2sZ4PxTjY9pvg4SBEEQ%2FdrOG4thnHAjW7knOrgffJKN86LJaK52ehHOTZOpTa5Vkj%2BAT9%2B0r%2FYS1g%2F7zrGjWXdMfGv9ZmKMzOhlM4KpyZp1R%2B0gVRJ5Jh2GAO%2FnmY3u3BcbrBuBxBhs4Yn9yo1UGR2ttmVUWhtyIHfqPW2H&X-Amz-Signature=5b88dcbca773d7f556c444bbbe12ad8826b3c63295e10eafa07e14c53e9fecb0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663BIRSSD3%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJHMEUCIQCr0ssHrJGvCPQXqy3SssWHfPScGxeHN%2Bo2BUrt%2Bey%2FkAIgL0rVN4nyXSYLIzi9h77o%2BslEEE68%2F7YtxWgLTPFR81Aq%2FwMIUBAAGgw2Mzc0MjMxODM4MDUiDEk%2B2zV8n3%2FP9CyDryrcA62oXfura7RLECRpA0IKIfI8HaeQC5XawvTfsy09d09LmGXEz2rajcEx3Eca0FZPYfFVAvnWgWv76XEiTA4CSDJhU72A5XPEQTBbBzeoaqzTD%2BfW%2FAEvIRz2sSBqyZEJ7zK%2Bh0Hcm5sSG9A2VErFItHefs9Xw26a%2B9xiFhMgoRkYz0l6yDk2YPMs0NjDkzm%2B3%2FuJH9Npr%2F5o7R%2BwaMgaOXhqDWBiBNpeBLgcMiYOqU8NQ4D%2Bhl%2FvtCmYwzNmB9LwO0L1TT0ShKVFhnoCSSsglt2D9lXbFsO1JJ%2BC374V2Pds1qxUgP003CyYNhAHTY1too%2FP1q05PRSb%2F%2BV82r%2FTUsXCZB%2Be6UskVDv4dBQTNoBjSCGsk2KjOlunaSwhK4ChgR5ogdWj8DyOXTfb3LJXio6DbEsrorHPtHymQrNAn5cbKONW5ASR3JSOyZGVyHdmdKFu6lvNilyIafqrQOGMVxjHqTbaimZsZUUUu3ZflV%2BzZ9xBDzNe1qia7sv2XARRk1kyC7V2l96R0LEuN220gPCxRSclYgqK3%2FKfjRa3AhJ%2BAojaZEFdo9hKLukMEIkOh2oqMMPP%2BC8zwTOMrRehEsutkzu3%2BAkX%2Fz%2BM1xwPRh8qZkMLI%2FwNtCtJa6o5MNjXj70GOqUBjRv%2F8eqxpj6ukxh0GHfSUwlvvzhA7qU8vKadP82hRd7BUJYqZZlAqMC%2BcVVMz20zWSJHB7%2Bf3rZR%2F3WBD6hRNJLPayHlrwIUVT80ypChg7IMPMpSfTcxKOV2uW3VBY89hB%2BGLNUetNFC6UXzzEtquHhKKg5qJuCJr4yCYsk4qjFXJKg%2BU2hcB3yLOg17ATHiyZ8RZq%2BiC6UD8oJfmNxz%2FhUGhOJD&X-Amz-Signature=c6cb99800d03da1dc629dfba3be4a11f626f027be1e7bb391ab4033212d9f5fe&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XIVG4NIV%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJHMEUCIB7gldyOEU5Qhe92WvLyHsRftYh%2BWkFhAqrV4t8w3q5lAiEA1RqZjUukzwu48pEAh2YzLPHP%2BKBi4D%2FrDgALbqw2P98q%2FwMIUBAAGgw2Mzc0MjMxODM4MDUiDLxUPF39V%2BRbhRgLmircAy6HwudeJq6us39hA04po%2BxdBganXYU3HcRig1VSyZzcLDc23N71LB0BzFqlWgLgnetPm%2FK2pyLQhyCzMHYERUFqa0%2BDH%2BQndGzihKz08M7YrXa1cD7JYaNZsKPLZ8tfu5nUEl6cY4sDNMonA1A%2FrJSb6ctirCyWOJ1VF%2B5KGY7Qo9V7%2F7cBbcXzlIezvPuxhSFq1rkcFDZ1fLvIXrZH5OcMntUrdqIeP1vTCESaUiBHJjmEdB%2BOh7x8Hzu0Rw%2F0kNCY7b5L8x6935Y21MMXBPZpBTA%2Bmlw4OFYLkd8pK2uCzsk5ioOivmcaoXxxIMI%2FVG9SSV7p4G4Qtu28UcCJPsYy9Voy2mElRdWW9mCl5A2tzIiOHrThRhePIdNTeUSRksbxpKRHeUXb8RE5hp3khpoV%2F9lgSIEOsz2lJP3QLy2%2BdAyzElubajtgqN8Y5leXfD1WDuyYtI9u6OnJSFN2orDfGQfj%2F%2F3KeFqbCGtiZAZoESV0RwfXmcoa%2BU2RHb95I5BmWJvmoMYz2aEg9kbiqnceyABFcyAU%2FHBmeNJnzqBbOMO%2Fe25PGTjsUvCqB4PpV2MNL%2Frm3%2BNEqlwHJPrREF66kPw%2FKFf1RkpguDqVEGmyjgTLwhzfYk%2FmdZlCMJ7bj70GOqUB%2F6Ay9yjgdL1evYfozgAgeVDs2mJf3G1SQM6R93lN2z0MVsb%2Bw6BI5dPu0P5aPtQUks50QJ1nmziPtM6c3QFnkNdtxpReJ5520kV1yXEk9iNKgqQpsG1Ny7CVDzxQm13xLd3K5TEJCO%2B7DzADmXCbhv5HfUgfHD6HnAoOsidB9xpb%2FjP68pNeGIe31tT7Z6IWUeMlX%2Fa9NQblYPgtUrJoDXDrWUoA&X-Amz-Signature=2a8fb80f65c86cc4609b3df98d646953e9a17b1a0e45b05da30ff876c1742ca4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46626PKALEQ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQCz0Cb52GDh7VWjPkroYAjjjnUKJpyfStIeKf5ql2nXjAIgYnN2ykMp4ro1BUVwOsk3%2FU7Osi4Q5GG%2BhTm0%2BaBbkSYq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDI9%2Fb9H9n7IPhGxqXircA8B1BjG5TL0X6mBbWFf38s3LVAIeqBjppDqtaa9eqSqZHdsHDGp8FFp8zKwTmbB0PKc0vCRiUXDEGesjBHt6P4xt6WYWYkInPh3WpyAUNdOZmaEOcmkqm3VSiicEi6IQ3UGB14JnV2uKObmBCa4%2Bpmr3H27b28OssD2PbhAvS45Y4cMopd0ZQZkYMdvBjSlYWSgSKFO1PezuzOSCySkqfQSc8sTj2MyPcYRrf6RD6EgfxLSfBn3eSvzqfEqeLFFjTj7eZgoywMait9pkTuAuzXRV3J7K8QxBnBNxTjErVapKPAqbBZTDILyRV4FwrYBzz6K0Pqiva55%2B6lIHW7q%2BUHkstfgH76gpqZeR1tLOeD9MLrI5mV5bABXQAp%2FW7N5KvEHWzNlNQA6Bz8b5g%2BQaD7QAH%2B1kDFBD4naUiYnFHLrCaDe9E7Qrn%2F15eF%2FDjby%2FpeluOpQMLs06j7sXZUYtAIZe9vzCvbj%2FbyNEfYqsuJNYEnPkl%2BM88PUQOgNtoAyJ%2BJ%2FUUXFbLMqwxK4Teixs6befZpZ6YxBFgEwqGMu1%2FrzInrMSuWpKm1LzxtTw7ttyJj43gZy5qTTBvYIpozKokDsY%2BInaqt6xIoQh0fs%2BJY54LxrahwRVTQiVNTBUMIm8jr0GOqUBgyTdHF9Mc2cQy6IS7px28IQTumZu1pVSPpulrrRnbl43eD7%2BFQH3y2sZ4PxTjY9pvg4SBEEQ%2FdrOG4thnHAjW7knOrgffJKN86LJaK52ehHOTZOpTa5Vkj%2BAT9%2B0r%2FYS1g%2F7zrGjWXdMfGv9ZmKMzOhlM4KpyZp1R%2B0gVRJ5Jh2GAO%2FnmY3u3BcbrBuBxBhs4Yn9yo1UGR2ttmVUWhtyIHfqPW2H&X-Amz-Signature=90f772310468c4209b6e64d9a0d7f5ced403950cd907449bd95093ca2f823485&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46626PKALEQ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQCz0Cb52GDh7VWjPkroYAjjjnUKJpyfStIeKf5ql2nXjAIgYnN2ykMp4ro1BUVwOsk3%2FU7Osi4Q5GG%2BhTm0%2BaBbkSYq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDI9%2Fb9H9n7IPhGxqXircA8B1BjG5TL0X6mBbWFf38s3LVAIeqBjppDqtaa9eqSqZHdsHDGp8FFp8zKwTmbB0PKc0vCRiUXDEGesjBHt6P4xt6WYWYkInPh3WpyAUNdOZmaEOcmkqm3VSiicEi6IQ3UGB14JnV2uKObmBCa4%2Bpmr3H27b28OssD2PbhAvS45Y4cMopd0ZQZkYMdvBjSlYWSgSKFO1PezuzOSCySkqfQSc8sTj2MyPcYRrf6RD6EgfxLSfBn3eSvzqfEqeLFFjTj7eZgoywMait9pkTuAuzXRV3J7K8QxBnBNxTjErVapKPAqbBZTDILyRV4FwrYBzz6K0Pqiva55%2B6lIHW7q%2BUHkstfgH76gpqZeR1tLOeD9MLrI5mV5bABXQAp%2FW7N5KvEHWzNlNQA6Bz8b5g%2BQaD7QAH%2B1kDFBD4naUiYnFHLrCaDe9E7Qrn%2F15eF%2FDjby%2FpeluOpQMLs06j7sXZUYtAIZe9vzCvbj%2FbyNEfYqsuJNYEnPkl%2BM88PUQOgNtoAyJ%2BJ%2FUUXFbLMqwxK4Teixs6befZpZ6YxBFgEwqGMu1%2FrzInrMSuWpKm1LzxtTw7ttyJj43gZy5qTTBvYIpozKokDsY%2BInaqt6xIoQh0fs%2BJY54LxrahwRVTQiVNTBUMIm8jr0GOqUBgyTdHF9Mc2cQy6IS7px28IQTumZu1pVSPpulrrRnbl43eD7%2BFQH3y2sZ4PxTjY9pvg4SBEEQ%2FdrOG4thnHAjW7knOrgffJKN86LJaK52ehHOTZOpTa5Vkj%2BAT9%2B0r%2FYS1g%2F7zrGjWXdMfGv9ZmKMzOhlM4KpyZp1R%2B0gVRJ5Jh2GAO%2FnmY3u3BcbrBuBxBhs4Yn9yo1UGR2ttmVUWhtyIHfqPW2H&X-Amz-Signature=673782364b2d5a8929d4db405b1d508a3cdec6291da2f9824b1fb392f6211b7b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46626PKALEQ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQCz0Cb52GDh7VWjPkroYAjjjnUKJpyfStIeKf5ql2nXjAIgYnN2ykMp4ro1BUVwOsk3%2FU7Osi4Q5GG%2BhTm0%2BaBbkSYq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDI9%2Fb9H9n7IPhGxqXircA8B1BjG5TL0X6mBbWFf38s3LVAIeqBjppDqtaa9eqSqZHdsHDGp8FFp8zKwTmbB0PKc0vCRiUXDEGesjBHt6P4xt6WYWYkInPh3WpyAUNdOZmaEOcmkqm3VSiicEi6IQ3UGB14JnV2uKObmBCa4%2Bpmr3H27b28OssD2PbhAvS45Y4cMopd0ZQZkYMdvBjSlYWSgSKFO1PezuzOSCySkqfQSc8sTj2MyPcYRrf6RD6EgfxLSfBn3eSvzqfEqeLFFjTj7eZgoywMait9pkTuAuzXRV3J7K8QxBnBNxTjErVapKPAqbBZTDILyRV4FwrYBzz6K0Pqiva55%2B6lIHW7q%2BUHkstfgH76gpqZeR1tLOeD9MLrI5mV5bABXQAp%2FW7N5KvEHWzNlNQA6Bz8b5g%2BQaD7QAH%2B1kDFBD4naUiYnFHLrCaDe9E7Qrn%2F15eF%2FDjby%2FpeluOpQMLs06j7sXZUYtAIZe9vzCvbj%2FbyNEfYqsuJNYEnPkl%2BM88PUQOgNtoAyJ%2BJ%2FUUXFbLMqwxK4Teixs6befZpZ6YxBFgEwqGMu1%2FrzInrMSuWpKm1LzxtTw7ttyJj43gZy5qTTBvYIpozKokDsY%2BInaqt6xIoQh0fs%2BJY54LxrahwRVTQiVNTBUMIm8jr0GOqUBgyTdHF9Mc2cQy6IS7px28IQTumZu1pVSPpulrrRnbl43eD7%2BFQH3y2sZ4PxTjY9pvg4SBEEQ%2FdrOG4thnHAjW7knOrgffJKN86LJaK52ehHOTZOpTa5Vkj%2BAT9%2B0r%2FYS1g%2F7zrGjWXdMfGv9ZmKMzOhlM4KpyZp1R%2B0gVRJ5Jh2GAO%2FnmY3u3BcbrBuBxBhs4Yn9yo1UGR2ttmVUWhtyIHfqPW2H&X-Amz-Signature=1ebd584967a9de3c22061c64f92f782cb80267a46074c0f12da5ae282b368fd1&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46626PKALEQ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQCz0Cb52GDh7VWjPkroYAjjjnUKJpyfStIeKf5ql2nXjAIgYnN2ykMp4ro1BUVwOsk3%2FU7Osi4Q5GG%2BhTm0%2BaBbkSYq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDI9%2Fb9H9n7IPhGxqXircA8B1BjG5TL0X6mBbWFf38s3LVAIeqBjppDqtaa9eqSqZHdsHDGp8FFp8zKwTmbB0PKc0vCRiUXDEGesjBHt6P4xt6WYWYkInPh3WpyAUNdOZmaEOcmkqm3VSiicEi6IQ3UGB14JnV2uKObmBCa4%2Bpmr3H27b28OssD2PbhAvS45Y4cMopd0ZQZkYMdvBjSlYWSgSKFO1PezuzOSCySkqfQSc8sTj2MyPcYRrf6RD6EgfxLSfBn3eSvzqfEqeLFFjTj7eZgoywMait9pkTuAuzXRV3J7K8QxBnBNxTjErVapKPAqbBZTDILyRV4FwrYBzz6K0Pqiva55%2B6lIHW7q%2BUHkstfgH76gpqZeR1tLOeD9MLrI5mV5bABXQAp%2FW7N5KvEHWzNlNQA6Bz8b5g%2BQaD7QAH%2B1kDFBD4naUiYnFHLrCaDe9E7Qrn%2F15eF%2FDjby%2FpeluOpQMLs06j7sXZUYtAIZe9vzCvbj%2FbyNEfYqsuJNYEnPkl%2BM88PUQOgNtoAyJ%2BJ%2FUUXFbLMqwxK4Teixs6befZpZ6YxBFgEwqGMu1%2FrzInrMSuWpKm1LzxtTw7ttyJj43gZy5qTTBvYIpozKokDsY%2BInaqt6xIoQh0fs%2BJY54LxrahwRVTQiVNTBUMIm8jr0GOqUBgyTdHF9Mc2cQy6IS7px28IQTumZu1pVSPpulrrRnbl43eD7%2BFQH3y2sZ4PxTjY9pvg4SBEEQ%2FdrOG4thnHAjW7knOrgffJKN86LJaK52ehHOTZOpTa5Vkj%2BAT9%2B0r%2FYS1g%2F7zrGjWXdMfGv9ZmKMzOhlM4KpyZp1R%2B0gVRJ5Jh2GAO%2FnmY3u3BcbrBuBxBhs4Yn9yo1UGR2ttmVUWhtyIHfqPW2H&X-Amz-Signature=8edfc75ef9fa0c2bd6ffde5541f40e380d1dcc5174700c1ae1ff06580cdb4288&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
