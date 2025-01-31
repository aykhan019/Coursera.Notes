

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ATT4GJZ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIATu0Mt5BTIoeo8L71TUb45c5xYcVeCPvYlLrPvx4EBaAiByorWImhvedy8%2B9Q%2FSc9GraGk9VKPcZto7g4tSV7SRzyqIBAjA%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNbAIkVG6lvszj89mKtwDR7TgTDkwrdtIy0ZQMAqyZGppLHIzSZmFRZ%2BaYPleyl%2BS5o4UZD%2BnY0Pq6DDKYjEuudnAW0mh63iYSx%2FlKiOQd%2FC%2FZTaLX4GWO4FL3B6jrKrW5AaIWj%2FVzenLg%2B40U1%2BIC9QLVUhldJdneuF6cnGh4tW%2Fz9332jt0PBn4mSL5SoFHyHqauHi8KP6kiHEp0UdfrqsG7Q1E45A9I67ktnZUwPXiyCmmO8UZMa5muY1%2FQIE1mLdT6gQokL2sZN35bL9Y78rfXQYAUT5oXx55i%2F279NDtFTDmt9xOvJVHjyEZOAVGRrL5Pc57nW1uKTB75KUlWk4Ewp7lfgq9%2FE4XcVQEX8JK8k2wn4afZYhocYEam7r7FzJO%2BsPt%2FH9BfydyKq0fLuEscWkexU4hmheavyTnSw%2B8NQh4pderbWo6fa%2B5D94gs4%2BOIB3kK2uiosem2A8bx6X%2F87PPpuYjPspmDSfLlP2wFeZ35ZjOUWr6Gkbd0y92HbMAFaO54EQekXOZmf7CVgLFj9NdbZ96K8B%2F%2FU2pbZ%2F8pt8Ec2l%2BNFD7vAR%2FrdlVXPwSDNKVSoYmBO5Zv2BZzMg9jc%2FLj%2FKqDgnhIkKnXzbI%2FCFm9KloE0y%2BKHhjm06rlbuBph%2FDdXGL2BMwisjzvAY6pgFNVkca%2BUUWw3hcSJFRfk1pxekT%2Bz7XhdA664PtGSTjLEkz%2BRSDEdlDhm%2FfoE%2FLeUqpw9U7gf9cH9eeGgtlVjQGknaXdvfmA%2FvpP32JseHUCzubYNZK1ogexMDPKtOgqsyRvebxyTobOsWf9oD%2FYhoLVOnZEkyLfCa6I8VSb065QWzBJes6oLyE3YGEyQYiAx9mF9X75rNPt2zT4kbhaxPSgLlmOQxT&X-Amz-Signature=015948b16e0a17769dbd98a7d5139a452e07e09d2fa2b2e476416096840c1c9c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ATT4GJZ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIATu0Mt5BTIoeo8L71TUb45c5xYcVeCPvYlLrPvx4EBaAiByorWImhvedy8%2B9Q%2FSc9GraGk9VKPcZto7g4tSV7SRzyqIBAjA%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNbAIkVG6lvszj89mKtwDR7TgTDkwrdtIy0ZQMAqyZGppLHIzSZmFRZ%2BaYPleyl%2BS5o4UZD%2BnY0Pq6DDKYjEuudnAW0mh63iYSx%2FlKiOQd%2FC%2FZTaLX4GWO4FL3B6jrKrW5AaIWj%2FVzenLg%2B40U1%2BIC9QLVUhldJdneuF6cnGh4tW%2Fz9332jt0PBn4mSL5SoFHyHqauHi8KP6kiHEp0UdfrqsG7Q1E45A9I67ktnZUwPXiyCmmO8UZMa5muY1%2FQIE1mLdT6gQokL2sZN35bL9Y78rfXQYAUT5oXx55i%2F279NDtFTDmt9xOvJVHjyEZOAVGRrL5Pc57nW1uKTB75KUlWk4Ewp7lfgq9%2FE4XcVQEX8JK8k2wn4afZYhocYEam7r7FzJO%2BsPt%2FH9BfydyKq0fLuEscWkexU4hmheavyTnSw%2B8NQh4pderbWo6fa%2B5D94gs4%2BOIB3kK2uiosem2A8bx6X%2F87PPpuYjPspmDSfLlP2wFeZ35ZjOUWr6Gkbd0y92HbMAFaO54EQekXOZmf7CVgLFj9NdbZ96K8B%2F%2FU2pbZ%2F8pt8Ec2l%2BNFD7vAR%2FrdlVXPwSDNKVSoYmBO5Zv2BZzMg9jc%2FLj%2FKqDgnhIkKnXzbI%2FCFm9KloE0y%2BKHhjm06rlbuBph%2FDdXGL2BMwisjzvAY6pgFNVkca%2BUUWw3hcSJFRfk1pxekT%2Bz7XhdA664PtGSTjLEkz%2BRSDEdlDhm%2FfoE%2FLeUqpw9U7gf9cH9eeGgtlVjQGknaXdvfmA%2FvpP32JseHUCzubYNZK1ogexMDPKtOgqsyRvebxyTobOsWf9oD%2FYhoLVOnZEkyLfCa6I8VSb065QWzBJes6oLyE3YGEyQYiAx9mF9X75rNPt2zT4kbhaxPSgLlmOQxT&X-Amz-Signature=432c4a60eb9ad976f4e41c4f18cd158bdd4c624be2e9c7a8262b42769b3a0e28&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ATT4GJZ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIATu0Mt5BTIoeo8L71TUb45c5xYcVeCPvYlLrPvx4EBaAiByorWImhvedy8%2B9Q%2FSc9GraGk9VKPcZto7g4tSV7SRzyqIBAjA%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNbAIkVG6lvszj89mKtwDR7TgTDkwrdtIy0ZQMAqyZGppLHIzSZmFRZ%2BaYPleyl%2BS5o4UZD%2BnY0Pq6DDKYjEuudnAW0mh63iYSx%2FlKiOQd%2FC%2FZTaLX4GWO4FL3B6jrKrW5AaIWj%2FVzenLg%2B40U1%2BIC9QLVUhldJdneuF6cnGh4tW%2Fz9332jt0PBn4mSL5SoFHyHqauHi8KP6kiHEp0UdfrqsG7Q1E45A9I67ktnZUwPXiyCmmO8UZMa5muY1%2FQIE1mLdT6gQokL2sZN35bL9Y78rfXQYAUT5oXx55i%2F279NDtFTDmt9xOvJVHjyEZOAVGRrL5Pc57nW1uKTB75KUlWk4Ewp7lfgq9%2FE4XcVQEX8JK8k2wn4afZYhocYEam7r7FzJO%2BsPt%2FH9BfydyKq0fLuEscWkexU4hmheavyTnSw%2B8NQh4pderbWo6fa%2B5D94gs4%2BOIB3kK2uiosem2A8bx6X%2F87PPpuYjPspmDSfLlP2wFeZ35ZjOUWr6Gkbd0y92HbMAFaO54EQekXOZmf7CVgLFj9NdbZ96K8B%2F%2FU2pbZ%2F8pt8Ec2l%2BNFD7vAR%2FrdlVXPwSDNKVSoYmBO5Zv2BZzMg9jc%2FLj%2FKqDgnhIkKnXzbI%2FCFm9KloE0y%2BKHhjm06rlbuBph%2FDdXGL2BMwisjzvAY6pgFNVkca%2BUUWw3hcSJFRfk1pxekT%2Bz7XhdA664PtGSTjLEkz%2BRSDEdlDhm%2FfoE%2FLeUqpw9U7gf9cH9eeGgtlVjQGknaXdvfmA%2FvpP32JseHUCzubYNZK1ogexMDPKtOgqsyRvebxyTobOsWf9oD%2FYhoLVOnZEkyLfCa6I8VSb065QWzBJes6oLyE3YGEyQYiAx9mF9X75rNPt2zT4kbhaxPSgLlmOQxT&X-Amz-Signature=34b7c972ec66d1dcf9c959fad32da16ab0c46c801c07060f3ae75cddd71c99ed&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ATT4GJZ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIATu0Mt5BTIoeo8L71TUb45c5xYcVeCPvYlLrPvx4EBaAiByorWImhvedy8%2B9Q%2FSc9GraGk9VKPcZto7g4tSV7SRzyqIBAjA%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNbAIkVG6lvszj89mKtwDR7TgTDkwrdtIy0ZQMAqyZGppLHIzSZmFRZ%2BaYPleyl%2BS5o4UZD%2BnY0Pq6DDKYjEuudnAW0mh63iYSx%2FlKiOQd%2FC%2FZTaLX4GWO4FL3B6jrKrW5AaIWj%2FVzenLg%2B40U1%2BIC9QLVUhldJdneuF6cnGh4tW%2Fz9332jt0PBn4mSL5SoFHyHqauHi8KP6kiHEp0UdfrqsG7Q1E45A9I67ktnZUwPXiyCmmO8UZMa5muY1%2FQIE1mLdT6gQokL2sZN35bL9Y78rfXQYAUT5oXx55i%2F279NDtFTDmt9xOvJVHjyEZOAVGRrL5Pc57nW1uKTB75KUlWk4Ewp7lfgq9%2FE4XcVQEX8JK8k2wn4afZYhocYEam7r7FzJO%2BsPt%2FH9BfydyKq0fLuEscWkexU4hmheavyTnSw%2B8NQh4pderbWo6fa%2B5D94gs4%2BOIB3kK2uiosem2A8bx6X%2F87PPpuYjPspmDSfLlP2wFeZ35ZjOUWr6Gkbd0y92HbMAFaO54EQekXOZmf7CVgLFj9NdbZ96K8B%2F%2FU2pbZ%2F8pt8Ec2l%2BNFD7vAR%2FrdlVXPwSDNKVSoYmBO5Zv2BZzMg9jc%2FLj%2FKqDgnhIkKnXzbI%2FCFm9KloE0y%2BKHhjm06rlbuBph%2FDdXGL2BMwisjzvAY6pgFNVkca%2BUUWw3hcSJFRfk1pxekT%2Bz7XhdA664PtGSTjLEkz%2BRSDEdlDhm%2FfoE%2FLeUqpw9U7gf9cH9eeGgtlVjQGknaXdvfmA%2FvpP32JseHUCzubYNZK1ogexMDPKtOgqsyRvebxyTobOsWf9oD%2FYhoLVOnZEkyLfCa6I8VSb065QWzBJes6oLyE3YGEyQYiAx9mF9X75rNPt2zT4kbhaxPSgLlmOQxT&X-Amz-Signature=e3067ebae9b105715ff5a97dc2869ed6bdff8892a62d95a80dd663f11cefe2e2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ATT4GJZ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIATu0Mt5BTIoeo8L71TUb45c5xYcVeCPvYlLrPvx4EBaAiByorWImhvedy8%2B9Q%2FSc9GraGk9VKPcZto7g4tSV7SRzyqIBAjA%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNbAIkVG6lvszj89mKtwDR7TgTDkwrdtIy0ZQMAqyZGppLHIzSZmFRZ%2BaYPleyl%2BS5o4UZD%2BnY0Pq6DDKYjEuudnAW0mh63iYSx%2FlKiOQd%2FC%2FZTaLX4GWO4FL3B6jrKrW5AaIWj%2FVzenLg%2B40U1%2BIC9QLVUhldJdneuF6cnGh4tW%2Fz9332jt0PBn4mSL5SoFHyHqauHi8KP6kiHEp0UdfrqsG7Q1E45A9I67ktnZUwPXiyCmmO8UZMa5muY1%2FQIE1mLdT6gQokL2sZN35bL9Y78rfXQYAUT5oXx55i%2F279NDtFTDmt9xOvJVHjyEZOAVGRrL5Pc57nW1uKTB75KUlWk4Ewp7lfgq9%2FE4XcVQEX8JK8k2wn4afZYhocYEam7r7FzJO%2BsPt%2FH9BfydyKq0fLuEscWkexU4hmheavyTnSw%2B8NQh4pderbWo6fa%2B5D94gs4%2BOIB3kK2uiosem2A8bx6X%2F87PPpuYjPspmDSfLlP2wFeZ35ZjOUWr6Gkbd0y92HbMAFaO54EQekXOZmf7CVgLFj9NdbZ96K8B%2F%2FU2pbZ%2F8pt8Ec2l%2BNFD7vAR%2FrdlVXPwSDNKVSoYmBO5Zv2BZzMg9jc%2FLj%2FKqDgnhIkKnXzbI%2FCFm9KloE0y%2BKHhjm06rlbuBph%2FDdXGL2BMwisjzvAY6pgFNVkca%2BUUWw3hcSJFRfk1pxekT%2Bz7XhdA664PtGSTjLEkz%2BRSDEdlDhm%2FfoE%2FLeUqpw9U7gf9cH9eeGgtlVjQGknaXdvfmA%2FvpP32JseHUCzubYNZK1ogexMDPKtOgqsyRvebxyTobOsWf9oD%2FYhoLVOnZEkyLfCa6I8VSb065QWzBJes6oLyE3YGEyQYiAx9mF9X75rNPt2zT4kbhaxPSgLlmOQxT&X-Amz-Signature=a0b31307827973c40a4e2db1e3d75a6c292952ea5cc740bad9dc8d794a088108&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ATT4GJZ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIATu0Mt5BTIoeo8L71TUb45c5xYcVeCPvYlLrPvx4EBaAiByorWImhvedy8%2B9Q%2FSc9GraGk9VKPcZto7g4tSV7SRzyqIBAjA%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNbAIkVG6lvszj89mKtwDR7TgTDkwrdtIy0ZQMAqyZGppLHIzSZmFRZ%2BaYPleyl%2BS5o4UZD%2BnY0Pq6DDKYjEuudnAW0mh63iYSx%2FlKiOQd%2FC%2FZTaLX4GWO4FL3B6jrKrW5AaIWj%2FVzenLg%2B40U1%2BIC9QLVUhldJdneuF6cnGh4tW%2Fz9332jt0PBn4mSL5SoFHyHqauHi8KP6kiHEp0UdfrqsG7Q1E45A9I67ktnZUwPXiyCmmO8UZMa5muY1%2FQIE1mLdT6gQokL2sZN35bL9Y78rfXQYAUT5oXx55i%2F279NDtFTDmt9xOvJVHjyEZOAVGRrL5Pc57nW1uKTB75KUlWk4Ewp7lfgq9%2FE4XcVQEX8JK8k2wn4afZYhocYEam7r7FzJO%2BsPt%2FH9BfydyKq0fLuEscWkexU4hmheavyTnSw%2B8NQh4pderbWo6fa%2B5D94gs4%2BOIB3kK2uiosem2A8bx6X%2F87PPpuYjPspmDSfLlP2wFeZ35ZjOUWr6Gkbd0y92HbMAFaO54EQekXOZmf7CVgLFj9NdbZ96K8B%2F%2FU2pbZ%2F8pt8Ec2l%2BNFD7vAR%2FrdlVXPwSDNKVSoYmBO5Zv2BZzMg9jc%2FLj%2FKqDgnhIkKnXzbI%2FCFm9KloE0y%2BKHhjm06rlbuBph%2FDdXGL2BMwisjzvAY6pgFNVkca%2BUUWw3hcSJFRfk1pxekT%2Bz7XhdA664PtGSTjLEkz%2BRSDEdlDhm%2FfoE%2FLeUqpw9U7gf9cH9eeGgtlVjQGknaXdvfmA%2FvpP32JseHUCzubYNZK1ogexMDPKtOgqsyRvebxyTobOsWf9oD%2FYhoLVOnZEkyLfCa6I8VSb065QWzBJes6oLyE3YGEyQYiAx9mF9X75rNPt2zT4kbhaxPSgLlmOQxT&X-Amz-Signature=de983643595d34c1f02471f05780f87aea9df9616a5df4d570777e2f6c7fd19a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ATT4GJZ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIATu0Mt5BTIoeo8L71TUb45c5xYcVeCPvYlLrPvx4EBaAiByorWImhvedy8%2B9Q%2FSc9GraGk9VKPcZto7g4tSV7SRzyqIBAjA%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNbAIkVG6lvszj89mKtwDR7TgTDkwrdtIy0ZQMAqyZGppLHIzSZmFRZ%2BaYPleyl%2BS5o4UZD%2BnY0Pq6DDKYjEuudnAW0mh63iYSx%2FlKiOQd%2FC%2FZTaLX4GWO4FL3B6jrKrW5AaIWj%2FVzenLg%2B40U1%2BIC9QLVUhldJdneuF6cnGh4tW%2Fz9332jt0PBn4mSL5SoFHyHqauHi8KP6kiHEp0UdfrqsG7Q1E45A9I67ktnZUwPXiyCmmO8UZMa5muY1%2FQIE1mLdT6gQokL2sZN35bL9Y78rfXQYAUT5oXx55i%2F279NDtFTDmt9xOvJVHjyEZOAVGRrL5Pc57nW1uKTB75KUlWk4Ewp7lfgq9%2FE4XcVQEX8JK8k2wn4afZYhocYEam7r7FzJO%2BsPt%2FH9BfydyKq0fLuEscWkexU4hmheavyTnSw%2B8NQh4pderbWo6fa%2B5D94gs4%2BOIB3kK2uiosem2A8bx6X%2F87PPpuYjPspmDSfLlP2wFeZ35ZjOUWr6Gkbd0y92HbMAFaO54EQekXOZmf7CVgLFj9NdbZ96K8B%2F%2FU2pbZ%2F8pt8Ec2l%2BNFD7vAR%2FrdlVXPwSDNKVSoYmBO5Zv2BZzMg9jc%2FLj%2FKqDgnhIkKnXzbI%2FCFm9KloE0y%2BKHhjm06rlbuBph%2FDdXGL2BMwisjzvAY6pgFNVkca%2BUUWw3hcSJFRfk1pxekT%2Bz7XhdA664PtGSTjLEkz%2BRSDEdlDhm%2FfoE%2FLeUqpw9U7gf9cH9eeGgtlVjQGknaXdvfmA%2FvpP32JseHUCzubYNZK1ogexMDPKtOgqsyRvebxyTobOsWf9oD%2FYhoLVOnZEkyLfCa6I8VSb065QWzBJes6oLyE3YGEyQYiAx9mF9X75rNPt2zT4kbhaxPSgLlmOQxT&X-Amz-Signature=2b6c71135b2deb64d6d78b0e5545009194f932c2adb9d606ab51b73e2055db61&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ATT4GJZ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIATu0Mt5BTIoeo8L71TUb45c5xYcVeCPvYlLrPvx4EBaAiByorWImhvedy8%2B9Q%2FSc9GraGk9VKPcZto7g4tSV7SRzyqIBAjA%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNbAIkVG6lvszj89mKtwDR7TgTDkwrdtIy0ZQMAqyZGppLHIzSZmFRZ%2BaYPleyl%2BS5o4UZD%2BnY0Pq6DDKYjEuudnAW0mh63iYSx%2FlKiOQd%2FC%2FZTaLX4GWO4FL3B6jrKrW5AaIWj%2FVzenLg%2B40U1%2BIC9QLVUhldJdneuF6cnGh4tW%2Fz9332jt0PBn4mSL5SoFHyHqauHi8KP6kiHEp0UdfrqsG7Q1E45A9I67ktnZUwPXiyCmmO8UZMa5muY1%2FQIE1mLdT6gQokL2sZN35bL9Y78rfXQYAUT5oXx55i%2F279NDtFTDmt9xOvJVHjyEZOAVGRrL5Pc57nW1uKTB75KUlWk4Ewp7lfgq9%2FE4XcVQEX8JK8k2wn4afZYhocYEam7r7FzJO%2BsPt%2FH9BfydyKq0fLuEscWkexU4hmheavyTnSw%2B8NQh4pderbWo6fa%2B5D94gs4%2BOIB3kK2uiosem2A8bx6X%2F87PPpuYjPspmDSfLlP2wFeZ35ZjOUWr6Gkbd0y92HbMAFaO54EQekXOZmf7CVgLFj9NdbZ96K8B%2F%2FU2pbZ%2F8pt8Ec2l%2BNFD7vAR%2FrdlVXPwSDNKVSoYmBO5Zv2BZzMg9jc%2FLj%2FKqDgnhIkKnXzbI%2FCFm9KloE0y%2BKHhjm06rlbuBph%2FDdXGL2BMwisjzvAY6pgFNVkca%2BUUWw3hcSJFRfk1pxekT%2Bz7XhdA664PtGSTjLEkz%2BRSDEdlDhm%2FfoE%2FLeUqpw9U7gf9cH9eeGgtlVjQGknaXdvfmA%2FvpP32JseHUCzubYNZK1ogexMDPKtOgqsyRvebxyTobOsWf9oD%2FYhoLVOnZEkyLfCa6I8VSb065QWzBJes6oLyE3YGEyQYiAx9mF9X75rNPt2zT4kbhaxPSgLlmOQxT&X-Amz-Signature=24d8efae471cd36ec07f50457b6b1c5fa738c4b42f76c4535cd637732d74bc7b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ATT4GJZ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIATu0Mt5BTIoeo8L71TUb45c5xYcVeCPvYlLrPvx4EBaAiByorWImhvedy8%2B9Q%2FSc9GraGk9VKPcZto7g4tSV7SRzyqIBAjA%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNbAIkVG6lvszj89mKtwDR7TgTDkwrdtIy0ZQMAqyZGppLHIzSZmFRZ%2BaYPleyl%2BS5o4UZD%2BnY0Pq6DDKYjEuudnAW0mh63iYSx%2FlKiOQd%2FC%2FZTaLX4GWO4FL3B6jrKrW5AaIWj%2FVzenLg%2B40U1%2BIC9QLVUhldJdneuF6cnGh4tW%2Fz9332jt0PBn4mSL5SoFHyHqauHi8KP6kiHEp0UdfrqsG7Q1E45A9I67ktnZUwPXiyCmmO8UZMa5muY1%2FQIE1mLdT6gQokL2sZN35bL9Y78rfXQYAUT5oXx55i%2F279NDtFTDmt9xOvJVHjyEZOAVGRrL5Pc57nW1uKTB75KUlWk4Ewp7lfgq9%2FE4XcVQEX8JK8k2wn4afZYhocYEam7r7FzJO%2BsPt%2FH9BfydyKq0fLuEscWkexU4hmheavyTnSw%2B8NQh4pderbWo6fa%2B5D94gs4%2BOIB3kK2uiosem2A8bx6X%2F87PPpuYjPspmDSfLlP2wFeZ35ZjOUWr6Gkbd0y92HbMAFaO54EQekXOZmf7CVgLFj9NdbZ96K8B%2F%2FU2pbZ%2F8pt8Ec2l%2BNFD7vAR%2FrdlVXPwSDNKVSoYmBO5Zv2BZzMg9jc%2FLj%2FKqDgnhIkKnXzbI%2FCFm9KloE0y%2BKHhjm06rlbuBph%2FDdXGL2BMwisjzvAY6pgFNVkca%2BUUWw3hcSJFRfk1pxekT%2Bz7XhdA664PtGSTjLEkz%2BRSDEdlDhm%2FfoE%2FLeUqpw9U7gf9cH9eeGgtlVjQGknaXdvfmA%2FvpP32JseHUCzubYNZK1ogexMDPKtOgqsyRvebxyTobOsWf9oD%2FYhoLVOnZEkyLfCa6I8VSb065QWzBJes6oLyE3YGEyQYiAx9mF9X75rNPt2zT4kbhaxPSgLlmOQxT&X-Amz-Signature=f861ab770895845e37f4c99c0720974fdc521691885fc150eec2f764dfab63f7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNEKLXI4%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHfCIOrmXgk%2FGr%2Fmr4zci%2FheVSxMKOkAzMxvMSin7hhpAiA62zNyySHGQmEnT1txv4fBg51NGczpb%2BHM%2FOQS6I0T8SqIBAjA%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZPfPobJlDolNDFsTKtwDDaTEb%2BS35CRqQLKExG%2BDgbNbZguzZjIs5QHuIr6PcDGmBmCitTaBs99BIcvynpUJ0BSEJNtDUvudadyqFu1EHKOr%2FQHdFhspVx7gvI%2FmM%2Ff2NY1Atn9xWYmJ9wKeK3exG%2F%2F3sjZmkqdcs4coLhV6W10Np%2Fz0kOL2HWtHXO43Fr36x76hyMXsyIls2QgsFMITuNciaZUwWLkWwSbLhwzxY6Z9h68JV8MaLFsrq53nHGexqBPMCklXQWR1qfk7JSDBRVeaRNfOW%2FJ3SMS6uDI8t4jm3wIZSCHYsvhob3EDipdCMdjqajNYoj%2FcQtNsAlrskfxrHFNDnA3QHkIRjM39PSkqSwzDmdZfI9dGcjoGT%2FZkeDbuUY%2BVktg9h%2BrZnIt03dv2ApcYrccZfPctd1RW%2F1C1JPFd%2BsM26GihQyg9HBVyLh1qyXKkcRjQgiPsgmzElCPStITlKHq%2FFsZaqM4kLQD3b5WId3G9lUs%2BF1TAGLdLKK%2BnGpAsnY6ddfuuapBQJY9FMZGuk8tS4vxXFw8vETuM4409ZwDlMe9yLc7XcI6Lh603vVOT8LiB5L%2B3%2FgBKrP%2BjRA%2FmT1mMYyQ%2FO7rHxL6j25inhGFaG8NTFA75RXtwOVxJKNL9HYomvvEwusjzvAY6pgHsAO%2Bb2%2FFCX%2Fglq%2F%2FHNjYLs9AtlTXPv16GPwswzWTTpNWBVVFjNo60cqDE5G8mbB8SizTtsS5%2Bi3VK86KcVsOgb61DaUzsV2oksX61CWUp33oeswJY%2BrxkCz7Ry%2Fy8QowRB4yXWewuy0FMGrMKcDN8lpliCsIiV0t92uT7wLD7RNAU8gojPgcEr1JFgmzCoNiNb43yHIyG1%2BveMuKUsubTxH82vv0Q&X-Amz-Signature=84b1e45dd5a5ea42b40689390492e259c0097153d5a09e8cf5145bbc06c9d169&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNEKLXI4%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHfCIOrmXgk%2FGr%2Fmr4zci%2FheVSxMKOkAzMxvMSin7hhpAiA62zNyySHGQmEnT1txv4fBg51NGczpb%2BHM%2FOQS6I0T8SqIBAjA%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZPfPobJlDolNDFsTKtwDDaTEb%2BS35CRqQLKExG%2BDgbNbZguzZjIs5QHuIr6PcDGmBmCitTaBs99BIcvynpUJ0BSEJNtDUvudadyqFu1EHKOr%2FQHdFhspVx7gvI%2FmM%2Ff2NY1Atn9xWYmJ9wKeK3exG%2F%2F3sjZmkqdcs4coLhV6W10Np%2Fz0kOL2HWtHXO43Fr36x76hyMXsyIls2QgsFMITuNciaZUwWLkWwSbLhwzxY6Z9h68JV8MaLFsrq53nHGexqBPMCklXQWR1qfk7JSDBRVeaRNfOW%2FJ3SMS6uDI8t4jm3wIZSCHYsvhob3EDipdCMdjqajNYoj%2FcQtNsAlrskfxrHFNDnA3QHkIRjM39PSkqSwzDmdZfI9dGcjoGT%2FZkeDbuUY%2BVktg9h%2BrZnIt03dv2ApcYrccZfPctd1RW%2F1C1JPFd%2BsM26GihQyg9HBVyLh1qyXKkcRjQgiPsgmzElCPStITlKHq%2FFsZaqM4kLQD3b5WId3G9lUs%2BF1TAGLdLKK%2BnGpAsnY6ddfuuapBQJY9FMZGuk8tS4vxXFw8vETuM4409ZwDlMe9yLc7XcI6Lh603vVOT8LiB5L%2B3%2FgBKrP%2BjRA%2FmT1mMYyQ%2FO7rHxL6j25inhGFaG8NTFA75RXtwOVxJKNL9HYomvvEwusjzvAY6pgHsAO%2Bb2%2FFCX%2Fglq%2F%2FHNjYLs9AtlTXPv16GPwswzWTTpNWBVVFjNo60cqDE5G8mbB8SizTtsS5%2Bi3VK86KcVsOgb61DaUzsV2oksX61CWUp33oeswJY%2BrxkCz7Ry%2Fy8QowRB4yXWewuy0FMGrMKcDN8lpliCsIiV0t92uT7wLD7RNAU8gojPgcEr1JFgmzCoNiNb43yHIyG1%2BveMuKUsubTxH82vv0Q&X-Amz-Signature=7617b6c6ff52a8812597f90d20237f20510548051f152a38fc3f696161b4da06&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
