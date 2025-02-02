

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662R72GVM4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011146Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD3JeEQeW7ctpB3F4NzYQXF48YYj8hjZTrdI5%2FCD%2FdahwIhAKGqYYGjgklhaXVtzolNrwF0rSYbg7okJfM2evy62hL9KogECOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz0KWmdNRpjNYTlWfAq3ANRYhV4w3wdqUNqWVM%2BBcC3956xI8IZs9lYiI%2F7%2FvR9aBv17RYjtmMIhnjuVUyrXoR0dYJHfHkG8TNRuL%2BISL2WT2vwta3eo5fgv3fsPLnWCOmkGrHZqMy2s5Nwgz4rQzAbMabhJaxkad%2BVsuwzEPENDda5TfKlIK%2Fl190mVojzxe23tqzhJf8%2B%2BaAyPY%2BJr190sQLYg4xL4dqH5IQn5FN2x%2B%2FYsPfWtgSO90yaOTXrY69LWy1r70iB96o9f469OTQsHa4No%2Bu%2FZrTUZ%2FaGGfdWemFUkJ8R4KmYMLg22IOxc7Y%2FvM0oWRnWR1OzDF9K8MXyEHDT7h%2F7iYaYaNORiAMnnNz%2BCpun%2Feamd0gtVKBk4mhzSGX%2BQvyC0qn8nxHtsT2bnoQ21HEdpHZY2WHS%2FwmVLUw59na8K8XDV58pB9oPud4yvRTLIE5Xv9ib5Hae%2BgAdKPEPa6JSXt3fWu5H1HxS%2FpNGeipxdWDn89KIZgZwDObRwnGHzlxW8FTMvJD9YDTaYf4rPpLsAJtz%2F0XK%2BeAuPL3LGduF8BYwdr2sTObMHnI19599WfB%2F9GXdlf7snonL7DOP5XT%2FLuk82Cvn0koCZNidgaw%2BNz%2FBn69XOsUvdROgvHQ05JkI3711EjCW8vq8BjqkAXh3Htxo%2F6VZYwlGE0tcSs3n5P1uT5bog3ZqcuxQvpUWPptZ3f%2B4b9EWm7QxyMzd0zojSZ0xSrECzmC0P3a%2F9%2BBWmVX7Ta1rwuAMnRihNtShc7Cb%2B1yS%2BQGOLstabveZXIU5BuHrv9a4qFpUbMfKkvnS0G2MjKuebW5MPAEKLmvUVyoqarxoKLxMeKNw5cShYlkZvKqOuluPiNdzTOoeeVA8epCS&X-Amz-Signature=4aab8326a0fb21c98bd84ce6c3aa6f92244db692649f426bf06d19b185bf6380&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RNCTJLI6%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCe7bIdEJu%2Bf9I5XRzaj6fYM0d72nR6J9XDpVABkUH7vgIhAODUaz6bWCtHDrbz0YnWijrTYkt1Lore%2BNI4pGP2jDxsKogECOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx8yrrvgi9WiySPEZsq3ANlIkryV9LODPmDCkPXM6%2B69Lp3HE%2BpNeR7pYlsMn6InAiI1LhTYcv%2FkwIpeB%2BBxZx4n5DJk1p1WPQHVrw5a6KgeNdd%2F4vfjoX9iDAqoxUhpE1FkaqTpgMQ1MqAc0B2eJD%2B2D0wlprZ5buyOJVlQTxAQsJf176Nc4eVJbdn7HquASCJkFP%2FEDeQrVSFQn6SXFBy5NX9%2BT245bB%2F2jRiftWdue%2BkDlICdUN2yqcs71lHDfwt6OBashfUdCnAqEeKOWHkmM81NFomgr41fox%2B2D8%2BNHfDiQ2o5MWoee3dGzAUU72suHw%2F8LTAQt2OyVs6poorH4QYV%2BP%2BIqVRJnmGP4BNSGEvzr4gArUaw%2FomRY3QGLhy%2FTC4FNGV3alNXL4Iy0aTAR5YtMj3gp1olezCv4soOnbfJSlkT5KCvU3%2Fjw5vMJbSOphJcN666XOaPDuBcZ1sHPQLWYDuD09mMJJ84g37LUpJPgazVJcWOZBOgxyCfBJMAB6xrvDQauOybq6yn82WA3TWXPQoNS%2FVL0znuZWHL9a1suxUE49sRPy7GcmJTPWptAAFkMgB4%2B6d1NnIBMKo7StCtAvDdi331PKm9cqWniBziVaO9n%2Ffu6G6WYK6Dlu0629jqXs%2BAgI72zC88fq8BjqkARS86fpSJwkvaTd9DYj6kyeOU%2FmlbESLSRrwB%2BzP0XrmwABz7yh7cflcLiJP4HywxAXIdoo9IR%2B%2FO4OkqXRiorAvIBQBZygrx%2F9SpOp9Nir3HKkTWVUjqxm6wIqGwmTqG8%2F77FJ7qeFlkK6ugqAivjvH9yaKJ5vuNSXy1DaoessOldZSZiNkZOsUc3Tb8vubIkH4EIPPmqHrtgth%2BHd%2BtdM0IuFq&X-Amz-Signature=0a7445943dc2c879735bd57cc57a075997a4d538e17d1bec912a985d7ac334ad&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RNCTJLI6%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCe7bIdEJu%2Bf9I5XRzaj6fYM0d72nR6J9XDpVABkUH7vgIhAODUaz6bWCtHDrbz0YnWijrTYkt1Lore%2BNI4pGP2jDxsKogECOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx8yrrvgi9WiySPEZsq3ANlIkryV9LODPmDCkPXM6%2B69Lp3HE%2BpNeR7pYlsMn6InAiI1LhTYcv%2FkwIpeB%2BBxZx4n5DJk1p1WPQHVrw5a6KgeNdd%2F4vfjoX9iDAqoxUhpE1FkaqTpgMQ1MqAc0B2eJD%2B2D0wlprZ5buyOJVlQTxAQsJf176Nc4eVJbdn7HquASCJkFP%2FEDeQrVSFQn6SXFBy5NX9%2BT245bB%2F2jRiftWdue%2BkDlICdUN2yqcs71lHDfwt6OBashfUdCnAqEeKOWHkmM81NFomgr41fox%2B2D8%2BNHfDiQ2o5MWoee3dGzAUU72suHw%2F8LTAQt2OyVs6poorH4QYV%2BP%2BIqVRJnmGP4BNSGEvzr4gArUaw%2FomRY3QGLhy%2FTC4FNGV3alNXL4Iy0aTAR5YtMj3gp1olezCv4soOnbfJSlkT5KCvU3%2Fjw5vMJbSOphJcN666XOaPDuBcZ1sHPQLWYDuD09mMJJ84g37LUpJPgazVJcWOZBOgxyCfBJMAB6xrvDQauOybq6yn82WA3TWXPQoNS%2FVL0znuZWHL9a1suxUE49sRPy7GcmJTPWptAAFkMgB4%2B6d1NnIBMKo7StCtAvDdi331PKm9cqWniBziVaO9n%2Ffu6G6WYK6Dlu0629jqXs%2BAgI72zC88fq8BjqkARS86fpSJwkvaTd9DYj6kyeOU%2FmlbESLSRrwB%2BzP0XrmwABz7yh7cflcLiJP4HywxAXIdoo9IR%2B%2FO4OkqXRiorAvIBQBZygrx%2F9SpOp9Nir3HKkTWVUjqxm6wIqGwmTqG8%2F77FJ7qeFlkK6ugqAivjvH9yaKJ5vuNSXy1DaoessOldZSZiNkZOsUc3Tb8vubIkH4EIPPmqHrtgth%2BHd%2BtdM0IuFq&X-Amz-Signature=c691311e5e0689c0d2fd4369df874096a35f92618bc6367b817de061c783efc1&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RNCTJLI6%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCe7bIdEJu%2Bf9I5XRzaj6fYM0d72nR6J9XDpVABkUH7vgIhAODUaz6bWCtHDrbz0YnWijrTYkt1Lore%2BNI4pGP2jDxsKogECOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx8yrrvgi9WiySPEZsq3ANlIkryV9LODPmDCkPXM6%2B69Lp3HE%2BpNeR7pYlsMn6InAiI1LhTYcv%2FkwIpeB%2BBxZx4n5DJk1p1WPQHVrw5a6KgeNdd%2F4vfjoX9iDAqoxUhpE1FkaqTpgMQ1MqAc0B2eJD%2B2D0wlprZ5buyOJVlQTxAQsJf176Nc4eVJbdn7HquASCJkFP%2FEDeQrVSFQn6SXFBy5NX9%2BT245bB%2F2jRiftWdue%2BkDlICdUN2yqcs71lHDfwt6OBashfUdCnAqEeKOWHkmM81NFomgr41fox%2B2D8%2BNHfDiQ2o5MWoee3dGzAUU72suHw%2F8LTAQt2OyVs6poorH4QYV%2BP%2BIqVRJnmGP4BNSGEvzr4gArUaw%2FomRY3QGLhy%2FTC4FNGV3alNXL4Iy0aTAR5YtMj3gp1olezCv4soOnbfJSlkT5KCvU3%2Fjw5vMJbSOphJcN666XOaPDuBcZ1sHPQLWYDuD09mMJJ84g37LUpJPgazVJcWOZBOgxyCfBJMAB6xrvDQauOybq6yn82WA3TWXPQoNS%2FVL0znuZWHL9a1suxUE49sRPy7GcmJTPWptAAFkMgB4%2B6d1NnIBMKo7StCtAvDdi331PKm9cqWniBziVaO9n%2Ffu6G6WYK6Dlu0629jqXs%2BAgI72zC88fq8BjqkARS86fpSJwkvaTd9DYj6kyeOU%2FmlbESLSRrwB%2BzP0XrmwABz7yh7cflcLiJP4HywxAXIdoo9IR%2B%2FO4OkqXRiorAvIBQBZygrx%2F9SpOp9Nir3HKkTWVUjqxm6wIqGwmTqG8%2F77FJ7qeFlkK6ugqAivjvH9yaKJ5vuNSXy1DaoessOldZSZiNkZOsUc3Tb8vubIkH4EIPPmqHrtgth%2BHd%2BtdM0IuFq&X-Amz-Signature=6932d8018c33940421bb7d8e0790bbcf185979e4b2ec3fb9399ffaa729677d0c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RNCTJLI6%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCe7bIdEJu%2Bf9I5XRzaj6fYM0d72nR6J9XDpVABkUH7vgIhAODUaz6bWCtHDrbz0YnWijrTYkt1Lore%2BNI4pGP2jDxsKogECOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx8yrrvgi9WiySPEZsq3ANlIkryV9LODPmDCkPXM6%2B69Lp3HE%2BpNeR7pYlsMn6InAiI1LhTYcv%2FkwIpeB%2BBxZx4n5DJk1p1WPQHVrw5a6KgeNdd%2F4vfjoX9iDAqoxUhpE1FkaqTpgMQ1MqAc0B2eJD%2B2D0wlprZ5buyOJVlQTxAQsJf176Nc4eVJbdn7HquASCJkFP%2FEDeQrVSFQn6SXFBy5NX9%2BT245bB%2F2jRiftWdue%2BkDlICdUN2yqcs71lHDfwt6OBashfUdCnAqEeKOWHkmM81NFomgr41fox%2B2D8%2BNHfDiQ2o5MWoee3dGzAUU72suHw%2F8LTAQt2OyVs6poorH4QYV%2BP%2BIqVRJnmGP4BNSGEvzr4gArUaw%2FomRY3QGLhy%2FTC4FNGV3alNXL4Iy0aTAR5YtMj3gp1olezCv4soOnbfJSlkT5KCvU3%2Fjw5vMJbSOphJcN666XOaPDuBcZ1sHPQLWYDuD09mMJJ84g37LUpJPgazVJcWOZBOgxyCfBJMAB6xrvDQauOybq6yn82WA3TWXPQoNS%2FVL0znuZWHL9a1suxUE49sRPy7GcmJTPWptAAFkMgB4%2B6d1NnIBMKo7StCtAvDdi331PKm9cqWniBziVaO9n%2Ffu6G6WYK6Dlu0629jqXs%2BAgI72zC88fq8BjqkARS86fpSJwkvaTd9DYj6kyeOU%2FmlbESLSRrwB%2BzP0XrmwABz7yh7cflcLiJP4HywxAXIdoo9IR%2B%2FO4OkqXRiorAvIBQBZygrx%2F9SpOp9Nir3HKkTWVUjqxm6wIqGwmTqG8%2F77FJ7qeFlkK6ugqAivjvH9yaKJ5vuNSXy1DaoessOldZSZiNkZOsUc3Tb8vubIkH4EIPPmqHrtgth%2BHd%2BtdM0IuFq&X-Amz-Signature=cc17908c950dfb4de9ecffb51a9c9c29a2bee89ae684d1299b4be15b76dfa081&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RNCTJLI6%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCe7bIdEJu%2Bf9I5XRzaj6fYM0d72nR6J9XDpVABkUH7vgIhAODUaz6bWCtHDrbz0YnWijrTYkt1Lore%2BNI4pGP2jDxsKogECOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx8yrrvgi9WiySPEZsq3ANlIkryV9LODPmDCkPXM6%2B69Lp3HE%2BpNeR7pYlsMn6InAiI1LhTYcv%2FkwIpeB%2BBxZx4n5DJk1p1WPQHVrw5a6KgeNdd%2F4vfjoX9iDAqoxUhpE1FkaqTpgMQ1MqAc0B2eJD%2B2D0wlprZ5buyOJVlQTxAQsJf176Nc4eVJbdn7HquASCJkFP%2FEDeQrVSFQn6SXFBy5NX9%2BT245bB%2F2jRiftWdue%2BkDlICdUN2yqcs71lHDfwt6OBashfUdCnAqEeKOWHkmM81NFomgr41fox%2B2D8%2BNHfDiQ2o5MWoee3dGzAUU72suHw%2F8LTAQt2OyVs6poorH4QYV%2BP%2BIqVRJnmGP4BNSGEvzr4gArUaw%2FomRY3QGLhy%2FTC4FNGV3alNXL4Iy0aTAR5YtMj3gp1olezCv4soOnbfJSlkT5KCvU3%2Fjw5vMJbSOphJcN666XOaPDuBcZ1sHPQLWYDuD09mMJJ84g37LUpJPgazVJcWOZBOgxyCfBJMAB6xrvDQauOybq6yn82WA3TWXPQoNS%2FVL0znuZWHL9a1suxUE49sRPy7GcmJTPWptAAFkMgB4%2B6d1NnIBMKo7StCtAvDdi331PKm9cqWniBziVaO9n%2Ffu6G6WYK6Dlu0629jqXs%2BAgI72zC88fq8BjqkARS86fpSJwkvaTd9DYj6kyeOU%2FmlbESLSRrwB%2BzP0XrmwABz7yh7cflcLiJP4HywxAXIdoo9IR%2B%2FO4OkqXRiorAvIBQBZygrx%2F9SpOp9Nir3HKkTWVUjqxm6wIqGwmTqG8%2F77FJ7qeFlkK6ugqAivjvH9yaKJ5vuNSXy1DaoessOldZSZiNkZOsUc3Tb8vubIkH4EIPPmqHrtgth%2BHd%2BtdM0IuFq&X-Amz-Signature=8b79389385a46cd5e96e486c664b5aab3df4f8449fcb427bc6d0962c5794bd40&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662R72GVM4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011146Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD3JeEQeW7ctpB3F4NzYQXF48YYj8hjZTrdI5%2FCD%2FdahwIhAKGqYYGjgklhaXVtzolNrwF0rSYbg7okJfM2evy62hL9KogECOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz0KWmdNRpjNYTlWfAq3ANRYhV4w3wdqUNqWVM%2BBcC3956xI8IZs9lYiI%2F7%2FvR9aBv17RYjtmMIhnjuVUyrXoR0dYJHfHkG8TNRuL%2BISL2WT2vwta3eo5fgv3fsPLnWCOmkGrHZqMy2s5Nwgz4rQzAbMabhJaxkad%2BVsuwzEPENDda5TfKlIK%2Fl190mVojzxe23tqzhJf8%2B%2BaAyPY%2BJr190sQLYg4xL4dqH5IQn5FN2x%2B%2FYsPfWtgSO90yaOTXrY69LWy1r70iB96o9f469OTQsHa4No%2Bu%2FZrTUZ%2FaGGfdWemFUkJ8R4KmYMLg22IOxc7Y%2FvM0oWRnWR1OzDF9K8MXyEHDT7h%2F7iYaYaNORiAMnnNz%2BCpun%2Feamd0gtVKBk4mhzSGX%2BQvyC0qn8nxHtsT2bnoQ21HEdpHZY2WHS%2FwmVLUw59na8K8XDV58pB9oPud4yvRTLIE5Xv9ib5Hae%2BgAdKPEPa6JSXt3fWu5H1HxS%2FpNGeipxdWDn89KIZgZwDObRwnGHzlxW8FTMvJD9YDTaYf4rPpLsAJtz%2F0XK%2BeAuPL3LGduF8BYwdr2sTObMHnI19599WfB%2F9GXdlf7snonL7DOP5XT%2FLuk82Cvn0koCZNidgaw%2BNz%2FBn69XOsUvdROgvHQ05JkI3711EjCW8vq8BjqkAXh3Htxo%2F6VZYwlGE0tcSs3n5P1uT5bog3ZqcuxQvpUWPptZ3f%2B4b9EWm7QxyMzd0zojSZ0xSrECzmC0P3a%2F9%2BBWmVX7Ta1rwuAMnRihNtShc7Cb%2B1yS%2BQGOLstabveZXIU5BuHrv9a4qFpUbMfKkvnS0G2MjKuebW5MPAEKLmvUVyoqarxoKLxMeKNw5cShYlkZvKqOuluPiNdzTOoeeVA8epCS&X-Amz-Signature=271164b7662662b090c0541af0c98f71b4d1f37b7bdf2614328e5781e8cea3b8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662R72GVM4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011146Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD3JeEQeW7ctpB3F4NzYQXF48YYj8hjZTrdI5%2FCD%2FdahwIhAKGqYYGjgklhaXVtzolNrwF0rSYbg7okJfM2evy62hL9KogECOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz0KWmdNRpjNYTlWfAq3ANRYhV4w3wdqUNqWVM%2BBcC3956xI8IZs9lYiI%2F7%2FvR9aBv17RYjtmMIhnjuVUyrXoR0dYJHfHkG8TNRuL%2BISL2WT2vwta3eo5fgv3fsPLnWCOmkGrHZqMy2s5Nwgz4rQzAbMabhJaxkad%2BVsuwzEPENDda5TfKlIK%2Fl190mVojzxe23tqzhJf8%2B%2BaAyPY%2BJr190sQLYg4xL4dqH5IQn5FN2x%2B%2FYsPfWtgSO90yaOTXrY69LWy1r70iB96o9f469OTQsHa4No%2Bu%2FZrTUZ%2FaGGfdWemFUkJ8R4KmYMLg22IOxc7Y%2FvM0oWRnWR1OzDF9K8MXyEHDT7h%2F7iYaYaNORiAMnnNz%2BCpun%2Feamd0gtVKBk4mhzSGX%2BQvyC0qn8nxHtsT2bnoQ21HEdpHZY2WHS%2FwmVLUw59na8K8XDV58pB9oPud4yvRTLIE5Xv9ib5Hae%2BgAdKPEPa6JSXt3fWu5H1HxS%2FpNGeipxdWDn89KIZgZwDObRwnGHzlxW8FTMvJD9YDTaYf4rPpLsAJtz%2F0XK%2BeAuPL3LGduF8BYwdr2sTObMHnI19599WfB%2F9GXdlf7snonL7DOP5XT%2FLuk82Cvn0koCZNidgaw%2BNz%2FBn69XOsUvdROgvHQ05JkI3711EjCW8vq8BjqkAXh3Htxo%2F6VZYwlGE0tcSs3n5P1uT5bog3ZqcuxQvpUWPptZ3f%2B4b9EWm7QxyMzd0zojSZ0xSrECzmC0P3a%2F9%2BBWmVX7Ta1rwuAMnRihNtShc7Cb%2B1yS%2BQGOLstabveZXIU5BuHrv9a4qFpUbMfKkvnS0G2MjKuebW5MPAEKLmvUVyoqarxoKLxMeKNw5cShYlkZvKqOuluPiNdzTOoeeVA8epCS&X-Amz-Signature=d19b67e6743541bcb4bb6880e1c25099384c4e08f13a7a3bb973785aa1883f38&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662R72GVM4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011146Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD3JeEQeW7ctpB3F4NzYQXF48YYj8hjZTrdI5%2FCD%2FdahwIhAKGqYYGjgklhaXVtzolNrwF0rSYbg7okJfM2evy62hL9KogECOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz0KWmdNRpjNYTlWfAq3ANRYhV4w3wdqUNqWVM%2BBcC3956xI8IZs9lYiI%2F7%2FvR9aBv17RYjtmMIhnjuVUyrXoR0dYJHfHkG8TNRuL%2BISL2WT2vwta3eo5fgv3fsPLnWCOmkGrHZqMy2s5Nwgz4rQzAbMabhJaxkad%2BVsuwzEPENDda5TfKlIK%2Fl190mVojzxe23tqzhJf8%2B%2BaAyPY%2BJr190sQLYg4xL4dqH5IQn5FN2x%2B%2FYsPfWtgSO90yaOTXrY69LWy1r70iB96o9f469OTQsHa4No%2Bu%2FZrTUZ%2FaGGfdWemFUkJ8R4KmYMLg22IOxc7Y%2FvM0oWRnWR1OzDF9K8MXyEHDT7h%2F7iYaYaNORiAMnnNz%2BCpun%2Feamd0gtVKBk4mhzSGX%2BQvyC0qn8nxHtsT2bnoQ21HEdpHZY2WHS%2FwmVLUw59na8K8XDV58pB9oPud4yvRTLIE5Xv9ib5Hae%2BgAdKPEPa6JSXt3fWu5H1HxS%2FpNGeipxdWDn89KIZgZwDObRwnGHzlxW8FTMvJD9YDTaYf4rPpLsAJtz%2F0XK%2BeAuPL3LGduF8BYwdr2sTObMHnI19599WfB%2F9GXdlf7snonL7DOP5XT%2FLuk82Cvn0koCZNidgaw%2BNz%2FBn69XOsUvdROgvHQ05JkI3711EjCW8vq8BjqkAXh3Htxo%2F6VZYwlGE0tcSs3n5P1uT5bog3ZqcuxQvpUWPptZ3f%2B4b9EWm7QxyMzd0zojSZ0xSrECzmC0P3a%2F9%2BBWmVX7Ta1rwuAMnRihNtShc7Cb%2B1yS%2BQGOLstabveZXIU5BuHrv9a4qFpUbMfKkvnS0G2MjKuebW5MPAEKLmvUVyoqarxoKLxMeKNw5cShYlkZvKqOuluPiNdzTOoeeVA8epCS&X-Amz-Signature=58d5a927205cc1ef87c704d8ec78855efd853c1235f63394117a21e1746fa1f7&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662R72GVM4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011146Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD3JeEQeW7ctpB3F4NzYQXF48YYj8hjZTrdI5%2FCD%2FdahwIhAKGqYYGjgklhaXVtzolNrwF0rSYbg7okJfM2evy62hL9KogECOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz0KWmdNRpjNYTlWfAq3ANRYhV4w3wdqUNqWVM%2BBcC3956xI8IZs9lYiI%2F7%2FvR9aBv17RYjtmMIhnjuVUyrXoR0dYJHfHkG8TNRuL%2BISL2WT2vwta3eo5fgv3fsPLnWCOmkGrHZqMy2s5Nwgz4rQzAbMabhJaxkad%2BVsuwzEPENDda5TfKlIK%2Fl190mVojzxe23tqzhJf8%2B%2BaAyPY%2BJr190sQLYg4xL4dqH5IQn5FN2x%2B%2FYsPfWtgSO90yaOTXrY69LWy1r70iB96o9f469OTQsHa4No%2Bu%2FZrTUZ%2FaGGfdWemFUkJ8R4KmYMLg22IOxc7Y%2FvM0oWRnWR1OzDF9K8MXyEHDT7h%2F7iYaYaNORiAMnnNz%2BCpun%2Feamd0gtVKBk4mhzSGX%2BQvyC0qn8nxHtsT2bnoQ21HEdpHZY2WHS%2FwmVLUw59na8K8XDV58pB9oPud4yvRTLIE5Xv9ib5Hae%2BgAdKPEPa6JSXt3fWu5H1HxS%2FpNGeipxdWDn89KIZgZwDObRwnGHzlxW8FTMvJD9YDTaYf4rPpLsAJtz%2F0XK%2BeAuPL3LGduF8BYwdr2sTObMHnI19599WfB%2F9GXdlf7snonL7DOP5XT%2FLuk82Cvn0koCZNidgaw%2BNz%2FBn69XOsUvdROgvHQ05JkI3711EjCW8vq8BjqkAXh3Htxo%2F6VZYwlGE0tcSs3n5P1uT5bog3ZqcuxQvpUWPptZ3f%2B4b9EWm7QxyMzd0zojSZ0xSrECzmC0P3a%2F9%2BBWmVX7Ta1rwuAMnRihNtShc7Cb%2B1yS%2BQGOLstabveZXIU5BuHrv9a4qFpUbMfKkvnS0G2MjKuebW5MPAEKLmvUVyoqarxoKLxMeKNw5cShYlkZvKqOuluPiNdzTOoeeVA8epCS&X-Amz-Signature=7a7b32d06e92133bcbb0c119b6aecd7c379050b854008b349ff636fa8c445b1f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662R72GVM4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011146Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD3JeEQeW7ctpB3F4NzYQXF48YYj8hjZTrdI5%2FCD%2FdahwIhAKGqYYGjgklhaXVtzolNrwF0rSYbg7okJfM2evy62hL9KogECOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz0KWmdNRpjNYTlWfAq3ANRYhV4w3wdqUNqWVM%2BBcC3956xI8IZs9lYiI%2F7%2FvR9aBv17RYjtmMIhnjuVUyrXoR0dYJHfHkG8TNRuL%2BISL2WT2vwta3eo5fgv3fsPLnWCOmkGrHZqMy2s5Nwgz4rQzAbMabhJaxkad%2BVsuwzEPENDda5TfKlIK%2Fl190mVojzxe23tqzhJf8%2B%2BaAyPY%2BJr190sQLYg4xL4dqH5IQn5FN2x%2B%2FYsPfWtgSO90yaOTXrY69LWy1r70iB96o9f469OTQsHa4No%2Bu%2FZrTUZ%2FaGGfdWemFUkJ8R4KmYMLg22IOxc7Y%2FvM0oWRnWR1OzDF9K8MXyEHDT7h%2F7iYaYaNORiAMnnNz%2BCpun%2Feamd0gtVKBk4mhzSGX%2BQvyC0qn8nxHtsT2bnoQ21HEdpHZY2WHS%2FwmVLUw59na8K8XDV58pB9oPud4yvRTLIE5Xv9ib5Hae%2BgAdKPEPa6JSXt3fWu5H1HxS%2FpNGeipxdWDn89KIZgZwDObRwnGHzlxW8FTMvJD9YDTaYf4rPpLsAJtz%2F0XK%2BeAuPL3LGduF8BYwdr2sTObMHnI19599WfB%2F9GXdlf7snonL7DOP5XT%2FLuk82Cvn0koCZNidgaw%2BNz%2FBn69XOsUvdROgvHQ05JkI3711EjCW8vq8BjqkAXh3Htxo%2F6VZYwlGE0tcSs3n5P1uT5bog3ZqcuxQvpUWPptZ3f%2B4b9EWm7QxyMzd0zojSZ0xSrECzmC0P3a%2F9%2BBWmVX7Ta1rwuAMnRihNtShc7Cb%2B1yS%2BQGOLstabveZXIU5BuHrv9a4qFpUbMfKkvnS0G2MjKuebW5MPAEKLmvUVyoqarxoKLxMeKNw5cShYlkZvKqOuluPiNdzTOoeeVA8epCS&X-Amz-Signature=cbd321e0187c0b355ad2d168dee5c9c0d6b579db7ef57d488e718c5e3c29f537&X-Amz-SignedHeaders=host&x-id=GetObject)
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


