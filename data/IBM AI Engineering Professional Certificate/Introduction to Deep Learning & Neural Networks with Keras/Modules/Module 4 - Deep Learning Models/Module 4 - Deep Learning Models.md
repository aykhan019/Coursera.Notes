

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UE4ZLRPC%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221427Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQClkfKerv40Lx76ZSgwzkS3855k0M25zap39h8k9UYPwgIhAJ8V7R0D7v4JxrBX73crnun3kwypt9tQHYmqpLMhm4EcKogECN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwLTiE0tGLhKc3hDtUq3ANP86Ouju1CKHqEkCH658P1o0zaYpscLwXG9MZYOpxx3hzgxyahLWfU5Va2arpSjoKFJ3FeJe5VptCrJmcAY8huXdq6T4vZeATGRMIHKn38EVZVi8ifCe2%2Fq7BgHyyI%2FDy7to0moM5sdLyTuKam2xVXkxLD4%2Brt0Ca0J%2FXd629gvPuMK4UY1WT%2B2OEGZlKnWBp4XGyil6PIg%2B7FQtWumHHYJj6OeOpyywjKO2VWS%2FCjpl2QlnT8lZVsukw3x8KagkJtNyIVBLWzCPnODLcyRmdYK1XKUyrkBr9t5KAzAbKnqyrchC%2BN0Mx82ArM8orMA0QpYb9sL1tKGIYLnP5pATzyvRBTyeI465FX%2BipqVBcYKarwc76OobBuK3iwYtEEPTsVFpjLRTDV5r0t0CqG8cuXcmanir39mRh5BNeAEOmqFcRg4%2FZwpFrxKjbWU2eplZDNHITH4Q19O%2Fm9iS9K1CdfADyJiYVGan5dHt%2BApGHie%2FTsgFaDabA5oTapeB27C27Ce%2FYvR8OOysPESFdERuCO6HnLkqUUj3QZBSLMq8T%2BSJcufRx2MMc5tmZTIq8kAXHLEkeWas1sVJ0D1rDDN8s3jl9dYriPzKtVmNp1jzXPfxi7OWlqOu9abZQpojD%2Fsfq8BjqkAXUtsSZ5T9FG0WqgF6OZgGeXb8V2KHpb2LZtHDDpFZj%2Fp2JKmV7uL1oIZJF3zzCvvjl3erkbJFZMBqAVxg62LmoLJvZHgMfP3eFyrFRvLqERgwkD%2FzaQCMjC%2BoVLJKd4tSQynFJPdhBY3FYDeE%2B7LYA6aUtJhenxpLXzBgLNUx1L%2FexQIRBNL9c9B%2FLm3TGGyWBN7JtsdHOSeuQ2NSjf7PmcmG60&X-Amz-Signature=4669c0a35abb4dbc786315182205f11c42554df867cb6ea6dbfff07879263f91&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UE4ZLRPC%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221427Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQClkfKerv40Lx76ZSgwzkS3855k0M25zap39h8k9UYPwgIhAJ8V7R0D7v4JxrBX73crnun3kwypt9tQHYmqpLMhm4EcKogECN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwLTiE0tGLhKc3hDtUq3ANP86Ouju1CKHqEkCH658P1o0zaYpscLwXG9MZYOpxx3hzgxyahLWfU5Va2arpSjoKFJ3FeJe5VptCrJmcAY8huXdq6T4vZeATGRMIHKn38EVZVi8ifCe2%2Fq7BgHyyI%2FDy7to0moM5sdLyTuKam2xVXkxLD4%2Brt0Ca0J%2FXd629gvPuMK4UY1WT%2B2OEGZlKnWBp4XGyil6PIg%2B7FQtWumHHYJj6OeOpyywjKO2VWS%2FCjpl2QlnT8lZVsukw3x8KagkJtNyIVBLWzCPnODLcyRmdYK1XKUyrkBr9t5KAzAbKnqyrchC%2BN0Mx82ArM8orMA0QpYb9sL1tKGIYLnP5pATzyvRBTyeI465FX%2BipqVBcYKarwc76OobBuK3iwYtEEPTsVFpjLRTDV5r0t0CqG8cuXcmanir39mRh5BNeAEOmqFcRg4%2FZwpFrxKjbWU2eplZDNHITH4Q19O%2Fm9iS9K1CdfADyJiYVGan5dHt%2BApGHie%2FTsgFaDabA5oTapeB27C27Ce%2FYvR8OOysPESFdERuCO6HnLkqUUj3QZBSLMq8T%2BSJcufRx2MMc5tmZTIq8kAXHLEkeWas1sVJ0D1rDDN8s3jl9dYriPzKtVmNp1jzXPfxi7OWlqOu9abZQpojD%2Fsfq8BjqkAXUtsSZ5T9FG0WqgF6OZgGeXb8V2KHpb2LZtHDDpFZj%2Fp2JKmV7uL1oIZJF3zzCvvjl3erkbJFZMBqAVxg62LmoLJvZHgMfP3eFyrFRvLqERgwkD%2FzaQCMjC%2BoVLJKd4tSQynFJPdhBY3FYDeE%2B7LYA6aUtJhenxpLXzBgLNUx1L%2FexQIRBNL9c9B%2FLm3TGGyWBN7JtsdHOSeuQ2NSjf7PmcmG60&X-Amz-Signature=bf3c504cbf77e00556a2c6251ddfc81353f7d48b662410888387843cad30294b&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UE4ZLRPC%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221427Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQClkfKerv40Lx76ZSgwzkS3855k0M25zap39h8k9UYPwgIhAJ8V7R0D7v4JxrBX73crnun3kwypt9tQHYmqpLMhm4EcKogECN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwLTiE0tGLhKc3hDtUq3ANP86Ouju1CKHqEkCH658P1o0zaYpscLwXG9MZYOpxx3hzgxyahLWfU5Va2arpSjoKFJ3FeJe5VptCrJmcAY8huXdq6T4vZeATGRMIHKn38EVZVi8ifCe2%2Fq7BgHyyI%2FDy7to0moM5sdLyTuKam2xVXkxLD4%2Brt0Ca0J%2FXd629gvPuMK4UY1WT%2B2OEGZlKnWBp4XGyil6PIg%2B7FQtWumHHYJj6OeOpyywjKO2VWS%2FCjpl2QlnT8lZVsukw3x8KagkJtNyIVBLWzCPnODLcyRmdYK1XKUyrkBr9t5KAzAbKnqyrchC%2BN0Mx82ArM8orMA0QpYb9sL1tKGIYLnP5pATzyvRBTyeI465FX%2BipqVBcYKarwc76OobBuK3iwYtEEPTsVFpjLRTDV5r0t0CqG8cuXcmanir39mRh5BNeAEOmqFcRg4%2FZwpFrxKjbWU2eplZDNHITH4Q19O%2Fm9iS9K1CdfADyJiYVGan5dHt%2BApGHie%2FTsgFaDabA5oTapeB27C27Ce%2FYvR8OOysPESFdERuCO6HnLkqUUj3QZBSLMq8T%2BSJcufRx2MMc5tmZTIq8kAXHLEkeWas1sVJ0D1rDDN8s3jl9dYriPzKtVmNp1jzXPfxi7OWlqOu9abZQpojD%2Fsfq8BjqkAXUtsSZ5T9FG0WqgF6OZgGeXb8V2KHpb2LZtHDDpFZj%2Fp2JKmV7uL1oIZJF3zzCvvjl3erkbJFZMBqAVxg62LmoLJvZHgMfP3eFyrFRvLqERgwkD%2FzaQCMjC%2BoVLJKd4tSQynFJPdhBY3FYDeE%2B7LYA6aUtJhenxpLXzBgLNUx1L%2FexQIRBNL9c9B%2FLm3TGGyWBN7JtsdHOSeuQ2NSjf7PmcmG60&X-Amz-Signature=2c3328c2ef08f4a9eff5b1bcbe1fc54c8d94fac9f066924be008e23b4f2aeb4d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UE4ZLRPC%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221427Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQClkfKerv40Lx76ZSgwzkS3855k0M25zap39h8k9UYPwgIhAJ8V7R0D7v4JxrBX73crnun3kwypt9tQHYmqpLMhm4EcKogECN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwLTiE0tGLhKc3hDtUq3ANP86Ouju1CKHqEkCH658P1o0zaYpscLwXG9MZYOpxx3hzgxyahLWfU5Va2arpSjoKFJ3FeJe5VptCrJmcAY8huXdq6T4vZeATGRMIHKn38EVZVi8ifCe2%2Fq7BgHyyI%2FDy7to0moM5sdLyTuKam2xVXkxLD4%2Brt0Ca0J%2FXd629gvPuMK4UY1WT%2B2OEGZlKnWBp4XGyil6PIg%2B7FQtWumHHYJj6OeOpyywjKO2VWS%2FCjpl2QlnT8lZVsukw3x8KagkJtNyIVBLWzCPnODLcyRmdYK1XKUyrkBr9t5KAzAbKnqyrchC%2BN0Mx82ArM8orMA0QpYb9sL1tKGIYLnP5pATzyvRBTyeI465FX%2BipqVBcYKarwc76OobBuK3iwYtEEPTsVFpjLRTDV5r0t0CqG8cuXcmanir39mRh5BNeAEOmqFcRg4%2FZwpFrxKjbWU2eplZDNHITH4Q19O%2Fm9iS9K1CdfADyJiYVGan5dHt%2BApGHie%2FTsgFaDabA5oTapeB27C27Ce%2FYvR8OOysPESFdERuCO6HnLkqUUj3QZBSLMq8T%2BSJcufRx2MMc5tmZTIq8kAXHLEkeWas1sVJ0D1rDDN8s3jl9dYriPzKtVmNp1jzXPfxi7OWlqOu9abZQpojD%2Fsfq8BjqkAXUtsSZ5T9FG0WqgF6OZgGeXb8V2KHpb2LZtHDDpFZj%2Fp2JKmV7uL1oIZJF3zzCvvjl3erkbJFZMBqAVxg62LmoLJvZHgMfP3eFyrFRvLqERgwkD%2FzaQCMjC%2BoVLJKd4tSQynFJPdhBY3FYDeE%2B7LYA6aUtJhenxpLXzBgLNUx1L%2FexQIRBNL9c9B%2FLm3TGGyWBN7JtsdHOSeuQ2NSjf7PmcmG60&X-Amz-Signature=9c445f64a6f3cf783c7e2f7d02991af25f0892eb46162dd90f009165e49571a6&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UE4ZLRPC%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221427Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQClkfKerv40Lx76ZSgwzkS3855k0M25zap39h8k9UYPwgIhAJ8V7R0D7v4JxrBX73crnun3kwypt9tQHYmqpLMhm4EcKogECN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwLTiE0tGLhKc3hDtUq3ANP86Ouju1CKHqEkCH658P1o0zaYpscLwXG9MZYOpxx3hzgxyahLWfU5Va2arpSjoKFJ3FeJe5VptCrJmcAY8huXdq6T4vZeATGRMIHKn38EVZVi8ifCe2%2Fq7BgHyyI%2FDy7to0moM5sdLyTuKam2xVXkxLD4%2Brt0Ca0J%2FXd629gvPuMK4UY1WT%2B2OEGZlKnWBp4XGyil6PIg%2B7FQtWumHHYJj6OeOpyywjKO2VWS%2FCjpl2QlnT8lZVsukw3x8KagkJtNyIVBLWzCPnODLcyRmdYK1XKUyrkBr9t5KAzAbKnqyrchC%2BN0Mx82ArM8orMA0QpYb9sL1tKGIYLnP5pATzyvRBTyeI465FX%2BipqVBcYKarwc76OobBuK3iwYtEEPTsVFpjLRTDV5r0t0CqG8cuXcmanir39mRh5BNeAEOmqFcRg4%2FZwpFrxKjbWU2eplZDNHITH4Q19O%2Fm9iS9K1CdfADyJiYVGan5dHt%2BApGHie%2FTsgFaDabA5oTapeB27C27Ce%2FYvR8OOysPESFdERuCO6HnLkqUUj3QZBSLMq8T%2BSJcufRx2MMc5tmZTIq8kAXHLEkeWas1sVJ0D1rDDN8s3jl9dYriPzKtVmNp1jzXPfxi7OWlqOu9abZQpojD%2Fsfq8BjqkAXUtsSZ5T9FG0WqgF6OZgGeXb8V2KHpb2LZtHDDpFZj%2Fp2JKmV7uL1oIZJF3zzCvvjl3erkbJFZMBqAVxg62LmoLJvZHgMfP3eFyrFRvLqERgwkD%2FzaQCMjC%2BoVLJKd4tSQynFJPdhBY3FYDeE%2B7LYA6aUtJhenxpLXzBgLNUx1L%2FexQIRBNL9c9B%2FLm3TGGyWBN7JtsdHOSeuQ2NSjf7PmcmG60&X-Amz-Signature=2166dfe24f6b8183c22b686619b9db102add117e7c78afe03e35d9ece3f41861&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UE4ZLRPC%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221427Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQClkfKerv40Lx76ZSgwzkS3855k0M25zap39h8k9UYPwgIhAJ8V7R0D7v4JxrBX73crnun3kwypt9tQHYmqpLMhm4EcKogECN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwLTiE0tGLhKc3hDtUq3ANP86Ouju1CKHqEkCH658P1o0zaYpscLwXG9MZYOpxx3hzgxyahLWfU5Va2arpSjoKFJ3FeJe5VptCrJmcAY8huXdq6T4vZeATGRMIHKn38EVZVi8ifCe2%2Fq7BgHyyI%2FDy7to0moM5sdLyTuKam2xVXkxLD4%2Brt0Ca0J%2FXd629gvPuMK4UY1WT%2B2OEGZlKnWBp4XGyil6PIg%2B7FQtWumHHYJj6OeOpyywjKO2VWS%2FCjpl2QlnT8lZVsukw3x8KagkJtNyIVBLWzCPnODLcyRmdYK1XKUyrkBr9t5KAzAbKnqyrchC%2BN0Mx82ArM8orMA0QpYb9sL1tKGIYLnP5pATzyvRBTyeI465FX%2BipqVBcYKarwc76OobBuK3iwYtEEPTsVFpjLRTDV5r0t0CqG8cuXcmanir39mRh5BNeAEOmqFcRg4%2FZwpFrxKjbWU2eplZDNHITH4Q19O%2Fm9iS9K1CdfADyJiYVGan5dHt%2BApGHie%2FTsgFaDabA5oTapeB27C27Ce%2FYvR8OOysPESFdERuCO6HnLkqUUj3QZBSLMq8T%2BSJcufRx2MMc5tmZTIq8kAXHLEkeWas1sVJ0D1rDDN8s3jl9dYriPzKtVmNp1jzXPfxi7OWlqOu9abZQpojD%2Fsfq8BjqkAXUtsSZ5T9FG0WqgF6OZgGeXb8V2KHpb2LZtHDDpFZj%2Fp2JKmV7uL1oIZJF3zzCvvjl3erkbJFZMBqAVxg62LmoLJvZHgMfP3eFyrFRvLqERgwkD%2FzaQCMjC%2BoVLJKd4tSQynFJPdhBY3FYDeE%2B7LYA6aUtJhenxpLXzBgLNUx1L%2FexQIRBNL9c9B%2FLm3TGGyWBN7JtsdHOSeuQ2NSjf7PmcmG60&X-Amz-Signature=93bd9dc2c1414431ee8ae110dd18e4387f730138fb0bf881b63d13ff2d540f7c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UE4ZLRPC%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221427Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQClkfKerv40Lx76ZSgwzkS3855k0M25zap39h8k9UYPwgIhAJ8V7R0D7v4JxrBX73crnun3kwypt9tQHYmqpLMhm4EcKogECN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwLTiE0tGLhKc3hDtUq3ANP86Ouju1CKHqEkCH658P1o0zaYpscLwXG9MZYOpxx3hzgxyahLWfU5Va2arpSjoKFJ3FeJe5VptCrJmcAY8huXdq6T4vZeATGRMIHKn38EVZVi8ifCe2%2Fq7BgHyyI%2FDy7to0moM5sdLyTuKam2xVXkxLD4%2Brt0Ca0J%2FXd629gvPuMK4UY1WT%2B2OEGZlKnWBp4XGyil6PIg%2B7FQtWumHHYJj6OeOpyywjKO2VWS%2FCjpl2QlnT8lZVsukw3x8KagkJtNyIVBLWzCPnODLcyRmdYK1XKUyrkBr9t5KAzAbKnqyrchC%2BN0Mx82ArM8orMA0QpYb9sL1tKGIYLnP5pATzyvRBTyeI465FX%2BipqVBcYKarwc76OobBuK3iwYtEEPTsVFpjLRTDV5r0t0CqG8cuXcmanir39mRh5BNeAEOmqFcRg4%2FZwpFrxKjbWU2eplZDNHITH4Q19O%2Fm9iS9K1CdfADyJiYVGan5dHt%2BApGHie%2FTsgFaDabA5oTapeB27C27Ce%2FYvR8OOysPESFdERuCO6HnLkqUUj3QZBSLMq8T%2BSJcufRx2MMc5tmZTIq8kAXHLEkeWas1sVJ0D1rDDN8s3jl9dYriPzKtVmNp1jzXPfxi7OWlqOu9abZQpojD%2Fsfq8BjqkAXUtsSZ5T9FG0WqgF6OZgGeXb8V2KHpb2LZtHDDpFZj%2Fp2JKmV7uL1oIZJF3zzCvvjl3erkbJFZMBqAVxg62LmoLJvZHgMfP3eFyrFRvLqERgwkD%2FzaQCMjC%2BoVLJKd4tSQynFJPdhBY3FYDeE%2B7LYA6aUtJhenxpLXzBgLNUx1L%2FexQIRBNL9c9B%2FLm3TGGyWBN7JtsdHOSeuQ2NSjf7PmcmG60&X-Amz-Signature=0962a1a8531dc276108d7322d6ab48dc7a26326b41aa753001a802c994f5ba6c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UE4ZLRPC%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221427Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQClkfKerv40Lx76ZSgwzkS3855k0M25zap39h8k9UYPwgIhAJ8V7R0D7v4JxrBX73crnun3kwypt9tQHYmqpLMhm4EcKogECN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwLTiE0tGLhKc3hDtUq3ANP86Ouju1CKHqEkCH658P1o0zaYpscLwXG9MZYOpxx3hzgxyahLWfU5Va2arpSjoKFJ3FeJe5VptCrJmcAY8huXdq6T4vZeATGRMIHKn38EVZVi8ifCe2%2Fq7BgHyyI%2FDy7to0moM5sdLyTuKam2xVXkxLD4%2Brt0Ca0J%2FXd629gvPuMK4UY1WT%2B2OEGZlKnWBp4XGyil6PIg%2B7FQtWumHHYJj6OeOpyywjKO2VWS%2FCjpl2QlnT8lZVsukw3x8KagkJtNyIVBLWzCPnODLcyRmdYK1XKUyrkBr9t5KAzAbKnqyrchC%2BN0Mx82ArM8orMA0QpYb9sL1tKGIYLnP5pATzyvRBTyeI465FX%2BipqVBcYKarwc76OobBuK3iwYtEEPTsVFpjLRTDV5r0t0CqG8cuXcmanir39mRh5BNeAEOmqFcRg4%2FZwpFrxKjbWU2eplZDNHITH4Q19O%2Fm9iS9K1CdfADyJiYVGan5dHt%2BApGHie%2FTsgFaDabA5oTapeB27C27Ce%2FYvR8OOysPESFdERuCO6HnLkqUUj3QZBSLMq8T%2BSJcufRx2MMc5tmZTIq8kAXHLEkeWas1sVJ0D1rDDN8s3jl9dYriPzKtVmNp1jzXPfxi7OWlqOu9abZQpojD%2Fsfq8BjqkAXUtsSZ5T9FG0WqgF6OZgGeXb8V2KHpb2LZtHDDpFZj%2Fp2JKmV7uL1oIZJF3zzCvvjl3erkbJFZMBqAVxg62LmoLJvZHgMfP3eFyrFRvLqERgwkD%2FzaQCMjC%2BoVLJKd4tSQynFJPdhBY3FYDeE%2B7LYA6aUtJhenxpLXzBgLNUx1L%2FexQIRBNL9c9B%2FLm3TGGyWBN7JtsdHOSeuQ2NSjf7PmcmG60&X-Amz-Signature=bbf13af4376068915f70570e9ce5fe55d8ff1733858434495c9187382917bc6f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UE4ZLRPC%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221427Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQClkfKerv40Lx76ZSgwzkS3855k0M25zap39h8k9UYPwgIhAJ8V7R0D7v4JxrBX73crnun3kwypt9tQHYmqpLMhm4EcKogECN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwLTiE0tGLhKc3hDtUq3ANP86Ouju1CKHqEkCH658P1o0zaYpscLwXG9MZYOpxx3hzgxyahLWfU5Va2arpSjoKFJ3FeJe5VptCrJmcAY8huXdq6T4vZeATGRMIHKn38EVZVi8ifCe2%2Fq7BgHyyI%2FDy7to0moM5sdLyTuKam2xVXkxLD4%2Brt0Ca0J%2FXd629gvPuMK4UY1WT%2B2OEGZlKnWBp4XGyil6PIg%2B7FQtWumHHYJj6OeOpyywjKO2VWS%2FCjpl2QlnT8lZVsukw3x8KagkJtNyIVBLWzCPnODLcyRmdYK1XKUyrkBr9t5KAzAbKnqyrchC%2BN0Mx82ArM8orMA0QpYb9sL1tKGIYLnP5pATzyvRBTyeI465FX%2BipqVBcYKarwc76OobBuK3iwYtEEPTsVFpjLRTDV5r0t0CqG8cuXcmanir39mRh5BNeAEOmqFcRg4%2FZwpFrxKjbWU2eplZDNHITH4Q19O%2Fm9iS9K1CdfADyJiYVGan5dHt%2BApGHie%2FTsgFaDabA5oTapeB27C27Ce%2FYvR8OOysPESFdERuCO6HnLkqUUj3QZBSLMq8T%2BSJcufRx2MMc5tmZTIq8kAXHLEkeWas1sVJ0D1rDDN8s3jl9dYriPzKtVmNp1jzXPfxi7OWlqOu9abZQpojD%2Fsfq8BjqkAXUtsSZ5T9FG0WqgF6OZgGeXb8V2KHpb2LZtHDDpFZj%2Fp2JKmV7uL1oIZJF3zzCvvjl3erkbJFZMBqAVxg62LmoLJvZHgMfP3eFyrFRvLqERgwkD%2FzaQCMjC%2BoVLJKd4tSQynFJPdhBY3FYDeE%2B7LYA6aUtJhenxpLXzBgLNUx1L%2FexQIRBNL9c9B%2FLm3TGGyWBN7JtsdHOSeuQ2NSjf7PmcmG60&X-Amz-Signature=238a76f9a3a368b9b1967751afad06fbc4a651b69615f93182c28a7b70a5eae4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665UKE37T6%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFYOt4O%2BGF391O9UimUo0U1e59ZDlj192P4a7wtbZ1cBAiBqXa4GiU95%2Bmuwu4v4k1%2B6uX2wj%2F415ueIwUzRQAfAbiqIBAjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUQmqKhf%2FIbzyBrmpKtwDz0YfdVT5EW9%2B1EMLunjUfv%2BEVHqFKaD4%2BKUPJICk49qiF5yx35K1CVj64%2BUpfh%2B5Z3Lhc4oAIgT8FUhuUCG6zRFPDXiwg9UWqNBM6FRd64pD2uokPOUF6e%2BVZ7nJFs%2FlqjjwbBC5afp5ObunqFF8R4wLAjo6E47xa8GmEM3veE%2FQVfxskwR%2FXQPRyks67UW44IwN4AA8d8ElpcTbuHNDWSB718Rky4lABqLeFshS4E5kHWcd4tuy4Q9HuraiYL7jtzGTW4Ce0Go%2BHqrXaSKGxcbAquj6s5ZOuuakIUPcas7B5ubIa6EBg%2FHiwa1fIE9chEaTaIPOAHmka5L94ErNkQ%2FsDBRv4b0vf1qxaBMWVzvI8vu7VJL4fhFGb6fqELKqWRrTCPqW5BQ18VmRVaWPeiKm9326tC2GUZQbbl5pNPf8pBQA0TCOcffdIFcFHU7Oqs5v3XFSTilxslW8LMmFNmJCsRIt2q4lsxP9SQCGPozC51VT7Cv7JVtj4JLTw1nYfc5nH4tnBPMiGgzjnPdnLig41hIFSIA4G9CwNBl6T%2B4%2BTDIYlTMYPCMs3VU3IgmuOvp8wE6BUHA%2F1R0VnOSKP9uDpOzTJdcor7EqxFxwM4pHq5NUZKtIGSfvDQwwkbH6vAY6pgEBv99A1RVeuMXSgSNIEdG4VO3EPw3gcEhAdNC0KWEP54iSqvq79eOJAd5JA8yiaYgl50H6jw7jMxwY%2FFD0wt%2FAcCukfznHdRjVf8I330IEcKCyKZYGYcwi6s39m2PwEWMlB1LhV8wkNtzNq8bMtuqNtP%2B%2FS5mjMxXpD7dIU2GM3hzD4mmp9QSrAAmS%2FIf2R535hLGN%2FtkmKuIBoZFrwNqyJVX%2BSOVP&X-Amz-Signature=7d75a17d96a23a7bedcda8324c40f1382981e0c8985dafada3268745a2182938&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665UKE37T6%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFYOt4O%2BGF391O9UimUo0U1e59ZDlj192P4a7wtbZ1cBAiBqXa4GiU95%2Bmuwu4v4k1%2B6uX2wj%2F415ueIwUzRQAfAbiqIBAjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUQmqKhf%2FIbzyBrmpKtwDz0YfdVT5EW9%2B1EMLunjUfv%2BEVHqFKaD4%2BKUPJICk49qiF5yx35K1CVj64%2BUpfh%2B5Z3Lhc4oAIgT8FUhuUCG6zRFPDXiwg9UWqNBM6FRd64pD2uokPOUF6e%2BVZ7nJFs%2FlqjjwbBC5afp5ObunqFF8R4wLAjo6E47xa8GmEM3veE%2FQVfxskwR%2FXQPRyks67UW44IwN4AA8d8ElpcTbuHNDWSB718Rky4lABqLeFshS4E5kHWcd4tuy4Q9HuraiYL7jtzGTW4Ce0Go%2BHqrXaSKGxcbAquj6s5ZOuuakIUPcas7B5ubIa6EBg%2FHiwa1fIE9chEaTaIPOAHmka5L94ErNkQ%2FsDBRv4b0vf1qxaBMWVzvI8vu7VJL4fhFGb6fqELKqWRrTCPqW5BQ18VmRVaWPeiKm9326tC2GUZQbbl5pNPf8pBQA0TCOcffdIFcFHU7Oqs5v3XFSTilxslW8LMmFNmJCsRIt2q4lsxP9SQCGPozC51VT7Cv7JVtj4JLTw1nYfc5nH4tnBPMiGgzjnPdnLig41hIFSIA4G9CwNBl6T%2B4%2BTDIYlTMYPCMs3VU3IgmuOvp8wE6BUHA%2F1R0VnOSKP9uDpOzTJdcor7EqxFxwM4pHq5NUZKtIGSfvDQwwkbH6vAY6pgEBv99A1RVeuMXSgSNIEdG4VO3EPw3gcEhAdNC0KWEP54iSqvq79eOJAd5JA8yiaYgl50H6jw7jMxwY%2FFD0wt%2FAcCukfznHdRjVf8I330IEcKCyKZYGYcwi6s39m2PwEWMlB1LhV8wkNtzNq8bMtuqNtP%2B%2FS5mjMxXpD7dIU2GM3hzD4mmp9QSrAAmS%2FIf2R535hLGN%2FtkmKuIBoZFrwNqyJVX%2BSOVP&X-Amz-Signature=23ea5631bbc982c574fd61357bb6c40de55f88997c9cbdfb80d880411a049f22&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
