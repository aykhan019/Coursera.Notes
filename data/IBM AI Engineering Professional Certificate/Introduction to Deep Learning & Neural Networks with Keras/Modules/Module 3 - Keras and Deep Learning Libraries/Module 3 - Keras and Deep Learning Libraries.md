

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646BGMV7O%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJHMEUCIQCMDbU5aSRSMkueKuOvp1h8tGK572LiQ1Jfek4PH4%2B5eQIgZ0qujQPij2bbPzg4XyYe12DEHQvn3rHwropHGT%2BdofUq%2FwMIPhAAGgw2Mzc0MjMxODM4MDUiDBzzj09LRJ%2BYtQc4dyrcA9chHNjTSl%2Fm4VnzU0qSlDUZQ53UcGBPhwytp3vYdin163c97rPPCAJlY%2FOfZzsEVXt4hnb50DeX48RJI2xD9VEnKjyHOVX1nQTbg91os5BloNsdlEUEC7%2B2loLhfgq8dJYXXXtG00%2BtN46%2FbO9F8NBGRxNjdfTVmQWrOqURYM0XLD8JfFv%2BBeoH8bjnw8E%2Fw1XzULWRIQN9yY%2BdqjFYsn2ywkmhN2mv4E2tgc5oruBzKP72J0swJektHVlKK60W8F3BgXesf3r18T74ApwAXPvjOz%2F7TA8idhZFs%2BL86cSB%2B4kua84FQWbiDWSfctRBKmzMJB5loxfqcIVpM35sdVgkzoXBaxDvA%2F%2BjUvmD3qRvE93nM3E1uGlXcF38SzDqrR6BNOFhRozCymkEmb5Sd2mhfGSV2T02xvijyiCdVEAFo8CXvngcbd1T7goK0fDlYrZH2GlTo%2BV618DHHIbMuhGSPEMrH9TA2cKYyZqQBJkLWUXBfD0qlhKS51sFsvVA4fzap2ZbvomljozZCI7d4QmcZo0NNZhrL4oKLR11lXFSv4DdjLLGnQk3ra6L3kio6kkEF%2FQPGVod9F42CQyxt6QzIm6rZLvUvXH7EL0i66KwUA3huIzbbuoV1VAQMKffi70GOqUBMa1iOENbW1pHbz5UI81VzkQrfemVg3pjdsjZh8uNGaphxFhcR2u%2BCxR5Po7ui9gVj9e4TNRC%2F8STaOowP7qZ%2B%2FG97JgnSO%2Bp2ZBsc3V6Jg3UhZg0HupCQgYLlhFSa1hh6%2BZ82pbZoJHNFOHyEHRtQWu%2FUgicCKudHOQwaLY0leBGOebyiYI0GXT2fix5bxklIY%2Bz%2FL6Rh825vvPJisknX274fk2O&X-Amz-Signature=06ab5900fea009fad83a9880596064dc99012411ffbc2214d6fb47d7fdf69827&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646BGMV7O%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJHMEUCIQCMDbU5aSRSMkueKuOvp1h8tGK572LiQ1Jfek4PH4%2B5eQIgZ0qujQPij2bbPzg4XyYe12DEHQvn3rHwropHGT%2BdofUq%2FwMIPhAAGgw2Mzc0MjMxODM4MDUiDBzzj09LRJ%2BYtQc4dyrcA9chHNjTSl%2Fm4VnzU0qSlDUZQ53UcGBPhwytp3vYdin163c97rPPCAJlY%2FOfZzsEVXt4hnb50DeX48RJI2xD9VEnKjyHOVX1nQTbg91os5BloNsdlEUEC7%2B2loLhfgq8dJYXXXtG00%2BtN46%2FbO9F8NBGRxNjdfTVmQWrOqURYM0XLD8JfFv%2BBeoH8bjnw8E%2Fw1XzULWRIQN9yY%2BdqjFYsn2ywkmhN2mv4E2tgc5oruBzKP72J0swJektHVlKK60W8F3BgXesf3r18T74ApwAXPvjOz%2F7TA8idhZFs%2BL86cSB%2B4kua84FQWbiDWSfctRBKmzMJB5loxfqcIVpM35sdVgkzoXBaxDvA%2F%2BjUvmD3qRvE93nM3E1uGlXcF38SzDqrR6BNOFhRozCymkEmb5Sd2mhfGSV2T02xvijyiCdVEAFo8CXvngcbd1T7goK0fDlYrZH2GlTo%2BV618DHHIbMuhGSPEMrH9TA2cKYyZqQBJkLWUXBfD0qlhKS51sFsvVA4fzap2ZbvomljozZCI7d4QmcZo0NNZhrL4oKLR11lXFSv4DdjLLGnQk3ra6L3kio6kkEF%2FQPGVod9F42CQyxt6QzIm6rZLvUvXH7EL0i66KwUA3huIzbbuoV1VAQMKffi70GOqUBMa1iOENbW1pHbz5UI81VzkQrfemVg3pjdsjZh8uNGaphxFhcR2u%2BCxR5Po7ui9gVj9e4TNRC%2F8STaOowP7qZ%2B%2FG97JgnSO%2Bp2ZBsc3V6Jg3UhZg0HupCQgYLlhFSa1hh6%2BZ82pbZoJHNFOHyEHRtQWu%2FUgicCKudHOQwaLY0leBGOebyiYI0GXT2fix5bxklIY%2Bz%2FL6Rh825vvPJisknX274fk2O&X-Amz-Signature=8a1f66594f63ad10fa1442b168bc179b91973d0f6a62bef59f91e8011dd71859&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646BGMV7O%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJHMEUCIQCMDbU5aSRSMkueKuOvp1h8tGK572LiQ1Jfek4PH4%2B5eQIgZ0qujQPij2bbPzg4XyYe12DEHQvn3rHwropHGT%2BdofUq%2FwMIPhAAGgw2Mzc0MjMxODM4MDUiDBzzj09LRJ%2BYtQc4dyrcA9chHNjTSl%2Fm4VnzU0qSlDUZQ53UcGBPhwytp3vYdin163c97rPPCAJlY%2FOfZzsEVXt4hnb50DeX48RJI2xD9VEnKjyHOVX1nQTbg91os5BloNsdlEUEC7%2B2loLhfgq8dJYXXXtG00%2BtN46%2FbO9F8NBGRxNjdfTVmQWrOqURYM0XLD8JfFv%2BBeoH8bjnw8E%2Fw1XzULWRIQN9yY%2BdqjFYsn2ywkmhN2mv4E2tgc5oruBzKP72J0swJektHVlKK60W8F3BgXesf3r18T74ApwAXPvjOz%2F7TA8idhZFs%2BL86cSB%2B4kua84FQWbiDWSfctRBKmzMJB5loxfqcIVpM35sdVgkzoXBaxDvA%2F%2BjUvmD3qRvE93nM3E1uGlXcF38SzDqrR6BNOFhRozCymkEmb5Sd2mhfGSV2T02xvijyiCdVEAFo8CXvngcbd1T7goK0fDlYrZH2GlTo%2BV618DHHIbMuhGSPEMrH9TA2cKYyZqQBJkLWUXBfD0qlhKS51sFsvVA4fzap2ZbvomljozZCI7d4QmcZo0NNZhrL4oKLR11lXFSv4DdjLLGnQk3ra6L3kio6kkEF%2FQPGVod9F42CQyxt6QzIm6rZLvUvXH7EL0i66KwUA3huIzbbuoV1VAQMKffi70GOqUBMa1iOENbW1pHbz5UI81VzkQrfemVg3pjdsjZh8uNGaphxFhcR2u%2BCxR5Po7ui9gVj9e4TNRC%2F8STaOowP7qZ%2B%2FG97JgnSO%2Bp2ZBsc3V6Jg3UhZg0HupCQgYLlhFSa1hh6%2BZ82pbZoJHNFOHyEHRtQWu%2FUgicCKudHOQwaLY0leBGOebyiYI0GXT2fix5bxklIY%2Bz%2FL6Rh825vvPJisknX274fk2O&X-Amz-Signature=7485e8b0143bf4a405f86841ec5f8957465a067e97ce1fe4d6f2f7c841d30b5a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SA4PGZ6T%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJIMEYCIQClOpv%2B%2F2cwg8UauLBjxDdbOX5gf%2B9Lg%2BbjE7F3LZUU1gIhAPhI8wWYr0NpRjhJXVzSRTz7RAF7GkU8uZwijjvFEIrCKv8DCD4QABoMNjM3NDIzMTgzODA1IgwnqODHAiL465J3UfQq3AMc7Ve3sLqs4y2As206LugIC1vZjGZ5GAQ5v2iTGH%2F9eKg%2FVFMuHkT4WizcqVd5AvoP1KCpQIp6Uqoy%2Fylm1px%2BZlNXF5g0tC%2BvpJ5CKfGzZtV4lUpXLlwZfdXlycFfJqMGfq%2Fbw%2Fn1xVJI0DdHkyiUYKuA7y%2F3CX8a%2FeVMhoz6wDo16lo5drnTCbrgCGnZGuVWW7EKqlh7y4RQuKyELO1C13eU13rPrv63m300%2FBNzEzSdWgT5GnJQMLxUo9PM02FfKSs6W3JfIcjN5zFcLsfPw%2BSQn%2FbdTLHUZai0M1wCpkEqapo578OZVFHTfPUIHk30pBhGOTn0efbAh8CNEhSfkM1a3eeIwHHUXCoyJga7rOYmiPHnvWNba5dsFW9VudWBrUdWHzzuqUNhrtSZP3OkGq55IyuIrnNf5fhmKZsf2n7qWctHYl1bXjBOKHJsA1YEUv%2F7pW8Yw3KcUw76NDisQ%2BaXCicjxGyPoGYOJpS9K8x5ZIre8EpvsYgmE2Taz6XtXJKF8FnssGmMxAdfwyXxZMnhkMDIzEIcihf%2B308KlYIaFjoiIzTTxpxQLQl0sG%2BDcnK%2Fn%2B5wxaRFq3A7aaKK%2Fk8EfeyDiusKBZywly4EYHBamgBRa4blsQCGJjDM3Yu9BjqkAZlpbo7oqnY6qlItXPKkn%2Frrp3DvEUB5dAuRd7BLKYHWWChfT513FJIftUO97BN1mZpZgN%2FChoucabDe6ggnUGL6AWyrapnzGR%2FHfLkM5oAKBFsXNevKTAIL6oF9m6QkDOtAY8NRzZNim4LRQKCzNQrbDvGd23KD8VHdUq%2B2gzEM0%2FILfeN2iUxVCnhZfxZw8qTj5C4K2Brpm1iY%2BEve9GUHy4hY&X-Amz-Signature=612a84bf4bc3d9bf158e39b4c2ca292ac45a47f3c0ffdd635e65235c876041f3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YN3ZKTHB%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJIMEYCIQDIYsFDi4WjDsYTGKvP6IoloImDL8rag2SbG5AUCEYiwgIhAMKCK24YpEd8QnE%2BSJvgxqPYI5DrquhOmCm0sIecTYVfKv8DCD4QABoMNjM3NDIzMTgzODA1Igy8knvWpfGJfnSqc84q3AMa39n8eDJYpns44KqSBCxrirbz0yG4ICwVkjCr9MdxQ0jhh6F7rW7eMovS1H09cik6wJ9vxjHpIVlFtoSwSjcEY1EJ1L15XL3jCviAnRd5%2FHE0qvPf4ofgjCwftpWilu%2BrWLg4ynOyAuU3ouD0PtniNv9h20FdtGnErL%2FQQPRJ0PRqv%2FHq8MmSkkoww06Hr%2B%2FdumAqV7HZsfSpZTF9wTJVPqMb8icEaWv4S4XgYlfpmDXepD8kv3U%2FdQJNTGsLoZDVDtFAfQHRMI9JoJBID0DNlAI9zjXFtC2FlxxzLeN5dGuA%2BolVc1MQtZ31A8ys7XIIs4DwdHgfxv3OI1HlOf43lLeMLN1QljS7x2iCFgYwO9p4Fe8yvFl84F45FcZ2y5gq7lC0e%2FYZAPc8YRkYJWujxKg5dofok6fKKnLMZ4eY%2FsHhDtID%2F5Oiu1F0zpnQA93o53QW1neDPm4uXyRLp3bBGsBg3UMkHr%2BRy9m%2FWdreu2lVS0Pg4uTG0Jj1IaAUaJjHeTgac1euXkOf6I%2BBbpFg0qVgOC8%2BNfHzU1UDSTS1cElWR7N8qnQJKBLVFOnB%2FIr9yO2TtJl3AsSjV43767kuWZdcbT5%2BnREDnUhXKGOXZgaCApRe6R1g8AZFVzCc3ou9BjqkAY7GR2qG7f%2B3I1LSfaEVI02qr9gYG07Cr4S9X1ynvgIZqS4hRxh2xEMgtpks%2BFN4y1PrSUrBgIcUnLHPiA%2BP%2FXmDxqdMEqOQ7aPTkW7EGaYsutGEACw%2Beax3m3lBEpLugoo2Z8knxmlJ3AGYrjmG%2FdyVknV%2FUhyRs3a63EOAPMTRxDK2ijeFX6GUgtNNIbrpet7JXbg4nU8PeIjRKVhCQ7D%2Byhy1&X-Amz-Signature=5c9da8df8b2304fb5b0cde4f6c526b3290921dbb771c8c68b3e534cb0d166d49&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646BGMV7O%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJHMEUCIQCMDbU5aSRSMkueKuOvp1h8tGK572LiQ1Jfek4PH4%2B5eQIgZ0qujQPij2bbPzg4XyYe12DEHQvn3rHwropHGT%2BdofUq%2FwMIPhAAGgw2Mzc0MjMxODM4MDUiDBzzj09LRJ%2BYtQc4dyrcA9chHNjTSl%2Fm4VnzU0qSlDUZQ53UcGBPhwytp3vYdin163c97rPPCAJlY%2FOfZzsEVXt4hnb50DeX48RJI2xD9VEnKjyHOVX1nQTbg91os5BloNsdlEUEC7%2B2loLhfgq8dJYXXXtG00%2BtN46%2FbO9F8NBGRxNjdfTVmQWrOqURYM0XLD8JfFv%2BBeoH8bjnw8E%2Fw1XzULWRIQN9yY%2BdqjFYsn2ywkmhN2mv4E2tgc5oruBzKP72J0swJektHVlKK60W8F3BgXesf3r18T74ApwAXPvjOz%2F7TA8idhZFs%2BL86cSB%2B4kua84FQWbiDWSfctRBKmzMJB5loxfqcIVpM35sdVgkzoXBaxDvA%2F%2BjUvmD3qRvE93nM3E1uGlXcF38SzDqrR6BNOFhRozCymkEmb5Sd2mhfGSV2T02xvijyiCdVEAFo8CXvngcbd1T7goK0fDlYrZH2GlTo%2BV618DHHIbMuhGSPEMrH9TA2cKYyZqQBJkLWUXBfD0qlhKS51sFsvVA4fzap2ZbvomljozZCI7d4QmcZo0NNZhrL4oKLR11lXFSv4DdjLLGnQk3ra6L3kio6kkEF%2FQPGVod9F42CQyxt6QzIm6rZLvUvXH7EL0i66KwUA3huIzbbuoV1VAQMKffi70GOqUBMa1iOENbW1pHbz5UI81VzkQrfemVg3pjdsjZh8uNGaphxFhcR2u%2BCxR5Po7ui9gVj9e4TNRC%2F8STaOowP7qZ%2B%2FG97JgnSO%2Bp2ZBsc3V6Jg3UhZg0HupCQgYLlhFSa1hh6%2BZ82pbZoJHNFOHyEHRtQWu%2FUgicCKudHOQwaLY0leBGOebyiYI0GXT2fix5bxklIY%2Bz%2FL6Rh825vvPJisknX274fk2O&X-Amz-Signature=883dd119625587686446b99148d00b1081a1617e3b10b6b52a69478b7b03ae2d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646BGMV7O%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJHMEUCIQCMDbU5aSRSMkueKuOvp1h8tGK572LiQ1Jfek4PH4%2B5eQIgZ0qujQPij2bbPzg4XyYe12DEHQvn3rHwropHGT%2BdofUq%2FwMIPhAAGgw2Mzc0MjMxODM4MDUiDBzzj09LRJ%2BYtQc4dyrcA9chHNjTSl%2Fm4VnzU0qSlDUZQ53UcGBPhwytp3vYdin163c97rPPCAJlY%2FOfZzsEVXt4hnb50DeX48RJI2xD9VEnKjyHOVX1nQTbg91os5BloNsdlEUEC7%2B2loLhfgq8dJYXXXtG00%2BtN46%2FbO9F8NBGRxNjdfTVmQWrOqURYM0XLD8JfFv%2BBeoH8bjnw8E%2Fw1XzULWRIQN9yY%2BdqjFYsn2ywkmhN2mv4E2tgc5oruBzKP72J0swJektHVlKK60W8F3BgXesf3r18T74ApwAXPvjOz%2F7TA8idhZFs%2BL86cSB%2B4kua84FQWbiDWSfctRBKmzMJB5loxfqcIVpM35sdVgkzoXBaxDvA%2F%2BjUvmD3qRvE93nM3E1uGlXcF38SzDqrR6BNOFhRozCymkEmb5Sd2mhfGSV2T02xvijyiCdVEAFo8CXvngcbd1T7goK0fDlYrZH2GlTo%2BV618DHHIbMuhGSPEMrH9TA2cKYyZqQBJkLWUXBfD0qlhKS51sFsvVA4fzap2ZbvomljozZCI7d4QmcZo0NNZhrL4oKLR11lXFSv4DdjLLGnQk3ra6L3kio6kkEF%2FQPGVod9F42CQyxt6QzIm6rZLvUvXH7EL0i66KwUA3huIzbbuoV1VAQMKffi70GOqUBMa1iOENbW1pHbz5UI81VzkQrfemVg3pjdsjZh8uNGaphxFhcR2u%2BCxR5Po7ui9gVj9e4TNRC%2F8STaOowP7qZ%2B%2FG97JgnSO%2Bp2ZBsc3V6Jg3UhZg0HupCQgYLlhFSa1hh6%2BZ82pbZoJHNFOHyEHRtQWu%2FUgicCKudHOQwaLY0leBGOebyiYI0GXT2fix5bxklIY%2Bz%2FL6Rh825vvPJisknX274fk2O&X-Amz-Signature=09dc33e60ca248a394be8b002c8394da5029517717f0c5cfc3cffeeed8fc1e36&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646BGMV7O%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJHMEUCIQCMDbU5aSRSMkueKuOvp1h8tGK572LiQ1Jfek4PH4%2B5eQIgZ0qujQPij2bbPzg4XyYe12DEHQvn3rHwropHGT%2BdofUq%2FwMIPhAAGgw2Mzc0MjMxODM4MDUiDBzzj09LRJ%2BYtQc4dyrcA9chHNjTSl%2Fm4VnzU0qSlDUZQ53UcGBPhwytp3vYdin163c97rPPCAJlY%2FOfZzsEVXt4hnb50DeX48RJI2xD9VEnKjyHOVX1nQTbg91os5BloNsdlEUEC7%2B2loLhfgq8dJYXXXtG00%2BtN46%2FbO9F8NBGRxNjdfTVmQWrOqURYM0XLD8JfFv%2BBeoH8bjnw8E%2Fw1XzULWRIQN9yY%2BdqjFYsn2ywkmhN2mv4E2tgc5oruBzKP72J0swJektHVlKK60W8F3BgXesf3r18T74ApwAXPvjOz%2F7TA8idhZFs%2BL86cSB%2B4kua84FQWbiDWSfctRBKmzMJB5loxfqcIVpM35sdVgkzoXBaxDvA%2F%2BjUvmD3qRvE93nM3E1uGlXcF38SzDqrR6BNOFhRozCymkEmb5Sd2mhfGSV2T02xvijyiCdVEAFo8CXvngcbd1T7goK0fDlYrZH2GlTo%2BV618DHHIbMuhGSPEMrH9TA2cKYyZqQBJkLWUXBfD0qlhKS51sFsvVA4fzap2ZbvomljozZCI7d4QmcZo0NNZhrL4oKLR11lXFSv4DdjLLGnQk3ra6L3kio6kkEF%2FQPGVod9F42CQyxt6QzIm6rZLvUvXH7EL0i66KwUA3huIzbbuoV1VAQMKffi70GOqUBMa1iOENbW1pHbz5UI81VzkQrfemVg3pjdsjZh8uNGaphxFhcR2u%2BCxR5Po7ui9gVj9e4TNRC%2F8STaOowP7qZ%2B%2FG97JgnSO%2Bp2ZBsc3V6Jg3UhZg0HupCQgYLlhFSa1hh6%2BZ82pbZoJHNFOHyEHRtQWu%2FUgicCKudHOQwaLY0leBGOebyiYI0GXT2fix5bxklIY%2Bz%2FL6Rh825vvPJisknX274fk2O&X-Amz-Signature=27ad7acd0f5a3718fa2fc92d7ed57bc223cefb30c89e716ed8f26a1bd3219c23&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646BGMV7O%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJHMEUCIQCMDbU5aSRSMkueKuOvp1h8tGK572LiQ1Jfek4PH4%2B5eQIgZ0qujQPij2bbPzg4XyYe12DEHQvn3rHwropHGT%2BdofUq%2FwMIPhAAGgw2Mzc0MjMxODM4MDUiDBzzj09LRJ%2BYtQc4dyrcA9chHNjTSl%2Fm4VnzU0qSlDUZQ53UcGBPhwytp3vYdin163c97rPPCAJlY%2FOfZzsEVXt4hnb50DeX48RJI2xD9VEnKjyHOVX1nQTbg91os5BloNsdlEUEC7%2B2loLhfgq8dJYXXXtG00%2BtN46%2FbO9F8NBGRxNjdfTVmQWrOqURYM0XLD8JfFv%2BBeoH8bjnw8E%2Fw1XzULWRIQN9yY%2BdqjFYsn2ywkmhN2mv4E2tgc5oruBzKP72J0swJektHVlKK60W8F3BgXesf3r18T74ApwAXPvjOz%2F7TA8idhZFs%2BL86cSB%2B4kua84FQWbiDWSfctRBKmzMJB5loxfqcIVpM35sdVgkzoXBaxDvA%2F%2BjUvmD3qRvE93nM3E1uGlXcF38SzDqrR6BNOFhRozCymkEmb5Sd2mhfGSV2T02xvijyiCdVEAFo8CXvngcbd1T7goK0fDlYrZH2GlTo%2BV618DHHIbMuhGSPEMrH9TA2cKYyZqQBJkLWUXBfD0qlhKS51sFsvVA4fzap2ZbvomljozZCI7d4QmcZo0NNZhrL4oKLR11lXFSv4DdjLLGnQk3ra6L3kio6kkEF%2FQPGVod9F42CQyxt6QzIm6rZLvUvXH7EL0i66KwUA3huIzbbuoV1VAQMKffi70GOqUBMa1iOENbW1pHbz5UI81VzkQrfemVg3pjdsjZh8uNGaphxFhcR2u%2BCxR5Po7ui9gVj9e4TNRC%2F8STaOowP7qZ%2B%2FG97JgnSO%2Bp2ZBsc3V6Jg3UhZg0HupCQgYLlhFSa1hh6%2BZ82pbZoJHNFOHyEHRtQWu%2FUgicCKudHOQwaLY0leBGOebyiYI0GXT2fix5bxklIY%2Bz%2FL6Rh825vvPJisknX274fk2O&X-Amz-Signature=4719bf4646d9170c81daecaa077bb7633f03d1cb39e115b4e452afd2058a3373&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
