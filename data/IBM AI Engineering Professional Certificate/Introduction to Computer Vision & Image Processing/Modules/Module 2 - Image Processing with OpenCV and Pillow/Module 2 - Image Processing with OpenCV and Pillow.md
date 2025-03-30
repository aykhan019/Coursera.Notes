

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KK3IHQQ%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIDasNkqgcyBu8LDfvcJzclwbokGcSr15ieOyuB22%2F7pfAiEAimL5scSDBsvvRQxj0KA1VT%2FK%2BF57SqnBH8GKw2L0tOMqiAQIgP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOlcEfifLOaHv3I4uircA3qvC%2F2wKV2GI76glWn%2BOt%2FMZP6C6DmWElZYA39s%2BZjYNojzYeiIAuiJECiOAGGqFC%2Brnt2%2Bki%2F9rJ7OypFer1QLVcf6rHurJzwRnZoZf5nbuRqTgoDe1HKNcw21MygGqLHaq1feS4zzY9uoHrIo9ayt7%2BIiLty2YklNRXbMhyON1jpAWhSjjkznRDymAtC%2B%2Be1nFgJEe3IODdgxy5nnYg%2BsUQ3OSNk3g%2Fg2lK%2BSQxumgIV7YYjuv%2BGYxzEoSgmxcGlOQj5TRxCBgeY45fn0E2hsprn5r8daO8G4rm64sys%2BOoeY%2FvAdEj51pM%2BsbTuGBV3WZ3ONzEv3nG7%2B%2Bz4u7S1JCZVvr3oFSUP8pmGxnGMvbsMxwfzPtQteH8bWCeiFb%2F9sHIBTkK3d3wF1%2Bleod2x6go98uiycydlOmoX4EZMM%2FlZu8LHBPrbSN4jTH%2BR%2BKl%2FeFDoHDl%2B6Yr5PukmaU33KFxYe%2FsPTYDB8CHRJj1IQoP6f5UQ9f4Nm%2FzBctV8wiIpWNGlf%2FgoPBHnZiB10R9bP8Ob%2BrXVYS5e4urAiVs9J9Cj4BLnaN6c6Q8kLfKk8TLjzn0XXW1vfFPMjNfNxWX1xKQA220lfa9pxeNrKZSMeaOZ2mKcwDaluvZ8IMNP8ob8GOqUBejhKXZvnF9m6srePieU%2B7oRV8mk6A%2FcvFBWyzFm9mNyFFEU4l61UFHkBJaXrBCfi4OwgDBUAlTOdoTJYlGCRKpKnECwm4t5C9vetm192Sn6KiFut12uSYtjsyPBiYkil1yNGUqH4tAP9MI%2F7Jq3Ra7YGGfnOByEMxDAA8uwm0yq4ynSmJRV1QmKr9G13ZfoR%2FfCvxUO5yOtu0M5lnfVYpg0ZKcsc&X-Amz-Signature=7f70875192beb2a5690d12385cdaa127615aafad0b6658c327f801f5226a3498&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTOFPV3Q%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004516Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCIEpiT2qLmz32eELV05lNsSfIBv5jJoJ5myEnhE%2BpkvakAiBsznlNZZ7n4zoZm35kmJE9mjfJhZxtOELVxkWuLKKhqiqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMwzIOMzi%2FpkL5QJNfKtwDTvfKlqVrSrHOC1nRQx2A7t2TehlWMQ4M%2Fb%2BJjHBUUpNJ848mj9oNjHxvrrZaUrJLovpez%2FLFYWaop7Tq7NTszq7tHwJK8%2BkNJBQiM4SQ8xmkXikHh4Fd%2Fp5Nq9TTUwsAV2a1Mo6aI8BO%2Bj5s7HrdLoJ4CMMkmL%2Fwi8qqpPbohF4fwuZm4XVMUnBV8z1GXVzFtUhcHfTALzTUcG252dZnA1rncObqwbqfmoztQRn7tjd5Nu3gnJKvgzQ0WZPnR1wsxbtxyMrV9343V52ODT%2FvvS0%2F7lzr4uq0BGBj7KACPe0BFrVtfcNa%2FTiX0M1pEqaZh%2BvhuCWMzHlKLltfc7yccwj75A3T2oiltGO8m9%2BgYIOTfjSWRecoi7paJLus1%2Fg%2ByYH1viU3O9DrVUPRo3VGHCr6weYH0nBnmH17sTO0b3bacsag9p9HPtdfzzCRpNX4NcAJpO%2F6MRnQnX0K09wSuXwJnBYoK%2BFrOeJ%2BK2kTa3KF9SJll9AFI9JqiXC5n5%2B9GZ0QEYeiuSeDpnDK89fxXDkAFg%2Bu7cV5FS11Q3qK0InfmxJQajPHfmBbZoXP22H%2Blwp67vW5Tr1rYq%2BRsPbVBwI40qoHKOqbkZ1eYy7Z4VgpH4lCEwDVqqaNXl4wmJqivwY6pgH8goiepZWXUmsK%2FaVBM70STtDx5ZFEaGSF7iuEa6Yv0qzQIBHqJnSCy%2FQGtqxOyNAZeEUQh7aLgrw%2FFn1zL8%2BoqhzUgFswOY9sMFzOHq2vtVCIJ5CRMO%2Fhv%2FPtuxqbTYeh%2F3I%2BGNFM8w8iMPQ9wE67k8x7njJDb0ILxCvrCTVvjwQciBJy0F2r1ihN4c7DbKjqU2ncduBgpt5hFRi6%2B7BtN%2BUw5mW3&X-Amz-Signature=ff295082dab8484edade2beea4916f4c1970013dc869158745eb150616e07771&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTOFPV3Q%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004516Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCIEpiT2qLmz32eELV05lNsSfIBv5jJoJ5myEnhE%2BpkvakAiBsznlNZZ7n4zoZm35kmJE9mjfJhZxtOELVxkWuLKKhqiqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMwzIOMzi%2FpkL5QJNfKtwDTvfKlqVrSrHOC1nRQx2A7t2TehlWMQ4M%2Fb%2BJjHBUUpNJ848mj9oNjHxvrrZaUrJLovpez%2FLFYWaop7Tq7NTszq7tHwJK8%2BkNJBQiM4SQ8xmkXikHh4Fd%2Fp5Nq9TTUwsAV2a1Mo6aI8BO%2Bj5s7HrdLoJ4CMMkmL%2Fwi8qqpPbohF4fwuZm4XVMUnBV8z1GXVzFtUhcHfTALzTUcG252dZnA1rncObqwbqfmoztQRn7tjd5Nu3gnJKvgzQ0WZPnR1wsxbtxyMrV9343V52ODT%2FvvS0%2F7lzr4uq0BGBj7KACPe0BFrVtfcNa%2FTiX0M1pEqaZh%2BvhuCWMzHlKLltfc7yccwj75A3T2oiltGO8m9%2BgYIOTfjSWRecoi7paJLus1%2Fg%2ByYH1viU3O9DrVUPRo3VGHCr6weYH0nBnmH17sTO0b3bacsag9p9HPtdfzzCRpNX4NcAJpO%2F6MRnQnX0K09wSuXwJnBYoK%2BFrOeJ%2BK2kTa3KF9SJll9AFI9JqiXC5n5%2B9GZ0QEYeiuSeDpnDK89fxXDkAFg%2Bu7cV5FS11Q3qK0InfmxJQajPHfmBbZoXP22H%2Blwp67vW5Tr1rYq%2BRsPbVBwI40qoHKOqbkZ1eYy7Z4VgpH4lCEwDVqqaNXl4wmJqivwY6pgH8goiepZWXUmsK%2FaVBM70STtDx5ZFEaGSF7iuEa6Yv0qzQIBHqJnSCy%2FQGtqxOyNAZeEUQh7aLgrw%2FFn1zL8%2BoqhzUgFswOY9sMFzOHq2vtVCIJ5CRMO%2Fhv%2FPtuxqbTYeh%2F3I%2BGNFM8w8iMPQ9wE67k8x7njJDb0ILxCvrCTVvjwQciBJy0F2r1ihN4c7DbKjqU2ncduBgpt5hFRi6%2B7BtN%2BUw5mW3&X-Amz-Signature=ca6d65ee97b91dad24a38524df1b37bfd91a5ede30cec57f7793592b1f02af49&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTOFPV3Q%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004516Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCIEpiT2qLmz32eELV05lNsSfIBv5jJoJ5myEnhE%2BpkvakAiBsznlNZZ7n4zoZm35kmJE9mjfJhZxtOELVxkWuLKKhqiqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMwzIOMzi%2FpkL5QJNfKtwDTvfKlqVrSrHOC1nRQx2A7t2TehlWMQ4M%2Fb%2BJjHBUUpNJ848mj9oNjHxvrrZaUrJLovpez%2FLFYWaop7Tq7NTszq7tHwJK8%2BkNJBQiM4SQ8xmkXikHh4Fd%2Fp5Nq9TTUwsAV2a1Mo6aI8BO%2Bj5s7HrdLoJ4CMMkmL%2Fwi8qqpPbohF4fwuZm4XVMUnBV8z1GXVzFtUhcHfTALzTUcG252dZnA1rncObqwbqfmoztQRn7tjd5Nu3gnJKvgzQ0WZPnR1wsxbtxyMrV9343V52ODT%2FvvS0%2F7lzr4uq0BGBj7KACPe0BFrVtfcNa%2FTiX0M1pEqaZh%2BvhuCWMzHlKLltfc7yccwj75A3T2oiltGO8m9%2BgYIOTfjSWRecoi7paJLus1%2Fg%2ByYH1viU3O9DrVUPRo3VGHCr6weYH0nBnmH17sTO0b3bacsag9p9HPtdfzzCRpNX4NcAJpO%2F6MRnQnX0K09wSuXwJnBYoK%2BFrOeJ%2BK2kTa3KF9SJll9AFI9JqiXC5n5%2B9GZ0QEYeiuSeDpnDK89fxXDkAFg%2Bu7cV5FS11Q3qK0InfmxJQajPHfmBbZoXP22H%2Blwp67vW5Tr1rYq%2BRsPbVBwI40qoHKOqbkZ1eYy7Z4VgpH4lCEwDVqqaNXl4wmJqivwY6pgH8goiepZWXUmsK%2FaVBM70STtDx5ZFEaGSF7iuEa6Yv0qzQIBHqJnSCy%2FQGtqxOyNAZeEUQh7aLgrw%2FFn1zL8%2BoqhzUgFswOY9sMFzOHq2vtVCIJ5CRMO%2Fhv%2FPtuxqbTYeh%2F3I%2BGNFM8w8iMPQ9wE67k8x7njJDb0ILxCvrCTVvjwQciBJy0F2r1ihN4c7DbKjqU2ncduBgpt5hFRi6%2B7BtN%2BUw5mW3&X-Amz-Signature=f44476d3f24bd4abad802f5fdf05bad46d02f2c9d3b4cf06d0c2d377cd927f22&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTOFPV3Q%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004516Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCIEpiT2qLmz32eELV05lNsSfIBv5jJoJ5myEnhE%2BpkvakAiBsznlNZZ7n4zoZm35kmJE9mjfJhZxtOELVxkWuLKKhqiqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMwzIOMzi%2FpkL5QJNfKtwDTvfKlqVrSrHOC1nRQx2A7t2TehlWMQ4M%2Fb%2BJjHBUUpNJ848mj9oNjHxvrrZaUrJLovpez%2FLFYWaop7Tq7NTszq7tHwJK8%2BkNJBQiM4SQ8xmkXikHh4Fd%2Fp5Nq9TTUwsAV2a1Mo6aI8BO%2Bj5s7HrdLoJ4CMMkmL%2Fwi8qqpPbohF4fwuZm4XVMUnBV8z1GXVzFtUhcHfTALzTUcG252dZnA1rncObqwbqfmoztQRn7tjd5Nu3gnJKvgzQ0WZPnR1wsxbtxyMrV9343V52ODT%2FvvS0%2F7lzr4uq0BGBj7KACPe0BFrVtfcNa%2FTiX0M1pEqaZh%2BvhuCWMzHlKLltfc7yccwj75A3T2oiltGO8m9%2BgYIOTfjSWRecoi7paJLus1%2Fg%2ByYH1viU3O9DrVUPRo3VGHCr6weYH0nBnmH17sTO0b3bacsag9p9HPtdfzzCRpNX4NcAJpO%2F6MRnQnX0K09wSuXwJnBYoK%2BFrOeJ%2BK2kTa3KF9SJll9AFI9JqiXC5n5%2B9GZ0QEYeiuSeDpnDK89fxXDkAFg%2Bu7cV5FS11Q3qK0InfmxJQajPHfmBbZoXP22H%2Blwp67vW5Tr1rYq%2BRsPbVBwI40qoHKOqbkZ1eYy7Z4VgpH4lCEwDVqqaNXl4wmJqivwY6pgH8goiepZWXUmsK%2FaVBM70STtDx5ZFEaGSF7iuEa6Yv0qzQIBHqJnSCy%2FQGtqxOyNAZeEUQh7aLgrw%2FFn1zL8%2BoqhzUgFswOY9sMFzOHq2vtVCIJ5CRMO%2Fhv%2FPtuxqbTYeh%2F3I%2BGNFM8w8iMPQ9wE67k8x7njJDb0ILxCvrCTVvjwQciBJy0F2r1ihN4c7DbKjqU2ncduBgpt5hFRi6%2B7BtN%2BUw5mW3&X-Amz-Signature=04bcf04aebf83d768dab4ba802b9e22b6827ddadf87582b0cd9698968bbf4585&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTOFPV3Q%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004516Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCIEpiT2qLmz32eELV05lNsSfIBv5jJoJ5myEnhE%2BpkvakAiBsznlNZZ7n4zoZm35kmJE9mjfJhZxtOELVxkWuLKKhqiqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMwzIOMzi%2FpkL5QJNfKtwDTvfKlqVrSrHOC1nRQx2A7t2TehlWMQ4M%2Fb%2BJjHBUUpNJ848mj9oNjHxvrrZaUrJLovpez%2FLFYWaop7Tq7NTszq7tHwJK8%2BkNJBQiM4SQ8xmkXikHh4Fd%2Fp5Nq9TTUwsAV2a1Mo6aI8BO%2Bj5s7HrdLoJ4CMMkmL%2Fwi8qqpPbohF4fwuZm4XVMUnBV8z1GXVzFtUhcHfTALzTUcG252dZnA1rncObqwbqfmoztQRn7tjd5Nu3gnJKvgzQ0WZPnR1wsxbtxyMrV9343V52ODT%2FvvS0%2F7lzr4uq0BGBj7KACPe0BFrVtfcNa%2FTiX0M1pEqaZh%2BvhuCWMzHlKLltfc7yccwj75A3T2oiltGO8m9%2BgYIOTfjSWRecoi7paJLus1%2Fg%2ByYH1viU3O9DrVUPRo3VGHCr6weYH0nBnmH17sTO0b3bacsag9p9HPtdfzzCRpNX4NcAJpO%2F6MRnQnX0K09wSuXwJnBYoK%2BFrOeJ%2BK2kTa3KF9SJll9AFI9JqiXC5n5%2B9GZ0QEYeiuSeDpnDK89fxXDkAFg%2Bu7cV5FS11Q3qK0InfmxJQajPHfmBbZoXP22H%2Blwp67vW5Tr1rYq%2BRsPbVBwI40qoHKOqbkZ1eYy7Z4VgpH4lCEwDVqqaNXl4wmJqivwY6pgH8goiepZWXUmsK%2FaVBM70STtDx5ZFEaGSF7iuEa6Yv0qzQIBHqJnSCy%2FQGtqxOyNAZeEUQh7aLgrw%2FFn1zL8%2BoqhzUgFswOY9sMFzOHq2vtVCIJ5CRMO%2Fhv%2FPtuxqbTYeh%2F3I%2BGNFM8w8iMPQ9wE67k8x7njJDb0ILxCvrCTVvjwQciBJy0F2r1ihN4c7DbKjqU2ncduBgpt5hFRi6%2B7BtN%2BUw5mW3&X-Amz-Signature=3c778fb172dd81383af4fb51564384783573a051be8943a3a45ed270e43fc1fe&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KK3IHQQ%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIDasNkqgcyBu8LDfvcJzclwbokGcSr15ieOyuB22%2F7pfAiEAimL5scSDBsvvRQxj0KA1VT%2FK%2BF57SqnBH8GKw2L0tOMqiAQIgP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOlcEfifLOaHv3I4uircA3qvC%2F2wKV2GI76glWn%2BOt%2FMZP6C6DmWElZYA39s%2BZjYNojzYeiIAuiJECiOAGGqFC%2Brnt2%2Bki%2F9rJ7OypFer1QLVcf6rHurJzwRnZoZf5nbuRqTgoDe1HKNcw21MygGqLHaq1feS4zzY9uoHrIo9ayt7%2BIiLty2YklNRXbMhyON1jpAWhSjjkznRDymAtC%2B%2Be1nFgJEe3IODdgxy5nnYg%2BsUQ3OSNk3g%2Fg2lK%2BSQxumgIV7YYjuv%2BGYxzEoSgmxcGlOQj5TRxCBgeY45fn0E2hsprn5r8daO8G4rm64sys%2BOoeY%2FvAdEj51pM%2BsbTuGBV3WZ3ONzEv3nG7%2B%2Bz4u7S1JCZVvr3oFSUP8pmGxnGMvbsMxwfzPtQteH8bWCeiFb%2F9sHIBTkK3d3wF1%2Bleod2x6go98uiycydlOmoX4EZMM%2FlZu8LHBPrbSN4jTH%2BR%2BKl%2FeFDoHDl%2B6Yr5PukmaU33KFxYe%2FsPTYDB8CHRJj1IQoP6f5UQ9f4Nm%2FzBctV8wiIpWNGlf%2FgoPBHnZiB10R9bP8Ob%2BrXVYS5e4urAiVs9J9Cj4BLnaN6c6Q8kLfKk8TLjzn0XXW1vfFPMjNfNxWX1xKQA220lfa9pxeNrKZSMeaOZ2mKcwDaluvZ8IMNP8ob8GOqUBejhKXZvnF9m6srePieU%2B7oRV8mk6A%2FcvFBWyzFm9mNyFFEU4l61UFHkBJaXrBCfi4OwgDBUAlTOdoTJYlGCRKpKnECwm4t5C9vetm192Sn6KiFut12uSYtjsyPBiYkil1yNGUqH4tAP9MI%2F7Jq3Ra7YGGfnOByEMxDAA8uwm0yq4ynSmJRV1QmKr9G13ZfoR%2FfCvxUO5yOtu0M5lnfVYpg0ZKcsc&X-Amz-Signature=535e3c04f18610fa1d21b29b9ea8ae6f1282bd64fa9cb01ecdb58518b9463f38&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KK3IHQQ%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIDasNkqgcyBu8LDfvcJzclwbokGcSr15ieOyuB22%2F7pfAiEAimL5scSDBsvvRQxj0KA1VT%2FK%2BF57SqnBH8GKw2L0tOMqiAQIgP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOlcEfifLOaHv3I4uircA3qvC%2F2wKV2GI76glWn%2BOt%2FMZP6C6DmWElZYA39s%2BZjYNojzYeiIAuiJECiOAGGqFC%2Brnt2%2Bki%2F9rJ7OypFer1QLVcf6rHurJzwRnZoZf5nbuRqTgoDe1HKNcw21MygGqLHaq1feS4zzY9uoHrIo9ayt7%2BIiLty2YklNRXbMhyON1jpAWhSjjkznRDymAtC%2B%2Be1nFgJEe3IODdgxy5nnYg%2BsUQ3OSNk3g%2Fg2lK%2BSQxumgIV7YYjuv%2BGYxzEoSgmxcGlOQj5TRxCBgeY45fn0E2hsprn5r8daO8G4rm64sys%2BOoeY%2FvAdEj51pM%2BsbTuGBV3WZ3ONzEv3nG7%2B%2Bz4u7S1JCZVvr3oFSUP8pmGxnGMvbsMxwfzPtQteH8bWCeiFb%2F9sHIBTkK3d3wF1%2Bleod2x6go98uiycydlOmoX4EZMM%2FlZu8LHBPrbSN4jTH%2BR%2BKl%2FeFDoHDl%2B6Yr5PukmaU33KFxYe%2FsPTYDB8CHRJj1IQoP6f5UQ9f4Nm%2FzBctV8wiIpWNGlf%2FgoPBHnZiB10R9bP8Ob%2BrXVYS5e4urAiVs9J9Cj4BLnaN6c6Q8kLfKk8TLjzn0XXW1vfFPMjNfNxWX1xKQA220lfa9pxeNrKZSMeaOZ2mKcwDaluvZ8IMNP8ob8GOqUBejhKXZvnF9m6srePieU%2B7oRV8mk6A%2FcvFBWyzFm9mNyFFEU4l61UFHkBJaXrBCfi4OwgDBUAlTOdoTJYlGCRKpKnECwm4t5C9vetm192Sn6KiFut12uSYtjsyPBiYkil1yNGUqH4tAP9MI%2F7Jq3Ra7YGGfnOByEMxDAA8uwm0yq4ynSmJRV1QmKr9G13ZfoR%2FfCvxUO5yOtu0M5lnfVYpg0ZKcsc&X-Amz-Signature=23106185edb338fc91f67382f742e61425ba091740d5894d1abea1510ba6c177&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KK3IHQQ%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIDasNkqgcyBu8LDfvcJzclwbokGcSr15ieOyuB22%2F7pfAiEAimL5scSDBsvvRQxj0KA1VT%2FK%2BF57SqnBH8GKw2L0tOMqiAQIgP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOlcEfifLOaHv3I4uircA3qvC%2F2wKV2GI76glWn%2BOt%2FMZP6C6DmWElZYA39s%2BZjYNojzYeiIAuiJECiOAGGqFC%2Brnt2%2Bki%2F9rJ7OypFer1QLVcf6rHurJzwRnZoZf5nbuRqTgoDe1HKNcw21MygGqLHaq1feS4zzY9uoHrIo9ayt7%2BIiLty2YklNRXbMhyON1jpAWhSjjkznRDymAtC%2B%2Be1nFgJEe3IODdgxy5nnYg%2BsUQ3OSNk3g%2Fg2lK%2BSQxumgIV7YYjuv%2BGYxzEoSgmxcGlOQj5TRxCBgeY45fn0E2hsprn5r8daO8G4rm64sys%2BOoeY%2FvAdEj51pM%2BsbTuGBV3WZ3ONzEv3nG7%2B%2Bz4u7S1JCZVvr3oFSUP8pmGxnGMvbsMxwfzPtQteH8bWCeiFb%2F9sHIBTkK3d3wF1%2Bleod2x6go98uiycydlOmoX4EZMM%2FlZu8LHBPrbSN4jTH%2BR%2BKl%2FeFDoHDl%2B6Yr5PukmaU33KFxYe%2FsPTYDB8CHRJj1IQoP6f5UQ9f4Nm%2FzBctV8wiIpWNGlf%2FgoPBHnZiB10R9bP8Ob%2BrXVYS5e4urAiVs9J9Cj4BLnaN6c6Q8kLfKk8TLjzn0XXW1vfFPMjNfNxWX1xKQA220lfa9pxeNrKZSMeaOZ2mKcwDaluvZ8IMNP8ob8GOqUBejhKXZvnF9m6srePieU%2B7oRV8mk6A%2FcvFBWyzFm9mNyFFEU4l61UFHkBJaXrBCfi4OwgDBUAlTOdoTJYlGCRKpKnECwm4t5C9vetm192Sn6KiFut12uSYtjsyPBiYkil1yNGUqH4tAP9MI%2F7Jq3Ra7YGGfnOByEMxDAA8uwm0yq4ynSmJRV1QmKr9G13ZfoR%2FfCvxUO5yOtu0M5lnfVYpg0ZKcsc&X-Amz-Signature=8d19cf669ba6959ecf1ea2b8644579b610b2783beacfe74eca95c774629ed601&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KK3IHQQ%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIDasNkqgcyBu8LDfvcJzclwbokGcSr15ieOyuB22%2F7pfAiEAimL5scSDBsvvRQxj0KA1VT%2FK%2BF57SqnBH8GKw2L0tOMqiAQIgP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOlcEfifLOaHv3I4uircA3qvC%2F2wKV2GI76glWn%2BOt%2FMZP6C6DmWElZYA39s%2BZjYNojzYeiIAuiJECiOAGGqFC%2Brnt2%2Bki%2F9rJ7OypFer1QLVcf6rHurJzwRnZoZf5nbuRqTgoDe1HKNcw21MygGqLHaq1feS4zzY9uoHrIo9ayt7%2BIiLty2YklNRXbMhyON1jpAWhSjjkznRDymAtC%2B%2Be1nFgJEe3IODdgxy5nnYg%2BsUQ3OSNk3g%2Fg2lK%2BSQxumgIV7YYjuv%2BGYxzEoSgmxcGlOQj5TRxCBgeY45fn0E2hsprn5r8daO8G4rm64sys%2BOoeY%2FvAdEj51pM%2BsbTuGBV3WZ3ONzEv3nG7%2B%2Bz4u7S1JCZVvr3oFSUP8pmGxnGMvbsMxwfzPtQteH8bWCeiFb%2F9sHIBTkK3d3wF1%2Bleod2x6go98uiycydlOmoX4EZMM%2FlZu8LHBPrbSN4jTH%2BR%2BKl%2FeFDoHDl%2B6Yr5PukmaU33KFxYe%2FsPTYDB8CHRJj1IQoP6f5UQ9f4Nm%2FzBctV8wiIpWNGlf%2FgoPBHnZiB10R9bP8Ob%2BrXVYS5e4urAiVs9J9Cj4BLnaN6c6Q8kLfKk8TLjzn0XXW1vfFPMjNfNxWX1xKQA220lfa9pxeNrKZSMeaOZ2mKcwDaluvZ8IMNP8ob8GOqUBejhKXZvnF9m6srePieU%2B7oRV8mk6A%2FcvFBWyzFm9mNyFFEU4l61UFHkBJaXrBCfi4OwgDBUAlTOdoTJYlGCRKpKnECwm4t5C9vetm192Sn6KiFut12uSYtjsyPBiYkil1yNGUqH4tAP9MI%2F7Jq3Ra7YGGfnOByEMxDAA8uwm0yq4ynSmJRV1QmKr9G13ZfoR%2FfCvxUO5yOtu0M5lnfVYpg0ZKcsc&X-Amz-Signature=678a00341d8477680a890d5dea9f03deac2f3502f42d09d8d63499120fc1492c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KK3IHQQ%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIDasNkqgcyBu8LDfvcJzclwbokGcSr15ieOyuB22%2F7pfAiEAimL5scSDBsvvRQxj0KA1VT%2FK%2BF57SqnBH8GKw2L0tOMqiAQIgP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOlcEfifLOaHv3I4uircA3qvC%2F2wKV2GI76glWn%2BOt%2FMZP6C6DmWElZYA39s%2BZjYNojzYeiIAuiJECiOAGGqFC%2Brnt2%2Bki%2F9rJ7OypFer1QLVcf6rHurJzwRnZoZf5nbuRqTgoDe1HKNcw21MygGqLHaq1feS4zzY9uoHrIo9ayt7%2BIiLty2YklNRXbMhyON1jpAWhSjjkznRDymAtC%2B%2Be1nFgJEe3IODdgxy5nnYg%2BsUQ3OSNk3g%2Fg2lK%2BSQxumgIV7YYjuv%2BGYxzEoSgmxcGlOQj5TRxCBgeY45fn0E2hsprn5r8daO8G4rm64sys%2BOoeY%2FvAdEj51pM%2BsbTuGBV3WZ3ONzEv3nG7%2B%2Bz4u7S1JCZVvr3oFSUP8pmGxnGMvbsMxwfzPtQteH8bWCeiFb%2F9sHIBTkK3d3wF1%2Bleod2x6go98uiycydlOmoX4EZMM%2FlZu8LHBPrbSN4jTH%2BR%2BKl%2FeFDoHDl%2B6Yr5PukmaU33KFxYe%2FsPTYDB8CHRJj1IQoP6f5UQ9f4Nm%2FzBctV8wiIpWNGlf%2FgoPBHnZiB10R9bP8Ob%2BrXVYS5e4urAiVs9J9Cj4BLnaN6c6Q8kLfKk8TLjzn0XXW1vfFPMjNfNxWX1xKQA220lfa9pxeNrKZSMeaOZ2mKcwDaluvZ8IMNP8ob8GOqUBejhKXZvnF9m6srePieU%2B7oRV8mk6A%2FcvFBWyzFm9mNyFFEU4l61UFHkBJaXrBCfi4OwgDBUAlTOdoTJYlGCRKpKnECwm4t5C9vetm192Sn6KiFut12uSYtjsyPBiYkil1yNGUqH4tAP9MI%2F7Jq3Ra7YGGfnOByEMxDAA8uwm0yq4ynSmJRV1QmKr9G13ZfoR%2FfCvxUO5yOtu0M5lnfVYpg0ZKcsc&X-Amz-Signature=4d02fa7da76eda740aa4c43e93a9698c3eb01c5e9fa819b4637a4eac86999531&X-Amz-SignedHeaders=host&x-id=GetObject)
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


