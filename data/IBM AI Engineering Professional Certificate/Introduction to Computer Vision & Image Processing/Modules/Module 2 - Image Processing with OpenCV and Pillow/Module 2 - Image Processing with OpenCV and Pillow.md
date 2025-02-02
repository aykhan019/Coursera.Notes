

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZAMGRR7P%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T101344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAp1MssuLBW%2BZe%2FQev%2Fgwc6sexR%2BA4hkZCC9LiDQ6QrxAiEAsizznOctSupWQYMm50U0qj8cBkGTP%2Fny7SjuK4MRgNkqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC9tbotiJp7ApLpqmircA95kIsusB1gBHelag1X9jTP6Ik%2FupyOjzQNKk%2Bcm%2FFxFvMO2WOMPOO40PnVVCDUO6bFPrLZ%2FIZ%2FNdUY9M6%2BDBf350OGJP3jshHYKKOlcFVRyzcuXZid71HnhCdddIeZzKG5%2F78J1EycXzqmqpVU0c6gIJ%2FL5mqEFyY0FaMnIlymlc98maDF7zxLylcjduETAU1CRNY5ZTOX%2B%2BDLYLka8BpUf2N317huWQsWcL%2FfB92Bm0kvyM3tuWGex5GjL06dpshDya1m7WjnHMopM3UlkLq2kIR08L8zC8RpWgmNQs7X8%2FQQ5Q5cspMylZxT%2FQi83OduSHTDVEl5Q0PfFQZAdwlVm8MBR%2Ft49tO23vcvTaaApSzp1q3ADXkgoZ%2Bs%2BGuWrqUavYOytSjt%2BSI45FoCF38HORngwL5F6ujbk7og4pgIk1V7dUUtKzCJ5g0RlF2qBJI%2BfhoGx7GuDCkxqi1kNFoFGfHF%2FJwxZfkd6Z95gC19emJ7xDBHbcln3LDVF6tS%2BDSipZawJleUwg9YPRQ8hOMx6QOQlomhs8u5ZhJwMTa0ggGOMR%2BO1vsRfJPw%2Fe9ETRsS14u1%2BoYnm08hdbtMu6%2Fqb4iZxyN7zOC4jYNkkBe%2Fmc2Mc1aBssPaPeTmEMNCb%2FLwGOqUB6dAm7jz2IMPz%2FNdgMGwt25Qap4CRuH5J0E%2FwmqDXq%2F5%2BbtKP66L%2Fp%2BQ4bcHTuNlwbAE%2FvzYOGdAMVg72CHJCcxiProcTSpcCt1ak%2BzwBRQUhWJaU%2BXPUS8yeYrqXK8smsK9muiHpSrP7J1cbr5X%2F97mSDxxDXWYeiyyMZglXOsR2ka4IZyQXWTE2GiI%2BNXZvotWsAtbogneL9xJ1rDXfA%2BN9Hdps&X-Amz-Signature=1f4e4fd45634625154675ab8f5828d01efa2252256a7e2f88a1101a998063b5a&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXUBOINS%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T101344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCiGLMVqBSsGzNNPaFZGPha3QFiSSILeLJIJNlgRBixcQIgD%2FQbStqgqmnOtHwiNWAenl5gPYFXXPuLYVdokEVPM1UqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPVvroXV1jOh7qHYbyrcA51f28gCHMlin7dzh%2BbbK80atEnnDu9qZbhPXWns%2FkhvHV9vTkFzJNoixD%2B9%2BzTHcxlzDQjAfFR3yt2eStRm7Qnygu1irkQ594DrQ%2Fyrk05sp%2FpnqmIMlQ0PtEEIFGGcOq1S4mpav9OYYiIBlzpaWeHsnHF5A%2FDH%2FsAipSqX%2B0MqDEK9H1xlEgy3tYR1yimhqs49up5feEnvNOSk9PFEzc6RHt3cO6RuFop9kGzPOI2sMMwwTSbXTlR3TJy3KYMMkiTaOSXDxcyGg5eoWtUQD05U1J%2BSomQgkabjBAgZfeUDT3%2F0iD9BJx74ixYEETR3mCkOe9t05HmsMmQpRQdQDIcJaUa7%2Fgi1usR0zfSKn%2FITRIWSpXIJdYkfuoSuUwZadAvl4wy3PnPGyhILGu6t%2F9qApRBdMN65eqwkgoQmNn4B3FfFjS930M9J8Fsp8qY7aJ7NYGzMWI2NZCTZc3BxF0oj9ghh1Wa%2BPgJMrUrXdgTjQvQ2S1cTc9ihI%2F%2BlMUkjhQ67V2zw7VvSgatyHASUElaztac35jb1EvjeqEXGeWwG2vs42a%2FeFckkFb8%2Bg3GpzktU0s%2FZhpTkF2j%2BkommevcaYlIv4OSyn5tIpn3W9XqEY4EDtbGqrsyNODz7MKGc%2FLwGOqUBvgyBAWnhPZ5383eXffGD8mdqRJfgr8uC27HSJq7MC2XpmMgVEwO65p0Lww3YdSgjxw1d94hEiUqmV0JgWSjEH5qlq6w79uWfp4PtooZJHW49AIDwQyaCRLjWgVN6xckKMAXZvoekAMU2g1pJYkQ50Sj0IjdvPGudKe%2FqmZBFQWMlG6kgcl7mvSHwyuoQ09p9xuITGFrUo8dau6FRahwNX23AyEJe&X-Amz-Signature=3f1d0d0d79ed356c4c96c528d77b84d8353a9674f8558c74110f39a0bc6b48ea&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXUBOINS%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T101344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCiGLMVqBSsGzNNPaFZGPha3QFiSSILeLJIJNlgRBixcQIgD%2FQbStqgqmnOtHwiNWAenl5gPYFXXPuLYVdokEVPM1UqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPVvroXV1jOh7qHYbyrcA51f28gCHMlin7dzh%2BbbK80atEnnDu9qZbhPXWns%2FkhvHV9vTkFzJNoixD%2B9%2BzTHcxlzDQjAfFR3yt2eStRm7Qnygu1irkQ594DrQ%2Fyrk05sp%2FpnqmIMlQ0PtEEIFGGcOq1S4mpav9OYYiIBlzpaWeHsnHF5A%2FDH%2FsAipSqX%2B0MqDEK9H1xlEgy3tYR1yimhqs49up5feEnvNOSk9PFEzc6RHt3cO6RuFop9kGzPOI2sMMwwTSbXTlR3TJy3KYMMkiTaOSXDxcyGg5eoWtUQD05U1J%2BSomQgkabjBAgZfeUDT3%2F0iD9BJx74ixYEETR3mCkOe9t05HmsMmQpRQdQDIcJaUa7%2Fgi1usR0zfSKn%2FITRIWSpXIJdYkfuoSuUwZadAvl4wy3PnPGyhILGu6t%2F9qApRBdMN65eqwkgoQmNn4B3FfFjS930M9J8Fsp8qY7aJ7NYGzMWI2NZCTZc3BxF0oj9ghh1Wa%2BPgJMrUrXdgTjQvQ2S1cTc9ihI%2F%2BlMUkjhQ67V2zw7VvSgatyHASUElaztac35jb1EvjeqEXGeWwG2vs42a%2FeFckkFb8%2Bg3GpzktU0s%2FZhpTkF2j%2BkommevcaYlIv4OSyn5tIpn3W9XqEY4EDtbGqrsyNODz7MKGc%2FLwGOqUBvgyBAWnhPZ5383eXffGD8mdqRJfgr8uC27HSJq7MC2XpmMgVEwO65p0Lww3YdSgjxw1d94hEiUqmV0JgWSjEH5qlq6w79uWfp4PtooZJHW49AIDwQyaCRLjWgVN6xckKMAXZvoekAMU2g1pJYkQ50Sj0IjdvPGudKe%2FqmZBFQWMlG6kgcl7mvSHwyuoQ09p9xuITGFrUo8dau6FRahwNX23AyEJe&X-Amz-Signature=06955a62b47d7908daa61f255b284fbbef115a03d8424542923e74fc300c9364&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXUBOINS%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T101344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCiGLMVqBSsGzNNPaFZGPha3QFiSSILeLJIJNlgRBixcQIgD%2FQbStqgqmnOtHwiNWAenl5gPYFXXPuLYVdokEVPM1UqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPVvroXV1jOh7qHYbyrcA51f28gCHMlin7dzh%2BbbK80atEnnDu9qZbhPXWns%2FkhvHV9vTkFzJNoixD%2B9%2BzTHcxlzDQjAfFR3yt2eStRm7Qnygu1irkQ594DrQ%2Fyrk05sp%2FpnqmIMlQ0PtEEIFGGcOq1S4mpav9OYYiIBlzpaWeHsnHF5A%2FDH%2FsAipSqX%2B0MqDEK9H1xlEgy3tYR1yimhqs49up5feEnvNOSk9PFEzc6RHt3cO6RuFop9kGzPOI2sMMwwTSbXTlR3TJy3KYMMkiTaOSXDxcyGg5eoWtUQD05U1J%2BSomQgkabjBAgZfeUDT3%2F0iD9BJx74ixYEETR3mCkOe9t05HmsMmQpRQdQDIcJaUa7%2Fgi1usR0zfSKn%2FITRIWSpXIJdYkfuoSuUwZadAvl4wy3PnPGyhILGu6t%2F9qApRBdMN65eqwkgoQmNn4B3FfFjS930M9J8Fsp8qY7aJ7NYGzMWI2NZCTZc3BxF0oj9ghh1Wa%2BPgJMrUrXdgTjQvQ2S1cTc9ihI%2F%2BlMUkjhQ67V2zw7VvSgatyHASUElaztac35jb1EvjeqEXGeWwG2vs42a%2FeFckkFb8%2Bg3GpzktU0s%2FZhpTkF2j%2BkommevcaYlIv4OSyn5tIpn3W9XqEY4EDtbGqrsyNODz7MKGc%2FLwGOqUBvgyBAWnhPZ5383eXffGD8mdqRJfgr8uC27HSJq7MC2XpmMgVEwO65p0Lww3YdSgjxw1d94hEiUqmV0JgWSjEH5qlq6w79uWfp4PtooZJHW49AIDwQyaCRLjWgVN6xckKMAXZvoekAMU2g1pJYkQ50Sj0IjdvPGudKe%2FqmZBFQWMlG6kgcl7mvSHwyuoQ09p9xuITGFrUo8dau6FRahwNX23AyEJe&X-Amz-Signature=e640d5d33b108471dbca07375846f0ade469d66926caa9d19c073b8d36f006a4&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXUBOINS%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T101344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCiGLMVqBSsGzNNPaFZGPha3QFiSSILeLJIJNlgRBixcQIgD%2FQbStqgqmnOtHwiNWAenl5gPYFXXPuLYVdokEVPM1UqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPVvroXV1jOh7qHYbyrcA51f28gCHMlin7dzh%2BbbK80atEnnDu9qZbhPXWns%2FkhvHV9vTkFzJNoixD%2B9%2BzTHcxlzDQjAfFR3yt2eStRm7Qnygu1irkQ594DrQ%2Fyrk05sp%2FpnqmIMlQ0PtEEIFGGcOq1S4mpav9OYYiIBlzpaWeHsnHF5A%2FDH%2FsAipSqX%2B0MqDEK9H1xlEgy3tYR1yimhqs49up5feEnvNOSk9PFEzc6RHt3cO6RuFop9kGzPOI2sMMwwTSbXTlR3TJy3KYMMkiTaOSXDxcyGg5eoWtUQD05U1J%2BSomQgkabjBAgZfeUDT3%2F0iD9BJx74ixYEETR3mCkOe9t05HmsMmQpRQdQDIcJaUa7%2Fgi1usR0zfSKn%2FITRIWSpXIJdYkfuoSuUwZadAvl4wy3PnPGyhILGu6t%2F9qApRBdMN65eqwkgoQmNn4B3FfFjS930M9J8Fsp8qY7aJ7NYGzMWI2NZCTZc3BxF0oj9ghh1Wa%2BPgJMrUrXdgTjQvQ2S1cTc9ihI%2F%2BlMUkjhQ67V2zw7VvSgatyHASUElaztac35jb1EvjeqEXGeWwG2vs42a%2FeFckkFb8%2Bg3GpzktU0s%2FZhpTkF2j%2BkommevcaYlIv4OSyn5tIpn3W9XqEY4EDtbGqrsyNODz7MKGc%2FLwGOqUBvgyBAWnhPZ5383eXffGD8mdqRJfgr8uC27HSJq7MC2XpmMgVEwO65p0Lww3YdSgjxw1d94hEiUqmV0JgWSjEH5qlq6w79uWfp4PtooZJHW49AIDwQyaCRLjWgVN6xckKMAXZvoekAMU2g1pJYkQ50Sj0IjdvPGudKe%2FqmZBFQWMlG6kgcl7mvSHwyuoQ09p9xuITGFrUo8dau6FRahwNX23AyEJe&X-Amz-Signature=176e72f3d6dec9fb65db3e35bbb3e44df540fa716574c7d1eb1dcdb7797dbb0d&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXUBOINS%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T101344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCiGLMVqBSsGzNNPaFZGPha3QFiSSILeLJIJNlgRBixcQIgD%2FQbStqgqmnOtHwiNWAenl5gPYFXXPuLYVdokEVPM1UqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPVvroXV1jOh7qHYbyrcA51f28gCHMlin7dzh%2BbbK80atEnnDu9qZbhPXWns%2FkhvHV9vTkFzJNoixD%2B9%2BzTHcxlzDQjAfFR3yt2eStRm7Qnygu1irkQ594DrQ%2Fyrk05sp%2FpnqmIMlQ0PtEEIFGGcOq1S4mpav9OYYiIBlzpaWeHsnHF5A%2FDH%2FsAipSqX%2B0MqDEK9H1xlEgy3tYR1yimhqs49up5feEnvNOSk9PFEzc6RHt3cO6RuFop9kGzPOI2sMMwwTSbXTlR3TJy3KYMMkiTaOSXDxcyGg5eoWtUQD05U1J%2BSomQgkabjBAgZfeUDT3%2F0iD9BJx74ixYEETR3mCkOe9t05HmsMmQpRQdQDIcJaUa7%2Fgi1usR0zfSKn%2FITRIWSpXIJdYkfuoSuUwZadAvl4wy3PnPGyhILGu6t%2F9qApRBdMN65eqwkgoQmNn4B3FfFjS930M9J8Fsp8qY7aJ7NYGzMWI2NZCTZc3BxF0oj9ghh1Wa%2BPgJMrUrXdgTjQvQ2S1cTc9ihI%2F%2BlMUkjhQ67V2zw7VvSgatyHASUElaztac35jb1EvjeqEXGeWwG2vs42a%2FeFckkFb8%2Bg3GpzktU0s%2FZhpTkF2j%2BkommevcaYlIv4OSyn5tIpn3W9XqEY4EDtbGqrsyNODz7MKGc%2FLwGOqUBvgyBAWnhPZ5383eXffGD8mdqRJfgr8uC27HSJq7MC2XpmMgVEwO65p0Lww3YdSgjxw1d94hEiUqmV0JgWSjEH5qlq6w79uWfp4PtooZJHW49AIDwQyaCRLjWgVN6xckKMAXZvoekAMU2g1pJYkQ50Sj0IjdvPGudKe%2FqmZBFQWMlG6kgcl7mvSHwyuoQ09p9xuITGFrUo8dau6FRahwNX23AyEJe&X-Amz-Signature=7c3ece845c32f4463909e87903f498e5c0275b183f25249c8d4ca9e5f4b0a9df&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZAMGRR7P%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T101344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAp1MssuLBW%2BZe%2FQev%2Fgwc6sexR%2BA4hkZCC9LiDQ6QrxAiEAsizznOctSupWQYMm50U0qj8cBkGTP%2Fny7SjuK4MRgNkqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC9tbotiJp7ApLpqmircA95kIsusB1gBHelag1X9jTP6Ik%2FupyOjzQNKk%2Bcm%2FFxFvMO2WOMPOO40PnVVCDUO6bFPrLZ%2FIZ%2FNdUY9M6%2BDBf350OGJP3jshHYKKOlcFVRyzcuXZid71HnhCdddIeZzKG5%2F78J1EycXzqmqpVU0c6gIJ%2FL5mqEFyY0FaMnIlymlc98maDF7zxLylcjduETAU1CRNY5ZTOX%2B%2BDLYLka8BpUf2N317huWQsWcL%2FfB92Bm0kvyM3tuWGex5GjL06dpshDya1m7WjnHMopM3UlkLq2kIR08L8zC8RpWgmNQs7X8%2FQQ5Q5cspMylZxT%2FQi83OduSHTDVEl5Q0PfFQZAdwlVm8MBR%2Ft49tO23vcvTaaApSzp1q3ADXkgoZ%2Bs%2BGuWrqUavYOytSjt%2BSI45FoCF38HORngwL5F6ujbk7og4pgIk1V7dUUtKzCJ5g0RlF2qBJI%2BfhoGx7GuDCkxqi1kNFoFGfHF%2FJwxZfkd6Z95gC19emJ7xDBHbcln3LDVF6tS%2BDSipZawJleUwg9YPRQ8hOMx6QOQlomhs8u5ZhJwMTa0ggGOMR%2BO1vsRfJPw%2Fe9ETRsS14u1%2BoYnm08hdbtMu6%2Fqb4iZxyN7zOC4jYNkkBe%2Fmc2Mc1aBssPaPeTmEMNCb%2FLwGOqUB6dAm7jz2IMPz%2FNdgMGwt25Qap4CRuH5J0E%2FwmqDXq%2F5%2BbtKP66L%2Fp%2BQ4bcHTuNlwbAE%2FvzYOGdAMVg72CHJCcxiProcTSpcCt1ak%2BzwBRQUhWJaU%2BXPUS8yeYrqXK8smsK9muiHpSrP7J1cbr5X%2F97mSDxxDXWYeiyyMZglXOsR2ka4IZyQXWTE2GiI%2BNXZvotWsAtbogneL9xJ1rDXfA%2BN9Hdps&X-Amz-Signature=f79bbdcc2f8a4ecb5d04465febcb4bcc361e4bdf2a3e16a401d539bfd64e076a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZAMGRR7P%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T101344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAp1MssuLBW%2BZe%2FQev%2Fgwc6sexR%2BA4hkZCC9LiDQ6QrxAiEAsizznOctSupWQYMm50U0qj8cBkGTP%2Fny7SjuK4MRgNkqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC9tbotiJp7ApLpqmircA95kIsusB1gBHelag1X9jTP6Ik%2FupyOjzQNKk%2Bcm%2FFxFvMO2WOMPOO40PnVVCDUO6bFPrLZ%2FIZ%2FNdUY9M6%2BDBf350OGJP3jshHYKKOlcFVRyzcuXZid71HnhCdddIeZzKG5%2F78J1EycXzqmqpVU0c6gIJ%2FL5mqEFyY0FaMnIlymlc98maDF7zxLylcjduETAU1CRNY5ZTOX%2B%2BDLYLka8BpUf2N317huWQsWcL%2FfB92Bm0kvyM3tuWGex5GjL06dpshDya1m7WjnHMopM3UlkLq2kIR08L8zC8RpWgmNQs7X8%2FQQ5Q5cspMylZxT%2FQi83OduSHTDVEl5Q0PfFQZAdwlVm8MBR%2Ft49tO23vcvTaaApSzp1q3ADXkgoZ%2Bs%2BGuWrqUavYOytSjt%2BSI45FoCF38HORngwL5F6ujbk7og4pgIk1V7dUUtKzCJ5g0RlF2qBJI%2BfhoGx7GuDCkxqi1kNFoFGfHF%2FJwxZfkd6Z95gC19emJ7xDBHbcln3LDVF6tS%2BDSipZawJleUwg9YPRQ8hOMx6QOQlomhs8u5ZhJwMTa0ggGOMR%2BO1vsRfJPw%2Fe9ETRsS14u1%2BoYnm08hdbtMu6%2Fqb4iZxyN7zOC4jYNkkBe%2Fmc2Mc1aBssPaPeTmEMNCb%2FLwGOqUB6dAm7jz2IMPz%2FNdgMGwt25Qap4CRuH5J0E%2FwmqDXq%2F5%2BbtKP66L%2Fp%2BQ4bcHTuNlwbAE%2FvzYOGdAMVg72CHJCcxiProcTSpcCt1ak%2BzwBRQUhWJaU%2BXPUS8yeYrqXK8smsK9muiHpSrP7J1cbr5X%2F97mSDxxDXWYeiyyMZglXOsR2ka4IZyQXWTE2GiI%2BNXZvotWsAtbogneL9xJ1rDXfA%2BN9Hdps&X-Amz-Signature=82fe618fc5327a72fd901dcbedd4a7921e479c282847b7710dabf821917bd7f2&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZAMGRR7P%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T101344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAp1MssuLBW%2BZe%2FQev%2Fgwc6sexR%2BA4hkZCC9LiDQ6QrxAiEAsizznOctSupWQYMm50U0qj8cBkGTP%2Fny7SjuK4MRgNkqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC9tbotiJp7ApLpqmircA95kIsusB1gBHelag1X9jTP6Ik%2FupyOjzQNKk%2Bcm%2FFxFvMO2WOMPOO40PnVVCDUO6bFPrLZ%2FIZ%2FNdUY9M6%2BDBf350OGJP3jshHYKKOlcFVRyzcuXZid71HnhCdddIeZzKG5%2F78J1EycXzqmqpVU0c6gIJ%2FL5mqEFyY0FaMnIlymlc98maDF7zxLylcjduETAU1CRNY5ZTOX%2B%2BDLYLka8BpUf2N317huWQsWcL%2FfB92Bm0kvyM3tuWGex5GjL06dpshDya1m7WjnHMopM3UlkLq2kIR08L8zC8RpWgmNQs7X8%2FQQ5Q5cspMylZxT%2FQi83OduSHTDVEl5Q0PfFQZAdwlVm8MBR%2Ft49tO23vcvTaaApSzp1q3ADXkgoZ%2Bs%2BGuWrqUavYOytSjt%2BSI45FoCF38HORngwL5F6ujbk7og4pgIk1V7dUUtKzCJ5g0RlF2qBJI%2BfhoGx7GuDCkxqi1kNFoFGfHF%2FJwxZfkd6Z95gC19emJ7xDBHbcln3LDVF6tS%2BDSipZawJleUwg9YPRQ8hOMx6QOQlomhs8u5ZhJwMTa0ggGOMR%2BO1vsRfJPw%2Fe9ETRsS14u1%2BoYnm08hdbtMu6%2Fqb4iZxyN7zOC4jYNkkBe%2Fmc2Mc1aBssPaPeTmEMNCb%2FLwGOqUB6dAm7jz2IMPz%2FNdgMGwt25Qap4CRuH5J0E%2FwmqDXq%2F5%2BbtKP66L%2Fp%2BQ4bcHTuNlwbAE%2FvzYOGdAMVg72CHJCcxiProcTSpcCt1ak%2BzwBRQUhWJaU%2BXPUS8yeYrqXK8smsK9muiHpSrP7J1cbr5X%2F97mSDxxDXWYeiyyMZglXOsR2ka4IZyQXWTE2GiI%2BNXZvotWsAtbogneL9xJ1rDXfA%2BN9Hdps&X-Amz-Signature=78edf8a1cf24947bd1f02a2bb48a8373224ab6c999a5a0d5a020ee6ab283f237&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZAMGRR7P%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T101344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAp1MssuLBW%2BZe%2FQev%2Fgwc6sexR%2BA4hkZCC9LiDQ6QrxAiEAsizznOctSupWQYMm50U0qj8cBkGTP%2Fny7SjuK4MRgNkqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC9tbotiJp7ApLpqmircA95kIsusB1gBHelag1X9jTP6Ik%2FupyOjzQNKk%2Bcm%2FFxFvMO2WOMPOO40PnVVCDUO6bFPrLZ%2FIZ%2FNdUY9M6%2BDBf350OGJP3jshHYKKOlcFVRyzcuXZid71HnhCdddIeZzKG5%2F78J1EycXzqmqpVU0c6gIJ%2FL5mqEFyY0FaMnIlymlc98maDF7zxLylcjduETAU1CRNY5ZTOX%2B%2BDLYLka8BpUf2N317huWQsWcL%2FfB92Bm0kvyM3tuWGex5GjL06dpshDya1m7WjnHMopM3UlkLq2kIR08L8zC8RpWgmNQs7X8%2FQQ5Q5cspMylZxT%2FQi83OduSHTDVEl5Q0PfFQZAdwlVm8MBR%2Ft49tO23vcvTaaApSzp1q3ADXkgoZ%2Bs%2BGuWrqUavYOytSjt%2BSI45FoCF38HORngwL5F6ujbk7og4pgIk1V7dUUtKzCJ5g0RlF2qBJI%2BfhoGx7GuDCkxqi1kNFoFGfHF%2FJwxZfkd6Z95gC19emJ7xDBHbcln3LDVF6tS%2BDSipZawJleUwg9YPRQ8hOMx6QOQlomhs8u5ZhJwMTa0ggGOMR%2BO1vsRfJPw%2Fe9ETRsS14u1%2BoYnm08hdbtMu6%2Fqb4iZxyN7zOC4jYNkkBe%2Fmc2Mc1aBssPaPeTmEMNCb%2FLwGOqUB6dAm7jz2IMPz%2FNdgMGwt25Qap4CRuH5J0E%2FwmqDXq%2F5%2BbtKP66L%2Fp%2BQ4bcHTuNlwbAE%2FvzYOGdAMVg72CHJCcxiProcTSpcCt1ak%2BzwBRQUhWJaU%2BXPUS8yeYrqXK8smsK9muiHpSrP7J1cbr5X%2F97mSDxxDXWYeiyyMZglXOsR2ka4IZyQXWTE2GiI%2BNXZvotWsAtbogneL9xJ1rDXfA%2BN9Hdps&X-Amz-Signature=b9aa37588a3cdaa20e1197c6bb378ed70d3980dfebcb9cd9e3f88be9ac43f682&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZAMGRR7P%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T101344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAp1MssuLBW%2BZe%2FQev%2Fgwc6sexR%2BA4hkZCC9LiDQ6QrxAiEAsizznOctSupWQYMm50U0qj8cBkGTP%2Fny7SjuK4MRgNkqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC9tbotiJp7ApLpqmircA95kIsusB1gBHelag1X9jTP6Ik%2FupyOjzQNKk%2Bcm%2FFxFvMO2WOMPOO40PnVVCDUO6bFPrLZ%2FIZ%2FNdUY9M6%2BDBf350OGJP3jshHYKKOlcFVRyzcuXZid71HnhCdddIeZzKG5%2F78J1EycXzqmqpVU0c6gIJ%2FL5mqEFyY0FaMnIlymlc98maDF7zxLylcjduETAU1CRNY5ZTOX%2B%2BDLYLka8BpUf2N317huWQsWcL%2FfB92Bm0kvyM3tuWGex5GjL06dpshDya1m7WjnHMopM3UlkLq2kIR08L8zC8RpWgmNQs7X8%2FQQ5Q5cspMylZxT%2FQi83OduSHTDVEl5Q0PfFQZAdwlVm8MBR%2Ft49tO23vcvTaaApSzp1q3ADXkgoZ%2Bs%2BGuWrqUavYOytSjt%2BSI45FoCF38HORngwL5F6ujbk7og4pgIk1V7dUUtKzCJ5g0RlF2qBJI%2BfhoGx7GuDCkxqi1kNFoFGfHF%2FJwxZfkd6Z95gC19emJ7xDBHbcln3LDVF6tS%2BDSipZawJleUwg9YPRQ8hOMx6QOQlomhs8u5ZhJwMTa0ggGOMR%2BO1vsRfJPw%2Fe9ETRsS14u1%2BoYnm08hdbtMu6%2Fqb4iZxyN7zOC4jYNkkBe%2Fmc2Mc1aBssPaPeTmEMNCb%2FLwGOqUB6dAm7jz2IMPz%2FNdgMGwt25Qap4CRuH5J0E%2FwmqDXq%2F5%2BbtKP66L%2Fp%2BQ4bcHTuNlwbAE%2FvzYOGdAMVg72CHJCcxiProcTSpcCt1ak%2BzwBRQUhWJaU%2BXPUS8yeYrqXK8smsK9muiHpSrP7J1cbr5X%2F97mSDxxDXWYeiyyMZglXOsR2ka4IZyQXWTE2GiI%2BNXZvotWsAtbogneL9xJ1rDXfA%2BN9Hdps&X-Amz-Signature=955909276bc0d9d95be023d91034573d1f0da6833debefe6efe88017421f0202&X-Amz-SignedHeaders=host&x-id=GetObject)
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


