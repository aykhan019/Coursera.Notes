

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMHOHCOL%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIFBaqJKqeqNdmenXtbQ1Zw8v32HXofGPgU8OtS%2FC6qyVAiAWv5x%2FE9a72Ixi6OjdauuoTRvli0yyQcJ0BVV8mFcuLSr%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMBxeT3%2F758hlxtomEKtwDoP421EDkbcNgq65sbvJY2EXVRKp5%2Fa%2FayglVn9LPb7guvRpp9sZFBxtP0dkbFoG2RMuSHfCQQ5NYhWkQ2iaA3oPnoi8UgKDPx39tTKvgOYfXlnu6WHY4BPJegtXK%2ButTlVfXPT99vfDoJnABbHokBc8RHFQlNzzIQgAw1oaotEM8YozfJ61Fa446kNsrJ7J82sPXdcCs75orRZwI4ImtaAczahDz94BI1oSdDmojUdPtxm7CCbZI7JpJDjFphrO2kc8Vzdb6veghN7HSiEJg7QrtYkE5W4OEM34UIF1VMQVJo7EWDff1x%2FPSDvuK8kCbwenmZz3aDUNLcqW%2F7dw19bgXazU7kX9a5zcbRCbkUeuWxTeCTjnTL3KoIO4VtVFV3o3ka6DJEyz0Kl3DSqxocPuR2n%2BweO9777pYvoBPxwjC3HwNw7o57RX66KQYQOhBODMxZSPZJ8gIqQ%2B04eXnDA7eW0Tm5avgx%2FSvxPwSr20%2F7nKrheXPE2Tgv1KwWhEFPlQ%2BdFaCbKY%2BnIIZR97kZz7vivjgluHz0RJ24Pvq6d%2Fb1W5HmFRZ4ZB5%2FctR6jlQQxYNDQyTBuptlAm35JOp5lhUJSeFHUgEJ0ASojBLGQf15FD%2BVEdfCaZxX2EwzeyRvQY6pgGzi%2BVgW7e5gb7GpbQtklMu668CNkr%2BgrM1QtStrj%2Fa6X0NfeIw28WD%2FYY7JR6uAHppbdoxdzzIpyM%2Fo%2FV%2B5FowAUoOeVtzZW7IDEeC9Y%2BSeBhtIzLkR4tr%2Bo8Em0Gm6DxT6ZgBfZXJKYwAzQ%2BThcpREmxsyzbOMEFVLIHg9YaOm633nIRn31KBYR4HIBUTSOnMvDCL5EVCuw5YObgA6WN%2B5BGT3ChU&X-Amz-Signature=2de71ac44a2958415e3b705ba3ae2d310619278bbf466245d72993722d155496&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMYMOAWR%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIBmCk98lam9emQPYuvUepfYD12RpZCl0LXo4VEDz6pMpAiBqsrnWxlyIWTGAiyyZ6mFmyvHkNUD2oFX%2FhzGiHfqUzir%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMm5GdQCEl3CuJ10DgKtwD56uWe1YznwXogY1kAWF0YcZTT7cOMtBrdmYVcj2EuK03QJ5m5fjZFD%2BVPk4LOeOZ92CGCFWZY88FqY8nztDxjUy%2Fc0tSGxbZFDpEVDfm8%2BdCmGHDgP4UyUSQTseuIVB9HUpyKrGm0ouIw8m1sLIl7pi7vP9bfq0c3Adr2qy6QMa8173tipSzazdNzrLdoW%2FNoaBDzoAxHwdw%2FJ5wv7u3ZHgQVMDU5z%2FQc89065%2Bnq4z2han9rZ7tNb9amnZY66vGqd3aExDjfkPuPsug477UvEpuTP5BIdeRqqRCBCK1KwipLjg0VAgMx4kD1bsVAUHhFm8d%2BhXbpH1Yux%2FyyNB%2B7oFJhQzhHVNVBMb36bDg2bDJtJLShphUc09cgTV6fNz3HjwYosWMnvyvxTdPVCqikLZgJwsUr%2FN4P6YwT735mwghcmm8VF5rD9DYmqT%2BBQg2%2FSAQGLG44Cdnaak28lNaFURCLjsCGDC1bmgKYgf3vhly1%2FWycuZ2lm1pEDd3v42KHt4fzuBdY0eYkjlD%2FOwtC3ggaUZaITC0M2MHwDLKUNjpC10lGiWb2PsR9kgHEp8nwVufcFUKpFENtH6wBKOcxM6qnUYu%2BTQmB%2F42vOAJ3%2B%2B40aD7L0sOR7dhGfQwtOyRvQY6pgEERDJcFyiZNPf6zMBsdxuCqGpnzgC15DS9eYwcewJhTtJ8LttT2QJEwkl3TM3UoC%2FI2rv72XXSyzzv4xK3KtA4%2Bwo3OZEOJ1ZDwwdTPc8msg5Bnbn6IGMbN26IUL5oucV6S8iIhgJD0qlZa5cQKcd1l8Cu6DgyTwVehLzWdyQtjgED1qULI16fQhfZNXtjPUCD8gv1sCiBnxM%2F0Qsp6NcRHgSNmxew&X-Amz-Signature=c1ca32fd3f0b72df8babbdfadfe05c0f975a1cc6cd9a7f451efb504ea6c41b2b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMYMOAWR%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIBmCk98lam9emQPYuvUepfYD12RpZCl0LXo4VEDz6pMpAiBqsrnWxlyIWTGAiyyZ6mFmyvHkNUD2oFX%2FhzGiHfqUzir%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMm5GdQCEl3CuJ10DgKtwD56uWe1YznwXogY1kAWF0YcZTT7cOMtBrdmYVcj2EuK03QJ5m5fjZFD%2BVPk4LOeOZ92CGCFWZY88FqY8nztDxjUy%2Fc0tSGxbZFDpEVDfm8%2BdCmGHDgP4UyUSQTseuIVB9HUpyKrGm0ouIw8m1sLIl7pi7vP9bfq0c3Adr2qy6QMa8173tipSzazdNzrLdoW%2FNoaBDzoAxHwdw%2FJ5wv7u3ZHgQVMDU5z%2FQc89065%2Bnq4z2han9rZ7tNb9amnZY66vGqd3aExDjfkPuPsug477UvEpuTP5BIdeRqqRCBCK1KwipLjg0VAgMx4kD1bsVAUHhFm8d%2BhXbpH1Yux%2FyyNB%2B7oFJhQzhHVNVBMb36bDg2bDJtJLShphUc09cgTV6fNz3HjwYosWMnvyvxTdPVCqikLZgJwsUr%2FN4P6YwT735mwghcmm8VF5rD9DYmqT%2BBQg2%2FSAQGLG44Cdnaak28lNaFURCLjsCGDC1bmgKYgf3vhly1%2FWycuZ2lm1pEDd3v42KHt4fzuBdY0eYkjlD%2FOwtC3ggaUZaITC0M2MHwDLKUNjpC10lGiWb2PsR9kgHEp8nwVufcFUKpFENtH6wBKOcxM6qnUYu%2BTQmB%2F42vOAJ3%2B%2B40aD7L0sOR7dhGfQwtOyRvQY6pgEERDJcFyiZNPf6zMBsdxuCqGpnzgC15DS9eYwcewJhTtJ8LttT2QJEwkl3TM3UoC%2FI2rv72XXSyzzv4xK3KtA4%2Bwo3OZEOJ1ZDwwdTPc8msg5Bnbn6IGMbN26IUL5oucV6S8iIhgJD0qlZa5cQKcd1l8Cu6DgyTwVehLzWdyQtjgED1qULI16fQhfZNXtjPUCD8gv1sCiBnxM%2F0Qsp6NcRHgSNmxew&X-Amz-Signature=30a5f292a936f84f005f7c3aa2fa27f15ce58dca7e644d9705bc2b8ec5f9e586&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMYMOAWR%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIBmCk98lam9emQPYuvUepfYD12RpZCl0LXo4VEDz6pMpAiBqsrnWxlyIWTGAiyyZ6mFmyvHkNUD2oFX%2FhzGiHfqUzir%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMm5GdQCEl3CuJ10DgKtwD56uWe1YznwXogY1kAWF0YcZTT7cOMtBrdmYVcj2EuK03QJ5m5fjZFD%2BVPk4LOeOZ92CGCFWZY88FqY8nztDxjUy%2Fc0tSGxbZFDpEVDfm8%2BdCmGHDgP4UyUSQTseuIVB9HUpyKrGm0ouIw8m1sLIl7pi7vP9bfq0c3Adr2qy6QMa8173tipSzazdNzrLdoW%2FNoaBDzoAxHwdw%2FJ5wv7u3ZHgQVMDU5z%2FQc89065%2Bnq4z2han9rZ7tNb9amnZY66vGqd3aExDjfkPuPsug477UvEpuTP5BIdeRqqRCBCK1KwipLjg0VAgMx4kD1bsVAUHhFm8d%2BhXbpH1Yux%2FyyNB%2B7oFJhQzhHVNVBMb36bDg2bDJtJLShphUc09cgTV6fNz3HjwYosWMnvyvxTdPVCqikLZgJwsUr%2FN4P6YwT735mwghcmm8VF5rD9DYmqT%2BBQg2%2FSAQGLG44Cdnaak28lNaFURCLjsCGDC1bmgKYgf3vhly1%2FWycuZ2lm1pEDd3v42KHt4fzuBdY0eYkjlD%2FOwtC3ggaUZaITC0M2MHwDLKUNjpC10lGiWb2PsR9kgHEp8nwVufcFUKpFENtH6wBKOcxM6qnUYu%2BTQmB%2F42vOAJ3%2B%2B40aD7L0sOR7dhGfQwtOyRvQY6pgEERDJcFyiZNPf6zMBsdxuCqGpnzgC15DS9eYwcewJhTtJ8LttT2QJEwkl3TM3UoC%2FI2rv72XXSyzzv4xK3KtA4%2Bwo3OZEOJ1ZDwwdTPc8msg5Bnbn6IGMbN26IUL5oucV6S8iIhgJD0qlZa5cQKcd1l8Cu6DgyTwVehLzWdyQtjgED1qULI16fQhfZNXtjPUCD8gv1sCiBnxM%2F0Qsp6NcRHgSNmxew&X-Amz-Signature=cf07293e36f2a4513a33698e409405db56584790290597c1a4736de5c08d7e96&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMYMOAWR%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIBmCk98lam9emQPYuvUepfYD12RpZCl0LXo4VEDz6pMpAiBqsrnWxlyIWTGAiyyZ6mFmyvHkNUD2oFX%2FhzGiHfqUzir%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMm5GdQCEl3CuJ10DgKtwD56uWe1YznwXogY1kAWF0YcZTT7cOMtBrdmYVcj2EuK03QJ5m5fjZFD%2BVPk4LOeOZ92CGCFWZY88FqY8nztDxjUy%2Fc0tSGxbZFDpEVDfm8%2BdCmGHDgP4UyUSQTseuIVB9HUpyKrGm0ouIw8m1sLIl7pi7vP9bfq0c3Adr2qy6QMa8173tipSzazdNzrLdoW%2FNoaBDzoAxHwdw%2FJ5wv7u3ZHgQVMDU5z%2FQc89065%2Bnq4z2han9rZ7tNb9amnZY66vGqd3aExDjfkPuPsug477UvEpuTP5BIdeRqqRCBCK1KwipLjg0VAgMx4kD1bsVAUHhFm8d%2BhXbpH1Yux%2FyyNB%2B7oFJhQzhHVNVBMb36bDg2bDJtJLShphUc09cgTV6fNz3HjwYosWMnvyvxTdPVCqikLZgJwsUr%2FN4P6YwT735mwghcmm8VF5rD9DYmqT%2BBQg2%2FSAQGLG44Cdnaak28lNaFURCLjsCGDC1bmgKYgf3vhly1%2FWycuZ2lm1pEDd3v42KHt4fzuBdY0eYkjlD%2FOwtC3ggaUZaITC0M2MHwDLKUNjpC10lGiWb2PsR9kgHEp8nwVufcFUKpFENtH6wBKOcxM6qnUYu%2BTQmB%2F42vOAJ3%2B%2B40aD7L0sOR7dhGfQwtOyRvQY6pgEERDJcFyiZNPf6zMBsdxuCqGpnzgC15DS9eYwcewJhTtJ8LttT2QJEwkl3TM3UoC%2FI2rv72XXSyzzv4xK3KtA4%2Bwo3OZEOJ1ZDwwdTPc8msg5Bnbn6IGMbN26IUL5oucV6S8iIhgJD0qlZa5cQKcd1l8Cu6DgyTwVehLzWdyQtjgED1qULI16fQhfZNXtjPUCD8gv1sCiBnxM%2F0Qsp6NcRHgSNmxew&X-Amz-Signature=a459583137d9cffc1070a4e09bdb619af01b61f5c8762197c3ac1327fa5ee573&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMYMOAWR%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIBmCk98lam9emQPYuvUepfYD12RpZCl0LXo4VEDz6pMpAiBqsrnWxlyIWTGAiyyZ6mFmyvHkNUD2oFX%2FhzGiHfqUzir%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMm5GdQCEl3CuJ10DgKtwD56uWe1YznwXogY1kAWF0YcZTT7cOMtBrdmYVcj2EuK03QJ5m5fjZFD%2BVPk4LOeOZ92CGCFWZY88FqY8nztDxjUy%2Fc0tSGxbZFDpEVDfm8%2BdCmGHDgP4UyUSQTseuIVB9HUpyKrGm0ouIw8m1sLIl7pi7vP9bfq0c3Adr2qy6QMa8173tipSzazdNzrLdoW%2FNoaBDzoAxHwdw%2FJ5wv7u3ZHgQVMDU5z%2FQc89065%2Bnq4z2han9rZ7tNb9amnZY66vGqd3aExDjfkPuPsug477UvEpuTP5BIdeRqqRCBCK1KwipLjg0VAgMx4kD1bsVAUHhFm8d%2BhXbpH1Yux%2FyyNB%2B7oFJhQzhHVNVBMb36bDg2bDJtJLShphUc09cgTV6fNz3HjwYosWMnvyvxTdPVCqikLZgJwsUr%2FN4P6YwT735mwghcmm8VF5rD9DYmqT%2BBQg2%2FSAQGLG44Cdnaak28lNaFURCLjsCGDC1bmgKYgf3vhly1%2FWycuZ2lm1pEDd3v42KHt4fzuBdY0eYkjlD%2FOwtC3ggaUZaITC0M2MHwDLKUNjpC10lGiWb2PsR9kgHEp8nwVufcFUKpFENtH6wBKOcxM6qnUYu%2BTQmB%2F42vOAJ3%2B%2B40aD7L0sOR7dhGfQwtOyRvQY6pgEERDJcFyiZNPf6zMBsdxuCqGpnzgC15DS9eYwcewJhTtJ8LttT2QJEwkl3TM3UoC%2FI2rv72XXSyzzv4xK3KtA4%2Bwo3OZEOJ1ZDwwdTPc8msg5Bnbn6IGMbN26IUL5oucV6S8iIhgJD0qlZa5cQKcd1l8Cu6DgyTwVehLzWdyQtjgED1qULI16fQhfZNXtjPUCD8gv1sCiBnxM%2F0Qsp6NcRHgSNmxew&X-Amz-Signature=222ab2c6670b72550537eb7b6b57670eba772a65fabba85efe580d6d43a4f892&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMHOHCOL%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIFBaqJKqeqNdmenXtbQ1Zw8v32HXofGPgU8OtS%2FC6qyVAiAWv5x%2FE9a72Ixi6OjdauuoTRvli0yyQcJ0BVV8mFcuLSr%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMBxeT3%2F758hlxtomEKtwDoP421EDkbcNgq65sbvJY2EXVRKp5%2Fa%2FayglVn9LPb7guvRpp9sZFBxtP0dkbFoG2RMuSHfCQQ5NYhWkQ2iaA3oPnoi8UgKDPx39tTKvgOYfXlnu6WHY4BPJegtXK%2ButTlVfXPT99vfDoJnABbHokBc8RHFQlNzzIQgAw1oaotEM8YozfJ61Fa446kNsrJ7J82sPXdcCs75orRZwI4ImtaAczahDz94BI1oSdDmojUdPtxm7CCbZI7JpJDjFphrO2kc8Vzdb6veghN7HSiEJg7QrtYkE5W4OEM34UIF1VMQVJo7EWDff1x%2FPSDvuK8kCbwenmZz3aDUNLcqW%2F7dw19bgXazU7kX9a5zcbRCbkUeuWxTeCTjnTL3KoIO4VtVFV3o3ka6DJEyz0Kl3DSqxocPuR2n%2BweO9777pYvoBPxwjC3HwNw7o57RX66KQYQOhBODMxZSPZJ8gIqQ%2B04eXnDA7eW0Tm5avgx%2FSvxPwSr20%2F7nKrheXPE2Tgv1KwWhEFPlQ%2BdFaCbKY%2BnIIZR97kZz7vivjgluHz0RJ24Pvq6d%2Fb1W5HmFRZ4ZB5%2FctR6jlQQxYNDQyTBuptlAm35JOp5lhUJSeFHUgEJ0ASojBLGQf15FD%2BVEdfCaZxX2EwzeyRvQY6pgGzi%2BVgW7e5gb7GpbQtklMu668CNkr%2BgrM1QtStrj%2Fa6X0NfeIw28WD%2FYY7JR6uAHppbdoxdzzIpyM%2Fo%2FV%2B5FowAUoOeVtzZW7IDEeC9Y%2BSeBhtIzLkR4tr%2Bo8Em0Gm6DxT6ZgBfZXJKYwAzQ%2BThcpREmxsyzbOMEFVLIHg9YaOm633nIRn31KBYR4HIBUTSOnMvDCL5EVCuw5YObgA6WN%2B5BGT3ChU&X-Amz-Signature=f732016b552942aace62505d4727417d7f7a12904f55260b64c89ccd15194fd5&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMHOHCOL%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIFBaqJKqeqNdmenXtbQ1Zw8v32HXofGPgU8OtS%2FC6qyVAiAWv5x%2FE9a72Ixi6OjdauuoTRvli0yyQcJ0BVV8mFcuLSr%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMBxeT3%2F758hlxtomEKtwDoP421EDkbcNgq65sbvJY2EXVRKp5%2Fa%2FayglVn9LPb7guvRpp9sZFBxtP0dkbFoG2RMuSHfCQQ5NYhWkQ2iaA3oPnoi8UgKDPx39tTKvgOYfXlnu6WHY4BPJegtXK%2ButTlVfXPT99vfDoJnABbHokBc8RHFQlNzzIQgAw1oaotEM8YozfJ61Fa446kNsrJ7J82sPXdcCs75orRZwI4ImtaAczahDz94BI1oSdDmojUdPtxm7CCbZI7JpJDjFphrO2kc8Vzdb6veghN7HSiEJg7QrtYkE5W4OEM34UIF1VMQVJo7EWDff1x%2FPSDvuK8kCbwenmZz3aDUNLcqW%2F7dw19bgXazU7kX9a5zcbRCbkUeuWxTeCTjnTL3KoIO4VtVFV3o3ka6DJEyz0Kl3DSqxocPuR2n%2BweO9777pYvoBPxwjC3HwNw7o57RX66KQYQOhBODMxZSPZJ8gIqQ%2B04eXnDA7eW0Tm5avgx%2FSvxPwSr20%2F7nKrheXPE2Tgv1KwWhEFPlQ%2BdFaCbKY%2BnIIZR97kZz7vivjgluHz0RJ24Pvq6d%2Fb1W5HmFRZ4ZB5%2FctR6jlQQxYNDQyTBuptlAm35JOp5lhUJSeFHUgEJ0ASojBLGQf15FD%2BVEdfCaZxX2EwzeyRvQY6pgGzi%2BVgW7e5gb7GpbQtklMu668CNkr%2BgrM1QtStrj%2Fa6X0NfeIw28WD%2FYY7JR6uAHppbdoxdzzIpyM%2Fo%2FV%2B5FowAUoOeVtzZW7IDEeC9Y%2BSeBhtIzLkR4tr%2Bo8Em0Gm6DxT6ZgBfZXJKYwAzQ%2BThcpREmxsyzbOMEFVLIHg9YaOm633nIRn31KBYR4HIBUTSOnMvDCL5EVCuw5YObgA6WN%2B5BGT3ChU&X-Amz-Signature=9b6b8c3a704f3d96953fca89ad5a1f7ccfc08bd397b338ed1a348b908e9c964e&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMHOHCOL%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIFBaqJKqeqNdmenXtbQ1Zw8v32HXofGPgU8OtS%2FC6qyVAiAWv5x%2FE9a72Ixi6OjdauuoTRvli0yyQcJ0BVV8mFcuLSr%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMBxeT3%2F758hlxtomEKtwDoP421EDkbcNgq65sbvJY2EXVRKp5%2Fa%2FayglVn9LPb7guvRpp9sZFBxtP0dkbFoG2RMuSHfCQQ5NYhWkQ2iaA3oPnoi8UgKDPx39tTKvgOYfXlnu6WHY4BPJegtXK%2ButTlVfXPT99vfDoJnABbHokBc8RHFQlNzzIQgAw1oaotEM8YozfJ61Fa446kNsrJ7J82sPXdcCs75orRZwI4ImtaAczahDz94BI1oSdDmojUdPtxm7CCbZI7JpJDjFphrO2kc8Vzdb6veghN7HSiEJg7QrtYkE5W4OEM34UIF1VMQVJo7EWDff1x%2FPSDvuK8kCbwenmZz3aDUNLcqW%2F7dw19bgXazU7kX9a5zcbRCbkUeuWxTeCTjnTL3KoIO4VtVFV3o3ka6DJEyz0Kl3DSqxocPuR2n%2BweO9777pYvoBPxwjC3HwNw7o57RX66KQYQOhBODMxZSPZJ8gIqQ%2B04eXnDA7eW0Tm5avgx%2FSvxPwSr20%2F7nKrheXPE2Tgv1KwWhEFPlQ%2BdFaCbKY%2BnIIZR97kZz7vivjgluHz0RJ24Pvq6d%2Fb1W5HmFRZ4ZB5%2FctR6jlQQxYNDQyTBuptlAm35JOp5lhUJSeFHUgEJ0ASojBLGQf15FD%2BVEdfCaZxX2EwzeyRvQY6pgGzi%2BVgW7e5gb7GpbQtklMu668CNkr%2BgrM1QtStrj%2Fa6X0NfeIw28WD%2FYY7JR6uAHppbdoxdzzIpyM%2Fo%2FV%2B5FowAUoOeVtzZW7IDEeC9Y%2BSeBhtIzLkR4tr%2Bo8Em0Gm6DxT6ZgBfZXJKYwAzQ%2BThcpREmxsyzbOMEFVLIHg9YaOm633nIRn31KBYR4HIBUTSOnMvDCL5EVCuw5YObgA6WN%2B5BGT3ChU&X-Amz-Signature=99e8506f427c8491348d2fc795b1655364836dbda822e1bc4e8f189a449ceae4&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMHOHCOL%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIFBaqJKqeqNdmenXtbQ1Zw8v32HXofGPgU8OtS%2FC6qyVAiAWv5x%2FE9a72Ixi6OjdauuoTRvli0yyQcJ0BVV8mFcuLSr%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMBxeT3%2F758hlxtomEKtwDoP421EDkbcNgq65sbvJY2EXVRKp5%2Fa%2FayglVn9LPb7guvRpp9sZFBxtP0dkbFoG2RMuSHfCQQ5NYhWkQ2iaA3oPnoi8UgKDPx39tTKvgOYfXlnu6WHY4BPJegtXK%2ButTlVfXPT99vfDoJnABbHokBc8RHFQlNzzIQgAw1oaotEM8YozfJ61Fa446kNsrJ7J82sPXdcCs75orRZwI4ImtaAczahDz94BI1oSdDmojUdPtxm7CCbZI7JpJDjFphrO2kc8Vzdb6veghN7HSiEJg7QrtYkE5W4OEM34UIF1VMQVJo7EWDff1x%2FPSDvuK8kCbwenmZz3aDUNLcqW%2F7dw19bgXazU7kX9a5zcbRCbkUeuWxTeCTjnTL3KoIO4VtVFV3o3ka6DJEyz0Kl3DSqxocPuR2n%2BweO9777pYvoBPxwjC3HwNw7o57RX66KQYQOhBODMxZSPZJ8gIqQ%2B04eXnDA7eW0Tm5avgx%2FSvxPwSr20%2F7nKrheXPE2Tgv1KwWhEFPlQ%2BdFaCbKY%2BnIIZR97kZz7vivjgluHz0RJ24Pvq6d%2Fb1W5HmFRZ4ZB5%2FctR6jlQQxYNDQyTBuptlAm35JOp5lhUJSeFHUgEJ0ASojBLGQf15FD%2BVEdfCaZxX2EwzeyRvQY6pgGzi%2BVgW7e5gb7GpbQtklMu668CNkr%2BgrM1QtStrj%2Fa6X0NfeIw28WD%2FYY7JR6uAHppbdoxdzzIpyM%2Fo%2FV%2B5FowAUoOeVtzZW7IDEeC9Y%2BSeBhtIzLkR4tr%2Bo8Em0Gm6DxT6ZgBfZXJKYwAzQ%2BThcpREmxsyzbOMEFVLIHg9YaOm633nIRn31KBYR4HIBUTSOnMvDCL5EVCuw5YObgA6WN%2B5BGT3ChU&X-Amz-Signature=ae4febfa30c3467d80b859bba8db37011529b987b078875d446d27cc2e7808e4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMHOHCOL%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIFBaqJKqeqNdmenXtbQ1Zw8v32HXofGPgU8OtS%2FC6qyVAiAWv5x%2FE9a72Ixi6OjdauuoTRvli0yyQcJ0BVV8mFcuLSr%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMBxeT3%2F758hlxtomEKtwDoP421EDkbcNgq65sbvJY2EXVRKp5%2Fa%2FayglVn9LPb7guvRpp9sZFBxtP0dkbFoG2RMuSHfCQQ5NYhWkQ2iaA3oPnoi8UgKDPx39tTKvgOYfXlnu6WHY4BPJegtXK%2ButTlVfXPT99vfDoJnABbHokBc8RHFQlNzzIQgAw1oaotEM8YozfJ61Fa446kNsrJ7J82sPXdcCs75orRZwI4ImtaAczahDz94BI1oSdDmojUdPtxm7CCbZI7JpJDjFphrO2kc8Vzdb6veghN7HSiEJg7QrtYkE5W4OEM34UIF1VMQVJo7EWDff1x%2FPSDvuK8kCbwenmZz3aDUNLcqW%2F7dw19bgXazU7kX9a5zcbRCbkUeuWxTeCTjnTL3KoIO4VtVFV3o3ka6DJEyz0Kl3DSqxocPuR2n%2BweO9777pYvoBPxwjC3HwNw7o57RX66KQYQOhBODMxZSPZJ8gIqQ%2B04eXnDA7eW0Tm5avgx%2FSvxPwSr20%2F7nKrheXPE2Tgv1KwWhEFPlQ%2BdFaCbKY%2BnIIZR97kZz7vivjgluHz0RJ24Pvq6d%2Fb1W5HmFRZ4ZB5%2FctR6jlQQxYNDQyTBuptlAm35JOp5lhUJSeFHUgEJ0ASojBLGQf15FD%2BVEdfCaZxX2EwzeyRvQY6pgGzi%2BVgW7e5gb7GpbQtklMu668CNkr%2BgrM1QtStrj%2Fa6X0NfeIw28WD%2FYY7JR6uAHppbdoxdzzIpyM%2Fo%2FV%2B5FowAUoOeVtzZW7IDEeC9Y%2BSeBhtIzLkR4tr%2Bo8Em0Gm6DxT6ZgBfZXJKYwAzQ%2BThcpREmxsyzbOMEFVLIHg9YaOm633nIRn31KBYR4HIBUTSOnMvDCL5EVCuw5YObgA6WN%2B5BGT3ChU&X-Amz-Signature=0aaa97e9b12516b90364172f5561d22f1a5b7edc390d8fcecbad7a79c66c2c3d&X-Amz-SignedHeaders=host&x-id=GetObject)
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


