

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZW7JCHZ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHxHo3Y%2BQucv5xvnExIxFMSXJy9Kc3LjSn9ZDCQUoGkOAiBr0u908Q32Wa1AFRbCDxIIzRpjTaY1bnJ5XK7ZB6p7%2ByqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrjYuhbLm%2F2waNy9iKtwDiOomHB7xDeRouYsS4G8E8m2RGIkLjicSGCA0hzcJMSaTGxl2%2BKPVn6v32z6dfDDUW5atb2k1%2FGBQTQVH7sM6aUXgm3ipJBYoSBvuIvJZIUXA2hvdA9WjfyVlO6ASv%2BVZtcTubhJEm0T1KIXqZFyFObBta6b3RU%2BTwL%2BX9c9HnrXntLbhUlDzaGBqbsqgrSWLNN2cNIVzHD%2BIaXecXdHo4BGcUcXYBtNHI1vu5hYBtKx%2Fop%2BEDCIxnQ8lCcW41%2FRyvdlxEcNOFRUAQkCyR8I8A2fYCKM9Q6rcryZfmWgRr0%2FzWdVhQwmPl%2FHXZErr6d5SEKwrZ2d3zRnCvvuJNCcE3IWQkrwT8OnZMZrrBAIWFlS1%2B5Dz5roLardKSk%2Bxp%2B55GXqeXF1XHPsZtxPrSxRdi4hylMxg7bYy%2Bd9%2BFGERX2W6ssVBPYWTovetEKLjR0Q3jCq%2BUzRZ8qd3ph0o4WU5V%2FCQfqMfg14VcWto9XBTzktIWPflrkbJAdvaunnKNEOwd3EkxsmxWPZuRz7oazzMEPayNBJmdCOMQXld1KajnMA0pNbhBTWkna3Nvk5%2FC7H2vcG4gUj3nG0ZpkBgY5UMvNEOIkaqf7DykwZAt%2BsFrS%2FejZpbqkBIpHvuC%2Fsw0tv0vAY6pgGxe5nrY70I5mwK7mcL8XPs7Mh80mVQdOoNIhFp0bIvGXiidU6ve01i39HyKCQSL%2BHnPvS6i%2BQ%2FYSk4U9W8S8%2Bw0CZ8Up6Po9xPK5EcYMjnn8%2FLXYSdG5OVkj%2BuOIETcxP0nZ7jw4ypLGQhTMUep74g%2FymrUsLm3XqFL%2FAVHpmu9qWm2epwDn4wsCKZ8dViJW3M5Ce9vx1exHPNEFKCCksQY3K6r63f&X-Amz-Signature=58c824c43ba257f98b77fe1b1525e3cb65eb498068df906830a9b5976251553c&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XHL5GLQK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDuBD7zySHzrYygf50WvYw2LTXZIeen8yzpnDFl4aq5bwIhAO1RF8HV6OrHbqOG%2FWBfC0LGUDhJZYpX23kWUuLG8b95KogECMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxdBmoE9AYvBjsnmdcq3AM9YtXNK4%2BJXdZfJXBV3SuMHZ9a1T1X4kCwFjsCfKiHrWk0JZf5x1O3Jh9Cy2%2FeGdGkgwrsDqC1isneXXjMfOVVZEqC3RKRR6PCwQgQH3cgvrNG8wbebyMETQStb%2Bye9HNMiRFSceWPQUM7RYnGkcwQpw3thKZY0nC6h6VWr4r8nk%2BM%2B%2Be4QBImH1l3lcEvVMz1Zjg3lOcC1WofI%2B4NLrd2FAFaF8R34NUVZrkpcK7bzXSFbfXhT6Bhko4cR5FRqASEQfALEHNMTcJoUZwdPSBqcmlt%2BIdkrjTe1oYyRQuIjc3Y7f3LXdwNiuFbBtDxX00ERdMYernN0bfXaRagXX7kHqQ5Z94HsV%2B7BAi4VYDPzGgDooiykrATdXO38AIW7Tt4h4cRhxGHFN3X66c2uFe1oA2CzK34RwE%2Fs%2F%2FdbbkOf7lCmRJT1uPBFgAEtTBBWSLKeA90XfgvfisN3dl5RBqYwqE0UE1%2BcXrfV80iunoBGWq1685EAhQzndIiueOE3hv%2FCMkqHkjX1ZXI2D%2FONTjUvS43YmivpQ6D1n0iNJ%2F7yT7YNdHrWrCWdVq8Cm5yTIe5D4Ehul8iaP6iiM5EnTPhSaODn%2F7ntdWjOMGpZlSbPnkDPORN4J1Azl6MzTDR2%2FS8BjqkAfSfDc635e%2F4a1eXH8Y3G%2FXZRiT9fZPwbZUtGcKCpC%2BbqrToRcEKVvm5nJ5qeAUVlx1f%2FJPgTehyvqgBCK8aAKd0QU317vKnXvkCS6p7nzvYetqzPBun%2FWErjfXbzyrmJb82%2BMtefLAWJRS%2BrGERUqvwPRAaOmPLzE3mc2n04GxOQozIXx3F9ya9zfR1hYBZwtesWKqunZrAYxb4hnIPGpe2vtGP&X-Amz-Signature=dd9ae7a9bf16b6c60b8fc79a88b6bc0849c2730f68ecc0813ed52daaf60a0375&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XHL5GLQK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDuBD7zySHzrYygf50WvYw2LTXZIeen8yzpnDFl4aq5bwIhAO1RF8HV6OrHbqOG%2FWBfC0LGUDhJZYpX23kWUuLG8b95KogECMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxdBmoE9AYvBjsnmdcq3AM9YtXNK4%2BJXdZfJXBV3SuMHZ9a1T1X4kCwFjsCfKiHrWk0JZf5x1O3Jh9Cy2%2FeGdGkgwrsDqC1isneXXjMfOVVZEqC3RKRR6PCwQgQH3cgvrNG8wbebyMETQStb%2Bye9HNMiRFSceWPQUM7RYnGkcwQpw3thKZY0nC6h6VWr4r8nk%2BM%2B%2Be4QBImH1l3lcEvVMz1Zjg3lOcC1WofI%2B4NLrd2FAFaF8R34NUVZrkpcK7bzXSFbfXhT6Bhko4cR5FRqASEQfALEHNMTcJoUZwdPSBqcmlt%2BIdkrjTe1oYyRQuIjc3Y7f3LXdwNiuFbBtDxX00ERdMYernN0bfXaRagXX7kHqQ5Z94HsV%2B7BAi4VYDPzGgDooiykrATdXO38AIW7Tt4h4cRhxGHFN3X66c2uFe1oA2CzK34RwE%2Fs%2F%2FdbbkOf7lCmRJT1uPBFgAEtTBBWSLKeA90XfgvfisN3dl5RBqYwqE0UE1%2BcXrfV80iunoBGWq1685EAhQzndIiueOE3hv%2FCMkqHkjX1ZXI2D%2FONTjUvS43YmivpQ6D1n0iNJ%2F7yT7YNdHrWrCWdVq8Cm5yTIe5D4Ehul8iaP6iiM5EnTPhSaODn%2F7ntdWjOMGpZlSbPnkDPORN4J1Azl6MzTDR2%2FS8BjqkAfSfDc635e%2F4a1eXH8Y3G%2FXZRiT9fZPwbZUtGcKCpC%2BbqrToRcEKVvm5nJ5qeAUVlx1f%2FJPgTehyvqgBCK8aAKd0QU317vKnXvkCS6p7nzvYetqzPBun%2FWErjfXbzyrmJb82%2BMtefLAWJRS%2BrGERUqvwPRAaOmPLzE3mc2n04GxOQozIXx3F9ya9zfR1hYBZwtesWKqunZrAYxb4hnIPGpe2vtGP&X-Amz-Signature=c7311e52a88aad3e6bdd585e8f943d48171c3703e3d994047ecf93a22b3e76e4&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XHL5GLQK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDuBD7zySHzrYygf50WvYw2LTXZIeen8yzpnDFl4aq5bwIhAO1RF8HV6OrHbqOG%2FWBfC0LGUDhJZYpX23kWUuLG8b95KogECMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxdBmoE9AYvBjsnmdcq3AM9YtXNK4%2BJXdZfJXBV3SuMHZ9a1T1X4kCwFjsCfKiHrWk0JZf5x1O3Jh9Cy2%2FeGdGkgwrsDqC1isneXXjMfOVVZEqC3RKRR6PCwQgQH3cgvrNG8wbebyMETQStb%2Bye9HNMiRFSceWPQUM7RYnGkcwQpw3thKZY0nC6h6VWr4r8nk%2BM%2B%2Be4QBImH1l3lcEvVMz1Zjg3lOcC1WofI%2B4NLrd2FAFaF8R34NUVZrkpcK7bzXSFbfXhT6Bhko4cR5FRqASEQfALEHNMTcJoUZwdPSBqcmlt%2BIdkrjTe1oYyRQuIjc3Y7f3LXdwNiuFbBtDxX00ERdMYernN0bfXaRagXX7kHqQ5Z94HsV%2B7BAi4VYDPzGgDooiykrATdXO38AIW7Tt4h4cRhxGHFN3X66c2uFe1oA2CzK34RwE%2Fs%2F%2FdbbkOf7lCmRJT1uPBFgAEtTBBWSLKeA90XfgvfisN3dl5RBqYwqE0UE1%2BcXrfV80iunoBGWq1685EAhQzndIiueOE3hv%2FCMkqHkjX1ZXI2D%2FONTjUvS43YmivpQ6D1n0iNJ%2F7yT7YNdHrWrCWdVq8Cm5yTIe5D4Ehul8iaP6iiM5EnTPhSaODn%2F7ntdWjOMGpZlSbPnkDPORN4J1Azl6MzTDR2%2FS8BjqkAfSfDc635e%2F4a1eXH8Y3G%2FXZRiT9fZPwbZUtGcKCpC%2BbqrToRcEKVvm5nJ5qeAUVlx1f%2FJPgTehyvqgBCK8aAKd0QU317vKnXvkCS6p7nzvYetqzPBun%2FWErjfXbzyrmJb82%2BMtefLAWJRS%2BrGERUqvwPRAaOmPLzE3mc2n04GxOQozIXx3F9ya9zfR1hYBZwtesWKqunZrAYxb4hnIPGpe2vtGP&X-Amz-Signature=52e51f512756271bf80c210946599c6560cbf5d7bd200ec2704880d74b89f61d&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XHL5GLQK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDuBD7zySHzrYygf50WvYw2LTXZIeen8yzpnDFl4aq5bwIhAO1RF8HV6OrHbqOG%2FWBfC0LGUDhJZYpX23kWUuLG8b95KogECMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxdBmoE9AYvBjsnmdcq3AM9YtXNK4%2BJXdZfJXBV3SuMHZ9a1T1X4kCwFjsCfKiHrWk0JZf5x1O3Jh9Cy2%2FeGdGkgwrsDqC1isneXXjMfOVVZEqC3RKRR6PCwQgQH3cgvrNG8wbebyMETQStb%2Bye9HNMiRFSceWPQUM7RYnGkcwQpw3thKZY0nC6h6VWr4r8nk%2BM%2B%2Be4QBImH1l3lcEvVMz1Zjg3lOcC1WofI%2B4NLrd2FAFaF8R34NUVZrkpcK7bzXSFbfXhT6Bhko4cR5FRqASEQfALEHNMTcJoUZwdPSBqcmlt%2BIdkrjTe1oYyRQuIjc3Y7f3LXdwNiuFbBtDxX00ERdMYernN0bfXaRagXX7kHqQ5Z94HsV%2B7BAi4VYDPzGgDooiykrATdXO38AIW7Tt4h4cRhxGHFN3X66c2uFe1oA2CzK34RwE%2Fs%2F%2FdbbkOf7lCmRJT1uPBFgAEtTBBWSLKeA90XfgvfisN3dl5RBqYwqE0UE1%2BcXrfV80iunoBGWq1685EAhQzndIiueOE3hv%2FCMkqHkjX1ZXI2D%2FONTjUvS43YmivpQ6D1n0iNJ%2F7yT7YNdHrWrCWdVq8Cm5yTIe5D4Ehul8iaP6iiM5EnTPhSaODn%2F7ntdWjOMGpZlSbPnkDPORN4J1Azl6MzTDR2%2FS8BjqkAfSfDc635e%2F4a1eXH8Y3G%2FXZRiT9fZPwbZUtGcKCpC%2BbqrToRcEKVvm5nJ5qeAUVlx1f%2FJPgTehyvqgBCK8aAKd0QU317vKnXvkCS6p7nzvYetqzPBun%2FWErjfXbzyrmJb82%2BMtefLAWJRS%2BrGERUqvwPRAaOmPLzE3mc2n04GxOQozIXx3F9ya9zfR1hYBZwtesWKqunZrAYxb4hnIPGpe2vtGP&X-Amz-Signature=84c5f308776019a6aac94db84871f7644d411f7c92df589044c77a64bd4bd5d1&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XHL5GLQK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDuBD7zySHzrYygf50WvYw2LTXZIeen8yzpnDFl4aq5bwIhAO1RF8HV6OrHbqOG%2FWBfC0LGUDhJZYpX23kWUuLG8b95KogECMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxdBmoE9AYvBjsnmdcq3AM9YtXNK4%2BJXdZfJXBV3SuMHZ9a1T1X4kCwFjsCfKiHrWk0JZf5x1O3Jh9Cy2%2FeGdGkgwrsDqC1isneXXjMfOVVZEqC3RKRR6PCwQgQH3cgvrNG8wbebyMETQStb%2Bye9HNMiRFSceWPQUM7RYnGkcwQpw3thKZY0nC6h6VWr4r8nk%2BM%2B%2Be4QBImH1l3lcEvVMz1Zjg3lOcC1WofI%2B4NLrd2FAFaF8R34NUVZrkpcK7bzXSFbfXhT6Bhko4cR5FRqASEQfALEHNMTcJoUZwdPSBqcmlt%2BIdkrjTe1oYyRQuIjc3Y7f3LXdwNiuFbBtDxX00ERdMYernN0bfXaRagXX7kHqQ5Z94HsV%2B7BAi4VYDPzGgDooiykrATdXO38AIW7Tt4h4cRhxGHFN3X66c2uFe1oA2CzK34RwE%2Fs%2F%2FdbbkOf7lCmRJT1uPBFgAEtTBBWSLKeA90XfgvfisN3dl5RBqYwqE0UE1%2BcXrfV80iunoBGWq1685EAhQzndIiueOE3hv%2FCMkqHkjX1ZXI2D%2FONTjUvS43YmivpQ6D1n0iNJ%2F7yT7YNdHrWrCWdVq8Cm5yTIe5D4Ehul8iaP6iiM5EnTPhSaODn%2F7ntdWjOMGpZlSbPnkDPORN4J1Azl6MzTDR2%2FS8BjqkAfSfDc635e%2F4a1eXH8Y3G%2FXZRiT9fZPwbZUtGcKCpC%2BbqrToRcEKVvm5nJ5qeAUVlx1f%2FJPgTehyvqgBCK8aAKd0QU317vKnXvkCS6p7nzvYetqzPBun%2FWErjfXbzyrmJb82%2BMtefLAWJRS%2BrGERUqvwPRAaOmPLzE3mc2n04GxOQozIXx3F9ya9zfR1hYBZwtesWKqunZrAYxb4hnIPGpe2vtGP&X-Amz-Signature=99cef15d9c4ded01ff61ff21485079c6750f965a1faf18849ffdad0bc22b10ff&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZW7JCHZ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHxHo3Y%2BQucv5xvnExIxFMSXJy9Kc3LjSn9ZDCQUoGkOAiBr0u908Q32Wa1AFRbCDxIIzRpjTaY1bnJ5XK7ZB6p7%2ByqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrjYuhbLm%2F2waNy9iKtwDiOomHB7xDeRouYsS4G8E8m2RGIkLjicSGCA0hzcJMSaTGxl2%2BKPVn6v32z6dfDDUW5atb2k1%2FGBQTQVH7sM6aUXgm3ipJBYoSBvuIvJZIUXA2hvdA9WjfyVlO6ASv%2BVZtcTubhJEm0T1KIXqZFyFObBta6b3RU%2BTwL%2BX9c9HnrXntLbhUlDzaGBqbsqgrSWLNN2cNIVzHD%2BIaXecXdHo4BGcUcXYBtNHI1vu5hYBtKx%2Fop%2BEDCIxnQ8lCcW41%2FRyvdlxEcNOFRUAQkCyR8I8A2fYCKM9Q6rcryZfmWgRr0%2FzWdVhQwmPl%2FHXZErr6d5SEKwrZ2d3zRnCvvuJNCcE3IWQkrwT8OnZMZrrBAIWFlS1%2B5Dz5roLardKSk%2Bxp%2B55GXqeXF1XHPsZtxPrSxRdi4hylMxg7bYy%2Bd9%2BFGERX2W6ssVBPYWTovetEKLjR0Q3jCq%2BUzRZ8qd3ph0o4WU5V%2FCQfqMfg14VcWto9XBTzktIWPflrkbJAdvaunnKNEOwd3EkxsmxWPZuRz7oazzMEPayNBJmdCOMQXld1KajnMA0pNbhBTWkna3Nvk5%2FC7H2vcG4gUj3nG0ZpkBgY5UMvNEOIkaqf7DykwZAt%2BsFrS%2FejZpbqkBIpHvuC%2Fsw0tv0vAY6pgGxe5nrY70I5mwK7mcL8XPs7Mh80mVQdOoNIhFp0bIvGXiidU6ve01i39HyKCQSL%2BHnPvS6i%2BQ%2FYSk4U9W8S8%2Bw0CZ8Up6Po9xPK5EcYMjnn8%2FLXYSdG5OVkj%2BuOIETcxP0nZ7jw4ypLGQhTMUep74g%2FymrUsLm3XqFL%2FAVHpmu9qWm2epwDn4wsCKZ8dViJW3M5Ce9vx1exHPNEFKCCksQY3K6r63f&X-Amz-Signature=6dc46676a6c4d8de4714e9e66ca55891ca6e80d45193f7e3e7616132b81c6524&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZW7JCHZ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHxHo3Y%2BQucv5xvnExIxFMSXJy9Kc3LjSn9ZDCQUoGkOAiBr0u908Q32Wa1AFRbCDxIIzRpjTaY1bnJ5XK7ZB6p7%2ByqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrjYuhbLm%2F2waNy9iKtwDiOomHB7xDeRouYsS4G8E8m2RGIkLjicSGCA0hzcJMSaTGxl2%2BKPVn6v32z6dfDDUW5atb2k1%2FGBQTQVH7sM6aUXgm3ipJBYoSBvuIvJZIUXA2hvdA9WjfyVlO6ASv%2BVZtcTubhJEm0T1KIXqZFyFObBta6b3RU%2BTwL%2BX9c9HnrXntLbhUlDzaGBqbsqgrSWLNN2cNIVzHD%2BIaXecXdHo4BGcUcXYBtNHI1vu5hYBtKx%2Fop%2BEDCIxnQ8lCcW41%2FRyvdlxEcNOFRUAQkCyR8I8A2fYCKM9Q6rcryZfmWgRr0%2FzWdVhQwmPl%2FHXZErr6d5SEKwrZ2d3zRnCvvuJNCcE3IWQkrwT8OnZMZrrBAIWFlS1%2B5Dz5roLardKSk%2Bxp%2B55GXqeXF1XHPsZtxPrSxRdi4hylMxg7bYy%2Bd9%2BFGERX2W6ssVBPYWTovetEKLjR0Q3jCq%2BUzRZ8qd3ph0o4WU5V%2FCQfqMfg14VcWto9XBTzktIWPflrkbJAdvaunnKNEOwd3EkxsmxWPZuRz7oazzMEPayNBJmdCOMQXld1KajnMA0pNbhBTWkna3Nvk5%2FC7H2vcG4gUj3nG0ZpkBgY5UMvNEOIkaqf7DykwZAt%2BsFrS%2FejZpbqkBIpHvuC%2Fsw0tv0vAY6pgGxe5nrY70I5mwK7mcL8XPs7Mh80mVQdOoNIhFp0bIvGXiidU6ve01i39HyKCQSL%2BHnPvS6i%2BQ%2FYSk4U9W8S8%2Bw0CZ8Up6Po9xPK5EcYMjnn8%2FLXYSdG5OVkj%2BuOIETcxP0nZ7jw4ypLGQhTMUep74g%2FymrUsLm3XqFL%2FAVHpmu9qWm2epwDn4wsCKZ8dViJW3M5Ce9vx1exHPNEFKCCksQY3K6r63f&X-Amz-Signature=b83c8a11a0873b6f8a7d609226c6d76892955531a845d34df8a4be81b0e4636d&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZW7JCHZ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHxHo3Y%2BQucv5xvnExIxFMSXJy9Kc3LjSn9ZDCQUoGkOAiBr0u908Q32Wa1AFRbCDxIIzRpjTaY1bnJ5XK7ZB6p7%2ByqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrjYuhbLm%2F2waNy9iKtwDiOomHB7xDeRouYsS4G8E8m2RGIkLjicSGCA0hzcJMSaTGxl2%2BKPVn6v32z6dfDDUW5atb2k1%2FGBQTQVH7sM6aUXgm3ipJBYoSBvuIvJZIUXA2hvdA9WjfyVlO6ASv%2BVZtcTubhJEm0T1KIXqZFyFObBta6b3RU%2BTwL%2BX9c9HnrXntLbhUlDzaGBqbsqgrSWLNN2cNIVzHD%2BIaXecXdHo4BGcUcXYBtNHI1vu5hYBtKx%2Fop%2BEDCIxnQ8lCcW41%2FRyvdlxEcNOFRUAQkCyR8I8A2fYCKM9Q6rcryZfmWgRr0%2FzWdVhQwmPl%2FHXZErr6d5SEKwrZ2d3zRnCvvuJNCcE3IWQkrwT8OnZMZrrBAIWFlS1%2B5Dz5roLardKSk%2Bxp%2B55GXqeXF1XHPsZtxPrSxRdi4hylMxg7bYy%2Bd9%2BFGERX2W6ssVBPYWTovetEKLjR0Q3jCq%2BUzRZ8qd3ph0o4WU5V%2FCQfqMfg14VcWto9XBTzktIWPflrkbJAdvaunnKNEOwd3EkxsmxWPZuRz7oazzMEPayNBJmdCOMQXld1KajnMA0pNbhBTWkna3Nvk5%2FC7H2vcG4gUj3nG0ZpkBgY5UMvNEOIkaqf7DykwZAt%2BsFrS%2FejZpbqkBIpHvuC%2Fsw0tv0vAY6pgGxe5nrY70I5mwK7mcL8XPs7Mh80mVQdOoNIhFp0bIvGXiidU6ve01i39HyKCQSL%2BHnPvS6i%2BQ%2FYSk4U9W8S8%2Bw0CZ8Up6Po9xPK5EcYMjnn8%2FLXYSdG5OVkj%2BuOIETcxP0nZ7jw4ypLGQhTMUep74g%2FymrUsLm3XqFL%2FAVHpmu9qWm2epwDn4wsCKZ8dViJW3M5Ce9vx1exHPNEFKCCksQY3K6r63f&X-Amz-Signature=1960a27011d439a89d2d8044c0a0133d0b42be7f56cba31970305b380f876f23&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZW7JCHZ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHxHo3Y%2BQucv5xvnExIxFMSXJy9Kc3LjSn9ZDCQUoGkOAiBr0u908Q32Wa1AFRbCDxIIzRpjTaY1bnJ5XK7ZB6p7%2ByqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrjYuhbLm%2F2waNy9iKtwDiOomHB7xDeRouYsS4G8E8m2RGIkLjicSGCA0hzcJMSaTGxl2%2BKPVn6v32z6dfDDUW5atb2k1%2FGBQTQVH7sM6aUXgm3ipJBYoSBvuIvJZIUXA2hvdA9WjfyVlO6ASv%2BVZtcTubhJEm0T1KIXqZFyFObBta6b3RU%2BTwL%2BX9c9HnrXntLbhUlDzaGBqbsqgrSWLNN2cNIVzHD%2BIaXecXdHo4BGcUcXYBtNHI1vu5hYBtKx%2Fop%2BEDCIxnQ8lCcW41%2FRyvdlxEcNOFRUAQkCyR8I8A2fYCKM9Q6rcryZfmWgRr0%2FzWdVhQwmPl%2FHXZErr6d5SEKwrZ2d3zRnCvvuJNCcE3IWQkrwT8OnZMZrrBAIWFlS1%2B5Dz5roLardKSk%2Bxp%2B55GXqeXF1XHPsZtxPrSxRdi4hylMxg7bYy%2Bd9%2BFGERX2W6ssVBPYWTovetEKLjR0Q3jCq%2BUzRZ8qd3ph0o4WU5V%2FCQfqMfg14VcWto9XBTzktIWPflrkbJAdvaunnKNEOwd3EkxsmxWPZuRz7oazzMEPayNBJmdCOMQXld1KajnMA0pNbhBTWkna3Nvk5%2FC7H2vcG4gUj3nG0ZpkBgY5UMvNEOIkaqf7DykwZAt%2BsFrS%2FejZpbqkBIpHvuC%2Fsw0tv0vAY6pgGxe5nrY70I5mwK7mcL8XPs7Mh80mVQdOoNIhFp0bIvGXiidU6ve01i39HyKCQSL%2BHnPvS6i%2BQ%2FYSk4U9W8S8%2Bw0CZ8Up6Po9xPK5EcYMjnn8%2FLXYSdG5OVkj%2BuOIETcxP0nZ7jw4ypLGQhTMUep74g%2FymrUsLm3XqFL%2FAVHpmu9qWm2epwDn4wsCKZ8dViJW3M5Ce9vx1exHPNEFKCCksQY3K6r63f&X-Amz-Signature=2aea29f7271285628949df5358f7c2b40ace5a86fc98179a1e16047b9956cfbb&X-Amz-SignedHeaders=host&x-id=GetObject)
### Video Sequences
A **video** can be viewed as a sequence of multiple **images** or **frames**.
### Image Formats
Common image file formats include:
- **JPEG** (Joint Photographic Expert Group)
- **PNG** (Portable Network Graphics)
These formats compress and reduce file sizes while maintaining image quality.
### Image Processing Libraries in Python
#### Pillow (PIL)
Pillow is a widely used Python library for image manipulation.
- To load an image:
```python
from PIL import Image
img = Image.open('image.png')
```
- **Attributes** of a Pillow image:
	- `format`: The file format (e.g., PNG, JPEG).
	- `size`: The dimensions of the image (width x height).
	- `mode`: The color space (e.g., RGB, L for grayscale).
#### Example: Converting to Gray-Scale
- Convert an image to **gray-scale**:
```python
gray_img = img.convert('L')
gray_img.show()
```
#### Example: Quantization
- **Quantize** an image to reduce the number of intensity levels:
```python
quantized_img = img.quantize(colors=16)
quantized_img.show()
```
#### OpenCV
**OpenCV** is a powerful library for **computer vision** with more functionality than PIL.
- Import OpenCV:
```python
import cv2
```
- Load an image:
```python
img = cv2.imread('image.png')
```
- **Attributes** of an OpenCV image:
	- OpenCV represents images as **NumPy arrays**.
	- The **color channels** are ordered as **BGR** (blue, green, red) instead of **RGB**.
#### Example: Color Space Conversion
- Convert from **BGR to RGB**:
```python
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
```
- Convert to **gray-scale**:
```python
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
```
#### Example: Saving an Image
- Save an image using OpenCV:
```python
cv2.imwrite('output.png', img)
```
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZW7JCHZ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHxHo3Y%2BQucv5xvnExIxFMSXJy9Kc3LjSn9ZDCQUoGkOAiBr0u908Q32Wa1AFRbCDxIIzRpjTaY1bnJ5XK7ZB6p7%2ByqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrjYuhbLm%2F2waNy9iKtwDiOomHB7xDeRouYsS4G8E8m2RGIkLjicSGCA0hzcJMSaTGxl2%2BKPVn6v32z6dfDDUW5atb2k1%2FGBQTQVH7sM6aUXgm3ipJBYoSBvuIvJZIUXA2hvdA9WjfyVlO6ASv%2BVZtcTubhJEm0T1KIXqZFyFObBta6b3RU%2BTwL%2BX9c9HnrXntLbhUlDzaGBqbsqgrSWLNN2cNIVzHD%2BIaXecXdHo4BGcUcXYBtNHI1vu5hYBtKx%2Fop%2BEDCIxnQ8lCcW41%2FRyvdlxEcNOFRUAQkCyR8I8A2fYCKM9Q6rcryZfmWgRr0%2FzWdVhQwmPl%2FHXZErr6d5SEKwrZ2d3zRnCvvuJNCcE3IWQkrwT8OnZMZrrBAIWFlS1%2B5Dz5roLardKSk%2Bxp%2B55GXqeXF1XHPsZtxPrSxRdi4hylMxg7bYy%2Bd9%2BFGERX2W6ssVBPYWTovetEKLjR0Q3jCq%2BUzRZ8qd3ph0o4WU5V%2FCQfqMfg14VcWto9XBTzktIWPflrkbJAdvaunnKNEOwd3EkxsmxWPZuRz7oazzMEPayNBJmdCOMQXld1KajnMA0pNbhBTWkna3Nvk5%2FC7H2vcG4gUj3nG0ZpkBgY5UMvNEOIkaqf7DykwZAt%2BsFrS%2FejZpbqkBIpHvuC%2Fsw0tv0vAY6pgGxe5nrY70I5mwK7mcL8XPs7Mh80mVQdOoNIhFp0bIvGXiidU6ve01i39HyKCQSL%2BHnPvS6i%2BQ%2FYSk4U9W8S8%2Bw0CZ8Up6Po9xPK5EcYMjnn8%2FLXYSdG5OVkj%2BuOIETcxP0nZ7jw4ypLGQhTMUep74g%2FymrUsLm3XqFL%2FAVHpmu9qWm2epwDn4wsCKZ8dViJW3M5Ce9vx1exHPNEFKCCksQY3K6r63f&X-Amz-Signature=04a82a14c7a888e4d0c898692c36c8426fe47d55554ff29e373b4df1416b702a&X-Amz-SignedHeaders=host&x-id=GetObject)
### Working with Color Channels
Using **slices**, individual color channels (e.g., **blue**, **green**, **red**) can be extracted:
```python
blue_channel = img[:, :, 0]
green_channel = img[:, :, 1]
red_channel = img[:, :, 2]
```
Each channel can then be processed or analyzed separately.
#### Conversion between PIL and NumPy Arrays
PIL images can be easily converted to **NumPy arrays** for further processing:
```python
import numpy as np
np_img = np.array(img)
```
This conversion is particularly useful when integrating with **OpenCV** and performing advanced operations.
### Conclusion
Both **PIL** and **OpenCV** are essential tools for handling and processing digital images in Python. Each has its strengths:
- **PIL** is simple and great for basic tasks.
- **OpenCV** offers more advanced capabilities for **computer vision** applications.
___


