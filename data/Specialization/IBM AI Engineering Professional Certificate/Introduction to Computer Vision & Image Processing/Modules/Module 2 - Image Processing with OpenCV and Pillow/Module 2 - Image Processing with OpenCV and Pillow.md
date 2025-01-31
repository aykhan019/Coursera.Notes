

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VT6S4RJ4%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081842Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICeKh%2BRqvuc%2BEFUYln4wb%2Fn1XZLk%2Fk18WkNcpt%2BpXfevAiBE1r1LQLk2g8dVWchHdsmeiBL6uz2eOvTuR0%2F73nMN%2FyqIBAi5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9xe6UCne1jCo7%2FdYKtwDLqqlBGebinq0lyyTJaKhowFcY%2FJHY6vW8jZ3J6PluhAqySjQINeqRtFajAuc46C7RPF3nfRK%2FaOXQysgMqo4rBPYTJ36tuncsg4zw1jWtHvN39%2FpeFU38JxFF4VSSRxU8W1Ta%2BKv1bv5K53cNYasLITPJhjSWLljuERx%2FF%2Fpgtd5li3CkZakfzDn6gZqSW99adggyCVlAZSno%2FII85U3v%2ByX4YeXlFutM47lWzg%2Ffn8F2k2z%2Bxd7UjiotKSDHMNX2jZk2k8e5JsuDzJ%2FKASJF%2BiiN0D6BH2Q7L%2BUBKvQ6GGF9%2BMLB9jOTIFyZLv9sb8jok3%2F5oBPkpG3EMTv4SjWrPrse9oLxjxMiYI%2FERKgIejVzyADExGRVI8xAfUsJMk8Dan%2FTjAoK6NWjFFvZ8JNDYnWnzKOnVUIo44jklRyu%2FvaxWxWgLliUr0PMXu82LOe9O9JTlJYzx9ZKXS8Vf05zPiuzccmqS9LhHI%2FIEcHTYhYInjspML82mBkVhHFMY%2BDigNsD53DDv%2Fao5qRqON74a18H2YGSHt5FdqhjoFk7%2FAyaIa0KVV9yudseZnaO2seR84E8YP7NaL6y3UMC%2F9SZ%2BjOWe8wLfCbNtwLME%2FWSb3FxPnoGTNQ0EghAVEwwYLyvAY6pgFIk1Ihwa4noazdOQjHXAF%2Fr8kyS6qfmiVLBGaxuzX0UZWlyqSdI9fjTUuFSEgrEPjFYD85gKc2ZoLJzvHi0K9XV45Md9WRJ%2FIGm9lO3QyxmxKJSMIaB1ttOojzEMZ5CknvJGwfZPe0tWfdzBg2dQqDoShYCFn9SRrODJNl3o6ynL9Z%2F8mhJ49P5iOmdTh09zwIxgkACoIpX%2B97Uwp9lAb2eLB9Qpby&X-Amz-Signature=6d5ca1a4cdf90f883dff63462779ee4200995d8995d6c42d042bc0fa5c5ac0b0&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46652PVRWO4%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081842Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH46TyDJC6SQ%2FHXD8KmU3TaQNXaNQc9rmOGWTUESaY3BAiBUHlYuUZlPoM7tLkRNbzNkzuyNQAv6m67SQ80RnrVFxyqIBAi5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8alklyarImSTHX1rKtwD7dzrflG4At2PyyQ0bkRDquEsZDUtTnJr%2BkLsZ91rvMnLlrQhnS1rg%2F5TvCDsSVjfJiDHIipPyE13FIcIw7iHQORRqnm1Vy06Ph9LWItWxq4sUwWiTHeNbGrRALLCdE3ORWYSPglnh%2Bw2U9PVInPoMxuPdtgxQ3tMNxd0dYdrXiK47Vwt0gYjanohM9ZdbY9VPhEBWEYttRt5GsmhO4LQp0Mh1xZUBsbtQIsoGcCYrv55q%2FxyMYC9yavpD6EZ4vXu1f8o%2FMEg35Juz79Bq8H28G66OjIbNwjUNtugaE%2FivChln95sEzGGlEmUPHHKSsSCx8cQ4VNDzQ0tfADXkFoX4Xsbmk70uyC8bTwNZ0TvJQsa2gnnVsPG%2BjIr79KFNC3675P0gejicyEIkK%2B9Ztie%2FF9z8CI%2FSEH1GmTqAI92JUWT%2B6U0bWh9eeCsTiGkLYHtPjzO%2B3qkrnpHYYBz0aQWNGasXPdMwgTqIBTtUVGtr7fzLnxydw4CNfTyQYAKnGQuBW%2FhxvuGbnkUxnMgYCtx7CgXu5epcCFdPC%2F7zdeMFacyvICsaET%2FKVysbaIhKBqDyuiH75F6nhaIuZtra09THj0WD4tUjhkgZWawv8a7plnyKdM515BuygbugRkw%2B%2F7xvAY6pgFnQ3xeTde4Isf2hdh%2BHAz0sM4cuJTQATitmmIcIDPjATOqRQNAzDkoR4MUySRns9RmKsv%2BsV1gUoI4WmwikY1Fl4pfQK2wJvWyW%2FqYxdby%2Bo6lNht0NWPn5dcoVpKe5YVasmBVNTXpmzGrJFHOrWfH%2BxgcCKe0oDee9ScDh3tAwMDcV1nzY6ZbLUDJSFW1hnp7mggtekXkArM8qXEvYavIzFTeGmmJ&X-Amz-Signature=862d60b1238c4a34e485eed9e3f81a6a8855ab4e7cedb8cf9d03810a99a490d8&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46652PVRWO4%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081842Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH46TyDJC6SQ%2FHXD8KmU3TaQNXaNQc9rmOGWTUESaY3BAiBUHlYuUZlPoM7tLkRNbzNkzuyNQAv6m67SQ80RnrVFxyqIBAi5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8alklyarImSTHX1rKtwD7dzrflG4At2PyyQ0bkRDquEsZDUtTnJr%2BkLsZ91rvMnLlrQhnS1rg%2F5TvCDsSVjfJiDHIipPyE13FIcIw7iHQORRqnm1Vy06Ph9LWItWxq4sUwWiTHeNbGrRALLCdE3ORWYSPglnh%2Bw2U9PVInPoMxuPdtgxQ3tMNxd0dYdrXiK47Vwt0gYjanohM9ZdbY9VPhEBWEYttRt5GsmhO4LQp0Mh1xZUBsbtQIsoGcCYrv55q%2FxyMYC9yavpD6EZ4vXu1f8o%2FMEg35Juz79Bq8H28G66OjIbNwjUNtugaE%2FivChln95sEzGGlEmUPHHKSsSCx8cQ4VNDzQ0tfADXkFoX4Xsbmk70uyC8bTwNZ0TvJQsa2gnnVsPG%2BjIr79KFNC3675P0gejicyEIkK%2B9Ztie%2FF9z8CI%2FSEH1GmTqAI92JUWT%2B6U0bWh9eeCsTiGkLYHtPjzO%2B3qkrnpHYYBz0aQWNGasXPdMwgTqIBTtUVGtr7fzLnxydw4CNfTyQYAKnGQuBW%2FhxvuGbnkUxnMgYCtx7CgXu5epcCFdPC%2F7zdeMFacyvICsaET%2FKVysbaIhKBqDyuiH75F6nhaIuZtra09THj0WD4tUjhkgZWawv8a7plnyKdM515BuygbugRkw%2B%2F7xvAY6pgFnQ3xeTde4Isf2hdh%2BHAz0sM4cuJTQATitmmIcIDPjATOqRQNAzDkoR4MUySRns9RmKsv%2BsV1gUoI4WmwikY1Fl4pfQK2wJvWyW%2FqYxdby%2Bo6lNht0NWPn5dcoVpKe5YVasmBVNTXpmzGrJFHOrWfH%2BxgcCKe0oDee9ScDh3tAwMDcV1nzY6ZbLUDJSFW1hnp7mggtekXkArM8qXEvYavIzFTeGmmJ&X-Amz-Signature=ed27ffb12de7ed5a213ae5ba28c87d329c7481585183bbb667da2f3d38a7f334&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46652PVRWO4%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081842Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH46TyDJC6SQ%2FHXD8KmU3TaQNXaNQc9rmOGWTUESaY3BAiBUHlYuUZlPoM7tLkRNbzNkzuyNQAv6m67SQ80RnrVFxyqIBAi5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8alklyarImSTHX1rKtwD7dzrflG4At2PyyQ0bkRDquEsZDUtTnJr%2BkLsZ91rvMnLlrQhnS1rg%2F5TvCDsSVjfJiDHIipPyE13FIcIw7iHQORRqnm1Vy06Ph9LWItWxq4sUwWiTHeNbGrRALLCdE3ORWYSPglnh%2Bw2U9PVInPoMxuPdtgxQ3tMNxd0dYdrXiK47Vwt0gYjanohM9ZdbY9VPhEBWEYttRt5GsmhO4LQp0Mh1xZUBsbtQIsoGcCYrv55q%2FxyMYC9yavpD6EZ4vXu1f8o%2FMEg35Juz79Bq8H28G66OjIbNwjUNtugaE%2FivChln95sEzGGlEmUPHHKSsSCx8cQ4VNDzQ0tfADXkFoX4Xsbmk70uyC8bTwNZ0TvJQsa2gnnVsPG%2BjIr79KFNC3675P0gejicyEIkK%2B9Ztie%2FF9z8CI%2FSEH1GmTqAI92JUWT%2B6U0bWh9eeCsTiGkLYHtPjzO%2B3qkrnpHYYBz0aQWNGasXPdMwgTqIBTtUVGtr7fzLnxydw4CNfTyQYAKnGQuBW%2FhxvuGbnkUxnMgYCtx7CgXu5epcCFdPC%2F7zdeMFacyvICsaET%2FKVysbaIhKBqDyuiH75F6nhaIuZtra09THj0WD4tUjhkgZWawv8a7plnyKdM515BuygbugRkw%2B%2F7xvAY6pgFnQ3xeTde4Isf2hdh%2BHAz0sM4cuJTQATitmmIcIDPjATOqRQNAzDkoR4MUySRns9RmKsv%2BsV1gUoI4WmwikY1Fl4pfQK2wJvWyW%2FqYxdby%2Bo6lNht0NWPn5dcoVpKe5YVasmBVNTXpmzGrJFHOrWfH%2BxgcCKe0oDee9ScDh3tAwMDcV1nzY6ZbLUDJSFW1hnp7mggtekXkArM8qXEvYavIzFTeGmmJ&X-Amz-Signature=491a08f2170433a90a2b2928f32541d2ce497f17f666a7dafe73fc51455b467a&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46652PVRWO4%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081842Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH46TyDJC6SQ%2FHXD8KmU3TaQNXaNQc9rmOGWTUESaY3BAiBUHlYuUZlPoM7tLkRNbzNkzuyNQAv6m67SQ80RnrVFxyqIBAi5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8alklyarImSTHX1rKtwD7dzrflG4At2PyyQ0bkRDquEsZDUtTnJr%2BkLsZ91rvMnLlrQhnS1rg%2F5TvCDsSVjfJiDHIipPyE13FIcIw7iHQORRqnm1Vy06Ph9LWItWxq4sUwWiTHeNbGrRALLCdE3ORWYSPglnh%2Bw2U9PVInPoMxuPdtgxQ3tMNxd0dYdrXiK47Vwt0gYjanohM9ZdbY9VPhEBWEYttRt5GsmhO4LQp0Mh1xZUBsbtQIsoGcCYrv55q%2FxyMYC9yavpD6EZ4vXu1f8o%2FMEg35Juz79Bq8H28G66OjIbNwjUNtugaE%2FivChln95sEzGGlEmUPHHKSsSCx8cQ4VNDzQ0tfADXkFoX4Xsbmk70uyC8bTwNZ0TvJQsa2gnnVsPG%2BjIr79KFNC3675P0gejicyEIkK%2B9Ztie%2FF9z8CI%2FSEH1GmTqAI92JUWT%2B6U0bWh9eeCsTiGkLYHtPjzO%2B3qkrnpHYYBz0aQWNGasXPdMwgTqIBTtUVGtr7fzLnxydw4CNfTyQYAKnGQuBW%2FhxvuGbnkUxnMgYCtx7CgXu5epcCFdPC%2F7zdeMFacyvICsaET%2FKVysbaIhKBqDyuiH75F6nhaIuZtra09THj0WD4tUjhkgZWawv8a7plnyKdM515BuygbugRkw%2B%2F7xvAY6pgFnQ3xeTde4Isf2hdh%2BHAz0sM4cuJTQATitmmIcIDPjATOqRQNAzDkoR4MUySRns9RmKsv%2BsV1gUoI4WmwikY1Fl4pfQK2wJvWyW%2FqYxdby%2Bo6lNht0NWPn5dcoVpKe5YVasmBVNTXpmzGrJFHOrWfH%2BxgcCKe0oDee9ScDh3tAwMDcV1nzY6ZbLUDJSFW1hnp7mggtekXkArM8qXEvYavIzFTeGmmJ&X-Amz-Signature=62c2a29c851d75b53a752c3c214b914a44a15e3ab4bdeff680be65749ed61631&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46652PVRWO4%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081842Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH46TyDJC6SQ%2FHXD8KmU3TaQNXaNQc9rmOGWTUESaY3BAiBUHlYuUZlPoM7tLkRNbzNkzuyNQAv6m67SQ80RnrVFxyqIBAi5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8alklyarImSTHX1rKtwD7dzrflG4At2PyyQ0bkRDquEsZDUtTnJr%2BkLsZ91rvMnLlrQhnS1rg%2F5TvCDsSVjfJiDHIipPyE13FIcIw7iHQORRqnm1Vy06Ph9LWItWxq4sUwWiTHeNbGrRALLCdE3ORWYSPglnh%2Bw2U9PVInPoMxuPdtgxQ3tMNxd0dYdrXiK47Vwt0gYjanohM9ZdbY9VPhEBWEYttRt5GsmhO4LQp0Mh1xZUBsbtQIsoGcCYrv55q%2FxyMYC9yavpD6EZ4vXu1f8o%2FMEg35Juz79Bq8H28G66OjIbNwjUNtugaE%2FivChln95sEzGGlEmUPHHKSsSCx8cQ4VNDzQ0tfADXkFoX4Xsbmk70uyC8bTwNZ0TvJQsa2gnnVsPG%2BjIr79KFNC3675P0gejicyEIkK%2B9Ztie%2FF9z8CI%2FSEH1GmTqAI92JUWT%2B6U0bWh9eeCsTiGkLYHtPjzO%2B3qkrnpHYYBz0aQWNGasXPdMwgTqIBTtUVGtr7fzLnxydw4CNfTyQYAKnGQuBW%2FhxvuGbnkUxnMgYCtx7CgXu5epcCFdPC%2F7zdeMFacyvICsaET%2FKVysbaIhKBqDyuiH75F6nhaIuZtra09THj0WD4tUjhkgZWawv8a7plnyKdM515BuygbugRkw%2B%2F7xvAY6pgFnQ3xeTde4Isf2hdh%2BHAz0sM4cuJTQATitmmIcIDPjATOqRQNAzDkoR4MUySRns9RmKsv%2BsV1gUoI4WmwikY1Fl4pfQK2wJvWyW%2FqYxdby%2Bo6lNht0NWPn5dcoVpKe5YVasmBVNTXpmzGrJFHOrWfH%2BxgcCKe0oDee9ScDh3tAwMDcV1nzY6ZbLUDJSFW1hnp7mggtekXkArM8qXEvYavIzFTeGmmJ&X-Amz-Signature=037df872a0e6b6f7a53a1b7631023b49ecb202aea06b81dbd884d2ea1c41b034&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VT6S4RJ4%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081842Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICeKh%2BRqvuc%2BEFUYln4wb%2Fn1XZLk%2Fk18WkNcpt%2BpXfevAiBE1r1LQLk2g8dVWchHdsmeiBL6uz2eOvTuR0%2F73nMN%2FyqIBAi5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9xe6UCne1jCo7%2FdYKtwDLqqlBGebinq0lyyTJaKhowFcY%2FJHY6vW8jZ3J6PluhAqySjQINeqRtFajAuc46C7RPF3nfRK%2FaOXQysgMqo4rBPYTJ36tuncsg4zw1jWtHvN39%2FpeFU38JxFF4VSSRxU8W1Ta%2BKv1bv5K53cNYasLITPJhjSWLljuERx%2FF%2Fpgtd5li3CkZakfzDn6gZqSW99adggyCVlAZSno%2FII85U3v%2ByX4YeXlFutM47lWzg%2Ffn8F2k2z%2Bxd7UjiotKSDHMNX2jZk2k8e5JsuDzJ%2FKASJF%2BiiN0D6BH2Q7L%2BUBKvQ6GGF9%2BMLB9jOTIFyZLv9sb8jok3%2F5oBPkpG3EMTv4SjWrPrse9oLxjxMiYI%2FERKgIejVzyADExGRVI8xAfUsJMk8Dan%2FTjAoK6NWjFFvZ8JNDYnWnzKOnVUIo44jklRyu%2FvaxWxWgLliUr0PMXu82LOe9O9JTlJYzx9ZKXS8Vf05zPiuzccmqS9LhHI%2FIEcHTYhYInjspML82mBkVhHFMY%2BDigNsD53DDv%2Fao5qRqON74a18H2YGSHt5FdqhjoFk7%2FAyaIa0KVV9yudseZnaO2seR84E8YP7NaL6y3UMC%2F9SZ%2BjOWe8wLfCbNtwLME%2FWSb3FxPnoGTNQ0EghAVEwwYLyvAY6pgFIk1Ihwa4noazdOQjHXAF%2Fr8kyS6qfmiVLBGaxuzX0UZWlyqSdI9fjTUuFSEgrEPjFYD85gKc2ZoLJzvHi0K9XV45Md9WRJ%2FIGm9lO3QyxmxKJSMIaB1ttOojzEMZ5CknvJGwfZPe0tWfdzBg2dQqDoShYCFn9SRrODJNl3o6ynL9Z%2F8mhJ49P5iOmdTh09zwIxgkACoIpX%2B97Uwp9lAb2eLB9Qpby&X-Amz-Signature=e42810628d15c5988428530d4339aadabf0d09ebd9e3087b98e84e3d00ce1052&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VT6S4RJ4%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081842Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICeKh%2BRqvuc%2BEFUYln4wb%2Fn1XZLk%2Fk18WkNcpt%2BpXfevAiBE1r1LQLk2g8dVWchHdsmeiBL6uz2eOvTuR0%2F73nMN%2FyqIBAi5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9xe6UCne1jCo7%2FdYKtwDLqqlBGebinq0lyyTJaKhowFcY%2FJHY6vW8jZ3J6PluhAqySjQINeqRtFajAuc46C7RPF3nfRK%2FaOXQysgMqo4rBPYTJ36tuncsg4zw1jWtHvN39%2FpeFU38JxFF4VSSRxU8W1Ta%2BKv1bv5K53cNYasLITPJhjSWLljuERx%2FF%2Fpgtd5li3CkZakfzDn6gZqSW99adggyCVlAZSno%2FII85U3v%2ByX4YeXlFutM47lWzg%2Ffn8F2k2z%2Bxd7UjiotKSDHMNX2jZk2k8e5JsuDzJ%2FKASJF%2BiiN0D6BH2Q7L%2BUBKvQ6GGF9%2BMLB9jOTIFyZLv9sb8jok3%2F5oBPkpG3EMTv4SjWrPrse9oLxjxMiYI%2FERKgIejVzyADExGRVI8xAfUsJMk8Dan%2FTjAoK6NWjFFvZ8JNDYnWnzKOnVUIo44jklRyu%2FvaxWxWgLliUr0PMXu82LOe9O9JTlJYzx9ZKXS8Vf05zPiuzccmqS9LhHI%2FIEcHTYhYInjspML82mBkVhHFMY%2BDigNsD53DDv%2Fao5qRqON74a18H2YGSHt5FdqhjoFk7%2FAyaIa0KVV9yudseZnaO2seR84E8YP7NaL6y3UMC%2F9SZ%2BjOWe8wLfCbNtwLME%2FWSb3FxPnoGTNQ0EghAVEwwYLyvAY6pgFIk1Ihwa4noazdOQjHXAF%2Fr8kyS6qfmiVLBGaxuzX0UZWlyqSdI9fjTUuFSEgrEPjFYD85gKc2ZoLJzvHi0K9XV45Md9WRJ%2FIGm9lO3QyxmxKJSMIaB1ttOojzEMZ5CknvJGwfZPe0tWfdzBg2dQqDoShYCFn9SRrODJNl3o6ynL9Z%2F8mhJ49P5iOmdTh09zwIxgkACoIpX%2B97Uwp9lAb2eLB9Qpby&X-Amz-Signature=f07f689429b4c1f9b3f32fef158fb9877268bebb09f1c4dfbbfa8bba6da9f2a4&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VT6S4RJ4%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081842Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICeKh%2BRqvuc%2BEFUYln4wb%2Fn1XZLk%2Fk18WkNcpt%2BpXfevAiBE1r1LQLk2g8dVWchHdsmeiBL6uz2eOvTuR0%2F73nMN%2FyqIBAi5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9xe6UCne1jCo7%2FdYKtwDLqqlBGebinq0lyyTJaKhowFcY%2FJHY6vW8jZ3J6PluhAqySjQINeqRtFajAuc46C7RPF3nfRK%2FaOXQysgMqo4rBPYTJ36tuncsg4zw1jWtHvN39%2FpeFU38JxFF4VSSRxU8W1Ta%2BKv1bv5K53cNYasLITPJhjSWLljuERx%2FF%2Fpgtd5li3CkZakfzDn6gZqSW99adggyCVlAZSno%2FII85U3v%2ByX4YeXlFutM47lWzg%2Ffn8F2k2z%2Bxd7UjiotKSDHMNX2jZk2k8e5JsuDzJ%2FKASJF%2BiiN0D6BH2Q7L%2BUBKvQ6GGF9%2BMLB9jOTIFyZLv9sb8jok3%2F5oBPkpG3EMTv4SjWrPrse9oLxjxMiYI%2FERKgIejVzyADExGRVI8xAfUsJMk8Dan%2FTjAoK6NWjFFvZ8JNDYnWnzKOnVUIo44jklRyu%2FvaxWxWgLliUr0PMXu82LOe9O9JTlJYzx9ZKXS8Vf05zPiuzccmqS9LhHI%2FIEcHTYhYInjspML82mBkVhHFMY%2BDigNsD53DDv%2Fao5qRqON74a18H2YGSHt5FdqhjoFk7%2FAyaIa0KVV9yudseZnaO2seR84E8YP7NaL6y3UMC%2F9SZ%2BjOWe8wLfCbNtwLME%2FWSb3FxPnoGTNQ0EghAVEwwYLyvAY6pgFIk1Ihwa4noazdOQjHXAF%2Fr8kyS6qfmiVLBGaxuzX0UZWlyqSdI9fjTUuFSEgrEPjFYD85gKc2ZoLJzvHi0K9XV45Md9WRJ%2FIGm9lO3QyxmxKJSMIaB1ttOojzEMZ5CknvJGwfZPe0tWfdzBg2dQqDoShYCFn9SRrODJNl3o6ynL9Z%2F8mhJ49P5iOmdTh09zwIxgkACoIpX%2B97Uwp9lAb2eLB9Qpby&X-Amz-Signature=1b8582689490ad6683439835d69b0a5b5f909f9be0eda229232867aee26284c0&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VT6S4RJ4%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081842Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICeKh%2BRqvuc%2BEFUYln4wb%2Fn1XZLk%2Fk18WkNcpt%2BpXfevAiBE1r1LQLk2g8dVWchHdsmeiBL6uz2eOvTuR0%2F73nMN%2FyqIBAi5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9xe6UCne1jCo7%2FdYKtwDLqqlBGebinq0lyyTJaKhowFcY%2FJHY6vW8jZ3J6PluhAqySjQINeqRtFajAuc46C7RPF3nfRK%2FaOXQysgMqo4rBPYTJ36tuncsg4zw1jWtHvN39%2FpeFU38JxFF4VSSRxU8W1Ta%2BKv1bv5K53cNYasLITPJhjSWLljuERx%2FF%2Fpgtd5li3CkZakfzDn6gZqSW99adggyCVlAZSno%2FII85U3v%2ByX4YeXlFutM47lWzg%2Ffn8F2k2z%2Bxd7UjiotKSDHMNX2jZk2k8e5JsuDzJ%2FKASJF%2BiiN0D6BH2Q7L%2BUBKvQ6GGF9%2BMLB9jOTIFyZLv9sb8jok3%2F5oBPkpG3EMTv4SjWrPrse9oLxjxMiYI%2FERKgIejVzyADExGRVI8xAfUsJMk8Dan%2FTjAoK6NWjFFvZ8JNDYnWnzKOnVUIo44jklRyu%2FvaxWxWgLliUr0PMXu82LOe9O9JTlJYzx9ZKXS8Vf05zPiuzccmqS9LhHI%2FIEcHTYhYInjspML82mBkVhHFMY%2BDigNsD53DDv%2Fao5qRqON74a18H2YGSHt5FdqhjoFk7%2FAyaIa0KVV9yudseZnaO2seR84E8YP7NaL6y3UMC%2F9SZ%2BjOWe8wLfCbNtwLME%2FWSb3FxPnoGTNQ0EghAVEwwYLyvAY6pgFIk1Ihwa4noazdOQjHXAF%2Fr8kyS6qfmiVLBGaxuzX0UZWlyqSdI9fjTUuFSEgrEPjFYD85gKc2ZoLJzvHi0K9XV45Md9WRJ%2FIGm9lO3QyxmxKJSMIaB1ttOojzEMZ5CknvJGwfZPe0tWfdzBg2dQqDoShYCFn9SRrODJNl3o6ynL9Z%2F8mhJ49P5iOmdTh09zwIxgkACoIpX%2B97Uwp9lAb2eLB9Qpby&X-Amz-Signature=1646ed466e09af209b23e270e5ceeabfbee5200172b08dfae7faca196de6943b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VT6S4RJ4%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081842Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICeKh%2BRqvuc%2BEFUYln4wb%2Fn1XZLk%2Fk18WkNcpt%2BpXfevAiBE1r1LQLk2g8dVWchHdsmeiBL6uz2eOvTuR0%2F73nMN%2FyqIBAi5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9xe6UCne1jCo7%2FdYKtwDLqqlBGebinq0lyyTJaKhowFcY%2FJHY6vW8jZ3J6PluhAqySjQINeqRtFajAuc46C7RPF3nfRK%2FaOXQysgMqo4rBPYTJ36tuncsg4zw1jWtHvN39%2FpeFU38JxFF4VSSRxU8W1Ta%2BKv1bv5K53cNYasLITPJhjSWLljuERx%2FF%2Fpgtd5li3CkZakfzDn6gZqSW99adggyCVlAZSno%2FII85U3v%2ByX4YeXlFutM47lWzg%2Ffn8F2k2z%2Bxd7UjiotKSDHMNX2jZk2k8e5JsuDzJ%2FKASJF%2BiiN0D6BH2Q7L%2BUBKvQ6GGF9%2BMLB9jOTIFyZLv9sb8jok3%2F5oBPkpG3EMTv4SjWrPrse9oLxjxMiYI%2FERKgIejVzyADExGRVI8xAfUsJMk8Dan%2FTjAoK6NWjFFvZ8JNDYnWnzKOnVUIo44jklRyu%2FvaxWxWgLliUr0PMXu82LOe9O9JTlJYzx9ZKXS8Vf05zPiuzccmqS9LhHI%2FIEcHTYhYInjspML82mBkVhHFMY%2BDigNsD53DDv%2Fao5qRqON74a18H2YGSHt5FdqhjoFk7%2FAyaIa0KVV9yudseZnaO2seR84E8YP7NaL6y3UMC%2F9SZ%2BjOWe8wLfCbNtwLME%2FWSb3FxPnoGTNQ0EghAVEwwYLyvAY6pgFIk1Ihwa4noazdOQjHXAF%2Fr8kyS6qfmiVLBGaxuzX0UZWlyqSdI9fjTUuFSEgrEPjFYD85gKc2ZoLJzvHi0K9XV45Md9WRJ%2FIGm9lO3QyxmxKJSMIaB1ttOojzEMZ5CknvJGwfZPe0tWfdzBg2dQqDoShYCFn9SRrODJNl3o6ynL9Z%2F8mhJ49P5iOmdTh09zwIxgkACoIpX%2B97Uwp9lAb2eLB9Qpby&X-Amz-Signature=ca135915d7d404f955263f43a8cfe932f20fb10e6a43976b2d08c4f9de411f30&X-Amz-SignedHeaders=host&x-id=GetObject)
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


