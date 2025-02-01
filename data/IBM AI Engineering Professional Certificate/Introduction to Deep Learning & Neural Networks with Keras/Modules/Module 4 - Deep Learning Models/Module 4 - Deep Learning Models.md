

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XIBZANLD%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBGTpTTDKVswpsDiqrQH231mpEsctUkhnNLPNbDbRNoCAiEAvbjqv3ucfE6YnSl9NUWppd756gz%2FdgzZGr6yiV6sSroqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFHCsiP4mx5YIWLLSSrcA5l7IDdF2iUFcSWhOcppVUbSUhz%2BVUjW%2B7f1uIVj%2F6rSDxgM%2BFbJ%2FUiBkJofcVKTcCI8OO8utsX%2BPL43BpR4dFnn6WMOIHFZJu6R7pL04Beq0kTAuiQyCuEuRYMVudmcAM9qimiohzVK1DlV43QbO6hQNKLB7YaSXTvEAQX%2BvU2CvwCMUDf%2Fjq60el2uClAgcBLAsoyrtDjrw7hT5spezbCX2knNN08H0re6qA0%2FOMXVE3WXu75hpOaPDvUDtToeU2ELXqf00ng5JDrxRjuHQ8bqLOHozDiClmuv5ak63YluTa%2FDmvq9p6J%2FfBmghbQR8kzIgr5i9SRlLl%2B0uChi1xoAi%2B0ZOaw8ZEhzI6jI0cTqIDzzXv3R0yL47ZiY9hdiJS5FvTOts9qLuEOs0PMklJh1dd4%2BA8AJMLItlGFMVvTmcKtYgtb4lzZrwxYUrYnW0pYjt3nad1DrdQrGL5%2FbgYE9uW8%2FSJNAuLBNnfPpP9ICEl%2BOekWjwIBn1ctq4MbdE9zZNaVnjxYnnUPf2zq99KP1D%2FKy0iFSdro9k2LQxXfmMJaPxO%2BZWcNRZGqKtMwC3ub1ZFFQ8cDDWcNHdU7gRJqoUIdl6DgyFf9mFetOEn36GwUpp4461olzRiwBMOj2%2BbwGOqUBliLZbGIV6x8eQxjjHXTqIDiGYJ8xdA6o9jI9AYToeVVLEH7BN%2BCdlHEYuBZ%2BIw9msmF5APzGFxzPnQtpV1x5KZ0gd56kTvTKwWjpBIgtLj5y4cv1q3p2CCG%2B6IctfDWkDj5z88SwLYGs4oXEaW8Hyy7BLuTrF8Ji7jpH8Y1MJjD9azdhYWGcwfnjYSgfrI%2BLhaKazdbrLvfSBjGuUfzcQd5pa9Fr&X-Amz-Signature=36fb665d8ec51615de9ce706222a3cb72ac3d3ffbb15ebc5ad8f85bb14554815&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XIBZANLD%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBGTpTTDKVswpsDiqrQH231mpEsctUkhnNLPNbDbRNoCAiEAvbjqv3ucfE6YnSl9NUWppd756gz%2FdgzZGr6yiV6sSroqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFHCsiP4mx5YIWLLSSrcA5l7IDdF2iUFcSWhOcppVUbSUhz%2BVUjW%2B7f1uIVj%2F6rSDxgM%2BFbJ%2FUiBkJofcVKTcCI8OO8utsX%2BPL43BpR4dFnn6WMOIHFZJu6R7pL04Beq0kTAuiQyCuEuRYMVudmcAM9qimiohzVK1DlV43QbO6hQNKLB7YaSXTvEAQX%2BvU2CvwCMUDf%2Fjq60el2uClAgcBLAsoyrtDjrw7hT5spezbCX2knNN08H0re6qA0%2FOMXVE3WXu75hpOaPDvUDtToeU2ELXqf00ng5JDrxRjuHQ8bqLOHozDiClmuv5ak63YluTa%2FDmvq9p6J%2FfBmghbQR8kzIgr5i9SRlLl%2B0uChi1xoAi%2B0ZOaw8ZEhzI6jI0cTqIDzzXv3R0yL47ZiY9hdiJS5FvTOts9qLuEOs0PMklJh1dd4%2BA8AJMLItlGFMVvTmcKtYgtb4lzZrwxYUrYnW0pYjt3nad1DrdQrGL5%2FbgYE9uW8%2FSJNAuLBNnfPpP9ICEl%2BOekWjwIBn1ctq4MbdE9zZNaVnjxYnnUPf2zq99KP1D%2FKy0iFSdro9k2LQxXfmMJaPxO%2BZWcNRZGqKtMwC3ub1ZFFQ8cDDWcNHdU7gRJqoUIdl6DgyFf9mFetOEn36GwUpp4461olzRiwBMOj2%2BbwGOqUBliLZbGIV6x8eQxjjHXTqIDiGYJ8xdA6o9jI9AYToeVVLEH7BN%2BCdlHEYuBZ%2BIw9msmF5APzGFxzPnQtpV1x5KZ0gd56kTvTKwWjpBIgtLj5y4cv1q3p2CCG%2B6IctfDWkDj5z88SwLYGs4oXEaW8Hyy7BLuTrF8Ji7jpH8Y1MJjD9azdhYWGcwfnjYSgfrI%2BLhaKazdbrLvfSBjGuUfzcQd5pa9Fr&X-Amz-Signature=51d572dd3f44455e5a3169a940179ccf88fe82af201943b3082a92aa24f638a1&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XIBZANLD%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBGTpTTDKVswpsDiqrQH231mpEsctUkhnNLPNbDbRNoCAiEAvbjqv3ucfE6YnSl9NUWppd756gz%2FdgzZGr6yiV6sSroqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFHCsiP4mx5YIWLLSSrcA5l7IDdF2iUFcSWhOcppVUbSUhz%2BVUjW%2B7f1uIVj%2F6rSDxgM%2BFbJ%2FUiBkJofcVKTcCI8OO8utsX%2BPL43BpR4dFnn6WMOIHFZJu6R7pL04Beq0kTAuiQyCuEuRYMVudmcAM9qimiohzVK1DlV43QbO6hQNKLB7YaSXTvEAQX%2BvU2CvwCMUDf%2Fjq60el2uClAgcBLAsoyrtDjrw7hT5spezbCX2knNN08H0re6qA0%2FOMXVE3WXu75hpOaPDvUDtToeU2ELXqf00ng5JDrxRjuHQ8bqLOHozDiClmuv5ak63YluTa%2FDmvq9p6J%2FfBmghbQR8kzIgr5i9SRlLl%2B0uChi1xoAi%2B0ZOaw8ZEhzI6jI0cTqIDzzXv3R0yL47ZiY9hdiJS5FvTOts9qLuEOs0PMklJh1dd4%2BA8AJMLItlGFMVvTmcKtYgtb4lzZrwxYUrYnW0pYjt3nad1DrdQrGL5%2FbgYE9uW8%2FSJNAuLBNnfPpP9ICEl%2BOekWjwIBn1ctq4MbdE9zZNaVnjxYnnUPf2zq99KP1D%2FKy0iFSdro9k2LQxXfmMJaPxO%2BZWcNRZGqKtMwC3ub1ZFFQ8cDDWcNHdU7gRJqoUIdl6DgyFf9mFetOEn36GwUpp4461olzRiwBMOj2%2BbwGOqUBliLZbGIV6x8eQxjjHXTqIDiGYJ8xdA6o9jI9AYToeVVLEH7BN%2BCdlHEYuBZ%2BIw9msmF5APzGFxzPnQtpV1x5KZ0gd56kTvTKwWjpBIgtLj5y4cv1q3p2CCG%2B6IctfDWkDj5z88SwLYGs4oXEaW8Hyy7BLuTrF8Ji7jpH8Y1MJjD9azdhYWGcwfnjYSgfrI%2BLhaKazdbrLvfSBjGuUfzcQd5pa9Fr&X-Amz-Signature=13acf43a5526baabf7a7a7b2482ca1fcd3db4e24184a16b037cdf3171ff10dd1&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XIBZANLD%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBGTpTTDKVswpsDiqrQH231mpEsctUkhnNLPNbDbRNoCAiEAvbjqv3ucfE6YnSl9NUWppd756gz%2FdgzZGr6yiV6sSroqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFHCsiP4mx5YIWLLSSrcA5l7IDdF2iUFcSWhOcppVUbSUhz%2BVUjW%2B7f1uIVj%2F6rSDxgM%2BFbJ%2FUiBkJofcVKTcCI8OO8utsX%2BPL43BpR4dFnn6WMOIHFZJu6R7pL04Beq0kTAuiQyCuEuRYMVudmcAM9qimiohzVK1DlV43QbO6hQNKLB7YaSXTvEAQX%2BvU2CvwCMUDf%2Fjq60el2uClAgcBLAsoyrtDjrw7hT5spezbCX2knNN08H0re6qA0%2FOMXVE3WXu75hpOaPDvUDtToeU2ELXqf00ng5JDrxRjuHQ8bqLOHozDiClmuv5ak63YluTa%2FDmvq9p6J%2FfBmghbQR8kzIgr5i9SRlLl%2B0uChi1xoAi%2B0ZOaw8ZEhzI6jI0cTqIDzzXv3R0yL47ZiY9hdiJS5FvTOts9qLuEOs0PMklJh1dd4%2BA8AJMLItlGFMVvTmcKtYgtb4lzZrwxYUrYnW0pYjt3nad1DrdQrGL5%2FbgYE9uW8%2FSJNAuLBNnfPpP9ICEl%2BOekWjwIBn1ctq4MbdE9zZNaVnjxYnnUPf2zq99KP1D%2FKy0iFSdro9k2LQxXfmMJaPxO%2BZWcNRZGqKtMwC3ub1ZFFQ8cDDWcNHdU7gRJqoUIdl6DgyFf9mFetOEn36GwUpp4461olzRiwBMOj2%2BbwGOqUBliLZbGIV6x8eQxjjHXTqIDiGYJ8xdA6o9jI9AYToeVVLEH7BN%2BCdlHEYuBZ%2BIw9msmF5APzGFxzPnQtpV1x5KZ0gd56kTvTKwWjpBIgtLj5y4cv1q3p2CCG%2B6IctfDWkDj5z88SwLYGs4oXEaW8Hyy7BLuTrF8Ji7jpH8Y1MJjD9azdhYWGcwfnjYSgfrI%2BLhaKazdbrLvfSBjGuUfzcQd5pa9Fr&X-Amz-Signature=39c160cdff816d91c0f0fd62aa6eb78255b65557853df082055ef950a268bd1d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XIBZANLD%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBGTpTTDKVswpsDiqrQH231mpEsctUkhnNLPNbDbRNoCAiEAvbjqv3ucfE6YnSl9NUWppd756gz%2FdgzZGr6yiV6sSroqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFHCsiP4mx5YIWLLSSrcA5l7IDdF2iUFcSWhOcppVUbSUhz%2BVUjW%2B7f1uIVj%2F6rSDxgM%2BFbJ%2FUiBkJofcVKTcCI8OO8utsX%2BPL43BpR4dFnn6WMOIHFZJu6R7pL04Beq0kTAuiQyCuEuRYMVudmcAM9qimiohzVK1DlV43QbO6hQNKLB7YaSXTvEAQX%2BvU2CvwCMUDf%2Fjq60el2uClAgcBLAsoyrtDjrw7hT5spezbCX2knNN08H0re6qA0%2FOMXVE3WXu75hpOaPDvUDtToeU2ELXqf00ng5JDrxRjuHQ8bqLOHozDiClmuv5ak63YluTa%2FDmvq9p6J%2FfBmghbQR8kzIgr5i9SRlLl%2B0uChi1xoAi%2B0ZOaw8ZEhzI6jI0cTqIDzzXv3R0yL47ZiY9hdiJS5FvTOts9qLuEOs0PMklJh1dd4%2BA8AJMLItlGFMVvTmcKtYgtb4lzZrwxYUrYnW0pYjt3nad1DrdQrGL5%2FbgYE9uW8%2FSJNAuLBNnfPpP9ICEl%2BOekWjwIBn1ctq4MbdE9zZNaVnjxYnnUPf2zq99KP1D%2FKy0iFSdro9k2LQxXfmMJaPxO%2BZWcNRZGqKtMwC3ub1ZFFQ8cDDWcNHdU7gRJqoUIdl6DgyFf9mFetOEn36GwUpp4461olzRiwBMOj2%2BbwGOqUBliLZbGIV6x8eQxjjHXTqIDiGYJ8xdA6o9jI9AYToeVVLEH7BN%2BCdlHEYuBZ%2BIw9msmF5APzGFxzPnQtpV1x5KZ0gd56kTvTKwWjpBIgtLj5y4cv1q3p2CCG%2B6IctfDWkDj5z88SwLYGs4oXEaW8Hyy7BLuTrF8Ji7jpH8Y1MJjD9azdhYWGcwfnjYSgfrI%2BLhaKazdbrLvfSBjGuUfzcQd5pa9Fr&X-Amz-Signature=926020d3996e361b4de02c2455208f3788954089681ea98fbaefee8c40640d99&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XIBZANLD%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBGTpTTDKVswpsDiqrQH231mpEsctUkhnNLPNbDbRNoCAiEAvbjqv3ucfE6YnSl9NUWppd756gz%2FdgzZGr6yiV6sSroqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFHCsiP4mx5YIWLLSSrcA5l7IDdF2iUFcSWhOcppVUbSUhz%2BVUjW%2B7f1uIVj%2F6rSDxgM%2BFbJ%2FUiBkJofcVKTcCI8OO8utsX%2BPL43BpR4dFnn6WMOIHFZJu6R7pL04Beq0kTAuiQyCuEuRYMVudmcAM9qimiohzVK1DlV43QbO6hQNKLB7YaSXTvEAQX%2BvU2CvwCMUDf%2Fjq60el2uClAgcBLAsoyrtDjrw7hT5spezbCX2knNN08H0re6qA0%2FOMXVE3WXu75hpOaPDvUDtToeU2ELXqf00ng5JDrxRjuHQ8bqLOHozDiClmuv5ak63YluTa%2FDmvq9p6J%2FfBmghbQR8kzIgr5i9SRlLl%2B0uChi1xoAi%2B0ZOaw8ZEhzI6jI0cTqIDzzXv3R0yL47ZiY9hdiJS5FvTOts9qLuEOs0PMklJh1dd4%2BA8AJMLItlGFMVvTmcKtYgtb4lzZrwxYUrYnW0pYjt3nad1DrdQrGL5%2FbgYE9uW8%2FSJNAuLBNnfPpP9ICEl%2BOekWjwIBn1ctq4MbdE9zZNaVnjxYnnUPf2zq99KP1D%2FKy0iFSdro9k2LQxXfmMJaPxO%2BZWcNRZGqKtMwC3ub1ZFFQ8cDDWcNHdU7gRJqoUIdl6DgyFf9mFetOEn36GwUpp4461olzRiwBMOj2%2BbwGOqUBliLZbGIV6x8eQxjjHXTqIDiGYJ8xdA6o9jI9AYToeVVLEH7BN%2BCdlHEYuBZ%2BIw9msmF5APzGFxzPnQtpV1x5KZ0gd56kTvTKwWjpBIgtLj5y4cv1q3p2CCG%2B6IctfDWkDj5z88SwLYGs4oXEaW8Hyy7BLuTrF8Ji7jpH8Y1MJjD9azdhYWGcwfnjYSgfrI%2BLhaKazdbrLvfSBjGuUfzcQd5pa9Fr&X-Amz-Signature=5eac7732fdcf22ae1c5b68cc52f4a1225253f4fc0265113a57fee0c52629da55&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XIBZANLD%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBGTpTTDKVswpsDiqrQH231mpEsctUkhnNLPNbDbRNoCAiEAvbjqv3ucfE6YnSl9NUWppd756gz%2FdgzZGr6yiV6sSroqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFHCsiP4mx5YIWLLSSrcA5l7IDdF2iUFcSWhOcppVUbSUhz%2BVUjW%2B7f1uIVj%2F6rSDxgM%2BFbJ%2FUiBkJofcVKTcCI8OO8utsX%2BPL43BpR4dFnn6WMOIHFZJu6R7pL04Beq0kTAuiQyCuEuRYMVudmcAM9qimiohzVK1DlV43QbO6hQNKLB7YaSXTvEAQX%2BvU2CvwCMUDf%2Fjq60el2uClAgcBLAsoyrtDjrw7hT5spezbCX2knNN08H0re6qA0%2FOMXVE3WXu75hpOaPDvUDtToeU2ELXqf00ng5JDrxRjuHQ8bqLOHozDiClmuv5ak63YluTa%2FDmvq9p6J%2FfBmghbQR8kzIgr5i9SRlLl%2B0uChi1xoAi%2B0ZOaw8ZEhzI6jI0cTqIDzzXv3R0yL47ZiY9hdiJS5FvTOts9qLuEOs0PMklJh1dd4%2BA8AJMLItlGFMVvTmcKtYgtb4lzZrwxYUrYnW0pYjt3nad1DrdQrGL5%2FbgYE9uW8%2FSJNAuLBNnfPpP9ICEl%2BOekWjwIBn1ctq4MbdE9zZNaVnjxYnnUPf2zq99KP1D%2FKy0iFSdro9k2LQxXfmMJaPxO%2BZWcNRZGqKtMwC3ub1ZFFQ8cDDWcNHdU7gRJqoUIdl6DgyFf9mFetOEn36GwUpp4461olzRiwBMOj2%2BbwGOqUBliLZbGIV6x8eQxjjHXTqIDiGYJ8xdA6o9jI9AYToeVVLEH7BN%2BCdlHEYuBZ%2BIw9msmF5APzGFxzPnQtpV1x5KZ0gd56kTvTKwWjpBIgtLj5y4cv1q3p2CCG%2B6IctfDWkDj5z88SwLYGs4oXEaW8Hyy7BLuTrF8Ji7jpH8Y1MJjD9azdhYWGcwfnjYSgfrI%2BLhaKazdbrLvfSBjGuUfzcQd5pa9Fr&X-Amz-Signature=18d75bede84f727c2a12bfafd156de02a9d82c453ca87f1fb41e41c9c864e6fc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XIBZANLD%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBGTpTTDKVswpsDiqrQH231mpEsctUkhnNLPNbDbRNoCAiEAvbjqv3ucfE6YnSl9NUWppd756gz%2FdgzZGr6yiV6sSroqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFHCsiP4mx5YIWLLSSrcA5l7IDdF2iUFcSWhOcppVUbSUhz%2BVUjW%2B7f1uIVj%2F6rSDxgM%2BFbJ%2FUiBkJofcVKTcCI8OO8utsX%2BPL43BpR4dFnn6WMOIHFZJu6R7pL04Beq0kTAuiQyCuEuRYMVudmcAM9qimiohzVK1DlV43QbO6hQNKLB7YaSXTvEAQX%2BvU2CvwCMUDf%2Fjq60el2uClAgcBLAsoyrtDjrw7hT5spezbCX2knNN08H0re6qA0%2FOMXVE3WXu75hpOaPDvUDtToeU2ELXqf00ng5JDrxRjuHQ8bqLOHozDiClmuv5ak63YluTa%2FDmvq9p6J%2FfBmghbQR8kzIgr5i9SRlLl%2B0uChi1xoAi%2B0ZOaw8ZEhzI6jI0cTqIDzzXv3R0yL47ZiY9hdiJS5FvTOts9qLuEOs0PMklJh1dd4%2BA8AJMLItlGFMVvTmcKtYgtb4lzZrwxYUrYnW0pYjt3nad1DrdQrGL5%2FbgYE9uW8%2FSJNAuLBNnfPpP9ICEl%2BOekWjwIBn1ctq4MbdE9zZNaVnjxYnnUPf2zq99KP1D%2FKy0iFSdro9k2LQxXfmMJaPxO%2BZWcNRZGqKtMwC3ub1ZFFQ8cDDWcNHdU7gRJqoUIdl6DgyFf9mFetOEn36GwUpp4461olzRiwBMOj2%2BbwGOqUBliLZbGIV6x8eQxjjHXTqIDiGYJ8xdA6o9jI9AYToeVVLEH7BN%2BCdlHEYuBZ%2BIw9msmF5APzGFxzPnQtpV1x5KZ0gd56kTvTKwWjpBIgtLj5y4cv1q3p2CCG%2B6IctfDWkDj5z88SwLYGs4oXEaW8Hyy7BLuTrF8Ji7jpH8Y1MJjD9azdhYWGcwfnjYSgfrI%2BLhaKazdbrLvfSBjGuUfzcQd5pa9Fr&X-Amz-Signature=2558ded43df509d4647283eeb821b3a6d438916d01bb45dd827c2bdb0cf5a793&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XIBZANLD%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBGTpTTDKVswpsDiqrQH231mpEsctUkhnNLPNbDbRNoCAiEAvbjqv3ucfE6YnSl9NUWppd756gz%2FdgzZGr6yiV6sSroqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFHCsiP4mx5YIWLLSSrcA5l7IDdF2iUFcSWhOcppVUbSUhz%2BVUjW%2B7f1uIVj%2F6rSDxgM%2BFbJ%2FUiBkJofcVKTcCI8OO8utsX%2BPL43BpR4dFnn6WMOIHFZJu6R7pL04Beq0kTAuiQyCuEuRYMVudmcAM9qimiohzVK1DlV43QbO6hQNKLB7YaSXTvEAQX%2BvU2CvwCMUDf%2Fjq60el2uClAgcBLAsoyrtDjrw7hT5spezbCX2knNN08H0re6qA0%2FOMXVE3WXu75hpOaPDvUDtToeU2ELXqf00ng5JDrxRjuHQ8bqLOHozDiClmuv5ak63YluTa%2FDmvq9p6J%2FfBmghbQR8kzIgr5i9SRlLl%2B0uChi1xoAi%2B0ZOaw8ZEhzI6jI0cTqIDzzXv3R0yL47ZiY9hdiJS5FvTOts9qLuEOs0PMklJh1dd4%2BA8AJMLItlGFMVvTmcKtYgtb4lzZrwxYUrYnW0pYjt3nad1DrdQrGL5%2FbgYE9uW8%2FSJNAuLBNnfPpP9ICEl%2BOekWjwIBn1ctq4MbdE9zZNaVnjxYnnUPf2zq99KP1D%2FKy0iFSdro9k2LQxXfmMJaPxO%2BZWcNRZGqKtMwC3ub1ZFFQ8cDDWcNHdU7gRJqoUIdl6DgyFf9mFetOEn36GwUpp4461olzRiwBMOj2%2BbwGOqUBliLZbGIV6x8eQxjjHXTqIDiGYJ8xdA6o9jI9AYToeVVLEH7BN%2BCdlHEYuBZ%2BIw9msmF5APzGFxzPnQtpV1x5KZ0gd56kTvTKwWjpBIgtLj5y4cv1q3p2CCG%2B6IctfDWkDj5z88SwLYGs4oXEaW8Hyy7BLuTrF8Ji7jpH8Y1MJjD9azdhYWGcwfnjYSgfrI%2BLhaKazdbrLvfSBjGuUfzcQd5pa9Fr&X-Amz-Signature=cc905c1d9c5b7eaa56ffac49577348739e4632e9eafcc5da08454b8b3582f698&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UEOOWWB%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG%2FcLLtWN2720cyJsH%2B%2BSYZiKM%2F3qbQCERP7PmCHi4tQAiEA6H8aEPHA%2BLhVcx%2BGJ%2FwOiaup0nkaMORgNW4KQHu%2Bk5EqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHbmlMZXalNzGpTvrSrcA6ndx2v44kD6811QU2tjiUlaRaAU9%2BlPBI7LSOre0dZYWIR5raw%2Fld0m2ujWsHv7XiESfgr9CVyZXE8X992%2B%2BmtWmSFOKZqYDi6WsNYoSQLTt%2BZ%2FoiBxJXK1W2Q4cczI7%2FDgfeJP0CBJC1o1P5XLPj7yteLNzXybTvuT9TYvQ85ffp3fSDdXGoTHmdthJLWlNT9cXk%2BFn%2FvGHQOBdvwrMmW9q3YYH1f5wY9ftgC1gbYSgieV%2BiEn367cxkcQ6gJ2kk%2F36m1iB4nOiC0XPq0scHOcPll7urPGYHB8M0rmweLjtVxJlnWZA5LVh97pfX5%2Bp1NJTxMCYCbRUprFYD8yTBrC7QLNqJmvHmzTgdBoTQw63hdkctqVML05ui3CvQeYyARsz1TiEsnld7r9Wg2NX2f3yDcCT%2BpcK7dlsGPBkpjtcStADJ30dlVCkhh8RumJt%2BB2xVHZyNEhuqIIA7hqAyUkkHSBkAbIuqKC%2FG5mJY9rK6dKqVsbENhYckZ7q1xjwTZCT1%2BGlmZN57GX9B5lBWihB68C4qlzU%2Fn0Gz4iyXCgh6zbAFHheD4r%2FzVrspztHy7R3yhljjQmZXj6mmL%2FNg6TqhIDUvx%2F%2F4oMlm2BCcLI%2FR4jnrVby68KPEdpMI%2F3%2BbwGOqUBIcgeLuopsgpX06599zFwmo2PpU%2FafHmU%2FHxpJE6BFD6QZiKvJZA%2FRuzk5pGT0walFIXNpWh9NyaoSEo7h1gHSn2W1egWGqDFrETw%2BjMGOxWSgJ5oMir1rR7iLaDikLBjayLvEGE%2F9X810P%2BqGjxUVPFsRSURpk%2FyPBhHTnYBGqo5aUuGrwKm3y0cGjrJ8s%2FSK%2BEgXOw6qMxxaxRI4VOrYsogc%2Flv&X-Amz-Signature=2dee0990b18ca11f5a10caa9412455d534acee9fdb29eff6b7369591654020c4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UEOOWWB%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG%2FcLLtWN2720cyJsH%2B%2BSYZiKM%2F3qbQCERP7PmCHi4tQAiEA6H8aEPHA%2BLhVcx%2BGJ%2FwOiaup0nkaMORgNW4KQHu%2Bk5EqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHbmlMZXalNzGpTvrSrcA6ndx2v44kD6811QU2tjiUlaRaAU9%2BlPBI7LSOre0dZYWIR5raw%2Fld0m2ujWsHv7XiESfgr9CVyZXE8X992%2B%2BmtWmSFOKZqYDi6WsNYoSQLTt%2BZ%2FoiBxJXK1W2Q4cczI7%2FDgfeJP0CBJC1o1P5XLPj7yteLNzXybTvuT9TYvQ85ffp3fSDdXGoTHmdthJLWlNT9cXk%2BFn%2FvGHQOBdvwrMmW9q3YYH1f5wY9ftgC1gbYSgieV%2BiEn367cxkcQ6gJ2kk%2F36m1iB4nOiC0XPq0scHOcPll7urPGYHB8M0rmweLjtVxJlnWZA5LVh97pfX5%2Bp1NJTxMCYCbRUprFYD8yTBrC7QLNqJmvHmzTgdBoTQw63hdkctqVML05ui3CvQeYyARsz1TiEsnld7r9Wg2NX2f3yDcCT%2BpcK7dlsGPBkpjtcStADJ30dlVCkhh8RumJt%2BB2xVHZyNEhuqIIA7hqAyUkkHSBkAbIuqKC%2FG5mJY9rK6dKqVsbENhYckZ7q1xjwTZCT1%2BGlmZN57GX9B5lBWihB68C4qlzU%2Fn0Gz4iyXCgh6zbAFHheD4r%2FzVrspztHy7R3yhljjQmZXj6mmL%2FNg6TqhIDUvx%2F%2F4oMlm2BCcLI%2FR4jnrVby68KPEdpMI%2F3%2BbwGOqUBIcgeLuopsgpX06599zFwmo2PpU%2FafHmU%2FHxpJE6BFD6QZiKvJZA%2FRuzk5pGT0walFIXNpWh9NyaoSEo7h1gHSn2W1egWGqDFrETw%2BjMGOxWSgJ5oMir1rR7iLaDikLBjayLvEGE%2F9X810P%2BqGjxUVPFsRSURpk%2FyPBhHTnYBGqo5aUuGrwKm3y0cGjrJ8s%2FSK%2BEgXOw6qMxxaxRI4VOrYsogc%2Flv&X-Amz-Signature=a43c639a2b0082a3a1f82e9151fc8ff1c227812d204657a8e3cbdcaf36941dd3&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
