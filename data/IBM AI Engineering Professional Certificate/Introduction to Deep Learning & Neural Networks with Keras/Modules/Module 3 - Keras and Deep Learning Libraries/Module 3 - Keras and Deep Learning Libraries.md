

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YD6JKFXW%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIQCf6%2Fv6BJ5aUvvpxdyjTVtxDjUCALqDwi5ll14z9GrMvgIgAV5b2IkCDc%2Fuho1C7fUViZqOJBnCs2kLnF2qrGDh2iEq%2FwMIHxAAGgw2Mzc0MjMxODM4MDUiDOP0l7N%2Bt1hVLhQpySrcAz3PKBoaPGJ1PMFWWPww%2BipoaUI5ohsdHhLo1WoL%2BxXk1pqHqb8DNHP77lVzdGB0d6AY%2BwKq1T6ro6U54%2B22cwe5bZaGaSp%2FuUdvYgn9NRaMytaUu%2Bp9zWp8yDI7hDJ0il0vmiurOgvMcmRzAc%2BSxJ%2Fu5NpebS8s47lop1ndHMgYMqV2LBgbHycIe%2B7aWSS5oV46BaoCb4Wvpi6JyNf4LapOuI471jznLstC%2FvGm4YGNROB1Csd61kpy%2BFXBhuJ7MMbj3wljDmAkXyT59zpEIlvlFtRS4XJpbP9TJuNCovG09DQHtUkQ53onRuUE5z430vBCTsybqmfr5s0ZHWAX6XQDb840wni7vQoTsyDU57UKsbNq0WaysvNWqaNMgYhjehl8Wxq9ebTbMx%2BL7UHIjJmrPcrvM7KZtChQDe5sQm4k6%2BBWL3J6eINMSdR1jHmrW8MavAPPTao4t%2BP%2FafVqPS6ISiyhoRvCgDnjHod2hviZePgFw9PdtzD0SBoqOAu4Ieva%2FM9lUmQ6Roye%2B4SqgqYhjhG3tpTiUls4Ec6azj6kU9Zl0K2GRAD%2BgCTRhwQWaUkbj5jW3FmItw2iWVCLeAonE04DuK%2BBP9mpudViBYCUOqurIi2hnYN4c49MMP%2F3hL0GOqUBfON5ngC8I7tdes5Z6zjDSBz2gCwbO0UlkghvtS5j33ytlek6tS8h3UdHTEbsD7zMLY1cTq6aCznHIotD%2FZEgsHDG3T3HNfEI3WPVeK8NVlTG5xgsGGTz%2BG7PVdLWrdzuiNMwTEL5zad7oU2Qf3ncPY9iNsk31V3pOvyamFiKEKJDhTL%2BdPmPwndn2I1HOQT%2BZfcN80GipCtd6XKvcLYLpdPs1bUw&X-Amz-Signature=c35447d7626fdd9cff28c298755c036eef6a0fef4a0e73672c67bf9f680cd945&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YD6JKFXW%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIQCf6%2Fv6BJ5aUvvpxdyjTVtxDjUCALqDwi5ll14z9GrMvgIgAV5b2IkCDc%2Fuho1C7fUViZqOJBnCs2kLnF2qrGDh2iEq%2FwMIHxAAGgw2Mzc0MjMxODM4MDUiDOP0l7N%2Bt1hVLhQpySrcAz3PKBoaPGJ1PMFWWPww%2BipoaUI5ohsdHhLo1WoL%2BxXk1pqHqb8DNHP77lVzdGB0d6AY%2BwKq1T6ro6U54%2B22cwe5bZaGaSp%2FuUdvYgn9NRaMytaUu%2Bp9zWp8yDI7hDJ0il0vmiurOgvMcmRzAc%2BSxJ%2Fu5NpebS8s47lop1ndHMgYMqV2LBgbHycIe%2B7aWSS5oV46BaoCb4Wvpi6JyNf4LapOuI471jznLstC%2FvGm4YGNROB1Csd61kpy%2BFXBhuJ7MMbj3wljDmAkXyT59zpEIlvlFtRS4XJpbP9TJuNCovG09DQHtUkQ53onRuUE5z430vBCTsybqmfr5s0ZHWAX6XQDb840wni7vQoTsyDU57UKsbNq0WaysvNWqaNMgYhjehl8Wxq9ebTbMx%2BL7UHIjJmrPcrvM7KZtChQDe5sQm4k6%2BBWL3J6eINMSdR1jHmrW8MavAPPTao4t%2BP%2FafVqPS6ISiyhoRvCgDnjHod2hviZePgFw9PdtzD0SBoqOAu4Ieva%2FM9lUmQ6Roye%2B4SqgqYhjhG3tpTiUls4Ec6azj6kU9Zl0K2GRAD%2BgCTRhwQWaUkbj5jW3FmItw2iWVCLeAonE04DuK%2BBP9mpudViBYCUOqurIi2hnYN4c49MMP%2F3hL0GOqUBfON5ngC8I7tdes5Z6zjDSBz2gCwbO0UlkghvtS5j33ytlek6tS8h3UdHTEbsD7zMLY1cTq6aCznHIotD%2FZEgsHDG3T3HNfEI3WPVeK8NVlTG5xgsGGTz%2BG7PVdLWrdzuiNMwTEL5zad7oU2Qf3ncPY9iNsk31V3pOvyamFiKEKJDhTL%2BdPmPwndn2I1HOQT%2BZfcN80GipCtd6XKvcLYLpdPs1bUw&X-Amz-Signature=381356939821654f08625319f8a941829b3a52ca8607a7f4f0ecafac17d45d20&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YD6JKFXW%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIQCf6%2Fv6BJ5aUvvpxdyjTVtxDjUCALqDwi5ll14z9GrMvgIgAV5b2IkCDc%2Fuho1C7fUViZqOJBnCs2kLnF2qrGDh2iEq%2FwMIHxAAGgw2Mzc0MjMxODM4MDUiDOP0l7N%2Bt1hVLhQpySrcAz3PKBoaPGJ1PMFWWPww%2BipoaUI5ohsdHhLo1WoL%2BxXk1pqHqb8DNHP77lVzdGB0d6AY%2BwKq1T6ro6U54%2B22cwe5bZaGaSp%2FuUdvYgn9NRaMytaUu%2Bp9zWp8yDI7hDJ0il0vmiurOgvMcmRzAc%2BSxJ%2Fu5NpebS8s47lop1ndHMgYMqV2LBgbHycIe%2B7aWSS5oV46BaoCb4Wvpi6JyNf4LapOuI471jznLstC%2FvGm4YGNROB1Csd61kpy%2BFXBhuJ7MMbj3wljDmAkXyT59zpEIlvlFtRS4XJpbP9TJuNCovG09DQHtUkQ53onRuUE5z430vBCTsybqmfr5s0ZHWAX6XQDb840wni7vQoTsyDU57UKsbNq0WaysvNWqaNMgYhjehl8Wxq9ebTbMx%2BL7UHIjJmrPcrvM7KZtChQDe5sQm4k6%2BBWL3J6eINMSdR1jHmrW8MavAPPTao4t%2BP%2FafVqPS6ISiyhoRvCgDnjHod2hviZePgFw9PdtzD0SBoqOAu4Ieva%2FM9lUmQ6Roye%2B4SqgqYhjhG3tpTiUls4Ec6azj6kU9Zl0K2GRAD%2BgCTRhwQWaUkbj5jW3FmItw2iWVCLeAonE04DuK%2BBP9mpudViBYCUOqurIi2hnYN4c49MMP%2F3hL0GOqUBfON5ngC8I7tdes5Z6zjDSBz2gCwbO0UlkghvtS5j33ytlek6tS8h3UdHTEbsD7zMLY1cTq6aCznHIotD%2FZEgsHDG3T3HNfEI3WPVeK8NVlTG5xgsGGTz%2BG7PVdLWrdzuiNMwTEL5zad7oU2Qf3ncPY9iNsk31V3pOvyamFiKEKJDhTL%2BdPmPwndn2I1HOQT%2BZfcN80GipCtd6XKvcLYLpdPs1bUw&X-Amz-Signature=6ec1a08addaa84617b1997392c42e5ad3ea5cb0aca6413a1e8747deb16e6632b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YCDRUSB2%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJGMEQCICZvC1C6975gQ8WJW9gSpgKNNduX7tlQ412HclGAoH2FAiBzlxksOn5Iy7ycEGWR5IxZYGusEAWc33SI6bh35Yxjcir%2FAwgfEAAaDDYzNzQyMzE4MzgwNSIM4W4JJikWeVxVK1IgKtwDpNI%2BNGFvHptbIAmutxKn2qmfXxHRmVGTFdvHmz0AC82MehNKvJN1ZztAh8tpdq7h0RejC8WCME1JvFUfjDkDiyU0IH%2FA2KTTnOFymZh%2FH2AiLrkFIc7gE%2BdZFZHyWvmODHBibQBBnUCYNIFGRF77bKnOHDAtXkdsVYzD3Of9OIS6iDhGGmFHLeY0%2Bc7tkwhV9j6JWC5%2BetOg9jNaofyMUnYmMMjMiXTi1vsrs%2FzzZ86Fa4pC186QsDrrn90t3pXS5sAhfKyVxfTbtrWP%2BDJoMyYtGhkc%2FcVdAnWUEKNGaYKbDabhGK1vtjidudnmtM1B9OXRJOPwFZ2dvnyOmKm%2BoPSMIGmlPN1xgJwlHgw8b2c1icpQ9J0qteB4lwPaRSjxqjQ1VZuit8s5HtLI12N1zxl96fcai6w4U0cSZFmLhq1zZt9eX%2BMlq8NrwdEewtqXTdQJ1xODt%2FGHE3yCE79DYtG9zs7MZnA5%2Bx8JMEmMLNbn7Ms1qb1lJDzFQc3aTIxKDTntH2SUTcspuq%2F6xdWHavhb%2FmKtzrc2NBE%2FyaMhrP9Ytk5Tu3MfuqGtmIe0XBZDbPHd4GEnN7qTsXcwYuIfhtRQ7SXR6uRQzPK1VBvkRyHP9hf9nHNswsQiegkww%2FeEvQY6pgERdRfowejMsvtZvP5O9gi3Hbbor7s9HwNmsDb11iR0BQeZtSUAvH7dvitCIWW%2BuluvCMIy%2F46WqYQjgwqSyy2irO5w4Ed6DDL1jN%2B4IA%2FFgjv07ViuZfbGx3nD5SojkiGNL9d9Jz6KVD1quRuTmA54LP0mB2aCgSqXMqHOtsFANbq6PMIQnGjMZzxBwU7A2BvTImtvRWXH8WdTecsKGd33m%2BN%2Bsk%2BX&X-Amz-Signature=6502a1e5b0b8fe092989f037f0092afa72b2eac52c304bbb8a028812b21eb066&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VZNOSKHV%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIQCSjPN639Hd%2Fp9IttypswezKdFBkqSckY%2FYUeGJ1HohPgIgRiWV3awR9%2FleJAdOPzZl8utOzyTGoyvD37edNMeypFsq%2FwMIHxAAGgw2Mzc0MjMxODM4MDUiDLkuiJXfKDDVJY4f2ircAzMCc3MRNePJRREwclAbahdb%2FyuquQ4OaeqFhriiEFmffBrHdhvZriOsJ24ff9QwsP8PugFEBSM%2B6aQk%2FSx6KfuYqZWiIJezlPIPt%2FT0v4dynQ4xx2MP09BnrFIzcRMYst8ZE02KeY2BJNIUrBSLCVlIBcQf3BlfCkfjghR7Jq1Yrh6BvWiMzJs4c%2FzTuMZBzrvuQpZ9mhJDJHl9UcnBGHv2xw83W5mi3gvsbjUSS90I%2FCcYlpbAXBvtWKEDqhChsIyn%2BhqXyKdhBLX6dVovQqMM4oMRhzM8SVXLvyKIIksAL4WMgwExC8UifRhMWLiIpHWCoVYdbiBOGj%2FRtRKA%2BcM54A1bBodeZnNgfiSdBVqD5hfS3ulWNJK9yiMvjj61T9%2FXzikP6kDhK4phV9OWkXP76k2oS6vJw%2FB%2ByNNzWNF1hWqmeeu10aydPadPtPKkN9hdrVodynTnXs7OE9Cj8zwDupd9ZvVl%2FPWgzPtpjmdS2rR22DFlir13G8SgaWzkCdqWmwhVd2%2FU4PwDl%2BbWmo0RqP%2BjjieQskY44Y8UGZl%2BB7SZNv9Jyq2N1knv80QBbWRZKY%2FAfMQddsjSZKzWAaRaDZKz04ke%2FlKY40gikWJjDI1SW0N2HvMFPJxCMMP3hL0GOqUBEhyCEiQORP48dAKH9cM9GnLl86OzFbphoer2Ma0w0Jq8DksDx%2FcdzSMof66ozSyi32ZklqtK997OgVVjqUdhBY4wTqBpEBCsVzMagKTBVOYZHadDW3iUIcKsLFtTvVp8N5XMRc%2Bf35amFcnIZVKJGvLVnRk6XoMltSDYrfaxA6QB%2BOWhC35TD%2FtDx%2BnT5U3u7zpxwHjsn9qUdHdYddq5tNU8RkBl&X-Amz-Signature=2d53d264d9f120cc5e7d1765061cd251f3674614200762b1426051d6fefab246&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YD6JKFXW%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIQCf6%2Fv6BJ5aUvvpxdyjTVtxDjUCALqDwi5ll14z9GrMvgIgAV5b2IkCDc%2Fuho1C7fUViZqOJBnCs2kLnF2qrGDh2iEq%2FwMIHxAAGgw2Mzc0MjMxODM4MDUiDOP0l7N%2Bt1hVLhQpySrcAz3PKBoaPGJ1PMFWWPww%2BipoaUI5ohsdHhLo1WoL%2BxXk1pqHqb8DNHP77lVzdGB0d6AY%2BwKq1T6ro6U54%2B22cwe5bZaGaSp%2FuUdvYgn9NRaMytaUu%2Bp9zWp8yDI7hDJ0il0vmiurOgvMcmRzAc%2BSxJ%2Fu5NpebS8s47lop1ndHMgYMqV2LBgbHycIe%2B7aWSS5oV46BaoCb4Wvpi6JyNf4LapOuI471jznLstC%2FvGm4YGNROB1Csd61kpy%2BFXBhuJ7MMbj3wljDmAkXyT59zpEIlvlFtRS4XJpbP9TJuNCovG09DQHtUkQ53onRuUE5z430vBCTsybqmfr5s0ZHWAX6XQDb840wni7vQoTsyDU57UKsbNq0WaysvNWqaNMgYhjehl8Wxq9ebTbMx%2BL7UHIjJmrPcrvM7KZtChQDe5sQm4k6%2BBWL3J6eINMSdR1jHmrW8MavAPPTao4t%2BP%2FafVqPS6ISiyhoRvCgDnjHod2hviZePgFw9PdtzD0SBoqOAu4Ieva%2FM9lUmQ6Roye%2B4SqgqYhjhG3tpTiUls4Ec6azj6kU9Zl0K2GRAD%2BgCTRhwQWaUkbj5jW3FmItw2iWVCLeAonE04DuK%2BBP9mpudViBYCUOqurIi2hnYN4c49MMP%2F3hL0GOqUBfON5ngC8I7tdes5Z6zjDSBz2gCwbO0UlkghvtS5j33ytlek6tS8h3UdHTEbsD7zMLY1cTq6aCznHIotD%2FZEgsHDG3T3HNfEI3WPVeK8NVlTG5xgsGGTz%2BG7PVdLWrdzuiNMwTEL5zad7oU2Qf3ncPY9iNsk31V3pOvyamFiKEKJDhTL%2BdPmPwndn2I1HOQT%2BZfcN80GipCtd6XKvcLYLpdPs1bUw&X-Amz-Signature=2f4b5fc1da559972329c53cd93823a652745f6c55527ea4d7f48988310d70f83&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YD6JKFXW%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIQCf6%2Fv6BJ5aUvvpxdyjTVtxDjUCALqDwi5ll14z9GrMvgIgAV5b2IkCDc%2Fuho1C7fUViZqOJBnCs2kLnF2qrGDh2iEq%2FwMIHxAAGgw2Mzc0MjMxODM4MDUiDOP0l7N%2Bt1hVLhQpySrcAz3PKBoaPGJ1PMFWWPww%2BipoaUI5ohsdHhLo1WoL%2BxXk1pqHqb8DNHP77lVzdGB0d6AY%2BwKq1T6ro6U54%2B22cwe5bZaGaSp%2FuUdvYgn9NRaMytaUu%2Bp9zWp8yDI7hDJ0il0vmiurOgvMcmRzAc%2BSxJ%2Fu5NpebS8s47lop1ndHMgYMqV2LBgbHycIe%2B7aWSS5oV46BaoCb4Wvpi6JyNf4LapOuI471jznLstC%2FvGm4YGNROB1Csd61kpy%2BFXBhuJ7MMbj3wljDmAkXyT59zpEIlvlFtRS4XJpbP9TJuNCovG09DQHtUkQ53onRuUE5z430vBCTsybqmfr5s0ZHWAX6XQDb840wni7vQoTsyDU57UKsbNq0WaysvNWqaNMgYhjehl8Wxq9ebTbMx%2BL7UHIjJmrPcrvM7KZtChQDe5sQm4k6%2BBWL3J6eINMSdR1jHmrW8MavAPPTao4t%2BP%2FafVqPS6ISiyhoRvCgDnjHod2hviZePgFw9PdtzD0SBoqOAu4Ieva%2FM9lUmQ6Roye%2B4SqgqYhjhG3tpTiUls4Ec6azj6kU9Zl0K2GRAD%2BgCTRhwQWaUkbj5jW3FmItw2iWVCLeAonE04DuK%2BBP9mpudViBYCUOqurIi2hnYN4c49MMP%2F3hL0GOqUBfON5ngC8I7tdes5Z6zjDSBz2gCwbO0UlkghvtS5j33ytlek6tS8h3UdHTEbsD7zMLY1cTq6aCznHIotD%2FZEgsHDG3T3HNfEI3WPVeK8NVlTG5xgsGGTz%2BG7PVdLWrdzuiNMwTEL5zad7oU2Qf3ncPY9iNsk31V3pOvyamFiKEKJDhTL%2BdPmPwndn2I1HOQT%2BZfcN80GipCtd6XKvcLYLpdPs1bUw&X-Amz-Signature=6a3513a79d9d27f7e1375ae53350a0a3c7b93daa78f2066d4a862016f6871330&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YD6JKFXW%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIQCf6%2Fv6BJ5aUvvpxdyjTVtxDjUCALqDwi5ll14z9GrMvgIgAV5b2IkCDc%2Fuho1C7fUViZqOJBnCs2kLnF2qrGDh2iEq%2FwMIHxAAGgw2Mzc0MjMxODM4MDUiDOP0l7N%2Bt1hVLhQpySrcAz3PKBoaPGJ1PMFWWPww%2BipoaUI5ohsdHhLo1WoL%2BxXk1pqHqb8DNHP77lVzdGB0d6AY%2BwKq1T6ro6U54%2B22cwe5bZaGaSp%2FuUdvYgn9NRaMytaUu%2Bp9zWp8yDI7hDJ0il0vmiurOgvMcmRzAc%2BSxJ%2Fu5NpebS8s47lop1ndHMgYMqV2LBgbHycIe%2B7aWSS5oV46BaoCb4Wvpi6JyNf4LapOuI471jznLstC%2FvGm4YGNROB1Csd61kpy%2BFXBhuJ7MMbj3wljDmAkXyT59zpEIlvlFtRS4XJpbP9TJuNCovG09DQHtUkQ53onRuUE5z430vBCTsybqmfr5s0ZHWAX6XQDb840wni7vQoTsyDU57UKsbNq0WaysvNWqaNMgYhjehl8Wxq9ebTbMx%2BL7UHIjJmrPcrvM7KZtChQDe5sQm4k6%2BBWL3J6eINMSdR1jHmrW8MavAPPTao4t%2BP%2FafVqPS6ISiyhoRvCgDnjHod2hviZePgFw9PdtzD0SBoqOAu4Ieva%2FM9lUmQ6Roye%2B4SqgqYhjhG3tpTiUls4Ec6azj6kU9Zl0K2GRAD%2BgCTRhwQWaUkbj5jW3FmItw2iWVCLeAonE04DuK%2BBP9mpudViBYCUOqurIi2hnYN4c49MMP%2F3hL0GOqUBfON5ngC8I7tdes5Z6zjDSBz2gCwbO0UlkghvtS5j33ytlek6tS8h3UdHTEbsD7zMLY1cTq6aCznHIotD%2FZEgsHDG3T3HNfEI3WPVeK8NVlTG5xgsGGTz%2BG7PVdLWrdzuiNMwTEL5zad7oU2Qf3ncPY9iNsk31V3pOvyamFiKEKJDhTL%2BdPmPwndn2I1HOQT%2BZfcN80GipCtd6XKvcLYLpdPs1bUw&X-Amz-Signature=079386e615df22a652657c18928de02d8d919f0e5807bd68cec1970c94dff0ad&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YD6JKFXW%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIQCf6%2Fv6BJ5aUvvpxdyjTVtxDjUCALqDwi5ll14z9GrMvgIgAV5b2IkCDc%2Fuho1C7fUViZqOJBnCs2kLnF2qrGDh2iEq%2FwMIHxAAGgw2Mzc0MjMxODM4MDUiDOP0l7N%2Bt1hVLhQpySrcAz3PKBoaPGJ1PMFWWPww%2BipoaUI5ohsdHhLo1WoL%2BxXk1pqHqb8DNHP77lVzdGB0d6AY%2BwKq1T6ro6U54%2B22cwe5bZaGaSp%2FuUdvYgn9NRaMytaUu%2Bp9zWp8yDI7hDJ0il0vmiurOgvMcmRzAc%2BSxJ%2Fu5NpebS8s47lop1ndHMgYMqV2LBgbHycIe%2B7aWSS5oV46BaoCb4Wvpi6JyNf4LapOuI471jznLstC%2FvGm4YGNROB1Csd61kpy%2BFXBhuJ7MMbj3wljDmAkXyT59zpEIlvlFtRS4XJpbP9TJuNCovG09DQHtUkQ53onRuUE5z430vBCTsybqmfr5s0ZHWAX6XQDb840wni7vQoTsyDU57UKsbNq0WaysvNWqaNMgYhjehl8Wxq9ebTbMx%2BL7UHIjJmrPcrvM7KZtChQDe5sQm4k6%2BBWL3J6eINMSdR1jHmrW8MavAPPTao4t%2BP%2FafVqPS6ISiyhoRvCgDnjHod2hviZePgFw9PdtzD0SBoqOAu4Ieva%2FM9lUmQ6Roye%2B4SqgqYhjhG3tpTiUls4Ec6azj6kU9Zl0K2GRAD%2BgCTRhwQWaUkbj5jW3FmItw2iWVCLeAonE04DuK%2BBP9mpudViBYCUOqurIi2hnYN4c49MMP%2F3hL0GOqUBfON5ngC8I7tdes5Z6zjDSBz2gCwbO0UlkghvtS5j33ytlek6tS8h3UdHTEbsD7zMLY1cTq6aCznHIotD%2FZEgsHDG3T3HNfEI3WPVeK8NVlTG5xgsGGTz%2BG7PVdLWrdzuiNMwTEL5zad7oU2Qf3ncPY9iNsk31V3pOvyamFiKEKJDhTL%2BdPmPwndn2I1HOQT%2BZfcN80GipCtd6XKvcLYLpdPs1bUw&X-Amz-Signature=1278d1e552edb8dab245b69ab6006de6216c74bd3ca4c7dd506c0e0a1db0fffc&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
