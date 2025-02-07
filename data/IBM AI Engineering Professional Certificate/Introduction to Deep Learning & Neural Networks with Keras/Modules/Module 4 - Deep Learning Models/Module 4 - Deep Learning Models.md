

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663LCJX6YF%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQDEdh7V1B9Wfl7bLzK53wByS8jhyZKsSSE7gh3I6%2BjEXAIgJTK%2BZHWdPLbwAgXL%2BvVsygJvVfCxSSBxeOCtsAD39bgq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDFIDTz6VgmI4Mhx1zSrcA11Q8uhlP8pHMteGEkL1crOmBZxLCNIQj%2BpW6U3kwwtR1oJzecpeLLgffnKbSAd3Kcq7Ji6tEoqFE9iAUzz0To8a%2FRUOVM17nVMlYLaCws3yW4ZCBYr306Io5nS9XUXo1354gGu9eTqZcn5CkUdw08Jo0d3u77oELSbLtR9eH0FmjaWifbOVfzGnnryuNBrD35UQNbUkFMpIsyqc7A1905QmvPJJd%2Fsp8v3BgHHf72Ng5p3GcmtWFydrvPwv%2B%2BPIEJDLdK9%2Fs3khjbGdTspqTqL58KP200nt4M2CQzGMuLEieyeAq1ZNe5xFfFaxYXHIyQoyB%2BJh9Uvd2IO0Qyoffq5%2BCEIR0C%2B0%2BBp2q3f7gFgvd4uo9Dz7ksohIa4B8lu%2BOhY0kzDgU0mXbZR67QKQQf1ZebL70rQaIulQA%2B64slteQ1p2bm8iY1B96QAfiCIewY1w%2Fi8mNt7%2F9GvLQ%2FKuTSPhJYChDxDAWdQ%2Fyje7Oiez%2FPlRcLNoc7sled3EpzQmhtredcbikuBZO7iS52mlQleXWsU%2BQUI%2F%2F5sjPWhhTQHRV9OoJCcy0IIe8DuXvfPhbvjpp8i2QqWB8h8HhCxHDYb4XpygTkwFhUJ29jY1I49p1GolDPJXIF7Y9RowMNX5lr0GOqUBFN1nzHQHWbu7Mte%2BzUAqAe7JkHLtTAFtNPj%2Fe%2FwxGudXXS%2FP6lZCwaN1o1YXITNLtpjkWv9lL49CGfVFchTAKnuuOsrrAzpVHKCShOgjsHnxJg9DUvKVV6AX0H0si%2Bw5C9q3XoYFXKR1TIwP%2Bu4Ld2GMTODr9WcwCjJBISLEvjlVFa2hAJkJWCg5YTNQSfIeSgvkFJE8WJoGNWWfAzdz8B80lWOU&X-Amz-Signature=c8e09a3a3a90b2f6dfbbbcb1c3093f989da6742eed1dc2eab4604e36b15978bb&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663LCJX6YF%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQDEdh7V1B9Wfl7bLzK53wByS8jhyZKsSSE7gh3I6%2BjEXAIgJTK%2BZHWdPLbwAgXL%2BvVsygJvVfCxSSBxeOCtsAD39bgq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDFIDTz6VgmI4Mhx1zSrcA11Q8uhlP8pHMteGEkL1crOmBZxLCNIQj%2BpW6U3kwwtR1oJzecpeLLgffnKbSAd3Kcq7Ji6tEoqFE9iAUzz0To8a%2FRUOVM17nVMlYLaCws3yW4ZCBYr306Io5nS9XUXo1354gGu9eTqZcn5CkUdw08Jo0d3u77oELSbLtR9eH0FmjaWifbOVfzGnnryuNBrD35UQNbUkFMpIsyqc7A1905QmvPJJd%2Fsp8v3BgHHf72Ng5p3GcmtWFydrvPwv%2B%2BPIEJDLdK9%2Fs3khjbGdTspqTqL58KP200nt4M2CQzGMuLEieyeAq1ZNe5xFfFaxYXHIyQoyB%2BJh9Uvd2IO0Qyoffq5%2BCEIR0C%2B0%2BBp2q3f7gFgvd4uo9Dz7ksohIa4B8lu%2BOhY0kzDgU0mXbZR67QKQQf1ZebL70rQaIulQA%2B64slteQ1p2bm8iY1B96QAfiCIewY1w%2Fi8mNt7%2F9GvLQ%2FKuTSPhJYChDxDAWdQ%2Fyje7Oiez%2FPlRcLNoc7sled3EpzQmhtredcbikuBZO7iS52mlQleXWsU%2BQUI%2F%2F5sjPWhhTQHRV9OoJCcy0IIe8DuXvfPhbvjpp8i2QqWB8h8HhCxHDYb4XpygTkwFhUJ29jY1I49p1GolDPJXIF7Y9RowMNX5lr0GOqUBFN1nzHQHWbu7Mte%2BzUAqAe7JkHLtTAFtNPj%2Fe%2FwxGudXXS%2FP6lZCwaN1o1YXITNLtpjkWv9lL49CGfVFchTAKnuuOsrrAzpVHKCShOgjsHnxJg9DUvKVV6AX0H0si%2Bw5C9q3XoYFXKR1TIwP%2Bu4Ld2GMTODr9WcwCjJBISLEvjlVFa2hAJkJWCg5YTNQSfIeSgvkFJE8WJoGNWWfAzdz8B80lWOU&X-Amz-Signature=acec8573e359086b349bea553cca868cfddb64e04a5515cbc7f0d1f9633f81a3&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663LCJX6YF%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQDEdh7V1B9Wfl7bLzK53wByS8jhyZKsSSE7gh3I6%2BjEXAIgJTK%2BZHWdPLbwAgXL%2BvVsygJvVfCxSSBxeOCtsAD39bgq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDFIDTz6VgmI4Mhx1zSrcA11Q8uhlP8pHMteGEkL1crOmBZxLCNIQj%2BpW6U3kwwtR1oJzecpeLLgffnKbSAd3Kcq7Ji6tEoqFE9iAUzz0To8a%2FRUOVM17nVMlYLaCws3yW4ZCBYr306Io5nS9XUXo1354gGu9eTqZcn5CkUdw08Jo0d3u77oELSbLtR9eH0FmjaWifbOVfzGnnryuNBrD35UQNbUkFMpIsyqc7A1905QmvPJJd%2Fsp8v3BgHHf72Ng5p3GcmtWFydrvPwv%2B%2BPIEJDLdK9%2Fs3khjbGdTspqTqL58KP200nt4M2CQzGMuLEieyeAq1ZNe5xFfFaxYXHIyQoyB%2BJh9Uvd2IO0Qyoffq5%2BCEIR0C%2B0%2BBp2q3f7gFgvd4uo9Dz7ksohIa4B8lu%2BOhY0kzDgU0mXbZR67QKQQf1ZebL70rQaIulQA%2B64slteQ1p2bm8iY1B96QAfiCIewY1w%2Fi8mNt7%2F9GvLQ%2FKuTSPhJYChDxDAWdQ%2Fyje7Oiez%2FPlRcLNoc7sled3EpzQmhtredcbikuBZO7iS52mlQleXWsU%2BQUI%2F%2F5sjPWhhTQHRV9OoJCcy0IIe8DuXvfPhbvjpp8i2QqWB8h8HhCxHDYb4XpygTkwFhUJ29jY1I49p1GolDPJXIF7Y9RowMNX5lr0GOqUBFN1nzHQHWbu7Mte%2BzUAqAe7JkHLtTAFtNPj%2Fe%2FwxGudXXS%2FP6lZCwaN1o1YXITNLtpjkWv9lL49CGfVFchTAKnuuOsrrAzpVHKCShOgjsHnxJg9DUvKVV6AX0H0si%2Bw5C9q3XoYFXKR1TIwP%2Bu4Ld2GMTODr9WcwCjJBISLEvjlVFa2hAJkJWCg5YTNQSfIeSgvkFJE8WJoGNWWfAzdz8B80lWOU&X-Amz-Signature=8f38eda5cbed112a3f0d8116e398ec08a0bae239f3fa9aa18194a14e9291867d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663LCJX6YF%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQDEdh7V1B9Wfl7bLzK53wByS8jhyZKsSSE7gh3I6%2BjEXAIgJTK%2BZHWdPLbwAgXL%2BvVsygJvVfCxSSBxeOCtsAD39bgq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDFIDTz6VgmI4Mhx1zSrcA11Q8uhlP8pHMteGEkL1crOmBZxLCNIQj%2BpW6U3kwwtR1oJzecpeLLgffnKbSAd3Kcq7Ji6tEoqFE9iAUzz0To8a%2FRUOVM17nVMlYLaCws3yW4ZCBYr306Io5nS9XUXo1354gGu9eTqZcn5CkUdw08Jo0d3u77oELSbLtR9eH0FmjaWifbOVfzGnnryuNBrD35UQNbUkFMpIsyqc7A1905QmvPJJd%2Fsp8v3BgHHf72Ng5p3GcmtWFydrvPwv%2B%2BPIEJDLdK9%2Fs3khjbGdTspqTqL58KP200nt4M2CQzGMuLEieyeAq1ZNe5xFfFaxYXHIyQoyB%2BJh9Uvd2IO0Qyoffq5%2BCEIR0C%2B0%2BBp2q3f7gFgvd4uo9Dz7ksohIa4B8lu%2BOhY0kzDgU0mXbZR67QKQQf1ZebL70rQaIulQA%2B64slteQ1p2bm8iY1B96QAfiCIewY1w%2Fi8mNt7%2F9GvLQ%2FKuTSPhJYChDxDAWdQ%2Fyje7Oiez%2FPlRcLNoc7sled3EpzQmhtredcbikuBZO7iS52mlQleXWsU%2BQUI%2F%2F5sjPWhhTQHRV9OoJCcy0IIe8DuXvfPhbvjpp8i2QqWB8h8HhCxHDYb4XpygTkwFhUJ29jY1I49p1GolDPJXIF7Y9RowMNX5lr0GOqUBFN1nzHQHWbu7Mte%2BzUAqAe7JkHLtTAFtNPj%2Fe%2FwxGudXXS%2FP6lZCwaN1o1YXITNLtpjkWv9lL49CGfVFchTAKnuuOsrrAzpVHKCShOgjsHnxJg9DUvKVV6AX0H0si%2Bw5C9q3XoYFXKR1TIwP%2Bu4Ld2GMTODr9WcwCjJBISLEvjlVFa2hAJkJWCg5YTNQSfIeSgvkFJE8WJoGNWWfAzdz8B80lWOU&X-Amz-Signature=09e628f7810ad16d9f70e6156f2ea9ca7adcb210b72a48145e0141a448adb7a3&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663LCJX6YF%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQDEdh7V1B9Wfl7bLzK53wByS8jhyZKsSSE7gh3I6%2BjEXAIgJTK%2BZHWdPLbwAgXL%2BvVsygJvVfCxSSBxeOCtsAD39bgq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDFIDTz6VgmI4Mhx1zSrcA11Q8uhlP8pHMteGEkL1crOmBZxLCNIQj%2BpW6U3kwwtR1oJzecpeLLgffnKbSAd3Kcq7Ji6tEoqFE9iAUzz0To8a%2FRUOVM17nVMlYLaCws3yW4ZCBYr306Io5nS9XUXo1354gGu9eTqZcn5CkUdw08Jo0d3u77oELSbLtR9eH0FmjaWifbOVfzGnnryuNBrD35UQNbUkFMpIsyqc7A1905QmvPJJd%2Fsp8v3BgHHf72Ng5p3GcmtWFydrvPwv%2B%2BPIEJDLdK9%2Fs3khjbGdTspqTqL58KP200nt4M2CQzGMuLEieyeAq1ZNe5xFfFaxYXHIyQoyB%2BJh9Uvd2IO0Qyoffq5%2BCEIR0C%2B0%2BBp2q3f7gFgvd4uo9Dz7ksohIa4B8lu%2BOhY0kzDgU0mXbZR67QKQQf1ZebL70rQaIulQA%2B64slteQ1p2bm8iY1B96QAfiCIewY1w%2Fi8mNt7%2F9GvLQ%2FKuTSPhJYChDxDAWdQ%2Fyje7Oiez%2FPlRcLNoc7sled3EpzQmhtredcbikuBZO7iS52mlQleXWsU%2BQUI%2F%2F5sjPWhhTQHRV9OoJCcy0IIe8DuXvfPhbvjpp8i2QqWB8h8HhCxHDYb4XpygTkwFhUJ29jY1I49p1GolDPJXIF7Y9RowMNX5lr0GOqUBFN1nzHQHWbu7Mte%2BzUAqAe7JkHLtTAFtNPj%2Fe%2FwxGudXXS%2FP6lZCwaN1o1YXITNLtpjkWv9lL49CGfVFchTAKnuuOsrrAzpVHKCShOgjsHnxJg9DUvKVV6AX0H0si%2Bw5C9q3XoYFXKR1TIwP%2Bu4Ld2GMTODr9WcwCjJBISLEvjlVFa2hAJkJWCg5YTNQSfIeSgvkFJE8WJoGNWWfAzdz8B80lWOU&X-Amz-Signature=a1372b500454115f22f38f1e7bd218336a39f441391452f8c73df34868fd104b&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663LCJX6YF%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQDEdh7V1B9Wfl7bLzK53wByS8jhyZKsSSE7gh3I6%2BjEXAIgJTK%2BZHWdPLbwAgXL%2BvVsygJvVfCxSSBxeOCtsAD39bgq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDFIDTz6VgmI4Mhx1zSrcA11Q8uhlP8pHMteGEkL1crOmBZxLCNIQj%2BpW6U3kwwtR1oJzecpeLLgffnKbSAd3Kcq7Ji6tEoqFE9iAUzz0To8a%2FRUOVM17nVMlYLaCws3yW4ZCBYr306Io5nS9XUXo1354gGu9eTqZcn5CkUdw08Jo0d3u77oELSbLtR9eH0FmjaWifbOVfzGnnryuNBrD35UQNbUkFMpIsyqc7A1905QmvPJJd%2Fsp8v3BgHHf72Ng5p3GcmtWFydrvPwv%2B%2BPIEJDLdK9%2Fs3khjbGdTspqTqL58KP200nt4M2CQzGMuLEieyeAq1ZNe5xFfFaxYXHIyQoyB%2BJh9Uvd2IO0Qyoffq5%2BCEIR0C%2B0%2BBp2q3f7gFgvd4uo9Dz7ksohIa4B8lu%2BOhY0kzDgU0mXbZR67QKQQf1ZebL70rQaIulQA%2B64slteQ1p2bm8iY1B96QAfiCIewY1w%2Fi8mNt7%2F9GvLQ%2FKuTSPhJYChDxDAWdQ%2Fyje7Oiez%2FPlRcLNoc7sled3EpzQmhtredcbikuBZO7iS52mlQleXWsU%2BQUI%2F%2F5sjPWhhTQHRV9OoJCcy0IIe8DuXvfPhbvjpp8i2QqWB8h8HhCxHDYb4XpygTkwFhUJ29jY1I49p1GolDPJXIF7Y9RowMNX5lr0GOqUBFN1nzHQHWbu7Mte%2BzUAqAe7JkHLtTAFtNPj%2Fe%2FwxGudXXS%2FP6lZCwaN1o1YXITNLtpjkWv9lL49CGfVFchTAKnuuOsrrAzpVHKCShOgjsHnxJg9DUvKVV6AX0H0si%2Bw5C9q3XoYFXKR1TIwP%2Bu4Ld2GMTODr9WcwCjJBISLEvjlVFa2hAJkJWCg5YTNQSfIeSgvkFJE8WJoGNWWfAzdz8B80lWOU&X-Amz-Signature=a009fc6eccc27db533dcd328ecd51a2aafeee5a55216ccc9a735544bd05ed6b9&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663LCJX6YF%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQDEdh7V1B9Wfl7bLzK53wByS8jhyZKsSSE7gh3I6%2BjEXAIgJTK%2BZHWdPLbwAgXL%2BvVsygJvVfCxSSBxeOCtsAD39bgq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDFIDTz6VgmI4Mhx1zSrcA11Q8uhlP8pHMteGEkL1crOmBZxLCNIQj%2BpW6U3kwwtR1oJzecpeLLgffnKbSAd3Kcq7Ji6tEoqFE9iAUzz0To8a%2FRUOVM17nVMlYLaCws3yW4ZCBYr306Io5nS9XUXo1354gGu9eTqZcn5CkUdw08Jo0d3u77oELSbLtR9eH0FmjaWifbOVfzGnnryuNBrD35UQNbUkFMpIsyqc7A1905QmvPJJd%2Fsp8v3BgHHf72Ng5p3GcmtWFydrvPwv%2B%2BPIEJDLdK9%2Fs3khjbGdTspqTqL58KP200nt4M2CQzGMuLEieyeAq1ZNe5xFfFaxYXHIyQoyB%2BJh9Uvd2IO0Qyoffq5%2BCEIR0C%2B0%2BBp2q3f7gFgvd4uo9Dz7ksohIa4B8lu%2BOhY0kzDgU0mXbZR67QKQQf1ZebL70rQaIulQA%2B64slteQ1p2bm8iY1B96QAfiCIewY1w%2Fi8mNt7%2F9GvLQ%2FKuTSPhJYChDxDAWdQ%2Fyje7Oiez%2FPlRcLNoc7sled3EpzQmhtredcbikuBZO7iS52mlQleXWsU%2BQUI%2F%2F5sjPWhhTQHRV9OoJCcy0IIe8DuXvfPhbvjpp8i2QqWB8h8HhCxHDYb4XpygTkwFhUJ29jY1I49p1GolDPJXIF7Y9RowMNX5lr0GOqUBFN1nzHQHWbu7Mte%2BzUAqAe7JkHLtTAFtNPj%2Fe%2FwxGudXXS%2FP6lZCwaN1o1YXITNLtpjkWv9lL49CGfVFchTAKnuuOsrrAzpVHKCShOgjsHnxJg9DUvKVV6AX0H0si%2Bw5C9q3XoYFXKR1TIwP%2Bu4Ld2GMTODr9WcwCjJBISLEvjlVFa2hAJkJWCg5YTNQSfIeSgvkFJE8WJoGNWWfAzdz8B80lWOU&X-Amz-Signature=e891cbc9b0ef50b48528128490967bf409cc13a124eabf9782f1171f63192971&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663LCJX6YF%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQDEdh7V1B9Wfl7bLzK53wByS8jhyZKsSSE7gh3I6%2BjEXAIgJTK%2BZHWdPLbwAgXL%2BvVsygJvVfCxSSBxeOCtsAD39bgq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDFIDTz6VgmI4Mhx1zSrcA11Q8uhlP8pHMteGEkL1crOmBZxLCNIQj%2BpW6U3kwwtR1oJzecpeLLgffnKbSAd3Kcq7Ji6tEoqFE9iAUzz0To8a%2FRUOVM17nVMlYLaCws3yW4ZCBYr306Io5nS9XUXo1354gGu9eTqZcn5CkUdw08Jo0d3u77oELSbLtR9eH0FmjaWifbOVfzGnnryuNBrD35UQNbUkFMpIsyqc7A1905QmvPJJd%2Fsp8v3BgHHf72Ng5p3GcmtWFydrvPwv%2B%2BPIEJDLdK9%2Fs3khjbGdTspqTqL58KP200nt4M2CQzGMuLEieyeAq1ZNe5xFfFaxYXHIyQoyB%2BJh9Uvd2IO0Qyoffq5%2BCEIR0C%2B0%2BBp2q3f7gFgvd4uo9Dz7ksohIa4B8lu%2BOhY0kzDgU0mXbZR67QKQQf1ZebL70rQaIulQA%2B64slteQ1p2bm8iY1B96QAfiCIewY1w%2Fi8mNt7%2F9GvLQ%2FKuTSPhJYChDxDAWdQ%2Fyje7Oiez%2FPlRcLNoc7sled3EpzQmhtredcbikuBZO7iS52mlQleXWsU%2BQUI%2F%2F5sjPWhhTQHRV9OoJCcy0IIe8DuXvfPhbvjpp8i2QqWB8h8HhCxHDYb4XpygTkwFhUJ29jY1I49p1GolDPJXIF7Y9RowMNX5lr0GOqUBFN1nzHQHWbu7Mte%2BzUAqAe7JkHLtTAFtNPj%2Fe%2FwxGudXXS%2FP6lZCwaN1o1YXITNLtpjkWv9lL49CGfVFchTAKnuuOsrrAzpVHKCShOgjsHnxJg9DUvKVV6AX0H0si%2Bw5C9q3XoYFXKR1TIwP%2Bu4Ld2GMTODr9WcwCjJBISLEvjlVFa2hAJkJWCg5YTNQSfIeSgvkFJE8WJoGNWWfAzdz8B80lWOU&X-Amz-Signature=876c646ea5466d90e13b4d0a4d7f68de28952beee945214c031b33ffa36bc657&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663LCJX6YF%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQDEdh7V1B9Wfl7bLzK53wByS8jhyZKsSSE7gh3I6%2BjEXAIgJTK%2BZHWdPLbwAgXL%2BvVsygJvVfCxSSBxeOCtsAD39bgq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDFIDTz6VgmI4Mhx1zSrcA11Q8uhlP8pHMteGEkL1crOmBZxLCNIQj%2BpW6U3kwwtR1oJzecpeLLgffnKbSAd3Kcq7Ji6tEoqFE9iAUzz0To8a%2FRUOVM17nVMlYLaCws3yW4ZCBYr306Io5nS9XUXo1354gGu9eTqZcn5CkUdw08Jo0d3u77oELSbLtR9eH0FmjaWifbOVfzGnnryuNBrD35UQNbUkFMpIsyqc7A1905QmvPJJd%2Fsp8v3BgHHf72Ng5p3GcmtWFydrvPwv%2B%2BPIEJDLdK9%2Fs3khjbGdTspqTqL58KP200nt4M2CQzGMuLEieyeAq1ZNe5xFfFaxYXHIyQoyB%2BJh9Uvd2IO0Qyoffq5%2BCEIR0C%2B0%2BBp2q3f7gFgvd4uo9Dz7ksohIa4B8lu%2BOhY0kzDgU0mXbZR67QKQQf1ZebL70rQaIulQA%2B64slteQ1p2bm8iY1B96QAfiCIewY1w%2Fi8mNt7%2F9GvLQ%2FKuTSPhJYChDxDAWdQ%2Fyje7Oiez%2FPlRcLNoc7sled3EpzQmhtredcbikuBZO7iS52mlQleXWsU%2BQUI%2F%2F5sjPWhhTQHRV9OoJCcy0IIe8DuXvfPhbvjpp8i2QqWB8h8HhCxHDYb4XpygTkwFhUJ29jY1I49p1GolDPJXIF7Y9RowMNX5lr0GOqUBFN1nzHQHWbu7Mte%2BzUAqAe7JkHLtTAFtNPj%2Fe%2FwxGudXXS%2FP6lZCwaN1o1YXITNLtpjkWv9lL49CGfVFchTAKnuuOsrrAzpVHKCShOgjsHnxJg9DUvKVV6AX0H0si%2Bw5C9q3XoYFXKR1TIwP%2Bu4Ld2GMTODr9WcwCjJBISLEvjlVFa2hAJkJWCg5YTNQSfIeSgvkFJE8WJoGNWWfAzdz8B80lWOU&X-Amz-Signature=f9d47334e214a8cdfa3ae6e812c52636293521a6da0fce145d40ad83dc605852&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZPD2L5I6%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCID4%2BS0omqm8kwW5y0HaZQnauUkonIbOwF3AzECMWJKbjAiALSTQcMgqu8NJueqeFaghJLGuVQk1JgtGuj49Pe5xNOir%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIM3Hprk3MYZfUL%2BjGRKtwDww9zgXPNY%2Bj0jq2SCnCAes5ut2CF%2BECzs41KmdEFJB7OTcts2%2BNyhTN8hKDFpknn%2BHCJ1TDiEE0vwjtQK79%2FoX9Y5B0bnfqcpn4ll1ed2iaphdw8On7o2Hd6KeONeuLAz4rgPJJN733Y%2B941wqKfUStrabaiCiCAN68042UMxp4xsbbhxTMmPhCydAoKcWymrfiF73cSyfACvQA1IAwwnJMAkMJVtTAEXI5alF9DUFc3ccOl%2FgYp2dM2Jjqak%2BSQ%2Bhq6PzFwugdVKo0wU6qMymlZOEFviDv0jPtyptj6%2BP%2F3lxXQ1gugVYhoOCBKI3GKhCN9p16OoqC1i1DbdiArS40tlqNvv9hPPg1FKFWy%2FGJdrtzakVHEgvTHGXyAYPgEFM2DIi3RMXI%2B9d6W%2Blh1z03XZYB8eVZ%2Fc1UGujt5J7koO6YasD59Kbq1YvlUaCyafWDJb2gn%2FBkJTyJ5beqdLhaHwT7vSYijTqZqvC4%2BoJG80tx727tAYbKZ%2BtOwT8iSd1CPrwJYiVVwC6dH%2FaTEnY490lC0W16F7IWU6VjgzAyKk8IgJaM16W1%2BtAXcQh1ipE6cmvEHESawrftn7fDj0QIjz3Fof8Q4gjvNP%2BB0sXOM0fQt1WigTxHLunww8vmWvQY6pgFNgJ%2FAQPYjx06zTssLSnHsIm%2FhUCrijKNEZjae7YHvT7Sev1h4Xug5utmMBfCkCzMoruvaNFacCS5J2QX7Z8P0PBg0lyIj1zeubpFEwgXAaXYkKTiktCdef0gbwiUiEGmrgGMJppchdc8eIDvVSAEZNZm7MtnjqkYAfz%2FcQVLRHEckm4TzClGAzwGoWwoMJxrRytgoKK3rPPXzzar2nj7ogXqWUoFI&X-Amz-Signature=252ca9642e46cc8940a815f06c1f40c913c2b5a3a60a387487364bd8c1aed177&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZPD2L5I6%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCID4%2BS0omqm8kwW5y0HaZQnauUkonIbOwF3AzECMWJKbjAiALSTQcMgqu8NJueqeFaghJLGuVQk1JgtGuj49Pe5xNOir%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIM3Hprk3MYZfUL%2BjGRKtwDww9zgXPNY%2Bj0jq2SCnCAes5ut2CF%2BECzs41KmdEFJB7OTcts2%2BNyhTN8hKDFpknn%2BHCJ1TDiEE0vwjtQK79%2FoX9Y5B0bnfqcpn4ll1ed2iaphdw8On7o2Hd6KeONeuLAz4rgPJJN733Y%2B941wqKfUStrabaiCiCAN68042UMxp4xsbbhxTMmPhCydAoKcWymrfiF73cSyfACvQA1IAwwnJMAkMJVtTAEXI5alF9DUFc3ccOl%2FgYp2dM2Jjqak%2BSQ%2Bhq6PzFwugdVKo0wU6qMymlZOEFviDv0jPtyptj6%2BP%2F3lxXQ1gugVYhoOCBKI3GKhCN9p16OoqC1i1DbdiArS40tlqNvv9hPPg1FKFWy%2FGJdrtzakVHEgvTHGXyAYPgEFM2DIi3RMXI%2B9d6W%2Blh1z03XZYB8eVZ%2Fc1UGujt5J7koO6YasD59Kbq1YvlUaCyafWDJb2gn%2FBkJTyJ5beqdLhaHwT7vSYijTqZqvC4%2BoJG80tx727tAYbKZ%2BtOwT8iSd1CPrwJYiVVwC6dH%2FaTEnY490lC0W16F7IWU6VjgzAyKk8IgJaM16W1%2BtAXcQh1ipE6cmvEHESawrftn7fDj0QIjz3Fof8Q4gjvNP%2BB0sXOM0fQt1WigTxHLunww8vmWvQY6pgFNgJ%2FAQPYjx06zTssLSnHsIm%2FhUCrijKNEZjae7YHvT7Sev1h4Xug5utmMBfCkCzMoruvaNFacCS5J2QX7Z8P0PBg0lyIj1zeubpFEwgXAaXYkKTiktCdef0gbwiUiEGmrgGMJppchdc8eIDvVSAEZNZm7MtnjqkYAfz%2FcQVLRHEckm4TzClGAzwGoWwoMJxrRytgoKK3rPPXzzar2nj7ogXqWUoFI&X-Amz-Signature=34adef1a2ae09e0bb6042a6cf1f8e9aef20b927320fb5fa8cbf147c4bc804000&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
