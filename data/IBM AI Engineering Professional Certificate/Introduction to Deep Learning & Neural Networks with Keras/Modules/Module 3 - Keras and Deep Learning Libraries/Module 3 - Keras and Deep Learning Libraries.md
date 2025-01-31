

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662JLQPPJY%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC7zXp2zGiCxoUPmRa5SG8Ei1G0RNiu6Sxxk2VCdYn6DwIhAO%2Fgn2SGG7%2F82oXxyYcxSPwjY6jyETtsPi%2FdVD%2F1znT%2FKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzlBH7bwBnja7ExwDEq3AOuL0UfSC6d6GGxWUtgJFGGlNUdZbQadM5X62e2zvGabvwJh1lWgjDAUcDyLSaThscsIX7AbxkdFOk%2FdqDzE8Ld0QUJF8343Y3wdGZIChnbaA6v4e9DzwVY9sUyMiZ4bjfv1IGgYwR29ol4VHkMqB8aIBJOtoIbErKQvnffv%2BI2945pU82BIemi1xjs8NNcf%2BplpYOM9ETBppujeH%2FFWFN06tujN0QEVd%2FCiym6XylM2egx7CiD09gxoCfW8%2FyjjyDDox9P2c7jJCgYduklDsAC3%2FkV77U%2BaBhNOw0UkVwVBHyL61AvuX1jWOjyCCHCjv8MwmcbJzUw7ThQd9ijRiqev%2FgqSJdX%2FFiQPEC2GAZ99XiIHTup2Gki9ATL0VjIzDKsZwUMZC%2BLidjdf6tjjSGDQ2Hn5qs3QSQfHuyiuACSHiefB63mvhhDWjTuW%2BiI2FBYpk11UA6XiES%2B%2FIEWVPujnjxayRS0fIOmWDBsF4vv6SVyhcbiAuvklpqeCCBN1QjtxrmiltRf9%2B9u23U4Bh1GMg3bGZ0Dm7VdyF8e2TzFZFky570%2BTpsSemVDIN1euxsT61GE5W54CDtP2repKlRlcOQbeH8kSSHbJLlboPwKRtIQAQ45%2FKv%2BYGE1mjCF%2BPS8BjqkAadIfGydKSxdmvMXm27w7L1k3%2BWr0lvtS3LuQY%2FJ%2BxieR3aRlyVbWn3WhbHd9LhLLu6EZpagmcd1UwbAlu8xj7HVODB6A9LMbqdVdW%2B29lVpX5dXv7s7JYkTwTkfmtS4Qha26Z5PVb2gWsVUM8GczS3c633R5c8xLkc4rpQpASxv6rqsSUGkm67scwdZrw2YnrhVf9ZkrRPwmo0SAu2z%2FCWx17UC&X-Amz-Signature=9beb894e4290734dad1b4b0c54ae708cb7e30d5532976ce4ff40b28bd0e6da98&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662JLQPPJY%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC7zXp2zGiCxoUPmRa5SG8Ei1G0RNiu6Sxxk2VCdYn6DwIhAO%2Fgn2SGG7%2F82oXxyYcxSPwjY6jyETtsPi%2FdVD%2F1znT%2FKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzlBH7bwBnja7ExwDEq3AOuL0UfSC6d6GGxWUtgJFGGlNUdZbQadM5X62e2zvGabvwJh1lWgjDAUcDyLSaThscsIX7AbxkdFOk%2FdqDzE8Ld0QUJF8343Y3wdGZIChnbaA6v4e9DzwVY9sUyMiZ4bjfv1IGgYwR29ol4VHkMqB8aIBJOtoIbErKQvnffv%2BI2945pU82BIemi1xjs8NNcf%2BplpYOM9ETBppujeH%2FFWFN06tujN0QEVd%2FCiym6XylM2egx7CiD09gxoCfW8%2FyjjyDDox9P2c7jJCgYduklDsAC3%2FkV77U%2BaBhNOw0UkVwVBHyL61AvuX1jWOjyCCHCjv8MwmcbJzUw7ThQd9ijRiqev%2FgqSJdX%2FFiQPEC2GAZ99XiIHTup2Gki9ATL0VjIzDKsZwUMZC%2BLidjdf6tjjSGDQ2Hn5qs3QSQfHuyiuACSHiefB63mvhhDWjTuW%2BiI2FBYpk11UA6XiES%2B%2FIEWVPujnjxayRS0fIOmWDBsF4vv6SVyhcbiAuvklpqeCCBN1QjtxrmiltRf9%2B9u23U4Bh1GMg3bGZ0Dm7VdyF8e2TzFZFky570%2BTpsSemVDIN1euxsT61GE5W54CDtP2repKlRlcOQbeH8kSSHbJLlboPwKRtIQAQ45%2FKv%2BYGE1mjCF%2BPS8BjqkAadIfGydKSxdmvMXm27w7L1k3%2BWr0lvtS3LuQY%2FJ%2BxieR3aRlyVbWn3WhbHd9LhLLu6EZpagmcd1UwbAlu8xj7HVODB6A9LMbqdVdW%2B29lVpX5dXv7s7JYkTwTkfmtS4Qha26Z5PVb2gWsVUM8GczS3c633R5c8xLkc4rpQpASxv6rqsSUGkm67scwdZrw2YnrhVf9ZkrRPwmo0SAu2z%2FCWx17UC&X-Amz-Signature=7456e4905bfb95ccc7c4613fd286b06c33e311262013faf0b192579e89ee653c&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662JLQPPJY%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC7zXp2zGiCxoUPmRa5SG8Ei1G0RNiu6Sxxk2VCdYn6DwIhAO%2Fgn2SGG7%2F82oXxyYcxSPwjY6jyETtsPi%2FdVD%2F1znT%2FKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzlBH7bwBnja7ExwDEq3AOuL0UfSC6d6GGxWUtgJFGGlNUdZbQadM5X62e2zvGabvwJh1lWgjDAUcDyLSaThscsIX7AbxkdFOk%2FdqDzE8Ld0QUJF8343Y3wdGZIChnbaA6v4e9DzwVY9sUyMiZ4bjfv1IGgYwR29ol4VHkMqB8aIBJOtoIbErKQvnffv%2BI2945pU82BIemi1xjs8NNcf%2BplpYOM9ETBppujeH%2FFWFN06tujN0QEVd%2FCiym6XylM2egx7CiD09gxoCfW8%2FyjjyDDox9P2c7jJCgYduklDsAC3%2FkV77U%2BaBhNOw0UkVwVBHyL61AvuX1jWOjyCCHCjv8MwmcbJzUw7ThQd9ijRiqev%2FgqSJdX%2FFiQPEC2GAZ99XiIHTup2Gki9ATL0VjIzDKsZwUMZC%2BLidjdf6tjjSGDQ2Hn5qs3QSQfHuyiuACSHiefB63mvhhDWjTuW%2BiI2FBYpk11UA6XiES%2B%2FIEWVPujnjxayRS0fIOmWDBsF4vv6SVyhcbiAuvklpqeCCBN1QjtxrmiltRf9%2B9u23U4Bh1GMg3bGZ0Dm7VdyF8e2TzFZFky570%2BTpsSemVDIN1euxsT61GE5W54CDtP2repKlRlcOQbeH8kSSHbJLlboPwKRtIQAQ45%2FKv%2BYGE1mjCF%2BPS8BjqkAadIfGydKSxdmvMXm27w7L1k3%2BWr0lvtS3LuQY%2FJ%2BxieR3aRlyVbWn3WhbHd9LhLLu6EZpagmcd1UwbAlu8xj7HVODB6A9LMbqdVdW%2B29lVpX5dXv7s7JYkTwTkfmtS4Qha26Z5PVb2gWsVUM8GczS3c633R5c8xLkc4rpQpASxv6rqsSUGkm67scwdZrw2YnrhVf9ZkrRPwmo0SAu2z%2FCWx17UC&X-Amz-Signature=d1f1523c869d6c8be22951d34f433bad5bea7b899506fbb69f26c13391c4937f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665EDRFPFP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCr%2FzmBEOuXx9hdY4G3R1ZBQ%2BVgKIkK0zz6GRbjr0fNSQIhAJOSsC1dsIo%2Bpsia8khhWDopF%2FsjmU4JAZDkQHl%2F81WWKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwWIaC7l298Wna3tt4q3AO8tKVNV21H2qZQIpgEe%2FNvZfpWqojVEpHirNSI4c3hfgCMrQ4AgfUtyQJLFFJIfH0mjOMG%2FOhD8pYqoQmdPn2yc0oRmOGX4jTJAwDxuE31%2BFeWFsXL5FS5GpEugJV0EZECvJyiRMeqP7UtphgzBdUGUDghY5vFvzDRR6C7MfHNEdd41%2BTEXlMjcgul4WghM1C7SAz%2BKWJRcKEI85E6fvFPfCooHOJw1R43rduatvKqvLVZ6OvYog4Gu%2FnMfAm4EXsgfNJzfZrBhoo%2B3PZ%2Btlucl2XtSKF%2B4erKRGgQcmm0AA5xl7Yf%2F30iDVIrQ1dD4e553BiwjUIvkL9FixYz6FZpPP7H%2BtzfWlDF07AoK7HjVq6P3pfJqa3vz%2B7o1cB0oQBpza%2BXWbEHQsZnXyKb9F2suzO5zne6Aqhmr%2BDp0kBd42IazFDguBA5fockpiKZ5TZy89Sa%2FIJt4TPAl2EQUBEQSXZgKs4QmoqUA9S6fPOHeVO4roN5I8KuXxWuWvtEW8yaSLGczzvVTJfJB2ZLwk1GygHc%2BZlQ2s76AqiDnj%2FgVD%2BhPoA4KEpn%2B%2BK%2BgcHF98MwJclWMpfYFSUllTiiwJ3L%2BaHEKHB47vg%2BUYWGtl6ntOwc3LYOrcESvdAQHjDA%2BPS8BjqkARAYdvrmYkv3MjvgeDx9fIrx63dAM9Al1INQiSmleNuqUVHVeleJ6mqE9Fm%2F%2B4Og2d1IvQTUS%2BAm%2FH2%2BjoTl%2BPiinC%2FDfes6NWYlkD0QLvGmXrmP80%2FeWVhbs7ZCCMk5wEDdk0yDAX9LRZUYkrZKJWBVB%2Fau05VTJW0GU2H5paiFHKruW98aD7qlv3XcdHWA%2BsY6pAzNt61HTraQYm%2FjYayt0mCx&X-Amz-Signature=f3cf0239d93937581fe4fd9a1769e5ec77f79231a7d84f1a16d86474db757c9f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQYDF5MR%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCPpKAlU3q9k9w2oD%2FiUK9xtxoRiH1nxv52REmmv08EqwIgYrsvOqhn9jshHHMAAZv7k0aG8njsIV2OV7VYSB47DPsqiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBdrkIk%2FfCVD0lxeGSrcA2y19TlF6AMeH78ToT6iwrNYgvw%2F%2BhbPO6o3RsNHNxce2nuPpq6yHY9ePJkyfsey8h0j3bbYPzy0j9y5j93NyNbFazyDJLIjOCnRm7RVR4KV0Q1OT9sm9%2Ff4cA6rAqtwrE6mNevXinN522Wl1iSAvB4D%2FI0HkdwndmYtdLGxGh9QGESlJtxOIkSTBbN0D%2FYGStVvNak%2BDxP8Ghlv1JCJ1oX7XyVbRlMaOPZIeSEh5%2B1b19Oc2pNNV9ESi0r%2BXtvo0D51BRhvbqh80Gi4g9XOYB63OQsgKvh5o5umKhx5Ko2o89DwpeQdFVdXzpNprrjcbvtLEtMc9%2BOPy2%2FDlxGheepPBnYU3LEUzWSpWT%2Ba61rcKiZ7L9kI4H%2BKZSmOHAKSiCnGC4iH9wrRGQLUJ3EVGl%2FoLZJBJ%2Btl8mmsjrAa5fLTV%2FwtA%2FecG1G0JdqE9oKS69lr0%2BCpTeePGJYvdUC7LoHk4sIH5eiray57Pis%2FZN9HCF6O8nZZ1i1cdk%2FDl1S6GtpEXJ%2FYI1VdBs853bFMTvPtb752jjBtP5rnW7%2BvuNKOzIQQyI1ubg6PDhtOjXaaw1esKLGnU%2FbJSFDfe1VJv8qTWgywZMQ38%2BsqewKf5WFxpMxJ66fZzP%2Fc0c4jMKbb9LwGOqUB2Uj9EXRaI51orG5PkBlBEbpSCZRRxihj8UTI3BUxgGFP%2Bp5yWo54gkHfW5YnMBkRcAfj0ESkrgJ0Bv22sC%2FGLy71Y6RFuesCYvdpJelQmyUCCFi1IN6gv0xYQQuavqT0oWF2wikWbULjYvF5x%2BuzgpoJPkHLMxa8Zg7CurhvmsvewJDNEVbvfXS4JJppHcKYKIm4hYmQzmhSsi5u2hDE%2F5CxHijq&X-Amz-Signature=2821bb7811c80873fb87a8028742aac1cf8c5c26ad1fa029592684d581d48111&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662JLQPPJY%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC7zXp2zGiCxoUPmRa5SG8Ei1G0RNiu6Sxxk2VCdYn6DwIhAO%2Fgn2SGG7%2F82oXxyYcxSPwjY6jyETtsPi%2FdVD%2F1znT%2FKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzlBH7bwBnja7ExwDEq3AOuL0UfSC6d6GGxWUtgJFGGlNUdZbQadM5X62e2zvGabvwJh1lWgjDAUcDyLSaThscsIX7AbxkdFOk%2FdqDzE8Ld0QUJF8343Y3wdGZIChnbaA6v4e9DzwVY9sUyMiZ4bjfv1IGgYwR29ol4VHkMqB8aIBJOtoIbErKQvnffv%2BI2945pU82BIemi1xjs8NNcf%2BplpYOM9ETBppujeH%2FFWFN06tujN0QEVd%2FCiym6XylM2egx7CiD09gxoCfW8%2FyjjyDDox9P2c7jJCgYduklDsAC3%2FkV77U%2BaBhNOw0UkVwVBHyL61AvuX1jWOjyCCHCjv8MwmcbJzUw7ThQd9ijRiqev%2FgqSJdX%2FFiQPEC2GAZ99XiIHTup2Gki9ATL0VjIzDKsZwUMZC%2BLidjdf6tjjSGDQ2Hn5qs3QSQfHuyiuACSHiefB63mvhhDWjTuW%2BiI2FBYpk11UA6XiES%2B%2FIEWVPujnjxayRS0fIOmWDBsF4vv6SVyhcbiAuvklpqeCCBN1QjtxrmiltRf9%2B9u23U4Bh1GMg3bGZ0Dm7VdyF8e2TzFZFky570%2BTpsSemVDIN1euxsT61GE5W54CDtP2repKlRlcOQbeH8kSSHbJLlboPwKRtIQAQ45%2FKv%2BYGE1mjCF%2BPS8BjqkAadIfGydKSxdmvMXm27w7L1k3%2BWr0lvtS3LuQY%2FJ%2BxieR3aRlyVbWn3WhbHd9LhLLu6EZpagmcd1UwbAlu8xj7HVODB6A9LMbqdVdW%2B29lVpX5dXv7s7JYkTwTkfmtS4Qha26Z5PVb2gWsVUM8GczS3c633R5c8xLkc4rpQpASxv6rqsSUGkm67scwdZrw2YnrhVf9ZkrRPwmo0SAu2z%2FCWx17UC&X-Amz-Signature=a11082fed9a06ae27882b9777e53d739859bd0f400375d5c339c3de8b900538e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662JLQPPJY%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC7zXp2zGiCxoUPmRa5SG8Ei1G0RNiu6Sxxk2VCdYn6DwIhAO%2Fgn2SGG7%2F82oXxyYcxSPwjY6jyETtsPi%2FdVD%2F1znT%2FKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzlBH7bwBnja7ExwDEq3AOuL0UfSC6d6GGxWUtgJFGGlNUdZbQadM5X62e2zvGabvwJh1lWgjDAUcDyLSaThscsIX7AbxkdFOk%2FdqDzE8Ld0QUJF8343Y3wdGZIChnbaA6v4e9DzwVY9sUyMiZ4bjfv1IGgYwR29ol4VHkMqB8aIBJOtoIbErKQvnffv%2BI2945pU82BIemi1xjs8NNcf%2BplpYOM9ETBppujeH%2FFWFN06tujN0QEVd%2FCiym6XylM2egx7CiD09gxoCfW8%2FyjjyDDox9P2c7jJCgYduklDsAC3%2FkV77U%2BaBhNOw0UkVwVBHyL61AvuX1jWOjyCCHCjv8MwmcbJzUw7ThQd9ijRiqev%2FgqSJdX%2FFiQPEC2GAZ99XiIHTup2Gki9ATL0VjIzDKsZwUMZC%2BLidjdf6tjjSGDQ2Hn5qs3QSQfHuyiuACSHiefB63mvhhDWjTuW%2BiI2FBYpk11UA6XiES%2B%2FIEWVPujnjxayRS0fIOmWDBsF4vv6SVyhcbiAuvklpqeCCBN1QjtxrmiltRf9%2B9u23U4Bh1GMg3bGZ0Dm7VdyF8e2TzFZFky570%2BTpsSemVDIN1euxsT61GE5W54CDtP2repKlRlcOQbeH8kSSHbJLlboPwKRtIQAQ45%2FKv%2BYGE1mjCF%2BPS8BjqkAadIfGydKSxdmvMXm27w7L1k3%2BWr0lvtS3LuQY%2FJ%2BxieR3aRlyVbWn3WhbHd9LhLLu6EZpagmcd1UwbAlu8xj7HVODB6A9LMbqdVdW%2B29lVpX5dXv7s7JYkTwTkfmtS4Qha26Z5PVb2gWsVUM8GczS3c633R5c8xLkc4rpQpASxv6rqsSUGkm67scwdZrw2YnrhVf9ZkrRPwmo0SAu2z%2FCWx17UC&X-Amz-Signature=088bc0cfbc62dbc23702c4056f9c3112b2b63438500c476867375fdcb5e60d93&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662JLQPPJY%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC7zXp2zGiCxoUPmRa5SG8Ei1G0RNiu6Sxxk2VCdYn6DwIhAO%2Fgn2SGG7%2F82oXxyYcxSPwjY6jyETtsPi%2FdVD%2F1znT%2FKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzlBH7bwBnja7ExwDEq3AOuL0UfSC6d6GGxWUtgJFGGlNUdZbQadM5X62e2zvGabvwJh1lWgjDAUcDyLSaThscsIX7AbxkdFOk%2FdqDzE8Ld0QUJF8343Y3wdGZIChnbaA6v4e9DzwVY9sUyMiZ4bjfv1IGgYwR29ol4VHkMqB8aIBJOtoIbErKQvnffv%2BI2945pU82BIemi1xjs8NNcf%2BplpYOM9ETBppujeH%2FFWFN06tujN0QEVd%2FCiym6XylM2egx7CiD09gxoCfW8%2FyjjyDDox9P2c7jJCgYduklDsAC3%2FkV77U%2BaBhNOw0UkVwVBHyL61AvuX1jWOjyCCHCjv8MwmcbJzUw7ThQd9ijRiqev%2FgqSJdX%2FFiQPEC2GAZ99XiIHTup2Gki9ATL0VjIzDKsZwUMZC%2BLidjdf6tjjSGDQ2Hn5qs3QSQfHuyiuACSHiefB63mvhhDWjTuW%2BiI2FBYpk11UA6XiES%2B%2FIEWVPujnjxayRS0fIOmWDBsF4vv6SVyhcbiAuvklpqeCCBN1QjtxrmiltRf9%2B9u23U4Bh1GMg3bGZ0Dm7VdyF8e2TzFZFky570%2BTpsSemVDIN1euxsT61GE5W54CDtP2repKlRlcOQbeH8kSSHbJLlboPwKRtIQAQ45%2FKv%2BYGE1mjCF%2BPS8BjqkAadIfGydKSxdmvMXm27w7L1k3%2BWr0lvtS3LuQY%2FJ%2BxieR3aRlyVbWn3WhbHd9LhLLu6EZpagmcd1UwbAlu8xj7HVODB6A9LMbqdVdW%2B29lVpX5dXv7s7JYkTwTkfmtS4Qha26Z5PVb2gWsVUM8GczS3c633R5c8xLkc4rpQpASxv6rqsSUGkm67scwdZrw2YnrhVf9ZkrRPwmo0SAu2z%2FCWx17UC&X-Amz-Signature=e4b8771b91be5e2e66dcc26a77c489c322daa9b744201951c70cba9f1a2aeeee&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662JLQPPJY%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC7zXp2zGiCxoUPmRa5SG8Ei1G0RNiu6Sxxk2VCdYn6DwIhAO%2Fgn2SGG7%2F82oXxyYcxSPwjY6jyETtsPi%2FdVD%2F1znT%2FKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzlBH7bwBnja7ExwDEq3AOuL0UfSC6d6GGxWUtgJFGGlNUdZbQadM5X62e2zvGabvwJh1lWgjDAUcDyLSaThscsIX7AbxkdFOk%2FdqDzE8Ld0QUJF8343Y3wdGZIChnbaA6v4e9DzwVY9sUyMiZ4bjfv1IGgYwR29ol4VHkMqB8aIBJOtoIbErKQvnffv%2BI2945pU82BIemi1xjs8NNcf%2BplpYOM9ETBppujeH%2FFWFN06tujN0QEVd%2FCiym6XylM2egx7CiD09gxoCfW8%2FyjjyDDox9P2c7jJCgYduklDsAC3%2FkV77U%2BaBhNOw0UkVwVBHyL61AvuX1jWOjyCCHCjv8MwmcbJzUw7ThQd9ijRiqev%2FgqSJdX%2FFiQPEC2GAZ99XiIHTup2Gki9ATL0VjIzDKsZwUMZC%2BLidjdf6tjjSGDQ2Hn5qs3QSQfHuyiuACSHiefB63mvhhDWjTuW%2BiI2FBYpk11UA6XiES%2B%2FIEWVPujnjxayRS0fIOmWDBsF4vv6SVyhcbiAuvklpqeCCBN1QjtxrmiltRf9%2B9u23U4Bh1GMg3bGZ0Dm7VdyF8e2TzFZFky570%2BTpsSemVDIN1euxsT61GE5W54CDtP2repKlRlcOQbeH8kSSHbJLlboPwKRtIQAQ45%2FKv%2BYGE1mjCF%2BPS8BjqkAadIfGydKSxdmvMXm27w7L1k3%2BWr0lvtS3LuQY%2FJ%2BxieR3aRlyVbWn3WhbHd9LhLLu6EZpagmcd1UwbAlu8xj7HVODB6A9LMbqdVdW%2B29lVpX5dXv7s7JYkTwTkfmtS4Qha26Z5PVb2gWsVUM8GczS3c633R5c8xLkc4rpQpASxv6rqsSUGkm67scwdZrw2YnrhVf9ZkrRPwmo0SAu2z%2FCWx17UC&X-Amz-Signature=2273891d63c5b3940747c2494c3193de21ec49c0dcfed8c093cbaab08d4d7774&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
