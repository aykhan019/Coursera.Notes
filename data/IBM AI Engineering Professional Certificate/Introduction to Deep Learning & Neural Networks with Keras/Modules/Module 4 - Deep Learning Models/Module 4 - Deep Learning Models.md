

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666X5G7DXJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCID4MRo3jqWBz57tiPDM1%2BTopHFIqAdwvnIashmpUWqSOAiATU28E3ZOTIhsYPMX7CMApLLdnqIZYF98xBzWdB2O03ir%2FAwgxEAAaDDYzNzQyMzE4MzgwNSIMDhOcRSElYFSJwM91KtwDIZfhpjs2KN5OWz81tFWn2bnf7eEqMEsDP%2BrpmqwrPL%2FM%2F%2FPMmRiPQRywAHD5vFp3k8n7iFwDo2ZcVd8Qzj7YDWUDTvgbWxdn6ZF3OYIFcWptBkYVjCqp0vhOjUVaboArMiRaOUJZnlNeupg6qouOTbN93sD22LY84gK4aS%2BUE2104%2FfJJWjBaL2Lun%2B0H3CivXXn9ZAtrwvjP%2F4dVoWJ4K7U9FC1PJTTn0jpcAPE4kI2VB%2BxyGgFjDv3tMJP0PrdK5hqDAie37M0%2BzlI%2FuV0WNVjW98Y2qlEs8H8Pl18UDMj9wf05AUNWB3VTux6%2BQa4K8m6gFOQAN82nWsAZX0vzaXxN6hg2WhxnEJWg6bi0Ol72RzhojOPywdXJPCnm9s2ipc4yh4kOxX4lMTTMYd8clHe%2FhaGhgsxmrnHVsxqbf3dM5GxI2eF9EItFKTAhwXUZMuv2H3ZE2%2BjVgtKydqXSd5SS%2FsstevAbfzrGoV5rBlITLgKMOnDe30%2F%2BNICDjhzoGDqkiNO8Kw6WxtmVtCmT79bqPdnqJHclbbFurnv1OAmF3Pj5WwYoR2OyBX79O0K01FqSQjZ2wGROjFkLqUfqIg1K8ZMifEKREYUA5jFhRqXiCs48v5P6CdWdE0w4eaIvQY6pgH4gC8lynyffACNu35NZ03j6YXh73sNPJLXN%2Btw%2Bve04bl0MML9PQ%2ByJlQE0MYT5sjax33N%2BoXH5qHdF0unlJOiW9fXeT85GQw%2FSJmcXx0Qhq4lucB5cUeuDmmtL5lMk0xQ8QRvIPHe9fRmNF1%2BtD%2FqfnaTSBlynty7B7JqTgL4myex6aCCN2VIy%2Fso%2F9ILiXGp%2Bl5cg%2BFJty7RuWczHzXxDgNkvh0x&X-Amz-Signature=2e9cedda709665eb43eddf9f4124a9dd75acda9831f19e2501eff74263fb8358&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666X5G7DXJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCID4MRo3jqWBz57tiPDM1%2BTopHFIqAdwvnIashmpUWqSOAiATU28E3ZOTIhsYPMX7CMApLLdnqIZYF98xBzWdB2O03ir%2FAwgxEAAaDDYzNzQyMzE4MzgwNSIMDhOcRSElYFSJwM91KtwDIZfhpjs2KN5OWz81tFWn2bnf7eEqMEsDP%2BrpmqwrPL%2FM%2F%2FPMmRiPQRywAHD5vFp3k8n7iFwDo2ZcVd8Qzj7YDWUDTvgbWxdn6ZF3OYIFcWptBkYVjCqp0vhOjUVaboArMiRaOUJZnlNeupg6qouOTbN93sD22LY84gK4aS%2BUE2104%2FfJJWjBaL2Lun%2B0H3CivXXn9ZAtrwvjP%2F4dVoWJ4K7U9FC1PJTTn0jpcAPE4kI2VB%2BxyGgFjDv3tMJP0PrdK5hqDAie37M0%2BzlI%2FuV0WNVjW98Y2qlEs8H8Pl18UDMj9wf05AUNWB3VTux6%2BQa4K8m6gFOQAN82nWsAZX0vzaXxN6hg2WhxnEJWg6bi0Ol72RzhojOPywdXJPCnm9s2ipc4yh4kOxX4lMTTMYd8clHe%2FhaGhgsxmrnHVsxqbf3dM5GxI2eF9EItFKTAhwXUZMuv2H3ZE2%2BjVgtKydqXSd5SS%2FsstevAbfzrGoV5rBlITLgKMOnDe30%2F%2BNICDjhzoGDqkiNO8Kw6WxtmVtCmT79bqPdnqJHclbbFurnv1OAmF3Pj5WwYoR2OyBX79O0K01FqSQjZ2wGROjFkLqUfqIg1K8ZMifEKREYUA5jFhRqXiCs48v5P6CdWdE0w4eaIvQY6pgH4gC8lynyffACNu35NZ03j6YXh73sNPJLXN%2Btw%2Bve04bl0MML9PQ%2ByJlQE0MYT5sjax33N%2BoXH5qHdF0unlJOiW9fXeT85GQw%2FSJmcXx0Qhq4lucB5cUeuDmmtL5lMk0xQ8QRvIPHe9fRmNF1%2BtD%2FqfnaTSBlynty7B7JqTgL4myex6aCCN2VIy%2Fso%2F9ILiXGp%2Bl5cg%2BFJty7RuWczHzXxDgNkvh0x&X-Amz-Signature=632e304225e4f24e0cbd389bf860cf347b04d98c7199b60c7cccd3322106b8c3&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666X5G7DXJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCID4MRo3jqWBz57tiPDM1%2BTopHFIqAdwvnIashmpUWqSOAiATU28E3ZOTIhsYPMX7CMApLLdnqIZYF98xBzWdB2O03ir%2FAwgxEAAaDDYzNzQyMzE4MzgwNSIMDhOcRSElYFSJwM91KtwDIZfhpjs2KN5OWz81tFWn2bnf7eEqMEsDP%2BrpmqwrPL%2FM%2F%2FPMmRiPQRywAHD5vFp3k8n7iFwDo2ZcVd8Qzj7YDWUDTvgbWxdn6ZF3OYIFcWptBkYVjCqp0vhOjUVaboArMiRaOUJZnlNeupg6qouOTbN93sD22LY84gK4aS%2BUE2104%2FfJJWjBaL2Lun%2B0H3CivXXn9ZAtrwvjP%2F4dVoWJ4K7U9FC1PJTTn0jpcAPE4kI2VB%2BxyGgFjDv3tMJP0PrdK5hqDAie37M0%2BzlI%2FuV0WNVjW98Y2qlEs8H8Pl18UDMj9wf05AUNWB3VTux6%2BQa4K8m6gFOQAN82nWsAZX0vzaXxN6hg2WhxnEJWg6bi0Ol72RzhojOPywdXJPCnm9s2ipc4yh4kOxX4lMTTMYd8clHe%2FhaGhgsxmrnHVsxqbf3dM5GxI2eF9EItFKTAhwXUZMuv2H3ZE2%2BjVgtKydqXSd5SS%2FsstevAbfzrGoV5rBlITLgKMOnDe30%2F%2BNICDjhzoGDqkiNO8Kw6WxtmVtCmT79bqPdnqJHclbbFurnv1OAmF3Pj5WwYoR2OyBX79O0K01FqSQjZ2wGROjFkLqUfqIg1K8ZMifEKREYUA5jFhRqXiCs48v5P6CdWdE0w4eaIvQY6pgH4gC8lynyffACNu35NZ03j6YXh73sNPJLXN%2Btw%2Bve04bl0MML9PQ%2ByJlQE0MYT5sjax33N%2BoXH5qHdF0unlJOiW9fXeT85GQw%2FSJmcXx0Qhq4lucB5cUeuDmmtL5lMk0xQ8QRvIPHe9fRmNF1%2BtD%2FqfnaTSBlynty7B7JqTgL4myex6aCCN2VIy%2Fso%2F9ILiXGp%2Bl5cg%2BFJty7RuWczHzXxDgNkvh0x&X-Amz-Signature=b34cc1a879912578309a62b49ec90707d235f0d5d2647c938523fcb8512e6e06&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666X5G7DXJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCID4MRo3jqWBz57tiPDM1%2BTopHFIqAdwvnIashmpUWqSOAiATU28E3ZOTIhsYPMX7CMApLLdnqIZYF98xBzWdB2O03ir%2FAwgxEAAaDDYzNzQyMzE4MzgwNSIMDhOcRSElYFSJwM91KtwDIZfhpjs2KN5OWz81tFWn2bnf7eEqMEsDP%2BrpmqwrPL%2FM%2F%2FPMmRiPQRywAHD5vFp3k8n7iFwDo2ZcVd8Qzj7YDWUDTvgbWxdn6ZF3OYIFcWptBkYVjCqp0vhOjUVaboArMiRaOUJZnlNeupg6qouOTbN93sD22LY84gK4aS%2BUE2104%2FfJJWjBaL2Lun%2B0H3CivXXn9ZAtrwvjP%2F4dVoWJ4K7U9FC1PJTTn0jpcAPE4kI2VB%2BxyGgFjDv3tMJP0PrdK5hqDAie37M0%2BzlI%2FuV0WNVjW98Y2qlEs8H8Pl18UDMj9wf05AUNWB3VTux6%2BQa4K8m6gFOQAN82nWsAZX0vzaXxN6hg2WhxnEJWg6bi0Ol72RzhojOPywdXJPCnm9s2ipc4yh4kOxX4lMTTMYd8clHe%2FhaGhgsxmrnHVsxqbf3dM5GxI2eF9EItFKTAhwXUZMuv2H3ZE2%2BjVgtKydqXSd5SS%2FsstevAbfzrGoV5rBlITLgKMOnDe30%2F%2BNICDjhzoGDqkiNO8Kw6WxtmVtCmT79bqPdnqJHclbbFurnv1OAmF3Pj5WwYoR2OyBX79O0K01FqSQjZ2wGROjFkLqUfqIg1K8ZMifEKREYUA5jFhRqXiCs48v5P6CdWdE0w4eaIvQY6pgH4gC8lynyffACNu35NZ03j6YXh73sNPJLXN%2Btw%2Bve04bl0MML9PQ%2ByJlQE0MYT5sjax33N%2BoXH5qHdF0unlJOiW9fXeT85GQw%2FSJmcXx0Qhq4lucB5cUeuDmmtL5lMk0xQ8QRvIPHe9fRmNF1%2BtD%2FqfnaTSBlynty7B7JqTgL4myex6aCCN2VIy%2Fso%2F9ILiXGp%2Bl5cg%2BFJty7RuWczHzXxDgNkvh0x&X-Amz-Signature=23c8d8d47b39a41a1d0be9cc436878d18144ea3f47fae863df8cdfc9ec85ed3b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666X5G7DXJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCID4MRo3jqWBz57tiPDM1%2BTopHFIqAdwvnIashmpUWqSOAiATU28E3ZOTIhsYPMX7CMApLLdnqIZYF98xBzWdB2O03ir%2FAwgxEAAaDDYzNzQyMzE4MzgwNSIMDhOcRSElYFSJwM91KtwDIZfhpjs2KN5OWz81tFWn2bnf7eEqMEsDP%2BrpmqwrPL%2FM%2F%2FPMmRiPQRywAHD5vFp3k8n7iFwDo2ZcVd8Qzj7YDWUDTvgbWxdn6ZF3OYIFcWptBkYVjCqp0vhOjUVaboArMiRaOUJZnlNeupg6qouOTbN93sD22LY84gK4aS%2BUE2104%2FfJJWjBaL2Lun%2B0H3CivXXn9ZAtrwvjP%2F4dVoWJ4K7U9FC1PJTTn0jpcAPE4kI2VB%2BxyGgFjDv3tMJP0PrdK5hqDAie37M0%2BzlI%2FuV0WNVjW98Y2qlEs8H8Pl18UDMj9wf05AUNWB3VTux6%2BQa4K8m6gFOQAN82nWsAZX0vzaXxN6hg2WhxnEJWg6bi0Ol72RzhojOPywdXJPCnm9s2ipc4yh4kOxX4lMTTMYd8clHe%2FhaGhgsxmrnHVsxqbf3dM5GxI2eF9EItFKTAhwXUZMuv2H3ZE2%2BjVgtKydqXSd5SS%2FsstevAbfzrGoV5rBlITLgKMOnDe30%2F%2BNICDjhzoGDqkiNO8Kw6WxtmVtCmT79bqPdnqJHclbbFurnv1OAmF3Pj5WwYoR2OyBX79O0K01FqSQjZ2wGROjFkLqUfqIg1K8ZMifEKREYUA5jFhRqXiCs48v5P6CdWdE0w4eaIvQY6pgH4gC8lynyffACNu35NZ03j6YXh73sNPJLXN%2Btw%2Bve04bl0MML9PQ%2ByJlQE0MYT5sjax33N%2BoXH5qHdF0unlJOiW9fXeT85GQw%2FSJmcXx0Qhq4lucB5cUeuDmmtL5lMk0xQ8QRvIPHe9fRmNF1%2BtD%2FqfnaTSBlynty7B7JqTgL4myex6aCCN2VIy%2Fso%2F9ILiXGp%2Bl5cg%2BFJty7RuWczHzXxDgNkvh0x&X-Amz-Signature=3c54a49431e2bb21b3bd7f29b9d8f25bf35654c25b0a658bc4f0498bd77d5d92&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666X5G7DXJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCID4MRo3jqWBz57tiPDM1%2BTopHFIqAdwvnIashmpUWqSOAiATU28E3ZOTIhsYPMX7CMApLLdnqIZYF98xBzWdB2O03ir%2FAwgxEAAaDDYzNzQyMzE4MzgwNSIMDhOcRSElYFSJwM91KtwDIZfhpjs2KN5OWz81tFWn2bnf7eEqMEsDP%2BrpmqwrPL%2FM%2F%2FPMmRiPQRywAHD5vFp3k8n7iFwDo2ZcVd8Qzj7YDWUDTvgbWxdn6ZF3OYIFcWptBkYVjCqp0vhOjUVaboArMiRaOUJZnlNeupg6qouOTbN93sD22LY84gK4aS%2BUE2104%2FfJJWjBaL2Lun%2B0H3CivXXn9ZAtrwvjP%2F4dVoWJ4K7U9FC1PJTTn0jpcAPE4kI2VB%2BxyGgFjDv3tMJP0PrdK5hqDAie37M0%2BzlI%2FuV0WNVjW98Y2qlEs8H8Pl18UDMj9wf05AUNWB3VTux6%2BQa4K8m6gFOQAN82nWsAZX0vzaXxN6hg2WhxnEJWg6bi0Ol72RzhojOPywdXJPCnm9s2ipc4yh4kOxX4lMTTMYd8clHe%2FhaGhgsxmrnHVsxqbf3dM5GxI2eF9EItFKTAhwXUZMuv2H3ZE2%2BjVgtKydqXSd5SS%2FsstevAbfzrGoV5rBlITLgKMOnDe30%2F%2BNICDjhzoGDqkiNO8Kw6WxtmVtCmT79bqPdnqJHclbbFurnv1OAmF3Pj5WwYoR2OyBX79O0K01FqSQjZ2wGROjFkLqUfqIg1K8ZMifEKREYUA5jFhRqXiCs48v5P6CdWdE0w4eaIvQY6pgH4gC8lynyffACNu35NZ03j6YXh73sNPJLXN%2Btw%2Bve04bl0MML9PQ%2ByJlQE0MYT5sjax33N%2BoXH5qHdF0unlJOiW9fXeT85GQw%2FSJmcXx0Qhq4lucB5cUeuDmmtL5lMk0xQ8QRvIPHe9fRmNF1%2BtD%2FqfnaTSBlynty7B7JqTgL4myex6aCCN2VIy%2Fso%2F9ILiXGp%2Bl5cg%2BFJty7RuWczHzXxDgNkvh0x&X-Amz-Signature=ccddfe9d8dda42ce0630c19793ed8b8c5ceba177355a6fe02bddd9b02cfc6fe9&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666X5G7DXJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCID4MRo3jqWBz57tiPDM1%2BTopHFIqAdwvnIashmpUWqSOAiATU28E3ZOTIhsYPMX7CMApLLdnqIZYF98xBzWdB2O03ir%2FAwgxEAAaDDYzNzQyMzE4MzgwNSIMDhOcRSElYFSJwM91KtwDIZfhpjs2KN5OWz81tFWn2bnf7eEqMEsDP%2BrpmqwrPL%2FM%2F%2FPMmRiPQRywAHD5vFp3k8n7iFwDo2ZcVd8Qzj7YDWUDTvgbWxdn6ZF3OYIFcWptBkYVjCqp0vhOjUVaboArMiRaOUJZnlNeupg6qouOTbN93sD22LY84gK4aS%2BUE2104%2FfJJWjBaL2Lun%2B0H3CivXXn9ZAtrwvjP%2F4dVoWJ4K7U9FC1PJTTn0jpcAPE4kI2VB%2BxyGgFjDv3tMJP0PrdK5hqDAie37M0%2BzlI%2FuV0WNVjW98Y2qlEs8H8Pl18UDMj9wf05AUNWB3VTux6%2BQa4K8m6gFOQAN82nWsAZX0vzaXxN6hg2WhxnEJWg6bi0Ol72RzhojOPywdXJPCnm9s2ipc4yh4kOxX4lMTTMYd8clHe%2FhaGhgsxmrnHVsxqbf3dM5GxI2eF9EItFKTAhwXUZMuv2H3ZE2%2BjVgtKydqXSd5SS%2FsstevAbfzrGoV5rBlITLgKMOnDe30%2F%2BNICDjhzoGDqkiNO8Kw6WxtmVtCmT79bqPdnqJHclbbFurnv1OAmF3Pj5WwYoR2OyBX79O0K01FqSQjZ2wGROjFkLqUfqIg1K8ZMifEKREYUA5jFhRqXiCs48v5P6CdWdE0w4eaIvQY6pgH4gC8lynyffACNu35NZ03j6YXh73sNPJLXN%2Btw%2Bve04bl0MML9PQ%2ByJlQE0MYT5sjax33N%2BoXH5qHdF0unlJOiW9fXeT85GQw%2FSJmcXx0Qhq4lucB5cUeuDmmtL5lMk0xQ8QRvIPHe9fRmNF1%2BtD%2FqfnaTSBlynty7B7JqTgL4myex6aCCN2VIy%2Fso%2F9ILiXGp%2Bl5cg%2BFJty7RuWczHzXxDgNkvh0x&X-Amz-Signature=75f4999e914b1aba2b0bc7e3e20f28b280f99c6e62ffd3419ca529f355e49e3a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666X5G7DXJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCID4MRo3jqWBz57tiPDM1%2BTopHFIqAdwvnIashmpUWqSOAiATU28E3ZOTIhsYPMX7CMApLLdnqIZYF98xBzWdB2O03ir%2FAwgxEAAaDDYzNzQyMzE4MzgwNSIMDhOcRSElYFSJwM91KtwDIZfhpjs2KN5OWz81tFWn2bnf7eEqMEsDP%2BrpmqwrPL%2FM%2F%2FPMmRiPQRywAHD5vFp3k8n7iFwDo2ZcVd8Qzj7YDWUDTvgbWxdn6ZF3OYIFcWptBkYVjCqp0vhOjUVaboArMiRaOUJZnlNeupg6qouOTbN93sD22LY84gK4aS%2BUE2104%2FfJJWjBaL2Lun%2B0H3CivXXn9ZAtrwvjP%2F4dVoWJ4K7U9FC1PJTTn0jpcAPE4kI2VB%2BxyGgFjDv3tMJP0PrdK5hqDAie37M0%2BzlI%2FuV0WNVjW98Y2qlEs8H8Pl18UDMj9wf05AUNWB3VTux6%2BQa4K8m6gFOQAN82nWsAZX0vzaXxN6hg2WhxnEJWg6bi0Ol72RzhojOPywdXJPCnm9s2ipc4yh4kOxX4lMTTMYd8clHe%2FhaGhgsxmrnHVsxqbf3dM5GxI2eF9EItFKTAhwXUZMuv2H3ZE2%2BjVgtKydqXSd5SS%2FsstevAbfzrGoV5rBlITLgKMOnDe30%2F%2BNICDjhzoGDqkiNO8Kw6WxtmVtCmT79bqPdnqJHclbbFurnv1OAmF3Pj5WwYoR2OyBX79O0K01FqSQjZ2wGROjFkLqUfqIg1K8ZMifEKREYUA5jFhRqXiCs48v5P6CdWdE0w4eaIvQY6pgH4gC8lynyffACNu35NZ03j6YXh73sNPJLXN%2Btw%2Bve04bl0MML9PQ%2ByJlQE0MYT5sjax33N%2BoXH5qHdF0unlJOiW9fXeT85GQw%2FSJmcXx0Qhq4lucB5cUeuDmmtL5lMk0xQ8QRvIPHe9fRmNF1%2BtD%2FqfnaTSBlynty7B7JqTgL4myex6aCCN2VIy%2Fso%2F9ILiXGp%2Bl5cg%2BFJty7RuWczHzXxDgNkvh0x&X-Amz-Signature=b23b00e2477252030f82eb1bcc846862c7a7189116528576b0732398e3da93ef&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666X5G7DXJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCID4MRo3jqWBz57tiPDM1%2BTopHFIqAdwvnIashmpUWqSOAiATU28E3ZOTIhsYPMX7CMApLLdnqIZYF98xBzWdB2O03ir%2FAwgxEAAaDDYzNzQyMzE4MzgwNSIMDhOcRSElYFSJwM91KtwDIZfhpjs2KN5OWz81tFWn2bnf7eEqMEsDP%2BrpmqwrPL%2FM%2F%2FPMmRiPQRywAHD5vFp3k8n7iFwDo2ZcVd8Qzj7YDWUDTvgbWxdn6ZF3OYIFcWptBkYVjCqp0vhOjUVaboArMiRaOUJZnlNeupg6qouOTbN93sD22LY84gK4aS%2BUE2104%2FfJJWjBaL2Lun%2B0H3CivXXn9ZAtrwvjP%2F4dVoWJ4K7U9FC1PJTTn0jpcAPE4kI2VB%2BxyGgFjDv3tMJP0PrdK5hqDAie37M0%2BzlI%2FuV0WNVjW98Y2qlEs8H8Pl18UDMj9wf05AUNWB3VTux6%2BQa4K8m6gFOQAN82nWsAZX0vzaXxN6hg2WhxnEJWg6bi0Ol72RzhojOPywdXJPCnm9s2ipc4yh4kOxX4lMTTMYd8clHe%2FhaGhgsxmrnHVsxqbf3dM5GxI2eF9EItFKTAhwXUZMuv2H3ZE2%2BjVgtKydqXSd5SS%2FsstevAbfzrGoV5rBlITLgKMOnDe30%2F%2BNICDjhzoGDqkiNO8Kw6WxtmVtCmT79bqPdnqJHclbbFurnv1OAmF3Pj5WwYoR2OyBX79O0K01FqSQjZ2wGROjFkLqUfqIg1K8ZMifEKREYUA5jFhRqXiCs48v5P6CdWdE0w4eaIvQY6pgH4gC8lynyffACNu35NZ03j6YXh73sNPJLXN%2Btw%2Bve04bl0MML9PQ%2ByJlQE0MYT5sjax33N%2BoXH5qHdF0unlJOiW9fXeT85GQw%2FSJmcXx0Qhq4lucB5cUeuDmmtL5lMk0xQ8QRvIPHe9fRmNF1%2BtD%2FqfnaTSBlynty7B7JqTgL4myex6aCCN2VIy%2Fso%2F9ILiXGp%2Bl5cg%2BFJty7RuWczHzXxDgNkvh0x&X-Amz-Signature=9fce0b1a2e6405db3c616a20c2e47985886a6a8ed0935c13faef7371ecca5313&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663VDQXXZU%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJIMEYCIQC6FxWocF3TBY2LCJIKiP8DQDQa2eKdDJ68AFhw5bfjMQIhAJwPDDjxJ2kOHc%2B7ulyartVUNSKJIbLN282ZTOCOMjvVKv8DCDEQABoMNjM3NDIzMTgzODA1Igy%2FNMGXDB%2FTqAh8JjUq3ANhlDr%2FFBXTVf2fGmDWXhMA0TmPtzhYzRzSMlG7Y6drwKWJlsL%2Be39QEA0Ty7fnNu%2BtN5qrFQoarXxBKL0NiX8PCGFuMFsJ7tfWnWZcW9qNjtbJ1T1ogLp8IqDNGbuV3bYl6UOGIZq2u2rFYK7qD%2FkxiK0yFPV6TifUZfGY9IXTUmTczp9U6T%2FH5OAb%2BSU14rglX5%2BE5ECrRYrwmgXXVHVbV9IIGaFW0Iz9RZp%2BpMyg4rvb7xqub4j0S8oTkxi2WBH2ACsVockCu323Cq5dwv3Cf9sqqBzN23%2FaOMv%2FntM%2FIksIrUcC0PPRqQuokTTJ4QC0c95hspmxAfobU4cT7axDi8EzNrPihgr1GAgXnWTI%2FgpdfnZmhWjnVUIVNSBCE%2FREBk8t7SnSGz9CIwDXzuq0iiGlXwtlOcDjlxHcWZFgGyG0Xq602V5jl8G01PuiuJ2iCf8tZDHUkYtH5uO2lT30iZ9NKTKJnXlrcdmWgEIxj%2F9exuNJQ9JMCkYhWJGABN%2Bl7WQHuaVeSw77QwvANuwXABS7DTyC4daLwc1XNY5WiMLE2hV6SwLdJ3Bw8bwZyJFd9VtK77S6v%2FwoGK2pu4p6uk1mHIPdDRloOBtlZoSL2hc6sLpF17aupoSzWDDp5oi9BjqkAUgg5%2Fspx6ttiI69pZwBFVDN39hWBQCRbn9ZUY1rmqVc4XDYmOPq%2F%2Blv81V%2BGzddS1J719DrZIRvwT6R0DM3Bi7vyYaIs6%2FO%2B2X0tLp3sagQ0w5j9cZg8KYBKSde5347z%2BjyUB9Z0JeQ6UozyJdrvQ%2Bmaxkh8Q6b3OPCSEmga%2FmFRZf4GoJFzBzoWaqANP3UIkFtHBfDdv8r%2FW90U%2FJmMP22sNF%2B&X-Amz-Signature=4ebb97338833dc883057153549c29c2f28198c36c0cb57ff0774b17da426526e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663VDQXXZU%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJIMEYCIQC6FxWocF3TBY2LCJIKiP8DQDQa2eKdDJ68AFhw5bfjMQIhAJwPDDjxJ2kOHc%2B7ulyartVUNSKJIbLN282ZTOCOMjvVKv8DCDEQABoMNjM3NDIzMTgzODA1Igy%2FNMGXDB%2FTqAh8JjUq3ANhlDr%2FFBXTVf2fGmDWXhMA0TmPtzhYzRzSMlG7Y6drwKWJlsL%2Be39QEA0Ty7fnNu%2BtN5qrFQoarXxBKL0NiX8PCGFuMFsJ7tfWnWZcW9qNjtbJ1T1ogLp8IqDNGbuV3bYl6UOGIZq2u2rFYK7qD%2FkxiK0yFPV6TifUZfGY9IXTUmTczp9U6T%2FH5OAb%2BSU14rglX5%2BE5ECrRYrwmgXXVHVbV9IIGaFW0Iz9RZp%2BpMyg4rvb7xqub4j0S8oTkxi2WBH2ACsVockCu323Cq5dwv3Cf9sqqBzN23%2FaOMv%2FntM%2FIksIrUcC0PPRqQuokTTJ4QC0c95hspmxAfobU4cT7axDi8EzNrPihgr1GAgXnWTI%2FgpdfnZmhWjnVUIVNSBCE%2FREBk8t7SnSGz9CIwDXzuq0iiGlXwtlOcDjlxHcWZFgGyG0Xq602V5jl8G01PuiuJ2iCf8tZDHUkYtH5uO2lT30iZ9NKTKJnXlrcdmWgEIxj%2F9exuNJQ9JMCkYhWJGABN%2Bl7WQHuaVeSw77QwvANuwXABS7DTyC4daLwc1XNY5WiMLE2hV6SwLdJ3Bw8bwZyJFd9VtK77S6v%2FwoGK2pu4p6uk1mHIPdDRloOBtlZoSL2hc6sLpF17aupoSzWDDp5oi9BjqkAUgg5%2Fspx6ttiI69pZwBFVDN39hWBQCRbn9ZUY1rmqVc4XDYmOPq%2F%2Blv81V%2BGzddS1J719DrZIRvwT6R0DM3Bi7vyYaIs6%2FO%2B2X0tLp3sagQ0w5j9cZg8KYBKSde5347z%2BjyUB9Z0JeQ6UozyJdrvQ%2Bmaxkh8Q6b3OPCSEmga%2FmFRZf4GoJFzBzoWaqANP3UIkFtHBfDdv8r%2FW90U%2FJmMP22sNF%2B&X-Amz-Signature=028440222a931715397fe564c01bdc220bd46b0f906d22d03527f8ed0509622c&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
