

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVIQ5QHB%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJGMEQCIAq5hsd%2Bj5J8W4DWi5mtg%2BUpgtRRd%2FcxnbLfBP9Cf6LAAiBEW%2B%2BRWJ2HHYJRFO485IaeIlfYCKKyHo89n0JlWxK4xCr%2FAwhpEAAaDDYzNzQyMzE4MzgwNSIMXWGb5JlXYPDsy3WRKtwDvOx9%2BXsokv4lOtz9GuYeG4CSEKOilxBPYQISXSNMsJFAi%2Bnc%2F7te1eWw7nKx2I%2FbtK6xB6A0uE8H%2BynZyiIq4dfiHJ5IaVfuTTghIWSBbIpSRJqWFQGXU44yCV9ZA9bOq%2BTqAYflaPGpVXzl2vmn971%2B9MG2oXmTag9DNzYJHhaJhx4k4LDsQcQyH5mvDXg7dP0NLqG8qerNfznqNk5VvhwTZB4CT%2BJN8J8lL6ntT59NwR6MTAgMuHlvWOUb1%2FMPXUZ%2FTlq%2Ba1G1rXZJjyxqXppevE8MyhhG74a8oO00ANw5aTChqHHP8S1ZGgiH5%2Ffpo874tYHX4pdKd4%2BO78Nsv6rMrRPjnSauBpzcrk5lEvYt%2B%2FnkJXz%2Fy28A9ngdck0Nt2il0wFJsHR2qZgGIq2mx44nO5UujE5U6jLFFSjFxwJZKFzMohCHW2t8pE3fYV90ZuU%2FkaiMYI4PFZglQBMxFIjFD%2Ffeo40p8%2FkeJWQ%2Fs1wI6XiCzRzYbT%2FFKuxG5rc3lXpPnjVs%2B%2FxM5FQWRlxuJLbQquCLJKi4O410l8xiws6qKlD%2FtBUwb1xvefTZPzSk8hULRFy1LimllGzQkGjz5YHMmhnUou%2FYLBkxEBUOuDUvg9o0%2FWWolHPgF50w5pmVvQY6pgG9rlBwsbU26JCNlM5w%2FjnfxCbdle1EkqAtHGzGP%2FFay2vXhx45R4Ytcq9CD5OWhzFCXBA6Fia95JRlGwzNK3Ey9%2FhCb%2F%2FXO4fFFkbz6yFW%2FuYAp4gKgAyKoHnC5YXeVO4IBTQthZwp8ONrIimCtBVcKc8Tb1WfIwV%2Bx%2FLoaMVgtOgNLOjxUMetGgSsXa6%2BS0TPSNaQKN2xTToGEN3bdlG2PUldaNjP&X-Amz-Signature=18500230f6206623671e8a9de228f9a0f6447f5b8023e803274767c7dad89816&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVIQ5QHB%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJGMEQCIAq5hsd%2Bj5J8W4DWi5mtg%2BUpgtRRd%2FcxnbLfBP9Cf6LAAiBEW%2B%2BRWJ2HHYJRFO485IaeIlfYCKKyHo89n0JlWxK4xCr%2FAwhpEAAaDDYzNzQyMzE4MzgwNSIMXWGb5JlXYPDsy3WRKtwDvOx9%2BXsokv4lOtz9GuYeG4CSEKOilxBPYQISXSNMsJFAi%2Bnc%2F7te1eWw7nKx2I%2FbtK6xB6A0uE8H%2BynZyiIq4dfiHJ5IaVfuTTghIWSBbIpSRJqWFQGXU44yCV9ZA9bOq%2BTqAYflaPGpVXzl2vmn971%2B9MG2oXmTag9DNzYJHhaJhx4k4LDsQcQyH5mvDXg7dP0NLqG8qerNfznqNk5VvhwTZB4CT%2BJN8J8lL6ntT59NwR6MTAgMuHlvWOUb1%2FMPXUZ%2FTlq%2Ba1G1rXZJjyxqXppevE8MyhhG74a8oO00ANw5aTChqHHP8S1ZGgiH5%2Ffpo874tYHX4pdKd4%2BO78Nsv6rMrRPjnSauBpzcrk5lEvYt%2B%2FnkJXz%2Fy28A9ngdck0Nt2il0wFJsHR2qZgGIq2mx44nO5UujE5U6jLFFSjFxwJZKFzMohCHW2t8pE3fYV90ZuU%2FkaiMYI4PFZglQBMxFIjFD%2Ffeo40p8%2FkeJWQ%2Fs1wI6XiCzRzYbT%2FFKuxG5rc3lXpPnjVs%2B%2FxM5FQWRlxuJLbQquCLJKi4O410l8xiws6qKlD%2FtBUwb1xvefTZPzSk8hULRFy1LimllGzQkGjz5YHMmhnUou%2FYLBkxEBUOuDUvg9o0%2FWWolHPgF50w5pmVvQY6pgG9rlBwsbU26JCNlM5w%2FjnfxCbdle1EkqAtHGzGP%2FFay2vXhx45R4Ytcq9CD5OWhzFCXBA6Fia95JRlGwzNK3Ey9%2FhCb%2F%2FXO4fFFkbz6yFW%2FuYAp4gKgAyKoHnC5YXeVO4IBTQthZwp8ONrIimCtBVcKc8Tb1WfIwV%2Bx%2FLoaMVgtOgNLOjxUMetGgSsXa6%2BS0TPSNaQKN2xTToGEN3bdlG2PUldaNjP&X-Amz-Signature=2b42a395f4b045c5cbf26b1c67afe04dc5ae320aa0c7682289efb7e66c8e3ff6&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVIQ5QHB%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJGMEQCIAq5hsd%2Bj5J8W4DWi5mtg%2BUpgtRRd%2FcxnbLfBP9Cf6LAAiBEW%2B%2BRWJ2HHYJRFO485IaeIlfYCKKyHo89n0JlWxK4xCr%2FAwhpEAAaDDYzNzQyMzE4MzgwNSIMXWGb5JlXYPDsy3WRKtwDvOx9%2BXsokv4lOtz9GuYeG4CSEKOilxBPYQISXSNMsJFAi%2Bnc%2F7te1eWw7nKx2I%2FbtK6xB6A0uE8H%2BynZyiIq4dfiHJ5IaVfuTTghIWSBbIpSRJqWFQGXU44yCV9ZA9bOq%2BTqAYflaPGpVXzl2vmn971%2B9MG2oXmTag9DNzYJHhaJhx4k4LDsQcQyH5mvDXg7dP0NLqG8qerNfznqNk5VvhwTZB4CT%2BJN8J8lL6ntT59NwR6MTAgMuHlvWOUb1%2FMPXUZ%2FTlq%2Ba1G1rXZJjyxqXppevE8MyhhG74a8oO00ANw5aTChqHHP8S1ZGgiH5%2Ffpo874tYHX4pdKd4%2BO78Nsv6rMrRPjnSauBpzcrk5lEvYt%2B%2FnkJXz%2Fy28A9ngdck0Nt2il0wFJsHR2qZgGIq2mx44nO5UujE5U6jLFFSjFxwJZKFzMohCHW2t8pE3fYV90ZuU%2FkaiMYI4PFZglQBMxFIjFD%2Ffeo40p8%2FkeJWQ%2Fs1wI6XiCzRzYbT%2FFKuxG5rc3lXpPnjVs%2B%2FxM5FQWRlxuJLbQquCLJKi4O410l8xiws6qKlD%2FtBUwb1xvefTZPzSk8hULRFy1LimllGzQkGjz5YHMmhnUou%2FYLBkxEBUOuDUvg9o0%2FWWolHPgF50w5pmVvQY6pgG9rlBwsbU26JCNlM5w%2FjnfxCbdle1EkqAtHGzGP%2FFay2vXhx45R4Ytcq9CD5OWhzFCXBA6Fia95JRlGwzNK3Ey9%2FhCb%2F%2FXO4fFFkbz6yFW%2FuYAp4gKgAyKoHnC5YXeVO4IBTQthZwp8ONrIimCtBVcKc8Tb1WfIwV%2Bx%2FLoaMVgtOgNLOjxUMetGgSsXa6%2BS0TPSNaQKN2xTToGEN3bdlG2PUldaNjP&X-Amz-Signature=89ac63ca770ccd1bf1410ec59cb6d3d0a164e3716e54be9b83ae8970b12b8436&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVIQ5QHB%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJGMEQCIAq5hsd%2Bj5J8W4DWi5mtg%2BUpgtRRd%2FcxnbLfBP9Cf6LAAiBEW%2B%2BRWJ2HHYJRFO485IaeIlfYCKKyHo89n0JlWxK4xCr%2FAwhpEAAaDDYzNzQyMzE4MzgwNSIMXWGb5JlXYPDsy3WRKtwDvOx9%2BXsokv4lOtz9GuYeG4CSEKOilxBPYQISXSNMsJFAi%2Bnc%2F7te1eWw7nKx2I%2FbtK6xB6A0uE8H%2BynZyiIq4dfiHJ5IaVfuTTghIWSBbIpSRJqWFQGXU44yCV9ZA9bOq%2BTqAYflaPGpVXzl2vmn971%2B9MG2oXmTag9DNzYJHhaJhx4k4LDsQcQyH5mvDXg7dP0NLqG8qerNfznqNk5VvhwTZB4CT%2BJN8J8lL6ntT59NwR6MTAgMuHlvWOUb1%2FMPXUZ%2FTlq%2Ba1G1rXZJjyxqXppevE8MyhhG74a8oO00ANw5aTChqHHP8S1ZGgiH5%2Ffpo874tYHX4pdKd4%2BO78Nsv6rMrRPjnSauBpzcrk5lEvYt%2B%2FnkJXz%2Fy28A9ngdck0Nt2il0wFJsHR2qZgGIq2mx44nO5UujE5U6jLFFSjFxwJZKFzMohCHW2t8pE3fYV90ZuU%2FkaiMYI4PFZglQBMxFIjFD%2Ffeo40p8%2FkeJWQ%2Fs1wI6XiCzRzYbT%2FFKuxG5rc3lXpPnjVs%2B%2FxM5FQWRlxuJLbQquCLJKi4O410l8xiws6qKlD%2FtBUwb1xvefTZPzSk8hULRFy1LimllGzQkGjz5YHMmhnUou%2FYLBkxEBUOuDUvg9o0%2FWWolHPgF50w5pmVvQY6pgG9rlBwsbU26JCNlM5w%2FjnfxCbdle1EkqAtHGzGP%2FFay2vXhx45R4Ytcq9CD5OWhzFCXBA6Fia95JRlGwzNK3Ey9%2FhCb%2F%2FXO4fFFkbz6yFW%2FuYAp4gKgAyKoHnC5YXeVO4IBTQthZwp8ONrIimCtBVcKc8Tb1WfIwV%2Bx%2FLoaMVgtOgNLOjxUMetGgSsXa6%2BS0TPSNaQKN2xTToGEN3bdlG2PUldaNjP&X-Amz-Signature=a71ec875eaa6dff9c0cb7bbd65f05b522c79ab1f98ff436184d258234850bbec&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVIQ5QHB%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJGMEQCIAq5hsd%2Bj5J8W4DWi5mtg%2BUpgtRRd%2FcxnbLfBP9Cf6LAAiBEW%2B%2BRWJ2HHYJRFO485IaeIlfYCKKyHo89n0JlWxK4xCr%2FAwhpEAAaDDYzNzQyMzE4MzgwNSIMXWGb5JlXYPDsy3WRKtwDvOx9%2BXsokv4lOtz9GuYeG4CSEKOilxBPYQISXSNMsJFAi%2Bnc%2F7te1eWw7nKx2I%2FbtK6xB6A0uE8H%2BynZyiIq4dfiHJ5IaVfuTTghIWSBbIpSRJqWFQGXU44yCV9ZA9bOq%2BTqAYflaPGpVXzl2vmn971%2B9MG2oXmTag9DNzYJHhaJhx4k4LDsQcQyH5mvDXg7dP0NLqG8qerNfznqNk5VvhwTZB4CT%2BJN8J8lL6ntT59NwR6MTAgMuHlvWOUb1%2FMPXUZ%2FTlq%2Ba1G1rXZJjyxqXppevE8MyhhG74a8oO00ANw5aTChqHHP8S1ZGgiH5%2Ffpo874tYHX4pdKd4%2BO78Nsv6rMrRPjnSauBpzcrk5lEvYt%2B%2FnkJXz%2Fy28A9ngdck0Nt2il0wFJsHR2qZgGIq2mx44nO5UujE5U6jLFFSjFxwJZKFzMohCHW2t8pE3fYV90ZuU%2FkaiMYI4PFZglQBMxFIjFD%2Ffeo40p8%2FkeJWQ%2Fs1wI6XiCzRzYbT%2FFKuxG5rc3lXpPnjVs%2B%2FxM5FQWRlxuJLbQquCLJKi4O410l8xiws6qKlD%2FtBUwb1xvefTZPzSk8hULRFy1LimllGzQkGjz5YHMmhnUou%2FYLBkxEBUOuDUvg9o0%2FWWolHPgF50w5pmVvQY6pgG9rlBwsbU26JCNlM5w%2FjnfxCbdle1EkqAtHGzGP%2FFay2vXhx45R4Ytcq9CD5OWhzFCXBA6Fia95JRlGwzNK3Ey9%2FhCb%2F%2FXO4fFFkbz6yFW%2FuYAp4gKgAyKoHnC5YXeVO4IBTQthZwp8ONrIimCtBVcKc8Tb1WfIwV%2Bx%2FLoaMVgtOgNLOjxUMetGgSsXa6%2BS0TPSNaQKN2xTToGEN3bdlG2PUldaNjP&X-Amz-Signature=373cb2087b73cca620538b4c4b488bb0dd07b861f058393f0ce2ab1675a9c1a0&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVIQ5QHB%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJGMEQCIAq5hsd%2Bj5J8W4DWi5mtg%2BUpgtRRd%2FcxnbLfBP9Cf6LAAiBEW%2B%2BRWJ2HHYJRFO485IaeIlfYCKKyHo89n0JlWxK4xCr%2FAwhpEAAaDDYzNzQyMzE4MzgwNSIMXWGb5JlXYPDsy3WRKtwDvOx9%2BXsokv4lOtz9GuYeG4CSEKOilxBPYQISXSNMsJFAi%2Bnc%2F7te1eWw7nKx2I%2FbtK6xB6A0uE8H%2BynZyiIq4dfiHJ5IaVfuTTghIWSBbIpSRJqWFQGXU44yCV9ZA9bOq%2BTqAYflaPGpVXzl2vmn971%2B9MG2oXmTag9DNzYJHhaJhx4k4LDsQcQyH5mvDXg7dP0NLqG8qerNfznqNk5VvhwTZB4CT%2BJN8J8lL6ntT59NwR6MTAgMuHlvWOUb1%2FMPXUZ%2FTlq%2Ba1G1rXZJjyxqXppevE8MyhhG74a8oO00ANw5aTChqHHP8S1ZGgiH5%2Ffpo874tYHX4pdKd4%2BO78Nsv6rMrRPjnSauBpzcrk5lEvYt%2B%2FnkJXz%2Fy28A9ngdck0Nt2il0wFJsHR2qZgGIq2mx44nO5UujE5U6jLFFSjFxwJZKFzMohCHW2t8pE3fYV90ZuU%2FkaiMYI4PFZglQBMxFIjFD%2Ffeo40p8%2FkeJWQ%2Fs1wI6XiCzRzYbT%2FFKuxG5rc3lXpPnjVs%2B%2FxM5FQWRlxuJLbQquCLJKi4O410l8xiws6qKlD%2FtBUwb1xvefTZPzSk8hULRFy1LimllGzQkGjz5YHMmhnUou%2FYLBkxEBUOuDUvg9o0%2FWWolHPgF50w5pmVvQY6pgG9rlBwsbU26JCNlM5w%2FjnfxCbdle1EkqAtHGzGP%2FFay2vXhx45R4Ytcq9CD5OWhzFCXBA6Fia95JRlGwzNK3Ey9%2FhCb%2F%2FXO4fFFkbz6yFW%2FuYAp4gKgAyKoHnC5YXeVO4IBTQthZwp8ONrIimCtBVcKc8Tb1WfIwV%2Bx%2FLoaMVgtOgNLOjxUMetGgSsXa6%2BS0TPSNaQKN2xTToGEN3bdlG2PUldaNjP&X-Amz-Signature=4f52f58a10a5a2c4accb9fc9cdf45c9de615e98bb63d66f76bb8d9139388d07d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVIQ5QHB%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJGMEQCIAq5hsd%2Bj5J8W4DWi5mtg%2BUpgtRRd%2FcxnbLfBP9Cf6LAAiBEW%2B%2BRWJ2HHYJRFO485IaeIlfYCKKyHo89n0JlWxK4xCr%2FAwhpEAAaDDYzNzQyMzE4MzgwNSIMXWGb5JlXYPDsy3WRKtwDvOx9%2BXsokv4lOtz9GuYeG4CSEKOilxBPYQISXSNMsJFAi%2Bnc%2F7te1eWw7nKx2I%2FbtK6xB6A0uE8H%2BynZyiIq4dfiHJ5IaVfuTTghIWSBbIpSRJqWFQGXU44yCV9ZA9bOq%2BTqAYflaPGpVXzl2vmn971%2B9MG2oXmTag9DNzYJHhaJhx4k4LDsQcQyH5mvDXg7dP0NLqG8qerNfznqNk5VvhwTZB4CT%2BJN8J8lL6ntT59NwR6MTAgMuHlvWOUb1%2FMPXUZ%2FTlq%2Ba1G1rXZJjyxqXppevE8MyhhG74a8oO00ANw5aTChqHHP8S1ZGgiH5%2Ffpo874tYHX4pdKd4%2BO78Nsv6rMrRPjnSauBpzcrk5lEvYt%2B%2FnkJXz%2Fy28A9ngdck0Nt2il0wFJsHR2qZgGIq2mx44nO5UujE5U6jLFFSjFxwJZKFzMohCHW2t8pE3fYV90ZuU%2FkaiMYI4PFZglQBMxFIjFD%2Ffeo40p8%2FkeJWQ%2Fs1wI6XiCzRzYbT%2FFKuxG5rc3lXpPnjVs%2B%2FxM5FQWRlxuJLbQquCLJKi4O410l8xiws6qKlD%2FtBUwb1xvefTZPzSk8hULRFy1LimllGzQkGjz5YHMmhnUou%2FYLBkxEBUOuDUvg9o0%2FWWolHPgF50w5pmVvQY6pgG9rlBwsbU26JCNlM5w%2FjnfxCbdle1EkqAtHGzGP%2FFay2vXhx45R4Ytcq9CD5OWhzFCXBA6Fia95JRlGwzNK3Ey9%2FhCb%2F%2FXO4fFFkbz6yFW%2FuYAp4gKgAyKoHnC5YXeVO4IBTQthZwp8ONrIimCtBVcKc8Tb1WfIwV%2Bx%2FLoaMVgtOgNLOjxUMetGgSsXa6%2BS0TPSNaQKN2xTToGEN3bdlG2PUldaNjP&X-Amz-Signature=7ba11169795ed3400825ee95197275a1853d3089127dd7c393d9effc305b0488&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVIQ5QHB%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJGMEQCIAq5hsd%2Bj5J8W4DWi5mtg%2BUpgtRRd%2FcxnbLfBP9Cf6LAAiBEW%2B%2BRWJ2HHYJRFO485IaeIlfYCKKyHo89n0JlWxK4xCr%2FAwhpEAAaDDYzNzQyMzE4MzgwNSIMXWGb5JlXYPDsy3WRKtwDvOx9%2BXsokv4lOtz9GuYeG4CSEKOilxBPYQISXSNMsJFAi%2Bnc%2F7te1eWw7nKx2I%2FbtK6xB6A0uE8H%2BynZyiIq4dfiHJ5IaVfuTTghIWSBbIpSRJqWFQGXU44yCV9ZA9bOq%2BTqAYflaPGpVXzl2vmn971%2B9MG2oXmTag9DNzYJHhaJhx4k4LDsQcQyH5mvDXg7dP0NLqG8qerNfznqNk5VvhwTZB4CT%2BJN8J8lL6ntT59NwR6MTAgMuHlvWOUb1%2FMPXUZ%2FTlq%2Ba1G1rXZJjyxqXppevE8MyhhG74a8oO00ANw5aTChqHHP8S1ZGgiH5%2Ffpo874tYHX4pdKd4%2BO78Nsv6rMrRPjnSauBpzcrk5lEvYt%2B%2FnkJXz%2Fy28A9ngdck0Nt2il0wFJsHR2qZgGIq2mx44nO5UujE5U6jLFFSjFxwJZKFzMohCHW2t8pE3fYV90ZuU%2FkaiMYI4PFZglQBMxFIjFD%2Ffeo40p8%2FkeJWQ%2Fs1wI6XiCzRzYbT%2FFKuxG5rc3lXpPnjVs%2B%2FxM5FQWRlxuJLbQquCLJKi4O410l8xiws6qKlD%2FtBUwb1xvefTZPzSk8hULRFy1LimllGzQkGjz5YHMmhnUou%2FYLBkxEBUOuDUvg9o0%2FWWolHPgF50w5pmVvQY6pgG9rlBwsbU26JCNlM5w%2FjnfxCbdle1EkqAtHGzGP%2FFay2vXhx45R4Ytcq9CD5OWhzFCXBA6Fia95JRlGwzNK3Ey9%2FhCb%2F%2FXO4fFFkbz6yFW%2FuYAp4gKgAyKoHnC5YXeVO4IBTQthZwp8ONrIimCtBVcKc8Tb1WfIwV%2Bx%2FLoaMVgtOgNLOjxUMetGgSsXa6%2BS0TPSNaQKN2xTToGEN3bdlG2PUldaNjP&X-Amz-Signature=5c41359ee4022a18213768bd095df059477cf9629fd7e443e6152b0f700722dd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVIQ5QHB%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJGMEQCIAq5hsd%2Bj5J8W4DWi5mtg%2BUpgtRRd%2FcxnbLfBP9Cf6LAAiBEW%2B%2BRWJ2HHYJRFO485IaeIlfYCKKyHo89n0JlWxK4xCr%2FAwhpEAAaDDYzNzQyMzE4MzgwNSIMXWGb5JlXYPDsy3WRKtwDvOx9%2BXsokv4lOtz9GuYeG4CSEKOilxBPYQISXSNMsJFAi%2Bnc%2F7te1eWw7nKx2I%2FbtK6xB6A0uE8H%2BynZyiIq4dfiHJ5IaVfuTTghIWSBbIpSRJqWFQGXU44yCV9ZA9bOq%2BTqAYflaPGpVXzl2vmn971%2B9MG2oXmTag9DNzYJHhaJhx4k4LDsQcQyH5mvDXg7dP0NLqG8qerNfznqNk5VvhwTZB4CT%2BJN8J8lL6ntT59NwR6MTAgMuHlvWOUb1%2FMPXUZ%2FTlq%2Ba1G1rXZJjyxqXppevE8MyhhG74a8oO00ANw5aTChqHHP8S1ZGgiH5%2Ffpo874tYHX4pdKd4%2BO78Nsv6rMrRPjnSauBpzcrk5lEvYt%2B%2FnkJXz%2Fy28A9ngdck0Nt2il0wFJsHR2qZgGIq2mx44nO5UujE5U6jLFFSjFxwJZKFzMohCHW2t8pE3fYV90ZuU%2FkaiMYI4PFZglQBMxFIjFD%2Ffeo40p8%2FkeJWQ%2Fs1wI6XiCzRzYbT%2FFKuxG5rc3lXpPnjVs%2B%2FxM5FQWRlxuJLbQquCLJKi4O410l8xiws6qKlD%2FtBUwb1xvefTZPzSk8hULRFy1LimllGzQkGjz5YHMmhnUou%2FYLBkxEBUOuDUvg9o0%2FWWolHPgF50w5pmVvQY6pgG9rlBwsbU26JCNlM5w%2FjnfxCbdle1EkqAtHGzGP%2FFay2vXhx45R4Ytcq9CD5OWhzFCXBA6Fia95JRlGwzNK3Ey9%2FhCb%2F%2FXO4fFFkbz6yFW%2FuYAp4gKgAyKoHnC5YXeVO4IBTQthZwp8ONrIimCtBVcKc8Tb1WfIwV%2Bx%2FLoaMVgtOgNLOjxUMetGgSsXa6%2BS0TPSNaQKN2xTToGEN3bdlG2PUldaNjP&X-Amz-Signature=465eb7ef552081c2f650478492d09337302258b0ac924433d867804d863a57b7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RQRLVXXT%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIQDoyel1mJlAgJJVeGQAwgjOUHA%2BqQmKs7CMDBMYfHwQlgIgAdIjbOJH6TepEpNrE%2FQ9yNsoZ4HPh222EcH3wv%2F0NoEq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDIq2im805LVyN2gpqCrcA7IWP%2FWt0vbjf5wKhVq7Q%2FbrGFcUG8RnDMp4c%2BI8TU%2BvLL7RKs8aNLE%2Fc2BFFLXm9H1prME6gtzZOQREgZ0T6xcNtNwRWCSCoA3FaqPyCv2nhGvVFAQoW9jrJlUgHyBJaEMyf9CqkFn1%2FZwMo1WUvaWcU9tcJyxi3mES0YM9rCzRUPwbAe3g7xsaiQNpWpDjPx7kf5lpRUfOImHF5z%2F6g1TLjjXhKvx%2F%2FvzFRP5Ck%2F%2BNZymEkIKnMDZQXqoHDFGZYoO6EvuQysaGGIjlGI7hqkAIa51S4xmnGUIeP5X2zw8C4afHzhpZB714xjYPHR%2FKU3LwnqO2O4fo1Azr0tc%2BycGpBnUEya7RVTAvcFBGq8amu4%2BQIephxPf7e8xRTsMy7oU7A75fGX%2BxWG8qqS6jKbc8X7a7Ffe2%2Bavg0wNq5fNfGHYR%2BKIm7O%2BaEfUf9674VIDa4H3xFHWuSlcUzSKQQqBPwYU2h28G2P%2BdcDJhkijpT8baaGjHYN4E7spiqYkA4d3%2FjYnkbo3K5bGApl7lem74duey650Rdu35K5hTpcoS%2BMS3oE71jYJJ5wXxK1JkY%2BNZRGIrkP%2BklBKJRyTHZmD1BkKG9v9HxyTDWhtWDyXB%2FzV7rU6wsAKT0%2FqnMKKalb0GOqUBmrj6qO9PoD%2F52%2Blz61zQLWEsnRFEWWK%2FOfIOCAgeDdCyateaKHunfuiHPGzkpGjTZjwFGw6rnJBOHRiJJuohSve%2BDv2RpUfAv0I0J2HVhi0bNnwS1byjGoZzLi1EOGVS9GGSaqbo2bOdDsdDKWFZXsPu%2F5fBczS6UcWJGoiFdihWkxSO7ZMUe5uXlVTm1a8ZU0s7wt0lktefhlRkjzQ7kLS3nr1%2F&X-Amz-Signature=442d8b42b321223706b405d494636a3b67ba2a60c6270984b809549742a64daf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RQRLVXXT%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIQDoyel1mJlAgJJVeGQAwgjOUHA%2BqQmKs7CMDBMYfHwQlgIgAdIjbOJH6TepEpNrE%2FQ9yNsoZ4HPh222EcH3wv%2F0NoEq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDIq2im805LVyN2gpqCrcA7IWP%2FWt0vbjf5wKhVq7Q%2FbrGFcUG8RnDMp4c%2BI8TU%2BvLL7RKs8aNLE%2Fc2BFFLXm9H1prME6gtzZOQREgZ0T6xcNtNwRWCSCoA3FaqPyCv2nhGvVFAQoW9jrJlUgHyBJaEMyf9CqkFn1%2FZwMo1WUvaWcU9tcJyxi3mES0YM9rCzRUPwbAe3g7xsaiQNpWpDjPx7kf5lpRUfOImHF5z%2F6g1TLjjXhKvx%2F%2FvzFRP5Ck%2F%2BNZymEkIKnMDZQXqoHDFGZYoO6EvuQysaGGIjlGI7hqkAIa51S4xmnGUIeP5X2zw8C4afHzhpZB714xjYPHR%2FKU3LwnqO2O4fo1Azr0tc%2BycGpBnUEya7RVTAvcFBGq8amu4%2BQIephxPf7e8xRTsMy7oU7A75fGX%2BxWG8qqS6jKbc8X7a7Ffe2%2Bavg0wNq5fNfGHYR%2BKIm7O%2BaEfUf9674VIDa4H3xFHWuSlcUzSKQQqBPwYU2h28G2P%2BdcDJhkijpT8baaGjHYN4E7spiqYkA4d3%2FjYnkbo3K5bGApl7lem74duey650Rdu35K5hTpcoS%2BMS3oE71jYJJ5wXxK1JkY%2BNZRGIrkP%2BklBKJRyTHZmD1BkKG9v9HxyTDWhtWDyXB%2FzV7rU6wsAKT0%2FqnMKKalb0GOqUBmrj6qO9PoD%2F52%2Blz61zQLWEsnRFEWWK%2FOfIOCAgeDdCyateaKHunfuiHPGzkpGjTZjwFGw6rnJBOHRiJJuohSve%2BDv2RpUfAv0I0J2HVhi0bNnwS1byjGoZzLi1EOGVS9GGSaqbo2bOdDsdDKWFZXsPu%2F5fBczS6UcWJGoiFdihWkxSO7ZMUe5uXlVTm1a8ZU0s7wt0lktefhlRkjzQ7kLS3nr1%2F&X-Amz-Signature=8c2ee581c71114d7d31999ba7be589c3f64d35863ad96b84960c27ef08b649d1&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
