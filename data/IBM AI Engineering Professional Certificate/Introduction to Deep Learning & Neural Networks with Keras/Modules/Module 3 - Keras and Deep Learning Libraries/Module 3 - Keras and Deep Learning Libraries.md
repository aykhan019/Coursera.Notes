

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46655SWONPT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIFkH0WPtsow2WrWGdnMW21co1wCJArCg9wZyKKim%2FfcbAiEAjwFN6gGmlQEZKEXmlqRXuHY47cKXIsF4MKfALiKW1ncq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDB%2FbURPw7c4e0ckwBCrcA49wUg1Rr0UUaCmBzwofwyXcpcc3jAv%2FQ2%2ByL3kXemYP64M8sKiofYnvL%2F4guk6ob1NW5rQLxC7qXMjNfOqbnKTF5pYAUZ2mpJMcw%2Fjuq8sGK5fCaDXs2tFgRg%2Fv8lCmclHOZ1XjAwVaK5m%2F8gWjyljqxCyD0HHCCPREIsC2oB7pM3EZ2EMz0eBAKELK4%2FaAmr3cg3tADMsPRiYAS%2FOnuWKst%2FW9yL285ECBROjq8bZ%2FvXFH%2B0xvM0XR1tdZVcKs0%2F%2BCfXd1N9rMkvnxQZnLrWUxqjHigaNutK6MGpllYpczf404xe2opbrV3i%2F0uv2dq05VxMBRmWhQqOgRvNkyCdCLNKraoTsK86cBB%2FawNA%2F6DRXC7BmVjz8NUcrhrNPE%2FdkXBz%2BO2vtns%2BI%2FuXu55JxWSch6uk8ykgvtx1fLu89x0GtXe5UoV3sAIHfZfXz6YvcOfZxfmrUk5AKmHdGL6xhusQUe0%2Ft1R8rNK2n8QiPmu9yjQ2iuMvl2uEwuNryywRS48tEO4SOHKky%2BbffGam2xLW1gQiXzgYdu9kF7Lj1FKqW3dCLe2%2BKsYxzkE7FBAOHSXyx8DVyHaOPWubxxcHQX3WCpboknZg%2BECB7qk1m0RrTiDgEX1nenigk2MKP5i70GOqUBFVDKuzrNohHWV0cgewHoRfU%2FquVx201fhxLn4tG43Op91m%2FVC9rtizog%2B4R8Zt7XzSkFfUhN8qDe7noWQ%2BC%2BuYF7ZdYKz%2Fg8%2Fv1h7BfZg8C%2FkNJxmtBQqhHzsRB5vtAiwbikrJx9DGwOF2cb1wi2KBsqCfF1IT9a8MVmNXBeXmPSeXPVaawassiEiwcsVwTXIfhIBDYYSo8UcDaVQP2MpeJNtxzg&X-Amz-Signature=24ccb7da485f5eabe968be3f9d12e5cd0d09ebcf49fe15418c82d5ea5a0592ab&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46655SWONPT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIFkH0WPtsow2WrWGdnMW21co1wCJArCg9wZyKKim%2FfcbAiEAjwFN6gGmlQEZKEXmlqRXuHY47cKXIsF4MKfALiKW1ncq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDB%2FbURPw7c4e0ckwBCrcA49wUg1Rr0UUaCmBzwofwyXcpcc3jAv%2FQ2%2ByL3kXemYP64M8sKiofYnvL%2F4guk6ob1NW5rQLxC7qXMjNfOqbnKTF5pYAUZ2mpJMcw%2Fjuq8sGK5fCaDXs2tFgRg%2Fv8lCmclHOZ1XjAwVaK5m%2F8gWjyljqxCyD0HHCCPREIsC2oB7pM3EZ2EMz0eBAKELK4%2FaAmr3cg3tADMsPRiYAS%2FOnuWKst%2FW9yL285ECBROjq8bZ%2FvXFH%2B0xvM0XR1tdZVcKs0%2F%2BCfXd1N9rMkvnxQZnLrWUxqjHigaNutK6MGpllYpczf404xe2opbrV3i%2F0uv2dq05VxMBRmWhQqOgRvNkyCdCLNKraoTsK86cBB%2FawNA%2F6DRXC7BmVjz8NUcrhrNPE%2FdkXBz%2BO2vtns%2BI%2FuXu55JxWSch6uk8ykgvtx1fLu89x0GtXe5UoV3sAIHfZfXz6YvcOfZxfmrUk5AKmHdGL6xhusQUe0%2Ft1R8rNK2n8QiPmu9yjQ2iuMvl2uEwuNryywRS48tEO4SOHKky%2BbffGam2xLW1gQiXzgYdu9kF7Lj1FKqW3dCLe2%2BKsYxzkE7FBAOHSXyx8DVyHaOPWubxxcHQX3WCpboknZg%2BECB7qk1m0RrTiDgEX1nenigk2MKP5i70GOqUBFVDKuzrNohHWV0cgewHoRfU%2FquVx201fhxLn4tG43Op91m%2FVC9rtizog%2B4R8Zt7XzSkFfUhN8qDe7noWQ%2BC%2BuYF7ZdYKz%2Fg8%2Fv1h7BfZg8C%2FkNJxmtBQqhHzsRB5vtAiwbikrJx9DGwOF2cb1wi2KBsqCfF1IT9a8MVmNXBeXmPSeXPVaawassiEiwcsVwTXIfhIBDYYSo8UcDaVQP2MpeJNtxzg&X-Amz-Signature=c4a3a06f0361a30aa6f7e69820e15547a79dc1add644e9fb80ab22700b7bc337&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46655SWONPT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIFkH0WPtsow2WrWGdnMW21co1wCJArCg9wZyKKim%2FfcbAiEAjwFN6gGmlQEZKEXmlqRXuHY47cKXIsF4MKfALiKW1ncq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDB%2FbURPw7c4e0ckwBCrcA49wUg1Rr0UUaCmBzwofwyXcpcc3jAv%2FQ2%2ByL3kXemYP64M8sKiofYnvL%2F4guk6ob1NW5rQLxC7qXMjNfOqbnKTF5pYAUZ2mpJMcw%2Fjuq8sGK5fCaDXs2tFgRg%2Fv8lCmclHOZ1XjAwVaK5m%2F8gWjyljqxCyD0HHCCPREIsC2oB7pM3EZ2EMz0eBAKELK4%2FaAmr3cg3tADMsPRiYAS%2FOnuWKst%2FW9yL285ECBROjq8bZ%2FvXFH%2B0xvM0XR1tdZVcKs0%2F%2BCfXd1N9rMkvnxQZnLrWUxqjHigaNutK6MGpllYpczf404xe2opbrV3i%2F0uv2dq05VxMBRmWhQqOgRvNkyCdCLNKraoTsK86cBB%2FawNA%2F6DRXC7BmVjz8NUcrhrNPE%2FdkXBz%2BO2vtns%2BI%2FuXu55JxWSch6uk8ykgvtx1fLu89x0GtXe5UoV3sAIHfZfXz6YvcOfZxfmrUk5AKmHdGL6xhusQUe0%2Ft1R8rNK2n8QiPmu9yjQ2iuMvl2uEwuNryywRS48tEO4SOHKky%2BbffGam2xLW1gQiXzgYdu9kF7Lj1FKqW3dCLe2%2BKsYxzkE7FBAOHSXyx8DVyHaOPWubxxcHQX3WCpboknZg%2BECB7qk1m0RrTiDgEX1nenigk2MKP5i70GOqUBFVDKuzrNohHWV0cgewHoRfU%2FquVx201fhxLn4tG43Op91m%2FVC9rtizog%2B4R8Zt7XzSkFfUhN8qDe7noWQ%2BC%2BuYF7ZdYKz%2Fg8%2Fv1h7BfZg8C%2FkNJxmtBQqhHzsRB5vtAiwbikrJx9DGwOF2cb1wi2KBsqCfF1IT9a8MVmNXBeXmPSeXPVaawassiEiwcsVwTXIfhIBDYYSo8UcDaVQP2MpeJNtxzg&X-Amz-Signature=8fb4f700214c4aefc3893bff777e8cc446a19a9af1dab53c950b403adf77bafb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46673POAJ6E%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJGMEQCIE1aPAjiNdXY321UU9Pcnwm%2Bc2lzs7BJFPjWSWk%2BKk8eAiAoRIO3BSHPH079iiM00X8vow4MZVUpWJy4i5qMqrkFJyr%2FAwg%2FEAAaDDYzNzQyMzE4MzgwNSIMjj5HMe0XjNIbRqjcKtwDFs9UcJ9duG5bndr%2FNwtLpsTgCxH3%2Bj8T8q%2FnKLwGidd3jsSVsQdN%2FZQQOHsNCoHVSAjpFZCjcq72tsZIlrY2m81qJ1FLQxXyCKuqixwSUqbQHucTJXFjg0SzOLRfu80ahvtYqgXw7CZQrxq5%2F2ZrBm3NurJhCSVzcc8%2FBuTEKqzZMQxf7uBoZnZI7dzUnBVP9imRjh3rI5DuyDT6oLoC7E9ifBO2Srn%2BRVY5jKVphwvk2mSOaaMhaSpRKsts0ZDYXLNw7RMK2JIUAkt2FYV0e1qpRgExb6NS3oKe4JnFsCQH5kJDPzOuFQ3x6nXsgstmBStOFpqMxQDiMWcZcuhVoYA2Al9Oko7a2L%2FsUN9cUwi3VvPQg1jUlj39j%2F1ady%2BbmvhkiWM%2B4vD1qQUc9Dd5hXF7qYSbwiyna6YM2pMa5jpNJq8Ewv29%2FKVy0zjv5g0E%2BhXZXKp2KCV%2FsIgvq6AgkebcWAKTjZOlg6r76SzT3moYuwt%2FzfjBKBxskr50clj%2BIj494Zn5u7UjqVLcrwFz%2BHNtiHgMua4stO%2BflO%2FJYzGngKwPkDNkYeUOsEjKuXEgRtxiD1d0%2FSnHldOttmon2i2YZC4AEwnoWynT1NHpnXi2g0A9dT%2F7dMbMhoUw%2F%2FmLvQY6pgFokYx8pL60%2BjmJQEicWIwu229DoeUVEmlRFpZMTteZbLC1dJFJhdkjRcBZ1Rwr0bdKmGH8thq0b95nWue0ZXdnzZm%2FXnUE7XOd5%2BkPGpxpr%2BU5njD7zoMPpnaPeAmgqixmyzIcofvos0lUAzb735YprnnNA4A%2BDn0oQmi9eTVo3aaiIAcq1seLMKAaNZg%2Be0pWnptgZ2A9EPgR%2B2cVQxIt0vw%2BBjX3&X-Amz-Signature=531d39af0dc7385c5a6e71f4cfa9c40ddf0064b83269e84d7140f1337be77c31&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46667QOOLEI%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIE69chON1zkejk5XEqyv7APWgyIpQHd8y4WPXKj7eTLlAiEAvWruUJe62jpQj%2FbL1p%2BRTIv3QKbpO0eJArvA0LngBbYq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDAL3OexMVUJBQk49LSrcAxNRqy4H3BRzdAjbxzP9VtrD%2F9NJ%2FU7k3ucEkDrGwEh%2FhWTxWKMIWoO1xcIN49NvlvR3Hr6MUxIy8AFqOgohJLeTjJ5%2F3dP%2FUNZnhWEMRqIF617EePl0nevagliivJ6guQ6bcqAj21tveYoFEBnoJ1dtPNA8n4sF6%2FsmGTlbKnKRuDI0FkTmHwFSIUA1cx%2FtugbSH099ugV4vNprppNRunBOgp6MZGJrqkV0lXJiAZQvHgQvuE2wBoWux%2BtMqv%2FrDaSOW7fRrB3zhOJTwsdUVn6%2Fe5eqLsl1N8qPdU1%2BoYioPK6U6e8Fc%2BhJDvzwVmllh3H9QuGGiDoL8tcsDNM8AqpdETjXy7mXnmLIhMBS1yqEPZcpFWARcQaHwAn37z%2B5zfxEcf0EOUwiCotC%2BZlS6AZto24dXT0XDOENuB5YGAPv6G7Vk1%2F9UC%2BfsZFXXlY4C68FwiFRjsX2CwVqGIbpvfeGjOq93v1EIJK0S2CVJvR2WnZkJ38eJgyN0hXmQsMoQtUz2ALifxc0xTZUcjc8pIJ8410%2Bry8S6osXxOaDrgRDtNkT5cjF3MPJb%2FVjTIQ9ku9UkqbcEtLpwFFqSMs9nkUEk%2FyjSpqKiHjieFStsPDHFP57J%2B5GMG6P7LgJMNX5i70GOqUB58LgwNA4z5shA1h601j184YwCj86DluG7nql5L3BtRCqmiG9apw3Yjsxrn5to2%2BKf00rMI5zmgYYZuAaNIC87fzRL8qQYIDvwStlmwFto6nGVVa803ZbY0jUs8Rl%2FssT74R0z9kVHhVV3FCimWcMc1fb1%2FqqaKsANfvO2%2FtXvhJZ21QkaP2EutAcWq2QFTai9wDfIcNmU1c0B4lHsHriFAUlFIOZ&X-Amz-Signature=97f0da569229b66804c6238df067d31ffb6437792995cc6eddd2545e3ee19d62&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46655SWONPT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIFkH0WPtsow2WrWGdnMW21co1wCJArCg9wZyKKim%2FfcbAiEAjwFN6gGmlQEZKEXmlqRXuHY47cKXIsF4MKfALiKW1ncq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDB%2FbURPw7c4e0ckwBCrcA49wUg1Rr0UUaCmBzwofwyXcpcc3jAv%2FQ2%2ByL3kXemYP64M8sKiofYnvL%2F4guk6ob1NW5rQLxC7qXMjNfOqbnKTF5pYAUZ2mpJMcw%2Fjuq8sGK5fCaDXs2tFgRg%2Fv8lCmclHOZ1XjAwVaK5m%2F8gWjyljqxCyD0HHCCPREIsC2oB7pM3EZ2EMz0eBAKELK4%2FaAmr3cg3tADMsPRiYAS%2FOnuWKst%2FW9yL285ECBROjq8bZ%2FvXFH%2B0xvM0XR1tdZVcKs0%2F%2BCfXd1N9rMkvnxQZnLrWUxqjHigaNutK6MGpllYpczf404xe2opbrV3i%2F0uv2dq05VxMBRmWhQqOgRvNkyCdCLNKraoTsK86cBB%2FawNA%2F6DRXC7BmVjz8NUcrhrNPE%2FdkXBz%2BO2vtns%2BI%2FuXu55JxWSch6uk8ykgvtx1fLu89x0GtXe5UoV3sAIHfZfXz6YvcOfZxfmrUk5AKmHdGL6xhusQUe0%2Ft1R8rNK2n8QiPmu9yjQ2iuMvl2uEwuNryywRS48tEO4SOHKky%2BbffGam2xLW1gQiXzgYdu9kF7Lj1FKqW3dCLe2%2BKsYxzkE7FBAOHSXyx8DVyHaOPWubxxcHQX3WCpboknZg%2BECB7qk1m0RrTiDgEX1nenigk2MKP5i70GOqUBFVDKuzrNohHWV0cgewHoRfU%2FquVx201fhxLn4tG43Op91m%2FVC9rtizog%2B4R8Zt7XzSkFfUhN8qDe7noWQ%2BC%2BuYF7ZdYKz%2Fg8%2Fv1h7BfZg8C%2FkNJxmtBQqhHzsRB5vtAiwbikrJx9DGwOF2cb1wi2KBsqCfF1IT9a8MVmNXBeXmPSeXPVaawassiEiwcsVwTXIfhIBDYYSo8UcDaVQP2MpeJNtxzg&X-Amz-Signature=0e38b6f43c784e1791c724866e8832897231507980619ffe77ddfcd1898cfd52&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46655SWONPT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIFkH0WPtsow2WrWGdnMW21co1wCJArCg9wZyKKim%2FfcbAiEAjwFN6gGmlQEZKEXmlqRXuHY47cKXIsF4MKfALiKW1ncq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDB%2FbURPw7c4e0ckwBCrcA49wUg1Rr0UUaCmBzwofwyXcpcc3jAv%2FQ2%2ByL3kXemYP64M8sKiofYnvL%2F4guk6ob1NW5rQLxC7qXMjNfOqbnKTF5pYAUZ2mpJMcw%2Fjuq8sGK5fCaDXs2tFgRg%2Fv8lCmclHOZ1XjAwVaK5m%2F8gWjyljqxCyD0HHCCPREIsC2oB7pM3EZ2EMz0eBAKELK4%2FaAmr3cg3tADMsPRiYAS%2FOnuWKst%2FW9yL285ECBROjq8bZ%2FvXFH%2B0xvM0XR1tdZVcKs0%2F%2BCfXd1N9rMkvnxQZnLrWUxqjHigaNutK6MGpllYpczf404xe2opbrV3i%2F0uv2dq05VxMBRmWhQqOgRvNkyCdCLNKraoTsK86cBB%2FawNA%2F6DRXC7BmVjz8NUcrhrNPE%2FdkXBz%2BO2vtns%2BI%2FuXu55JxWSch6uk8ykgvtx1fLu89x0GtXe5UoV3sAIHfZfXz6YvcOfZxfmrUk5AKmHdGL6xhusQUe0%2Ft1R8rNK2n8QiPmu9yjQ2iuMvl2uEwuNryywRS48tEO4SOHKky%2BbffGam2xLW1gQiXzgYdu9kF7Lj1FKqW3dCLe2%2BKsYxzkE7FBAOHSXyx8DVyHaOPWubxxcHQX3WCpboknZg%2BECB7qk1m0RrTiDgEX1nenigk2MKP5i70GOqUBFVDKuzrNohHWV0cgewHoRfU%2FquVx201fhxLn4tG43Op91m%2FVC9rtizog%2B4R8Zt7XzSkFfUhN8qDe7noWQ%2BC%2BuYF7ZdYKz%2Fg8%2Fv1h7BfZg8C%2FkNJxmtBQqhHzsRB5vtAiwbikrJx9DGwOF2cb1wi2KBsqCfF1IT9a8MVmNXBeXmPSeXPVaawassiEiwcsVwTXIfhIBDYYSo8UcDaVQP2MpeJNtxzg&X-Amz-Signature=058aecc41494deb45ead074f305f0f5979297919457d77b8c3da199e0f1fa8c0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46655SWONPT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIFkH0WPtsow2WrWGdnMW21co1wCJArCg9wZyKKim%2FfcbAiEAjwFN6gGmlQEZKEXmlqRXuHY47cKXIsF4MKfALiKW1ncq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDB%2FbURPw7c4e0ckwBCrcA49wUg1Rr0UUaCmBzwofwyXcpcc3jAv%2FQ2%2ByL3kXemYP64M8sKiofYnvL%2F4guk6ob1NW5rQLxC7qXMjNfOqbnKTF5pYAUZ2mpJMcw%2Fjuq8sGK5fCaDXs2tFgRg%2Fv8lCmclHOZ1XjAwVaK5m%2F8gWjyljqxCyD0HHCCPREIsC2oB7pM3EZ2EMz0eBAKELK4%2FaAmr3cg3tADMsPRiYAS%2FOnuWKst%2FW9yL285ECBROjq8bZ%2FvXFH%2B0xvM0XR1tdZVcKs0%2F%2BCfXd1N9rMkvnxQZnLrWUxqjHigaNutK6MGpllYpczf404xe2opbrV3i%2F0uv2dq05VxMBRmWhQqOgRvNkyCdCLNKraoTsK86cBB%2FawNA%2F6DRXC7BmVjz8NUcrhrNPE%2FdkXBz%2BO2vtns%2BI%2FuXu55JxWSch6uk8ykgvtx1fLu89x0GtXe5UoV3sAIHfZfXz6YvcOfZxfmrUk5AKmHdGL6xhusQUe0%2Ft1R8rNK2n8QiPmu9yjQ2iuMvl2uEwuNryywRS48tEO4SOHKky%2BbffGam2xLW1gQiXzgYdu9kF7Lj1FKqW3dCLe2%2BKsYxzkE7FBAOHSXyx8DVyHaOPWubxxcHQX3WCpboknZg%2BECB7qk1m0RrTiDgEX1nenigk2MKP5i70GOqUBFVDKuzrNohHWV0cgewHoRfU%2FquVx201fhxLn4tG43Op91m%2FVC9rtizog%2B4R8Zt7XzSkFfUhN8qDe7noWQ%2BC%2BuYF7ZdYKz%2Fg8%2Fv1h7BfZg8C%2FkNJxmtBQqhHzsRB5vtAiwbikrJx9DGwOF2cb1wi2KBsqCfF1IT9a8MVmNXBeXmPSeXPVaawassiEiwcsVwTXIfhIBDYYSo8UcDaVQP2MpeJNtxzg&X-Amz-Signature=a9a763b7d97d3ed0a5754bfd4710b5fa6fb3052fc30889c422ac87418bea6f3f&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46655SWONPT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIFkH0WPtsow2WrWGdnMW21co1wCJArCg9wZyKKim%2FfcbAiEAjwFN6gGmlQEZKEXmlqRXuHY47cKXIsF4MKfALiKW1ncq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDB%2FbURPw7c4e0ckwBCrcA49wUg1Rr0UUaCmBzwofwyXcpcc3jAv%2FQ2%2ByL3kXemYP64M8sKiofYnvL%2F4guk6ob1NW5rQLxC7qXMjNfOqbnKTF5pYAUZ2mpJMcw%2Fjuq8sGK5fCaDXs2tFgRg%2Fv8lCmclHOZ1XjAwVaK5m%2F8gWjyljqxCyD0HHCCPREIsC2oB7pM3EZ2EMz0eBAKELK4%2FaAmr3cg3tADMsPRiYAS%2FOnuWKst%2FW9yL285ECBROjq8bZ%2FvXFH%2B0xvM0XR1tdZVcKs0%2F%2BCfXd1N9rMkvnxQZnLrWUxqjHigaNutK6MGpllYpczf404xe2opbrV3i%2F0uv2dq05VxMBRmWhQqOgRvNkyCdCLNKraoTsK86cBB%2FawNA%2F6DRXC7BmVjz8NUcrhrNPE%2FdkXBz%2BO2vtns%2BI%2FuXu55JxWSch6uk8ykgvtx1fLu89x0GtXe5UoV3sAIHfZfXz6YvcOfZxfmrUk5AKmHdGL6xhusQUe0%2Ft1R8rNK2n8QiPmu9yjQ2iuMvl2uEwuNryywRS48tEO4SOHKky%2BbffGam2xLW1gQiXzgYdu9kF7Lj1FKqW3dCLe2%2BKsYxzkE7FBAOHSXyx8DVyHaOPWubxxcHQX3WCpboknZg%2BECB7qk1m0RrTiDgEX1nenigk2MKP5i70GOqUBFVDKuzrNohHWV0cgewHoRfU%2FquVx201fhxLn4tG43Op91m%2FVC9rtizog%2B4R8Zt7XzSkFfUhN8qDe7noWQ%2BC%2BuYF7ZdYKz%2Fg8%2Fv1h7BfZg8C%2FkNJxmtBQqhHzsRB5vtAiwbikrJx9DGwOF2cb1wi2KBsqCfF1IT9a8MVmNXBeXmPSeXPVaawassiEiwcsVwTXIfhIBDYYSo8UcDaVQP2MpeJNtxzg&X-Amz-Signature=ffaf721096de84a2060cf7539b744dff34521e42e6271c762d8045e3a0728cbb&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
