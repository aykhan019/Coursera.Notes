

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QXCZCKGX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICckPGQPa6NRQHOJ%2Fid7%2BDHthtbIsJ3%2BbPnq9BJ4grUAAiAIE98pDrbARxipD0rzdKOTmYfv72PilBdqrGAgafiPWCqIBAio%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2FWH22aoLk296d0A2KtwDDKI8d2umWPsXxMwX5tB6L98M5gl4IEPGHEhfPl7SOiYC8K%2BRGFJe46RQrgPps3cP%2BuI%2BxKsTh%2FQ8Ys7FCCHOxZger9wN%2BQWU2d%2BFBFjSrEENB9RsYWZjfC6GVpdzohzDRcvgqL1uPm%2BtnB91jaksoy4RpGWrs0fKvTm6AF%2F5mnmWBB8QiprN4IsnZwmCpHTOyRqlcfSzEYCEFYJkAymEOlzprFIL5WFSS6AjWzR1wNpDkJoAkaqgmkRA2T9X3pNspauSUS862fjQx7H%2FPa%2BE2h0FVY6JxSlfSCA2ARIS7y7B63snO1HMR8IBySBkmCiTIdSdCuKcY8ghBgn%2F84NjyhpsC9HbUtQf6CRgeHj0gtMWIN4foOLJ%2FtMGaa%2F%2BUYYQxi6qhFvTPSoI3xb9ETSANymqJaTpAziQReNSyS4arJqtlzJ9LkpddVdc2UBrtgDhwrLizzap4AVmy6qxIhbLjTP%2F6veqhMvfe2nZc%2FYCPo5GBS1YXcUUrlZmUXjMGSKDV36Lf%2Bd7keoxgHZX%2BBwDzMBHLp70OJOyHGEgIS09mun%2BbS9JjvwclwHzft%2BfPXvG6xlQtJRAgf4NX8%2B%2FrDXkjtLxZcu0s9sqa3Ed9zPhU4NkMPRXLNrMz6kJuVgwjJjuvAY6pgFl9yFx7kdBM9d2X5xchw8TgFnWBfVbqjC5M1d1jw59iFOhxYUt9jB7eLTy5eYsWXT6%2B93aNMI%2FZkJAO%2BHw5hTCZIsa1xgKfL6FeyBFAXH2XshQEd66VY5QiRd2WECjiM93cFueBKcMpT5rzmgRYy2zOb5UyGeugfnqjOmw1DawxNbV5TvpeC0R%2B9RaI89uqlM0wGFW3Us2SA7lFiC5gU%2Bor7MS2Bgf&X-Amz-Signature=f767c959bb9f96b1900c957766b490c9d14ee93fe15f6f7b2f58b8e9e5b08a13&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QXCZCKGX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICckPGQPa6NRQHOJ%2Fid7%2BDHthtbIsJ3%2BbPnq9BJ4grUAAiAIE98pDrbARxipD0rzdKOTmYfv72PilBdqrGAgafiPWCqIBAio%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2FWH22aoLk296d0A2KtwDDKI8d2umWPsXxMwX5tB6L98M5gl4IEPGHEhfPl7SOiYC8K%2BRGFJe46RQrgPps3cP%2BuI%2BxKsTh%2FQ8Ys7FCCHOxZger9wN%2BQWU2d%2BFBFjSrEENB9RsYWZjfC6GVpdzohzDRcvgqL1uPm%2BtnB91jaksoy4RpGWrs0fKvTm6AF%2F5mnmWBB8QiprN4IsnZwmCpHTOyRqlcfSzEYCEFYJkAymEOlzprFIL5WFSS6AjWzR1wNpDkJoAkaqgmkRA2T9X3pNspauSUS862fjQx7H%2FPa%2BE2h0FVY6JxSlfSCA2ARIS7y7B63snO1HMR8IBySBkmCiTIdSdCuKcY8ghBgn%2F84NjyhpsC9HbUtQf6CRgeHj0gtMWIN4foOLJ%2FtMGaa%2F%2BUYYQxi6qhFvTPSoI3xb9ETSANymqJaTpAziQReNSyS4arJqtlzJ9LkpddVdc2UBrtgDhwrLizzap4AVmy6qxIhbLjTP%2F6veqhMvfe2nZc%2FYCPo5GBS1YXcUUrlZmUXjMGSKDV36Lf%2Bd7keoxgHZX%2BBwDzMBHLp70OJOyHGEgIS09mun%2BbS9JjvwclwHzft%2BfPXvG6xlQtJRAgf4NX8%2B%2FrDXkjtLxZcu0s9sqa3Ed9zPhU4NkMPRXLNrMz6kJuVgwjJjuvAY6pgFl9yFx7kdBM9d2X5xchw8TgFnWBfVbqjC5M1d1jw59iFOhxYUt9jB7eLTy5eYsWXT6%2B93aNMI%2FZkJAO%2BHw5hTCZIsa1xgKfL6FeyBFAXH2XshQEd66VY5QiRd2WECjiM93cFueBKcMpT5rzmgRYy2zOb5UyGeugfnqjOmw1DawxNbV5TvpeC0R%2B9RaI89uqlM0wGFW3Us2SA7lFiC5gU%2Bor7MS2Bgf&X-Amz-Signature=33f66c3f335fee04f1ee33e5e9aad47e1c226ab8e90fa8388e65e26dd1981d18&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QXCZCKGX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICckPGQPa6NRQHOJ%2Fid7%2BDHthtbIsJ3%2BbPnq9BJ4grUAAiAIE98pDrbARxipD0rzdKOTmYfv72PilBdqrGAgafiPWCqIBAio%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2FWH22aoLk296d0A2KtwDDKI8d2umWPsXxMwX5tB6L98M5gl4IEPGHEhfPl7SOiYC8K%2BRGFJe46RQrgPps3cP%2BuI%2BxKsTh%2FQ8Ys7FCCHOxZger9wN%2BQWU2d%2BFBFjSrEENB9RsYWZjfC6GVpdzohzDRcvgqL1uPm%2BtnB91jaksoy4RpGWrs0fKvTm6AF%2F5mnmWBB8QiprN4IsnZwmCpHTOyRqlcfSzEYCEFYJkAymEOlzprFIL5WFSS6AjWzR1wNpDkJoAkaqgmkRA2T9X3pNspauSUS862fjQx7H%2FPa%2BE2h0FVY6JxSlfSCA2ARIS7y7B63snO1HMR8IBySBkmCiTIdSdCuKcY8ghBgn%2F84NjyhpsC9HbUtQf6CRgeHj0gtMWIN4foOLJ%2FtMGaa%2F%2BUYYQxi6qhFvTPSoI3xb9ETSANymqJaTpAziQReNSyS4arJqtlzJ9LkpddVdc2UBrtgDhwrLizzap4AVmy6qxIhbLjTP%2F6veqhMvfe2nZc%2FYCPo5GBS1YXcUUrlZmUXjMGSKDV36Lf%2Bd7keoxgHZX%2BBwDzMBHLp70OJOyHGEgIS09mun%2BbS9JjvwclwHzft%2BfPXvG6xlQtJRAgf4NX8%2B%2FrDXkjtLxZcu0s9sqa3Ed9zPhU4NkMPRXLNrMz6kJuVgwjJjuvAY6pgFl9yFx7kdBM9d2X5xchw8TgFnWBfVbqjC5M1d1jw59iFOhxYUt9jB7eLTy5eYsWXT6%2B93aNMI%2FZkJAO%2BHw5hTCZIsa1xgKfL6FeyBFAXH2XshQEd66VY5QiRd2WECjiM93cFueBKcMpT5rzmgRYy2zOb5UyGeugfnqjOmw1DawxNbV5TvpeC0R%2B9RaI89uqlM0wGFW3Us2SA7lFiC5gU%2Bor7MS2Bgf&X-Amz-Signature=d20e4173fa55a7a40648e1a482ea27bfbf4a7d5c7199d9509b46acaa66792a65&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QXCZCKGX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICckPGQPa6NRQHOJ%2Fid7%2BDHthtbIsJ3%2BbPnq9BJ4grUAAiAIE98pDrbARxipD0rzdKOTmYfv72PilBdqrGAgafiPWCqIBAio%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2FWH22aoLk296d0A2KtwDDKI8d2umWPsXxMwX5tB6L98M5gl4IEPGHEhfPl7SOiYC8K%2BRGFJe46RQrgPps3cP%2BuI%2BxKsTh%2FQ8Ys7FCCHOxZger9wN%2BQWU2d%2BFBFjSrEENB9RsYWZjfC6GVpdzohzDRcvgqL1uPm%2BtnB91jaksoy4RpGWrs0fKvTm6AF%2F5mnmWBB8QiprN4IsnZwmCpHTOyRqlcfSzEYCEFYJkAymEOlzprFIL5WFSS6AjWzR1wNpDkJoAkaqgmkRA2T9X3pNspauSUS862fjQx7H%2FPa%2BE2h0FVY6JxSlfSCA2ARIS7y7B63snO1HMR8IBySBkmCiTIdSdCuKcY8ghBgn%2F84NjyhpsC9HbUtQf6CRgeHj0gtMWIN4foOLJ%2FtMGaa%2F%2BUYYQxi6qhFvTPSoI3xb9ETSANymqJaTpAziQReNSyS4arJqtlzJ9LkpddVdc2UBrtgDhwrLizzap4AVmy6qxIhbLjTP%2F6veqhMvfe2nZc%2FYCPo5GBS1YXcUUrlZmUXjMGSKDV36Lf%2Bd7keoxgHZX%2BBwDzMBHLp70OJOyHGEgIS09mun%2BbS9JjvwclwHzft%2BfPXvG6xlQtJRAgf4NX8%2B%2FrDXkjtLxZcu0s9sqa3Ed9zPhU4NkMPRXLNrMz6kJuVgwjJjuvAY6pgFl9yFx7kdBM9d2X5xchw8TgFnWBfVbqjC5M1d1jw59iFOhxYUt9jB7eLTy5eYsWXT6%2B93aNMI%2FZkJAO%2BHw5hTCZIsa1xgKfL6FeyBFAXH2XshQEd66VY5QiRd2WECjiM93cFueBKcMpT5rzmgRYy2zOb5UyGeugfnqjOmw1DawxNbV5TvpeC0R%2B9RaI89uqlM0wGFW3Us2SA7lFiC5gU%2Bor7MS2Bgf&X-Amz-Signature=c6e20ebdc43f59ba9dd1087d9d6d5fa1d45f264a3772089753a969af926ab8d3&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QXCZCKGX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICckPGQPa6NRQHOJ%2Fid7%2BDHthtbIsJ3%2BbPnq9BJ4grUAAiAIE98pDrbARxipD0rzdKOTmYfv72PilBdqrGAgafiPWCqIBAio%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2FWH22aoLk296d0A2KtwDDKI8d2umWPsXxMwX5tB6L98M5gl4IEPGHEhfPl7SOiYC8K%2BRGFJe46RQrgPps3cP%2BuI%2BxKsTh%2FQ8Ys7FCCHOxZger9wN%2BQWU2d%2BFBFjSrEENB9RsYWZjfC6GVpdzohzDRcvgqL1uPm%2BtnB91jaksoy4RpGWrs0fKvTm6AF%2F5mnmWBB8QiprN4IsnZwmCpHTOyRqlcfSzEYCEFYJkAymEOlzprFIL5WFSS6AjWzR1wNpDkJoAkaqgmkRA2T9X3pNspauSUS862fjQx7H%2FPa%2BE2h0FVY6JxSlfSCA2ARIS7y7B63snO1HMR8IBySBkmCiTIdSdCuKcY8ghBgn%2F84NjyhpsC9HbUtQf6CRgeHj0gtMWIN4foOLJ%2FtMGaa%2F%2BUYYQxi6qhFvTPSoI3xb9ETSANymqJaTpAziQReNSyS4arJqtlzJ9LkpddVdc2UBrtgDhwrLizzap4AVmy6qxIhbLjTP%2F6veqhMvfe2nZc%2FYCPo5GBS1YXcUUrlZmUXjMGSKDV36Lf%2Bd7keoxgHZX%2BBwDzMBHLp70OJOyHGEgIS09mun%2BbS9JjvwclwHzft%2BfPXvG6xlQtJRAgf4NX8%2B%2FrDXkjtLxZcu0s9sqa3Ed9zPhU4NkMPRXLNrMz6kJuVgwjJjuvAY6pgFl9yFx7kdBM9d2X5xchw8TgFnWBfVbqjC5M1d1jw59iFOhxYUt9jB7eLTy5eYsWXT6%2B93aNMI%2FZkJAO%2BHw5hTCZIsa1xgKfL6FeyBFAXH2XshQEd66VY5QiRd2WECjiM93cFueBKcMpT5rzmgRYy2zOb5UyGeugfnqjOmw1DawxNbV5TvpeC0R%2B9RaI89uqlM0wGFW3Us2SA7lFiC5gU%2Bor7MS2Bgf&X-Amz-Signature=fbb0a12f3da0d477f0867bb6e064de02a3a68fccdeb7265711c0daf97725e140&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QXCZCKGX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICckPGQPa6NRQHOJ%2Fid7%2BDHthtbIsJ3%2BbPnq9BJ4grUAAiAIE98pDrbARxipD0rzdKOTmYfv72PilBdqrGAgafiPWCqIBAio%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2FWH22aoLk296d0A2KtwDDKI8d2umWPsXxMwX5tB6L98M5gl4IEPGHEhfPl7SOiYC8K%2BRGFJe46RQrgPps3cP%2BuI%2BxKsTh%2FQ8Ys7FCCHOxZger9wN%2BQWU2d%2BFBFjSrEENB9RsYWZjfC6GVpdzohzDRcvgqL1uPm%2BtnB91jaksoy4RpGWrs0fKvTm6AF%2F5mnmWBB8QiprN4IsnZwmCpHTOyRqlcfSzEYCEFYJkAymEOlzprFIL5WFSS6AjWzR1wNpDkJoAkaqgmkRA2T9X3pNspauSUS862fjQx7H%2FPa%2BE2h0FVY6JxSlfSCA2ARIS7y7B63snO1HMR8IBySBkmCiTIdSdCuKcY8ghBgn%2F84NjyhpsC9HbUtQf6CRgeHj0gtMWIN4foOLJ%2FtMGaa%2F%2BUYYQxi6qhFvTPSoI3xb9ETSANymqJaTpAziQReNSyS4arJqtlzJ9LkpddVdc2UBrtgDhwrLizzap4AVmy6qxIhbLjTP%2F6veqhMvfe2nZc%2FYCPo5GBS1YXcUUrlZmUXjMGSKDV36Lf%2Bd7keoxgHZX%2BBwDzMBHLp70OJOyHGEgIS09mun%2BbS9JjvwclwHzft%2BfPXvG6xlQtJRAgf4NX8%2B%2FrDXkjtLxZcu0s9sqa3Ed9zPhU4NkMPRXLNrMz6kJuVgwjJjuvAY6pgFl9yFx7kdBM9d2X5xchw8TgFnWBfVbqjC5M1d1jw59iFOhxYUt9jB7eLTy5eYsWXT6%2B93aNMI%2FZkJAO%2BHw5hTCZIsa1xgKfL6FeyBFAXH2XshQEd66VY5QiRd2WECjiM93cFueBKcMpT5rzmgRYy2zOb5UyGeugfnqjOmw1DawxNbV5TvpeC0R%2B9RaI89uqlM0wGFW3Us2SA7lFiC5gU%2Bor7MS2Bgf&X-Amz-Signature=eec0178f2f5cd50120cb1561f4dd866fdc509360cf8292d1267c4dfe958988c2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QXCZCKGX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICckPGQPa6NRQHOJ%2Fid7%2BDHthtbIsJ3%2BbPnq9BJ4grUAAiAIE98pDrbARxipD0rzdKOTmYfv72PilBdqrGAgafiPWCqIBAio%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2FWH22aoLk296d0A2KtwDDKI8d2umWPsXxMwX5tB6L98M5gl4IEPGHEhfPl7SOiYC8K%2BRGFJe46RQrgPps3cP%2BuI%2BxKsTh%2FQ8Ys7FCCHOxZger9wN%2BQWU2d%2BFBFjSrEENB9RsYWZjfC6GVpdzohzDRcvgqL1uPm%2BtnB91jaksoy4RpGWrs0fKvTm6AF%2F5mnmWBB8QiprN4IsnZwmCpHTOyRqlcfSzEYCEFYJkAymEOlzprFIL5WFSS6AjWzR1wNpDkJoAkaqgmkRA2T9X3pNspauSUS862fjQx7H%2FPa%2BE2h0FVY6JxSlfSCA2ARIS7y7B63snO1HMR8IBySBkmCiTIdSdCuKcY8ghBgn%2F84NjyhpsC9HbUtQf6CRgeHj0gtMWIN4foOLJ%2FtMGaa%2F%2BUYYQxi6qhFvTPSoI3xb9ETSANymqJaTpAziQReNSyS4arJqtlzJ9LkpddVdc2UBrtgDhwrLizzap4AVmy6qxIhbLjTP%2F6veqhMvfe2nZc%2FYCPo5GBS1YXcUUrlZmUXjMGSKDV36Lf%2Bd7keoxgHZX%2BBwDzMBHLp70OJOyHGEgIS09mun%2BbS9JjvwclwHzft%2BfPXvG6xlQtJRAgf4NX8%2B%2FrDXkjtLxZcu0s9sqa3Ed9zPhU4NkMPRXLNrMz6kJuVgwjJjuvAY6pgFl9yFx7kdBM9d2X5xchw8TgFnWBfVbqjC5M1d1jw59iFOhxYUt9jB7eLTy5eYsWXT6%2B93aNMI%2FZkJAO%2BHw5hTCZIsa1xgKfL6FeyBFAXH2XshQEd66VY5QiRd2WECjiM93cFueBKcMpT5rzmgRYy2zOb5UyGeugfnqjOmw1DawxNbV5TvpeC0R%2B9RaI89uqlM0wGFW3Us2SA7lFiC5gU%2Bor7MS2Bgf&X-Amz-Signature=522a7865bf03d399817c4d642544f859c3f1c469d3eb5dcd6cf565ec11928c72&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QXCZCKGX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICckPGQPa6NRQHOJ%2Fid7%2BDHthtbIsJ3%2BbPnq9BJ4grUAAiAIE98pDrbARxipD0rzdKOTmYfv72PilBdqrGAgafiPWCqIBAio%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2FWH22aoLk296d0A2KtwDDKI8d2umWPsXxMwX5tB6L98M5gl4IEPGHEhfPl7SOiYC8K%2BRGFJe46RQrgPps3cP%2BuI%2BxKsTh%2FQ8Ys7FCCHOxZger9wN%2BQWU2d%2BFBFjSrEENB9RsYWZjfC6GVpdzohzDRcvgqL1uPm%2BtnB91jaksoy4RpGWrs0fKvTm6AF%2F5mnmWBB8QiprN4IsnZwmCpHTOyRqlcfSzEYCEFYJkAymEOlzprFIL5WFSS6AjWzR1wNpDkJoAkaqgmkRA2T9X3pNspauSUS862fjQx7H%2FPa%2BE2h0FVY6JxSlfSCA2ARIS7y7B63snO1HMR8IBySBkmCiTIdSdCuKcY8ghBgn%2F84NjyhpsC9HbUtQf6CRgeHj0gtMWIN4foOLJ%2FtMGaa%2F%2BUYYQxi6qhFvTPSoI3xb9ETSANymqJaTpAziQReNSyS4arJqtlzJ9LkpddVdc2UBrtgDhwrLizzap4AVmy6qxIhbLjTP%2F6veqhMvfe2nZc%2FYCPo5GBS1YXcUUrlZmUXjMGSKDV36Lf%2Bd7keoxgHZX%2BBwDzMBHLp70OJOyHGEgIS09mun%2BbS9JjvwclwHzft%2BfPXvG6xlQtJRAgf4NX8%2B%2FrDXkjtLxZcu0s9sqa3Ed9zPhU4NkMPRXLNrMz6kJuVgwjJjuvAY6pgFl9yFx7kdBM9d2X5xchw8TgFnWBfVbqjC5M1d1jw59iFOhxYUt9jB7eLTy5eYsWXT6%2B93aNMI%2FZkJAO%2BHw5hTCZIsa1xgKfL6FeyBFAXH2XshQEd66VY5QiRd2WECjiM93cFueBKcMpT5rzmgRYy2zOb5UyGeugfnqjOmw1DawxNbV5TvpeC0R%2B9RaI89uqlM0wGFW3Us2SA7lFiC5gU%2Bor7MS2Bgf&X-Amz-Signature=6931214e5880eaa523e6b55733e1acbb379f3cd4eabc874d1cbde096ba6fe858&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QXCZCKGX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICckPGQPa6NRQHOJ%2Fid7%2BDHthtbIsJ3%2BbPnq9BJ4grUAAiAIE98pDrbARxipD0rzdKOTmYfv72PilBdqrGAgafiPWCqIBAio%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2FWH22aoLk296d0A2KtwDDKI8d2umWPsXxMwX5tB6L98M5gl4IEPGHEhfPl7SOiYC8K%2BRGFJe46RQrgPps3cP%2BuI%2BxKsTh%2FQ8Ys7FCCHOxZger9wN%2BQWU2d%2BFBFjSrEENB9RsYWZjfC6GVpdzohzDRcvgqL1uPm%2BtnB91jaksoy4RpGWrs0fKvTm6AF%2F5mnmWBB8QiprN4IsnZwmCpHTOyRqlcfSzEYCEFYJkAymEOlzprFIL5WFSS6AjWzR1wNpDkJoAkaqgmkRA2T9X3pNspauSUS862fjQx7H%2FPa%2BE2h0FVY6JxSlfSCA2ARIS7y7B63snO1HMR8IBySBkmCiTIdSdCuKcY8ghBgn%2F84NjyhpsC9HbUtQf6CRgeHj0gtMWIN4foOLJ%2FtMGaa%2F%2BUYYQxi6qhFvTPSoI3xb9ETSANymqJaTpAziQReNSyS4arJqtlzJ9LkpddVdc2UBrtgDhwrLizzap4AVmy6qxIhbLjTP%2F6veqhMvfe2nZc%2FYCPo5GBS1YXcUUrlZmUXjMGSKDV36Lf%2Bd7keoxgHZX%2BBwDzMBHLp70OJOyHGEgIS09mun%2BbS9JjvwclwHzft%2BfPXvG6xlQtJRAgf4NX8%2B%2FrDXkjtLxZcu0s9sqa3Ed9zPhU4NkMPRXLNrMz6kJuVgwjJjuvAY6pgFl9yFx7kdBM9d2X5xchw8TgFnWBfVbqjC5M1d1jw59iFOhxYUt9jB7eLTy5eYsWXT6%2B93aNMI%2FZkJAO%2BHw5hTCZIsa1xgKfL6FeyBFAXH2XshQEd66VY5QiRd2WECjiM93cFueBKcMpT5rzmgRYy2zOb5UyGeugfnqjOmw1DawxNbV5TvpeC0R%2B9RaI89uqlM0wGFW3Us2SA7lFiC5gU%2Bor7MS2Bgf&X-Amz-Signature=981bee7369cebc6f06296838a90546c973cf8e4a934437bc2364eb5111ba9c49&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UHR2WZV5%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC14x8%2Bd3O9nPl5%2BAiB9q1ZrmiU5iCqgjOdDsKEAY6ZuAIgRqYsjXP722zF3sDDwGTVl2D%2B2JaxvLv%2BDuajrnexKF8qiAQIqP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG%2BSU94nmy4aidGSICrcA1n6KE6LuXpF6XzK6%2B0dxtMP62%2BconvUfOE0281UmY7eebi1HjI4bjf47ZLHzsdzc1v7WRETXymq92smLth1EpFZ1BkNf3rIu0QRlyperhmNc7QSzVHShSXLi00EOF%2FcgeMxVByMxtxtlSA6EL7%2F3rOdajRhPduAIfC0cP3y35m7GJI8yniJwOn5LRpr7B3XZaFgz102DbdJdfJLGg1AegREKv24WdZMkA4x%2BZzVN3N6UQUpIaM%2F9kMPDSxmLgGMyg2w7chG%2F6cknnvst4jtCCNhuVur7HF%2BwceP8AiCvbcyRPhuOssX%2FKHtZkq9Z%2FzJ1jkNNUzMHwqBGzqsD%2BlwLWHiesl0vkT3q89ojfkUxopWpUMmXvKHr3AbMRAhbLr26ei7YNH7FX7X11CjO%2BDMenfQfLNWpipHKI60IbZkdI2WIRziJ1h9rq7ozdqxON5HrUveIQAs2tkjCqjbpS1zNVWQVJImwxWzXRFan6ZvOanDGyVzaOa5e7cNWdKthczx9J%2BCsnnCxC%2BLK5EyPW4Kw7w7rXLJGFrRI%2B%2FiGcxlLCda%2B4dynSSQQf7msOmK0if%2F8y7CUEU2V3w4k90egPO3adO4%2FA8c0AymByCKr0ZgwxPxkEVPrlZhqXoN%2Bb1rMKOX7rwGOqUBx8zw%2FBwtPxFr%2BgBSPH9CLsEiGL1NK%2BXAHpH8I42u5mS7yJoLvjGoh0tb6hJbRYUdew8R4NIY7MKmHa4VlIkofRi28gy6NATxS1CHOvMCFCIBO6n9LKD8hpOjojV5wIjcaFpUtlxiXxch7884HRuhxDQLmMxWa3KAQ%2FbXJpeVBHUd%2B%2F5sPYOmXZO01L5vpvRfXRiwO3z8duOZ%2B2uFk6P0uoCAhXjB&X-Amz-Signature=be3b9987d46de7e5fdf506f35f2a5dd6907c95a5fc2e6d1a0f2155d5dbb5cfe1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UHR2WZV5%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC14x8%2Bd3O9nPl5%2BAiB9q1ZrmiU5iCqgjOdDsKEAY6ZuAIgRqYsjXP722zF3sDDwGTVl2D%2B2JaxvLv%2BDuajrnexKF8qiAQIqP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG%2BSU94nmy4aidGSICrcA1n6KE6LuXpF6XzK6%2B0dxtMP62%2BconvUfOE0281UmY7eebi1HjI4bjf47ZLHzsdzc1v7WRETXymq92smLth1EpFZ1BkNf3rIu0QRlyperhmNc7QSzVHShSXLi00EOF%2FcgeMxVByMxtxtlSA6EL7%2F3rOdajRhPduAIfC0cP3y35m7GJI8yniJwOn5LRpr7B3XZaFgz102DbdJdfJLGg1AegREKv24WdZMkA4x%2BZzVN3N6UQUpIaM%2F9kMPDSxmLgGMyg2w7chG%2F6cknnvst4jtCCNhuVur7HF%2BwceP8AiCvbcyRPhuOssX%2FKHtZkq9Z%2FzJ1jkNNUzMHwqBGzqsD%2BlwLWHiesl0vkT3q89ojfkUxopWpUMmXvKHr3AbMRAhbLr26ei7YNH7FX7X11CjO%2BDMenfQfLNWpipHKI60IbZkdI2WIRziJ1h9rq7ozdqxON5HrUveIQAs2tkjCqjbpS1zNVWQVJImwxWzXRFan6ZvOanDGyVzaOa5e7cNWdKthczx9J%2BCsnnCxC%2BLK5EyPW4Kw7w7rXLJGFrRI%2B%2FiGcxlLCda%2B4dynSSQQf7msOmK0if%2F8y7CUEU2V3w4k90egPO3adO4%2FA8c0AymByCKr0ZgwxPxkEVPrlZhqXoN%2Bb1rMKOX7rwGOqUBx8zw%2FBwtPxFr%2BgBSPH9CLsEiGL1NK%2BXAHpH8I42u5mS7yJoLvjGoh0tb6hJbRYUdew8R4NIY7MKmHa4VlIkofRi28gy6NATxS1CHOvMCFCIBO6n9LKD8hpOjojV5wIjcaFpUtlxiXxch7884HRuhxDQLmMxWa3KAQ%2FbXJpeVBHUd%2B%2F5sPYOmXZO01L5vpvRfXRiwO3z8duOZ%2B2uFk6P0uoCAhXjB&X-Amz-Signature=08cf6051a4be94b78ae627194fd9d72ec53af406f1cdb50a78bce03539d5e9e2&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
