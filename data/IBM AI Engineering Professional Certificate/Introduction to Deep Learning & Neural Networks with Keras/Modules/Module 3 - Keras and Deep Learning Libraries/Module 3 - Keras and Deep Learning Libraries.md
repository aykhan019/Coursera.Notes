

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663F5IB6KS%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJGMEQCIDyYLfR3w04hZY2S8bevYfwZBcAbrwt5x0TOKh0sGBdwAiBytcpXAt%2BJgkC4svcYYskjLheZn6LRpnIgk6fOiUvYair%2FAwgtEAAaDDYzNzQyMzE4MzgwNSIMo6cGpTNmJsQ2aWsIKtwDlqyzKtQyG%2Fq0ldsrIoKzPuCkZRjBKgeR5QuKpCSA4kuqzbIGdl28kWu0JQcT5yXn9I%2FzsOSmHgsvLF9xaLcosUmGYmKGvzekprJ12C8MUNVM%2BjuRccEfJoy07ZY56IvcqHbCBAjZ0hHk6XOUfihwyZ5lArt41UxFrrsS1HUBYpRtvtWmklBV7MEPOlLTNKXjF877So%2FV5p%2FvLWQ3saorMHKeAdl9fK1J%2BItyaR1%2BXIAdBLQ7mt%2BWn76L0aS6e3tcjNOMUM2uBgiqtjKt5DkqzSelNa1Pqt9JTYr2JIsF5RVrJo6ghhGbm9OaQn0ZDp7FhpYfowsuLF%2Bb%2F3feJiHPLm2x%2FayotgUQtMu0QXUQvdKFpX%2BPvid0xnb%2BDELBDv%2BP20qMoGPzR%2Bx1As1PExNf5F10cg117WhE2kZfTJiFkU0ld0gwMgGRNoxLswa23s9LMekJzFsOr1JJPgPvJc9sqy7RhAEgybF7u0qJsOAPHuoFnVsyctr%2FiKunmLhD119VFxytVmqs8fx6aYAahbI%2BGc4L4YbXmSQoJ6ZjUnbHU3jWt2her%2FDQYqk2HKqR2OWpMITcpswOmJjbhb2JBPVguvk7Uh9WwkHNWegnJprzVAaC3lETrfru2CHTRnEwm4KIvQY6pgEaFgRSQIuUmqjonwsHx8ER%2BsVOoOEiV2REbjxS1cns6v8TVJdu3GkjsGBSq%2B7IXYPcEImBZGouIPpLKdIpC6AGVc6k9v9vEumgygQr1J5fyQna1sRQnMDnzAVPdBzVCR5Dok0tsgxXT9bB6r4C901IFFzDcIgint8lzx3vbD%2BqTFLOeOK8C9kgZ1j74nafYUSgdcT4%2BIC2NzxE2FTFg3b1xHVDMrOe&X-Amz-Signature=d53e816a2d43796cf9dac5a3bda3f79903bd596aa9103689ac5147bfaf9dca71&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663F5IB6KS%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJGMEQCIDyYLfR3w04hZY2S8bevYfwZBcAbrwt5x0TOKh0sGBdwAiBytcpXAt%2BJgkC4svcYYskjLheZn6LRpnIgk6fOiUvYair%2FAwgtEAAaDDYzNzQyMzE4MzgwNSIMo6cGpTNmJsQ2aWsIKtwDlqyzKtQyG%2Fq0ldsrIoKzPuCkZRjBKgeR5QuKpCSA4kuqzbIGdl28kWu0JQcT5yXn9I%2FzsOSmHgsvLF9xaLcosUmGYmKGvzekprJ12C8MUNVM%2BjuRccEfJoy07ZY56IvcqHbCBAjZ0hHk6XOUfihwyZ5lArt41UxFrrsS1HUBYpRtvtWmklBV7MEPOlLTNKXjF877So%2FV5p%2FvLWQ3saorMHKeAdl9fK1J%2BItyaR1%2BXIAdBLQ7mt%2BWn76L0aS6e3tcjNOMUM2uBgiqtjKt5DkqzSelNa1Pqt9JTYr2JIsF5RVrJo6ghhGbm9OaQn0ZDp7FhpYfowsuLF%2Bb%2F3feJiHPLm2x%2FayotgUQtMu0QXUQvdKFpX%2BPvid0xnb%2BDELBDv%2BP20qMoGPzR%2Bx1As1PExNf5F10cg117WhE2kZfTJiFkU0ld0gwMgGRNoxLswa23s9LMekJzFsOr1JJPgPvJc9sqy7RhAEgybF7u0qJsOAPHuoFnVsyctr%2FiKunmLhD119VFxytVmqs8fx6aYAahbI%2BGc4L4YbXmSQoJ6ZjUnbHU3jWt2her%2FDQYqk2HKqR2OWpMITcpswOmJjbhb2JBPVguvk7Uh9WwkHNWegnJprzVAaC3lETrfru2CHTRnEwm4KIvQY6pgEaFgRSQIuUmqjonwsHx8ER%2BsVOoOEiV2REbjxS1cns6v8TVJdu3GkjsGBSq%2B7IXYPcEImBZGouIPpLKdIpC6AGVc6k9v9vEumgygQr1J5fyQna1sRQnMDnzAVPdBzVCR5Dok0tsgxXT9bB6r4C901IFFzDcIgint8lzx3vbD%2BqTFLOeOK8C9kgZ1j74nafYUSgdcT4%2BIC2NzxE2FTFg3b1xHVDMrOe&X-Amz-Signature=baf7384c966321fa47d7d346239d17c1aa9799b5b4ffbad05c63fb6d7812bb4d&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663F5IB6KS%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJGMEQCIDyYLfR3w04hZY2S8bevYfwZBcAbrwt5x0TOKh0sGBdwAiBytcpXAt%2BJgkC4svcYYskjLheZn6LRpnIgk6fOiUvYair%2FAwgtEAAaDDYzNzQyMzE4MzgwNSIMo6cGpTNmJsQ2aWsIKtwDlqyzKtQyG%2Fq0ldsrIoKzPuCkZRjBKgeR5QuKpCSA4kuqzbIGdl28kWu0JQcT5yXn9I%2FzsOSmHgsvLF9xaLcosUmGYmKGvzekprJ12C8MUNVM%2BjuRccEfJoy07ZY56IvcqHbCBAjZ0hHk6XOUfihwyZ5lArt41UxFrrsS1HUBYpRtvtWmklBV7MEPOlLTNKXjF877So%2FV5p%2FvLWQ3saorMHKeAdl9fK1J%2BItyaR1%2BXIAdBLQ7mt%2BWn76L0aS6e3tcjNOMUM2uBgiqtjKt5DkqzSelNa1Pqt9JTYr2JIsF5RVrJo6ghhGbm9OaQn0ZDp7FhpYfowsuLF%2Bb%2F3feJiHPLm2x%2FayotgUQtMu0QXUQvdKFpX%2BPvid0xnb%2BDELBDv%2BP20qMoGPzR%2Bx1As1PExNf5F10cg117WhE2kZfTJiFkU0ld0gwMgGRNoxLswa23s9LMekJzFsOr1JJPgPvJc9sqy7RhAEgybF7u0qJsOAPHuoFnVsyctr%2FiKunmLhD119VFxytVmqs8fx6aYAahbI%2BGc4L4YbXmSQoJ6ZjUnbHU3jWt2her%2FDQYqk2HKqR2OWpMITcpswOmJjbhb2JBPVguvk7Uh9WwkHNWegnJprzVAaC3lETrfru2CHTRnEwm4KIvQY6pgEaFgRSQIuUmqjonwsHx8ER%2BsVOoOEiV2REbjxS1cns6v8TVJdu3GkjsGBSq%2B7IXYPcEImBZGouIPpLKdIpC6AGVc6k9v9vEumgygQr1J5fyQna1sRQnMDnzAVPdBzVCR5Dok0tsgxXT9bB6r4C901IFFzDcIgint8lzx3vbD%2BqTFLOeOK8C9kgZ1j74nafYUSgdcT4%2BIC2NzxE2FTFg3b1xHVDMrOe&X-Amz-Signature=d5ff0807b68e144c993f5ec7ac27a5d7274ea687c8db38745abe2dd4149d513c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UH7DPDW4%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJIMEYCIQDIipyGgm%2B0oPt4bnxyIYkVJuQYkbLlaERaTskkYPDF3AIhAP%2BTIMOdACPbbpwYVd0j3MaC6pPguWnWqkizs80llnQVKv8DCC0QABoMNjM3NDIzMTgzODA1IgyYYPL7%2Bx9wmU8SmdMq3AN%2Bvw3omQhurwV9lfUiFAjFajKdnyITkHWM%2FF2p9Dvy8UpqrKj9k9%2BN%2FbMrYiXpkE2e7edYA5qkMZW6GffzuBQrQJlAPv7kpKi5GgVgA0v2XdoRywLdVVexVA%2FM3LYVPlhw%2Fh%2Fm965UVwLjxVQTNcBc1MgdgHNCrXfppmzdaqVoKNerJL04RyXaClB9croD%2Bv8xnZXrdCt7P3p5RdZaFUIWTI0lYcaW7ocMgCoFLQ0TV%2Bp0UrKchYZ8yw%2BTwfE24c5gSh2uIDtz27pZKp7kGjKIPrT5UDR34mIG7KwgZFgp2lRxuxwxfp0eYhjvkekO8Q2ShOhrmDHe%2FQAVSTqsvXYvF8HtFx3ovc%2F973ZUw5OaIlJtS2aazr8%2B%2BXYuKd%2FMKif6EW%2F9P9pKLE%2FhY7jWt8HQyk1AgDZxR9oH%2FHsJKi4kmtk7a89hgqk8L59D8OBeMSMMbeEwNwKwu7MQvjr7Ms9TFUVFRxIHfT%2BUZ71qW0AEOTADfKmCBUJ9%2F%2FWLwdEeiJhcEHAESfZb%2FI6VFprkEHT%2Bn%2Bf9pifMqxCHl44qajw7W06A1iIFoKkVQcjr7sHGylV9A6iNdnv3mBJKq8kLGdg3OfPJMxBWAPIzVDe4HyG1%2BuJ5BL6%2FTk1pffy4izDqgYi9BjqkATGiXKjzD24bz82X5gPHyBb8x64ob6CCWXetjLoPDCdA0T6h%2BEPC8LypFdZvljrBIhcgGeBpwJFjQ0EyQgym5XjJJ8gZtpQY1IutEmv3Li7TgW8WuG8pZuWpwdOO7WdYt%2Bv5ZqZoLQeP1xfNMTlTMO%2F1e55Vn4vBzqzaAtUhQRkknb%2B0KH5IzwyS9xRB76EeUhc6kpz3uDAGtUDUtZyr336Doddv&X-Amz-Signature=6882b2e09af0791d2842107a5972cca2df1bb907d36a472a44968dd28532cadd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVBWBUTO%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJIMEYCIQCVibEt4q7srqU4xXgd6%2FUw4WT2hrDPSUd58KkJMjTf0gIhAIJpEPx4p8gIzDkC8lJ8w5HVEdq2q8nTh56TWPKWdxy4Kv8DCC0QABoMNjM3NDIzMTgzODA1IgywBnN1PyCtgvY9H%2FUq3AOricEhS80I02hts%2BUg1wWbP0SODDnguuM%2FLSggyWcWgMgpXVPsHcQkvntdBqeM%2BkHHaCYOzIIztUEofcQpsKmj8I8aAdbqkOuNQTOU%2BS7%2FCoywFjOMtnCqz4oMmiON%2B7wWp2B16O4XoEraJmdqMelmRE%2BeSo8beK19BfgwMd59HIEKYzhm7OMbtHBWW97ofL7gwDMaWW1GXylG%2Fon%2BttdLGWGJx45zthQMZxcvHM12KxH2IJsVRme9Ggm%2FqhksvCyYyUx%2FaI9Gc0XBC%2F8Er1Q9xzo0eSzl7IX7N1luIyyUjfVQDaO1DckHDlwfcL2C7U1ZpsEq%2F0McRqPpC7KOdwLgjGcC1SNcQ7TPDwOeVK5Uy7KdCpeDbK%2B78HdeZl%2Fu5JWqzYWz5N%2BYt4aHgcFauoJU0H9p9t3Nd8o36haqIP67L%2BOeGM%2BksCmpKpo%2BSnglOZy49ATjibOlvpNZIALPWRCZigdJlCCgRUwUOEZLJRbHrpjgA8Zy2zSuVkmbEHEk%2BeG8rJxMuLDzJ8z%2Bst2GvcYo%2FGBbn8PsuwOYB2ksVSO6Ck7dcEI3zqV%2FGeODtudflLqpqOFjb9oWjCuIXifByhcZEBwIs%2Bhhcqvi%2B9OFXPfIv0Q5lsgHr4RhRSPnMzCKgoi9BjqkARQG9D9znLL75kVafRK7%2BgqhjJFVDJDwLgAmgV4mnn31tE%2BfhWZ7B2KEE9luV7RKf1FIYeSvL%2B4gTJekYgUEG1iBEpuWwCZPUqwPPC6q52W3IIGdnTeWlRj%2FMZOFMEuzbzUBac2hGjsQ5NzYXwt11MUjMxwgSiM4qDO%2BudZshTX%2B5o2UKHLs1fkXgWp%2FbI%2BSj7PZOn0Ii%2BZycEFAJM%2Bh%2BO4L5WvE&X-Amz-Signature=4407d77bcc2afea62b5d90f41648bc3da7c84cd3d1faf1f0715fbfc0af908dc4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663F5IB6KS%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJGMEQCIDyYLfR3w04hZY2S8bevYfwZBcAbrwt5x0TOKh0sGBdwAiBytcpXAt%2BJgkC4svcYYskjLheZn6LRpnIgk6fOiUvYair%2FAwgtEAAaDDYzNzQyMzE4MzgwNSIMo6cGpTNmJsQ2aWsIKtwDlqyzKtQyG%2Fq0ldsrIoKzPuCkZRjBKgeR5QuKpCSA4kuqzbIGdl28kWu0JQcT5yXn9I%2FzsOSmHgsvLF9xaLcosUmGYmKGvzekprJ12C8MUNVM%2BjuRccEfJoy07ZY56IvcqHbCBAjZ0hHk6XOUfihwyZ5lArt41UxFrrsS1HUBYpRtvtWmklBV7MEPOlLTNKXjF877So%2FV5p%2FvLWQ3saorMHKeAdl9fK1J%2BItyaR1%2BXIAdBLQ7mt%2BWn76L0aS6e3tcjNOMUM2uBgiqtjKt5DkqzSelNa1Pqt9JTYr2JIsF5RVrJo6ghhGbm9OaQn0ZDp7FhpYfowsuLF%2Bb%2F3feJiHPLm2x%2FayotgUQtMu0QXUQvdKFpX%2BPvid0xnb%2BDELBDv%2BP20qMoGPzR%2Bx1As1PExNf5F10cg117WhE2kZfTJiFkU0ld0gwMgGRNoxLswa23s9LMekJzFsOr1JJPgPvJc9sqy7RhAEgybF7u0qJsOAPHuoFnVsyctr%2FiKunmLhD119VFxytVmqs8fx6aYAahbI%2BGc4L4YbXmSQoJ6ZjUnbHU3jWt2her%2FDQYqk2HKqR2OWpMITcpswOmJjbhb2JBPVguvk7Uh9WwkHNWegnJprzVAaC3lETrfru2CHTRnEwm4KIvQY6pgEaFgRSQIuUmqjonwsHx8ER%2BsVOoOEiV2REbjxS1cns6v8TVJdu3GkjsGBSq%2B7IXYPcEImBZGouIPpLKdIpC6AGVc6k9v9vEumgygQr1J5fyQna1sRQnMDnzAVPdBzVCR5Dok0tsgxXT9bB6r4C901IFFzDcIgint8lzx3vbD%2BqTFLOeOK8C9kgZ1j74nafYUSgdcT4%2BIC2NzxE2FTFg3b1xHVDMrOe&X-Amz-Signature=e18befcd2b5fcf1f44a2a5199283ab0ee069c019031013330f8b86b3bbbd8bbd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663F5IB6KS%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJGMEQCIDyYLfR3w04hZY2S8bevYfwZBcAbrwt5x0TOKh0sGBdwAiBytcpXAt%2BJgkC4svcYYskjLheZn6LRpnIgk6fOiUvYair%2FAwgtEAAaDDYzNzQyMzE4MzgwNSIMo6cGpTNmJsQ2aWsIKtwDlqyzKtQyG%2Fq0ldsrIoKzPuCkZRjBKgeR5QuKpCSA4kuqzbIGdl28kWu0JQcT5yXn9I%2FzsOSmHgsvLF9xaLcosUmGYmKGvzekprJ12C8MUNVM%2BjuRccEfJoy07ZY56IvcqHbCBAjZ0hHk6XOUfihwyZ5lArt41UxFrrsS1HUBYpRtvtWmklBV7MEPOlLTNKXjF877So%2FV5p%2FvLWQ3saorMHKeAdl9fK1J%2BItyaR1%2BXIAdBLQ7mt%2BWn76L0aS6e3tcjNOMUM2uBgiqtjKt5DkqzSelNa1Pqt9JTYr2JIsF5RVrJo6ghhGbm9OaQn0ZDp7FhpYfowsuLF%2Bb%2F3feJiHPLm2x%2FayotgUQtMu0QXUQvdKFpX%2BPvid0xnb%2BDELBDv%2BP20qMoGPzR%2Bx1As1PExNf5F10cg117WhE2kZfTJiFkU0ld0gwMgGRNoxLswa23s9LMekJzFsOr1JJPgPvJc9sqy7RhAEgybF7u0qJsOAPHuoFnVsyctr%2FiKunmLhD119VFxytVmqs8fx6aYAahbI%2BGc4L4YbXmSQoJ6ZjUnbHU3jWt2her%2FDQYqk2HKqR2OWpMITcpswOmJjbhb2JBPVguvk7Uh9WwkHNWegnJprzVAaC3lETrfru2CHTRnEwm4KIvQY6pgEaFgRSQIuUmqjonwsHx8ER%2BsVOoOEiV2REbjxS1cns6v8TVJdu3GkjsGBSq%2B7IXYPcEImBZGouIPpLKdIpC6AGVc6k9v9vEumgygQr1J5fyQna1sRQnMDnzAVPdBzVCR5Dok0tsgxXT9bB6r4C901IFFzDcIgint8lzx3vbD%2BqTFLOeOK8C9kgZ1j74nafYUSgdcT4%2BIC2NzxE2FTFg3b1xHVDMrOe&X-Amz-Signature=682dc7e5b9bc848370bdeea88e729f084c6df775a7443d19110b43e79783920b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663F5IB6KS%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJGMEQCIDyYLfR3w04hZY2S8bevYfwZBcAbrwt5x0TOKh0sGBdwAiBytcpXAt%2BJgkC4svcYYskjLheZn6LRpnIgk6fOiUvYair%2FAwgtEAAaDDYzNzQyMzE4MzgwNSIMo6cGpTNmJsQ2aWsIKtwDlqyzKtQyG%2Fq0ldsrIoKzPuCkZRjBKgeR5QuKpCSA4kuqzbIGdl28kWu0JQcT5yXn9I%2FzsOSmHgsvLF9xaLcosUmGYmKGvzekprJ12C8MUNVM%2BjuRccEfJoy07ZY56IvcqHbCBAjZ0hHk6XOUfihwyZ5lArt41UxFrrsS1HUBYpRtvtWmklBV7MEPOlLTNKXjF877So%2FV5p%2FvLWQ3saorMHKeAdl9fK1J%2BItyaR1%2BXIAdBLQ7mt%2BWn76L0aS6e3tcjNOMUM2uBgiqtjKt5DkqzSelNa1Pqt9JTYr2JIsF5RVrJo6ghhGbm9OaQn0ZDp7FhpYfowsuLF%2Bb%2F3feJiHPLm2x%2FayotgUQtMu0QXUQvdKFpX%2BPvid0xnb%2BDELBDv%2BP20qMoGPzR%2Bx1As1PExNf5F10cg117WhE2kZfTJiFkU0ld0gwMgGRNoxLswa23s9LMekJzFsOr1JJPgPvJc9sqy7RhAEgybF7u0qJsOAPHuoFnVsyctr%2FiKunmLhD119VFxytVmqs8fx6aYAahbI%2BGc4L4YbXmSQoJ6ZjUnbHU3jWt2her%2FDQYqk2HKqR2OWpMITcpswOmJjbhb2JBPVguvk7Uh9WwkHNWegnJprzVAaC3lETrfru2CHTRnEwm4KIvQY6pgEaFgRSQIuUmqjonwsHx8ER%2BsVOoOEiV2REbjxS1cns6v8TVJdu3GkjsGBSq%2B7IXYPcEImBZGouIPpLKdIpC6AGVc6k9v9vEumgygQr1J5fyQna1sRQnMDnzAVPdBzVCR5Dok0tsgxXT9bB6r4C901IFFzDcIgint8lzx3vbD%2BqTFLOeOK8C9kgZ1j74nafYUSgdcT4%2BIC2NzxE2FTFg3b1xHVDMrOe&X-Amz-Signature=ee8bad08d9c743c67fb13e8363785ec613828024050de958b43a0f4e3edea8ea&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663F5IB6KS%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJGMEQCIDyYLfR3w04hZY2S8bevYfwZBcAbrwt5x0TOKh0sGBdwAiBytcpXAt%2BJgkC4svcYYskjLheZn6LRpnIgk6fOiUvYair%2FAwgtEAAaDDYzNzQyMzE4MzgwNSIMo6cGpTNmJsQ2aWsIKtwDlqyzKtQyG%2Fq0ldsrIoKzPuCkZRjBKgeR5QuKpCSA4kuqzbIGdl28kWu0JQcT5yXn9I%2FzsOSmHgsvLF9xaLcosUmGYmKGvzekprJ12C8MUNVM%2BjuRccEfJoy07ZY56IvcqHbCBAjZ0hHk6XOUfihwyZ5lArt41UxFrrsS1HUBYpRtvtWmklBV7MEPOlLTNKXjF877So%2FV5p%2FvLWQ3saorMHKeAdl9fK1J%2BItyaR1%2BXIAdBLQ7mt%2BWn76L0aS6e3tcjNOMUM2uBgiqtjKt5DkqzSelNa1Pqt9JTYr2JIsF5RVrJo6ghhGbm9OaQn0ZDp7FhpYfowsuLF%2Bb%2F3feJiHPLm2x%2FayotgUQtMu0QXUQvdKFpX%2BPvid0xnb%2BDELBDv%2BP20qMoGPzR%2Bx1As1PExNf5F10cg117WhE2kZfTJiFkU0ld0gwMgGRNoxLswa23s9LMekJzFsOr1JJPgPvJc9sqy7RhAEgybF7u0qJsOAPHuoFnVsyctr%2FiKunmLhD119VFxytVmqs8fx6aYAahbI%2BGc4L4YbXmSQoJ6ZjUnbHU3jWt2her%2FDQYqk2HKqR2OWpMITcpswOmJjbhb2JBPVguvk7Uh9WwkHNWegnJprzVAaC3lETrfru2CHTRnEwm4KIvQY6pgEaFgRSQIuUmqjonwsHx8ER%2BsVOoOEiV2REbjxS1cns6v8TVJdu3GkjsGBSq%2B7IXYPcEImBZGouIPpLKdIpC6AGVc6k9v9vEumgygQr1J5fyQna1sRQnMDnzAVPdBzVCR5Dok0tsgxXT9bB6r4C901IFFzDcIgint8lzx3vbD%2BqTFLOeOK8C9kgZ1j74nafYUSgdcT4%2BIC2NzxE2FTFg3b1xHVDMrOe&X-Amz-Signature=5fd28fb6dd87c126cf33426edf990aadf9bc94d14d09cfca8f0010b093e58ba6&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
