

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWTYLKXF%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF8quyhmeBkToVih5Npl1kfOpfL43G%2Fp184CN0orKwNdAiA7Klk4cL8hFwyTLaZtfjeSoRIymLfVrJNtcWIra0faBSqIBAjD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMK6XgEHLkIX9g7IlRKtwD6uCRGoIXCsSjTPIGxXmJbFh%2FYhCMkTmNG7%2BeQ3FsA8aoyqQTLYiao2ozPIsiZ2DRp8QZzBKADRRpugE%2BazwAZZjRvhVuSuC9SqVQ5pybmll9KRVY6ffKddAVK855UYAaZpjrIPlumX3gB9R3vztw8XPeJy4YCd3EkqKsDvM0lYgnQ5M5Hq%2FZkMCYeG1TaHbu7HX0JaxqJ8%2BGXtGKoqrLFN956OM18OnBIFf4epn6h%2BQ807nD0fHH4Zks9%2Fs91mJczi7ipYWzPa3O1QfmtenYm13VHz%2FmvpI4F7Ed6eOaqy6ItqsHHzxScHH2t3vKCSYUPi4JepFgZKS%2BknYpxl7eRTdH6zAtGTZFsuqdEwz1bdV7QliEkplUt4Gd1Castk84BswWxApaxThXWJqdB2Vs8P3uiP41H16g0cuF987qneasJeYlqkvPBg8qTBADt8mpuZqkMj%2BBCd4iAXSzMy8W%2BiAYRNvkOJA2mSgWlyvn3ojMKXqqQfTOXYBjLIvWpjTJTTq7q%2Flz3nGipKo9UUQyfquYO1ChsdsBUyeRmKrtXHxdS9di3I1ID1Vce1B9%2BfUjP1bZ2mQOspYisToRKKmqkddfBoDPwFqlvpBSi%2BNDWPXWfQcFJhn7N8qyN7Uw8aP0vAY6pgGRsM06U5tM5RbIa6lvQFquL8D9D10KnXHVzwUpPxZK2RJJV%2BdQWB6DlfjAFr0OBVSx%2FtZdaPrvhtOBFmNpp2j4tLNSW9Li291VHayjO4IPs5U1SqZnV0dkNHcj87Do4lZpzN1skhcqUHw4NL7Do5yI9Gf7OW5zdUwvjtL0slgyX%2FR9Flf%2FppQmBxxH8w7mrIeMPtbdFttxgnUxOLFLJRwgSIWEyaYZ&X-Amz-Signature=03dd660075c6605f096afc56d65ad39b49c621109aa555ef322b5ba78397872e&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWTYLKXF%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF8quyhmeBkToVih5Npl1kfOpfL43G%2Fp184CN0orKwNdAiA7Klk4cL8hFwyTLaZtfjeSoRIymLfVrJNtcWIra0faBSqIBAjD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMK6XgEHLkIX9g7IlRKtwD6uCRGoIXCsSjTPIGxXmJbFh%2FYhCMkTmNG7%2BeQ3FsA8aoyqQTLYiao2ozPIsiZ2DRp8QZzBKADRRpugE%2BazwAZZjRvhVuSuC9SqVQ5pybmll9KRVY6ffKddAVK855UYAaZpjrIPlumX3gB9R3vztw8XPeJy4YCd3EkqKsDvM0lYgnQ5M5Hq%2FZkMCYeG1TaHbu7HX0JaxqJ8%2BGXtGKoqrLFN956OM18OnBIFf4epn6h%2BQ807nD0fHH4Zks9%2Fs91mJczi7ipYWzPa3O1QfmtenYm13VHz%2FmvpI4F7Ed6eOaqy6ItqsHHzxScHH2t3vKCSYUPi4JepFgZKS%2BknYpxl7eRTdH6zAtGTZFsuqdEwz1bdV7QliEkplUt4Gd1Castk84BswWxApaxThXWJqdB2Vs8P3uiP41H16g0cuF987qneasJeYlqkvPBg8qTBADt8mpuZqkMj%2BBCd4iAXSzMy8W%2BiAYRNvkOJA2mSgWlyvn3ojMKXqqQfTOXYBjLIvWpjTJTTq7q%2Flz3nGipKo9UUQyfquYO1ChsdsBUyeRmKrtXHxdS9di3I1ID1Vce1B9%2BfUjP1bZ2mQOspYisToRKKmqkddfBoDPwFqlvpBSi%2BNDWPXWfQcFJhn7N8qyN7Uw8aP0vAY6pgGRsM06U5tM5RbIa6lvQFquL8D9D10KnXHVzwUpPxZK2RJJV%2BdQWB6DlfjAFr0OBVSx%2FtZdaPrvhtOBFmNpp2j4tLNSW9Li291VHayjO4IPs5U1SqZnV0dkNHcj87Do4lZpzN1skhcqUHw4NL7Do5yI9Gf7OW5zdUwvjtL0slgyX%2FR9Flf%2FppQmBxxH8w7mrIeMPtbdFttxgnUxOLFLJRwgSIWEyaYZ&X-Amz-Signature=0b7af0442aa1382fab05aeac27790b289fdb2e78176495be132e168250d89a42&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWTYLKXF%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF8quyhmeBkToVih5Npl1kfOpfL43G%2Fp184CN0orKwNdAiA7Klk4cL8hFwyTLaZtfjeSoRIymLfVrJNtcWIra0faBSqIBAjD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMK6XgEHLkIX9g7IlRKtwD6uCRGoIXCsSjTPIGxXmJbFh%2FYhCMkTmNG7%2BeQ3FsA8aoyqQTLYiao2ozPIsiZ2DRp8QZzBKADRRpugE%2BazwAZZjRvhVuSuC9SqVQ5pybmll9KRVY6ffKddAVK855UYAaZpjrIPlumX3gB9R3vztw8XPeJy4YCd3EkqKsDvM0lYgnQ5M5Hq%2FZkMCYeG1TaHbu7HX0JaxqJ8%2BGXtGKoqrLFN956OM18OnBIFf4epn6h%2BQ807nD0fHH4Zks9%2Fs91mJczi7ipYWzPa3O1QfmtenYm13VHz%2FmvpI4F7Ed6eOaqy6ItqsHHzxScHH2t3vKCSYUPi4JepFgZKS%2BknYpxl7eRTdH6zAtGTZFsuqdEwz1bdV7QliEkplUt4Gd1Castk84BswWxApaxThXWJqdB2Vs8P3uiP41H16g0cuF987qneasJeYlqkvPBg8qTBADt8mpuZqkMj%2BBCd4iAXSzMy8W%2BiAYRNvkOJA2mSgWlyvn3ojMKXqqQfTOXYBjLIvWpjTJTTq7q%2Flz3nGipKo9UUQyfquYO1ChsdsBUyeRmKrtXHxdS9di3I1ID1Vce1B9%2BfUjP1bZ2mQOspYisToRKKmqkddfBoDPwFqlvpBSi%2BNDWPXWfQcFJhn7N8qyN7Uw8aP0vAY6pgGRsM06U5tM5RbIa6lvQFquL8D9D10KnXHVzwUpPxZK2RJJV%2BdQWB6DlfjAFr0OBVSx%2FtZdaPrvhtOBFmNpp2j4tLNSW9Li291VHayjO4IPs5U1SqZnV0dkNHcj87Do4lZpzN1skhcqUHw4NL7Do5yI9Gf7OW5zdUwvjtL0slgyX%2FR9Flf%2FppQmBxxH8w7mrIeMPtbdFttxgnUxOLFLJRwgSIWEyaYZ&X-Amz-Signature=8567e8394188a6449e7b44cfd4aee9fddebb9fbc4b7d0e6b9df93d92df2b6882&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XWJGXMSR%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICDqBCvdxZu8hB%2BlNkgvPh9PG33Cd1PjYR3O5n3VASzRAiBhCcyTrE0hVdq6MMA9NScj7gN0WGkRBF5ngoxf%2FKM5fiqIBAjD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMn2p4ySuvydjGsSpYKtwD7AnTVmpfu7PAziwA4EQ3phHcOoK%2BdWK%2B865RJjPhnvlCp%2BS5CFdwOUD342Gkc%2BlebX%2BqPmbL3yduOyNHx7AAU5%2FidGcxMuSiFjVm6fRuZdmofkD3DojYqeslGlUC6SOnV85eYfb5n7SVd8H%2FHy8T59Glv%2BC97tkW7XbdeGxtkVdXsPJj%2FLHgBNEcxdtkas3kuIeMdu8NoyAXdFn2NFk43CDqfeI9ypnIrFgyiJ%2Bmbt7CFRB%2FhWYH%2BmXTr8F15pVFjUUQ6wSlIUnQkHiQLfgHihCwIqPBifAmnullDGrPQzRk5PHOfcEl0ijmDKL4Ag9UHn%2BVSLegyEBI5ffPOnkqGkUh%2B9X7eU4IyvKVG9ei4KM9ABsfLCsJINPLAsKAlk8IbSO2Ov%2FD%2BgNnMceumrfjZXrc89%2FOQGEhrgtrq8VgzzweGRaYpv%2Fhy1vzVO9xrmOZMHudkjDYiQ2NrTBmIuUTxvKeTwYHXM7OvfIIUo4rkXbWfYx5ZD8uPW9Mdr0jGFOpk89STJM%2FEJ2klr3EyYIcGoN4QcHHB4t%2FidFwWVLTMjnUtOgxmoC%2BGsoAdwlShq9aLEh8uT2aTtSoh36QwHJp193uMnxSuCQUepiZk8AL7ovpKbC%2FtcVHyJRxp8gwkqT0vAY6pgHne3QO1AuA3Zhhxv29jxBZGUu0BFH5kHtzHx1DQ2N0i5iLoet5my2Bez2htMEbMwpuTMmXd79I%2FJXsVj7qglvWhrVDB11RWmprZH4U%2Btdq6iM5QrL6G9Zc0pL%2FtcUtt9qTqm8oUug12%2F8kPHSLbt1RaGb9qfhSiH%2BvdQC3BkUN27hPXt7QN%2FNAHYozOcHJ%2F%2BYwEepdeuQomk0yT2x2%2FAZqPKF4aIXg&X-Amz-Signature=f860aa1e5d02cbdf42362b7bd7650791312be3de08be4c4aacf512d888152a7d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YOCNEIXD%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAgOAH52dTCdoD9SOmNyhtk93wukPyqbKBh9P86rTL98AiBX2qXWzpubBgUyVW%2FpPDP3fGX0XIrB9kzZUN8V6BDC7SqIBAjD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMyBocwZKFi3f6TRXzKtwDrYM%2FNFR9bYztHydMqGhxnc3Gv0BKEB8oDtIN2dUbKYQeUlwmCmYKYobcpDk%2FSJ%2Fhmhlxqpb4zxRsIptRP4u1PhmIUT8DYsf39aWMaalrqlsrkJmaGc6rG5%2BwIRDuXGOENJceBi%2B0DcARP7UP0WbLHDC9tWzraIsh3VC7zq21MKIHguQJY82qVA4lww6O%2FTdQSsajPNyJUEZOK%2FBC3d%2B2c7ICRYkB355HbuTUCZeqtNtojZp4Ef8t8pye8S1I%2FAoKYgNUsvSzN5416B%2BtnhBTG63rJrpKwAOMShEND2ZjgdGNwpzvKpDRSs4SOggxtKExWrE0h7d12UVeBP6xwk%2FVlM%2FN%2FpXYivMkcKJ17Ddx2HzErUJoaDFKhZWmVToA7TuZMILW4dHauX8NxLyvJ7BHmNNJRKYAErgpDWcH7DJnyR19evV2mLdOqfwDaBypp3x5EHgVRqC8FSVbEqTpE1kM5MvrV%2FYG%2BEeuBeBFDIhjQ47OpZRrc0bdUi2vSATgnIIWdV%2BElzsMXUO5zOrFiDBah%2BgU8g9JKcuFyY5yx8O%2BPJBOrIlV9tuf76%2FxeCok8MlVyv3S40jX271PArsBsa%2FNa1yW4XpAsOM6esnd2KBg0TVfL2HaOpq%2BBfrfF4MwhaT0vAY6pgHLl4J7tSUfKelGoWk70ovChzgxt3SVYuqaC4RkXdKJPE0JrQC6papq%2FxkXN2ym%2FSnheZpVMf9bc6vi0XFe%2BNfLNgv4WYT97JtQ6XTSLYPVD6N3GVHdJPtgyxku2aWgwEsYQdV%2B9fzuRzU9ER9WZNI7nQcs7zU2kU2ktXc2%2F%2FSkt%2B35bZ7yTkJyyy5sYyzOFEIyhCnW44mRV70GdHCHP48i3%2B2nmDtU&X-Amz-Signature=c95a2cbaa709634cba2fdbbcd87eb897528e7980ea71f7fde350d14d29d1d88d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWTYLKXF%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF8quyhmeBkToVih5Npl1kfOpfL43G%2Fp184CN0orKwNdAiA7Klk4cL8hFwyTLaZtfjeSoRIymLfVrJNtcWIra0faBSqIBAjD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMK6XgEHLkIX9g7IlRKtwD6uCRGoIXCsSjTPIGxXmJbFh%2FYhCMkTmNG7%2BeQ3FsA8aoyqQTLYiao2ozPIsiZ2DRp8QZzBKADRRpugE%2BazwAZZjRvhVuSuC9SqVQ5pybmll9KRVY6ffKddAVK855UYAaZpjrIPlumX3gB9R3vztw8XPeJy4YCd3EkqKsDvM0lYgnQ5M5Hq%2FZkMCYeG1TaHbu7HX0JaxqJ8%2BGXtGKoqrLFN956OM18OnBIFf4epn6h%2BQ807nD0fHH4Zks9%2Fs91mJczi7ipYWzPa3O1QfmtenYm13VHz%2FmvpI4F7Ed6eOaqy6ItqsHHzxScHH2t3vKCSYUPi4JepFgZKS%2BknYpxl7eRTdH6zAtGTZFsuqdEwz1bdV7QliEkplUt4Gd1Castk84BswWxApaxThXWJqdB2Vs8P3uiP41H16g0cuF987qneasJeYlqkvPBg8qTBADt8mpuZqkMj%2BBCd4iAXSzMy8W%2BiAYRNvkOJA2mSgWlyvn3ojMKXqqQfTOXYBjLIvWpjTJTTq7q%2Flz3nGipKo9UUQyfquYO1ChsdsBUyeRmKrtXHxdS9di3I1ID1Vce1B9%2BfUjP1bZ2mQOspYisToRKKmqkddfBoDPwFqlvpBSi%2BNDWPXWfQcFJhn7N8qyN7Uw8aP0vAY6pgGRsM06U5tM5RbIa6lvQFquL8D9D10KnXHVzwUpPxZK2RJJV%2BdQWB6DlfjAFr0OBVSx%2FtZdaPrvhtOBFmNpp2j4tLNSW9Li291VHayjO4IPs5U1SqZnV0dkNHcj87Do4lZpzN1skhcqUHw4NL7Do5yI9Gf7OW5zdUwvjtL0slgyX%2FR9Flf%2FppQmBxxH8w7mrIeMPtbdFttxgnUxOLFLJRwgSIWEyaYZ&X-Amz-Signature=c1f3ee98ec4dc453c3d4a59bf78cffc0a18220f980a63b7ebe11366ebd18c6ec&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWTYLKXF%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF8quyhmeBkToVih5Npl1kfOpfL43G%2Fp184CN0orKwNdAiA7Klk4cL8hFwyTLaZtfjeSoRIymLfVrJNtcWIra0faBSqIBAjD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMK6XgEHLkIX9g7IlRKtwD6uCRGoIXCsSjTPIGxXmJbFh%2FYhCMkTmNG7%2BeQ3FsA8aoyqQTLYiao2ozPIsiZ2DRp8QZzBKADRRpugE%2BazwAZZjRvhVuSuC9SqVQ5pybmll9KRVY6ffKddAVK855UYAaZpjrIPlumX3gB9R3vztw8XPeJy4YCd3EkqKsDvM0lYgnQ5M5Hq%2FZkMCYeG1TaHbu7HX0JaxqJ8%2BGXtGKoqrLFN956OM18OnBIFf4epn6h%2BQ807nD0fHH4Zks9%2Fs91mJczi7ipYWzPa3O1QfmtenYm13VHz%2FmvpI4F7Ed6eOaqy6ItqsHHzxScHH2t3vKCSYUPi4JepFgZKS%2BknYpxl7eRTdH6zAtGTZFsuqdEwz1bdV7QliEkplUt4Gd1Castk84BswWxApaxThXWJqdB2Vs8P3uiP41H16g0cuF987qneasJeYlqkvPBg8qTBADt8mpuZqkMj%2BBCd4iAXSzMy8W%2BiAYRNvkOJA2mSgWlyvn3ojMKXqqQfTOXYBjLIvWpjTJTTq7q%2Flz3nGipKo9UUQyfquYO1ChsdsBUyeRmKrtXHxdS9di3I1ID1Vce1B9%2BfUjP1bZ2mQOspYisToRKKmqkddfBoDPwFqlvpBSi%2BNDWPXWfQcFJhn7N8qyN7Uw8aP0vAY6pgGRsM06U5tM5RbIa6lvQFquL8D9D10KnXHVzwUpPxZK2RJJV%2BdQWB6DlfjAFr0OBVSx%2FtZdaPrvhtOBFmNpp2j4tLNSW9Li291VHayjO4IPs5U1SqZnV0dkNHcj87Do4lZpzN1skhcqUHw4NL7Do5yI9Gf7OW5zdUwvjtL0slgyX%2FR9Flf%2FppQmBxxH8w7mrIeMPtbdFttxgnUxOLFLJRwgSIWEyaYZ&X-Amz-Signature=3fbc24fa23344fec205721aa2e9d42dad29bcd0c0cfbb40e1541d63c28b7f4cb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWTYLKXF%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF8quyhmeBkToVih5Npl1kfOpfL43G%2Fp184CN0orKwNdAiA7Klk4cL8hFwyTLaZtfjeSoRIymLfVrJNtcWIra0faBSqIBAjD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMK6XgEHLkIX9g7IlRKtwD6uCRGoIXCsSjTPIGxXmJbFh%2FYhCMkTmNG7%2BeQ3FsA8aoyqQTLYiao2ozPIsiZ2DRp8QZzBKADRRpugE%2BazwAZZjRvhVuSuC9SqVQ5pybmll9KRVY6ffKddAVK855UYAaZpjrIPlumX3gB9R3vztw8XPeJy4YCd3EkqKsDvM0lYgnQ5M5Hq%2FZkMCYeG1TaHbu7HX0JaxqJ8%2BGXtGKoqrLFN956OM18OnBIFf4epn6h%2BQ807nD0fHH4Zks9%2Fs91mJczi7ipYWzPa3O1QfmtenYm13VHz%2FmvpI4F7Ed6eOaqy6ItqsHHzxScHH2t3vKCSYUPi4JepFgZKS%2BknYpxl7eRTdH6zAtGTZFsuqdEwz1bdV7QliEkplUt4Gd1Castk84BswWxApaxThXWJqdB2Vs8P3uiP41H16g0cuF987qneasJeYlqkvPBg8qTBADt8mpuZqkMj%2BBCd4iAXSzMy8W%2BiAYRNvkOJA2mSgWlyvn3ojMKXqqQfTOXYBjLIvWpjTJTTq7q%2Flz3nGipKo9UUQyfquYO1ChsdsBUyeRmKrtXHxdS9di3I1ID1Vce1B9%2BfUjP1bZ2mQOspYisToRKKmqkddfBoDPwFqlvpBSi%2BNDWPXWfQcFJhn7N8qyN7Uw8aP0vAY6pgGRsM06U5tM5RbIa6lvQFquL8D9D10KnXHVzwUpPxZK2RJJV%2BdQWB6DlfjAFr0OBVSx%2FtZdaPrvhtOBFmNpp2j4tLNSW9Li291VHayjO4IPs5U1SqZnV0dkNHcj87Do4lZpzN1skhcqUHw4NL7Do5yI9Gf7OW5zdUwvjtL0slgyX%2FR9Flf%2FppQmBxxH8w7mrIeMPtbdFttxgnUxOLFLJRwgSIWEyaYZ&X-Amz-Signature=57091186df110f6f4319fe4684ea05f8568b72f6e8651b3e5306bc0965447991&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWTYLKXF%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF8quyhmeBkToVih5Npl1kfOpfL43G%2Fp184CN0orKwNdAiA7Klk4cL8hFwyTLaZtfjeSoRIymLfVrJNtcWIra0faBSqIBAjD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMK6XgEHLkIX9g7IlRKtwD6uCRGoIXCsSjTPIGxXmJbFh%2FYhCMkTmNG7%2BeQ3FsA8aoyqQTLYiao2ozPIsiZ2DRp8QZzBKADRRpugE%2BazwAZZjRvhVuSuC9SqVQ5pybmll9KRVY6ffKddAVK855UYAaZpjrIPlumX3gB9R3vztw8XPeJy4YCd3EkqKsDvM0lYgnQ5M5Hq%2FZkMCYeG1TaHbu7HX0JaxqJ8%2BGXtGKoqrLFN956OM18OnBIFf4epn6h%2BQ807nD0fHH4Zks9%2Fs91mJczi7ipYWzPa3O1QfmtenYm13VHz%2FmvpI4F7Ed6eOaqy6ItqsHHzxScHH2t3vKCSYUPi4JepFgZKS%2BknYpxl7eRTdH6zAtGTZFsuqdEwz1bdV7QliEkplUt4Gd1Castk84BswWxApaxThXWJqdB2Vs8P3uiP41H16g0cuF987qneasJeYlqkvPBg8qTBADt8mpuZqkMj%2BBCd4iAXSzMy8W%2BiAYRNvkOJA2mSgWlyvn3ojMKXqqQfTOXYBjLIvWpjTJTTq7q%2Flz3nGipKo9UUQyfquYO1ChsdsBUyeRmKrtXHxdS9di3I1ID1Vce1B9%2BfUjP1bZ2mQOspYisToRKKmqkddfBoDPwFqlvpBSi%2BNDWPXWfQcFJhn7N8qyN7Uw8aP0vAY6pgGRsM06U5tM5RbIa6lvQFquL8D9D10KnXHVzwUpPxZK2RJJV%2BdQWB6DlfjAFr0OBVSx%2FtZdaPrvhtOBFmNpp2j4tLNSW9Li291VHayjO4IPs5U1SqZnV0dkNHcj87Do4lZpzN1skhcqUHw4NL7Do5yI9Gf7OW5zdUwvjtL0slgyX%2FR9Flf%2FppQmBxxH8w7mrIeMPtbdFttxgnUxOLFLJRwgSIWEyaYZ&X-Amz-Signature=dbce84c28ec5c734d944d7fe92c62410412cc489dd11762786c115c8b6d1474a&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
