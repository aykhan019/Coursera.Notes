

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSZJOAZU%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDcpHiHa0FbW2Xk%2BoANxZz0qfRA5kbWT09iUnENIGCOtQIhANtEJUtRkyE0NS8P4D4UOCW9MC4DP4fBgXX%2FUdqHYOknKogECMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwgy9mRRiJrjEvzJ5Mq3AMn1Nfq8ZxLWyp93ANCIGhOvCkTjEXSuYB4ZN0LXthBzgGW9Jt2VGx2%2B1D%2Bk9j9PU%2F7%2FcyEu2tdgQfdJFN3Dyx1eQTA7KygzJjSrltc3ONg%2Bil4OiFknGWPPxLqhhXBHWbvzuGj20xZKsnJjMAB5g1wYul4n1KJK4ZwJfFVfYggIOMuFB5WV8%2BCZjX%2FG%2FsDRCZo939gSQWy76JtpJxKI6rC5srX76PgVpc0hwA44sJ6SU9RXhMu3SzeWkigV45oLfew3P1AZVHq3KnOkjbQ1cuc9NMkBQbyYQPLH2fo88ow9HIN45CGTudgQSzgGS5vsX0h1yIEMdTbf8E1tEIzaGm94VVxAjlGxzqu1kYWQvirPcPKkOw8ONv0LII71j3kebiRuFeB0QArYk%2F8i0TBIH4NC7rhTSAYKn3Qvjy%2FyZvuSHPqHiyXsk5u1phzIauImkSASIIY3CXEW73QP4QBa2DZZ1qSdOEbovN5Tmk5bIoXBHWRcCIWuX38coUDZHk5qHQN%2Bq7Mag2rHHv4T0lS4QZWKdGq9aNH4C2VT%2Fm7upQJtMDR%2FHtV7WP1eHAET53OVnWVmnywIwXFz2cKYIUS2XRMEJrkxV%2FtvQK%2Be9gf%2BR4DRP1VpOr3KjB0ViFAqTDE7PW8BjqkAfxGfqq%2FU2ti76T%2F2EwxnoNbLh%2B9h6M3Ekg57oTp1S5qNSbLiQFJRufqofz%2B%2BYKcsZiegvkbAMs7a%2FQiouyPNkJjVbRiRnt5Nv8nB4xaXAJuCJwYTJ9Z%2FhhV9Cc7Sg9jWZP3YrMeXoTGON0DYAUmb1Kd5HT44Q1klCL2Nb6gFRHajm9dvWYOFUK1ayZ9qr8fwu8z5pG8HC7YC1DIx7WbxVWAkxbK&X-Amz-Signature=68539b51bb8b034c6dbee6879e0227145c05a086e1537febebfd93b5c2c7725d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSZJOAZU%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDcpHiHa0FbW2Xk%2BoANxZz0qfRA5kbWT09iUnENIGCOtQIhANtEJUtRkyE0NS8P4D4UOCW9MC4DP4fBgXX%2FUdqHYOknKogECMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwgy9mRRiJrjEvzJ5Mq3AMn1Nfq8ZxLWyp93ANCIGhOvCkTjEXSuYB4ZN0LXthBzgGW9Jt2VGx2%2B1D%2Bk9j9PU%2F7%2FcyEu2tdgQfdJFN3Dyx1eQTA7KygzJjSrltc3ONg%2Bil4OiFknGWPPxLqhhXBHWbvzuGj20xZKsnJjMAB5g1wYul4n1KJK4ZwJfFVfYggIOMuFB5WV8%2BCZjX%2FG%2FsDRCZo939gSQWy76JtpJxKI6rC5srX76PgVpc0hwA44sJ6SU9RXhMu3SzeWkigV45oLfew3P1AZVHq3KnOkjbQ1cuc9NMkBQbyYQPLH2fo88ow9HIN45CGTudgQSzgGS5vsX0h1yIEMdTbf8E1tEIzaGm94VVxAjlGxzqu1kYWQvirPcPKkOw8ONv0LII71j3kebiRuFeB0QArYk%2F8i0TBIH4NC7rhTSAYKn3Qvjy%2FyZvuSHPqHiyXsk5u1phzIauImkSASIIY3CXEW73QP4QBa2DZZ1qSdOEbovN5Tmk5bIoXBHWRcCIWuX38coUDZHk5qHQN%2Bq7Mag2rHHv4T0lS4QZWKdGq9aNH4C2VT%2Fm7upQJtMDR%2FHtV7WP1eHAET53OVnWVmnywIwXFz2cKYIUS2XRMEJrkxV%2FtvQK%2Be9gf%2BR4DRP1VpOr3KjB0ViFAqTDE7PW8BjqkAfxGfqq%2FU2ti76T%2F2EwxnoNbLh%2B9h6M3Ekg57oTp1S5qNSbLiQFJRufqofz%2B%2BYKcsZiegvkbAMs7a%2FQiouyPNkJjVbRiRnt5Nv8nB4xaXAJuCJwYTJ9Z%2FhhV9Cc7Sg9jWZP3YrMeXoTGON0DYAUmb1Kd5HT44Q1klCL2Nb6gFRHajm9dvWYOFUK1ayZ9qr8fwu8z5pG8HC7YC1DIx7WbxVWAkxbK&X-Amz-Signature=fa8786040c1b5e3d708369157bec5fd7559da8667754cbdb1408d3c643ece1c0&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSZJOAZU%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDcpHiHa0FbW2Xk%2BoANxZz0qfRA5kbWT09iUnENIGCOtQIhANtEJUtRkyE0NS8P4D4UOCW9MC4DP4fBgXX%2FUdqHYOknKogECMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwgy9mRRiJrjEvzJ5Mq3AMn1Nfq8ZxLWyp93ANCIGhOvCkTjEXSuYB4ZN0LXthBzgGW9Jt2VGx2%2B1D%2Bk9j9PU%2F7%2FcyEu2tdgQfdJFN3Dyx1eQTA7KygzJjSrltc3ONg%2Bil4OiFknGWPPxLqhhXBHWbvzuGj20xZKsnJjMAB5g1wYul4n1KJK4ZwJfFVfYggIOMuFB5WV8%2BCZjX%2FG%2FsDRCZo939gSQWy76JtpJxKI6rC5srX76PgVpc0hwA44sJ6SU9RXhMu3SzeWkigV45oLfew3P1AZVHq3KnOkjbQ1cuc9NMkBQbyYQPLH2fo88ow9HIN45CGTudgQSzgGS5vsX0h1yIEMdTbf8E1tEIzaGm94VVxAjlGxzqu1kYWQvirPcPKkOw8ONv0LII71j3kebiRuFeB0QArYk%2F8i0TBIH4NC7rhTSAYKn3Qvjy%2FyZvuSHPqHiyXsk5u1phzIauImkSASIIY3CXEW73QP4QBa2DZZ1qSdOEbovN5Tmk5bIoXBHWRcCIWuX38coUDZHk5qHQN%2Bq7Mag2rHHv4T0lS4QZWKdGq9aNH4C2VT%2Fm7upQJtMDR%2FHtV7WP1eHAET53OVnWVmnywIwXFz2cKYIUS2XRMEJrkxV%2FtvQK%2Be9gf%2BR4DRP1VpOr3KjB0ViFAqTDE7PW8BjqkAfxGfqq%2FU2ti76T%2F2EwxnoNbLh%2B9h6M3Ekg57oTp1S5qNSbLiQFJRufqofz%2B%2BYKcsZiegvkbAMs7a%2FQiouyPNkJjVbRiRnt5Nv8nB4xaXAJuCJwYTJ9Z%2FhhV9Cc7Sg9jWZP3YrMeXoTGON0DYAUmb1Kd5HT44Q1klCL2Nb6gFRHajm9dvWYOFUK1ayZ9qr8fwu8z5pG8HC7YC1DIx7WbxVWAkxbK&X-Amz-Signature=ec12e05bfc48e70e04f985a9dd21316f5e0ce064ebb6c3d858fb1579c35945af&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSZJOAZU%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDcpHiHa0FbW2Xk%2BoANxZz0qfRA5kbWT09iUnENIGCOtQIhANtEJUtRkyE0NS8P4D4UOCW9MC4DP4fBgXX%2FUdqHYOknKogECMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwgy9mRRiJrjEvzJ5Mq3AMn1Nfq8ZxLWyp93ANCIGhOvCkTjEXSuYB4ZN0LXthBzgGW9Jt2VGx2%2B1D%2Bk9j9PU%2F7%2FcyEu2tdgQfdJFN3Dyx1eQTA7KygzJjSrltc3ONg%2Bil4OiFknGWPPxLqhhXBHWbvzuGj20xZKsnJjMAB5g1wYul4n1KJK4ZwJfFVfYggIOMuFB5WV8%2BCZjX%2FG%2FsDRCZo939gSQWy76JtpJxKI6rC5srX76PgVpc0hwA44sJ6SU9RXhMu3SzeWkigV45oLfew3P1AZVHq3KnOkjbQ1cuc9NMkBQbyYQPLH2fo88ow9HIN45CGTudgQSzgGS5vsX0h1yIEMdTbf8E1tEIzaGm94VVxAjlGxzqu1kYWQvirPcPKkOw8ONv0LII71j3kebiRuFeB0QArYk%2F8i0TBIH4NC7rhTSAYKn3Qvjy%2FyZvuSHPqHiyXsk5u1phzIauImkSASIIY3CXEW73QP4QBa2DZZ1qSdOEbovN5Tmk5bIoXBHWRcCIWuX38coUDZHk5qHQN%2Bq7Mag2rHHv4T0lS4QZWKdGq9aNH4C2VT%2Fm7upQJtMDR%2FHtV7WP1eHAET53OVnWVmnywIwXFz2cKYIUS2XRMEJrkxV%2FtvQK%2Be9gf%2BR4DRP1VpOr3KjB0ViFAqTDE7PW8BjqkAfxGfqq%2FU2ti76T%2F2EwxnoNbLh%2B9h6M3Ekg57oTp1S5qNSbLiQFJRufqofz%2B%2BYKcsZiegvkbAMs7a%2FQiouyPNkJjVbRiRnt5Nv8nB4xaXAJuCJwYTJ9Z%2FhhV9Cc7Sg9jWZP3YrMeXoTGON0DYAUmb1Kd5HT44Q1klCL2Nb6gFRHajm9dvWYOFUK1ayZ9qr8fwu8z5pG8HC7YC1DIx7WbxVWAkxbK&X-Amz-Signature=6890ee7953e917f6b3bd50076116a4c5092e972be4d1e6728e352e4b234b3f9f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSZJOAZU%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDcpHiHa0FbW2Xk%2BoANxZz0qfRA5kbWT09iUnENIGCOtQIhANtEJUtRkyE0NS8P4D4UOCW9MC4DP4fBgXX%2FUdqHYOknKogECMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwgy9mRRiJrjEvzJ5Mq3AMn1Nfq8ZxLWyp93ANCIGhOvCkTjEXSuYB4ZN0LXthBzgGW9Jt2VGx2%2B1D%2Bk9j9PU%2F7%2FcyEu2tdgQfdJFN3Dyx1eQTA7KygzJjSrltc3ONg%2Bil4OiFknGWPPxLqhhXBHWbvzuGj20xZKsnJjMAB5g1wYul4n1KJK4ZwJfFVfYggIOMuFB5WV8%2BCZjX%2FG%2FsDRCZo939gSQWy76JtpJxKI6rC5srX76PgVpc0hwA44sJ6SU9RXhMu3SzeWkigV45oLfew3P1AZVHq3KnOkjbQ1cuc9NMkBQbyYQPLH2fo88ow9HIN45CGTudgQSzgGS5vsX0h1yIEMdTbf8E1tEIzaGm94VVxAjlGxzqu1kYWQvirPcPKkOw8ONv0LII71j3kebiRuFeB0QArYk%2F8i0TBIH4NC7rhTSAYKn3Qvjy%2FyZvuSHPqHiyXsk5u1phzIauImkSASIIY3CXEW73QP4QBa2DZZ1qSdOEbovN5Tmk5bIoXBHWRcCIWuX38coUDZHk5qHQN%2Bq7Mag2rHHv4T0lS4QZWKdGq9aNH4C2VT%2Fm7upQJtMDR%2FHtV7WP1eHAET53OVnWVmnywIwXFz2cKYIUS2XRMEJrkxV%2FtvQK%2Be9gf%2BR4DRP1VpOr3KjB0ViFAqTDE7PW8BjqkAfxGfqq%2FU2ti76T%2F2EwxnoNbLh%2B9h6M3Ekg57oTp1S5qNSbLiQFJRufqofz%2B%2BYKcsZiegvkbAMs7a%2FQiouyPNkJjVbRiRnt5Nv8nB4xaXAJuCJwYTJ9Z%2FhhV9Cc7Sg9jWZP3YrMeXoTGON0DYAUmb1Kd5HT44Q1klCL2Nb6gFRHajm9dvWYOFUK1ayZ9qr8fwu8z5pG8HC7YC1DIx7WbxVWAkxbK&X-Amz-Signature=b9cb74bd758d10f0f45e33212b9d6720e71931e4ab7194e9081e2fb22b92511e&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSZJOAZU%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDcpHiHa0FbW2Xk%2BoANxZz0qfRA5kbWT09iUnENIGCOtQIhANtEJUtRkyE0NS8P4D4UOCW9MC4DP4fBgXX%2FUdqHYOknKogECMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwgy9mRRiJrjEvzJ5Mq3AMn1Nfq8ZxLWyp93ANCIGhOvCkTjEXSuYB4ZN0LXthBzgGW9Jt2VGx2%2B1D%2Bk9j9PU%2F7%2FcyEu2tdgQfdJFN3Dyx1eQTA7KygzJjSrltc3ONg%2Bil4OiFknGWPPxLqhhXBHWbvzuGj20xZKsnJjMAB5g1wYul4n1KJK4ZwJfFVfYggIOMuFB5WV8%2BCZjX%2FG%2FsDRCZo939gSQWy76JtpJxKI6rC5srX76PgVpc0hwA44sJ6SU9RXhMu3SzeWkigV45oLfew3P1AZVHq3KnOkjbQ1cuc9NMkBQbyYQPLH2fo88ow9HIN45CGTudgQSzgGS5vsX0h1yIEMdTbf8E1tEIzaGm94VVxAjlGxzqu1kYWQvirPcPKkOw8ONv0LII71j3kebiRuFeB0QArYk%2F8i0TBIH4NC7rhTSAYKn3Qvjy%2FyZvuSHPqHiyXsk5u1phzIauImkSASIIY3CXEW73QP4QBa2DZZ1qSdOEbovN5Tmk5bIoXBHWRcCIWuX38coUDZHk5qHQN%2Bq7Mag2rHHv4T0lS4QZWKdGq9aNH4C2VT%2Fm7upQJtMDR%2FHtV7WP1eHAET53OVnWVmnywIwXFz2cKYIUS2XRMEJrkxV%2FtvQK%2Be9gf%2BR4DRP1VpOr3KjB0ViFAqTDE7PW8BjqkAfxGfqq%2FU2ti76T%2F2EwxnoNbLh%2B9h6M3Ekg57oTp1S5qNSbLiQFJRufqofz%2B%2BYKcsZiegvkbAMs7a%2FQiouyPNkJjVbRiRnt5Nv8nB4xaXAJuCJwYTJ9Z%2FhhV9Cc7Sg9jWZP3YrMeXoTGON0DYAUmb1Kd5HT44Q1klCL2Nb6gFRHajm9dvWYOFUK1ayZ9qr8fwu8z5pG8HC7YC1DIx7WbxVWAkxbK&X-Amz-Signature=876e08c84885ca843e66f1fa2e10d6c3435cfbdce261475ee327ba09f8aa7c6b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSZJOAZU%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDcpHiHa0FbW2Xk%2BoANxZz0qfRA5kbWT09iUnENIGCOtQIhANtEJUtRkyE0NS8P4D4UOCW9MC4DP4fBgXX%2FUdqHYOknKogECMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwgy9mRRiJrjEvzJ5Mq3AMn1Nfq8ZxLWyp93ANCIGhOvCkTjEXSuYB4ZN0LXthBzgGW9Jt2VGx2%2B1D%2Bk9j9PU%2F7%2FcyEu2tdgQfdJFN3Dyx1eQTA7KygzJjSrltc3ONg%2Bil4OiFknGWPPxLqhhXBHWbvzuGj20xZKsnJjMAB5g1wYul4n1KJK4ZwJfFVfYggIOMuFB5WV8%2BCZjX%2FG%2FsDRCZo939gSQWy76JtpJxKI6rC5srX76PgVpc0hwA44sJ6SU9RXhMu3SzeWkigV45oLfew3P1AZVHq3KnOkjbQ1cuc9NMkBQbyYQPLH2fo88ow9HIN45CGTudgQSzgGS5vsX0h1yIEMdTbf8E1tEIzaGm94VVxAjlGxzqu1kYWQvirPcPKkOw8ONv0LII71j3kebiRuFeB0QArYk%2F8i0TBIH4NC7rhTSAYKn3Qvjy%2FyZvuSHPqHiyXsk5u1phzIauImkSASIIY3CXEW73QP4QBa2DZZ1qSdOEbovN5Tmk5bIoXBHWRcCIWuX38coUDZHk5qHQN%2Bq7Mag2rHHv4T0lS4QZWKdGq9aNH4C2VT%2Fm7upQJtMDR%2FHtV7WP1eHAET53OVnWVmnywIwXFz2cKYIUS2XRMEJrkxV%2FtvQK%2Be9gf%2BR4DRP1VpOr3KjB0ViFAqTDE7PW8BjqkAfxGfqq%2FU2ti76T%2F2EwxnoNbLh%2B9h6M3Ekg57oTp1S5qNSbLiQFJRufqofz%2B%2BYKcsZiegvkbAMs7a%2FQiouyPNkJjVbRiRnt5Nv8nB4xaXAJuCJwYTJ9Z%2FhhV9Cc7Sg9jWZP3YrMeXoTGON0DYAUmb1Kd5HT44Q1klCL2Nb6gFRHajm9dvWYOFUK1ayZ9qr8fwu8z5pG8HC7YC1DIx7WbxVWAkxbK&X-Amz-Signature=1534f9a42598499dd7d9e0770445f1d34c07fbd20644412e4be9bdeee1428368&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSZJOAZU%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDcpHiHa0FbW2Xk%2BoANxZz0qfRA5kbWT09iUnENIGCOtQIhANtEJUtRkyE0NS8P4D4UOCW9MC4DP4fBgXX%2FUdqHYOknKogECMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwgy9mRRiJrjEvzJ5Mq3AMn1Nfq8ZxLWyp93ANCIGhOvCkTjEXSuYB4ZN0LXthBzgGW9Jt2VGx2%2B1D%2Bk9j9PU%2F7%2FcyEu2tdgQfdJFN3Dyx1eQTA7KygzJjSrltc3ONg%2Bil4OiFknGWPPxLqhhXBHWbvzuGj20xZKsnJjMAB5g1wYul4n1KJK4ZwJfFVfYggIOMuFB5WV8%2BCZjX%2FG%2FsDRCZo939gSQWy76JtpJxKI6rC5srX76PgVpc0hwA44sJ6SU9RXhMu3SzeWkigV45oLfew3P1AZVHq3KnOkjbQ1cuc9NMkBQbyYQPLH2fo88ow9HIN45CGTudgQSzgGS5vsX0h1yIEMdTbf8E1tEIzaGm94VVxAjlGxzqu1kYWQvirPcPKkOw8ONv0LII71j3kebiRuFeB0QArYk%2F8i0TBIH4NC7rhTSAYKn3Qvjy%2FyZvuSHPqHiyXsk5u1phzIauImkSASIIY3CXEW73QP4QBa2DZZ1qSdOEbovN5Tmk5bIoXBHWRcCIWuX38coUDZHk5qHQN%2Bq7Mag2rHHv4T0lS4QZWKdGq9aNH4C2VT%2Fm7upQJtMDR%2FHtV7WP1eHAET53OVnWVmnywIwXFz2cKYIUS2XRMEJrkxV%2FtvQK%2Be9gf%2BR4DRP1VpOr3KjB0ViFAqTDE7PW8BjqkAfxGfqq%2FU2ti76T%2F2EwxnoNbLh%2B9h6M3Ekg57oTp1S5qNSbLiQFJRufqofz%2B%2BYKcsZiegvkbAMs7a%2FQiouyPNkJjVbRiRnt5Nv8nB4xaXAJuCJwYTJ9Z%2FhhV9Cc7Sg9jWZP3YrMeXoTGON0DYAUmb1Kd5HT44Q1klCL2Nb6gFRHajm9dvWYOFUK1ayZ9qr8fwu8z5pG8HC7YC1DIx7WbxVWAkxbK&X-Amz-Signature=e2a08204015a1c3c75eb9f9e97daf4c4dae9f6b0e711075c2dad5aa1079ffdf1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSZJOAZU%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDcpHiHa0FbW2Xk%2BoANxZz0qfRA5kbWT09iUnENIGCOtQIhANtEJUtRkyE0NS8P4D4UOCW9MC4DP4fBgXX%2FUdqHYOknKogECMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwgy9mRRiJrjEvzJ5Mq3AMn1Nfq8ZxLWyp93ANCIGhOvCkTjEXSuYB4ZN0LXthBzgGW9Jt2VGx2%2B1D%2Bk9j9PU%2F7%2FcyEu2tdgQfdJFN3Dyx1eQTA7KygzJjSrltc3ONg%2Bil4OiFknGWPPxLqhhXBHWbvzuGj20xZKsnJjMAB5g1wYul4n1KJK4ZwJfFVfYggIOMuFB5WV8%2BCZjX%2FG%2FsDRCZo939gSQWy76JtpJxKI6rC5srX76PgVpc0hwA44sJ6SU9RXhMu3SzeWkigV45oLfew3P1AZVHq3KnOkjbQ1cuc9NMkBQbyYQPLH2fo88ow9HIN45CGTudgQSzgGS5vsX0h1yIEMdTbf8E1tEIzaGm94VVxAjlGxzqu1kYWQvirPcPKkOw8ONv0LII71j3kebiRuFeB0QArYk%2F8i0TBIH4NC7rhTSAYKn3Qvjy%2FyZvuSHPqHiyXsk5u1phzIauImkSASIIY3CXEW73QP4QBa2DZZ1qSdOEbovN5Tmk5bIoXBHWRcCIWuX38coUDZHk5qHQN%2Bq7Mag2rHHv4T0lS4QZWKdGq9aNH4C2VT%2Fm7upQJtMDR%2FHtV7WP1eHAET53OVnWVmnywIwXFz2cKYIUS2XRMEJrkxV%2FtvQK%2Be9gf%2BR4DRP1VpOr3KjB0ViFAqTDE7PW8BjqkAfxGfqq%2FU2ti76T%2F2EwxnoNbLh%2B9h6M3Ekg57oTp1S5qNSbLiQFJRufqofz%2B%2BYKcsZiegvkbAMs7a%2FQiouyPNkJjVbRiRnt5Nv8nB4xaXAJuCJwYTJ9Z%2FhhV9Cc7Sg9jWZP3YrMeXoTGON0DYAUmb1Kd5HT44Q1klCL2Nb6gFRHajm9dvWYOFUK1ayZ9qr8fwu8z5pG8HC7YC1DIx7WbxVWAkxbK&X-Amz-Signature=3619ea98587b179ebbae73dbf096b6f103c98bd2b55ff3adcbde209ed1311963&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RIWPU3LI%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDuzcfmAsklKcR2JyaDh7NanFfFy6NYpRwRQMv6fi%2B1tQIhAOEgmAE2bMIJXGElOFPz7tDnAlox0XNR2Br%2BLLX83YJDKogECMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyKHoGLEIA0SkRPICcq3AOTYQHIcrpvr9L3K6y8pZrVNHhHTamw78h9bV8CNnjVk52SMeRypjLOoT%2BQZWD7vQqt8ylYrTJisD29l2MR4M8gNBPBpDWXykBDo9WZn6j1uHIwm6mDmjcSAzdQQ9d1dZJSkwOla3NXfqGVPPuBK%2Fpacj9HhU%2BDvyVvLJ6rMifMvppChOogs%2FLTt98IBuSVgqorOgVEX8MOEySDArYyNn50Oq2PQMMdnKzFBgswEjqSu2m4QDzsK%2FQaqQyFwIRh5YV%2Bo%2FqQy%2BYJoCV%2Fxo2quYJwBEEFgkRHfgxN3rZ0Vw33yDOHjds5rxVHop8ZYrX9z%2BM6NVziALbaIdge2OroDpJfEUiPX03Pz23ENv2HABHGmB%2F8yzlhixa3FPDleNfhTRNTImDSwyz9g0QDGDfYHmbJ9FLtGWeEXYolzWHaAdGKo2gZfSO27rAqfEdWZA6aGQOHJNpcTV60fNjR7eOMiiPNyFMszo3AQlH1C92U1CA03QrWOXWrjegFeqYPhGdNQnHTgA9I6cYSNGCKsJiOLadw%2FjMQNAZRCWiC%2Fmh3cdKaVG4rDwkrEcE8yhL4s6kSeuOpQ9AEiejRsZePoBdAafeThizUMi%2ByWfYjh0BozHQtBsfjXUY%2F7pplJNCT9DDq7PW8BjqkAexmR9VZV6C%2F7j62xpLdrakspgG%2F8%2FWHw4wJppPNweq1S8D%2Byi%2FfkrKhYfIzJ2v1WPkUzgEHBOZfUS0zjCrm8Bsvw8St7bDDyVxmYNvtaoikaA8KmK9OjEyE8%2F4PuasUyT5hLI6ezzSar1%2BvXC6UJ6iiLmlj%2Fimwi85zRVZHWbKWfNTtH85hwuW0JWxzONki4wpe7kiNAl73OztMCcZ1wiMVfJL1&X-Amz-Signature=4b813bea15513263df713f7cc2737749bd413d8de80fdf86bf51649469dc4c80&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RIWPU3LI%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDuzcfmAsklKcR2JyaDh7NanFfFy6NYpRwRQMv6fi%2B1tQIhAOEgmAE2bMIJXGElOFPz7tDnAlox0XNR2Br%2BLLX83YJDKogECMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyKHoGLEIA0SkRPICcq3AOTYQHIcrpvr9L3K6y8pZrVNHhHTamw78h9bV8CNnjVk52SMeRypjLOoT%2BQZWD7vQqt8ylYrTJisD29l2MR4M8gNBPBpDWXykBDo9WZn6j1uHIwm6mDmjcSAzdQQ9d1dZJSkwOla3NXfqGVPPuBK%2Fpacj9HhU%2BDvyVvLJ6rMifMvppChOogs%2FLTt98IBuSVgqorOgVEX8MOEySDArYyNn50Oq2PQMMdnKzFBgswEjqSu2m4QDzsK%2FQaqQyFwIRh5YV%2Bo%2FqQy%2BYJoCV%2Fxo2quYJwBEEFgkRHfgxN3rZ0Vw33yDOHjds5rxVHop8ZYrX9z%2BM6NVziALbaIdge2OroDpJfEUiPX03Pz23ENv2HABHGmB%2F8yzlhixa3FPDleNfhTRNTImDSwyz9g0QDGDfYHmbJ9FLtGWeEXYolzWHaAdGKo2gZfSO27rAqfEdWZA6aGQOHJNpcTV60fNjR7eOMiiPNyFMszo3AQlH1C92U1CA03QrWOXWrjegFeqYPhGdNQnHTgA9I6cYSNGCKsJiOLadw%2FjMQNAZRCWiC%2Fmh3cdKaVG4rDwkrEcE8yhL4s6kSeuOpQ9AEiejRsZePoBdAafeThizUMi%2ByWfYjh0BozHQtBsfjXUY%2F7pplJNCT9DDq7PW8BjqkAexmR9VZV6C%2F7j62xpLdrakspgG%2F8%2FWHw4wJppPNweq1S8D%2Byi%2FfkrKhYfIzJ2v1WPkUzgEHBOZfUS0zjCrm8Bsvw8St7bDDyVxmYNvtaoikaA8KmK9OjEyE8%2F4PuasUyT5hLI6ezzSar1%2BvXC6UJ6iiLmlj%2Fimwi85zRVZHWbKWfNTtH85hwuW0JWxzONki4wpe7kiNAl73OztMCcZ1wiMVfJL1&X-Amz-Signature=9088351cb8b704bfb1df8f32ba064fc6896e6afee25706d476fb96e7090229b8&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
