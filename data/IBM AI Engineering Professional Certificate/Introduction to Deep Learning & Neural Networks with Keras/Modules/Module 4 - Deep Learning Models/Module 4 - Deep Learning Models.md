

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TVTW3N6P%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJGMEQCIDnNH34W9M8NCLcXVcMgdIELSIZY762ua2Y8%2FyLoRHXpAiApHpC7aoyMpVKx7W7mCFe3SFQxidlPOLnwNlB%2BAGqfxir%2FAwhJEAAaDDYzNzQyMzE4MzgwNSIMnCVDvhZz%2BmU4YtFeKtwDDC7dkQ1NUEMEnNiUMDg0omHewVgz0x4jH99bUjsBDtg%2Bz%2BhVuoaV%2B7TXRnO0%2BYhDBz3rKjK5WopJh4Wqmt8vk5iWDUP%2BwrAcVxgluTdoxU8ZXk4KtfzmTg77XzFpthWiQIhKjLpEi7E1QOtTP63OI3NGrAgTLn%2BEKKM1vH5NENXG6o5lR1JdFF1m9KAKzP05jPtcWQTpuYYYU2%2FIVZMSBAinHbG6bGJBLIZ5mHa9iBYqdrtYIY4oOxe2QjTL3n%2BsYFOic15fkMm17WkxYGT9bTqjoJwjWBgaz8pd6ipjy0iGa8L8rQ9C0D%2BYlkT2w5BZjRPxIMbkcAT%2FwV3oHjQ5zXfXL19mO6sjMh9UEZPLbm6jOFCHQFq8DsH73b2yQqFq8TNCCskuLboX9HycSULkQO6lXZ8yA2aUXErIZNqYQj5OPXJ7pPJ6w4aC326Y3ioz5hZW1PDnvspKY48IQEaN2dx4hpO%2F0DQDrpg4rMsEzQl08nQ1F0z3rKuN3de2Ldsd3WzDaEiZlkmQyXpjPu5kpAtkGW1U0xOJIlgdC7NQlgTlKtYSA32kR%2F%2FWXwoJPOxF5eSiJ%2FKvDpuXRbuzgozAq5Owqb7JXI39ECNLbTfr2uheB8LySziSxXs0hm4wnp2OvQY6pgHWKDSq5KkgF5%2BSsL0weUm4BKzD2gRwoBajLB7vfSJd5EF45UMTeIisGBButRy87LyXcDGUqWvJNNzLbtP%2B%2BX5MpA8leasQmKwstOcN%2Fp%2BAwJjyyb%2Bvs3uaQ1ndhccA8t2Hqfy52u%2FCIrsyuc4a%2BCTyusV3t3sZOhJC2Naq8lznXXFCDF1vMum%2FlLCkP%2F2%2Ft61EF4JI4bTsY7Dx%2FQywyhXneTOcvbky&X-Amz-Signature=18c4eece92842d086acc5218002b56f4782f0fcbc0bd557a0fc1fb02e5c0407b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TVTW3N6P%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJGMEQCIDnNH34W9M8NCLcXVcMgdIELSIZY762ua2Y8%2FyLoRHXpAiApHpC7aoyMpVKx7W7mCFe3SFQxidlPOLnwNlB%2BAGqfxir%2FAwhJEAAaDDYzNzQyMzE4MzgwNSIMnCVDvhZz%2BmU4YtFeKtwDDC7dkQ1NUEMEnNiUMDg0omHewVgz0x4jH99bUjsBDtg%2Bz%2BhVuoaV%2B7TXRnO0%2BYhDBz3rKjK5WopJh4Wqmt8vk5iWDUP%2BwrAcVxgluTdoxU8ZXk4KtfzmTg77XzFpthWiQIhKjLpEi7E1QOtTP63OI3NGrAgTLn%2BEKKM1vH5NENXG6o5lR1JdFF1m9KAKzP05jPtcWQTpuYYYU2%2FIVZMSBAinHbG6bGJBLIZ5mHa9iBYqdrtYIY4oOxe2QjTL3n%2BsYFOic15fkMm17WkxYGT9bTqjoJwjWBgaz8pd6ipjy0iGa8L8rQ9C0D%2BYlkT2w5BZjRPxIMbkcAT%2FwV3oHjQ5zXfXL19mO6sjMh9UEZPLbm6jOFCHQFq8DsH73b2yQqFq8TNCCskuLboX9HycSULkQO6lXZ8yA2aUXErIZNqYQj5OPXJ7pPJ6w4aC326Y3ioz5hZW1PDnvspKY48IQEaN2dx4hpO%2F0DQDrpg4rMsEzQl08nQ1F0z3rKuN3de2Ldsd3WzDaEiZlkmQyXpjPu5kpAtkGW1U0xOJIlgdC7NQlgTlKtYSA32kR%2F%2FWXwoJPOxF5eSiJ%2FKvDpuXRbuzgozAq5Owqb7JXI39ECNLbTfr2uheB8LySziSxXs0hm4wnp2OvQY6pgHWKDSq5KkgF5%2BSsL0weUm4BKzD2gRwoBajLB7vfSJd5EF45UMTeIisGBButRy87LyXcDGUqWvJNNzLbtP%2B%2BX5MpA8leasQmKwstOcN%2Fp%2BAwJjyyb%2Bvs3uaQ1ndhccA8t2Hqfy52u%2FCIrsyuc4a%2BCTyusV3t3sZOhJC2Naq8lznXXFCDF1vMum%2FlLCkP%2F2%2Ft61EF4JI4bTsY7Dx%2FQywyhXneTOcvbky&X-Amz-Signature=7c3fddb783cf5431f16b39616948de73a1845037cc48a140054cf304737ca9a9&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TVTW3N6P%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJGMEQCIDnNH34W9M8NCLcXVcMgdIELSIZY762ua2Y8%2FyLoRHXpAiApHpC7aoyMpVKx7W7mCFe3SFQxidlPOLnwNlB%2BAGqfxir%2FAwhJEAAaDDYzNzQyMzE4MzgwNSIMnCVDvhZz%2BmU4YtFeKtwDDC7dkQ1NUEMEnNiUMDg0omHewVgz0x4jH99bUjsBDtg%2Bz%2BhVuoaV%2B7TXRnO0%2BYhDBz3rKjK5WopJh4Wqmt8vk5iWDUP%2BwrAcVxgluTdoxU8ZXk4KtfzmTg77XzFpthWiQIhKjLpEi7E1QOtTP63OI3NGrAgTLn%2BEKKM1vH5NENXG6o5lR1JdFF1m9KAKzP05jPtcWQTpuYYYU2%2FIVZMSBAinHbG6bGJBLIZ5mHa9iBYqdrtYIY4oOxe2QjTL3n%2BsYFOic15fkMm17WkxYGT9bTqjoJwjWBgaz8pd6ipjy0iGa8L8rQ9C0D%2BYlkT2w5BZjRPxIMbkcAT%2FwV3oHjQ5zXfXL19mO6sjMh9UEZPLbm6jOFCHQFq8DsH73b2yQqFq8TNCCskuLboX9HycSULkQO6lXZ8yA2aUXErIZNqYQj5OPXJ7pPJ6w4aC326Y3ioz5hZW1PDnvspKY48IQEaN2dx4hpO%2F0DQDrpg4rMsEzQl08nQ1F0z3rKuN3de2Ldsd3WzDaEiZlkmQyXpjPu5kpAtkGW1U0xOJIlgdC7NQlgTlKtYSA32kR%2F%2FWXwoJPOxF5eSiJ%2FKvDpuXRbuzgozAq5Owqb7JXI39ECNLbTfr2uheB8LySziSxXs0hm4wnp2OvQY6pgHWKDSq5KkgF5%2BSsL0weUm4BKzD2gRwoBajLB7vfSJd5EF45UMTeIisGBButRy87LyXcDGUqWvJNNzLbtP%2B%2BX5MpA8leasQmKwstOcN%2Fp%2BAwJjyyb%2Bvs3uaQ1ndhccA8t2Hqfy52u%2FCIrsyuc4a%2BCTyusV3t3sZOhJC2Naq8lznXXFCDF1vMum%2FlLCkP%2F2%2Ft61EF4JI4bTsY7Dx%2FQywyhXneTOcvbky&X-Amz-Signature=d9f0524c7033374e43b7ee148fdea5901e7212e040db3b7e514d3c44b1c58028&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TVTW3N6P%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJGMEQCIDnNH34W9M8NCLcXVcMgdIELSIZY762ua2Y8%2FyLoRHXpAiApHpC7aoyMpVKx7W7mCFe3SFQxidlPOLnwNlB%2BAGqfxir%2FAwhJEAAaDDYzNzQyMzE4MzgwNSIMnCVDvhZz%2BmU4YtFeKtwDDC7dkQ1NUEMEnNiUMDg0omHewVgz0x4jH99bUjsBDtg%2Bz%2BhVuoaV%2B7TXRnO0%2BYhDBz3rKjK5WopJh4Wqmt8vk5iWDUP%2BwrAcVxgluTdoxU8ZXk4KtfzmTg77XzFpthWiQIhKjLpEi7E1QOtTP63OI3NGrAgTLn%2BEKKM1vH5NENXG6o5lR1JdFF1m9KAKzP05jPtcWQTpuYYYU2%2FIVZMSBAinHbG6bGJBLIZ5mHa9iBYqdrtYIY4oOxe2QjTL3n%2BsYFOic15fkMm17WkxYGT9bTqjoJwjWBgaz8pd6ipjy0iGa8L8rQ9C0D%2BYlkT2w5BZjRPxIMbkcAT%2FwV3oHjQ5zXfXL19mO6sjMh9UEZPLbm6jOFCHQFq8DsH73b2yQqFq8TNCCskuLboX9HycSULkQO6lXZ8yA2aUXErIZNqYQj5OPXJ7pPJ6w4aC326Y3ioz5hZW1PDnvspKY48IQEaN2dx4hpO%2F0DQDrpg4rMsEzQl08nQ1F0z3rKuN3de2Ldsd3WzDaEiZlkmQyXpjPu5kpAtkGW1U0xOJIlgdC7NQlgTlKtYSA32kR%2F%2FWXwoJPOxF5eSiJ%2FKvDpuXRbuzgozAq5Owqb7JXI39ECNLbTfr2uheB8LySziSxXs0hm4wnp2OvQY6pgHWKDSq5KkgF5%2BSsL0weUm4BKzD2gRwoBajLB7vfSJd5EF45UMTeIisGBButRy87LyXcDGUqWvJNNzLbtP%2B%2BX5MpA8leasQmKwstOcN%2Fp%2BAwJjyyb%2Bvs3uaQ1ndhccA8t2Hqfy52u%2FCIrsyuc4a%2BCTyusV3t3sZOhJC2Naq8lznXXFCDF1vMum%2FlLCkP%2F2%2Ft61EF4JI4bTsY7Dx%2FQywyhXneTOcvbky&X-Amz-Signature=f8bac966c4c37ad2aa28288c0902e627eced5d55a05aa3a4e3ef0ff4d599cfa4&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TVTW3N6P%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJGMEQCIDnNH34W9M8NCLcXVcMgdIELSIZY762ua2Y8%2FyLoRHXpAiApHpC7aoyMpVKx7W7mCFe3SFQxidlPOLnwNlB%2BAGqfxir%2FAwhJEAAaDDYzNzQyMzE4MzgwNSIMnCVDvhZz%2BmU4YtFeKtwDDC7dkQ1NUEMEnNiUMDg0omHewVgz0x4jH99bUjsBDtg%2Bz%2BhVuoaV%2B7TXRnO0%2BYhDBz3rKjK5WopJh4Wqmt8vk5iWDUP%2BwrAcVxgluTdoxU8ZXk4KtfzmTg77XzFpthWiQIhKjLpEi7E1QOtTP63OI3NGrAgTLn%2BEKKM1vH5NENXG6o5lR1JdFF1m9KAKzP05jPtcWQTpuYYYU2%2FIVZMSBAinHbG6bGJBLIZ5mHa9iBYqdrtYIY4oOxe2QjTL3n%2BsYFOic15fkMm17WkxYGT9bTqjoJwjWBgaz8pd6ipjy0iGa8L8rQ9C0D%2BYlkT2w5BZjRPxIMbkcAT%2FwV3oHjQ5zXfXL19mO6sjMh9UEZPLbm6jOFCHQFq8DsH73b2yQqFq8TNCCskuLboX9HycSULkQO6lXZ8yA2aUXErIZNqYQj5OPXJ7pPJ6w4aC326Y3ioz5hZW1PDnvspKY48IQEaN2dx4hpO%2F0DQDrpg4rMsEzQl08nQ1F0z3rKuN3de2Ldsd3WzDaEiZlkmQyXpjPu5kpAtkGW1U0xOJIlgdC7NQlgTlKtYSA32kR%2F%2FWXwoJPOxF5eSiJ%2FKvDpuXRbuzgozAq5Owqb7JXI39ECNLbTfr2uheB8LySziSxXs0hm4wnp2OvQY6pgHWKDSq5KkgF5%2BSsL0weUm4BKzD2gRwoBajLB7vfSJd5EF45UMTeIisGBButRy87LyXcDGUqWvJNNzLbtP%2B%2BX5MpA8leasQmKwstOcN%2Fp%2BAwJjyyb%2Bvs3uaQ1ndhccA8t2Hqfy52u%2FCIrsyuc4a%2BCTyusV3t3sZOhJC2Naq8lznXXFCDF1vMum%2FlLCkP%2F2%2Ft61EF4JI4bTsY7Dx%2FQywyhXneTOcvbky&X-Amz-Signature=6180afbd4e88f7e9aa9b64d3c58e655a7e4c7445b6dd5a5977a41859b45bbf0b&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TVTW3N6P%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJGMEQCIDnNH34W9M8NCLcXVcMgdIELSIZY762ua2Y8%2FyLoRHXpAiApHpC7aoyMpVKx7W7mCFe3SFQxidlPOLnwNlB%2BAGqfxir%2FAwhJEAAaDDYzNzQyMzE4MzgwNSIMnCVDvhZz%2BmU4YtFeKtwDDC7dkQ1NUEMEnNiUMDg0omHewVgz0x4jH99bUjsBDtg%2Bz%2BhVuoaV%2B7TXRnO0%2BYhDBz3rKjK5WopJh4Wqmt8vk5iWDUP%2BwrAcVxgluTdoxU8ZXk4KtfzmTg77XzFpthWiQIhKjLpEi7E1QOtTP63OI3NGrAgTLn%2BEKKM1vH5NENXG6o5lR1JdFF1m9KAKzP05jPtcWQTpuYYYU2%2FIVZMSBAinHbG6bGJBLIZ5mHa9iBYqdrtYIY4oOxe2QjTL3n%2BsYFOic15fkMm17WkxYGT9bTqjoJwjWBgaz8pd6ipjy0iGa8L8rQ9C0D%2BYlkT2w5BZjRPxIMbkcAT%2FwV3oHjQ5zXfXL19mO6sjMh9UEZPLbm6jOFCHQFq8DsH73b2yQqFq8TNCCskuLboX9HycSULkQO6lXZ8yA2aUXErIZNqYQj5OPXJ7pPJ6w4aC326Y3ioz5hZW1PDnvspKY48IQEaN2dx4hpO%2F0DQDrpg4rMsEzQl08nQ1F0z3rKuN3de2Ldsd3WzDaEiZlkmQyXpjPu5kpAtkGW1U0xOJIlgdC7NQlgTlKtYSA32kR%2F%2FWXwoJPOxF5eSiJ%2FKvDpuXRbuzgozAq5Owqb7JXI39ECNLbTfr2uheB8LySziSxXs0hm4wnp2OvQY6pgHWKDSq5KkgF5%2BSsL0weUm4BKzD2gRwoBajLB7vfSJd5EF45UMTeIisGBButRy87LyXcDGUqWvJNNzLbtP%2B%2BX5MpA8leasQmKwstOcN%2Fp%2BAwJjyyb%2Bvs3uaQ1ndhccA8t2Hqfy52u%2FCIrsyuc4a%2BCTyusV3t3sZOhJC2Naq8lznXXFCDF1vMum%2FlLCkP%2F2%2Ft61EF4JI4bTsY7Dx%2FQywyhXneTOcvbky&X-Amz-Signature=252196ad8d9c64c42214b235e1a30976a984ebc766e2b8892ecb83b5d79181fe&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TVTW3N6P%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJGMEQCIDnNH34W9M8NCLcXVcMgdIELSIZY762ua2Y8%2FyLoRHXpAiApHpC7aoyMpVKx7W7mCFe3SFQxidlPOLnwNlB%2BAGqfxir%2FAwhJEAAaDDYzNzQyMzE4MzgwNSIMnCVDvhZz%2BmU4YtFeKtwDDC7dkQ1NUEMEnNiUMDg0omHewVgz0x4jH99bUjsBDtg%2Bz%2BhVuoaV%2B7TXRnO0%2BYhDBz3rKjK5WopJh4Wqmt8vk5iWDUP%2BwrAcVxgluTdoxU8ZXk4KtfzmTg77XzFpthWiQIhKjLpEi7E1QOtTP63OI3NGrAgTLn%2BEKKM1vH5NENXG6o5lR1JdFF1m9KAKzP05jPtcWQTpuYYYU2%2FIVZMSBAinHbG6bGJBLIZ5mHa9iBYqdrtYIY4oOxe2QjTL3n%2BsYFOic15fkMm17WkxYGT9bTqjoJwjWBgaz8pd6ipjy0iGa8L8rQ9C0D%2BYlkT2w5BZjRPxIMbkcAT%2FwV3oHjQ5zXfXL19mO6sjMh9UEZPLbm6jOFCHQFq8DsH73b2yQqFq8TNCCskuLboX9HycSULkQO6lXZ8yA2aUXErIZNqYQj5OPXJ7pPJ6w4aC326Y3ioz5hZW1PDnvspKY48IQEaN2dx4hpO%2F0DQDrpg4rMsEzQl08nQ1F0z3rKuN3de2Ldsd3WzDaEiZlkmQyXpjPu5kpAtkGW1U0xOJIlgdC7NQlgTlKtYSA32kR%2F%2FWXwoJPOxF5eSiJ%2FKvDpuXRbuzgozAq5Owqb7JXI39ECNLbTfr2uheB8LySziSxXs0hm4wnp2OvQY6pgHWKDSq5KkgF5%2BSsL0weUm4BKzD2gRwoBajLB7vfSJd5EF45UMTeIisGBButRy87LyXcDGUqWvJNNzLbtP%2B%2BX5MpA8leasQmKwstOcN%2Fp%2BAwJjyyb%2Bvs3uaQ1ndhccA8t2Hqfy52u%2FCIrsyuc4a%2BCTyusV3t3sZOhJC2Naq8lznXXFCDF1vMum%2FlLCkP%2F2%2Ft61EF4JI4bTsY7Dx%2FQywyhXneTOcvbky&X-Amz-Signature=60cd641fe27b37b13f7020ab846f6a22c6be0d92b851dda5a944d3b88be7955b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TVTW3N6P%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJGMEQCIDnNH34W9M8NCLcXVcMgdIELSIZY762ua2Y8%2FyLoRHXpAiApHpC7aoyMpVKx7W7mCFe3SFQxidlPOLnwNlB%2BAGqfxir%2FAwhJEAAaDDYzNzQyMzE4MzgwNSIMnCVDvhZz%2BmU4YtFeKtwDDC7dkQ1NUEMEnNiUMDg0omHewVgz0x4jH99bUjsBDtg%2Bz%2BhVuoaV%2B7TXRnO0%2BYhDBz3rKjK5WopJh4Wqmt8vk5iWDUP%2BwrAcVxgluTdoxU8ZXk4KtfzmTg77XzFpthWiQIhKjLpEi7E1QOtTP63OI3NGrAgTLn%2BEKKM1vH5NENXG6o5lR1JdFF1m9KAKzP05jPtcWQTpuYYYU2%2FIVZMSBAinHbG6bGJBLIZ5mHa9iBYqdrtYIY4oOxe2QjTL3n%2BsYFOic15fkMm17WkxYGT9bTqjoJwjWBgaz8pd6ipjy0iGa8L8rQ9C0D%2BYlkT2w5BZjRPxIMbkcAT%2FwV3oHjQ5zXfXL19mO6sjMh9UEZPLbm6jOFCHQFq8DsH73b2yQqFq8TNCCskuLboX9HycSULkQO6lXZ8yA2aUXErIZNqYQj5OPXJ7pPJ6w4aC326Y3ioz5hZW1PDnvspKY48IQEaN2dx4hpO%2F0DQDrpg4rMsEzQl08nQ1F0z3rKuN3de2Ldsd3WzDaEiZlkmQyXpjPu5kpAtkGW1U0xOJIlgdC7NQlgTlKtYSA32kR%2F%2FWXwoJPOxF5eSiJ%2FKvDpuXRbuzgozAq5Owqb7JXI39ECNLbTfr2uheB8LySziSxXs0hm4wnp2OvQY6pgHWKDSq5KkgF5%2BSsL0weUm4BKzD2gRwoBajLB7vfSJd5EF45UMTeIisGBButRy87LyXcDGUqWvJNNzLbtP%2B%2BX5MpA8leasQmKwstOcN%2Fp%2BAwJjyyb%2Bvs3uaQ1ndhccA8t2Hqfy52u%2FCIrsyuc4a%2BCTyusV3t3sZOhJC2Naq8lznXXFCDF1vMum%2FlLCkP%2F2%2Ft61EF4JI4bTsY7Dx%2FQywyhXneTOcvbky&X-Amz-Signature=0efb1d565c035ed3261785cb90e4eb3e8077de352aa531340a2c784724c50ebb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TVTW3N6P%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJGMEQCIDnNH34W9M8NCLcXVcMgdIELSIZY762ua2Y8%2FyLoRHXpAiApHpC7aoyMpVKx7W7mCFe3SFQxidlPOLnwNlB%2BAGqfxir%2FAwhJEAAaDDYzNzQyMzE4MzgwNSIMnCVDvhZz%2BmU4YtFeKtwDDC7dkQ1NUEMEnNiUMDg0omHewVgz0x4jH99bUjsBDtg%2Bz%2BhVuoaV%2B7TXRnO0%2BYhDBz3rKjK5WopJh4Wqmt8vk5iWDUP%2BwrAcVxgluTdoxU8ZXk4KtfzmTg77XzFpthWiQIhKjLpEi7E1QOtTP63OI3NGrAgTLn%2BEKKM1vH5NENXG6o5lR1JdFF1m9KAKzP05jPtcWQTpuYYYU2%2FIVZMSBAinHbG6bGJBLIZ5mHa9iBYqdrtYIY4oOxe2QjTL3n%2BsYFOic15fkMm17WkxYGT9bTqjoJwjWBgaz8pd6ipjy0iGa8L8rQ9C0D%2BYlkT2w5BZjRPxIMbkcAT%2FwV3oHjQ5zXfXL19mO6sjMh9UEZPLbm6jOFCHQFq8DsH73b2yQqFq8TNCCskuLboX9HycSULkQO6lXZ8yA2aUXErIZNqYQj5OPXJ7pPJ6w4aC326Y3ioz5hZW1PDnvspKY48IQEaN2dx4hpO%2F0DQDrpg4rMsEzQl08nQ1F0z3rKuN3de2Ldsd3WzDaEiZlkmQyXpjPu5kpAtkGW1U0xOJIlgdC7NQlgTlKtYSA32kR%2F%2FWXwoJPOxF5eSiJ%2FKvDpuXRbuzgozAq5Owqb7JXI39ECNLbTfr2uheB8LySziSxXs0hm4wnp2OvQY6pgHWKDSq5KkgF5%2BSsL0weUm4BKzD2gRwoBajLB7vfSJd5EF45UMTeIisGBButRy87LyXcDGUqWvJNNzLbtP%2B%2BX5MpA8leasQmKwstOcN%2Fp%2BAwJjyyb%2Bvs3uaQ1ndhccA8t2Hqfy52u%2FCIrsyuc4a%2BCTyusV3t3sZOhJC2Naq8lznXXFCDF1vMum%2FlLCkP%2F2%2Ft61EF4JI4bTsY7Dx%2FQywyhXneTOcvbky&X-Amz-Signature=921b2a7561d5d2ee4cc4e21c54c40946023dd9ee3a1cd63fffa3b9da95bbd84d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBNYK4YY%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJGMEQCICvSGofiu70CqiAuxPScmDik8i68O5gl79ORL2gM6n07AiAGBwbTI30R0%2FOVAGp2zEhYNiCeTNeXLu45TaFqi6GG9ir%2FAwhJEAAaDDYzNzQyMzE4MzgwNSIMhnS8ajV8drrINoi4KtwDyyoQxFdrKtgGPw3uTxy1WVMWfYypEeuhNJpb49qkYc3ehcjCaK2uJ47tG6A%2By9SmZqead2KI2fRXD%2F5Og4YRDDcoZoQdNbYs92OdvP5WTY5so6FKHXClpkSlZy%2FAZs0aaa%2FdgSPYEF1rwdvmboVfY3J5j1XbOVbrmEPYv%2FS1%2Fng1leBbRZ0H%2BMtgZ4FKT3Oj3IByu1ccEOw0%2BykD5x%2FsAYiAgR%2By6dvrubEJjLn4gFdRIai2wlMODeNZOH%2FbyhoXQL%2BZh%2B9FoVlfGzKQ%2BhLU0N4dmcw%2FgFZ1DKlwkSvAIH8V48q8KosHYhCS1ItlBrVoZnd2cmw7yavgSRwFdqLzsK7FKY9JEEYV4cZpLjF4GW96eng56K4Da24dAspwiGPfteoDzoVQMsTzn8RMPBHbLoRvxuo97fFsnQOouaVw6t0MeOicvucUCgdiI4mH0VMM9FWaJZIMVuLoV4GIs0%2Be31PfLl0PpsTtR0j8JHrE1b9nvZZhepKLPUsYdOpvBbvyUPA5iLRUYBOpHjQemsFenbjEeAY575dHlm6OzaEN52ZODT05y6a%2BqAHMNc27qBHUAdYOT7BfEFnKUyr8Y5n0%2FTO1%2Fml0lg3JKSyLzH8YqNCAmxKQ9Ku2tNVaYGcwwZ2OvQY6pgEkUFtAbAmiZY6H3anJkrmikWMpWFW6aF7hVWKc8tIZTSbAiI4qHW92GFby9PA6WbUEJ60Wb%2BaymmyQ9V5SdpScFvvOQmsu4OzlCcbZaonDE9SPFQfvM7nzc%2FAeck57AHWkJS48bfjvPlVWNyMLSXXk03q3P%2B8ysmZOG8%2BWzR8Zxg89GftiUh9EWX%2B3yVJzfxVkb21nw7tT4S00qk2r2URb2PVCm5Oo&X-Amz-Signature=de716aca560b6f092bfc6af676e58c66428238e1237906b6c3406bb1d2886f6e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBNYK4YY%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJGMEQCICvSGofiu70CqiAuxPScmDik8i68O5gl79ORL2gM6n07AiAGBwbTI30R0%2FOVAGp2zEhYNiCeTNeXLu45TaFqi6GG9ir%2FAwhJEAAaDDYzNzQyMzE4MzgwNSIMhnS8ajV8drrINoi4KtwDyyoQxFdrKtgGPw3uTxy1WVMWfYypEeuhNJpb49qkYc3ehcjCaK2uJ47tG6A%2By9SmZqead2KI2fRXD%2F5Og4YRDDcoZoQdNbYs92OdvP5WTY5so6FKHXClpkSlZy%2FAZs0aaa%2FdgSPYEF1rwdvmboVfY3J5j1XbOVbrmEPYv%2FS1%2Fng1leBbRZ0H%2BMtgZ4FKT3Oj3IByu1ccEOw0%2BykD5x%2FsAYiAgR%2By6dvrubEJjLn4gFdRIai2wlMODeNZOH%2FbyhoXQL%2BZh%2B9FoVlfGzKQ%2BhLU0N4dmcw%2FgFZ1DKlwkSvAIH8V48q8KosHYhCS1ItlBrVoZnd2cmw7yavgSRwFdqLzsK7FKY9JEEYV4cZpLjF4GW96eng56K4Da24dAspwiGPfteoDzoVQMsTzn8RMPBHbLoRvxuo97fFsnQOouaVw6t0MeOicvucUCgdiI4mH0VMM9FWaJZIMVuLoV4GIs0%2Be31PfLl0PpsTtR0j8JHrE1b9nvZZhepKLPUsYdOpvBbvyUPA5iLRUYBOpHjQemsFenbjEeAY575dHlm6OzaEN52ZODT05y6a%2BqAHMNc27qBHUAdYOT7BfEFnKUyr8Y5n0%2FTO1%2Fml0lg3JKSyLzH8YqNCAmxKQ9Ku2tNVaYGcwwZ2OvQY6pgEkUFtAbAmiZY6H3anJkrmikWMpWFW6aF7hVWKc8tIZTSbAiI4qHW92GFby9PA6WbUEJ60Wb%2BaymmyQ9V5SdpScFvvOQmsu4OzlCcbZaonDE9SPFQfvM7nzc%2FAeck57AHWkJS48bfjvPlVWNyMLSXXk03q3P%2B8ysmZOG8%2BWzR8Zxg89GftiUh9EWX%2B3yVJzfxVkb21nw7tT4S00qk2r2URb2PVCm5Oo&X-Amz-Signature=8a5f97b034a3407e2a9affc4238214ee82480b090fa16d3c5fc2ba7b795868d8&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
