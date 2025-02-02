

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5B2KLKH%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T131459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFsFW2yb4Chc%2BwnDrnvM5Zy6HrLCUu5GEW3xAcGwBMl%2FAiB1RoKSGla3xdmYNxlMqFBl40ogLtABiAM8pz479LTCNiqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMq6iwowGK2S2jmvz%2BKtwDR4aLDRBIJo0ZAxkg4ppVqMbFZCUuBEC4uloj%2BGz0YoTjLDHgRqMlzozsCJaS%2ByQw4qFNokmmR1OMMxpzJ22UMR3R8H5qh2peDOvhvhcv4AXjCSPTFt3Zr1XeBRO%2FI8UrI96zFpS7roYoiiy0j%2FqQ2B7Nf1zO0qiLDYiRVou4FJ5iyGwQTxq%2BedLBNK2gtOx0axLijQzkw9UhcdyY86yhzNqNdA6z9xWMsIaOmSeeGGt0ROEh8Uy1AJFlvx2AuGBHpxeThSQwDYHKdbjExmGJ%2F5LArkwPpomY%2FgI8ZyN7vqEnKCud6ZClMvwvUxADxZ1KdxTKtfN6x1jNQQ%2B0sEYEjjdt5Dryfz1Q2BVBi1GchQR5mA7shdSNxbV20z4YwWgkQWvHqjoC6bINM9jw0e8%2BebLYWT9UHVkms2rTxafqbYGtEly2eQJen7A847a6OHDjeURnb%2FdNNOo5%2FKUffah9gts4nFRhG9gxQgHbmQf5CTvF1TR0qsbSfrap9zaX9KxoFYutqOD0lAWvy85XOfdc%2B8zjBmfugQr0oSa7oZqzXwaRJ%2BUXLphfI0rerbOTtAE3T4ufrKbulWSj0PIwqDrLu0Zxv%2F6SZDCQfDWd8kFfiOvNVHJK4BW1xQE%2FmTcwucH9vAY6pgEauQnSk35kzjdDd2nsBvt4gZfPrlN9rOrQGMR9k%2B46J16jOa9%2Be4YBF7K3R8ev5uLpjzPe0cfM6AVNDcSt2Uji1TcQDtbSwvB3zFlqTO%2B63kOpCN%2FC6oCIhyYh2t%2FjhaquCOowP2P1qT14ouFaXU1iwq8TzmcFQdZxoQOhO8a9d%2BGS5LVxYJRtUht9cDsR1tgKAjzsAuFnpXqiF3Bv9AsPj7z9A2OV&X-Amz-Signature=b3944889f3da6620a2a6dbeaa65f46e460248a7fe1ffe3c4b1fbf957b4b05920&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666FG6GVA4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T131500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFEDTQM12EBPLY%2B2R0a4eNqBh0InwUqgZOFjh9r%2F1N8LAiEAhDvADicuZexACYB7panf9w8qLy%2BMeiUPxSJC4cCcM1MqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG7g5FFbFd17pFZLnCrcA3zW3%2BktXinbOfQSXU1j%2FFuDZWmaLHeyJIuSLVpCmpN5ofIdBnXK2m4Y7sBr8PeRfYuoLPgQDh3%2FEzEkftVpJRy%2F2IjyI4lkT8ZTRV3OH4%2FI9JutYAYBG7mRtAEJ4j3%2FLqRoCiM5fS3hu9cCtTlb%2BM3QD0bYleIPOvCG3dzXX4zgsuLHm%2F9yVFiKk0%2BbMZyBRC8MJ0MKA9b03cUq757Xb4MBXfulDE0NgJKTHhaODyDsoIUept4QiJkgcAyZHBjJ99n4YWgfIdUgK2gYngndCbEh1Be9rBbu2%2Bmd9cjfP7wHnF2UanrgyWqmq3Q7p6iAWYAJEH%2FKrDL7xluLB6iuRY6WoWKMrOeRZtxvSALX%2FEORF35QgYnmpLm6g7cSRhq7sMgMsJVEAq8h%2Fks2q6ddIO4T13IhvkSfa6EJSM56iSiDppAb0ekqkl8daFVMC3lwrukk3o9OVCOd%2FR9e%2FE7JsseGUN%2Funip79DhPF9Uu3OefELodvRmknLMdIToTXXVPTidnZEFLtHhx0iPxJ5EJ7RMd2mmE62m%2BTM6mCPajJFCT9jJ2HDWUYVfU9cTsCKnh8tCPnW7w0A6Gtct2qE7jhD85DRSovCuiTUvKQx%2Fp3ZU53RYLRuEx%2FnXqY92AMP%2B%2F%2FbwGOqUBSfb9gXpm%2FdymYZPQEsg2%2F%2Bw5jTWLvzVjc2WnAbx6wleejWH0YM%2BrQMmbZQ8vF32RQjQ0V9XPZ2Aho7vTkCDL5ChX9NsyR0Ri3OThMbQcnwWzlk6YAOqp%2B2ih%2BoqHzz%2FzYB7Iku9kX98axy3FYncYAtx0c0QEWD1YCUQby0XcUx%2BMruoVogWox1KrUQfFP4bH0Dt4zGTksDl8L6A3W4SG2m3dxxH6&X-Amz-Signature=fc8e99a74545aff9e4e7ad0498a256dfdae3c9731e0b0c7e8988fc59757633dc&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666FG6GVA4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T131500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFEDTQM12EBPLY%2B2R0a4eNqBh0InwUqgZOFjh9r%2F1N8LAiEAhDvADicuZexACYB7panf9w8qLy%2BMeiUPxSJC4cCcM1MqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG7g5FFbFd17pFZLnCrcA3zW3%2BktXinbOfQSXU1j%2FFuDZWmaLHeyJIuSLVpCmpN5ofIdBnXK2m4Y7sBr8PeRfYuoLPgQDh3%2FEzEkftVpJRy%2F2IjyI4lkT8ZTRV3OH4%2FI9JutYAYBG7mRtAEJ4j3%2FLqRoCiM5fS3hu9cCtTlb%2BM3QD0bYleIPOvCG3dzXX4zgsuLHm%2F9yVFiKk0%2BbMZyBRC8MJ0MKA9b03cUq757Xb4MBXfulDE0NgJKTHhaODyDsoIUept4QiJkgcAyZHBjJ99n4YWgfIdUgK2gYngndCbEh1Be9rBbu2%2Bmd9cjfP7wHnF2UanrgyWqmq3Q7p6iAWYAJEH%2FKrDL7xluLB6iuRY6WoWKMrOeRZtxvSALX%2FEORF35QgYnmpLm6g7cSRhq7sMgMsJVEAq8h%2Fks2q6ddIO4T13IhvkSfa6EJSM56iSiDppAb0ekqkl8daFVMC3lwrukk3o9OVCOd%2FR9e%2FE7JsseGUN%2Funip79DhPF9Uu3OefELodvRmknLMdIToTXXVPTidnZEFLtHhx0iPxJ5EJ7RMd2mmE62m%2BTM6mCPajJFCT9jJ2HDWUYVfU9cTsCKnh8tCPnW7w0A6Gtct2qE7jhD85DRSovCuiTUvKQx%2Fp3ZU53RYLRuEx%2FnXqY92AMP%2B%2F%2FbwGOqUBSfb9gXpm%2FdymYZPQEsg2%2F%2Bw5jTWLvzVjc2WnAbx6wleejWH0YM%2BrQMmbZQ8vF32RQjQ0V9XPZ2Aho7vTkCDL5ChX9NsyR0Ri3OThMbQcnwWzlk6YAOqp%2B2ih%2BoqHzz%2FzYB7Iku9kX98axy3FYncYAtx0c0QEWD1YCUQby0XcUx%2BMruoVogWox1KrUQfFP4bH0Dt4zGTksDl8L6A3W4SG2m3dxxH6&X-Amz-Signature=a7da4267c4be5359fea89dd4da86e1676f80af3acd9067bdafcba167a38374ca&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666FG6GVA4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T131500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFEDTQM12EBPLY%2B2R0a4eNqBh0InwUqgZOFjh9r%2F1N8LAiEAhDvADicuZexACYB7panf9w8qLy%2BMeiUPxSJC4cCcM1MqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG7g5FFbFd17pFZLnCrcA3zW3%2BktXinbOfQSXU1j%2FFuDZWmaLHeyJIuSLVpCmpN5ofIdBnXK2m4Y7sBr8PeRfYuoLPgQDh3%2FEzEkftVpJRy%2F2IjyI4lkT8ZTRV3OH4%2FI9JutYAYBG7mRtAEJ4j3%2FLqRoCiM5fS3hu9cCtTlb%2BM3QD0bYleIPOvCG3dzXX4zgsuLHm%2F9yVFiKk0%2BbMZyBRC8MJ0MKA9b03cUq757Xb4MBXfulDE0NgJKTHhaODyDsoIUept4QiJkgcAyZHBjJ99n4YWgfIdUgK2gYngndCbEh1Be9rBbu2%2Bmd9cjfP7wHnF2UanrgyWqmq3Q7p6iAWYAJEH%2FKrDL7xluLB6iuRY6WoWKMrOeRZtxvSALX%2FEORF35QgYnmpLm6g7cSRhq7sMgMsJVEAq8h%2Fks2q6ddIO4T13IhvkSfa6EJSM56iSiDppAb0ekqkl8daFVMC3lwrukk3o9OVCOd%2FR9e%2FE7JsseGUN%2Funip79DhPF9Uu3OefELodvRmknLMdIToTXXVPTidnZEFLtHhx0iPxJ5EJ7RMd2mmE62m%2BTM6mCPajJFCT9jJ2HDWUYVfU9cTsCKnh8tCPnW7w0A6Gtct2qE7jhD85DRSovCuiTUvKQx%2Fp3ZU53RYLRuEx%2FnXqY92AMP%2B%2F%2FbwGOqUBSfb9gXpm%2FdymYZPQEsg2%2F%2Bw5jTWLvzVjc2WnAbx6wleejWH0YM%2BrQMmbZQ8vF32RQjQ0V9XPZ2Aho7vTkCDL5ChX9NsyR0Ri3OThMbQcnwWzlk6YAOqp%2B2ih%2BoqHzz%2FzYB7Iku9kX98axy3FYncYAtx0c0QEWD1YCUQby0XcUx%2BMruoVogWox1KrUQfFP4bH0Dt4zGTksDl8L6A3W4SG2m3dxxH6&X-Amz-Signature=b1b5f130cb8dc804190ff2a8435cbf77cf47c1346e94c8e7477c88fc2e1e05bf&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666FG6GVA4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T131500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFEDTQM12EBPLY%2B2R0a4eNqBh0InwUqgZOFjh9r%2F1N8LAiEAhDvADicuZexACYB7panf9w8qLy%2BMeiUPxSJC4cCcM1MqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG7g5FFbFd17pFZLnCrcA3zW3%2BktXinbOfQSXU1j%2FFuDZWmaLHeyJIuSLVpCmpN5ofIdBnXK2m4Y7sBr8PeRfYuoLPgQDh3%2FEzEkftVpJRy%2F2IjyI4lkT8ZTRV3OH4%2FI9JutYAYBG7mRtAEJ4j3%2FLqRoCiM5fS3hu9cCtTlb%2BM3QD0bYleIPOvCG3dzXX4zgsuLHm%2F9yVFiKk0%2BbMZyBRC8MJ0MKA9b03cUq757Xb4MBXfulDE0NgJKTHhaODyDsoIUept4QiJkgcAyZHBjJ99n4YWgfIdUgK2gYngndCbEh1Be9rBbu2%2Bmd9cjfP7wHnF2UanrgyWqmq3Q7p6iAWYAJEH%2FKrDL7xluLB6iuRY6WoWKMrOeRZtxvSALX%2FEORF35QgYnmpLm6g7cSRhq7sMgMsJVEAq8h%2Fks2q6ddIO4T13IhvkSfa6EJSM56iSiDppAb0ekqkl8daFVMC3lwrukk3o9OVCOd%2FR9e%2FE7JsseGUN%2Funip79DhPF9Uu3OefELodvRmknLMdIToTXXVPTidnZEFLtHhx0iPxJ5EJ7RMd2mmE62m%2BTM6mCPajJFCT9jJ2HDWUYVfU9cTsCKnh8tCPnW7w0A6Gtct2qE7jhD85DRSovCuiTUvKQx%2Fp3ZU53RYLRuEx%2FnXqY92AMP%2B%2F%2FbwGOqUBSfb9gXpm%2FdymYZPQEsg2%2F%2Bw5jTWLvzVjc2WnAbx6wleejWH0YM%2BrQMmbZQ8vF32RQjQ0V9XPZ2Aho7vTkCDL5ChX9NsyR0Ri3OThMbQcnwWzlk6YAOqp%2B2ih%2BoqHzz%2FzYB7Iku9kX98axy3FYncYAtx0c0QEWD1YCUQby0XcUx%2BMruoVogWox1KrUQfFP4bH0Dt4zGTksDl8L6A3W4SG2m3dxxH6&X-Amz-Signature=c4a55b41c2e3c7248a629b70b060950362b6781d29c279b004768e6632365d4f&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666FG6GVA4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T131500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFEDTQM12EBPLY%2B2R0a4eNqBh0InwUqgZOFjh9r%2F1N8LAiEAhDvADicuZexACYB7panf9w8qLy%2BMeiUPxSJC4cCcM1MqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG7g5FFbFd17pFZLnCrcA3zW3%2BktXinbOfQSXU1j%2FFuDZWmaLHeyJIuSLVpCmpN5ofIdBnXK2m4Y7sBr8PeRfYuoLPgQDh3%2FEzEkftVpJRy%2F2IjyI4lkT8ZTRV3OH4%2FI9JutYAYBG7mRtAEJ4j3%2FLqRoCiM5fS3hu9cCtTlb%2BM3QD0bYleIPOvCG3dzXX4zgsuLHm%2F9yVFiKk0%2BbMZyBRC8MJ0MKA9b03cUq757Xb4MBXfulDE0NgJKTHhaODyDsoIUept4QiJkgcAyZHBjJ99n4YWgfIdUgK2gYngndCbEh1Be9rBbu2%2Bmd9cjfP7wHnF2UanrgyWqmq3Q7p6iAWYAJEH%2FKrDL7xluLB6iuRY6WoWKMrOeRZtxvSALX%2FEORF35QgYnmpLm6g7cSRhq7sMgMsJVEAq8h%2Fks2q6ddIO4T13IhvkSfa6EJSM56iSiDppAb0ekqkl8daFVMC3lwrukk3o9OVCOd%2FR9e%2FE7JsseGUN%2Funip79DhPF9Uu3OefELodvRmknLMdIToTXXVPTidnZEFLtHhx0iPxJ5EJ7RMd2mmE62m%2BTM6mCPajJFCT9jJ2HDWUYVfU9cTsCKnh8tCPnW7w0A6Gtct2qE7jhD85DRSovCuiTUvKQx%2Fp3ZU53RYLRuEx%2FnXqY92AMP%2B%2F%2FbwGOqUBSfb9gXpm%2FdymYZPQEsg2%2F%2Bw5jTWLvzVjc2WnAbx6wleejWH0YM%2BrQMmbZQ8vF32RQjQ0V9XPZ2Aho7vTkCDL5ChX9NsyR0Ri3OThMbQcnwWzlk6YAOqp%2B2ih%2BoqHzz%2FzYB7Iku9kX98axy3FYncYAtx0c0QEWD1YCUQby0XcUx%2BMruoVogWox1KrUQfFP4bH0Dt4zGTksDl8L6A3W4SG2m3dxxH6&X-Amz-Signature=8342c23d39449261765a5d9e5ce396bf589b3bc5cae2bba8c071b4b9631095ba&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5B2KLKH%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T131459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFsFW2yb4Chc%2BwnDrnvM5Zy6HrLCUu5GEW3xAcGwBMl%2FAiB1RoKSGla3xdmYNxlMqFBl40ogLtABiAM8pz479LTCNiqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMq6iwowGK2S2jmvz%2BKtwDR4aLDRBIJo0ZAxkg4ppVqMbFZCUuBEC4uloj%2BGz0YoTjLDHgRqMlzozsCJaS%2ByQw4qFNokmmR1OMMxpzJ22UMR3R8H5qh2peDOvhvhcv4AXjCSPTFt3Zr1XeBRO%2FI8UrI96zFpS7roYoiiy0j%2FqQ2B7Nf1zO0qiLDYiRVou4FJ5iyGwQTxq%2BedLBNK2gtOx0axLijQzkw9UhcdyY86yhzNqNdA6z9xWMsIaOmSeeGGt0ROEh8Uy1AJFlvx2AuGBHpxeThSQwDYHKdbjExmGJ%2F5LArkwPpomY%2FgI8ZyN7vqEnKCud6ZClMvwvUxADxZ1KdxTKtfN6x1jNQQ%2B0sEYEjjdt5Dryfz1Q2BVBi1GchQR5mA7shdSNxbV20z4YwWgkQWvHqjoC6bINM9jw0e8%2BebLYWT9UHVkms2rTxafqbYGtEly2eQJen7A847a6OHDjeURnb%2FdNNOo5%2FKUffah9gts4nFRhG9gxQgHbmQf5CTvF1TR0qsbSfrap9zaX9KxoFYutqOD0lAWvy85XOfdc%2B8zjBmfugQr0oSa7oZqzXwaRJ%2BUXLphfI0rerbOTtAE3T4ufrKbulWSj0PIwqDrLu0Zxv%2F6SZDCQfDWd8kFfiOvNVHJK4BW1xQE%2FmTcwucH9vAY6pgEauQnSk35kzjdDd2nsBvt4gZfPrlN9rOrQGMR9k%2B46J16jOa9%2Be4YBF7K3R8ev5uLpjzPe0cfM6AVNDcSt2Uji1TcQDtbSwvB3zFlqTO%2B63kOpCN%2FC6oCIhyYh2t%2FjhaquCOowP2P1qT14ouFaXU1iwq8TzmcFQdZxoQOhO8a9d%2BGS5LVxYJRtUht9cDsR1tgKAjzsAuFnpXqiF3Bv9AsPj7z9A2OV&X-Amz-Signature=3fa90cc5c9fde3a2b3dc231c54c44fed50ea0384aab23552f93eabc3d202ad1f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5B2KLKH%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T131459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFsFW2yb4Chc%2BwnDrnvM5Zy6HrLCUu5GEW3xAcGwBMl%2FAiB1RoKSGla3xdmYNxlMqFBl40ogLtABiAM8pz479LTCNiqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMq6iwowGK2S2jmvz%2BKtwDR4aLDRBIJo0ZAxkg4ppVqMbFZCUuBEC4uloj%2BGz0YoTjLDHgRqMlzozsCJaS%2ByQw4qFNokmmR1OMMxpzJ22UMR3R8H5qh2peDOvhvhcv4AXjCSPTFt3Zr1XeBRO%2FI8UrI96zFpS7roYoiiy0j%2FqQ2B7Nf1zO0qiLDYiRVou4FJ5iyGwQTxq%2BedLBNK2gtOx0axLijQzkw9UhcdyY86yhzNqNdA6z9xWMsIaOmSeeGGt0ROEh8Uy1AJFlvx2AuGBHpxeThSQwDYHKdbjExmGJ%2F5LArkwPpomY%2FgI8ZyN7vqEnKCud6ZClMvwvUxADxZ1KdxTKtfN6x1jNQQ%2B0sEYEjjdt5Dryfz1Q2BVBi1GchQR5mA7shdSNxbV20z4YwWgkQWvHqjoC6bINM9jw0e8%2BebLYWT9UHVkms2rTxafqbYGtEly2eQJen7A847a6OHDjeURnb%2FdNNOo5%2FKUffah9gts4nFRhG9gxQgHbmQf5CTvF1TR0qsbSfrap9zaX9KxoFYutqOD0lAWvy85XOfdc%2B8zjBmfugQr0oSa7oZqzXwaRJ%2BUXLphfI0rerbOTtAE3T4ufrKbulWSj0PIwqDrLu0Zxv%2F6SZDCQfDWd8kFfiOvNVHJK4BW1xQE%2FmTcwucH9vAY6pgEauQnSk35kzjdDd2nsBvt4gZfPrlN9rOrQGMR9k%2B46J16jOa9%2Be4YBF7K3R8ev5uLpjzPe0cfM6AVNDcSt2Uji1TcQDtbSwvB3zFlqTO%2B63kOpCN%2FC6oCIhyYh2t%2FjhaquCOowP2P1qT14ouFaXU1iwq8TzmcFQdZxoQOhO8a9d%2BGS5LVxYJRtUht9cDsR1tgKAjzsAuFnpXqiF3Bv9AsPj7z9A2OV&X-Amz-Signature=0044f4b95e0e9f32f52fb55f0593c3387c2a4bd25027d9688bacc99362a7d9d4&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5B2KLKH%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T131459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFsFW2yb4Chc%2BwnDrnvM5Zy6HrLCUu5GEW3xAcGwBMl%2FAiB1RoKSGla3xdmYNxlMqFBl40ogLtABiAM8pz479LTCNiqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMq6iwowGK2S2jmvz%2BKtwDR4aLDRBIJo0ZAxkg4ppVqMbFZCUuBEC4uloj%2BGz0YoTjLDHgRqMlzozsCJaS%2ByQw4qFNokmmR1OMMxpzJ22UMR3R8H5qh2peDOvhvhcv4AXjCSPTFt3Zr1XeBRO%2FI8UrI96zFpS7roYoiiy0j%2FqQ2B7Nf1zO0qiLDYiRVou4FJ5iyGwQTxq%2BedLBNK2gtOx0axLijQzkw9UhcdyY86yhzNqNdA6z9xWMsIaOmSeeGGt0ROEh8Uy1AJFlvx2AuGBHpxeThSQwDYHKdbjExmGJ%2F5LArkwPpomY%2FgI8ZyN7vqEnKCud6ZClMvwvUxADxZ1KdxTKtfN6x1jNQQ%2B0sEYEjjdt5Dryfz1Q2BVBi1GchQR5mA7shdSNxbV20z4YwWgkQWvHqjoC6bINM9jw0e8%2BebLYWT9UHVkms2rTxafqbYGtEly2eQJen7A847a6OHDjeURnb%2FdNNOo5%2FKUffah9gts4nFRhG9gxQgHbmQf5CTvF1TR0qsbSfrap9zaX9KxoFYutqOD0lAWvy85XOfdc%2B8zjBmfugQr0oSa7oZqzXwaRJ%2BUXLphfI0rerbOTtAE3T4ufrKbulWSj0PIwqDrLu0Zxv%2F6SZDCQfDWd8kFfiOvNVHJK4BW1xQE%2FmTcwucH9vAY6pgEauQnSk35kzjdDd2nsBvt4gZfPrlN9rOrQGMR9k%2B46J16jOa9%2Be4YBF7K3R8ev5uLpjzPe0cfM6AVNDcSt2Uji1TcQDtbSwvB3zFlqTO%2B63kOpCN%2FC6oCIhyYh2t%2FjhaquCOowP2P1qT14ouFaXU1iwq8TzmcFQdZxoQOhO8a9d%2BGS5LVxYJRtUht9cDsR1tgKAjzsAuFnpXqiF3Bv9AsPj7z9A2OV&X-Amz-Signature=5288f30b406a0b0dd0b7a595b99931657461e4a2c9d2526f793475b97cefb7c6&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5B2KLKH%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T131459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFsFW2yb4Chc%2BwnDrnvM5Zy6HrLCUu5GEW3xAcGwBMl%2FAiB1RoKSGla3xdmYNxlMqFBl40ogLtABiAM8pz479LTCNiqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMq6iwowGK2S2jmvz%2BKtwDR4aLDRBIJo0ZAxkg4ppVqMbFZCUuBEC4uloj%2BGz0YoTjLDHgRqMlzozsCJaS%2ByQw4qFNokmmR1OMMxpzJ22UMR3R8H5qh2peDOvhvhcv4AXjCSPTFt3Zr1XeBRO%2FI8UrI96zFpS7roYoiiy0j%2FqQ2B7Nf1zO0qiLDYiRVou4FJ5iyGwQTxq%2BedLBNK2gtOx0axLijQzkw9UhcdyY86yhzNqNdA6z9xWMsIaOmSeeGGt0ROEh8Uy1AJFlvx2AuGBHpxeThSQwDYHKdbjExmGJ%2F5LArkwPpomY%2FgI8ZyN7vqEnKCud6ZClMvwvUxADxZ1KdxTKtfN6x1jNQQ%2B0sEYEjjdt5Dryfz1Q2BVBi1GchQR5mA7shdSNxbV20z4YwWgkQWvHqjoC6bINM9jw0e8%2BebLYWT9UHVkms2rTxafqbYGtEly2eQJen7A847a6OHDjeURnb%2FdNNOo5%2FKUffah9gts4nFRhG9gxQgHbmQf5CTvF1TR0qsbSfrap9zaX9KxoFYutqOD0lAWvy85XOfdc%2B8zjBmfugQr0oSa7oZqzXwaRJ%2BUXLphfI0rerbOTtAE3T4ufrKbulWSj0PIwqDrLu0Zxv%2F6SZDCQfDWd8kFfiOvNVHJK4BW1xQE%2FmTcwucH9vAY6pgEauQnSk35kzjdDd2nsBvt4gZfPrlN9rOrQGMR9k%2B46J16jOa9%2Be4YBF7K3R8ev5uLpjzPe0cfM6AVNDcSt2Uji1TcQDtbSwvB3zFlqTO%2B63kOpCN%2FC6oCIhyYh2t%2FjhaquCOowP2P1qT14ouFaXU1iwq8TzmcFQdZxoQOhO8a9d%2BGS5LVxYJRtUht9cDsR1tgKAjzsAuFnpXqiF3Bv9AsPj7z9A2OV&X-Amz-Signature=cb49c9f123b7a839488cfd3ff633e4fd540be1c852292312020debce6699bf1e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5B2KLKH%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T131459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFsFW2yb4Chc%2BwnDrnvM5Zy6HrLCUu5GEW3xAcGwBMl%2FAiB1RoKSGla3xdmYNxlMqFBl40ogLtABiAM8pz479LTCNiqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMq6iwowGK2S2jmvz%2BKtwDR4aLDRBIJo0ZAxkg4ppVqMbFZCUuBEC4uloj%2BGz0YoTjLDHgRqMlzozsCJaS%2ByQw4qFNokmmR1OMMxpzJ22UMR3R8H5qh2peDOvhvhcv4AXjCSPTFt3Zr1XeBRO%2FI8UrI96zFpS7roYoiiy0j%2FqQ2B7Nf1zO0qiLDYiRVou4FJ5iyGwQTxq%2BedLBNK2gtOx0axLijQzkw9UhcdyY86yhzNqNdA6z9xWMsIaOmSeeGGt0ROEh8Uy1AJFlvx2AuGBHpxeThSQwDYHKdbjExmGJ%2F5LArkwPpomY%2FgI8ZyN7vqEnKCud6ZClMvwvUxADxZ1KdxTKtfN6x1jNQQ%2B0sEYEjjdt5Dryfz1Q2BVBi1GchQR5mA7shdSNxbV20z4YwWgkQWvHqjoC6bINM9jw0e8%2BebLYWT9UHVkms2rTxafqbYGtEly2eQJen7A847a6OHDjeURnb%2FdNNOo5%2FKUffah9gts4nFRhG9gxQgHbmQf5CTvF1TR0qsbSfrap9zaX9KxoFYutqOD0lAWvy85XOfdc%2B8zjBmfugQr0oSa7oZqzXwaRJ%2BUXLphfI0rerbOTtAE3T4ufrKbulWSj0PIwqDrLu0Zxv%2F6SZDCQfDWd8kFfiOvNVHJK4BW1xQE%2FmTcwucH9vAY6pgEauQnSk35kzjdDd2nsBvt4gZfPrlN9rOrQGMR9k%2B46J16jOa9%2Be4YBF7K3R8ev5uLpjzPe0cfM6AVNDcSt2Uji1TcQDtbSwvB3zFlqTO%2B63kOpCN%2FC6oCIhyYh2t%2FjhaquCOowP2P1qT14ouFaXU1iwq8TzmcFQdZxoQOhO8a9d%2BGS5LVxYJRtUht9cDsR1tgKAjzsAuFnpXqiF3Bv9AsPj7z9A2OV&X-Amz-Signature=82b9d543698d91e1110a0fba2ca1956fa01060821edb55a279a99a3c32738981&X-Amz-SignedHeaders=host&x-id=GetObject)
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


