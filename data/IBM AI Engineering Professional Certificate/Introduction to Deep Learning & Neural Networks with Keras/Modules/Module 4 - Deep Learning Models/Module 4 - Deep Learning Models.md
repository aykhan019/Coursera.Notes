

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SJEZXUB%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJFMEMCHyeNBTG78EeGm6HqBdhmGLnlGaP0SOZh5BChoEyndLsCIBss9%2FsaUTefE54m0p19dxDV9%2FAgHPECvf9PgEyA9HUcKv8DCBUQABoMNjM3NDIzMTgzODA1IgwX6wLYyuXp9NpVEUUq3APMNjyd9JcN1ngE5YDnPwNLm4NptgFkW1gxRdljn52PuWbdgZhvoPmtKbFzqXqJZ%2B0SoEMcQNnANR9txlzsnpGZZ2SLe%2B%2BqmIGcs%2FUoLdt1Ib%2Fkd97vuSvNWyiuYW1WK6%2FVCLKI8Z%2F%2B3E0IHuMnUrlocDqx11GWOV%2B61VyPJOud35%2F2VpAuVHGanBb4v7PLGI6NJcaXRpAcYo4TTn3vsYTztX2nvCR392jICX679SxgJg8buNGBth8X3g9gKUg7BmIgry7tHo9wME74Zxd9vpy%2B8%2B%2BkYOflU8T7K6cn%2BzEXD0sJuQrXt3OUElK9cc9U1oUy1dZR9n%2Bl2tBoCvjzsi6UrLgg8zPl0SurOffRMEfNdfvaCglzRxsqnJ0hfbp3QVhTUV%2FGMfPm7DeN%2FIaFiWH30YggBrqehIzq509Vjdh%2FsWxOyZ2qQzk1iySp207reqk4cdTN4ZBQEg0QmHkPbst%2FNoR%2Bq%2FTelwf3h672qVywVmWRLTY2wV4%2FxzW4SDxdNYb7D8L%2BCxkRMwJqZTK45MS1TAjhS2BrAvFdXXk2Ma536XI%2FYA6ke7SJDEJ1ZxFtBYE8TvCuOdJq06dWiNBAAWgeP%2BVMBXY2j3aiDrle6KsJ0N0bxJloaA%2FjbyXOhjCH04K9BjqnARnKx9GBlAFGTah7yyNiEdxmzy3ZZN%2BbKxu2sorrVWvCoIE%2Bfuk3LDruqCbZ68MG7LU7AN%2B1XkuEa6o1faS6%2B71PtcaZY1yalYDu4ToYvwVPJIOpv6LXEvfZB7S4O%2Ba%2FiAgz21flflLAZqCtDsL1v9QUlbxvuFkzjEeHx%2FgLWsAtgLgs6k%2BPnoqwEK3awIdZ7Lr9RUOzsE22PJPJjT9PNsX8cmJc7LAH&X-Amz-Signature=bab5a8b7890db207e511bdd77dc0eda1132a9201f686180876ddf09f66d1fed1&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SJEZXUB%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJFMEMCHyeNBTG78EeGm6HqBdhmGLnlGaP0SOZh5BChoEyndLsCIBss9%2FsaUTefE54m0p19dxDV9%2FAgHPECvf9PgEyA9HUcKv8DCBUQABoMNjM3NDIzMTgzODA1IgwX6wLYyuXp9NpVEUUq3APMNjyd9JcN1ngE5YDnPwNLm4NptgFkW1gxRdljn52PuWbdgZhvoPmtKbFzqXqJZ%2B0SoEMcQNnANR9txlzsnpGZZ2SLe%2B%2BqmIGcs%2FUoLdt1Ib%2Fkd97vuSvNWyiuYW1WK6%2FVCLKI8Z%2F%2B3E0IHuMnUrlocDqx11GWOV%2B61VyPJOud35%2F2VpAuVHGanBb4v7PLGI6NJcaXRpAcYo4TTn3vsYTztX2nvCR392jICX679SxgJg8buNGBth8X3g9gKUg7BmIgry7tHo9wME74Zxd9vpy%2B8%2B%2BkYOflU8T7K6cn%2BzEXD0sJuQrXt3OUElK9cc9U1oUy1dZR9n%2Bl2tBoCvjzsi6UrLgg8zPl0SurOffRMEfNdfvaCglzRxsqnJ0hfbp3QVhTUV%2FGMfPm7DeN%2FIaFiWH30YggBrqehIzq509Vjdh%2FsWxOyZ2qQzk1iySp207reqk4cdTN4ZBQEg0QmHkPbst%2FNoR%2Bq%2FTelwf3h672qVywVmWRLTY2wV4%2FxzW4SDxdNYb7D8L%2BCxkRMwJqZTK45MS1TAjhS2BrAvFdXXk2Ma536XI%2FYA6ke7SJDEJ1ZxFtBYE8TvCuOdJq06dWiNBAAWgeP%2BVMBXY2j3aiDrle6KsJ0N0bxJloaA%2FjbyXOhjCH04K9BjqnARnKx9GBlAFGTah7yyNiEdxmzy3ZZN%2BbKxu2sorrVWvCoIE%2Bfuk3LDruqCbZ68MG7LU7AN%2B1XkuEa6o1faS6%2B71PtcaZY1yalYDu4ToYvwVPJIOpv6LXEvfZB7S4O%2Ba%2FiAgz21flflLAZqCtDsL1v9QUlbxvuFkzjEeHx%2FgLWsAtgLgs6k%2BPnoqwEK3awIdZ7Lr9RUOzsE22PJPJjT9PNsX8cmJc7LAH&X-Amz-Signature=ad4a9ed1a0efa0a078ff9e9121a10d9c97450a67f6f02f71377cfe1a08cfd4e0&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SJEZXUB%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJFMEMCHyeNBTG78EeGm6HqBdhmGLnlGaP0SOZh5BChoEyndLsCIBss9%2FsaUTefE54m0p19dxDV9%2FAgHPECvf9PgEyA9HUcKv8DCBUQABoMNjM3NDIzMTgzODA1IgwX6wLYyuXp9NpVEUUq3APMNjyd9JcN1ngE5YDnPwNLm4NptgFkW1gxRdljn52PuWbdgZhvoPmtKbFzqXqJZ%2B0SoEMcQNnANR9txlzsnpGZZ2SLe%2B%2BqmIGcs%2FUoLdt1Ib%2Fkd97vuSvNWyiuYW1WK6%2FVCLKI8Z%2F%2B3E0IHuMnUrlocDqx11GWOV%2B61VyPJOud35%2F2VpAuVHGanBb4v7PLGI6NJcaXRpAcYo4TTn3vsYTztX2nvCR392jICX679SxgJg8buNGBth8X3g9gKUg7BmIgry7tHo9wME74Zxd9vpy%2B8%2B%2BkYOflU8T7K6cn%2BzEXD0sJuQrXt3OUElK9cc9U1oUy1dZR9n%2Bl2tBoCvjzsi6UrLgg8zPl0SurOffRMEfNdfvaCglzRxsqnJ0hfbp3QVhTUV%2FGMfPm7DeN%2FIaFiWH30YggBrqehIzq509Vjdh%2FsWxOyZ2qQzk1iySp207reqk4cdTN4ZBQEg0QmHkPbst%2FNoR%2Bq%2FTelwf3h672qVywVmWRLTY2wV4%2FxzW4SDxdNYb7D8L%2BCxkRMwJqZTK45MS1TAjhS2BrAvFdXXk2Ma536XI%2FYA6ke7SJDEJ1ZxFtBYE8TvCuOdJq06dWiNBAAWgeP%2BVMBXY2j3aiDrle6KsJ0N0bxJloaA%2FjbyXOhjCH04K9BjqnARnKx9GBlAFGTah7yyNiEdxmzy3ZZN%2BbKxu2sorrVWvCoIE%2Bfuk3LDruqCbZ68MG7LU7AN%2B1XkuEa6o1faS6%2B71PtcaZY1yalYDu4ToYvwVPJIOpv6LXEvfZB7S4O%2Ba%2FiAgz21flflLAZqCtDsL1v9QUlbxvuFkzjEeHx%2FgLWsAtgLgs6k%2BPnoqwEK3awIdZ7Lr9RUOzsE22PJPJjT9PNsX8cmJc7LAH&X-Amz-Signature=92829c2d252858a0b4bba3efe05b4eeac5bd7edfdca4c2c51747f0c7a6c5deaf&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SJEZXUB%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJFMEMCHyeNBTG78EeGm6HqBdhmGLnlGaP0SOZh5BChoEyndLsCIBss9%2FsaUTefE54m0p19dxDV9%2FAgHPECvf9PgEyA9HUcKv8DCBUQABoMNjM3NDIzMTgzODA1IgwX6wLYyuXp9NpVEUUq3APMNjyd9JcN1ngE5YDnPwNLm4NptgFkW1gxRdljn52PuWbdgZhvoPmtKbFzqXqJZ%2B0SoEMcQNnANR9txlzsnpGZZ2SLe%2B%2BqmIGcs%2FUoLdt1Ib%2Fkd97vuSvNWyiuYW1WK6%2FVCLKI8Z%2F%2B3E0IHuMnUrlocDqx11GWOV%2B61VyPJOud35%2F2VpAuVHGanBb4v7PLGI6NJcaXRpAcYo4TTn3vsYTztX2nvCR392jICX679SxgJg8buNGBth8X3g9gKUg7BmIgry7tHo9wME74Zxd9vpy%2B8%2B%2BkYOflU8T7K6cn%2BzEXD0sJuQrXt3OUElK9cc9U1oUy1dZR9n%2Bl2tBoCvjzsi6UrLgg8zPl0SurOffRMEfNdfvaCglzRxsqnJ0hfbp3QVhTUV%2FGMfPm7DeN%2FIaFiWH30YggBrqehIzq509Vjdh%2FsWxOyZ2qQzk1iySp207reqk4cdTN4ZBQEg0QmHkPbst%2FNoR%2Bq%2FTelwf3h672qVywVmWRLTY2wV4%2FxzW4SDxdNYb7D8L%2BCxkRMwJqZTK45MS1TAjhS2BrAvFdXXk2Ma536XI%2FYA6ke7SJDEJ1ZxFtBYE8TvCuOdJq06dWiNBAAWgeP%2BVMBXY2j3aiDrle6KsJ0N0bxJloaA%2FjbyXOhjCH04K9BjqnARnKx9GBlAFGTah7yyNiEdxmzy3ZZN%2BbKxu2sorrVWvCoIE%2Bfuk3LDruqCbZ68MG7LU7AN%2B1XkuEa6o1faS6%2B71PtcaZY1yalYDu4ToYvwVPJIOpv6LXEvfZB7S4O%2Ba%2FiAgz21flflLAZqCtDsL1v9QUlbxvuFkzjEeHx%2FgLWsAtgLgs6k%2BPnoqwEK3awIdZ7Lr9RUOzsE22PJPJjT9PNsX8cmJc7LAH&X-Amz-Signature=6d64d2788a61cd2b56654e1b288e235c0ffe57057d942af730c68aab81af0eca&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SJEZXUB%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJFMEMCHyeNBTG78EeGm6HqBdhmGLnlGaP0SOZh5BChoEyndLsCIBss9%2FsaUTefE54m0p19dxDV9%2FAgHPECvf9PgEyA9HUcKv8DCBUQABoMNjM3NDIzMTgzODA1IgwX6wLYyuXp9NpVEUUq3APMNjyd9JcN1ngE5YDnPwNLm4NptgFkW1gxRdljn52PuWbdgZhvoPmtKbFzqXqJZ%2B0SoEMcQNnANR9txlzsnpGZZ2SLe%2B%2BqmIGcs%2FUoLdt1Ib%2Fkd97vuSvNWyiuYW1WK6%2FVCLKI8Z%2F%2B3E0IHuMnUrlocDqx11GWOV%2B61VyPJOud35%2F2VpAuVHGanBb4v7PLGI6NJcaXRpAcYo4TTn3vsYTztX2nvCR392jICX679SxgJg8buNGBth8X3g9gKUg7BmIgry7tHo9wME74Zxd9vpy%2B8%2B%2BkYOflU8T7K6cn%2BzEXD0sJuQrXt3OUElK9cc9U1oUy1dZR9n%2Bl2tBoCvjzsi6UrLgg8zPl0SurOffRMEfNdfvaCglzRxsqnJ0hfbp3QVhTUV%2FGMfPm7DeN%2FIaFiWH30YggBrqehIzq509Vjdh%2FsWxOyZ2qQzk1iySp207reqk4cdTN4ZBQEg0QmHkPbst%2FNoR%2Bq%2FTelwf3h672qVywVmWRLTY2wV4%2FxzW4SDxdNYb7D8L%2BCxkRMwJqZTK45MS1TAjhS2BrAvFdXXk2Ma536XI%2FYA6ke7SJDEJ1ZxFtBYE8TvCuOdJq06dWiNBAAWgeP%2BVMBXY2j3aiDrle6KsJ0N0bxJloaA%2FjbyXOhjCH04K9BjqnARnKx9GBlAFGTah7yyNiEdxmzy3ZZN%2BbKxu2sorrVWvCoIE%2Bfuk3LDruqCbZ68MG7LU7AN%2B1XkuEa6o1faS6%2B71PtcaZY1yalYDu4ToYvwVPJIOpv6LXEvfZB7S4O%2Ba%2FiAgz21flflLAZqCtDsL1v9QUlbxvuFkzjEeHx%2FgLWsAtgLgs6k%2BPnoqwEK3awIdZ7Lr9RUOzsE22PJPJjT9PNsX8cmJc7LAH&X-Amz-Signature=fc86023225025bfd18be222c168dee6b621c769e21872fcc69924956ee420eb7&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SJEZXUB%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJFMEMCHyeNBTG78EeGm6HqBdhmGLnlGaP0SOZh5BChoEyndLsCIBss9%2FsaUTefE54m0p19dxDV9%2FAgHPECvf9PgEyA9HUcKv8DCBUQABoMNjM3NDIzMTgzODA1IgwX6wLYyuXp9NpVEUUq3APMNjyd9JcN1ngE5YDnPwNLm4NptgFkW1gxRdljn52PuWbdgZhvoPmtKbFzqXqJZ%2B0SoEMcQNnANR9txlzsnpGZZ2SLe%2B%2BqmIGcs%2FUoLdt1Ib%2Fkd97vuSvNWyiuYW1WK6%2FVCLKI8Z%2F%2B3E0IHuMnUrlocDqx11GWOV%2B61VyPJOud35%2F2VpAuVHGanBb4v7PLGI6NJcaXRpAcYo4TTn3vsYTztX2nvCR392jICX679SxgJg8buNGBth8X3g9gKUg7BmIgry7tHo9wME74Zxd9vpy%2B8%2B%2BkYOflU8T7K6cn%2BzEXD0sJuQrXt3OUElK9cc9U1oUy1dZR9n%2Bl2tBoCvjzsi6UrLgg8zPl0SurOffRMEfNdfvaCglzRxsqnJ0hfbp3QVhTUV%2FGMfPm7DeN%2FIaFiWH30YggBrqehIzq509Vjdh%2FsWxOyZ2qQzk1iySp207reqk4cdTN4ZBQEg0QmHkPbst%2FNoR%2Bq%2FTelwf3h672qVywVmWRLTY2wV4%2FxzW4SDxdNYb7D8L%2BCxkRMwJqZTK45MS1TAjhS2BrAvFdXXk2Ma536XI%2FYA6ke7SJDEJ1ZxFtBYE8TvCuOdJq06dWiNBAAWgeP%2BVMBXY2j3aiDrle6KsJ0N0bxJloaA%2FjbyXOhjCH04K9BjqnARnKx9GBlAFGTah7yyNiEdxmzy3ZZN%2BbKxu2sorrVWvCoIE%2Bfuk3LDruqCbZ68MG7LU7AN%2B1XkuEa6o1faS6%2B71PtcaZY1yalYDu4ToYvwVPJIOpv6LXEvfZB7S4O%2Ba%2FiAgz21flflLAZqCtDsL1v9QUlbxvuFkzjEeHx%2FgLWsAtgLgs6k%2BPnoqwEK3awIdZ7Lr9RUOzsE22PJPJjT9PNsX8cmJc7LAH&X-Amz-Signature=1210790470b63c8a54998129b9a2bed0d6ca7f988e2aa7d5877752d792a55d35&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SJEZXUB%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJFMEMCHyeNBTG78EeGm6HqBdhmGLnlGaP0SOZh5BChoEyndLsCIBss9%2FsaUTefE54m0p19dxDV9%2FAgHPECvf9PgEyA9HUcKv8DCBUQABoMNjM3NDIzMTgzODA1IgwX6wLYyuXp9NpVEUUq3APMNjyd9JcN1ngE5YDnPwNLm4NptgFkW1gxRdljn52PuWbdgZhvoPmtKbFzqXqJZ%2B0SoEMcQNnANR9txlzsnpGZZ2SLe%2B%2BqmIGcs%2FUoLdt1Ib%2Fkd97vuSvNWyiuYW1WK6%2FVCLKI8Z%2F%2B3E0IHuMnUrlocDqx11GWOV%2B61VyPJOud35%2F2VpAuVHGanBb4v7PLGI6NJcaXRpAcYo4TTn3vsYTztX2nvCR392jICX679SxgJg8buNGBth8X3g9gKUg7BmIgry7tHo9wME74Zxd9vpy%2B8%2B%2BkYOflU8T7K6cn%2BzEXD0sJuQrXt3OUElK9cc9U1oUy1dZR9n%2Bl2tBoCvjzsi6UrLgg8zPl0SurOffRMEfNdfvaCglzRxsqnJ0hfbp3QVhTUV%2FGMfPm7DeN%2FIaFiWH30YggBrqehIzq509Vjdh%2FsWxOyZ2qQzk1iySp207reqk4cdTN4ZBQEg0QmHkPbst%2FNoR%2Bq%2FTelwf3h672qVywVmWRLTY2wV4%2FxzW4SDxdNYb7D8L%2BCxkRMwJqZTK45MS1TAjhS2BrAvFdXXk2Ma536XI%2FYA6ke7SJDEJ1ZxFtBYE8TvCuOdJq06dWiNBAAWgeP%2BVMBXY2j3aiDrle6KsJ0N0bxJloaA%2FjbyXOhjCH04K9BjqnARnKx9GBlAFGTah7yyNiEdxmzy3ZZN%2BbKxu2sorrVWvCoIE%2Bfuk3LDruqCbZ68MG7LU7AN%2B1XkuEa6o1faS6%2B71PtcaZY1yalYDu4ToYvwVPJIOpv6LXEvfZB7S4O%2Ba%2FiAgz21flflLAZqCtDsL1v9QUlbxvuFkzjEeHx%2FgLWsAtgLgs6k%2BPnoqwEK3awIdZ7Lr9RUOzsE22PJPJjT9PNsX8cmJc7LAH&X-Amz-Signature=03a0d572990be41eedeb2fe094655a7c06090fef5e08b355426a06c894746f72&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SJEZXUB%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJFMEMCHyeNBTG78EeGm6HqBdhmGLnlGaP0SOZh5BChoEyndLsCIBss9%2FsaUTefE54m0p19dxDV9%2FAgHPECvf9PgEyA9HUcKv8DCBUQABoMNjM3NDIzMTgzODA1IgwX6wLYyuXp9NpVEUUq3APMNjyd9JcN1ngE5YDnPwNLm4NptgFkW1gxRdljn52PuWbdgZhvoPmtKbFzqXqJZ%2B0SoEMcQNnANR9txlzsnpGZZ2SLe%2B%2BqmIGcs%2FUoLdt1Ib%2Fkd97vuSvNWyiuYW1WK6%2FVCLKI8Z%2F%2B3E0IHuMnUrlocDqx11GWOV%2B61VyPJOud35%2F2VpAuVHGanBb4v7PLGI6NJcaXRpAcYo4TTn3vsYTztX2nvCR392jICX679SxgJg8buNGBth8X3g9gKUg7BmIgry7tHo9wME74Zxd9vpy%2B8%2B%2BkYOflU8T7K6cn%2BzEXD0sJuQrXt3OUElK9cc9U1oUy1dZR9n%2Bl2tBoCvjzsi6UrLgg8zPl0SurOffRMEfNdfvaCglzRxsqnJ0hfbp3QVhTUV%2FGMfPm7DeN%2FIaFiWH30YggBrqehIzq509Vjdh%2FsWxOyZ2qQzk1iySp207reqk4cdTN4ZBQEg0QmHkPbst%2FNoR%2Bq%2FTelwf3h672qVywVmWRLTY2wV4%2FxzW4SDxdNYb7D8L%2BCxkRMwJqZTK45MS1TAjhS2BrAvFdXXk2Ma536XI%2FYA6ke7SJDEJ1ZxFtBYE8TvCuOdJq06dWiNBAAWgeP%2BVMBXY2j3aiDrle6KsJ0N0bxJloaA%2FjbyXOhjCH04K9BjqnARnKx9GBlAFGTah7yyNiEdxmzy3ZZN%2BbKxu2sorrVWvCoIE%2Bfuk3LDruqCbZ68MG7LU7AN%2B1XkuEa6o1faS6%2B71PtcaZY1yalYDu4ToYvwVPJIOpv6LXEvfZB7S4O%2Ba%2FiAgz21flflLAZqCtDsL1v9QUlbxvuFkzjEeHx%2FgLWsAtgLgs6k%2BPnoqwEK3awIdZ7Lr9RUOzsE22PJPJjT9PNsX8cmJc7LAH&X-Amz-Signature=36e9a4d86cf8a574836abeaf8e4bed30db518dcfac23bce0787fea151cdad452&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SJEZXUB%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJFMEMCHyeNBTG78EeGm6HqBdhmGLnlGaP0SOZh5BChoEyndLsCIBss9%2FsaUTefE54m0p19dxDV9%2FAgHPECvf9PgEyA9HUcKv8DCBUQABoMNjM3NDIzMTgzODA1IgwX6wLYyuXp9NpVEUUq3APMNjyd9JcN1ngE5YDnPwNLm4NptgFkW1gxRdljn52PuWbdgZhvoPmtKbFzqXqJZ%2B0SoEMcQNnANR9txlzsnpGZZ2SLe%2B%2BqmIGcs%2FUoLdt1Ib%2Fkd97vuSvNWyiuYW1WK6%2FVCLKI8Z%2F%2B3E0IHuMnUrlocDqx11GWOV%2B61VyPJOud35%2F2VpAuVHGanBb4v7PLGI6NJcaXRpAcYo4TTn3vsYTztX2nvCR392jICX679SxgJg8buNGBth8X3g9gKUg7BmIgry7tHo9wME74Zxd9vpy%2B8%2B%2BkYOflU8T7K6cn%2BzEXD0sJuQrXt3OUElK9cc9U1oUy1dZR9n%2Bl2tBoCvjzsi6UrLgg8zPl0SurOffRMEfNdfvaCglzRxsqnJ0hfbp3QVhTUV%2FGMfPm7DeN%2FIaFiWH30YggBrqehIzq509Vjdh%2FsWxOyZ2qQzk1iySp207reqk4cdTN4ZBQEg0QmHkPbst%2FNoR%2Bq%2FTelwf3h672qVywVmWRLTY2wV4%2FxzW4SDxdNYb7D8L%2BCxkRMwJqZTK45MS1TAjhS2BrAvFdXXk2Ma536XI%2FYA6ke7SJDEJ1ZxFtBYE8TvCuOdJq06dWiNBAAWgeP%2BVMBXY2j3aiDrle6KsJ0N0bxJloaA%2FjbyXOhjCH04K9BjqnARnKx9GBlAFGTah7yyNiEdxmzy3ZZN%2BbKxu2sorrVWvCoIE%2Bfuk3LDruqCbZ68MG7LU7AN%2B1XkuEa6o1faS6%2B71PtcaZY1yalYDu4ToYvwVPJIOpv6LXEvfZB7S4O%2Ba%2FiAgz21flflLAZqCtDsL1v9QUlbxvuFkzjEeHx%2FgLWsAtgLgs6k%2BPnoqwEK3awIdZ7Lr9RUOzsE22PJPJjT9PNsX8cmJc7LAH&X-Amz-Signature=e4284ce21f40fcb979f8bfeb8bdcd8c1f9ef10cc11749c5dcf2b9cb3fe0f8313&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q352GT33%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFpImO0tWfdZvDfSOyjra183JQCg%2BOrIBBeZ%2FNG05TqFAiAAo4bPEhF0PkmHXtUw5ViaW9xn6gF1STSd4p44Mo3fISr%2FAwgVEAAaDDYzNzQyMzE4MzgwNSIMQd2%2B7mJujIeDbOHvKtwD1hz6hlfQu5SIT%2FfH%2B85X0YFF0gV0ddk5KpuZvHIlIV%2BntB3rJk9i6hRQAeIbtt%2FF5SFUkPeYlNO7m8uABoPH3mm1ty2zR%2BCthHyzoEelE4X46FB%2FBQrGxDjxlZxvXjDOTm7ZKAQhxngDsmLvjBcZdBi6raHiKbIjfn0WZvrt3Qe8Psd4tISDGUR2zY69McKtz%2Fcr%2B%2F19UHEwTw1HVzT7rjxr7COp2ibKwyxPnBGrlgh8hvrjfSeu5oL%2F2yzzXF8Erl1hvhnHOMrlE3xsLft%2FWYiEroTq3d3Qktc%2BVI%2BgIbpZdXGCkigK%2BHNUFzbP1oHZpEhHgT4S%2F%2BrOHRXaSL29%2BBCTKNzBEWPQYuKDQWkeILvU0CcT3yjqim9DXzTwjaF%2BR7NtqWNaxynBwIOpDiFFkwnU4YyUL%2F44dePMYlaVMwMEoyt0wQE34OCtcbITj%2FlLRH3OZKJuFssCM%2BesewiruCYu3q88k7ofkc0bs3eMktwiQK5wnJ%2FUxPYHcOdEZNv%2BPh4%2B1skW3odSZzVXIKqyGnh2%2BT4sMksL78UPk5PsTrB%2BTDNMF9ODH9A5Hk0cka%2BCiyrwz3%2FuMPi4UqXU9w4KBn%2FsKEkrlwY04m7Cc4Kqcg1%2FKYahaXbyPbKaTy0wxtKCvQY6pgHGDuEG%2BuQEoZpeLVZiNOKJKPmIbz8TPcYg21oWGUv06VTbI5cSAC%2BAq%2BjdPzpKrO93a5u7o%2Bp%2F6DvHIOgF48ge%2BNQaNulUCkevNjlP80KOeS8hEX2XvxQobeRnO%2FLxUIB7lBUFvIoFVzeBsGiyAE5FB%2BNpTVaS71tu8iyQ%2FYEhzsT%2F2%2BnKfdldB5rPsKDkzRkqqxmwl4c1qBUJPOuiUuQUuDXQoEss&X-Amz-Signature=0ce452c2c7798377ff914e190ed08ed71ef287239713cab7057e14fd4b86a07d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q352GT33%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFpImO0tWfdZvDfSOyjra183JQCg%2BOrIBBeZ%2FNG05TqFAiAAo4bPEhF0PkmHXtUw5ViaW9xn6gF1STSd4p44Mo3fISr%2FAwgVEAAaDDYzNzQyMzE4MzgwNSIMQd2%2B7mJujIeDbOHvKtwD1hz6hlfQu5SIT%2FfH%2B85X0YFF0gV0ddk5KpuZvHIlIV%2BntB3rJk9i6hRQAeIbtt%2FF5SFUkPeYlNO7m8uABoPH3mm1ty2zR%2BCthHyzoEelE4X46FB%2FBQrGxDjxlZxvXjDOTm7ZKAQhxngDsmLvjBcZdBi6raHiKbIjfn0WZvrt3Qe8Psd4tISDGUR2zY69McKtz%2Fcr%2B%2F19UHEwTw1HVzT7rjxr7COp2ibKwyxPnBGrlgh8hvrjfSeu5oL%2F2yzzXF8Erl1hvhnHOMrlE3xsLft%2FWYiEroTq3d3Qktc%2BVI%2BgIbpZdXGCkigK%2BHNUFzbP1oHZpEhHgT4S%2F%2BrOHRXaSL29%2BBCTKNzBEWPQYuKDQWkeILvU0CcT3yjqim9DXzTwjaF%2BR7NtqWNaxynBwIOpDiFFkwnU4YyUL%2F44dePMYlaVMwMEoyt0wQE34OCtcbITj%2FlLRH3OZKJuFssCM%2BesewiruCYu3q88k7ofkc0bs3eMktwiQK5wnJ%2FUxPYHcOdEZNv%2BPh4%2B1skW3odSZzVXIKqyGnh2%2BT4sMksL78UPk5PsTrB%2BTDNMF9ODH9A5Hk0cka%2BCiyrwz3%2FuMPi4UqXU9w4KBn%2FsKEkrlwY04m7Cc4Kqcg1%2FKYahaXbyPbKaTy0wxtKCvQY6pgHGDuEG%2BuQEoZpeLVZiNOKJKPmIbz8TPcYg21oWGUv06VTbI5cSAC%2BAq%2BjdPzpKrO93a5u7o%2Bp%2F6DvHIOgF48ge%2BNQaNulUCkevNjlP80KOeS8hEX2XvxQobeRnO%2FLxUIB7lBUFvIoFVzeBsGiyAE5FB%2BNpTVaS71tu8iyQ%2FYEhzsT%2F2%2BnKfdldB5rPsKDkzRkqqxmwl4c1qBUJPOuiUuQUuDXQoEss&X-Amz-Signature=51b1b7a91c7dfd9cb36c72738fd9799baa626ec63ddc45d8b28222d2ee9738bd&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
