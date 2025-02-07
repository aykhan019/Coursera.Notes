

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V47CCKPD%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQDPIK9XTVx2NmfJf9QZeTR3whxvMF6phxrnmKltMv%2FEAgIgVKom8IZ032Ezvqn3UeEtoacN3e6cS9QDesIXC4R5U8gq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDNbCOHlHo6Pl8l1x4yrcA15XiPMwb%2Be8O3Sl3oiup4KGhIC8%2F8ULuZntEJTISYm7C%2FRoez%2BdCvLefu4JGbmBxA%2Fq%2Fabr9%2FTruN%2FHszsLrX8YdgxPzifclZ6iiWUZ4iT7kJbOr87j%2Bq84UoVIEGD177fSgMaNJlsx4cQeBVczTB%2FpYlwbXr7jZWq6KYXYD%2FUm%2BoWQ4EdEdoeexEB4EQ5C6hKO02lLUcUkgAwIhQFbRGE6dkwaEZ7ymxVvcOx0gG14fb8kIawv66XKDntjhX3P5JvfpNdKqFz8uTc2V2rwn2eSk7pM%2BGv5mNVhMHYiwfUD45r7uflnV3WbUpUB2P4uF8Z5uH1Xcqal2OmJ6ggD6dKArof2Jv3Jhf6AwVe2QN7MMaAA0IImtg8zbK1xdPrPki8H8w9IFyiSkSP3W0r0RIv9OVDuB628HNXo2mGIDvpvKCEKhFWdUN8OkefFsIrnz6iDrlydMHWTcOIb4rNfLQ%2B19ObYtMqfPehT5bzOFT00GK6K1H51Bz%2BINMdRVoxd0wdOsdv2Lgwlu3wv0t1PH8Bg61tmr3MBrqaKddphsyctq%2BswMtTAJQF1ppJTo1Yb3DUV%2Bbctd0zPNjXeADX0jVT1CRVNDghAf9p2MpEElqrRZL%2BvzB5VZAWQhZzlMP%2F5lr0GOqUB4njSBhoBzMC102obVDdBhoBiCqzCi5lY9yJG3ERYI2EUTXwvQwK3MoOHmY27Cm48Wc1RdGcRyiSGgWX2ogMUwTRzXb7Jw7HD0jbSnIw%2B1zjumJ%2BYNHf%2F6fYknIteLQn%2BKDInGJDaSOUWQq7B%2FjdqdqKlI5Yt%2FYxYx02TLy9kip4XGRwSKY%2B1152pBtEjAEBUK9AwbY%2FtrKcJ6BXQToUSB6pZ2QoU&X-Amz-Signature=10f6fbae72bcb62fdcf57dbbe2141b16a0b4d1b501a8b4da380a713c968e69c9&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V47CCKPD%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQDPIK9XTVx2NmfJf9QZeTR3whxvMF6phxrnmKltMv%2FEAgIgVKom8IZ032Ezvqn3UeEtoacN3e6cS9QDesIXC4R5U8gq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDNbCOHlHo6Pl8l1x4yrcA15XiPMwb%2Be8O3Sl3oiup4KGhIC8%2F8ULuZntEJTISYm7C%2FRoez%2BdCvLefu4JGbmBxA%2Fq%2Fabr9%2FTruN%2FHszsLrX8YdgxPzifclZ6iiWUZ4iT7kJbOr87j%2Bq84UoVIEGD177fSgMaNJlsx4cQeBVczTB%2FpYlwbXr7jZWq6KYXYD%2FUm%2BoWQ4EdEdoeexEB4EQ5C6hKO02lLUcUkgAwIhQFbRGE6dkwaEZ7ymxVvcOx0gG14fb8kIawv66XKDntjhX3P5JvfpNdKqFz8uTc2V2rwn2eSk7pM%2BGv5mNVhMHYiwfUD45r7uflnV3WbUpUB2P4uF8Z5uH1Xcqal2OmJ6ggD6dKArof2Jv3Jhf6AwVe2QN7MMaAA0IImtg8zbK1xdPrPki8H8w9IFyiSkSP3W0r0RIv9OVDuB628HNXo2mGIDvpvKCEKhFWdUN8OkefFsIrnz6iDrlydMHWTcOIb4rNfLQ%2B19ObYtMqfPehT5bzOFT00GK6K1H51Bz%2BINMdRVoxd0wdOsdv2Lgwlu3wv0t1PH8Bg61tmr3MBrqaKddphsyctq%2BswMtTAJQF1ppJTo1Yb3DUV%2Bbctd0zPNjXeADX0jVT1CRVNDghAf9p2MpEElqrRZL%2BvzB5VZAWQhZzlMP%2F5lr0GOqUB4njSBhoBzMC102obVDdBhoBiCqzCi5lY9yJG3ERYI2EUTXwvQwK3MoOHmY27Cm48Wc1RdGcRyiSGgWX2ogMUwTRzXb7Jw7HD0jbSnIw%2B1zjumJ%2BYNHf%2F6fYknIteLQn%2BKDInGJDaSOUWQq7B%2FjdqdqKlI5Yt%2FYxYx02TLy9kip4XGRwSKY%2B1152pBtEjAEBUK9AwbY%2FtrKcJ6BXQToUSB6pZ2QoU&X-Amz-Signature=3f730f7ca5cc07bbeb07a052f4876591731ccf34fd7c5fdacee4f966404e3046&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V47CCKPD%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQDPIK9XTVx2NmfJf9QZeTR3whxvMF6phxrnmKltMv%2FEAgIgVKom8IZ032Ezvqn3UeEtoacN3e6cS9QDesIXC4R5U8gq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDNbCOHlHo6Pl8l1x4yrcA15XiPMwb%2Be8O3Sl3oiup4KGhIC8%2F8ULuZntEJTISYm7C%2FRoez%2BdCvLefu4JGbmBxA%2Fq%2Fabr9%2FTruN%2FHszsLrX8YdgxPzifclZ6iiWUZ4iT7kJbOr87j%2Bq84UoVIEGD177fSgMaNJlsx4cQeBVczTB%2FpYlwbXr7jZWq6KYXYD%2FUm%2BoWQ4EdEdoeexEB4EQ5C6hKO02lLUcUkgAwIhQFbRGE6dkwaEZ7ymxVvcOx0gG14fb8kIawv66XKDntjhX3P5JvfpNdKqFz8uTc2V2rwn2eSk7pM%2BGv5mNVhMHYiwfUD45r7uflnV3WbUpUB2P4uF8Z5uH1Xcqal2OmJ6ggD6dKArof2Jv3Jhf6AwVe2QN7MMaAA0IImtg8zbK1xdPrPki8H8w9IFyiSkSP3W0r0RIv9OVDuB628HNXo2mGIDvpvKCEKhFWdUN8OkefFsIrnz6iDrlydMHWTcOIb4rNfLQ%2B19ObYtMqfPehT5bzOFT00GK6K1H51Bz%2BINMdRVoxd0wdOsdv2Lgwlu3wv0t1PH8Bg61tmr3MBrqaKddphsyctq%2BswMtTAJQF1ppJTo1Yb3DUV%2Bbctd0zPNjXeADX0jVT1CRVNDghAf9p2MpEElqrRZL%2BvzB5VZAWQhZzlMP%2F5lr0GOqUB4njSBhoBzMC102obVDdBhoBiCqzCi5lY9yJG3ERYI2EUTXwvQwK3MoOHmY27Cm48Wc1RdGcRyiSGgWX2ogMUwTRzXb7Jw7HD0jbSnIw%2B1zjumJ%2BYNHf%2F6fYknIteLQn%2BKDInGJDaSOUWQq7B%2FjdqdqKlI5Yt%2FYxYx02TLy9kip4XGRwSKY%2B1152pBtEjAEBUK9AwbY%2FtrKcJ6BXQToUSB6pZ2QoU&X-Amz-Signature=ac69b3b0b7769cbd46bee99d12a1859d4ef948ee58078ca867d7ed26d89ed5d3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UO53AZOG%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCID05dsrfKoQ3PhLspZoYIAVYA9rKbHx06ccVMGZ09nvPAiAKVjfx%2FoNBgEgSJWc0W8p8QXpI7vMQG3CksgOk3Xz%2Ftir%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIMMJFBUxAlTjgXyWF4KtwDGvMq3KWpui9CCQtNR5J5JUKbyyd%2FGaCN6PsCD3JRkoo7OEBCCkCnpSD2H5tDjWxbCIO1Qp7Few2qR8LYL98yIN26hFgj%2FRisZM0LlF5GkjnTE1%2BFuXfAZ19i4l2jqGUWvWCV09lYF0n4VvcVLbEiQjLn8Gx3iJO4rOtQKcEqW2tYiI2qlHmUnn6DptlANwuAv%2FNwIok39ET7B5NUmf4WhP5V5auiuyUfEMXufDJwrlz5l8zdwBYlaF%2FzhzlvkuuoW2llChHwHPDrmlKBrTE7Urpgt%2BuifRMOatKVHsm0Dahfc2%2FVv8%2F4NQn9EBiXRS7RTwRwVqXAHKnQLojYgwPWTXQLS%2FdKSl9ssHbuhpE9WhWvT0y2q9aCcvV7RnhxQ0Gyyotrz7E31xsTyxe3abm8SCJHu6FIP5XoHx1n%2BQnU64DXBKTZ5DK06xETRphDEkhteYxR7j1LhN0hcn05scG5icVGOyl4azbqvewCG3PonpVGnEZPYpeJtTerZU9MmXNDsJiQ%2BLg%2BNnhnW2xLya5k213R55Q%2BuTusnPHSFfkEE%2BraInGS4MkRLQKu5AoBu85TGxubMvlF9tjJBISeAYLfpPPAniehes2Jdc8wZtEA1jOlKuPp2kzJUwOEhCEwzfmWvQY6pgGDMBDpRPng%2FwZ1jthQfDSa5wnOfBTFFspC8phxUkMNVHjZSSZ5W49EalXxNndtV%2FOgWM5woliuX2LPtQVQT4MhrQ%2FPS1HPAiLDho7oFp0FAQQ%2FV825oBxk3wquRsfVFzWsQ6zR0Z8LuygCk18GEX0NTXAgqgK48zXNA0%2Fe4SZEBlT5j4f0Ok0fMoRDK9JZ197MzOSt1ajzsDyj1NNjzwL6zTqYKedl&X-Amz-Signature=540bf30979bce552a08b11c2c3bbeed6255b1b1355bb6d2b81524af43c4cc0a0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TXGFJ3KS%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIF8t1Jp5UYubcXy0uS%2FJ1vF1EaHxEdfUFfZSnDtwsf1bAiEA5LFMwaAKBIQ%2BORIqtqJo7de%2Fk%2F72nl7NnQ2nlOdzPkAq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDLRxz%2BGktj%2BvL3kLHCrcA21VA5ZAFPiQtZu%2FqTA4%2BRdQva4lwx1u23u8eNIGu5i7Z%2FJ2mDHFmmJgeDAo0OohjNN8C5nwEPeVWI7EogFVGlIwCxLB5wiZwZbCnyOKuAuE9CHGQXxCQCRYMZ78FPF3DjmphcBHFPEAv03U0hGnNUEyjRHPWG4G29Sb31u%2FpMweJGHqFr9Nk%2BC9n%2BSdyC9cic0b%2FudClcJ2kq3pHC%2Fv%2FTmbV0bgl2KRQVw1vHVQEbwsN%2B1S9oEfxNi7pzLECEyduIk%2FVlDA25Z4W7x5xNUOFG8hnyOdiLSHQgmZFv5uUiOHs68j6TX%2B6fnE9sUKhvpMPiFbKCLtPhh8Cu3MbIuA8rpWvAmYRu2kXiB0VgCjuJKMrtxjIdNukDQvjDVr22pgv4UgT%2FGHhNy4Gva7jUFyV6i1SxbrZpNsjyMrCu3CIuFCU4QRdS3MSVpHfSiYV3y5dHr1ZG9R4pYSt6f%2FV7hMpjus0wMuptfFY60omg%2BjL3%2Fxm7hNc4Fr%2F%2BMdz6PATlwE0PqqHoyunAlJ1p8H4uUURTMy5lYIEfNuiCbxh0OBcWpE4tFBjNZxm8DYO%2FruqCdTia7EHKYIcYply6pPT%2Bmw5sfM06FieWAmBnGlR%2Fqne6il%2BdqCCOpGbRfbtujzMMX5lr0GOqUByVO%2BHkqkMGBhQPa2%2BrASOHlsly6wNEm0uASYOWxisPQOBVMKaCUmd1wCeyZ13y1T9xSSk4VcG1q4K3VVkGvsTK%2FJOyhAey8%2BoeBiljMNub3M3V3S8uIUlcONJfSnanbHvycp9ZYzjF4KtxHuEfNCQG6myXMJQxOqSlSCoKY4TlqbjtkExucG%2FDoPiNyKC%2Bi285qiMGm4sYaRjoHpzVM6mTVzWvNX&X-Amz-Signature=3e45fc844da4e34e226ebb6736baebc55e87569abcfc97bfe04975fb7ce45230&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V47CCKPD%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQDPIK9XTVx2NmfJf9QZeTR3whxvMF6phxrnmKltMv%2FEAgIgVKom8IZ032Ezvqn3UeEtoacN3e6cS9QDesIXC4R5U8gq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDNbCOHlHo6Pl8l1x4yrcA15XiPMwb%2Be8O3Sl3oiup4KGhIC8%2F8ULuZntEJTISYm7C%2FRoez%2BdCvLefu4JGbmBxA%2Fq%2Fabr9%2FTruN%2FHszsLrX8YdgxPzifclZ6iiWUZ4iT7kJbOr87j%2Bq84UoVIEGD177fSgMaNJlsx4cQeBVczTB%2FpYlwbXr7jZWq6KYXYD%2FUm%2BoWQ4EdEdoeexEB4EQ5C6hKO02lLUcUkgAwIhQFbRGE6dkwaEZ7ymxVvcOx0gG14fb8kIawv66XKDntjhX3P5JvfpNdKqFz8uTc2V2rwn2eSk7pM%2BGv5mNVhMHYiwfUD45r7uflnV3WbUpUB2P4uF8Z5uH1Xcqal2OmJ6ggD6dKArof2Jv3Jhf6AwVe2QN7MMaAA0IImtg8zbK1xdPrPki8H8w9IFyiSkSP3W0r0RIv9OVDuB628HNXo2mGIDvpvKCEKhFWdUN8OkefFsIrnz6iDrlydMHWTcOIb4rNfLQ%2B19ObYtMqfPehT5bzOFT00GK6K1H51Bz%2BINMdRVoxd0wdOsdv2Lgwlu3wv0t1PH8Bg61tmr3MBrqaKddphsyctq%2BswMtTAJQF1ppJTo1Yb3DUV%2Bbctd0zPNjXeADX0jVT1CRVNDghAf9p2MpEElqrRZL%2BvzB5VZAWQhZzlMP%2F5lr0GOqUB4njSBhoBzMC102obVDdBhoBiCqzCi5lY9yJG3ERYI2EUTXwvQwK3MoOHmY27Cm48Wc1RdGcRyiSGgWX2ogMUwTRzXb7Jw7HD0jbSnIw%2B1zjumJ%2BYNHf%2F6fYknIteLQn%2BKDInGJDaSOUWQq7B%2FjdqdqKlI5Yt%2FYxYx02TLy9kip4XGRwSKY%2B1152pBtEjAEBUK9AwbY%2FtrKcJ6BXQToUSB6pZ2QoU&X-Amz-Signature=240ba7ada6b07c17a0ee6353107eac3941a98c1a2de0d079f08225db1d28b65e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V47CCKPD%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQDPIK9XTVx2NmfJf9QZeTR3whxvMF6phxrnmKltMv%2FEAgIgVKom8IZ032Ezvqn3UeEtoacN3e6cS9QDesIXC4R5U8gq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDNbCOHlHo6Pl8l1x4yrcA15XiPMwb%2Be8O3Sl3oiup4KGhIC8%2F8ULuZntEJTISYm7C%2FRoez%2BdCvLefu4JGbmBxA%2Fq%2Fabr9%2FTruN%2FHszsLrX8YdgxPzifclZ6iiWUZ4iT7kJbOr87j%2Bq84UoVIEGD177fSgMaNJlsx4cQeBVczTB%2FpYlwbXr7jZWq6KYXYD%2FUm%2BoWQ4EdEdoeexEB4EQ5C6hKO02lLUcUkgAwIhQFbRGE6dkwaEZ7ymxVvcOx0gG14fb8kIawv66XKDntjhX3P5JvfpNdKqFz8uTc2V2rwn2eSk7pM%2BGv5mNVhMHYiwfUD45r7uflnV3WbUpUB2P4uF8Z5uH1Xcqal2OmJ6ggD6dKArof2Jv3Jhf6AwVe2QN7MMaAA0IImtg8zbK1xdPrPki8H8w9IFyiSkSP3W0r0RIv9OVDuB628HNXo2mGIDvpvKCEKhFWdUN8OkefFsIrnz6iDrlydMHWTcOIb4rNfLQ%2B19ObYtMqfPehT5bzOFT00GK6K1H51Bz%2BINMdRVoxd0wdOsdv2Lgwlu3wv0t1PH8Bg61tmr3MBrqaKddphsyctq%2BswMtTAJQF1ppJTo1Yb3DUV%2Bbctd0zPNjXeADX0jVT1CRVNDghAf9p2MpEElqrRZL%2BvzB5VZAWQhZzlMP%2F5lr0GOqUB4njSBhoBzMC102obVDdBhoBiCqzCi5lY9yJG3ERYI2EUTXwvQwK3MoOHmY27Cm48Wc1RdGcRyiSGgWX2ogMUwTRzXb7Jw7HD0jbSnIw%2B1zjumJ%2BYNHf%2F6fYknIteLQn%2BKDInGJDaSOUWQq7B%2FjdqdqKlI5Yt%2FYxYx02TLy9kip4XGRwSKY%2B1152pBtEjAEBUK9AwbY%2FtrKcJ6BXQToUSB6pZ2QoU&X-Amz-Signature=e21819722c8eb5baa34d236d36cb60cb8614dcbbe88ab6ebd5896196599ed005&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V47CCKPD%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQDPIK9XTVx2NmfJf9QZeTR3whxvMF6phxrnmKltMv%2FEAgIgVKom8IZ032Ezvqn3UeEtoacN3e6cS9QDesIXC4R5U8gq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDNbCOHlHo6Pl8l1x4yrcA15XiPMwb%2Be8O3Sl3oiup4KGhIC8%2F8ULuZntEJTISYm7C%2FRoez%2BdCvLefu4JGbmBxA%2Fq%2Fabr9%2FTruN%2FHszsLrX8YdgxPzifclZ6iiWUZ4iT7kJbOr87j%2Bq84UoVIEGD177fSgMaNJlsx4cQeBVczTB%2FpYlwbXr7jZWq6KYXYD%2FUm%2BoWQ4EdEdoeexEB4EQ5C6hKO02lLUcUkgAwIhQFbRGE6dkwaEZ7ymxVvcOx0gG14fb8kIawv66XKDntjhX3P5JvfpNdKqFz8uTc2V2rwn2eSk7pM%2BGv5mNVhMHYiwfUD45r7uflnV3WbUpUB2P4uF8Z5uH1Xcqal2OmJ6ggD6dKArof2Jv3Jhf6AwVe2QN7MMaAA0IImtg8zbK1xdPrPki8H8w9IFyiSkSP3W0r0RIv9OVDuB628HNXo2mGIDvpvKCEKhFWdUN8OkefFsIrnz6iDrlydMHWTcOIb4rNfLQ%2B19ObYtMqfPehT5bzOFT00GK6K1H51Bz%2BINMdRVoxd0wdOsdv2Lgwlu3wv0t1PH8Bg61tmr3MBrqaKddphsyctq%2BswMtTAJQF1ppJTo1Yb3DUV%2Bbctd0zPNjXeADX0jVT1CRVNDghAf9p2MpEElqrRZL%2BvzB5VZAWQhZzlMP%2F5lr0GOqUB4njSBhoBzMC102obVDdBhoBiCqzCi5lY9yJG3ERYI2EUTXwvQwK3MoOHmY27Cm48Wc1RdGcRyiSGgWX2ogMUwTRzXb7Jw7HD0jbSnIw%2B1zjumJ%2BYNHf%2F6fYknIteLQn%2BKDInGJDaSOUWQq7B%2FjdqdqKlI5Yt%2FYxYx02TLy9kip4XGRwSKY%2B1152pBtEjAEBUK9AwbY%2FtrKcJ6BXQToUSB6pZ2QoU&X-Amz-Signature=bd080d06f8ba79c71773740d1e3aa2aea1944fa7d2aa8df40e83265b4b061eb6&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V47CCKPD%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQDPIK9XTVx2NmfJf9QZeTR3whxvMF6phxrnmKltMv%2FEAgIgVKom8IZ032Ezvqn3UeEtoacN3e6cS9QDesIXC4R5U8gq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDNbCOHlHo6Pl8l1x4yrcA15XiPMwb%2Be8O3Sl3oiup4KGhIC8%2F8ULuZntEJTISYm7C%2FRoez%2BdCvLefu4JGbmBxA%2Fq%2Fabr9%2FTruN%2FHszsLrX8YdgxPzifclZ6iiWUZ4iT7kJbOr87j%2Bq84UoVIEGD177fSgMaNJlsx4cQeBVczTB%2FpYlwbXr7jZWq6KYXYD%2FUm%2BoWQ4EdEdoeexEB4EQ5C6hKO02lLUcUkgAwIhQFbRGE6dkwaEZ7ymxVvcOx0gG14fb8kIawv66XKDntjhX3P5JvfpNdKqFz8uTc2V2rwn2eSk7pM%2BGv5mNVhMHYiwfUD45r7uflnV3WbUpUB2P4uF8Z5uH1Xcqal2OmJ6ggD6dKArof2Jv3Jhf6AwVe2QN7MMaAA0IImtg8zbK1xdPrPki8H8w9IFyiSkSP3W0r0RIv9OVDuB628HNXo2mGIDvpvKCEKhFWdUN8OkefFsIrnz6iDrlydMHWTcOIb4rNfLQ%2B19ObYtMqfPehT5bzOFT00GK6K1H51Bz%2BINMdRVoxd0wdOsdv2Lgwlu3wv0t1PH8Bg61tmr3MBrqaKddphsyctq%2BswMtTAJQF1ppJTo1Yb3DUV%2Bbctd0zPNjXeADX0jVT1CRVNDghAf9p2MpEElqrRZL%2BvzB5VZAWQhZzlMP%2F5lr0GOqUB4njSBhoBzMC102obVDdBhoBiCqzCi5lY9yJG3ERYI2EUTXwvQwK3MoOHmY27Cm48Wc1RdGcRyiSGgWX2ogMUwTRzXb7Jw7HD0jbSnIw%2B1zjumJ%2BYNHf%2F6fYknIteLQn%2BKDInGJDaSOUWQq7B%2FjdqdqKlI5Yt%2FYxYx02TLy9kip4XGRwSKY%2B1152pBtEjAEBUK9AwbY%2FtrKcJ6BXQToUSB6pZ2QoU&X-Amz-Signature=e058fe5dd3b8d2d5ddd63d219238ab4ce0d0831e8fe7cf1fcd0d0c48f2d041bd&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
