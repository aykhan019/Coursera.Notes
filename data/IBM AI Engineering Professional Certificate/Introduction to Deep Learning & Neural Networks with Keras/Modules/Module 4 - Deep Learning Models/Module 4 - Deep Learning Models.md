

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZWGPKWF%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJHMEUCIQDIVTH3h3P2rDx1KzKyCiGiXbnhNTRwbBtUlwDlvQGIvQIgLMPcymhBGSDW2uMnJJgdw3NnxKUzgLTGoqyrUHVdYqAq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDM1Za%2BbcLy3OKhdQ7yrcA%2FznXTAfeXwCGJ9TZaSvSAa6PzHt1%2Fkk6qZtW4KT4zBMayNYQQQZ%2FUWgurhz0mAhqBFev6zkm6kPhpid%2BsKXo3hvITWNjjXirdRFekAQSiMBOa1QxlPSMscT0YQruTkIONauZ119HmuDzju6glNUIp%2BLPHEhHEuYEpzSeAbY%2FRDbvWNCD97sSdUZo4dGpaQoG90gzfmDrAFA4lIIzn6DcAsJ7yai1f5Hxalqi4KvEKzH4uO8Vn4HWHOERQmoK%2FtSZTP%2BsaNoBENreHijmfn58gTTj7R6KjxL4KWdotiC31Ll8pnli9Ua7uyK4dFRH4VPtM%2B5pjHoxdhAMUddRNQHdA2zcQCQBLzJGSbMQgrgk9ZMMPVhLZKHUFJSzTR8DhRKlt4fELfUrqwqOgTABmLt6n0X7bGDbu46lDU%2BvNiOsH99D4CwRpytelLwi%2FKVPocxEpZgaXT9%2B7rRqPbN1s8hVSrOhv%2Fip1eDwCjZKCGX7BUyuKOqUllasD7HrEJ2C5nY8BkpUqS5Qs53eCTLa2yY1QNKxUFT9A3U8sQILt%2ByHsX2h7DXTLr%2FVmkgvnFQAGZgn8FRnZEKul7TtKx0PfuHJm3p0oCpCkN3VnhcIKLN7C44bBcwuRfJJqJCWWUKMMHgmL0GOqUB%2BlDNRgBi90GIBQFlNXkZFeprT5yi2tMj8pr0ZkF3Qhlc9KdLGaRMcdt2EyRhEoaLj0qPb6M3hFjx%2Ft66V9O94AORohKc2hSWU6zUy5MGr6QGsb%2BQfYqAWRUEpME0Q2yPdDFI%2FoAfxbrpqIOdMNlC7ioxh7k1dLK5chvYFvKMoPegjwFn8M6O9cTyfccnOMJBLrLClv%2B9gfrdD0n7%2BQIaqX1qPbN0&X-Amz-Signature=0140ff0a388b5ff21ad0e0895f4b6481f27ab9f0690a7456ec947ea36c3c9fba&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZWGPKWF%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJHMEUCIQDIVTH3h3P2rDx1KzKyCiGiXbnhNTRwbBtUlwDlvQGIvQIgLMPcymhBGSDW2uMnJJgdw3NnxKUzgLTGoqyrUHVdYqAq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDM1Za%2BbcLy3OKhdQ7yrcA%2FznXTAfeXwCGJ9TZaSvSAa6PzHt1%2Fkk6qZtW4KT4zBMayNYQQQZ%2FUWgurhz0mAhqBFev6zkm6kPhpid%2BsKXo3hvITWNjjXirdRFekAQSiMBOa1QxlPSMscT0YQruTkIONauZ119HmuDzju6glNUIp%2BLPHEhHEuYEpzSeAbY%2FRDbvWNCD97sSdUZo4dGpaQoG90gzfmDrAFA4lIIzn6DcAsJ7yai1f5Hxalqi4KvEKzH4uO8Vn4HWHOERQmoK%2FtSZTP%2BsaNoBENreHijmfn58gTTj7R6KjxL4KWdotiC31Ll8pnli9Ua7uyK4dFRH4VPtM%2B5pjHoxdhAMUddRNQHdA2zcQCQBLzJGSbMQgrgk9ZMMPVhLZKHUFJSzTR8DhRKlt4fELfUrqwqOgTABmLt6n0X7bGDbu46lDU%2BvNiOsH99D4CwRpytelLwi%2FKVPocxEpZgaXT9%2B7rRqPbN1s8hVSrOhv%2Fip1eDwCjZKCGX7BUyuKOqUllasD7HrEJ2C5nY8BkpUqS5Qs53eCTLa2yY1QNKxUFT9A3U8sQILt%2ByHsX2h7DXTLr%2FVmkgvnFQAGZgn8FRnZEKul7TtKx0PfuHJm3p0oCpCkN3VnhcIKLN7C44bBcwuRfJJqJCWWUKMMHgmL0GOqUB%2BlDNRgBi90GIBQFlNXkZFeprT5yi2tMj8pr0ZkF3Qhlc9KdLGaRMcdt2EyRhEoaLj0qPb6M3hFjx%2Ft66V9O94AORohKc2hSWU6zUy5MGr6QGsb%2BQfYqAWRUEpME0Q2yPdDFI%2FoAfxbrpqIOdMNlC7ioxh7k1dLK5chvYFvKMoPegjwFn8M6O9cTyfccnOMJBLrLClv%2B9gfrdD0n7%2BQIaqX1qPbN0&X-Amz-Signature=87687be98752a83a750fc4a73646951ebd90e25bad5223d2d5d79fde05f04bba&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZWGPKWF%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJHMEUCIQDIVTH3h3P2rDx1KzKyCiGiXbnhNTRwbBtUlwDlvQGIvQIgLMPcymhBGSDW2uMnJJgdw3NnxKUzgLTGoqyrUHVdYqAq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDM1Za%2BbcLy3OKhdQ7yrcA%2FznXTAfeXwCGJ9TZaSvSAa6PzHt1%2Fkk6qZtW4KT4zBMayNYQQQZ%2FUWgurhz0mAhqBFev6zkm6kPhpid%2BsKXo3hvITWNjjXirdRFekAQSiMBOa1QxlPSMscT0YQruTkIONauZ119HmuDzju6glNUIp%2BLPHEhHEuYEpzSeAbY%2FRDbvWNCD97sSdUZo4dGpaQoG90gzfmDrAFA4lIIzn6DcAsJ7yai1f5Hxalqi4KvEKzH4uO8Vn4HWHOERQmoK%2FtSZTP%2BsaNoBENreHijmfn58gTTj7R6KjxL4KWdotiC31Ll8pnli9Ua7uyK4dFRH4VPtM%2B5pjHoxdhAMUddRNQHdA2zcQCQBLzJGSbMQgrgk9ZMMPVhLZKHUFJSzTR8DhRKlt4fELfUrqwqOgTABmLt6n0X7bGDbu46lDU%2BvNiOsH99D4CwRpytelLwi%2FKVPocxEpZgaXT9%2B7rRqPbN1s8hVSrOhv%2Fip1eDwCjZKCGX7BUyuKOqUllasD7HrEJ2C5nY8BkpUqS5Qs53eCTLa2yY1QNKxUFT9A3U8sQILt%2ByHsX2h7DXTLr%2FVmkgvnFQAGZgn8FRnZEKul7TtKx0PfuHJm3p0oCpCkN3VnhcIKLN7C44bBcwuRfJJqJCWWUKMMHgmL0GOqUB%2BlDNRgBi90GIBQFlNXkZFeprT5yi2tMj8pr0ZkF3Qhlc9KdLGaRMcdt2EyRhEoaLj0qPb6M3hFjx%2Ft66V9O94AORohKc2hSWU6zUy5MGr6QGsb%2BQfYqAWRUEpME0Q2yPdDFI%2FoAfxbrpqIOdMNlC7ioxh7k1dLK5chvYFvKMoPegjwFn8M6O9cTyfccnOMJBLrLClv%2B9gfrdD0n7%2BQIaqX1qPbN0&X-Amz-Signature=4298d58f82a7bb7161672bbeca73f57745a6aef9753822553c7e21f73aba3eef&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZWGPKWF%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJHMEUCIQDIVTH3h3P2rDx1KzKyCiGiXbnhNTRwbBtUlwDlvQGIvQIgLMPcymhBGSDW2uMnJJgdw3NnxKUzgLTGoqyrUHVdYqAq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDM1Za%2BbcLy3OKhdQ7yrcA%2FznXTAfeXwCGJ9TZaSvSAa6PzHt1%2Fkk6qZtW4KT4zBMayNYQQQZ%2FUWgurhz0mAhqBFev6zkm6kPhpid%2BsKXo3hvITWNjjXirdRFekAQSiMBOa1QxlPSMscT0YQruTkIONauZ119HmuDzju6glNUIp%2BLPHEhHEuYEpzSeAbY%2FRDbvWNCD97sSdUZo4dGpaQoG90gzfmDrAFA4lIIzn6DcAsJ7yai1f5Hxalqi4KvEKzH4uO8Vn4HWHOERQmoK%2FtSZTP%2BsaNoBENreHijmfn58gTTj7R6KjxL4KWdotiC31Ll8pnli9Ua7uyK4dFRH4VPtM%2B5pjHoxdhAMUddRNQHdA2zcQCQBLzJGSbMQgrgk9ZMMPVhLZKHUFJSzTR8DhRKlt4fELfUrqwqOgTABmLt6n0X7bGDbu46lDU%2BvNiOsH99D4CwRpytelLwi%2FKVPocxEpZgaXT9%2B7rRqPbN1s8hVSrOhv%2Fip1eDwCjZKCGX7BUyuKOqUllasD7HrEJ2C5nY8BkpUqS5Qs53eCTLa2yY1QNKxUFT9A3U8sQILt%2ByHsX2h7DXTLr%2FVmkgvnFQAGZgn8FRnZEKul7TtKx0PfuHJm3p0oCpCkN3VnhcIKLN7C44bBcwuRfJJqJCWWUKMMHgmL0GOqUB%2BlDNRgBi90GIBQFlNXkZFeprT5yi2tMj8pr0ZkF3Qhlc9KdLGaRMcdt2EyRhEoaLj0qPb6M3hFjx%2Ft66V9O94AORohKc2hSWU6zUy5MGr6QGsb%2BQfYqAWRUEpME0Q2yPdDFI%2FoAfxbrpqIOdMNlC7ioxh7k1dLK5chvYFvKMoPegjwFn8M6O9cTyfccnOMJBLrLClv%2B9gfrdD0n7%2BQIaqX1qPbN0&X-Amz-Signature=e98b7f4a72dfbe9e57cb3f7e11e3d7230961bee0aae459c9bab1e795f0a8219c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZWGPKWF%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJHMEUCIQDIVTH3h3P2rDx1KzKyCiGiXbnhNTRwbBtUlwDlvQGIvQIgLMPcymhBGSDW2uMnJJgdw3NnxKUzgLTGoqyrUHVdYqAq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDM1Za%2BbcLy3OKhdQ7yrcA%2FznXTAfeXwCGJ9TZaSvSAa6PzHt1%2Fkk6qZtW4KT4zBMayNYQQQZ%2FUWgurhz0mAhqBFev6zkm6kPhpid%2BsKXo3hvITWNjjXirdRFekAQSiMBOa1QxlPSMscT0YQruTkIONauZ119HmuDzju6glNUIp%2BLPHEhHEuYEpzSeAbY%2FRDbvWNCD97sSdUZo4dGpaQoG90gzfmDrAFA4lIIzn6DcAsJ7yai1f5Hxalqi4KvEKzH4uO8Vn4HWHOERQmoK%2FtSZTP%2BsaNoBENreHijmfn58gTTj7R6KjxL4KWdotiC31Ll8pnli9Ua7uyK4dFRH4VPtM%2B5pjHoxdhAMUddRNQHdA2zcQCQBLzJGSbMQgrgk9ZMMPVhLZKHUFJSzTR8DhRKlt4fELfUrqwqOgTABmLt6n0X7bGDbu46lDU%2BvNiOsH99D4CwRpytelLwi%2FKVPocxEpZgaXT9%2B7rRqPbN1s8hVSrOhv%2Fip1eDwCjZKCGX7BUyuKOqUllasD7HrEJ2C5nY8BkpUqS5Qs53eCTLa2yY1QNKxUFT9A3U8sQILt%2ByHsX2h7DXTLr%2FVmkgvnFQAGZgn8FRnZEKul7TtKx0PfuHJm3p0oCpCkN3VnhcIKLN7C44bBcwuRfJJqJCWWUKMMHgmL0GOqUB%2BlDNRgBi90GIBQFlNXkZFeprT5yi2tMj8pr0ZkF3Qhlc9KdLGaRMcdt2EyRhEoaLj0qPb6M3hFjx%2Ft66V9O94AORohKc2hSWU6zUy5MGr6QGsb%2BQfYqAWRUEpME0Q2yPdDFI%2FoAfxbrpqIOdMNlC7ioxh7k1dLK5chvYFvKMoPegjwFn8M6O9cTyfccnOMJBLrLClv%2B9gfrdD0n7%2BQIaqX1qPbN0&X-Amz-Signature=b43e14e2ab4ef1bbaa16db7c24eaefdf523e6054457e205a5be3e271245d76b7&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZWGPKWF%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJHMEUCIQDIVTH3h3P2rDx1KzKyCiGiXbnhNTRwbBtUlwDlvQGIvQIgLMPcymhBGSDW2uMnJJgdw3NnxKUzgLTGoqyrUHVdYqAq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDM1Za%2BbcLy3OKhdQ7yrcA%2FznXTAfeXwCGJ9TZaSvSAa6PzHt1%2Fkk6qZtW4KT4zBMayNYQQQZ%2FUWgurhz0mAhqBFev6zkm6kPhpid%2BsKXo3hvITWNjjXirdRFekAQSiMBOa1QxlPSMscT0YQruTkIONauZ119HmuDzju6glNUIp%2BLPHEhHEuYEpzSeAbY%2FRDbvWNCD97sSdUZo4dGpaQoG90gzfmDrAFA4lIIzn6DcAsJ7yai1f5Hxalqi4KvEKzH4uO8Vn4HWHOERQmoK%2FtSZTP%2BsaNoBENreHijmfn58gTTj7R6KjxL4KWdotiC31Ll8pnli9Ua7uyK4dFRH4VPtM%2B5pjHoxdhAMUddRNQHdA2zcQCQBLzJGSbMQgrgk9ZMMPVhLZKHUFJSzTR8DhRKlt4fELfUrqwqOgTABmLt6n0X7bGDbu46lDU%2BvNiOsH99D4CwRpytelLwi%2FKVPocxEpZgaXT9%2B7rRqPbN1s8hVSrOhv%2Fip1eDwCjZKCGX7BUyuKOqUllasD7HrEJ2C5nY8BkpUqS5Qs53eCTLa2yY1QNKxUFT9A3U8sQILt%2ByHsX2h7DXTLr%2FVmkgvnFQAGZgn8FRnZEKul7TtKx0PfuHJm3p0oCpCkN3VnhcIKLN7C44bBcwuRfJJqJCWWUKMMHgmL0GOqUB%2BlDNRgBi90GIBQFlNXkZFeprT5yi2tMj8pr0ZkF3Qhlc9KdLGaRMcdt2EyRhEoaLj0qPb6M3hFjx%2Ft66V9O94AORohKc2hSWU6zUy5MGr6QGsb%2BQfYqAWRUEpME0Q2yPdDFI%2FoAfxbrpqIOdMNlC7ioxh7k1dLK5chvYFvKMoPegjwFn8M6O9cTyfccnOMJBLrLClv%2B9gfrdD0n7%2BQIaqX1qPbN0&X-Amz-Signature=76679c73857451df4cd1b7f4092ae544f67d768e2c505e11368e0f15370331d3&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZWGPKWF%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJHMEUCIQDIVTH3h3P2rDx1KzKyCiGiXbnhNTRwbBtUlwDlvQGIvQIgLMPcymhBGSDW2uMnJJgdw3NnxKUzgLTGoqyrUHVdYqAq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDM1Za%2BbcLy3OKhdQ7yrcA%2FznXTAfeXwCGJ9TZaSvSAa6PzHt1%2Fkk6qZtW4KT4zBMayNYQQQZ%2FUWgurhz0mAhqBFev6zkm6kPhpid%2BsKXo3hvITWNjjXirdRFekAQSiMBOa1QxlPSMscT0YQruTkIONauZ119HmuDzju6glNUIp%2BLPHEhHEuYEpzSeAbY%2FRDbvWNCD97sSdUZo4dGpaQoG90gzfmDrAFA4lIIzn6DcAsJ7yai1f5Hxalqi4KvEKzH4uO8Vn4HWHOERQmoK%2FtSZTP%2BsaNoBENreHijmfn58gTTj7R6KjxL4KWdotiC31Ll8pnli9Ua7uyK4dFRH4VPtM%2B5pjHoxdhAMUddRNQHdA2zcQCQBLzJGSbMQgrgk9ZMMPVhLZKHUFJSzTR8DhRKlt4fELfUrqwqOgTABmLt6n0X7bGDbu46lDU%2BvNiOsH99D4CwRpytelLwi%2FKVPocxEpZgaXT9%2B7rRqPbN1s8hVSrOhv%2Fip1eDwCjZKCGX7BUyuKOqUllasD7HrEJ2C5nY8BkpUqS5Qs53eCTLa2yY1QNKxUFT9A3U8sQILt%2ByHsX2h7DXTLr%2FVmkgvnFQAGZgn8FRnZEKul7TtKx0PfuHJm3p0oCpCkN3VnhcIKLN7C44bBcwuRfJJqJCWWUKMMHgmL0GOqUB%2BlDNRgBi90GIBQFlNXkZFeprT5yi2tMj8pr0ZkF3Qhlc9KdLGaRMcdt2EyRhEoaLj0qPb6M3hFjx%2Ft66V9O94AORohKc2hSWU6zUy5MGr6QGsb%2BQfYqAWRUEpME0Q2yPdDFI%2FoAfxbrpqIOdMNlC7ioxh7k1dLK5chvYFvKMoPegjwFn8M6O9cTyfccnOMJBLrLClv%2B9gfrdD0n7%2BQIaqX1qPbN0&X-Amz-Signature=45a73dda4206a2ad9132f7ef10ac2da41dc7af72afca2762cf65f6801b5fd478&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZWGPKWF%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJHMEUCIQDIVTH3h3P2rDx1KzKyCiGiXbnhNTRwbBtUlwDlvQGIvQIgLMPcymhBGSDW2uMnJJgdw3NnxKUzgLTGoqyrUHVdYqAq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDM1Za%2BbcLy3OKhdQ7yrcA%2FznXTAfeXwCGJ9TZaSvSAa6PzHt1%2Fkk6qZtW4KT4zBMayNYQQQZ%2FUWgurhz0mAhqBFev6zkm6kPhpid%2BsKXo3hvITWNjjXirdRFekAQSiMBOa1QxlPSMscT0YQruTkIONauZ119HmuDzju6glNUIp%2BLPHEhHEuYEpzSeAbY%2FRDbvWNCD97sSdUZo4dGpaQoG90gzfmDrAFA4lIIzn6DcAsJ7yai1f5Hxalqi4KvEKzH4uO8Vn4HWHOERQmoK%2FtSZTP%2BsaNoBENreHijmfn58gTTj7R6KjxL4KWdotiC31Ll8pnli9Ua7uyK4dFRH4VPtM%2B5pjHoxdhAMUddRNQHdA2zcQCQBLzJGSbMQgrgk9ZMMPVhLZKHUFJSzTR8DhRKlt4fELfUrqwqOgTABmLt6n0X7bGDbu46lDU%2BvNiOsH99D4CwRpytelLwi%2FKVPocxEpZgaXT9%2B7rRqPbN1s8hVSrOhv%2Fip1eDwCjZKCGX7BUyuKOqUllasD7HrEJ2C5nY8BkpUqS5Qs53eCTLa2yY1QNKxUFT9A3U8sQILt%2ByHsX2h7DXTLr%2FVmkgvnFQAGZgn8FRnZEKul7TtKx0PfuHJm3p0oCpCkN3VnhcIKLN7C44bBcwuRfJJqJCWWUKMMHgmL0GOqUB%2BlDNRgBi90GIBQFlNXkZFeprT5yi2tMj8pr0ZkF3Qhlc9KdLGaRMcdt2EyRhEoaLj0qPb6M3hFjx%2Ft66V9O94AORohKc2hSWU6zUy5MGr6QGsb%2BQfYqAWRUEpME0Q2yPdDFI%2FoAfxbrpqIOdMNlC7ioxh7k1dLK5chvYFvKMoPegjwFn8M6O9cTyfccnOMJBLrLClv%2B9gfrdD0n7%2BQIaqX1qPbN0&X-Amz-Signature=756a2e2499c977b36818ce6d6bba2efe467944629e363825b3f6cecd1e5e8db7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZWGPKWF%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJHMEUCIQDIVTH3h3P2rDx1KzKyCiGiXbnhNTRwbBtUlwDlvQGIvQIgLMPcymhBGSDW2uMnJJgdw3NnxKUzgLTGoqyrUHVdYqAq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDM1Za%2BbcLy3OKhdQ7yrcA%2FznXTAfeXwCGJ9TZaSvSAa6PzHt1%2Fkk6qZtW4KT4zBMayNYQQQZ%2FUWgurhz0mAhqBFev6zkm6kPhpid%2BsKXo3hvITWNjjXirdRFekAQSiMBOa1QxlPSMscT0YQruTkIONauZ119HmuDzju6glNUIp%2BLPHEhHEuYEpzSeAbY%2FRDbvWNCD97sSdUZo4dGpaQoG90gzfmDrAFA4lIIzn6DcAsJ7yai1f5Hxalqi4KvEKzH4uO8Vn4HWHOERQmoK%2FtSZTP%2BsaNoBENreHijmfn58gTTj7R6KjxL4KWdotiC31Ll8pnli9Ua7uyK4dFRH4VPtM%2B5pjHoxdhAMUddRNQHdA2zcQCQBLzJGSbMQgrgk9ZMMPVhLZKHUFJSzTR8DhRKlt4fELfUrqwqOgTABmLt6n0X7bGDbu46lDU%2BvNiOsH99D4CwRpytelLwi%2FKVPocxEpZgaXT9%2B7rRqPbN1s8hVSrOhv%2Fip1eDwCjZKCGX7BUyuKOqUllasD7HrEJ2C5nY8BkpUqS5Qs53eCTLa2yY1QNKxUFT9A3U8sQILt%2ByHsX2h7DXTLr%2FVmkgvnFQAGZgn8FRnZEKul7TtKx0PfuHJm3p0oCpCkN3VnhcIKLN7C44bBcwuRfJJqJCWWUKMMHgmL0GOqUB%2BlDNRgBi90GIBQFlNXkZFeprT5yi2tMj8pr0ZkF3Qhlc9KdLGaRMcdt2EyRhEoaLj0qPb6M3hFjx%2Ft66V9O94AORohKc2hSWU6zUy5MGr6QGsb%2BQfYqAWRUEpME0Q2yPdDFI%2FoAfxbrpqIOdMNlC7ioxh7k1dLK5chvYFvKMoPegjwFn8M6O9cTyfccnOMJBLrLClv%2B9gfrdD0n7%2BQIaqX1qPbN0&X-Amz-Signature=78e9a17a440d8656d2e6d9983c6463de1b29a9861770da9f1745c7f42aba6e0b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664EZA7QZX%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJHMEUCIQDrCffQ6Y5r4O97GS%2Fenfc2aE9Q1%2BKbl57TXwG%2F1VLqigIgT65Ee6McLWVpSm9MWmbIZMILtLE%2FYOQqeoyKVidU660q%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDG7%2BRWjuGNUg0U97sSrcA0I5E%2FwOL7UrsZ0HVlOhsG9QhRRRQy1gTaQ6mJTR7M2XQvyDfcS8sRxIXp0KHQLr7Q86sqCy6jCViQmNfunAdwDqk0yBrejSaV7UInfeyfAxuIJBVatiTEdR0QF50mH5FJhwMLi%2BsmmDRHc6Oca23iDjYa%2BAW7r5kaj2ld5PmaOcwd6sBZZe%2B2w0YB0OohlCVCDc2%2BWrCUm1XjD6Ilqh8LhGSgNtBadsXC0%2Bixyq2DqZq0GBPH70VF6eF6QFlIiY0OWBH%2FJ9uSEagAyPwW7B2pFEDgb%2BARcbHUbLQQEk1Cwrh7YIXcaYCR44pS6k37y4AzA3p21TgMXiKKOvJML4rQQBw1xdjEIlABADkx%2F9MenyrwAjCNtQ8UlaVJyaKSf5t508HnLj4ZNnBX8axiGHkjiGZtzCU4AY2G4j2SjK0%2BtAzCb0sptGYo6h7aqDOQ3I4LH0BvPhVBkCnA6NllKAY8gPgiBvscN%2Fj7OZA1vq%2FfdQvShnBXsCd2eOcupUgQD4tc1bIJGeMvIDxqGbPz6iaHtAwgq6UfklXYJoOCBgOFRyYtT%2FNzwueftG49ZNcfTUnoTXHSd%2F4pqDIUhoJp7RewRymX0SWYsdjqu%2FH8%2BYLK8%2BlRti63vuFN1nOA2dMK%2FgmL0GOqUB54yHmnVYhIU0OjmYMJeTk3zHf0%2FUAVujFhK9iQihOxL0edQRhPaI4nFAgBxGlUsw9Z4WiydlFGhxALpKrqRBi8hPEmDCBt3EHGouO5vCQkxPrziETgB0C%2BywnEjCGcQfq%2BZT1g062tUTkfQqb9DdGB5Pit3bacUwBt%2FaGM4mLghhgfU2yHqgztSMwdWgStW9xQxZFs1FNDxKec5LTarjpPySZLG3&X-Amz-Signature=29ae2749de2e6ae6bf695a534a7d0b364418e2688917c0ed9fa0be86ac1a012c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664EZA7QZX%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJHMEUCIQDrCffQ6Y5r4O97GS%2Fenfc2aE9Q1%2BKbl57TXwG%2F1VLqigIgT65Ee6McLWVpSm9MWmbIZMILtLE%2FYOQqeoyKVidU660q%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDG7%2BRWjuGNUg0U97sSrcA0I5E%2FwOL7UrsZ0HVlOhsG9QhRRRQy1gTaQ6mJTR7M2XQvyDfcS8sRxIXp0KHQLr7Q86sqCy6jCViQmNfunAdwDqk0yBrejSaV7UInfeyfAxuIJBVatiTEdR0QF50mH5FJhwMLi%2BsmmDRHc6Oca23iDjYa%2BAW7r5kaj2ld5PmaOcwd6sBZZe%2B2w0YB0OohlCVCDc2%2BWrCUm1XjD6Ilqh8LhGSgNtBadsXC0%2Bixyq2DqZq0GBPH70VF6eF6QFlIiY0OWBH%2FJ9uSEagAyPwW7B2pFEDgb%2BARcbHUbLQQEk1Cwrh7YIXcaYCR44pS6k37y4AzA3p21TgMXiKKOvJML4rQQBw1xdjEIlABADkx%2F9MenyrwAjCNtQ8UlaVJyaKSf5t508HnLj4ZNnBX8axiGHkjiGZtzCU4AY2G4j2SjK0%2BtAzCb0sptGYo6h7aqDOQ3I4LH0BvPhVBkCnA6NllKAY8gPgiBvscN%2Fj7OZA1vq%2FfdQvShnBXsCd2eOcupUgQD4tc1bIJGeMvIDxqGbPz6iaHtAwgq6UfklXYJoOCBgOFRyYtT%2FNzwueftG49ZNcfTUnoTXHSd%2F4pqDIUhoJp7RewRymX0SWYsdjqu%2FH8%2BYLK8%2BlRti63vuFN1nOA2dMK%2FgmL0GOqUB54yHmnVYhIU0OjmYMJeTk3zHf0%2FUAVujFhK9iQihOxL0edQRhPaI4nFAgBxGlUsw9Z4WiydlFGhxALpKrqRBi8hPEmDCBt3EHGouO5vCQkxPrziETgB0C%2BywnEjCGcQfq%2BZT1g062tUTkfQqb9DdGB5Pit3bacUwBt%2FaGM4mLghhgfU2yHqgztSMwdWgStW9xQxZFs1FNDxKec5LTarjpPySZLG3&X-Amz-Signature=c05665bb6591f740bbb4831b09562c7f7af3049b61aaf1fc66da1b9b64852194&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
