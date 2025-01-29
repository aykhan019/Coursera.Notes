

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664B5DQPIS%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJHMEUCIQDyK%2FN4lSnT1iO5%2Bkw28LOMBcdjC4NT2L%2FO4Zc4F8bYRAIgCbmqvGs7TX0HL5dTI5zg0%2FaVr0f32iZrqC9CNiOWi8IqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJrU48YFZOp8Ir0njSrcA7OH3Fv%2BPe8noVnzl6eYTD%2FTIQe6dL7PjHbHd2SLeYyEFh4vAcDgThhsOlQyT4w6lVvk5HR4j2BiX4eaUBQijZlwIJxpbdJx8buwkoDRFemkCBgINrd%2BGWVJeRbLvuJPiyZSYet5StnJZXHlDBU6OqPelTA9H5e8riuAJ7A8%2Be4MoxQ0zvsQvMy57qC%2BN9VATP1vX0Q3l17tZOHozrs4sHccQHXNJrweaWo2ReDHLWv6WDMIi9ldDrD2PefI2TWFWCApxkbPwTB7ECFKJZfpgAOhJxaySXha9hZfWuJT0%2FDtZJdsMe5oi%2FZPMARF9kXXFf3%2FGoC07eKJPpT%2FUZ05VERi3%2F8FbFrwQ287NEt7WVAS6hBbY0ETiYrz9ep8Xw7vCN0Ayqeci%2FSNihC2x2LGZ5wtsMqChjb7fucwuqxiJXMS8CSvTja7UFggQ95tP44r4bMPiVl0X6OibZ56PriOHaEQlcK7hzeMEqIDdQLtJxzOPV7nKxv8NuNz0ax88rAyiijk65%2BISvxI7p2Kmn7Dzott1HD%2FjtlqIIFSiZREI1kwuY47ehzadXFuWvo9YqsQd17hZCcB6QS7rX%2F%2FzpFRn2bWB%2FKUqgwFuYtl5jpvFs4d4pp2Sya11LYUtXOIMLmf5rwGOqUBkmt6lqmyRgcmQGqKi1rJSMv5AkKJpb6cYpmhDNKJpfsp2%2FC6Jjqp8KNtTTg8PDOYyKTQNmbKrhbp0gP39JJZK0khjboAtoxkKsxFagTkHbBXoiabc28M9wWEb4LYFMuTACQLu%2B4q%2FXpo6NlxcmCBME5UBrgaJ0b9R8G1g166L67HmZvcojpsmppVVrLn82NGDvenj8ldRnf5%2FSPbQrW9Im8DHvkB&X-Amz-Signature=40f74ae848c5e717e2679268cda6df7c031fa0224cc353ca3d4b8bdb608dcc67&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664B5DQPIS%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJHMEUCIQDyK%2FN4lSnT1iO5%2Bkw28LOMBcdjC4NT2L%2FO4Zc4F8bYRAIgCbmqvGs7TX0HL5dTI5zg0%2FaVr0f32iZrqC9CNiOWi8IqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJrU48YFZOp8Ir0njSrcA7OH3Fv%2BPe8noVnzl6eYTD%2FTIQe6dL7PjHbHd2SLeYyEFh4vAcDgThhsOlQyT4w6lVvk5HR4j2BiX4eaUBQijZlwIJxpbdJx8buwkoDRFemkCBgINrd%2BGWVJeRbLvuJPiyZSYet5StnJZXHlDBU6OqPelTA9H5e8riuAJ7A8%2Be4MoxQ0zvsQvMy57qC%2BN9VATP1vX0Q3l17tZOHozrs4sHccQHXNJrweaWo2ReDHLWv6WDMIi9ldDrD2PefI2TWFWCApxkbPwTB7ECFKJZfpgAOhJxaySXha9hZfWuJT0%2FDtZJdsMe5oi%2FZPMARF9kXXFf3%2FGoC07eKJPpT%2FUZ05VERi3%2F8FbFrwQ287NEt7WVAS6hBbY0ETiYrz9ep8Xw7vCN0Ayqeci%2FSNihC2x2LGZ5wtsMqChjb7fucwuqxiJXMS8CSvTja7UFggQ95tP44r4bMPiVl0X6OibZ56PriOHaEQlcK7hzeMEqIDdQLtJxzOPV7nKxv8NuNz0ax88rAyiijk65%2BISvxI7p2Kmn7Dzott1HD%2FjtlqIIFSiZREI1kwuY47ehzadXFuWvo9YqsQd17hZCcB6QS7rX%2F%2FzpFRn2bWB%2FKUqgwFuYtl5jpvFs4d4pp2Sya11LYUtXOIMLmf5rwGOqUBkmt6lqmyRgcmQGqKi1rJSMv5AkKJpb6cYpmhDNKJpfsp2%2FC6Jjqp8KNtTTg8PDOYyKTQNmbKrhbp0gP39JJZK0khjboAtoxkKsxFagTkHbBXoiabc28M9wWEb4LYFMuTACQLu%2B4q%2FXpo6NlxcmCBME5UBrgaJ0b9R8G1g166L67HmZvcojpsmppVVrLn82NGDvenj8ldRnf5%2FSPbQrW9Im8DHvkB&X-Amz-Signature=2c5d7bb67d121eea5bc801b61d73fddc8ce3158dda5eda05244fc8d0a9952b4c&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664B5DQPIS%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJHMEUCIQDyK%2FN4lSnT1iO5%2Bkw28LOMBcdjC4NT2L%2FO4Zc4F8bYRAIgCbmqvGs7TX0HL5dTI5zg0%2FaVr0f32iZrqC9CNiOWi8IqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJrU48YFZOp8Ir0njSrcA7OH3Fv%2BPe8noVnzl6eYTD%2FTIQe6dL7PjHbHd2SLeYyEFh4vAcDgThhsOlQyT4w6lVvk5HR4j2BiX4eaUBQijZlwIJxpbdJx8buwkoDRFemkCBgINrd%2BGWVJeRbLvuJPiyZSYet5StnJZXHlDBU6OqPelTA9H5e8riuAJ7A8%2Be4MoxQ0zvsQvMy57qC%2BN9VATP1vX0Q3l17tZOHozrs4sHccQHXNJrweaWo2ReDHLWv6WDMIi9ldDrD2PefI2TWFWCApxkbPwTB7ECFKJZfpgAOhJxaySXha9hZfWuJT0%2FDtZJdsMe5oi%2FZPMARF9kXXFf3%2FGoC07eKJPpT%2FUZ05VERi3%2F8FbFrwQ287NEt7WVAS6hBbY0ETiYrz9ep8Xw7vCN0Ayqeci%2FSNihC2x2LGZ5wtsMqChjb7fucwuqxiJXMS8CSvTja7UFggQ95tP44r4bMPiVl0X6OibZ56PriOHaEQlcK7hzeMEqIDdQLtJxzOPV7nKxv8NuNz0ax88rAyiijk65%2BISvxI7p2Kmn7Dzott1HD%2FjtlqIIFSiZREI1kwuY47ehzadXFuWvo9YqsQd17hZCcB6QS7rX%2F%2FzpFRn2bWB%2FKUqgwFuYtl5jpvFs4d4pp2Sya11LYUtXOIMLmf5rwGOqUBkmt6lqmyRgcmQGqKi1rJSMv5AkKJpb6cYpmhDNKJpfsp2%2FC6Jjqp8KNtTTg8PDOYyKTQNmbKrhbp0gP39JJZK0khjboAtoxkKsxFagTkHbBXoiabc28M9wWEb4LYFMuTACQLu%2B4q%2FXpo6NlxcmCBME5UBrgaJ0b9R8G1g166L67HmZvcojpsmppVVrLn82NGDvenj8ldRnf5%2FSPbQrW9Im8DHvkB&X-Amz-Signature=c364933307c134ab982ade59e12e22b4e2326b9fb7a9a91cade895a6499674ca&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WERU3FGB%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031619Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIEXUFgmxDjxOkbfMT%2Bmt2y4M2E0ahWAbWXZ4SN6eU16KAiBE5WImqD3UPXb%2F2ESKnWLVVmdci%2FOWIrtEtDu5Li%2BrFiqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMXNBzdaf9bhd1basJKtwDeSxWhr7qa8rf6n2v4zb%2FfgFXE7teKouRm7K1MBTCY2AzCk2xbpCrqNGI7r2KPMaXQ58UDGNP3Dp72HXc5WjAEL5KeFEdalD3%2BwdFaJXKd5TewJYL3EB54r6rmFIw%2Ft0mJ02mpjsN1nIYMptW9VwJliG3mQayxSXswf7f3tQ9SdVNgxUZDPlniYBSNKqMEyMG%2BjjdGvXlA10ZS2M4mk4lSfBUEgFLQeyqjcX7Rn65RlurOBk%2FwZZ8GYZ7lLZJzmx9%2FSBYXc2oLto0MP0ONC3T%2FqfWSq6Gwtl8O7FGYTlDBs0SBXXWulmp41eSf%2BypayM2%2FhXNmaNLgWgyTIoZ6RsdztH%2FndPp3BXyj%2BVPQKgVaUJBaZemvdVAeLDCobpVb3CAgap2U8uGE%2FD0oiab%2F8KyhmDH7mc3RNw4DAwbqdTSjtwWEheaF3KfYoiwJU%2BAU0t8F%2FuCaIHINlcK157HukkxeBLNgGssSZjHISmAJYtUqFivLujW%2BkdPWM4N09Dujtq6UUvuTADY3aFaGTk4RWHWtwUOsx8DE%2FQZz20KaS4Dm6buWmHLe1Gh97TlyzVG%2BaRUNsJUbfLmy5WuB6JJBiagvlM33AXRPRr8kCCKZHtG1D1WmPZyWBPlo9yFjHwwjKDmvAY6pgFMIk3o6UhnzPI6JjFTCQzHSRlxIypQnuWf0vD2vfu94OOEl8NFb6EU7ucUUN5Ljl36kBxkj4dDxEWCFlw%2BxjjdVhaEA10MyFPsEh1DWng8nY30hisQo91oivU6dJk4%2BOvEypcpMKgdQ0uAoXgTsguF8tbD4Lp90eO%2FHnl0a9X3Hgl28cYX8LQqLCDJCrxKtj0S1ydKTtT7s7QIRyyO8v%2BWzH8xvXr3&X-Amz-Signature=9510c34f9b8ad09fe6256f7ef3bcac1587c56aa85451d6ab6753490c67fdbc1e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFTCRUBX%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031618Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCH1y5TvxrIQygwxF0FG%2F4sJ5YP1GllnHFlDgCA0mUascCIQCYHmWk6zZYJwXpH%2BZL4jp3YVpxa2jI8ueCy3HJvn1w6CqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMd45i1YmmFaBsuYyIKtwDvNolcbLc%2BsFIIJMvvAi9qWyZKMt1K%2BzW4FISDOXFw5MYoRMqD7dw32wpti%2FNqST%2F5z4rFlTR55RodurvAAyQ%2FEGUEl53GgI03tKXr0LkZDBeh4gw%2Baw8gPL%2FH612ZWBPURuT06zdXVU5vBtWHPXu7mhacbWaEM1%2B0nw9HkYSEA9LBTBeke5YMfr97ZABsePiR%2Bsuwb1pg5pTZXyeeJ5W%2Bu14jF38B5hlDpFnNpasrwskxW5uLyy%2Bg7jRCsfMTIzIvf4eK7H%2FECHVPrMVrQ8E%2Ba5Dt5hVcFhRDqQGjPGMmozADioIDadtfe1ABZ8Y1xcvMw7TPllGPndjqqTehZRC9plpOv3%2FNECU7L7SfjaIxrOgyro%2FNRs%2F3oO%2FT161iF3yxJFQ7445xzA7FnRk2qfroC9b1jAQnGE8699oauk9SkfTk9mi7B14Ul5dW1IOS4Yrs%2BA%2BT5GPkfw2ZDlBN%2F8gEnH3BizczgyIPvLnqv7s1qAauBdlmE4KwPQIEFQVNlk363pR5brfvEcwHI0H3zPC1rjZa0Raj8wcjemt3%2BgA2bssaQGkq5yJXFpMX5k3b1Yvwm%2BWLuHZRR6DxakwKHo6imnevX2dhPDWM29Pj7Salh8qcpZ9CfqxwUsdgM0w6p%2FmvAY6pgHKotyF%2F%2FhChTaJhtUnMxCIsnq9UVoEGtzKPpxAhPQF7cAbTOk8ea8FiJN4cpHLG40EzHfBwHHO1oQ0FBfvT4EuF6lBAfZiS57twjnmF3k6l5TyRnE0VLp7zJUiXogouhBxK9TrXiRXaMCuKgWWcR2ssjT1rn7FsdlYLC51%2Fs2miawLmekbsoT%2FtKg6BJQx5Ca4hioqVeQKIYPLRM7g48keNaYl7dqs&X-Amz-Signature=3de4222235838904c3c7521e257b8e113fbbec3a42b92278ca193d0f57ec7f74&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664B5DQPIS%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJHMEUCIQDyK%2FN4lSnT1iO5%2Bkw28LOMBcdjC4NT2L%2FO4Zc4F8bYRAIgCbmqvGs7TX0HL5dTI5zg0%2FaVr0f32iZrqC9CNiOWi8IqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJrU48YFZOp8Ir0njSrcA7OH3Fv%2BPe8noVnzl6eYTD%2FTIQe6dL7PjHbHd2SLeYyEFh4vAcDgThhsOlQyT4w6lVvk5HR4j2BiX4eaUBQijZlwIJxpbdJx8buwkoDRFemkCBgINrd%2BGWVJeRbLvuJPiyZSYet5StnJZXHlDBU6OqPelTA9H5e8riuAJ7A8%2Be4MoxQ0zvsQvMy57qC%2BN9VATP1vX0Q3l17tZOHozrs4sHccQHXNJrweaWo2ReDHLWv6WDMIi9ldDrD2PefI2TWFWCApxkbPwTB7ECFKJZfpgAOhJxaySXha9hZfWuJT0%2FDtZJdsMe5oi%2FZPMARF9kXXFf3%2FGoC07eKJPpT%2FUZ05VERi3%2F8FbFrwQ287NEt7WVAS6hBbY0ETiYrz9ep8Xw7vCN0Ayqeci%2FSNihC2x2LGZ5wtsMqChjb7fucwuqxiJXMS8CSvTja7UFggQ95tP44r4bMPiVl0X6OibZ56PriOHaEQlcK7hzeMEqIDdQLtJxzOPV7nKxv8NuNz0ax88rAyiijk65%2BISvxI7p2Kmn7Dzott1HD%2FjtlqIIFSiZREI1kwuY47ehzadXFuWvo9YqsQd17hZCcB6QS7rX%2F%2FzpFRn2bWB%2FKUqgwFuYtl5jpvFs4d4pp2Sya11LYUtXOIMLmf5rwGOqUBkmt6lqmyRgcmQGqKi1rJSMv5AkKJpb6cYpmhDNKJpfsp2%2FC6Jjqp8KNtTTg8PDOYyKTQNmbKrhbp0gP39JJZK0khjboAtoxkKsxFagTkHbBXoiabc28M9wWEb4LYFMuTACQLu%2B4q%2FXpo6NlxcmCBME5UBrgaJ0b9R8G1g166L67HmZvcojpsmppVVrLn82NGDvenj8ldRnf5%2FSPbQrW9Im8DHvkB&X-Amz-Signature=ffd25bb3acf6656446c18c34d1eab1a74c0867871ac56adb1342ad8fc9ddd772&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664B5DQPIS%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJHMEUCIQDyK%2FN4lSnT1iO5%2Bkw28LOMBcdjC4NT2L%2FO4Zc4F8bYRAIgCbmqvGs7TX0HL5dTI5zg0%2FaVr0f32iZrqC9CNiOWi8IqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJrU48YFZOp8Ir0njSrcA7OH3Fv%2BPe8noVnzl6eYTD%2FTIQe6dL7PjHbHd2SLeYyEFh4vAcDgThhsOlQyT4w6lVvk5HR4j2BiX4eaUBQijZlwIJxpbdJx8buwkoDRFemkCBgINrd%2BGWVJeRbLvuJPiyZSYet5StnJZXHlDBU6OqPelTA9H5e8riuAJ7A8%2Be4MoxQ0zvsQvMy57qC%2BN9VATP1vX0Q3l17tZOHozrs4sHccQHXNJrweaWo2ReDHLWv6WDMIi9ldDrD2PefI2TWFWCApxkbPwTB7ECFKJZfpgAOhJxaySXha9hZfWuJT0%2FDtZJdsMe5oi%2FZPMARF9kXXFf3%2FGoC07eKJPpT%2FUZ05VERi3%2F8FbFrwQ287NEt7WVAS6hBbY0ETiYrz9ep8Xw7vCN0Ayqeci%2FSNihC2x2LGZ5wtsMqChjb7fucwuqxiJXMS8CSvTja7UFggQ95tP44r4bMPiVl0X6OibZ56PriOHaEQlcK7hzeMEqIDdQLtJxzOPV7nKxv8NuNz0ax88rAyiijk65%2BISvxI7p2Kmn7Dzott1HD%2FjtlqIIFSiZREI1kwuY47ehzadXFuWvo9YqsQd17hZCcB6QS7rX%2F%2FzpFRn2bWB%2FKUqgwFuYtl5jpvFs4d4pp2Sya11LYUtXOIMLmf5rwGOqUBkmt6lqmyRgcmQGqKi1rJSMv5AkKJpb6cYpmhDNKJpfsp2%2FC6Jjqp8KNtTTg8PDOYyKTQNmbKrhbp0gP39JJZK0khjboAtoxkKsxFagTkHbBXoiabc28M9wWEb4LYFMuTACQLu%2B4q%2FXpo6NlxcmCBME5UBrgaJ0b9R8G1g166L67HmZvcojpsmppVVrLn82NGDvenj8ldRnf5%2FSPbQrW9Im8DHvkB&X-Amz-Signature=ad41fe629635fd97dd78b511a6f57a7a114ddd22918e61c2a16855f19e66dd50&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664B5DQPIS%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJHMEUCIQDyK%2FN4lSnT1iO5%2Bkw28LOMBcdjC4NT2L%2FO4Zc4F8bYRAIgCbmqvGs7TX0HL5dTI5zg0%2FaVr0f32iZrqC9CNiOWi8IqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJrU48YFZOp8Ir0njSrcA7OH3Fv%2BPe8noVnzl6eYTD%2FTIQe6dL7PjHbHd2SLeYyEFh4vAcDgThhsOlQyT4w6lVvk5HR4j2BiX4eaUBQijZlwIJxpbdJx8buwkoDRFemkCBgINrd%2BGWVJeRbLvuJPiyZSYet5StnJZXHlDBU6OqPelTA9H5e8riuAJ7A8%2Be4MoxQ0zvsQvMy57qC%2BN9VATP1vX0Q3l17tZOHozrs4sHccQHXNJrweaWo2ReDHLWv6WDMIi9ldDrD2PefI2TWFWCApxkbPwTB7ECFKJZfpgAOhJxaySXha9hZfWuJT0%2FDtZJdsMe5oi%2FZPMARF9kXXFf3%2FGoC07eKJPpT%2FUZ05VERi3%2F8FbFrwQ287NEt7WVAS6hBbY0ETiYrz9ep8Xw7vCN0Ayqeci%2FSNihC2x2LGZ5wtsMqChjb7fucwuqxiJXMS8CSvTja7UFggQ95tP44r4bMPiVl0X6OibZ56PriOHaEQlcK7hzeMEqIDdQLtJxzOPV7nKxv8NuNz0ax88rAyiijk65%2BISvxI7p2Kmn7Dzott1HD%2FjtlqIIFSiZREI1kwuY47ehzadXFuWvo9YqsQd17hZCcB6QS7rX%2F%2FzpFRn2bWB%2FKUqgwFuYtl5jpvFs4d4pp2Sya11LYUtXOIMLmf5rwGOqUBkmt6lqmyRgcmQGqKi1rJSMv5AkKJpb6cYpmhDNKJpfsp2%2FC6Jjqp8KNtTTg8PDOYyKTQNmbKrhbp0gP39JJZK0khjboAtoxkKsxFagTkHbBXoiabc28M9wWEb4LYFMuTACQLu%2B4q%2FXpo6NlxcmCBME5UBrgaJ0b9R8G1g166L67HmZvcojpsmppVVrLn82NGDvenj8ldRnf5%2FSPbQrW9Im8DHvkB&X-Amz-Signature=8ed7b524b51c638b1ba23ee4528546874a26567418d69935d7628f88ba66ece2&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664B5DQPIS%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJHMEUCIQDyK%2FN4lSnT1iO5%2Bkw28LOMBcdjC4NT2L%2FO4Zc4F8bYRAIgCbmqvGs7TX0HL5dTI5zg0%2FaVr0f32iZrqC9CNiOWi8IqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJrU48YFZOp8Ir0njSrcA7OH3Fv%2BPe8noVnzl6eYTD%2FTIQe6dL7PjHbHd2SLeYyEFh4vAcDgThhsOlQyT4w6lVvk5HR4j2BiX4eaUBQijZlwIJxpbdJx8buwkoDRFemkCBgINrd%2BGWVJeRbLvuJPiyZSYet5StnJZXHlDBU6OqPelTA9H5e8riuAJ7A8%2Be4MoxQ0zvsQvMy57qC%2BN9VATP1vX0Q3l17tZOHozrs4sHccQHXNJrweaWo2ReDHLWv6WDMIi9ldDrD2PefI2TWFWCApxkbPwTB7ECFKJZfpgAOhJxaySXha9hZfWuJT0%2FDtZJdsMe5oi%2FZPMARF9kXXFf3%2FGoC07eKJPpT%2FUZ05VERi3%2F8FbFrwQ287NEt7WVAS6hBbY0ETiYrz9ep8Xw7vCN0Ayqeci%2FSNihC2x2LGZ5wtsMqChjb7fucwuqxiJXMS8CSvTja7UFggQ95tP44r4bMPiVl0X6OibZ56PriOHaEQlcK7hzeMEqIDdQLtJxzOPV7nKxv8NuNz0ax88rAyiijk65%2BISvxI7p2Kmn7Dzott1HD%2FjtlqIIFSiZREI1kwuY47ehzadXFuWvo9YqsQd17hZCcB6QS7rX%2F%2FzpFRn2bWB%2FKUqgwFuYtl5jpvFs4d4pp2Sya11LYUtXOIMLmf5rwGOqUBkmt6lqmyRgcmQGqKi1rJSMv5AkKJpb6cYpmhDNKJpfsp2%2FC6Jjqp8KNtTTg8PDOYyKTQNmbKrhbp0gP39JJZK0khjboAtoxkKsxFagTkHbBXoiabc28M9wWEb4LYFMuTACQLu%2B4q%2FXpo6NlxcmCBME5UBrgaJ0b9R8G1g166L67HmZvcojpsmppVVrLn82NGDvenj8ldRnf5%2FSPbQrW9Im8DHvkB&X-Amz-Signature=7c8266513fdef0dd51b746fedd3cbb8ceaccf1aba56677dbf9dfd51214d5ae56&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
