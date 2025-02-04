

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X2ST5PSI%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJHMEUCIFmkKUxPYy8SYSy1eHRU2dvBB3dSYceju2%2B3XuysoMtzAiEApTgRJusolLyo127tOkh153YR4POCkRk1f2V2iEffYngq%2FwMILhAAGgw2Mzc0MjMxODM4MDUiDNkGMPVqTmNFXCXesCrcA9M838GT4au7Ab41j3kkGxnk%2BOC1kX02LJUbUaf%2FVxNdbUmuKMJ7gbWCjyGKvnIASVdjmE8RHERJ6DaV%2BdtYOA8eXVwwQzwcZ01Qc0iCYfCSNej8iTxZwBGW6NkiUAO5W7CitVuFtfu4oidWLb8MfVtyJbZTOhT4g4SAUbmcXvGgyXg%2F8AaM%2FhXIgWknZLV7Og4%2FCTIe7ctA940BiDyG5qXJ0BX6QTU920VQw%2FEBl8Jh4ZDCnc2DclDw4Utlkoce9JxngW9AK3hv0MoWoiuY24CuDoVzsKG%2BSwgWv2dhwARtGPxdqI%2Brpqep6bA2zfiIlp9q%2FKp6%2BKY3MgkDLZjOCDSxKNgJTJ2iK%2BVPKC10IrSzdtKE36s%2BVkSC6tSH9SyQZWop%2BQTD%2BbQfpyPnqUpDXxLkz0sAG7YGZqwShg4lJuaah%2FPog4mlOZvNX0oYufiVPR2B%2FzFUBc3ZKcw7S0KjVlKCZtZEExi99%2BcFnwTYUoUgM8vJizdUg3EYKSpPTTAMynQmBrZN%2B%2FX0EbtkR3C818sxKqo5Lfx6bWi7BtxQfsYNE0xu8wz6BnRNx7jKuse4539%2FdQIEE9QRwq0%2FYnEyDp9Ubbc%2F0CmzS41NcQAdPriAjb2ywfoZRdrtGV%2FDMIKeiL0GOqUBUWRkYYxwjuUAyZVbIf4sIgeL%2BCpa6agib9X%2FyO3iCROf%2B5hrWhImjnntRW1fM4t7UDEUMMB47X8B%2BH50aI2bprmcUFvsqwgdlCqSpO45XePT%2FKs4rYOG9HeO8TrAXjxMsgIiyYkC%2Fvd%2FJV6xVggJcHFZWotdozGzmLDU7X4qS8%2Bb40Q6bi4qLgJHkSEAGA3lUpgoq15Oq%2FKGzKMVfDspfN1hvkXi&X-Amz-Signature=a58eadad6116b444ed5316739b22bfe52bec2dd34c400a0c41dbd0afc3641d8b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X2ST5PSI%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132040Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJHMEUCIFmkKUxPYy8SYSy1eHRU2dvBB3dSYceju2%2B3XuysoMtzAiEApTgRJusolLyo127tOkh153YR4POCkRk1f2V2iEffYngq%2FwMILhAAGgw2Mzc0MjMxODM4MDUiDNkGMPVqTmNFXCXesCrcA9M838GT4au7Ab41j3kkGxnk%2BOC1kX02LJUbUaf%2FVxNdbUmuKMJ7gbWCjyGKvnIASVdjmE8RHERJ6DaV%2BdtYOA8eXVwwQzwcZ01Qc0iCYfCSNej8iTxZwBGW6NkiUAO5W7CitVuFtfu4oidWLb8MfVtyJbZTOhT4g4SAUbmcXvGgyXg%2F8AaM%2FhXIgWknZLV7Og4%2FCTIe7ctA940BiDyG5qXJ0BX6QTU920VQw%2FEBl8Jh4ZDCnc2DclDw4Utlkoce9JxngW9AK3hv0MoWoiuY24CuDoVzsKG%2BSwgWv2dhwARtGPxdqI%2Brpqep6bA2zfiIlp9q%2FKp6%2BKY3MgkDLZjOCDSxKNgJTJ2iK%2BVPKC10IrSzdtKE36s%2BVkSC6tSH9SyQZWop%2BQTD%2BbQfpyPnqUpDXxLkz0sAG7YGZqwShg4lJuaah%2FPog4mlOZvNX0oYufiVPR2B%2FzFUBc3ZKcw7S0KjVlKCZtZEExi99%2BcFnwTYUoUgM8vJizdUg3EYKSpPTTAMynQmBrZN%2B%2FX0EbtkR3C818sxKqo5Lfx6bWi7BtxQfsYNE0xu8wz6BnRNx7jKuse4539%2FdQIEE9QRwq0%2FYnEyDp9Ubbc%2F0CmzS41NcQAdPriAjb2ywfoZRdrtGV%2FDMIKeiL0GOqUBUWRkYYxwjuUAyZVbIf4sIgeL%2BCpa6agib9X%2FyO3iCROf%2B5hrWhImjnntRW1fM4t7UDEUMMB47X8B%2BH50aI2bprmcUFvsqwgdlCqSpO45XePT%2FKs4rYOG9HeO8TrAXjxMsgIiyYkC%2Fvd%2FJV6xVggJcHFZWotdozGzmLDU7X4qS8%2Bb40Q6bi4qLgJHkSEAGA3lUpgoq15Oq%2FKGzKMVfDspfN1hvkXi&X-Amz-Signature=f1c3abb11dddd0eb9406d6eda418e79cc6bb29247e26b62f6040c69c853e60cb&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X2ST5PSI%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132040Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJHMEUCIFmkKUxPYy8SYSy1eHRU2dvBB3dSYceju2%2B3XuysoMtzAiEApTgRJusolLyo127tOkh153YR4POCkRk1f2V2iEffYngq%2FwMILhAAGgw2Mzc0MjMxODM4MDUiDNkGMPVqTmNFXCXesCrcA9M838GT4au7Ab41j3kkGxnk%2BOC1kX02LJUbUaf%2FVxNdbUmuKMJ7gbWCjyGKvnIASVdjmE8RHERJ6DaV%2BdtYOA8eXVwwQzwcZ01Qc0iCYfCSNej8iTxZwBGW6NkiUAO5W7CitVuFtfu4oidWLb8MfVtyJbZTOhT4g4SAUbmcXvGgyXg%2F8AaM%2FhXIgWknZLV7Og4%2FCTIe7ctA940BiDyG5qXJ0BX6QTU920VQw%2FEBl8Jh4ZDCnc2DclDw4Utlkoce9JxngW9AK3hv0MoWoiuY24CuDoVzsKG%2BSwgWv2dhwARtGPxdqI%2Brpqep6bA2zfiIlp9q%2FKp6%2BKY3MgkDLZjOCDSxKNgJTJ2iK%2BVPKC10IrSzdtKE36s%2BVkSC6tSH9SyQZWop%2BQTD%2BbQfpyPnqUpDXxLkz0sAG7YGZqwShg4lJuaah%2FPog4mlOZvNX0oYufiVPR2B%2FzFUBc3ZKcw7S0KjVlKCZtZEExi99%2BcFnwTYUoUgM8vJizdUg3EYKSpPTTAMynQmBrZN%2B%2FX0EbtkR3C818sxKqo5Lfx6bWi7BtxQfsYNE0xu8wz6BnRNx7jKuse4539%2FdQIEE9QRwq0%2FYnEyDp9Ubbc%2F0CmzS41NcQAdPriAjb2ywfoZRdrtGV%2FDMIKeiL0GOqUBUWRkYYxwjuUAyZVbIf4sIgeL%2BCpa6agib9X%2FyO3iCROf%2B5hrWhImjnntRW1fM4t7UDEUMMB47X8B%2BH50aI2bprmcUFvsqwgdlCqSpO45XePT%2FKs4rYOG9HeO8TrAXjxMsgIiyYkC%2Fvd%2FJV6xVggJcHFZWotdozGzmLDU7X4qS8%2Bb40Q6bi4qLgJHkSEAGA3lUpgoq15Oq%2FKGzKMVfDspfN1hvkXi&X-Amz-Signature=0e57258a848fc85c80911d0c1f7a685a883be5b57ae2d43f5607642343cc1d91&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X2ST5PSI%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJHMEUCIFmkKUxPYy8SYSy1eHRU2dvBB3dSYceju2%2B3XuysoMtzAiEApTgRJusolLyo127tOkh153YR4POCkRk1f2V2iEffYngq%2FwMILhAAGgw2Mzc0MjMxODM4MDUiDNkGMPVqTmNFXCXesCrcA9M838GT4au7Ab41j3kkGxnk%2BOC1kX02LJUbUaf%2FVxNdbUmuKMJ7gbWCjyGKvnIASVdjmE8RHERJ6DaV%2BdtYOA8eXVwwQzwcZ01Qc0iCYfCSNej8iTxZwBGW6NkiUAO5W7CitVuFtfu4oidWLb8MfVtyJbZTOhT4g4SAUbmcXvGgyXg%2F8AaM%2FhXIgWknZLV7Og4%2FCTIe7ctA940BiDyG5qXJ0BX6QTU920VQw%2FEBl8Jh4ZDCnc2DclDw4Utlkoce9JxngW9AK3hv0MoWoiuY24CuDoVzsKG%2BSwgWv2dhwARtGPxdqI%2Brpqep6bA2zfiIlp9q%2FKp6%2BKY3MgkDLZjOCDSxKNgJTJ2iK%2BVPKC10IrSzdtKE36s%2BVkSC6tSH9SyQZWop%2BQTD%2BbQfpyPnqUpDXxLkz0sAG7YGZqwShg4lJuaah%2FPog4mlOZvNX0oYufiVPR2B%2FzFUBc3ZKcw7S0KjVlKCZtZEExi99%2BcFnwTYUoUgM8vJizdUg3EYKSpPTTAMynQmBrZN%2B%2FX0EbtkR3C818sxKqo5Lfx6bWi7BtxQfsYNE0xu8wz6BnRNx7jKuse4539%2FdQIEE9QRwq0%2FYnEyDp9Ubbc%2F0CmzS41NcQAdPriAjb2ywfoZRdrtGV%2FDMIKeiL0GOqUBUWRkYYxwjuUAyZVbIf4sIgeL%2BCpa6agib9X%2FyO3iCROf%2B5hrWhImjnntRW1fM4t7UDEUMMB47X8B%2BH50aI2bprmcUFvsqwgdlCqSpO45XePT%2FKs4rYOG9HeO8TrAXjxMsgIiyYkC%2Fvd%2FJV6xVggJcHFZWotdozGzmLDU7X4qS8%2Bb40Q6bi4qLgJHkSEAGA3lUpgoq15Oq%2FKGzKMVfDspfN1hvkXi&X-Amz-Signature=a6ff3a4ddb4159f9f3a75ebba83fb035d7092c038403c07565f03f18de3c30e2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X2ST5PSI%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132040Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJHMEUCIFmkKUxPYy8SYSy1eHRU2dvBB3dSYceju2%2B3XuysoMtzAiEApTgRJusolLyo127tOkh153YR4POCkRk1f2V2iEffYngq%2FwMILhAAGgw2Mzc0MjMxODM4MDUiDNkGMPVqTmNFXCXesCrcA9M838GT4au7Ab41j3kkGxnk%2BOC1kX02LJUbUaf%2FVxNdbUmuKMJ7gbWCjyGKvnIASVdjmE8RHERJ6DaV%2BdtYOA8eXVwwQzwcZ01Qc0iCYfCSNej8iTxZwBGW6NkiUAO5W7CitVuFtfu4oidWLb8MfVtyJbZTOhT4g4SAUbmcXvGgyXg%2F8AaM%2FhXIgWknZLV7Og4%2FCTIe7ctA940BiDyG5qXJ0BX6QTU920VQw%2FEBl8Jh4ZDCnc2DclDw4Utlkoce9JxngW9AK3hv0MoWoiuY24CuDoVzsKG%2BSwgWv2dhwARtGPxdqI%2Brpqep6bA2zfiIlp9q%2FKp6%2BKY3MgkDLZjOCDSxKNgJTJ2iK%2BVPKC10IrSzdtKE36s%2BVkSC6tSH9SyQZWop%2BQTD%2BbQfpyPnqUpDXxLkz0sAG7YGZqwShg4lJuaah%2FPog4mlOZvNX0oYufiVPR2B%2FzFUBc3ZKcw7S0KjVlKCZtZEExi99%2BcFnwTYUoUgM8vJizdUg3EYKSpPTTAMynQmBrZN%2B%2FX0EbtkR3C818sxKqo5Lfx6bWi7BtxQfsYNE0xu8wz6BnRNx7jKuse4539%2FdQIEE9QRwq0%2FYnEyDp9Ubbc%2F0CmzS41NcQAdPriAjb2ywfoZRdrtGV%2FDMIKeiL0GOqUBUWRkYYxwjuUAyZVbIf4sIgeL%2BCpa6agib9X%2FyO3iCROf%2B5hrWhImjnntRW1fM4t7UDEUMMB47X8B%2BH50aI2bprmcUFvsqwgdlCqSpO45XePT%2FKs4rYOG9HeO8TrAXjxMsgIiyYkC%2Fvd%2FJV6xVggJcHFZWotdozGzmLDU7X4qS8%2Bb40Q6bi4qLgJHkSEAGA3lUpgoq15Oq%2FKGzKMVfDspfN1hvkXi&X-Amz-Signature=e27c5a5c734b80b8fe1e1a28f49f0c531ffb8b883997d8a125c878b84d523123&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X2ST5PSI%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132040Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJHMEUCIFmkKUxPYy8SYSy1eHRU2dvBB3dSYceju2%2B3XuysoMtzAiEApTgRJusolLyo127tOkh153YR4POCkRk1f2V2iEffYngq%2FwMILhAAGgw2Mzc0MjMxODM4MDUiDNkGMPVqTmNFXCXesCrcA9M838GT4au7Ab41j3kkGxnk%2BOC1kX02LJUbUaf%2FVxNdbUmuKMJ7gbWCjyGKvnIASVdjmE8RHERJ6DaV%2BdtYOA8eXVwwQzwcZ01Qc0iCYfCSNej8iTxZwBGW6NkiUAO5W7CitVuFtfu4oidWLb8MfVtyJbZTOhT4g4SAUbmcXvGgyXg%2F8AaM%2FhXIgWknZLV7Og4%2FCTIe7ctA940BiDyG5qXJ0BX6QTU920VQw%2FEBl8Jh4ZDCnc2DclDw4Utlkoce9JxngW9AK3hv0MoWoiuY24CuDoVzsKG%2BSwgWv2dhwARtGPxdqI%2Brpqep6bA2zfiIlp9q%2FKp6%2BKY3MgkDLZjOCDSxKNgJTJ2iK%2BVPKC10IrSzdtKE36s%2BVkSC6tSH9SyQZWop%2BQTD%2BbQfpyPnqUpDXxLkz0sAG7YGZqwShg4lJuaah%2FPog4mlOZvNX0oYufiVPR2B%2FzFUBc3ZKcw7S0KjVlKCZtZEExi99%2BcFnwTYUoUgM8vJizdUg3EYKSpPTTAMynQmBrZN%2B%2FX0EbtkR3C818sxKqo5Lfx6bWi7BtxQfsYNE0xu8wz6BnRNx7jKuse4539%2FdQIEE9QRwq0%2FYnEyDp9Ubbc%2F0CmzS41NcQAdPriAjb2ywfoZRdrtGV%2FDMIKeiL0GOqUBUWRkYYxwjuUAyZVbIf4sIgeL%2BCpa6agib9X%2FyO3iCROf%2B5hrWhImjnntRW1fM4t7UDEUMMB47X8B%2BH50aI2bprmcUFvsqwgdlCqSpO45XePT%2FKs4rYOG9HeO8TrAXjxMsgIiyYkC%2Fvd%2FJV6xVggJcHFZWotdozGzmLDU7X4qS8%2Bb40Q6bi4qLgJHkSEAGA3lUpgoq15Oq%2FKGzKMVfDspfN1hvkXi&X-Amz-Signature=bab2506a2df2815a7a40f7bda6ead00b2922c0a23d4f2fd06b4a954133b0bda6&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X2ST5PSI%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJHMEUCIFmkKUxPYy8SYSy1eHRU2dvBB3dSYceju2%2B3XuysoMtzAiEApTgRJusolLyo127tOkh153YR4POCkRk1f2V2iEffYngq%2FwMILhAAGgw2Mzc0MjMxODM4MDUiDNkGMPVqTmNFXCXesCrcA9M838GT4au7Ab41j3kkGxnk%2BOC1kX02LJUbUaf%2FVxNdbUmuKMJ7gbWCjyGKvnIASVdjmE8RHERJ6DaV%2BdtYOA8eXVwwQzwcZ01Qc0iCYfCSNej8iTxZwBGW6NkiUAO5W7CitVuFtfu4oidWLb8MfVtyJbZTOhT4g4SAUbmcXvGgyXg%2F8AaM%2FhXIgWknZLV7Og4%2FCTIe7ctA940BiDyG5qXJ0BX6QTU920VQw%2FEBl8Jh4ZDCnc2DclDw4Utlkoce9JxngW9AK3hv0MoWoiuY24CuDoVzsKG%2BSwgWv2dhwARtGPxdqI%2Brpqep6bA2zfiIlp9q%2FKp6%2BKY3MgkDLZjOCDSxKNgJTJ2iK%2BVPKC10IrSzdtKE36s%2BVkSC6tSH9SyQZWop%2BQTD%2BbQfpyPnqUpDXxLkz0sAG7YGZqwShg4lJuaah%2FPog4mlOZvNX0oYufiVPR2B%2FzFUBc3ZKcw7S0KjVlKCZtZEExi99%2BcFnwTYUoUgM8vJizdUg3EYKSpPTTAMynQmBrZN%2B%2FX0EbtkR3C818sxKqo5Lfx6bWi7BtxQfsYNE0xu8wz6BnRNx7jKuse4539%2FdQIEE9QRwq0%2FYnEyDp9Ubbc%2F0CmzS41NcQAdPriAjb2ywfoZRdrtGV%2FDMIKeiL0GOqUBUWRkYYxwjuUAyZVbIf4sIgeL%2BCpa6agib9X%2FyO3iCROf%2B5hrWhImjnntRW1fM4t7UDEUMMB47X8B%2BH50aI2bprmcUFvsqwgdlCqSpO45XePT%2FKs4rYOG9HeO8TrAXjxMsgIiyYkC%2Fvd%2FJV6xVggJcHFZWotdozGzmLDU7X4qS8%2Bb40Q6bi4qLgJHkSEAGA3lUpgoq15Oq%2FKGzKMVfDspfN1hvkXi&X-Amz-Signature=d4207b6cac20a4049cf5cadf144673b334e816ef19763198df8be6e449583b05&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X2ST5PSI%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJHMEUCIFmkKUxPYy8SYSy1eHRU2dvBB3dSYceju2%2B3XuysoMtzAiEApTgRJusolLyo127tOkh153YR4POCkRk1f2V2iEffYngq%2FwMILhAAGgw2Mzc0MjMxODM4MDUiDNkGMPVqTmNFXCXesCrcA9M838GT4au7Ab41j3kkGxnk%2BOC1kX02LJUbUaf%2FVxNdbUmuKMJ7gbWCjyGKvnIASVdjmE8RHERJ6DaV%2BdtYOA8eXVwwQzwcZ01Qc0iCYfCSNej8iTxZwBGW6NkiUAO5W7CitVuFtfu4oidWLb8MfVtyJbZTOhT4g4SAUbmcXvGgyXg%2F8AaM%2FhXIgWknZLV7Og4%2FCTIe7ctA940BiDyG5qXJ0BX6QTU920VQw%2FEBl8Jh4ZDCnc2DclDw4Utlkoce9JxngW9AK3hv0MoWoiuY24CuDoVzsKG%2BSwgWv2dhwARtGPxdqI%2Brpqep6bA2zfiIlp9q%2FKp6%2BKY3MgkDLZjOCDSxKNgJTJ2iK%2BVPKC10IrSzdtKE36s%2BVkSC6tSH9SyQZWop%2BQTD%2BbQfpyPnqUpDXxLkz0sAG7YGZqwShg4lJuaah%2FPog4mlOZvNX0oYufiVPR2B%2FzFUBc3ZKcw7S0KjVlKCZtZEExi99%2BcFnwTYUoUgM8vJizdUg3EYKSpPTTAMynQmBrZN%2B%2FX0EbtkR3C818sxKqo5Lfx6bWi7BtxQfsYNE0xu8wz6BnRNx7jKuse4539%2FdQIEE9QRwq0%2FYnEyDp9Ubbc%2F0CmzS41NcQAdPriAjb2ywfoZRdrtGV%2FDMIKeiL0GOqUBUWRkYYxwjuUAyZVbIf4sIgeL%2BCpa6agib9X%2FyO3iCROf%2B5hrWhImjnntRW1fM4t7UDEUMMB47X8B%2BH50aI2bprmcUFvsqwgdlCqSpO45XePT%2FKs4rYOG9HeO8TrAXjxMsgIiyYkC%2Fvd%2FJV6xVggJcHFZWotdozGzmLDU7X4qS8%2Bb40Q6bi4qLgJHkSEAGA3lUpgoq15Oq%2FKGzKMVfDspfN1hvkXi&X-Amz-Signature=c398c707bb628e1b3971508aef2a77e276bb32cef717b3bc9cdecead937d0244&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X2ST5PSI%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJHMEUCIFmkKUxPYy8SYSy1eHRU2dvBB3dSYceju2%2B3XuysoMtzAiEApTgRJusolLyo127tOkh153YR4POCkRk1f2V2iEffYngq%2FwMILhAAGgw2Mzc0MjMxODM4MDUiDNkGMPVqTmNFXCXesCrcA9M838GT4au7Ab41j3kkGxnk%2BOC1kX02LJUbUaf%2FVxNdbUmuKMJ7gbWCjyGKvnIASVdjmE8RHERJ6DaV%2BdtYOA8eXVwwQzwcZ01Qc0iCYfCSNej8iTxZwBGW6NkiUAO5W7CitVuFtfu4oidWLb8MfVtyJbZTOhT4g4SAUbmcXvGgyXg%2F8AaM%2FhXIgWknZLV7Og4%2FCTIe7ctA940BiDyG5qXJ0BX6QTU920VQw%2FEBl8Jh4ZDCnc2DclDw4Utlkoce9JxngW9AK3hv0MoWoiuY24CuDoVzsKG%2BSwgWv2dhwARtGPxdqI%2Brpqep6bA2zfiIlp9q%2FKp6%2BKY3MgkDLZjOCDSxKNgJTJ2iK%2BVPKC10IrSzdtKE36s%2BVkSC6tSH9SyQZWop%2BQTD%2BbQfpyPnqUpDXxLkz0sAG7YGZqwShg4lJuaah%2FPog4mlOZvNX0oYufiVPR2B%2FzFUBc3ZKcw7S0KjVlKCZtZEExi99%2BcFnwTYUoUgM8vJizdUg3EYKSpPTTAMynQmBrZN%2B%2FX0EbtkR3C818sxKqo5Lfx6bWi7BtxQfsYNE0xu8wz6BnRNx7jKuse4539%2FdQIEE9QRwq0%2FYnEyDp9Ubbc%2F0CmzS41NcQAdPriAjb2ywfoZRdrtGV%2FDMIKeiL0GOqUBUWRkYYxwjuUAyZVbIf4sIgeL%2BCpa6agib9X%2FyO3iCROf%2B5hrWhImjnntRW1fM4t7UDEUMMB47X8B%2BH50aI2bprmcUFvsqwgdlCqSpO45XePT%2FKs4rYOG9HeO8TrAXjxMsgIiyYkC%2Fvd%2FJV6xVggJcHFZWotdozGzmLDU7X4qS8%2Bb40Q6bi4qLgJHkSEAGA3lUpgoq15Oq%2FKGzKMVfDspfN1hvkXi&X-Amz-Signature=81991ff58740df13b895fbf1d42e8c5b968b5cd1ab469fd79bdad7a517e7dcaa&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4QADEWN%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJIMEYCIQD6DPTNnl1xQiX5bjLMu9FhBF98IbVX2NWkA9YqpEejVAIhAPjHkVJxcF9VsVB%2BUuPhLcfi8xf%2FgqgkpdEg72kKCz7hKv8DCC4QABoMNjM3NDIzMTgzODA1Igz%2FGF3Qo1pai%2BY7MZMq3AOnMgPTREhCUeKmcUF%2B42KAc8lb8wB6Qq7AHLrvZ69SIvlfV%2BlLvJMJnFSbJYJtcGc7UuJziZBkKntyvfjFK92CyaLKgHmGZwN6u62dA7iNFHeVCIAk62NVw7ENC3xYDME%2FSvTkCc3x90h4H%2BfxAv1g8aWLeuVHwqihsaTDL3CQMbpyheKOBkwxgGHuqL0FWHqgbrDlq%2BLBf5sWdoSZeVpwnwO4CInDqrrI%2FFAdCRmX8HuWkJkTnFV8eyZgjf7Qha3SfbqawDBsypbEg2remtweebOJMXsOuzpTpzPtZTzK0Neo3eP621AGUig8akEq%2FS0Iv2T9OGlVwmNxDHGK1oaalwS%2F9rB7WCJVyy19gFeNlR5cJ5u73nVsQbkVfpya2c%2B3NQ9zf5GFluc3WN3iJTLVWUbGg9llhSbP9KHsghYl25FTTh%2BvaixSmbsFoHxN0hWZaCtC8bRQfHfM%2FSRMwkSjkMk84Avtcg0taTyhS9aZpVt0fPE2PxgCiSjA0C998b1nJME1QqGBLJMff8jDDesA4kiNDYbDTLHM%2FE3JKvDaBJs5r%2FHZTOQTgLGYL82JXO4Zp3oWLgc6kUlZHnajfvj8gj1o6J7L%2FeiRS1cOiFhgGyklwIvLAOCGxqQWujCunoi9BjqkAc678cbZ%2Bbq9kTDCg1x4Eb1kSKK%2Fx3qEOOE8MKZLzOPIVNt6RArAd0giiTNjh8GFMH0HYwicOcYximww6SGlQ%2BHk%2FR6qHqg2xOnOpKzLQSLJX64jUpCxXRWpxmv37d06TSaXbRT7dONUBY48Wx2DeDYLVeG1PCNL2%2B804sgU%2F9JQYp5OCxB71yZpb1q%2FG1I5w1h2L4waKUeiN0Y2K4u%2F9MUpj0mB&X-Amz-Signature=f97ee2b389aa17aeb8fb90f11125911073313c2f97d901bf6f6c63a97efd2948&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4QADEWN%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJIMEYCIQD6DPTNnl1xQiX5bjLMu9FhBF98IbVX2NWkA9YqpEejVAIhAPjHkVJxcF9VsVB%2BUuPhLcfi8xf%2FgqgkpdEg72kKCz7hKv8DCC4QABoMNjM3NDIzMTgzODA1Igz%2FGF3Qo1pai%2BY7MZMq3AOnMgPTREhCUeKmcUF%2B42KAc8lb8wB6Qq7AHLrvZ69SIvlfV%2BlLvJMJnFSbJYJtcGc7UuJziZBkKntyvfjFK92CyaLKgHmGZwN6u62dA7iNFHeVCIAk62NVw7ENC3xYDME%2FSvTkCc3x90h4H%2BfxAv1g8aWLeuVHwqihsaTDL3CQMbpyheKOBkwxgGHuqL0FWHqgbrDlq%2BLBf5sWdoSZeVpwnwO4CInDqrrI%2FFAdCRmX8HuWkJkTnFV8eyZgjf7Qha3SfbqawDBsypbEg2remtweebOJMXsOuzpTpzPtZTzK0Neo3eP621AGUig8akEq%2FS0Iv2T9OGlVwmNxDHGK1oaalwS%2F9rB7WCJVyy19gFeNlR5cJ5u73nVsQbkVfpya2c%2B3NQ9zf5GFluc3WN3iJTLVWUbGg9llhSbP9KHsghYl25FTTh%2BvaixSmbsFoHxN0hWZaCtC8bRQfHfM%2FSRMwkSjkMk84Avtcg0taTyhS9aZpVt0fPE2PxgCiSjA0C998b1nJME1QqGBLJMff8jDDesA4kiNDYbDTLHM%2FE3JKvDaBJs5r%2FHZTOQTgLGYL82JXO4Zp3oWLgc6kUlZHnajfvj8gj1o6J7L%2FeiRS1cOiFhgGyklwIvLAOCGxqQWujCunoi9BjqkAc678cbZ%2Bbq9kTDCg1x4Eb1kSKK%2Fx3qEOOE8MKZLzOPIVNt6RArAd0giiTNjh8GFMH0HYwicOcYximww6SGlQ%2BHk%2FR6qHqg2xOnOpKzLQSLJX64jUpCxXRWpxmv37d06TSaXbRT7dONUBY48Wx2DeDYLVeG1PCNL2%2B804sgU%2F9JQYp5OCxB71yZpb1q%2FG1I5w1h2L4waKUeiN0Y2K4u%2F9MUpj0mB&X-Amz-Signature=befc45212452cd6c656db2e039e6c6bf80208119a72726dfc2d06bd319220984&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
