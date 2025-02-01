

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667T2XG7IB%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDkFrQesMHZfojJMYSNyFZP0sSYrEsXV6uUATy8EEwlkAiEAruO1nVsJuWJc9Fb5CWR5fleKknvKZIy5r70T8AR03MkqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKCeiz%2F4GQ9D0KM51SrcA6oU3e0T%2BOsmQIOevKO%2BBufpnR1FueFmw8pD3gon9mmKsmMFtSsftLHwUrDjctDpRTbUNspumDCvfVTnUbaLgR242rsR1T4VzY8WfVDaROo7K7IjntGyKFTYFhMwzZqYIhgWWZcqk0pbcAx2NK4RUBz8jYQtpiaDROLlY%2Fgdye2u8KXBSwSMhsL1C9%2B4tnK2EtUbMhXchWyrGrMSAsw4JawSLeVebs5x%2BwCwmKJGtcLBKTh%2F955M7vlpxCgVUlRLrvvYPGiHSCgzCZkGVpgprnh2xNimcADAOudt28ETr0jxM1xMxn16BFj3njNM8LTQq6cvrqyqpzKLZAhlO2t1CSyplYXJsQibtIuUW4exJAAbiaUlxr3jBVFixSN4klzPQef3PzAspUJtACVkPu2WVubhFg7oIcfzB70MW0I7t9btq69EGgh9hULj%2BCkXBRygYS71Qkb6qIfzdEGWKz5P8Rv%2FNvmwDbOIg0Jla0V9NVo%2FRnm%2BvPNrUFOutrCTVjatFPVhrNaqj%2BKlM2ACXJsogWIGKLMKN3pYdXYzGwVv1xTUWb5mWsn2dpBi7eMyz4a2HZ9slzw19TaPTQ55FrfrjlEbgM0XeHmDfPmzGM3Y2M71RYgXfwZs%2FPPk1x8FMKTH%2BLwGOqUBC8LQUlQyW9TevxnvEYx6mB04c5mdyWirs6ivD38XjwXRzfK7vSos8owJmTXWBvrhOC2Fdrfn86la5mKHDpJihyW1pds5PD83CvwDDyB9iuVnMj2jkUTe5zIi7gSHsq5K%2FUiXZ9wPENeHZkp3ABvQnBZvCC13REn%2FojTst0SSjwco5HpFTiYXV6RPBCxw0SH1%2FPJHLrKZnDB8YeKb2ES02yPuq0tE&X-Amz-Signature=2b4352729c666c547f766ad374744354f8ab3e57d47f58163ee89a1c23b76464&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YSLBUM4F%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141154Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEjgr0j5wVbG5I3arMiWB%2FYRPcwAunZgwlsVA8%2FZAEaVAiA9BXOe2bmozfxYHSL%2FGk82g1qoykGLKsNhQkaa6XkoPCqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMoY0kjNIcVmk%2BdVu0KtwDgod2EAAyUyeBIvmPCJjYaCb3lp2jmFbaGvFgsKRR27vaLwZlhKAufe%2FbNuM%2BSvnpqs75glk6nJVl%2Fs0yp3nBdQfhotXDfFyaX%2Ft3kjq5660v2OM8T2HyX2VThvD7OV3iBSq6Q2lci8YkqOfJFo7He7xF%2BMRyWjzoVn3eSZxdStQfs06YqSLbNM1ak8yzsmnz39DSm4hf28pg5fq9Io6KGbXDpjwt21dN9BPYRVO0ui9bCswtrXHIN4IolAJs%2BDsTpEYoHsOYasQ3Kh5pCK0tWu2OmbkHtkZoZ%2F3jD0SWDmnZPRZ1ExuxsnnLBoXvJk4oZD9eHuDOdV8vUHp2NBVzsnFUQUR8rlinxrVTkNzVMxccByK3UyqMq6soOnW1%2F1k84pVFDS7C6HFZE%2BRRSAHCzlwUQILiKzVLrskPFcUMGrktJAOU%2Fyj67QQgfVi96Iv%2Fpktct0vKW14RnxxS9N4Kh5VN0Y3iPDDpk%2B5bv2vg8h6rj3glZ12wU2cJ0Qp92J65%2F1Wj%2FNgvzt9zUYSbrLHGL0VR%2BvjzGB%2Bb6kkmMNNzHEDO0CwewsmZ94iZ3NxNNGtZ%2BFXUh6K0nZltRawaPXNt%2FtMcqjkhQVkbaNKJ561vR2lVcl33JQNum5K7ihkw68f4vAY6pgHRFCT4paASxaMMT2aw1WvpxkrYCmkd3e560NYY1nj5DvtI7C5BYk3vyTSp50fflDQ91RngLAFTW9WXQeXXGNI0yFA32xLKGRHGFDQMOPbJTrQgyg7%2FUaTjb2mKUUok93H5JftN3I5b198IxD%2BNetm0KDHB5n41TC0kZCxCGfeG%2Fej8j0AYnhbtv9oqTcGPUd7cb%2BLf1NxKkeMKLFZ9DvGwK8mQwouZ&X-Amz-Signature=539a64a62fb707b3418ee711ec2133c8cab719105116a1ec8cbbe66396d225b6&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YSLBUM4F%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141154Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEjgr0j5wVbG5I3arMiWB%2FYRPcwAunZgwlsVA8%2FZAEaVAiA9BXOe2bmozfxYHSL%2FGk82g1qoykGLKsNhQkaa6XkoPCqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMoY0kjNIcVmk%2BdVu0KtwDgod2EAAyUyeBIvmPCJjYaCb3lp2jmFbaGvFgsKRR27vaLwZlhKAufe%2FbNuM%2BSvnpqs75glk6nJVl%2Fs0yp3nBdQfhotXDfFyaX%2Ft3kjq5660v2OM8T2HyX2VThvD7OV3iBSq6Q2lci8YkqOfJFo7He7xF%2BMRyWjzoVn3eSZxdStQfs06YqSLbNM1ak8yzsmnz39DSm4hf28pg5fq9Io6KGbXDpjwt21dN9BPYRVO0ui9bCswtrXHIN4IolAJs%2BDsTpEYoHsOYasQ3Kh5pCK0tWu2OmbkHtkZoZ%2F3jD0SWDmnZPRZ1ExuxsnnLBoXvJk4oZD9eHuDOdV8vUHp2NBVzsnFUQUR8rlinxrVTkNzVMxccByK3UyqMq6soOnW1%2F1k84pVFDS7C6HFZE%2BRRSAHCzlwUQILiKzVLrskPFcUMGrktJAOU%2Fyj67QQgfVi96Iv%2Fpktct0vKW14RnxxS9N4Kh5VN0Y3iPDDpk%2B5bv2vg8h6rj3glZ12wU2cJ0Qp92J65%2F1Wj%2FNgvzt9zUYSbrLHGL0VR%2BvjzGB%2Bb6kkmMNNzHEDO0CwewsmZ94iZ3NxNNGtZ%2BFXUh6K0nZltRawaPXNt%2FtMcqjkhQVkbaNKJ561vR2lVcl33JQNum5K7ihkw68f4vAY6pgHRFCT4paASxaMMT2aw1WvpxkrYCmkd3e560NYY1nj5DvtI7C5BYk3vyTSp50fflDQ91RngLAFTW9WXQeXXGNI0yFA32xLKGRHGFDQMOPbJTrQgyg7%2FUaTjb2mKUUok93H5JftN3I5b198IxD%2BNetm0KDHB5n41TC0kZCxCGfeG%2Fej8j0AYnhbtv9oqTcGPUd7cb%2BLf1NxKkeMKLFZ9DvGwK8mQwouZ&X-Amz-Signature=d9495e2846d83cc894206a47b4937771710cfccb7571692d454cb7e782b48bbc&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YSLBUM4F%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141154Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEjgr0j5wVbG5I3arMiWB%2FYRPcwAunZgwlsVA8%2FZAEaVAiA9BXOe2bmozfxYHSL%2FGk82g1qoykGLKsNhQkaa6XkoPCqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMoY0kjNIcVmk%2BdVu0KtwDgod2EAAyUyeBIvmPCJjYaCb3lp2jmFbaGvFgsKRR27vaLwZlhKAufe%2FbNuM%2BSvnpqs75glk6nJVl%2Fs0yp3nBdQfhotXDfFyaX%2Ft3kjq5660v2OM8T2HyX2VThvD7OV3iBSq6Q2lci8YkqOfJFo7He7xF%2BMRyWjzoVn3eSZxdStQfs06YqSLbNM1ak8yzsmnz39DSm4hf28pg5fq9Io6KGbXDpjwt21dN9BPYRVO0ui9bCswtrXHIN4IolAJs%2BDsTpEYoHsOYasQ3Kh5pCK0tWu2OmbkHtkZoZ%2F3jD0SWDmnZPRZ1ExuxsnnLBoXvJk4oZD9eHuDOdV8vUHp2NBVzsnFUQUR8rlinxrVTkNzVMxccByK3UyqMq6soOnW1%2F1k84pVFDS7C6HFZE%2BRRSAHCzlwUQILiKzVLrskPFcUMGrktJAOU%2Fyj67QQgfVi96Iv%2Fpktct0vKW14RnxxS9N4Kh5VN0Y3iPDDpk%2B5bv2vg8h6rj3glZ12wU2cJ0Qp92J65%2F1Wj%2FNgvzt9zUYSbrLHGL0VR%2BvjzGB%2Bb6kkmMNNzHEDO0CwewsmZ94iZ3NxNNGtZ%2BFXUh6K0nZltRawaPXNt%2FtMcqjkhQVkbaNKJ561vR2lVcl33JQNum5K7ihkw68f4vAY6pgHRFCT4paASxaMMT2aw1WvpxkrYCmkd3e560NYY1nj5DvtI7C5BYk3vyTSp50fflDQ91RngLAFTW9WXQeXXGNI0yFA32xLKGRHGFDQMOPbJTrQgyg7%2FUaTjb2mKUUok93H5JftN3I5b198IxD%2BNetm0KDHB5n41TC0kZCxCGfeG%2Fej8j0AYnhbtv9oqTcGPUd7cb%2BLf1NxKkeMKLFZ9DvGwK8mQwouZ&X-Amz-Signature=2e1f691d09bcaffe708addc7604e6700ad7aac10796db7a4bcc11f2b34fceb03&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YSLBUM4F%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141154Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEjgr0j5wVbG5I3arMiWB%2FYRPcwAunZgwlsVA8%2FZAEaVAiA9BXOe2bmozfxYHSL%2FGk82g1qoykGLKsNhQkaa6XkoPCqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMoY0kjNIcVmk%2BdVu0KtwDgod2EAAyUyeBIvmPCJjYaCb3lp2jmFbaGvFgsKRR27vaLwZlhKAufe%2FbNuM%2BSvnpqs75glk6nJVl%2Fs0yp3nBdQfhotXDfFyaX%2Ft3kjq5660v2OM8T2HyX2VThvD7OV3iBSq6Q2lci8YkqOfJFo7He7xF%2BMRyWjzoVn3eSZxdStQfs06YqSLbNM1ak8yzsmnz39DSm4hf28pg5fq9Io6KGbXDpjwt21dN9BPYRVO0ui9bCswtrXHIN4IolAJs%2BDsTpEYoHsOYasQ3Kh5pCK0tWu2OmbkHtkZoZ%2F3jD0SWDmnZPRZ1ExuxsnnLBoXvJk4oZD9eHuDOdV8vUHp2NBVzsnFUQUR8rlinxrVTkNzVMxccByK3UyqMq6soOnW1%2F1k84pVFDS7C6HFZE%2BRRSAHCzlwUQILiKzVLrskPFcUMGrktJAOU%2Fyj67QQgfVi96Iv%2Fpktct0vKW14RnxxS9N4Kh5VN0Y3iPDDpk%2B5bv2vg8h6rj3glZ12wU2cJ0Qp92J65%2F1Wj%2FNgvzt9zUYSbrLHGL0VR%2BvjzGB%2Bb6kkmMNNzHEDO0CwewsmZ94iZ3NxNNGtZ%2BFXUh6K0nZltRawaPXNt%2FtMcqjkhQVkbaNKJ561vR2lVcl33JQNum5K7ihkw68f4vAY6pgHRFCT4paASxaMMT2aw1WvpxkrYCmkd3e560NYY1nj5DvtI7C5BYk3vyTSp50fflDQ91RngLAFTW9WXQeXXGNI0yFA32xLKGRHGFDQMOPbJTrQgyg7%2FUaTjb2mKUUok93H5JftN3I5b198IxD%2BNetm0KDHB5n41TC0kZCxCGfeG%2Fej8j0AYnhbtv9oqTcGPUd7cb%2BLf1NxKkeMKLFZ9DvGwK8mQwouZ&X-Amz-Signature=d067d4891806bebb56a3951757443c392a1e0cb015c18e888aaa0be9ac4e90bf&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YSLBUM4F%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141154Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEjgr0j5wVbG5I3arMiWB%2FYRPcwAunZgwlsVA8%2FZAEaVAiA9BXOe2bmozfxYHSL%2FGk82g1qoykGLKsNhQkaa6XkoPCqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMoY0kjNIcVmk%2BdVu0KtwDgod2EAAyUyeBIvmPCJjYaCb3lp2jmFbaGvFgsKRR27vaLwZlhKAufe%2FbNuM%2BSvnpqs75glk6nJVl%2Fs0yp3nBdQfhotXDfFyaX%2Ft3kjq5660v2OM8T2HyX2VThvD7OV3iBSq6Q2lci8YkqOfJFo7He7xF%2BMRyWjzoVn3eSZxdStQfs06YqSLbNM1ak8yzsmnz39DSm4hf28pg5fq9Io6KGbXDpjwt21dN9BPYRVO0ui9bCswtrXHIN4IolAJs%2BDsTpEYoHsOYasQ3Kh5pCK0tWu2OmbkHtkZoZ%2F3jD0SWDmnZPRZ1ExuxsnnLBoXvJk4oZD9eHuDOdV8vUHp2NBVzsnFUQUR8rlinxrVTkNzVMxccByK3UyqMq6soOnW1%2F1k84pVFDS7C6HFZE%2BRRSAHCzlwUQILiKzVLrskPFcUMGrktJAOU%2Fyj67QQgfVi96Iv%2Fpktct0vKW14RnxxS9N4Kh5VN0Y3iPDDpk%2B5bv2vg8h6rj3glZ12wU2cJ0Qp92J65%2F1Wj%2FNgvzt9zUYSbrLHGL0VR%2BvjzGB%2Bb6kkmMNNzHEDO0CwewsmZ94iZ3NxNNGtZ%2BFXUh6K0nZltRawaPXNt%2FtMcqjkhQVkbaNKJ561vR2lVcl33JQNum5K7ihkw68f4vAY6pgHRFCT4paASxaMMT2aw1WvpxkrYCmkd3e560NYY1nj5DvtI7C5BYk3vyTSp50fflDQ91RngLAFTW9WXQeXXGNI0yFA32xLKGRHGFDQMOPbJTrQgyg7%2FUaTjb2mKUUok93H5JftN3I5b198IxD%2BNetm0KDHB5n41TC0kZCxCGfeG%2Fej8j0AYnhbtv9oqTcGPUd7cb%2BLf1NxKkeMKLFZ9DvGwK8mQwouZ&X-Amz-Signature=53aa811b1d335fdda32017c99f172b8a8a3fe7ad6472497ef21366afca096777&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667T2XG7IB%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDkFrQesMHZfojJMYSNyFZP0sSYrEsXV6uUATy8EEwlkAiEAruO1nVsJuWJc9Fb5CWR5fleKknvKZIy5r70T8AR03MkqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKCeiz%2F4GQ9D0KM51SrcA6oU3e0T%2BOsmQIOevKO%2BBufpnR1FueFmw8pD3gon9mmKsmMFtSsftLHwUrDjctDpRTbUNspumDCvfVTnUbaLgR242rsR1T4VzY8WfVDaROo7K7IjntGyKFTYFhMwzZqYIhgWWZcqk0pbcAx2NK4RUBz8jYQtpiaDROLlY%2Fgdye2u8KXBSwSMhsL1C9%2B4tnK2EtUbMhXchWyrGrMSAsw4JawSLeVebs5x%2BwCwmKJGtcLBKTh%2F955M7vlpxCgVUlRLrvvYPGiHSCgzCZkGVpgprnh2xNimcADAOudt28ETr0jxM1xMxn16BFj3njNM8LTQq6cvrqyqpzKLZAhlO2t1CSyplYXJsQibtIuUW4exJAAbiaUlxr3jBVFixSN4klzPQef3PzAspUJtACVkPu2WVubhFg7oIcfzB70MW0I7t9btq69EGgh9hULj%2BCkXBRygYS71Qkb6qIfzdEGWKz5P8Rv%2FNvmwDbOIg0Jla0V9NVo%2FRnm%2BvPNrUFOutrCTVjatFPVhrNaqj%2BKlM2ACXJsogWIGKLMKN3pYdXYzGwVv1xTUWb5mWsn2dpBi7eMyz4a2HZ9slzw19TaPTQ55FrfrjlEbgM0XeHmDfPmzGM3Y2M71RYgXfwZs%2FPPk1x8FMKTH%2BLwGOqUBC8LQUlQyW9TevxnvEYx6mB04c5mdyWirs6ivD38XjwXRzfK7vSos8owJmTXWBvrhOC2Fdrfn86la5mKHDpJihyW1pds5PD83CvwDDyB9iuVnMj2jkUTe5zIi7gSHsq5K%2FUiXZ9wPENeHZkp3ABvQnBZvCC13REn%2FojTst0SSjwco5HpFTiYXV6RPBCxw0SH1%2FPJHLrKZnDB8YeKb2ES02yPuq0tE&X-Amz-Signature=2280bf1ecb65a8b22d3eca0f657b58fd77b19dec1a4a76cdd3539f10ecebc29e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667T2XG7IB%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDkFrQesMHZfojJMYSNyFZP0sSYrEsXV6uUATy8EEwlkAiEAruO1nVsJuWJc9Fb5CWR5fleKknvKZIy5r70T8AR03MkqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKCeiz%2F4GQ9D0KM51SrcA6oU3e0T%2BOsmQIOevKO%2BBufpnR1FueFmw8pD3gon9mmKsmMFtSsftLHwUrDjctDpRTbUNspumDCvfVTnUbaLgR242rsR1T4VzY8WfVDaROo7K7IjntGyKFTYFhMwzZqYIhgWWZcqk0pbcAx2NK4RUBz8jYQtpiaDROLlY%2Fgdye2u8KXBSwSMhsL1C9%2B4tnK2EtUbMhXchWyrGrMSAsw4JawSLeVebs5x%2BwCwmKJGtcLBKTh%2F955M7vlpxCgVUlRLrvvYPGiHSCgzCZkGVpgprnh2xNimcADAOudt28ETr0jxM1xMxn16BFj3njNM8LTQq6cvrqyqpzKLZAhlO2t1CSyplYXJsQibtIuUW4exJAAbiaUlxr3jBVFixSN4klzPQef3PzAspUJtACVkPu2WVubhFg7oIcfzB70MW0I7t9btq69EGgh9hULj%2BCkXBRygYS71Qkb6qIfzdEGWKz5P8Rv%2FNvmwDbOIg0Jla0V9NVo%2FRnm%2BvPNrUFOutrCTVjatFPVhrNaqj%2BKlM2ACXJsogWIGKLMKN3pYdXYzGwVv1xTUWb5mWsn2dpBi7eMyz4a2HZ9slzw19TaPTQ55FrfrjlEbgM0XeHmDfPmzGM3Y2M71RYgXfwZs%2FPPk1x8FMKTH%2BLwGOqUBC8LQUlQyW9TevxnvEYx6mB04c5mdyWirs6ivD38XjwXRzfK7vSos8owJmTXWBvrhOC2Fdrfn86la5mKHDpJihyW1pds5PD83CvwDDyB9iuVnMj2jkUTe5zIi7gSHsq5K%2FUiXZ9wPENeHZkp3ABvQnBZvCC13REn%2FojTst0SSjwco5HpFTiYXV6RPBCxw0SH1%2FPJHLrKZnDB8YeKb2ES02yPuq0tE&X-Amz-Signature=4bb89ad401ac6ff21ce2b26daeb28357165be622144980894f0f1d630887fed7&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667T2XG7IB%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDkFrQesMHZfojJMYSNyFZP0sSYrEsXV6uUATy8EEwlkAiEAruO1nVsJuWJc9Fb5CWR5fleKknvKZIy5r70T8AR03MkqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKCeiz%2F4GQ9D0KM51SrcA6oU3e0T%2BOsmQIOevKO%2BBufpnR1FueFmw8pD3gon9mmKsmMFtSsftLHwUrDjctDpRTbUNspumDCvfVTnUbaLgR242rsR1T4VzY8WfVDaROo7K7IjntGyKFTYFhMwzZqYIhgWWZcqk0pbcAx2NK4RUBz8jYQtpiaDROLlY%2Fgdye2u8KXBSwSMhsL1C9%2B4tnK2EtUbMhXchWyrGrMSAsw4JawSLeVebs5x%2BwCwmKJGtcLBKTh%2F955M7vlpxCgVUlRLrvvYPGiHSCgzCZkGVpgprnh2xNimcADAOudt28ETr0jxM1xMxn16BFj3njNM8LTQq6cvrqyqpzKLZAhlO2t1CSyplYXJsQibtIuUW4exJAAbiaUlxr3jBVFixSN4klzPQef3PzAspUJtACVkPu2WVubhFg7oIcfzB70MW0I7t9btq69EGgh9hULj%2BCkXBRygYS71Qkb6qIfzdEGWKz5P8Rv%2FNvmwDbOIg0Jla0V9NVo%2FRnm%2BvPNrUFOutrCTVjatFPVhrNaqj%2BKlM2ACXJsogWIGKLMKN3pYdXYzGwVv1xTUWb5mWsn2dpBi7eMyz4a2HZ9slzw19TaPTQ55FrfrjlEbgM0XeHmDfPmzGM3Y2M71RYgXfwZs%2FPPk1x8FMKTH%2BLwGOqUBC8LQUlQyW9TevxnvEYx6mB04c5mdyWirs6ivD38XjwXRzfK7vSos8owJmTXWBvrhOC2Fdrfn86la5mKHDpJihyW1pds5PD83CvwDDyB9iuVnMj2jkUTe5zIi7gSHsq5K%2FUiXZ9wPENeHZkp3ABvQnBZvCC13REn%2FojTst0SSjwco5HpFTiYXV6RPBCxw0SH1%2FPJHLrKZnDB8YeKb2ES02yPuq0tE&X-Amz-Signature=a490592861f8e82c00ef867d58a5fe6ca9b2a7c2b6f7eccb12d6eecf07b76c88&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667T2XG7IB%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDkFrQesMHZfojJMYSNyFZP0sSYrEsXV6uUATy8EEwlkAiEAruO1nVsJuWJc9Fb5CWR5fleKknvKZIy5r70T8AR03MkqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKCeiz%2F4GQ9D0KM51SrcA6oU3e0T%2BOsmQIOevKO%2BBufpnR1FueFmw8pD3gon9mmKsmMFtSsftLHwUrDjctDpRTbUNspumDCvfVTnUbaLgR242rsR1T4VzY8WfVDaROo7K7IjntGyKFTYFhMwzZqYIhgWWZcqk0pbcAx2NK4RUBz8jYQtpiaDROLlY%2Fgdye2u8KXBSwSMhsL1C9%2B4tnK2EtUbMhXchWyrGrMSAsw4JawSLeVebs5x%2BwCwmKJGtcLBKTh%2F955M7vlpxCgVUlRLrvvYPGiHSCgzCZkGVpgprnh2xNimcADAOudt28ETr0jxM1xMxn16BFj3njNM8LTQq6cvrqyqpzKLZAhlO2t1CSyplYXJsQibtIuUW4exJAAbiaUlxr3jBVFixSN4klzPQef3PzAspUJtACVkPu2WVubhFg7oIcfzB70MW0I7t9btq69EGgh9hULj%2BCkXBRygYS71Qkb6qIfzdEGWKz5P8Rv%2FNvmwDbOIg0Jla0V9NVo%2FRnm%2BvPNrUFOutrCTVjatFPVhrNaqj%2BKlM2ACXJsogWIGKLMKN3pYdXYzGwVv1xTUWb5mWsn2dpBi7eMyz4a2HZ9slzw19TaPTQ55FrfrjlEbgM0XeHmDfPmzGM3Y2M71RYgXfwZs%2FPPk1x8FMKTH%2BLwGOqUBC8LQUlQyW9TevxnvEYx6mB04c5mdyWirs6ivD38XjwXRzfK7vSos8owJmTXWBvrhOC2Fdrfn86la5mKHDpJihyW1pds5PD83CvwDDyB9iuVnMj2jkUTe5zIi7gSHsq5K%2FUiXZ9wPENeHZkp3ABvQnBZvCC13REn%2FojTst0SSjwco5HpFTiYXV6RPBCxw0SH1%2FPJHLrKZnDB8YeKb2ES02yPuq0tE&X-Amz-Signature=4c990d9a76ace09dcf3de69919b7636446e19680b2cfdcac5c55d98ae46c0def&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667T2XG7IB%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDkFrQesMHZfojJMYSNyFZP0sSYrEsXV6uUATy8EEwlkAiEAruO1nVsJuWJc9Fb5CWR5fleKknvKZIy5r70T8AR03MkqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKCeiz%2F4GQ9D0KM51SrcA6oU3e0T%2BOsmQIOevKO%2BBufpnR1FueFmw8pD3gon9mmKsmMFtSsftLHwUrDjctDpRTbUNspumDCvfVTnUbaLgR242rsR1T4VzY8WfVDaROo7K7IjntGyKFTYFhMwzZqYIhgWWZcqk0pbcAx2NK4RUBz8jYQtpiaDROLlY%2Fgdye2u8KXBSwSMhsL1C9%2B4tnK2EtUbMhXchWyrGrMSAsw4JawSLeVebs5x%2BwCwmKJGtcLBKTh%2F955M7vlpxCgVUlRLrvvYPGiHSCgzCZkGVpgprnh2xNimcADAOudt28ETr0jxM1xMxn16BFj3njNM8LTQq6cvrqyqpzKLZAhlO2t1CSyplYXJsQibtIuUW4exJAAbiaUlxr3jBVFixSN4klzPQef3PzAspUJtACVkPu2WVubhFg7oIcfzB70MW0I7t9btq69EGgh9hULj%2BCkXBRygYS71Qkb6qIfzdEGWKz5P8Rv%2FNvmwDbOIg0Jla0V9NVo%2FRnm%2BvPNrUFOutrCTVjatFPVhrNaqj%2BKlM2ACXJsogWIGKLMKN3pYdXYzGwVv1xTUWb5mWsn2dpBi7eMyz4a2HZ9slzw19TaPTQ55FrfrjlEbgM0XeHmDfPmzGM3Y2M71RYgXfwZs%2FPPk1x8FMKTH%2BLwGOqUBC8LQUlQyW9TevxnvEYx6mB04c5mdyWirs6ivD38XjwXRzfK7vSos8owJmTXWBvrhOC2Fdrfn86la5mKHDpJihyW1pds5PD83CvwDDyB9iuVnMj2jkUTe5zIi7gSHsq5K%2FUiXZ9wPENeHZkp3ABvQnBZvCC13REn%2FojTst0SSjwco5HpFTiYXV6RPBCxw0SH1%2FPJHLrKZnDB8YeKb2ES02yPuq0tE&X-Amz-Signature=df13e33f035b3b94a2b20ae2f58972ea56167ec3a03ccb32f9858d41bf8a30a3&X-Amz-SignedHeaders=host&x-id=GetObject)
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


