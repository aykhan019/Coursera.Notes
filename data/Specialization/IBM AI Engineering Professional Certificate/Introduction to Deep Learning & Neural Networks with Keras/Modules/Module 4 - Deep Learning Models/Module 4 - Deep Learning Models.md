

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46652QN4SUN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAYvSbKhEEwbQxED5j00%2FdeNg4%2B9ZRnmTELL10uuVv5KAiEA66ok8FL8otc1bnR0SHqoL4VvSCIgf4n1qKX2GJjUYM8qiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPAHiZyHqkCrlaUcmSrcA9IRhDsZqmSBW4jN%2F22%2BQp2A%2FNHAd8PK2N50slTGsKKSaUXve%2FeoaWAo8A9nEjAsWQewGZd8FHpS%2BSTdfMzUxKy9YqwT%2B%2BgROnMrzsZOLDLSp3779VMBVVV%2BP555%2FV5F0QZoWInmH1AIyaDkPxVyD0w9sb9PU0%2FTt8ZkCBrH%2BvciMcXH3%2B7tHjW68Jal0eekzkaIdvyuSU83IKx%2BpOJl7Lkb5AEw1O6nx%2BN8%2FgtOg6xA1c3SSn7Wl%2BO%2FUqJfn7bvbw%2BKawZLYVHqD9T1EDAw1HZVspRpNT2VPhlb3vjr217M92JY7mdqFUwnZQ%2BgFMdrGvKrLMjXAkyVr6Ol5wlmGBU8XK%2B1cyYi9AJhsHQQt6Led5LLJX%2Br3rFPZaNy14wXBGFhBR0yCDYhTMbs5t0VjR5GeHNdkHopsA6QRBH5rDhP1DMC21dM%2FsVyZTHtiPn%2BMgxH3HFbJkM8ceSmeq1UMlPqJNLQZVh%2BhNAoPpRYexiNxg7yHP9pcMsp6nnfuIJ7XYaUXj5CwPQbrShmaCIFLzye92tSD4ssoHeiXtAGBcxs51BL8i1fJ7KMQLTgTHpmlOHQjiZK1h0XYXkdORF%2FVi9ksI816M2W%2B4%2BNyc3x%2BRIlMizTRlhM7fOn2OwyMOmD6bwGOqUBs70GFaKeRQPGmNlOPV13SLZPQGth5K1%2FgfEnblGQ3TJG1CnIpaTZBnxgmM27R3QRjoHOL3bmVpLA2rS2%2FJ9a22aF49BY4CfiHozMEfVjiAYibuPp6DJ2jV5aQ1iRY5C4YlYeGpj%2ByGnkm7sasC2meXddQobLSbQsQ%2F6Hp3ZIr8L72qA7KHgSTx3f1ldP1HL8UzzqRTfw2yzy6ua5MSB8g0deXsPv&X-Amz-Signature=2caa38bd86e3d339bd4104f1bd12f9e9b68feb99a3e1b4053a84fa6627d6d27e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46652QN4SUN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAYvSbKhEEwbQxED5j00%2FdeNg4%2B9ZRnmTELL10uuVv5KAiEA66ok8FL8otc1bnR0SHqoL4VvSCIgf4n1qKX2GJjUYM8qiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPAHiZyHqkCrlaUcmSrcA9IRhDsZqmSBW4jN%2F22%2BQp2A%2FNHAd8PK2N50slTGsKKSaUXve%2FeoaWAo8A9nEjAsWQewGZd8FHpS%2BSTdfMzUxKy9YqwT%2B%2BgROnMrzsZOLDLSp3779VMBVVV%2BP555%2FV5F0QZoWInmH1AIyaDkPxVyD0w9sb9PU0%2FTt8ZkCBrH%2BvciMcXH3%2B7tHjW68Jal0eekzkaIdvyuSU83IKx%2BpOJl7Lkb5AEw1O6nx%2BN8%2FgtOg6xA1c3SSn7Wl%2BO%2FUqJfn7bvbw%2BKawZLYVHqD9T1EDAw1HZVspRpNT2VPhlb3vjr217M92JY7mdqFUwnZQ%2BgFMdrGvKrLMjXAkyVr6Ol5wlmGBU8XK%2B1cyYi9AJhsHQQt6Led5LLJX%2Br3rFPZaNy14wXBGFhBR0yCDYhTMbs5t0VjR5GeHNdkHopsA6QRBH5rDhP1DMC21dM%2FsVyZTHtiPn%2BMgxH3HFbJkM8ceSmeq1UMlPqJNLQZVh%2BhNAoPpRYexiNxg7yHP9pcMsp6nnfuIJ7XYaUXj5CwPQbrShmaCIFLzye92tSD4ssoHeiXtAGBcxs51BL8i1fJ7KMQLTgTHpmlOHQjiZK1h0XYXkdORF%2FVi9ksI816M2W%2B4%2BNyc3x%2BRIlMizTRlhM7fOn2OwyMOmD6bwGOqUBs70GFaKeRQPGmNlOPV13SLZPQGth5K1%2FgfEnblGQ3TJG1CnIpaTZBnxgmM27R3QRjoHOL3bmVpLA2rS2%2FJ9a22aF49BY4CfiHozMEfVjiAYibuPp6DJ2jV5aQ1iRY5C4YlYeGpj%2ByGnkm7sasC2meXddQobLSbQsQ%2F6Hp3ZIr8L72qA7KHgSTx3f1ldP1HL8UzzqRTfw2yzy6ua5MSB8g0deXsPv&X-Amz-Signature=5c41a125918c34ad13660087ec19c4ed1521a72022d6d42731cdbfbead8fe783&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46652QN4SUN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAYvSbKhEEwbQxED5j00%2FdeNg4%2B9ZRnmTELL10uuVv5KAiEA66ok8FL8otc1bnR0SHqoL4VvSCIgf4n1qKX2GJjUYM8qiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPAHiZyHqkCrlaUcmSrcA9IRhDsZqmSBW4jN%2F22%2BQp2A%2FNHAd8PK2N50slTGsKKSaUXve%2FeoaWAo8A9nEjAsWQewGZd8FHpS%2BSTdfMzUxKy9YqwT%2B%2BgROnMrzsZOLDLSp3779VMBVVV%2BP555%2FV5F0QZoWInmH1AIyaDkPxVyD0w9sb9PU0%2FTt8ZkCBrH%2BvciMcXH3%2B7tHjW68Jal0eekzkaIdvyuSU83IKx%2BpOJl7Lkb5AEw1O6nx%2BN8%2FgtOg6xA1c3SSn7Wl%2BO%2FUqJfn7bvbw%2BKawZLYVHqD9T1EDAw1HZVspRpNT2VPhlb3vjr217M92JY7mdqFUwnZQ%2BgFMdrGvKrLMjXAkyVr6Ol5wlmGBU8XK%2B1cyYi9AJhsHQQt6Led5LLJX%2Br3rFPZaNy14wXBGFhBR0yCDYhTMbs5t0VjR5GeHNdkHopsA6QRBH5rDhP1DMC21dM%2FsVyZTHtiPn%2BMgxH3HFbJkM8ceSmeq1UMlPqJNLQZVh%2BhNAoPpRYexiNxg7yHP9pcMsp6nnfuIJ7XYaUXj5CwPQbrShmaCIFLzye92tSD4ssoHeiXtAGBcxs51BL8i1fJ7KMQLTgTHpmlOHQjiZK1h0XYXkdORF%2FVi9ksI816M2W%2B4%2BNyc3x%2BRIlMizTRlhM7fOn2OwyMOmD6bwGOqUBs70GFaKeRQPGmNlOPV13SLZPQGth5K1%2FgfEnblGQ3TJG1CnIpaTZBnxgmM27R3QRjoHOL3bmVpLA2rS2%2FJ9a22aF49BY4CfiHozMEfVjiAYibuPp6DJ2jV5aQ1iRY5C4YlYeGpj%2ByGnkm7sasC2meXddQobLSbQsQ%2F6Hp3ZIr8L72qA7KHgSTx3f1ldP1HL8UzzqRTfw2yzy6ua5MSB8g0deXsPv&X-Amz-Signature=6ced87f87e33c7e49cdaaef8e19bbeae0bbc0e952b2bd9d6d5ed965fc86d3dcc&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46652QN4SUN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAYvSbKhEEwbQxED5j00%2FdeNg4%2B9ZRnmTELL10uuVv5KAiEA66ok8FL8otc1bnR0SHqoL4VvSCIgf4n1qKX2GJjUYM8qiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPAHiZyHqkCrlaUcmSrcA9IRhDsZqmSBW4jN%2F22%2BQp2A%2FNHAd8PK2N50slTGsKKSaUXve%2FeoaWAo8A9nEjAsWQewGZd8FHpS%2BSTdfMzUxKy9YqwT%2B%2BgROnMrzsZOLDLSp3779VMBVVV%2BP555%2FV5F0QZoWInmH1AIyaDkPxVyD0w9sb9PU0%2FTt8ZkCBrH%2BvciMcXH3%2B7tHjW68Jal0eekzkaIdvyuSU83IKx%2BpOJl7Lkb5AEw1O6nx%2BN8%2FgtOg6xA1c3SSn7Wl%2BO%2FUqJfn7bvbw%2BKawZLYVHqD9T1EDAw1HZVspRpNT2VPhlb3vjr217M92JY7mdqFUwnZQ%2BgFMdrGvKrLMjXAkyVr6Ol5wlmGBU8XK%2B1cyYi9AJhsHQQt6Led5LLJX%2Br3rFPZaNy14wXBGFhBR0yCDYhTMbs5t0VjR5GeHNdkHopsA6QRBH5rDhP1DMC21dM%2FsVyZTHtiPn%2BMgxH3HFbJkM8ceSmeq1UMlPqJNLQZVh%2BhNAoPpRYexiNxg7yHP9pcMsp6nnfuIJ7XYaUXj5CwPQbrShmaCIFLzye92tSD4ssoHeiXtAGBcxs51BL8i1fJ7KMQLTgTHpmlOHQjiZK1h0XYXkdORF%2FVi9ksI816M2W%2B4%2BNyc3x%2BRIlMizTRlhM7fOn2OwyMOmD6bwGOqUBs70GFaKeRQPGmNlOPV13SLZPQGth5K1%2FgfEnblGQ3TJG1CnIpaTZBnxgmM27R3QRjoHOL3bmVpLA2rS2%2FJ9a22aF49BY4CfiHozMEfVjiAYibuPp6DJ2jV5aQ1iRY5C4YlYeGpj%2ByGnkm7sasC2meXddQobLSbQsQ%2F6Hp3ZIr8L72qA7KHgSTx3f1ldP1HL8UzzqRTfw2yzy6ua5MSB8g0deXsPv&X-Amz-Signature=84fb26677f4a050ac2e5a58af01def3112d05cb79deaf5bdaad21c162115b1fb&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46652QN4SUN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAYvSbKhEEwbQxED5j00%2FdeNg4%2B9ZRnmTELL10uuVv5KAiEA66ok8FL8otc1bnR0SHqoL4VvSCIgf4n1qKX2GJjUYM8qiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPAHiZyHqkCrlaUcmSrcA9IRhDsZqmSBW4jN%2F22%2BQp2A%2FNHAd8PK2N50slTGsKKSaUXve%2FeoaWAo8A9nEjAsWQewGZd8FHpS%2BSTdfMzUxKy9YqwT%2B%2BgROnMrzsZOLDLSp3779VMBVVV%2BP555%2FV5F0QZoWInmH1AIyaDkPxVyD0w9sb9PU0%2FTt8ZkCBrH%2BvciMcXH3%2B7tHjW68Jal0eekzkaIdvyuSU83IKx%2BpOJl7Lkb5AEw1O6nx%2BN8%2FgtOg6xA1c3SSn7Wl%2BO%2FUqJfn7bvbw%2BKawZLYVHqD9T1EDAw1HZVspRpNT2VPhlb3vjr217M92JY7mdqFUwnZQ%2BgFMdrGvKrLMjXAkyVr6Ol5wlmGBU8XK%2B1cyYi9AJhsHQQt6Led5LLJX%2Br3rFPZaNy14wXBGFhBR0yCDYhTMbs5t0VjR5GeHNdkHopsA6QRBH5rDhP1DMC21dM%2FsVyZTHtiPn%2BMgxH3HFbJkM8ceSmeq1UMlPqJNLQZVh%2BhNAoPpRYexiNxg7yHP9pcMsp6nnfuIJ7XYaUXj5CwPQbrShmaCIFLzye92tSD4ssoHeiXtAGBcxs51BL8i1fJ7KMQLTgTHpmlOHQjiZK1h0XYXkdORF%2FVi9ksI816M2W%2B4%2BNyc3x%2BRIlMizTRlhM7fOn2OwyMOmD6bwGOqUBs70GFaKeRQPGmNlOPV13SLZPQGth5K1%2FgfEnblGQ3TJG1CnIpaTZBnxgmM27R3QRjoHOL3bmVpLA2rS2%2FJ9a22aF49BY4CfiHozMEfVjiAYibuPp6DJ2jV5aQ1iRY5C4YlYeGpj%2ByGnkm7sasC2meXddQobLSbQsQ%2F6Hp3ZIr8L72qA7KHgSTx3f1ldP1HL8UzzqRTfw2yzy6ua5MSB8g0deXsPv&X-Amz-Signature=4857fd668e70dceda50d727d6b0a5f6c5ba97f877ccace4dd6392073072c2c37&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46652QN4SUN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAYvSbKhEEwbQxED5j00%2FdeNg4%2B9ZRnmTELL10uuVv5KAiEA66ok8FL8otc1bnR0SHqoL4VvSCIgf4n1qKX2GJjUYM8qiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPAHiZyHqkCrlaUcmSrcA9IRhDsZqmSBW4jN%2F22%2BQp2A%2FNHAd8PK2N50slTGsKKSaUXve%2FeoaWAo8A9nEjAsWQewGZd8FHpS%2BSTdfMzUxKy9YqwT%2B%2BgROnMrzsZOLDLSp3779VMBVVV%2BP555%2FV5F0QZoWInmH1AIyaDkPxVyD0w9sb9PU0%2FTt8ZkCBrH%2BvciMcXH3%2B7tHjW68Jal0eekzkaIdvyuSU83IKx%2BpOJl7Lkb5AEw1O6nx%2BN8%2FgtOg6xA1c3SSn7Wl%2BO%2FUqJfn7bvbw%2BKawZLYVHqD9T1EDAw1HZVspRpNT2VPhlb3vjr217M92JY7mdqFUwnZQ%2BgFMdrGvKrLMjXAkyVr6Ol5wlmGBU8XK%2B1cyYi9AJhsHQQt6Led5LLJX%2Br3rFPZaNy14wXBGFhBR0yCDYhTMbs5t0VjR5GeHNdkHopsA6QRBH5rDhP1DMC21dM%2FsVyZTHtiPn%2BMgxH3HFbJkM8ceSmeq1UMlPqJNLQZVh%2BhNAoPpRYexiNxg7yHP9pcMsp6nnfuIJ7XYaUXj5CwPQbrShmaCIFLzye92tSD4ssoHeiXtAGBcxs51BL8i1fJ7KMQLTgTHpmlOHQjiZK1h0XYXkdORF%2FVi9ksI816M2W%2B4%2BNyc3x%2BRIlMizTRlhM7fOn2OwyMOmD6bwGOqUBs70GFaKeRQPGmNlOPV13SLZPQGth5K1%2FgfEnblGQ3TJG1CnIpaTZBnxgmM27R3QRjoHOL3bmVpLA2rS2%2FJ9a22aF49BY4CfiHozMEfVjiAYibuPp6DJ2jV5aQ1iRY5C4YlYeGpj%2ByGnkm7sasC2meXddQobLSbQsQ%2F6Hp3ZIr8L72qA7KHgSTx3f1ldP1HL8UzzqRTfw2yzy6ua5MSB8g0deXsPv&X-Amz-Signature=232492e1d2732e518f577dc494106fe51715f4a843e40dfea49369972d2e704e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46652QN4SUN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAYvSbKhEEwbQxED5j00%2FdeNg4%2B9ZRnmTELL10uuVv5KAiEA66ok8FL8otc1bnR0SHqoL4VvSCIgf4n1qKX2GJjUYM8qiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPAHiZyHqkCrlaUcmSrcA9IRhDsZqmSBW4jN%2F22%2BQp2A%2FNHAd8PK2N50slTGsKKSaUXve%2FeoaWAo8A9nEjAsWQewGZd8FHpS%2BSTdfMzUxKy9YqwT%2B%2BgROnMrzsZOLDLSp3779VMBVVV%2BP555%2FV5F0QZoWInmH1AIyaDkPxVyD0w9sb9PU0%2FTt8ZkCBrH%2BvciMcXH3%2B7tHjW68Jal0eekzkaIdvyuSU83IKx%2BpOJl7Lkb5AEw1O6nx%2BN8%2FgtOg6xA1c3SSn7Wl%2BO%2FUqJfn7bvbw%2BKawZLYVHqD9T1EDAw1HZVspRpNT2VPhlb3vjr217M92JY7mdqFUwnZQ%2BgFMdrGvKrLMjXAkyVr6Ol5wlmGBU8XK%2B1cyYi9AJhsHQQt6Led5LLJX%2Br3rFPZaNy14wXBGFhBR0yCDYhTMbs5t0VjR5GeHNdkHopsA6QRBH5rDhP1DMC21dM%2FsVyZTHtiPn%2BMgxH3HFbJkM8ceSmeq1UMlPqJNLQZVh%2BhNAoPpRYexiNxg7yHP9pcMsp6nnfuIJ7XYaUXj5CwPQbrShmaCIFLzye92tSD4ssoHeiXtAGBcxs51BL8i1fJ7KMQLTgTHpmlOHQjiZK1h0XYXkdORF%2FVi9ksI816M2W%2B4%2BNyc3x%2BRIlMizTRlhM7fOn2OwyMOmD6bwGOqUBs70GFaKeRQPGmNlOPV13SLZPQGth5K1%2FgfEnblGQ3TJG1CnIpaTZBnxgmM27R3QRjoHOL3bmVpLA2rS2%2FJ9a22aF49BY4CfiHozMEfVjiAYibuPp6DJ2jV5aQ1iRY5C4YlYeGpj%2ByGnkm7sasC2meXddQobLSbQsQ%2F6Hp3ZIr8L72qA7KHgSTx3f1ldP1HL8UzzqRTfw2yzy6ua5MSB8g0deXsPv&X-Amz-Signature=c76b5102896a77b72d5ae8e783ed2cb49dcf2e6ea2203fb8d173b76901ffdf35&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46652QN4SUN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAYvSbKhEEwbQxED5j00%2FdeNg4%2B9ZRnmTELL10uuVv5KAiEA66ok8FL8otc1bnR0SHqoL4VvSCIgf4n1qKX2GJjUYM8qiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPAHiZyHqkCrlaUcmSrcA9IRhDsZqmSBW4jN%2F22%2BQp2A%2FNHAd8PK2N50slTGsKKSaUXve%2FeoaWAo8A9nEjAsWQewGZd8FHpS%2BSTdfMzUxKy9YqwT%2B%2BgROnMrzsZOLDLSp3779VMBVVV%2BP555%2FV5F0QZoWInmH1AIyaDkPxVyD0w9sb9PU0%2FTt8ZkCBrH%2BvciMcXH3%2B7tHjW68Jal0eekzkaIdvyuSU83IKx%2BpOJl7Lkb5AEw1O6nx%2BN8%2FgtOg6xA1c3SSn7Wl%2BO%2FUqJfn7bvbw%2BKawZLYVHqD9T1EDAw1HZVspRpNT2VPhlb3vjr217M92JY7mdqFUwnZQ%2BgFMdrGvKrLMjXAkyVr6Ol5wlmGBU8XK%2B1cyYi9AJhsHQQt6Led5LLJX%2Br3rFPZaNy14wXBGFhBR0yCDYhTMbs5t0VjR5GeHNdkHopsA6QRBH5rDhP1DMC21dM%2FsVyZTHtiPn%2BMgxH3HFbJkM8ceSmeq1UMlPqJNLQZVh%2BhNAoPpRYexiNxg7yHP9pcMsp6nnfuIJ7XYaUXj5CwPQbrShmaCIFLzye92tSD4ssoHeiXtAGBcxs51BL8i1fJ7KMQLTgTHpmlOHQjiZK1h0XYXkdORF%2FVi9ksI816M2W%2B4%2BNyc3x%2BRIlMizTRlhM7fOn2OwyMOmD6bwGOqUBs70GFaKeRQPGmNlOPV13SLZPQGth5K1%2FgfEnblGQ3TJG1CnIpaTZBnxgmM27R3QRjoHOL3bmVpLA2rS2%2FJ9a22aF49BY4CfiHozMEfVjiAYibuPp6DJ2jV5aQ1iRY5C4YlYeGpj%2ByGnkm7sasC2meXddQobLSbQsQ%2F6Hp3ZIr8L72qA7KHgSTx3f1ldP1HL8UzzqRTfw2yzy6ua5MSB8g0deXsPv&X-Amz-Signature=121d03806f03e27226227e6226329ee45f36dd2ed18fea7fabc387c31035abf7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46652QN4SUN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAYvSbKhEEwbQxED5j00%2FdeNg4%2B9ZRnmTELL10uuVv5KAiEA66ok8FL8otc1bnR0SHqoL4VvSCIgf4n1qKX2GJjUYM8qiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPAHiZyHqkCrlaUcmSrcA9IRhDsZqmSBW4jN%2F22%2BQp2A%2FNHAd8PK2N50slTGsKKSaUXve%2FeoaWAo8A9nEjAsWQewGZd8FHpS%2BSTdfMzUxKy9YqwT%2B%2BgROnMrzsZOLDLSp3779VMBVVV%2BP555%2FV5F0QZoWInmH1AIyaDkPxVyD0w9sb9PU0%2FTt8ZkCBrH%2BvciMcXH3%2B7tHjW68Jal0eekzkaIdvyuSU83IKx%2BpOJl7Lkb5AEw1O6nx%2BN8%2FgtOg6xA1c3SSn7Wl%2BO%2FUqJfn7bvbw%2BKawZLYVHqD9T1EDAw1HZVspRpNT2VPhlb3vjr217M92JY7mdqFUwnZQ%2BgFMdrGvKrLMjXAkyVr6Ol5wlmGBU8XK%2B1cyYi9AJhsHQQt6Led5LLJX%2Br3rFPZaNy14wXBGFhBR0yCDYhTMbs5t0VjR5GeHNdkHopsA6QRBH5rDhP1DMC21dM%2FsVyZTHtiPn%2BMgxH3HFbJkM8ceSmeq1UMlPqJNLQZVh%2BhNAoPpRYexiNxg7yHP9pcMsp6nnfuIJ7XYaUXj5CwPQbrShmaCIFLzye92tSD4ssoHeiXtAGBcxs51BL8i1fJ7KMQLTgTHpmlOHQjiZK1h0XYXkdORF%2FVi9ksI816M2W%2B4%2BNyc3x%2BRIlMizTRlhM7fOn2OwyMOmD6bwGOqUBs70GFaKeRQPGmNlOPV13SLZPQGth5K1%2FgfEnblGQ3TJG1CnIpaTZBnxgmM27R3QRjoHOL3bmVpLA2rS2%2FJ9a22aF49BY4CfiHozMEfVjiAYibuPp6DJ2jV5aQ1iRY5C4YlYeGpj%2ByGnkm7sasC2meXddQobLSbQsQ%2F6Hp3ZIr8L72qA7KHgSTx3f1ldP1HL8UzzqRTfw2yzy6ua5MSB8g0deXsPv&X-Amz-Signature=e33f03edb9d8bf22841fbba6b813d19e78bf65b65307c92884a60b89c3691fd5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZKSYINFT%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDmtxNUVp3xqDFxrvP8U36Wf%2BVbx7MG%2B3L%2B98GlQpOviAiEA%2FY8HSacbe43DvR%2B3%2F2s9raZG%2FgOp41khxj8otwDixFQqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAV91p20x6OHFH4c9SrcA1d6y2aVZhZN01HBT0L1ZM7YUNQUNOq0dQn1XxyrBFc0xzl1W5Z%2BEax9rJCtyaZPkqS%2Biu6KArF%2FYn7hVQZu1udgbxWZF0PlktpyXmL%2BvQj3NygFbRVLI6oGhtL%2FzD7RKwEI%2F3ET7Sj2yGUjBfv5GSbHFbRkT3jsuLurExaw1mlmcQlmNzPiCG0U3Ngt55tjQU%2BMaheLtp3shZoCs%2B6%2FWZIGBlDe51BJ0VlwsuteLXCSp19gtrFyYJGa6r8KsvD5MoXjHTY9ZaOawX8MVBCPn0Nrn5WqmOUKIgnM6ZOJrq6neweIqYKJJylDupGuwZNOBzAs7d3Lue8UbWuzomsI7rDXsvX3L1iulC9SVkSQzwoIxKMUGQe6JVdgf22n4PXJHYebARhQJfUIkRNhAZZL7khFYWXuR6%2BKbFU4IqFwa8rJ5caFkIoiDKYtBfufANKvaHFuaaIFb4gj0fP4eU%2BqIywHBXxRzZ46QdJy4wCb%2BYoMi0myiIMEHYmBp8wP%2Bl%2FkOMaFOX9uJ5fET%2BW6hk4Wx9W4HUc3T%2FuSgX3awK712PozFN2gFigPzEDLPtjTqNXxQAPJwjNMBCWJYXFtxBlSAzgm7cE8mI1XUKFypTnbXJoYUfk0RM5P5O5aazLOMMKD6bwGOqUBE6Uy0OUgogvmWYC1TNoYLyiEvhHUr%2BN3pY%2B9ll%2FVU%2F5M0yPFjshHRMzJvPxgsJ5ZsTd%2B9QSUPa5j4xzsOMggBcLsvfGY0ZkMYtkh4VUO2bdGuolfV7Rkeb7E%2BQhZR1ydUKU%2B6s2gSLP6xvVy5CcmzmQN1Rsf%2FYPRecPLkZYRvufxEng1BFFnqIMzENEKGCFJCGg%2BgMxsu4uUEl5jKwMJpuQDmsvk&X-Amz-Signature=1f00facd0abbbaabecd45e1365b0701d5c9e21b34d6da81edb52b6e042ac14bd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZKSYINFT%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDmtxNUVp3xqDFxrvP8U36Wf%2BVbx7MG%2B3L%2B98GlQpOviAiEA%2FY8HSacbe43DvR%2B3%2F2s9raZG%2FgOp41khxj8otwDixFQqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAV91p20x6OHFH4c9SrcA1d6y2aVZhZN01HBT0L1ZM7YUNQUNOq0dQn1XxyrBFc0xzl1W5Z%2BEax9rJCtyaZPkqS%2Biu6KArF%2FYn7hVQZu1udgbxWZF0PlktpyXmL%2BvQj3NygFbRVLI6oGhtL%2FzD7RKwEI%2F3ET7Sj2yGUjBfv5GSbHFbRkT3jsuLurExaw1mlmcQlmNzPiCG0U3Ngt55tjQU%2BMaheLtp3shZoCs%2B6%2FWZIGBlDe51BJ0VlwsuteLXCSp19gtrFyYJGa6r8KsvD5MoXjHTY9ZaOawX8MVBCPn0Nrn5WqmOUKIgnM6ZOJrq6neweIqYKJJylDupGuwZNOBzAs7d3Lue8UbWuzomsI7rDXsvX3L1iulC9SVkSQzwoIxKMUGQe6JVdgf22n4PXJHYebARhQJfUIkRNhAZZL7khFYWXuR6%2BKbFU4IqFwa8rJ5caFkIoiDKYtBfufANKvaHFuaaIFb4gj0fP4eU%2BqIywHBXxRzZ46QdJy4wCb%2BYoMi0myiIMEHYmBp8wP%2Bl%2FkOMaFOX9uJ5fET%2BW6hk4Wx9W4HUc3T%2FuSgX3awK712PozFN2gFigPzEDLPtjTqNXxQAPJwjNMBCWJYXFtxBlSAzgm7cE8mI1XUKFypTnbXJoYUfk0RM5P5O5aazLOMMKD6bwGOqUBE6Uy0OUgogvmWYC1TNoYLyiEvhHUr%2BN3pY%2B9ll%2FVU%2F5M0yPFjshHRMzJvPxgsJ5ZsTd%2B9QSUPa5j4xzsOMggBcLsvfGY0ZkMYtkh4VUO2bdGuolfV7Rkeb7E%2BQhZR1ydUKU%2B6s2gSLP6xvVy5CcmzmQN1Rsf%2FYPRecPLkZYRvufxEng1BFFnqIMzENEKGCFJCGg%2BgMxsu4uUEl5jKwMJpuQDmsvk&X-Amz-Signature=e8ecc352ff734f9e3753d5a520e89324acb16e34bc678fd898423edb5595430f&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
