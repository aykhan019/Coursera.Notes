

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGVL62U5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQDsWPUNseuv3KHL7k2KI0aQvZEPFK6JASBSc82xgViujAIgWOCNfvdTbDXPj22GSRbONlhc%2BO1JQfAaYtsdqRRh3nwq%2FwMIQhAAGgw2Mzc0MjMxODM4MDUiDGo9pe3KFQ2JfgixdSrcAyXxKVGxv67JQXURxtd2nI7d3qqLPC%2FegFaCZRiOGWJ7LGbbdtxF%2B29%2BbgTJuOKI%2FlWMhIyy2jNj4agKOmDaOSzu560tbenCsR69%2B4tepzzdh9Pmi2Ynn3b3NvIteNfVPF57wphGhwxwjlgGFEabElgjk9MP48QXWzEynaFptSpIK465Hm7F%2BsrxmLNrb7K%2BaxbrBVRKpHtBbs0JBn%2Fb%2B8cXW7GET6vk3NA1Uv6ravB%2FyIFHHmnbYpndFVD%2BlBh0CdhY%2FqXNf3voek68TPE2ar4OyKj6gp06WzdfUlISDCwtyC1SUwehiaL%2FRY7R9wHh55hHueXty1WaIpg6e49JFbYmlZv02qBZziAzi65s0aqImfEdomCJcULGSKoSts%2BM4gQRqf8Kq7uT4XJOVa4ZAahcgWU%2FU%2Fv6vm0SLBeKay9jkvuXUw%2Bm9nt68EsG6tQRTxxzEsjYE2TgZYb%2FX1wVeNyT22yUcXoRExEDw53yFxaCyb%2FnMkvbpgvxY27tLb2RilurI3Cip%2B04X5GVESUckH%2BILJCrXp1PslD6c5SrAOHQxBrs%2BJJm9%2Fc7RvVjmv9ez0a20QnGvDzanYeydAnvepDfnjFAGTgio347aWQYOLqjwwuB6b61jNElkarXMLzPjL0GOqUBbR1ZGJ%2F5UB9H7OXekXf6LV83XnFv4LeXc4yGRF%2FjUA%2FMswo7UgDV3T7B5EyZosuDRqkV4cBx2Tkz6z%2FYePxUfJj0Lzaq1MkJec2FYzyZ5l1jq3uVxztjSTXSq6XZ4CooYLwu4vS1tkuYDnLPPIDDH0hoFysnflILcXy9fQNbHA0B6WG%2Fe8UGKPvyLGctSK98aBvSPzKCjOGtB%2BOAi8Sj3Fs75%2B%2Bf&X-Amz-Signature=05f7b82c8819b0996d1bf9fcdbd273116adc1da6bb32f21073da57ee807206c5&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGVL62U5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQDsWPUNseuv3KHL7k2KI0aQvZEPFK6JASBSc82xgViujAIgWOCNfvdTbDXPj22GSRbONlhc%2BO1JQfAaYtsdqRRh3nwq%2FwMIQhAAGgw2Mzc0MjMxODM4MDUiDGo9pe3KFQ2JfgixdSrcAyXxKVGxv67JQXURxtd2nI7d3qqLPC%2FegFaCZRiOGWJ7LGbbdtxF%2B29%2BbgTJuOKI%2FlWMhIyy2jNj4agKOmDaOSzu560tbenCsR69%2B4tepzzdh9Pmi2Ynn3b3NvIteNfVPF57wphGhwxwjlgGFEabElgjk9MP48QXWzEynaFptSpIK465Hm7F%2BsrxmLNrb7K%2BaxbrBVRKpHtBbs0JBn%2Fb%2B8cXW7GET6vk3NA1Uv6ravB%2FyIFHHmnbYpndFVD%2BlBh0CdhY%2FqXNf3voek68TPE2ar4OyKj6gp06WzdfUlISDCwtyC1SUwehiaL%2FRY7R9wHh55hHueXty1WaIpg6e49JFbYmlZv02qBZziAzi65s0aqImfEdomCJcULGSKoSts%2BM4gQRqf8Kq7uT4XJOVa4ZAahcgWU%2FU%2Fv6vm0SLBeKay9jkvuXUw%2Bm9nt68EsG6tQRTxxzEsjYE2TgZYb%2FX1wVeNyT22yUcXoRExEDw53yFxaCyb%2FnMkvbpgvxY27tLb2RilurI3Cip%2B04X5GVESUckH%2BILJCrXp1PslD6c5SrAOHQxBrs%2BJJm9%2Fc7RvVjmv9ez0a20QnGvDzanYeydAnvepDfnjFAGTgio347aWQYOLqjwwuB6b61jNElkarXMLzPjL0GOqUBbR1ZGJ%2F5UB9H7OXekXf6LV83XnFv4LeXc4yGRF%2FjUA%2FMswo7UgDV3T7B5EyZosuDRqkV4cBx2Tkz6z%2FYePxUfJj0Lzaq1MkJec2FYzyZ5l1jq3uVxztjSTXSq6XZ4CooYLwu4vS1tkuYDnLPPIDDH0hoFysnflILcXy9fQNbHA0B6WG%2Fe8UGKPvyLGctSK98aBvSPzKCjOGtB%2BOAi8Sj3Fs75%2B%2Bf&X-Amz-Signature=7cb9ee744a4f1e61a8aca6224a092b4ba07b7a73be4edbeb50b082bca8fa0dc7&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGVL62U5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQDsWPUNseuv3KHL7k2KI0aQvZEPFK6JASBSc82xgViujAIgWOCNfvdTbDXPj22GSRbONlhc%2BO1JQfAaYtsdqRRh3nwq%2FwMIQhAAGgw2Mzc0MjMxODM4MDUiDGo9pe3KFQ2JfgixdSrcAyXxKVGxv67JQXURxtd2nI7d3qqLPC%2FegFaCZRiOGWJ7LGbbdtxF%2B29%2BbgTJuOKI%2FlWMhIyy2jNj4agKOmDaOSzu560tbenCsR69%2B4tepzzdh9Pmi2Ynn3b3NvIteNfVPF57wphGhwxwjlgGFEabElgjk9MP48QXWzEynaFptSpIK465Hm7F%2BsrxmLNrb7K%2BaxbrBVRKpHtBbs0JBn%2Fb%2B8cXW7GET6vk3NA1Uv6ravB%2FyIFHHmnbYpndFVD%2BlBh0CdhY%2FqXNf3voek68TPE2ar4OyKj6gp06WzdfUlISDCwtyC1SUwehiaL%2FRY7R9wHh55hHueXty1WaIpg6e49JFbYmlZv02qBZziAzi65s0aqImfEdomCJcULGSKoSts%2BM4gQRqf8Kq7uT4XJOVa4ZAahcgWU%2FU%2Fv6vm0SLBeKay9jkvuXUw%2Bm9nt68EsG6tQRTxxzEsjYE2TgZYb%2FX1wVeNyT22yUcXoRExEDw53yFxaCyb%2FnMkvbpgvxY27tLb2RilurI3Cip%2B04X5GVESUckH%2BILJCrXp1PslD6c5SrAOHQxBrs%2BJJm9%2Fc7RvVjmv9ez0a20QnGvDzanYeydAnvepDfnjFAGTgio347aWQYOLqjwwuB6b61jNElkarXMLzPjL0GOqUBbR1ZGJ%2F5UB9H7OXekXf6LV83XnFv4LeXc4yGRF%2FjUA%2FMswo7UgDV3T7B5EyZosuDRqkV4cBx2Tkz6z%2FYePxUfJj0Lzaq1MkJec2FYzyZ5l1jq3uVxztjSTXSq6XZ4CooYLwu4vS1tkuYDnLPPIDDH0hoFysnflILcXy9fQNbHA0B6WG%2Fe8UGKPvyLGctSK98aBvSPzKCjOGtB%2BOAi8Sj3Fs75%2B%2Bf&X-Amz-Signature=25067a04753213c6863355bfb8f3b6910d0e11bc29365177be6d84a31ad9355d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z7MJHLKR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJGMEQCIDegUMsIDzm7lXBCDjB7W0bvHU4igBODTWp5PNrx9IVmAiAzyE8yyhiF0Ncza6q7e%2BlXstgPy7UbB6pKv7PWLUL4Air%2FAwhCEAAaDDYzNzQyMzE4MzgwNSIMubOzRlCDeAVo%2B6nWKtwDcjpRarNS39g3L3cRitnD85Dw9xXCr3IGLZmSFkDVQ05k6wgTucnQC%2FfDCj4GNYNDS%2BOI%2FkhJT%2Fwt4l7XbjcJD1JgsoY1fhRuG5uveXmlB91yqG0n2h5sKmYeQUQCJYTmT16STQMtiLxAR3kTjorSufzxCZyLFLxBi%2BclHXwg4A%2B4NSe0fR5cNtdII5Hcc3A1jRYYiBK%2FeqIQmJ%2FbaE%2B9Cc80EfMEg6jyN3wnhofjw0NP%2BGRMZEBCK7oNbX2yeGQ4gUGV7ib5k8HGLHVYPNRD99qywJwTCZ4muYzaYSQqe9S6z1SxxUAujA1epIamONgcElYR7c64l49TRPziiS2ORuj2Fwx%2Fglnx2CQgyhqDgIqpkk6QInTxGFrn40oRBlx7rytygnE1MXs74qD%2BDDdWyVpptM3ONTg0g78JMpHQno9nVUjGPg%2F61vESagSRHft8fdOE%2FTTztvxP38bIo74HgaIkjyE%2F559eSFxEpIZ3xVzBj8AHOEgu2OqdMlrfaediE%2B1%2FRowQAK9Mc%2BE94mJJqTgpMPiHUuKsotFZrGfHjxJDNcBezUvv07lLKuHH4MRvCfICFZpkee6fOTpX7ZBt3EMowDV2YfVnwfHVqHfR3BCy8nrIPVeawF%2FGiJ8wt8%2BMvQY6pgGooqeBbjsgmIeD4JCP0QDu0ghFalCSAWqsx7uyOu6aPdJq%2BUm8h9UranJSAsNpZ0qWEEsOWLDLeSSgBnUZ1bylHLGAz5Hs%2B7f6DA5I3%2Bpr%2B27108Ggk7k8wcHeRTIlYhU65SfmyFr1wA43pxJW3%2FbPCeUGAK3riuur3ngumEepoXes6fAVubZrp4BZUbVucslTg8Urjh9%2BJ2LFeGxWkcLm38mhS6kJ&X-Amz-Signature=4bc43f00e482d115d4329557c76c1b58e7bbe1296fbb7868df02da37b6ff1e30&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466262RSHLY%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCID3YAqCqfyH%2F9Kr7hkX7wvYcHNUUyCA8Ms9Q47N0HB7oAiEA%2FNyRojnZFVFxN07FrQIP0q56YHYSFLIJd3UFACV2Ovkq%2FwMIQhAAGgw2Mzc0MjMxODM4MDUiDFMiANcpCtok9UgweircAwVdESvsfcxCTmFe%2BjKiGq4qMCvnvgZ5OGVffuuQyORqGqtzbpoTnWLrmM9qlw%2BKqGyyiNdUmNoBXLOytRowUOireRHtoPTyU2oeGvn8zQbIwpVXxS569PnOTBZk%2BOkW4C4Ut2RPAE7WHSgJRDt0r6ESry1lsxqigqbDFSB1DJizQIoDvXY%2BhE9jD%2BfEZn3FtB3TWID1xhgRzyH90O3ciT8UGSoXoBGp09A2zRyEdRDIwvYJVvbaLGlyIx4Yn2wpBircUJ%2FyYGuheuWIn6M%2BfOec0nZKHGvzaeQOF8joBuvsLfTUZKXll9DG3ZEdgB%2Fa6fjx4ZdHfq07ihp%2FGvro2lAfj%2Bf2vEB8q3FqmeeNWrBoaqjRHG4FlptXmYutr%2FwBK3uoc29YXfGZJlpSQ87ygCNSA9J9VOIIoyYP59oKpZRWmRiy%2BHtHv4gIqWDMn%2BANceX2t1qc47t56COBjpjo3Cuo8qpPq4g8VsmD9I1ABPQ7t7vrgR3mzY8XOMdK83KilGSd%2FHv2Ot4us77EhbrdqpwJxpC59Etd3jrujA79BHDZoeYuNMEAEHXF1CnLzsGt3GE%2B3Nvte2HjIl9emnPX7jAe4wfsidIniCjWmpVFESrs9rJXR1f%2F91QHCAO5MKjPjL0GOqUBPozGQ7Sbuo5B9guawrdHtp49rme389bP%2BpL30U7RLje%2F3hrbKvL2jRgauGeoKD1LvQC0%2Bvh3Bh4hVkz8hetw%2F9hDmoKNG3HIp5GkSjYYvySinCIALsIdcdABM9aTscxfGK8cZuz83AjNBBW%2FU8u%2FMac3NLXP93ZyJai8B%2FAJFR6%2Fov7AqrVIvPJWrLQAdTEmtJGHPnWBW2SchN3sBGknNR%2FI46Pr&X-Amz-Signature=f74b4d9940fa8d68dc19cc7e75ee51a12289f26a272011ed7385361dd4d29e19&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGVL62U5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQDsWPUNseuv3KHL7k2KI0aQvZEPFK6JASBSc82xgViujAIgWOCNfvdTbDXPj22GSRbONlhc%2BO1JQfAaYtsdqRRh3nwq%2FwMIQhAAGgw2Mzc0MjMxODM4MDUiDGo9pe3KFQ2JfgixdSrcAyXxKVGxv67JQXURxtd2nI7d3qqLPC%2FegFaCZRiOGWJ7LGbbdtxF%2B29%2BbgTJuOKI%2FlWMhIyy2jNj4agKOmDaOSzu560tbenCsR69%2B4tepzzdh9Pmi2Ynn3b3NvIteNfVPF57wphGhwxwjlgGFEabElgjk9MP48QXWzEynaFptSpIK465Hm7F%2BsrxmLNrb7K%2BaxbrBVRKpHtBbs0JBn%2Fb%2B8cXW7GET6vk3NA1Uv6ravB%2FyIFHHmnbYpndFVD%2BlBh0CdhY%2FqXNf3voek68TPE2ar4OyKj6gp06WzdfUlISDCwtyC1SUwehiaL%2FRY7R9wHh55hHueXty1WaIpg6e49JFbYmlZv02qBZziAzi65s0aqImfEdomCJcULGSKoSts%2BM4gQRqf8Kq7uT4XJOVa4ZAahcgWU%2FU%2Fv6vm0SLBeKay9jkvuXUw%2Bm9nt68EsG6tQRTxxzEsjYE2TgZYb%2FX1wVeNyT22yUcXoRExEDw53yFxaCyb%2FnMkvbpgvxY27tLb2RilurI3Cip%2B04X5GVESUckH%2BILJCrXp1PslD6c5SrAOHQxBrs%2BJJm9%2Fc7RvVjmv9ez0a20QnGvDzanYeydAnvepDfnjFAGTgio347aWQYOLqjwwuB6b61jNElkarXMLzPjL0GOqUBbR1ZGJ%2F5UB9H7OXekXf6LV83XnFv4LeXc4yGRF%2FjUA%2FMswo7UgDV3T7B5EyZosuDRqkV4cBx2Tkz6z%2FYePxUfJj0Lzaq1MkJec2FYzyZ5l1jq3uVxztjSTXSq6XZ4CooYLwu4vS1tkuYDnLPPIDDH0hoFysnflILcXy9fQNbHA0B6WG%2Fe8UGKPvyLGctSK98aBvSPzKCjOGtB%2BOAi8Sj3Fs75%2B%2Bf&X-Amz-Signature=759963dd64cfd4e0f9747efe31dbc9421ed1970de927c863b94054ecb8988123&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGVL62U5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQDsWPUNseuv3KHL7k2KI0aQvZEPFK6JASBSc82xgViujAIgWOCNfvdTbDXPj22GSRbONlhc%2BO1JQfAaYtsdqRRh3nwq%2FwMIQhAAGgw2Mzc0MjMxODM4MDUiDGo9pe3KFQ2JfgixdSrcAyXxKVGxv67JQXURxtd2nI7d3qqLPC%2FegFaCZRiOGWJ7LGbbdtxF%2B29%2BbgTJuOKI%2FlWMhIyy2jNj4agKOmDaOSzu560tbenCsR69%2B4tepzzdh9Pmi2Ynn3b3NvIteNfVPF57wphGhwxwjlgGFEabElgjk9MP48QXWzEynaFptSpIK465Hm7F%2BsrxmLNrb7K%2BaxbrBVRKpHtBbs0JBn%2Fb%2B8cXW7GET6vk3NA1Uv6ravB%2FyIFHHmnbYpndFVD%2BlBh0CdhY%2FqXNf3voek68TPE2ar4OyKj6gp06WzdfUlISDCwtyC1SUwehiaL%2FRY7R9wHh55hHueXty1WaIpg6e49JFbYmlZv02qBZziAzi65s0aqImfEdomCJcULGSKoSts%2BM4gQRqf8Kq7uT4XJOVa4ZAahcgWU%2FU%2Fv6vm0SLBeKay9jkvuXUw%2Bm9nt68EsG6tQRTxxzEsjYE2TgZYb%2FX1wVeNyT22yUcXoRExEDw53yFxaCyb%2FnMkvbpgvxY27tLb2RilurI3Cip%2B04X5GVESUckH%2BILJCrXp1PslD6c5SrAOHQxBrs%2BJJm9%2Fc7RvVjmv9ez0a20QnGvDzanYeydAnvepDfnjFAGTgio347aWQYOLqjwwuB6b61jNElkarXMLzPjL0GOqUBbR1ZGJ%2F5UB9H7OXekXf6LV83XnFv4LeXc4yGRF%2FjUA%2FMswo7UgDV3T7B5EyZosuDRqkV4cBx2Tkz6z%2FYePxUfJj0Lzaq1MkJec2FYzyZ5l1jq3uVxztjSTXSq6XZ4CooYLwu4vS1tkuYDnLPPIDDH0hoFysnflILcXy9fQNbHA0B6WG%2Fe8UGKPvyLGctSK98aBvSPzKCjOGtB%2BOAi8Sj3Fs75%2B%2Bf&X-Amz-Signature=89ea21f1ba259f7b97267bd0cc0b125b041347a90f71fc15dc31bf922622343f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGVL62U5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQDsWPUNseuv3KHL7k2KI0aQvZEPFK6JASBSc82xgViujAIgWOCNfvdTbDXPj22GSRbONlhc%2BO1JQfAaYtsdqRRh3nwq%2FwMIQhAAGgw2Mzc0MjMxODM4MDUiDGo9pe3KFQ2JfgixdSrcAyXxKVGxv67JQXURxtd2nI7d3qqLPC%2FegFaCZRiOGWJ7LGbbdtxF%2B29%2BbgTJuOKI%2FlWMhIyy2jNj4agKOmDaOSzu560tbenCsR69%2B4tepzzdh9Pmi2Ynn3b3NvIteNfVPF57wphGhwxwjlgGFEabElgjk9MP48QXWzEynaFptSpIK465Hm7F%2BsrxmLNrb7K%2BaxbrBVRKpHtBbs0JBn%2Fb%2B8cXW7GET6vk3NA1Uv6ravB%2FyIFHHmnbYpndFVD%2BlBh0CdhY%2FqXNf3voek68TPE2ar4OyKj6gp06WzdfUlISDCwtyC1SUwehiaL%2FRY7R9wHh55hHueXty1WaIpg6e49JFbYmlZv02qBZziAzi65s0aqImfEdomCJcULGSKoSts%2BM4gQRqf8Kq7uT4XJOVa4ZAahcgWU%2FU%2Fv6vm0SLBeKay9jkvuXUw%2Bm9nt68EsG6tQRTxxzEsjYE2TgZYb%2FX1wVeNyT22yUcXoRExEDw53yFxaCyb%2FnMkvbpgvxY27tLb2RilurI3Cip%2B04X5GVESUckH%2BILJCrXp1PslD6c5SrAOHQxBrs%2BJJm9%2Fc7RvVjmv9ez0a20QnGvDzanYeydAnvepDfnjFAGTgio347aWQYOLqjwwuB6b61jNElkarXMLzPjL0GOqUBbR1ZGJ%2F5UB9H7OXekXf6LV83XnFv4LeXc4yGRF%2FjUA%2FMswo7UgDV3T7B5EyZosuDRqkV4cBx2Tkz6z%2FYePxUfJj0Lzaq1MkJec2FYzyZ5l1jq3uVxztjSTXSq6XZ4CooYLwu4vS1tkuYDnLPPIDDH0hoFysnflILcXy9fQNbHA0B6WG%2Fe8UGKPvyLGctSK98aBvSPzKCjOGtB%2BOAi8Sj3Fs75%2B%2Bf&X-Amz-Signature=eee63aaf05285fbccc9cb37f899453f4bbf0a6c43009314198b72f36fbcc4016&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGVL62U5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQDsWPUNseuv3KHL7k2KI0aQvZEPFK6JASBSc82xgViujAIgWOCNfvdTbDXPj22GSRbONlhc%2BO1JQfAaYtsdqRRh3nwq%2FwMIQhAAGgw2Mzc0MjMxODM4MDUiDGo9pe3KFQ2JfgixdSrcAyXxKVGxv67JQXURxtd2nI7d3qqLPC%2FegFaCZRiOGWJ7LGbbdtxF%2B29%2BbgTJuOKI%2FlWMhIyy2jNj4agKOmDaOSzu560tbenCsR69%2B4tepzzdh9Pmi2Ynn3b3NvIteNfVPF57wphGhwxwjlgGFEabElgjk9MP48QXWzEynaFptSpIK465Hm7F%2BsrxmLNrb7K%2BaxbrBVRKpHtBbs0JBn%2Fb%2B8cXW7GET6vk3NA1Uv6ravB%2FyIFHHmnbYpndFVD%2BlBh0CdhY%2FqXNf3voek68TPE2ar4OyKj6gp06WzdfUlISDCwtyC1SUwehiaL%2FRY7R9wHh55hHueXty1WaIpg6e49JFbYmlZv02qBZziAzi65s0aqImfEdomCJcULGSKoSts%2BM4gQRqf8Kq7uT4XJOVa4ZAahcgWU%2FU%2Fv6vm0SLBeKay9jkvuXUw%2Bm9nt68EsG6tQRTxxzEsjYE2TgZYb%2FX1wVeNyT22yUcXoRExEDw53yFxaCyb%2FnMkvbpgvxY27tLb2RilurI3Cip%2B04X5GVESUckH%2BILJCrXp1PslD6c5SrAOHQxBrs%2BJJm9%2Fc7RvVjmv9ez0a20QnGvDzanYeydAnvepDfnjFAGTgio347aWQYOLqjwwuB6b61jNElkarXMLzPjL0GOqUBbR1ZGJ%2F5UB9H7OXekXf6LV83XnFv4LeXc4yGRF%2FjUA%2FMswo7UgDV3T7B5EyZosuDRqkV4cBx2Tkz6z%2FYePxUfJj0Lzaq1MkJec2FYzyZ5l1jq3uVxztjSTXSq6XZ4CooYLwu4vS1tkuYDnLPPIDDH0hoFysnflILcXy9fQNbHA0B6WG%2Fe8UGKPvyLGctSK98aBvSPzKCjOGtB%2BOAi8Sj3Fs75%2B%2Bf&X-Amz-Signature=9464411131e428c1f089762b8645c76cf312c6efea8e1a45dec8bd2f8ec204b9&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
