

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWNNSWOV%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIErhVj8JVPMM9osa2hE0Aajzfq4tKkVnWBNih9MW26opAiEA%2FqXMxwuje2vhHUd292mg3X50%2FJdmMqbE9K5148B%2F5vsq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDBNdzSi13%2FlsqXE6jyrcA%2B2ztcNlXWLSc523avMQ5cmanTdOUG%2Byn%2FOxJXx7J%2BR7jFG1AWUVwLPzVAvvlhUcEw%2BMP71if0eDVjj%2FMBsPzouNwgGkyfEvgTSv0jLXkJcOIpbxlA6TrSdGleUOX9Pd2wg8AQrWVLqusZnqzBhyVSm25W1DfCLqa%2F%2FQ2KKfo2ByhH0gP0%2BW5wkeFsEFlSydKkC58th3nWQjrpUnYAX0HgVEZfm60H9d4LXgEpoR%2FYh9JXdUO1bsPGvPTF1Z9PtbdjTbB8L9g2q6vUmzzLcsiY%2FzTFbZesW8%2BuuFugs%2FGfaAQZ4FpEfgBImShNRn%2FPipyhPD79F5Wy4qhPmeK5Pd37vT%2BfhzZ3YGktdH5iLxBFapAE3rxtOh9Ido93BVTJZ%2FWBqnaJJ%2B1MDDXIm8MuczLF6vIgK69tT6Nb4f8i3Qoupo1mdctwOjIkhY16z0bCRPh9IvU7Pg2m9TUn9w43VK%2Fx3QBYQVjqqbAEGUBkx3qcgDqhTR6Hd9DbWo6IJeNKgLqZaGUfKfoV6EoNTzV8fUJK%2B3dFFpC3qMfmvuRlANlBFQgdvtXeZa3uF13SPQPbDJYAZFCfovj%2Fy3lkXmqy303b%2FOsxcswWgn6klC9QhrMde8IdgioOa%2BI3X6vnoXMNWuh70GOqUBTOGuXxIiFT9KfC2LSkgTLGS2F1TiHiDW1wPE6G9ReqoPlqCV81dtF9eGj256jjLLJvF5kGGp7lE1yp973GLQDB%2FGnL3U4GEwA7a9U2VPwXsCNbPdRP6m%2FCoDLKqcVZ4q70SfKCMpNNIBuDokA37uOolWriC0WoOaaq%2BBS1VIu%2Bfk%2BFdPLRZoZ4cS3FwYh9WNr%2FNu48NTwtu5fcF7fHhBZDmeljLH&X-Amz-Signature=b785d8f10e9a18567470c76753ecc83c1596c6677122eb926ee8863a14c65462&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWNNSWOV%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIErhVj8JVPMM9osa2hE0Aajzfq4tKkVnWBNih9MW26opAiEA%2FqXMxwuje2vhHUd292mg3X50%2FJdmMqbE9K5148B%2F5vsq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDBNdzSi13%2FlsqXE6jyrcA%2B2ztcNlXWLSc523avMQ5cmanTdOUG%2Byn%2FOxJXx7J%2BR7jFG1AWUVwLPzVAvvlhUcEw%2BMP71if0eDVjj%2FMBsPzouNwgGkyfEvgTSv0jLXkJcOIpbxlA6TrSdGleUOX9Pd2wg8AQrWVLqusZnqzBhyVSm25W1DfCLqa%2F%2FQ2KKfo2ByhH0gP0%2BW5wkeFsEFlSydKkC58th3nWQjrpUnYAX0HgVEZfm60H9d4LXgEpoR%2FYh9JXdUO1bsPGvPTF1Z9PtbdjTbB8L9g2q6vUmzzLcsiY%2FzTFbZesW8%2BuuFugs%2FGfaAQZ4FpEfgBImShNRn%2FPipyhPD79F5Wy4qhPmeK5Pd37vT%2BfhzZ3YGktdH5iLxBFapAE3rxtOh9Ido93BVTJZ%2FWBqnaJJ%2B1MDDXIm8MuczLF6vIgK69tT6Nb4f8i3Qoupo1mdctwOjIkhY16z0bCRPh9IvU7Pg2m9TUn9w43VK%2Fx3QBYQVjqqbAEGUBkx3qcgDqhTR6Hd9DbWo6IJeNKgLqZaGUfKfoV6EoNTzV8fUJK%2B3dFFpC3qMfmvuRlANlBFQgdvtXeZa3uF13SPQPbDJYAZFCfovj%2Fy3lkXmqy303b%2FOsxcswWgn6klC9QhrMde8IdgioOa%2BI3X6vnoXMNWuh70GOqUBTOGuXxIiFT9KfC2LSkgTLGS2F1TiHiDW1wPE6G9ReqoPlqCV81dtF9eGj256jjLLJvF5kGGp7lE1yp973GLQDB%2FGnL3U4GEwA7a9U2VPwXsCNbPdRP6m%2FCoDLKqcVZ4q70SfKCMpNNIBuDokA37uOolWriC0WoOaaq%2BBS1VIu%2Bfk%2BFdPLRZoZ4cS3FwYh9WNr%2FNu48NTwtu5fcF7fHhBZDmeljLH&X-Amz-Signature=49327308dcea09625b248ccf76354b7cf78d287f85ba267ff15c16cb3511291b&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWNNSWOV%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIErhVj8JVPMM9osa2hE0Aajzfq4tKkVnWBNih9MW26opAiEA%2FqXMxwuje2vhHUd292mg3X50%2FJdmMqbE9K5148B%2F5vsq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDBNdzSi13%2FlsqXE6jyrcA%2B2ztcNlXWLSc523avMQ5cmanTdOUG%2Byn%2FOxJXx7J%2BR7jFG1AWUVwLPzVAvvlhUcEw%2BMP71if0eDVjj%2FMBsPzouNwgGkyfEvgTSv0jLXkJcOIpbxlA6TrSdGleUOX9Pd2wg8AQrWVLqusZnqzBhyVSm25W1DfCLqa%2F%2FQ2KKfo2ByhH0gP0%2BW5wkeFsEFlSydKkC58th3nWQjrpUnYAX0HgVEZfm60H9d4LXgEpoR%2FYh9JXdUO1bsPGvPTF1Z9PtbdjTbB8L9g2q6vUmzzLcsiY%2FzTFbZesW8%2BuuFugs%2FGfaAQZ4FpEfgBImShNRn%2FPipyhPD79F5Wy4qhPmeK5Pd37vT%2BfhzZ3YGktdH5iLxBFapAE3rxtOh9Ido93BVTJZ%2FWBqnaJJ%2B1MDDXIm8MuczLF6vIgK69tT6Nb4f8i3Qoupo1mdctwOjIkhY16z0bCRPh9IvU7Pg2m9TUn9w43VK%2Fx3QBYQVjqqbAEGUBkx3qcgDqhTR6Hd9DbWo6IJeNKgLqZaGUfKfoV6EoNTzV8fUJK%2B3dFFpC3qMfmvuRlANlBFQgdvtXeZa3uF13SPQPbDJYAZFCfovj%2Fy3lkXmqy303b%2FOsxcswWgn6klC9QhrMde8IdgioOa%2BI3X6vnoXMNWuh70GOqUBTOGuXxIiFT9KfC2LSkgTLGS2F1TiHiDW1wPE6G9ReqoPlqCV81dtF9eGj256jjLLJvF5kGGp7lE1yp973GLQDB%2FGnL3U4GEwA7a9U2VPwXsCNbPdRP6m%2FCoDLKqcVZ4q70SfKCMpNNIBuDokA37uOolWriC0WoOaaq%2BBS1VIu%2Bfk%2BFdPLRZoZ4cS3FwYh9WNr%2FNu48NTwtu5fcF7fHhBZDmeljLH&X-Amz-Signature=1f41c3f0d1da600679bcf404f183cb30f57bf9635f14dcf877d8f92fbf66e60e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46666XDWDSU%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091533Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIQDBWTj6XrjcdVqnTjat5b3BsYeCMN03S4TXnZNWk9rftQIgF2iPEGEpPXXu0ugFD2Xaxrxr60Fim3VNagKLrdw1fecq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDDT7Axv%2FsbmZV8fIvircA4kKnnxmxNBEocoZ5Bo%2Bh%2BVDrZVjR%2FQWNdflOsj4tfr%2F40vMWSWuDZq8vghR6KvwL8aaXPn%2F3kCvWV1v0SsuqtZyE1dAoyI%2Fat00EvvXYSypriLxgN3cyB7vOQlHtewUp8ZAB8YZjVpgWABo9bgjrdLtzOKCcNygseTkba09e7Dh1NWgew9isqpNGQEqTW%2B0%2FKtd7cg7Un%2Fkz7tzcVdn2QahsMirsjqvQD4wRZpN8tF%2F5oEwPJHQ03TzOie%2B9ZMFI%2FEo3A0qERtTvaLzWZPlNIjZclDb60YJZTCqe1B9smCdSvlDKQ%2ByTNnwhzcc7hHt4DyIydFMMijwKcQtN6qQ3uwvsQBjRjJWCewq86e4lOmRA%2BAnCb88jh28OhAkt8hEMJbmuEs14zXhYjkyOC1YanyKDI8st%2BP1zDaJmCcFZYlzCyC6zsNlVjIa0KkcVSQCEIVXsT%2FGUbpLDpkgttL038cWwBRNe%2FNSOoU2w3V5%2BlXQNMEszmQ4xpKuKaGRjcvhMbMskGQdgZoCitzyl22BVlxABl9SYqFDRTHgDZnPC9Rgv20b8PpSNhZTwY4ISEi7tUT47z9JHNwCrxlS6TYvJXd0hCDlwElf2d09y6%2FAL48ERoMwgdolQY%2Bd5g0AMJ%2Buh70GOqUBL%2FyjytlhbJrTq3Fje%2FO2poCnwIuaKDop%2BGoDccUpVFebgIEYpufWDLRgrAj7Y7twFH4dG1BX1Dh4jznGA%2FTcJBuSjDrVf1m42g9fUy7bb4uIZSSBuzeefX1GwqGOS86y9CjdbjVa9lYn2mSygXUM3f4N8NqVR1JCOWNQbzBZbw4g21Y0JZDvpbkii6tiQpB26TTyXi8b28xbeSljSIjW3CDZYrcB&X-Amz-Signature=f5984989dc6669ce6e9805ae272541ebe579ef9da1c5792f0b1f0b3713568486&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46674K6XBK5%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIQDthrIEkPPU3r5KCsGPbxnZbC9LCWN8Evb3tHjhySUcqwIgUfzkNHK3KLFkrsWH5VmQ%2FDW1v%2BhssKJxwDI2h1OyhKcq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDBKwEJOWUee%2B7jfIHircAyKYxfFMnlwfp%2B0om9egK3QWiJ3LZEQHGD6ZMl1NzOWTqpQ%2FuhI7%2BOr7uc7alwgjh6MxluG6ThJIrxfrpHXTqW2AiqdX0Y8rWWMXmEuYRy0wmz2t7lfKlILqbXPUTmlH1lEQ9tm6xTHHWyWp%2BHP2Y4KgfHF7bg05nJo99Zc2VHJIfw5zSoOidGp6SLDwOUEDL9%2FuYNLv13dx%2BQWSNYJLewRGspEqFp20H56Vw3aTH3WTtYTP30a2gy1Mwmfwi2YmXdTV8xuXPbw0fWxcBzUsEf%2Bfz0a6MFxxF217lIKQTf%2FCQdvvmfZtZNirHxVZD%2FRkUoJskjiJi5jNAgr%2FpvsaIMMmTPP7fboUaJt62uVOoum7C1VrIAUEliRq9%2FNwU5jB3YlLEwRW%2Bwjnv5Gb%2B6EDOzpbG6FdWfQqlwsbjuQeELo32WWbY8hkd9UOHHyR3QlrUfv7rdHgs1s2Q5ZKrZJh2WxAZCid2SfkOMwLBigM%2BH7cX8cf8V2ck1RvOjyXJ2Ovjz6DhZgoe6VKgLRl%2BljbJa2M96BJDqYFmeFqm3dJHOXpL6w%2BmafbIRnX7OsmhJs10x5hjOL4p9lgh58uzj1y7S8GyLXTqyDXNVcei5lg2Qw%2FYJhmsXGQ6l27HOA4MNauh70GOqUB0XnCHy%2FwXmv5FMzwT1VZdyrx2ZP85jMpDW94CqTLzmoJCwZv7AZsj3F%2FXX4EP1SHA8n3n%2FQtNHrZG8AxwS6PgMFiSoUYGjvm2WKDH%2F%2BO%2FBaeIc%2FsvAaCSF0NfC8hpm36cwuFPspsc9gdz5gopFdPaqZu4CeBTKXFcjYurejQvwwF3aVMQyhREbZbiaXYj4RK2%2FSATmqHICuUWHqLQP66ME%2F2o6Wd&X-Amz-Signature=50a9aec7b3e95ac5c830c5e83014b7e8c9b679a5752beb95d068a5811dae3405&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWNNSWOV%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIErhVj8JVPMM9osa2hE0Aajzfq4tKkVnWBNih9MW26opAiEA%2FqXMxwuje2vhHUd292mg3X50%2FJdmMqbE9K5148B%2F5vsq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDBNdzSi13%2FlsqXE6jyrcA%2B2ztcNlXWLSc523avMQ5cmanTdOUG%2Byn%2FOxJXx7J%2BR7jFG1AWUVwLPzVAvvlhUcEw%2BMP71if0eDVjj%2FMBsPzouNwgGkyfEvgTSv0jLXkJcOIpbxlA6TrSdGleUOX9Pd2wg8AQrWVLqusZnqzBhyVSm25W1DfCLqa%2F%2FQ2KKfo2ByhH0gP0%2BW5wkeFsEFlSydKkC58th3nWQjrpUnYAX0HgVEZfm60H9d4LXgEpoR%2FYh9JXdUO1bsPGvPTF1Z9PtbdjTbB8L9g2q6vUmzzLcsiY%2FzTFbZesW8%2BuuFugs%2FGfaAQZ4FpEfgBImShNRn%2FPipyhPD79F5Wy4qhPmeK5Pd37vT%2BfhzZ3YGktdH5iLxBFapAE3rxtOh9Ido93BVTJZ%2FWBqnaJJ%2B1MDDXIm8MuczLF6vIgK69tT6Nb4f8i3Qoupo1mdctwOjIkhY16z0bCRPh9IvU7Pg2m9TUn9w43VK%2Fx3QBYQVjqqbAEGUBkx3qcgDqhTR6Hd9DbWo6IJeNKgLqZaGUfKfoV6EoNTzV8fUJK%2B3dFFpC3qMfmvuRlANlBFQgdvtXeZa3uF13SPQPbDJYAZFCfovj%2Fy3lkXmqy303b%2FOsxcswWgn6klC9QhrMde8IdgioOa%2BI3X6vnoXMNWuh70GOqUBTOGuXxIiFT9KfC2LSkgTLGS2F1TiHiDW1wPE6G9ReqoPlqCV81dtF9eGj256jjLLJvF5kGGp7lE1yp973GLQDB%2FGnL3U4GEwA7a9U2VPwXsCNbPdRP6m%2FCoDLKqcVZ4q70SfKCMpNNIBuDokA37uOolWriC0WoOaaq%2BBS1VIu%2Bfk%2BFdPLRZoZ4cS3FwYh9WNr%2FNu48NTwtu5fcF7fHhBZDmeljLH&X-Amz-Signature=f69d6be2efab2b0a46212e4c7b4636a4a8edc1689ca66e1a07a96258e79d5037&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWNNSWOV%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIErhVj8JVPMM9osa2hE0Aajzfq4tKkVnWBNih9MW26opAiEA%2FqXMxwuje2vhHUd292mg3X50%2FJdmMqbE9K5148B%2F5vsq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDBNdzSi13%2FlsqXE6jyrcA%2B2ztcNlXWLSc523avMQ5cmanTdOUG%2Byn%2FOxJXx7J%2BR7jFG1AWUVwLPzVAvvlhUcEw%2BMP71if0eDVjj%2FMBsPzouNwgGkyfEvgTSv0jLXkJcOIpbxlA6TrSdGleUOX9Pd2wg8AQrWVLqusZnqzBhyVSm25W1DfCLqa%2F%2FQ2KKfo2ByhH0gP0%2BW5wkeFsEFlSydKkC58th3nWQjrpUnYAX0HgVEZfm60H9d4LXgEpoR%2FYh9JXdUO1bsPGvPTF1Z9PtbdjTbB8L9g2q6vUmzzLcsiY%2FzTFbZesW8%2BuuFugs%2FGfaAQZ4FpEfgBImShNRn%2FPipyhPD79F5Wy4qhPmeK5Pd37vT%2BfhzZ3YGktdH5iLxBFapAE3rxtOh9Ido93BVTJZ%2FWBqnaJJ%2B1MDDXIm8MuczLF6vIgK69tT6Nb4f8i3Qoupo1mdctwOjIkhY16z0bCRPh9IvU7Pg2m9TUn9w43VK%2Fx3QBYQVjqqbAEGUBkx3qcgDqhTR6Hd9DbWo6IJeNKgLqZaGUfKfoV6EoNTzV8fUJK%2B3dFFpC3qMfmvuRlANlBFQgdvtXeZa3uF13SPQPbDJYAZFCfovj%2Fy3lkXmqy303b%2FOsxcswWgn6klC9QhrMde8IdgioOa%2BI3X6vnoXMNWuh70GOqUBTOGuXxIiFT9KfC2LSkgTLGS2F1TiHiDW1wPE6G9ReqoPlqCV81dtF9eGj256jjLLJvF5kGGp7lE1yp973GLQDB%2FGnL3U4GEwA7a9U2VPwXsCNbPdRP6m%2FCoDLKqcVZ4q70SfKCMpNNIBuDokA37uOolWriC0WoOaaq%2BBS1VIu%2Bfk%2BFdPLRZoZ4cS3FwYh9WNr%2FNu48NTwtu5fcF7fHhBZDmeljLH&X-Amz-Signature=8b2b0812aadb0a41a5d7943b8e572f9f1fabcbe76bc11a55a0c3c524612cc7f0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWNNSWOV%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIErhVj8JVPMM9osa2hE0Aajzfq4tKkVnWBNih9MW26opAiEA%2FqXMxwuje2vhHUd292mg3X50%2FJdmMqbE9K5148B%2F5vsq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDBNdzSi13%2FlsqXE6jyrcA%2B2ztcNlXWLSc523avMQ5cmanTdOUG%2Byn%2FOxJXx7J%2BR7jFG1AWUVwLPzVAvvlhUcEw%2BMP71if0eDVjj%2FMBsPzouNwgGkyfEvgTSv0jLXkJcOIpbxlA6TrSdGleUOX9Pd2wg8AQrWVLqusZnqzBhyVSm25W1DfCLqa%2F%2FQ2KKfo2ByhH0gP0%2BW5wkeFsEFlSydKkC58th3nWQjrpUnYAX0HgVEZfm60H9d4LXgEpoR%2FYh9JXdUO1bsPGvPTF1Z9PtbdjTbB8L9g2q6vUmzzLcsiY%2FzTFbZesW8%2BuuFugs%2FGfaAQZ4FpEfgBImShNRn%2FPipyhPD79F5Wy4qhPmeK5Pd37vT%2BfhzZ3YGktdH5iLxBFapAE3rxtOh9Ido93BVTJZ%2FWBqnaJJ%2B1MDDXIm8MuczLF6vIgK69tT6Nb4f8i3Qoupo1mdctwOjIkhY16z0bCRPh9IvU7Pg2m9TUn9w43VK%2Fx3QBYQVjqqbAEGUBkx3qcgDqhTR6Hd9DbWo6IJeNKgLqZaGUfKfoV6EoNTzV8fUJK%2B3dFFpC3qMfmvuRlANlBFQgdvtXeZa3uF13SPQPbDJYAZFCfovj%2Fy3lkXmqy303b%2FOsxcswWgn6klC9QhrMde8IdgioOa%2BI3X6vnoXMNWuh70GOqUBTOGuXxIiFT9KfC2LSkgTLGS2F1TiHiDW1wPE6G9ReqoPlqCV81dtF9eGj256jjLLJvF5kGGp7lE1yp973GLQDB%2FGnL3U4GEwA7a9U2VPwXsCNbPdRP6m%2FCoDLKqcVZ4q70SfKCMpNNIBuDokA37uOolWriC0WoOaaq%2BBS1VIu%2Bfk%2BFdPLRZoZ4cS3FwYh9WNr%2FNu48NTwtu5fcF7fHhBZDmeljLH&X-Amz-Signature=62a1a8c071f6956a8aaabb5af0cfb9233ed4486f062e65ee8bf6884c5cb39e68&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWNNSWOV%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIErhVj8JVPMM9osa2hE0Aajzfq4tKkVnWBNih9MW26opAiEA%2FqXMxwuje2vhHUd292mg3X50%2FJdmMqbE9K5148B%2F5vsq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDBNdzSi13%2FlsqXE6jyrcA%2B2ztcNlXWLSc523avMQ5cmanTdOUG%2Byn%2FOxJXx7J%2BR7jFG1AWUVwLPzVAvvlhUcEw%2BMP71if0eDVjj%2FMBsPzouNwgGkyfEvgTSv0jLXkJcOIpbxlA6TrSdGleUOX9Pd2wg8AQrWVLqusZnqzBhyVSm25W1DfCLqa%2F%2FQ2KKfo2ByhH0gP0%2BW5wkeFsEFlSydKkC58th3nWQjrpUnYAX0HgVEZfm60H9d4LXgEpoR%2FYh9JXdUO1bsPGvPTF1Z9PtbdjTbB8L9g2q6vUmzzLcsiY%2FzTFbZesW8%2BuuFugs%2FGfaAQZ4FpEfgBImShNRn%2FPipyhPD79F5Wy4qhPmeK5Pd37vT%2BfhzZ3YGktdH5iLxBFapAE3rxtOh9Ido93BVTJZ%2FWBqnaJJ%2B1MDDXIm8MuczLF6vIgK69tT6Nb4f8i3Qoupo1mdctwOjIkhY16z0bCRPh9IvU7Pg2m9TUn9w43VK%2Fx3QBYQVjqqbAEGUBkx3qcgDqhTR6Hd9DbWo6IJeNKgLqZaGUfKfoV6EoNTzV8fUJK%2B3dFFpC3qMfmvuRlANlBFQgdvtXeZa3uF13SPQPbDJYAZFCfovj%2Fy3lkXmqy303b%2FOsxcswWgn6klC9QhrMde8IdgioOa%2BI3X6vnoXMNWuh70GOqUBTOGuXxIiFT9KfC2LSkgTLGS2F1TiHiDW1wPE6G9ReqoPlqCV81dtF9eGj256jjLLJvF5kGGp7lE1yp973GLQDB%2FGnL3U4GEwA7a9U2VPwXsCNbPdRP6m%2FCoDLKqcVZ4q70SfKCMpNNIBuDokA37uOolWriC0WoOaaq%2BBS1VIu%2Bfk%2BFdPLRZoZ4cS3FwYh9WNr%2FNu48NTwtu5fcF7fHhBZDmeljLH&X-Amz-Signature=7e2b9d848b053b82d20d6c5a794a554e1ae2be2465e2adfb491ca7db34592a8e&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
