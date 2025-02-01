

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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a856b76b-1241-47c1-a61e-debae39d7c40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOC6UTAJ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD%2FQh3%2BA7KwL2ywSVbEHwsHbltK2nMYZDaEU0LoCJSW%2FgIhALsd8KBJDxu8IfsKYrQApSPV%2Bndaf3sIupfoY3AdcshuKogECMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx2MVBr5SOrQl%2FW7LYq3ANWVlCL1yAYF9VG7PXC2gNJlNkGqlkf7GtCIGadPZP%2BGMQ6XAJVnX3xB6HnHjkgnNEXeRFaCYhG%2Btw%2Bn6bu58Eo3lwyB8x%2Bl6xR6lRoP3W%2FBp2p2o2V%2FnA3Ueb88QLWxCI84xBvxVAIyX6fMIKZ%2BLMLG1H9yrIZ9oqiWCqkmwnnq8tAxa%2BszfrF76kzjph6LT5cvgQBVg%2BDT0s0byc0UNXSoCB%2FtaQ2lAPCBh9vZgqaYJU0vdGilWE5N1bMIev%2F%2B6dzmHBKfKML37NCZnykD0pMO60TeJiyU9YRrSI6TNQClDMI5M%2FHD%2BQU9q8pqyT3TGrrxKdcsov4Lp58lTzULqIoZZysfEOLL10CLkT7r4Dhq3KqFXTRn8tvMONe67XWJJYNgTdA0yKXiLNbU2VlEuGZ82nJA2JOWf1d4k3NMy56qcL4SQTfVyggUIxHWhEd9vAZj%2F9F8GC5%2Bx60FoGx0N9OUf5E5q6L6TlsNwJmKOWfKfm07tQeoQGs0rInvjN%2FNmJsC4xNkDDUzkgKIZrdZuygmaiYY99b40WBEO%2Bhxr0juAAg5Lf2bj9zfPpl0GYCsZZJWTqFck2eTQFbsATQ1KN3V47ZIbD5x6CX%2FPXDR3f4WsbWKNVCCner95%2BRyzDv7PW8BjqkAYijNlcqyvOnZoTH7I%2Bvtv70v7PBYLg1fDtsU1JJrne3wdLVWidF%2Fr7nwACvlag36ibp8f2A1hEQVkjqk%2FTIOWoeByPY3VSeue7lFh1azDUb%2Fr1iXnTUHVfqX2G8cDdIzomAg%2F0FygfgliZyYplR3CY%2B1Zxt9tZA%2BiwZve4UUSXAZXjrh4iHCDiTsWHFmYuWDUfesd8gYGodM5Vlol%2BoFBeNDQWj&X-Amz-Signature=035a74d214556ff2f7c38a51a54e5ccd21dfddb9440d1f205de34a8fdf2c4149&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Input Dimensions
- **Grayscale Images**: (n x m x 1)
- **Colored Images**: (n x m x 3), where 3 represents RGB channels.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c425f6cf-48e6-47ec-a267-b9616abf9492/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOC6UTAJ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD%2FQh3%2BA7KwL2ywSVbEHwsHbltK2nMYZDaEU0LoCJSW%2FgIhALsd8KBJDxu8IfsKYrQApSPV%2Bndaf3sIupfoY3AdcshuKogECMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx2MVBr5SOrQl%2FW7LYq3ANWVlCL1yAYF9VG7PXC2gNJlNkGqlkf7GtCIGadPZP%2BGMQ6XAJVnX3xB6HnHjkgnNEXeRFaCYhG%2Btw%2Bn6bu58Eo3lwyB8x%2Bl6xR6lRoP3W%2FBp2p2o2V%2FnA3Ueb88QLWxCI84xBvxVAIyX6fMIKZ%2BLMLG1H9yrIZ9oqiWCqkmwnnq8tAxa%2BszfrF76kzjph6LT5cvgQBVg%2BDT0s0byc0UNXSoCB%2FtaQ2lAPCBh9vZgqaYJU0vdGilWE5N1bMIev%2F%2B6dzmHBKfKML37NCZnykD0pMO60TeJiyU9YRrSI6TNQClDMI5M%2FHD%2BQU9q8pqyT3TGrrxKdcsov4Lp58lTzULqIoZZysfEOLL10CLkT7r4Dhq3KqFXTRn8tvMONe67XWJJYNgTdA0yKXiLNbU2VlEuGZ82nJA2JOWf1d4k3NMy56qcL4SQTfVyggUIxHWhEd9vAZj%2F9F8GC5%2Bx60FoGx0N9OUf5E5q6L6TlsNwJmKOWfKfm07tQeoQGs0rInvjN%2FNmJsC4xNkDDUzkgKIZrdZuygmaiYY99b40WBEO%2Bhxr0juAAg5Lf2bj9zfPpl0GYCsZZJWTqFck2eTQFbsATQ1KN3V47ZIbD5x6CX%2FPXDR3f4WsbWKNVCCner95%2BRyzDv7PW8BjqkAYijNlcqyvOnZoTH7I%2Bvtv70v7PBYLg1fDtsU1JJrne3wdLVWidF%2Fr7nwACvlag36ibp8f2A1hEQVkjqk%2FTIOWoeByPY3VSeue7lFh1azDUb%2Fr1iXnTUHVfqX2G8cDdIzomAg%2F0FygfgliZyYplR3CY%2B1Zxt9tZA%2BiwZve4UUSXAZXjrh4iHCDiTsWHFmYuWDUfesd8gYGodM5Vlol%2BoFBeNDQWj&X-Amz-Signature=b026a3439fb8942cb11504ad54fc486a013cea3ae39d7d77a2dc20a1ca50783f&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Components of CNNs
#### 1. Convolutional Layer
- **Purpose**: Applies filters to the input image to produce feature maps.
- **Filter**: A small matrix used to detect features such as edges, textures, or patterns.
- **Operation**: Computes the convolution operation between the filter and the input image.
	- **Filter Size**: e.g., (2 x 2)
	- **Stride**: The number of pixels by which the filter moves across the image.
	- **Output**: An empty matrix filled with results from the convolution process
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f46f7f48-ccab-4a7b-adb0-4b63dbd530da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOC6UTAJ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD%2FQh3%2BA7KwL2ywSVbEHwsHbltK2nMYZDaEU0LoCJSW%2FgIhALsd8KBJDxu8IfsKYrQApSPV%2Bndaf3sIupfoY3AdcshuKogECMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx2MVBr5SOrQl%2FW7LYq3ANWVlCL1yAYF9VG7PXC2gNJlNkGqlkf7GtCIGadPZP%2BGMQ6XAJVnX3xB6HnHjkgnNEXeRFaCYhG%2Btw%2Bn6bu58Eo3lwyB8x%2Bl6xR6lRoP3W%2FBp2p2o2V%2FnA3Ueb88QLWxCI84xBvxVAIyX6fMIKZ%2BLMLG1H9yrIZ9oqiWCqkmwnnq8tAxa%2BszfrF76kzjph6LT5cvgQBVg%2BDT0s0byc0UNXSoCB%2FtaQ2lAPCBh9vZgqaYJU0vdGilWE5N1bMIev%2F%2B6dzmHBKfKML37NCZnykD0pMO60TeJiyU9YRrSI6TNQClDMI5M%2FHD%2BQU9q8pqyT3TGrrxKdcsov4Lp58lTzULqIoZZysfEOLL10CLkT7r4Dhq3KqFXTRn8tvMONe67XWJJYNgTdA0yKXiLNbU2VlEuGZ82nJA2JOWf1d4k3NMy56qcL4SQTfVyggUIxHWhEd9vAZj%2F9F8GC5%2Bx60FoGx0N9OUf5E5q6L6TlsNwJmKOWfKfm07tQeoQGs0rInvjN%2FNmJsC4xNkDDUzkgKIZrdZuygmaiYY99b40WBEO%2Bhxr0juAAg5Lf2bj9zfPpl0GYCsZZJWTqFck2eTQFbsATQ1KN3V47ZIbD5x6CX%2FPXDR3f4WsbWKNVCCner95%2BRyzDv7PW8BjqkAYijNlcqyvOnZoTH7I%2Bvtv70v7PBYLg1fDtsU1JJrne3wdLVWidF%2Fr7nwACvlag36ibp8f2A1hEQVkjqk%2FTIOWoeByPY3VSeue7lFh1azDUb%2Fr1iXnTUHVfqX2G8cDdIzomAg%2F0FygfgliZyYplR3CY%2B1Zxt9tZA%2BiwZve4UUSXAZXjrh4iHCDiTsWHFmYuWDUfesd8gYGodM5Vlol%2BoFBeNDQWj&X-Amz-Signature=d7ad1ef8f37b60f8d6fa9897cdb942531c7559f7f1e3abb05f4c2d01072cae7b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 2. Activation Function (ReLU)
- **Purpose**: Introduces non-linearity into the model.
- **Operation**: Applies the ReLU (Rectified Linear Unit) function to the output of the convolutional layer.
	- **ReLU Function**: Outputs the input directly if it is positive; otherwise, it outputs zero.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7660e416-eb44-4488-b210-c6c586e99cc4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOC6UTAJ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD%2FQh3%2BA7KwL2ywSVbEHwsHbltK2nMYZDaEU0LoCJSW%2FgIhALsd8KBJDxu8IfsKYrQApSPV%2Bndaf3sIupfoY3AdcshuKogECMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx2MVBr5SOrQl%2FW7LYq3ANWVlCL1yAYF9VG7PXC2gNJlNkGqlkf7GtCIGadPZP%2BGMQ6XAJVnX3xB6HnHjkgnNEXeRFaCYhG%2Btw%2Bn6bu58Eo3lwyB8x%2Bl6xR6lRoP3W%2FBp2p2o2V%2FnA3Ueb88QLWxCI84xBvxVAIyX6fMIKZ%2BLMLG1H9yrIZ9oqiWCqkmwnnq8tAxa%2BszfrF76kzjph6LT5cvgQBVg%2BDT0s0byc0UNXSoCB%2FtaQ2lAPCBh9vZgqaYJU0vdGilWE5N1bMIev%2F%2B6dzmHBKfKML37NCZnykD0pMO60TeJiyU9YRrSI6TNQClDMI5M%2FHD%2BQU9q8pqyT3TGrrxKdcsov4Lp58lTzULqIoZZysfEOLL10CLkT7r4Dhq3KqFXTRn8tvMONe67XWJJYNgTdA0yKXiLNbU2VlEuGZ82nJA2JOWf1d4k3NMy56qcL4SQTfVyggUIxHWhEd9vAZj%2F9F8GC5%2Bx60FoGx0N9OUf5E5q6L6TlsNwJmKOWfKfm07tQeoQGs0rInvjN%2FNmJsC4xNkDDUzkgKIZrdZuygmaiYY99b40WBEO%2Bhxr0juAAg5Lf2bj9zfPpl0GYCsZZJWTqFck2eTQFbsATQ1KN3V47ZIbD5x6CX%2FPXDR3f4WsbWKNVCCner95%2BRyzDv7PW8BjqkAYijNlcqyvOnZoTH7I%2Bvtv70v7PBYLg1fDtsU1JJrne3wdLVWidF%2Fr7nwACvlag36ibp8f2A1hEQVkjqk%2FTIOWoeByPY3VSeue7lFh1azDUb%2Fr1iXnTUHVfqX2G8cDdIzomAg%2F0FygfgliZyYplR3CY%2B1Zxt9tZA%2BiwZve4UUSXAZXjrh4iHCDiTsWHFmYuWDUfesd8gYGodM5Vlol%2BoFBeNDQWj&X-Amz-Signature=ba23a69ba5e47b8c95065ba799fe1aa1b7178660520550c88121f62322277557&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 3. Pooling Layer
- **Purpose**: Reduces the spatial dimensions of the feature maps.
- **Types**:
	- **Max-Pooling**: Selects the maximum value from each section of the feature map.
		- **Filter Size**: e.g., (2 x 2)
		- **Stride**: The number of pixels by which the pooling filter moves.
	- **Average-Pooling**: Computes the average value from each section of the feature map.
- **Benefit**: Reduces computational complexity and helps prevent overfitting.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8791e5e6-af9f-45eb-a433-23a7c733feb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOC6UTAJ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD%2FQh3%2BA7KwL2ywSVbEHwsHbltK2nMYZDaEU0LoCJSW%2FgIhALsd8KBJDxu8IfsKYrQApSPV%2Bndaf3sIupfoY3AdcshuKogECMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx2MVBr5SOrQl%2FW7LYq3ANWVlCL1yAYF9VG7PXC2gNJlNkGqlkf7GtCIGadPZP%2BGMQ6XAJVnX3xB6HnHjkgnNEXeRFaCYhG%2Btw%2Bn6bu58Eo3lwyB8x%2Bl6xR6lRoP3W%2FBp2p2o2V%2FnA3Ueb88QLWxCI84xBvxVAIyX6fMIKZ%2BLMLG1H9yrIZ9oqiWCqkmwnnq8tAxa%2BszfrF76kzjph6LT5cvgQBVg%2BDT0s0byc0UNXSoCB%2FtaQ2lAPCBh9vZgqaYJU0vdGilWE5N1bMIev%2F%2B6dzmHBKfKML37NCZnykD0pMO60TeJiyU9YRrSI6TNQClDMI5M%2FHD%2BQU9q8pqyT3TGrrxKdcsov4Lp58lTzULqIoZZysfEOLL10CLkT7r4Dhq3KqFXTRn8tvMONe67XWJJYNgTdA0yKXiLNbU2VlEuGZ82nJA2JOWf1d4k3NMy56qcL4SQTfVyggUIxHWhEd9vAZj%2F9F8GC5%2Bx60FoGx0N9OUf5E5q6L6TlsNwJmKOWfKfm07tQeoQGs0rInvjN%2FNmJsC4xNkDDUzkgKIZrdZuygmaiYY99b40WBEO%2Bhxr0juAAg5Lf2bj9zfPpl0GYCsZZJWTqFck2eTQFbsATQ1KN3V47ZIbD5x6CX%2FPXDR3f4WsbWKNVCCner95%2BRyzDv7PW8BjqkAYijNlcqyvOnZoTH7I%2Bvtv70v7PBYLg1fDtsU1JJrne3wdLVWidF%2Fr7nwACvlag36ibp8f2A1hEQVkjqk%2FTIOWoeByPY3VSeue7lFh1azDUb%2Fr1iXnTUHVfqX2G8cDdIzomAg%2F0FygfgliZyYplR3CY%2B1Zxt9tZA%2BiwZve4UUSXAZXjrh4iHCDiTsWHFmYuWDUfesd8gYGodM5Vlol%2BoFBeNDQWj&X-Amz-Signature=5cbdeaaea3104c5a8294e78f1594427ebb19bbc1fd91be909906161644ce2b16&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4c528212-221a-47dc-9d7c-9ae194171597/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOC6UTAJ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD%2FQh3%2BA7KwL2ywSVbEHwsHbltK2nMYZDaEU0LoCJSW%2FgIhALsd8KBJDxu8IfsKYrQApSPV%2Bndaf3sIupfoY3AdcshuKogECMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx2MVBr5SOrQl%2FW7LYq3ANWVlCL1yAYF9VG7PXC2gNJlNkGqlkf7GtCIGadPZP%2BGMQ6XAJVnX3xB6HnHjkgnNEXeRFaCYhG%2Btw%2Bn6bu58Eo3lwyB8x%2Bl6xR6lRoP3W%2FBp2p2o2V%2FnA3Ueb88QLWxCI84xBvxVAIyX6fMIKZ%2BLMLG1H9yrIZ9oqiWCqkmwnnq8tAxa%2BszfrF76kzjph6LT5cvgQBVg%2BDT0s0byc0UNXSoCB%2FtaQ2lAPCBh9vZgqaYJU0vdGilWE5N1bMIev%2F%2B6dzmHBKfKML37NCZnykD0pMO60TeJiyU9YRrSI6TNQClDMI5M%2FHD%2BQU9q8pqyT3TGrrxKdcsov4Lp58lTzULqIoZZysfEOLL10CLkT7r4Dhq3KqFXTRn8tvMONe67XWJJYNgTdA0yKXiLNbU2VlEuGZ82nJA2JOWf1d4k3NMy56qcL4SQTfVyggUIxHWhEd9vAZj%2F9F8GC5%2Bx60FoGx0N9OUf5E5q6L6TlsNwJmKOWfKfm07tQeoQGs0rInvjN%2FNmJsC4xNkDDUzkgKIZrdZuygmaiYY99b40WBEO%2Bhxr0juAAg5Lf2bj9zfPpl0GYCsZZJWTqFck2eTQFbsATQ1KN3V47ZIbD5x6CX%2FPXDR3f4WsbWKNVCCner95%2BRyzDv7PW8BjqkAYijNlcqyvOnZoTH7I%2Bvtv70v7PBYLg1fDtsU1JJrne3wdLVWidF%2Fr7nwACvlag36ibp8f2A1hEQVkjqk%2FTIOWoeByPY3VSeue7lFh1azDUb%2Fr1iXnTUHVfqX2G8cDdIzomAg%2F0FygfgliZyYplR3CY%2B1Zxt9tZA%2BiwZve4UUSXAZXjrh4iHCDiTsWHFmYuWDUfesd8gYGodM5Vlol%2BoFBeNDQWj&X-Amz-Signature=1ba96bc335fbb63f910b0667e3dc370637eeadf458e8e152410fe1b0f92ebdb2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### 4. Fully Connected Layer
- **Purpose**: Connects every node from the previous layer to every node in the current layer.
- **Operation**: Flattens the output from the previous layers and produces an n-dimensional vector, where n corresponds to the number of classes.
- **Activation Function**: Typically uses the softmax function to convert the outputs into probabilities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/51e84329-f1c0-4784-a080-d1fbd5c4d0ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOC6UTAJ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD%2FQh3%2BA7KwL2ywSVbEHwsHbltK2nMYZDaEU0LoCJSW%2FgIhALsd8KBJDxu8IfsKYrQApSPV%2Bndaf3sIupfoY3AdcshuKogECMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx2MVBr5SOrQl%2FW7LYq3ANWVlCL1yAYF9VG7PXC2gNJlNkGqlkf7GtCIGadPZP%2BGMQ6XAJVnX3xB6HnHjkgnNEXeRFaCYhG%2Btw%2Bn6bu58Eo3lwyB8x%2Bl6xR6lRoP3W%2FBp2p2o2V%2FnA3Ueb88QLWxCI84xBvxVAIyX6fMIKZ%2BLMLG1H9yrIZ9oqiWCqkmwnnq8tAxa%2BszfrF76kzjph6LT5cvgQBVg%2BDT0s0byc0UNXSoCB%2FtaQ2lAPCBh9vZgqaYJU0vdGilWE5N1bMIev%2F%2B6dzmHBKfKML37NCZnykD0pMO60TeJiyU9YRrSI6TNQClDMI5M%2FHD%2BQU9q8pqyT3TGrrxKdcsov4Lp58lTzULqIoZZysfEOLL10CLkT7r4Dhq3KqFXTRn8tvMONe67XWJJYNgTdA0yKXiLNbU2VlEuGZ82nJA2JOWf1d4k3NMy56qcL4SQTfVyggUIxHWhEd9vAZj%2F9F8GC5%2Bx60FoGx0N9OUf5E5q6L6TlsNwJmKOWfKfm07tQeoQGs0rInvjN%2FNmJsC4xNkDDUzkgKIZrdZuygmaiYY99b40WBEO%2Bhxr0juAAg5Lf2bj9zfPpl0GYCsZZJWTqFck2eTQFbsATQ1KN3V47ZIbD5x6CX%2FPXDR3f4WsbWKNVCCner95%2BRyzDv7PW8BjqkAYijNlcqyvOnZoTH7I%2Bvtv70v7PBYLg1fDtsU1JJrne3wdLVWidF%2Fr7nwACvlag36ibp8f2A1hEQVkjqk%2FTIOWoeByPY3VSeue7lFh1azDUb%2Fr1iXnTUHVfqX2G8cDdIzomAg%2F0FygfgliZyYplR3CY%2B1Zxt9tZA%2BiwZve4UUSXAZXjrh4iHCDiTsWHFmYuWDUfesd8gYGodM5Vlol%2BoFBeNDQWj&X-Amz-Signature=4d635f04e0e935e5fede5737741d0f580d26d8328f068350201e36c55514b525&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/47b54c06-9f0d-49d3-9183-2d29bfa51d80/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOC6UTAJ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD%2FQh3%2BA7KwL2ywSVbEHwsHbltK2nMYZDaEU0LoCJSW%2FgIhALsd8KBJDxu8IfsKYrQApSPV%2Bndaf3sIupfoY3AdcshuKogECMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx2MVBr5SOrQl%2FW7LYq3ANWVlCL1yAYF9VG7PXC2gNJlNkGqlkf7GtCIGadPZP%2BGMQ6XAJVnX3xB6HnHjkgnNEXeRFaCYhG%2Btw%2Bn6bu58Eo3lwyB8x%2Bl6xR6lRoP3W%2FBp2p2o2V%2FnA3Ueb88QLWxCI84xBvxVAIyX6fMIKZ%2BLMLG1H9yrIZ9oqiWCqkmwnnq8tAxa%2BszfrF76kzjph6LT5cvgQBVg%2BDT0s0byc0UNXSoCB%2FtaQ2lAPCBh9vZgqaYJU0vdGilWE5N1bMIev%2F%2B6dzmHBKfKML37NCZnykD0pMO60TeJiyU9YRrSI6TNQClDMI5M%2FHD%2BQU9q8pqyT3TGrrxKdcsov4Lp58lTzULqIoZZysfEOLL10CLkT7r4Dhq3KqFXTRn8tvMONe67XWJJYNgTdA0yKXiLNbU2VlEuGZ82nJA2JOWf1d4k3NMy56qcL4SQTfVyggUIxHWhEd9vAZj%2F9F8GC5%2Bx60FoGx0N9OUf5E5q6L6TlsNwJmKOWfKfm07tQeoQGs0rInvjN%2FNmJsC4xNkDDUzkgKIZrdZuygmaiYY99b40WBEO%2Bhxr0juAAg5Lf2bj9zfPpl0GYCsZZJWTqFck2eTQFbsATQ1KN3V47ZIbD5x6CX%2FPXDR3f4WsbWKNVCCner95%2BRyzDv7PW8BjqkAYijNlcqyvOnZoTH7I%2Bvtv70v7PBYLg1fDtsU1JJrne3wdLVWidF%2Fr7nwACvlag36ibp8f2A1hEQVkjqk%2FTIOWoeByPY3VSeue7lFh1azDUb%2Fr1iXnTUHVfqX2G8cDdIzomAg%2F0FygfgliZyYplR3CY%2B1Zxt9tZA%2BiwZve4UUSXAZXjrh4iHCDiTsWHFmYuWDUfesd8gYGodM5Vlol%2BoFBeNDQWj&X-Amz-Signature=dda20b875c1afaf54666a35298a9e9c2c33095db3cea5ba1a23839b5372add49&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/88d6b2af-f6f0-4932-984c-b68479fb8ab5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOC6UTAJ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD%2FQh3%2BA7KwL2ywSVbEHwsHbltK2nMYZDaEU0LoCJSW%2FgIhALsd8KBJDxu8IfsKYrQApSPV%2Bndaf3sIupfoY3AdcshuKogECMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx2MVBr5SOrQl%2FW7LYq3ANWVlCL1yAYF9VG7PXC2gNJlNkGqlkf7GtCIGadPZP%2BGMQ6XAJVnX3xB6HnHjkgnNEXeRFaCYhG%2Btw%2Bn6bu58Eo3lwyB8x%2Bl6xR6lRoP3W%2FBp2p2o2V%2FnA3Ueb88QLWxCI84xBvxVAIyX6fMIKZ%2BLMLG1H9yrIZ9oqiWCqkmwnnq8tAxa%2BszfrF76kzjph6LT5cvgQBVg%2BDT0s0byc0UNXSoCB%2FtaQ2lAPCBh9vZgqaYJU0vdGilWE5N1bMIev%2F%2B6dzmHBKfKML37NCZnykD0pMO60TeJiyU9YRrSI6TNQClDMI5M%2FHD%2BQU9q8pqyT3TGrrxKdcsov4Lp58lTzULqIoZZysfEOLL10CLkT7r4Dhq3KqFXTRn8tvMONe67XWJJYNgTdA0yKXiLNbU2VlEuGZ82nJA2JOWf1d4k3NMy56qcL4SQTfVyggUIxHWhEd9vAZj%2F9F8GC5%2Bx60FoGx0N9OUf5E5q6L6TlsNwJmKOWfKfm07tQeoQGs0rInvjN%2FNmJsC4xNkDDUzkgKIZrdZuygmaiYY99b40WBEO%2Bhxr0juAAg5Lf2bj9zfPpl0GYCsZZJWTqFck2eTQFbsATQ1KN3V47ZIbD5x6CX%2FPXDR3f4WsbWKNVCCner95%2BRyzDv7PW8BjqkAYijNlcqyvOnZoTH7I%2Bvtv70v7PBYLg1fDtsU1JJrne3wdLVWidF%2Fr7nwACvlag36ibp8f2A1hEQVkjqk%2FTIOWoeByPY3VSeue7lFh1azDUb%2Fr1iXnTUHVfqX2G8cDdIzomAg%2F0FygfgliZyYplR3CY%2B1Zxt9tZA%2BiwZve4UUSXAZXjrh4iHCDiTsWHFmYuWDUfesd8gYGodM5Vlol%2BoFBeNDQWj&X-Amz-Signature=99da6743b8c5a792e1b07825b9e63039eafcc3de307982f2ede4ed6754e1ae48&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13d5eb4d-dac0-40e6-97fb-d5688c6a13e7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665YR3H3YK%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBZIau3NPpZWXDCpvRzM44I%2FbhQz7yP3wg4wxzzAFWgvAiEAmoBlvPoOzoo2pcc1UvVSysr0TzXE5XLhcvh47pyFUZsqiAQIyv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK22XvXEZjz3dpnLlyrcAwmqQ16JXra0K1ffxVUjwnFvOqxw5empj3RXydr4sA5MhJi3bTAYTjX6p9uyKxwDg%2FFEU8Gjg8PRwlmj473NFawImngG2AgCp5bO9kOp6O47nIDez1%2BvU7Jykw78I2FAPlSv%2B9fpTzmUBw1msBk1T1SIiY70wFnL%2F5RLJPdNXyGgQhFNqFQPFvVTIoOA7OHHXl5lDifXPFOGE3wU79wR4Vt5AeWS4ycoWANW7y3gX6b6guTpFnYQ2PiOwkDirjbJBaPFDom00xybCoYGLPL3cbBsg%2BlwuRv6MHmELqIXvJraXVYOE6JXhNyHk0XwoFFrpvpeY2%2BakUBpL8gpMWcVSuphYc54cu027Nht1WLGVe4fdcWcFUX6qwwvtwzd7RgZpzisCR90o7aNCOTuxhRAtKxENMtYkljMAT5aHYvgb7%2BfWqSSJiDrcDeIXZk2H9OuYO1wS%2BZ0D1UcOAr5FbEqMjOD8NgN2f%2FpaKBo0lr3nZOw8%2Fgr%2FLMvNy1OY64GBbOhLrkEcAMY%2FO6WmS4qIxUULSCvg8pql22%2FA48VbMHiS0S%2B63lAZETPGMdtqUkNUqtZR0MziDBzm58vxZnOYmbb7mEd4g1Gfs1RixiUzcUBUZhHlXR4F%2F5dJKUdE99zMOTs9bwGOqUB%2FqJI%2FY%2B%2BpTEmKG9P2JY0z2TNTPoGPPA91K6BiLEReGLbgo%2FkVhUYpsuTTbSPS8vlptFlvmTRwiiUHoioHmju%2FuUalof3Jf43yCs2gzUC5eNJrUGzkRrzMuNvDIPKDUb0OvJh6l6VONFWyZqt2oBQelJw3ZYZejm6ePE1fQ%2BM95NUHrqoYAzEc6fUuPX5jPnvwNMc0GIts%2BN0wzKUBUTu1RJMWTf9&X-Amz-Signature=1a62d0f29971cc433ffb618b9d7ed1eef0b5df936cb28e51135b793533e3fb0d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e56b5c68-d1d6-4a40-986f-30aa54ab7681/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665YR3H3YK%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBZIau3NPpZWXDCpvRzM44I%2FbhQz7yP3wg4wxzzAFWgvAiEAmoBlvPoOzoo2pcc1UvVSysr0TzXE5XLhcvh47pyFUZsqiAQIyv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK22XvXEZjz3dpnLlyrcAwmqQ16JXra0K1ffxVUjwnFvOqxw5empj3RXydr4sA5MhJi3bTAYTjX6p9uyKxwDg%2FFEU8Gjg8PRwlmj473NFawImngG2AgCp5bO9kOp6O47nIDez1%2BvU7Jykw78I2FAPlSv%2B9fpTzmUBw1msBk1T1SIiY70wFnL%2F5RLJPdNXyGgQhFNqFQPFvVTIoOA7OHHXl5lDifXPFOGE3wU79wR4Vt5AeWS4ycoWANW7y3gX6b6guTpFnYQ2PiOwkDirjbJBaPFDom00xybCoYGLPL3cbBsg%2BlwuRv6MHmELqIXvJraXVYOE6JXhNyHk0XwoFFrpvpeY2%2BakUBpL8gpMWcVSuphYc54cu027Nht1WLGVe4fdcWcFUX6qwwvtwzd7RgZpzisCR90o7aNCOTuxhRAtKxENMtYkljMAT5aHYvgb7%2BfWqSSJiDrcDeIXZk2H9OuYO1wS%2BZ0D1UcOAr5FbEqMjOD8NgN2f%2FpaKBo0lr3nZOw8%2Fgr%2FLMvNy1OY64GBbOhLrkEcAMY%2FO6WmS4qIxUULSCvg8pql22%2FA48VbMHiS0S%2B63lAZETPGMdtqUkNUqtZR0MziDBzm58vxZnOYmbb7mEd4g1Gfs1RixiUzcUBUZhHlXR4F%2F5dJKUdE99zMOTs9bwGOqUB%2FqJI%2FY%2B%2BpTEmKG9P2JY0z2TNTPoGPPA91K6BiLEReGLbgo%2FkVhUYpsuTTbSPS8vlptFlvmTRwiiUHoioHmju%2FuUalof3Jf43yCs2gzUC5eNJrUGzkRrzMuNvDIPKDUb0OvJh6l6VONFWyZqt2oBQelJw3ZYZejm6ePE1fQ%2BM95NUHrqoYAzEc6fUuPX5jPnvwNMc0GIts%2BN0wzKUBUTu1RJMWTf9&X-Amz-Signature=4be23442317c95a63f41609e53b6d080df784ba099ffb296c6fba5b7d28dedc6&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
- **Autoencoders**: Useful for data compression, denoising, and dimensionality reduction.
- **RBMs**: Specialized autoencoders effective for handling imbalanced datasets, estimating missing values, and feature extraction.
This concludes the introduction to autoencoders and Restricted Boltzmann Machines (RBMs).
___
