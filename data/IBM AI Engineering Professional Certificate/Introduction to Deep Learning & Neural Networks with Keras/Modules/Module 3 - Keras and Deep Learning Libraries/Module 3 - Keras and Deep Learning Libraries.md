

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJG64RUJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062048Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCICLWiUrGlI7CR%2Bi7EJA6%2ByAvVBdm4KodI%2F1naK4AIbyGAiEAmbkRynNMX1KKSpRjyzwRIdns5I%2BQJFXK3MV0TRE%2FK90q%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDMJLTtr2ORHMuVVGmCrcA85DiWY0%2F%2B29eVNbRoW0s3GFBHqijydVHCt9rh2qv34mzSCGXhzHWrw4SYxpnDwLiql9quh0c7UGfyRf4laIAZjTjGnt05PHOS99SW0JLtSBVPeq%2BS%2BuKXuIjcbIJDA%2BkDjH6HGyJoGgSUtGONEvxENq6X2w1%2BiFM2mkVIHSX7660RTSMjoighTlncwIhWjqU6mxqdLcGKqbrew4JjmcKO7q97OCYx3XcZ3nDKSpRibeb%2BLzcS6hf6NMU8yzJoSt9uPqIEKXUn4HdbcvRGP564EkHrzpa9nqhQS2K1ipHbQTaSUONF85n2R4D93Ydh5A4jdx75jwDDWhv%2B5pariHIi3hkprlP3cXdQLJVE4uUcxssxzSI%2FT1m2LXhrn2du5eLsBfa8DzvB6wbKt%2BSc8xzP7m9%2BOO%2FB2OurmJmb28u62f6vtq%2B3pmhERoKvpOhC6lkrZrW389%2Frv9ESmIZDOIA7T6S9ZtoysmFtGFXVFC7mFB8RoG6Vf5VV1mymTAbw4f5L23BOhm0mekkzgOOp35iFyGFt7fylEd6mrTEm5y%2BAcK%2FsQmuQcpV6k1TYhaxdA3KpVGfo8XpLeCmt3Zewb7HaoBfCfYHeuwpxI%2B3rarRYbG%2FoG%2BF1nXY%2F0DDEdWMIa%2Fhr0GOqUBj69V0I2II1KtCwiRDpPuLEaUCfXz1dhTmntYYrF%2BiKZYVSDSiFQgdRyFu9R8lC7uOULpPAy8cLaQAURu9kXT%2BaIO7rFAkL3RxTk0CouOP4ItMj30FXjqd%2BL%2BossMZu%2B%2ByNML%2F00TipkxZp5SjT5ZBniSNgh%2Br9jbP78Ep3UNKMWcTYQo3TUg1bNrBmRVTtUPtG19obNv%2BoUhozw4s%2BrXreMb2y5g&X-Amz-Signature=af00f4edb769781847621c18eb239675719c0ae34cb64f397739e1fc9462a5a4&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJG64RUJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062048Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCICLWiUrGlI7CR%2Bi7EJA6%2ByAvVBdm4KodI%2F1naK4AIbyGAiEAmbkRynNMX1KKSpRjyzwRIdns5I%2BQJFXK3MV0TRE%2FK90q%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDMJLTtr2ORHMuVVGmCrcA85DiWY0%2F%2B29eVNbRoW0s3GFBHqijydVHCt9rh2qv34mzSCGXhzHWrw4SYxpnDwLiql9quh0c7UGfyRf4laIAZjTjGnt05PHOS99SW0JLtSBVPeq%2BS%2BuKXuIjcbIJDA%2BkDjH6HGyJoGgSUtGONEvxENq6X2w1%2BiFM2mkVIHSX7660RTSMjoighTlncwIhWjqU6mxqdLcGKqbrew4JjmcKO7q97OCYx3XcZ3nDKSpRibeb%2BLzcS6hf6NMU8yzJoSt9uPqIEKXUn4HdbcvRGP564EkHrzpa9nqhQS2K1ipHbQTaSUONF85n2R4D93Ydh5A4jdx75jwDDWhv%2B5pariHIi3hkprlP3cXdQLJVE4uUcxssxzSI%2FT1m2LXhrn2du5eLsBfa8DzvB6wbKt%2BSc8xzP7m9%2BOO%2FB2OurmJmb28u62f6vtq%2B3pmhERoKvpOhC6lkrZrW389%2Frv9ESmIZDOIA7T6S9ZtoysmFtGFXVFC7mFB8RoG6Vf5VV1mymTAbw4f5L23BOhm0mekkzgOOp35iFyGFt7fylEd6mrTEm5y%2BAcK%2FsQmuQcpV6k1TYhaxdA3KpVGfo8XpLeCmt3Zewb7HaoBfCfYHeuwpxI%2B3rarRYbG%2FoG%2BF1nXY%2F0DDEdWMIa%2Fhr0GOqUBj69V0I2II1KtCwiRDpPuLEaUCfXz1dhTmntYYrF%2BiKZYVSDSiFQgdRyFu9R8lC7uOULpPAy8cLaQAURu9kXT%2BaIO7rFAkL3RxTk0CouOP4ItMj30FXjqd%2BL%2BossMZu%2B%2ByNML%2F00TipkxZp5SjT5ZBniSNgh%2Br9jbP78Ep3UNKMWcTYQo3TUg1bNrBmRVTtUPtG19obNv%2BoUhozw4s%2BrXreMb2y5g&X-Amz-Signature=6d1b7808434b537ae1cbcad6c9f8fe2b23d6bfdca157905be108aa1a744dd52f&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJG64RUJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062048Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCICLWiUrGlI7CR%2Bi7EJA6%2ByAvVBdm4KodI%2F1naK4AIbyGAiEAmbkRynNMX1KKSpRjyzwRIdns5I%2BQJFXK3MV0TRE%2FK90q%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDMJLTtr2ORHMuVVGmCrcA85DiWY0%2F%2B29eVNbRoW0s3GFBHqijydVHCt9rh2qv34mzSCGXhzHWrw4SYxpnDwLiql9quh0c7UGfyRf4laIAZjTjGnt05PHOS99SW0JLtSBVPeq%2BS%2BuKXuIjcbIJDA%2BkDjH6HGyJoGgSUtGONEvxENq6X2w1%2BiFM2mkVIHSX7660RTSMjoighTlncwIhWjqU6mxqdLcGKqbrew4JjmcKO7q97OCYx3XcZ3nDKSpRibeb%2BLzcS6hf6NMU8yzJoSt9uPqIEKXUn4HdbcvRGP564EkHrzpa9nqhQS2K1ipHbQTaSUONF85n2R4D93Ydh5A4jdx75jwDDWhv%2B5pariHIi3hkprlP3cXdQLJVE4uUcxssxzSI%2FT1m2LXhrn2du5eLsBfa8DzvB6wbKt%2BSc8xzP7m9%2BOO%2FB2OurmJmb28u62f6vtq%2B3pmhERoKvpOhC6lkrZrW389%2Frv9ESmIZDOIA7T6S9ZtoysmFtGFXVFC7mFB8RoG6Vf5VV1mymTAbw4f5L23BOhm0mekkzgOOp35iFyGFt7fylEd6mrTEm5y%2BAcK%2FsQmuQcpV6k1TYhaxdA3KpVGfo8XpLeCmt3Zewb7HaoBfCfYHeuwpxI%2B3rarRYbG%2FoG%2BF1nXY%2F0DDEdWMIa%2Fhr0GOqUBj69V0I2II1KtCwiRDpPuLEaUCfXz1dhTmntYYrF%2BiKZYVSDSiFQgdRyFu9R8lC7uOULpPAy8cLaQAURu9kXT%2BaIO7rFAkL3RxTk0CouOP4ItMj30FXjqd%2BL%2BossMZu%2B%2ByNML%2F00TipkxZp5SjT5ZBniSNgh%2Br9jbP78Ep3UNKMWcTYQo3TUg1bNrBmRVTtUPtG19obNv%2BoUhozw4s%2BrXreMb2y5g&X-Amz-Signature=2af9478f24040e27ea9e50c85f3e2983e6b66fb61136706340a5edde902aecc3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSVSXHF4%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062049Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQDABQjBwe%2Fjao2NHbFgMyyWesDVBQ3LHfw8a0TV1sE4wAIhAOV4RH0kQuhUvKxYVAytJLe0Jw7TOeHFDVetJ%2BqWn9GBKv8DCCYQABoMNjM3NDIzMTgzODA1IgwnYKhgtoz%2FSJ9%2Bh1gq3AOTqpKU5hsngZi2snxlbg6i%2Fq1gDO3jUeOXN2BX%2BoQ8AmYo5LPmW1RR%2BnM4p%2Bif88i4dIuys1S%2BC51N2vLFLgz2uU3velI8MCJT8taojPSKmaSELSD%2BqTW2FxFgltjMsaLHVJzQBkAKpQRHZRVpP%2F%2BPyb8VRIdmEC0qgXzrnU8PuA0fJPC1Ri8i%2FcqKC4O5S306iIQJ%2Fr%2FVNKyaMhCnR4qFkp%2BO9ggG67t2fg8AX9kjMGpnuI55%2B9eNRDdXmgLFppGT6%2FvvTYxygLKTx6Gu3keBdDpuqyOJaBy4VmSjgRWxO49Emt4MEUgFzPSRvYTdmmyC7a%2FoGJghd02mAwfRLrysg3aqMGqUIHeQLbTrit%2BWnJLZivJHLJlac%2Bg9kDlf2y%2BQEAOSdkH8pFnD%2BBPn23qY1uK7VgseuEXvsgX1Oa%2Fuy7SxTouqf3Ej9rr1bqf6Zicbn4%2BrjnQK1So0EyqkrpjtILaWidFPnyRdz%2Bz54Ne%2FhqNC7Ld%2FUckdhaxBRnak%2Fizcd3ezIYgonDhMtph3HgMZ1bKD0u7B92za7FTV%2FDouO1JVJNE6%2B5BoVUF2TZMt7kqcWbMam91wfldK69kEagIJY73g%2BiIX7GwKmmhpBztMBPI6u5iAqtzTbCWLrjC0voa9BjqkAaJdCI1RJcwb5YqfFW4B0Ob7PQac2daImUj4C5MkD1e9cy7YbcPjH8Yo6IkxZsMnc7HS4BYryYUjPHdgy2JZt0uovhk8IHAGXiIDliR8a0JgpBIAQnFBp3Pm5sw8SyG7NXxqizcBX4shq9MIVNnLa8Q6n8uIietuo8%2BUvVC6hUStmHRjoY3CxbrbCP9JXX%2B7kDnf4D1fetARRO3ZlNxBDlr1iBlA&X-Amz-Signature=b113bd102e7a4942b665af849be6c7ac4949a649495e0d9058a43a8c480727ec&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YKX3RMPZ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062049Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQCQM9946Xt3eTlqZiJ9Lb4VNFQ1oTqg0FMxhoJlrNAaYgIgP4IYs1onowijNs1ek%2F2sL6tHf5uA1KLadG%2B9SY6QllUq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDDeoHJZeffwsUV1BVCrcA3x3Y9%2BqR90xHXV9arwQpcjZCcFLUHc1IiSR0Aqn317fM4FXNpwxK3tfC1mfbMh67jZw6I1s881OL4JSFgOQaGwyCcioivy8PJ9J%2BC0i%2FmvXABChmd6mDwEjESOnNVao1JM%2FLPTbKu7%2BU3VCo72QZn43RsnG%2FMNufogtzVmoWVt6tzWReboH11alFlPx63De%2BX47EqIuaxI7v%2BXCpo%2FNYfUMqqrngeHOqdflq6RRS34067nlXEs0X%2FoAmCvrW4H59fh7AXa0sTaVx3Y5P1qX%2B6sWeGJd%2F3zwBm6GRBBI3dzxttkIds9nQ%2Fg9%2FO6mH3RXaBNsdP0DGB7iNrnp7h9z0g5bZ0EttwSNDM31TQd3PbqU%2FkfR3twE%2FVwReW9%2FeBJ%2BN30Tm81P9hofmcJiwhWHfanyQR%2BWItdHVEyOtx%2FGrJi5GjGQFTxPGQHPVpvYnu8wTnEK1OKQSd71WBJY0lvLImzgdyNfr%2Fxd8LifR4FEZLRIpX8STtgpe8Qf6MRR032L2C2IyfkonNMXkCpkuvfj6HBsQOGmoqzkXWKKzwvstR7Dk71Q5AZvyxYrU7OgCLEVCjWGiKFeUm3%2B4hHrBFSXFcf2q3Ra0pID%2BixHf9ICEFCepYKKWXPC%2FnQC9XNPMKK%2Fhr0GOqUBtuuScLbftSMtHOh9DBg0p1%2BdiYeWdJ%2BND5A74u2%2Bkl4CVPk40A5NXlz%2FgOhDe9J8LLLGgaNTz2bhKV9fWr3dbAliTjjm8ulN7A9jKdeUk92EWSJXeq7e4tOZMiODnVLLtIBluVqJ31g8M3oW9l08HDwue5wWBBLWspZH6l5y71xSACiQAxPpgTUa5k3kss2C%2F%2FvgsY33VwBcUfIA6i%2FZrGXcg%2BHG&X-Amz-Signature=2bc2c97f456434cf2cd8ed69a385098a04b6d0c52609ab10023e39656f0fb7cb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJG64RUJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062048Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCICLWiUrGlI7CR%2Bi7EJA6%2ByAvVBdm4KodI%2F1naK4AIbyGAiEAmbkRynNMX1KKSpRjyzwRIdns5I%2BQJFXK3MV0TRE%2FK90q%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDMJLTtr2ORHMuVVGmCrcA85DiWY0%2F%2B29eVNbRoW0s3GFBHqijydVHCt9rh2qv34mzSCGXhzHWrw4SYxpnDwLiql9quh0c7UGfyRf4laIAZjTjGnt05PHOS99SW0JLtSBVPeq%2BS%2BuKXuIjcbIJDA%2BkDjH6HGyJoGgSUtGONEvxENq6X2w1%2BiFM2mkVIHSX7660RTSMjoighTlncwIhWjqU6mxqdLcGKqbrew4JjmcKO7q97OCYx3XcZ3nDKSpRibeb%2BLzcS6hf6NMU8yzJoSt9uPqIEKXUn4HdbcvRGP564EkHrzpa9nqhQS2K1ipHbQTaSUONF85n2R4D93Ydh5A4jdx75jwDDWhv%2B5pariHIi3hkprlP3cXdQLJVE4uUcxssxzSI%2FT1m2LXhrn2du5eLsBfa8DzvB6wbKt%2BSc8xzP7m9%2BOO%2FB2OurmJmb28u62f6vtq%2B3pmhERoKvpOhC6lkrZrW389%2Frv9ESmIZDOIA7T6S9ZtoysmFtGFXVFC7mFB8RoG6Vf5VV1mymTAbw4f5L23BOhm0mekkzgOOp35iFyGFt7fylEd6mrTEm5y%2BAcK%2FsQmuQcpV6k1TYhaxdA3KpVGfo8XpLeCmt3Zewb7HaoBfCfYHeuwpxI%2B3rarRYbG%2FoG%2BF1nXY%2F0DDEdWMIa%2Fhr0GOqUBj69V0I2II1KtCwiRDpPuLEaUCfXz1dhTmntYYrF%2BiKZYVSDSiFQgdRyFu9R8lC7uOULpPAy8cLaQAURu9kXT%2BaIO7rFAkL3RxTk0CouOP4ItMj30FXjqd%2BL%2BossMZu%2B%2ByNML%2F00TipkxZp5SjT5ZBniSNgh%2Br9jbP78Ep3UNKMWcTYQo3TUg1bNrBmRVTtUPtG19obNv%2BoUhozw4s%2BrXreMb2y5g&X-Amz-Signature=a20c00030edd07711c7e5ac46d204da258ab4c78ae0d28cc41cfefbf598a3465&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJG64RUJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062048Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCICLWiUrGlI7CR%2Bi7EJA6%2ByAvVBdm4KodI%2F1naK4AIbyGAiEAmbkRynNMX1KKSpRjyzwRIdns5I%2BQJFXK3MV0TRE%2FK90q%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDMJLTtr2ORHMuVVGmCrcA85DiWY0%2F%2B29eVNbRoW0s3GFBHqijydVHCt9rh2qv34mzSCGXhzHWrw4SYxpnDwLiql9quh0c7UGfyRf4laIAZjTjGnt05PHOS99SW0JLtSBVPeq%2BS%2BuKXuIjcbIJDA%2BkDjH6HGyJoGgSUtGONEvxENq6X2w1%2BiFM2mkVIHSX7660RTSMjoighTlncwIhWjqU6mxqdLcGKqbrew4JjmcKO7q97OCYx3XcZ3nDKSpRibeb%2BLzcS6hf6NMU8yzJoSt9uPqIEKXUn4HdbcvRGP564EkHrzpa9nqhQS2K1ipHbQTaSUONF85n2R4D93Ydh5A4jdx75jwDDWhv%2B5pariHIi3hkprlP3cXdQLJVE4uUcxssxzSI%2FT1m2LXhrn2du5eLsBfa8DzvB6wbKt%2BSc8xzP7m9%2BOO%2FB2OurmJmb28u62f6vtq%2B3pmhERoKvpOhC6lkrZrW389%2Frv9ESmIZDOIA7T6S9ZtoysmFtGFXVFC7mFB8RoG6Vf5VV1mymTAbw4f5L23BOhm0mekkzgOOp35iFyGFt7fylEd6mrTEm5y%2BAcK%2FsQmuQcpV6k1TYhaxdA3KpVGfo8XpLeCmt3Zewb7HaoBfCfYHeuwpxI%2B3rarRYbG%2FoG%2BF1nXY%2F0DDEdWMIa%2Fhr0GOqUBj69V0I2II1KtCwiRDpPuLEaUCfXz1dhTmntYYrF%2BiKZYVSDSiFQgdRyFu9R8lC7uOULpPAy8cLaQAURu9kXT%2BaIO7rFAkL3RxTk0CouOP4ItMj30FXjqd%2BL%2BossMZu%2B%2ByNML%2F00TipkxZp5SjT5ZBniSNgh%2Br9jbP78Ep3UNKMWcTYQo3TUg1bNrBmRVTtUPtG19obNv%2BoUhozw4s%2BrXreMb2y5g&X-Amz-Signature=12fc999e3e905df385d59da897da1009582764a0c4fabb4c41030ce90f7d86ef&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJG64RUJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062048Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCICLWiUrGlI7CR%2Bi7EJA6%2ByAvVBdm4KodI%2F1naK4AIbyGAiEAmbkRynNMX1KKSpRjyzwRIdns5I%2BQJFXK3MV0TRE%2FK90q%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDMJLTtr2ORHMuVVGmCrcA85DiWY0%2F%2B29eVNbRoW0s3GFBHqijydVHCt9rh2qv34mzSCGXhzHWrw4SYxpnDwLiql9quh0c7UGfyRf4laIAZjTjGnt05PHOS99SW0JLtSBVPeq%2BS%2BuKXuIjcbIJDA%2BkDjH6HGyJoGgSUtGONEvxENq6X2w1%2BiFM2mkVIHSX7660RTSMjoighTlncwIhWjqU6mxqdLcGKqbrew4JjmcKO7q97OCYx3XcZ3nDKSpRibeb%2BLzcS6hf6NMU8yzJoSt9uPqIEKXUn4HdbcvRGP564EkHrzpa9nqhQS2K1ipHbQTaSUONF85n2R4D93Ydh5A4jdx75jwDDWhv%2B5pariHIi3hkprlP3cXdQLJVE4uUcxssxzSI%2FT1m2LXhrn2du5eLsBfa8DzvB6wbKt%2BSc8xzP7m9%2BOO%2FB2OurmJmb28u62f6vtq%2B3pmhERoKvpOhC6lkrZrW389%2Frv9ESmIZDOIA7T6S9ZtoysmFtGFXVFC7mFB8RoG6Vf5VV1mymTAbw4f5L23BOhm0mekkzgOOp35iFyGFt7fylEd6mrTEm5y%2BAcK%2FsQmuQcpV6k1TYhaxdA3KpVGfo8XpLeCmt3Zewb7HaoBfCfYHeuwpxI%2B3rarRYbG%2FoG%2BF1nXY%2F0DDEdWMIa%2Fhr0GOqUBj69V0I2II1KtCwiRDpPuLEaUCfXz1dhTmntYYrF%2BiKZYVSDSiFQgdRyFu9R8lC7uOULpPAy8cLaQAURu9kXT%2BaIO7rFAkL3RxTk0CouOP4ItMj30FXjqd%2BL%2BossMZu%2B%2ByNML%2F00TipkxZp5SjT5ZBniSNgh%2Br9jbP78Ep3UNKMWcTYQo3TUg1bNrBmRVTtUPtG19obNv%2BoUhozw4s%2BrXreMb2y5g&X-Amz-Signature=78718963810154b0e8076b671e2c741bb5a3061fbadf0205efeb8e21babebef3&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJG64RUJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062048Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCICLWiUrGlI7CR%2Bi7EJA6%2ByAvVBdm4KodI%2F1naK4AIbyGAiEAmbkRynNMX1KKSpRjyzwRIdns5I%2BQJFXK3MV0TRE%2FK90q%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDMJLTtr2ORHMuVVGmCrcA85DiWY0%2F%2B29eVNbRoW0s3GFBHqijydVHCt9rh2qv34mzSCGXhzHWrw4SYxpnDwLiql9quh0c7UGfyRf4laIAZjTjGnt05PHOS99SW0JLtSBVPeq%2BS%2BuKXuIjcbIJDA%2BkDjH6HGyJoGgSUtGONEvxENq6X2w1%2BiFM2mkVIHSX7660RTSMjoighTlncwIhWjqU6mxqdLcGKqbrew4JjmcKO7q97OCYx3XcZ3nDKSpRibeb%2BLzcS6hf6NMU8yzJoSt9uPqIEKXUn4HdbcvRGP564EkHrzpa9nqhQS2K1ipHbQTaSUONF85n2R4D93Ydh5A4jdx75jwDDWhv%2B5pariHIi3hkprlP3cXdQLJVE4uUcxssxzSI%2FT1m2LXhrn2du5eLsBfa8DzvB6wbKt%2BSc8xzP7m9%2BOO%2FB2OurmJmb28u62f6vtq%2B3pmhERoKvpOhC6lkrZrW389%2Frv9ESmIZDOIA7T6S9ZtoysmFtGFXVFC7mFB8RoG6Vf5VV1mymTAbw4f5L23BOhm0mekkzgOOp35iFyGFt7fylEd6mrTEm5y%2BAcK%2FsQmuQcpV6k1TYhaxdA3KpVGfo8XpLeCmt3Zewb7HaoBfCfYHeuwpxI%2B3rarRYbG%2FoG%2BF1nXY%2F0DDEdWMIa%2Fhr0GOqUBj69V0I2II1KtCwiRDpPuLEaUCfXz1dhTmntYYrF%2BiKZYVSDSiFQgdRyFu9R8lC7uOULpPAy8cLaQAURu9kXT%2BaIO7rFAkL3RxTk0CouOP4ItMj30FXjqd%2BL%2BossMZu%2B%2ByNML%2F00TipkxZp5SjT5ZBniSNgh%2Br9jbP78Ep3UNKMWcTYQo3TUg1bNrBmRVTtUPtG19obNv%2BoUhozw4s%2BrXreMb2y5g&X-Amz-Signature=371d4b3e186bd287c953009b5736beb3a1402a0a142a96a61ca501dd288d2245&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
