

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662SWNRNQ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCTvQr0MU0idLFPJjaATGfyDQpfR2zV3VQVFw%2FtLUU%2BEgIhAOoUeh3q%2BTQvwTWoMpXabfJsQyLZ%2BskpILOSKUwRVpPQKogECMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxcEQm4MIerBYtOsrcq3AOhgB9FiVS9fC%2BGloGsB9mD6xi90a32C5JvmP2%2FkfEDSBf84NyF1OfB2gs5VO43gT3eCy5y4%2B%2FhuDEQD5vxGSlnU9VseKs5vzrDRGgPQ%2FMdrQGUxMvUZTXqnAyMVU72tcAGEvMmDet%2FrX81ZkaTBvthVPOd2Oftfwgcea5eKksxsRwuVjHFm637tDjbVVo%2BUEGSWdxtfUZBVYCovhTGoKMGhDbcYkWv9ZyQ%2FT6CVmN%2B6IH1XUsv7DCOKWps4xOy%2BHilOo16wT%2FCTbdZ4pjqiQnyKn1F2W0KVgkP1gl0Il4SybYEL1aPRYiR0E0aOFsKGmY3ql%2BrHV6k2OtoManm53jcBG2374A3kdFsDpYFL8EzJ9LO1lioJnrZexA%2F7iWbPBCInslw7PE0ZYeQBl4kiRyulmTX2TdkFw6t01kkwXdjemI%2BL3sGpD%2FfHvXQckwaQ96XawOtJVf6EKVfuXwjUeiEKuGBWQpJBUUJb%2F4V4OzMbv9ja5oRzvCk%2BeWXpKG5lIc6dUYcnpnRBstn5QFNSS22I4pA3c9EJEho8ak5sF0EScfg3K%2Fv%2Box73QblZx2h%2BlL1ZqHVO5WPICOeTwsadLZXhSzoO7ghLOP15g%2BhHDuP9kBd8eaxqJIJ0mAhvDCd2%2FS8BjqkAbSaZOMc%2B0%2Be%2BHm32eCFFMndLrBEhFQtgn4ta4Ri%2BC%2BGRKlU9Xz75DgAOfHpTJ9ueVvTbsL95wg9z7Rn8Zh7p%2Bu4fnKaCmLTQqg9udsdOHANWxCF4ms88yp3YZbMpmJ994q5JCsmEMh8DsDZkHrTtCCiOyKK2HzSuKk5QBXI311uF0xVj2z7cLea6g%2FzXm1G%2BDYv3I1%2Bdn5IXeXfPJ%2FpzDIbZ4oI&X-Amz-Signature=d24c7521445625215f290cb1e93b4b77eff3155ff72a31deaf8b59103c2d2aed&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662SWNRNQ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCTvQr0MU0idLFPJjaATGfyDQpfR2zV3VQVFw%2FtLUU%2BEgIhAOoUeh3q%2BTQvwTWoMpXabfJsQyLZ%2BskpILOSKUwRVpPQKogECMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxcEQm4MIerBYtOsrcq3AOhgB9FiVS9fC%2BGloGsB9mD6xi90a32C5JvmP2%2FkfEDSBf84NyF1OfB2gs5VO43gT3eCy5y4%2B%2FhuDEQD5vxGSlnU9VseKs5vzrDRGgPQ%2FMdrQGUxMvUZTXqnAyMVU72tcAGEvMmDet%2FrX81ZkaTBvthVPOd2Oftfwgcea5eKksxsRwuVjHFm637tDjbVVo%2BUEGSWdxtfUZBVYCovhTGoKMGhDbcYkWv9ZyQ%2FT6CVmN%2B6IH1XUsv7DCOKWps4xOy%2BHilOo16wT%2FCTbdZ4pjqiQnyKn1F2W0KVgkP1gl0Il4SybYEL1aPRYiR0E0aOFsKGmY3ql%2BrHV6k2OtoManm53jcBG2374A3kdFsDpYFL8EzJ9LO1lioJnrZexA%2F7iWbPBCInslw7PE0ZYeQBl4kiRyulmTX2TdkFw6t01kkwXdjemI%2BL3sGpD%2FfHvXQckwaQ96XawOtJVf6EKVfuXwjUeiEKuGBWQpJBUUJb%2F4V4OzMbv9ja5oRzvCk%2BeWXpKG5lIc6dUYcnpnRBstn5QFNSS22I4pA3c9EJEho8ak5sF0EScfg3K%2Fv%2Box73QblZx2h%2BlL1ZqHVO5WPICOeTwsadLZXhSzoO7ghLOP15g%2BhHDuP9kBd8eaxqJIJ0mAhvDCd2%2FS8BjqkAbSaZOMc%2B0%2Be%2BHm32eCFFMndLrBEhFQtgn4ta4Ri%2BC%2BGRKlU9Xz75DgAOfHpTJ9ueVvTbsL95wg9z7Rn8Zh7p%2Bu4fnKaCmLTQqg9udsdOHANWxCF4ms88yp3YZbMpmJ994q5JCsmEMh8DsDZkHrTtCCiOyKK2HzSuKk5QBXI311uF0xVj2z7cLea6g%2FzXm1G%2BDYv3I1%2Bdn5IXeXfPJ%2FpzDIbZ4oI&X-Amz-Signature=254937755c31d28c7531816669c06f67b61a0e3bb8adac0abed8107ec497f516&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662SWNRNQ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCTvQr0MU0idLFPJjaATGfyDQpfR2zV3VQVFw%2FtLUU%2BEgIhAOoUeh3q%2BTQvwTWoMpXabfJsQyLZ%2BskpILOSKUwRVpPQKogECMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxcEQm4MIerBYtOsrcq3AOhgB9FiVS9fC%2BGloGsB9mD6xi90a32C5JvmP2%2FkfEDSBf84NyF1OfB2gs5VO43gT3eCy5y4%2B%2FhuDEQD5vxGSlnU9VseKs5vzrDRGgPQ%2FMdrQGUxMvUZTXqnAyMVU72tcAGEvMmDet%2FrX81ZkaTBvthVPOd2Oftfwgcea5eKksxsRwuVjHFm637tDjbVVo%2BUEGSWdxtfUZBVYCovhTGoKMGhDbcYkWv9ZyQ%2FT6CVmN%2B6IH1XUsv7DCOKWps4xOy%2BHilOo16wT%2FCTbdZ4pjqiQnyKn1F2W0KVgkP1gl0Il4SybYEL1aPRYiR0E0aOFsKGmY3ql%2BrHV6k2OtoManm53jcBG2374A3kdFsDpYFL8EzJ9LO1lioJnrZexA%2F7iWbPBCInslw7PE0ZYeQBl4kiRyulmTX2TdkFw6t01kkwXdjemI%2BL3sGpD%2FfHvXQckwaQ96XawOtJVf6EKVfuXwjUeiEKuGBWQpJBUUJb%2F4V4OzMbv9ja5oRzvCk%2BeWXpKG5lIc6dUYcnpnRBstn5QFNSS22I4pA3c9EJEho8ak5sF0EScfg3K%2Fv%2Box73QblZx2h%2BlL1ZqHVO5WPICOeTwsadLZXhSzoO7ghLOP15g%2BhHDuP9kBd8eaxqJIJ0mAhvDCd2%2FS8BjqkAbSaZOMc%2B0%2Be%2BHm32eCFFMndLrBEhFQtgn4ta4Ri%2BC%2BGRKlU9Xz75DgAOfHpTJ9ueVvTbsL95wg9z7Rn8Zh7p%2Bu4fnKaCmLTQqg9udsdOHANWxCF4ms88yp3YZbMpmJ994q5JCsmEMh8DsDZkHrTtCCiOyKK2HzSuKk5QBXI311uF0xVj2z7cLea6g%2FzXm1G%2BDYv3I1%2Bdn5IXeXfPJ%2FpzDIbZ4oI&X-Amz-Signature=a9742bed9cd6c0a21c19661d32a218d057140317bc33b304a3cc215e2349d1ab&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662SWNRNQ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCTvQr0MU0idLFPJjaATGfyDQpfR2zV3VQVFw%2FtLUU%2BEgIhAOoUeh3q%2BTQvwTWoMpXabfJsQyLZ%2BskpILOSKUwRVpPQKogECMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxcEQm4MIerBYtOsrcq3AOhgB9FiVS9fC%2BGloGsB9mD6xi90a32C5JvmP2%2FkfEDSBf84NyF1OfB2gs5VO43gT3eCy5y4%2B%2FhuDEQD5vxGSlnU9VseKs5vzrDRGgPQ%2FMdrQGUxMvUZTXqnAyMVU72tcAGEvMmDet%2FrX81ZkaTBvthVPOd2Oftfwgcea5eKksxsRwuVjHFm637tDjbVVo%2BUEGSWdxtfUZBVYCovhTGoKMGhDbcYkWv9ZyQ%2FT6CVmN%2B6IH1XUsv7DCOKWps4xOy%2BHilOo16wT%2FCTbdZ4pjqiQnyKn1F2W0KVgkP1gl0Il4SybYEL1aPRYiR0E0aOFsKGmY3ql%2BrHV6k2OtoManm53jcBG2374A3kdFsDpYFL8EzJ9LO1lioJnrZexA%2F7iWbPBCInslw7PE0ZYeQBl4kiRyulmTX2TdkFw6t01kkwXdjemI%2BL3sGpD%2FfHvXQckwaQ96XawOtJVf6EKVfuXwjUeiEKuGBWQpJBUUJb%2F4V4OzMbv9ja5oRzvCk%2BeWXpKG5lIc6dUYcnpnRBstn5QFNSS22I4pA3c9EJEho8ak5sF0EScfg3K%2Fv%2Box73QblZx2h%2BlL1ZqHVO5WPICOeTwsadLZXhSzoO7ghLOP15g%2BhHDuP9kBd8eaxqJIJ0mAhvDCd2%2FS8BjqkAbSaZOMc%2B0%2Be%2BHm32eCFFMndLrBEhFQtgn4ta4Ri%2BC%2BGRKlU9Xz75DgAOfHpTJ9ueVvTbsL95wg9z7Rn8Zh7p%2Bu4fnKaCmLTQqg9udsdOHANWxCF4ms88yp3YZbMpmJ994q5JCsmEMh8DsDZkHrTtCCiOyKK2HzSuKk5QBXI311uF0xVj2z7cLea6g%2FzXm1G%2BDYv3I1%2Bdn5IXeXfPJ%2FpzDIbZ4oI&X-Amz-Signature=7d43f7aed905de9a63f038c59b9e0c6fe133ea790f8637b5aab71b0b096f2f4d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662SWNRNQ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCTvQr0MU0idLFPJjaATGfyDQpfR2zV3VQVFw%2FtLUU%2BEgIhAOoUeh3q%2BTQvwTWoMpXabfJsQyLZ%2BskpILOSKUwRVpPQKogECMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxcEQm4MIerBYtOsrcq3AOhgB9FiVS9fC%2BGloGsB9mD6xi90a32C5JvmP2%2FkfEDSBf84NyF1OfB2gs5VO43gT3eCy5y4%2B%2FhuDEQD5vxGSlnU9VseKs5vzrDRGgPQ%2FMdrQGUxMvUZTXqnAyMVU72tcAGEvMmDet%2FrX81ZkaTBvthVPOd2Oftfwgcea5eKksxsRwuVjHFm637tDjbVVo%2BUEGSWdxtfUZBVYCovhTGoKMGhDbcYkWv9ZyQ%2FT6CVmN%2B6IH1XUsv7DCOKWps4xOy%2BHilOo16wT%2FCTbdZ4pjqiQnyKn1F2W0KVgkP1gl0Il4SybYEL1aPRYiR0E0aOFsKGmY3ql%2BrHV6k2OtoManm53jcBG2374A3kdFsDpYFL8EzJ9LO1lioJnrZexA%2F7iWbPBCInslw7PE0ZYeQBl4kiRyulmTX2TdkFw6t01kkwXdjemI%2BL3sGpD%2FfHvXQckwaQ96XawOtJVf6EKVfuXwjUeiEKuGBWQpJBUUJb%2F4V4OzMbv9ja5oRzvCk%2BeWXpKG5lIc6dUYcnpnRBstn5QFNSS22I4pA3c9EJEho8ak5sF0EScfg3K%2Fv%2Box73QblZx2h%2BlL1ZqHVO5WPICOeTwsadLZXhSzoO7ghLOP15g%2BhHDuP9kBd8eaxqJIJ0mAhvDCd2%2FS8BjqkAbSaZOMc%2B0%2Be%2BHm32eCFFMndLrBEhFQtgn4ta4Ri%2BC%2BGRKlU9Xz75DgAOfHpTJ9ueVvTbsL95wg9z7Rn8Zh7p%2Bu4fnKaCmLTQqg9udsdOHANWxCF4ms88yp3YZbMpmJ994q5JCsmEMh8DsDZkHrTtCCiOyKK2HzSuKk5QBXI311uF0xVj2z7cLea6g%2FzXm1G%2BDYv3I1%2Bdn5IXeXfPJ%2FpzDIbZ4oI&X-Amz-Signature=d870b092806fe71da07c6711177ddd2f7795fce1eca4d03f435576fd7b76c742&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662SWNRNQ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCTvQr0MU0idLFPJjaATGfyDQpfR2zV3VQVFw%2FtLUU%2BEgIhAOoUeh3q%2BTQvwTWoMpXabfJsQyLZ%2BskpILOSKUwRVpPQKogECMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxcEQm4MIerBYtOsrcq3AOhgB9FiVS9fC%2BGloGsB9mD6xi90a32C5JvmP2%2FkfEDSBf84NyF1OfB2gs5VO43gT3eCy5y4%2B%2FhuDEQD5vxGSlnU9VseKs5vzrDRGgPQ%2FMdrQGUxMvUZTXqnAyMVU72tcAGEvMmDet%2FrX81ZkaTBvthVPOd2Oftfwgcea5eKksxsRwuVjHFm637tDjbVVo%2BUEGSWdxtfUZBVYCovhTGoKMGhDbcYkWv9ZyQ%2FT6CVmN%2B6IH1XUsv7DCOKWps4xOy%2BHilOo16wT%2FCTbdZ4pjqiQnyKn1F2W0KVgkP1gl0Il4SybYEL1aPRYiR0E0aOFsKGmY3ql%2BrHV6k2OtoManm53jcBG2374A3kdFsDpYFL8EzJ9LO1lioJnrZexA%2F7iWbPBCInslw7PE0ZYeQBl4kiRyulmTX2TdkFw6t01kkwXdjemI%2BL3sGpD%2FfHvXQckwaQ96XawOtJVf6EKVfuXwjUeiEKuGBWQpJBUUJb%2F4V4OzMbv9ja5oRzvCk%2BeWXpKG5lIc6dUYcnpnRBstn5QFNSS22I4pA3c9EJEho8ak5sF0EScfg3K%2Fv%2Box73QblZx2h%2BlL1ZqHVO5WPICOeTwsadLZXhSzoO7ghLOP15g%2BhHDuP9kBd8eaxqJIJ0mAhvDCd2%2FS8BjqkAbSaZOMc%2B0%2Be%2BHm32eCFFMndLrBEhFQtgn4ta4Ri%2BC%2BGRKlU9Xz75DgAOfHpTJ9ueVvTbsL95wg9z7Rn8Zh7p%2Bu4fnKaCmLTQqg9udsdOHANWxCF4ms88yp3YZbMpmJ994q5JCsmEMh8DsDZkHrTtCCiOyKK2HzSuKk5QBXI311uF0xVj2z7cLea6g%2FzXm1G%2BDYv3I1%2Bdn5IXeXfPJ%2FpzDIbZ4oI&X-Amz-Signature=e36193318b74334c0977582e3cbe01e77c836b129c26a9c847657304cd9f90b9&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662SWNRNQ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCTvQr0MU0idLFPJjaATGfyDQpfR2zV3VQVFw%2FtLUU%2BEgIhAOoUeh3q%2BTQvwTWoMpXabfJsQyLZ%2BskpILOSKUwRVpPQKogECMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxcEQm4MIerBYtOsrcq3AOhgB9FiVS9fC%2BGloGsB9mD6xi90a32C5JvmP2%2FkfEDSBf84NyF1OfB2gs5VO43gT3eCy5y4%2B%2FhuDEQD5vxGSlnU9VseKs5vzrDRGgPQ%2FMdrQGUxMvUZTXqnAyMVU72tcAGEvMmDet%2FrX81ZkaTBvthVPOd2Oftfwgcea5eKksxsRwuVjHFm637tDjbVVo%2BUEGSWdxtfUZBVYCovhTGoKMGhDbcYkWv9ZyQ%2FT6CVmN%2B6IH1XUsv7DCOKWps4xOy%2BHilOo16wT%2FCTbdZ4pjqiQnyKn1F2W0KVgkP1gl0Il4SybYEL1aPRYiR0E0aOFsKGmY3ql%2BrHV6k2OtoManm53jcBG2374A3kdFsDpYFL8EzJ9LO1lioJnrZexA%2F7iWbPBCInslw7PE0ZYeQBl4kiRyulmTX2TdkFw6t01kkwXdjemI%2BL3sGpD%2FfHvXQckwaQ96XawOtJVf6EKVfuXwjUeiEKuGBWQpJBUUJb%2F4V4OzMbv9ja5oRzvCk%2BeWXpKG5lIc6dUYcnpnRBstn5QFNSS22I4pA3c9EJEho8ak5sF0EScfg3K%2Fv%2Box73QblZx2h%2BlL1ZqHVO5WPICOeTwsadLZXhSzoO7ghLOP15g%2BhHDuP9kBd8eaxqJIJ0mAhvDCd2%2FS8BjqkAbSaZOMc%2B0%2Be%2BHm32eCFFMndLrBEhFQtgn4ta4Ri%2BC%2BGRKlU9Xz75DgAOfHpTJ9ueVvTbsL95wg9z7Rn8Zh7p%2Bu4fnKaCmLTQqg9udsdOHANWxCF4ms88yp3YZbMpmJ994q5JCsmEMh8DsDZkHrTtCCiOyKK2HzSuKk5QBXI311uF0xVj2z7cLea6g%2FzXm1G%2BDYv3I1%2Bdn5IXeXfPJ%2FpzDIbZ4oI&X-Amz-Signature=0924e58051d90215830fe508c59a4e0372890fa48819064e3cf03ee4b95209ab&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662SWNRNQ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCTvQr0MU0idLFPJjaATGfyDQpfR2zV3VQVFw%2FtLUU%2BEgIhAOoUeh3q%2BTQvwTWoMpXabfJsQyLZ%2BskpILOSKUwRVpPQKogECMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxcEQm4MIerBYtOsrcq3AOhgB9FiVS9fC%2BGloGsB9mD6xi90a32C5JvmP2%2FkfEDSBf84NyF1OfB2gs5VO43gT3eCy5y4%2B%2FhuDEQD5vxGSlnU9VseKs5vzrDRGgPQ%2FMdrQGUxMvUZTXqnAyMVU72tcAGEvMmDet%2FrX81ZkaTBvthVPOd2Oftfwgcea5eKksxsRwuVjHFm637tDjbVVo%2BUEGSWdxtfUZBVYCovhTGoKMGhDbcYkWv9ZyQ%2FT6CVmN%2B6IH1XUsv7DCOKWps4xOy%2BHilOo16wT%2FCTbdZ4pjqiQnyKn1F2W0KVgkP1gl0Il4SybYEL1aPRYiR0E0aOFsKGmY3ql%2BrHV6k2OtoManm53jcBG2374A3kdFsDpYFL8EzJ9LO1lioJnrZexA%2F7iWbPBCInslw7PE0ZYeQBl4kiRyulmTX2TdkFw6t01kkwXdjemI%2BL3sGpD%2FfHvXQckwaQ96XawOtJVf6EKVfuXwjUeiEKuGBWQpJBUUJb%2F4V4OzMbv9ja5oRzvCk%2BeWXpKG5lIc6dUYcnpnRBstn5QFNSS22I4pA3c9EJEho8ak5sF0EScfg3K%2Fv%2Box73QblZx2h%2BlL1ZqHVO5WPICOeTwsadLZXhSzoO7ghLOP15g%2BhHDuP9kBd8eaxqJIJ0mAhvDCd2%2FS8BjqkAbSaZOMc%2B0%2Be%2BHm32eCFFMndLrBEhFQtgn4ta4Ri%2BC%2BGRKlU9Xz75DgAOfHpTJ9ueVvTbsL95wg9z7Rn8Zh7p%2Bu4fnKaCmLTQqg9udsdOHANWxCF4ms88yp3YZbMpmJ994q5JCsmEMh8DsDZkHrTtCCiOyKK2HzSuKk5QBXI311uF0xVj2z7cLea6g%2FzXm1G%2BDYv3I1%2Bdn5IXeXfPJ%2FpzDIbZ4oI&X-Amz-Signature=a308adc7d29c706bc325afa0cde4623de42e664d10d117e666b3ba1b55c120fe&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662SWNRNQ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCTvQr0MU0idLFPJjaATGfyDQpfR2zV3VQVFw%2FtLUU%2BEgIhAOoUeh3q%2BTQvwTWoMpXabfJsQyLZ%2BskpILOSKUwRVpPQKogECMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxcEQm4MIerBYtOsrcq3AOhgB9FiVS9fC%2BGloGsB9mD6xi90a32C5JvmP2%2FkfEDSBf84NyF1OfB2gs5VO43gT3eCy5y4%2B%2FhuDEQD5vxGSlnU9VseKs5vzrDRGgPQ%2FMdrQGUxMvUZTXqnAyMVU72tcAGEvMmDet%2FrX81ZkaTBvthVPOd2Oftfwgcea5eKksxsRwuVjHFm637tDjbVVo%2BUEGSWdxtfUZBVYCovhTGoKMGhDbcYkWv9ZyQ%2FT6CVmN%2B6IH1XUsv7DCOKWps4xOy%2BHilOo16wT%2FCTbdZ4pjqiQnyKn1F2W0KVgkP1gl0Il4SybYEL1aPRYiR0E0aOFsKGmY3ql%2BrHV6k2OtoManm53jcBG2374A3kdFsDpYFL8EzJ9LO1lioJnrZexA%2F7iWbPBCInslw7PE0ZYeQBl4kiRyulmTX2TdkFw6t01kkwXdjemI%2BL3sGpD%2FfHvXQckwaQ96XawOtJVf6EKVfuXwjUeiEKuGBWQpJBUUJb%2F4V4OzMbv9ja5oRzvCk%2BeWXpKG5lIc6dUYcnpnRBstn5QFNSS22I4pA3c9EJEho8ak5sF0EScfg3K%2Fv%2Box73QblZx2h%2BlL1ZqHVO5WPICOeTwsadLZXhSzoO7ghLOP15g%2BhHDuP9kBd8eaxqJIJ0mAhvDCd2%2FS8BjqkAbSaZOMc%2B0%2Be%2BHm32eCFFMndLrBEhFQtgn4ta4Ri%2BC%2BGRKlU9Xz75DgAOfHpTJ9ueVvTbsL95wg9z7Rn8Zh7p%2Bu4fnKaCmLTQqg9udsdOHANWxCF4ms88yp3YZbMpmJ994q5JCsmEMh8DsDZkHrTtCCiOyKK2HzSuKk5QBXI311uF0xVj2z7cLea6g%2FzXm1G%2BDYv3I1%2Bdn5IXeXfPJ%2FpzDIbZ4oI&X-Amz-Signature=9094bcd1815511190e5d9367d59d828f5021f15afe66ffc05963bf232e133374&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664734CDGU%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAq1UDKniUF7l6yo65Iym1TxBrbFi5U6iw5aVO%2BkMImqAiEA4ng%2BqyFuhJR2Ao2Om82eywMjGFCaysCip6KGx4d53E8qiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMdWxPTa8snrrb0oEyrcA7fDZ6K93X%2F0HuMf92cK29FLCZjEwYkaeo4ElYmgAc9%2BimUjAPry4twh2NakRzH%2Bm0QBFXCF5hWbGzwn%2FeKHSHqOdXYSvdEQEihZfIo8dfyhbc1k%2BPsxgLq8q8fa4zloIVjkiog3GmlUglDuRAG%2BYzOzyEPNetpx%2BP4ojl1hfxJvNakpoDxKoXfqj7P%2FMIKZ9v%2FRrC5hzbYUfpxNIPHbu84PLgiIrzdmNjjrbcHNb%2BozNP4f1AfNJaM7x8aOo63%2B3kqGBgwjWaxX7Qevsn4pRsmEH5VHpUHR7oAu9YUoKn3k7C3%2Fb4p8v99fyPVc5mxx6RArcM3YmbaIjxoOV2rILvAQ53GTtbgSLTNK40pUHNJbfmqUHqr%2FThSQYEoXd650Rp2RLH6eLku8s9e98QL73AMOeYh%2F53U51CIHgPYibG%2BZiRgneyEjfb5bLIU9c%2FJBMPjj6h5KQAT%2FMxNEpPfGI6Kv4ZofAT72LGsIKr3EBLEjsmA5vzusqbVGTKVKieHTcuCYRbqr3IUGwd0TS0sE3bdoMK%2BDw0hVSyL1jLwOU1cvdFgqeBs%2F05%2B8gpTIsF2e22Mu3%2F4nUtRgOh0%2Bicwvt1PH81fVVJ7RAzXJ51ci2XXMW3YWX6mERycYUMOyMIjb9LwGOqUBO6soLGIOlcvx2d2TqFunDi9jzhxfJIi1FqNJv7SdZ0G33ZrwFAb50r86KIJIX4EadNapBjRyTEsuIDjCN4VKmVEIolEeWpz5dfkGxGlLLS%2FqduDjhKnMBiWalwyFg70%2Fve2JLfCLbZtZJKt5dCwUIFVqtt%2F1IzuiAekrAOjB3YzfNfd%2FsRqkUP3m2GACsTgt25pUcX3d3GWUD%2BV67Mxdq8dAEA%2FD&X-Amz-Signature=b91bed37f5f057a87caf8ca92e6a1dc534f1724ca4ae52006739df4db20e6763&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664734CDGU%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAq1UDKniUF7l6yo65Iym1TxBrbFi5U6iw5aVO%2BkMImqAiEA4ng%2BqyFuhJR2Ao2Om82eywMjGFCaysCip6KGx4d53E8qiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMdWxPTa8snrrb0oEyrcA7fDZ6K93X%2F0HuMf92cK29FLCZjEwYkaeo4ElYmgAc9%2BimUjAPry4twh2NakRzH%2Bm0QBFXCF5hWbGzwn%2FeKHSHqOdXYSvdEQEihZfIo8dfyhbc1k%2BPsxgLq8q8fa4zloIVjkiog3GmlUglDuRAG%2BYzOzyEPNetpx%2BP4ojl1hfxJvNakpoDxKoXfqj7P%2FMIKZ9v%2FRrC5hzbYUfpxNIPHbu84PLgiIrzdmNjjrbcHNb%2BozNP4f1AfNJaM7x8aOo63%2B3kqGBgwjWaxX7Qevsn4pRsmEH5VHpUHR7oAu9YUoKn3k7C3%2Fb4p8v99fyPVc5mxx6RArcM3YmbaIjxoOV2rILvAQ53GTtbgSLTNK40pUHNJbfmqUHqr%2FThSQYEoXd650Rp2RLH6eLku8s9e98QL73AMOeYh%2F53U51CIHgPYibG%2BZiRgneyEjfb5bLIU9c%2FJBMPjj6h5KQAT%2FMxNEpPfGI6Kv4ZofAT72LGsIKr3EBLEjsmA5vzusqbVGTKVKieHTcuCYRbqr3IUGwd0TS0sE3bdoMK%2BDw0hVSyL1jLwOU1cvdFgqeBs%2F05%2B8gpTIsF2e22Mu3%2F4nUtRgOh0%2Bicwvt1PH81fVVJ7RAzXJ51ci2XXMW3YWX6mERycYUMOyMIjb9LwGOqUBO6soLGIOlcvx2d2TqFunDi9jzhxfJIi1FqNJv7SdZ0G33ZrwFAb50r86KIJIX4EadNapBjRyTEsuIDjCN4VKmVEIolEeWpz5dfkGxGlLLS%2FqduDjhKnMBiWalwyFg70%2Fve2JLfCLbZtZJKt5dCwUIFVqtt%2F1IzuiAekrAOjB3YzfNfd%2FsRqkUP3m2GACsTgt25pUcX3d3GWUD%2BV67Mxdq8dAEA%2FD&X-Amz-Signature=c980f08a0997118b675e8149fa6f66377cabcec7bd2c7448d6dcc15f5a90a22d&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
