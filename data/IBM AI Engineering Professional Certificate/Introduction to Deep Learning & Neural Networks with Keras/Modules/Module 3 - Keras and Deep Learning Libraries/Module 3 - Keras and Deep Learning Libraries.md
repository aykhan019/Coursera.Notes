

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74e41980-5708-4dc2-8b36-6fa847d6b94d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666UGJCO6Y%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122622Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJIMEYCIQCnJ%2FQCZ4WibUgPmRgXTLQ7Ock%2FU24bKDYLkKH0TqTuZAIhAPq%2FDHrLa7wcOMklHVnYpI4cOuPhZAG3zS6%2B88%2Fa9mDoKogECI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz35PsDyJH0a662NCkq3APqaFHFM0rcxLpgOTt4Xaf10kkv0WLBps4Y3nMW5vFrgUMN3nwzbbaHVeopxdqxlX%2FlTh%2FY8Ep1g9FLh0JuH1y77jOppx4v1RBDmhzS1mOdPpTTuasqEmaKeUZ%2FVL31HnvSnVezkhae2DQpxj%2Fi2EA8X6qRBE%2Ba7h%2FpLAscDTRSIyWwRXEbiXU5bf9jJh%2Bg4%2B86xrDk2MOTC6YnU2%2B%2BPmgBZpN6HuLiKHRsSyqduLXN9AAF3rznDsBNxQGt%2FRrUdCvbSUZTZp2jDC2AOpW8KeK16Zlmy2%2BybL1EiY8utuUbR0Ku044hiCrH6%2Bj3BZOM7IGOkdDIwJfSeozmvc4Q78LGCaIzQmjw%2F8gIhi6yc3zeaFdCfPXn5FB%2BOr9n2kg54xykWdowfSBoIgm%2FVPubIBt9H3PykNEBCxW94kTtElEmWxBepxu2We2fyUsBukhYaY2sj5gWHSiLyaAIynBRSWdgLWgRzoSQ76Or9wzcIz%2FUoUfs8r9T97Yvk9xHX9vKwBwGfV3aG%2FL2NEm4Q7wx%2Bz0jHBKsqRbmpoachFQl2CbsYD6gpxoX5Ny7h9OrgucLymAhsJOqVs%2FsicpsK2cn4hr8kz%2FrrD3OGK3LlTbZeFkDxlguV1JOL1hLxuFGPDCMhZ29BjqkAeGNOt7qqQWDwSkF6UvquwV3D1Ql2FPJYwH2STN1K91FRSyw6BRAe73VL6%2BQaBT06eF19ACQOpG7O8CSKAi7eKICHHm%2FNz1D3jTV4STw36K0sCz5G6wohS9f4Li8X89mjc0kcSEpWfoNhXj1Yj3eSzdcUak2kfs9c%2FnQcowvtZ%2B91Pd76W83ul16Ou1ynNfMbkFIaHYYKy%2Fgu2gvzkpv1bOaGX5o&X-Amz-Signature=6b26b7410b43ca81cbd27c694d79368fb660627be722bd110f95dda500f1e43c&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. PyTorch
#### Description
PyTorch, developed by Facebook in 2016, has gained popularity in academic and research settings. It emphasizes flexibility and dynamic computation graphs, making it ideal for applications requiring custom deep learning models. PyTorch is a cousin of the Lua-Based Torch Framework, and is a strong competitor  
#### Features
- Dynamic computational graph
- Strong academic presence
- Easier debugging and optimization
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f420ac7a-3545-4ca4-807d-b1f088e34f6b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666UGJCO6Y%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122622Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJIMEYCIQCnJ%2FQCZ4WibUgPmRgXTLQ7Ock%2FU24bKDYLkKH0TqTuZAIhAPq%2FDHrLa7wcOMklHVnYpI4cOuPhZAG3zS6%2B88%2Fa9mDoKogECI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz35PsDyJH0a662NCkq3APqaFHFM0rcxLpgOTt4Xaf10kkv0WLBps4Y3nMW5vFrgUMN3nwzbbaHVeopxdqxlX%2FlTh%2FY8Ep1g9FLh0JuH1y77jOppx4v1RBDmhzS1mOdPpTTuasqEmaKeUZ%2FVL31HnvSnVezkhae2DQpxj%2Fi2EA8X6qRBE%2Ba7h%2FpLAscDTRSIyWwRXEbiXU5bf9jJh%2Bg4%2B86xrDk2MOTC6YnU2%2B%2BPmgBZpN6HuLiKHRsSyqduLXN9AAF3rznDsBNxQGt%2FRrUdCvbSUZTZp2jDC2AOpW8KeK16Zlmy2%2BybL1EiY8utuUbR0Ku044hiCrH6%2Bj3BZOM7IGOkdDIwJfSeozmvc4Q78LGCaIzQmjw%2F8gIhi6yc3zeaFdCfPXn5FB%2BOr9n2kg54xykWdowfSBoIgm%2FVPubIBt9H3PykNEBCxW94kTtElEmWxBepxu2We2fyUsBukhYaY2sj5gWHSiLyaAIynBRSWdgLWgRzoSQ76Or9wzcIz%2FUoUfs8r9T97Yvk9xHX9vKwBwGfV3aG%2FL2NEm4Q7wx%2Bz0jHBKsqRbmpoachFQl2CbsYD6gpxoX5Ny7h9OrgucLymAhsJOqVs%2FsicpsK2cn4hr8kz%2FrrD3OGK3LlTbZeFkDxlguV1JOL1hLxuFGPDCMhZ29BjqkAeGNOt7qqQWDwSkF6UvquwV3D1Ql2FPJYwH2STN1K91FRSyw6BRAe73VL6%2BQaBT06eF19ACQOpG7O8CSKAi7eKICHHm%2FNz1D3jTV4STw36K0sCz5G6wohS9f4Li8X89mjc0kcSEpWfoNhXj1Yj3eSzdcUak2kfs9c%2FnQcowvtZ%2B91Pd76W83ul16Ou1ynNfMbkFIaHYYKy%2Fgu2gvzkpv1bOaGX5o&X-Amz-Signature=e89390fea7de10c5738b33425376e822f7d250204d6b76278037318426eb3c04&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Keras
#### Description
Keras is a high-level API for building neural networks. It runs on top of TensorFlow and simplifies model building with a user-friendly interface, making it a great option for beginners and rapid prototyping.
#### Features
- Simplified syntax for rapid development
- Can run on top of TensorFlow or Theano
- User-friendly and easy to learn
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/18d63fa6-e71d-4007-b06a-fdde1fc12b03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666UGJCO6Y%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122622Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJIMEYCIQCnJ%2FQCZ4WibUgPmRgXTLQ7Ock%2FU24bKDYLkKH0TqTuZAIhAPq%2FDHrLa7wcOMklHVnYpI4cOuPhZAG3zS6%2B88%2Fa9mDoKogECI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz35PsDyJH0a662NCkq3APqaFHFM0rcxLpgOTt4Xaf10kkv0WLBps4Y3nMW5vFrgUMN3nwzbbaHVeopxdqxlX%2FlTh%2FY8Ep1g9FLh0JuH1y77jOppx4v1RBDmhzS1mOdPpTTuasqEmaKeUZ%2FVL31HnvSnVezkhae2DQpxj%2Fi2EA8X6qRBE%2Ba7h%2FpLAscDTRSIyWwRXEbiXU5bf9jJh%2Bg4%2B86xrDk2MOTC6YnU2%2B%2BPmgBZpN6HuLiKHRsSyqduLXN9AAF3rznDsBNxQGt%2FRrUdCvbSUZTZp2jDC2AOpW8KeK16Zlmy2%2BybL1EiY8utuUbR0Ku044hiCrH6%2Bj3BZOM7IGOkdDIwJfSeozmvc4Q78LGCaIzQmjw%2F8gIhi6yc3zeaFdCfPXn5FB%2BOr9n2kg54xykWdowfSBoIgm%2FVPubIBt9H3PykNEBCxW94kTtElEmWxBepxu2We2fyUsBukhYaY2sj5gWHSiLyaAIynBRSWdgLWgRzoSQ76Or9wzcIz%2FUoUfs8r9T97Yvk9xHX9vKwBwGfV3aG%2FL2NEm4Q7wx%2Bz0jHBKsqRbmpoachFQl2CbsYD6gpxoX5Ny7h9OrgucLymAhsJOqVs%2FsicpsK2cn4hr8kz%2FrrD3OGK3LlTbZeFkDxlguV1JOL1hLxuFGPDCMhZ29BjqkAeGNOt7qqQWDwSkF6UvquwV3D1Ql2FPJYwH2STN1K91FRSyw6BRAe73VL6%2BQaBT06eF19ACQOpG7O8CSKAi7eKICHHm%2FNz1D3jTV4STw36K0sCz5G6wohS9f4Li8X89mjc0kcSEpWfoNhXj1Yj3eSzdcUak2kfs9c%2FnQcowvtZ%2B91Pd76W83ul16Ou1ynNfMbkFIaHYYKy%2Fgu2gvzkpv1bOaGX5o&X-Amz-Signature=4ceff4b3e6375a962a04a57b56b47c55bfdb9ca2a2617de8c5b1f7c9527026d0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1307e63c-51d4-4bc0-954a-ff8ae7a3e2e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664H4ZJ757%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122623Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJIMEYCIQDka6%2B7%2FVUAF5yqbkD5KR%2BUjx%2Bq3%2BNgcs%2FmvGre%2Bj4T2AIhAKofwQ3jEJt28JNMYdROoWDcCaWPgzM7RDLTFotJjo%2F5KogECI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzlqx%2FUTxxtWAofBUAq3AP43qZBxct4qN2cARxpQKTssSM7KrNhJH8uG402iB5peh6IaKfCuyge68pJvkXA0xnoxCP3J3Lsr8M7Gd%2BoXALYeHr%2FGjVFgRLx1wTXMjOz6PT5XC%2FzU1mMz5MCnquOfIuhMe6B0YRQyUPkRluFpmXzKwoG33uhNmMMb%2Bo9edSg2VuHi9BUPx%2BuAN2fGOETQ4OuvenXcVf%2F1ewBHIdHYoXsSTsbYj2cbJPL2i3fk4GueUIAqjsoXlEmSM3%2FsdB0tOkm4qXyVlkFBhJgstlp2MfPo1aNP6F%2FLebaL2oR%2FxfmwtxSu2oyD%2BtSnRqL4G1M8PaCyXcA0QhJ7Ni882VKbb3w47xbrrQofVhjiRRBPbP0w%2FgPyg0QkyDx8BwD46t3qv%2Bb3%2BDIa3QymEBxZlBxGiIX4vQuwtYndcRyp85DaPoOCaHFb5ysouudWxrfJOKseTiPVNH6zhu0tBYxfYeU%2F2MlhOoczBcX4NQ6WHgrywma1VUpzjNjYb9N2wRFXtTC2L%2BKUeWcoQkUaipc614Fyh7E%2BFKj0yNfE129fRZ2EQUwZbIpmhY%2Bc0ZT4zvPutHgG3X82guem1kacdOchfMCsxgLc4D8erMBTXVSzBa17o2uMvHE%2FZxYW9zLsoSQbjDNhZ29BjqkAdAeOM4fSa5ne5t9L78emwMhvssdyvTSfcm69RJqQ8cQLXrNaQI%2F64YiQPrKkN7wSTqEaxaseaRwBSJqjA9sZuW6IbTSrib2SCyOlmxQ2%2BLexpGL0tZnM9%2BK19CS8AMplsjWetvYi1s5MQO0DjlQxIZigJKlYEJZDBdQDcOH7kqazV%2Bk%2Fc%2FlaPZOax10fwqw%2FTbYSBZgQHMJP4zyHMpEqoJDxxNd&X-Amz-Signature=485cd184093b303a50430ed0a940f53a9267820a9e555a165f4da8f12acb5e98&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e6193001-64de-41d3-8624-a8f8d5f99f66/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQSVMERN%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122623Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIGIcGdbi1d8sHrvrsDJjuJsOiZElVb1WcEUJ%2Fceqxf5yAiEA2CLx%2BesWWwVtNvFrmnIUjdm7m6kRhYduV32PtNZT1VoqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHbykhheYzZY6KXnkCrcA%2FbF1jdtM2XJ73AhTq2TGZrfGFlxe7KeHPn23pJAkDAPFPbQWJmblYfB3RK%2BSlp3JZ0uT2suwtNLFxbsS8WJibQYAFvHs1rlsBOJpPwL6OlGpZZjRsJGFCxHvz9Y8hB0wzT%2B%2F7Rwg1YDVMzPDZR3NY%2BAkFDU2j8JuYHC3Jws6WJTyW6DHAq5wWSsX5cMgHK9Zr5Qp%2BVw6IZ6fVcJjY%2B2jmIrRuUeQZ01umkz4jHNTQU%2FXqsJdgljN6bIcIWTrVMm1DSHXhrmyO49xXQvvAfEsQ0Sk%2FTL1uFXDBLp48MG7JtYaAmc7kKx5NlrY0brTBQEelKz5YXSlbAnhcLbfJ4th0fTOdPjtkzom9zVfzwCSY4ZnT8oJ6Z0x1mkgk2PuW4j757VnH9vQpC%2FztYAiOO9qX%2BPBMtd4uK0OJ%2BlHdcNDOuOEohT9tZZ0hLTF0o%2BPOCnywC5EOB8Aafqizn%2BR9Ycz4H%2F1X0YyBcpgwLDWlQR322ikXPmCM3LYbusAk33FO%2F1HO2G45jx%2BzvchIM32jnrohYX39poJqfz6m8Cx1jcRh7al8wI3Ng11NDMGMFT%2B4va%2BDAHhfQbZawgltAD2%2BzuUXMEeyLAN%2FUBIh%2BqAdmCzbaYD0Au6ry2rN7lliWNMLWFnb0GOqUBAqn84Fp8qEqp7RDCU7VFO%2BkPXWDCn9HaHsAwrfTDuQjmM0nPCB4GqkcMCZHV7uXeNpj1meBcpAD1Wo0EbnSlQ2PbfPhIqnIjpJY2xiMj%2FbuUjbsaArqqr4zULDMyYN4CoG7A0h3o54v6UhwQpKHBE2QdcR1M8hUT2sFUzwCni8INvs8xA7UTXY9k8IqiTvpNDqg7iY%2FwwOMcg21yo51mBUh2bhwb&X-Amz-Signature=4a30db5937271b5f40ae35b04d9c420c96137f15dbebf7bbf90efce64228f791&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/eac113a6-c35b-46e8-a33e-827216ab294a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666UGJCO6Y%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122622Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJIMEYCIQCnJ%2FQCZ4WibUgPmRgXTLQ7Ock%2FU24bKDYLkKH0TqTuZAIhAPq%2FDHrLa7wcOMklHVnYpI4cOuPhZAG3zS6%2B88%2Fa9mDoKogECI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz35PsDyJH0a662NCkq3APqaFHFM0rcxLpgOTt4Xaf10kkv0WLBps4Y3nMW5vFrgUMN3nwzbbaHVeopxdqxlX%2FlTh%2FY8Ep1g9FLh0JuH1y77jOppx4v1RBDmhzS1mOdPpTTuasqEmaKeUZ%2FVL31HnvSnVezkhae2DQpxj%2Fi2EA8X6qRBE%2Ba7h%2FpLAscDTRSIyWwRXEbiXU5bf9jJh%2Bg4%2B86xrDk2MOTC6YnU2%2B%2BPmgBZpN6HuLiKHRsSyqduLXN9AAF3rznDsBNxQGt%2FRrUdCvbSUZTZp2jDC2AOpW8KeK16Zlmy2%2BybL1EiY8utuUbR0Ku044hiCrH6%2Bj3BZOM7IGOkdDIwJfSeozmvc4Q78LGCaIzQmjw%2F8gIhi6yc3zeaFdCfPXn5FB%2BOr9n2kg54xykWdowfSBoIgm%2FVPubIBt9H3PykNEBCxW94kTtElEmWxBepxu2We2fyUsBukhYaY2sj5gWHSiLyaAIynBRSWdgLWgRzoSQ76Or9wzcIz%2FUoUfs8r9T97Yvk9xHX9vKwBwGfV3aG%2FL2NEm4Q7wx%2Bz0jHBKsqRbmpoachFQl2CbsYD6gpxoX5Ny7h9OrgucLymAhsJOqVs%2FsicpsK2cn4hr8kz%2FrrD3OGK3LlTbZeFkDxlguV1JOL1hLxuFGPDCMhZ29BjqkAeGNOt7qqQWDwSkF6UvquwV3D1Ql2FPJYwH2STN1K91FRSyw6BRAe73VL6%2BQaBT06eF19ACQOpG7O8CSKAi7eKICHHm%2FNz1D3jTV4STw36K0sCz5G6wohS9f4Li8X89mjc0kcSEpWfoNhXj1Yj3eSzdcUak2kfs9c%2FnQcowvtZ%2B91Pd76W83ul16Ou1ynNfMbkFIaHYYKy%2Fgu2gvzkpv1bOaGX5o&X-Amz-Signature=aa8531714dc383fb352c36ee47f00845401502080058327e1195153cf2fd2b6c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b1126cec-3993-4fb3-82c4-d7f67fbc1e81/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666UGJCO6Y%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122622Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJIMEYCIQCnJ%2FQCZ4WibUgPmRgXTLQ7Ock%2FU24bKDYLkKH0TqTuZAIhAPq%2FDHrLa7wcOMklHVnYpI4cOuPhZAG3zS6%2B88%2Fa9mDoKogECI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz35PsDyJH0a662NCkq3APqaFHFM0rcxLpgOTt4Xaf10kkv0WLBps4Y3nMW5vFrgUMN3nwzbbaHVeopxdqxlX%2FlTh%2FY8Ep1g9FLh0JuH1y77jOppx4v1RBDmhzS1mOdPpTTuasqEmaKeUZ%2FVL31HnvSnVezkhae2DQpxj%2Fi2EA8X6qRBE%2Ba7h%2FpLAscDTRSIyWwRXEbiXU5bf9jJh%2Bg4%2B86xrDk2MOTC6YnU2%2B%2BPmgBZpN6HuLiKHRsSyqduLXN9AAF3rznDsBNxQGt%2FRrUdCvbSUZTZp2jDC2AOpW8KeK16Zlmy2%2BybL1EiY8utuUbR0Ku044hiCrH6%2Bj3BZOM7IGOkdDIwJfSeozmvc4Q78LGCaIzQmjw%2F8gIhi6yc3zeaFdCfPXn5FB%2BOr9n2kg54xykWdowfSBoIgm%2FVPubIBt9H3PykNEBCxW94kTtElEmWxBepxu2We2fyUsBukhYaY2sj5gWHSiLyaAIynBRSWdgLWgRzoSQ76Or9wzcIz%2FUoUfs8r9T97Yvk9xHX9vKwBwGfV3aG%2FL2NEm4Q7wx%2Bz0jHBKsqRbmpoachFQl2CbsYD6gpxoX5Ny7h9OrgucLymAhsJOqVs%2FsicpsK2cn4hr8kz%2FrrD3OGK3LlTbZeFkDxlguV1JOL1hLxuFGPDCMhZ29BjqkAeGNOt7qqQWDwSkF6UvquwV3D1Ql2FPJYwH2STN1K91FRSyw6BRAe73VL6%2BQaBT06eF19ACQOpG7O8CSKAi7eKICHHm%2FNz1D3jTV4STw36K0sCz5G6wohS9f4Li8X89mjc0kcSEpWfoNhXj1Yj3eSzdcUak2kfs9c%2FnQcowvtZ%2B91Pd76W83ul16Ou1ynNfMbkFIaHYYKy%2Fgu2gvzkpv1bOaGX5o&X-Amz-Signature=398f75510c836074679365aeff746ea284628970086bd6a337920762b5637def&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8e3957d0-609f-4d84-a6b2-bd48b5c3562e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666UGJCO6Y%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122622Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJIMEYCIQCnJ%2FQCZ4WibUgPmRgXTLQ7Ock%2FU24bKDYLkKH0TqTuZAIhAPq%2FDHrLa7wcOMklHVnYpI4cOuPhZAG3zS6%2B88%2Fa9mDoKogECI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz35PsDyJH0a662NCkq3APqaFHFM0rcxLpgOTt4Xaf10kkv0WLBps4Y3nMW5vFrgUMN3nwzbbaHVeopxdqxlX%2FlTh%2FY8Ep1g9FLh0JuH1y77jOppx4v1RBDmhzS1mOdPpTTuasqEmaKeUZ%2FVL31HnvSnVezkhae2DQpxj%2Fi2EA8X6qRBE%2Ba7h%2FpLAscDTRSIyWwRXEbiXU5bf9jJh%2Bg4%2B86xrDk2MOTC6YnU2%2B%2BPmgBZpN6HuLiKHRsSyqduLXN9AAF3rznDsBNxQGt%2FRrUdCvbSUZTZp2jDC2AOpW8KeK16Zlmy2%2BybL1EiY8utuUbR0Ku044hiCrH6%2Bj3BZOM7IGOkdDIwJfSeozmvc4Q78LGCaIzQmjw%2F8gIhi6yc3zeaFdCfPXn5FB%2BOr9n2kg54xykWdowfSBoIgm%2FVPubIBt9H3PykNEBCxW94kTtElEmWxBepxu2We2fyUsBukhYaY2sj5gWHSiLyaAIynBRSWdgLWgRzoSQ76Or9wzcIz%2FUoUfs8r9T97Yvk9xHX9vKwBwGfV3aG%2FL2NEm4Q7wx%2Bz0jHBKsqRbmpoachFQl2CbsYD6gpxoX5Ny7h9OrgucLymAhsJOqVs%2FsicpsK2cn4hr8kz%2FrrD3OGK3LlTbZeFkDxlguV1JOL1hLxuFGPDCMhZ29BjqkAeGNOt7qqQWDwSkF6UvquwV3D1Ql2FPJYwH2STN1K91FRSyw6BRAe73VL6%2BQaBT06eF19ACQOpG7O8CSKAi7eKICHHm%2FNz1D3jTV4STw36K0sCz5G6wohS9f4Li8X89mjc0kcSEpWfoNhXj1Yj3eSzdcUak2kfs9c%2FnQcowvtZ%2B91Pd76W83ul16Ou1ynNfMbkFIaHYYKy%2Fgu2gvzkpv1bOaGX5o&X-Amz-Signature=30f267fb31d048d1863e0275a1d65d7a2f136a10b1526504ed082f2569a24bad&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b9a0b3fa-70ea-45e5-9593-7351d697026d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666UGJCO6Y%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122622Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJIMEYCIQCnJ%2FQCZ4WibUgPmRgXTLQ7Ock%2FU24bKDYLkKH0TqTuZAIhAPq%2FDHrLa7wcOMklHVnYpI4cOuPhZAG3zS6%2B88%2Fa9mDoKogECI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz35PsDyJH0a662NCkq3APqaFHFM0rcxLpgOTt4Xaf10kkv0WLBps4Y3nMW5vFrgUMN3nwzbbaHVeopxdqxlX%2FlTh%2FY8Ep1g9FLh0JuH1y77jOppx4v1RBDmhzS1mOdPpTTuasqEmaKeUZ%2FVL31HnvSnVezkhae2DQpxj%2Fi2EA8X6qRBE%2Ba7h%2FpLAscDTRSIyWwRXEbiXU5bf9jJh%2Bg4%2B86xrDk2MOTC6YnU2%2B%2BPmgBZpN6HuLiKHRsSyqduLXN9AAF3rznDsBNxQGt%2FRrUdCvbSUZTZp2jDC2AOpW8KeK16Zlmy2%2BybL1EiY8utuUbR0Ku044hiCrH6%2Bj3BZOM7IGOkdDIwJfSeozmvc4Q78LGCaIzQmjw%2F8gIhi6yc3zeaFdCfPXn5FB%2BOr9n2kg54xykWdowfSBoIgm%2FVPubIBt9H3PykNEBCxW94kTtElEmWxBepxu2We2fyUsBukhYaY2sj5gWHSiLyaAIynBRSWdgLWgRzoSQ76Or9wzcIz%2FUoUfs8r9T97Yvk9xHX9vKwBwGfV3aG%2FL2NEm4Q7wx%2Bz0jHBKsqRbmpoachFQl2CbsYD6gpxoX5Ny7h9OrgucLymAhsJOqVs%2FsicpsK2cn4hr8kz%2FrrD3OGK3LlTbZeFkDxlguV1JOL1hLxuFGPDCMhZ29BjqkAeGNOt7qqQWDwSkF6UvquwV3D1Ql2FPJYwH2STN1K91FRSyw6BRAe73VL6%2BQaBT06eF19ACQOpG7O8CSKAi7eKICHHm%2FNz1D3jTV4STw36K0sCz5G6wohS9f4Li8X89mjc0kcSEpWfoNhXj1Yj3eSzdcUak2kfs9c%2FnQcowvtZ%2B91Pd76W83ul16Ou1ynNfMbkFIaHYYKy%2Fgu2gvzkpv1bOaGX5o&X-Amz-Signature=e52807a97f7bca48a95178faa92e1f45fc3725588d45f8bed5991256e50526ee&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Conclusion**
Keras provides a straightforward approach to building and training classification models. For classification tasks, the model architecture and training process are similar to those used for regression, with the key differences being the activation functions and loss functions used. For more detailed information, refer to the Keras documentation on optimizers, models, and methods.
___
