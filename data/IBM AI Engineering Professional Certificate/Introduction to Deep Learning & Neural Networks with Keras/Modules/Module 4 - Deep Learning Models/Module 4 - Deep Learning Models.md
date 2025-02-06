

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W7WY2X7M%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQDgJ4pnMyK8AUzwnOhKkultcONGiaMuEgDEDBK2c%2BCryAIgSSjPzbfIogvO0o2BIjGsMKDV0OLx5KVPNqH46dYUtCYq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDI5VKc040esq61XPXCrcAyKLMM7qMgeLqrvvl6mQgJ1imPkOz7hSmTTgQrCgA%2FZKdS5eBVMCyGrhpSjLl8hI0382M5sBazmbcQ0q3y0%2FZkVpQDSSHHL0d5ExR7Ar9hvDAZDtWYlU0Xm%2FlR2LJbqBOhp9lybXiqk68S%2BFOXiiLAoRKbyW9VyT%2BswlQsFSL09Gut926YbbhjVar2RxrEHn9V0gP0n8WFzNyt%2F0yrkDbyaR2DzftSvxXnjd5p33dU0qF4C0patjk2fPRnsPF8eMJxpfWJCRWyYvNC96QG9Uz%2BD9WAB%2BJ5WcaOKVROifW9uEVQ2aHMu2C8%2B1nLsYiU1MS%2BPBZWVLpaw874h8of%2Fnvd8WNEkuXkJA19nUrFk7faiPlHQd79YMv%2FXaFva2es%2FjzQ8jtfkIJg%2BsaxdFoqF643KTwUNKxdAz0s2JY68qU0zX32T2sIlJdxOm8wEdYxsi0sSxJITZI2gOXXsbFSmitDhrbh1ef1husbgbrAXrJNGIikn%2BfODnxiuWjwlPFwju8YGuBCNH513TywP4WyHeW76j5ql%2FpWJ8jyLQlnqJeKgTOhq6AxNj27YQ3UGyefOEotUmk3B53Q%2FDu5RDfTFIXJtVdy26FltHirSO1lFx%2FCbhHGAfSqPpSsbJJiqEMKjEkr0GOqUBS0Ioxv%2B%2BqKdLfulB1C6XuM3OFyv4eOPrRIrB62oBf1XHh4A5dFYXliWcFgmKhiFhGJEvAu2BOrYp2WwvDYhEydWDAg7FfKWo5VnVwbW3mm5rZE%2FjqvZTHc9shJAEyw4Udk0NXJmA%2B2vPQ204I%2Bao7ZpWpeCfti2KgjitoJyxOsd4Zpi7IP6PfTPjeKUJxSo1fP9M2pLwY%2Be7VaIgTUDmyYQkhGDp&X-Amz-Signature=6735d793b7c296f1f3a6b9457607d91d5666d559b2947e6cba3d0f8eec9de71a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W7WY2X7M%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQDgJ4pnMyK8AUzwnOhKkultcONGiaMuEgDEDBK2c%2BCryAIgSSjPzbfIogvO0o2BIjGsMKDV0OLx5KVPNqH46dYUtCYq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDI5VKc040esq61XPXCrcAyKLMM7qMgeLqrvvl6mQgJ1imPkOz7hSmTTgQrCgA%2FZKdS5eBVMCyGrhpSjLl8hI0382M5sBazmbcQ0q3y0%2FZkVpQDSSHHL0d5ExR7Ar9hvDAZDtWYlU0Xm%2FlR2LJbqBOhp9lybXiqk68S%2BFOXiiLAoRKbyW9VyT%2BswlQsFSL09Gut926YbbhjVar2RxrEHn9V0gP0n8WFzNyt%2F0yrkDbyaR2DzftSvxXnjd5p33dU0qF4C0patjk2fPRnsPF8eMJxpfWJCRWyYvNC96QG9Uz%2BD9WAB%2BJ5WcaOKVROifW9uEVQ2aHMu2C8%2B1nLsYiU1MS%2BPBZWVLpaw874h8of%2Fnvd8WNEkuXkJA19nUrFk7faiPlHQd79YMv%2FXaFva2es%2FjzQ8jtfkIJg%2BsaxdFoqF643KTwUNKxdAz0s2JY68qU0zX32T2sIlJdxOm8wEdYxsi0sSxJITZI2gOXXsbFSmitDhrbh1ef1husbgbrAXrJNGIikn%2BfODnxiuWjwlPFwju8YGuBCNH513TywP4WyHeW76j5ql%2FpWJ8jyLQlnqJeKgTOhq6AxNj27YQ3UGyefOEotUmk3B53Q%2FDu5RDfTFIXJtVdy26FltHirSO1lFx%2FCbhHGAfSqPpSsbJJiqEMKjEkr0GOqUBS0Ioxv%2B%2BqKdLfulB1C6XuM3OFyv4eOPrRIrB62oBf1XHh4A5dFYXliWcFgmKhiFhGJEvAu2BOrYp2WwvDYhEydWDAg7FfKWo5VnVwbW3mm5rZE%2FjqvZTHc9shJAEyw4Udk0NXJmA%2B2vPQ204I%2Bao7ZpWpeCfti2KgjitoJyxOsd4Zpi7IP6PfTPjeKUJxSo1fP9M2pLwY%2Be7VaIgTUDmyYQkhGDp&X-Amz-Signature=cda4a65791cca306938ac4b6740c231b4d9802ac2ea735b885762380418be8e4&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W7WY2X7M%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQDgJ4pnMyK8AUzwnOhKkultcONGiaMuEgDEDBK2c%2BCryAIgSSjPzbfIogvO0o2BIjGsMKDV0OLx5KVPNqH46dYUtCYq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDI5VKc040esq61XPXCrcAyKLMM7qMgeLqrvvl6mQgJ1imPkOz7hSmTTgQrCgA%2FZKdS5eBVMCyGrhpSjLl8hI0382M5sBazmbcQ0q3y0%2FZkVpQDSSHHL0d5ExR7Ar9hvDAZDtWYlU0Xm%2FlR2LJbqBOhp9lybXiqk68S%2BFOXiiLAoRKbyW9VyT%2BswlQsFSL09Gut926YbbhjVar2RxrEHn9V0gP0n8WFzNyt%2F0yrkDbyaR2DzftSvxXnjd5p33dU0qF4C0patjk2fPRnsPF8eMJxpfWJCRWyYvNC96QG9Uz%2BD9WAB%2BJ5WcaOKVROifW9uEVQ2aHMu2C8%2B1nLsYiU1MS%2BPBZWVLpaw874h8of%2Fnvd8WNEkuXkJA19nUrFk7faiPlHQd79YMv%2FXaFva2es%2FjzQ8jtfkIJg%2BsaxdFoqF643KTwUNKxdAz0s2JY68qU0zX32T2sIlJdxOm8wEdYxsi0sSxJITZI2gOXXsbFSmitDhrbh1ef1husbgbrAXrJNGIikn%2BfODnxiuWjwlPFwju8YGuBCNH513TywP4WyHeW76j5ql%2FpWJ8jyLQlnqJeKgTOhq6AxNj27YQ3UGyefOEotUmk3B53Q%2FDu5RDfTFIXJtVdy26FltHirSO1lFx%2FCbhHGAfSqPpSsbJJiqEMKjEkr0GOqUBS0Ioxv%2B%2BqKdLfulB1C6XuM3OFyv4eOPrRIrB62oBf1XHh4A5dFYXliWcFgmKhiFhGJEvAu2BOrYp2WwvDYhEydWDAg7FfKWo5VnVwbW3mm5rZE%2FjqvZTHc9shJAEyw4Udk0NXJmA%2B2vPQ204I%2Bao7ZpWpeCfti2KgjitoJyxOsd4Zpi7IP6PfTPjeKUJxSo1fP9M2pLwY%2Be7VaIgTUDmyYQkhGDp&X-Amz-Signature=4229fa71972b7dffd1bef6a5e14fb996a89a3a20d46d8b06e368e7497f4ea438&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W7WY2X7M%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQDgJ4pnMyK8AUzwnOhKkultcONGiaMuEgDEDBK2c%2BCryAIgSSjPzbfIogvO0o2BIjGsMKDV0OLx5KVPNqH46dYUtCYq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDI5VKc040esq61XPXCrcAyKLMM7qMgeLqrvvl6mQgJ1imPkOz7hSmTTgQrCgA%2FZKdS5eBVMCyGrhpSjLl8hI0382M5sBazmbcQ0q3y0%2FZkVpQDSSHHL0d5ExR7Ar9hvDAZDtWYlU0Xm%2FlR2LJbqBOhp9lybXiqk68S%2BFOXiiLAoRKbyW9VyT%2BswlQsFSL09Gut926YbbhjVar2RxrEHn9V0gP0n8WFzNyt%2F0yrkDbyaR2DzftSvxXnjd5p33dU0qF4C0patjk2fPRnsPF8eMJxpfWJCRWyYvNC96QG9Uz%2BD9WAB%2BJ5WcaOKVROifW9uEVQ2aHMu2C8%2B1nLsYiU1MS%2BPBZWVLpaw874h8of%2Fnvd8WNEkuXkJA19nUrFk7faiPlHQd79YMv%2FXaFva2es%2FjzQ8jtfkIJg%2BsaxdFoqF643KTwUNKxdAz0s2JY68qU0zX32T2sIlJdxOm8wEdYxsi0sSxJITZI2gOXXsbFSmitDhrbh1ef1husbgbrAXrJNGIikn%2BfODnxiuWjwlPFwju8YGuBCNH513TywP4WyHeW76j5ql%2FpWJ8jyLQlnqJeKgTOhq6AxNj27YQ3UGyefOEotUmk3B53Q%2FDu5RDfTFIXJtVdy26FltHirSO1lFx%2FCbhHGAfSqPpSsbJJiqEMKjEkr0GOqUBS0Ioxv%2B%2BqKdLfulB1C6XuM3OFyv4eOPrRIrB62oBf1XHh4A5dFYXliWcFgmKhiFhGJEvAu2BOrYp2WwvDYhEydWDAg7FfKWo5VnVwbW3mm5rZE%2FjqvZTHc9shJAEyw4Udk0NXJmA%2B2vPQ204I%2Bao7ZpWpeCfti2KgjitoJyxOsd4Zpi7IP6PfTPjeKUJxSo1fP9M2pLwY%2Be7VaIgTUDmyYQkhGDp&X-Amz-Signature=cb60347fe28d7772eb9b60441b723d613f6d21b89af29f30f7db517132c20e46&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W7WY2X7M%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQDgJ4pnMyK8AUzwnOhKkultcONGiaMuEgDEDBK2c%2BCryAIgSSjPzbfIogvO0o2BIjGsMKDV0OLx5KVPNqH46dYUtCYq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDI5VKc040esq61XPXCrcAyKLMM7qMgeLqrvvl6mQgJ1imPkOz7hSmTTgQrCgA%2FZKdS5eBVMCyGrhpSjLl8hI0382M5sBazmbcQ0q3y0%2FZkVpQDSSHHL0d5ExR7Ar9hvDAZDtWYlU0Xm%2FlR2LJbqBOhp9lybXiqk68S%2BFOXiiLAoRKbyW9VyT%2BswlQsFSL09Gut926YbbhjVar2RxrEHn9V0gP0n8WFzNyt%2F0yrkDbyaR2DzftSvxXnjd5p33dU0qF4C0patjk2fPRnsPF8eMJxpfWJCRWyYvNC96QG9Uz%2BD9WAB%2BJ5WcaOKVROifW9uEVQ2aHMu2C8%2B1nLsYiU1MS%2BPBZWVLpaw874h8of%2Fnvd8WNEkuXkJA19nUrFk7faiPlHQd79YMv%2FXaFva2es%2FjzQ8jtfkIJg%2BsaxdFoqF643KTwUNKxdAz0s2JY68qU0zX32T2sIlJdxOm8wEdYxsi0sSxJITZI2gOXXsbFSmitDhrbh1ef1husbgbrAXrJNGIikn%2BfODnxiuWjwlPFwju8YGuBCNH513TywP4WyHeW76j5ql%2FpWJ8jyLQlnqJeKgTOhq6AxNj27YQ3UGyefOEotUmk3B53Q%2FDu5RDfTFIXJtVdy26FltHirSO1lFx%2FCbhHGAfSqPpSsbJJiqEMKjEkr0GOqUBS0Ioxv%2B%2BqKdLfulB1C6XuM3OFyv4eOPrRIrB62oBf1XHh4A5dFYXliWcFgmKhiFhGJEvAu2BOrYp2WwvDYhEydWDAg7FfKWo5VnVwbW3mm5rZE%2FjqvZTHc9shJAEyw4Udk0NXJmA%2B2vPQ204I%2Bao7ZpWpeCfti2KgjitoJyxOsd4Zpi7IP6PfTPjeKUJxSo1fP9M2pLwY%2Be7VaIgTUDmyYQkhGDp&X-Amz-Signature=71f62551471490e36397c8f70ae4adc429915c1024145b614ee7a64679cb7e6a&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W7WY2X7M%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQDgJ4pnMyK8AUzwnOhKkultcONGiaMuEgDEDBK2c%2BCryAIgSSjPzbfIogvO0o2BIjGsMKDV0OLx5KVPNqH46dYUtCYq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDI5VKc040esq61XPXCrcAyKLMM7qMgeLqrvvl6mQgJ1imPkOz7hSmTTgQrCgA%2FZKdS5eBVMCyGrhpSjLl8hI0382M5sBazmbcQ0q3y0%2FZkVpQDSSHHL0d5ExR7Ar9hvDAZDtWYlU0Xm%2FlR2LJbqBOhp9lybXiqk68S%2BFOXiiLAoRKbyW9VyT%2BswlQsFSL09Gut926YbbhjVar2RxrEHn9V0gP0n8WFzNyt%2F0yrkDbyaR2DzftSvxXnjd5p33dU0qF4C0patjk2fPRnsPF8eMJxpfWJCRWyYvNC96QG9Uz%2BD9WAB%2BJ5WcaOKVROifW9uEVQ2aHMu2C8%2B1nLsYiU1MS%2BPBZWVLpaw874h8of%2Fnvd8WNEkuXkJA19nUrFk7faiPlHQd79YMv%2FXaFva2es%2FjzQ8jtfkIJg%2BsaxdFoqF643KTwUNKxdAz0s2JY68qU0zX32T2sIlJdxOm8wEdYxsi0sSxJITZI2gOXXsbFSmitDhrbh1ef1husbgbrAXrJNGIikn%2BfODnxiuWjwlPFwju8YGuBCNH513TywP4WyHeW76j5ql%2FpWJ8jyLQlnqJeKgTOhq6AxNj27YQ3UGyefOEotUmk3B53Q%2FDu5RDfTFIXJtVdy26FltHirSO1lFx%2FCbhHGAfSqPpSsbJJiqEMKjEkr0GOqUBS0Ioxv%2B%2BqKdLfulB1C6XuM3OFyv4eOPrRIrB62oBf1XHh4A5dFYXliWcFgmKhiFhGJEvAu2BOrYp2WwvDYhEydWDAg7FfKWo5VnVwbW3mm5rZE%2FjqvZTHc9shJAEyw4Udk0NXJmA%2B2vPQ204I%2Bao7ZpWpeCfti2KgjitoJyxOsd4Zpi7IP6PfTPjeKUJxSo1fP9M2pLwY%2Be7VaIgTUDmyYQkhGDp&X-Amz-Signature=f70254cd705c88cd61dd99dda9d9426249539375ba3b2fdc35d6e0308731fc71&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W7WY2X7M%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQDgJ4pnMyK8AUzwnOhKkultcONGiaMuEgDEDBK2c%2BCryAIgSSjPzbfIogvO0o2BIjGsMKDV0OLx5KVPNqH46dYUtCYq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDI5VKc040esq61XPXCrcAyKLMM7qMgeLqrvvl6mQgJ1imPkOz7hSmTTgQrCgA%2FZKdS5eBVMCyGrhpSjLl8hI0382M5sBazmbcQ0q3y0%2FZkVpQDSSHHL0d5ExR7Ar9hvDAZDtWYlU0Xm%2FlR2LJbqBOhp9lybXiqk68S%2BFOXiiLAoRKbyW9VyT%2BswlQsFSL09Gut926YbbhjVar2RxrEHn9V0gP0n8WFzNyt%2F0yrkDbyaR2DzftSvxXnjd5p33dU0qF4C0patjk2fPRnsPF8eMJxpfWJCRWyYvNC96QG9Uz%2BD9WAB%2BJ5WcaOKVROifW9uEVQ2aHMu2C8%2B1nLsYiU1MS%2BPBZWVLpaw874h8of%2Fnvd8WNEkuXkJA19nUrFk7faiPlHQd79YMv%2FXaFva2es%2FjzQ8jtfkIJg%2BsaxdFoqF643KTwUNKxdAz0s2JY68qU0zX32T2sIlJdxOm8wEdYxsi0sSxJITZI2gOXXsbFSmitDhrbh1ef1husbgbrAXrJNGIikn%2BfODnxiuWjwlPFwju8YGuBCNH513TywP4WyHeW76j5ql%2FpWJ8jyLQlnqJeKgTOhq6AxNj27YQ3UGyefOEotUmk3B53Q%2FDu5RDfTFIXJtVdy26FltHirSO1lFx%2FCbhHGAfSqPpSsbJJiqEMKjEkr0GOqUBS0Ioxv%2B%2BqKdLfulB1C6XuM3OFyv4eOPrRIrB62oBf1XHh4A5dFYXliWcFgmKhiFhGJEvAu2BOrYp2WwvDYhEydWDAg7FfKWo5VnVwbW3mm5rZE%2FjqvZTHc9shJAEyw4Udk0NXJmA%2B2vPQ204I%2Bao7ZpWpeCfti2KgjitoJyxOsd4Zpi7IP6PfTPjeKUJxSo1fP9M2pLwY%2Be7VaIgTUDmyYQkhGDp&X-Amz-Signature=aeeff6e01489363eb47c0fea4bbb63c8348bef7a453053a643de62b0f97cceea&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W7WY2X7M%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQDgJ4pnMyK8AUzwnOhKkultcONGiaMuEgDEDBK2c%2BCryAIgSSjPzbfIogvO0o2BIjGsMKDV0OLx5KVPNqH46dYUtCYq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDI5VKc040esq61XPXCrcAyKLMM7qMgeLqrvvl6mQgJ1imPkOz7hSmTTgQrCgA%2FZKdS5eBVMCyGrhpSjLl8hI0382M5sBazmbcQ0q3y0%2FZkVpQDSSHHL0d5ExR7Ar9hvDAZDtWYlU0Xm%2FlR2LJbqBOhp9lybXiqk68S%2BFOXiiLAoRKbyW9VyT%2BswlQsFSL09Gut926YbbhjVar2RxrEHn9V0gP0n8WFzNyt%2F0yrkDbyaR2DzftSvxXnjd5p33dU0qF4C0patjk2fPRnsPF8eMJxpfWJCRWyYvNC96QG9Uz%2BD9WAB%2BJ5WcaOKVROifW9uEVQ2aHMu2C8%2B1nLsYiU1MS%2BPBZWVLpaw874h8of%2Fnvd8WNEkuXkJA19nUrFk7faiPlHQd79YMv%2FXaFva2es%2FjzQ8jtfkIJg%2BsaxdFoqF643KTwUNKxdAz0s2JY68qU0zX32T2sIlJdxOm8wEdYxsi0sSxJITZI2gOXXsbFSmitDhrbh1ef1husbgbrAXrJNGIikn%2BfODnxiuWjwlPFwju8YGuBCNH513TywP4WyHeW76j5ql%2FpWJ8jyLQlnqJeKgTOhq6AxNj27YQ3UGyefOEotUmk3B53Q%2FDu5RDfTFIXJtVdy26FltHirSO1lFx%2FCbhHGAfSqPpSsbJJiqEMKjEkr0GOqUBS0Ioxv%2B%2BqKdLfulB1C6XuM3OFyv4eOPrRIrB62oBf1XHh4A5dFYXliWcFgmKhiFhGJEvAu2BOrYp2WwvDYhEydWDAg7FfKWo5VnVwbW3mm5rZE%2FjqvZTHc9shJAEyw4Udk0NXJmA%2B2vPQ204I%2Bao7ZpWpeCfti2KgjitoJyxOsd4Zpi7IP6PfTPjeKUJxSo1fP9M2pLwY%2Be7VaIgTUDmyYQkhGDp&X-Amz-Signature=21011351125c6eebe9bf79838b1a4855966eb59c94656d500b62d8e049f91d75&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W7WY2X7M%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQDgJ4pnMyK8AUzwnOhKkultcONGiaMuEgDEDBK2c%2BCryAIgSSjPzbfIogvO0o2BIjGsMKDV0OLx5KVPNqH46dYUtCYq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDI5VKc040esq61XPXCrcAyKLMM7qMgeLqrvvl6mQgJ1imPkOz7hSmTTgQrCgA%2FZKdS5eBVMCyGrhpSjLl8hI0382M5sBazmbcQ0q3y0%2FZkVpQDSSHHL0d5ExR7Ar9hvDAZDtWYlU0Xm%2FlR2LJbqBOhp9lybXiqk68S%2BFOXiiLAoRKbyW9VyT%2BswlQsFSL09Gut926YbbhjVar2RxrEHn9V0gP0n8WFzNyt%2F0yrkDbyaR2DzftSvxXnjd5p33dU0qF4C0patjk2fPRnsPF8eMJxpfWJCRWyYvNC96QG9Uz%2BD9WAB%2BJ5WcaOKVROifW9uEVQ2aHMu2C8%2B1nLsYiU1MS%2BPBZWVLpaw874h8of%2Fnvd8WNEkuXkJA19nUrFk7faiPlHQd79YMv%2FXaFva2es%2FjzQ8jtfkIJg%2BsaxdFoqF643KTwUNKxdAz0s2JY68qU0zX32T2sIlJdxOm8wEdYxsi0sSxJITZI2gOXXsbFSmitDhrbh1ef1husbgbrAXrJNGIikn%2BfODnxiuWjwlPFwju8YGuBCNH513TywP4WyHeW76j5ql%2FpWJ8jyLQlnqJeKgTOhq6AxNj27YQ3UGyefOEotUmk3B53Q%2FDu5RDfTFIXJtVdy26FltHirSO1lFx%2FCbhHGAfSqPpSsbJJiqEMKjEkr0GOqUBS0Ioxv%2B%2BqKdLfulB1C6XuM3OFyv4eOPrRIrB62oBf1XHh4A5dFYXliWcFgmKhiFhGJEvAu2BOrYp2WwvDYhEydWDAg7FfKWo5VnVwbW3mm5rZE%2FjqvZTHc9shJAEyw4Udk0NXJmA%2B2vPQ204I%2Bao7ZpWpeCfti2KgjitoJyxOsd4Zpi7IP6PfTPjeKUJxSo1fP9M2pLwY%2Be7VaIgTUDmyYQkhGDp&X-Amz-Signature=8bcb6ffa819ee54b2f3b2f77717dfe60f87b267afb8340d9d45e526823600d8d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XTFZDXRD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQCgW6BF4TcyElBCKifu78PZlt9F4rxJHimCHsndKGOrZAIgNZv9MYrLMVDSJErhDCKV5F1D222f3ykDzvVfqhhLF6wq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDMfaIAvqfAaFLKh%2FUyrcA9K5rjDH2cMxhucVY3QSKRahDfO7utbeK4LZuAg97sMq%2FcMnyXl8Zyyr4LWmC07K10lAct2WyqnUEPxCAK27vNYNVnld3bly2a1yYSbx%2BmtzkrihX%2FTcaKAO%2BvXce343vZaqj20iT2zdOiwMc7TUgv0NKtVanoxrx93jMNAQC%2BRg9d0wpa2W6phBgaZrS69mkrls5w1X6kXuakuS78jo5qE%2FpW09oSBjhL7dT6Mfjdmx6IY2a4JSZwYRqlZeMeI3aI66Dym4QEcyqa5Nx68FzdtmkagsQaZREiqGKgEFtPDoqVV4h11dvFOpSE950ZaCC%2FaykdxZjFKotfecqTUOtDELIQP%2B6ayWrvsAUAYTSta2uCfWJasBRoWZnEl%2BeASMm5slWYpbiaZ7Vh5GcMBC7ohpkCY7Q1yNJJPDYw4bZTDvs58y8G2SsXOlkQ1K8XI2m0aayYQTPqdb%2Bhxn%2FB46luHCrRRKZpSnIdMyHio06kfflQ7zJoRjkPoKe4BtyEvSSkhtmjOC54hxQq%2Ff0sjZ7zVEm%2FjW0nx3n5GskTcUrkh23ipu6YThRgf%2BRJps8f%2FvQO7dLcszyh8FmnksufKGXyKrw6obz16IaTIiDFU2Zne1119Kdq6HRcOrUp99MInEkr0GOqUBv%2BQRjQVukFbwugNOmk1a6IxB1UsH40Uom33QJEu3wu5dFB41lV6rlE9WAo48DubYE1Utr%2F4fXUJ%2FF45dq0xCssGIw6UF35CGKhZ6sASghv8hOdq6cwdorfNluplQESTssBiZzX4VUKZKugTvmk1El8Oc8YWc4J3HBIsFPkcz9rbIDaDk%2Fj4FST3eS6N%2FuuFhMziG9cVUFNRO%2FZ6pTiVp%2FPrehp10&X-Amz-Signature=b2eba2d7296c41d5bbaa47e64a468cb830aadf70f74442be114b9982be638bf0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XTFZDXRD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQCgW6BF4TcyElBCKifu78PZlt9F4rxJHimCHsndKGOrZAIgNZv9MYrLMVDSJErhDCKV5F1D222f3ykDzvVfqhhLF6wq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDMfaIAvqfAaFLKh%2FUyrcA9K5rjDH2cMxhucVY3QSKRahDfO7utbeK4LZuAg97sMq%2FcMnyXl8Zyyr4LWmC07K10lAct2WyqnUEPxCAK27vNYNVnld3bly2a1yYSbx%2BmtzkrihX%2FTcaKAO%2BvXce343vZaqj20iT2zdOiwMc7TUgv0NKtVanoxrx93jMNAQC%2BRg9d0wpa2W6phBgaZrS69mkrls5w1X6kXuakuS78jo5qE%2FpW09oSBjhL7dT6Mfjdmx6IY2a4JSZwYRqlZeMeI3aI66Dym4QEcyqa5Nx68FzdtmkagsQaZREiqGKgEFtPDoqVV4h11dvFOpSE950ZaCC%2FaykdxZjFKotfecqTUOtDELIQP%2B6ayWrvsAUAYTSta2uCfWJasBRoWZnEl%2BeASMm5slWYpbiaZ7Vh5GcMBC7ohpkCY7Q1yNJJPDYw4bZTDvs58y8G2SsXOlkQ1K8XI2m0aayYQTPqdb%2Bhxn%2FB46luHCrRRKZpSnIdMyHio06kfflQ7zJoRjkPoKe4BtyEvSSkhtmjOC54hxQq%2Ff0sjZ7zVEm%2FjW0nx3n5GskTcUrkh23ipu6YThRgf%2BRJps8f%2FvQO7dLcszyh8FmnksufKGXyKrw6obz16IaTIiDFU2Zne1119Kdq6HRcOrUp99MInEkr0GOqUBv%2BQRjQVukFbwugNOmk1a6IxB1UsH40Uom33QJEu3wu5dFB41lV6rlE9WAo48DubYE1Utr%2F4fXUJ%2FF45dq0xCssGIw6UF35CGKhZ6sASghv8hOdq6cwdorfNluplQESTssBiZzX4VUKZKugTvmk1El8Oc8YWc4J3HBIsFPkcz9rbIDaDk%2Fj4FST3eS6N%2FuuFhMziG9cVUFNRO%2FZ6pTiVp%2FPrehp10&X-Amz-Signature=c5d9a7ea9b3ff321fc35abb23056c949bbba659d4f0a612dd76a7fe4e2425e9b&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
