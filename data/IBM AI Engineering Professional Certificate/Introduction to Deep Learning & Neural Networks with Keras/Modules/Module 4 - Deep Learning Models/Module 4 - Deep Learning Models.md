

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YNSO6EVT%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJHMEUCIHznwjoPRV3tMVmGKy%2BCDOSektKmfHR71Ct0nEHQFMynAiEA3D1jjILeAaexYfDKQnZYqn8x8g5EtELWX6cA751emg8qiAQIsf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMKR%2Bgdcea8qlm6PxSrcA%2Bh5feGYHszLUCon6CY43W2qE7eay5InDv26ugSy1TmymXd%2Foz7dG2rYooG5AECE8Ina7eJ98JqHiQnbDHEWOXhDiUdHC%2FEmijIiarY2tbc%2B8ZpMxG0FcATJXSf5yg2su2yIvJU9F%2B%2Fs98dh8bxZkvPDlrtkQq4M7NsNY7vepOYgNvgKHkW8%2BxE5qRy7NgaNDXLFiUe2jErPKuA%2Fu3twKVLzD6v4lkvoyEfp52fewi7UY8%2FPfTrYUpb6Aw3hl18sRmOPKiiJDBD3k2qZmp7M87%2F5Ply6kSsjWVg%2BTvGOoa%2BfDj5tQaV%2FxRMh7HUofrASeb9qsjszJuGqCTXUcSpOTU49ohoG%2Bjt2p%2FNscgYNmkz4CQteXYJ%2B9vgbLebpsvr7%2F8dIjE%2F8CX%2BTVJMTjSu8sgNQO1VjTRka0s2uBfYOpgZ7cHYLMsqRFwDFNF54qAPXCyPOrhPRFBpqTFtmKM6kQgg66b2BH4pn8NhyvzBmhV33fsehwngii4Hvw9cvkDX1CvlORY4X6rFKfxgVDXNAR89kz2OTvEzzx2rM1kfmQXDHXoojg5105gfEooZKnB%2BcrqIl4hvuDlQwAycqw%2BWcTG8Pr5APo65sIDPSCMzFyXEEekuL4NoW5j4ur6mzMPG3jr4GOqUB%2B%2Bp4kutmZORG9u6m0YXK4tSsu%2Fgo3Q9UlL5ZU1%2Fu%2F8jmT775Q4d%2FKDnQqO6wGBgB7uXWVbAPHAc2l5nmX53Wx%2FIhgvVy8M1VDaCgdbG%2FFaz%2BfB2DZWNhXAOCI%2BInX9%2FeNaUP5KYlAI8NkOXOa%2FKhyUCjzimH2fNKejXevX5NCt%2FQkQeRZNsXrRSUHdUT9twQYD%2B8%2F%2FUsBT0LGNNK9m4X5VotU6Oh&X-Amz-Signature=ce638e1a4dfd3d0c4bfbf8b414086c259e34f707a57ef3862801530ca1b098ad&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YNSO6EVT%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJHMEUCIHznwjoPRV3tMVmGKy%2BCDOSektKmfHR71Ct0nEHQFMynAiEA3D1jjILeAaexYfDKQnZYqn8x8g5EtELWX6cA751emg8qiAQIsf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMKR%2Bgdcea8qlm6PxSrcA%2Bh5feGYHszLUCon6CY43W2qE7eay5InDv26ugSy1TmymXd%2Foz7dG2rYooG5AECE8Ina7eJ98JqHiQnbDHEWOXhDiUdHC%2FEmijIiarY2tbc%2B8ZpMxG0FcATJXSf5yg2su2yIvJU9F%2B%2Fs98dh8bxZkvPDlrtkQq4M7NsNY7vepOYgNvgKHkW8%2BxE5qRy7NgaNDXLFiUe2jErPKuA%2Fu3twKVLzD6v4lkvoyEfp52fewi7UY8%2FPfTrYUpb6Aw3hl18sRmOPKiiJDBD3k2qZmp7M87%2F5Ply6kSsjWVg%2BTvGOoa%2BfDj5tQaV%2FxRMh7HUofrASeb9qsjszJuGqCTXUcSpOTU49ohoG%2Bjt2p%2FNscgYNmkz4CQteXYJ%2B9vgbLebpsvr7%2F8dIjE%2F8CX%2BTVJMTjSu8sgNQO1VjTRka0s2uBfYOpgZ7cHYLMsqRFwDFNF54qAPXCyPOrhPRFBpqTFtmKM6kQgg66b2BH4pn8NhyvzBmhV33fsehwngii4Hvw9cvkDX1CvlORY4X6rFKfxgVDXNAR89kz2OTvEzzx2rM1kfmQXDHXoojg5105gfEooZKnB%2BcrqIl4hvuDlQwAycqw%2BWcTG8Pr5APo65sIDPSCMzFyXEEekuL4NoW5j4ur6mzMPG3jr4GOqUB%2B%2Bp4kutmZORG9u6m0YXK4tSsu%2Fgo3Q9UlL5ZU1%2Fu%2F8jmT775Q4d%2FKDnQqO6wGBgB7uXWVbAPHAc2l5nmX53Wx%2FIhgvVy8M1VDaCgdbG%2FFaz%2BfB2DZWNhXAOCI%2BInX9%2FeNaUP5KYlAI8NkOXOa%2FKhyUCjzimH2fNKejXevX5NCt%2FQkQeRZNsXrRSUHdUT9twQYD%2B8%2F%2FUsBT0LGNNK9m4X5VotU6Oh&X-Amz-Signature=73e40767dd21699f9b900eb19fc9bfbf5e2360138f6a0459f2093a23b936ac9b&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YNSO6EVT%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJHMEUCIHznwjoPRV3tMVmGKy%2BCDOSektKmfHR71Ct0nEHQFMynAiEA3D1jjILeAaexYfDKQnZYqn8x8g5EtELWX6cA751emg8qiAQIsf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMKR%2Bgdcea8qlm6PxSrcA%2Bh5feGYHszLUCon6CY43W2qE7eay5InDv26ugSy1TmymXd%2Foz7dG2rYooG5AECE8Ina7eJ98JqHiQnbDHEWOXhDiUdHC%2FEmijIiarY2tbc%2B8ZpMxG0FcATJXSf5yg2su2yIvJU9F%2B%2Fs98dh8bxZkvPDlrtkQq4M7NsNY7vepOYgNvgKHkW8%2BxE5qRy7NgaNDXLFiUe2jErPKuA%2Fu3twKVLzD6v4lkvoyEfp52fewi7UY8%2FPfTrYUpb6Aw3hl18sRmOPKiiJDBD3k2qZmp7M87%2F5Ply6kSsjWVg%2BTvGOoa%2BfDj5tQaV%2FxRMh7HUofrASeb9qsjszJuGqCTXUcSpOTU49ohoG%2Bjt2p%2FNscgYNmkz4CQteXYJ%2B9vgbLebpsvr7%2F8dIjE%2F8CX%2BTVJMTjSu8sgNQO1VjTRka0s2uBfYOpgZ7cHYLMsqRFwDFNF54qAPXCyPOrhPRFBpqTFtmKM6kQgg66b2BH4pn8NhyvzBmhV33fsehwngii4Hvw9cvkDX1CvlORY4X6rFKfxgVDXNAR89kz2OTvEzzx2rM1kfmQXDHXoojg5105gfEooZKnB%2BcrqIl4hvuDlQwAycqw%2BWcTG8Pr5APo65sIDPSCMzFyXEEekuL4NoW5j4ur6mzMPG3jr4GOqUB%2B%2Bp4kutmZORG9u6m0YXK4tSsu%2Fgo3Q9UlL5ZU1%2Fu%2F8jmT775Q4d%2FKDnQqO6wGBgB7uXWVbAPHAc2l5nmX53Wx%2FIhgvVy8M1VDaCgdbG%2FFaz%2BfB2DZWNhXAOCI%2BInX9%2FeNaUP5KYlAI8NkOXOa%2FKhyUCjzimH2fNKejXevX5NCt%2FQkQeRZNsXrRSUHdUT9twQYD%2B8%2F%2FUsBT0LGNNK9m4X5VotU6Oh&X-Amz-Signature=8b4fd8785076988a5e2279193a5c1d58731bd49000130b7fe8a51111fc217c5f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YNSO6EVT%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJHMEUCIHznwjoPRV3tMVmGKy%2BCDOSektKmfHR71Ct0nEHQFMynAiEA3D1jjILeAaexYfDKQnZYqn8x8g5EtELWX6cA751emg8qiAQIsf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMKR%2Bgdcea8qlm6PxSrcA%2Bh5feGYHszLUCon6CY43W2qE7eay5InDv26ugSy1TmymXd%2Foz7dG2rYooG5AECE8Ina7eJ98JqHiQnbDHEWOXhDiUdHC%2FEmijIiarY2tbc%2B8ZpMxG0FcATJXSf5yg2su2yIvJU9F%2B%2Fs98dh8bxZkvPDlrtkQq4M7NsNY7vepOYgNvgKHkW8%2BxE5qRy7NgaNDXLFiUe2jErPKuA%2Fu3twKVLzD6v4lkvoyEfp52fewi7UY8%2FPfTrYUpb6Aw3hl18sRmOPKiiJDBD3k2qZmp7M87%2F5Ply6kSsjWVg%2BTvGOoa%2BfDj5tQaV%2FxRMh7HUofrASeb9qsjszJuGqCTXUcSpOTU49ohoG%2Bjt2p%2FNscgYNmkz4CQteXYJ%2B9vgbLebpsvr7%2F8dIjE%2F8CX%2BTVJMTjSu8sgNQO1VjTRka0s2uBfYOpgZ7cHYLMsqRFwDFNF54qAPXCyPOrhPRFBpqTFtmKM6kQgg66b2BH4pn8NhyvzBmhV33fsehwngii4Hvw9cvkDX1CvlORY4X6rFKfxgVDXNAR89kz2OTvEzzx2rM1kfmQXDHXoojg5105gfEooZKnB%2BcrqIl4hvuDlQwAycqw%2BWcTG8Pr5APo65sIDPSCMzFyXEEekuL4NoW5j4ur6mzMPG3jr4GOqUB%2B%2Bp4kutmZORG9u6m0YXK4tSsu%2Fgo3Q9UlL5ZU1%2Fu%2F8jmT775Q4d%2FKDnQqO6wGBgB7uXWVbAPHAc2l5nmX53Wx%2FIhgvVy8M1VDaCgdbG%2FFaz%2BfB2DZWNhXAOCI%2BInX9%2FeNaUP5KYlAI8NkOXOa%2FKhyUCjzimH2fNKejXevX5NCt%2FQkQeRZNsXrRSUHdUT9twQYD%2B8%2F%2FUsBT0LGNNK9m4X5VotU6Oh&X-Amz-Signature=360f8795932ad119f453c0ebfa392f3b395020e917e6291582d8f1cfa97531ff&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YNSO6EVT%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJHMEUCIHznwjoPRV3tMVmGKy%2BCDOSektKmfHR71Ct0nEHQFMynAiEA3D1jjILeAaexYfDKQnZYqn8x8g5EtELWX6cA751emg8qiAQIsf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMKR%2Bgdcea8qlm6PxSrcA%2Bh5feGYHszLUCon6CY43W2qE7eay5InDv26ugSy1TmymXd%2Foz7dG2rYooG5AECE8Ina7eJ98JqHiQnbDHEWOXhDiUdHC%2FEmijIiarY2tbc%2B8ZpMxG0FcATJXSf5yg2su2yIvJU9F%2B%2Fs98dh8bxZkvPDlrtkQq4M7NsNY7vepOYgNvgKHkW8%2BxE5qRy7NgaNDXLFiUe2jErPKuA%2Fu3twKVLzD6v4lkvoyEfp52fewi7UY8%2FPfTrYUpb6Aw3hl18sRmOPKiiJDBD3k2qZmp7M87%2F5Ply6kSsjWVg%2BTvGOoa%2BfDj5tQaV%2FxRMh7HUofrASeb9qsjszJuGqCTXUcSpOTU49ohoG%2Bjt2p%2FNscgYNmkz4CQteXYJ%2B9vgbLebpsvr7%2F8dIjE%2F8CX%2BTVJMTjSu8sgNQO1VjTRka0s2uBfYOpgZ7cHYLMsqRFwDFNF54qAPXCyPOrhPRFBpqTFtmKM6kQgg66b2BH4pn8NhyvzBmhV33fsehwngii4Hvw9cvkDX1CvlORY4X6rFKfxgVDXNAR89kz2OTvEzzx2rM1kfmQXDHXoojg5105gfEooZKnB%2BcrqIl4hvuDlQwAycqw%2BWcTG8Pr5APo65sIDPSCMzFyXEEekuL4NoW5j4ur6mzMPG3jr4GOqUB%2B%2Bp4kutmZORG9u6m0YXK4tSsu%2Fgo3Q9UlL5ZU1%2Fu%2F8jmT775Q4d%2FKDnQqO6wGBgB7uXWVbAPHAc2l5nmX53Wx%2FIhgvVy8M1VDaCgdbG%2FFaz%2BfB2DZWNhXAOCI%2BInX9%2FeNaUP5KYlAI8NkOXOa%2FKhyUCjzimH2fNKejXevX5NCt%2FQkQeRZNsXrRSUHdUT9twQYD%2B8%2F%2FUsBT0LGNNK9m4X5VotU6Oh&X-Amz-Signature=b73783c2928b231bb0f2ad966cea22578f2592f68129dced6834f7da8ad83a43&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YNSO6EVT%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJHMEUCIHznwjoPRV3tMVmGKy%2BCDOSektKmfHR71Ct0nEHQFMynAiEA3D1jjILeAaexYfDKQnZYqn8x8g5EtELWX6cA751emg8qiAQIsf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMKR%2Bgdcea8qlm6PxSrcA%2Bh5feGYHszLUCon6CY43W2qE7eay5InDv26ugSy1TmymXd%2Foz7dG2rYooG5AECE8Ina7eJ98JqHiQnbDHEWOXhDiUdHC%2FEmijIiarY2tbc%2B8ZpMxG0FcATJXSf5yg2su2yIvJU9F%2B%2Fs98dh8bxZkvPDlrtkQq4M7NsNY7vepOYgNvgKHkW8%2BxE5qRy7NgaNDXLFiUe2jErPKuA%2Fu3twKVLzD6v4lkvoyEfp52fewi7UY8%2FPfTrYUpb6Aw3hl18sRmOPKiiJDBD3k2qZmp7M87%2F5Ply6kSsjWVg%2BTvGOoa%2BfDj5tQaV%2FxRMh7HUofrASeb9qsjszJuGqCTXUcSpOTU49ohoG%2Bjt2p%2FNscgYNmkz4CQteXYJ%2B9vgbLebpsvr7%2F8dIjE%2F8CX%2BTVJMTjSu8sgNQO1VjTRka0s2uBfYOpgZ7cHYLMsqRFwDFNF54qAPXCyPOrhPRFBpqTFtmKM6kQgg66b2BH4pn8NhyvzBmhV33fsehwngii4Hvw9cvkDX1CvlORY4X6rFKfxgVDXNAR89kz2OTvEzzx2rM1kfmQXDHXoojg5105gfEooZKnB%2BcrqIl4hvuDlQwAycqw%2BWcTG8Pr5APo65sIDPSCMzFyXEEekuL4NoW5j4ur6mzMPG3jr4GOqUB%2B%2Bp4kutmZORG9u6m0YXK4tSsu%2Fgo3Q9UlL5ZU1%2Fu%2F8jmT775Q4d%2FKDnQqO6wGBgB7uXWVbAPHAc2l5nmX53Wx%2FIhgvVy8M1VDaCgdbG%2FFaz%2BfB2DZWNhXAOCI%2BInX9%2FeNaUP5KYlAI8NkOXOa%2FKhyUCjzimH2fNKejXevX5NCt%2FQkQeRZNsXrRSUHdUT9twQYD%2B8%2F%2FUsBT0LGNNK9m4X5VotU6Oh&X-Amz-Signature=ddff2b8d21a2982dd78166cafd79406246f78b232f32b5cf6b805895c5df849a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YNSO6EVT%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJHMEUCIHznwjoPRV3tMVmGKy%2BCDOSektKmfHR71Ct0nEHQFMynAiEA3D1jjILeAaexYfDKQnZYqn8x8g5EtELWX6cA751emg8qiAQIsf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMKR%2Bgdcea8qlm6PxSrcA%2Bh5feGYHszLUCon6CY43W2qE7eay5InDv26ugSy1TmymXd%2Foz7dG2rYooG5AECE8Ina7eJ98JqHiQnbDHEWOXhDiUdHC%2FEmijIiarY2tbc%2B8ZpMxG0FcATJXSf5yg2su2yIvJU9F%2B%2Fs98dh8bxZkvPDlrtkQq4M7NsNY7vepOYgNvgKHkW8%2BxE5qRy7NgaNDXLFiUe2jErPKuA%2Fu3twKVLzD6v4lkvoyEfp52fewi7UY8%2FPfTrYUpb6Aw3hl18sRmOPKiiJDBD3k2qZmp7M87%2F5Ply6kSsjWVg%2BTvGOoa%2BfDj5tQaV%2FxRMh7HUofrASeb9qsjszJuGqCTXUcSpOTU49ohoG%2Bjt2p%2FNscgYNmkz4CQteXYJ%2B9vgbLebpsvr7%2F8dIjE%2F8CX%2BTVJMTjSu8sgNQO1VjTRka0s2uBfYOpgZ7cHYLMsqRFwDFNF54qAPXCyPOrhPRFBpqTFtmKM6kQgg66b2BH4pn8NhyvzBmhV33fsehwngii4Hvw9cvkDX1CvlORY4X6rFKfxgVDXNAR89kz2OTvEzzx2rM1kfmQXDHXoojg5105gfEooZKnB%2BcrqIl4hvuDlQwAycqw%2BWcTG8Pr5APo65sIDPSCMzFyXEEekuL4NoW5j4ur6mzMPG3jr4GOqUB%2B%2Bp4kutmZORG9u6m0YXK4tSsu%2Fgo3Q9UlL5ZU1%2Fu%2F8jmT775Q4d%2FKDnQqO6wGBgB7uXWVbAPHAc2l5nmX53Wx%2FIhgvVy8M1VDaCgdbG%2FFaz%2BfB2DZWNhXAOCI%2BInX9%2FeNaUP5KYlAI8NkOXOa%2FKhyUCjzimH2fNKejXevX5NCt%2FQkQeRZNsXrRSUHdUT9twQYD%2B8%2F%2FUsBT0LGNNK9m4X5VotU6Oh&X-Amz-Signature=0935d460b82d5c1b94382f1922401b129804910416a48aeaf39035b21c66d2a3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YNSO6EVT%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJHMEUCIHznwjoPRV3tMVmGKy%2BCDOSektKmfHR71Ct0nEHQFMynAiEA3D1jjILeAaexYfDKQnZYqn8x8g5EtELWX6cA751emg8qiAQIsf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMKR%2Bgdcea8qlm6PxSrcA%2Bh5feGYHszLUCon6CY43W2qE7eay5InDv26ugSy1TmymXd%2Foz7dG2rYooG5AECE8Ina7eJ98JqHiQnbDHEWOXhDiUdHC%2FEmijIiarY2tbc%2B8ZpMxG0FcATJXSf5yg2su2yIvJU9F%2B%2Fs98dh8bxZkvPDlrtkQq4M7NsNY7vepOYgNvgKHkW8%2BxE5qRy7NgaNDXLFiUe2jErPKuA%2Fu3twKVLzD6v4lkvoyEfp52fewi7UY8%2FPfTrYUpb6Aw3hl18sRmOPKiiJDBD3k2qZmp7M87%2F5Ply6kSsjWVg%2BTvGOoa%2BfDj5tQaV%2FxRMh7HUofrASeb9qsjszJuGqCTXUcSpOTU49ohoG%2Bjt2p%2FNscgYNmkz4CQteXYJ%2B9vgbLebpsvr7%2F8dIjE%2F8CX%2BTVJMTjSu8sgNQO1VjTRka0s2uBfYOpgZ7cHYLMsqRFwDFNF54qAPXCyPOrhPRFBpqTFtmKM6kQgg66b2BH4pn8NhyvzBmhV33fsehwngii4Hvw9cvkDX1CvlORY4X6rFKfxgVDXNAR89kz2OTvEzzx2rM1kfmQXDHXoojg5105gfEooZKnB%2BcrqIl4hvuDlQwAycqw%2BWcTG8Pr5APo65sIDPSCMzFyXEEekuL4NoW5j4ur6mzMPG3jr4GOqUB%2B%2Bp4kutmZORG9u6m0YXK4tSsu%2Fgo3Q9UlL5ZU1%2Fu%2F8jmT775Q4d%2FKDnQqO6wGBgB7uXWVbAPHAc2l5nmX53Wx%2FIhgvVy8M1VDaCgdbG%2FFaz%2BfB2DZWNhXAOCI%2BInX9%2FeNaUP5KYlAI8NkOXOa%2FKhyUCjzimH2fNKejXevX5NCt%2FQkQeRZNsXrRSUHdUT9twQYD%2B8%2F%2FUsBT0LGNNK9m4X5VotU6Oh&X-Amz-Signature=cfc3c4bd34df93a3e8086a9f7b34c7f3706921827a448035ef82e28827f6e34b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YNSO6EVT%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJHMEUCIHznwjoPRV3tMVmGKy%2BCDOSektKmfHR71Ct0nEHQFMynAiEA3D1jjILeAaexYfDKQnZYqn8x8g5EtELWX6cA751emg8qiAQIsf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMKR%2Bgdcea8qlm6PxSrcA%2Bh5feGYHszLUCon6CY43W2qE7eay5InDv26ugSy1TmymXd%2Foz7dG2rYooG5AECE8Ina7eJ98JqHiQnbDHEWOXhDiUdHC%2FEmijIiarY2tbc%2B8ZpMxG0FcATJXSf5yg2su2yIvJU9F%2B%2Fs98dh8bxZkvPDlrtkQq4M7NsNY7vepOYgNvgKHkW8%2BxE5qRy7NgaNDXLFiUe2jErPKuA%2Fu3twKVLzD6v4lkvoyEfp52fewi7UY8%2FPfTrYUpb6Aw3hl18sRmOPKiiJDBD3k2qZmp7M87%2F5Ply6kSsjWVg%2BTvGOoa%2BfDj5tQaV%2FxRMh7HUofrASeb9qsjszJuGqCTXUcSpOTU49ohoG%2Bjt2p%2FNscgYNmkz4CQteXYJ%2B9vgbLebpsvr7%2F8dIjE%2F8CX%2BTVJMTjSu8sgNQO1VjTRka0s2uBfYOpgZ7cHYLMsqRFwDFNF54qAPXCyPOrhPRFBpqTFtmKM6kQgg66b2BH4pn8NhyvzBmhV33fsehwngii4Hvw9cvkDX1CvlORY4X6rFKfxgVDXNAR89kz2OTvEzzx2rM1kfmQXDHXoojg5105gfEooZKnB%2BcrqIl4hvuDlQwAycqw%2BWcTG8Pr5APo65sIDPSCMzFyXEEekuL4NoW5j4ur6mzMPG3jr4GOqUB%2B%2Bp4kutmZORG9u6m0YXK4tSsu%2Fgo3Q9UlL5ZU1%2Fu%2F8jmT775Q4d%2FKDnQqO6wGBgB7uXWVbAPHAc2l5nmX53Wx%2FIhgvVy8M1VDaCgdbG%2FFaz%2BfB2DZWNhXAOCI%2BInX9%2FeNaUP5KYlAI8NkOXOa%2FKhyUCjzimH2fNKejXevX5NCt%2FQkQeRZNsXrRSUHdUT9twQYD%2B8%2F%2FUsBT0LGNNK9m4X5VotU6Oh&X-Amz-Signature=96f5a15ac34e4b1bf309259887f7ce4920e9e5fbbfc8ba325258f86a83c5ea75&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VBIZZIOP%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJIMEYCIQDbN3WKHYsd%2Ber2s2rkFjsN7etZg0QFAANBXrEwiJZFZwIhAMNMPZosA6Ani4kYTIyrBVTEmhD7kBUKiLjlXTTcNQUSKogECLH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzFmDvsDTVoLKK3BaAq3AN6MQQB2LYnL%2B1JvWvpFZX%2BEineC%2FrlcvYN4PsQ3nz8Ag%2BKXImmJ75pv5phu5DwynP3ajVJ2Rjgtyv1gRN9lQoG2%2BwjnPeZuQYURwI1UW6VabaWbNNU5M391AJUL5JZByWCPR8YuFK%2Bhs0UyPp0Mcida6t5I%2BNW8YsHqFkxWXcks%2BTDq%2BPO3y0WG9HUUMp4KlShg6iKqsYSuZ5W7KTME27CmxrOeJ4vE%2BDeRN01feUanDqgXRZUOkRg5YYldOy1muFdexXbShPV%2BBGTMv%2BXCGz63DY8aT8MtfRMl%2BBf7NMVV9ODwwH5SersY3%2Fk%2Fc%2FgFkDfAsPsk%2BrBE44xagnZwg4bRMoRJRwIxrcMEVeoz9hlsFHEN1pPkMml1QihX7bC5T23WblQot1%2F05bUrwvrLr%2FZSUokBQy0P0fYtSkqDpKg%2F5xMVO9QvZ9dbvNZSbh5EgapyFhiIBd5v9rgwRHCLPIZqU1%2F%2BDlimpav5SQ1kFe%2FEyGlZo%2Bw04YA%2Bu3HfKxy0MOGgwVD6yXMKEzJsr3pNiAWj9K2VQyBwBaP%2BsM5W2yhorGqHcc9m2fdRQBqdraroeldshcdJ%2BXNUqM%2Bh6xMyVYG3%2BtiZ9FAV%2B9DRjuhhjXYiGiI1PJ9vu%2BOff8PvDCRuI6%2BBjqkAfMSk5iaQBXeoYhTv4A7mx6ZaGr9OKp5gkYyY%2Fst1btQChsuD5GvNFRXADvXZ8AsPU3GwybKt8X9jgyCswpElY7RBkzqPe5s7jzV6gI6tsw0z3rn724B%2BpH2NzgeMtOSBkracVtGLFKtvtQ7RRhk0ohZm1as%2FCdvbAbv3ZLmcEIpqNzidHppRpYEg1t7QxYllQh7QCA20uqzWhervd7TZMOqzLWC&X-Amz-Signature=20b78852e394f63dec50b39d95820c39f2f0f49ed7330cd2185131b9507f1c39&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VBIZZIOP%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJIMEYCIQDbN3WKHYsd%2Ber2s2rkFjsN7etZg0QFAANBXrEwiJZFZwIhAMNMPZosA6Ani4kYTIyrBVTEmhD7kBUKiLjlXTTcNQUSKogECLH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzFmDvsDTVoLKK3BaAq3AN6MQQB2LYnL%2B1JvWvpFZX%2BEineC%2FrlcvYN4PsQ3nz8Ag%2BKXImmJ75pv5phu5DwynP3ajVJ2Rjgtyv1gRN9lQoG2%2BwjnPeZuQYURwI1UW6VabaWbNNU5M391AJUL5JZByWCPR8YuFK%2Bhs0UyPp0Mcida6t5I%2BNW8YsHqFkxWXcks%2BTDq%2BPO3y0WG9HUUMp4KlShg6iKqsYSuZ5W7KTME27CmxrOeJ4vE%2BDeRN01feUanDqgXRZUOkRg5YYldOy1muFdexXbShPV%2BBGTMv%2BXCGz63DY8aT8MtfRMl%2BBf7NMVV9ODwwH5SersY3%2Fk%2Fc%2FgFkDfAsPsk%2BrBE44xagnZwg4bRMoRJRwIxrcMEVeoz9hlsFHEN1pPkMml1QihX7bC5T23WblQot1%2F05bUrwvrLr%2FZSUokBQy0P0fYtSkqDpKg%2F5xMVO9QvZ9dbvNZSbh5EgapyFhiIBd5v9rgwRHCLPIZqU1%2F%2BDlimpav5SQ1kFe%2FEyGlZo%2Bw04YA%2Bu3HfKxy0MOGgwVD6yXMKEzJsr3pNiAWj9K2VQyBwBaP%2BsM5W2yhorGqHcc9m2fdRQBqdraroeldshcdJ%2BXNUqM%2Bh6xMyVYG3%2BtiZ9FAV%2B9DRjuhhjXYiGiI1PJ9vu%2BOff8PvDCRuI6%2BBjqkAfMSk5iaQBXeoYhTv4A7mx6ZaGr9OKp5gkYyY%2Fst1btQChsuD5GvNFRXADvXZ8AsPU3GwybKt8X9jgyCswpElY7RBkzqPe5s7jzV6gI6tsw0z3rn724B%2BpH2NzgeMtOSBkracVtGLFKtvtQ7RRhk0ohZm1as%2FCdvbAbv3ZLmcEIpqNzidHppRpYEg1t7QxYllQh7QCA20uqzWhervd7TZMOqzLWC&X-Amz-Signature=a11d6551bad6b8d2b48ca0e65db62104f6697eaee817d6e060ea42455d4dba19&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
