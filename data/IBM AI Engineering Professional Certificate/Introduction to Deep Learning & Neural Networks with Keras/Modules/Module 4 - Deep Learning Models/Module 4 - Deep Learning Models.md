

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQ2A5OCD%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJHMEUCIFX8Cses3SNM4mIAJZE6gCE1mr3YMcOahyOzmT2fZ5kqAiEA%2FVZKbe%2BUD%2FPAJp50G6ufqpObUvaM3fGQIBwe5VmxHCwq%2FwMIHRAAGgw2Mzc0MjMxODM4MDUiDDeQYpKTDoXGzAa5fyrcA6wtMN7x0oJcmFkZJClr0uF9NJushjCXePxRWI5z6S4qTfoLk6cD3%2Bo4bieTAkCG%2Blv%2BZlG20nU%2FSN5gK3ZwdBoE%2F3WjzMm89TMG1pvhnCrstxhErVi%2FpFP11VJUWRFnng4FuRZOsjdf3%2F28wOAcwsUjQyO0cvck%2BZxlumcB4yhmQdCKqzETiUzHtl0aAQzY68uq51LhsZiQ3u6Oi0eDufhCIcy6vKjUmC68BX4Id46bzVJEj89u4EzZDVkLCCgPodAoer%2B6s5xosbl%2BJO1EH5%2B9l%2BuDN3ca0TJo0Y8A6KNnDHVywC%2FzsQBjsf7BhUZMneUraxJQKYJxP1GxDWpChRz4bKAj7i282TyVj6B6yPXXXq%2BJ4u9ftoeBiAgvZ7qIZ0cztkUYQGoYASPI5ZOHxnQlyrSTtGXaWweoJ1kYsdIM2qclmXJUPvoJmJ6NcKp8c58fD%2BH5Ej%2BausRMHfIKP8oGyxTwctN5%2BwOhyQKlshTOcOw9jMxFvTFxC%2FdRj478xU9TIOFPt8RTBOUyZ38t%2Bw3D6poLAhBegPtEL6FqniygaPYRv4TnY%2F4MtDisE0J3eNDo5k38XyOJf1wq7oMZZaLVm1fHTlI8RodiPuSijmNNYLtnXWWDv4%2BEX8jFMJC9hL0GOqUBiWC7v16%2Bj2mN7iDQGgK%2F7t4h%2BWxkFhdjB2WBHxPmCn%2FTAijwId%2BwCuJtAugoSrl98V68z0DNeqT6vvHthfnCnQWkt%2BMnJ4EehSiTVLw1XIaa8bm0Ip2ezHdcImNbWizL0twNqw%2BGLMGeK7%2FXf4PDwIKkEnW3nqFOokdpYXEHHq4vNjKPcB%2FgipWxXe9OZCZ%2B%2Br1trOPWjVTxCLmntHnpI502GGWS&X-Amz-Signature=0f55b408f3edb106d21a1fdb67712b1c52558722c04b4bf51cd51e636581eba6&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQ2A5OCD%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJHMEUCIFX8Cses3SNM4mIAJZE6gCE1mr3YMcOahyOzmT2fZ5kqAiEA%2FVZKbe%2BUD%2FPAJp50G6ufqpObUvaM3fGQIBwe5VmxHCwq%2FwMIHRAAGgw2Mzc0MjMxODM4MDUiDDeQYpKTDoXGzAa5fyrcA6wtMN7x0oJcmFkZJClr0uF9NJushjCXePxRWI5z6S4qTfoLk6cD3%2Bo4bieTAkCG%2Blv%2BZlG20nU%2FSN5gK3ZwdBoE%2F3WjzMm89TMG1pvhnCrstxhErVi%2FpFP11VJUWRFnng4FuRZOsjdf3%2F28wOAcwsUjQyO0cvck%2BZxlumcB4yhmQdCKqzETiUzHtl0aAQzY68uq51LhsZiQ3u6Oi0eDufhCIcy6vKjUmC68BX4Id46bzVJEj89u4EzZDVkLCCgPodAoer%2B6s5xosbl%2BJO1EH5%2B9l%2BuDN3ca0TJo0Y8A6KNnDHVywC%2FzsQBjsf7BhUZMneUraxJQKYJxP1GxDWpChRz4bKAj7i282TyVj6B6yPXXXq%2BJ4u9ftoeBiAgvZ7qIZ0cztkUYQGoYASPI5ZOHxnQlyrSTtGXaWweoJ1kYsdIM2qclmXJUPvoJmJ6NcKp8c58fD%2BH5Ej%2BausRMHfIKP8oGyxTwctN5%2BwOhyQKlshTOcOw9jMxFvTFxC%2FdRj478xU9TIOFPt8RTBOUyZ38t%2Bw3D6poLAhBegPtEL6FqniygaPYRv4TnY%2F4MtDisE0J3eNDo5k38XyOJf1wq7oMZZaLVm1fHTlI8RodiPuSijmNNYLtnXWWDv4%2BEX8jFMJC9hL0GOqUBiWC7v16%2Bj2mN7iDQGgK%2F7t4h%2BWxkFhdjB2WBHxPmCn%2FTAijwId%2BwCuJtAugoSrl98V68z0DNeqT6vvHthfnCnQWkt%2BMnJ4EehSiTVLw1XIaa8bm0Ip2ezHdcImNbWizL0twNqw%2BGLMGeK7%2FXf4PDwIKkEnW3nqFOokdpYXEHHq4vNjKPcB%2FgipWxXe9OZCZ%2B%2Br1trOPWjVTxCLmntHnpI502GGWS&X-Amz-Signature=983e07e7316aa16f13380e305d8ae017140930c03583ccf1bcbf3405bbc9c029&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQ2A5OCD%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJHMEUCIFX8Cses3SNM4mIAJZE6gCE1mr3YMcOahyOzmT2fZ5kqAiEA%2FVZKbe%2BUD%2FPAJp50G6ufqpObUvaM3fGQIBwe5VmxHCwq%2FwMIHRAAGgw2Mzc0MjMxODM4MDUiDDeQYpKTDoXGzAa5fyrcA6wtMN7x0oJcmFkZJClr0uF9NJushjCXePxRWI5z6S4qTfoLk6cD3%2Bo4bieTAkCG%2Blv%2BZlG20nU%2FSN5gK3ZwdBoE%2F3WjzMm89TMG1pvhnCrstxhErVi%2FpFP11VJUWRFnng4FuRZOsjdf3%2F28wOAcwsUjQyO0cvck%2BZxlumcB4yhmQdCKqzETiUzHtl0aAQzY68uq51LhsZiQ3u6Oi0eDufhCIcy6vKjUmC68BX4Id46bzVJEj89u4EzZDVkLCCgPodAoer%2B6s5xosbl%2BJO1EH5%2B9l%2BuDN3ca0TJo0Y8A6KNnDHVywC%2FzsQBjsf7BhUZMneUraxJQKYJxP1GxDWpChRz4bKAj7i282TyVj6B6yPXXXq%2BJ4u9ftoeBiAgvZ7qIZ0cztkUYQGoYASPI5ZOHxnQlyrSTtGXaWweoJ1kYsdIM2qclmXJUPvoJmJ6NcKp8c58fD%2BH5Ej%2BausRMHfIKP8oGyxTwctN5%2BwOhyQKlshTOcOw9jMxFvTFxC%2FdRj478xU9TIOFPt8RTBOUyZ38t%2Bw3D6poLAhBegPtEL6FqniygaPYRv4TnY%2F4MtDisE0J3eNDo5k38XyOJf1wq7oMZZaLVm1fHTlI8RodiPuSijmNNYLtnXWWDv4%2BEX8jFMJC9hL0GOqUBiWC7v16%2Bj2mN7iDQGgK%2F7t4h%2BWxkFhdjB2WBHxPmCn%2FTAijwId%2BwCuJtAugoSrl98V68z0DNeqT6vvHthfnCnQWkt%2BMnJ4EehSiTVLw1XIaa8bm0Ip2ezHdcImNbWizL0twNqw%2BGLMGeK7%2FXf4PDwIKkEnW3nqFOokdpYXEHHq4vNjKPcB%2FgipWxXe9OZCZ%2B%2Br1trOPWjVTxCLmntHnpI502GGWS&X-Amz-Signature=d35ac55e6b5e5227252b05d7c9fd88319c5268a87d0eb762a44be36f12fb53fd&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQ2A5OCD%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJHMEUCIFX8Cses3SNM4mIAJZE6gCE1mr3YMcOahyOzmT2fZ5kqAiEA%2FVZKbe%2BUD%2FPAJp50G6ufqpObUvaM3fGQIBwe5VmxHCwq%2FwMIHRAAGgw2Mzc0MjMxODM4MDUiDDeQYpKTDoXGzAa5fyrcA6wtMN7x0oJcmFkZJClr0uF9NJushjCXePxRWI5z6S4qTfoLk6cD3%2Bo4bieTAkCG%2Blv%2BZlG20nU%2FSN5gK3ZwdBoE%2F3WjzMm89TMG1pvhnCrstxhErVi%2FpFP11VJUWRFnng4FuRZOsjdf3%2F28wOAcwsUjQyO0cvck%2BZxlumcB4yhmQdCKqzETiUzHtl0aAQzY68uq51LhsZiQ3u6Oi0eDufhCIcy6vKjUmC68BX4Id46bzVJEj89u4EzZDVkLCCgPodAoer%2B6s5xosbl%2BJO1EH5%2B9l%2BuDN3ca0TJo0Y8A6KNnDHVywC%2FzsQBjsf7BhUZMneUraxJQKYJxP1GxDWpChRz4bKAj7i282TyVj6B6yPXXXq%2BJ4u9ftoeBiAgvZ7qIZ0cztkUYQGoYASPI5ZOHxnQlyrSTtGXaWweoJ1kYsdIM2qclmXJUPvoJmJ6NcKp8c58fD%2BH5Ej%2BausRMHfIKP8oGyxTwctN5%2BwOhyQKlshTOcOw9jMxFvTFxC%2FdRj478xU9TIOFPt8RTBOUyZ38t%2Bw3D6poLAhBegPtEL6FqniygaPYRv4TnY%2F4MtDisE0J3eNDo5k38XyOJf1wq7oMZZaLVm1fHTlI8RodiPuSijmNNYLtnXWWDv4%2BEX8jFMJC9hL0GOqUBiWC7v16%2Bj2mN7iDQGgK%2F7t4h%2BWxkFhdjB2WBHxPmCn%2FTAijwId%2BwCuJtAugoSrl98V68z0DNeqT6vvHthfnCnQWkt%2BMnJ4EehSiTVLw1XIaa8bm0Ip2ezHdcImNbWizL0twNqw%2BGLMGeK7%2FXf4PDwIKkEnW3nqFOokdpYXEHHq4vNjKPcB%2FgipWxXe9OZCZ%2B%2Br1trOPWjVTxCLmntHnpI502GGWS&X-Amz-Signature=7598b72e106d1117c6a78b7ee578e71ee037286bebd84b564321fdfa3916f249&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQ2A5OCD%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJHMEUCIFX8Cses3SNM4mIAJZE6gCE1mr3YMcOahyOzmT2fZ5kqAiEA%2FVZKbe%2BUD%2FPAJp50G6ufqpObUvaM3fGQIBwe5VmxHCwq%2FwMIHRAAGgw2Mzc0MjMxODM4MDUiDDeQYpKTDoXGzAa5fyrcA6wtMN7x0oJcmFkZJClr0uF9NJushjCXePxRWI5z6S4qTfoLk6cD3%2Bo4bieTAkCG%2Blv%2BZlG20nU%2FSN5gK3ZwdBoE%2F3WjzMm89TMG1pvhnCrstxhErVi%2FpFP11VJUWRFnng4FuRZOsjdf3%2F28wOAcwsUjQyO0cvck%2BZxlumcB4yhmQdCKqzETiUzHtl0aAQzY68uq51LhsZiQ3u6Oi0eDufhCIcy6vKjUmC68BX4Id46bzVJEj89u4EzZDVkLCCgPodAoer%2B6s5xosbl%2BJO1EH5%2B9l%2BuDN3ca0TJo0Y8A6KNnDHVywC%2FzsQBjsf7BhUZMneUraxJQKYJxP1GxDWpChRz4bKAj7i282TyVj6B6yPXXXq%2BJ4u9ftoeBiAgvZ7qIZ0cztkUYQGoYASPI5ZOHxnQlyrSTtGXaWweoJ1kYsdIM2qclmXJUPvoJmJ6NcKp8c58fD%2BH5Ej%2BausRMHfIKP8oGyxTwctN5%2BwOhyQKlshTOcOw9jMxFvTFxC%2FdRj478xU9TIOFPt8RTBOUyZ38t%2Bw3D6poLAhBegPtEL6FqniygaPYRv4TnY%2F4MtDisE0J3eNDo5k38XyOJf1wq7oMZZaLVm1fHTlI8RodiPuSijmNNYLtnXWWDv4%2BEX8jFMJC9hL0GOqUBiWC7v16%2Bj2mN7iDQGgK%2F7t4h%2BWxkFhdjB2WBHxPmCn%2FTAijwId%2BwCuJtAugoSrl98V68z0DNeqT6vvHthfnCnQWkt%2BMnJ4EehSiTVLw1XIaa8bm0Ip2ezHdcImNbWizL0twNqw%2BGLMGeK7%2FXf4PDwIKkEnW3nqFOokdpYXEHHq4vNjKPcB%2FgipWxXe9OZCZ%2B%2Br1trOPWjVTxCLmntHnpI502GGWS&X-Amz-Signature=be3a2136e9914e2de3d9142ef72606fb4db9147504222b64516e8b5471ec66ea&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQ2A5OCD%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJHMEUCIFX8Cses3SNM4mIAJZE6gCE1mr3YMcOahyOzmT2fZ5kqAiEA%2FVZKbe%2BUD%2FPAJp50G6ufqpObUvaM3fGQIBwe5VmxHCwq%2FwMIHRAAGgw2Mzc0MjMxODM4MDUiDDeQYpKTDoXGzAa5fyrcA6wtMN7x0oJcmFkZJClr0uF9NJushjCXePxRWI5z6S4qTfoLk6cD3%2Bo4bieTAkCG%2Blv%2BZlG20nU%2FSN5gK3ZwdBoE%2F3WjzMm89TMG1pvhnCrstxhErVi%2FpFP11VJUWRFnng4FuRZOsjdf3%2F28wOAcwsUjQyO0cvck%2BZxlumcB4yhmQdCKqzETiUzHtl0aAQzY68uq51LhsZiQ3u6Oi0eDufhCIcy6vKjUmC68BX4Id46bzVJEj89u4EzZDVkLCCgPodAoer%2B6s5xosbl%2BJO1EH5%2B9l%2BuDN3ca0TJo0Y8A6KNnDHVywC%2FzsQBjsf7BhUZMneUraxJQKYJxP1GxDWpChRz4bKAj7i282TyVj6B6yPXXXq%2BJ4u9ftoeBiAgvZ7qIZ0cztkUYQGoYASPI5ZOHxnQlyrSTtGXaWweoJ1kYsdIM2qclmXJUPvoJmJ6NcKp8c58fD%2BH5Ej%2BausRMHfIKP8oGyxTwctN5%2BwOhyQKlshTOcOw9jMxFvTFxC%2FdRj478xU9TIOFPt8RTBOUyZ38t%2Bw3D6poLAhBegPtEL6FqniygaPYRv4TnY%2F4MtDisE0J3eNDo5k38XyOJf1wq7oMZZaLVm1fHTlI8RodiPuSijmNNYLtnXWWDv4%2BEX8jFMJC9hL0GOqUBiWC7v16%2Bj2mN7iDQGgK%2F7t4h%2BWxkFhdjB2WBHxPmCn%2FTAijwId%2BwCuJtAugoSrl98V68z0DNeqT6vvHthfnCnQWkt%2BMnJ4EehSiTVLw1XIaa8bm0Ip2ezHdcImNbWizL0twNqw%2BGLMGeK7%2FXf4PDwIKkEnW3nqFOokdpYXEHHq4vNjKPcB%2FgipWxXe9OZCZ%2B%2Br1trOPWjVTxCLmntHnpI502GGWS&X-Amz-Signature=04e5f77a4ea9ed5c43f69beeb4d6387fe8c589806335d4da2361548bf2730a6a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQ2A5OCD%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJHMEUCIFX8Cses3SNM4mIAJZE6gCE1mr3YMcOahyOzmT2fZ5kqAiEA%2FVZKbe%2BUD%2FPAJp50G6ufqpObUvaM3fGQIBwe5VmxHCwq%2FwMIHRAAGgw2Mzc0MjMxODM4MDUiDDeQYpKTDoXGzAa5fyrcA6wtMN7x0oJcmFkZJClr0uF9NJushjCXePxRWI5z6S4qTfoLk6cD3%2Bo4bieTAkCG%2Blv%2BZlG20nU%2FSN5gK3ZwdBoE%2F3WjzMm89TMG1pvhnCrstxhErVi%2FpFP11VJUWRFnng4FuRZOsjdf3%2F28wOAcwsUjQyO0cvck%2BZxlumcB4yhmQdCKqzETiUzHtl0aAQzY68uq51LhsZiQ3u6Oi0eDufhCIcy6vKjUmC68BX4Id46bzVJEj89u4EzZDVkLCCgPodAoer%2B6s5xosbl%2BJO1EH5%2B9l%2BuDN3ca0TJo0Y8A6KNnDHVywC%2FzsQBjsf7BhUZMneUraxJQKYJxP1GxDWpChRz4bKAj7i282TyVj6B6yPXXXq%2BJ4u9ftoeBiAgvZ7qIZ0cztkUYQGoYASPI5ZOHxnQlyrSTtGXaWweoJ1kYsdIM2qclmXJUPvoJmJ6NcKp8c58fD%2BH5Ej%2BausRMHfIKP8oGyxTwctN5%2BwOhyQKlshTOcOw9jMxFvTFxC%2FdRj478xU9TIOFPt8RTBOUyZ38t%2Bw3D6poLAhBegPtEL6FqniygaPYRv4TnY%2F4MtDisE0J3eNDo5k38XyOJf1wq7oMZZaLVm1fHTlI8RodiPuSijmNNYLtnXWWDv4%2BEX8jFMJC9hL0GOqUBiWC7v16%2Bj2mN7iDQGgK%2F7t4h%2BWxkFhdjB2WBHxPmCn%2FTAijwId%2BwCuJtAugoSrl98V68z0DNeqT6vvHthfnCnQWkt%2BMnJ4EehSiTVLw1XIaa8bm0Ip2ezHdcImNbWizL0twNqw%2BGLMGeK7%2FXf4PDwIKkEnW3nqFOokdpYXEHHq4vNjKPcB%2FgipWxXe9OZCZ%2B%2Br1trOPWjVTxCLmntHnpI502GGWS&X-Amz-Signature=4b24b5cc5e976c27b26e0fff989afad7d4c0643eee6064120665dc6c2afd2be8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQ2A5OCD%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJHMEUCIFX8Cses3SNM4mIAJZE6gCE1mr3YMcOahyOzmT2fZ5kqAiEA%2FVZKbe%2BUD%2FPAJp50G6ufqpObUvaM3fGQIBwe5VmxHCwq%2FwMIHRAAGgw2Mzc0MjMxODM4MDUiDDeQYpKTDoXGzAa5fyrcA6wtMN7x0oJcmFkZJClr0uF9NJushjCXePxRWI5z6S4qTfoLk6cD3%2Bo4bieTAkCG%2Blv%2BZlG20nU%2FSN5gK3ZwdBoE%2F3WjzMm89TMG1pvhnCrstxhErVi%2FpFP11VJUWRFnng4FuRZOsjdf3%2F28wOAcwsUjQyO0cvck%2BZxlumcB4yhmQdCKqzETiUzHtl0aAQzY68uq51LhsZiQ3u6Oi0eDufhCIcy6vKjUmC68BX4Id46bzVJEj89u4EzZDVkLCCgPodAoer%2B6s5xosbl%2BJO1EH5%2B9l%2BuDN3ca0TJo0Y8A6KNnDHVywC%2FzsQBjsf7BhUZMneUraxJQKYJxP1GxDWpChRz4bKAj7i282TyVj6B6yPXXXq%2BJ4u9ftoeBiAgvZ7qIZ0cztkUYQGoYASPI5ZOHxnQlyrSTtGXaWweoJ1kYsdIM2qclmXJUPvoJmJ6NcKp8c58fD%2BH5Ej%2BausRMHfIKP8oGyxTwctN5%2BwOhyQKlshTOcOw9jMxFvTFxC%2FdRj478xU9TIOFPt8RTBOUyZ38t%2Bw3D6poLAhBegPtEL6FqniygaPYRv4TnY%2F4MtDisE0J3eNDo5k38XyOJf1wq7oMZZaLVm1fHTlI8RodiPuSijmNNYLtnXWWDv4%2BEX8jFMJC9hL0GOqUBiWC7v16%2Bj2mN7iDQGgK%2F7t4h%2BWxkFhdjB2WBHxPmCn%2FTAijwId%2BwCuJtAugoSrl98V68z0DNeqT6vvHthfnCnQWkt%2BMnJ4EehSiTVLw1XIaa8bm0Ip2ezHdcImNbWizL0twNqw%2BGLMGeK7%2FXf4PDwIKkEnW3nqFOokdpYXEHHq4vNjKPcB%2FgipWxXe9OZCZ%2B%2Br1trOPWjVTxCLmntHnpI502GGWS&X-Amz-Signature=04d2142b2b9b5a36298a7641a4aa187ec54a783be9cfc07ef9d2dc2d24e67c70&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQ2A5OCD%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJHMEUCIFX8Cses3SNM4mIAJZE6gCE1mr3YMcOahyOzmT2fZ5kqAiEA%2FVZKbe%2BUD%2FPAJp50G6ufqpObUvaM3fGQIBwe5VmxHCwq%2FwMIHRAAGgw2Mzc0MjMxODM4MDUiDDeQYpKTDoXGzAa5fyrcA6wtMN7x0oJcmFkZJClr0uF9NJushjCXePxRWI5z6S4qTfoLk6cD3%2Bo4bieTAkCG%2Blv%2BZlG20nU%2FSN5gK3ZwdBoE%2F3WjzMm89TMG1pvhnCrstxhErVi%2FpFP11VJUWRFnng4FuRZOsjdf3%2F28wOAcwsUjQyO0cvck%2BZxlumcB4yhmQdCKqzETiUzHtl0aAQzY68uq51LhsZiQ3u6Oi0eDufhCIcy6vKjUmC68BX4Id46bzVJEj89u4EzZDVkLCCgPodAoer%2B6s5xosbl%2BJO1EH5%2B9l%2BuDN3ca0TJo0Y8A6KNnDHVywC%2FzsQBjsf7BhUZMneUraxJQKYJxP1GxDWpChRz4bKAj7i282TyVj6B6yPXXXq%2BJ4u9ftoeBiAgvZ7qIZ0cztkUYQGoYASPI5ZOHxnQlyrSTtGXaWweoJ1kYsdIM2qclmXJUPvoJmJ6NcKp8c58fD%2BH5Ej%2BausRMHfIKP8oGyxTwctN5%2BwOhyQKlshTOcOw9jMxFvTFxC%2FdRj478xU9TIOFPt8RTBOUyZ38t%2Bw3D6poLAhBegPtEL6FqniygaPYRv4TnY%2F4MtDisE0J3eNDo5k38XyOJf1wq7oMZZaLVm1fHTlI8RodiPuSijmNNYLtnXWWDv4%2BEX8jFMJC9hL0GOqUBiWC7v16%2Bj2mN7iDQGgK%2F7t4h%2BWxkFhdjB2WBHxPmCn%2FTAijwId%2BwCuJtAugoSrl98V68z0DNeqT6vvHthfnCnQWkt%2BMnJ4EehSiTVLw1XIaa8bm0Ip2ezHdcImNbWizL0twNqw%2BGLMGeK7%2FXf4PDwIKkEnW3nqFOokdpYXEHHq4vNjKPcB%2FgipWxXe9OZCZ%2B%2Br1trOPWjVTxCLmntHnpI502GGWS&X-Amz-Signature=3d454146d874630e5691e516828effc1cf26247182e298a0326a4c33cfd86f69&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667NVLYO3F%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJIMEYCIQCWwCtKdCBySPdvD3opcaplnEZBnnpaiXkojjdE7ZDnCAIhAIlq9v4CfdbRSlw38203oOc4jN%2FeG0EioB7FbT7DJcnZKv8DCB0QABoMNjM3NDIzMTgzODA1IgzqmHIwGST7%2BcliNJcq3ANvgqFTcGtIs3qx7hIdHD9lVvzG4E60c07Bs8ECsTXRAWgHVgMi%2Fg5N%2BcWzGwrmUb0npUJyjRm59KlYYUlrlf6hz0AtMY49MvqP2GJEgvMb4e4FZzJWz7CBrjt77o%2FI8JTadojGWiyyps5Y7p8F1GDzyauWf8soxzmGnRvEDDPGC7ccmW489knUeW5njzBqUyF3H%2BoNRxWKYm6pMXQhbf8%2FkfyPDrlFlgSeBCl7eyJdM9dNNl%2BFr7TtUE03Ci36qMmxSrTVDe9onotMnwdDhvNgh%2BUgAoaA%2B9eAj6MsEFutJ0ThuJVInOZaacT6mPl6t6XGaHsqxvAsf4oePlW%2FpxGdGDdJ%2B0WYPu9kqNapbmMdZnC%2FTJFvEvCkhGWpHiei4CGOgdsB4YSnuW%2FimGwnnVvoVKkZFJ97lTler6wbD1fdyukiKteRcIEAccvWkuVDfdgddO8qDhx88ccegTOQLqgqpvpOIkDZofnL7lnyiDmxCuWFepWt6gLpSvG02h%2By0ul0l7k9eLut6NBdpbHnSyl8kZHuQtun7KBpZ2xYGmtgNTLseo9BpCRxO1KfiTApFxXa%2BJPodfCB57HYtswkd7NDCo5AhGrS%2Fl9I6hVqg5K40ltMT5hP6%2FquADMFtjD1vIS9BjqkAf3zh141t%2BZbPl1mTYjzoIBt2xV0HQQLmcRPevsjWwm68Uc93Q7lTxMVURNOe9ihQDmluoDrsJSyY829X3Yp40Ni149fDRsnNuQm%2BEmGYvINTngpZMQcvID%2BnbcXf3pEL7CeNakaBGBL6cVhBwk9yWKwWyXXOzANTZLVTzYeDI7PQ99fQ7XN6ndj7eugC%2BoiRgTa3qRfJIdqBcv68ccf2EiSMR4F&X-Amz-Signature=a0dc9e68eca3b5aac65338723a87b67787935b66d982eea288afa037c23d9fa9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667NVLYO3F%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJIMEYCIQCWwCtKdCBySPdvD3opcaplnEZBnnpaiXkojjdE7ZDnCAIhAIlq9v4CfdbRSlw38203oOc4jN%2FeG0EioB7FbT7DJcnZKv8DCB0QABoMNjM3NDIzMTgzODA1IgzqmHIwGST7%2BcliNJcq3ANvgqFTcGtIs3qx7hIdHD9lVvzG4E60c07Bs8ECsTXRAWgHVgMi%2Fg5N%2BcWzGwrmUb0npUJyjRm59KlYYUlrlf6hz0AtMY49MvqP2GJEgvMb4e4FZzJWz7CBrjt77o%2FI8JTadojGWiyyps5Y7p8F1GDzyauWf8soxzmGnRvEDDPGC7ccmW489knUeW5njzBqUyF3H%2BoNRxWKYm6pMXQhbf8%2FkfyPDrlFlgSeBCl7eyJdM9dNNl%2BFr7TtUE03Ci36qMmxSrTVDe9onotMnwdDhvNgh%2BUgAoaA%2B9eAj6MsEFutJ0ThuJVInOZaacT6mPl6t6XGaHsqxvAsf4oePlW%2FpxGdGDdJ%2B0WYPu9kqNapbmMdZnC%2FTJFvEvCkhGWpHiei4CGOgdsB4YSnuW%2FimGwnnVvoVKkZFJ97lTler6wbD1fdyukiKteRcIEAccvWkuVDfdgddO8qDhx88ccegTOQLqgqpvpOIkDZofnL7lnyiDmxCuWFepWt6gLpSvG02h%2By0ul0l7k9eLut6NBdpbHnSyl8kZHuQtun7KBpZ2xYGmtgNTLseo9BpCRxO1KfiTApFxXa%2BJPodfCB57HYtswkd7NDCo5AhGrS%2Fl9I6hVqg5K40ltMT5hP6%2FquADMFtjD1vIS9BjqkAf3zh141t%2BZbPl1mTYjzoIBt2xV0HQQLmcRPevsjWwm68Uc93Q7lTxMVURNOe9ihQDmluoDrsJSyY829X3Yp40Ni149fDRsnNuQm%2BEmGYvINTngpZMQcvID%2BnbcXf3pEL7CeNakaBGBL6cVhBwk9yWKwWyXXOzANTZLVTzYeDI7PQ99fQ7XN6ndj7eugC%2BoiRgTa3qRfJIdqBcv68ccf2EiSMR4F&X-Amz-Signature=b107b890600c86be8f746f6611bf0b8d4290d040a897c69e91b0086e72fe233c&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
