

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VQ7YB6Q%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T191057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCUjcWWb5eu4uY%2FXM%2BAf5sKda5DB%2FyfpAycnmUjpTh3WwIhAKsnFJ8stw6b5lwCszbl13Ic%2F2UJwlZP%2Fe36EMPyU2XpKogECJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwEFB%2FO0P8chGXDEFIq3AMp9h2bpN3wOqXYWDiLBn6qyMhV7rrwxKZX44AS2sa7FUVPDD0sEK8a9VCma%2BBkEX1OFv2ApiArdz%2BGtPeKMIraiXUbNpkAowPnqkdxYj2SyIAD9iH%2Bjqv%2FXVLeoa0fnvoe8TTd%2BDklvgzC14xXzwMAIDPVocphi9j3w6ZqKZc9YGTMMwuAK7BsiWq0fFaEho0GxX9rVq4imhqllAfttVUSNjtNW5rT2xyfCaFz1qn0exVxEiVoGCqBBQsPM3G2vLsL3w43fECJHHpgZjpMmJ5IPyKWn3E2HET3aZEoZ%2FR7TYjJ1f%2BDhuLXixqYRyfLJL3%2Bhz8POKIUM7l3a4aeImyhrJutjpl9DSJ7kf1MKb5dgFhTkRlh7crRurATieaGh%2Baj06btb7%2BSf4s9WoYOsjAclkDgHLfSYEUQqcrqBJn0WhK7lMw6J0Zf6tc5xgKf4qbQte02jZ9mCsEEblTNqrGvbwrmglIMUJ69IQiTM%2BkBlHgy7Ov8pm5yT0VSy81ZS6C8t6F6pFp8gAFwRLfDo592bz24uzb5O3ZT00ze%2F%2BYqxSu%2F7yzRP7pvBKu8Uy6xqkp0OD9sN9GGI9S7zdKi4qTBU08OSgm4VPR59YycBuUxRCcvirnKIPb1H2vHzTCP9em8BjqkAdpcgDmyIj02Tdimwio3ybYJnZMCxGbiN9OkuWXAetUEuKFY1%2BMsBVWiesd5lqUt9yvOeDCTIR73S6XPNv3K5TpmoEHy3RNIQFMInj8LsD3j5ojpxfNV5bx2OXdC54IFFIfeKdS7A6O0tgFEIAuDH7uh56PiH%2BDncVDcpQj7EuJR4OeyuenAhs4Cpssou8%2BJR9K90jYH3dOTsezo3YJklH1dpzG6&X-Amz-Signature=755b6d42db806f87827fa1f7b2f2fdf856d90df2de85629a11262f437624c82c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VQ7YB6Q%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T191057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCUjcWWb5eu4uY%2FXM%2BAf5sKda5DB%2FyfpAycnmUjpTh3WwIhAKsnFJ8stw6b5lwCszbl13Ic%2F2UJwlZP%2Fe36EMPyU2XpKogECJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwEFB%2FO0P8chGXDEFIq3AMp9h2bpN3wOqXYWDiLBn6qyMhV7rrwxKZX44AS2sa7FUVPDD0sEK8a9VCma%2BBkEX1OFv2ApiArdz%2BGtPeKMIraiXUbNpkAowPnqkdxYj2SyIAD9iH%2Bjqv%2FXVLeoa0fnvoe8TTd%2BDklvgzC14xXzwMAIDPVocphi9j3w6ZqKZc9YGTMMwuAK7BsiWq0fFaEho0GxX9rVq4imhqllAfttVUSNjtNW5rT2xyfCaFz1qn0exVxEiVoGCqBBQsPM3G2vLsL3w43fECJHHpgZjpMmJ5IPyKWn3E2HET3aZEoZ%2FR7TYjJ1f%2BDhuLXixqYRyfLJL3%2Bhz8POKIUM7l3a4aeImyhrJutjpl9DSJ7kf1MKb5dgFhTkRlh7crRurATieaGh%2Baj06btb7%2BSf4s9WoYOsjAclkDgHLfSYEUQqcrqBJn0WhK7lMw6J0Zf6tc5xgKf4qbQte02jZ9mCsEEblTNqrGvbwrmglIMUJ69IQiTM%2BkBlHgy7Ov8pm5yT0VSy81ZS6C8t6F6pFp8gAFwRLfDo592bz24uzb5O3ZT00ze%2F%2BYqxSu%2F7yzRP7pvBKu8Uy6xqkp0OD9sN9GGI9S7zdKi4qTBU08OSgm4VPR59YycBuUxRCcvirnKIPb1H2vHzTCP9em8BjqkAdpcgDmyIj02Tdimwio3ybYJnZMCxGbiN9OkuWXAetUEuKFY1%2BMsBVWiesd5lqUt9yvOeDCTIR73S6XPNv3K5TpmoEHy3RNIQFMInj8LsD3j5ojpxfNV5bx2OXdC54IFFIfeKdS7A6O0tgFEIAuDH7uh56PiH%2BDncVDcpQj7EuJR4OeyuenAhs4Cpssou8%2BJR9K90jYH3dOTsezo3YJklH1dpzG6&X-Amz-Signature=ac081349201c140f28176fa2ae3c677b67a35cede2fe95236c258a58bb616d12&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VQ7YB6Q%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T191057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCUjcWWb5eu4uY%2FXM%2BAf5sKda5DB%2FyfpAycnmUjpTh3WwIhAKsnFJ8stw6b5lwCszbl13Ic%2F2UJwlZP%2Fe36EMPyU2XpKogECJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwEFB%2FO0P8chGXDEFIq3AMp9h2bpN3wOqXYWDiLBn6qyMhV7rrwxKZX44AS2sa7FUVPDD0sEK8a9VCma%2BBkEX1OFv2ApiArdz%2BGtPeKMIraiXUbNpkAowPnqkdxYj2SyIAD9iH%2Bjqv%2FXVLeoa0fnvoe8TTd%2BDklvgzC14xXzwMAIDPVocphi9j3w6ZqKZc9YGTMMwuAK7BsiWq0fFaEho0GxX9rVq4imhqllAfttVUSNjtNW5rT2xyfCaFz1qn0exVxEiVoGCqBBQsPM3G2vLsL3w43fECJHHpgZjpMmJ5IPyKWn3E2HET3aZEoZ%2FR7TYjJ1f%2BDhuLXixqYRyfLJL3%2Bhz8POKIUM7l3a4aeImyhrJutjpl9DSJ7kf1MKb5dgFhTkRlh7crRurATieaGh%2Baj06btb7%2BSf4s9WoYOsjAclkDgHLfSYEUQqcrqBJn0WhK7lMw6J0Zf6tc5xgKf4qbQte02jZ9mCsEEblTNqrGvbwrmglIMUJ69IQiTM%2BkBlHgy7Ov8pm5yT0VSy81ZS6C8t6F6pFp8gAFwRLfDo592bz24uzb5O3ZT00ze%2F%2BYqxSu%2F7yzRP7pvBKu8Uy6xqkp0OD9sN9GGI9S7zdKi4qTBU08OSgm4VPR59YycBuUxRCcvirnKIPb1H2vHzTCP9em8BjqkAdpcgDmyIj02Tdimwio3ybYJnZMCxGbiN9OkuWXAetUEuKFY1%2BMsBVWiesd5lqUt9yvOeDCTIR73S6XPNv3K5TpmoEHy3RNIQFMInj8LsD3j5ojpxfNV5bx2OXdC54IFFIfeKdS7A6O0tgFEIAuDH7uh56PiH%2BDncVDcpQj7EuJR4OeyuenAhs4Cpssou8%2BJR9K90jYH3dOTsezo3YJklH1dpzG6&X-Amz-Signature=0fadf9880d897bb16012f06217961b3b2f0ccfec7178f3aeeb5ba8583d42f469&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VQ7YB6Q%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T191057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCUjcWWb5eu4uY%2FXM%2BAf5sKda5DB%2FyfpAycnmUjpTh3WwIhAKsnFJ8stw6b5lwCszbl13Ic%2F2UJwlZP%2Fe36EMPyU2XpKogECJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwEFB%2FO0P8chGXDEFIq3AMp9h2bpN3wOqXYWDiLBn6qyMhV7rrwxKZX44AS2sa7FUVPDD0sEK8a9VCma%2BBkEX1OFv2ApiArdz%2BGtPeKMIraiXUbNpkAowPnqkdxYj2SyIAD9iH%2Bjqv%2FXVLeoa0fnvoe8TTd%2BDklvgzC14xXzwMAIDPVocphi9j3w6ZqKZc9YGTMMwuAK7BsiWq0fFaEho0GxX9rVq4imhqllAfttVUSNjtNW5rT2xyfCaFz1qn0exVxEiVoGCqBBQsPM3G2vLsL3w43fECJHHpgZjpMmJ5IPyKWn3E2HET3aZEoZ%2FR7TYjJ1f%2BDhuLXixqYRyfLJL3%2Bhz8POKIUM7l3a4aeImyhrJutjpl9DSJ7kf1MKb5dgFhTkRlh7crRurATieaGh%2Baj06btb7%2BSf4s9WoYOsjAclkDgHLfSYEUQqcrqBJn0WhK7lMw6J0Zf6tc5xgKf4qbQte02jZ9mCsEEblTNqrGvbwrmglIMUJ69IQiTM%2BkBlHgy7Ov8pm5yT0VSy81ZS6C8t6F6pFp8gAFwRLfDo592bz24uzb5O3ZT00ze%2F%2BYqxSu%2F7yzRP7pvBKu8Uy6xqkp0OD9sN9GGI9S7zdKi4qTBU08OSgm4VPR59YycBuUxRCcvirnKIPb1H2vHzTCP9em8BjqkAdpcgDmyIj02Tdimwio3ybYJnZMCxGbiN9OkuWXAetUEuKFY1%2BMsBVWiesd5lqUt9yvOeDCTIR73S6XPNv3K5TpmoEHy3RNIQFMInj8LsD3j5ojpxfNV5bx2OXdC54IFFIfeKdS7A6O0tgFEIAuDH7uh56PiH%2BDncVDcpQj7EuJR4OeyuenAhs4Cpssou8%2BJR9K90jYH3dOTsezo3YJklH1dpzG6&X-Amz-Signature=b46ad9989fdaaa836441fd4076f61cfc31c6f37079d275875aada9c94a5885d3&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VQ7YB6Q%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T191057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCUjcWWb5eu4uY%2FXM%2BAf5sKda5DB%2FyfpAycnmUjpTh3WwIhAKsnFJ8stw6b5lwCszbl13Ic%2F2UJwlZP%2Fe36EMPyU2XpKogECJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwEFB%2FO0P8chGXDEFIq3AMp9h2bpN3wOqXYWDiLBn6qyMhV7rrwxKZX44AS2sa7FUVPDD0sEK8a9VCma%2BBkEX1OFv2ApiArdz%2BGtPeKMIraiXUbNpkAowPnqkdxYj2SyIAD9iH%2Bjqv%2FXVLeoa0fnvoe8TTd%2BDklvgzC14xXzwMAIDPVocphi9j3w6ZqKZc9YGTMMwuAK7BsiWq0fFaEho0GxX9rVq4imhqllAfttVUSNjtNW5rT2xyfCaFz1qn0exVxEiVoGCqBBQsPM3G2vLsL3w43fECJHHpgZjpMmJ5IPyKWn3E2HET3aZEoZ%2FR7TYjJ1f%2BDhuLXixqYRyfLJL3%2Bhz8POKIUM7l3a4aeImyhrJutjpl9DSJ7kf1MKb5dgFhTkRlh7crRurATieaGh%2Baj06btb7%2BSf4s9WoYOsjAclkDgHLfSYEUQqcrqBJn0WhK7lMw6J0Zf6tc5xgKf4qbQte02jZ9mCsEEblTNqrGvbwrmglIMUJ69IQiTM%2BkBlHgy7Ov8pm5yT0VSy81ZS6C8t6F6pFp8gAFwRLfDo592bz24uzb5O3ZT00ze%2F%2BYqxSu%2F7yzRP7pvBKu8Uy6xqkp0OD9sN9GGI9S7zdKi4qTBU08OSgm4VPR59YycBuUxRCcvirnKIPb1H2vHzTCP9em8BjqkAdpcgDmyIj02Tdimwio3ybYJnZMCxGbiN9OkuWXAetUEuKFY1%2BMsBVWiesd5lqUt9yvOeDCTIR73S6XPNv3K5TpmoEHy3RNIQFMInj8LsD3j5ojpxfNV5bx2OXdC54IFFIfeKdS7A6O0tgFEIAuDH7uh56PiH%2BDncVDcpQj7EuJR4OeyuenAhs4Cpssou8%2BJR9K90jYH3dOTsezo3YJklH1dpzG6&X-Amz-Signature=0f704d2af061c201099b3cff88867f48ee1bd8bb7320f9d4317ac6678b610942&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VQ7YB6Q%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T191057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCUjcWWb5eu4uY%2FXM%2BAf5sKda5DB%2FyfpAycnmUjpTh3WwIhAKsnFJ8stw6b5lwCszbl13Ic%2F2UJwlZP%2Fe36EMPyU2XpKogECJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwEFB%2FO0P8chGXDEFIq3AMp9h2bpN3wOqXYWDiLBn6qyMhV7rrwxKZX44AS2sa7FUVPDD0sEK8a9VCma%2BBkEX1OFv2ApiArdz%2BGtPeKMIraiXUbNpkAowPnqkdxYj2SyIAD9iH%2Bjqv%2FXVLeoa0fnvoe8TTd%2BDklvgzC14xXzwMAIDPVocphi9j3w6ZqKZc9YGTMMwuAK7BsiWq0fFaEho0GxX9rVq4imhqllAfttVUSNjtNW5rT2xyfCaFz1qn0exVxEiVoGCqBBQsPM3G2vLsL3w43fECJHHpgZjpMmJ5IPyKWn3E2HET3aZEoZ%2FR7TYjJ1f%2BDhuLXixqYRyfLJL3%2Bhz8POKIUM7l3a4aeImyhrJutjpl9DSJ7kf1MKb5dgFhTkRlh7crRurATieaGh%2Baj06btb7%2BSf4s9WoYOsjAclkDgHLfSYEUQqcrqBJn0WhK7lMw6J0Zf6tc5xgKf4qbQte02jZ9mCsEEblTNqrGvbwrmglIMUJ69IQiTM%2BkBlHgy7Ov8pm5yT0VSy81ZS6C8t6F6pFp8gAFwRLfDo592bz24uzb5O3ZT00ze%2F%2BYqxSu%2F7yzRP7pvBKu8Uy6xqkp0OD9sN9GGI9S7zdKi4qTBU08OSgm4VPR59YycBuUxRCcvirnKIPb1H2vHzTCP9em8BjqkAdpcgDmyIj02Tdimwio3ybYJnZMCxGbiN9OkuWXAetUEuKFY1%2BMsBVWiesd5lqUt9yvOeDCTIR73S6XPNv3K5TpmoEHy3RNIQFMInj8LsD3j5ojpxfNV5bx2OXdC54IFFIfeKdS7A6O0tgFEIAuDH7uh56PiH%2BDncVDcpQj7EuJR4OeyuenAhs4Cpssou8%2BJR9K90jYH3dOTsezo3YJklH1dpzG6&X-Amz-Signature=cf5d14b67df83570fe77993c3e160f5678046b110ecb843792af671604b320b6&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VQ7YB6Q%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T191057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCUjcWWb5eu4uY%2FXM%2BAf5sKda5DB%2FyfpAycnmUjpTh3WwIhAKsnFJ8stw6b5lwCszbl13Ic%2F2UJwlZP%2Fe36EMPyU2XpKogECJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwEFB%2FO0P8chGXDEFIq3AMp9h2bpN3wOqXYWDiLBn6qyMhV7rrwxKZX44AS2sa7FUVPDD0sEK8a9VCma%2BBkEX1OFv2ApiArdz%2BGtPeKMIraiXUbNpkAowPnqkdxYj2SyIAD9iH%2Bjqv%2FXVLeoa0fnvoe8TTd%2BDklvgzC14xXzwMAIDPVocphi9j3w6ZqKZc9YGTMMwuAK7BsiWq0fFaEho0GxX9rVq4imhqllAfttVUSNjtNW5rT2xyfCaFz1qn0exVxEiVoGCqBBQsPM3G2vLsL3w43fECJHHpgZjpMmJ5IPyKWn3E2HET3aZEoZ%2FR7TYjJ1f%2BDhuLXixqYRyfLJL3%2Bhz8POKIUM7l3a4aeImyhrJutjpl9DSJ7kf1MKb5dgFhTkRlh7crRurATieaGh%2Baj06btb7%2BSf4s9WoYOsjAclkDgHLfSYEUQqcrqBJn0WhK7lMw6J0Zf6tc5xgKf4qbQte02jZ9mCsEEblTNqrGvbwrmglIMUJ69IQiTM%2BkBlHgy7Ov8pm5yT0VSy81ZS6C8t6F6pFp8gAFwRLfDo592bz24uzb5O3ZT00ze%2F%2BYqxSu%2F7yzRP7pvBKu8Uy6xqkp0OD9sN9GGI9S7zdKi4qTBU08OSgm4VPR59YycBuUxRCcvirnKIPb1H2vHzTCP9em8BjqkAdpcgDmyIj02Tdimwio3ybYJnZMCxGbiN9OkuWXAetUEuKFY1%2BMsBVWiesd5lqUt9yvOeDCTIR73S6XPNv3K5TpmoEHy3RNIQFMInj8LsD3j5ojpxfNV5bx2OXdC54IFFIfeKdS7A6O0tgFEIAuDH7uh56PiH%2BDncVDcpQj7EuJR4OeyuenAhs4Cpssou8%2BJR9K90jYH3dOTsezo3YJklH1dpzG6&X-Amz-Signature=4e1b2a3c754787315d855688ffa2419f16811f7d94c22e0b1c3d1a4372d2f769&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VQ7YB6Q%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T191057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCUjcWWb5eu4uY%2FXM%2BAf5sKda5DB%2FyfpAycnmUjpTh3WwIhAKsnFJ8stw6b5lwCszbl13Ic%2F2UJwlZP%2Fe36EMPyU2XpKogECJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwEFB%2FO0P8chGXDEFIq3AMp9h2bpN3wOqXYWDiLBn6qyMhV7rrwxKZX44AS2sa7FUVPDD0sEK8a9VCma%2BBkEX1OFv2ApiArdz%2BGtPeKMIraiXUbNpkAowPnqkdxYj2SyIAD9iH%2Bjqv%2FXVLeoa0fnvoe8TTd%2BDklvgzC14xXzwMAIDPVocphi9j3w6ZqKZc9YGTMMwuAK7BsiWq0fFaEho0GxX9rVq4imhqllAfttVUSNjtNW5rT2xyfCaFz1qn0exVxEiVoGCqBBQsPM3G2vLsL3w43fECJHHpgZjpMmJ5IPyKWn3E2HET3aZEoZ%2FR7TYjJ1f%2BDhuLXixqYRyfLJL3%2Bhz8POKIUM7l3a4aeImyhrJutjpl9DSJ7kf1MKb5dgFhTkRlh7crRurATieaGh%2Baj06btb7%2BSf4s9WoYOsjAclkDgHLfSYEUQqcrqBJn0WhK7lMw6J0Zf6tc5xgKf4qbQte02jZ9mCsEEblTNqrGvbwrmglIMUJ69IQiTM%2BkBlHgy7Ov8pm5yT0VSy81ZS6C8t6F6pFp8gAFwRLfDo592bz24uzb5O3ZT00ze%2F%2BYqxSu%2F7yzRP7pvBKu8Uy6xqkp0OD9sN9GGI9S7zdKi4qTBU08OSgm4VPR59YycBuUxRCcvirnKIPb1H2vHzTCP9em8BjqkAdpcgDmyIj02Tdimwio3ybYJnZMCxGbiN9OkuWXAetUEuKFY1%2BMsBVWiesd5lqUt9yvOeDCTIR73S6XPNv3K5TpmoEHy3RNIQFMInj8LsD3j5ojpxfNV5bx2OXdC54IFFIfeKdS7A6O0tgFEIAuDH7uh56PiH%2BDncVDcpQj7EuJR4OeyuenAhs4Cpssou8%2BJR9K90jYH3dOTsezo3YJklH1dpzG6&X-Amz-Signature=302da9b2d8731de08724837222f85b688b63e1ef9e8c08c280495cda5a133357&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VQ7YB6Q%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T191057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCUjcWWb5eu4uY%2FXM%2BAf5sKda5DB%2FyfpAycnmUjpTh3WwIhAKsnFJ8stw6b5lwCszbl13Ic%2F2UJwlZP%2Fe36EMPyU2XpKogECJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwEFB%2FO0P8chGXDEFIq3AMp9h2bpN3wOqXYWDiLBn6qyMhV7rrwxKZX44AS2sa7FUVPDD0sEK8a9VCma%2BBkEX1OFv2ApiArdz%2BGtPeKMIraiXUbNpkAowPnqkdxYj2SyIAD9iH%2Bjqv%2FXVLeoa0fnvoe8TTd%2BDklvgzC14xXzwMAIDPVocphi9j3w6ZqKZc9YGTMMwuAK7BsiWq0fFaEho0GxX9rVq4imhqllAfttVUSNjtNW5rT2xyfCaFz1qn0exVxEiVoGCqBBQsPM3G2vLsL3w43fECJHHpgZjpMmJ5IPyKWn3E2HET3aZEoZ%2FR7TYjJ1f%2BDhuLXixqYRyfLJL3%2Bhz8POKIUM7l3a4aeImyhrJutjpl9DSJ7kf1MKb5dgFhTkRlh7crRurATieaGh%2Baj06btb7%2BSf4s9WoYOsjAclkDgHLfSYEUQqcrqBJn0WhK7lMw6J0Zf6tc5xgKf4qbQte02jZ9mCsEEblTNqrGvbwrmglIMUJ69IQiTM%2BkBlHgy7Ov8pm5yT0VSy81ZS6C8t6F6pFp8gAFwRLfDo592bz24uzb5O3ZT00ze%2F%2BYqxSu%2F7yzRP7pvBKu8Uy6xqkp0OD9sN9GGI9S7zdKi4qTBU08OSgm4VPR59YycBuUxRCcvirnKIPb1H2vHzTCP9em8BjqkAdpcgDmyIj02Tdimwio3ybYJnZMCxGbiN9OkuWXAetUEuKFY1%2BMsBVWiesd5lqUt9yvOeDCTIR73S6XPNv3K5TpmoEHy3RNIQFMInj8LsD3j5ojpxfNV5bx2OXdC54IFFIfeKdS7A6O0tgFEIAuDH7uh56PiH%2BDncVDcpQj7EuJR4OeyuenAhs4Cpssou8%2BJR9K90jYH3dOTsezo3YJklH1dpzG6&X-Amz-Signature=10a278565371247dec2901e3e90962b394044777ab9cb0aa618eaac236c46696&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664H6FWQQZ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T191058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDfs8n1p8Z3D7ZQPRgEXC5IcPEZW2wyfSkqcCuSGPrvaQIgJmj%2BroJQthLQkk9xiE3IloB81uWtdiqPVjpzRi0jUn8qiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIMRzRFCl9ECrkIsgircA8yQaS4VfPinhetADZqkPbkweNrNl%2FY4Kx1iCbx8M56rM%2Bh5Cvb9SjlkfCYiN6PGf1sgANNFs1nWX2CA8Im%2BbR5ejbFlLwgMzWi1n%2Fkl2iTzwOtK%2Bo%2B4PAgBzy4oxpfifdDrxgWRP0wY1CKgklpDIfB%2BOhx19aRt6yAyaCSikIGPL1JJW2zz3sbeoBz554yLX6zqKkl80hgYFnBor65Njv84BhMdPeMIGUiye8w4H1pPb9AsNSI6dDk1qgh%2B%2B%2F8nLamOvVYNHBlo%2BVqVt6tzLN6Z4czBaZoSKPSne%2BtXcqu0H%2FdzANjWjOs7xcdnPX2g5PV2SRu1sjdvICeabEa6xgQ9ajdcb5XjDiVZXav9qbaEeK%2Brm%2BzdqYf8He0J1Uvm2OThYhIwZJStNfQcNudnKYutfdR4oUsa0VN4w3b6%2F317X%2FoZrvNQlxCBkNwrumQFzOuQsro9y8V6rs4QXT%2FbTjEBWICNFnk9iod42YB5MkOBitItWiTOoxbuXCina%2FRYFnNEbUJr2fMzc8BIogXgYzoJ4ExHIzzyAsKR3PXtLNQ9iEIotCRkhKvWAVu97AedhC4Ltwh31S31mVXX3LgaU5IjME6B76u%2FnHFZH8%2BttV9rga3kvli7bvuDmwYuMLX16bwGOqUBplfNn2Ze%2FAZcm2IrJWoJ43Qe43oeIJpb5bfgcL65svwWtTUy%2BjNe4DhPrLJsqpHqx6WfPGAcm2Z7YbwUKyAf3yFTZ4rt1eCckFtmPO%2BX%2BxFDhamb1JkzFv9w09Tl%2F%2Fy5BvDMpZEwWdMf3hV1eVJ4YpHutij0RxUG1mAo5ttspIS%2FXeyZ%2FaDp7zmd9p2iJVrM7amqIRybJZPVc7URdpzFZ%2F839PEO&X-Amz-Signature=29f2caffea7dba28d177e8f162f060c932426e01c7dd651a9a36967e45465fcf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664H6FWQQZ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T191058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDfs8n1p8Z3D7ZQPRgEXC5IcPEZW2wyfSkqcCuSGPrvaQIgJmj%2BroJQthLQkk9xiE3IloB81uWtdiqPVjpzRi0jUn8qiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIMRzRFCl9ECrkIsgircA8yQaS4VfPinhetADZqkPbkweNrNl%2FY4Kx1iCbx8M56rM%2Bh5Cvb9SjlkfCYiN6PGf1sgANNFs1nWX2CA8Im%2BbR5ejbFlLwgMzWi1n%2Fkl2iTzwOtK%2Bo%2B4PAgBzy4oxpfifdDrxgWRP0wY1CKgklpDIfB%2BOhx19aRt6yAyaCSikIGPL1JJW2zz3sbeoBz554yLX6zqKkl80hgYFnBor65Njv84BhMdPeMIGUiye8w4H1pPb9AsNSI6dDk1qgh%2B%2B%2F8nLamOvVYNHBlo%2BVqVt6tzLN6Z4czBaZoSKPSne%2BtXcqu0H%2FdzANjWjOs7xcdnPX2g5PV2SRu1sjdvICeabEa6xgQ9ajdcb5XjDiVZXav9qbaEeK%2Brm%2BzdqYf8He0J1Uvm2OThYhIwZJStNfQcNudnKYutfdR4oUsa0VN4w3b6%2F317X%2FoZrvNQlxCBkNwrumQFzOuQsro9y8V6rs4QXT%2FbTjEBWICNFnk9iod42YB5MkOBitItWiTOoxbuXCina%2FRYFnNEbUJr2fMzc8BIogXgYzoJ4ExHIzzyAsKR3PXtLNQ9iEIotCRkhKvWAVu97AedhC4Ltwh31S31mVXX3LgaU5IjME6B76u%2FnHFZH8%2BttV9rga3kvli7bvuDmwYuMLX16bwGOqUBplfNn2Ze%2FAZcm2IrJWoJ43Qe43oeIJpb5bfgcL65svwWtTUy%2BjNe4DhPrLJsqpHqx6WfPGAcm2Z7YbwUKyAf3yFTZ4rt1eCckFtmPO%2BX%2BxFDhamb1JkzFv9w09Tl%2F%2Fy5BvDMpZEwWdMf3hV1eVJ4YpHutij0RxUG1mAo5ttspIS%2FXeyZ%2FaDp7zmd9p2iJVrM7amqIRybJZPVc7URdpzFZ%2F839PEO&X-Amz-Signature=2a9f3bdfa9c8384f132de134a059831e5d5758abf1689750b70a6c054978713a&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
