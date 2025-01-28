

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SHTYKV42%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJGMEQCIDdegJHHWavAHy0ogvUi2S0usuJJx5ElPilawI1To0CoAiBtpjxlH4bOnYPT9DRXj95oj%2Bxp626iEqG4mKP4UI4KUCr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIM42oMkxltwPbTZSKZKtwDeJLhpUED4H9GmZ1sV%2BqfJ67rsMYor1huef3hk5O6blCskhLBD4K4NUNwf%2FXUvKhFwwSt%2FxM4Q644P1fpbCBJ3T8xtwH2qfPSWJ8IFhuDxURUMF2Skl2ccWgSztjI3SSb%2BIg2xAX92bEABCU92jh1Ef0cTDJpj32OtdY9Xg5rMcyq1lntlht0tgYOAhr9nos4Y1Hemx1sLaw1NnRXzPL%2Fy7TaVYXaGCdOLwTIM17SUyU6%2Bavk1LUJdW4i%2FEfnbUCKowVzv8py%2BKxTAuOOconaLmef608VEkG1yD%2BgQvsx%2BeS8sZ2EHRQUTAB9wICKvvXhmqJUkgIkpMfYFEk34wegcfo%2F8RGFID8jMFFs4aNQNR3tzIxUxYvFwWaucJn2rMIjTBu9YecMOWUPSVPvuGso8Vk2MGmxi2JyMIs1H7x%2Faj2XVWZdo2vzzkkvxk6YBHx1dEK4TrUi3wTS3Lvj6yWsgS5HzkmVJqRmtFgmKoguKTQ2adTm%2FsH%2FBCo61rPdmU%2Fj9RPadK2bEeyIGSw5wBXF2C1IojnFY%2BRCLcxDnZgpA4FEyJbnrdGA3beyGxZPGI7MUVsBXXagSKNyu2RMhOA4TNNNknmRf6wrEBMUjOMrsO%2FvQIAjd2QUgJNj57ww%2F7DlvAY6pgH62FsNj2L%2F1g0MpzCxq4j167GvVki06HiYy3cjYgC1hgbLvJPX%2FSFstwiMnfQL13AecQ%2FmPDyPt9YaqrSlSwgDcqm3skCil%2FIg%2B5yzx08uFFYrvzsIV3MssjELt%2FAhkr%2Bv%2B%2BDtPTTWFxW6KTbMWQo1igtPAaN5%2FQFVHSDLLneXDwHhbGlmjGguCLwNmXpBQYe23D1WVtWHaaz6fJKbOe7AkmTU7iB6&X-Amz-Signature=7c4136c55c49b201c9e2e015d93150e8f1de2a4de84d18779f690dfecad844cf&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SHTYKV42%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJGMEQCIDdegJHHWavAHy0ogvUi2S0usuJJx5ElPilawI1To0CoAiBtpjxlH4bOnYPT9DRXj95oj%2Bxp626iEqG4mKP4UI4KUCr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIM42oMkxltwPbTZSKZKtwDeJLhpUED4H9GmZ1sV%2BqfJ67rsMYor1huef3hk5O6blCskhLBD4K4NUNwf%2FXUvKhFwwSt%2FxM4Q644P1fpbCBJ3T8xtwH2qfPSWJ8IFhuDxURUMF2Skl2ccWgSztjI3SSb%2BIg2xAX92bEABCU92jh1Ef0cTDJpj32OtdY9Xg5rMcyq1lntlht0tgYOAhr9nos4Y1Hemx1sLaw1NnRXzPL%2Fy7TaVYXaGCdOLwTIM17SUyU6%2Bavk1LUJdW4i%2FEfnbUCKowVzv8py%2BKxTAuOOconaLmef608VEkG1yD%2BgQvsx%2BeS8sZ2EHRQUTAB9wICKvvXhmqJUkgIkpMfYFEk34wegcfo%2F8RGFID8jMFFs4aNQNR3tzIxUxYvFwWaucJn2rMIjTBu9YecMOWUPSVPvuGso8Vk2MGmxi2JyMIs1H7x%2Faj2XVWZdo2vzzkkvxk6YBHx1dEK4TrUi3wTS3Lvj6yWsgS5HzkmVJqRmtFgmKoguKTQ2adTm%2FsH%2FBCo61rPdmU%2Fj9RPadK2bEeyIGSw5wBXF2C1IojnFY%2BRCLcxDnZgpA4FEyJbnrdGA3beyGxZPGI7MUVsBXXagSKNyu2RMhOA4TNNNknmRf6wrEBMUjOMrsO%2FvQIAjd2QUgJNj57ww%2F7DlvAY6pgH62FsNj2L%2F1g0MpzCxq4j167GvVki06HiYy3cjYgC1hgbLvJPX%2FSFstwiMnfQL13AecQ%2FmPDyPt9YaqrSlSwgDcqm3skCil%2FIg%2B5yzx08uFFYrvzsIV3MssjELt%2FAhkr%2Bv%2B%2BDtPTTWFxW6KTbMWQo1igtPAaN5%2FQFVHSDLLneXDwHhbGlmjGguCLwNmXpBQYe23D1WVtWHaaz6fJKbOe7AkmTU7iB6&X-Amz-Signature=3eaa33b598cc7945654480d221cf527904e7df69f81f4080d977a67d05a0ff13&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SHTYKV42%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJGMEQCIDdegJHHWavAHy0ogvUi2S0usuJJx5ElPilawI1To0CoAiBtpjxlH4bOnYPT9DRXj95oj%2Bxp626iEqG4mKP4UI4KUCr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIM42oMkxltwPbTZSKZKtwDeJLhpUED4H9GmZ1sV%2BqfJ67rsMYor1huef3hk5O6blCskhLBD4K4NUNwf%2FXUvKhFwwSt%2FxM4Q644P1fpbCBJ3T8xtwH2qfPSWJ8IFhuDxURUMF2Skl2ccWgSztjI3SSb%2BIg2xAX92bEABCU92jh1Ef0cTDJpj32OtdY9Xg5rMcyq1lntlht0tgYOAhr9nos4Y1Hemx1sLaw1NnRXzPL%2Fy7TaVYXaGCdOLwTIM17SUyU6%2Bavk1LUJdW4i%2FEfnbUCKowVzv8py%2BKxTAuOOconaLmef608VEkG1yD%2BgQvsx%2BeS8sZ2EHRQUTAB9wICKvvXhmqJUkgIkpMfYFEk34wegcfo%2F8RGFID8jMFFs4aNQNR3tzIxUxYvFwWaucJn2rMIjTBu9YecMOWUPSVPvuGso8Vk2MGmxi2JyMIs1H7x%2Faj2XVWZdo2vzzkkvxk6YBHx1dEK4TrUi3wTS3Lvj6yWsgS5HzkmVJqRmtFgmKoguKTQ2adTm%2FsH%2FBCo61rPdmU%2Fj9RPadK2bEeyIGSw5wBXF2C1IojnFY%2BRCLcxDnZgpA4FEyJbnrdGA3beyGxZPGI7MUVsBXXagSKNyu2RMhOA4TNNNknmRf6wrEBMUjOMrsO%2FvQIAjd2QUgJNj57ww%2F7DlvAY6pgH62FsNj2L%2F1g0MpzCxq4j167GvVki06HiYy3cjYgC1hgbLvJPX%2FSFstwiMnfQL13AecQ%2FmPDyPt9YaqrSlSwgDcqm3skCil%2FIg%2B5yzx08uFFYrvzsIV3MssjELt%2FAhkr%2Bv%2B%2BDtPTTWFxW6KTbMWQo1igtPAaN5%2FQFVHSDLLneXDwHhbGlmjGguCLwNmXpBQYe23D1WVtWHaaz6fJKbOe7AkmTU7iB6&X-Amz-Signature=7313ccd9fbdb53e3a611e46e78279f6eed87b97701becc257f0ef6b199d19a12&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SHTYKV42%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJGMEQCIDdegJHHWavAHy0ogvUi2S0usuJJx5ElPilawI1To0CoAiBtpjxlH4bOnYPT9DRXj95oj%2Bxp626iEqG4mKP4UI4KUCr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIM42oMkxltwPbTZSKZKtwDeJLhpUED4H9GmZ1sV%2BqfJ67rsMYor1huef3hk5O6blCskhLBD4K4NUNwf%2FXUvKhFwwSt%2FxM4Q644P1fpbCBJ3T8xtwH2qfPSWJ8IFhuDxURUMF2Skl2ccWgSztjI3SSb%2BIg2xAX92bEABCU92jh1Ef0cTDJpj32OtdY9Xg5rMcyq1lntlht0tgYOAhr9nos4Y1Hemx1sLaw1NnRXzPL%2Fy7TaVYXaGCdOLwTIM17SUyU6%2Bavk1LUJdW4i%2FEfnbUCKowVzv8py%2BKxTAuOOconaLmef608VEkG1yD%2BgQvsx%2BeS8sZ2EHRQUTAB9wICKvvXhmqJUkgIkpMfYFEk34wegcfo%2F8RGFID8jMFFs4aNQNR3tzIxUxYvFwWaucJn2rMIjTBu9YecMOWUPSVPvuGso8Vk2MGmxi2JyMIs1H7x%2Faj2XVWZdo2vzzkkvxk6YBHx1dEK4TrUi3wTS3Lvj6yWsgS5HzkmVJqRmtFgmKoguKTQ2adTm%2FsH%2FBCo61rPdmU%2Fj9RPadK2bEeyIGSw5wBXF2C1IojnFY%2BRCLcxDnZgpA4FEyJbnrdGA3beyGxZPGI7MUVsBXXagSKNyu2RMhOA4TNNNknmRf6wrEBMUjOMrsO%2FvQIAjd2QUgJNj57ww%2F7DlvAY6pgH62FsNj2L%2F1g0MpzCxq4j167GvVki06HiYy3cjYgC1hgbLvJPX%2FSFstwiMnfQL13AecQ%2FmPDyPt9YaqrSlSwgDcqm3skCil%2FIg%2B5yzx08uFFYrvzsIV3MssjELt%2FAhkr%2Bv%2B%2BDtPTTWFxW6KTbMWQo1igtPAaN5%2FQFVHSDLLneXDwHhbGlmjGguCLwNmXpBQYe23D1WVtWHaaz6fJKbOe7AkmTU7iB6&X-Amz-Signature=42b627760842bb93279c33f980cae244bd14692e8977b00f0340e24b8c573c41&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SHTYKV42%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJGMEQCIDdegJHHWavAHy0ogvUi2S0usuJJx5ElPilawI1To0CoAiBtpjxlH4bOnYPT9DRXj95oj%2Bxp626iEqG4mKP4UI4KUCr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIM42oMkxltwPbTZSKZKtwDeJLhpUED4H9GmZ1sV%2BqfJ67rsMYor1huef3hk5O6blCskhLBD4K4NUNwf%2FXUvKhFwwSt%2FxM4Q644P1fpbCBJ3T8xtwH2qfPSWJ8IFhuDxURUMF2Skl2ccWgSztjI3SSb%2BIg2xAX92bEABCU92jh1Ef0cTDJpj32OtdY9Xg5rMcyq1lntlht0tgYOAhr9nos4Y1Hemx1sLaw1NnRXzPL%2Fy7TaVYXaGCdOLwTIM17SUyU6%2Bavk1LUJdW4i%2FEfnbUCKowVzv8py%2BKxTAuOOconaLmef608VEkG1yD%2BgQvsx%2BeS8sZ2EHRQUTAB9wICKvvXhmqJUkgIkpMfYFEk34wegcfo%2F8RGFID8jMFFs4aNQNR3tzIxUxYvFwWaucJn2rMIjTBu9YecMOWUPSVPvuGso8Vk2MGmxi2JyMIs1H7x%2Faj2XVWZdo2vzzkkvxk6YBHx1dEK4TrUi3wTS3Lvj6yWsgS5HzkmVJqRmtFgmKoguKTQ2adTm%2FsH%2FBCo61rPdmU%2Fj9RPadK2bEeyIGSw5wBXF2C1IojnFY%2BRCLcxDnZgpA4FEyJbnrdGA3beyGxZPGI7MUVsBXXagSKNyu2RMhOA4TNNNknmRf6wrEBMUjOMrsO%2FvQIAjd2QUgJNj57ww%2F7DlvAY6pgH62FsNj2L%2F1g0MpzCxq4j167GvVki06HiYy3cjYgC1hgbLvJPX%2FSFstwiMnfQL13AecQ%2FmPDyPt9YaqrSlSwgDcqm3skCil%2FIg%2B5yzx08uFFYrvzsIV3MssjELt%2FAhkr%2Bv%2B%2BDtPTTWFxW6KTbMWQo1igtPAaN5%2FQFVHSDLLneXDwHhbGlmjGguCLwNmXpBQYe23D1WVtWHaaz6fJKbOe7AkmTU7iB6&X-Amz-Signature=1877e91284f6235062e731e11e55ddad1abf742ac0451fd68bf3e04780df4444&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SHTYKV42%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJGMEQCIDdegJHHWavAHy0ogvUi2S0usuJJx5ElPilawI1To0CoAiBtpjxlH4bOnYPT9DRXj95oj%2Bxp626iEqG4mKP4UI4KUCr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIM42oMkxltwPbTZSKZKtwDeJLhpUED4H9GmZ1sV%2BqfJ67rsMYor1huef3hk5O6blCskhLBD4K4NUNwf%2FXUvKhFwwSt%2FxM4Q644P1fpbCBJ3T8xtwH2qfPSWJ8IFhuDxURUMF2Skl2ccWgSztjI3SSb%2BIg2xAX92bEABCU92jh1Ef0cTDJpj32OtdY9Xg5rMcyq1lntlht0tgYOAhr9nos4Y1Hemx1sLaw1NnRXzPL%2Fy7TaVYXaGCdOLwTIM17SUyU6%2Bavk1LUJdW4i%2FEfnbUCKowVzv8py%2BKxTAuOOconaLmef608VEkG1yD%2BgQvsx%2BeS8sZ2EHRQUTAB9wICKvvXhmqJUkgIkpMfYFEk34wegcfo%2F8RGFID8jMFFs4aNQNR3tzIxUxYvFwWaucJn2rMIjTBu9YecMOWUPSVPvuGso8Vk2MGmxi2JyMIs1H7x%2Faj2XVWZdo2vzzkkvxk6YBHx1dEK4TrUi3wTS3Lvj6yWsgS5HzkmVJqRmtFgmKoguKTQ2adTm%2FsH%2FBCo61rPdmU%2Fj9RPadK2bEeyIGSw5wBXF2C1IojnFY%2BRCLcxDnZgpA4FEyJbnrdGA3beyGxZPGI7MUVsBXXagSKNyu2RMhOA4TNNNknmRf6wrEBMUjOMrsO%2FvQIAjd2QUgJNj57ww%2F7DlvAY6pgH62FsNj2L%2F1g0MpzCxq4j167GvVki06HiYy3cjYgC1hgbLvJPX%2FSFstwiMnfQL13AecQ%2FmPDyPt9YaqrSlSwgDcqm3skCil%2FIg%2B5yzx08uFFYrvzsIV3MssjELt%2FAhkr%2Bv%2B%2BDtPTTWFxW6KTbMWQo1igtPAaN5%2FQFVHSDLLneXDwHhbGlmjGguCLwNmXpBQYe23D1WVtWHaaz6fJKbOe7AkmTU7iB6&X-Amz-Signature=2961d7aa322ecbd9d46c5e560e8bbb51a4b7ed8bec7af23ee07c3f94f4c3dcfe&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SHTYKV42%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJGMEQCIDdegJHHWavAHy0ogvUi2S0usuJJx5ElPilawI1To0CoAiBtpjxlH4bOnYPT9DRXj95oj%2Bxp626iEqG4mKP4UI4KUCr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIM42oMkxltwPbTZSKZKtwDeJLhpUED4H9GmZ1sV%2BqfJ67rsMYor1huef3hk5O6blCskhLBD4K4NUNwf%2FXUvKhFwwSt%2FxM4Q644P1fpbCBJ3T8xtwH2qfPSWJ8IFhuDxURUMF2Skl2ccWgSztjI3SSb%2BIg2xAX92bEABCU92jh1Ef0cTDJpj32OtdY9Xg5rMcyq1lntlht0tgYOAhr9nos4Y1Hemx1sLaw1NnRXzPL%2Fy7TaVYXaGCdOLwTIM17SUyU6%2Bavk1LUJdW4i%2FEfnbUCKowVzv8py%2BKxTAuOOconaLmef608VEkG1yD%2BgQvsx%2BeS8sZ2EHRQUTAB9wICKvvXhmqJUkgIkpMfYFEk34wegcfo%2F8RGFID8jMFFs4aNQNR3tzIxUxYvFwWaucJn2rMIjTBu9YecMOWUPSVPvuGso8Vk2MGmxi2JyMIs1H7x%2Faj2XVWZdo2vzzkkvxk6YBHx1dEK4TrUi3wTS3Lvj6yWsgS5HzkmVJqRmtFgmKoguKTQ2adTm%2FsH%2FBCo61rPdmU%2Fj9RPadK2bEeyIGSw5wBXF2C1IojnFY%2BRCLcxDnZgpA4FEyJbnrdGA3beyGxZPGI7MUVsBXXagSKNyu2RMhOA4TNNNknmRf6wrEBMUjOMrsO%2FvQIAjd2QUgJNj57ww%2F7DlvAY6pgH62FsNj2L%2F1g0MpzCxq4j167GvVki06HiYy3cjYgC1hgbLvJPX%2FSFstwiMnfQL13AecQ%2FmPDyPt9YaqrSlSwgDcqm3skCil%2FIg%2B5yzx08uFFYrvzsIV3MssjELt%2FAhkr%2Bv%2B%2BDtPTTWFxW6KTbMWQo1igtPAaN5%2FQFVHSDLLneXDwHhbGlmjGguCLwNmXpBQYe23D1WVtWHaaz6fJKbOe7AkmTU7iB6&X-Amz-Signature=a9d02077755f6a0402addb66203ca6e0465c2dbe97b841cc96ea92484416f420&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SHTYKV42%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJGMEQCIDdegJHHWavAHy0ogvUi2S0usuJJx5ElPilawI1To0CoAiBtpjxlH4bOnYPT9DRXj95oj%2Bxp626iEqG4mKP4UI4KUCr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIM42oMkxltwPbTZSKZKtwDeJLhpUED4H9GmZ1sV%2BqfJ67rsMYor1huef3hk5O6blCskhLBD4K4NUNwf%2FXUvKhFwwSt%2FxM4Q644P1fpbCBJ3T8xtwH2qfPSWJ8IFhuDxURUMF2Skl2ccWgSztjI3SSb%2BIg2xAX92bEABCU92jh1Ef0cTDJpj32OtdY9Xg5rMcyq1lntlht0tgYOAhr9nos4Y1Hemx1sLaw1NnRXzPL%2Fy7TaVYXaGCdOLwTIM17SUyU6%2Bavk1LUJdW4i%2FEfnbUCKowVzv8py%2BKxTAuOOconaLmef608VEkG1yD%2BgQvsx%2BeS8sZ2EHRQUTAB9wICKvvXhmqJUkgIkpMfYFEk34wegcfo%2F8RGFID8jMFFs4aNQNR3tzIxUxYvFwWaucJn2rMIjTBu9YecMOWUPSVPvuGso8Vk2MGmxi2JyMIs1H7x%2Faj2XVWZdo2vzzkkvxk6YBHx1dEK4TrUi3wTS3Lvj6yWsgS5HzkmVJqRmtFgmKoguKTQ2adTm%2FsH%2FBCo61rPdmU%2Fj9RPadK2bEeyIGSw5wBXF2C1IojnFY%2BRCLcxDnZgpA4FEyJbnrdGA3beyGxZPGI7MUVsBXXagSKNyu2RMhOA4TNNNknmRf6wrEBMUjOMrsO%2FvQIAjd2QUgJNj57ww%2F7DlvAY6pgH62FsNj2L%2F1g0MpzCxq4j167GvVki06HiYy3cjYgC1hgbLvJPX%2FSFstwiMnfQL13AecQ%2FmPDyPt9YaqrSlSwgDcqm3skCil%2FIg%2B5yzx08uFFYrvzsIV3MssjELt%2FAhkr%2Bv%2B%2BDtPTTWFxW6KTbMWQo1igtPAaN5%2FQFVHSDLLneXDwHhbGlmjGguCLwNmXpBQYe23D1WVtWHaaz6fJKbOe7AkmTU7iB6&X-Amz-Signature=4dfba120bc4a509da0fdaae87b8a701a5ab8ebd5c62bc27adf2a0ebb35a2ea8b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SHTYKV42%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJGMEQCIDdegJHHWavAHy0ogvUi2S0usuJJx5ElPilawI1To0CoAiBtpjxlH4bOnYPT9DRXj95oj%2Bxp626iEqG4mKP4UI4KUCr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIM42oMkxltwPbTZSKZKtwDeJLhpUED4H9GmZ1sV%2BqfJ67rsMYor1huef3hk5O6blCskhLBD4K4NUNwf%2FXUvKhFwwSt%2FxM4Q644P1fpbCBJ3T8xtwH2qfPSWJ8IFhuDxURUMF2Skl2ccWgSztjI3SSb%2BIg2xAX92bEABCU92jh1Ef0cTDJpj32OtdY9Xg5rMcyq1lntlht0tgYOAhr9nos4Y1Hemx1sLaw1NnRXzPL%2Fy7TaVYXaGCdOLwTIM17SUyU6%2Bavk1LUJdW4i%2FEfnbUCKowVzv8py%2BKxTAuOOconaLmef608VEkG1yD%2BgQvsx%2BeS8sZ2EHRQUTAB9wICKvvXhmqJUkgIkpMfYFEk34wegcfo%2F8RGFID8jMFFs4aNQNR3tzIxUxYvFwWaucJn2rMIjTBu9YecMOWUPSVPvuGso8Vk2MGmxi2JyMIs1H7x%2Faj2XVWZdo2vzzkkvxk6YBHx1dEK4TrUi3wTS3Lvj6yWsgS5HzkmVJqRmtFgmKoguKTQ2adTm%2FsH%2FBCo61rPdmU%2Fj9RPadK2bEeyIGSw5wBXF2C1IojnFY%2BRCLcxDnZgpA4FEyJbnrdGA3beyGxZPGI7MUVsBXXagSKNyu2RMhOA4TNNNknmRf6wrEBMUjOMrsO%2FvQIAjd2QUgJNj57ww%2F7DlvAY6pgH62FsNj2L%2F1g0MpzCxq4j167GvVki06HiYy3cjYgC1hgbLvJPX%2FSFstwiMnfQL13AecQ%2FmPDyPt9YaqrSlSwgDcqm3skCil%2FIg%2B5yzx08uFFYrvzsIV3MssjELt%2FAhkr%2Bv%2B%2BDtPTTWFxW6KTbMWQo1igtPAaN5%2FQFVHSDLLneXDwHhbGlmjGguCLwNmXpBQYe23D1WVtWHaaz6fJKbOe7AkmTU7iB6&X-Amz-Signature=975430aee4648ce046858b2d1c0886bf569795ee8b6020897e4175b07dbfa4d0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665MFO7HMP%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJHMEUCIQDojzllhbKTye3KiT6GxW2xsFY%2Fkv2IOJEltlCz7GsBagIgF33yP3JIU2iJTTnp7iChI6QISB3TFOoNCod768Dgikoq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDNmZI5E1wtaOIvc60CrcA8A%2FuXGuRcVqdBBU6NxtQGXK0De9P6JVilZ%2FNkeYcje0TGh3iFw7%2F%2BloekYywWmY7cWxMjEB5XRfZ6dCt%2FdxCf8%2FvQrQzKk5dYQchtmMbx6vpDCuMwmyhugelR73H4AD%2BI3IbUI6L1Q72wXfBbP5XP5DDTCyjh5JLPN9wVcnXFEkB8DfWcMo9jWdHOJ8Hw3xQH3ncL85umpx6meAMyYLCxsafO8wmYUCGTotVUNLBZGHH5EX5HzzM%2Bl%2BxM%2BzwzkP9emZBYDBWYkG82uF2pevMQvstxAJt8hOb6vm23LIdBQUwluEUmtU8RXYK8lCauepFu07ZjSNA%2B5Mz08MmTvjdnbZWvW1GVgnXCd6fC4B0k72JIyq6zNe7JJp7JGbC9DPCVpVgFcr4%2BH4wmbReJNB%2B6jddf%2FxlQ1xq9zq6ywHnSXjAY8TemExr%2BQIX8FSbYKbqA2rW16xIi%2BRcHW6MYsg9i0Q%2FbXOn3XR%2F6viK8Sop%2FoDSiZseyfQttlUN3jaB93KmP8pgnBCmAb8A5QA%2F1iQ5GRg906Hy3LUl3DFv1UwH1tZY2WDdIgwV%2F%2FzgqrUD%2FN1hC33fRGODI8i1%2B0aUESkuROz0AoGOYDnWc8GP5ZgO%2FoQz%2BCPLmUIIX9THHECMICx5bwGOqUB08u0bjzP27d6ilNXFsrKmuiTvdF1EbBqaHuJHTMyDrRrtYPsRrnV3SUdlBOGa72px4Kl7R01vBAr%2FJOCzoa8aE5Zerii%2FfNKOzBbRK0fq7fJpFifQPRX0d3JR6zAtu%2FDoxkECS%2Bw8tJ8xpmeBGuetjOH6XYQSbsK40K1YAxBLcLjMkUP7ghgStARVK8BPHdbYuN5Cp06pY9zpdU9M9sFvj5NCO7F&X-Amz-Signature=cb575e5ee7d5af8d40cf5c035d168faacdc237faa4bbd64628a031d076cacfd5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665MFO7HMP%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJHMEUCIQDojzllhbKTye3KiT6GxW2xsFY%2Fkv2IOJEltlCz7GsBagIgF33yP3JIU2iJTTnp7iChI6QISB3TFOoNCod768Dgikoq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDNmZI5E1wtaOIvc60CrcA8A%2FuXGuRcVqdBBU6NxtQGXK0De9P6JVilZ%2FNkeYcje0TGh3iFw7%2F%2BloekYywWmY7cWxMjEB5XRfZ6dCt%2FdxCf8%2FvQrQzKk5dYQchtmMbx6vpDCuMwmyhugelR73H4AD%2BI3IbUI6L1Q72wXfBbP5XP5DDTCyjh5JLPN9wVcnXFEkB8DfWcMo9jWdHOJ8Hw3xQH3ncL85umpx6meAMyYLCxsafO8wmYUCGTotVUNLBZGHH5EX5HzzM%2Bl%2BxM%2BzwzkP9emZBYDBWYkG82uF2pevMQvstxAJt8hOb6vm23LIdBQUwluEUmtU8RXYK8lCauepFu07ZjSNA%2B5Mz08MmTvjdnbZWvW1GVgnXCd6fC4B0k72JIyq6zNe7JJp7JGbC9DPCVpVgFcr4%2BH4wmbReJNB%2B6jddf%2FxlQ1xq9zq6ywHnSXjAY8TemExr%2BQIX8FSbYKbqA2rW16xIi%2BRcHW6MYsg9i0Q%2FbXOn3XR%2F6viK8Sop%2FoDSiZseyfQttlUN3jaB93KmP8pgnBCmAb8A5QA%2F1iQ5GRg906Hy3LUl3DFv1UwH1tZY2WDdIgwV%2F%2FzgqrUD%2FN1hC33fRGODI8i1%2B0aUESkuROz0AoGOYDnWc8GP5ZgO%2FoQz%2BCPLmUIIX9THHECMICx5bwGOqUB08u0bjzP27d6ilNXFsrKmuiTvdF1EbBqaHuJHTMyDrRrtYPsRrnV3SUdlBOGa72px4Kl7R01vBAr%2FJOCzoa8aE5Zerii%2FfNKOzBbRK0fq7fJpFifQPRX0d3JR6zAtu%2FDoxkECS%2Bw8tJ8xpmeBGuetjOH6XYQSbsK40K1YAxBLcLjMkUP7ghgStARVK8BPHdbYuN5Cp06pY9zpdU9M9sFvj5NCO7F&X-Amz-Signature=6b153d29ae9db48d824c9d7132748526d9b20e7c168ef6bae147e4e25ab4067a&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
