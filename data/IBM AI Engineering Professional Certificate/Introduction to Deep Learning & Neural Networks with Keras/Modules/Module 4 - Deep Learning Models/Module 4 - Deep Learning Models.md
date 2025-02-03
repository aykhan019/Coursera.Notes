

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664W64BXTC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141425Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDZtK20hCPCat4%2F8mvNF%2BfBAiLUvj%2F%2BLrO%2FnaOXrtvDuAIhAK%2BDTtCKcUFtvl1DHRJwOBeaDAkzgxSon8BVgLal%2F1TfKv8DCBcQABoMNjM3NDIzMTgzODA1Igy3Nhfez0Naju0sxrwq3AP%2BmtoFcfRyeGKrza5CF8q7%2FSr6f1N%2B74X2kGn%2FpLiovCnZzR6%2BG1SNrGMT48UmtZ4u7aGnq4l2m22Wm44ktxGFxRNiCdyzqyf9vQpnfA8QXqLYcaztCho4F9lAk%2BmsfKz2hEsRcdzRVvG3XA0A7BAX5n8RWzOz0jidy7KCg0twPKuBzlNwxU07NCt4yhJtQ5Rpv7HgqDzjMOuZbZYY4QA6zq8CRkUcGfzcrTLrMfcQ%2F%2BGGCDn5uBsMYNIHhtAuxYN19N0bZeyepR5EbjHW9x44tBBixB%2BB%2Bu%2BukKQbblauYnh3gpsa0tkL88wNBaVFcYCQmp011rOa1iu53eZ2ofzUppDAkIsGnnzGCzkrPydtGepQfRfJrSNtwF%2FajUF8Ei743nlQ7b0etMBzamFr%2Bzxu6CbCdyoQpLQe4VcKTrqCqzqH19RRqQ9sP2zwrnKmjpce82SshYn7hKFtSjiiayML09OPE5j8TP2na3k3%2FQUYjgtojfO5dkIDXVCq3x6ok4kd8bdC%2Fv9%2Fa2BpTofgidPEAliRIYMJ9zzrl%2F3jZpTn7yhMZFTHG9MV0PTCAcv5De6SN9MRAoj79LRyJbLt7eK6uUh8jwMgb7sHDuLMqsh23JcCOizaP8TPpOXCdTDjjYO9BjqkAcaG%2BqUeE2Qwdn1VO2qB1xvdkfHWh1E%2F8P2AB0nn6pSCVEmGcEDHZWWSFtGGXEeu6jRPha0voqX7OS4Kkjf9AhkJoNti7728p7BA2zqkc%2F2M9OV7d7ABk8FoZg2Qfv3ynKpK1S3m3npAbpcTqqP3efVEQgSHPRvXyXVd%2FtIdqj6gGwEVkfX4wX%2BZoZRs9mVpVtJiSDMV%2FhHd34LWRntXs3rkol2c&X-Amz-Signature=baabf244fe82555c3f9671f66a328b66ed43568cdca116f1c2e269e65461e220&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664W64BXTC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141425Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDZtK20hCPCat4%2F8mvNF%2BfBAiLUvj%2F%2BLrO%2FnaOXrtvDuAIhAK%2BDTtCKcUFtvl1DHRJwOBeaDAkzgxSon8BVgLal%2F1TfKv8DCBcQABoMNjM3NDIzMTgzODA1Igy3Nhfez0Naju0sxrwq3AP%2BmtoFcfRyeGKrza5CF8q7%2FSr6f1N%2B74X2kGn%2FpLiovCnZzR6%2BG1SNrGMT48UmtZ4u7aGnq4l2m22Wm44ktxGFxRNiCdyzqyf9vQpnfA8QXqLYcaztCho4F9lAk%2BmsfKz2hEsRcdzRVvG3XA0A7BAX5n8RWzOz0jidy7KCg0twPKuBzlNwxU07NCt4yhJtQ5Rpv7HgqDzjMOuZbZYY4QA6zq8CRkUcGfzcrTLrMfcQ%2F%2BGGCDn5uBsMYNIHhtAuxYN19N0bZeyepR5EbjHW9x44tBBixB%2BB%2Bu%2BukKQbblauYnh3gpsa0tkL88wNBaVFcYCQmp011rOa1iu53eZ2ofzUppDAkIsGnnzGCzkrPydtGepQfRfJrSNtwF%2FajUF8Ei743nlQ7b0etMBzamFr%2Bzxu6CbCdyoQpLQe4VcKTrqCqzqH19RRqQ9sP2zwrnKmjpce82SshYn7hKFtSjiiayML09OPE5j8TP2na3k3%2FQUYjgtojfO5dkIDXVCq3x6ok4kd8bdC%2Fv9%2Fa2BpTofgidPEAliRIYMJ9zzrl%2F3jZpTn7yhMZFTHG9MV0PTCAcv5De6SN9MRAoj79LRyJbLt7eK6uUh8jwMgb7sHDuLMqsh23JcCOizaP8TPpOXCdTDjjYO9BjqkAcaG%2BqUeE2Qwdn1VO2qB1xvdkfHWh1E%2F8P2AB0nn6pSCVEmGcEDHZWWSFtGGXEeu6jRPha0voqX7OS4Kkjf9AhkJoNti7728p7BA2zqkc%2F2M9OV7d7ABk8FoZg2Qfv3ynKpK1S3m3npAbpcTqqP3efVEQgSHPRvXyXVd%2FtIdqj6gGwEVkfX4wX%2BZoZRs9mVpVtJiSDMV%2FhHd34LWRntXs3rkol2c&X-Amz-Signature=c44f2073fdbdb52c028356b64b2c106cb9d2f48d4ad508925aca56b521f859bd&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664W64BXTC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141425Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDZtK20hCPCat4%2F8mvNF%2BfBAiLUvj%2F%2BLrO%2FnaOXrtvDuAIhAK%2BDTtCKcUFtvl1DHRJwOBeaDAkzgxSon8BVgLal%2F1TfKv8DCBcQABoMNjM3NDIzMTgzODA1Igy3Nhfez0Naju0sxrwq3AP%2BmtoFcfRyeGKrza5CF8q7%2FSr6f1N%2B74X2kGn%2FpLiovCnZzR6%2BG1SNrGMT48UmtZ4u7aGnq4l2m22Wm44ktxGFxRNiCdyzqyf9vQpnfA8QXqLYcaztCho4F9lAk%2BmsfKz2hEsRcdzRVvG3XA0A7BAX5n8RWzOz0jidy7KCg0twPKuBzlNwxU07NCt4yhJtQ5Rpv7HgqDzjMOuZbZYY4QA6zq8CRkUcGfzcrTLrMfcQ%2F%2BGGCDn5uBsMYNIHhtAuxYN19N0bZeyepR5EbjHW9x44tBBixB%2BB%2Bu%2BukKQbblauYnh3gpsa0tkL88wNBaVFcYCQmp011rOa1iu53eZ2ofzUppDAkIsGnnzGCzkrPydtGepQfRfJrSNtwF%2FajUF8Ei743nlQ7b0etMBzamFr%2Bzxu6CbCdyoQpLQe4VcKTrqCqzqH19RRqQ9sP2zwrnKmjpce82SshYn7hKFtSjiiayML09OPE5j8TP2na3k3%2FQUYjgtojfO5dkIDXVCq3x6ok4kd8bdC%2Fv9%2Fa2BpTofgidPEAliRIYMJ9zzrl%2F3jZpTn7yhMZFTHG9MV0PTCAcv5De6SN9MRAoj79LRyJbLt7eK6uUh8jwMgb7sHDuLMqsh23JcCOizaP8TPpOXCdTDjjYO9BjqkAcaG%2BqUeE2Qwdn1VO2qB1xvdkfHWh1E%2F8P2AB0nn6pSCVEmGcEDHZWWSFtGGXEeu6jRPha0voqX7OS4Kkjf9AhkJoNti7728p7BA2zqkc%2F2M9OV7d7ABk8FoZg2Qfv3ynKpK1S3m3npAbpcTqqP3efVEQgSHPRvXyXVd%2FtIdqj6gGwEVkfX4wX%2BZoZRs9mVpVtJiSDMV%2FhHd34LWRntXs3rkol2c&X-Amz-Signature=b45691804c8453e225a8eb4693e7ec6f11ed69bbca4279a0364bb57693f63d89&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664W64BXTC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141424Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDZtK20hCPCat4%2F8mvNF%2BfBAiLUvj%2F%2BLrO%2FnaOXrtvDuAIhAK%2BDTtCKcUFtvl1DHRJwOBeaDAkzgxSon8BVgLal%2F1TfKv8DCBcQABoMNjM3NDIzMTgzODA1Igy3Nhfez0Naju0sxrwq3AP%2BmtoFcfRyeGKrza5CF8q7%2FSr6f1N%2B74X2kGn%2FpLiovCnZzR6%2BG1SNrGMT48UmtZ4u7aGnq4l2m22Wm44ktxGFxRNiCdyzqyf9vQpnfA8QXqLYcaztCho4F9lAk%2BmsfKz2hEsRcdzRVvG3XA0A7BAX5n8RWzOz0jidy7KCg0twPKuBzlNwxU07NCt4yhJtQ5Rpv7HgqDzjMOuZbZYY4QA6zq8CRkUcGfzcrTLrMfcQ%2F%2BGGCDn5uBsMYNIHhtAuxYN19N0bZeyepR5EbjHW9x44tBBixB%2BB%2Bu%2BukKQbblauYnh3gpsa0tkL88wNBaVFcYCQmp011rOa1iu53eZ2ofzUppDAkIsGnnzGCzkrPydtGepQfRfJrSNtwF%2FajUF8Ei743nlQ7b0etMBzamFr%2Bzxu6CbCdyoQpLQe4VcKTrqCqzqH19RRqQ9sP2zwrnKmjpce82SshYn7hKFtSjiiayML09OPE5j8TP2na3k3%2FQUYjgtojfO5dkIDXVCq3x6ok4kd8bdC%2Fv9%2Fa2BpTofgidPEAliRIYMJ9zzrl%2F3jZpTn7yhMZFTHG9MV0PTCAcv5De6SN9MRAoj79LRyJbLt7eK6uUh8jwMgb7sHDuLMqsh23JcCOizaP8TPpOXCdTDjjYO9BjqkAcaG%2BqUeE2Qwdn1VO2qB1xvdkfHWh1E%2F8P2AB0nn6pSCVEmGcEDHZWWSFtGGXEeu6jRPha0voqX7OS4Kkjf9AhkJoNti7728p7BA2zqkc%2F2M9OV7d7ABk8FoZg2Qfv3ynKpK1S3m3npAbpcTqqP3efVEQgSHPRvXyXVd%2FtIdqj6gGwEVkfX4wX%2BZoZRs9mVpVtJiSDMV%2FhHd34LWRntXs3rkol2c&X-Amz-Signature=46c9f84a4f108d31ccbec0bb2474609c09f56cc7e28420c7519d19accfff0f1b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664W64BXTC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141424Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDZtK20hCPCat4%2F8mvNF%2BfBAiLUvj%2F%2BLrO%2FnaOXrtvDuAIhAK%2BDTtCKcUFtvl1DHRJwOBeaDAkzgxSon8BVgLal%2F1TfKv8DCBcQABoMNjM3NDIzMTgzODA1Igy3Nhfez0Naju0sxrwq3AP%2BmtoFcfRyeGKrza5CF8q7%2FSr6f1N%2B74X2kGn%2FpLiovCnZzR6%2BG1SNrGMT48UmtZ4u7aGnq4l2m22Wm44ktxGFxRNiCdyzqyf9vQpnfA8QXqLYcaztCho4F9lAk%2BmsfKz2hEsRcdzRVvG3XA0A7BAX5n8RWzOz0jidy7KCg0twPKuBzlNwxU07NCt4yhJtQ5Rpv7HgqDzjMOuZbZYY4QA6zq8CRkUcGfzcrTLrMfcQ%2F%2BGGCDn5uBsMYNIHhtAuxYN19N0bZeyepR5EbjHW9x44tBBixB%2BB%2Bu%2BukKQbblauYnh3gpsa0tkL88wNBaVFcYCQmp011rOa1iu53eZ2ofzUppDAkIsGnnzGCzkrPydtGepQfRfJrSNtwF%2FajUF8Ei743nlQ7b0etMBzamFr%2Bzxu6CbCdyoQpLQe4VcKTrqCqzqH19RRqQ9sP2zwrnKmjpce82SshYn7hKFtSjiiayML09OPE5j8TP2na3k3%2FQUYjgtojfO5dkIDXVCq3x6ok4kd8bdC%2Fv9%2Fa2BpTofgidPEAliRIYMJ9zzrl%2F3jZpTn7yhMZFTHG9MV0PTCAcv5De6SN9MRAoj79LRyJbLt7eK6uUh8jwMgb7sHDuLMqsh23JcCOizaP8TPpOXCdTDjjYO9BjqkAcaG%2BqUeE2Qwdn1VO2qB1xvdkfHWh1E%2F8P2AB0nn6pSCVEmGcEDHZWWSFtGGXEeu6jRPha0voqX7OS4Kkjf9AhkJoNti7728p7BA2zqkc%2F2M9OV7d7ABk8FoZg2Qfv3ynKpK1S3m3npAbpcTqqP3efVEQgSHPRvXyXVd%2FtIdqj6gGwEVkfX4wX%2BZoZRs9mVpVtJiSDMV%2FhHd34LWRntXs3rkol2c&X-Amz-Signature=be990420db60f67fe103738dc7b8253c8506e970369968fbd59786347a0ef84e&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664W64BXTC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141424Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDZtK20hCPCat4%2F8mvNF%2BfBAiLUvj%2F%2BLrO%2FnaOXrtvDuAIhAK%2BDTtCKcUFtvl1DHRJwOBeaDAkzgxSon8BVgLal%2F1TfKv8DCBcQABoMNjM3NDIzMTgzODA1Igy3Nhfez0Naju0sxrwq3AP%2BmtoFcfRyeGKrza5CF8q7%2FSr6f1N%2B74X2kGn%2FpLiovCnZzR6%2BG1SNrGMT48UmtZ4u7aGnq4l2m22Wm44ktxGFxRNiCdyzqyf9vQpnfA8QXqLYcaztCho4F9lAk%2BmsfKz2hEsRcdzRVvG3XA0A7BAX5n8RWzOz0jidy7KCg0twPKuBzlNwxU07NCt4yhJtQ5Rpv7HgqDzjMOuZbZYY4QA6zq8CRkUcGfzcrTLrMfcQ%2F%2BGGCDn5uBsMYNIHhtAuxYN19N0bZeyepR5EbjHW9x44tBBixB%2BB%2Bu%2BukKQbblauYnh3gpsa0tkL88wNBaVFcYCQmp011rOa1iu53eZ2ofzUppDAkIsGnnzGCzkrPydtGepQfRfJrSNtwF%2FajUF8Ei743nlQ7b0etMBzamFr%2Bzxu6CbCdyoQpLQe4VcKTrqCqzqH19RRqQ9sP2zwrnKmjpce82SshYn7hKFtSjiiayML09OPE5j8TP2na3k3%2FQUYjgtojfO5dkIDXVCq3x6ok4kd8bdC%2Fv9%2Fa2BpTofgidPEAliRIYMJ9zzrl%2F3jZpTn7yhMZFTHG9MV0PTCAcv5De6SN9MRAoj79LRyJbLt7eK6uUh8jwMgb7sHDuLMqsh23JcCOizaP8TPpOXCdTDjjYO9BjqkAcaG%2BqUeE2Qwdn1VO2qB1xvdkfHWh1E%2F8P2AB0nn6pSCVEmGcEDHZWWSFtGGXEeu6jRPha0voqX7OS4Kkjf9AhkJoNti7728p7BA2zqkc%2F2M9OV7d7ABk8FoZg2Qfv3ynKpK1S3m3npAbpcTqqP3efVEQgSHPRvXyXVd%2FtIdqj6gGwEVkfX4wX%2BZoZRs9mVpVtJiSDMV%2FhHd34LWRntXs3rkol2c&X-Amz-Signature=a595a8f99b18691fcca52411513fc94c5317df24632147d19fcef9abb066ab4b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664W64BXTC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141425Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDZtK20hCPCat4%2F8mvNF%2BfBAiLUvj%2F%2BLrO%2FnaOXrtvDuAIhAK%2BDTtCKcUFtvl1DHRJwOBeaDAkzgxSon8BVgLal%2F1TfKv8DCBcQABoMNjM3NDIzMTgzODA1Igy3Nhfez0Naju0sxrwq3AP%2BmtoFcfRyeGKrza5CF8q7%2FSr6f1N%2B74X2kGn%2FpLiovCnZzR6%2BG1SNrGMT48UmtZ4u7aGnq4l2m22Wm44ktxGFxRNiCdyzqyf9vQpnfA8QXqLYcaztCho4F9lAk%2BmsfKz2hEsRcdzRVvG3XA0A7BAX5n8RWzOz0jidy7KCg0twPKuBzlNwxU07NCt4yhJtQ5Rpv7HgqDzjMOuZbZYY4QA6zq8CRkUcGfzcrTLrMfcQ%2F%2BGGCDn5uBsMYNIHhtAuxYN19N0bZeyepR5EbjHW9x44tBBixB%2BB%2Bu%2BukKQbblauYnh3gpsa0tkL88wNBaVFcYCQmp011rOa1iu53eZ2ofzUppDAkIsGnnzGCzkrPydtGepQfRfJrSNtwF%2FajUF8Ei743nlQ7b0etMBzamFr%2Bzxu6CbCdyoQpLQe4VcKTrqCqzqH19RRqQ9sP2zwrnKmjpce82SshYn7hKFtSjiiayML09OPE5j8TP2na3k3%2FQUYjgtojfO5dkIDXVCq3x6ok4kd8bdC%2Fv9%2Fa2BpTofgidPEAliRIYMJ9zzrl%2F3jZpTn7yhMZFTHG9MV0PTCAcv5De6SN9MRAoj79LRyJbLt7eK6uUh8jwMgb7sHDuLMqsh23JcCOizaP8TPpOXCdTDjjYO9BjqkAcaG%2BqUeE2Qwdn1VO2qB1xvdkfHWh1E%2F8P2AB0nn6pSCVEmGcEDHZWWSFtGGXEeu6jRPha0voqX7OS4Kkjf9AhkJoNti7728p7BA2zqkc%2F2M9OV7d7ABk8FoZg2Qfv3ynKpK1S3m3npAbpcTqqP3efVEQgSHPRvXyXVd%2FtIdqj6gGwEVkfX4wX%2BZoZRs9mVpVtJiSDMV%2FhHd34LWRntXs3rkol2c&X-Amz-Signature=96ccf8f44a434eca70b1d8a24e7c3a5ca4c8de080f15e30ebfd06e41afd380ad&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664W64BXTC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141425Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDZtK20hCPCat4%2F8mvNF%2BfBAiLUvj%2F%2BLrO%2FnaOXrtvDuAIhAK%2BDTtCKcUFtvl1DHRJwOBeaDAkzgxSon8BVgLal%2F1TfKv8DCBcQABoMNjM3NDIzMTgzODA1Igy3Nhfez0Naju0sxrwq3AP%2BmtoFcfRyeGKrza5CF8q7%2FSr6f1N%2B74X2kGn%2FpLiovCnZzR6%2BG1SNrGMT48UmtZ4u7aGnq4l2m22Wm44ktxGFxRNiCdyzqyf9vQpnfA8QXqLYcaztCho4F9lAk%2BmsfKz2hEsRcdzRVvG3XA0A7BAX5n8RWzOz0jidy7KCg0twPKuBzlNwxU07NCt4yhJtQ5Rpv7HgqDzjMOuZbZYY4QA6zq8CRkUcGfzcrTLrMfcQ%2F%2BGGCDn5uBsMYNIHhtAuxYN19N0bZeyepR5EbjHW9x44tBBixB%2BB%2Bu%2BukKQbblauYnh3gpsa0tkL88wNBaVFcYCQmp011rOa1iu53eZ2ofzUppDAkIsGnnzGCzkrPydtGepQfRfJrSNtwF%2FajUF8Ei743nlQ7b0etMBzamFr%2Bzxu6CbCdyoQpLQe4VcKTrqCqzqH19RRqQ9sP2zwrnKmjpce82SshYn7hKFtSjiiayML09OPE5j8TP2na3k3%2FQUYjgtojfO5dkIDXVCq3x6ok4kd8bdC%2Fv9%2Fa2BpTofgidPEAliRIYMJ9zzrl%2F3jZpTn7yhMZFTHG9MV0PTCAcv5De6SN9MRAoj79LRyJbLt7eK6uUh8jwMgb7sHDuLMqsh23JcCOizaP8TPpOXCdTDjjYO9BjqkAcaG%2BqUeE2Qwdn1VO2qB1xvdkfHWh1E%2F8P2AB0nn6pSCVEmGcEDHZWWSFtGGXEeu6jRPha0voqX7OS4Kkjf9AhkJoNti7728p7BA2zqkc%2F2M9OV7d7ABk8FoZg2Qfv3ynKpK1S3m3npAbpcTqqP3efVEQgSHPRvXyXVd%2FtIdqj6gGwEVkfX4wX%2BZoZRs9mVpVtJiSDMV%2FhHd34LWRntXs3rkol2c&X-Amz-Signature=738e9545e130904ddd42838e9857b37425e45dca88c27e200db92f1c3aad13bc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664W64BXTC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141425Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDZtK20hCPCat4%2F8mvNF%2BfBAiLUvj%2F%2BLrO%2FnaOXrtvDuAIhAK%2BDTtCKcUFtvl1DHRJwOBeaDAkzgxSon8BVgLal%2F1TfKv8DCBcQABoMNjM3NDIzMTgzODA1Igy3Nhfez0Naju0sxrwq3AP%2BmtoFcfRyeGKrza5CF8q7%2FSr6f1N%2B74X2kGn%2FpLiovCnZzR6%2BG1SNrGMT48UmtZ4u7aGnq4l2m22Wm44ktxGFxRNiCdyzqyf9vQpnfA8QXqLYcaztCho4F9lAk%2BmsfKz2hEsRcdzRVvG3XA0A7BAX5n8RWzOz0jidy7KCg0twPKuBzlNwxU07NCt4yhJtQ5Rpv7HgqDzjMOuZbZYY4QA6zq8CRkUcGfzcrTLrMfcQ%2F%2BGGCDn5uBsMYNIHhtAuxYN19N0bZeyepR5EbjHW9x44tBBixB%2BB%2Bu%2BukKQbblauYnh3gpsa0tkL88wNBaVFcYCQmp011rOa1iu53eZ2ofzUppDAkIsGnnzGCzkrPydtGepQfRfJrSNtwF%2FajUF8Ei743nlQ7b0etMBzamFr%2Bzxu6CbCdyoQpLQe4VcKTrqCqzqH19RRqQ9sP2zwrnKmjpce82SshYn7hKFtSjiiayML09OPE5j8TP2na3k3%2FQUYjgtojfO5dkIDXVCq3x6ok4kd8bdC%2Fv9%2Fa2BpTofgidPEAliRIYMJ9zzrl%2F3jZpTn7yhMZFTHG9MV0PTCAcv5De6SN9MRAoj79LRyJbLt7eK6uUh8jwMgb7sHDuLMqsh23JcCOizaP8TPpOXCdTDjjYO9BjqkAcaG%2BqUeE2Qwdn1VO2qB1xvdkfHWh1E%2F8P2AB0nn6pSCVEmGcEDHZWWSFtGGXEeu6jRPha0voqX7OS4Kkjf9AhkJoNti7728p7BA2zqkc%2F2M9OV7d7ABk8FoZg2Qfv3ynKpK1S3m3npAbpcTqqP3efVEQgSHPRvXyXVd%2FtIdqj6gGwEVkfX4wX%2BZoZRs9mVpVtJiSDMV%2FhHd34LWRntXs3rkol2c&X-Amz-Signature=a1b53954caa9cf5f50bbb05548d29dcc1b19feaf74d4d9e43a1c19f0e24e8bdb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UI5PFB55%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141425Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCjrMLeAzuAlaG%2BNTgXyPY49Qsp%2BUqHVlE%2BCHeokOtTCAIgG36xtGJgxuTSFExpX%2FLGr9Dc572r1e%2Byi8MJYJUEbLoq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDLbvks7Mk43XnRuxPyrcAyojhO5imBHXd7p%2FtFROFnmOmJnBDwA7Qr7vUpzwcJqPTkBXqH%2BL1AfVzZ75rLUTVR9Iy%2BofV6DB%2BaEdO76a6%2BfL22AOq5K5Xm5SfcY8P9fbuH5bbAOA0ZWkzEdzaAPcYVm9MYa%2F76A9V5gQp3XpwS%2FmYY6FUMAVxmPgFBUULMtEx1LJ9XddP9tFAiBVISpdYKX9J2klWGzbKglEU%2FaZwusI8o%2Bpw63mJdXnsAseawQjHkmBGhNzerAdLW%2BRuKjc7eFyNVrOw3iSe92cNw5DVf66Rvd8CPi8FXsxcqNDOi0oVpBJgDBVHB0dXxrKVPhz%2B13pZKl%2FDuqTCYS0ltrf8OgZsQ2pEr2KEh6jymkKb9qbvM6KbAQjadqzJEc1bcM1YA41pfOqw6qX1arWYm5YiqZHwVu1jqw2dfBb2ALFWNI2ScDH%2BYfrJI2YLHuMOMrbwr8UP5HK8DgPnMS2Ha6sA%2Bj3NpagkNbTU7v8KN7vGm4iuE3kaOy8zY2U841%2F251UZWyqW%2FWtUoUyjLml3HAXxrk6mSLOdP5nI%2BsLGsaaDXOBlRZXebfk3vbPmq6FPKaVFZ5fMhurYttAM8iXxA8rtS9a3ihezU0YFTPNdh58D0RCHbBeD7CpV0x35CRrMNeNg70GOqUBL5gA9XtecNtXAMaPCq%2F2flacfQtDTlvOpmRlePapYC%2FNQBoXxrFLdSo%2F8wReZWEl14qbviEvsopE3amyaXgUVkcEy2L%2BlAKFlYXpEUFzPG6aFAqm%2BtnyTxEBr7VRkGg3xpecx9V9Gy1QZg6BSy%2FWzhoTYZkGBstQNPdlx20SdDrEsXKUSoDcjznFFycjYI2UHC44pumWV9y%2FT5BBhBiTYa8FIY3b&X-Amz-Signature=1ce4f55246145f9375dd5340228323142a8cc41f4e3cc783d4f2dbba12a35e92&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UI5PFB55%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141425Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCjrMLeAzuAlaG%2BNTgXyPY49Qsp%2BUqHVlE%2BCHeokOtTCAIgG36xtGJgxuTSFExpX%2FLGr9Dc572r1e%2Byi8MJYJUEbLoq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDLbvks7Mk43XnRuxPyrcAyojhO5imBHXd7p%2FtFROFnmOmJnBDwA7Qr7vUpzwcJqPTkBXqH%2BL1AfVzZ75rLUTVR9Iy%2BofV6DB%2BaEdO76a6%2BfL22AOq5K5Xm5SfcY8P9fbuH5bbAOA0ZWkzEdzaAPcYVm9MYa%2F76A9V5gQp3XpwS%2FmYY6FUMAVxmPgFBUULMtEx1LJ9XddP9tFAiBVISpdYKX9J2klWGzbKglEU%2FaZwusI8o%2Bpw63mJdXnsAseawQjHkmBGhNzerAdLW%2BRuKjc7eFyNVrOw3iSe92cNw5DVf66Rvd8CPi8FXsxcqNDOi0oVpBJgDBVHB0dXxrKVPhz%2B13pZKl%2FDuqTCYS0ltrf8OgZsQ2pEr2KEh6jymkKb9qbvM6KbAQjadqzJEc1bcM1YA41pfOqw6qX1arWYm5YiqZHwVu1jqw2dfBb2ALFWNI2ScDH%2BYfrJI2YLHuMOMrbwr8UP5HK8DgPnMS2Ha6sA%2Bj3NpagkNbTU7v8KN7vGm4iuE3kaOy8zY2U841%2F251UZWyqW%2FWtUoUyjLml3HAXxrk6mSLOdP5nI%2BsLGsaaDXOBlRZXebfk3vbPmq6FPKaVFZ5fMhurYttAM8iXxA8rtS9a3ihezU0YFTPNdh58D0RCHbBeD7CpV0x35CRrMNeNg70GOqUBL5gA9XtecNtXAMaPCq%2F2flacfQtDTlvOpmRlePapYC%2FNQBoXxrFLdSo%2F8wReZWEl14qbviEvsopE3amyaXgUVkcEy2L%2BlAKFlYXpEUFzPG6aFAqm%2BtnyTxEBr7VRkGg3xpecx9V9Gy1QZg6BSy%2FWzhoTYZkGBstQNPdlx20SdDrEsXKUSoDcjznFFycjYI2UHC44pumWV9y%2FT5BBhBiTYa8FIY3b&X-Amz-Signature=e98261530148650f9981ea61d3647d97eab791ef12dcd8d219a8d1359503d07c&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
