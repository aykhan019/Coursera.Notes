

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667OOF7IWN%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQDUd%2B2ecGiOnEewJsWIarx4XS6%2FRaHyPQqwMdJIiqL%2BxwIgGJIS%2BMltZjI9XT1fpF%2B1gv1e%2FwoKwbZcwkaIcomfNTIq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDG1v2OXpbEu7%2BYPKLSrcA1WgatwjrYtw7Nv1eo%2FM3%2FmXX8SWkZaOWmorZqw%2BxkcKaAGAq5npghUN3Bh4qqY3NJxgsR0oTQDk%2FGkgbtk1w9zT7tvhJlgAwBXsrL2dfM5fopNAHQahel7H2Q189lu01jqsQP%2FvKFHFHxuVzS2RIn07CgJizi9BiR%2Fj5J8TBcg3pIDnnd6cpfWenTAVpLsqk%2FBPsZBLdPYwxYwnPsUpF5z71gMZYmKaQq%2F0Ef%2BYpYaSkB%2B7acJNVwgIBQ%2Fg0H1XzY9FV4gvjKji7e1293MFb0vLVCGxWnanfRVI10ukKg8Bb%2FGc%2Bx4Z6FDR9Lww9usz19HW8C2NE7eIFjrPB75LnN%2FJDWq2DX4LKEv1JjBiDTMdrlSooOSwf6eoDGgMHz0lY1LdazYGgsXEnNQPqd%2FHxVHPBEHqNpgG04rezr7XEofLfYkzGlq7eiyJE60NetTC3bkkqO6w25IwRRO7nMqnsG4kvMBrXjIab1%2B1a01LPJT%2Fd1heFfSZAcrPzwu6nId9DGdWQUhobnhV%2BfG0xlh9Mf5uYJuXpu2uxn3%2FCZ3COyb%2BojbJkp2z%2B6CZ1K6W4p51bt6qHQ1nFXda%2FP2lCruseqIvN3grL9wcavSwx7ke8XfxlzhjKrEM6JIQ7GdVMKDskb0GOqUBOA4cCj%2BReYa9z3ObqVAXTq1s0hzVugTIGTlee0klw3pnjskn4ixXDYI0K8mvPuTNbInQvDfvbVwLBwAxJFxnI09Q60ICPQjW6yr0TOUitGSSj2ukJwQj6pjXQSTx5gnzsW9pSktgZYSKy%2BbjSYc%2Fsx0tDT3Zr3y%2B0l0q1UHqgZmlzBUF6rvykBAKDKu6aDM28z1PnlV8vyiqGKmsuYY7sTwfWwj6&X-Amz-Signature=263188095416ea806934cb19b3001e5d98a31edabdbb7f636518f2179dad41c2&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667OOF7IWN%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQDUd%2B2ecGiOnEewJsWIarx4XS6%2FRaHyPQqwMdJIiqL%2BxwIgGJIS%2BMltZjI9XT1fpF%2B1gv1e%2FwoKwbZcwkaIcomfNTIq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDG1v2OXpbEu7%2BYPKLSrcA1WgatwjrYtw7Nv1eo%2FM3%2FmXX8SWkZaOWmorZqw%2BxkcKaAGAq5npghUN3Bh4qqY3NJxgsR0oTQDk%2FGkgbtk1w9zT7tvhJlgAwBXsrL2dfM5fopNAHQahel7H2Q189lu01jqsQP%2FvKFHFHxuVzS2RIn07CgJizi9BiR%2Fj5J8TBcg3pIDnnd6cpfWenTAVpLsqk%2FBPsZBLdPYwxYwnPsUpF5z71gMZYmKaQq%2F0Ef%2BYpYaSkB%2B7acJNVwgIBQ%2Fg0H1XzY9FV4gvjKji7e1293MFb0vLVCGxWnanfRVI10ukKg8Bb%2FGc%2Bx4Z6FDR9Lww9usz19HW8C2NE7eIFjrPB75LnN%2FJDWq2DX4LKEv1JjBiDTMdrlSooOSwf6eoDGgMHz0lY1LdazYGgsXEnNQPqd%2FHxVHPBEHqNpgG04rezr7XEofLfYkzGlq7eiyJE60NetTC3bkkqO6w25IwRRO7nMqnsG4kvMBrXjIab1%2B1a01LPJT%2Fd1heFfSZAcrPzwu6nId9DGdWQUhobnhV%2BfG0xlh9Mf5uYJuXpu2uxn3%2FCZ3COyb%2BojbJkp2z%2B6CZ1K6W4p51bt6qHQ1nFXda%2FP2lCruseqIvN3grL9wcavSwx7ke8XfxlzhjKrEM6JIQ7GdVMKDskb0GOqUBOA4cCj%2BReYa9z3ObqVAXTq1s0hzVugTIGTlee0klw3pnjskn4ixXDYI0K8mvPuTNbInQvDfvbVwLBwAxJFxnI09Q60ICPQjW6yr0TOUitGSSj2ukJwQj6pjXQSTx5gnzsW9pSktgZYSKy%2BbjSYc%2Fsx0tDT3Zr3y%2B0l0q1UHqgZmlzBUF6rvykBAKDKu6aDM28z1PnlV8vyiqGKmsuYY7sTwfWwj6&X-Amz-Signature=fe20acfa1befd44185b5199d883099549faf96289d38ea01b795d487159fb2b3&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667OOF7IWN%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQDUd%2B2ecGiOnEewJsWIarx4XS6%2FRaHyPQqwMdJIiqL%2BxwIgGJIS%2BMltZjI9XT1fpF%2B1gv1e%2FwoKwbZcwkaIcomfNTIq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDG1v2OXpbEu7%2BYPKLSrcA1WgatwjrYtw7Nv1eo%2FM3%2FmXX8SWkZaOWmorZqw%2BxkcKaAGAq5npghUN3Bh4qqY3NJxgsR0oTQDk%2FGkgbtk1w9zT7tvhJlgAwBXsrL2dfM5fopNAHQahel7H2Q189lu01jqsQP%2FvKFHFHxuVzS2RIn07CgJizi9BiR%2Fj5J8TBcg3pIDnnd6cpfWenTAVpLsqk%2FBPsZBLdPYwxYwnPsUpF5z71gMZYmKaQq%2F0Ef%2BYpYaSkB%2B7acJNVwgIBQ%2Fg0H1XzY9FV4gvjKji7e1293MFb0vLVCGxWnanfRVI10ukKg8Bb%2FGc%2Bx4Z6FDR9Lww9usz19HW8C2NE7eIFjrPB75LnN%2FJDWq2DX4LKEv1JjBiDTMdrlSooOSwf6eoDGgMHz0lY1LdazYGgsXEnNQPqd%2FHxVHPBEHqNpgG04rezr7XEofLfYkzGlq7eiyJE60NetTC3bkkqO6w25IwRRO7nMqnsG4kvMBrXjIab1%2B1a01LPJT%2Fd1heFfSZAcrPzwu6nId9DGdWQUhobnhV%2BfG0xlh9Mf5uYJuXpu2uxn3%2FCZ3COyb%2BojbJkp2z%2B6CZ1K6W4p51bt6qHQ1nFXda%2FP2lCruseqIvN3grL9wcavSwx7ke8XfxlzhjKrEM6JIQ7GdVMKDskb0GOqUBOA4cCj%2BReYa9z3ObqVAXTq1s0hzVugTIGTlee0klw3pnjskn4ixXDYI0K8mvPuTNbInQvDfvbVwLBwAxJFxnI09Q60ICPQjW6yr0TOUitGSSj2ukJwQj6pjXQSTx5gnzsW9pSktgZYSKy%2BbjSYc%2Fsx0tDT3Zr3y%2B0l0q1UHqgZmlzBUF6rvykBAKDKu6aDM28z1PnlV8vyiqGKmsuYY7sTwfWwj6&X-Amz-Signature=1eae4c7717be61492bf254f3a8e7538e1d913619bfa2dd2dc66aafc7f92b304b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V6WON435%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIFPHeowtTFewVFsfheVYsYtO1wr0nRgLVMKhVVmOAqqyAiA3hiI8zau9HtijanLfqFRSTXuZMHFJYfDR%2FS2yM3i6Uyr%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMZrui%2Fsfu7%2BBeamlvKtwD3Qq4wNGlJV3Murp65WvkWaCIOJnDfE7JzhcUJpbbP83JQMlxQkNEYq73z8cP3YyzEcxjBdRBPflzXegS%2BQT9BzYTDUTWDg5nf8jL%2FrL8exRJNMB%2FbtP3zpMLu4E92Q7sDuCATr%2BdiPuDED%2F3Oh89GTL4RYS7KQbjLU0hE%2B2Pp2MvQslDcc4n2xho8mTdQLtt7gcbsb3s%2FoY4TReVOIpwGi6uYrrUicoa6wPjGSNwLTFp1SJ%2B3jIILhzx%2BzSZmpTs1p%2BKggyDf7Ry59ctv1moiAsRsmA3g9x%2Bxv%2FFmLt70cbj4jmR%2Fc8GOCTrYtHHHqtwSMGMrpRNcnguXHNAIZ3NgUzh50hEmBkHA7Tb5NDrGV7%2FRCcYvFX7JMAe%2BK%2FwIGVTkD%2Fl7fCRnXx6ZmQl6J8MKaAXRW88pOb9WBGvBciih5Jm8oFi5Nm9VqZ3FEZN%2FywFnrb%2BZlGgweI7QEn27AVxdWHPFhidcvUSNMShN%2BPsvNi%2F%2Fo%2FGUXrzX8uKm%2B0jYwiAnX03R45vr4MdHShBHVd%2FH7pVwpOb%2F5yVHfm5udyaQVeQ3EBRZySNW4%2Fcp6Z6menW5lPc0Y2%2BVQYPVz9is5NbSPPnLdOe%2F%2BkqPa1%2BWXh%2FBcL5qm2THIfu6T95gK0wquyRvQY6pgFgpxOGJVaZ967SaWIb5cBR7vwi%2F5gE2mryVMitS5HSho9vDDR3qLzVCDO3d%2F2gap6yUM%2BRG3OutCSDX8UnhZM5WirQGtdJDTvUh25J%2F2QgQk8h5lykCtqFdR0sdJAC%2F4oMGYOS4QIZClf3V0K5HU1lYhT0yX6p7VpU6EVOmNvt4W0KCVmYt0HiH4TxYYO7ORkVKZlN4RQ9MwXStmhzsxjiEsg5xBIw&X-Amz-Signature=1b87db149a73625324dafa96acb07bc7dbf017687f512f607a8df7f87aa55d2b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6MZLREX%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQDgWde9p73srAVew3xLBylwJaI%2FHLaQ4fIP05qzic%2BWvQIhAOFXvsUa6DRrFhurWAIDw0Eiv%2FGCNV6GLXGzX2SFaPELKv8DCFoQABoMNjM3NDIzMTgzODA1IgzdbZE5qVsOIYNhDg8q3AOGm%2F4f1ce9Hdy5R3b30%2B2PHIGqrxIim09hEllBmkkiWdz16gwUVTb8JDSJahzcDpAZ5lfRGQVcDkaqrUzrNYL%2Fm7W3X%2BalgZYpW8PXHJHR%2BkyKAGmt0QOTtn0hWPGZxQcUHhdKxl%2FGvMF90OiEamX%2B3cR9fQpQ6sJBr84p2AeoKRejgWaP8y4vREY0Xn%2FpZvYbi49cQpFmkMY5gL3Muy1kzofDXW2n%2Bnd8Dmux9CdUqzfllCsL1sw4xwk2tvCYWrH%2FvOWkWaRW8wBvCsmGDjjNWrV6yLiGZXpI37FjwSsBXbhK%2BNzf9h6CpDJZG6ok3V9g0FbLGwymmkKyOKpS%2FkgvU4jzO0of%2BzZAAEt1CNJBQZU%2BfBnrvciPBRHoIRbRKscGgTh6k5fgz1Do3s%2BiNXeexX5Lnmv4zoCO%2FuRg8Itluuiln2jOuUipzav0tMj%2FLWx0WmGiRR0fMf0UoJ%2BQQmVbenUtP9S7paVvViGiMYjW80R9TZHYWJP5vlERM5Iw11rXYVGYix%2BTmCkV1b%2FhPjCeOIeW0bqSj20g5uh3ONvGiyLYenf5Ms2gYKR8DI%2B01OHmC9RBEQJJi%2FodYCZdc3CvEF6pdb6iTyQES5TzqTpWUaaeodBGqtt4oJTCDjDZ7JG9BjqkAR1cMp4k2wprDDCv359xcfSCKqo37VIe9%2F%2F0w4jgGlv8Z4cIcPXXW601LZSX%2BdCVk4473aq7yjnc74FpFv1s0bxoSGvP970j6qMKb6v6hzwJx%2BOpu2Xmy%2FARuDJqMGpdM%2Bk2Kg8SHRK%2Bi542c1U9bESW9KSOPW%2FWA2P6ut9BvRa5527bYqmblDybZl3LeM%2FVsR%2Fm%2F7dCiLv5Zu8nis6j%2FawXRuoS&X-Amz-Signature=62fadbfe3e69cdc324d2e805865d1affcaa2c85051f962f0eb94c350fb58f87a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667OOF7IWN%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQDUd%2B2ecGiOnEewJsWIarx4XS6%2FRaHyPQqwMdJIiqL%2BxwIgGJIS%2BMltZjI9XT1fpF%2B1gv1e%2FwoKwbZcwkaIcomfNTIq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDG1v2OXpbEu7%2BYPKLSrcA1WgatwjrYtw7Nv1eo%2FM3%2FmXX8SWkZaOWmorZqw%2BxkcKaAGAq5npghUN3Bh4qqY3NJxgsR0oTQDk%2FGkgbtk1w9zT7tvhJlgAwBXsrL2dfM5fopNAHQahel7H2Q189lu01jqsQP%2FvKFHFHxuVzS2RIn07CgJizi9BiR%2Fj5J8TBcg3pIDnnd6cpfWenTAVpLsqk%2FBPsZBLdPYwxYwnPsUpF5z71gMZYmKaQq%2F0Ef%2BYpYaSkB%2B7acJNVwgIBQ%2Fg0H1XzY9FV4gvjKji7e1293MFb0vLVCGxWnanfRVI10ukKg8Bb%2FGc%2Bx4Z6FDR9Lww9usz19HW8C2NE7eIFjrPB75LnN%2FJDWq2DX4LKEv1JjBiDTMdrlSooOSwf6eoDGgMHz0lY1LdazYGgsXEnNQPqd%2FHxVHPBEHqNpgG04rezr7XEofLfYkzGlq7eiyJE60NetTC3bkkqO6w25IwRRO7nMqnsG4kvMBrXjIab1%2B1a01LPJT%2Fd1heFfSZAcrPzwu6nId9DGdWQUhobnhV%2BfG0xlh9Mf5uYJuXpu2uxn3%2FCZ3COyb%2BojbJkp2z%2B6CZ1K6W4p51bt6qHQ1nFXda%2FP2lCruseqIvN3grL9wcavSwx7ke8XfxlzhjKrEM6JIQ7GdVMKDskb0GOqUBOA4cCj%2BReYa9z3ObqVAXTq1s0hzVugTIGTlee0klw3pnjskn4ixXDYI0K8mvPuTNbInQvDfvbVwLBwAxJFxnI09Q60ICPQjW6yr0TOUitGSSj2ukJwQj6pjXQSTx5gnzsW9pSktgZYSKy%2BbjSYc%2Fsx0tDT3Zr3y%2B0l0q1UHqgZmlzBUF6rvykBAKDKu6aDM28z1PnlV8vyiqGKmsuYY7sTwfWwj6&X-Amz-Signature=2040a479fe3d3d521b4040af5ac39877b2e14dccdbaa8f8f5c31cd80808a9fbc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667OOF7IWN%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQDUd%2B2ecGiOnEewJsWIarx4XS6%2FRaHyPQqwMdJIiqL%2BxwIgGJIS%2BMltZjI9XT1fpF%2B1gv1e%2FwoKwbZcwkaIcomfNTIq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDG1v2OXpbEu7%2BYPKLSrcA1WgatwjrYtw7Nv1eo%2FM3%2FmXX8SWkZaOWmorZqw%2BxkcKaAGAq5npghUN3Bh4qqY3NJxgsR0oTQDk%2FGkgbtk1w9zT7tvhJlgAwBXsrL2dfM5fopNAHQahel7H2Q189lu01jqsQP%2FvKFHFHxuVzS2RIn07CgJizi9BiR%2Fj5J8TBcg3pIDnnd6cpfWenTAVpLsqk%2FBPsZBLdPYwxYwnPsUpF5z71gMZYmKaQq%2F0Ef%2BYpYaSkB%2B7acJNVwgIBQ%2Fg0H1XzY9FV4gvjKji7e1293MFb0vLVCGxWnanfRVI10ukKg8Bb%2FGc%2Bx4Z6FDR9Lww9usz19HW8C2NE7eIFjrPB75LnN%2FJDWq2DX4LKEv1JjBiDTMdrlSooOSwf6eoDGgMHz0lY1LdazYGgsXEnNQPqd%2FHxVHPBEHqNpgG04rezr7XEofLfYkzGlq7eiyJE60NetTC3bkkqO6w25IwRRO7nMqnsG4kvMBrXjIab1%2B1a01LPJT%2Fd1heFfSZAcrPzwu6nId9DGdWQUhobnhV%2BfG0xlh9Mf5uYJuXpu2uxn3%2FCZ3COyb%2BojbJkp2z%2B6CZ1K6W4p51bt6qHQ1nFXda%2FP2lCruseqIvN3grL9wcavSwx7ke8XfxlzhjKrEM6JIQ7GdVMKDskb0GOqUBOA4cCj%2BReYa9z3ObqVAXTq1s0hzVugTIGTlee0klw3pnjskn4ixXDYI0K8mvPuTNbInQvDfvbVwLBwAxJFxnI09Q60ICPQjW6yr0TOUitGSSj2ukJwQj6pjXQSTx5gnzsW9pSktgZYSKy%2BbjSYc%2Fsx0tDT3Zr3y%2B0l0q1UHqgZmlzBUF6rvykBAKDKu6aDM28z1PnlV8vyiqGKmsuYY7sTwfWwj6&X-Amz-Signature=b0e1c2b205189739796376999797fe9bdc9bae235e69a650425eafbc69ee3118&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667OOF7IWN%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQDUd%2B2ecGiOnEewJsWIarx4XS6%2FRaHyPQqwMdJIiqL%2BxwIgGJIS%2BMltZjI9XT1fpF%2B1gv1e%2FwoKwbZcwkaIcomfNTIq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDG1v2OXpbEu7%2BYPKLSrcA1WgatwjrYtw7Nv1eo%2FM3%2FmXX8SWkZaOWmorZqw%2BxkcKaAGAq5npghUN3Bh4qqY3NJxgsR0oTQDk%2FGkgbtk1w9zT7tvhJlgAwBXsrL2dfM5fopNAHQahel7H2Q189lu01jqsQP%2FvKFHFHxuVzS2RIn07CgJizi9BiR%2Fj5J8TBcg3pIDnnd6cpfWenTAVpLsqk%2FBPsZBLdPYwxYwnPsUpF5z71gMZYmKaQq%2F0Ef%2BYpYaSkB%2B7acJNVwgIBQ%2Fg0H1XzY9FV4gvjKji7e1293MFb0vLVCGxWnanfRVI10ukKg8Bb%2FGc%2Bx4Z6FDR9Lww9usz19HW8C2NE7eIFjrPB75LnN%2FJDWq2DX4LKEv1JjBiDTMdrlSooOSwf6eoDGgMHz0lY1LdazYGgsXEnNQPqd%2FHxVHPBEHqNpgG04rezr7XEofLfYkzGlq7eiyJE60NetTC3bkkqO6w25IwRRO7nMqnsG4kvMBrXjIab1%2B1a01LPJT%2Fd1heFfSZAcrPzwu6nId9DGdWQUhobnhV%2BfG0xlh9Mf5uYJuXpu2uxn3%2FCZ3COyb%2BojbJkp2z%2B6CZ1K6W4p51bt6qHQ1nFXda%2FP2lCruseqIvN3grL9wcavSwx7ke8XfxlzhjKrEM6JIQ7GdVMKDskb0GOqUBOA4cCj%2BReYa9z3ObqVAXTq1s0hzVugTIGTlee0klw3pnjskn4ixXDYI0K8mvPuTNbInQvDfvbVwLBwAxJFxnI09Q60ICPQjW6yr0TOUitGSSj2ukJwQj6pjXQSTx5gnzsW9pSktgZYSKy%2BbjSYc%2Fsx0tDT3Zr3y%2B0l0q1UHqgZmlzBUF6rvykBAKDKu6aDM28z1PnlV8vyiqGKmsuYY7sTwfWwj6&X-Amz-Signature=51657674510c031f6f528ce51095fbe350dc556f23c5049f8d2e30872878bd9f&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667OOF7IWN%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQDUd%2B2ecGiOnEewJsWIarx4XS6%2FRaHyPQqwMdJIiqL%2BxwIgGJIS%2BMltZjI9XT1fpF%2B1gv1e%2FwoKwbZcwkaIcomfNTIq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDG1v2OXpbEu7%2BYPKLSrcA1WgatwjrYtw7Nv1eo%2FM3%2FmXX8SWkZaOWmorZqw%2BxkcKaAGAq5npghUN3Bh4qqY3NJxgsR0oTQDk%2FGkgbtk1w9zT7tvhJlgAwBXsrL2dfM5fopNAHQahel7H2Q189lu01jqsQP%2FvKFHFHxuVzS2RIn07CgJizi9BiR%2Fj5J8TBcg3pIDnnd6cpfWenTAVpLsqk%2FBPsZBLdPYwxYwnPsUpF5z71gMZYmKaQq%2F0Ef%2BYpYaSkB%2B7acJNVwgIBQ%2Fg0H1XzY9FV4gvjKji7e1293MFb0vLVCGxWnanfRVI10ukKg8Bb%2FGc%2Bx4Z6FDR9Lww9usz19HW8C2NE7eIFjrPB75LnN%2FJDWq2DX4LKEv1JjBiDTMdrlSooOSwf6eoDGgMHz0lY1LdazYGgsXEnNQPqd%2FHxVHPBEHqNpgG04rezr7XEofLfYkzGlq7eiyJE60NetTC3bkkqO6w25IwRRO7nMqnsG4kvMBrXjIab1%2B1a01LPJT%2Fd1heFfSZAcrPzwu6nId9DGdWQUhobnhV%2BfG0xlh9Mf5uYJuXpu2uxn3%2FCZ3COyb%2BojbJkp2z%2B6CZ1K6W4p51bt6qHQ1nFXda%2FP2lCruseqIvN3grL9wcavSwx7ke8XfxlzhjKrEM6JIQ7GdVMKDskb0GOqUBOA4cCj%2BReYa9z3ObqVAXTq1s0hzVugTIGTlee0klw3pnjskn4ixXDYI0K8mvPuTNbInQvDfvbVwLBwAxJFxnI09Q60ICPQjW6yr0TOUitGSSj2ukJwQj6pjXQSTx5gnzsW9pSktgZYSKy%2BbjSYc%2Fsx0tDT3Zr3y%2B0l0q1UHqgZmlzBUF6rvykBAKDKu6aDM28z1PnlV8vyiqGKmsuYY7sTwfWwj6&X-Amz-Signature=dae50545708504118c66812f2c3cf5a47b7d5649a0fbb3015c7928f0b27b06a5&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
