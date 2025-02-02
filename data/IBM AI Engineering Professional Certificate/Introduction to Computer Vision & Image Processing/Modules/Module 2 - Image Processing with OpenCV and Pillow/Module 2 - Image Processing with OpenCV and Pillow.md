

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666FG6GVA4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFEDTQM12EBPLY%2B2R0a4eNqBh0InwUqgZOFjh9r%2F1N8LAiEAhDvADicuZexACYB7panf9w8qLy%2BMeiUPxSJC4cCcM1MqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG7g5FFbFd17pFZLnCrcA3zW3%2BktXinbOfQSXU1j%2FFuDZWmaLHeyJIuSLVpCmpN5ofIdBnXK2m4Y7sBr8PeRfYuoLPgQDh3%2FEzEkftVpJRy%2F2IjyI4lkT8ZTRV3OH4%2FI9JutYAYBG7mRtAEJ4j3%2FLqRoCiM5fS3hu9cCtTlb%2BM3QD0bYleIPOvCG3dzXX4zgsuLHm%2F9yVFiKk0%2BbMZyBRC8MJ0MKA9b03cUq757Xb4MBXfulDE0NgJKTHhaODyDsoIUept4QiJkgcAyZHBjJ99n4YWgfIdUgK2gYngndCbEh1Be9rBbu2%2Bmd9cjfP7wHnF2UanrgyWqmq3Q7p6iAWYAJEH%2FKrDL7xluLB6iuRY6WoWKMrOeRZtxvSALX%2FEORF35QgYnmpLm6g7cSRhq7sMgMsJVEAq8h%2Fks2q6ddIO4T13IhvkSfa6EJSM56iSiDppAb0ekqkl8daFVMC3lwrukk3o9OVCOd%2FR9e%2FE7JsseGUN%2Funip79DhPF9Uu3OefELodvRmknLMdIToTXXVPTidnZEFLtHhx0iPxJ5EJ7RMd2mmE62m%2BTM6mCPajJFCT9jJ2HDWUYVfU9cTsCKnh8tCPnW7w0A6Gtct2qE7jhD85DRSovCuiTUvKQx%2Fp3ZU53RYLRuEx%2FnXqY92AMP%2B%2F%2FbwGOqUBSfb9gXpm%2FdymYZPQEsg2%2F%2Bw5jTWLvzVjc2WnAbx6wleejWH0YM%2BrQMmbZQ8vF32RQjQ0V9XPZ2Aho7vTkCDL5ChX9NsyR0Ri3OThMbQcnwWzlk6YAOqp%2B2ih%2BoqHzz%2FzYB7Iku9kX98axy3FYncYAtx0c0QEWD1YCUQby0XcUx%2BMruoVogWox1KrUQfFP4bH0Dt4zGTksDl8L6A3W4SG2m3dxxH6&X-Amz-Signature=65fa9e2a80ee63545047b814b5ac7720cbf5308e8fb5181fdea8235b8d69ef49&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666DOFMH3Z%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141213Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFZJjWRMKDcxdl04DzJGUvlK4Z11VsGiA1GZbMnumiI6AiEAnqOOl2CUoiyAHUNUKCLf%2B2FQXOzo4za5dlU8uk1sN0YqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPvZKC9Z0mAhKjEDxSrcAyGIVzhnzn1TbVy0CpiuYagFA2UoVIZ0Bydfs8s1e2HDeY6sSAHKDbOWBQMAZaPLLo0Xc9GbZlJHT%2FF4HwpmqRUWqe9LH0hPZpCflimG8dzjHktz81%2FggP9KZoL%2BFArKQ8m6e0gzPP5OhoC13B4f93y%2F35vM3WaTQalb7Pmim8HpIVhlrojtAhlEeVYXPUuoj7ERrNySpPvCB1g3no4nCfvqTNlH0Kn3ArDWCiz1GoLwkSA96yTsYKO0f7XFb4irkUqxaBYzg9hSUHrrAQHX62%2BTmSt4rw%2FXKPeBedVGXpHabLBgevr4JhaZ2bvDpORdocHmrLaH4t7QIdmX2LOTIV%2F28nw7DGHOwKJGMuOUbDPj8eK3fh4kAVMO4I8J2oArZtkpl6HYZvcDLb0k8q5weU8Xs4y1lXdSsduVk49HlwsOb1WWQO0qz3xkYb8fEBZAUp4SziGjuSqIJXwIMQziJ%2BK7wYkHXO2CtO2BLCoY6lCxT3nEtFl%2FwA5WqXuESQ8%2BUt4%2FQkD%2BtbsIwnvSRCIq4Cny6cDfxRQj0Jl23pTZ38%2FkKfeW%2BqMrFUI6XsDv2TT6mZ7D527Y6IHUrjN7fZh408euCf1QDzb3eypJJsGP%2F2NWN3II0XSP2W5CylOxMNu8%2FbwGOqUBJZnjRIubD0T6egcXVmAOIbyRpV44c%2F7bfu9DxV1DqvQpEzfBnZR6ky6uf%2BSK2zQsLTXeM%2BrillDRqJU%2BFpL0W9DCcRPWXFRZPRBI0ndbernJAtx7RzFdnjThU14yOj1a%2BILl9txLzebkYPtQKufTzod48qZx%2BjlQNVSvne7lgUtaiW7QVj3ekr726IeJGoZKlyuDdvWb56G1FvPSuGMV%2Fgudbx7K&X-Amz-Signature=9ed3ef306b6a7f4c599d25c6239874152f12bcd53adbea9ffad42d7463dd78d6&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666DOFMH3Z%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141213Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFZJjWRMKDcxdl04DzJGUvlK4Z11VsGiA1GZbMnumiI6AiEAnqOOl2CUoiyAHUNUKCLf%2B2FQXOzo4za5dlU8uk1sN0YqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPvZKC9Z0mAhKjEDxSrcAyGIVzhnzn1TbVy0CpiuYagFA2UoVIZ0Bydfs8s1e2HDeY6sSAHKDbOWBQMAZaPLLo0Xc9GbZlJHT%2FF4HwpmqRUWqe9LH0hPZpCflimG8dzjHktz81%2FggP9KZoL%2BFArKQ8m6e0gzPP5OhoC13B4f93y%2F35vM3WaTQalb7Pmim8HpIVhlrojtAhlEeVYXPUuoj7ERrNySpPvCB1g3no4nCfvqTNlH0Kn3ArDWCiz1GoLwkSA96yTsYKO0f7XFb4irkUqxaBYzg9hSUHrrAQHX62%2BTmSt4rw%2FXKPeBedVGXpHabLBgevr4JhaZ2bvDpORdocHmrLaH4t7QIdmX2LOTIV%2F28nw7DGHOwKJGMuOUbDPj8eK3fh4kAVMO4I8J2oArZtkpl6HYZvcDLb0k8q5weU8Xs4y1lXdSsduVk49HlwsOb1WWQO0qz3xkYb8fEBZAUp4SziGjuSqIJXwIMQziJ%2BK7wYkHXO2CtO2BLCoY6lCxT3nEtFl%2FwA5WqXuESQ8%2BUt4%2FQkD%2BtbsIwnvSRCIq4Cny6cDfxRQj0Jl23pTZ38%2FkKfeW%2BqMrFUI6XsDv2TT6mZ7D527Y6IHUrjN7fZh408euCf1QDzb3eypJJsGP%2F2NWN3II0XSP2W5CylOxMNu8%2FbwGOqUBJZnjRIubD0T6egcXVmAOIbyRpV44c%2F7bfu9DxV1DqvQpEzfBnZR6ky6uf%2BSK2zQsLTXeM%2BrillDRqJU%2BFpL0W9DCcRPWXFRZPRBI0ndbernJAtx7RzFdnjThU14yOj1a%2BILl9txLzebkYPtQKufTzod48qZx%2BjlQNVSvne7lgUtaiW7QVj3ekr726IeJGoZKlyuDdvWb56G1FvPSuGMV%2Fgudbx7K&X-Amz-Signature=c3f8e9ae496a4de86fa41f032d952f0eacc822bd2b3aa8b91a2660f10b58ea55&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666DOFMH3Z%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141213Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFZJjWRMKDcxdl04DzJGUvlK4Z11VsGiA1GZbMnumiI6AiEAnqOOl2CUoiyAHUNUKCLf%2B2FQXOzo4za5dlU8uk1sN0YqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPvZKC9Z0mAhKjEDxSrcAyGIVzhnzn1TbVy0CpiuYagFA2UoVIZ0Bydfs8s1e2HDeY6sSAHKDbOWBQMAZaPLLo0Xc9GbZlJHT%2FF4HwpmqRUWqe9LH0hPZpCflimG8dzjHktz81%2FggP9KZoL%2BFArKQ8m6e0gzPP5OhoC13B4f93y%2F35vM3WaTQalb7Pmim8HpIVhlrojtAhlEeVYXPUuoj7ERrNySpPvCB1g3no4nCfvqTNlH0Kn3ArDWCiz1GoLwkSA96yTsYKO0f7XFb4irkUqxaBYzg9hSUHrrAQHX62%2BTmSt4rw%2FXKPeBedVGXpHabLBgevr4JhaZ2bvDpORdocHmrLaH4t7QIdmX2LOTIV%2F28nw7DGHOwKJGMuOUbDPj8eK3fh4kAVMO4I8J2oArZtkpl6HYZvcDLb0k8q5weU8Xs4y1lXdSsduVk49HlwsOb1WWQO0qz3xkYb8fEBZAUp4SziGjuSqIJXwIMQziJ%2BK7wYkHXO2CtO2BLCoY6lCxT3nEtFl%2FwA5WqXuESQ8%2BUt4%2FQkD%2BtbsIwnvSRCIq4Cny6cDfxRQj0Jl23pTZ38%2FkKfeW%2BqMrFUI6XsDv2TT6mZ7D527Y6IHUrjN7fZh408euCf1QDzb3eypJJsGP%2F2NWN3II0XSP2W5CylOxMNu8%2FbwGOqUBJZnjRIubD0T6egcXVmAOIbyRpV44c%2F7bfu9DxV1DqvQpEzfBnZR6ky6uf%2BSK2zQsLTXeM%2BrillDRqJU%2BFpL0W9DCcRPWXFRZPRBI0ndbernJAtx7RzFdnjThU14yOj1a%2BILl9txLzebkYPtQKufTzod48qZx%2BjlQNVSvne7lgUtaiW7QVj3ekr726IeJGoZKlyuDdvWb56G1FvPSuGMV%2Fgudbx7K&X-Amz-Signature=e83d9de345c025b79a016fcb22c4f01de791dff97e117a18196bc94e9395c704&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666DOFMH3Z%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141213Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFZJjWRMKDcxdl04DzJGUvlK4Z11VsGiA1GZbMnumiI6AiEAnqOOl2CUoiyAHUNUKCLf%2B2FQXOzo4za5dlU8uk1sN0YqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPvZKC9Z0mAhKjEDxSrcAyGIVzhnzn1TbVy0CpiuYagFA2UoVIZ0Bydfs8s1e2HDeY6sSAHKDbOWBQMAZaPLLo0Xc9GbZlJHT%2FF4HwpmqRUWqe9LH0hPZpCflimG8dzjHktz81%2FggP9KZoL%2BFArKQ8m6e0gzPP5OhoC13B4f93y%2F35vM3WaTQalb7Pmim8HpIVhlrojtAhlEeVYXPUuoj7ERrNySpPvCB1g3no4nCfvqTNlH0Kn3ArDWCiz1GoLwkSA96yTsYKO0f7XFb4irkUqxaBYzg9hSUHrrAQHX62%2BTmSt4rw%2FXKPeBedVGXpHabLBgevr4JhaZ2bvDpORdocHmrLaH4t7QIdmX2LOTIV%2F28nw7DGHOwKJGMuOUbDPj8eK3fh4kAVMO4I8J2oArZtkpl6HYZvcDLb0k8q5weU8Xs4y1lXdSsduVk49HlwsOb1WWQO0qz3xkYb8fEBZAUp4SziGjuSqIJXwIMQziJ%2BK7wYkHXO2CtO2BLCoY6lCxT3nEtFl%2FwA5WqXuESQ8%2BUt4%2FQkD%2BtbsIwnvSRCIq4Cny6cDfxRQj0Jl23pTZ38%2FkKfeW%2BqMrFUI6XsDv2TT6mZ7D527Y6IHUrjN7fZh408euCf1QDzb3eypJJsGP%2F2NWN3II0XSP2W5CylOxMNu8%2FbwGOqUBJZnjRIubD0T6egcXVmAOIbyRpV44c%2F7bfu9DxV1DqvQpEzfBnZR6ky6uf%2BSK2zQsLTXeM%2BrillDRqJU%2BFpL0W9DCcRPWXFRZPRBI0ndbernJAtx7RzFdnjThU14yOj1a%2BILl9txLzebkYPtQKufTzod48qZx%2BjlQNVSvne7lgUtaiW7QVj3ekr726IeJGoZKlyuDdvWb56G1FvPSuGMV%2Fgudbx7K&X-Amz-Signature=6e67cb58935e5c59ab83dcc5122830a729e64d0134f76aaeec3fe6f66fa95919&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666DOFMH3Z%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141213Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFZJjWRMKDcxdl04DzJGUvlK4Z11VsGiA1GZbMnumiI6AiEAnqOOl2CUoiyAHUNUKCLf%2B2FQXOzo4za5dlU8uk1sN0YqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPvZKC9Z0mAhKjEDxSrcAyGIVzhnzn1TbVy0CpiuYagFA2UoVIZ0Bydfs8s1e2HDeY6sSAHKDbOWBQMAZaPLLo0Xc9GbZlJHT%2FF4HwpmqRUWqe9LH0hPZpCflimG8dzjHktz81%2FggP9KZoL%2BFArKQ8m6e0gzPP5OhoC13B4f93y%2F35vM3WaTQalb7Pmim8HpIVhlrojtAhlEeVYXPUuoj7ERrNySpPvCB1g3no4nCfvqTNlH0Kn3ArDWCiz1GoLwkSA96yTsYKO0f7XFb4irkUqxaBYzg9hSUHrrAQHX62%2BTmSt4rw%2FXKPeBedVGXpHabLBgevr4JhaZ2bvDpORdocHmrLaH4t7QIdmX2LOTIV%2F28nw7DGHOwKJGMuOUbDPj8eK3fh4kAVMO4I8J2oArZtkpl6HYZvcDLb0k8q5weU8Xs4y1lXdSsduVk49HlwsOb1WWQO0qz3xkYb8fEBZAUp4SziGjuSqIJXwIMQziJ%2BK7wYkHXO2CtO2BLCoY6lCxT3nEtFl%2FwA5WqXuESQ8%2BUt4%2FQkD%2BtbsIwnvSRCIq4Cny6cDfxRQj0Jl23pTZ38%2FkKfeW%2BqMrFUI6XsDv2TT6mZ7D527Y6IHUrjN7fZh408euCf1QDzb3eypJJsGP%2F2NWN3II0XSP2W5CylOxMNu8%2FbwGOqUBJZnjRIubD0T6egcXVmAOIbyRpV44c%2F7bfu9DxV1DqvQpEzfBnZR6ky6uf%2BSK2zQsLTXeM%2BrillDRqJU%2BFpL0W9DCcRPWXFRZPRBI0ndbernJAtx7RzFdnjThU14yOj1a%2BILl9txLzebkYPtQKufTzod48qZx%2BjlQNVSvne7lgUtaiW7QVj3ekr726IeJGoZKlyuDdvWb56G1FvPSuGMV%2Fgudbx7K&X-Amz-Signature=96fcf83c34f4f31a52ba7033f58b4eae081ebce44f3930185117238c405f7659&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666FG6GVA4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFEDTQM12EBPLY%2B2R0a4eNqBh0InwUqgZOFjh9r%2F1N8LAiEAhDvADicuZexACYB7panf9w8qLy%2BMeiUPxSJC4cCcM1MqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG7g5FFbFd17pFZLnCrcA3zW3%2BktXinbOfQSXU1j%2FFuDZWmaLHeyJIuSLVpCmpN5ofIdBnXK2m4Y7sBr8PeRfYuoLPgQDh3%2FEzEkftVpJRy%2F2IjyI4lkT8ZTRV3OH4%2FI9JutYAYBG7mRtAEJ4j3%2FLqRoCiM5fS3hu9cCtTlb%2BM3QD0bYleIPOvCG3dzXX4zgsuLHm%2F9yVFiKk0%2BbMZyBRC8MJ0MKA9b03cUq757Xb4MBXfulDE0NgJKTHhaODyDsoIUept4QiJkgcAyZHBjJ99n4YWgfIdUgK2gYngndCbEh1Be9rBbu2%2Bmd9cjfP7wHnF2UanrgyWqmq3Q7p6iAWYAJEH%2FKrDL7xluLB6iuRY6WoWKMrOeRZtxvSALX%2FEORF35QgYnmpLm6g7cSRhq7sMgMsJVEAq8h%2Fks2q6ddIO4T13IhvkSfa6EJSM56iSiDppAb0ekqkl8daFVMC3lwrukk3o9OVCOd%2FR9e%2FE7JsseGUN%2Funip79DhPF9Uu3OefELodvRmknLMdIToTXXVPTidnZEFLtHhx0iPxJ5EJ7RMd2mmE62m%2BTM6mCPajJFCT9jJ2HDWUYVfU9cTsCKnh8tCPnW7w0A6Gtct2qE7jhD85DRSovCuiTUvKQx%2Fp3ZU53RYLRuEx%2FnXqY92AMP%2B%2F%2FbwGOqUBSfb9gXpm%2FdymYZPQEsg2%2F%2Bw5jTWLvzVjc2WnAbx6wleejWH0YM%2BrQMmbZQ8vF32RQjQ0V9XPZ2Aho7vTkCDL5ChX9NsyR0Ri3OThMbQcnwWzlk6YAOqp%2B2ih%2BoqHzz%2FzYB7Iku9kX98axy3FYncYAtx0c0QEWD1YCUQby0XcUx%2BMruoVogWox1KrUQfFP4bH0Dt4zGTksDl8L6A3W4SG2m3dxxH6&X-Amz-Signature=a5a59afed84deee7065b78f0d2dbfad6dfe76265fe6285f325d48728764d6e63&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666FG6GVA4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFEDTQM12EBPLY%2B2R0a4eNqBh0InwUqgZOFjh9r%2F1N8LAiEAhDvADicuZexACYB7panf9w8qLy%2BMeiUPxSJC4cCcM1MqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG7g5FFbFd17pFZLnCrcA3zW3%2BktXinbOfQSXU1j%2FFuDZWmaLHeyJIuSLVpCmpN5ofIdBnXK2m4Y7sBr8PeRfYuoLPgQDh3%2FEzEkftVpJRy%2F2IjyI4lkT8ZTRV3OH4%2FI9JutYAYBG7mRtAEJ4j3%2FLqRoCiM5fS3hu9cCtTlb%2BM3QD0bYleIPOvCG3dzXX4zgsuLHm%2F9yVFiKk0%2BbMZyBRC8MJ0MKA9b03cUq757Xb4MBXfulDE0NgJKTHhaODyDsoIUept4QiJkgcAyZHBjJ99n4YWgfIdUgK2gYngndCbEh1Be9rBbu2%2Bmd9cjfP7wHnF2UanrgyWqmq3Q7p6iAWYAJEH%2FKrDL7xluLB6iuRY6WoWKMrOeRZtxvSALX%2FEORF35QgYnmpLm6g7cSRhq7sMgMsJVEAq8h%2Fks2q6ddIO4T13IhvkSfa6EJSM56iSiDppAb0ekqkl8daFVMC3lwrukk3o9OVCOd%2FR9e%2FE7JsseGUN%2Funip79DhPF9Uu3OefELodvRmknLMdIToTXXVPTidnZEFLtHhx0iPxJ5EJ7RMd2mmE62m%2BTM6mCPajJFCT9jJ2HDWUYVfU9cTsCKnh8tCPnW7w0A6Gtct2qE7jhD85DRSovCuiTUvKQx%2Fp3ZU53RYLRuEx%2FnXqY92AMP%2B%2F%2FbwGOqUBSfb9gXpm%2FdymYZPQEsg2%2F%2Bw5jTWLvzVjc2WnAbx6wleejWH0YM%2BrQMmbZQ8vF32RQjQ0V9XPZ2Aho7vTkCDL5ChX9NsyR0Ri3OThMbQcnwWzlk6YAOqp%2B2ih%2BoqHzz%2FzYB7Iku9kX98axy3FYncYAtx0c0QEWD1YCUQby0XcUx%2BMruoVogWox1KrUQfFP4bH0Dt4zGTksDl8L6A3W4SG2m3dxxH6&X-Amz-Signature=537945a43ecbe06fb3158ff5cce3888f97fbc501db6d9b9acf6943436f05763b&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666FG6GVA4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFEDTQM12EBPLY%2B2R0a4eNqBh0InwUqgZOFjh9r%2F1N8LAiEAhDvADicuZexACYB7panf9w8qLy%2BMeiUPxSJC4cCcM1MqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG7g5FFbFd17pFZLnCrcA3zW3%2BktXinbOfQSXU1j%2FFuDZWmaLHeyJIuSLVpCmpN5ofIdBnXK2m4Y7sBr8PeRfYuoLPgQDh3%2FEzEkftVpJRy%2F2IjyI4lkT8ZTRV3OH4%2FI9JutYAYBG7mRtAEJ4j3%2FLqRoCiM5fS3hu9cCtTlb%2BM3QD0bYleIPOvCG3dzXX4zgsuLHm%2F9yVFiKk0%2BbMZyBRC8MJ0MKA9b03cUq757Xb4MBXfulDE0NgJKTHhaODyDsoIUept4QiJkgcAyZHBjJ99n4YWgfIdUgK2gYngndCbEh1Be9rBbu2%2Bmd9cjfP7wHnF2UanrgyWqmq3Q7p6iAWYAJEH%2FKrDL7xluLB6iuRY6WoWKMrOeRZtxvSALX%2FEORF35QgYnmpLm6g7cSRhq7sMgMsJVEAq8h%2Fks2q6ddIO4T13IhvkSfa6EJSM56iSiDppAb0ekqkl8daFVMC3lwrukk3o9OVCOd%2FR9e%2FE7JsseGUN%2Funip79DhPF9Uu3OefELodvRmknLMdIToTXXVPTidnZEFLtHhx0iPxJ5EJ7RMd2mmE62m%2BTM6mCPajJFCT9jJ2HDWUYVfU9cTsCKnh8tCPnW7w0A6Gtct2qE7jhD85DRSovCuiTUvKQx%2Fp3ZU53RYLRuEx%2FnXqY92AMP%2B%2F%2FbwGOqUBSfb9gXpm%2FdymYZPQEsg2%2F%2Bw5jTWLvzVjc2WnAbx6wleejWH0YM%2BrQMmbZQ8vF32RQjQ0V9XPZ2Aho7vTkCDL5ChX9NsyR0Ri3OThMbQcnwWzlk6YAOqp%2B2ih%2BoqHzz%2FzYB7Iku9kX98axy3FYncYAtx0c0QEWD1YCUQby0XcUx%2BMruoVogWox1KrUQfFP4bH0Dt4zGTksDl8L6A3W4SG2m3dxxH6&X-Amz-Signature=a7c1699338ad9956433060344bad4cc1e92b7ca58f270171594a506aea7d7306&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666FG6GVA4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFEDTQM12EBPLY%2B2R0a4eNqBh0InwUqgZOFjh9r%2F1N8LAiEAhDvADicuZexACYB7panf9w8qLy%2BMeiUPxSJC4cCcM1MqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG7g5FFbFd17pFZLnCrcA3zW3%2BktXinbOfQSXU1j%2FFuDZWmaLHeyJIuSLVpCmpN5ofIdBnXK2m4Y7sBr8PeRfYuoLPgQDh3%2FEzEkftVpJRy%2F2IjyI4lkT8ZTRV3OH4%2FI9JutYAYBG7mRtAEJ4j3%2FLqRoCiM5fS3hu9cCtTlb%2BM3QD0bYleIPOvCG3dzXX4zgsuLHm%2F9yVFiKk0%2BbMZyBRC8MJ0MKA9b03cUq757Xb4MBXfulDE0NgJKTHhaODyDsoIUept4QiJkgcAyZHBjJ99n4YWgfIdUgK2gYngndCbEh1Be9rBbu2%2Bmd9cjfP7wHnF2UanrgyWqmq3Q7p6iAWYAJEH%2FKrDL7xluLB6iuRY6WoWKMrOeRZtxvSALX%2FEORF35QgYnmpLm6g7cSRhq7sMgMsJVEAq8h%2Fks2q6ddIO4T13IhvkSfa6EJSM56iSiDppAb0ekqkl8daFVMC3lwrukk3o9OVCOd%2FR9e%2FE7JsseGUN%2Funip79DhPF9Uu3OefELodvRmknLMdIToTXXVPTidnZEFLtHhx0iPxJ5EJ7RMd2mmE62m%2BTM6mCPajJFCT9jJ2HDWUYVfU9cTsCKnh8tCPnW7w0A6Gtct2qE7jhD85DRSovCuiTUvKQx%2Fp3ZU53RYLRuEx%2FnXqY92AMP%2B%2F%2FbwGOqUBSfb9gXpm%2FdymYZPQEsg2%2F%2Bw5jTWLvzVjc2WnAbx6wleejWH0YM%2BrQMmbZQ8vF32RQjQ0V9XPZ2Aho7vTkCDL5ChX9NsyR0Ri3OThMbQcnwWzlk6YAOqp%2B2ih%2BoqHzz%2FzYB7Iku9kX98axy3FYncYAtx0c0QEWD1YCUQby0XcUx%2BMruoVogWox1KrUQfFP4bH0Dt4zGTksDl8L6A3W4SG2m3dxxH6&X-Amz-Signature=4b9f12c7fb7477aa663dcd26c5bb4618b3a3f0c836a8243afebeac9f101556de&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666FG6GVA4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFEDTQM12EBPLY%2B2R0a4eNqBh0InwUqgZOFjh9r%2F1N8LAiEAhDvADicuZexACYB7panf9w8qLy%2BMeiUPxSJC4cCcM1MqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG7g5FFbFd17pFZLnCrcA3zW3%2BktXinbOfQSXU1j%2FFuDZWmaLHeyJIuSLVpCmpN5ofIdBnXK2m4Y7sBr8PeRfYuoLPgQDh3%2FEzEkftVpJRy%2F2IjyI4lkT8ZTRV3OH4%2FI9JutYAYBG7mRtAEJ4j3%2FLqRoCiM5fS3hu9cCtTlb%2BM3QD0bYleIPOvCG3dzXX4zgsuLHm%2F9yVFiKk0%2BbMZyBRC8MJ0MKA9b03cUq757Xb4MBXfulDE0NgJKTHhaODyDsoIUept4QiJkgcAyZHBjJ99n4YWgfIdUgK2gYngndCbEh1Be9rBbu2%2Bmd9cjfP7wHnF2UanrgyWqmq3Q7p6iAWYAJEH%2FKrDL7xluLB6iuRY6WoWKMrOeRZtxvSALX%2FEORF35QgYnmpLm6g7cSRhq7sMgMsJVEAq8h%2Fks2q6ddIO4T13IhvkSfa6EJSM56iSiDppAb0ekqkl8daFVMC3lwrukk3o9OVCOd%2FR9e%2FE7JsseGUN%2Funip79DhPF9Uu3OefELodvRmknLMdIToTXXVPTidnZEFLtHhx0iPxJ5EJ7RMd2mmE62m%2BTM6mCPajJFCT9jJ2HDWUYVfU9cTsCKnh8tCPnW7w0A6Gtct2qE7jhD85DRSovCuiTUvKQx%2Fp3ZU53RYLRuEx%2FnXqY92AMP%2B%2F%2FbwGOqUBSfb9gXpm%2FdymYZPQEsg2%2F%2Bw5jTWLvzVjc2WnAbx6wleejWH0YM%2BrQMmbZQ8vF32RQjQ0V9XPZ2Aho7vTkCDL5ChX9NsyR0Ri3OThMbQcnwWzlk6YAOqp%2B2ih%2BoqHzz%2FzYB7Iku9kX98axy3FYncYAtx0c0QEWD1YCUQby0XcUx%2BMruoVogWox1KrUQfFP4bH0Dt4zGTksDl8L6A3W4SG2m3dxxH6&X-Amz-Signature=50b080ec16a2a47fc2d624da4bf482f9abcf540617941f3a993701e2c99bd931&X-Amz-SignedHeaders=host&x-id=GetObject)
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


