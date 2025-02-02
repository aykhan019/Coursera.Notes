

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664L2DJOZ4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T131500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBluc9fQaluoyQL4ZrAHpMCWCmlGWFoqz00c%2BJWBKmVFAiAOTVNTrN9es4729Gbl5WFhbMyIXkcss214cxolWLjg%2FSqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8TAaJv%2FgOS14h8OcKtwDZ7qYlZNBcrc2J5KJPXUttdDj%2F%2FjxYUaiCx3XX3SIYNycY0MSZN%2BXvOEJXGXiz%2FeLpmd0oji4%2B12QHnxBD93m4t1LX4nqFA13IqHzMiVGYVntMktcEh1G%2BlFa9eVLQteANnBwDB8WnObPsievxkcPElK5oHdAiu8XXK298931uTnvcOR6JKV7I%2BYQs8UUhReHrTmFcVp%2B8rpush7rfz3CTYpNYL7FC33Bcqcn%2Bm7AIpXp3aGvL4gKDU7%2FWdux%2FWlaKPRBusWxVQf%2FHAeUlYPd6Xa%2FodXWnA8uAUy38tBSRTL6UIYeB3l9LzaFZnWpLmq9XmYAxBhpePQOaDppeGc1fHShQv%2BloXzNbYBiojG152giZrlIVohCXlkBrUu3QdtsGifGdU2tTUZj7VOODDAWjXpt8AQK4cuhr8vqEWvrgVgYG9MDFwss5BH1ZZIAU2ztLgOOdnFD5fMC7QUuaZw3NPIVqiZSVCcwlrOueJIHTjcDD8AVKJi%2Fiz%2BO4JihHZMqV5nT0pA0H3QuAs584Aussn0TnTKUE4fBjHqj8O782FjqgQcEytwNChpyCaiOrR5bKgfYnv%2FLxpkN%2Blar7jTnsTUFoqrEZ4m2ByMJ5uoqEBVzkQXpoZ94O080rQQwr7z9vAY6pgFhDfke9RMrDT1vLTmI2aF%2BiRzZI1Rvuukvx7bVlHKBcRaMN%2Bc9Thmk516QgCe18lwfAl2mw6Ciw93Z%2Fb5vEKUWZrUeFglXU68epJzODEotJ%2BUCrYpBiYgR9GyifxuwpbH77TGjDHI8zoF%2FdudnOvgGkIQIwLQqSmQlyqT%2BotiwIXXy9arpKlNqKZ7aO07V5KXoPhG8VNiIEXmqVWXZNIcBvpd0LYTg&X-Amz-Signature=e0d1e0dad233ea59fa9a9234d0c2d2a16c1904b4dac37fbba272b041d5e41999&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664L2DJOZ4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T131500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBluc9fQaluoyQL4ZrAHpMCWCmlGWFoqz00c%2BJWBKmVFAiAOTVNTrN9es4729Gbl5WFhbMyIXkcss214cxolWLjg%2FSqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8TAaJv%2FgOS14h8OcKtwDZ7qYlZNBcrc2J5KJPXUttdDj%2F%2FjxYUaiCx3XX3SIYNycY0MSZN%2BXvOEJXGXiz%2FeLpmd0oji4%2B12QHnxBD93m4t1LX4nqFA13IqHzMiVGYVntMktcEh1G%2BlFa9eVLQteANnBwDB8WnObPsievxkcPElK5oHdAiu8XXK298931uTnvcOR6JKV7I%2BYQs8UUhReHrTmFcVp%2B8rpush7rfz3CTYpNYL7FC33Bcqcn%2Bm7AIpXp3aGvL4gKDU7%2FWdux%2FWlaKPRBusWxVQf%2FHAeUlYPd6Xa%2FodXWnA8uAUy38tBSRTL6UIYeB3l9LzaFZnWpLmq9XmYAxBhpePQOaDppeGc1fHShQv%2BloXzNbYBiojG152giZrlIVohCXlkBrUu3QdtsGifGdU2tTUZj7VOODDAWjXpt8AQK4cuhr8vqEWvrgVgYG9MDFwss5BH1ZZIAU2ztLgOOdnFD5fMC7QUuaZw3NPIVqiZSVCcwlrOueJIHTjcDD8AVKJi%2Fiz%2BO4JihHZMqV5nT0pA0H3QuAs584Aussn0TnTKUE4fBjHqj8O782FjqgQcEytwNChpyCaiOrR5bKgfYnv%2FLxpkN%2Blar7jTnsTUFoqrEZ4m2ByMJ5uoqEBVzkQXpoZ94O080rQQwr7z9vAY6pgFhDfke9RMrDT1vLTmI2aF%2BiRzZI1Rvuukvx7bVlHKBcRaMN%2Bc9Thmk516QgCe18lwfAl2mw6Ciw93Z%2Fb5vEKUWZrUeFglXU68epJzODEotJ%2BUCrYpBiYgR9GyifxuwpbH77TGjDHI8zoF%2FdudnOvgGkIQIwLQqSmQlyqT%2BotiwIXXy9arpKlNqKZ7aO07V5KXoPhG8VNiIEXmqVWXZNIcBvpd0LYTg&X-Amz-Signature=913d5a81b57eb3a715e71cf1f0dce74c0b1c9c0e7c388db513d2b6e91c530637&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664L2DJOZ4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T131500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBluc9fQaluoyQL4ZrAHpMCWCmlGWFoqz00c%2BJWBKmVFAiAOTVNTrN9es4729Gbl5WFhbMyIXkcss214cxolWLjg%2FSqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8TAaJv%2FgOS14h8OcKtwDZ7qYlZNBcrc2J5KJPXUttdDj%2F%2FjxYUaiCx3XX3SIYNycY0MSZN%2BXvOEJXGXiz%2FeLpmd0oji4%2B12QHnxBD93m4t1LX4nqFA13IqHzMiVGYVntMktcEh1G%2BlFa9eVLQteANnBwDB8WnObPsievxkcPElK5oHdAiu8XXK298931uTnvcOR6JKV7I%2BYQs8UUhReHrTmFcVp%2B8rpush7rfz3CTYpNYL7FC33Bcqcn%2Bm7AIpXp3aGvL4gKDU7%2FWdux%2FWlaKPRBusWxVQf%2FHAeUlYPd6Xa%2FodXWnA8uAUy38tBSRTL6UIYeB3l9LzaFZnWpLmq9XmYAxBhpePQOaDppeGc1fHShQv%2BloXzNbYBiojG152giZrlIVohCXlkBrUu3QdtsGifGdU2tTUZj7VOODDAWjXpt8AQK4cuhr8vqEWvrgVgYG9MDFwss5BH1ZZIAU2ztLgOOdnFD5fMC7QUuaZw3NPIVqiZSVCcwlrOueJIHTjcDD8AVKJi%2Fiz%2BO4JihHZMqV5nT0pA0H3QuAs584Aussn0TnTKUE4fBjHqj8O782FjqgQcEytwNChpyCaiOrR5bKgfYnv%2FLxpkN%2Blar7jTnsTUFoqrEZ4m2ByMJ5uoqEBVzkQXpoZ94O080rQQwr7z9vAY6pgFhDfke9RMrDT1vLTmI2aF%2BiRzZI1Rvuukvx7bVlHKBcRaMN%2Bc9Thmk516QgCe18lwfAl2mw6Ciw93Z%2Fb5vEKUWZrUeFglXU68epJzODEotJ%2BUCrYpBiYgR9GyifxuwpbH77TGjDHI8zoF%2FdudnOvgGkIQIwLQqSmQlyqT%2BotiwIXXy9arpKlNqKZ7aO07V5KXoPhG8VNiIEXmqVWXZNIcBvpd0LYTg&X-Amz-Signature=fb1fc512e3e7650e96a73e9f70420a4df4c351d5d87d6362d6dd8d32e90e8f80&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664L2DJOZ4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T131500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBluc9fQaluoyQL4ZrAHpMCWCmlGWFoqz00c%2BJWBKmVFAiAOTVNTrN9es4729Gbl5WFhbMyIXkcss214cxolWLjg%2FSqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8TAaJv%2FgOS14h8OcKtwDZ7qYlZNBcrc2J5KJPXUttdDj%2F%2FjxYUaiCx3XX3SIYNycY0MSZN%2BXvOEJXGXiz%2FeLpmd0oji4%2B12QHnxBD93m4t1LX4nqFA13IqHzMiVGYVntMktcEh1G%2BlFa9eVLQteANnBwDB8WnObPsievxkcPElK5oHdAiu8XXK298931uTnvcOR6JKV7I%2BYQs8UUhReHrTmFcVp%2B8rpush7rfz3CTYpNYL7FC33Bcqcn%2Bm7AIpXp3aGvL4gKDU7%2FWdux%2FWlaKPRBusWxVQf%2FHAeUlYPd6Xa%2FodXWnA8uAUy38tBSRTL6UIYeB3l9LzaFZnWpLmq9XmYAxBhpePQOaDppeGc1fHShQv%2BloXzNbYBiojG152giZrlIVohCXlkBrUu3QdtsGifGdU2tTUZj7VOODDAWjXpt8AQK4cuhr8vqEWvrgVgYG9MDFwss5BH1ZZIAU2ztLgOOdnFD5fMC7QUuaZw3NPIVqiZSVCcwlrOueJIHTjcDD8AVKJi%2Fiz%2BO4JihHZMqV5nT0pA0H3QuAs584Aussn0TnTKUE4fBjHqj8O782FjqgQcEytwNChpyCaiOrR5bKgfYnv%2FLxpkN%2Blar7jTnsTUFoqrEZ4m2ByMJ5uoqEBVzkQXpoZ94O080rQQwr7z9vAY6pgFhDfke9RMrDT1vLTmI2aF%2BiRzZI1Rvuukvx7bVlHKBcRaMN%2Bc9Thmk516QgCe18lwfAl2mw6Ciw93Z%2Fb5vEKUWZrUeFglXU68epJzODEotJ%2BUCrYpBiYgR9GyifxuwpbH77TGjDHI8zoF%2FdudnOvgGkIQIwLQqSmQlyqT%2BotiwIXXy9arpKlNqKZ7aO07V5KXoPhG8VNiIEXmqVWXZNIcBvpd0LYTg&X-Amz-Signature=123fe54876b1d8709d96dd690c0bf562939ef658ea87370f0b8bd0b53adfee2b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664L2DJOZ4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T131500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBluc9fQaluoyQL4ZrAHpMCWCmlGWFoqz00c%2BJWBKmVFAiAOTVNTrN9es4729Gbl5WFhbMyIXkcss214cxolWLjg%2FSqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8TAaJv%2FgOS14h8OcKtwDZ7qYlZNBcrc2J5KJPXUttdDj%2F%2FjxYUaiCx3XX3SIYNycY0MSZN%2BXvOEJXGXiz%2FeLpmd0oji4%2B12QHnxBD93m4t1LX4nqFA13IqHzMiVGYVntMktcEh1G%2BlFa9eVLQteANnBwDB8WnObPsievxkcPElK5oHdAiu8XXK298931uTnvcOR6JKV7I%2BYQs8UUhReHrTmFcVp%2B8rpush7rfz3CTYpNYL7FC33Bcqcn%2Bm7AIpXp3aGvL4gKDU7%2FWdux%2FWlaKPRBusWxVQf%2FHAeUlYPd6Xa%2FodXWnA8uAUy38tBSRTL6UIYeB3l9LzaFZnWpLmq9XmYAxBhpePQOaDppeGc1fHShQv%2BloXzNbYBiojG152giZrlIVohCXlkBrUu3QdtsGifGdU2tTUZj7VOODDAWjXpt8AQK4cuhr8vqEWvrgVgYG9MDFwss5BH1ZZIAU2ztLgOOdnFD5fMC7QUuaZw3NPIVqiZSVCcwlrOueJIHTjcDD8AVKJi%2Fiz%2BO4JihHZMqV5nT0pA0H3QuAs584Aussn0TnTKUE4fBjHqj8O782FjqgQcEytwNChpyCaiOrR5bKgfYnv%2FLxpkN%2Blar7jTnsTUFoqrEZ4m2ByMJ5uoqEBVzkQXpoZ94O080rQQwr7z9vAY6pgFhDfke9RMrDT1vLTmI2aF%2BiRzZI1Rvuukvx7bVlHKBcRaMN%2Bc9Thmk516QgCe18lwfAl2mw6Ciw93Z%2Fb5vEKUWZrUeFglXU68epJzODEotJ%2BUCrYpBiYgR9GyifxuwpbH77TGjDHI8zoF%2FdudnOvgGkIQIwLQqSmQlyqT%2BotiwIXXy9arpKlNqKZ7aO07V5KXoPhG8VNiIEXmqVWXZNIcBvpd0LYTg&X-Amz-Signature=87654eef86b3bb4918720b7c6c2122465fef0daaa30d427662ebdefc0725b902&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664L2DJOZ4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T131500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBluc9fQaluoyQL4ZrAHpMCWCmlGWFoqz00c%2BJWBKmVFAiAOTVNTrN9es4729Gbl5WFhbMyIXkcss214cxolWLjg%2FSqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8TAaJv%2FgOS14h8OcKtwDZ7qYlZNBcrc2J5KJPXUttdDj%2F%2FjxYUaiCx3XX3SIYNycY0MSZN%2BXvOEJXGXiz%2FeLpmd0oji4%2B12QHnxBD93m4t1LX4nqFA13IqHzMiVGYVntMktcEh1G%2BlFa9eVLQteANnBwDB8WnObPsievxkcPElK5oHdAiu8XXK298931uTnvcOR6JKV7I%2BYQs8UUhReHrTmFcVp%2B8rpush7rfz3CTYpNYL7FC33Bcqcn%2Bm7AIpXp3aGvL4gKDU7%2FWdux%2FWlaKPRBusWxVQf%2FHAeUlYPd6Xa%2FodXWnA8uAUy38tBSRTL6UIYeB3l9LzaFZnWpLmq9XmYAxBhpePQOaDppeGc1fHShQv%2BloXzNbYBiojG152giZrlIVohCXlkBrUu3QdtsGifGdU2tTUZj7VOODDAWjXpt8AQK4cuhr8vqEWvrgVgYG9MDFwss5BH1ZZIAU2ztLgOOdnFD5fMC7QUuaZw3NPIVqiZSVCcwlrOueJIHTjcDD8AVKJi%2Fiz%2BO4JihHZMqV5nT0pA0H3QuAs584Aussn0TnTKUE4fBjHqj8O782FjqgQcEytwNChpyCaiOrR5bKgfYnv%2FLxpkN%2Blar7jTnsTUFoqrEZ4m2ByMJ5uoqEBVzkQXpoZ94O080rQQwr7z9vAY6pgFhDfke9RMrDT1vLTmI2aF%2BiRzZI1Rvuukvx7bVlHKBcRaMN%2Bc9Thmk516QgCe18lwfAl2mw6Ciw93Z%2Fb5vEKUWZrUeFglXU68epJzODEotJ%2BUCrYpBiYgR9GyifxuwpbH77TGjDHI8zoF%2FdudnOvgGkIQIwLQqSmQlyqT%2BotiwIXXy9arpKlNqKZ7aO07V5KXoPhG8VNiIEXmqVWXZNIcBvpd0LYTg&X-Amz-Signature=1a2a6a36e7f14e6ab90f6c1ad2b397daccafa13a4224adec21617fc90e5a9480&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664L2DJOZ4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T131500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBluc9fQaluoyQL4ZrAHpMCWCmlGWFoqz00c%2BJWBKmVFAiAOTVNTrN9es4729Gbl5WFhbMyIXkcss214cxolWLjg%2FSqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8TAaJv%2FgOS14h8OcKtwDZ7qYlZNBcrc2J5KJPXUttdDj%2F%2FjxYUaiCx3XX3SIYNycY0MSZN%2BXvOEJXGXiz%2FeLpmd0oji4%2B12QHnxBD93m4t1LX4nqFA13IqHzMiVGYVntMktcEh1G%2BlFa9eVLQteANnBwDB8WnObPsievxkcPElK5oHdAiu8XXK298931uTnvcOR6JKV7I%2BYQs8UUhReHrTmFcVp%2B8rpush7rfz3CTYpNYL7FC33Bcqcn%2Bm7AIpXp3aGvL4gKDU7%2FWdux%2FWlaKPRBusWxVQf%2FHAeUlYPd6Xa%2FodXWnA8uAUy38tBSRTL6UIYeB3l9LzaFZnWpLmq9XmYAxBhpePQOaDppeGc1fHShQv%2BloXzNbYBiojG152giZrlIVohCXlkBrUu3QdtsGifGdU2tTUZj7VOODDAWjXpt8AQK4cuhr8vqEWvrgVgYG9MDFwss5BH1ZZIAU2ztLgOOdnFD5fMC7QUuaZw3NPIVqiZSVCcwlrOueJIHTjcDD8AVKJi%2Fiz%2BO4JihHZMqV5nT0pA0H3QuAs584Aussn0TnTKUE4fBjHqj8O782FjqgQcEytwNChpyCaiOrR5bKgfYnv%2FLxpkN%2Blar7jTnsTUFoqrEZ4m2ByMJ5uoqEBVzkQXpoZ94O080rQQwr7z9vAY6pgFhDfke9RMrDT1vLTmI2aF%2BiRzZI1Rvuukvx7bVlHKBcRaMN%2Bc9Thmk516QgCe18lwfAl2mw6Ciw93Z%2Fb5vEKUWZrUeFglXU68epJzODEotJ%2BUCrYpBiYgR9GyifxuwpbH77TGjDHI8zoF%2FdudnOvgGkIQIwLQqSmQlyqT%2BotiwIXXy9arpKlNqKZ7aO07V5KXoPhG8VNiIEXmqVWXZNIcBvpd0LYTg&X-Amz-Signature=b4c7f2cbd39174c91dc8cf30f86f02bbf28ad0e41ed8df89165678cbe69d6f02&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664L2DJOZ4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T131500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBluc9fQaluoyQL4ZrAHpMCWCmlGWFoqz00c%2BJWBKmVFAiAOTVNTrN9es4729Gbl5WFhbMyIXkcss214cxolWLjg%2FSqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8TAaJv%2FgOS14h8OcKtwDZ7qYlZNBcrc2J5KJPXUttdDj%2F%2FjxYUaiCx3XX3SIYNycY0MSZN%2BXvOEJXGXiz%2FeLpmd0oji4%2B12QHnxBD93m4t1LX4nqFA13IqHzMiVGYVntMktcEh1G%2BlFa9eVLQteANnBwDB8WnObPsievxkcPElK5oHdAiu8XXK298931uTnvcOR6JKV7I%2BYQs8UUhReHrTmFcVp%2B8rpush7rfz3CTYpNYL7FC33Bcqcn%2Bm7AIpXp3aGvL4gKDU7%2FWdux%2FWlaKPRBusWxVQf%2FHAeUlYPd6Xa%2FodXWnA8uAUy38tBSRTL6UIYeB3l9LzaFZnWpLmq9XmYAxBhpePQOaDppeGc1fHShQv%2BloXzNbYBiojG152giZrlIVohCXlkBrUu3QdtsGifGdU2tTUZj7VOODDAWjXpt8AQK4cuhr8vqEWvrgVgYG9MDFwss5BH1ZZIAU2ztLgOOdnFD5fMC7QUuaZw3NPIVqiZSVCcwlrOueJIHTjcDD8AVKJi%2Fiz%2BO4JihHZMqV5nT0pA0H3QuAs584Aussn0TnTKUE4fBjHqj8O782FjqgQcEytwNChpyCaiOrR5bKgfYnv%2FLxpkN%2Blar7jTnsTUFoqrEZ4m2ByMJ5uoqEBVzkQXpoZ94O080rQQwr7z9vAY6pgFhDfke9RMrDT1vLTmI2aF%2BiRzZI1Rvuukvx7bVlHKBcRaMN%2Bc9Thmk516QgCe18lwfAl2mw6Ciw93Z%2Fb5vEKUWZrUeFglXU68epJzODEotJ%2BUCrYpBiYgR9GyifxuwpbH77TGjDHI8zoF%2FdudnOvgGkIQIwLQqSmQlyqT%2BotiwIXXy9arpKlNqKZ7aO07V5KXoPhG8VNiIEXmqVWXZNIcBvpd0LYTg&X-Amz-Signature=8bb6dccd87407afece4a9c3e083031173a93bd65be40b3222e396d2066a39765&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664L2DJOZ4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T131500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBluc9fQaluoyQL4ZrAHpMCWCmlGWFoqz00c%2BJWBKmVFAiAOTVNTrN9es4729Gbl5WFhbMyIXkcss214cxolWLjg%2FSqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8TAaJv%2FgOS14h8OcKtwDZ7qYlZNBcrc2J5KJPXUttdDj%2F%2FjxYUaiCx3XX3SIYNycY0MSZN%2BXvOEJXGXiz%2FeLpmd0oji4%2B12QHnxBD93m4t1LX4nqFA13IqHzMiVGYVntMktcEh1G%2BlFa9eVLQteANnBwDB8WnObPsievxkcPElK5oHdAiu8XXK298931uTnvcOR6JKV7I%2BYQs8UUhReHrTmFcVp%2B8rpush7rfz3CTYpNYL7FC33Bcqcn%2Bm7AIpXp3aGvL4gKDU7%2FWdux%2FWlaKPRBusWxVQf%2FHAeUlYPd6Xa%2FodXWnA8uAUy38tBSRTL6UIYeB3l9LzaFZnWpLmq9XmYAxBhpePQOaDppeGc1fHShQv%2BloXzNbYBiojG152giZrlIVohCXlkBrUu3QdtsGifGdU2tTUZj7VOODDAWjXpt8AQK4cuhr8vqEWvrgVgYG9MDFwss5BH1ZZIAU2ztLgOOdnFD5fMC7QUuaZw3NPIVqiZSVCcwlrOueJIHTjcDD8AVKJi%2Fiz%2BO4JihHZMqV5nT0pA0H3QuAs584Aussn0TnTKUE4fBjHqj8O782FjqgQcEytwNChpyCaiOrR5bKgfYnv%2FLxpkN%2Blar7jTnsTUFoqrEZ4m2ByMJ5uoqEBVzkQXpoZ94O080rQQwr7z9vAY6pgFhDfke9RMrDT1vLTmI2aF%2BiRzZI1Rvuukvx7bVlHKBcRaMN%2Bc9Thmk516QgCe18lwfAl2mw6Ciw93Z%2Fb5vEKUWZrUeFglXU68epJzODEotJ%2BUCrYpBiYgR9GyifxuwpbH77TGjDHI8zoF%2FdudnOvgGkIQIwLQqSmQlyqT%2BotiwIXXy9arpKlNqKZ7aO07V5KXoPhG8VNiIEXmqVWXZNIcBvpd0LYTg&X-Amz-Signature=018778072e1b76712cfad679f61a31093fb37b43b198911f5a0e54574d701c0b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VUPOHH5R%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T131501Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCI9i%2Btd0eL4o4b%2B5QgcfmnbmKwI13nkWyhvGI%2Bhlcw9AIgM7oKmWWI7ujhYvjKC9FaFMofC4VxbiHV6bjPnM5IsWQqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHSnh9vGZgox0jpn9ircA5h7DvtzY21%2FfatfzLm9bZ5OwWxbuPtdn5epJaqDKSHgqxKGoJSRQywFJo3Ua6zhgjpkFfNm%2B1uF%2B%2BBX%2BWQFpJi6H381vJp0KpbuFLrbytMfqGq4kBXa7Qo8kKvPxzWj0rekEtueVcnmDenXjaQWzsoAy4LnrwjnAKEuu8oUixrBS7a3XunGmDBAfgOTI%2Bqmbv7HfsyfXPTJk7JsKDHbob8SG2n86%2F32pYC1TbQ6g25KTNKOFAF4Ka%2BuLrjYqHoEo1wI2kboCyTYGx5vDVtO6d94bGbNsGgSB88CQdba37dDTDu%2BIbgq72CPGqgfA%2BgR%2FlMAvWKtuqwFLWr1yCRzNm1vzubVmW%2BX66CdWZl1QKYSOkAqynP%2F%2Ba%2B09Eu%2B%2B4bMnioc0tZ0SaD4DRLgkw2L7tNEZjnXdJOW3EAGDkhklg2ZgHQg%2FpirWvLJRdrJOcy16a33ygm%2F%2FTrIkYXAz1ePdr06Ww4tOE827HWN0Hos68HN50g4SRryvMnqYcvT9tQZB4GBYgHUCgVyEGrwh%2BEhVFAy5ZctQVJ4WgUByJ%2B5Cwutzy1XI4FQzSpD9WM%2B5jbJe%2BwMfnxZucOFW3IjpxcacOlSct%2BnN7sYH4Ms5RnXjedewohKDv7MKebcMUYDMLC9%2FbwGOqUBbqiHdRdRjeT3cvvI7zvhw5RmhvZdrQpIBifVOzN6Isk39F9scXA7z2ksBTV0UyyCO0BvTdtf%2FUNkQW7ZA1gg26jW4pimKpflhlVKVdMF77vFl0Zn47Ab89oJqG0SByTQvhApg6HD%2F3azxB3g2OXK0s7oeP2M6Ryc1eXSwiNpHTUVd467Ty5j5fnfw9ZdBzKlFsMuuyTzZIk3LdGMBGrskZBs99sx&X-Amz-Signature=fe9861a9b63076aea38a81e3760666aabcc2c5426e13333685676aa689b37112&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VUPOHH5R%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T131501Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCI9i%2Btd0eL4o4b%2B5QgcfmnbmKwI13nkWyhvGI%2Bhlcw9AIgM7oKmWWI7ujhYvjKC9FaFMofC4VxbiHV6bjPnM5IsWQqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHSnh9vGZgox0jpn9ircA5h7DvtzY21%2FfatfzLm9bZ5OwWxbuPtdn5epJaqDKSHgqxKGoJSRQywFJo3Ua6zhgjpkFfNm%2B1uF%2B%2BBX%2BWQFpJi6H381vJp0KpbuFLrbytMfqGq4kBXa7Qo8kKvPxzWj0rekEtueVcnmDenXjaQWzsoAy4LnrwjnAKEuu8oUixrBS7a3XunGmDBAfgOTI%2Bqmbv7HfsyfXPTJk7JsKDHbob8SG2n86%2F32pYC1TbQ6g25KTNKOFAF4Ka%2BuLrjYqHoEo1wI2kboCyTYGx5vDVtO6d94bGbNsGgSB88CQdba37dDTDu%2BIbgq72CPGqgfA%2BgR%2FlMAvWKtuqwFLWr1yCRzNm1vzubVmW%2BX66CdWZl1QKYSOkAqynP%2F%2Ba%2B09Eu%2B%2B4bMnioc0tZ0SaD4DRLgkw2L7tNEZjnXdJOW3EAGDkhklg2ZgHQg%2FpirWvLJRdrJOcy16a33ygm%2F%2FTrIkYXAz1ePdr06Ww4tOE827HWN0Hos68HN50g4SRryvMnqYcvT9tQZB4GBYgHUCgVyEGrwh%2BEhVFAy5ZctQVJ4WgUByJ%2B5Cwutzy1XI4FQzSpD9WM%2B5jbJe%2BwMfnxZucOFW3IjpxcacOlSct%2BnN7sYH4Ms5RnXjedewohKDv7MKebcMUYDMLC9%2FbwGOqUBbqiHdRdRjeT3cvvI7zvhw5RmhvZdrQpIBifVOzN6Isk39F9scXA7z2ksBTV0UyyCO0BvTdtf%2FUNkQW7ZA1gg26jW4pimKpflhlVKVdMF77vFl0Zn47Ab89oJqG0SByTQvhApg6HD%2F3azxB3g2OXK0s7oeP2M6Ryc1eXSwiNpHTUVd467Ty5j5fnfw9ZdBzKlFsMuuyTzZIk3LdGMBGrskZBs99sx&X-Amz-Signature=31978c8377ce7a580cf07da55f3eb38eb951841795a5e8ccb87f0708bfd3f093&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
