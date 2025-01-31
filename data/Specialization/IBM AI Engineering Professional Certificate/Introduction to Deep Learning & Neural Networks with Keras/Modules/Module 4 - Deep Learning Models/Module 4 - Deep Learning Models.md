

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664KTD5NVG%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE3xo8BC%2BspCRox2H7LhKIRFo1LhYz2CC8I4jiqcAxuiAiEAhB%2B%2FI45p92vw6OgGjm8MmEvl3KbLJNUvMxLjk21bBj0qiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBSLo7kTI%2BPLmfUwHSrcA74KquCxRSOe%2Fy9b3Ho0PAmV%2FLiE6UO8QX5RCZCNb7XP9k5LNwIuvliTHriYPemtDwqx0Re5BJBpDi3Rwisx74%2Fj1hV9MdHz25o0H5Y%2B9xMJyoVkI5M34g9n%2ByWoosDlt7yIhoJYTqddb%2BFlLg5joXvW1sdpIDDjiT2O3qyq9ivu6%2FKo%2Bnm4HeJ5YcJM9QkIZZjvWrH1qG7bhmwLybI1L8fYajDsnTr64spevW2vPVH3tdwVQZpcxIWq92TVpA9flncujS%2BXwjpWS1W2jvX2T0I0YBk5eYeXwEcfr0Gup6nRbd4hWg8eCJcfNY%2FHO6HqHsxKB97a%2BNjbcJTBgBoDxmL%2FuShAmZXmPU5Gc1mqCgW4PqtrPbKoaDozyhUdufFP%2Br3emYiRVJMd2SsEPaSR5he7tFm9yL2dc%2Fadw7F8vpjXnALOcRIonSTe2O0ranNlmcPQFsj%2B7dLrcKRSbAoksk913gsSH1ypHzQRHqJpd9vKgX0dVpbxiip0IK8KwfJUEdeo5hB2ROcaBe9M01q82DeyMdnejQM1Iy8CH2KhirqnU%2FIvFWLebtJE1LLxm6ze2thakK80tgWU%2FCbhOTa2Cuzg4s2YDl38ZvUTv0mTBOclbHuTAnuj4En9dCRBMKjQ8LwGOqUB4ELpuKdsO3DJyN%2BpTo8PDrYVpMa7t35Yib%2BcjyvVH12WAtWmVaXIV1aRc91cTx%2FLY%2BG3eu4a8Qw%2FD6CtmZ5Xl1j6xzhIWJXncSNVVl5FaexNPtBKVS1Dvn4Ekt%2BNj5B4%2FMOq%2FNT1T03po9JCKEZWnm7BkhpFpmaB1E4KgTzLLN0I9VZYYFfvo1WJY8G3nf3yWzddmQoJHeldtZ0FZlbrC2hyifR%2B&X-Amz-Signature=7d1ab4bcb7d2c7793560ccf38c08585f1722c445d58a37e424df081b16ea6aba&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664KTD5NVG%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE3xo8BC%2BspCRox2H7LhKIRFo1LhYz2CC8I4jiqcAxuiAiEAhB%2B%2FI45p92vw6OgGjm8MmEvl3KbLJNUvMxLjk21bBj0qiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBSLo7kTI%2BPLmfUwHSrcA74KquCxRSOe%2Fy9b3Ho0PAmV%2FLiE6UO8QX5RCZCNb7XP9k5LNwIuvliTHriYPemtDwqx0Re5BJBpDi3Rwisx74%2Fj1hV9MdHz25o0H5Y%2B9xMJyoVkI5M34g9n%2ByWoosDlt7yIhoJYTqddb%2BFlLg5joXvW1sdpIDDjiT2O3qyq9ivu6%2FKo%2Bnm4HeJ5YcJM9QkIZZjvWrH1qG7bhmwLybI1L8fYajDsnTr64spevW2vPVH3tdwVQZpcxIWq92TVpA9flncujS%2BXwjpWS1W2jvX2T0I0YBk5eYeXwEcfr0Gup6nRbd4hWg8eCJcfNY%2FHO6HqHsxKB97a%2BNjbcJTBgBoDxmL%2FuShAmZXmPU5Gc1mqCgW4PqtrPbKoaDozyhUdufFP%2Br3emYiRVJMd2SsEPaSR5he7tFm9yL2dc%2Fadw7F8vpjXnALOcRIonSTe2O0ranNlmcPQFsj%2B7dLrcKRSbAoksk913gsSH1ypHzQRHqJpd9vKgX0dVpbxiip0IK8KwfJUEdeo5hB2ROcaBe9M01q82DeyMdnejQM1Iy8CH2KhirqnU%2FIvFWLebtJE1LLxm6ze2thakK80tgWU%2FCbhOTa2Cuzg4s2YDl38ZvUTv0mTBOclbHuTAnuj4En9dCRBMKjQ8LwGOqUB4ELpuKdsO3DJyN%2BpTo8PDrYVpMa7t35Yib%2BcjyvVH12WAtWmVaXIV1aRc91cTx%2FLY%2BG3eu4a8Qw%2FD6CtmZ5Xl1j6xzhIWJXncSNVVl5FaexNPtBKVS1Dvn4Ekt%2BNj5B4%2FMOq%2FNT1T03po9JCKEZWnm7BkhpFpmaB1E4KgTzLLN0I9VZYYFfvo1WJY8G3nf3yWzddmQoJHeldtZ0FZlbrC2hyifR%2B&X-Amz-Signature=955037e62a2bb2344aaef00218681a88627bb027c804f9e6d5a1cd3ccb988338&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664KTD5NVG%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE3xo8BC%2BspCRox2H7LhKIRFo1LhYz2CC8I4jiqcAxuiAiEAhB%2B%2FI45p92vw6OgGjm8MmEvl3KbLJNUvMxLjk21bBj0qiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBSLo7kTI%2BPLmfUwHSrcA74KquCxRSOe%2Fy9b3Ho0PAmV%2FLiE6UO8QX5RCZCNb7XP9k5LNwIuvliTHriYPemtDwqx0Re5BJBpDi3Rwisx74%2Fj1hV9MdHz25o0H5Y%2B9xMJyoVkI5M34g9n%2ByWoosDlt7yIhoJYTqddb%2BFlLg5joXvW1sdpIDDjiT2O3qyq9ivu6%2FKo%2Bnm4HeJ5YcJM9QkIZZjvWrH1qG7bhmwLybI1L8fYajDsnTr64spevW2vPVH3tdwVQZpcxIWq92TVpA9flncujS%2BXwjpWS1W2jvX2T0I0YBk5eYeXwEcfr0Gup6nRbd4hWg8eCJcfNY%2FHO6HqHsxKB97a%2BNjbcJTBgBoDxmL%2FuShAmZXmPU5Gc1mqCgW4PqtrPbKoaDozyhUdufFP%2Br3emYiRVJMd2SsEPaSR5he7tFm9yL2dc%2Fadw7F8vpjXnALOcRIonSTe2O0ranNlmcPQFsj%2B7dLrcKRSbAoksk913gsSH1ypHzQRHqJpd9vKgX0dVpbxiip0IK8KwfJUEdeo5hB2ROcaBe9M01q82DeyMdnejQM1Iy8CH2KhirqnU%2FIvFWLebtJE1LLxm6ze2thakK80tgWU%2FCbhOTa2Cuzg4s2YDl38ZvUTv0mTBOclbHuTAnuj4En9dCRBMKjQ8LwGOqUB4ELpuKdsO3DJyN%2BpTo8PDrYVpMa7t35Yib%2BcjyvVH12WAtWmVaXIV1aRc91cTx%2FLY%2BG3eu4a8Qw%2FD6CtmZ5Xl1j6xzhIWJXncSNVVl5FaexNPtBKVS1Dvn4Ekt%2BNj5B4%2FMOq%2FNT1T03po9JCKEZWnm7BkhpFpmaB1E4KgTzLLN0I9VZYYFfvo1WJY8G3nf3yWzddmQoJHeldtZ0FZlbrC2hyifR%2B&X-Amz-Signature=765d1545b703fa9039cb5f7c956a1b108cf0a7889a7e7f5c8a954fb455ef6c33&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664KTD5NVG%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE3xo8BC%2BspCRox2H7LhKIRFo1LhYz2CC8I4jiqcAxuiAiEAhB%2B%2FI45p92vw6OgGjm8MmEvl3KbLJNUvMxLjk21bBj0qiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBSLo7kTI%2BPLmfUwHSrcA74KquCxRSOe%2Fy9b3Ho0PAmV%2FLiE6UO8QX5RCZCNb7XP9k5LNwIuvliTHriYPemtDwqx0Re5BJBpDi3Rwisx74%2Fj1hV9MdHz25o0H5Y%2B9xMJyoVkI5M34g9n%2ByWoosDlt7yIhoJYTqddb%2BFlLg5joXvW1sdpIDDjiT2O3qyq9ivu6%2FKo%2Bnm4HeJ5YcJM9QkIZZjvWrH1qG7bhmwLybI1L8fYajDsnTr64spevW2vPVH3tdwVQZpcxIWq92TVpA9flncujS%2BXwjpWS1W2jvX2T0I0YBk5eYeXwEcfr0Gup6nRbd4hWg8eCJcfNY%2FHO6HqHsxKB97a%2BNjbcJTBgBoDxmL%2FuShAmZXmPU5Gc1mqCgW4PqtrPbKoaDozyhUdufFP%2Br3emYiRVJMd2SsEPaSR5he7tFm9yL2dc%2Fadw7F8vpjXnALOcRIonSTe2O0ranNlmcPQFsj%2B7dLrcKRSbAoksk913gsSH1ypHzQRHqJpd9vKgX0dVpbxiip0IK8KwfJUEdeo5hB2ROcaBe9M01q82DeyMdnejQM1Iy8CH2KhirqnU%2FIvFWLebtJE1LLxm6ze2thakK80tgWU%2FCbhOTa2Cuzg4s2YDl38ZvUTv0mTBOclbHuTAnuj4En9dCRBMKjQ8LwGOqUB4ELpuKdsO3DJyN%2BpTo8PDrYVpMa7t35Yib%2BcjyvVH12WAtWmVaXIV1aRc91cTx%2FLY%2BG3eu4a8Qw%2FD6CtmZ5Xl1j6xzhIWJXncSNVVl5FaexNPtBKVS1Dvn4Ekt%2BNj5B4%2FMOq%2FNT1T03po9JCKEZWnm7BkhpFpmaB1E4KgTzLLN0I9VZYYFfvo1WJY8G3nf3yWzddmQoJHeldtZ0FZlbrC2hyifR%2B&X-Amz-Signature=f8376c19fb3e9923dbcfeb2a76e1053271b12e9b161d2dd8edf82f80cd022898&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664KTD5NVG%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE3xo8BC%2BspCRox2H7LhKIRFo1LhYz2CC8I4jiqcAxuiAiEAhB%2B%2FI45p92vw6OgGjm8MmEvl3KbLJNUvMxLjk21bBj0qiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBSLo7kTI%2BPLmfUwHSrcA74KquCxRSOe%2Fy9b3Ho0PAmV%2FLiE6UO8QX5RCZCNb7XP9k5LNwIuvliTHriYPemtDwqx0Re5BJBpDi3Rwisx74%2Fj1hV9MdHz25o0H5Y%2B9xMJyoVkI5M34g9n%2ByWoosDlt7yIhoJYTqddb%2BFlLg5joXvW1sdpIDDjiT2O3qyq9ivu6%2FKo%2Bnm4HeJ5YcJM9QkIZZjvWrH1qG7bhmwLybI1L8fYajDsnTr64spevW2vPVH3tdwVQZpcxIWq92TVpA9flncujS%2BXwjpWS1W2jvX2T0I0YBk5eYeXwEcfr0Gup6nRbd4hWg8eCJcfNY%2FHO6HqHsxKB97a%2BNjbcJTBgBoDxmL%2FuShAmZXmPU5Gc1mqCgW4PqtrPbKoaDozyhUdufFP%2Br3emYiRVJMd2SsEPaSR5he7tFm9yL2dc%2Fadw7F8vpjXnALOcRIonSTe2O0ranNlmcPQFsj%2B7dLrcKRSbAoksk913gsSH1ypHzQRHqJpd9vKgX0dVpbxiip0IK8KwfJUEdeo5hB2ROcaBe9M01q82DeyMdnejQM1Iy8CH2KhirqnU%2FIvFWLebtJE1LLxm6ze2thakK80tgWU%2FCbhOTa2Cuzg4s2YDl38ZvUTv0mTBOclbHuTAnuj4En9dCRBMKjQ8LwGOqUB4ELpuKdsO3DJyN%2BpTo8PDrYVpMa7t35Yib%2BcjyvVH12WAtWmVaXIV1aRc91cTx%2FLY%2BG3eu4a8Qw%2FD6CtmZ5Xl1j6xzhIWJXncSNVVl5FaexNPtBKVS1Dvn4Ekt%2BNj5B4%2FMOq%2FNT1T03po9JCKEZWnm7BkhpFpmaB1E4KgTzLLN0I9VZYYFfvo1WJY8G3nf3yWzddmQoJHeldtZ0FZlbrC2hyifR%2B&X-Amz-Signature=46bab8526bfa90b6bec50967a6eac0e9edc66103359be5d0672e64e1b40e1c7d&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664KTD5NVG%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE3xo8BC%2BspCRox2H7LhKIRFo1LhYz2CC8I4jiqcAxuiAiEAhB%2B%2FI45p92vw6OgGjm8MmEvl3KbLJNUvMxLjk21bBj0qiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBSLo7kTI%2BPLmfUwHSrcA74KquCxRSOe%2Fy9b3Ho0PAmV%2FLiE6UO8QX5RCZCNb7XP9k5LNwIuvliTHriYPemtDwqx0Re5BJBpDi3Rwisx74%2Fj1hV9MdHz25o0H5Y%2B9xMJyoVkI5M34g9n%2ByWoosDlt7yIhoJYTqddb%2BFlLg5joXvW1sdpIDDjiT2O3qyq9ivu6%2FKo%2Bnm4HeJ5YcJM9QkIZZjvWrH1qG7bhmwLybI1L8fYajDsnTr64spevW2vPVH3tdwVQZpcxIWq92TVpA9flncujS%2BXwjpWS1W2jvX2T0I0YBk5eYeXwEcfr0Gup6nRbd4hWg8eCJcfNY%2FHO6HqHsxKB97a%2BNjbcJTBgBoDxmL%2FuShAmZXmPU5Gc1mqCgW4PqtrPbKoaDozyhUdufFP%2Br3emYiRVJMd2SsEPaSR5he7tFm9yL2dc%2Fadw7F8vpjXnALOcRIonSTe2O0ranNlmcPQFsj%2B7dLrcKRSbAoksk913gsSH1ypHzQRHqJpd9vKgX0dVpbxiip0IK8KwfJUEdeo5hB2ROcaBe9M01q82DeyMdnejQM1Iy8CH2KhirqnU%2FIvFWLebtJE1LLxm6ze2thakK80tgWU%2FCbhOTa2Cuzg4s2YDl38ZvUTv0mTBOclbHuTAnuj4En9dCRBMKjQ8LwGOqUB4ELpuKdsO3DJyN%2BpTo8PDrYVpMa7t35Yib%2BcjyvVH12WAtWmVaXIV1aRc91cTx%2FLY%2BG3eu4a8Qw%2FD6CtmZ5Xl1j6xzhIWJXncSNVVl5FaexNPtBKVS1Dvn4Ekt%2BNj5B4%2FMOq%2FNT1T03po9JCKEZWnm7BkhpFpmaB1E4KgTzLLN0I9VZYYFfvo1WJY8G3nf3yWzddmQoJHeldtZ0FZlbrC2hyifR%2B&X-Amz-Signature=4c74d53b91abc00a0fec6336d44bb6f65cfd11ed73130c8643bd1ee45bc9b7ba&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664KTD5NVG%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE3xo8BC%2BspCRox2H7LhKIRFo1LhYz2CC8I4jiqcAxuiAiEAhB%2B%2FI45p92vw6OgGjm8MmEvl3KbLJNUvMxLjk21bBj0qiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBSLo7kTI%2BPLmfUwHSrcA74KquCxRSOe%2Fy9b3Ho0PAmV%2FLiE6UO8QX5RCZCNb7XP9k5LNwIuvliTHriYPemtDwqx0Re5BJBpDi3Rwisx74%2Fj1hV9MdHz25o0H5Y%2B9xMJyoVkI5M34g9n%2ByWoosDlt7yIhoJYTqddb%2BFlLg5joXvW1sdpIDDjiT2O3qyq9ivu6%2FKo%2Bnm4HeJ5YcJM9QkIZZjvWrH1qG7bhmwLybI1L8fYajDsnTr64spevW2vPVH3tdwVQZpcxIWq92TVpA9flncujS%2BXwjpWS1W2jvX2T0I0YBk5eYeXwEcfr0Gup6nRbd4hWg8eCJcfNY%2FHO6HqHsxKB97a%2BNjbcJTBgBoDxmL%2FuShAmZXmPU5Gc1mqCgW4PqtrPbKoaDozyhUdufFP%2Br3emYiRVJMd2SsEPaSR5he7tFm9yL2dc%2Fadw7F8vpjXnALOcRIonSTe2O0ranNlmcPQFsj%2B7dLrcKRSbAoksk913gsSH1ypHzQRHqJpd9vKgX0dVpbxiip0IK8KwfJUEdeo5hB2ROcaBe9M01q82DeyMdnejQM1Iy8CH2KhirqnU%2FIvFWLebtJE1LLxm6ze2thakK80tgWU%2FCbhOTa2Cuzg4s2YDl38ZvUTv0mTBOclbHuTAnuj4En9dCRBMKjQ8LwGOqUB4ELpuKdsO3DJyN%2BpTo8PDrYVpMa7t35Yib%2BcjyvVH12WAtWmVaXIV1aRc91cTx%2FLY%2BG3eu4a8Qw%2FD6CtmZ5Xl1j6xzhIWJXncSNVVl5FaexNPtBKVS1Dvn4Ekt%2BNj5B4%2FMOq%2FNT1T03po9JCKEZWnm7BkhpFpmaB1E4KgTzLLN0I9VZYYFfvo1WJY8G3nf3yWzddmQoJHeldtZ0FZlbrC2hyifR%2B&X-Amz-Signature=f3e5b2da89794a2c98cbb134ff771cbb3bf629158c8a415a7229a9c9a07e89dc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664KTD5NVG%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE3xo8BC%2BspCRox2H7LhKIRFo1LhYz2CC8I4jiqcAxuiAiEAhB%2B%2FI45p92vw6OgGjm8MmEvl3KbLJNUvMxLjk21bBj0qiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBSLo7kTI%2BPLmfUwHSrcA74KquCxRSOe%2Fy9b3Ho0PAmV%2FLiE6UO8QX5RCZCNb7XP9k5LNwIuvliTHriYPemtDwqx0Re5BJBpDi3Rwisx74%2Fj1hV9MdHz25o0H5Y%2B9xMJyoVkI5M34g9n%2ByWoosDlt7yIhoJYTqddb%2BFlLg5joXvW1sdpIDDjiT2O3qyq9ivu6%2FKo%2Bnm4HeJ5YcJM9QkIZZjvWrH1qG7bhmwLybI1L8fYajDsnTr64spevW2vPVH3tdwVQZpcxIWq92TVpA9flncujS%2BXwjpWS1W2jvX2T0I0YBk5eYeXwEcfr0Gup6nRbd4hWg8eCJcfNY%2FHO6HqHsxKB97a%2BNjbcJTBgBoDxmL%2FuShAmZXmPU5Gc1mqCgW4PqtrPbKoaDozyhUdufFP%2Br3emYiRVJMd2SsEPaSR5he7tFm9yL2dc%2Fadw7F8vpjXnALOcRIonSTe2O0ranNlmcPQFsj%2B7dLrcKRSbAoksk913gsSH1ypHzQRHqJpd9vKgX0dVpbxiip0IK8KwfJUEdeo5hB2ROcaBe9M01q82DeyMdnejQM1Iy8CH2KhirqnU%2FIvFWLebtJE1LLxm6ze2thakK80tgWU%2FCbhOTa2Cuzg4s2YDl38ZvUTv0mTBOclbHuTAnuj4En9dCRBMKjQ8LwGOqUB4ELpuKdsO3DJyN%2BpTo8PDrYVpMa7t35Yib%2BcjyvVH12WAtWmVaXIV1aRc91cTx%2FLY%2BG3eu4a8Qw%2FD6CtmZ5Xl1j6xzhIWJXncSNVVl5FaexNPtBKVS1Dvn4Ekt%2BNj5B4%2FMOq%2FNT1T03po9JCKEZWnm7BkhpFpmaB1E4KgTzLLN0I9VZYYFfvo1WJY8G3nf3yWzddmQoJHeldtZ0FZlbrC2hyifR%2B&X-Amz-Signature=e0357c8d2be1c01b88ac13075f3b21d5c62285792c22d521279a97e5be8f524a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664KTD5NVG%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE3xo8BC%2BspCRox2H7LhKIRFo1LhYz2CC8I4jiqcAxuiAiEAhB%2B%2FI45p92vw6OgGjm8MmEvl3KbLJNUvMxLjk21bBj0qiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBSLo7kTI%2BPLmfUwHSrcA74KquCxRSOe%2Fy9b3Ho0PAmV%2FLiE6UO8QX5RCZCNb7XP9k5LNwIuvliTHriYPemtDwqx0Re5BJBpDi3Rwisx74%2Fj1hV9MdHz25o0H5Y%2B9xMJyoVkI5M34g9n%2ByWoosDlt7yIhoJYTqddb%2BFlLg5joXvW1sdpIDDjiT2O3qyq9ivu6%2FKo%2Bnm4HeJ5YcJM9QkIZZjvWrH1qG7bhmwLybI1L8fYajDsnTr64spevW2vPVH3tdwVQZpcxIWq92TVpA9flncujS%2BXwjpWS1W2jvX2T0I0YBk5eYeXwEcfr0Gup6nRbd4hWg8eCJcfNY%2FHO6HqHsxKB97a%2BNjbcJTBgBoDxmL%2FuShAmZXmPU5Gc1mqCgW4PqtrPbKoaDozyhUdufFP%2Br3emYiRVJMd2SsEPaSR5he7tFm9yL2dc%2Fadw7F8vpjXnALOcRIonSTe2O0ranNlmcPQFsj%2B7dLrcKRSbAoksk913gsSH1ypHzQRHqJpd9vKgX0dVpbxiip0IK8KwfJUEdeo5hB2ROcaBe9M01q82DeyMdnejQM1Iy8CH2KhirqnU%2FIvFWLebtJE1LLxm6ze2thakK80tgWU%2FCbhOTa2Cuzg4s2YDl38ZvUTv0mTBOclbHuTAnuj4En9dCRBMKjQ8LwGOqUB4ELpuKdsO3DJyN%2BpTo8PDrYVpMa7t35Yib%2BcjyvVH12WAtWmVaXIV1aRc91cTx%2FLY%2BG3eu4a8Qw%2FD6CtmZ5Xl1j6xzhIWJXncSNVVl5FaexNPtBKVS1Dvn4Ekt%2BNj5B4%2FMOq%2FNT1T03po9JCKEZWnm7BkhpFpmaB1E4KgTzLLN0I9VZYYFfvo1WJY8G3nf3yWzddmQoJHeldtZ0FZlbrC2hyifR%2B&X-Amz-Signature=541fa75f0a414a5a2a7324873c6e0563932e8013255f2fd744b1d0317d880af5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TYI5NKQM%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF%2BMofSt9tazTv%2FqDLlzqs%2FiscVPNMlBzIUdCGShKWvfAiAHWKzuEUggmPYubB7DwqMRDW%2FyW0hzRqo57udohAxXMiqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMxeIPiMR3lBmMlzBiKtwDjJN%2F01LtgNtRfWUaON%2B3AURUjRpjfOFvgVQ8Gb6kBU16rG2cFtCFNk3FqPYvrJ3ZPhFDVTAE5U%2B6mb5H3lAPzpr4PudzfdFh0SD2JqSJ3fp6EksarSigw0mcE%2BsQPt2iZ8fgnWDKhtgSOOj8QilojxPxZhjXLyvjYRudA5kNhSkkjkCk9hrYE3%2ByUZm2wIQ61PK1r1wjuY0IrbtkWE2Osk6KAEtqlMTY1u5uoiFB9Jb1bKClv1DecT%2FKDHkuc%2F75OiLL2Jrgi8%2FR%2BKoKi1hyNlqxwZQesf%2FRq2mv%2FjGbh1yIeawCWWAoFUSfjwwv3jpHncDcMFcINY4bNO9SKmz%2FPe9VJT2nG0XKKyJSZqKa%2B0cSMlm52Mr5K6FxzofmGDwAvG4ownBJFMN7aMgH%2FONb9djIPv5Kk7glGx1sZHkK46JU7NdLglC2JCzr%2Fq4qaxAl1jGqXl%2BNQbcYZdhBMEzHZVUZ2tM570TEWBJSazANCbbD%2BSDMTtIMaE0dG95V9LsZ2o%2BKmLm%2BT%2FW14aDMPBII2osnXUG997ylLBohIBVw%2B2NVcJFxtw1hYhVED04qFzphGD%2BKfjAfkvx7RPHSCxDe9AE3BwOG4vzFvmYyH%2Bu%2BZtYUF%2Bp0Dw9eBRvRdj4wvtDwvAY6pgHyKbXj4l9togHLEBe3RRA0k53pKthjK7dShdYrdFydJl4gWZ%2FckbAQNWK02EapR0aUN74a%2F7v%2Fy7qnb%2FkowGhuqNpfg1NwCcL0GN0%2BiRXDrwiUit150TKpIjLVDD6rGthK%2BXaIB%2Fcz18Poft1sQCtgamoZNtin1upQC9uKxiL2bYu26CWH9I%2F%2F9IU188Dm5h4d9RNBT%2FL%2Bw2a2ZkVoRdzCx1rJURTu&X-Amz-Signature=e3bf1a2624da76fdd952a7df11a48c80077c925c2f2a20ab62c0fb278a7fc150&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TYI5NKQM%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF%2BMofSt9tazTv%2FqDLlzqs%2FiscVPNMlBzIUdCGShKWvfAiAHWKzuEUggmPYubB7DwqMRDW%2FyW0hzRqo57udohAxXMiqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMxeIPiMR3lBmMlzBiKtwDjJN%2F01LtgNtRfWUaON%2B3AURUjRpjfOFvgVQ8Gb6kBU16rG2cFtCFNk3FqPYvrJ3ZPhFDVTAE5U%2B6mb5H3lAPzpr4PudzfdFh0SD2JqSJ3fp6EksarSigw0mcE%2BsQPt2iZ8fgnWDKhtgSOOj8QilojxPxZhjXLyvjYRudA5kNhSkkjkCk9hrYE3%2ByUZm2wIQ61PK1r1wjuY0IrbtkWE2Osk6KAEtqlMTY1u5uoiFB9Jb1bKClv1DecT%2FKDHkuc%2F75OiLL2Jrgi8%2FR%2BKoKi1hyNlqxwZQesf%2FRq2mv%2FjGbh1yIeawCWWAoFUSfjwwv3jpHncDcMFcINY4bNO9SKmz%2FPe9VJT2nG0XKKyJSZqKa%2B0cSMlm52Mr5K6FxzofmGDwAvG4ownBJFMN7aMgH%2FONb9djIPv5Kk7glGx1sZHkK46JU7NdLglC2JCzr%2Fq4qaxAl1jGqXl%2BNQbcYZdhBMEzHZVUZ2tM570TEWBJSazANCbbD%2BSDMTtIMaE0dG95V9LsZ2o%2BKmLm%2BT%2FW14aDMPBII2osnXUG997ylLBohIBVw%2B2NVcJFxtw1hYhVED04qFzphGD%2BKfjAfkvx7RPHSCxDe9AE3BwOG4vzFvmYyH%2Bu%2BZtYUF%2Bp0Dw9eBRvRdj4wvtDwvAY6pgHyKbXj4l9togHLEBe3RRA0k53pKthjK7dShdYrdFydJl4gWZ%2FckbAQNWK02EapR0aUN74a%2F7v%2Fy7qnb%2FkowGhuqNpfg1NwCcL0GN0%2BiRXDrwiUit150TKpIjLVDD6rGthK%2BXaIB%2Fcz18Poft1sQCtgamoZNtin1upQC9uKxiL2bYu26CWH9I%2F%2F9IU188Dm5h4d9RNBT%2FL%2Bw2a2ZkVoRdzCx1rJURTu&X-Amz-Signature=63217d7021eb51aa8464cda8a5fddf8c68c6e32a4113329442bd531a523e2865&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
