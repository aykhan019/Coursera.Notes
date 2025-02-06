

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XS3CUXW%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJGMEQCIFbx%2B%2F1oqLq63YY2pSDTT0pk2Gy3cDFueNffxDF1rTFrAiBUnHIr4G5rT1BpyQmtlU4sZVEm7z0TsQAsKin4M8mzryr%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIMLsKrwouvbD7R2cfiKtwDS9RKBC5%2Bz4%2FEru8NfRYK0WoFXoB%2BSgfnh0DRRQ7feATpV60vgNAPmIRFwdJVTT5XrOC9TS6cOPI7vmMDyW%2B2dbB0kJvEazzE7YT3e%2FT5gJjsNXSJFTO7tFQAioqyzJPojKSoppFurOchfL7lWtPn1nUwCpJdlceiBUrfpDHgBkLI3Ih2aZf1ft9LVariAJAUs7gchlfnmbu2E2Nos%2FXzIlfIcrMXdFxd6hizfom8cC0om7BY0%2FMAGUm7YdE489ZJoq8IhqADnFuuDIA98262vNb5Jt2ThTP1MBjcZeCjww0qHkSvLIQpB2LdO8WyUZTFeDI0myxEpUkQ6qooDscbhH06kFLr%2FIHNNf4ajq78v0cF07LCPQob%2F3TfkAVGPtP78Wvokb%2BNWC1cUhhlgEe%2Bhx%2FKaG7IClfzDOpK%2B0ZKp6jTv416EqOEfny0kz4ZHCQvEdnv1VGE9OzLaKUq5yvLyKAO0bqBz27yquDh6Dx%2BMfn5IJgdqQmGBrRGt7ThoUcwBbJ952iin1y%2B2DLKotlf%2BKtgM4QCTlRN86UA0ReavdvtyhPhorVTgGyqoh9%2BId9jEM1mhCyel2jdR5WNsFga1YJhxaUgp8QBJoXJg10LUsS%2FGaRu7OHjUhWj5zcw6NGTvQY6pgGQ6sN62ltIq7lb1kHcb16BsgarQBPKbFP6JploKLjbSfJeVJQ0HA7QRBBTAes0BedvdQHmxgN79ZLODR5ocoPeIzm7yGXenLYEgIG9ynxoFpQF3jEG0%2FLmAMcsxtWvIAQ7%2Ft%2BIgWVJAC5QWl6Wf59f5%2F43FXdopF0Vv3SGkSqbyjlkDYPA6pcSzY2Cy0Q44QyNJaaEaVL7vlOc6fia8X0Q7sKP0g%2Fn&X-Amz-Signature=082a147a5dd41256deadaac1eb0656b04f2daa591e24ed6edb8a3373145e877f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XS3CUXW%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJGMEQCIFbx%2B%2F1oqLq63YY2pSDTT0pk2Gy3cDFueNffxDF1rTFrAiBUnHIr4G5rT1BpyQmtlU4sZVEm7z0TsQAsKin4M8mzryr%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIMLsKrwouvbD7R2cfiKtwDS9RKBC5%2Bz4%2FEru8NfRYK0WoFXoB%2BSgfnh0DRRQ7feATpV60vgNAPmIRFwdJVTT5XrOC9TS6cOPI7vmMDyW%2B2dbB0kJvEazzE7YT3e%2FT5gJjsNXSJFTO7tFQAioqyzJPojKSoppFurOchfL7lWtPn1nUwCpJdlceiBUrfpDHgBkLI3Ih2aZf1ft9LVariAJAUs7gchlfnmbu2E2Nos%2FXzIlfIcrMXdFxd6hizfom8cC0om7BY0%2FMAGUm7YdE489ZJoq8IhqADnFuuDIA98262vNb5Jt2ThTP1MBjcZeCjww0qHkSvLIQpB2LdO8WyUZTFeDI0myxEpUkQ6qooDscbhH06kFLr%2FIHNNf4ajq78v0cF07LCPQob%2F3TfkAVGPtP78Wvokb%2BNWC1cUhhlgEe%2Bhx%2FKaG7IClfzDOpK%2B0ZKp6jTv416EqOEfny0kz4ZHCQvEdnv1VGE9OzLaKUq5yvLyKAO0bqBz27yquDh6Dx%2BMfn5IJgdqQmGBrRGt7ThoUcwBbJ952iin1y%2B2DLKotlf%2BKtgM4QCTlRN86UA0ReavdvtyhPhorVTgGyqoh9%2BId9jEM1mhCyel2jdR5WNsFga1YJhxaUgp8QBJoXJg10LUsS%2FGaRu7OHjUhWj5zcw6NGTvQY6pgGQ6sN62ltIq7lb1kHcb16BsgarQBPKbFP6JploKLjbSfJeVJQ0HA7QRBBTAes0BedvdQHmxgN79ZLODR5ocoPeIzm7yGXenLYEgIG9ynxoFpQF3jEG0%2FLmAMcsxtWvIAQ7%2Ft%2BIgWVJAC5QWl6Wf59f5%2F43FXdopF0Vv3SGkSqbyjlkDYPA6pcSzY2Cy0Q44QyNJaaEaVL7vlOc6fia8X0Q7sKP0g%2Fn&X-Amz-Signature=3fd90162b4fea18da4cd4545642c9d4bf0e82f37157ee4e8862f3447ce560ca6&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XS3CUXW%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJGMEQCIFbx%2B%2F1oqLq63YY2pSDTT0pk2Gy3cDFueNffxDF1rTFrAiBUnHIr4G5rT1BpyQmtlU4sZVEm7z0TsQAsKin4M8mzryr%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIMLsKrwouvbD7R2cfiKtwDS9RKBC5%2Bz4%2FEru8NfRYK0WoFXoB%2BSgfnh0DRRQ7feATpV60vgNAPmIRFwdJVTT5XrOC9TS6cOPI7vmMDyW%2B2dbB0kJvEazzE7YT3e%2FT5gJjsNXSJFTO7tFQAioqyzJPojKSoppFurOchfL7lWtPn1nUwCpJdlceiBUrfpDHgBkLI3Ih2aZf1ft9LVariAJAUs7gchlfnmbu2E2Nos%2FXzIlfIcrMXdFxd6hizfom8cC0om7BY0%2FMAGUm7YdE489ZJoq8IhqADnFuuDIA98262vNb5Jt2ThTP1MBjcZeCjww0qHkSvLIQpB2LdO8WyUZTFeDI0myxEpUkQ6qooDscbhH06kFLr%2FIHNNf4ajq78v0cF07LCPQob%2F3TfkAVGPtP78Wvokb%2BNWC1cUhhlgEe%2Bhx%2FKaG7IClfzDOpK%2B0ZKp6jTv416EqOEfny0kz4ZHCQvEdnv1VGE9OzLaKUq5yvLyKAO0bqBz27yquDh6Dx%2BMfn5IJgdqQmGBrRGt7ThoUcwBbJ952iin1y%2B2DLKotlf%2BKtgM4QCTlRN86UA0ReavdvtyhPhorVTgGyqoh9%2BId9jEM1mhCyel2jdR5WNsFga1YJhxaUgp8QBJoXJg10LUsS%2FGaRu7OHjUhWj5zcw6NGTvQY6pgGQ6sN62ltIq7lb1kHcb16BsgarQBPKbFP6JploKLjbSfJeVJQ0HA7QRBBTAes0BedvdQHmxgN79ZLODR5ocoPeIzm7yGXenLYEgIG9ynxoFpQF3jEG0%2FLmAMcsxtWvIAQ7%2Ft%2BIgWVJAC5QWl6Wf59f5%2F43FXdopF0Vv3SGkSqbyjlkDYPA6pcSzY2Cy0Q44QyNJaaEaVL7vlOc6fia8X0Q7sKP0g%2Fn&X-Amz-Signature=c8ecb5459611c86fd7017396b32b6917a767f25ac3d9f0e9bdb912b40988a178&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XS3CUXW%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJGMEQCIFbx%2B%2F1oqLq63YY2pSDTT0pk2Gy3cDFueNffxDF1rTFrAiBUnHIr4G5rT1BpyQmtlU4sZVEm7z0TsQAsKin4M8mzryr%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIMLsKrwouvbD7R2cfiKtwDS9RKBC5%2Bz4%2FEru8NfRYK0WoFXoB%2BSgfnh0DRRQ7feATpV60vgNAPmIRFwdJVTT5XrOC9TS6cOPI7vmMDyW%2B2dbB0kJvEazzE7YT3e%2FT5gJjsNXSJFTO7tFQAioqyzJPojKSoppFurOchfL7lWtPn1nUwCpJdlceiBUrfpDHgBkLI3Ih2aZf1ft9LVariAJAUs7gchlfnmbu2E2Nos%2FXzIlfIcrMXdFxd6hizfom8cC0om7BY0%2FMAGUm7YdE489ZJoq8IhqADnFuuDIA98262vNb5Jt2ThTP1MBjcZeCjww0qHkSvLIQpB2LdO8WyUZTFeDI0myxEpUkQ6qooDscbhH06kFLr%2FIHNNf4ajq78v0cF07LCPQob%2F3TfkAVGPtP78Wvokb%2BNWC1cUhhlgEe%2Bhx%2FKaG7IClfzDOpK%2B0ZKp6jTv416EqOEfny0kz4ZHCQvEdnv1VGE9OzLaKUq5yvLyKAO0bqBz27yquDh6Dx%2BMfn5IJgdqQmGBrRGt7ThoUcwBbJ952iin1y%2B2DLKotlf%2BKtgM4QCTlRN86UA0ReavdvtyhPhorVTgGyqoh9%2BId9jEM1mhCyel2jdR5WNsFga1YJhxaUgp8QBJoXJg10LUsS%2FGaRu7OHjUhWj5zcw6NGTvQY6pgGQ6sN62ltIq7lb1kHcb16BsgarQBPKbFP6JploKLjbSfJeVJQ0HA7QRBBTAes0BedvdQHmxgN79ZLODR5ocoPeIzm7yGXenLYEgIG9ynxoFpQF3jEG0%2FLmAMcsxtWvIAQ7%2Ft%2BIgWVJAC5QWl6Wf59f5%2F43FXdopF0Vv3SGkSqbyjlkDYPA6pcSzY2Cy0Q44QyNJaaEaVL7vlOc6fia8X0Q7sKP0g%2Fn&X-Amz-Signature=4b705923d96bc538bd93e436cf527fd42894663c8769df95749712ce013a8085&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XS3CUXW%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJGMEQCIFbx%2B%2F1oqLq63YY2pSDTT0pk2Gy3cDFueNffxDF1rTFrAiBUnHIr4G5rT1BpyQmtlU4sZVEm7z0TsQAsKin4M8mzryr%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIMLsKrwouvbD7R2cfiKtwDS9RKBC5%2Bz4%2FEru8NfRYK0WoFXoB%2BSgfnh0DRRQ7feATpV60vgNAPmIRFwdJVTT5XrOC9TS6cOPI7vmMDyW%2B2dbB0kJvEazzE7YT3e%2FT5gJjsNXSJFTO7tFQAioqyzJPojKSoppFurOchfL7lWtPn1nUwCpJdlceiBUrfpDHgBkLI3Ih2aZf1ft9LVariAJAUs7gchlfnmbu2E2Nos%2FXzIlfIcrMXdFxd6hizfom8cC0om7BY0%2FMAGUm7YdE489ZJoq8IhqADnFuuDIA98262vNb5Jt2ThTP1MBjcZeCjww0qHkSvLIQpB2LdO8WyUZTFeDI0myxEpUkQ6qooDscbhH06kFLr%2FIHNNf4ajq78v0cF07LCPQob%2F3TfkAVGPtP78Wvokb%2BNWC1cUhhlgEe%2Bhx%2FKaG7IClfzDOpK%2B0ZKp6jTv416EqOEfny0kz4ZHCQvEdnv1VGE9OzLaKUq5yvLyKAO0bqBz27yquDh6Dx%2BMfn5IJgdqQmGBrRGt7ThoUcwBbJ952iin1y%2B2DLKotlf%2BKtgM4QCTlRN86UA0ReavdvtyhPhorVTgGyqoh9%2BId9jEM1mhCyel2jdR5WNsFga1YJhxaUgp8QBJoXJg10LUsS%2FGaRu7OHjUhWj5zcw6NGTvQY6pgGQ6sN62ltIq7lb1kHcb16BsgarQBPKbFP6JploKLjbSfJeVJQ0HA7QRBBTAes0BedvdQHmxgN79ZLODR5ocoPeIzm7yGXenLYEgIG9ynxoFpQF3jEG0%2FLmAMcsxtWvIAQ7%2Ft%2BIgWVJAC5QWl6Wf59f5%2F43FXdopF0Vv3SGkSqbyjlkDYPA6pcSzY2Cy0Q44QyNJaaEaVL7vlOc6fia8X0Q7sKP0g%2Fn&X-Amz-Signature=e10a0a5b24661465ff7d872c696de2107c7d63daafbb1bf2cc9634a2ebefe425&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XS3CUXW%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJGMEQCIFbx%2B%2F1oqLq63YY2pSDTT0pk2Gy3cDFueNffxDF1rTFrAiBUnHIr4G5rT1BpyQmtlU4sZVEm7z0TsQAsKin4M8mzryr%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIMLsKrwouvbD7R2cfiKtwDS9RKBC5%2Bz4%2FEru8NfRYK0WoFXoB%2BSgfnh0DRRQ7feATpV60vgNAPmIRFwdJVTT5XrOC9TS6cOPI7vmMDyW%2B2dbB0kJvEazzE7YT3e%2FT5gJjsNXSJFTO7tFQAioqyzJPojKSoppFurOchfL7lWtPn1nUwCpJdlceiBUrfpDHgBkLI3Ih2aZf1ft9LVariAJAUs7gchlfnmbu2E2Nos%2FXzIlfIcrMXdFxd6hizfom8cC0om7BY0%2FMAGUm7YdE489ZJoq8IhqADnFuuDIA98262vNb5Jt2ThTP1MBjcZeCjww0qHkSvLIQpB2LdO8WyUZTFeDI0myxEpUkQ6qooDscbhH06kFLr%2FIHNNf4ajq78v0cF07LCPQob%2F3TfkAVGPtP78Wvokb%2BNWC1cUhhlgEe%2Bhx%2FKaG7IClfzDOpK%2B0ZKp6jTv416EqOEfny0kz4ZHCQvEdnv1VGE9OzLaKUq5yvLyKAO0bqBz27yquDh6Dx%2BMfn5IJgdqQmGBrRGt7ThoUcwBbJ952iin1y%2B2DLKotlf%2BKtgM4QCTlRN86UA0ReavdvtyhPhorVTgGyqoh9%2BId9jEM1mhCyel2jdR5WNsFga1YJhxaUgp8QBJoXJg10LUsS%2FGaRu7OHjUhWj5zcw6NGTvQY6pgGQ6sN62ltIq7lb1kHcb16BsgarQBPKbFP6JploKLjbSfJeVJQ0HA7QRBBTAes0BedvdQHmxgN79ZLODR5ocoPeIzm7yGXenLYEgIG9ynxoFpQF3jEG0%2FLmAMcsxtWvIAQ7%2Ft%2BIgWVJAC5QWl6Wf59f5%2F43FXdopF0Vv3SGkSqbyjlkDYPA6pcSzY2Cy0Q44QyNJaaEaVL7vlOc6fia8X0Q7sKP0g%2Fn&X-Amz-Signature=75aadab0d96e57bbb57c0f362b0949333f854765347723c71faba98a8341f2cb&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XS3CUXW%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJGMEQCIFbx%2B%2F1oqLq63YY2pSDTT0pk2Gy3cDFueNffxDF1rTFrAiBUnHIr4G5rT1BpyQmtlU4sZVEm7z0TsQAsKin4M8mzryr%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIMLsKrwouvbD7R2cfiKtwDS9RKBC5%2Bz4%2FEru8NfRYK0WoFXoB%2BSgfnh0DRRQ7feATpV60vgNAPmIRFwdJVTT5XrOC9TS6cOPI7vmMDyW%2B2dbB0kJvEazzE7YT3e%2FT5gJjsNXSJFTO7tFQAioqyzJPojKSoppFurOchfL7lWtPn1nUwCpJdlceiBUrfpDHgBkLI3Ih2aZf1ft9LVariAJAUs7gchlfnmbu2E2Nos%2FXzIlfIcrMXdFxd6hizfom8cC0om7BY0%2FMAGUm7YdE489ZJoq8IhqADnFuuDIA98262vNb5Jt2ThTP1MBjcZeCjww0qHkSvLIQpB2LdO8WyUZTFeDI0myxEpUkQ6qooDscbhH06kFLr%2FIHNNf4ajq78v0cF07LCPQob%2F3TfkAVGPtP78Wvokb%2BNWC1cUhhlgEe%2Bhx%2FKaG7IClfzDOpK%2B0ZKp6jTv416EqOEfny0kz4ZHCQvEdnv1VGE9OzLaKUq5yvLyKAO0bqBz27yquDh6Dx%2BMfn5IJgdqQmGBrRGt7ThoUcwBbJ952iin1y%2B2DLKotlf%2BKtgM4QCTlRN86UA0ReavdvtyhPhorVTgGyqoh9%2BId9jEM1mhCyel2jdR5WNsFga1YJhxaUgp8QBJoXJg10LUsS%2FGaRu7OHjUhWj5zcw6NGTvQY6pgGQ6sN62ltIq7lb1kHcb16BsgarQBPKbFP6JploKLjbSfJeVJQ0HA7QRBBTAes0BedvdQHmxgN79ZLODR5ocoPeIzm7yGXenLYEgIG9ynxoFpQF3jEG0%2FLmAMcsxtWvIAQ7%2Ft%2BIgWVJAC5QWl6Wf59f5%2F43FXdopF0Vv3SGkSqbyjlkDYPA6pcSzY2Cy0Q44QyNJaaEaVL7vlOc6fia8X0Q7sKP0g%2Fn&X-Amz-Signature=b555412ac661b7288beddf113337256d266df3fc3ec3dcffca04da8b9e03b35c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XS3CUXW%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJGMEQCIFbx%2B%2F1oqLq63YY2pSDTT0pk2Gy3cDFueNffxDF1rTFrAiBUnHIr4G5rT1BpyQmtlU4sZVEm7z0TsQAsKin4M8mzryr%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIMLsKrwouvbD7R2cfiKtwDS9RKBC5%2Bz4%2FEru8NfRYK0WoFXoB%2BSgfnh0DRRQ7feATpV60vgNAPmIRFwdJVTT5XrOC9TS6cOPI7vmMDyW%2B2dbB0kJvEazzE7YT3e%2FT5gJjsNXSJFTO7tFQAioqyzJPojKSoppFurOchfL7lWtPn1nUwCpJdlceiBUrfpDHgBkLI3Ih2aZf1ft9LVariAJAUs7gchlfnmbu2E2Nos%2FXzIlfIcrMXdFxd6hizfom8cC0om7BY0%2FMAGUm7YdE489ZJoq8IhqADnFuuDIA98262vNb5Jt2ThTP1MBjcZeCjww0qHkSvLIQpB2LdO8WyUZTFeDI0myxEpUkQ6qooDscbhH06kFLr%2FIHNNf4ajq78v0cF07LCPQob%2F3TfkAVGPtP78Wvokb%2BNWC1cUhhlgEe%2Bhx%2FKaG7IClfzDOpK%2B0ZKp6jTv416EqOEfny0kz4ZHCQvEdnv1VGE9OzLaKUq5yvLyKAO0bqBz27yquDh6Dx%2BMfn5IJgdqQmGBrRGt7ThoUcwBbJ952iin1y%2B2DLKotlf%2BKtgM4QCTlRN86UA0ReavdvtyhPhorVTgGyqoh9%2BId9jEM1mhCyel2jdR5WNsFga1YJhxaUgp8QBJoXJg10LUsS%2FGaRu7OHjUhWj5zcw6NGTvQY6pgGQ6sN62ltIq7lb1kHcb16BsgarQBPKbFP6JploKLjbSfJeVJQ0HA7QRBBTAes0BedvdQHmxgN79ZLODR5ocoPeIzm7yGXenLYEgIG9ynxoFpQF3jEG0%2FLmAMcsxtWvIAQ7%2Ft%2BIgWVJAC5QWl6Wf59f5%2F43FXdopF0Vv3SGkSqbyjlkDYPA6pcSzY2Cy0Q44QyNJaaEaVL7vlOc6fia8X0Q7sKP0g%2Fn&X-Amz-Signature=fe421a6fa52384ba04097ca8dbd9a3cd52909cae408794dd0b681b95b551ce36&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XS3CUXW%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJGMEQCIFbx%2B%2F1oqLq63YY2pSDTT0pk2Gy3cDFueNffxDF1rTFrAiBUnHIr4G5rT1BpyQmtlU4sZVEm7z0TsQAsKin4M8mzryr%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIMLsKrwouvbD7R2cfiKtwDS9RKBC5%2Bz4%2FEru8NfRYK0WoFXoB%2BSgfnh0DRRQ7feATpV60vgNAPmIRFwdJVTT5XrOC9TS6cOPI7vmMDyW%2B2dbB0kJvEazzE7YT3e%2FT5gJjsNXSJFTO7tFQAioqyzJPojKSoppFurOchfL7lWtPn1nUwCpJdlceiBUrfpDHgBkLI3Ih2aZf1ft9LVariAJAUs7gchlfnmbu2E2Nos%2FXzIlfIcrMXdFxd6hizfom8cC0om7BY0%2FMAGUm7YdE489ZJoq8IhqADnFuuDIA98262vNb5Jt2ThTP1MBjcZeCjww0qHkSvLIQpB2LdO8WyUZTFeDI0myxEpUkQ6qooDscbhH06kFLr%2FIHNNf4ajq78v0cF07LCPQob%2F3TfkAVGPtP78Wvokb%2BNWC1cUhhlgEe%2Bhx%2FKaG7IClfzDOpK%2B0ZKp6jTv416EqOEfny0kz4ZHCQvEdnv1VGE9OzLaKUq5yvLyKAO0bqBz27yquDh6Dx%2BMfn5IJgdqQmGBrRGt7ThoUcwBbJ952iin1y%2B2DLKotlf%2BKtgM4QCTlRN86UA0ReavdvtyhPhorVTgGyqoh9%2BId9jEM1mhCyel2jdR5WNsFga1YJhxaUgp8QBJoXJg10LUsS%2FGaRu7OHjUhWj5zcw6NGTvQY6pgGQ6sN62ltIq7lb1kHcb16BsgarQBPKbFP6JploKLjbSfJeVJQ0HA7QRBBTAes0BedvdQHmxgN79ZLODR5ocoPeIzm7yGXenLYEgIG9ynxoFpQF3jEG0%2FLmAMcsxtWvIAQ7%2Ft%2BIgWVJAC5QWl6Wf59f5%2F43FXdopF0Vv3SGkSqbyjlkDYPA6pcSzY2Cy0Q44QyNJaaEaVL7vlOc6fia8X0Q7sKP0g%2Fn&X-Amz-Signature=c8daef3a126dfcd4d5b4798e0afcc1f346c41298f4f0b2399754c5918d142d80&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XD4G3NTQ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJIMEYCIQDVARiSDu7A1fgwQSTfEFf2L2d49ghuthor9wMK0t0YpQIhAOm%2BVzfMy%2FtzHWmgnHN5tuztt1j0osAga60OvwKVPz9IKv8DCGIQABoMNjM3NDIzMTgzODA1IgzCcOslYaP0f057Pz0q3AOe1lixNYPspri4jhVUBaPF6Vo1A8rB5lejp9m9M6%2BULYAacgGWaqEA4E3SQPX%2FgEQl%2F13%2FYqRvB%2Be2QzrHn6%2FryZ8PtbMGcnm%2BV9B2%2FQ090Ri6xzutyB6nz4RzSonMwX0ZNalLXfzP6n7cMjn3rSAqqj5prSz1U4tvEOtUNvD4tP%2FN3JxtXA9Ij31zXXgRSkWQV3g6al%2BriFeCVdXx3VkZ4Rh2EnshZ08rDbsnY6Mu3omIFWvtZ%2B3hRaZOXTDeVQHjaccosjGw9oWonFfG%2BR9NoBHuFt0jUjWGt5s7KkuH2GMIWUS655%2BcrTGeGkKgTm5z36d7NY3vx85QAfPQ4fblmdYSYKpJ9YcMsDPPDW02E194iQyUyGfXEldBOS9c7y8iOl6q%2Bf73pw8M2y2MEcI9U7eptb44SjLle7pXagjRrCNszT%2FZwWcqq3DJ7GBpVSZY8FgBjBCWTy%2FXtRdQ0OPZem%2FA7ZkWhNBSKiP%2FYfEmclaINi79GCsuyLCjfD1WGuDsVTLmF1eWUdPZMXrq9reI8pXJXsG8ENKjTbukzuaz%2BCtJwvamU8Lf7goSp2Hry0YJWm%2Fs460aKjPjZauCw%2FZEq3lniQ1eC7mGGKW5FVR76QzNRH9tBDj9gjWRgTDG0ZO9BjqkAfX%2BSLPerqV9yRrFaAfHR6lyKjti0OVHc4eXt3V0ZbacHGXm2NzymUweuPNEsn%2B4XAzbEdPk2Pc3COdENy3Y0jdURi8osNKIROHoicDNZT0N3qDPOM%2FlB84ZupTox76Jq56YdwqGwqGRxcLQEzN9DpUcy2INbS28omP89HXcigtx1PotsrgcrGjt1Gv7nogvVuoNw1wi2CvW71Ma4Rm0ThwmBID3&X-Amz-Signature=64b4f50628382a2248f2e29446bc202749372748157a61f9e79ceda673d6e0f7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XD4G3NTQ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJIMEYCIQDVARiSDu7A1fgwQSTfEFf2L2d49ghuthor9wMK0t0YpQIhAOm%2BVzfMy%2FtzHWmgnHN5tuztt1j0osAga60OvwKVPz9IKv8DCGIQABoMNjM3NDIzMTgzODA1IgzCcOslYaP0f057Pz0q3AOe1lixNYPspri4jhVUBaPF6Vo1A8rB5lejp9m9M6%2BULYAacgGWaqEA4E3SQPX%2FgEQl%2F13%2FYqRvB%2Be2QzrHn6%2FryZ8PtbMGcnm%2BV9B2%2FQ090Ri6xzutyB6nz4RzSonMwX0ZNalLXfzP6n7cMjn3rSAqqj5prSz1U4tvEOtUNvD4tP%2FN3JxtXA9Ij31zXXgRSkWQV3g6al%2BriFeCVdXx3VkZ4Rh2EnshZ08rDbsnY6Mu3omIFWvtZ%2B3hRaZOXTDeVQHjaccosjGw9oWonFfG%2BR9NoBHuFt0jUjWGt5s7KkuH2GMIWUS655%2BcrTGeGkKgTm5z36d7NY3vx85QAfPQ4fblmdYSYKpJ9YcMsDPPDW02E194iQyUyGfXEldBOS9c7y8iOl6q%2Bf73pw8M2y2MEcI9U7eptb44SjLle7pXagjRrCNszT%2FZwWcqq3DJ7GBpVSZY8FgBjBCWTy%2FXtRdQ0OPZem%2FA7ZkWhNBSKiP%2FYfEmclaINi79GCsuyLCjfD1WGuDsVTLmF1eWUdPZMXrq9reI8pXJXsG8ENKjTbukzuaz%2BCtJwvamU8Lf7goSp2Hry0YJWm%2Fs460aKjPjZauCw%2FZEq3lniQ1eC7mGGKW5FVR76QzNRH9tBDj9gjWRgTDG0ZO9BjqkAfX%2BSLPerqV9yRrFaAfHR6lyKjti0OVHc4eXt3V0ZbacHGXm2NzymUweuPNEsn%2B4XAzbEdPk2Pc3COdENy3Y0jdURi8osNKIROHoicDNZT0N3qDPOM%2FlB84ZupTox76Jq56YdwqGwqGRxcLQEzN9DpUcy2INbS28omP89HXcigtx1PotsrgcrGjt1Gv7nogvVuoNw1wi2CvW71Ma4Rm0ThwmBID3&X-Amz-Signature=75b9ee208b28002002b4524e673d7057681597e9b2f70f6cfa5a68cac94d54a9&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
