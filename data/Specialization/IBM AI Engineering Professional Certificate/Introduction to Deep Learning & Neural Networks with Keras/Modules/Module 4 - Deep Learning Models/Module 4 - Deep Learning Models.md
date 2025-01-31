

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OZK6VRR%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T091511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDuoDbCH9qKHMtB62uAXGLVOdQW0zmPs8%2BlQ19toLFrqAIhALJo5g51x9o32lH5GURwj40iVOazw%2FfXl%2BSxQbQr2ab4KogECLr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxPNgIaJmfpZ29C0uoq3AMqrnbkQad07bVW24jlU4rQN7RaitU5s1aJe0oC%2FQcPcjR5Jus2lc295Uq2OVRNIURt0DqwabQhkjzxpg2di4vIsi8w15%2FjdkYNReBbFoccpUcr0C0ZPsA%2BkOgWz4559dttQKIra2pI4UpSL5A1HlsqeiDqQ7GP%2Bj61hGaJ8bdvNSbnbA%2BDY49VSVWB12cTu%2FwoUzrk48HTkhK5b2qec1obBPnqgLMHyiQBNtAxUs3mD0dlHe5E8iIjh9r3XYq5Ejbn30pAHNRwDo3Kpk2a8peQtODSDs7gyAod4W%2FVSD2L4F%2Bl36BaXOhXpa%2FarsJyRtyu0fLbFTdVmyoLZWf1IOmg2nBdIqNHsj5lEDFasTosWLj8lRk%2FJtrQriUlqwQuwxLxT9Zy1NWJqxKx%2F0vpR2iGJ04J4f4%2BEKWVdWte8joleULg6XOu1IuX9Pa4Swpj6%2B6jANrDVHWdvGVURzU6yr7HJHF9mx1bWQmQkPtY7EVaKuiFdCMo0a%2Fz5HpEOn9TEqyhgsFtsq9ElDPFbzgKjyAapwi7xI6TOa4R5za9xeKGGpbZ1WI%2BKYRqwybqMA86C5Jx%2F5%2B9Ja%2FZwdBB8do2jTxXN7RuZpic0KOjpFOJQ9J65qWA7xo1BlkfKrGNODDgmvK8BjqkAUjCwGUbQLlqSDBJ5A%2Fg2hzvFqaZIrfOQX0kd4eJ6PnwkDlfB73qBX82GhBoT336Hj2kA5zz%2BW4II0I5b0I0F6EpSyUVQ7bYigjAaOizSQSOcLWnwVn9kvrE7htcRZgLsWDKD42qrJztHQaiJXKDis8UXY2vZlSsS6q%2FCe%2BeddYmDtfr3YAQu%2F%2FMB8nZZc03sLji8CqXZcoHNxM4c12DyRZfeicp&X-Amz-Signature=d89250f45f4608c1fd5599c33771ee8b980a8cb576d040e6dd5ccee045b7d16b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OZK6VRR%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T091511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDuoDbCH9qKHMtB62uAXGLVOdQW0zmPs8%2BlQ19toLFrqAIhALJo5g51x9o32lH5GURwj40iVOazw%2FfXl%2BSxQbQr2ab4KogECLr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxPNgIaJmfpZ29C0uoq3AMqrnbkQad07bVW24jlU4rQN7RaitU5s1aJe0oC%2FQcPcjR5Jus2lc295Uq2OVRNIURt0DqwabQhkjzxpg2di4vIsi8w15%2FjdkYNReBbFoccpUcr0C0ZPsA%2BkOgWz4559dttQKIra2pI4UpSL5A1HlsqeiDqQ7GP%2Bj61hGaJ8bdvNSbnbA%2BDY49VSVWB12cTu%2FwoUzrk48HTkhK5b2qec1obBPnqgLMHyiQBNtAxUs3mD0dlHe5E8iIjh9r3XYq5Ejbn30pAHNRwDo3Kpk2a8peQtODSDs7gyAod4W%2FVSD2L4F%2Bl36BaXOhXpa%2FarsJyRtyu0fLbFTdVmyoLZWf1IOmg2nBdIqNHsj5lEDFasTosWLj8lRk%2FJtrQriUlqwQuwxLxT9Zy1NWJqxKx%2F0vpR2iGJ04J4f4%2BEKWVdWte8joleULg6XOu1IuX9Pa4Swpj6%2B6jANrDVHWdvGVURzU6yr7HJHF9mx1bWQmQkPtY7EVaKuiFdCMo0a%2Fz5HpEOn9TEqyhgsFtsq9ElDPFbzgKjyAapwi7xI6TOa4R5za9xeKGGpbZ1WI%2BKYRqwybqMA86C5Jx%2F5%2B9Ja%2FZwdBB8do2jTxXN7RuZpic0KOjpFOJQ9J65qWA7xo1BlkfKrGNODDgmvK8BjqkAUjCwGUbQLlqSDBJ5A%2Fg2hzvFqaZIrfOQX0kd4eJ6PnwkDlfB73qBX82GhBoT336Hj2kA5zz%2BW4II0I5b0I0F6EpSyUVQ7bYigjAaOizSQSOcLWnwVn9kvrE7htcRZgLsWDKD42qrJztHQaiJXKDis8UXY2vZlSsS6q%2FCe%2BeddYmDtfr3YAQu%2F%2FMB8nZZc03sLji8CqXZcoHNxM4c12DyRZfeicp&X-Amz-Signature=0ac4c39228bff5a6c94851b4a947610490245bdc950dbf15889f4a8be6be35b2&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OZK6VRR%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T091511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDuoDbCH9qKHMtB62uAXGLVOdQW0zmPs8%2BlQ19toLFrqAIhALJo5g51x9o32lH5GURwj40iVOazw%2FfXl%2BSxQbQr2ab4KogECLr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxPNgIaJmfpZ29C0uoq3AMqrnbkQad07bVW24jlU4rQN7RaitU5s1aJe0oC%2FQcPcjR5Jus2lc295Uq2OVRNIURt0DqwabQhkjzxpg2di4vIsi8w15%2FjdkYNReBbFoccpUcr0C0ZPsA%2BkOgWz4559dttQKIra2pI4UpSL5A1HlsqeiDqQ7GP%2Bj61hGaJ8bdvNSbnbA%2BDY49VSVWB12cTu%2FwoUzrk48HTkhK5b2qec1obBPnqgLMHyiQBNtAxUs3mD0dlHe5E8iIjh9r3XYq5Ejbn30pAHNRwDo3Kpk2a8peQtODSDs7gyAod4W%2FVSD2L4F%2Bl36BaXOhXpa%2FarsJyRtyu0fLbFTdVmyoLZWf1IOmg2nBdIqNHsj5lEDFasTosWLj8lRk%2FJtrQriUlqwQuwxLxT9Zy1NWJqxKx%2F0vpR2iGJ04J4f4%2BEKWVdWte8joleULg6XOu1IuX9Pa4Swpj6%2B6jANrDVHWdvGVURzU6yr7HJHF9mx1bWQmQkPtY7EVaKuiFdCMo0a%2Fz5HpEOn9TEqyhgsFtsq9ElDPFbzgKjyAapwi7xI6TOa4R5za9xeKGGpbZ1WI%2BKYRqwybqMA86C5Jx%2F5%2B9Ja%2FZwdBB8do2jTxXN7RuZpic0KOjpFOJQ9J65qWA7xo1BlkfKrGNODDgmvK8BjqkAUjCwGUbQLlqSDBJ5A%2Fg2hzvFqaZIrfOQX0kd4eJ6PnwkDlfB73qBX82GhBoT336Hj2kA5zz%2BW4II0I5b0I0F6EpSyUVQ7bYigjAaOizSQSOcLWnwVn9kvrE7htcRZgLsWDKD42qrJztHQaiJXKDis8UXY2vZlSsS6q%2FCe%2BeddYmDtfr3YAQu%2F%2FMB8nZZc03sLji8CqXZcoHNxM4c12DyRZfeicp&X-Amz-Signature=e8e9413e984ea971351580beb7bc451e0834f2229df359f2d5a31eed02fda6f0&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OZK6VRR%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T091511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDuoDbCH9qKHMtB62uAXGLVOdQW0zmPs8%2BlQ19toLFrqAIhALJo5g51x9o32lH5GURwj40iVOazw%2FfXl%2BSxQbQr2ab4KogECLr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxPNgIaJmfpZ29C0uoq3AMqrnbkQad07bVW24jlU4rQN7RaitU5s1aJe0oC%2FQcPcjR5Jus2lc295Uq2OVRNIURt0DqwabQhkjzxpg2di4vIsi8w15%2FjdkYNReBbFoccpUcr0C0ZPsA%2BkOgWz4559dttQKIra2pI4UpSL5A1HlsqeiDqQ7GP%2Bj61hGaJ8bdvNSbnbA%2BDY49VSVWB12cTu%2FwoUzrk48HTkhK5b2qec1obBPnqgLMHyiQBNtAxUs3mD0dlHe5E8iIjh9r3XYq5Ejbn30pAHNRwDo3Kpk2a8peQtODSDs7gyAod4W%2FVSD2L4F%2Bl36BaXOhXpa%2FarsJyRtyu0fLbFTdVmyoLZWf1IOmg2nBdIqNHsj5lEDFasTosWLj8lRk%2FJtrQriUlqwQuwxLxT9Zy1NWJqxKx%2F0vpR2iGJ04J4f4%2BEKWVdWte8joleULg6XOu1IuX9Pa4Swpj6%2B6jANrDVHWdvGVURzU6yr7HJHF9mx1bWQmQkPtY7EVaKuiFdCMo0a%2Fz5HpEOn9TEqyhgsFtsq9ElDPFbzgKjyAapwi7xI6TOa4R5za9xeKGGpbZ1WI%2BKYRqwybqMA86C5Jx%2F5%2B9Ja%2FZwdBB8do2jTxXN7RuZpic0KOjpFOJQ9J65qWA7xo1BlkfKrGNODDgmvK8BjqkAUjCwGUbQLlqSDBJ5A%2Fg2hzvFqaZIrfOQX0kd4eJ6PnwkDlfB73qBX82GhBoT336Hj2kA5zz%2BW4II0I5b0I0F6EpSyUVQ7bYigjAaOizSQSOcLWnwVn9kvrE7htcRZgLsWDKD42qrJztHQaiJXKDis8UXY2vZlSsS6q%2FCe%2BeddYmDtfr3YAQu%2F%2FMB8nZZc03sLji8CqXZcoHNxM4c12DyRZfeicp&X-Amz-Signature=729c25846ef00babd7f75bbf29d14b94d598abc457bf2c4fea6dcac778214b96&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OZK6VRR%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T091511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDuoDbCH9qKHMtB62uAXGLVOdQW0zmPs8%2BlQ19toLFrqAIhALJo5g51x9o32lH5GURwj40iVOazw%2FfXl%2BSxQbQr2ab4KogECLr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxPNgIaJmfpZ29C0uoq3AMqrnbkQad07bVW24jlU4rQN7RaitU5s1aJe0oC%2FQcPcjR5Jus2lc295Uq2OVRNIURt0DqwabQhkjzxpg2di4vIsi8w15%2FjdkYNReBbFoccpUcr0C0ZPsA%2BkOgWz4559dttQKIra2pI4UpSL5A1HlsqeiDqQ7GP%2Bj61hGaJ8bdvNSbnbA%2BDY49VSVWB12cTu%2FwoUzrk48HTkhK5b2qec1obBPnqgLMHyiQBNtAxUs3mD0dlHe5E8iIjh9r3XYq5Ejbn30pAHNRwDo3Kpk2a8peQtODSDs7gyAod4W%2FVSD2L4F%2Bl36BaXOhXpa%2FarsJyRtyu0fLbFTdVmyoLZWf1IOmg2nBdIqNHsj5lEDFasTosWLj8lRk%2FJtrQriUlqwQuwxLxT9Zy1NWJqxKx%2F0vpR2iGJ04J4f4%2BEKWVdWte8joleULg6XOu1IuX9Pa4Swpj6%2B6jANrDVHWdvGVURzU6yr7HJHF9mx1bWQmQkPtY7EVaKuiFdCMo0a%2Fz5HpEOn9TEqyhgsFtsq9ElDPFbzgKjyAapwi7xI6TOa4R5za9xeKGGpbZ1WI%2BKYRqwybqMA86C5Jx%2F5%2B9Ja%2FZwdBB8do2jTxXN7RuZpic0KOjpFOJQ9J65qWA7xo1BlkfKrGNODDgmvK8BjqkAUjCwGUbQLlqSDBJ5A%2Fg2hzvFqaZIrfOQX0kd4eJ6PnwkDlfB73qBX82GhBoT336Hj2kA5zz%2BW4II0I5b0I0F6EpSyUVQ7bYigjAaOizSQSOcLWnwVn9kvrE7htcRZgLsWDKD42qrJztHQaiJXKDis8UXY2vZlSsS6q%2FCe%2BeddYmDtfr3YAQu%2F%2FMB8nZZc03sLji8CqXZcoHNxM4c12DyRZfeicp&X-Amz-Signature=2658f748e68d12607c1f53408b33f0a8db470310c90aed94c5ec933f59c3eeb1&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OZK6VRR%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T091511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDuoDbCH9qKHMtB62uAXGLVOdQW0zmPs8%2BlQ19toLFrqAIhALJo5g51x9o32lH5GURwj40iVOazw%2FfXl%2BSxQbQr2ab4KogECLr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxPNgIaJmfpZ29C0uoq3AMqrnbkQad07bVW24jlU4rQN7RaitU5s1aJe0oC%2FQcPcjR5Jus2lc295Uq2OVRNIURt0DqwabQhkjzxpg2di4vIsi8w15%2FjdkYNReBbFoccpUcr0C0ZPsA%2BkOgWz4559dttQKIra2pI4UpSL5A1HlsqeiDqQ7GP%2Bj61hGaJ8bdvNSbnbA%2BDY49VSVWB12cTu%2FwoUzrk48HTkhK5b2qec1obBPnqgLMHyiQBNtAxUs3mD0dlHe5E8iIjh9r3XYq5Ejbn30pAHNRwDo3Kpk2a8peQtODSDs7gyAod4W%2FVSD2L4F%2Bl36BaXOhXpa%2FarsJyRtyu0fLbFTdVmyoLZWf1IOmg2nBdIqNHsj5lEDFasTosWLj8lRk%2FJtrQriUlqwQuwxLxT9Zy1NWJqxKx%2F0vpR2iGJ04J4f4%2BEKWVdWte8joleULg6XOu1IuX9Pa4Swpj6%2B6jANrDVHWdvGVURzU6yr7HJHF9mx1bWQmQkPtY7EVaKuiFdCMo0a%2Fz5HpEOn9TEqyhgsFtsq9ElDPFbzgKjyAapwi7xI6TOa4R5za9xeKGGpbZ1WI%2BKYRqwybqMA86C5Jx%2F5%2B9Ja%2FZwdBB8do2jTxXN7RuZpic0KOjpFOJQ9J65qWA7xo1BlkfKrGNODDgmvK8BjqkAUjCwGUbQLlqSDBJ5A%2Fg2hzvFqaZIrfOQX0kd4eJ6PnwkDlfB73qBX82GhBoT336Hj2kA5zz%2BW4II0I5b0I0F6EpSyUVQ7bYigjAaOizSQSOcLWnwVn9kvrE7htcRZgLsWDKD42qrJztHQaiJXKDis8UXY2vZlSsS6q%2FCe%2BeddYmDtfr3YAQu%2F%2FMB8nZZc03sLji8CqXZcoHNxM4c12DyRZfeicp&X-Amz-Signature=98932ce716de36ae2b000ea04d818e37c4bcfb3da3556e03ab60f039daee5ecb&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OZK6VRR%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T091511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDuoDbCH9qKHMtB62uAXGLVOdQW0zmPs8%2BlQ19toLFrqAIhALJo5g51x9o32lH5GURwj40iVOazw%2FfXl%2BSxQbQr2ab4KogECLr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxPNgIaJmfpZ29C0uoq3AMqrnbkQad07bVW24jlU4rQN7RaitU5s1aJe0oC%2FQcPcjR5Jus2lc295Uq2OVRNIURt0DqwabQhkjzxpg2di4vIsi8w15%2FjdkYNReBbFoccpUcr0C0ZPsA%2BkOgWz4559dttQKIra2pI4UpSL5A1HlsqeiDqQ7GP%2Bj61hGaJ8bdvNSbnbA%2BDY49VSVWB12cTu%2FwoUzrk48HTkhK5b2qec1obBPnqgLMHyiQBNtAxUs3mD0dlHe5E8iIjh9r3XYq5Ejbn30pAHNRwDo3Kpk2a8peQtODSDs7gyAod4W%2FVSD2L4F%2Bl36BaXOhXpa%2FarsJyRtyu0fLbFTdVmyoLZWf1IOmg2nBdIqNHsj5lEDFasTosWLj8lRk%2FJtrQriUlqwQuwxLxT9Zy1NWJqxKx%2F0vpR2iGJ04J4f4%2BEKWVdWte8joleULg6XOu1IuX9Pa4Swpj6%2B6jANrDVHWdvGVURzU6yr7HJHF9mx1bWQmQkPtY7EVaKuiFdCMo0a%2Fz5HpEOn9TEqyhgsFtsq9ElDPFbzgKjyAapwi7xI6TOa4R5za9xeKGGpbZ1WI%2BKYRqwybqMA86C5Jx%2F5%2B9Ja%2FZwdBB8do2jTxXN7RuZpic0KOjpFOJQ9J65qWA7xo1BlkfKrGNODDgmvK8BjqkAUjCwGUbQLlqSDBJ5A%2Fg2hzvFqaZIrfOQX0kd4eJ6PnwkDlfB73qBX82GhBoT336Hj2kA5zz%2BW4II0I5b0I0F6EpSyUVQ7bYigjAaOizSQSOcLWnwVn9kvrE7htcRZgLsWDKD42qrJztHQaiJXKDis8UXY2vZlSsS6q%2FCe%2BeddYmDtfr3YAQu%2F%2FMB8nZZc03sLji8CqXZcoHNxM4c12DyRZfeicp&X-Amz-Signature=d38c8536a5c0075cdb1105ee92db214d6367eccc252d8f720df3174f1d7bcf33&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OZK6VRR%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T091511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDuoDbCH9qKHMtB62uAXGLVOdQW0zmPs8%2BlQ19toLFrqAIhALJo5g51x9o32lH5GURwj40iVOazw%2FfXl%2BSxQbQr2ab4KogECLr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxPNgIaJmfpZ29C0uoq3AMqrnbkQad07bVW24jlU4rQN7RaitU5s1aJe0oC%2FQcPcjR5Jus2lc295Uq2OVRNIURt0DqwabQhkjzxpg2di4vIsi8w15%2FjdkYNReBbFoccpUcr0C0ZPsA%2BkOgWz4559dttQKIra2pI4UpSL5A1HlsqeiDqQ7GP%2Bj61hGaJ8bdvNSbnbA%2BDY49VSVWB12cTu%2FwoUzrk48HTkhK5b2qec1obBPnqgLMHyiQBNtAxUs3mD0dlHe5E8iIjh9r3XYq5Ejbn30pAHNRwDo3Kpk2a8peQtODSDs7gyAod4W%2FVSD2L4F%2Bl36BaXOhXpa%2FarsJyRtyu0fLbFTdVmyoLZWf1IOmg2nBdIqNHsj5lEDFasTosWLj8lRk%2FJtrQriUlqwQuwxLxT9Zy1NWJqxKx%2F0vpR2iGJ04J4f4%2BEKWVdWte8joleULg6XOu1IuX9Pa4Swpj6%2B6jANrDVHWdvGVURzU6yr7HJHF9mx1bWQmQkPtY7EVaKuiFdCMo0a%2Fz5HpEOn9TEqyhgsFtsq9ElDPFbzgKjyAapwi7xI6TOa4R5za9xeKGGpbZ1WI%2BKYRqwybqMA86C5Jx%2F5%2B9Ja%2FZwdBB8do2jTxXN7RuZpic0KOjpFOJQ9J65qWA7xo1BlkfKrGNODDgmvK8BjqkAUjCwGUbQLlqSDBJ5A%2Fg2hzvFqaZIrfOQX0kd4eJ6PnwkDlfB73qBX82GhBoT336Hj2kA5zz%2BW4II0I5b0I0F6EpSyUVQ7bYigjAaOizSQSOcLWnwVn9kvrE7htcRZgLsWDKD42qrJztHQaiJXKDis8UXY2vZlSsS6q%2FCe%2BeddYmDtfr3YAQu%2F%2FMB8nZZc03sLji8CqXZcoHNxM4c12DyRZfeicp&X-Amz-Signature=cef76e82ebfa82657b72d754cf057568a9d7b85018a10d1e61b9dedef5bb0fa2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OZK6VRR%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T091511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDuoDbCH9qKHMtB62uAXGLVOdQW0zmPs8%2BlQ19toLFrqAIhALJo5g51x9o32lH5GURwj40iVOazw%2FfXl%2BSxQbQr2ab4KogECLr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxPNgIaJmfpZ29C0uoq3AMqrnbkQad07bVW24jlU4rQN7RaitU5s1aJe0oC%2FQcPcjR5Jus2lc295Uq2OVRNIURt0DqwabQhkjzxpg2di4vIsi8w15%2FjdkYNReBbFoccpUcr0C0ZPsA%2BkOgWz4559dttQKIra2pI4UpSL5A1HlsqeiDqQ7GP%2Bj61hGaJ8bdvNSbnbA%2BDY49VSVWB12cTu%2FwoUzrk48HTkhK5b2qec1obBPnqgLMHyiQBNtAxUs3mD0dlHe5E8iIjh9r3XYq5Ejbn30pAHNRwDo3Kpk2a8peQtODSDs7gyAod4W%2FVSD2L4F%2Bl36BaXOhXpa%2FarsJyRtyu0fLbFTdVmyoLZWf1IOmg2nBdIqNHsj5lEDFasTosWLj8lRk%2FJtrQriUlqwQuwxLxT9Zy1NWJqxKx%2F0vpR2iGJ04J4f4%2BEKWVdWte8joleULg6XOu1IuX9Pa4Swpj6%2B6jANrDVHWdvGVURzU6yr7HJHF9mx1bWQmQkPtY7EVaKuiFdCMo0a%2Fz5HpEOn9TEqyhgsFtsq9ElDPFbzgKjyAapwi7xI6TOa4R5za9xeKGGpbZ1WI%2BKYRqwybqMA86C5Jx%2F5%2B9Ja%2FZwdBB8do2jTxXN7RuZpic0KOjpFOJQ9J65qWA7xo1BlkfKrGNODDgmvK8BjqkAUjCwGUbQLlqSDBJ5A%2Fg2hzvFqaZIrfOQX0kd4eJ6PnwkDlfB73qBX82GhBoT336Hj2kA5zz%2BW4II0I5b0I0F6EpSyUVQ7bYigjAaOizSQSOcLWnwVn9kvrE7htcRZgLsWDKD42qrJztHQaiJXKDis8UXY2vZlSsS6q%2FCe%2BeddYmDtfr3YAQu%2F%2FMB8nZZc03sLji8CqXZcoHNxM4c12DyRZfeicp&X-Amz-Signature=7d76abcec517fba98731b416343bcf4bf389d5e775157d7e38394b614841196b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662MRJJABY%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T091512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC7C1Ykk2qdB0vmgFUyWB7OAznr2hjB2MDUwh1bGiauDwIgK1fXhAvtFqXe5FnoeqfgX5Lxy07TgvMaEImLK8xqjDYqiAQIuv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEzQibBAYdWalvZ8CyrcA0U9J1ejW6gVfcD3hN4u8zhtWCf%2BUqRR6GirXFjVZgUrkub0%2FD2C4v2udDHZFau6G%2BXYO7O1Iv74k4BbAJjtkewbbM6F%2FlhnaGgFK2WAJnj1QB2qt2lfmKedDl6SYlXLYw6kOl0R3fgjsEylxiej8%2BvcJ7sgVkwufr43g7uJUTCiGdij1aXhj4ukU0TN8LUWPt1vMc9nxxUYkt%2BGWrXhpNyhw6%2FcTfyv%2Fc5kHrGxB%2FvqqizsW8JioKBGVa6ZW%2BnukfBRQZ8KD6rfp53NBfaxrSuQlNP4XGjxHCukPrEZIdjhVSyJw%2F4QVoud4fWuTMpHXr9VsR%2F3R%2Bl%2BQI1SOhfEVs0uCOKB8oJVVttAiXjg%2F5r1dOFsJcdwYmki9YxsqbYOISnYtdWjKHioQVBxg6UKUpMu5aHh%2BCBH3ezc933lLYNz1qP70Ktgxk5yJJDoOn%2BoL%2B2d4soXLHNDsHT1T8Kz2Y31F9%2FqfSxl5ZFsOpVw58MJROCHePT3X25IFcYOhr8dAf0MQ97r1lawprPLYw8Gfbpjhw1QsuKaE1OhE1EDPJAeyxx%2FlBqNh8nDKOFlelZppWupL7rZ73%2FRJA%2F0jfePK03mCGvBMuFuUdZAhdWxElAi3o8O0126UfxTiX%2BjMNqa8rwGOqUBp4kxnMUk7VvD8ERhTMnQOhdQvaF2jXz9ZIQYuAGZJUHOMaXQdsioxDWe63VJod0T3RQcyVSS6bTRw1NQjmSYSQvKxFERnl1HbjKmcgRfTWU9zl%2FMVXqJEq4cGpUl6v79vzhyE4czZ3OO10w%2BKuGhMQAUfx1BV0u1wcNYV76lH0pGk%2BTYSCDWbu1pvr2Op7497hSmkwrK9UBBviIrRPyXbGrDqUMw&X-Amz-Signature=3500348c015831104c91e22a6b4814bafb4d7ddd3d14b892351a3d755df6bf34&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662MRJJABY%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T091512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC7C1Ykk2qdB0vmgFUyWB7OAznr2hjB2MDUwh1bGiauDwIgK1fXhAvtFqXe5FnoeqfgX5Lxy07TgvMaEImLK8xqjDYqiAQIuv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEzQibBAYdWalvZ8CyrcA0U9J1ejW6gVfcD3hN4u8zhtWCf%2BUqRR6GirXFjVZgUrkub0%2FD2C4v2udDHZFau6G%2BXYO7O1Iv74k4BbAJjtkewbbM6F%2FlhnaGgFK2WAJnj1QB2qt2lfmKedDl6SYlXLYw6kOl0R3fgjsEylxiej8%2BvcJ7sgVkwufr43g7uJUTCiGdij1aXhj4ukU0TN8LUWPt1vMc9nxxUYkt%2BGWrXhpNyhw6%2FcTfyv%2Fc5kHrGxB%2FvqqizsW8JioKBGVa6ZW%2BnukfBRQZ8KD6rfp53NBfaxrSuQlNP4XGjxHCukPrEZIdjhVSyJw%2F4QVoud4fWuTMpHXr9VsR%2F3R%2Bl%2BQI1SOhfEVs0uCOKB8oJVVttAiXjg%2F5r1dOFsJcdwYmki9YxsqbYOISnYtdWjKHioQVBxg6UKUpMu5aHh%2BCBH3ezc933lLYNz1qP70Ktgxk5yJJDoOn%2BoL%2B2d4soXLHNDsHT1T8Kz2Y31F9%2FqfSxl5ZFsOpVw58MJROCHePT3X25IFcYOhr8dAf0MQ97r1lawprPLYw8Gfbpjhw1QsuKaE1OhE1EDPJAeyxx%2FlBqNh8nDKOFlelZppWupL7rZ73%2FRJA%2F0jfePK03mCGvBMuFuUdZAhdWxElAi3o8O0126UfxTiX%2BjMNqa8rwGOqUBp4kxnMUk7VvD8ERhTMnQOhdQvaF2jXz9ZIQYuAGZJUHOMaXQdsioxDWe63VJod0T3RQcyVSS6bTRw1NQjmSYSQvKxFERnl1HbjKmcgRfTWU9zl%2FMVXqJEq4cGpUl6v79vzhyE4czZ3OO10w%2BKuGhMQAUfx1BV0u1wcNYV76lH0pGk%2BTYSCDWbu1pvr2Op7497hSmkwrK9UBBviIrRPyXbGrDqUMw&X-Amz-Signature=a335c7768c90caf8167446a0ffdd2c3dce3c88d35ba8df9c63ef9b4aa3f37cc8&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
