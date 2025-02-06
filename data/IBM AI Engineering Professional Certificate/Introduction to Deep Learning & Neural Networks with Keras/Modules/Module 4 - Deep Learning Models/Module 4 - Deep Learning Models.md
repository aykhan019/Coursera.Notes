

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGIUNM7E%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIA4SSdM3TYsUAvFewLT8YnV0t3oBIDR6fe6SGYZXbr5nAiAk9PCNNAIPtjdUB3oKeU%2FlPQbII3R0RZMwOC5eWc8QoSr%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIMwemoCTrGj2Vgh6I1KtwDaKnw8PgwguS6I%2Bct5AzVAXy%2B2kwz98dQeEXf6LCpM%2BgDVWm0s%2Bxyjn9LhYRTW8oBFe19zHBOp4obI1f%2BDymTPnZtKYZC6kCa2ZMktAgaqd6tdgErAQfuGN9ZKcriVURttTOlRA6GwypYReFpJf0%2BSREZwsAl3IDl73y5mVwRFXPUHjiWq6Wo3QuFRpiCZUmtDjhNEif0DlV%2Bc%2BIBFOeXuHBDhkAaXI4IaTXnPyQ51i71iDHe%2FizfhkswJ4mO5JHe09t7xzoAM%2FMBuwN15QiXV2ya46sMDu0nnUP3ZQJPyCg7kKEJ9%2FLknNWnVKi%2FlNBXkM6rpathz3ktSbVDu5G6g4Af7ISN6%2BrfNrRi6jh466r06P9CBlgMI6lLaFHVYxfvaYNvLEIVluAeKWEMA0mIvOwvw9ZHXGCiK6iBvanhtD3nUbB4zVYS3xawCLIBsV4w5FJSC5VIpl8PKW1fwpVf5JIYoH%2FqrfkPhmFsqHzx13BfmrJZ5RJVKCBTkCvLMEL0e5mT88Na0%2B9f5uKTZE3hXcQWaCJyUtBAwWvZVphOSQUZe9mYrbD07yHWblZ1NDDC2Zm%2BinwucZtCed%2B7fSakdgtwgL1mXPLvxZmDWGe5xRs2tM3hOTNFJF%2B3u9kwzfuTvQY6pgGjyCR6Y5COpXRC6ZqmSO5PuLUwidyxgT%2Fv30Npdg4PvnbJymMvi3NGTA4evRJdqyE%2Fe4h8OaQpzfQN62FeAmx%2Ft4xYAfIuIJGcUrMOsoluxz1Op3Pveu29GRZr9ABRGUTih62oB%2BY0vEWevmvtJNPKPgLw%2FJhwjflzUIqDOMPx08vlOWX%2B5WMwwyYWzbadMkdPkqzVzarabCKRSN6qIN1vudoFt1KF&X-Amz-Signature=044ffe4ce8e8f14aa234adeb35980ece16a31802fcbcca860ad54854eaa641bb&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGIUNM7E%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIA4SSdM3TYsUAvFewLT8YnV0t3oBIDR6fe6SGYZXbr5nAiAk9PCNNAIPtjdUB3oKeU%2FlPQbII3R0RZMwOC5eWc8QoSr%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIMwemoCTrGj2Vgh6I1KtwDaKnw8PgwguS6I%2Bct5AzVAXy%2B2kwz98dQeEXf6LCpM%2BgDVWm0s%2Bxyjn9LhYRTW8oBFe19zHBOp4obI1f%2BDymTPnZtKYZC6kCa2ZMktAgaqd6tdgErAQfuGN9ZKcriVURttTOlRA6GwypYReFpJf0%2BSREZwsAl3IDl73y5mVwRFXPUHjiWq6Wo3QuFRpiCZUmtDjhNEif0DlV%2Bc%2BIBFOeXuHBDhkAaXI4IaTXnPyQ51i71iDHe%2FizfhkswJ4mO5JHe09t7xzoAM%2FMBuwN15QiXV2ya46sMDu0nnUP3ZQJPyCg7kKEJ9%2FLknNWnVKi%2FlNBXkM6rpathz3ktSbVDu5G6g4Af7ISN6%2BrfNrRi6jh466r06P9CBlgMI6lLaFHVYxfvaYNvLEIVluAeKWEMA0mIvOwvw9ZHXGCiK6iBvanhtD3nUbB4zVYS3xawCLIBsV4w5FJSC5VIpl8PKW1fwpVf5JIYoH%2FqrfkPhmFsqHzx13BfmrJZ5RJVKCBTkCvLMEL0e5mT88Na0%2B9f5uKTZE3hXcQWaCJyUtBAwWvZVphOSQUZe9mYrbD07yHWblZ1NDDC2Zm%2BinwucZtCed%2B7fSakdgtwgL1mXPLvxZmDWGe5xRs2tM3hOTNFJF%2B3u9kwzfuTvQY6pgGjyCR6Y5COpXRC6ZqmSO5PuLUwidyxgT%2Fv30Npdg4PvnbJymMvi3NGTA4evRJdqyE%2Fe4h8OaQpzfQN62FeAmx%2Ft4xYAfIuIJGcUrMOsoluxz1Op3Pveu29GRZr9ABRGUTih62oB%2BY0vEWevmvtJNPKPgLw%2FJhwjflzUIqDOMPx08vlOWX%2B5WMwwyYWzbadMkdPkqzVzarabCKRSN6qIN1vudoFt1KF&X-Amz-Signature=05fc62b6a09cad129bd03f7c182c92b2383a932968b93011e9208b6e0777dab7&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGIUNM7E%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIA4SSdM3TYsUAvFewLT8YnV0t3oBIDR6fe6SGYZXbr5nAiAk9PCNNAIPtjdUB3oKeU%2FlPQbII3R0RZMwOC5eWc8QoSr%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIMwemoCTrGj2Vgh6I1KtwDaKnw8PgwguS6I%2Bct5AzVAXy%2B2kwz98dQeEXf6LCpM%2BgDVWm0s%2Bxyjn9LhYRTW8oBFe19zHBOp4obI1f%2BDymTPnZtKYZC6kCa2ZMktAgaqd6tdgErAQfuGN9ZKcriVURttTOlRA6GwypYReFpJf0%2BSREZwsAl3IDl73y5mVwRFXPUHjiWq6Wo3QuFRpiCZUmtDjhNEif0DlV%2Bc%2BIBFOeXuHBDhkAaXI4IaTXnPyQ51i71iDHe%2FizfhkswJ4mO5JHe09t7xzoAM%2FMBuwN15QiXV2ya46sMDu0nnUP3ZQJPyCg7kKEJ9%2FLknNWnVKi%2FlNBXkM6rpathz3ktSbVDu5G6g4Af7ISN6%2BrfNrRi6jh466r06P9CBlgMI6lLaFHVYxfvaYNvLEIVluAeKWEMA0mIvOwvw9ZHXGCiK6iBvanhtD3nUbB4zVYS3xawCLIBsV4w5FJSC5VIpl8PKW1fwpVf5JIYoH%2FqrfkPhmFsqHzx13BfmrJZ5RJVKCBTkCvLMEL0e5mT88Na0%2B9f5uKTZE3hXcQWaCJyUtBAwWvZVphOSQUZe9mYrbD07yHWblZ1NDDC2Zm%2BinwucZtCed%2B7fSakdgtwgL1mXPLvxZmDWGe5xRs2tM3hOTNFJF%2B3u9kwzfuTvQY6pgGjyCR6Y5COpXRC6ZqmSO5PuLUwidyxgT%2Fv30Npdg4PvnbJymMvi3NGTA4evRJdqyE%2Fe4h8OaQpzfQN62FeAmx%2Ft4xYAfIuIJGcUrMOsoluxz1Op3Pveu29GRZr9ABRGUTih62oB%2BY0vEWevmvtJNPKPgLw%2FJhwjflzUIqDOMPx08vlOWX%2B5WMwwyYWzbadMkdPkqzVzarabCKRSN6qIN1vudoFt1KF&X-Amz-Signature=1e65b394bff58a2074214246e6afcee005b335bd7db9aa50289e04ed633ffbca&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGIUNM7E%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIA4SSdM3TYsUAvFewLT8YnV0t3oBIDR6fe6SGYZXbr5nAiAk9PCNNAIPtjdUB3oKeU%2FlPQbII3R0RZMwOC5eWc8QoSr%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIMwemoCTrGj2Vgh6I1KtwDaKnw8PgwguS6I%2Bct5AzVAXy%2B2kwz98dQeEXf6LCpM%2BgDVWm0s%2Bxyjn9LhYRTW8oBFe19zHBOp4obI1f%2BDymTPnZtKYZC6kCa2ZMktAgaqd6tdgErAQfuGN9ZKcriVURttTOlRA6GwypYReFpJf0%2BSREZwsAl3IDl73y5mVwRFXPUHjiWq6Wo3QuFRpiCZUmtDjhNEif0DlV%2Bc%2BIBFOeXuHBDhkAaXI4IaTXnPyQ51i71iDHe%2FizfhkswJ4mO5JHe09t7xzoAM%2FMBuwN15QiXV2ya46sMDu0nnUP3ZQJPyCg7kKEJ9%2FLknNWnVKi%2FlNBXkM6rpathz3ktSbVDu5G6g4Af7ISN6%2BrfNrRi6jh466r06P9CBlgMI6lLaFHVYxfvaYNvLEIVluAeKWEMA0mIvOwvw9ZHXGCiK6iBvanhtD3nUbB4zVYS3xawCLIBsV4w5FJSC5VIpl8PKW1fwpVf5JIYoH%2FqrfkPhmFsqHzx13BfmrJZ5RJVKCBTkCvLMEL0e5mT88Na0%2B9f5uKTZE3hXcQWaCJyUtBAwWvZVphOSQUZe9mYrbD07yHWblZ1NDDC2Zm%2BinwucZtCed%2B7fSakdgtwgL1mXPLvxZmDWGe5xRs2tM3hOTNFJF%2B3u9kwzfuTvQY6pgGjyCR6Y5COpXRC6ZqmSO5PuLUwidyxgT%2Fv30Npdg4PvnbJymMvi3NGTA4evRJdqyE%2Fe4h8OaQpzfQN62FeAmx%2Ft4xYAfIuIJGcUrMOsoluxz1Op3Pveu29GRZr9ABRGUTih62oB%2BY0vEWevmvtJNPKPgLw%2FJhwjflzUIqDOMPx08vlOWX%2B5WMwwyYWzbadMkdPkqzVzarabCKRSN6qIN1vudoFt1KF&X-Amz-Signature=29c9398b05dfcd60ca2e0a033c6f7ad41c0e6875e2e2d8da4bcad7d44f0c2e12&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGIUNM7E%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIA4SSdM3TYsUAvFewLT8YnV0t3oBIDR6fe6SGYZXbr5nAiAk9PCNNAIPtjdUB3oKeU%2FlPQbII3R0RZMwOC5eWc8QoSr%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIMwemoCTrGj2Vgh6I1KtwDaKnw8PgwguS6I%2Bct5AzVAXy%2B2kwz98dQeEXf6LCpM%2BgDVWm0s%2Bxyjn9LhYRTW8oBFe19zHBOp4obI1f%2BDymTPnZtKYZC6kCa2ZMktAgaqd6tdgErAQfuGN9ZKcriVURttTOlRA6GwypYReFpJf0%2BSREZwsAl3IDl73y5mVwRFXPUHjiWq6Wo3QuFRpiCZUmtDjhNEif0DlV%2Bc%2BIBFOeXuHBDhkAaXI4IaTXnPyQ51i71iDHe%2FizfhkswJ4mO5JHe09t7xzoAM%2FMBuwN15QiXV2ya46sMDu0nnUP3ZQJPyCg7kKEJ9%2FLknNWnVKi%2FlNBXkM6rpathz3ktSbVDu5G6g4Af7ISN6%2BrfNrRi6jh466r06P9CBlgMI6lLaFHVYxfvaYNvLEIVluAeKWEMA0mIvOwvw9ZHXGCiK6iBvanhtD3nUbB4zVYS3xawCLIBsV4w5FJSC5VIpl8PKW1fwpVf5JIYoH%2FqrfkPhmFsqHzx13BfmrJZ5RJVKCBTkCvLMEL0e5mT88Na0%2B9f5uKTZE3hXcQWaCJyUtBAwWvZVphOSQUZe9mYrbD07yHWblZ1NDDC2Zm%2BinwucZtCed%2B7fSakdgtwgL1mXPLvxZmDWGe5xRs2tM3hOTNFJF%2B3u9kwzfuTvQY6pgGjyCR6Y5COpXRC6ZqmSO5PuLUwidyxgT%2Fv30Npdg4PvnbJymMvi3NGTA4evRJdqyE%2Fe4h8OaQpzfQN62FeAmx%2Ft4xYAfIuIJGcUrMOsoluxz1Op3Pveu29GRZr9ABRGUTih62oB%2BY0vEWevmvtJNPKPgLw%2FJhwjflzUIqDOMPx08vlOWX%2B5WMwwyYWzbadMkdPkqzVzarabCKRSN6qIN1vudoFt1KF&X-Amz-Signature=7369e09344b3b421dfc5df44695c4080782843b5bbc8dc0ecc7caf58de610be5&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGIUNM7E%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIA4SSdM3TYsUAvFewLT8YnV0t3oBIDR6fe6SGYZXbr5nAiAk9PCNNAIPtjdUB3oKeU%2FlPQbII3R0RZMwOC5eWc8QoSr%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIMwemoCTrGj2Vgh6I1KtwDaKnw8PgwguS6I%2Bct5AzVAXy%2B2kwz98dQeEXf6LCpM%2BgDVWm0s%2Bxyjn9LhYRTW8oBFe19zHBOp4obI1f%2BDymTPnZtKYZC6kCa2ZMktAgaqd6tdgErAQfuGN9ZKcriVURttTOlRA6GwypYReFpJf0%2BSREZwsAl3IDl73y5mVwRFXPUHjiWq6Wo3QuFRpiCZUmtDjhNEif0DlV%2Bc%2BIBFOeXuHBDhkAaXI4IaTXnPyQ51i71iDHe%2FizfhkswJ4mO5JHe09t7xzoAM%2FMBuwN15QiXV2ya46sMDu0nnUP3ZQJPyCg7kKEJ9%2FLknNWnVKi%2FlNBXkM6rpathz3ktSbVDu5G6g4Af7ISN6%2BrfNrRi6jh466r06P9CBlgMI6lLaFHVYxfvaYNvLEIVluAeKWEMA0mIvOwvw9ZHXGCiK6iBvanhtD3nUbB4zVYS3xawCLIBsV4w5FJSC5VIpl8PKW1fwpVf5JIYoH%2FqrfkPhmFsqHzx13BfmrJZ5RJVKCBTkCvLMEL0e5mT88Na0%2B9f5uKTZE3hXcQWaCJyUtBAwWvZVphOSQUZe9mYrbD07yHWblZ1NDDC2Zm%2BinwucZtCed%2B7fSakdgtwgL1mXPLvxZmDWGe5xRs2tM3hOTNFJF%2B3u9kwzfuTvQY6pgGjyCR6Y5COpXRC6ZqmSO5PuLUwidyxgT%2Fv30Npdg4PvnbJymMvi3NGTA4evRJdqyE%2Fe4h8OaQpzfQN62FeAmx%2Ft4xYAfIuIJGcUrMOsoluxz1Op3Pveu29GRZr9ABRGUTih62oB%2BY0vEWevmvtJNPKPgLw%2FJhwjflzUIqDOMPx08vlOWX%2B5WMwwyYWzbadMkdPkqzVzarabCKRSN6qIN1vudoFt1KF&X-Amz-Signature=c61a8b1ebea119349995d86fee948cda6267c7486606346bc727883cbcaca7d0&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGIUNM7E%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIA4SSdM3TYsUAvFewLT8YnV0t3oBIDR6fe6SGYZXbr5nAiAk9PCNNAIPtjdUB3oKeU%2FlPQbII3R0RZMwOC5eWc8QoSr%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIMwemoCTrGj2Vgh6I1KtwDaKnw8PgwguS6I%2Bct5AzVAXy%2B2kwz98dQeEXf6LCpM%2BgDVWm0s%2Bxyjn9LhYRTW8oBFe19zHBOp4obI1f%2BDymTPnZtKYZC6kCa2ZMktAgaqd6tdgErAQfuGN9ZKcriVURttTOlRA6GwypYReFpJf0%2BSREZwsAl3IDl73y5mVwRFXPUHjiWq6Wo3QuFRpiCZUmtDjhNEif0DlV%2Bc%2BIBFOeXuHBDhkAaXI4IaTXnPyQ51i71iDHe%2FizfhkswJ4mO5JHe09t7xzoAM%2FMBuwN15QiXV2ya46sMDu0nnUP3ZQJPyCg7kKEJ9%2FLknNWnVKi%2FlNBXkM6rpathz3ktSbVDu5G6g4Af7ISN6%2BrfNrRi6jh466r06P9CBlgMI6lLaFHVYxfvaYNvLEIVluAeKWEMA0mIvOwvw9ZHXGCiK6iBvanhtD3nUbB4zVYS3xawCLIBsV4w5FJSC5VIpl8PKW1fwpVf5JIYoH%2FqrfkPhmFsqHzx13BfmrJZ5RJVKCBTkCvLMEL0e5mT88Na0%2B9f5uKTZE3hXcQWaCJyUtBAwWvZVphOSQUZe9mYrbD07yHWblZ1NDDC2Zm%2BinwucZtCed%2B7fSakdgtwgL1mXPLvxZmDWGe5xRs2tM3hOTNFJF%2B3u9kwzfuTvQY6pgGjyCR6Y5COpXRC6ZqmSO5PuLUwidyxgT%2Fv30Npdg4PvnbJymMvi3NGTA4evRJdqyE%2Fe4h8OaQpzfQN62FeAmx%2Ft4xYAfIuIJGcUrMOsoluxz1Op3Pveu29GRZr9ABRGUTih62oB%2BY0vEWevmvtJNPKPgLw%2FJhwjflzUIqDOMPx08vlOWX%2B5WMwwyYWzbadMkdPkqzVzarabCKRSN6qIN1vudoFt1KF&X-Amz-Signature=610a21fae9d4c627b804b5bf15c7d66ab279d82acdddabffb8c3f1f7b436f680&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGIUNM7E%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIA4SSdM3TYsUAvFewLT8YnV0t3oBIDR6fe6SGYZXbr5nAiAk9PCNNAIPtjdUB3oKeU%2FlPQbII3R0RZMwOC5eWc8QoSr%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIMwemoCTrGj2Vgh6I1KtwDaKnw8PgwguS6I%2Bct5AzVAXy%2B2kwz98dQeEXf6LCpM%2BgDVWm0s%2Bxyjn9LhYRTW8oBFe19zHBOp4obI1f%2BDymTPnZtKYZC6kCa2ZMktAgaqd6tdgErAQfuGN9ZKcriVURttTOlRA6GwypYReFpJf0%2BSREZwsAl3IDl73y5mVwRFXPUHjiWq6Wo3QuFRpiCZUmtDjhNEif0DlV%2Bc%2BIBFOeXuHBDhkAaXI4IaTXnPyQ51i71iDHe%2FizfhkswJ4mO5JHe09t7xzoAM%2FMBuwN15QiXV2ya46sMDu0nnUP3ZQJPyCg7kKEJ9%2FLknNWnVKi%2FlNBXkM6rpathz3ktSbVDu5G6g4Af7ISN6%2BrfNrRi6jh466r06P9CBlgMI6lLaFHVYxfvaYNvLEIVluAeKWEMA0mIvOwvw9ZHXGCiK6iBvanhtD3nUbB4zVYS3xawCLIBsV4w5FJSC5VIpl8PKW1fwpVf5JIYoH%2FqrfkPhmFsqHzx13BfmrJZ5RJVKCBTkCvLMEL0e5mT88Na0%2B9f5uKTZE3hXcQWaCJyUtBAwWvZVphOSQUZe9mYrbD07yHWblZ1NDDC2Zm%2BinwucZtCed%2B7fSakdgtwgL1mXPLvxZmDWGe5xRs2tM3hOTNFJF%2B3u9kwzfuTvQY6pgGjyCR6Y5COpXRC6ZqmSO5PuLUwidyxgT%2Fv30Npdg4PvnbJymMvi3NGTA4evRJdqyE%2Fe4h8OaQpzfQN62FeAmx%2Ft4xYAfIuIJGcUrMOsoluxz1Op3Pveu29GRZr9ABRGUTih62oB%2BY0vEWevmvtJNPKPgLw%2FJhwjflzUIqDOMPx08vlOWX%2B5WMwwyYWzbadMkdPkqzVzarabCKRSN6qIN1vudoFt1KF&X-Amz-Signature=1e204c9449f0fc18a273dc61b887843108861aacfab35d0edd9ced686cb35f44&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGIUNM7E%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIA4SSdM3TYsUAvFewLT8YnV0t3oBIDR6fe6SGYZXbr5nAiAk9PCNNAIPtjdUB3oKeU%2FlPQbII3R0RZMwOC5eWc8QoSr%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIMwemoCTrGj2Vgh6I1KtwDaKnw8PgwguS6I%2Bct5AzVAXy%2B2kwz98dQeEXf6LCpM%2BgDVWm0s%2Bxyjn9LhYRTW8oBFe19zHBOp4obI1f%2BDymTPnZtKYZC6kCa2ZMktAgaqd6tdgErAQfuGN9ZKcriVURttTOlRA6GwypYReFpJf0%2BSREZwsAl3IDl73y5mVwRFXPUHjiWq6Wo3QuFRpiCZUmtDjhNEif0DlV%2Bc%2BIBFOeXuHBDhkAaXI4IaTXnPyQ51i71iDHe%2FizfhkswJ4mO5JHe09t7xzoAM%2FMBuwN15QiXV2ya46sMDu0nnUP3ZQJPyCg7kKEJ9%2FLknNWnVKi%2FlNBXkM6rpathz3ktSbVDu5G6g4Af7ISN6%2BrfNrRi6jh466r06P9CBlgMI6lLaFHVYxfvaYNvLEIVluAeKWEMA0mIvOwvw9ZHXGCiK6iBvanhtD3nUbB4zVYS3xawCLIBsV4w5FJSC5VIpl8PKW1fwpVf5JIYoH%2FqrfkPhmFsqHzx13BfmrJZ5RJVKCBTkCvLMEL0e5mT88Na0%2B9f5uKTZE3hXcQWaCJyUtBAwWvZVphOSQUZe9mYrbD07yHWblZ1NDDC2Zm%2BinwucZtCed%2B7fSakdgtwgL1mXPLvxZmDWGe5xRs2tM3hOTNFJF%2B3u9kwzfuTvQY6pgGjyCR6Y5COpXRC6ZqmSO5PuLUwidyxgT%2Fv30Npdg4PvnbJymMvi3NGTA4evRJdqyE%2Fe4h8OaQpzfQN62FeAmx%2Ft4xYAfIuIJGcUrMOsoluxz1Op3Pveu29GRZr9ABRGUTih62oB%2BY0vEWevmvtJNPKPgLw%2FJhwjflzUIqDOMPx08vlOWX%2B5WMwwyYWzbadMkdPkqzVzarabCKRSN6qIN1vudoFt1KF&X-Amz-Signature=2a948da091a4865207afa29250bd30ec8929d57c89a4035c684ccc9c95bc37c1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667KRMFANE%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCID7Y1V3aD%2FvAjIen2ZP0dW9jvDRJu1ezGfqdPh0jUm67AiEA8bFxD055WiTrlR2a8otm17xLMcj%2FMbwXpPBoc2jkA7Yq%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDMiQEA9Aa%2FmV2%2BkQhircA3KJZUleR2mm3WONe0HTGhEDhF%2Bh5rdQ26b%2FytTx0RjDGQiXYDpgPY0JCFBMy%2BY%2BVSSd7ZE6juOIUOV3WLWO0YgoTQSEOaKaJmimcP4%2B3tb7oZESyFsJGZOVZu8zLlPOlgszTMPZuNmxB9cFHJ%2FTeHAcoB%2BB7JV7c%2F35BVIeAY9w5dyHhYusG%2FiwYkpKYCkSZaQocyaRODkYYOOPuxPm8DHHoFcoql00eKWgBlttGGGKzDwLQxLlZBwp3%2FZ68RJja00QIfvWuOrTpzcEGhM80I52puFVYdalTz8iBqaQRLrJR0hSBZWtYxJO%2FG7y6YHvB1ON8hRaME8jpP8A%2BZHxXdwUTVTKkT4pNURL4fkdObRtMcGw%2ByqRSSw%2B5O%2Fh0DvrYBIMpCBwDDlCnYNk%2BTNstJJ7S5LlTLwbNbc7QPZG6pmjtHm%2BkcwJOPyitodUeNJaJvmIOWgck2mik7s7bllB3csq5%2B3joTEJkLCAveO6eYoOeKb6hon3aJ9ytGybL1gi5lX11K%2BY0st7yNZVLdCCmQ0%2FHvH8AcFUHVdEMhjNi0TH5JqgdYhoTyEro0i9qhmfueuiECU7nC8LPnVQoHH7Y1ts%2FVDsvSLE%2B9wXeoNd7modKlVEIjNUxSdFhqqaMOj7k70GOqUB0pAm6APD5XTWl5Y3v5rZBQf5GivBnEB10Ko%2FPwJqCqUnIqeU0c8RlhXpQskIxl2EhHMA%2BJ3vSCKZFIvj1lCO9ntC9zEn2R%2F4kYvYHpQ3vrUCN7KovufyxDvmxy0aSO8RE7akmaOEI5%2BmwE9CNQo%2F1TqZj3o2qjuE4du9OgqyvYkgrhPw2B%2BXgzuh%2BCbkVLH7gY1BSn9ShzA9VqaWdD3Sv4kVUCXB&X-Amz-Signature=71a4dd42b4d974811b6b3070bcc5c119276085efa91616e055f907a3dc4ac4b1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667KRMFANE%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCID7Y1V3aD%2FvAjIen2ZP0dW9jvDRJu1ezGfqdPh0jUm67AiEA8bFxD055WiTrlR2a8otm17xLMcj%2FMbwXpPBoc2jkA7Yq%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDMiQEA9Aa%2FmV2%2BkQhircA3KJZUleR2mm3WONe0HTGhEDhF%2Bh5rdQ26b%2FytTx0RjDGQiXYDpgPY0JCFBMy%2BY%2BVSSd7ZE6juOIUOV3WLWO0YgoTQSEOaKaJmimcP4%2B3tb7oZESyFsJGZOVZu8zLlPOlgszTMPZuNmxB9cFHJ%2FTeHAcoB%2BB7JV7c%2F35BVIeAY9w5dyHhYusG%2FiwYkpKYCkSZaQocyaRODkYYOOPuxPm8DHHoFcoql00eKWgBlttGGGKzDwLQxLlZBwp3%2FZ68RJja00QIfvWuOrTpzcEGhM80I52puFVYdalTz8iBqaQRLrJR0hSBZWtYxJO%2FG7y6YHvB1ON8hRaME8jpP8A%2BZHxXdwUTVTKkT4pNURL4fkdObRtMcGw%2ByqRSSw%2B5O%2Fh0DvrYBIMpCBwDDlCnYNk%2BTNstJJ7S5LlTLwbNbc7QPZG6pmjtHm%2BkcwJOPyitodUeNJaJvmIOWgck2mik7s7bllB3csq5%2B3joTEJkLCAveO6eYoOeKb6hon3aJ9ytGybL1gi5lX11K%2BY0st7yNZVLdCCmQ0%2FHvH8AcFUHVdEMhjNi0TH5JqgdYhoTyEro0i9qhmfueuiECU7nC8LPnVQoHH7Y1ts%2FVDsvSLE%2B9wXeoNd7modKlVEIjNUxSdFhqqaMOj7k70GOqUB0pAm6APD5XTWl5Y3v5rZBQf5GivBnEB10Ko%2FPwJqCqUnIqeU0c8RlhXpQskIxl2EhHMA%2BJ3vSCKZFIvj1lCO9ntC9zEn2R%2F4kYvYHpQ3vrUCN7KovufyxDvmxy0aSO8RE7akmaOEI5%2BmwE9CNQo%2F1TqZj3o2qjuE4du9OgqyvYkgrhPw2B%2BXgzuh%2BCbkVLH7gY1BSn9ShzA9VqaWdD3Sv4kVUCXB&X-Amz-Signature=1894ea5fcb2e0705d5261121ac8921c299031b54e891096b502ea76fa5ef3449&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
