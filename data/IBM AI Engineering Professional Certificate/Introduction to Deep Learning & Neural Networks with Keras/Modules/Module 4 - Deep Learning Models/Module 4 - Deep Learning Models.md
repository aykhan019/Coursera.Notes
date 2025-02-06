

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJQHQ37X%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIDPA5SIBs2%2BbXO5E%2F3mQFkLlnpTkkWyVOjf%2Bin%2BNXNc%2FAiBn12sYkkDA57CpHHntSbS39Kt5HF4osvmAieNO4A0gFSr%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIMXbR7BxbiJXxrSC2qKtwD%2F8Uiui7D7NDVDm8nR1ldvF45fqjhYut7q84KCNnXRifdtj6iI2i2fF9a4ET0ulINm1Ue1HgRhz6sTLFWCPMEq2GHH%2FwNyNjbc74XNhE%2BAcf4FHLbO31i793mlQv6ZfvQb%2BoHGJV5J7w7aNAris%2ByvETiFnk0hD0sEgjBFAfRYn0qFlmfhmB0kjKMLTtX2CbG%2F%2BHjebpwd5kMEusJbxc8uSY41Js8gIeZBI9CXRHe3L7zCJ09kWC2JQYqp2t0yZDaNqXJPxd0Bt2QZQPjfprzHGnSam3QlIVBgatiS9XwLyWpXXJ5vvi9ghpHs6LbhqxRrxRgPf3VoYYehLx4DnJQAdgCn4aZ9R38bXdkO9AyUmwcEPm40mM0cfD8FKLbobI%2BKe9ZUXwp%2F1ycMhH4AOkTn%2BJeopnb1JXCNGrzaMEfNehbiIGGzamqGpCe7JihmV6FAbK5Xo8lH92XmOKxNJlPobHPPWlLNcmrW%2ByUdbY%2B%2BLpGnyIbqDkzfoSXUM%2BttXRo2suGgNrBUfxREN7%2BIebipJPIs7gzTReUX8L5aGTgbRV8Uve5Ddq88MQP6psEOesBWpsltsO0FABZlZMFx06v2dCaIF7jmmlqKiyi1TQuD03OVqCu0BVDqZUlBekw0%2FuTvQY6pgF0ANmMujA2Vomg9XbYt1inQMaGQOs1kX4yLmy8uN2Aqgbh3PWzXNID7BBv0y9p%2BjLvG1XI5efeIhnn%2BaiejqKYpQxMXDKTszlNETaRP8AEBLrsSj8m2U%2FcLZw4rMBPqAyaX0jYY1%2B7pYfegm%2B3Q6Hazwfdhmd21I6G9X8I%2BzABj4KrNMghs69whcei2QjJr2BkhHhdIrC%2BRMX%2BzNjFFj740KRYSigt&X-Amz-Signature=7398b0118f3c0ba22ab1490d9f3ca55da6fdf5c2fdc4a12ed170c71dc602ab32&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJQHQ37X%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIDPA5SIBs2%2BbXO5E%2F3mQFkLlnpTkkWyVOjf%2Bin%2BNXNc%2FAiBn12sYkkDA57CpHHntSbS39Kt5HF4osvmAieNO4A0gFSr%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIMXbR7BxbiJXxrSC2qKtwD%2F8Uiui7D7NDVDm8nR1ldvF45fqjhYut7q84KCNnXRifdtj6iI2i2fF9a4ET0ulINm1Ue1HgRhz6sTLFWCPMEq2GHH%2FwNyNjbc74XNhE%2BAcf4FHLbO31i793mlQv6ZfvQb%2BoHGJV5J7w7aNAris%2ByvETiFnk0hD0sEgjBFAfRYn0qFlmfhmB0kjKMLTtX2CbG%2F%2BHjebpwd5kMEusJbxc8uSY41Js8gIeZBI9CXRHe3L7zCJ09kWC2JQYqp2t0yZDaNqXJPxd0Bt2QZQPjfprzHGnSam3QlIVBgatiS9XwLyWpXXJ5vvi9ghpHs6LbhqxRrxRgPf3VoYYehLx4DnJQAdgCn4aZ9R38bXdkO9AyUmwcEPm40mM0cfD8FKLbobI%2BKe9ZUXwp%2F1ycMhH4AOkTn%2BJeopnb1JXCNGrzaMEfNehbiIGGzamqGpCe7JihmV6FAbK5Xo8lH92XmOKxNJlPobHPPWlLNcmrW%2ByUdbY%2B%2BLpGnyIbqDkzfoSXUM%2BttXRo2suGgNrBUfxREN7%2BIebipJPIs7gzTReUX8L5aGTgbRV8Uve5Ddq88MQP6psEOesBWpsltsO0FABZlZMFx06v2dCaIF7jmmlqKiyi1TQuD03OVqCu0BVDqZUlBekw0%2FuTvQY6pgF0ANmMujA2Vomg9XbYt1inQMaGQOs1kX4yLmy8uN2Aqgbh3PWzXNID7BBv0y9p%2BjLvG1XI5efeIhnn%2BaiejqKYpQxMXDKTszlNETaRP8AEBLrsSj8m2U%2FcLZw4rMBPqAyaX0jYY1%2B7pYfegm%2B3Q6Hazwfdhmd21I6G9X8I%2BzABj4KrNMghs69whcei2QjJr2BkhHhdIrC%2BRMX%2BzNjFFj740KRYSigt&X-Amz-Signature=3c0be3ac120cc88957b6db17a739b621b936347b7965082b15d5e9587af11007&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJQHQ37X%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIDPA5SIBs2%2BbXO5E%2F3mQFkLlnpTkkWyVOjf%2Bin%2BNXNc%2FAiBn12sYkkDA57CpHHntSbS39Kt5HF4osvmAieNO4A0gFSr%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIMXbR7BxbiJXxrSC2qKtwD%2F8Uiui7D7NDVDm8nR1ldvF45fqjhYut7q84KCNnXRifdtj6iI2i2fF9a4ET0ulINm1Ue1HgRhz6sTLFWCPMEq2GHH%2FwNyNjbc74XNhE%2BAcf4FHLbO31i793mlQv6ZfvQb%2BoHGJV5J7w7aNAris%2ByvETiFnk0hD0sEgjBFAfRYn0qFlmfhmB0kjKMLTtX2CbG%2F%2BHjebpwd5kMEusJbxc8uSY41Js8gIeZBI9CXRHe3L7zCJ09kWC2JQYqp2t0yZDaNqXJPxd0Bt2QZQPjfprzHGnSam3QlIVBgatiS9XwLyWpXXJ5vvi9ghpHs6LbhqxRrxRgPf3VoYYehLx4DnJQAdgCn4aZ9R38bXdkO9AyUmwcEPm40mM0cfD8FKLbobI%2BKe9ZUXwp%2F1ycMhH4AOkTn%2BJeopnb1JXCNGrzaMEfNehbiIGGzamqGpCe7JihmV6FAbK5Xo8lH92XmOKxNJlPobHPPWlLNcmrW%2ByUdbY%2B%2BLpGnyIbqDkzfoSXUM%2BttXRo2suGgNrBUfxREN7%2BIebipJPIs7gzTReUX8L5aGTgbRV8Uve5Ddq88MQP6psEOesBWpsltsO0FABZlZMFx06v2dCaIF7jmmlqKiyi1TQuD03OVqCu0BVDqZUlBekw0%2FuTvQY6pgF0ANmMujA2Vomg9XbYt1inQMaGQOs1kX4yLmy8uN2Aqgbh3PWzXNID7BBv0y9p%2BjLvG1XI5efeIhnn%2BaiejqKYpQxMXDKTszlNETaRP8AEBLrsSj8m2U%2FcLZw4rMBPqAyaX0jYY1%2B7pYfegm%2B3Q6Hazwfdhmd21I6G9X8I%2BzABj4KrNMghs69whcei2QjJr2BkhHhdIrC%2BRMX%2BzNjFFj740KRYSigt&X-Amz-Signature=b11540dc2fa9c0d5c95830ff8196214b98d36b6cc9fda40c50fe5baa675e9551&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJQHQ37X%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIDPA5SIBs2%2BbXO5E%2F3mQFkLlnpTkkWyVOjf%2Bin%2BNXNc%2FAiBn12sYkkDA57CpHHntSbS39Kt5HF4osvmAieNO4A0gFSr%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIMXbR7BxbiJXxrSC2qKtwD%2F8Uiui7D7NDVDm8nR1ldvF45fqjhYut7q84KCNnXRifdtj6iI2i2fF9a4ET0ulINm1Ue1HgRhz6sTLFWCPMEq2GHH%2FwNyNjbc74XNhE%2BAcf4FHLbO31i793mlQv6ZfvQb%2BoHGJV5J7w7aNAris%2ByvETiFnk0hD0sEgjBFAfRYn0qFlmfhmB0kjKMLTtX2CbG%2F%2BHjebpwd5kMEusJbxc8uSY41Js8gIeZBI9CXRHe3L7zCJ09kWC2JQYqp2t0yZDaNqXJPxd0Bt2QZQPjfprzHGnSam3QlIVBgatiS9XwLyWpXXJ5vvi9ghpHs6LbhqxRrxRgPf3VoYYehLx4DnJQAdgCn4aZ9R38bXdkO9AyUmwcEPm40mM0cfD8FKLbobI%2BKe9ZUXwp%2F1ycMhH4AOkTn%2BJeopnb1JXCNGrzaMEfNehbiIGGzamqGpCe7JihmV6FAbK5Xo8lH92XmOKxNJlPobHPPWlLNcmrW%2ByUdbY%2B%2BLpGnyIbqDkzfoSXUM%2BttXRo2suGgNrBUfxREN7%2BIebipJPIs7gzTReUX8L5aGTgbRV8Uve5Ddq88MQP6psEOesBWpsltsO0FABZlZMFx06v2dCaIF7jmmlqKiyi1TQuD03OVqCu0BVDqZUlBekw0%2FuTvQY6pgF0ANmMujA2Vomg9XbYt1inQMaGQOs1kX4yLmy8uN2Aqgbh3PWzXNID7BBv0y9p%2BjLvG1XI5efeIhnn%2BaiejqKYpQxMXDKTszlNETaRP8AEBLrsSj8m2U%2FcLZw4rMBPqAyaX0jYY1%2B7pYfegm%2B3Q6Hazwfdhmd21I6G9X8I%2BzABj4KrNMghs69whcei2QjJr2BkhHhdIrC%2BRMX%2BzNjFFj740KRYSigt&X-Amz-Signature=beb9cd02ba3092cf2dbb72ba811ca3e06e01e83a06e3589701681c5dacbacf31&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJQHQ37X%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIDPA5SIBs2%2BbXO5E%2F3mQFkLlnpTkkWyVOjf%2Bin%2BNXNc%2FAiBn12sYkkDA57CpHHntSbS39Kt5HF4osvmAieNO4A0gFSr%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIMXbR7BxbiJXxrSC2qKtwD%2F8Uiui7D7NDVDm8nR1ldvF45fqjhYut7q84KCNnXRifdtj6iI2i2fF9a4ET0ulINm1Ue1HgRhz6sTLFWCPMEq2GHH%2FwNyNjbc74XNhE%2BAcf4FHLbO31i793mlQv6ZfvQb%2BoHGJV5J7w7aNAris%2ByvETiFnk0hD0sEgjBFAfRYn0qFlmfhmB0kjKMLTtX2CbG%2F%2BHjebpwd5kMEusJbxc8uSY41Js8gIeZBI9CXRHe3L7zCJ09kWC2JQYqp2t0yZDaNqXJPxd0Bt2QZQPjfprzHGnSam3QlIVBgatiS9XwLyWpXXJ5vvi9ghpHs6LbhqxRrxRgPf3VoYYehLx4DnJQAdgCn4aZ9R38bXdkO9AyUmwcEPm40mM0cfD8FKLbobI%2BKe9ZUXwp%2F1ycMhH4AOkTn%2BJeopnb1JXCNGrzaMEfNehbiIGGzamqGpCe7JihmV6FAbK5Xo8lH92XmOKxNJlPobHPPWlLNcmrW%2ByUdbY%2B%2BLpGnyIbqDkzfoSXUM%2BttXRo2suGgNrBUfxREN7%2BIebipJPIs7gzTReUX8L5aGTgbRV8Uve5Ddq88MQP6psEOesBWpsltsO0FABZlZMFx06v2dCaIF7jmmlqKiyi1TQuD03OVqCu0BVDqZUlBekw0%2FuTvQY6pgF0ANmMujA2Vomg9XbYt1inQMaGQOs1kX4yLmy8uN2Aqgbh3PWzXNID7BBv0y9p%2BjLvG1XI5efeIhnn%2BaiejqKYpQxMXDKTszlNETaRP8AEBLrsSj8m2U%2FcLZw4rMBPqAyaX0jYY1%2B7pYfegm%2B3Q6Hazwfdhmd21I6G9X8I%2BzABj4KrNMghs69whcei2QjJr2BkhHhdIrC%2BRMX%2BzNjFFj740KRYSigt&X-Amz-Signature=48eeeddd8552fd35723f6731ac5ab8eb381ee74ee8d958e606c774d55622fb1f&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJQHQ37X%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIDPA5SIBs2%2BbXO5E%2F3mQFkLlnpTkkWyVOjf%2Bin%2BNXNc%2FAiBn12sYkkDA57CpHHntSbS39Kt5HF4osvmAieNO4A0gFSr%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIMXbR7BxbiJXxrSC2qKtwD%2F8Uiui7D7NDVDm8nR1ldvF45fqjhYut7q84KCNnXRifdtj6iI2i2fF9a4ET0ulINm1Ue1HgRhz6sTLFWCPMEq2GHH%2FwNyNjbc74XNhE%2BAcf4FHLbO31i793mlQv6ZfvQb%2BoHGJV5J7w7aNAris%2ByvETiFnk0hD0sEgjBFAfRYn0qFlmfhmB0kjKMLTtX2CbG%2F%2BHjebpwd5kMEusJbxc8uSY41Js8gIeZBI9CXRHe3L7zCJ09kWC2JQYqp2t0yZDaNqXJPxd0Bt2QZQPjfprzHGnSam3QlIVBgatiS9XwLyWpXXJ5vvi9ghpHs6LbhqxRrxRgPf3VoYYehLx4DnJQAdgCn4aZ9R38bXdkO9AyUmwcEPm40mM0cfD8FKLbobI%2BKe9ZUXwp%2F1ycMhH4AOkTn%2BJeopnb1JXCNGrzaMEfNehbiIGGzamqGpCe7JihmV6FAbK5Xo8lH92XmOKxNJlPobHPPWlLNcmrW%2ByUdbY%2B%2BLpGnyIbqDkzfoSXUM%2BttXRo2suGgNrBUfxREN7%2BIebipJPIs7gzTReUX8L5aGTgbRV8Uve5Ddq88MQP6psEOesBWpsltsO0FABZlZMFx06v2dCaIF7jmmlqKiyi1TQuD03OVqCu0BVDqZUlBekw0%2FuTvQY6pgF0ANmMujA2Vomg9XbYt1inQMaGQOs1kX4yLmy8uN2Aqgbh3PWzXNID7BBv0y9p%2BjLvG1XI5efeIhnn%2BaiejqKYpQxMXDKTszlNETaRP8AEBLrsSj8m2U%2FcLZw4rMBPqAyaX0jYY1%2B7pYfegm%2B3Q6Hazwfdhmd21I6G9X8I%2BzABj4KrNMghs69whcei2QjJr2BkhHhdIrC%2BRMX%2BzNjFFj740KRYSigt&X-Amz-Signature=958753b39d0a2647bf703833373569ce01deee6b7b03a48742415c4ee24b0f0b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJQHQ37X%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIDPA5SIBs2%2BbXO5E%2F3mQFkLlnpTkkWyVOjf%2Bin%2BNXNc%2FAiBn12sYkkDA57CpHHntSbS39Kt5HF4osvmAieNO4A0gFSr%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIMXbR7BxbiJXxrSC2qKtwD%2F8Uiui7D7NDVDm8nR1ldvF45fqjhYut7q84KCNnXRifdtj6iI2i2fF9a4ET0ulINm1Ue1HgRhz6sTLFWCPMEq2GHH%2FwNyNjbc74XNhE%2BAcf4FHLbO31i793mlQv6ZfvQb%2BoHGJV5J7w7aNAris%2ByvETiFnk0hD0sEgjBFAfRYn0qFlmfhmB0kjKMLTtX2CbG%2F%2BHjebpwd5kMEusJbxc8uSY41Js8gIeZBI9CXRHe3L7zCJ09kWC2JQYqp2t0yZDaNqXJPxd0Bt2QZQPjfprzHGnSam3QlIVBgatiS9XwLyWpXXJ5vvi9ghpHs6LbhqxRrxRgPf3VoYYehLx4DnJQAdgCn4aZ9R38bXdkO9AyUmwcEPm40mM0cfD8FKLbobI%2BKe9ZUXwp%2F1ycMhH4AOkTn%2BJeopnb1JXCNGrzaMEfNehbiIGGzamqGpCe7JihmV6FAbK5Xo8lH92XmOKxNJlPobHPPWlLNcmrW%2ByUdbY%2B%2BLpGnyIbqDkzfoSXUM%2BttXRo2suGgNrBUfxREN7%2BIebipJPIs7gzTReUX8L5aGTgbRV8Uve5Ddq88MQP6psEOesBWpsltsO0FABZlZMFx06v2dCaIF7jmmlqKiyi1TQuD03OVqCu0BVDqZUlBekw0%2FuTvQY6pgF0ANmMujA2Vomg9XbYt1inQMaGQOs1kX4yLmy8uN2Aqgbh3PWzXNID7BBv0y9p%2BjLvG1XI5efeIhnn%2BaiejqKYpQxMXDKTszlNETaRP8AEBLrsSj8m2U%2FcLZw4rMBPqAyaX0jYY1%2B7pYfegm%2B3Q6Hazwfdhmd21I6G9X8I%2BzABj4KrNMghs69whcei2QjJr2BkhHhdIrC%2BRMX%2BzNjFFj740KRYSigt&X-Amz-Signature=6253ddd971b0954d8ddece75e820bef955ecfcfbbb6e1eef460cd01e76ca4518&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJQHQ37X%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIDPA5SIBs2%2BbXO5E%2F3mQFkLlnpTkkWyVOjf%2Bin%2BNXNc%2FAiBn12sYkkDA57CpHHntSbS39Kt5HF4osvmAieNO4A0gFSr%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIMXbR7BxbiJXxrSC2qKtwD%2F8Uiui7D7NDVDm8nR1ldvF45fqjhYut7q84KCNnXRifdtj6iI2i2fF9a4ET0ulINm1Ue1HgRhz6sTLFWCPMEq2GHH%2FwNyNjbc74XNhE%2BAcf4FHLbO31i793mlQv6ZfvQb%2BoHGJV5J7w7aNAris%2ByvETiFnk0hD0sEgjBFAfRYn0qFlmfhmB0kjKMLTtX2CbG%2F%2BHjebpwd5kMEusJbxc8uSY41Js8gIeZBI9CXRHe3L7zCJ09kWC2JQYqp2t0yZDaNqXJPxd0Bt2QZQPjfprzHGnSam3QlIVBgatiS9XwLyWpXXJ5vvi9ghpHs6LbhqxRrxRgPf3VoYYehLx4DnJQAdgCn4aZ9R38bXdkO9AyUmwcEPm40mM0cfD8FKLbobI%2BKe9ZUXwp%2F1ycMhH4AOkTn%2BJeopnb1JXCNGrzaMEfNehbiIGGzamqGpCe7JihmV6FAbK5Xo8lH92XmOKxNJlPobHPPWlLNcmrW%2ByUdbY%2B%2BLpGnyIbqDkzfoSXUM%2BttXRo2suGgNrBUfxREN7%2BIebipJPIs7gzTReUX8L5aGTgbRV8Uve5Ddq88MQP6psEOesBWpsltsO0FABZlZMFx06v2dCaIF7jmmlqKiyi1TQuD03OVqCu0BVDqZUlBekw0%2FuTvQY6pgF0ANmMujA2Vomg9XbYt1inQMaGQOs1kX4yLmy8uN2Aqgbh3PWzXNID7BBv0y9p%2BjLvG1XI5efeIhnn%2BaiejqKYpQxMXDKTszlNETaRP8AEBLrsSj8m2U%2FcLZw4rMBPqAyaX0jYY1%2B7pYfegm%2B3Q6Hazwfdhmd21I6G9X8I%2BzABj4KrNMghs69whcei2QjJr2BkhHhdIrC%2BRMX%2BzNjFFj740KRYSigt&X-Amz-Signature=c2553045d7a518a46cadda1248665794d2b3b4226637f2736267a4430ada632a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJQHQ37X%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIDPA5SIBs2%2BbXO5E%2F3mQFkLlnpTkkWyVOjf%2Bin%2BNXNc%2FAiBn12sYkkDA57CpHHntSbS39Kt5HF4osvmAieNO4A0gFSr%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIMXbR7BxbiJXxrSC2qKtwD%2F8Uiui7D7NDVDm8nR1ldvF45fqjhYut7q84KCNnXRifdtj6iI2i2fF9a4ET0ulINm1Ue1HgRhz6sTLFWCPMEq2GHH%2FwNyNjbc74XNhE%2BAcf4FHLbO31i793mlQv6ZfvQb%2BoHGJV5J7w7aNAris%2ByvETiFnk0hD0sEgjBFAfRYn0qFlmfhmB0kjKMLTtX2CbG%2F%2BHjebpwd5kMEusJbxc8uSY41Js8gIeZBI9CXRHe3L7zCJ09kWC2JQYqp2t0yZDaNqXJPxd0Bt2QZQPjfprzHGnSam3QlIVBgatiS9XwLyWpXXJ5vvi9ghpHs6LbhqxRrxRgPf3VoYYehLx4DnJQAdgCn4aZ9R38bXdkO9AyUmwcEPm40mM0cfD8FKLbobI%2BKe9ZUXwp%2F1ycMhH4AOkTn%2BJeopnb1JXCNGrzaMEfNehbiIGGzamqGpCe7JihmV6FAbK5Xo8lH92XmOKxNJlPobHPPWlLNcmrW%2ByUdbY%2B%2BLpGnyIbqDkzfoSXUM%2BttXRo2suGgNrBUfxREN7%2BIebipJPIs7gzTReUX8L5aGTgbRV8Uve5Ddq88MQP6psEOesBWpsltsO0FABZlZMFx06v2dCaIF7jmmlqKiyi1TQuD03OVqCu0BVDqZUlBekw0%2FuTvQY6pgF0ANmMujA2Vomg9XbYt1inQMaGQOs1kX4yLmy8uN2Aqgbh3PWzXNID7BBv0y9p%2BjLvG1XI5efeIhnn%2BaiejqKYpQxMXDKTszlNETaRP8AEBLrsSj8m2U%2FcLZw4rMBPqAyaX0jYY1%2B7pYfegm%2B3Q6Hazwfdhmd21I6G9X8I%2BzABj4KrNMghs69whcei2QjJr2BkhHhdIrC%2BRMX%2BzNjFFj740KRYSigt&X-Amz-Signature=b93a562ea728725984eddb7bc312347119a8e40a87605b910616dfeb51342482&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZVID7WD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIECtVV960ruBmOH2l3HRfod1WzRiswgjvZcuTx1qccHqAiEA7q5gE1NOvHL1ye%2BMOJxQN0zQi1Ke2nDK6cdF4r6OosQq%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDPpDpRCTZ0rypvlTiyrcA79HNggLOBaTOfMvdUPax0vcqrpZ2qGw7562%2F1zQKOrf0jx%2Bxp9bBALcuG%2B8vzXgQo28P1rj1cdMqmmnBEKQoplmqa1TjnfoB9Kpi75Ht%2FKh8eU6LsgsvxfeKWeNFJkSkyX67BI9vb9He86qmEO%2B67o%2BuXn0qYFREg7Zb7nIbCL4fKvyL3brpbkqj8exVzyi4mowWZ0RvU7TCekoguvJRtWWL7ABzN6DekRd79vVUkREZOImJbNV7eis%2Fi8yBCZFjpwr5DG7BtwqnAGBCn8abN%2FUQRCY6whU%2FNj4pacjy5LN1dze%2F%2BTnmXNH8BXLCYLxQHKn2vX%2FYMJFmJmcd%2FK89IdLWY7WxqCvIDBcEBSnVq1SQs5OSY%2F1v2WaKgupX5g4mNUZSIG3n53TB7LFOSABJ9Bhmfi4AhsalcMu1B2MKYrU%2FGtyo8jqdAdtoM2c6tXjqbyfSQm2M3if1QERIc5x69qAw%2F6m3FBU7n3wq6Zuf2WK%2FzVZ3YuRZOJ%2FJcy0T2fTvCmyg9a7gNZBNe2RFr0lGKm5IMK1RUz%2Bx2KcWGCsqG7rCcUKQS9goOukc%2FhYHsF%2FpfV8P8S6C7YKLUAuVdp5Fi8oAXBVpKHzyszIEo1MTOHvoJNFitmd5HDChlsqMPP7k70GOqUBLfZfd18srDO9GbhZxYrygDQbp8PaV1vWUNJwpEVt8losb6VgZUgAtZClqk8ieilGecRxIgUfFamwtYi0X6DlSCTEhpiA5uAOeiR72udqBXe53KarWxJMFbxJO0ktGbcZzaEZ0ywLLBGXOZRrFnuktv%2F1C1BKF2wDkxn6uOdWz8b%2Bl90x5DEfCgcgvkK0il88aBXX%2BvbsLHgm7thA%2ByQkIsRk5yCS&X-Amz-Signature=e159b30f39c28330393afebe0ac9f5801907dbf60a8203078faf83c7cb54d5b4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZVID7WD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIECtVV960ruBmOH2l3HRfod1WzRiswgjvZcuTx1qccHqAiEA7q5gE1NOvHL1ye%2BMOJxQN0zQi1Ke2nDK6cdF4r6OosQq%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDPpDpRCTZ0rypvlTiyrcA79HNggLOBaTOfMvdUPax0vcqrpZ2qGw7562%2F1zQKOrf0jx%2Bxp9bBALcuG%2B8vzXgQo28P1rj1cdMqmmnBEKQoplmqa1TjnfoB9Kpi75Ht%2FKh8eU6LsgsvxfeKWeNFJkSkyX67BI9vb9He86qmEO%2B67o%2BuXn0qYFREg7Zb7nIbCL4fKvyL3brpbkqj8exVzyi4mowWZ0RvU7TCekoguvJRtWWL7ABzN6DekRd79vVUkREZOImJbNV7eis%2Fi8yBCZFjpwr5DG7BtwqnAGBCn8abN%2FUQRCY6whU%2FNj4pacjy5LN1dze%2F%2BTnmXNH8BXLCYLxQHKn2vX%2FYMJFmJmcd%2FK89IdLWY7WxqCvIDBcEBSnVq1SQs5OSY%2F1v2WaKgupX5g4mNUZSIG3n53TB7LFOSABJ9Bhmfi4AhsalcMu1B2MKYrU%2FGtyo8jqdAdtoM2c6tXjqbyfSQm2M3if1QERIc5x69qAw%2F6m3FBU7n3wq6Zuf2WK%2FzVZ3YuRZOJ%2FJcy0T2fTvCmyg9a7gNZBNe2RFr0lGKm5IMK1RUz%2Bx2KcWGCsqG7rCcUKQS9goOukc%2FhYHsF%2FpfV8P8S6C7YKLUAuVdp5Fi8oAXBVpKHzyszIEo1MTOHvoJNFitmd5HDChlsqMPP7k70GOqUBLfZfd18srDO9GbhZxYrygDQbp8PaV1vWUNJwpEVt8losb6VgZUgAtZClqk8ieilGecRxIgUfFamwtYi0X6DlSCTEhpiA5uAOeiR72udqBXe53KarWxJMFbxJO0ktGbcZzaEZ0ywLLBGXOZRrFnuktv%2F1C1BKF2wDkxn6uOdWz8b%2Bl90x5DEfCgcgvkK0il88aBXX%2BvbsLHgm7thA%2ByQkIsRk5yCS&X-Amz-Signature=d65d5ddeab9591358b24c89bd7fc91e7bc95f7dfadf5f922a895f46c20ba61a3&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
