

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642KH4XWZ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCIAleDYBfC2BOKyRF5UsexEL4PmklM4sxZYYG3KGGZQEuAiBfZllZMUZ5mE9QD5c9D7%2BQoTAbxUctKrP9H1xSWllB4iqIBAiF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjDYJ48Bjgx%2BXle4PKtwDdUvCdicL%2FvqeKZBU2Mv9TyjwAwfdEXDwOrhm3j4xdwlgzQad514qwNsy5emABwDM06JNmiRbKtPFrVD1ri0cGO3bnpyKv73jSMXKhkQZlVCgiMfzsIjlVDiB8mq6DhH3PufSolnbXNNGXEQbdNeR%2FDnK%2FWTnuqVuh6YHpFz%2Fag1Ntprkz%2BHIt7bw9XcWtu%2FFWSG%2FsfTlrSdXz%2FZw00Pf445LJmZcdMFhxzO%2FhR2XtGBc2HbAZ2R6KgM3fNUvmHe72LkVrUP%2F1YjuqCrFHXPegnKBVtgV5wl0ZQerNCh%2FK3OTDKOJpBwg%2BH15IuUc4hMoAx5clseq%2BgtrLd9H9Fkn1KCo5Vlez7hHC5C2gf%2FQs9xjOc7zQGKrI5DSISTpkpqCnLbjFmBmhShw0ss0iDeKrMiXOHzjyD8IFCtxdcew05MxMHcDrX7Uwe7yFZ6RhDBxV9JTPLj5sX56KjkZ64NIkyr1hNy124sFoe8kaLtEp4bHIvzSesWQjKQBdTof5x8kRGrQeM%2B%2BkellbyamvjPD%2FQK0tXjEhP%2FUcDA%2F%2FCkE7E%2FBawtsIpB0LlROdex6Cw1ddPCfcC1ClhKqHXuiHB%2FXVpmR1a%2F7pmqn5leo2C4RhoZVrZJFDrz%2FhWKLlPcwi7ObvQY6pgEFi7%2BgzNFfHGjGrDbZn11rMSKAcKPBZka9kzQXCboiLyt0TGyNMFZ4ZAROTXxr0I1w1%2B1LCW1FkT0%2Fgr4rBxaz9uu%2F8LIwdllE2mzUEYWXw9IoflOUrFKr4LNTUQPfEtODtyRDWlOJUbZ1QJNot1dFvw3nqhLHlB%2Fvia1MVSMAiMLZUdFw4srcX6XhmlIAhettHEgaw0TJ2q%2BMO4zYt90QgWhIxJuk&X-Amz-Signature=d266d79bbd2503665cda1bddb9b6d5789499493f28643e3b95e27c6d8180a2a3&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642KH4XWZ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCIAleDYBfC2BOKyRF5UsexEL4PmklM4sxZYYG3KGGZQEuAiBfZllZMUZ5mE9QD5c9D7%2BQoTAbxUctKrP9H1xSWllB4iqIBAiF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjDYJ48Bjgx%2BXle4PKtwDdUvCdicL%2FvqeKZBU2Mv9TyjwAwfdEXDwOrhm3j4xdwlgzQad514qwNsy5emABwDM06JNmiRbKtPFrVD1ri0cGO3bnpyKv73jSMXKhkQZlVCgiMfzsIjlVDiB8mq6DhH3PufSolnbXNNGXEQbdNeR%2FDnK%2FWTnuqVuh6YHpFz%2Fag1Ntprkz%2BHIt7bw9XcWtu%2FFWSG%2FsfTlrSdXz%2FZw00Pf445LJmZcdMFhxzO%2FhR2XtGBc2HbAZ2R6KgM3fNUvmHe72LkVrUP%2F1YjuqCrFHXPegnKBVtgV5wl0ZQerNCh%2FK3OTDKOJpBwg%2BH15IuUc4hMoAx5clseq%2BgtrLd9H9Fkn1KCo5Vlez7hHC5C2gf%2FQs9xjOc7zQGKrI5DSISTpkpqCnLbjFmBmhShw0ss0iDeKrMiXOHzjyD8IFCtxdcew05MxMHcDrX7Uwe7yFZ6RhDBxV9JTPLj5sX56KjkZ64NIkyr1hNy124sFoe8kaLtEp4bHIvzSesWQjKQBdTof5x8kRGrQeM%2B%2BkellbyamvjPD%2FQK0tXjEhP%2FUcDA%2F%2FCkE7E%2FBawtsIpB0LlROdex6Cw1ddPCfcC1ClhKqHXuiHB%2FXVpmR1a%2F7pmqn5leo2C4RhoZVrZJFDrz%2FhWKLlPcwi7ObvQY6pgEFi7%2BgzNFfHGjGrDbZn11rMSKAcKPBZka9kzQXCboiLyt0TGyNMFZ4ZAROTXxr0I1w1%2B1LCW1FkT0%2Fgr4rBxaz9uu%2F8LIwdllE2mzUEYWXw9IoflOUrFKr4LNTUQPfEtODtyRDWlOJUbZ1QJNot1dFvw3nqhLHlB%2Fvia1MVSMAiMLZUdFw4srcX6XhmlIAhettHEgaw0TJ2q%2BMO4zYt90QgWhIxJuk&X-Amz-Signature=451096e25dde0e15c9a3931753dcb5ed805cf52b18651574f42925807e00d471&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642KH4XWZ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCIAleDYBfC2BOKyRF5UsexEL4PmklM4sxZYYG3KGGZQEuAiBfZllZMUZ5mE9QD5c9D7%2BQoTAbxUctKrP9H1xSWllB4iqIBAiF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjDYJ48Bjgx%2BXle4PKtwDdUvCdicL%2FvqeKZBU2Mv9TyjwAwfdEXDwOrhm3j4xdwlgzQad514qwNsy5emABwDM06JNmiRbKtPFrVD1ri0cGO3bnpyKv73jSMXKhkQZlVCgiMfzsIjlVDiB8mq6DhH3PufSolnbXNNGXEQbdNeR%2FDnK%2FWTnuqVuh6YHpFz%2Fag1Ntprkz%2BHIt7bw9XcWtu%2FFWSG%2FsfTlrSdXz%2FZw00Pf445LJmZcdMFhxzO%2FhR2XtGBc2HbAZ2R6KgM3fNUvmHe72LkVrUP%2F1YjuqCrFHXPegnKBVtgV5wl0ZQerNCh%2FK3OTDKOJpBwg%2BH15IuUc4hMoAx5clseq%2BgtrLd9H9Fkn1KCo5Vlez7hHC5C2gf%2FQs9xjOc7zQGKrI5DSISTpkpqCnLbjFmBmhShw0ss0iDeKrMiXOHzjyD8IFCtxdcew05MxMHcDrX7Uwe7yFZ6RhDBxV9JTPLj5sX56KjkZ64NIkyr1hNy124sFoe8kaLtEp4bHIvzSesWQjKQBdTof5x8kRGrQeM%2B%2BkellbyamvjPD%2FQK0tXjEhP%2FUcDA%2F%2FCkE7E%2FBawtsIpB0LlROdex6Cw1ddPCfcC1ClhKqHXuiHB%2FXVpmR1a%2F7pmqn5leo2C4RhoZVrZJFDrz%2FhWKLlPcwi7ObvQY6pgEFi7%2BgzNFfHGjGrDbZn11rMSKAcKPBZka9kzQXCboiLyt0TGyNMFZ4ZAROTXxr0I1w1%2B1LCW1FkT0%2Fgr4rBxaz9uu%2F8LIwdllE2mzUEYWXw9IoflOUrFKr4LNTUQPfEtODtyRDWlOJUbZ1QJNot1dFvw3nqhLHlB%2Fvia1MVSMAiMLZUdFw4srcX6XhmlIAhettHEgaw0TJ2q%2BMO4zYt90QgWhIxJuk&X-Amz-Signature=021a4a931b714655a8442281b509cfb53cee259cfdb33bcd308e57c8472f0b7a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642KH4XWZ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCIAleDYBfC2BOKyRF5UsexEL4PmklM4sxZYYG3KGGZQEuAiBfZllZMUZ5mE9QD5c9D7%2BQoTAbxUctKrP9H1xSWllB4iqIBAiF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjDYJ48Bjgx%2BXle4PKtwDdUvCdicL%2FvqeKZBU2Mv9TyjwAwfdEXDwOrhm3j4xdwlgzQad514qwNsy5emABwDM06JNmiRbKtPFrVD1ri0cGO3bnpyKv73jSMXKhkQZlVCgiMfzsIjlVDiB8mq6DhH3PufSolnbXNNGXEQbdNeR%2FDnK%2FWTnuqVuh6YHpFz%2Fag1Ntprkz%2BHIt7bw9XcWtu%2FFWSG%2FsfTlrSdXz%2FZw00Pf445LJmZcdMFhxzO%2FhR2XtGBc2HbAZ2R6KgM3fNUvmHe72LkVrUP%2F1YjuqCrFHXPegnKBVtgV5wl0ZQerNCh%2FK3OTDKOJpBwg%2BH15IuUc4hMoAx5clseq%2BgtrLd9H9Fkn1KCo5Vlez7hHC5C2gf%2FQs9xjOc7zQGKrI5DSISTpkpqCnLbjFmBmhShw0ss0iDeKrMiXOHzjyD8IFCtxdcew05MxMHcDrX7Uwe7yFZ6RhDBxV9JTPLj5sX56KjkZ64NIkyr1hNy124sFoe8kaLtEp4bHIvzSesWQjKQBdTof5x8kRGrQeM%2B%2BkellbyamvjPD%2FQK0tXjEhP%2FUcDA%2F%2FCkE7E%2FBawtsIpB0LlROdex6Cw1ddPCfcC1ClhKqHXuiHB%2FXVpmR1a%2F7pmqn5leo2C4RhoZVrZJFDrz%2FhWKLlPcwi7ObvQY6pgEFi7%2BgzNFfHGjGrDbZn11rMSKAcKPBZka9kzQXCboiLyt0TGyNMFZ4ZAROTXxr0I1w1%2B1LCW1FkT0%2Fgr4rBxaz9uu%2F8LIwdllE2mzUEYWXw9IoflOUrFKr4LNTUQPfEtODtyRDWlOJUbZ1QJNot1dFvw3nqhLHlB%2Fvia1MVSMAiMLZUdFw4srcX6XhmlIAhettHEgaw0TJ2q%2BMO4zYt90QgWhIxJuk&X-Amz-Signature=53689199cd0c4d87713fedb78393f8518162f24c8006a47c8a9c23e1869bd278&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642KH4XWZ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCIAleDYBfC2BOKyRF5UsexEL4PmklM4sxZYYG3KGGZQEuAiBfZllZMUZ5mE9QD5c9D7%2BQoTAbxUctKrP9H1xSWllB4iqIBAiF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjDYJ48Bjgx%2BXle4PKtwDdUvCdicL%2FvqeKZBU2Mv9TyjwAwfdEXDwOrhm3j4xdwlgzQad514qwNsy5emABwDM06JNmiRbKtPFrVD1ri0cGO3bnpyKv73jSMXKhkQZlVCgiMfzsIjlVDiB8mq6DhH3PufSolnbXNNGXEQbdNeR%2FDnK%2FWTnuqVuh6YHpFz%2Fag1Ntprkz%2BHIt7bw9XcWtu%2FFWSG%2FsfTlrSdXz%2FZw00Pf445LJmZcdMFhxzO%2FhR2XtGBc2HbAZ2R6KgM3fNUvmHe72LkVrUP%2F1YjuqCrFHXPegnKBVtgV5wl0ZQerNCh%2FK3OTDKOJpBwg%2BH15IuUc4hMoAx5clseq%2BgtrLd9H9Fkn1KCo5Vlez7hHC5C2gf%2FQs9xjOc7zQGKrI5DSISTpkpqCnLbjFmBmhShw0ss0iDeKrMiXOHzjyD8IFCtxdcew05MxMHcDrX7Uwe7yFZ6RhDBxV9JTPLj5sX56KjkZ64NIkyr1hNy124sFoe8kaLtEp4bHIvzSesWQjKQBdTof5x8kRGrQeM%2B%2BkellbyamvjPD%2FQK0tXjEhP%2FUcDA%2F%2FCkE7E%2FBawtsIpB0LlROdex6Cw1ddPCfcC1ClhKqHXuiHB%2FXVpmR1a%2F7pmqn5leo2C4RhoZVrZJFDrz%2FhWKLlPcwi7ObvQY6pgEFi7%2BgzNFfHGjGrDbZn11rMSKAcKPBZka9kzQXCboiLyt0TGyNMFZ4ZAROTXxr0I1w1%2B1LCW1FkT0%2Fgr4rBxaz9uu%2F8LIwdllE2mzUEYWXw9IoflOUrFKr4LNTUQPfEtODtyRDWlOJUbZ1QJNot1dFvw3nqhLHlB%2Fvia1MVSMAiMLZUdFw4srcX6XhmlIAhettHEgaw0TJ2q%2BMO4zYt90QgWhIxJuk&X-Amz-Signature=ad40dca72154255b607ce7f15f87f6c4a275ee73d6f2c47ad420f2519a40f9be&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642KH4XWZ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCIAleDYBfC2BOKyRF5UsexEL4PmklM4sxZYYG3KGGZQEuAiBfZllZMUZ5mE9QD5c9D7%2BQoTAbxUctKrP9H1xSWllB4iqIBAiF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjDYJ48Bjgx%2BXle4PKtwDdUvCdicL%2FvqeKZBU2Mv9TyjwAwfdEXDwOrhm3j4xdwlgzQad514qwNsy5emABwDM06JNmiRbKtPFrVD1ri0cGO3bnpyKv73jSMXKhkQZlVCgiMfzsIjlVDiB8mq6DhH3PufSolnbXNNGXEQbdNeR%2FDnK%2FWTnuqVuh6YHpFz%2Fag1Ntprkz%2BHIt7bw9XcWtu%2FFWSG%2FsfTlrSdXz%2FZw00Pf445LJmZcdMFhxzO%2FhR2XtGBc2HbAZ2R6KgM3fNUvmHe72LkVrUP%2F1YjuqCrFHXPegnKBVtgV5wl0ZQerNCh%2FK3OTDKOJpBwg%2BH15IuUc4hMoAx5clseq%2BgtrLd9H9Fkn1KCo5Vlez7hHC5C2gf%2FQs9xjOc7zQGKrI5DSISTpkpqCnLbjFmBmhShw0ss0iDeKrMiXOHzjyD8IFCtxdcew05MxMHcDrX7Uwe7yFZ6RhDBxV9JTPLj5sX56KjkZ64NIkyr1hNy124sFoe8kaLtEp4bHIvzSesWQjKQBdTof5x8kRGrQeM%2B%2BkellbyamvjPD%2FQK0tXjEhP%2FUcDA%2F%2FCkE7E%2FBawtsIpB0LlROdex6Cw1ddPCfcC1ClhKqHXuiHB%2FXVpmR1a%2F7pmqn5leo2C4RhoZVrZJFDrz%2FhWKLlPcwi7ObvQY6pgEFi7%2BgzNFfHGjGrDbZn11rMSKAcKPBZka9kzQXCboiLyt0TGyNMFZ4ZAROTXxr0I1w1%2B1LCW1FkT0%2Fgr4rBxaz9uu%2F8LIwdllE2mzUEYWXw9IoflOUrFKr4LNTUQPfEtODtyRDWlOJUbZ1QJNot1dFvw3nqhLHlB%2Fvia1MVSMAiMLZUdFw4srcX6XhmlIAhettHEgaw0TJ2q%2BMO4zYt90QgWhIxJuk&X-Amz-Signature=9f2e3cd26af0c734d727c7e3ad3daa05e1829784570227f3c8b4126571a2414b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642KH4XWZ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCIAleDYBfC2BOKyRF5UsexEL4PmklM4sxZYYG3KGGZQEuAiBfZllZMUZ5mE9QD5c9D7%2BQoTAbxUctKrP9H1xSWllB4iqIBAiF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjDYJ48Bjgx%2BXle4PKtwDdUvCdicL%2FvqeKZBU2Mv9TyjwAwfdEXDwOrhm3j4xdwlgzQad514qwNsy5emABwDM06JNmiRbKtPFrVD1ri0cGO3bnpyKv73jSMXKhkQZlVCgiMfzsIjlVDiB8mq6DhH3PufSolnbXNNGXEQbdNeR%2FDnK%2FWTnuqVuh6YHpFz%2Fag1Ntprkz%2BHIt7bw9XcWtu%2FFWSG%2FsfTlrSdXz%2FZw00Pf445LJmZcdMFhxzO%2FhR2XtGBc2HbAZ2R6KgM3fNUvmHe72LkVrUP%2F1YjuqCrFHXPegnKBVtgV5wl0ZQerNCh%2FK3OTDKOJpBwg%2BH15IuUc4hMoAx5clseq%2BgtrLd9H9Fkn1KCo5Vlez7hHC5C2gf%2FQs9xjOc7zQGKrI5DSISTpkpqCnLbjFmBmhShw0ss0iDeKrMiXOHzjyD8IFCtxdcew05MxMHcDrX7Uwe7yFZ6RhDBxV9JTPLj5sX56KjkZ64NIkyr1hNy124sFoe8kaLtEp4bHIvzSesWQjKQBdTof5x8kRGrQeM%2B%2BkellbyamvjPD%2FQK0tXjEhP%2FUcDA%2F%2FCkE7E%2FBawtsIpB0LlROdex6Cw1ddPCfcC1ClhKqHXuiHB%2FXVpmR1a%2F7pmqn5leo2C4RhoZVrZJFDrz%2FhWKLlPcwi7ObvQY6pgEFi7%2BgzNFfHGjGrDbZn11rMSKAcKPBZka9kzQXCboiLyt0TGyNMFZ4ZAROTXxr0I1w1%2B1LCW1FkT0%2Fgr4rBxaz9uu%2F8LIwdllE2mzUEYWXw9IoflOUrFKr4LNTUQPfEtODtyRDWlOJUbZ1QJNot1dFvw3nqhLHlB%2Fvia1MVSMAiMLZUdFw4srcX6XhmlIAhettHEgaw0TJ2q%2BMO4zYt90QgWhIxJuk&X-Amz-Signature=27876002964374717d996d8ec935588503667e74f6b365e041975567ee97410b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642KH4XWZ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCIAleDYBfC2BOKyRF5UsexEL4PmklM4sxZYYG3KGGZQEuAiBfZllZMUZ5mE9QD5c9D7%2BQoTAbxUctKrP9H1xSWllB4iqIBAiF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjDYJ48Bjgx%2BXle4PKtwDdUvCdicL%2FvqeKZBU2Mv9TyjwAwfdEXDwOrhm3j4xdwlgzQad514qwNsy5emABwDM06JNmiRbKtPFrVD1ri0cGO3bnpyKv73jSMXKhkQZlVCgiMfzsIjlVDiB8mq6DhH3PufSolnbXNNGXEQbdNeR%2FDnK%2FWTnuqVuh6YHpFz%2Fag1Ntprkz%2BHIt7bw9XcWtu%2FFWSG%2FsfTlrSdXz%2FZw00Pf445LJmZcdMFhxzO%2FhR2XtGBc2HbAZ2R6KgM3fNUvmHe72LkVrUP%2F1YjuqCrFHXPegnKBVtgV5wl0ZQerNCh%2FK3OTDKOJpBwg%2BH15IuUc4hMoAx5clseq%2BgtrLd9H9Fkn1KCo5Vlez7hHC5C2gf%2FQs9xjOc7zQGKrI5DSISTpkpqCnLbjFmBmhShw0ss0iDeKrMiXOHzjyD8IFCtxdcew05MxMHcDrX7Uwe7yFZ6RhDBxV9JTPLj5sX56KjkZ64NIkyr1hNy124sFoe8kaLtEp4bHIvzSesWQjKQBdTof5x8kRGrQeM%2B%2BkellbyamvjPD%2FQK0tXjEhP%2FUcDA%2F%2FCkE7E%2FBawtsIpB0LlROdex6Cw1ddPCfcC1ClhKqHXuiHB%2FXVpmR1a%2F7pmqn5leo2C4RhoZVrZJFDrz%2FhWKLlPcwi7ObvQY6pgEFi7%2BgzNFfHGjGrDbZn11rMSKAcKPBZka9kzQXCboiLyt0TGyNMFZ4ZAROTXxr0I1w1%2B1LCW1FkT0%2Fgr4rBxaz9uu%2F8LIwdllE2mzUEYWXw9IoflOUrFKr4LNTUQPfEtODtyRDWlOJUbZ1QJNot1dFvw3nqhLHlB%2Fvia1MVSMAiMLZUdFw4srcX6XhmlIAhettHEgaw0TJ2q%2BMO4zYt90QgWhIxJuk&X-Amz-Signature=59c3aade4018045d641e2074fccef922a55844a1b642232a7dfb99ef3c8e0e2c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642KH4XWZ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCIAleDYBfC2BOKyRF5UsexEL4PmklM4sxZYYG3KGGZQEuAiBfZllZMUZ5mE9QD5c9D7%2BQoTAbxUctKrP9H1xSWllB4iqIBAiF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjDYJ48Bjgx%2BXle4PKtwDdUvCdicL%2FvqeKZBU2Mv9TyjwAwfdEXDwOrhm3j4xdwlgzQad514qwNsy5emABwDM06JNmiRbKtPFrVD1ri0cGO3bnpyKv73jSMXKhkQZlVCgiMfzsIjlVDiB8mq6DhH3PufSolnbXNNGXEQbdNeR%2FDnK%2FWTnuqVuh6YHpFz%2Fag1Ntprkz%2BHIt7bw9XcWtu%2FFWSG%2FsfTlrSdXz%2FZw00Pf445LJmZcdMFhxzO%2FhR2XtGBc2HbAZ2R6KgM3fNUvmHe72LkVrUP%2F1YjuqCrFHXPegnKBVtgV5wl0ZQerNCh%2FK3OTDKOJpBwg%2BH15IuUc4hMoAx5clseq%2BgtrLd9H9Fkn1KCo5Vlez7hHC5C2gf%2FQs9xjOc7zQGKrI5DSISTpkpqCnLbjFmBmhShw0ss0iDeKrMiXOHzjyD8IFCtxdcew05MxMHcDrX7Uwe7yFZ6RhDBxV9JTPLj5sX56KjkZ64NIkyr1hNy124sFoe8kaLtEp4bHIvzSesWQjKQBdTof5x8kRGrQeM%2B%2BkellbyamvjPD%2FQK0tXjEhP%2FUcDA%2F%2FCkE7E%2FBawtsIpB0LlROdex6Cw1ddPCfcC1ClhKqHXuiHB%2FXVpmR1a%2F7pmqn5leo2C4RhoZVrZJFDrz%2FhWKLlPcwi7ObvQY6pgEFi7%2BgzNFfHGjGrDbZn11rMSKAcKPBZka9kzQXCboiLyt0TGyNMFZ4ZAROTXxr0I1w1%2B1LCW1FkT0%2Fgr4rBxaz9uu%2F8LIwdllE2mzUEYWXw9IoflOUrFKr4LNTUQPfEtODtyRDWlOJUbZ1QJNot1dFvw3nqhLHlB%2Fvia1MVSMAiMLZUdFw4srcX6XhmlIAhettHEgaw0TJ2q%2BMO4zYt90QgWhIxJuk&X-Amz-Signature=e03b9ae689be259ef66d1624067fa37e817a9fa6ba5b396ca221c9872e34a4b1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662AIINOWI%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIQChAl2ADXiMApJ3eSPbSNoOk9PD7qVUhzIuJV0szsMg2QIgTXnClZdRpIyXBs8UoYBiKF3v6VTi61M5sXcUrQMLOF8qiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHpGtl%2F%2BvXPX0CWUJircA0bKB2%2BpN%2B9Zh5bww9j2HRq%2BpKGqfRe9KEPzthuJBGjZDBegEolFy6vlCxVk8%2FnUCwGdxzG%2Fcgz5jPHNAxcP2L11a8vdZ1yETON4re2q%2FcpfHtSEFV2Usl3L8KNXBrXWP8iBQqRS%2Fgh1v37NtFwSz40SgxDbbr6Hph71wAsaCklGQ7V67kHb3obQU596FZFSP%2FJVzkTbQJwxIt18sOMx9L6cIf6DP4FJSWEYBNQN9fuUnCXtbKDTUvFmRTv2rV5N7I3AcelffkeXjgkeHT9y3CissYDN7%2FG3AEMee6zIZurUx%2FWFPgOLYviep4M9CxxY7R3Whs%2Ba4FGvJErns7GtBLNgvHv4GxGgWSN42ye9vI78Qia9%2B927ctdJCuvm%2Bibwfzb%2FL2itb%2B8QvnwNTNRtfL3zvt02i%2FLM4T5w5LtKurnGKseNyh0h6vaMSOF0KZBj%2BElcQVkL%2B2rZPlaTMRYNupx678PItX3fnS%2BrL8qArQBCfHUhWGeSMkvlKxMkMP4Y4SR%2FpDxQ50XwwNDkqgC6tIDlBrf0Kx5a%2FMqos4EHJQNoVL1Ec2Ql%2BeOmziJDdAEgpc9lyuzBSA9HHtnCQHUtlwpkQgXyNv3dH2qyRuRggHSpnCqsqRAOPirUHLAOMN2ym70GOqUBXlsglPHpfgFOoKMwJ4CMKP%2F5BRWMiE9zOGpGsLydxOgtd5M2oNBesRUeIPvlFj4KkzwPZiIa9n%2Fv2QVunccNWGEScWZx%2BJ14DIidJ1V8IUfAx%2BYqLh5hT1NPTJ4fi0cSoqNAdtnbHvSDDkqIqwW9QzbaYlsUigg4IzSJ2PfHn4PTxv9JOgQ2QLO77v7df4qPH94Oyp%2BlYSVXu9gtnURS%2F96%2BiO6l&X-Amz-Signature=309a10c6ef9da907cb4653f5e2fc7fbd38fc71ab1a7b54486e9d61af12e354fc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662AIINOWI%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIQChAl2ADXiMApJ3eSPbSNoOk9PD7qVUhzIuJV0szsMg2QIgTXnClZdRpIyXBs8UoYBiKF3v6VTi61M5sXcUrQMLOF8qiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHpGtl%2F%2BvXPX0CWUJircA0bKB2%2BpN%2B9Zh5bww9j2HRq%2BpKGqfRe9KEPzthuJBGjZDBegEolFy6vlCxVk8%2FnUCwGdxzG%2Fcgz5jPHNAxcP2L11a8vdZ1yETON4re2q%2FcpfHtSEFV2Usl3L8KNXBrXWP8iBQqRS%2Fgh1v37NtFwSz40SgxDbbr6Hph71wAsaCklGQ7V67kHb3obQU596FZFSP%2FJVzkTbQJwxIt18sOMx9L6cIf6DP4FJSWEYBNQN9fuUnCXtbKDTUvFmRTv2rV5N7I3AcelffkeXjgkeHT9y3CissYDN7%2FG3AEMee6zIZurUx%2FWFPgOLYviep4M9CxxY7R3Whs%2Ba4FGvJErns7GtBLNgvHv4GxGgWSN42ye9vI78Qia9%2B927ctdJCuvm%2Bibwfzb%2FL2itb%2B8QvnwNTNRtfL3zvt02i%2FLM4T5w5LtKurnGKseNyh0h6vaMSOF0KZBj%2BElcQVkL%2B2rZPlaTMRYNupx678PItX3fnS%2BrL8qArQBCfHUhWGeSMkvlKxMkMP4Y4SR%2FpDxQ50XwwNDkqgC6tIDlBrf0Kx5a%2FMqos4EHJQNoVL1Ec2Ql%2BeOmziJDdAEgpc9lyuzBSA9HHtnCQHUtlwpkQgXyNv3dH2qyRuRggHSpnCqsqRAOPirUHLAOMN2ym70GOqUBXlsglPHpfgFOoKMwJ4CMKP%2F5BRWMiE9zOGpGsLydxOgtd5M2oNBesRUeIPvlFj4KkzwPZiIa9n%2Fv2QVunccNWGEScWZx%2BJ14DIidJ1V8IUfAx%2BYqLh5hT1NPTJ4fi0cSoqNAdtnbHvSDDkqIqwW9QzbaYlsUigg4IzSJ2PfHn4PTxv9JOgQ2QLO77v7df4qPH94Oyp%2BlYSVXu9gtnURS%2F96%2BiO6l&X-Amz-Signature=e4c976f707772f03fdd3608da41f7c013fb4612bd14133627d551d680cee4cc0&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
