

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665QAY3NFE%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQDhTQbosBVthMYqpO6Q%2F%2BvswjCCyY0sMJmpN968Ub7nwAIgBfIV9LLJoCl%2F%2FjrngKnHhmIYxnJxaIY3FfJrDkQjCiEq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDBNSkOPtHUAX5fAFnyrcAzurYEffUdQxLqQzEVKw7CMBgOsTDddQHM9ijP7AIj5E7jmOcNzVG8rlqIGOiO7oPcFkBOZhaOC14ap7j4GX4N6CF1KkgkC12S4x7mLBMsr4oP0wqUe6zp7hhY5FO7IjeT1JneLdRRq6SM68hu%2F8DSQhRzzDVPhynmkzwkzd5rLQ2%2BONTOOiggbnj5pseN9kGfj8UMRq%2FPzzU4shs91OjDpf4aZTc1cfSct8U4agsZRR2EZLS4%2Be%2BDQldD3qfudPEe2cKQerSdyvOP%2Fji%2BvGObd1cly%2ByXUKsxlpVLR4DMOYJyZaZ1GJpICsyyv6fuLmfJF0ceWAhMoRJMpEvCwzrDcwk9bbVgKZgbB8CSOSy47i%2F6HQJOHw0PI8P0vyN5vhAbKngFeao1bJZn2Kmdn4aFw2u8KWn5XJ9sZxwe2ftI4bnZPL%2B3B1iANQbZqcIsAGPqZXOlE6D8vCvm3T6O2o7sLmYiZThYYOjYN9KrshNj%2FrXGrwDvI2u7S6WGW9nBzp%2F%2BTCymKWfwThd%2FTB0562CK9%2Bi4qWUqxIke3nDIVoipcVBoDmYaIv%2BqskrJb5RkAa%2FZpdywglGmTNseClpxDoKL2eZOnzn9XYbEGeAUo05czyabNrv%2FRBIopZnCG8ML2ihr0GOqUBceJiLJlK%2BdsRrAfSIN9R12UcDDlGyGS71gN1Jnpz8f9jqs%2Bk5KWRsUjZFobv5BSfNrG3USRlX0UoqQ7X7P9TQs3a3MVYBsvDDICGkC6R%2FCsXPoZb2O3fpzVUgb4BirfEBdk%2FDSCEhVKvURTkV2e6nBoZwL6yBQhIUlYqbgwDjznK3Q0MHz6Rv%2B1TZTGadO%2BpF%2FlIYs6GriJwlizQRGl1%2BQR9r0Zf&X-Amz-Signature=56d00d1e481937fabd2b941beaeb8bd57adb67e763dac8b54e7d6f0954f20514&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665QAY3NFE%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQDhTQbosBVthMYqpO6Q%2F%2BvswjCCyY0sMJmpN968Ub7nwAIgBfIV9LLJoCl%2F%2FjrngKnHhmIYxnJxaIY3FfJrDkQjCiEq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDBNSkOPtHUAX5fAFnyrcAzurYEffUdQxLqQzEVKw7CMBgOsTDddQHM9ijP7AIj5E7jmOcNzVG8rlqIGOiO7oPcFkBOZhaOC14ap7j4GX4N6CF1KkgkC12S4x7mLBMsr4oP0wqUe6zp7hhY5FO7IjeT1JneLdRRq6SM68hu%2F8DSQhRzzDVPhynmkzwkzd5rLQ2%2BONTOOiggbnj5pseN9kGfj8UMRq%2FPzzU4shs91OjDpf4aZTc1cfSct8U4agsZRR2EZLS4%2Be%2BDQldD3qfudPEe2cKQerSdyvOP%2Fji%2BvGObd1cly%2ByXUKsxlpVLR4DMOYJyZaZ1GJpICsyyv6fuLmfJF0ceWAhMoRJMpEvCwzrDcwk9bbVgKZgbB8CSOSy47i%2F6HQJOHw0PI8P0vyN5vhAbKngFeao1bJZn2Kmdn4aFw2u8KWn5XJ9sZxwe2ftI4bnZPL%2B3B1iANQbZqcIsAGPqZXOlE6D8vCvm3T6O2o7sLmYiZThYYOjYN9KrshNj%2FrXGrwDvI2u7S6WGW9nBzp%2F%2BTCymKWfwThd%2FTB0562CK9%2Bi4qWUqxIke3nDIVoipcVBoDmYaIv%2BqskrJb5RkAa%2FZpdywglGmTNseClpxDoKL2eZOnzn9XYbEGeAUo05czyabNrv%2FRBIopZnCG8ML2ihr0GOqUBceJiLJlK%2BdsRrAfSIN9R12UcDDlGyGS71gN1Jnpz8f9jqs%2Bk5KWRsUjZFobv5BSfNrG3USRlX0UoqQ7X7P9TQs3a3MVYBsvDDICGkC6R%2FCsXPoZb2O3fpzVUgb4BirfEBdk%2FDSCEhVKvURTkV2e6nBoZwL6yBQhIUlYqbgwDjznK3Q0MHz6Rv%2B1TZTGadO%2BpF%2FlIYs6GriJwlizQRGl1%2BQR9r0Zf&X-Amz-Signature=6d3f0fde96b2e3133a4c3d5f2d522e67a1db728aa6234f84d198d5941f794b56&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665QAY3NFE%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQDhTQbosBVthMYqpO6Q%2F%2BvswjCCyY0sMJmpN968Ub7nwAIgBfIV9LLJoCl%2F%2FjrngKnHhmIYxnJxaIY3FfJrDkQjCiEq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDBNSkOPtHUAX5fAFnyrcAzurYEffUdQxLqQzEVKw7CMBgOsTDddQHM9ijP7AIj5E7jmOcNzVG8rlqIGOiO7oPcFkBOZhaOC14ap7j4GX4N6CF1KkgkC12S4x7mLBMsr4oP0wqUe6zp7hhY5FO7IjeT1JneLdRRq6SM68hu%2F8DSQhRzzDVPhynmkzwkzd5rLQ2%2BONTOOiggbnj5pseN9kGfj8UMRq%2FPzzU4shs91OjDpf4aZTc1cfSct8U4agsZRR2EZLS4%2Be%2BDQldD3qfudPEe2cKQerSdyvOP%2Fji%2BvGObd1cly%2ByXUKsxlpVLR4DMOYJyZaZ1GJpICsyyv6fuLmfJF0ceWAhMoRJMpEvCwzrDcwk9bbVgKZgbB8CSOSy47i%2F6HQJOHw0PI8P0vyN5vhAbKngFeao1bJZn2Kmdn4aFw2u8KWn5XJ9sZxwe2ftI4bnZPL%2B3B1iANQbZqcIsAGPqZXOlE6D8vCvm3T6O2o7sLmYiZThYYOjYN9KrshNj%2FrXGrwDvI2u7S6WGW9nBzp%2F%2BTCymKWfwThd%2FTB0562CK9%2Bi4qWUqxIke3nDIVoipcVBoDmYaIv%2BqskrJb5RkAa%2FZpdywglGmTNseClpxDoKL2eZOnzn9XYbEGeAUo05czyabNrv%2FRBIopZnCG8ML2ihr0GOqUBceJiLJlK%2BdsRrAfSIN9R12UcDDlGyGS71gN1Jnpz8f9jqs%2Bk5KWRsUjZFobv5BSfNrG3USRlX0UoqQ7X7P9TQs3a3MVYBsvDDICGkC6R%2FCsXPoZb2O3fpzVUgb4BirfEBdk%2FDSCEhVKvURTkV2e6nBoZwL6yBQhIUlYqbgwDjznK3Q0MHz6Rv%2B1TZTGadO%2BpF%2FlIYs6GriJwlizQRGl1%2BQR9r0Zf&X-Amz-Signature=e31785597234b140e8caeb9cf9c2296c94c34893d4d92bbddd975b2b9b1f3517&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665QAY3NFE%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQDhTQbosBVthMYqpO6Q%2F%2BvswjCCyY0sMJmpN968Ub7nwAIgBfIV9LLJoCl%2F%2FjrngKnHhmIYxnJxaIY3FfJrDkQjCiEq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDBNSkOPtHUAX5fAFnyrcAzurYEffUdQxLqQzEVKw7CMBgOsTDddQHM9ijP7AIj5E7jmOcNzVG8rlqIGOiO7oPcFkBOZhaOC14ap7j4GX4N6CF1KkgkC12S4x7mLBMsr4oP0wqUe6zp7hhY5FO7IjeT1JneLdRRq6SM68hu%2F8DSQhRzzDVPhynmkzwkzd5rLQ2%2BONTOOiggbnj5pseN9kGfj8UMRq%2FPzzU4shs91OjDpf4aZTc1cfSct8U4agsZRR2EZLS4%2Be%2BDQldD3qfudPEe2cKQerSdyvOP%2Fji%2BvGObd1cly%2ByXUKsxlpVLR4DMOYJyZaZ1GJpICsyyv6fuLmfJF0ceWAhMoRJMpEvCwzrDcwk9bbVgKZgbB8CSOSy47i%2F6HQJOHw0PI8P0vyN5vhAbKngFeao1bJZn2Kmdn4aFw2u8KWn5XJ9sZxwe2ftI4bnZPL%2B3B1iANQbZqcIsAGPqZXOlE6D8vCvm3T6O2o7sLmYiZThYYOjYN9KrshNj%2FrXGrwDvI2u7S6WGW9nBzp%2F%2BTCymKWfwThd%2FTB0562CK9%2Bi4qWUqxIke3nDIVoipcVBoDmYaIv%2BqskrJb5RkAa%2FZpdywglGmTNseClpxDoKL2eZOnzn9XYbEGeAUo05czyabNrv%2FRBIopZnCG8ML2ihr0GOqUBceJiLJlK%2BdsRrAfSIN9R12UcDDlGyGS71gN1Jnpz8f9jqs%2Bk5KWRsUjZFobv5BSfNrG3USRlX0UoqQ7X7P9TQs3a3MVYBsvDDICGkC6R%2FCsXPoZb2O3fpzVUgb4BirfEBdk%2FDSCEhVKvURTkV2e6nBoZwL6yBQhIUlYqbgwDjznK3Q0MHz6Rv%2B1TZTGadO%2BpF%2FlIYs6GriJwlizQRGl1%2BQR9r0Zf&X-Amz-Signature=a5d1d7e76e8853c69b4995595453b9b6c6f6001f3298003a98a175f30048a118&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665QAY3NFE%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQDhTQbosBVthMYqpO6Q%2F%2BvswjCCyY0sMJmpN968Ub7nwAIgBfIV9LLJoCl%2F%2FjrngKnHhmIYxnJxaIY3FfJrDkQjCiEq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDBNSkOPtHUAX5fAFnyrcAzurYEffUdQxLqQzEVKw7CMBgOsTDddQHM9ijP7AIj5E7jmOcNzVG8rlqIGOiO7oPcFkBOZhaOC14ap7j4GX4N6CF1KkgkC12S4x7mLBMsr4oP0wqUe6zp7hhY5FO7IjeT1JneLdRRq6SM68hu%2F8DSQhRzzDVPhynmkzwkzd5rLQ2%2BONTOOiggbnj5pseN9kGfj8UMRq%2FPzzU4shs91OjDpf4aZTc1cfSct8U4agsZRR2EZLS4%2Be%2BDQldD3qfudPEe2cKQerSdyvOP%2Fji%2BvGObd1cly%2ByXUKsxlpVLR4DMOYJyZaZ1GJpICsyyv6fuLmfJF0ceWAhMoRJMpEvCwzrDcwk9bbVgKZgbB8CSOSy47i%2F6HQJOHw0PI8P0vyN5vhAbKngFeao1bJZn2Kmdn4aFw2u8KWn5XJ9sZxwe2ftI4bnZPL%2B3B1iANQbZqcIsAGPqZXOlE6D8vCvm3T6O2o7sLmYiZThYYOjYN9KrshNj%2FrXGrwDvI2u7S6WGW9nBzp%2F%2BTCymKWfwThd%2FTB0562CK9%2Bi4qWUqxIke3nDIVoipcVBoDmYaIv%2BqskrJb5RkAa%2FZpdywglGmTNseClpxDoKL2eZOnzn9XYbEGeAUo05czyabNrv%2FRBIopZnCG8ML2ihr0GOqUBceJiLJlK%2BdsRrAfSIN9R12UcDDlGyGS71gN1Jnpz8f9jqs%2Bk5KWRsUjZFobv5BSfNrG3USRlX0UoqQ7X7P9TQs3a3MVYBsvDDICGkC6R%2FCsXPoZb2O3fpzVUgb4BirfEBdk%2FDSCEhVKvURTkV2e6nBoZwL6yBQhIUlYqbgwDjznK3Q0MHz6Rv%2B1TZTGadO%2BpF%2FlIYs6GriJwlizQRGl1%2BQR9r0Zf&X-Amz-Signature=9c1d747d9e95d586e824334014e250d42e9ed3209e68b620ddd94e1c6156de3d&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665QAY3NFE%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQDhTQbosBVthMYqpO6Q%2F%2BvswjCCyY0sMJmpN968Ub7nwAIgBfIV9LLJoCl%2F%2FjrngKnHhmIYxnJxaIY3FfJrDkQjCiEq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDBNSkOPtHUAX5fAFnyrcAzurYEffUdQxLqQzEVKw7CMBgOsTDddQHM9ijP7AIj5E7jmOcNzVG8rlqIGOiO7oPcFkBOZhaOC14ap7j4GX4N6CF1KkgkC12S4x7mLBMsr4oP0wqUe6zp7hhY5FO7IjeT1JneLdRRq6SM68hu%2F8DSQhRzzDVPhynmkzwkzd5rLQ2%2BONTOOiggbnj5pseN9kGfj8UMRq%2FPzzU4shs91OjDpf4aZTc1cfSct8U4agsZRR2EZLS4%2Be%2BDQldD3qfudPEe2cKQerSdyvOP%2Fji%2BvGObd1cly%2ByXUKsxlpVLR4DMOYJyZaZ1GJpICsyyv6fuLmfJF0ceWAhMoRJMpEvCwzrDcwk9bbVgKZgbB8CSOSy47i%2F6HQJOHw0PI8P0vyN5vhAbKngFeao1bJZn2Kmdn4aFw2u8KWn5XJ9sZxwe2ftI4bnZPL%2B3B1iANQbZqcIsAGPqZXOlE6D8vCvm3T6O2o7sLmYiZThYYOjYN9KrshNj%2FrXGrwDvI2u7S6WGW9nBzp%2F%2BTCymKWfwThd%2FTB0562CK9%2Bi4qWUqxIke3nDIVoipcVBoDmYaIv%2BqskrJb5RkAa%2FZpdywglGmTNseClpxDoKL2eZOnzn9XYbEGeAUo05czyabNrv%2FRBIopZnCG8ML2ihr0GOqUBceJiLJlK%2BdsRrAfSIN9R12UcDDlGyGS71gN1Jnpz8f9jqs%2Bk5KWRsUjZFobv5BSfNrG3USRlX0UoqQ7X7P9TQs3a3MVYBsvDDICGkC6R%2FCsXPoZb2O3fpzVUgb4BirfEBdk%2FDSCEhVKvURTkV2e6nBoZwL6yBQhIUlYqbgwDjznK3Q0MHz6Rv%2B1TZTGadO%2BpF%2FlIYs6GriJwlizQRGl1%2BQR9r0Zf&X-Amz-Signature=6943da5fda1343834e77fdfbcee5e8008023452db7fb4b2ccef8eb85e30b6b1a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665QAY3NFE%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQDhTQbosBVthMYqpO6Q%2F%2BvswjCCyY0sMJmpN968Ub7nwAIgBfIV9LLJoCl%2F%2FjrngKnHhmIYxnJxaIY3FfJrDkQjCiEq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDBNSkOPtHUAX5fAFnyrcAzurYEffUdQxLqQzEVKw7CMBgOsTDddQHM9ijP7AIj5E7jmOcNzVG8rlqIGOiO7oPcFkBOZhaOC14ap7j4GX4N6CF1KkgkC12S4x7mLBMsr4oP0wqUe6zp7hhY5FO7IjeT1JneLdRRq6SM68hu%2F8DSQhRzzDVPhynmkzwkzd5rLQ2%2BONTOOiggbnj5pseN9kGfj8UMRq%2FPzzU4shs91OjDpf4aZTc1cfSct8U4agsZRR2EZLS4%2Be%2BDQldD3qfudPEe2cKQerSdyvOP%2Fji%2BvGObd1cly%2ByXUKsxlpVLR4DMOYJyZaZ1GJpICsyyv6fuLmfJF0ceWAhMoRJMpEvCwzrDcwk9bbVgKZgbB8CSOSy47i%2F6HQJOHw0PI8P0vyN5vhAbKngFeao1bJZn2Kmdn4aFw2u8KWn5XJ9sZxwe2ftI4bnZPL%2B3B1iANQbZqcIsAGPqZXOlE6D8vCvm3T6O2o7sLmYiZThYYOjYN9KrshNj%2FrXGrwDvI2u7S6WGW9nBzp%2F%2BTCymKWfwThd%2FTB0562CK9%2Bi4qWUqxIke3nDIVoipcVBoDmYaIv%2BqskrJb5RkAa%2FZpdywglGmTNseClpxDoKL2eZOnzn9XYbEGeAUo05czyabNrv%2FRBIopZnCG8ML2ihr0GOqUBceJiLJlK%2BdsRrAfSIN9R12UcDDlGyGS71gN1Jnpz8f9jqs%2Bk5KWRsUjZFobv5BSfNrG3USRlX0UoqQ7X7P9TQs3a3MVYBsvDDICGkC6R%2FCsXPoZb2O3fpzVUgb4BirfEBdk%2FDSCEhVKvURTkV2e6nBoZwL6yBQhIUlYqbgwDjznK3Q0MHz6Rv%2B1TZTGadO%2BpF%2FlIYs6GriJwlizQRGl1%2BQR9r0Zf&X-Amz-Signature=4dfa2ba06cb32e0d4620382c8af279ec227b5547957f98ccfdaf3bc5398fd78b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665QAY3NFE%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQDhTQbosBVthMYqpO6Q%2F%2BvswjCCyY0sMJmpN968Ub7nwAIgBfIV9LLJoCl%2F%2FjrngKnHhmIYxnJxaIY3FfJrDkQjCiEq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDBNSkOPtHUAX5fAFnyrcAzurYEffUdQxLqQzEVKw7CMBgOsTDddQHM9ijP7AIj5E7jmOcNzVG8rlqIGOiO7oPcFkBOZhaOC14ap7j4GX4N6CF1KkgkC12S4x7mLBMsr4oP0wqUe6zp7hhY5FO7IjeT1JneLdRRq6SM68hu%2F8DSQhRzzDVPhynmkzwkzd5rLQ2%2BONTOOiggbnj5pseN9kGfj8UMRq%2FPzzU4shs91OjDpf4aZTc1cfSct8U4agsZRR2EZLS4%2Be%2BDQldD3qfudPEe2cKQerSdyvOP%2Fji%2BvGObd1cly%2ByXUKsxlpVLR4DMOYJyZaZ1GJpICsyyv6fuLmfJF0ceWAhMoRJMpEvCwzrDcwk9bbVgKZgbB8CSOSy47i%2F6HQJOHw0PI8P0vyN5vhAbKngFeao1bJZn2Kmdn4aFw2u8KWn5XJ9sZxwe2ftI4bnZPL%2B3B1iANQbZqcIsAGPqZXOlE6D8vCvm3T6O2o7sLmYiZThYYOjYN9KrshNj%2FrXGrwDvI2u7S6WGW9nBzp%2F%2BTCymKWfwThd%2FTB0562CK9%2Bi4qWUqxIke3nDIVoipcVBoDmYaIv%2BqskrJb5RkAa%2FZpdywglGmTNseClpxDoKL2eZOnzn9XYbEGeAUo05czyabNrv%2FRBIopZnCG8ML2ihr0GOqUBceJiLJlK%2BdsRrAfSIN9R12UcDDlGyGS71gN1Jnpz8f9jqs%2Bk5KWRsUjZFobv5BSfNrG3USRlX0UoqQ7X7P9TQs3a3MVYBsvDDICGkC6R%2FCsXPoZb2O3fpzVUgb4BirfEBdk%2FDSCEhVKvURTkV2e6nBoZwL6yBQhIUlYqbgwDjznK3Q0MHz6Rv%2B1TZTGadO%2BpF%2FlIYs6GriJwlizQRGl1%2BQR9r0Zf&X-Amz-Signature=80d6a11c55529d5dc30169b96eb7414a0f790576abbedc8f347dd84e7df18bba&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665QAY3NFE%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQDhTQbosBVthMYqpO6Q%2F%2BvswjCCyY0sMJmpN968Ub7nwAIgBfIV9LLJoCl%2F%2FjrngKnHhmIYxnJxaIY3FfJrDkQjCiEq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDBNSkOPtHUAX5fAFnyrcAzurYEffUdQxLqQzEVKw7CMBgOsTDddQHM9ijP7AIj5E7jmOcNzVG8rlqIGOiO7oPcFkBOZhaOC14ap7j4GX4N6CF1KkgkC12S4x7mLBMsr4oP0wqUe6zp7hhY5FO7IjeT1JneLdRRq6SM68hu%2F8DSQhRzzDVPhynmkzwkzd5rLQ2%2BONTOOiggbnj5pseN9kGfj8UMRq%2FPzzU4shs91OjDpf4aZTc1cfSct8U4agsZRR2EZLS4%2Be%2BDQldD3qfudPEe2cKQerSdyvOP%2Fji%2BvGObd1cly%2ByXUKsxlpVLR4DMOYJyZaZ1GJpICsyyv6fuLmfJF0ceWAhMoRJMpEvCwzrDcwk9bbVgKZgbB8CSOSy47i%2F6HQJOHw0PI8P0vyN5vhAbKngFeao1bJZn2Kmdn4aFw2u8KWn5XJ9sZxwe2ftI4bnZPL%2B3B1iANQbZqcIsAGPqZXOlE6D8vCvm3T6O2o7sLmYiZThYYOjYN9KrshNj%2FrXGrwDvI2u7S6WGW9nBzp%2F%2BTCymKWfwThd%2FTB0562CK9%2Bi4qWUqxIke3nDIVoipcVBoDmYaIv%2BqskrJb5RkAa%2FZpdywglGmTNseClpxDoKL2eZOnzn9XYbEGeAUo05czyabNrv%2FRBIopZnCG8ML2ihr0GOqUBceJiLJlK%2BdsRrAfSIN9R12UcDDlGyGS71gN1Jnpz8f9jqs%2Bk5KWRsUjZFobv5BSfNrG3USRlX0UoqQ7X7P9TQs3a3MVYBsvDDICGkC6R%2FCsXPoZb2O3fpzVUgb4BirfEBdk%2FDSCEhVKvURTkV2e6nBoZwL6yBQhIUlYqbgwDjznK3Q0MHz6Rv%2B1TZTGadO%2BpF%2FlIYs6GriJwlizQRGl1%2BQR9r0Zf&X-Amz-Signature=b32c64b88b2680950c46f5bd937fb52c00e5198990c3bd69e90db1c3904721cc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQ763KQQ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041721Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJGMEQCIFD9h2kXI5yWHhbf2%2BJsB588B3v4kBd49O2nRGZZQ8r3AiB4L0UXeZCZTc3f9ZjrGnyRfi9MS32slGS%2FV4vPVwupmyr%2FAwglEAAaDDYzNzQyMzE4MzgwNSIM3%2Ftb4UcsO%2FaKY8IIKtwDa3xE8mEOuzIPd0kFjMp%2BF7MCF%2FM5%2B%2FkOdKw0vF0su%2Bo50q71Nkbpl%2FiogXfKhWpeK5SBCK1k%2FpidI62W5JRWqaDiWW%2B5CYtu4VtwIU8R%2FmXWIuWEGYGQF7MQEH87oFMM8otjs0HIjgjFjw6TBOgcwaFTXouAlvGCqLwtjjgxSju5UV%2FAA0e6x%2FCwSLl10hzMD42ccWVGocwl0Oh4fRY4ossrg9WnXHANFe4BiqYRdzPRDUAzlAFzLxLep%2BIcP2sWKNVRFR68oITSneNlL%2BgE6D%2Fk3mHE7yndBAtN%2Fm2l6sqZFvwMNNB9d3uVZMFJd5OsWJoSbgqfwIJKT35Nn8QG6rWZmA1XSNgYEvnxjFcgMR%2BqqSKBO78E%2F5TQQcVNw4NPXCdjUFL07LKcKW9aHJCrW6iwUL%2FH8sUh7tP6iErhR3arwXtN76ZH3rPbcbR6XHuWutz2oqq9ddaklu6p4ZjygLR%2BIxTTT4fIG2cGonScOgj4Igof8kwTvRQfEdbYamvSInU86a4kMLrAEjdMfNvYsXVSqhmUeg2Mmn4K82rHhtzENYsnVDjOO%2Bree3i3so1lt5UJpzackU%2F0i4YUS6indmEMeZ28T58ufT0LFrbtjxA%2BpFYMglLgEGt6xpcwzqGGvQY6pgHmhU9C3xG7C7G6h6pW8OHTLGEu1rEnOFdaHIWh75IA3750aMcob4Dwql%2B6kw3Evg1F3i%2BLwjPRJoMg%2Bp7fG1nZ7BJQujN9ZkzW%2FMQunhmHP5%2B2cy29Kngy%2F6xGmg4JCwmnVDT36TWfFSjbHVN3N37vbjdcybPKc8hJZYWAQFtB7nD%2BWaF0bzDKC3qCMyjj1IQ%2F0MnTmNgK7KPaKn%2FA7PFWBNGvnvRH&X-Amz-Signature=ffed099b1bfe70c3f7bfc747e05ce3e90ed077a1c223067fc31e7cb76dc1008b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQ763KQQ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041721Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJGMEQCIFD9h2kXI5yWHhbf2%2BJsB588B3v4kBd49O2nRGZZQ8r3AiB4L0UXeZCZTc3f9ZjrGnyRfi9MS32slGS%2FV4vPVwupmyr%2FAwglEAAaDDYzNzQyMzE4MzgwNSIM3%2Ftb4UcsO%2FaKY8IIKtwDa3xE8mEOuzIPd0kFjMp%2BF7MCF%2FM5%2B%2FkOdKw0vF0su%2Bo50q71Nkbpl%2FiogXfKhWpeK5SBCK1k%2FpidI62W5JRWqaDiWW%2B5CYtu4VtwIU8R%2FmXWIuWEGYGQF7MQEH87oFMM8otjs0HIjgjFjw6TBOgcwaFTXouAlvGCqLwtjjgxSju5UV%2FAA0e6x%2FCwSLl10hzMD42ccWVGocwl0Oh4fRY4ossrg9WnXHANFe4BiqYRdzPRDUAzlAFzLxLep%2BIcP2sWKNVRFR68oITSneNlL%2BgE6D%2Fk3mHE7yndBAtN%2Fm2l6sqZFvwMNNB9d3uVZMFJd5OsWJoSbgqfwIJKT35Nn8QG6rWZmA1XSNgYEvnxjFcgMR%2BqqSKBO78E%2F5TQQcVNw4NPXCdjUFL07LKcKW9aHJCrW6iwUL%2FH8sUh7tP6iErhR3arwXtN76ZH3rPbcbR6XHuWutz2oqq9ddaklu6p4ZjygLR%2BIxTTT4fIG2cGonScOgj4Igof8kwTvRQfEdbYamvSInU86a4kMLrAEjdMfNvYsXVSqhmUeg2Mmn4K82rHhtzENYsnVDjOO%2Bree3i3so1lt5UJpzackU%2F0i4YUS6indmEMeZ28T58ufT0LFrbtjxA%2BpFYMglLgEGt6xpcwzqGGvQY6pgHmhU9C3xG7C7G6h6pW8OHTLGEu1rEnOFdaHIWh75IA3750aMcob4Dwql%2B6kw3Evg1F3i%2BLwjPRJoMg%2Bp7fG1nZ7BJQujN9ZkzW%2FMQunhmHP5%2B2cy29Kngy%2F6xGmg4JCwmnVDT36TWfFSjbHVN3N37vbjdcybPKc8hJZYWAQFtB7nD%2BWaF0bzDKC3qCMyjj1IQ%2F0MnTmNgK7KPaKn%2FA7PFWBNGvnvRH&X-Amz-Signature=ab64d6a69784a773a12d3740eee16bcb4a796156748b9a16802e69b0697a4be4&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
