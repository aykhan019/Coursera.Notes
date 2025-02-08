

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663SYFKXAK%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQCO36PPiRGeWj67NjXoBu%2Fk8uDYenDILkstn6UMeEJBsQIgIYnZ0VERcEKFadVEx8wXBymFm3R%2BEUpXplw86Zb3DeEqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFjNnSS58GrJEOfh7SrcAyh8Bib07kQyn3BnH5D%2BrO8rIP8XLtZB6zaQpIM6uKMlk%2Fp8OrojjoN1vD92HtIVaMcgKTr5tJVRR6v%2Fer2M7fgxQBNaNpS2kM08rZfGiZG4mzF4pQYxktD4zz3oW7ULEwazH%2FrbIGSIFp5rkHjv3LEAfG9KEZ4rvFOmTNZ9VqiSXPU7j5qppM4g8KXXGK%2FwnLBN3gLIsYBqWp%2BgZnMAsjxH%2FxfZfIKQ3bI9cqUGs7UEHA%2Fm23kwfXUPXgAwLmjWJkEsNDf%2Fn1PlPZh97wxc6txsPO4BYrYB9ecm51JHkN%2BvNgxidU8ABjeQw4dUJgl0ofBGYq4w4h2z3TjtmpHw3rI1UlKKvjMrQb4Zj5lJ58y9Mas0ScXcm%2BFvHVXLpUGsahAM5rqOxXwnIWb4h9pS0F0HITnUufpWh87N6iFF1W46eCznOwhlKd6SYE81yqAFIO166jLQaGb3KMU11sCTCPLZMgjqhVKujhcV2R%2FmXZhoaxn7fAxwUlDrF9gbHxUbTWgsyBKHQ15O6OaHZkaJLKb9Xgcd7FphRJM%2FmGaUK5Y3X5HzC1AIR4AZGgO2Ig%2FIRt4I%2BdzPlGJMcp4CjkUpAEUnOt3ExQoXitEldY6E7V40FFbemaMFJr6wVUInMMCFnb0GOqUBFjjlr2%2FMvajYr0lJ%2BM3v0BPPHUXfR8mtuENTN8bF23caPfjDeCVQNvvns3fm3yTljeq0zh2w3FwZBs4KnHKzESU8kGxxS%2FRjZ9kBJle61aVMy1%2FtN7f4wlDwSleCAR2Mlqut%2F8WR8eoRytGiEMLytr5VpPSMxmvxpzeyxhAQAOZ%2FwYmhbZy07jYfje9VimyAE9kwWDTgdZpbz8M9BAfUatDwKiN%2F&X-Amz-Signature=ea600378bd8a9e4b7d8b87d950199c7b9e123c828e05737cca5508d619a84e90&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663SYFKXAK%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQCO36PPiRGeWj67NjXoBu%2Fk8uDYenDILkstn6UMeEJBsQIgIYnZ0VERcEKFadVEx8wXBymFm3R%2BEUpXplw86Zb3DeEqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFjNnSS58GrJEOfh7SrcAyh8Bib07kQyn3BnH5D%2BrO8rIP8XLtZB6zaQpIM6uKMlk%2Fp8OrojjoN1vD92HtIVaMcgKTr5tJVRR6v%2Fer2M7fgxQBNaNpS2kM08rZfGiZG4mzF4pQYxktD4zz3oW7ULEwazH%2FrbIGSIFp5rkHjv3LEAfG9KEZ4rvFOmTNZ9VqiSXPU7j5qppM4g8KXXGK%2FwnLBN3gLIsYBqWp%2BgZnMAsjxH%2FxfZfIKQ3bI9cqUGs7UEHA%2Fm23kwfXUPXgAwLmjWJkEsNDf%2Fn1PlPZh97wxc6txsPO4BYrYB9ecm51JHkN%2BvNgxidU8ABjeQw4dUJgl0ofBGYq4w4h2z3TjtmpHw3rI1UlKKvjMrQb4Zj5lJ58y9Mas0ScXcm%2BFvHVXLpUGsahAM5rqOxXwnIWb4h9pS0F0HITnUufpWh87N6iFF1W46eCznOwhlKd6SYE81yqAFIO166jLQaGb3KMU11sCTCPLZMgjqhVKujhcV2R%2FmXZhoaxn7fAxwUlDrF9gbHxUbTWgsyBKHQ15O6OaHZkaJLKb9Xgcd7FphRJM%2FmGaUK5Y3X5HzC1AIR4AZGgO2Ig%2FIRt4I%2BdzPlGJMcp4CjkUpAEUnOt3ExQoXitEldY6E7V40FFbemaMFJr6wVUInMMCFnb0GOqUBFjjlr2%2FMvajYr0lJ%2BM3v0BPPHUXfR8mtuENTN8bF23caPfjDeCVQNvvns3fm3yTljeq0zh2w3FwZBs4KnHKzESU8kGxxS%2FRjZ9kBJle61aVMy1%2FtN7f4wlDwSleCAR2Mlqut%2F8WR8eoRytGiEMLytr5VpPSMxmvxpzeyxhAQAOZ%2FwYmhbZy07jYfje9VimyAE9kwWDTgdZpbz8M9BAfUatDwKiN%2F&X-Amz-Signature=f182f1c9bd284cc1288f7182a4c9c30debcdf2d4bc22a8ee4521e74a8874520f&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663SYFKXAK%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQCO36PPiRGeWj67NjXoBu%2Fk8uDYenDILkstn6UMeEJBsQIgIYnZ0VERcEKFadVEx8wXBymFm3R%2BEUpXplw86Zb3DeEqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFjNnSS58GrJEOfh7SrcAyh8Bib07kQyn3BnH5D%2BrO8rIP8XLtZB6zaQpIM6uKMlk%2Fp8OrojjoN1vD92HtIVaMcgKTr5tJVRR6v%2Fer2M7fgxQBNaNpS2kM08rZfGiZG4mzF4pQYxktD4zz3oW7ULEwazH%2FrbIGSIFp5rkHjv3LEAfG9KEZ4rvFOmTNZ9VqiSXPU7j5qppM4g8KXXGK%2FwnLBN3gLIsYBqWp%2BgZnMAsjxH%2FxfZfIKQ3bI9cqUGs7UEHA%2Fm23kwfXUPXgAwLmjWJkEsNDf%2Fn1PlPZh97wxc6txsPO4BYrYB9ecm51JHkN%2BvNgxidU8ABjeQw4dUJgl0ofBGYq4w4h2z3TjtmpHw3rI1UlKKvjMrQb4Zj5lJ58y9Mas0ScXcm%2BFvHVXLpUGsahAM5rqOxXwnIWb4h9pS0F0HITnUufpWh87N6iFF1W46eCznOwhlKd6SYE81yqAFIO166jLQaGb3KMU11sCTCPLZMgjqhVKujhcV2R%2FmXZhoaxn7fAxwUlDrF9gbHxUbTWgsyBKHQ15O6OaHZkaJLKb9Xgcd7FphRJM%2FmGaUK5Y3X5HzC1AIR4AZGgO2Ig%2FIRt4I%2BdzPlGJMcp4CjkUpAEUnOt3ExQoXitEldY6E7V40FFbemaMFJr6wVUInMMCFnb0GOqUBFjjlr2%2FMvajYr0lJ%2BM3v0BPPHUXfR8mtuENTN8bF23caPfjDeCVQNvvns3fm3yTljeq0zh2w3FwZBs4KnHKzESU8kGxxS%2FRjZ9kBJle61aVMy1%2FtN7f4wlDwSleCAR2Mlqut%2F8WR8eoRytGiEMLytr5VpPSMxmvxpzeyxhAQAOZ%2FwYmhbZy07jYfje9VimyAE9kwWDTgdZpbz8M9BAfUatDwKiN%2F&X-Amz-Signature=b670bcb0f5cb00083f0720305f078939b7e7ad9813a87817c5f39b0f9b484620&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLEEF4SC%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIADxpvM%2F6jZAYyoe%2F5DXCH5ZqJIKarRD9x25YsEyzmKwAiAL86cPs9%2BON%2FzLGxXqHoillEorfNzRbGeimGK575g24yqIBAiN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMtO%2BqYRTrxiWSH%2BkIKtwDOzCpGPRW%2Bk%2B%2FO78NdtkM9bJldLHehMkzMOA4MreI%2Be%2FWWUXGkBn%2FI7%2FfoQ%2Fq9CI27uwT0hM2i%2BmhQoJ8l0u1nzNUbYVAWF2grd5sCzIGxsTFYXpIhg%2B7ycNhcpq9QY1PjfsuDOU7nXiFOFfDkultn4IwcWiQuJ7dd%2BKEe48jUHyjnFioEC4do81if8ESEiCos6CGzRWC9xF49JCvkSEb3HD%2Fg8TcYX%2F9hiY9Sqz8DxJeqCChd8REk%2BW0WeZvUBNaM7X6kqZ7qiiNzewHi0AHRazbtaG40mgcDU94GLmYjBtBDKVupB0QP8LjbgTVPrcXi9mDT6QiaSAON08VGxP24Dz62R30Fb%2BhBZUPU31%2FZ5P2iHamRPhtVNA4016XLioiaFz8EW%2F62fSxhEffwEGDUyOO2R719ihIHzb4LkcAR4feAFJcmT7SslOFuehmpZX2gkkt6eKgHMUbleSe4W3%2F4Mg3mYjg%2FWnKuRDEuXmZtLBR%2F5A5nLXnVV8ISoPZapCf%2FIjkbU9FclJC1zhu4TT1njoBNKVV2VWtgAK17I094jCATR8bN6gooWdkUGBjEXl5Yz6e8XXzQVjS3miNkTity7smV3PZP%2F%2F56lV4Xdrakfg0qF6Hn5mXmpx5Kncw4oWdvQY6pgEcr%2F8csnpWA%2FVfXL7yaRrIGBRXuSKwibP1XeulvC3iWQgyyUQGN8NAFoLa3AexeOBLzfTHZiw2YEKcGplWLsxWDA9%2BjFt9o00doerZD54Zl34MG4DvzxBbcg2p%2FgZd9W7D1cYf07jqfv2enU5qe7ssezyWhuyaMqD7qPM6uHECg4j0zknrQxK2fZsVIls2y%2FM12hfV2LTvM8x1PP4XsJQp7VMej%2Fzb&X-Amz-Signature=be493e8435223cf32d1f6014a1d08b84386f13d424f501fd725c7cda01426cb7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635RUWXJ3%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJIMEYCIQDMSnjbU7yu1R9F3S%2B%2F7Ug1C66ql%2FlKkew9O23QcrnNEQIhAP1Y1pM2CPdYa018elVPtI4AnWVp4meTFwHBKATotlAwKogECI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxK02GJIp4W7p732C0q3AP9bqScxi1%2BO8Wfb36bIPoX4CzkNmVf%2FQCsCSOh2%2BS1RphrIzWWzN7eMJb1EaGEgQM37fCaAFupUdk2P%2F3BaPHN%2Fnak9yTh7BLlvxBlILn%2BQlmcXRvUk9NvDWtM%2B0lnjodeDdh%2B7sr2gymcYXWY5zyZDQob2uSYyQFwCRmxf23%2BtLQhaz7j4XyJWs6Bw5YL0xjrmk1%2FVGF70neIyQvYZjMG3rpBMCKnM9s1R7wLEsEoNmqZvs2Weax%2FHomsH%2Fkok%2Blco7iL3BZ2bGvqvo11ZdaiBn2IP3pq%2FYRXMClugl6b%2BQuujW%2F2Cm%2FATlvLXqmDmoSOSCibE0arN8VKX%2FyjPoUtKyZakHN0FmoRQeZ1q4TE44yfNBapsTvDAhmQ%2B0B2rmV3G23w9beGMtnLhA%2FkzVYqJUk3%2BHKrcV9zsoPmpOEFhj2wDrKDcthrjM7vg5ZnyuBG5%2BeTD8uFxZVkaVe4%2BlSTwnPb6fLvH7JZRm3n6bkmHpj8Ua2b53SSRAkJJvrewZdo54dGnxvhbiVWccmBDakXKHvrak78cTc%2B40RisqQQHInXjzu8HR1e9bTFPFNrIf1HNbcskQz50RO%2B%2FRb8bnsAWoBEFztwg%2BwPmi3X7AW%2B6%2FVmOUzPPQPZdCAzMzC1hZ29BjqkAW%2Bg5wTOAUZFPiTT%2B35Nthv2NbVmuhZWUqJvVb2AV%2FZXvKLcy%2FS5V%2BPDcUQjCY%2FCjSnTLOXsl%2B9fa%2F%2F4djMfX48RmmY77j6i1FpOSCkGlaBivyei%2B4XfiCmSRWmfKpcm%2FhHVmde9qFfJJ9iOq2YZlocK9gFawW9lU%2F0qolSBqGFwkUF2GQ2Wvuok7nag2Xn9YYFlKJGPyVp2m0afmhpo31Hftpro&X-Amz-Signature=9d994e3ab3df9a61224dbb02198b62d0c76e671ece8b76fe3c6d764b1ffacc48&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663SYFKXAK%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQCO36PPiRGeWj67NjXoBu%2Fk8uDYenDILkstn6UMeEJBsQIgIYnZ0VERcEKFadVEx8wXBymFm3R%2BEUpXplw86Zb3DeEqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFjNnSS58GrJEOfh7SrcAyh8Bib07kQyn3BnH5D%2BrO8rIP8XLtZB6zaQpIM6uKMlk%2Fp8OrojjoN1vD92HtIVaMcgKTr5tJVRR6v%2Fer2M7fgxQBNaNpS2kM08rZfGiZG4mzF4pQYxktD4zz3oW7ULEwazH%2FrbIGSIFp5rkHjv3LEAfG9KEZ4rvFOmTNZ9VqiSXPU7j5qppM4g8KXXGK%2FwnLBN3gLIsYBqWp%2BgZnMAsjxH%2FxfZfIKQ3bI9cqUGs7UEHA%2Fm23kwfXUPXgAwLmjWJkEsNDf%2Fn1PlPZh97wxc6txsPO4BYrYB9ecm51JHkN%2BvNgxidU8ABjeQw4dUJgl0ofBGYq4w4h2z3TjtmpHw3rI1UlKKvjMrQb4Zj5lJ58y9Mas0ScXcm%2BFvHVXLpUGsahAM5rqOxXwnIWb4h9pS0F0HITnUufpWh87N6iFF1W46eCznOwhlKd6SYE81yqAFIO166jLQaGb3KMU11sCTCPLZMgjqhVKujhcV2R%2FmXZhoaxn7fAxwUlDrF9gbHxUbTWgsyBKHQ15O6OaHZkaJLKb9Xgcd7FphRJM%2FmGaUK5Y3X5HzC1AIR4AZGgO2Ig%2FIRt4I%2BdzPlGJMcp4CjkUpAEUnOt3ExQoXitEldY6E7V40FFbemaMFJr6wVUInMMCFnb0GOqUBFjjlr2%2FMvajYr0lJ%2BM3v0BPPHUXfR8mtuENTN8bF23caPfjDeCVQNvvns3fm3yTljeq0zh2w3FwZBs4KnHKzESU8kGxxS%2FRjZ9kBJle61aVMy1%2FtN7f4wlDwSleCAR2Mlqut%2F8WR8eoRytGiEMLytr5VpPSMxmvxpzeyxhAQAOZ%2FwYmhbZy07jYfje9VimyAE9kwWDTgdZpbz8M9BAfUatDwKiN%2F&X-Amz-Signature=932e8b26dc0a473ec81cf216cd4ec63ca3fbf1abb1f8dba8e30ea3de68c53407&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663SYFKXAK%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQCO36PPiRGeWj67NjXoBu%2Fk8uDYenDILkstn6UMeEJBsQIgIYnZ0VERcEKFadVEx8wXBymFm3R%2BEUpXplw86Zb3DeEqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFjNnSS58GrJEOfh7SrcAyh8Bib07kQyn3BnH5D%2BrO8rIP8XLtZB6zaQpIM6uKMlk%2Fp8OrojjoN1vD92HtIVaMcgKTr5tJVRR6v%2Fer2M7fgxQBNaNpS2kM08rZfGiZG4mzF4pQYxktD4zz3oW7ULEwazH%2FrbIGSIFp5rkHjv3LEAfG9KEZ4rvFOmTNZ9VqiSXPU7j5qppM4g8KXXGK%2FwnLBN3gLIsYBqWp%2BgZnMAsjxH%2FxfZfIKQ3bI9cqUGs7UEHA%2Fm23kwfXUPXgAwLmjWJkEsNDf%2Fn1PlPZh97wxc6txsPO4BYrYB9ecm51JHkN%2BvNgxidU8ABjeQw4dUJgl0ofBGYq4w4h2z3TjtmpHw3rI1UlKKvjMrQb4Zj5lJ58y9Mas0ScXcm%2BFvHVXLpUGsahAM5rqOxXwnIWb4h9pS0F0HITnUufpWh87N6iFF1W46eCznOwhlKd6SYE81yqAFIO166jLQaGb3KMU11sCTCPLZMgjqhVKujhcV2R%2FmXZhoaxn7fAxwUlDrF9gbHxUbTWgsyBKHQ15O6OaHZkaJLKb9Xgcd7FphRJM%2FmGaUK5Y3X5HzC1AIR4AZGgO2Ig%2FIRt4I%2BdzPlGJMcp4CjkUpAEUnOt3ExQoXitEldY6E7V40FFbemaMFJr6wVUInMMCFnb0GOqUBFjjlr2%2FMvajYr0lJ%2BM3v0BPPHUXfR8mtuENTN8bF23caPfjDeCVQNvvns3fm3yTljeq0zh2w3FwZBs4KnHKzESU8kGxxS%2FRjZ9kBJle61aVMy1%2FtN7f4wlDwSleCAR2Mlqut%2F8WR8eoRytGiEMLytr5VpPSMxmvxpzeyxhAQAOZ%2FwYmhbZy07jYfje9VimyAE9kwWDTgdZpbz8M9BAfUatDwKiN%2F&X-Amz-Signature=5c5f9bd784b77a4007b1a2bced23c8f2a943da9057fb6785a3e91d1bd7f537d5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663SYFKXAK%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQCO36PPiRGeWj67NjXoBu%2Fk8uDYenDILkstn6UMeEJBsQIgIYnZ0VERcEKFadVEx8wXBymFm3R%2BEUpXplw86Zb3DeEqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFjNnSS58GrJEOfh7SrcAyh8Bib07kQyn3BnH5D%2BrO8rIP8XLtZB6zaQpIM6uKMlk%2Fp8OrojjoN1vD92HtIVaMcgKTr5tJVRR6v%2Fer2M7fgxQBNaNpS2kM08rZfGiZG4mzF4pQYxktD4zz3oW7ULEwazH%2FrbIGSIFp5rkHjv3LEAfG9KEZ4rvFOmTNZ9VqiSXPU7j5qppM4g8KXXGK%2FwnLBN3gLIsYBqWp%2BgZnMAsjxH%2FxfZfIKQ3bI9cqUGs7UEHA%2Fm23kwfXUPXgAwLmjWJkEsNDf%2Fn1PlPZh97wxc6txsPO4BYrYB9ecm51JHkN%2BvNgxidU8ABjeQw4dUJgl0ofBGYq4w4h2z3TjtmpHw3rI1UlKKvjMrQb4Zj5lJ58y9Mas0ScXcm%2BFvHVXLpUGsahAM5rqOxXwnIWb4h9pS0F0HITnUufpWh87N6iFF1W46eCznOwhlKd6SYE81yqAFIO166jLQaGb3KMU11sCTCPLZMgjqhVKujhcV2R%2FmXZhoaxn7fAxwUlDrF9gbHxUbTWgsyBKHQ15O6OaHZkaJLKb9Xgcd7FphRJM%2FmGaUK5Y3X5HzC1AIR4AZGgO2Ig%2FIRt4I%2BdzPlGJMcp4CjkUpAEUnOt3ExQoXitEldY6E7V40FFbemaMFJr6wVUInMMCFnb0GOqUBFjjlr2%2FMvajYr0lJ%2BM3v0BPPHUXfR8mtuENTN8bF23caPfjDeCVQNvvns3fm3yTljeq0zh2w3FwZBs4KnHKzESU8kGxxS%2FRjZ9kBJle61aVMy1%2FtN7f4wlDwSleCAR2Mlqut%2F8WR8eoRytGiEMLytr5VpPSMxmvxpzeyxhAQAOZ%2FwYmhbZy07jYfje9VimyAE9kwWDTgdZpbz8M9BAfUatDwKiN%2F&X-Amz-Signature=b287f069b4961b88e252e87c36d9438dc8a8194fb82f555aa149183779a135c4&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663SYFKXAK%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQCO36PPiRGeWj67NjXoBu%2Fk8uDYenDILkstn6UMeEJBsQIgIYnZ0VERcEKFadVEx8wXBymFm3R%2BEUpXplw86Zb3DeEqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFjNnSS58GrJEOfh7SrcAyh8Bib07kQyn3BnH5D%2BrO8rIP8XLtZB6zaQpIM6uKMlk%2Fp8OrojjoN1vD92HtIVaMcgKTr5tJVRR6v%2Fer2M7fgxQBNaNpS2kM08rZfGiZG4mzF4pQYxktD4zz3oW7ULEwazH%2FrbIGSIFp5rkHjv3LEAfG9KEZ4rvFOmTNZ9VqiSXPU7j5qppM4g8KXXGK%2FwnLBN3gLIsYBqWp%2BgZnMAsjxH%2FxfZfIKQ3bI9cqUGs7UEHA%2Fm23kwfXUPXgAwLmjWJkEsNDf%2Fn1PlPZh97wxc6txsPO4BYrYB9ecm51JHkN%2BvNgxidU8ABjeQw4dUJgl0ofBGYq4w4h2z3TjtmpHw3rI1UlKKvjMrQb4Zj5lJ58y9Mas0ScXcm%2BFvHVXLpUGsahAM5rqOxXwnIWb4h9pS0F0HITnUufpWh87N6iFF1W46eCznOwhlKd6SYE81yqAFIO166jLQaGb3KMU11sCTCPLZMgjqhVKujhcV2R%2FmXZhoaxn7fAxwUlDrF9gbHxUbTWgsyBKHQ15O6OaHZkaJLKb9Xgcd7FphRJM%2FmGaUK5Y3X5HzC1AIR4AZGgO2Ig%2FIRt4I%2BdzPlGJMcp4CjkUpAEUnOt3ExQoXitEldY6E7V40FFbemaMFJr6wVUInMMCFnb0GOqUBFjjlr2%2FMvajYr0lJ%2BM3v0BPPHUXfR8mtuENTN8bF23caPfjDeCVQNvvns3fm3yTljeq0zh2w3FwZBs4KnHKzESU8kGxxS%2FRjZ9kBJle61aVMy1%2FtN7f4wlDwSleCAR2Mlqut%2F8WR8eoRytGiEMLytr5VpPSMxmvxpzeyxhAQAOZ%2FwYmhbZy07jYfje9VimyAE9kwWDTgdZpbz8M9BAfUatDwKiN%2F&X-Amz-Signature=c9bb38bb0644283258768ea249dc6bc0289661129e0b5d73ebec511447b5c2cf&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
