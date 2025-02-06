

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662SK4FREQ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJHMEUCIHtqKRGZ8XbUeE%2FDpohpgD2YqL8Ue5gNHM8PRWxg9sNjAiEAsi0cz3L8L2X4TTdIjXWgi6yjyX2%2FLWzpg%2FL5fXgLdXwq%2FwMIaBAAGgw2Mzc0MjMxODM4MDUiDD3%2BHsOiDj%2BNiVBaSCrcAx2%2FoKPiicOm%2FWX68%2FHJuw9qrcgH6BiEUUqveCqNeaPVlseGjjCkh38%2BhMixDfJnOaKz9q1B%2F2CwaPoSReowbETqBiKbek%2F8xxeze0W60pqNZm2%2FOcS5lyqwRDjezVketUpIz%2BbBChHdKjn2Bm1HVYBcPbSsYJ5lRr%2F%2FNcmodb66FSwhVcW7a%2FBN0txnzhGY3NGWI4INELhODRAKczMyVh%2B2T5B6P1jrc5r6Rra3zzqr6hBQ3%2FuX1fb%2Bji%2FWUZX%2FD8YoTL4nvdIWqu6rhV4mz7jEH3YsP2m7lIkaxFSoCHEaPNiL01b0SR5qzvhyIA32bf74XgRPxxd99%2BCwGA9T6yvhsC9Mc8alhpHd0fs24f%2BsD43uakzl6I8qO34t2KVUPteBkp0oK7qDSu99dscIpG8jSkLmP%2BB8QqyEQMBLL2QM0VRnFYAyLdMLKip%2Bh6hLq2H8wNMSMysEHAALUhfjHwlX8tXoV0p63VegIEbduvGdvDkxi3um3n%2Fs7iLHQ5hRUE67%2FBu2PqE5L7x5Z8B7KeVjFSjmumoWC8jCpTf6aHsCltsszFq2eWOXV3BqQdDx9hHkOmfuIYjc7VhB3Aa%2BNj4y6lCVrWFzNYyh7YWimZV0URLi%2BzPRNZ7HLq%2FyMKX%2BlL0GOqUB1q6IBr5f5BHYyo1isDw%2BJ7RMrxzkKyP5QUingZOnSTWYShk3chpAG1k%2BTHDh2v1o%2FcuD7Vba%2BpBbQhh51B%2FO67HEGwL5D%2BXuiT71SpS8YqkRX1nodEdb6PgH7UBjZIn2UACScYjZHr2Kt78yT3qjDR2ffFiBG2JJ9wHOR2%2FUVEzRnzXbSyZA7GC6hqUPQTl6i1ifsVwUbk20RMdXwfWdbllgN3R6&X-Amz-Signature=56b50f3a30ed1e000c3352a70c55315a7b31c82d629fe8b68559e643e3823824&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662SK4FREQ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJHMEUCIHtqKRGZ8XbUeE%2FDpohpgD2YqL8Ue5gNHM8PRWxg9sNjAiEAsi0cz3L8L2X4TTdIjXWgi6yjyX2%2FLWzpg%2FL5fXgLdXwq%2FwMIaBAAGgw2Mzc0MjMxODM4MDUiDD3%2BHsOiDj%2BNiVBaSCrcAx2%2FoKPiicOm%2FWX68%2FHJuw9qrcgH6BiEUUqveCqNeaPVlseGjjCkh38%2BhMixDfJnOaKz9q1B%2F2CwaPoSReowbETqBiKbek%2F8xxeze0W60pqNZm2%2FOcS5lyqwRDjezVketUpIz%2BbBChHdKjn2Bm1HVYBcPbSsYJ5lRr%2F%2FNcmodb66FSwhVcW7a%2FBN0txnzhGY3NGWI4INELhODRAKczMyVh%2B2T5B6P1jrc5r6Rra3zzqr6hBQ3%2FuX1fb%2Bji%2FWUZX%2FD8YoTL4nvdIWqu6rhV4mz7jEH3YsP2m7lIkaxFSoCHEaPNiL01b0SR5qzvhyIA32bf74XgRPxxd99%2BCwGA9T6yvhsC9Mc8alhpHd0fs24f%2BsD43uakzl6I8qO34t2KVUPteBkp0oK7qDSu99dscIpG8jSkLmP%2BB8QqyEQMBLL2QM0VRnFYAyLdMLKip%2Bh6hLq2H8wNMSMysEHAALUhfjHwlX8tXoV0p63VegIEbduvGdvDkxi3um3n%2Fs7iLHQ5hRUE67%2FBu2PqE5L7x5Z8B7KeVjFSjmumoWC8jCpTf6aHsCltsszFq2eWOXV3BqQdDx9hHkOmfuIYjc7VhB3Aa%2BNj4y6lCVrWFzNYyh7YWimZV0URLi%2BzPRNZ7HLq%2FyMKX%2BlL0GOqUB1q6IBr5f5BHYyo1isDw%2BJ7RMrxzkKyP5QUingZOnSTWYShk3chpAG1k%2BTHDh2v1o%2FcuD7Vba%2BpBbQhh51B%2FO67HEGwL5D%2BXuiT71SpS8YqkRX1nodEdb6PgH7UBjZIn2UACScYjZHr2Kt78yT3qjDR2ffFiBG2JJ9wHOR2%2FUVEzRnzXbSyZA7GC6hqUPQTl6i1ifsVwUbk20RMdXwfWdbllgN3R6&X-Amz-Signature=1c1f4c83c2b42cd9eaa02283666e48336196829e970b6ee7e4a1f6aac5310f6d&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662SK4FREQ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJHMEUCIHtqKRGZ8XbUeE%2FDpohpgD2YqL8Ue5gNHM8PRWxg9sNjAiEAsi0cz3L8L2X4TTdIjXWgi6yjyX2%2FLWzpg%2FL5fXgLdXwq%2FwMIaBAAGgw2Mzc0MjMxODM4MDUiDD3%2BHsOiDj%2BNiVBaSCrcAx2%2FoKPiicOm%2FWX68%2FHJuw9qrcgH6BiEUUqveCqNeaPVlseGjjCkh38%2BhMixDfJnOaKz9q1B%2F2CwaPoSReowbETqBiKbek%2F8xxeze0W60pqNZm2%2FOcS5lyqwRDjezVketUpIz%2BbBChHdKjn2Bm1HVYBcPbSsYJ5lRr%2F%2FNcmodb66FSwhVcW7a%2FBN0txnzhGY3NGWI4INELhODRAKczMyVh%2B2T5B6P1jrc5r6Rra3zzqr6hBQ3%2FuX1fb%2Bji%2FWUZX%2FD8YoTL4nvdIWqu6rhV4mz7jEH3YsP2m7lIkaxFSoCHEaPNiL01b0SR5qzvhyIA32bf74XgRPxxd99%2BCwGA9T6yvhsC9Mc8alhpHd0fs24f%2BsD43uakzl6I8qO34t2KVUPteBkp0oK7qDSu99dscIpG8jSkLmP%2BB8QqyEQMBLL2QM0VRnFYAyLdMLKip%2Bh6hLq2H8wNMSMysEHAALUhfjHwlX8tXoV0p63VegIEbduvGdvDkxi3um3n%2Fs7iLHQ5hRUE67%2FBu2PqE5L7x5Z8B7KeVjFSjmumoWC8jCpTf6aHsCltsszFq2eWOXV3BqQdDx9hHkOmfuIYjc7VhB3Aa%2BNj4y6lCVrWFzNYyh7YWimZV0URLi%2BzPRNZ7HLq%2FyMKX%2BlL0GOqUB1q6IBr5f5BHYyo1isDw%2BJ7RMrxzkKyP5QUingZOnSTWYShk3chpAG1k%2BTHDh2v1o%2FcuD7Vba%2BpBbQhh51B%2FO67HEGwL5D%2BXuiT71SpS8YqkRX1nodEdb6PgH7UBjZIn2UACScYjZHr2Kt78yT3qjDR2ffFiBG2JJ9wHOR2%2FUVEzRnzXbSyZA7GC6hqUPQTl6i1ifsVwUbk20RMdXwfWdbllgN3R6&X-Amz-Signature=88bc633c49fd81e243bea8928d3f8ef025ece38d154cd46de1e456ccc56ea6f3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SLDSKGPB%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJHMEUCIQC5ow3x4pQ%2FyFYkaLKS%2FJNjEQlDyD%2B%2Fmo5OQroov3RKbQIgBiQULx%2FcdYPSDfIT4Umr8NyyePuEf1X9C4P42lOM9u0q%2FwMIaBAAGgw2Mzc0MjMxODM4MDUiDDgxDFzpgCKBQ2NiMircA1diZxBv6E8fk%2FxajTSULMuly5%2BQI1igPUqpcAgUXfoOyRWwUvNDfv6FTYF64aqp%2B0Kx%2F0nE7dtQvJ93xtgH1ydLdvtI8O2AJWMlbdLz3b407pmy8UPIOmGDVeTPuvGr4EPffnkQkc49gKi%2FRMGpxLk4AqANmFCxgh7H1Xyv0ASnbHv%2BxOUe3DWJu6V%2FsaDIzvI1qKWnxWhiSVgZQYTh1BB4zJtDrnsh2%2FudLj29Gy64zUHv85eIYApmRaXnEbzg4HtM0Z9kbyLkSBYdqUZSQXd3LXKM14GtuV5bciLyoZ8HXlpmTs8djW2gOOxTyGPK07K8k8D2sbyamo3unE2OCxnJxM2d0gDRKPds3K%2BsROnAanW%2F67PXgQaVGRFiBB%2BuGfpfTpKLRQZ74LBhyV8j0Dl%2BKJsZCAxDB5qhFOfzHus95XWimHXFGNeLxH6rm2trEY%2FStNs2c3KHFecPCounnQ7dMR8fN8o3kuww1Sh0U14%2BBZey8Q12pcTzeYQ5WCA9mEoPymUg26%2ByDlnY%2BZBRglFN2B7U05iYGcC1fJfJp16Xc8IR7QLfKSFtFSFfwN3NgbUHemwVMhqEbpk56eLbmVXtmbLj0aUuLqoe0emH8dtsSoqa7xU3JCurOqyuMMb9lL0GOqUBAWpvn1vvojUQ0iYi27E0gDkRin0CKnzo6uoRt5FAjNeIGtUyu9pg4ek0YhnvO4%2BgXfRE8s%2B%2FcKDiUvLyX%2FjSs3jV9KyJEx%2FnGG4Q%2FtHT79F3L%2F%2Bx93EXqtX7fVmzznmmBhhYBxtPpjccUBneVTPjHRUFLRDrEOMYTB4KspHFPCr95mqc7EmuD7JeSjJhDH6zc3GQMl5xZdo9F2a3FfooGiK%2Ff54O&X-Amz-Signature=8ca8256a34341618c76df3c4f310e504ffa746ac57e474f0fbfdbef55543f9d4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662B4MDIAJ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJHMEUCIQDdPkMcOH1cYiRbrbqlCZW2EgB16ulVBPgcfgPGXwE%2FCAIgCkd6RlGo8wBFC6RVV1u25Wnk0lfmRXCLtkMgjMtngnYq%2FwMIaBAAGgw2Mzc0MjMxODM4MDUiDJeGARq7id2rP3ibHSrcA2l3iRQHk9JOyvKLoVoqyD2Qam8ex29UZ7VoGbiAftYM%2FpWY%2B8Bf5RBT8at%2FzH%2F9nIBZHDLfEAE2pUOa35iKxMuS%2B3rm4rZKefKfXDg0hKLgXKND5tVEnu9d3CiUAf6l324ZwcM67PXl2YSyOOQyQdlfL%2BnY7%2BNdRTkD1a%2B0eEMbX92cY4GT4pA5vq%2BaaO4UaCG8EEarJY1b6MNcqphERLnwoVIQULZiCZhgPtUZMkrUeZMNngO%2B7%2Fs%2F9vsQ0K38oDGhPh5xy8YTabClW3jNOj8XuiIklfct8CUy6SuR8ZTgBY2DjQWtWsBmk62Vqj8YGvl0ZsLSSm2ipelH4pRtIwBwj4m3iBm%2BMZQpxRtnRdiWGuIpmm%2BsJjk2u5yIrB8imuvfjdMDm75%2FvJg60tDJ8WRo6%2BPKpjs3yfc9N0aE7Iak%2FasO%2BexA4o3WzBT9pRhh2ZVLJsex614qpubUTRpzFxptFuCkfIyh5A0OPnPrLwlRNOvH35Zw3LC6N6MnlImRN%2FQ0xQVs6UhNBgvacceoftoTuk9dQSe0uBzbmvdUIUTaiaG56ohkfOYXbiACJlDKgJmgsgP1xwLOVd%2BYF9YQC9RQVGLIpz1u%2FRbpQT%2FhpL1BTFDAjKZr2lDXnISoMMX9lL0GOqUBlROlG%2B011EqhM%2FreBg0nMxf9om5eAjPw5dCS3TY98fgwvy5dp2TaI0sKI%2Fvln%2FGNjF9EjqIu9In33nR5gJwvlVrL4gDseBiFzM4FKKN0%2Bkfm%2BBHyCq5r2%2B5U4twhfRwJiRkbe%2FAUG9wUAl2AyeMbRdr0ZwpyqP5hjdeft6vh8aO4TYQvVy2yU0Btzs2dN193Hv%2FAo0TLGtnzS894Cm%2BIcy16Eixc&X-Amz-Signature=b003d98875c649bc5c6bf90e0cefaca93cb5903971c3cdbe236941ccc974dceb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662SK4FREQ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJHMEUCIHtqKRGZ8XbUeE%2FDpohpgD2YqL8Ue5gNHM8PRWxg9sNjAiEAsi0cz3L8L2X4TTdIjXWgi6yjyX2%2FLWzpg%2FL5fXgLdXwq%2FwMIaBAAGgw2Mzc0MjMxODM4MDUiDD3%2BHsOiDj%2BNiVBaSCrcAx2%2FoKPiicOm%2FWX68%2FHJuw9qrcgH6BiEUUqveCqNeaPVlseGjjCkh38%2BhMixDfJnOaKz9q1B%2F2CwaPoSReowbETqBiKbek%2F8xxeze0W60pqNZm2%2FOcS5lyqwRDjezVketUpIz%2BbBChHdKjn2Bm1HVYBcPbSsYJ5lRr%2F%2FNcmodb66FSwhVcW7a%2FBN0txnzhGY3NGWI4INELhODRAKczMyVh%2B2T5B6P1jrc5r6Rra3zzqr6hBQ3%2FuX1fb%2Bji%2FWUZX%2FD8YoTL4nvdIWqu6rhV4mz7jEH3YsP2m7lIkaxFSoCHEaPNiL01b0SR5qzvhyIA32bf74XgRPxxd99%2BCwGA9T6yvhsC9Mc8alhpHd0fs24f%2BsD43uakzl6I8qO34t2KVUPteBkp0oK7qDSu99dscIpG8jSkLmP%2BB8QqyEQMBLL2QM0VRnFYAyLdMLKip%2Bh6hLq2H8wNMSMysEHAALUhfjHwlX8tXoV0p63VegIEbduvGdvDkxi3um3n%2Fs7iLHQ5hRUE67%2FBu2PqE5L7x5Z8B7KeVjFSjmumoWC8jCpTf6aHsCltsszFq2eWOXV3BqQdDx9hHkOmfuIYjc7VhB3Aa%2BNj4y6lCVrWFzNYyh7YWimZV0URLi%2BzPRNZ7HLq%2FyMKX%2BlL0GOqUB1q6IBr5f5BHYyo1isDw%2BJ7RMrxzkKyP5QUingZOnSTWYShk3chpAG1k%2BTHDh2v1o%2FcuD7Vba%2BpBbQhh51B%2FO67HEGwL5D%2BXuiT71SpS8YqkRX1nodEdb6PgH7UBjZIn2UACScYjZHr2Kt78yT3qjDR2ffFiBG2JJ9wHOR2%2FUVEzRnzXbSyZA7GC6hqUPQTl6i1ifsVwUbk20RMdXwfWdbllgN3R6&X-Amz-Signature=a7a792c2416e3a38a8d112a8c0b2dda27d531535758bbae2db7be0b5076536d9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662SK4FREQ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJHMEUCIHtqKRGZ8XbUeE%2FDpohpgD2YqL8Ue5gNHM8PRWxg9sNjAiEAsi0cz3L8L2X4TTdIjXWgi6yjyX2%2FLWzpg%2FL5fXgLdXwq%2FwMIaBAAGgw2Mzc0MjMxODM4MDUiDD3%2BHsOiDj%2BNiVBaSCrcAx2%2FoKPiicOm%2FWX68%2FHJuw9qrcgH6BiEUUqveCqNeaPVlseGjjCkh38%2BhMixDfJnOaKz9q1B%2F2CwaPoSReowbETqBiKbek%2F8xxeze0W60pqNZm2%2FOcS5lyqwRDjezVketUpIz%2BbBChHdKjn2Bm1HVYBcPbSsYJ5lRr%2F%2FNcmodb66FSwhVcW7a%2FBN0txnzhGY3NGWI4INELhODRAKczMyVh%2B2T5B6P1jrc5r6Rra3zzqr6hBQ3%2FuX1fb%2Bji%2FWUZX%2FD8YoTL4nvdIWqu6rhV4mz7jEH3YsP2m7lIkaxFSoCHEaPNiL01b0SR5qzvhyIA32bf74XgRPxxd99%2BCwGA9T6yvhsC9Mc8alhpHd0fs24f%2BsD43uakzl6I8qO34t2KVUPteBkp0oK7qDSu99dscIpG8jSkLmP%2BB8QqyEQMBLL2QM0VRnFYAyLdMLKip%2Bh6hLq2H8wNMSMysEHAALUhfjHwlX8tXoV0p63VegIEbduvGdvDkxi3um3n%2Fs7iLHQ5hRUE67%2FBu2PqE5L7x5Z8B7KeVjFSjmumoWC8jCpTf6aHsCltsszFq2eWOXV3BqQdDx9hHkOmfuIYjc7VhB3Aa%2BNj4y6lCVrWFzNYyh7YWimZV0URLi%2BzPRNZ7HLq%2FyMKX%2BlL0GOqUB1q6IBr5f5BHYyo1isDw%2BJ7RMrxzkKyP5QUingZOnSTWYShk3chpAG1k%2BTHDh2v1o%2FcuD7Vba%2BpBbQhh51B%2FO67HEGwL5D%2BXuiT71SpS8YqkRX1nodEdb6PgH7UBjZIn2UACScYjZHr2Kt78yT3qjDR2ffFiBG2JJ9wHOR2%2FUVEzRnzXbSyZA7GC6hqUPQTl6i1ifsVwUbk20RMdXwfWdbllgN3R6&X-Amz-Signature=4147e5a9d6cef4c0c3ac6c83e885906344dc4ce657be71384e4c93a65c7a6bd8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662SK4FREQ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJHMEUCIHtqKRGZ8XbUeE%2FDpohpgD2YqL8Ue5gNHM8PRWxg9sNjAiEAsi0cz3L8L2X4TTdIjXWgi6yjyX2%2FLWzpg%2FL5fXgLdXwq%2FwMIaBAAGgw2Mzc0MjMxODM4MDUiDD3%2BHsOiDj%2BNiVBaSCrcAx2%2FoKPiicOm%2FWX68%2FHJuw9qrcgH6BiEUUqveCqNeaPVlseGjjCkh38%2BhMixDfJnOaKz9q1B%2F2CwaPoSReowbETqBiKbek%2F8xxeze0W60pqNZm2%2FOcS5lyqwRDjezVketUpIz%2BbBChHdKjn2Bm1HVYBcPbSsYJ5lRr%2F%2FNcmodb66FSwhVcW7a%2FBN0txnzhGY3NGWI4INELhODRAKczMyVh%2B2T5B6P1jrc5r6Rra3zzqr6hBQ3%2FuX1fb%2Bji%2FWUZX%2FD8YoTL4nvdIWqu6rhV4mz7jEH3YsP2m7lIkaxFSoCHEaPNiL01b0SR5qzvhyIA32bf74XgRPxxd99%2BCwGA9T6yvhsC9Mc8alhpHd0fs24f%2BsD43uakzl6I8qO34t2KVUPteBkp0oK7qDSu99dscIpG8jSkLmP%2BB8QqyEQMBLL2QM0VRnFYAyLdMLKip%2Bh6hLq2H8wNMSMysEHAALUhfjHwlX8tXoV0p63VegIEbduvGdvDkxi3um3n%2Fs7iLHQ5hRUE67%2FBu2PqE5L7x5Z8B7KeVjFSjmumoWC8jCpTf6aHsCltsszFq2eWOXV3BqQdDx9hHkOmfuIYjc7VhB3Aa%2BNj4y6lCVrWFzNYyh7YWimZV0URLi%2BzPRNZ7HLq%2FyMKX%2BlL0GOqUB1q6IBr5f5BHYyo1isDw%2BJ7RMrxzkKyP5QUingZOnSTWYShk3chpAG1k%2BTHDh2v1o%2FcuD7Vba%2BpBbQhh51B%2FO67HEGwL5D%2BXuiT71SpS8YqkRX1nodEdb6PgH7UBjZIn2UACScYjZHr2Kt78yT3qjDR2ffFiBG2JJ9wHOR2%2FUVEzRnzXbSyZA7GC6hqUPQTl6i1ifsVwUbk20RMdXwfWdbllgN3R6&X-Amz-Signature=5a3d672c7f497338d12d76dfec9d3b5ce5da3c5cb7a39673d369dbb7c141511a&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662SK4FREQ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJHMEUCIHtqKRGZ8XbUeE%2FDpohpgD2YqL8Ue5gNHM8PRWxg9sNjAiEAsi0cz3L8L2X4TTdIjXWgi6yjyX2%2FLWzpg%2FL5fXgLdXwq%2FwMIaBAAGgw2Mzc0MjMxODM4MDUiDD3%2BHsOiDj%2BNiVBaSCrcAx2%2FoKPiicOm%2FWX68%2FHJuw9qrcgH6BiEUUqveCqNeaPVlseGjjCkh38%2BhMixDfJnOaKz9q1B%2F2CwaPoSReowbETqBiKbek%2F8xxeze0W60pqNZm2%2FOcS5lyqwRDjezVketUpIz%2BbBChHdKjn2Bm1HVYBcPbSsYJ5lRr%2F%2FNcmodb66FSwhVcW7a%2FBN0txnzhGY3NGWI4INELhODRAKczMyVh%2B2T5B6P1jrc5r6Rra3zzqr6hBQ3%2FuX1fb%2Bji%2FWUZX%2FD8YoTL4nvdIWqu6rhV4mz7jEH3YsP2m7lIkaxFSoCHEaPNiL01b0SR5qzvhyIA32bf74XgRPxxd99%2BCwGA9T6yvhsC9Mc8alhpHd0fs24f%2BsD43uakzl6I8qO34t2KVUPteBkp0oK7qDSu99dscIpG8jSkLmP%2BB8QqyEQMBLL2QM0VRnFYAyLdMLKip%2Bh6hLq2H8wNMSMysEHAALUhfjHwlX8tXoV0p63VegIEbduvGdvDkxi3um3n%2Fs7iLHQ5hRUE67%2FBu2PqE5L7x5Z8B7KeVjFSjmumoWC8jCpTf6aHsCltsszFq2eWOXV3BqQdDx9hHkOmfuIYjc7VhB3Aa%2BNj4y6lCVrWFzNYyh7YWimZV0URLi%2BzPRNZ7HLq%2FyMKX%2BlL0GOqUB1q6IBr5f5BHYyo1isDw%2BJ7RMrxzkKyP5QUingZOnSTWYShk3chpAG1k%2BTHDh2v1o%2FcuD7Vba%2BpBbQhh51B%2FO67HEGwL5D%2BXuiT71SpS8YqkRX1nodEdb6PgH7UBjZIn2UACScYjZHr2Kt78yT3qjDR2ffFiBG2JJ9wHOR2%2FUVEzRnzXbSyZA7GC6hqUPQTl6i1ifsVwUbk20RMdXwfWdbllgN3R6&X-Amz-Signature=9ea8c91617d0f6c0bf5caba542b2b3dbfa0e0361c3d39f71bc058d9995153503&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
