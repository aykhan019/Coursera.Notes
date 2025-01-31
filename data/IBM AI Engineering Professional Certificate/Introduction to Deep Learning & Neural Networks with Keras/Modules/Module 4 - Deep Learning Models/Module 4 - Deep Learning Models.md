

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RLUQ2BB4%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHabPmfmUlATdL8lT2EO67ksXhp0wRJi8Qt6N9HFd2ylAiEA3HWv9q%2FgY5hpnoL5zRLAFi8Bzlr%2B6TUjG1F%2ByHGgK3AqiAQIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHCETO6Fj2bp2AyhtSrcA2vq8Eyby7DPY8SyVOXT6EcjKtUIwmh2vWzOiIifBfPKTOLu7TKzV4vdM%2F7EsbHfDSdxiaYahZ7X3%2B8jF6PaDkAd1j9GiXUY4RBdvBjJJZu47FOZBFElLi9Rmol4V6YqjOlB%2BhkDVvkxdJ%2BZ7s43JTlNX6lk5NNKptRTKTFRYDtMcthdFdtkSXt7%2BygX4KdiFL3vUvxieE%2FVUHQFNttiWcEVFB0dsYQakpdTLDOQhAxX0BoaiZv4FC2iDG25YgVM7k9auvgmqXX5Vn4utzg%2BHl4HGpAwORHaPic57St2TdQaUfrrn%2FuTkZImHV5bpdjJhwUu1mxM5haXj8xMpFPLo1QW0FCq7Al12aPTzrMQA1fthpPHY03hXgzE7zPF4%2FmnpIUpYlJmc0OAZVjAGg0MX1uuSVzr9e7ZnBbcY%2Fm7prc1eOq%2F8V13Mc3hlcZwiEw4kVpTKqUsw%2Fjq6L7AKCNUjG9bKQCLh7gigvMfR3mRHa%2BYClHCwJJWveqFeYW%2FBtt68q%2BvpAlDp5yv%2FxkAIhsaAhioulzA92R%2B2tawP7bPt%2Fy2zX%2F6%2BMufTYzjHauc1bjH0U%2BBL1OSxWYxWw%2BTUrBvSvXvnXBifKy%2BKwVAD7ZgQG8FJEDEDys%2FyztcctpZMOSs87wGOqUBpfaBzpkA4pSYi9ZdsRGSmsiDq2cwVvWJdGl0Uy3wnZDFJHhfpiVBFyiDZ%2FXcvZziasX8dxLT8s9p%2BmcDllo098GLnYiI2s2PDyXrlox%2BO4zMvzh8h14Yxo6SjHLSD1Qo1Les9mewBjrTXdx%2B5GMKfXzoZwqbLsI5ZU1U7%2Blmw3AsNZYX1yvGEgiEvJtUR5nyZOS3BzkTmVu59CYmw6gqKQQ4LFLE&X-Amz-Signature=e7a5b22f280207ac4d7adc82385627cd86f54851cbacdcddea2cdf3414be62bf&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RLUQ2BB4%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHabPmfmUlATdL8lT2EO67ksXhp0wRJi8Qt6N9HFd2ylAiEA3HWv9q%2FgY5hpnoL5zRLAFi8Bzlr%2B6TUjG1F%2ByHGgK3AqiAQIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHCETO6Fj2bp2AyhtSrcA2vq8Eyby7DPY8SyVOXT6EcjKtUIwmh2vWzOiIifBfPKTOLu7TKzV4vdM%2F7EsbHfDSdxiaYahZ7X3%2B8jF6PaDkAd1j9GiXUY4RBdvBjJJZu47FOZBFElLi9Rmol4V6YqjOlB%2BhkDVvkxdJ%2BZ7s43JTlNX6lk5NNKptRTKTFRYDtMcthdFdtkSXt7%2BygX4KdiFL3vUvxieE%2FVUHQFNttiWcEVFB0dsYQakpdTLDOQhAxX0BoaiZv4FC2iDG25YgVM7k9auvgmqXX5Vn4utzg%2BHl4HGpAwORHaPic57St2TdQaUfrrn%2FuTkZImHV5bpdjJhwUu1mxM5haXj8xMpFPLo1QW0FCq7Al12aPTzrMQA1fthpPHY03hXgzE7zPF4%2FmnpIUpYlJmc0OAZVjAGg0MX1uuSVzr9e7ZnBbcY%2Fm7prc1eOq%2F8V13Mc3hlcZwiEw4kVpTKqUsw%2Fjq6L7AKCNUjG9bKQCLh7gigvMfR3mRHa%2BYClHCwJJWveqFeYW%2FBtt68q%2BvpAlDp5yv%2FxkAIhsaAhioulzA92R%2B2tawP7bPt%2Fy2zX%2F6%2BMufTYzjHauc1bjH0U%2BBL1OSxWYxWw%2BTUrBvSvXvnXBifKy%2BKwVAD7ZgQG8FJEDEDys%2FyztcctpZMOSs87wGOqUBpfaBzpkA4pSYi9ZdsRGSmsiDq2cwVvWJdGl0Uy3wnZDFJHhfpiVBFyiDZ%2FXcvZziasX8dxLT8s9p%2BmcDllo098GLnYiI2s2PDyXrlox%2BO4zMvzh8h14Yxo6SjHLSD1Qo1Les9mewBjrTXdx%2B5GMKfXzoZwqbLsI5ZU1U7%2Blmw3AsNZYX1yvGEgiEvJtUR5nyZOS3BzkTmVu59CYmw6gqKQQ4LFLE&X-Amz-Signature=2d18fc7b311c79029e2844b5e3a371766d87e8fb7b01645ff74191216f2f7f5c&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RLUQ2BB4%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHabPmfmUlATdL8lT2EO67ksXhp0wRJi8Qt6N9HFd2ylAiEA3HWv9q%2FgY5hpnoL5zRLAFi8Bzlr%2B6TUjG1F%2ByHGgK3AqiAQIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHCETO6Fj2bp2AyhtSrcA2vq8Eyby7DPY8SyVOXT6EcjKtUIwmh2vWzOiIifBfPKTOLu7TKzV4vdM%2F7EsbHfDSdxiaYahZ7X3%2B8jF6PaDkAd1j9GiXUY4RBdvBjJJZu47FOZBFElLi9Rmol4V6YqjOlB%2BhkDVvkxdJ%2BZ7s43JTlNX6lk5NNKptRTKTFRYDtMcthdFdtkSXt7%2BygX4KdiFL3vUvxieE%2FVUHQFNttiWcEVFB0dsYQakpdTLDOQhAxX0BoaiZv4FC2iDG25YgVM7k9auvgmqXX5Vn4utzg%2BHl4HGpAwORHaPic57St2TdQaUfrrn%2FuTkZImHV5bpdjJhwUu1mxM5haXj8xMpFPLo1QW0FCq7Al12aPTzrMQA1fthpPHY03hXgzE7zPF4%2FmnpIUpYlJmc0OAZVjAGg0MX1uuSVzr9e7ZnBbcY%2Fm7prc1eOq%2F8V13Mc3hlcZwiEw4kVpTKqUsw%2Fjq6L7AKCNUjG9bKQCLh7gigvMfR3mRHa%2BYClHCwJJWveqFeYW%2FBtt68q%2BvpAlDp5yv%2FxkAIhsaAhioulzA92R%2B2tawP7bPt%2Fy2zX%2F6%2BMufTYzjHauc1bjH0U%2BBL1OSxWYxWw%2BTUrBvSvXvnXBifKy%2BKwVAD7ZgQG8FJEDEDys%2FyztcctpZMOSs87wGOqUBpfaBzpkA4pSYi9ZdsRGSmsiDq2cwVvWJdGl0Uy3wnZDFJHhfpiVBFyiDZ%2FXcvZziasX8dxLT8s9p%2BmcDllo098GLnYiI2s2PDyXrlox%2BO4zMvzh8h14Yxo6SjHLSD1Qo1Les9mewBjrTXdx%2B5GMKfXzoZwqbLsI5ZU1U7%2Blmw3AsNZYX1yvGEgiEvJtUR5nyZOS3BzkTmVu59CYmw6gqKQQ4LFLE&X-Amz-Signature=1735321e108ae256e724b71cf35fb3540996c9ffe6e8da7a213a7449d2785dd2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RLUQ2BB4%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHabPmfmUlATdL8lT2EO67ksXhp0wRJi8Qt6N9HFd2ylAiEA3HWv9q%2FgY5hpnoL5zRLAFi8Bzlr%2B6TUjG1F%2ByHGgK3AqiAQIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHCETO6Fj2bp2AyhtSrcA2vq8Eyby7DPY8SyVOXT6EcjKtUIwmh2vWzOiIifBfPKTOLu7TKzV4vdM%2F7EsbHfDSdxiaYahZ7X3%2B8jF6PaDkAd1j9GiXUY4RBdvBjJJZu47FOZBFElLi9Rmol4V6YqjOlB%2BhkDVvkxdJ%2BZ7s43JTlNX6lk5NNKptRTKTFRYDtMcthdFdtkSXt7%2BygX4KdiFL3vUvxieE%2FVUHQFNttiWcEVFB0dsYQakpdTLDOQhAxX0BoaiZv4FC2iDG25YgVM7k9auvgmqXX5Vn4utzg%2BHl4HGpAwORHaPic57St2TdQaUfrrn%2FuTkZImHV5bpdjJhwUu1mxM5haXj8xMpFPLo1QW0FCq7Al12aPTzrMQA1fthpPHY03hXgzE7zPF4%2FmnpIUpYlJmc0OAZVjAGg0MX1uuSVzr9e7ZnBbcY%2Fm7prc1eOq%2F8V13Mc3hlcZwiEw4kVpTKqUsw%2Fjq6L7AKCNUjG9bKQCLh7gigvMfR3mRHa%2BYClHCwJJWveqFeYW%2FBtt68q%2BvpAlDp5yv%2FxkAIhsaAhioulzA92R%2B2tawP7bPt%2Fy2zX%2F6%2BMufTYzjHauc1bjH0U%2BBL1OSxWYxWw%2BTUrBvSvXvnXBifKy%2BKwVAD7ZgQG8FJEDEDys%2FyztcctpZMOSs87wGOqUBpfaBzpkA4pSYi9ZdsRGSmsiDq2cwVvWJdGl0Uy3wnZDFJHhfpiVBFyiDZ%2FXcvZziasX8dxLT8s9p%2BmcDllo098GLnYiI2s2PDyXrlox%2BO4zMvzh8h14Yxo6SjHLSD1Qo1Les9mewBjrTXdx%2B5GMKfXzoZwqbLsI5ZU1U7%2Blmw3AsNZYX1yvGEgiEvJtUR5nyZOS3BzkTmVu59CYmw6gqKQQ4LFLE&X-Amz-Signature=2cbaa42bf3961ad0f9ad30d4ec353e8d4ecba4e720938ca8f68e637fb2d2e510&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RLUQ2BB4%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHabPmfmUlATdL8lT2EO67ksXhp0wRJi8Qt6N9HFd2ylAiEA3HWv9q%2FgY5hpnoL5zRLAFi8Bzlr%2B6TUjG1F%2ByHGgK3AqiAQIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHCETO6Fj2bp2AyhtSrcA2vq8Eyby7DPY8SyVOXT6EcjKtUIwmh2vWzOiIifBfPKTOLu7TKzV4vdM%2F7EsbHfDSdxiaYahZ7X3%2B8jF6PaDkAd1j9GiXUY4RBdvBjJJZu47FOZBFElLi9Rmol4V6YqjOlB%2BhkDVvkxdJ%2BZ7s43JTlNX6lk5NNKptRTKTFRYDtMcthdFdtkSXt7%2BygX4KdiFL3vUvxieE%2FVUHQFNttiWcEVFB0dsYQakpdTLDOQhAxX0BoaiZv4FC2iDG25YgVM7k9auvgmqXX5Vn4utzg%2BHl4HGpAwORHaPic57St2TdQaUfrrn%2FuTkZImHV5bpdjJhwUu1mxM5haXj8xMpFPLo1QW0FCq7Al12aPTzrMQA1fthpPHY03hXgzE7zPF4%2FmnpIUpYlJmc0OAZVjAGg0MX1uuSVzr9e7ZnBbcY%2Fm7prc1eOq%2F8V13Mc3hlcZwiEw4kVpTKqUsw%2Fjq6L7AKCNUjG9bKQCLh7gigvMfR3mRHa%2BYClHCwJJWveqFeYW%2FBtt68q%2BvpAlDp5yv%2FxkAIhsaAhioulzA92R%2B2tawP7bPt%2Fy2zX%2F6%2BMufTYzjHauc1bjH0U%2BBL1OSxWYxWw%2BTUrBvSvXvnXBifKy%2BKwVAD7ZgQG8FJEDEDys%2FyztcctpZMOSs87wGOqUBpfaBzpkA4pSYi9ZdsRGSmsiDq2cwVvWJdGl0Uy3wnZDFJHhfpiVBFyiDZ%2FXcvZziasX8dxLT8s9p%2BmcDllo098GLnYiI2s2PDyXrlox%2BO4zMvzh8h14Yxo6SjHLSD1Qo1Les9mewBjrTXdx%2B5GMKfXzoZwqbLsI5ZU1U7%2Blmw3AsNZYX1yvGEgiEvJtUR5nyZOS3BzkTmVu59CYmw6gqKQQ4LFLE&X-Amz-Signature=e020bc7a2602bceb6e72fff30a78df6a901b6db85465a16815b7684c4111305e&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RLUQ2BB4%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHabPmfmUlATdL8lT2EO67ksXhp0wRJi8Qt6N9HFd2ylAiEA3HWv9q%2FgY5hpnoL5zRLAFi8Bzlr%2B6TUjG1F%2ByHGgK3AqiAQIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHCETO6Fj2bp2AyhtSrcA2vq8Eyby7DPY8SyVOXT6EcjKtUIwmh2vWzOiIifBfPKTOLu7TKzV4vdM%2F7EsbHfDSdxiaYahZ7X3%2B8jF6PaDkAd1j9GiXUY4RBdvBjJJZu47FOZBFElLi9Rmol4V6YqjOlB%2BhkDVvkxdJ%2BZ7s43JTlNX6lk5NNKptRTKTFRYDtMcthdFdtkSXt7%2BygX4KdiFL3vUvxieE%2FVUHQFNttiWcEVFB0dsYQakpdTLDOQhAxX0BoaiZv4FC2iDG25YgVM7k9auvgmqXX5Vn4utzg%2BHl4HGpAwORHaPic57St2TdQaUfrrn%2FuTkZImHV5bpdjJhwUu1mxM5haXj8xMpFPLo1QW0FCq7Al12aPTzrMQA1fthpPHY03hXgzE7zPF4%2FmnpIUpYlJmc0OAZVjAGg0MX1uuSVzr9e7ZnBbcY%2Fm7prc1eOq%2F8V13Mc3hlcZwiEw4kVpTKqUsw%2Fjq6L7AKCNUjG9bKQCLh7gigvMfR3mRHa%2BYClHCwJJWveqFeYW%2FBtt68q%2BvpAlDp5yv%2FxkAIhsaAhioulzA92R%2B2tawP7bPt%2Fy2zX%2F6%2BMufTYzjHauc1bjH0U%2BBL1OSxWYxWw%2BTUrBvSvXvnXBifKy%2BKwVAD7ZgQG8FJEDEDys%2FyztcctpZMOSs87wGOqUBpfaBzpkA4pSYi9ZdsRGSmsiDq2cwVvWJdGl0Uy3wnZDFJHhfpiVBFyiDZ%2FXcvZziasX8dxLT8s9p%2BmcDllo098GLnYiI2s2PDyXrlox%2BO4zMvzh8h14Yxo6SjHLSD1Qo1Les9mewBjrTXdx%2B5GMKfXzoZwqbLsI5ZU1U7%2Blmw3AsNZYX1yvGEgiEvJtUR5nyZOS3BzkTmVu59CYmw6gqKQQ4LFLE&X-Amz-Signature=ab2401be675d62636dec6585026fecde1ccae01f4e53e6abcc0de16bc2c0944e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RLUQ2BB4%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHabPmfmUlATdL8lT2EO67ksXhp0wRJi8Qt6N9HFd2ylAiEA3HWv9q%2FgY5hpnoL5zRLAFi8Bzlr%2B6TUjG1F%2ByHGgK3AqiAQIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHCETO6Fj2bp2AyhtSrcA2vq8Eyby7DPY8SyVOXT6EcjKtUIwmh2vWzOiIifBfPKTOLu7TKzV4vdM%2F7EsbHfDSdxiaYahZ7X3%2B8jF6PaDkAd1j9GiXUY4RBdvBjJJZu47FOZBFElLi9Rmol4V6YqjOlB%2BhkDVvkxdJ%2BZ7s43JTlNX6lk5NNKptRTKTFRYDtMcthdFdtkSXt7%2BygX4KdiFL3vUvxieE%2FVUHQFNttiWcEVFB0dsYQakpdTLDOQhAxX0BoaiZv4FC2iDG25YgVM7k9auvgmqXX5Vn4utzg%2BHl4HGpAwORHaPic57St2TdQaUfrrn%2FuTkZImHV5bpdjJhwUu1mxM5haXj8xMpFPLo1QW0FCq7Al12aPTzrMQA1fthpPHY03hXgzE7zPF4%2FmnpIUpYlJmc0OAZVjAGg0MX1uuSVzr9e7ZnBbcY%2Fm7prc1eOq%2F8V13Mc3hlcZwiEw4kVpTKqUsw%2Fjq6L7AKCNUjG9bKQCLh7gigvMfR3mRHa%2BYClHCwJJWveqFeYW%2FBtt68q%2BvpAlDp5yv%2FxkAIhsaAhioulzA92R%2B2tawP7bPt%2Fy2zX%2F6%2BMufTYzjHauc1bjH0U%2BBL1OSxWYxWw%2BTUrBvSvXvnXBifKy%2BKwVAD7ZgQG8FJEDEDys%2FyztcctpZMOSs87wGOqUBpfaBzpkA4pSYi9ZdsRGSmsiDq2cwVvWJdGl0Uy3wnZDFJHhfpiVBFyiDZ%2FXcvZziasX8dxLT8s9p%2BmcDllo098GLnYiI2s2PDyXrlox%2BO4zMvzh8h14Yxo6SjHLSD1Qo1Les9mewBjrTXdx%2B5GMKfXzoZwqbLsI5ZU1U7%2Blmw3AsNZYX1yvGEgiEvJtUR5nyZOS3BzkTmVu59CYmw6gqKQQ4LFLE&X-Amz-Signature=c376580eb068bf37bb0fc63fef62c2cb884d7973279967836edb0818fd4f1523&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RLUQ2BB4%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHabPmfmUlATdL8lT2EO67ksXhp0wRJi8Qt6N9HFd2ylAiEA3HWv9q%2FgY5hpnoL5zRLAFi8Bzlr%2B6TUjG1F%2ByHGgK3AqiAQIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHCETO6Fj2bp2AyhtSrcA2vq8Eyby7DPY8SyVOXT6EcjKtUIwmh2vWzOiIifBfPKTOLu7TKzV4vdM%2F7EsbHfDSdxiaYahZ7X3%2B8jF6PaDkAd1j9GiXUY4RBdvBjJJZu47FOZBFElLi9Rmol4V6YqjOlB%2BhkDVvkxdJ%2BZ7s43JTlNX6lk5NNKptRTKTFRYDtMcthdFdtkSXt7%2BygX4KdiFL3vUvxieE%2FVUHQFNttiWcEVFB0dsYQakpdTLDOQhAxX0BoaiZv4FC2iDG25YgVM7k9auvgmqXX5Vn4utzg%2BHl4HGpAwORHaPic57St2TdQaUfrrn%2FuTkZImHV5bpdjJhwUu1mxM5haXj8xMpFPLo1QW0FCq7Al12aPTzrMQA1fthpPHY03hXgzE7zPF4%2FmnpIUpYlJmc0OAZVjAGg0MX1uuSVzr9e7ZnBbcY%2Fm7prc1eOq%2F8V13Mc3hlcZwiEw4kVpTKqUsw%2Fjq6L7AKCNUjG9bKQCLh7gigvMfR3mRHa%2BYClHCwJJWveqFeYW%2FBtt68q%2BvpAlDp5yv%2FxkAIhsaAhioulzA92R%2B2tawP7bPt%2Fy2zX%2F6%2BMufTYzjHauc1bjH0U%2BBL1OSxWYxWw%2BTUrBvSvXvnXBifKy%2BKwVAD7ZgQG8FJEDEDys%2FyztcctpZMOSs87wGOqUBpfaBzpkA4pSYi9ZdsRGSmsiDq2cwVvWJdGl0Uy3wnZDFJHhfpiVBFyiDZ%2FXcvZziasX8dxLT8s9p%2BmcDllo098GLnYiI2s2PDyXrlox%2BO4zMvzh8h14Yxo6SjHLSD1Qo1Les9mewBjrTXdx%2B5GMKfXzoZwqbLsI5ZU1U7%2Blmw3AsNZYX1yvGEgiEvJtUR5nyZOS3BzkTmVu59CYmw6gqKQQ4LFLE&X-Amz-Signature=1fbbe9dbe5fab0609bef1012220b3f860100ed2b5a36a0541479531191642ad1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RLUQ2BB4%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHabPmfmUlATdL8lT2EO67ksXhp0wRJi8Qt6N9HFd2ylAiEA3HWv9q%2FgY5hpnoL5zRLAFi8Bzlr%2B6TUjG1F%2ByHGgK3AqiAQIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHCETO6Fj2bp2AyhtSrcA2vq8Eyby7DPY8SyVOXT6EcjKtUIwmh2vWzOiIifBfPKTOLu7TKzV4vdM%2F7EsbHfDSdxiaYahZ7X3%2B8jF6PaDkAd1j9GiXUY4RBdvBjJJZu47FOZBFElLi9Rmol4V6YqjOlB%2BhkDVvkxdJ%2BZ7s43JTlNX6lk5NNKptRTKTFRYDtMcthdFdtkSXt7%2BygX4KdiFL3vUvxieE%2FVUHQFNttiWcEVFB0dsYQakpdTLDOQhAxX0BoaiZv4FC2iDG25YgVM7k9auvgmqXX5Vn4utzg%2BHl4HGpAwORHaPic57St2TdQaUfrrn%2FuTkZImHV5bpdjJhwUu1mxM5haXj8xMpFPLo1QW0FCq7Al12aPTzrMQA1fthpPHY03hXgzE7zPF4%2FmnpIUpYlJmc0OAZVjAGg0MX1uuSVzr9e7ZnBbcY%2Fm7prc1eOq%2F8V13Mc3hlcZwiEw4kVpTKqUsw%2Fjq6L7AKCNUjG9bKQCLh7gigvMfR3mRHa%2BYClHCwJJWveqFeYW%2FBtt68q%2BvpAlDp5yv%2FxkAIhsaAhioulzA92R%2B2tawP7bPt%2Fy2zX%2F6%2BMufTYzjHauc1bjH0U%2BBL1OSxWYxWw%2BTUrBvSvXvnXBifKy%2BKwVAD7ZgQG8FJEDEDys%2FyztcctpZMOSs87wGOqUBpfaBzpkA4pSYi9ZdsRGSmsiDq2cwVvWJdGl0Uy3wnZDFJHhfpiVBFyiDZ%2FXcvZziasX8dxLT8s9p%2BmcDllo098GLnYiI2s2PDyXrlox%2BO4zMvzh8h14Yxo6SjHLSD1Qo1Les9mewBjrTXdx%2B5GMKfXzoZwqbLsI5ZU1U7%2Blmw3AsNZYX1yvGEgiEvJtUR5nyZOS3BzkTmVu59CYmw6gqKQQ4LFLE&X-Amz-Signature=ce09ea8af54fb172795ccb8d89812221f00f85269b07185f49de173832e1152f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663EZJ5OVQ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDHEkD0DknR0CTDu4ICIISuVWLGPVvAGau0HM9oYVg0ngIhAIUTEe%2FwQsGAPT6gcJaK4HKUmYkJ3%2BWBfWNNiKNIkeGfKogECL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxBJMO32iZshtcipmQq3APELcUC7q%2B8aXSL9VbxBQ1XndJJA24C5DCQ4n0WRlPIRja3760zIoPQJ0TE1yFCysx5ZT3R9%2B8XuyO79x1LmqylX%2BEe%2BAk9SuKSA3o1yWc85JR%2FvsxLGU%2B9wLCiIjtrrXiQ4QVyDaFO%2BMyqd6l%2BacwGgWSMU1NDTgXuKTPRKqm5FRVHxmaF6cpIHAbcIrTRaZmVJX1JKgocTiJv5xlzOARcADSb3fzRfOG8B9ShheYHGU6%2Fwz1nA7sB0Eg3wPRqplRUoGmJvplz5zF07HfY3bb3O%2FvZPpZQxJ7WHGpCsf2F%2Be7DsmaUmxe4WFxYQi5FNGrFnsOU4IX%2BXGnYdaeQ3tiV9q4%2FyL34P4HwJ3atdRZly1y2qAZ%2FcPTunvB0j%2BvcEDx2VCh%2BF4NV3GhE5KVoYare71YkdfIwmsGwqHCgn461Y21sRo%2FrNWws0qDt0vqTofBbE60RzsACos2RKP8XZrZIHJwfcnIyHSsy322J%2FyaIxIljO0YJ952JoWPjDd3%2F5Fx%2Fu9jsx0FkIw5sAcaggvlwzPwGNraHiRSKCBKgKzjP%2BjOx%2BoqsN4SRTzuW8KXNDiyK7gR7Ka2jaWjRRowDATM3NGPERl1DERtovxGZwpVFnKitldxOGBtk20Rv0TC7rPO8BjqkAWMRvuAcTE%2BN7XP%2FQ8z6FfKIp01hevZGLnL9yAjfNW8nHatL2zeSBOJDFB2dJy0oqpXBV0yE4my3bHZQEem3D6jUCtUpUNDSolhue%2BJLHlG%2FARWEgrQ5pxzgBK6gdLbFgYFgFBHDoKV%2FcktefqoAgfa9bDtYtMg3AmFbU1Zr1Y%2BbOLOVldMM9UQI4APWbEo8uZubbXl1UBOpBIjHZQkx99ytjjCZ&X-Amz-Signature=10894bf9b54e07071c0b2cf2f39921eb90b4291c17bf70fbf7a7a1a2d30635c9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663EZJ5OVQ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDHEkD0DknR0CTDu4ICIISuVWLGPVvAGau0HM9oYVg0ngIhAIUTEe%2FwQsGAPT6gcJaK4HKUmYkJ3%2BWBfWNNiKNIkeGfKogECL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxBJMO32iZshtcipmQq3APELcUC7q%2B8aXSL9VbxBQ1XndJJA24C5DCQ4n0WRlPIRja3760zIoPQJ0TE1yFCysx5ZT3R9%2B8XuyO79x1LmqylX%2BEe%2BAk9SuKSA3o1yWc85JR%2FvsxLGU%2B9wLCiIjtrrXiQ4QVyDaFO%2BMyqd6l%2BacwGgWSMU1NDTgXuKTPRKqm5FRVHxmaF6cpIHAbcIrTRaZmVJX1JKgocTiJv5xlzOARcADSb3fzRfOG8B9ShheYHGU6%2Fwz1nA7sB0Eg3wPRqplRUoGmJvplz5zF07HfY3bb3O%2FvZPpZQxJ7WHGpCsf2F%2Be7DsmaUmxe4WFxYQi5FNGrFnsOU4IX%2BXGnYdaeQ3tiV9q4%2FyL34P4HwJ3atdRZly1y2qAZ%2FcPTunvB0j%2BvcEDx2VCh%2BF4NV3GhE5KVoYare71YkdfIwmsGwqHCgn461Y21sRo%2FrNWws0qDt0vqTofBbE60RzsACos2RKP8XZrZIHJwfcnIyHSsy322J%2FyaIxIljO0YJ952JoWPjDd3%2F5Fx%2Fu9jsx0FkIw5sAcaggvlwzPwGNraHiRSKCBKgKzjP%2BjOx%2BoqsN4SRTzuW8KXNDiyK7gR7Ka2jaWjRRowDATM3NGPERl1DERtovxGZwpVFnKitldxOGBtk20Rv0TC7rPO8BjqkAWMRvuAcTE%2BN7XP%2FQ8z6FfKIp01hevZGLnL9yAjfNW8nHatL2zeSBOJDFB2dJy0oqpXBV0yE4my3bHZQEem3D6jUCtUpUNDSolhue%2BJLHlG%2FARWEgrQ5pxzgBK6gdLbFgYFgFBHDoKV%2FcktefqoAgfa9bDtYtMg3AmFbU1Zr1Y%2BbOLOVldMM9UQI4APWbEo8uZubbXl1UBOpBIjHZQkx99ytjjCZ&X-Amz-Signature=674a3fc867a156c30a5a715fb723dbce70a9a67c298e837b3aed5d29eab9e39b&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
