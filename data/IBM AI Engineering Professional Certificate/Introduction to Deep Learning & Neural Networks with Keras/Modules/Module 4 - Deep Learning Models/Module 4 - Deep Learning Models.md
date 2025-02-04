

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SH7AP4BP%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQDPVHAeU%2FTMx2GwY4NPxFAFLjkaUl2qEozABX90%2BhDjAAIhAKytW94M1nkKjbfg21gUBFXwBlD8AJEHrRBPR%2F2NQMxeKv8DCDcQABoMNjM3NDIzMTgzODA1Igwlr0wR9elWSmOZyZMq3AOpEGUsA0c3nafWM0iOmrNwrBP2X6FH%2BTojKxo1tUnYj89i0S6HzXR8MKtQ3TERQx0CifEXxMCTcKEtq%2BS3lvVm9xIU4JcTxs%2Fypy%2BvDJDmTmYsmvfopuYZjeZB%2BArcwurM6UoCFtBCGg9pNhoS7sJYZQ3A0KsX8c%2BpOQDDR5WXFSsOS3cNDyXmeTthYTEU0FsX%2BxCe%2FEdwLtH8MYL%2B9RtKSkxgBbKWoudeQbUtlbparxffGeZsK%2FahrDze0F6Gg73WB46JbHipSMkQK%2FfRQst0%2BAK%2F4%2FyetNG6SnzxXmugvyOB4EK4vGgcp%2FhClckdQJd%2FTLE0b1TwBAoLUAw2ydO4VEDYkMgUTmzZ0HjJSWd%2FQRh1%2BgAZ4Q95%2FTBZLWFAWP5smgOONq%2BIwL4wjkPR0VKsPaQqhaRa5ST5dyqXW7MIXdec%2Bgm7mAsjnVIND0DF%2FUmfMJMMB0wOdeEjQQ64WQ9eCRF%2FKBJKq8e8Egqr98XN1HjSZ8Tr9VKmS3vMU%2FUb6iX2oDwZQMnWP8wDyT2Ni42%2FvkxEls5qmdewQXjMN9HB6J1qaovxZagjqk1dlrOszlaVtYMQHvjAP5GOEBUJDuINVMkakxHQzHOHO2MRxcchvd%2Fj8xw8FyeTq8Pd4TCWlIq9BjqkAdVs3W0LxQ1nUDOcbPuBccHlhFyv%2BhWqM92y2TfIq3If8qxGd07eo9G03peX4UEYx3xNA5Rhmpu%2FGGdAYWOw5dpWxLDU2%2FMtlO9FGFG%2BvF0m%2BxrIePmvpeuWBJSP7sDJ2wsj8l3pcUAJtb4Gzki243pitfHraMkxpQFm4285N8QFlL6k5a%2FjQoY%2BZ9mub5uyD1re3GmT0Aoiuhtv0%2BDWH8kCE9FR&X-Amz-Signature=7e26a68b70cebf976099933f7dc795c20594f38aae7e19770d09a96802f90cbc&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SH7AP4BP%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQDPVHAeU%2FTMx2GwY4NPxFAFLjkaUl2qEozABX90%2BhDjAAIhAKytW94M1nkKjbfg21gUBFXwBlD8AJEHrRBPR%2F2NQMxeKv8DCDcQABoMNjM3NDIzMTgzODA1Igwlr0wR9elWSmOZyZMq3AOpEGUsA0c3nafWM0iOmrNwrBP2X6FH%2BTojKxo1tUnYj89i0S6HzXR8MKtQ3TERQx0CifEXxMCTcKEtq%2BS3lvVm9xIU4JcTxs%2Fypy%2BvDJDmTmYsmvfopuYZjeZB%2BArcwurM6UoCFtBCGg9pNhoS7sJYZQ3A0KsX8c%2BpOQDDR5WXFSsOS3cNDyXmeTthYTEU0FsX%2BxCe%2FEdwLtH8MYL%2B9RtKSkxgBbKWoudeQbUtlbparxffGeZsK%2FahrDze0F6Gg73WB46JbHipSMkQK%2FfRQst0%2BAK%2F4%2FyetNG6SnzxXmugvyOB4EK4vGgcp%2FhClckdQJd%2FTLE0b1TwBAoLUAw2ydO4VEDYkMgUTmzZ0HjJSWd%2FQRh1%2BgAZ4Q95%2FTBZLWFAWP5smgOONq%2BIwL4wjkPR0VKsPaQqhaRa5ST5dyqXW7MIXdec%2Bgm7mAsjnVIND0DF%2FUmfMJMMB0wOdeEjQQ64WQ9eCRF%2FKBJKq8e8Egqr98XN1HjSZ8Tr9VKmS3vMU%2FUb6iX2oDwZQMnWP8wDyT2Ni42%2FvkxEls5qmdewQXjMN9HB6J1qaovxZagjqk1dlrOszlaVtYMQHvjAP5GOEBUJDuINVMkakxHQzHOHO2MRxcchvd%2Fj8xw8FyeTq8Pd4TCWlIq9BjqkAdVs3W0LxQ1nUDOcbPuBccHlhFyv%2BhWqM92y2TfIq3If8qxGd07eo9G03peX4UEYx3xNA5Rhmpu%2FGGdAYWOw5dpWxLDU2%2FMtlO9FGFG%2BvF0m%2BxrIePmvpeuWBJSP7sDJ2wsj8l3pcUAJtb4Gzki243pitfHraMkxpQFm4285N8QFlL6k5a%2FjQoY%2BZ9mub5uyD1re3GmT0Aoiuhtv0%2BDWH8kCE9FR&X-Amz-Signature=40aeee7cf0b197218b66cab0599382d40c45da296199ecc0fd0af89801d58619&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SH7AP4BP%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQDPVHAeU%2FTMx2GwY4NPxFAFLjkaUl2qEozABX90%2BhDjAAIhAKytW94M1nkKjbfg21gUBFXwBlD8AJEHrRBPR%2F2NQMxeKv8DCDcQABoMNjM3NDIzMTgzODA1Igwlr0wR9elWSmOZyZMq3AOpEGUsA0c3nafWM0iOmrNwrBP2X6FH%2BTojKxo1tUnYj89i0S6HzXR8MKtQ3TERQx0CifEXxMCTcKEtq%2BS3lvVm9xIU4JcTxs%2Fypy%2BvDJDmTmYsmvfopuYZjeZB%2BArcwurM6UoCFtBCGg9pNhoS7sJYZQ3A0KsX8c%2BpOQDDR5WXFSsOS3cNDyXmeTthYTEU0FsX%2BxCe%2FEdwLtH8MYL%2B9RtKSkxgBbKWoudeQbUtlbparxffGeZsK%2FahrDze0F6Gg73WB46JbHipSMkQK%2FfRQst0%2BAK%2F4%2FyetNG6SnzxXmugvyOB4EK4vGgcp%2FhClckdQJd%2FTLE0b1TwBAoLUAw2ydO4VEDYkMgUTmzZ0HjJSWd%2FQRh1%2BgAZ4Q95%2FTBZLWFAWP5smgOONq%2BIwL4wjkPR0VKsPaQqhaRa5ST5dyqXW7MIXdec%2Bgm7mAsjnVIND0DF%2FUmfMJMMB0wOdeEjQQ64WQ9eCRF%2FKBJKq8e8Egqr98XN1HjSZ8Tr9VKmS3vMU%2FUb6iX2oDwZQMnWP8wDyT2Ni42%2FvkxEls5qmdewQXjMN9HB6J1qaovxZagjqk1dlrOszlaVtYMQHvjAP5GOEBUJDuINVMkakxHQzHOHO2MRxcchvd%2Fj8xw8FyeTq8Pd4TCWlIq9BjqkAdVs3W0LxQ1nUDOcbPuBccHlhFyv%2BhWqM92y2TfIq3If8qxGd07eo9G03peX4UEYx3xNA5Rhmpu%2FGGdAYWOw5dpWxLDU2%2FMtlO9FGFG%2BvF0m%2BxrIePmvpeuWBJSP7sDJ2wsj8l3pcUAJtb4Gzki243pitfHraMkxpQFm4285N8QFlL6k5a%2FjQoY%2BZ9mub5uyD1re3GmT0Aoiuhtv0%2BDWH8kCE9FR&X-Amz-Signature=5e4a4d759748799cff315eb91c515f7e2d89d1632c2ab773a719a7acd0c7c6e6&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SH7AP4BP%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQDPVHAeU%2FTMx2GwY4NPxFAFLjkaUl2qEozABX90%2BhDjAAIhAKytW94M1nkKjbfg21gUBFXwBlD8AJEHrRBPR%2F2NQMxeKv8DCDcQABoMNjM3NDIzMTgzODA1Igwlr0wR9elWSmOZyZMq3AOpEGUsA0c3nafWM0iOmrNwrBP2X6FH%2BTojKxo1tUnYj89i0S6HzXR8MKtQ3TERQx0CifEXxMCTcKEtq%2BS3lvVm9xIU4JcTxs%2Fypy%2BvDJDmTmYsmvfopuYZjeZB%2BArcwurM6UoCFtBCGg9pNhoS7sJYZQ3A0KsX8c%2BpOQDDR5WXFSsOS3cNDyXmeTthYTEU0FsX%2BxCe%2FEdwLtH8MYL%2B9RtKSkxgBbKWoudeQbUtlbparxffGeZsK%2FahrDze0F6Gg73WB46JbHipSMkQK%2FfRQst0%2BAK%2F4%2FyetNG6SnzxXmugvyOB4EK4vGgcp%2FhClckdQJd%2FTLE0b1TwBAoLUAw2ydO4VEDYkMgUTmzZ0HjJSWd%2FQRh1%2BgAZ4Q95%2FTBZLWFAWP5smgOONq%2BIwL4wjkPR0VKsPaQqhaRa5ST5dyqXW7MIXdec%2Bgm7mAsjnVIND0DF%2FUmfMJMMB0wOdeEjQQ64WQ9eCRF%2FKBJKq8e8Egqr98XN1HjSZ8Tr9VKmS3vMU%2FUb6iX2oDwZQMnWP8wDyT2Ni42%2FvkxEls5qmdewQXjMN9HB6J1qaovxZagjqk1dlrOszlaVtYMQHvjAP5GOEBUJDuINVMkakxHQzHOHO2MRxcchvd%2Fj8xw8FyeTq8Pd4TCWlIq9BjqkAdVs3W0LxQ1nUDOcbPuBccHlhFyv%2BhWqM92y2TfIq3If8qxGd07eo9G03peX4UEYx3xNA5Rhmpu%2FGGdAYWOw5dpWxLDU2%2FMtlO9FGFG%2BvF0m%2BxrIePmvpeuWBJSP7sDJ2wsj8l3pcUAJtb4Gzki243pitfHraMkxpQFm4285N8QFlL6k5a%2FjQoY%2BZ9mub5uyD1re3GmT0Aoiuhtv0%2BDWH8kCE9FR&X-Amz-Signature=c9ee0d632fe92c368e053c3fc51796263a8f4f75aa6645fcd778ef7e16cc8c96&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SH7AP4BP%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221350Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQDPVHAeU%2FTMx2GwY4NPxFAFLjkaUl2qEozABX90%2BhDjAAIhAKytW94M1nkKjbfg21gUBFXwBlD8AJEHrRBPR%2F2NQMxeKv8DCDcQABoMNjM3NDIzMTgzODA1Igwlr0wR9elWSmOZyZMq3AOpEGUsA0c3nafWM0iOmrNwrBP2X6FH%2BTojKxo1tUnYj89i0S6HzXR8MKtQ3TERQx0CifEXxMCTcKEtq%2BS3lvVm9xIU4JcTxs%2Fypy%2BvDJDmTmYsmvfopuYZjeZB%2BArcwurM6UoCFtBCGg9pNhoS7sJYZQ3A0KsX8c%2BpOQDDR5WXFSsOS3cNDyXmeTthYTEU0FsX%2BxCe%2FEdwLtH8MYL%2B9RtKSkxgBbKWoudeQbUtlbparxffGeZsK%2FahrDze0F6Gg73WB46JbHipSMkQK%2FfRQst0%2BAK%2F4%2FyetNG6SnzxXmugvyOB4EK4vGgcp%2FhClckdQJd%2FTLE0b1TwBAoLUAw2ydO4VEDYkMgUTmzZ0HjJSWd%2FQRh1%2BgAZ4Q95%2FTBZLWFAWP5smgOONq%2BIwL4wjkPR0VKsPaQqhaRa5ST5dyqXW7MIXdec%2Bgm7mAsjnVIND0DF%2FUmfMJMMB0wOdeEjQQ64WQ9eCRF%2FKBJKq8e8Egqr98XN1HjSZ8Tr9VKmS3vMU%2FUb6iX2oDwZQMnWP8wDyT2Ni42%2FvkxEls5qmdewQXjMN9HB6J1qaovxZagjqk1dlrOszlaVtYMQHvjAP5GOEBUJDuINVMkakxHQzHOHO2MRxcchvd%2Fj8xw8FyeTq8Pd4TCWlIq9BjqkAdVs3W0LxQ1nUDOcbPuBccHlhFyv%2BhWqM92y2TfIq3If8qxGd07eo9G03peX4UEYx3xNA5Rhmpu%2FGGdAYWOw5dpWxLDU2%2FMtlO9FGFG%2BvF0m%2BxrIePmvpeuWBJSP7sDJ2wsj8l3pcUAJtb4Gzki243pitfHraMkxpQFm4285N8QFlL6k5a%2FjQoY%2BZ9mub5uyD1re3GmT0Aoiuhtv0%2BDWH8kCE9FR&X-Amz-Signature=e429195b40fe75cf605e2285855ab2d9949e3b6173a5d7f82ea68da736dafc3f&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SH7AP4BP%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQDPVHAeU%2FTMx2GwY4NPxFAFLjkaUl2qEozABX90%2BhDjAAIhAKytW94M1nkKjbfg21gUBFXwBlD8AJEHrRBPR%2F2NQMxeKv8DCDcQABoMNjM3NDIzMTgzODA1Igwlr0wR9elWSmOZyZMq3AOpEGUsA0c3nafWM0iOmrNwrBP2X6FH%2BTojKxo1tUnYj89i0S6HzXR8MKtQ3TERQx0CifEXxMCTcKEtq%2BS3lvVm9xIU4JcTxs%2Fypy%2BvDJDmTmYsmvfopuYZjeZB%2BArcwurM6UoCFtBCGg9pNhoS7sJYZQ3A0KsX8c%2BpOQDDR5WXFSsOS3cNDyXmeTthYTEU0FsX%2BxCe%2FEdwLtH8MYL%2B9RtKSkxgBbKWoudeQbUtlbparxffGeZsK%2FahrDze0F6Gg73WB46JbHipSMkQK%2FfRQst0%2BAK%2F4%2FyetNG6SnzxXmugvyOB4EK4vGgcp%2FhClckdQJd%2FTLE0b1TwBAoLUAw2ydO4VEDYkMgUTmzZ0HjJSWd%2FQRh1%2BgAZ4Q95%2FTBZLWFAWP5smgOONq%2BIwL4wjkPR0VKsPaQqhaRa5ST5dyqXW7MIXdec%2Bgm7mAsjnVIND0DF%2FUmfMJMMB0wOdeEjQQ64WQ9eCRF%2FKBJKq8e8Egqr98XN1HjSZ8Tr9VKmS3vMU%2FUb6iX2oDwZQMnWP8wDyT2Ni42%2FvkxEls5qmdewQXjMN9HB6J1qaovxZagjqk1dlrOszlaVtYMQHvjAP5GOEBUJDuINVMkakxHQzHOHO2MRxcchvd%2Fj8xw8FyeTq8Pd4TCWlIq9BjqkAdVs3W0LxQ1nUDOcbPuBccHlhFyv%2BhWqM92y2TfIq3If8qxGd07eo9G03peX4UEYx3xNA5Rhmpu%2FGGdAYWOw5dpWxLDU2%2FMtlO9FGFG%2BvF0m%2BxrIePmvpeuWBJSP7sDJ2wsj8l3pcUAJtb4Gzki243pitfHraMkxpQFm4285N8QFlL6k5a%2FjQoY%2BZ9mub5uyD1re3GmT0Aoiuhtv0%2BDWH8kCE9FR&X-Amz-Signature=ce350e42b380c88de2f301ab9d1572f0c61e00b79060684e950014dc69d88962&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SH7AP4BP%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQDPVHAeU%2FTMx2GwY4NPxFAFLjkaUl2qEozABX90%2BhDjAAIhAKytW94M1nkKjbfg21gUBFXwBlD8AJEHrRBPR%2F2NQMxeKv8DCDcQABoMNjM3NDIzMTgzODA1Igwlr0wR9elWSmOZyZMq3AOpEGUsA0c3nafWM0iOmrNwrBP2X6FH%2BTojKxo1tUnYj89i0S6HzXR8MKtQ3TERQx0CifEXxMCTcKEtq%2BS3lvVm9xIU4JcTxs%2Fypy%2BvDJDmTmYsmvfopuYZjeZB%2BArcwurM6UoCFtBCGg9pNhoS7sJYZQ3A0KsX8c%2BpOQDDR5WXFSsOS3cNDyXmeTthYTEU0FsX%2BxCe%2FEdwLtH8MYL%2B9RtKSkxgBbKWoudeQbUtlbparxffGeZsK%2FahrDze0F6Gg73WB46JbHipSMkQK%2FfRQst0%2BAK%2F4%2FyetNG6SnzxXmugvyOB4EK4vGgcp%2FhClckdQJd%2FTLE0b1TwBAoLUAw2ydO4VEDYkMgUTmzZ0HjJSWd%2FQRh1%2BgAZ4Q95%2FTBZLWFAWP5smgOONq%2BIwL4wjkPR0VKsPaQqhaRa5ST5dyqXW7MIXdec%2Bgm7mAsjnVIND0DF%2FUmfMJMMB0wOdeEjQQ64WQ9eCRF%2FKBJKq8e8Egqr98XN1HjSZ8Tr9VKmS3vMU%2FUb6iX2oDwZQMnWP8wDyT2Ni42%2FvkxEls5qmdewQXjMN9HB6J1qaovxZagjqk1dlrOszlaVtYMQHvjAP5GOEBUJDuINVMkakxHQzHOHO2MRxcchvd%2Fj8xw8FyeTq8Pd4TCWlIq9BjqkAdVs3W0LxQ1nUDOcbPuBccHlhFyv%2BhWqM92y2TfIq3If8qxGd07eo9G03peX4UEYx3xNA5Rhmpu%2FGGdAYWOw5dpWxLDU2%2FMtlO9FGFG%2BvF0m%2BxrIePmvpeuWBJSP7sDJ2wsj8l3pcUAJtb4Gzki243pitfHraMkxpQFm4285N8QFlL6k5a%2FjQoY%2BZ9mub5uyD1re3GmT0Aoiuhtv0%2BDWH8kCE9FR&X-Amz-Signature=1446f2c0b0b3fa24eeb5fe7ee1668f18ff7a7612da6d1ea4881f599fae224b30&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SH7AP4BP%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQDPVHAeU%2FTMx2GwY4NPxFAFLjkaUl2qEozABX90%2BhDjAAIhAKytW94M1nkKjbfg21gUBFXwBlD8AJEHrRBPR%2F2NQMxeKv8DCDcQABoMNjM3NDIzMTgzODA1Igwlr0wR9elWSmOZyZMq3AOpEGUsA0c3nafWM0iOmrNwrBP2X6FH%2BTojKxo1tUnYj89i0S6HzXR8MKtQ3TERQx0CifEXxMCTcKEtq%2BS3lvVm9xIU4JcTxs%2Fypy%2BvDJDmTmYsmvfopuYZjeZB%2BArcwurM6UoCFtBCGg9pNhoS7sJYZQ3A0KsX8c%2BpOQDDR5WXFSsOS3cNDyXmeTthYTEU0FsX%2BxCe%2FEdwLtH8MYL%2B9RtKSkxgBbKWoudeQbUtlbparxffGeZsK%2FahrDze0F6Gg73WB46JbHipSMkQK%2FfRQst0%2BAK%2F4%2FyetNG6SnzxXmugvyOB4EK4vGgcp%2FhClckdQJd%2FTLE0b1TwBAoLUAw2ydO4VEDYkMgUTmzZ0HjJSWd%2FQRh1%2BgAZ4Q95%2FTBZLWFAWP5smgOONq%2BIwL4wjkPR0VKsPaQqhaRa5ST5dyqXW7MIXdec%2Bgm7mAsjnVIND0DF%2FUmfMJMMB0wOdeEjQQ64WQ9eCRF%2FKBJKq8e8Egqr98XN1HjSZ8Tr9VKmS3vMU%2FUb6iX2oDwZQMnWP8wDyT2Ni42%2FvkxEls5qmdewQXjMN9HB6J1qaovxZagjqk1dlrOszlaVtYMQHvjAP5GOEBUJDuINVMkakxHQzHOHO2MRxcchvd%2Fj8xw8FyeTq8Pd4TCWlIq9BjqkAdVs3W0LxQ1nUDOcbPuBccHlhFyv%2BhWqM92y2TfIq3If8qxGd07eo9G03peX4UEYx3xNA5Rhmpu%2FGGdAYWOw5dpWxLDU2%2FMtlO9FGFG%2BvF0m%2BxrIePmvpeuWBJSP7sDJ2wsj8l3pcUAJtb4Gzki243pitfHraMkxpQFm4285N8QFlL6k5a%2FjQoY%2BZ9mub5uyD1re3GmT0Aoiuhtv0%2BDWH8kCE9FR&X-Amz-Signature=28466775ad807489ab044c83cb23a71afeb1d9cc23287e2f49a63021a47deeff&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SH7AP4BP%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQDPVHAeU%2FTMx2GwY4NPxFAFLjkaUl2qEozABX90%2BhDjAAIhAKytW94M1nkKjbfg21gUBFXwBlD8AJEHrRBPR%2F2NQMxeKv8DCDcQABoMNjM3NDIzMTgzODA1Igwlr0wR9elWSmOZyZMq3AOpEGUsA0c3nafWM0iOmrNwrBP2X6FH%2BTojKxo1tUnYj89i0S6HzXR8MKtQ3TERQx0CifEXxMCTcKEtq%2BS3lvVm9xIU4JcTxs%2Fypy%2BvDJDmTmYsmvfopuYZjeZB%2BArcwurM6UoCFtBCGg9pNhoS7sJYZQ3A0KsX8c%2BpOQDDR5WXFSsOS3cNDyXmeTthYTEU0FsX%2BxCe%2FEdwLtH8MYL%2B9RtKSkxgBbKWoudeQbUtlbparxffGeZsK%2FahrDze0F6Gg73WB46JbHipSMkQK%2FfRQst0%2BAK%2F4%2FyetNG6SnzxXmugvyOB4EK4vGgcp%2FhClckdQJd%2FTLE0b1TwBAoLUAw2ydO4VEDYkMgUTmzZ0HjJSWd%2FQRh1%2BgAZ4Q95%2FTBZLWFAWP5smgOONq%2BIwL4wjkPR0VKsPaQqhaRa5ST5dyqXW7MIXdec%2Bgm7mAsjnVIND0DF%2FUmfMJMMB0wOdeEjQQ64WQ9eCRF%2FKBJKq8e8Egqr98XN1HjSZ8Tr9VKmS3vMU%2FUb6iX2oDwZQMnWP8wDyT2Ni42%2FvkxEls5qmdewQXjMN9HB6J1qaovxZagjqk1dlrOszlaVtYMQHvjAP5GOEBUJDuINVMkakxHQzHOHO2MRxcchvd%2Fj8xw8FyeTq8Pd4TCWlIq9BjqkAdVs3W0LxQ1nUDOcbPuBccHlhFyv%2BhWqM92y2TfIq3If8qxGd07eo9G03peX4UEYx3xNA5Rhmpu%2FGGdAYWOw5dpWxLDU2%2FMtlO9FGFG%2BvF0m%2BxrIePmvpeuWBJSP7sDJ2wsj8l3pcUAJtb4Gzki243pitfHraMkxpQFm4285N8QFlL6k5a%2FjQoY%2BZ9mub5uyD1re3GmT0Aoiuhtv0%2BDWH8kCE9FR&X-Amz-Signature=bb76bbd8210bb70e01347f62483655362a668e138e477d1a2c18671320a6cc8c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662BHSR7UD%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJGMEQCIDKEtfF6YNEIY8irhwB4kl%2FRc3%2FQflJtYQ0ezAK3sRqQAiByrk%2FxbmL38TDEzdR2oyrDViu4DVhSVlep2vgkG4EqhSr%2FAwg3EAAaDDYzNzQyMzE4MzgwNSIMZVMRRBUK%2F2KDawv9KtwDsBEMzUvk97fS2yNaRA8rdCVhHtzUl6O8SdSQICX5Z79wqd%2Fcd9e9qe2fmxDn8jmtHmaw1Z0pykmLIR24iMA8sobRbmm9CdWb%2FKzPv3hqXGRX1tuQRz676VNdVu1tWJPob6rVtHVWuo0fFY0jYC3eHPNMcV15DMafUlakuaNiq9Cl7b2dd1OOyHFo8%2B7%2FKfzhOnxfVatZ35joIVEb3gk0j60uk3DgJnx2lmE33ozGnXBVTRY%2BxQv57xfzOiLr71H3mc4VjDpa24Dy%2B%2BRQ1Xg0BXCyTRHSCEkbth65CQLrOWwYS6C9sxVI2xXY1Sm%2BX0wmtz8NR0WOWfrGmlygIweUJyR5T3dmeeU366Pbd%2FSdG0VdgXc5oxyZ15rPegv0lZIWg9Cb%2F%2FBPviRFY90VJZ%2Fb9O1ZnTj4uDS5YXFi6uew8EkFOycHnGuUTLAPPIva1iXiQY6ziXLbe%2Bvm2AgRmmRaTkwfCYfsZSBngWvrwkYbCBWd6vNHIrUksHJXhi%2Fovju294%2FU%2Bx4HKwnydnqleTSNGWzpUawwwdHedI8iOK2QUnh5%2Fy0jX4vsDSTbhkSOXekuk1cNeQJ1WWKAK8wgYaVB2U8%2Bycv7FHJ7%2BVmJHcrShF5YgVHP98md6Lw64qYw2pSKvQY6pgFk180oJZ8IF789YHNoW9t8Iz9scgtZWmGK%2FSasgXLv4eBOY6Knjs1LUTEzofCZY9AO%2Bv5BBLy2CMkDYMWlT0V%2FVo2rjtse1JJA2E2t7Vpz689rZbBOz28Y1KQrdKUsYiqKGcI2EOQGg8VOcrJal2KEvMUNAOW3NHfovMCA4ZQiV9Pd7mxHWBOpnxLR7PMwbFFBFAp7ny%2Fd3mJgwJg8iMcbTxe2%2Bv96&X-Amz-Signature=1b506f5b37ca8dbd0020941e7d692ef407685ff3947371eeac71d2c0ed3978bc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662BHSR7UD%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJGMEQCIDKEtfF6YNEIY8irhwB4kl%2FRc3%2FQflJtYQ0ezAK3sRqQAiByrk%2FxbmL38TDEzdR2oyrDViu4DVhSVlep2vgkG4EqhSr%2FAwg3EAAaDDYzNzQyMzE4MzgwNSIMZVMRRBUK%2F2KDawv9KtwDsBEMzUvk97fS2yNaRA8rdCVhHtzUl6O8SdSQICX5Z79wqd%2Fcd9e9qe2fmxDn8jmtHmaw1Z0pykmLIR24iMA8sobRbmm9CdWb%2FKzPv3hqXGRX1tuQRz676VNdVu1tWJPob6rVtHVWuo0fFY0jYC3eHPNMcV15DMafUlakuaNiq9Cl7b2dd1OOyHFo8%2B7%2FKfzhOnxfVatZ35joIVEb3gk0j60uk3DgJnx2lmE33ozGnXBVTRY%2BxQv57xfzOiLr71H3mc4VjDpa24Dy%2B%2BRQ1Xg0BXCyTRHSCEkbth65CQLrOWwYS6C9sxVI2xXY1Sm%2BX0wmtz8NR0WOWfrGmlygIweUJyR5T3dmeeU366Pbd%2FSdG0VdgXc5oxyZ15rPegv0lZIWg9Cb%2F%2FBPviRFY90VJZ%2Fb9O1ZnTj4uDS5YXFi6uew8EkFOycHnGuUTLAPPIva1iXiQY6ziXLbe%2Bvm2AgRmmRaTkwfCYfsZSBngWvrwkYbCBWd6vNHIrUksHJXhi%2Fovju294%2FU%2Bx4HKwnydnqleTSNGWzpUawwwdHedI8iOK2QUnh5%2Fy0jX4vsDSTbhkSOXekuk1cNeQJ1WWKAK8wgYaVB2U8%2Bycv7FHJ7%2BVmJHcrShF5YgVHP98md6Lw64qYw2pSKvQY6pgFk180oJZ8IF789YHNoW9t8Iz9scgtZWmGK%2FSasgXLv4eBOY6Knjs1LUTEzofCZY9AO%2Bv5BBLy2CMkDYMWlT0V%2FVo2rjtse1JJA2E2t7Vpz689rZbBOz28Y1KQrdKUsYiqKGcI2EOQGg8VOcrJal2KEvMUNAOW3NHfovMCA4ZQiV9Pd7mxHWBOpnxLR7PMwbFFBFAp7ny%2Fd3mJgwJg8iMcbTxe2%2Bv96&X-Amz-Signature=00bbe36cdc067784a0c15739ca04d6ea4933c4f659de9ab499a69c84086fa320&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
