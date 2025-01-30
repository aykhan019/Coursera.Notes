

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y5T7CX3J%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCe%2B%2BG1%2Fmmrl2GlGDDAdC3lTbKDfiyX9nXGaPqZ24%2BlLgIgIy5u4eFMPFALuvdznmkUKZP6Yplt4D7FNF7AsNQRiNYqiAQIof%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHgbm7OIyPzeCVm1CyrcA%2FRGtJMGIGvujJZX1%2F%2B8Mo1j3l1rAbetv5caN9lVGtQZSqyKOJaNYAJx1j41K8gGFinC%2FyjhLZARObzV%2BuJaoUeExpuICYJYLgqk48VZkgM8%2FtN0gFkYQRLEPvnioRlMThLJY9z0PI97LZ%2B3hRpxrMkGSjjNWYwFWIfj89V%2FhJAmR3pmQvoLxMQFAMgRnRDW5siSdT9BtEB06cNmdEUJp4JWLRe3Dgo75lMyPSkKoDj1vTzP4MzcKOEDvz23XqVfAZk5o%2BoddrpYfCowsK%2BgZHNDnnngvgIjMQHwWLG7QCj0X%2Bii4yQmLiVTHxuXTwvrK8LvqWAuitnIHlvpki8iM4rnru%2BrRB7eTyjbliNWBCiij8joqVj0Whdkd4eBvCCrg24e0J%2BRNFJvJp%2FUWWrHo%2Fcg7UZPIQufniBsejmFuxxub0pyycR5Q8iAA%2BH8qRIpqER%2BAPORS2lY7nwc5ymPX7P4pLR072DcvxFIXEys11O3L71wve31acy5zWKa7qvqWlVXC7NBlP7Bhxpz3t99Ea%2BrZIb3nSkleEAD9ZU8aYew6WjEUkbVDZvDsp9G3SKX%2B6dqSSV9chNEkfs%2BB0XeJ2xzQOL9dhETuwvhfVzje4iiTNEbqsCJqcb31TuzMNrs7LwGOqUBqDXKwutA9aQeXWg1kfOu2z4pUindRh6Wl8oDQFS5npxRvMoZaJNDkVXdjtKio5%2FtMfkZQ0RJF4DKfbabgpJSSbGYeS7ZwT%2BPU1GNfheLs%2BSTrLzCHoDtDaVc%2Bf6qZ%2Bj%2Fa1CQSZ8eOMZX%2FCjbpTRAmvMxwpEQyHe4%2FOiSCzWhM8zC%2FGn%2F2VlNZhfOrVNrcK2FxHIHSrsdWgHzYmI9OYDhPEXY0xxp&X-Amz-Signature=7ec27dbf91dd465e2d1051564941c96461a68ca47e07b23e23b7d45334c703a2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y5T7CX3J%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCe%2B%2BG1%2Fmmrl2GlGDDAdC3lTbKDfiyX9nXGaPqZ24%2BlLgIgIy5u4eFMPFALuvdznmkUKZP6Yplt4D7FNF7AsNQRiNYqiAQIof%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHgbm7OIyPzeCVm1CyrcA%2FRGtJMGIGvujJZX1%2F%2B8Mo1j3l1rAbetv5caN9lVGtQZSqyKOJaNYAJx1j41K8gGFinC%2FyjhLZARObzV%2BuJaoUeExpuICYJYLgqk48VZkgM8%2FtN0gFkYQRLEPvnioRlMThLJY9z0PI97LZ%2B3hRpxrMkGSjjNWYwFWIfj89V%2FhJAmR3pmQvoLxMQFAMgRnRDW5siSdT9BtEB06cNmdEUJp4JWLRe3Dgo75lMyPSkKoDj1vTzP4MzcKOEDvz23XqVfAZk5o%2BoddrpYfCowsK%2BgZHNDnnngvgIjMQHwWLG7QCj0X%2Bii4yQmLiVTHxuXTwvrK8LvqWAuitnIHlvpki8iM4rnru%2BrRB7eTyjbliNWBCiij8joqVj0Whdkd4eBvCCrg24e0J%2BRNFJvJp%2FUWWrHo%2Fcg7UZPIQufniBsejmFuxxub0pyycR5Q8iAA%2BH8qRIpqER%2BAPORS2lY7nwc5ymPX7P4pLR072DcvxFIXEys11O3L71wve31acy5zWKa7qvqWlVXC7NBlP7Bhxpz3t99Ea%2BrZIb3nSkleEAD9ZU8aYew6WjEUkbVDZvDsp9G3SKX%2B6dqSSV9chNEkfs%2BB0XeJ2xzQOL9dhETuwvhfVzje4iiTNEbqsCJqcb31TuzMNrs7LwGOqUBqDXKwutA9aQeXWg1kfOu2z4pUindRh6Wl8oDQFS5npxRvMoZaJNDkVXdjtKio5%2FtMfkZQ0RJF4DKfbabgpJSSbGYeS7ZwT%2BPU1GNfheLs%2BSTrLzCHoDtDaVc%2Bf6qZ%2Bj%2Fa1CQSZ8eOMZX%2FCjbpTRAmvMxwpEQyHe4%2FOiSCzWhM8zC%2FGn%2F2VlNZhfOrVNrcK2FxHIHSrsdWgHzYmI9OYDhPEXY0xxp&X-Amz-Signature=53c18a609375635b370a5abe0bedcd5763d8473acdcf83888350c00dff709d20&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y5T7CX3J%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCe%2B%2BG1%2Fmmrl2GlGDDAdC3lTbKDfiyX9nXGaPqZ24%2BlLgIgIy5u4eFMPFALuvdznmkUKZP6Yplt4D7FNF7AsNQRiNYqiAQIof%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHgbm7OIyPzeCVm1CyrcA%2FRGtJMGIGvujJZX1%2F%2B8Mo1j3l1rAbetv5caN9lVGtQZSqyKOJaNYAJx1j41K8gGFinC%2FyjhLZARObzV%2BuJaoUeExpuICYJYLgqk48VZkgM8%2FtN0gFkYQRLEPvnioRlMThLJY9z0PI97LZ%2B3hRpxrMkGSjjNWYwFWIfj89V%2FhJAmR3pmQvoLxMQFAMgRnRDW5siSdT9BtEB06cNmdEUJp4JWLRe3Dgo75lMyPSkKoDj1vTzP4MzcKOEDvz23XqVfAZk5o%2BoddrpYfCowsK%2BgZHNDnnngvgIjMQHwWLG7QCj0X%2Bii4yQmLiVTHxuXTwvrK8LvqWAuitnIHlvpki8iM4rnru%2BrRB7eTyjbliNWBCiij8joqVj0Whdkd4eBvCCrg24e0J%2BRNFJvJp%2FUWWrHo%2Fcg7UZPIQufniBsejmFuxxub0pyycR5Q8iAA%2BH8qRIpqER%2BAPORS2lY7nwc5ymPX7P4pLR072DcvxFIXEys11O3L71wve31acy5zWKa7qvqWlVXC7NBlP7Bhxpz3t99Ea%2BrZIb3nSkleEAD9ZU8aYew6WjEUkbVDZvDsp9G3SKX%2B6dqSSV9chNEkfs%2BB0XeJ2xzQOL9dhETuwvhfVzje4iiTNEbqsCJqcb31TuzMNrs7LwGOqUBqDXKwutA9aQeXWg1kfOu2z4pUindRh6Wl8oDQFS5npxRvMoZaJNDkVXdjtKio5%2FtMfkZQ0RJF4DKfbabgpJSSbGYeS7ZwT%2BPU1GNfheLs%2BSTrLzCHoDtDaVc%2Bf6qZ%2Bj%2Fa1CQSZ8eOMZX%2FCjbpTRAmvMxwpEQyHe4%2FOiSCzWhM8zC%2FGn%2F2VlNZhfOrVNrcK2FxHIHSrsdWgHzYmI9OYDhPEXY0xxp&X-Amz-Signature=c59e528dc5c97e711e03fff1a376c2045977c57e82ed9e2ac26b4ad7bd7b2fa3&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y5T7CX3J%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCe%2B%2BG1%2Fmmrl2GlGDDAdC3lTbKDfiyX9nXGaPqZ24%2BlLgIgIy5u4eFMPFALuvdznmkUKZP6Yplt4D7FNF7AsNQRiNYqiAQIof%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHgbm7OIyPzeCVm1CyrcA%2FRGtJMGIGvujJZX1%2F%2B8Mo1j3l1rAbetv5caN9lVGtQZSqyKOJaNYAJx1j41K8gGFinC%2FyjhLZARObzV%2BuJaoUeExpuICYJYLgqk48VZkgM8%2FtN0gFkYQRLEPvnioRlMThLJY9z0PI97LZ%2B3hRpxrMkGSjjNWYwFWIfj89V%2FhJAmR3pmQvoLxMQFAMgRnRDW5siSdT9BtEB06cNmdEUJp4JWLRe3Dgo75lMyPSkKoDj1vTzP4MzcKOEDvz23XqVfAZk5o%2BoddrpYfCowsK%2BgZHNDnnngvgIjMQHwWLG7QCj0X%2Bii4yQmLiVTHxuXTwvrK8LvqWAuitnIHlvpki8iM4rnru%2BrRB7eTyjbliNWBCiij8joqVj0Whdkd4eBvCCrg24e0J%2BRNFJvJp%2FUWWrHo%2Fcg7UZPIQufniBsejmFuxxub0pyycR5Q8iAA%2BH8qRIpqER%2BAPORS2lY7nwc5ymPX7P4pLR072DcvxFIXEys11O3L71wve31acy5zWKa7qvqWlVXC7NBlP7Bhxpz3t99Ea%2BrZIb3nSkleEAD9ZU8aYew6WjEUkbVDZvDsp9G3SKX%2B6dqSSV9chNEkfs%2BB0XeJ2xzQOL9dhETuwvhfVzje4iiTNEbqsCJqcb31TuzMNrs7LwGOqUBqDXKwutA9aQeXWg1kfOu2z4pUindRh6Wl8oDQFS5npxRvMoZaJNDkVXdjtKio5%2FtMfkZQ0RJF4DKfbabgpJSSbGYeS7ZwT%2BPU1GNfheLs%2BSTrLzCHoDtDaVc%2Bf6qZ%2Bj%2Fa1CQSZ8eOMZX%2FCjbpTRAmvMxwpEQyHe4%2FOiSCzWhM8zC%2FGn%2F2VlNZhfOrVNrcK2FxHIHSrsdWgHzYmI9OYDhPEXY0xxp&X-Amz-Signature=f61626645d69cad613e76093407e7f7f09b70a6fa1e869ad488787a6755bd003&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y5T7CX3J%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCe%2B%2BG1%2Fmmrl2GlGDDAdC3lTbKDfiyX9nXGaPqZ24%2BlLgIgIy5u4eFMPFALuvdznmkUKZP6Yplt4D7FNF7AsNQRiNYqiAQIof%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHgbm7OIyPzeCVm1CyrcA%2FRGtJMGIGvujJZX1%2F%2B8Mo1j3l1rAbetv5caN9lVGtQZSqyKOJaNYAJx1j41K8gGFinC%2FyjhLZARObzV%2BuJaoUeExpuICYJYLgqk48VZkgM8%2FtN0gFkYQRLEPvnioRlMThLJY9z0PI97LZ%2B3hRpxrMkGSjjNWYwFWIfj89V%2FhJAmR3pmQvoLxMQFAMgRnRDW5siSdT9BtEB06cNmdEUJp4JWLRe3Dgo75lMyPSkKoDj1vTzP4MzcKOEDvz23XqVfAZk5o%2BoddrpYfCowsK%2BgZHNDnnngvgIjMQHwWLG7QCj0X%2Bii4yQmLiVTHxuXTwvrK8LvqWAuitnIHlvpki8iM4rnru%2BrRB7eTyjbliNWBCiij8joqVj0Whdkd4eBvCCrg24e0J%2BRNFJvJp%2FUWWrHo%2Fcg7UZPIQufniBsejmFuxxub0pyycR5Q8iAA%2BH8qRIpqER%2BAPORS2lY7nwc5ymPX7P4pLR072DcvxFIXEys11O3L71wve31acy5zWKa7qvqWlVXC7NBlP7Bhxpz3t99Ea%2BrZIb3nSkleEAD9ZU8aYew6WjEUkbVDZvDsp9G3SKX%2B6dqSSV9chNEkfs%2BB0XeJ2xzQOL9dhETuwvhfVzje4iiTNEbqsCJqcb31TuzMNrs7LwGOqUBqDXKwutA9aQeXWg1kfOu2z4pUindRh6Wl8oDQFS5npxRvMoZaJNDkVXdjtKio5%2FtMfkZQ0RJF4DKfbabgpJSSbGYeS7ZwT%2BPU1GNfheLs%2BSTrLzCHoDtDaVc%2Bf6qZ%2Bj%2Fa1CQSZ8eOMZX%2FCjbpTRAmvMxwpEQyHe4%2FOiSCzWhM8zC%2FGn%2F2VlNZhfOrVNrcK2FxHIHSrsdWgHzYmI9OYDhPEXY0xxp&X-Amz-Signature=62f11b5bcc5a61cf397bc00a2394850b6d6c215fbf3c6d97496f140c814ed388&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y5T7CX3J%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCe%2B%2BG1%2Fmmrl2GlGDDAdC3lTbKDfiyX9nXGaPqZ24%2BlLgIgIy5u4eFMPFALuvdznmkUKZP6Yplt4D7FNF7AsNQRiNYqiAQIof%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHgbm7OIyPzeCVm1CyrcA%2FRGtJMGIGvujJZX1%2F%2B8Mo1j3l1rAbetv5caN9lVGtQZSqyKOJaNYAJx1j41K8gGFinC%2FyjhLZARObzV%2BuJaoUeExpuICYJYLgqk48VZkgM8%2FtN0gFkYQRLEPvnioRlMThLJY9z0PI97LZ%2B3hRpxrMkGSjjNWYwFWIfj89V%2FhJAmR3pmQvoLxMQFAMgRnRDW5siSdT9BtEB06cNmdEUJp4JWLRe3Dgo75lMyPSkKoDj1vTzP4MzcKOEDvz23XqVfAZk5o%2BoddrpYfCowsK%2BgZHNDnnngvgIjMQHwWLG7QCj0X%2Bii4yQmLiVTHxuXTwvrK8LvqWAuitnIHlvpki8iM4rnru%2BrRB7eTyjbliNWBCiij8joqVj0Whdkd4eBvCCrg24e0J%2BRNFJvJp%2FUWWrHo%2Fcg7UZPIQufniBsejmFuxxub0pyycR5Q8iAA%2BH8qRIpqER%2BAPORS2lY7nwc5ymPX7P4pLR072DcvxFIXEys11O3L71wve31acy5zWKa7qvqWlVXC7NBlP7Bhxpz3t99Ea%2BrZIb3nSkleEAD9ZU8aYew6WjEUkbVDZvDsp9G3SKX%2B6dqSSV9chNEkfs%2BB0XeJ2xzQOL9dhETuwvhfVzje4iiTNEbqsCJqcb31TuzMNrs7LwGOqUBqDXKwutA9aQeXWg1kfOu2z4pUindRh6Wl8oDQFS5npxRvMoZaJNDkVXdjtKio5%2FtMfkZQ0RJF4DKfbabgpJSSbGYeS7ZwT%2BPU1GNfheLs%2BSTrLzCHoDtDaVc%2Bf6qZ%2Bj%2Fa1CQSZ8eOMZX%2FCjbpTRAmvMxwpEQyHe4%2FOiSCzWhM8zC%2FGn%2F2VlNZhfOrVNrcK2FxHIHSrsdWgHzYmI9OYDhPEXY0xxp&X-Amz-Signature=992e5e47e307de206eab7e31cf8647570574263e6b64c8db3ea3febc9e7e70d9&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y5T7CX3J%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCe%2B%2BG1%2Fmmrl2GlGDDAdC3lTbKDfiyX9nXGaPqZ24%2BlLgIgIy5u4eFMPFALuvdznmkUKZP6Yplt4D7FNF7AsNQRiNYqiAQIof%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHgbm7OIyPzeCVm1CyrcA%2FRGtJMGIGvujJZX1%2F%2B8Mo1j3l1rAbetv5caN9lVGtQZSqyKOJaNYAJx1j41K8gGFinC%2FyjhLZARObzV%2BuJaoUeExpuICYJYLgqk48VZkgM8%2FtN0gFkYQRLEPvnioRlMThLJY9z0PI97LZ%2B3hRpxrMkGSjjNWYwFWIfj89V%2FhJAmR3pmQvoLxMQFAMgRnRDW5siSdT9BtEB06cNmdEUJp4JWLRe3Dgo75lMyPSkKoDj1vTzP4MzcKOEDvz23XqVfAZk5o%2BoddrpYfCowsK%2BgZHNDnnngvgIjMQHwWLG7QCj0X%2Bii4yQmLiVTHxuXTwvrK8LvqWAuitnIHlvpki8iM4rnru%2BrRB7eTyjbliNWBCiij8joqVj0Whdkd4eBvCCrg24e0J%2BRNFJvJp%2FUWWrHo%2Fcg7UZPIQufniBsejmFuxxub0pyycR5Q8iAA%2BH8qRIpqER%2BAPORS2lY7nwc5ymPX7P4pLR072DcvxFIXEys11O3L71wve31acy5zWKa7qvqWlVXC7NBlP7Bhxpz3t99Ea%2BrZIb3nSkleEAD9ZU8aYew6WjEUkbVDZvDsp9G3SKX%2B6dqSSV9chNEkfs%2BB0XeJ2xzQOL9dhETuwvhfVzje4iiTNEbqsCJqcb31TuzMNrs7LwGOqUBqDXKwutA9aQeXWg1kfOu2z4pUindRh6Wl8oDQFS5npxRvMoZaJNDkVXdjtKio5%2FtMfkZQ0RJF4DKfbabgpJSSbGYeS7ZwT%2BPU1GNfheLs%2BSTrLzCHoDtDaVc%2Bf6qZ%2Bj%2Fa1CQSZ8eOMZX%2FCjbpTRAmvMxwpEQyHe4%2FOiSCzWhM8zC%2FGn%2F2VlNZhfOrVNrcK2FxHIHSrsdWgHzYmI9OYDhPEXY0xxp&X-Amz-Signature=573b3bd2fac201aab3a769b96b298693bb99d3ef90fa4ba38e24228b6888d521&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y5T7CX3J%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCe%2B%2BG1%2Fmmrl2GlGDDAdC3lTbKDfiyX9nXGaPqZ24%2BlLgIgIy5u4eFMPFALuvdznmkUKZP6Yplt4D7FNF7AsNQRiNYqiAQIof%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHgbm7OIyPzeCVm1CyrcA%2FRGtJMGIGvujJZX1%2F%2B8Mo1j3l1rAbetv5caN9lVGtQZSqyKOJaNYAJx1j41K8gGFinC%2FyjhLZARObzV%2BuJaoUeExpuICYJYLgqk48VZkgM8%2FtN0gFkYQRLEPvnioRlMThLJY9z0PI97LZ%2B3hRpxrMkGSjjNWYwFWIfj89V%2FhJAmR3pmQvoLxMQFAMgRnRDW5siSdT9BtEB06cNmdEUJp4JWLRe3Dgo75lMyPSkKoDj1vTzP4MzcKOEDvz23XqVfAZk5o%2BoddrpYfCowsK%2BgZHNDnnngvgIjMQHwWLG7QCj0X%2Bii4yQmLiVTHxuXTwvrK8LvqWAuitnIHlvpki8iM4rnru%2BrRB7eTyjbliNWBCiij8joqVj0Whdkd4eBvCCrg24e0J%2BRNFJvJp%2FUWWrHo%2Fcg7UZPIQufniBsejmFuxxub0pyycR5Q8iAA%2BH8qRIpqER%2BAPORS2lY7nwc5ymPX7P4pLR072DcvxFIXEys11O3L71wve31acy5zWKa7qvqWlVXC7NBlP7Bhxpz3t99Ea%2BrZIb3nSkleEAD9ZU8aYew6WjEUkbVDZvDsp9G3SKX%2B6dqSSV9chNEkfs%2BB0XeJ2xzQOL9dhETuwvhfVzje4iiTNEbqsCJqcb31TuzMNrs7LwGOqUBqDXKwutA9aQeXWg1kfOu2z4pUindRh6Wl8oDQFS5npxRvMoZaJNDkVXdjtKio5%2FtMfkZQ0RJF4DKfbabgpJSSbGYeS7ZwT%2BPU1GNfheLs%2BSTrLzCHoDtDaVc%2Bf6qZ%2Bj%2Fa1CQSZ8eOMZX%2FCjbpTRAmvMxwpEQyHe4%2FOiSCzWhM8zC%2FGn%2F2VlNZhfOrVNrcK2FxHIHSrsdWgHzYmI9OYDhPEXY0xxp&X-Amz-Signature=1b7e7fe40761d86fe97a0a85b6fd866f1419ca921be0c1b9c2e78dc3d01f89af&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y5T7CX3J%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCe%2B%2BG1%2Fmmrl2GlGDDAdC3lTbKDfiyX9nXGaPqZ24%2BlLgIgIy5u4eFMPFALuvdznmkUKZP6Yplt4D7FNF7AsNQRiNYqiAQIof%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHgbm7OIyPzeCVm1CyrcA%2FRGtJMGIGvujJZX1%2F%2B8Mo1j3l1rAbetv5caN9lVGtQZSqyKOJaNYAJx1j41K8gGFinC%2FyjhLZARObzV%2BuJaoUeExpuICYJYLgqk48VZkgM8%2FtN0gFkYQRLEPvnioRlMThLJY9z0PI97LZ%2B3hRpxrMkGSjjNWYwFWIfj89V%2FhJAmR3pmQvoLxMQFAMgRnRDW5siSdT9BtEB06cNmdEUJp4JWLRe3Dgo75lMyPSkKoDj1vTzP4MzcKOEDvz23XqVfAZk5o%2BoddrpYfCowsK%2BgZHNDnnngvgIjMQHwWLG7QCj0X%2Bii4yQmLiVTHxuXTwvrK8LvqWAuitnIHlvpki8iM4rnru%2BrRB7eTyjbliNWBCiij8joqVj0Whdkd4eBvCCrg24e0J%2BRNFJvJp%2FUWWrHo%2Fcg7UZPIQufniBsejmFuxxub0pyycR5Q8iAA%2BH8qRIpqER%2BAPORS2lY7nwc5ymPX7P4pLR072DcvxFIXEys11O3L71wve31acy5zWKa7qvqWlVXC7NBlP7Bhxpz3t99Ea%2BrZIb3nSkleEAD9ZU8aYew6WjEUkbVDZvDsp9G3SKX%2B6dqSSV9chNEkfs%2BB0XeJ2xzQOL9dhETuwvhfVzje4iiTNEbqsCJqcb31TuzMNrs7LwGOqUBqDXKwutA9aQeXWg1kfOu2z4pUindRh6Wl8oDQFS5npxRvMoZaJNDkVXdjtKio5%2FtMfkZQ0RJF4DKfbabgpJSSbGYeS7ZwT%2BPU1GNfheLs%2BSTrLzCHoDtDaVc%2Bf6qZ%2Bj%2Fa1CQSZ8eOMZX%2FCjbpTRAmvMxwpEQyHe4%2FOiSCzWhM8zC%2FGn%2F2VlNZhfOrVNrcK2FxHIHSrsdWgHzYmI9OYDhPEXY0xxp&X-Amz-Signature=e31939fbcb53cac39c264e9bd1fcc1d9c2e9b0be3379cf96e843f6474a8fc816&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TS5LOS52%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFVDlYwv61Q%2FL67DAJ2uVyKkNu2v6uct4G4oRjGXFdt8AiBFAYa87GkueMCedY6z2DQV93%2BKCeKkvbGngrt5FwXYQyqIBAih%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMipdHEqJCmceoYHZ7KtwDqm3%2FjtNM9WLOcexCCZaD7jqJ1FBsLYXcoPhIrFQ4Jhqr66R%2F3zdmiW3xT%2B16%2BjWIvKETSIDC0Hm%2FyHDzTq2afyRg4gxQ6vzc%2FSAFG5zEn2y4YxHnuavIQJs6a%2F0JH2pjFwe40v7SmyxhUrQF%2BmjWu3MIj1Io6%2Bys%2Ff0pplVaESHuAZ5ZySK3btuVflMPLaDzbkRLIbKOo1tg%2BCd5%2BDSRCLUBWp8k9PVhp%2FQsu2fit0riO08ZPp3ehnOepO4Lcpf53xY0wWfRFIm2XOf8R3642mLSFGFfKGBGgNty8zQZDPSoaFbX1Nze6fo2WszEc4eVCmIhy5vrKsNcEX3yNzO5%2FdrYyZB84cm7AjcVdmOguz7eKPukRixkkIDgLKLPAr4iF67yn85U%2Bk7pdAP4v%2FR0LZKoNxZIvtxwT4%2FL3bPTDgjvntV9T0aP0JigzmhyX9gnHJImnwoFr16fj74eR2SIIAuN0%2FXXEXC6wRrFEZXndjZZ0tZjgJx6U51viJFlcYCSD%2FcPfGULUO%2FzYs6jrIUtkkSpwtM9TO%2FUGHITVxlWbP9mz9LcWY7CcAuPo7ESZh7dM%2FaatP%2BHpqHaSFjl6ctKIF6xZdiyo6BXKtGuQf7Wb1ZOKhdFK%2B87DiNzhQow4OvsvAY6pgHKH08RJXGgNTtDNGjQjl6EQbFHdSJo%2FNPykXbjSUkqpoGbW2ylGNFaD4YjtXI9ysfUxguivgKRLcFEvVbpbCuOT%2BPu3MPQIc2YbnOHoaIykMfoZcNIzUPY9L4AqSJnLpep3JS4sL3C62e7tr1k%2FwcOtbPr2pqMJUlPnGJGPv7qQGIH2gFWh7DCIauDD45bmDPwWSuRYrkzKufR4eU58jV%2F%2BclTT5M5&X-Amz-Signature=0a58aae56516d46e7e84edf3a31ea214f2d22280cbccf9e1a9e56f99fc9a175a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TS5LOS52%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFVDlYwv61Q%2FL67DAJ2uVyKkNu2v6uct4G4oRjGXFdt8AiBFAYa87GkueMCedY6z2DQV93%2BKCeKkvbGngrt5FwXYQyqIBAih%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMipdHEqJCmceoYHZ7KtwDqm3%2FjtNM9WLOcexCCZaD7jqJ1FBsLYXcoPhIrFQ4Jhqr66R%2F3zdmiW3xT%2B16%2BjWIvKETSIDC0Hm%2FyHDzTq2afyRg4gxQ6vzc%2FSAFG5zEn2y4YxHnuavIQJs6a%2F0JH2pjFwe40v7SmyxhUrQF%2BmjWu3MIj1Io6%2Bys%2Ff0pplVaESHuAZ5ZySK3btuVflMPLaDzbkRLIbKOo1tg%2BCd5%2BDSRCLUBWp8k9PVhp%2FQsu2fit0riO08ZPp3ehnOepO4Lcpf53xY0wWfRFIm2XOf8R3642mLSFGFfKGBGgNty8zQZDPSoaFbX1Nze6fo2WszEc4eVCmIhy5vrKsNcEX3yNzO5%2FdrYyZB84cm7AjcVdmOguz7eKPukRixkkIDgLKLPAr4iF67yn85U%2Bk7pdAP4v%2FR0LZKoNxZIvtxwT4%2FL3bPTDgjvntV9T0aP0JigzmhyX9gnHJImnwoFr16fj74eR2SIIAuN0%2FXXEXC6wRrFEZXndjZZ0tZjgJx6U51viJFlcYCSD%2FcPfGULUO%2FzYs6jrIUtkkSpwtM9TO%2FUGHITVxlWbP9mz9LcWY7CcAuPo7ESZh7dM%2FaatP%2BHpqHaSFjl6ctKIF6xZdiyo6BXKtGuQf7Wb1ZOKhdFK%2B87DiNzhQow4OvsvAY6pgHKH08RJXGgNTtDNGjQjl6EQbFHdSJo%2FNPykXbjSUkqpoGbW2ylGNFaD4YjtXI9ysfUxguivgKRLcFEvVbpbCuOT%2BPu3MPQIc2YbnOHoaIykMfoZcNIzUPY9L4AqSJnLpep3JS4sL3C62e7tr1k%2FwcOtbPr2pqMJUlPnGJGPv7qQGIH2gFWh7DCIauDD45bmDPwWSuRYrkzKufR4eU58jV%2F%2BclTT5M5&X-Amz-Signature=5489ae09f712fcfa197617c94d7262f9ecda9a072c9ef64f6500057f89ccadc3&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
