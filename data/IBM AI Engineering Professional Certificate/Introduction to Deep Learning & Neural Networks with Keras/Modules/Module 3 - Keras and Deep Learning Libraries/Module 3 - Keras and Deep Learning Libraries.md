

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SLEUVW6K%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIQDL6CWHSUpvHYrEmKml%2BNmiirUZRDa0Z0I08P02%2BKApBQIgCfb8LxtKBJlB3NeJhwDjTBkIYkq1dX%2F6Ei6jxh6Ph7Iq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDHomNInFfaIOABP1FyrcA5lPKZLCevkbhcWgFrw01LnXIic0Uf%2Bd%2BqwvYabBAG0ZYFZjmL4hjvMlX%2FHiFUlAMI7Ljj4wjHY59bCzYM%2BRv3TABhKn%2FlaPknb6Ga9gm%2FDHymDbCY4uaSxT9oyFT%2BASPonW2ULStNGnrKetdMBG7UYEjg1hw6jXtOfUd11%2FpVP4icVqoJPCCnrOCycFcGXBdYrdndjR8DOaJM2hV8GlGdhXcXdgWfsjERapiQDCdH6wMGpUZDnjjABnm0LyLCjE0xXXLE2MdflpX4vw%2F79ixKNUntOtqJiEDxXMTZXRP3UJAe9Xmemxql2cuEuQgocFvNoyTCjEm9O%2FNeMrtch%2FbgmrHYBkBuXTzu1l2wPuaVstgTp0M9OdzmoXWT3naShKDAzH5CKCZuoHVxdYWrT8l06oQnHwypvGs2IhCOP1DV1qaDDvxDMfLHEp1OxRYmgM7kT6bGboXYug4In0ZibL2%2FxQDvirW4XMwX%2BJc8CuYu%2BaH1wtDIrKGZuWLtX3xEd0SP4ZJR%2B4woBTlwUrqVCimnznCWQPTaLT6h%2B6BVz7teRTqjjRU4HBFNVkS%2Fulg8IHLqcsC0LExiAlPCkpFVcWJzR5hxBMZtzSLOFXLIgsKB2%2Fz9Q9cDAgYC%2B4AXwbMJf%2Bmb0GOqUBgzdbposI8J%2Fsjzx6BzGUSkvC69HjQt57WEORkT%2By9XeIXxMBtaNni92hBA3yO32Gtz2QOFh6XQX7cHP157cCCKd9tGuX7H%2F6QJ7InVcmCoZXc3mM%2Bu1sjJ6V0BxN2JkK7nZHtNpTKj2yeZrTBvlN3hl4FBh1nMEP5XAL%2FUFiUYmhtJq%2BDn1S81ZSa%2BN%2BFax%2FR7kI6mtpCdhcjPqYuyN%2BK1Yyb20y&X-Amz-Signature=4475a8df88171fe5335d72d1a74615938836c6d696ddb3c622cd59ee8c64f9f7&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SLEUVW6K%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIQDL6CWHSUpvHYrEmKml%2BNmiirUZRDa0Z0I08P02%2BKApBQIgCfb8LxtKBJlB3NeJhwDjTBkIYkq1dX%2F6Ei6jxh6Ph7Iq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDHomNInFfaIOABP1FyrcA5lPKZLCevkbhcWgFrw01LnXIic0Uf%2Bd%2BqwvYabBAG0ZYFZjmL4hjvMlX%2FHiFUlAMI7Ljj4wjHY59bCzYM%2BRv3TABhKn%2FlaPknb6Ga9gm%2FDHymDbCY4uaSxT9oyFT%2BASPonW2ULStNGnrKetdMBG7UYEjg1hw6jXtOfUd11%2FpVP4icVqoJPCCnrOCycFcGXBdYrdndjR8DOaJM2hV8GlGdhXcXdgWfsjERapiQDCdH6wMGpUZDnjjABnm0LyLCjE0xXXLE2MdflpX4vw%2F79ixKNUntOtqJiEDxXMTZXRP3UJAe9Xmemxql2cuEuQgocFvNoyTCjEm9O%2FNeMrtch%2FbgmrHYBkBuXTzu1l2wPuaVstgTp0M9OdzmoXWT3naShKDAzH5CKCZuoHVxdYWrT8l06oQnHwypvGs2IhCOP1DV1qaDDvxDMfLHEp1OxRYmgM7kT6bGboXYug4In0ZibL2%2FxQDvirW4XMwX%2BJc8CuYu%2BaH1wtDIrKGZuWLtX3xEd0SP4ZJR%2B4woBTlwUrqVCimnznCWQPTaLT6h%2B6BVz7teRTqjjRU4HBFNVkS%2Fulg8IHLqcsC0LExiAlPCkpFVcWJzR5hxBMZtzSLOFXLIgsKB2%2Fz9Q9cDAgYC%2B4AXwbMJf%2Bmb0GOqUBgzdbposI8J%2Fsjzx6BzGUSkvC69HjQt57WEORkT%2By9XeIXxMBtaNni92hBA3yO32Gtz2QOFh6XQX7cHP157cCCKd9tGuX7H%2F6QJ7InVcmCoZXc3mM%2Bu1sjJ6V0BxN2JkK7nZHtNpTKj2yeZrTBvlN3hl4FBh1nMEP5XAL%2FUFiUYmhtJq%2BDn1S81ZSa%2BN%2BFax%2FR7kI6mtpCdhcjPqYuyN%2BK1Yyb20y&X-Amz-Signature=00f004f294831c3c1bec6fa4a2553372657f77d253d0fd4357399e881ed14741&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SLEUVW6K%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIQDL6CWHSUpvHYrEmKml%2BNmiirUZRDa0Z0I08P02%2BKApBQIgCfb8LxtKBJlB3NeJhwDjTBkIYkq1dX%2F6Ei6jxh6Ph7Iq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDHomNInFfaIOABP1FyrcA5lPKZLCevkbhcWgFrw01LnXIic0Uf%2Bd%2BqwvYabBAG0ZYFZjmL4hjvMlX%2FHiFUlAMI7Ljj4wjHY59bCzYM%2BRv3TABhKn%2FlaPknb6Ga9gm%2FDHymDbCY4uaSxT9oyFT%2BASPonW2ULStNGnrKetdMBG7UYEjg1hw6jXtOfUd11%2FpVP4icVqoJPCCnrOCycFcGXBdYrdndjR8DOaJM2hV8GlGdhXcXdgWfsjERapiQDCdH6wMGpUZDnjjABnm0LyLCjE0xXXLE2MdflpX4vw%2F79ixKNUntOtqJiEDxXMTZXRP3UJAe9Xmemxql2cuEuQgocFvNoyTCjEm9O%2FNeMrtch%2FbgmrHYBkBuXTzu1l2wPuaVstgTp0M9OdzmoXWT3naShKDAzH5CKCZuoHVxdYWrT8l06oQnHwypvGs2IhCOP1DV1qaDDvxDMfLHEp1OxRYmgM7kT6bGboXYug4In0ZibL2%2FxQDvirW4XMwX%2BJc8CuYu%2BaH1wtDIrKGZuWLtX3xEd0SP4ZJR%2B4woBTlwUrqVCimnznCWQPTaLT6h%2B6BVz7teRTqjjRU4HBFNVkS%2Fulg8IHLqcsC0LExiAlPCkpFVcWJzR5hxBMZtzSLOFXLIgsKB2%2Fz9Q9cDAgYC%2B4AXwbMJf%2Bmb0GOqUBgzdbposI8J%2Fsjzx6BzGUSkvC69HjQt57WEORkT%2By9XeIXxMBtaNni92hBA3yO32Gtz2QOFh6XQX7cHP157cCCKd9tGuX7H%2F6QJ7InVcmCoZXc3mM%2Bu1sjJ6V0BxN2JkK7nZHtNpTKj2yeZrTBvlN3hl4FBh1nMEP5XAL%2FUFiUYmhtJq%2BDn1S81ZSa%2BN%2BFax%2FR7kI6mtpCdhcjPqYuyN%2BK1Yyb20y&X-Amz-Signature=1820945815b94535f6a7e8f858f0d8b654c8770dab029e373209bb7490b3322e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663S5YVMCY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJIMEYCIQDMsIzLTyse9pwlagNgk2UiTHSX2xTKg%2F5jZuiXEHjZ2gIhAJ1uqxDwZcIef5mGtslIziSH16tFM4FxynxAw7mnJiO%2FKv8DCH8QABoMNjM3NDIzMTgzODA1Igz%2Byjhmx8Y8ElRdKlQq3APS2Y9TvzZ9DVpmepgsW%2FUtDUJAu0bYBEzNnAuDf4x9XTkwJdpiQWpbWU1TYBaH7XZb9korToexiCTx%2BiBVWc7uyfBLyfBC07ZFhdLVJFScaH%2B9cJ3igxaIA7gpwzPdcwpdw1WSQc2Kz1SiBXkB6XDUdV1UOdzGQaFg1tV0INiMS4qIfC1OvXnCTzzv0uiRXPC9IYZvUuUDL%2BTAvInFgSmKRlEx0s2f%2FwL6cgL9sJwwGA9JTuFBoGpmX4QiX8zyk7y1nr%2BBzATlX7snQhM8CesrpeqxNFYOzPUeDPi4eVnQ%2FeGzQOlEOadYKgB6kdsm3%2FEmJf7x1H7cY2aWCoqsGUVDA5kEap4jHQVsaaHEaZyXiutklZzakFxASlUgQ7KoP6ueyO30DmZdfn4cTfTRjrVHV473JfQJVSVR5TeSHhbjttQq5L%2B1irf83eTjhhBmM39LX6Yp%2FNJjQ29l7XaRIiVc8HrpEookfm2etqpnvyb7jiSZKKKaQC%2BrLOke3pLq301fyjgiR1lGHqcfPIAk%2BaSaU6QK0S%2FIDwYrQHhDvqU%2FxQfcoYKDEga8Nn1fDEnfEk6oo%2FrjmZkfA%2BcSxuRcqAcR8jEeP9CId5zZWD2Sl22E1eUJpMX1BrDv0IURlTCT%2Fpm9BjqkAYKlcM98DvCFq3c1iWti%2BYPHIUONrZeENWUV4gNzfNLHrCTBZ38K7lhYJKCxLis0Z8N8mRloM9jWANwStZUsYwR%2Bv9CF1dpUs9m5uj%2BHgpDdmlnsi%2BrXNK05jaM9hnzvifrSOy9Q0L3YMmCA3paLQS7swrpwhaLpg5X9SF1vZRG%2Fg5GPPkTAu7Dfyzqq21o%2BGc%2F%2BtMBRtuJBc9qZvHjqTY6cycok&X-Amz-Signature=8b748d3911472e1dd01b927ec740fee0ecc8ad1cf805e017afdb8651ea6f81c6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VBRZSGGE%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJIMEYCIQDJNqxWPk8KZHmCKcwwyOWAKzJjv0H7sg3M6wHjQpnbrAIhAMtV5MAxNJMKJqAHgrXKGlU%2Bvttd4VaimrF6z9DwxQH1Kv8DCH8QABoMNjM3NDIzMTgzODA1IgxdKGEZnxKLJisp2l4q3APWg0qITWDS0KEuufMxXFrcgetVjjiT9qwuFexJkCw%2BzqPu91f%2BemlABX39e5knY4PKm%2BptHZe93GdggDpZh44fALGJjodkXCiLEg5a6jc4EEkUgr8Dbc%2F5htqPG9QcDofqkN3AxW9Abwiq3OKxgMR5mnXusho2xOiEYhVHZOqQ3rP5dPEUcRYV8HudGCqI57YHqKCYxT8kMBMdm4nesKR4xD8JwgroS5Zf91oatVDB2h4cN1c8QCf9SSk8MNaJ55TNWsO0Ny4XmbAaJiR7bciSsrC2WUss0Ro1%2FlxcS7RjU2r%2FxevF%2FEJXzopTFFQpeZLB2dOOPVs8bDX%2BIncbItLhF1tAWmgehUlhDrCvB3XlzXzPHC7%2B1mNI14uIqkOrlFreGCUZyS3h76LAfdJBqxNHSKJjjMIVsmC9xcCOlCTNKS1RQLRTxg9F0RT6T5X8yrtNwZ6fR0ulz%2BbyDSgcRQhYZsv7fJeumzlISr1jXazRHA73qje0AqecOEuTsHdjeda7M9PLj85kqmpJtsrRRlYvNLN%2BCOmSjq%2BKPtPJaatVK2Dxv7I%2FZVajNiB%2FHzfxLQ%2F17yiInT1kFgI3PwMnKpAtWra1J0xWL0nzWeWk3e8BgIARyjfQRE1L1UOnJTCi%2Fpm9BjqkAQXwzinhjx4gnhV%2BfnmJaQKj49tUYSkqFdeNeo0ZcHZSTK3WRajI18czOcEETCm7XgwE3yk0rW7WzvYAGjp3M4fmuTbQ%2B6Gwr5iOp%2FTh5iMMayFeKN5DhrQJhicruAzJscanlYLmMf2jtLATn9Q%2FO3d%2FagFRYGRDpfsp5Av9m7qHfrK%2BBbBsoBQFsaiOcn0hhEaPZ%2BZQ5bKE5aqPExbE%2FG%2B1gz0g&X-Amz-Signature=a458356b59a0325a7861bf65143c22347cb4ab03268b73784e70874d28e8aab7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SLEUVW6K%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIQDL6CWHSUpvHYrEmKml%2BNmiirUZRDa0Z0I08P02%2BKApBQIgCfb8LxtKBJlB3NeJhwDjTBkIYkq1dX%2F6Ei6jxh6Ph7Iq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDHomNInFfaIOABP1FyrcA5lPKZLCevkbhcWgFrw01LnXIic0Uf%2Bd%2BqwvYabBAG0ZYFZjmL4hjvMlX%2FHiFUlAMI7Ljj4wjHY59bCzYM%2BRv3TABhKn%2FlaPknb6Ga9gm%2FDHymDbCY4uaSxT9oyFT%2BASPonW2ULStNGnrKetdMBG7UYEjg1hw6jXtOfUd11%2FpVP4icVqoJPCCnrOCycFcGXBdYrdndjR8DOaJM2hV8GlGdhXcXdgWfsjERapiQDCdH6wMGpUZDnjjABnm0LyLCjE0xXXLE2MdflpX4vw%2F79ixKNUntOtqJiEDxXMTZXRP3UJAe9Xmemxql2cuEuQgocFvNoyTCjEm9O%2FNeMrtch%2FbgmrHYBkBuXTzu1l2wPuaVstgTp0M9OdzmoXWT3naShKDAzH5CKCZuoHVxdYWrT8l06oQnHwypvGs2IhCOP1DV1qaDDvxDMfLHEp1OxRYmgM7kT6bGboXYug4In0ZibL2%2FxQDvirW4XMwX%2BJc8CuYu%2BaH1wtDIrKGZuWLtX3xEd0SP4ZJR%2B4woBTlwUrqVCimnznCWQPTaLT6h%2B6BVz7teRTqjjRU4HBFNVkS%2Fulg8IHLqcsC0LExiAlPCkpFVcWJzR5hxBMZtzSLOFXLIgsKB2%2Fz9Q9cDAgYC%2B4AXwbMJf%2Bmb0GOqUBgzdbposI8J%2Fsjzx6BzGUSkvC69HjQt57WEORkT%2By9XeIXxMBtaNni92hBA3yO32Gtz2QOFh6XQX7cHP157cCCKd9tGuX7H%2F6QJ7InVcmCoZXc3mM%2Bu1sjJ6V0BxN2JkK7nZHtNpTKj2yeZrTBvlN3hl4FBh1nMEP5XAL%2FUFiUYmhtJq%2BDn1S81ZSa%2BN%2BFax%2FR7kI6mtpCdhcjPqYuyN%2BK1Yyb20y&X-Amz-Signature=1d2a40a4334a71347dffe0775bc3f289f93173d757476b2f5cefb087cc436297&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SLEUVW6K%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIQDL6CWHSUpvHYrEmKml%2BNmiirUZRDa0Z0I08P02%2BKApBQIgCfb8LxtKBJlB3NeJhwDjTBkIYkq1dX%2F6Ei6jxh6Ph7Iq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDHomNInFfaIOABP1FyrcA5lPKZLCevkbhcWgFrw01LnXIic0Uf%2Bd%2BqwvYabBAG0ZYFZjmL4hjvMlX%2FHiFUlAMI7Ljj4wjHY59bCzYM%2BRv3TABhKn%2FlaPknb6Ga9gm%2FDHymDbCY4uaSxT9oyFT%2BASPonW2ULStNGnrKetdMBG7UYEjg1hw6jXtOfUd11%2FpVP4icVqoJPCCnrOCycFcGXBdYrdndjR8DOaJM2hV8GlGdhXcXdgWfsjERapiQDCdH6wMGpUZDnjjABnm0LyLCjE0xXXLE2MdflpX4vw%2F79ixKNUntOtqJiEDxXMTZXRP3UJAe9Xmemxql2cuEuQgocFvNoyTCjEm9O%2FNeMrtch%2FbgmrHYBkBuXTzu1l2wPuaVstgTp0M9OdzmoXWT3naShKDAzH5CKCZuoHVxdYWrT8l06oQnHwypvGs2IhCOP1DV1qaDDvxDMfLHEp1OxRYmgM7kT6bGboXYug4In0ZibL2%2FxQDvirW4XMwX%2BJc8CuYu%2BaH1wtDIrKGZuWLtX3xEd0SP4ZJR%2B4woBTlwUrqVCimnznCWQPTaLT6h%2B6BVz7teRTqjjRU4HBFNVkS%2Fulg8IHLqcsC0LExiAlPCkpFVcWJzR5hxBMZtzSLOFXLIgsKB2%2Fz9Q9cDAgYC%2B4AXwbMJf%2Bmb0GOqUBgzdbposI8J%2Fsjzx6BzGUSkvC69HjQt57WEORkT%2By9XeIXxMBtaNni92hBA3yO32Gtz2QOFh6XQX7cHP157cCCKd9tGuX7H%2F6QJ7InVcmCoZXc3mM%2Bu1sjJ6V0BxN2JkK7nZHtNpTKj2yeZrTBvlN3hl4FBh1nMEP5XAL%2FUFiUYmhtJq%2BDn1S81ZSa%2BN%2BFax%2FR7kI6mtpCdhcjPqYuyN%2BK1Yyb20y&X-Amz-Signature=87cc7da451f7413938dede23b7abbbc897bbc83e4a8e6a0942a156dec931dffd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SLEUVW6K%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIQDL6CWHSUpvHYrEmKml%2BNmiirUZRDa0Z0I08P02%2BKApBQIgCfb8LxtKBJlB3NeJhwDjTBkIYkq1dX%2F6Ei6jxh6Ph7Iq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDHomNInFfaIOABP1FyrcA5lPKZLCevkbhcWgFrw01LnXIic0Uf%2Bd%2BqwvYabBAG0ZYFZjmL4hjvMlX%2FHiFUlAMI7Ljj4wjHY59bCzYM%2BRv3TABhKn%2FlaPknb6Ga9gm%2FDHymDbCY4uaSxT9oyFT%2BASPonW2ULStNGnrKetdMBG7UYEjg1hw6jXtOfUd11%2FpVP4icVqoJPCCnrOCycFcGXBdYrdndjR8DOaJM2hV8GlGdhXcXdgWfsjERapiQDCdH6wMGpUZDnjjABnm0LyLCjE0xXXLE2MdflpX4vw%2F79ixKNUntOtqJiEDxXMTZXRP3UJAe9Xmemxql2cuEuQgocFvNoyTCjEm9O%2FNeMrtch%2FbgmrHYBkBuXTzu1l2wPuaVstgTp0M9OdzmoXWT3naShKDAzH5CKCZuoHVxdYWrT8l06oQnHwypvGs2IhCOP1DV1qaDDvxDMfLHEp1OxRYmgM7kT6bGboXYug4In0ZibL2%2FxQDvirW4XMwX%2BJc8CuYu%2BaH1wtDIrKGZuWLtX3xEd0SP4ZJR%2B4woBTlwUrqVCimnznCWQPTaLT6h%2B6BVz7teRTqjjRU4HBFNVkS%2Fulg8IHLqcsC0LExiAlPCkpFVcWJzR5hxBMZtzSLOFXLIgsKB2%2Fz9Q9cDAgYC%2B4AXwbMJf%2Bmb0GOqUBgzdbposI8J%2Fsjzx6BzGUSkvC69HjQt57WEORkT%2By9XeIXxMBtaNni92hBA3yO32Gtz2QOFh6XQX7cHP157cCCKd9tGuX7H%2F6QJ7InVcmCoZXc3mM%2Bu1sjJ6V0BxN2JkK7nZHtNpTKj2yeZrTBvlN3hl4FBh1nMEP5XAL%2FUFiUYmhtJq%2BDn1S81ZSa%2BN%2BFax%2FR7kI6mtpCdhcjPqYuyN%2BK1Yyb20y&X-Amz-Signature=8d99d77c2397de2f076e7b43f975a484108889e8e9a76b8e788a5cd0056c20da&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SLEUVW6K%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIQDL6CWHSUpvHYrEmKml%2BNmiirUZRDa0Z0I08P02%2BKApBQIgCfb8LxtKBJlB3NeJhwDjTBkIYkq1dX%2F6Ei6jxh6Ph7Iq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDHomNInFfaIOABP1FyrcA5lPKZLCevkbhcWgFrw01LnXIic0Uf%2Bd%2BqwvYabBAG0ZYFZjmL4hjvMlX%2FHiFUlAMI7Ljj4wjHY59bCzYM%2BRv3TABhKn%2FlaPknb6Ga9gm%2FDHymDbCY4uaSxT9oyFT%2BASPonW2ULStNGnrKetdMBG7UYEjg1hw6jXtOfUd11%2FpVP4icVqoJPCCnrOCycFcGXBdYrdndjR8DOaJM2hV8GlGdhXcXdgWfsjERapiQDCdH6wMGpUZDnjjABnm0LyLCjE0xXXLE2MdflpX4vw%2F79ixKNUntOtqJiEDxXMTZXRP3UJAe9Xmemxql2cuEuQgocFvNoyTCjEm9O%2FNeMrtch%2FbgmrHYBkBuXTzu1l2wPuaVstgTp0M9OdzmoXWT3naShKDAzH5CKCZuoHVxdYWrT8l06oQnHwypvGs2IhCOP1DV1qaDDvxDMfLHEp1OxRYmgM7kT6bGboXYug4In0ZibL2%2FxQDvirW4XMwX%2BJc8CuYu%2BaH1wtDIrKGZuWLtX3xEd0SP4ZJR%2B4woBTlwUrqVCimnznCWQPTaLT6h%2B6BVz7teRTqjjRU4HBFNVkS%2Fulg8IHLqcsC0LExiAlPCkpFVcWJzR5hxBMZtzSLOFXLIgsKB2%2Fz9Q9cDAgYC%2B4AXwbMJf%2Bmb0GOqUBgzdbposI8J%2Fsjzx6BzGUSkvC69HjQt57WEORkT%2By9XeIXxMBtaNni92hBA3yO32Gtz2QOFh6XQX7cHP157cCCKd9tGuX7H%2F6QJ7InVcmCoZXc3mM%2Bu1sjJ6V0BxN2JkK7nZHtNpTKj2yeZrTBvlN3hl4FBh1nMEP5XAL%2FUFiUYmhtJq%2BDn1S81ZSa%2BN%2BFax%2FR7kI6mtpCdhcjPqYuyN%2BK1Yyb20y&X-Amz-Signature=c08c344a7caa521a6e375eacd0f8d7d7692e06c1f6f5c624d1271c500810de6f&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
