

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNT7BWUC%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJIMEYCIQDSIe778%2BYF1BX2oYh923QQM1IOr%2FOM5h6AuEJrO37d6wIhAICvOYalpoeezC8aFBjsfqwEsxT719Lqm4gLzDG9wClbKv8DCCIQABoMNjM3NDIzMTgzODA1Igw3zAHXTFOLAu2MA3Eq3AMCH4Iynevyy3%2FvIC17a9zoNqScM6fQcNQX308coNY%2FeZ7UK1unmk7HK1di8%2BxL5uEE7yvad9WRlsi%2FqgtYSTohQsUf2rXgo%2F4n7bMIbGUSLy5KTx7anKGacYmXBlFWr2TnoUc7fYtqINVoT1VnBQIbJS3RlMj0GLWIxMarS%2BrsCrSljsreNgZoXWvHpBWNBDwJjGUMBBvpj96Q7HJERpNfv66dB%2BN58w64zBUC3I4K3BlSVKqM5dnc7tWh9oAnUJME1d%2BmZM0PkWlm0R6%2F4OoqS1GGl32wanIJDn0DG2vQOJD%2Fi%2B6hTIbGOXJj%2BZaDwe07qUIZSfX91JMdV8XSaotlKygARK15roo7ADF7%2BVmqI9QKdMgQGngxta%2Br%2BO%2F87PVsELDqWNWl3I7zCRk2DsQRxy%2FWE%2FgddOiGS9BJEfGFAkmkvoSLAWttzZicgsHRKqYwrJz9CMCHemS70bkH86qxvX%2F4Fofc2xjFPo%2FpUf0S8kZIr%2B5Cw55aAe%2F3K6eRuxW47GoeUeZcFv7UtTqIhJZcibJkFC4T51vte05bC34P6JgEMzGDSlfL9pdLJUF9Oo8%2FmhSCnfnIu4SlwSRWp3dhgMqnY2ni6nA%2FqmgAwAaePCAqZ0h5BESEgQF44jCvzYW9BjqkAZSJ2Wh4F1vD9rbXjYxOkNIKmH8USWAZig8wbMuR8oCSW5lM9AUw%2FxkSxPzp0kcKPTrO%2BqzJ7upTIT%2BgfB2PjSdYTCeBduC0%2BaKDAc7Zr%2B1PWofqr9dsJXnJkzZrSFxy817U%2FO%2FV05zf9N1yISdQobma7JvkN17cgm1jGTqGEN20yG8mpYl624FmDY1tRQMakHB4Sowdfpf3CeNJInAp2PXGl6IU&X-Amz-Signature=bf118867c4e87626e615124dfeed7f2bc07921b77529b9edab36f1f1d6572fb6&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNT7BWUC%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJIMEYCIQDSIe778%2BYF1BX2oYh923QQM1IOr%2FOM5h6AuEJrO37d6wIhAICvOYalpoeezC8aFBjsfqwEsxT719Lqm4gLzDG9wClbKv8DCCIQABoMNjM3NDIzMTgzODA1Igw3zAHXTFOLAu2MA3Eq3AMCH4Iynevyy3%2FvIC17a9zoNqScM6fQcNQX308coNY%2FeZ7UK1unmk7HK1di8%2BxL5uEE7yvad9WRlsi%2FqgtYSTohQsUf2rXgo%2F4n7bMIbGUSLy5KTx7anKGacYmXBlFWr2TnoUc7fYtqINVoT1VnBQIbJS3RlMj0GLWIxMarS%2BrsCrSljsreNgZoXWvHpBWNBDwJjGUMBBvpj96Q7HJERpNfv66dB%2BN58w64zBUC3I4K3BlSVKqM5dnc7tWh9oAnUJME1d%2BmZM0PkWlm0R6%2F4OoqS1GGl32wanIJDn0DG2vQOJD%2Fi%2B6hTIbGOXJj%2BZaDwe07qUIZSfX91JMdV8XSaotlKygARK15roo7ADF7%2BVmqI9QKdMgQGngxta%2Br%2BO%2F87PVsELDqWNWl3I7zCRk2DsQRxy%2FWE%2FgddOiGS9BJEfGFAkmkvoSLAWttzZicgsHRKqYwrJz9CMCHemS70bkH86qxvX%2F4Fofc2xjFPo%2FpUf0S8kZIr%2B5Cw55aAe%2F3K6eRuxW47GoeUeZcFv7UtTqIhJZcibJkFC4T51vte05bC34P6JgEMzGDSlfL9pdLJUF9Oo8%2FmhSCnfnIu4SlwSRWp3dhgMqnY2ni6nA%2FqmgAwAaePCAqZ0h5BESEgQF44jCvzYW9BjqkAZSJ2Wh4F1vD9rbXjYxOkNIKmH8USWAZig8wbMuR8oCSW5lM9AUw%2FxkSxPzp0kcKPTrO%2BqzJ7upTIT%2BgfB2PjSdYTCeBduC0%2BaKDAc7Zr%2B1PWofqr9dsJXnJkzZrSFxy817U%2FO%2FV05zf9N1yISdQobma7JvkN17cgm1jGTqGEN20yG8mpYl624FmDY1tRQMakHB4Sowdfpf3CeNJInAp2PXGl6IU&X-Amz-Signature=921630928d5d3a728fac709ee88cf67c9261e40e412349f684f12f08ea1af875&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNT7BWUC%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJIMEYCIQDSIe778%2BYF1BX2oYh923QQM1IOr%2FOM5h6AuEJrO37d6wIhAICvOYalpoeezC8aFBjsfqwEsxT719Lqm4gLzDG9wClbKv8DCCIQABoMNjM3NDIzMTgzODA1Igw3zAHXTFOLAu2MA3Eq3AMCH4Iynevyy3%2FvIC17a9zoNqScM6fQcNQX308coNY%2FeZ7UK1unmk7HK1di8%2BxL5uEE7yvad9WRlsi%2FqgtYSTohQsUf2rXgo%2F4n7bMIbGUSLy5KTx7anKGacYmXBlFWr2TnoUc7fYtqINVoT1VnBQIbJS3RlMj0GLWIxMarS%2BrsCrSljsreNgZoXWvHpBWNBDwJjGUMBBvpj96Q7HJERpNfv66dB%2BN58w64zBUC3I4K3BlSVKqM5dnc7tWh9oAnUJME1d%2BmZM0PkWlm0R6%2F4OoqS1GGl32wanIJDn0DG2vQOJD%2Fi%2B6hTIbGOXJj%2BZaDwe07qUIZSfX91JMdV8XSaotlKygARK15roo7ADF7%2BVmqI9QKdMgQGngxta%2Br%2BO%2F87PVsELDqWNWl3I7zCRk2DsQRxy%2FWE%2FgddOiGS9BJEfGFAkmkvoSLAWttzZicgsHRKqYwrJz9CMCHemS70bkH86qxvX%2F4Fofc2xjFPo%2FpUf0S8kZIr%2B5Cw55aAe%2F3K6eRuxW47GoeUeZcFv7UtTqIhJZcibJkFC4T51vte05bC34P6JgEMzGDSlfL9pdLJUF9Oo8%2FmhSCnfnIu4SlwSRWp3dhgMqnY2ni6nA%2FqmgAwAaePCAqZ0h5BESEgQF44jCvzYW9BjqkAZSJ2Wh4F1vD9rbXjYxOkNIKmH8USWAZig8wbMuR8oCSW5lM9AUw%2FxkSxPzp0kcKPTrO%2BqzJ7upTIT%2BgfB2PjSdYTCeBduC0%2BaKDAc7Zr%2B1PWofqr9dsJXnJkzZrSFxy817U%2FO%2FV05zf9N1yISdQobma7JvkN17cgm1jGTqGEN20yG8mpYl624FmDY1tRQMakHB4Sowdfpf3CeNJInAp2PXGl6IU&X-Amz-Signature=36e69b426ec9da9e0f1b8320445598fdece0d6d47267c27596abfe930211a80a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNT7BWUC%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJIMEYCIQDSIe778%2BYF1BX2oYh923QQM1IOr%2FOM5h6AuEJrO37d6wIhAICvOYalpoeezC8aFBjsfqwEsxT719Lqm4gLzDG9wClbKv8DCCIQABoMNjM3NDIzMTgzODA1Igw3zAHXTFOLAu2MA3Eq3AMCH4Iynevyy3%2FvIC17a9zoNqScM6fQcNQX308coNY%2FeZ7UK1unmk7HK1di8%2BxL5uEE7yvad9WRlsi%2FqgtYSTohQsUf2rXgo%2F4n7bMIbGUSLy5KTx7anKGacYmXBlFWr2TnoUc7fYtqINVoT1VnBQIbJS3RlMj0GLWIxMarS%2BrsCrSljsreNgZoXWvHpBWNBDwJjGUMBBvpj96Q7HJERpNfv66dB%2BN58w64zBUC3I4K3BlSVKqM5dnc7tWh9oAnUJME1d%2BmZM0PkWlm0R6%2F4OoqS1GGl32wanIJDn0DG2vQOJD%2Fi%2B6hTIbGOXJj%2BZaDwe07qUIZSfX91JMdV8XSaotlKygARK15roo7ADF7%2BVmqI9QKdMgQGngxta%2Br%2BO%2F87PVsELDqWNWl3I7zCRk2DsQRxy%2FWE%2FgddOiGS9BJEfGFAkmkvoSLAWttzZicgsHRKqYwrJz9CMCHemS70bkH86qxvX%2F4Fofc2xjFPo%2FpUf0S8kZIr%2B5Cw55aAe%2F3K6eRuxW47GoeUeZcFv7UtTqIhJZcibJkFC4T51vte05bC34P6JgEMzGDSlfL9pdLJUF9Oo8%2FmhSCnfnIu4SlwSRWp3dhgMqnY2ni6nA%2FqmgAwAaePCAqZ0h5BESEgQF44jCvzYW9BjqkAZSJ2Wh4F1vD9rbXjYxOkNIKmH8USWAZig8wbMuR8oCSW5lM9AUw%2FxkSxPzp0kcKPTrO%2BqzJ7upTIT%2BgfB2PjSdYTCeBduC0%2BaKDAc7Zr%2B1PWofqr9dsJXnJkzZrSFxy817U%2FO%2FV05zf9N1yISdQobma7JvkN17cgm1jGTqGEN20yG8mpYl624FmDY1tRQMakHB4Sowdfpf3CeNJInAp2PXGl6IU&X-Amz-Signature=2d52bcccdc8f01e84fd77a02920b20e35f6b2061be7487b40a63b2addc13d9be&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNT7BWUC%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJIMEYCIQDSIe778%2BYF1BX2oYh923QQM1IOr%2FOM5h6AuEJrO37d6wIhAICvOYalpoeezC8aFBjsfqwEsxT719Lqm4gLzDG9wClbKv8DCCIQABoMNjM3NDIzMTgzODA1Igw3zAHXTFOLAu2MA3Eq3AMCH4Iynevyy3%2FvIC17a9zoNqScM6fQcNQX308coNY%2FeZ7UK1unmk7HK1di8%2BxL5uEE7yvad9WRlsi%2FqgtYSTohQsUf2rXgo%2F4n7bMIbGUSLy5KTx7anKGacYmXBlFWr2TnoUc7fYtqINVoT1VnBQIbJS3RlMj0GLWIxMarS%2BrsCrSljsreNgZoXWvHpBWNBDwJjGUMBBvpj96Q7HJERpNfv66dB%2BN58w64zBUC3I4K3BlSVKqM5dnc7tWh9oAnUJME1d%2BmZM0PkWlm0R6%2F4OoqS1GGl32wanIJDn0DG2vQOJD%2Fi%2B6hTIbGOXJj%2BZaDwe07qUIZSfX91JMdV8XSaotlKygARK15roo7ADF7%2BVmqI9QKdMgQGngxta%2Br%2BO%2F87PVsELDqWNWl3I7zCRk2DsQRxy%2FWE%2FgddOiGS9BJEfGFAkmkvoSLAWttzZicgsHRKqYwrJz9CMCHemS70bkH86qxvX%2F4Fofc2xjFPo%2FpUf0S8kZIr%2B5Cw55aAe%2F3K6eRuxW47GoeUeZcFv7UtTqIhJZcibJkFC4T51vte05bC34P6JgEMzGDSlfL9pdLJUF9Oo8%2FmhSCnfnIu4SlwSRWp3dhgMqnY2ni6nA%2FqmgAwAaePCAqZ0h5BESEgQF44jCvzYW9BjqkAZSJ2Wh4F1vD9rbXjYxOkNIKmH8USWAZig8wbMuR8oCSW5lM9AUw%2FxkSxPzp0kcKPTrO%2BqzJ7upTIT%2BgfB2PjSdYTCeBduC0%2BaKDAc7Zr%2B1PWofqr9dsJXnJkzZrSFxy817U%2FO%2FV05zf9N1yISdQobma7JvkN17cgm1jGTqGEN20yG8mpYl624FmDY1tRQMakHB4Sowdfpf3CeNJInAp2PXGl6IU&X-Amz-Signature=f22fcec86df4f2d5642e8a22094388e3643f492805ac36699a7e38e2bf9300c3&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNT7BWUC%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJIMEYCIQDSIe778%2BYF1BX2oYh923QQM1IOr%2FOM5h6AuEJrO37d6wIhAICvOYalpoeezC8aFBjsfqwEsxT719Lqm4gLzDG9wClbKv8DCCIQABoMNjM3NDIzMTgzODA1Igw3zAHXTFOLAu2MA3Eq3AMCH4Iynevyy3%2FvIC17a9zoNqScM6fQcNQX308coNY%2FeZ7UK1unmk7HK1di8%2BxL5uEE7yvad9WRlsi%2FqgtYSTohQsUf2rXgo%2F4n7bMIbGUSLy5KTx7anKGacYmXBlFWr2TnoUc7fYtqINVoT1VnBQIbJS3RlMj0GLWIxMarS%2BrsCrSljsreNgZoXWvHpBWNBDwJjGUMBBvpj96Q7HJERpNfv66dB%2BN58w64zBUC3I4K3BlSVKqM5dnc7tWh9oAnUJME1d%2BmZM0PkWlm0R6%2F4OoqS1GGl32wanIJDn0DG2vQOJD%2Fi%2B6hTIbGOXJj%2BZaDwe07qUIZSfX91JMdV8XSaotlKygARK15roo7ADF7%2BVmqI9QKdMgQGngxta%2Br%2BO%2F87PVsELDqWNWl3I7zCRk2DsQRxy%2FWE%2FgddOiGS9BJEfGFAkmkvoSLAWttzZicgsHRKqYwrJz9CMCHemS70bkH86qxvX%2F4Fofc2xjFPo%2FpUf0S8kZIr%2B5Cw55aAe%2F3K6eRuxW47GoeUeZcFv7UtTqIhJZcibJkFC4T51vte05bC34P6JgEMzGDSlfL9pdLJUF9Oo8%2FmhSCnfnIu4SlwSRWp3dhgMqnY2ni6nA%2FqmgAwAaePCAqZ0h5BESEgQF44jCvzYW9BjqkAZSJ2Wh4F1vD9rbXjYxOkNIKmH8USWAZig8wbMuR8oCSW5lM9AUw%2FxkSxPzp0kcKPTrO%2BqzJ7upTIT%2BgfB2PjSdYTCeBduC0%2BaKDAc7Zr%2B1PWofqr9dsJXnJkzZrSFxy817U%2FO%2FV05zf9N1yISdQobma7JvkN17cgm1jGTqGEN20yG8mpYl624FmDY1tRQMakHB4Sowdfpf3CeNJInAp2PXGl6IU&X-Amz-Signature=1522e8ea6579f6c080592bef94e92d0739564a07bfed7e641ee897c47919736e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNT7BWUC%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJIMEYCIQDSIe778%2BYF1BX2oYh923QQM1IOr%2FOM5h6AuEJrO37d6wIhAICvOYalpoeezC8aFBjsfqwEsxT719Lqm4gLzDG9wClbKv8DCCIQABoMNjM3NDIzMTgzODA1Igw3zAHXTFOLAu2MA3Eq3AMCH4Iynevyy3%2FvIC17a9zoNqScM6fQcNQX308coNY%2FeZ7UK1unmk7HK1di8%2BxL5uEE7yvad9WRlsi%2FqgtYSTohQsUf2rXgo%2F4n7bMIbGUSLy5KTx7anKGacYmXBlFWr2TnoUc7fYtqINVoT1VnBQIbJS3RlMj0GLWIxMarS%2BrsCrSljsreNgZoXWvHpBWNBDwJjGUMBBvpj96Q7HJERpNfv66dB%2BN58w64zBUC3I4K3BlSVKqM5dnc7tWh9oAnUJME1d%2BmZM0PkWlm0R6%2F4OoqS1GGl32wanIJDn0DG2vQOJD%2Fi%2B6hTIbGOXJj%2BZaDwe07qUIZSfX91JMdV8XSaotlKygARK15roo7ADF7%2BVmqI9QKdMgQGngxta%2Br%2BO%2F87PVsELDqWNWl3I7zCRk2DsQRxy%2FWE%2FgddOiGS9BJEfGFAkmkvoSLAWttzZicgsHRKqYwrJz9CMCHemS70bkH86qxvX%2F4Fofc2xjFPo%2FpUf0S8kZIr%2B5Cw55aAe%2F3K6eRuxW47GoeUeZcFv7UtTqIhJZcibJkFC4T51vte05bC34P6JgEMzGDSlfL9pdLJUF9Oo8%2FmhSCnfnIu4SlwSRWp3dhgMqnY2ni6nA%2FqmgAwAaePCAqZ0h5BESEgQF44jCvzYW9BjqkAZSJ2Wh4F1vD9rbXjYxOkNIKmH8USWAZig8wbMuR8oCSW5lM9AUw%2FxkSxPzp0kcKPTrO%2BqzJ7upTIT%2BgfB2PjSdYTCeBduC0%2BaKDAc7Zr%2B1PWofqr9dsJXnJkzZrSFxy817U%2FO%2FV05zf9N1yISdQobma7JvkN17cgm1jGTqGEN20yG8mpYl624FmDY1tRQMakHB4Sowdfpf3CeNJInAp2PXGl6IU&X-Amz-Signature=fea06d40f998c947fc3e6af54011cf48fcf7951ec558374c8b32eb4b02a2e124&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNT7BWUC%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJIMEYCIQDSIe778%2BYF1BX2oYh923QQM1IOr%2FOM5h6AuEJrO37d6wIhAICvOYalpoeezC8aFBjsfqwEsxT719Lqm4gLzDG9wClbKv8DCCIQABoMNjM3NDIzMTgzODA1Igw3zAHXTFOLAu2MA3Eq3AMCH4Iynevyy3%2FvIC17a9zoNqScM6fQcNQX308coNY%2FeZ7UK1unmk7HK1di8%2BxL5uEE7yvad9WRlsi%2FqgtYSTohQsUf2rXgo%2F4n7bMIbGUSLy5KTx7anKGacYmXBlFWr2TnoUc7fYtqINVoT1VnBQIbJS3RlMj0GLWIxMarS%2BrsCrSljsreNgZoXWvHpBWNBDwJjGUMBBvpj96Q7HJERpNfv66dB%2BN58w64zBUC3I4K3BlSVKqM5dnc7tWh9oAnUJME1d%2BmZM0PkWlm0R6%2F4OoqS1GGl32wanIJDn0DG2vQOJD%2Fi%2B6hTIbGOXJj%2BZaDwe07qUIZSfX91JMdV8XSaotlKygARK15roo7ADF7%2BVmqI9QKdMgQGngxta%2Br%2BO%2F87PVsELDqWNWl3I7zCRk2DsQRxy%2FWE%2FgddOiGS9BJEfGFAkmkvoSLAWttzZicgsHRKqYwrJz9CMCHemS70bkH86qxvX%2F4Fofc2xjFPo%2FpUf0S8kZIr%2B5Cw55aAe%2F3K6eRuxW47GoeUeZcFv7UtTqIhJZcibJkFC4T51vte05bC34P6JgEMzGDSlfL9pdLJUF9Oo8%2FmhSCnfnIu4SlwSRWp3dhgMqnY2ni6nA%2FqmgAwAaePCAqZ0h5BESEgQF44jCvzYW9BjqkAZSJ2Wh4F1vD9rbXjYxOkNIKmH8USWAZig8wbMuR8oCSW5lM9AUw%2FxkSxPzp0kcKPTrO%2BqzJ7upTIT%2BgfB2PjSdYTCeBduC0%2BaKDAc7Zr%2B1PWofqr9dsJXnJkzZrSFxy817U%2FO%2FV05zf9N1yISdQobma7JvkN17cgm1jGTqGEN20yG8mpYl624FmDY1tRQMakHB4Sowdfpf3CeNJInAp2PXGl6IU&X-Amz-Signature=823ba3cf2d9113a599015b2e13b3cd993cad9752491c3ee83eba92bff6d53dd7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNT7BWUC%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJIMEYCIQDSIe778%2BYF1BX2oYh923QQM1IOr%2FOM5h6AuEJrO37d6wIhAICvOYalpoeezC8aFBjsfqwEsxT719Lqm4gLzDG9wClbKv8DCCIQABoMNjM3NDIzMTgzODA1Igw3zAHXTFOLAu2MA3Eq3AMCH4Iynevyy3%2FvIC17a9zoNqScM6fQcNQX308coNY%2FeZ7UK1unmk7HK1di8%2BxL5uEE7yvad9WRlsi%2FqgtYSTohQsUf2rXgo%2F4n7bMIbGUSLy5KTx7anKGacYmXBlFWr2TnoUc7fYtqINVoT1VnBQIbJS3RlMj0GLWIxMarS%2BrsCrSljsreNgZoXWvHpBWNBDwJjGUMBBvpj96Q7HJERpNfv66dB%2BN58w64zBUC3I4K3BlSVKqM5dnc7tWh9oAnUJME1d%2BmZM0PkWlm0R6%2F4OoqS1GGl32wanIJDn0DG2vQOJD%2Fi%2B6hTIbGOXJj%2BZaDwe07qUIZSfX91JMdV8XSaotlKygARK15roo7ADF7%2BVmqI9QKdMgQGngxta%2Br%2BO%2F87PVsELDqWNWl3I7zCRk2DsQRxy%2FWE%2FgddOiGS9BJEfGFAkmkvoSLAWttzZicgsHRKqYwrJz9CMCHemS70bkH86qxvX%2F4Fofc2xjFPo%2FpUf0S8kZIr%2B5Cw55aAe%2F3K6eRuxW47GoeUeZcFv7UtTqIhJZcibJkFC4T51vte05bC34P6JgEMzGDSlfL9pdLJUF9Oo8%2FmhSCnfnIu4SlwSRWp3dhgMqnY2ni6nA%2FqmgAwAaePCAqZ0h5BESEgQF44jCvzYW9BjqkAZSJ2Wh4F1vD9rbXjYxOkNIKmH8USWAZig8wbMuR8oCSW5lM9AUw%2FxkSxPzp0kcKPTrO%2BqzJ7upTIT%2BgfB2PjSdYTCeBduC0%2BaKDAc7Zr%2B1PWofqr9dsJXnJkzZrSFxy817U%2FO%2FV05zf9N1yISdQobma7JvkN17cgm1jGTqGEN20yG8mpYl624FmDY1tRQMakHB4Sowdfpf3CeNJInAp2PXGl6IU&X-Amz-Signature=3e80ec0943819be97f6181eff723d4530fa601fdf4c6011a1269dd6bd5eab07a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W42MIY4F%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJHMEUCIQC5T%2BUp7Z13MRYdI6QAyCR37X1Em9u%2F5sQJS7bXdTeX3AIgdClNO93wgBQhjtFbpeerQ183%2Bqnz7Y1FAG%2Bg3JU%2Fvwgq%2FwMIIhAAGgw2Mzc0MjMxODM4MDUiDDVvxhEOPGBKh3%2BPNCrcA568Qjs%2ByHTHN4RDiFdtQJL7klGG7vgvpok%2BJAUGJw2Vc9qzV7ajh5Mwd6Wn1hKv%2BGxX5y75F0bhplpq8EiDkmLlz1N2Aox9PQcXbYdo2R1VNI6rXku60DQ4QPXUwYm%2BKcp9sRXghr%2FXlBwT%2B7oiyO09pybwFley%2F5DtyoyscM6Z5hnVfWwSBgwod1zVBxyd6GoGugwMrf2pr3IpdF3R5NyoURrZGbYDu2ZlbNED3aOJZp9%2BfWpYBR6WZrc8pD6MAdVkmXgn4waviZrMUezWiXi2qZBNkRhRjuVP1z3rZF4ZLij3sLuUV3f1KbUfrd0BlUpIYnuIOdfJJ0PvPFkQpx4B6ijCkw73Xr6sQJ2WX9qssTbJE54bRj6pONj6feIPlOwE2IzDRvLwuy9Nk2fmGKdCI7F4ZAXMqLCpfNeI93Mj3dpWeyW62rTZXo0RDfoQSwWpDEMejb6N5fZSiZwQrgOsBBdIIupGomX%2FniVU9krSbCfhZJDS%2FnzDhtZzjOej%2FZODojtJPfe4FLcHW%2FF1wIWHpzAlhXIN8AHBcNAnj04B8aRySjdDnrgXbBg6pBfD1dUAEaHCuxaVmKyZEhSCIB6qm2dj1VtiJiR4OjCmDfNYDU9jNZMZH4dwzpBkMPTMhb0GOqUBHHGYDHE9ulLiiZoexegivz7kHXtepzG8kwNYzWOMgM8XczHrxN%2F9tLNBTPYeIxJPaKIh3aYH%2FMouIqv0nhzLItef%2FyQQx4isuuLWvWFhzlYSpAhSkToSlJWHV%2BWFl1vniouv%2BDXzVo2OdarMP%2ByTyMhfJ55i03fh%2BCQ%2FvUBJNJx7Vh32CQJ%2F20p7UWRNeCvMBdaI5QtyP%2F4Crz3WQYMOCB6nSwT9&X-Amz-Signature=25c723abac18f4418ef6d19b5193afe132629b87ed084d9b0e3ed8ebebf63d98&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W42MIY4F%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJHMEUCIQC5T%2BUp7Z13MRYdI6QAyCR37X1Em9u%2F5sQJS7bXdTeX3AIgdClNO93wgBQhjtFbpeerQ183%2Bqnz7Y1FAG%2Bg3JU%2Fvwgq%2FwMIIhAAGgw2Mzc0MjMxODM4MDUiDDVvxhEOPGBKh3%2BPNCrcA568Qjs%2ByHTHN4RDiFdtQJL7klGG7vgvpok%2BJAUGJw2Vc9qzV7ajh5Mwd6Wn1hKv%2BGxX5y75F0bhplpq8EiDkmLlz1N2Aox9PQcXbYdo2R1VNI6rXku60DQ4QPXUwYm%2BKcp9sRXghr%2FXlBwT%2B7oiyO09pybwFley%2F5DtyoyscM6Z5hnVfWwSBgwod1zVBxyd6GoGugwMrf2pr3IpdF3R5NyoURrZGbYDu2ZlbNED3aOJZp9%2BfWpYBR6WZrc8pD6MAdVkmXgn4waviZrMUezWiXi2qZBNkRhRjuVP1z3rZF4ZLij3sLuUV3f1KbUfrd0BlUpIYnuIOdfJJ0PvPFkQpx4B6ijCkw73Xr6sQJ2WX9qssTbJE54bRj6pONj6feIPlOwE2IzDRvLwuy9Nk2fmGKdCI7F4ZAXMqLCpfNeI93Mj3dpWeyW62rTZXo0RDfoQSwWpDEMejb6N5fZSiZwQrgOsBBdIIupGomX%2FniVU9krSbCfhZJDS%2FnzDhtZzjOej%2FZODojtJPfe4FLcHW%2FF1wIWHpzAlhXIN8AHBcNAnj04B8aRySjdDnrgXbBg6pBfD1dUAEaHCuxaVmKyZEhSCIB6qm2dj1VtiJiR4OjCmDfNYDU9jNZMZH4dwzpBkMPTMhb0GOqUBHHGYDHE9ulLiiZoexegivz7kHXtepzG8kwNYzWOMgM8XczHrxN%2F9tLNBTPYeIxJPaKIh3aYH%2FMouIqv0nhzLItef%2FyQQx4isuuLWvWFhzlYSpAhSkToSlJWHV%2BWFl1vniouv%2BDXzVo2OdarMP%2ByTyMhfJ55i03fh%2BCQ%2FvUBJNJx7Vh32CQJ%2F20p7UWRNeCvMBdaI5QtyP%2F4Crz3WQYMOCB6nSwT9&X-Amz-Signature=bc55a7fd8db87e36f7e2814ff8384ade006d9d505a302d23ed40656a90303b8b&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
