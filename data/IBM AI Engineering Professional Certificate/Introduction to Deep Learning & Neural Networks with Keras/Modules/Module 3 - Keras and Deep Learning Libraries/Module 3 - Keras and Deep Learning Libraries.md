

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V2XO575H%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJGMEQCIARjrBJon5ZoIvrKG83O6%2Ff3QlaLZZB3yIzLcFCxZ43aAiBLPQvakIQX2DDBa5nw048AWBPoFuB6amt5KKHKgg5vzSr%2FAwhAEAAaDDYzNzQyMzE4MzgwNSIMGO92qY1PGn9J8uwUKtwDV%2FwrwSPurKsci55EH%2FTSqisZ9re1W%2FwlBiBZSutO7cQzrUcZxIby69am3j0RPxaOhkmy0CRbhFuqQipnoAABpHMm5eB%2BwMmoQ3sBV3eBzX0gaU%2BykJjB5NhvuzEoUWWFpTb1YYQ%2BcCWWEt66Me9Wc2daq5x5rIzjVQkt%2FKbfhneEcJz8Dxmrw5UzvNQpe8jL1spNuLnn2wOiD4%2FpM2f8NJO4aQYwHk3c5uIg7l4Kxcqu7carrpyxpPk%2BZl4jbj%2BacNRck2pW0%2BYDwf9C2fgpq5a9MAFLBNJtncV8vOZ7VG%2Flilr0fZgX1XJG0JdF%2FdOBiED0KePTapn4p6pVlJeB8AqIQ3nbBApPWBUE%2BYu1v9%2FfKcMawlzXSxcrdk6H2G%2BllUpX5%2Bv1ytDyaFXuGDMor%2FwI0piLol%2Fhyss%2FhGprSPdngzZrlXKFTAyjXzG%2FtAj633ucWhVq3vFWzRJsW3IMcyJjTFq0%2B1HQG1n5X1BPczED%2ByjKpZxEmREVoToy6Bia%2BvqBT7OsLaFzhLxzdnjkKt9irxcJkwMTlPP830SO4OzR84aHB3IrCaqxsfRp44trlv%2BYjMfBRUh2LkS6UlKEjev95q4Eyyn0ZOf8Xya%2B2ovBk4kR69zH%2BibcVT8wpJaMvQY6pgG84CZA32KJFZTFh9PejyiEC%2BR8tQ39jJERWodl2u2cytBO86xAwmDyfYvxoQJedHuIpZtIkQuQrcgFuzr%2Fxc6LfvupM5kqUx7a0wKX6%2F49AoURMl7arD2TvpMITJaBLJr1q%2FtI2vCas45FievSPGEOUhpeT6UMmCJsgRumAGj0u9qAlERtLhXwoAyiLdH4Cp5PiK%2FYLvWMbPWnWbEiS41lk1cz8zUY&X-Amz-Signature=357d1e32f04d915a98833e09408dab55ba1d1807917156ed6a789c29dd3f2382&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V2XO575H%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJGMEQCIARjrBJon5ZoIvrKG83O6%2Ff3QlaLZZB3yIzLcFCxZ43aAiBLPQvakIQX2DDBa5nw048AWBPoFuB6amt5KKHKgg5vzSr%2FAwhAEAAaDDYzNzQyMzE4MzgwNSIMGO92qY1PGn9J8uwUKtwDV%2FwrwSPurKsci55EH%2FTSqisZ9re1W%2FwlBiBZSutO7cQzrUcZxIby69am3j0RPxaOhkmy0CRbhFuqQipnoAABpHMm5eB%2BwMmoQ3sBV3eBzX0gaU%2BykJjB5NhvuzEoUWWFpTb1YYQ%2BcCWWEt66Me9Wc2daq5x5rIzjVQkt%2FKbfhneEcJz8Dxmrw5UzvNQpe8jL1spNuLnn2wOiD4%2FpM2f8NJO4aQYwHk3c5uIg7l4Kxcqu7carrpyxpPk%2BZl4jbj%2BacNRck2pW0%2BYDwf9C2fgpq5a9MAFLBNJtncV8vOZ7VG%2Flilr0fZgX1XJG0JdF%2FdOBiED0KePTapn4p6pVlJeB8AqIQ3nbBApPWBUE%2BYu1v9%2FfKcMawlzXSxcrdk6H2G%2BllUpX5%2Bv1ytDyaFXuGDMor%2FwI0piLol%2Fhyss%2FhGprSPdngzZrlXKFTAyjXzG%2FtAj633ucWhVq3vFWzRJsW3IMcyJjTFq0%2B1HQG1n5X1BPczED%2ByjKpZxEmREVoToy6Bia%2BvqBT7OsLaFzhLxzdnjkKt9irxcJkwMTlPP830SO4OzR84aHB3IrCaqxsfRp44trlv%2BYjMfBRUh2LkS6UlKEjev95q4Eyyn0ZOf8Xya%2B2ovBk4kR69zH%2BibcVT8wpJaMvQY6pgG84CZA32KJFZTFh9PejyiEC%2BR8tQ39jJERWodl2u2cytBO86xAwmDyfYvxoQJedHuIpZtIkQuQrcgFuzr%2Fxc6LfvupM5kqUx7a0wKX6%2F49AoURMl7arD2TvpMITJaBLJr1q%2FtI2vCas45FievSPGEOUhpeT6UMmCJsgRumAGj0u9qAlERtLhXwoAyiLdH4Cp5PiK%2FYLvWMbPWnWbEiS41lk1cz8zUY&X-Amz-Signature=f1db9960c729bfd3d54581436ca330736fa141bee2f351e3fd70c89845325aa6&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V2XO575H%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJGMEQCIARjrBJon5ZoIvrKG83O6%2Ff3QlaLZZB3yIzLcFCxZ43aAiBLPQvakIQX2DDBa5nw048AWBPoFuB6amt5KKHKgg5vzSr%2FAwhAEAAaDDYzNzQyMzE4MzgwNSIMGO92qY1PGn9J8uwUKtwDV%2FwrwSPurKsci55EH%2FTSqisZ9re1W%2FwlBiBZSutO7cQzrUcZxIby69am3j0RPxaOhkmy0CRbhFuqQipnoAABpHMm5eB%2BwMmoQ3sBV3eBzX0gaU%2BykJjB5NhvuzEoUWWFpTb1YYQ%2BcCWWEt66Me9Wc2daq5x5rIzjVQkt%2FKbfhneEcJz8Dxmrw5UzvNQpe8jL1spNuLnn2wOiD4%2FpM2f8NJO4aQYwHk3c5uIg7l4Kxcqu7carrpyxpPk%2BZl4jbj%2BacNRck2pW0%2BYDwf9C2fgpq5a9MAFLBNJtncV8vOZ7VG%2Flilr0fZgX1XJG0JdF%2FdOBiED0KePTapn4p6pVlJeB8AqIQ3nbBApPWBUE%2BYu1v9%2FfKcMawlzXSxcrdk6H2G%2BllUpX5%2Bv1ytDyaFXuGDMor%2FwI0piLol%2Fhyss%2FhGprSPdngzZrlXKFTAyjXzG%2FtAj633ucWhVq3vFWzRJsW3IMcyJjTFq0%2B1HQG1n5X1BPczED%2ByjKpZxEmREVoToy6Bia%2BvqBT7OsLaFzhLxzdnjkKt9irxcJkwMTlPP830SO4OzR84aHB3IrCaqxsfRp44trlv%2BYjMfBRUh2LkS6UlKEjev95q4Eyyn0ZOf8Xya%2B2ovBk4kR69zH%2BibcVT8wpJaMvQY6pgG84CZA32KJFZTFh9PejyiEC%2BR8tQ39jJERWodl2u2cytBO86xAwmDyfYvxoQJedHuIpZtIkQuQrcgFuzr%2Fxc6LfvupM5kqUx7a0wKX6%2F49AoURMl7arD2TvpMITJaBLJr1q%2FtI2vCas45FievSPGEOUhpeT6UMmCJsgRumAGj0u9qAlERtLhXwoAyiLdH4Cp5PiK%2FYLvWMbPWnWbEiS41lk1cz8zUY&X-Amz-Signature=4ca3c480f15dbb79c722a255f74511a629c4e9376fa3738b5e2ad173b52a6c0b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USJCCPW6%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJIMEYCIQD6bhsu9ClpnKu87lOW995Spwy%2F0wDw766u7SDUSEeyeQIhAP%2FeXbFx5Dza9sE8GJNaYOG8WlPxgElq2oyuuZu8HtXIKv8DCEAQABoMNjM3NDIzMTgzODA1Igwc%2B9DgjBigsF%2FeavMq3ANwgaGGf8%2Bl%2FlQcXapdS5ShVU7AEcEPsuA4EgyZTpjjJiicyZyLQV2T6mqpRh3locJ3QIjf3vF9D4g2LPzEMscOmkmf%2B%2Fcsm6XvjpvD9xhWyns%2BBBi1rjV8XdK7JXXNA%2Fz6ppcOUbEV7BYiRRKuVrYN2DlmK3AUerIhg7HrR9YCY56%2FDR4I%2BgexMXv%2FTLqwmBJuxp5dB2VayeY%2FDETPDH11sm%2BNgRfm9uJ0SE0NnRhtU7cDcoLzj%2FPHsJilG5RlbcBaqDg24x1UiEltF9OiF3wXhXcjMWDz7CnxRi0PAAI6zikQxNDDFONGiV4QHmDV4NULaH%2F48gU%2BkjM3pmO%2BZVlTlpyd8J1Z2hIDV40b1Txz7OVfYMMmN9HD%2FLFvQ9Mbc5%2FLT%2BLAZ1gQ1gQASPaioW23ibueWUg3qfTM6DIIH%2BS7Y%2Ft5qwt72b1hOExCZvlkTWLuIO9llxwqUqdGf9yITsSGno7NNMGjXZCHTKZgUJDFiA4wxxh8Vm0h7d3GttgiftPoT7k7hOZ2Y9SS9DzOy%2FnYpROXILmANJqhVw0%2Fk2j4jgyhx8vXe331U8QYnhV%2Bj8ZvbW2HvA7ogEDlmBC%2F2ZnF9woxpu8Jc1U5OLu8VxXMzAfYgU6gt46PGbgBMjD9lYy9BjqkAaO%2Fd3a%2B%2Fn5a5Ox6YrnJOD%2Bp3FlrK8uoFFpmm7U40of3sDmkwW9EGQlVtAgKIn7qu4h86AZQFKlt8oc9KMhH7GuerwMS7oZohoxPbSKPXYOLBbrnGJnbP7rQue6OSbYtdq9xMhZ7sSVf508ffPtk%2FiAfwLbviIoSxezjUB1Vu0PcPjxSV2n4bmTOeZMoxwaphJ8ZeWh%2FtXWtaqXJ72JlPgpoek6J&X-Amz-Signature=16827cd8aec82df0de55ce316226a16f427d611e2695dd161f657a909b362503&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V6DF4AT7%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJHMEUCIQDXRg0GblYXzk1HCzbte%2BgM3QebvAXmOcyVyNIPuDde5wIgPWMFUZCSuDl7SJQKRX79nCRJXicspfuRZT2vU1K1qlEq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDBwkfGBm5zxIMmxjQyrcA4TmvAsULG5IFExuvnuMvz3y92QO%2BFd%2FajHZ340nD7ojft9BJoCvlycomfOU5Pxw3jU0psnJHO8caXuyaYTKLB%2BC9FCKkNmQWTgvqJj1sSIYEgg7j%2FN4QE8edibVCtsLhOBgrhUa6qaOCEyyraTWRMpibiR2V34yTe2tZTsw6NV%2FeSK%2BZJ9FwWgMI42piTmu8Ol4Ql7UCGT2PjscDTGqezPYOWx6K8Z4q7h5C7qRCvlQwFBDp69hjbs3Y3dg3Gju9IUkmPHXhdTwofCzXKuoefNFbOmDc9kK4EFUbNJGbsvJQCxNeApzN%2FV5ifFGLR7rmnFndSBvtEGCbHblhxaFfeV%2FZxJgiBQJPZuh7k4vzOrf9rJY2xCGv%2FcM0eKI1rhkz4Tl2wTu695fhwnNhjssr2seB%2BDMp7BSrYc8nATMOvU2J%2F%2B7Prkty6wiNxY%2BE7LfiMWbx%2BA58lmTxag9aon90D3JrLRn85Jv%2BinShNGsmwt4q2R9Cp1t024rRaKBysbMVGk5PWBgsDaNv5yiD8icQNkcoe5sZbhWItUfT9corNqhPv3uaLFvqvgVWA8dJRgjWQ%2F3gFnC3pxRHuc0j4HyH1PZXIJH0zsCKOB%2BzryaB2RhAOp0mGaE2h2GnN%2F%2BMPWVjL0GOqUBbb1ZtZkydXjpnogvhN%2Bts1nSIv9hNbS6hz%2FjwKa5JeoJ3QBJQnsN3aqP%2FsZ8gt1lZXtJ3w7hREAjWG53%2Bb6En%2FxNt9OIDwxboYWPENIFOGHAxmfhdTrTQd%2F7vqpzqR1SzpU7JEAEwPjWg8cMcbfa22%2BA9QGn6m%2FqZP7ua08btqU%2BdDLv1m8VUasVevu%2F%2B9nIU9w0nJ6Tlei12SpffUdt9tlYv%2BzZ&X-Amz-Signature=3382797963bece516bc8cec794d5fc16c540c9f6c158696e84a42c3c4748282f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V2XO575H%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJGMEQCIARjrBJon5ZoIvrKG83O6%2Ff3QlaLZZB3yIzLcFCxZ43aAiBLPQvakIQX2DDBa5nw048AWBPoFuB6amt5KKHKgg5vzSr%2FAwhAEAAaDDYzNzQyMzE4MzgwNSIMGO92qY1PGn9J8uwUKtwDV%2FwrwSPurKsci55EH%2FTSqisZ9re1W%2FwlBiBZSutO7cQzrUcZxIby69am3j0RPxaOhkmy0CRbhFuqQipnoAABpHMm5eB%2BwMmoQ3sBV3eBzX0gaU%2BykJjB5NhvuzEoUWWFpTb1YYQ%2BcCWWEt66Me9Wc2daq5x5rIzjVQkt%2FKbfhneEcJz8Dxmrw5UzvNQpe8jL1spNuLnn2wOiD4%2FpM2f8NJO4aQYwHk3c5uIg7l4Kxcqu7carrpyxpPk%2BZl4jbj%2BacNRck2pW0%2BYDwf9C2fgpq5a9MAFLBNJtncV8vOZ7VG%2Flilr0fZgX1XJG0JdF%2FdOBiED0KePTapn4p6pVlJeB8AqIQ3nbBApPWBUE%2BYu1v9%2FfKcMawlzXSxcrdk6H2G%2BllUpX5%2Bv1ytDyaFXuGDMor%2FwI0piLol%2Fhyss%2FhGprSPdngzZrlXKFTAyjXzG%2FtAj633ucWhVq3vFWzRJsW3IMcyJjTFq0%2B1HQG1n5X1BPczED%2ByjKpZxEmREVoToy6Bia%2BvqBT7OsLaFzhLxzdnjkKt9irxcJkwMTlPP830SO4OzR84aHB3IrCaqxsfRp44trlv%2BYjMfBRUh2LkS6UlKEjev95q4Eyyn0ZOf8Xya%2B2ovBk4kR69zH%2BibcVT8wpJaMvQY6pgG84CZA32KJFZTFh9PejyiEC%2BR8tQ39jJERWodl2u2cytBO86xAwmDyfYvxoQJedHuIpZtIkQuQrcgFuzr%2Fxc6LfvupM5kqUx7a0wKX6%2F49AoURMl7arD2TvpMITJaBLJr1q%2FtI2vCas45FievSPGEOUhpeT6UMmCJsgRumAGj0u9qAlERtLhXwoAyiLdH4Cp5PiK%2FYLvWMbPWnWbEiS41lk1cz8zUY&X-Amz-Signature=e6667079335ae0309a639a361975dc9650ad36b06f409d682d87df8495b0415b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V2XO575H%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJGMEQCIARjrBJon5ZoIvrKG83O6%2Ff3QlaLZZB3yIzLcFCxZ43aAiBLPQvakIQX2DDBa5nw048AWBPoFuB6amt5KKHKgg5vzSr%2FAwhAEAAaDDYzNzQyMzE4MzgwNSIMGO92qY1PGn9J8uwUKtwDV%2FwrwSPurKsci55EH%2FTSqisZ9re1W%2FwlBiBZSutO7cQzrUcZxIby69am3j0RPxaOhkmy0CRbhFuqQipnoAABpHMm5eB%2BwMmoQ3sBV3eBzX0gaU%2BykJjB5NhvuzEoUWWFpTb1YYQ%2BcCWWEt66Me9Wc2daq5x5rIzjVQkt%2FKbfhneEcJz8Dxmrw5UzvNQpe8jL1spNuLnn2wOiD4%2FpM2f8NJO4aQYwHk3c5uIg7l4Kxcqu7carrpyxpPk%2BZl4jbj%2BacNRck2pW0%2BYDwf9C2fgpq5a9MAFLBNJtncV8vOZ7VG%2Flilr0fZgX1XJG0JdF%2FdOBiED0KePTapn4p6pVlJeB8AqIQ3nbBApPWBUE%2BYu1v9%2FfKcMawlzXSxcrdk6H2G%2BllUpX5%2Bv1ytDyaFXuGDMor%2FwI0piLol%2Fhyss%2FhGprSPdngzZrlXKFTAyjXzG%2FtAj633ucWhVq3vFWzRJsW3IMcyJjTFq0%2B1HQG1n5X1BPczED%2ByjKpZxEmREVoToy6Bia%2BvqBT7OsLaFzhLxzdnjkKt9irxcJkwMTlPP830SO4OzR84aHB3IrCaqxsfRp44trlv%2BYjMfBRUh2LkS6UlKEjev95q4Eyyn0ZOf8Xya%2B2ovBk4kR69zH%2BibcVT8wpJaMvQY6pgG84CZA32KJFZTFh9PejyiEC%2BR8tQ39jJERWodl2u2cytBO86xAwmDyfYvxoQJedHuIpZtIkQuQrcgFuzr%2Fxc6LfvupM5kqUx7a0wKX6%2F49AoURMl7arD2TvpMITJaBLJr1q%2FtI2vCas45FievSPGEOUhpeT6UMmCJsgRumAGj0u9qAlERtLhXwoAyiLdH4Cp5PiK%2FYLvWMbPWnWbEiS41lk1cz8zUY&X-Amz-Signature=78e613445f900f5cd5ae74c49c1c7db3f11a88fd1720cb1783f66e233973640f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V2XO575H%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJGMEQCIARjrBJon5ZoIvrKG83O6%2Ff3QlaLZZB3yIzLcFCxZ43aAiBLPQvakIQX2DDBa5nw048AWBPoFuB6amt5KKHKgg5vzSr%2FAwhAEAAaDDYzNzQyMzE4MzgwNSIMGO92qY1PGn9J8uwUKtwDV%2FwrwSPurKsci55EH%2FTSqisZ9re1W%2FwlBiBZSutO7cQzrUcZxIby69am3j0RPxaOhkmy0CRbhFuqQipnoAABpHMm5eB%2BwMmoQ3sBV3eBzX0gaU%2BykJjB5NhvuzEoUWWFpTb1YYQ%2BcCWWEt66Me9Wc2daq5x5rIzjVQkt%2FKbfhneEcJz8Dxmrw5UzvNQpe8jL1spNuLnn2wOiD4%2FpM2f8NJO4aQYwHk3c5uIg7l4Kxcqu7carrpyxpPk%2BZl4jbj%2BacNRck2pW0%2BYDwf9C2fgpq5a9MAFLBNJtncV8vOZ7VG%2Flilr0fZgX1XJG0JdF%2FdOBiED0KePTapn4p6pVlJeB8AqIQ3nbBApPWBUE%2BYu1v9%2FfKcMawlzXSxcrdk6H2G%2BllUpX5%2Bv1ytDyaFXuGDMor%2FwI0piLol%2Fhyss%2FhGprSPdngzZrlXKFTAyjXzG%2FtAj633ucWhVq3vFWzRJsW3IMcyJjTFq0%2B1HQG1n5X1BPczED%2ByjKpZxEmREVoToy6Bia%2BvqBT7OsLaFzhLxzdnjkKt9irxcJkwMTlPP830SO4OzR84aHB3IrCaqxsfRp44trlv%2BYjMfBRUh2LkS6UlKEjev95q4Eyyn0ZOf8Xya%2B2ovBk4kR69zH%2BibcVT8wpJaMvQY6pgG84CZA32KJFZTFh9PejyiEC%2BR8tQ39jJERWodl2u2cytBO86xAwmDyfYvxoQJedHuIpZtIkQuQrcgFuzr%2Fxc6LfvupM5kqUx7a0wKX6%2F49AoURMl7arD2TvpMITJaBLJr1q%2FtI2vCas45FievSPGEOUhpeT6UMmCJsgRumAGj0u9qAlERtLhXwoAyiLdH4Cp5PiK%2FYLvWMbPWnWbEiS41lk1cz8zUY&X-Amz-Signature=d3ff583719c9b85c50a1111619db9408eac1299794ea0f05a0bfdcfaf9f23aa7&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V2XO575H%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJGMEQCIARjrBJon5ZoIvrKG83O6%2Ff3QlaLZZB3yIzLcFCxZ43aAiBLPQvakIQX2DDBa5nw048AWBPoFuB6amt5KKHKgg5vzSr%2FAwhAEAAaDDYzNzQyMzE4MzgwNSIMGO92qY1PGn9J8uwUKtwDV%2FwrwSPurKsci55EH%2FTSqisZ9re1W%2FwlBiBZSutO7cQzrUcZxIby69am3j0RPxaOhkmy0CRbhFuqQipnoAABpHMm5eB%2BwMmoQ3sBV3eBzX0gaU%2BykJjB5NhvuzEoUWWFpTb1YYQ%2BcCWWEt66Me9Wc2daq5x5rIzjVQkt%2FKbfhneEcJz8Dxmrw5UzvNQpe8jL1spNuLnn2wOiD4%2FpM2f8NJO4aQYwHk3c5uIg7l4Kxcqu7carrpyxpPk%2BZl4jbj%2BacNRck2pW0%2BYDwf9C2fgpq5a9MAFLBNJtncV8vOZ7VG%2Flilr0fZgX1XJG0JdF%2FdOBiED0KePTapn4p6pVlJeB8AqIQ3nbBApPWBUE%2BYu1v9%2FfKcMawlzXSxcrdk6H2G%2BllUpX5%2Bv1ytDyaFXuGDMor%2FwI0piLol%2Fhyss%2FhGprSPdngzZrlXKFTAyjXzG%2FtAj633ucWhVq3vFWzRJsW3IMcyJjTFq0%2B1HQG1n5X1BPczED%2ByjKpZxEmREVoToy6Bia%2BvqBT7OsLaFzhLxzdnjkKt9irxcJkwMTlPP830SO4OzR84aHB3IrCaqxsfRp44trlv%2BYjMfBRUh2LkS6UlKEjev95q4Eyyn0ZOf8Xya%2B2ovBk4kR69zH%2BibcVT8wpJaMvQY6pgG84CZA32KJFZTFh9PejyiEC%2BR8tQ39jJERWodl2u2cytBO86xAwmDyfYvxoQJedHuIpZtIkQuQrcgFuzr%2Fxc6LfvupM5kqUx7a0wKX6%2F49AoURMl7arD2TvpMITJaBLJr1q%2FtI2vCas45FievSPGEOUhpeT6UMmCJsgRumAGj0u9qAlERtLhXwoAyiLdH4Cp5PiK%2FYLvWMbPWnWbEiS41lk1cz8zUY&X-Amz-Signature=d0bdbdbc1d2afd5662506f8421f1c8fe7e595a133ab63baa581d396cdca2a13b&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
