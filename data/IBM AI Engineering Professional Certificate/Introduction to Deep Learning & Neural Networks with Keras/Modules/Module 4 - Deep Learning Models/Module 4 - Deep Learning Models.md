

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665I3V4YMQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD2wz3IwFh4%2FGXkqYgcKKecRAehmgswFpdOKp18Z2SCzAIgfysFR3nz9PPts3Z9raf3kVJnjCWAwQudsbqUcAaMXHcqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKZYmIfqwxmHpeoHHSrcAweAOFQ9MXG%2B%2FoEOO9Ts7TWNOzFw%2Fygq58YZS6mgiNs4xmf3FW93Im9rvbkTFWb1FhhcGGP9fpAQ6quph0WOcauLciqQXfOW2ZWzlEMBzDNA%2BgeC%2FV0HOeDCEUEPOrD24k4NU9MUbUEbeAqDB91cqdZW9jkfqSEtiFFcJ7AIB%2FcPFXq1iaI9PwXq5G0myO1o%2BAgK3%2BV8CERRX6lHwiPpFvYil2KXz4e71nZ9X81m0UHN9XSJfCn2AlWvHdMoOGbDlNrfJ3fNfeT41nG%2BgCaP6pVnM5Asc1U5boqeS5I4nh984YP7TX0172EusXDjTI6tVxqzlLnqXdZY51sODKOH%2F5YXdwdIcvxErG%2F%2BLuR4kJKIQ2PzXqNvMJ5BokVJcQNMBGzbQzNuAKkx3VcE8xzKZlseu4OE2n7jCl5g4Q5tGRhKaeXHyhyW4E7nSjB%2B2e8WlezK9Gb9Ko2UiIG5nQNf6PCLBfgu8l2D957d6Y8vsb5wm16ElwBa%2Fnf2KQgzo2yRXsrSbG5zlTUeybsdpFyXa8d9rXOGLvxmBHhp76BflsqfTGdHozumEqHXKmuW4dqDYu3tzb0X4ooTAyb7ad6CJoARkBHGnBD1nosYjZWFtfbl8t0%2BVYoBL0CfKVt8MKjy%2BrwGOqUBNGYj376aJRfpnAhmDdyXaEfu%2B4a%2BPNvPGHo9CeOra4lB1DbbV14JCZOFaPQFbigHU9Y2eD1Xh0PEHV0qs0HaY73%2BqK%2FY3Kq2j7vAuY%2FEJLemFafoZHMEm%2F0VdZvESEk2DjPVUAZ58M6yiR2XRslYsPjlfIoK5%2FR72rzSHxHcMOQVr7hS0m4FSkzm%2BahMvj%2BSMmlnatpK%2Fs7PkM5j7VyVEbQV6npm&X-Amz-Signature=ffdf1c55becd106040fc40b500a3bcd04b2b1464c4df033e718fcd9a7f8d8ed5&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665I3V4YMQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011146Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD2wz3IwFh4%2FGXkqYgcKKecRAehmgswFpdOKp18Z2SCzAIgfysFR3nz9PPts3Z9raf3kVJnjCWAwQudsbqUcAaMXHcqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKZYmIfqwxmHpeoHHSrcAweAOFQ9MXG%2B%2FoEOO9Ts7TWNOzFw%2Fygq58YZS6mgiNs4xmf3FW93Im9rvbkTFWb1FhhcGGP9fpAQ6quph0WOcauLciqQXfOW2ZWzlEMBzDNA%2BgeC%2FV0HOeDCEUEPOrD24k4NU9MUbUEbeAqDB91cqdZW9jkfqSEtiFFcJ7AIB%2FcPFXq1iaI9PwXq5G0myO1o%2BAgK3%2BV8CERRX6lHwiPpFvYil2KXz4e71nZ9X81m0UHN9XSJfCn2AlWvHdMoOGbDlNrfJ3fNfeT41nG%2BgCaP6pVnM5Asc1U5boqeS5I4nh984YP7TX0172EusXDjTI6tVxqzlLnqXdZY51sODKOH%2F5YXdwdIcvxErG%2F%2BLuR4kJKIQ2PzXqNvMJ5BokVJcQNMBGzbQzNuAKkx3VcE8xzKZlseu4OE2n7jCl5g4Q5tGRhKaeXHyhyW4E7nSjB%2B2e8WlezK9Gb9Ko2UiIG5nQNf6PCLBfgu8l2D957d6Y8vsb5wm16ElwBa%2Fnf2KQgzo2yRXsrSbG5zlTUeybsdpFyXa8d9rXOGLvxmBHhp76BflsqfTGdHozumEqHXKmuW4dqDYu3tzb0X4ooTAyb7ad6CJoARkBHGnBD1nosYjZWFtfbl8t0%2BVYoBL0CfKVt8MKjy%2BrwGOqUBNGYj376aJRfpnAhmDdyXaEfu%2B4a%2BPNvPGHo9CeOra4lB1DbbV14JCZOFaPQFbigHU9Y2eD1Xh0PEHV0qs0HaY73%2BqK%2FY3Kq2j7vAuY%2FEJLemFafoZHMEm%2F0VdZvESEk2DjPVUAZ58M6yiR2XRslYsPjlfIoK5%2FR72rzSHxHcMOQVr7hS0m4FSkzm%2BahMvj%2BSMmlnatpK%2Fs7PkM5j7VyVEbQV6npm&X-Amz-Signature=17df75a96bf861d2826cbd1c9173d3ee8d69914558346d2657dcc8e994c4f515&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665I3V4YMQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011146Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD2wz3IwFh4%2FGXkqYgcKKecRAehmgswFpdOKp18Z2SCzAIgfysFR3nz9PPts3Z9raf3kVJnjCWAwQudsbqUcAaMXHcqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKZYmIfqwxmHpeoHHSrcAweAOFQ9MXG%2B%2FoEOO9Ts7TWNOzFw%2Fygq58YZS6mgiNs4xmf3FW93Im9rvbkTFWb1FhhcGGP9fpAQ6quph0WOcauLciqQXfOW2ZWzlEMBzDNA%2BgeC%2FV0HOeDCEUEPOrD24k4NU9MUbUEbeAqDB91cqdZW9jkfqSEtiFFcJ7AIB%2FcPFXq1iaI9PwXq5G0myO1o%2BAgK3%2BV8CERRX6lHwiPpFvYil2KXz4e71nZ9X81m0UHN9XSJfCn2AlWvHdMoOGbDlNrfJ3fNfeT41nG%2BgCaP6pVnM5Asc1U5boqeS5I4nh984YP7TX0172EusXDjTI6tVxqzlLnqXdZY51sODKOH%2F5YXdwdIcvxErG%2F%2BLuR4kJKIQ2PzXqNvMJ5BokVJcQNMBGzbQzNuAKkx3VcE8xzKZlseu4OE2n7jCl5g4Q5tGRhKaeXHyhyW4E7nSjB%2B2e8WlezK9Gb9Ko2UiIG5nQNf6PCLBfgu8l2D957d6Y8vsb5wm16ElwBa%2Fnf2KQgzo2yRXsrSbG5zlTUeybsdpFyXa8d9rXOGLvxmBHhp76BflsqfTGdHozumEqHXKmuW4dqDYu3tzb0X4ooTAyb7ad6CJoARkBHGnBD1nosYjZWFtfbl8t0%2BVYoBL0CfKVt8MKjy%2BrwGOqUBNGYj376aJRfpnAhmDdyXaEfu%2B4a%2BPNvPGHo9CeOra4lB1DbbV14JCZOFaPQFbigHU9Y2eD1Xh0PEHV0qs0HaY73%2BqK%2FY3Kq2j7vAuY%2FEJLemFafoZHMEm%2F0VdZvESEk2DjPVUAZ58M6yiR2XRslYsPjlfIoK5%2FR72rzSHxHcMOQVr7hS0m4FSkzm%2BahMvj%2BSMmlnatpK%2Fs7PkM5j7VyVEbQV6npm&X-Amz-Signature=262da7c171db7abce50a6bca6a2a2a420da4ebfa34b6d2bb77039452db1a6bfb&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665I3V4YMQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011146Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD2wz3IwFh4%2FGXkqYgcKKecRAehmgswFpdOKp18Z2SCzAIgfysFR3nz9PPts3Z9raf3kVJnjCWAwQudsbqUcAaMXHcqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKZYmIfqwxmHpeoHHSrcAweAOFQ9MXG%2B%2FoEOO9Ts7TWNOzFw%2Fygq58YZS6mgiNs4xmf3FW93Im9rvbkTFWb1FhhcGGP9fpAQ6quph0WOcauLciqQXfOW2ZWzlEMBzDNA%2BgeC%2FV0HOeDCEUEPOrD24k4NU9MUbUEbeAqDB91cqdZW9jkfqSEtiFFcJ7AIB%2FcPFXq1iaI9PwXq5G0myO1o%2BAgK3%2BV8CERRX6lHwiPpFvYil2KXz4e71nZ9X81m0UHN9XSJfCn2AlWvHdMoOGbDlNrfJ3fNfeT41nG%2BgCaP6pVnM5Asc1U5boqeS5I4nh984YP7TX0172EusXDjTI6tVxqzlLnqXdZY51sODKOH%2F5YXdwdIcvxErG%2F%2BLuR4kJKIQ2PzXqNvMJ5BokVJcQNMBGzbQzNuAKkx3VcE8xzKZlseu4OE2n7jCl5g4Q5tGRhKaeXHyhyW4E7nSjB%2B2e8WlezK9Gb9Ko2UiIG5nQNf6PCLBfgu8l2D957d6Y8vsb5wm16ElwBa%2Fnf2KQgzo2yRXsrSbG5zlTUeybsdpFyXa8d9rXOGLvxmBHhp76BflsqfTGdHozumEqHXKmuW4dqDYu3tzb0X4ooTAyb7ad6CJoARkBHGnBD1nosYjZWFtfbl8t0%2BVYoBL0CfKVt8MKjy%2BrwGOqUBNGYj376aJRfpnAhmDdyXaEfu%2B4a%2BPNvPGHo9CeOra4lB1DbbV14JCZOFaPQFbigHU9Y2eD1Xh0PEHV0qs0HaY73%2BqK%2FY3Kq2j7vAuY%2FEJLemFafoZHMEm%2F0VdZvESEk2DjPVUAZ58M6yiR2XRslYsPjlfIoK5%2FR72rzSHxHcMOQVr7hS0m4FSkzm%2BahMvj%2BSMmlnatpK%2Fs7PkM5j7VyVEbQV6npm&X-Amz-Signature=89158d9b5cdeeabfe2b29db6c8a1edc6dc41135f2304f269d7f1f7470b8b902e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665I3V4YMQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011146Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD2wz3IwFh4%2FGXkqYgcKKecRAehmgswFpdOKp18Z2SCzAIgfysFR3nz9PPts3Z9raf3kVJnjCWAwQudsbqUcAaMXHcqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKZYmIfqwxmHpeoHHSrcAweAOFQ9MXG%2B%2FoEOO9Ts7TWNOzFw%2Fygq58YZS6mgiNs4xmf3FW93Im9rvbkTFWb1FhhcGGP9fpAQ6quph0WOcauLciqQXfOW2ZWzlEMBzDNA%2BgeC%2FV0HOeDCEUEPOrD24k4NU9MUbUEbeAqDB91cqdZW9jkfqSEtiFFcJ7AIB%2FcPFXq1iaI9PwXq5G0myO1o%2BAgK3%2BV8CERRX6lHwiPpFvYil2KXz4e71nZ9X81m0UHN9XSJfCn2AlWvHdMoOGbDlNrfJ3fNfeT41nG%2BgCaP6pVnM5Asc1U5boqeS5I4nh984YP7TX0172EusXDjTI6tVxqzlLnqXdZY51sODKOH%2F5YXdwdIcvxErG%2F%2BLuR4kJKIQ2PzXqNvMJ5BokVJcQNMBGzbQzNuAKkx3VcE8xzKZlseu4OE2n7jCl5g4Q5tGRhKaeXHyhyW4E7nSjB%2B2e8WlezK9Gb9Ko2UiIG5nQNf6PCLBfgu8l2D957d6Y8vsb5wm16ElwBa%2Fnf2KQgzo2yRXsrSbG5zlTUeybsdpFyXa8d9rXOGLvxmBHhp76BflsqfTGdHozumEqHXKmuW4dqDYu3tzb0X4ooTAyb7ad6CJoARkBHGnBD1nosYjZWFtfbl8t0%2BVYoBL0CfKVt8MKjy%2BrwGOqUBNGYj376aJRfpnAhmDdyXaEfu%2B4a%2BPNvPGHo9CeOra4lB1DbbV14JCZOFaPQFbigHU9Y2eD1Xh0PEHV0qs0HaY73%2BqK%2FY3Kq2j7vAuY%2FEJLemFafoZHMEm%2F0VdZvESEk2DjPVUAZ58M6yiR2XRslYsPjlfIoK5%2FR72rzSHxHcMOQVr7hS0m4FSkzm%2BahMvj%2BSMmlnatpK%2Fs7PkM5j7VyVEbQV6npm&X-Amz-Signature=7ac54a86969995012321715cae00da327a0bf6306cca7d8bc07aa7f37538f292&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665I3V4YMQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011146Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD2wz3IwFh4%2FGXkqYgcKKecRAehmgswFpdOKp18Z2SCzAIgfysFR3nz9PPts3Z9raf3kVJnjCWAwQudsbqUcAaMXHcqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKZYmIfqwxmHpeoHHSrcAweAOFQ9MXG%2B%2FoEOO9Ts7TWNOzFw%2Fygq58YZS6mgiNs4xmf3FW93Im9rvbkTFWb1FhhcGGP9fpAQ6quph0WOcauLciqQXfOW2ZWzlEMBzDNA%2BgeC%2FV0HOeDCEUEPOrD24k4NU9MUbUEbeAqDB91cqdZW9jkfqSEtiFFcJ7AIB%2FcPFXq1iaI9PwXq5G0myO1o%2BAgK3%2BV8CERRX6lHwiPpFvYil2KXz4e71nZ9X81m0UHN9XSJfCn2AlWvHdMoOGbDlNrfJ3fNfeT41nG%2BgCaP6pVnM5Asc1U5boqeS5I4nh984YP7TX0172EusXDjTI6tVxqzlLnqXdZY51sODKOH%2F5YXdwdIcvxErG%2F%2BLuR4kJKIQ2PzXqNvMJ5BokVJcQNMBGzbQzNuAKkx3VcE8xzKZlseu4OE2n7jCl5g4Q5tGRhKaeXHyhyW4E7nSjB%2B2e8WlezK9Gb9Ko2UiIG5nQNf6PCLBfgu8l2D957d6Y8vsb5wm16ElwBa%2Fnf2KQgzo2yRXsrSbG5zlTUeybsdpFyXa8d9rXOGLvxmBHhp76BflsqfTGdHozumEqHXKmuW4dqDYu3tzb0X4ooTAyb7ad6CJoARkBHGnBD1nosYjZWFtfbl8t0%2BVYoBL0CfKVt8MKjy%2BrwGOqUBNGYj376aJRfpnAhmDdyXaEfu%2B4a%2BPNvPGHo9CeOra4lB1DbbV14JCZOFaPQFbigHU9Y2eD1Xh0PEHV0qs0HaY73%2BqK%2FY3Kq2j7vAuY%2FEJLemFafoZHMEm%2F0VdZvESEk2DjPVUAZ58M6yiR2XRslYsPjlfIoK5%2FR72rzSHxHcMOQVr7hS0m4FSkzm%2BahMvj%2BSMmlnatpK%2Fs7PkM5j7VyVEbQV6npm&X-Amz-Signature=8a4c2e1f15232e9550210b5cc9357f3b1e1f7c27bcbe6d37bbd0d82cd4498607&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665I3V4YMQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD2wz3IwFh4%2FGXkqYgcKKecRAehmgswFpdOKp18Z2SCzAIgfysFR3nz9PPts3Z9raf3kVJnjCWAwQudsbqUcAaMXHcqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKZYmIfqwxmHpeoHHSrcAweAOFQ9MXG%2B%2FoEOO9Ts7TWNOzFw%2Fygq58YZS6mgiNs4xmf3FW93Im9rvbkTFWb1FhhcGGP9fpAQ6quph0WOcauLciqQXfOW2ZWzlEMBzDNA%2BgeC%2FV0HOeDCEUEPOrD24k4NU9MUbUEbeAqDB91cqdZW9jkfqSEtiFFcJ7AIB%2FcPFXq1iaI9PwXq5G0myO1o%2BAgK3%2BV8CERRX6lHwiPpFvYil2KXz4e71nZ9X81m0UHN9XSJfCn2AlWvHdMoOGbDlNrfJ3fNfeT41nG%2BgCaP6pVnM5Asc1U5boqeS5I4nh984YP7TX0172EusXDjTI6tVxqzlLnqXdZY51sODKOH%2F5YXdwdIcvxErG%2F%2BLuR4kJKIQ2PzXqNvMJ5BokVJcQNMBGzbQzNuAKkx3VcE8xzKZlseu4OE2n7jCl5g4Q5tGRhKaeXHyhyW4E7nSjB%2B2e8WlezK9Gb9Ko2UiIG5nQNf6PCLBfgu8l2D957d6Y8vsb5wm16ElwBa%2Fnf2KQgzo2yRXsrSbG5zlTUeybsdpFyXa8d9rXOGLvxmBHhp76BflsqfTGdHozumEqHXKmuW4dqDYu3tzb0X4ooTAyb7ad6CJoARkBHGnBD1nosYjZWFtfbl8t0%2BVYoBL0CfKVt8MKjy%2BrwGOqUBNGYj376aJRfpnAhmDdyXaEfu%2B4a%2BPNvPGHo9CeOra4lB1DbbV14JCZOFaPQFbigHU9Y2eD1Xh0PEHV0qs0HaY73%2BqK%2FY3Kq2j7vAuY%2FEJLemFafoZHMEm%2F0VdZvESEk2DjPVUAZ58M6yiR2XRslYsPjlfIoK5%2FR72rzSHxHcMOQVr7hS0m4FSkzm%2BahMvj%2BSMmlnatpK%2Fs7PkM5j7VyVEbQV6npm&X-Amz-Signature=40bd5eba219e9ad97dab99ac80dff59c9aa372232a6c310cba0a69c5a748ea0e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665I3V4YMQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD2wz3IwFh4%2FGXkqYgcKKecRAehmgswFpdOKp18Z2SCzAIgfysFR3nz9PPts3Z9raf3kVJnjCWAwQudsbqUcAaMXHcqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKZYmIfqwxmHpeoHHSrcAweAOFQ9MXG%2B%2FoEOO9Ts7TWNOzFw%2Fygq58YZS6mgiNs4xmf3FW93Im9rvbkTFWb1FhhcGGP9fpAQ6quph0WOcauLciqQXfOW2ZWzlEMBzDNA%2BgeC%2FV0HOeDCEUEPOrD24k4NU9MUbUEbeAqDB91cqdZW9jkfqSEtiFFcJ7AIB%2FcPFXq1iaI9PwXq5G0myO1o%2BAgK3%2BV8CERRX6lHwiPpFvYil2KXz4e71nZ9X81m0UHN9XSJfCn2AlWvHdMoOGbDlNrfJ3fNfeT41nG%2BgCaP6pVnM5Asc1U5boqeS5I4nh984YP7TX0172EusXDjTI6tVxqzlLnqXdZY51sODKOH%2F5YXdwdIcvxErG%2F%2BLuR4kJKIQ2PzXqNvMJ5BokVJcQNMBGzbQzNuAKkx3VcE8xzKZlseu4OE2n7jCl5g4Q5tGRhKaeXHyhyW4E7nSjB%2B2e8WlezK9Gb9Ko2UiIG5nQNf6PCLBfgu8l2D957d6Y8vsb5wm16ElwBa%2Fnf2KQgzo2yRXsrSbG5zlTUeybsdpFyXa8d9rXOGLvxmBHhp76BflsqfTGdHozumEqHXKmuW4dqDYu3tzb0X4ooTAyb7ad6CJoARkBHGnBD1nosYjZWFtfbl8t0%2BVYoBL0CfKVt8MKjy%2BrwGOqUBNGYj376aJRfpnAhmDdyXaEfu%2B4a%2BPNvPGHo9CeOra4lB1DbbV14JCZOFaPQFbigHU9Y2eD1Xh0PEHV0qs0HaY73%2BqK%2FY3Kq2j7vAuY%2FEJLemFafoZHMEm%2F0VdZvESEk2DjPVUAZ58M6yiR2XRslYsPjlfIoK5%2FR72rzSHxHcMOQVr7hS0m4FSkzm%2BahMvj%2BSMmlnatpK%2Fs7PkM5j7VyVEbQV6npm&X-Amz-Signature=3363f1327a6f30869a8758c291bd7ec41933dcb5f2235b85cc55fcc61ac6536a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665I3V4YMQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD2wz3IwFh4%2FGXkqYgcKKecRAehmgswFpdOKp18Z2SCzAIgfysFR3nz9PPts3Z9raf3kVJnjCWAwQudsbqUcAaMXHcqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKZYmIfqwxmHpeoHHSrcAweAOFQ9MXG%2B%2FoEOO9Ts7TWNOzFw%2Fygq58YZS6mgiNs4xmf3FW93Im9rvbkTFWb1FhhcGGP9fpAQ6quph0WOcauLciqQXfOW2ZWzlEMBzDNA%2BgeC%2FV0HOeDCEUEPOrD24k4NU9MUbUEbeAqDB91cqdZW9jkfqSEtiFFcJ7AIB%2FcPFXq1iaI9PwXq5G0myO1o%2BAgK3%2BV8CERRX6lHwiPpFvYil2KXz4e71nZ9X81m0UHN9XSJfCn2AlWvHdMoOGbDlNrfJ3fNfeT41nG%2BgCaP6pVnM5Asc1U5boqeS5I4nh984YP7TX0172EusXDjTI6tVxqzlLnqXdZY51sODKOH%2F5YXdwdIcvxErG%2F%2BLuR4kJKIQ2PzXqNvMJ5BokVJcQNMBGzbQzNuAKkx3VcE8xzKZlseu4OE2n7jCl5g4Q5tGRhKaeXHyhyW4E7nSjB%2B2e8WlezK9Gb9Ko2UiIG5nQNf6PCLBfgu8l2D957d6Y8vsb5wm16ElwBa%2Fnf2KQgzo2yRXsrSbG5zlTUeybsdpFyXa8d9rXOGLvxmBHhp76BflsqfTGdHozumEqHXKmuW4dqDYu3tzb0X4ooTAyb7ad6CJoARkBHGnBD1nosYjZWFtfbl8t0%2BVYoBL0CfKVt8MKjy%2BrwGOqUBNGYj376aJRfpnAhmDdyXaEfu%2B4a%2BPNvPGHo9CeOra4lB1DbbV14JCZOFaPQFbigHU9Y2eD1Xh0PEHV0qs0HaY73%2BqK%2FY3Kq2j7vAuY%2FEJLemFafoZHMEm%2F0VdZvESEk2DjPVUAZ58M6yiR2XRslYsPjlfIoK5%2FR72rzSHxHcMOQVr7hS0m4FSkzm%2BahMvj%2BSMmlnatpK%2Fs7PkM5j7VyVEbQV6npm&X-Amz-Signature=c39ba73c6b95af510736b4c1745d4482c3d7c7e72d810ce4f7537c315d9463ff&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DRVDM3E%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG2i%2BBOcMoxcCIfgIMJWQt1M0l0kPgYTy3FDAUTCTXl5AiEAj3Y4cU8SdLttYKwPbqM8O03ZO2o6UipWIEO4PV1dEf8qiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDErLkgPuLyMvqS65MCrcA0AC23VO0HvasnBYtytU9bZdMAfdHz8y92d3ksAtHYQfO0780soab4fgSHo2Ea519JAYJvYj7VHvJ0iUBIDDgHGrjcB3VTP7eJQ27Z33V4qdInZKzCR0wzJj5V1eQ4bUTOB0TUB9ARG%2Bu77tEfLNVhbubuG26cuyc2cSF4w7GMb2geud068C0vjM%2BSkYF2AJtVncxArB1iBqL4MCZ1WUbp8eA49Fb3v2z%2ByOBp%2FLsT2fIvI%2FqxY38RwT11i6pEY7VzXx%2BuythrcatB88HAlKP5XjKTBckjk2%2F0V2QqEGDykJ4uYcECu20EmWAocW3XVJBdouQIGEVhF45gRjT4kp4JUbZ4QVadG2KtqKW%2ByIywBX7hYGFh3aLRkE65GSkLBLrmA5ORQqssemwApSYMDj0OCsmAJ0%2F0zYRQuGEViuT8xOgc06cGgq6B%2FzqMbtro%2BWWhBljKrrw0052faeMb2buwwQKi%2FBBjjt5oPWKcjeGwKg752M89aSELat0%2FoToFdMu6Enk5Fghdot91W9gC5%2BOjOq7pL29uj%2FqX7zT%2BuZHODZHXL2grT5n0KUKbwwv0ZKDryEKJ02iUVAF8ct5u%2BOTluDYvZeSE0d4KeJicfFnqWGB%2B%2BtEScqxIJW6G2KMM%2Fx%2BrwGOqUBS387YO%2BsSSBOLWKTz%2BAaizmyV6NIkdAiyD%2BiLSAhuQimfeZ7fNN2pwYzcMYvDPOBPHiinHfuBVWTl3yyC67GpyWX7Ihpg%2BjHvRSw1Ul16bhOPeOMoN%2FT4xe1XmizqlIN6mYNnLaezziH8gvzEXD8h0RUl%2B853t1%2BVrbA8JloIv0GYV8jjSrGde7j0PrJaS5bdDCWCMjXTWZNYMHdYDBNkt5%2FiYzM&X-Amz-Signature=de67617d7ec7257b1a0ad1f8028269517e5554a3ee76974f5f2ea73ad98f12eb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DRVDM3E%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG2i%2BBOcMoxcCIfgIMJWQt1M0l0kPgYTy3FDAUTCTXl5AiEAj3Y4cU8SdLttYKwPbqM8O03ZO2o6UipWIEO4PV1dEf8qiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDErLkgPuLyMvqS65MCrcA0AC23VO0HvasnBYtytU9bZdMAfdHz8y92d3ksAtHYQfO0780soab4fgSHo2Ea519JAYJvYj7VHvJ0iUBIDDgHGrjcB3VTP7eJQ27Z33V4qdInZKzCR0wzJj5V1eQ4bUTOB0TUB9ARG%2Bu77tEfLNVhbubuG26cuyc2cSF4w7GMb2geud068C0vjM%2BSkYF2AJtVncxArB1iBqL4MCZ1WUbp8eA49Fb3v2z%2ByOBp%2FLsT2fIvI%2FqxY38RwT11i6pEY7VzXx%2BuythrcatB88HAlKP5XjKTBckjk2%2F0V2QqEGDykJ4uYcECu20EmWAocW3XVJBdouQIGEVhF45gRjT4kp4JUbZ4QVadG2KtqKW%2ByIywBX7hYGFh3aLRkE65GSkLBLrmA5ORQqssemwApSYMDj0OCsmAJ0%2F0zYRQuGEViuT8xOgc06cGgq6B%2FzqMbtro%2BWWhBljKrrw0052faeMb2buwwQKi%2FBBjjt5oPWKcjeGwKg752M89aSELat0%2FoToFdMu6Enk5Fghdot91W9gC5%2BOjOq7pL29uj%2FqX7zT%2BuZHODZHXL2grT5n0KUKbwwv0ZKDryEKJ02iUVAF8ct5u%2BOTluDYvZeSE0d4KeJicfFnqWGB%2B%2BtEScqxIJW6G2KMM%2Fx%2BrwGOqUBS387YO%2BsSSBOLWKTz%2BAaizmyV6NIkdAiyD%2BiLSAhuQimfeZ7fNN2pwYzcMYvDPOBPHiinHfuBVWTl3yyC67GpyWX7Ihpg%2BjHvRSw1Ul16bhOPeOMoN%2FT4xe1XmizqlIN6mYNnLaezziH8gvzEXD8h0RUl%2B853t1%2BVrbA8JloIv0GYV8jjSrGde7j0PrJaS5bdDCWCMjXTWZNYMHdYDBNkt5%2FiYzM&X-Amz-Signature=8c3fb1d021859941f861fa8216637704deb238a5db18f2cfa8a103866057db41&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
