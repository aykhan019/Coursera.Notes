

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5AVEL43%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJHMEUCIFrgcXW%2F5i6rat0kg8pcf2P%2Fpw1TXbBuCN%2F44ZRD6qGbAiEAwlqQbyCiQ4qmTvSY0%2B2IBX6Nf2Abc2k%2BS%2BU%2Fz2j07RQq%2FwMIaBAAGgw2Mzc0MjMxODM4MDUiDNRsonuXIr4dVtK5kSrcA3QYlgtcboX06H5cPRdU3f%2FHMXLuOCASNlctPT4Gi7iB8ITvsC7jyVJNjPNRI%2F69P%2Bx9REr6GpPc2JsDLYwsUFTrur5%2B%2F8Fma7tBAqYhrV5YEX60PxvzWyMzNBvfnKx9B0yy2XGPuEw3zTtipYE7N5IE92TRhRcdCyGCOqOrUGcI0pRGYUWOYldq3WZTZXBd06E3zb057NZugjcrUKSEjTGncWFO%2FoPgkYEchtkTLNOXjoLfQc6TOgURk19VijODznWPu7Ax8LCEO47NkhbP85Y1jekHw6Z2RYBxzvrjqAIB5GwhKBfYy2fG4f97aEVr3WcObjsVwvLCJ4SSovBXgMjFsCuBCVRmF7i5tlwFVzbL39oGOdxiw3lN6AQkPmbggxD9TnTt7enmBLJa1Q79GY7steY01mHGiGgDhfE%2BbEcmzrjKsMH3OtSKjkvPvHlrYFp1d7lJ7aUiCHAkvK%2F9S43QwrEHbz8BvOx8PyvOhOhQSTuTPV3QBBSRBhtVf4O3L6SZMp1EjFBfmmZhwz8v6U4LJLHeS9cG%2BY%2FgWg%2F2WHomUOcteEzDmJ3SWlL2QiKPxClVqaAWW7Gh6Ou5qp32iG6MBjM8nh4X4NJrGazecR8lJBv%2FzDqDtkYwtlrJMIv9lL0GOqUBjDgiRhYe%2FfliqXAU2rhugRxr%2BbBC0e4oyWkgW5xCr%2FEjinl%2BEhQrtw%2BbWkO0az%2FMOWPUUYHLrOdkN6WJzkNxhrWap0UuJOBgdJa6m2g4%2FufXJGGnh1jqLrHaxrV5Mr%2FfNy9kNCJo3CxDLDmtdPaeReauK3t5LKXPgFqL008mqKPYSGyk4BtWoaIHKpsBZGhT4866a%2BCbHYRpN1Q0GjbLt02fWMa7&X-Amz-Signature=f4d41056928e53fdcdbdfdcb1d14e604a25218f189fd0bade18976e0bc555946&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5AVEL43%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJHMEUCIFrgcXW%2F5i6rat0kg8pcf2P%2Fpw1TXbBuCN%2F44ZRD6qGbAiEAwlqQbyCiQ4qmTvSY0%2B2IBX6Nf2Abc2k%2BS%2BU%2Fz2j07RQq%2FwMIaBAAGgw2Mzc0MjMxODM4MDUiDNRsonuXIr4dVtK5kSrcA3QYlgtcboX06H5cPRdU3f%2FHMXLuOCASNlctPT4Gi7iB8ITvsC7jyVJNjPNRI%2F69P%2Bx9REr6GpPc2JsDLYwsUFTrur5%2B%2F8Fma7tBAqYhrV5YEX60PxvzWyMzNBvfnKx9B0yy2XGPuEw3zTtipYE7N5IE92TRhRcdCyGCOqOrUGcI0pRGYUWOYldq3WZTZXBd06E3zb057NZugjcrUKSEjTGncWFO%2FoPgkYEchtkTLNOXjoLfQc6TOgURk19VijODznWPu7Ax8LCEO47NkhbP85Y1jekHw6Z2RYBxzvrjqAIB5GwhKBfYy2fG4f97aEVr3WcObjsVwvLCJ4SSovBXgMjFsCuBCVRmF7i5tlwFVzbL39oGOdxiw3lN6AQkPmbggxD9TnTt7enmBLJa1Q79GY7steY01mHGiGgDhfE%2BbEcmzrjKsMH3OtSKjkvPvHlrYFp1d7lJ7aUiCHAkvK%2F9S43QwrEHbz8BvOx8PyvOhOhQSTuTPV3QBBSRBhtVf4O3L6SZMp1EjFBfmmZhwz8v6U4LJLHeS9cG%2BY%2FgWg%2F2WHomUOcteEzDmJ3SWlL2QiKPxClVqaAWW7Gh6Ou5qp32iG6MBjM8nh4X4NJrGazecR8lJBv%2FzDqDtkYwtlrJMIv9lL0GOqUBjDgiRhYe%2FfliqXAU2rhugRxr%2BbBC0e4oyWkgW5xCr%2FEjinl%2BEhQrtw%2BbWkO0az%2FMOWPUUYHLrOdkN6WJzkNxhrWap0UuJOBgdJa6m2g4%2FufXJGGnh1jqLrHaxrV5Mr%2FfNy9kNCJo3CxDLDmtdPaeReauK3t5LKXPgFqL008mqKPYSGyk4BtWoaIHKpsBZGhT4866a%2BCbHYRpN1Q0GjbLt02fWMa7&X-Amz-Signature=d0e4b7125b43ce748fd6251224e01684280c616de9e4190ee3ca8259efec0978&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5AVEL43%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJHMEUCIFrgcXW%2F5i6rat0kg8pcf2P%2Fpw1TXbBuCN%2F44ZRD6qGbAiEAwlqQbyCiQ4qmTvSY0%2B2IBX6Nf2Abc2k%2BS%2BU%2Fz2j07RQq%2FwMIaBAAGgw2Mzc0MjMxODM4MDUiDNRsonuXIr4dVtK5kSrcA3QYlgtcboX06H5cPRdU3f%2FHMXLuOCASNlctPT4Gi7iB8ITvsC7jyVJNjPNRI%2F69P%2Bx9REr6GpPc2JsDLYwsUFTrur5%2B%2F8Fma7tBAqYhrV5YEX60PxvzWyMzNBvfnKx9B0yy2XGPuEw3zTtipYE7N5IE92TRhRcdCyGCOqOrUGcI0pRGYUWOYldq3WZTZXBd06E3zb057NZugjcrUKSEjTGncWFO%2FoPgkYEchtkTLNOXjoLfQc6TOgURk19VijODznWPu7Ax8LCEO47NkhbP85Y1jekHw6Z2RYBxzvrjqAIB5GwhKBfYy2fG4f97aEVr3WcObjsVwvLCJ4SSovBXgMjFsCuBCVRmF7i5tlwFVzbL39oGOdxiw3lN6AQkPmbggxD9TnTt7enmBLJa1Q79GY7steY01mHGiGgDhfE%2BbEcmzrjKsMH3OtSKjkvPvHlrYFp1d7lJ7aUiCHAkvK%2F9S43QwrEHbz8BvOx8PyvOhOhQSTuTPV3QBBSRBhtVf4O3L6SZMp1EjFBfmmZhwz8v6U4LJLHeS9cG%2BY%2FgWg%2F2WHomUOcteEzDmJ3SWlL2QiKPxClVqaAWW7Gh6Ou5qp32iG6MBjM8nh4X4NJrGazecR8lJBv%2FzDqDtkYwtlrJMIv9lL0GOqUBjDgiRhYe%2FfliqXAU2rhugRxr%2BbBC0e4oyWkgW5xCr%2FEjinl%2BEhQrtw%2BbWkO0az%2FMOWPUUYHLrOdkN6WJzkNxhrWap0UuJOBgdJa6m2g4%2FufXJGGnh1jqLrHaxrV5Mr%2FfNy9kNCJo3CxDLDmtdPaeReauK3t5LKXPgFqL008mqKPYSGyk4BtWoaIHKpsBZGhT4866a%2BCbHYRpN1Q0GjbLt02fWMa7&X-Amz-Signature=463753135e0b09a5e6f759c05f5f5d3f0cf6e4bf4bb17b2feb7000384a3268ca&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5AVEL43%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJHMEUCIFrgcXW%2F5i6rat0kg8pcf2P%2Fpw1TXbBuCN%2F44ZRD6qGbAiEAwlqQbyCiQ4qmTvSY0%2B2IBX6Nf2Abc2k%2BS%2BU%2Fz2j07RQq%2FwMIaBAAGgw2Mzc0MjMxODM4MDUiDNRsonuXIr4dVtK5kSrcA3QYlgtcboX06H5cPRdU3f%2FHMXLuOCASNlctPT4Gi7iB8ITvsC7jyVJNjPNRI%2F69P%2Bx9REr6GpPc2JsDLYwsUFTrur5%2B%2F8Fma7tBAqYhrV5YEX60PxvzWyMzNBvfnKx9B0yy2XGPuEw3zTtipYE7N5IE92TRhRcdCyGCOqOrUGcI0pRGYUWOYldq3WZTZXBd06E3zb057NZugjcrUKSEjTGncWFO%2FoPgkYEchtkTLNOXjoLfQc6TOgURk19VijODznWPu7Ax8LCEO47NkhbP85Y1jekHw6Z2RYBxzvrjqAIB5GwhKBfYy2fG4f97aEVr3WcObjsVwvLCJ4SSovBXgMjFsCuBCVRmF7i5tlwFVzbL39oGOdxiw3lN6AQkPmbggxD9TnTt7enmBLJa1Q79GY7steY01mHGiGgDhfE%2BbEcmzrjKsMH3OtSKjkvPvHlrYFp1d7lJ7aUiCHAkvK%2F9S43QwrEHbz8BvOx8PyvOhOhQSTuTPV3QBBSRBhtVf4O3L6SZMp1EjFBfmmZhwz8v6U4LJLHeS9cG%2BY%2FgWg%2F2WHomUOcteEzDmJ3SWlL2QiKPxClVqaAWW7Gh6Ou5qp32iG6MBjM8nh4X4NJrGazecR8lJBv%2FzDqDtkYwtlrJMIv9lL0GOqUBjDgiRhYe%2FfliqXAU2rhugRxr%2BbBC0e4oyWkgW5xCr%2FEjinl%2BEhQrtw%2BbWkO0az%2FMOWPUUYHLrOdkN6WJzkNxhrWap0UuJOBgdJa6m2g4%2FufXJGGnh1jqLrHaxrV5Mr%2FfNy9kNCJo3CxDLDmtdPaeReauK3t5LKXPgFqL008mqKPYSGyk4BtWoaIHKpsBZGhT4866a%2BCbHYRpN1Q0GjbLt02fWMa7&X-Amz-Signature=6511f11ab0114b8193381cafe037137ba17416d8e9d19e5e35d36dbdf924115b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5AVEL43%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJHMEUCIFrgcXW%2F5i6rat0kg8pcf2P%2Fpw1TXbBuCN%2F44ZRD6qGbAiEAwlqQbyCiQ4qmTvSY0%2B2IBX6Nf2Abc2k%2BS%2BU%2Fz2j07RQq%2FwMIaBAAGgw2Mzc0MjMxODM4MDUiDNRsonuXIr4dVtK5kSrcA3QYlgtcboX06H5cPRdU3f%2FHMXLuOCASNlctPT4Gi7iB8ITvsC7jyVJNjPNRI%2F69P%2Bx9REr6GpPc2JsDLYwsUFTrur5%2B%2F8Fma7tBAqYhrV5YEX60PxvzWyMzNBvfnKx9B0yy2XGPuEw3zTtipYE7N5IE92TRhRcdCyGCOqOrUGcI0pRGYUWOYldq3WZTZXBd06E3zb057NZugjcrUKSEjTGncWFO%2FoPgkYEchtkTLNOXjoLfQc6TOgURk19VijODznWPu7Ax8LCEO47NkhbP85Y1jekHw6Z2RYBxzvrjqAIB5GwhKBfYy2fG4f97aEVr3WcObjsVwvLCJ4SSovBXgMjFsCuBCVRmF7i5tlwFVzbL39oGOdxiw3lN6AQkPmbggxD9TnTt7enmBLJa1Q79GY7steY01mHGiGgDhfE%2BbEcmzrjKsMH3OtSKjkvPvHlrYFp1d7lJ7aUiCHAkvK%2F9S43QwrEHbz8BvOx8PyvOhOhQSTuTPV3QBBSRBhtVf4O3L6SZMp1EjFBfmmZhwz8v6U4LJLHeS9cG%2BY%2FgWg%2F2WHomUOcteEzDmJ3SWlL2QiKPxClVqaAWW7Gh6Ou5qp32iG6MBjM8nh4X4NJrGazecR8lJBv%2FzDqDtkYwtlrJMIv9lL0GOqUBjDgiRhYe%2FfliqXAU2rhugRxr%2BbBC0e4oyWkgW5xCr%2FEjinl%2BEhQrtw%2BbWkO0az%2FMOWPUUYHLrOdkN6WJzkNxhrWap0UuJOBgdJa6m2g4%2FufXJGGnh1jqLrHaxrV5Mr%2FfNy9kNCJo3CxDLDmtdPaeReauK3t5LKXPgFqL008mqKPYSGyk4BtWoaIHKpsBZGhT4866a%2BCbHYRpN1Q0GjbLt02fWMa7&X-Amz-Signature=f88ff3252c74cf37f9f1674f9bb8f05b479495fc8bb0984c5565f6545cb2d63e&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5AVEL43%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJHMEUCIFrgcXW%2F5i6rat0kg8pcf2P%2Fpw1TXbBuCN%2F44ZRD6qGbAiEAwlqQbyCiQ4qmTvSY0%2B2IBX6Nf2Abc2k%2BS%2BU%2Fz2j07RQq%2FwMIaBAAGgw2Mzc0MjMxODM4MDUiDNRsonuXIr4dVtK5kSrcA3QYlgtcboX06H5cPRdU3f%2FHMXLuOCASNlctPT4Gi7iB8ITvsC7jyVJNjPNRI%2F69P%2Bx9REr6GpPc2JsDLYwsUFTrur5%2B%2F8Fma7tBAqYhrV5YEX60PxvzWyMzNBvfnKx9B0yy2XGPuEw3zTtipYE7N5IE92TRhRcdCyGCOqOrUGcI0pRGYUWOYldq3WZTZXBd06E3zb057NZugjcrUKSEjTGncWFO%2FoPgkYEchtkTLNOXjoLfQc6TOgURk19VijODznWPu7Ax8LCEO47NkhbP85Y1jekHw6Z2RYBxzvrjqAIB5GwhKBfYy2fG4f97aEVr3WcObjsVwvLCJ4SSovBXgMjFsCuBCVRmF7i5tlwFVzbL39oGOdxiw3lN6AQkPmbggxD9TnTt7enmBLJa1Q79GY7steY01mHGiGgDhfE%2BbEcmzrjKsMH3OtSKjkvPvHlrYFp1d7lJ7aUiCHAkvK%2F9S43QwrEHbz8BvOx8PyvOhOhQSTuTPV3QBBSRBhtVf4O3L6SZMp1EjFBfmmZhwz8v6U4LJLHeS9cG%2BY%2FgWg%2F2WHomUOcteEzDmJ3SWlL2QiKPxClVqaAWW7Gh6Ou5qp32iG6MBjM8nh4X4NJrGazecR8lJBv%2FzDqDtkYwtlrJMIv9lL0GOqUBjDgiRhYe%2FfliqXAU2rhugRxr%2BbBC0e4oyWkgW5xCr%2FEjinl%2BEhQrtw%2BbWkO0az%2FMOWPUUYHLrOdkN6WJzkNxhrWap0UuJOBgdJa6m2g4%2FufXJGGnh1jqLrHaxrV5Mr%2FfNy9kNCJo3CxDLDmtdPaeReauK3t5LKXPgFqL008mqKPYSGyk4BtWoaIHKpsBZGhT4866a%2BCbHYRpN1Q0GjbLt02fWMa7&X-Amz-Signature=cd1a89cc6d6e58889ef0b8cf9f9a6754ac8c8bc32bfa931abcf373d24cad8526&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5AVEL43%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJHMEUCIFrgcXW%2F5i6rat0kg8pcf2P%2Fpw1TXbBuCN%2F44ZRD6qGbAiEAwlqQbyCiQ4qmTvSY0%2B2IBX6Nf2Abc2k%2BS%2BU%2Fz2j07RQq%2FwMIaBAAGgw2Mzc0MjMxODM4MDUiDNRsonuXIr4dVtK5kSrcA3QYlgtcboX06H5cPRdU3f%2FHMXLuOCASNlctPT4Gi7iB8ITvsC7jyVJNjPNRI%2F69P%2Bx9REr6GpPc2JsDLYwsUFTrur5%2B%2F8Fma7tBAqYhrV5YEX60PxvzWyMzNBvfnKx9B0yy2XGPuEw3zTtipYE7N5IE92TRhRcdCyGCOqOrUGcI0pRGYUWOYldq3WZTZXBd06E3zb057NZugjcrUKSEjTGncWFO%2FoPgkYEchtkTLNOXjoLfQc6TOgURk19VijODznWPu7Ax8LCEO47NkhbP85Y1jekHw6Z2RYBxzvrjqAIB5GwhKBfYy2fG4f97aEVr3WcObjsVwvLCJ4SSovBXgMjFsCuBCVRmF7i5tlwFVzbL39oGOdxiw3lN6AQkPmbggxD9TnTt7enmBLJa1Q79GY7steY01mHGiGgDhfE%2BbEcmzrjKsMH3OtSKjkvPvHlrYFp1d7lJ7aUiCHAkvK%2F9S43QwrEHbz8BvOx8PyvOhOhQSTuTPV3QBBSRBhtVf4O3L6SZMp1EjFBfmmZhwz8v6U4LJLHeS9cG%2BY%2FgWg%2F2WHomUOcteEzDmJ3SWlL2QiKPxClVqaAWW7Gh6Ou5qp32iG6MBjM8nh4X4NJrGazecR8lJBv%2FzDqDtkYwtlrJMIv9lL0GOqUBjDgiRhYe%2FfliqXAU2rhugRxr%2BbBC0e4oyWkgW5xCr%2FEjinl%2BEhQrtw%2BbWkO0az%2FMOWPUUYHLrOdkN6WJzkNxhrWap0UuJOBgdJa6m2g4%2FufXJGGnh1jqLrHaxrV5Mr%2FfNy9kNCJo3CxDLDmtdPaeReauK3t5LKXPgFqL008mqKPYSGyk4BtWoaIHKpsBZGhT4866a%2BCbHYRpN1Q0GjbLt02fWMa7&X-Amz-Signature=476568a19af91e9adbba2dd0bd9a78515a91eea3edc1f4d6e9fe15ab43d97a5a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5AVEL43%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJHMEUCIFrgcXW%2F5i6rat0kg8pcf2P%2Fpw1TXbBuCN%2F44ZRD6qGbAiEAwlqQbyCiQ4qmTvSY0%2B2IBX6Nf2Abc2k%2BS%2BU%2Fz2j07RQq%2FwMIaBAAGgw2Mzc0MjMxODM4MDUiDNRsonuXIr4dVtK5kSrcA3QYlgtcboX06H5cPRdU3f%2FHMXLuOCASNlctPT4Gi7iB8ITvsC7jyVJNjPNRI%2F69P%2Bx9REr6GpPc2JsDLYwsUFTrur5%2B%2F8Fma7tBAqYhrV5YEX60PxvzWyMzNBvfnKx9B0yy2XGPuEw3zTtipYE7N5IE92TRhRcdCyGCOqOrUGcI0pRGYUWOYldq3WZTZXBd06E3zb057NZugjcrUKSEjTGncWFO%2FoPgkYEchtkTLNOXjoLfQc6TOgURk19VijODznWPu7Ax8LCEO47NkhbP85Y1jekHw6Z2RYBxzvrjqAIB5GwhKBfYy2fG4f97aEVr3WcObjsVwvLCJ4SSovBXgMjFsCuBCVRmF7i5tlwFVzbL39oGOdxiw3lN6AQkPmbggxD9TnTt7enmBLJa1Q79GY7steY01mHGiGgDhfE%2BbEcmzrjKsMH3OtSKjkvPvHlrYFp1d7lJ7aUiCHAkvK%2F9S43QwrEHbz8BvOx8PyvOhOhQSTuTPV3QBBSRBhtVf4O3L6SZMp1EjFBfmmZhwz8v6U4LJLHeS9cG%2BY%2FgWg%2F2WHomUOcteEzDmJ3SWlL2QiKPxClVqaAWW7Gh6Ou5qp32iG6MBjM8nh4X4NJrGazecR8lJBv%2FzDqDtkYwtlrJMIv9lL0GOqUBjDgiRhYe%2FfliqXAU2rhugRxr%2BbBC0e4oyWkgW5xCr%2FEjinl%2BEhQrtw%2BbWkO0az%2FMOWPUUYHLrOdkN6WJzkNxhrWap0UuJOBgdJa6m2g4%2FufXJGGnh1jqLrHaxrV5Mr%2FfNy9kNCJo3CxDLDmtdPaeReauK3t5LKXPgFqL008mqKPYSGyk4BtWoaIHKpsBZGhT4866a%2BCbHYRpN1Q0GjbLt02fWMa7&X-Amz-Signature=5913f8a24bfe639afe5271053305f8747d16399bd7784fa54b9f4c60f0c3cbb2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5AVEL43%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJHMEUCIFrgcXW%2F5i6rat0kg8pcf2P%2Fpw1TXbBuCN%2F44ZRD6qGbAiEAwlqQbyCiQ4qmTvSY0%2B2IBX6Nf2Abc2k%2BS%2BU%2Fz2j07RQq%2FwMIaBAAGgw2Mzc0MjMxODM4MDUiDNRsonuXIr4dVtK5kSrcA3QYlgtcboX06H5cPRdU3f%2FHMXLuOCASNlctPT4Gi7iB8ITvsC7jyVJNjPNRI%2F69P%2Bx9REr6GpPc2JsDLYwsUFTrur5%2B%2F8Fma7tBAqYhrV5YEX60PxvzWyMzNBvfnKx9B0yy2XGPuEw3zTtipYE7N5IE92TRhRcdCyGCOqOrUGcI0pRGYUWOYldq3WZTZXBd06E3zb057NZugjcrUKSEjTGncWFO%2FoPgkYEchtkTLNOXjoLfQc6TOgURk19VijODznWPu7Ax8LCEO47NkhbP85Y1jekHw6Z2RYBxzvrjqAIB5GwhKBfYy2fG4f97aEVr3WcObjsVwvLCJ4SSovBXgMjFsCuBCVRmF7i5tlwFVzbL39oGOdxiw3lN6AQkPmbggxD9TnTt7enmBLJa1Q79GY7steY01mHGiGgDhfE%2BbEcmzrjKsMH3OtSKjkvPvHlrYFp1d7lJ7aUiCHAkvK%2F9S43QwrEHbz8BvOx8PyvOhOhQSTuTPV3QBBSRBhtVf4O3L6SZMp1EjFBfmmZhwz8v6U4LJLHeS9cG%2BY%2FgWg%2F2WHomUOcteEzDmJ3SWlL2QiKPxClVqaAWW7Gh6Ou5qp32iG6MBjM8nh4X4NJrGazecR8lJBv%2FzDqDtkYwtlrJMIv9lL0GOqUBjDgiRhYe%2FfliqXAU2rhugRxr%2BbBC0e4oyWkgW5xCr%2FEjinl%2BEhQrtw%2BbWkO0az%2FMOWPUUYHLrOdkN6WJzkNxhrWap0UuJOBgdJa6m2g4%2FufXJGGnh1jqLrHaxrV5Mr%2FfNy9kNCJo3CxDLDmtdPaeReauK3t5LKXPgFqL008mqKPYSGyk4BtWoaIHKpsBZGhT4866a%2BCbHYRpN1Q0GjbLt02fWMa7&X-Amz-Signature=0c39dfd5e1c471d3c53155adc49ac8f585a84ec968690cbc42ba46f4bee9d66a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VPVNESII%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJIMEYCIQDT0BIFBbNCy0%2Bctj8o6G%2FQEP1zyKAmCBD0%2FVsXVEIqHwIhAIaFcIURLgC3dsLLpXZVhmtjvfUJa9r8jzf5B77pvOy0Kv8DCGgQABoMNjM3NDIzMTgzODA1IgxsderS0WjXGFJkHu4q3AN2zb6piWvHlgom%2B0CBYBRkpP2fluyA5jGMaPAk4YqG0czyg9IG2eFHiDOOw86p%2FLZ6mhstqG4%2FAfSfg0rTs0Cb%2FLtAyUdzv4c%2BFAUdF4IzFLPcwbfwoOzdi8KtCu6pML0CUIlNYqxwM6QsttlO%2Bo%2BzEgzSW7SPASXX1mKRaGZPNjmERSL%2BQDeCLg3qSf0I6XwkcdOCggtmq5Z%2F2k%2FlvdzXyWt0WlkgFO8zfDMQAME3nKWQcJ0uoYT%2BOMne4J22NP5Qvr7ImvLvJ23BOwDguTMKfSA0kjRNvFJ%2F44X2O1Uul2MmaJ5PMRew35ZNQkt6%2FmDG7sEdSauhCinRrKXWa5Wfz1vmepNsHKc%2FzObD6cuT3MAodNM%2FXyIVwarzJ1zJjcs9pv%2Ba5oG1PZYC9U0zohHbqzkvvW6JCItDOLA7dik3wjLrMOVmO%2B1QRH7cRi4VQ9tYrPXNsEogMq9Uty1u1IcsSSJPZZ6o0OLvZa21E002%2BQI%2B6AhkblPw%2F22M4txx0yuA%2FbqQbXxn9qZniaYaHDx6MJ%2BupO%2F4pKaE7JZlwnqIhHv167xNZEhmVunX8JMOCfSM5X6zXiQacgxKmTlbaqpsxvENaom0SEvb%2FbPTwuJKjbTA6zn3WSWwypCuRDDl%2FZS9BjqkAV4JWAo7lyM%2F%2BaKln8g10EuV7kkoYPQ9ZZP%2FWsV4IWLUdBIY%2BqbE8zxsczp1Ax6SFQDpVvQSWm6zoG0vzsPE3AIg9AXTtqy9w%2Bfy28%2BW2u3qes%2FnEZtymCIqsI5KO8h5YkRB%2BxKuassfUpUN3mSIeIuhYrMH8l%2BUnsecCTcc6dVuRZlu2IoHpzKCuXMMuP5Eh08BpePiJDr4x2wT8N02I9FnBVAT&X-Amz-Signature=3e27847d12289db44d1c1c68dc4a37b5141c68a0db8c99bfa917adbbe1c09c85&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VPVNESII%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJIMEYCIQDT0BIFBbNCy0%2Bctj8o6G%2FQEP1zyKAmCBD0%2FVsXVEIqHwIhAIaFcIURLgC3dsLLpXZVhmtjvfUJa9r8jzf5B77pvOy0Kv8DCGgQABoMNjM3NDIzMTgzODA1IgxsderS0WjXGFJkHu4q3AN2zb6piWvHlgom%2B0CBYBRkpP2fluyA5jGMaPAk4YqG0czyg9IG2eFHiDOOw86p%2FLZ6mhstqG4%2FAfSfg0rTs0Cb%2FLtAyUdzv4c%2BFAUdF4IzFLPcwbfwoOzdi8KtCu6pML0CUIlNYqxwM6QsttlO%2Bo%2BzEgzSW7SPASXX1mKRaGZPNjmERSL%2BQDeCLg3qSf0I6XwkcdOCggtmq5Z%2F2k%2FlvdzXyWt0WlkgFO8zfDMQAME3nKWQcJ0uoYT%2BOMne4J22NP5Qvr7ImvLvJ23BOwDguTMKfSA0kjRNvFJ%2F44X2O1Uul2MmaJ5PMRew35ZNQkt6%2FmDG7sEdSauhCinRrKXWa5Wfz1vmepNsHKc%2FzObD6cuT3MAodNM%2FXyIVwarzJ1zJjcs9pv%2Ba5oG1PZYC9U0zohHbqzkvvW6JCItDOLA7dik3wjLrMOVmO%2B1QRH7cRi4VQ9tYrPXNsEogMq9Uty1u1IcsSSJPZZ6o0OLvZa21E002%2BQI%2B6AhkblPw%2F22M4txx0yuA%2FbqQbXxn9qZniaYaHDx6MJ%2BupO%2F4pKaE7JZlwnqIhHv167xNZEhmVunX8JMOCfSM5X6zXiQacgxKmTlbaqpsxvENaom0SEvb%2FbPTwuJKjbTA6zn3WSWwypCuRDDl%2FZS9BjqkAV4JWAo7lyM%2F%2BaKln8g10EuV7kkoYPQ9ZZP%2FWsV4IWLUdBIY%2BqbE8zxsczp1Ax6SFQDpVvQSWm6zoG0vzsPE3AIg9AXTtqy9w%2Bfy28%2BW2u3qes%2FnEZtymCIqsI5KO8h5YkRB%2BxKuassfUpUN3mSIeIuhYrMH8l%2BUnsecCTcc6dVuRZlu2IoHpzKCuXMMuP5Eh08BpePiJDr4x2wT8N02I9FnBVAT&X-Amz-Signature=09202d133d2e2c8b8919976feee14f6aeb2ed9cca657d00c28d6bedbbb664811&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
