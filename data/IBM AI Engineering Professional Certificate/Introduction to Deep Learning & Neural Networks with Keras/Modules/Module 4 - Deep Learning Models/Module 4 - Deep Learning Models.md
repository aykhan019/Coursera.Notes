

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VCUF6IUX%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJIMEYCIQCOD%2FKGMCr3TOH3nVB4odjoo4VBBmnGY7x1gdD%2F9qReGQIhAJ%2FT9VUUfWmGzgtRoskz%2FRITFsgS64jtECpviEyT0wNXKv8DCEEQABoMNjM3NDIzMTgzODA1Igy1agWQX47xDwfeLTcq3ANpwH9Mv%2BG%2BsGSzmhik%2By%2BS6sWDwsHm36kqLpLKemhXfhEHWfVMj5GzV8LmZEf%2BYx%2FX9frH0Zs4kC9kANUitegGYztl8PVlwTDoiS%2Bopl%2BTZobr5INIrMsDm2%2FGk85OFjFCehGkK%2BwQxKMxGdo2QmuX2NM9Ejn%2F8%2BwmxpsG6UivHAcwwLJb82k4rJY%2FpG%2F%2FqiSQcbJ0E0haEnX2upAU88OCxRDinZAYe2pJ%2F366UQc3ZXectb6kvkU%2FPzKSekPs6ckFsNgYJdktwsScTNZsckG5DDBmCQuQg5M4Xeb5Gr5IRK5a45GfNRSvOlQlvjFKHtffhqJuEjenxgXjPPpK0FNSzk1jmUnbxHCN8Z%2FIYeaPYK1fM%2BxO%2FIXXrnV6HlOaCUK8NWkc5G%2B5GQ%2FAPCqL9R9zUpoPi%2F3d2TPlLGzm%2FLqdEPHTa5lXKE5bVC215mKFch53mf8ILPRKODBgFMm2d85LKOvN3Bv5bqZv9px3RbxiPp2mWkQF8RPS2TT9PEx10Rjp9asBbeP5Z4WRuT33Kbi8k53dlQqPxxrFDns%2BfCA%2FAkuc1GnLswSX2SI%2FGXVE34m4acjBoN2vIeTQ%2B4ufg5MKd8YaHebt0DCuGdV5ZTqwx97rm1N3XVF33JdcijCas4y9BjqkAblMvli5tBnQELXRJKU%2B7gfhj7y3Mo%2BSRyIjAc8xf8GxKTUOyvd4HjUXTuCYH5s8D7IoA1KnAZwXJcAcb0UBHGbpnHGHGpdOQQm5BHScr5Ara5n9s7zoYi6%2BCeahbNx5vMOnzQcPx9UGmRBOP2TSbG3KVCbHoFJuLAMZ%2F1YOBxYRpfBAgN%2FsSYeK6Af4Tc1kR6%2B0luC8KoFp2aSklh1F232IuPIk&X-Amz-Signature=964b64b906379c754f8a43485226333abf838595bd4a0bdff737bb7f5dafd2d3&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VCUF6IUX%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJIMEYCIQCOD%2FKGMCr3TOH3nVB4odjoo4VBBmnGY7x1gdD%2F9qReGQIhAJ%2FT9VUUfWmGzgtRoskz%2FRITFsgS64jtECpviEyT0wNXKv8DCEEQABoMNjM3NDIzMTgzODA1Igy1agWQX47xDwfeLTcq3ANpwH9Mv%2BG%2BsGSzmhik%2By%2BS6sWDwsHm36kqLpLKemhXfhEHWfVMj5GzV8LmZEf%2BYx%2FX9frH0Zs4kC9kANUitegGYztl8PVlwTDoiS%2Bopl%2BTZobr5INIrMsDm2%2FGk85OFjFCehGkK%2BwQxKMxGdo2QmuX2NM9Ejn%2F8%2BwmxpsG6UivHAcwwLJb82k4rJY%2FpG%2F%2FqiSQcbJ0E0haEnX2upAU88OCxRDinZAYe2pJ%2F366UQc3ZXectb6kvkU%2FPzKSekPs6ckFsNgYJdktwsScTNZsckG5DDBmCQuQg5M4Xeb5Gr5IRK5a45GfNRSvOlQlvjFKHtffhqJuEjenxgXjPPpK0FNSzk1jmUnbxHCN8Z%2FIYeaPYK1fM%2BxO%2FIXXrnV6HlOaCUK8NWkc5G%2B5GQ%2FAPCqL9R9zUpoPi%2F3d2TPlLGzm%2FLqdEPHTa5lXKE5bVC215mKFch53mf8ILPRKODBgFMm2d85LKOvN3Bv5bqZv9px3RbxiPp2mWkQF8RPS2TT9PEx10Rjp9asBbeP5Z4WRuT33Kbi8k53dlQqPxxrFDns%2BfCA%2FAkuc1GnLswSX2SI%2FGXVE34m4acjBoN2vIeTQ%2B4ufg5MKd8YaHebt0DCuGdV5ZTqwx97rm1N3XVF33JdcijCas4y9BjqkAblMvli5tBnQELXRJKU%2B7gfhj7y3Mo%2BSRyIjAc8xf8GxKTUOyvd4HjUXTuCYH5s8D7IoA1KnAZwXJcAcb0UBHGbpnHGHGpdOQQm5BHScr5Ara5n9s7zoYi6%2BCeahbNx5vMOnzQcPx9UGmRBOP2TSbG3KVCbHoFJuLAMZ%2F1YOBxYRpfBAgN%2FsSYeK6Af4Tc1kR6%2B0luC8KoFp2aSklh1F232IuPIk&X-Amz-Signature=a5617e7addbc8094b32d8684aa0aef9a25716d07e9aa6efc4ea425ca938b6c8e&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VCUF6IUX%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJIMEYCIQCOD%2FKGMCr3TOH3nVB4odjoo4VBBmnGY7x1gdD%2F9qReGQIhAJ%2FT9VUUfWmGzgtRoskz%2FRITFsgS64jtECpviEyT0wNXKv8DCEEQABoMNjM3NDIzMTgzODA1Igy1agWQX47xDwfeLTcq3ANpwH9Mv%2BG%2BsGSzmhik%2By%2BS6sWDwsHm36kqLpLKemhXfhEHWfVMj5GzV8LmZEf%2BYx%2FX9frH0Zs4kC9kANUitegGYztl8PVlwTDoiS%2Bopl%2BTZobr5INIrMsDm2%2FGk85OFjFCehGkK%2BwQxKMxGdo2QmuX2NM9Ejn%2F8%2BwmxpsG6UivHAcwwLJb82k4rJY%2FpG%2F%2FqiSQcbJ0E0haEnX2upAU88OCxRDinZAYe2pJ%2F366UQc3ZXectb6kvkU%2FPzKSekPs6ckFsNgYJdktwsScTNZsckG5DDBmCQuQg5M4Xeb5Gr5IRK5a45GfNRSvOlQlvjFKHtffhqJuEjenxgXjPPpK0FNSzk1jmUnbxHCN8Z%2FIYeaPYK1fM%2BxO%2FIXXrnV6HlOaCUK8NWkc5G%2B5GQ%2FAPCqL9R9zUpoPi%2F3d2TPlLGzm%2FLqdEPHTa5lXKE5bVC215mKFch53mf8ILPRKODBgFMm2d85LKOvN3Bv5bqZv9px3RbxiPp2mWkQF8RPS2TT9PEx10Rjp9asBbeP5Z4WRuT33Kbi8k53dlQqPxxrFDns%2BfCA%2FAkuc1GnLswSX2SI%2FGXVE34m4acjBoN2vIeTQ%2B4ufg5MKd8YaHebt0DCuGdV5ZTqwx97rm1N3XVF33JdcijCas4y9BjqkAblMvli5tBnQELXRJKU%2B7gfhj7y3Mo%2BSRyIjAc8xf8GxKTUOyvd4HjUXTuCYH5s8D7IoA1KnAZwXJcAcb0UBHGbpnHGHGpdOQQm5BHScr5Ara5n9s7zoYi6%2BCeahbNx5vMOnzQcPx9UGmRBOP2TSbG3KVCbHoFJuLAMZ%2F1YOBxYRpfBAgN%2FsSYeK6Af4Tc1kR6%2B0luC8KoFp2aSklh1F232IuPIk&X-Amz-Signature=02c5d6d085353ff3b3854911583599462afaa782c9299f6a790c392b448e9430&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VCUF6IUX%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJIMEYCIQCOD%2FKGMCr3TOH3nVB4odjoo4VBBmnGY7x1gdD%2F9qReGQIhAJ%2FT9VUUfWmGzgtRoskz%2FRITFsgS64jtECpviEyT0wNXKv8DCEEQABoMNjM3NDIzMTgzODA1Igy1agWQX47xDwfeLTcq3ANpwH9Mv%2BG%2BsGSzmhik%2By%2BS6sWDwsHm36kqLpLKemhXfhEHWfVMj5GzV8LmZEf%2BYx%2FX9frH0Zs4kC9kANUitegGYztl8PVlwTDoiS%2Bopl%2BTZobr5INIrMsDm2%2FGk85OFjFCehGkK%2BwQxKMxGdo2QmuX2NM9Ejn%2F8%2BwmxpsG6UivHAcwwLJb82k4rJY%2FpG%2F%2FqiSQcbJ0E0haEnX2upAU88OCxRDinZAYe2pJ%2F366UQc3ZXectb6kvkU%2FPzKSekPs6ckFsNgYJdktwsScTNZsckG5DDBmCQuQg5M4Xeb5Gr5IRK5a45GfNRSvOlQlvjFKHtffhqJuEjenxgXjPPpK0FNSzk1jmUnbxHCN8Z%2FIYeaPYK1fM%2BxO%2FIXXrnV6HlOaCUK8NWkc5G%2B5GQ%2FAPCqL9R9zUpoPi%2F3d2TPlLGzm%2FLqdEPHTa5lXKE5bVC215mKFch53mf8ILPRKODBgFMm2d85LKOvN3Bv5bqZv9px3RbxiPp2mWkQF8RPS2TT9PEx10Rjp9asBbeP5Z4WRuT33Kbi8k53dlQqPxxrFDns%2BfCA%2FAkuc1GnLswSX2SI%2FGXVE34m4acjBoN2vIeTQ%2B4ufg5MKd8YaHebt0DCuGdV5ZTqwx97rm1N3XVF33JdcijCas4y9BjqkAblMvli5tBnQELXRJKU%2B7gfhj7y3Mo%2BSRyIjAc8xf8GxKTUOyvd4HjUXTuCYH5s8D7IoA1KnAZwXJcAcb0UBHGbpnHGHGpdOQQm5BHScr5Ara5n9s7zoYi6%2BCeahbNx5vMOnzQcPx9UGmRBOP2TSbG3KVCbHoFJuLAMZ%2F1YOBxYRpfBAgN%2FsSYeK6Af4Tc1kR6%2B0luC8KoFp2aSklh1F232IuPIk&X-Amz-Signature=06ba7d6810a33cf8c5ae5823289b0b5198a412f7c3127daa96f531954106fa07&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VCUF6IUX%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJIMEYCIQCOD%2FKGMCr3TOH3nVB4odjoo4VBBmnGY7x1gdD%2F9qReGQIhAJ%2FT9VUUfWmGzgtRoskz%2FRITFsgS64jtECpviEyT0wNXKv8DCEEQABoMNjM3NDIzMTgzODA1Igy1agWQX47xDwfeLTcq3ANpwH9Mv%2BG%2BsGSzmhik%2By%2BS6sWDwsHm36kqLpLKemhXfhEHWfVMj5GzV8LmZEf%2BYx%2FX9frH0Zs4kC9kANUitegGYztl8PVlwTDoiS%2Bopl%2BTZobr5INIrMsDm2%2FGk85OFjFCehGkK%2BwQxKMxGdo2QmuX2NM9Ejn%2F8%2BwmxpsG6UivHAcwwLJb82k4rJY%2FpG%2F%2FqiSQcbJ0E0haEnX2upAU88OCxRDinZAYe2pJ%2F366UQc3ZXectb6kvkU%2FPzKSekPs6ckFsNgYJdktwsScTNZsckG5DDBmCQuQg5M4Xeb5Gr5IRK5a45GfNRSvOlQlvjFKHtffhqJuEjenxgXjPPpK0FNSzk1jmUnbxHCN8Z%2FIYeaPYK1fM%2BxO%2FIXXrnV6HlOaCUK8NWkc5G%2B5GQ%2FAPCqL9R9zUpoPi%2F3d2TPlLGzm%2FLqdEPHTa5lXKE5bVC215mKFch53mf8ILPRKODBgFMm2d85LKOvN3Bv5bqZv9px3RbxiPp2mWkQF8RPS2TT9PEx10Rjp9asBbeP5Z4WRuT33Kbi8k53dlQqPxxrFDns%2BfCA%2FAkuc1GnLswSX2SI%2FGXVE34m4acjBoN2vIeTQ%2B4ufg5MKd8YaHebt0DCuGdV5ZTqwx97rm1N3XVF33JdcijCas4y9BjqkAblMvli5tBnQELXRJKU%2B7gfhj7y3Mo%2BSRyIjAc8xf8GxKTUOyvd4HjUXTuCYH5s8D7IoA1KnAZwXJcAcb0UBHGbpnHGHGpdOQQm5BHScr5Ara5n9s7zoYi6%2BCeahbNx5vMOnzQcPx9UGmRBOP2TSbG3KVCbHoFJuLAMZ%2F1YOBxYRpfBAgN%2FsSYeK6Af4Tc1kR6%2B0luC8KoFp2aSklh1F232IuPIk&X-Amz-Signature=147e1ce96f981b2ff56a696e17773ed2c7bc47927bb7af034b50987bde496cd8&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VCUF6IUX%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJIMEYCIQCOD%2FKGMCr3TOH3nVB4odjoo4VBBmnGY7x1gdD%2F9qReGQIhAJ%2FT9VUUfWmGzgtRoskz%2FRITFsgS64jtECpviEyT0wNXKv8DCEEQABoMNjM3NDIzMTgzODA1Igy1agWQX47xDwfeLTcq3ANpwH9Mv%2BG%2BsGSzmhik%2By%2BS6sWDwsHm36kqLpLKemhXfhEHWfVMj5GzV8LmZEf%2BYx%2FX9frH0Zs4kC9kANUitegGYztl8PVlwTDoiS%2Bopl%2BTZobr5INIrMsDm2%2FGk85OFjFCehGkK%2BwQxKMxGdo2QmuX2NM9Ejn%2F8%2BwmxpsG6UivHAcwwLJb82k4rJY%2FpG%2F%2FqiSQcbJ0E0haEnX2upAU88OCxRDinZAYe2pJ%2F366UQc3ZXectb6kvkU%2FPzKSekPs6ckFsNgYJdktwsScTNZsckG5DDBmCQuQg5M4Xeb5Gr5IRK5a45GfNRSvOlQlvjFKHtffhqJuEjenxgXjPPpK0FNSzk1jmUnbxHCN8Z%2FIYeaPYK1fM%2BxO%2FIXXrnV6HlOaCUK8NWkc5G%2B5GQ%2FAPCqL9R9zUpoPi%2F3d2TPlLGzm%2FLqdEPHTa5lXKE5bVC215mKFch53mf8ILPRKODBgFMm2d85LKOvN3Bv5bqZv9px3RbxiPp2mWkQF8RPS2TT9PEx10Rjp9asBbeP5Z4WRuT33Kbi8k53dlQqPxxrFDns%2BfCA%2FAkuc1GnLswSX2SI%2FGXVE34m4acjBoN2vIeTQ%2B4ufg5MKd8YaHebt0DCuGdV5ZTqwx97rm1N3XVF33JdcijCas4y9BjqkAblMvli5tBnQELXRJKU%2B7gfhj7y3Mo%2BSRyIjAc8xf8GxKTUOyvd4HjUXTuCYH5s8D7IoA1KnAZwXJcAcb0UBHGbpnHGHGpdOQQm5BHScr5Ara5n9s7zoYi6%2BCeahbNx5vMOnzQcPx9UGmRBOP2TSbG3KVCbHoFJuLAMZ%2F1YOBxYRpfBAgN%2FsSYeK6Af4Tc1kR6%2B0luC8KoFp2aSklh1F232IuPIk&X-Amz-Signature=5f0bc15b55878c0bd5d50ae67ce07204cd5a758f56f754b2ec1e5f1641798d3f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VCUF6IUX%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJIMEYCIQCOD%2FKGMCr3TOH3nVB4odjoo4VBBmnGY7x1gdD%2F9qReGQIhAJ%2FT9VUUfWmGzgtRoskz%2FRITFsgS64jtECpviEyT0wNXKv8DCEEQABoMNjM3NDIzMTgzODA1Igy1agWQX47xDwfeLTcq3ANpwH9Mv%2BG%2BsGSzmhik%2By%2BS6sWDwsHm36kqLpLKemhXfhEHWfVMj5GzV8LmZEf%2BYx%2FX9frH0Zs4kC9kANUitegGYztl8PVlwTDoiS%2Bopl%2BTZobr5INIrMsDm2%2FGk85OFjFCehGkK%2BwQxKMxGdo2QmuX2NM9Ejn%2F8%2BwmxpsG6UivHAcwwLJb82k4rJY%2FpG%2F%2FqiSQcbJ0E0haEnX2upAU88OCxRDinZAYe2pJ%2F366UQc3ZXectb6kvkU%2FPzKSekPs6ckFsNgYJdktwsScTNZsckG5DDBmCQuQg5M4Xeb5Gr5IRK5a45GfNRSvOlQlvjFKHtffhqJuEjenxgXjPPpK0FNSzk1jmUnbxHCN8Z%2FIYeaPYK1fM%2BxO%2FIXXrnV6HlOaCUK8NWkc5G%2B5GQ%2FAPCqL9R9zUpoPi%2F3d2TPlLGzm%2FLqdEPHTa5lXKE5bVC215mKFch53mf8ILPRKODBgFMm2d85LKOvN3Bv5bqZv9px3RbxiPp2mWkQF8RPS2TT9PEx10Rjp9asBbeP5Z4WRuT33Kbi8k53dlQqPxxrFDns%2BfCA%2FAkuc1GnLswSX2SI%2FGXVE34m4acjBoN2vIeTQ%2B4ufg5MKd8YaHebt0DCuGdV5ZTqwx97rm1N3XVF33JdcijCas4y9BjqkAblMvli5tBnQELXRJKU%2B7gfhj7y3Mo%2BSRyIjAc8xf8GxKTUOyvd4HjUXTuCYH5s8D7IoA1KnAZwXJcAcb0UBHGbpnHGHGpdOQQm5BHScr5Ara5n9s7zoYi6%2BCeahbNx5vMOnzQcPx9UGmRBOP2TSbG3KVCbHoFJuLAMZ%2F1YOBxYRpfBAgN%2FsSYeK6Af4Tc1kR6%2B0luC8KoFp2aSklh1F232IuPIk&X-Amz-Signature=664baa9ad78e4edc5378b2cd295eb56ead7c286a4295627d246b68a37de31c1f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VCUF6IUX%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJIMEYCIQCOD%2FKGMCr3TOH3nVB4odjoo4VBBmnGY7x1gdD%2F9qReGQIhAJ%2FT9VUUfWmGzgtRoskz%2FRITFsgS64jtECpviEyT0wNXKv8DCEEQABoMNjM3NDIzMTgzODA1Igy1agWQX47xDwfeLTcq3ANpwH9Mv%2BG%2BsGSzmhik%2By%2BS6sWDwsHm36kqLpLKemhXfhEHWfVMj5GzV8LmZEf%2BYx%2FX9frH0Zs4kC9kANUitegGYztl8PVlwTDoiS%2Bopl%2BTZobr5INIrMsDm2%2FGk85OFjFCehGkK%2BwQxKMxGdo2QmuX2NM9Ejn%2F8%2BwmxpsG6UivHAcwwLJb82k4rJY%2FpG%2F%2FqiSQcbJ0E0haEnX2upAU88OCxRDinZAYe2pJ%2F366UQc3ZXectb6kvkU%2FPzKSekPs6ckFsNgYJdktwsScTNZsckG5DDBmCQuQg5M4Xeb5Gr5IRK5a45GfNRSvOlQlvjFKHtffhqJuEjenxgXjPPpK0FNSzk1jmUnbxHCN8Z%2FIYeaPYK1fM%2BxO%2FIXXrnV6HlOaCUK8NWkc5G%2B5GQ%2FAPCqL9R9zUpoPi%2F3d2TPlLGzm%2FLqdEPHTa5lXKE5bVC215mKFch53mf8ILPRKODBgFMm2d85LKOvN3Bv5bqZv9px3RbxiPp2mWkQF8RPS2TT9PEx10Rjp9asBbeP5Z4WRuT33Kbi8k53dlQqPxxrFDns%2BfCA%2FAkuc1GnLswSX2SI%2FGXVE34m4acjBoN2vIeTQ%2B4ufg5MKd8YaHebt0DCuGdV5ZTqwx97rm1N3XVF33JdcijCas4y9BjqkAblMvli5tBnQELXRJKU%2B7gfhj7y3Mo%2BSRyIjAc8xf8GxKTUOyvd4HjUXTuCYH5s8D7IoA1KnAZwXJcAcb0UBHGbpnHGHGpdOQQm5BHScr5Ara5n9s7zoYi6%2BCeahbNx5vMOnzQcPx9UGmRBOP2TSbG3KVCbHoFJuLAMZ%2F1YOBxYRpfBAgN%2FsSYeK6Af4Tc1kR6%2B0luC8KoFp2aSklh1F232IuPIk&X-Amz-Signature=9a503ef0646040e817916ea8e761402c4e61d4dfd0e32eb5bc74aafd10433b33&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VCUF6IUX%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJIMEYCIQCOD%2FKGMCr3TOH3nVB4odjoo4VBBmnGY7x1gdD%2F9qReGQIhAJ%2FT9VUUfWmGzgtRoskz%2FRITFsgS64jtECpviEyT0wNXKv8DCEEQABoMNjM3NDIzMTgzODA1Igy1agWQX47xDwfeLTcq3ANpwH9Mv%2BG%2BsGSzmhik%2By%2BS6sWDwsHm36kqLpLKemhXfhEHWfVMj5GzV8LmZEf%2BYx%2FX9frH0Zs4kC9kANUitegGYztl8PVlwTDoiS%2Bopl%2BTZobr5INIrMsDm2%2FGk85OFjFCehGkK%2BwQxKMxGdo2QmuX2NM9Ejn%2F8%2BwmxpsG6UivHAcwwLJb82k4rJY%2FpG%2F%2FqiSQcbJ0E0haEnX2upAU88OCxRDinZAYe2pJ%2F366UQc3ZXectb6kvkU%2FPzKSekPs6ckFsNgYJdktwsScTNZsckG5DDBmCQuQg5M4Xeb5Gr5IRK5a45GfNRSvOlQlvjFKHtffhqJuEjenxgXjPPpK0FNSzk1jmUnbxHCN8Z%2FIYeaPYK1fM%2BxO%2FIXXrnV6HlOaCUK8NWkc5G%2B5GQ%2FAPCqL9R9zUpoPi%2F3d2TPlLGzm%2FLqdEPHTa5lXKE5bVC215mKFch53mf8ILPRKODBgFMm2d85LKOvN3Bv5bqZv9px3RbxiPp2mWkQF8RPS2TT9PEx10Rjp9asBbeP5Z4WRuT33Kbi8k53dlQqPxxrFDns%2BfCA%2FAkuc1GnLswSX2SI%2FGXVE34m4acjBoN2vIeTQ%2B4ufg5MKd8YaHebt0DCuGdV5ZTqwx97rm1N3XVF33JdcijCas4y9BjqkAblMvli5tBnQELXRJKU%2B7gfhj7y3Mo%2BSRyIjAc8xf8GxKTUOyvd4HjUXTuCYH5s8D7IoA1KnAZwXJcAcb0UBHGbpnHGHGpdOQQm5BHScr5Ara5n9s7zoYi6%2BCeahbNx5vMOnzQcPx9UGmRBOP2TSbG3KVCbHoFJuLAMZ%2F1YOBxYRpfBAgN%2FsSYeK6Af4Tc1kR6%2B0luC8KoFp2aSklh1F232IuPIk&X-Amz-Signature=dfb2e91b0ff60ae44e7acdcd5edd3ae88e532ecef2ed3daf6e7519d1bc458ea8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XLSIFSGR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081810Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJIMEYCIQC6MRKyG%2FPTsXqzt7Xli9WF9AOpFBXf6xLwH1IERV7QcgIhAOZcRiAeJTrZ%2BNKTXXPtmDnhibNHdQBVimO7b09hkZvEKv8DCEEQABoMNjM3NDIzMTgzODA1IgwdJpvq%2BIlSWp%2BYu0Iq3AP8oLSntXrr0LniANgv8tbjBN%2F9kU0LQ6VxArt3IDc%2F2prPO9llzywSuR6n1p8BYovY6mxYb6Uwrpt9lBLfgvvP99Tc5uwBrTJhsZl5JvxxiMIprdGMJzv9t0h6Gzm8eumvwvDu9AYBqr5FwpGlmMnJrcO8wvKO0GTe53xG53JdKZNRVY8zVjZRwgdKTmI5qbnScylLSgS3jP%2FbNSfIAD2a%2B8kB5LGoh3tCFPfgp1N8xU2nMnji8fAAsb0QtCdmwpqzGRBXlSSyAmisGPlZsb4drIVu69y2DEWQpq3eSjUba7usB1NRgXZarsFIWNV%2FztDPAfRQ2ueFQ7wP1YA3gKBYTJos%2FHL0cnQ4Q%2FTtJCDh%2F5TSCg2IZT004KrTydRGIgVrsecWfBpGQRVthfTDQg%2BqPTez%2FPND3ABEAd9toAqHwCQ%2FWr8tTcwl8rvylzmSTSG4XkxJO0R9iAEthXYojKm1bFdDb3Wj2N1hI8WsLBNygfpqYaxf73GzYizrRNjF%2BvyTk1rpY6Gcv9hbtXir64tkWm11qKTwmSI8RuTcNK0r2OPxla5Qv0EjHRDiYSkrItGxiO1lCA1pAascca0XC%2BcLNJ6LuZ7voKdIVjyPHk2BEfoKV7%2FWilR3BM6llzDcs4y9BjqkAZ7VDk8oJ1GYLKj%2FMUSLbdpIDlj0jcWgaeW8KZD5TuHLEAw7yAYTBybg7xS4HP1pJMM88%2BoVcTX999mfcWkYg3qZKwBGV2typqiFcQBXWisWNGtVGk%2FQD8bAObbal9vRLH3wmXAu2rVf5bsudElNQRAHN1xPDTGh6YvskRqAa%2F1grbRc8CDDXi%2BlOfrh%2BurcfhxKUrbLWi2Z7Ucv%2FBmq2vWFNqnV&X-Amz-Signature=1d07f7ef1f0105d9443ba1df73293181a948f3eddef639098011f6ed1d31bc00&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XLSIFSGR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081810Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJIMEYCIQC6MRKyG%2FPTsXqzt7Xli9WF9AOpFBXf6xLwH1IERV7QcgIhAOZcRiAeJTrZ%2BNKTXXPtmDnhibNHdQBVimO7b09hkZvEKv8DCEEQABoMNjM3NDIzMTgzODA1IgwdJpvq%2BIlSWp%2BYu0Iq3AP8oLSntXrr0LniANgv8tbjBN%2F9kU0LQ6VxArt3IDc%2F2prPO9llzywSuR6n1p8BYovY6mxYb6Uwrpt9lBLfgvvP99Tc5uwBrTJhsZl5JvxxiMIprdGMJzv9t0h6Gzm8eumvwvDu9AYBqr5FwpGlmMnJrcO8wvKO0GTe53xG53JdKZNRVY8zVjZRwgdKTmI5qbnScylLSgS3jP%2FbNSfIAD2a%2B8kB5LGoh3tCFPfgp1N8xU2nMnji8fAAsb0QtCdmwpqzGRBXlSSyAmisGPlZsb4drIVu69y2DEWQpq3eSjUba7usB1NRgXZarsFIWNV%2FztDPAfRQ2ueFQ7wP1YA3gKBYTJos%2FHL0cnQ4Q%2FTtJCDh%2F5TSCg2IZT004KrTydRGIgVrsecWfBpGQRVthfTDQg%2BqPTez%2FPND3ABEAd9toAqHwCQ%2FWr8tTcwl8rvylzmSTSG4XkxJO0R9iAEthXYojKm1bFdDb3Wj2N1hI8WsLBNygfpqYaxf73GzYizrRNjF%2BvyTk1rpY6Gcv9hbtXir64tkWm11qKTwmSI8RuTcNK0r2OPxla5Qv0EjHRDiYSkrItGxiO1lCA1pAascca0XC%2BcLNJ6LuZ7voKdIVjyPHk2BEfoKV7%2FWilR3BM6llzDcs4y9BjqkAZ7VDk8oJ1GYLKj%2FMUSLbdpIDlj0jcWgaeW8KZD5TuHLEAw7yAYTBybg7xS4HP1pJMM88%2BoVcTX999mfcWkYg3qZKwBGV2typqiFcQBXWisWNGtVGk%2FQD8bAObbal9vRLH3wmXAu2rVf5bsudElNQRAHN1xPDTGh6YvskRqAa%2F1grbRc8CDDXi%2BlOfrh%2BurcfhxKUrbLWi2Z7Ucv%2FBmq2vWFNqnV&X-Amz-Signature=b75cf905bc7682c682a34a924b6aeacb30fe7c2b15b6529aa646e84a87d8ffca&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
