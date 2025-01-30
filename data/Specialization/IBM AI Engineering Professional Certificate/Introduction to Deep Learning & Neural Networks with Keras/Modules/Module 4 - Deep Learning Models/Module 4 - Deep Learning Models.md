

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YSJXDQDD%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDvgKGwUxhuXpaD8OPJ7oZHZvvrBFAnE0NY0PQBg9S2aQIhANZwPw8vl1zLeaTJYvMOPeKoSRFljF1bS2qgq6oNiDASKogECJz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxOWm1zHdfHXz5G8BUq3AM0mNtQNaHqpLIA7HmmkJ2N4VfWo%2B%2FkG%2BS4ENEcnf4foJ6aMf97EFmMvC%2ByVmyFWgYdoN0w1N03VDCJP2QsbGh0uA8izQDljESbt9FQZ0mv8INJsQcg1pego%2FkKv9zby3SSWGknQ13ODhBPSWzPN5ogrUXGesnC4JGfuWPRa8jh8TUBixKWFh20PN3uGrwhjyamcLaT04GQvDpNSwbdgamYaYO99%2FRd9fmPBQsFy%2FiP3Iyir3cI%2FcAliI8Au5SyYjJgJgpUxgd5p8amnfaaVBgHCD6whfBMVlaDH9Z%2B7xMquH8A%2Fm5lyCeUgmLjkVplFjQY896VJWT7r4Py3%2FysNd7seS2T5D5JELdFqNNAlxVR6B1SntqFZ2IbJSGvKlPGseWp4MCLqT%2FsH7DeIxeI5TdMBFJaB1LUEHcFL4WaP%2FGU%2BLAwXo0rSgLDc99iTCOSgcN0gOQfwjSVdKyJXIM8fTnBDZ4PzP%2BRc8fjUKODRYep5Gn364cSXYMFH0e731YPE6j8xzpreRNmBGWkv%2FzSKu4pp%2BCQrRgWY%2FT0xs2u1sjJLTKAMc5P3bImX5qLBW0G7V5mfnuIMeVdPEo5N44fq0rNA2%2BpvFN1yrAhnIOnhZ1Ja4X2G5%2FpAipSXKCsxzDRzuu8BjqkAQzgL%2FNHMeQOT165rKCD1AvgGgb21W3v33i00UmGP85lIYlpgTeR%2BEmdTNWD%2BEfIp2gCJjZjiO9DGmLQ0DMFq8wT28ZDbDP5CT%2FxvWnpbk2jYwkwyiyI7RJef%2Btvp2HDX4Maj%2BVt7lVSMC%2FAYV%2BvIPmWCuigDOwFMFfgNj%2BVs47S61CrmL%2FV%2BYX%2FibD2u%2Fo60zF1AzG7hfwAGxr19edcO3wu0fup&X-Amz-Signature=921f968895d58c3b0f404a9f5a83b0aa7bd04333a3677ae402d43d9fae808759&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YSJXDQDD%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDvgKGwUxhuXpaD8OPJ7oZHZvvrBFAnE0NY0PQBg9S2aQIhANZwPw8vl1zLeaTJYvMOPeKoSRFljF1bS2qgq6oNiDASKogECJz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxOWm1zHdfHXz5G8BUq3AM0mNtQNaHqpLIA7HmmkJ2N4VfWo%2B%2FkG%2BS4ENEcnf4foJ6aMf97EFmMvC%2ByVmyFWgYdoN0w1N03VDCJP2QsbGh0uA8izQDljESbt9FQZ0mv8INJsQcg1pego%2FkKv9zby3SSWGknQ13ODhBPSWzPN5ogrUXGesnC4JGfuWPRa8jh8TUBixKWFh20PN3uGrwhjyamcLaT04GQvDpNSwbdgamYaYO99%2FRd9fmPBQsFy%2FiP3Iyir3cI%2FcAliI8Au5SyYjJgJgpUxgd5p8amnfaaVBgHCD6whfBMVlaDH9Z%2B7xMquH8A%2Fm5lyCeUgmLjkVplFjQY896VJWT7r4Py3%2FysNd7seS2T5D5JELdFqNNAlxVR6B1SntqFZ2IbJSGvKlPGseWp4MCLqT%2FsH7DeIxeI5TdMBFJaB1LUEHcFL4WaP%2FGU%2BLAwXo0rSgLDc99iTCOSgcN0gOQfwjSVdKyJXIM8fTnBDZ4PzP%2BRc8fjUKODRYep5Gn364cSXYMFH0e731YPE6j8xzpreRNmBGWkv%2FzSKu4pp%2BCQrRgWY%2FT0xs2u1sjJLTKAMc5P3bImX5qLBW0G7V5mfnuIMeVdPEo5N44fq0rNA2%2BpvFN1yrAhnIOnhZ1Ja4X2G5%2FpAipSXKCsxzDRzuu8BjqkAQzgL%2FNHMeQOT165rKCD1AvgGgb21W3v33i00UmGP85lIYlpgTeR%2BEmdTNWD%2BEfIp2gCJjZjiO9DGmLQ0DMFq8wT28ZDbDP5CT%2FxvWnpbk2jYwkwyiyI7RJef%2Btvp2HDX4Maj%2BVt7lVSMC%2FAYV%2BvIPmWCuigDOwFMFfgNj%2BVs47S61CrmL%2FV%2BYX%2FibD2u%2Fo60zF1AzG7hfwAGxr19edcO3wu0fup&X-Amz-Signature=21b4a900ef45aea5c15a38eb28b178182cc86ab94b742d0594372966a784dac1&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YSJXDQDD%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDvgKGwUxhuXpaD8OPJ7oZHZvvrBFAnE0NY0PQBg9S2aQIhANZwPw8vl1zLeaTJYvMOPeKoSRFljF1bS2qgq6oNiDASKogECJz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxOWm1zHdfHXz5G8BUq3AM0mNtQNaHqpLIA7HmmkJ2N4VfWo%2B%2FkG%2BS4ENEcnf4foJ6aMf97EFmMvC%2ByVmyFWgYdoN0w1N03VDCJP2QsbGh0uA8izQDljESbt9FQZ0mv8INJsQcg1pego%2FkKv9zby3SSWGknQ13ODhBPSWzPN5ogrUXGesnC4JGfuWPRa8jh8TUBixKWFh20PN3uGrwhjyamcLaT04GQvDpNSwbdgamYaYO99%2FRd9fmPBQsFy%2FiP3Iyir3cI%2FcAliI8Au5SyYjJgJgpUxgd5p8amnfaaVBgHCD6whfBMVlaDH9Z%2B7xMquH8A%2Fm5lyCeUgmLjkVplFjQY896VJWT7r4Py3%2FysNd7seS2T5D5JELdFqNNAlxVR6B1SntqFZ2IbJSGvKlPGseWp4MCLqT%2FsH7DeIxeI5TdMBFJaB1LUEHcFL4WaP%2FGU%2BLAwXo0rSgLDc99iTCOSgcN0gOQfwjSVdKyJXIM8fTnBDZ4PzP%2BRc8fjUKODRYep5Gn364cSXYMFH0e731YPE6j8xzpreRNmBGWkv%2FzSKu4pp%2BCQrRgWY%2FT0xs2u1sjJLTKAMc5P3bImX5qLBW0G7V5mfnuIMeVdPEo5N44fq0rNA2%2BpvFN1yrAhnIOnhZ1Ja4X2G5%2FpAipSXKCsxzDRzuu8BjqkAQzgL%2FNHMeQOT165rKCD1AvgGgb21W3v33i00UmGP85lIYlpgTeR%2BEmdTNWD%2BEfIp2gCJjZjiO9DGmLQ0DMFq8wT28ZDbDP5CT%2FxvWnpbk2jYwkwyiyI7RJef%2Btvp2HDX4Maj%2BVt7lVSMC%2FAYV%2BvIPmWCuigDOwFMFfgNj%2BVs47S61CrmL%2FV%2BYX%2FibD2u%2Fo60zF1AzG7hfwAGxr19edcO3wu0fup&X-Amz-Signature=3ba531fe57448a9019ea6c75bf1ef0e7ce81ef8add87e09a498ab2aff6e82c7a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YSJXDQDD%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDvgKGwUxhuXpaD8OPJ7oZHZvvrBFAnE0NY0PQBg9S2aQIhANZwPw8vl1zLeaTJYvMOPeKoSRFljF1bS2qgq6oNiDASKogECJz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxOWm1zHdfHXz5G8BUq3AM0mNtQNaHqpLIA7HmmkJ2N4VfWo%2B%2FkG%2BS4ENEcnf4foJ6aMf97EFmMvC%2ByVmyFWgYdoN0w1N03VDCJP2QsbGh0uA8izQDljESbt9FQZ0mv8INJsQcg1pego%2FkKv9zby3SSWGknQ13ODhBPSWzPN5ogrUXGesnC4JGfuWPRa8jh8TUBixKWFh20PN3uGrwhjyamcLaT04GQvDpNSwbdgamYaYO99%2FRd9fmPBQsFy%2FiP3Iyir3cI%2FcAliI8Au5SyYjJgJgpUxgd5p8amnfaaVBgHCD6whfBMVlaDH9Z%2B7xMquH8A%2Fm5lyCeUgmLjkVplFjQY896VJWT7r4Py3%2FysNd7seS2T5D5JELdFqNNAlxVR6B1SntqFZ2IbJSGvKlPGseWp4MCLqT%2FsH7DeIxeI5TdMBFJaB1LUEHcFL4WaP%2FGU%2BLAwXo0rSgLDc99iTCOSgcN0gOQfwjSVdKyJXIM8fTnBDZ4PzP%2BRc8fjUKODRYep5Gn364cSXYMFH0e731YPE6j8xzpreRNmBGWkv%2FzSKu4pp%2BCQrRgWY%2FT0xs2u1sjJLTKAMc5P3bImX5qLBW0G7V5mfnuIMeVdPEo5N44fq0rNA2%2BpvFN1yrAhnIOnhZ1Ja4X2G5%2FpAipSXKCsxzDRzuu8BjqkAQzgL%2FNHMeQOT165rKCD1AvgGgb21W3v33i00UmGP85lIYlpgTeR%2BEmdTNWD%2BEfIp2gCJjZjiO9DGmLQ0DMFq8wT28ZDbDP5CT%2FxvWnpbk2jYwkwyiyI7RJef%2Btvp2HDX4Maj%2BVt7lVSMC%2FAYV%2BvIPmWCuigDOwFMFfgNj%2BVs47S61CrmL%2FV%2BYX%2FibD2u%2Fo60zF1AzG7hfwAGxr19edcO3wu0fup&X-Amz-Signature=93d10872c2cb0ac3fe2dac300f1c7f1028d130ceef5e86df3130e11961394748&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YSJXDQDD%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDvgKGwUxhuXpaD8OPJ7oZHZvvrBFAnE0NY0PQBg9S2aQIhANZwPw8vl1zLeaTJYvMOPeKoSRFljF1bS2qgq6oNiDASKogECJz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxOWm1zHdfHXz5G8BUq3AM0mNtQNaHqpLIA7HmmkJ2N4VfWo%2B%2FkG%2BS4ENEcnf4foJ6aMf97EFmMvC%2ByVmyFWgYdoN0w1N03VDCJP2QsbGh0uA8izQDljESbt9FQZ0mv8INJsQcg1pego%2FkKv9zby3SSWGknQ13ODhBPSWzPN5ogrUXGesnC4JGfuWPRa8jh8TUBixKWFh20PN3uGrwhjyamcLaT04GQvDpNSwbdgamYaYO99%2FRd9fmPBQsFy%2FiP3Iyir3cI%2FcAliI8Au5SyYjJgJgpUxgd5p8amnfaaVBgHCD6whfBMVlaDH9Z%2B7xMquH8A%2Fm5lyCeUgmLjkVplFjQY896VJWT7r4Py3%2FysNd7seS2T5D5JELdFqNNAlxVR6B1SntqFZ2IbJSGvKlPGseWp4MCLqT%2FsH7DeIxeI5TdMBFJaB1LUEHcFL4WaP%2FGU%2BLAwXo0rSgLDc99iTCOSgcN0gOQfwjSVdKyJXIM8fTnBDZ4PzP%2BRc8fjUKODRYep5Gn364cSXYMFH0e731YPE6j8xzpreRNmBGWkv%2FzSKu4pp%2BCQrRgWY%2FT0xs2u1sjJLTKAMc5P3bImX5qLBW0G7V5mfnuIMeVdPEo5N44fq0rNA2%2BpvFN1yrAhnIOnhZ1Ja4X2G5%2FpAipSXKCsxzDRzuu8BjqkAQzgL%2FNHMeQOT165rKCD1AvgGgb21W3v33i00UmGP85lIYlpgTeR%2BEmdTNWD%2BEfIp2gCJjZjiO9DGmLQ0DMFq8wT28ZDbDP5CT%2FxvWnpbk2jYwkwyiyI7RJef%2Btvp2HDX4Maj%2BVt7lVSMC%2FAYV%2BvIPmWCuigDOwFMFfgNj%2BVs47S61CrmL%2FV%2BYX%2FibD2u%2Fo60zF1AzG7hfwAGxr19edcO3wu0fup&X-Amz-Signature=0b26aab4ed4d2ac0215e4f20f61ea513126538cf6478e37b656d5e00632a6eb4&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YSJXDQDD%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDvgKGwUxhuXpaD8OPJ7oZHZvvrBFAnE0NY0PQBg9S2aQIhANZwPw8vl1zLeaTJYvMOPeKoSRFljF1bS2qgq6oNiDASKogECJz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxOWm1zHdfHXz5G8BUq3AM0mNtQNaHqpLIA7HmmkJ2N4VfWo%2B%2FkG%2BS4ENEcnf4foJ6aMf97EFmMvC%2ByVmyFWgYdoN0w1N03VDCJP2QsbGh0uA8izQDljESbt9FQZ0mv8INJsQcg1pego%2FkKv9zby3SSWGknQ13ODhBPSWzPN5ogrUXGesnC4JGfuWPRa8jh8TUBixKWFh20PN3uGrwhjyamcLaT04GQvDpNSwbdgamYaYO99%2FRd9fmPBQsFy%2FiP3Iyir3cI%2FcAliI8Au5SyYjJgJgpUxgd5p8amnfaaVBgHCD6whfBMVlaDH9Z%2B7xMquH8A%2Fm5lyCeUgmLjkVplFjQY896VJWT7r4Py3%2FysNd7seS2T5D5JELdFqNNAlxVR6B1SntqFZ2IbJSGvKlPGseWp4MCLqT%2FsH7DeIxeI5TdMBFJaB1LUEHcFL4WaP%2FGU%2BLAwXo0rSgLDc99iTCOSgcN0gOQfwjSVdKyJXIM8fTnBDZ4PzP%2BRc8fjUKODRYep5Gn364cSXYMFH0e731YPE6j8xzpreRNmBGWkv%2FzSKu4pp%2BCQrRgWY%2FT0xs2u1sjJLTKAMc5P3bImX5qLBW0G7V5mfnuIMeVdPEo5N44fq0rNA2%2BpvFN1yrAhnIOnhZ1Ja4X2G5%2FpAipSXKCsxzDRzuu8BjqkAQzgL%2FNHMeQOT165rKCD1AvgGgb21W3v33i00UmGP85lIYlpgTeR%2BEmdTNWD%2BEfIp2gCJjZjiO9DGmLQ0DMFq8wT28ZDbDP5CT%2FxvWnpbk2jYwkwyiyI7RJef%2Btvp2HDX4Maj%2BVt7lVSMC%2FAYV%2BvIPmWCuigDOwFMFfgNj%2BVs47S61CrmL%2FV%2BYX%2FibD2u%2Fo60zF1AzG7hfwAGxr19edcO3wu0fup&X-Amz-Signature=39c2da25f00b61a6f6e69a5cef4e71a6e6d17d1e2325ce9910fa8e84fa05566d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YSJXDQDD%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDvgKGwUxhuXpaD8OPJ7oZHZvvrBFAnE0NY0PQBg9S2aQIhANZwPw8vl1zLeaTJYvMOPeKoSRFljF1bS2qgq6oNiDASKogECJz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxOWm1zHdfHXz5G8BUq3AM0mNtQNaHqpLIA7HmmkJ2N4VfWo%2B%2FkG%2BS4ENEcnf4foJ6aMf97EFmMvC%2ByVmyFWgYdoN0w1N03VDCJP2QsbGh0uA8izQDljESbt9FQZ0mv8INJsQcg1pego%2FkKv9zby3SSWGknQ13ODhBPSWzPN5ogrUXGesnC4JGfuWPRa8jh8TUBixKWFh20PN3uGrwhjyamcLaT04GQvDpNSwbdgamYaYO99%2FRd9fmPBQsFy%2FiP3Iyir3cI%2FcAliI8Au5SyYjJgJgpUxgd5p8amnfaaVBgHCD6whfBMVlaDH9Z%2B7xMquH8A%2Fm5lyCeUgmLjkVplFjQY896VJWT7r4Py3%2FysNd7seS2T5D5JELdFqNNAlxVR6B1SntqFZ2IbJSGvKlPGseWp4MCLqT%2FsH7DeIxeI5TdMBFJaB1LUEHcFL4WaP%2FGU%2BLAwXo0rSgLDc99iTCOSgcN0gOQfwjSVdKyJXIM8fTnBDZ4PzP%2BRc8fjUKODRYep5Gn364cSXYMFH0e731YPE6j8xzpreRNmBGWkv%2FzSKu4pp%2BCQrRgWY%2FT0xs2u1sjJLTKAMc5P3bImX5qLBW0G7V5mfnuIMeVdPEo5N44fq0rNA2%2BpvFN1yrAhnIOnhZ1Ja4X2G5%2FpAipSXKCsxzDRzuu8BjqkAQzgL%2FNHMeQOT165rKCD1AvgGgb21W3v33i00UmGP85lIYlpgTeR%2BEmdTNWD%2BEfIp2gCJjZjiO9DGmLQ0DMFq8wT28ZDbDP5CT%2FxvWnpbk2jYwkwyiyI7RJef%2Btvp2HDX4Maj%2BVt7lVSMC%2FAYV%2BvIPmWCuigDOwFMFfgNj%2BVs47S61CrmL%2FV%2BYX%2FibD2u%2Fo60zF1AzG7hfwAGxr19edcO3wu0fup&X-Amz-Signature=c05c889649b901e03cd02cc434505350d285026f09625da1851d32aa1b9d2a6c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YSJXDQDD%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDvgKGwUxhuXpaD8OPJ7oZHZvvrBFAnE0NY0PQBg9S2aQIhANZwPw8vl1zLeaTJYvMOPeKoSRFljF1bS2qgq6oNiDASKogECJz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxOWm1zHdfHXz5G8BUq3AM0mNtQNaHqpLIA7HmmkJ2N4VfWo%2B%2FkG%2BS4ENEcnf4foJ6aMf97EFmMvC%2ByVmyFWgYdoN0w1N03VDCJP2QsbGh0uA8izQDljESbt9FQZ0mv8INJsQcg1pego%2FkKv9zby3SSWGknQ13ODhBPSWzPN5ogrUXGesnC4JGfuWPRa8jh8TUBixKWFh20PN3uGrwhjyamcLaT04GQvDpNSwbdgamYaYO99%2FRd9fmPBQsFy%2FiP3Iyir3cI%2FcAliI8Au5SyYjJgJgpUxgd5p8amnfaaVBgHCD6whfBMVlaDH9Z%2B7xMquH8A%2Fm5lyCeUgmLjkVplFjQY896VJWT7r4Py3%2FysNd7seS2T5D5JELdFqNNAlxVR6B1SntqFZ2IbJSGvKlPGseWp4MCLqT%2FsH7DeIxeI5TdMBFJaB1LUEHcFL4WaP%2FGU%2BLAwXo0rSgLDc99iTCOSgcN0gOQfwjSVdKyJXIM8fTnBDZ4PzP%2BRc8fjUKODRYep5Gn364cSXYMFH0e731YPE6j8xzpreRNmBGWkv%2FzSKu4pp%2BCQrRgWY%2FT0xs2u1sjJLTKAMc5P3bImX5qLBW0G7V5mfnuIMeVdPEo5N44fq0rNA2%2BpvFN1yrAhnIOnhZ1Ja4X2G5%2FpAipSXKCsxzDRzuu8BjqkAQzgL%2FNHMeQOT165rKCD1AvgGgb21W3v33i00UmGP85lIYlpgTeR%2BEmdTNWD%2BEfIp2gCJjZjiO9DGmLQ0DMFq8wT28ZDbDP5CT%2FxvWnpbk2jYwkwyiyI7RJef%2Btvp2HDX4Maj%2BVt7lVSMC%2FAYV%2BvIPmWCuigDOwFMFfgNj%2BVs47S61CrmL%2FV%2BYX%2FibD2u%2Fo60zF1AzG7hfwAGxr19edcO3wu0fup&X-Amz-Signature=a7b402ed5fa80e28ad81c368d0203c3f66f87856eb9c4d08ce31fb2e3fb2d751&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YSJXDQDD%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDvgKGwUxhuXpaD8OPJ7oZHZvvrBFAnE0NY0PQBg9S2aQIhANZwPw8vl1zLeaTJYvMOPeKoSRFljF1bS2qgq6oNiDASKogECJz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxOWm1zHdfHXz5G8BUq3AM0mNtQNaHqpLIA7HmmkJ2N4VfWo%2B%2FkG%2BS4ENEcnf4foJ6aMf97EFmMvC%2ByVmyFWgYdoN0w1N03VDCJP2QsbGh0uA8izQDljESbt9FQZ0mv8INJsQcg1pego%2FkKv9zby3SSWGknQ13ODhBPSWzPN5ogrUXGesnC4JGfuWPRa8jh8TUBixKWFh20PN3uGrwhjyamcLaT04GQvDpNSwbdgamYaYO99%2FRd9fmPBQsFy%2FiP3Iyir3cI%2FcAliI8Au5SyYjJgJgpUxgd5p8amnfaaVBgHCD6whfBMVlaDH9Z%2B7xMquH8A%2Fm5lyCeUgmLjkVplFjQY896VJWT7r4Py3%2FysNd7seS2T5D5JELdFqNNAlxVR6B1SntqFZ2IbJSGvKlPGseWp4MCLqT%2FsH7DeIxeI5TdMBFJaB1LUEHcFL4WaP%2FGU%2BLAwXo0rSgLDc99iTCOSgcN0gOQfwjSVdKyJXIM8fTnBDZ4PzP%2BRc8fjUKODRYep5Gn364cSXYMFH0e731YPE6j8xzpreRNmBGWkv%2FzSKu4pp%2BCQrRgWY%2FT0xs2u1sjJLTKAMc5P3bImX5qLBW0G7V5mfnuIMeVdPEo5N44fq0rNA2%2BpvFN1yrAhnIOnhZ1Ja4X2G5%2FpAipSXKCsxzDRzuu8BjqkAQzgL%2FNHMeQOT165rKCD1AvgGgb21W3v33i00UmGP85lIYlpgTeR%2BEmdTNWD%2BEfIp2gCJjZjiO9DGmLQ0DMFq8wT28ZDbDP5CT%2FxvWnpbk2jYwkwyiyI7RJef%2Btvp2HDX4Maj%2BVt7lVSMC%2FAYV%2BvIPmWCuigDOwFMFfgNj%2BVs47S61CrmL%2FV%2BYX%2FibD2u%2Fo60zF1AzG7hfwAGxr19edcO3wu0fup&X-Amz-Signature=c3fef6d8985d24be7aaa0f6c1e8ca1884d9d28b3ac528071cd9de7d0ef260d1f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VDR6GQ6I%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCMgLJCAB3D3QSQO0i0qm8JWeWqWAZy6kfL9nipJAvIfQIhAJjdbx8n67HYnO%2BmQRDG6ZcGIXNCcTu4ixEK2wbk%2BmU9KogECJz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzyH3uKXgJiFKfeDDIq3AMLxvhzP0c609No3jqnoty9v1RPigy4ZB83XiWMhXmN20vc3fFlmQvPqQ2Uz%2FysqkLKHaXZpqxGbsT9RcNetlZAcs%2BXTb%2FWhePugJxKGgwEYfi%2FN467utqtMlzr22EOcEkrsGezaQxavJTVspV703ndsDY9WBH8A8Kg3o5iIrWLeG7k8a2q%2FAj9lICiFk2UOZfSRannd2dN5TB0Etu9%2FT7v8YOFB05AKlDEl1rlf%2F04heFb7bLw0kNgVIPZlHkDC0sDzzCvn5WUGulE69S74y3hbm9kSwLPevxhgzd9ouICTL5SE2M2dSjGVmic4kvbDpdK6%2BbVoDqg97L5kTV9AQbIVgBEU23wJg8GEANiykqRCHcEfJ3F0oc0PqwBy2L3J70%2FR%2F8TWeimX6eaqOwPWP3ON3j1iAbVIfpacbKARaosKxPpWvMOdMFGHwqJnVrdbVHYTdm6StP2CGGYDDIna4EGhyJUHRdPviUyIwOasqPBS%2BP8ytB7TpACTHIB1pfWyXzZ75mtlOssswEA2AFn9XeRnLuUqfpVSZVSi9gahe8TAE23bFrCEIgnrv4b0rTXNbKBGwEukc%2BKtJCQi8SBQYgAQ3VNs1VnZ%2BVMledVWvqZJ2pJcCe3rWYf0DIHmzCyzuu8BjqkAc%2FLVFYW50CADeehPmUp4iwWTXgYvna5FxmQ59asePIl3NUwEE2CL9IWmBVffEkxlg2lrx4ZMmTGf6rBsZSIIRxJIIgm1P4g2%2FsnH1Wn2nhYvl7h6vJfhYTWFXurEOQ3Td1f5zGYFQL%2Ftdr21P70%2F%2F2ukItg5kRnJSniK58QZRAH%2BJEcQ5is74D%2BeYvVdQSraNgQ914PnvPgSpUX542sDtGylYmM&X-Amz-Signature=a18e45977971c31be9537179851c954aa0ec2d41414a057b32b72fcd4ac132bc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VDR6GQ6I%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCMgLJCAB3D3QSQO0i0qm8JWeWqWAZy6kfL9nipJAvIfQIhAJjdbx8n67HYnO%2BmQRDG6ZcGIXNCcTu4ixEK2wbk%2BmU9KogECJz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzyH3uKXgJiFKfeDDIq3AMLxvhzP0c609No3jqnoty9v1RPigy4ZB83XiWMhXmN20vc3fFlmQvPqQ2Uz%2FysqkLKHaXZpqxGbsT9RcNetlZAcs%2BXTb%2FWhePugJxKGgwEYfi%2FN467utqtMlzr22EOcEkrsGezaQxavJTVspV703ndsDY9WBH8A8Kg3o5iIrWLeG7k8a2q%2FAj9lICiFk2UOZfSRannd2dN5TB0Etu9%2FT7v8YOFB05AKlDEl1rlf%2F04heFb7bLw0kNgVIPZlHkDC0sDzzCvn5WUGulE69S74y3hbm9kSwLPevxhgzd9ouICTL5SE2M2dSjGVmic4kvbDpdK6%2BbVoDqg97L5kTV9AQbIVgBEU23wJg8GEANiykqRCHcEfJ3F0oc0PqwBy2L3J70%2FR%2F8TWeimX6eaqOwPWP3ON3j1iAbVIfpacbKARaosKxPpWvMOdMFGHwqJnVrdbVHYTdm6StP2CGGYDDIna4EGhyJUHRdPviUyIwOasqPBS%2BP8ytB7TpACTHIB1pfWyXzZ75mtlOssswEA2AFn9XeRnLuUqfpVSZVSi9gahe8TAE23bFrCEIgnrv4b0rTXNbKBGwEukc%2BKtJCQi8SBQYgAQ3VNs1VnZ%2BVMledVWvqZJ2pJcCe3rWYf0DIHmzCyzuu8BjqkAc%2FLVFYW50CADeehPmUp4iwWTXgYvna5FxmQ59asePIl3NUwEE2CL9IWmBVffEkxlg2lrx4ZMmTGf6rBsZSIIRxJIIgm1P4g2%2FsnH1Wn2nhYvl7h6vJfhYTWFXurEOQ3Td1f5zGYFQL%2Ftdr21P70%2F%2F2ukItg5kRnJSniK58QZRAH%2BJEcQ5is74D%2BeYvVdQSraNgQ914PnvPgSpUX542sDtGylYmM&X-Amz-Signature=77015fa0d74f53333862e2a310db5e1e9a0abed23dc4d07c1f1cd77dbb214c18&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
