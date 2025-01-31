

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SSYHC34%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081842Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDbofWR70zoBdgYNo3A5SyAgzWXvt9%2F1mgJLEZPioK85wIhAOyRkGmE7%2BAVIXemBbolF822AqHLuTYzF7%2FRu070IdvNKogECLn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyxKo709E1b%2FOCwJDQq3ANdnWGyAQSg08IK5WqUvTHabyAOWhyRESfDvpRKAZmXt%2BXnJ%2BVHnKY20k1Jzb6CxOFPk32fyV75Aj9GoD6IL7krx6P6Dg4%2FpvKJ7iNvHWERh%2F%2FN9%2FUmp4KAxld5PGETKOVKaho%2Bpm152kd%2Fw6KIZmjdiTggm51GHHyUHr1EHO%2By9LsVI8Pt1h9dlsqFmhSXlSStaUP45yK9UyELlUFaR6IivzosJTCif%2BJKxdMPqj9XNa3a3q%2FVeqsMi9VYC9MmxP5YdavKY1TT0E4872e96DuJm8cW8tlOYskXm%2FuWQVxMT6herqTSEWGkWIggkqK0dcxlD%2FMXI0Ca0zh5AqDAV6VWKv%2BZRKXcnTHWK%2BmIvoRmizoJuubdX4eRGgzGHcZ%2FM6UPEtc6qfbnPse0Cs%2Bj%2Fl%2FxgBxIJnt0iGMnTcO71MeuxtW%2FgULqH5lACb4HwysbsnYw1PHPq0rWOr7hEtzK3E%2FPd0MLwPs9PUheZuhY024xdLutvFBbz9E9X6QimGaZeCkYdGfyQii%2B6tKcWBAPbCVIQawItdTuEe99sO1K7Q%2FYKpQFwz7wjoRPw%2BKfjWlYV5eEjCuuK%2BuIp8kec2YdQ1MNb2mb48BA4cLrmi0sxk%2F29ImS7uLHlBsNK3orAzDb%2FvG8BjqkAXE7QB3mbzbISsbNtJOdySnXLzLZoH%2BclWtCMrg7vr9dIrvsR1pcFEDl%2FftTM6ooEDhTGZvpHWekQfPUmEcfxpck0Dkf11A7golMnbfZq9pSwlWfTOCuJVMBRDKyLXaITSzljA0O4ToJ%2BTq8zCBc8gm4JJ7ZtkcF9iCQlXmqDSC%2Fww9y5gtwrQz1jhdlplAYsB1SKvXBOT%2FxnfJxQaLczrxfl%2BpQ&X-Amz-Signature=c1d184e4b3396c3499f71e7f31ade82ecdbae2d579244d8feb9bd0eda1dd9994&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SSYHC34%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081842Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDbofWR70zoBdgYNo3A5SyAgzWXvt9%2F1mgJLEZPioK85wIhAOyRkGmE7%2BAVIXemBbolF822AqHLuTYzF7%2FRu070IdvNKogECLn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyxKo709E1b%2FOCwJDQq3ANdnWGyAQSg08IK5WqUvTHabyAOWhyRESfDvpRKAZmXt%2BXnJ%2BVHnKY20k1Jzb6CxOFPk32fyV75Aj9GoD6IL7krx6P6Dg4%2FpvKJ7iNvHWERh%2F%2FN9%2FUmp4KAxld5PGETKOVKaho%2Bpm152kd%2Fw6KIZmjdiTggm51GHHyUHr1EHO%2By9LsVI8Pt1h9dlsqFmhSXlSStaUP45yK9UyELlUFaR6IivzosJTCif%2BJKxdMPqj9XNa3a3q%2FVeqsMi9VYC9MmxP5YdavKY1TT0E4872e96DuJm8cW8tlOYskXm%2FuWQVxMT6herqTSEWGkWIggkqK0dcxlD%2FMXI0Ca0zh5AqDAV6VWKv%2BZRKXcnTHWK%2BmIvoRmizoJuubdX4eRGgzGHcZ%2FM6UPEtc6qfbnPse0Cs%2Bj%2Fl%2FxgBxIJnt0iGMnTcO71MeuxtW%2FgULqH5lACb4HwysbsnYw1PHPq0rWOr7hEtzK3E%2FPd0MLwPs9PUheZuhY024xdLutvFBbz9E9X6QimGaZeCkYdGfyQii%2B6tKcWBAPbCVIQawItdTuEe99sO1K7Q%2FYKpQFwz7wjoRPw%2BKfjWlYV5eEjCuuK%2BuIp8kec2YdQ1MNb2mb48BA4cLrmi0sxk%2F29ImS7uLHlBsNK3orAzDb%2FvG8BjqkAXE7QB3mbzbISsbNtJOdySnXLzLZoH%2BclWtCMrg7vr9dIrvsR1pcFEDl%2FftTM6ooEDhTGZvpHWekQfPUmEcfxpck0Dkf11A7golMnbfZq9pSwlWfTOCuJVMBRDKyLXaITSzljA0O4ToJ%2BTq8zCBc8gm4JJ7ZtkcF9iCQlXmqDSC%2Fww9y5gtwrQz1jhdlplAYsB1SKvXBOT%2FxnfJxQaLczrxfl%2BpQ&X-Amz-Signature=13bcbc496b0ceb71002c34038b76eb3175fe91b68a3a6abb0f71a124496dde57&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SSYHC34%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081842Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDbofWR70zoBdgYNo3A5SyAgzWXvt9%2F1mgJLEZPioK85wIhAOyRkGmE7%2BAVIXemBbolF822AqHLuTYzF7%2FRu070IdvNKogECLn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyxKo709E1b%2FOCwJDQq3ANdnWGyAQSg08IK5WqUvTHabyAOWhyRESfDvpRKAZmXt%2BXnJ%2BVHnKY20k1Jzb6CxOFPk32fyV75Aj9GoD6IL7krx6P6Dg4%2FpvKJ7iNvHWERh%2F%2FN9%2FUmp4KAxld5PGETKOVKaho%2Bpm152kd%2Fw6KIZmjdiTggm51GHHyUHr1EHO%2By9LsVI8Pt1h9dlsqFmhSXlSStaUP45yK9UyELlUFaR6IivzosJTCif%2BJKxdMPqj9XNa3a3q%2FVeqsMi9VYC9MmxP5YdavKY1TT0E4872e96DuJm8cW8tlOYskXm%2FuWQVxMT6herqTSEWGkWIggkqK0dcxlD%2FMXI0Ca0zh5AqDAV6VWKv%2BZRKXcnTHWK%2BmIvoRmizoJuubdX4eRGgzGHcZ%2FM6UPEtc6qfbnPse0Cs%2Bj%2Fl%2FxgBxIJnt0iGMnTcO71MeuxtW%2FgULqH5lACb4HwysbsnYw1PHPq0rWOr7hEtzK3E%2FPd0MLwPs9PUheZuhY024xdLutvFBbz9E9X6QimGaZeCkYdGfyQii%2B6tKcWBAPbCVIQawItdTuEe99sO1K7Q%2FYKpQFwz7wjoRPw%2BKfjWlYV5eEjCuuK%2BuIp8kec2YdQ1MNb2mb48BA4cLrmi0sxk%2F29ImS7uLHlBsNK3orAzDb%2FvG8BjqkAXE7QB3mbzbISsbNtJOdySnXLzLZoH%2BclWtCMrg7vr9dIrvsR1pcFEDl%2FftTM6ooEDhTGZvpHWekQfPUmEcfxpck0Dkf11A7golMnbfZq9pSwlWfTOCuJVMBRDKyLXaITSzljA0O4ToJ%2BTq8zCBc8gm4JJ7ZtkcF9iCQlXmqDSC%2Fww9y5gtwrQz1jhdlplAYsB1SKvXBOT%2FxnfJxQaLczrxfl%2BpQ&X-Amz-Signature=12334138b9129b78944443decd7df7f5702d8a16a8f8dfb04fe8f51a417894cd&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SSYHC34%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081842Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDbofWR70zoBdgYNo3A5SyAgzWXvt9%2F1mgJLEZPioK85wIhAOyRkGmE7%2BAVIXemBbolF822AqHLuTYzF7%2FRu070IdvNKogECLn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyxKo709E1b%2FOCwJDQq3ANdnWGyAQSg08IK5WqUvTHabyAOWhyRESfDvpRKAZmXt%2BXnJ%2BVHnKY20k1Jzb6CxOFPk32fyV75Aj9GoD6IL7krx6P6Dg4%2FpvKJ7iNvHWERh%2F%2FN9%2FUmp4KAxld5PGETKOVKaho%2Bpm152kd%2Fw6KIZmjdiTggm51GHHyUHr1EHO%2By9LsVI8Pt1h9dlsqFmhSXlSStaUP45yK9UyELlUFaR6IivzosJTCif%2BJKxdMPqj9XNa3a3q%2FVeqsMi9VYC9MmxP5YdavKY1TT0E4872e96DuJm8cW8tlOYskXm%2FuWQVxMT6herqTSEWGkWIggkqK0dcxlD%2FMXI0Ca0zh5AqDAV6VWKv%2BZRKXcnTHWK%2BmIvoRmizoJuubdX4eRGgzGHcZ%2FM6UPEtc6qfbnPse0Cs%2Bj%2Fl%2FxgBxIJnt0iGMnTcO71MeuxtW%2FgULqH5lACb4HwysbsnYw1PHPq0rWOr7hEtzK3E%2FPd0MLwPs9PUheZuhY024xdLutvFBbz9E9X6QimGaZeCkYdGfyQii%2B6tKcWBAPbCVIQawItdTuEe99sO1K7Q%2FYKpQFwz7wjoRPw%2BKfjWlYV5eEjCuuK%2BuIp8kec2YdQ1MNb2mb48BA4cLrmi0sxk%2F29ImS7uLHlBsNK3orAzDb%2FvG8BjqkAXE7QB3mbzbISsbNtJOdySnXLzLZoH%2BclWtCMrg7vr9dIrvsR1pcFEDl%2FftTM6ooEDhTGZvpHWekQfPUmEcfxpck0Dkf11A7golMnbfZq9pSwlWfTOCuJVMBRDKyLXaITSzljA0O4ToJ%2BTq8zCBc8gm4JJ7ZtkcF9iCQlXmqDSC%2Fww9y5gtwrQz1jhdlplAYsB1SKvXBOT%2FxnfJxQaLczrxfl%2BpQ&X-Amz-Signature=981433e8dcf1c70803bafa625ec74e3caf3a13d9d07b3b2b3bc1c41bec18782b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SSYHC34%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081842Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDbofWR70zoBdgYNo3A5SyAgzWXvt9%2F1mgJLEZPioK85wIhAOyRkGmE7%2BAVIXemBbolF822AqHLuTYzF7%2FRu070IdvNKogECLn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyxKo709E1b%2FOCwJDQq3ANdnWGyAQSg08IK5WqUvTHabyAOWhyRESfDvpRKAZmXt%2BXnJ%2BVHnKY20k1Jzb6CxOFPk32fyV75Aj9GoD6IL7krx6P6Dg4%2FpvKJ7iNvHWERh%2F%2FN9%2FUmp4KAxld5PGETKOVKaho%2Bpm152kd%2Fw6KIZmjdiTggm51GHHyUHr1EHO%2By9LsVI8Pt1h9dlsqFmhSXlSStaUP45yK9UyELlUFaR6IivzosJTCif%2BJKxdMPqj9XNa3a3q%2FVeqsMi9VYC9MmxP5YdavKY1TT0E4872e96DuJm8cW8tlOYskXm%2FuWQVxMT6herqTSEWGkWIggkqK0dcxlD%2FMXI0Ca0zh5AqDAV6VWKv%2BZRKXcnTHWK%2BmIvoRmizoJuubdX4eRGgzGHcZ%2FM6UPEtc6qfbnPse0Cs%2Bj%2Fl%2FxgBxIJnt0iGMnTcO71MeuxtW%2FgULqH5lACb4HwysbsnYw1PHPq0rWOr7hEtzK3E%2FPd0MLwPs9PUheZuhY024xdLutvFBbz9E9X6QimGaZeCkYdGfyQii%2B6tKcWBAPbCVIQawItdTuEe99sO1K7Q%2FYKpQFwz7wjoRPw%2BKfjWlYV5eEjCuuK%2BuIp8kec2YdQ1MNb2mb48BA4cLrmi0sxk%2F29ImS7uLHlBsNK3orAzDb%2FvG8BjqkAXE7QB3mbzbISsbNtJOdySnXLzLZoH%2BclWtCMrg7vr9dIrvsR1pcFEDl%2FftTM6ooEDhTGZvpHWekQfPUmEcfxpck0Dkf11A7golMnbfZq9pSwlWfTOCuJVMBRDKyLXaITSzljA0O4ToJ%2BTq8zCBc8gm4JJ7ZtkcF9iCQlXmqDSC%2Fww9y5gtwrQz1jhdlplAYsB1SKvXBOT%2FxnfJxQaLczrxfl%2BpQ&X-Amz-Signature=8f92639f65d21eb54213935ad0841fc2a3679823698108c108bba9ef3ae0705c&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SSYHC34%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081842Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDbofWR70zoBdgYNo3A5SyAgzWXvt9%2F1mgJLEZPioK85wIhAOyRkGmE7%2BAVIXemBbolF822AqHLuTYzF7%2FRu070IdvNKogECLn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyxKo709E1b%2FOCwJDQq3ANdnWGyAQSg08IK5WqUvTHabyAOWhyRESfDvpRKAZmXt%2BXnJ%2BVHnKY20k1Jzb6CxOFPk32fyV75Aj9GoD6IL7krx6P6Dg4%2FpvKJ7iNvHWERh%2F%2FN9%2FUmp4KAxld5PGETKOVKaho%2Bpm152kd%2Fw6KIZmjdiTggm51GHHyUHr1EHO%2By9LsVI8Pt1h9dlsqFmhSXlSStaUP45yK9UyELlUFaR6IivzosJTCif%2BJKxdMPqj9XNa3a3q%2FVeqsMi9VYC9MmxP5YdavKY1TT0E4872e96DuJm8cW8tlOYskXm%2FuWQVxMT6herqTSEWGkWIggkqK0dcxlD%2FMXI0Ca0zh5AqDAV6VWKv%2BZRKXcnTHWK%2BmIvoRmizoJuubdX4eRGgzGHcZ%2FM6UPEtc6qfbnPse0Cs%2Bj%2Fl%2FxgBxIJnt0iGMnTcO71MeuxtW%2FgULqH5lACb4HwysbsnYw1PHPq0rWOr7hEtzK3E%2FPd0MLwPs9PUheZuhY024xdLutvFBbz9E9X6QimGaZeCkYdGfyQii%2B6tKcWBAPbCVIQawItdTuEe99sO1K7Q%2FYKpQFwz7wjoRPw%2BKfjWlYV5eEjCuuK%2BuIp8kec2YdQ1MNb2mb48BA4cLrmi0sxk%2F29ImS7uLHlBsNK3orAzDb%2FvG8BjqkAXE7QB3mbzbISsbNtJOdySnXLzLZoH%2BclWtCMrg7vr9dIrvsR1pcFEDl%2FftTM6ooEDhTGZvpHWekQfPUmEcfxpck0Dkf11A7golMnbfZq9pSwlWfTOCuJVMBRDKyLXaITSzljA0O4ToJ%2BTq8zCBc8gm4JJ7ZtkcF9iCQlXmqDSC%2Fww9y5gtwrQz1jhdlplAYsB1SKvXBOT%2FxnfJxQaLczrxfl%2BpQ&X-Amz-Signature=7c459e0540884b04a3a2c357695bc3a1e7ea7727305a5bf25501463c321be440&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SSYHC34%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081842Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDbofWR70zoBdgYNo3A5SyAgzWXvt9%2F1mgJLEZPioK85wIhAOyRkGmE7%2BAVIXemBbolF822AqHLuTYzF7%2FRu070IdvNKogECLn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyxKo709E1b%2FOCwJDQq3ANdnWGyAQSg08IK5WqUvTHabyAOWhyRESfDvpRKAZmXt%2BXnJ%2BVHnKY20k1Jzb6CxOFPk32fyV75Aj9GoD6IL7krx6P6Dg4%2FpvKJ7iNvHWERh%2F%2FN9%2FUmp4KAxld5PGETKOVKaho%2Bpm152kd%2Fw6KIZmjdiTggm51GHHyUHr1EHO%2By9LsVI8Pt1h9dlsqFmhSXlSStaUP45yK9UyELlUFaR6IivzosJTCif%2BJKxdMPqj9XNa3a3q%2FVeqsMi9VYC9MmxP5YdavKY1TT0E4872e96DuJm8cW8tlOYskXm%2FuWQVxMT6herqTSEWGkWIggkqK0dcxlD%2FMXI0Ca0zh5AqDAV6VWKv%2BZRKXcnTHWK%2BmIvoRmizoJuubdX4eRGgzGHcZ%2FM6UPEtc6qfbnPse0Cs%2Bj%2Fl%2FxgBxIJnt0iGMnTcO71MeuxtW%2FgULqH5lACb4HwysbsnYw1PHPq0rWOr7hEtzK3E%2FPd0MLwPs9PUheZuhY024xdLutvFBbz9E9X6QimGaZeCkYdGfyQii%2B6tKcWBAPbCVIQawItdTuEe99sO1K7Q%2FYKpQFwz7wjoRPw%2BKfjWlYV5eEjCuuK%2BuIp8kec2YdQ1MNb2mb48BA4cLrmi0sxk%2F29ImS7uLHlBsNK3orAzDb%2FvG8BjqkAXE7QB3mbzbISsbNtJOdySnXLzLZoH%2BclWtCMrg7vr9dIrvsR1pcFEDl%2FftTM6ooEDhTGZvpHWekQfPUmEcfxpck0Dkf11A7golMnbfZq9pSwlWfTOCuJVMBRDKyLXaITSzljA0O4ToJ%2BTq8zCBc8gm4JJ7ZtkcF9iCQlXmqDSC%2Fww9y5gtwrQz1jhdlplAYsB1SKvXBOT%2FxnfJxQaLczrxfl%2BpQ&X-Amz-Signature=86f8ca9bdee7cc19a74b56b3eaf8e2845c67e7909dd19f0c0926b00a648dee88&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SSYHC34%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081842Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDbofWR70zoBdgYNo3A5SyAgzWXvt9%2F1mgJLEZPioK85wIhAOyRkGmE7%2BAVIXemBbolF822AqHLuTYzF7%2FRu070IdvNKogECLn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyxKo709E1b%2FOCwJDQq3ANdnWGyAQSg08IK5WqUvTHabyAOWhyRESfDvpRKAZmXt%2BXnJ%2BVHnKY20k1Jzb6CxOFPk32fyV75Aj9GoD6IL7krx6P6Dg4%2FpvKJ7iNvHWERh%2F%2FN9%2FUmp4KAxld5PGETKOVKaho%2Bpm152kd%2Fw6KIZmjdiTggm51GHHyUHr1EHO%2By9LsVI8Pt1h9dlsqFmhSXlSStaUP45yK9UyELlUFaR6IivzosJTCif%2BJKxdMPqj9XNa3a3q%2FVeqsMi9VYC9MmxP5YdavKY1TT0E4872e96DuJm8cW8tlOYskXm%2FuWQVxMT6herqTSEWGkWIggkqK0dcxlD%2FMXI0Ca0zh5AqDAV6VWKv%2BZRKXcnTHWK%2BmIvoRmizoJuubdX4eRGgzGHcZ%2FM6UPEtc6qfbnPse0Cs%2Bj%2Fl%2FxgBxIJnt0iGMnTcO71MeuxtW%2FgULqH5lACb4HwysbsnYw1PHPq0rWOr7hEtzK3E%2FPd0MLwPs9PUheZuhY024xdLutvFBbz9E9X6QimGaZeCkYdGfyQii%2B6tKcWBAPbCVIQawItdTuEe99sO1K7Q%2FYKpQFwz7wjoRPw%2BKfjWlYV5eEjCuuK%2BuIp8kec2YdQ1MNb2mb48BA4cLrmi0sxk%2F29ImS7uLHlBsNK3orAzDb%2FvG8BjqkAXE7QB3mbzbISsbNtJOdySnXLzLZoH%2BclWtCMrg7vr9dIrvsR1pcFEDl%2FftTM6ooEDhTGZvpHWekQfPUmEcfxpck0Dkf11A7golMnbfZq9pSwlWfTOCuJVMBRDKyLXaITSzljA0O4ToJ%2BTq8zCBc8gm4JJ7ZtkcF9iCQlXmqDSC%2Fww9y5gtwrQz1jhdlplAYsB1SKvXBOT%2FxnfJxQaLczrxfl%2BpQ&X-Amz-Signature=8b2ed32b288e78c04a5246e303e473efa7019c418295549e66e27faf01a8f8d6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SSYHC34%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081842Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDbofWR70zoBdgYNo3A5SyAgzWXvt9%2F1mgJLEZPioK85wIhAOyRkGmE7%2BAVIXemBbolF822AqHLuTYzF7%2FRu070IdvNKogECLn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyxKo709E1b%2FOCwJDQq3ANdnWGyAQSg08IK5WqUvTHabyAOWhyRESfDvpRKAZmXt%2BXnJ%2BVHnKY20k1Jzb6CxOFPk32fyV75Aj9GoD6IL7krx6P6Dg4%2FpvKJ7iNvHWERh%2F%2FN9%2FUmp4KAxld5PGETKOVKaho%2Bpm152kd%2Fw6KIZmjdiTggm51GHHyUHr1EHO%2By9LsVI8Pt1h9dlsqFmhSXlSStaUP45yK9UyELlUFaR6IivzosJTCif%2BJKxdMPqj9XNa3a3q%2FVeqsMi9VYC9MmxP5YdavKY1TT0E4872e96DuJm8cW8tlOYskXm%2FuWQVxMT6herqTSEWGkWIggkqK0dcxlD%2FMXI0Ca0zh5AqDAV6VWKv%2BZRKXcnTHWK%2BmIvoRmizoJuubdX4eRGgzGHcZ%2FM6UPEtc6qfbnPse0Cs%2Bj%2Fl%2FxgBxIJnt0iGMnTcO71MeuxtW%2FgULqH5lACb4HwysbsnYw1PHPq0rWOr7hEtzK3E%2FPd0MLwPs9PUheZuhY024xdLutvFBbz9E9X6QimGaZeCkYdGfyQii%2B6tKcWBAPbCVIQawItdTuEe99sO1K7Q%2FYKpQFwz7wjoRPw%2BKfjWlYV5eEjCuuK%2BuIp8kec2YdQ1MNb2mb48BA4cLrmi0sxk%2F29ImS7uLHlBsNK3orAzDb%2FvG8BjqkAXE7QB3mbzbISsbNtJOdySnXLzLZoH%2BclWtCMrg7vr9dIrvsR1pcFEDl%2FftTM6ooEDhTGZvpHWekQfPUmEcfxpck0Dkf11A7golMnbfZq9pSwlWfTOCuJVMBRDKyLXaITSzljA0O4ToJ%2BTq8zCBc8gm4JJ7ZtkcF9iCQlXmqDSC%2Fww9y5gtwrQz1jhdlplAYsB1SKvXBOT%2FxnfJxQaLczrxfl%2BpQ&X-Amz-Signature=e95d2519acb0a236322180f44bf8a61972bf11571b4351f8dba15a598d6feb5a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMHAY5VA%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081842Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCSbt0mrXcvVytd8Zj0%2FNLx6wjWC2Zfm%2BaMcygGHODfQwIhAIeNa2ypzJW2bLHJPvH%2FpX7fXqP7Pbuv9%2B3BziBN4oM3KogECLn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwISbDxfPj7kUxkNsQq3APrqgeKMQ%2Fu0yzXedQkoH6KFsEKq0q%2FKMtLHcnuWHIlkegvpSyL6TBd1MySJssgiRbbyccvBHWSMCog4LiF76Hx9%2B%2B7%2BXUwoEFzoWINbJNGb%2BxwIzQ%2Bu9JiN29mhJAXe3g0EGJGbQfiRIE32YSuQwNmxcpM42%2FOpV6Uu53PJAJjYBN0aCsaOauuL0Nn3zxWfZ%2FQte48xKtvCwPrFK%2Bm7PWeb29lUhbdTQYgds%2FH%2FKjJjQstAXYP3vvQahDoFzNF2DDJyE%2F%2BeU3Ki1GM%2B%2FXNqACm%2FHylHvZHrwGsxqdlHQWU%2FFvrWPZEsOfuqMYJNezMDDITfL2olQov%2Bbx6fWuON0v1MKuCYm3UzOIh%2F9r8%2B54T5n70cmquE2N%2BjUASc9L%2F2UFbPRdwnFGz8yc21SWV%2BRSemvOUDpOTbTjafuhNGM%2B14UxSAAPiTy9g1BHQsOPRCPHry4WGB0Eb57%2FL7LoPhvrpLxM9ov3xTvAeJGklxBpT4ojFwopm7Rfsl%2F1jIZnS2I1lUn0cAXJZZHflosQdJZmbQj8MvN3V5mxOJip2PG0pCfeL5X07NqL6QWyBefrCTDS2KyY2bh2Gn5eM06NO%2Bp2M7x7o2OSj%2Fbnx7WMw%2BqcVO%2B9OfiTw5ctUX8FG7jDX%2FfG8BjqkAQaBPthrzlQApiGnLy96DE6%2F45bgI0h5mFy120Y6rF08Wm%2F7DHG18988IrStrQYvX%2FWeO1GSMg5F7BooAokwVXkkFvJ%2BFoI0HWpCSO%2BOXvr2jsq0z64amzavRiwIr7CK%2FsuPpq9M7%2FKC0DMbRyhePYnNHtpBlESkibkxnkq5J27I1ZqKIEupqBsO%2BjmBOpUNFQueNH6Mv9FtLpAeWMQYALuXhwTr&X-Amz-Signature=559e0f8868c6fd48b917e85baebfa3ecfea2a1d6a761e4515e96d4bd6025b4c4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMHAY5VA%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081842Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCSbt0mrXcvVytd8Zj0%2FNLx6wjWC2Zfm%2BaMcygGHODfQwIhAIeNa2ypzJW2bLHJPvH%2FpX7fXqP7Pbuv9%2B3BziBN4oM3KogECLn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwISbDxfPj7kUxkNsQq3APrqgeKMQ%2Fu0yzXedQkoH6KFsEKq0q%2FKMtLHcnuWHIlkegvpSyL6TBd1MySJssgiRbbyccvBHWSMCog4LiF76Hx9%2B%2B7%2BXUwoEFzoWINbJNGb%2BxwIzQ%2Bu9JiN29mhJAXe3g0EGJGbQfiRIE32YSuQwNmxcpM42%2FOpV6Uu53PJAJjYBN0aCsaOauuL0Nn3zxWfZ%2FQte48xKtvCwPrFK%2Bm7PWeb29lUhbdTQYgds%2FH%2FKjJjQstAXYP3vvQahDoFzNF2DDJyE%2F%2BeU3Ki1GM%2B%2FXNqACm%2FHylHvZHrwGsxqdlHQWU%2FFvrWPZEsOfuqMYJNezMDDITfL2olQov%2Bbx6fWuON0v1MKuCYm3UzOIh%2F9r8%2B54T5n70cmquE2N%2BjUASc9L%2F2UFbPRdwnFGz8yc21SWV%2BRSemvOUDpOTbTjafuhNGM%2B14UxSAAPiTy9g1BHQsOPRCPHry4WGB0Eb57%2FL7LoPhvrpLxM9ov3xTvAeJGklxBpT4ojFwopm7Rfsl%2F1jIZnS2I1lUn0cAXJZZHflosQdJZmbQj8MvN3V5mxOJip2PG0pCfeL5X07NqL6QWyBefrCTDS2KyY2bh2Gn5eM06NO%2Bp2M7x7o2OSj%2Fbnx7WMw%2BqcVO%2B9OfiTw5ctUX8FG7jDX%2FfG8BjqkAQaBPthrzlQApiGnLy96DE6%2F45bgI0h5mFy120Y6rF08Wm%2F7DHG18988IrStrQYvX%2FWeO1GSMg5F7BooAokwVXkkFvJ%2BFoI0HWpCSO%2BOXvr2jsq0z64amzavRiwIr7CK%2FsuPpq9M7%2FKC0DMbRyhePYnNHtpBlESkibkxnkq5J27I1ZqKIEupqBsO%2BjmBOpUNFQueNH6Mv9FtLpAeWMQYALuXhwTr&X-Amz-Signature=03120d321a9361f939e655bc800f704b1d66308c4396c18b8fdcb1888c51cfae&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
