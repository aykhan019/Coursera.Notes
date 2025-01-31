

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWCVDZGP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDsvEZgRhLQoLvIRAFdISkfiV60dN0D47NrkYz%2BFLcNWgIhAMdWr7Ahm6ZFt5GeXbn3ZWzAFlEdJsVYBQRL9WBI8y5sKogECMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igym752OYPNY5sar34Eq3AMoqFdFcvTjhukUnaaM86mv7lTiQkVFnnzu5tc6SBwcEGmq3eV9pnWHACub4Su4XzYVhBC1mN7xy4TZtZWIs%2B7Fgnz8yTwnd1LB9KCXhL4b1O9Ck1%2BhDqJr8ge3bKTUpvFqquThynjOUFcH%2F5PjJ99EpmJT3v2UhmGDGNaE1owqfwc3ThW6rXA9SxwXrMPn9r35I9CesX7dVE8Z0%2Fdn8%2BISSj8FmDtM%2FrV2%2FAYkgr5ILOrPG2n%2F1ZbSElqrdUwRSfzimcK3D9JAtH25wkjxXvlvWql0VoMPUqTBFYMBxAlJ4bL%2BTAoYlpeKAPVtYlFmsdN6xQgfpTwdR8TGTD9ScSFh7P9ErCQydWwDeOFQ%2BooeKzRS01HGUdiB5mpKcQguM5LI1%2Feq4xQy%2FG3xis%2FmpMPjEBAv5i5TIv2q%2BzUnZLFIwWbSxSsuCME3ExbOGHXrZoFuQpK5Zr90fuefYSmnZf%2BSe%2BBeFNtdr595WLWWMG0jZWEiMvaxXKprtNmIiLekJT51uRF7w1T1ydL5YoyB7%2FyysRnjE4utwvSJcGL214%2Fa7fyRZ%2FN%2F6iQSIUFxogxJOD%2FMbuNYQakN9TfQuHun6zt6aFrtJ0bA6fV06tWzZQ6Qp56TppBkYAnUL7HNWzDB6%2FO8BjqkAbAP%2B02AD8PvNfrs7PBKl6Ggstbs5oWMVI9XE5BfE7ftwDUfz8IvzZ0NrcVZTaUUiU3YH3C6guy6rB%2Bj5PCPK93oDQokl%2FxdBIU0D%2BfRI3hDymNchkHA29dvygecKXwqX44iTwv%2FEGJtVsWDB8YZhTgSaEAVxLtkgypH0%2Bm3OCRooVi0ez96tim%2Bl1j2mnW3vBBOYDM2B%2Bc6f439qPMiKt7mw%2BP8&X-Amz-Signature=5db47edfe5bea6452d5c1bc6575c79a003478f4da3084ff0610ab044e0ca7e4d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWCVDZGP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDsvEZgRhLQoLvIRAFdISkfiV60dN0D47NrkYz%2BFLcNWgIhAMdWr7Ahm6ZFt5GeXbn3ZWzAFlEdJsVYBQRL9WBI8y5sKogECMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igym752OYPNY5sar34Eq3AMoqFdFcvTjhukUnaaM86mv7lTiQkVFnnzu5tc6SBwcEGmq3eV9pnWHACub4Su4XzYVhBC1mN7xy4TZtZWIs%2B7Fgnz8yTwnd1LB9KCXhL4b1O9Ck1%2BhDqJr8ge3bKTUpvFqquThynjOUFcH%2F5PjJ99EpmJT3v2UhmGDGNaE1owqfwc3ThW6rXA9SxwXrMPn9r35I9CesX7dVE8Z0%2Fdn8%2BISSj8FmDtM%2FrV2%2FAYkgr5ILOrPG2n%2F1ZbSElqrdUwRSfzimcK3D9JAtH25wkjxXvlvWql0VoMPUqTBFYMBxAlJ4bL%2BTAoYlpeKAPVtYlFmsdN6xQgfpTwdR8TGTD9ScSFh7P9ErCQydWwDeOFQ%2BooeKzRS01HGUdiB5mpKcQguM5LI1%2Feq4xQy%2FG3xis%2FmpMPjEBAv5i5TIv2q%2BzUnZLFIwWbSxSsuCME3ExbOGHXrZoFuQpK5Zr90fuefYSmnZf%2BSe%2BBeFNtdr595WLWWMG0jZWEiMvaxXKprtNmIiLekJT51uRF7w1T1ydL5YoyB7%2FyysRnjE4utwvSJcGL214%2Fa7fyRZ%2FN%2F6iQSIUFxogxJOD%2FMbuNYQakN9TfQuHun6zt6aFrtJ0bA6fV06tWzZQ6Qp56TppBkYAnUL7HNWzDB6%2FO8BjqkAbAP%2B02AD8PvNfrs7PBKl6Ggstbs5oWMVI9XE5BfE7ftwDUfz8IvzZ0NrcVZTaUUiU3YH3C6guy6rB%2Bj5PCPK93oDQokl%2FxdBIU0D%2BfRI3hDymNchkHA29dvygecKXwqX44iTwv%2FEGJtVsWDB8YZhTgSaEAVxLtkgypH0%2Bm3OCRooVi0ez96tim%2Bl1j2mnW3vBBOYDM2B%2Bc6f439qPMiKt7mw%2BP8&X-Amz-Signature=83c7a73e3642d2ccaa48edd5e2f0da7b77fb0604e703d6ccafd2abfd48c21ba9&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWCVDZGP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDsvEZgRhLQoLvIRAFdISkfiV60dN0D47NrkYz%2BFLcNWgIhAMdWr7Ahm6ZFt5GeXbn3ZWzAFlEdJsVYBQRL9WBI8y5sKogECMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igym752OYPNY5sar34Eq3AMoqFdFcvTjhukUnaaM86mv7lTiQkVFnnzu5tc6SBwcEGmq3eV9pnWHACub4Su4XzYVhBC1mN7xy4TZtZWIs%2B7Fgnz8yTwnd1LB9KCXhL4b1O9Ck1%2BhDqJr8ge3bKTUpvFqquThynjOUFcH%2F5PjJ99EpmJT3v2UhmGDGNaE1owqfwc3ThW6rXA9SxwXrMPn9r35I9CesX7dVE8Z0%2Fdn8%2BISSj8FmDtM%2FrV2%2FAYkgr5ILOrPG2n%2F1ZbSElqrdUwRSfzimcK3D9JAtH25wkjxXvlvWql0VoMPUqTBFYMBxAlJ4bL%2BTAoYlpeKAPVtYlFmsdN6xQgfpTwdR8TGTD9ScSFh7P9ErCQydWwDeOFQ%2BooeKzRS01HGUdiB5mpKcQguM5LI1%2Feq4xQy%2FG3xis%2FmpMPjEBAv5i5TIv2q%2BzUnZLFIwWbSxSsuCME3ExbOGHXrZoFuQpK5Zr90fuefYSmnZf%2BSe%2BBeFNtdr595WLWWMG0jZWEiMvaxXKprtNmIiLekJT51uRF7w1T1ydL5YoyB7%2FyysRnjE4utwvSJcGL214%2Fa7fyRZ%2FN%2F6iQSIUFxogxJOD%2FMbuNYQakN9TfQuHun6zt6aFrtJ0bA6fV06tWzZQ6Qp56TppBkYAnUL7HNWzDB6%2FO8BjqkAbAP%2B02AD8PvNfrs7PBKl6Ggstbs5oWMVI9XE5BfE7ftwDUfz8IvzZ0NrcVZTaUUiU3YH3C6guy6rB%2Bj5PCPK93oDQokl%2FxdBIU0D%2BfRI3hDymNchkHA29dvygecKXwqX44iTwv%2FEGJtVsWDB8YZhTgSaEAVxLtkgypH0%2Bm3OCRooVi0ez96tim%2Bl1j2mnW3vBBOYDM2B%2Bc6f439qPMiKt7mw%2BP8&X-Amz-Signature=27d77ceed0c7911a26bb2b24372ca4366c1a679b9aa73f357492d0133ad438b9&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWCVDZGP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161750Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDsvEZgRhLQoLvIRAFdISkfiV60dN0D47NrkYz%2BFLcNWgIhAMdWr7Ahm6ZFt5GeXbn3ZWzAFlEdJsVYBQRL9WBI8y5sKogECMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igym752OYPNY5sar34Eq3AMoqFdFcvTjhukUnaaM86mv7lTiQkVFnnzu5tc6SBwcEGmq3eV9pnWHACub4Su4XzYVhBC1mN7xy4TZtZWIs%2B7Fgnz8yTwnd1LB9KCXhL4b1O9Ck1%2BhDqJr8ge3bKTUpvFqquThynjOUFcH%2F5PjJ99EpmJT3v2UhmGDGNaE1owqfwc3ThW6rXA9SxwXrMPn9r35I9CesX7dVE8Z0%2Fdn8%2BISSj8FmDtM%2FrV2%2FAYkgr5ILOrPG2n%2F1ZbSElqrdUwRSfzimcK3D9JAtH25wkjxXvlvWql0VoMPUqTBFYMBxAlJ4bL%2BTAoYlpeKAPVtYlFmsdN6xQgfpTwdR8TGTD9ScSFh7P9ErCQydWwDeOFQ%2BooeKzRS01HGUdiB5mpKcQguM5LI1%2Feq4xQy%2FG3xis%2FmpMPjEBAv5i5TIv2q%2BzUnZLFIwWbSxSsuCME3ExbOGHXrZoFuQpK5Zr90fuefYSmnZf%2BSe%2BBeFNtdr595WLWWMG0jZWEiMvaxXKprtNmIiLekJT51uRF7w1T1ydL5YoyB7%2FyysRnjE4utwvSJcGL214%2Fa7fyRZ%2FN%2F6iQSIUFxogxJOD%2FMbuNYQakN9TfQuHun6zt6aFrtJ0bA6fV06tWzZQ6Qp56TppBkYAnUL7HNWzDB6%2FO8BjqkAbAP%2B02AD8PvNfrs7PBKl6Ggstbs5oWMVI9XE5BfE7ftwDUfz8IvzZ0NrcVZTaUUiU3YH3C6guy6rB%2Bj5PCPK93oDQokl%2FxdBIU0D%2BfRI3hDymNchkHA29dvygecKXwqX44iTwv%2FEGJtVsWDB8YZhTgSaEAVxLtkgypH0%2Bm3OCRooVi0ez96tim%2Bl1j2mnW3vBBOYDM2B%2Bc6f439qPMiKt7mw%2BP8&X-Amz-Signature=f8a3299fee3433865be6a815457a9546d109cb2354d5d6dcb251e11af553ae57&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWCVDZGP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161750Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDsvEZgRhLQoLvIRAFdISkfiV60dN0D47NrkYz%2BFLcNWgIhAMdWr7Ahm6ZFt5GeXbn3ZWzAFlEdJsVYBQRL9WBI8y5sKogECMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igym752OYPNY5sar34Eq3AMoqFdFcvTjhukUnaaM86mv7lTiQkVFnnzu5tc6SBwcEGmq3eV9pnWHACub4Su4XzYVhBC1mN7xy4TZtZWIs%2B7Fgnz8yTwnd1LB9KCXhL4b1O9Ck1%2BhDqJr8ge3bKTUpvFqquThynjOUFcH%2F5PjJ99EpmJT3v2UhmGDGNaE1owqfwc3ThW6rXA9SxwXrMPn9r35I9CesX7dVE8Z0%2Fdn8%2BISSj8FmDtM%2FrV2%2FAYkgr5ILOrPG2n%2F1ZbSElqrdUwRSfzimcK3D9JAtH25wkjxXvlvWql0VoMPUqTBFYMBxAlJ4bL%2BTAoYlpeKAPVtYlFmsdN6xQgfpTwdR8TGTD9ScSFh7P9ErCQydWwDeOFQ%2BooeKzRS01HGUdiB5mpKcQguM5LI1%2Feq4xQy%2FG3xis%2FmpMPjEBAv5i5TIv2q%2BzUnZLFIwWbSxSsuCME3ExbOGHXrZoFuQpK5Zr90fuefYSmnZf%2BSe%2BBeFNtdr595WLWWMG0jZWEiMvaxXKprtNmIiLekJT51uRF7w1T1ydL5YoyB7%2FyysRnjE4utwvSJcGL214%2Fa7fyRZ%2FN%2F6iQSIUFxogxJOD%2FMbuNYQakN9TfQuHun6zt6aFrtJ0bA6fV06tWzZQ6Qp56TppBkYAnUL7HNWzDB6%2FO8BjqkAbAP%2B02AD8PvNfrs7PBKl6Ggstbs5oWMVI9XE5BfE7ftwDUfz8IvzZ0NrcVZTaUUiU3YH3C6guy6rB%2Bj5PCPK93oDQokl%2FxdBIU0D%2BfRI3hDymNchkHA29dvygecKXwqX44iTwv%2FEGJtVsWDB8YZhTgSaEAVxLtkgypH0%2Bm3OCRooVi0ez96tim%2Bl1j2mnW3vBBOYDM2B%2Bc6f439qPMiKt7mw%2BP8&X-Amz-Signature=7b90cbbef815ac5cbe9d3cb96c6acf4cdc21d26f114ee08a77bca5c56ab8eff0&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWCVDZGP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161750Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDsvEZgRhLQoLvIRAFdISkfiV60dN0D47NrkYz%2BFLcNWgIhAMdWr7Ahm6ZFt5GeXbn3ZWzAFlEdJsVYBQRL9WBI8y5sKogECMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igym752OYPNY5sar34Eq3AMoqFdFcvTjhukUnaaM86mv7lTiQkVFnnzu5tc6SBwcEGmq3eV9pnWHACub4Su4XzYVhBC1mN7xy4TZtZWIs%2B7Fgnz8yTwnd1LB9KCXhL4b1O9Ck1%2BhDqJr8ge3bKTUpvFqquThynjOUFcH%2F5PjJ99EpmJT3v2UhmGDGNaE1owqfwc3ThW6rXA9SxwXrMPn9r35I9CesX7dVE8Z0%2Fdn8%2BISSj8FmDtM%2FrV2%2FAYkgr5ILOrPG2n%2F1ZbSElqrdUwRSfzimcK3D9JAtH25wkjxXvlvWql0VoMPUqTBFYMBxAlJ4bL%2BTAoYlpeKAPVtYlFmsdN6xQgfpTwdR8TGTD9ScSFh7P9ErCQydWwDeOFQ%2BooeKzRS01HGUdiB5mpKcQguM5LI1%2Feq4xQy%2FG3xis%2FmpMPjEBAv5i5TIv2q%2BzUnZLFIwWbSxSsuCME3ExbOGHXrZoFuQpK5Zr90fuefYSmnZf%2BSe%2BBeFNtdr595WLWWMG0jZWEiMvaxXKprtNmIiLekJT51uRF7w1T1ydL5YoyB7%2FyysRnjE4utwvSJcGL214%2Fa7fyRZ%2FN%2F6iQSIUFxogxJOD%2FMbuNYQakN9TfQuHun6zt6aFrtJ0bA6fV06tWzZQ6Qp56TppBkYAnUL7HNWzDB6%2FO8BjqkAbAP%2B02AD8PvNfrs7PBKl6Ggstbs5oWMVI9XE5BfE7ftwDUfz8IvzZ0NrcVZTaUUiU3YH3C6guy6rB%2Bj5PCPK93oDQokl%2FxdBIU0D%2BfRI3hDymNchkHA29dvygecKXwqX44iTwv%2FEGJtVsWDB8YZhTgSaEAVxLtkgypH0%2Bm3OCRooVi0ez96tim%2Bl1j2mnW3vBBOYDM2B%2Bc6f439qPMiKt7mw%2BP8&X-Amz-Signature=b6ea255442832f2e155d9e3e0272150b0a4e1c9ca79e969a17f6a3291c890fc3&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWCVDZGP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDsvEZgRhLQoLvIRAFdISkfiV60dN0D47NrkYz%2BFLcNWgIhAMdWr7Ahm6ZFt5GeXbn3ZWzAFlEdJsVYBQRL9WBI8y5sKogECMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igym752OYPNY5sar34Eq3AMoqFdFcvTjhukUnaaM86mv7lTiQkVFnnzu5tc6SBwcEGmq3eV9pnWHACub4Su4XzYVhBC1mN7xy4TZtZWIs%2B7Fgnz8yTwnd1LB9KCXhL4b1O9Ck1%2BhDqJr8ge3bKTUpvFqquThynjOUFcH%2F5PjJ99EpmJT3v2UhmGDGNaE1owqfwc3ThW6rXA9SxwXrMPn9r35I9CesX7dVE8Z0%2Fdn8%2BISSj8FmDtM%2FrV2%2FAYkgr5ILOrPG2n%2F1ZbSElqrdUwRSfzimcK3D9JAtH25wkjxXvlvWql0VoMPUqTBFYMBxAlJ4bL%2BTAoYlpeKAPVtYlFmsdN6xQgfpTwdR8TGTD9ScSFh7P9ErCQydWwDeOFQ%2BooeKzRS01HGUdiB5mpKcQguM5LI1%2Feq4xQy%2FG3xis%2FmpMPjEBAv5i5TIv2q%2BzUnZLFIwWbSxSsuCME3ExbOGHXrZoFuQpK5Zr90fuefYSmnZf%2BSe%2BBeFNtdr595WLWWMG0jZWEiMvaxXKprtNmIiLekJT51uRF7w1T1ydL5YoyB7%2FyysRnjE4utwvSJcGL214%2Fa7fyRZ%2FN%2F6iQSIUFxogxJOD%2FMbuNYQakN9TfQuHun6zt6aFrtJ0bA6fV06tWzZQ6Qp56TppBkYAnUL7HNWzDB6%2FO8BjqkAbAP%2B02AD8PvNfrs7PBKl6Ggstbs5oWMVI9XE5BfE7ftwDUfz8IvzZ0NrcVZTaUUiU3YH3C6guy6rB%2Bj5PCPK93oDQokl%2FxdBIU0D%2BfRI3hDymNchkHA29dvygecKXwqX44iTwv%2FEGJtVsWDB8YZhTgSaEAVxLtkgypH0%2Bm3OCRooVi0ez96tim%2Bl1j2mnW3vBBOYDM2B%2Bc6f439qPMiKt7mw%2BP8&X-Amz-Signature=3970f69a11f0871129e1515de8b51e3b956cd820aff18939791193ec6fca8c36&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWCVDZGP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDsvEZgRhLQoLvIRAFdISkfiV60dN0D47NrkYz%2BFLcNWgIhAMdWr7Ahm6ZFt5GeXbn3ZWzAFlEdJsVYBQRL9WBI8y5sKogECMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igym752OYPNY5sar34Eq3AMoqFdFcvTjhukUnaaM86mv7lTiQkVFnnzu5tc6SBwcEGmq3eV9pnWHACub4Su4XzYVhBC1mN7xy4TZtZWIs%2B7Fgnz8yTwnd1LB9KCXhL4b1O9Ck1%2BhDqJr8ge3bKTUpvFqquThynjOUFcH%2F5PjJ99EpmJT3v2UhmGDGNaE1owqfwc3ThW6rXA9SxwXrMPn9r35I9CesX7dVE8Z0%2Fdn8%2BISSj8FmDtM%2FrV2%2FAYkgr5ILOrPG2n%2F1ZbSElqrdUwRSfzimcK3D9JAtH25wkjxXvlvWql0VoMPUqTBFYMBxAlJ4bL%2BTAoYlpeKAPVtYlFmsdN6xQgfpTwdR8TGTD9ScSFh7P9ErCQydWwDeOFQ%2BooeKzRS01HGUdiB5mpKcQguM5LI1%2Feq4xQy%2FG3xis%2FmpMPjEBAv5i5TIv2q%2BzUnZLFIwWbSxSsuCME3ExbOGHXrZoFuQpK5Zr90fuefYSmnZf%2BSe%2BBeFNtdr595WLWWMG0jZWEiMvaxXKprtNmIiLekJT51uRF7w1T1ydL5YoyB7%2FyysRnjE4utwvSJcGL214%2Fa7fyRZ%2FN%2F6iQSIUFxogxJOD%2FMbuNYQakN9TfQuHun6zt6aFrtJ0bA6fV06tWzZQ6Qp56TppBkYAnUL7HNWzDB6%2FO8BjqkAbAP%2B02AD8PvNfrs7PBKl6Ggstbs5oWMVI9XE5BfE7ftwDUfz8IvzZ0NrcVZTaUUiU3YH3C6guy6rB%2Bj5PCPK93oDQokl%2FxdBIU0D%2BfRI3hDymNchkHA29dvygecKXwqX44iTwv%2FEGJtVsWDB8YZhTgSaEAVxLtkgypH0%2Bm3OCRooVi0ez96tim%2Bl1j2mnW3vBBOYDM2B%2Bc6f439qPMiKt7mw%2BP8&X-Amz-Signature=ecb9b3123835ead3234cbad304b5c6b38e32a86690e3ea3fc6b61bb2c2185c0a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWCVDZGP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDsvEZgRhLQoLvIRAFdISkfiV60dN0D47NrkYz%2BFLcNWgIhAMdWr7Ahm6ZFt5GeXbn3ZWzAFlEdJsVYBQRL9WBI8y5sKogECMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igym752OYPNY5sar34Eq3AMoqFdFcvTjhukUnaaM86mv7lTiQkVFnnzu5tc6SBwcEGmq3eV9pnWHACub4Su4XzYVhBC1mN7xy4TZtZWIs%2B7Fgnz8yTwnd1LB9KCXhL4b1O9Ck1%2BhDqJr8ge3bKTUpvFqquThynjOUFcH%2F5PjJ99EpmJT3v2UhmGDGNaE1owqfwc3ThW6rXA9SxwXrMPn9r35I9CesX7dVE8Z0%2Fdn8%2BISSj8FmDtM%2FrV2%2FAYkgr5ILOrPG2n%2F1ZbSElqrdUwRSfzimcK3D9JAtH25wkjxXvlvWql0VoMPUqTBFYMBxAlJ4bL%2BTAoYlpeKAPVtYlFmsdN6xQgfpTwdR8TGTD9ScSFh7P9ErCQydWwDeOFQ%2BooeKzRS01HGUdiB5mpKcQguM5LI1%2Feq4xQy%2FG3xis%2FmpMPjEBAv5i5TIv2q%2BzUnZLFIwWbSxSsuCME3ExbOGHXrZoFuQpK5Zr90fuefYSmnZf%2BSe%2BBeFNtdr595WLWWMG0jZWEiMvaxXKprtNmIiLekJT51uRF7w1T1ydL5YoyB7%2FyysRnjE4utwvSJcGL214%2Fa7fyRZ%2FN%2F6iQSIUFxogxJOD%2FMbuNYQakN9TfQuHun6zt6aFrtJ0bA6fV06tWzZQ6Qp56TppBkYAnUL7HNWzDB6%2FO8BjqkAbAP%2B02AD8PvNfrs7PBKl6Ggstbs5oWMVI9XE5BfE7ftwDUfz8IvzZ0NrcVZTaUUiU3YH3C6guy6rB%2Bj5PCPK93oDQokl%2FxdBIU0D%2BfRI3hDymNchkHA29dvygecKXwqX44iTwv%2FEGJtVsWDB8YZhTgSaEAVxLtkgypH0%2Bm3OCRooVi0ez96tim%2Bl1j2mnW3vBBOYDM2B%2Bc6f439qPMiKt7mw%2BP8&X-Amz-Signature=e60ece6131512b4504f54ce4c872b2698f5149fc619266ace057f08e74bcc1c2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46665OEWFLZ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCH59geOcNgXJVaeYSZLayIGmcMg0E54wQ1YVke7ggfxAIgO9rwRfnalfDmAanRchxUnultFR9LNkx0nhfXFxdam4EqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDW8dlnuKcbQCJeHIyrcA8P9gQxVXdcFtiOK6s7Ct%2B8aSu5SfqN%2FgZjwx2Sq4bxoNyOswD6zy8k68mP35uXjIt%2FC1%2FbgazpbEMPCOPiUJZBz2UwSg6MNsfZi49FKCQ4qU3MsjR1HbwaCEj%2F1JgL8xjTcNMczFSOgde4ug2KEdXtNkTn2ecjJbXc%2B%2F8zncl7W3lPKQvQF7JmQmP%2FXpLs5cb%2FF8ahN8yxkT%2FgU4vAYI8fGvCw1J%2F9iCpEYZRp2bW3l4g0crDWyplRSJwvYII3r%2Bo%2FRHOP8e%2Ff6Jrx7WhQ%2BOZa19wf%2FJknNHVpMwkoxdb%2BouoeCQ9fOpvrk4zKJ5xYnV7jPa05Omlo8KQ7Zf3fB40hXfiHzys6HUXD9jJiQJKH%2FIUt0y6hannS7ClxIW9R7c10Pqo74LgFSqhI%2FIVR%2FZ1dl%2BAPBnsLq%2FKKE0YzEUIaX%2FLZK5qkrf2bnmwlK6ttzK4C6PRvDIHqXJ8DDpNKo0Jz%2FyGYNvmOZhqAYZbHlscr2TGhQBHG%2Fh9gi9KnkivktrhnD4Ue6aH270aTVFmn1TkeMa%2Fm9%2FUsgCnT2kkWCbplI%2FbdRo8ur9aNLZWSHqK4DINqDPhgoyvLaUdhJOYFUwUx7GEDCEkuxNHUE6R9CrHfSR0lHNaaxEZROWJbdMJfr87wGOqUBOu5sXgBats5q%2BQij7d%2BYEaSb0P3OVpNA3GvVaSzWaWAnTldFMiWrj6iOoLW59I%2BKZ7XqPhuojKqgrn7VGpQ9JFpegw4j5V%2BaTF51qLa1CE4X%2BA8PKPJcbZJzMncfb%2FTiJEaeUB%2FoKApDsfvixxifM7s7qva0%2Bbm0vOfd%2FYPHKAfsVqOCVLpe0BA2LNMSntQQikc4NfoQxZ9gB%2F73VROLGC0Qe0oj&X-Amz-Signature=0db3da146bf6acb91998eb7f5875759208e4b5ae276796dc33ece7730189897f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46665OEWFLZ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCH59geOcNgXJVaeYSZLayIGmcMg0E54wQ1YVke7ggfxAIgO9rwRfnalfDmAanRchxUnultFR9LNkx0nhfXFxdam4EqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDW8dlnuKcbQCJeHIyrcA8P9gQxVXdcFtiOK6s7Ct%2B8aSu5SfqN%2FgZjwx2Sq4bxoNyOswD6zy8k68mP35uXjIt%2FC1%2FbgazpbEMPCOPiUJZBz2UwSg6MNsfZi49FKCQ4qU3MsjR1HbwaCEj%2F1JgL8xjTcNMczFSOgde4ug2KEdXtNkTn2ecjJbXc%2B%2F8zncl7W3lPKQvQF7JmQmP%2FXpLs5cb%2FF8ahN8yxkT%2FgU4vAYI8fGvCw1J%2F9iCpEYZRp2bW3l4g0crDWyplRSJwvYII3r%2Bo%2FRHOP8e%2Ff6Jrx7WhQ%2BOZa19wf%2FJknNHVpMwkoxdb%2BouoeCQ9fOpvrk4zKJ5xYnV7jPa05Omlo8KQ7Zf3fB40hXfiHzys6HUXD9jJiQJKH%2FIUt0y6hannS7ClxIW9R7c10Pqo74LgFSqhI%2FIVR%2FZ1dl%2BAPBnsLq%2FKKE0YzEUIaX%2FLZK5qkrf2bnmwlK6ttzK4C6PRvDIHqXJ8DDpNKo0Jz%2FyGYNvmOZhqAYZbHlscr2TGhQBHG%2Fh9gi9KnkivktrhnD4Ue6aH270aTVFmn1TkeMa%2Fm9%2FUsgCnT2kkWCbplI%2FbdRo8ur9aNLZWSHqK4DINqDPhgoyvLaUdhJOYFUwUx7GEDCEkuxNHUE6R9CrHfSR0lHNaaxEZROWJbdMJfr87wGOqUBOu5sXgBats5q%2BQij7d%2BYEaSb0P3OVpNA3GvVaSzWaWAnTldFMiWrj6iOoLW59I%2BKZ7XqPhuojKqgrn7VGpQ9JFpegw4j5V%2BaTF51qLa1CE4X%2BA8PKPJcbZJzMncfb%2FTiJEaeUB%2FoKApDsfvixxifM7s7qva0%2Bbm0vOfd%2FYPHKAfsVqOCVLpe0BA2LNMSntQQikc4NfoQxZ9gB%2F73VROLGC0Qe0oj&X-Amz-Signature=b06f2aaea2f2eadc5fcf68f0c727d0cae189bd999050e1f1fe5f653779a491f5&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
