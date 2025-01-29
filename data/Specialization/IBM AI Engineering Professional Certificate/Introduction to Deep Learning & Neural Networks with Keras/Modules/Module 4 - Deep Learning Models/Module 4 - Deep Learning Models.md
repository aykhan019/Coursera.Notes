

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665VGQWQHM%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFbaxD14072lpy%2FS1NWoD1kSH1s70A0wv6GCwhGxsOYNAiEA9fWaPfxlBOqGJbCSTjxooiXH7HwsbJcvY5V9d0L1Wl0qiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMldtDd0LvDFAy2C0SrcAzwOiHIc47dTQaKxk8%2BIlOlXWg2zaIyPneA0tY9mQBDpcfq9ZicdTv320SMoggPq2Zjtx9EJJcWsBEux6iDQYNZJTdyBX94V%2BU%2FE1Q6UqKDZuBi4x4n3ly288QD%2B4%2FZkpASOC%2F9oqs2%2FKXfK3zyMY%2BV%2B%2FV%2F3w83Izsi25iUJcRHvTT2SIytNZRWGWivSlS5e0Z5jbvguzGLXV6TOIHWtUKfAu6n9yY2CllawFgDZyPMTPcjJPmMkz6mzPAPS4Tbw82bUEXR%2FHD0p1ZIMsucVQ%2BH3GX8DOhtxraRlBdfuwWDSfxh6w53mpmCTUuWFtNatgdH0Q6Ph8o%2BcmY3ik%2Fyr628uRsR2RvajvJ1iRKTknziS8wSKJFofvwk1XABH9TPr1a31t9GnVlK4RqecuLogs2Po9CV0maOXW3wo5BR%2Bl0cJqF%2BpONNWYeHqghgW6OtsFBzLVgcZmPtPeqnSgDWxQxVA4emBVxijWnsXd2HwxKoRv1VIJ2N%2BCpccTbYMpFLFSU31g9SXGHr%2Bah8wfWAK4okf4caDS82W1n4d%2BhIKjRiUobudpvgZ2EeKXiDcKAIIl%2BUZB9nCQurDXjktPCzio5wf1pg03NwqfhDqhUVoP7zzHHPBA%2BaPV%2B1JClouMLKE6bwGOqUBUnjAhjG4W9jJg7DxP5crD9nHvaZdQQwgfpJGdCJp%2BuE7MriyhFVYZkFceUgE81H39B6ie6OuRR2yvomzhYoIawluqZgNmeHhwM9JNFKda7AJ7hsGdrByX0TuraIwelCvky8vP800rlyhlujwt3t4UX47lkQgvL71KNUow5lG4og7ne1o%2FVGi6cIUpf7DVm%2FTA2keBFv3y2bDojtq5IgJARTnDNKB&X-Amz-Signature=97e37180c1c4a84e090303c4d34508d4ec049f0e79b50e5a426eb382dc20c5fb&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665VGQWQHM%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFbaxD14072lpy%2FS1NWoD1kSH1s70A0wv6GCwhGxsOYNAiEA9fWaPfxlBOqGJbCSTjxooiXH7HwsbJcvY5V9d0L1Wl0qiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMldtDd0LvDFAy2C0SrcAzwOiHIc47dTQaKxk8%2BIlOlXWg2zaIyPneA0tY9mQBDpcfq9ZicdTv320SMoggPq2Zjtx9EJJcWsBEux6iDQYNZJTdyBX94V%2BU%2FE1Q6UqKDZuBi4x4n3ly288QD%2B4%2FZkpASOC%2F9oqs2%2FKXfK3zyMY%2BV%2B%2FV%2F3w83Izsi25iUJcRHvTT2SIytNZRWGWivSlS5e0Z5jbvguzGLXV6TOIHWtUKfAu6n9yY2CllawFgDZyPMTPcjJPmMkz6mzPAPS4Tbw82bUEXR%2FHD0p1ZIMsucVQ%2BH3GX8DOhtxraRlBdfuwWDSfxh6w53mpmCTUuWFtNatgdH0Q6Ph8o%2BcmY3ik%2Fyr628uRsR2RvajvJ1iRKTknziS8wSKJFofvwk1XABH9TPr1a31t9GnVlK4RqecuLogs2Po9CV0maOXW3wo5BR%2Bl0cJqF%2BpONNWYeHqghgW6OtsFBzLVgcZmPtPeqnSgDWxQxVA4emBVxijWnsXd2HwxKoRv1VIJ2N%2BCpccTbYMpFLFSU31g9SXGHr%2Bah8wfWAK4okf4caDS82W1n4d%2BhIKjRiUobudpvgZ2EeKXiDcKAIIl%2BUZB9nCQurDXjktPCzio5wf1pg03NwqfhDqhUVoP7zzHHPBA%2BaPV%2B1JClouMLKE6bwGOqUBUnjAhjG4W9jJg7DxP5crD9nHvaZdQQwgfpJGdCJp%2BuE7MriyhFVYZkFceUgE81H39B6ie6OuRR2yvomzhYoIawluqZgNmeHhwM9JNFKda7AJ7hsGdrByX0TuraIwelCvky8vP800rlyhlujwt3t4UX47lkQgvL71KNUow5lG4og7ne1o%2FVGi6cIUpf7DVm%2FTA2keBFv3y2bDojtq5IgJARTnDNKB&X-Amz-Signature=2a63eeeadbecc5e2e2172106bb4975a4f1e37fad204e75d22c8ff583c37bd7f2&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665VGQWQHM%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFbaxD14072lpy%2FS1NWoD1kSH1s70A0wv6GCwhGxsOYNAiEA9fWaPfxlBOqGJbCSTjxooiXH7HwsbJcvY5V9d0L1Wl0qiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMldtDd0LvDFAy2C0SrcAzwOiHIc47dTQaKxk8%2BIlOlXWg2zaIyPneA0tY9mQBDpcfq9ZicdTv320SMoggPq2Zjtx9EJJcWsBEux6iDQYNZJTdyBX94V%2BU%2FE1Q6UqKDZuBi4x4n3ly288QD%2B4%2FZkpASOC%2F9oqs2%2FKXfK3zyMY%2BV%2B%2FV%2F3w83Izsi25iUJcRHvTT2SIytNZRWGWivSlS5e0Z5jbvguzGLXV6TOIHWtUKfAu6n9yY2CllawFgDZyPMTPcjJPmMkz6mzPAPS4Tbw82bUEXR%2FHD0p1ZIMsucVQ%2BH3GX8DOhtxraRlBdfuwWDSfxh6w53mpmCTUuWFtNatgdH0Q6Ph8o%2BcmY3ik%2Fyr628uRsR2RvajvJ1iRKTknziS8wSKJFofvwk1XABH9TPr1a31t9GnVlK4RqecuLogs2Po9CV0maOXW3wo5BR%2Bl0cJqF%2BpONNWYeHqghgW6OtsFBzLVgcZmPtPeqnSgDWxQxVA4emBVxijWnsXd2HwxKoRv1VIJ2N%2BCpccTbYMpFLFSU31g9SXGHr%2Bah8wfWAK4okf4caDS82W1n4d%2BhIKjRiUobudpvgZ2EeKXiDcKAIIl%2BUZB9nCQurDXjktPCzio5wf1pg03NwqfhDqhUVoP7zzHHPBA%2BaPV%2B1JClouMLKE6bwGOqUBUnjAhjG4W9jJg7DxP5crD9nHvaZdQQwgfpJGdCJp%2BuE7MriyhFVYZkFceUgE81H39B6ie6OuRR2yvomzhYoIawluqZgNmeHhwM9JNFKda7AJ7hsGdrByX0TuraIwelCvky8vP800rlyhlujwt3t4UX47lkQgvL71KNUow5lG4og7ne1o%2FVGi6cIUpf7DVm%2FTA2keBFv3y2bDojtq5IgJARTnDNKB&X-Amz-Signature=409ae31f66a85f61e83ec972e0a88379ff234c52644485b4f8f4c9f2ef421a1f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665VGQWQHM%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFbaxD14072lpy%2FS1NWoD1kSH1s70A0wv6GCwhGxsOYNAiEA9fWaPfxlBOqGJbCSTjxooiXH7HwsbJcvY5V9d0L1Wl0qiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMldtDd0LvDFAy2C0SrcAzwOiHIc47dTQaKxk8%2BIlOlXWg2zaIyPneA0tY9mQBDpcfq9ZicdTv320SMoggPq2Zjtx9EJJcWsBEux6iDQYNZJTdyBX94V%2BU%2FE1Q6UqKDZuBi4x4n3ly288QD%2B4%2FZkpASOC%2F9oqs2%2FKXfK3zyMY%2BV%2B%2FV%2F3w83Izsi25iUJcRHvTT2SIytNZRWGWivSlS5e0Z5jbvguzGLXV6TOIHWtUKfAu6n9yY2CllawFgDZyPMTPcjJPmMkz6mzPAPS4Tbw82bUEXR%2FHD0p1ZIMsucVQ%2BH3GX8DOhtxraRlBdfuwWDSfxh6w53mpmCTUuWFtNatgdH0Q6Ph8o%2BcmY3ik%2Fyr628uRsR2RvajvJ1iRKTknziS8wSKJFofvwk1XABH9TPr1a31t9GnVlK4RqecuLogs2Po9CV0maOXW3wo5BR%2Bl0cJqF%2BpONNWYeHqghgW6OtsFBzLVgcZmPtPeqnSgDWxQxVA4emBVxijWnsXd2HwxKoRv1VIJ2N%2BCpccTbYMpFLFSU31g9SXGHr%2Bah8wfWAK4okf4caDS82W1n4d%2BhIKjRiUobudpvgZ2EeKXiDcKAIIl%2BUZB9nCQurDXjktPCzio5wf1pg03NwqfhDqhUVoP7zzHHPBA%2BaPV%2B1JClouMLKE6bwGOqUBUnjAhjG4W9jJg7DxP5crD9nHvaZdQQwgfpJGdCJp%2BuE7MriyhFVYZkFceUgE81H39B6ie6OuRR2yvomzhYoIawluqZgNmeHhwM9JNFKda7AJ7hsGdrByX0TuraIwelCvky8vP800rlyhlujwt3t4UX47lkQgvL71KNUow5lG4og7ne1o%2FVGi6cIUpf7DVm%2FTA2keBFv3y2bDojtq5IgJARTnDNKB&X-Amz-Signature=2b7914f35f4d0b5a2ad7616eca53e0d1f36e1a63b65a56d25b991bbc1f1106b2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665VGQWQHM%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFbaxD14072lpy%2FS1NWoD1kSH1s70A0wv6GCwhGxsOYNAiEA9fWaPfxlBOqGJbCSTjxooiXH7HwsbJcvY5V9d0L1Wl0qiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMldtDd0LvDFAy2C0SrcAzwOiHIc47dTQaKxk8%2BIlOlXWg2zaIyPneA0tY9mQBDpcfq9ZicdTv320SMoggPq2Zjtx9EJJcWsBEux6iDQYNZJTdyBX94V%2BU%2FE1Q6UqKDZuBi4x4n3ly288QD%2B4%2FZkpASOC%2F9oqs2%2FKXfK3zyMY%2BV%2B%2FV%2F3w83Izsi25iUJcRHvTT2SIytNZRWGWivSlS5e0Z5jbvguzGLXV6TOIHWtUKfAu6n9yY2CllawFgDZyPMTPcjJPmMkz6mzPAPS4Tbw82bUEXR%2FHD0p1ZIMsucVQ%2BH3GX8DOhtxraRlBdfuwWDSfxh6w53mpmCTUuWFtNatgdH0Q6Ph8o%2BcmY3ik%2Fyr628uRsR2RvajvJ1iRKTknziS8wSKJFofvwk1XABH9TPr1a31t9GnVlK4RqecuLogs2Po9CV0maOXW3wo5BR%2Bl0cJqF%2BpONNWYeHqghgW6OtsFBzLVgcZmPtPeqnSgDWxQxVA4emBVxijWnsXd2HwxKoRv1VIJ2N%2BCpccTbYMpFLFSU31g9SXGHr%2Bah8wfWAK4okf4caDS82W1n4d%2BhIKjRiUobudpvgZ2EeKXiDcKAIIl%2BUZB9nCQurDXjktPCzio5wf1pg03NwqfhDqhUVoP7zzHHPBA%2BaPV%2B1JClouMLKE6bwGOqUBUnjAhjG4W9jJg7DxP5crD9nHvaZdQQwgfpJGdCJp%2BuE7MriyhFVYZkFceUgE81H39B6ie6OuRR2yvomzhYoIawluqZgNmeHhwM9JNFKda7AJ7hsGdrByX0TuraIwelCvky8vP800rlyhlujwt3t4UX47lkQgvL71KNUow5lG4og7ne1o%2FVGi6cIUpf7DVm%2FTA2keBFv3y2bDojtq5IgJARTnDNKB&X-Amz-Signature=e097a6cd708ebd36692f81d41234ec9de05532a7542838b12eb4c95a70547d50&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665VGQWQHM%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFbaxD14072lpy%2FS1NWoD1kSH1s70A0wv6GCwhGxsOYNAiEA9fWaPfxlBOqGJbCSTjxooiXH7HwsbJcvY5V9d0L1Wl0qiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMldtDd0LvDFAy2C0SrcAzwOiHIc47dTQaKxk8%2BIlOlXWg2zaIyPneA0tY9mQBDpcfq9ZicdTv320SMoggPq2Zjtx9EJJcWsBEux6iDQYNZJTdyBX94V%2BU%2FE1Q6UqKDZuBi4x4n3ly288QD%2B4%2FZkpASOC%2F9oqs2%2FKXfK3zyMY%2BV%2B%2FV%2F3w83Izsi25iUJcRHvTT2SIytNZRWGWivSlS5e0Z5jbvguzGLXV6TOIHWtUKfAu6n9yY2CllawFgDZyPMTPcjJPmMkz6mzPAPS4Tbw82bUEXR%2FHD0p1ZIMsucVQ%2BH3GX8DOhtxraRlBdfuwWDSfxh6w53mpmCTUuWFtNatgdH0Q6Ph8o%2BcmY3ik%2Fyr628uRsR2RvajvJ1iRKTknziS8wSKJFofvwk1XABH9TPr1a31t9GnVlK4RqecuLogs2Po9CV0maOXW3wo5BR%2Bl0cJqF%2BpONNWYeHqghgW6OtsFBzLVgcZmPtPeqnSgDWxQxVA4emBVxijWnsXd2HwxKoRv1VIJ2N%2BCpccTbYMpFLFSU31g9SXGHr%2Bah8wfWAK4okf4caDS82W1n4d%2BhIKjRiUobudpvgZ2EeKXiDcKAIIl%2BUZB9nCQurDXjktPCzio5wf1pg03NwqfhDqhUVoP7zzHHPBA%2BaPV%2B1JClouMLKE6bwGOqUBUnjAhjG4W9jJg7DxP5crD9nHvaZdQQwgfpJGdCJp%2BuE7MriyhFVYZkFceUgE81H39B6ie6OuRR2yvomzhYoIawluqZgNmeHhwM9JNFKda7AJ7hsGdrByX0TuraIwelCvky8vP800rlyhlujwt3t4UX47lkQgvL71KNUow5lG4og7ne1o%2FVGi6cIUpf7DVm%2FTA2keBFv3y2bDojtq5IgJARTnDNKB&X-Amz-Signature=dae1778bfe4e2a6e9fdf87c2323094390788a0104f18a955aa4451101ed88cc9&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665VGQWQHM%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFbaxD14072lpy%2FS1NWoD1kSH1s70A0wv6GCwhGxsOYNAiEA9fWaPfxlBOqGJbCSTjxooiXH7HwsbJcvY5V9d0L1Wl0qiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMldtDd0LvDFAy2C0SrcAzwOiHIc47dTQaKxk8%2BIlOlXWg2zaIyPneA0tY9mQBDpcfq9ZicdTv320SMoggPq2Zjtx9EJJcWsBEux6iDQYNZJTdyBX94V%2BU%2FE1Q6UqKDZuBi4x4n3ly288QD%2B4%2FZkpASOC%2F9oqs2%2FKXfK3zyMY%2BV%2B%2FV%2F3w83Izsi25iUJcRHvTT2SIytNZRWGWivSlS5e0Z5jbvguzGLXV6TOIHWtUKfAu6n9yY2CllawFgDZyPMTPcjJPmMkz6mzPAPS4Tbw82bUEXR%2FHD0p1ZIMsucVQ%2BH3GX8DOhtxraRlBdfuwWDSfxh6w53mpmCTUuWFtNatgdH0Q6Ph8o%2BcmY3ik%2Fyr628uRsR2RvajvJ1iRKTknziS8wSKJFofvwk1XABH9TPr1a31t9GnVlK4RqecuLogs2Po9CV0maOXW3wo5BR%2Bl0cJqF%2BpONNWYeHqghgW6OtsFBzLVgcZmPtPeqnSgDWxQxVA4emBVxijWnsXd2HwxKoRv1VIJ2N%2BCpccTbYMpFLFSU31g9SXGHr%2Bah8wfWAK4okf4caDS82W1n4d%2BhIKjRiUobudpvgZ2EeKXiDcKAIIl%2BUZB9nCQurDXjktPCzio5wf1pg03NwqfhDqhUVoP7zzHHPBA%2BaPV%2B1JClouMLKE6bwGOqUBUnjAhjG4W9jJg7DxP5crD9nHvaZdQQwgfpJGdCJp%2BuE7MriyhFVYZkFceUgE81H39B6ie6OuRR2yvomzhYoIawluqZgNmeHhwM9JNFKda7AJ7hsGdrByX0TuraIwelCvky8vP800rlyhlujwt3t4UX47lkQgvL71KNUow5lG4og7ne1o%2FVGi6cIUpf7DVm%2FTA2keBFv3y2bDojtq5IgJARTnDNKB&X-Amz-Signature=74ca8efedc057c720cf5febf121df4c80de0f3df64d36b84ccd03eeee2f2003f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665VGQWQHM%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFbaxD14072lpy%2FS1NWoD1kSH1s70A0wv6GCwhGxsOYNAiEA9fWaPfxlBOqGJbCSTjxooiXH7HwsbJcvY5V9d0L1Wl0qiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMldtDd0LvDFAy2C0SrcAzwOiHIc47dTQaKxk8%2BIlOlXWg2zaIyPneA0tY9mQBDpcfq9ZicdTv320SMoggPq2Zjtx9EJJcWsBEux6iDQYNZJTdyBX94V%2BU%2FE1Q6UqKDZuBi4x4n3ly288QD%2B4%2FZkpASOC%2F9oqs2%2FKXfK3zyMY%2BV%2B%2FV%2F3w83Izsi25iUJcRHvTT2SIytNZRWGWivSlS5e0Z5jbvguzGLXV6TOIHWtUKfAu6n9yY2CllawFgDZyPMTPcjJPmMkz6mzPAPS4Tbw82bUEXR%2FHD0p1ZIMsucVQ%2BH3GX8DOhtxraRlBdfuwWDSfxh6w53mpmCTUuWFtNatgdH0Q6Ph8o%2BcmY3ik%2Fyr628uRsR2RvajvJ1iRKTknziS8wSKJFofvwk1XABH9TPr1a31t9GnVlK4RqecuLogs2Po9CV0maOXW3wo5BR%2Bl0cJqF%2BpONNWYeHqghgW6OtsFBzLVgcZmPtPeqnSgDWxQxVA4emBVxijWnsXd2HwxKoRv1VIJ2N%2BCpccTbYMpFLFSU31g9SXGHr%2Bah8wfWAK4okf4caDS82W1n4d%2BhIKjRiUobudpvgZ2EeKXiDcKAIIl%2BUZB9nCQurDXjktPCzio5wf1pg03NwqfhDqhUVoP7zzHHPBA%2BaPV%2B1JClouMLKE6bwGOqUBUnjAhjG4W9jJg7DxP5crD9nHvaZdQQwgfpJGdCJp%2BuE7MriyhFVYZkFceUgE81H39B6ie6OuRR2yvomzhYoIawluqZgNmeHhwM9JNFKda7AJ7hsGdrByX0TuraIwelCvky8vP800rlyhlujwt3t4UX47lkQgvL71KNUow5lG4og7ne1o%2FVGi6cIUpf7DVm%2FTA2keBFv3y2bDojtq5IgJARTnDNKB&X-Amz-Signature=68a1199ad5cfea0088fb49d41e129824cdec65871764401d572b68fd30318e6e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665VGQWQHM%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFbaxD14072lpy%2FS1NWoD1kSH1s70A0wv6GCwhGxsOYNAiEA9fWaPfxlBOqGJbCSTjxooiXH7HwsbJcvY5V9d0L1Wl0qiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMldtDd0LvDFAy2C0SrcAzwOiHIc47dTQaKxk8%2BIlOlXWg2zaIyPneA0tY9mQBDpcfq9ZicdTv320SMoggPq2Zjtx9EJJcWsBEux6iDQYNZJTdyBX94V%2BU%2FE1Q6UqKDZuBi4x4n3ly288QD%2B4%2FZkpASOC%2F9oqs2%2FKXfK3zyMY%2BV%2B%2FV%2F3w83Izsi25iUJcRHvTT2SIytNZRWGWivSlS5e0Z5jbvguzGLXV6TOIHWtUKfAu6n9yY2CllawFgDZyPMTPcjJPmMkz6mzPAPS4Tbw82bUEXR%2FHD0p1ZIMsucVQ%2BH3GX8DOhtxraRlBdfuwWDSfxh6w53mpmCTUuWFtNatgdH0Q6Ph8o%2BcmY3ik%2Fyr628uRsR2RvajvJ1iRKTknziS8wSKJFofvwk1XABH9TPr1a31t9GnVlK4RqecuLogs2Po9CV0maOXW3wo5BR%2Bl0cJqF%2BpONNWYeHqghgW6OtsFBzLVgcZmPtPeqnSgDWxQxVA4emBVxijWnsXd2HwxKoRv1VIJ2N%2BCpccTbYMpFLFSU31g9SXGHr%2Bah8wfWAK4okf4caDS82W1n4d%2BhIKjRiUobudpvgZ2EeKXiDcKAIIl%2BUZB9nCQurDXjktPCzio5wf1pg03NwqfhDqhUVoP7zzHHPBA%2BaPV%2B1JClouMLKE6bwGOqUBUnjAhjG4W9jJg7DxP5crD9nHvaZdQQwgfpJGdCJp%2BuE7MriyhFVYZkFceUgE81H39B6ie6OuRR2yvomzhYoIawluqZgNmeHhwM9JNFKda7AJ7hsGdrByX0TuraIwelCvky8vP800rlyhlujwt3t4UX47lkQgvL71KNUow5lG4og7ne1o%2FVGi6cIUpf7DVm%2FTA2keBFv3y2bDojtq5IgJARTnDNKB&X-Amz-Signature=250aa9bf50d7a52eb36982410a1d198c3539dd121d83f26eabccd292ac2a82a6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W4BB4BNM%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBzStyOUX8Ya44sH6PEUgQ09PYUzON3m9aIV41AFaWkIAiEAmg%2Bbm0vX%2FvaZutRL%2FOIq9iZULkIe%2BmfYlwDBIUL7dawqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIvZH2NgG4%2BYWAptryrcA5ksp5lJiJQOrPO3tyFytHYoFjE012gtTulPOB%2FbsgjjhEuvj7egDPCGs1begUWUXMpb1V6WVt3ZGquVWvOyIdrjS2n8H8QwH7%2FgMe%2BUTMRXZcLXkLnf%2FuvU9x6oKWluiqK4ZMlWBRJp0rIBF8jb37D7rUBB%2BwqHXQEBMRLd%2BE3Uyamg7Q4EH3gyb7Zv2MYhJgoog0c9inXqJH03yb%2FLDRqNoZAPmpfpA1PAIZMhEbTW6aa4HXdHacqlR2mOA2FVGDhrtxn3xpBCsCaE8VWIoQcHC24S%2F2MEHJPwd6%2FrnJ%2FXmN31A6GnM40rhKRcAdm7y7UFO8%2BKqmceNWNa3bawK11%2F5x7wvcpuXxXez7FnPa6huileJQb5QAFtydOMG3PwQeMi%2F9faApEC%2BAiE1jVvPzvRB9hT7SkC4%2FzUT8QXUaywKWGuR1lLcEJ8CoxLXm%2FLpZhJpajRSRbwixJbdp8wPRm3OupJFp1rHReo7%2B4Za5jT%2BrU%2FK2aB1hMo%2BbRbgEHi%2FEo75t660hcWLZePJNdX04ayVajKqguhe6IunGieaoKWrskjG3mcTxFtiacx8qL%2Bmuta0%2BYBpjumI244Qa56pmi5VAmA9X5mTOn05KIA6UQNvzPRWbxgEh%2BdUsS7MIGE6bwGOqUBPwd2B84%2FWwnT%2Bu9ipmKFtMcjL%2BOycD9%2FJPPJN65xljFZOAi4Yano5igETQ9N31BIYPq14xdTm2Yz1HWVvlG2W1bX0TFPByx%2FAlYs2XkRqkyucgg%2Fp%2BZUxThM9VfR9gYyAJSOFncidFIggowy39DnIjrjGVmeJkDo1f%2Bi6a78%2FQmcVGS9lEITv2uA4FMgxwtjD4Z8TWrO4tIB5vdpunzKVWaQzvs9&X-Amz-Signature=91f9574f46f568b20bebcb085bdf090d229aa0fd82306c5c3a6e9a57c2d0f0ed&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W4BB4BNM%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBzStyOUX8Ya44sH6PEUgQ09PYUzON3m9aIV41AFaWkIAiEAmg%2Bbm0vX%2FvaZutRL%2FOIq9iZULkIe%2BmfYlwDBIUL7dawqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIvZH2NgG4%2BYWAptryrcA5ksp5lJiJQOrPO3tyFytHYoFjE012gtTulPOB%2FbsgjjhEuvj7egDPCGs1begUWUXMpb1V6WVt3ZGquVWvOyIdrjS2n8H8QwH7%2FgMe%2BUTMRXZcLXkLnf%2FuvU9x6oKWluiqK4ZMlWBRJp0rIBF8jb37D7rUBB%2BwqHXQEBMRLd%2BE3Uyamg7Q4EH3gyb7Zv2MYhJgoog0c9inXqJH03yb%2FLDRqNoZAPmpfpA1PAIZMhEbTW6aa4HXdHacqlR2mOA2FVGDhrtxn3xpBCsCaE8VWIoQcHC24S%2F2MEHJPwd6%2FrnJ%2FXmN31A6GnM40rhKRcAdm7y7UFO8%2BKqmceNWNa3bawK11%2F5x7wvcpuXxXez7FnPa6huileJQb5QAFtydOMG3PwQeMi%2F9faApEC%2BAiE1jVvPzvRB9hT7SkC4%2FzUT8QXUaywKWGuR1lLcEJ8CoxLXm%2FLpZhJpajRSRbwixJbdp8wPRm3OupJFp1rHReo7%2B4Za5jT%2BrU%2FK2aB1hMo%2BbRbgEHi%2FEo75t660hcWLZePJNdX04ayVajKqguhe6IunGieaoKWrskjG3mcTxFtiacx8qL%2Bmuta0%2BYBpjumI244Qa56pmi5VAmA9X5mTOn05KIA6UQNvzPRWbxgEh%2BdUsS7MIGE6bwGOqUBPwd2B84%2FWwnT%2Bu9ipmKFtMcjL%2BOycD9%2FJPPJN65xljFZOAi4Yano5igETQ9N31BIYPq14xdTm2Yz1HWVvlG2W1bX0TFPByx%2FAlYs2XkRqkyucgg%2Fp%2BZUxThM9VfR9gYyAJSOFncidFIggowy39DnIjrjGVmeJkDo1f%2Bi6a78%2FQmcVGS9lEITv2uA4FMgxwtjD4Z8TWrO4tIB5vdpunzKVWaQzvs9&X-Amz-Signature=075e64b5c45a546d3509e69cb1edf43c5ee3de4370d0f4652d95ae26a61c4a16&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
