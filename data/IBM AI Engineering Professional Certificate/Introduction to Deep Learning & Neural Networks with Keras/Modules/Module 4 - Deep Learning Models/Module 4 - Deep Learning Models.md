

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZCHA6BAY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T161555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAXaPu%2BI32KRXSDZ2IEy4RYlLGVBQhal4LLc%2FcFuvjw6AiBmDd4XryuhJESNLPzCrGePwcvRu4SKZzf5s8h8OPpeUSqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMc2mE11wBA8l%2Bg6DYKtwDqJw%2BKtDsB%2F0D4VRZasARCTfgwZi031WlVrQO8IOAgzQR1FcijSsEc%2Fr0SmafOJ0uQ6HipkRyZ8%2F4MMDKvREtdO643%2F%2B6kMVOJ4jmCU5K5Hv5evhv%2FnBZi94TWwGfUnQVLBzuAR%2F3mQrc7xHtkKUfLCu3f28%2FLacXZbfWzjoHGZOsq9b8robCRtzxzRBv4tZCubmIVzIpqhHmcZSlpL1OKfOpbjvefQ4E3BUbXSm1LeYZOdpM3cJrX3ibCus1hRVN5ioXZPfSZ1LA90tBCuWeco0Zd%2BMZYNdlOdfqBz93ING7LbkR4ubq1hjJePlVw5adAEt6GI5gwE0Xy1A5SYwsgl8N5CDFQxNe6Wg9j1P%2F%2FkcNIF9sv1HqTFL7Ozwl9p2VqjfJM3M7I5izozWD1LZL6lh0V3E4FtwJhGurQgUrsd%2FzBBgRIZt4YiWhZckjZSOLVKdJGuazi1mpzKX0I268epjmQRR5TEDVAGKrChhZKFvMl87pRTRN7r6aIjHHhrftKmswBOvVI9%2BLAEgRB%2BqB689GZNmU0DTqEQdOOxF7b%2FFouQ6c1brpqn0DeOMjTCvzwN3a6vqd%2B54It4FMy2m5Ue8MppFiDJtS1cxl7O4OZuUuUyx7s%2FSkwXgZ2Tswosr4vAY6pgEY6W4YpvSt3z1xWM%2FhaWJ5rBIxzu7iRYWLm4k1atFxL4H3uDxlb9BB24UlBkLbfJAxGVLhFa8GilDfAhr5xV3KKIqFDtSXB9mZQDJPyw4kuiFu3fSf16uUrYhiQPk6LtMzfb6OSRsiNU0Nl%2FMOe%2F1NIW3oFQV%2F7bh7zxbtQfiW%2BA9yIwdop%2Fh7TwI1csip35fyzmMr81EA9SXSt96lVTnhEsOrKz5k&X-Amz-Signature=ebd206ca6136db8d389c6b35af2b57d579ea00cd931af43c50a9c3a4f0a1aefe&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZCHA6BAY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T161555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAXaPu%2BI32KRXSDZ2IEy4RYlLGVBQhal4LLc%2FcFuvjw6AiBmDd4XryuhJESNLPzCrGePwcvRu4SKZzf5s8h8OPpeUSqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMc2mE11wBA8l%2Bg6DYKtwDqJw%2BKtDsB%2F0D4VRZasARCTfgwZi031WlVrQO8IOAgzQR1FcijSsEc%2Fr0SmafOJ0uQ6HipkRyZ8%2F4MMDKvREtdO643%2F%2B6kMVOJ4jmCU5K5Hv5evhv%2FnBZi94TWwGfUnQVLBzuAR%2F3mQrc7xHtkKUfLCu3f28%2FLacXZbfWzjoHGZOsq9b8robCRtzxzRBv4tZCubmIVzIpqhHmcZSlpL1OKfOpbjvefQ4E3BUbXSm1LeYZOdpM3cJrX3ibCus1hRVN5ioXZPfSZ1LA90tBCuWeco0Zd%2BMZYNdlOdfqBz93ING7LbkR4ubq1hjJePlVw5adAEt6GI5gwE0Xy1A5SYwsgl8N5CDFQxNe6Wg9j1P%2F%2FkcNIF9sv1HqTFL7Ozwl9p2VqjfJM3M7I5izozWD1LZL6lh0V3E4FtwJhGurQgUrsd%2FzBBgRIZt4YiWhZckjZSOLVKdJGuazi1mpzKX0I268epjmQRR5TEDVAGKrChhZKFvMl87pRTRN7r6aIjHHhrftKmswBOvVI9%2BLAEgRB%2BqB689GZNmU0DTqEQdOOxF7b%2FFouQ6c1brpqn0DeOMjTCvzwN3a6vqd%2B54It4FMy2m5Ue8MppFiDJtS1cxl7O4OZuUuUyx7s%2FSkwXgZ2Tswosr4vAY6pgEY6W4YpvSt3z1xWM%2FhaWJ5rBIxzu7iRYWLm4k1atFxL4H3uDxlb9BB24UlBkLbfJAxGVLhFa8GilDfAhr5xV3KKIqFDtSXB9mZQDJPyw4kuiFu3fSf16uUrYhiQPk6LtMzfb6OSRsiNU0Nl%2FMOe%2F1NIW3oFQV%2F7bh7zxbtQfiW%2BA9yIwdop%2Fh7TwI1csip35fyzmMr81EA9SXSt96lVTnhEsOrKz5k&X-Amz-Signature=5bfca02e80acc7714df130a55a46d1dcee31ca4d0ae6f651c0ca96748a4f344b&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZCHA6BAY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T161555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAXaPu%2BI32KRXSDZ2IEy4RYlLGVBQhal4LLc%2FcFuvjw6AiBmDd4XryuhJESNLPzCrGePwcvRu4SKZzf5s8h8OPpeUSqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMc2mE11wBA8l%2Bg6DYKtwDqJw%2BKtDsB%2F0D4VRZasARCTfgwZi031WlVrQO8IOAgzQR1FcijSsEc%2Fr0SmafOJ0uQ6HipkRyZ8%2F4MMDKvREtdO643%2F%2B6kMVOJ4jmCU5K5Hv5evhv%2FnBZi94TWwGfUnQVLBzuAR%2F3mQrc7xHtkKUfLCu3f28%2FLacXZbfWzjoHGZOsq9b8robCRtzxzRBv4tZCubmIVzIpqhHmcZSlpL1OKfOpbjvefQ4E3BUbXSm1LeYZOdpM3cJrX3ibCus1hRVN5ioXZPfSZ1LA90tBCuWeco0Zd%2BMZYNdlOdfqBz93ING7LbkR4ubq1hjJePlVw5adAEt6GI5gwE0Xy1A5SYwsgl8N5CDFQxNe6Wg9j1P%2F%2FkcNIF9sv1HqTFL7Ozwl9p2VqjfJM3M7I5izozWD1LZL6lh0V3E4FtwJhGurQgUrsd%2FzBBgRIZt4YiWhZckjZSOLVKdJGuazi1mpzKX0I268epjmQRR5TEDVAGKrChhZKFvMl87pRTRN7r6aIjHHhrftKmswBOvVI9%2BLAEgRB%2BqB689GZNmU0DTqEQdOOxF7b%2FFouQ6c1brpqn0DeOMjTCvzwN3a6vqd%2B54It4FMy2m5Ue8MppFiDJtS1cxl7O4OZuUuUyx7s%2FSkwXgZ2Tswosr4vAY6pgEY6W4YpvSt3z1xWM%2FhaWJ5rBIxzu7iRYWLm4k1atFxL4H3uDxlb9BB24UlBkLbfJAxGVLhFa8GilDfAhr5xV3KKIqFDtSXB9mZQDJPyw4kuiFu3fSf16uUrYhiQPk6LtMzfb6OSRsiNU0Nl%2FMOe%2F1NIW3oFQV%2F7bh7zxbtQfiW%2BA9yIwdop%2Fh7TwI1csip35fyzmMr81EA9SXSt96lVTnhEsOrKz5k&X-Amz-Signature=599b5c37cf7232ec872865887c07802c13dbd264227ccb745c8e8fa5ced0befe&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZCHA6BAY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T161555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAXaPu%2BI32KRXSDZ2IEy4RYlLGVBQhal4LLc%2FcFuvjw6AiBmDd4XryuhJESNLPzCrGePwcvRu4SKZzf5s8h8OPpeUSqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMc2mE11wBA8l%2Bg6DYKtwDqJw%2BKtDsB%2F0D4VRZasARCTfgwZi031WlVrQO8IOAgzQR1FcijSsEc%2Fr0SmafOJ0uQ6HipkRyZ8%2F4MMDKvREtdO643%2F%2B6kMVOJ4jmCU5K5Hv5evhv%2FnBZi94TWwGfUnQVLBzuAR%2F3mQrc7xHtkKUfLCu3f28%2FLacXZbfWzjoHGZOsq9b8robCRtzxzRBv4tZCubmIVzIpqhHmcZSlpL1OKfOpbjvefQ4E3BUbXSm1LeYZOdpM3cJrX3ibCus1hRVN5ioXZPfSZ1LA90tBCuWeco0Zd%2BMZYNdlOdfqBz93ING7LbkR4ubq1hjJePlVw5adAEt6GI5gwE0Xy1A5SYwsgl8N5CDFQxNe6Wg9j1P%2F%2FkcNIF9sv1HqTFL7Ozwl9p2VqjfJM3M7I5izozWD1LZL6lh0V3E4FtwJhGurQgUrsd%2FzBBgRIZt4YiWhZckjZSOLVKdJGuazi1mpzKX0I268epjmQRR5TEDVAGKrChhZKFvMl87pRTRN7r6aIjHHhrftKmswBOvVI9%2BLAEgRB%2BqB689GZNmU0DTqEQdOOxF7b%2FFouQ6c1brpqn0DeOMjTCvzwN3a6vqd%2B54It4FMy2m5Ue8MppFiDJtS1cxl7O4OZuUuUyx7s%2FSkwXgZ2Tswosr4vAY6pgEY6W4YpvSt3z1xWM%2FhaWJ5rBIxzu7iRYWLm4k1atFxL4H3uDxlb9BB24UlBkLbfJAxGVLhFa8GilDfAhr5xV3KKIqFDtSXB9mZQDJPyw4kuiFu3fSf16uUrYhiQPk6LtMzfb6OSRsiNU0Nl%2FMOe%2F1NIW3oFQV%2F7bh7zxbtQfiW%2BA9yIwdop%2Fh7TwI1csip35fyzmMr81EA9SXSt96lVTnhEsOrKz5k&X-Amz-Signature=e66b8430a45cc669a02b0e8e27fe83dcfe05af84504167e2901199f827bbaf48&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZCHA6BAY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T161555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAXaPu%2BI32KRXSDZ2IEy4RYlLGVBQhal4LLc%2FcFuvjw6AiBmDd4XryuhJESNLPzCrGePwcvRu4SKZzf5s8h8OPpeUSqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMc2mE11wBA8l%2Bg6DYKtwDqJw%2BKtDsB%2F0D4VRZasARCTfgwZi031WlVrQO8IOAgzQR1FcijSsEc%2Fr0SmafOJ0uQ6HipkRyZ8%2F4MMDKvREtdO643%2F%2B6kMVOJ4jmCU5K5Hv5evhv%2FnBZi94TWwGfUnQVLBzuAR%2F3mQrc7xHtkKUfLCu3f28%2FLacXZbfWzjoHGZOsq9b8robCRtzxzRBv4tZCubmIVzIpqhHmcZSlpL1OKfOpbjvefQ4E3BUbXSm1LeYZOdpM3cJrX3ibCus1hRVN5ioXZPfSZ1LA90tBCuWeco0Zd%2BMZYNdlOdfqBz93ING7LbkR4ubq1hjJePlVw5adAEt6GI5gwE0Xy1A5SYwsgl8N5CDFQxNe6Wg9j1P%2F%2FkcNIF9sv1HqTFL7Ozwl9p2VqjfJM3M7I5izozWD1LZL6lh0V3E4FtwJhGurQgUrsd%2FzBBgRIZt4YiWhZckjZSOLVKdJGuazi1mpzKX0I268epjmQRR5TEDVAGKrChhZKFvMl87pRTRN7r6aIjHHhrftKmswBOvVI9%2BLAEgRB%2BqB689GZNmU0DTqEQdOOxF7b%2FFouQ6c1brpqn0DeOMjTCvzwN3a6vqd%2B54It4FMy2m5Ue8MppFiDJtS1cxl7O4OZuUuUyx7s%2FSkwXgZ2Tswosr4vAY6pgEY6W4YpvSt3z1xWM%2FhaWJ5rBIxzu7iRYWLm4k1atFxL4H3uDxlb9BB24UlBkLbfJAxGVLhFa8GilDfAhr5xV3KKIqFDtSXB9mZQDJPyw4kuiFu3fSf16uUrYhiQPk6LtMzfb6OSRsiNU0Nl%2FMOe%2F1NIW3oFQV%2F7bh7zxbtQfiW%2BA9yIwdop%2Fh7TwI1csip35fyzmMr81EA9SXSt96lVTnhEsOrKz5k&X-Amz-Signature=b50cd45901192b82e44c383a322752ce6a87de5820a7ae52f6751e40faf31828&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZCHA6BAY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T161555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAXaPu%2BI32KRXSDZ2IEy4RYlLGVBQhal4LLc%2FcFuvjw6AiBmDd4XryuhJESNLPzCrGePwcvRu4SKZzf5s8h8OPpeUSqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMc2mE11wBA8l%2Bg6DYKtwDqJw%2BKtDsB%2F0D4VRZasARCTfgwZi031WlVrQO8IOAgzQR1FcijSsEc%2Fr0SmafOJ0uQ6HipkRyZ8%2F4MMDKvREtdO643%2F%2B6kMVOJ4jmCU5K5Hv5evhv%2FnBZi94TWwGfUnQVLBzuAR%2F3mQrc7xHtkKUfLCu3f28%2FLacXZbfWzjoHGZOsq9b8robCRtzxzRBv4tZCubmIVzIpqhHmcZSlpL1OKfOpbjvefQ4E3BUbXSm1LeYZOdpM3cJrX3ibCus1hRVN5ioXZPfSZ1LA90tBCuWeco0Zd%2BMZYNdlOdfqBz93ING7LbkR4ubq1hjJePlVw5adAEt6GI5gwE0Xy1A5SYwsgl8N5CDFQxNe6Wg9j1P%2F%2FkcNIF9sv1HqTFL7Ozwl9p2VqjfJM3M7I5izozWD1LZL6lh0V3E4FtwJhGurQgUrsd%2FzBBgRIZt4YiWhZckjZSOLVKdJGuazi1mpzKX0I268epjmQRR5TEDVAGKrChhZKFvMl87pRTRN7r6aIjHHhrftKmswBOvVI9%2BLAEgRB%2BqB689GZNmU0DTqEQdOOxF7b%2FFouQ6c1brpqn0DeOMjTCvzwN3a6vqd%2B54It4FMy2m5Ue8MppFiDJtS1cxl7O4OZuUuUyx7s%2FSkwXgZ2Tswosr4vAY6pgEY6W4YpvSt3z1xWM%2FhaWJ5rBIxzu7iRYWLm4k1atFxL4H3uDxlb9BB24UlBkLbfJAxGVLhFa8GilDfAhr5xV3KKIqFDtSXB9mZQDJPyw4kuiFu3fSf16uUrYhiQPk6LtMzfb6OSRsiNU0Nl%2FMOe%2F1NIW3oFQV%2F7bh7zxbtQfiW%2BA9yIwdop%2Fh7TwI1csip35fyzmMr81EA9SXSt96lVTnhEsOrKz5k&X-Amz-Signature=6ee4143469a3c1a867a239d036c52cf83368f297abd7a5ae2225e889b39d2940&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZCHA6BAY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T161555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAXaPu%2BI32KRXSDZ2IEy4RYlLGVBQhal4LLc%2FcFuvjw6AiBmDd4XryuhJESNLPzCrGePwcvRu4SKZzf5s8h8OPpeUSqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMc2mE11wBA8l%2Bg6DYKtwDqJw%2BKtDsB%2F0D4VRZasARCTfgwZi031WlVrQO8IOAgzQR1FcijSsEc%2Fr0SmafOJ0uQ6HipkRyZ8%2F4MMDKvREtdO643%2F%2B6kMVOJ4jmCU5K5Hv5evhv%2FnBZi94TWwGfUnQVLBzuAR%2F3mQrc7xHtkKUfLCu3f28%2FLacXZbfWzjoHGZOsq9b8robCRtzxzRBv4tZCubmIVzIpqhHmcZSlpL1OKfOpbjvefQ4E3BUbXSm1LeYZOdpM3cJrX3ibCus1hRVN5ioXZPfSZ1LA90tBCuWeco0Zd%2BMZYNdlOdfqBz93ING7LbkR4ubq1hjJePlVw5adAEt6GI5gwE0Xy1A5SYwsgl8N5CDFQxNe6Wg9j1P%2F%2FkcNIF9sv1HqTFL7Ozwl9p2VqjfJM3M7I5izozWD1LZL6lh0V3E4FtwJhGurQgUrsd%2FzBBgRIZt4YiWhZckjZSOLVKdJGuazi1mpzKX0I268epjmQRR5TEDVAGKrChhZKFvMl87pRTRN7r6aIjHHhrftKmswBOvVI9%2BLAEgRB%2BqB689GZNmU0DTqEQdOOxF7b%2FFouQ6c1brpqn0DeOMjTCvzwN3a6vqd%2B54It4FMy2m5Ue8MppFiDJtS1cxl7O4OZuUuUyx7s%2FSkwXgZ2Tswosr4vAY6pgEY6W4YpvSt3z1xWM%2FhaWJ5rBIxzu7iRYWLm4k1atFxL4H3uDxlb9BB24UlBkLbfJAxGVLhFa8GilDfAhr5xV3KKIqFDtSXB9mZQDJPyw4kuiFu3fSf16uUrYhiQPk6LtMzfb6OSRsiNU0Nl%2FMOe%2F1NIW3oFQV%2F7bh7zxbtQfiW%2BA9yIwdop%2Fh7TwI1csip35fyzmMr81EA9SXSt96lVTnhEsOrKz5k&X-Amz-Signature=68d0054598330926eb87e2e1fab7e351c97d7c5b9a3e09d0c552d3548652b83c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZCHA6BAY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T161555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAXaPu%2BI32KRXSDZ2IEy4RYlLGVBQhal4LLc%2FcFuvjw6AiBmDd4XryuhJESNLPzCrGePwcvRu4SKZzf5s8h8OPpeUSqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMc2mE11wBA8l%2Bg6DYKtwDqJw%2BKtDsB%2F0D4VRZasARCTfgwZi031WlVrQO8IOAgzQR1FcijSsEc%2Fr0SmafOJ0uQ6HipkRyZ8%2F4MMDKvREtdO643%2F%2B6kMVOJ4jmCU5K5Hv5evhv%2FnBZi94TWwGfUnQVLBzuAR%2F3mQrc7xHtkKUfLCu3f28%2FLacXZbfWzjoHGZOsq9b8robCRtzxzRBv4tZCubmIVzIpqhHmcZSlpL1OKfOpbjvefQ4E3BUbXSm1LeYZOdpM3cJrX3ibCus1hRVN5ioXZPfSZ1LA90tBCuWeco0Zd%2BMZYNdlOdfqBz93ING7LbkR4ubq1hjJePlVw5adAEt6GI5gwE0Xy1A5SYwsgl8N5CDFQxNe6Wg9j1P%2F%2FkcNIF9sv1HqTFL7Ozwl9p2VqjfJM3M7I5izozWD1LZL6lh0V3E4FtwJhGurQgUrsd%2FzBBgRIZt4YiWhZckjZSOLVKdJGuazi1mpzKX0I268epjmQRR5TEDVAGKrChhZKFvMl87pRTRN7r6aIjHHhrftKmswBOvVI9%2BLAEgRB%2BqB689GZNmU0DTqEQdOOxF7b%2FFouQ6c1brpqn0DeOMjTCvzwN3a6vqd%2B54It4FMy2m5Ue8MppFiDJtS1cxl7O4OZuUuUyx7s%2FSkwXgZ2Tswosr4vAY6pgEY6W4YpvSt3z1xWM%2FhaWJ5rBIxzu7iRYWLm4k1atFxL4H3uDxlb9BB24UlBkLbfJAxGVLhFa8GilDfAhr5xV3KKIqFDtSXB9mZQDJPyw4kuiFu3fSf16uUrYhiQPk6LtMzfb6OSRsiNU0Nl%2FMOe%2F1NIW3oFQV%2F7bh7zxbtQfiW%2BA9yIwdop%2Fh7TwI1csip35fyzmMr81EA9SXSt96lVTnhEsOrKz5k&X-Amz-Signature=ec2467dd95eb3697d53ccd824529887074176647b5bd3997c2bcae82d6265f47&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZCHA6BAY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T161555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAXaPu%2BI32KRXSDZ2IEy4RYlLGVBQhal4LLc%2FcFuvjw6AiBmDd4XryuhJESNLPzCrGePwcvRu4SKZzf5s8h8OPpeUSqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMc2mE11wBA8l%2Bg6DYKtwDqJw%2BKtDsB%2F0D4VRZasARCTfgwZi031WlVrQO8IOAgzQR1FcijSsEc%2Fr0SmafOJ0uQ6HipkRyZ8%2F4MMDKvREtdO643%2F%2B6kMVOJ4jmCU5K5Hv5evhv%2FnBZi94TWwGfUnQVLBzuAR%2F3mQrc7xHtkKUfLCu3f28%2FLacXZbfWzjoHGZOsq9b8robCRtzxzRBv4tZCubmIVzIpqhHmcZSlpL1OKfOpbjvefQ4E3BUbXSm1LeYZOdpM3cJrX3ibCus1hRVN5ioXZPfSZ1LA90tBCuWeco0Zd%2BMZYNdlOdfqBz93ING7LbkR4ubq1hjJePlVw5adAEt6GI5gwE0Xy1A5SYwsgl8N5CDFQxNe6Wg9j1P%2F%2FkcNIF9sv1HqTFL7Ozwl9p2VqjfJM3M7I5izozWD1LZL6lh0V3E4FtwJhGurQgUrsd%2FzBBgRIZt4YiWhZckjZSOLVKdJGuazi1mpzKX0I268epjmQRR5TEDVAGKrChhZKFvMl87pRTRN7r6aIjHHhrftKmswBOvVI9%2BLAEgRB%2BqB689GZNmU0DTqEQdOOxF7b%2FFouQ6c1brpqn0DeOMjTCvzwN3a6vqd%2B54It4FMy2m5Ue8MppFiDJtS1cxl7O4OZuUuUyx7s%2FSkwXgZ2Tswosr4vAY6pgEY6W4YpvSt3z1xWM%2FhaWJ5rBIxzu7iRYWLm4k1atFxL4H3uDxlb9BB24UlBkLbfJAxGVLhFa8GilDfAhr5xV3KKIqFDtSXB9mZQDJPyw4kuiFu3fSf16uUrYhiQPk6LtMzfb6OSRsiNU0Nl%2FMOe%2F1NIW3oFQV%2F7bh7zxbtQfiW%2BA9yIwdop%2Fh7TwI1csip35fyzmMr81EA9SXSt96lVTnhEsOrKz5k&X-Amz-Signature=d5dbd247172009c1269f0b2d8b28aad8108b2cbdc907bdc6a0d9f99d6078a9b0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WARNE2CI%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T161555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC5jSsLMiUrKWs96CCw9ty578C3HL0QLpn87lbZuWYxVQIhAI0BIlLgluQKwmyW2MjhvXj%2BmjDWBzVVwZymzeCTjcH8KogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwAYCuwPz%2BaHMOjk8wq3AMEwyCvzhFQQZeOcOVFAokAfUQGE%2BEGf40BFvBceO03QNzizrkf3HSGeKyJBM%2BiIw5JpIfk5jsEinCxG%2Bx2WYhDGdiVeGSTECAlIGL88UyD%2FyIyrg2pRyY833XDaHlPCZoJ2hX%2FbwfFqjHj7DG2%2FXd1%2FI%2FmZERAFrNeMa82CqvhLDN5YO%2BlZViHqyrR2aNFilTX0jQ1t%2B1ZvFSWPDk6Mxwcby6TPdSBQ8w468FNOpR4vY6sRxUH9YHmKcAZ8ZEgWSn5JFzbmjR%2FjHrt%2FupGO%2FLTHXEOW1tn1rBvdH2JPvtwdyv2wztFF9rWRJ0iF5d14E0kClVQshIxXjq%2F%2Fq0ltb7GxAk3%2BNfAmwbxiyOc%2BEruSsyEFLT0SztuVy0HXS2uRwNNLSwdu%2B6NGIKrNkyKJlxwzaXJgR1dtpbEuWtBieLVJjt%2FbCEFLro%2FQHyLpEp384tEu9KrnlYK%2BaGijobGapURtv5FDntHeraiNwc169T2zN%2Btksqp7C%2F6TIxLk3auAd0ZyqEjAXE%2Fp12tnEA2jgHe9YfgekYZMdCOdG%2BEfcCjjfRozkERXbPN7sJz6Nmq%2BsR9b0c1Kn2LlnFCRff2ohY16H7vly4Wg7ujRiz%2BiADFDAaFkPQ04AHa%2B3930zD7yfi8BjqkAbnuu%2FRZKf2TK2ih2JRjp5DuJUwln%2BzK8VGDb5NyQAYz2zTjfmSK9sqiIZ6Hz29K77t%2ByaMB0pYYR41ssMhBg2TWnWnmtktS9e9Q5vM5wYtOQqDu2CC9XjPOvv%2BfYpv5SLaKNV2KsiYxPSiJAUyVsHOablZB5IZUjxMuaNTpI3ENZJ11D4PpCthrYNZKJiZMC%2FjWWs6uFeSx8O%2BzZnWP1OMTAA7a&X-Amz-Signature=26693ecf0a1e16f92213a5adb15765d6074b1e370d3b0f52dedd975c6bad873c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WARNE2CI%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T161555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC5jSsLMiUrKWs96CCw9ty578C3HL0QLpn87lbZuWYxVQIhAI0BIlLgluQKwmyW2MjhvXj%2BmjDWBzVVwZymzeCTjcH8KogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwAYCuwPz%2BaHMOjk8wq3AMEwyCvzhFQQZeOcOVFAokAfUQGE%2BEGf40BFvBceO03QNzizrkf3HSGeKyJBM%2BiIw5JpIfk5jsEinCxG%2Bx2WYhDGdiVeGSTECAlIGL88UyD%2FyIyrg2pRyY833XDaHlPCZoJ2hX%2FbwfFqjHj7DG2%2FXd1%2FI%2FmZERAFrNeMa82CqvhLDN5YO%2BlZViHqyrR2aNFilTX0jQ1t%2B1ZvFSWPDk6Mxwcby6TPdSBQ8w468FNOpR4vY6sRxUH9YHmKcAZ8ZEgWSn5JFzbmjR%2FjHrt%2FupGO%2FLTHXEOW1tn1rBvdH2JPvtwdyv2wztFF9rWRJ0iF5d14E0kClVQshIxXjq%2F%2Fq0ltb7GxAk3%2BNfAmwbxiyOc%2BEruSsyEFLT0SztuVy0HXS2uRwNNLSwdu%2B6NGIKrNkyKJlxwzaXJgR1dtpbEuWtBieLVJjt%2FbCEFLro%2FQHyLpEp384tEu9KrnlYK%2BaGijobGapURtv5FDntHeraiNwc169T2zN%2Btksqp7C%2F6TIxLk3auAd0ZyqEjAXE%2Fp12tnEA2jgHe9YfgekYZMdCOdG%2BEfcCjjfRozkERXbPN7sJz6Nmq%2BsR9b0c1Kn2LlnFCRff2ohY16H7vly4Wg7ujRiz%2BiADFDAaFkPQ04AHa%2B3930zD7yfi8BjqkAbnuu%2FRZKf2TK2ih2JRjp5DuJUwln%2BzK8VGDb5NyQAYz2zTjfmSK9sqiIZ6Hz29K77t%2ByaMB0pYYR41ssMhBg2TWnWnmtktS9e9Q5vM5wYtOQqDu2CC9XjPOvv%2BfYpv5SLaKNV2KsiYxPSiJAUyVsHOablZB5IZUjxMuaNTpI3ENZJ11D4PpCthrYNZKJiZMC%2FjWWs6uFeSx8O%2BzZnWP1OMTAA7a&X-Amz-Signature=4f5228c48b814fdea4de39b28fac0b73c99a42e08c65ad1332c7acd37827783e&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
