

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YMVMS6GX%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQDmRGyxKp34ymvPulqmd3PeIFRxLbTx5vQCujsOcN8s%2BQIhANqlGDTpaWODTUyRBGQW6EAdKHng00L02w4Hjd7ZGC0iKogECIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzIv0MG%2FpzX%2BBzqzfsq3AMXr6zMaGr6CB%2F%2FonofZdivBwrrYSHK%2B%2BJ9bmQODTo%2FncHAoIwX0ZCsIeNmN3h6dYPXkqVaskOguU4BVZFeKULrO6DD%2F%2F3kPcDQx6jIhBhDh1Fwt8PpEHTYamOofd5kWMOrqK0%2FPzQEkc7rTqXPJLCiUsWMrhjxhmquTlkTyDt9%2B34zvmbC8%2BoMNHLM7H%2FmXg49uVoPiwQN8dhg%2FqypzEJ8Kaan8R%2B4FgEG6KNVe4ThHF%2BhP%2B%2BacPazekhDXPaqGNx5%2B4aW%2BKrjJPoZAdTX%2Fx1iwz5SKMZFhFA%2BVelYdzL9dmyokZrcfCqMCtIQ7iEE74qvfiyj0xL%2BKYBZEra0wWxCdvjOCXNHyqa3rm6IIzoiyl6QsJgcZF8fufXCW1DU14drKVc48TgBiRsQPQ9N39obmFHRCfqYxXSiheZhHY4Vd3k2g4V%2F0frLJs101bJp9aFugRSdNbF3a5QrGgGz0J2t4rUh17ifegMoYReeLhUgczQo1L%2Fei7wCHfiODDpvG6SwNJvoipr6LDI6nw8rFo9TieEgytDD7NKG8ouIqmiVkx3Cjpwb%2Bo8P7KlK4LvSlm%2Bz1OAviHZXQPXWiqKbu2EBCyphog7tDpXoH4%2FwoNo94RXu%2FuaOoxU9ZT1gLTDVn%2Ba8BjqkAWXemWLKqtM%2BeB2ULSfFeCDwwxB%2B0QR%2FZc0r%2FqePK%2FV9yu2KFZmm3sqXkQKY8HrwsCeqY2u78rM%2FiISMm9lQMiJfgdXa7Gioi5jcv%2BmgAkx%2FPyvI%2F2vullAEmhP9VtQg4tFd8HiOI%2FC1phEBjJysZQnaOM7p9jsOSIx6fo5SwDMiN5XFAe%2B6dK1bWHqJ%2F5HXJdcsaZL1KGY7RMyzLmvYnCphmQ90&X-Amz-Signature=d0c480a629a2869f079c8c5d4cee06c06c6ca5be0ce67a435aaa56020fa2ced8&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBKLD2XP%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIERgD7P0qGVdDPEAaUPQTlUYUr2huTvdJVXOLIfECOttAiEApg3BkC9Xz1DtSFVD46t7fkmLcYyQDwP8rXd%2F7EH8bgQqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK21on51lSzP2VdWvCrcA0Dy8h2ErFfyxvnTM9n%2FuX2K%2Fyh2PXihoHzipRSg23MwdgdR3LVauNJZ3uGRfM0wNB7GBAJ%2F7tnWmZr7Z3IyIO2kjnJj11mhMQE%2BRe34yNkRbd%2FDj6XL%2FCczbF6Udomm4pimsPvz1%2FAaW78glZA8jpSftbr5cJXEKOMdnIHTtvsk0qbfnkYbubErKp8%2B%2BAoRnFOGfoo2mlN4wuArTGlOp7J0zLXRan%2B6IVAdtr9xCjU04vSdUXiPac2b2CNew9T9%2F7jV0WiJiHTHQttK%2BVvLUjXDQ7Rz5mbpPOybFveHtOG7VtUEyn4ncRQri%2Boxu9gxda258QBV%2BHZLI3uU05dVBiNPUswbMBUTVm68%2BBb5IhSNIkieWmlB%2Bp4DAi3i6qDxJVqYK6X402X2siFQiDzEUjlIUgy8Ef0NFDfplkCgUgC4dG%2F8mag39N7mz1dDJgQ358Y5clBQeIJ1jXT%2B0DKzdPDuaUbOxt%2FBkdckMhU4exmT7jMSSdyqjW5f2VCBLTDTwl8eK4PvTUCaKVMDjJFIa6qqYz1OfAaTKs%2Bx7cVyZkZkYxuTCqayE9Yun4v1MkDPci9pURL90ArPJB4vzbMc0G8TyEMRzaxi%2FCJCdYs1HmEs0PWQsypEJMoYvnCYMNSf5rwGOqUBWbXz2p6UlB4vIlBoeRgtIRhlWp1u3dNakd5z8JJ6AAYLOzb4cYU9WikSW%2BvSNmVN3mri50yfYxOQNTr8AnkHtVUqSxWnfceuuY1cVQZ5bbPbrObOgeLm1H%2FHsKoO2tBMWQxu8B%2BlrUrAgRGnS%2BDr8mGLxppwCuuDn0tsuMNBy2N%2FEHueT%2FwpdLNY37zdc8T2jMDK3%2BQR20YBRS4F9Ej2ytnsYnSo&X-Amz-Signature=46949c2d0012730ee8394002a1a0ba88570320be18131bfbfd2a1c9f5a06c1e6&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBKLD2XP%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIERgD7P0qGVdDPEAaUPQTlUYUr2huTvdJVXOLIfECOttAiEApg3BkC9Xz1DtSFVD46t7fkmLcYyQDwP8rXd%2F7EH8bgQqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK21on51lSzP2VdWvCrcA0Dy8h2ErFfyxvnTM9n%2FuX2K%2Fyh2PXihoHzipRSg23MwdgdR3LVauNJZ3uGRfM0wNB7GBAJ%2F7tnWmZr7Z3IyIO2kjnJj11mhMQE%2BRe34yNkRbd%2FDj6XL%2FCczbF6Udomm4pimsPvz1%2FAaW78glZA8jpSftbr5cJXEKOMdnIHTtvsk0qbfnkYbubErKp8%2B%2BAoRnFOGfoo2mlN4wuArTGlOp7J0zLXRan%2B6IVAdtr9xCjU04vSdUXiPac2b2CNew9T9%2F7jV0WiJiHTHQttK%2BVvLUjXDQ7Rz5mbpPOybFveHtOG7VtUEyn4ncRQri%2Boxu9gxda258QBV%2BHZLI3uU05dVBiNPUswbMBUTVm68%2BBb5IhSNIkieWmlB%2Bp4DAi3i6qDxJVqYK6X402X2siFQiDzEUjlIUgy8Ef0NFDfplkCgUgC4dG%2F8mag39N7mz1dDJgQ358Y5clBQeIJ1jXT%2B0DKzdPDuaUbOxt%2FBkdckMhU4exmT7jMSSdyqjW5f2VCBLTDTwl8eK4PvTUCaKVMDjJFIa6qqYz1OfAaTKs%2Bx7cVyZkZkYxuTCqayE9Yun4v1MkDPci9pURL90ArPJB4vzbMc0G8TyEMRzaxi%2FCJCdYs1HmEs0PWQsypEJMoYvnCYMNSf5rwGOqUBWbXz2p6UlB4vIlBoeRgtIRhlWp1u3dNakd5z8JJ6AAYLOzb4cYU9WikSW%2BvSNmVN3mri50yfYxOQNTr8AnkHtVUqSxWnfceuuY1cVQZ5bbPbrObOgeLm1H%2FHsKoO2tBMWQxu8B%2BlrUrAgRGnS%2BDr8mGLxppwCuuDn0tsuMNBy2N%2FEHueT%2FwpdLNY37zdc8T2jMDK3%2BQR20YBRS4F9Ej2ytnsYnSo&X-Amz-Signature=564ba12bdfda99cfc273ae5cf654de34915e3f0c91fe3d3a890681fa1c0adc27&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBKLD2XP%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIERgD7P0qGVdDPEAaUPQTlUYUr2huTvdJVXOLIfECOttAiEApg3BkC9Xz1DtSFVD46t7fkmLcYyQDwP8rXd%2F7EH8bgQqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK21on51lSzP2VdWvCrcA0Dy8h2ErFfyxvnTM9n%2FuX2K%2Fyh2PXihoHzipRSg23MwdgdR3LVauNJZ3uGRfM0wNB7GBAJ%2F7tnWmZr7Z3IyIO2kjnJj11mhMQE%2BRe34yNkRbd%2FDj6XL%2FCczbF6Udomm4pimsPvz1%2FAaW78glZA8jpSftbr5cJXEKOMdnIHTtvsk0qbfnkYbubErKp8%2B%2BAoRnFOGfoo2mlN4wuArTGlOp7J0zLXRan%2B6IVAdtr9xCjU04vSdUXiPac2b2CNew9T9%2F7jV0WiJiHTHQttK%2BVvLUjXDQ7Rz5mbpPOybFveHtOG7VtUEyn4ncRQri%2Boxu9gxda258QBV%2BHZLI3uU05dVBiNPUswbMBUTVm68%2BBb5IhSNIkieWmlB%2Bp4DAi3i6qDxJVqYK6X402X2siFQiDzEUjlIUgy8Ef0NFDfplkCgUgC4dG%2F8mag39N7mz1dDJgQ358Y5clBQeIJ1jXT%2B0DKzdPDuaUbOxt%2FBkdckMhU4exmT7jMSSdyqjW5f2VCBLTDTwl8eK4PvTUCaKVMDjJFIa6qqYz1OfAaTKs%2Bx7cVyZkZkYxuTCqayE9Yun4v1MkDPci9pURL90ArPJB4vzbMc0G8TyEMRzaxi%2FCJCdYs1HmEs0PWQsypEJMoYvnCYMNSf5rwGOqUBWbXz2p6UlB4vIlBoeRgtIRhlWp1u3dNakd5z8JJ6AAYLOzb4cYU9WikSW%2BvSNmVN3mri50yfYxOQNTr8AnkHtVUqSxWnfceuuY1cVQZ5bbPbrObOgeLm1H%2FHsKoO2tBMWQxu8B%2BlrUrAgRGnS%2BDr8mGLxppwCuuDn0tsuMNBy2N%2FEHueT%2FwpdLNY37zdc8T2jMDK3%2BQR20YBRS4F9Ej2ytnsYnSo&X-Amz-Signature=306999b8be90c301e1749149e83574164a8b776be9361be63dde59f786ba8224&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBKLD2XP%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIERgD7P0qGVdDPEAaUPQTlUYUr2huTvdJVXOLIfECOttAiEApg3BkC9Xz1DtSFVD46t7fkmLcYyQDwP8rXd%2F7EH8bgQqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK21on51lSzP2VdWvCrcA0Dy8h2ErFfyxvnTM9n%2FuX2K%2Fyh2PXihoHzipRSg23MwdgdR3LVauNJZ3uGRfM0wNB7GBAJ%2F7tnWmZr7Z3IyIO2kjnJj11mhMQE%2BRe34yNkRbd%2FDj6XL%2FCczbF6Udomm4pimsPvz1%2FAaW78glZA8jpSftbr5cJXEKOMdnIHTtvsk0qbfnkYbubErKp8%2B%2BAoRnFOGfoo2mlN4wuArTGlOp7J0zLXRan%2B6IVAdtr9xCjU04vSdUXiPac2b2CNew9T9%2F7jV0WiJiHTHQttK%2BVvLUjXDQ7Rz5mbpPOybFveHtOG7VtUEyn4ncRQri%2Boxu9gxda258QBV%2BHZLI3uU05dVBiNPUswbMBUTVm68%2BBb5IhSNIkieWmlB%2Bp4DAi3i6qDxJVqYK6X402X2siFQiDzEUjlIUgy8Ef0NFDfplkCgUgC4dG%2F8mag39N7mz1dDJgQ358Y5clBQeIJ1jXT%2B0DKzdPDuaUbOxt%2FBkdckMhU4exmT7jMSSdyqjW5f2VCBLTDTwl8eK4PvTUCaKVMDjJFIa6qqYz1OfAaTKs%2Bx7cVyZkZkYxuTCqayE9Yun4v1MkDPci9pURL90ArPJB4vzbMc0G8TyEMRzaxi%2FCJCdYs1HmEs0PWQsypEJMoYvnCYMNSf5rwGOqUBWbXz2p6UlB4vIlBoeRgtIRhlWp1u3dNakd5z8JJ6AAYLOzb4cYU9WikSW%2BvSNmVN3mri50yfYxOQNTr8AnkHtVUqSxWnfceuuY1cVQZ5bbPbrObOgeLm1H%2FHsKoO2tBMWQxu8B%2BlrUrAgRGnS%2BDr8mGLxppwCuuDn0tsuMNBy2N%2FEHueT%2FwpdLNY37zdc8T2jMDK3%2BQR20YBRS4F9Ej2ytnsYnSo&X-Amz-Signature=288e1dcec8232aa35d71385d5f019af9e08683f237398d83a333b9461f9efa5b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBKLD2XP%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIERgD7P0qGVdDPEAaUPQTlUYUr2huTvdJVXOLIfECOttAiEApg3BkC9Xz1DtSFVD46t7fkmLcYyQDwP8rXd%2F7EH8bgQqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK21on51lSzP2VdWvCrcA0Dy8h2ErFfyxvnTM9n%2FuX2K%2Fyh2PXihoHzipRSg23MwdgdR3LVauNJZ3uGRfM0wNB7GBAJ%2F7tnWmZr7Z3IyIO2kjnJj11mhMQE%2BRe34yNkRbd%2FDj6XL%2FCczbF6Udomm4pimsPvz1%2FAaW78glZA8jpSftbr5cJXEKOMdnIHTtvsk0qbfnkYbubErKp8%2B%2BAoRnFOGfoo2mlN4wuArTGlOp7J0zLXRan%2B6IVAdtr9xCjU04vSdUXiPac2b2CNew9T9%2F7jV0WiJiHTHQttK%2BVvLUjXDQ7Rz5mbpPOybFveHtOG7VtUEyn4ncRQri%2Boxu9gxda258QBV%2BHZLI3uU05dVBiNPUswbMBUTVm68%2BBb5IhSNIkieWmlB%2Bp4DAi3i6qDxJVqYK6X402X2siFQiDzEUjlIUgy8Ef0NFDfplkCgUgC4dG%2F8mag39N7mz1dDJgQ358Y5clBQeIJ1jXT%2B0DKzdPDuaUbOxt%2FBkdckMhU4exmT7jMSSdyqjW5f2VCBLTDTwl8eK4PvTUCaKVMDjJFIa6qqYz1OfAaTKs%2Bx7cVyZkZkYxuTCqayE9Yun4v1MkDPci9pURL90ArPJB4vzbMc0G8TyEMRzaxi%2FCJCdYs1HmEs0PWQsypEJMoYvnCYMNSf5rwGOqUBWbXz2p6UlB4vIlBoeRgtIRhlWp1u3dNakd5z8JJ6AAYLOzb4cYU9WikSW%2BvSNmVN3mri50yfYxOQNTr8AnkHtVUqSxWnfceuuY1cVQZ5bbPbrObOgeLm1H%2FHsKoO2tBMWQxu8B%2BlrUrAgRGnS%2BDr8mGLxppwCuuDn0tsuMNBy2N%2FEHueT%2FwpdLNY37zdc8T2jMDK3%2BQR20YBRS4F9Ej2ytnsYnSo&X-Amz-Signature=1ad75c2816a676db6241c9bcc8491aad2842ec35a089b2986c6c58628655164f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YMVMS6GX%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQDmRGyxKp34ymvPulqmd3PeIFRxLbTx5vQCujsOcN8s%2BQIhANqlGDTpaWODTUyRBGQW6EAdKHng00L02w4Hjd7ZGC0iKogECIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzIv0MG%2FpzX%2BBzqzfsq3AMXr6zMaGr6CB%2F%2FonofZdivBwrrYSHK%2B%2BJ9bmQODTo%2FncHAoIwX0ZCsIeNmN3h6dYPXkqVaskOguU4BVZFeKULrO6DD%2F%2F3kPcDQx6jIhBhDh1Fwt8PpEHTYamOofd5kWMOrqK0%2FPzQEkc7rTqXPJLCiUsWMrhjxhmquTlkTyDt9%2B34zvmbC8%2BoMNHLM7H%2FmXg49uVoPiwQN8dhg%2FqypzEJ8Kaan8R%2B4FgEG6KNVe4ThHF%2BhP%2B%2BacPazekhDXPaqGNx5%2B4aW%2BKrjJPoZAdTX%2Fx1iwz5SKMZFhFA%2BVelYdzL9dmyokZrcfCqMCtIQ7iEE74qvfiyj0xL%2BKYBZEra0wWxCdvjOCXNHyqa3rm6IIzoiyl6QsJgcZF8fufXCW1DU14drKVc48TgBiRsQPQ9N39obmFHRCfqYxXSiheZhHY4Vd3k2g4V%2F0frLJs101bJp9aFugRSdNbF3a5QrGgGz0J2t4rUh17ifegMoYReeLhUgczQo1L%2Fei7wCHfiODDpvG6SwNJvoipr6LDI6nw8rFo9TieEgytDD7NKG8ouIqmiVkx3Cjpwb%2Bo8P7KlK4LvSlm%2Bz1OAviHZXQPXWiqKbu2EBCyphog7tDpXoH4%2FwoNo94RXu%2FuaOoxU9ZT1gLTDVn%2Ba8BjqkAWXemWLKqtM%2BeB2ULSfFeCDwwxB%2B0QR%2FZc0r%2FqePK%2FV9yu2KFZmm3sqXkQKY8HrwsCeqY2u78rM%2FiISMm9lQMiJfgdXa7Gioi5jcv%2BmgAkx%2FPyvI%2F2vullAEmhP9VtQg4tFd8HiOI%2FC1phEBjJysZQnaOM7p9jsOSIx6fo5SwDMiN5XFAe%2B6dK1bWHqJ%2F5HXJdcsaZL1KGY7RMyzLmvYnCphmQ90&X-Amz-Signature=96c66be6bdf7e9179707d2e9e6454866897be1bcb102853d23d221e0068932a2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YMVMS6GX%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQDmRGyxKp34ymvPulqmd3PeIFRxLbTx5vQCujsOcN8s%2BQIhANqlGDTpaWODTUyRBGQW6EAdKHng00L02w4Hjd7ZGC0iKogECIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzIv0MG%2FpzX%2BBzqzfsq3AMXr6zMaGr6CB%2F%2FonofZdivBwrrYSHK%2B%2BJ9bmQODTo%2FncHAoIwX0ZCsIeNmN3h6dYPXkqVaskOguU4BVZFeKULrO6DD%2F%2F3kPcDQx6jIhBhDh1Fwt8PpEHTYamOofd5kWMOrqK0%2FPzQEkc7rTqXPJLCiUsWMrhjxhmquTlkTyDt9%2B34zvmbC8%2BoMNHLM7H%2FmXg49uVoPiwQN8dhg%2FqypzEJ8Kaan8R%2B4FgEG6KNVe4ThHF%2BhP%2B%2BacPazekhDXPaqGNx5%2B4aW%2BKrjJPoZAdTX%2Fx1iwz5SKMZFhFA%2BVelYdzL9dmyokZrcfCqMCtIQ7iEE74qvfiyj0xL%2BKYBZEra0wWxCdvjOCXNHyqa3rm6IIzoiyl6QsJgcZF8fufXCW1DU14drKVc48TgBiRsQPQ9N39obmFHRCfqYxXSiheZhHY4Vd3k2g4V%2F0frLJs101bJp9aFugRSdNbF3a5QrGgGz0J2t4rUh17ifegMoYReeLhUgczQo1L%2Fei7wCHfiODDpvG6SwNJvoipr6LDI6nw8rFo9TieEgytDD7NKG8ouIqmiVkx3Cjpwb%2Bo8P7KlK4LvSlm%2Bz1OAviHZXQPXWiqKbu2EBCyphog7tDpXoH4%2FwoNo94RXu%2FuaOoxU9ZT1gLTDVn%2Ba8BjqkAWXemWLKqtM%2BeB2ULSfFeCDwwxB%2B0QR%2FZc0r%2FqePK%2FV9yu2KFZmm3sqXkQKY8HrwsCeqY2u78rM%2FiISMm9lQMiJfgdXa7Gioi5jcv%2BmgAkx%2FPyvI%2F2vullAEmhP9VtQg4tFd8HiOI%2FC1phEBjJysZQnaOM7p9jsOSIx6fo5SwDMiN5XFAe%2B6dK1bWHqJ%2F5HXJdcsaZL1KGY7RMyzLmvYnCphmQ90&X-Amz-Signature=0429103a617630f97b5eb418857d5b99f5f6e9b5876ef9f1228c42fb06450fae&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YMVMS6GX%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQDmRGyxKp34ymvPulqmd3PeIFRxLbTx5vQCujsOcN8s%2BQIhANqlGDTpaWODTUyRBGQW6EAdKHng00L02w4Hjd7ZGC0iKogECIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzIv0MG%2FpzX%2BBzqzfsq3AMXr6zMaGr6CB%2F%2FonofZdivBwrrYSHK%2B%2BJ9bmQODTo%2FncHAoIwX0ZCsIeNmN3h6dYPXkqVaskOguU4BVZFeKULrO6DD%2F%2F3kPcDQx6jIhBhDh1Fwt8PpEHTYamOofd5kWMOrqK0%2FPzQEkc7rTqXPJLCiUsWMrhjxhmquTlkTyDt9%2B34zvmbC8%2BoMNHLM7H%2FmXg49uVoPiwQN8dhg%2FqypzEJ8Kaan8R%2B4FgEG6KNVe4ThHF%2BhP%2B%2BacPazekhDXPaqGNx5%2B4aW%2BKrjJPoZAdTX%2Fx1iwz5SKMZFhFA%2BVelYdzL9dmyokZrcfCqMCtIQ7iEE74qvfiyj0xL%2BKYBZEra0wWxCdvjOCXNHyqa3rm6IIzoiyl6QsJgcZF8fufXCW1DU14drKVc48TgBiRsQPQ9N39obmFHRCfqYxXSiheZhHY4Vd3k2g4V%2F0frLJs101bJp9aFugRSdNbF3a5QrGgGz0J2t4rUh17ifegMoYReeLhUgczQo1L%2Fei7wCHfiODDpvG6SwNJvoipr6LDI6nw8rFo9TieEgytDD7NKG8ouIqmiVkx3Cjpwb%2Bo8P7KlK4LvSlm%2Bz1OAviHZXQPXWiqKbu2EBCyphog7tDpXoH4%2FwoNo94RXu%2FuaOoxU9ZT1gLTDVn%2Ba8BjqkAWXemWLKqtM%2BeB2ULSfFeCDwwxB%2B0QR%2FZc0r%2FqePK%2FV9yu2KFZmm3sqXkQKY8HrwsCeqY2u78rM%2FiISMm9lQMiJfgdXa7Gioi5jcv%2BmgAkx%2FPyvI%2F2vullAEmhP9VtQg4tFd8HiOI%2FC1phEBjJysZQnaOM7p9jsOSIx6fo5SwDMiN5XFAe%2B6dK1bWHqJ%2F5HXJdcsaZL1KGY7RMyzLmvYnCphmQ90&X-Amz-Signature=8f3fc034197dd88cd43e928c53fe0407d4b33b30f1369fd6da7507d41a4f992a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YMVMS6GX%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQDmRGyxKp34ymvPulqmd3PeIFRxLbTx5vQCujsOcN8s%2BQIhANqlGDTpaWODTUyRBGQW6EAdKHng00L02w4Hjd7ZGC0iKogECIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzIv0MG%2FpzX%2BBzqzfsq3AMXr6zMaGr6CB%2F%2FonofZdivBwrrYSHK%2B%2BJ9bmQODTo%2FncHAoIwX0ZCsIeNmN3h6dYPXkqVaskOguU4BVZFeKULrO6DD%2F%2F3kPcDQx6jIhBhDh1Fwt8PpEHTYamOofd5kWMOrqK0%2FPzQEkc7rTqXPJLCiUsWMrhjxhmquTlkTyDt9%2B34zvmbC8%2BoMNHLM7H%2FmXg49uVoPiwQN8dhg%2FqypzEJ8Kaan8R%2B4FgEG6KNVe4ThHF%2BhP%2B%2BacPazekhDXPaqGNx5%2B4aW%2BKrjJPoZAdTX%2Fx1iwz5SKMZFhFA%2BVelYdzL9dmyokZrcfCqMCtIQ7iEE74qvfiyj0xL%2BKYBZEra0wWxCdvjOCXNHyqa3rm6IIzoiyl6QsJgcZF8fufXCW1DU14drKVc48TgBiRsQPQ9N39obmFHRCfqYxXSiheZhHY4Vd3k2g4V%2F0frLJs101bJp9aFugRSdNbF3a5QrGgGz0J2t4rUh17ifegMoYReeLhUgczQo1L%2Fei7wCHfiODDpvG6SwNJvoipr6LDI6nw8rFo9TieEgytDD7NKG8ouIqmiVkx3Cjpwb%2Bo8P7KlK4LvSlm%2Bz1OAviHZXQPXWiqKbu2EBCyphog7tDpXoH4%2FwoNo94RXu%2FuaOoxU9ZT1gLTDVn%2Ba8BjqkAWXemWLKqtM%2BeB2ULSfFeCDwwxB%2B0QR%2FZc0r%2FqePK%2FV9yu2KFZmm3sqXkQKY8HrwsCeqY2u78rM%2FiISMm9lQMiJfgdXa7Gioi5jcv%2BmgAkx%2FPyvI%2F2vullAEmhP9VtQg4tFd8HiOI%2FC1phEBjJysZQnaOM7p9jsOSIx6fo5SwDMiN5XFAe%2B6dK1bWHqJ%2F5HXJdcsaZL1KGY7RMyzLmvYnCphmQ90&X-Amz-Signature=216298c79cfa13d9b055774e5816727223d59d690b05604ebb380cdb0ba601dd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YMVMS6GX%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQDmRGyxKp34ymvPulqmd3PeIFRxLbTx5vQCujsOcN8s%2BQIhANqlGDTpaWODTUyRBGQW6EAdKHng00L02w4Hjd7ZGC0iKogECIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzIv0MG%2FpzX%2BBzqzfsq3AMXr6zMaGr6CB%2F%2FonofZdivBwrrYSHK%2B%2BJ9bmQODTo%2FncHAoIwX0ZCsIeNmN3h6dYPXkqVaskOguU4BVZFeKULrO6DD%2F%2F3kPcDQx6jIhBhDh1Fwt8PpEHTYamOofd5kWMOrqK0%2FPzQEkc7rTqXPJLCiUsWMrhjxhmquTlkTyDt9%2B34zvmbC8%2BoMNHLM7H%2FmXg49uVoPiwQN8dhg%2FqypzEJ8Kaan8R%2B4FgEG6KNVe4ThHF%2BhP%2B%2BacPazekhDXPaqGNx5%2B4aW%2BKrjJPoZAdTX%2Fx1iwz5SKMZFhFA%2BVelYdzL9dmyokZrcfCqMCtIQ7iEE74qvfiyj0xL%2BKYBZEra0wWxCdvjOCXNHyqa3rm6IIzoiyl6QsJgcZF8fufXCW1DU14drKVc48TgBiRsQPQ9N39obmFHRCfqYxXSiheZhHY4Vd3k2g4V%2F0frLJs101bJp9aFugRSdNbF3a5QrGgGz0J2t4rUh17ifegMoYReeLhUgczQo1L%2Fei7wCHfiODDpvG6SwNJvoipr6LDI6nw8rFo9TieEgytDD7NKG8ouIqmiVkx3Cjpwb%2Bo8P7KlK4LvSlm%2Bz1OAviHZXQPXWiqKbu2EBCyphog7tDpXoH4%2FwoNo94RXu%2FuaOoxU9ZT1gLTDVn%2Ba8BjqkAWXemWLKqtM%2BeB2ULSfFeCDwwxB%2B0QR%2FZc0r%2FqePK%2FV9yu2KFZmm3sqXkQKY8HrwsCeqY2u78rM%2FiISMm9lQMiJfgdXa7Gioi5jcv%2BmgAkx%2FPyvI%2F2vullAEmhP9VtQg4tFd8HiOI%2FC1phEBjJysZQnaOM7p9jsOSIx6fo5SwDMiN5XFAe%2B6dK1bWHqJ%2F5HXJdcsaZL1KGY7RMyzLmvYnCphmQ90&X-Amz-Signature=9b0f423f5466008dac9296ab5bd9727230f3e0ed8510f38fc6a3042cbb54ae59&X-Amz-SignedHeaders=host&x-id=GetObject)
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


