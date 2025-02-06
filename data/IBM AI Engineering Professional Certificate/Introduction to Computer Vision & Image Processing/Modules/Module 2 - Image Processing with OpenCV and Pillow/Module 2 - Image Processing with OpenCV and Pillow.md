

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WS5DTBO4%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJIMEYCIQCJz9kcbHuQqt%2BBWVfXDJCMZcuFMKsQjagIkrRi2rhyWgIhAOH2OdZ1jpZFuZ2wv5Ik2vdSuZgMkffr%2B%2Bi4Kf24nUnTKv8DCGAQABoMNjM3NDIzMTgzODA1Igx1IXut3rXiYXwq26Qq3APjfUp9Ovw9ZRDLc%2F0m5GQVzM7SR%2FFT1ffliWJYKcsp8EQwB2RcRYcgnLET7OUz118uCSMZBC1Ur6nU%2BMMqBQjxNbuYY7wjAKO4DGLtAwvsuQKwuYz%2FRf5hNr7BguC%2FmUL7xz6v47zf822BRDeJy8icB322h5yFKReRWDw8ahtJJ4lEoDRRGbeLp0tkIB8MlpjDCVZFGFdhzpJNDi6o1ilG2rYykkWeY8pzCu3IKazP8IW6gFClyXUGolTSZiDRv5t1rjmSK1IBKuw0z15bBFqN%2FutdJK7GJhQ8%2FSFFgbVtUfCgmlA1%2FDbyGfTWhp%2F1wZ8XmeuNd1qw0Gvq38mFtmRhIBqozKUPT2eUbk3RnIpF3zhPKitST%2Bqdi%2FLEh47FdeM5JKKxSyeKVEXl8t1bXK07DURAABSV4r4LT2jIRqNjIv4Ow%2Fzj9pnaLr7WL5XIkCGB1KCcVNHpKrfq8ibqlPzjjByVgTOmRloIoGUWRTo7mtugt5KKMa1vkkkolY5JxhOACujNyCAmFU5qRPmkgDY7N2EsTJz%2Bzuwb6HoYLYL09qToh5zVCe%2BBUIQhCLkBXQIw%2FxmRmZbU7Wa3K6%2FNdqMCfoKQEK9fre1pLegf7Y%2BCXxCfCB6iKXrt1smdWzCunJO9BjqkAfoI5wkbL%2B2KH7d99j9Y%2FSIxzZabz1yX4GjWDO3g9i96aYFieL9qmfzuvHgHUguraZLD7IjD9l8rY%2FOuGNipbp8JYcfdfHNhh6GoHOOVTPF0n2S3SEpA1tIxhxoQ7tq4rOibPZBPzFNRX4eEAY6ULA1i%2FaSRDKrDEcyl33zNvij1icONzlcdxMICmq9wSLW%2BdMNeSoxBiAc%2BxjFUeL87kN2gvKG%2F&X-Amz-Signature=b9485571765c2f0a4683ab4f015703414a4a6d1e5aef7da9c2f3de2e4cf759b6&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ZDEOO6Q%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJGMEQCID7tSXb7rGiChZO6LsZN8QdhJ9epcTOlcAoBJ3o2%2FYC3AiBTfgW1gwrnUpA2VrVhayFK6%2BIglnsSZuxVwpC425xCHSr%2FAwhgEAAaDDYzNzQyMzE4MzgwNSIMTUA59zeLWxUCgcN%2BKtwDeOo%2FA9W8SZYrItDP4d92%2BYNJ%2B2LRMoaYbo1VqC%2Bu5SSwpsEpI6OJHs4V2tjg3kuncsNDJZvXV0tIixr8u2FFwDoJK%2B12QOI89dDsY%2FQ0IlbHoTbwJHth2mPIX2B%2FyfQwHDz9gkEQVwiOyhRsA1tYRvDpAkVTBJxqE574wv4IzpqseipJDrV%2BOFTM4uNdqmi2H0sERFrHyQqeXHtU%2Fy0%2BzJ%2BnmDHbmTGK4PZpEoiDhUTPXt6l0UknTvkjzVPn8MKdiTA0bfqy7PYz%2BOSzvUVd%2BGLHf715XmDYKQqnj%2FEktLob1S%2BN05CjEFxFdGpybmpJ3o4rOdYiZzCJDsqUhOBnRldKsCprp4qU2lKmo0WT%2BdiCMAu%2FaFZVeFLLtetuEPUqvvLZBWqg6N8LxnbwLFPO8Neeh2nrzrTp5VdlSz0xu6AR7WAyBA3u6cCvxIRCrU2ZDVRsaKAPx4OK05wfBZvSaF4JomMQZS5Uni8BgVjUVmJ%2F2h%2B50WljjjeE%2Fhloj162qjeUumqdSa5OCrmbbv4%2BQNZqkTvfpDo7PXIRPOf%2BICXk4sw3rVLuT1gtLV8QY0a%2B%2BgJf63dnxOPgWTSRvN8Q8fANJUJnBgkIhkKy7pOmB09ALDDJv1HB9gQOaL4woZyTvQY6pgG%2Fbfr3tsJCEXvLxWbXGiHL8fH%2Fg2VDeBrTHusqMQqCDWEUeIJ2wHrHR1wQpZfB3DSWMfOWHjw4gtoHD8PVs6QIl1SSOfSDiV%2BXnY1d%2FSgK9MH%2BmzWhFBEn5W2oUSW%2FtROeFLodvAnkUxqy8%2Bx7E8wRjj5tCvDatVMa6xyMKXv7o6uvdTmhxvlhwPnknLdeiJC%2FtimD7Rlqhe%2BKA6%2BQARfXP%2Ffemb8V&X-Amz-Signature=08a07341b9e4de5457be423d77638a2e54fb5b891596afec88486d583d6af053&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ZDEOO6Q%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJGMEQCID7tSXb7rGiChZO6LsZN8QdhJ9epcTOlcAoBJ3o2%2FYC3AiBTfgW1gwrnUpA2VrVhayFK6%2BIglnsSZuxVwpC425xCHSr%2FAwhgEAAaDDYzNzQyMzE4MzgwNSIMTUA59zeLWxUCgcN%2BKtwDeOo%2FA9W8SZYrItDP4d92%2BYNJ%2B2LRMoaYbo1VqC%2Bu5SSwpsEpI6OJHs4V2tjg3kuncsNDJZvXV0tIixr8u2FFwDoJK%2B12QOI89dDsY%2FQ0IlbHoTbwJHth2mPIX2B%2FyfQwHDz9gkEQVwiOyhRsA1tYRvDpAkVTBJxqE574wv4IzpqseipJDrV%2BOFTM4uNdqmi2H0sERFrHyQqeXHtU%2Fy0%2BzJ%2BnmDHbmTGK4PZpEoiDhUTPXt6l0UknTvkjzVPn8MKdiTA0bfqy7PYz%2BOSzvUVd%2BGLHf715XmDYKQqnj%2FEktLob1S%2BN05CjEFxFdGpybmpJ3o4rOdYiZzCJDsqUhOBnRldKsCprp4qU2lKmo0WT%2BdiCMAu%2FaFZVeFLLtetuEPUqvvLZBWqg6N8LxnbwLFPO8Neeh2nrzrTp5VdlSz0xu6AR7WAyBA3u6cCvxIRCrU2ZDVRsaKAPx4OK05wfBZvSaF4JomMQZS5Uni8BgVjUVmJ%2F2h%2B50WljjjeE%2Fhloj162qjeUumqdSa5OCrmbbv4%2BQNZqkTvfpDo7PXIRPOf%2BICXk4sw3rVLuT1gtLV8QY0a%2B%2BgJf63dnxOPgWTSRvN8Q8fANJUJnBgkIhkKy7pOmB09ALDDJv1HB9gQOaL4woZyTvQY6pgG%2Fbfr3tsJCEXvLxWbXGiHL8fH%2Fg2VDeBrTHusqMQqCDWEUeIJ2wHrHR1wQpZfB3DSWMfOWHjw4gtoHD8PVs6QIl1SSOfSDiV%2BXnY1d%2FSgK9MH%2BmzWhFBEn5W2oUSW%2FtROeFLodvAnkUxqy8%2Bx7E8wRjj5tCvDatVMa6xyMKXv7o6uvdTmhxvlhwPnknLdeiJC%2FtimD7Rlqhe%2BKA6%2BQARfXP%2Ffemb8V&X-Amz-Signature=0fd9ad124ea4d8556832995df3873a2f8199dce44e42fc19d3411765ff39bd3a&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ZDEOO6Q%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJGMEQCID7tSXb7rGiChZO6LsZN8QdhJ9epcTOlcAoBJ3o2%2FYC3AiBTfgW1gwrnUpA2VrVhayFK6%2BIglnsSZuxVwpC425xCHSr%2FAwhgEAAaDDYzNzQyMzE4MzgwNSIMTUA59zeLWxUCgcN%2BKtwDeOo%2FA9W8SZYrItDP4d92%2BYNJ%2B2LRMoaYbo1VqC%2Bu5SSwpsEpI6OJHs4V2tjg3kuncsNDJZvXV0tIixr8u2FFwDoJK%2B12QOI89dDsY%2FQ0IlbHoTbwJHth2mPIX2B%2FyfQwHDz9gkEQVwiOyhRsA1tYRvDpAkVTBJxqE574wv4IzpqseipJDrV%2BOFTM4uNdqmi2H0sERFrHyQqeXHtU%2Fy0%2BzJ%2BnmDHbmTGK4PZpEoiDhUTPXt6l0UknTvkjzVPn8MKdiTA0bfqy7PYz%2BOSzvUVd%2BGLHf715XmDYKQqnj%2FEktLob1S%2BN05CjEFxFdGpybmpJ3o4rOdYiZzCJDsqUhOBnRldKsCprp4qU2lKmo0WT%2BdiCMAu%2FaFZVeFLLtetuEPUqvvLZBWqg6N8LxnbwLFPO8Neeh2nrzrTp5VdlSz0xu6AR7WAyBA3u6cCvxIRCrU2ZDVRsaKAPx4OK05wfBZvSaF4JomMQZS5Uni8BgVjUVmJ%2F2h%2B50WljjjeE%2Fhloj162qjeUumqdSa5OCrmbbv4%2BQNZqkTvfpDo7PXIRPOf%2BICXk4sw3rVLuT1gtLV8QY0a%2B%2BgJf63dnxOPgWTSRvN8Q8fANJUJnBgkIhkKy7pOmB09ALDDJv1HB9gQOaL4woZyTvQY6pgG%2Fbfr3tsJCEXvLxWbXGiHL8fH%2Fg2VDeBrTHusqMQqCDWEUeIJ2wHrHR1wQpZfB3DSWMfOWHjw4gtoHD8PVs6QIl1SSOfSDiV%2BXnY1d%2FSgK9MH%2BmzWhFBEn5W2oUSW%2FtROeFLodvAnkUxqy8%2Bx7E8wRjj5tCvDatVMa6xyMKXv7o6uvdTmhxvlhwPnknLdeiJC%2FtimD7Rlqhe%2BKA6%2BQARfXP%2Ffemb8V&X-Amz-Signature=96a000739c53dca5fd17f218d13fd6f9c940e1ba2544302f0e510f384f41229c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ZDEOO6Q%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJGMEQCID7tSXb7rGiChZO6LsZN8QdhJ9epcTOlcAoBJ3o2%2FYC3AiBTfgW1gwrnUpA2VrVhayFK6%2BIglnsSZuxVwpC425xCHSr%2FAwhgEAAaDDYzNzQyMzE4MzgwNSIMTUA59zeLWxUCgcN%2BKtwDeOo%2FA9W8SZYrItDP4d92%2BYNJ%2B2LRMoaYbo1VqC%2Bu5SSwpsEpI6OJHs4V2tjg3kuncsNDJZvXV0tIixr8u2FFwDoJK%2B12QOI89dDsY%2FQ0IlbHoTbwJHth2mPIX2B%2FyfQwHDz9gkEQVwiOyhRsA1tYRvDpAkVTBJxqE574wv4IzpqseipJDrV%2BOFTM4uNdqmi2H0sERFrHyQqeXHtU%2Fy0%2BzJ%2BnmDHbmTGK4PZpEoiDhUTPXt6l0UknTvkjzVPn8MKdiTA0bfqy7PYz%2BOSzvUVd%2BGLHf715XmDYKQqnj%2FEktLob1S%2BN05CjEFxFdGpybmpJ3o4rOdYiZzCJDsqUhOBnRldKsCprp4qU2lKmo0WT%2BdiCMAu%2FaFZVeFLLtetuEPUqvvLZBWqg6N8LxnbwLFPO8Neeh2nrzrTp5VdlSz0xu6AR7WAyBA3u6cCvxIRCrU2ZDVRsaKAPx4OK05wfBZvSaF4JomMQZS5Uni8BgVjUVmJ%2F2h%2B50WljjjeE%2Fhloj162qjeUumqdSa5OCrmbbv4%2BQNZqkTvfpDo7PXIRPOf%2BICXk4sw3rVLuT1gtLV8QY0a%2B%2BgJf63dnxOPgWTSRvN8Q8fANJUJnBgkIhkKy7pOmB09ALDDJv1HB9gQOaL4woZyTvQY6pgG%2Fbfr3tsJCEXvLxWbXGiHL8fH%2Fg2VDeBrTHusqMQqCDWEUeIJ2wHrHR1wQpZfB3DSWMfOWHjw4gtoHD8PVs6QIl1SSOfSDiV%2BXnY1d%2FSgK9MH%2BmzWhFBEn5W2oUSW%2FtROeFLodvAnkUxqy8%2Bx7E8wRjj5tCvDatVMa6xyMKXv7o6uvdTmhxvlhwPnknLdeiJC%2FtimD7Rlqhe%2BKA6%2BQARfXP%2Ffemb8V&X-Amz-Signature=f099deee622eac304d81a9cbab87862bd0f133f2f088cb100493299fa67d2773&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ZDEOO6Q%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJGMEQCID7tSXb7rGiChZO6LsZN8QdhJ9epcTOlcAoBJ3o2%2FYC3AiBTfgW1gwrnUpA2VrVhayFK6%2BIglnsSZuxVwpC425xCHSr%2FAwhgEAAaDDYzNzQyMzE4MzgwNSIMTUA59zeLWxUCgcN%2BKtwDeOo%2FA9W8SZYrItDP4d92%2BYNJ%2B2LRMoaYbo1VqC%2Bu5SSwpsEpI6OJHs4V2tjg3kuncsNDJZvXV0tIixr8u2FFwDoJK%2B12QOI89dDsY%2FQ0IlbHoTbwJHth2mPIX2B%2FyfQwHDz9gkEQVwiOyhRsA1tYRvDpAkVTBJxqE574wv4IzpqseipJDrV%2BOFTM4uNdqmi2H0sERFrHyQqeXHtU%2Fy0%2BzJ%2BnmDHbmTGK4PZpEoiDhUTPXt6l0UknTvkjzVPn8MKdiTA0bfqy7PYz%2BOSzvUVd%2BGLHf715XmDYKQqnj%2FEktLob1S%2BN05CjEFxFdGpybmpJ3o4rOdYiZzCJDsqUhOBnRldKsCprp4qU2lKmo0WT%2BdiCMAu%2FaFZVeFLLtetuEPUqvvLZBWqg6N8LxnbwLFPO8Neeh2nrzrTp5VdlSz0xu6AR7WAyBA3u6cCvxIRCrU2ZDVRsaKAPx4OK05wfBZvSaF4JomMQZS5Uni8BgVjUVmJ%2F2h%2B50WljjjeE%2Fhloj162qjeUumqdSa5OCrmbbv4%2BQNZqkTvfpDo7PXIRPOf%2BICXk4sw3rVLuT1gtLV8QY0a%2B%2BgJf63dnxOPgWTSRvN8Q8fANJUJnBgkIhkKy7pOmB09ALDDJv1HB9gQOaL4woZyTvQY6pgG%2Fbfr3tsJCEXvLxWbXGiHL8fH%2Fg2VDeBrTHusqMQqCDWEUeIJ2wHrHR1wQpZfB3DSWMfOWHjw4gtoHD8PVs6QIl1SSOfSDiV%2BXnY1d%2FSgK9MH%2BmzWhFBEn5W2oUSW%2FtROeFLodvAnkUxqy8%2Bx7E8wRjj5tCvDatVMa6xyMKXv7o6uvdTmhxvlhwPnknLdeiJC%2FtimD7Rlqhe%2BKA6%2BQARfXP%2Ffemb8V&X-Amz-Signature=f2d588c25ce0def0c82c78d2ee721a1d4a789772d12c9390d4f07989abc63679&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WS5DTBO4%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJIMEYCIQCJz9kcbHuQqt%2BBWVfXDJCMZcuFMKsQjagIkrRi2rhyWgIhAOH2OdZ1jpZFuZ2wv5Ik2vdSuZgMkffr%2B%2Bi4Kf24nUnTKv8DCGAQABoMNjM3NDIzMTgzODA1Igx1IXut3rXiYXwq26Qq3APjfUp9Ovw9ZRDLc%2F0m5GQVzM7SR%2FFT1ffliWJYKcsp8EQwB2RcRYcgnLET7OUz118uCSMZBC1Ur6nU%2BMMqBQjxNbuYY7wjAKO4DGLtAwvsuQKwuYz%2FRf5hNr7BguC%2FmUL7xz6v47zf822BRDeJy8icB322h5yFKReRWDw8ahtJJ4lEoDRRGbeLp0tkIB8MlpjDCVZFGFdhzpJNDi6o1ilG2rYykkWeY8pzCu3IKazP8IW6gFClyXUGolTSZiDRv5t1rjmSK1IBKuw0z15bBFqN%2FutdJK7GJhQ8%2FSFFgbVtUfCgmlA1%2FDbyGfTWhp%2F1wZ8XmeuNd1qw0Gvq38mFtmRhIBqozKUPT2eUbk3RnIpF3zhPKitST%2Bqdi%2FLEh47FdeM5JKKxSyeKVEXl8t1bXK07DURAABSV4r4LT2jIRqNjIv4Ow%2Fzj9pnaLr7WL5XIkCGB1KCcVNHpKrfq8ibqlPzjjByVgTOmRloIoGUWRTo7mtugt5KKMa1vkkkolY5JxhOACujNyCAmFU5qRPmkgDY7N2EsTJz%2Bzuwb6HoYLYL09qToh5zVCe%2BBUIQhCLkBXQIw%2FxmRmZbU7Wa3K6%2FNdqMCfoKQEK9fre1pLegf7Y%2BCXxCfCB6iKXrt1smdWzCunJO9BjqkAfoI5wkbL%2B2KH7d99j9Y%2FSIxzZabz1yX4GjWDO3g9i96aYFieL9qmfzuvHgHUguraZLD7IjD9l8rY%2FOuGNipbp8JYcfdfHNhh6GoHOOVTPF0n2S3SEpA1tIxhxoQ7tq4rOibPZBPzFNRX4eEAY6ULA1i%2FaSRDKrDEcyl33zNvij1icONzlcdxMICmq9wSLW%2BdMNeSoxBiAc%2BxjFUeL87kN2gvKG%2F&X-Amz-Signature=b774b2a3b8c95cb3598927020e97417507b85e31a6d21e571d4c4ccc629df8ca&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WS5DTBO4%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJIMEYCIQCJz9kcbHuQqt%2BBWVfXDJCMZcuFMKsQjagIkrRi2rhyWgIhAOH2OdZ1jpZFuZ2wv5Ik2vdSuZgMkffr%2B%2Bi4Kf24nUnTKv8DCGAQABoMNjM3NDIzMTgzODA1Igx1IXut3rXiYXwq26Qq3APjfUp9Ovw9ZRDLc%2F0m5GQVzM7SR%2FFT1ffliWJYKcsp8EQwB2RcRYcgnLET7OUz118uCSMZBC1Ur6nU%2BMMqBQjxNbuYY7wjAKO4DGLtAwvsuQKwuYz%2FRf5hNr7BguC%2FmUL7xz6v47zf822BRDeJy8icB322h5yFKReRWDw8ahtJJ4lEoDRRGbeLp0tkIB8MlpjDCVZFGFdhzpJNDi6o1ilG2rYykkWeY8pzCu3IKazP8IW6gFClyXUGolTSZiDRv5t1rjmSK1IBKuw0z15bBFqN%2FutdJK7GJhQ8%2FSFFgbVtUfCgmlA1%2FDbyGfTWhp%2F1wZ8XmeuNd1qw0Gvq38mFtmRhIBqozKUPT2eUbk3RnIpF3zhPKitST%2Bqdi%2FLEh47FdeM5JKKxSyeKVEXl8t1bXK07DURAABSV4r4LT2jIRqNjIv4Ow%2Fzj9pnaLr7WL5XIkCGB1KCcVNHpKrfq8ibqlPzjjByVgTOmRloIoGUWRTo7mtugt5KKMa1vkkkolY5JxhOACujNyCAmFU5qRPmkgDY7N2EsTJz%2Bzuwb6HoYLYL09qToh5zVCe%2BBUIQhCLkBXQIw%2FxmRmZbU7Wa3K6%2FNdqMCfoKQEK9fre1pLegf7Y%2BCXxCfCB6iKXrt1smdWzCunJO9BjqkAfoI5wkbL%2B2KH7d99j9Y%2FSIxzZabz1yX4GjWDO3g9i96aYFieL9qmfzuvHgHUguraZLD7IjD9l8rY%2FOuGNipbp8JYcfdfHNhh6GoHOOVTPF0n2S3SEpA1tIxhxoQ7tq4rOibPZBPzFNRX4eEAY6ULA1i%2FaSRDKrDEcyl33zNvij1icONzlcdxMICmq9wSLW%2BdMNeSoxBiAc%2BxjFUeL87kN2gvKG%2F&X-Amz-Signature=896d8886e7d5e855f5d938402e2ec08de830be7bbde217ba866228659bb35bcb&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WS5DTBO4%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJIMEYCIQCJz9kcbHuQqt%2BBWVfXDJCMZcuFMKsQjagIkrRi2rhyWgIhAOH2OdZ1jpZFuZ2wv5Ik2vdSuZgMkffr%2B%2Bi4Kf24nUnTKv8DCGAQABoMNjM3NDIzMTgzODA1Igx1IXut3rXiYXwq26Qq3APjfUp9Ovw9ZRDLc%2F0m5GQVzM7SR%2FFT1ffliWJYKcsp8EQwB2RcRYcgnLET7OUz118uCSMZBC1Ur6nU%2BMMqBQjxNbuYY7wjAKO4DGLtAwvsuQKwuYz%2FRf5hNr7BguC%2FmUL7xz6v47zf822BRDeJy8icB322h5yFKReRWDw8ahtJJ4lEoDRRGbeLp0tkIB8MlpjDCVZFGFdhzpJNDi6o1ilG2rYykkWeY8pzCu3IKazP8IW6gFClyXUGolTSZiDRv5t1rjmSK1IBKuw0z15bBFqN%2FutdJK7GJhQ8%2FSFFgbVtUfCgmlA1%2FDbyGfTWhp%2F1wZ8XmeuNd1qw0Gvq38mFtmRhIBqozKUPT2eUbk3RnIpF3zhPKitST%2Bqdi%2FLEh47FdeM5JKKxSyeKVEXl8t1bXK07DURAABSV4r4LT2jIRqNjIv4Ow%2Fzj9pnaLr7WL5XIkCGB1KCcVNHpKrfq8ibqlPzjjByVgTOmRloIoGUWRTo7mtugt5KKMa1vkkkolY5JxhOACujNyCAmFU5qRPmkgDY7N2EsTJz%2Bzuwb6HoYLYL09qToh5zVCe%2BBUIQhCLkBXQIw%2FxmRmZbU7Wa3K6%2FNdqMCfoKQEK9fre1pLegf7Y%2BCXxCfCB6iKXrt1smdWzCunJO9BjqkAfoI5wkbL%2B2KH7d99j9Y%2FSIxzZabz1yX4GjWDO3g9i96aYFieL9qmfzuvHgHUguraZLD7IjD9l8rY%2FOuGNipbp8JYcfdfHNhh6GoHOOVTPF0n2S3SEpA1tIxhxoQ7tq4rOibPZBPzFNRX4eEAY6ULA1i%2FaSRDKrDEcyl33zNvij1icONzlcdxMICmq9wSLW%2BdMNeSoxBiAc%2BxjFUeL87kN2gvKG%2F&X-Amz-Signature=e11506564d9be66fe592e7a21f72e0da23a26695f5370cd00d68f96c2a7501e9&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WS5DTBO4%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJIMEYCIQCJz9kcbHuQqt%2BBWVfXDJCMZcuFMKsQjagIkrRi2rhyWgIhAOH2OdZ1jpZFuZ2wv5Ik2vdSuZgMkffr%2B%2Bi4Kf24nUnTKv8DCGAQABoMNjM3NDIzMTgzODA1Igx1IXut3rXiYXwq26Qq3APjfUp9Ovw9ZRDLc%2F0m5GQVzM7SR%2FFT1ffliWJYKcsp8EQwB2RcRYcgnLET7OUz118uCSMZBC1Ur6nU%2BMMqBQjxNbuYY7wjAKO4DGLtAwvsuQKwuYz%2FRf5hNr7BguC%2FmUL7xz6v47zf822BRDeJy8icB322h5yFKReRWDw8ahtJJ4lEoDRRGbeLp0tkIB8MlpjDCVZFGFdhzpJNDi6o1ilG2rYykkWeY8pzCu3IKazP8IW6gFClyXUGolTSZiDRv5t1rjmSK1IBKuw0z15bBFqN%2FutdJK7GJhQ8%2FSFFgbVtUfCgmlA1%2FDbyGfTWhp%2F1wZ8XmeuNd1qw0Gvq38mFtmRhIBqozKUPT2eUbk3RnIpF3zhPKitST%2Bqdi%2FLEh47FdeM5JKKxSyeKVEXl8t1bXK07DURAABSV4r4LT2jIRqNjIv4Ow%2Fzj9pnaLr7WL5XIkCGB1KCcVNHpKrfq8ibqlPzjjByVgTOmRloIoGUWRTo7mtugt5KKMa1vkkkolY5JxhOACujNyCAmFU5qRPmkgDY7N2EsTJz%2Bzuwb6HoYLYL09qToh5zVCe%2BBUIQhCLkBXQIw%2FxmRmZbU7Wa3K6%2FNdqMCfoKQEK9fre1pLegf7Y%2BCXxCfCB6iKXrt1smdWzCunJO9BjqkAfoI5wkbL%2B2KH7d99j9Y%2FSIxzZabz1yX4GjWDO3g9i96aYFieL9qmfzuvHgHUguraZLD7IjD9l8rY%2FOuGNipbp8JYcfdfHNhh6GoHOOVTPF0n2S3SEpA1tIxhxoQ7tq4rOibPZBPzFNRX4eEAY6ULA1i%2FaSRDKrDEcyl33zNvij1icONzlcdxMICmq9wSLW%2BdMNeSoxBiAc%2BxjFUeL87kN2gvKG%2F&X-Amz-Signature=48d97ed2317e22f3f923ce21f1d52ce8cb4a35a7d2a4205abcb363e3f3d48eeb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WS5DTBO4%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJIMEYCIQCJz9kcbHuQqt%2BBWVfXDJCMZcuFMKsQjagIkrRi2rhyWgIhAOH2OdZ1jpZFuZ2wv5Ik2vdSuZgMkffr%2B%2Bi4Kf24nUnTKv8DCGAQABoMNjM3NDIzMTgzODA1Igx1IXut3rXiYXwq26Qq3APjfUp9Ovw9ZRDLc%2F0m5GQVzM7SR%2FFT1ffliWJYKcsp8EQwB2RcRYcgnLET7OUz118uCSMZBC1Ur6nU%2BMMqBQjxNbuYY7wjAKO4DGLtAwvsuQKwuYz%2FRf5hNr7BguC%2FmUL7xz6v47zf822BRDeJy8icB322h5yFKReRWDw8ahtJJ4lEoDRRGbeLp0tkIB8MlpjDCVZFGFdhzpJNDi6o1ilG2rYykkWeY8pzCu3IKazP8IW6gFClyXUGolTSZiDRv5t1rjmSK1IBKuw0z15bBFqN%2FutdJK7GJhQ8%2FSFFgbVtUfCgmlA1%2FDbyGfTWhp%2F1wZ8XmeuNd1qw0Gvq38mFtmRhIBqozKUPT2eUbk3RnIpF3zhPKitST%2Bqdi%2FLEh47FdeM5JKKxSyeKVEXl8t1bXK07DURAABSV4r4LT2jIRqNjIv4Ow%2Fzj9pnaLr7WL5XIkCGB1KCcVNHpKrfq8ibqlPzjjByVgTOmRloIoGUWRTo7mtugt5KKMa1vkkkolY5JxhOACujNyCAmFU5qRPmkgDY7N2EsTJz%2Bzuwb6HoYLYL09qToh5zVCe%2BBUIQhCLkBXQIw%2FxmRmZbU7Wa3K6%2FNdqMCfoKQEK9fre1pLegf7Y%2BCXxCfCB6iKXrt1smdWzCunJO9BjqkAfoI5wkbL%2B2KH7d99j9Y%2FSIxzZabz1yX4GjWDO3g9i96aYFieL9qmfzuvHgHUguraZLD7IjD9l8rY%2FOuGNipbp8JYcfdfHNhh6GoHOOVTPF0n2S3SEpA1tIxhxoQ7tq4rOibPZBPzFNRX4eEAY6ULA1i%2FaSRDKrDEcyl33zNvij1icONzlcdxMICmq9wSLW%2BdMNeSoxBiAc%2BxjFUeL87kN2gvKG%2F&X-Amz-Signature=49d006eb7a23abe84260b3aecc8db5f7f8dda9034be61935c120bc0175f2fe30&X-Amz-SignedHeaders=host&x-id=GetObject)
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


