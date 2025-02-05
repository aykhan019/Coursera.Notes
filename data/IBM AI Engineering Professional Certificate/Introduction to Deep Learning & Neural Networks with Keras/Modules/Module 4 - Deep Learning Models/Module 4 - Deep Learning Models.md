

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGYZQH4Y%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJGMEQCIE9PSglxkfR%2F5Mlygo%2FyWV4ItnVkUdUvzitwSlyHD%2FHuAiAKEa57cQUMhljeKBi9xQNXvVojM6tyRdjagNEhm16t3yr%2FAwhHEAAaDDYzNzQyMzE4MzgwNSIMW8P8%2FBUK%2Bsd4ppvkKtwDKaTUHVH6Vum7rJmPXsXyeUUO5Bi4SINetWhb%2FVNIWNf0OYg4%2F%2Fnf7%2Bl4m1%2BTQLEJgRln9yff6m%2Fdev8O9GnsRQlMbtuxckVtgE6MSgbWlGo1G%2FIKXQrmnLEa3ucYjA18r5tjgMCjJnjmHm7rW6ZGxbdtWY%2Bsl9kSwNGdf1jINSsc0b7x9Muo3ddBr1PzzJAKSVJqt%2BUnjyg1JBo97SW5wz4JRRSqlb1DhKf%2BtPFgVaHTw7537NYFhVv5D2l5x8iADR5pI%2B%2F2Tlj1REBQeWhVPIrC4fWuiUPVzpjBb0Js3gGaj9vmVCnOkE8lIulW2NVz8O%2BrkZyN5dpNoYZH%2BX8lN1rI1RLPjwwNNFlzdi5ebgQ0sN4SzPPrPlb%2BHnPggHwr%2BKyoekM9iUul1SXvqgiVQgDQ0ozy8OJXR7Ei%2FDjNS7%2BC6GAK4C0r1D9M%2FZ9mnut7EyVl03U45CUirwdI%2FICkKh%2F3cqm00EhaUz5tppS5rHlQ%2BCct04JZIp1nik2N2%2Bl8qIlF2AlTg5zc7JYVfSK9jR7kWVGYdMS1aZjt8TZRcgVAvTzA6uxPrPtjLx1WsR1nyCdnlVmfOAJR9RjBIeMzBNonxudvq3R0SPxTDo9OMJZw9c6%2BtrUAglB4Om8wxeONvQY6pgGgnadFG9WdNc1prG2gj2TfsFPO1PIxqw86tRNIeV9vLLRU%2F4dj6v%2BkRn3CsQjY%2Fgw6qY9FPgli6MPegmKm03XoodkgeqwWjRD5BPUK%2BvCtFgqF9en%2F3JCvWTHPU7dYPgS63BvbEL7pRKVj2fSJPUUpdmUCGAqHCMs1CEPKN%2FMUKdigFzPwjkfdwh6VUo9iSmIF9c%2FaacFYW3gkUh9kLD1M%2BD4UXmcf&X-Amz-Signature=458fc3b4aaf70d0f2400c776e72704abc87eb80fe0a7684cbc5d2b04352ce8cc&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGYZQH4Y%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJGMEQCIE9PSglxkfR%2F5Mlygo%2FyWV4ItnVkUdUvzitwSlyHD%2FHuAiAKEa57cQUMhljeKBi9xQNXvVojM6tyRdjagNEhm16t3yr%2FAwhHEAAaDDYzNzQyMzE4MzgwNSIMW8P8%2FBUK%2Bsd4ppvkKtwDKaTUHVH6Vum7rJmPXsXyeUUO5Bi4SINetWhb%2FVNIWNf0OYg4%2F%2Fnf7%2Bl4m1%2BTQLEJgRln9yff6m%2Fdev8O9GnsRQlMbtuxckVtgE6MSgbWlGo1G%2FIKXQrmnLEa3ucYjA18r5tjgMCjJnjmHm7rW6ZGxbdtWY%2Bsl9kSwNGdf1jINSsc0b7x9Muo3ddBr1PzzJAKSVJqt%2BUnjyg1JBo97SW5wz4JRRSqlb1DhKf%2BtPFgVaHTw7537NYFhVv5D2l5x8iADR5pI%2B%2F2Tlj1REBQeWhVPIrC4fWuiUPVzpjBb0Js3gGaj9vmVCnOkE8lIulW2NVz8O%2BrkZyN5dpNoYZH%2BX8lN1rI1RLPjwwNNFlzdi5ebgQ0sN4SzPPrPlb%2BHnPggHwr%2BKyoekM9iUul1SXvqgiVQgDQ0ozy8OJXR7Ei%2FDjNS7%2BC6GAK4C0r1D9M%2FZ9mnut7EyVl03U45CUirwdI%2FICkKh%2F3cqm00EhaUz5tppS5rHlQ%2BCct04JZIp1nik2N2%2Bl8qIlF2AlTg5zc7JYVfSK9jR7kWVGYdMS1aZjt8TZRcgVAvTzA6uxPrPtjLx1WsR1nyCdnlVmfOAJR9RjBIeMzBNonxudvq3R0SPxTDo9OMJZw9c6%2BtrUAglB4Om8wxeONvQY6pgGgnadFG9WdNc1prG2gj2TfsFPO1PIxqw86tRNIeV9vLLRU%2F4dj6v%2BkRn3CsQjY%2Fgw6qY9FPgli6MPegmKm03XoodkgeqwWjRD5BPUK%2BvCtFgqF9en%2F3JCvWTHPU7dYPgS63BvbEL7pRKVj2fSJPUUpdmUCGAqHCMs1CEPKN%2FMUKdigFzPwjkfdwh6VUo9iSmIF9c%2FaacFYW3gkUh9kLD1M%2BD4UXmcf&X-Amz-Signature=78c45b721f6d0351e815f58adf5116ecd7dfa40979c86a357ed24732280c1fc1&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGYZQH4Y%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJGMEQCIE9PSglxkfR%2F5Mlygo%2FyWV4ItnVkUdUvzitwSlyHD%2FHuAiAKEa57cQUMhljeKBi9xQNXvVojM6tyRdjagNEhm16t3yr%2FAwhHEAAaDDYzNzQyMzE4MzgwNSIMW8P8%2FBUK%2Bsd4ppvkKtwDKaTUHVH6Vum7rJmPXsXyeUUO5Bi4SINetWhb%2FVNIWNf0OYg4%2F%2Fnf7%2Bl4m1%2BTQLEJgRln9yff6m%2Fdev8O9GnsRQlMbtuxckVtgE6MSgbWlGo1G%2FIKXQrmnLEa3ucYjA18r5tjgMCjJnjmHm7rW6ZGxbdtWY%2Bsl9kSwNGdf1jINSsc0b7x9Muo3ddBr1PzzJAKSVJqt%2BUnjyg1JBo97SW5wz4JRRSqlb1DhKf%2BtPFgVaHTw7537NYFhVv5D2l5x8iADR5pI%2B%2F2Tlj1REBQeWhVPIrC4fWuiUPVzpjBb0Js3gGaj9vmVCnOkE8lIulW2NVz8O%2BrkZyN5dpNoYZH%2BX8lN1rI1RLPjwwNNFlzdi5ebgQ0sN4SzPPrPlb%2BHnPggHwr%2BKyoekM9iUul1SXvqgiVQgDQ0ozy8OJXR7Ei%2FDjNS7%2BC6GAK4C0r1D9M%2FZ9mnut7EyVl03U45CUirwdI%2FICkKh%2F3cqm00EhaUz5tppS5rHlQ%2BCct04JZIp1nik2N2%2Bl8qIlF2AlTg5zc7JYVfSK9jR7kWVGYdMS1aZjt8TZRcgVAvTzA6uxPrPtjLx1WsR1nyCdnlVmfOAJR9RjBIeMzBNonxudvq3R0SPxTDo9OMJZw9c6%2BtrUAglB4Om8wxeONvQY6pgGgnadFG9WdNc1prG2gj2TfsFPO1PIxqw86tRNIeV9vLLRU%2F4dj6v%2BkRn3CsQjY%2Fgw6qY9FPgli6MPegmKm03XoodkgeqwWjRD5BPUK%2BvCtFgqF9en%2F3JCvWTHPU7dYPgS63BvbEL7pRKVj2fSJPUUpdmUCGAqHCMs1CEPKN%2FMUKdigFzPwjkfdwh6VUo9iSmIF9c%2FaacFYW3gkUh9kLD1M%2BD4UXmcf&X-Amz-Signature=edc3666e9dda311bd75dbee3e66d122e3e70d995ff4687129f7624f46d1a4f90&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGYZQH4Y%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJGMEQCIE9PSglxkfR%2F5Mlygo%2FyWV4ItnVkUdUvzitwSlyHD%2FHuAiAKEa57cQUMhljeKBi9xQNXvVojM6tyRdjagNEhm16t3yr%2FAwhHEAAaDDYzNzQyMzE4MzgwNSIMW8P8%2FBUK%2Bsd4ppvkKtwDKaTUHVH6Vum7rJmPXsXyeUUO5Bi4SINetWhb%2FVNIWNf0OYg4%2F%2Fnf7%2Bl4m1%2BTQLEJgRln9yff6m%2Fdev8O9GnsRQlMbtuxckVtgE6MSgbWlGo1G%2FIKXQrmnLEa3ucYjA18r5tjgMCjJnjmHm7rW6ZGxbdtWY%2Bsl9kSwNGdf1jINSsc0b7x9Muo3ddBr1PzzJAKSVJqt%2BUnjyg1JBo97SW5wz4JRRSqlb1DhKf%2BtPFgVaHTw7537NYFhVv5D2l5x8iADR5pI%2B%2F2Tlj1REBQeWhVPIrC4fWuiUPVzpjBb0Js3gGaj9vmVCnOkE8lIulW2NVz8O%2BrkZyN5dpNoYZH%2BX8lN1rI1RLPjwwNNFlzdi5ebgQ0sN4SzPPrPlb%2BHnPggHwr%2BKyoekM9iUul1SXvqgiVQgDQ0ozy8OJXR7Ei%2FDjNS7%2BC6GAK4C0r1D9M%2FZ9mnut7EyVl03U45CUirwdI%2FICkKh%2F3cqm00EhaUz5tppS5rHlQ%2BCct04JZIp1nik2N2%2Bl8qIlF2AlTg5zc7JYVfSK9jR7kWVGYdMS1aZjt8TZRcgVAvTzA6uxPrPtjLx1WsR1nyCdnlVmfOAJR9RjBIeMzBNonxudvq3R0SPxTDo9OMJZw9c6%2BtrUAglB4Om8wxeONvQY6pgGgnadFG9WdNc1prG2gj2TfsFPO1PIxqw86tRNIeV9vLLRU%2F4dj6v%2BkRn3CsQjY%2Fgw6qY9FPgli6MPegmKm03XoodkgeqwWjRD5BPUK%2BvCtFgqF9en%2F3JCvWTHPU7dYPgS63BvbEL7pRKVj2fSJPUUpdmUCGAqHCMs1CEPKN%2FMUKdigFzPwjkfdwh6VUo9iSmIF9c%2FaacFYW3gkUh9kLD1M%2BD4UXmcf&X-Amz-Signature=a47abf01b691a3b474c8e9bd7af0053b56f3f580177fa9fa7f90ef435d3c2134&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGYZQH4Y%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJGMEQCIE9PSglxkfR%2F5Mlygo%2FyWV4ItnVkUdUvzitwSlyHD%2FHuAiAKEa57cQUMhljeKBi9xQNXvVojM6tyRdjagNEhm16t3yr%2FAwhHEAAaDDYzNzQyMzE4MzgwNSIMW8P8%2FBUK%2Bsd4ppvkKtwDKaTUHVH6Vum7rJmPXsXyeUUO5Bi4SINetWhb%2FVNIWNf0OYg4%2F%2Fnf7%2Bl4m1%2BTQLEJgRln9yff6m%2Fdev8O9GnsRQlMbtuxckVtgE6MSgbWlGo1G%2FIKXQrmnLEa3ucYjA18r5tjgMCjJnjmHm7rW6ZGxbdtWY%2Bsl9kSwNGdf1jINSsc0b7x9Muo3ddBr1PzzJAKSVJqt%2BUnjyg1JBo97SW5wz4JRRSqlb1DhKf%2BtPFgVaHTw7537NYFhVv5D2l5x8iADR5pI%2B%2F2Tlj1REBQeWhVPIrC4fWuiUPVzpjBb0Js3gGaj9vmVCnOkE8lIulW2NVz8O%2BrkZyN5dpNoYZH%2BX8lN1rI1RLPjwwNNFlzdi5ebgQ0sN4SzPPrPlb%2BHnPggHwr%2BKyoekM9iUul1SXvqgiVQgDQ0ozy8OJXR7Ei%2FDjNS7%2BC6GAK4C0r1D9M%2FZ9mnut7EyVl03U45CUirwdI%2FICkKh%2F3cqm00EhaUz5tppS5rHlQ%2BCct04JZIp1nik2N2%2Bl8qIlF2AlTg5zc7JYVfSK9jR7kWVGYdMS1aZjt8TZRcgVAvTzA6uxPrPtjLx1WsR1nyCdnlVmfOAJR9RjBIeMzBNonxudvq3R0SPxTDo9OMJZw9c6%2BtrUAglB4Om8wxeONvQY6pgGgnadFG9WdNc1prG2gj2TfsFPO1PIxqw86tRNIeV9vLLRU%2F4dj6v%2BkRn3CsQjY%2Fgw6qY9FPgli6MPegmKm03XoodkgeqwWjRD5BPUK%2BvCtFgqF9en%2F3JCvWTHPU7dYPgS63BvbEL7pRKVj2fSJPUUpdmUCGAqHCMs1CEPKN%2FMUKdigFzPwjkfdwh6VUo9iSmIF9c%2FaacFYW3gkUh9kLD1M%2BD4UXmcf&X-Amz-Signature=003d494929a279d00a3906d85766ee9580f41666e5a728f20d4b0c3460a29130&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGYZQH4Y%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJGMEQCIE9PSglxkfR%2F5Mlygo%2FyWV4ItnVkUdUvzitwSlyHD%2FHuAiAKEa57cQUMhljeKBi9xQNXvVojM6tyRdjagNEhm16t3yr%2FAwhHEAAaDDYzNzQyMzE4MzgwNSIMW8P8%2FBUK%2Bsd4ppvkKtwDKaTUHVH6Vum7rJmPXsXyeUUO5Bi4SINetWhb%2FVNIWNf0OYg4%2F%2Fnf7%2Bl4m1%2BTQLEJgRln9yff6m%2Fdev8O9GnsRQlMbtuxckVtgE6MSgbWlGo1G%2FIKXQrmnLEa3ucYjA18r5tjgMCjJnjmHm7rW6ZGxbdtWY%2Bsl9kSwNGdf1jINSsc0b7x9Muo3ddBr1PzzJAKSVJqt%2BUnjyg1JBo97SW5wz4JRRSqlb1DhKf%2BtPFgVaHTw7537NYFhVv5D2l5x8iADR5pI%2B%2F2Tlj1REBQeWhVPIrC4fWuiUPVzpjBb0Js3gGaj9vmVCnOkE8lIulW2NVz8O%2BrkZyN5dpNoYZH%2BX8lN1rI1RLPjwwNNFlzdi5ebgQ0sN4SzPPrPlb%2BHnPggHwr%2BKyoekM9iUul1SXvqgiVQgDQ0ozy8OJXR7Ei%2FDjNS7%2BC6GAK4C0r1D9M%2FZ9mnut7EyVl03U45CUirwdI%2FICkKh%2F3cqm00EhaUz5tppS5rHlQ%2BCct04JZIp1nik2N2%2Bl8qIlF2AlTg5zc7JYVfSK9jR7kWVGYdMS1aZjt8TZRcgVAvTzA6uxPrPtjLx1WsR1nyCdnlVmfOAJR9RjBIeMzBNonxudvq3R0SPxTDo9OMJZw9c6%2BtrUAglB4Om8wxeONvQY6pgGgnadFG9WdNc1prG2gj2TfsFPO1PIxqw86tRNIeV9vLLRU%2F4dj6v%2BkRn3CsQjY%2Fgw6qY9FPgli6MPegmKm03XoodkgeqwWjRD5BPUK%2BvCtFgqF9en%2F3JCvWTHPU7dYPgS63BvbEL7pRKVj2fSJPUUpdmUCGAqHCMs1CEPKN%2FMUKdigFzPwjkfdwh6VUo9iSmIF9c%2FaacFYW3gkUh9kLD1M%2BD4UXmcf&X-Amz-Signature=3a8914b9fab1439c056b9d910f1131e3098ed5bef10ac53a34af2bf4ff72a4ca&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGYZQH4Y%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJGMEQCIE9PSglxkfR%2F5Mlygo%2FyWV4ItnVkUdUvzitwSlyHD%2FHuAiAKEa57cQUMhljeKBi9xQNXvVojM6tyRdjagNEhm16t3yr%2FAwhHEAAaDDYzNzQyMzE4MzgwNSIMW8P8%2FBUK%2Bsd4ppvkKtwDKaTUHVH6Vum7rJmPXsXyeUUO5Bi4SINetWhb%2FVNIWNf0OYg4%2F%2Fnf7%2Bl4m1%2BTQLEJgRln9yff6m%2Fdev8O9GnsRQlMbtuxckVtgE6MSgbWlGo1G%2FIKXQrmnLEa3ucYjA18r5tjgMCjJnjmHm7rW6ZGxbdtWY%2Bsl9kSwNGdf1jINSsc0b7x9Muo3ddBr1PzzJAKSVJqt%2BUnjyg1JBo97SW5wz4JRRSqlb1DhKf%2BtPFgVaHTw7537NYFhVv5D2l5x8iADR5pI%2B%2F2Tlj1REBQeWhVPIrC4fWuiUPVzpjBb0Js3gGaj9vmVCnOkE8lIulW2NVz8O%2BrkZyN5dpNoYZH%2BX8lN1rI1RLPjwwNNFlzdi5ebgQ0sN4SzPPrPlb%2BHnPggHwr%2BKyoekM9iUul1SXvqgiVQgDQ0ozy8OJXR7Ei%2FDjNS7%2BC6GAK4C0r1D9M%2FZ9mnut7EyVl03U45CUirwdI%2FICkKh%2F3cqm00EhaUz5tppS5rHlQ%2BCct04JZIp1nik2N2%2Bl8qIlF2AlTg5zc7JYVfSK9jR7kWVGYdMS1aZjt8TZRcgVAvTzA6uxPrPtjLx1WsR1nyCdnlVmfOAJR9RjBIeMzBNonxudvq3R0SPxTDo9OMJZw9c6%2BtrUAglB4Om8wxeONvQY6pgGgnadFG9WdNc1prG2gj2TfsFPO1PIxqw86tRNIeV9vLLRU%2F4dj6v%2BkRn3CsQjY%2Fgw6qY9FPgli6MPegmKm03XoodkgeqwWjRD5BPUK%2BvCtFgqF9en%2F3JCvWTHPU7dYPgS63BvbEL7pRKVj2fSJPUUpdmUCGAqHCMs1CEPKN%2FMUKdigFzPwjkfdwh6VUo9iSmIF9c%2FaacFYW3gkUh9kLD1M%2BD4UXmcf&X-Amz-Signature=e5b479119a8a1f7452d42167406154642e60f0d250de4154262b2afd8a4bbbc7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGYZQH4Y%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJGMEQCIE9PSglxkfR%2F5Mlygo%2FyWV4ItnVkUdUvzitwSlyHD%2FHuAiAKEa57cQUMhljeKBi9xQNXvVojM6tyRdjagNEhm16t3yr%2FAwhHEAAaDDYzNzQyMzE4MzgwNSIMW8P8%2FBUK%2Bsd4ppvkKtwDKaTUHVH6Vum7rJmPXsXyeUUO5Bi4SINetWhb%2FVNIWNf0OYg4%2F%2Fnf7%2Bl4m1%2BTQLEJgRln9yff6m%2Fdev8O9GnsRQlMbtuxckVtgE6MSgbWlGo1G%2FIKXQrmnLEa3ucYjA18r5tjgMCjJnjmHm7rW6ZGxbdtWY%2Bsl9kSwNGdf1jINSsc0b7x9Muo3ddBr1PzzJAKSVJqt%2BUnjyg1JBo97SW5wz4JRRSqlb1DhKf%2BtPFgVaHTw7537NYFhVv5D2l5x8iADR5pI%2B%2F2Tlj1REBQeWhVPIrC4fWuiUPVzpjBb0Js3gGaj9vmVCnOkE8lIulW2NVz8O%2BrkZyN5dpNoYZH%2BX8lN1rI1RLPjwwNNFlzdi5ebgQ0sN4SzPPrPlb%2BHnPggHwr%2BKyoekM9iUul1SXvqgiVQgDQ0ozy8OJXR7Ei%2FDjNS7%2BC6GAK4C0r1D9M%2FZ9mnut7EyVl03U45CUirwdI%2FICkKh%2F3cqm00EhaUz5tppS5rHlQ%2BCct04JZIp1nik2N2%2Bl8qIlF2AlTg5zc7JYVfSK9jR7kWVGYdMS1aZjt8TZRcgVAvTzA6uxPrPtjLx1WsR1nyCdnlVmfOAJR9RjBIeMzBNonxudvq3R0SPxTDo9OMJZw9c6%2BtrUAglB4Om8wxeONvQY6pgGgnadFG9WdNc1prG2gj2TfsFPO1PIxqw86tRNIeV9vLLRU%2F4dj6v%2BkRn3CsQjY%2Fgw6qY9FPgli6MPegmKm03XoodkgeqwWjRD5BPUK%2BvCtFgqF9en%2F3JCvWTHPU7dYPgS63BvbEL7pRKVj2fSJPUUpdmUCGAqHCMs1CEPKN%2FMUKdigFzPwjkfdwh6VUo9iSmIF9c%2FaacFYW3gkUh9kLD1M%2BD4UXmcf&X-Amz-Signature=53691d40daaf0ac960da7bb480ee51de0e5021b008adf8f27ab3ce5dfe9aaad5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGYZQH4Y%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJGMEQCIE9PSglxkfR%2F5Mlygo%2FyWV4ItnVkUdUvzitwSlyHD%2FHuAiAKEa57cQUMhljeKBi9xQNXvVojM6tyRdjagNEhm16t3yr%2FAwhHEAAaDDYzNzQyMzE4MzgwNSIMW8P8%2FBUK%2Bsd4ppvkKtwDKaTUHVH6Vum7rJmPXsXyeUUO5Bi4SINetWhb%2FVNIWNf0OYg4%2F%2Fnf7%2Bl4m1%2BTQLEJgRln9yff6m%2Fdev8O9GnsRQlMbtuxckVtgE6MSgbWlGo1G%2FIKXQrmnLEa3ucYjA18r5tjgMCjJnjmHm7rW6ZGxbdtWY%2Bsl9kSwNGdf1jINSsc0b7x9Muo3ddBr1PzzJAKSVJqt%2BUnjyg1JBo97SW5wz4JRRSqlb1DhKf%2BtPFgVaHTw7537NYFhVv5D2l5x8iADR5pI%2B%2F2Tlj1REBQeWhVPIrC4fWuiUPVzpjBb0Js3gGaj9vmVCnOkE8lIulW2NVz8O%2BrkZyN5dpNoYZH%2BX8lN1rI1RLPjwwNNFlzdi5ebgQ0sN4SzPPrPlb%2BHnPggHwr%2BKyoekM9iUul1SXvqgiVQgDQ0ozy8OJXR7Ei%2FDjNS7%2BC6GAK4C0r1D9M%2FZ9mnut7EyVl03U45CUirwdI%2FICkKh%2F3cqm00EhaUz5tppS5rHlQ%2BCct04JZIp1nik2N2%2Bl8qIlF2AlTg5zc7JYVfSK9jR7kWVGYdMS1aZjt8TZRcgVAvTzA6uxPrPtjLx1WsR1nyCdnlVmfOAJR9RjBIeMzBNonxudvq3R0SPxTDo9OMJZw9c6%2BtrUAglB4Om8wxeONvQY6pgGgnadFG9WdNc1prG2gj2TfsFPO1PIxqw86tRNIeV9vLLRU%2F4dj6v%2BkRn3CsQjY%2Fgw6qY9FPgli6MPegmKm03XoodkgeqwWjRD5BPUK%2BvCtFgqF9en%2F3JCvWTHPU7dYPgS63BvbEL7pRKVj2fSJPUUpdmUCGAqHCMs1CEPKN%2FMUKdigFzPwjkfdwh6VUo9iSmIF9c%2FaacFYW3gkUh9kLD1M%2BD4UXmcf&X-Amz-Signature=53d722b2edd9ae476199786f9a347fc13cc466bdd7ee00a760f3a8d35701f603&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662NTUR5QC%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQChw7wcJFfpQdokHeGuPgyD4h4wvnFltm%2B5Bi2A9so6CQIhAP87WSsk5xnnK01EtbAjx7FFp%2FtSO8d%2FojBnZDfeiShaKv8DCEQQABoMNjM3NDIzMTgzODA1Igx4I5FbDY%2FZXAAlfjkq3ANqaASHDG%2F729T3QVuFm57klKO%2BCErt%2BVEjT0WXsvneQGl3pS4Ptp2U51VZjCuK5f225ljT1nZJbTa%2FjOTXKh%2Fvr8Fn0%2BZ%2FbI%2FEZ9vGwI0pnF%2FCRRPNXyUH155tU5%2Bog3TEk%2FAtDtvFStnDZLoBDlUobQ1x6RtnzdcRc5CH0ue71XgL0M9N%2BE%2FVTsx%2BM1wlODaue3gt3NU1iqOeGL2Y8QW%2BXe06V4%2Fls1b8xQy7zC1wWJKFOvs3TfwVrhm7plc%2B1deeIJQvryfk0pLaIkQUvKOlogXQRAxOC0yiSwjwH0XFoH18stactZYxBGRtRfWLpdq6DRqxHxtDJtqmQeYGYxZ2rfpm60v4w6gVv79t4lYXuyfWT9gX4rQvQCFffVfy4ko5FJrZqtEbQbORXBghn9xC%2BLmAEIXeMpmvyCtw0jekO0GBZiPmPzDKrfy6EeV37rS3OhNvao2dvlKPJwNr0cwiaQLslIPM4681S1K3eIscHAtfT1ZPIBT0EKKrnWmzZYmB1dYUX20BIW9p9wNv0AJq%2F40mcCFv6v2ZTfimzH2BQDIUhijJdY5uRnVvB3U1ifatCV43WPOR%2FGpJN1KdJl3CQzHI2%2FxT5rCJcWMw98Ytu4jz8C8%2FoS3V3DvGhTCgi429BjqkAWVFQ2TE0bm7AlxCtgYy6BmEBOSrnx8BLpD4yIijuiXr86dxJCOhfTxEiXof1EBqUzg3%2BKOtK5eCp82z3dsVwbFR6geCzZ38zHZpURKaPCZS0sEs6PgkSmyW3ZZV%2FiesxiEDYBUW9jMkPcYhsJ%2FLVk7MnBTNk0sYjJp25v%2Bbfjih61ZoSpGnaKj0gDxE2mQM%2FtKFFrzJniezhzQkoEpTp1z7rGty&X-Amz-Signature=682d0bebf23337a719344714e6c414e54452f9f6261655f34512a73b0fce128e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662NTUR5QC%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQChw7wcJFfpQdokHeGuPgyD4h4wvnFltm%2B5Bi2A9so6CQIhAP87WSsk5xnnK01EtbAjx7FFp%2FtSO8d%2FojBnZDfeiShaKv8DCEQQABoMNjM3NDIzMTgzODA1Igx4I5FbDY%2FZXAAlfjkq3ANqaASHDG%2F729T3QVuFm57klKO%2BCErt%2BVEjT0WXsvneQGl3pS4Ptp2U51VZjCuK5f225ljT1nZJbTa%2FjOTXKh%2Fvr8Fn0%2BZ%2FbI%2FEZ9vGwI0pnF%2FCRRPNXyUH155tU5%2Bog3TEk%2FAtDtvFStnDZLoBDlUobQ1x6RtnzdcRc5CH0ue71XgL0M9N%2BE%2FVTsx%2BM1wlODaue3gt3NU1iqOeGL2Y8QW%2BXe06V4%2Fls1b8xQy7zC1wWJKFOvs3TfwVrhm7plc%2B1deeIJQvryfk0pLaIkQUvKOlogXQRAxOC0yiSwjwH0XFoH18stactZYxBGRtRfWLpdq6DRqxHxtDJtqmQeYGYxZ2rfpm60v4w6gVv79t4lYXuyfWT9gX4rQvQCFffVfy4ko5FJrZqtEbQbORXBghn9xC%2BLmAEIXeMpmvyCtw0jekO0GBZiPmPzDKrfy6EeV37rS3OhNvao2dvlKPJwNr0cwiaQLslIPM4681S1K3eIscHAtfT1ZPIBT0EKKrnWmzZYmB1dYUX20BIW9p9wNv0AJq%2F40mcCFv6v2ZTfimzH2BQDIUhijJdY5uRnVvB3U1ifatCV43WPOR%2FGpJN1KdJl3CQzHI2%2FxT5rCJcWMw98Ytu4jz8C8%2FoS3V3DvGhTCgi429BjqkAWVFQ2TE0bm7AlxCtgYy6BmEBOSrnx8BLpD4yIijuiXr86dxJCOhfTxEiXof1EBqUzg3%2BKOtK5eCp82z3dsVwbFR6geCzZ38zHZpURKaPCZS0sEs6PgkSmyW3ZZV%2FiesxiEDYBUW9jMkPcYhsJ%2FLVk7MnBTNk0sYjJp25v%2Bbfjih61ZoSpGnaKj0gDxE2mQM%2FtKFFrzJniezhzQkoEpTp1z7rGty&X-Amz-Signature=93162876312857a7a526d4c4aea1250fe343ac6b1d3b3e0cdae3f3a0af76800e&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
