

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665WZ6D54K%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJHMEUCIBmC9%2FV%2FHl0pyNSLX1QU%2Fi486AOg5zfdNkbfpNXHW1otAiEAsNodMGGpxeSm3Hh9bkLjuxkWboywfT8UG6T5J13jODEq%2FwMIXxAAGgw2Mzc0MjMxODM4MDUiDEbrJu6ijJvNp168uCrcA3QK5LXW6Il16fXYtT42%2FqiONAkgMPlqpsgxg9%2B6SomuDIk7JBTWlGRZll2Y0DP6LN%2BjN%2F5SpcnRdB4VpJMqnL%2BWWCGUd3H6QbLb3McL5rkqlCSgf6qRQJQVrLkAGubFCKKyWJY67Gk5J7nufFoOJgv2o7YLXMsKixQ0CcI5vXmAbIGXnog%2FvqTRjbgOYPbvM0yRLGPASMxSpOYJKkRS59jQtMpSIGD1BkCH9X59XdXKJzxMMEraTVjZobl9Oacsd1b3cLrLBfHyrhKEDPJcH%2Ffw1sgkdUceUtWQsJJepM7UK1sgnUgQZUni4ciYUGvuSPk6AFZ3HbfCe94TJLKtNSbUYuA4hZcB1tQO6a%2FCcSdLSILF%2BGgxeZ3Kd%2F%2FkZt4%2B0Idxpy9kz5%2FOuIL42gCawhqPXZQZxU4rx9FzdA%2Bcd1ocrxSPE%2BVntAKVzfm5fDpCDwvyNGTAO%2FfIhj5EOrAyBYHXaCG%2B2LycTsS6pRCy49voPKebIrG4kMUzJ4JAoJZoSRAnF1t6MG0NbudU%2BnYeSdgVgqxiVzNkBywabytiSl2rWFf2kIR%2FjEFaNjK9aoPiKVGdK68%2BejnT86%2BBS9Z%2BCEsrm6iZolVmVW4V3cZpdLP2%2BUVzIx4lAcQjkXm3MJf5kr0GOqUBlfCxRwji0UkLmPCIPpoVdDkXnbBK%2FFtwIi4nQ1GQC6taINGU%2B2qHM2NyZzeP6nV3raV8iz6OgE1OVIIwbTF%2Fm0ZmID5s%2FSz2WVKKw0VannDdnPkazl91uGtw7IdnPzZSV3yf%2FKQQ81UURVDC6gFPrgvMGEjW0qlVanMnJwGHSZghUn4ELbAIdtas0qVZzx65exkfjzJNBCephguXNelEcRKbImoZ&X-Amz-Signature=dabc298feadd58e4af331bc736b794b4b5c3d5e0a19053b5610535784441f942&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665WZ6D54K%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJHMEUCIBmC9%2FV%2FHl0pyNSLX1QU%2Fi486AOg5zfdNkbfpNXHW1otAiEAsNodMGGpxeSm3Hh9bkLjuxkWboywfT8UG6T5J13jODEq%2FwMIXxAAGgw2Mzc0MjMxODM4MDUiDEbrJu6ijJvNp168uCrcA3QK5LXW6Il16fXYtT42%2FqiONAkgMPlqpsgxg9%2B6SomuDIk7JBTWlGRZll2Y0DP6LN%2BjN%2F5SpcnRdB4VpJMqnL%2BWWCGUd3H6QbLb3McL5rkqlCSgf6qRQJQVrLkAGubFCKKyWJY67Gk5J7nufFoOJgv2o7YLXMsKixQ0CcI5vXmAbIGXnog%2FvqTRjbgOYPbvM0yRLGPASMxSpOYJKkRS59jQtMpSIGD1BkCH9X59XdXKJzxMMEraTVjZobl9Oacsd1b3cLrLBfHyrhKEDPJcH%2Ffw1sgkdUceUtWQsJJepM7UK1sgnUgQZUni4ciYUGvuSPk6AFZ3HbfCe94TJLKtNSbUYuA4hZcB1tQO6a%2FCcSdLSILF%2BGgxeZ3Kd%2F%2FkZt4%2B0Idxpy9kz5%2FOuIL42gCawhqPXZQZxU4rx9FzdA%2Bcd1ocrxSPE%2BVntAKVzfm5fDpCDwvyNGTAO%2FfIhj5EOrAyBYHXaCG%2B2LycTsS6pRCy49voPKebIrG4kMUzJ4JAoJZoSRAnF1t6MG0NbudU%2BnYeSdgVgqxiVzNkBywabytiSl2rWFf2kIR%2FjEFaNjK9aoPiKVGdK68%2BejnT86%2BBS9Z%2BCEsrm6iZolVmVW4V3cZpdLP2%2BUVzIx4lAcQjkXm3MJf5kr0GOqUBlfCxRwji0UkLmPCIPpoVdDkXnbBK%2FFtwIi4nQ1GQC6taINGU%2B2qHM2NyZzeP6nV3raV8iz6OgE1OVIIwbTF%2Fm0ZmID5s%2FSz2WVKKw0VannDdnPkazl91uGtw7IdnPzZSV3yf%2FKQQ81UURVDC6gFPrgvMGEjW0qlVanMnJwGHSZghUn4ELbAIdtas0qVZzx65exkfjzJNBCephguXNelEcRKbImoZ&X-Amz-Signature=da75448233703aba566a04a6149e2dfbc3c27ccc33c05f3c22609f3016e8f522&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665WZ6D54K%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJHMEUCIBmC9%2FV%2FHl0pyNSLX1QU%2Fi486AOg5zfdNkbfpNXHW1otAiEAsNodMGGpxeSm3Hh9bkLjuxkWboywfT8UG6T5J13jODEq%2FwMIXxAAGgw2Mzc0MjMxODM4MDUiDEbrJu6ijJvNp168uCrcA3QK5LXW6Il16fXYtT42%2FqiONAkgMPlqpsgxg9%2B6SomuDIk7JBTWlGRZll2Y0DP6LN%2BjN%2F5SpcnRdB4VpJMqnL%2BWWCGUd3H6QbLb3McL5rkqlCSgf6qRQJQVrLkAGubFCKKyWJY67Gk5J7nufFoOJgv2o7YLXMsKixQ0CcI5vXmAbIGXnog%2FvqTRjbgOYPbvM0yRLGPASMxSpOYJKkRS59jQtMpSIGD1BkCH9X59XdXKJzxMMEraTVjZobl9Oacsd1b3cLrLBfHyrhKEDPJcH%2Ffw1sgkdUceUtWQsJJepM7UK1sgnUgQZUni4ciYUGvuSPk6AFZ3HbfCe94TJLKtNSbUYuA4hZcB1tQO6a%2FCcSdLSILF%2BGgxeZ3Kd%2F%2FkZt4%2B0Idxpy9kz5%2FOuIL42gCawhqPXZQZxU4rx9FzdA%2Bcd1ocrxSPE%2BVntAKVzfm5fDpCDwvyNGTAO%2FfIhj5EOrAyBYHXaCG%2B2LycTsS6pRCy49voPKebIrG4kMUzJ4JAoJZoSRAnF1t6MG0NbudU%2BnYeSdgVgqxiVzNkBywabytiSl2rWFf2kIR%2FjEFaNjK9aoPiKVGdK68%2BejnT86%2BBS9Z%2BCEsrm6iZolVmVW4V3cZpdLP2%2BUVzIx4lAcQjkXm3MJf5kr0GOqUBlfCxRwji0UkLmPCIPpoVdDkXnbBK%2FFtwIi4nQ1GQC6taINGU%2B2qHM2NyZzeP6nV3raV8iz6OgE1OVIIwbTF%2Fm0ZmID5s%2FSz2WVKKw0VannDdnPkazl91uGtw7IdnPzZSV3yf%2FKQQ81UURVDC6gFPrgvMGEjW0qlVanMnJwGHSZghUn4ELbAIdtas0qVZzx65exkfjzJNBCephguXNelEcRKbImoZ&X-Amz-Signature=d7e7cf818061c6d6c875b8b8f06050d1f50894b866b0f2933327f1b35136ea85&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46655L5ZE5J%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141354Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJGMEQCIAVSjXHOancOkKtMyucUApCdTSmID0GdXeGay655lsuWAiBHOx3BhlH0Df9%2B8M6dgkEeqVUO%2FAGoA%2FnUkdsG%2BqwBfSr%2FAwhfEAAaDDYzNzQyMzE4MzgwNSIM27fTi5piNiZ0M1ulKtwDOhZ0polY92UUy1Lix6MdVe1tBoH7HNXjA9JGBpMSQqN9ZAZnAEsdN%2B9dH9D7tQbdZOKEuoMP2OjaBrufwIpC0gLxg6iq1AF065f%2FU7ATj7zmRLE9OoQ0jWhqr3HSDhgD5LOV44ImdtkgIQ6v%2FTM0Q9D856LYiu70Im1ptYR0ExCGUnq7ziVCzppSAhmCp8jtYHSosskLlv7MvE%2FRM%2FNxCRNjzd8QAfII0HUvgwid1ErzBVcKDoMPLJRQerAsjgNpXs8yzKJEetGuodGggFO%2BVjlBgiUpCgN0xiILY2m07lQ%2B%2FQw3yoniBtkk9l1fsfxcVEU4e7Pp%2FsNAiOz%2Bjqm6rt2GTrajwzUf2gOg4UrMNonQFJuQD7QfbMMw97%2B6dEOr0NuO8%2FU7ieMuTakCO5SYDOSweT07wZ8Fk71wLTSoXY1fE7Eys7K3%2B860exO02ivRIZIoOT%2BWACohIS22r%2B%2Ba1Tdzyrt0jN9PX7BC9w4dhgMSX%2BLzv0Ro%2FIZZu31Do5QnvUzAvztgKNQH3zMtXo0Rb6FXDZ8Vqr0U5huSUH9ENQ2Ws6nTG8A6gVuMJdzQn5oTjU801HrVz83F8rPn7h1lQHFfTX5xJ%2F9RnoOzYa9jFcdTaarbNCmQtRV6%2FnEw0vmSvQY6pgERzI0J%2F4h%2BFqugvuUdOE0HAoleGX6lLvUX33I38R8yUBdfwfelUgdAxr9KL%2BCaHkf35uMPHsKMaQzWuq05DSpKurtyiTYiw2XoNy1WdbrALLctUKfcjEAAEV3XjbNByG%2BC0O657Lh0GO7ciPC23YHMw8FDcGPgiFI1JjWf5X6REl0fC7Fu8KvG3lcXFnWRxNMwHYNcUk%2FNaVBUCLkiqDTdu%2Frq6H28&X-Amz-Signature=666ff97c9d4d9168984f74fca34ad4a420f833cd1f045c3f208d86ac84f79b22&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y744SVH4%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141354Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJGMEQCIFDC6eatwx3trFw22imPzwaEm12861dKzkhD%2FoSu%2FMIoAiB5v7LyR%2BI0Tuy9QhgbACZ87RN40foKUKL9hBkkJS%2BuLir%2FAwhfEAAaDDYzNzQyMzE4MzgwNSIMjwyh73p751F8SGZVKtwDjgC1Ge8S0X4iAxfoilT37gWYtRMRwn5BkyyjDDVYI4EmCQfBoVdtUaDt6Vt5EnvGcnD9gLUOjFbbnvEY7ZrchsDcLNevXEVNUDMmZHRIuPDh0UdZr7MIA6aaTjOLFMP2QG85XIaDKu132Fi7BGPx2eCgukG5f4VYhZl%2F%2FUyDXSalAphtqvw%2F6CfoZGvn%2BqEjnxh%2BBy4KIV24On4qwdb654wsiVmlWZ0WNBtUKPxnH3e2KdG8EOe8gz1QsdlwtdhL2RldWU8aCse9BoXthrwKvcxloR3dj7PR9xEIfGrjZtI6QNGQfXiSnI42%2BNyRXgmQZUxBkp1XzLHYX64ZVwux4coE2GwMTlV6H3qd8AbAXZyoVmaifIiqa5ocOspdQ0GmBjJgsWMp8kzlv0WQIqWopMvZCsAHFy%2BsZO3jZ8xhs2TZd9Nc%2FkVMswO2IgVFaDIl%2Fuz7F%2FAPSEvcx0HiZFeIAUDJFfznwzIaZ2d1KYJDUaf%2BSV4jT01ZHZwvjSMsAD83vXXjTmI88PGzozF0sf76yFT8QixqspVIzT6dr37dls7gM4F%2B6rSEa1Mt1YDGuRHYEQh1U4vde5S3W0%2BbxxW4ypF5q0T1ZynymDW9Jmu1GdZXho%2BUwOP7%2BTUnWlYwg%2FmSvQY6pgH%2FHBhFfaaVM%2FQjxmExwGniHcvToYUkTljGo3Dvozpm4ILNzIE%2BQf6OYnGoxCsFqBiNL4JaFGJ9r%2Bm9rgxq1rc6z6VtQPjc0P34h0vYOt76idETMoPt%2BIzJKedN5z9VkGarKMUGIDiz0Y5OxtreT7Yumt4WdeNsFuspo8sMQP70XhKBuKtljPTb5qjTLhl3U83g9kVIXkzvjYdr%2FRdq1aW20M6oprhD&X-Amz-Signature=d902e5386ed8cb5031c76b95fdf9360fa8ae09e2de83b5038b5b1eaf59a2843f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665WZ6D54K%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJHMEUCIBmC9%2FV%2FHl0pyNSLX1QU%2Fi486AOg5zfdNkbfpNXHW1otAiEAsNodMGGpxeSm3Hh9bkLjuxkWboywfT8UG6T5J13jODEq%2FwMIXxAAGgw2Mzc0MjMxODM4MDUiDEbrJu6ijJvNp168uCrcA3QK5LXW6Il16fXYtT42%2FqiONAkgMPlqpsgxg9%2B6SomuDIk7JBTWlGRZll2Y0DP6LN%2BjN%2F5SpcnRdB4VpJMqnL%2BWWCGUd3H6QbLb3McL5rkqlCSgf6qRQJQVrLkAGubFCKKyWJY67Gk5J7nufFoOJgv2o7YLXMsKixQ0CcI5vXmAbIGXnog%2FvqTRjbgOYPbvM0yRLGPASMxSpOYJKkRS59jQtMpSIGD1BkCH9X59XdXKJzxMMEraTVjZobl9Oacsd1b3cLrLBfHyrhKEDPJcH%2Ffw1sgkdUceUtWQsJJepM7UK1sgnUgQZUni4ciYUGvuSPk6AFZ3HbfCe94TJLKtNSbUYuA4hZcB1tQO6a%2FCcSdLSILF%2BGgxeZ3Kd%2F%2FkZt4%2B0Idxpy9kz5%2FOuIL42gCawhqPXZQZxU4rx9FzdA%2Bcd1ocrxSPE%2BVntAKVzfm5fDpCDwvyNGTAO%2FfIhj5EOrAyBYHXaCG%2B2LycTsS6pRCy49voPKebIrG4kMUzJ4JAoJZoSRAnF1t6MG0NbudU%2BnYeSdgVgqxiVzNkBywabytiSl2rWFf2kIR%2FjEFaNjK9aoPiKVGdK68%2BejnT86%2BBS9Z%2BCEsrm6iZolVmVW4V3cZpdLP2%2BUVzIx4lAcQjkXm3MJf5kr0GOqUBlfCxRwji0UkLmPCIPpoVdDkXnbBK%2FFtwIi4nQ1GQC6taINGU%2B2qHM2NyZzeP6nV3raV8iz6OgE1OVIIwbTF%2Fm0ZmID5s%2FSz2WVKKw0VannDdnPkazl91uGtw7IdnPzZSV3yf%2FKQQ81UURVDC6gFPrgvMGEjW0qlVanMnJwGHSZghUn4ELbAIdtas0qVZzx65exkfjzJNBCephguXNelEcRKbImoZ&X-Amz-Signature=7fb0ad29a57b2c70d830e3bdf0810d420394683a1cbe81bd8a37287c8012f920&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665WZ6D54K%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJHMEUCIBmC9%2FV%2FHl0pyNSLX1QU%2Fi486AOg5zfdNkbfpNXHW1otAiEAsNodMGGpxeSm3Hh9bkLjuxkWboywfT8UG6T5J13jODEq%2FwMIXxAAGgw2Mzc0MjMxODM4MDUiDEbrJu6ijJvNp168uCrcA3QK5LXW6Il16fXYtT42%2FqiONAkgMPlqpsgxg9%2B6SomuDIk7JBTWlGRZll2Y0DP6LN%2BjN%2F5SpcnRdB4VpJMqnL%2BWWCGUd3H6QbLb3McL5rkqlCSgf6qRQJQVrLkAGubFCKKyWJY67Gk5J7nufFoOJgv2o7YLXMsKixQ0CcI5vXmAbIGXnog%2FvqTRjbgOYPbvM0yRLGPASMxSpOYJKkRS59jQtMpSIGD1BkCH9X59XdXKJzxMMEraTVjZobl9Oacsd1b3cLrLBfHyrhKEDPJcH%2Ffw1sgkdUceUtWQsJJepM7UK1sgnUgQZUni4ciYUGvuSPk6AFZ3HbfCe94TJLKtNSbUYuA4hZcB1tQO6a%2FCcSdLSILF%2BGgxeZ3Kd%2F%2FkZt4%2B0Idxpy9kz5%2FOuIL42gCawhqPXZQZxU4rx9FzdA%2Bcd1ocrxSPE%2BVntAKVzfm5fDpCDwvyNGTAO%2FfIhj5EOrAyBYHXaCG%2B2LycTsS6pRCy49voPKebIrG4kMUzJ4JAoJZoSRAnF1t6MG0NbudU%2BnYeSdgVgqxiVzNkBywabytiSl2rWFf2kIR%2FjEFaNjK9aoPiKVGdK68%2BejnT86%2BBS9Z%2BCEsrm6iZolVmVW4V3cZpdLP2%2BUVzIx4lAcQjkXm3MJf5kr0GOqUBlfCxRwji0UkLmPCIPpoVdDkXnbBK%2FFtwIi4nQ1GQC6taINGU%2B2qHM2NyZzeP6nV3raV8iz6OgE1OVIIwbTF%2Fm0ZmID5s%2FSz2WVKKw0VannDdnPkazl91uGtw7IdnPzZSV3yf%2FKQQ81UURVDC6gFPrgvMGEjW0qlVanMnJwGHSZghUn4ELbAIdtas0qVZzx65exkfjzJNBCephguXNelEcRKbImoZ&X-Amz-Signature=b47db1917b5afb8b8915988a2021c7c3920039cc813db11e1c90f42cdf4c6504&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665WZ6D54K%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJHMEUCIBmC9%2FV%2FHl0pyNSLX1QU%2Fi486AOg5zfdNkbfpNXHW1otAiEAsNodMGGpxeSm3Hh9bkLjuxkWboywfT8UG6T5J13jODEq%2FwMIXxAAGgw2Mzc0MjMxODM4MDUiDEbrJu6ijJvNp168uCrcA3QK5LXW6Il16fXYtT42%2FqiONAkgMPlqpsgxg9%2B6SomuDIk7JBTWlGRZll2Y0DP6LN%2BjN%2F5SpcnRdB4VpJMqnL%2BWWCGUd3H6QbLb3McL5rkqlCSgf6qRQJQVrLkAGubFCKKyWJY67Gk5J7nufFoOJgv2o7YLXMsKixQ0CcI5vXmAbIGXnog%2FvqTRjbgOYPbvM0yRLGPASMxSpOYJKkRS59jQtMpSIGD1BkCH9X59XdXKJzxMMEraTVjZobl9Oacsd1b3cLrLBfHyrhKEDPJcH%2Ffw1sgkdUceUtWQsJJepM7UK1sgnUgQZUni4ciYUGvuSPk6AFZ3HbfCe94TJLKtNSbUYuA4hZcB1tQO6a%2FCcSdLSILF%2BGgxeZ3Kd%2F%2FkZt4%2B0Idxpy9kz5%2FOuIL42gCawhqPXZQZxU4rx9FzdA%2Bcd1ocrxSPE%2BVntAKVzfm5fDpCDwvyNGTAO%2FfIhj5EOrAyBYHXaCG%2B2LycTsS6pRCy49voPKebIrG4kMUzJ4JAoJZoSRAnF1t6MG0NbudU%2BnYeSdgVgqxiVzNkBywabytiSl2rWFf2kIR%2FjEFaNjK9aoPiKVGdK68%2BejnT86%2BBS9Z%2BCEsrm6iZolVmVW4V3cZpdLP2%2BUVzIx4lAcQjkXm3MJf5kr0GOqUBlfCxRwji0UkLmPCIPpoVdDkXnbBK%2FFtwIi4nQ1GQC6taINGU%2B2qHM2NyZzeP6nV3raV8iz6OgE1OVIIwbTF%2Fm0ZmID5s%2FSz2WVKKw0VannDdnPkazl91uGtw7IdnPzZSV3yf%2FKQQ81UURVDC6gFPrgvMGEjW0qlVanMnJwGHSZghUn4ELbAIdtas0qVZzx65exkfjzJNBCephguXNelEcRKbImoZ&X-Amz-Signature=2dca1c1cd265d95ae2b6592878509d7c2c4752b1897761b483c6eccbcb7dbfaa&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665WZ6D54K%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJHMEUCIBmC9%2FV%2FHl0pyNSLX1QU%2Fi486AOg5zfdNkbfpNXHW1otAiEAsNodMGGpxeSm3Hh9bkLjuxkWboywfT8UG6T5J13jODEq%2FwMIXxAAGgw2Mzc0MjMxODM4MDUiDEbrJu6ijJvNp168uCrcA3QK5LXW6Il16fXYtT42%2FqiONAkgMPlqpsgxg9%2B6SomuDIk7JBTWlGRZll2Y0DP6LN%2BjN%2F5SpcnRdB4VpJMqnL%2BWWCGUd3H6QbLb3McL5rkqlCSgf6qRQJQVrLkAGubFCKKyWJY67Gk5J7nufFoOJgv2o7YLXMsKixQ0CcI5vXmAbIGXnog%2FvqTRjbgOYPbvM0yRLGPASMxSpOYJKkRS59jQtMpSIGD1BkCH9X59XdXKJzxMMEraTVjZobl9Oacsd1b3cLrLBfHyrhKEDPJcH%2Ffw1sgkdUceUtWQsJJepM7UK1sgnUgQZUni4ciYUGvuSPk6AFZ3HbfCe94TJLKtNSbUYuA4hZcB1tQO6a%2FCcSdLSILF%2BGgxeZ3Kd%2F%2FkZt4%2B0Idxpy9kz5%2FOuIL42gCawhqPXZQZxU4rx9FzdA%2Bcd1ocrxSPE%2BVntAKVzfm5fDpCDwvyNGTAO%2FfIhj5EOrAyBYHXaCG%2B2LycTsS6pRCy49voPKebIrG4kMUzJ4JAoJZoSRAnF1t6MG0NbudU%2BnYeSdgVgqxiVzNkBywabytiSl2rWFf2kIR%2FjEFaNjK9aoPiKVGdK68%2BejnT86%2BBS9Z%2BCEsrm6iZolVmVW4V3cZpdLP2%2BUVzIx4lAcQjkXm3MJf5kr0GOqUBlfCxRwji0UkLmPCIPpoVdDkXnbBK%2FFtwIi4nQ1GQC6taINGU%2B2qHM2NyZzeP6nV3raV8iz6OgE1OVIIwbTF%2Fm0ZmID5s%2FSz2WVKKw0VannDdnPkazl91uGtw7IdnPzZSV3yf%2FKQQ81UURVDC6gFPrgvMGEjW0qlVanMnJwGHSZghUn4ELbAIdtas0qVZzx65exkfjzJNBCephguXNelEcRKbImoZ&X-Amz-Signature=5b30a2752f2630172a88c1d96826f32457c470721f2fbac749909b03214c76b0&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
