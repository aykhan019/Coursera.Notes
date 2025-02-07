

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S7DUZYHY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIAY%2F1kqum9TS9Yj3oBUvjSTU%2B7mc3BerzQgv0pgWBtKbAiEAg%2BJePHz3ZieKReIVtWJWjzYT03TRmsB64YKcZ6nOHlIq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDPLDBeM2lF%2BpSdxLLCrcA0HxF68h4V22nfVlWQrtTkTQ0tbqkWbBdBzxpUyB9g5gcUZAr939fXdaixpJ0wZY222vfYImVyvpXepxa%2FiNVliMBJhbElpwdZS9ia4ZKZi79mJKZmTns59gonjajrR2UblwnMHwOcb5oUNXWTv6PKIvRyOMRM2uphUZrUQU5EGSvh4t0wXVNNusBMMwu0sVYxiZObPbg5TnCdqbSsxrWIuUSTpPitY33x25jAm7mhlu3N2u%2Fgkct1OcpMb6eyOrXIFHH%2BXclPZMVfGVuqrj4Rs949IKW77xOAQ5qa5mKFDwn5mOGiPGxi7CDwGpcTs4pMcLZs20n9oBGqy7kR3o7wInzj0X8Rj31k4BzjQlpB%2BQnOWYqnMfn%2BxYCxNby%2BWBVKnP4b0v2He2QM6oL%2FhdUpFoW0v6nv2r%2FOPtFG46q%2B5odsjSNp1H4ZpXxjHB7%2BOGWzAGGe3u1guKcC3yUbB2BvSBJtO47PaZQj3gm%2F9qa6iXC8wlTLTYrN8rSk9UfP8HCNafFeFLdNvsTeO%2BpcFvWx3GSTJDxd3RdFzYyUqrjoANMHbdOGJJkaFeUinYBtOwe%2Bc21dHp2CIq5HPd%2FiUUfF9snE9lQpbvvoy2R47Uc%2F9TpmQ5cd1TrkZ%2FAR1kMKn%2Bmb0GOqUBk%2F2UgUeqSVYo5T%2Bd%2FJq%2FldKFvt%2FA9mK1Yxv0ROUZYYImiAOrTuIOaVORS%2FgVDWSRSbolPIyf8iRT%2B7xDPCX1mbZPA2NaDrAACdNsmKeXIPkltAkdAz%2FrURzXPBMgNJpi9CbxITyZb5d9pgPrKkLMfqx4L6djO0DsgY5avRjI8Xf8siZ00%2BAcwcdYfsHfmyCY2YZJQSN4Y0n4XtZpK0X4Epyr2xiu&X-Amz-Signature=7ccb72eb3f31be8dde38b3d8bad8b632641dd4ebbda09ab0ff5560c3740093ba&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S7DUZYHY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIAY%2F1kqum9TS9Yj3oBUvjSTU%2B7mc3BerzQgv0pgWBtKbAiEAg%2BJePHz3ZieKReIVtWJWjzYT03TRmsB64YKcZ6nOHlIq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDPLDBeM2lF%2BpSdxLLCrcA0HxF68h4V22nfVlWQrtTkTQ0tbqkWbBdBzxpUyB9g5gcUZAr939fXdaixpJ0wZY222vfYImVyvpXepxa%2FiNVliMBJhbElpwdZS9ia4ZKZi79mJKZmTns59gonjajrR2UblwnMHwOcb5oUNXWTv6PKIvRyOMRM2uphUZrUQU5EGSvh4t0wXVNNusBMMwu0sVYxiZObPbg5TnCdqbSsxrWIuUSTpPitY33x25jAm7mhlu3N2u%2Fgkct1OcpMb6eyOrXIFHH%2BXclPZMVfGVuqrj4Rs949IKW77xOAQ5qa5mKFDwn5mOGiPGxi7CDwGpcTs4pMcLZs20n9oBGqy7kR3o7wInzj0X8Rj31k4BzjQlpB%2BQnOWYqnMfn%2BxYCxNby%2BWBVKnP4b0v2He2QM6oL%2FhdUpFoW0v6nv2r%2FOPtFG46q%2B5odsjSNp1H4ZpXxjHB7%2BOGWzAGGe3u1guKcC3yUbB2BvSBJtO47PaZQj3gm%2F9qa6iXC8wlTLTYrN8rSk9UfP8HCNafFeFLdNvsTeO%2BpcFvWx3GSTJDxd3RdFzYyUqrjoANMHbdOGJJkaFeUinYBtOwe%2Bc21dHp2CIq5HPd%2FiUUfF9snE9lQpbvvoy2R47Uc%2F9TpmQ5cd1TrkZ%2FAR1kMKn%2Bmb0GOqUBk%2F2UgUeqSVYo5T%2Bd%2FJq%2FldKFvt%2FA9mK1Yxv0ROUZYYImiAOrTuIOaVORS%2FgVDWSRSbolPIyf8iRT%2B7xDPCX1mbZPA2NaDrAACdNsmKeXIPkltAkdAz%2FrURzXPBMgNJpi9CbxITyZb5d9pgPrKkLMfqx4L6djO0DsgY5avRjI8Xf8siZ00%2BAcwcdYfsHfmyCY2YZJQSN4Y0n4XtZpK0X4Epyr2xiu&X-Amz-Signature=cbdd8ec49d2313f1693974d214e4761258d5fd8e5620c123f64dfb76d0250ce1&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S7DUZYHY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIAY%2F1kqum9TS9Yj3oBUvjSTU%2B7mc3BerzQgv0pgWBtKbAiEAg%2BJePHz3ZieKReIVtWJWjzYT03TRmsB64YKcZ6nOHlIq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDPLDBeM2lF%2BpSdxLLCrcA0HxF68h4V22nfVlWQrtTkTQ0tbqkWbBdBzxpUyB9g5gcUZAr939fXdaixpJ0wZY222vfYImVyvpXepxa%2FiNVliMBJhbElpwdZS9ia4ZKZi79mJKZmTns59gonjajrR2UblwnMHwOcb5oUNXWTv6PKIvRyOMRM2uphUZrUQU5EGSvh4t0wXVNNusBMMwu0sVYxiZObPbg5TnCdqbSsxrWIuUSTpPitY33x25jAm7mhlu3N2u%2Fgkct1OcpMb6eyOrXIFHH%2BXclPZMVfGVuqrj4Rs949IKW77xOAQ5qa5mKFDwn5mOGiPGxi7CDwGpcTs4pMcLZs20n9oBGqy7kR3o7wInzj0X8Rj31k4BzjQlpB%2BQnOWYqnMfn%2BxYCxNby%2BWBVKnP4b0v2He2QM6oL%2FhdUpFoW0v6nv2r%2FOPtFG46q%2B5odsjSNp1H4ZpXxjHB7%2BOGWzAGGe3u1guKcC3yUbB2BvSBJtO47PaZQj3gm%2F9qa6iXC8wlTLTYrN8rSk9UfP8HCNafFeFLdNvsTeO%2BpcFvWx3GSTJDxd3RdFzYyUqrjoANMHbdOGJJkaFeUinYBtOwe%2Bc21dHp2CIq5HPd%2FiUUfF9snE9lQpbvvoy2R47Uc%2F9TpmQ5cd1TrkZ%2FAR1kMKn%2Bmb0GOqUBk%2F2UgUeqSVYo5T%2Bd%2FJq%2FldKFvt%2FA9mK1Yxv0ROUZYYImiAOrTuIOaVORS%2FgVDWSRSbolPIyf8iRT%2B7xDPCX1mbZPA2NaDrAACdNsmKeXIPkltAkdAz%2FrURzXPBMgNJpi9CbxITyZb5d9pgPrKkLMfqx4L6djO0DsgY5avRjI8Xf8siZ00%2BAcwcdYfsHfmyCY2YZJQSN4Y0n4XtZpK0X4Epyr2xiu&X-Amz-Signature=eb29ba7b5343d13322828254b77e011eefb51d1b1ec45f2ce63969da9f984d5d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S7DUZYHY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIAY%2F1kqum9TS9Yj3oBUvjSTU%2B7mc3BerzQgv0pgWBtKbAiEAg%2BJePHz3ZieKReIVtWJWjzYT03TRmsB64YKcZ6nOHlIq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDPLDBeM2lF%2BpSdxLLCrcA0HxF68h4V22nfVlWQrtTkTQ0tbqkWbBdBzxpUyB9g5gcUZAr939fXdaixpJ0wZY222vfYImVyvpXepxa%2FiNVliMBJhbElpwdZS9ia4ZKZi79mJKZmTns59gonjajrR2UblwnMHwOcb5oUNXWTv6PKIvRyOMRM2uphUZrUQU5EGSvh4t0wXVNNusBMMwu0sVYxiZObPbg5TnCdqbSsxrWIuUSTpPitY33x25jAm7mhlu3N2u%2Fgkct1OcpMb6eyOrXIFHH%2BXclPZMVfGVuqrj4Rs949IKW77xOAQ5qa5mKFDwn5mOGiPGxi7CDwGpcTs4pMcLZs20n9oBGqy7kR3o7wInzj0X8Rj31k4BzjQlpB%2BQnOWYqnMfn%2BxYCxNby%2BWBVKnP4b0v2He2QM6oL%2FhdUpFoW0v6nv2r%2FOPtFG46q%2B5odsjSNp1H4ZpXxjHB7%2BOGWzAGGe3u1guKcC3yUbB2BvSBJtO47PaZQj3gm%2F9qa6iXC8wlTLTYrN8rSk9UfP8HCNafFeFLdNvsTeO%2BpcFvWx3GSTJDxd3RdFzYyUqrjoANMHbdOGJJkaFeUinYBtOwe%2Bc21dHp2CIq5HPd%2FiUUfF9snE9lQpbvvoy2R47Uc%2F9TpmQ5cd1TrkZ%2FAR1kMKn%2Bmb0GOqUBk%2F2UgUeqSVYo5T%2Bd%2FJq%2FldKFvt%2FA9mK1Yxv0ROUZYYImiAOrTuIOaVORS%2FgVDWSRSbolPIyf8iRT%2B7xDPCX1mbZPA2NaDrAACdNsmKeXIPkltAkdAz%2FrURzXPBMgNJpi9CbxITyZb5d9pgPrKkLMfqx4L6djO0DsgY5avRjI8Xf8siZ00%2BAcwcdYfsHfmyCY2YZJQSN4Y0n4XtZpK0X4Epyr2xiu&X-Amz-Signature=d27629d085ed00edce07b12b4e5317b1ac069bbf9524974ad99483d9eda79176&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S7DUZYHY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIAY%2F1kqum9TS9Yj3oBUvjSTU%2B7mc3BerzQgv0pgWBtKbAiEAg%2BJePHz3ZieKReIVtWJWjzYT03TRmsB64YKcZ6nOHlIq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDPLDBeM2lF%2BpSdxLLCrcA0HxF68h4V22nfVlWQrtTkTQ0tbqkWbBdBzxpUyB9g5gcUZAr939fXdaixpJ0wZY222vfYImVyvpXepxa%2FiNVliMBJhbElpwdZS9ia4ZKZi79mJKZmTns59gonjajrR2UblwnMHwOcb5oUNXWTv6PKIvRyOMRM2uphUZrUQU5EGSvh4t0wXVNNusBMMwu0sVYxiZObPbg5TnCdqbSsxrWIuUSTpPitY33x25jAm7mhlu3N2u%2Fgkct1OcpMb6eyOrXIFHH%2BXclPZMVfGVuqrj4Rs949IKW77xOAQ5qa5mKFDwn5mOGiPGxi7CDwGpcTs4pMcLZs20n9oBGqy7kR3o7wInzj0X8Rj31k4BzjQlpB%2BQnOWYqnMfn%2BxYCxNby%2BWBVKnP4b0v2He2QM6oL%2FhdUpFoW0v6nv2r%2FOPtFG46q%2B5odsjSNp1H4ZpXxjHB7%2BOGWzAGGe3u1guKcC3yUbB2BvSBJtO47PaZQj3gm%2F9qa6iXC8wlTLTYrN8rSk9UfP8HCNafFeFLdNvsTeO%2BpcFvWx3GSTJDxd3RdFzYyUqrjoANMHbdOGJJkaFeUinYBtOwe%2Bc21dHp2CIq5HPd%2FiUUfF9snE9lQpbvvoy2R47Uc%2F9TpmQ5cd1TrkZ%2FAR1kMKn%2Bmb0GOqUBk%2F2UgUeqSVYo5T%2Bd%2FJq%2FldKFvt%2FA9mK1Yxv0ROUZYYImiAOrTuIOaVORS%2FgVDWSRSbolPIyf8iRT%2B7xDPCX1mbZPA2NaDrAACdNsmKeXIPkltAkdAz%2FrURzXPBMgNJpi9CbxITyZb5d9pgPrKkLMfqx4L6djO0DsgY5avRjI8Xf8siZ00%2BAcwcdYfsHfmyCY2YZJQSN4Y0n4XtZpK0X4Epyr2xiu&X-Amz-Signature=8ce78cbc83e3ab719718213f375123a7e83d121d88a3ce402725f4c4f0c7914a&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S7DUZYHY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIAY%2F1kqum9TS9Yj3oBUvjSTU%2B7mc3BerzQgv0pgWBtKbAiEAg%2BJePHz3ZieKReIVtWJWjzYT03TRmsB64YKcZ6nOHlIq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDPLDBeM2lF%2BpSdxLLCrcA0HxF68h4V22nfVlWQrtTkTQ0tbqkWbBdBzxpUyB9g5gcUZAr939fXdaixpJ0wZY222vfYImVyvpXepxa%2FiNVliMBJhbElpwdZS9ia4ZKZi79mJKZmTns59gonjajrR2UblwnMHwOcb5oUNXWTv6PKIvRyOMRM2uphUZrUQU5EGSvh4t0wXVNNusBMMwu0sVYxiZObPbg5TnCdqbSsxrWIuUSTpPitY33x25jAm7mhlu3N2u%2Fgkct1OcpMb6eyOrXIFHH%2BXclPZMVfGVuqrj4Rs949IKW77xOAQ5qa5mKFDwn5mOGiPGxi7CDwGpcTs4pMcLZs20n9oBGqy7kR3o7wInzj0X8Rj31k4BzjQlpB%2BQnOWYqnMfn%2BxYCxNby%2BWBVKnP4b0v2He2QM6oL%2FhdUpFoW0v6nv2r%2FOPtFG46q%2B5odsjSNp1H4ZpXxjHB7%2BOGWzAGGe3u1guKcC3yUbB2BvSBJtO47PaZQj3gm%2F9qa6iXC8wlTLTYrN8rSk9UfP8HCNafFeFLdNvsTeO%2BpcFvWx3GSTJDxd3RdFzYyUqrjoANMHbdOGJJkaFeUinYBtOwe%2Bc21dHp2CIq5HPd%2FiUUfF9snE9lQpbvvoy2R47Uc%2F9TpmQ5cd1TrkZ%2FAR1kMKn%2Bmb0GOqUBk%2F2UgUeqSVYo5T%2Bd%2FJq%2FldKFvt%2FA9mK1Yxv0ROUZYYImiAOrTuIOaVORS%2FgVDWSRSbolPIyf8iRT%2B7xDPCX1mbZPA2NaDrAACdNsmKeXIPkltAkdAz%2FrURzXPBMgNJpi9CbxITyZb5d9pgPrKkLMfqx4L6djO0DsgY5avRjI8Xf8siZ00%2BAcwcdYfsHfmyCY2YZJQSN4Y0n4XtZpK0X4Epyr2xiu&X-Amz-Signature=3b1de0896b2ca78e994e3304b9976ff769e018d66f1413a42f388642eda1bb68&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S7DUZYHY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIAY%2F1kqum9TS9Yj3oBUvjSTU%2B7mc3BerzQgv0pgWBtKbAiEAg%2BJePHz3ZieKReIVtWJWjzYT03TRmsB64YKcZ6nOHlIq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDPLDBeM2lF%2BpSdxLLCrcA0HxF68h4V22nfVlWQrtTkTQ0tbqkWbBdBzxpUyB9g5gcUZAr939fXdaixpJ0wZY222vfYImVyvpXepxa%2FiNVliMBJhbElpwdZS9ia4ZKZi79mJKZmTns59gonjajrR2UblwnMHwOcb5oUNXWTv6PKIvRyOMRM2uphUZrUQU5EGSvh4t0wXVNNusBMMwu0sVYxiZObPbg5TnCdqbSsxrWIuUSTpPitY33x25jAm7mhlu3N2u%2Fgkct1OcpMb6eyOrXIFHH%2BXclPZMVfGVuqrj4Rs949IKW77xOAQ5qa5mKFDwn5mOGiPGxi7CDwGpcTs4pMcLZs20n9oBGqy7kR3o7wInzj0X8Rj31k4BzjQlpB%2BQnOWYqnMfn%2BxYCxNby%2BWBVKnP4b0v2He2QM6oL%2FhdUpFoW0v6nv2r%2FOPtFG46q%2B5odsjSNp1H4ZpXxjHB7%2BOGWzAGGe3u1guKcC3yUbB2BvSBJtO47PaZQj3gm%2F9qa6iXC8wlTLTYrN8rSk9UfP8HCNafFeFLdNvsTeO%2BpcFvWx3GSTJDxd3RdFzYyUqrjoANMHbdOGJJkaFeUinYBtOwe%2Bc21dHp2CIq5HPd%2FiUUfF9snE9lQpbvvoy2R47Uc%2F9TpmQ5cd1TrkZ%2FAR1kMKn%2Bmb0GOqUBk%2F2UgUeqSVYo5T%2Bd%2FJq%2FldKFvt%2FA9mK1Yxv0ROUZYYImiAOrTuIOaVORS%2FgVDWSRSbolPIyf8iRT%2B7xDPCX1mbZPA2NaDrAACdNsmKeXIPkltAkdAz%2FrURzXPBMgNJpi9CbxITyZb5d9pgPrKkLMfqx4L6djO0DsgY5avRjI8Xf8siZ00%2BAcwcdYfsHfmyCY2YZJQSN4Y0n4XtZpK0X4Epyr2xiu&X-Amz-Signature=3bd41ebdca84b4d87e5aa33e6c7e13f15fbd1b6708beeebfdc5df5d8b740fe79&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S7DUZYHY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIAY%2F1kqum9TS9Yj3oBUvjSTU%2B7mc3BerzQgv0pgWBtKbAiEAg%2BJePHz3ZieKReIVtWJWjzYT03TRmsB64YKcZ6nOHlIq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDPLDBeM2lF%2BpSdxLLCrcA0HxF68h4V22nfVlWQrtTkTQ0tbqkWbBdBzxpUyB9g5gcUZAr939fXdaixpJ0wZY222vfYImVyvpXepxa%2FiNVliMBJhbElpwdZS9ia4ZKZi79mJKZmTns59gonjajrR2UblwnMHwOcb5oUNXWTv6PKIvRyOMRM2uphUZrUQU5EGSvh4t0wXVNNusBMMwu0sVYxiZObPbg5TnCdqbSsxrWIuUSTpPitY33x25jAm7mhlu3N2u%2Fgkct1OcpMb6eyOrXIFHH%2BXclPZMVfGVuqrj4Rs949IKW77xOAQ5qa5mKFDwn5mOGiPGxi7CDwGpcTs4pMcLZs20n9oBGqy7kR3o7wInzj0X8Rj31k4BzjQlpB%2BQnOWYqnMfn%2BxYCxNby%2BWBVKnP4b0v2He2QM6oL%2FhdUpFoW0v6nv2r%2FOPtFG46q%2B5odsjSNp1H4ZpXxjHB7%2BOGWzAGGe3u1guKcC3yUbB2BvSBJtO47PaZQj3gm%2F9qa6iXC8wlTLTYrN8rSk9UfP8HCNafFeFLdNvsTeO%2BpcFvWx3GSTJDxd3RdFzYyUqrjoANMHbdOGJJkaFeUinYBtOwe%2Bc21dHp2CIq5HPd%2FiUUfF9snE9lQpbvvoy2R47Uc%2F9TpmQ5cd1TrkZ%2FAR1kMKn%2Bmb0GOqUBk%2F2UgUeqSVYo5T%2Bd%2FJq%2FldKFvt%2FA9mK1Yxv0ROUZYYImiAOrTuIOaVORS%2FgVDWSRSbolPIyf8iRT%2B7xDPCX1mbZPA2NaDrAACdNsmKeXIPkltAkdAz%2FrURzXPBMgNJpi9CbxITyZb5d9pgPrKkLMfqx4L6djO0DsgY5avRjI8Xf8siZ00%2BAcwcdYfsHfmyCY2YZJQSN4Y0n4XtZpK0X4Epyr2xiu&X-Amz-Signature=020f48659bfa749e2495a7fb1db9a0d3ffa42a20aa3bfac427b16635d4b1dd15&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S7DUZYHY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIAY%2F1kqum9TS9Yj3oBUvjSTU%2B7mc3BerzQgv0pgWBtKbAiEAg%2BJePHz3ZieKReIVtWJWjzYT03TRmsB64YKcZ6nOHlIq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDPLDBeM2lF%2BpSdxLLCrcA0HxF68h4V22nfVlWQrtTkTQ0tbqkWbBdBzxpUyB9g5gcUZAr939fXdaixpJ0wZY222vfYImVyvpXepxa%2FiNVliMBJhbElpwdZS9ia4ZKZi79mJKZmTns59gonjajrR2UblwnMHwOcb5oUNXWTv6PKIvRyOMRM2uphUZrUQU5EGSvh4t0wXVNNusBMMwu0sVYxiZObPbg5TnCdqbSsxrWIuUSTpPitY33x25jAm7mhlu3N2u%2Fgkct1OcpMb6eyOrXIFHH%2BXclPZMVfGVuqrj4Rs949IKW77xOAQ5qa5mKFDwn5mOGiPGxi7CDwGpcTs4pMcLZs20n9oBGqy7kR3o7wInzj0X8Rj31k4BzjQlpB%2BQnOWYqnMfn%2BxYCxNby%2BWBVKnP4b0v2He2QM6oL%2FhdUpFoW0v6nv2r%2FOPtFG46q%2B5odsjSNp1H4ZpXxjHB7%2BOGWzAGGe3u1guKcC3yUbB2BvSBJtO47PaZQj3gm%2F9qa6iXC8wlTLTYrN8rSk9UfP8HCNafFeFLdNvsTeO%2BpcFvWx3GSTJDxd3RdFzYyUqrjoANMHbdOGJJkaFeUinYBtOwe%2Bc21dHp2CIq5HPd%2FiUUfF9snE9lQpbvvoy2R47Uc%2F9TpmQ5cd1TrkZ%2FAR1kMKn%2Bmb0GOqUBk%2F2UgUeqSVYo5T%2Bd%2FJq%2FldKFvt%2FA9mK1Yxv0ROUZYYImiAOrTuIOaVORS%2FgVDWSRSbolPIyf8iRT%2B7xDPCX1mbZPA2NaDrAACdNsmKeXIPkltAkdAz%2FrURzXPBMgNJpi9CbxITyZb5d9pgPrKkLMfqx4L6djO0DsgY5avRjI8Xf8siZ00%2BAcwcdYfsHfmyCY2YZJQSN4Y0n4XtZpK0X4Epyr2xiu&X-Amz-Signature=223c0959ca85b7d8c364c66f311439ba68408402948e40d12a69707ad947b15f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663TXBLJAE%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCID0RKNH8y5csHCtdAneKBuQQiGLHGUijrNuFtGhwpP5TAiEAj9NYjAIcc7DBFyR08vsvIeQzNiJi288w0S7AtLMGgjIq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDGMRRP3L7JkALBA60yrcA601fzC3Sx%2FFHlLAptEzYjR7i%2ByXOMIYvylfEzo2n0abuYKZ6WFWt8%2FRln2q44wtXrSrA%2FBDP1CHDfs%2Bx%2FeLbMcEU1JsrYLKfhkZbyD2tMd3e%2FI7x9aTd85%2FPfkzm%2Bqzr6qC39qLHRPooCYR1k2SYu0iF%2BL34%2BIDvBZ2m%2BFeoAxDz08Q2nTwM4%2B6rTsrOLKvBEtiDnqQSonYa4OkyElQiCsOJwczVkWQ6B3I1CXpO%2BwFJmn6b9FsBHqFga1vX%2F1K0acYByk1%2FcOFFUtcJaSfZ9wJeA3Mxgxru3CO7e%2Bq560KQ%2BeS%2F3enYXgkT2umb2QKZOavlbeVNSzjPcFB6cIGofAAbCquykjTil32WuUUVWAdxJEaSHlffYhR4I3nBGuZ8OZVbkEdxAS5M8la%2F8ilPTydIVmHJ9qbHbAbsszpoo6TYjoTaeut4fWzvF%2BVZCyjHBMztg%2FmvXSlTOmInbS9cN20DiZqQXNdtFXryo6I%2Fe1Jm4xab8vJdUZUWT3zI9TK1gbYH0BdeAO50Ud3M8eCb5t0wD%2Fwl%2BAlGh4TKE1HVlBvxukK0gaqyUz6HnOLKwUFl3FV%2FE0eUUzg1lGXeeZY2tgYFg0igjYozJJc7gAOZDmDa8d26Dqv4kp02%2BK%2FMMr%2Bmb0GOqUBEsz7QsBxGoThud75hmOvvflHYHj%2FsP8KQmnE0OMyI4Uxgfz%2F%2FspGF5hVsW4KVOe5DgHL%2F7VOwHe9Z5bVjVUSEckQhdcJdrT17ctcLiTjxxd5xtgZzoYtUs5GJn6gp3h07k9ojbJcMH%2B5Raw5e6ol4P1bU99mOQpsP%2B1E9LE2wmzd0Mt1SacdvllYSdynOSq6xQ4HTiu54muTCJsSGspZJGlSoIEE&X-Amz-Signature=5efb3b07cf0bf750eebb0e45e1364e486cd1371e2a572087984b37c261de57b0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663TXBLJAE%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCID0RKNH8y5csHCtdAneKBuQQiGLHGUijrNuFtGhwpP5TAiEAj9NYjAIcc7DBFyR08vsvIeQzNiJi288w0S7AtLMGgjIq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDGMRRP3L7JkALBA60yrcA601fzC3Sx%2FFHlLAptEzYjR7i%2ByXOMIYvylfEzo2n0abuYKZ6WFWt8%2FRln2q44wtXrSrA%2FBDP1CHDfs%2Bx%2FeLbMcEU1JsrYLKfhkZbyD2tMd3e%2FI7x9aTd85%2FPfkzm%2Bqzr6qC39qLHRPooCYR1k2SYu0iF%2BL34%2BIDvBZ2m%2BFeoAxDz08Q2nTwM4%2B6rTsrOLKvBEtiDnqQSonYa4OkyElQiCsOJwczVkWQ6B3I1CXpO%2BwFJmn6b9FsBHqFga1vX%2F1K0acYByk1%2FcOFFUtcJaSfZ9wJeA3Mxgxru3CO7e%2Bq560KQ%2BeS%2F3enYXgkT2umb2QKZOavlbeVNSzjPcFB6cIGofAAbCquykjTil32WuUUVWAdxJEaSHlffYhR4I3nBGuZ8OZVbkEdxAS5M8la%2F8ilPTydIVmHJ9qbHbAbsszpoo6TYjoTaeut4fWzvF%2BVZCyjHBMztg%2FmvXSlTOmInbS9cN20DiZqQXNdtFXryo6I%2Fe1Jm4xab8vJdUZUWT3zI9TK1gbYH0BdeAO50Ud3M8eCb5t0wD%2Fwl%2BAlGh4TKE1HVlBvxukK0gaqyUz6HnOLKwUFl3FV%2FE0eUUzg1lGXeeZY2tgYFg0igjYozJJc7gAOZDmDa8d26Dqv4kp02%2BK%2FMMr%2Bmb0GOqUBEsz7QsBxGoThud75hmOvvflHYHj%2FsP8KQmnE0OMyI4Uxgfz%2F%2FspGF5hVsW4KVOe5DgHL%2F7VOwHe9Z5bVjVUSEckQhdcJdrT17ctcLiTjxxd5xtgZzoYtUs5GJn6gp3h07k9ojbJcMH%2B5Raw5e6ol4P1bU99mOQpsP%2B1E9LE2wmzd0Mt1SacdvllYSdynOSq6xQ4HTiu54muTCJsSGspZJGlSoIEE&X-Amz-Signature=0e93cb5c10ca2aa60007e1c43f87c49d51d2b8cc8ac1a0dce0524bae5b67e46d&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
