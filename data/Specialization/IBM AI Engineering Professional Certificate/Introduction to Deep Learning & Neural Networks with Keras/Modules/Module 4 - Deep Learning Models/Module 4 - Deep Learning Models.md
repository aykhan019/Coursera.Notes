

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666GBNLAPS%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF0XQaQakpiE0%2FY1HlvhdPVAJJ1IN4Mw4rSxkVja64MeAiBxJVwRkzZUbesmqP%2FSlPjdZ4Bl7SL14LfvUhfNicRM3yqIBAiS%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMkKhWmB%2FDRzLV4%2BekKtwDNIKI8olSSjsTE4c%2Btk8lPn6k5fjjf%2FdIhMSFx4w9%2BySJlSMvkGe5zsUxbPOBbqQHAtCx67sCbXymXVkJBLa%2BjtO1sXEZscHCzI4IJSAsRJCA7R0idSTQ2D5RxxeJ6KB%2Bk1CPVGDbHjUyXguzrHinlblH4Up9z9d1zOlq%2B6TXZhRRc8G5FZmBteQA8VPqbPLWx886fjdooF3IzyxJfi3O1s8qfBu%2BQfpObPS5lel427XlRV9gKYssdTKH13P0NyGcYoD6iA3Sge6BP4aSRS%2Bc3lWkKdnbujwOBXJLII8iFkrjOPJfeoPx2rWucbD2AoU53SmgkDFN2bPLc7YSDRx9vDLHjnp%2F9ah6vSTT4fwSUcjZHMXsMuXpNeATe6kpj%2F0BYL%2FwUzzMnaDvasQjOfuPxY4dkEbbzCMymilLE44Yyj%2FTbiKea5MAYe4XiQkt%2BKyQc9RkbLwkp2dgUHEGU6nf4eL9EOuPOVdR8rvaSdeRD7v%2FjWCytgqV8hot7yQQegEG7DC7Vr5kxjPI4QdxoTrxI8azRojcS%2BQln6YBavd1%2BQStlTdKTJzVecjB1qnqaIiB2yo8Y2laHlkShGDJulcUhQyPAN5BB%2F2ioMfKeXFwGyDK%2F3djwzpSxttQirIwkrzpvAY6pgGztBSbUK%2BacpyUxfda3hak88EXutr%2BNLInLmpCOx%2B2IKWknbaUl1j2XiORlh9EWaP9jaVC3KNzNTzc7Cn%2Fee4uT6FqbsCW39WTbSM3DKfAAFkcxwpYUICDjaQFh9d4i7CkFauPrYl%2Fzm4r42aqChO1gYTQqMG90RXQqJoKpqLRIgjw65VDHkONdspGVMxEQrOuKXUHPpkF16l6K9R8raSpwcFZFi6s&X-Amz-Signature=a37c3c0e08d10184a0b70b3e6259bda1f6fa0cf863873e95c087ad80346e22dd&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666GBNLAPS%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF0XQaQakpiE0%2FY1HlvhdPVAJJ1IN4Mw4rSxkVja64MeAiBxJVwRkzZUbesmqP%2FSlPjdZ4Bl7SL14LfvUhfNicRM3yqIBAiS%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMkKhWmB%2FDRzLV4%2BekKtwDNIKI8olSSjsTE4c%2Btk8lPn6k5fjjf%2FdIhMSFx4w9%2BySJlSMvkGe5zsUxbPOBbqQHAtCx67sCbXymXVkJBLa%2BjtO1sXEZscHCzI4IJSAsRJCA7R0idSTQ2D5RxxeJ6KB%2Bk1CPVGDbHjUyXguzrHinlblH4Up9z9d1zOlq%2B6TXZhRRc8G5FZmBteQA8VPqbPLWx886fjdooF3IzyxJfi3O1s8qfBu%2BQfpObPS5lel427XlRV9gKYssdTKH13P0NyGcYoD6iA3Sge6BP4aSRS%2Bc3lWkKdnbujwOBXJLII8iFkrjOPJfeoPx2rWucbD2AoU53SmgkDFN2bPLc7YSDRx9vDLHjnp%2F9ah6vSTT4fwSUcjZHMXsMuXpNeATe6kpj%2F0BYL%2FwUzzMnaDvasQjOfuPxY4dkEbbzCMymilLE44Yyj%2FTbiKea5MAYe4XiQkt%2BKyQc9RkbLwkp2dgUHEGU6nf4eL9EOuPOVdR8rvaSdeRD7v%2FjWCytgqV8hot7yQQegEG7DC7Vr5kxjPI4QdxoTrxI8azRojcS%2BQln6YBavd1%2BQStlTdKTJzVecjB1qnqaIiB2yo8Y2laHlkShGDJulcUhQyPAN5BB%2F2ioMfKeXFwGyDK%2F3djwzpSxttQirIwkrzpvAY6pgGztBSbUK%2BacpyUxfda3hak88EXutr%2BNLInLmpCOx%2B2IKWknbaUl1j2XiORlh9EWaP9jaVC3KNzNTzc7Cn%2Fee4uT6FqbsCW39WTbSM3DKfAAFkcxwpYUICDjaQFh9d4i7CkFauPrYl%2Fzm4r42aqChO1gYTQqMG90RXQqJoKpqLRIgjw65VDHkONdspGVMxEQrOuKXUHPpkF16l6K9R8raSpwcFZFi6s&X-Amz-Signature=15c9b0c9ad8602b9689ad2e774fc2d9d4c2d6c9a2992f678ead45d900c1f787d&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666GBNLAPS%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF0XQaQakpiE0%2FY1HlvhdPVAJJ1IN4Mw4rSxkVja64MeAiBxJVwRkzZUbesmqP%2FSlPjdZ4Bl7SL14LfvUhfNicRM3yqIBAiS%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMkKhWmB%2FDRzLV4%2BekKtwDNIKI8olSSjsTE4c%2Btk8lPn6k5fjjf%2FdIhMSFx4w9%2BySJlSMvkGe5zsUxbPOBbqQHAtCx67sCbXymXVkJBLa%2BjtO1sXEZscHCzI4IJSAsRJCA7R0idSTQ2D5RxxeJ6KB%2Bk1CPVGDbHjUyXguzrHinlblH4Up9z9d1zOlq%2B6TXZhRRc8G5FZmBteQA8VPqbPLWx886fjdooF3IzyxJfi3O1s8qfBu%2BQfpObPS5lel427XlRV9gKYssdTKH13P0NyGcYoD6iA3Sge6BP4aSRS%2Bc3lWkKdnbujwOBXJLII8iFkrjOPJfeoPx2rWucbD2AoU53SmgkDFN2bPLc7YSDRx9vDLHjnp%2F9ah6vSTT4fwSUcjZHMXsMuXpNeATe6kpj%2F0BYL%2FwUzzMnaDvasQjOfuPxY4dkEbbzCMymilLE44Yyj%2FTbiKea5MAYe4XiQkt%2BKyQc9RkbLwkp2dgUHEGU6nf4eL9EOuPOVdR8rvaSdeRD7v%2FjWCytgqV8hot7yQQegEG7DC7Vr5kxjPI4QdxoTrxI8azRojcS%2BQln6YBavd1%2BQStlTdKTJzVecjB1qnqaIiB2yo8Y2laHlkShGDJulcUhQyPAN5BB%2F2ioMfKeXFwGyDK%2F3djwzpSxttQirIwkrzpvAY6pgGztBSbUK%2BacpyUxfda3hak88EXutr%2BNLInLmpCOx%2B2IKWknbaUl1j2XiORlh9EWaP9jaVC3KNzNTzc7Cn%2Fee4uT6FqbsCW39WTbSM3DKfAAFkcxwpYUICDjaQFh9d4i7CkFauPrYl%2Fzm4r42aqChO1gYTQqMG90RXQqJoKpqLRIgjw65VDHkONdspGVMxEQrOuKXUHPpkF16l6K9R8raSpwcFZFi6s&X-Amz-Signature=f0f147c5823853ec9e6e2544a02259ff61e6a30b438a45f58977a3355a2d5357&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666GBNLAPS%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF0XQaQakpiE0%2FY1HlvhdPVAJJ1IN4Mw4rSxkVja64MeAiBxJVwRkzZUbesmqP%2FSlPjdZ4Bl7SL14LfvUhfNicRM3yqIBAiS%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMkKhWmB%2FDRzLV4%2BekKtwDNIKI8olSSjsTE4c%2Btk8lPn6k5fjjf%2FdIhMSFx4w9%2BySJlSMvkGe5zsUxbPOBbqQHAtCx67sCbXymXVkJBLa%2BjtO1sXEZscHCzI4IJSAsRJCA7R0idSTQ2D5RxxeJ6KB%2Bk1CPVGDbHjUyXguzrHinlblH4Up9z9d1zOlq%2B6TXZhRRc8G5FZmBteQA8VPqbPLWx886fjdooF3IzyxJfi3O1s8qfBu%2BQfpObPS5lel427XlRV9gKYssdTKH13P0NyGcYoD6iA3Sge6BP4aSRS%2Bc3lWkKdnbujwOBXJLII8iFkrjOPJfeoPx2rWucbD2AoU53SmgkDFN2bPLc7YSDRx9vDLHjnp%2F9ah6vSTT4fwSUcjZHMXsMuXpNeATe6kpj%2F0BYL%2FwUzzMnaDvasQjOfuPxY4dkEbbzCMymilLE44Yyj%2FTbiKea5MAYe4XiQkt%2BKyQc9RkbLwkp2dgUHEGU6nf4eL9EOuPOVdR8rvaSdeRD7v%2FjWCytgqV8hot7yQQegEG7DC7Vr5kxjPI4QdxoTrxI8azRojcS%2BQln6YBavd1%2BQStlTdKTJzVecjB1qnqaIiB2yo8Y2laHlkShGDJulcUhQyPAN5BB%2F2ioMfKeXFwGyDK%2F3djwzpSxttQirIwkrzpvAY6pgGztBSbUK%2BacpyUxfda3hak88EXutr%2BNLInLmpCOx%2B2IKWknbaUl1j2XiORlh9EWaP9jaVC3KNzNTzc7Cn%2Fee4uT6FqbsCW39WTbSM3DKfAAFkcxwpYUICDjaQFh9d4i7CkFauPrYl%2Fzm4r42aqChO1gYTQqMG90RXQqJoKpqLRIgjw65VDHkONdspGVMxEQrOuKXUHPpkF16l6K9R8raSpwcFZFi6s&X-Amz-Signature=73c2f0ad87803af5fc847f280a55def91453bb8559cda45aee6afe111c6b4aa3&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666GBNLAPS%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF0XQaQakpiE0%2FY1HlvhdPVAJJ1IN4Mw4rSxkVja64MeAiBxJVwRkzZUbesmqP%2FSlPjdZ4Bl7SL14LfvUhfNicRM3yqIBAiS%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMkKhWmB%2FDRzLV4%2BekKtwDNIKI8olSSjsTE4c%2Btk8lPn6k5fjjf%2FdIhMSFx4w9%2BySJlSMvkGe5zsUxbPOBbqQHAtCx67sCbXymXVkJBLa%2BjtO1sXEZscHCzI4IJSAsRJCA7R0idSTQ2D5RxxeJ6KB%2Bk1CPVGDbHjUyXguzrHinlblH4Up9z9d1zOlq%2B6TXZhRRc8G5FZmBteQA8VPqbPLWx886fjdooF3IzyxJfi3O1s8qfBu%2BQfpObPS5lel427XlRV9gKYssdTKH13P0NyGcYoD6iA3Sge6BP4aSRS%2Bc3lWkKdnbujwOBXJLII8iFkrjOPJfeoPx2rWucbD2AoU53SmgkDFN2bPLc7YSDRx9vDLHjnp%2F9ah6vSTT4fwSUcjZHMXsMuXpNeATe6kpj%2F0BYL%2FwUzzMnaDvasQjOfuPxY4dkEbbzCMymilLE44Yyj%2FTbiKea5MAYe4XiQkt%2BKyQc9RkbLwkp2dgUHEGU6nf4eL9EOuPOVdR8rvaSdeRD7v%2FjWCytgqV8hot7yQQegEG7DC7Vr5kxjPI4QdxoTrxI8azRojcS%2BQln6YBavd1%2BQStlTdKTJzVecjB1qnqaIiB2yo8Y2laHlkShGDJulcUhQyPAN5BB%2F2ioMfKeXFwGyDK%2F3djwzpSxttQirIwkrzpvAY6pgGztBSbUK%2BacpyUxfda3hak88EXutr%2BNLInLmpCOx%2B2IKWknbaUl1j2XiORlh9EWaP9jaVC3KNzNTzc7Cn%2Fee4uT6FqbsCW39WTbSM3DKfAAFkcxwpYUICDjaQFh9d4i7CkFauPrYl%2Fzm4r42aqChO1gYTQqMG90RXQqJoKpqLRIgjw65VDHkONdspGVMxEQrOuKXUHPpkF16l6K9R8raSpwcFZFi6s&X-Amz-Signature=9e12e2d8b4518a1f2aade5fa207a168a7d212f24c73c3dfb835982007824592c&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666GBNLAPS%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF0XQaQakpiE0%2FY1HlvhdPVAJJ1IN4Mw4rSxkVja64MeAiBxJVwRkzZUbesmqP%2FSlPjdZ4Bl7SL14LfvUhfNicRM3yqIBAiS%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMkKhWmB%2FDRzLV4%2BekKtwDNIKI8olSSjsTE4c%2Btk8lPn6k5fjjf%2FdIhMSFx4w9%2BySJlSMvkGe5zsUxbPOBbqQHAtCx67sCbXymXVkJBLa%2BjtO1sXEZscHCzI4IJSAsRJCA7R0idSTQ2D5RxxeJ6KB%2Bk1CPVGDbHjUyXguzrHinlblH4Up9z9d1zOlq%2B6TXZhRRc8G5FZmBteQA8VPqbPLWx886fjdooF3IzyxJfi3O1s8qfBu%2BQfpObPS5lel427XlRV9gKYssdTKH13P0NyGcYoD6iA3Sge6BP4aSRS%2Bc3lWkKdnbujwOBXJLII8iFkrjOPJfeoPx2rWucbD2AoU53SmgkDFN2bPLc7YSDRx9vDLHjnp%2F9ah6vSTT4fwSUcjZHMXsMuXpNeATe6kpj%2F0BYL%2FwUzzMnaDvasQjOfuPxY4dkEbbzCMymilLE44Yyj%2FTbiKea5MAYe4XiQkt%2BKyQc9RkbLwkp2dgUHEGU6nf4eL9EOuPOVdR8rvaSdeRD7v%2FjWCytgqV8hot7yQQegEG7DC7Vr5kxjPI4QdxoTrxI8azRojcS%2BQln6YBavd1%2BQStlTdKTJzVecjB1qnqaIiB2yo8Y2laHlkShGDJulcUhQyPAN5BB%2F2ioMfKeXFwGyDK%2F3djwzpSxttQirIwkrzpvAY6pgGztBSbUK%2BacpyUxfda3hak88EXutr%2BNLInLmpCOx%2B2IKWknbaUl1j2XiORlh9EWaP9jaVC3KNzNTzc7Cn%2Fee4uT6FqbsCW39WTbSM3DKfAAFkcxwpYUICDjaQFh9d4i7CkFauPrYl%2Fzm4r42aqChO1gYTQqMG90RXQqJoKpqLRIgjw65VDHkONdspGVMxEQrOuKXUHPpkF16l6K9R8raSpwcFZFi6s&X-Amz-Signature=82a64c7b6d4005b69e746cb888a3b0d83297d9277db6ee7ee3a336465c22de2c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666GBNLAPS%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF0XQaQakpiE0%2FY1HlvhdPVAJJ1IN4Mw4rSxkVja64MeAiBxJVwRkzZUbesmqP%2FSlPjdZ4Bl7SL14LfvUhfNicRM3yqIBAiS%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMkKhWmB%2FDRzLV4%2BekKtwDNIKI8olSSjsTE4c%2Btk8lPn6k5fjjf%2FdIhMSFx4w9%2BySJlSMvkGe5zsUxbPOBbqQHAtCx67sCbXymXVkJBLa%2BjtO1sXEZscHCzI4IJSAsRJCA7R0idSTQ2D5RxxeJ6KB%2Bk1CPVGDbHjUyXguzrHinlblH4Up9z9d1zOlq%2B6TXZhRRc8G5FZmBteQA8VPqbPLWx886fjdooF3IzyxJfi3O1s8qfBu%2BQfpObPS5lel427XlRV9gKYssdTKH13P0NyGcYoD6iA3Sge6BP4aSRS%2Bc3lWkKdnbujwOBXJLII8iFkrjOPJfeoPx2rWucbD2AoU53SmgkDFN2bPLc7YSDRx9vDLHjnp%2F9ah6vSTT4fwSUcjZHMXsMuXpNeATe6kpj%2F0BYL%2FwUzzMnaDvasQjOfuPxY4dkEbbzCMymilLE44Yyj%2FTbiKea5MAYe4XiQkt%2BKyQc9RkbLwkp2dgUHEGU6nf4eL9EOuPOVdR8rvaSdeRD7v%2FjWCytgqV8hot7yQQegEG7DC7Vr5kxjPI4QdxoTrxI8azRojcS%2BQln6YBavd1%2BQStlTdKTJzVecjB1qnqaIiB2yo8Y2laHlkShGDJulcUhQyPAN5BB%2F2ioMfKeXFwGyDK%2F3djwzpSxttQirIwkrzpvAY6pgGztBSbUK%2BacpyUxfda3hak88EXutr%2BNLInLmpCOx%2B2IKWknbaUl1j2XiORlh9EWaP9jaVC3KNzNTzc7Cn%2Fee4uT6FqbsCW39WTbSM3DKfAAFkcxwpYUICDjaQFh9d4i7CkFauPrYl%2Fzm4r42aqChO1gYTQqMG90RXQqJoKpqLRIgjw65VDHkONdspGVMxEQrOuKXUHPpkF16l6K9R8raSpwcFZFi6s&X-Amz-Signature=76484a49b77e6940b4e2654a7d4fa9ed809e14ea94b6399c4cb8338a17868b95&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666GBNLAPS%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF0XQaQakpiE0%2FY1HlvhdPVAJJ1IN4Mw4rSxkVja64MeAiBxJVwRkzZUbesmqP%2FSlPjdZ4Bl7SL14LfvUhfNicRM3yqIBAiS%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMkKhWmB%2FDRzLV4%2BekKtwDNIKI8olSSjsTE4c%2Btk8lPn6k5fjjf%2FdIhMSFx4w9%2BySJlSMvkGe5zsUxbPOBbqQHAtCx67sCbXymXVkJBLa%2BjtO1sXEZscHCzI4IJSAsRJCA7R0idSTQ2D5RxxeJ6KB%2Bk1CPVGDbHjUyXguzrHinlblH4Up9z9d1zOlq%2B6TXZhRRc8G5FZmBteQA8VPqbPLWx886fjdooF3IzyxJfi3O1s8qfBu%2BQfpObPS5lel427XlRV9gKYssdTKH13P0NyGcYoD6iA3Sge6BP4aSRS%2Bc3lWkKdnbujwOBXJLII8iFkrjOPJfeoPx2rWucbD2AoU53SmgkDFN2bPLc7YSDRx9vDLHjnp%2F9ah6vSTT4fwSUcjZHMXsMuXpNeATe6kpj%2F0BYL%2FwUzzMnaDvasQjOfuPxY4dkEbbzCMymilLE44Yyj%2FTbiKea5MAYe4XiQkt%2BKyQc9RkbLwkp2dgUHEGU6nf4eL9EOuPOVdR8rvaSdeRD7v%2FjWCytgqV8hot7yQQegEG7DC7Vr5kxjPI4QdxoTrxI8azRojcS%2BQln6YBavd1%2BQStlTdKTJzVecjB1qnqaIiB2yo8Y2laHlkShGDJulcUhQyPAN5BB%2F2ioMfKeXFwGyDK%2F3djwzpSxttQirIwkrzpvAY6pgGztBSbUK%2BacpyUxfda3hak88EXutr%2BNLInLmpCOx%2B2IKWknbaUl1j2XiORlh9EWaP9jaVC3KNzNTzc7Cn%2Fee4uT6FqbsCW39WTbSM3DKfAAFkcxwpYUICDjaQFh9d4i7CkFauPrYl%2Fzm4r42aqChO1gYTQqMG90RXQqJoKpqLRIgjw65VDHkONdspGVMxEQrOuKXUHPpkF16l6K9R8raSpwcFZFi6s&X-Amz-Signature=6539b745f3068c3b688aabd73a350da60f7b5a4a97f306076a0d80e0fb40df1d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666GBNLAPS%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF0XQaQakpiE0%2FY1HlvhdPVAJJ1IN4Mw4rSxkVja64MeAiBxJVwRkzZUbesmqP%2FSlPjdZ4Bl7SL14LfvUhfNicRM3yqIBAiS%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMkKhWmB%2FDRzLV4%2BekKtwDNIKI8olSSjsTE4c%2Btk8lPn6k5fjjf%2FdIhMSFx4w9%2BySJlSMvkGe5zsUxbPOBbqQHAtCx67sCbXymXVkJBLa%2BjtO1sXEZscHCzI4IJSAsRJCA7R0idSTQ2D5RxxeJ6KB%2Bk1CPVGDbHjUyXguzrHinlblH4Up9z9d1zOlq%2B6TXZhRRc8G5FZmBteQA8VPqbPLWx886fjdooF3IzyxJfi3O1s8qfBu%2BQfpObPS5lel427XlRV9gKYssdTKH13P0NyGcYoD6iA3Sge6BP4aSRS%2Bc3lWkKdnbujwOBXJLII8iFkrjOPJfeoPx2rWucbD2AoU53SmgkDFN2bPLc7YSDRx9vDLHjnp%2F9ah6vSTT4fwSUcjZHMXsMuXpNeATe6kpj%2F0BYL%2FwUzzMnaDvasQjOfuPxY4dkEbbzCMymilLE44Yyj%2FTbiKea5MAYe4XiQkt%2BKyQc9RkbLwkp2dgUHEGU6nf4eL9EOuPOVdR8rvaSdeRD7v%2FjWCytgqV8hot7yQQegEG7DC7Vr5kxjPI4QdxoTrxI8azRojcS%2BQln6YBavd1%2BQStlTdKTJzVecjB1qnqaIiB2yo8Y2laHlkShGDJulcUhQyPAN5BB%2F2ioMfKeXFwGyDK%2F3djwzpSxttQirIwkrzpvAY6pgGztBSbUK%2BacpyUxfda3hak88EXutr%2BNLInLmpCOx%2B2IKWknbaUl1j2XiORlh9EWaP9jaVC3KNzNTzc7Cn%2Fee4uT6FqbsCW39WTbSM3DKfAAFkcxwpYUICDjaQFh9d4i7CkFauPrYl%2Fzm4r42aqChO1gYTQqMG90RXQqJoKpqLRIgjw65VDHkONdspGVMxEQrOuKXUHPpkF16l6K9R8raSpwcFZFi6s&X-Amz-Signature=330cd7be77370630d4f0df63469cd0f681bf1dfc12fff109a2c35f18ff927361&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WA4V76EN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDN8EeG8y%2FZbehUEyJvtG5xYlEInViB2aDVjKZCAo88AAiEA8TlhR8xVjrQ6bwySseqRSKxD6mSSsIaXNgv1DHDtqJgqiAQIkv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNBS7DmF892Ejg0vzircA5iPTeqjMP2e8QiI2XxoJH5kCBBj8%2BaWSxHGLpVT7dNw0A6WtA8ZtGDHiXO7SoQikS8xl%2B4DjhQOYt75ESEePl%2F29l%2Bk7iVAp017rMspL7%2BIC0Kh6N5g5diag4j1HTX%2BYOFXzn7PbBoKZltanA2zTe9GJzUcSI4NGZxEMBj6gvK1RW%2FxA5LTSfiqcgAZxz2%2BoKtUUdUWNYIXdpX0iw049lzwmGAk0uI38wjviRVKqgD5Epm7InXZ1AjVApEpxRAgILUN3KIWgcE7zfJuBlbJZAbg7kVn212EbW1H9yQAUgiuxkdIl68GxpLHZUqb7PvdjHXFdWM8PMyNirZrFMwYG7mpX00x03DArW338RC9GKM7MJzSkxp3z4TSxSFgB4rnl3RmdnCj33pz9nR10CKoXLnzBY3CWwND%2B0bN1na3WFCgJSxezfXFRDodYbH65dZZ7HivlrgrXsDIVmy5OaV0kEWjaULm60FABhyOmmTd1vsSx2oi2zlZSaONUTlicfO9ECRs3e%2FZ7GKPTNsE1%2Fm0TTiiUGjZ%2FIl83VhMGXAQMQ57j2RcFqIoiEfj1hnBxyQd3WAoK3fqPThY33%2BJref6B%2B0yJuwolQZaJ9cP03ZC8274PGFu3FQkG6LkfGT7MPW76bwGOqUB4wY2iQ9XGS%2F9V5EMc6bwWFcGAXIIb3GTDXJqFPn%2BuQckDOPq%2F6BcwqRALKoWZIb%2BpeJOlDspMOIRnQGMSPqKCFmIDrkR%2B5bBbwa4Psa7K8Ud87YpXXchuRghFVeCqW5u118w9hZWX90ydSYS4q7Ttt2apO65n0KKRxYNMdm80xlYHvkGuzTwJjD5XPaxw9I0ZFa7QV5rAIz0c02%2B21gUaAqsJE7N&X-Amz-Signature=f6f1f75414e0aa39866169fec625c9fe4b154c6b2d00bb3fe255d87617a849c5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WA4V76EN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDN8EeG8y%2FZbehUEyJvtG5xYlEInViB2aDVjKZCAo88AAiEA8TlhR8xVjrQ6bwySseqRSKxD6mSSsIaXNgv1DHDtqJgqiAQIkv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNBS7DmF892Ejg0vzircA5iPTeqjMP2e8QiI2XxoJH5kCBBj8%2BaWSxHGLpVT7dNw0A6WtA8ZtGDHiXO7SoQikS8xl%2B4DjhQOYt75ESEePl%2F29l%2Bk7iVAp017rMspL7%2BIC0Kh6N5g5diag4j1HTX%2BYOFXzn7PbBoKZltanA2zTe9GJzUcSI4NGZxEMBj6gvK1RW%2FxA5LTSfiqcgAZxz2%2BoKtUUdUWNYIXdpX0iw049lzwmGAk0uI38wjviRVKqgD5Epm7InXZ1AjVApEpxRAgILUN3KIWgcE7zfJuBlbJZAbg7kVn212EbW1H9yQAUgiuxkdIl68GxpLHZUqb7PvdjHXFdWM8PMyNirZrFMwYG7mpX00x03DArW338RC9GKM7MJzSkxp3z4TSxSFgB4rnl3RmdnCj33pz9nR10CKoXLnzBY3CWwND%2B0bN1na3WFCgJSxezfXFRDodYbH65dZZ7HivlrgrXsDIVmy5OaV0kEWjaULm60FABhyOmmTd1vsSx2oi2zlZSaONUTlicfO9ECRs3e%2FZ7GKPTNsE1%2Fm0TTiiUGjZ%2FIl83VhMGXAQMQ57j2RcFqIoiEfj1hnBxyQd3WAoK3fqPThY33%2BJref6B%2B0yJuwolQZaJ9cP03ZC8274PGFu3FQkG6LkfGT7MPW76bwGOqUB4wY2iQ9XGS%2F9V5EMc6bwWFcGAXIIb3GTDXJqFPn%2BuQckDOPq%2F6BcwqRALKoWZIb%2BpeJOlDspMOIRnQGMSPqKCFmIDrkR%2B5bBbwa4Psa7K8Ud87YpXXchuRghFVeCqW5u118w9hZWX90ydSYS4q7Ttt2apO65n0KKRxYNMdm80xlYHvkGuzTwJjD5XPaxw9I0ZFa7QV5rAIz0c02%2B21gUaAqsJE7N&X-Amz-Signature=7aecce4d39ca25e569948528136feada43a2079653f69ba8a66534413564f5ed&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
