

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFHTF2KM%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCsSgmHvSQAv9YPKFz62I0rdq4ehQ5N5OBblQVLdVSAZwIhAKUGQSmwoYXMbD7AEsZhUP0JTAaYdNy2nr8%2FzORYRfpGKv8DCDkQABoMNjM3NDIzMTgzODA1Igze5gW2wkO8%2BRGJmNMq3AMFpm7Hed8%2FPvlnTPiicC%2FUKyx2NxHSieCJ1fatW8EaS2re%2B0zlKbOZEns8FnG%2BRe%2FAQLxKsC%2F%2BBsRPzZwk5M4aKE7UWFvopl6mpvk1rQPCYLTzRnjplOj%2B8Dvj6ZwcOslfMYwG5tu7%2F%2F0GeC8pxKcNL8q1IgVogZen2NsjjB8coFg6oprczmELAiTm6oiu02ErZf7JCBFVEZJXyRm1VJ0S9LbEDvPVU25PF7%2FQCiRIurvUnBdnmAKG96ZhkTgFlgu5L6tb9exnNdM4dgYqRxnQZPXjshr3377HE3oWHCWXKkdi1Sw0HvhuMYDtKzLiB6Z5kI3fEIzrb6Kv8Bc9WZcaOAUq4Vj8Md6Spul3V94sYj1wBW1XLiLGWgqum97JtufG6yuQtUiKlTib88Bx7WraIGowTdwqeJ%2FRgwers7dw4fsSWCQstNkaft8%2F8H%2BycUSifiPYTsa9C592YqKRokYP261bC6KCURYzLnJUFjJWjsDMudMZKs4fVzd6H6hnXlFQ3lMcONPuvyqYKB%2Bzh4zi624uPjDAd%2Fhx%2BIT6xu6bGBEUhhW6CoKYo%2BTsfjoYXE02vK1t6WejfuKCChLjTj%2FlUYaVWyegi7rOmydIZZCjQ10BPGyKuSFTbWLz3TCZzYq9BjqkAWFbUT0241BbDhvuTBzDSeSyHFCt5V7yVcxKViSK4uYFAG3f2XNb32E4GmLQQZLoatbmjB03r0arY7WN8x3dBy2sKLaeiHA%2FmRF215nyn9%2Fk%2FGnZOiKwFR36tWIc9Eu2a9GJY%2BwbSPJHlCEF9KoJNPOqpflVx66pqw4y7M0DmCWk3gFUcIkuDWoDuCoM3bAOfH2hoqACMdPlHVV%2BfC8HUW7ZFpl6&X-Amz-Signature=f5115878c32183ed7106554a3cdd0a0c18169277b7bf0308bd40ae5fcd5555d4&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFHTF2KM%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCsSgmHvSQAv9YPKFz62I0rdq4ehQ5N5OBblQVLdVSAZwIhAKUGQSmwoYXMbD7AEsZhUP0JTAaYdNy2nr8%2FzORYRfpGKv8DCDkQABoMNjM3NDIzMTgzODA1Igze5gW2wkO8%2BRGJmNMq3AMFpm7Hed8%2FPvlnTPiicC%2FUKyx2NxHSieCJ1fatW8EaS2re%2B0zlKbOZEns8FnG%2BRe%2FAQLxKsC%2F%2BBsRPzZwk5M4aKE7UWFvopl6mpvk1rQPCYLTzRnjplOj%2B8Dvj6ZwcOslfMYwG5tu7%2F%2F0GeC8pxKcNL8q1IgVogZen2NsjjB8coFg6oprczmELAiTm6oiu02ErZf7JCBFVEZJXyRm1VJ0S9LbEDvPVU25PF7%2FQCiRIurvUnBdnmAKG96ZhkTgFlgu5L6tb9exnNdM4dgYqRxnQZPXjshr3377HE3oWHCWXKkdi1Sw0HvhuMYDtKzLiB6Z5kI3fEIzrb6Kv8Bc9WZcaOAUq4Vj8Md6Spul3V94sYj1wBW1XLiLGWgqum97JtufG6yuQtUiKlTib88Bx7WraIGowTdwqeJ%2FRgwers7dw4fsSWCQstNkaft8%2F8H%2BycUSifiPYTsa9C592YqKRokYP261bC6KCURYzLnJUFjJWjsDMudMZKs4fVzd6H6hnXlFQ3lMcONPuvyqYKB%2Bzh4zi624uPjDAd%2Fhx%2BIT6xu6bGBEUhhW6CoKYo%2BTsfjoYXE02vK1t6WejfuKCChLjTj%2FlUYaVWyegi7rOmydIZZCjQ10BPGyKuSFTbWLz3TCZzYq9BjqkAWFbUT0241BbDhvuTBzDSeSyHFCt5V7yVcxKViSK4uYFAG3f2XNb32E4GmLQQZLoatbmjB03r0arY7WN8x3dBy2sKLaeiHA%2FmRF215nyn9%2Fk%2FGnZOiKwFR36tWIc9Eu2a9GJY%2BwbSPJHlCEF9KoJNPOqpflVx66pqw4y7M0DmCWk3gFUcIkuDWoDuCoM3bAOfH2hoqACMdPlHVV%2BfC8HUW7ZFpl6&X-Amz-Signature=84b7a7ede09da8556ff5a5e9569a6c669dcbda5367c7140218b723b02e3cd3a9&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFHTF2KM%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCsSgmHvSQAv9YPKFz62I0rdq4ehQ5N5OBblQVLdVSAZwIhAKUGQSmwoYXMbD7AEsZhUP0JTAaYdNy2nr8%2FzORYRfpGKv8DCDkQABoMNjM3NDIzMTgzODA1Igze5gW2wkO8%2BRGJmNMq3AMFpm7Hed8%2FPvlnTPiicC%2FUKyx2NxHSieCJ1fatW8EaS2re%2B0zlKbOZEns8FnG%2BRe%2FAQLxKsC%2F%2BBsRPzZwk5M4aKE7UWFvopl6mpvk1rQPCYLTzRnjplOj%2B8Dvj6ZwcOslfMYwG5tu7%2F%2F0GeC8pxKcNL8q1IgVogZen2NsjjB8coFg6oprczmELAiTm6oiu02ErZf7JCBFVEZJXyRm1VJ0S9LbEDvPVU25PF7%2FQCiRIurvUnBdnmAKG96ZhkTgFlgu5L6tb9exnNdM4dgYqRxnQZPXjshr3377HE3oWHCWXKkdi1Sw0HvhuMYDtKzLiB6Z5kI3fEIzrb6Kv8Bc9WZcaOAUq4Vj8Md6Spul3V94sYj1wBW1XLiLGWgqum97JtufG6yuQtUiKlTib88Bx7WraIGowTdwqeJ%2FRgwers7dw4fsSWCQstNkaft8%2F8H%2BycUSifiPYTsa9C592YqKRokYP261bC6KCURYzLnJUFjJWjsDMudMZKs4fVzd6H6hnXlFQ3lMcONPuvyqYKB%2Bzh4zi624uPjDAd%2Fhx%2BIT6xu6bGBEUhhW6CoKYo%2BTsfjoYXE02vK1t6WejfuKCChLjTj%2FlUYaVWyegi7rOmydIZZCjQ10BPGyKuSFTbWLz3TCZzYq9BjqkAWFbUT0241BbDhvuTBzDSeSyHFCt5V7yVcxKViSK4uYFAG3f2XNb32E4GmLQQZLoatbmjB03r0arY7WN8x3dBy2sKLaeiHA%2FmRF215nyn9%2Fk%2FGnZOiKwFR36tWIc9Eu2a9GJY%2BwbSPJHlCEF9KoJNPOqpflVx66pqw4y7M0DmCWk3gFUcIkuDWoDuCoM3bAOfH2hoqACMdPlHVV%2BfC8HUW7ZFpl6&X-Amz-Signature=6c39d55aad16c4fc77d54c799e2db1b16b723f02489601592374e825b1258ad2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFHTF2KM%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCsSgmHvSQAv9YPKFz62I0rdq4ehQ5N5OBblQVLdVSAZwIhAKUGQSmwoYXMbD7AEsZhUP0JTAaYdNy2nr8%2FzORYRfpGKv8DCDkQABoMNjM3NDIzMTgzODA1Igze5gW2wkO8%2BRGJmNMq3AMFpm7Hed8%2FPvlnTPiicC%2FUKyx2NxHSieCJ1fatW8EaS2re%2B0zlKbOZEns8FnG%2BRe%2FAQLxKsC%2F%2BBsRPzZwk5M4aKE7UWFvopl6mpvk1rQPCYLTzRnjplOj%2B8Dvj6ZwcOslfMYwG5tu7%2F%2F0GeC8pxKcNL8q1IgVogZen2NsjjB8coFg6oprczmELAiTm6oiu02ErZf7JCBFVEZJXyRm1VJ0S9LbEDvPVU25PF7%2FQCiRIurvUnBdnmAKG96ZhkTgFlgu5L6tb9exnNdM4dgYqRxnQZPXjshr3377HE3oWHCWXKkdi1Sw0HvhuMYDtKzLiB6Z5kI3fEIzrb6Kv8Bc9WZcaOAUq4Vj8Md6Spul3V94sYj1wBW1XLiLGWgqum97JtufG6yuQtUiKlTib88Bx7WraIGowTdwqeJ%2FRgwers7dw4fsSWCQstNkaft8%2F8H%2BycUSifiPYTsa9C592YqKRokYP261bC6KCURYzLnJUFjJWjsDMudMZKs4fVzd6H6hnXlFQ3lMcONPuvyqYKB%2Bzh4zi624uPjDAd%2Fhx%2BIT6xu6bGBEUhhW6CoKYo%2BTsfjoYXE02vK1t6WejfuKCChLjTj%2FlUYaVWyegi7rOmydIZZCjQ10BPGyKuSFTbWLz3TCZzYq9BjqkAWFbUT0241BbDhvuTBzDSeSyHFCt5V7yVcxKViSK4uYFAG3f2XNb32E4GmLQQZLoatbmjB03r0arY7WN8x3dBy2sKLaeiHA%2FmRF215nyn9%2Fk%2FGnZOiKwFR36tWIc9Eu2a9GJY%2BwbSPJHlCEF9KoJNPOqpflVx66pqw4y7M0DmCWk3gFUcIkuDWoDuCoM3bAOfH2hoqACMdPlHVV%2BfC8HUW7ZFpl6&X-Amz-Signature=58791a415d55cba77ca230333941ba903e8ddafa1304e2e68b7bbdb92ac1f1f1&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFHTF2KM%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCsSgmHvSQAv9YPKFz62I0rdq4ehQ5N5OBblQVLdVSAZwIhAKUGQSmwoYXMbD7AEsZhUP0JTAaYdNy2nr8%2FzORYRfpGKv8DCDkQABoMNjM3NDIzMTgzODA1Igze5gW2wkO8%2BRGJmNMq3AMFpm7Hed8%2FPvlnTPiicC%2FUKyx2NxHSieCJ1fatW8EaS2re%2B0zlKbOZEns8FnG%2BRe%2FAQLxKsC%2F%2BBsRPzZwk5M4aKE7UWFvopl6mpvk1rQPCYLTzRnjplOj%2B8Dvj6ZwcOslfMYwG5tu7%2F%2F0GeC8pxKcNL8q1IgVogZen2NsjjB8coFg6oprczmELAiTm6oiu02ErZf7JCBFVEZJXyRm1VJ0S9LbEDvPVU25PF7%2FQCiRIurvUnBdnmAKG96ZhkTgFlgu5L6tb9exnNdM4dgYqRxnQZPXjshr3377HE3oWHCWXKkdi1Sw0HvhuMYDtKzLiB6Z5kI3fEIzrb6Kv8Bc9WZcaOAUq4Vj8Md6Spul3V94sYj1wBW1XLiLGWgqum97JtufG6yuQtUiKlTib88Bx7WraIGowTdwqeJ%2FRgwers7dw4fsSWCQstNkaft8%2F8H%2BycUSifiPYTsa9C592YqKRokYP261bC6KCURYzLnJUFjJWjsDMudMZKs4fVzd6H6hnXlFQ3lMcONPuvyqYKB%2Bzh4zi624uPjDAd%2Fhx%2BIT6xu6bGBEUhhW6CoKYo%2BTsfjoYXE02vK1t6WejfuKCChLjTj%2FlUYaVWyegi7rOmydIZZCjQ10BPGyKuSFTbWLz3TCZzYq9BjqkAWFbUT0241BbDhvuTBzDSeSyHFCt5V7yVcxKViSK4uYFAG3f2XNb32E4GmLQQZLoatbmjB03r0arY7WN8x3dBy2sKLaeiHA%2FmRF215nyn9%2Fk%2FGnZOiKwFR36tWIc9Eu2a9GJY%2BwbSPJHlCEF9KoJNPOqpflVx66pqw4y7M0DmCWk3gFUcIkuDWoDuCoM3bAOfH2hoqACMdPlHVV%2BfC8HUW7ZFpl6&X-Amz-Signature=ed535262fd5a71cfa264b40198c1f560104b10b7b476170be545fbc36fa03b06&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFHTF2KM%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCsSgmHvSQAv9YPKFz62I0rdq4ehQ5N5OBblQVLdVSAZwIhAKUGQSmwoYXMbD7AEsZhUP0JTAaYdNy2nr8%2FzORYRfpGKv8DCDkQABoMNjM3NDIzMTgzODA1Igze5gW2wkO8%2BRGJmNMq3AMFpm7Hed8%2FPvlnTPiicC%2FUKyx2NxHSieCJ1fatW8EaS2re%2B0zlKbOZEns8FnG%2BRe%2FAQLxKsC%2F%2BBsRPzZwk5M4aKE7UWFvopl6mpvk1rQPCYLTzRnjplOj%2B8Dvj6ZwcOslfMYwG5tu7%2F%2F0GeC8pxKcNL8q1IgVogZen2NsjjB8coFg6oprczmELAiTm6oiu02ErZf7JCBFVEZJXyRm1VJ0S9LbEDvPVU25PF7%2FQCiRIurvUnBdnmAKG96ZhkTgFlgu5L6tb9exnNdM4dgYqRxnQZPXjshr3377HE3oWHCWXKkdi1Sw0HvhuMYDtKzLiB6Z5kI3fEIzrb6Kv8Bc9WZcaOAUq4Vj8Md6Spul3V94sYj1wBW1XLiLGWgqum97JtufG6yuQtUiKlTib88Bx7WraIGowTdwqeJ%2FRgwers7dw4fsSWCQstNkaft8%2F8H%2BycUSifiPYTsa9C592YqKRokYP261bC6KCURYzLnJUFjJWjsDMudMZKs4fVzd6H6hnXlFQ3lMcONPuvyqYKB%2Bzh4zi624uPjDAd%2Fhx%2BIT6xu6bGBEUhhW6CoKYo%2BTsfjoYXE02vK1t6WejfuKCChLjTj%2FlUYaVWyegi7rOmydIZZCjQ10BPGyKuSFTbWLz3TCZzYq9BjqkAWFbUT0241BbDhvuTBzDSeSyHFCt5V7yVcxKViSK4uYFAG3f2XNb32E4GmLQQZLoatbmjB03r0arY7WN8x3dBy2sKLaeiHA%2FmRF215nyn9%2Fk%2FGnZOiKwFR36tWIc9Eu2a9GJY%2BwbSPJHlCEF9KoJNPOqpflVx66pqw4y7M0DmCWk3gFUcIkuDWoDuCoM3bAOfH2hoqACMdPlHVV%2BfC8HUW7ZFpl6&X-Amz-Signature=4bbb659e7d487d69b9d2e50d3375f5134049548548ee26b47620bd400a92758a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFHTF2KM%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCsSgmHvSQAv9YPKFz62I0rdq4ehQ5N5OBblQVLdVSAZwIhAKUGQSmwoYXMbD7AEsZhUP0JTAaYdNy2nr8%2FzORYRfpGKv8DCDkQABoMNjM3NDIzMTgzODA1Igze5gW2wkO8%2BRGJmNMq3AMFpm7Hed8%2FPvlnTPiicC%2FUKyx2NxHSieCJ1fatW8EaS2re%2B0zlKbOZEns8FnG%2BRe%2FAQLxKsC%2F%2BBsRPzZwk5M4aKE7UWFvopl6mpvk1rQPCYLTzRnjplOj%2B8Dvj6ZwcOslfMYwG5tu7%2F%2F0GeC8pxKcNL8q1IgVogZen2NsjjB8coFg6oprczmELAiTm6oiu02ErZf7JCBFVEZJXyRm1VJ0S9LbEDvPVU25PF7%2FQCiRIurvUnBdnmAKG96ZhkTgFlgu5L6tb9exnNdM4dgYqRxnQZPXjshr3377HE3oWHCWXKkdi1Sw0HvhuMYDtKzLiB6Z5kI3fEIzrb6Kv8Bc9WZcaOAUq4Vj8Md6Spul3V94sYj1wBW1XLiLGWgqum97JtufG6yuQtUiKlTib88Bx7WraIGowTdwqeJ%2FRgwers7dw4fsSWCQstNkaft8%2F8H%2BycUSifiPYTsa9C592YqKRokYP261bC6KCURYzLnJUFjJWjsDMudMZKs4fVzd6H6hnXlFQ3lMcONPuvyqYKB%2Bzh4zi624uPjDAd%2Fhx%2BIT6xu6bGBEUhhW6CoKYo%2BTsfjoYXE02vK1t6WejfuKCChLjTj%2FlUYaVWyegi7rOmydIZZCjQ10BPGyKuSFTbWLz3TCZzYq9BjqkAWFbUT0241BbDhvuTBzDSeSyHFCt5V7yVcxKViSK4uYFAG3f2XNb32E4GmLQQZLoatbmjB03r0arY7WN8x3dBy2sKLaeiHA%2FmRF215nyn9%2Fk%2FGnZOiKwFR36tWIc9Eu2a9GJY%2BwbSPJHlCEF9KoJNPOqpflVx66pqw4y7M0DmCWk3gFUcIkuDWoDuCoM3bAOfH2hoqACMdPlHVV%2BfC8HUW7ZFpl6&X-Amz-Signature=3519688705dd3159b58051551bf19f40fac850040ebc35a42782c19888b31fa9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFHTF2KM%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCsSgmHvSQAv9YPKFz62I0rdq4ehQ5N5OBblQVLdVSAZwIhAKUGQSmwoYXMbD7AEsZhUP0JTAaYdNy2nr8%2FzORYRfpGKv8DCDkQABoMNjM3NDIzMTgzODA1Igze5gW2wkO8%2BRGJmNMq3AMFpm7Hed8%2FPvlnTPiicC%2FUKyx2NxHSieCJ1fatW8EaS2re%2B0zlKbOZEns8FnG%2BRe%2FAQLxKsC%2F%2BBsRPzZwk5M4aKE7UWFvopl6mpvk1rQPCYLTzRnjplOj%2B8Dvj6ZwcOslfMYwG5tu7%2F%2F0GeC8pxKcNL8q1IgVogZen2NsjjB8coFg6oprczmELAiTm6oiu02ErZf7JCBFVEZJXyRm1VJ0S9LbEDvPVU25PF7%2FQCiRIurvUnBdnmAKG96ZhkTgFlgu5L6tb9exnNdM4dgYqRxnQZPXjshr3377HE3oWHCWXKkdi1Sw0HvhuMYDtKzLiB6Z5kI3fEIzrb6Kv8Bc9WZcaOAUq4Vj8Md6Spul3V94sYj1wBW1XLiLGWgqum97JtufG6yuQtUiKlTib88Bx7WraIGowTdwqeJ%2FRgwers7dw4fsSWCQstNkaft8%2F8H%2BycUSifiPYTsa9C592YqKRokYP261bC6KCURYzLnJUFjJWjsDMudMZKs4fVzd6H6hnXlFQ3lMcONPuvyqYKB%2Bzh4zi624uPjDAd%2Fhx%2BIT6xu6bGBEUhhW6CoKYo%2BTsfjoYXE02vK1t6WejfuKCChLjTj%2FlUYaVWyegi7rOmydIZZCjQ10BPGyKuSFTbWLz3TCZzYq9BjqkAWFbUT0241BbDhvuTBzDSeSyHFCt5V7yVcxKViSK4uYFAG3f2XNb32E4GmLQQZLoatbmjB03r0arY7WN8x3dBy2sKLaeiHA%2FmRF215nyn9%2Fk%2FGnZOiKwFR36tWIc9Eu2a9GJY%2BwbSPJHlCEF9KoJNPOqpflVx66pqw4y7M0DmCWk3gFUcIkuDWoDuCoM3bAOfH2hoqACMdPlHVV%2BfC8HUW7ZFpl6&X-Amz-Signature=c8e6a097b2f25329041e01471951a1e9dcec9034be2f2a86efe0e446340f4898&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFHTF2KM%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCsSgmHvSQAv9YPKFz62I0rdq4ehQ5N5OBblQVLdVSAZwIhAKUGQSmwoYXMbD7AEsZhUP0JTAaYdNy2nr8%2FzORYRfpGKv8DCDkQABoMNjM3NDIzMTgzODA1Igze5gW2wkO8%2BRGJmNMq3AMFpm7Hed8%2FPvlnTPiicC%2FUKyx2NxHSieCJ1fatW8EaS2re%2B0zlKbOZEns8FnG%2BRe%2FAQLxKsC%2F%2BBsRPzZwk5M4aKE7UWFvopl6mpvk1rQPCYLTzRnjplOj%2B8Dvj6ZwcOslfMYwG5tu7%2F%2F0GeC8pxKcNL8q1IgVogZen2NsjjB8coFg6oprczmELAiTm6oiu02ErZf7JCBFVEZJXyRm1VJ0S9LbEDvPVU25PF7%2FQCiRIurvUnBdnmAKG96ZhkTgFlgu5L6tb9exnNdM4dgYqRxnQZPXjshr3377HE3oWHCWXKkdi1Sw0HvhuMYDtKzLiB6Z5kI3fEIzrb6Kv8Bc9WZcaOAUq4Vj8Md6Spul3V94sYj1wBW1XLiLGWgqum97JtufG6yuQtUiKlTib88Bx7WraIGowTdwqeJ%2FRgwers7dw4fsSWCQstNkaft8%2F8H%2BycUSifiPYTsa9C592YqKRokYP261bC6KCURYzLnJUFjJWjsDMudMZKs4fVzd6H6hnXlFQ3lMcONPuvyqYKB%2Bzh4zi624uPjDAd%2Fhx%2BIT6xu6bGBEUhhW6CoKYo%2BTsfjoYXE02vK1t6WejfuKCChLjTj%2FlUYaVWyegi7rOmydIZZCjQ10BPGyKuSFTbWLz3TCZzYq9BjqkAWFbUT0241BbDhvuTBzDSeSyHFCt5V7yVcxKViSK4uYFAG3f2XNb32E4GmLQQZLoatbmjB03r0arY7WN8x3dBy2sKLaeiHA%2FmRF215nyn9%2Fk%2FGnZOiKwFR36tWIc9Eu2a9GJY%2BwbSPJHlCEF9KoJNPOqpflVx66pqw4y7M0DmCWk3gFUcIkuDWoDuCoM3bAOfH2hoqACMdPlHVV%2BfC8HUW7ZFpl6&X-Amz-Signature=9f40fbde05241e17b5d201ab6edfab7e688d362e8281bc47df60e3ac1247b35d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RGP3HEQR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041753Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCICSbke8WlNaHAQglroskllUuDViB3HPaoz%2FWJvycUkvPAiEA74r3Ej5pYbOFs4fBq%2BdivX%2Fx%2B42%2Bms0WrjplajjlelUq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDEyW0PYZmVPpZlVewCrcA160eRIHwhvS5CbKPgdU6FEHsz8fYr0RZwUESvchel4YqRiFXXaqrPldqReFkJrjRjxv73kAObCXtM1iNcN8%2BKabzMnXhjuO17sMKmcL%2BviiGd4OeHld%2F0VRb7kzlYMknKE3i%2F70dZiyfLpoSYrfcLiMxvZTvGtFLohGUTWbnawklqMlnQT3y8koX3zi8buBqIv7sFb78yUj9CJOiCi4MmGEBs5jOnah4tD3f%2FXSS0BkvSUUlI68H0cySsAl6b7KTNQs%2BNsrDYjVloYp3qJsAazGVAFbNc19ioj%2Fvt9RYw06cUvD1R2QMif0z6%2BV2AOjy94z%2Bm%2BKinssY0QfxWeAOlhIXJBXVnPXMTXApfZLRGQ83qKD0zCajdEuu52%2FuRKH%2FkHRuuungOKJhrm7Hl5m%2FLmL9230kwFXIjvhGafgVEX2Lxv76VCMGapBWd9bVuhalJyUWJYGsCi26OJO9tM%2B8saM1S0X3TGmr40C8BFPra3z8fSKBT6KGHELNjDKQItsmPm94dCvPEyqvKoD8HsWpCHP%2BwtKQngZr1ORE1H2Ie%2BtFx1fyvu1gXzHXfKByDqLjteeeA0A7zMuVktpIzwbLVVFvso2ZquoY4sJoY8wSRyXZIpu0xgSuVmq64aSMLvNir0GOqUB5z5cMy0AB4cV%2BgNNJKRx%2B3Y8RZmJ5GRr7bJxVcaXENmHoQb9Qt5eNGdPS36VZdjjHcqWIgifrZ1cJrWsBiQBnjj9QGqkZPbFCFvmio9SNe1P3Q8VV9w7cGaXfjONYH0%2Bcf2FgqOJKqGcEXhviEQvUxREAUK4f5s9bICQUA6n%2BsSDj8ZAS814oLR2BPnyEHW56H0Fn4wA9FdDd9%2BJQn6b7sFekcz%2F&X-Amz-Signature=ce4c870c84ee236b6d8e5e589d325b9b6de7e52156c92e9b013962be77ee7175&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RGP3HEQR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041753Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCICSbke8WlNaHAQglroskllUuDViB3HPaoz%2FWJvycUkvPAiEA74r3Ej5pYbOFs4fBq%2BdivX%2Fx%2B42%2Bms0WrjplajjlelUq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDEyW0PYZmVPpZlVewCrcA160eRIHwhvS5CbKPgdU6FEHsz8fYr0RZwUESvchel4YqRiFXXaqrPldqReFkJrjRjxv73kAObCXtM1iNcN8%2BKabzMnXhjuO17sMKmcL%2BviiGd4OeHld%2F0VRb7kzlYMknKE3i%2F70dZiyfLpoSYrfcLiMxvZTvGtFLohGUTWbnawklqMlnQT3y8koX3zi8buBqIv7sFb78yUj9CJOiCi4MmGEBs5jOnah4tD3f%2FXSS0BkvSUUlI68H0cySsAl6b7KTNQs%2BNsrDYjVloYp3qJsAazGVAFbNc19ioj%2Fvt9RYw06cUvD1R2QMif0z6%2BV2AOjy94z%2Bm%2BKinssY0QfxWeAOlhIXJBXVnPXMTXApfZLRGQ83qKD0zCajdEuu52%2FuRKH%2FkHRuuungOKJhrm7Hl5m%2FLmL9230kwFXIjvhGafgVEX2Lxv76VCMGapBWd9bVuhalJyUWJYGsCi26OJO9tM%2B8saM1S0X3TGmr40C8BFPra3z8fSKBT6KGHELNjDKQItsmPm94dCvPEyqvKoD8HsWpCHP%2BwtKQngZr1ORE1H2Ie%2BtFx1fyvu1gXzHXfKByDqLjteeeA0A7zMuVktpIzwbLVVFvso2ZquoY4sJoY8wSRyXZIpu0xgSuVmq64aSMLvNir0GOqUB5z5cMy0AB4cV%2BgNNJKRx%2B3Y8RZmJ5GRr7bJxVcaXENmHoQb9Qt5eNGdPS36VZdjjHcqWIgifrZ1cJrWsBiQBnjj9QGqkZPbFCFvmio9SNe1P3Q8VV9w7cGaXfjONYH0%2Bcf2FgqOJKqGcEXhviEQvUxREAUK4f5s9bICQUA6n%2BsSDj8ZAS814oLR2BPnyEHW56H0Fn4wA9FdDd9%2BJQn6b7sFekcz%2F&X-Amz-Signature=50eea9650ffdf2c37fcbd7c0d82b42210b7d9abd47a7594222945f10e6bff8c3&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
