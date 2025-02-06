

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBX6U5F7%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJGMEQCIApxozpMJVcMd9CLfoB4G83w6cO4twwzIAvI5xo%2FG7Y9AiAW04Smk86ux7QoQM%2BcsOI7ZZlr2%2F2eMuNRrz9wOg1tSyr%2FAwhgEAAaDDYzNzQyMzE4MzgwNSIMp6uYVX4fJrKz%2BmNYKtwDq9tYfBgpZanEFbkqBCSrFeFClHqmAljV0yHJSs1Pz95Lqg5N7%2BjsTmbaYl2voXjR%2Fw5XL7Ec4ez%2BJOllsavUSgQET2AAASfY%2BM6nx%2B7KzErW4AZAmEd48qdJlAfgOfjsSfTAEOnUs1UuW1gbgI0kBh6k9cfjDj9Qdg%2FkW3kLWZu%2Fbg4AzIxiqb%2BbN3LXOhQo%2FVwjrhF%2BSvi2y3hkMiihYe8oFIReKVNMptACBBg2ydmgKXoDOjuVCMww3eMyQfvnO8dlRL7%2FSs%2Fw09WaUcCy88F55Z6eb9qOHN%2BPN9Z%2BOc5axlr%2BHgLpUDUauOSFFLCQ9BUHFwu8KMatBcSL92T%2BjPjE4nvdL3nPg1GMTpR1R30GkSXTgw7GcZn3bKMq2yB9cAbSIpePS7Cn7b494Lp1YsxIlg7Rf79aColZQor2rs9qKwX0vfhXl6Omum%2BA23BtzhYDykoDZ55JZBsZicJE3t7IN3qYfAhKJmTypvQi49X%2BDftLWjR5Vj146gWjtnV2lKSmgYlMX4CTEnL9tAUB%2FRpEsb6XSb5rhcg9tESxc1YSKYl%2BRpCbwc34SUwp2VGPZUrf%2BrdUXGLRO6pnaMTLlh3%2FJLEfIatjVbnICIogOLrb3vz0a02rP2NwpxQw7ZuTvQY6pgHATv1iBNKagym5Tqi6%2F8EG0%2BrPSmTYSlzpdwNBzBIVxcCP%2FKMpHtO4eNTRaAFzETqVlgA8oLqmOV9TmpaIGVEbr%2B1Pg54q%2B8J90MBBkCk8WSqtqy8TUbeF4J1%2BrdPXGyZ%2FxOgDBN6PiCMi0Ehfxskzcnlop9ej0vUF6SWJ8BM2YbHVEKAFRTuBskVMlA1MApalr8YkXWXcXY3cVP4iANFdVL8kYY6j&X-Amz-Signature=18ed80dcbb01dac23fd1b543dde501cbab0f4abd10e43b85ad76ac78cda8a399&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBX6U5F7%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJGMEQCIApxozpMJVcMd9CLfoB4G83w6cO4twwzIAvI5xo%2FG7Y9AiAW04Smk86ux7QoQM%2BcsOI7ZZlr2%2F2eMuNRrz9wOg1tSyr%2FAwhgEAAaDDYzNzQyMzE4MzgwNSIMp6uYVX4fJrKz%2BmNYKtwDq9tYfBgpZanEFbkqBCSrFeFClHqmAljV0yHJSs1Pz95Lqg5N7%2BjsTmbaYl2voXjR%2Fw5XL7Ec4ez%2BJOllsavUSgQET2AAASfY%2BM6nx%2B7KzErW4AZAmEd48qdJlAfgOfjsSfTAEOnUs1UuW1gbgI0kBh6k9cfjDj9Qdg%2FkW3kLWZu%2Fbg4AzIxiqb%2BbN3LXOhQo%2FVwjrhF%2BSvi2y3hkMiihYe8oFIReKVNMptACBBg2ydmgKXoDOjuVCMww3eMyQfvnO8dlRL7%2FSs%2Fw09WaUcCy88F55Z6eb9qOHN%2BPN9Z%2BOc5axlr%2BHgLpUDUauOSFFLCQ9BUHFwu8KMatBcSL92T%2BjPjE4nvdL3nPg1GMTpR1R30GkSXTgw7GcZn3bKMq2yB9cAbSIpePS7Cn7b494Lp1YsxIlg7Rf79aColZQor2rs9qKwX0vfhXl6Omum%2BA23BtzhYDykoDZ55JZBsZicJE3t7IN3qYfAhKJmTypvQi49X%2BDftLWjR5Vj146gWjtnV2lKSmgYlMX4CTEnL9tAUB%2FRpEsb6XSb5rhcg9tESxc1YSKYl%2BRpCbwc34SUwp2VGPZUrf%2BrdUXGLRO6pnaMTLlh3%2FJLEfIatjVbnICIogOLrb3vz0a02rP2NwpxQw7ZuTvQY6pgHATv1iBNKagym5Tqi6%2F8EG0%2BrPSmTYSlzpdwNBzBIVxcCP%2FKMpHtO4eNTRaAFzETqVlgA8oLqmOV9TmpaIGVEbr%2B1Pg54q%2B8J90MBBkCk8WSqtqy8TUbeF4J1%2BrdPXGyZ%2FxOgDBN6PiCMi0Ehfxskzcnlop9ej0vUF6SWJ8BM2YbHVEKAFRTuBskVMlA1MApalr8YkXWXcXY3cVP4iANFdVL8kYY6j&X-Amz-Signature=44358e7cf5304a63b6eed4053061080dd1d902b7f92e8ad4522a0caa466ee828&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBX6U5F7%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJGMEQCIApxozpMJVcMd9CLfoB4G83w6cO4twwzIAvI5xo%2FG7Y9AiAW04Smk86ux7QoQM%2BcsOI7ZZlr2%2F2eMuNRrz9wOg1tSyr%2FAwhgEAAaDDYzNzQyMzE4MzgwNSIMp6uYVX4fJrKz%2BmNYKtwDq9tYfBgpZanEFbkqBCSrFeFClHqmAljV0yHJSs1Pz95Lqg5N7%2BjsTmbaYl2voXjR%2Fw5XL7Ec4ez%2BJOllsavUSgQET2AAASfY%2BM6nx%2B7KzErW4AZAmEd48qdJlAfgOfjsSfTAEOnUs1UuW1gbgI0kBh6k9cfjDj9Qdg%2FkW3kLWZu%2Fbg4AzIxiqb%2BbN3LXOhQo%2FVwjrhF%2BSvi2y3hkMiihYe8oFIReKVNMptACBBg2ydmgKXoDOjuVCMww3eMyQfvnO8dlRL7%2FSs%2Fw09WaUcCy88F55Z6eb9qOHN%2BPN9Z%2BOc5axlr%2BHgLpUDUauOSFFLCQ9BUHFwu8KMatBcSL92T%2BjPjE4nvdL3nPg1GMTpR1R30GkSXTgw7GcZn3bKMq2yB9cAbSIpePS7Cn7b494Lp1YsxIlg7Rf79aColZQor2rs9qKwX0vfhXl6Omum%2BA23BtzhYDykoDZ55JZBsZicJE3t7IN3qYfAhKJmTypvQi49X%2BDftLWjR5Vj146gWjtnV2lKSmgYlMX4CTEnL9tAUB%2FRpEsb6XSb5rhcg9tESxc1YSKYl%2BRpCbwc34SUwp2VGPZUrf%2BrdUXGLRO6pnaMTLlh3%2FJLEfIatjVbnICIogOLrb3vz0a02rP2NwpxQw7ZuTvQY6pgHATv1iBNKagym5Tqi6%2F8EG0%2BrPSmTYSlzpdwNBzBIVxcCP%2FKMpHtO4eNTRaAFzETqVlgA8oLqmOV9TmpaIGVEbr%2B1Pg54q%2B8J90MBBkCk8WSqtqy8TUbeF4J1%2BrdPXGyZ%2FxOgDBN6PiCMi0Ehfxskzcnlop9ej0vUF6SWJ8BM2YbHVEKAFRTuBskVMlA1MApalr8YkXWXcXY3cVP4iANFdVL8kYY6j&X-Amz-Signature=93417ba10bb5cc21d37571221942b7358a0b4cd1d70118f11b83bf3e9c5ba183&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VBYE5BOX%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJGMEQCIGFFkapiaTn0iYHFw9uhaA2g4EoiOgRM5xHnUY%2BqJIrzAiBUbO45gOXAojA7KXR%2BrdgtPVshLpW69XThTGaumW2t6ir%2FAwhgEAAaDDYzNzQyMzE4MzgwNSIM5k0GUAuMYmv38p0NKtwDSPKs18QyjiCULJeBluNV%2BHYz3I3QOZmAvCj4aRKXLNxwbo2y3D1TSDx9cFB%2BSDgKgRgvvf8XuZ4w%2FEBDkL%2BkuOkdKgGJuCF6D5QhsNNxdd5hY9eYfJiHq1UrKOI30MKQr%2F%2BElbPPIid5FotVHomd%2FtfcXZIaw1uqVjThMs15bSeDcB8Or1jHEi5R7wwyotLrojXAeH%2FQBLMwO3n2IMgStZY%2FlFJMbLuxNtZpbCaakaW1GQpTZzIIyB3XeBWRDZxTrZidCVUA2RB7XkmdbBE2VCLvTIumHakzP5KJ0FxgXuQwIMrau6jVzYV2Y9zCLTpzb8JlKEqilZ%2BXRmOUr0kp40pSfOfEO4KTXjurp%2BepVOBHPoZTicCT8trc9zvearFXIqahxQtXqxK%2FoYjt2o9N%2FPDiZSM9wQAAVx95As8OkEMV0ahcppFkf8FVAk9vD6S5Nd9cgzNTEqc9MyER7SxQol%2FmloRATw6pA5BozeBnm3GMrSn%2BZ58UpChnLK%2BSlT%2FLro4tUZdySRnms8DxWK2CN5v%2BYxfhKrTXqK6%2Fecu5anPi0Wnpn1JZFe2EcZWURaJxU9bAnqWxybf98YyamFivlPvDwRopmCB0GWa%2FDQbPkGB%2FKPVLPLDZifQrAYYwmJyTvQY6pgEKWmLwOOHerk0HeQMhG4G%2F9Eqoa%2BsVPqJ8SkcZyvFqugWqTpavylZnUn5gRJR%2BVO0Lq3yvxTay3Bbxu7Dmt6WoQ7wumM2U04o9nbafYmtPtB2ifzcOKx1gWixN8sT66uxkSdA0MbxV7035BrAXBH5o36HOPZiAZeqfIgQZvLlOC1pZAnu4EC9%2F0%2F8uFPe20%2BTazAoy71keNN9A6kVDeV8Xwtlg7xM5&X-Amz-Signature=de21170e5c3af1751275e2fb69b9c62fc4a58087f8d89de1bc2ddc804907dcf2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664H5GQWN5%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIQD0K%2BFHz6%2BYUCjWkZRsfEW0Xiw2SGAnWfRRRNDBOJo7OQIgfwznIdHZLN%2FtcaoKSzpuo8nJA4%2Fs8yJ6kw5LIw%2Frh0wq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDAs%2BZ6zdy57k7CdHMCrcA3d%2BSOjz409KPatlnIDP9Yz6WI4mLiJOrBShey5t%2BLIaranZ5%2FDQFhm0JoZQ7svWyluX%2BH%2FljJYfIqTeRFQIgXNmvihDcgfNLCHMlvBTUpPwRcHrhxmia32oVR987ltqwDOOdg%2BfO35dylVIJ%2FPVrsUe%2BaPFfO9a8cBcClwYB98qL07Po8oSR2n2v5BPz21E8LGuzcPEssTumbkergEclBOJ0h3kdZHul0YAni1bd0zqKyGPHwbfd%2Fkh5R7AI0cbSv6e1L1PH5FcF%2B5LrO%2BRH4R6MoJHfdM38P8%2FPXPZ24NM19iVXGn1uWSv4NXnGIl3jZWJkeTdKODzhlaT8OvUHbrGlKYe8g2mWXfNRSbrkN3OWNljYSCA3LQB7U6vEcWgVvApqdKVY5G%2BtiUa246pmWO8DiCFtNlbgNcWNdLRsCoW57qw3JMVVkY5OmlS0ZE4SbLnW5KlRlXhG0bY7Qsdx0XnYMDrjcvCesKCECLrUFXPLHGaGBUsOAQAQW%2FzWV0JS%2BwHBacnfrshXOqasBE88ZqJOraDB6Ev6kpLn%2BJ2E8InKG9jtqIaHxeEdtpVAwwsJVq%2FIl22Y%2Fdh3bU%2FGz2ykPYFb8VYLabEpGsFb0CekrmQxIZcnfMJnH0E%2F23GMPabk70GOqUBEmNQw88%2BoMDxgQ7etZOi6HAkGsNdsLUB0rgSYf46Qx1Rz9gVrdyVSCk%2FmGUBFU47j9AQBjCN2D6TzL12IHX5nB27SDMnxIFlBYY1XbpgfcHRZLnOnbnBG6HQ6UNWVwz%2B57arYgbGbM6WhV%2Bmhyl%2BD1M5ZCEgng%2FZBv0U7FlWuktAsfjtCX3SIUwUAL%2FmyeK1nDcQse18z96CC4DOT5EEod5Bh9j5&X-Amz-Signature=c33f710a5fa89b5ab89bb0d3c4f37174f7f801689d652b029076e5981cf539da&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBX6U5F7%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJGMEQCIApxozpMJVcMd9CLfoB4G83w6cO4twwzIAvI5xo%2FG7Y9AiAW04Smk86ux7QoQM%2BcsOI7ZZlr2%2F2eMuNRrz9wOg1tSyr%2FAwhgEAAaDDYzNzQyMzE4MzgwNSIMp6uYVX4fJrKz%2BmNYKtwDq9tYfBgpZanEFbkqBCSrFeFClHqmAljV0yHJSs1Pz95Lqg5N7%2BjsTmbaYl2voXjR%2Fw5XL7Ec4ez%2BJOllsavUSgQET2AAASfY%2BM6nx%2B7KzErW4AZAmEd48qdJlAfgOfjsSfTAEOnUs1UuW1gbgI0kBh6k9cfjDj9Qdg%2FkW3kLWZu%2Fbg4AzIxiqb%2BbN3LXOhQo%2FVwjrhF%2BSvi2y3hkMiihYe8oFIReKVNMptACBBg2ydmgKXoDOjuVCMww3eMyQfvnO8dlRL7%2FSs%2Fw09WaUcCy88F55Z6eb9qOHN%2BPN9Z%2BOc5axlr%2BHgLpUDUauOSFFLCQ9BUHFwu8KMatBcSL92T%2BjPjE4nvdL3nPg1GMTpR1R30GkSXTgw7GcZn3bKMq2yB9cAbSIpePS7Cn7b494Lp1YsxIlg7Rf79aColZQor2rs9qKwX0vfhXl6Omum%2BA23BtzhYDykoDZ55JZBsZicJE3t7IN3qYfAhKJmTypvQi49X%2BDftLWjR5Vj146gWjtnV2lKSmgYlMX4CTEnL9tAUB%2FRpEsb6XSb5rhcg9tESxc1YSKYl%2BRpCbwc34SUwp2VGPZUrf%2BrdUXGLRO6pnaMTLlh3%2FJLEfIatjVbnICIogOLrb3vz0a02rP2NwpxQw7ZuTvQY6pgHATv1iBNKagym5Tqi6%2F8EG0%2BrPSmTYSlzpdwNBzBIVxcCP%2FKMpHtO4eNTRaAFzETqVlgA8oLqmOV9TmpaIGVEbr%2B1Pg54q%2B8J90MBBkCk8WSqtqy8TUbeF4J1%2BrdPXGyZ%2FxOgDBN6PiCMi0Ehfxskzcnlop9ej0vUF6SWJ8BM2YbHVEKAFRTuBskVMlA1MApalr8YkXWXcXY3cVP4iANFdVL8kYY6j&X-Amz-Signature=11e7fae59183f8efb8dc15bcb68067437594a344eeadbbf7178cabd0768c7af3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBX6U5F7%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJGMEQCIApxozpMJVcMd9CLfoB4G83w6cO4twwzIAvI5xo%2FG7Y9AiAW04Smk86ux7QoQM%2BcsOI7ZZlr2%2F2eMuNRrz9wOg1tSyr%2FAwhgEAAaDDYzNzQyMzE4MzgwNSIMp6uYVX4fJrKz%2BmNYKtwDq9tYfBgpZanEFbkqBCSrFeFClHqmAljV0yHJSs1Pz95Lqg5N7%2BjsTmbaYl2voXjR%2Fw5XL7Ec4ez%2BJOllsavUSgQET2AAASfY%2BM6nx%2B7KzErW4AZAmEd48qdJlAfgOfjsSfTAEOnUs1UuW1gbgI0kBh6k9cfjDj9Qdg%2FkW3kLWZu%2Fbg4AzIxiqb%2BbN3LXOhQo%2FVwjrhF%2BSvi2y3hkMiihYe8oFIReKVNMptACBBg2ydmgKXoDOjuVCMww3eMyQfvnO8dlRL7%2FSs%2Fw09WaUcCy88F55Z6eb9qOHN%2BPN9Z%2BOc5axlr%2BHgLpUDUauOSFFLCQ9BUHFwu8KMatBcSL92T%2BjPjE4nvdL3nPg1GMTpR1R30GkSXTgw7GcZn3bKMq2yB9cAbSIpePS7Cn7b494Lp1YsxIlg7Rf79aColZQor2rs9qKwX0vfhXl6Omum%2BA23BtzhYDykoDZ55JZBsZicJE3t7IN3qYfAhKJmTypvQi49X%2BDftLWjR5Vj146gWjtnV2lKSmgYlMX4CTEnL9tAUB%2FRpEsb6XSb5rhcg9tESxc1YSKYl%2BRpCbwc34SUwp2VGPZUrf%2BrdUXGLRO6pnaMTLlh3%2FJLEfIatjVbnICIogOLrb3vz0a02rP2NwpxQw7ZuTvQY6pgHATv1iBNKagym5Tqi6%2F8EG0%2BrPSmTYSlzpdwNBzBIVxcCP%2FKMpHtO4eNTRaAFzETqVlgA8oLqmOV9TmpaIGVEbr%2B1Pg54q%2B8J90MBBkCk8WSqtqy8TUbeF4J1%2BrdPXGyZ%2FxOgDBN6PiCMi0Ehfxskzcnlop9ej0vUF6SWJ8BM2YbHVEKAFRTuBskVMlA1MApalr8YkXWXcXY3cVP4iANFdVL8kYY6j&X-Amz-Signature=3b4186fd6b09fd81c91c7c6fe934c3a4d2223dd8177e08366a8906184a8594f3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBX6U5F7%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJGMEQCIApxozpMJVcMd9CLfoB4G83w6cO4twwzIAvI5xo%2FG7Y9AiAW04Smk86ux7QoQM%2BcsOI7ZZlr2%2F2eMuNRrz9wOg1tSyr%2FAwhgEAAaDDYzNzQyMzE4MzgwNSIMp6uYVX4fJrKz%2BmNYKtwDq9tYfBgpZanEFbkqBCSrFeFClHqmAljV0yHJSs1Pz95Lqg5N7%2BjsTmbaYl2voXjR%2Fw5XL7Ec4ez%2BJOllsavUSgQET2AAASfY%2BM6nx%2B7KzErW4AZAmEd48qdJlAfgOfjsSfTAEOnUs1UuW1gbgI0kBh6k9cfjDj9Qdg%2FkW3kLWZu%2Fbg4AzIxiqb%2BbN3LXOhQo%2FVwjrhF%2BSvi2y3hkMiihYe8oFIReKVNMptACBBg2ydmgKXoDOjuVCMww3eMyQfvnO8dlRL7%2FSs%2Fw09WaUcCy88F55Z6eb9qOHN%2BPN9Z%2BOc5axlr%2BHgLpUDUauOSFFLCQ9BUHFwu8KMatBcSL92T%2BjPjE4nvdL3nPg1GMTpR1R30GkSXTgw7GcZn3bKMq2yB9cAbSIpePS7Cn7b494Lp1YsxIlg7Rf79aColZQor2rs9qKwX0vfhXl6Omum%2BA23BtzhYDykoDZ55JZBsZicJE3t7IN3qYfAhKJmTypvQi49X%2BDftLWjR5Vj146gWjtnV2lKSmgYlMX4CTEnL9tAUB%2FRpEsb6XSb5rhcg9tESxc1YSKYl%2BRpCbwc34SUwp2VGPZUrf%2BrdUXGLRO6pnaMTLlh3%2FJLEfIatjVbnICIogOLrb3vz0a02rP2NwpxQw7ZuTvQY6pgHATv1iBNKagym5Tqi6%2F8EG0%2BrPSmTYSlzpdwNBzBIVxcCP%2FKMpHtO4eNTRaAFzETqVlgA8oLqmOV9TmpaIGVEbr%2B1Pg54q%2B8J90MBBkCk8WSqtqy8TUbeF4J1%2BrdPXGyZ%2FxOgDBN6PiCMi0Ehfxskzcnlop9ej0vUF6SWJ8BM2YbHVEKAFRTuBskVMlA1MApalr8YkXWXcXY3cVP4iANFdVL8kYY6j&X-Amz-Signature=4241fabb59a6904e46990e0eb0934f3a8ada3d22d20615dd2f7af88230b0e3c1&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBX6U5F7%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJGMEQCIApxozpMJVcMd9CLfoB4G83w6cO4twwzIAvI5xo%2FG7Y9AiAW04Smk86ux7QoQM%2BcsOI7ZZlr2%2F2eMuNRrz9wOg1tSyr%2FAwhgEAAaDDYzNzQyMzE4MzgwNSIMp6uYVX4fJrKz%2BmNYKtwDq9tYfBgpZanEFbkqBCSrFeFClHqmAljV0yHJSs1Pz95Lqg5N7%2BjsTmbaYl2voXjR%2Fw5XL7Ec4ez%2BJOllsavUSgQET2AAASfY%2BM6nx%2B7KzErW4AZAmEd48qdJlAfgOfjsSfTAEOnUs1UuW1gbgI0kBh6k9cfjDj9Qdg%2FkW3kLWZu%2Fbg4AzIxiqb%2BbN3LXOhQo%2FVwjrhF%2BSvi2y3hkMiihYe8oFIReKVNMptACBBg2ydmgKXoDOjuVCMww3eMyQfvnO8dlRL7%2FSs%2Fw09WaUcCy88F55Z6eb9qOHN%2BPN9Z%2BOc5axlr%2BHgLpUDUauOSFFLCQ9BUHFwu8KMatBcSL92T%2BjPjE4nvdL3nPg1GMTpR1R30GkSXTgw7GcZn3bKMq2yB9cAbSIpePS7Cn7b494Lp1YsxIlg7Rf79aColZQor2rs9qKwX0vfhXl6Omum%2BA23BtzhYDykoDZ55JZBsZicJE3t7IN3qYfAhKJmTypvQi49X%2BDftLWjR5Vj146gWjtnV2lKSmgYlMX4CTEnL9tAUB%2FRpEsb6XSb5rhcg9tESxc1YSKYl%2BRpCbwc34SUwp2VGPZUrf%2BrdUXGLRO6pnaMTLlh3%2FJLEfIatjVbnICIogOLrb3vz0a02rP2NwpxQw7ZuTvQY6pgHATv1iBNKagym5Tqi6%2F8EG0%2BrPSmTYSlzpdwNBzBIVxcCP%2FKMpHtO4eNTRaAFzETqVlgA8oLqmOV9TmpaIGVEbr%2B1Pg54q%2B8J90MBBkCk8WSqtqy8TUbeF4J1%2BrdPXGyZ%2FxOgDBN6PiCMi0Ehfxskzcnlop9ej0vUF6SWJ8BM2YbHVEKAFRTuBskVMlA1MApalr8YkXWXcXY3cVP4iANFdVL8kYY6j&X-Amz-Signature=c27f5fbcdeb7d3e882f49af845a0e75986d66f4c62fe5dcb7e4ede9ff9384895&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
