

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YSWG2ABC%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQC3ZEab6eVgGaxo%2Bh0hjifFLFMKwN1oJmfuNbH4sSEDpwIgUgWApQwxt%2FMCSVWYn2NjgEC8lIgTkU9fvkJxKlMIVhwq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDDEAKKbBO7OuJp7BIyrcA%2FIZ%2FMQN5wif36B1B7oVmNnyEsq2f5d7pYOLXNmqAVkrsHh87y%2BiSHywKNko7ibYet%2FWqcUspEzvfybx5Y%2BRDXFOVUq5q%2FDMgJgA%2FZ7BVq1Ya%2F9%2BVK4CjomInF81tGif57yJ0CGjhXLCITsX4CLEdiubIYqoiF%2FwoWHY2EqijC0HXiMFh4zS%2F8OObnpMQkRlyNnSIoOZ0dCvrAZdLlmVWnRQMQY0%2FkRdAEuBXxf%2BmLIUI3fnBjQsJfvEDTQRhUrvz1OqCEvLMCnCTMHq0FihksqO6zvoyLEyePC%2Bx530aD9vpys%2FrZ1Klr7OC2XfnjsAQElgDEXo3gvRo3TIf1mhEKVfmcJ3sCAf7ZBNf3ubmAjAhJdTuLHJ7%2FW7xqnajKsXOzC4irmD%2FL%2BEho6quTCIuE%2FYjx84e3pjdPLDiDCMU4DNYQvnguR3Gj1EYpaouXTDKJfU6DOkUsQdluNhfdq6RT4TlL6dCNDCiqDxMAZIDoQQvtsuNex8Qb0MZ5bQggEHBqNOiAJVNCmg4Xnyf2UaAw9W2W2t6yC%2BFvi6fHETDDKAdJq90dcB72mfkGpUzAV9CKBGdPhEX2EmY%2BuUn1pAv4hiBg4lLwC9xUPDbXjHv4CWf8qyAm4CQ1XivnIeMJq%2Fhr0GOqUBYa7XoS8%2FaSDe4zgKzh6IJDJs8vHSC6HggkNvp352UbK%2Ft61EhCQ8DKNlv3LpBYbWbpUCJxnLfMkBR3KRwW5Ai5pWybieDd8JSi8sI4kotmN6U%2BiBUqcbixn9qg1hY4V35F361AZ1Q4DKsvrGagc36sv8%2Ba53rD0hN5c%2BTTCxgEO3LPS5OSEY8Sdqdo%2BSQTiCfN7tN0yCUSPbpvDU55fq2CF5lMNl&X-Amz-Signature=77238067b33df9c70970c636457f1a04817b2722c67014bdb679a93e72a307e5&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YSWG2ABC%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQC3ZEab6eVgGaxo%2Bh0hjifFLFMKwN1oJmfuNbH4sSEDpwIgUgWApQwxt%2FMCSVWYn2NjgEC8lIgTkU9fvkJxKlMIVhwq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDDEAKKbBO7OuJp7BIyrcA%2FIZ%2FMQN5wif36B1B7oVmNnyEsq2f5d7pYOLXNmqAVkrsHh87y%2BiSHywKNko7ibYet%2FWqcUspEzvfybx5Y%2BRDXFOVUq5q%2FDMgJgA%2FZ7BVq1Ya%2F9%2BVK4CjomInF81tGif57yJ0CGjhXLCITsX4CLEdiubIYqoiF%2FwoWHY2EqijC0HXiMFh4zS%2F8OObnpMQkRlyNnSIoOZ0dCvrAZdLlmVWnRQMQY0%2FkRdAEuBXxf%2BmLIUI3fnBjQsJfvEDTQRhUrvz1OqCEvLMCnCTMHq0FihksqO6zvoyLEyePC%2Bx530aD9vpys%2FrZ1Klr7OC2XfnjsAQElgDEXo3gvRo3TIf1mhEKVfmcJ3sCAf7ZBNf3ubmAjAhJdTuLHJ7%2FW7xqnajKsXOzC4irmD%2FL%2BEho6quTCIuE%2FYjx84e3pjdPLDiDCMU4DNYQvnguR3Gj1EYpaouXTDKJfU6DOkUsQdluNhfdq6RT4TlL6dCNDCiqDxMAZIDoQQvtsuNex8Qb0MZ5bQggEHBqNOiAJVNCmg4Xnyf2UaAw9W2W2t6yC%2BFvi6fHETDDKAdJq90dcB72mfkGpUzAV9CKBGdPhEX2EmY%2BuUn1pAv4hiBg4lLwC9xUPDbXjHv4CWf8qyAm4CQ1XivnIeMJq%2Fhr0GOqUBYa7XoS8%2FaSDe4zgKzh6IJDJs8vHSC6HggkNvp352UbK%2Ft61EhCQ8DKNlv3LpBYbWbpUCJxnLfMkBR3KRwW5Ai5pWybieDd8JSi8sI4kotmN6U%2BiBUqcbixn9qg1hY4V35F361AZ1Q4DKsvrGagc36sv8%2Ba53rD0hN5c%2BTTCxgEO3LPS5OSEY8Sdqdo%2BSQTiCfN7tN0yCUSPbpvDU55fq2CF5lMNl&X-Amz-Signature=d55174d9f48a97566f248e80b0121702a021c91a8bc38065d49630de926d9cc7&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YSWG2ABC%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQC3ZEab6eVgGaxo%2Bh0hjifFLFMKwN1oJmfuNbH4sSEDpwIgUgWApQwxt%2FMCSVWYn2NjgEC8lIgTkU9fvkJxKlMIVhwq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDDEAKKbBO7OuJp7BIyrcA%2FIZ%2FMQN5wif36B1B7oVmNnyEsq2f5d7pYOLXNmqAVkrsHh87y%2BiSHywKNko7ibYet%2FWqcUspEzvfybx5Y%2BRDXFOVUq5q%2FDMgJgA%2FZ7BVq1Ya%2F9%2BVK4CjomInF81tGif57yJ0CGjhXLCITsX4CLEdiubIYqoiF%2FwoWHY2EqijC0HXiMFh4zS%2F8OObnpMQkRlyNnSIoOZ0dCvrAZdLlmVWnRQMQY0%2FkRdAEuBXxf%2BmLIUI3fnBjQsJfvEDTQRhUrvz1OqCEvLMCnCTMHq0FihksqO6zvoyLEyePC%2Bx530aD9vpys%2FrZ1Klr7OC2XfnjsAQElgDEXo3gvRo3TIf1mhEKVfmcJ3sCAf7ZBNf3ubmAjAhJdTuLHJ7%2FW7xqnajKsXOzC4irmD%2FL%2BEho6quTCIuE%2FYjx84e3pjdPLDiDCMU4DNYQvnguR3Gj1EYpaouXTDKJfU6DOkUsQdluNhfdq6RT4TlL6dCNDCiqDxMAZIDoQQvtsuNex8Qb0MZ5bQggEHBqNOiAJVNCmg4Xnyf2UaAw9W2W2t6yC%2BFvi6fHETDDKAdJq90dcB72mfkGpUzAV9CKBGdPhEX2EmY%2BuUn1pAv4hiBg4lLwC9xUPDbXjHv4CWf8qyAm4CQ1XivnIeMJq%2Fhr0GOqUBYa7XoS8%2FaSDe4zgKzh6IJDJs8vHSC6HggkNvp352UbK%2Ft61EhCQ8DKNlv3LpBYbWbpUCJxnLfMkBR3KRwW5Ai5pWybieDd8JSi8sI4kotmN6U%2BiBUqcbixn9qg1hY4V35F361AZ1Q4DKsvrGagc36sv8%2Ba53rD0hN5c%2BTTCxgEO3LPS5OSEY8Sdqdo%2BSQTiCfN7tN0yCUSPbpvDU55fq2CF5lMNl&X-Amz-Signature=c53b2602d2632fee5a520f4019c88fc27054ecd4dc0aa9a4eb81fe4e408d6fb4&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YSWG2ABC%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQC3ZEab6eVgGaxo%2Bh0hjifFLFMKwN1oJmfuNbH4sSEDpwIgUgWApQwxt%2FMCSVWYn2NjgEC8lIgTkU9fvkJxKlMIVhwq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDDEAKKbBO7OuJp7BIyrcA%2FIZ%2FMQN5wif36B1B7oVmNnyEsq2f5d7pYOLXNmqAVkrsHh87y%2BiSHywKNko7ibYet%2FWqcUspEzvfybx5Y%2BRDXFOVUq5q%2FDMgJgA%2FZ7BVq1Ya%2F9%2BVK4CjomInF81tGif57yJ0CGjhXLCITsX4CLEdiubIYqoiF%2FwoWHY2EqijC0HXiMFh4zS%2F8OObnpMQkRlyNnSIoOZ0dCvrAZdLlmVWnRQMQY0%2FkRdAEuBXxf%2BmLIUI3fnBjQsJfvEDTQRhUrvz1OqCEvLMCnCTMHq0FihksqO6zvoyLEyePC%2Bx530aD9vpys%2FrZ1Klr7OC2XfnjsAQElgDEXo3gvRo3TIf1mhEKVfmcJ3sCAf7ZBNf3ubmAjAhJdTuLHJ7%2FW7xqnajKsXOzC4irmD%2FL%2BEho6quTCIuE%2FYjx84e3pjdPLDiDCMU4DNYQvnguR3Gj1EYpaouXTDKJfU6DOkUsQdluNhfdq6RT4TlL6dCNDCiqDxMAZIDoQQvtsuNex8Qb0MZ5bQggEHBqNOiAJVNCmg4Xnyf2UaAw9W2W2t6yC%2BFvi6fHETDDKAdJq90dcB72mfkGpUzAV9CKBGdPhEX2EmY%2BuUn1pAv4hiBg4lLwC9xUPDbXjHv4CWf8qyAm4CQ1XivnIeMJq%2Fhr0GOqUBYa7XoS8%2FaSDe4zgKzh6IJDJs8vHSC6HggkNvp352UbK%2Ft61EhCQ8DKNlv3LpBYbWbpUCJxnLfMkBR3KRwW5Ai5pWybieDd8JSi8sI4kotmN6U%2BiBUqcbixn9qg1hY4V35F361AZ1Q4DKsvrGagc36sv8%2Ba53rD0hN5c%2BTTCxgEO3LPS5OSEY8Sdqdo%2BSQTiCfN7tN0yCUSPbpvDU55fq2CF5lMNl&X-Amz-Signature=00f5277b82ae88c0467f6af236fea7511560659f80234944950e8dacd4199d82&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YSWG2ABC%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQC3ZEab6eVgGaxo%2Bh0hjifFLFMKwN1oJmfuNbH4sSEDpwIgUgWApQwxt%2FMCSVWYn2NjgEC8lIgTkU9fvkJxKlMIVhwq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDDEAKKbBO7OuJp7BIyrcA%2FIZ%2FMQN5wif36B1B7oVmNnyEsq2f5d7pYOLXNmqAVkrsHh87y%2BiSHywKNko7ibYet%2FWqcUspEzvfybx5Y%2BRDXFOVUq5q%2FDMgJgA%2FZ7BVq1Ya%2F9%2BVK4CjomInF81tGif57yJ0CGjhXLCITsX4CLEdiubIYqoiF%2FwoWHY2EqijC0HXiMFh4zS%2F8OObnpMQkRlyNnSIoOZ0dCvrAZdLlmVWnRQMQY0%2FkRdAEuBXxf%2BmLIUI3fnBjQsJfvEDTQRhUrvz1OqCEvLMCnCTMHq0FihksqO6zvoyLEyePC%2Bx530aD9vpys%2FrZ1Klr7OC2XfnjsAQElgDEXo3gvRo3TIf1mhEKVfmcJ3sCAf7ZBNf3ubmAjAhJdTuLHJ7%2FW7xqnajKsXOzC4irmD%2FL%2BEho6quTCIuE%2FYjx84e3pjdPLDiDCMU4DNYQvnguR3Gj1EYpaouXTDKJfU6DOkUsQdluNhfdq6RT4TlL6dCNDCiqDxMAZIDoQQvtsuNex8Qb0MZ5bQggEHBqNOiAJVNCmg4Xnyf2UaAw9W2W2t6yC%2BFvi6fHETDDKAdJq90dcB72mfkGpUzAV9CKBGdPhEX2EmY%2BuUn1pAv4hiBg4lLwC9xUPDbXjHv4CWf8qyAm4CQ1XivnIeMJq%2Fhr0GOqUBYa7XoS8%2FaSDe4zgKzh6IJDJs8vHSC6HggkNvp352UbK%2Ft61EhCQ8DKNlv3LpBYbWbpUCJxnLfMkBR3KRwW5Ai5pWybieDd8JSi8sI4kotmN6U%2BiBUqcbixn9qg1hY4V35F361AZ1Q4DKsvrGagc36sv8%2Ba53rD0hN5c%2BTTCxgEO3LPS5OSEY8Sdqdo%2BSQTiCfN7tN0yCUSPbpvDU55fq2CF5lMNl&X-Amz-Signature=0c03c0ac3deed9b6d6024b9023c9c7c650cefe594517ede3a83f381bfceb9c37&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YSWG2ABC%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQC3ZEab6eVgGaxo%2Bh0hjifFLFMKwN1oJmfuNbH4sSEDpwIgUgWApQwxt%2FMCSVWYn2NjgEC8lIgTkU9fvkJxKlMIVhwq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDDEAKKbBO7OuJp7BIyrcA%2FIZ%2FMQN5wif36B1B7oVmNnyEsq2f5d7pYOLXNmqAVkrsHh87y%2BiSHywKNko7ibYet%2FWqcUspEzvfybx5Y%2BRDXFOVUq5q%2FDMgJgA%2FZ7BVq1Ya%2F9%2BVK4CjomInF81tGif57yJ0CGjhXLCITsX4CLEdiubIYqoiF%2FwoWHY2EqijC0HXiMFh4zS%2F8OObnpMQkRlyNnSIoOZ0dCvrAZdLlmVWnRQMQY0%2FkRdAEuBXxf%2BmLIUI3fnBjQsJfvEDTQRhUrvz1OqCEvLMCnCTMHq0FihksqO6zvoyLEyePC%2Bx530aD9vpys%2FrZ1Klr7OC2XfnjsAQElgDEXo3gvRo3TIf1mhEKVfmcJ3sCAf7ZBNf3ubmAjAhJdTuLHJ7%2FW7xqnajKsXOzC4irmD%2FL%2BEho6quTCIuE%2FYjx84e3pjdPLDiDCMU4DNYQvnguR3Gj1EYpaouXTDKJfU6DOkUsQdluNhfdq6RT4TlL6dCNDCiqDxMAZIDoQQvtsuNex8Qb0MZ5bQggEHBqNOiAJVNCmg4Xnyf2UaAw9W2W2t6yC%2BFvi6fHETDDKAdJq90dcB72mfkGpUzAV9CKBGdPhEX2EmY%2BuUn1pAv4hiBg4lLwC9xUPDbXjHv4CWf8qyAm4CQ1XivnIeMJq%2Fhr0GOqUBYa7XoS8%2FaSDe4zgKzh6IJDJs8vHSC6HggkNvp352UbK%2Ft61EhCQ8DKNlv3LpBYbWbpUCJxnLfMkBR3KRwW5Ai5pWybieDd8JSi8sI4kotmN6U%2BiBUqcbixn9qg1hY4V35F361AZ1Q4DKsvrGagc36sv8%2Ba53rD0hN5c%2BTTCxgEO3LPS5OSEY8Sdqdo%2BSQTiCfN7tN0yCUSPbpvDU55fq2CF5lMNl&X-Amz-Signature=2871b5e7d5783797a7713f24a0e411acddbd8523f0b02be0764684e6912c323d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YSWG2ABC%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQC3ZEab6eVgGaxo%2Bh0hjifFLFMKwN1oJmfuNbH4sSEDpwIgUgWApQwxt%2FMCSVWYn2NjgEC8lIgTkU9fvkJxKlMIVhwq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDDEAKKbBO7OuJp7BIyrcA%2FIZ%2FMQN5wif36B1B7oVmNnyEsq2f5d7pYOLXNmqAVkrsHh87y%2BiSHywKNko7ibYet%2FWqcUspEzvfybx5Y%2BRDXFOVUq5q%2FDMgJgA%2FZ7BVq1Ya%2F9%2BVK4CjomInF81tGif57yJ0CGjhXLCITsX4CLEdiubIYqoiF%2FwoWHY2EqijC0HXiMFh4zS%2F8OObnpMQkRlyNnSIoOZ0dCvrAZdLlmVWnRQMQY0%2FkRdAEuBXxf%2BmLIUI3fnBjQsJfvEDTQRhUrvz1OqCEvLMCnCTMHq0FihksqO6zvoyLEyePC%2Bx530aD9vpys%2FrZ1Klr7OC2XfnjsAQElgDEXo3gvRo3TIf1mhEKVfmcJ3sCAf7ZBNf3ubmAjAhJdTuLHJ7%2FW7xqnajKsXOzC4irmD%2FL%2BEho6quTCIuE%2FYjx84e3pjdPLDiDCMU4DNYQvnguR3Gj1EYpaouXTDKJfU6DOkUsQdluNhfdq6RT4TlL6dCNDCiqDxMAZIDoQQvtsuNex8Qb0MZ5bQggEHBqNOiAJVNCmg4Xnyf2UaAw9W2W2t6yC%2BFvi6fHETDDKAdJq90dcB72mfkGpUzAV9CKBGdPhEX2EmY%2BuUn1pAv4hiBg4lLwC9xUPDbXjHv4CWf8qyAm4CQ1XivnIeMJq%2Fhr0GOqUBYa7XoS8%2FaSDe4zgKzh6IJDJs8vHSC6HggkNvp352UbK%2Ft61EhCQ8DKNlv3LpBYbWbpUCJxnLfMkBR3KRwW5Ai5pWybieDd8JSi8sI4kotmN6U%2BiBUqcbixn9qg1hY4V35F361AZ1Q4DKsvrGagc36sv8%2Ba53rD0hN5c%2BTTCxgEO3LPS5OSEY8Sdqdo%2BSQTiCfN7tN0yCUSPbpvDU55fq2CF5lMNl&X-Amz-Signature=60ba6bb5f7578537bdfd14bc3f6cff4582c9c0df41f61623e101a18c6a595b79&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YSWG2ABC%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQC3ZEab6eVgGaxo%2Bh0hjifFLFMKwN1oJmfuNbH4sSEDpwIgUgWApQwxt%2FMCSVWYn2NjgEC8lIgTkU9fvkJxKlMIVhwq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDDEAKKbBO7OuJp7BIyrcA%2FIZ%2FMQN5wif36B1B7oVmNnyEsq2f5d7pYOLXNmqAVkrsHh87y%2BiSHywKNko7ibYet%2FWqcUspEzvfybx5Y%2BRDXFOVUq5q%2FDMgJgA%2FZ7BVq1Ya%2F9%2BVK4CjomInF81tGif57yJ0CGjhXLCITsX4CLEdiubIYqoiF%2FwoWHY2EqijC0HXiMFh4zS%2F8OObnpMQkRlyNnSIoOZ0dCvrAZdLlmVWnRQMQY0%2FkRdAEuBXxf%2BmLIUI3fnBjQsJfvEDTQRhUrvz1OqCEvLMCnCTMHq0FihksqO6zvoyLEyePC%2Bx530aD9vpys%2FrZ1Klr7OC2XfnjsAQElgDEXo3gvRo3TIf1mhEKVfmcJ3sCAf7ZBNf3ubmAjAhJdTuLHJ7%2FW7xqnajKsXOzC4irmD%2FL%2BEho6quTCIuE%2FYjx84e3pjdPLDiDCMU4DNYQvnguR3Gj1EYpaouXTDKJfU6DOkUsQdluNhfdq6RT4TlL6dCNDCiqDxMAZIDoQQvtsuNex8Qb0MZ5bQggEHBqNOiAJVNCmg4Xnyf2UaAw9W2W2t6yC%2BFvi6fHETDDKAdJq90dcB72mfkGpUzAV9CKBGdPhEX2EmY%2BuUn1pAv4hiBg4lLwC9xUPDbXjHv4CWf8qyAm4CQ1XivnIeMJq%2Fhr0GOqUBYa7XoS8%2FaSDe4zgKzh6IJDJs8vHSC6HggkNvp352UbK%2Ft61EhCQ8DKNlv3LpBYbWbpUCJxnLfMkBR3KRwW5Ai5pWybieDd8JSi8sI4kotmN6U%2BiBUqcbixn9qg1hY4V35F361AZ1Q4DKsvrGagc36sv8%2Ba53rD0hN5c%2BTTCxgEO3LPS5OSEY8Sdqdo%2BSQTiCfN7tN0yCUSPbpvDU55fq2CF5lMNl&X-Amz-Signature=b2b325e0cffdc696d6d5c8c29034cfaab5a1809cd56f1a954bf283f4e9dfd34a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YSWG2ABC%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQC3ZEab6eVgGaxo%2Bh0hjifFLFMKwN1oJmfuNbH4sSEDpwIgUgWApQwxt%2FMCSVWYn2NjgEC8lIgTkU9fvkJxKlMIVhwq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDDEAKKbBO7OuJp7BIyrcA%2FIZ%2FMQN5wif36B1B7oVmNnyEsq2f5d7pYOLXNmqAVkrsHh87y%2BiSHywKNko7ibYet%2FWqcUspEzvfybx5Y%2BRDXFOVUq5q%2FDMgJgA%2FZ7BVq1Ya%2F9%2BVK4CjomInF81tGif57yJ0CGjhXLCITsX4CLEdiubIYqoiF%2FwoWHY2EqijC0HXiMFh4zS%2F8OObnpMQkRlyNnSIoOZ0dCvrAZdLlmVWnRQMQY0%2FkRdAEuBXxf%2BmLIUI3fnBjQsJfvEDTQRhUrvz1OqCEvLMCnCTMHq0FihksqO6zvoyLEyePC%2Bx530aD9vpys%2FrZ1Klr7OC2XfnjsAQElgDEXo3gvRo3TIf1mhEKVfmcJ3sCAf7ZBNf3ubmAjAhJdTuLHJ7%2FW7xqnajKsXOzC4irmD%2FL%2BEho6quTCIuE%2FYjx84e3pjdPLDiDCMU4DNYQvnguR3Gj1EYpaouXTDKJfU6DOkUsQdluNhfdq6RT4TlL6dCNDCiqDxMAZIDoQQvtsuNex8Qb0MZ5bQggEHBqNOiAJVNCmg4Xnyf2UaAw9W2W2t6yC%2BFvi6fHETDDKAdJq90dcB72mfkGpUzAV9CKBGdPhEX2EmY%2BuUn1pAv4hiBg4lLwC9xUPDbXjHv4CWf8qyAm4CQ1XivnIeMJq%2Fhr0GOqUBYa7XoS8%2FaSDe4zgKzh6IJDJs8vHSC6HggkNvp352UbK%2Ft61EhCQ8DKNlv3LpBYbWbpUCJxnLfMkBR3KRwW5Ai5pWybieDd8JSi8sI4kotmN6U%2BiBUqcbixn9qg1hY4V35F361AZ1Q4DKsvrGagc36sv8%2Ba53rD0hN5c%2BTTCxgEO3LPS5OSEY8Sdqdo%2BSQTiCfN7tN0yCUSPbpvDU55fq2CF5lMNl&X-Amz-Signature=35a0e1b4a3823bd6ae1308425a28e6e7fbf23d7f79a9098d6116ad900ec7fae9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662LMYKU6B%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJGMEQCIHh%2Bdr5LOaCGXC%2BMtslJKGGmp4RckuSPw8%2BqG9QsCYgMAiB1x6VN8Ym629oHhXi8KHYnbcHtA0jCJvtkls2inhUPLSr%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIMKQv25%2BpXmfwWoLyzKtwDBfrdZwOWPTwB6uK1X66DMw%2FamvtPwrt17c0UAwGaNLU1M7k2aKeUYmg7aVqLzaFADYT%2FbVg21vK8Nr0C4haIzx89kW4CiG%2BkHDUy%2FAXn86iQ2bvKLCznhqsJ9fYW8jpkglkZnW3fCVJdrORCuOtICJ1TzpMZSgLk%2BMlc5MvwIVmf489AQLX5hz19Um%2BaJtE8cMjPFi3M0fnOW8tH84Cw1H%2Fsvbqu9JGc%2Bt%2BksVE6uEB9%2BYg2zzg%2BRTKQtBZCTldrg58bwCDa9qJv%2FE%2Bwyjmw5BHoHqEG1ECpFKQs5wjWA%2Btb1MGJVwgIpZ43ZKcCFx75ZGDgptZ8NS3uCiakanCAA1dflh6TiHjhrsWFnVJDvaaLVi8gZIeYgbN2cxRtLqgiHA4t2tJ0EbLZspiTghykUxoAh2iBFk19hxqGypup9v4qDw9Lr8Q0gmaFKSzMTXJTdkoJBWNQsDf%2BP2Ecumz0k203Hy9tAVrMJnO5MgYz%2BojoEozRq%2B6QRjKID7Ou6opBzLVPP55mX2vaPm53yLy%2BC4ht3q1vsEUqYuMvXw3%2BnqcN%2F7HKS%2FN8w4adxxq0pVsRvkkNsEL8wVIfZlB3zBGwMkeuccwlGeuyqCoUBkrUeZ1e9NVIGHyMhr0qVAQw0r6GvQY6pgEiq1rQ08S%2FtmVzsztuO4NxvogureaQVseY68GqAn%2BCxIjYTGqhonCom4cI6OZFdfMD3MB1SBoiUuHP9ww1pWuLAXUdksCxzyUxYuV6WZSJmcOSK3bYuvfzTCX2P%2FJ8kQUjVlVTJXwW4hWw7Ioxv3WLXTwtxeS%2BW98TM%2Bl781KpxDkbgs1vx8wzf2SPrJpvX9j3rOOYwHpusadZfFqk7szx0Exs7wgS&X-Amz-Signature=f8d289473abfbfc3e72f022a11b3d2cd2a5e5fdd84a5d6559687a904530e1223&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662LMYKU6B%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJGMEQCIHh%2Bdr5LOaCGXC%2BMtslJKGGmp4RckuSPw8%2BqG9QsCYgMAiB1x6VN8Ym629oHhXi8KHYnbcHtA0jCJvtkls2inhUPLSr%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIMKQv25%2BpXmfwWoLyzKtwDBfrdZwOWPTwB6uK1X66DMw%2FamvtPwrt17c0UAwGaNLU1M7k2aKeUYmg7aVqLzaFADYT%2FbVg21vK8Nr0C4haIzx89kW4CiG%2BkHDUy%2FAXn86iQ2bvKLCznhqsJ9fYW8jpkglkZnW3fCVJdrORCuOtICJ1TzpMZSgLk%2BMlc5MvwIVmf489AQLX5hz19Um%2BaJtE8cMjPFi3M0fnOW8tH84Cw1H%2Fsvbqu9JGc%2Bt%2BksVE6uEB9%2BYg2zzg%2BRTKQtBZCTldrg58bwCDa9qJv%2FE%2Bwyjmw5BHoHqEG1ECpFKQs5wjWA%2Btb1MGJVwgIpZ43ZKcCFx75ZGDgptZ8NS3uCiakanCAA1dflh6TiHjhrsWFnVJDvaaLVi8gZIeYgbN2cxRtLqgiHA4t2tJ0EbLZspiTghykUxoAh2iBFk19hxqGypup9v4qDw9Lr8Q0gmaFKSzMTXJTdkoJBWNQsDf%2BP2Ecumz0k203Hy9tAVrMJnO5MgYz%2BojoEozRq%2B6QRjKID7Ou6opBzLVPP55mX2vaPm53yLy%2BC4ht3q1vsEUqYuMvXw3%2BnqcN%2F7HKS%2FN8w4adxxq0pVsRvkkNsEL8wVIfZlB3zBGwMkeuccwlGeuyqCoUBkrUeZ1e9NVIGHyMhr0qVAQw0r6GvQY6pgEiq1rQ08S%2FtmVzsztuO4NxvogureaQVseY68GqAn%2BCxIjYTGqhonCom4cI6OZFdfMD3MB1SBoiUuHP9ww1pWuLAXUdksCxzyUxYuV6WZSJmcOSK3bYuvfzTCX2P%2FJ8kQUjVlVTJXwW4hWw7Ioxv3WLXTwtxeS%2BW98TM%2Bl781KpxDkbgs1vx8wzf2SPrJpvX9j3rOOYwHpusadZfFqk7szx0Exs7wgS&X-Amz-Signature=3eaa45caec9b082b95d31edcbe1b690e78bf6bc045c273e4bdb7110ad58cb655&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
