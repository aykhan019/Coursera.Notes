

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHTARAOD%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171247Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJGMEQCIECdiPjdAEyb8Pv%2FbgiGfJl5jAjt%2BMunLBfLf5ud3kBHAiAW%2FkfjFCACni5s9Ji3CZOPEVnKxy09rvFTmitWM%2BcUqir%2FAwh6EAAaDDYzNzQyMzE4MzgwNSIMs%2FJgRWh%2B06umF%2BVjKtwDnc00Fce3cxR8WvoowbMrSh5tYnkaAyTMjQF1%2FI%2FrwwJYRQARhO9yUdllzEWCniThm3zR87%2Fyr7zyTrL8Vj2%2FHHaTxBmXVPWW9rvGG%2FbqHzwboJ4bPF6r3IvW2YQ3OpccbuarlheM9eXGOa0N6qJUHnB5cZOJ77Cx66YJ8X%2BQdfByczHNeGX%2FgLSFL86Nfuffhi0%2Ffn%2Boh5dq7uBHC7xQxzv%2BTVJ9kwkqpClWvzetyxrjeB5ami8epvx%2Fi6VWI5mIH9fgpA7KsK9wukFhJx5vmrReQLlgGcM5zg3rx3xOI81ut9UIJKq%2BdWwdjgNj0s9xSLhDZj%2B%2B%2B71FHhJUwjnzKDj3GAhCqbVZZPgX8X2EJxJPAa0pG1Vxcre%2B3t73uctIDNfjbvEbkXDBtdD4Ux4UWuZTLp%2B8QDQ7Kr5Wx6uuUg%2Bu37%2BZ0HYQuOtzDEq6B9YJv6rlq8PkbyPRiszDH2BmA9NFDCYhfFCdgMl0fzw%2BaRXN1ck0m1UL7f2TaspeRghjOeFaFaFLDdOvRC3jnsZbmp18fgMGMXye8dZJj9X8zF%2BDTeRgiDcbEZ9hY9J6pvdufCTw4dSD5G4aAOaqGTlYCrqSAOtW9%2BNihRLhbmXbtrVn9QNifEyBDG9uvZIw2fuYvQY6pgGe3QxCxenh9rVISMwv2M0B%2FaV9ScAtNM0zMyr%2BZMkIV37y3qJF%2F03IJ7dfj6DflKxW5KWGTSQ30cjS0M7QujozOIBTu4ldZP44Rvfr5Hh54ojGwftLZeHXvWc7hfL87m0xJHQfdg4xeTtiu08gCGgf7kl4OCFzn7kXSAfG%2BMTjAmLmA8EV7pEOq9AxAS0QJ11fwG84fwdqptySqq9cR0zZr4OWn5b9&X-Amz-Signature=3d688a4e8b0bbfc358767dcd661bb669a2212ef0735c4f731454151337ca6f75&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHTARAOD%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171247Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJGMEQCIECdiPjdAEyb8Pv%2FbgiGfJl5jAjt%2BMunLBfLf5ud3kBHAiAW%2FkfjFCACni5s9Ji3CZOPEVnKxy09rvFTmitWM%2BcUqir%2FAwh6EAAaDDYzNzQyMzE4MzgwNSIMs%2FJgRWh%2B06umF%2BVjKtwDnc00Fce3cxR8WvoowbMrSh5tYnkaAyTMjQF1%2FI%2FrwwJYRQARhO9yUdllzEWCniThm3zR87%2Fyr7zyTrL8Vj2%2FHHaTxBmXVPWW9rvGG%2FbqHzwboJ4bPF6r3IvW2YQ3OpccbuarlheM9eXGOa0N6qJUHnB5cZOJ77Cx66YJ8X%2BQdfByczHNeGX%2FgLSFL86Nfuffhi0%2Ffn%2Boh5dq7uBHC7xQxzv%2BTVJ9kwkqpClWvzetyxrjeB5ami8epvx%2Fi6VWI5mIH9fgpA7KsK9wukFhJx5vmrReQLlgGcM5zg3rx3xOI81ut9UIJKq%2BdWwdjgNj0s9xSLhDZj%2B%2B%2B71FHhJUwjnzKDj3GAhCqbVZZPgX8X2EJxJPAa0pG1Vxcre%2B3t73uctIDNfjbvEbkXDBtdD4Ux4UWuZTLp%2B8QDQ7Kr5Wx6uuUg%2Bu37%2BZ0HYQuOtzDEq6B9YJv6rlq8PkbyPRiszDH2BmA9NFDCYhfFCdgMl0fzw%2BaRXN1ck0m1UL7f2TaspeRghjOeFaFaFLDdOvRC3jnsZbmp18fgMGMXye8dZJj9X8zF%2BDTeRgiDcbEZ9hY9J6pvdufCTw4dSD5G4aAOaqGTlYCrqSAOtW9%2BNihRLhbmXbtrVn9QNifEyBDG9uvZIw2fuYvQY6pgGe3QxCxenh9rVISMwv2M0B%2FaV9ScAtNM0zMyr%2BZMkIV37y3qJF%2F03IJ7dfj6DflKxW5KWGTSQ30cjS0M7QujozOIBTu4ldZP44Rvfr5Hh54ojGwftLZeHXvWc7hfL87m0xJHQfdg4xeTtiu08gCGgf7kl4OCFzn7kXSAfG%2BMTjAmLmA8EV7pEOq9AxAS0QJ11fwG84fwdqptySqq9cR0zZr4OWn5b9&X-Amz-Signature=6e27fbad819bc82279acf8fbed0a7c1c89aa80db0a1500b3d6b12d36759fb382&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHTARAOD%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171247Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJGMEQCIECdiPjdAEyb8Pv%2FbgiGfJl5jAjt%2BMunLBfLf5ud3kBHAiAW%2FkfjFCACni5s9Ji3CZOPEVnKxy09rvFTmitWM%2BcUqir%2FAwh6EAAaDDYzNzQyMzE4MzgwNSIMs%2FJgRWh%2B06umF%2BVjKtwDnc00Fce3cxR8WvoowbMrSh5tYnkaAyTMjQF1%2FI%2FrwwJYRQARhO9yUdllzEWCniThm3zR87%2Fyr7zyTrL8Vj2%2FHHaTxBmXVPWW9rvGG%2FbqHzwboJ4bPF6r3IvW2YQ3OpccbuarlheM9eXGOa0N6qJUHnB5cZOJ77Cx66YJ8X%2BQdfByczHNeGX%2FgLSFL86Nfuffhi0%2Ffn%2Boh5dq7uBHC7xQxzv%2BTVJ9kwkqpClWvzetyxrjeB5ami8epvx%2Fi6VWI5mIH9fgpA7KsK9wukFhJx5vmrReQLlgGcM5zg3rx3xOI81ut9UIJKq%2BdWwdjgNj0s9xSLhDZj%2B%2B%2B71FHhJUwjnzKDj3GAhCqbVZZPgX8X2EJxJPAa0pG1Vxcre%2B3t73uctIDNfjbvEbkXDBtdD4Ux4UWuZTLp%2B8QDQ7Kr5Wx6uuUg%2Bu37%2BZ0HYQuOtzDEq6B9YJv6rlq8PkbyPRiszDH2BmA9NFDCYhfFCdgMl0fzw%2BaRXN1ck0m1UL7f2TaspeRghjOeFaFaFLDdOvRC3jnsZbmp18fgMGMXye8dZJj9X8zF%2BDTeRgiDcbEZ9hY9J6pvdufCTw4dSD5G4aAOaqGTlYCrqSAOtW9%2BNihRLhbmXbtrVn9QNifEyBDG9uvZIw2fuYvQY6pgGe3QxCxenh9rVISMwv2M0B%2FaV9ScAtNM0zMyr%2BZMkIV37y3qJF%2F03IJ7dfj6DflKxW5KWGTSQ30cjS0M7QujozOIBTu4ldZP44Rvfr5Hh54ojGwftLZeHXvWc7hfL87m0xJHQfdg4xeTtiu08gCGgf7kl4OCFzn7kXSAfG%2BMTjAmLmA8EV7pEOq9AxAS0QJ11fwG84fwdqptySqq9cR0zZr4OWn5b9&X-Amz-Signature=8dda52aa79ec444b1d91b3d38d10f96bbac2a20fc6ff04f994f47a3aac6dd5c9&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHTARAOD%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171247Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJGMEQCIECdiPjdAEyb8Pv%2FbgiGfJl5jAjt%2BMunLBfLf5ud3kBHAiAW%2FkfjFCACni5s9Ji3CZOPEVnKxy09rvFTmitWM%2BcUqir%2FAwh6EAAaDDYzNzQyMzE4MzgwNSIMs%2FJgRWh%2B06umF%2BVjKtwDnc00Fce3cxR8WvoowbMrSh5tYnkaAyTMjQF1%2FI%2FrwwJYRQARhO9yUdllzEWCniThm3zR87%2Fyr7zyTrL8Vj2%2FHHaTxBmXVPWW9rvGG%2FbqHzwboJ4bPF6r3IvW2YQ3OpccbuarlheM9eXGOa0N6qJUHnB5cZOJ77Cx66YJ8X%2BQdfByczHNeGX%2FgLSFL86Nfuffhi0%2Ffn%2Boh5dq7uBHC7xQxzv%2BTVJ9kwkqpClWvzetyxrjeB5ami8epvx%2Fi6VWI5mIH9fgpA7KsK9wukFhJx5vmrReQLlgGcM5zg3rx3xOI81ut9UIJKq%2BdWwdjgNj0s9xSLhDZj%2B%2B%2B71FHhJUwjnzKDj3GAhCqbVZZPgX8X2EJxJPAa0pG1Vxcre%2B3t73uctIDNfjbvEbkXDBtdD4Ux4UWuZTLp%2B8QDQ7Kr5Wx6uuUg%2Bu37%2BZ0HYQuOtzDEq6B9YJv6rlq8PkbyPRiszDH2BmA9NFDCYhfFCdgMl0fzw%2BaRXN1ck0m1UL7f2TaspeRghjOeFaFaFLDdOvRC3jnsZbmp18fgMGMXye8dZJj9X8zF%2BDTeRgiDcbEZ9hY9J6pvdufCTw4dSD5G4aAOaqGTlYCrqSAOtW9%2BNihRLhbmXbtrVn9QNifEyBDG9uvZIw2fuYvQY6pgGe3QxCxenh9rVISMwv2M0B%2FaV9ScAtNM0zMyr%2BZMkIV37y3qJF%2F03IJ7dfj6DflKxW5KWGTSQ30cjS0M7QujozOIBTu4ldZP44Rvfr5Hh54ojGwftLZeHXvWc7hfL87m0xJHQfdg4xeTtiu08gCGgf7kl4OCFzn7kXSAfG%2BMTjAmLmA8EV7pEOq9AxAS0QJ11fwG84fwdqptySqq9cR0zZr4OWn5b9&X-Amz-Signature=a4e0a59b48ca6202af45998f8968ce52c7c80e48760683d581a96e0e1de98fe7&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHTARAOD%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171247Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJGMEQCIECdiPjdAEyb8Pv%2FbgiGfJl5jAjt%2BMunLBfLf5ud3kBHAiAW%2FkfjFCACni5s9Ji3CZOPEVnKxy09rvFTmitWM%2BcUqir%2FAwh6EAAaDDYzNzQyMzE4MzgwNSIMs%2FJgRWh%2B06umF%2BVjKtwDnc00Fce3cxR8WvoowbMrSh5tYnkaAyTMjQF1%2FI%2FrwwJYRQARhO9yUdllzEWCniThm3zR87%2Fyr7zyTrL8Vj2%2FHHaTxBmXVPWW9rvGG%2FbqHzwboJ4bPF6r3IvW2YQ3OpccbuarlheM9eXGOa0N6qJUHnB5cZOJ77Cx66YJ8X%2BQdfByczHNeGX%2FgLSFL86Nfuffhi0%2Ffn%2Boh5dq7uBHC7xQxzv%2BTVJ9kwkqpClWvzetyxrjeB5ami8epvx%2Fi6VWI5mIH9fgpA7KsK9wukFhJx5vmrReQLlgGcM5zg3rx3xOI81ut9UIJKq%2BdWwdjgNj0s9xSLhDZj%2B%2B%2B71FHhJUwjnzKDj3GAhCqbVZZPgX8X2EJxJPAa0pG1Vxcre%2B3t73uctIDNfjbvEbkXDBtdD4Ux4UWuZTLp%2B8QDQ7Kr5Wx6uuUg%2Bu37%2BZ0HYQuOtzDEq6B9YJv6rlq8PkbyPRiszDH2BmA9NFDCYhfFCdgMl0fzw%2BaRXN1ck0m1UL7f2TaspeRghjOeFaFaFLDdOvRC3jnsZbmp18fgMGMXye8dZJj9X8zF%2BDTeRgiDcbEZ9hY9J6pvdufCTw4dSD5G4aAOaqGTlYCrqSAOtW9%2BNihRLhbmXbtrVn9QNifEyBDG9uvZIw2fuYvQY6pgGe3QxCxenh9rVISMwv2M0B%2FaV9ScAtNM0zMyr%2BZMkIV37y3qJF%2F03IJ7dfj6DflKxW5KWGTSQ30cjS0M7QujozOIBTu4ldZP44Rvfr5Hh54ojGwftLZeHXvWc7hfL87m0xJHQfdg4xeTtiu08gCGgf7kl4OCFzn7kXSAfG%2BMTjAmLmA8EV7pEOq9AxAS0QJ11fwG84fwdqptySqq9cR0zZr4OWn5b9&X-Amz-Signature=9e006359511f19f28183f769e02add1105efe56c889d7358f8df67066e4b1b61&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHTARAOD%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171247Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJGMEQCIECdiPjdAEyb8Pv%2FbgiGfJl5jAjt%2BMunLBfLf5ud3kBHAiAW%2FkfjFCACni5s9Ji3CZOPEVnKxy09rvFTmitWM%2BcUqir%2FAwh6EAAaDDYzNzQyMzE4MzgwNSIMs%2FJgRWh%2B06umF%2BVjKtwDnc00Fce3cxR8WvoowbMrSh5tYnkaAyTMjQF1%2FI%2FrwwJYRQARhO9yUdllzEWCniThm3zR87%2Fyr7zyTrL8Vj2%2FHHaTxBmXVPWW9rvGG%2FbqHzwboJ4bPF6r3IvW2YQ3OpccbuarlheM9eXGOa0N6qJUHnB5cZOJ77Cx66YJ8X%2BQdfByczHNeGX%2FgLSFL86Nfuffhi0%2Ffn%2Boh5dq7uBHC7xQxzv%2BTVJ9kwkqpClWvzetyxrjeB5ami8epvx%2Fi6VWI5mIH9fgpA7KsK9wukFhJx5vmrReQLlgGcM5zg3rx3xOI81ut9UIJKq%2BdWwdjgNj0s9xSLhDZj%2B%2B%2B71FHhJUwjnzKDj3GAhCqbVZZPgX8X2EJxJPAa0pG1Vxcre%2B3t73uctIDNfjbvEbkXDBtdD4Ux4UWuZTLp%2B8QDQ7Kr5Wx6uuUg%2Bu37%2BZ0HYQuOtzDEq6B9YJv6rlq8PkbyPRiszDH2BmA9NFDCYhfFCdgMl0fzw%2BaRXN1ck0m1UL7f2TaspeRghjOeFaFaFLDdOvRC3jnsZbmp18fgMGMXye8dZJj9X8zF%2BDTeRgiDcbEZ9hY9J6pvdufCTw4dSD5G4aAOaqGTlYCrqSAOtW9%2BNihRLhbmXbtrVn9QNifEyBDG9uvZIw2fuYvQY6pgGe3QxCxenh9rVISMwv2M0B%2FaV9ScAtNM0zMyr%2BZMkIV37y3qJF%2F03IJ7dfj6DflKxW5KWGTSQ30cjS0M7QujozOIBTu4ldZP44Rvfr5Hh54ojGwftLZeHXvWc7hfL87m0xJHQfdg4xeTtiu08gCGgf7kl4OCFzn7kXSAfG%2BMTjAmLmA8EV7pEOq9AxAS0QJ11fwG84fwdqptySqq9cR0zZr4OWn5b9&X-Amz-Signature=21daecffc5b44af6bd1d781e4d5ee1546363bf988c8b45fe8fc5aeb79d60da70&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHTARAOD%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171247Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJGMEQCIECdiPjdAEyb8Pv%2FbgiGfJl5jAjt%2BMunLBfLf5ud3kBHAiAW%2FkfjFCACni5s9Ji3CZOPEVnKxy09rvFTmitWM%2BcUqir%2FAwh6EAAaDDYzNzQyMzE4MzgwNSIMs%2FJgRWh%2B06umF%2BVjKtwDnc00Fce3cxR8WvoowbMrSh5tYnkaAyTMjQF1%2FI%2FrwwJYRQARhO9yUdllzEWCniThm3zR87%2Fyr7zyTrL8Vj2%2FHHaTxBmXVPWW9rvGG%2FbqHzwboJ4bPF6r3IvW2YQ3OpccbuarlheM9eXGOa0N6qJUHnB5cZOJ77Cx66YJ8X%2BQdfByczHNeGX%2FgLSFL86Nfuffhi0%2Ffn%2Boh5dq7uBHC7xQxzv%2BTVJ9kwkqpClWvzetyxrjeB5ami8epvx%2Fi6VWI5mIH9fgpA7KsK9wukFhJx5vmrReQLlgGcM5zg3rx3xOI81ut9UIJKq%2BdWwdjgNj0s9xSLhDZj%2B%2B%2B71FHhJUwjnzKDj3GAhCqbVZZPgX8X2EJxJPAa0pG1Vxcre%2B3t73uctIDNfjbvEbkXDBtdD4Ux4UWuZTLp%2B8QDQ7Kr5Wx6uuUg%2Bu37%2BZ0HYQuOtzDEq6B9YJv6rlq8PkbyPRiszDH2BmA9NFDCYhfFCdgMl0fzw%2BaRXN1ck0m1UL7f2TaspeRghjOeFaFaFLDdOvRC3jnsZbmp18fgMGMXye8dZJj9X8zF%2BDTeRgiDcbEZ9hY9J6pvdufCTw4dSD5G4aAOaqGTlYCrqSAOtW9%2BNihRLhbmXbtrVn9QNifEyBDG9uvZIw2fuYvQY6pgGe3QxCxenh9rVISMwv2M0B%2FaV9ScAtNM0zMyr%2BZMkIV37y3qJF%2F03IJ7dfj6DflKxW5KWGTSQ30cjS0M7QujozOIBTu4ldZP44Rvfr5Hh54ojGwftLZeHXvWc7hfL87m0xJHQfdg4xeTtiu08gCGgf7kl4OCFzn7kXSAfG%2BMTjAmLmA8EV7pEOq9AxAS0QJ11fwG84fwdqptySqq9cR0zZr4OWn5b9&X-Amz-Signature=2a8c21d44432e01d0b9109a6afd8a6706fc1353a6d8ac475ee7b69779e22a4e6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHTARAOD%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171247Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJGMEQCIECdiPjdAEyb8Pv%2FbgiGfJl5jAjt%2BMunLBfLf5ud3kBHAiAW%2FkfjFCACni5s9Ji3CZOPEVnKxy09rvFTmitWM%2BcUqir%2FAwh6EAAaDDYzNzQyMzE4MzgwNSIMs%2FJgRWh%2B06umF%2BVjKtwDnc00Fce3cxR8WvoowbMrSh5tYnkaAyTMjQF1%2FI%2FrwwJYRQARhO9yUdllzEWCniThm3zR87%2Fyr7zyTrL8Vj2%2FHHaTxBmXVPWW9rvGG%2FbqHzwboJ4bPF6r3IvW2YQ3OpccbuarlheM9eXGOa0N6qJUHnB5cZOJ77Cx66YJ8X%2BQdfByczHNeGX%2FgLSFL86Nfuffhi0%2Ffn%2Boh5dq7uBHC7xQxzv%2BTVJ9kwkqpClWvzetyxrjeB5ami8epvx%2Fi6VWI5mIH9fgpA7KsK9wukFhJx5vmrReQLlgGcM5zg3rx3xOI81ut9UIJKq%2BdWwdjgNj0s9xSLhDZj%2B%2B%2B71FHhJUwjnzKDj3GAhCqbVZZPgX8X2EJxJPAa0pG1Vxcre%2B3t73uctIDNfjbvEbkXDBtdD4Ux4UWuZTLp%2B8QDQ7Kr5Wx6uuUg%2Bu37%2BZ0HYQuOtzDEq6B9YJv6rlq8PkbyPRiszDH2BmA9NFDCYhfFCdgMl0fzw%2BaRXN1ck0m1UL7f2TaspeRghjOeFaFaFLDdOvRC3jnsZbmp18fgMGMXye8dZJj9X8zF%2BDTeRgiDcbEZ9hY9J6pvdufCTw4dSD5G4aAOaqGTlYCrqSAOtW9%2BNihRLhbmXbtrVn9QNifEyBDG9uvZIw2fuYvQY6pgGe3QxCxenh9rVISMwv2M0B%2FaV9ScAtNM0zMyr%2BZMkIV37y3qJF%2F03IJ7dfj6DflKxW5KWGTSQ30cjS0M7QujozOIBTu4ldZP44Rvfr5Hh54ojGwftLZeHXvWc7hfL87m0xJHQfdg4xeTtiu08gCGgf7kl4OCFzn7kXSAfG%2BMTjAmLmA8EV7pEOq9AxAS0QJ11fwG84fwdqptySqq9cR0zZr4OWn5b9&X-Amz-Signature=3b896199745be1aa7a356dbe294379ca210446a82c9f104249b456c17a5db9b6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHTARAOD%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171247Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJGMEQCIECdiPjdAEyb8Pv%2FbgiGfJl5jAjt%2BMunLBfLf5ud3kBHAiAW%2FkfjFCACni5s9Ji3CZOPEVnKxy09rvFTmitWM%2BcUqir%2FAwh6EAAaDDYzNzQyMzE4MzgwNSIMs%2FJgRWh%2B06umF%2BVjKtwDnc00Fce3cxR8WvoowbMrSh5tYnkaAyTMjQF1%2FI%2FrwwJYRQARhO9yUdllzEWCniThm3zR87%2Fyr7zyTrL8Vj2%2FHHaTxBmXVPWW9rvGG%2FbqHzwboJ4bPF6r3IvW2YQ3OpccbuarlheM9eXGOa0N6qJUHnB5cZOJ77Cx66YJ8X%2BQdfByczHNeGX%2FgLSFL86Nfuffhi0%2Ffn%2Boh5dq7uBHC7xQxzv%2BTVJ9kwkqpClWvzetyxrjeB5ami8epvx%2Fi6VWI5mIH9fgpA7KsK9wukFhJx5vmrReQLlgGcM5zg3rx3xOI81ut9UIJKq%2BdWwdjgNj0s9xSLhDZj%2B%2B%2B71FHhJUwjnzKDj3GAhCqbVZZPgX8X2EJxJPAa0pG1Vxcre%2B3t73uctIDNfjbvEbkXDBtdD4Ux4UWuZTLp%2B8QDQ7Kr5Wx6uuUg%2Bu37%2BZ0HYQuOtzDEq6B9YJv6rlq8PkbyPRiszDH2BmA9NFDCYhfFCdgMl0fzw%2BaRXN1ck0m1UL7f2TaspeRghjOeFaFaFLDdOvRC3jnsZbmp18fgMGMXye8dZJj9X8zF%2BDTeRgiDcbEZ9hY9J6pvdufCTw4dSD5G4aAOaqGTlYCrqSAOtW9%2BNihRLhbmXbtrVn9QNifEyBDG9uvZIw2fuYvQY6pgGe3QxCxenh9rVISMwv2M0B%2FaV9ScAtNM0zMyr%2BZMkIV37y3qJF%2F03IJ7dfj6DflKxW5KWGTSQ30cjS0M7QujozOIBTu4ldZP44Rvfr5Hh54ojGwftLZeHXvWc7hfL87m0xJHQfdg4xeTtiu08gCGgf7kl4OCFzn7kXSAfG%2BMTjAmLmA8EV7pEOq9AxAS0QJ11fwG84fwdqptySqq9cR0zZr4OWn5b9&X-Amz-Signature=2879c1ca1b6231819a4b5a811bbc4a609b21fdebdac05813bd02f38875dd19f5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UAF5UHU%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIAuxt2cHzC%2B0jTCwEllFyEZd9%2F6Pmo4ZLTC3c4JHujWdAiEAuc4Xl83xXtAEm7wANgSXyPYffp2ImInaCA8A0EFw7c8q%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDP6w1DacrCHsqzQmNSrcA%2BuTXardPZ9RaS98%2BqwQY0AAZllJK5bz6Q1MFy6ijFFxQpBwrHrrdLoTKkxDfe6dS%2FCyOyQa30q%2Bl2ukk96xUWB42YrfGF56d43%2Bl8ndd9IjnbwK8E9Dhg86ERn8x5%2FjwA2FEvY2ZiNVLkvk%2FwALo8yX%2F6XQRpN2Yq8cjHyFOnbPwIpow21jRkvANUsSrBmvaSWTr0v7VyMeiDwyt3BpEn35p5mQKQoxJCW9vbc%2Bc7V7J%2BGbAlhKapSBufyte3zT0Udgws69FzZurFm5q7DEwv3U3q%2BEERmVaINVMhkofvsjRUcd98%2BD8UBHFXvYKewiQaqJCpJJ3OeZjl4dx11sI%2Fl3jmXWLJo8yz6XHuzjsVyoZ75mBP8EMWIyow2cRAiDRL%2B6fowR1JEbON90DLVlr7PTb%2BuocVcEHuM3xCTCKaPtNfu4oEhUgzpe2uqzC141tUzJlENfi6rDxuEU8WEm3wVceMP%2BOxIE0%2Fwn4koGbmKWURT%2BQjhNMjidIB0MKQ%2Bs1OjJ7BIDeW3zDbU3eOQcu2K%2Bmlql886iNZpmRM%2BujFbE1s0RDPP6IQfsfFrq1qiV8uSXJ%2B2hV%2Fgv6e%2B6VHvzbJKIa1oXjeyQPX%2BO3hTAAAo6YrvgHs0GJ5TLTP%2BbMIX8mL0GOqUBXxkAx50Vpp8AGkpZStKm3BEpNaMWcOM780QP5Fne5Qw%2BStytS2ejrvj%2B9RCC%2FGuLsSdu2me%2F43xvTBX4M%2BRGKU0%2BNnzZ57tnqkiWJ%2FyWVZ8GdhCdOwf7h1yOk6Gv%2FOvbc9%2Fj6eIyGOUK0QMT%2BU%2BRfqtO9U8bYSHvrTSwKoFPFLU1SgaErKRsPPFknYhKjVdrU8gPG690tsJf0s9gl9a7YRfrxG5i&X-Amz-Signature=84079057efcee336208dff0c61ac96d76bee6780efa08e702f3a4b2f7055d332&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UAF5UHU%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIAuxt2cHzC%2B0jTCwEllFyEZd9%2F6Pmo4ZLTC3c4JHujWdAiEAuc4Xl83xXtAEm7wANgSXyPYffp2ImInaCA8A0EFw7c8q%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDP6w1DacrCHsqzQmNSrcA%2BuTXardPZ9RaS98%2BqwQY0AAZllJK5bz6Q1MFy6ijFFxQpBwrHrrdLoTKkxDfe6dS%2FCyOyQa30q%2Bl2ukk96xUWB42YrfGF56d43%2Bl8ndd9IjnbwK8E9Dhg86ERn8x5%2FjwA2FEvY2ZiNVLkvk%2FwALo8yX%2F6XQRpN2Yq8cjHyFOnbPwIpow21jRkvANUsSrBmvaSWTr0v7VyMeiDwyt3BpEn35p5mQKQoxJCW9vbc%2Bc7V7J%2BGbAlhKapSBufyte3zT0Udgws69FzZurFm5q7DEwv3U3q%2BEERmVaINVMhkofvsjRUcd98%2BD8UBHFXvYKewiQaqJCpJJ3OeZjl4dx11sI%2Fl3jmXWLJo8yz6XHuzjsVyoZ75mBP8EMWIyow2cRAiDRL%2B6fowR1JEbON90DLVlr7PTb%2BuocVcEHuM3xCTCKaPtNfu4oEhUgzpe2uqzC141tUzJlENfi6rDxuEU8WEm3wVceMP%2BOxIE0%2Fwn4koGbmKWURT%2BQjhNMjidIB0MKQ%2Bs1OjJ7BIDeW3zDbU3eOQcu2K%2Bmlql886iNZpmRM%2BujFbE1s0RDPP6IQfsfFrq1qiV8uSXJ%2B2hV%2Fgv6e%2B6VHvzbJKIa1oXjeyQPX%2BO3hTAAAo6YrvgHs0GJ5TLTP%2BbMIX8mL0GOqUBXxkAx50Vpp8AGkpZStKm3BEpNaMWcOM780QP5Fne5Qw%2BStytS2ejrvj%2B9RCC%2FGuLsSdu2me%2F43xvTBX4M%2BRGKU0%2BNnzZ57tnqkiWJ%2FyWVZ8GdhCdOwf7h1yOk6Gv%2FOvbc9%2Fj6eIyGOUK0QMT%2BU%2BRfqtO9U8bYSHvrTSwKoFPFLU1SgaErKRsPPFknYhKjVdrU8gPG690tsJf0s9gl9a7YRfrxG5i&X-Amz-Signature=f71d2f1e0d15644735483cb8373419b29bda1b311428465a5f78cef3dd0757b4&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
