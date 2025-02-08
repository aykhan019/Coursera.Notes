

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGHIBY3C%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJHMEUCIDg1R5P8cuzergueM%2BkuukbS5hC2n7KxJN1mwmcnpMjQAiEA8BK9h54wvO39M84CP%2BSjtHUWYFaHrrbXux7%2B4aIXzJYqiAQIhv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFDPWrcIQTiYUNcSbSrcA%2FBMhIFWVmslo%2FjkOP3cPnDrBvSWALHTkB0ehnN%2F7mF%2FCEttMkzcZZlKbjLLk20n2T6s9gYkWgjTIvyAwb2gSsfAGJTATf1SvbYfGLg%2FnWTysPoNTms7umpnAOE1Bp2E5v6bcf%2BXuSnblVfYeB%2B6XxWbv0NP%2FiRkrLcNlMFjCHwfXT6XOZ1rCrHmUftIAPxHCdkihYRXL1yyD%2BVYcLFaRImOYoFBAHjG0kdTOpJP1IobGdUFiqM4jYpqpV55UZDmb%2BugG%2FWRYlFl%2Bi%2BfHQPSuffmblmPMbG3%2FWFj%2FcX99GqGJkfnQVCIcYPiBEuIIWHDzMEMnJ%2BTjmQ30F8KpNq7Cuxt8QinvUFA8BnrL%2FuOSilNzrzQxc4yVMqIV3z852qHwTbECdRVeZQGiIRBLKLBka1l4tu0mZK1IpCSf7ntrdgzgxwOJg%2FWp68cRqZCJRQukxU0LffhQ0OCYQiPd2ocThq8Mdw5FU0XfCQm01iyAqXy6uJCBCpfXzXh30y9bPUb6pLzLurM7IeQFkuff6uRLFlX%2F9iGqcfye0KenbH%2BnR814wfdBfHuFiX72qVzZxtSzrCVx%2BLFUbdzno8smy5mtSV1uGBJEUVvO8G7dW9aSSPMDdJFXzjEitVgLTTsMOLUm70GOqUBYOXK2FPGEu36Eka46PQPPhmj3YEHf7NFNEVGW1sdMpMnQnRcR8PaSIrBoM4E%2FmOn06u54WghyZrLT7ebTkMh6dmA2bKR%2BUGNMiL5hBWEMQd1j0z25JdEJyYX8JtMS6NqIIcUymkjCSBSyS11ywTjb2yrE4nTz6RKdnbs2XMc3NdQNu%2FSDKfuKoBNyTIQEe1sT7gfLZlUI0KBW9pydWGj34egDCYT&X-Amz-Signature=d05e45fa4b0fd861c5882e60736e061fcc6cb7d3e05ec624e24a7957261f7bc0&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGHIBY3C%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJHMEUCIDg1R5P8cuzergueM%2BkuukbS5hC2n7KxJN1mwmcnpMjQAiEA8BK9h54wvO39M84CP%2BSjtHUWYFaHrrbXux7%2B4aIXzJYqiAQIhv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFDPWrcIQTiYUNcSbSrcA%2FBMhIFWVmslo%2FjkOP3cPnDrBvSWALHTkB0ehnN%2F7mF%2FCEttMkzcZZlKbjLLk20n2T6s9gYkWgjTIvyAwb2gSsfAGJTATf1SvbYfGLg%2FnWTysPoNTms7umpnAOE1Bp2E5v6bcf%2BXuSnblVfYeB%2B6XxWbv0NP%2FiRkrLcNlMFjCHwfXT6XOZ1rCrHmUftIAPxHCdkihYRXL1yyD%2BVYcLFaRImOYoFBAHjG0kdTOpJP1IobGdUFiqM4jYpqpV55UZDmb%2BugG%2FWRYlFl%2Bi%2BfHQPSuffmblmPMbG3%2FWFj%2FcX99GqGJkfnQVCIcYPiBEuIIWHDzMEMnJ%2BTjmQ30F8KpNq7Cuxt8QinvUFA8BnrL%2FuOSilNzrzQxc4yVMqIV3z852qHwTbECdRVeZQGiIRBLKLBka1l4tu0mZK1IpCSf7ntrdgzgxwOJg%2FWp68cRqZCJRQukxU0LffhQ0OCYQiPd2ocThq8Mdw5FU0XfCQm01iyAqXy6uJCBCpfXzXh30y9bPUb6pLzLurM7IeQFkuff6uRLFlX%2F9iGqcfye0KenbH%2BnR814wfdBfHuFiX72qVzZxtSzrCVx%2BLFUbdzno8smy5mtSV1uGBJEUVvO8G7dW9aSSPMDdJFXzjEitVgLTTsMOLUm70GOqUBYOXK2FPGEu36Eka46PQPPhmj3YEHf7NFNEVGW1sdMpMnQnRcR8PaSIrBoM4E%2FmOn06u54WghyZrLT7ebTkMh6dmA2bKR%2BUGNMiL5hBWEMQd1j0z25JdEJyYX8JtMS6NqIIcUymkjCSBSyS11ywTjb2yrE4nTz6RKdnbs2XMc3NdQNu%2FSDKfuKoBNyTIQEe1sT7gfLZlUI0KBW9pydWGj34egDCYT&X-Amz-Signature=a75fbf69229c350b286f56f92f9d039b533c840f86f05778918038c606136ed0&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGHIBY3C%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJHMEUCIDg1R5P8cuzergueM%2BkuukbS5hC2n7KxJN1mwmcnpMjQAiEA8BK9h54wvO39M84CP%2BSjtHUWYFaHrrbXux7%2B4aIXzJYqiAQIhv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFDPWrcIQTiYUNcSbSrcA%2FBMhIFWVmslo%2FjkOP3cPnDrBvSWALHTkB0ehnN%2F7mF%2FCEttMkzcZZlKbjLLk20n2T6s9gYkWgjTIvyAwb2gSsfAGJTATf1SvbYfGLg%2FnWTysPoNTms7umpnAOE1Bp2E5v6bcf%2BXuSnblVfYeB%2B6XxWbv0NP%2FiRkrLcNlMFjCHwfXT6XOZ1rCrHmUftIAPxHCdkihYRXL1yyD%2BVYcLFaRImOYoFBAHjG0kdTOpJP1IobGdUFiqM4jYpqpV55UZDmb%2BugG%2FWRYlFl%2Bi%2BfHQPSuffmblmPMbG3%2FWFj%2FcX99GqGJkfnQVCIcYPiBEuIIWHDzMEMnJ%2BTjmQ30F8KpNq7Cuxt8QinvUFA8BnrL%2FuOSilNzrzQxc4yVMqIV3z852qHwTbECdRVeZQGiIRBLKLBka1l4tu0mZK1IpCSf7ntrdgzgxwOJg%2FWp68cRqZCJRQukxU0LffhQ0OCYQiPd2ocThq8Mdw5FU0XfCQm01iyAqXy6uJCBCpfXzXh30y9bPUb6pLzLurM7IeQFkuff6uRLFlX%2F9iGqcfye0KenbH%2BnR814wfdBfHuFiX72qVzZxtSzrCVx%2BLFUbdzno8smy5mtSV1uGBJEUVvO8G7dW9aSSPMDdJFXzjEitVgLTTsMOLUm70GOqUBYOXK2FPGEu36Eka46PQPPhmj3YEHf7NFNEVGW1sdMpMnQnRcR8PaSIrBoM4E%2FmOn06u54WghyZrLT7ebTkMh6dmA2bKR%2BUGNMiL5hBWEMQd1j0z25JdEJyYX8JtMS6NqIIcUymkjCSBSyS11ywTjb2yrE4nTz6RKdnbs2XMc3NdQNu%2FSDKfuKoBNyTIQEe1sT7gfLZlUI0KBW9pydWGj34egDCYT&X-Amz-Signature=0755093bf3afb39ec5db53f941e3f7b4aad65104194880a97bf7ccaf2e2fdbdf&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGHIBY3C%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJHMEUCIDg1R5P8cuzergueM%2BkuukbS5hC2n7KxJN1mwmcnpMjQAiEA8BK9h54wvO39M84CP%2BSjtHUWYFaHrrbXux7%2B4aIXzJYqiAQIhv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFDPWrcIQTiYUNcSbSrcA%2FBMhIFWVmslo%2FjkOP3cPnDrBvSWALHTkB0ehnN%2F7mF%2FCEttMkzcZZlKbjLLk20n2T6s9gYkWgjTIvyAwb2gSsfAGJTATf1SvbYfGLg%2FnWTysPoNTms7umpnAOE1Bp2E5v6bcf%2BXuSnblVfYeB%2B6XxWbv0NP%2FiRkrLcNlMFjCHwfXT6XOZ1rCrHmUftIAPxHCdkihYRXL1yyD%2BVYcLFaRImOYoFBAHjG0kdTOpJP1IobGdUFiqM4jYpqpV55UZDmb%2BugG%2FWRYlFl%2Bi%2BfHQPSuffmblmPMbG3%2FWFj%2FcX99GqGJkfnQVCIcYPiBEuIIWHDzMEMnJ%2BTjmQ30F8KpNq7Cuxt8QinvUFA8BnrL%2FuOSilNzrzQxc4yVMqIV3z852qHwTbECdRVeZQGiIRBLKLBka1l4tu0mZK1IpCSf7ntrdgzgxwOJg%2FWp68cRqZCJRQukxU0LffhQ0OCYQiPd2ocThq8Mdw5FU0XfCQm01iyAqXy6uJCBCpfXzXh30y9bPUb6pLzLurM7IeQFkuff6uRLFlX%2F9iGqcfye0KenbH%2BnR814wfdBfHuFiX72qVzZxtSzrCVx%2BLFUbdzno8smy5mtSV1uGBJEUVvO8G7dW9aSSPMDdJFXzjEitVgLTTsMOLUm70GOqUBYOXK2FPGEu36Eka46PQPPhmj3YEHf7NFNEVGW1sdMpMnQnRcR8PaSIrBoM4E%2FmOn06u54WghyZrLT7ebTkMh6dmA2bKR%2BUGNMiL5hBWEMQd1j0z25JdEJyYX8JtMS6NqIIcUymkjCSBSyS11ywTjb2yrE4nTz6RKdnbs2XMc3NdQNu%2FSDKfuKoBNyTIQEe1sT7gfLZlUI0KBW9pydWGj34egDCYT&X-Amz-Signature=1662bc88989cd9c202ec4a5bfe948b1d195e2fb5285133361be7a80755d73a63&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGHIBY3C%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJHMEUCIDg1R5P8cuzergueM%2BkuukbS5hC2n7KxJN1mwmcnpMjQAiEA8BK9h54wvO39M84CP%2BSjtHUWYFaHrrbXux7%2B4aIXzJYqiAQIhv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFDPWrcIQTiYUNcSbSrcA%2FBMhIFWVmslo%2FjkOP3cPnDrBvSWALHTkB0ehnN%2F7mF%2FCEttMkzcZZlKbjLLk20n2T6s9gYkWgjTIvyAwb2gSsfAGJTATf1SvbYfGLg%2FnWTysPoNTms7umpnAOE1Bp2E5v6bcf%2BXuSnblVfYeB%2B6XxWbv0NP%2FiRkrLcNlMFjCHwfXT6XOZ1rCrHmUftIAPxHCdkihYRXL1yyD%2BVYcLFaRImOYoFBAHjG0kdTOpJP1IobGdUFiqM4jYpqpV55UZDmb%2BugG%2FWRYlFl%2Bi%2BfHQPSuffmblmPMbG3%2FWFj%2FcX99GqGJkfnQVCIcYPiBEuIIWHDzMEMnJ%2BTjmQ30F8KpNq7Cuxt8QinvUFA8BnrL%2FuOSilNzrzQxc4yVMqIV3z852qHwTbECdRVeZQGiIRBLKLBka1l4tu0mZK1IpCSf7ntrdgzgxwOJg%2FWp68cRqZCJRQukxU0LffhQ0OCYQiPd2ocThq8Mdw5FU0XfCQm01iyAqXy6uJCBCpfXzXh30y9bPUb6pLzLurM7IeQFkuff6uRLFlX%2F9iGqcfye0KenbH%2BnR814wfdBfHuFiX72qVzZxtSzrCVx%2BLFUbdzno8smy5mtSV1uGBJEUVvO8G7dW9aSSPMDdJFXzjEitVgLTTsMOLUm70GOqUBYOXK2FPGEu36Eka46PQPPhmj3YEHf7NFNEVGW1sdMpMnQnRcR8PaSIrBoM4E%2FmOn06u54WghyZrLT7ebTkMh6dmA2bKR%2BUGNMiL5hBWEMQd1j0z25JdEJyYX8JtMS6NqIIcUymkjCSBSyS11ywTjb2yrE4nTz6RKdnbs2XMc3NdQNu%2FSDKfuKoBNyTIQEe1sT7gfLZlUI0KBW9pydWGj34egDCYT&X-Amz-Signature=9ef7ab28b6579e092d7b8d5a9a59e5c34a8f3fffe20b8a29766721b123f5adba&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGHIBY3C%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJHMEUCIDg1R5P8cuzergueM%2BkuukbS5hC2n7KxJN1mwmcnpMjQAiEA8BK9h54wvO39M84CP%2BSjtHUWYFaHrrbXux7%2B4aIXzJYqiAQIhv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFDPWrcIQTiYUNcSbSrcA%2FBMhIFWVmslo%2FjkOP3cPnDrBvSWALHTkB0ehnN%2F7mF%2FCEttMkzcZZlKbjLLk20n2T6s9gYkWgjTIvyAwb2gSsfAGJTATf1SvbYfGLg%2FnWTysPoNTms7umpnAOE1Bp2E5v6bcf%2BXuSnblVfYeB%2B6XxWbv0NP%2FiRkrLcNlMFjCHwfXT6XOZ1rCrHmUftIAPxHCdkihYRXL1yyD%2BVYcLFaRImOYoFBAHjG0kdTOpJP1IobGdUFiqM4jYpqpV55UZDmb%2BugG%2FWRYlFl%2Bi%2BfHQPSuffmblmPMbG3%2FWFj%2FcX99GqGJkfnQVCIcYPiBEuIIWHDzMEMnJ%2BTjmQ30F8KpNq7Cuxt8QinvUFA8BnrL%2FuOSilNzrzQxc4yVMqIV3z852qHwTbECdRVeZQGiIRBLKLBka1l4tu0mZK1IpCSf7ntrdgzgxwOJg%2FWp68cRqZCJRQukxU0LffhQ0OCYQiPd2ocThq8Mdw5FU0XfCQm01iyAqXy6uJCBCpfXzXh30y9bPUb6pLzLurM7IeQFkuff6uRLFlX%2F9iGqcfye0KenbH%2BnR814wfdBfHuFiX72qVzZxtSzrCVx%2BLFUbdzno8smy5mtSV1uGBJEUVvO8G7dW9aSSPMDdJFXzjEitVgLTTsMOLUm70GOqUBYOXK2FPGEu36Eka46PQPPhmj3YEHf7NFNEVGW1sdMpMnQnRcR8PaSIrBoM4E%2FmOn06u54WghyZrLT7ebTkMh6dmA2bKR%2BUGNMiL5hBWEMQd1j0z25JdEJyYX8JtMS6NqIIcUymkjCSBSyS11ywTjb2yrE4nTz6RKdnbs2XMc3NdQNu%2FSDKfuKoBNyTIQEe1sT7gfLZlUI0KBW9pydWGj34egDCYT&X-Amz-Signature=4b189b09c548c5dec6d4e67506a38d1ac41f8a9fbd3b80ef9915c13ece098a02&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGHIBY3C%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJHMEUCIDg1R5P8cuzergueM%2BkuukbS5hC2n7KxJN1mwmcnpMjQAiEA8BK9h54wvO39M84CP%2BSjtHUWYFaHrrbXux7%2B4aIXzJYqiAQIhv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFDPWrcIQTiYUNcSbSrcA%2FBMhIFWVmslo%2FjkOP3cPnDrBvSWALHTkB0ehnN%2F7mF%2FCEttMkzcZZlKbjLLk20n2T6s9gYkWgjTIvyAwb2gSsfAGJTATf1SvbYfGLg%2FnWTysPoNTms7umpnAOE1Bp2E5v6bcf%2BXuSnblVfYeB%2B6XxWbv0NP%2FiRkrLcNlMFjCHwfXT6XOZ1rCrHmUftIAPxHCdkihYRXL1yyD%2BVYcLFaRImOYoFBAHjG0kdTOpJP1IobGdUFiqM4jYpqpV55UZDmb%2BugG%2FWRYlFl%2Bi%2BfHQPSuffmblmPMbG3%2FWFj%2FcX99GqGJkfnQVCIcYPiBEuIIWHDzMEMnJ%2BTjmQ30F8KpNq7Cuxt8QinvUFA8BnrL%2FuOSilNzrzQxc4yVMqIV3z852qHwTbECdRVeZQGiIRBLKLBka1l4tu0mZK1IpCSf7ntrdgzgxwOJg%2FWp68cRqZCJRQukxU0LffhQ0OCYQiPd2ocThq8Mdw5FU0XfCQm01iyAqXy6uJCBCpfXzXh30y9bPUb6pLzLurM7IeQFkuff6uRLFlX%2F9iGqcfye0KenbH%2BnR814wfdBfHuFiX72qVzZxtSzrCVx%2BLFUbdzno8smy5mtSV1uGBJEUVvO8G7dW9aSSPMDdJFXzjEitVgLTTsMOLUm70GOqUBYOXK2FPGEu36Eka46PQPPhmj3YEHf7NFNEVGW1sdMpMnQnRcR8PaSIrBoM4E%2FmOn06u54WghyZrLT7ebTkMh6dmA2bKR%2BUGNMiL5hBWEMQd1j0z25JdEJyYX8JtMS6NqIIcUymkjCSBSyS11ywTjb2yrE4nTz6RKdnbs2XMc3NdQNu%2FSDKfuKoBNyTIQEe1sT7gfLZlUI0KBW9pydWGj34egDCYT&X-Amz-Signature=4b9e4f9d0c14c524406e012c94ee91cd9625a181f53a65a04bffb3dfe7dac983&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGHIBY3C%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJHMEUCIDg1R5P8cuzergueM%2BkuukbS5hC2n7KxJN1mwmcnpMjQAiEA8BK9h54wvO39M84CP%2BSjtHUWYFaHrrbXux7%2B4aIXzJYqiAQIhv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFDPWrcIQTiYUNcSbSrcA%2FBMhIFWVmslo%2FjkOP3cPnDrBvSWALHTkB0ehnN%2F7mF%2FCEttMkzcZZlKbjLLk20n2T6s9gYkWgjTIvyAwb2gSsfAGJTATf1SvbYfGLg%2FnWTysPoNTms7umpnAOE1Bp2E5v6bcf%2BXuSnblVfYeB%2B6XxWbv0NP%2FiRkrLcNlMFjCHwfXT6XOZ1rCrHmUftIAPxHCdkihYRXL1yyD%2BVYcLFaRImOYoFBAHjG0kdTOpJP1IobGdUFiqM4jYpqpV55UZDmb%2BugG%2FWRYlFl%2Bi%2BfHQPSuffmblmPMbG3%2FWFj%2FcX99GqGJkfnQVCIcYPiBEuIIWHDzMEMnJ%2BTjmQ30F8KpNq7Cuxt8QinvUFA8BnrL%2FuOSilNzrzQxc4yVMqIV3z852qHwTbECdRVeZQGiIRBLKLBka1l4tu0mZK1IpCSf7ntrdgzgxwOJg%2FWp68cRqZCJRQukxU0LffhQ0OCYQiPd2ocThq8Mdw5FU0XfCQm01iyAqXy6uJCBCpfXzXh30y9bPUb6pLzLurM7IeQFkuff6uRLFlX%2F9iGqcfye0KenbH%2BnR814wfdBfHuFiX72qVzZxtSzrCVx%2BLFUbdzno8smy5mtSV1uGBJEUVvO8G7dW9aSSPMDdJFXzjEitVgLTTsMOLUm70GOqUBYOXK2FPGEu36Eka46PQPPhmj3YEHf7NFNEVGW1sdMpMnQnRcR8PaSIrBoM4E%2FmOn06u54WghyZrLT7ebTkMh6dmA2bKR%2BUGNMiL5hBWEMQd1j0z25JdEJyYX8JtMS6NqIIcUymkjCSBSyS11ywTjb2yrE4nTz6RKdnbs2XMc3NdQNu%2FSDKfuKoBNyTIQEe1sT7gfLZlUI0KBW9pydWGj34egDCYT&X-Amz-Signature=c7f5163a08430acc5c6acff35a72deafc982316d05b2bc03331e984a8188b524&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGHIBY3C%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJHMEUCIDg1R5P8cuzergueM%2BkuukbS5hC2n7KxJN1mwmcnpMjQAiEA8BK9h54wvO39M84CP%2BSjtHUWYFaHrrbXux7%2B4aIXzJYqiAQIhv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFDPWrcIQTiYUNcSbSrcA%2FBMhIFWVmslo%2FjkOP3cPnDrBvSWALHTkB0ehnN%2F7mF%2FCEttMkzcZZlKbjLLk20n2T6s9gYkWgjTIvyAwb2gSsfAGJTATf1SvbYfGLg%2FnWTysPoNTms7umpnAOE1Bp2E5v6bcf%2BXuSnblVfYeB%2B6XxWbv0NP%2FiRkrLcNlMFjCHwfXT6XOZ1rCrHmUftIAPxHCdkihYRXL1yyD%2BVYcLFaRImOYoFBAHjG0kdTOpJP1IobGdUFiqM4jYpqpV55UZDmb%2BugG%2FWRYlFl%2Bi%2BfHQPSuffmblmPMbG3%2FWFj%2FcX99GqGJkfnQVCIcYPiBEuIIWHDzMEMnJ%2BTjmQ30F8KpNq7Cuxt8QinvUFA8BnrL%2FuOSilNzrzQxc4yVMqIV3z852qHwTbECdRVeZQGiIRBLKLBka1l4tu0mZK1IpCSf7ntrdgzgxwOJg%2FWp68cRqZCJRQukxU0LffhQ0OCYQiPd2ocThq8Mdw5FU0XfCQm01iyAqXy6uJCBCpfXzXh30y9bPUb6pLzLurM7IeQFkuff6uRLFlX%2F9iGqcfye0KenbH%2BnR814wfdBfHuFiX72qVzZxtSzrCVx%2BLFUbdzno8smy5mtSV1uGBJEUVvO8G7dW9aSSPMDdJFXzjEitVgLTTsMOLUm70GOqUBYOXK2FPGEu36Eka46PQPPhmj3YEHf7NFNEVGW1sdMpMnQnRcR8PaSIrBoM4E%2FmOn06u54WghyZrLT7ebTkMh6dmA2bKR%2BUGNMiL5hBWEMQd1j0z25JdEJyYX8JtMS6NqIIcUymkjCSBSyS11ywTjb2yrE4nTz6RKdnbs2XMc3NdQNu%2FSDKfuKoBNyTIQEe1sT7gfLZlUI0KBW9pydWGj34egDCYT&X-Amz-Signature=49e350fc873b6a7f2f14c2bf26862905d642c68e72ab87b673d82f93a94b1d6d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666C7Z2WT2%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJHMEUCIFp68FKdHb%2BgcQ40ank5k20tb2G99i6oZtmGTkNUGimrAiEA4nRNUeqcpXrjOkC%2BK2ur8TxLVmvpC5x9NC1f4n6Qa38qiAQIhv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGLSb35nCJO3AoVynircA4397Pqm6h1gFIWY9MDn0geXhxHAu2rbGAytki1pCw0hf%2BV0IhGwRN1KR4fL9FB7yJ9jQC7b714ftZ81Y4R6CQNQeKUZh98fgquLPdEPKOWv1hTnHJAhp%2B%2F4F6YdMjme2YfSQvqDQHQdx60ggcnonDDernZl49h1e7i9Z6SKaJb6jFyyzEGmVKeczyIiBLwNUYMUyN3Fxny9fUQRkmf8jeZiwyygFvOajCLfmEl3Maz0IsYNwehVxzCNx%2BXbU43%2BmWa10L1G9cMzwp1nej%2BATVbkhim1%2FTRvB0m9YnNREKgugJDM1l%2BLlzeD4XpnkR4GoYoZRlRQDJnt21sDocBmAhgdLigYAZb%2BXvnr2pMSCkvAW1jwnwgnxiLESJbHcNXHpSV6at0VspjR6qgdpdqj1m2F2F3pKUGK3E9OT%2BSurvoJjepGsdr8toaZfDRyeVi3vpedKr%2BohZ40EqVovnjfCN4QP3Fx3CtibUOWWlZYZ88EU%2BQ1Uh075%2BO%2Fcag96fYpd4HohecVyld40%2FjCd%2FX6jjMB9EGZgiFgzIrF%2B4ML2sKPWap%2FSlWyVUUfWJRucGwX1oEeKHAYR%2BiOMeK2EvXzRNX4%2BVOnWa3tvFnwafWNWlNN3bLMMtHOvExZP10wMMDUm70GOqUBbKQkgow8IKtP65tewAy5veoYPJP3RBwuozXCxUoG5VRHklw9AyVGPAk6lEQy0QVyQFlTzAvvm6JlmnuGRmuGnuSmKYDxGt9fAnDjWvoh7vvg7ppJHjkwtR%2Bqav0jMlOayU0OLeEejlZ7vmF32DbDaFz412Ldz9LhAVrdh4YZxtn4%2FfKwYmHe7REBv%2FftceLCj5oK3fx8xqeVsDpc61gymw6VObg%2B&X-Amz-Signature=98bd99e47f458ebac60a1c6bd360a7d14664b35ac62be86032f150fd45786b01&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666C7Z2WT2%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJHMEUCIFp68FKdHb%2BgcQ40ank5k20tb2G99i6oZtmGTkNUGimrAiEA4nRNUeqcpXrjOkC%2BK2ur8TxLVmvpC5x9NC1f4n6Qa38qiAQIhv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGLSb35nCJO3AoVynircA4397Pqm6h1gFIWY9MDn0geXhxHAu2rbGAytki1pCw0hf%2BV0IhGwRN1KR4fL9FB7yJ9jQC7b714ftZ81Y4R6CQNQeKUZh98fgquLPdEPKOWv1hTnHJAhp%2B%2F4F6YdMjme2YfSQvqDQHQdx60ggcnonDDernZl49h1e7i9Z6SKaJb6jFyyzEGmVKeczyIiBLwNUYMUyN3Fxny9fUQRkmf8jeZiwyygFvOajCLfmEl3Maz0IsYNwehVxzCNx%2BXbU43%2BmWa10L1G9cMzwp1nej%2BATVbkhim1%2FTRvB0m9YnNREKgugJDM1l%2BLlzeD4XpnkR4GoYoZRlRQDJnt21sDocBmAhgdLigYAZb%2BXvnr2pMSCkvAW1jwnwgnxiLESJbHcNXHpSV6at0VspjR6qgdpdqj1m2F2F3pKUGK3E9OT%2BSurvoJjepGsdr8toaZfDRyeVi3vpedKr%2BohZ40EqVovnjfCN4QP3Fx3CtibUOWWlZYZ88EU%2BQ1Uh075%2BO%2Fcag96fYpd4HohecVyld40%2FjCd%2FX6jjMB9EGZgiFgzIrF%2B4ML2sKPWap%2FSlWyVUUfWJRucGwX1oEeKHAYR%2BiOMeK2EvXzRNX4%2BVOnWa3tvFnwafWNWlNN3bLMMtHOvExZP10wMMDUm70GOqUBbKQkgow8IKtP65tewAy5veoYPJP3RBwuozXCxUoG5VRHklw9AyVGPAk6lEQy0QVyQFlTzAvvm6JlmnuGRmuGnuSmKYDxGt9fAnDjWvoh7vvg7ppJHjkwtR%2Bqav0jMlOayU0OLeEejlZ7vmF32DbDaFz412Ldz9LhAVrdh4YZxtn4%2FfKwYmHe7REBv%2FftceLCj5oK3fx8xqeVsDpc61gymw6VObg%2B&X-Amz-Signature=2696eafb7c5c3741f592a4d9c756ea2f9d7afc93de3749639854eddd4e1fec0f&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
