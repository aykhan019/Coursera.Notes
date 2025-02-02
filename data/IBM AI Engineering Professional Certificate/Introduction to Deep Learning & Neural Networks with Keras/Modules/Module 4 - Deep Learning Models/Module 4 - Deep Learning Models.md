

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UDWBIENZ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHnzKWpgd%2FYfU%2BTaP9Sd6fhlLahbIsMBU6LBdzqly0T%2FAiEAyLpnIcA03qsXiI0qA2KNVA7Z3DDTYBSdbT%2BiY7X3b%2BQqiAQI5P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHGW%2FVEtm9kmH%2F5rpSrcA%2FeATq7V6YApbyF2%2BEUbI6zyUYwi8cpXQ3yQh9sNCaHuLVnVTx2wYzkz0RLbRwe7ot72BgiyVqJoQScirCKmmmcs%2FFe%2BbGYyGsfQu2Cp8p2oQPl8PpmsrW77K9Fw3QLeThf5c021t%2FT%2Fslw%2F2tqVwr0HO1lWbcqOox2FIQdLwmME%2FouiAExsAEywMr92pwcEUera1w87WzySrtbLwnOEI8FuoiibeZVJeWewzrH1cHAmS2LTgmKKNWpUi1JQRtYCP8qai5x4Nmp7GT1fsbwz0buRz3egIL5%2B4NeqXbtpeTuCqi%2BBoLccXtBubelCAnoS%2FFtnwlothvNsLG7PTONLqZH1SNZGwSkFlete2VIgFrVE70mBFXkd3FExjg8N2FbbV%2FbcXSclJTbiSGGMYRG3GZRatRq27k1tW31TE9wku6n8Tc3ybMiANzIwl%2BXBZI%2FpC55QrfLnTuZYrfz1I%2FblFJ6shP13gyr9rD5U%2FE5HmL91LO%2Fs%2BgFjreX4ET%2F2M%2FZFRRNMWtdWhCLQ3a3jFPthLRc7D7Eec4jt%2Fge67V8lXy%2FF4z1iqUNUXEUuJoUxzZpLDI3F2ueF5oh9JKD9lBgnWib282VpfEwob1A7q%2FIe%2FRlII5amie4TUDgkRgZ%2BMIS7%2B7wGOqUBqhuYdhs48TFNzDURkgYO9dK1IDr7H67HW620I2a0AGP1BB15TJIvsy%2FBq2P7vcY6TSEUIJ2fVrhS7YhpFPsi4BpHCkhRvs71PpWGZ55raU5T1W4lHICS7YW2HYuNBcRAcoCeWavcCriPdTHkKLKVA0yTmGsBH9vYjNyTb4GGvUt0%2B3PBTSN8r5WessfTPP2gU4sLNpHxdCFvM1Yq%2B7FB6c0h8e08&X-Amz-Signature=da3ab3ed09d4cc697e3187255fba29560b09dbb8ae0d60eb6ae6c448eb1c3681&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UDWBIENZ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHnzKWpgd%2FYfU%2BTaP9Sd6fhlLahbIsMBU6LBdzqly0T%2FAiEAyLpnIcA03qsXiI0qA2KNVA7Z3DDTYBSdbT%2BiY7X3b%2BQqiAQI5P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHGW%2FVEtm9kmH%2F5rpSrcA%2FeATq7V6YApbyF2%2BEUbI6zyUYwi8cpXQ3yQh9sNCaHuLVnVTx2wYzkz0RLbRwe7ot72BgiyVqJoQScirCKmmmcs%2FFe%2BbGYyGsfQu2Cp8p2oQPl8PpmsrW77K9Fw3QLeThf5c021t%2FT%2Fslw%2F2tqVwr0HO1lWbcqOox2FIQdLwmME%2FouiAExsAEywMr92pwcEUera1w87WzySrtbLwnOEI8FuoiibeZVJeWewzrH1cHAmS2LTgmKKNWpUi1JQRtYCP8qai5x4Nmp7GT1fsbwz0buRz3egIL5%2B4NeqXbtpeTuCqi%2BBoLccXtBubelCAnoS%2FFtnwlothvNsLG7PTONLqZH1SNZGwSkFlete2VIgFrVE70mBFXkd3FExjg8N2FbbV%2FbcXSclJTbiSGGMYRG3GZRatRq27k1tW31TE9wku6n8Tc3ybMiANzIwl%2BXBZI%2FpC55QrfLnTuZYrfz1I%2FblFJ6shP13gyr9rD5U%2FE5HmL91LO%2Fs%2BgFjreX4ET%2F2M%2FZFRRNMWtdWhCLQ3a3jFPthLRc7D7Eec4jt%2Fge67V8lXy%2FF4z1iqUNUXEUuJoUxzZpLDI3F2ueF5oh9JKD9lBgnWib282VpfEwob1A7q%2FIe%2FRlII5amie4TUDgkRgZ%2BMIS7%2B7wGOqUBqhuYdhs48TFNzDURkgYO9dK1IDr7H67HW620I2a0AGP1BB15TJIvsy%2FBq2P7vcY6TSEUIJ2fVrhS7YhpFPsi4BpHCkhRvs71PpWGZ55raU5T1W4lHICS7YW2HYuNBcRAcoCeWavcCriPdTHkKLKVA0yTmGsBH9vYjNyTb4GGvUt0%2B3PBTSN8r5WessfTPP2gU4sLNpHxdCFvM1Yq%2B7FB6c0h8e08&X-Amz-Signature=983679e8c8c2ebcd4c9a402c76dcb2f318efb48c81a29209cb5f0d175ef33163&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UDWBIENZ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHnzKWpgd%2FYfU%2BTaP9Sd6fhlLahbIsMBU6LBdzqly0T%2FAiEAyLpnIcA03qsXiI0qA2KNVA7Z3DDTYBSdbT%2BiY7X3b%2BQqiAQI5P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHGW%2FVEtm9kmH%2F5rpSrcA%2FeATq7V6YApbyF2%2BEUbI6zyUYwi8cpXQ3yQh9sNCaHuLVnVTx2wYzkz0RLbRwe7ot72BgiyVqJoQScirCKmmmcs%2FFe%2BbGYyGsfQu2Cp8p2oQPl8PpmsrW77K9Fw3QLeThf5c021t%2FT%2Fslw%2F2tqVwr0HO1lWbcqOox2FIQdLwmME%2FouiAExsAEywMr92pwcEUera1w87WzySrtbLwnOEI8FuoiibeZVJeWewzrH1cHAmS2LTgmKKNWpUi1JQRtYCP8qai5x4Nmp7GT1fsbwz0buRz3egIL5%2B4NeqXbtpeTuCqi%2BBoLccXtBubelCAnoS%2FFtnwlothvNsLG7PTONLqZH1SNZGwSkFlete2VIgFrVE70mBFXkd3FExjg8N2FbbV%2FbcXSclJTbiSGGMYRG3GZRatRq27k1tW31TE9wku6n8Tc3ybMiANzIwl%2BXBZI%2FpC55QrfLnTuZYrfz1I%2FblFJ6shP13gyr9rD5U%2FE5HmL91LO%2Fs%2BgFjreX4ET%2F2M%2FZFRRNMWtdWhCLQ3a3jFPthLRc7D7Eec4jt%2Fge67V8lXy%2FF4z1iqUNUXEUuJoUxzZpLDI3F2ueF5oh9JKD9lBgnWib282VpfEwob1A7q%2FIe%2FRlII5amie4TUDgkRgZ%2BMIS7%2B7wGOqUBqhuYdhs48TFNzDURkgYO9dK1IDr7H67HW620I2a0AGP1BB15TJIvsy%2FBq2P7vcY6TSEUIJ2fVrhS7YhpFPsi4BpHCkhRvs71PpWGZ55raU5T1W4lHICS7YW2HYuNBcRAcoCeWavcCriPdTHkKLKVA0yTmGsBH9vYjNyTb4GGvUt0%2B3PBTSN8r5WessfTPP2gU4sLNpHxdCFvM1Yq%2B7FB6c0h8e08&X-Amz-Signature=3e5be61d79ffe34c302e95d965fc2e57af747a0a897c436e2281a6f4db7a6fd7&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UDWBIENZ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHnzKWpgd%2FYfU%2BTaP9Sd6fhlLahbIsMBU6LBdzqly0T%2FAiEAyLpnIcA03qsXiI0qA2KNVA7Z3DDTYBSdbT%2BiY7X3b%2BQqiAQI5P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHGW%2FVEtm9kmH%2F5rpSrcA%2FeATq7V6YApbyF2%2BEUbI6zyUYwi8cpXQ3yQh9sNCaHuLVnVTx2wYzkz0RLbRwe7ot72BgiyVqJoQScirCKmmmcs%2FFe%2BbGYyGsfQu2Cp8p2oQPl8PpmsrW77K9Fw3QLeThf5c021t%2FT%2Fslw%2F2tqVwr0HO1lWbcqOox2FIQdLwmME%2FouiAExsAEywMr92pwcEUera1w87WzySrtbLwnOEI8FuoiibeZVJeWewzrH1cHAmS2LTgmKKNWpUi1JQRtYCP8qai5x4Nmp7GT1fsbwz0buRz3egIL5%2B4NeqXbtpeTuCqi%2BBoLccXtBubelCAnoS%2FFtnwlothvNsLG7PTONLqZH1SNZGwSkFlete2VIgFrVE70mBFXkd3FExjg8N2FbbV%2FbcXSclJTbiSGGMYRG3GZRatRq27k1tW31TE9wku6n8Tc3ybMiANzIwl%2BXBZI%2FpC55QrfLnTuZYrfz1I%2FblFJ6shP13gyr9rD5U%2FE5HmL91LO%2Fs%2BgFjreX4ET%2F2M%2FZFRRNMWtdWhCLQ3a3jFPthLRc7D7Eec4jt%2Fge67V8lXy%2FF4z1iqUNUXEUuJoUxzZpLDI3F2ueF5oh9JKD9lBgnWib282VpfEwob1A7q%2FIe%2FRlII5amie4TUDgkRgZ%2BMIS7%2B7wGOqUBqhuYdhs48TFNzDURkgYO9dK1IDr7H67HW620I2a0AGP1BB15TJIvsy%2FBq2P7vcY6TSEUIJ2fVrhS7YhpFPsi4BpHCkhRvs71PpWGZ55raU5T1W4lHICS7YW2HYuNBcRAcoCeWavcCriPdTHkKLKVA0yTmGsBH9vYjNyTb4GGvUt0%2B3PBTSN8r5WessfTPP2gU4sLNpHxdCFvM1Yq%2B7FB6c0h8e08&X-Amz-Signature=e968a98896c845507a88d34152f1750a990b09c14951a7ce403e263d7f295c9f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UDWBIENZ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHnzKWpgd%2FYfU%2BTaP9Sd6fhlLahbIsMBU6LBdzqly0T%2FAiEAyLpnIcA03qsXiI0qA2KNVA7Z3DDTYBSdbT%2BiY7X3b%2BQqiAQI5P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHGW%2FVEtm9kmH%2F5rpSrcA%2FeATq7V6YApbyF2%2BEUbI6zyUYwi8cpXQ3yQh9sNCaHuLVnVTx2wYzkz0RLbRwe7ot72BgiyVqJoQScirCKmmmcs%2FFe%2BbGYyGsfQu2Cp8p2oQPl8PpmsrW77K9Fw3QLeThf5c021t%2FT%2Fslw%2F2tqVwr0HO1lWbcqOox2FIQdLwmME%2FouiAExsAEywMr92pwcEUera1w87WzySrtbLwnOEI8FuoiibeZVJeWewzrH1cHAmS2LTgmKKNWpUi1JQRtYCP8qai5x4Nmp7GT1fsbwz0buRz3egIL5%2B4NeqXbtpeTuCqi%2BBoLccXtBubelCAnoS%2FFtnwlothvNsLG7PTONLqZH1SNZGwSkFlete2VIgFrVE70mBFXkd3FExjg8N2FbbV%2FbcXSclJTbiSGGMYRG3GZRatRq27k1tW31TE9wku6n8Tc3ybMiANzIwl%2BXBZI%2FpC55QrfLnTuZYrfz1I%2FblFJ6shP13gyr9rD5U%2FE5HmL91LO%2Fs%2BgFjreX4ET%2F2M%2FZFRRNMWtdWhCLQ3a3jFPthLRc7D7Eec4jt%2Fge67V8lXy%2FF4z1iqUNUXEUuJoUxzZpLDI3F2ueF5oh9JKD9lBgnWib282VpfEwob1A7q%2FIe%2FRlII5amie4TUDgkRgZ%2BMIS7%2B7wGOqUBqhuYdhs48TFNzDURkgYO9dK1IDr7H67HW620I2a0AGP1BB15TJIvsy%2FBq2P7vcY6TSEUIJ2fVrhS7YhpFPsi4BpHCkhRvs71PpWGZ55raU5T1W4lHICS7YW2HYuNBcRAcoCeWavcCriPdTHkKLKVA0yTmGsBH9vYjNyTb4GGvUt0%2B3PBTSN8r5WessfTPP2gU4sLNpHxdCFvM1Yq%2B7FB6c0h8e08&X-Amz-Signature=5ef5d77c7b58cfcbb3a20190658f44d39df9b3ce97cac7ec148603efb6470a63&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UDWBIENZ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHnzKWpgd%2FYfU%2BTaP9Sd6fhlLahbIsMBU6LBdzqly0T%2FAiEAyLpnIcA03qsXiI0qA2KNVA7Z3DDTYBSdbT%2BiY7X3b%2BQqiAQI5P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHGW%2FVEtm9kmH%2F5rpSrcA%2FeATq7V6YApbyF2%2BEUbI6zyUYwi8cpXQ3yQh9sNCaHuLVnVTx2wYzkz0RLbRwe7ot72BgiyVqJoQScirCKmmmcs%2FFe%2BbGYyGsfQu2Cp8p2oQPl8PpmsrW77K9Fw3QLeThf5c021t%2FT%2Fslw%2F2tqVwr0HO1lWbcqOox2FIQdLwmME%2FouiAExsAEywMr92pwcEUera1w87WzySrtbLwnOEI8FuoiibeZVJeWewzrH1cHAmS2LTgmKKNWpUi1JQRtYCP8qai5x4Nmp7GT1fsbwz0buRz3egIL5%2B4NeqXbtpeTuCqi%2BBoLccXtBubelCAnoS%2FFtnwlothvNsLG7PTONLqZH1SNZGwSkFlete2VIgFrVE70mBFXkd3FExjg8N2FbbV%2FbcXSclJTbiSGGMYRG3GZRatRq27k1tW31TE9wku6n8Tc3ybMiANzIwl%2BXBZI%2FpC55QrfLnTuZYrfz1I%2FblFJ6shP13gyr9rD5U%2FE5HmL91LO%2Fs%2BgFjreX4ET%2F2M%2FZFRRNMWtdWhCLQ3a3jFPthLRc7D7Eec4jt%2Fge67V8lXy%2FF4z1iqUNUXEUuJoUxzZpLDI3F2ueF5oh9JKD9lBgnWib282VpfEwob1A7q%2FIe%2FRlII5amie4TUDgkRgZ%2BMIS7%2B7wGOqUBqhuYdhs48TFNzDURkgYO9dK1IDr7H67HW620I2a0AGP1BB15TJIvsy%2FBq2P7vcY6TSEUIJ2fVrhS7YhpFPsi4BpHCkhRvs71PpWGZ55raU5T1W4lHICS7YW2HYuNBcRAcoCeWavcCriPdTHkKLKVA0yTmGsBH9vYjNyTb4GGvUt0%2B3PBTSN8r5WessfTPP2gU4sLNpHxdCFvM1Yq%2B7FB6c0h8e08&X-Amz-Signature=0e442cb71964504074c9ca2cc89a63400594733d8d7099a7a6acf2a5f1a78184&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UDWBIENZ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHnzKWpgd%2FYfU%2BTaP9Sd6fhlLahbIsMBU6LBdzqly0T%2FAiEAyLpnIcA03qsXiI0qA2KNVA7Z3DDTYBSdbT%2BiY7X3b%2BQqiAQI5P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHGW%2FVEtm9kmH%2F5rpSrcA%2FeATq7V6YApbyF2%2BEUbI6zyUYwi8cpXQ3yQh9sNCaHuLVnVTx2wYzkz0RLbRwe7ot72BgiyVqJoQScirCKmmmcs%2FFe%2BbGYyGsfQu2Cp8p2oQPl8PpmsrW77K9Fw3QLeThf5c021t%2FT%2Fslw%2F2tqVwr0HO1lWbcqOox2FIQdLwmME%2FouiAExsAEywMr92pwcEUera1w87WzySrtbLwnOEI8FuoiibeZVJeWewzrH1cHAmS2LTgmKKNWpUi1JQRtYCP8qai5x4Nmp7GT1fsbwz0buRz3egIL5%2B4NeqXbtpeTuCqi%2BBoLccXtBubelCAnoS%2FFtnwlothvNsLG7PTONLqZH1SNZGwSkFlete2VIgFrVE70mBFXkd3FExjg8N2FbbV%2FbcXSclJTbiSGGMYRG3GZRatRq27k1tW31TE9wku6n8Tc3ybMiANzIwl%2BXBZI%2FpC55QrfLnTuZYrfz1I%2FblFJ6shP13gyr9rD5U%2FE5HmL91LO%2Fs%2BgFjreX4ET%2F2M%2FZFRRNMWtdWhCLQ3a3jFPthLRc7D7Eec4jt%2Fge67V8lXy%2FF4z1iqUNUXEUuJoUxzZpLDI3F2ueF5oh9JKD9lBgnWib282VpfEwob1A7q%2FIe%2FRlII5amie4TUDgkRgZ%2BMIS7%2B7wGOqUBqhuYdhs48TFNzDURkgYO9dK1IDr7H67HW620I2a0AGP1BB15TJIvsy%2FBq2P7vcY6TSEUIJ2fVrhS7YhpFPsi4BpHCkhRvs71PpWGZ55raU5T1W4lHICS7YW2HYuNBcRAcoCeWavcCriPdTHkKLKVA0yTmGsBH9vYjNyTb4GGvUt0%2B3PBTSN8r5WessfTPP2gU4sLNpHxdCFvM1Yq%2B7FB6c0h8e08&X-Amz-Signature=5578551bed074c678ba3cab077d8b4c2267bfbd5cff2015f1b54659ef994be39&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UDWBIENZ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHnzKWpgd%2FYfU%2BTaP9Sd6fhlLahbIsMBU6LBdzqly0T%2FAiEAyLpnIcA03qsXiI0qA2KNVA7Z3DDTYBSdbT%2BiY7X3b%2BQqiAQI5P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHGW%2FVEtm9kmH%2F5rpSrcA%2FeATq7V6YApbyF2%2BEUbI6zyUYwi8cpXQ3yQh9sNCaHuLVnVTx2wYzkz0RLbRwe7ot72BgiyVqJoQScirCKmmmcs%2FFe%2BbGYyGsfQu2Cp8p2oQPl8PpmsrW77K9Fw3QLeThf5c021t%2FT%2Fslw%2F2tqVwr0HO1lWbcqOox2FIQdLwmME%2FouiAExsAEywMr92pwcEUera1w87WzySrtbLwnOEI8FuoiibeZVJeWewzrH1cHAmS2LTgmKKNWpUi1JQRtYCP8qai5x4Nmp7GT1fsbwz0buRz3egIL5%2B4NeqXbtpeTuCqi%2BBoLccXtBubelCAnoS%2FFtnwlothvNsLG7PTONLqZH1SNZGwSkFlete2VIgFrVE70mBFXkd3FExjg8N2FbbV%2FbcXSclJTbiSGGMYRG3GZRatRq27k1tW31TE9wku6n8Tc3ybMiANzIwl%2BXBZI%2FpC55QrfLnTuZYrfz1I%2FblFJ6shP13gyr9rD5U%2FE5HmL91LO%2Fs%2BgFjreX4ET%2F2M%2FZFRRNMWtdWhCLQ3a3jFPthLRc7D7Eec4jt%2Fge67V8lXy%2FF4z1iqUNUXEUuJoUxzZpLDI3F2ueF5oh9JKD9lBgnWib282VpfEwob1A7q%2FIe%2FRlII5amie4TUDgkRgZ%2BMIS7%2B7wGOqUBqhuYdhs48TFNzDURkgYO9dK1IDr7H67HW620I2a0AGP1BB15TJIvsy%2FBq2P7vcY6TSEUIJ2fVrhS7YhpFPsi4BpHCkhRvs71PpWGZ55raU5T1W4lHICS7YW2HYuNBcRAcoCeWavcCriPdTHkKLKVA0yTmGsBH9vYjNyTb4GGvUt0%2B3PBTSN8r5WessfTPP2gU4sLNpHxdCFvM1Yq%2B7FB6c0h8e08&X-Amz-Signature=536ba2b5e67d89fe00643871bee9e3c72b654f1787afe6535c19c2a4b896d629&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UDWBIENZ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHnzKWpgd%2FYfU%2BTaP9Sd6fhlLahbIsMBU6LBdzqly0T%2FAiEAyLpnIcA03qsXiI0qA2KNVA7Z3DDTYBSdbT%2BiY7X3b%2BQqiAQI5P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHGW%2FVEtm9kmH%2F5rpSrcA%2FeATq7V6YApbyF2%2BEUbI6zyUYwi8cpXQ3yQh9sNCaHuLVnVTx2wYzkz0RLbRwe7ot72BgiyVqJoQScirCKmmmcs%2FFe%2BbGYyGsfQu2Cp8p2oQPl8PpmsrW77K9Fw3QLeThf5c021t%2FT%2Fslw%2F2tqVwr0HO1lWbcqOox2FIQdLwmME%2FouiAExsAEywMr92pwcEUera1w87WzySrtbLwnOEI8FuoiibeZVJeWewzrH1cHAmS2LTgmKKNWpUi1JQRtYCP8qai5x4Nmp7GT1fsbwz0buRz3egIL5%2B4NeqXbtpeTuCqi%2BBoLccXtBubelCAnoS%2FFtnwlothvNsLG7PTONLqZH1SNZGwSkFlete2VIgFrVE70mBFXkd3FExjg8N2FbbV%2FbcXSclJTbiSGGMYRG3GZRatRq27k1tW31TE9wku6n8Tc3ybMiANzIwl%2BXBZI%2FpC55QrfLnTuZYrfz1I%2FblFJ6shP13gyr9rD5U%2FE5HmL91LO%2Fs%2BgFjreX4ET%2F2M%2FZFRRNMWtdWhCLQ3a3jFPthLRc7D7Eec4jt%2Fge67V8lXy%2FF4z1iqUNUXEUuJoUxzZpLDI3F2ueF5oh9JKD9lBgnWib282VpfEwob1A7q%2FIe%2FRlII5amie4TUDgkRgZ%2BMIS7%2B7wGOqUBqhuYdhs48TFNzDURkgYO9dK1IDr7H67HW620I2a0AGP1BB15TJIvsy%2FBq2P7vcY6TSEUIJ2fVrhS7YhpFPsi4BpHCkhRvs71PpWGZ55raU5T1W4lHICS7YW2HYuNBcRAcoCeWavcCriPdTHkKLKVA0yTmGsBH9vYjNyTb4GGvUt0%2B3PBTSN8r5WessfTPP2gU4sLNpHxdCFvM1Yq%2B7FB6c0h8e08&X-Amz-Signature=e08dc7c351441390ee11faef52f9a8bf749f2dbf43ca73b79dcc1949e2892335&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y664B6AG%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCFwK5m1tQ6rLKyJ4mm0Ncim5lL5Aa6p9sxPgolQSY7tAIhAKIEJPgHQZZi4pb%2Foe%2BJJUDxoj03e2p4qeWylVjNWFI2KogECOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzPB6WgSrlKHCzrJEQq3APvZvHW3%2FK%2FctrroCRZS8DXcTgrdOzkrxFs%2BJIVzpCYvOSqFY9QSL9rZSPmQl2emp88GY168jMvx8WcwGaJ8jMZNCXOjTNEb%2FEoEomWr%2Fk0LZuDWnf8D1nsgDloIlviVZMmoK2rIkWvVZmhxXWYIeAqvLrhzFXdbZRaR2D5RDJVsaPC%2FJpxWPE2MwMHVHytqL135PAwy5GsxdxsPuyR2SQCbPFmyIUbENo3a9lBX4eT8gcn1e4rCclk%2FHOnzqTqsvDkeKrAg5GWJ56%2BVriaixzWHov8beipRc1NA6aDhevCEspPGcfPOqMBD6Ipjm6Nmg20m1Ha80FbPzXnh3wdo%2FcBnnX%2BuJ9K%2FMeL2hrf4Vt8r55YVzG1NIsAeqc97G6QT61cDdwzoQyeeiCctR9f7nM%2FsQZqp%2BGypm7rdYypidOc7yaM%2BPXMSVyjMNh2idMTTAf7wP3FohAj8vVRaljPMJ6%2B6LJv3N1ps0tzPsoVu52I5QbxtNYlY%2FkaMw%2FojKwsQNHnN3IZSPK6EBdkCOGM7km%2F8OaYPlWThXOiscAv2O4mLkIg8Y8u4k5B0x7SdWo%2Fnf4rgfwgffW7jEFt46wQi9FJKMnA%2BONQFd4EKxQzG6F5%2FForkrRCeFoiPn8FSDCLu%2Fu8BjqkATEH5TR%2F28JL%2FB2ZsEXaP4JT2DXy%2B1W8SL9nMC5z%2FX2c9h1RvmEUUve9FTNAFOvhCqpQOFx6tXg57uL6FwAEwOnI8n474lijEZxrcT2EXTMptz266hsP8vp39BsAtiWm8mX27sX49zuvvWm3znpFGhy3bDaqcbCciL8dWaVsYEG2Um8O%2B2eg8xAC3W3J%2F%2B0YWE1yDdU5g3SwQHXU1bWqe%2F83ps95&X-Amz-Signature=bd811e358baf60e441d7a106efca952ef0ed122fb9a17b7a0d3ff49a4f97fb10&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y664B6AG%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCFwK5m1tQ6rLKyJ4mm0Ncim5lL5Aa6p9sxPgolQSY7tAIhAKIEJPgHQZZi4pb%2Foe%2BJJUDxoj03e2p4qeWylVjNWFI2KogECOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzPB6WgSrlKHCzrJEQq3APvZvHW3%2FK%2FctrroCRZS8DXcTgrdOzkrxFs%2BJIVzpCYvOSqFY9QSL9rZSPmQl2emp88GY168jMvx8WcwGaJ8jMZNCXOjTNEb%2FEoEomWr%2Fk0LZuDWnf8D1nsgDloIlviVZMmoK2rIkWvVZmhxXWYIeAqvLrhzFXdbZRaR2D5RDJVsaPC%2FJpxWPE2MwMHVHytqL135PAwy5GsxdxsPuyR2SQCbPFmyIUbENo3a9lBX4eT8gcn1e4rCclk%2FHOnzqTqsvDkeKrAg5GWJ56%2BVriaixzWHov8beipRc1NA6aDhevCEspPGcfPOqMBD6Ipjm6Nmg20m1Ha80FbPzXnh3wdo%2FcBnnX%2BuJ9K%2FMeL2hrf4Vt8r55YVzG1NIsAeqc97G6QT61cDdwzoQyeeiCctR9f7nM%2FsQZqp%2BGypm7rdYypidOc7yaM%2BPXMSVyjMNh2idMTTAf7wP3FohAj8vVRaljPMJ6%2B6LJv3N1ps0tzPsoVu52I5QbxtNYlY%2FkaMw%2FojKwsQNHnN3IZSPK6EBdkCOGM7km%2F8OaYPlWThXOiscAv2O4mLkIg8Y8u4k5B0x7SdWo%2Fnf4rgfwgffW7jEFt46wQi9FJKMnA%2BONQFd4EKxQzG6F5%2FForkrRCeFoiPn8FSDCLu%2Fu8BjqkATEH5TR%2F28JL%2FB2ZsEXaP4JT2DXy%2B1W8SL9nMC5z%2FX2c9h1RvmEUUve9FTNAFOvhCqpQOFx6tXg57uL6FwAEwOnI8n474lijEZxrcT2EXTMptz266hsP8vp39BsAtiWm8mX27sX49zuvvWm3znpFGhy3bDaqcbCciL8dWaVsYEG2Um8O%2B2eg8xAC3W3J%2F%2B0YWE1yDdU5g3SwQHXU1bWqe%2F83ps95&X-Amz-Signature=28cb7b0fd7dc51b3a7ff02923c65c9e9e15a6a48261387757313a47e6f48acc2&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
