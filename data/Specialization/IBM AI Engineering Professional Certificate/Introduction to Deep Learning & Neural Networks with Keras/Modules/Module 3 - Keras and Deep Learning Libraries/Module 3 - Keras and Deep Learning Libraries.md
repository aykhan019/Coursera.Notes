

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WOS5SKS%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJGMEQCIDlln%2BIkagJDpSLUrnIg%2Fvo14bG3qmaDQBTsf5p1eobSAiAMmV4hLPhXZPC6m84EQC5YEUNyX7LTYdHh%2Fw3f1h%2BeUir%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIM3bRCjRWd64JuRgoPKtwD2cFLzZp0329KAyd9ktuSivCxHSoj0VH%2Fu010BAMM6zyGfFqpf8c%2FZxQPJUsoaKhKPc59Ej4b%2BTffgS1DuDAG9IElKiHX30GI98SZT5yr%2BpkM16pWeAqpgdp96ZTUOKKVw74dvjnFu%2BAAPGlNaqu52nOkgdul%2FGykNUZj9ulKsxI%2FtMZ%2BXsPfAZC6zkVzmvnVnStL5mY70wvRAzUQv4aWq4%2FcPGXleajVd07tJOn%2B%2Bw3aoJArR1zym4qsEvwXDkEttv81Tx5yJwHfC3ZlMiZOsogdeBqyRwisAPv6HINmXlz%2F6Lz%2Bb9%2Brhb8aGbE%2FwGESiXx4bzDwIcA60JsVfP0683CmwK9n3c7eOIm7SDU%2BZ%2FoEJPytx9eQFESJ0gbpUdlvWBrzkI9Nt%2FZYf1BrsYdz%2FXjCfm5LA5P1poVR2pC0KenHM2zIo2jRwsDVTiBlXdyEQhBYZrepCZgJQyhx3n%2Bqpj0q6tr7UYMm6sCYEPq%2BCSnswO4XAWzh2nDDt5NVfW21lvRFlJWeND67KbnBEEBBXTinDbncUHY6%2BlKGygoKG0dSpmiBKxgptebdQhqBZ96e1C2MgA6AKQQHyUekdTgvryw8K3C0BwUF8V1EoCScoPqiDVIHcWSMdQyk3W0worHlvAY6pgGHtUl9YdX1z%2FF1Ufh%2B9iW3N97HIRzL0Y2Dz%2B4cxAzmV6x8HWlG8KgqrbcjzuW6t%2BzeC%2BZyu2w%2F3nIh7ucV%2BQygKhWcQT5QSQLd8COkVpjifiOiMfEPcuB%2BM5nikvuXzwNY9JlxitBfBX00xj4TiEgywttwizxQqD8nWpPnaLCuIZfiGq9x5QApr5lqjFsG2f8DqaSWwFzJ4%2FNiZE1ybfeomaaOWE3v&X-Amz-Signature=7acbca5a5ecd22379494d84a5f9af746fb25e91dbc4a1dcafc2bdf25475b6780&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WOS5SKS%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJGMEQCIDlln%2BIkagJDpSLUrnIg%2Fvo14bG3qmaDQBTsf5p1eobSAiAMmV4hLPhXZPC6m84EQC5YEUNyX7LTYdHh%2Fw3f1h%2BeUir%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIM3bRCjRWd64JuRgoPKtwD2cFLzZp0329KAyd9ktuSivCxHSoj0VH%2Fu010BAMM6zyGfFqpf8c%2FZxQPJUsoaKhKPc59Ej4b%2BTffgS1DuDAG9IElKiHX30GI98SZT5yr%2BpkM16pWeAqpgdp96ZTUOKKVw74dvjnFu%2BAAPGlNaqu52nOkgdul%2FGykNUZj9ulKsxI%2FtMZ%2BXsPfAZC6zkVzmvnVnStL5mY70wvRAzUQv4aWq4%2FcPGXleajVd07tJOn%2B%2Bw3aoJArR1zym4qsEvwXDkEttv81Tx5yJwHfC3ZlMiZOsogdeBqyRwisAPv6HINmXlz%2F6Lz%2Bb9%2Brhb8aGbE%2FwGESiXx4bzDwIcA60JsVfP0683CmwK9n3c7eOIm7SDU%2BZ%2FoEJPytx9eQFESJ0gbpUdlvWBrzkI9Nt%2FZYf1BrsYdz%2FXjCfm5LA5P1poVR2pC0KenHM2zIo2jRwsDVTiBlXdyEQhBYZrepCZgJQyhx3n%2Bqpj0q6tr7UYMm6sCYEPq%2BCSnswO4XAWzh2nDDt5NVfW21lvRFlJWeND67KbnBEEBBXTinDbncUHY6%2BlKGygoKG0dSpmiBKxgptebdQhqBZ96e1C2MgA6AKQQHyUekdTgvryw8K3C0BwUF8V1EoCScoPqiDVIHcWSMdQyk3W0worHlvAY6pgGHtUl9YdX1z%2FF1Ufh%2B9iW3N97HIRzL0Y2Dz%2B4cxAzmV6x8HWlG8KgqrbcjzuW6t%2BzeC%2BZyu2w%2F3nIh7ucV%2BQygKhWcQT5QSQLd8COkVpjifiOiMfEPcuB%2BM5nikvuXzwNY9JlxitBfBX00xj4TiEgywttwizxQqD8nWpPnaLCuIZfiGq9x5QApr5lqjFsG2f8DqaSWwFzJ4%2FNiZE1ybfeomaaOWE3v&X-Amz-Signature=9ea3fbe31abf07963ac03c4a283eb86c04475114e749db1bfec463b47fba593d&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WOS5SKS%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJGMEQCIDlln%2BIkagJDpSLUrnIg%2Fvo14bG3qmaDQBTsf5p1eobSAiAMmV4hLPhXZPC6m84EQC5YEUNyX7LTYdHh%2Fw3f1h%2BeUir%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIM3bRCjRWd64JuRgoPKtwD2cFLzZp0329KAyd9ktuSivCxHSoj0VH%2Fu010BAMM6zyGfFqpf8c%2FZxQPJUsoaKhKPc59Ej4b%2BTffgS1DuDAG9IElKiHX30GI98SZT5yr%2BpkM16pWeAqpgdp96ZTUOKKVw74dvjnFu%2BAAPGlNaqu52nOkgdul%2FGykNUZj9ulKsxI%2FtMZ%2BXsPfAZC6zkVzmvnVnStL5mY70wvRAzUQv4aWq4%2FcPGXleajVd07tJOn%2B%2Bw3aoJArR1zym4qsEvwXDkEttv81Tx5yJwHfC3ZlMiZOsogdeBqyRwisAPv6HINmXlz%2F6Lz%2Bb9%2Brhb8aGbE%2FwGESiXx4bzDwIcA60JsVfP0683CmwK9n3c7eOIm7SDU%2BZ%2FoEJPytx9eQFESJ0gbpUdlvWBrzkI9Nt%2FZYf1BrsYdz%2FXjCfm5LA5P1poVR2pC0KenHM2zIo2jRwsDVTiBlXdyEQhBYZrepCZgJQyhx3n%2Bqpj0q6tr7UYMm6sCYEPq%2BCSnswO4XAWzh2nDDt5NVfW21lvRFlJWeND67KbnBEEBBXTinDbncUHY6%2BlKGygoKG0dSpmiBKxgptebdQhqBZ96e1C2MgA6AKQQHyUekdTgvryw8K3C0BwUF8V1EoCScoPqiDVIHcWSMdQyk3W0worHlvAY6pgGHtUl9YdX1z%2FF1Ufh%2B9iW3N97HIRzL0Y2Dz%2B4cxAzmV6x8HWlG8KgqrbcjzuW6t%2BzeC%2BZyu2w%2F3nIh7ucV%2BQygKhWcQT5QSQLd8COkVpjifiOiMfEPcuB%2BM5nikvuXzwNY9JlxitBfBX00xj4TiEgywttwizxQqD8nWpPnaLCuIZfiGq9x5QApr5lqjFsG2f8DqaSWwFzJ4%2FNiZE1ybfeomaaOWE3v&X-Amz-Signature=58fd169c7ca23e47c9683ce61eb8379a6c9ac274bd3dabd75ea9d7da112215e1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VT6I5QM4%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJGMEQCIETaLNDT7eng%2F4UAgtw5S0dJwZ9mCtn0uZxDSWFuNa9EAiAsr%2FPkmPPcOK5cFFge0vef2rMRuzlsTRnWhnaRUV1IkCr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMGK41tOMv2eW42ez8KtwD0a7adeOGULLRUJ7bha0E0xVUva4kT31WICeV7blDTioi7XPwGjyya312Bs%2ByDO%2FZtbfnKiNzElfwAZn3N9ZnU6VhLmxYUd5yk6epTwEIfsRNtsNkCStIQeSYvnhWz%2BlUkVi2y6AUPgCSHbLhQwavK8ZKwc6IXhHY0d8Zbsz5XtyhWfI7E58bQdYzZ53crMfrGKVDdQlHbybkPCFStOW7%2FfhhQu7W3TJakz8YlHryg3DLSHT7t6pCHpKkkvSX8V8Zp3swaqof%2FRjbIAMIT2eFOVPsI461jfwhWq3tWVyEcUW%2FHPmOF7YtGbRGikRkjmxbV%2BNHcEUdOYXQCIY8kaDNxFAS2qYOaCY3UN2Y%2BTiUkk2IjnAscms29HVY%2Bx%2BMTx6wcbBZ2aE24x1%2BGF1A9WNfFpii9BOWPxQyzTRDQzwnuXsSk1bBjcbn%2BJF98Ktdyezse%2BDjKH5bMWzV21%2B4wqDDawiWQbVxcdD2m5E1V9EW%2F9niKE3fq%2FQy1e4znUj5FSHQs1ulQr2V3g8UGzv4Xevy1e%2ByGXCkKAn6LeiYjAb5bgOMbYaFgVZcIyF6PXlMHlQ%2BtzJ%2FrC8R0NU1XS2ayA%2BgSu5fQ1cfgll3WYK0dXSKIPlnDtJeGXv4E5E6vesw4LDlvAY6pgGky3GyUyYAC5N3ONV74z8QdfUBxzm6cdCES3iw9RPmNC5pjGHAhbL6f1SGqaaivvRYqJ20%2BlvB896YaCi2Ll5cug1WkzOavzhuu6sQASQa%2BYlr9waRZyfGYv8OxH3%2B9LitLFQePPXH9Ci9IQ%2B%2B%2FmjuHfN2StJYPtZTW9rYvwmGX8HPttPHky8cYhYB28v2FNIJiWT%2Brh1qrrP5KbW%2BNkUlvedRLdz1&X-Amz-Signature=4f76ae3a6b7399f4f62c47477c268a9b1c6d69c539e6f60ca32d884eca71dbe5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662AOWQ43M%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJHMEUCIE4kO%2BGXcBoMB5rFTDKnKQFzWFXZ7wQK39jVMP3TZSPPAiEAkY1LXStu%2FPEgqfA1nYtGUjvqVv59SK64R0LeOusmprsq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDEaSmcnCYbPMGs4tyCrcAxjwfUofcsvVllBbt%2FQ4XrpcOeo1t6C2ryA2ARXtUk54S7CWz%2BDwwW3GRyRSF1W3MlO7yb7lLnDljBy7XcrtJHuza1n06aQ1gK%2BpX9a3uYboAJZa6OhtMC79XaEek8qv%2BKKWVnGG6wFD1TPoEUa99bIr5jcf6g19Mhj8bLSH6hAXI1y5vh3%2FwuSgbLABkjUDegdGxKMX7tuXIwvCKHlr7O3g1MY0KNlVazrO1BKg5%2FAw8QZo9Bta8sdQDb0TE2P2UD5SfMjvjqr5cFBaetbs%2BjJaFsMqGCas9ofvHmZYWjwAZkHqw6ayNk65CMSaQH12MtZokUF8yIby4rj8OMFneXw7lxgquC7QyQbYZz%2BPrjFQUoHli3al6wTcltQmsS3%2BsRAXH%2FhILDBNdcf9UjStuKQHhu7K%2BhY45MRc5HMGbZRwtyMwVf2lGdaMF5L7nEwOG81nRT166rN%2BIf0nAsPt%2BlSu9sEFdJ%2BZ%2B4z5ewtCaXZKIPx5dvGyMd4IlSlJScKpEHNKc3LaJFN1AoV5x9PIVLB9lnvgEsZjeaR9GNT1swIFCjUCkMKEctxy%2BfVE6LWBICj0d8jPUNe1Kx5Sc6mp0PMFcGtizpsfLhQmZM%2Bx9wHeNcnwuP12OIK9x054MK2x5bwGOqUBL8lmsNk2JBSQ8VZNiO2W42eXSrwvBTMG1gBhg0WJAE3cPqFGA5BxNV5QHCDtg11gLgfao9o%2FYyud%2F4pYj4T3JpLCtpux49gT9Exd1QzXr1L9tNQjUAXDhLr5Aqw%2FZ5Dp2pf0kDODjt6FIuntKd9L8fBsZQyhlFjpHR3ImY%2FDEm7aVbcKXY8YwjEZiEGWbc2RjzsNXW80Yy7hTIxLby2R1OkuiWDl&X-Amz-Signature=e33851e35d1b83df4fc6aa9bcf3928d7a70322c1fb7c108327dda61e6ce13f77&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WOS5SKS%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJGMEQCIDlln%2BIkagJDpSLUrnIg%2Fvo14bG3qmaDQBTsf5p1eobSAiAMmV4hLPhXZPC6m84EQC5YEUNyX7LTYdHh%2Fw3f1h%2BeUir%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIM3bRCjRWd64JuRgoPKtwD2cFLzZp0329KAyd9ktuSivCxHSoj0VH%2Fu010BAMM6zyGfFqpf8c%2FZxQPJUsoaKhKPc59Ej4b%2BTffgS1DuDAG9IElKiHX30GI98SZT5yr%2BpkM16pWeAqpgdp96ZTUOKKVw74dvjnFu%2BAAPGlNaqu52nOkgdul%2FGykNUZj9ulKsxI%2FtMZ%2BXsPfAZC6zkVzmvnVnStL5mY70wvRAzUQv4aWq4%2FcPGXleajVd07tJOn%2B%2Bw3aoJArR1zym4qsEvwXDkEttv81Tx5yJwHfC3ZlMiZOsogdeBqyRwisAPv6HINmXlz%2F6Lz%2Bb9%2Brhb8aGbE%2FwGESiXx4bzDwIcA60JsVfP0683CmwK9n3c7eOIm7SDU%2BZ%2FoEJPytx9eQFESJ0gbpUdlvWBrzkI9Nt%2FZYf1BrsYdz%2FXjCfm5LA5P1poVR2pC0KenHM2zIo2jRwsDVTiBlXdyEQhBYZrepCZgJQyhx3n%2Bqpj0q6tr7UYMm6sCYEPq%2BCSnswO4XAWzh2nDDt5NVfW21lvRFlJWeND67KbnBEEBBXTinDbncUHY6%2BlKGygoKG0dSpmiBKxgptebdQhqBZ96e1C2MgA6AKQQHyUekdTgvryw8K3C0BwUF8V1EoCScoPqiDVIHcWSMdQyk3W0worHlvAY6pgGHtUl9YdX1z%2FF1Ufh%2B9iW3N97HIRzL0Y2Dz%2B4cxAzmV6x8HWlG8KgqrbcjzuW6t%2BzeC%2BZyu2w%2F3nIh7ucV%2BQygKhWcQT5QSQLd8COkVpjifiOiMfEPcuB%2BM5nikvuXzwNY9JlxitBfBX00xj4TiEgywttwizxQqD8nWpPnaLCuIZfiGq9x5QApr5lqjFsG2f8DqaSWwFzJ4%2FNiZE1ybfeomaaOWE3v&X-Amz-Signature=e67b1f321d6f243878212ac1f38f5b8d90655b42ac56486e6fa2118f3e4bb16e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WOS5SKS%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJGMEQCIDlln%2BIkagJDpSLUrnIg%2Fvo14bG3qmaDQBTsf5p1eobSAiAMmV4hLPhXZPC6m84EQC5YEUNyX7LTYdHh%2Fw3f1h%2BeUir%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIM3bRCjRWd64JuRgoPKtwD2cFLzZp0329KAyd9ktuSivCxHSoj0VH%2Fu010BAMM6zyGfFqpf8c%2FZxQPJUsoaKhKPc59Ej4b%2BTffgS1DuDAG9IElKiHX30GI98SZT5yr%2BpkM16pWeAqpgdp96ZTUOKKVw74dvjnFu%2BAAPGlNaqu52nOkgdul%2FGykNUZj9ulKsxI%2FtMZ%2BXsPfAZC6zkVzmvnVnStL5mY70wvRAzUQv4aWq4%2FcPGXleajVd07tJOn%2B%2Bw3aoJArR1zym4qsEvwXDkEttv81Tx5yJwHfC3ZlMiZOsogdeBqyRwisAPv6HINmXlz%2F6Lz%2Bb9%2Brhb8aGbE%2FwGESiXx4bzDwIcA60JsVfP0683CmwK9n3c7eOIm7SDU%2BZ%2FoEJPytx9eQFESJ0gbpUdlvWBrzkI9Nt%2FZYf1BrsYdz%2FXjCfm5LA5P1poVR2pC0KenHM2zIo2jRwsDVTiBlXdyEQhBYZrepCZgJQyhx3n%2Bqpj0q6tr7UYMm6sCYEPq%2BCSnswO4XAWzh2nDDt5NVfW21lvRFlJWeND67KbnBEEBBXTinDbncUHY6%2BlKGygoKG0dSpmiBKxgptebdQhqBZ96e1C2MgA6AKQQHyUekdTgvryw8K3C0BwUF8V1EoCScoPqiDVIHcWSMdQyk3W0worHlvAY6pgGHtUl9YdX1z%2FF1Ufh%2B9iW3N97HIRzL0Y2Dz%2B4cxAzmV6x8HWlG8KgqrbcjzuW6t%2BzeC%2BZyu2w%2F3nIh7ucV%2BQygKhWcQT5QSQLd8COkVpjifiOiMfEPcuB%2BM5nikvuXzwNY9JlxitBfBX00xj4TiEgywttwizxQqD8nWpPnaLCuIZfiGq9x5QApr5lqjFsG2f8DqaSWwFzJ4%2FNiZE1ybfeomaaOWE3v&X-Amz-Signature=ec89a9e47a90b4bcd248beca2c74b497bb75e0841dfcb4141bab4ac1a6b5362d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WOS5SKS%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJGMEQCIDlln%2BIkagJDpSLUrnIg%2Fvo14bG3qmaDQBTsf5p1eobSAiAMmV4hLPhXZPC6m84EQC5YEUNyX7LTYdHh%2Fw3f1h%2BeUir%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIM3bRCjRWd64JuRgoPKtwD2cFLzZp0329KAyd9ktuSivCxHSoj0VH%2Fu010BAMM6zyGfFqpf8c%2FZxQPJUsoaKhKPc59Ej4b%2BTffgS1DuDAG9IElKiHX30GI98SZT5yr%2BpkM16pWeAqpgdp96ZTUOKKVw74dvjnFu%2BAAPGlNaqu52nOkgdul%2FGykNUZj9ulKsxI%2FtMZ%2BXsPfAZC6zkVzmvnVnStL5mY70wvRAzUQv4aWq4%2FcPGXleajVd07tJOn%2B%2Bw3aoJArR1zym4qsEvwXDkEttv81Tx5yJwHfC3ZlMiZOsogdeBqyRwisAPv6HINmXlz%2F6Lz%2Bb9%2Brhb8aGbE%2FwGESiXx4bzDwIcA60JsVfP0683CmwK9n3c7eOIm7SDU%2BZ%2FoEJPytx9eQFESJ0gbpUdlvWBrzkI9Nt%2FZYf1BrsYdz%2FXjCfm5LA5P1poVR2pC0KenHM2zIo2jRwsDVTiBlXdyEQhBYZrepCZgJQyhx3n%2Bqpj0q6tr7UYMm6sCYEPq%2BCSnswO4XAWzh2nDDt5NVfW21lvRFlJWeND67KbnBEEBBXTinDbncUHY6%2BlKGygoKG0dSpmiBKxgptebdQhqBZ96e1C2MgA6AKQQHyUekdTgvryw8K3C0BwUF8V1EoCScoPqiDVIHcWSMdQyk3W0worHlvAY6pgGHtUl9YdX1z%2FF1Ufh%2B9iW3N97HIRzL0Y2Dz%2B4cxAzmV6x8HWlG8KgqrbcjzuW6t%2BzeC%2BZyu2w%2F3nIh7ucV%2BQygKhWcQT5QSQLd8COkVpjifiOiMfEPcuB%2BM5nikvuXzwNY9JlxitBfBX00xj4TiEgywttwizxQqD8nWpPnaLCuIZfiGq9x5QApr5lqjFsG2f8DqaSWwFzJ4%2FNiZE1ybfeomaaOWE3v&X-Amz-Signature=dbffe102b5d4f5b25e3fe5e8f993d1510b0620f5f453b32e652b946f32efd645&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WOS5SKS%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJGMEQCIDlln%2BIkagJDpSLUrnIg%2Fvo14bG3qmaDQBTsf5p1eobSAiAMmV4hLPhXZPC6m84EQC5YEUNyX7LTYdHh%2Fw3f1h%2BeUir%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIM3bRCjRWd64JuRgoPKtwD2cFLzZp0329KAyd9ktuSivCxHSoj0VH%2Fu010BAMM6zyGfFqpf8c%2FZxQPJUsoaKhKPc59Ej4b%2BTffgS1DuDAG9IElKiHX30GI98SZT5yr%2BpkM16pWeAqpgdp96ZTUOKKVw74dvjnFu%2BAAPGlNaqu52nOkgdul%2FGykNUZj9ulKsxI%2FtMZ%2BXsPfAZC6zkVzmvnVnStL5mY70wvRAzUQv4aWq4%2FcPGXleajVd07tJOn%2B%2Bw3aoJArR1zym4qsEvwXDkEttv81Tx5yJwHfC3ZlMiZOsogdeBqyRwisAPv6HINmXlz%2F6Lz%2Bb9%2Brhb8aGbE%2FwGESiXx4bzDwIcA60JsVfP0683CmwK9n3c7eOIm7SDU%2BZ%2FoEJPytx9eQFESJ0gbpUdlvWBrzkI9Nt%2FZYf1BrsYdz%2FXjCfm5LA5P1poVR2pC0KenHM2zIo2jRwsDVTiBlXdyEQhBYZrepCZgJQyhx3n%2Bqpj0q6tr7UYMm6sCYEPq%2BCSnswO4XAWzh2nDDt5NVfW21lvRFlJWeND67KbnBEEBBXTinDbncUHY6%2BlKGygoKG0dSpmiBKxgptebdQhqBZ96e1C2MgA6AKQQHyUekdTgvryw8K3C0BwUF8V1EoCScoPqiDVIHcWSMdQyk3W0worHlvAY6pgGHtUl9YdX1z%2FF1Ufh%2B9iW3N97HIRzL0Y2Dz%2B4cxAzmV6x8HWlG8KgqrbcjzuW6t%2BzeC%2BZyu2w%2F3nIh7ucV%2BQygKhWcQT5QSQLd8COkVpjifiOiMfEPcuB%2BM5nikvuXzwNY9JlxitBfBX00xj4TiEgywttwizxQqD8nWpPnaLCuIZfiGq9x5QApr5lqjFsG2f8DqaSWwFzJ4%2FNiZE1ybfeomaaOWE3v&X-Amz-Signature=6cde2d43da7cdefcda88b5ea3fda1b5659264241537bf0c094886308402bfe15&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
