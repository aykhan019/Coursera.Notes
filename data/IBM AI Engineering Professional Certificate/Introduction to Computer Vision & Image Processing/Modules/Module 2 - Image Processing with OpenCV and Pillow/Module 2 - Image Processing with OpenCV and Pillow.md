

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XW7VC6OC%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGZKiJneanxjR4nw%2FgRaD9blc6Jyu%2F1cCgcL5pfedW%2F7AiEA%2FmOO7zsUdztMOoKk2tOaBFnF1Mb3JBFXJh2b8SSTjPUqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIg4DKEleatnu38LOyrcA4G0WmrmqESDmDH0GJlMe%2FRyTeID3RRS8RsqvvB6hdb%2FnEn6P2yWSXNLuOC9hUg1h%2BkCs8mFjhXFbyvnL1rO%2BhkmKTP7ZzCwsGvZf01G8qGnst0pezpH3nFbved8eE7SO7UXqO3EqUzJqEcZg8yJSFPfhnr%2Fn5rVzm739IMl1T2iliami65r8Jkq1YtsGv49Gsaj5u1rc3hZ48p2ILP4QnZzVHvyuEcAVjDBkOxfgT6aMP0hCgddXNNmMQR%2BFBtIIFhEr6mwlGJjVC7sc95%2FcPzgrWaT9khb%2B%2F4bXclK%2FBQBMXrSQxZBMbbva1GQglJrJ08fHo9dsvipW%2FClEWi9AIU95vI1G%2B7Msxk1brELw3PaMceVuJ12cZ6u9Pm16wQSFqjmWvMA5XFUHe2mjMVUreqzIP2KG4BYax8abIqSA%2B1Nc73MMegKbm%2BkFhySnD8r2YxnV0%2BeeklsBCcB%2B3W4t%2BVcHHyJ%2F5ixJwy8ROH4kRN2%2FMzLVa7UICpDIsHQaqxnrrNS%2Boyp%2FQywOQh%2BOIGFsvkpVdkC8Lsft2nFK9f%2BSAyrKX%2FnvqbqDasQ2hiRqx1GGkZHXZSArhape%2FvdaBg6GvAXjEvCQsam83onOFc1Lx4abygAZ1HxZzZ%2FJRX5MIef%2B7wGOqUBKxZPs%2BbNJYgeUth6LpCx%2FFLnrxLYgkNwO7DNaoKa%2Fc2WP1ZQDv1UGMZlRU7n%2BsPXVaNNi86tLwT2arwqTc7TwOe4JSwXBusvp1VFcZb2X%2BpciaVvdOJPPHj80bMojQN%2FISzLuceKaXsLtGiOQWzF4PrAm0dogExFVQNYWilx9nYC57Emjml75buKkcuLwnaP3RHMRgDF3Tc9BxbvN%2F4XbtFkrUbx&X-Amz-Signature=f842fcf8f8b92ffe76861c53eb7d3c639fc067492cde8a154087fb9bfba8c8f6&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QYCRGZCO%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCV2uKrfSIEoF5re53bLvipF9tnA%2FsIZ0iwx5njZGfa%2BgIgQ%2BYgvBp8Rg7%2FbkVUE4DhL1P2xQICqnhlIaXVOgGX6IoqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIhKfi7A6j8MMtutrircA9A2U6QUi%2Fw0WDjcFjCBhYLLis9h5%2BeNCJBk835G5Q6Dzidcnc%2B84iSrtSxmJUr9W0kSh%2F5VSzBonRsXLColyT%2F9CSMms4F4aERWQc0JHomQF0rp3NXQNFXKF7QYRVRxPhz7eXLuRVR1yjlqejdPwp0LXPoGk3gES8u3kA0MhcbrZ136hYEVvG%2BEdUt53Wptq9UR1bVevUFpRQRaGhUljv7ghrKiRVUHOLNyFt9LGoVrXWQOO4AYv9CzTvVFWqFor%2FbMetsG1aRrlcbcmzQ82yZhySurjmv6Ii2uXswH15q%2B5U6%2FD8Suisu%2FJW2rpo5wxZhUJl%2FXoct%2FVg7FM4ql%2F%2FwePGeYCesZtLQna1%2FDCV16a0NoYxthBLtBNHllnM3qV49OEOqtONci1vU%2FagSYMyXC4N2Td9fL%2BS2I%2B4BlriMk5pfqC2uJvMJw7K8gt6BH%2Fz1z2Rg0Tw0b6jl2brmc7en6O1RmpDAKwFbUXk0GeQXbV9pXySjTVbA4hpo5VBFHTXr%2FA5UdNMC7vaBiUPmZofIPaA3ZzhYE1rNLRTHPo1gau56RqBeBbPvehgHblocPuxLfDGMQm4z9riRo7zGkp00cEXLnAH3f8b1So1lSVAEzehoksNwtsN%2B0HBTBMNOe%2B7wGOqUBPKH69Ly3HOQ9lyaze3rE%2FCp9ivBA939n6iMYIetaJLzzPLeHitu7SaBrjLVl6F88PQhbCcRsK5tWbTNTpu0ctJsmf3oRVQyQcYTZ0Z4CEGvpuFVxvpPn2GllSdYqVvrk%2Fg4tOAb8m8DoUTNTQuf9BFDerQwb9g2yTLZQoTes7qVDRg5WZ0oFdnuXMOrXa8BsOB6XVfIhF70%2FwiucLaCs53ccdXFp&X-Amz-Signature=065154791eb6913ecfaacc5470b004e32b1c739ec06faabf3272de484e7dc22a&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QYCRGZCO%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCV2uKrfSIEoF5re53bLvipF9tnA%2FsIZ0iwx5njZGfa%2BgIgQ%2BYgvBp8Rg7%2FbkVUE4DhL1P2xQICqnhlIaXVOgGX6IoqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIhKfi7A6j8MMtutrircA9A2U6QUi%2Fw0WDjcFjCBhYLLis9h5%2BeNCJBk835G5Q6Dzidcnc%2B84iSrtSxmJUr9W0kSh%2F5VSzBonRsXLColyT%2F9CSMms4F4aERWQc0JHomQF0rp3NXQNFXKF7QYRVRxPhz7eXLuRVR1yjlqejdPwp0LXPoGk3gES8u3kA0MhcbrZ136hYEVvG%2BEdUt53Wptq9UR1bVevUFpRQRaGhUljv7ghrKiRVUHOLNyFt9LGoVrXWQOO4AYv9CzTvVFWqFor%2FbMetsG1aRrlcbcmzQ82yZhySurjmv6Ii2uXswH15q%2B5U6%2FD8Suisu%2FJW2rpo5wxZhUJl%2FXoct%2FVg7FM4ql%2F%2FwePGeYCesZtLQna1%2FDCV16a0NoYxthBLtBNHllnM3qV49OEOqtONci1vU%2FagSYMyXC4N2Td9fL%2BS2I%2B4BlriMk5pfqC2uJvMJw7K8gt6BH%2Fz1z2Rg0Tw0b6jl2brmc7en6O1RmpDAKwFbUXk0GeQXbV9pXySjTVbA4hpo5VBFHTXr%2FA5UdNMC7vaBiUPmZofIPaA3ZzhYE1rNLRTHPo1gau56RqBeBbPvehgHblocPuxLfDGMQm4z9riRo7zGkp00cEXLnAH3f8b1So1lSVAEzehoksNwtsN%2B0HBTBMNOe%2B7wGOqUBPKH69Ly3HOQ9lyaze3rE%2FCp9ivBA939n6iMYIetaJLzzPLeHitu7SaBrjLVl6F88PQhbCcRsK5tWbTNTpu0ctJsmf3oRVQyQcYTZ0Z4CEGvpuFVxvpPn2GllSdYqVvrk%2Fg4tOAb8m8DoUTNTQuf9BFDerQwb9g2yTLZQoTes7qVDRg5WZ0oFdnuXMOrXa8BsOB6XVfIhF70%2FwiucLaCs53ccdXFp&X-Amz-Signature=02fadf3b3d2933d790f669ed2df651ab6f8e47e3acfa4ec559c281dc33daf2e2&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QYCRGZCO%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCV2uKrfSIEoF5re53bLvipF9tnA%2FsIZ0iwx5njZGfa%2BgIgQ%2BYgvBp8Rg7%2FbkVUE4DhL1P2xQICqnhlIaXVOgGX6IoqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIhKfi7A6j8MMtutrircA9A2U6QUi%2Fw0WDjcFjCBhYLLis9h5%2BeNCJBk835G5Q6Dzidcnc%2B84iSrtSxmJUr9W0kSh%2F5VSzBonRsXLColyT%2F9CSMms4F4aERWQc0JHomQF0rp3NXQNFXKF7QYRVRxPhz7eXLuRVR1yjlqejdPwp0LXPoGk3gES8u3kA0MhcbrZ136hYEVvG%2BEdUt53Wptq9UR1bVevUFpRQRaGhUljv7ghrKiRVUHOLNyFt9LGoVrXWQOO4AYv9CzTvVFWqFor%2FbMetsG1aRrlcbcmzQ82yZhySurjmv6Ii2uXswH15q%2B5U6%2FD8Suisu%2FJW2rpo5wxZhUJl%2FXoct%2FVg7FM4ql%2F%2FwePGeYCesZtLQna1%2FDCV16a0NoYxthBLtBNHllnM3qV49OEOqtONci1vU%2FagSYMyXC4N2Td9fL%2BS2I%2B4BlriMk5pfqC2uJvMJw7K8gt6BH%2Fz1z2Rg0Tw0b6jl2brmc7en6O1RmpDAKwFbUXk0GeQXbV9pXySjTVbA4hpo5VBFHTXr%2FA5UdNMC7vaBiUPmZofIPaA3ZzhYE1rNLRTHPo1gau56RqBeBbPvehgHblocPuxLfDGMQm4z9riRo7zGkp00cEXLnAH3f8b1So1lSVAEzehoksNwtsN%2B0HBTBMNOe%2B7wGOqUBPKH69Ly3HOQ9lyaze3rE%2FCp9ivBA939n6iMYIetaJLzzPLeHitu7SaBrjLVl6F88PQhbCcRsK5tWbTNTpu0ctJsmf3oRVQyQcYTZ0Z4CEGvpuFVxvpPn2GllSdYqVvrk%2Fg4tOAb8m8DoUTNTQuf9BFDerQwb9g2yTLZQoTes7qVDRg5WZ0oFdnuXMOrXa8BsOB6XVfIhF70%2FwiucLaCs53ccdXFp&X-Amz-Signature=2765a286cab2b32d28f23b448756a93644e034ff295551624b896bc3bc4d051c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QYCRGZCO%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCV2uKrfSIEoF5re53bLvipF9tnA%2FsIZ0iwx5njZGfa%2BgIgQ%2BYgvBp8Rg7%2FbkVUE4DhL1P2xQICqnhlIaXVOgGX6IoqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIhKfi7A6j8MMtutrircA9A2U6QUi%2Fw0WDjcFjCBhYLLis9h5%2BeNCJBk835G5Q6Dzidcnc%2B84iSrtSxmJUr9W0kSh%2F5VSzBonRsXLColyT%2F9CSMms4F4aERWQc0JHomQF0rp3NXQNFXKF7QYRVRxPhz7eXLuRVR1yjlqejdPwp0LXPoGk3gES8u3kA0MhcbrZ136hYEVvG%2BEdUt53Wptq9UR1bVevUFpRQRaGhUljv7ghrKiRVUHOLNyFt9LGoVrXWQOO4AYv9CzTvVFWqFor%2FbMetsG1aRrlcbcmzQ82yZhySurjmv6Ii2uXswH15q%2B5U6%2FD8Suisu%2FJW2rpo5wxZhUJl%2FXoct%2FVg7FM4ql%2F%2FwePGeYCesZtLQna1%2FDCV16a0NoYxthBLtBNHllnM3qV49OEOqtONci1vU%2FagSYMyXC4N2Td9fL%2BS2I%2B4BlriMk5pfqC2uJvMJw7K8gt6BH%2Fz1z2Rg0Tw0b6jl2brmc7en6O1RmpDAKwFbUXk0GeQXbV9pXySjTVbA4hpo5VBFHTXr%2FA5UdNMC7vaBiUPmZofIPaA3ZzhYE1rNLRTHPo1gau56RqBeBbPvehgHblocPuxLfDGMQm4z9riRo7zGkp00cEXLnAH3f8b1So1lSVAEzehoksNwtsN%2B0HBTBMNOe%2B7wGOqUBPKH69Ly3HOQ9lyaze3rE%2FCp9ivBA939n6iMYIetaJLzzPLeHitu7SaBrjLVl6F88PQhbCcRsK5tWbTNTpu0ctJsmf3oRVQyQcYTZ0Z4CEGvpuFVxvpPn2GllSdYqVvrk%2Fg4tOAb8m8DoUTNTQuf9BFDerQwb9g2yTLZQoTes7qVDRg5WZ0oFdnuXMOrXa8BsOB6XVfIhF70%2FwiucLaCs53ccdXFp&X-Amz-Signature=739391b3a85f83cd684457442df6d83200eafba56c8d5c996949091e67dbe0ed&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QYCRGZCO%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCV2uKrfSIEoF5re53bLvipF9tnA%2FsIZ0iwx5njZGfa%2BgIgQ%2BYgvBp8Rg7%2FbkVUE4DhL1P2xQICqnhlIaXVOgGX6IoqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIhKfi7A6j8MMtutrircA9A2U6QUi%2Fw0WDjcFjCBhYLLis9h5%2BeNCJBk835G5Q6Dzidcnc%2B84iSrtSxmJUr9W0kSh%2F5VSzBonRsXLColyT%2F9CSMms4F4aERWQc0JHomQF0rp3NXQNFXKF7QYRVRxPhz7eXLuRVR1yjlqejdPwp0LXPoGk3gES8u3kA0MhcbrZ136hYEVvG%2BEdUt53Wptq9UR1bVevUFpRQRaGhUljv7ghrKiRVUHOLNyFt9LGoVrXWQOO4AYv9CzTvVFWqFor%2FbMetsG1aRrlcbcmzQ82yZhySurjmv6Ii2uXswH15q%2B5U6%2FD8Suisu%2FJW2rpo5wxZhUJl%2FXoct%2FVg7FM4ql%2F%2FwePGeYCesZtLQna1%2FDCV16a0NoYxthBLtBNHllnM3qV49OEOqtONci1vU%2FagSYMyXC4N2Td9fL%2BS2I%2B4BlriMk5pfqC2uJvMJw7K8gt6BH%2Fz1z2Rg0Tw0b6jl2brmc7en6O1RmpDAKwFbUXk0GeQXbV9pXySjTVbA4hpo5VBFHTXr%2FA5UdNMC7vaBiUPmZofIPaA3ZzhYE1rNLRTHPo1gau56RqBeBbPvehgHblocPuxLfDGMQm4z9riRo7zGkp00cEXLnAH3f8b1So1lSVAEzehoksNwtsN%2B0HBTBMNOe%2B7wGOqUBPKH69Ly3HOQ9lyaze3rE%2FCp9ivBA939n6iMYIetaJLzzPLeHitu7SaBrjLVl6F88PQhbCcRsK5tWbTNTpu0ctJsmf3oRVQyQcYTZ0Z4CEGvpuFVxvpPn2GllSdYqVvrk%2Fg4tOAb8m8DoUTNTQuf9BFDerQwb9g2yTLZQoTes7qVDRg5WZ0oFdnuXMOrXa8BsOB6XVfIhF70%2FwiucLaCs53ccdXFp&X-Amz-Signature=4a8e9a879e8dc105b34cd1609e206d18c44e15c647f6d6afd4ce54421720e563&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XW7VC6OC%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGZKiJneanxjR4nw%2FgRaD9blc6Jyu%2F1cCgcL5pfedW%2F7AiEA%2FmOO7zsUdztMOoKk2tOaBFnF1Mb3JBFXJh2b8SSTjPUqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIg4DKEleatnu38LOyrcA4G0WmrmqESDmDH0GJlMe%2FRyTeID3RRS8RsqvvB6hdb%2FnEn6P2yWSXNLuOC9hUg1h%2BkCs8mFjhXFbyvnL1rO%2BhkmKTP7ZzCwsGvZf01G8qGnst0pezpH3nFbved8eE7SO7UXqO3EqUzJqEcZg8yJSFPfhnr%2Fn5rVzm739IMl1T2iliami65r8Jkq1YtsGv49Gsaj5u1rc3hZ48p2ILP4QnZzVHvyuEcAVjDBkOxfgT6aMP0hCgddXNNmMQR%2BFBtIIFhEr6mwlGJjVC7sc95%2FcPzgrWaT9khb%2B%2F4bXclK%2FBQBMXrSQxZBMbbva1GQglJrJ08fHo9dsvipW%2FClEWi9AIU95vI1G%2B7Msxk1brELw3PaMceVuJ12cZ6u9Pm16wQSFqjmWvMA5XFUHe2mjMVUreqzIP2KG4BYax8abIqSA%2B1Nc73MMegKbm%2BkFhySnD8r2YxnV0%2BeeklsBCcB%2B3W4t%2BVcHHyJ%2F5ixJwy8ROH4kRN2%2FMzLVa7UICpDIsHQaqxnrrNS%2Boyp%2FQywOQh%2BOIGFsvkpVdkC8Lsft2nFK9f%2BSAyrKX%2FnvqbqDasQ2hiRqx1GGkZHXZSArhape%2FvdaBg6GvAXjEvCQsam83onOFc1Lx4abygAZ1HxZzZ%2FJRX5MIef%2B7wGOqUBKxZPs%2BbNJYgeUth6LpCx%2FFLnrxLYgkNwO7DNaoKa%2Fc2WP1ZQDv1UGMZlRU7n%2BsPXVaNNi86tLwT2arwqTc7TwOe4JSwXBusvp1VFcZb2X%2BpciaVvdOJPPHj80bMojQN%2FISzLuceKaXsLtGiOQWzF4PrAm0dogExFVQNYWilx9nYC57Emjml75buKkcuLwnaP3RHMRgDF3Tc9BxbvN%2F4XbtFkrUbx&X-Amz-Signature=5f1c8b6decdbc1da37bd482207a210d81ed1c611735ad1dbd1dd58b3f3a33360&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XW7VC6OC%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGZKiJneanxjR4nw%2FgRaD9blc6Jyu%2F1cCgcL5pfedW%2F7AiEA%2FmOO7zsUdztMOoKk2tOaBFnF1Mb3JBFXJh2b8SSTjPUqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIg4DKEleatnu38LOyrcA4G0WmrmqESDmDH0GJlMe%2FRyTeID3RRS8RsqvvB6hdb%2FnEn6P2yWSXNLuOC9hUg1h%2BkCs8mFjhXFbyvnL1rO%2BhkmKTP7ZzCwsGvZf01G8qGnst0pezpH3nFbved8eE7SO7UXqO3EqUzJqEcZg8yJSFPfhnr%2Fn5rVzm739IMl1T2iliami65r8Jkq1YtsGv49Gsaj5u1rc3hZ48p2ILP4QnZzVHvyuEcAVjDBkOxfgT6aMP0hCgddXNNmMQR%2BFBtIIFhEr6mwlGJjVC7sc95%2FcPzgrWaT9khb%2B%2F4bXclK%2FBQBMXrSQxZBMbbva1GQglJrJ08fHo9dsvipW%2FClEWi9AIU95vI1G%2B7Msxk1brELw3PaMceVuJ12cZ6u9Pm16wQSFqjmWvMA5XFUHe2mjMVUreqzIP2KG4BYax8abIqSA%2B1Nc73MMegKbm%2BkFhySnD8r2YxnV0%2BeeklsBCcB%2B3W4t%2BVcHHyJ%2F5ixJwy8ROH4kRN2%2FMzLVa7UICpDIsHQaqxnrrNS%2Boyp%2FQywOQh%2BOIGFsvkpVdkC8Lsft2nFK9f%2BSAyrKX%2FnvqbqDasQ2hiRqx1GGkZHXZSArhape%2FvdaBg6GvAXjEvCQsam83onOFc1Lx4abygAZ1HxZzZ%2FJRX5MIef%2B7wGOqUBKxZPs%2BbNJYgeUth6LpCx%2FFLnrxLYgkNwO7DNaoKa%2Fc2WP1ZQDv1UGMZlRU7n%2BsPXVaNNi86tLwT2arwqTc7TwOe4JSwXBusvp1VFcZb2X%2BpciaVvdOJPPHj80bMojQN%2FISzLuceKaXsLtGiOQWzF4PrAm0dogExFVQNYWilx9nYC57Emjml75buKkcuLwnaP3RHMRgDF3Tc9BxbvN%2F4XbtFkrUbx&X-Amz-Signature=8949f75ef5d3bcc3f717d3759dd33a5e38eca4396ab414c24805968e8b96cc38&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XW7VC6OC%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGZKiJneanxjR4nw%2FgRaD9blc6Jyu%2F1cCgcL5pfedW%2F7AiEA%2FmOO7zsUdztMOoKk2tOaBFnF1Mb3JBFXJh2b8SSTjPUqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIg4DKEleatnu38LOyrcA4G0WmrmqESDmDH0GJlMe%2FRyTeID3RRS8RsqvvB6hdb%2FnEn6P2yWSXNLuOC9hUg1h%2BkCs8mFjhXFbyvnL1rO%2BhkmKTP7ZzCwsGvZf01G8qGnst0pezpH3nFbved8eE7SO7UXqO3EqUzJqEcZg8yJSFPfhnr%2Fn5rVzm739IMl1T2iliami65r8Jkq1YtsGv49Gsaj5u1rc3hZ48p2ILP4QnZzVHvyuEcAVjDBkOxfgT6aMP0hCgddXNNmMQR%2BFBtIIFhEr6mwlGJjVC7sc95%2FcPzgrWaT9khb%2B%2F4bXclK%2FBQBMXrSQxZBMbbva1GQglJrJ08fHo9dsvipW%2FClEWi9AIU95vI1G%2B7Msxk1brELw3PaMceVuJ12cZ6u9Pm16wQSFqjmWvMA5XFUHe2mjMVUreqzIP2KG4BYax8abIqSA%2B1Nc73MMegKbm%2BkFhySnD8r2YxnV0%2BeeklsBCcB%2B3W4t%2BVcHHyJ%2F5ixJwy8ROH4kRN2%2FMzLVa7UICpDIsHQaqxnrrNS%2Boyp%2FQywOQh%2BOIGFsvkpVdkC8Lsft2nFK9f%2BSAyrKX%2FnvqbqDasQ2hiRqx1GGkZHXZSArhape%2FvdaBg6GvAXjEvCQsam83onOFc1Lx4abygAZ1HxZzZ%2FJRX5MIef%2B7wGOqUBKxZPs%2BbNJYgeUth6LpCx%2FFLnrxLYgkNwO7DNaoKa%2Fc2WP1ZQDv1UGMZlRU7n%2BsPXVaNNi86tLwT2arwqTc7TwOe4JSwXBusvp1VFcZb2X%2BpciaVvdOJPPHj80bMojQN%2FISzLuceKaXsLtGiOQWzF4PrAm0dogExFVQNYWilx9nYC57Emjml75buKkcuLwnaP3RHMRgDF3Tc9BxbvN%2F4XbtFkrUbx&X-Amz-Signature=7b9bcafdfc6345692bb1f832c0ec405d8ff2fb8a44bbb1bedeb6e6c897d6089e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XW7VC6OC%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGZKiJneanxjR4nw%2FgRaD9blc6Jyu%2F1cCgcL5pfedW%2F7AiEA%2FmOO7zsUdztMOoKk2tOaBFnF1Mb3JBFXJh2b8SSTjPUqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIg4DKEleatnu38LOyrcA4G0WmrmqESDmDH0GJlMe%2FRyTeID3RRS8RsqvvB6hdb%2FnEn6P2yWSXNLuOC9hUg1h%2BkCs8mFjhXFbyvnL1rO%2BhkmKTP7ZzCwsGvZf01G8qGnst0pezpH3nFbved8eE7SO7UXqO3EqUzJqEcZg8yJSFPfhnr%2Fn5rVzm739IMl1T2iliami65r8Jkq1YtsGv49Gsaj5u1rc3hZ48p2ILP4QnZzVHvyuEcAVjDBkOxfgT6aMP0hCgddXNNmMQR%2BFBtIIFhEr6mwlGJjVC7sc95%2FcPzgrWaT9khb%2B%2F4bXclK%2FBQBMXrSQxZBMbbva1GQglJrJ08fHo9dsvipW%2FClEWi9AIU95vI1G%2B7Msxk1brELw3PaMceVuJ12cZ6u9Pm16wQSFqjmWvMA5XFUHe2mjMVUreqzIP2KG4BYax8abIqSA%2B1Nc73MMegKbm%2BkFhySnD8r2YxnV0%2BeeklsBCcB%2B3W4t%2BVcHHyJ%2F5ixJwy8ROH4kRN2%2FMzLVa7UICpDIsHQaqxnrrNS%2Boyp%2FQywOQh%2BOIGFsvkpVdkC8Lsft2nFK9f%2BSAyrKX%2FnvqbqDasQ2hiRqx1GGkZHXZSArhape%2FvdaBg6GvAXjEvCQsam83onOFc1Lx4abygAZ1HxZzZ%2FJRX5MIef%2B7wGOqUBKxZPs%2BbNJYgeUth6LpCx%2FFLnrxLYgkNwO7DNaoKa%2Fc2WP1ZQDv1UGMZlRU7n%2BsPXVaNNi86tLwT2arwqTc7TwOe4JSwXBusvp1VFcZb2X%2BpciaVvdOJPPHj80bMojQN%2FISzLuceKaXsLtGiOQWzF4PrAm0dogExFVQNYWilx9nYC57Emjml75buKkcuLwnaP3RHMRgDF3Tc9BxbvN%2F4XbtFkrUbx&X-Amz-Signature=edcadb8572eeb1ab31b5ce18804f4d355ce8f177c58b35bd4b17d2048e3b4623&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XW7VC6OC%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGZKiJneanxjR4nw%2FgRaD9blc6Jyu%2F1cCgcL5pfedW%2F7AiEA%2FmOO7zsUdztMOoKk2tOaBFnF1Mb3JBFXJh2b8SSTjPUqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIg4DKEleatnu38LOyrcA4G0WmrmqESDmDH0GJlMe%2FRyTeID3RRS8RsqvvB6hdb%2FnEn6P2yWSXNLuOC9hUg1h%2BkCs8mFjhXFbyvnL1rO%2BhkmKTP7ZzCwsGvZf01G8qGnst0pezpH3nFbved8eE7SO7UXqO3EqUzJqEcZg8yJSFPfhnr%2Fn5rVzm739IMl1T2iliami65r8Jkq1YtsGv49Gsaj5u1rc3hZ48p2ILP4QnZzVHvyuEcAVjDBkOxfgT6aMP0hCgddXNNmMQR%2BFBtIIFhEr6mwlGJjVC7sc95%2FcPzgrWaT9khb%2B%2F4bXclK%2FBQBMXrSQxZBMbbva1GQglJrJ08fHo9dsvipW%2FClEWi9AIU95vI1G%2B7Msxk1brELw3PaMceVuJ12cZ6u9Pm16wQSFqjmWvMA5XFUHe2mjMVUreqzIP2KG4BYax8abIqSA%2B1Nc73MMegKbm%2BkFhySnD8r2YxnV0%2BeeklsBCcB%2B3W4t%2BVcHHyJ%2F5ixJwy8ROH4kRN2%2FMzLVa7UICpDIsHQaqxnrrNS%2Boyp%2FQywOQh%2BOIGFsvkpVdkC8Lsft2nFK9f%2BSAyrKX%2FnvqbqDasQ2hiRqx1GGkZHXZSArhape%2FvdaBg6GvAXjEvCQsam83onOFc1Lx4abygAZ1HxZzZ%2FJRX5MIef%2B7wGOqUBKxZPs%2BbNJYgeUth6LpCx%2FFLnrxLYgkNwO7DNaoKa%2Fc2WP1ZQDv1UGMZlRU7n%2BsPXVaNNi86tLwT2arwqTc7TwOe4JSwXBusvp1VFcZb2X%2BpciaVvdOJPPHj80bMojQN%2FISzLuceKaXsLtGiOQWzF4PrAm0dogExFVQNYWilx9nYC57Emjml75buKkcuLwnaP3RHMRgDF3Tc9BxbvN%2F4XbtFkrUbx&X-Amz-Signature=eaf8d2ce039f8fe7743cbf6e9e759fad2dfbb228cabeac8b8614da4200abf9b7&X-Amz-SignedHeaders=host&x-id=GetObject)
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


