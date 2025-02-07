

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WS6NRLS3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201607Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIHRzNxvUXX%2BfhopoMROXtlbZnyQdPV%2B14vdMX5wP%2BO7xAiEA4IyqYOkQccIWUflcMEAkqrH%2B4B3Ifcgj9xt5XN%2Fz2pUq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDB%2FBrD0dy8Hz%2FuYGHyrcAyUakh5RP04oHxSy60carSn8tZSmWtM7kiG8LQNo%2BSrmBqCKaETVo2M642%2F%2FaP%2B8Ip6EAR7QHfRX%2FhGkJFR7bxtJUGRE%2FuFveWcYO2lbYsbmk3aLzIjFv1CJmYkw0rubhPf604CKejhCid8lUP0lUug0eeyWzFAnml2nPXewFopkG2WWYaRLayZbU8yyK1jlQl1AZGy458xyp3cAsOVj6Cfd7HlUdFZY9NSglC5hk38tbI%2BAkY1%2F%2FlDklazAYKaF3h4JQG74%2B6eW0btAW0K%2BqzbH3MD7t418XRyiGrgfxi0GJZ1IhE0v5Dih%2FGkEmvgOtVMnZMYkoFJYEvog5oaIsrys9vsNVMyrwh3cXXazcVTVkU1ZeGH4slScS%2BVBRS%2B0OcbN7RrOHZr%2FSHpWLo2J28m1HCqOeIvbRiJ5wLcrqQMniu1MAz1MrT6lmjChK6xEYH9aXaBnkVn8ATsGexNowpMRwoEcA5U6LKrJAXR8NLJWm%2FYRyh7upC1giOsOFmPzs1M2jwEX%2BL8wuhIUuYHp31UbM1TaWOVaXW3T3NY4qk5fpWJBRDR9hR5JvYnGlKFcLcYh3%2BCU7KWJpNZLgNHNvFEpmLPsbgzzEVco3FTJ3nZzuYWQ2JTqrMlFCtaUMKnSmb0GOqUBvw0q%2Bb9yDJe80jbqXKhynnV%2F%2BVTh28K23jGT%2FQyaaB5L6rPksZwUJg229N2j9v2QUj94wDir2PW3gm1QviUNK7NCChfbCj63zInrm0OrHdxuOPUuWiEm3tAntGvybC60LWC%2FuchyE3Q3bSLyyb9DcBNCEPyvW%2Bjn8spOVHv%2BZezyccXrq1SvGRD0k0ruslMq0XxvRFVP0SlPiS0YGfXqHO9FjFXC&X-Amz-Signature=2c6f0b1cbec993df8376d8df57a84aebfbd2c189ac64adf8c06ea94f6d1982ae&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WS6NRLS3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201607Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIHRzNxvUXX%2BfhopoMROXtlbZnyQdPV%2B14vdMX5wP%2BO7xAiEA4IyqYOkQccIWUflcMEAkqrH%2B4B3Ifcgj9xt5XN%2Fz2pUq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDB%2FBrD0dy8Hz%2FuYGHyrcAyUakh5RP04oHxSy60carSn8tZSmWtM7kiG8LQNo%2BSrmBqCKaETVo2M642%2F%2FaP%2B8Ip6EAR7QHfRX%2FhGkJFR7bxtJUGRE%2FuFveWcYO2lbYsbmk3aLzIjFv1CJmYkw0rubhPf604CKejhCid8lUP0lUug0eeyWzFAnml2nPXewFopkG2WWYaRLayZbU8yyK1jlQl1AZGy458xyp3cAsOVj6Cfd7HlUdFZY9NSglC5hk38tbI%2BAkY1%2F%2FlDklazAYKaF3h4JQG74%2B6eW0btAW0K%2BqzbH3MD7t418XRyiGrgfxi0GJZ1IhE0v5Dih%2FGkEmvgOtVMnZMYkoFJYEvog5oaIsrys9vsNVMyrwh3cXXazcVTVkU1ZeGH4slScS%2BVBRS%2B0OcbN7RrOHZr%2FSHpWLo2J28m1HCqOeIvbRiJ5wLcrqQMniu1MAz1MrT6lmjChK6xEYH9aXaBnkVn8ATsGexNowpMRwoEcA5U6LKrJAXR8NLJWm%2FYRyh7upC1giOsOFmPzs1M2jwEX%2BL8wuhIUuYHp31UbM1TaWOVaXW3T3NY4qk5fpWJBRDR9hR5JvYnGlKFcLcYh3%2BCU7KWJpNZLgNHNvFEpmLPsbgzzEVco3FTJ3nZzuYWQ2JTqrMlFCtaUMKnSmb0GOqUBvw0q%2Bb9yDJe80jbqXKhynnV%2F%2BVTh28K23jGT%2FQyaaB5L6rPksZwUJg229N2j9v2QUj94wDir2PW3gm1QviUNK7NCChfbCj63zInrm0OrHdxuOPUuWiEm3tAntGvybC60LWC%2FuchyE3Q3bSLyyb9DcBNCEPyvW%2Bjn8spOVHv%2BZezyccXrq1SvGRD0k0ruslMq0XxvRFVP0SlPiS0YGfXqHO9FjFXC&X-Amz-Signature=ce7ba619c6c89e954df984a2b9bb54c0a2d646ca2ab43d9b9b9d6c80194eeb7d&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WS6NRLS3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201607Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIHRzNxvUXX%2BfhopoMROXtlbZnyQdPV%2B14vdMX5wP%2BO7xAiEA4IyqYOkQccIWUflcMEAkqrH%2B4B3Ifcgj9xt5XN%2Fz2pUq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDB%2FBrD0dy8Hz%2FuYGHyrcAyUakh5RP04oHxSy60carSn8tZSmWtM7kiG8LQNo%2BSrmBqCKaETVo2M642%2F%2FaP%2B8Ip6EAR7QHfRX%2FhGkJFR7bxtJUGRE%2FuFveWcYO2lbYsbmk3aLzIjFv1CJmYkw0rubhPf604CKejhCid8lUP0lUug0eeyWzFAnml2nPXewFopkG2WWYaRLayZbU8yyK1jlQl1AZGy458xyp3cAsOVj6Cfd7HlUdFZY9NSglC5hk38tbI%2BAkY1%2F%2FlDklazAYKaF3h4JQG74%2B6eW0btAW0K%2BqzbH3MD7t418XRyiGrgfxi0GJZ1IhE0v5Dih%2FGkEmvgOtVMnZMYkoFJYEvog5oaIsrys9vsNVMyrwh3cXXazcVTVkU1ZeGH4slScS%2BVBRS%2B0OcbN7RrOHZr%2FSHpWLo2J28m1HCqOeIvbRiJ5wLcrqQMniu1MAz1MrT6lmjChK6xEYH9aXaBnkVn8ATsGexNowpMRwoEcA5U6LKrJAXR8NLJWm%2FYRyh7upC1giOsOFmPzs1M2jwEX%2BL8wuhIUuYHp31UbM1TaWOVaXW3T3NY4qk5fpWJBRDR9hR5JvYnGlKFcLcYh3%2BCU7KWJpNZLgNHNvFEpmLPsbgzzEVco3FTJ3nZzuYWQ2JTqrMlFCtaUMKnSmb0GOqUBvw0q%2Bb9yDJe80jbqXKhynnV%2F%2BVTh28K23jGT%2FQyaaB5L6rPksZwUJg229N2j9v2QUj94wDir2PW3gm1QviUNK7NCChfbCj63zInrm0OrHdxuOPUuWiEm3tAntGvybC60LWC%2FuchyE3Q3bSLyyb9DcBNCEPyvW%2Bjn8spOVHv%2BZezyccXrq1SvGRD0k0ruslMq0XxvRFVP0SlPiS0YGfXqHO9FjFXC&X-Amz-Signature=312f8957536429bb3e37fa398b69a8d8c39270e0d0d21f6dc366e40ca1753fcc&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WS6NRLS3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201607Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIHRzNxvUXX%2BfhopoMROXtlbZnyQdPV%2B14vdMX5wP%2BO7xAiEA4IyqYOkQccIWUflcMEAkqrH%2B4B3Ifcgj9xt5XN%2Fz2pUq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDB%2FBrD0dy8Hz%2FuYGHyrcAyUakh5RP04oHxSy60carSn8tZSmWtM7kiG8LQNo%2BSrmBqCKaETVo2M642%2F%2FaP%2B8Ip6EAR7QHfRX%2FhGkJFR7bxtJUGRE%2FuFveWcYO2lbYsbmk3aLzIjFv1CJmYkw0rubhPf604CKejhCid8lUP0lUug0eeyWzFAnml2nPXewFopkG2WWYaRLayZbU8yyK1jlQl1AZGy458xyp3cAsOVj6Cfd7HlUdFZY9NSglC5hk38tbI%2BAkY1%2F%2FlDklazAYKaF3h4JQG74%2B6eW0btAW0K%2BqzbH3MD7t418XRyiGrgfxi0GJZ1IhE0v5Dih%2FGkEmvgOtVMnZMYkoFJYEvog5oaIsrys9vsNVMyrwh3cXXazcVTVkU1ZeGH4slScS%2BVBRS%2B0OcbN7RrOHZr%2FSHpWLo2J28m1HCqOeIvbRiJ5wLcrqQMniu1MAz1MrT6lmjChK6xEYH9aXaBnkVn8ATsGexNowpMRwoEcA5U6LKrJAXR8NLJWm%2FYRyh7upC1giOsOFmPzs1M2jwEX%2BL8wuhIUuYHp31UbM1TaWOVaXW3T3NY4qk5fpWJBRDR9hR5JvYnGlKFcLcYh3%2BCU7KWJpNZLgNHNvFEpmLPsbgzzEVco3FTJ3nZzuYWQ2JTqrMlFCtaUMKnSmb0GOqUBvw0q%2Bb9yDJe80jbqXKhynnV%2F%2BVTh28K23jGT%2FQyaaB5L6rPksZwUJg229N2j9v2QUj94wDir2PW3gm1QviUNK7NCChfbCj63zInrm0OrHdxuOPUuWiEm3tAntGvybC60LWC%2FuchyE3Q3bSLyyb9DcBNCEPyvW%2Bjn8spOVHv%2BZezyccXrq1SvGRD0k0ruslMq0XxvRFVP0SlPiS0YGfXqHO9FjFXC&X-Amz-Signature=d24748a99d4f60c602d484626a385a5d4d9c2d97519c4d121ac2c5b45df1f55b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WS6NRLS3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201607Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIHRzNxvUXX%2BfhopoMROXtlbZnyQdPV%2B14vdMX5wP%2BO7xAiEA4IyqYOkQccIWUflcMEAkqrH%2B4B3Ifcgj9xt5XN%2Fz2pUq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDB%2FBrD0dy8Hz%2FuYGHyrcAyUakh5RP04oHxSy60carSn8tZSmWtM7kiG8LQNo%2BSrmBqCKaETVo2M642%2F%2FaP%2B8Ip6EAR7QHfRX%2FhGkJFR7bxtJUGRE%2FuFveWcYO2lbYsbmk3aLzIjFv1CJmYkw0rubhPf604CKejhCid8lUP0lUug0eeyWzFAnml2nPXewFopkG2WWYaRLayZbU8yyK1jlQl1AZGy458xyp3cAsOVj6Cfd7HlUdFZY9NSglC5hk38tbI%2BAkY1%2F%2FlDklazAYKaF3h4JQG74%2B6eW0btAW0K%2BqzbH3MD7t418XRyiGrgfxi0GJZ1IhE0v5Dih%2FGkEmvgOtVMnZMYkoFJYEvog5oaIsrys9vsNVMyrwh3cXXazcVTVkU1ZeGH4slScS%2BVBRS%2B0OcbN7RrOHZr%2FSHpWLo2J28m1HCqOeIvbRiJ5wLcrqQMniu1MAz1MrT6lmjChK6xEYH9aXaBnkVn8ATsGexNowpMRwoEcA5U6LKrJAXR8NLJWm%2FYRyh7upC1giOsOFmPzs1M2jwEX%2BL8wuhIUuYHp31UbM1TaWOVaXW3T3NY4qk5fpWJBRDR9hR5JvYnGlKFcLcYh3%2BCU7KWJpNZLgNHNvFEpmLPsbgzzEVco3FTJ3nZzuYWQ2JTqrMlFCtaUMKnSmb0GOqUBvw0q%2Bb9yDJe80jbqXKhynnV%2F%2BVTh28K23jGT%2FQyaaB5L6rPksZwUJg229N2j9v2QUj94wDir2PW3gm1QviUNK7NCChfbCj63zInrm0OrHdxuOPUuWiEm3tAntGvybC60LWC%2FuchyE3Q3bSLyyb9DcBNCEPyvW%2Bjn8spOVHv%2BZezyccXrq1SvGRD0k0ruslMq0XxvRFVP0SlPiS0YGfXqHO9FjFXC&X-Amz-Signature=3b9c21c1a216166705e16689db02ca4ed6548028f8ba0cb756125a6d9dcde841&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WS6NRLS3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201607Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIHRzNxvUXX%2BfhopoMROXtlbZnyQdPV%2B14vdMX5wP%2BO7xAiEA4IyqYOkQccIWUflcMEAkqrH%2B4B3Ifcgj9xt5XN%2Fz2pUq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDB%2FBrD0dy8Hz%2FuYGHyrcAyUakh5RP04oHxSy60carSn8tZSmWtM7kiG8LQNo%2BSrmBqCKaETVo2M642%2F%2FaP%2B8Ip6EAR7QHfRX%2FhGkJFR7bxtJUGRE%2FuFveWcYO2lbYsbmk3aLzIjFv1CJmYkw0rubhPf604CKejhCid8lUP0lUug0eeyWzFAnml2nPXewFopkG2WWYaRLayZbU8yyK1jlQl1AZGy458xyp3cAsOVj6Cfd7HlUdFZY9NSglC5hk38tbI%2BAkY1%2F%2FlDklazAYKaF3h4JQG74%2B6eW0btAW0K%2BqzbH3MD7t418XRyiGrgfxi0GJZ1IhE0v5Dih%2FGkEmvgOtVMnZMYkoFJYEvog5oaIsrys9vsNVMyrwh3cXXazcVTVkU1ZeGH4slScS%2BVBRS%2B0OcbN7RrOHZr%2FSHpWLo2J28m1HCqOeIvbRiJ5wLcrqQMniu1MAz1MrT6lmjChK6xEYH9aXaBnkVn8ATsGexNowpMRwoEcA5U6LKrJAXR8NLJWm%2FYRyh7upC1giOsOFmPzs1M2jwEX%2BL8wuhIUuYHp31UbM1TaWOVaXW3T3NY4qk5fpWJBRDR9hR5JvYnGlKFcLcYh3%2BCU7KWJpNZLgNHNvFEpmLPsbgzzEVco3FTJ3nZzuYWQ2JTqrMlFCtaUMKnSmb0GOqUBvw0q%2Bb9yDJe80jbqXKhynnV%2F%2BVTh28K23jGT%2FQyaaB5L6rPksZwUJg229N2j9v2QUj94wDir2PW3gm1QviUNK7NCChfbCj63zInrm0OrHdxuOPUuWiEm3tAntGvybC60LWC%2FuchyE3Q3bSLyyb9DcBNCEPyvW%2Bjn8spOVHv%2BZezyccXrq1SvGRD0k0ruslMq0XxvRFVP0SlPiS0YGfXqHO9FjFXC&X-Amz-Signature=02ea08aad84abf5f9230019b50123c332b61de2f5166684088d33ff855557c57&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WS6NRLS3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201607Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIHRzNxvUXX%2BfhopoMROXtlbZnyQdPV%2B14vdMX5wP%2BO7xAiEA4IyqYOkQccIWUflcMEAkqrH%2B4B3Ifcgj9xt5XN%2Fz2pUq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDB%2FBrD0dy8Hz%2FuYGHyrcAyUakh5RP04oHxSy60carSn8tZSmWtM7kiG8LQNo%2BSrmBqCKaETVo2M642%2F%2FaP%2B8Ip6EAR7QHfRX%2FhGkJFR7bxtJUGRE%2FuFveWcYO2lbYsbmk3aLzIjFv1CJmYkw0rubhPf604CKejhCid8lUP0lUug0eeyWzFAnml2nPXewFopkG2WWYaRLayZbU8yyK1jlQl1AZGy458xyp3cAsOVj6Cfd7HlUdFZY9NSglC5hk38tbI%2BAkY1%2F%2FlDklazAYKaF3h4JQG74%2B6eW0btAW0K%2BqzbH3MD7t418XRyiGrgfxi0GJZ1IhE0v5Dih%2FGkEmvgOtVMnZMYkoFJYEvog5oaIsrys9vsNVMyrwh3cXXazcVTVkU1ZeGH4slScS%2BVBRS%2B0OcbN7RrOHZr%2FSHpWLo2J28m1HCqOeIvbRiJ5wLcrqQMniu1MAz1MrT6lmjChK6xEYH9aXaBnkVn8ATsGexNowpMRwoEcA5U6LKrJAXR8NLJWm%2FYRyh7upC1giOsOFmPzs1M2jwEX%2BL8wuhIUuYHp31UbM1TaWOVaXW3T3NY4qk5fpWJBRDR9hR5JvYnGlKFcLcYh3%2BCU7KWJpNZLgNHNvFEpmLPsbgzzEVco3FTJ3nZzuYWQ2JTqrMlFCtaUMKnSmb0GOqUBvw0q%2Bb9yDJe80jbqXKhynnV%2F%2BVTh28K23jGT%2FQyaaB5L6rPksZwUJg229N2j9v2QUj94wDir2PW3gm1QviUNK7NCChfbCj63zInrm0OrHdxuOPUuWiEm3tAntGvybC60LWC%2FuchyE3Q3bSLyyb9DcBNCEPyvW%2Bjn8spOVHv%2BZezyccXrq1SvGRD0k0ruslMq0XxvRFVP0SlPiS0YGfXqHO9FjFXC&X-Amz-Signature=6e2ca602bcdab3a7f65c0747fd5abd6b7e07ee8b6db626f51e4b00bf6facc775&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WS6NRLS3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201607Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIHRzNxvUXX%2BfhopoMROXtlbZnyQdPV%2B14vdMX5wP%2BO7xAiEA4IyqYOkQccIWUflcMEAkqrH%2B4B3Ifcgj9xt5XN%2Fz2pUq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDB%2FBrD0dy8Hz%2FuYGHyrcAyUakh5RP04oHxSy60carSn8tZSmWtM7kiG8LQNo%2BSrmBqCKaETVo2M642%2F%2FaP%2B8Ip6EAR7QHfRX%2FhGkJFR7bxtJUGRE%2FuFveWcYO2lbYsbmk3aLzIjFv1CJmYkw0rubhPf604CKejhCid8lUP0lUug0eeyWzFAnml2nPXewFopkG2WWYaRLayZbU8yyK1jlQl1AZGy458xyp3cAsOVj6Cfd7HlUdFZY9NSglC5hk38tbI%2BAkY1%2F%2FlDklazAYKaF3h4JQG74%2B6eW0btAW0K%2BqzbH3MD7t418XRyiGrgfxi0GJZ1IhE0v5Dih%2FGkEmvgOtVMnZMYkoFJYEvog5oaIsrys9vsNVMyrwh3cXXazcVTVkU1ZeGH4slScS%2BVBRS%2B0OcbN7RrOHZr%2FSHpWLo2J28m1HCqOeIvbRiJ5wLcrqQMniu1MAz1MrT6lmjChK6xEYH9aXaBnkVn8ATsGexNowpMRwoEcA5U6LKrJAXR8NLJWm%2FYRyh7upC1giOsOFmPzs1M2jwEX%2BL8wuhIUuYHp31UbM1TaWOVaXW3T3NY4qk5fpWJBRDR9hR5JvYnGlKFcLcYh3%2BCU7KWJpNZLgNHNvFEpmLPsbgzzEVco3FTJ3nZzuYWQ2JTqrMlFCtaUMKnSmb0GOqUBvw0q%2Bb9yDJe80jbqXKhynnV%2F%2BVTh28K23jGT%2FQyaaB5L6rPksZwUJg229N2j9v2QUj94wDir2PW3gm1QviUNK7NCChfbCj63zInrm0OrHdxuOPUuWiEm3tAntGvybC60LWC%2FuchyE3Q3bSLyyb9DcBNCEPyvW%2Bjn8spOVHv%2BZezyccXrq1SvGRD0k0ruslMq0XxvRFVP0SlPiS0YGfXqHO9FjFXC&X-Amz-Signature=e5ad6ad147fb8b97b187d7075584abd35fa84effd22bc5506e17aa0b63c0a569&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WS6NRLS3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201607Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIHRzNxvUXX%2BfhopoMROXtlbZnyQdPV%2B14vdMX5wP%2BO7xAiEA4IyqYOkQccIWUflcMEAkqrH%2B4B3Ifcgj9xt5XN%2Fz2pUq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDB%2FBrD0dy8Hz%2FuYGHyrcAyUakh5RP04oHxSy60carSn8tZSmWtM7kiG8LQNo%2BSrmBqCKaETVo2M642%2F%2FaP%2B8Ip6EAR7QHfRX%2FhGkJFR7bxtJUGRE%2FuFveWcYO2lbYsbmk3aLzIjFv1CJmYkw0rubhPf604CKejhCid8lUP0lUug0eeyWzFAnml2nPXewFopkG2WWYaRLayZbU8yyK1jlQl1AZGy458xyp3cAsOVj6Cfd7HlUdFZY9NSglC5hk38tbI%2BAkY1%2F%2FlDklazAYKaF3h4JQG74%2B6eW0btAW0K%2BqzbH3MD7t418XRyiGrgfxi0GJZ1IhE0v5Dih%2FGkEmvgOtVMnZMYkoFJYEvog5oaIsrys9vsNVMyrwh3cXXazcVTVkU1ZeGH4slScS%2BVBRS%2B0OcbN7RrOHZr%2FSHpWLo2J28m1HCqOeIvbRiJ5wLcrqQMniu1MAz1MrT6lmjChK6xEYH9aXaBnkVn8ATsGexNowpMRwoEcA5U6LKrJAXR8NLJWm%2FYRyh7upC1giOsOFmPzs1M2jwEX%2BL8wuhIUuYHp31UbM1TaWOVaXW3T3NY4qk5fpWJBRDR9hR5JvYnGlKFcLcYh3%2BCU7KWJpNZLgNHNvFEpmLPsbgzzEVco3FTJ3nZzuYWQ2JTqrMlFCtaUMKnSmb0GOqUBvw0q%2Bb9yDJe80jbqXKhynnV%2F%2BVTh28K23jGT%2FQyaaB5L6rPksZwUJg229N2j9v2QUj94wDir2PW3gm1QviUNK7NCChfbCj63zInrm0OrHdxuOPUuWiEm3tAntGvybC60LWC%2FuchyE3Q3bSLyyb9DcBNCEPyvW%2Bjn8spOVHv%2BZezyccXrq1SvGRD0k0ruslMq0XxvRFVP0SlPiS0YGfXqHO9FjFXC&X-Amz-Signature=ce614bc29b35e001ab98129a73401d83c2a16853aa41bd42265e94ac2de10fe4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YEF46DW%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIQCZrZYLyDYkVfIMq9UWWHR6iGWwGSe5wR%2FlKaR0oGAHfwIgcFlIVAInXBLRJvieEu2admg2ko%2FPedsyQs3AYmqsCMQq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDNegyltoy64mKAlJKyrcA13lutPSn75GduvITFgl0O83We3YcV5udi7WcAqkfubya8WBNl4zf5CiqUI3B%2BT6VqJC9Jmr0LybLs69tf%2FpW2TYTltScosmsCmwTpn2pu7kMqqt9MJqMEnz4lrdxGoCPZ5lyVgE6qSjzVDZdt4Zp25FH65AOdqXhz2sPr8X48Z%2BFSI6nQKt4pFXd4j%2BmnAAE6zvv%2FMcR5NVh2EgKGN86L1K2lkOF0%2BZO6OsFBq1MwAQHXBB27RmlXl6WzpczFqItmBQU8QU8sS%2FBY%2BFgOQwi66vD8k1VXXEpmUu1idoGuUKDnc9KnGZHA2WGZ6MXTLVob3It6SfQ0K1GtW3aCWm3CAJuBzY8dEa6GvUycCXhGZYrho4lErQ%2Fz4CTYZXUZmAf2a5jRt84wCD0bJDTo6u6i%2F3y1NFC02kbIHbsr65iRrTF38EQRb38zN%2Fu%2BOTMOKWZMTaNfAUat1lnMLtxlIxQU%2FInyBhBHDy%2FWShyzK%2BzHIEolHYN3CJxRDNWHjels7EFygdqIxkVc2KlwiJc8hCncyivkvNDivJ6gZ5b3C8vgzKZdANJDOuRKinVeaYgFoYiUP5HVIWuwStFKcxSw3qSVkXj%2F2xsstEWj6CegAjUsroZLPyEcEXmxXyPH2jMI%2FSmb0GOqUBP9rxKL0y%2F4uG0e2NaQU9vJfbxnjepG712Lqbq4Okw0WY03WvNVQhaPPEyJC%2F%2BlGYYxHXdq%2FRctw1AjnzA6JH52LhShTBZqaAmkQK%2Fvzo2IEMayXqspgD91Y5eRJCGg3rLdQ9ISPQpuk3kLqBQfHCRFc6HleL2fDg2kzyY1vcS%2BJGHJ9HdpA0tZhi%2BJ0fv8gzSnlyAZ9Qv1NcIl8iLoQ6B7gEp%2BZd&X-Amz-Signature=65f78ee803648c78a206c887b30f45600bc8e864fc0da535aaa8985ca9ab3000&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YEF46DW%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIQCZrZYLyDYkVfIMq9UWWHR6iGWwGSe5wR%2FlKaR0oGAHfwIgcFlIVAInXBLRJvieEu2admg2ko%2FPedsyQs3AYmqsCMQq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDNegyltoy64mKAlJKyrcA13lutPSn75GduvITFgl0O83We3YcV5udi7WcAqkfubya8WBNl4zf5CiqUI3B%2BT6VqJC9Jmr0LybLs69tf%2FpW2TYTltScosmsCmwTpn2pu7kMqqt9MJqMEnz4lrdxGoCPZ5lyVgE6qSjzVDZdt4Zp25FH65AOdqXhz2sPr8X48Z%2BFSI6nQKt4pFXd4j%2BmnAAE6zvv%2FMcR5NVh2EgKGN86L1K2lkOF0%2BZO6OsFBq1MwAQHXBB27RmlXl6WzpczFqItmBQU8QU8sS%2FBY%2BFgOQwi66vD8k1VXXEpmUu1idoGuUKDnc9KnGZHA2WGZ6MXTLVob3It6SfQ0K1GtW3aCWm3CAJuBzY8dEa6GvUycCXhGZYrho4lErQ%2Fz4CTYZXUZmAf2a5jRt84wCD0bJDTo6u6i%2F3y1NFC02kbIHbsr65iRrTF38EQRb38zN%2Fu%2BOTMOKWZMTaNfAUat1lnMLtxlIxQU%2FInyBhBHDy%2FWShyzK%2BzHIEolHYN3CJxRDNWHjels7EFygdqIxkVc2KlwiJc8hCncyivkvNDivJ6gZ5b3C8vgzKZdANJDOuRKinVeaYgFoYiUP5HVIWuwStFKcxSw3qSVkXj%2F2xsstEWj6CegAjUsroZLPyEcEXmxXyPH2jMI%2FSmb0GOqUBP9rxKL0y%2F4uG0e2NaQU9vJfbxnjepG712Lqbq4Okw0WY03WvNVQhaPPEyJC%2F%2BlGYYxHXdq%2FRctw1AjnzA6JH52LhShTBZqaAmkQK%2Fvzo2IEMayXqspgD91Y5eRJCGg3rLdQ9ISPQpuk3kLqBQfHCRFc6HleL2fDg2kzyY1vcS%2BJGHJ9HdpA0tZhi%2BJ0fv8gzSnlyAZ9Qv1NcIl8iLoQ6B7gEp%2BZd&X-Amz-Signature=a3001659d9ca47622332022213aa2085adac4c919e5e3bfce9f56a13a045c4d2&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
