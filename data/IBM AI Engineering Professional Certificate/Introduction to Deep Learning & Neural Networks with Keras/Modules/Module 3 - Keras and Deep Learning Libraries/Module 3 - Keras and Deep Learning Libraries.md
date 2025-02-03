

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R4XSFEH7%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJHMEUCIAW%2BHNZQPsu7uCodKSVVaXTrENuXKUc6rDj0U7XwttKuAiEAoKXJkMZXD0b1ruKM11OuO1MIBEVlInZEZpgvtg4ljc0q%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDKiCeVom9cG0jASyHircA%2FgI%2BrsWm1E46%2FJbWq2CoirW2ZjZObLGL2bU1YjHrdKpYdsGEbXQbV%2BO94LyTyzBuTdCYb3SVuIvKwRXaX9JCodJo2mGTpe4NFvdA26mQluQgwRr6UymXY%2BseZAU%2FFK1KpGJPVN7VOQ0qFBtQRdUFPDvoRB8VKjQKut4dfE1WNIcWwoSMdXz94CNJNbDUxrijEWXESACLVg4yGXdKYsxFpyv2YqZY8C6%2Farb0ynAqXCVJrl2IGuk%2B1PG2EQ92%2BpzUXGVtayiRtYIFrBHCinWhYfMQwHOFTDC8pTnJnE4%2B92PqbIupEj6PQPprF9Ba3fuH0VEtM9Jey3G7AaLsPioNBKPmmGGVUpsbAZSggMlMWc0gZYM5G0pXzazVVylTbotxiYYP2TwdoX2W7FBLJ5TT3O1NVTh1FAgM26Ep7XSNkZHgsYCZdPXHNGH6IzV3Ad8iWPVISmdG3o9DMoI%2BkxZfNH3nb4RxUfVV1wgfoXhgD2WhglGV8W0yl16bNW06%2BNljPZcB4jPa0XXZ5gU3flt3FOC3WRbdLvcfQQYn6QIUfpWSG2lsU5hv6LtKLC6CDcFFNchOch%2B6E6T6DOLMRK1xfIfByysNVZzQG4XjH3e5mAB5dZ121fPbCaF9OJmMMjZhL0GOqUBEDAbcuq02jABbRSbY%2BVwIGfJibqcr6xwKmZ6xHTFqan90FJCey2Kc0aI8EaYSNUvDfnEJFgjKHx5D0mkyAcNfbaQ%2Brx2CGFRZ7YnDjdxlCSJIu1CG2XB4tiuZGseqWxqGl5mOZqNzHuDBcM%2FeRql9Ji6bHAzms0viJS7Boc4QdDymI03v8r1Q1U7P%2BLnTGuKDn6EXT8b7%2FG9bhUt9u8nCOq3tBc%2B&X-Amz-Signature=344992f78482ebb881fd4ab2f28b57abc14695ee1b4cd81cf1cd09e9298d2610&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R4XSFEH7%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJHMEUCIAW%2BHNZQPsu7uCodKSVVaXTrENuXKUc6rDj0U7XwttKuAiEAoKXJkMZXD0b1ruKM11OuO1MIBEVlInZEZpgvtg4ljc0q%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDKiCeVom9cG0jASyHircA%2FgI%2BrsWm1E46%2FJbWq2CoirW2ZjZObLGL2bU1YjHrdKpYdsGEbXQbV%2BO94LyTyzBuTdCYb3SVuIvKwRXaX9JCodJo2mGTpe4NFvdA26mQluQgwRr6UymXY%2BseZAU%2FFK1KpGJPVN7VOQ0qFBtQRdUFPDvoRB8VKjQKut4dfE1WNIcWwoSMdXz94CNJNbDUxrijEWXESACLVg4yGXdKYsxFpyv2YqZY8C6%2Farb0ynAqXCVJrl2IGuk%2B1PG2EQ92%2BpzUXGVtayiRtYIFrBHCinWhYfMQwHOFTDC8pTnJnE4%2B92PqbIupEj6PQPprF9Ba3fuH0VEtM9Jey3G7AaLsPioNBKPmmGGVUpsbAZSggMlMWc0gZYM5G0pXzazVVylTbotxiYYP2TwdoX2W7FBLJ5TT3O1NVTh1FAgM26Ep7XSNkZHgsYCZdPXHNGH6IzV3Ad8iWPVISmdG3o9DMoI%2BkxZfNH3nb4RxUfVV1wgfoXhgD2WhglGV8W0yl16bNW06%2BNljPZcB4jPa0XXZ5gU3flt3FOC3WRbdLvcfQQYn6QIUfpWSG2lsU5hv6LtKLC6CDcFFNchOch%2B6E6T6DOLMRK1xfIfByysNVZzQG4XjH3e5mAB5dZ121fPbCaF9OJmMMjZhL0GOqUBEDAbcuq02jABbRSbY%2BVwIGfJibqcr6xwKmZ6xHTFqan90FJCey2Kc0aI8EaYSNUvDfnEJFgjKHx5D0mkyAcNfbaQ%2Brx2CGFRZ7YnDjdxlCSJIu1CG2XB4tiuZGseqWxqGl5mOZqNzHuDBcM%2FeRql9Ji6bHAzms0viJS7Boc4QdDymI03v8r1Q1U7P%2BLnTGuKDn6EXT8b7%2FG9bhUt9u8nCOq3tBc%2B&X-Amz-Signature=48ba122248cd1ac9e3c2669698f853078570f890bca1d85770a94f0bf9d02a68&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R4XSFEH7%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJHMEUCIAW%2BHNZQPsu7uCodKSVVaXTrENuXKUc6rDj0U7XwttKuAiEAoKXJkMZXD0b1ruKM11OuO1MIBEVlInZEZpgvtg4ljc0q%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDKiCeVom9cG0jASyHircA%2FgI%2BrsWm1E46%2FJbWq2CoirW2ZjZObLGL2bU1YjHrdKpYdsGEbXQbV%2BO94LyTyzBuTdCYb3SVuIvKwRXaX9JCodJo2mGTpe4NFvdA26mQluQgwRr6UymXY%2BseZAU%2FFK1KpGJPVN7VOQ0qFBtQRdUFPDvoRB8VKjQKut4dfE1WNIcWwoSMdXz94CNJNbDUxrijEWXESACLVg4yGXdKYsxFpyv2YqZY8C6%2Farb0ynAqXCVJrl2IGuk%2B1PG2EQ92%2BpzUXGVtayiRtYIFrBHCinWhYfMQwHOFTDC8pTnJnE4%2B92PqbIupEj6PQPprF9Ba3fuH0VEtM9Jey3G7AaLsPioNBKPmmGGVUpsbAZSggMlMWc0gZYM5G0pXzazVVylTbotxiYYP2TwdoX2W7FBLJ5TT3O1NVTh1FAgM26Ep7XSNkZHgsYCZdPXHNGH6IzV3Ad8iWPVISmdG3o9DMoI%2BkxZfNH3nb4RxUfVV1wgfoXhgD2WhglGV8W0yl16bNW06%2BNljPZcB4jPa0XXZ5gU3flt3FOC3WRbdLvcfQQYn6QIUfpWSG2lsU5hv6LtKLC6CDcFFNchOch%2B6E6T6DOLMRK1xfIfByysNVZzQG4XjH3e5mAB5dZ121fPbCaF9OJmMMjZhL0GOqUBEDAbcuq02jABbRSbY%2BVwIGfJibqcr6xwKmZ6xHTFqan90FJCey2Kc0aI8EaYSNUvDfnEJFgjKHx5D0mkyAcNfbaQ%2Brx2CGFRZ7YnDjdxlCSJIu1CG2XB4tiuZGseqWxqGl5mOZqNzHuDBcM%2FeRql9Ji6bHAzms0viJS7Boc4QdDymI03v8r1Q1U7P%2BLnTGuKDn6EXT8b7%2FG9bhUt9u8nCOq3tBc%2B&X-Amz-Signature=157d03a0b6b74717a37fa370f59a1f2a86d782a10aaf34438e3ef77b520132a6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TL2FUIEE%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJHMEUCIGdeVDQNswL2HZPXmVhx9nhwp1g6hSZxd4XLOl%2Bk0wVxAiEAm6ffCHIeyRs0QAwOPklZYe2%2FnldfMfM0QmHHrGIFvlYq%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDBBixyGnPU8VwCmpBSrcA%2FXEKrjkd9rht72PBtV%2BazwISHE6xJSmVzFSYIKFRkE1PSmxeD9s6KM8p9rCcTywb6r8DMOh%2BkmnImr6yshrit3ajR3RnL4BK5cRWjvuSf0vB%2BGzxU81k6l95LVou2eh418nyJa%2F1WvCwCxndy8WmmsehY0cYfnn%2BuC0FFxsyUBCnA2wj%2BatkBe7hU4BCJDj%2F050TxgzU4hnMtnFU6QYR%2BSOnDAPwO9lQzpyT8HGsm9PUSddb1uB0z2kVBV4M44a4n9m7VopaBWYQebOHaJ13BqUBP9LM8QJIyNA8EjrP1mLwENRDQ6AsNFmVF%2BeR%2Fs41agRb7tiy%2BTUuguDnwqkJNR1BTjsq8UhSJOmjMATG8PVX7j53B4K9hUe3diu3RCyJ9z9BWUzmQhbm0EX224V8%2FbEfld8nIJ%2BkR3urNSBBIJcniTu5MsBro9eJODm6%2FPy8qxF53R%2BMlgiTyQVN1HweBWh31hnAUv60bAySuOWaQw%2BvlydBuhmmLoYFmwJI0yYcLwzMxaX5dxvU4tHqjahfz0Ny4uI3KXQeIXc6XUybquNMN0%2B6tjzBAwU57jTPJi1x5xmx4q6muJWtRO0PpRWcLl8fqD7nK4ALs4%2F62GFlsMLXu3ZUhLMTH9fhv7MMNPZhL0GOqUBaTtg6IUgqGIcDCe8UYwodCg3tN9oueInly4gFTKbIg1ib4k1a6afRptou0Imm9qCit%2Bfs1DfSklPBri9L7s8kK9o5aZ7RFYXpSF7FSTwNp5cEx4pX62bR0YJDZIcn9YOfEMRRylNv45GrHeE5TbUh2N6kHyRuqIU5zsqoUhjEEhPPpTcpX3Gft%2BDe8LcqLWT8JLTo5cMh2BhE3vJLf2gAecpleV9&X-Amz-Signature=64026a95e1a1018a5c4b551e27166b95829d044fa5f10c6832b164aed1ec5f79&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WEASKYRR%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJHMEUCIQCfNRWsUdpday9rmeUuJIxgq1ayhOQ7y2QK1NYIZGRL5QIgDBFwJyMuAfjBQr%2FHbFpavgQ9oKDQ%2FsonrJIYMzWStLIq%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDPh%2BQ869djatrG0q5yrcA3ZrzqGgCpchEXnYN9UwWQ8fHcHqauq88UTBoTJLQP7QKXGWRF4kiVcdrPbNcgCJ5f6bc0Cdae3VEyb5ZJA5W3W1YSk1qSndY6e65VSMKfJpnY7y3Ish7xq9NJVH8ipB2ha1TgJiQX7FX4adEXx2DMmtgitkhYPwwx9fsb8IkEtaXBmioikjk5bW5Rm9AT5tvXbKa7RujUx8tWV10MSHu8H%2FlOuVzcIGCf6Kq0xKGvpG3DHFkbjp3SErul5hiUVKpWvv3qGg7IFG0Fv4ePk7IoJqSgaOjY8RtSOytJ8440qdajupp56XBUAVHwv2pkCKduJBXfSwzT27L97VBdUw5FFElM30ei3GIWrwJYJqa8rWGzLUqL4EEFSR1BMbtw7atFVuocpuoaG7d7VKJ9hiLY8U0xQuclYwC2lGbVGEgE1%2FZvXN3Lf1UlQqfVzVtYMHcgti2P43CMR6Hv0ObIFqU0cRB9TvRXFsi7LCmuUQhWuINXRcFKH%2FB1XCA40g8UrBgSuQ8uYyyq7T0%2FRt5avbK%2F0MUQHmujbSeIIkCcTdAf9tM%2Fk%2BAz5rDOlZjQ0461Yu%2FZ0ld4dquvaJv3YVfldfQM8YUYOgNg2x2X0lmjIegd6y8BVzkamS4ntNkZ7NMMnZhL0GOqUBWwSjbtYz2tgq60byY9do1O8jXL8ez7VgVNswzm8IXS2Tx%2F8o%2FggekVJ0ryxp2aAut4Zuvgn0Q2H%2FptOgkY%2BAANaLHSWsi93OaoatnxU38Hgm28kIAWjNzTlIyZdnuKg42DF2nuC5df07eL73IVcn%2BWUSDZ6eyupozphi56ON7XjAzk3exchCcDsid9hQnL6obBhS4O98As089VEJa9bPP6bZMi5C&X-Amz-Signature=3d878050d77d564964f4223ad11e496c719908bf75c5a82cccdf97686df9c013&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R4XSFEH7%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJHMEUCIAW%2BHNZQPsu7uCodKSVVaXTrENuXKUc6rDj0U7XwttKuAiEAoKXJkMZXD0b1ruKM11OuO1MIBEVlInZEZpgvtg4ljc0q%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDKiCeVom9cG0jASyHircA%2FgI%2BrsWm1E46%2FJbWq2CoirW2ZjZObLGL2bU1YjHrdKpYdsGEbXQbV%2BO94LyTyzBuTdCYb3SVuIvKwRXaX9JCodJo2mGTpe4NFvdA26mQluQgwRr6UymXY%2BseZAU%2FFK1KpGJPVN7VOQ0qFBtQRdUFPDvoRB8VKjQKut4dfE1WNIcWwoSMdXz94CNJNbDUxrijEWXESACLVg4yGXdKYsxFpyv2YqZY8C6%2Farb0ynAqXCVJrl2IGuk%2B1PG2EQ92%2BpzUXGVtayiRtYIFrBHCinWhYfMQwHOFTDC8pTnJnE4%2B92PqbIupEj6PQPprF9Ba3fuH0VEtM9Jey3G7AaLsPioNBKPmmGGVUpsbAZSggMlMWc0gZYM5G0pXzazVVylTbotxiYYP2TwdoX2W7FBLJ5TT3O1NVTh1FAgM26Ep7XSNkZHgsYCZdPXHNGH6IzV3Ad8iWPVISmdG3o9DMoI%2BkxZfNH3nb4RxUfVV1wgfoXhgD2WhglGV8W0yl16bNW06%2BNljPZcB4jPa0XXZ5gU3flt3FOC3WRbdLvcfQQYn6QIUfpWSG2lsU5hv6LtKLC6CDcFFNchOch%2B6E6T6DOLMRK1xfIfByysNVZzQG4XjH3e5mAB5dZ121fPbCaF9OJmMMjZhL0GOqUBEDAbcuq02jABbRSbY%2BVwIGfJibqcr6xwKmZ6xHTFqan90FJCey2Kc0aI8EaYSNUvDfnEJFgjKHx5D0mkyAcNfbaQ%2Brx2CGFRZ7YnDjdxlCSJIu1CG2XB4tiuZGseqWxqGl5mOZqNzHuDBcM%2FeRql9Ji6bHAzms0viJS7Boc4QdDymI03v8r1Q1U7P%2BLnTGuKDn6EXT8b7%2FG9bhUt9u8nCOq3tBc%2B&X-Amz-Signature=7f306776c3d9df1d2ef9dc2941b1ef9c258527ba8f2ca9a3ed151d555f508dd3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R4XSFEH7%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJHMEUCIAW%2BHNZQPsu7uCodKSVVaXTrENuXKUc6rDj0U7XwttKuAiEAoKXJkMZXD0b1ruKM11OuO1MIBEVlInZEZpgvtg4ljc0q%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDKiCeVom9cG0jASyHircA%2FgI%2BrsWm1E46%2FJbWq2CoirW2ZjZObLGL2bU1YjHrdKpYdsGEbXQbV%2BO94LyTyzBuTdCYb3SVuIvKwRXaX9JCodJo2mGTpe4NFvdA26mQluQgwRr6UymXY%2BseZAU%2FFK1KpGJPVN7VOQ0qFBtQRdUFPDvoRB8VKjQKut4dfE1WNIcWwoSMdXz94CNJNbDUxrijEWXESACLVg4yGXdKYsxFpyv2YqZY8C6%2Farb0ynAqXCVJrl2IGuk%2B1PG2EQ92%2BpzUXGVtayiRtYIFrBHCinWhYfMQwHOFTDC8pTnJnE4%2B92PqbIupEj6PQPprF9Ba3fuH0VEtM9Jey3G7AaLsPioNBKPmmGGVUpsbAZSggMlMWc0gZYM5G0pXzazVVylTbotxiYYP2TwdoX2W7FBLJ5TT3O1NVTh1FAgM26Ep7XSNkZHgsYCZdPXHNGH6IzV3Ad8iWPVISmdG3o9DMoI%2BkxZfNH3nb4RxUfVV1wgfoXhgD2WhglGV8W0yl16bNW06%2BNljPZcB4jPa0XXZ5gU3flt3FOC3WRbdLvcfQQYn6QIUfpWSG2lsU5hv6LtKLC6CDcFFNchOch%2B6E6T6DOLMRK1xfIfByysNVZzQG4XjH3e5mAB5dZ121fPbCaF9OJmMMjZhL0GOqUBEDAbcuq02jABbRSbY%2BVwIGfJibqcr6xwKmZ6xHTFqan90FJCey2Kc0aI8EaYSNUvDfnEJFgjKHx5D0mkyAcNfbaQ%2Brx2CGFRZ7YnDjdxlCSJIu1CG2XB4tiuZGseqWxqGl5mOZqNzHuDBcM%2FeRql9Ji6bHAzms0viJS7Boc4QdDymI03v8r1Q1U7P%2BLnTGuKDn6EXT8b7%2FG9bhUt9u8nCOq3tBc%2B&X-Amz-Signature=887c7859a18e9469403c118946b369712e03dc8930ee83ee83ff3f6f9bbfdf86&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R4XSFEH7%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJHMEUCIAW%2BHNZQPsu7uCodKSVVaXTrENuXKUc6rDj0U7XwttKuAiEAoKXJkMZXD0b1ruKM11OuO1MIBEVlInZEZpgvtg4ljc0q%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDKiCeVom9cG0jASyHircA%2FgI%2BrsWm1E46%2FJbWq2CoirW2ZjZObLGL2bU1YjHrdKpYdsGEbXQbV%2BO94LyTyzBuTdCYb3SVuIvKwRXaX9JCodJo2mGTpe4NFvdA26mQluQgwRr6UymXY%2BseZAU%2FFK1KpGJPVN7VOQ0qFBtQRdUFPDvoRB8VKjQKut4dfE1WNIcWwoSMdXz94CNJNbDUxrijEWXESACLVg4yGXdKYsxFpyv2YqZY8C6%2Farb0ynAqXCVJrl2IGuk%2B1PG2EQ92%2BpzUXGVtayiRtYIFrBHCinWhYfMQwHOFTDC8pTnJnE4%2B92PqbIupEj6PQPprF9Ba3fuH0VEtM9Jey3G7AaLsPioNBKPmmGGVUpsbAZSggMlMWc0gZYM5G0pXzazVVylTbotxiYYP2TwdoX2W7FBLJ5TT3O1NVTh1FAgM26Ep7XSNkZHgsYCZdPXHNGH6IzV3Ad8iWPVISmdG3o9DMoI%2BkxZfNH3nb4RxUfVV1wgfoXhgD2WhglGV8W0yl16bNW06%2BNljPZcB4jPa0XXZ5gU3flt3FOC3WRbdLvcfQQYn6QIUfpWSG2lsU5hv6LtKLC6CDcFFNchOch%2B6E6T6DOLMRK1xfIfByysNVZzQG4XjH3e5mAB5dZ121fPbCaF9OJmMMjZhL0GOqUBEDAbcuq02jABbRSbY%2BVwIGfJibqcr6xwKmZ6xHTFqan90FJCey2Kc0aI8EaYSNUvDfnEJFgjKHx5D0mkyAcNfbaQ%2Brx2CGFRZ7YnDjdxlCSJIu1CG2XB4tiuZGseqWxqGl5mOZqNzHuDBcM%2FeRql9Ji6bHAzms0viJS7Boc4QdDymI03v8r1Q1U7P%2BLnTGuKDn6EXT8b7%2FG9bhUt9u8nCOq3tBc%2B&X-Amz-Signature=8918a35f67cf563abaded75f61c592bc1c95841878c96b604c08adf7b994672c&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R4XSFEH7%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJHMEUCIAW%2BHNZQPsu7uCodKSVVaXTrENuXKUc6rDj0U7XwttKuAiEAoKXJkMZXD0b1ruKM11OuO1MIBEVlInZEZpgvtg4ljc0q%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDKiCeVom9cG0jASyHircA%2FgI%2BrsWm1E46%2FJbWq2CoirW2ZjZObLGL2bU1YjHrdKpYdsGEbXQbV%2BO94LyTyzBuTdCYb3SVuIvKwRXaX9JCodJo2mGTpe4NFvdA26mQluQgwRr6UymXY%2BseZAU%2FFK1KpGJPVN7VOQ0qFBtQRdUFPDvoRB8VKjQKut4dfE1WNIcWwoSMdXz94CNJNbDUxrijEWXESACLVg4yGXdKYsxFpyv2YqZY8C6%2Farb0ynAqXCVJrl2IGuk%2B1PG2EQ92%2BpzUXGVtayiRtYIFrBHCinWhYfMQwHOFTDC8pTnJnE4%2B92PqbIupEj6PQPprF9Ba3fuH0VEtM9Jey3G7AaLsPioNBKPmmGGVUpsbAZSggMlMWc0gZYM5G0pXzazVVylTbotxiYYP2TwdoX2W7FBLJ5TT3O1NVTh1FAgM26Ep7XSNkZHgsYCZdPXHNGH6IzV3Ad8iWPVISmdG3o9DMoI%2BkxZfNH3nb4RxUfVV1wgfoXhgD2WhglGV8W0yl16bNW06%2BNljPZcB4jPa0XXZ5gU3flt3FOC3WRbdLvcfQQYn6QIUfpWSG2lsU5hv6LtKLC6CDcFFNchOch%2B6E6T6DOLMRK1xfIfByysNVZzQG4XjH3e5mAB5dZ121fPbCaF9OJmMMjZhL0GOqUBEDAbcuq02jABbRSbY%2BVwIGfJibqcr6xwKmZ6xHTFqan90FJCey2Kc0aI8EaYSNUvDfnEJFgjKHx5D0mkyAcNfbaQ%2Brx2CGFRZ7YnDjdxlCSJIu1CG2XB4tiuZGseqWxqGl5mOZqNzHuDBcM%2FeRql9Ji6bHAzms0viJS7Boc4QdDymI03v8r1Q1U7P%2BLnTGuKDn6EXT8b7%2FG9bhUt9u8nCOq3tBc%2B&X-Amz-Signature=951c87b20847cbfb3df724545b5169ffd667b7798e21afb9bfbe904842c42131&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
