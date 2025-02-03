

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTYZXUUX%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJGMEQCICgTQUJMZZGFOvvyPbvs8klwnIB9UKksY%2Bf3pXTZOkYCAiB5SUK3jlQv5YLA1lvNLUJYbFHiDrVd%2FPUyltb%2FMwkZ9Cr%2FAwgZEAAaDDYzNzQyMzE4MzgwNSIMnEKD%2FFx2AnVbDtKiKtwDPGhYWybNCVlG0QyECEwqRZxIf7b7yHGCqqXBLbJ9e0dHYBctvGbBx6GOq1E6z09Ug%2BZ%2F3onPW4YOdVH02lWcwbZBS3W3asEUfOk%2BzUh6cqawRLT%2FZ3OGuBgNpQgFoSfy8Z9CajaxEB8IFfSyLRTAv5As%2Fgi3AzWVQib7fyeOFk8wzZjJ8gzIX6tUedfAs%2F0OHnBTSOOO92DeoDMcq7UmlCYX2Z2JHbWF4Ra24BFD%2F5FJqr5W1ge0E0T9%2FvFp6gSKiMSf2qbNlj4KGg%2B8ifNYf8I0ATCIt9%2BSbVTud%2FmOm4FLU%2BkhQs55BM8q64itK8hm4jmkqs4ycwVEsv2SumwPPCBRp5TxoWBRncu1IlodmIlh9REmurfGKDX7AD4XvR7q0g%2FBS7yMwiVtL%2ByHWFFbvHdFSYFXLMkJrKcEuzQLiDidR%2FVzUb4zbEoIfSB2Z1gsBhBqdQB8RqLG94evAsEVFAhSIh6i%2BbUNNBmGvO88sjYwx4zbJPS5zD9YRRFfwe4t3A0vLmlM%2Bi%2BqsqB%2BvgYKs6dejANMhZ8f3wB1%2BkBkkezXlXoZHjPuwJa6eviln%2F1cy2PQI39v7dWyGAK2mz4sGmTj4FriU6VEwUNLjoL045efm6JuVNXXpVvWu4Iw5MqDvQY6pgFKWIcvbUN16fteEjK10CLyRho%2BarwzTDBDe3Z7b9Nu6pnrGLHBee2jXOgoNaTok8EXeofWJ%2BCMOnxXXfASYB%2F%2F87chV1997Wok5rGVJnJeXXrpK7LL07yscQ1iMNim4IK%2FqAXIU7OvDtM02nfMCdBqLQDrzvfQW4PFLx5yDqUL3gMUPtz0BUUcMMv7OdPEW74QR95VeSDCWmxc8w3JQXretyaV5luz&X-Amz-Signature=87f764cabf595e7ba13219448c58b9bc171f09eaa885f8f995f788e74d548e53&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTYZXUUX%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJGMEQCICgTQUJMZZGFOvvyPbvs8klwnIB9UKksY%2Bf3pXTZOkYCAiB5SUK3jlQv5YLA1lvNLUJYbFHiDrVd%2FPUyltb%2FMwkZ9Cr%2FAwgZEAAaDDYzNzQyMzE4MzgwNSIMnEKD%2FFx2AnVbDtKiKtwDPGhYWybNCVlG0QyECEwqRZxIf7b7yHGCqqXBLbJ9e0dHYBctvGbBx6GOq1E6z09Ug%2BZ%2F3onPW4YOdVH02lWcwbZBS3W3asEUfOk%2BzUh6cqawRLT%2FZ3OGuBgNpQgFoSfy8Z9CajaxEB8IFfSyLRTAv5As%2Fgi3AzWVQib7fyeOFk8wzZjJ8gzIX6tUedfAs%2F0OHnBTSOOO92DeoDMcq7UmlCYX2Z2JHbWF4Ra24BFD%2F5FJqr5W1ge0E0T9%2FvFp6gSKiMSf2qbNlj4KGg%2B8ifNYf8I0ATCIt9%2BSbVTud%2FmOm4FLU%2BkhQs55BM8q64itK8hm4jmkqs4ycwVEsv2SumwPPCBRp5TxoWBRncu1IlodmIlh9REmurfGKDX7AD4XvR7q0g%2FBS7yMwiVtL%2ByHWFFbvHdFSYFXLMkJrKcEuzQLiDidR%2FVzUb4zbEoIfSB2Z1gsBhBqdQB8RqLG94evAsEVFAhSIh6i%2BbUNNBmGvO88sjYwx4zbJPS5zD9YRRFfwe4t3A0vLmlM%2Bi%2BqsqB%2BvgYKs6dejANMhZ8f3wB1%2BkBkkezXlXoZHjPuwJa6eviln%2F1cy2PQI39v7dWyGAK2mz4sGmTj4FriU6VEwUNLjoL045efm6JuVNXXpVvWu4Iw5MqDvQY6pgFKWIcvbUN16fteEjK10CLyRho%2BarwzTDBDe3Z7b9Nu6pnrGLHBee2jXOgoNaTok8EXeofWJ%2BCMOnxXXfASYB%2F%2F87chV1997Wok5rGVJnJeXXrpK7LL07yscQ1iMNim4IK%2FqAXIU7OvDtM02nfMCdBqLQDrzvfQW4PFLx5yDqUL3gMUPtz0BUUcMMv7OdPEW74QR95VeSDCWmxc8w3JQXretyaV5luz&X-Amz-Signature=738d6504b6685a4e665403cdbb4032b35b29d617428170ba202acb3e445af121&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTYZXUUX%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJGMEQCICgTQUJMZZGFOvvyPbvs8klwnIB9UKksY%2Bf3pXTZOkYCAiB5SUK3jlQv5YLA1lvNLUJYbFHiDrVd%2FPUyltb%2FMwkZ9Cr%2FAwgZEAAaDDYzNzQyMzE4MzgwNSIMnEKD%2FFx2AnVbDtKiKtwDPGhYWybNCVlG0QyECEwqRZxIf7b7yHGCqqXBLbJ9e0dHYBctvGbBx6GOq1E6z09Ug%2BZ%2F3onPW4YOdVH02lWcwbZBS3W3asEUfOk%2BzUh6cqawRLT%2FZ3OGuBgNpQgFoSfy8Z9CajaxEB8IFfSyLRTAv5As%2Fgi3AzWVQib7fyeOFk8wzZjJ8gzIX6tUedfAs%2F0OHnBTSOOO92DeoDMcq7UmlCYX2Z2JHbWF4Ra24BFD%2F5FJqr5W1ge0E0T9%2FvFp6gSKiMSf2qbNlj4KGg%2B8ifNYf8I0ATCIt9%2BSbVTud%2FmOm4FLU%2BkhQs55BM8q64itK8hm4jmkqs4ycwVEsv2SumwPPCBRp5TxoWBRncu1IlodmIlh9REmurfGKDX7AD4XvR7q0g%2FBS7yMwiVtL%2ByHWFFbvHdFSYFXLMkJrKcEuzQLiDidR%2FVzUb4zbEoIfSB2Z1gsBhBqdQB8RqLG94evAsEVFAhSIh6i%2BbUNNBmGvO88sjYwx4zbJPS5zD9YRRFfwe4t3A0vLmlM%2Bi%2BqsqB%2BvgYKs6dejANMhZ8f3wB1%2BkBkkezXlXoZHjPuwJa6eviln%2F1cy2PQI39v7dWyGAK2mz4sGmTj4FriU6VEwUNLjoL045efm6JuVNXXpVvWu4Iw5MqDvQY6pgFKWIcvbUN16fteEjK10CLyRho%2BarwzTDBDe3Z7b9Nu6pnrGLHBee2jXOgoNaTok8EXeofWJ%2BCMOnxXXfASYB%2F%2F87chV1997Wok5rGVJnJeXXrpK7LL07yscQ1iMNim4IK%2FqAXIU7OvDtM02nfMCdBqLQDrzvfQW4PFLx5yDqUL3gMUPtz0BUUcMMv7OdPEW74QR95VeSDCWmxc8w3JQXretyaV5luz&X-Amz-Signature=323b6fb309436bd682ff1bcbebd2fc5936b242346b1e49d50a77a89b70ea8543&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTYZXUUX%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJGMEQCICgTQUJMZZGFOvvyPbvs8klwnIB9UKksY%2Bf3pXTZOkYCAiB5SUK3jlQv5YLA1lvNLUJYbFHiDrVd%2FPUyltb%2FMwkZ9Cr%2FAwgZEAAaDDYzNzQyMzE4MzgwNSIMnEKD%2FFx2AnVbDtKiKtwDPGhYWybNCVlG0QyECEwqRZxIf7b7yHGCqqXBLbJ9e0dHYBctvGbBx6GOq1E6z09Ug%2BZ%2F3onPW4YOdVH02lWcwbZBS3W3asEUfOk%2BzUh6cqawRLT%2FZ3OGuBgNpQgFoSfy8Z9CajaxEB8IFfSyLRTAv5As%2Fgi3AzWVQib7fyeOFk8wzZjJ8gzIX6tUedfAs%2F0OHnBTSOOO92DeoDMcq7UmlCYX2Z2JHbWF4Ra24BFD%2F5FJqr5W1ge0E0T9%2FvFp6gSKiMSf2qbNlj4KGg%2B8ifNYf8I0ATCIt9%2BSbVTud%2FmOm4FLU%2BkhQs55BM8q64itK8hm4jmkqs4ycwVEsv2SumwPPCBRp5TxoWBRncu1IlodmIlh9REmurfGKDX7AD4XvR7q0g%2FBS7yMwiVtL%2ByHWFFbvHdFSYFXLMkJrKcEuzQLiDidR%2FVzUb4zbEoIfSB2Z1gsBhBqdQB8RqLG94evAsEVFAhSIh6i%2BbUNNBmGvO88sjYwx4zbJPS5zD9YRRFfwe4t3A0vLmlM%2Bi%2BqsqB%2BvgYKs6dejANMhZ8f3wB1%2BkBkkezXlXoZHjPuwJa6eviln%2F1cy2PQI39v7dWyGAK2mz4sGmTj4FriU6VEwUNLjoL045efm6JuVNXXpVvWu4Iw5MqDvQY6pgFKWIcvbUN16fteEjK10CLyRho%2BarwzTDBDe3Z7b9Nu6pnrGLHBee2jXOgoNaTok8EXeofWJ%2BCMOnxXXfASYB%2F%2F87chV1997Wok5rGVJnJeXXrpK7LL07yscQ1iMNim4IK%2FqAXIU7OvDtM02nfMCdBqLQDrzvfQW4PFLx5yDqUL3gMUPtz0BUUcMMv7OdPEW74QR95VeSDCWmxc8w3JQXretyaV5luz&X-Amz-Signature=5b18bb4f2675488c8fcb23c41ec77c0258b41085b3dec72e8c2408e8ed19bb69&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTYZXUUX%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJGMEQCICgTQUJMZZGFOvvyPbvs8klwnIB9UKksY%2Bf3pXTZOkYCAiB5SUK3jlQv5YLA1lvNLUJYbFHiDrVd%2FPUyltb%2FMwkZ9Cr%2FAwgZEAAaDDYzNzQyMzE4MzgwNSIMnEKD%2FFx2AnVbDtKiKtwDPGhYWybNCVlG0QyECEwqRZxIf7b7yHGCqqXBLbJ9e0dHYBctvGbBx6GOq1E6z09Ug%2BZ%2F3onPW4YOdVH02lWcwbZBS3W3asEUfOk%2BzUh6cqawRLT%2FZ3OGuBgNpQgFoSfy8Z9CajaxEB8IFfSyLRTAv5As%2Fgi3AzWVQib7fyeOFk8wzZjJ8gzIX6tUedfAs%2F0OHnBTSOOO92DeoDMcq7UmlCYX2Z2JHbWF4Ra24BFD%2F5FJqr5W1ge0E0T9%2FvFp6gSKiMSf2qbNlj4KGg%2B8ifNYf8I0ATCIt9%2BSbVTud%2FmOm4FLU%2BkhQs55BM8q64itK8hm4jmkqs4ycwVEsv2SumwPPCBRp5TxoWBRncu1IlodmIlh9REmurfGKDX7AD4XvR7q0g%2FBS7yMwiVtL%2ByHWFFbvHdFSYFXLMkJrKcEuzQLiDidR%2FVzUb4zbEoIfSB2Z1gsBhBqdQB8RqLG94evAsEVFAhSIh6i%2BbUNNBmGvO88sjYwx4zbJPS5zD9YRRFfwe4t3A0vLmlM%2Bi%2BqsqB%2BvgYKs6dejANMhZ8f3wB1%2BkBkkezXlXoZHjPuwJa6eviln%2F1cy2PQI39v7dWyGAK2mz4sGmTj4FriU6VEwUNLjoL045efm6JuVNXXpVvWu4Iw5MqDvQY6pgFKWIcvbUN16fteEjK10CLyRho%2BarwzTDBDe3Z7b9Nu6pnrGLHBee2jXOgoNaTok8EXeofWJ%2BCMOnxXXfASYB%2F%2F87chV1997Wok5rGVJnJeXXrpK7LL07yscQ1iMNim4IK%2FqAXIU7OvDtM02nfMCdBqLQDrzvfQW4PFLx5yDqUL3gMUPtz0BUUcMMv7OdPEW74QR95VeSDCWmxc8w3JQXretyaV5luz&X-Amz-Signature=b3c48898b099883450d2c2747219940f1fd96c035a7bb892616526ad59393d73&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTYZXUUX%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJGMEQCICgTQUJMZZGFOvvyPbvs8klwnIB9UKksY%2Bf3pXTZOkYCAiB5SUK3jlQv5YLA1lvNLUJYbFHiDrVd%2FPUyltb%2FMwkZ9Cr%2FAwgZEAAaDDYzNzQyMzE4MzgwNSIMnEKD%2FFx2AnVbDtKiKtwDPGhYWybNCVlG0QyECEwqRZxIf7b7yHGCqqXBLbJ9e0dHYBctvGbBx6GOq1E6z09Ug%2BZ%2F3onPW4YOdVH02lWcwbZBS3W3asEUfOk%2BzUh6cqawRLT%2FZ3OGuBgNpQgFoSfy8Z9CajaxEB8IFfSyLRTAv5As%2Fgi3AzWVQib7fyeOFk8wzZjJ8gzIX6tUedfAs%2F0OHnBTSOOO92DeoDMcq7UmlCYX2Z2JHbWF4Ra24BFD%2F5FJqr5W1ge0E0T9%2FvFp6gSKiMSf2qbNlj4KGg%2B8ifNYf8I0ATCIt9%2BSbVTud%2FmOm4FLU%2BkhQs55BM8q64itK8hm4jmkqs4ycwVEsv2SumwPPCBRp5TxoWBRncu1IlodmIlh9REmurfGKDX7AD4XvR7q0g%2FBS7yMwiVtL%2ByHWFFbvHdFSYFXLMkJrKcEuzQLiDidR%2FVzUb4zbEoIfSB2Z1gsBhBqdQB8RqLG94evAsEVFAhSIh6i%2BbUNNBmGvO88sjYwx4zbJPS5zD9YRRFfwe4t3A0vLmlM%2Bi%2BqsqB%2BvgYKs6dejANMhZ8f3wB1%2BkBkkezXlXoZHjPuwJa6eviln%2F1cy2PQI39v7dWyGAK2mz4sGmTj4FriU6VEwUNLjoL045efm6JuVNXXpVvWu4Iw5MqDvQY6pgFKWIcvbUN16fteEjK10CLyRho%2BarwzTDBDe3Z7b9Nu6pnrGLHBee2jXOgoNaTok8EXeofWJ%2BCMOnxXXfASYB%2F%2F87chV1997Wok5rGVJnJeXXrpK7LL07yscQ1iMNim4IK%2FqAXIU7OvDtM02nfMCdBqLQDrzvfQW4PFLx5yDqUL3gMUPtz0BUUcMMv7OdPEW74QR95VeSDCWmxc8w3JQXretyaV5luz&X-Amz-Signature=f1333d2b31fd2b53379fc2a19644d90a51bfb4b46f5e85ad4df04e68dac0b442&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTYZXUUX%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJGMEQCICgTQUJMZZGFOvvyPbvs8klwnIB9UKksY%2Bf3pXTZOkYCAiB5SUK3jlQv5YLA1lvNLUJYbFHiDrVd%2FPUyltb%2FMwkZ9Cr%2FAwgZEAAaDDYzNzQyMzE4MzgwNSIMnEKD%2FFx2AnVbDtKiKtwDPGhYWybNCVlG0QyECEwqRZxIf7b7yHGCqqXBLbJ9e0dHYBctvGbBx6GOq1E6z09Ug%2BZ%2F3onPW4YOdVH02lWcwbZBS3W3asEUfOk%2BzUh6cqawRLT%2FZ3OGuBgNpQgFoSfy8Z9CajaxEB8IFfSyLRTAv5As%2Fgi3AzWVQib7fyeOFk8wzZjJ8gzIX6tUedfAs%2F0OHnBTSOOO92DeoDMcq7UmlCYX2Z2JHbWF4Ra24BFD%2F5FJqr5W1ge0E0T9%2FvFp6gSKiMSf2qbNlj4KGg%2B8ifNYf8I0ATCIt9%2BSbVTud%2FmOm4FLU%2BkhQs55BM8q64itK8hm4jmkqs4ycwVEsv2SumwPPCBRp5TxoWBRncu1IlodmIlh9REmurfGKDX7AD4XvR7q0g%2FBS7yMwiVtL%2ByHWFFbvHdFSYFXLMkJrKcEuzQLiDidR%2FVzUb4zbEoIfSB2Z1gsBhBqdQB8RqLG94evAsEVFAhSIh6i%2BbUNNBmGvO88sjYwx4zbJPS5zD9YRRFfwe4t3A0vLmlM%2Bi%2BqsqB%2BvgYKs6dejANMhZ8f3wB1%2BkBkkezXlXoZHjPuwJa6eviln%2F1cy2PQI39v7dWyGAK2mz4sGmTj4FriU6VEwUNLjoL045efm6JuVNXXpVvWu4Iw5MqDvQY6pgFKWIcvbUN16fteEjK10CLyRho%2BarwzTDBDe3Z7b9Nu6pnrGLHBee2jXOgoNaTok8EXeofWJ%2BCMOnxXXfASYB%2F%2F87chV1997Wok5rGVJnJeXXrpK7LL07yscQ1iMNim4IK%2FqAXIU7OvDtM02nfMCdBqLQDrzvfQW4PFLx5yDqUL3gMUPtz0BUUcMMv7OdPEW74QR95VeSDCWmxc8w3JQXretyaV5luz&X-Amz-Signature=6a85ecfa36ee54e6af0fca551c9f558346f485881c10aa565437aafe5c63b661&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTYZXUUX%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJGMEQCICgTQUJMZZGFOvvyPbvs8klwnIB9UKksY%2Bf3pXTZOkYCAiB5SUK3jlQv5YLA1lvNLUJYbFHiDrVd%2FPUyltb%2FMwkZ9Cr%2FAwgZEAAaDDYzNzQyMzE4MzgwNSIMnEKD%2FFx2AnVbDtKiKtwDPGhYWybNCVlG0QyECEwqRZxIf7b7yHGCqqXBLbJ9e0dHYBctvGbBx6GOq1E6z09Ug%2BZ%2F3onPW4YOdVH02lWcwbZBS3W3asEUfOk%2BzUh6cqawRLT%2FZ3OGuBgNpQgFoSfy8Z9CajaxEB8IFfSyLRTAv5As%2Fgi3AzWVQib7fyeOFk8wzZjJ8gzIX6tUedfAs%2F0OHnBTSOOO92DeoDMcq7UmlCYX2Z2JHbWF4Ra24BFD%2F5FJqr5W1ge0E0T9%2FvFp6gSKiMSf2qbNlj4KGg%2B8ifNYf8I0ATCIt9%2BSbVTud%2FmOm4FLU%2BkhQs55BM8q64itK8hm4jmkqs4ycwVEsv2SumwPPCBRp5TxoWBRncu1IlodmIlh9REmurfGKDX7AD4XvR7q0g%2FBS7yMwiVtL%2ByHWFFbvHdFSYFXLMkJrKcEuzQLiDidR%2FVzUb4zbEoIfSB2Z1gsBhBqdQB8RqLG94evAsEVFAhSIh6i%2BbUNNBmGvO88sjYwx4zbJPS5zD9YRRFfwe4t3A0vLmlM%2Bi%2BqsqB%2BvgYKs6dejANMhZ8f3wB1%2BkBkkezXlXoZHjPuwJa6eviln%2F1cy2PQI39v7dWyGAK2mz4sGmTj4FriU6VEwUNLjoL045efm6JuVNXXpVvWu4Iw5MqDvQY6pgFKWIcvbUN16fteEjK10CLyRho%2BarwzTDBDe3Z7b9Nu6pnrGLHBee2jXOgoNaTok8EXeofWJ%2BCMOnxXXfASYB%2F%2F87chV1997Wok5rGVJnJeXXrpK7LL07yscQ1iMNim4IK%2FqAXIU7OvDtM02nfMCdBqLQDrzvfQW4PFLx5yDqUL3gMUPtz0BUUcMMv7OdPEW74QR95VeSDCWmxc8w3JQXretyaV5luz&X-Amz-Signature=b369d139db7e60259d1c86ee47f3b73b383c678e91b22d18b10e99feeded81b1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTYZXUUX%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJGMEQCICgTQUJMZZGFOvvyPbvs8klwnIB9UKksY%2Bf3pXTZOkYCAiB5SUK3jlQv5YLA1lvNLUJYbFHiDrVd%2FPUyltb%2FMwkZ9Cr%2FAwgZEAAaDDYzNzQyMzE4MzgwNSIMnEKD%2FFx2AnVbDtKiKtwDPGhYWybNCVlG0QyECEwqRZxIf7b7yHGCqqXBLbJ9e0dHYBctvGbBx6GOq1E6z09Ug%2BZ%2F3onPW4YOdVH02lWcwbZBS3W3asEUfOk%2BzUh6cqawRLT%2FZ3OGuBgNpQgFoSfy8Z9CajaxEB8IFfSyLRTAv5As%2Fgi3AzWVQib7fyeOFk8wzZjJ8gzIX6tUedfAs%2F0OHnBTSOOO92DeoDMcq7UmlCYX2Z2JHbWF4Ra24BFD%2F5FJqr5W1ge0E0T9%2FvFp6gSKiMSf2qbNlj4KGg%2B8ifNYf8I0ATCIt9%2BSbVTud%2FmOm4FLU%2BkhQs55BM8q64itK8hm4jmkqs4ycwVEsv2SumwPPCBRp5TxoWBRncu1IlodmIlh9REmurfGKDX7AD4XvR7q0g%2FBS7yMwiVtL%2ByHWFFbvHdFSYFXLMkJrKcEuzQLiDidR%2FVzUb4zbEoIfSB2Z1gsBhBqdQB8RqLG94evAsEVFAhSIh6i%2BbUNNBmGvO88sjYwx4zbJPS5zD9YRRFfwe4t3A0vLmlM%2Bi%2BqsqB%2BvgYKs6dejANMhZ8f3wB1%2BkBkkezXlXoZHjPuwJa6eviln%2F1cy2PQI39v7dWyGAK2mz4sGmTj4FriU6VEwUNLjoL045efm6JuVNXXpVvWu4Iw5MqDvQY6pgFKWIcvbUN16fteEjK10CLyRho%2BarwzTDBDe3Z7b9Nu6pnrGLHBee2jXOgoNaTok8EXeofWJ%2BCMOnxXXfASYB%2F%2F87chV1997Wok5rGVJnJeXXrpK7LL07yscQ1iMNim4IK%2FqAXIU7OvDtM02nfMCdBqLQDrzvfQW4PFLx5yDqUL3gMUPtz0BUUcMMv7OdPEW74QR95VeSDCWmxc8w3JQXretyaV5luz&X-Amz-Signature=bc99fdafcbda683d39e68ed0c6013436800a5e6eafc6764dab8d9733d5e0ed28&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TIUNDNC7%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJHMEUCIQDmqHF0AZFAKuUaCGhuOVAaU9HQhqV2mQQQJ6wbz0HkwAIgGknjTi%2BFTqE6ArK1FEJuoMNFB1ep%2FQVCT7oY0S%2B9kJQq%2FwMIGRAAGgw2Mzc0MjMxODM4MDUiDGrH9t77doaeDAm%2FUyrcA6aGCfJtLXnzOiExChT6lEDT2iw5FnG59UpoRNRzGgH67i0kOXMes%2B1iEq04N0g1OefHhKbGby9swODQ681ATWbtmQQnpSwP%2FUjGYdV90%2F5q03591UuP8mGKHjR9KvQHcxg7jDpyfBQBGqnp4WgV6FhnRHpfK9yU7ML33l8H9PbP8V44mRDgRhULbul4GMet%2BSbpFZKwdkZR9aw%2BZIiFU3iCzF8JIFQq%2BFeKBOwuz5SGnOqu6VdChmlUwnq4%2B4iSvDfa6VdISz%2F4BIqtbEB6u%2FfFXwW873uezo2KPgISMwVwW6RX6u4eSjzb7d4%2Bzlc6axD6LiAxRBEx%2Bf4QUwr%2FAcBpRQmODzNZnObateSm6gsR4yQxOUdm%2BFkny%2FPTeB%2F4dlupQyvRQLu1uBlZ4G0vH7GBsq2f6Et3gyktngyM4O%2B%2BSiRGo1R%2BmW4V2qdVEbfcD%2F1uCzFFNvYyKn8ifPLZiZ6Fk5HvHyMEYlxmCSSDZseoj42YaOy%2FH4i4oP7p3ixH%2FavBVM5v0pzngX%2FBjtO7U2CVqv5fgtTL0q6lLWAaMoAOrPu2no3cm2lKYkA3gghiLbqEEHrwZorixWH%2F6Qb96C6FfWRTRNIfy3wmxOvu4VK5S7VJuDvTWiyYah54MKfKg70GOqUBpzUK5ivXExoONs%2FcoP47Us1mMiBRv3qs87mwzdHD3XvR63RR6UFxAKhnRJxWCXcJY7rhci7VO1w43m583blP%2Ftu2kHObnWOnL230hLks9%2BWhPLwCH481%2F%2BcTGOpsf1E7Sko0%2BnUteaPWdvOkLP1KfNd5phgC2%2BnnFm6fR%2BNBtD31xD4qOzpYSB0zoP4eeMFQ8P9G98Mwax2e%2FqvxFbCAM4uq8fQO&X-Amz-Signature=b638d9ba43e7c0455e1e63c3904616ce74da937fb7858130d7937886f686fba3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TIUNDNC7%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJHMEUCIQDmqHF0AZFAKuUaCGhuOVAaU9HQhqV2mQQQJ6wbz0HkwAIgGknjTi%2BFTqE6ArK1FEJuoMNFB1ep%2FQVCT7oY0S%2B9kJQq%2FwMIGRAAGgw2Mzc0MjMxODM4MDUiDGrH9t77doaeDAm%2FUyrcA6aGCfJtLXnzOiExChT6lEDT2iw5FnG59UpoRNRzGgH67i0kOXMes%2B1iEq04N0g1OefHhKbGby9swODQ681ATWbtmQQnpSwP%2FUjGYdV90%2F5q03591UuP8mGKHjR9KvQHcxg7jDpyfBQBGqnp4WgV6FhnRHpfK9yU7ML33l8H9PbP8V44mRDgRhULbul4GMet%2BSbpFZKwdkZR9aw%2BZIiFU3iCzF8JIFQq%2BFeKBOwuz5SGnOqu6VdChmlUwnq4%2B4iSvDfa6VdISz%2F4BIqtbEB6u%2FfFXwW873uezo2KPgISMwVwW6RX6u4eSjzb7d4%2Bzlc6axD6LiAxRBEx%2Bf4QUwr%2FAcBpRQmODzNZnObateSm6gsR4yQxOUdm%2BFkny%2FPTeB%2F4dlupQyvRQLu1uBlZ4G0vH7GBsq2f6Et3gyktngyM4O%2B%2BSiRGo1R%2BmW4V2qdVEbfcD%2F1uCzFFNvYyKn8ifPLZiZ6Fk5HvHyMEYlxmCSSDZseoj42YaOy%2FH4i4oP7p3ixH%2FavBVM5v0pzngX%2FBjtO7U2CVqv5fgtTL0q6lLWAaMoAOrPu2no3cm2lKYkA3gghiLbqEEHrwZorixWH%2F6Qb96C6FfWRTRNIfy3wmxOvu4VK5S7VJuDvTWiyYah54MKfKg70GOqUBpzUK5ivXExoONs%2FcoP47Us1mMiBRv3qs87mwzdHD3XvR63RR6UFxAKhnRJxWCXcJY7rhci7VO1w43m583blP%2Ftu2kHObnWOnL230hLks9%2BWhPLwCH481%2F%2BcTGOpsf1E7Sko0%2BnUteaPWdvOkLP1KfNd5phgC2%2BnnFm6fR%2BNBtD31xD4qOzpYSB0zoP4eeMFQ8P9G98Mwax2e%2FqvxFbCAM4uq8fQO&X-Amz-Signature=16524b9148f7d706a25d2e6d22298a14116667f9133ff3d921a0b971d46781bd&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
