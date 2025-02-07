

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646ALOUW3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIHEnYPqmPbgYWtjrkMGiEhVkgNrZ2k%2BNbfU4eAkkHFefAiBJhfiS1HdrsF8bzHadWdg0a%2FzWExLk78ErN36gWXEJtSr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIMHs%2FrMfQls1RB0UEKKtwDyrKD6GhFkzJSKO22P0L5S9LAkx8%2BbHuoc2cGfC3iK7Bez6h3ZgjH1JCljaZlxNtjArcQYwEJVJ6l8cdiRQckG9KQob%2FowcQgW6vZ9coZVD9toJxEUHPjemnVmPEHWjHMuSj0Dxf7LCUxzxjdrAIqKsc%2BKoihh3ps7ZAnWIM7%2BtXAMWfEmwWeqKM%2FGFFTs3WQXalwrLyIqdC0njNy8PjfUPzQ2Kz5llAIdXEHEhOA9r%2BTINcAW4lbginlH4drTAPD4fPv1SvtI7ZidYuusCq4AplqNMd%2BRBg6IJVLBqPqnwVdWpXo%2B30ecTCM%2F0K0epFeOR3dt0R35uV19x9jtP86UqXxwI4sKdOsyR1Wh3pVxMsIwbAlWL8%2BB6A507V%2BRprc1yDe1lOhWVxcuyOcTchvhsS8c47Gc5KydKnEATkMmr6Fv3Lw6R44lAb9HgBEvKjKTk5Elha%2Bz%2F5R2%2FG5T7FPgHW4arqRDqzkXNJkMoWKM0FryQJpFNn%2Bxe99GVx%2Fl%2BdmE6%2FaDKCukLWB%2FmwaWYITmZL44dCQ%2Bl3LcUynYbrZSHpoI%2FpC2ErlpCeLGMs06rhmefXAA7aRVBWPXFz%2BgFAPNgR3A0nHchHCTwA9CkiHWJARof2%2FjElFy%2BcX1Jkwy%2FmWvQY6pgHOpdxPMKBLtJiA%2BpMN3mdLxr%2F%2Bs50A1tLL3AcA2X8Dy0cGHtQrBS%2FwXMGnHXECUTMybxytzi%2F3UAC%2BXqUJUBwogUKjdxw82wVduxFWNuFW74kqgHEXbXvMy2gJIev0fYRxpq6gaqcJ1RJEMQi4FsFNB18btAQOfLJ8JWtDkLLR2QdG3CYSqzGofjoPTGNaOOhZDaSgt8ecWSHJrzvVrD7woIx9Auoy&X-Amz-Signature=f531a50a492d65cd200613ebf5c9996731aeaefcf22d77a2d5c505c5467e9d55&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646ALOUW3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIHEnYPqmPbgYWtjrkMGiEhVkgNrZ2k%2BNbfU4eAkkHFefAiBJhfiS1HdrsF8bzHadWdg0a%2FzWExLk78ErN36gWXEJtSr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIMHs%2FrMfQls1RB0UEKKtwDyrKD6GhFkzJSKO22P0L5S9LAkx8%2BbHuoc2cGfC3iK7Bez6h3ZgjH1JCljaZlxNtjArcQYwEJVJ6l8cdiRQckG9KQob%2FowcQgW6vZ9coZVD9toJxEUHPjemnVmPEHWjHMuSj0Dxf7LCUxzxjdrAIqKsc%2BKoihh3ps7ZAnWIM7%2BtXAMWfEmwWeqKM%2FGFFTs3WQXalwrLyIqdC0njNy8PjfUPzQ2Kz5llAIdXEHEhOA9r%2BTINcAW4lbginlH4drTAPD4fPv1SvtI7ZidYuusCq4AplqNMd%2BRBg6IJVLBqPqnwVdWpXo%2B30ecTCM%2F0K0epFeOR3dt0R35uV19x9jtP86UqXxwI4sKdOsyR1Wh3pVxMsIwbAlWL8%2BB6A507V%2BRprc1yDe1lOhWVxcuyOcTchvhsS8c47Gc5KydKnEATkMmr6Fv3Lw6R44lAb9HgBEvKjKTk5Elha%2Bz%2F5R2%2FG5T7FPgHW4arqRDqzkXNJkMoWKM0FryQJpFNn%2Bxe99GVx%2Fl%2BdmE6%2FaDKCukLWB%2FmwaWYITmZL44dCQ%2Bl3LcUynYbrZSHpoI%2FpC2ErlpCeLGMs06rhmefXAA7aRVBWPXFz%2BgFAPNgR3A0nHchHCTwA9CkiHWJARof2%2FjElFy%2BcX1Jkwy%2FmWvQY6pgHOpdxPMKBLtJiA%2BpMN3mdLxr%2F%2Bs50A1tLL3AcA2X8Dy0cGHtQrBS%2FwXMGnHXECUTMybxytzi%2F3UAC%2BXqUJUBwogUKjdxw82wVduxFWNuFW74kqgHEXbXvMy2gJIev0fYRxpq6gaqcJ1RJEMQi4FsFNB18btAQOfLJ8JWtDkLLR2QdG3CYSqzGofjoPTGNaOOhZDaSgt8ecWSHJrzvVrD7woIx9Auoy&X-Amz-Signature=26d82093086e180ad77a0ac5992efea1eada9afbdc15ac7430e190103101877b&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646ALOUW3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIHEnYPqmPbgYWtjrkMGiEhVkgNrZ2k%2BNbfU4eAkkHFefAiBJhfiS1HdrsF8bzHadWdg0a%2FzWExLk78ErN36gWXEJtSr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIMHs%2FrMfQls1RB0UEKKtwDyrKD6GhFkzJSKO22P0L5S9LAkx8%2BbHuoc2cGfC3iK7Bez6h3ZgjH1JCljaZlxNtjArcQYwEJVJ6l8cdiRQckG9KQob%2FowcQgW6vZ9coZVD9toJxEUHPjemnVmPEHWjHMuSj0Dxf7LCUxzxjdrAIqKsc%2BKoihh3ps7ZAnWIM7%2BtXAMWfEmwWeqKM%2FGFFTs3WQXalwrLyIqdC0njNy8PjfUPzQ2Kz5llAIdXEHEhOA9r%2BTINcAW4lbginlH4drTAPD4fPv1SvtI7ZidYuusCq4AplqNMd%2BRBg6IJVLBqPqnwVdWpXo%2B30ecTCM%2F0K0epFeOR3dt0R35uV19x9jtP86UqXxwI4sKdOsyR1Wh3pVxMsIwbAlWL8%2BB6A507V%2BRprc1yDe1lOhWVxcuyOcTchvhsS8c47Gc5KydKnEATkMmr6Fv3Lw6R44lAb9HgBEvKjKTk5Elha%2Bz%2F5R2%2FG5T7FPgHW4arqRDqzkXNJkMoWKM0FryQJpFNn%2Bxe99GVx%2Fl%2BdmE6%2FaDKCukLWB%2FmwaWYITmZL44dCQ%2Bl3LcUynYbrZSHpoI%2FpC2ErlpCeLGMs06rhmefXAA7aRVBWPXFz%2BgFAPNgR3A0nHchHCTwA9CkiHWJARof2%2FjElFy%2BcX1Jkwy%2FmWvQY6pgHOpdxPMKBLtJiA%2BpMN3mdLxr%2F%2Bs50A1tLL3AcA2X8Dy0cGHtQrBS%2FwXMGnHXECUTMybxytzi%2F3UAC%2BXqUJUBwogUKjdxw82wVduxFWNuFW74kqgHEXbXvMy2gJIev0fYRxpq6gaqcJ1RJEMQi4FsFNB18btAQOfLJ8JWtDkLLR2QdG3CYSqzGofjoPTGNaOOhZDaSgt8ecWSHJrzvVrD7woIx9Auoy&X-Amz-Signature=6c6a0d6a4cce6be0f84ea22545dcde25f540c4e53a3c69d0bda98d98deb29a56&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QB6ZUVLP%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJIMEYCIQDFuiNgkFw2wI4DjBs48QLZgxQLyN%2Bcjv6%2Fv2pZLyrJ8QIhAIYZh2NLV3X%2BGeY%2FC4Wr2GzPCU0f7nTrSTH7DE5ltNWHKv8DCHEQABoMNjM3NDIzMTgzODA1IgxTpHcB%2BnauCEQACiYq3AMB7gn8IdZkAJWfgTUDjhDOpopBU4yMu97lYV5pjzUsuYjp4MH2rRV2ZYx56IM3DGiFYl44zJ4WmzOQvc7sqBa41T6lgxVTmmpWDGqxtmEhiZwpy%2B0XTF2hkCsz5agcN6kegl31BTs6Bq%2FDQL1ltREb7ZGj4ngubXKdm8fut3rC5h627AHemSlIm1M8NpZegKfT0XERVMvTNcV%2FY3N3RHcu7Fp9tKoMQv%2Bsq8RvFg8bYt1aErJDskZ0dIvwRm5P8Voo3qP%2Fm4AFHOPBbaBG0hqbeIygYGXgsKKqIRE3uL5XKOpeUSUZlEGzab5xXXlyXZqLgISuCDfoxSgR1yoi76LtBsKtCCauOknN42HU4lfzHsJwK9SVdku1ThuZR0MBnAyxPAOjBmPCS06pBNXdG38f88D4ihsrImIVIURsFpkmO%2B872hgG42gvwsrX9nt3htbOabfxWO%2BLCskBx9U1JwekOkuwakARuzleBr%2F%2F2DIj%2B2%2Bqm40mKfQUiDvEvWwpXDplyisu9tLV3k6TGX9wHTqsuz2zru9aPptTUA7OEOFvVvrjwHGaqSJ0NygMc7p26Dd0hcZTtx1aB%2FTHXFQh2zvkVy22RKpfPuelSPq1ZhCxPl3BwaRgwIQRnHfEJzDF%2BZa9BjqkAbzqwOH1jSSejE5SSsK6bJp3Se4uze2U4j7mrAtL%2BORBNuaume%2FG9o8c8Xv7oEzYy%2BRcT4d%2FKmIBdFfF6lhZwulin6IZE2CMWx08DiuaA8da3ADeqTuTK8IPvXQNwh9ePPZkLaDTUpS5FWDwCaXNNRECSVTW9tjxsS1W6r%2F%2FKKPhPbWzupMuKlA8wmYDjIRH0zymGQIaFRobT2F7EJjagInQsYvk&X-Amz-Signature=24b508002f7f929f82708c5d4e987577bbdcfcd603d2d9d72b1e385307c45912&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46673DLTDBD%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIB084GLykXLAJjzQwTtOr%2BZYoP53o3I73sDHfkc75cxUAiEAmR1w9noU1raY0Xtx%2FX2YEhMTDSkH00fK0ZxtNzqxx3oq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDMuH4wWLji5L8HRf1CrcA7Sz9h39rj0ruzKd4x8LUBhs6HRNMkYVCqdprtHbpWddPZ6vSBQ8HX23UMers4svB4cC6V%2BXLB3nKpeJrSWBOgCRkv9zg1XjGhtU1Ck1cd0%2BIhRgpa%2FIaYMttTtdf8XE3Jato0x1JlRNhjOuatkYhPhdukI9TntraPIizXJGm2vhUvBBGmPS0aekeonW9asJsQYhUdNVwAsuWX3EtQeC9x3ppQTegcYDlPXqks3Zpg7awPTCpSFdAavyrCYhLL0xlQKF8dVIB2uPaB6lPXt96Ufvz%2ByIdqzPnUIH0xTqAubl1KqWkqm3DjfXTb77NCtWAUaIaMmY%2BIPJ7wlhLF2DM6pervspidwt3uya0EmHWwu%2FjK9Lh6clLWA0SQpNWdecUYxFBvPvhQJfuF2rzj%2BmtBH%2BgZwpJ7n%2BuUZelR6wpOkK9iXTdnH97x61v%2FuLJPzczK1ayiFi11im8P6vkukRoJ2uD33Dfwtdg%2BZzgdXlHskCpJagUQLtLNYAaXNFhRgl5%2BfBwuSnlXDpqMiyxBdc0FnmRn4KtB6aWLtu2tMUiEUq648w9LvBvZNRiTiWWaElPuxck38iVAjrCC0A0Aa%2FYE41EfUhlaJdguBCyGFhmkPGbAzTblJTvAeLuxS9MPf5lr0GOqUBPPRi4RHnK5%2FDzq7LnrKGMuJAYFRxUKiVfXzeKOVBJRMWFRnqoYcjchjsY79dGm6T2U1OvjN%2BKhO%2F%2Bm3fF1DEKij5SqAh6RGlOnYhe%2Fg8U%2FiodYD3LfKSp1Jmc6GCaD7smNziG5oAPaFcdjRPT1iHXxhPNssCnvQYekE6FNCtbgRwuqh2GrH3KFa5jIvIZ2R829n3BN845uOM9%2BgDqi5PWNphJSxm&X-Amz-Signature=e211b40526b0a4f815a7805f08f134cce9283f1bc5c0490d5d1803356a9d1580&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646ALOUW3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIHEnYPqmPbgYWtjrkMGiEhVkgNrZ2k%2BNbfU4eAkkHFefAiBJhfiS1HdrsF8bzHadWdg0a%2FzWExLk78ErN36gWXEJtSr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIMHs%2FrMfQls1RB0UEKKtwDyrKD6GhFkzJSKO22P0L5S9LAkx8%2BbHuoc2cGfC3iK7Bez6h3ZgjH1JCljaZlxNtjArcQYwEJVJ6l8cdiRQckG9KQob%2FowcQgW6vZ9coZVD9toJxEUHPjemnVmPEHWjHMuSj0Dxf7LCUxzxjdrAIqKsc%2BKoihh3ps7ZAnWIM7%2BtXAMWfEmwWeqKM%2FGFFTs3WQXalwrLyIqdC0njNy8PjfUPzQ2Kz5llAIdXEHEhOA9r%2BTINcAW4lbginlH4drTAPD4fPv1SvtI7ZidYuusCq4AplqNMd%2BRBg6IJVLBqPqnwVdWpXo%2B30ecTCM%2F0K0epFeOR3dt0R35uV19x9jtP86UqXxwI4sKdOsyR1Wh3pVxMsIwbAlWL8%2BB6A507V%2BRprc1yDe1lOhWVxcuyOcTchvhsS8c47Gc5KydKnEATkMmr6Fv3Lw6R44lAb9HgBEvKjKTk5Elha%2Bz%2F5R2%2FG5T7FPgHW4arqRDqzkXNJkMoWKM0FryQJpFNn%2Bxe99GVx%2Fl%2BdmE6%2FaDKCukLWB%2FmwaWYITmZL44dCQ%2Bl3LcUynYbrZSHpoI%2FpC2ErlpCeLGMs06rhmefXAA7aRVBWPXFz%2BgFAPNgR3A0nHchHCTwA9CkiHWJARof2%2FjElFy%2BcX1Jkwy%2FmWvQY6pgHOpdxPMKBLtJiA%2BpMN3mdLxr%2F%2Bs50A1tLL3AcA2X8Dy0cGHtQrBS%2FwXMGnHXECUTMybxytzi%2F3UAC%2BXqUJUBwogUKjdxw82wVduxFWNuFW74kqgHEXbXvMy2gJIev0fYRxpq6gaqcJ1RJEMQi4FsFNB18btAQOfLJ8JWtDkLLR2QdG3CYSqzGofjoPTGNaOOhZDaSgt8ecWSHJrzvVrD7woIx9Auoy&X-Amz-Signature=f8148f1a695e0d79d3907184bc39b64d4bdee8f1a6f9ecbd27a47d3f73150e71&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646ALOUW3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIHEnYPqmPbgYWtjrkMGiEhVkgNrZ2k%2BNbfU4eAkkHFefAiBJhfiS1HdrsF8bzHadWdg0a%2FzWExLk78ErN36gWXEJtSr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIMHs%2FrMfQls1RB0UEKKtwDyrKD6GhFkzJSKO22P0L5S9LAkx8%2BbHuoc2cGfC3iK7Bez6h3ZgjH1JCljaZlxNtjArcQYwEJVJ6l8cdiRQckG9KQob%2FowcQgW6vZ9coZVD9toJxEUHPjemnVmPEHWjHMuSj0Dxf7LCUxzxjdrAIqKsc%2BKoihh3ps7ZAnWIM7%2BtXAMWfEmwWeqKM%2FGFFTs3WQXalwrLyIqdC0njNy8PjfUPzQ2Kz5llAIdXEHEhOA9r%2BTINcAW4lbginlH4drTAPD4fPv1SvtI7ZidYuusCq4AplqNMd%2BRBg6IJVLBqPqnwVdWpXo%2B30ecTCM%2F0K0epFeOR3dt0R35uV19x9jtP86UqXxwI4sKdOsyR1Wh3pVxMsIwbAlWL8%2BB6A507V%2BRprc1yDe1lOhWVxcuyOcTchvhsS8c47Gc5KydKnEATkMmr6Fv3Lw6R44lAb9HgBEvKjKTk5Elha%2Bz%2F5R2%2FG5T7FPgHW4arqRDqzkXNJkMoWKM0FryQJpFNn%2Bxe99GVx%2Fl%2BdmE6%2FaDKCukLWB%2FmwaWYITmZL44dCQ%2Bl3LcUynYbrZSHpoI%2FpC2ErlpCeLGMs06rhmefXAA7aRVBWPXFz%2BgFAPNgR3A0nHchHCTwA9CkiHWJARof2%2FjElFy%2BcX1Jkwy%2FmWvQY6pgHOpdxPMKBLtJiA%2BpMN3mdLxr%2F%2Bs50A1tLL3AcA2X8Dy0cGHtQrBS%2FwXMGnHXECUTMybxytzi%2F3UAC%2BXqUJUBwogUKjdxw82wVduxFWNuFW74kqgHEXbXvMy2gJIev0fYRxpq6gaqcJ1RJEMQi4FsFNB18btAQOfLJ8JWtDkLLR2QdG3CYSqzGofjoPTGNaOOhZDaSgt8ecWSHJrzvVrD7woIx9Auoy&X-Amz-Signature=e137eaba33b9be7391f95b5db1fc8f4b3e3842cb3aaebdcfa2e4c15c6470eb16&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646ALOUW3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIHEnYPqmPbgYWtjrkMGiEhVkgNrZ2k%2BNbfU4eAkkHFefAiBJhfiS1HdrsF8bzHadWdg0a%2FzWExLk78ErN36gWXEJtSr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIMHs%2FrMfQls1RB0UEKKtwDyrKD6GhFkzJSKO22P0L5S9LAkx8%2BbHuoc2cGfC3iK7Bez6h3ZgjH1JCljaZlxNtjArcQYwEJVJ6l8cdiRQckG9KQob%2FowcQgW6vZ9coZVD9toJxEUHPjemnVmPEHWjHMuSj0Dxf7LCUxzxjdrAIqKsc%2BKoihh3ps7ZAnWIM7%2BtXAMWfEmwWeqKM%2FGFFTs3WQXalwrLyIqdC0njNy8PjfUPzQ2Kz5llAIdXEHEhOA9r%2BTINcAW4lbginlH4drTAPD4fPv1SvtI7ZidYuusCq4AplqNMd%2BRBg6IJVLBqPqnwVdWpXo%2B30ecTCM%2F0K0epFeOR3dt0R35uV19x9jtP86UqXxwI4sKdOsyR1Wh3pVxMsIwbAlWL8%2BB6A507V%2BRprc1yDe1lOhWVxcuyOcTchvhsS8c47Gc5KydKnEATkMmr6Fv3Lw6R44lAb9HgBEvKjKTk5Elha%2Bz%2F5R2%2FG5T7FPgHW4arqRDqzkXNJkMoWKM0FryQJpFNn%2Bxe99GVx%2Fl%2BdmE6%2FaDKCukLWB%2FmwaWYITmZL44dCQ%2Bl3LcUynYbrZSHpoI%2FpC2ErlpCeLGMs06rhmefXAA7aRVBWPXFz%2BgFAPNgR3A0nHchHCTwA9CkiHWJARof2%2FjElFy%2BcX1Jkwy%2FmWvQY6pgHOpdxPMKBLtJiA%2BpMN3mdLxr%2F%2Bs50A1tLL3AcA2X8Dy0cGHtQrBS%2FwXMGnHXECUTMybxytzi%2F3UAC%2BXqUJUBwogUKjdxw82wVduxFWNuFW74kqgHEXbXvMy2gJIev0fYRxpq6gaqcJ1RJEMQi4FsFNB18btAQOfLJ8JWtDkLLR2QdG3CYSqzGofjoPTGNaOOhZDaSgt8ecWSHJrzvVrD7woIx9Auoy&X-Amz-Signature=ea479192ee3df6656f489f36d727c228f245ba634e835bc38009d6398ec081d6&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646ALOUW3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIHEnYPqmPbgYWtjrkMGiEhVkgNrZ2k%2BNbfU4eAkkHFefAiBJhfiS1HdrsF8bzHadWdg0a%2FzWExLk78ErN36gWXEJtSr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIMHs%2FrMfQls1RB0UEKKtwDyrKD6GhFkzJSKO22P0L5S9LAkx8%2BbHuoc2cGfC3iK7Bez6h3ZgjH1JCljaZlxNtjArcQYwEJVJ6l8cdiRQckG9KQob%2FowcQgW6vZ9coZVD9toJxEUHPjemnVmPEHWjHMuSj0Dxf7LCUxzxjdrAIqKsc%2BKoihh3ps7ZAnWIM7%2BtXAMWfEmwWeqKM%2FGFFTs3WQXalwrLyIqdC0njNy8PjfUPzQ2Kz5llAIdXEHEhOA9r%2BTINcAW4lbginlH4drTAPD4fPv1SvtI7ZidYuusCq4AplqNMd%2BRBg6IJVLBqPqnwVdWpXo%2B30ecTCM%2F0K0epFeOR3dt0R35uV19x9jtP86UqXxwI4sKdOsyR1Wh3pVxMsIwbAlWL8%2BB6A507V%2BRprc1yDe1lOhWVxcuyOcTchvhsS8c47Gc5KydKnEATkMmr6Fv3Lw6R44lAb9HgBEvKjKTk5Elha%2Bz%2F5R2%2FG5T7FPgHW4arqRDqzkXNJkMoWKM0FryQJpFNn%2Bxe99GVx%2Fl%2BdmE6%2FaDKCukLWB%2FmwaWYITmZL44dCQ%2Bl3LcUynYbrZSHpoI%2FpC2ErlpCeLGMs06rhmefXAA7aRVBWPXFz%2BgFAPNgR3A0nHchHCTwA9CkiHWJARof2%2FjElFy%2BcX1Jkwy%2FmWvQY6pgHOpdxPMKBLtJiA%2BpMN3mdLxr%2F%2Bs50A1tLL3AcA2X8Dy0cGHtQrBS%2FwXMGnHXECUTMybxytzi%2F3UAC%2BXqUJUBwogUKjdxw82wVduxFWNuFW74kqgHEXbXvMy2gJIev0fYRxpq6gaqcJ1RJEMQi4FsFNB18btAQOfLJ8JWtDkLLR2QdG3CYSqzGofjoPTGNaOOhZDaSgt8ecWSHJrzvVrD7woIx9Auoy&X-Amz-Signature=e67dd08b55299beaaf0ed8472072921da9024c0d5d9a8effce28e048f4e4a0ae&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
