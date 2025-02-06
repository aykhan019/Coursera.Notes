

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YXJZHHZA%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010938Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJGMEQCIDa%2BoxR07mfyNaYpdFIc%2F3A0C6EuG3zqhm%2BfXWedalcBAiBSmCDbV0WEUyWtiwOolznWk9BBnlJHoFFuLmGWDwNRYir%2FAwhREAAaDDYzNzQyMzE4MzgwNSIMlJAbSpoRuItj2MEEKtwDRLCwekycPiPATZyCyc1eYybIum9bn%2BvxFNOuH1Lt9SbopmaMZpI%2BtPhQw7DEXIkwYxjNc2NinmeiQ2Kn5K46t%2BjRCG1zpFiD0YfsYt43n8h3YBuG4dgal8dB6MEr5760%2Bf0a84vCzet19x8hzopZYa8S2GJMSehWtck237nwgtQrVD6%2B4pg9PnLm5tKXeqmbEpzJUlJ1b3rSk%2FK%2F1daEBldkyIVsWDw3bTxdsF9BfNa5j6hw4c6Hzuzbpl7UCWNW5jjOzNLZr7uskACAUaSJRKUt%2BFjeWYiSMxlCRWFV%2B%2BeClVacI1NMMfNs8o%2B5%2Fd%2FDwdSq0RKsTcE9IUOs1zVmZAUVRMScP3k5qz6qZr9JCfpI%2FaZBs0SLAaJeOdcColf%2F7oBrwmSEanK0posVnG75zOirGzefB%2Bhyi%2BQKGkEnFNrj3KHMS%2FvDRYlsBdGhy6CdhpWmmAyzB7f7wHA6te0occvCxDZFuROmr5pDysSiyThP5GPvAApVQy12dCXslm9MD56ys2KNAg1q9vPzqq70jXUOsv8fI%2BoM8GbYQG5LOk8LOf0pVmUDUf9EHUONHV3oEhzdJrXJvqE9NYwh5aDhNj5VVMJm4RApuIHvbxiS1h7PcBZn7pgLKyIXxJ8wkeuPvQY6pgFkA2cy0Ty9gigeLR%2BaibC9KotQtkwPMLFJcPJZyNvQY8%2F1yNymPvJNoKG%2FFpAP%2BtckKLgeaDxkeGvUPUhTeB5rBrbdAQ4A%2FAGPwNH0DOrlAyHTR0qASZWuwet3OuFocgVEr3Z5DXsmFJ%2Bj%2BhJSjaYD%2Fb1U98G1RUUSpIGbYtwWkFcS8LW74dXeXZc8rUZaTLLg76xOi1xD1uBHLaqo66lxDo3gODcU&X-Amz-Signature=52468942fc1196c68f3ebc71fa2235f873b4fc4e4e30c3bb350eb2e796743ebc&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YXJZHHZA%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010938Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJGMEQCIDa%2BoxR07mfyNaYpdFIc%2F3A0C6EuG3zqhm%2BfXWedalcBAiBSmCDbV0WEUyWtiwOolznWk9BBnlJHoFFuLmGWDwNRYir%2FAwhREAAaDDYzNzQyMzE4MzgwNSIMlJAbSpoRuItj2MEEKtwDRLCwekycPiPATZyCyc1eYybIum9bn%2BvxFNOuH1Lt9SbopmaMZpI%2BtPhQw7DEXIkwYxjNc2NinmeiQ2Kn5K46t%2BjRCG1zpFiD0YfsYt43n8h3YBuG4dgal8dB6MEr5760%2Bf0a84vCzet19x8hzopZYa8S2GJMSehWtck237nwgtQrVD6%2B4pg9PnLm5tKXeqmbEpzJUlJ1b3rSk%2FK%2F1daEBldkyIVsWDw3bTxdsF9BfNa5j6hw4c6Hzuzbpl7UCWNW5jjOzNLZr7uskACAUaSJRKUt%2BFjeWYiSMxlCRWFV%2B%2BeClVacI1NMMfNs8o%2B5%2Fd%2FDwdSq0RKsTcE9IUOs1zVmZAUVRMScP3k5qz6qZr9JCfpI%2FaZBs0SLAaJeOdcColf%2F7oBrwmSEanK0posVnG75zOirGzefB%2Bhyi%2BQKGkEnFNrj3KHMS%2FvDRYlsBdGhy6CdhpWmmAyzB7f7wHA6te0occvCxDZFuROmr5pDysSiyThP5GPvAApVQy12dCXslm9MD56ys2KNAg1q9vPzqq70jXUOsv8fI%2BoM8GbYQG5LOk8LOf0pVmUDUf9EHUONHV3oEhzdJrXJvqE9NYwh5aDhNj5VVMJm4RApuIHvbxiS1h7PcBZn7pgLKyIXxJ8wkeuPvQY6pgFkA2cy0Ty9gigeLR%2BaibC9KotQtkwPMLFJcPJZyNvQY8%2F1yNymPvJNoKG%2FFpAP%2BtckKLgeaDxkeGvUPUhTeB5rBrbdAQ4A%2FAGPwNH0DOrlAyHTR0qASZWuwet3OuFocgVEr3Z5DXsmFJ%2Bj%2BhJSjaYD%2Fb1U98G1RUUSpIGbYtwWkFcS8LW74dXeXZc8rUZaTLLg76xOi1xD1uBHLaqo66lxDo3gODcU&X-Amz-Signature=ce1316aaae002e374ebc6cfa00ac0a11d67c4670b82da1977f65abbb0f51a740&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YXJZHHZA%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010938Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJGMEQCIDa%2BoxR07mfyNaYpdFIc%2F3A0C6EuG3zqhm%2BfXWedalcBAiBSmCDbV0WEUyWtiwOolznWk9BBnlJHoFFuLmGWDwNRYir%2FAwhREAAaDDYzNzQyMzE4MzgwNSIMlJAbSpoRuItj2MEEKtwDRLCwekycPiPATZyCyc1eYybIum9bn%2BvxFNOuH1Lt9SbopmaMZpI%2BtPhQw7DEXIkwYxjNc2NinmeiQ2Kn5K46t%2BjRCG1zpFiD0YfsYt43n8h3YBuG4dgal8dB6MEr5760%2Bf0a84vCzet19x8hzopZYa8S2GJMSehWtck237nwgtQrVD6%2B4pg9PnLm5tKXeqmbEpzJUlJ1b3rSk%2FK%2F1daEBldkyIVsWDw3bTxdsF9BfNa5j6hw4c6Hzuzbpl7UCWNW5jjOzNLZr7uskACAUaSJRKUt%2BFjeWYiSMxlCRWFV%2B%2BeClVacI1NMMfNs8o%2B5%2Fd%2FDwdSq0RKsTcE9IUOs1zVmZAUVRMScP3k5qz6qZr9JCfpI%2FaZBs0SLAaJeOdcColf%2F7oBrwmSEanK0posVnG75zOirGzefB%2Bhyi%2BQKGkEnFNrj3KHMS%2FvDRYlsBdGhy6CdhpWmmAyzB7f7wHA6te0occvCxDZFuROmr5pDysSiyThP5GPvAApVQy12dCXslm9MD56ys2KNAg1q9vPzqq70jXUOsv8fI%2BoM8GbYQG5LOk8LOf0pVmUDUf9EHUONHV3oEhzdJrXJvqE9NYwh5aDhNj5VVMJm4RApuIHvbxiS1h7PcBZn7pgLKyIXxJ8wkeuPvQY6pgFkA2cy0Ty9gigeLR%2BaibC9KotQtkwPMLFJcPJZyNvQY8%2F1yNymPvJNoKG%2FFpAP%2BtckKLgeaDxkeGvUPUhTeB5rBrbdAQ4A%2FAGPwNH0DOrlAyHTR0qASZWuwet3OuFocgVEr3Z5DXsmFJ%2Bj%2BhJSjaYD%2Fb1U98G1RUUSpIGbYtwWkFcS8LW74dXeXZc8rUZaTLLg76xOi1xD1uBHLaqo66lxDo3gODcU&X-Amz-Signature=6a6b58301685ce7964c2fba42b96203ddf306dc1d7c2ca4e1c3c36d509cc26af&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YXJZHHZA%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJGMEQCIDa%2BoxR07mfyNaYpdFIc%2F3A0C6EuG3zqhm%2BfXWedalcBAiBSmCDbV0WEUyWtiwOolznWk9BBnlJHoFFuLmGWDwNRYir%2FAwhREAAaDDYzNzQyMzE4MzgwNSIMlJAbSpoRuItj2MEEKtwDRLCwekycPiPATZyCyc1eYybIum9bn%2BvxFNOuH1Lt9SbopmaMZpI%2BtPhQw7DEXIkwYxjNc2NinmeiQ2Kn5K46t%2BjRCG1zpFiD0YfsYt43n8h3YBuG4dgal8dB6MEr5760%2Bf0a84vCzet19x8hzopZYa8S2GJMSehWtck237nwgtQrVD6%2B4pg9PnLm5tKXeqmbEpzJUlJ1b3rSk%2FK%2F1daEBldkyIVsWDw3bTxdsF9BfNa5j6hw4c6Hzuzbpl7UCWNW5jjOzNLZr7uskACAUaSJRKUt%2BFjeWYiSMxlCRWFV%2B%2BeClVacI1NMMfNs8o%2B5%2Fd%2FDwdSq0RKsTcE9IUOs1zVmZAUVRMScP3k5qz6qZr9JCfpI%2FaZBs0SLAaJeOdcColf%2F7oBrwmSEanK0posVnG75zOirGzefB%2Bhyi%2BQKGkEnFNrj3KHMS%2FvDRYlsBdGhy6CdhpWmmAyzB7f7wHA6te0occvCxDZFuROmr5pDysSiyThP5GPvAApVQy12dCXslm9MD56ys2KNAg1q9vPzqq70jXUOsv8fI%2BoM8GbYQG5LOk8LOf0pVmUDUf9EHUONHV3oEhzdJrXJvqE9NYwh5aDhNj5VVMJm4RApuIHvbxiS1h7PcBZn7pgLKyIXxJ8wkeuPvQY6pgFkA2cy0Ty9gigeLR%2BaibC9KotQtkwPMLFJcPJZyNvQY8%2F1yNymPvJNoKG%2FFpAP%2BtckKLgeaDxkeGvUPUhTeB5rBrbdAQ4A%2FAGPwNH0DOrlAyHTR0qASZWuwet3OuFocgVEr3Z5DXsmFJ%2Bj%2BhJSjaYD%2Fb1U98G1RUUSpIGbYtwWkFcS8LW74dXeXZc8rUZaTLLg76xOi1xD1uBHLaqo66lxDo3gODcU&X-Amz-Signature=1fb31bf9eff9e3ac3bf97fcb7a9c6081633aef9f061e1fabbb152021f91b43b5&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YXJZHHZA%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJGMEQCIDa%2BoxR07mfyNaYpdFIc%2F3A0C6EuG3zqhm%2BfXWedalcBAiBSmCDbV0WEUyWtiwOolznWk9BBnlJHoFFuLmGWDwNRYir%2FAwhREAAaDDYzNzQyMzE4MzgwNSIMlJAbSpoRuItj2MEEKtwDRLCwekycPiPATZyCyc1eYybIum9bn%2BvxFNOuH1Lt9SbopmaMZpI%2BtPhQw7DEXIkwYxjNc2NinmeiQ2Kn5K46t%2BjRCG1zpFiD0YfsYt43n8h3YBuG4dgal8dB6MEr5760%2Bf0a84vCzet19x8hzopZYa8S2GJMSehWtck237nwgtQrVD6%2B4pg9PnLm5tKXeqmbEpzJUlJ1b3rSk%2FK%2F1daEBldkyIVsWDw3bTxdsF9BfNa5j6hw4c6Hzuzbpl7UCWNW5jjOzNLZr7uskACAUaSJRKUt%2BFjeWYiSMxlCRWFV%2B%2BeClVacI1NMMfNs8o%2B5%2Fd%2FDwdSq0RKsTcE9IUOs1zVmZAUVRMScP3k5qz6qZr9JCfpI%2FaZBs0SLAaJeOdcColf%2F7oBrwmSEanK0posVnG75zOirGzefB%2Bhyi%2BQKGkEnFNrj3KHMS%2FvDRYlsBdGhy6CdhpWmmAyzB7f7wHA6te0occvCxDZFuROmr5pDysSiyThP5GPvAApVQy12dCXslm9MD56ys2KNAg1q9vPzqq70jXUOsv8fI%2BoM8GbYQG5LOk8LOf0pVmUDUf9EHUONHV3oEhzdJrXJvqE9NYwh5aDhNj5VVMJm4RApuIHvbxiS1h7PcBZn7pgLKyIXxJ8wkeuPvQY6pgFkA2cy0Ty9gigeLR%2BaibC9KotQtkwPMLFJcPJZyNvQY8%2F1yNymPvJNoKG%2FFpAP%2BtckKLgeaDxkeGvUPUhTeB5rBrbdAQ4A%2FAGPwNH0DOrlAyHTR0qASZWuwet3OuFocgVEr3Z5DXsmFJ%2Bj%2BhJSjaYD%2Fb1U98G1RUUSpIGbYtwWkFcS8LW74dXeXZc8rUZaTLLg76xOi1xD1uBHLaqo66lxDo3gODcU&X-Amz-Signature=3a453932917f56b413984f6e8f7c8bb1b7545e256f744a7d8ed1f2c6aa5366da&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YXJZHHZA%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJGMEQCIDa%2BoxR07mfyNaYpdFIc%2F3A0C6EuG3zqhm%2BfXWedalcBAiBSmCDbV0WEUyWtiwOolznWk9BBnlJHoFFuLmGWDwNRYir%2FAwhREAAaDDYzNzQyMzE4MzgwNSIMlJAbSpoRuItj2MEEKtwDRLCwekycPiPATZyCyc1eYybIum9bn%2BvxFNOuH1Lt9SbopmaMZpI%2BtPhQw7DEXIkwYxjNc2NinmeiQ2Kn5K46t%2BjRCG1zpFiD0YfsYt43n8h3YBuG4dgal8dB6MEr5760%2Bf0a84vCzet19x8hzopZYa8S2GJMSehWtck237nwgtQrVD6%2B4pg9PnLm5tKXeqmbEpzJUlJ1b3rSk%2FK%2F1daEBldkyIVsWDw3bTxdsF9BfNa5j6hw4c6Hzuzbpl7UCWNW5jjOzNLZr7uskACAUaSJRKUt%2BFjeWYiSMxlCRWFV%2B%2BeClVacI1NMMfNs8o%2B5%2Fd%2FDwdSq0RKsTcE9IUOs1zVmZAUVRMScP3k5qz6qZr9JCfpI%2FaZBs0SLAaJeOdcColf%2F7oBrwmSEanK0posVnG75zOirGzefB%2Bhyi%2BQKGkEnFNrj3KHMS%2FvDRYlsBdGhy6CdhpWmmAyzB7f7wHA6te0occvCxDZFuROmr5pDysSiyThP5GPvAApVQy12dCXslm9MD56ys2KNAg1q9vPzqq70jXUOsv8fI%2BoM8GbYQG5LOk8LOf0pVmUDUf9EHUONHV3oEhzdJrXJvqE9NYwh5aDhNj5VVMJm4RApuIHvbxiS1h7PcBZn7pgLKyIXxJ8wkeuPvQY6pgFkA2cy0Ty9gigeLR%2BaibC9KotQtkwPMLFJcPJZyNvQY8%2F1yNymPvJNoKG%2FFpAP%2BtckKLgeaDxkeGvUPUhTeB5rBrbdAQ4A%2FAGPwNH0DOrlAyHTR0qASZWuwet3OuFocgVEr3Z5DXsmFJ%2Bj%2BhJSjaYD%2Fb1U98G1RUUSpIGbYtwWkFcS8LW74dXeXZc8rUZaTLLg76xOi1xD1uBHLaqo66lxDo3gODcU&X-Amz-Signature=3cb0c16495dec6355b7d0d2107102b19f51e33107a96e0b7f6e6943fd50efc35&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YXJZHHZA%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010938Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJGMEQCIDa%2BoxR07mfyNaYpdFIc%2F3A0C6EuG3zqhm%2BfXWedalcBAiBSmCDbV0WEUyWtiwOolznWk9BBnlJHoFFuLmGWDwNRYir%2FAwhREAAaDDYzNzQyMzE4MzgwNSIMlJAbSpoRuItj2MEEKtwDRLCwekycPiPATZyCyc1eYybIum9bn%2BvxFNOuH1Lt9SbopmaMZpI%2BtPhQw7DEXIkwYxjNc2NinmeiQ2Kn5K46t%2BjRCG1zpFiD0YfsYt43n8h3YBuG4dgal8dB6MEr5760%2Bf0a84vCzet19x8hzopZYa8S2GJMSehWtck237nwgtQrVD6%2B4pg9PnLm5tKXeqmbEpzJUlJ1b3rSk%2FK%2F1daEBldkyIVsWDw3bTxdsF9BfNa5j6hw4c6Hzuzbpl7UCWNW5jjOzNLZr7uskACAUaSJRKUt%2BFjeWYiSMxlCRWFV%2B%2BeClVacI1NMMfNs8o%2B5%2Fd%2FDwdSq0RKsTcE9IUOs1zVmZAUVRMScP3k5qz6qZr9JCfpI%2FaZBs0SLAaJeOdcColf%2F7oBrwmSEanK0posVnG75zOirGzefB%2Bhyi%2BQKGkEnFNrj3KHMS%2FvDRYlsBdGhy6CdhpWmmAyzB7f7wHA6te0occvCxDZFuROmr5pDysSiyThP5GPvAApVQy12dCXslm9MD56ys2KNAg1q9vPzqq70jXUOsv8fI%2BoM8GbYQG5LOk8LOf0pVmUDUf9EHUONHV3oEhzdJrXJvqE9NYwh5aDhNj5VVMJm4RApuIHvbxiS1h7PcBZn7pgLKyIXxJ8wkeuPvQY6pgFkA2cy0Ty9gigeLR%2BaibC9KotQtkwPMLFJcPJZyNvQY8%2F1yNymPvJNoKG%2FFpAP%2BtckKLgeaDxkeGvUPUhTeB5rBrbdAQ4A%2FAGPwNH0DOrlAyHTR0qASZWuwet3OuFocgVEr3Z5DXsmFJ%2Bj%2BhJSjaYD%2Fb1U98G1RUUSpIGbYtwWkFcS8LW74dXeXZc8rUZaTLLg76xOi1xD1uBHLaqo66lxDo3gODcU&X-Amz-Signature=d23da1788c464f3e3da9baa14f81aa733e3b597205b16fc984ff0f76c664dcc8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YXJZHHZA%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010938Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJGMEQCIDa%2BoxR07mfyNaYpdFIc%2F3A0C6EuG3zqhm%2BfXWedalcBAiBSmCDbV0WEUyWtiwOolznWk9BBnlJHoFFuLmGWDwNRYir%2FAwhREAAaDDYzNzQyMzE4MzgwNSIMlJAbSpoRuItj2MEEKtwDRLCwekycPiPATZyCyc1eYybIum9bn%2BvxFNOuH1Lt9SbopmaMZpI%2BtPhQw7DEXIkwYxjNc2NinmeiQ2Kn5K46t%2BjRCG1zpFiD0YfsYt43n8h3YBuG4dgal8dB6MEr5760%2Bf0a84vCzet19x8hzopZYa8S2GJMSehWtck237nwgtQrVD6%2B4pg9PnLm5tKXeqmbEpzJUlJ1b3rSk%2FK%2F1daEBldkyIVsWDw3bTxdsF9BfNa5j6hw4c6Hzuzbpl7UCWNW5jjOzNLZr7uskACAUaSJRKUt%2BFjeWYiSMxlCRWFV%2B%2BeClVacI1NMMfNs8o%2B5%2Fd%2FDwdSq0RKsTcE9IUOs1zVmZAUVRMScP3k5qz6qZr9JCfpI%2FaZBs0SLAaJeOdcColf%2F7oBrwmSEanK0posVnG75zOirGzefB%2Bhyi%2BQKGkEnFNrj3KHMS%2FvDRYlsBdGhy6CdhpWmmAyzB7f7wHA6te0occvCxDZFuROmr5pDysSiyThP5GPvAApVQy12dCXslm9MD56ys2KNAg1q9vPzqq70jXUOsv8fI%2BoM8GbYQG5LOk8LOf0pVmUDUf9EHUONHV3oEhzdJrXJvqE9NYwh5aDhNj5VVMJm4RApuIHvbxiS1h7PcBZn7pgLKyIXxJ8wkeuPvQY6pgFkA2cy0Ty9gigeLR%2BaibC9KotQtkwPMLFJcPJZyNvQY8%2F1yNymPvJNoKG%2FFpAP%2BtckKLgeaDxkeGvUPUhTeB5rBrbdAQ4A%2FAGPwNH0DOrlAyHTR0qASZWuwet3OuFocgVEr3Z5DXsmFJ%2Bj%2BhJSjaYD%2Fb1U98G1RUUSpIGbYtwWkFcS8LW74dXeXZc8rUZaTLLg76xOi1xD1uBHLaqo66lxDo3gODcU&X-Amz-Signature=9aa75a01a7faad8410b2746467a494c4bbc4b649617435ada2b66ebb5ab9cc04&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YXJZHHZA%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010938Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJGMEQCIDa%2BoxR07mfyNaYpdFIc%2F3A0C6EuG3zqhm%2BfXWedalcBAiBSmCDbV0WEUyWtiwOolznWk9BBnlJHoFFuLmGWDwNRYir%2FAwhREAAaDDYzNzQyMzE4MzgwNSIMlJAbSpoRuItj2MEEKtwDRLCwekycPiPATZyCyc1eYybIum9bn%2BvxFNOuH1Lt9SbopmaMZpI%2BtPhQw7DEXIkwYxjNc2NinmeiQ2Kn5K46t%2BjRCG1zpFiD0YfsYt43n8h3YBuG4dgal8dB6MEr5760%2Bf0a84vCzet19x8hzopZYa8S2GJMSehWtck237nwgtQrVD6%2B4pg9PnLm5tKXeqmbEpzJUlJ1b3rSk%2FK%2F1daEBldkyIVsWDw3bTxdsF9BfNa5j6hw4c6Hzuzbpl7UCWNW5jjOzNLZr7uskACAUaSJRKUt%2BFjeWYiSMxlCRWFV%2B%2BeClVacI1NMMfNs8o%2B5%2Fd%2FDwdSq0RKsTcE9IUOs1zVmZAUVRMScP3k5qz6qZr9JCfpI%2FaZBs0SLAaJeOdcColf%2F7oBrwmSEanK0posVnG75zOirGzefB%2Bhyi%2BQKGkEnFNrj3KHMS%2FvDRYlsBdGhy6CdhpWmmAyzB7f7wHA6te0occvCxDZFuROmr5pDysSiyThP5GPvAApVQy12dCXslm9MD56ys2KNAg1q9vPzqq70jXUOsv8fI%2BoM8GbYQG5LOk8LOf0pVmUDUf9EHUONHV3oEhzdJrXJvqE9NYwh5aDhNj5VVMJm4RApuIHvbxiS1h7PcBZn7pgLKyIXxJ8wkeuPvQY6pgFkA2cy0Ty9gigeLR%2BaibC9KotQtkwPMLFJcPJZyNvQY8%2F1yNymPvJNoKG%2FFpAP%2BtckKLgeaDxkeGvUPUhTeB5rBrbdAQ4A%2FAGPwNH0DOrlAyHTR0qASZWuwet3OuFocgVEr3Z5DXsmFJ%2Bj%2BhJSjaYD%2Fb1U98G1RUUSpIGbYtwWkFcS8LW74dXeXZc8rUZaTLLg76xOi1xD1uBHLaqo66lxDo3gODcU&X-Amz-Signature=3049cad15ab41ad61b306fb0af94524de811fc9ede515eb2f9794d748f58cc8c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XLZOGFZR%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010938Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIQD9Zyrp5TgZenOYNJHnQaUBfLYyw7lYF5%2FPEzMmMjL4%2FgIgPhb2sU4W113TCLMjMKNrlzrXy6gX%2FM1NiMVcO3MfcH4q%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDB8bnJi%2BSK8zR9%2BGcCrcA6yLsMNgt%2FHLamJucG4e6R0EDOcPQbwM%2FIj%2F8evNiF7qqduMj0rLcvT0eL7usr5mn0rh5lEYbNqe1hghIZ1AbA1khHAH2ah4UYtfZYD7SZC8o6U1%2FMseE5KAQD6paa1xGKjjA4BD6XqrZy9tKSmyRO0RSJdDbpdTU5IeLvqEwvmaxoFHUswjnLplKEJP3I1JEmijqlablbEGmBO6NhuCBrBJIM57YMBiWxMaB1UZk49b71GGyTpEHi%2BRmYtJkoyRX1XpCRS0hklS2Wda3WMDSen3WV8P%2BdGyM86mEfRfPWXEEOtsk%2BNYgcNqRsModR4SQS62EfFw6L1PdPeZKSY5BDfp0mPguGQQDdhR%2BPYYUO0vd4K2R4eLLKQIFdd6x73Jo1Isnk74nyBRxLjPG0FIf574QqPtyqFaKJQ0uxrF1VrZkh2YtIAB9KH4BIprzWQsVSJ44AXk1%2FapEy%2Fl5Vz%2FpvjDobnPyNuF5MyhvtZ17PV0nKFV%2F%2BBg50ShcSNHwVCmfJ4c%2BtIDybH8I4YC7fKQ%2B%2BjyhOAm9KTOLWtiFnVrlmdIO1NR2ZiYOv2Ryq7lN2KaIVFkRxT0vZsqY7Sy54czLN5sI51yDwAMl3Js4oR3U8OMbOYa8JpeaQT2WCihMIPrj70GOqUB83rzFbHc9KwBH2lkKOSik2SYxR1RiB5H3TXtee9eLMIkOz6Yw69UmDN7ZwdVQJZZKtLnQk4fROPqLFwRYt%2Bir2JLliRj33DfFqc1Mfz4%2BmoQuYyRaC2X38JF%2F47K6bsgiWF%2BHZF3KkPN7KkpqmOkm78BipgSNA29C1S6XHyV0TkNmdpPBHGRs0vuwDzw3fZbzeGQJQpuRR%2Bgvlnvr4XrttOJ4PQN&X-Amz-Signature=985200528881a9a3795eaa45ef6679bf02aa984765f4fded67a54a9a55da6128&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XLZOGFZR%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010938Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIQD9Zyrp5TgZenOYNJHnQaUBfLYyw7lYF5%2FPEzMmMjL4%2FgIgPhb2sU4W113TCLMjMKNrlzrXy6gX%2FM1NiMVcO3MfcH4q%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDB8bnJi%2BSK8zR9%2BGcCrcA6yLsMNgt%2FHLamJucG4e6R0EDOcPQbwM%2FIj%2F8evNiF7qqduMj0rLcvT0eL7usr5mn0rh5lEYbNqe1hghIZ1AbA1khHAH2ah4UYtfZYD7SZC8o6U1%2FMseE5KAQD6paa1xGKjjA4BD6XqrZy9tKSmyRO0RSJdDbpdTU5IeLvqEwvmaxoFHUswjnLplKEJP3I1JEmijqlablbEGmBO6NhuCBrBJIM57YMBiWxMaB1UZk49b71GGyTpEHi%2BRmYtJkoyRX1XpCRS0hklS2Wda3WMDSen3WV8P%2BdGyM86mEfRfPWXEEOtsk%2BNYgcNqRsModR4SQS62EfFw6L1PdPeZKSY5BDfp0mPguGQQDdhR%2BPYYUO0vd4K2R4eLLKQIFdd6x73Jo1Isnk74nyBRxLjPG0FIf574QqPtyqFaKJQ0uxrF1VrZkh2YtIAB9KH4BIprzWQsVSJ44AXk1%2FapEy%2Fl5Vz%2FpvjDobnPyNuF5MyhvtZ17PV0nKFV%2F%2BBg50ShcSNHwVCmfJ4c%2BtIDybH8I4YC7fKQ%2B%2BjyhOAm9KTOLWtiFnVrlmdIO1NR2ZiYOv2Ryq7lN2KaIVFkRxT0vZsqY7Sy54czLN5sI51yDwAMl3Js4oR3U8OMbOYa8JpeaQT2WCihMIPrj70GOqUB83rzFbHc9KwBH2lkKOSik2SYxR1RiB5H3TXtee9eLMIkOz6Yw69UmDN7ZwdVQJZZKtLnQk4fROPqLFwRYt%2Bir2JLliRj33DfFqc1Mfz4%2BmoQuYyRaC2X38JF%2F47K6bsgiWF%2BHZF3KkPN7KkpqmOkm78BipgSNA29C1S6XHyV0TkNmdpPBHGRs0vuwDzw3fZbzeGQJQpuRR%2Bgvlnvr4XrttOJ4PQN&X-Amz-Signature=724bcb34e5f848b9919bce9f9ce7e48f392073672af16301cf844a275581d9c8&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
