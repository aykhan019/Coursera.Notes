

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQQNCMXY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDDwKe6gWMXFseS4JFtVZWZAv1eOJY9qGO5%2BqAC4YJzoQIgaoBtHLoAFUmUsgYJxYNGiCpZVD4XO4Sh71IDP7DV5CEq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDIgvh%2FvJYCRC6QtlXSrcA98aJwfTXUVQ0en92WqEn4KAX30X3lDEnWcRxzEWF9FIF179lJgx4ArYYrWejUjZHicwI8NE9FJycY84F4EFwZNcv93zF3REJZPqaEynRQlgJOrikFIn91uKcSDhCzpyedIUrSnIMUKzMgGgA%2BDn7qoUEYr9nzRRNNslbBWg%2B4KgZYFh45q4Xqgwkw%2BbZq1Gvuqm8POL0r8uD%2FTgyDapJzDG7ajwQvosyAN2IvFxEZ%2BI5OC7QcrA7yFw%2FFuu4TlAzR7qyASBeS6p%2BdAQWBmkpYIVHWjFcXqKOMIuA1%2FUAZdhVzUYsbbeusE%2BESjjbMM7iFFn7CmVYa1md8cN0r0%2FAwO8LH1txKIipebD09UQSgGr2tAODe5og7BL%2FFdScik2Xa%2FYVXbP7Hb0vG%2BO%2FEhr4MeUwvflDLoJMU8kv8QVuDkVFJa75ZGoNljQfXjFBROhWoqPIOUyCNz4T0%2FyGUT0GdAM6JMnty1YtiAyqwbzOEAOLuDERZSyWScdsldBD0Dz1mjK3FtElyZ5L%2FghlILJUl5GEGB1rSChaYiY36AQnDVj%2BqdzkJX3ArCBekJP7XSg69e8cQusNA91qnjj7qgsO56O2%2FC0olUEgi0clPjFioJ5EdNEO33m2nilgX3LMPOKmL0GOqUBOYhJfrtZJg21aAh87BvYDtj0T7%2Bj7tsu0eO7P8ykBbehDhHZFw%2BtMu0ONA7LLPdVC5vDrg7uCHO%2FgyM6o3%2FFL8CBbi01KUZUWCPCNpVovj3YIV74gZr2ILcVPIS2v%2B8CBd%2BNwupIJAhXp9lwAPSxSfhfyS2LNAawg6hmG9VzijmUSmf%2F2KrhPK1HsQvQOvmPWiz9dVx6AOdzdMIXV%2FmHCDKPSoa7&X-Amz-Signature=e318a1d70d7344e3620ece1146695a088002dd8a92da28c78615479c9ab08005&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVXLZPWH%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIEefxjsN6BLIi%2FHcfDIiCR5E5e7Xo%2FuRaC5VjUMVEfojAiEAjqaWrFXKtYbIp7Qa%2FnpI2vvB1O0GHfHNAvWcl6yQjfcq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDGR2UbYCTHOzrF6XgCrcAybQpVf9%2BJQa8VqfhrIB0NWBEFO0A755xFiXcr0wV6mZggj6M0KdVBRnVR0EQZMPtlOXB4oNnp8iqdZGteXad43pPBi0E88hsMJtkzsmaWT%2BJ9ecjr0bZksOjHxYNtKHfJ71Ddr8txetushPHhVa5NCBtuC1XhwF4ILAbQQSKhxkea2ASZo28eHyq1QO6NduUNnHQn71YSAklLjgdEaY%2BsZuvKXJt4kPePcVEEREQ5%2Fvo4V9s8z9bhyiKmOuRd3DuaC6cYOkbdpovlldzOUh5J%2BiYrFhcWkCEUrzVae9szvvT%2BLoObmYFOfIXywzDUGICvknPgBfW%2B8%2BFpBP%2F4w3xRD10xVq%2F46y%2FEZAW9g%2FOjnZWm9Ei30mXBoiPvXhXr%2BXgA6N6leRxed4EAyZXiI2nMtlYLAp1gTB%2FGGHStmqN9Ifi65%2BPYCfB6KVRp2oKG6o%2FGv79Lfqt39FlYxhMQ42JaFauqC8K5Qj7guIxnJRraAD%2Bqj3mHV6ivTmeYPbvOmEqLdbjQHoWZto3tSr%2Fz992GnyZh4GiIpdhMg2EGTVdSdXduTN2CFckMAxtOYOySZbcRPGrryKnkPhiu2me5MGtInVYI4rPVK8VRFCzjcxkoFuRaD6xGeXx1mk1DOHMISLmL0GOqUB3WT0kywRkly4SM4Qvl0%2BJ72uzDgFAGHGD6So7FNI9nYK60cOIT5mJ6PlMGIbrlSCgGzWfSPE6GDD7EVBHvF41OkdMHAB4942BJHx9RtPwDZeJn0wqw%2FlueMaPmh7hPLwfBUN3ESECFvdbxQzH9pwcXjfec%2Ble%2BqIxJYK2OH8qSEqAWJVYY9hJ9YfgX5AuT6HgQjxH6kfEGq1d%2FuKjLnmlhk%2FcC%2BL&X-Amz-Signature=34267cbdb3f4a4f9f99ecaaf5d120d5fd5cdd65894b1d96ad7a04aa31e2bddab&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVXLZPWH%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIEefxjsN6BLIi%2FHcfDIiCR5E5e7Xo%2FuRaC5VjUMVEfojAiEAjqaWrFXKtYbIp7Qa%2FnpI2vvB1O0GHfHNAvWcl6yQjfcq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDGR2UbYCTHOzrF6XgCrcAybQpVf9%2BJQa8VqfhrIB0NWBEFO0A755xFiXcr0wV6mZggj6M0KdVBRnVR0EQZMPtlOXB4oNnp8iqdZGteXad43pPBi0E88hsMJtkzsmaWT%2BJ9ecjr0bZksOjHxYNtKHfJ71Ddr8txetushPHhVa5NCBtuC1XhwF4ILAbQQSKhxkea2ASZo28eHyq1QO6NduUNnHQn71YSAklLjgdEaY%2BsZuvKXJt4kPePcVEEREQ5%2Fvo4V9s8z9bhyiKmOuRd3DuaC6cYOkbdpovlldzOUh5J%2BiYrFhcWkCEUrzVae9szvvT%2BLoObmYFOfIXywzDUGICvknPgBfW%2B8%2BFpBP%2F4w3xRD10xVq%2F46y%2FEZAW9g%2FOjnZWm9Ei30mXBoiPvXhXr%2BXgA6N6leRxed4EAyZXiI2nMtlYLAp1gTB%2FGGHStmqN9Ifi65%2BPYCfB6KVRp2oKG6o%2FGv79Lfqt39FlYxhMQ42JaFauqC8K5Qj7guIxnJRraAD%2Bqj3mHV6ivTmeYPbvOmEqLdbjQHoWZto3tSr%2Fz992GnyZh4GiIpdhMg2EGTVdSdXduTN2CFckMAxtOYOySZbcRPGrryKnkPhiu2me5MGtInVYI4rPVK8VRFCzjcxkoFuRaD6xGeXx1mk1DOHMISLmL0GOqUB3WT0kywRkly4SM4Qvl0%2BJ72uzDgFAGHGD6So7FNI9nYK60cOIT5mJ6PlMGIbrlSCgGzWfSPE6GDD7EVBHvF41OkdMHAB4942BJHx9RtPwDZeJn0wqw%2FlueMaPmh7hPLwfBUN3ESECFvdbxQzH9pwcXjfec%2Ble%2BqIxJYK2OH8qSEqAWJVYY9hJ9YfgX5AuT6HgQjxH6kfEGq1d%2FuKjLnmlhk%2FcC%2BL&X-Amz-Signature=d784c9941d8093aab544df3e34a6eb19c52b088d2c97ff1132687919d854ad62&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVXLZPWH%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIEefxjsN6BLIi%2FHcfDIiCR5E5e7Xo%2FuRaC5VjUMVEfojAiEAjqaWrFXKtYbIp7Qa%2FnpI2vvB1O0GHfHNAvWcl6yQjfcq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDGR2UbYCTHOzrF6XgCrcAybQpVf9%2BJQa8VqfhrIB0NWBEFO0A755xFiXcr0wV6mZggj6M0KdVBRnVR0EQZMPtlOXB4oNnp8iqdZGteXad43pPBi0E88hsMJtkzsmaWT%2BJ9ecjr0bZksOjHxYNtKHfJ71Ddr8txetushPHhVa5NCBtuC1XhwF4ILAbQQSKhxkea2ASZo28eHyq1QO6NduUNnHQn71YSAklLjgdEaY%2BsZuvKXJt4kPePcVEEREQ5%2Fvo4V9s8z9bhyiKmOuRd3DuaC6cYOkbdpovlldzOUh5J%2BiYrFhcWkCEUrzVae9szvvT%2BLoObmYFOfIXywzDUGICvknPgBfW%2B8%2BFpBP%2F4w3xRD10xVq%2F46y%2FEZAW9g%2FOjnZWm9Ei30mXBoiPvXhXr%2BXgA6N6leRxed4EAyZXiI2nMtlYLAp1gTB%2FGGHStmqN9Ifi65%2BPYCfB6KVRp2oKG6o%2FGv79Lfqt39FlYxhMQ42JaFauqC8K5Qj7guIxnJRraAD%2Bqj3mHV6ivTmeYPbvOmEqLdbjQHoWZto3tSr%2Fz992GnyZh4GiIpdhMg2EGTVdSdXduTN2CFckMAxtOYOySZbcRPGrryKnkPhiu2me5MGtInVYI4rPVK8VRFCzjcxkoFuRaD6xGeXx1mk1DOHMISLmL0GOqUB3WT0kywRkly4SM4Qvl0%2BJ72uzDgFAGHGD6So7FNI9nYK60cOIT5mJ6PlMGIbrlSCgGzWfSPE6GDD7EVBHvF41OkdMHAB4942BJHx9RtPwDZeJn0wqw%2FlueMaPmh7hPLwfBUN3ESECFvdbxQzH9pwcXjfec%2Ble%2BqIxJYK2OH8qSEqAWJVYY9hJ9YfgX5AuT6HgQjxH6kfEGq1d%2FuKjLnmlhk%2FcC%2BL&X-Amz-Signature=2fb6e2116c86c4210d371f8aa401670f92982729ecedca3ea47003d4c0cdaea4&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVXLZPWH%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIEefxjsN6BLIi%2FHcfDIiCR5E5e7Xo%2FuRaC5VjUMVEfojAiEAjqaWrFXKtYbIp7Qa%2FnpI2vvB1O0GHfHNAvWcl6yQjfcq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDGR2UbYCTHOzrF6XgCrcAybQpVf9%2BJQa8VqfhrIB0NWBEFO0A755xFiXcr0wV6mZggj6M0KdVBRnVR0EQZMPtlOXB4oNnp8iqdZGteXad43pPBi0E88hsMJtkzsmaWT%2BJ9ecjr0bZksOjHxYNtKHfJ71Ddr8txetushPHhVa5NCBtuC1XhwF4ILAbQQSKhxkea2ASZo28eHyq1QO6NduUNnHQn71YSAklLjgdEaY%2BsZuvKXJt4kPePcVEEREQ5%2Fvo4V9s8z9bhyiKmOuRd3DuaC6cYOkbdpovlldzOUh5J%2BiYrFhcWkCEUrzVae9szvvT%2BLoObmYFOfIXywzDUGICvknPgBfW%2B8%2BFpBP%2F4w3xRD10xVq%2F46y%2FEZAW9g%2FOjnZWm9Ei30mXBoiPvXhXr%2BXgA6N6leRxed4EAyZXiI2nMtlYLAp1gTB%2FGGHStmqN9Ifi65%2BPYCfB6KVRp2oKG6o%2FGv79Lfqt39FlYxhMQ42JaFauqC8K5Qj7guIxnJRraAD%2Bqj3mHV6ivTmeYPbvOmEqLdbjQHoWZto3tSr%2Fz992GnyZh4GiIpdhMg2EGTVdSdXduTN2CFckMAxtOYOySZbcRPGrryKnkPhiu2me5MGtInVYI4rPVK8VRFCzjcxkoFuRaD6xGeXx1mk1DOHMISLmL0GOqUB3WT0kywRkly4SM4Qvl0%2BJ72uzDgFAGHGD6So7FNI9nYK60cOIT5mJ6PlMGIbrlSCgGzWfSPE6GDD7EVBHvF41OkdMHAB4942BJHx9RtPwDZeJn0wqw%2FlueMaPmh7hPLwfBUN3ESECFvdbxQzH9pwcXjfec%2Ble%2BqIxJYK2OH8qSEqAWJVYY9hJ9YfgX5AuT6HgQjxH6kfEGq1d%2FuKjLnmlhk%2FcC%2BL&X-Amz-Signature=5ad90c251a36da27320cfdcb946aae860cc387e8b269e62ac54c83f64c4686b9&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVXLZPWH%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIEefxjsN6BLIi%2FHcfDIiCR5E5e7Xo%2FuRaC5VjUMVEfojAiEAjqaWrFXKtYbIp7Qa%2FnpI2vvB1O0GHfHNAvWcl6yQjfcq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDGR2UbYCTHOzrF6XgCrcAybQpVf9%2BJQa8VqfhrIB0NWBEFO0A755xFiXcr0wV6mZggj6M0KdVBRnVR0EQZMPtlOXB4oNnp8iqdZGteXad43pPBi0E88hsMJtkzsmaWT%2BJ9ecjr0bZksOjHxYNtKHfJ71Ddr8txetushPHhVa5NCBtuC1XhwF4ILAbQQSKhxkea2ASZo28eHyq1QO6NduUNnHQn71YSAklLjgdEaY%2BsZuvKXJt4kPePcVEEREQ5%2Fvo4V9s8z9bhyiKmOuRd3DuaC6cYOkbdpovlldzOUh5J%2BiYrFhcWkCEUrzVae9szvvT%2BLoObmYFOfIXywzDUGICvknPgBfW%2B8%2BFpBP%2F4w3xRD10xVq%2F46y%2FEZAW9g%2FOjnZWm9Ei30mXBoiPvXhXr%2BXgA6N6leRxed4EAyZXiI2nMtlYLAp1gTB%2FGGHStmqN9Ifi65%2BPYCfB6KVRp2oKG6o%2FGv79Lfqt39FlYxhMQ42JaFauqC8K5Qj7guIxnJRraAD%2Bqj3mHV6ivTmeYPbvOmEqLdbjQHoWZto3tSr%2Fz992GnyZh4GiIpdhMg2EGTVdSdXduTN2CFckMAxtOYOySZbcRPGrryKnkPhiu2me5MGtInVYI4rPVK8VRFCzjcxkoFuRaD6xGeXx1mk1DOHMISLmL0GOqUB3WT0kywRkly4SM4Qvl0%2BJ72uzDgFAGHGD6So7FNI9nYK60cOIT5mJ6PlMGIbrlSCgGzWfSPE6GDD7EVBHvF41OkdMHAB4942BJHx9RtPwDZeJn0wqw%2FlueMaPmh7hPLwfBUN3ESECFvdbxQzH9pwcXjfec%2Ble%2BqIxJYK2OH8qSEqAWJVYY9hJ9YfgX5AuT6HgQjxH6kfEGq1d%2FuKjLnmlhk%2FcC%2BL&X-Amz-Signature=0ff48834483fbc39bf7f8899a6ef5c04ee49b1ee238bb8fd68ad264caa8064ba&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQQNCMXY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDDwKe6gWMXFseS4JFtVZWZAv1eOJY9qGO5%2BqAC4YJzoQIgaoBtHLoAFUmUsgYJxYNGiCpZVD4XO4Sh71IDP7DV5CEq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDIgvh%2FvJYCRC6QtlXSrcA98aJwfTXUVQ0en92WqEn4KAX30X3lDEnWcRxzEWF9FIF179lJgx4ArYYrWejUjZHicwI8NE9FJycY84F4EFwZNcv93zF3REJZPqaEynRQlgJOrikFIn91uKcSDhCzpyedIUrSnIMUKzMgGgA%2BDn7qoUEYr9nzRRNNslbBWg%2B4KgZYFh45q4Xqgwkw%2BbZq1Gvuqm8POL0r8uD%2FTgyDapJzDG7ajwQvosyAN2IvFxEZ%2BI5OC7QcrA7yFw%2FFuu4TlAzR7qyASBeS6p%2BdAQWBmkpYIVHWjFcXqKOMIuA1%2FUAZdhVzUYsbbeusE%2BESjjbMM7iFFn7CmVYa1md8cN0r0%2FAwO8LH1txKIipebD09UQSgGr2tAODe5og7BL%2FFdScik2Xa%2FYVXbP7Hb0vG%2BO%2FEhr4MeUwvflDLoJMU8kv8QVuDkVFJa75ZGoNljQfXjFBROhWoqPIOUyCNz4T0%2FyGUT0GdAM6JMnty1YtiAyqwbzOEAOLuDERZSyWScdsldBD0Dz1mjK3FtElyZ5L%2FghlILJUl5GEGB1rSChaYiY36AQnDVj%2BqdzkJX3ArCBekJP7XSg69e8cQusNA91qnjj7qgsO56O2%2FC0olUEgi0clPjFioJ5EdNEO33m2nilgX3LMPOKmL0GOqUBOYhJfrtZJg21aAh87BvYDtj0T7%2Bj7tsu0eO7P8ykBbehDhHZFw%2BtMu0ONA7LLPdVC5vDrg7uCHO%2FgyM6o3%2FFL8CBbi01KUZUWCPCNpVovj3YIV74gZr2ILcVPIS2v%2B8CBd%2BNwupIJAhXp9lwAPSxSfhfyS2LNAawg6hmG9VzijmUSmf%2F2KrhPK1HsQvQOvmPWiz9dVx6AOdzdMIXV%2FmHCDKPSoa7&X-Amz-Signature=f19fd1bd07a39abd20570da179e309f44aebc049321a47fc2891b6ca545f41e2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQQNCMXY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDDwKe6gWMXFseS4JFtVZWZAv1eOJY9qGO5%2BqAC4YJzoQIgaoBtHLoAFUmUsgYJxYNGiCpZVD4XO4Sh71IDP7DV5CEq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDIgvh%2FvJYCRC6QtlXSrcA98aJwfTXUVQ0en92WqEn4KAX30X3lDEnWcRxzEWF9FIF179lJgx4ArYYrWejUjZHicwI8NE9FJycY84F4EFwZNcv93zF3REJZPqaEynRQlgJOrikFIn91uKcSDhCzpyedIUrSnIMUKzMgGgA%2BDn7qoUEYr9nzRRNNslbBWg%2B4KgZYFh45q4Xqgwkw%2BbZq1Gvuqm8POL0r8uD%2FTgyDapJzDG7ajwQvosyAN2IvFxEZ%2BI5OC7QcrA7yFw%2FFuu4TlAzR7qyASBeS6p%2BdAQWBmkpYIVHWjFcXqKOMIuA1%2FUAZdhVzUYsbbeusE%2BESjjbMM7iFFn7CmVYa1md8cN0r0%2FAwO8LH1txKIipebD09UQSgGr2tAODe5og7BL%2FFdScik2Xa%2FYVXbP7Hb0vG%2BO%2FEhr4MeUwvflDLoJMU8kv8QVuDkVFJa75ZGoNljQfXjFBROhWoqPIOUyCNz4T0%2FyGUT0GdAM6JMnty1YtiAyqwbzOEAOLuDERZSyWScdsldBD0Dz1mjK3FtElyZ5L%2FghlILJUl5GEGB1rSChaYiY36AQnDVj%2BqdzkJX3ArCBekJP7XSg69e8cQusNA91qnjj7qgsO56O2%2FC0olUEgi0clPjFioJ5EdNEO33m2nilgX3LMPOKmL0GOqUBOYhJfrtZJg21aAh87BvYDtj0T7%2Bj7tsu0eO7P8ykBbehDhHZFw%2BtMu0ONA7LLPdVC5vDrg7uCHO%2FgyM6o3%2FFL8CBbi01KUZUWCPCNpVovj3YIV74gZr2ILcVPIS2v%2B8CBd%2BNwupIJAhXp9lwAPSxSfhfyS2LNAawg6hmG9VzijmUSmf%2F2KrhPK1HsQvQOvmPWiz9dVx6AOdzdMIXV%2FmHCDKPSoa7&X-Amz-Signature=fca5e80249db0ca9f67b1d03c8f772f489afd8cbc692a3bcdda1c82c6d333eb2&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQQNCMXY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDDwKe6gWMXFseS4JFtVZWZAv1eOJY9qGO5%2BqAC4YJzoQIgaoBtHLoAFUmUsgYJxYNGiCpZVD4XO4Sh71IDP7DV5CEq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDIgvh%2FvJYCRC6QtlXSrcA98aJwfTXUVQ0en92WqEn4KAX30X3lDEnWcRxzEWF9FIF179lJgx4ArYYrWejUjZHicwI8NE9FJycY84F4EFwZNcv93zF3REJZPqaEynRQlgJOrikFIn91uKcSDhCzpyedIUrSnIMUKzMgGgA%2BDn7qoUEYr9nzRRNNslbBWg%2B4KgZYFh45q4Xqgwkw%2BbZq1Gvuqm8POL0r8uD%2FTgyDapJzDG7ajwQvosyAN2IvFxEZ%2BI5OC7QcrA7yFw%2FFuu4TlAzR7qyASBeS6p%2BdAQWBmkpYIVHWjFcXqKOMIuA1%2FUAZdhVzUYsbbeusE%2BESjjbMM7iFFn7CmVYa1md8cN0r0%2FAwO8LH1txKIipebD09UQSgGr2tAODe5og7BL%2FFdScik2Xa%2FYVXbP7Hb0vG%2BO%2FEhr4MeUwvflDLoJMU8kv8QVuDkVFJa75ZGoNljQfXjFBROhWoqPIOUyCNz4T0%2FyGUT0GdAM6JMnty1YtiAyqwbzOEAOLuDERZSyWScdsldBD0Dz1mjK3FtElyZ5L%2FghlILJUl5GEGB1rSChaYiY36AQnDVj%2BqdzkJX3ArCBekJP7XSg69e8cQusNA91qnjj7qgsO56O2%2FC0olUEgi0clPjFioJ5EdNEO33m2nilgX3LMPOKmL0GOqUBOYhJfrtZJg21aAh87BvYDtj0T7%2Bj7tsu0eO7P8ykBbehDhHZFw%2BtMu0ONA7LLPdVC5vDrg7uCHO%2FgyM6o3%2FFL8CBbi01KUZUWCPCNpVovj3YIV74gZr2ILcVPIS2v%2B8CBd%2BNwupIJAhXp9lwAPSxSfhfyS2LNAawg6hmG9VzijmUSmf%2F2KrhPK1HsQvQOvmPWiz9dVx6AOdzdMIXV%2FmHCDKPSoa7&X-Amz-Signature=1c807a4d5fac032ae600347144b18a6029bd0e44fb0415439947dc2b0bd041e9&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQQNCMXY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDDwKe6gWMXFseS4JFtVZWZAv1eOJY9qGO5%2BqAC4YJzoQIgaoBtHLoAFUmUsgYJxYNGiCpZVD4XO4Sh71IDP7DV5CEq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDIgvh%2FvJYCRC6QtlXSrcA98aJwfTXUVQ0en92WqEn4KAX30X3lDEnWcRxzEWF9FIF179lJgx4ArYYrWejUjZHicwI8NE9FJycY84F4EFwZNcv93zF3REJZPqaEynRQlgJOrikFIn91uKcSDhCzpyedIUrSnIMUKzMgGgA%2BDn7qoUEYr9nzRRNNslbBWg%2B4KgZYFh45q4Xqgwkw%2BbZq1Gvuqm8POL0r8uD%2FTgyDapJzDG7ajwQvosyAN2IvFxEZ%2BI5OC7QcrA7yFw%2FFuu4TlAzR7qyASBeS6p%2BdAQWBmkpYIVHWjFcXqKOMIuA1%2FUAZdhVzUYsbbeusE%2BESjjbMM7iFFn7CmVYa1md8cN0r0%2FAwO8LH1txKIipebD09UQSgGr2tAODe5og7BL%2FFdScik2Xa%2FYVXbP7Hb0vG%2BO%2FEhr4MeUwvflDLoJMU8kv8QVuDkVFJa75ZGoNljQfXjFBROhWoqPIOUyCNz4T0%2FyGUT0GdAM6JMnty1YtiAyqwbzOEAOLuDERZSyWScdsldBD0Dz1mjK3FtElyZ5L%2FghlILJUl5GEGB1rSChaYiY36AQnDVj%2BqdzkJX3ArCBekJP7XSg69e8cQusNA91qnjj7qgsO56O2%2FC0olUEgi0clPjFioJ5EdNEO33m2nilgX3LMPOKmL0GOqUBOYhJfrtZJg21aAh87BvYDtj0T7%2Bj7tsu0eO7P8ykBbehDhHZFw%2BtMu0ONA7LLPdVC5vDrg7uCHO%2FgyM6o3%2FFL8CBbi01KUZUWCPCNpVovj3YIV74gZr2ILcVPIS2v%2B8CBd%2BNwupIJAhXp9lwAPSxSfhfyS2LNAawg6hmG9VzijmUSmf%2F2KrhPK1HsQvQOvmPWiz9dVx6AOdzdMIXV%2FmHCDKPSoa7&X-Amz-Signature=005439aa7969d6b86f1b7b6455f6e5d00bce66db649807d0e2a3c371c9984403&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQQNCMXY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDDwKe6gWMXFseS4JFtVZWZAv1eOJY9qGO5%2BqAC4YJzoQIgaoBtHLoAFUmUsgYJxYNGiCpZVD4XO4Sh71IDP7DV5CEq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDIgvh%2FvJYCRC6QtlXSrcA98aJwfTXUVQ0en92WqEn4KAX30X3lDEnWcRxzEWF9FIF179lJgx4ArYYrWejUjZHicwI8NE9FJycY84F4EFwZNcv93zF3REJZPqaEynRQlgJOrikFIn91uKcSDhCzpyedIUrSnIMUKzMgGgA%2BDn7qoUEYr9nzRRNNslbBWg%2B4KgZYFh45q4Xqgwkw%2BbZq1Gvuqm8POL0r8uD%2FTgyDapJzDG7ajwQvosyAN2IvFxEZ%2BI5OC7QcrA7yFw%2FFuu4TlAzR7qyASBeS6p%2BdAQWBmkpYIVHWjFcXqKOMIuA1%2FUAZdhVzUYsbbeusE%2BESjjbMM7iFFn7CmVYa1md8cN0r0%2FAwO8LH1txKIipebD09UQSgGr2tAODe5og7BL%2FFdScik2Xa%2FYVXbP7Hb0vG%2BO%2FEhr4MeUwvflDLoJMU8kv8QVuDkVFJa75ZGoNljQfXjFBROhWoqPIOUyCNz4T0%2FyGUT0GdAM6JMnty1YtiAyqwbzOEAOLuDERZSyWScdsldBD0Dz1mjK3FtElyZ5L%2FghlILJUl5GEGB1rSChaYiY36AQnDVj%2BqdzkJX3ArCBekJP7XSg69e8cQusNA91qnjj7qgsO56O2%2FC0olUEgi0clPjFioJ5EdNEO33m2nilgX3LMPOKmL0GOqUBOYhJfrtZJg21aAh87BvYDtj0T7%2Bj7tsu0eO7P8ykBbehDhHZFw%2BtMu0ONA7LLPdVC5vDrg7uCHO%2FgyM6o3%2FFL8CBbi01KUZUWCPCNpVovj3YIV74gZr2ILcVPIS2v%2B8CBd%2BNwupIJAhXp9lwAPSxSfhfyS2LNAawg6hmG9VzijmUSmf%2F2KrhPK1HsQvQOvmPWiz9dVx6AOdzdMIXV%2FmHCDKPSoa7&X-Amz-Signature=4caabf40cf5769efc37e98f2a1cff39dbc5678de6eff94d95c93bb98bf5db29c&X-Amz-SignedHeaders=host&x-id=GetObject)
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


