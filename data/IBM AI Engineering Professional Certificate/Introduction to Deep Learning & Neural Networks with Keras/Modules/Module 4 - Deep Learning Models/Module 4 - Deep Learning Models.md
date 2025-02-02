

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GEWR2CV%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041619Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCRD0mA0%2F2rxCcHBHaGygOQQR%2FsWEU9ctqQFsMyVCtrFwIgeaB5QEA6B0%2FWWYnlgSSup1JTlZj0YySKuaD5RTzlM3UqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMjMFgGFagCNcG96MSrcA09CALeOoTlnA3yU%2BNfNmGKXJLUN61Xcq%2F1ueWSaYQ3dO6kQ4WX1mUHytd3r%2FU3W61gZKDH%2Ba6HUZJjAkxWaDpmw4A3GOoiZ80snmw4pflLiz439XsNlJ%2BCyx0WHY%2FsqfPnvwqtTkIRKNlogv%2Bej6xa10DBgymSHrr30qoZB6Z6V5bG5ELxgRekIOelnbUJFe%2F3OsPxuqOU3GEm4x4FeOM3Fr5mm4XIpfuFFBKUXl330akk6JHsH%2Bff4Q08ejH4zb1r%2F2WlF%2F%2FhbXlULxBlv%2FFBM8M9yLpmzcHsLZzaZyLYA163%2FYo8NI7vEeTYiPzqP2iKFwIUlEgZhul9aZSamLqdAImr6y2gUiWreMNVmcLRhYeZlvyLvUO9HAYavjGSpvk4BCfGdkShBo5cHsx854WVphwKECEP771sWr4qOTYp%2BxSQFGxXe5uI71U5fxRqFzVCCmHsnnrC3TZEnbYhwJ%2BZOdfLinmCtLd4PnjTIpg%2FT8X944zpCTwEhf8%2Bg5z%2BdhOKpbNOrTcU8zYT5j0N2U4l6p%2FCPeXn5ZWg24jE2yULJ65ZOjlEkAS%2FLoxh4uoDwIDG3FtFNnUKPspb8ZQi1C19fZh9iC8mMRXr8HzdoapEQYYeDyigDNGkZ9ZitMLPh%2B7wGOqUBkkznbE8FQ47Dd6uOf%2Bgyfpb1L3SrDQpqmwh2%2Bwa5JYtBTdcWwq0YdTCIBa03uXCQmV%2BS5rFoIH4X2xraVGtVaHAurnpgwk66tdl%2FmU3mSPBG%2BJH3Pxf6Q7iZg5htwNqVX%2FR9H8VvqA0ioMQN9N1bc3ZDFSMGFOyTubRSzFg2%2BwDmHMPRk9RK36fhClktFvs8FQu3iiNHQeuzXI%2FSXZwTfJJjG8WG&X-Amz-Signature=2971e24f4a9d551053aed70f41c6ac9e1df53cd5da3cf4c20d88e43ccd46ddeb&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GEWR2CV%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041619Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCRD0mA0%2F2rxCcHBHaGygOQQR%2FsWEU9ctqQFsMyVCtrFwIgeaB5QEA6B0%2FWWYnlgSSup1JTlZj0YySKuaD5RTzlM3UqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMjMFgGFagCNcG96MSrcA09CALeOoTlnA3yU%2BNfNmGKXJLUN61Xcq%2F1ueWSaYQ3dO6kQ4WX1mUHytd3r%2FU3W61gZKDH%2Ba6HUZJjAkxWaDpmw4A3GOoiZ80snmw4pflLiz439XsNlJ%2BCyx0WHY%2FsqfPnvwqtTkIRKNlogv%2Bej6xa10DBgymSHrr30qoZB6Z6V5bG5ELxgRekIOelnbUJFe%2F3OsPxuqOU3GEm4x4FeOM3Fr5mm4XIpfuFFBKUXl330akk6JHsH%2Bff4Q08ejH4zb1r%2F2WlF%2F%2FhbXlULxBlv%2FFBM8M9yLpmzcHsLZzaZyLYA163%2FYo8NI7vEeTYiPzqP2iKFwIUlEgZhul9aZSamLqdAImr6y2gUiWreMNVmcLRhYeZlvyLvUO9HAYavjGSpvk4BCfGdkShBo5cHsx854WVphwKECEP771sWr4qOTYp%2BxSQFGxXe5uI71U5fxRqFzVCCmHsnnrC3TZEnbYhwJ%2BZOdfLinmCtLd4PnjTIpg%2FT8X944zpCTwEhf8%2Bg5z%2BdhOKpbNOrTcU8zYT5j0N2U4l6p%2FCPeXn5ZWg24jE2yULJ65ZOjlEkAS%2FLoxh4uoDwIDG3FtFNnUKPspb8ZQi1C19fZh9iC8mMRXr8HzdoapEQYYeDyigDNGkZ9ZitMLPh%2B7wGOqUBkkznbE8FQ47Dd6uOf%2Bgyfpb1L3SrDQpqmwh2%2Bwa5JYtBTdcWwq0YdTCIBa03uXCQmV%2BS5rFoIH4X2xraVGtVaHAurnpgwk66tdl%2FmU3mSPBG%2BJH3Pxf6Q7iZg5htwNqVX%2FR9H8VvqA0ioMQN9N1bc3ZDFSMGFOyTubRSzFg2%2BwDmHMPRk9RK36fhClktFvs8FQu3iiNHQeuzXI%2FSXZwTfJJjG8WG&X-Amz-Signature=9e6b4eb80f7d1ba2dcfd374b9585272785369ed285748d588b208c17e1141788&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GEWR2CV%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041619Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCRD0mA0%2F2rxCcHBHaGygOQQR%2FsWEU9ctqQFsMyVCtrFwIgeaB5QEA6B0%2FWWYnlgSSup1JTlZj0YySKuaD5RTzlM3UqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMjMFgGFagCNcG96MSrcA09CALeOoTlnA3yU%2BNfNmGKXJLUN61Xcq%2F1ueWSaYQ3dO6kQ4WX1mUHytd3r%2FU3W61gZKDH%2Ba6HUZJjAkxWaDpmw4A3GOoiZ80snmw4pflLiz439XsNlJ%2BCyx0WHY%2FsqfPnvwqtTkIRKNlogv%2Bej6xa10DBgymSHrr30qoZB6Z6V5bG5ELxgRekIOelnbUJFe%2F3OsPxuqOU3GEm4x4FeOM3Fr5mm4XIpfuFFBKUXl330akk6JHsH%2Bff4Q08ejH4zb1r%2F2WlF%2F%2FhbXlULxBlv%2FFBM8M9yLpmzcHsLZzaZyLYA163%2FYo8NI7vEeTYiPzqP2iKFwIUlEgZhul9aZSamLqdAImr6y2gUiWreMNVmcLRhYeZlvyLvUO9HAYavjGSpvk4BCfGdkShBo5cHsx854WVphwKECEP771sWr4qOTYp%2BxSQFGxXe5uI71U5fxRqFzVCCmHsnnrC3TZEnbYhwJ%2BZOdfLinmCtLd4PnjTIpg%2FT8X944zpCTwEhf8%2Bg5z%2BdhOKpbNOrTcU8zYT5j0N2U4l6p%2FCPeXn5ZWg24jE2yULJ65ZOjlEkAS%2FLoxh4uoDwIDG3FtFNnUKPspb8ZQi1C19fZh9iC8mMRXr8HzdoapEQYYeDyigDNGkZ9ZitMLPh%2B7wGOqUBkkznbE8FQ47Dd6uOf%2Bgyfpb1L3SrDQpqmwh2%2Bwa5JYtBTdcWwq0YdTCIBa03uXCQmV%2BS5rFoIH4X2xraVGtVaHAurnpgwk66tdl%2FmU3mSPBG%2BJH3Pxf6Q7iZg5htwNqVX%2FR9H8VvqA0ioMQN9N1bc3ZDFSMGFOyTubRSzFg2%2BwDmHMPRk9RK36fhClktFvs8FQu3iiNHQeuzXI%2FSXZwTfJJjG8WG&X-Amz-Signature=7cdccfcf94570f0656dab0576bf8eac80d9ebccecadeef660bc2edbaf1f3f07f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GEWR2CV%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041619Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCRD0mA0%2F2rxCcHBHaGygOQQR%2FsWEU9ctqQFsMyVCtrFwIgeaB5QEA6B0%2FWWYnlgSSup1JTlZj0YySKuaD5RTzlM3UqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMjMFgGFagCNcG96MSrcA09CALeOoTlnA3yU%2BNfNmGKXJLUN61Xcq%2F1ueWSaYQ3dO6kQ4WX1mUHytd3r%2FU3W61gZKDH%2Ba6HUZJjAkxWaDpmw4A3GOoiZ80snmw4pflLiz439XsNlJ%2BCyx0WHY%2FsqfPnvwqtTkIRKNlogv%2Bej6xa10DBgymSHrr30qoZB6Z6V5bG5ELxgRekIOelnbUJFe%2F3OsPxuqOU3GEm4x4FeOM3Fr5mm4XIpfuFFBKUXl330akk6JHsH%2Bff4Q08ejH4zb1r%2F2WlF%2F%2FhbXlULxBlv%2FFBM8M9yLpmzcHsLZzaZyLYA163%2FYo8NI7vEeTYiPzqP2iKFwIUlEgZhul9aZSamLqdAImr6y2gUiWreMNVmcLRhYeZlvyLvUO9HAYavjGSpvk4BCfGdkShBo5cHsx854WVphwKECEP771sWr4qOTYp%2BxSQFGxXe5uI71U5fxRqFzVCCmHsnnrC3TZEnbYhwJ%2BZOdfLinmCtLd4PnjTIpg%2FT8X944zpCTwEhf8%2Bg5z%2BdhOKpbNOrTcU8zYT5j0N2U4l6p%2FCPeXn5ZWg24jE2yULJ65ZOjlEkAS%2FLoxh4uoDwIDG3FtFNnUKPspb8ZQi1C19fZh9iC8mMRXr8HzdoapEQYYeDyigDNGkZ9ZitMLPh%2B7wGOqUBkkznbE8FQ47Dd6uOf%2Bgyfpb1L3SrDQpqmwh2%2Bwa5JYtBTdcWwq0YdTCIBa03uXCQmV%2BS5rFoIH4X2xraVGtVaHAurnpgwk66tdl%2FmU3mSPBG%2BJH3Pxf6Q7iZg5htwNqVX%2FR9H8VvqA0ioMQN9N1bc3ZDFSMGFOyTubRSzFg2%2BwDmHMPRk9RK36fhClktFvs8FQu3iiNHQeuzXI%2FSXZwTfJJjG8WG&X-Amz-Signature=9bdd3c758e1a3efcfd501b16962ad8be370d25a3b97a650111195901f08db022&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GEWR2CV%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041619Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCRD0mA0%2F2rxCcHBHaGygOQQR%2FsWEU9ctqQFsMyVCtrFwIgeaB5QEA6B0%2FWWYnlgSSup1JTlZj0YySKuaD5RTzlM3UqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMjMFgGFagCNcG96MSrcA09CALeOoTlnA3yU%2BNfNmGKXJLUN61Xcq%2F1ueWSaYQ3dO6kQ4WX1mUHytd3r%2FU3W61gZKDH%2Ba6HUZJjAkxWaDpmw4A3GOoiZ80snmw4pflLiz439XsNlJ%2BCyx0WHY%2FsqfPnvwqtTkIRKNlogv%2Bej6xa10DBgymSHrr30qoZB6Z6V5bG5ELxgRekIOelnbUJFe%2F3OsPxuqOU3GEm4x4FeOM3Fr5mm4XIpfuFFBKUXl330akk6JHsH%2Bff4Q08ejH4zb1r%2F2WlF%2F%2FhbXlULxBlv%2FFBM8M9yLpmzcHsLZzaZyLYA163%2FYo8NI7vEeTYiPzqP2iKFwIUlEgZhul9aZSamLqdAImr6y2gUiWreMNVmcLRhYeZlvyLvUO9HAYavjGSpvk4BCfGdkShBo5cHsx854WVphwKECEP771sWr4qOTYp%2BxSQFGxXe5uI71U5fxRqFzVCCmHsnnrC3TZEnbYhwJ%2BZOdfLinmCtLd4PnjTIpg%2FT8X944zpCTwEhf8%2Bg5z%2BdhOKpbNOrTcU8zYT5j0N2U4l6p%2FCPeXn5ZWg24jE2yULJ65ZOjlEkAS%2FLoxh4uoDwIDG3FtFNnUKPspb8ZQi1C19fZh9iC8mMRXr8HzdoapEQYYeDyigDNGkZ9ZitMLPh%2B7wGOqUBkkznbE8FQ47Dd6uOf%2Bgyfpb1L3SrDQpqmwh2%2Bwa5JYtBTdcWwq0YdTCIBa03uXCQmV%2BS5rFoIH4X2xraVGtVaHAurnpgwk66tdl%2FmU3mSPBG%2BJH3Pxf6Q7iZg5htwNqVX%2FR9H8VvqA0ioMQN9N1bc3ZDFSMGFOyTubRSzFg2%2BwDmHMPRk9RK36fhClktFvs8FQu3iiNHQeuzXI%2FSXZwTfJJjG8WG&X-Amz-Signature=ef6fac1c39489b7c3c46e3d77c6bcb1903ddeae43a9237581c4b477f7d76f5a0&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GEWR2CV%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041619Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCRD0mA0%2F2rxCcHBHaGygOQQR%2FsWEU9ctqQFsMyVCtrFwIgeaB5QEA6B0%2FWWYnlgSSup1JTlZj0YySKuaD5RTzlM3UqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMjMFgGFagCNcG96MSrcA09CALeOoTlnA3yU%2BNfNmGKXJLUN61Xcq%2F1ueWSaYQ3dO6kQ4WX1mUHytd3r%2FU3W61gZKDH%2Ba6HUZJjAkxWaDpmw4A3GOoiZ80snmw4pflLiz439XsNlJ%2BCyx0WHY%2FsqfPnvwqtTkIRKNlogv%2Bej6xa10DBgymSHrr30qoZB6Z6V5bG5ELxgRekIOelnbUJFe%2F3OsPxuqOU3GEm4x4FeOM3Fr5mm4XIpfuFFBKUXl330akk6JHsH%2Bff4Q08ejH4zb1r%2F2WlF%2F%2FhbXlULxBlv%2FFBM8M9yLpmzcHsLZzaZyLYA163%2FYo8NI7vEeTYiPzqP2iKFwIUlEgZhul9aZSamLqdAImr6y2gUiWreMNVmcLRhYeZlvyLvUO9HAYavjGSpvk4BCfGdkShBo5cHsx854WVphwKECEP771sWr4qOTYp%2BxSQFGxXe5uI71U5fxRqFzVCCmHsnnrC3TZEnbYhwJ%2BZOdfLinmCtLd4PnjTIpg%2FT8X944zpCTwEhf8%2Bg5z%2BdhOKpbNOrTcU8zYT5j0N2U4l6p%2FCPeXn5ZWg24jE2yULJ65ZOjlEkAS%2FLoxh4uoDwIDG3FtFNnUKPspb8ZQi1C19fZh9iC8mMRXr8HzdoapEQYYeDyigDNGkZ9ZitMLPh%2B7wGOqUBkkznbE8FQ47Dd6uOf%2Bgyfpb1L3SrDQpqmwh2%2Bwa5JYtBTdcWwq0YdTCIBa03uXCQmV%2BS5rFoIH4X2xraVGtVaHAurnpgwk66tdl%2FmU3mSPBG%2BJH3Pxf6Q7iZg5htwNqVX%2FR9H8VvqA0ioMQN9N1bc3ZDFSMGFOyTubRSzFg2%2BwDmHMPRk9RK36fhClktFvs8FQu3iiNHQeuzXI%2FSXZwTfJJjG8WG&X-Amz-Signature=222e1c1a0cffc6fff8e2c79ff2dada308dbf197b57ce4db66533be43713df58b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GEWR2CV%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041619Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCRD0mA0%2F2rxCcHBHaGygOQQR%2FsWEU9ctqQFsMyVCtrFwIgeaB5QEA6B0%2FWWYnlgSSup1JTlZj0YySKuaD5RTzlM3UqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMjMFgGFagCNcG96MSrcA09CALeOoTlnA3yU%2BNfNmGKXJLUN61Xcq%2F1ueWSaYQ3dO6kQ4WX1mUHytd3r%2FU3W61gZKDH%2Ba6HUZJjAkxWaDpmw4A3GOoiZ80snmw4pflLiz439XsNlJ%2BCyx0WHY%2FsqfPnvwqtTkIRKNlogv%2Bej6xa10DBgymSHrr30qoZB6Z6V5bG5ELxgRekIOelnbUJFe%2F3OsPxuqOU3GEm4x4FeOM3Fr5mm4XIpfuFFBKUXl330akk6JHsH%2Bff4Q08ejH4zb1r%2F2WlF%2F%2FhbXlULxBlv%2FFBM8M9yLpmzcHsLZzaZyLYA163%2FYo8NI7vEeTYiPzqP2iKFwIUlEgZhul9aZSamLqdAImr6y2gUiWreMNVmcLRhYeZlvyLvUO9HAYavjGSpvk4BCfGdkShBo5cHsx854WVphwKECEP771sWr4qOTYp%2BxSQFGxXe5uI71U5fxRqFzVCCmHsnnrC3TZEnbYhwJ%2BZOdfLinmCtLd4PnjTIpg%2FT8X944zpCTwEhf8%2Bg5z%2BdhOKpbNOrTcU8zYT5j0N2U4l6p%2FCPeXn5ZWg24jE2yULJ65ZOjlEkAS%2FLoxh4uoDwIDG3FtFNnUKPspb8ZQi1C19fZh9iC8mMRXr8HzdoapEQYYeDyigDNGkZ9ZitMLPh%2B7wGOqUBkkznbE8FQ47Dd6uOf%2Bgyfpb1L3SrDQpqmwh2%2Bwa5JYtBTdcWwq0YdTCIBa03uXCQmV%2BS5rFoIH4X2xraVGtVaHAurnpgwk66tdl%2FmU3mSPBG%2BJH3Pxf6Q7iZg5htwNqVX%2FR9H8VvqA0ioMQN9N1bc3ZDFSMGFOyTubRSzFg2%2BwDmHMPRk9RK36fhClktFvs8FQu3iiNHQeuzXI%2FSXZwTfJJjG8WG&X-Amz-Signature=96c794861322cbdc680d978215634b3ea9fe8929d680164ed4832735ea116cee&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GEWR2CV%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041619Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCRD0mA0%2F2rxCcHBHaGygOQQR%2FsWEU9ctqQFsMyVCtrFwIgeaB5QEA6B0%2FWWYnlgSSup1JTlZj0YySKuaD5RTzlM3UqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMjMFgGFagCNcG96MSrcA09CALeOoTlnA3yU%2BNfNmGKXJLUN61Xcq%2F1ueWSaYQ3dO6kQ4WX1mUHytd3r%2FU3W61gZKDH%2Ba6HUZJjAkxWaDpmw4A3GOoiZ80snmw4pflLiz439XsNlJ%2BCyx0WHY%2FsqfPnvwqtTkIRKNlogv%2Bej6xa10DBgymSHrr30qoZB6Z6V5bG5ELxgRekIOelnbUJFe%2F3OsPxuqOU3GEm4x4FeOM3Fr5mm4XIpfuFFBKUXl330akk6JHsH%2Bff4Q08ejH4zb1r%2F2WlF%2F%2FhbXlULxBlv%2FFBM8M9yLpmzcHsLZzaZyLYA163%2FYo8NI7vEeTYiPzqP2iKFwIUlEgZhul9aZSamLqdAImr6y2gUiWreMNVmcLRhYeZlvyLvUO9HAYavjGSpvk4BCfGdkShBo5cHsx854WVphwKECEP771sWr4qOTYp%2BxSQFGxXe5uI71U5fxRqFzVCCmHsnnrC3TZEnbYhwJ%2BZOdfLinmCtLd4PnjTIpg%2FT8X944zpCTwEhf8%2Bg5z%2BdhOKpbNOrTcU8zYT5j0N2U4l6p%2FCPeXn5ZWg24jE2yULJ65ZOjlEkAS%2FLoxh4uoDwIDG3FtFNnUKPspb8ZQi1C19fZh9iC8mMRXr8HzdoapEQYYeDyigDNGkZ9ZitMLPh%2B7wGOqUBkkznbE8FQ47Dd6uOf%2Bgyfpb1L3SrDQpqmwh2%2Bwa5JYtBTdcWwq0YdTCIBa03uXCQmV%2BS5rFoIH4X2xraVGtVaHAurnpgwk66tdl%2FmU3mSPBG%2BJH3Pxf6Q7iZg5htwNqVX%2FR9H8VvqA0ioMQN9N1bc3ZDFSMGFOyTubRSzFg2%2BwDmHMPRk9RK36fhClktFvs8FQu3iiNHQeuzXI%2FSXZwTfJJjG8WG&X-Amz-Signature=672305d69d8ab8ed64a174713c085fff65d3f08cd7385c69e900c6bbadb3840c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GEWR2CV%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041619Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCRD0mA0%2F2rxCcHBHaGygOQQR%2FsWEU9ctqQFsMyVCtrFwIgeaB5QEA6B0%2FWWYnlgSSup1JTlZj0YySKuaD5RTzlM3UqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMjMFgGFagCNcG96MSrcA09CALeOoTlnA3yU%2BNfNmGKXJLUN61Xcq%2F1ueWSaYQ3dO6kQ4WX1mUHytd3r%2FU3W61gZKDH%2Ba6HUZJjAkxWaDpmw4A3GOoiZ80snmw4pflLiz439XsNlJ%2BCyx0WHY%2FsqfPnvwqtTkIRKNlogv%2Bej6xa10DBgymSHrr30qoZB6Z6V5bG5ELxgRekIOelnbUJFe%2F3OsPxuqOU3GEm4x4FeOM3Fr5mm4XIpfuFFBKUXl330akk6JHsH%2Bff4Q08ejH4zb1r%2F2WlF%2F%2FhbXlULxBlv%2FFBM8M9yLpmzcHsLZzaZyLYA163%2FYo8NI7vEeTYiPzqP2iKFwIUlEgZhul9aZSamLqdAImr6y2gUiWreMNVmcLRhYeZlvyLvUO9HAYavjGSpvk4BCfGdkShBo5cHsx854WVphwKECEP771sWr4qOTYp%2BxSQFGxXe5uI71U5fxRqFzVCCmHsnnrC3TZEnbYhwJ%2BZOdfLinmCtLd4PnjTIpg%2FT8X944zpCTwEhf8%2Bg5z%2BdhOKpbNOrTcU8zYT5j0N2U4l6p%2FCPeXn5ZWg24jE2yULJ65ZOjlEkAS%2FLoxh4uoDwIDG3FtFNnUKPspb8ZQi1C19fZh9iC8mMRXr8HzdoapEQYYeDyigDNGkZ9ZitMLPh%2B7wGOqUBkkznbE8FQ47Dd6uOf%2Bgyfpb1L3SrDQpqmwh2%2Bwa5JYtBTdcWwq0YdTCIBa03uXCQmV%2BS5rFoIH4X2xraVGtVaHAurnpgwk66tdl%2FmU3mSPBG%2BJH3Pxf6Q7iZg5htwNqVX%2FR9H8VvqA0ioMQN9N1bc3ZDFSMGFOyTubRSzFg2%2BwDmHMPRk9RK36fhClktFvs8FQu3iiNHQeuzXI%2FSXZwTfJJjG8WG&X-Amz-Signature=ea3d39dfa2f805ea9939dffda3769b01cc72e3ac84d12bee9f02747f4f90c166&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROPANAGB%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041620Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDtMrtTPe6IgVHzKoWlC5C9TQTNImgYrHBzhGCIGhLVTgIgA1Im2F0Dm9XrPb9mMxU%2F54mB1HxhsKowRIouDcR3lKsqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB%2BtywLtnsrabFYvNSrcA2aZ8tagHd4O1ncSUTxthziSPenicFw0o0qqYbBxsa%2FggvcQ%2FNe%2BJ9Jm17CNOsOAbK6thK9grt62HE4NBMVoWXF0DcECUnOwLl8GnGm1JimnjATsv0kqFjOyfZj3EoWpwJemUN2%2Bsvz7gTclQGt%2FrBg1TGw2E03j%2BkHackUlpoLnx1e4tEHYOKvrKn%2BpcIgEn05byqzV%2FeuniG2KgA0B3K3tsF6cJv8JaPCqo4LUWg1ra1OjWWlGDpj3NzznfykpWd4apSGG8ilNGQv7vWR043GY%2BWoH2RgRENWW0pZKqlSIrH%2FeSXwxgHWIJdEHXzceJs221MwyCVNthYLW30wt1DDcw6K%2BDiZbHC%2F9RtAVqb%2FyxITaEKaPE7VLKyW4V%2B14s5halVdCSZExT045jrRhDWVENlyHbeiLtwmZYdmAk9CTnxxwKpga6S0gXegnvNVAWCFuwLrQ8fxfk6HPDXdH%2FSJ%2FnxB06qvAtYHZ5BQhJ1fMv%2Fo%2FYTyRaJQ9IRrULNqI5rz4g8xvrxHeOisjrOPaxwQJsd7PU%2Bqfr9ezisL5u3s91Rz90X5hgRmUjui1TF0p05gH9vJLm5xPyGp5%2Bmxtz29pPG7WSijfean68kRsqzTID2ywBC4snM6vuoYYMIHh%2B7wGOqUBVQ9wJFzBTDtyVJfu%2B%2B0g0ZIzMre7qMPbNz5OADXTV7W1lkEU%2B%2FS2QJCvcv4kAhEX6%2FJGRqf1nK9Cnzj0hPUlmFpZBUJTNdWHsrIlRnVh8YCTR6d5e7dn09RNzudbt2iRnMNoseQGC8BZZAFhuWH9qilAgh%2FYD4mzhq9JZ7R2wk6JiQ%2FBQgbZbeaKOVyCCALrUjZhCxwvWloXrFWwpWxvHj3nkARE&X-Amz-Signature=5ab1ed66da5ad47687a00c1df1e361cb615cce7490757c448565366eda1f1c22&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROPANAGB%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041620Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDtMrtTPe6IgVHzKoWlC5C9TQTNImgYrHBzhGCIGhLVTgIgA1Im2F0Dm9XrPb9mMxU%2F54mB1HxhsKowRIouDcR3lKsqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB%2BtywLtnsrabFYvNSrcA2aZ8tagHd4O1ncSUTxthziSPenicFw0o0qqYbBxsa%2FggvcQ%2FNe%2BJ9Jm17CNOsOAbK6thK9grt62HE4NBMVoWXF0DcECUnOwLl8GnGm1JimnjATsv0kqFjOyfZj3EoWpwJemUN2%2Bsvz7gTclQGt%2FrBg1TGw2E03j%2BkHackUlpoLnx1e4tEHYOKvrKn%2BpcIgEn05byqzV%2FeuniG2KgA0B3K3tsF6cJv8JaPCqo4LUWg1ra1OjWWlGDpj3NzznfykpWd4apSGG8ilNGQv7vWR043GY%2BWoH2RgRENWW0pZKqlSIrH%2FeSXwxgHWIJdEHXzceJs221MwyCVNthYLW30wt1DDcw6K%2BDiZbHC%2F9RtAVqb%2FyxITaEKaPE7VLKyW4V%2B14s5halVdCSZExT045jrRhDWVENlyHbeiLtwmZYdmAk9CTnxxwKpga6S0gXegnvNVAWCFuwLrQ8fxfk6HPDXdH%2FSJ%2FnxB06qvAtYHZ5BQhJ1fMv%2Fo%2FYTyRaJQ9IRrULNqI5rz4g8xvrxHeOisjrOPaxwQJsd7PU%2Bqfr9ezisL5u3s91Rz90X5hgRmUjui1TF0p05gH9vJLm5xPyGp5%2Bmxtz29pPG7WSijfean68kRsqzTID2ywBC4snM6vuoYYMIHh%2B7wGOqUBVQ9wJFzBTDtyVJfu%2B%2B0g0ZIzMre7qMPbNz5OADXTV7W1lkEU%2B%2FS2QJCvcv4kAhEX6%2FJGRqf1nK9Cnzj0hPUlmFpZBUJTNdWHsrIlRnVh8YCTR6d5e7dn09RNzudbt2iRnMNoseQGC8BZZAFhuWH9qilAgh%2FYD4mzhq9JZ7R2wk6JiQ%2FBQgbZbeaKOVyCCALrUjZhCxwvWloXrFWwpWxvHj3nkARE&X-Amz-Signature=c33f8c44c494aa845ed34977b4559eaf48033ccd82a922b6b3ee1a074e0410ea&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
