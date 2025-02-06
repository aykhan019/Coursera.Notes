

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664QHY7EZX%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJIMEYCIQDWB2afPlVj28p8BPNNS9s6UyEEEfJGaeyGtP353jPbOQIhAM1OD6Pu4SIKQqUFUU8Uo87TZ5SuZe%2F%2FBWfz%2BPsW4eZwKv8DCGMQABoMNjM3NDIzMTgzODA1IgxcDh4HB3amz7qG4TYq3AP0QiPeIW70YKlKHhEizQYQQwpwshSp7Q3UnxbLJpHGVZnE8P1e9ScUzHTOfGCWv0vvuuUtZrVdX5AwOH%2BVIulfI0hx%2F8brOdB0JeCk501kk1V90NFlSKkhoyI8kaoo%2BwEZ2tAAJIwkEndsmUnc5n5Bv%2F440O9iulZpuNWBO%2FDV0IY2ghnqaFF9fIpXK10S7cfLaqqT7YZYZGlMjDw%2FvSpSHwLghROvR7CbgJLy1PAbjQmu9x6q9w1WhP4KiXUO25EaO6ibwc9Wz4iDn5MFlRzvoRA5Uuoo5uPHDwdDxtxbeAOXUsfrVbuIYmPfDlcfEYTMldhi4UybfFxpJfAOaAOL2N6rdWD9NhPKDfVx9yMSbwzBfC%2BoZ2X0VPSW%2FGxlZBaypbtdXjNNq3NbENgK%2FUz0oeA1km%2BmnLj0%2BO1YK9CHan6%2FPuXulR0wrbK2mOpMouwSg3CEr6Pd5a41iMHDg23t1tX6JxpVksCBgE6vhw7NwsqsYSE6XZIuI2zqSTJZdnquoTFWvS6YEoPuTYq%2BoYet3gCtvAfqFjF8Xgky84u%2FGo6KqYsEjtBuM6gPSyYbd0d1timL9TF4z%2FdUQn08oKnGQ3QEe7F6pVwl93%2Fm%2Ft2fPLXnX4lwwhelsmSn%2FTD5%2B5O9BjqkAUuR5Zv7qwvW3oQyMzFXxgNun2RJgZ5Dfx2OUt78suFccg1PZ3fiZ879sefCAmiT8zORm0PJOZ2uvCznke0XFjrsF1A7Fqn7d3N%2B1JCg9n1K48m6DZHyCbexWhmwP5H0ABeKhJ1levuz9sPdsUqrFfzKjX31buGxxhvR43ch2zmtmcChBJq7yN3iLUNGHV5c3RoeEVWxfCCHMQYsJkqgyuLD27g%2F&X-Amz-Signature=75503ff020e03991f09c7eca9de5e1aec141ffe025b23bfe7c0b8ee191f876db&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RUYNPSD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIEOQ%2Fw5%2FswHYGSSfSbwOoUCHdCObOreI4ZoX781ds1oEAiEAvc91DDLPRojtlkxqLzXqeeQ9CFvOyYFvzJbjhVaVXQIq%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDISoYvlRvQlXQOUQlircA9wlhi4KvVSPsC%2FMroUBgVTrttOzM995yl1hwy42ko0yruD0NHewqiQrbdfAPSDkd%2FrYahCyMvWosK5A8%2FJlUN2IkGs5YTJsvioQy2tpkrdYpg1dLYHQen0TpwsQvBKSCU9TU4KeqL9ApsFbuV%2FUPEd%2F24FmqNorhNjZWz4I8pKJBuqIG%2F0a0KpkdCWJlUcw7O3dAxkEDglhTzdnmpWfrLAvbhEjC1YDkukh5n6yJXKyWpfKKg8ibCPilvsLor1HQR4pcqH%2B2M0f8KOiOOLiD5f03rjmgKsY4JmDgTDy7nLfuUCN04vRzz9F8sJPrcbxtFuS7oP8poeFOMN6tQn9Tup3PNdRhu8LXsQaavJbYDyLYwuj%2FPt7jBmjZ6xSPqtduyoYC7ZajD8QtTbYMI3XpMm6%2F0APTG%2FNEGT86uSmJOBGD0WYvvyCYctdCctBL81Q1TOIgVZ8jxnGPLlbIVwNt%2Fhz%2BpXVwdN1Osv3XK%2B4zpuerGhTiEo7xnEXkgHKaU9gzsmZPtY5nJsN3Dzsqo1NmoH2PGjJyjyRc871Dz0Tj8jaB6eKgKRzFjEg0oKd%2FZ0ncvvDbSKEtBsX1mdX%2BmaSgTSh2DFxrXXLCp64MWkZmgxnDpJ3%2BZYWWmeCU%2FA%2FMK37k70GOqUBLVFLVo%2BkZF3l2wBsLabRvHMqJ1VfpS7vP6dHClSpeH7tf41mWs3pc1TSc7vKzwM6r11GAogtUxJ9RLVB3w%2FVWWcGgr1pI5Ot4y8UoUsiqICV7y%2BODZtZbAZKg93dGph8APWfpHOuFoAOOxgdlcJwrEPjK9u6ZKdSu1S3NozzJCsL%2B%2Fpu1Phb8at3cBU%2FuTZWEyc1E9Ej4mv4G%2F0P9TJTZJpa9YYz&X-Amz-Signature=15841d7f5fbd121ac53fd3aeea3861d8b2116d1ec48d86e556094e4e6533fec0&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RUYNPSD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIEOQ%2Fw5%2FswHYGSSfSbwOoUCHdCObOreI4ZoX781ds1oEAiEAvc91DDLPRojtlkxqLzXqeeQ9CFvOyYFvzJbjhVaVXQIq%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDISoYvlRvQlXQOUQlircA9wlhi4KvVSPsC%2FMroUBgVTrttOzM995yl1hwy42ko0yruD0NHewqiQrbdfAPSDkd%2FrYahCyMvWosK5A8%2FJlUN2IkGs5YTJsvioQy2tpkrdYpg1dLYHQen0TpwsQvBKSCU9TU4KeqL9ApsFbuV%2FUPEd%2F24FmqNorhNjZWz4I8pKJBuqIG%2F0a0KpkdCWJlUcw7O3dAxkEDglhTzdnmpWfrLAvbhEjC1YDkukh5n6yJXKyWpfKKg8ibCPilvsLor1HQR4pcqH%2B2M0f8KOiOOLiD5f03rjmgKsY4JmDgTDy7nLfuUCN04vRzz9F8sJPrcbxtFuS7oP8poeFOMN6tQn9Tup3PNdRhu8LXsQaavJbYDyLYwuj%2FPt7jBmjZ6xSPqtduyoYC7ZajD8QtTbYMI3XpMm6%2F0APTG%2FNEGT86uSmJOBGD0WYvvyCYctdCctBL81Q1TOIgVZ8jxnGPLlbIVwNt%2Fhz%2BpXVwdN1Osv3XK%2B4zpuerGhTiEo7xnEXkgHKaU9gzsmZPtY5nJsN3Dzsqo1NmoH2PGjJyjyRc871Dz0Tj8jaB6eKgKRzFjEg0oKd%2FZ0ncvvDbSKEtBsX1mdX%2BmaSgTSh2DFxrXXLCp64MWkZmgxnDpJ3%2BZYWWmeCU%2FA%2FMK37k70GOqUBLVFLVo%2BkZF3l2wBsLabRvHMqJ1VfpS7vP6dHClSpeH7tf41mWs3pc1TSc7vKzwM6r11GAogtUxJ9RLVB3w%2FVWWcGgr1pI5Ot4y8UoUsiqICV7y%2BODZtZbAZKg93dGph8APWfpHOuFoAOOxgdlcJwrEPjK9u6ZKdSu1S3NozzJCsL%2B%2Fpu1Phb8at3cBU%2FuTZWEyc1E9Ej4mv4G%2F0P9TJTZJpa9YYz&X-Amz-Signature=7880eae3b954eb30abd5449d5e94c7dfed76e6bf48454fdcea6607983200edb9&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RUYNPSD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIEOQ%2Fw5%2FswHYGSSfSbwOoUCHdCObOreI4ZoX781ds1oEAiEAvc91DDLPRojtlkxqLzXqeeQ9CFvOyYFvzJbjhVaVXQIq%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDISoYvlRvQlXQOUQlircA9wlhi4KvVSPsC%2FMroUBgVTrttOzM995yl1hwy42ko0yruD0NHewqiQrbdfAPSDkd%2FrYahCyMvWosK5A8%2FJlUN2IkGs5YTJsvioQy2tpkrdYpg1dLYHQen0TpwsQvBKSCU9TU4KeqL9ApsFbuV%2FUPEd%2F24FmqNorhNjZWz4I8pKJBuqIG%2F0a0KpkdCWJlUcw7O3dAxkEDglhTzdnmpWfrLAvbhEjC1YDkukh5n6yJXKyWpfKKg8ibCPilvsLor1HQR4pcqH%2B2M0f8KOiOOLiD5f03rjmgKsY4JmDgTDy7nLfuUCN04vRzz9F8sJPrcbxtFuS7oP8poeFOMN6tQn9Tup3PNdRhu8LXsQaavJbYDyLYwuj%2FPt7jBmjZ6xSPqtduyoYC7ZajD8QtTbYMI3XpMm6%2F0APTG%2FNEGT86uSmJOBGD0WYvvyCYctdCctBL81Q1TOIgVZ8jxnGPLlbIVwNt%2Fhz%2BpXVwdN1Osv3XK%2B4zpuerGhTiEo7xnEXkgHKaU9gzsmZPtY5nJsN3Dzsqo1NmoH2PGjJyjyRc871Dz0Tj8jaB6eKgKRzFjEg0oKd%2FZ0ncvvDbSKEtBsX1mdX%2BmaSgTSh2DFxrXXLCp64MWkZmgxnDpJ3%2BZYWWmeCU%2FA%2FMK37k70GOqUBLVFLVo%2BkZF3l2wBsLabRvHMqJ1VfpS7vP6dHClSpeH7tf41mWs3pc1TSc7vKzwM6r11GAogtUxJ9RLVB3w%2FVWWcGgr1pI5Ot4y8UoUsiqICV7y%2BODZtZbAZKg93dGph8APWfpHOuFoAOOxgdlcJwrEPjK9u6ZKdSu1S3NozzJCsL%2B%2Fpu1Phb8at3cBU%2FuTZWEyc1E9Ej4mv4G%2F0P9TJTZJpa9YYz&X-Amz-Signature=4ab4d1a57b568336dc873758383e081bd00967c8dbda607f19417c4086ce0db2&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RUYNPSD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIEOQ%2Fw5%2FswHYGSSfSbwOoUCHdCObOreI4ZoX781ds1oEAiEAvc91DDLPRojtlkxqLzXqeeQ9CFvOyYFvzJbjhVaVXQIq%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDISoYvlRvQlXQOUQlircA9wlhi4KvVSPsC%2FMroUBgVTrttOzM995yl1hwy42ko0yruD0NHewqiQrbdfAPSDkd%2FrYahCyMvWosK5A8%2FJlUN2IkGs5YTJsvioQy2tpkrdYpg1dLYHQen0TpwsQvBKSCU9TU4KeqL9ApsFbuV%2FUPEd%2F24FmqNorhNjZWz4I8pKJBuqIG%2F0a0KpkdCWJlUcw7O3dAxkEDglhTzdnmpWfrLAvbhEjC1YDkukh5n6yJXKyWpfKKg8ibCPilvsLor1HQR4pcqH%2B2M0f8KOiOOLiD5f03rjmgKsY4JmDgTDy7nLfuUCN04vRzz9F8sJPrcbxtFuS7oP8poeFOMN6tQn9Tup3PNdRhu8LXsQaavJbYDyLYwuj%2FPt7jBmjZ6xSPqtduyoYC7ZajD8QtTbYMI3XpMm6%2F0APTG%2FNEGT86uSmJOBGD0WYvvyCYctdCctBL81Q1TOIgVZ8jxnGPLlbIVwNt%2Fhz%2BpXVwdN1Osv3XK%2B4zpuerGhTiEo7xnEXkgHKaU9gzsmZPtY5nJsN3Dzsqo1NmoH2PGjJyjyRc871Dz0Tj8jaB6eKgKRzFjEg0oKd%2FZ0ncvvDbSKEtBsX1mdX%2BmaSgTSh2DFxrXXLCp64MWkZmgxnDpJ3%2BZYWWmeCU%2FA%2FMK37k70GOqUBLVFLVo%2BkZF3l2wBsLabRvHMqJ1VfpS7vP6dHClSpeH7tf41mWs3pc1TSc7vKzwM6r11GAogtUxJ9RLVB3w%2FVWWcGgr1pI5Ot4y8UoUsiqICV7y%2BODZtZbAZKg93dGph8APWfpHOuFoAOOxgdlcJwrEPjK9u6ZKdSu1S3NozzJCsL%2B%2Fpu1Phb8at3cBU%2FuTZWEyc1E9Ej4mv4G%2F0P9TJTZJpa9YYz&X-Amz-Signature=2553f467391188fa9a74491d2e08602c248dd00d1bd6aa3306e029d0b32af15f&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RUYNPSD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIEOQ%2Fw5%2FswHYGSSfSbwOoUCHdCObOreI4ZoX781ds1oEAiEAvc91DDLPRojtlkxqLzXqeeQ9CFvOyYFvzJbjhVaVXQIq%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDISoYvlRvQlXQOUQlircA9wlhi4KvVSPsC%2FMroUBgVTrttOzM995yl1hwy42ko0yruD0NHewqiQrbdfAPSDkd%2FrYahCyMvWosK5A8%2FJlUN2IkGs5YTJsvioQy2tpkrdYpg1dLYHQen0TpwsQvBKSCU9TU4KeqL9ApsFbuV%2FUPEd%2F24FmqNorhNjZWz4I8pKJBuqIG%2F0a0KpkdCWJlUcw7O3dAxkEDglhTzdnmpWfrLAvbhEjC1YDkukh5n6yJXKyWpfKKg8ibCPilvsLor1HQR4pcqH%2B2M0f8KOiOOLiD5f03rjmgKsY4JmDgTDy7nLfuUCN04vRzz9F8sJPrcbxtFuS7oP8poeFOMN6tQn9Tup3PNdRhu8LXsQaavJbYDyLYwuj%2FPt7jBmjZ6xSPqtduyoYC7ZajD8QtTbYMI3XpMm6%2F0APTG%2FNEGT86uSmJOBGD0WYvvyCYctdCctBL81Q1TOIgVZ8jxnGPLlbIVwNt%2Fhz%2BpXVwdN1Osv3XK%2B4zpuerGhTiEo7xnEXkgHKaU9gzsmZPtY5nJsN3Dzsqo1NmoH2PGjJyjyRc871Dz0Tj8jaB6eKgKRzFjEg0oKd%2FZ0ncvvDbSKEtBsX1mdX%2BmaSgTSh2DFxrXXLCp64MWkZmgxnDpJ3%2BZYWWmeCU%2FA%2FMK37k70GOqUBLVFLVo%2BkZF3l2wBsLabRvHMqJ1VfpS7vP6dHClSpeH7tf41mWs3pc1TSc7vKzwM6r11GAogtUxJ9RLVB3w%2FVWWcGgr1pI5Ot4y8UoUsiqICV7y%2BODZtZbAZKg93dGph8APWfpHOuFoAOOxgdlcJwrEPjK9u6ZKdSu1S3NozzJCsL%2B%2Fpu1Phb8at3cBU%2FuTZWEyc1E9Ej4mv4G%2F0P9TJTZJpa9YYz&X-Amz-Signature=47c1f376f61c9d0d69b87a0382906a6d6a2d8b99932cc3f715c7835203d7e7d0&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664QHY7EZX%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJIMEYCIQDWB2afPlVj28p8BPNNS9s6UyEEEfJGaeyGtP353jPbOQIhAM1OD6Pu4SIKQqUFUU8Uo87TZ5SuZe%2F%2FBWfz%2BPsW4eZwKv8DCGMQABoMNjM3NDIzMTgzODA1IgxcDh4HB3amz7qG4TYq3AP0QiPeIW70YKlKHhEizQYQQwpwshSp7Q3UnxbLJpHGVZnE8P1e9ScUzHTOfGCWv0vvuuUtZrVdX5AwOH%2BVIulfI0hx%2F8brOdB0JeCk501kk1V90NFlSKkhoyI8kaoo%2BwEZ2tAAJIwkEndsmUnc5n5Bv%2F440O9iulZpuNWBO%2FDV0IY2ghnqaFF9fIpXK10S7cfLaqqT7YZYZGlMjDw%2FvSpSHwLghROvR7CbgJLy1PAbjQmu9x6q9w1WhP4KiXUO25EaO6ibwc9Wz4iDn5MFlRzvoRA5Uuoo5uPHDwdDxtxbeAOXUsfrVbuIYmPfDlcfEYTMldhi4UybfFxpJfAOaAOL2N6rdWD9NhPKDfVx9yMSbwzBfC%2BoZ2X0VPSW%2FGxlZBaypbtdXjNNq3NbENgK%2FUz0oeA1km%2BmnLj0%2BO1YK9CHan6%2FPuXulR0wrbK2mOpMouwSg3CEr6Pd5a41iMHDg23t1tX6JxpVksCBgE6vhw7NwsqsYSE6XZIuI2zqSTJZdnquoTFWvS6YEoPuTYq%2BoYet3gCtvAfqFjF8Xgky84u%2FGo6KqYsEjtBuM6gPSyYbd0d1timL9TF4z%2FdUQn08oKnGQ3QEe7F6pVwl93%2Fm%2Ft2fPLXnX4lwwhelsmSn%2FTD5%2B5O9BjqkAUuR5Zv7qwvW3oQyMzFXxgNun2RJgZ5Dfx2OUt78suFccg1PZ3fiZ879sefCAmiT8zORm0PJOZ2uvCznke0XFjrsF1A7Fqn7d3N%2B1JCg9n1K48m6DZHyCbexWhmwP5H0ABeKhJ1levuz9sPdsUqrFfzKjX31buGxxhvR43ch2zmtmcChBJq7yN3iLUNGHV5c3RoeEVWxfCCHMQYsJkqgyuLD27g%2F&X-Amz-Signature=238546f12f5609ab0f7119a83153021bb039b0dd7ea41acac57a1498019695ea&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664QHY7EZX%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJIMEYCIQDWB2afPlVj28p8BPNNS9s6UyEEEfJGaeyGtP353jPbOQIhAM1OD6Pu4SIKQqUFUU8Uo87TZ5SuZe%2F%2FBWfz%2BPsW4eZwKv8DCGMQABoMNjM3NDIzMTgzODA1IgxcDh4HB3amz7qG4TYq3AP0QiPeIW70YKlKHhEizQYQQwpwshSp7Q3UnxbLJpHGVZnE8P1e9ScUzHTOfGCWv0vvuuUtZrVdX5AwOH%2BVIulfI0hx%2F8brOdB0JeCk501kk1V90NFlSKkhoyI8kaoo%2BwEZ2tAAJIwkEndsmUnc5n5Bv%2F440O9iulZpuNWBO%2FDV0IY2ghnqaFF9fIpXK10S7cfLaqqT7YZYZGlMjDw%2FvSpSHwLghROvR7CbgJLy1PAbjQmu9x6q9w1WhP4KiXUO25EaO6ibwc9Wz4iDn5MFlRzvoRA5Uuoo5uPHDwdDxtxbeAOXUsfrVbuIYmPfDlcfEYTMldhi4UybfFxpJfAOaAOL2N6rdWD9NhPKDfVx9yMSbwzBfC%2BoZ2X0VPSW%2FGxlZBaypbtdXjNNq3NbENgK%2FUz0oeA1km%2BmnLj0%2BO1YK9CHan6%2FPuXulR0wrbK2mOpMouwSg3CEr6Pd5a41iMHDg23t1tX6JxpVksCBgE6vhw7NwsqsYSE6XZIuI2zqSTJZdnquoTFWvS6YEoPuTYq%2BoYet3gCtvAfqFjF8Xgky84u%2FGo6KqYsEjtBuM6gPSyYbd0d1timL9TF4z%2FdUQn08oKnGQ3QEe7F6pVwl93%2Fm%2Ft2fPLXnX4lwwhelsmSn%2FTD5%2B5O9BjqkAUuR5Zv7qwvW3oQyMzFXxgNun2RJgZ5Dfx2OUt78suFccg1PZ3fiZ879sefCAmiT8zORm0PJOZ2uvCznke0XFjrsF1A7Fqn7d3N%2B1JCg9n1K48m6DZHyCbexWhmwP5H0ABeKhJ1levuz9sPdsUqrFfzKjX31buGxxhvR43ch2zmtmcChBJq7yN3iLUNGHV5c3RoeEVWxfCCHMQYsJkqgyuLD27g%2F&X-Amz-Signature=8611e1833f87168c671e30ebaa70b30222e673cc4d6ce39a13c57f5da5805ff7&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664QHY7EZX%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJIMEYCIQDWB2afPlVj28p8BPNNS9s6UyEEEfJGaeyGtP353jPbOQIhAM1OD6Pu4SIKQqUFUU8Uo87TZ5SuZe%2F%2FBWfz%2BPsW4eZwKv8DCGMQABoMNjM3NDIzMTgzODA1IgxcDh4HB3amz7qG4TYq3AP0QiPeIW70YKlKHhEizQYQQwpwshSp7Q3UnxbLJpHGVZnE8P1e9ScUzHTOfGCWv0vvuuUtZrVdX5AwOH%2BVIulfI0hx%2F8brOdB0JeCk501kk1V90NFlSKkhoyI8kaoo%2BwEZ2tAAJIwkEndsmUnc5n5Bv%2F440O9iulZpuNWBO%2FDV0IY2ghnqaFF9fIpXK10S7cfLaqqT7YZYZGlMjDw%2FvSpSHwLghROvR7CbgJLy1PAbjQmu9x6q9w1WhP4KiXUO25EaO6ibwc9Wz4iDn5MFlRzvoRA5Uuoo5uPHDwdDxtxbeAOXUsfrVbuIYmPfDlcfEYTMldhi4UybfFxpJfAOaAOL2N6rdWD9NhPKDfVx9yMSbwzBfC%2BoZ2X0VPSW%2FGxlZBaypbtdXjNNq3NbENgK%2FUz0oeA1km%2BmnLj0%2BO1YK9CHan6%2FPuXulR0wrbK2mOpMouwSg3CEr6Pd5a41iMHDg23t1tX6JxpVksCBgE6vhw7NwsqsYSE6XZIuI2zqSTJZdnquoTFWvS6YEoPuTYq%2BoYet3gCtvAfqFjF8Xgky84u%2FGo6KqYsEjtBuM6gPSyYbd0d1timL9TF4z%2FdUQn08oKnGQ3QEe7F6pVwl93%2Fm%2Ft2fPLXnX4lwwhelsmSn%2FTD5%2B5O9BjqkAUuR5Zv7qwvW3oQyMzFXxgNun2RJgZ5Dfx2OUt78suFccg1PZ3fiZ879sefCAmiT8zORm0PJOZ2uvCznke0XFjrsF1A7Fqn7d3N%2B1JCg9n1K48m6DZHyCbexWhmwP5H0ABeKhJ1levuz9sPdsUqrFfzKjX31buGxxhvR43ch2zmtmcChBJq7yN3iLUNGHV5c3RoeEVWxfCCHMQYsJkqgyuLD27g%2F&X-Amz-Signature=8730078e08e5a624e3a277b795e588e6f0a6f67c998d0dbab632dda8611a3cd1&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664QHY7EZX%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJIMEYCIQDWB2afPlVj28p8BPNNS9s6UyEEEfJGaeyGtP353jPbOQIhAM1OD6Pu4SIKQqUFUU8Uo87TZ5SuZe%2F%2FBWfz%2BPsW4eZwKv8DCGMQABoMNjM3NDIzMTgzODA1IgxcDh4HB3amz7qG4TYq3AP0QiPeIW70YKlKHhEizQYQQwpwshSp7Q3UnxbLJpHGVZnE8P1e9ScUzHTOfGCWv0vvuuUtZrVdX5AwOH%2BVIulfI0hx%2F8brOdB0JeCk501kk1V90NFlSKkhoyI8kaoo%2BwEZ2tAAJIwkEndsmUnc5n5Bv%2F440O9iulZpuNWBO%2FDV0IY2ghnqaFF9fIpXK10S7cfLaqqT7YZYZGlMjDw%2FvSpSHwLghROvR7CbgJLy1PAbjQmu9x6q9w1WhP4KiXUO25EaO6ibwc9Wz4iDn5MFlRzvoRA5Uuoo5uPHDwdDxtxbeAOXUsfrVbuIYmPfDlcfEYTMldhi4UybfFxpJfAOaAOL2N6rdWD9NhPKDfVx9yMSbwzBfC%2BoZ2X0VPSW%2FGxlZBaypbtdXjNNq3NbENgK%2FUz0oeA1km%2BmnLj0%2BO1YK9CHan6%2FPuXulR0wrbK2mOpMouwSg3CEr6Pd5a41iMHDg23t1tX6JxpVksCBgE6vhw7NwsqsYSE6XZIuI2zqSTJZdnquoTFWvS6YEoPuTYq%2BoYet3gCtvAfqFjF8Xgky84u%2FGo6KqYsEjtBuM6gPSyYbd0d1timL9TF4z%2FdUQn08oKnGQ3QEe7F6pVwl93%2Fm%2Ft2fPLXnX4lwwhelsmSn%2FTD5%2B5O9BjqkAUuR5Zv7qwvW3oQyMzFXxgNun2RJgZ5Dfx2OUt78suFccg1PZ3fiZ879sefCAmiT8zORm0PJOZ2uvCznke0XFjrsF1A7Fqn7d3N%2B1JCg9n1K48m6DZHyCbexWhmwP5H0ABeKhJ1levuz9sPdsUqrFfzKjX31buGxxhvR43ch2zmtmcChBJq7yN3iLUNGHV5c3RoeEVWxfCCHMQYsJkqgyuLD27g%2F&X-Amz-Signature=d11cb10da05e9a108594d6a60a68878c2361678dd5425a79d9a2ae218bd88201&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664QHY7EZX%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJIMEYCIQDWB2afPlVj28p8BPNNS9s6UyEEEfJGaeyGtP353jPbOQIhAM1OD6Pu4SIKQqUFUU8Uo87TZ5SuZe%2F%2FBWfz%2BPsW4eZwKv8DCGMQABoMNjM3NDIzMTgzODA1IgxcDh4HB3amz7qG4TYq3AP0QiPeIW70YKlKHhEizQYQQwpwshSp7Q3UnxbLJpHGVZnE8P1e9ScUzHTOfGCWv0vvuuUtZrVdX5AwOH%2BVIulfI0hx%2F8brOdB0JeCk501kk1V90NFlSKkhoyI8kaoo%2BwEZ2tAAJIwkEndsmUnc5n5Bv%2F440O9iulZpuNWBO%2FDV0IY2ghnqaFF9fIpXK10S7cfLaqqT7YZYZGlMjDw%2FvSpSHwLghROvR7CbgJLy1PAbjQmu9x6q9w1WhP4KiXUO25EaO6ibwc9Wz4iDn5MFlRzvoRA5Uuoo5uPHDwdDxtxbeAOXUsfrVbuIYmPfDlcfEYTMldhi4UybfFxpJfAOaAOL2N6rdWD9NhPKDfVx9yMSbwzBfC%2BoZ2X0VPSW%2FGxlZBaypbtdXjNNq3NbENgK%2FUz0oeA1km%2BmnLj0%2BO1YK9CHan6%2FPuXulR0wrbK2mOpMouwSg3CEr6Pd5a41iMHDg23t1tX6JxpVksCBgE6vhw7NwsqsYSE6XZIuI2zqSTJZdnquoTFWvS6YEoPuTYq%2BoYet3gCtvAfqFjF8Xgky84u%2FGo6KqYsEjtBuM6gPSyYbd0d1timL9TF4z%2FdUQn08oKnGQ3QEe7F6pVwl93%2Fm%2Ft2fPLXnX4lwwhelsmSn%2FTD5%2B5O9BjqkAUuR5Zv7qwvW3oQyMzFXxgNun2RJgZ5Dfx2OUt78suFccg1PZ3fiZ879sefCAmiT8zORm0PJOZ2uvCznke0XFjrsF1A7Fqn7d3N%2B1JCg9n1K48m6DZHyCbexWhmwP5H0ABeKhJ1levuz9sPdsUqrFfzKjX31buGxxhvR43ch2zmtmcChBJq7yN3iLUNGHV5c3RoeEVWxfCCHMQYsJkqgyuLD27g%2F&X-Amz-Signature=37b105deb3494e613c6eba0d34b2745cedfd3357dc7f731429d3b420030cfdc9&X-Amz-SignedHeaders=host&x-id=GetObject)
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


