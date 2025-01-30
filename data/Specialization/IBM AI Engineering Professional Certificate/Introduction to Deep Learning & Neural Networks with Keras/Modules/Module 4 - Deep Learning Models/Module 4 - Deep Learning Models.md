

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663VWLP4SB%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191125Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGKrcdvPjHrWownINMNsC8yQ%2B036t08A%2FgQc3WobzP%2BIAiEA6dgKQHqpsFStWts0jQauZkOB0JKuXsdv2dVU2a7eNxgqiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLwls95SRcSdCuk5byrcA6gXKGGTo%2F17pPrOd0iSMrl1tpru8ldtoctXCBEhSXBV%2BmYcbcrPD1x1Isb7LpBbRQqQX8eOHoL9zLYG9JleT%2BhBnRfaCsLrRggPxZaFImk7oBZddyuqPfEToc8aYydXVEIvozsY3gfB6haJmFGADpFQDxNSNr4XTRSGjQj6N9YQCqDRON78AclwtnK5lzsxQAQId5FU%2FYc4v8WqTL%2BPzNYNXHjXtsUz5P7PeYXg7ikWYV%2Fl4uc1yMmJkEO4Ybr3rng2s1n3wYTY0HW5Gq9iNLT%2FAkCGCMbo8jTIZf1337g516lUxQ2KCNQgOB2sgbf0Q6uAgrA2%2Fzqz3XKKPtSo35ePl%2F7g5hX4F07tV9yD6%2BAzaeZ6Y67tF549ABFvO8u1h03%2B79u53VTjTVxPbsaMxK99MGotmToDqsbEnEaAF7irDt4AtTAAO7FkNjbCcMkaPovGwOGJ1LLvRqkV02ZUEdRlM6vwQbbrYR99oojRe49lwPFxMAxsLeDLIl5mFcVxte8MRXGHCOrDYgvEbw9aitO8crBpVzrIRwkdLxi4zs7uyvfR4TkmkSNQ37Ao7alUSMIpXwIUF89RptYgQlXCMmNDwOcuCZ1YKxqaLLcbsIrH8A9dXiJ8DVNx2MzIMN6O77wGOqUBIJNN3tPe1AU7lbBb5R44jL%2BHjQE%2FLmpPYNtpc11ocf8ZSD0UKIFhhZuSX%2F1qcOpFqm6jvby9r5EybJNugFDLHZMmpoGX3ufAgyhSluC3rXKE2TiWDl6EOckWj5KWQiOsdIDf3SqFRaG%2BqIL1rnfd2bLMx9ayiuV7QfpD6IU76KqbW6CG7sCvUIhsBJ65WatGAQoEoQUVZHFYT4j9TIRPKalcj54u&X-Amz-Signature=106f5b3f02e37ca878690fa72d2f05af3862726160f91494ae37262381ce3f1e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663VWLP4SB%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191125Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGKrcdvPjHrWownINMNsC8yQ%2B036t08A%2FgQc3WobzP%2BIAiEA6dgKQHqpsFStWts0jQauZkOB0JKuXsdv2dVU2a7eNxgqiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLwls95SRcSdCuk5byrcA6gXKGGTo%2F17pPrOd0iSMrl1tpru8ldtoctXCBEhSXBV%2BmYcbcrPD1x1Isb7LpBbRQqQX8eOHoL9zLYG9JleT%2BhBnRfaCsLrRggPxZaFImk7oBZddyuqPfEToc8aYydXVEIvozsY3gfB6haJmFGADpFQDxNSNr4XTRSGjQj6N9YQCqDRON78AclwtnK5lzsxQAQId5FU%2FYc4v8WqTL%2BPzNYNXHjXtsUz5P7PeYXg7ikWYV%2Fl4uc1yMmJkEO4Ybr3rng2s1n3wYTY0HW5Gq9iNLT%2FAkCGCMbo8jTIZf1337g516lUxQ2KCNQgOB2sgbf0Q6uAgrA2%2Fzqz3XKKPtSo35ePl%2F7g5hX4F07tV9yD6%2BAzaeZ6Y67tF549ABFvO8u1h03%2B79u53VTjTVxPbsaMxK99MGotmToDqsbEnEaAF7irDt4AtTAAO7FkNjbCcMkaPovGwOGJ1LLvRqkV02ZUEdRlM6vwQbbrYR99oojRe49lwPFxMAxsLeDLIl5mFcVxte8MRXGHCOrDYgvEbw9aitO8crBpVzrIRwkdLxi4zs7uyvfR4TkmkSNQ37Ao7alUSMIpXwIUF89RptYgQlXCMmNDwOcuCZ1YKxqaLLcbsIrH8A9dXiJ8DVNx2MzIMN6O77wGOqUBIJNN3tPe1AU7lbBb5R44jL%2BHjQE%2FLmpPYNtpc11ocf8ZSD0UKIFhhZuSX%2F1qcOpFqm6jvby9r5EybJNugFDLHZMmpoGX3ufAgyhSluC3rXKE2TiWDl6EOckWj5KWQiOsdIDf3SqFRaG%2BqIL1rnfd2bLMx9ayiuV7QfpD6IU76KqbW6CG7sCvUIhsBJ65WatGAQoEoQUVZHFYT4j9TIRPKalcj54u&X-Amz-Signature=dbb6f2cb19d5dd338a26a4b333ec2f04d3ad4fa95e2a6ef33f835fed2ad9e65f&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663VWLP4SB%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191125Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGKrcdvPjHrWownINMNsC8yQ%2B036t08A%2FgQc3WobzP%2BIAiEA6dgKQHqpsFStWts0jQauZkOB0JKuXsdv2dVU2a7eNxgqiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLwls95SRcSdCuk5byrcA6gXKGGTo%2F17pPrOd0iSMrl1tpru8ldtoctXCBEhSXBV%2BmYcbcrPD1x1Isb7LpBbRQqQX8eOHoL9zLYG9JleT%2BhBnRfaCsLrRggPxZaFImk7oBZddyuqPfEToc8aYydXVEIvozsY3gfB6haJmFGADpFQDxNSNr4XTRSGjQj6N9YQCqDRON78AclwtnK5lzsxQAQId5FU%2FYc4v8WqTL%2BPzNYNXHjXtsUz5P7PeYXg7ikWYV%2Fl4uc1yMmJkEO4Ybr3rng2s1n3wYTY0HW5Gq9iNLT%2FAkCGCMbo8jTIZf1337g516lUxQ2KCNQgOB2sgbf0Q6uAgrA2%2Fzqz3XKKPtSo35ePl%2F7g5hX4F07tV9yD6%2BAzaeZ6Y67tF549ABFvO8u1h03%2B79u53VTjTVxPbsaMxK99MGotmToDqsbEnEaAF7irDt4AtTAAO7FkNjbCcMkaPovGwOGJ1LLvRqkV02ZUEdRlM6vwQbbrYR99oojRe49lwPFxMAxsLeDLIl5mFcVxte8MRXGHCOrDYgvEbw9aitO8crBpVzrIRwkdLxi4zs7uyvfR4TkmkSNQ37Ao7alUSMIpXwIUF89RptYgQlXCMmNDwOcuCZ1YKxqaLLcbsIrH8A9dXiJ8DVNx2MzIMN6O77wGOqUBIJNN3tPe1AU7lbBb5R44jL%2BHjQE%2FLmpPYNtpc11ocf8ZSD0UKIFhhZuSX%2F1qcOpFqm6jvby9r5EybJNugFDLHZMmpoGX3ufAgyhSluC3rXKE2TiWDl6EOckWj5KWQiOsdIDf3SqFRaG%2BqIL1rnfd2bLMx9ayiuV7QfpD6IU76KqbW6CG7sCvUIhsBJ65WatGAQoEoQUVZHFYT4j9TIRPKalcj54u&X-Amz-Signature=a30358f6c32f9ddefecb02e2e07ac9c92a6ac491e360a0c197a42e24eec805b0&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663VWLP4SB%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191125Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGKrcdvPjHrWownINMNsC8yQ%2B036t08A%2FgQc3WobzP%2BIAiEA6dgKQHqpsFStWts0jQauZkOB0JKuXsdv2dVU2a7eNxgqiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLwls95SRcSdCuk5byrcA6gXKGGTo%2F17pPrOd0iSMrl1tpru8ldtoctXCBEhSXBV%2BmYcbcrPD1x1Isb7LpBbRQqQX8eOHoL9zLYG9JleT%2BhBnRfaCsLrRggPxZaFImk7oBZddyuqPfEToc8aYydXVEIvozsY3gfB6haJmFGADpFQDxNSNr4XTRSGjQj6N9YQCqDRON78AclwtnK5lzsxQAQId5FU%2FYc4v8WqTL%2BPzNYNXHjXtsUz5P7PeYXg7ikWYV%2Fl4uc1yMmJkEO4Ybr3rng2s1n3wYTY0HW5Gq9iNLT%2FAkCGCMbo8jTIZf1337g516lUxQ2KCNQgOB2sgbf0Q6uAgrA2%2Fzqz3XKKPtSo35ePl%2F7g5hX4F07tV9yD6%2BAzaeZ6Y67tF549ABFvO8u1h03%2B79u53VTjTVxPbsaMxK99MGotmToDqsbEnEaAF7irDt4AtTAAO7FkNjbCcMkaPovGwOGJ1LLvRqkV02ZUEdRlM6vwQbbrYR99oojRe49lwPFxMAxsLeDLIl5mFcVxte8MRXGHCOrDYgvEbw9aitO8crBpVzrIRwkdLxi4zs7uyvfR4TkmkSNQ37Ao7alUSMIpXwIUF89RptYgQlXCMmNDwOcuCZ1YKxqaLLcbsIrH8A9dXiJ8DVNx2MzIMN6O77wGOqUBIJNN3tPe1AU7lbBb5R44jL%2BHjQE%2FLmpPYNtpc11ocf8ZSD0UKIFhhZuSX%2F1qcOpFqm6jvby9r5EybJNugFDLHZMmpoGX3ufAgyhSluC3rXKE2TiWDl6EOckWj5KWQiOsdIDf3SqFRaG%2BqIL1rnfd2bLMx9ayiuV7QfpD6IU76KqbW6CG7sCvUIhsBJ65WatGAQoEoQUVZHFYT4j9TIRPKalcj54u&X-Amz-Signature=f6e9d22b2d82d4920bee34b69a0893437107a8e9cf8dfbff1d538fb73d0f286a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663VWLP4SB%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191125Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGKrcdvPjHrWownINMNsC8yQ%2B036t08A%2FgQc3WobzP%2BIAiEA6dgKQHqpsFStWts0jQauZkOB0JKuXsdv2dVU2a7eNxgqiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLwls95SRcSdCuk5byrcA6gXKGGTo%2F17pPrOd0iSMrl1tpru8ldtoctXCBEhSXBV%2BmYcbcrPD1x1Isb7LpBbRQqQX8eOHoL9zLYG9JleT%2BhBnRfaCsLrRggPxZaFImk7oBZddyuqPfEToc8aYydXVEIvozsY3gfB6haJmFGADpFQDxNSNr4XTRSGjQj6N9YQCqDRON78AclwtnK5lzsxQAQId5FU%2FYc4v8WqTL%2BPzNYNXHjXtsUz5P7PeYXg7ikWYV%2Fl4uc1yMmJkEO4Ybr3rng2s1n3wYTY0HW5Gq9iNLT%2FAkCGCMbo8jTIZf1337g516lUxQ2KCNQgOB2sgbf0Q6uAgrA2%2Fzqz3XKKPtSo35ePl%2F7g5hX4F07tV9yD6%2BAzaeZ6Y67tF549ABFvO8u1h03%2B79u53VTjTVxPbsaMxK99MGotmToDqsbEnEaAF7irDt4AtTAAO7FkNjbCcMkaPovGwOGJ1LLvRqkV02ZUEdRlM6vwQbbrYR99oojRe49lwPFxMAxsLeDLIl5mFcVxte8MRXGHCOrDYgvEbw9aitO8crBpVzrIRwkdLxi4zs7uyvfR4TkmkSNQ37Ao7alUSMIpXwIUF89RptYgQlXCMmNDwOcuCZ1YKxqaLLcbsIrH8A9dXiJ8DVNx2MzIMN6O77wGOqUBIJNN3tPe1AU7lbBb5R44jL%2BHjQE%2FLmpPYNtpc11ocf8ZSD0UKIFhhZuSX%2F1qcOpFqm6jvby9r5EybJNugFDLHZMmpoGX3ufAgyhSluC3rXKE2TiWDl6EOckWj5KWQiOsdIDf3SqFRaG%2BqIL1rnfd2bLMx9ayiuV7QfpD6IU76KqbW6CG7sCvUIhsBJ65WatGAQoEoQUVZHFYT4j9TIRPKalcj54u&X-Amz-Signature=2f5f5c3cdda0ae1b55089fb674501095f5e839ec1d5e920ec2a22a80f555cd5b&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663VWLP4SB%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191125Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGKrcdvPjHrWownINMNsC8yQ%2B036t08A%2FgQc3WobzP%2BIAiEA6dgKQHqpsFStWts0jQauZkOB0JKuXsdv2dVU2a7eNxgqiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLwls95SRcSdCuk5byrcA6gXKGGTo%2F17pPrOd0iSMrl1tpru8ldtoctXCBEhSXBV%2BmYcbcrPD1x1Isb7LpBbRQqQX8eOHoL9zLYG9JleT%2BhBnRfaCsLrRggPxZaFImk7oBZddyuqPfEToc8aYydXVEIvozsY3gfB6haJmFGADpFQDxNSNr4XTRSGjQj6N9YQCqDRON78AclwtnK5lzsxQAQId5FU%2FYc4v8WqTL%2BPzNYNXHjXtsUz5P7PeYXg7ikWYV%2Fl4uc1yMmJkEO4Ybr3rng2s1n3wYTY0HW5Gq9iNLT%2FAkCGCMbo8jTIZf1337g516lUxQ2KCNQgOB2sgbf0Q6uAgrA2%2Fzqz3XKKPtSo35ePl%2F7g5hX4F07tV9yD6%2BAzaeZ6Y67tF549ABFvO8u1h03%2B79u53VTjTVxPbsaMxK99MGotmToDqsbEnEaAF7irDt4AtTAAO7FkNjbCcMkaPovGwOGJ1LLvRqkV02ZUEdRlM6vwQbbrYR99oojRe49lwPFxMAxsLeDLIl5mFcVxte8MRXGHCOrDYgvEbw9aitO8crBpVzrIRwkdLxi4zs7uyvfR4TkmkSNQ37Ao7alUSMIpXwIUF89RptYgQlXCMmNDwOcuCZ1YKxqaLLcbsIrH8A9dXiJ8DVNx2MzIMN6O77wGOqUBIJNN3tPe1AU7lbBb5R44jL%2BHjQE%2FLmpPYNtpc11ocf8ZSD0UKIFhhZuSX%2F1qcOpFqm6jvby9r5EybJNugFDLHZMmpoGX3ufAgyhSluC3rXKE2TiWDl6EOckWj5KWQiOsdIDf3SqFRaG%2BqIL1rnfd2bLMx9ayiuV7QfpD6IU76KqbW6CG7sCvUIhsBJ65WatGAQoEoQUVZHFYT4j9TIRPKalcj54u&X-Amz-Signature=d85e06daf3457674e854a896fc5c19c29ff071fd05655d42754aa2b8d4dafad8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663VWLP4SB%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191125Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGKrcdvPjHrWownINMNsC8yQ%2B036t08A%2FgQc3WobzP%2BIAiEA6dgKQHqpsFStWts0jQauZkOB0JKuXsdv2dVU2a7eNxgqiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLwls95SRcSdCuk5byrcA6gXKGGTo%2F17pPrOd0iSMrl1tpru8ldtoctXCBEhSXBV%2BmYcbcrPD1x1Isb7LpBbRQqQX8eOHoL9zLYG9JleT%2BhBnRfaCsLrRggPxZaFImk7oBZddyuqPfEToc8aYydXVEIvozsY3gfB6haJmFGADpFQDxNSNr4XTRSGjQj6N9YQCqDRON78AclwtnK5lzsxQAQId5FU%2FYc4v8WqTL%2BPzNYNXHjXtsUz5P7PeYXg7ikWYV%2Fl4uc1yMmJkEO4Ybr3rng2s1n3wYTY0HW5Gq9iNLT%2FAkCGCMbo8jTIZf1337g516lUxQ2KCNQgOB2sgbf0Q6uAgrA2%2Fzqz3XKKPtSo35ePl%2F7g5hX4F07tV9yD6%2BAzaeZ6Y67tF549ABFvO8u1h03%2B79u53VTjTVxPbsaMxK99MGotmToDqsbEnEaAF7irDt4AtTAAO7FkNjbCcMkaPovGwOGJ1LLvRqkV02ZUEdRlM6vwQbbrYR99oojRe49lwPFxMAxsLeDLIl5mFcVxte8MRXGHCOrDYgvEbw9aitO8crBpVzrIRwkdLxi4zs7uyvfR4TkmkSNQ37Ao7alUSMIpXwIUF89RptYgQlXCMmNDwOcuCZ1YKxqaLLcbsIrH8A9dXiJ8DVNx2MzIMN6O77wGOqUBIJNN3tPe1AU7lbBb5R44jL%2BHjQE%2FLmpPYNtpc11ocf8ZSD0UKIFhhZuSX%2F1qcOpFqm6jvby9r5EybJNugFDLHZMmpoGX3ufAgyhSluC3rXKE2TiWDl6EOckWj5KWQiOsdIDf3SqFRaG%2BqIL1rnfd2bLMx9ayiuV7QfpD6IU76KqbW6CG7sCvUIhsBJ65WatGAQoEoQUVZHFYT4j9TIRPKalcj54u&X-Amz-Signature=e12e4b243e3b9ddd5c18e38f408246eb0540c741974beb3056af2129476a33e0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663VWLP4SB%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191125Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGKrcdvPjHrWownINMNsC8yQ%2B036t08A%2FgQc3WobzP%2BIAiEA6dgKQHqpsFStWts0jQauZkOB0JKuXsdv2dVU2a7eNxgqiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLwls95SRcSdCuk5byrcA6gXKGGTo%2F17pPrOd0iSMrl1tpru8ldtoctXCBEhSXBV%2BmYcbcrPD1x1Isb7LpBbRQqQX8eOHoL9zLYG9JleT%2BhBnRfaCsLrRggPxZaFImk7oBZddyuqPfEToc8aYydXVEIvozsY3gfB6haJmFGADpFQDxNSNr4XTRSGjQj6N9YQCqDRON78AclwtnK5lzsxQAQId5FU%2FYc4v8WqTL%2BPzNYNXHjXtsUz5P7PeYXg7ikWYV%2Fl4uc1yMmJkEO4Ybr3rng2s1n3wYTY0HW5Gq9iNLT%2FAkCGCMbo8jTIZf1337g516lUxQ2KCNQgOB2sgbf0Q6uAgrA2%2Fzqz3XKKPtSo35ePl%2F7g5hX4F07tV9yD6%2BAzaeZ6Y67tF549ABFvO8u1h03%2B79u53VTjTVxPbsaMxK99MGotmToDqsbEnEaAF7irDt4AtTAAO7FkNjbCcMkaPovGwOGJ1LLvRqkV02ZUEdRlM6vwQbbrYR99oojRe49lwPFxMAxsLeDLIl5mFcVxte8MRXGHCOrDYgvEbw9aitO8crBpVzrIRwkdLxi4zs7uyvfR4TkmkSNQ37Ao7alUSMIpXwIUF89RptYgQlXCMmNDwOcuCZ1YKxqaLLcbsIrH8A9dXiJ8DVNx2MzIMN6O77wGOqUBIJNN3tPe1AU7lbBb5R44jL%2BHjQE%2FLmpPYNtpc11ocf8ZSD0UKIFhhZuSX%2F1qcOpFqm6jvby9r5EybJNugFDLHZMmpoGX3ufAgyhSluC3rXKE2TiWDl6EOckWj5KWQiOsdIDf3SqFRaG%2BqIL1rnfd2bLMx9ayiuV7QfpD6IU76KqbW6CG7sCvUIhsBJ65WatGAQoEoQUVZHFYT4j9TIRPKalcj54u&X-Amz-Signature=b16ddbc54434198c696c689ac1f6d7bfa70fd78a4808d6804eaae4604258e54a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663VWLP4SB%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191125Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGKrcdvPjHrWownINMNsC8yQ%2B036t08A%2FgQc3WobzP%2BIAiEA6dgKQHqpsFStWts0jQauZkOB0JKuXsdv2dVU2a7eNxgqiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLwls95SRcSdCuk5byrcA6gXKGGTo%2F17pPrOd0iSMrl1tpru8ldtoctXCBEhSXBV%2BmYcbcrPD1x1Isb7LpBbRQqQX8eOHoL9zLYG9JleT%2BhBnRfaCsLrRggPxZaFImk7oBZddyuqPfEToc8aYydXVEIvozsY3gfB6haJmFGADpFQDxNSNr4XTRSGjQj6N9YQCqDRON78AclwtnK5lzsxQAQId5FU%2FYc4v8WqTL%2BPzNYNXHjXtsUz5P7PeYXg7ikWYV%2Fl4uc1yMmJkEO4Ybr3rng2s1n3wYTY0HW5Gq9iNLT%2FAkCGCMbo8jTIZf1337g516lUxQ2KCNQgOB2sgbf0Q6uAgrA2%2Fzqz3XKKPtSo35ePl%2F7g5hX4F07tV9yD6%2BAzaeZ6Y67tF549ABFvO8u1h03%2B79u53VTjTVxPbsaMxK99MGotmToDqsbEnEaAF7irDt4AtTAAO7FkNjbCcMkaPovGwOGJ1LLvRqkV02ZUEdRlM6vwQbbrYR99oojRe49lwPFxMAxsLeDLIl5mFcVxte8MRXGHCOrDYgvEbw9aitO8crBpVzrIRwkdLxi4zs7uyvfR4TkmkSNQ37Ao7alUSMIpXwIUF89RptYgQlXCMmNDwOcuCZ1YKxqaLLcbsIrH8A9dXiJ8DVNx2MzIMN6O77wGOqUBIJNN3tPe1AU7lbBb5R44jL%2BHjQE%2FLmpPYNtpc11ocf8ZSD0UKIFhhZuSX%2F1qcOpFqm6jvby9r5EybJNugFDLHZMmpoGX3ufAgyhSluC3rXKE2TiWDl6EOckWj5KWQiOsdIDf3SqFRaG%2BqIL1rnfd2bLMx9ayiuV7QfpD6IU76KqbW6CG7sCvUIhsBJ65WatGAQoEoQUVZHFYT4j9TIRPKalcj54u&X-Amz-Signature=869163aec3f05202494420bafc8a9d71230e987718b5f6a317f87451a44f43cc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46643RWEQMW%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEzWldGzgCXzjGT0H3xY5ChABENIX013a88FD3NtZfJoAiEAqjwH28JPrr2Iacs6tIrzDESISIQntw9%2FvAOPmXTBL3AqiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHE4CfwfhummVwloNSrcA5KJ3qnYIAAAxQtGDnprA2gLXY3PExO9BNPQiBfD60Nb3smXO5Y2uijmB6D50q36YFMzhCgiCKAMe3YRJ0bXTtEVpp%2FnoQq1hrBO8Hod%2Fgoi46jMW8VQtDlWVQMzxQoQ7UyJjHwLKcB25Fuo4TTayOEw8V0pE41Kip2%2FagM9T5tQISupvU9jwleNYnw6s2zyIyCUh313h69RWQs8R14tIZJMWR%2FE9TIq%2BGZQalzcZ0OJNr7LCGPSuQS4OqdTfGUklY%2FeiiFqhiyovvTVqXwnLcWKV%2Fic%2BigbNtcyENb8zMWsk%2B6IbnMx2iH6a5PrvwsPuEsJgVkINUUXGvh6Ig4ZGZ2oz23IMqVJl2B50sCeRqD0BCeSamQZSAKIjZPDbkzYvB4il0DtsOrKBk9jvFkJVRdVFjmpcFtZooqj%2B5Vcd%2FwvBX6PDTC4tz9M%2BINBBnJnEVv8gpsshlLApfCetSyVqWFZgML5dT4uL9Eqjiwv9BkTrMMtSPp%2F5fUOPzlVFZJI3RdP9xcjotDaPCdMNO8HqLkC8BWZ5XDtv73P9Jnqcj6Qgie3ltNZB%2BvjjuTIW3gUYawSlhcwoi9HQqvLSI8YEnTyOtSuHa8cijAaNHols%2FlygCTt41wOwJrsAOc0MPCN77wGOqUBiV9SS84zYuUtYeEDmJCuVY8OyqX3kiN8bEwPjoe%2FUMrLvK0vBa85Ry1zzDUrIGm4ng1sj2IiYzVYR9Rf2dHC1cdN%2BrP5aWCQ0w3pL5wg0YCNWP3PBgLKm2jjUAl9MPeMo08G6lmx49FatCpBxPSaQ5jSaGTAG%2Bh19bqpzSxOb93rI%2Biha6pBUeVif8mHy9h55ejTiYSwI6mpMJeQUgDfy4fReo0U&X-Amz-Signature=487fe2066f78fa47300e3dd787ff1aa85da45d95b1e9b13cd90aa3174a3b3c3d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46643RWEQMW%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEzWldGzgCXzjGT0H3xY5ChABENIX013a88FD3NtZfJoAiEAqjwH28JPrr2Iacs6tIrzDESISIQntw9%2FvAOPmXTBL3AqiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHE4CfwfhummVwloNSrcA5KJ3qnYIAAAxQtGDnprA2gLXY3PExO9BNPQiBfD60Nb3smXO5Y2uijmB6D50q36YFMzhCgiCKAMe3YRJ0bXTtEVpp%2FnoQq1hrBO8Hod%2Fgoi46jMW8VQtDlWVQMzxQoQ7UyJjHwLKcB25Fuo4TTayOEw8V0pE41Kip2%2FagM9T5tQISupvU9jwleNYnw6s2zyIyCUh313h69RWQs8R14tIZJMWR%2FE9TIq%2BGZQalzcZ0OJNr7LCGPSuQS4OqdTfGUklY%2FeiiFqhiyovvTVqXwnLcWKV%2Fic%2BigbNtcyENb8zMWsk%2B6IbnMx2iH6a5PrvwsPuEsJgVkINUUXGvh6Ig4ZGZ2oz23IMqVJl2B50sCeRqD0BCeSamQZSAKIjZPDbkzYvB4il0DtsOrKBk9jvFkJVRdVFjmpcFtZooqj%2B5Vcd%2FwvBX6PDTC4tz9M%2BINBBnJnEVv8gpsshlLApfCetSyVqWFZgML5dT4uL9Eqjiwv9BkTrMMtSPp%2F5fUOPzlVFZJI3RdP9xcjotDaPCdMNO8HqLkC8BWZ5XDtv73P9Jnqcj6Qgie3ltNZB%2BvjjuTIW3gUYawSlhcwoi9HQqvLSI8YEnTyOtSuHa8cijAaNHols%2FlygCTt41wOwJrsAOc0MPCN77wGOqUBiV9SS84zYuUtYeEDmJCuVY8OyqX3kiN8bEwPjoe%2FUMrLvK0vBa85Ry1zzDUrIGm4ng1sj2IiYzVYR9Rf2dHC1cdN%2BrP5aWCQ0w3pL5wg0YCNWP3PBgLKm2jjUAl9MPeMo08G6lmx49FatCpBxPSaQ5jSaGTAG%2Bh19bqpzSxOb93rI%2Biha6pBUeVif8mHy9h55ejTiYSwI6mpMJeQUgDfy4fReo0U&X-Amz-Signature=97f6c823bcc7a4eeb4bb3496b97f292ccd5a251e15d6778c57bd32898345830d&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
