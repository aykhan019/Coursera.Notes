

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZJADKFP%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIQCoccD5k6A7mJIL0VATMc3syYUbX1pa8j1PFBzMKuvCgAIgeV6H3j1gbTzRfFPedJjgqjuVfHTO9KCF4cSd1gSM5g4q%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDPS79g7e6bXExJRvJyrcA1LryXe2A32uXiUY39pgsTgWwEg5HimBjZEC2%2F47Op8xP2AFycK6W73NT4B5BodZ3XoVnF%2FigtzqIrCZ%2BTzQsZ8DknKy5BHLAUWZIGGiEoZ%2BDMt9NCJPqFdCC5uYNnYXaFdJ8sOGCdkIQZnfIE7byjpH9K%2BSlYhu8emGNmOsdfLpzE1BLrtLwn1qBtIu4uD%2FKu4BiEVnxSn3c8uUR1MiUSE6GsocDytvGATzQc%2B15mpraxSkSge5glk%2FgmrxhVrrNqSjQArfioz%2FL9cuexSKag%2BRReR22NgLRS1afGsn5AarAVanyCxOoO09WNlKO3oL6wsOejd5OHRwZbmosaw4z2A0WOV8kffwePLJcmSIYJzST51YjPRXFRGeTAcd3eYILy2YAobEglltDGyIX77cntaw0oLr9AxgcYG9KBXAi0bv9I8KZNbgHS6l1qp2i80rNW%2BihPpJG3My%2BYwgatCKtNBh1yssiPos2zvgB9sxq2g%2FU0ukJH5Nefv8fA6vDMN89JJPK2QLMU0s7xUBqYvnuKvekdQhVNAwHuffcirhuZ692HPNr4dZKQY6zhX9sdtPUuuCY2g51vu6NbWiDRSa8awPVgFyfpPDkahX8N1dQibpCxglc%2BfcH%2F1QIFx6MJy4lL0GOqUBjnfTEVfG8Z71kymssG0BJ3rUDp86C3PAlH2Ma1UWIZEbat9sJslxmbawoL55rxHPwDIc09tK%2BZ6hfPZHtxYZjv%2FX9%2Faansm99RF3fO3OiNwOir2ywmW34Jr6t94cHMX3dhjdjLVnOQ7rWxyHtGzRuNcacwoXhi0oCcomU4C32aVKdEloXV8%2BJ0DrX5RRyHWvboTNxcQbIz88EGPrXSS3G807v1Jy&X-Amz-Signature=229f789552cec1c6e3bcdf727c375053ca84d35f79f6fb414e41b28499796729&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZJADKFP%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIQCoccD5k6A7mJIL0VATMc3syYUbX1pa8j1PFBzMKuvCgAIgeV6H3j1gbTzRfFPedJjgqjuVfHTO9KCF4cSd1gSM5g4q%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDPS79g7e6bXExJRvJyrcA1LryXe2A32uXiUY39pgsTgWwEg5HimBjZEC2%2F47Op8xP2AFycK6W73NT4B5BodZ3XoVnF%2FigtzqIrCZ%2BTzQsZ8DknKy5BHLAUWZIGGiEoZ%2BDMt9NCJPqFdCC5uYNnYXaFdJ8sOGCdkIQZnfIE7byjpH9K%2BSlYhu8emGNmOsdfLpzE1BLrtLwn1qBtIu4uD%2FKu4BiEVnxSn3c8uUR1MiUSE6GsocDytvGATzQc%2B15mpraxSkSge5glk%2FgmrxhVrrNqSjQArfioz%2FL9cuexSKag%2BRReR22NgLRS1afGsn5AarAVanyCxOoO09WNlKO3oL6wsOejd5OHRwZbmosaw4z2A0WOV8kffwePLJcmSIYJzST51YjPRXFRGeTAcd3eYILy2YAobEglltDGyIX77cntaw0oLr9AxgcYG9KBXAi0bv9I8KZNbgHS6l1qp2i80rNW%2BihPpJG3My%2BYwgatCKtNBh1yssiPos2zvgB9sxq2g%2FU0ukJH5Nefv8fA6vDMN89JJPK2QLMU0s7xUBqYvnuKvekdQhVNAwHuffcirhuZ692HPNr4dZKQY6zhX9sdtPUuuCY2g51vu6NbWiDRSa8awPVgFyfpPDkahX8N1dQibpCxglc%2BfcH%2F1QIFx6MJy4lL0GOqUBjnfTEVfG8Z71kymssG0BJ3rUDp86C3PAlH2Ma1UWIZEbat9sJslxmbawoL55rxHPwDIc09tK%2BZ6hfPZHtxYZjv%2FX9%2Faansm99RF3fO3OiNwOir2ywmW34Jr6t94cHMX3dhjdjLVnOQ7rWxyHtGzRuNcacwoXhi0oCcomU4C32aVKdEloXV8%2BJ0DrX5RRyHWvboTNxcQbIz88EGPrXSS3G807v1Jy&X-Amz-Signature=c37f42f33afd44d14597997fc8489206b72417d1f2539e0b5218e7fb008ec63b&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZJADKFP%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIQCoccD5k6A7mJIL0VATMc3syYUbX1pa8j1PFBzMKuvCgAIgeV6H3j1gbTzRfFPedJjgqjuVfHTO9KCF4cSd1gSM5g4q%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDPS79g7e6bXExJRvJyrcA1LryXe2A32uXiUY39pgsTgWwEg5HimBjZEC2%2F47Op8xP2AFycK6W73NT4B5BodZ3XoVnF%2FigtzqIrCZ%2BTzQsZ8DknKy5BHLAUWZIGGiEoZ%2BDMt9NCJPqFdCC5uYNnYXaFdJ8sOGCdkIQZnfIE7byjpH9K%2BSlYhu8emGNmOsdfLpzE1BLrtLwn1qBtIu4uD%2FKu4BiEVnxSn3c8uUR1MiUSE6GsocDytvGATzQc%2B15mpraxSkSge5glk%2FgmrxhVrrNqSjQArfioz%2FL9cuexSKag%2BRReR22NgLRS1afGsn5AarAVanyCxOoO09WNlKO3oL6wsOejd5OHRwZbmosaw4z2A0WOV8kffwePLJcmSIYJzST51YjPRXFRGeTAcd3eYILy2YAobEglltDGyIX77cntaw0oLr9AxgcYG9KBXAi0bv9I8KZNbgHS6l1qp2i80rNW%2BihPpJG3My%2BYwgatCKtNBh1yssiPos2zvgB9sxq2g%2FU0ukJH5Nefv8fA6vDMN89JJPK2QLMU0s7xUBqYvnuKvekdQhVNAwHuffcirhuZ692HPNr4dZKQY6zhX9sdtPUuuCY2g51vu6NbWiDRSa8awPVgFyfpPDkahX8N1dQibpCxglc%2BfcH%2F1QIFx6MJy4lL0GOqUBjnfTEVfG8Z71kymssG0BJ3rUDp86C3PAlH2Ma1UWIZEbat9sJslxmbawoL55rxHPwDIc09tK%2BZ6hfPZHtxYZjv%2FX9%2Faansm99RF3fO3OiNwOir2ywmW34Jr6t94cHMX3dhjdjLVnOQ7rWxyHtGzRuNcacwoXhi0oCcomU4C32aVKdEloXV8%2BJ0DrX5RRyHWvboTNxcQbIz88EGPrXSS3G807v1Jy&X-Amz-Signature=672ba550450a8c155d82a7a68d4166aaee43efa4f54e0c6c04bfd6e77704a953&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZJADKFP%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIQCoccD5k6A7mJIL0VATMc3syYUbX1pa8j1PFBzMKuvCgAIgeV6H3j1gbTzRfFPedJjgqjuVfHTO9KCF4cSd1gSM5g4q%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDPS79g7e6bXExJRvJyrcA1LryXe2A32uXiUY39pgsTgWwEg5HimBjZEC2%2F47Op8xP2AFycK6W73NT4B5BodZ3XoVnF%2FigtzqIrCZ%2BTzQsZ8DknKy5BHLAUWZIGGiEoZ%2BDMt9NCJPqFdCC5uYNnYXaFdJ8sOGCdkIQZnfIE7byjpH9K%2BSlYhu8emGNmOsdfLpzE1BLrtLwn1qBtIu4uD%2FKu4BiEVnxSn3c8uUR1MiUSE6GsocDytvGATzQc%2B15mpraxSkSge5glk%2FgmrxhVrrNqSjQArfioz%2FL9cuexSKag%2BRReR22NgLRS1afGsn5AarAVanyCxOoO09WNlKO3oL6wsOejd5OHRwZbmosaw4z2A0WOV8kffwePLJcmSIYJzST51YjPRXFRGeTAcd3eYILy2YAobEglltDGyIX77cntaw0oLr9AxgcYG9KBXAi0bv9I8KZNbgHS6l1qp2i80rNW%2BihPpJG3My%2BYwgatCKtNBh1yssiPos2zvgB9sxq2g%2FU0ukJH5Nefv8fA6vDMN89JJPK2QLMU0s7xUBqYvnuKvekdQhVNAwHuffcirhuZ692HPNr4dZKQY6zhX9sdtPUuuCY2g51vu6NbWiDRSa8awPVgFyfpPDkahX8N1dQibpCxglc%2BfcH%2F1QIFx6MJy4lL0GOqUBjnfTEVfG8Z71kymssG0BJ3rUDp86C3PAlH2Ma1UWIZEbat9sJslxmbawoL55rxHPwDIc09tK%2BZ6hfPZHtxYZjv%2FX9%2Faansm99RF3fO3OiNwOir2ywmW34Jr6t94cHMX3dhjdjLVnOQ7rWxyHtGzRuNcacwoXhi0oCcomU4C32aVKdEloXV8%2BJ0DrX5RRyHWvboTNxcQbIz88EGPrXSS3G807v1Jy&X-Amz-Signature=7fee62516125d9d2f7733174f67ae36f4ede51361317c43111c8976800f043fe&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZJADKFP%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIQCoccD5k6A7mJIL0VATMc3syYUbX1pa8j1PFBzMKuvCgAIgeV6H3j1gbTzRfFPedJjgqjuVfHTO9KCF4cSd1gSM5g4q%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDPS79g7e6bXExJRvJyrcA1LryXe2A32uXiUY39pgsTgWwEg5HimBjZEC2%2F47Op8xP2AFycK6W73NT4B5BodZ3XoVnF%2FigtzqIrCZ%2BTzQsZ8DknKy5BHLAUWZIGGiEoZ%2BDMt9NCJPqFdCC5uYNnYXaFdJ8sOGCdkIQZnfIE7byjpH9K%2BSlYhu8emGNmOsdfLpzE1BLrtLwn1qBtIu4uD%2FKu4BiEVnxSn3c8uUR1MiUSE6GsocDytvGATzQc%2B15mpraxSkSge5glk%2FgmrxhVrrNqSjQArfioz%2FL9cuexSKag%2BRReR22NgLRS1afGsn5AarAVanyCxOoO09WNlKO3oL6wsOejd5OHRwZbmosaw4z2A0WOV8kffwePLJcmSIYJzST51YjPRXFRGeTAcd3eYILy2YAobEglltDGyIX77cntaw0oLr9AxgcYG9KBXAi0bv9I8KZNbgHS6l1qp2i80rNW%2BihPpJG3My%2BYwgatCKtNBh1yssiPos2zvgB9sxq2g%2FU0ukJH5Nefv8fA6vDMN89JJPK2QLMU0s7xUBqYvnuKvekdQhVNAwHuffcirhuZ692HPNr4dZKQY6zhX9sdtPUuuCY2g51vu6NbWiDRSa8awPVgFyfpPDkahX8N1dQibpCxglc%2BfcH%2F1QIFx6MJy4lL0GOqUBjnfTEVfG8Z71kymssG0BJ3rUDp86C3PAlH2Ma1UWIZEbat9sJslxmbawoL55rxHPwDIc09tK%2BZ6hfPZHtxYZjv%2FX9%2Faansm99RF3fO3OiNwOir2ywmW34Jr6t94cHMX3dhjdjLVnOQ7rWxyHtGzRuNcacwoXhi0oCcomU4C32aVKdEloXV8%2BJ0DrX5RRyHWvboTNxcQbIz88EGPrXSS3G807v1Jy&X-Amz-Signature=560ac55c9ac01973099e329fc5e3cddba75586e1c118162dec4ad69c730c4b82&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZJADKFP%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIQCoccD5k6A7mJIL0VATMc3syYUbX1pa8j1PFBzMKuvCgAIgeV6H3j1gbTzRfFPedJjgqjuVfHTO9KCF4cSd1gSM5g4q%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDPS79g7e6bXExJRvJyrcA1LryXe2A32uXiUY39pgsTgWwEg5HimBjZEC2%2F47Op8xP2AFycK6W73NT4B5BodZ3XoVnF%2FigtzqIrCZ%2BTzQsZ8DknKy5BHLAUWZIGGiEoZ%2BDMt9NCJPqFdCC5uYNnYXaFdJ8sOGCdkIQZnfIE7byjpH9K%2BSlYhu8emGNmOsdfLpzE1BLrtLwn1qBtIu4uD%2FKu4BiEVnxSn3c8uUR1MiUSE6GsocDytvGATzQc%2B15mpraxSkSge5glk%2FgmrxhVrrNqSjQArfioz%2FL9cuexSKag%2BRReR22NgLRS1afGsn5AarAVanyCxOoO09WNlKO3oL6wsOejd5OHRwZbmosaw4z2A0WOV8kffwePLJcmSIYJzST51YjPRXFRGeTAcd3eYILy2YAobEglltDGyIX77cntaw0oLr9AxgcYG9KBXAi0bv9I8KZNbgHS6l1qp2i80rNW%2BihPpJG3My%2BYwgatCKtNBh1yssiPos2zvgB9sxq2g%2FU0ukJH5Nefv8fA6vDMN89JJPK2QLMU0s7xUBqYvnuKvekdQhVNAwHuffcirhuZ692HPNr4dZKQY6zhX9sdtPUuuCY2g51vu6NbWiDRSa8awPVgFyfpPDkahX8N1dQibpCxglc%2BfcH%2F1QIFx6MJy4lL0GOqUBjnfTEVfG8Z71kymssG0BJ3rUDp86C3PAlH2Ma1UWIZEbat9sJslxmbawoL55rxHPwDIc09tK%2BZ6hfPZHtxYZjv%2FX9%2Faansm99RF3fO3OiNwOir2ywmW34Jr6t94cHMX3dhjdjLVnOQ7rWxyHtGzRuNcacwoXhi0oCcomU4C32aVKdEloXV8%2BJ0DrX5RRyHWvboTNxcQbIz88EGPrXSS3G807v1Jy&X-Amz-Signature=48dfcb87d6b5a25e06a5bcef027bba918c3e5e827622cfc896fd6da2333d5834&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZJADKFP%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIQCoccD5k6A7mJIL0VATMc3syYUbX1pa8j1PFBzMKuvCgAIgeV6H3j1gbTzRfFPedJjgqjuVfHTO9KCF4cSd1gSM5g4q%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDPS79g7e6bXExJRvJyrcA1LryXe2A32uXiUY39pgsTgWwEg5HimBjZEC2%2F47Op8xP2AFycK6W73NT4B5BodZ3XoVnF%2FigtzqIrCZ%2BTzQsZ8DknKy5BHLAUWZIGGiEoZ%2BDMt9NCJPqFdCC5uYNnYXaFdJ8sOGCdkIQZnfIE7byjpH9K%2BSlYhu8emGNmOsdfLpzE1BLrtLwn1qBtIu4uD%2FKu4BiEVnxSn3c8uUR1MiUSE6GsocDytvGATzQc%2B15mpraxSkSge5glk%2FgmrxhVrrNqSjQArfioz%2FL9cuexSKag%2BRReR22NgLRS1afGsn5AarAVanyCxOoO09WNlKO3oL6wsOejd5OHRwZbmosaw4z2A0WOV8kffwePLJcmSIYJzST51YjPRXFRGeTAcd3eYILy2YAobEglltDGyIX77cntaw0oLr9AxgcYG9KBXAi0bv9I8KZNbgHS6l1qp2i80rNW%2BihPpJG3My%2BYwgatCKtNBh1yssiPos2zvgB9sxq2g%2FU0ukJH5Nefv8fA6vDMN89JJPK2QLMU0s7xUBqYvnuKvekdQhVNAwHuffcirhuZ692HPNr4dZKQY6zhX9sdtPUuuCY2g51vu6NbWiDRSa8awPVgFyfpPDkahX8N1dQibpCxglc%2BfcH%2F1QIFx6MJy4lL0GOqUBjnfTEVfG8Z71kymssG0BJ3rUDp86C3PAlH2Ma1UWIZEbat9sJslxmbawoL55rxHPwDIc09tK%2BZ6hfPZHtxYZjv%2FX9%2Faansm99RF3fO3OiNwOir2ywmW34Jr6t94cHMX3dhjdjLVnOQ7rWxyHtGzRuNcacwoXhi0oCcomU4C32aVKdEloXV8%2BJ0DrX5RRyHWvboTNxcQbIz88EGPrXSS3G807v1Jy&X-Amz-Signature=ebade6b7ddd12b5e01bc0acb08f0eb0409fd6c125538523deaacf370b96dea8d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZJADKFP%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIQCoccD5k6A7mJIL0VATMc3syYUbX1pa8j1PFBzMKuvCgAIgeV6H3j1gbTzRfFPedJjgqjuVfHTO9KCF4cSd1gSM5g4q%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDPS79g7e6bXExJRvJyrcA1LryXe2A32uXiUY39pgsTgWwEg5HimBjZEC2%2F47Op8xP2AFycK6W73NT4B5BodZ3XoVnF%2FigtzqIrCZ%2BTzQsZ8DknKy5BHLAUWZIGGiEoZ%2BDMt9NCJPqFdCC5uYNnYXaFdJ8sOGCdkIQZnfIE7byjpH9K%2BSlYhu8emGNmOsdfLpzE1BLrtLwn1qBtIu4uD%2FKu4BiEVnxSn3c8uUR1MiUSE6GsocDytvGATzQc%2B15mpraxSkSge5glk%2FgmrxhVrrNqSjQArfioz%2FL9cuexSKag%2BRReR22NgLRS1afGsn5AarAVanyCxOoO09WNlKO3oL6wsOejd5OHRwZbmosaw4z2A0WOV8kffwePLJcmSIYJzST51YjPRXFRGeTAcd3eYILy2YAobEglltDGyIX77cntaw0oLr9AxgcYG9KBXAi0bv9I8KZNbgHS6l1qp2i80rNW%2BihPpJG3My%2BYwgatCKtNBh1yssiPos2zvgB9sxq2g%2FU0ukJH5Nefv8fA6vDMN89JJPK2QLMU0s7xUBqYvnuKvekdQhVNAwHuffcirhuZ692HPNr4dZKQY6zhX9sdtPUuuCY2g51vu6NbWiDRSa8awPVgFyfpPDkahX8N1dQibpCxglc%2BfcH%2F1QIFx6MJy4lL0GOqUBjnfTEVfG8Z71kymssG0BJ3rUDp86C3PAlH2Ma1UWIZEbat9sJslxmbawoL55rxHPwDIc09tK%2BZ6hfPZHtxYZjv%2FX9%2Faansm99RF3fO3OiNwOir2ywmW34Jr6t94cHMX3dhjdjLVnOQ7rWxyHtGzRuNcacwoXhi0oCcomU4C32aVKdEloXV8%2BJ0DrX5RRyHWvboTNxcQbIz88EGPrXSS3G807v1Jy&X-Amz-Signature=b371e8b689aed7cdfa7380aac9e3edce12ebafaa0b39d79f63b53fd20a5c84e0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZJADKFP%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIQCoccD5k6A7mJIL0VATMc3syYUbX1pa8j1PFBzMKuvCgAIgeV6H3j1gbTzRfFPedJjgqjuVfHTO9KCF4cSd1gSM5g4q%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDPS79g7e6bXExJRvJyrcA1LryXe2A32uXiUY39pgsTgWwEg5HimBjZEC2%2F47Op8xP2AFycK6W73NT4B5BodZ3XoVnF%2FigtzqIrCZ%2BTzQsZ8DknKy5BHLAUWZIGGiEoZ%2BDMt9NCJPqFdCC5uYNnYXaFdJ8sOGCdkIQZnfIE7byjpH9K%2BSlYhu8emGNmOsdfLpzE1BLrtLwn1qBtIu4uD%2FKu4BiEVnxSn3c8uUR1MiUSE6GsocDytvGATzQc%2B15mpraxSkSge5glk%2FgmrxhVrrNqSjQArfioz%2FL9cuexSKag%2BRReR22NgLRS1afGsn5AarAVanyCxOoO09WNlKO3oL6wsOejd5OHRwZbmosaw4z2A0WOV8kffwePLJcmSIYJzST51YjPRXFRGeTAcd3eYILy2YAobEglltDGyIX77cntaw0oLr9AxgcYG9KBXAi0bv9I8KZNbgHS6l1qp2i80rNW%2BihPpJG3My%2BYwgatCKtNBh1yssiPos2zvgB9sxq2g%2FU0ukJH5Nefv8fA6vDMN89JJPK2QLMU0s7xUBqYvnuKvekdQhVNAwHuffcirhuZ692HPNr4dZKQY6zhX9sdtPUuuCY2g51vu6NbWiDRSa8awPVgFyfpPDkahX8N1dQibpCxglc%2BfcH%2F1QIFx6MJy4lL0GOqUBjnfTEVfG8Z71kymssG0BJ3rUDp86C3PAlH2Ma1UWIZEbat9sJslxmbawoL55rxHPwDIc09tK%2BZ6hfPZHtxYZjv%2FX9%2Faansm99RF3fO3OiNwOir2ywmW34Jr6t94cHMX3dhjdjLVnOQ7rWxyHtGzRuNcacwoXhi0oCcomU4C32aVKdEloXV8%2BJ0DrX5RRyHWvboTNxcQbIz88EGPrXSS3G807v1Jy&X-Amz-Signature=4920c2edda1e20e3e5e9eaa3049a62ea2bfe2b40b77f2d1f1e27efcaace91a0c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662SBI45UP%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221412Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJGMEQCIFL3p7HIZr8%2Bgm2TQLZ4w%2FhOHRDlaBgviV%2FXSjPfSZw2AiBC%2FXHipJl4nuC641irVfI0TtGjPi1buwtgFqEVWhtyCir%2FAwhmEAAaDDYzNzQyMzE4MzgwNSIMCSDELOp1seyjI80rKtwDAh%2BCgqv4CQOTVmBMNVSwOgodV1FFWor7tdMHrZ4%2FBwMI7k7SfdW8yV0uCYhWPTtcif2U9MXYsDsporSWMAgSx%2FdHJ4%2FJCHozYSf%2Ber0wN38RdtrP650v8auFeHgOQHjMXCDdQG6HAw%2FFZaEX3yQnyAxdZqQ12mRf3ghPMOiXnJGBUcJ3qZyOjt1DORskllpOtJc9za1n%2Bo3CdNHu3fQI14l2eYMjy7XFs6L2jZnyFsZEvLG0Zc7z89wAlHzyRtGoUFSJs8ijuVuAcNlQ8ugf7kfe87Tn3nFT0McdmXji5y%2B%2F8LWJcqINITCg658nveDULuMcW09NWZ%2FrDvYjijvVKnAm40oAuLh70ESlZ1w1Br6diIgk%2BwnCDGuLi0u15otFoNzbZFuRdiDJZ%2FzPg2yUq9MhP3rd4eDqeuaL4%2Bvxebywv7mEKjj6c1xc4ogNY%2BT%2FZe8aHEGV0eApvXFe%2BlbYJxvIASvuvrIxJZ3CdHIk%2BMesjbqgqXLeBOp%2Ff69fCRv56RE9gItskJ6gDND6%2Fzhl25gI9ilaqXUkGLVbzr8Jx3RbC0vZvBmJN5NgPNwmVzvtucXTmQ4IUIZkDrHIoo8FmJO4g8S8isvpuHRipw8B%2FzDM0Bhyu%2BoeznYMbFsw%2BreUvQY6pgEr1JFhJYdevbcv3tlCNBh%2BBbB6DYQK7lQFmSkX4HgAzf8HCvzZeQTN%2Bf9QPQRWq7xQmfKBejmfDSkiOTr1i1vk8pIFllhc%2BOy382ngx7Eb0hi2v47J7GiO2QBwRzT%2F9upfkVYZ5FIn%2BQROnVBh%2BOxdu18I0STkXxHYzZzPwsDslMi8hYrRt2F16RKGD6tJpRokuxd4OzLxy06gCY9CkeUHXFwZI7Lq&X-Amz-Signature=e387d3ddf9aca1e8a9c64c5e2ea687ad1e380e966478a20ba76e7a6c0df6f99b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662SBI45UP%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221412Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJGMEQCIFL3p7HIZr8%2Bgm2TQLZ4w%2FhOHRDlaBgviV%2FXSjPfSZw2AiBC%2FXHipJl4nuC641irVfI0TtGjPi1buwtgFqEVWhtyCir%2FAwhmEAAaDDYzNzQyMzE4MzgwNSIMCSDELOp1seyjI80rKtwDAh%2BCgqv4CQOTVmBMNVSwOgodV1FFWor7tdMHrZ4%2FBwMI7k7SfdW8yV0uCYhWPTtcif2U9MXYsDsporSWMAgSx%2FdHJ4%2FJCHozYSf%2Ber0wN38RdtrP650v8auFeHgOQHjMXCDdQG6HAw%2FFZaEX3yQnyAxdZqQ12mRf3ghPMOiXnJGBUcJ3qZyOjt1DORskllpOtJc9za1n%2Bo3CdNHu3fQI14l2eYMjy7XFs6L2jZnyFsZEvLG0Zc7z89wAlHzyRtGoUFSJs8ijuVuAcNlQ8ugf7kfe87Tn3nFT0McdmXji5y%2B%2F8LWJcqINITCg658nveDULuMcW09NWZ%2FrDvYjijvVKnAm40oAuLh70ESlZ1w1Br6diIgk%2BwnCDGuLi0u15otFoNzbZFuRdiDJZ%2FzPg2yUq9MhP3rd4eDqeuaL4%2Bvxebywv7mEKjj6c1xc4ogNY%2BT%2FZe8aHEGV0eApvXFe%2BlbYJxvIASvuvrIxJZ3CdHIk%2BMesjbqgqXLeBOp%2Ff69fCRv56RE9gItskJ6gDND6%2Fzhl25gI9ilaqXUkGLVbzr8Jx3RbC0vZvBmJN5NgPNwmVzvtucXTmQ4IUIZkDrHIoo8FmJO4g8S8isvpuHRipw8B%2FzDM0Bhyu%2BoeznYMbFsw%2BreUvQY6pgEr1JFhJYdevbcv3tlCNBh%2BBbB6DYQK7lQFmSkX4HgAzf8HCvzZeQTN%2Bf9QPQRWq7xQmfKBejmfDSkiOTr1i1vk8pIFllhc%2BOy382ngx7Eb0hi2v47J7GiO2QBwRzT%2F9upfkVYZ5FIn%2BQROnVBh%2BOxdu18I0STkXxHYzZzPwsDslMi8hYrRt2F16RKGD6tJpRokuxd4OzLxy06gCY9CkeUHXFwZI7Lq&X-Amz-Signature=19ceb2fc965ff98b8667196c1c653de5b9dacedf836c6fbf58e0d23aec52232d&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
