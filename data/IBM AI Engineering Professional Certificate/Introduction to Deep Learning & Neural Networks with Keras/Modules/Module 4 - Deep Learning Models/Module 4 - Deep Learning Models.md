

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46657OSPINF%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJGMEQCIH%2F1nit5NFQBOBc0SLbAYLxTrEaD7IMMA4wXR%2BPLLcBXAiAhWm%2FLNexfPVwERLn9hpfoApmY%2FiUTOR5NNdG%2BOaZFbSr%2FAwhHEAAaDDYzNzQyMzE4MzgwNSIMgnMuPLzfodD1wFv0KtwDbzOVVSCBJfTh8ZIPEcn0CLf261JSA6s2QpNIAH8%2FYy9RhefUXmQNLGZmHECvaMFnzs%2Fj95dXjojr8oPUYi%2ByW5tmfocqdFp3QlfiGvup1GsEL%2FT5KoPOJwfBfchfGOYEeD6UP9wYISnO2G28baNFHAUpkjIbPDDQPENJJWGf5AhBwVXyJ5ioZT%2Bk8jWc4WkeLC3YT4zz9gkg2VCrtDJHV6YvPjUTuqfgUF7fhnDFD3ukP6VZ%2BlCNozr5a1ybyLVQvLarPyngK6oA0TLoFK5KRgbWnRsv34ZRS6%2Fy8oOVt%2FZ09dL4ziaRwbaE1KdSjitN5CYsWa3U3lzTHYYDkl3bIL9WMhlJDrOa82iq9ZWBJoJfUnAOeV9g9jAB1SQz6o23rpNyi7DgT7ghy96k8%2FhuENQsfOPphebJvVJhbbWb1SHmXSOo1tL78%2FBSDBu7pgWTU%2F3pjfb82N4G117Q1ogQcqqe4Hlv2%2BdmFSlI%2B9mNAbnoxWhL7DYIPpjo1gPslrPFxa%2FS6r27p2ZHVPE0gvxJubteJsKawgHYn5l969wLsRPlsi2jxksZBrx3LyW%2Fgv3kb9%2BJYmiP9yoQX%2FOrzmofOUeUnDAoDMrX%2FgfQ578PPMPzy6yadDFmoL85Fscw%2BOONvQY6pgEYbiUaPqiVB57yo0hLvjeweBcsNldgnp4HRaVjQf%2Fc7fDme3VdPs7AtOIGn8%2B3QwGuczb340Gr2P9O%2Bvp7bzsHf10u2obQ2rzX5NU41HCAXnXoXl1kTFS2a42zIc8uRAHVPVeBj6uik0KTWr1RvaVzVvMr3fQGCpNxuGwQu9l3e%2BbLvYKPcBRpDYnQiOYxHxXKhImOQs39OjWBdUfHTRHEeJ5t9fAr&X-Amz-Signature=b78e96d36db6ad4b0c4040c8b4b16f81f7c2d15666ae06d31e8819119df9f6b5&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46657OSPINF%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJGMEQCIH%2F1nit5NFQBOBc0SLbAYLxTrEaD7IMMA4wXR%2BPLLcBXAiAhWm%2FLNexfPVwERLn9hpfoApmY%2FiUTOR5NNdG%2BOaZFbSr%2FAwhHEAAaDDYzNzQyMzE4MzgwNSIMgnMuPLzfodD1wFv0KtwDbzOVVSCBJfTh8ZIPEcn0CLf261JSA6s2QpNIAH8%2FYy9RhefUXmQNLGZmHECvaMFnzs%2Fj95dXjojr8oPUYi%2ByW5tmfocqdFp3QlfiGvup1GsEL%2FT5KoPOJwfBfchfGOYEeD6UP9wYISnO2G28baNFHAUpkjIbPDDQPENJJWGf5AhBwVXyJ5ioZT%2Bk8jWc4WkeLC3YT4zz9gkg2VCrtDJHV6YvPjUTuqfgUF7fhnDFD3ukP6VZ%2BlCNozr5a1ybyLVQvLarPyngK6oA0TLoFK5KRgbWnRsv34ZRS6%2Fy8oOVt%2FZ09dL4ziaRwbaE1KdSjitN5CYsWa3U3lzTHYYDkl3bIL9WMhlJDrOa82iq9ZWBJoJfUnAOeV9g9jAB1SQz6o23rpNyi7DgT7ghy96k8%2FhuENQsfOPphebJvVJhbbWb1SHmXSOo1tL78%2FBSDBu7pgWTU%2F3pjfb82N4G117Q1ogQcqqe4Hlv2%2BdmFSlI%2B9mNAbnoxWhL7DYIPpjo1gPslrPFxa%2FS6r27p2ZHVPE0gvxJubteJsKawgHYn5l969wLsRPlsi2jxksZBrx3LyW%2Fgv3kb9%2BJYmiP9yoQX%2FOrzmofOUeUnDAoDMrX%2FgfQ578PPMPzy6yadDFmoL85Fscw%2BOONvQY6pgEYbiUaPqiVB57yo0hLvjeweBcsNldgnp4HRaVjQf%2Fc7fDme3VdPs7AtOIGn8%2B3QwGuczb340Gr2P9O%2Bvp7bzsHf10u2obQ2rzX5NU41HCAXnXoXl1kTFS2a42zIc8uRAHVPVeBj6uik0KTWr1RvaVzVvMr3fQGCpNxuGwQu9l3e%2BbLvYKPcBRpDYnQiOYxHxXKhImOQs39OjWBdUfHTRHEeJ5t9fAr&X-Amz-Signature=98925d56ca05b617cbccb6eb69cf1d12b72e201bfeccd88c3e25a80bd2c153d1&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46657OSPINF%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJGMEQCIH%2F1nit5NFQBOBc0SLbAYLxTrEaD7IMMA4wXR%2BPLLcBXAiAhWm%2FLNexfPVwERLn9hpfoApmY%2FiUTOR5NNdG%2BOaZFbSr%2FAwhHEAAaDDYzNzQyMzE4MzgwNSIMgnMuPLzfodD1wFv0KtwDbzOVVSCBJfTh8ZIPEcn0CLf261JSA6s2QpNIAH8%2FYy9RhefUXmQNLGZmHECvaMFnzs%2Fj95dXjojr8oPUYi%2ByW5tmfocqdFp3QlfiGvup1GsEL%2FT5KoPOJwfBfchfGOYEeD6UP9wYISnO2G28baNFHAUpkjIbPDDQPENJJWGf5AhBwVXyJ5ioZT%2Bk8jWc4WkeLC3YT4zz9gkg2VCrtDJHV6YvPjUTuqfgUF7fhnDFD3ukP6VZ%2BlCNozr5a1ybyLVQvLarPyngK6oA0TLoFK5KRgbWnRsv34ZRS6%2Fy8oOVt%2FZ09dL4ziaRwbaE1KdSjitN5CYsWa3U3lzTHYYDkl3bIL9WMhlJDrOa82iq9ZWBJoJfUnAOeV9g9jAB1SQz6o23rpNyi7DgT7ghy96k8%2FhuENQsfOPphebJvVJhbbWb1SHmXSOo1tL78%2FBSDBu7pgWTU%2F3pjfb82N4G117Q1ogQcqqe4Hlv2%2BdmFSlI%2B9mNAbnoxWhL7DYIPpjo1gPslrPFxa%2FS6r27p2ZHVPE0gvxJubteJsKawgHYn5l969wLsRPlsi2jxksZBrx3LyW%2Fgv3kb9%2BJYmiP9yoQX%2FOrzmofOUeUnDAoDMrX%2FgfQ578PPMPzy6yadDFmoL85Fscw%2BOONvQY6pgEYbiUaPqiVB57yo0hLvjeweBcsNldgnp4HRaVjQf%2Fc7fDme3VdPs7AtOIGn8%2B3QwGuczb340Gr2P9O%2Bvp7bzsHf10u2obQ2rzX5NU41HCAXnXoXl1kTFS2a42zIc8uRAHVPVeBj6uik0KTWr1RvaVzVvMr3fQGCpNxuGwQu9l3e%2BbLvYKPcBRpDYnQiOYxHxXKhImOQs39OjWBdUfHTRHEeJ5t9fAr&X-Amz-Signature=0a64c2a0f1bf5f7f3acbc88f2ba22c8eb226144f3e9e9de92e06389d02a6cb15&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46657OSPINF%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJGMEQCIH%2F1nit5NFQBOBc0SLbAYLxTrEaD7IMMA4wXR%2BPLLcBXAiAhWm%2FLNexfPVwERLn9hpfoApmY%2FiUTOR5NNdG%2BOaZFbSr%2FAwhHEAAaDDYzNzQyMzE4MzgwNSIMgnMuPLzfodD1wFv0KtwDbzOVVSCBJfTh8ZIPEcn0CLf261JSA6s2QpNIAH8%2FYy9RhefUXmQNLGZmHECvaMFnzs%2Fj95dXjojr8oPUYi%2ByW5tmfocqdFp3QlfiGvup1GsEL%2FT5KoPOJwfBfchfGOYEeD6UP9wYISnO2G28baNFHAUpkjIbPDDQPENJJWGf5AhBwVXyJ5ioZT%2Bk8jWc4WkeLC3YT4zz9gkg2VCrtDJHV6YvPjUTuqfgUF7fhnDFD3ukP6VZ%2BlCNozr5a1ybyLVQvLarPyngK6oA0TLoFK5KRgbWnRsv34ZRS6%2Fy8oOVt%2FZ09dL4ziaRwbaE1KdSjitN5CYsWa3U3lzTHYYDkl3bIL9WMhlJDrOa82iq9ZWBJoJfUnAOeV9g9jAB1SQz6o23rpNyi7DgT7ghy96k8%2FhuENQsfOPphebJvVJhbbWb1SHmXSOo1tL78%2FBSDBu7pgWTU%2F3pjfb82N4G117Q1ogQcqqe4Hlv2%2BdmFSlI%2B9mNAbnoxWhL7DYIPpjo1gPslrPFxa%2FS6r27p2ZHVPE0gvxJubteJsKawgHYn5l969wLsRPlsi2jxksZBrx3LyW%2Fgv3kb9%2BJYmiP9yoQX%2FOrzmofOUeUnDAoDMrX%2FgfQ578PPMPzy6yadDFmoL85Fscw%2BOONvQY6pgEYbiUaPqiVB57yo0hLvjeweBcsNldgnp4HRaVjQf%2Fc7fDme3VdPs7AtOIGn8%2B3QwGuczb340Gr2P9O%2Bvp7bzsHf10u2obQ2rzX5NU41HCAXnXoXl1kTFS2a42zIc8uRAHVPVeBj6uik0KTWr1RvaVzVvMr3fQGCpNxuGwQu9l3e%2BbLvYKPcBRpDYnQiOYxHxXKhImOQs39OjWBdUfHTRHEeJ5t9fAr&X-Amz-Signature=fc6fff899ef2d5fae10801129f68a6381185831c43ddb0c622623b080a414a47&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46657OSPINF%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJGMEQCIH%2F1nit5NFQBOBc0SLbAYLxTrEaD7IMMA4wXR%2BPLLcBXAiAhWm%2FLNexfPVwERLn9hpfoApmY%2FiUTOR5NNdG%2BOaZFbSr%2FAwhHEAAaDDYzNzQyMzE4MzgwNSIMgnMuPLzfodD1wFv0KtwDbzOVVSCBJfTh8ZIPEcn0CLf261JSA6s2QpNIAH8%2FYy9RhefUXmQNLGZmHECvaMFnzs%2Fj95dXjojr8oPUYi%2ByW5tmfocqdFp3QlfiGvup1GsEL%2FT5KoPOJwfBfchfGOYEeD6UP9wYISnO2G28baNFHAUpkjIbPDDQPENJJWGf5AhBwVXyJ5ioZT%2Bk8jWc4WkeLC3YT4zz9gkg2VCrtDJHV6YvPjUTuqfgUF7fhnDFD3ukP6VZ%2BlCNozr5a1ybyLVQvLarPyngK6oA0TLoFK5KRgbWnRsv34ZRS6%2Fy8oOVt%2FZ09dL4ziaRwbaE1KdSjitN5CYsWa3U3lzTHYYDkl3bIL9WMhlJDrOa82iq9ZWBJoJfUnAOeV9g9jAB1SQz6o23rpNyi7DgT7ghy96k8%2FhuENQsfOPphebJvVJhbbWb1SHmXSOo1tL78%2FBSDBu7pgWTU%2F3pjfb82N4G117Q1ogQcqqe4Hlv2%2BdmFSlI%2B9mNAbnoxWhL7DYIPpjo1gPslrPFxa%2FS6r27p2ZHVPE0gvxJubteJsKawgHYn5l969wLsRPlsi2jxksZBrx3LyW%2Fgv3kb9%2BJYmiP9yoQX%2FOrzmofOUeUnDAoDMrX%2FgfQ578PPMPzy6yadDFmoL85Fscw%2BOONvQY6pgEYbiUaPqiVB57yo0hLvjeweBcsNldgnp4HRaVjQf%2Fc7fDme3VdPs7AtOIGn8%2B3QwGuczb340Gr2P9O%2Bvp7bzsHf10u2obQ2rzX5NU41HCAXnXoXl1kTFS2a42zIc8uRAHVPVeBj6uik0KTWr1RvaVzVvMr3fQGCpNxuGwQu9l3e%2BbLvYKPcBRpDYnQiOYxHxXKhImOQs39OjWBdUfHTRHEeJ5t9fAr&X-Amz-Signature=b4ecc0bfe3b495be4cf13150e332e203ef1a9708257412a01877464aae3af666&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46657OSPINF%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJGMEQCIH%2F1nit5NFQBOBc0SLbAYLxTrEaD7IMMA4wXR%2BPLLcBXAiAhWm%2FLNexfPVwERLn9hpfoApmY%2FiUTOR5NNdG%2BOaZFbSr%2FAwhHEAAaDDYzNzQyMzE4MzgwNSIMgnMuPLzfodD1wFv0KtwDbzOVVSCBJfTh8ZIPEcn0CLf261JSA6s2QpNIAH8%2FYy9RhefUXmQNLGZmHECvaMFnzs%2Fj95dXjojr8oPUYi%2ByW5tmfocqdFp3QlfiGvup1GsEL%2FT5KoPOJwfBfchfGOYEeD6UP9wYISnO2G28baNFHAUpkjIbPDDQPENJJWGf5AhBwVXyJ5ioZT%2Bk8jWc4WkeLC3YT4zz9gkg2VCrtDJHV6YvPjUTuqfgUF7fhnDFD3ukP6VZ%2BlCNozr5a1ybyLVQvLarPyngK6oA0TLoFK5KRgbWnRsv34ZRS6%2Fy8oOVt%2FZ09dL4ziaRwbaE1KdSjitN5CYsWa3U3lzTHYYDkl3bIL9WMhlJDrOa82iq9ZWBJoJfUnAOeV9g9jAB1SQz6o23rpNyi7DgT7ghy96k8%2FhuENQsfOPphebJvVJhbbWb1SHmXSOo1tL78%2FBSDBu7pgWTU%2F3pjfb82N4G117Q1ogQcqqe4Hlv2%2BdmFSlI%2B9mNAbnoxWhL7DYIPpjo1gPslrPFxa%2FS6r27p2ZHVPE0gvxJubteJsKawgHYn5l969wLsRPlsi2jxksZBrx3LyW%2Fgv3kb9%2BJYmiP9yoQX%2FOrzmofOUeUnDAoDMrX%2FgfQ578PPMPzy6yadDFmoL85Fscw%2BOONvQY6pgEYbiUaPqiVB57yo0hLvjeweBcsNldgnp4HRaVjQf%2Fc7fDme3VdPs7AtOIGn8%2B3QwGuczb340Gr2P9O%2Bvp7bzsHf10u2obQ2rzX5NU41HCAXnXoXl1kTFS2a42zIc8uRAHVPVeBj6uik0KTWr1RvaVzVvMr3fQGCpNxuGwQu9l3e%2BbLvYKPcBRpDYnQiOYxHxXKhImOQs39OjWBdUfHTRHEeJ5t9fAr&X-Amz-Signature=0dd70a3165e0d91880dd5192ea3222f7a0bcdff9fa93d30e79cc6ed20bdeb075&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46657OSPINF%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJGMEQCIH%2F1nit5NFQBOBc0SLbAYLxTrEaD7IMMA4wXR%2BPLLcBXAiAhWm%2FLNexfPVwERLn9hpfoApmY%2FiUTOR5NNdG%2BOaZFbSr%2FAwhHEAAaDDYzNzQyMzE4MzgwNSIMgnMuPLzfodD1wFv0KtwDbzOVVSCBJfTh8ZIPEcn0CLf261JSA6s2QpNIAH8%2FYy9RhefUXmQNLGZmHECvaMFnzs%2Fj95dXjojr8oPUYi%2ByW5tmfocqdFp3QlfiGvup1GsEL%2FT5KoPOJwfBfchfGOYEeD6UP9wYISnO2G28baNFHAUpkjIbPDDQPENJJWGf5AhBwVXyJ5ioZT%2Bk8jWc4WkeLC3YT4zz9gkg2VCrtDJHV6YvPjUTuqfgUF7fhnDFD3ukP6VZ%2BlCNozr5a1ybyLVQvLarPyngK6oA0TLoFK5KRgbWnRsv34ZRS6%2Fy8oOVt%2FZ09dL4ziaRwbaE1KdSjitN5CYsWa3U3lzTHYYDkl3bIL9WMhlJDrOa82iq9ZWBJoJfUnAOeV9g9jAB1SQz6o23rpNyi7DgT7ghy96k8%2FhuENQsfOPphebJvVJhbbWb1SHmXSOo1tL78%2FBSDBu7pgWTU%2F3pjfb82N4G117Q1ogQcqqe4Hlv2%2BdmFSlI%2B9mNAbnoxWhL7DYIPpjo1gPslrPFxa%2FS6r27p2ZHVPE0gvxJubteJsKawgHYn5l969wLsRPlsi2jxksZBrx3LyW%2Fgv3kb9%2BJYmiP9yoQX%2FOrzmofOUeUnDAoDMrX%2FgfQ578PPMPzy6yadDFmoL85Fscw%2BOONvQY6pgEYbiUaPqiVB57yo0hLvjeweBcsNldgnp4HRaVjQf%2Fc7fDme3VdPs7AtOIGn8%2B3QwGuczb340Gr2P9O%2Bvp7bzsHf10u2obQ2rzX5NU41HCAXnXoXl1kTFS2a42zIc8uRAHVPVeBj6uik0KTWr1RvaVzVvMr3fQGCpNxuGwQu9l3e%2BbLvYKPcBRpDYnQiOYxHxXKhImOQs39OjWBdUfHTRHEeJ5t9fAr&X-Amz-Signature=7a1d529f447efd3a828c08ef6749a34f115d7f1a51402305afbf19f70f807a59&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46657OSPINF%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJGMEQCIH%2F1nit5NFQBOBc0SLbAYLxTrEaD7IMMA4wXR%2BPLLcBXAiAhWm%2FLNexfPVwERLn9hpfoApmY%2FiUTOR5NNdG%2BOaZFbSr%2FAwhHEAAaDDYzNzQyMzE4MzgwNSIMgnMuPLzfodD1wFv0KtwDbzOVVSCBJfTh8ZIPEcn0CLf261JSA6s2QpNIAH8%2FYy9RhefUXmQNLGZmHECvaMFnzs%2Fj95dXjojr8oPUYi%2ByW5tmfocqdFp3QlfiGvup1GsEL%2FT5KoPOJwfBfchfGOYEeD6UP9wYISnO2G28baNFHAUpkjIbPDDQPENJJWGf5AhBwVXyJ5ioZT%2Bk8jWc4WkeLC3YT4zz9gkg2VCrtDJHV6YvPjUTuqfgUF7fhnDFD3ukP6VZ%2BlCNozr5a1ybyLVQvLarPyngK6oA0TLoFK5KRgbWnRsv34ZRS6%2Fy8oOVt%2FZ09dL4ziaRwbaE1KdSjitN5CYsWa3U3lzTHYYDkl3bIL9WMhlJDrOa82iq9ZWBJoJfUnAOeV9g9jAB1SQz6o23rpNyi7DgT7ghy96k8%2FhuENQsfOPphebJvVJhbbWb1SHmXSOo1tL78%2FBSDBu7pgWTU%2F3pjfb82N4G117Q1ogQcqqe4Hlv2%2BdmFSlI%2B9mNAbnoxWhL7DYIPpjo1gPslrPFxa%2FS6r27p2ZHVPE0gvxJubteJsKawgHYn5l969wLsRPlsi2jxksZBrx3LyW%2Fgv3kb9%2BJYmiP9yoQX%2FOrzmofOUeUnDAoDMrX%2FgfQ578PPMPzy6yadDFmoL85Fscw%2BOONvQY6pgEYbiUaPqiVB57yo0hLvjeweBcsNldgnp4HRaVjQf%2Fc7fDme3VdPs7AtOIGn8%2B3QwGuczb340Gr2P9O%2Bvp7bzsHf10u2obQ2rzX5NU41HCAXnXoXl1kTFS2a42zIc8uRAHVPVeBj6uik0KTWr1RvaVzVvMr3fQGCpNxuGwQu9l3e%2BbLvYKPcBRpDYnQiOYxHxXKhImOQs39OjWBdUfHTRHEeJ5t9fAr&X-Amz-Signature=b1e258524148c21a6ee9ef0b812a9d88e9a30cabd949f94fe2863a05ba066f85&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46657OSPINF%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJGMEQCIH%2F1nit5NFQBOBc0SLbAYLxTrEaD7IMMA4wXR%2BPLLcBXAiAhWm%2FLNexfPVwERLn9hpfoApmY%2FiUTOR5NNdG%2BOaZFbSr%2FAwhHEAAaDDYzNzQyMzE4MzgwNSIMgnMuPLzfodD1wFv0KtwDbzOVVSCBJfTh8ZIPEcn0CLf261JSA6s2QpNIAH8%2FYy9RhefUXmQNLGZmHECvaMFnzs%2Fj95dXjojr8oPUYi%2ByW5tmfocqdFp3QlfiGvup1GsEL%2FT5KoPOJwfBfchfGOYEeD6UP9wYISnO2G28baNFHAUpkjIbPDDQPENJJWGf5AhBwVXyJ5ioZT%2Bk8jWc4WkeLC3YT4zz9gkg2VCrtDJHV6YvPjUTuqfgUF7fhnDFD3ukP6VZ%2BlCNozr5a1ybyLVQvLarPyngK6oA0TLoFK5KRgbWnRsv34ZRS6%2Fy8oOVt%2FZ09dL4ziaRwbaE1KdSjitN5CYsWa3U3lzTHYYDkl3bIL9WMhlJDrOa82iq9ZWBJoJfUnAOeV9g9jAB1SQz6o23rpNyi7DgT7ghy96k8%2FhuENQsfOPphebJvVJhbbWb1SHmXSOo1tL78%2FBSDBu7pgWTU%2F3pjfb82N4G117Q1ogQcqqe4Hlv2%2BdmFSlI%2B9mNAbnoxWhL7DYIPpjo1gPslrPFxa%2FS6r27p2ZHVPE0gvxJubteJsKawgHYn5l969wLsRPlsi2jxksZBrx3LyW%2Fgv3kb9%2BJYmiP9yoQX%2FOrzmofOUeUnDAoDMrX%2FgfQ578PPMPzy6yadDFmoL85Fscw%2BOONvQY6pgEYbiUaPqiVB57yo0hLvjeweBcsNldgnp4HRaVjQf%2Fc7fDme3VdPs7AtOIGn8%2B3QwGuczb340Gr2P9O%2Bvp7bzsHf10u2obQ2rzX5NU41HCAXnXoXl1kTFS2a42zIc8uRAHVPVeBj6uik0KTWr1RvaVzVvMr3fQGCpNxuGwQu9l3e%2BbLvYKPcBRpDYnQiOYxHxXKhImOQs39OjWBdUfHTRHEeJ5t9fAr&X-Amz-Signature=a840c98678e92dc14442e742d3f61eb472d4d1764f60bc7073e7c82a8cb228cf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SF6HVPLT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJGMEQCIEEr1eDvfDGzsZrhE5FX0VIVtus80UbAoqwOihlIYBKIAiBQPV4RF%2BbNhX4pq58yJZA1IunpG7Zk9KFKCxLQCqFeLCr%2FAwhHEAAaDDYzNzQyMzE4MzgwNSIMXxiKkJoTJrWQGgKxKtwDfVqx4dPQlOPR0rVvXAORFENUMZeA0h0jcVMDxq1feyaa5hfhfCCiLoGuhX4LKJVlnSVNyHWrrHqucf8g7n%2BUd0aG4cfnWE902zKHbejybVaHOKYROWMGG%2BCY%2FVmKZoD9tirqDbOTGj4ZETTKGT%2BxAAepV24ARzKKzqzD9N%2BHx%2BDtf6LfsSdXK8H8%2FX4z9pJIL0SNubJhNrvU%2F%2Fhy6cAAICnLohFsajAEkOzgD5W6JsmwC1oSwgSBINA5ORlOyfxA9bTPRcv71%2FzwVwZRgZ0lCwkAALmp%2FbWwM84FEUIzgeawYSH5%2FY2gpFkkKNjuwtSXsfXc91GO20Sei0WljpTL2iG2SN9kW6%2BQdUQPckfURn3UFvYEnTGyvNwP%2BtsiDCqiuSJJkL9sGZoLqcUyy8cNXu7JTbiGz3sH3UKVifaFfOzEG8X%2F6bwZUVh%2B917Ny3B2QnGxYr8gBh8LGlDWfcnMnzPsCr4v0lKLc4Oe4m8E%2FMd2e0B4%2F4o%2BnXhhKgiGbvWu26qwXKAE0zaHj%2F4M%2B8hW9CrNhvlfU03N7W5m6I66maOSsxVEiLBvSu573u5nXk%2BmX4kKN%2Fmjq%2FNPF8el5Q%2BkzBSj58MSFHnLWGpg2JfVkxDMDH04FgxMP1a%2Fv%2FwwueONvQY6pgFnUaRR703TKQZwNbBJom%2FRv1pnLzwMvhNLRFEsv4OZnmZJqKEDe8XRQLj8RBsz6FO%2BJyAucUYmyN2Q2f0g5OP5y5Z4yFere1lSTa7F2ZmSlcW6%2BHt%2FMqnZPhXIJ%2F54%2Bq6Zo%2FScf5%2BskiKaHdAj4fmWN3wfHtX2m5Ha9YsmWmciQ8oOpAqQkJ53nEqVoBbYjobtSjMbru3fD5rsFjU2yd11sjqju4bR&X-Amz-Signature=6bbc5a9dc45fc0b4f1d80d58a6ee5cfe52ce9ee86dd89c8590bf155fe0202340&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SF6HVPLT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJGMEQCIEEr1eDvfDGzsZrhE5FX0VIVtus80UbAoqwOihlIYBKIAiBQPV4RF%2BbNhX4pq58yJZA1IunpG7Zk9KFKCxLQCqFeLCr%2FAwhHEAAaDDYzNzQyMzE4MzgwNSIMXxiKkJoTJrWQGgKxKtwDfVqx4dPQlOPR0rVvXAORFENUMZeA0h0jcVMDxq1feyaa5hfhfCCiLoGuhX4LKJVlnSVNyHWrrHqucf8g7n%2BUd0aG4cfnWE902zKHbejybVaHOKYROWMGG%2BCY%2FVmKZoD9tirqDbOTGj4ZETTKGT%2BxAAepV24ARzKKzqzD9N%2BHx%2BDtf6LfsSdXK8H8%2FX4z9pJIL0SNubJhNrvU%2F%2Fhy6cAAICnLohFsajAEkOzgD5W6JsmwC1oSwgSBINA5ORlOyfxA9bTPRcv71%2FzwVwZRgZ0lCwkAALmp%2FbWwM84FEUIzgeawYSH5%2FY2gpFkkKNjuwtSXsfXc91GO20Sei0WljpTL2iG2SN9kW6%2BQdUQPckfURn3UFvYEnTGyvNwP%2BtsiDCqiuSJJkL9sGZoLqcUyy8cNXu7JTbiGz3sH3UKVifaFfOzEG8X%2F6bwZUVh%2B917Ny3B2QnGxYr8gBh8LGlDWfcnMnzPsCr4v0lKLc4Oe4m8E%2FMd2e0B4%2F4o%2BnXhhKgiGbvWu26qwXKAE0zaHj%2F4M%2B8hW9CrNhvlfU03N7W5m6I66maOSsxVEiLBvSu573u5nXk%2BmX4kKN%2Fmjq%2FNPF8el5Q%2BkzBSj58MSFHnLWGpg2JfVkxDMDH04FgxMP1a%2Fv%2FwwueONvQY6pgFnUaRR703TKQZwNbBJom%2FRv1pnLzwMvhNLRFEsv4OZnmZJqKEDe8XRQLj8RBsz6FO%2BJyAucUYmyN2Q2f0g5OP5y5Z4yFere1lSTa7F2ZmSlcW6%2BHt%2FMqnZPhXIJ%2F54%2Bq6Zo%2FScf5%2BskiKaHdAj4fmWN3wfHtX2m5Ha9YsmWmciQ8oOpAqQkJ53nEqVoBbYjobtSjMbru3fD5rsFjU2yd11sjqju4bR&X-Amz-Signature=76c1ca9985a13c111fb467c8a1f2255ef840502ddfb13698c2f4f9ac65da3520&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
