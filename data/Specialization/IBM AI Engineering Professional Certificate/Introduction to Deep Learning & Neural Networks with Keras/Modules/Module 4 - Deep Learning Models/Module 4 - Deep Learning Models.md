

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663M3U3CTQ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCuTaddjYVhItW9yi3a%2BJL3k2BPLUrpZRNvhShJ3ELeYAIgZwHYGO7QcpvzG6q4%2FIVqxhef0LBfUJQIux4VCJfN%2B70qiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI%2B0si3Xzgpwla4OQSrcA6rGwtqt2gqCffnQX27rUvtLOIbiyTNwYnoKa3CntOcdRlNTAomkXDSGJhmdOrZnTnwHmyIiSsSFAunAMrRPYWqVmgcUSkOLQGmdfPNNr9OboYIiG60BXadYG04CxP97MXNp%2Br1kRjpvBynIQD9v%2FMuGuyy1Zw7n89tmXFD%2FCydU68bX5OKNP2gQQ3D%2F2oZ8BiCY29b6pXdLS2TULBVVFFlH8XBhCnMRX%2BBtM0sbelLIQWYmMhlEJ%2FUuJ1uY921rbq8DGp3baPEor1PJX5X%2B0Bx%2F3gHey4wlGFxxsd3gcj%2FyZnY80s9%2Fh15HhfLgetLl6dVMhkcL6ntEsCJ8nZuVAV69UaDTe9shZVZW2fDbonYlT7EWBpuYyfb2cGkn0zhbu%2FEQ%2B%2F%2B2INWEQ%2F78QEjDOw%2FK8TBo%2FEb9eEMc3A6mjDEWgheBsyajavxy3Y4%2Fyjveec%2FCAfUe3eLF9pYAWmvUllIpd5IPfNQ%2F19qzNqZjgZlaeE5ennoWXXMZfUrR2eFHPfZPcicCdZMJZfKnBEeumx1NBV46U2%2FTFk2kt%2BjXPiPFjLM5GwOUltcBsJ4%2BMqAbsrZdjc0AnEb0wVWJkXBxwfTk8mD1LNLQYkJHUhZ%2FOOrvLRWkdqsx8Y4SBY57MJnQ8LwGOqUBvBWXfKBsmkv8c%2FCERBYenhMlisDqz8QZNDkQwWF%2BOJFYqcZ56yFLIH%2FjaVMLo%2BtwHKaGBHFFZLNBhDaILd3y3NZ5vdRu4iF%2B8VWplMG3Vo9I%2B2J4fgak%2FjnUH%2BicVhTgG%2FZJnxedQT7Qt%2BxilvwlnXodlbtZB8wjmbcDUK6WlKkFt8nsKsOnLA6BCaFwRFrXnvBz2Dpjc9TFtlrNLcVlZqFwSASg&X-Amz-Signature=cb3dd2ffc30c5a1886d34e53ecdb64bd9f0aab6d64d96454bd8e260663ac57e2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663M3U3CTQ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCuTaddjYVhItW9yi3a%2BJL3k2BPLUrpZRNvhShJ3ELeYAIgZwHYGO7QcpvzG6q4%2FIVqxhef0LBfUJQIux4VCJfN%2B70qiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI%2B0si3Xzgpwla4OQSrcA6rGwtqt2gqCffnQX27rUvtLOIbiyTNwYnoKa3CntOcdRlNTAomkXDSGJhmdOrZnTnwHmyIiSsSFAunAMrRPYWqVmgcUSkOLQGmdfPNNr9OboYIiG60BXadYG04CxP97MXNp%2Br1kRjpvBynIQD9v%2FMuGuyy1Zw7n89tmXFD%2FCydU68bX5OKNP2gQQ3D%2F2oZ8BiCY29b6pXdLS2TULBVVFFlH8XBhCnMRX%2BBtM0sbelLIQWYmMhlEJ%2FUuJ1uY921rbq8DGp3baPEor1PJX5X%2B0Bx%2F3gHey4wlGFxxsd3gcj%2FyZnY80s9%2Fh15HhfLgetLl6dVMhkcL6ntEsCJ8nZuVAV69UaDTe9shZVZW2fDbonYlT7EWBpuYyfb2cGkn0zhbu%2FEQ%2B%2F%2B2INWEQ%2F78QEjDOw%2FK8TBo%2FEb9eEMc3A6mjDEWgheBsyajavxy3Y4%2Fyjveec%2FCAfUe3eLF9pYAWmvUllIpd5IPfNQ%2F19qzNqZjgZlaeE5ennoWXXMZfUrR2eFHPfZPcicCdZMJZfKnBEeumx1NBV46U2%2FTFk2kt%2BjXPiPFjLM5GwOUltcBsJ4%2BMqAbsrZdjc0AnEb0wVWJkXBxwfTk8mD1LNLQYkJHUhZ%2FOOrvLRWkdqsx8Y4SBY57MJnQ8LwGOqUBvBWXfKBsmkv8c%2FCERBYenhMlisDqz8QZNDkQwWF%2BOJFYqcZ56yFLIH%2FjaVMLo%2BtwHKaGBHFFZLNBhDaILd3y3NZ5vdRu4iF%2B8VWplMG3Vo9I%2B2J4fgak%2FjnUH%2BicVhTgG%2FZJnxedQT7Qt%2BxilvwlnXodlbtZB8wjmbcDUK6WlKkFt8nsKsOnLA6BCaFwRFrXnvBz2Dpjc9TFtlrNLcVlZqFwSASg&X-Amz-Signature=5afbfc2a1f76b842f3218706167ad2e9d915dccf6704637c5b18cf441a4056ef&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663M3U3CTQ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCuTaddjYVhItW9yi3a%2BJL3k2BPLUrpZRNvhShJ3ELeYAIgZwHYGO7QcpvzG6q4%2FIVqxhef0LBfUJQIux4VCJfN%2B70qiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI%2B0si3Xzgpwla4OQSrcA6rGwtqt2gqCffnQX27rUvtLOIbiyTNwYnoKa3CntOcdRlNTAomkXDSGJhmdOrZnTnwHmyIiSsSFAunAMrRPYWqVmgcUSkOLQGmdfPNNr9OboYIiG60BXadYG04CxP97MXNp%2Br1kRjpvBynIQD9v%2FMuGuyy1Zw7n89tmXFD%2FCydU68bX5OKNP2gQQ3D%2F2oZ8BiCY29b6pXdLS2TULBVVFFlH8XBhCnMRX%2BBtM0sbelLIQWYmMhlEJ%2FUuJ1uY921rbq8DGp3baPEor1PJX5X%2B0Bx%2F3gHey4wlGFxxsd3gcj%2FyZnY80s9%2Fh15HhfLgetLl6dVMhkcL6ntEsCJ8nZuVAV69UaDTe9shZVZW2fDbonYlT7EWBpuYyfb2cGkn0zhbu%2FEQ%2B%2F%2B2INWEQ%2F78QEjDOw%2FK8TBo%2FEb9eEMc3A6mjDEWgheBsyajavxy3Y4%2Fyjveec%2FCAfUe3eLF9pYAWmvUllIpd5IPfNQ%2F19qzNqZjgZlaeE5ennoWXXMZfUrR2eFHPfZPcicCdZMJZfKnBEeumx1NBV46U2%2FTFk2kt%2BjXPiPFjLM5GwOUltcBsJ4%2BMqAbsrZdjc0AnEb0wVWJkXBxwfTk8mD1LNLQYkJHUhZ%2FOOrvLRWkdqsx8Y4SBY57MJnQ8LwGOqUBvBWXfKBsmkv8c%2FCERBYenhMlisDqz8QZNDkQwWF%2BOJFYqcZ56yFLIH%2FjaVMLo%2BtwHKaGBHFFZLNBhDaILd3y3NZ5vdRu4iF%2B8VWplMG3Vo9I%2B2J4fgak%2FjnUH%2BicVhTgG%2FZJnxedQT7Qt%2BxilvwlnXodlbtZB8wjmbcDUK6WlKkFt8nsKsOnLA6BCaFwRFrXnvBz2Dpjc9TFtlrNLcVlZqFwSASg&X-Amz-Signature=aaa5c78e12d7c79beaebedf423597049f68129813db6fd4c310df4ca52e7d718&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663M3U3CTQ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCuTaddjYVhItW9yi3a%2BJL3k2BPLUrpZRNvhShJ3ELeYAIgZwHYGO7QcpvzG6q4%2FIVqxhef0LBfUJQIux4VCJfN%2B70qiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI%2B0si3Xzgpwla4OQSrcA6rGwtqt2gqCffnQX27rUvtLOIbiyTNwYnoKa3CntOcdRlNTAomkXDSGJhmdOrZnTnwHmyIiSsSFAunAMrRPYWqVmgcUSkOLQGmdfPNNr9OboYIiG60BXadYG04CxP97MXNp%2Br1kRjpvBynIQD9v%2FMuGuyy1Zw7n89tmXFD%2FCydU68bX5OKNP2gQQ3D%2F2oZ8BiCY29b6pXdLS2TULBVVFFlH8XBhCnMRX%2BBtM0sbelLIQWYmMhlEJ%2FUuJ1uY921rbq8DGp3baPEor1PJX5X%2B0Bx%2F3gHey4wlGFxxsd3gcj%2FyZnY80s9%2Fh15HhfLgetLl6dVMhkcL6ntEsCJ8nZuVAV69UaDTe9shZVZW2fDbonYlT7EWBpuYyfb2cGkn0zhbu%2FEQ%2B%2F%2B2INWEQ%2F78QEjDOw%2FK8TBo%2FEb9eEMc3A6mjDEWgheBsyajavxy3Y4%2Fyjveec%2FCAfUe3eLF9pYAWmvUllIpd5IPfNQ%2F19qzNqZjgZlaeE5ennoWXXMZfUrR2eFHPfZPcicCdZMJZfKnBEeumx1NBV46U2%2FTFk2kt%2BjXPiPFjLM5GwOUltcBsJ4%2BMqAbsrZdjc0AnEb0wVWJkXBxwfTk8mD1LNLQYkJHUhZ%2FOOrvLRWkdqsx8Y4SBY57MJnQ8LwGOqUBvBWXfKBsmkv8c%2FCERBYenhMlisDqz8QZNDkQwWF%2BOJFYqcZ56yFLIH%2FjaVMLo%2BtwHKaGBHFFZLNBhDaILd3y3NZ5vdRu4iF%2B8VWplMG3Vo9I%2B2J4fgak%2FjnUH%2BicVhTgG%2FZJnxedQT7Qt%2BxilvwlnXodlbtZB8wjmbcDUK6WlKkFt8nsKsOnLA6BCaFwRFrXnvBz2Dpjc9TFtlrNLcVlZqFwSASg&X-Amz-Signature=4fa0cd3bb4a2def257d201f849c0d9c35eeefaed99e2cdedf27335e2dccdcf48&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663M3U3CTQ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCuTaddjYVhItW9yi3a%2BJL3k2BPLUrpZRNvhShJ3ELeYAIgZwHYGO7QcpvzG6q4%2FIVqxhef0LBfUJQIux4VCJfN%2B70qiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI%2B0si3Xzgpwla4OQSrcA6rGwtqt2gqCffnQX27rUvtLOIbiyTNwYnoKa3CntOcdRlNTAomkXDSGJhmdOrZnTnwHmyIiSsSFAunAMrRPYWqVmgcUSkOLQGmdfPNNr9OboYIiG60BXadYG04CxP97MXNp%2Br1kRjpvBynIQD9v%2FMuGuyy1Zw7n89tmXFD%2FCydU68bX5OKNP2gQQ3D%2F2oZ8BiCY29b6pXdLS2TULBVVFFlH8XBhCnMRX%2BBtM0sbelLIQWYmMhlEJ%2FUuJ1uY921rbq8DGp3baPEor1PJX5X%2B0Bx%2F3gHey4wlGFxxsd3gcj%2FyZnY80s9%2Fh15HhfLgetLl6dVMhkcL6ntEsCJ8nZuVAV69UaDTe9shZVZW2fDbonYlT7EWBpuYyfb2cGkn0zhbu%2FEQ%2B%2F%2B2INWEQ%2F78QEjDOw%2FK8TBo%2FEb9eEMc3A6mjDEWgheBsyajavxy3Y4%2Fyjveec%2FCAfUe3eLF9pYAWmvUllIpd5IPfNQ%2F19qzNqZjgZlaeE5ennoWXXMZfUrR2eFHPfZPcicCdZMJZfKnBEeumx1NBV46U2%2FTFk2kt%2BjXPiPFjLM5GwOUltcBsJ4%2BMqAbsrZdjc0AnEb0wVWJkXBxwfTk8mD1LNLQYkJHUhZ%2FOOrvLRWkdqsx8Y4SBY57MJnQ8LwGOqUBvBWXfKBsmkv8c%2FCERBYenhMlisDqz8QZNDkQwWF%2BOJFYqcZ56yFLIH%2FjaVMLo%2BtwHKaGBHFFZLNBhDaILd3y3NZ5vdRu4iF%2B8VWplMG3Vo9I%2B2J4fgak%2FjnUH%2BicVhTgG%2FZJnxedQT7Qt%2BxilvwlnXodlbtZB8wjmbcDUK6WlKkFt8nsKsOnLA6BCaFwRFrXnvBz2Dpjc9TFtlrNLcVlZqFwSASg&X-Amz-Signature=f7246ec7b750595b864e397f1b9cf0620a0a145192238ecea38ab2c17fc5722f&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663M3U3CTQ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCuTaddjYVhItW9yi3a%2BJL3k2BPLUrpZRNvhShJ3ELeYAIgZwHYGO7QcpvzG6q4%2FIVqxhef0LBfUJQIux4VCJfN%2B70qiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI%2B0si3Xzgpwla4OQSrcA6rGwtqt2gqCffnQX27rUvtLOIbiyTNwYnoKa3CntOcdRlNTAomkXDSGJhmdOrZnTnwHmyIiSsSFAunAMrRPYWqVmgcUSkOLQGmdfPNNr9OboYIiG60BXadYG04CxP97MXNp%2Br1kRjpvBynIQD9v%2FMuGuyy1Zw7n89tmXFD%2FCydU68bX5OKNP2gQQ3D%2F2oZ8BiCY29b6pXdLS2TULBVVFFlH8XBhCnMRX%2BBtM0sbelLIQWYmMhlEJ%2FUuJ1uY921rbq8DGp3baPEor1PJX5X%2B0Bx%2F3gHey4wlGFxxsd3gcj%2FyZnY80s9%2Fh15HhfLgetLl6dVMhkcL6ntEsCJ8nZuVAV69UaDTe9shZVZW2fDbonYlT7EWBpuYyfb2cGkn0zhbu%2FEQ%2B%2F%2B2INWEQ%2F78QEjDOw%2FK8TBo%2FEb9eEMc3A6mjDEWgheBsyajavxy3Y4%2Fyjveec%2FCAfUe3eLF9pYAWmvUllIpd5IPfNQ%2F19qzNqZjgZlaeE5ennoWXXMZfUrR2eFHPfZPcicCdZMJZfKnBEeumx1NBV46U2%2FTFk2kt%2BjXPiPFjLM5GwOUltcBsJ4%2BMqAbsrZdjc0AnEb0wVWJkXBxwfTk8mD1LNLQYkJHUhZ%2FOOrvLRWkdqsx8Y4SBY57MJnQ8LwGOqUBvBWXfKBsmkv8c%2FCERBYenhMlisDqz8QZNDkQwWF%2BOJFYqcZ56yFLIH%2FjaVMLo%2BtwHKaGBHFFZLNBhDaILd3y3NZ5vdRu4iF%2B8VWplMG3Vo9I%2B2J4fgak%2FjnUH%2BicVhTgG%2FZJnxedQT7Qt%2BxilvwlnXodlbtZB8wjmbcDUK6WlKkFt8nsKsOnLA6BCaFwRFrXnvBz2Dpjc9TFtlrNLcVlZqFwSASg&X-Amz-Signature=389e20c31c8ab4b639ea229e02d26460ec67a1846a0f7c281b61ac12a54c1943&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663M3U3CTQ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCuTaddjYVhItW9yi3a%2BJL3k2BPLUrpZRNvhShJ3ELeYAIgZwHYGO7QcpvzG6q4%2FIVqxhef0LBfUJQIux4VCJfN%2B70qiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI%2B0si3Xzgpwla4OQSrcA6rGwtqt2gqCffnQX27rUvtLOIbiyTNwYnoKa3CntOcdRlNTAomkXDSGJhmdOrZnTnwHmyIiSsSFAunAMrRPYWqVmgcUSkOLQGmdfPNNr9OboYIiG60BXadYG04CxP97MXNp%2Br1kRjpvBynIQD9v%2FMuGuyy1Zw7n89tmXFD%2FCydU68bX5OKNP2gQQ3D%2F2oZ8BiCY29b6pXdLS2TULBVVFFlH8XBhCnMRX%2BBtM0sbelLIQWYmMhlEJ%2FUuJ1uY921rbq8DGp3baPEor1PJX5X%2B0Bx%2F3gHey4wlGFxxsd3gcj%2FyZnY80s9%2Fh15HhfLgetLl6dVMhkcL6ntEsCJ8nZuVAV69UaDTe9shZVZW2fDbonYlT7EWBpuYyfb2cGkn0zhbu%2FEQ%2B%2F%2B2INWEQ%2F78QEjDOw%2FK8TBo%2FEb9eEMc3A6mjDEWgheBsyajavxy3Y4%2Fyjveec%2FCAfUe3eLF9pYAWmvUllIpd5IPfNQ%2F19qzNqZjgZlaeE5ennoWXXMZfUrR2eFHPfZPcicCdZMJZfKnBEeumx1NBV46U2%2FTFk2kt%2BjXPiPFjLM5GwOUltcBsJ4%2BMqAbsrZdjc0AnEb0wVWJkXBxwfTk8mD1LNLQYkJHUhZ%2FOOrvLRWkdqsx8Y4SBY57MJnQ8LwGOqUBvBWXfKBsmkv8c%2FCERBYenhMlisDqz8QZNDkQwWF%2BOJFYqcZ56yFLIH%2FjaVMLo%2BtwHKaGBHFFZLNBhDaILd3y3NZ5vdRu4iF%2B8VWplMG3Vo9I%2B2J4fgak%2FjnUH%2BicVhTgG%2FZJnxedQT7Qt%2BxilvwlnXodlbtZB8wjmbcDUK6WlKkFt8nsKsOnLA6BCaFwRFrXnvBz2Dpjc9TFtlrNLcVlZqFwSASg&X-Amz-Signature=60cc1d09c7c505f467a23873b70471cc46664227e3b2c28c7746235153c201b6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663M3U3CTQ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCuTaddjYVhItW9yi3a%2BJL3k2BPLUrpZRNvhShJ3ELeYAIgZwHYGO7QcpvzG6q4%2FIVqxhef0LBfUJQIux4VCJfN%2B70qiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI%2B0si3Xzgpwla4OQSrcA6rGwtqt2gqCffnQX27rUvtLOIbiyTNwYnoKa3CntOcdRlNTAomkXDSGJhmdOrZnTnwHmyIiSsSFAunAMrRPYWqVmgcUSkOLQGmdfPNNr9OboYIiG60BXadYG04CxP97MXNp%2Br1kRjpvBynIQD9v%2FMuGuyy1Zw7n89tmXFD%2FCydU68bX5OKNP2gQQ3D%2F2oZ8BiCY29b6pXdLS2TULBVVFFlH8XBhCnMRX%2BBtM0sbelLIQWYmMhlEJ%2FUuJ1uY921rbq8DGp3baPEor1PJX5X%2B0Bx%2F3gHey4wlGFxxsd3gcj%2FyZnY80s9%2Fh15HhfLgetLl6dVMhkcL6ntEsCJ8nZuVAV69UaDTe9shZVZW2fDbonYlT7EWBpuYyfb2cGkn0zhbu%2FEQ%2B%2F%2B2INWEQ%2F78QEjDOw%2FK8TBo%2FEb9eEMc3A6mjDEWgheBsyajavxy3Y4%2Fyjveec%2FCAfUe3eLF9pYAWmvUllIpd5IPfNQ%2F19qzNqZjgZlaeE5ennoWXXMZfUrR2eFHPfZPcicCdZMJZfKnBEeumx1NBV46U2%2FTFk2kt%2BjXPiPFjLM5GwOUltcBsJ4%2BMqAbsrZdjc0AnEb0wVWJkXBxwfTk8mD1LNLQYkJHUhZ%2FOOrvLRWkdqsx8Y4SBY57MJnQ8LwGOqUBvBWXfKBsmkv8c%2FCERBYenhMlisDqz8QZNDkQwWF%2BOJFYqcZ56yFLIH%2FjaVMLo%2BtwHKaGBHFFZLNBhDaILd3y3NZ5vdRu4iF%2B8VWplMG3Vo9I%2B2J4fgak%2FjnUH%2BicVhTgG%2FZJnxedQT7Qt%2BxilvwlnXodlbtZB8wjmbcDUK6WlKkFt8nsKsOnLA6BCaFwRFrXnvBz2Dpjc9TFtlrNLcVlZqFwSASg&X-Amz-Signature=87258530372434553a7f46132ef4cf01bd1e93591b34b95e6ca8161484cdadf9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663M3U3CTQ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCuTaddjYVhItW9yi3a%2BJL3k2BPLUrpZRNvhShJ3ELeYAIgZwHYGO7QcpvzG6q4%2FIVqxhef0LBfUJQIux4VCJfN%2B70qiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI%2B0si3Xzgpwla4OQSrcA6rGwtqt2gqCffnQX27rUvtLOIbiyTNwYnoKa3CntOcdRlNTAomkXDSGJhmdOrZnTnwHmyIiSsSFAunAMrRPYWqVmgcUSkOLQGmdfPNNr9OboYIiG60BXadYG04CxP97MXNp%2Br1kRjpvBynIQD9v%2FMuGuyy1Zw7n89tmXFD%2FCydU68bX5OKNP2gQQ3D%2F2oZ8BiCY29b6pXdLS2TULBVVFFlH8XBhCnMRX%2BBtM0sbelLIQWYmMhlEJ%2FUuJ1uY921rbq8DGp3baPEor1PJX5X%2B0Bx%2F3gHey4wlGFxxsd3gcj%2FyZnY80s9%2Fh15HhfLgetLl6dVMhkcL6ntEsCJ8nZuVAV69UaDTe9shZVZW2fDbonYlT7EWBpuYyfb2cGkn0zhbu%2FEQ%2B%2F%2B2INWEQ%2F78QEjDOw%2FK8TBo%2FEb9eEMc3A6mjDEWgheBsyajavxy3Y4%2Fyjveec%2FCAfUe3eLF9pYAWmvUllIpd5IPfNQ%2F19qzNqZjgZlaeE5ennoWXXMZfUrR2eFHPfZPcicCdZMJZfKnBEeumx1NBV46U2%2FTFk2kt%2BjXPiPFjLM5GwOUltcBsJ4%2BMqAbsrZdjc0AnEb0wVWJkXBxwfTk8mD1LNLQYkJHUhZ%2FOOrvLRWkdqsx8Y4SBY57MJnQ8LwGOqUBvBWXfKBsmkv8c%2FCERBYenhMlisDqz8QZNDkQwWF%2BOJFYqcZ56yFLIH%2FjaVMLo%2BtwHKaGBHFFZLNBhDaILd3y3NZ5vdRu4iF%2B8VWplMG3Vo9I%2B2J4fgak%2FjnUH%2BicVhTgG%2FZJnxedQT7Qt%2BxilvwlnXodlbtZB8wjmbcDUK6WlKkFt8nsKsOnLA6BCaFwRFrXnvBz2Dpjc9TFtlrNLcVlZqFwSASg&X-Amz-Signature=2e7bbe42f3836dcd9fb97067f1a640a9ce662e3efab004f290e65c8fdc0d7954&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662JGJCHHJ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEk5Qm1hf2ChAqZmWTRl8yiNaQWCYbyrnowHUMvHBvn5AiAjA78QQ5SH7zMgopLjGC2VGv%2F3rHCrG%2FMG7S8L%2BC8dASqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMfNpSp4wFL0Jpl2J8KtwDaT5JAWXP8JwzwL5ljiAiHslOU5aeFD3SkcViZhIN7vieqiUVOVSXOCwTJSF0hyOXwSZKH8uDT41vq4z3DISh2KkS%2BrrTtSr10HeNYe%2BPalGNRRrI3jCx5gjwS2p9zCnwvXNqVsprJHb0Zbun2RAO3OBFh2sy%2BdR2zuEItWEL1fXktvsVwWTZjaEvD8CY07tCo0i7pfvGV%2FQg3Xp4jVX6tbghv66Q2IlXmfdWP%2BvBEVSsWXmH0%2BLev0dDw4ncZHfZMy2ueG5mjQiEascz7Jmeubk7QmSoV88bw%2BeYB06yzrBhFmuqd25DjCNIunT4my2q%2F8zZPvFX0GiAXnSf1PVcRtdiwT4idVeOnPJQ9nJZ2KPGZOVy7rJTaVQnP6GFo%2BCjMZMQZKbIYQJQ%2FiSEVwGpvdZA0iHQjbFI5wHr%2Bf1Fwp4wXKRmAd4TVJ1WpXJXFF%2BkM0dcG9w%2FImIR4umqGvwANsOx09Rb%2BeCe0zPNUlGHEyg4VbEqjtzp5LlOS%2F7Q7jlm7Z1tz%2FgGYwQ0KM%2BaWNbSPdywpkhbEqndEjSmHKL38qpyj1hmo89qyOlgkQIYA2KCW4Yi21ZlkB%2BhBl2ITezXjgPyrJPcTBi2CsqLjBGzpsBJk1HAz%2Bh4Q3K9yKEw1dDwvAY6pgEpN50KNJWrEX6mPDylwEn6eTb2v4jU3PbEm8hOHEKegwqHyyl68bqEwusS07%2FOaVSIiLNtC9F44n%2FellV21KaoflXhb9P%2FJxitXN8lyACNnQEOdOQVHklWtCIbGuhFp5Zgtp6Th%2BHvrXV%2Bt9IjZd%2FK9xL2oc5lT3oyOLDpwz9bVgo7C5i6ORIeuRW89v9r851TKCWKuIPsG2iGiliTBT5lEjW8715k&X-Amz-Signature=f766da96bdeac462cda880a1d307e5e2d37963babd2c11668c6f78288828974c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662JGJCHHJ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEk5Qm1hf2ChAqZmWTRl8yiNaQWCYbyrnowHUMvHBvn5AiAjA78QQ5SH7zMgopLjGC2VGv%2F3rHCrG%2FMG7S8L%2BC8dASqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMfNpSp4wFL0Jpl2J8KtwDaT5JAWXP8JwzwL5ljiAiHslOU5aeFD3SkcViZhIN7vieqiUVOVSXOCwTJSF0hyOXwSZKH8uDT41vq4z3DISh2KkS%2BrrTtSr10HeNYe%2BPalGNRRrI3jCx5gjwS2p9zCnwvXNqVsprJHb0Zbun2RAO3OBFh2sy%2BdR2zuEItWEL1fXktvsVwWTZjaEvD8CY07tCo0i7pfvGV%2FQg3Xp4jVX6tbghv66Q2IlXmfdWP%2BvBEVSsWXmH0%2BLev0dDw4ncZHfZMy2ueG5mjQiEascz7Jmeubk7QmSoV88bw%2BeYB06yzrBhFmuqd25DjCNIunT4my2q%2F8zZPvFX0GiAXnSf1PVcRtdiwT4idVeOnPJQ9nJZ2KPGZOVy7rJTaVQnP6GFo%2BCjMZMQZKbIYQJQ%2FiSEVwGpvdZA0iHQjbFI5wHr%2Bf1Fwp4wXKRmAd4TVJ1WpXJXFF%2BkM0dcG9w%2FImIR4umqGvwANsOx09Rb%2BeCe0zPNUlGHEyg4VbEqjtzp5LlOS%2F7Q7jlm7Z1tz%2FgGYwQ0KM%2BaWNbSPdywpkhbEqndEjSmHKL38qpyj1hmo89qyOlgkQIYA2KCW4Yi21ZlkB%2BhBl2ITezXjgPyrJPcTBi2CsqLjBGzpsBJk1HAz%2Bh4Q3K9yKEw1dDwvAY6pgEpN50KNJWrEX6mPDylwEn6eTb2v4jU3PbEm8hOHEKegwqHyyl68bqEwusS07%2FOaVSIiLNtC9F44n%2FellV21KaoflXhb9P%2FJxitXN8lyACNnQEOdOQVHklWtCIbGuhFp5Zgtp6Th%2BHvrXV%2Bt9IjZd%2FK9xL2oc5lT3oyOLDpwz9bVgo7C5i6ORIeuRW89v9r851TKCWKuIPsG2iGiliTBT5lEjW8715k&X-Amz-Signature=5a95da2894e24ae7ed48a8508db01dcbdc44a6e5d85bfb454ef7b6e91b81d41a&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
