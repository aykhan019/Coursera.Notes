

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PDICGLX%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCVu5%2Fzj%2FBF%2BCPKoOTQBPt59r91aKcTzEBA1bFZEbCgigIgORdkk9DLzFvXtQfbWVqCL%2BAJQac%2Ff5Y1eDO%2BD8dZGUQqiAQIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHY93s2vvlES0XlwPircA9idcYCt2PrZQkUfpX4ggsUfLPERQRky%2FYyrcv1f2IyN4FLzNJnJVDURcSNhtuUmVhZDdJ5JGGbZQ9Ts7M%2F144uP8kbQYl3aDOYXBake0kHapCjBL0NuDGQf4L4gzU9I2jFkI7FBzcOJ5ccyJMLbW9ahmJmKpZZAAL4lj6R7awVVd%2FD2wupYfa7v2lJ07bWx6kPzrMCUREJ0walo%2BRxRJzzmFykyo%2BcY8Un%2Bd4gcfCpj2GoOh%2BchM10wANMuxNT%2Fh3lWXOPC9gJjA3TvkZNRssDeX0NbBKjXcQOHpqj1ANXIgUFc9vsCYkzS%2FNNwfd6tZi0Fv6WS01uHIwF67n4MNNPOzdHrEIfoKnCLpgH4zYa%2FWrf8jSSOFPro2hzM%2BGb%2BfdcSAtd0l1kMhvygHdCUYz4qvMaFmduA45bdaaaGlrba18GapTAM2h17Sy%2BeTG851q8XRXM89kwPBKLZHBNjzqlZHoELsr1M0t%2FRntooHHwYXZnboHaOTjzjukEohwyiS5qKg6iQgxlu4LYSvWuVlDxLlZW%2FSrID5qJCkmK257U7wHCiE1O%2BM61ZLXxwqJparRNme8gl8WPzs7nDws8W71WuKLTAtjAR919iQWIpaiklvRp%2F3qP9aItdSBTeMID69rwGOqUBdcRpWZbTMZK2J6Epf74DOQ7YjA7%2BPojSYy3iTxvBQXsRHFZS5nfW6N5DRoPTcYur6aEmZoWtV%2BGP2BZ%2B0C9gveaCR8vSpbfRpAc1P5jsol2iQEnwSv0FduOkusJYCEQ%2FjB2yBSjuLB1QjVL8pFj2EH7BNNMtPvPFJ7qmGR5GbIfS2dpB0LWcjwXUm4UwU0D0gaB0vYJKIuiDmplHDy7EdbnCufLK&X-Amz-Signature=be011e6a86c8e44860da830a1e0cd6d8cf08f879ac2fc48c7f2ff296c7345311&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PDICGLX%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCVu5%2Fzj%2FBF%2BCPKoOTQBPt59r91aKcTzEBA1bFZEbCgigIgORdkk9DLzFvXtQfbWVqCL%2BAJQac%2Ff5Y1eDO%2BD8dZGUQqiAQIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHY93s2vvlES0XlwPircA9idcYCt2PrZQkUfpX4ggsUfLPERQRky%2FYyrcv1f2IyN4FLzNJnJVDURcSNhtuUmVhZDdJ5JGGbZQ9Ts7M%2F144uP8kbQYl3aDOYXBake0kHapCjBL0NuDGQf4L4gzU9I2jFkI7FBzcOJ5ccyJMLbW9ahmJmKpZZAAL4lj6R7awVVd%2FD2wupYfa7v2lJ07bWx6kPzrMCUREJ0walo%2BRxRJzzmFykyo%2BcY8Un%2Bd4gcfCpj2GoOh%2BchM10wANMuxNT%2Fh3lWXOPC9gJjA3TvkZNRssDeX0NbBKjXcQOHpqj1ANXIgUFc9vsCYkzS%2FNNwfd6tZi0Fv6WS01uHIwF67n4MNNPOzdHrEIfoKnCLpgH4zYa%2FWrf8jSSOFPro2hzM%2BGb%2BfdcSAtd0l1kMhvygHdCUYz4qvMaFmduA45bdaaaGlrba18GapTAM2h17Sy%2BeTG851q8XRXM89kwPBKLZHBNjzqlZHoELsr1M0t%2FRntooHHwYXZnboHaOTjzjukEohwyiS5qKg6iQgxlu4LYSvWuVlDxLlZW%2FSrID5qJCkmK257U7wHCiE1O%2BM61ZLXxwqJparRNme8gl8WPzs7nDws8W71WuKLTAtjAR919iQWIpaiklvRp%2F3qP9aItdSBTeMID69rwGOqUBdcRpWZbTMZK2J6Epf74DOQ7YjA7%2BPojSYy3iTxvBQXsRHFZS5nfW6N5DRoPTcYur6aEmZoWtV%2BGP2BZ%2B0C9gveaCR8vSpbfRpAc1P5jsol2iQEnwSv0FduOkusJYCEQ%2FjB2yBSjuLB1QjVL8pFj2EH7BNNMtPvPFJ7qmGR5GbIfS2dpB0LWcjwXUm4UwU0D0gaB0vYJKIuiDmplHDy7EdbnCufLK&X-Amz-Signature=cdecfd24ba880a4e852d5c81e007787e5be93a9f17a002bdabdafe3b21f6b0c7&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PDICGLX%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCVu5%2Fzj%2FBF%2BCPKoOTQBPt59r91aKcTzEBA1bFZEbCgigIgORdkk9DLzFvXtQfbWVqCL%2BAJQac%2Ff5Y1eDO%2BD8dZGUQqiAQIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHY93s2vvlES0XlwPircA9idcYCt2PrZQkUfpX4ggsUfLPERQRky%2FYyrcv1f2IyN4FLzNJnJVDURcSNhtuUmVhZDdJ5JGGbZQ9Ts7M%2F144uP8kbQYl3aDOYXBake0kHapCjBL0NuDGQf4L4gzU9I2jFkI7FBzcOJ5ccyJMLbW9ahmJmKpZZAAL4lj6R7awVVd%2FD2wupYfa7v2lJ07bWx6kPzrMCUREJ0walo%2BRxRJzzmFykyo%2BcY8Un%2Bd4gcfCpj2GoOh%2BchM10wANMuxNT%2Fh3lWXOPC9gJjA3TvkZNRssDeX0NbBKjXcQOHpqj1ANXIgUFc9vsCYkzS%2FNNwfd6tZi0Fv6WS01uHIwF67n4MNNPOzdHrEIfoKnCLpgH4zYa%2FWrf8jSSOFPro2hzM%2BGb%2BfdcSAtd0l1kMhvygHdCUYz4qvMaFmduA45bdaaaGlrba18GapTAM2h17Sy%2BeTG851q8XRXM89kwPBKLZHBNjzqlZHoELsr1M0t%2FRntooHHwYXZnboHaOTjzjukEohwyiS5qKg6iQgxlu4LYSvWuVlDxLlZW%2FSrID5qJCkmK257U7wHCiE1O%2BM61ZLXxwqJparRNme8gl8WPzs7nDws8W71WuKLTAtjAR919iQWIpaiklvRp%2F3qP9aItdSBTeMID69rwGOqUBdcRpWZbTMZK2J6Epf74DOQ7YjA7%2BPojSYy3iTxvBQXsRHFZS5nfW6N5DRoPTcYur6aEmZoWtV%2BGP2BZ%2B0C9gveaCR8vSpbfRpAc1P5jsol2iQEnwSv0FduOkusJYCEQ%2FjB2yBSjuLB1QjVL8pFj2EH7BNNMtPvPFJ7qmGR5GbIfS2dpB0LWcjwXUm4UwU0D0gaB0vYJKIuiDmplHDy7EdbnCufLK&X-Amz-Signature=54d4b3604fbeac91ae5e459acf56526788f63730ae38829c2b592e29096151e4&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PDICGLX%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCVu5%2Fzj%2FBF%2BCPKoOTQBPt59r91aKcTzEBA1bFZEbCgigIgORdkk9DLzFvXtQfbWVqCL%2BAJQac%2Ff5Y1eDO%2BD8dZGUQqiAQIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHY93s2vvlES0XlwPircA9idcYCt2PrZQkUfpX4ggsUfLPERQRky%2FYyrcv1f2IyN4FLzNJnJVDURcSNhtuUmVhZDdJ5JGGbZQ9Ts7M%2F144uP8kbQYl3aDOYXBake0kHapCjBL0NuDGQf4L4gzU9I2jFkI7FBzcOJ5ccyJMLbW9ahmJmKpZZAAL4lj6R7awVVd%2FD2wupYfa7v2lJ07bWx6kPzrMCUREJ0walo%2BRxRJzzmFykyo%2BcY8Un%2Bd4gcfCpj2GoOh%2BchM10wANMuxNT%2Fh3lWXOPC9gJjA3TvkZNRssDeX0NbBKjXcQOHpqj1ANXIgUFc9vsCYkzS%2FNNwfd6tZi0Fv6WS01uHIwF67n4MNNPOzdHrEIfoKnCLpgH4zYa%2FWrf8jSSOFPro2hzM%2BGb%2BfdcSAtd0l1kMhvygHdCUYz4qvMaFmduA45bdaaaGlrba18GapTAM2h17Sy%2BeTG851q8XRXM89kwPBKLZHBNjzqlZHoELsr1M0t%2FRntooHHwYXZnboHaOTjzjukEohwyiS5qKg6iQgxlu4LYSvWuVlDxLlZW%2FSrID5qJCkmK257U7wHCiE1O%2BM61ZLXxwqJparRNme8gl8WPzs7nDws8W71WuKLTAtjAR919iQWIpaiklvRp%2F3qP9aItdSBTeMID69rwGOqUBdcRpWZbTMZK2J6Epf74DOQ7YjA7%2BPojSYy3iTxvBQXsRHFZS5nfW6N5DRoPTcYur6aEmZoWtV%2BGP2BZ%2B0C9gveaCR8vSpbfRpAc1P5jsol2iQEnwSv0FduOkusJYCEQ%2FjB2yBSjuLB1QjVL8pFj2EH7BNNMtPvPFJ7qmGR5GbIfS2dpB0LWcjwXUm4UwU0D0gaB0vYJKIuiDmplHDy7EdbnCufLK&X-Amz-Signature=421d41bbef8d476bdfb782f3201cd59ea121dc8780fdf4cc2c0190eab64bb1a5&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PDICGLX%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCVu5%2Fzj%2FBF%2BCPKoOTQBPt59r91aKcTzEBA1bFZEbCgigIgORdkk9DLzFvXtQfbWVqCL%2BAJQac%2Ff5Y1eDO%2BD8dZGUQqiAQIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHY93s2vvlES0XlwPircA9idcYCt2PrZQkUfpX4ggsUfLPERQRky%2FYyrcv1f2IyN4FLzNJnJVDURcSNhtuUmVhZDdJ5JGGbZQ9Ts7M%2F144uP8kbQYl3aDOYXBake0kHapCjBL0NuDGQf4L4gzU9I2jFkI7FBzcOJ5ccyJMLbW9ahmJmKpZZAAL4lj6R7awVVd%2FD2wupYfa7v2lJ07bWx6kPzrMCUREJ0walo%2BRxRJzzmFykyo%2BcY8Un%2Bd4gcfCpj2GoOh%2BchM10wANMuxNT%2Fh3lWXOPC9gJjA3TvkZNRssDeX0NbBKjXcQOHpqj1ANXIgUFc9vsCYkzS%2FNNwfd6tZi0Fv6WS01uHIwF67n4MNNPOzdHrEIfoKnCLpgH4zYa%2FWrf8jSSOFPro2hzM%2BGb%2BfdcSAtd0l1kMhvygHdCUYz4qvMaFmduA45bdaaaGlrba18GapTAM2h17Sy%2BeTG851q8XRXM89kwPBKLZHBNjzqlZHoELsr1M0t%2FRntooHHwYXZnboHaOTjzjukEohwyiS5qKg6iQgxlu4LYSvWuVlDxLlZW%2FSrID5qJCkmK257U7wHCiE1O%2BM61ZLXxwqJparRNme8gl8WPzs7nDws8W71WuKLTAtjAR919iQWIpaiklvRp%2F3qP9aItdSBTeMID69rwGOqUBdcRpWZbTMZK2J6Epf74DOQ7YjA7%2BPojSYy3iTxvBQXsRHFZS5nfW6N5DRoPTcYur6aEmZoWtV%2BGP2BZ%2B0C9gveaCR8vSpbfRpAc1P5jsol2iQEnwSv0FduOkusJYCEQ%2FjB2yBSjuLB1QjVL8pFj2EH7BNNMtPvPFJ7qmGR5GbIfS2dpB0LWcjwXUm4UwU0D0gaB0vYJKIuiDmplHDy7EdbnCufLK&X-Amz-Signature=0a28a499f210c5611139f760aafcb5ec345848d80716ef6e4866c533ba92d81d&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PDICGLX%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCVu5%2Fzj%2FBF%2BCPKoOTQBPt59r91aKcTzEBA1bFZEbCgigIgORdkk9DLzFvXtQfbWVqCL%2BAJQac%2Ff5Y1eDO%2BD8dZGUQqiAQIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHY93s2vvlES0XlwPircA9idcYCt2PrZQkUfpX4ggsUfLPERQRky%2FYyrcv1f2IyN4FLzNJnJVDURcSNhtuUmVhZDdJ5JGGbZQ9Ts7M%2F144uP8kbQYl3aDOYXBake0kHapCjBL0NuDGQf4L4gzU9I2jFkI7FBzcOJ5ccyJMLbW9ahmJmKpZZAAL4lj6R7awVVd%2FD2wupYfa7v2lJ07bWx6kPzrMCUREJ0walo%2BRxRJzzmFykyo%2BcY8Un%2Bd4gcfCpj2GoOh%2BchM10wANMuxNT%2Fh3lWXOPC9gJjA3TvkZNRssDeX0NbBKjXcQOHpqj1ANXIgUFc9vsCYkzS%2FNNwfd6tZi0Fv6WS01uHIwF67n4MNNPOzdHrEIfoKnCLpgH4zYa%2FWrf8jSSOFPro2hzM%2BGb%2BfdcSAtd0l1kMhvygHdCUYz4qvMaFmduA45bdaaaGlrba18GapTAM2h17Sy%2BeTG851q8XRXM89kwPBKLZHBNjzqlZHoELsr1M0t%2FRntooHHwYXZnboHaOTjzjukEohwyiS5qKg6iQgxlu4LYSvWuVlDxLlZW%2FSrID5qJCkmK257U7wHCiE1O%2BM61ZLXxwqJparRNme8gl8WPzs7nDws8W71WuKLTAtjAR919iQWIpaiklvRp%2F3qP9aItdSBTeMID69rwGOqUBdcRpWZbTMZK2J6Epf74DOQ7YjA7%2BPojSYy3iTxvBQXsRHFZS5nfW6N5DRoPTcYur6aEmZoWtV%2BGP2BZ%2B0C9gveaCR8vSpbfRpAc1P5jsol2iQEnwSv0FduOkusJYCEQ%2FjB2yBSjuLB1QjVL8pFj2EH7BNNMtPvPFJ7qmGR5GbIfS2dpB0LWcjwXUm4UwU0D0gaB0vYJKIuiDmplHDy7EdbnCufLK&X-Amz-Signature=0f8bbd74a1187c9fbbe6e06e4bb581383176a86889bb64ea0a5553e7ef91c930&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PDICGLX%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCVu5%2Fzj%2FBF%2BCPKoOTQBPt59r91aKcTzEBA1bFZEbCgigIgORdkk9DLzFvXtQfbWVqCL%2BAJQac%2Ff5Y1eDO%2BD8dZGUQqiAQIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHY93s2vvlES0XlwPircA9idcYCt2PrZQkUfpX4ggsUfLPERQRky%2FYyrcv1f2IyN4FLzNJnJVDURcSNhtuUmVhZDdJ5JGGbZQ9Ts7M%2F144uP8kbQYl3aDOYXBake0kHapCjBL0NuDGQf4L4gzU9I2jFkI7FBzcOJ5ccyJMLbW9ahmJmKpZZAAL4lj6R7awVVd%2FD2wupYfa7v2lJ07bWx6kPzrMCUREJ0walo%2BRxRJzzmFykyo%2BcY8Un%2Bd4gcfCpj2GoOh%2BchM10wANMuxNT%2Fh3lWXOPC9gJjA3TvkZNRssDeX0NbBKjXcQOHpqj1ANXIgUFc9vsCYkzS%2FNNwfd6tZi0Fv6WS01uHIwF67n4MNNPOzdHrEIfoKnCLpgH4zYa%2FWrf8jSSOFPro2hzM%2BGb%2BfdcSAtd0l1kMhvygHdCUYz4qvMaFmduA45bdaaaGlrba18GapTAM2h17Sy%2BeTG851q8XRXM89kwPBKLZHBNjzqlZHoELsr1M0t%2FRntooHHwYXZnboHaOTjzjukEohwyiS5qKg6iQgxlu4LYSvWuVlDxLlZW%2FSrID5qJCkmK257U7wHCiE1O%2BM61ZLXxwqJparRNme8gl8WPzs7nDws8W71WuKLTAtjAR919iQWIpaiklvRp%2F3qP9aItdSBTeMID69rwGOqUBdcRpWZbTMZK2J6Epf74DOQ7YjA7%2BPojSYy3iTxvBQXsRHFZS5nfW6N5DRoPTcYur6aEmZoWtV%2BGP2BZ%2B0C9gveaCR8vSpbfRpAc1P5jsol2iQEnwSv0FduOkusJYCEQ%2FjB2yBSjuLB1QjVL8pFj2EH7BNNMtPvPFJ7qmGR5GbIfS2dpB0LWcjwXUm4UwU0D0gaB0vYJKIuiDmplHDy7EdbnCufLK&X-Amz-Signature=a855a5c3527d154122b4588adbdafd7284d2b2e907d85d4291af403b161c0a33&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PDICGLX%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCVu5%2Fzj%2FBF%2BCPKoOTQBPt59r91aKcTzEBA1bFZEbCgigIgORdkk9DLzFvXtQfbWVqCL%2BAJQac%2Ff5Y1eDO%2BD8dZGUQqiAQIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHY93s2vvlES0XlwPircA9idcYCt2PrZQkUfpX4ggsUfLPERQRky%2FYyrcv1f2IyN4FLzNJnJVDURcSNhtuUmVhZDdJ5JGGbZQ9Ts7M%2F144uP8kbQYl3aDOYXBake0kHapCjBL0NuDGQf4L4gzU9I2jFkI7FBzcOJ5ccyJMLbW9ahmJmKpZZAAL4lj6R7awVVd%2FD2wupYfa7v2lJ07bWx6kPzrMCUREJ0walo%2BRxRJzzmFykyo%2BcY8Un%2Bd4gcfCpj2GoOh%2BchM10wANMuxNT%2Fh3lWXOPC9gJjA3TvkZNRssDeX0NbBKjXcQOHpqj1ANXIgUFc9vsCYkzS%2FNNwfd6tZi0Fv6WS01uHIwF67n4MNNPOzdHrEIfoKnCLpgH4zYa%2FWrf8jSSOFPro2hzM%2BGb%2BfdcSAtd0l1kMhvygHdCUYz4qvMaFmduA45bdaaaGlrba18GapTAM2h17Sy%2BeTG851q8XRXM89kwPBKLZHBNjzqlZHoELsr1M0t%2FRntooHHwYXZnboHaOTjzjukEohwyiS5qKg6iQgxlu4LYSvWuVlDxLlZW%2FSrID5qJCkmK257U7wHCiE1O%2BM61ZLXxwqJparRNme8gl8WPzs7nDws8W71WuKLTAtjAR919iQWIpaiklvRp%2F3qP9aItdSBTeMID69rwGOqUBdcRpWZbTMZK2J6Epf74DOQ7YjA7%2BPojSYy3iTxvBQXsRHFZS5nfW6N5DRoPTcYur6aEmZoWtV%2BGP2BZ%2B0C9gveaCR8vSpbfRpAc1P5jsol2iQEnwSv0FduOkusJYCEQ%2FjB2yBSjuLB1QjVL8pFj2EH7BNNMtPvPFJ7qmGR5GbIfS2dpB0LWcjwXUm4UwU0D0gaB0vYJKIuiDmplHDy7EdbnCufLK&X-Amz-Signature=052c71ab46236c78d391e6b5b2dbdbe2c38bcf31cf6be2316f5d1d184ec5aacb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PDICGLX%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCVu5%2Fzj%2FBF%2BCPKoOTQBPt59r91aKcTzEBA1bFZEbCgigIgORdkk9DLzFvXtQfbWVqCL%2BAJQac%2Ff5Y1eDO%2BD8dZGUQqiAQIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHY93s2vvlES0XlwPircA9idcYCt2PrZQkUfpX4ggsUfLPERQRky%2FYyrcv1f2IyN4FLzNJnJVDURcSNhtuUmVhZDdJ5JGGbZQ9Ts7M%2F144uP8kbQYl3aDOYXBake0kHapCjBL0NuDGQf4L4gzU9I2jFkI7FBzcOJ5ccyJMLbW9ahmJmKpZZAAL4lj6R7awVVd%2FD2wupYfa7v2lJ07bWx6kPzrMCUREJ0walo%2BRxRJzzmFykyo%2BcY8Un%2Bd4gcfCpj2GoOh%2BchM10wANMuxNT%2Fh3lWXOPC9gJjA3TvkZNRssDeX0NbBKjXcQOHpqj1ANXIgUFc9vsCYkzS%2FNNwfd6tZi0Fv6WS01uHIwF67n4MNNPOzdHrEIfoKnCLpgH4zYa%2FWrf8jSSOFPro2hzM%2BGb%2BfdcSAtd0l1kMhvygHdCUYz4qvMaFmduA45bdaaaGlrba18GapTAM2h17Sy%2BeTG851q8XRXM89kwPBKLZHBNjzqlZHoELsr1M0t%2FRntooHHwYXZnboHaOTjzjukEohwyiS5qKg6iQgxlu4LYSvWuVlDxLlZW%2FSrID5qJCkmK257U7wHCiE1O%2BM61ZLXxwqJparRNme8gl8WPzs7nDws8W71WuKLTAtjAR919iQWIpaiklvRp%2F3qP9aItdSBTeMID69rwGOqUBdcRpWZbTMZK2J6Epf74DOQ7YjA7%2BPojSYy3iTxvBQXsRHFZS5nfW6N5DRoPTcYur6aEmZoWtV%2BGP2BZ%2B0C9gveaCR8vSpbfRpAc1P5jsol2iQEnwSv0FduOkusJYCEQ%2FjB2yBSjuLB1QjVL8pFj2EH7BNNMtPvPFJ7qmGR5GbIfS2dpB0LWcjwXUm4UwU0D0gaB0vYJKIuiDmplHDy7EdbnCufLK&X-Amz-Signature=b25132ceaf8b60970aa4b92c661157f9ec8c5fda586df665c12c819fa3c84790&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QGZLUQ6F%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICFBmlOGZVfr4QDLWop4hJcCaelN8IyHpqm7bc1fuSf8AiEA4Gno8W9K0JHMU%2Fps%2FdObxpYNxKWRKpIDGp9fDxydQWQqiAQIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAXLJNcSZj0fTFSj1yrcA1KEhlteuE0Itl4GafitArtPlXVNk3A4%2Fw%2B7TMNvLlOokzOBFbEpa1mrdvLa1%2BC93omlc7bxOZ6TNxMTXtJ69T6hE0bL98bPGHJn%2B2UPAq2DMBBWMd3lJaPqHv2evrDCy2fsDBdowbcG38Y2PlRrhZaDpCeabquwcmKtNZV87lM4u3hjnZy3mG7juJ%2B4JpnSPphb7qPlHoR%2F90PgT7L4DGIGwetBuQojkXZklNWtc928DAzf8zZFuss%2Fzg0tAsE6jY2KkrKT4R%2F3g%2FQEgakUJu%2FuBAU5C%2FDTOcIjbZ0CZM%2B%2FozJxhC8VT0dqP2szBM5rS1XDMT044kVG%2FGB7u%2BBNPcNKhRq6PjnGLdSq5WkoJM6MDv6BPF3PMj6uQc2GpcBjKqigF1lA0HJAa%2Bnd70JMcvm3HTcT%2Ble03Ty0wn%2B%2FznqDd1HZ5Guq9C0wjDqevL7wUCbxV9zFreWGNAzxcBZlQ8iHUF7ToYT8ltPxw6tIN0d9nzZkJy0ZR5ItLPn1I5OOIb72AJp6hzy9c8FnyG3hoiqosoRHkrciCSTk5IVxsHFFD%2FQ7pI5uSKmsfOT2HQhzM6KgJA3qacL%2FHv0cFmSNt9UppFccWCHNV7HoeUc1SVwUT3hhJ2QvWlS3dGyFMNv59rwGOqUByXZXQEzF1tOGv3rXyHkP1HZMcb9iCR%2BowU4BYwBYMMN7BIokbMhBSBtk2n8cgrVvnv9Q6mz%2FQlbWQg6Ma63wR9r9wYvCfPHq44wIgQqOcks1OQSxYTeKPFpZDGxwAqwAW6QPKkDM670i%2Bg65%2FJ%2B2JRxJbrihBVJrJgxb6Z%2BMVDZ0ZYreAQylwYY16iAEGf%2FSJ9wYd7b2Lr7KI9Bha%2FY8FYtbWVo8&X-Amz-Signature=cb7db9d28611f913f3c0e5eb1fc05f661b78f8f00a273f0e4dd79ae43ddf76fa&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QGZLUQ6F%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICFBmlOGZVfr4QDLWop4hJcCaelN8IyHpqm7bc1fuSf8AiEA4Gno8W9K0JHMU%2Fps%2FdObxpYNxKWRKpIDGp9fDxydQWQqiAQIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAXLJNcSZj0fTFSj1yrcA1KEhlteuE0Itl4GafitArtPlXVNk3A4%2Fw%2B7TMNvLlOokzOBFbEpa1mrdvLa1%2BC93omlc7bxOZ6TNxMTXtJ69T6hE0bL98bPGHJn%2B2UPAq2DMBBWMd3lJaPqHv2evrDCy2fsDBdowbcG38Y2PlRrhZaDpCeabquwcmKtNZV87lM4u3hjnZy3mG7juJ%2B4JpnSPphb7qPlHoR%2F90PgT7L4DGIGwetBuQojkXZklNWtc928DAzf8zZFuss%2Fzg0tAsE6jY2KkrKT4R%2F3g%2FQEgakUJu%2FuBAU5C%2FDTOcIjbZ0CZM%2B%2FozJxhC8VT0dqP2szBM5rS1XDMT044kVG%2FGB7u%2BBNPcNKhRq6PjnGLdSq5WkoJM6MDv6BPF3PMj6uQc2GpcBjKqigF1lA0HJAa%2Bnd70JMcvm3HTcT%2Ble03Ty0wn%2B%2FznqDd1HZ5Guq9C0wjDqevL7wUCbxV9zFreWGNAzxcBZlQ8iHUF7ToYT8ltPxw6tIN0d9nzZkJy0ZR5ItLPn1I5OOIb72AJp6hzy9c8FnyG3hoiqosoRHkrciCSTk5IVxsHFFD%2FQ7pI5uSKmsfOT2HQhzM6KgJA3qacL%2FHv0cFmSNt9UppFccWCHNV7HoeUc1SVwUT3hhJ2QvWlS3dGyFMNv59rwGOqUByXZXQEzF1tOGv3rXyHkP1HZMcb9iCR%2BowU4BYwBYMMN7BIokbMhBSBtk2n8cgrVvnv9Q6mz%2FQlbWQg6Ma63wR9r9wYvCfPHq44wIgQqOcks1OQSxYTeKPFpZDGxwAqwAW6QPKkDM670i%2Bg65%2FJ%2B2JRxJbrihBVJrJgxb6Z%2BMVDZ0ZYreAQylwYY16iAEGf%2FSJ9wYd7b2Lr7KI9Bha%2FY8FYtbWVo8&X-Amz-Signature=493f2f487204043a8cda08b71527401b837147b66760bf19542cac47182d20e3&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
