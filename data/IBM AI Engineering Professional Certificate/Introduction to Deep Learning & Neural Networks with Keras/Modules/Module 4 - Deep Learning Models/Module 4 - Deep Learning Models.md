

# Module 4: Deep Learning Models
## Deep Neural Networks: An Introduction
### Overview
Neural networks have evolved significantly over time, transitioning from shallow networks to deep neural networks (DNNs) that handle complex tasks and data types. This note explores the distinctions between shallow and deep neural networks, and the reasons behind the recent advancements in deep learning.
### Shallow vs. Deep Neural Networks
#### Shallow Neural Networks
- **Definition**: A shallow neural network typically has only one hidden layer.
- **Characteristics**:
	- Simpler architectures
	- Limited ability to extract features from raw data
	- Often used for simpler tasks or as building blocks for deeper networks
#### Deep Neural Networks
- **Definition**: A deep neural network has multiple hidden layers and neurons.
- **Characteristics**:
	- Capable of learning hierarchical features from raw data such as images and text
	- Ability to extract features from raw data.
	- Handles more complex tasks and datasets
	- Example: Image recognition, natural language processing
### Factors Contributing to the Rise of Deep Learning
#### 1. Advancements in Neural Network Techniques
- **ReLU Activation Function**:
	- Addressed the vanishing gradient problem
	- Enabled the training of very deep networks
#### 2. Availability of Data
- **Importance**:
	- Deep neural networks excel with large datasets
	- Large data helps prevent overfitting
- **Current Trends**:
	- Access to vast amounts of data has become easier
	- Deep learning algorithms benefit significantly from increased data
#### 3. Computational Power
- **GPU Utilization**:
	- NVIDIA GPUs and other high-performance computing resources
	- Reduced training times from weeks to hours
- **Impact**:
	- Enables experimentation with different network architectures and prototypes in shorter periods
### Conclusion
The combination of advancements in neural network techniques, the availability of large datasets, and increased computational power has driven the recent boom in deep learning. The field continues to evolve, with deep neural networks becoming increasingly prevalent in various applications. Upcoming topics will delve into supervised deep learning algorithms and convolutional neural networks (CNNs).
___
## Introduction to Convolutional Neural Networks (CNNs) (Supervised Deep Learning Model)
### Overview
Convolutional Neural Networks (CNNs) are a specialized type of neural network designed for processing structured grid data such as images. This note covers the fundamental architecture of CNNs, their operational mechanisms, and how to build them using the Keras library.
#### Convolutional Neural Networks (CNNs)
### Architecture
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZGKEHYKE%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T122856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJGMEQCIH8TvZu2qGBpNfxsT9UpWhzFkmCJqU8cYF1UkCVMqIlYAiBQPGGpLrHrg9cMUnluXfuQsBP7Sb1piL5w3dYj1Y3RKSr%2FAwh1EAAaDDYzNzQyMzE4MzgwNSIMwrNF4yFpGXghHFJdKtwD96i1bVwQ5Oxd0WO65AyF24%2FRRunQ8ZnN69HDaLZqp3JWbAny2jNcU4tHFiOLSjHfLLLCky6dOkjwjo8eKpHSQB4%2BeQ6EvbZq8BUcwFJcNPUHLjQpZqUMHbJ6iM7eh2JoD5Qgh3%2BYCbpqaN1PRynfvGcShJMJRTJtFTJxcMAT4%2BWKgZNPbKd033y24zRMjqfZzYq6OIIrkZKLknuhROZntHHq1pGBYvQpFjOpj7GF%2FH2H5a4HYy24i4lCmkyr3tWfKfjSbDz1MWxfZa%2F2Dr2c%2FQ28pwhdc2iz%2FJ0ckwCJJl1PhA6QuLT6Rdz4LJARHwLtwktoUriF5DR1jUvYMKJnQasdCKi8306mkk7gO6v9uN2XRanRQt5Js0wurPbbrielb6pi1XQNKy56F%2Fdu%2FYbHRdYdUawCTmNwpSJws3P5akvllXaUQfch%2Bd%2F92%2B7EvLNznor4lzSl2X3pPUitVUACAXaLuUDWZoilJ%2BXPzbXlxMtdsMwpp4jZnEXE1qc2RP9oxeqaATKDUA8Q7CvUIW31ZP1%2FdvGefj2INUSjUOoxEJ90FElzuAUJlc80oxOsZ4aQ99Rsfh1Qhi5%2B07ePpmjzRnO1ELN2%2F%2BhjeYMq29pf9OdR2Pnwdr9jafpGuu8wofCXvQY6pgH1GsNDgA2zB%2FiT5sDoy8AQlcOJSXTpPAlGIKaFWD7ZiTd0pdg%2FbgbtnX5gNGsdK%2B6VpmvvkC8RhPmBhJgcNwiaKRq2abVvhirrkW9OZ8lK%2BILANVYK31qBf%2FqmCaTvC%2FwXnN6NboIBN5BX77%2F%2BeUaid3nTP2k8lIOAsAa2gF8GY2zWOOpqM1qEcRVf3NBJkAH8yhqiSEL9OmNsychzxfvklG9DyFCY&X-Amz-Signature=b21fafe4cc35e2da3ab0912284b13638ea577a868fd3d0a872ab21f7306079e1&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZGKEHYKE%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T122855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJGMEQCIH8TvZu2qGBpNfxsT9UpWhzFkmCJqU8cYF1UkCVMqIlYAiBQPGGpLrHrg9cMUnluXfuQsBP7Sb1piL5w3dYj1Y3RKSr%2FAwh1EAAaDDYzNzQyMzE4MzgwNSIMwrNF4yFpGXghHFJdKtwD96i1bVwQ5Oxd0WO65AyF24%2FRRunQ8ZnN69HDaLZqp3JWbAny2jNcU4tHFiOLSjHfLLLCky6dOkjwjo8eKpHSQB4%2BeQ6EvbZq8BUcwFJcNPUHLjQpZqUMHbJ6iM7eh2JoD5Qgh3%2BYCbpqaN1PRynfvGcShJMJRTJtFTJxcMAT4%2BWKgZNPbKd033y24zRMjqfZzYq6OIIrkZKLknuhROZntHHq1pGBYvQpFjOpj7GF%2FH2H5a4HYy24i4lCmkyr3tWfKfjSbDz1MWxfZa%2F2Dr2c%2FQ28pwhdc2iz%2FJ0ckwCJJl1PhA6QuLT6Rdz4LJARHwLtwktoUriF5DR1jUvYMKJnQasdCKi8306mkk7gO6v9uN2XRanRQt5Js0wurPbbrielb6pi1XQNKy56F%2Fdu%2FYbHRdYdUawCTmNwpSJws3P5akvllXaUQfch%2Bd%2F92%2B7EvLNznor4lzSl2X3pPUitVUACAXaLuUDWZoilJ%2BXPzbXlxMtdsMwpp4jZnEXE1qc2RP9oxeqaATKDUA8Q7CvUIW31ZP1%2FdvGefj2INUSjUOoxEJ90FElzuAUJlc80oxOsZ4aQ99Rsfh1Qhi5%2B07ePpmjzRnO1ELN2%2F%2BhjeYMq29pf9OdR2Pnwdr9jafpGuu8wofCXvQY6pgH1GsNDgA2zB%2FiT5sDoy8AQlcOJSXTpPAlGIKaFWD7ZiTd0pdg%2FbgbtnX5gNGsdK%2B6VpmvvkC8RhPmBhJgcNwiaKRq2abVvhirrkW9OZ8lK%2BILANVYK31qBf%2FqmCaTvC%2FwXnN6NboIBN5BX77%2F%2BeUaid3nTP2k8lIOAsAa2gF8GY2zWOOpqM1qEcRVf3NBJkAH8yhqiSEL9OmNsychzxfvklG9DyFCY&X-Amz-Signature=b1754d51f1ad432ef4986dc345a04152f9589ba4d214c0620a67580c7caef107&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZGKEHYKE%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T122855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJGMEQCIH8TvZu2qGBpNfxsT9UpWhzFkmCJqU8cYF1UkCVMqIlYAiBQPGGpLrHrg9cMUnluXfuQsBP7Sb1piL5w3dYj1Y3RKSr%2FAwh1EAAaDDYzNzQyMzE4MzgwNSIMwrNF4yFpGXghHFJdKtwD96i1bVwQ5Oxd0WO65AyF24%2FRRunQ8ZnN69HDaLZqp3JWbAny2jNcU4tHFiOLSjHfLLLCky6dOkjwjo8eKpHSQB4%2BeQ6EvbZq8BUcwFJcNPUHLjQpZqUMHbJ6iM7eh2JoD5Qgh3%2BYCbpqaN1PRynfvGcShJMJRTJtFTJxcMAT4%2BWKgZNPbKd033y24zRMjqfZzYq6OIIrkZKLknuhROZntHHq1pGBYvQpFjOpj7GF%2FH2H5a4HYy24i4lCmkyr3tWfKfjSbDz1MWxfZa%2F2Dr2c%2FQ28pwhdc2iz%2FJ0ckwCJJl1PhA6QuLT6Rdz4LJARHwLtwktoUriF5DR1jUvYMKJnQasdCKi8306mkk7gO6v9uN2XRanRQt5Js0wurPbbrielb6pi1XQNKy56F%2Fdu%2FYbHRdYdUawCTmNwpSJws3P5akvllXaUQfch%2Bd%2F92%2B7EvLNznor4lzSl2X3pPUitVUACAXaLuUDWZoilJ%2BXPzbXlxMtdsMwpp4jZnEXE1qc2RP9oxeqaATKDUA8Q7CvUIW31ZP1%2FdvGefj2INUSjUOoxEJ90FElzuAUJlc80oxOsZ4aQ99Rsfh1Qhi5%2B07ePpmjzRnO1ELN2%2F%2BhjeYMq29pf9OdR2Pnwdr9jafpGuu8wofCXvQY6pgH1GsNDgA2zB%2FiT5sDoy8AQlcOJSXTpPAlGIKaFWD7ZiTd0pdg%2FbgbtnX5gNGsdK%2B6VpmvvkC8RhPmBhJgcNwiaKRq2abVvhirrkW9OZ8lK%2BILANVYK31qBf%2FqmCaTvC%2FwXnN6NboIBN5BX77%2F%2BeUaid3nTP2k8lIOAsAa2gF8GY2zWOOpqM1qEcRVf3NBJkAH8yhqiSEL9OmNsychzxfvklG9DyFCY&X-Amz-Signature=11f4f2ac991563ae70e4933fc0c23abc82d242e1727c328dcfd1f399cb81c6ab&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZGKEHYKE%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T122856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJGMEQCIH8TvZu2qGBpNfxsT9UpWhzFkmCJqU8cYF1UkCVMqIlYAiBQPGGpLrHrg9cMUnluXfuQsBP7Sb1piL5w3dYj1Y3RKSr%2FAwh1EAAaDDYzNzQyMzE4MzgwNSIMwrNF4yFpGXghHFJdKtwD96i1bVwQ5Oxd0WO65AyF24%2FRRunQ8ZnN69HDaLZqp3JWbAny2jNcU4tHFiOLSjHfLLLCky6dOkjwjo8eKpHSQB4%2BeQ6EvbZq8BUcwFJcNPUHLjQpZqUMHbJ6iM7eh2JoD5Qgh3%2BYCbpqaN1PRynfvGcShJMJRTJtFTJxcMAT4%2BWKgZNPbKd033y24zRMjqfZzYq6OIIrkZKLknuhROZntHHq1pGBYvQpFjOpj7GF%2FH2H5a4HYy24i4lCmkyr3tWfKfjSbDz1MWxfZa%2F2Dr2c%2FQ28pwhdc2iz%2FJ0ckwCJJl1PhA6QuLT6Rdz4LJARHwLtwktoUriF5DR1jUvYMKJnQasdCKi8306mkk7gO6v9uN2XRanRQt5Js0wurPbbrielb6pi1XQNKy56F%2Fdu%2FYbHRdYdUawCTmNwpSJws3P5akvllXaUQfch%2Bd%2F92%2B7EvLNznor4lzSl2X3pPUitVUACAXaLuUDWZoilJ%2BXPzbXlxMtdsMwpp4jZnEXE1qc2RP9oxeqaATKDUA8Q7CvUIW31ZP1%2FdvGefj2INUSjUOoxEJ90FElzuAUJlc80oxOsZ4aQ99Rsfh1Qhi5%2B07ePpmjzRnO1ELN2%2F%2BhjeYMq29pf9OdR2Pnwdr9jafpGuu8wofCXvQY6pgH1GsNDgA2zB%2FiT5sDoy8AQlcOJSXTpPAlGIKaFWD7ZiTd0pdg%2FbgbtnX5gNGsdK%2B6VpmvvkC8RhPmBhJgcNwiaKRq2abVvhirrkW9OZ8lK%2BILANVYK31qBf%2FqmCaTvC%2FwXnN6NboIBN5BX77%2F%2BeUaid3nTP2k8lIOAsAa2gF8GY2zWOOpqM1qEcRVf3NBJkAH8yhqiSEL9OmNsychzxfvklG9DyFCY&X-Amz-Signature=3f492ea9c05998fc8ec47ade905bff8d0f65457982b0085a808baa39d450190f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZGKEHYKE%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T122855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJGMEQCIH8TvZu2qGBpNfxsT9UpWhzFkmCJqU8cYF1UkCVMqIlYAiBQPGGpLrHrg9cMUnluXfuQsBP7Sb1piL5w3dYj1Y3RKSr%2FAwh1EAAaDDYzNzQyMzE4MzgwNSIMwrNF4yFpGXghHFJdKtwD96i1bVwQ5Oxd0WO65AyF24%2FRRunQ8ZnN69HDaLZqp3JWbAny2jNcU4tHFiOLSjHfLLLCky6dOkjwjo8eKpHSQB4%2BeQ6EvbZq8BUcwFJcNPUHLjQpZqUMHbJ6iM7eh2JoD5Qgh3%2BYCbpqaN1PRynfvGcShJMJRTJtFTJxcMAT4%2BWKgZNPbKd033y24zRMjqfZzYq6OIIrkZKLknuhROZntHHq1pGBYvQpFjOpj7GF%2FH2H5a4HYy24i4lCmkyr3tWfKfjSbDz1MWxfZa%2F2Dr2c%2FQ28pwhdc2iz%2FJ0ckwCJJl1PhA6QuLT6Rdz4LJARHwLtwktoUriF5DR1jUvYMKJnQasdCKi8306mkk7gO6v9uN2XRanRQt5Js0wurPbbrielb6pi1XQNKy56F%2Fdu%2FYbHRdYdUawCTmNwpSJws3P5akvllXaUQfch%2Bd%2F92%2B7EvLNznor4lzSl2X3pPUitVUACAXaLuUDWZoilJ%2BXPzbXlxMtdsMwpp4jZnEXE1qc2RP9oxeqaATKDUA8Q7CvUIW31ZP1%2FdvGefj2INUSjUOoxEJ90FElzuAUJlc80oxOsZ4aQ99Rsfh1Qhi5%2B07ePpmjzRnO1ELN2%2F%2BhjeYMq29pf9OdR2Pnwdr9jafpGuu8wofCXvQY6pgH1GsNDgA2zB%2FiT5sDoy8AQlcOJSXTpPAlGIKaFWD7ZiTd0pdg%2FbgbtnX5gNGsdK%2B6VpmvvkC8RhPmBhJgcNwiaKRq2abVvhirrkW9OZ8lK%2BILANVYK31qBf%2FqmCaTvC%2FwXnN6NboIBN5BX77%2F%2BeUaid3nTP2k8lIOAsAa2gF8GY2zWOOpqM1qEcRVf3NBJkAH8yhqiSEL9OmNsychzxfvklG9DyFCY&X-Amz-Signature=5421cf6d53b3af07d61462ee562341c8278466f09680614bd78f5e3fcac9369c&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZGKEHYKE%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T122855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJGMEQCIH8TvZu2qGBpNfxsT9UpWhzFkmCJqU8cYF1UkCVMqIlYAiBQPGGpLrHrg9cMUnluXfuQsBP7Sb1piL5w3dYj1Y3RKSr%2FAwh1EAAaDDYzNzQyMzE4MzgwNSIMwrNF4yFpGXghHFJdKtwD96i1bVwQ5Oxd0WO65AyF24%2FRRunQ8ZnN69HDaLZqp3JWbAny2jNcU4tHFiOLSjHfLLLCky6dOkjwjo8eKpHSQB4%2BeQ6EvbZq8BUcwFJcNPUHLjQpZqUMHbJ6iM7eh2JoD5Qgh3%2BYCbpqaN1PRynfvGcShJMJRTJtFTJxcMAT4%2BWKgZNPbKd033y24zRMjqfZzYq6OIIrkZKLknuhROZntHHq1pGBYvQpFjOpj7GF%2FH2H5a4HYy24i4lCmkyr3tWfKfjSbDz1MWxfZa%2F2Dr2c%2FQ28pwhdc2iz%2FJ0ckwCJJl1PhA6QuLT6Rdz4LJARHwLtwktoUriF5DR1jUvYMKJnQasdCKi8306mkk7gO6v9uN2XRanRQt5Js0wurPbbrielb6pi1XQNKy56F%2Fdu%2FYbHRdYdUawCTmNwpSJws3P5akvllXaUQfch%2Bd%2F92%2B7EvLNznor4lzSl2X3pPUitVUACAXaLuUDWZoilJ%2BXPzbXlxMtdsMwpp4jZnEXE1qc2RP9oxeqaATKDUA8Q7CvUIW31ZP1%2FdvGefj2INUSjUOoxEJ90FElzuAUJlc80oxOsZ4aQ99Rsfh1Qhi5%2B07ePpmjzRnO1ELN2%2F%2BhjeYMq29pf9OdR2Pnwdr9jafpGuu8wofCXvQY6pgH1GsNDgA2zB%2FiT5sDoy8AQlcOJSXTpPAlGIKaFWD7ZiTd0pdg%2FbgbtnX5gNGsdK%2B6VpmvvkC8RhPmBhJgcNwiaKRq2abVvhirrkW9OZ8lK%2BILANVYK31qBf%2FqmCaTvC%2FwXnN6NboIBN5BX77%2F%2BeUaid3nTP2k8lIOAsAa2gF8GY2zWOOpqM1qEcRVf3NBJkAH8yhqiSEL9OmNsychzxfvklG9DyFCY&X-Amz-Signature=7695a09f68d5cdbcefe8b7273dff3f49adee9e5edd38d3cd734b9e8e0504714d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZGKEHYKE%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T122856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJGMEQCIH8TvZu2qGBpNfxsT9UpWhzFkmCJqU8cYF1UkCVMqIlYAiBQPGGpLrHrg9cMUnluXfuQsBP7Sb1piL5w3dYj1Y3RKSr%2FAwh1EAAaDDYzNzQyMzE4MzgwNSIMwrNF4yFpGXghHFJdKtwD96i1bVwQ5Oxd0WO65AyF24%2FRRunQ8ZnN69HDaLZqp3JWbAny2jNcU4tHFiOLSjHfLLLCky6dOkjwjo8eKpHSQB4%2BeQ6EvbZq8BUcwFJcNPUHLjQpZqUMHbJ6iM7eh2JoD5Qgh3%2BYCbpqaN1PRynfvGcShJMJRTJtFTJxcMAT4%2BWKgZNPbKd033y24zRMjqfZzYq6OIIrkZKLknuhROZntHHq1pGBYvQpFjOpj7GF%2FH2H5a4HYy24i4lCmkyr3tWfKfjSbDz1MWxfZa%2F2Dr2c%2FQ28pwhdc2iz%2FJ0ckwCJJl1PhA6QuLT6Rdz4LJARHwLtwktoUriF5DR1jUvYMKJnQasdCKi8306mkk7gO6v9uN2XRanRQt5Js0wurPbbrielb6pi1XQNKy56F%2Fdu%2FYbHRdYdUawCTmNwpSJws3P5akvllXaUQfch%2Bd%2F92%2B7EvLNznor4lzSl2X3pPUitVUACAXaLuUDWZoilJ%2BXPzbXlxMtdsMwpp4jZnEXE1qc2RP9oxeqaATKDUA8Q7CvUIW31ZP1%2FdvGefj2INUSjUOoxEJ90FElzuAUJlc80oxOsZ4aQ99Rsfh1Qhi5%2B07ePpmjzRnO1ELN2%2F%2BhjeYMq29pf9OdR2Pnwdr9jafpGuu8wofCXvQY6pgH1GsNDgA2zB%2FiT5sDoy8AQlcOJSXTpPAlGIKaFWD7ZiTd0pdg%2FbgbtnX5gNGsdK%2B6VpmvvkC8RhPmBhJgcNwiaKRq2abVvhirrkW9OZ8lK%2BILANVYK31qBf%2FqmCaTvC%2FwXnN6NboIBN5BX77%2F%2BeUaid3nTP2k8lIOAsAa2gF8GY2zWOOpqM1qEcRVf3NBJkAH8yhqiSEL9OmNsychzxfvklG9DyFCY&X-Amz-Signature=e4b6a11fd8e1a2979197459943f69e80592105013d69302768a57633ef7e14f4&X-Amz-SignedHeaders=host&x-id=GetObject)
### CNN Architecture
- **Input Layer**: Defines the size of the input images (e.g., 128 x 128 x 3 for color images).
- **Convolutional Layers**: Apply multiple filters and include ReLU activation.
- **Pooling Layers**: Apply max-pooling or average-pooling.
- **Fully Connected Layers**: Flatten the data and produce output based on the number of classes.
- **Output Layer**: Produces the final class probabilities using the softmax activation function.
### Summary
- **Efficiency**: CNNs reduce the number of parameters compared to traditional neural networks, making them computationally efficient.
- **Applications**: Ideal for tasks involving image recognition, object detection, and other computer vision problems.
### Building CNNs with Keras
1. **Model Creation**:
	- Use the `Sequential` model to build the CNN.
2. **Defining Input Shape**:
	- For 128x128 color images: `input_shape=(128, 128, 3)`
3. **Adding Layers**:
	- **Convolutional Layer**:
```python
model.add(Conv2D(16, (2, 2), strides=(1, 1), activation='relu', input_shape=(128, 128, 3)))
```
		- **Parameters**:
			- `16`: Number of filters or kernels.
			- `(2, 2)`: Size of each filter.
			- `strides=(1, 1)`: The step size with which the filter moves across the image.
			- `activation='relu'`: Activation function applied after the convolution operation.
			- `input_shape=(128, 128, 3)`: Shape of the input images. For color images, the last dimension is 3 (RGB channels).
	- **Pooling Layer**:
```python
model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
```
		- **Parameters**:
			- `pool_size=(2, 2)`: Size of the pooling window.
			- `strides=(2, 2)`: The step size with which the pooling window moves across the image.
	- **Additional Convolutional and Pooling Layers**:
```python
model.add(Conv2D(32, (2, 2), strides=(1, 1), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
```
		- **Parameters**:
			- `32`: Number of filters or kernels in this convolutional layer.
			- `(2, 2)`: Size of each filter.
			- `strides=(1, 1)`: The step size with which the filter moves across the image.
			- `activation='relu'`: Activation function applied after the convolution operation.
			- `pool_size=(2, 2)`: Size of the pooling window.
			- `strides=(2, 2)`: The step size with which the pooling window moves across the image.
4. **Flattening and Fully Connected Layers**:
	- **Flatten**: Converts 3D feature maps into 1D.
```python
model.add(Flatten())
```
	- **Dense Layers**:
```python
model.add(Dense(100, activation='relu'))
model.add(Dense(num_classes, activation='softmax'))
```
		- **Parameters**:
			- `100`: Number of neurons in the dense layer.
			- `activation='relu'`: Activation function applied to the neurons in the dense layer.
			- `num_classes`: Number of output neurons, typically equal to the number of classes in the classification problem.
			- `activation='softmax'`: Activation function applied to the output layer to convert raw scores into probabilities.
5. **Compilation**:
	- Define optimizer, loss function, and metrics:
```python
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
```
		- **Parameters**:
			- `optimizer='adam'`: Optimization algorithm used for training.
			- `loss='categorical_crossentropy'`: Loss function used for classification tasks with multiple classes.
			- `metrics=['accuracy']`: Evaluation metric used to measure the performance of the model.
6. **Training and Validation**:
	- Train the model using the `fit` method and validate using a test set.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZGKEHYKE%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T122856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJGMEQCIH8TvZu2qGBpNfxsT9UpWhzFkmCJqU8cYF1UkCVMqIlYAiBQPGGpLrHrg9cMUnluXfuQsBP7Sb1piL5w3dYj1Y3RKSr%2FAwh1EAAaDDYzNzQyMzE4MzgwNSIMwrNF4yFpGXghHFJdKtwD96i1bVwQ5Oxd0WO65AyF24%2FRRunQ8ZnN69HDaLZqp3JWbAny2jNcU4tHFiOLSjHfLLLCky6dOkjwjo8eKpHSQB4%2BeQ6EvbZq8BUcwFJcNPUHLjQpZqUMHbJ6iM7eh2JoD5Qgh3%2BYCbpqaN1PRynfvGcShJMJRTJtFTJxcMAT4%2BWKgZNPbKd033y24zRMjqfZzYq6OIIrkZKLknuhROZntHHq1pGBYvQpFjOpj7GF%2FH2H5a4HYy24i4lCmkyr3tWfKfjSbDz1MWxfZa%2F2Dr2c%2FQ28pwhdc2iz%2FJ0ckwCJJl1PhA6QuLT6Rdz4LJARHwLtwktoUriF5DR1jUvYMKJnQasdCKi8306mkk7gO6v9uN2XRanRQt5Js0wurPbbrielb6pi1XQNKy56F%2Fdu%2FYbHRdYdUawCTmNwpSJws3P5akvllXaUQfch%2Bd%2F92%2B7EvLNznor4lzSl2X3pPUitVUACAXaLuUDWZoilJ%2BXPzbXlxMtdsMwpp4jZnEXE1qc2RP9oxeqaATKDUA8Q7CvUIW31ZP1%2FdvGefj2INUSjUOoxEJ90FElzuAUJlc80oxOsZ4aQ99Rsfh1Qhi5%2B07ePpmjzRnO1ELN2%2F%2BhjeYMq29pf9OdR2Pnwdr9jafpGuu8wofCXvQY6pgH1GsNDgA2zB%2FiT5sDoy8AQlcOJSXTpPAlGIKaFWD7ZiTd0pdg%2FbgbtnX5gNGsdK%2B6VpmvvkC8RhPmBhJgcNwiaKRq2abVvhirrkW9OZ8lK%2BILANVYK31qBf%2FqmCaTvC%2FwXnN6NboIBN5BX77%2F%2BeUaid3nTP2k8lIOAsAa2gF8GY2zWOOpqM1qEcRVf3NBJkAH8yhqiSEL9OmNsychzxfvklG9DyFCY&X-Amz-Signature=4909c40aba549bbc2de3c07aeca0fbdd017e63edcbb18ffdcfaf2a0b1de5b689&X-Amz-SignedHeaders=host&x-id=GetObject)
### Conclusion
CNNs are powerful for image processing tasks due to their ability to automatically extract and learn features from images. The architecture involves convolutional, activation, pooling, and fully connected layers, which collectively enable the network to perform tasks such as image recognition and object detection.
___
## Recurrent Neural Networks (RNNs) Overview (Unsupervised Deep Learning Model)
### Introduction to RNNs
- **Purpose**: RNNs are used to analyze sequences where data points are not independent but rather follow a temporal or sequential relationship.
- **Architecture**: RNNs include loops that allow them to take both the current input and the output from the previous data point into account.
### How RNNs Work
- **Input and Output at Each Time Step**:
	- At time `t = 0`, the network takes in input $ x_0 $ and outputs $ a_0 $.
	- At time `t = 1`, the network takes in input $ x_1 $` `and the previous output $ a_0 $, weighted by $ w_{1,2} $.
	- This process continues, incorporating previous outputs into the computation at each step.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZGKEHYKE%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T122856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJGMEQCIH8TvZu2qGBpNfxsT9UpWhzFkmCJqU8cYF1UkCVMqIlYAiBQPGGpLrHrg9cMUnluXfuQsBP7Sb1piL5w3dYj1Y3RKSr%2FAwh1EAAaDDYzNzQyMzE4MzgwNSIMwrNF4yFpGXghHFJdKtwD96i1bVwQ5Oxd0WO65AyF24%2FRRunQ8ZnN69HDaLZqp3JWbAny2jNcU4tHFiOLSjHfLLLCky6dOkjwjo8eKpHSQB4%2BeQ6EvbZq8BUcwFJcNPUHLjQpZqUMHbJ6iM7eh2JoD5Qgh3%2BYCbpqaN1PRynfvGcShJMJRTJtFTJxcMAT4%2BWKgZNPbKd033y24zRMjqfZzYq6OIIrkZKLknuhROZntHHq1pGBYvQpFjOpj7GF%2FH2H5a4HYy24i4lCmkyr3tWfKfjSbDz1MWxfZa%2F2Dr2c%2FQ28pwhdc2iz%2FJ0ckwCJJl1PhA6QuLT6Rdz4LJARHwLtwktoUriF5DR1jUvYMKJnQasdCKi8306mkk7gO6v9uN2XRanRQt5Js0wurPbbrielb6pi1XQNKy56F%2Fdu%2FYbHRdYdUawCTmNwpSJws3P5akvllXaUQfch%2Bd%2F92%2B7EvLNznor4lzSl2X3pPUitVUACAXaLuUDWZoilJ%2BXPzbXlxMtdsMwpp4jZnEXE1qc2RP9oxeqaATKDUA8Q7CvUIW31ZP1%2FdvGefj2INUSjUOoxEJ90FElzuAUJlc80oxOsZ4aQ99Rsfh1Qhi5%2B07ePpmjzRnO1ELN2%2F%2BhjeYMq29pf9OdR2Pnwdr9jafpGuu8wofCXvQY6pgH1GsNDgA2zB%2FiT5sDoy8AQlcOJSXTpPAlGIKaFWD7ZiTd0pdg%2FbgbtnX5gNGsdK%2B6VpmvvkC8RhPmBhJgcNwiaKRq2abVvhirrkW9OZ8lK%2BILANVYK31qBf%2FqmCaTvC%2FwXnN6NboIBN5BX77%2F%2BeUaid3nTP2k8lIOAsAa2gF8GY2zWOOpqM1qEcRVf3NBJkAH8yhqiSEL9OmNsychzxfvklG9DyFCY&X-Amz-Signature=57ce8ece24ac288da8c9b15293ff5358fc7f0e16160e6b3cf081f925492bf2bc&X-Amz-SignedHeaders=host&x-id=GetObject)
### Applications of RNNs
- **Text Analysis**: Suitable for processing and modeling sequential text data.
- **Genomic Data**: Can analyze sequences in genetic information.
- **Handwriting**: Applied in handwriting generation and recognition.
- **Stock Markets**: Used for predicting stock prices based on historical data.
### Long Short-Term Memory (LSTM) Networks
- **Overview**: A specialized type of RNN designed to overcome some limitations of traditional RNNs.
- **Applications**:
	- **Image Generation**: Models trained on images to generate novel images.
	- **Handwriting Generation**: Creating handwritten text based on trained models.
	- **Image Description**: Automatically describing images.
	- **Video Streams**: Analyzing and describing video sequences.
### Summary
- **RNNs**: Effective for tasks involving sequences and temporal data.
- **LSTM Models**: A specific type of RNN that handles long-term dependencies and is used in advanced applications like image and video analysis.
___
### Autoencoders and Restricted Boltzmann Machines (RBMs)
### Introduction to Autoencoders
- **Definition**: Autoencoders are unsupervised deep learning models used for data compression. They learn to compress and decompress data automatically through neural networks.
- **Purpose**: They aim to learn a compressed representation of the input data and then reconstruct the original data from this representation.
- **Training**: Autoencoders use backpropagation with the target variable being the same as the input, effectively learning an approximation of an identity function.
### Architecture of an Autoencoder
- **Encoder**:
	- Compresses the input data into a lower-dimensional representation.
- **Decoder**:
	- Reconstructs the original data from the compressed representation.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VWN6RTHY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T122856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJHMEUCIQCwDuFhBrHtS9S9cGW2EjyxINcfI9I%2F%2Felgh5TG5ZyDEAIgO2Aa5H%2FNOYYKRQlQAmGf8R7MhBZhCGWeZ3%2FsTeVyWjUq%2FwMIdRAAGgw2Mzc0MjMxODM4MDUiDH1ll9BixEdlqVMDDircA%2BpV0iKoilll129xMJDJTdP7IbaLco%2FJ13T%2BP2iqJDga3S93F%2BiUIlRW8rLiMNb5V2VfCPqP5Gkb5yJ7H9EPZSyBH0XlXje7v1q3DXI5g29Iy1vlWx1jJCZOtKj4X1AO0eIXvHOQVaEBhlp4rXednwMleMQdh7EXPpRhBGZFu3Z7CCkiqfXSRALTuKGECF9x4xOo8JUGZgy4mX8MnomU57k8n783Jt%2F6DCDiOQydhgXiVFN75uDLnm7yOGWf8xpXGVQicYD9TNSxE2KZibXSHTTz47%2FAyjHPMyRd8aIsApubjq9z8Drh5V%2FH68qvIjAL%2FTDOucc9B6pEWx5y0UkfbefUt%2BLtajA84hvxXoYT8u3vYDUddC2wnos35ZSqXgoIPgH7TwMQPlTeOp70bIu6WLEc91Y9XchkncZD26rRdbBgMkYMgbO2EgfTjf6AeSe9VmoUVLTnFr3dplV0xuIrG3BNED%2Fp9AwXR4ea%2FVGKYjaguFOE%2B697Ct6XGeQwlreF%2BNLfVj66pa0c73FjYTBXS8Rhq5AyUP3pyMt4PdolA1JEUbd7w%2FlVT0xP%2FOiYcqTocQfR578NcAywGEXXFDU%2FiYM6JzF72etjqnNsuy%2F1xMrs32%2F7wMLjdzkaDzznMJ3vl70GOqUBJ%2B4ryOq5rArxcyl1nhhWTCDNM4rFxhUqoRWsOggu6ORlSph4de5Mo2dnL0n0D1lYhxeGSwGk4wgalShHPpPoCOQxVps8W8mB9lJlVwOsxBjpLH24oSGinyShZTZtEr2jMoOZYpxrpgESoPw5A8VLsXWAPwnxQaJfwxWtu5ZEG3pNzZDT9B3FmnrZqoKXEMOboMsCK2FNVaq6Q%2FnFyBnlvrmxCXUX&X-Amz-Signature=56ae1237136404b6ec659a78183ef36e31692808fc91842c4c30f7789bca95e8&X-Amz-SignedHeaders=host&x-id=GetObject)
### Applications of Autoencoders
- **Data Denoising**: Removing noise from data to recover the original signal.
- **Dimensionality Reduction**: Reducing the number of features in the data for visualization purposes.
### Advantages over Traditional Methods
- **Non-Linear Transformations**: Autoencoders, with their non-linear activation functions, can learn more complex projections compared to linear methods like Principal Component Analysis (PCA).
### Restricted Boltzmann Machines (RBMs)
- **Overview**: RBMs are a type of autoencoder that can learn the distribution of the input data to perform tasks such as:
	- **Fixing Imbalanced Datasets**: Generating more data points for minority classes to balance datasets.
	- **Estimating Missing Values**: Predicting missing feature values in datasets.
	- **Automatic Feature Extraction**: Learning features from unstructured data.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VWN6RTHY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T122856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJHMEUCIQCwDuFhBrHtS9S9cGW2EjyxINcfI9I%2F%2Felgh5TG5ZyDEAIgO2Aa5H%2FNOYYKRQlQAmGf8R7MhBZhCGWeZ3%2FsTeVyWjUq%2FwMIdRAAGgw2Mzc0MjMxODM4MDUiDH1ll9BixEdlqVMDDircA%2BpV0iKoilll129xMJDJTdP7IbaLco%2FJ13T%2BP2iqJDga3S93F%2BiUIlRW8rLiMNb5V2VfCPqP5Gkb5yJ7H9EPZSyBH0XlXje7v1q3DXI5g29Iy1vlWx1jJCZOtKj4X1AO0eIXvHOQVaEBhlp4rXednwMleMQdh7EXPpRhBGZFu3Z7CCkiqfXSRALTuKGECF9x4xOo8JUGZgy4mX8MnomU57k8n783Jt%2F6DCDiOQydhgXiVFN75uDLnm7yOGWf8xpXGVQicYD9TNSxE2KZibXSHTTz47%2FAyjHPMyRd8aIsApubjq9z8Drh5V%2FH68qvIjAL%2FTDOucc9B6pEWx5y0UkfbefUt%2BLtajA84hvxXoYT8u3vYDUddC2wnos35ZSqXgoIPgH7TwMQPlTeOp70bIu6WLEc91Y9XchkncZD26rRdbBgMkYMgbO2EgfTjf6AeSe9VmoUVLTnFr3dplV0xuIrG3BNED%2Fp9AwXR4ea%2FVGKYjaguFOE%2B697Ct6XGeQwlreF%2BNLfVj66pa0c73FjYTBXS8Rhq5AyUP3pyMt4PdolA1JEUbd7w%2FlVT0xP%2FOiYcqTocQfR578NcAywGEXXFDU%2FiYM6JzF72etjqnNsuy%2F1xMrs32%2F7wMLjdzkaDzznMJ3vl70GOqUBJ%2B4ryOq5rArxcyl1nhhWTCDNM4rFxhUqoRWsOggu6ORlSph4de5Mo2dnL0n0D1lYhxeGSwGk4wgalShHPpPoCOQxVps8W8mB9lJlVwOsxBjpLH24oSGinyShZTZtEr2jMoOZYpxrpgESoPw5A8VLsXWAPwnxQaJfwxWtu5ZEG3pNzZDT9B3FmnrZqoKXEMOboMsCK2FNVaq6Q%2FnFyBnlvrmxCXUX&X-Amz-Signature=125fba8a7b0abfb097b487b6582d7d41c820ffb9d4e7bd84a73047b5da4c1e35&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
