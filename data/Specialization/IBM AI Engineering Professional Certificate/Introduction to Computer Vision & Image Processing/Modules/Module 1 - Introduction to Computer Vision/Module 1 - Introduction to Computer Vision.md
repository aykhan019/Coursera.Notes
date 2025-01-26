

# Module 1: Introduction to Computer Vision
## Introduction to Computer Vision
### Course Overview
In this course, you will be introduced to the field of computer vision, including its applications, specialized methods, and techniques. You will learn to implement these techniques using Python.
#### Learning Objectives
- Understand what computer vision is.
- Apply and use computer vision algorithms with Python and OpenCV.
- Create custom classifiers for business problems.
- Build a web app to classify images.
#### Exclusions
- How computer vision works in detail.
- How neural networks or deep learning work.
- In-depth math and statistics.
### What is Computer Vision?
Computer vision involves providing computers with the ability to see and understand images. For example, while humans can instantly recognize and interpret images, computers cannot do so without assistance.
### Industry Impact
Computer vision is making significant waves in various industries due to its ability to improve efficiency and effectiveness. Key areas where computer vision is adopted include:
- **Automation**: Reducing manual tasks and making processes faster and more convenient.
- **Cost Efficiency**: Lowering expenses and making technologies more accessible.
- **Scalability**: Enabling scalable solutions for various applications.
#### Groundbreaking Change
Self-driving cars are a notable example of computer vision's impact, automating driving and potentially saving lives.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d2ff3738-322b-4bed-b884-e286566efb94/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45FSPPWI6X%2F20250126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250126T101405Z&X-Amz-Expires=3600&X-Amz-Signature=0805bffa80799fbbf9e8ffcc4b05decfa84317009dd908b40cb43e5e584fd687&X-Amz-SignedHeaders=host&x-id=GetObject)
### Applications Across Industries
Computer vision has transformative applications in multiple sectors, including:
- **Automotive**
- **Manufacturing**
- **Human Resources**
- **Insurance**
- **Healthcare**
#### Case Study: ADNOC
ADNOC (Abu Dhabi National Oil Company) produces around 3 million barrels of oil and 10.5 billion cubic feet of raw gas daily. Traditionally, classifying rock samples was labor-intensive. By using IBM Watson for analyzing high-resolution rock images, ADNOC can classify up to 25,000 thin-section rock images per day, significantly saving time and resources.
![merlin_190903830_f0aa9789-8002-4443-889b-cf52a2291890-articleLarge.webp](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00c2a896-0042-4cbe-a1e6-6bcda9bea64c/merlin_190903830_f0aa9789-8002-4443-889b-cf52a2291890-articleLarge.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45FSPPWI6X%2F20250126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250126T101405Z&X-Amz-Expires=3600&X-Amz-Signature=a8d26fef28a35f6a6e1d2acb788c13b9ec11cbf97d3fa8405100c60b3d28bc9a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Case Study: Knockri
In the HR sector, Knockri, a Canadian startup, is revolutionizing hiring with an AI video soft skill assessment tool. By leveraging computer vision, machine learning, and data science, Knockri quantifies soft skills and assists in early candidate assessments, streamlining the hiring process for large companies.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4f485c63-f28c-48ae-b5ae-758411aae60b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45FSPPWI6X%2F20250126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250126T101405Z&X-Amz-Expires=3600&X-Amz-Signature=8ce31a43ae93594cf3f120957d097112fa3b5c904e4dbaa938bf7e3fe0c086cb&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
Computer vision is rapidly transforming industries by enhancing automation, cost-efficiency, and scalability. Its applications are broad, impacting everything from oil classification to hiring processes.
___
## Applications of Computer Vision
### Overview
In this section, we explore various applications of computer vision and discuss how you can develop your own applications.
### Searching Through Videos
One common challenge is searching through videos to find specific scenes. Traditionally, this requires fast-forwarding and manual searching. IBM has addressed this by tagging videos with keywords based on the objects present in each scene.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6611b4b5-7716-4238-9394-371b7f97dd8d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45FSPPWI6X%2F20250126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250126T101405Z&X-Amz-Expires=3600&X-Amz-Signature=594aa9b49016f38a0e7ada809d3feee86bf5cddace1ce1c0285a6930fe9db34c&X-Amz-SignedHeaders=host&x-id=GetObject)
### Security and Object Recognition
Imagine a security company needing to find a suspect in a blue van among hours of footage. With computer vision and object recognition, this task becomes manageable and efficient, eliminating the need for extensive manual searching.
### Maintenance of Electric Towers
Electric towers require regular maintenance to check for rust and structural defects. Manually inspecting each tower is time-consuming and costly. Instead, high-resolution images can be taken from different angles, which are then analyzed using computer vision.
#### Custom Image Classifiers
By dividing high-resolution images into smaller segments, you can develop custom image classifiers. These classifiers can detect the presence of metal versus non-metal objects and assess the level of rust.
- **Metal Classifier**: Identifies metal structures in images.
- **Rust Classifier**: Determines the rust level based on predefined criteria, such as:
	- **Grade 1 Rust**: Minimal rust
	- **Grade 6 Rust**: Severe rust
This approach can save significant costs for industries like insurance by automating the analysis of thousands or millions of images.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/16d9e2cd-921b-4673-9544-fd20224f176c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45FSPPWI6X%2F20250126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250126T101405Z&X-Amz-Expires=3600&X-Amz-Signature=a439daac58338d714933663bcfd6f8a5a404a5607627bb30cd74dae2806472ee&X-Amz-SignedHeaders=host&x-id=GetObject)
### Insurance Claims Processing
Computer vision can also streamline the processing of insurance claims by automatically classifying damage, such as hail or ice pellet damage from storms. This improves efficiency and accuracy, reducing the time and cost associated with claim processing.
### Summary
This section highlights the diverse applications of computer vision, demonstrating how it can enhance efficiency and reduce costs across various industries, from security and maintenance to insurance.
___
## Active Research in Computer Vision
### Overview
This section covers recent advancements and ongoing research in the field of computer vision over the past decade.
### Object Detection
Researchers at Facebook are focusing on detecting objects in images. Accurate and efficient object detection is crucial for making meaningful inferences from images and video streams. This capability is particularly important for applications such as self-driving cars, where real-time object detection from camera feeds is necessary to avoid obstacles and prevent collisions.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4abd25e4-e758-4223-b0a0-c40adde5fd3d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45FSPPWI6X%2F20250126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250126T101405Z&X-Amz-Expires=3600&X-Amz-Signature=956bd593206bcc7358ad50764632162efa2978849454d787ef36dfc1b3e44285&X-Amz-SignedHeaders=host&x-id=GetObject)
### Image to Image Translation
Image to image translation involves converting an image from one representation to another. For example, transforming an image of a horse into a zebra or changing the scene of an image from summer to winter. Researchers at UC Berkeley are working on techniques for this kind of transformation, allowing for significant modifications in image content.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f4c69140-8edb-4b9c-9a3e-3ea01fdcda90/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45FSPPWI6X%2F20250126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250126T101405Z&X-Amz-Expires=3600&X-Amz-Signature=32cacc6e2dbbf3ab71194c08aa8b845161e7a0bcbaae1cbcb1b6147b7a180d7d&X-Amz-SignedHeaders=host&x-id=GetObject)
### Motion Transfer
The "Everybody Dance Now" project demonstrates computer vision techniques for motion transfer. This project allows the dance moves of a person in a video to be transferred to another person, enabling the target to perform the same dance moves as the original subject.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e5b2060e-a889-4469-90bd-3920e03b6e3d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45FSPPWI6X%2F20250126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250126T101405Z&X-Amz-Expires=3600&X-Amz-Signature=de5e5895b6171b6a5afe1fac6811baac6c42a1b50ae9e65231eecca651f68c5f&X-Amz-SignedHeaders=host&x-id=GetObject)
### Summary
Recent research in computer vision includes advancements in object detection, image to image translation, and motion transfer. These innovations are enhancing the capabilities of computer vision systems and expanding their applications in various domains.
___
## Generating Ideas for Computer Vision Applications
### Introduction
This section encourages the exploration of potential computer vision applications by starting with existing problems and considering how computer vision can provide solutions.
### Identifying Existing Problems
Instead of beginning with a specific computer vision solution, it can be more effective to start by identifying problems that could be addressed. Here are some examples across various industries:
#### Medicine
One of the most challenging and time-consuming tasks in medicine is training doctors to accurately detect cancer. Developing computer vision tools that can assist in diagnosing cancer from medical images could help alleviate this problem.
#### Driving
Driving requires constant visual attention, and mistakes can have severe consequences. Additionally, long-distance drivers are at risk of falling asleep at the wheel. Computer vision could be used to develop systems that monitor driver alertness and provide warnings if necessary.
#### Security and Surveillance
In the security and surveillance industry, searching for a suspect across hours of footage is time-consuming. Computer vision can automate this process by efficiently identifying and tracking suspects. Additionally, detecting dangerous goods in X-rays at airports is challenging, and computer vision could improve the accuracy of these detections.
#### Manufacturing
In manufacturing, ensuring the quality of thousands of products is labor-intensive. Computer vision could be employed to automate quality control processes and detect defects in real-time.
#### Insurance and Work Safety
For insurance, evaluating damage from car accidents is a complex task that involves assessing the make, model, and year of the vehicle. Computer vision could streamline this process. Additionally, ensuring that construction workers wear appropriate safety gear is crucial for work safety, and computer vision can help in monitoring compliance.
### Personal and Everyday Problems
Consider problems you face in daily life or at work, and think about how computer vision could provide solutions:
- **Finding Receipts**: Computer vision could help in organizing and searching receipts for returns or exchanges.
- **Plant Identification**: Identify and track the growth of plants in your backyard using computer vision.
- **Rodent Problems**: Monitor and address rodent issues, such as raccoons rummaging through garbage bins.
### Summary
Exploring potential applications of computer vision involves identifying real-world problems and considering how technology can offer solutions. Think about challenges in your life, work, or industry to generate innovative ideas for computer vision applications.
___
