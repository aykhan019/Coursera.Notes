

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466546ZK44V%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJGMEQCIE1lLQUBXAcPJi0JIg9gQP1nnfBgtENcia7QXv%2BDlaeEAiALONpe5Yv4QTKPP%2BKH8KoR%2FlT8X2hiR8M%2FYl8YnlA6QiqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMyDuy7E1KTuy5R7LQKtwD%2BLFZqKwPvSuQtrWJy7Pu9zF3oi0AkuOzI94Z2cp0nxdqytT1DRYHS0fKEGBsVEWoxC5k8olL21sDe5fL9bkPVKmv5SFQH8tS4BJUybGo16i1bvIa2JVMCkhRO3UUS2i1ZIstx2QckGrq%2Ff1K9fR7fc%2B29wAgL3cu7nVCeW3jth%2B0mHISkVeyab3TNdNsLhP1dPJCT%2Bflv2APNYcWzyP3eKof8lMV%2F72B1Ptmrz2SN6SGPXygoZZqv2ljqyIrVPJjlFvv4GVTRvTjM%2BK5%2Fo7pNZdMOFggx8%2Fd%2BsjDRCNAswdK9r%2FTsbdx8xLLKHNigmqDhK9B5jdLxhCybOc2VPj%2BIjdBsVchdx6ufGOlWuK9WY%2FxTJLtu4yibmZfk%2FETdxvnPEbXZbNDWLX2hmICQt8fQQ0gLLvVKJiNKNzJbjLWNw6tNbm%2BbnkyEL%2BlO1uoPGE2coIvXxlLX6GwWrtgrTuD3xxFkcyXumIy15SJ3e4ew1Hm3RrPlYysV8mF5jMR%2BJxbHou7g4e10lK86YK1vySEevjXXalNyS%2FnvSc5Yaf8Dj%2BZuuv5bgWbjniAjBY5mQqP%2F38iqWcEI4nItWElniZ0SNgIrS9fHpvuXng2pNgj2OpqHR4VN3KC4xN4hWMwz%2B%2BbvQY6pgEJay0gU7cmRspExsCfpVxAM5NdTQydgZRLcus%2BYcWienSMh2yORy9s0qSHsi0RhxsWM1HGK5%2BzsCkViNAyLJcOsseaSz36Tf9zkr9qlB%2Bo%2FpA%2Fh0pFsdRyp0xoBm1wNBI8iFTMWACGBORcA7m4FRnpAZQGqKhAc6PeGnAdEGmeOgJ6TLuAvXTzGfJ5VVb5zAQeWVGLQojFgXY1R8xM9XXPn696V3oY&X-Amz-Signature=111c01a25f512ee7afc1162f719eef9b2ea9288b8cb1704a65d632b91fa77b7d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466546ZK44V%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJGMEQCIE1lLQUBXAcPJi0JIg9gQP1nnfBgtENcia7QXv%2BDlaeEAiALONpe5Yv4QTKPP%2BKH8KoR%2FlT8X2hiR8M%2FYl8YnlA6QiqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMyDuy7E1KTuy5R7LQKtwD%2BLFZqKwPvSuQtrWJy7Pu9zF3oi0AkuOzI94Z2cp0nxdqytT1DRYHS0fKEGBsVEWoxC5k8olL21sDe5fL9bkPVKmv5SFQH8tS4BJUybGo16i1bvIa2JVMCkhRO3UUS2i1ZIstx2QckGrq%2Ff1K9fR7fc%2B29wAgL3cu7nVCeW3jth%2B0mHISkVeyab3TNdNsLhP1dPJCT%2Bflv2APNYcWzyP3eKof8lMV%2F72B1Ptmrz2SN6SGPXygoZZqv2ljqyIrVPJjlFvv4GVTRvTjM%2BK5%2Fo7pNZdMOFggx8%2Fd%2BsjDRCNAswdK9r%2FTsbdx8xLLKHNigmqDhK9B5jdLxhCybOc2VPj%2BIjdBsVchdx6ufGOlWuK9WY%2FxTJLtu4yibmZfk%2FETdxvnPEbXZbNDWLX2hmICQt8fQQ0gLLvVKJiNKNzJbjLWNw6tNbm%2BbnkyEL%2BlO1uoPGE2coIvXxlLX6GwWrtgrTuD3xxFkcyXumIy15SJ3e4ew1Hm3RrPlYysV8mF5jMR%2BJxbHou7g4e10lK86YK1vySEevjXXalNyS%2FnvSc5Yaf8Dj%2BZuuv5bgWbjniAjBY5mQqP%2F38iqWcEI4nItWElniZ0SNgIrS9fHpvuXng2pNgj2OpqHR4VN3KC4xN4hWMwz%2B%2BbvQY6pgEJay0gU7cmRspExsCfpVxAM5NdTQydgZRLcus%2BYcWienSMh2yORy9s0qSHsi0RhxsWM1HGK5%2BzsCkViNAyLJcOsseaSz36Tf9zkr9qlB%2Bo%2FpA%2Fh0pFsdRyp0xoBm1wNBI8iFTMWACGBORcA7m4FRnpAZQGqKhAc6PeGnAdEGmeOgJ6TLuAvXTzGfJ5VVb5zAQeWVGLQojFgXY1R8xM9XXPn696V3oY&X-Amz-Signature=0f422b80299048b1d5b1e134d135ea9bab8e5ccc5fcb97e2178e0d100b606685&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466546ZK44V%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJGMEQCIE1lLQUBXAcPJi0JIg9gQP1nnfBgtENcia7QXv%2BDlaeEAiALONpe5Yv4QTKPP%2BKH8KoR%2FlT8X2hiR8M%2FYl8YnlA6QiqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMyDuy7E1KTuy5R7LQKtwD%2BLFZqKwPvSuQtrWJy7Pu9zF3oi0AkuOzI94Z2cp0nxdqytT1DRYHS0fKEGBsVEWoxC5k8olL21sDe5fL9bkPVKmv5SFQH8tS4BJUybGo16i1bvIa2JVMCkhRO3UUS2i1ZIstx2QckGrq%2Ff1K9fR7fc%2B29wAgL3cu7nVCeW3jth%2B0mHISkVeyab3TNdNsLhP1dPJCT%2Bflv2APNYcWzyP3eKof8lMV%2F72B1Ptmrz2SN6SGPXygoZZqv2ljqyIrVPJjlFvv4GVTRvTjM%2BK5%2Fo7pNZdMOFggx8%2Fd%2BsjDRCNAswdK9r%2FTsbdx8xLLKHNigmqDhK9B5jdLxhCybOc2VPj%2BIjdBsVchdx6ufGOlWuK9WY%2FxTJLtu4yibmZfk%2FETdxvnPEbXZbNDWLX2hmICQt8fQQ0gLLvVKJiNKNzJbjLWNw6tNbm%2BbnkyEL%2BlO1uoPGE2coIvXxlLX6GwWrtgrTuD3xxFkcyXumIy15SJ3e4ew1Hm3RrPlYysV8mF5jMR%2BJxbHou7g4e10lK86YK1vySEevjXXalNyS%2FnvSc5Yaf8Dj%2BZuuv5bgWbjniAjBY5mQqP%2F38iqWcEI4nItWElniZ0SNgIrS9fHpvuXng2pNgj2OpqHR4VN3KC4xN4hWMwz%2B%2BbvQY6pgEJay0gU7cmRspExsCfpVxAM5NdTQydgZRLcus%2BYcWienSMh2yORy9s0qSHsi0RhxsWM1HGK5%2BzsCkViNAyLJcOsseaSz36Tf9zkr9qlB%2Bo%2FpA%2Fh0pFsdRyp0xoBm1wNBI8iFTMWACGBORcA7m4FRnpAZQGqKhAc6PeGnAdEGmeOgJ6TLuAvXTzGfJ5VVb5zAQeWVGLQojFgXY1R8xM9XXPn696V3oY&X-Amz-Signature=79fb4d5c8941db7a9c2cbe37733d85ccab444bd887ee2166653eb5036487a22c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466546ZK44V%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJGMEQCIE1lLQUBXAcPJi0JIg9gQP1nnfBgtENcia7QXv%2BDlaeEAiALONpe5Yv4QTKPP%2BKH8KoR%2FlT8X2hiR8M%2FYl8YnlA6QiqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMyDuy7E1KTuy5R7LQKtwD%2BLFZqKwPvSuQtrWJy7Pu9zF3oi0AkuOzI94Z2cp0nxdqytT1DRYHS0fKEGBsVEWoxC5k8olL21sDe5fL9bkPVKmv5SFQH8tS4BJUybGo16i1bvIa2JVMCkhRO3UUS2i1ZIstx2QckGrq%2Ff1K9fR7fc%2B29wAgL3cu7nVCeW3jth%2B0mHISkVeyab3TNdNsLhP1dPJCT%2Bflv2APNYcWzyP3eKof8lMV%2F72B1Ptmrz2SN6SGPXygoZZqv2ljqyIrVPJjlFvv4GVTRvTjM%2BK5%2Fo7pNZdMOFggx8%2Fd%2BsjDRCNAswdK9r%2FTsbdx8xLLKHNigmqDhK9B5jdLxhCybOc2VPj%2BIjdBsVchdx6ufGOlWuK9WY%2FxTJLtu4yibmZfk%2FETdxvnPEbXZbNDWLX2hmICQt8fQQ0gLLvVKJiNKNzJbjLWNw6tNbm%2BbnkyEL%2BlO1uoPGE2coIvXxlLX6GwWrtgrTuD3xxFkcyXumIy15SJ3e4ew1Hm3RrPlYysV8mF5jMR%2BJxbHou7g4e10lK86YK1vySEevjXXalNyS%2FnvSc5Yaf8Dj%2BZuuv5bgWbjniAjBY5mQqP%2F38iqWcEI4nItWElniZ0SNgIrS9fHpvuXng2pNgj2OpqHR4VN3KC4xN4hWMwz%2B%2BbvQY6pgEJay0gU7cmRspExsCfpVxAM5NdTQydgZRLcus%2BYcWienSMh2yORy9s0qSHsi0RhxsWM1HGK5%2BzsCkViNAyLJcOsseaSz36Tf9zkr9qlB%2Bo%2FpA%2Fh0pFsdRyp0xoBm1wNBI8iFTMWACGBORcA7m4FRnpAZQGqKhAc6PeGnAdEGmeOgJ6TLuAvXTzGfJ5VVb5zAQeWVGLQojFgXY1R8xM9XXPn696V3oY&X-Amz-Signature=843112433dd1a69e42bde21955331491629c5da9829f0926989e3b36a537c7ce&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466546ZK44V%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJGMEQCIE1lLQUBXAcPJi0JIg9gQP1nnfBgtENcia7QXv%2BDlaeEAiALONpe5Yv4QTKPP%2BKH8KoR%2FlT8X2hiR8M%2FYl8YnlA6QiqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMyDuy7E1KTuy5R7LQKtwD%2BLFZqKwPvSuQtrWJy7Pu9zF3oi0AkuOzI94Z2cp0nxdqytT1DRYHS0fKEGBsVEWoxC5k8olL21sDe5fL9bkPVKmv5SFQH8tS4BJUybGo16i1bvIa2JVMCkhRO3UUS2i1ZIstx2QckGrq%2Ff1K9fR7fc%2B29wAgL3cu7nVCeW3jth%2B0mHISkVeyab3TNdNsLhP1dPJCT%2Bflv2APNYcWzyP3eKof8lMV%2F72B1Ptmrz2SN6SGPXygoZZqv2ljqyIrVPJjlFvv4GVTRvTjM%2BK5%2Fo7pNZdMOFggx8%2Fd%2BsjDRCNAswdK9r%2FTsbdx8xLLKHNigmqDhK9B5jdLxhCybOc2VPj%2BIjdBsVchdx6ufGOlWuK9WY%2FxTJLtu4yibmZfk%2FETdxvnPEbXZbNDWLX2hmICQt8fQQ0gLLvVKJiNKNzJbjLWNw6tNbm%2BbnkyEL%2BlO1uoPGE2coIvXxlLX6GwWrtgrTuD3xxFkcyXumIy15SJ3e4ew1Hm3RrPlYysV8mF5jMR%2BJxbHou7g4e10lK86YK1vySEevjXXalNyS%2FnvSc5Yaf8Dj%2BZuuv5bgWbjniAjBY5mQqP%2F38iqWcEI4nItWElniZ0SNgIrS9fHpvuXng2pNgj2OpqHR4VN3KC4xN4hWMwz%2B%2BbvQY6pgEJay0gU7cmRspExsCfpVxAM5NdTQydgZRLcus%2BYcWienSMh2yORy9s0qSHsi0RhxsWM1HGK5%2BzsCkViNAyLJcOsseaSz36Tf9zkr9qlB%2Bo%2FpA%2Fh0pFsdRyp0xoBm1wNBI8iFTMWACGBORcA7m4FRnpAZQGqKhAc6PeGnAdEGmeOgJ6TLuAvXTzGfJ5VVb5zAQeWVGLQojFgXY1R8xM9XXPn696V3oY&X-Amz-Signature=26cb1553b93847d4881b9487d8ae1cc89f64131317072f72ddc22bfa38156c1b&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466546ZK44V%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJGMEQCIE1lLQUBXAcPJi0JIg9gQP1nnfBgtENcia7QXv%2BDlaeEAiALONpe5Yv4QTKPP%2BKH8KoR%2FlT8X2hiR8M%2FYl8YnlA6QiqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMyDuy7E1KTuy5R7LQKtwD%2BLFZqKwPvSuQtrWJy7Pu9zF3oi0AkuOzI94Z2cp0nxdqytT1DRYHS0fKEGBsVEWoxC5k8olL21sDe5fL9bkPVKmv5SFQH8tS4BJUybGo16i1bvIa2JVMCkhRO3UUS2i1ZIstx2QckGrq%2Ff1K9fR7fc%2B29wAgL3cu7nVCeW3jth%2B0mHISkVeyab3TNdNsLhP1dPJCT%2Bflv2APNYcWzyP3eKof8lMV%2F72B1Ptmrz2SN6SGPXygoZZqv2ljqyIrVPJjlFvv4GVTRvTjM%2BK5%2Fo7pNZdMOFggx8%2Fd%2BsjDRCNAswdK9r%2FTsbdx8xLLKHNigmqDhK9B5jdLxhCybOc2VPj%2BIjdBsVchdx6ufGOlWuK9WY%2FxTJLtu4yibmZfk%2FETdxvnPEbXZbNDWLX2hmICQt8fQQ0gLLvVKJiNKNzJbjLWNw6tNbm%2BbnkyEL%2BlO1uoPGE2coIvXxlLX6GwWrtgrTuD3xxFkcyXumIy15SJ3e4ew1Hm3RrPlYysV8mF5jMR%2BJxbHou7g4e10lK86YK1vySEevjXXalNyS%2FnvSc5Yaf8Dj%2BZuuv5bgWbjniAjBY5mQqP%2F38iqWcEI4nItWElniZ0SNgIrS9fHpvuXng2pNgj2OpqHR4VN3KC4xN4hWMwz%2B%2BbvQY6pgEJay0gU7cmRspExsCfpVxAM5NdTQydgZRLcus%2BYcWienSMh2yORy9s0qSHsi0RhxsWM1HGK5%2BzsCkViNAyLJcOsseaSz36Tf9zkr9qlB%2Bo%2FpA%2Fh0pFsdRyp0xoBm1wNBI8iFTMWACGBORcA7m4FRnpAZQGqKhAc6PeGnAdEGmeOgJ6TLuAvXTzGfJ5VVb5zAQeWVGLQojFgXY1R8xM9XXPn696V3oY&X-Amz-Signature=25c500b40a0d1ab98fa05a3d9b7a0ad55963e96ae702a387f5a32caaaf9d4045&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466546ZK44V%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJGMEQCIE1lLQUBXAcPJi0JIg9gQP1nnfBgtENcia7QXv%2BDlaeEAiALONpe5Yv4QTKPP%2BKH8KoR%2FlT8X2hiR8M%2FYl8YnlA6QiqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMyDuy7E1KTuy5R7LQKtwD%2BLFZqKwPvSuQtrWJy7Pu9zF3oi0AkuOzI94Z2cp0nxdqytT1DRYHS0fKEGBsVEWoxC5k8olL21sDe5fL9bkPVKmv5SFQH8tS4BJUybGo16i1bvIa2JVMCkhRO3UUS2i1ZIstx2QckGrq%2Ff1K9fR7fc%2B29wAgL3cu7nVCeW3jth%2B0mHISkVeyab3TNdNsLhP1dPJCT%2Bflv2APNYcWzyP3eKof8lMV%2F72B1Ptmrz2SN6SGPXygoZZqv2ljqyIrVPJjlFvv4GVTRvTjM%2BK5%2Fo7pNZdMOFggx8%2Fd%2BsjDRCNAswdK9r%2FTsbdx8xLLKHNigmqDhK9B5jdLxhCybOc2VPj%2BIjdBsVchdx6ufGOlWuK9WY%2FxTJLtu4yibmZfk%2FETdxvnPEbXZbNDWLX2hmICQt8fQQ0gLLvVKJiNKNzJbjLWNw6tNbm%2BbnkyEL%2BlO1uoPGE2coIvXxlLX6GwWrtgrTuD3xxFkcyXumIy15SJ3e4ew1Hm3RrPlYysV8mF5jMR%2BJxbHou7g4e10lK86YK1vySEevjXXalNyS%2FnvSc5Yaf8Dj%2BZuuv5bgWbjniAjBY5mQqP%2F38iqWcEI4nItWElniZ0SNgIrS9fHpvuXng2pNgj2OpqHR4VN3KC4xN4hWMwz%2B%2BbvQY6pgEJay0gU7cmRspExsCfpVxAM5NdTQydgZRLcus%2BYcWienSMh2yORy9s0qSHsi0RhxsWM1HGK5%2BzsCkViNAyLJcOsseaSz36Tf9zkr9qlB%2Bo%2FpA%2Fh0pFsdRyp0xoBm1wNBI8iFTMWACGBORcA7m4FRnpAZQGqKhAc6PeGnAdEGmeOgJ6TLuAvXTzGfJ5VVb5zAQeWVGLQojFgXY1R8xM9XXPn696V3oY&X-Amz-Signature=003720e5a572cc42184ac4bbf11f18be61bc7ac2f874bcdef0bc6612ba797320&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466546ZK44V%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJGMEQCIE1lLQUBXAcPJi0JIg9gQP1nnfBgtENcia7QXv%2BDlaeEAiALONpe5Yv4QTKPP%2BKH8KoR%2FlT8X2hiR8M%2FYl8YnlA6QiqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMyDuy7E1KTuy5R7LQKtwD%2BLFZqKwPvSuQtrWJy7Pu9zF3oi0AkuOzI94Z2cp0nxdqytT1DRYHS0fKEGBsVEWoxC5k8olL21sDe5fL9bkPVKmv5SFQH8tS4BJUybGo16i1bvIa2JVMCkhRO3UUS2i1ZIstx2QckGrq%2Ff1K9fR7fc%2B29wAgL3cu7nVCeW3jth%2B0mHISkVeyab3TNdNsLhP1dPJCT%2Bflv2APNYcWzyP3eKof8lMV%2F72B1Ptmrz2SN6SGPXygoZZqv2ljqyIrVPJjlFvv4GVTRvTjM%2BK5%2Fo7pNZdMOFggx8%2Fd%2BsjDRCNAswdK9r%2FTsbdx8xLLKHNigmqDhK9B5jdLxhCybOc2VPj%2BIjdBsVchdx6ufGOlWuK9WY%2FxTJLtu4yibmZfk%2FETdxvnPEbXZbNDWLX2hmICQt8fQQ0gLLvVKJiNKNzJbjLWNw6tNbm%2BbnkyEL%2BlO1uoPGE2coIvXxlLX6GwWrtgrTuD3xxFkcyXumIy15SJ3e4ew1Hm3RrPlYysV8mF5jMR%2BJxbHou7g4e10lK86YK1vySEevjXXalNyS%2FnvSc5Yaf8Dj%2BZuuv5bgWbjniAjBY5mQqP%2F38iqWcEI4nItWElniZ0SNgIrS9fHpvuXng2pNgj2OpqHR4VN3KC4xN4hWMwz%2B%2BbvQY6pgEJay0gU7cmRspExsCfpVxAM5NdTQydgZRLcus%2BYcWienSMh2yORy9s0qSHsi0RhxsWM1HGK5%2BzsCkViNAyLJcOsseaSz36Tf9zkr9qlB%2Bo%2FpA%2Fh0pFsdRyp0xoBm1wNBI8iFTMWACGBORcA7m4FRnpAZQGqKhAc6PeGnAdEGmeOgJ6TLuAvXTzGfJ5VVb5zAQeWVGLQojFgXY1R8xM9XXPn696V3oY&X-Amz-Signature=dae07d778a4097749560f058528789d68c604a17ae42ae347f56e1fce25017fa&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466546ZK44V%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJGMEQCIE1lLQUBXAcPJi0JIg9gQP1nnfBgtENcia7QXv%2BDlaeEAiALONpe5Yv4QTKPP%2BKH8KoR%2FlT8X2hiR8M%2FYl8YnlA6QiqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMyDuy7E1KTuy5R7LQKtwD%2BLFZqKwPvSuQtrWJy7Pu9zF3oi0AkuOzI94Z2cp0nxdqytT1DRYHS0fKEGBsVEWoxC5k8olL21sDe5fL9bkPVKmv5SFQH8tS4BJUybGo16i1bvIa2JVMCkhRO3UUS2i1ZIstx2QckGrq%2Ff1K9fR7fc%2B29wAgL3cu7nVCeW3jth%2B0mHISkVeyab3TNdNsLhP1dPJCT%2Bflv2APNYcWzyP3eKof8lMV%2F72B1Ptmrz2SN6SGPXygoZZqv2ljqyIrVPJjlFvv4GVTRvTjM%2BK5%2Fo7pNZdMOFggx8%2Fd%2BsjDRCNAswdK9r%2FTsbdx8xLLKHNigmqDhK9B5jdLxhCybOc2VPj%2BIjdBsVchdx6ufGOlWuK9WY%2FxTJLtu4yibmZfk%2FETdxvnPEbXZbNDWLX2hmICQt8fQQ0gLLvVKJiNKNzJbjLWNw6tNbm%2BbnkyEL%2BlO1uoPGE2coIvXxlLX6GwWrtgrTuD3xxFkcyXumIy15SJ3e4ew1Hm3RrPlYysV8mF5jMR%2BJxbHou7g4e10lK86YK1vySEevjXXalNyS%2FnvSc5Yaf8Dj%2BZuuv5bgWbjniAjBY5mQqP%2F38iqWcEI4nItWElniZ0SNgIrS9fHpvuXng2pNgj2OpqHR4VN3KC4xN4hWMwz%2B%2BbvQY6pgEJay0gU7cmRspExsCfpVxAM5NdTQydgZRLcus%2BYcWienSMh2yORy9s0qSHsi0RhxsWM1HGK5%2BzsCkViNAyLJcOsseaSz36Tf9zkr9qlB%2Bo%2FpA%2Fh0pFsdRyp0xoBm1wNBI8iFTMWACGBORcA7m4FRnpAZQGqKhAc6PeGnAdEGmeOgJ6TLuAvXTzGfJ5VVb5zAQeWVGLQojFgXY1R8xM9XXPn696V3oY&X-Amz-Signature=7fc4a5ccf0e771c7946e4da49f43fca79b276f5bcbea7823a69ee7530f2de1ca&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VKRRYJNR%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJHMEUCIC%2BJQ2vGf1FaPNIWUS%2F21ygjP2%2FnMu0y4%2B9ys%2FsNqgPfAiEAy%2FaWIfYsYW7Iypnsws69r6KDRsswb%2FqTYHEenN%2BMWf4qiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC3me%2BP6kzYpeD%2BrPircAy7nhXu8Ln9b0UmPRJZaab2yP4LJ2%2FFwsCyHAvke77mhtaa%2FdEs6xJmaVM9uyk676AuqnQBb5V2LiZIY%2F7uXVqwhEQdTBzHUYFPzVuVLkFv%2BCaUQcryWAHvEAaO0EIVOpE7A%2BcvkYu8T2%2BAFKqcoyBWXuMrqtuqIftm6Eh%2BEY4mlwysoNNSDd1iZ%2BGudt8eW2fFseXgE9o7kRhYJbpM6STfebFpzZesyZVMsFplwa%2BC%2FxCAZfNdurpJjYfSeAAKiuIUy0N%2FQ154%2FzD7qGGaYtGRg%2Fh5n4IH4v3nvMg%2FVsDkgOTvz7sU0GalLI1HfMZC8fAAum4QjEf1bsx8kI3fOKdxK3Av4ZLOyCKGH%2BEl2Hj32zDS3zHTPml0l99fi%2FKO3tjBwGmyQ0yiGwhRNzNjzDnRdJVVW3I0vshAr0P%2Fh1PuwZbiWWiKSJ4t6049vzWo3fh1eycPN7UxQqTm%2F9C3scgxplSgSjYXhLN1KwOt3KiZ0pC4pRRby%2BwzVdlH4PRsob2wffxkTZAMVebmtz3pNfPW7EH8dkh15hZmT1gt38f7U30gf%2BHThrvqqqvzheN2gLobaE%2FZzUipirvD5HWLo%2Fx9rDRaOI3WhHm%2F25IZR3ooFIdZaFjuwkWTSaCH3MLvvm70GOqUBmkL4e88Qc4h3Y4bVKSL7Kzr6c9%2FN4SYyuYVKvT07mjQTYI9pOF%2Fs5CvvgbgQUqI7hPP0XPkHipFfYW1MwA9diUM7R8H238FwHJoX8hP4XLQY%2BV3Z%2FtGdLhe0vwbQOw4gLVizJEG1pZRD7ZAIQ5mfwVnRxNJIEYpO7PLaNP7R1bPUsfKxnqdmd4Fp272g2jLHlqvEPWFyA%2B0%2BVFaq0%2B3%2B%2Fqgia098&X-Amz-Signature=6b0863bd072b7e5e0cc98287b819fcdbc5450f5eb2577c2e47333056074b9139&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VKRRYJNR%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJHMEUCIC%2BJQ2vGf1FaPNIWUS%2F21ygjP2%2FnMu0y4%2B9ys%2FsNqgPfAiEAy%2FaWIfYsYW7Iypnsws69r6KDRsswb%2FqTYHEenN%2BMWf4qiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC3me%2BP6kzYpeD%2BrPircAy7nhXu8Ln9b0UmPRJZaab2yP4LJ2%2FFwsCyHAvke77mhtaa%2FdEs6xJmaVM9uyk676AuqnQBb5V2LiZIY%2F7uXVqwhEQdTBzHUYFPzVuVLkFv%2BCaUQcryWAHvEAaO0EIVOpE7A%2BcvkYu8T2%2BAFKqcoyBWXuMrqtuqIftm6Eh%2BEY4mlwysoNNSDd1iZ%2BGudt8eW2fFseXgE9o7kRhYJbpM6STfebFpzZesyZVMsFplwa%2BC%2FxCAZfNdurpJjYfSeAAKiuIUy0N%2FQ154%2FzD7qGGaYtGRg%2Fh5n4IH4v3nvMg%2FVsDkgOTvz7sU0GalLI1HfMZC8fAAum4QjEf1bsx8kI3fOKdxK3Av4ZLOyCKGH%2BEl2Hj32zDS3zHTPml0l99fi%2FKO3tjBwGmyQ0yiGwhRNzNjzDnRdJVVW3I0vshAr0P%2Fh1PuwZbiWWiKSJ4t6049vzWo3fh1eycPN7UxQqTm%2F9C3scgxplSgSjYXhLN1KwOt3KiZ0pC4pRRby%2BwzVdlH4PRsob2wffxkTZAMVebmtz3pNfPW7EH8dkh15hZmT1gt38f7U30gf%2BHThrvqqqvzheN2gLobaE%2FZzUipirvD5HWLo%2Fx9rDRaOI3WhHm%2F25IZR3ooFIdZaFjuwkWTSaCH3MLvvm70GOqUBmkL4e88Qc4h3Y4bVKSL7Kzr6c9%2FN4SYyuYVKvT07mjQTYI9pOF%2Fs5CvvgbgQUqI7hPP0XPkHipFfYW1MwA9diUM7R8H238FwHJoX8hP4XLQY%2BV3Z%2FtGdLhe0vwbQOw4gLVizJEG1pZRD7ZAIQ5mfwVnRxNJIEYpO7PLaNP7R1bPUsfKxnqdmd4Fp272g2jLHlqvEPWFyA%2B0%2BVFaq0%2B3%2B%2Fqgia098&X-Amz-Signature=0f7941f68910b61d8855745a6ad56ae493b4cc135ac28b4e91f300c9deefc018&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
