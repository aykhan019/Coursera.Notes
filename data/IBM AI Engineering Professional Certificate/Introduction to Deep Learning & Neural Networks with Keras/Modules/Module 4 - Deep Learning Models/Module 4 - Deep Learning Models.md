

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664TSH4UI4%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQC8To9MI%2BaY%2FY8CZPDQ%2F3m9fnKD5wFRzgCrkhwNZs0SIwIgYeSrgUlpcgbRfI7OBLzyh1zrY9xJBl6HczZYq8hsDpwq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDGxloSDutuEksW%2BDTCrcA4KCZVak3oG4s5y1QOoVxf0luAJnzeTnjpu%2BHRUKbBDYx41ceVNUNG4lHln0yoNs76XPfPm8z39hupv4v%2FXcJEJ0DpoKyXU1Ph%2FOWDMFvaGxC36P2P2pd9xFCxGJX%2Bh6cx0bxp3FACgx7lGs4rZKSvsq0Zw2x9BrQmrFT4VF3M4XcGQu9NoEmSgYj7Untxk70HoaQs%2BK8dpT%2FfUZp%2Ff34RX86R%2FXjtsGrhAZi5bHB5yocBRr8gjkajTPkCYpQNKiR91s62gVG2cpu0hSlta0Z8f0qZ69SocWzQYZetXZ2zAKzuKVWaoPzAiaYD0NVYPYXICc03LRYMQYWinfFDYhVeIBfstMiWViIyEsh%2B8zF298Irq%2F7PHkkWvUX7VVhLbwGIV3QB3XpRSxpL14GOjP1NUtN2gTP2u2NgZj1B4GRMjGgv4mA88XgyQrfYu99USC6hSt7Wd9O8mrM949Cax6Ay8x2TLhDt%2BJS1ikxDYYiuTbrjJLuab5kM1wp5q%2BpCHOCCf7Em6l4CpxyO22m1P6G9yvpnwvpjMsKQQWMvlVOXm1dSPRLk%2BYhp0dM%2FbbjcrfPm1PtZHDVafMUR88iX2R%2F5YQx%2FPaoDwMrUf%2Bykt%2FkwjH3UVBHlH%2BdLI5HnrlMKnskb0GOqUBCdFSEmfqN3En5P0EgbzzoR%2F%2F9h6zSpyhXHahY6NRxI1Py3iOPRxTXeyISooItxxJkN4VHMNTNzpq1FQR%2FHDAM4qT7J71dVtc3gXHmCLPJogof9jOwg7UmkLx9UpNtvtiHVzcNc409Zgk7PHUP%2FB2vwa2Gb24XXY2%2FgtrHN5TydyJEu70g8MWBHbmhrn8Oe643FuT5%2Bxpvou3pgli6E29fuP%2B4XyP&X-Amz-Signature=011543da3da318ee8906c95570fed9060f064dc86e0b95dc5f39b125a5c7d8e7&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664TSH4UI4%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQC8To9MI%2BaY%2FY8CZPDQ%2F3m9fnKD5wFRzgCrkhwNZs0SIwIgYeSrgUlpcgbRfI7OBLzyh1zrY9xJBl6HczZYq8hsDpwq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDGxloSDutuEksW%2BDTCrcA4KCZVak3oG4s5y1QOoVxf0luAJnzeTnjpu%2BHRUKbBDYx41ceVNUNG4lHln0yoNs76XPfPm8z39hupv4v%2FXcJEJ0DpoKyXU1Ph%2FOWDMFvaGxC36P2P2pd9xFCxGJX%2Bh6cx0bxp3FACgx7lGs4rZKSvsq0Zw2x9BrQmrFT4VF3M4XcGQu9NoEmSgYj7Untxk70HoaQs%2BK8dpT%2FfUZp%2Ff34RX86R%2FXjtsGrhAZi5bHB5yocBRr8gjkajTPkCYpQNKiR91s62gVG2cpu0hSlta0Z8f0qZ69SocWzQYZetXZ2zAKzuKVWaoPzAiaYD0NVYPYXICc03LRYMQYWinfFDYhVeIBfstMiWViIyEsh%2B8zF298Irq%2F7PHkkWvUX7VVhLbwGIV3QB3XpRSxpL14GOjP1NUtN2gTP2u2NgZj1B4GRMjGgv4mA88XgyQrfYu99USC6hSt7Wd9O8mrM949Cax6Ay8x2TLhDt%2BJS1ikxDYYiuTbrjJLuab5kM1wp5q%2BpCHOCCf7Em6l4CpxyO22m1P6G9yvpnwvpjMsKQQWMvlVOXm1dSPRLk%2BYhp0dM%2FbbjcrfPm1PtZHDVafMUR88iX2R%2F5YQx%2FPaoDwMrUf%2Bykt%2FkwjH3UVBHlH%2BdLI5HnrlMKnskb0GOqUBCdFSEmfqN3En5P0EgbzzoR%2F%2F9h6zSpyhXHahY6NRxI1Py3iOPRxTXeyISooItxxJkN4VHMNTNzpq1FQR%2FHDAM4qT7J71dVtc3gXHmCLPJogof9jOwg7UmkLx9UpNtvtiHVzcNc409Zgk7PHUP%2FB2vwa2Gb24XXY2%2FgtrHN5TydyJEu70g8MWBHbmhrn8Oe643FuT5%2Bxpvou3pgli6E29fuP%2B4XyP&X-Amz-Signature=220915e4834d1cdaae3c6768f1718fd74510bcf18956762e49363d0694661e44&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664TSH4UI4%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQC8To9MI%2BaY%2FY8CZPDQ%2F3m9fnKD5wFRzgCrkhwNZs0SIwIgYeSrgUlpcgbRfI7OBLzyh1zrY9xJBl6HczZYq8hsDpwq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDGxloSDutuEksW%2BDTCrcA4KCZVak3oG4s5y1QOoVxf0luAJnzeTnjpu%2BHRUKbBDYx41ceVNUNG4lHln0yoNs76XPfPm8z39hupv4v%2FXcJEJ0DpoKyXU1Ph%2FOWDMFvaGxC36P2P2pd9xFCxGJX%2Bh6cx0bxp3FACgx7lGs4rZKSvsq0Zw2x9BrQmrFT4VF3M4XcGQu9NoEmSgYj7Untxk70HoaQs%2BK8dpT%2FfUZp%2Ff34RX86R%2FXjtsGrhAZi5bHB5yocBRr8gjkajTPkCYpQNKiR91s62gVG2cpu0hSlta0Z8f0qZ69SocWzQYZetXZ2zAKzuKVWaoPzAiaYD0NVYPYXICc03LRYMQYWinfFDYhVeIBfstMiWViIyEsh%2B8zF298Irq%2F7PHkkWvUX7VVhLbwGIV3QB3XpRSxpL14GOjP1NUtN2gTP2u2NgZj1B4GRMjGgv4mA88XgyQrfYu99USC6hSt7Wd9O8mrM949Cax6Ay8x2TLhDt%2BJS1ikxDYYiuTbrjJLuab5kM1wp5q%2BpCHOCCf7Em6l4CpxyO22m1P6G9yvpnwvpjMsKQQWMvlVOXm1dSPRLk%2BYhp0dM%2FbbjcrfPm1PtZHDVafMUR88iX2R%2F5YQx%2FPaoDwMrUf%2Bykt%2FkwjH3UVBHlH%2BdLI5HnrlMKnskb0GOqUBCdFSEmfqN3En5P0EgbzzoR%2F%2F9h6zSpyhXHahY6NRxI1Py3iOPRxTXeyISooItxxJkN4VHMNTNzpq1FQR%2FHDAM4qT7J71dVtc3gXHmCLPJogof9jOwg7UmkLx9UpNtvtiHVzcNc409Zgk7PHUP%2FB2vwa2Gb24XXY2%2FgtrHN5TydyJEu70g8MWBHbmhrn8Oe643FuT5%2Bxpvou3pgli6E29fuP%2B4XyP&X-Amz-Signature=cc54fa1a5da48c051c21f9d524d200984e8ad7212dc97fcc8cf8d1f655372bb1&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664TSH4UI4%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQC8To9MI%2BaY%2FY8CZPDQ%2F3m9fnKD5wFRzgCrkhwNZs0SIwIgYeSrgUlpcgbRfI7OBLzyh1zrY9xJBl6HczZYq8hsDpwq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDGxloSDutuEksW%2BDTCrcA4KCZVak3oG4s5y1QOoVxf0luAJnzeTnjpu%2BHRUKbBDYx41ceVNUNG4lHln0yoNs76XPfPm8z39hupv4v%2FXcJEJ0DpoKyXU1Ph%2FOWDMFvaGxC36P2P2pd9xFCxGJX%2Bh6cx0bxp3FACgx7lGs4rZKSvsq0Zw2x9BrQmrFT4VF3M4XcGQu9NoEmSgYj7Untxk70HoaQs%2BK8dpT%2FfUZp%2Ff34RX86R%2FXjtsGrhAZi5bHB5yocBRr8gjkajTPkCYpQNKiR91s62gVG2cpu0hSlta0Z8f0qZ69SocWzQYZetXZ2zAKzuKVWaoPzAiaYD0NVYPYXICc03LRYMQYWinfFDYhVeIBfstMiWViIyEsh%2B8zF298Irq%2F7PHkkWvUX7VVhLbwGIV3QB3XpRSxpL14GOjP1NUtN2gTP2u2NgZj1B4GRMjGgv4mA88XgyQrfYu99USC6hSt7Wd9O8mrM949Cax6Ay8x2TLhDt%2BJS1ikxDYYiuTbrjJLuab5kM1wp5q%2BpCHOCCf7Em6l4CpxyO22m1P6G9yvpnwvpjMsKQQWMvlVOXm1dSPRLk%2BYhp0dM%2FbbjcrfPm1PtZHDVafMUR88iX2R%2F5YQx%2FPaoDwMrUf%2Bykt%2FkwjH3UVBHlH%2BdLI5HnrlMKnskb0GOqUBCdFSEmfqN3En5P0EgbzzoR%2F%2F9h6zSpyhXHahY6NRxI1Py3iOPRxTXeyISooItxxJkN4VHMNTNzpq1FQR%2FHDAM4qT7J71dVtc3gXHmCLPJogof9jOwg7UmkLx9UpNtvtiHVzcNc409Zgk7PHUP%2FB2vwa2Gb24XXY2%2FgtrHN5TydyJEu70g8MWBHbmhrn8Oe643FuT5%2Bxpvou3pgli6E29fuP%2B4XyP&X-Amz-Signature=c789b486977c23c559c03754e2b2142c3dc6fe42a4400135f29dbc38da670f1b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664TSH4UI4%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQC8To9MI%2BaY%2FY8CZPDQ%2F3m9fnKD5wFRzgCrkhwNZs0SIwIgYeSrgUlpcgbRfI7OBLzyh1zrY9xJBl6HczZYq8hsDpwq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDGxloSDutuEksW%2BDTCrcA4KCZVak3oG4s5y1QOoVxf0luAJnzeTnjpu%2BHRUKbBDYx41ceVNUNG4lHln0yoNs76XPfPm8z39hupv4v%2FXcJEJ0DpoKyXU1Ph%2FOWDMFvaGxC36P2P2pd9xFCxGJX%2Bh6cx0bxp3FACgx7lGs4rZKSvsq0Zw2x9BrQmrFT4VF3M4XcGQu9NoEmSgYj7Untxk70HoaQs%2BK8dpT%2FfUZp%2Ff34RX86R%2FXjtsGrhAZi5bHB5yocBRr8gjkajTPkCYpQNKiR91s62gVG2cpu0hSlta0Z8f0qZ69SocWzQYZetXZ2zAKzuKVWaoPzAiaYD0NVYPYXICc03LRYMQYWinfFDYhVeIBfstMiWViIyEsh%2B8zF298Irq%2F7PHkkWvUX7VVhLbwGIV3QB3XpRSxpL14GOjP1NUtN2gTP2u2NgZj1B4GRMjGgv4mA88XgyQrfYu99USC6hSt7Wd9O8mrM949Cax6Ay8x2TLhDt%2BJS1ikxDYYiuTbrjJLuab5kM1wp5q%2BpCHOCCf7Em6l4CpxyO22m1P6G9yvpnwvpjMsKQQWMvlVOXm1dSPRLk%2BYhp0dM%2FbbjcrfPm1PtZHDVafMUR88iX2R%2F5YQx%2FPaoDwMrUf%2Bykt%2FkwjH3UVBHlH%2BdLI5HnrlMKnskb0GOqUBCdFSEmfqN3En5P0EgbzzoR%2F%2F9h6zSpyhXHahY6NRxI1Py3iOPRxTXeyISooItxxJkN4VHMNTNzpq1FQR%2FHDAM4qT7J71dVtc3gXHmCLPJogof9jOwg7UmkLx9UpNtvtiHVzcNc409Zgk7PHUP%2FB2vwa2Gb24XXY2%2FgtrHN5TydyJEu70g8MWBHbmhrn8Oe643FuT5%2Bxpvou3pgli6E29fuP%2B4XyP&X-Amz-Signature=5681082ef5e0e8730a42b5e5c71097f0bfd1c3a229a9480e425701308dde3c9c&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664TSH4UI4%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQC8To9MI%2BaY%2FY8CZPDQ%2F3m9fnKD5wFRzgCrkhwNZs0SIwIgYeSrgUlpcgbRfI7OBLzyh1zrY9xJBl6HczZYq8hsDpwq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDGxloSDutuEksW%2BDTCrcA4KCZVak3oG4s5y1QOoVxf0luAJnzeTnjpu%2BHRUKbBDYx41ceVNUNG4lHln0yoNs76XPfPm8z39hupv4v%2FXcJEJ0DpoKyXU1Ph%2FOWDMFvaGxC36P2P2pd9xFCxGJX%2Bh6cx0bxp3FACgx7lGs4rZKSvsq0Zw2x9BrQmrFT4VF3M4XcGQu9NoEmSgYj7Untxk70HoaQs%2BK8dpT%2FfUZp%2Ff34RX86R%2FXjtsGrhAZi5bHB5yocBRr8gjkajTPkCYpQNKiR91s62gVG2cpu0hSlta0Z8f0qZ69SocWzQYZetXZ2zAKzuKVWaoPzAiaYD0NVYPYXICc03LRYMQYWinfFDYhVeIBfstMiWViIyEsh%2B8zF298Irq%2F7PHkkWvUX7VVhLbwGIV3QB3XpRSxpL14GOjP1NUtN2gTP2u2NgZj1B4GRMjGgv4mA88XgyQrfYu99USC6hSt7Wd9O8mrM949Cax6Ay8x2TLhDt%2BJS1ikxDYYiuTbrjJLuab5kM1wp5q%2BpCHOCCf7Em6l4CpxyO22m1P6G9yvpnwvpjMsKQQWMvlVOXm1dSPRLk%2BYhp0dM%2FbbjcrfPm1PtZHDVafMUR88iX2R%2F5YQx%2FPaoDwMrUf%2Bykt%2FkwjH3UVBHlH%2BdLI5HnrlMKnskb0GOqUBCdFSEmfqN3En5P0EgbzzoR%2F%2F9h6zSpyhXHahY6NRxI1Py3iOPRxTXeyISooItxxJkN4VHMNTNzpq1FQR%2FHDAM4qT7J71dVtc3gXHmCLPJogof9jOwg7UmkLx9UpNtvtiHVzcNc409Zgk7PHUP%2FB2vwa2Gb24XXY2%2FgtrHN5TydyJEu70g8MWBHbmhrn8Oe643FuT5%2Bxpvou3pgli6E29fuP%2B4XyP&X-Amz-Signature=6b5e53c5ead0de3759069fb1ddc94b9a02497e94728d47e756b1e7216ec1b58d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664TSH4UI4%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQC8To9MI%2BaY%2FY8CZPDQ%2F3m9fnKD5wFRzgCrkhwNZs0SIwIgYeSrgUlpcgbRfI7OBLzyh1zrY9xJBl6HczZYq8hsDpwq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDGxloSDutuEksW%2BDTCrcA4KCZVak3oG4s5y1QOoVxf0luAJnzeTnjpu%2BHRUKbBDYx41ceVNUNG4lHln0yoNs76XPfPm8z39hupv4v%2FXcJEJ0DpoKyXU1Ph%2FOWDMFvaGxC36P2P2pd9xFCxGJX%2Bh6cx0bxp3FACgx7lGs4rZKSvsq0Zw2x9BrQmrFT4VF3M4XcGQu9NoEmSgYj7Untxk70HoaQs%2BK8dpT%2FfUZp%2Ff34RX86R%2FXjtsGrhAZi5bHB5yocBRr8gjkajTPkCYpQNKiR91s62gVG2cpu0hSlta0Z8f0qZ69SocWzQYZetXZ2zAKzuKVWaoPzAiaYD0NVYPYXICc03LRYMQYWinfFDYhVeIBfstMiWViIyEsh%2B8zF298Irq%2F7PHkkWvUX7VVhLbwGIV3QB3XpRSxpL14GOjP1NUtN2gTP2u2NgZj1B4GRMjGgv4mA88XgyQrfYu99USC6hSt7Wd9O8mrM949Cax6Ay8x2TLhDt%2BJS1ikxDYYiuTbrjJLuab5kM1wp5q%2BpCHOCCf7Em6l4CpxyO22m1P6G9yvpnwvpjMsKQQWMvlVOXm1dSPRLk%2BYhp0dM%2FbbjcrfPm1PtZHDVafMUR88iX2R%2F5YQx%2FPaoDwMrUf%2Bykt%2FkwjH3UVBHlH%2BdLI5HnrlMKnskb0GOqUBCdFSEmfqN3En5P0EgbzzoR%2F%2F9h6zSpyhXHahY6NRxI1Py3iOPRxTXeyISooItxxJkN4VHMNTNzpq1FQR%2FHDAM4qT7J71dVtc3gXHmCLPJogof9jOwg7UmkLx9UpNtvtiHVzcNc409Zgk7PHUP%2FB2vwa2Gb24XXY2%2FgtrHN5TydyJEu70g8MWBHbmhrn8Oe643FuT5%2Bxpvou3pgli6E29fuP%2B4XyP&X-Amz-Signature=deb310533434b46a5541fec4535c6236d8152cd74c2ee209370d3c45ef7f7283&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664TSH4UI4%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQC8To9MI%2BaY%2FY8CZPDQ%2F3m9fnKD5wFRzgCrkhwNZs0SIwIgYeSrgUlpcgbRfI7OBLzyh1zrY9xJBl6HczZYq8hsDpwq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDGxloSDutuEksW%2BDTCrcA4KCZVak3oG4s5y1QOoVxf0luAJnzeTnjpu%2BHRUKbBDYx41ceVNUNG4lHln0yoNs76XPfPm8z39hupv4v%2FXcJEJ0DpoKyXU1Ph%2FOWDMFvaGxC36P2P2pd9xFCxGJX%2Bh6cx0bxp3FACgx7lGs4rZKSvsq0Zw2x9BrQmrFT4VF3M4XcGQu9NoEmSgYj7Untxk70HoaQs%2BK8dpT%2FfUZp%2Ff34RX86R%2FXjtsGrhAZi5bHB5yocBRr8gjkajTPkCYpQNKiR91s62gVG2cpu0hSlta0Z8f0qZ69SocWzQYZetXZ2zAKzuKVWaoPzAiaYD0NVYPYXICc03LRYMQYWinfFDYhVeIBfstMiWViIyEsh%2B8zF298Irq%2F7PHkkWvUX7VVhLbwGIV3QB3XpRSxpL14GOjP1NUtN2gTP2u2NgZj1B4GRMjGgv4mA88XgyQrfYu99USC6hSt7Wd9O8mrM949Cax6Ay8x2TLhDt%2BJS1ikxDYYiuTbrjJLuab5kM1wp5q%2BpCHOCCf7Em6l4CpxyO22m1P6G9yvpnwvpjMsKQQWMvlVOXm1dSPRLk%2BYhp0dM%2FbbjcrfPm1PtZHDVafMUR88iX2R%2F5YQx%2FPaoDwMrUf%2Bykt%2FkwjH3UVBHlH%2BdLI5HnrlMKnskb0GOqUBCdFSEmfqN3En5P0EgbzzoR%2F%2F9h6zSpyhXHahY6NRxI1Py3iOPRxTXeyISooItxxJkN4VHMNTNzpq1FQR%2FHDAM4qT7J71dVtc3gXHmCLPJogof9jOwg7UmkLx9UpNtvtiHVzcNc409Zgk7PHUP%2FB2vwa2Gb24XXY2%2FgtrHN5TydyJEu70g8MWBHbmhrn8Oe643FuT5%2Bxpvou3pgli6E29fuP%2B4XyP&X-Amz-Signature=4b3d9f4ffe5a757ac4f63bebdb607dc40cee97437036a7395eb974e07100b291&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664TSH4UI4%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQC8To9MI%2BaY%2FY8CZPDQ%2F3m9fnKD5wFRzgCrkhwNZs0SIwIgYeSrgUlpcgbRfI7OBLzyh1zrY9xJBl6HczZYq8hsDpwq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDGxloSDutuEksW%2BDTCrcA4KCZVak3oG4s5y1QOoVxf0luAJnzeTnjpu%2BHRUKbBDYx41ceVNUNG4lHln0yoNs76XPfPm8z39hupv4v%2FXcJEJ0DpoKyXU1Ph%2FOWDMFvaGxC36P2P2pd9xFCxGJX%2Bh6cx0bxp3FACgx7lGs4rZKSvsq0Zw2x9BrQmrFT4VF3M4XcGQu9NoEmSgYj7Untxk70HoaQs%2BK8dpT%2FfUZp%2Ff34RX86R%2FXjtsGrhAZi5bHB5yocBRr8gjkajTPkCYpQNKiR91s62gVG2cpu0hSlta0Z8f0qZ69SocWzQYZetXZ2zAKzuKVWaoPzAiaYD0NVYPYXICc03LRYMQYWinfFDYhVeIBfstMiWViIyEsh%2B8zF298Irq%2F7PHkkWvUX7VVhLbwGIV3QB3XpRSxpL14GOjP1NUtN2gTP2u2NgZj1B4GRMjGgv4mA88XgyQrfYu99USC6hSt7Wd9O8mrM949Cax6Ay8x2TLhDt%2BJS1ikxDYYiuTbrjJLuab5kM1wp5q%2BpCHOCCf7Em6l4CpxyO22m1P6G9yvpnwvpjMsKQQWMvlVOXm1dSPRLk%2BYhp0dM%2FbbjcrfPm1PtZHDVafMUR88iX2R%2F5YQx%2FPaoDwMrUf%2Bykt%2FkwjH3UVBHlH%2BdLI5HnrlMKnskb0GOqUBCdFSEmfqN3En5P0EgbzzoR%2F%2F9h6zSpyhXHahY6NRxI1Py3iOPRxTXeyISooItxxJkN4VHMNTNzpq1FQR%2FHDAM4qT7J71dVtc3gXHmCLPJogof9jOwg7UmkLx9UpNtvtiHVzcNc409Zgk7PHUP%2FB2vwa2Gb24XXY2%2FgtrHN5TydyJEu70g8MWBHbmhrn8Oe643FuT5%2Bxpvou3pgli6E29fuP%2B4XyP&X-Amz-Signature=0c7e6c130ff040ad0c3d19a49bdffd1608a75b1820aa07bb4ae111c0922d3cad&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBYZY225%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIHdSE7wqhJSApSiVHoDUt5GlGC9bKGgKa8zFU0OTvF1XAiADkJcS8I5nDEoq2JJpEU93BXjoBN%2BlCdZ6%2FEah2gdTWCr%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMEPHkG1fSczYU1PXYKtwDcErgQqEiD5I00bY1dmbVGK2KFIgkJyQp%2FqXos%2Bt%2BppAYAuj1qpUYo8%2BvdLiBbT2nuDrR2ykdmv1S5wLMxeUIjwLNX%2FrZBB9s8%2B3vS3Q3n4ZkGGBYjZMDcJihqZU%2F%2BEu5%2FRMNmOSbVsEtumPBvkJPeft9I5V1bv0tS9G%2BcSCE64SmQhE5gfAzmk%2Bp8he%2BwcY5FOzbDW13tX9r0XrMLmqKSm02qHXcje3MYtF%2FU6PmxVFaNHHqh5F3B1%2F4SWPy53RFXft549oYYPSceNerZYa%2BAYh207LkUpANrzlYcTASZeTeOgLLMvNbqKaNnfA6O5MMIISnjL8JCbXo6MeM%2B1cY80LUEM1%2FEiO%2F5Syv8ShSkVidogh%2BAW0jo7qrqpJKlWXSvRB4PwJL2FbUW1LRHJMr5esE%2BXpzCLvm2aeuj375S1m7OtKX6nJc4za%2BkTHn%2B3Ff44zBX3025ITpybsYZVaaVmhkHFC8DA1CUMZNXr1n0kOoqSe%2FTK07m6KcoYGRPuBzgPfM9SYeenzxCyexaalMqicJ27zgMRalPqPFu6sgaI5al3xaH8Rp141I6wOtSPRjMgRUdOTONijKTj2VpvUtVBdLkeIo0FR5wEe%2FpSO1UJGC0koqCX9kwQ7QTrYwpeyRvQY6pgG2RhMP0EqDJcVE3W2xiBDm9jM6izU2WjJwRK6BLKRpzGAzp8m%2BkBqKHbdmEiu0%2F5aiRJTDqHXkslEDKXIMdr9%2FfjDobuhUPrnFXlv9qKG1KfGM%2F3IODtx1L%2BPNCKYAP1mbRYM8dmMcGnbu1MtG8EPhdoOvsAUIrsb9vZVBXqNj0%2BxH5Ofj0BOCUQE%2B9nGKXgphQh%2BpCPcCc834%2F51JHg53nQlmWsye&X-Amz-Signature=aec9f53baa026775b489827426a81872df449f4b00da1333ea93bd45b052b3d7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBYZY225%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIHdSE7wqhJSApSiVHoDUt5GlGC9bKGgKa8zFU0OTvF1XAiADkJcS8I5nDEoq2JJpEU93BXjoBN%2BlCdZ6%2FEah2gdTWCr%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMEPHkG1fSczYU1PXYKtwDcErgQqEiD5I00bY1dmbVGK2KFIgkJyQp%2FqXos%2Bt%2BppAYAuj1qpUYo8%2BvdLiBbT2nuDrR2ykdmv1S5wLMxeUIjwLNX%2FrZBB9s8%2B3vS3Q3n4ZkGGBYjZMDcJihqZU%2F%2BEu5%2FRMNmOSbVsEtumPBvkJPeft9I5V1bv0tS9G%2BcSCE64SmQhE5gfAzmk%2Bp8he%2BwcY5FOzbDW13tX9r0XrMLmqKSm02qHXcje3MYtF%2FU6PmxVFaNHHqh5F3B1%2F4SWPy53RFXft549oYYPSceNerZYa%2BAYh207LkUpANrzlYcTASZeTeOgLLMvNbqKaNnfA6O5MMIISnjL8JCbXo6MeM%2B1cY80LUEM1%2FEiO%2F5Syv8ShSkVidogh%2BAW0jo7qrqpJKlWXSvRB4PwJL2FbUW1LRHJMr5esE%2BXpzCLvm2aeuj375S1m7OtKX6nJc4za%2BkTHn%2B3Ff44zBX3025ITpybsYZVaaVmhkHFC8DA1CUMZNXr1n0kOoqSe%2FTK07m6KcoYGRPuBzgPfM9SYeenzxCyexaalMqicJ27zgMRalPqPFu6sgaI5al3xaH8Rp141I6wOtSPRjMgRUdOTONijKTj2VpvUtVBdLkeIo0FR5wEe%2FpSO1UJGC0koqCX9kwQ7QTrYwpeyRvQY6pgG2RhMP0EqDJcVE3W2xiBDm9jM6izU2WjJwRK6BLKRpzGAzp8m%2BkBqKHbdmEiu0%2F5aiRJTDqHXkslEDKXIMdr9%2FfjDobuhUPrnFXlv9qKG1KfGM%2F3IODtx1L%2BPNCKYAP1mbRYM8dmMcGnbu1MtG8EPhdoOvsAUIrsb9vZVBXqNj0%2BxH5Ofj0BOCUQE%2B9nGKXgphQh%2BpCPcCc834%2F51JHg53nQlmWsye&X-Amz-Signature=403fa7ba7b0160c67dfc8ae4e6e8b2f4fc8df82ee1a59a310fadf51527c2dfd0&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
