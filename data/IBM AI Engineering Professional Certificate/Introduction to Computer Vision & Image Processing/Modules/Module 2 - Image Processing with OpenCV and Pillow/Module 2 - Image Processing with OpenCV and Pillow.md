

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3BQWDTT%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJIMEYCIQCSmZEx5c%2BOq%2F8%2F8h8Q8URRGv%2BUp83assraKl%2BEJagJtQIhAK%2FOWumGUVNOmjNk4jL2bBANZhF%2FxxX6NNM0Jxh148rmKv8DCHsQABoMNjM3NDIzMTgzODA1IgwnAJlmxGG2YbGXuDIq3ANbbiAhHA8XHr3V7SEM2GQlRJMQs67pD0Wc3kjZmM9iiJtj7syodzQL0AuFgnHsqJem1X0RKZ6DBOd4TLix9TjWk9C%2B0wUwpXgpZI6otMfqzU90TrJ%2BsbGcIAuD62zkHNXUPQH%2FRd3rIyOZECLrGwjHrQK1F80%2FNcJ7sSBY5mCUU13IINQfZlbTtLNNw9%2FhFkU5ju2jcbnjbDXtcqUzxzfYd1mpmH4%2F8o%2B8bTT6HoVr%2BUBmrX8mscJkKUyUJ49UAZfJ2UfZ6BxUolDMtZ5MJCnjJT7JYDSFKglm1BNhaRYBkOc3MdFBzz6E9QFzTzzVlc5qJX8Gbzrk5pDz2bOPWUQnIUT0PDkZBkUXjHRP9BvMRKp97Wdd7q0b2c5%2Fz9MsiO0ua7T8ER7ogmsVSK52UZy%2BDGh6lII%2Bu45%2B5gNG%2BFjHsbXAZD%2FHU5PPvl0soP68m%2F54amfQDDKL5YVsxrXBzfZolCfrc6%2BPGErhvZ1X6sPurfn0QEOPd%2FjjfAkwcnSTyvAdQ0rjlw4AEP22t2eGnwn0CnD0QzaHZVozz0%2FBhigax%2BWvkWRhpdyN3btVhVGj%2FWx9hglJfUZWf7qiwPbxCiQEhLd%2Fu6ITYqNJ3a2jRwY7MQg3SBgCkg4Dotw%2BuDDAmZm9BjqkAS083kgR0UidG4Xric85th0Pn9OVMdrZ8ctUfMoTpqAuZwlaNYauvkhtq0%2BjMqncTN7eZdvMAmjvR6cuta3NtRORxUVG5av87E83AdVUaWPEHUmWthh1HxZgsNLtK3ZdfKNAumHMejb%2BsITf59x1qjZRrbA2HLFDNkY9xCWkHaIkZv8cCYIulfVj2nYxGkuFXpcaZsCIC5quDUjbnbeLtuhMzN%2BF&X-Amz-Signature=0ba293e55b138b7ca0e3598499c631638caebdfe9a899053b8561462514a4224&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYUXTVF4%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIAq9Qu9X6F7V0FErPG%2FKj0P2W3%2FWYCFtZ%2BR%2BprS6wPIpAiEA1F%2B7S2sO48RTlDEZzHqZ%2FySbl%2FK1hZ%2F4lgAmYGDS8SYq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDMBLUZyTjVP5VLCz0SrcA3lbLngHuQ4PcGmKRycYZHM85qMvTNOaGJ8Sm0Eyi0UMRYqzkuYio4VDZMRPqCB4ERuDYf1twq6jz6jqZ6gskvSSS%2FWb1yxyrxMXhigJnk0HjJRqIeF13GTiSmm7jZMCfiKhfJKCjySKlyhdyK1uoJxZoQINfk9ECnf0iLkqkPwIsXjz0HtmdP8Z6csouNTGD4ehm%2BJQCaGIsFBajqDedillQ3th%2BZFwrIQutuSsveTWjUn2%2BXO0NFfcv1Fv%2Fzqag%2BNx3gFzkMdVLw2lrlJStS1n%2B0PxUdjXWoxnm0T2WhoT2hppDmCl2aNU%2FRjHx1Gh6ZdeHOMD1e23RHm1FOBocwF7KQqRd2CY7L0f32p6EXsQsH%2FBWlgRIc9%2BHupqDTEZkh3%2F4%2FK7TDwiRowC2RQ1UVkjsSJi02Wy%2F5PNDLi%2FDSC13f5bb%2FdIzPZjhdiu%2B4kRAt3CjizxsvEoQE%2FgLkDHv0Y2IvCNr%2Bh1iimRkIvr%2BDAie2eVMCF%2BN%2FHWM4WIPlLyDzFByK78kBSctubP4aRny8q3Av6oQ2Z1EbuoaldhggOiJfoz9QpwKBdVeyFRG2BIqA1kikOtUikpFGVaOnyjx7vTVLMNTCgsMS9pNMWU7u0hMYKYmC9PEuYMCImjMPyZmb0GOqUBTu3zuEHGKTy2pmj1mOpIOGLxuMRH5tWm0GT8sqpC34r7zvaVc2nsInFrO5FAgNKin37bNh8ynMOxM5DH1mxHZmBz2tLND0mn14%2BsRIFDXEY%2F4MaCKxsSo9ARedueTZYz%2BteWkJMOQgYm0Su5QU9PegB%2BMP2EhzJ7LZa500m1MpFUW8aAn4Zy%2FvU%2BpV04yWZr6T6pKX59oTjVKDQbkmnDkTcTsf1n&X-Amz-Signature=a60594230405dbc6d5a673426b68f95f24c876ad2b69af9c95ccd6cedb87dd7b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYUXTVF4%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIAq9Qu9X6F7V0FErPG%2FKj0P2W3%2FWYCFtZ%2BR%2BprS6wPIpAiEA1F%2B7S2sO48RTlDEZzHqZ%2FySbl%2FK1hZ%2F4lgAmYGDS8SYq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDMBLUZyTjVP5VLCz0SrcA3lbLngHuQ4PcGmKRycYZHM85qMvTNOaGJ8Sm0Eyi0UMRYqzkuYio4VDZMRPqCB4ERuDYf1twq6jz6jqZ6gskvSSS%2FWb1yxyrxMXhigJnk0HjJRqIeF13GTiSmm7jZMCfiKhfJKCjySKlyhdyK1uoJxZoQINfk9ECnf0iLkqkPwIsXjz0HtmdP8Z6csouNTGD4ehm%2BJQCaGIsFBajqDedillQ3th%2BZFwrIQutuSsveTWjUn2%2BXO0NFfcv1Fv%2Fzqag%2BNx3gFzkMdVLw2lrlJStS1n%2B0PxUdjXWoxnm0T2WhoT2hppDmCl2aNU%2FRjHx1Gh6ZdeHOMD1e23RHm1FOBocwF7KQqRd2CY7L0f32p6EXsQsH%2FBWlgRIc9%2BHupqDTEZkh3%2F4%2FK7TDwiRowC2RQ1UVkjsSJi02Wy%2F5PNDLi%2FDSC13f5bb%2FdIzPZjhdiu%2B4kRAt3CjizxsvEoQE%2FgLkDHv0Y2IvCNr%2Bh1iimRkIvr%2BDAie2eVMCF%2BN%2FHWM4WIPlLyDzFByK78kBSctubP4aRny8q3Av6oQ2Z1EbuoaldhggOiJfoz9QpwKBdVeyFRG2BIqA1kikOtUikpFGVaOnyjx7vTVLMNTCgsMS9pNMWU7u0hMYKYmC9PEuYMCImjMPyZmb0GOqUBTu3zuEHGKTy2pmj1mOpIOGLxuMRH5tWm0GT8sqpC34r7zvaVc2nsInFrO5FAgNKin37bNh8ynMOxM5DH1mxHZmBz2tLND0mn14%2BsRIFDXEY%2F4MaCKxsSo9ARedueTZYz%2BteWkJMOQgYm0Su5QU9PegB%2BMP2EhzJ7LZa500m1MpFUW8aAn4Zy%2FvU%2BpV04yWZr6T6pKX59oTjVKDQbkmnDkTcTsf1n&X-Amz-Signature=ea9f15afbcad65fc0026f983c5e51e7de73779929226167e1de75cb5677bac72&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYUXTVF4%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIAq9Qu9X6F7V0FErPG%2FKj0P2W3%2FWYCFtZ%2BR%2BprS6wPIpAiEA1F%2B7S2sO48RTlDEZzHqZ%2FySbl%2FK1hZ%2F4lgAmYGDS8SYq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDMBLUZyTjVP5VLCz0SrcA3lbLngHuQ4PcGmKRycYZHM85qMvTNOaGJ8Sm0Eyi0UMRYqzkuYio4VDZMRPqCB4ERuDYf1twq6jz6jqZ6gskvSSS%2FWb1yxyrxMXhigJnk0HjJRqIeF13GTiSmm7jZMCfiKhfJKCjySKlyhdyK1uoJxZoQINfk9ECnf0iLkqkPwIsXjz0HtmdP8Z6csouNTGD4ehm%2BJQCaGIsFBajqDedillQ3th%2BZFwrIQutuSsveTWjUn2%2BXO0NFfcv1Fv%2Fzqag%2BNx3gFzkMdVLw2lrlJStS1n%2B0PxUdjXWoxnm0T2WhoT2hppDmCl2aNU%2FRjHx1Gh6ZdeHOMD1e23RHm1FOBocwF7KQqRd2CY7L0f32p6EXsQsH%2FBWlgRIc9%2BHupqDTEZkh3%2F4%2FK7TDwiRowC2RQ1UVkjsSJi02Wy%2F5PNDLi%2FDSC13f5bb%2FdIzPZjhdiu%2B4kRAt3CjizxsvEoQE%2FgLkDHv0Y2IvCNr%2Bh1iimRkIvr%2BDAie2eVMCF%2BN%2FHWM4WIPlLyDzFByK78kBSctubP4aRny8q3Av6oQ2Z1EbuoaldhggOiJfoz9QpwKBdVeyFRG2BIqA1kikOtUikpFGVaOnyjx7vTVLMNTCgsMS9pNMWU7u0hMYKYmC9PEuYMCImjMPyZmb0GOqUBTu3zuEHGKTy2pmj1mOpIOGLxuMRH5tWm0GT8sqpC34r7zvaVc2nsInFrO5FAgNKin37bNh8ynMOxM5DH1mxHZmBz2tLND0mn14%2BsRIFDXEY%2F4MaCKxsSo9ARedueTZYz%2BteWkJMOQgYm0Su5QU9PegB%2BMP2EhzJ7LZa500m1MpFUW8aAn4Zy%2FvU%2BpV04yWZr6T6pKX59oTjVKDQbkmnDkTcTsf1n&X-Amz-Signature=d367943e33a80db7dd897f32b4434a0b93693885c902b62c6b8319b9bf7bf504&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYUXTVF4%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIAq9Qu9X6F7V0FErPG%2FKj0P2W3%2FWYCFtZ%2BR%2BprS6wPIpAiEA1F%2B7S2sO48RTlDEZzHqZ%2FySbl%2FK1hZ%2F4lgAmYGDS8SYq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDMBLUZyTjVP5VLCz0SrcA3lbLngHuQ4PcGmKRycYZHM85qMvTNOaGJ8Sm0Eyi0UMRYqzkuYio4VDZMRPqCB4ERuDYf1twq6jz6jqZ6gskvSSS%2FWb1yxyrxMXhigJnk0HjJRqIeF13GTiSmm7jZMCfiKhfJKCjySKlyhdyK1uoJxZoQINfk9ECnf0iLkqkPwIsXjz0HtmdP8Z6csouNTGD4ehm%2BJQCaGIsFBajqDedillQ3th%2BZFwrIQutuSsveTWjUn2%2BXO0NFfcv1Fv%2Fzqag%2BNx3gFzkMdVLw2lrlJStS1n%2B0PxUdjXWoxnm0T2WhoT2hppDmCl2aNU%2FRjHx1Gh6ZdeHOMD1e23RHm1FOBocwF7KQqRd2CY7L0f32p6EXsQsH%2FBWlgRIc9%2BHupqDTEZkh3%2F4%2FK7TDwiRowC2RQ1UVkjsSJi02Wy%2F5PNDLi%2FDSC13f5bb%2FdIzPZjhdiu%2B4kRAt3CjizxsvEoQE%2FgLkDHv0Y2IvCNr%2Bh1iimRkIvr%2BDAie2eVMCF%2BN%2FHWM4WIPlLyDzFByK78kBSctubP4aRny8q3Av6oQ2Z1EbuoaldhggOiJfoz9QpwKBdVeyFRG2BIqA1kikOtUikpFGVaOnyjx7vTVLMNTCgsMS9pNMWU7u0hMYKYmC9PEuYMCImjMPyZmb0GOqUBTu3zuEHGKTy2pmj1mOpIOGLxuMRH5tWm0GT8sqpC34r7zvaVc2nsInFrO5FAgNKin37bNh8ynMOxM5DH1mxHZmBz2tLND0mn14%2BsRIFDXEY%2F4MaCKxsSo9ARedueTZYz%2BteWkJMOQgYm0Su5QU9PegB%2BMP2EhzJ7LZa500m1MpFUW8aAn4Zy%2FvU%2BpV04yWZr6T6pKX59oTjVKDQbkmnDkTcTsf1n&X-Amz-Signature=157c0ad5b99ef2d7d16f3d11453c261f2de8e42bdccff8f7a360e620e84627d0&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYUXTVF4%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIAq9Qu9X6F7V0FErPG%2FKj0P2W3%2FWYCFtZ%2BR%2BprS6wPIpAiEA1F%2B7S2sO48RTlDEZzHqZ%2FySbl%2FK1hZ%2F4lgAmYGDS8SYq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDMBLUZyTjVP5VLCz0SrcA3lbLngHuQ4PcGmKRycYZHM85qMvTNOaGJ8Sm0Eyi0UMRYqzkuYio4VDZMRPqCB4ERuDYf1twq6jz6jqZ6gskvSSS%2FWb1yxyrxMXhigJnk0HjJRqIeF13GTiSmm7jZMCfiKhfJKCjySKlyhdyK1uoJxZoQINfk9ECnf0iLkqkPwIsXjz0HtmdP8Z6csouNTGD4ehm%2BJQCaGIsFBajqDedillQ3th%2BZFwrIQutuSsveTWjUn2%2BXO0NFfcv1Fv%2Fzqag%2BNx3gFzkMdVLw2lrlJStS1n%2B0PxUdjXWoxnm0T2WhoT2hppDmCl2aNU%2FRjHx1Gh6ZdeHOMD1e23RHm1FOBocwF7KQqRd2CY7L0f32p6EXsQsH%2FBWlgRIc9%2BHupqDTEZkh3%2F4%2FK7TDwiRowC2RQ1UVkjsSJi02Wy%2F5PNDLi%2FDSC13f5bb%2FdIzPZjhdiu%2B4kRAt3CjizxsvEoQE%2FgLkDHv0Y2IvCNr%2Bh1iimRkIvr%2BDAie2eVMCF%2BN%2FHWM4WIPlLyDzFByK78kBSctubP4aRny8q3Av6oQ2Z1EbuoaldhggOiJfoz9QpwKBdVeyFRG2BIqA1kikOtUikpFGVaOnyjx7vTVLMNTCgsMS9pNMWU7u0hMYKYmC9PEuYMCImjMPyZmb0GOqUBTu3zuEHGKTy2pmj1mOpIOGLxuMRH5tWm0GT8sqpC34r7zvaVc2nsInFrO5FAgNKin37bNh8ynMOxM5DH1mxHZmBz2tLND0mn14%2BsRIFDXEY%2F4MaCKxsSo9ARedueTZYz%2BteWkJMOQgYm0Su5QU9PegB%2BMP2EhzJ7LZa500m1MpFUW8aAn4Zy%2FvU%2BpV04yWZr6T6pKX59oTjVKDQbkmnDkTcTsf1n&X-Amz-Signature=1553d38547e1971e3c2466571311d022a9bfb4823fc1191c6dba7241c551ea36&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3BQWDTT%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJIMEYCIQCSmZEx5c%2BOq%2F8%2F8h8Q8URRGv%2BUp83assraKl%2BEJagJtQIhAK%2FOWumGUVNOmjNk4jL2bBANZhF%2FxxX6NNM0Jxh148rmKv8DCHsQABoMNjM3NDIzMTgzODA1IgwnAJlmxGG2YbGXuDIq3ANbbiAhHA8XHr3V7SEM2GQlRJMQs67pD0Wc3kjZmM9iiJtj7syodzQL0AuFgnHsqJem1X0RKZ6DBOd4TLix9TjWk9C%2B0wUwpXgpZI6otMfqzU90TrJ%2BsbGcIAuD62zkHNXUPQH%2FRd3rIyOZECLrGwjHrQK1F80%2FNcJ7sSBY5mCUU13IINQfZlbTtLNNw9%2FhFkU5ju2jcbnjbDXtcqUzxzfYd1mpmH4%2F8o%2B8bTT6HoVr%2BUBmrX8mscJkKUyUJ49UAZfJ2UfZ6BxUolDMtZ5MJCnjJT7JYDSFKglm1BNhaRYBkOc3MdFBzz6E9QFzTzzVlc5qJX8Gbzrk5pDz2bOPWUQnIUT0PDkZBkUXjHRP9BvMRKp97Wdd7q0b2c5%2Fz9MsiO0ua7T8ER7ogmsVSK52UZy%2BDGh6lII%2Bu45%2B5gNG%2BFjHsbXAZD%2FHU5PPvl0soP68m%2F54amfQDDKL5YVsxrXBzfZolCfrc6%2BPGErhvZ1X6sPurfn0QEOPd%2FjjfAkwcnSTyvAdQ0rjlw4AEP22t2eGnwn0CnD0QzaHZVozz0%2FBhigax%2BWvkWRhpdyN3btVhVGj%2FWx9hglJfUZWf7qiwPbxCiQEhLd%2Fu6ITYqNJ3a2jRwY7MQg3SBgCkg4Dotw%2BuDDAmZm9BjqkAS083kgR0UidG4Xric85th0Pn9OVMdrZ8ctUfMoTpqAuZwlaNYauvkhtq0%2BjMqncTN7eZdvMAmjvR6cuta3NtRORxUVG5av87E83AdVUaWPEHUmWthh1HxZgsNLtK3ZdfKNAumHMejb%2BsITf59x1qjZRrbA2HLFDNkY9xCWkHaIkZv8cCYIulfVj2nYxGkuFXpcaZsCIC5quDUjbnbeLtuhMzN%2BF&X-Amz-Signature=002a01fbbb01ab2f37a1bfe3e86ba1e4ab2cde34a7a7dfa8f6282647929764c6&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3BQWDTT%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJIMEYCIQCSmZEx5c%2BOq%2F8%2F8h8Q8URRGv%2BUp83assraKl%2BEJagJtQIhAK%2FOWumGUVNOmjNk4jL2bBANZhF%2FxxX6NNM0Jxh148rmKv8DCHsQABoMNjM3NDIzMTgzODA1IgwnAJlmxGG2YbGXuDIq3ANbbiAhHA8XHr3V7SEM2GQlRJMQs67pD0Wc3kjZmM9iiJtj7syodzQL0AuFgnHsqJem1X0RKZ6DBOd4TLix9TjWk9C%2B0wUwpXgpZI6otMfqzU90TrJ%2BsbGcIAuD62zkHNXUPQH%2FRd3rIyOZECLrGwjHrQK1F80%2FNcJ7sSBY5mCUU13IINQfZlbTtLNNw9%2FhFkU5ju2jcbnjbDXtcqUzxzfYd1mpmH4%2F8o%2B8bTT6HoVr%2BUBmrX8mscJkKUyUJ49UAZfJ2UfZ6BxUolDMtZ5MJCnjJT7JYDSFKglm1BNhaRYBkOc3MdFBzz6E9QFzTzzVlc5qJX8Gbzrk5pDz2bOPWUQnIUT0PDkZBkUXjHRP9BvMRKp97Wdd7q0b2c5%2Fz9MsiO0ua7T8ER7ogmsVSK52UZy%2BDGh6lII%2Bu45%2B5gNG%2BFjHsbXAZD%2FHU5PPvl0soP68m%2F54amfQDDKL5YVsxrXBzfZolCfrc6%2BPGErhvZ1X6sPurfn0QEOPd%2FjjfAkwcnSTyvAdQ0rjlw4AEP22t2eGnwn0CnD0QzaHZVozz0%2FBhigax%2BWvkWRhpdyN3btVhVGj%2FWx9hglJfUZWf7qiwPbxCiQEhLd%2Fu6ITYqNJ3a2jRwY7MQg3SBgCkg4Dotw%2BuDDAmZm9BjqkAS083kgR0UidG4Xric85th0Pn9OVMdrZ8ctUfMoTpqAuZwlaNYauvkhtq0%2BjMqncTN7eZdvMAmjvR6cuta3NtRORxUVG5av87E83AdVUaWPEHUmWthh1HxZgsNLtK3ZdfKNAumHMejb%2BsITf59x1qjZRrbA2HLFDNkY9xCWkHaIkZv8cCYIulfVj2nYxGkuFXpcaZsCIC5quDUjbnbeLtuhMzN%2BF&X-Amz-Signature=b423f380e7ef267fd0252426cccdd9875bdb77489d53376ba019bb8ad7cf2689&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3BQWDTT%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJIMEYCIQCSmZEx5c%2BOq%2F8%2F8h8Q8URRGv%2BUp83assraKl%2BEJagJtQIhAK%2FOWumGUVNOmjNk4jL2bBANZhF%2FxxX6NNM0Jxh148rmKv8DCHsQABoMNjM3NDIzMTgzODA1IgwnAJlmxGG2YbGXuDIq3ANbbiAhHA8XHr3V7SEM2GQlRJMQs67pD0Wc3kjZmM9iiJtj7syodzQL0AuFgnHsqJem1X0RKZ6DBOd4TLix9TjWk9C%2B0wUwpXgpZI6otMfqzU90TrJ%2BsbGcIAuD62zkHNXUPQH%2FRd3rIyOZECLrGwjHrQK1F80%2FNcJ7sSBY5mCUU13IINQfZlbTtLNNw9%2FhFkU5ju2jcbnjbDXtcqUzxzfYd1mpmH4%2F8o%2B8bTT6HoVr%2BUBmrX8mscJkKUyUJ49UAZfJ2UfZ6BxUolDMtZ5MJCnjJT7JYDSFKglm1BNhaRYBkOc3MdFBzz6E9QFzTzzVlc5qJX8Gbzrk5pDz2bOPWUQnIUT0PDkZBkUXjHRP9BvMRKp97Wdd7q0b2c5%2Fz9MsiO0ua7T8ER7ogmsVSK52UZy%2BDGh6lII%2Bu45%2B5gNG%2BFjHsbXAZD%2FHU5PPvl0soP68m%2F54amfQDDKL5YVsxrXBzfZolCfrc6%2BPGErhvZ1X6sPurfn0QEOPd%2FjjfAkwcnSTyvAdQ0rjlw4AEP22t2eGnwn0CnD0QzaHZVozz0%2FBhigax%2BWvkWRhpdyN3btVhVGj%2FWx9hglJfUZWf7qiwPbxCiQEhLd%2Fu6ITYqNJ3a2jRwY7MQg3SBgCkg4Dotw%2BuDDAmZm9BjqkAS083kgR0UidG4Xric85th0Pn9OVMdrZ8ctUfMoTpqAuZwlaNYauvkhtq0%2BjMqncTN7eZdvMAmjvR6cuta3NtRORxUVG5av87E83AdVUaWPEHUmWthh1HxZgsNLtK3ZdfKNAumHMejb%2BsITf59x1qjZRrbA2HLFDNkY9xCWkHaIkZv8cCYIulfVj2nYxGkuFXpcaZsCIC5quDUjbnbeLtuhMzN%2BF&X-Amz-Signature=1376d4ed92ef77e8d802b1e182d76111f3d24e969b6f875a2af439a73c7487ff&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3BQWDTT%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJIMEYCIQCSmZEx5c%2BOq%2F8%2F8h8Q8URRGv%2BUp83assraKl%2BEJagJtQIhAK%2FOWumGUVNOmjNk4jL2bBANZhF%2FxxX6NNM0Jxh148rmKv8DCHsQABoMNjM3NDIzMTgzODA1IgwnAJlmxGG2YbGXuDIq3ANbbiAhHA8XHr3V7SEM2GQlRJMQs67pD0Wc3kjZmM9iiJtj7syodzQL0AuFgnHsqJem1X0RKZ6DBOd4TLix9TjWk9C%2B0wUwpXgpZI6otMfqzU90TrJ%2BsbGcIAuD62zkHNXUPQH%2FRd3rIyOZECLrGwjHrQK1F80%2FNcJ7sSBY5mCUU13IINQfZlbTtLNNw9%2FhFkU5ju2jcbnjbDXtcqUzxzfYd1mpmH4%2F8o%2B8bTT6HoVr%2BUBmrX8mscJkKUyUJ49UAZfJ2UfZ6BxUolDMtZ5MJCnjJT7JYDSFKglm1BNhaRYBkOc3MdFBzz6E9QFzTzzVlc5qJX8Gbzrk5pDz2bOPWUQnIUT0PDkZBkUXjHRP9BvMRKp97Wdd7q0b2c5%2Fz9MsiO0ua7T8ER7ogmsVSK52UZy%2BDGh6lII%2Bu45%2B5gNG%2BFjHsbXAZD%2FHU5PPvl0soP68m%2F54amfQDDKL5YVsxrXBzfZolCfrc6%2BPGErhvZ1X6sPurfn0QEOPd%2FjjfAkwcnSTyvAdQ0rjlw4AEP22t2eGnwn0CnD0QzaHZVozz0%2FBhigax%2BWvkWRhpdyN3btVhVGj%2FWx9hglJfUZWf7qiwPbxCiQEhLd%2Fu6ITYqNJ3a2jRwY7MQg3SBgCkg4Dotw%2BuDDAmZm9BjqkAS083kgR0UidG4Xric85th0Pn9OVMdrZ8ctUfMoTpqAuZwlaNYauvkhtq0%2BjMqncTN7eZdvMAmjvR6cuta3NtRORxUVG5av87E83AdVUaWPEHUmWthh1HxZgsNLtK3ZdfKNAumHMejb%2BsITf59x1qjZRrbA2HLFDNkY9xCWkHaIkZv8cCYIulfVj2nYxGkuFXpcaZsCIC5quDUjbnbeLtuhMzN%2BF&X-Amz-Signature=56123d182c5691e68db96ebbb8119b02afaf2312ffb0f3a4f09e474a1b72e7c7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3BQWDTT%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJIMEYCIQCSmZEx5c%2BOq%2F8%2F8h8Q8URRGv%2BUp83assraKl%2BEJagJtQIhAK%2FOWumGUVNOmjNk4jL2bBANZhF%2FxxX6NNM0Jxh148rmKv8DCHsQABoMNjM3NDIzMTgzODA1IgwnAJlmxGG2YbGXuDIq3ANbbiAhHA8XHr3V7SEM2GQlRJMQs67pD0Wc3kjZmM9iiJtj7syodzQL0AuFgnHsqJem1X0RKZ6DBOd4TLix9TjWk9C%2B0wUwpXgpZI6otMfqzU90TrJ%2BsbGcIAuD62zkHNXUPQH%2FRd3rIyOZECLrGwjHrQK1F80%2FNcJ7sSBY5mCUU13IINQfZlbTtLNNw9%2FhFkU5ju2jcbnjbDXtcqUzxzfYd1mpmH4%2F8o%2B8bTT6HoVr%2BUBmrX8mscJkKUyUJ49UAZfJ2UfZ6BxUolDMtZ5MJCnjJT7JYDSFKglm1BNhaRYBkOc3MdFBzz6E9QFzTzzVlc5qJX8Gbzrk5pDz2bOPWUQnIUT0PDkZBkUXjHRP9BvMRKp97Wdd7q0b2c5%2Fz9MsiO0ua7T8ER7ogmsVSK52UZy%2BDGh6lII%2Bu45%2B5gNG%2BFjHsbXAZD%2FHU5PPvl0soP68m%2F54amfQDDKL5YVsxrXBzfZolCfrc6%2BPGErhvZ1X6sPurfn0QEOPd%2FjjfAkwcnSTyvAdQ0rjlw4AEP22t2eGnwn0CnD0QzaHZVozz0%2FBhigax%2BWvkWRhpdyN3btVhVGj%2FWx9hglJfUZWf7qiwPbxCiQEhLd%2Fu6ITYqNJ3a2jRwY7MQg3SBgCkg4Dotw%2BuDDAmZm9BjqkAS083kgR0UidG4Xric85th0Pn9OVMdrZ8ctUfMoTpqAuZwlaNYauvkhtq0%2BjMqncTN7eZdvMAmjvR6cuta3NtRORxUVG5av87E83AdVUaWPEHUmWthh1HxZgsNLtK3ZdfKNAumHMejb%2BsITf59x1qjZRrbA2HLFDNkY9xCWkHaIkZv8cCYIulfVj2nYxGkuFXpcaZsCIC5quDUjbnbeLtuhMzN%2BF&X-Amz-Signature=3426b3f2315acb84784af633247516bfc7fa7787eadb60b05761d596a868e745&X-Amz-SignedHeaders=host&x-id=GetObject)
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


