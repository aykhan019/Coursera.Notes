

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJYSW65O%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181741Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG0qhspNufNuiQ36BD5ms5BPdG%2F1HpqWcU4lVCFQ%2BykMAiBKjQpAA52936RbTgA%2BsmxYKDonlUbUyKqUTTIuWT97mSqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM0bdFgTNtOa71%2FwPFKtwDFPtdG9yxL5sLihiDyuOEgH19TE5AMcYZRKQA3QGZ2rcGwLk9R1SYNVnAuUwCDTCfHKdB06CYbMk0rHaGg95ArW8f%2F9q26%2FwXtFqKEH6ENpafJIHW%2FABxgNuk8ZYRCmMqdu43Pt9KUKVk1L5%2FvcxUs2zqHbMRxcGmDx%2BcbNE5ntV9mKutEvziNGereS6XkaWOPONxO2H1BBu9smDt4eI1h7wXR7kpJzt2FRC1Vav1rJ%2F%2BGYOXJmvdbqvk7CCqFb77CR%2FF7j14Cs%2BhGm1vuZeelocDDn6JP2yo%2FsH31vocN4TFhCpTVs6q6Komr5V5Rz%2BHqu0kRg4a6%2ByhizDQC9FK8ec94QD%2BM7MhG%2BxIaByQKLbp4v0we8f%2BReNx74DxsS4wQynrcdkJ7PIAA9TpCJ7u%2Bi%2FNm89son198Bz%2FW4a0Z5hUpkir3ETZAKjFDSYMRQl702BOMKze8W%2Bxyu1q2wb%2ByR2IBl63vp5LJ4SnZBjHaq%2BqvruirXgK5liRfYPMI%2FVfe4tENsKYWWYz8JDg%2BYGZgcnm3OMtBAOwvljC%2F7KqMvjyOjMCok5Kbr5gTpSy%2BTY95Qrh2AhW%2Bsb1nZiM6ot07bFEVll%2F4CfoJGmrkPXwU%2FUm%2FoJLj%2BRjgCtMKDUwh8b4vAY6pgENhsgn0d%2Baw%2B8tU1ipJjrHT2BdRraZG%2BVzTH01flu9Ufh9kZkf8Z8yOe9GP591xYbER9myns%2FH3cKkBV9GOb8PUS8nQbtf0895vAXseTzJoIwM3nZv1teK%2BfT6x%2Fqu4uEpksN%2FiFU9xiJxCg6H3WfmlYC5svmAhs4xmhIO1VZNpqCDKjeHGs9DsW6%2BKItFMQ2IxiieM%2BOkQiXhBcSFvQHFwftPNPwm&X-Amz-Signature=1e28082e3a7654f3f1e078c716e8598e2ef4b9ff8b5557a27d878af03aea0583&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJYSW65O%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181741Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG0qhspNufNuiQ36BD5ms5BPdG%2F1HpqWcU4lVCFQ%2BykMAiBKjQpAA52936RbTgA%2BsmxYKDonlUbUyKqUTTIuWT97mSqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM0bdFgTNtOa71%2FwPFKtwDFPtdG9yxL5sLihiDyuOEgH19TE5AMcYZRKQA3QGZ2rcGwLk9R1SYNVnAuUwCDTCfHKdB06CYbMk0rHaGg95ArW8f%2F9q26%2FwXtFqKEH6ENpafJIHW%2FABxgNuk8ZYRCmMqdu43Pt9KUKVk1L5%2FvcxUs2zqHbMRxcGmDx%2BcbNE5ntV9mKutEvziNGereS6XkaWOPONxO2H1BBu9smDt4eI1h7wXR7kpJzt2FRC1Vav1rJ%2F%2BGYOXJmvdbqvk7CCqFb77CR%2FF7j14Cs%2BhGm1vuZeelocDDn6JP2yo%2FsH31vocN4TFhCpTVs6q6Komr5V5Rz%2BHqu0kRg4a6%2ByhizDQC9FK8ec94QD%2BM7MhG%2BxIaByQKLbp4v0we8f%2BReNx74DxsS4wQynrcdkJ7PIAA9TpCJ7u%2Bi%2FNm89son198Bz%2FW4a0Z5hUpkir3ETZAKjFDSYMRQl702BOMKze8W%2Bxyu1q2wb%2ByR2IBl63vp5LJ4SnZBjHaq%2BqvruirXgK5liRfYPMI%2FVfe4tENsKYWWYz8JDg%2BYGZgcnm3OMtBAOwvljC%2F7KqMvjyOjMCok5Kbr5gTpSy%2BTY95Qrh2AhW%2Bsb1nZiM6ot07bFEVll%2F4CfoJGmrkPXwU%2FUm%2FoJLj%2BRjgCtMKDUwh8b4vAY6pgENhsgn0d%2Baw%2B8tU1ipJjrHT2BdRraZG%2BVzTH01flu9Ufh9kZkf8Z8yOe9GP591xYbER9myns%2FH3cKkBV9GOb8PUS8nQbtf0895vAXseTzJoIwM3nZv1teK%2BfT6x%2Fqu4uEpksN%2FiFU9xiJxCg6H3WfmlYC5svmAhs4xmhIO1VZNpqCDKjeHGs9DsW6%2BKItFMQ2IxiieM%2BOkQiXhBcSFvQHFwftPNPwm&X-Amz-Signature=1332bb8534bcc9975ff46523eac46356a92cac4249600c2611fd5fff14354b69&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJYSW65O%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181741Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG0qhspNufNuiQ36BD5ms5BPdG%2F1HpqWcU4lVCFQ%2BykMAiBKjQpAA52936RbTgA%2BsmxYKDonlUbUyKqUTTIuWT97mSqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM0bdFgTNtOa71%2FwPFKtwDFPtdG9yxL5sLihiDyuOEgH19TE5AMcYZRKQA3QGZ2rcGwLk9R1SYNVnAuUwCDTCfHKdB06CYbMk0rHaGg95ArW8f%2F9q26%2FwXtFqKEH6ENpafJIHW%2FABxgNuk8ZYRCmMqdu43Pt9KUKVk1L5%2FvcxUs2zqHbMRxcGmDx%2BcbNE5ntV9mKutEvziNGereS6XkaWOPONxO2H1BBu9smDt4eI1h7wXR7kpJzt2FRC1Vav1rJ%2F%2BGYOXJmvdbqvk7CCqFb77CR%2FF7j14Cs%2BhGm1vuZeelocDDn6JP2yo%2FsH31vocN4TFhCpTVs6q6Komr5V5Rz%2BHqu0kRg4a6%2ByhizDQC9FK8ec94QD%2BM7MhG%2BxIaByQKLbp4v0we8f%2BReNx74DxsS4wQynrcdkJ7PIAA9TpCJ7u%2Bi%2FNm89son198Bz%2FW4a0Z5hUpkir3ETZAKjFDSYMRQl702BOMKze8W%2Bxyu1q2wb%2ByR2IBl63vp5LJ4SnZBjHaq%2BqvruirXgK5liRfYPMI%2FVfe4tENsKYWWYz8JDg%2BYGZgcnm3OMtBAOwvljC%2F7KqMvjyOjMCok5Kbr5gTpSy%2BTY95Qrh2AhW%2Bsb1nZiM6ot07bFEVll%2F4CfoJGmrkPXwU%2FUm%2FoJLj%2BRjgCtMKDUwh8b4vAY6pgENhsgn0d%2Baw%2B8tU1ipJjrHT2BdRraZG%2BVzTH01flu9Ufh9kZkf8Z8yOe9GP591xYbER9myns%2FH3cKkBV9GOb8PUS8nQbtf0895vAXseTzJoIwM3nZv1teK%2BfT6x%2Fqu4uEpksN%2FiFU9xiJxCg6H3WfmlYC5svmAhs4xmhIO1VZNpqCDKjeHGs9DsW6%2BKItFMQ2IxiieM%2BOkQiXhBcSFvQHFwftPNPwm&X-Amz-Signature=5eb7c32f66a17c69d500e79a03fce049a485bac3cbb8fa883c78174872ee918a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJYSW65O%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181741Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG0qhspNufNuiQ36BD5ms5BPdG%2F1HpqWcU4lVCFQ%2BykMAiBKjQpAA52936RbTgA%2BsmxYKDonlUbUyKqUTTIuWT97mSqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM0bdFgTNtOa71%2FwPFKtwDFPtdG9yxL5sLihiDyuOEgH19TE5AMcYZRKQA3QGZ2rcGwLk9R1SYNVnAuUwCDTCfHKdB06CYbMk0rHaGg95ArW8f%2F9q26%2FwXtFqKEH6ENpafJIHW%2FABxgNuk8ZYRCmMqdu43Pt9KUKVk1L5%2FvcxUs2zqHbMRxcGmDx%2BcbNE5ntV9mKutEvziNGereS6XkaWOPONxO2H1BBu9smDt4eI1h7wXR7kpJzt2FRC1Vav1rJ%2F%2BGYOXJmvdbqvk7CCqFb77CR%2FF7j14Cs%2BhGm1vuZeelocDDn6JP2yo%2FsH31vocN4TFhCpTVs6q6Komr5V5Rz%2BHqu0kRg4a6%2ByhizDQC9FK8ec94QD%2BM7MhG%2BxIaByQKLbp4v0we8f%2BReNx74DxsS4wQynrcdkJ7PIAA9TpCJ7u%2Bi%2FNm89son198Bz%2FW4a0Z5hUpkir3ETZAKjFDSYMRQl702BOMKze8W%2Bxyu1q2wb%2ByR2IBl63vp5LJ4SnZBjHaq%2BqvruirXgK5liRfYPMI%2FVfe4tENsKYWWYz8JDg%2BYGZgcnm3OMtBAOwvljC%2F7KqMvjyOjMCok5Kbr5gTpSy%2BTY95Qrh2AhW%2Bsb1nZiM6ot07bFEVll%2F4CfoJGmrkPXwU%2FUm%2FoJLj%2BRjgCtMKDUwh8b4vAY6pgENhsgn0d%2Baw%2B8tU1ipJjrHT2BdRraZG%2BVzTH01flu9Ufh9kZkf8Z8yOe9GP591xYbER9myns%2FH3cKkBV9GOb8PUS8nQbtf0895vAXseTzJoIwM3nZv1teK%2BfT6x%2Fqu4uEpksN%2FiFU9xiJxCg6H3WfmlYC5svmAhs4xmhIO1VZNpqCDKjeHGs9DsW6%2BKItFMQ2IxiieM%2BOkQiXhBcSFvQHFwftPNPwm&X-Amz-Signature=8d3314230ca96ecdf2cad78659008f25a97eecac14d80b7b23b6f3fab9580e7a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJYSW65O%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181741Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG0qhspNufNuiQ36BD5ms5BPdG%2F1HpqWcU4lVCFQ%2BykMAiBKjQpAA52936RbTgA%2BsmxYKDonlUbUyKqUTTIuWT97mSqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM0bdFgTNtOa71%2FwPFKtwDFPtdG9yxL5sLihiDyuOEgH19TE5AMcYZRKQA3QGZ2rcGwLk9R1SYNVnAuUwCDTCfHKdB06CYbMk0rHaGg95ArW8f%2F9q26%2FwXtFqKEH6ENpafJIHW%2FABxgNuk8ZYRCmMqdu43Pt9KUKVk1L5%2FvcxUs2zqHbMRxcGmDx%2BcbNE5ntV9mKutEvziNGereS6XkaWOPONxO2H1BBu9smDt4eI1h7wXR7kpJzt2FRC1Vav1rJ%2F%2BGYOXJmvdbqvk7CCqFb77CR%2FF7j14Cs%2BhGm1vuZeelocDDn6JP2yo%2FsH31vocN4TFhCpTVs6q6Komr5V5Rz%2BHqu0kRg4a6%2ByhizDQC9FK8ec94QD%2BM7MhG%2BxIaByQKLbp4v0we8f%2BReNx74DxsS4wQynrcdkJ7PIAA9TpCJ7u%2Bi%2FNm89son198Bz%2FW4a0Z5hUpkir3ETZAKjFDSYMRQl702BOMKze8W%2Bxyu1q2wb%2ByR2IBl63vp5LJ4SnZBjHaq%2BqvruirXgK5liRfYPMI%2FVfe4tENsKYWWYz8JDg%2BYGZgcnm3OMtBAOwvljC%2F7KqMvjyOjMCok5Kbr5gTpSy%2BTY95Qrh2AhW%2Bsb1nZiM6ot07bFEVll%2F4CfoJGmrkPXwU%2FUm%2FoJLj%2BRjgCtMKDUwh8b4vAY6pgENhsgn0d%2Baw%2B8tU1ipJjrHT2BdRraZG%2BVzTH01flu9Ufh9kZkf8Z8yOe9GP591xYbER9myns%2FH3cKkBV9GOb8PUS8nQbtf0895vAXseTzJoIwM3nZv1teK%2BfT6x%2Fqu4uEpksN%2FiFU9xiJxCg6H3WfmlYC5svmAhs4xmhIO1VZNpqCDKjeHGs9DsW6%2BKItFMQ2IxiieM%2BOkQiXhBcSFvQHFwftPNPwm&X-Amz-Signature=2256aacbb3c9c5e75194c46138ee750adf321214f0937c3851792545ad71eb4a&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJYSW65O%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181741Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG0qhspNufNuiQ36BD5ms5BPdG%2F1HpqWcU4lVCFQ%2BykMAiBKjQpAA52936RbTgA%2BsmxYKDonlUbUyKqUTTIuWT97mSqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM0bdFgTNtOa71%2FwPFKtwDFPtdG9yxL5sLihiDyuOEgH19TE5AMcYZRKQA3QGZ2rcGwLk9R1SYNVnAuUwCDTCfHKdB06CYbMk0rHaGg95ArW8f%2F9q26%2FwXtFqKEH6ENpafJIHW%2FABxgNuk8ZYRCmMqdu43Pt9KUKVk1L5%2FvcxUs2zqHbMRxcGmDx%2BcbNE5ntV9mKutEvziNGereS6XkaWOPONxO2H1BBu9smDt4eI1h7wXR7kpJzt2FRC1Vav1rJ%2F%2BGYOXJmvdbqvk7CCqFb77CR%2FF7j14Cs%2BhGm1vuZeelocDDn6JP2yo%2FsH31vocN4TFhCpTVs6q6Komr5V5Rz%2BHqu0kRg4a6%2ByhizDQC9FK8ec94QD%2BM7MhG%2BxIaByQKLbp4v0we8f%2BReNx74DxsS4wQynrcdkJ7PIAA9TpCJ7u%2Bi%2FNm89son198Bz%2FW4a0Z5hUpkir3ETZAKjFDSYMRQl702BOMKze8W%2Bxyu1q2wb%2ByR2IBl63vp5LJ4SnZBjHaq%2BqvruirXgK5liRfYPMI%2FVfe4tENsKYWWYz8JDg%2BYGZgcnm3OMtBAOwvljC%2F7KqMvjyOjMCok5Kbr5gTpSy%2BTY95Qrh2AhW%2Bsb1nZiM6ot07bFEVll%2F4CfoJGmrkPXwU%2FUm%2FoJLj%2BRjgCtMKDUwh8b4vAY6pgENhsgn0d%2Baw%2B8tU1ipJjrHT2BdRraZG%2BVzTH01flu9Ufh9kZkf8Z8yOe9GP591xYbER9myns%2FH3cKkBV9GOb8PUS8nQbtf0895vAXseTzJoIwM3nZv1teK%2BfT6x%2Fqu4uEpksN%2FiFU9xiJxCg6H3WfmlYC5svmAhs4xmhIO1VZNpqCDKjeHGs9DsW6%2BKItFMQ2IxiieM%2BOkQiXhBcSFvQHFwftPNPwm&X-Amz-Signature=1e96166f7cdd40a22b8871f618c41d86798ea7edbff551bacd1d39f214d23b22&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJYSW65O%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181741Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG0qhspNufNuiQ36BD5ms5BPdG%2F1HpqWcU4lVCFQ%2BykMAiBKjQpAA52936RbTgA%2BsmxYKDonlUbUyKqUTTIuWT97mSqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM0bdFgTNtOa71%2FwPFKtwDFPtdG9yxL5sLihiDyuOEgH19TE5AMcYZRKQA3QGZ2rcGwLk9R1SYNVnAuUwCDTCfHKdB06CYbMk0rHaGg95ArW8f%2F9q26%2FwXtFqKEH6ENpafJIHW%2FABxgNuk8ZYRCmMqdu43Pt9KUKVk1L5%2FvcxUs2zqHbMRxcGmDx%2BcbNE5ntV9mKutEvziNGereS6XkaWOPONxO2H1BBu9smDt4eI1h7wXR7kpJzt2FRC1Vav1rJ%2F%2BGYOXJmvdbqvk7CCqFb77CR%2FF7j14Cs%2BhGm1vuZeelocDDn6JP2yo%2FsH31vocN4TFhCpTVs6q6Komr5V5Rz%2BHqu0kRg4a6%2ByhizDQC9FK8ec94QD%2BM7MhG%2BxIaByQKLbp4v0we8f%2BReNx74DxsS4wQynrcdkJ7PIAA9TpCJ7u%2Bi%2FNm89son198Bz%2FW4a0Z5hUpkir3ETZAKjFDSYMRQl702BOMKze8W%2Bxyu1q2wb%2ByR2IBl63vp5LJ4SnZBjHaq%2BqvruirXgK5liRfYPMI%2FVfe4tENsKYWWYz8JDg%2BYGZgcnm3OMtBAOwvljC%2F7KqMvjyOjMCok5Kbr5gTpSy%2BTY95Qrh2AhW%2Bsb1nZiM6ot07bFEVll%2F4CfoJGmrkPXwU%2FUm%2FoJLj%2BRjgCtMKDUwh8b4vAY6pgENhsgn0d%2Baw%2B8tU1ipJjrHT2BdRraZG%2BVzTH01flu9Ufh9kZkf8Z8yOe9GP591xYbER9myns%2FH3cKkBV9GOb8PUS8nQbtf0895vAXseTzJoIwM3nZv1teK%2BfT6x%2Fqu4uEpksN%2FiFU9xiJxCg6H3WfmlYC5svmAhs4xmhIO1VZNpqCDKjeHGs9DsW6%2BKItFMQ2IxiieM%2BOkQiXhBcSFvQHFwftPNPwm&X-Amz-Signature=086f8abb879112d44a9ffc001b8da1dc3a650630849ff1c563b90a2184c7ae60&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJYSW65O%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181741Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG0qhspNufNuiQ36BD5ms5BPdG%2F1HpqWcU4lVCFQ%2BykMAiBKjQpAA52936RbTgA%2BsmxYKDonlUbUyKqUTTIuWT97mSqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM0bdFgTNtOa71%2FwPFKtwDFPtdG9yxL5sLihiDyuOEgH19TE5AMcYZRKQA3QGZ2rcGwLk9R1SYNVnAuUwCDTCfHKdB06CYbMk0rHaGg95ArW8f%2F9q26%2FwXtFqKEH6ENpafJIHW%2FABxgNuk8ZYRCmMqdu43Pt9KUKVk1L5%2FvcxUs2zqHbMRxcGmDx%2BcbNE5ntV9mKutEvziNGereS6XkaWOPONxO2H1BBu9smDt4eI1h7wXR7kpJzt2FRC1Vav1rJ%2F%2BGYOXJmvdbqvk7CCqFb77CR%2FF7j14Cs%2BhGm1vuZeelocDDn6JP2yo%2FsH31vocN4TFhCpTVs6q6Komr5V5Rz%2BHqu0kRg4a6%2ByhizDQC9FK8ec94QD%2BM7MhG%2BxIaByQKLbp4v0we8f%2BReNx74DxsS4wQynrcdkJ7PIAA9TpCJ7u%2Bi%2FNm89son198Bz%2FW4a0Z5hUpkir3ETZAKjFDSYMRQl702BOMKze8W%2Bxyu1q2wb%2ByR2IBl63vp5LJ4SnZBjHaq%2BqvruirXgK5liRfYPMI%2FVfe4tENsKYWWYz8JDg%2BYGZgcnm3OMtBAOwvljC%2F7KqMvjyOjMCok5Kbr5gTpSy%2BTY95Qrh2AhW%2Bsb1nZiM6ot07bFEVll%2F4CfoJGmrkPXwU%2FUm%2FoJLj%2BRjgCtMKDUwh8b4vAY6pgENhsgn0d%2Baw%2B8tU1ipJjrHT2BdRraZG%2BVzTH01flu9Ufh9kZkf8Z8yOe9GP591xYbER9myns%2FH3cKkBV9GOb8PUS8nQbtf0895vAXseTzJoIwM3nZv1teK%2BfT6x%2Fqu4uEpksN%2FiFU9xiJxCg6H3WfmlYC5svmAhs4xmhIO1VZNpqCDKjeHGs9DsW6%2BKItFMQ2IxiieM%2BOkQiXhBcSFvQHFwftPNPwm&X-Amz-Signature=b2766077adf18dc93855eb315ee3dc1cfd7e5de76afcaa6e9a819471ffbb5349&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJYSW65O%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181741Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG0qhspNufNuiQ36BD5ms5BPdG%2F1HpqWcU4lVCFQ%2BykMAiBKjQpAA52936RbTgA%2BsmxYKDonlUbUyKqUTTIuWT97mSqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM0bdFgTNtOa71%2FwPFKtwDFPtdG9yxL5sLihiDyuOEgH19TE5AMcYZRKQA3QGZ2rcGwLk9R1SYNVnAuUwCDTCfHKdB06CYbMk0rHaGg95ArW8f%2F9q26%2FwXtFqKEH6ENpafJIHW%2FABxgNuk8ZYRCmMqdu43Pt9KUKVk1L5%2FvcxUs2zqHbMRxcGmDx%2BcbNE5ntV9mKutEvziNGereS6XkaWOPONxO2H1BBu9smDt4eI1h7wXR7kpJzt2FRC1Vav1rJ%2F%2BGYOXJmvdbqvk7CCqFb77CR%2FF7j14Cs%2BhGm1vuZeelocDDn6JP2yo%2FsH31vocN4TFhCpTVs6q6Komr5V5Rz%2BHqu0kRg4a6%2ByhizDQC9FK8ec94QD%2BM7MhG%2BxIaByQKLbp4v0we8f%2BReNx74DxsS4wQynrcdkJ7PIAA9TpCJ7u%2Bi%2FNm89son198Bz%2FW4a0Z5hUpkir3ETZAKjFDSYMRQl702BOMKze8W%2Bxyu1q2wb%2ByR2IBl63vp5LJ4SnZBjHaq%2BqvruirXgK5liRfYPMI%2FVfe4tENsKYWWYz8JDg%2BYGZgcnm3OMtBAOwvljC%2F7KqMvjyOjMCok5Kbr5gTpSy%2BTY95Qrh2AhW%2Bsb1nZiM6ot07bFEVll%2F4CfoJGmrkPXwU%2FUm%2FoJLj%2BRjgCtMKDUwh8b4vAY6pgENhsgn0d%2Baw%2B8tU1ipJjrHT2BdRraZG%2BVzTH01flu9Ufh9kZkf8Z8yOe9GP591xYbER9myns%2FH3cKkBV9GOb8PUS8nQbtf0895vAXseTzJoIwM3nZv1teK%2BfT6x%2Fqu4uEpksN%2FiFU9xiJxCg6H3WfmlYC5svmAhs4xmhIO1VZNpqCDKjeHGs9DsW6%2BKItFMQ2IxiieM%2BOkQiXhBcSFvQHFwftPNPwm&X-Amz-Signature=40fd8df54e7b0d853fe2652943cc7a1a797bda39b238b5c1314da6e8567d5144&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VKB2UB3E%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181742Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDBxG7nFoIQGAZynmyCKS2myDAFeb5S9tS2guHXZ0Ge1AIhAMKylnHPsxh31J%2Fno9%2FW0F9QqDE1IXOWpAQQJ0MXubrWKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgybwQBNwgLVW4jt7Cwq3AOHCd62vxtRO72MjJCi3kOLUzqj8Ok%2FWO0z2r4nkaR%2By2PXeVPY87KWcGoWIEGRm4VZRGEd42FQrcdUDGbICxOCRB0ryfmkwjNz7MnywAHnemLXhjHKMHBzrSNJPAFgX3mr4tmVmBobub04F5WkduTh%2FEJFdBFJWRaJAXpiziy1Ofr2%2FtDcKaABa60EQkGwyDSjV22MUELpeYzDHIS%2BoI%2BSvP1HcGOzCqbGcnM1M%2FJ9p4P3oBrsEcBm6cHHsooo5Xwem51c2Wrr9bxIltkJ543zQtZL9SPylHMpHw8d3fh9ueyI%2Bdu5YWtTQRHDb34jllcCjUgllDA1Eu%2FZof4u2ZYKT0grtRKkpKjyvOa9t%2BFFx9UEFJtOUcl6x%2FwuTIefdkVP0fd06c30EaJle0bXfpaTfoVqrZhWEeQ2K1DSeoIKQjN2oPUUKgWX8U8aaxupOvUdkM6VZ4WU1Jl6oC36ec1HRDknS9AdSyrNCqtQyeKTpPnM65Ftr3XWEdnNYyg4WNuYF%2Bso5PaWdvq58%2BUEgqO1siUThOQ%2B9ksEU%2BZ9K4AqjKm22zfCMJj07mQB%2BcclHayBLySe7lvANOR%2FtSnqVxtt%2BkdanttanuNB%2BCU2UbXS4m8LWpmvqy8nrGw2MTDKx%2Fi8BjqkAX%2F%2F0h2Mfa0VnZaQl8u5M0O2uOggM71ADAsO3El5jxoZv2AnrI9XSYdQyvLWDNe40z6PlcuFVwXdFVfm6NDchvdFl3k5C3q%2Fl%2BP5gpkaSRMcYi6RmdD%2FcMjgxtQME1AccSh2pxrcKBbzVb9kW8%2FCM5okQ90Zj5zOBzfQZyAp9tG1%2F73pdNYvIegegT8J7i1qwZ9nfu5zvrUCAFIbdbwbcl%2BIbwLf&X-Amz-Signature=aacc2b7664f098f0100843fca563724613661511b18d07caaf4e9813bddc3553&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VKB2UB3E%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181742Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDBxG7nFoIQGAZynmyCKS2myDAFeb5S9tS2guHXZ0Ge1AIhAMKylnHPsxh31J%2Fno9%2FW0F9QqDE1IXOWpAQQJ0MXubrWKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgybwQBNwgLVW4jt7Cwq3AOHCd62vxtRO72MjJCi3kOLUzqj8Ok%2FWO0z2r4nkaR%2By2PXeVPY87KWcGoWIEGRm4VZRGEd42FQrcdUDGbICxOCRB0ryfmkwjNz7MnywAHnemLXhjHKMHBzrSNJPAFgX3mr4tmVmBobub04F5WkduTh%2FEJFdBFJWRaJAXpiziy1Ofr2%2FtDcKaABa60EQkGwyDSjV22MUELpeYzDHIS%2BoI%2BSvP1HcGOzCqbGcnM1M%2FJ9p4P3oBrsEcBm6cHHsooo5Xwem51c2Wrr9bxIltkJ543zQtZL9SPylHMpHw8d3fh9ueyI%2Bdu5YWtTQRHDb34jllcCjUgllDA1Eu%2FZof4u2ZYKT0grtRKkpKjyvOa9t%2BFFx9UEFJtOUcl6x%2FwuTIefdkVP0fd06c30EaJle0bXfpaTfoVqrZhWEeQ2K1DSeoIKQjN2oPUUKgWX8U8aaxupOvUdkM6VZ4WU1Jl6oC36ec1HRDknS9AdSyrNCqtQyeKTpPnM65Ftr3XWEdnNYyg4WNuYF%2Bso5PaWdvq58%2BUEgqO1siUThOQ%2B9ksEU%2BZ9K4AqjKm22zfCMJj07mQB%2BcclHayBLySe7lvANOR%2FtSnqVxtt%2BkdanttanuNB%2BCU2UbXS4m8LWpmvqy8nrGw2MTDKx%2Fi8BjqkAX%2F%2F0h2Mfa0VnZaQl8u5M0O2uOggM71ADAsO3El5jxoZv2AnrI9XSYdQyvLWDNe40z6PlcuFVwXdFVfm6NDchvdFl3k5C3q%2Fl%2BP5gpkaSRMcYi6RmdD%2FcMjgxtQME1AccSh2pxrcKBbzVb9kW8%2FCM5okQ90Zj5zOBzfQZyAp9tG1%2F73pdNYvIegegT8J7i1qwZ9nfu5zvrUCAFIbdbwbcl%2BIbwLf&X-Amz-Signature=018fd64c09d06bdcf7e56eb8a6dbb23d37a0cbc654a47b6a1ad04339428351ea&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
