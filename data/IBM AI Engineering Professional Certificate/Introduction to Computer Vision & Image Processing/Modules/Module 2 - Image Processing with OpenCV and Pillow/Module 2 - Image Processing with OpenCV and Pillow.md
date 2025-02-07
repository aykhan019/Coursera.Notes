

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWPKKP5A%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJHMEUCIQCvM7Y7iFvjUkk0BIbeYsGinju%2BeZ4rbkTZNk1C4BXa0gIgWNZaVKyMKTPmqEDE3wN%2BgW%2Fx0Xx55nLC3m06llGkTE0q%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDFDGptFxTH1bLdGAxyrcA8p%2F%2B2YIB%2FMB7b8lkxrMvUy8unXubZXgCyC3R4pMwzvAvHzrw237G%2B7jzMJh4vmkWsQCf0zBVFAviPOQ48UAHNd4KCWKHTCjM7XEYqPLZKKFpbB47YPqK5VSfWGK9ffNxu0LUR6qgSEV75BH2bAfcKOklihCx%2FovgXgeeAIwEmpMqBw3mi6vUAYO2XZjGh7z7a9o3LngQ5iXUU3V1F22%2FnTlBCr0UJpUCKV%2BLgu0%2FAmQq%2BOIo8yi4pHO04ytswErUMP0TLnluwovHrCFmBKCzBneaGIRyQaPUcqrMLcu3jyV40f67sGLXNqgyeE1xYkewr3esz50aLOpPwTs3Ko8j8tJ%2BbXz%2BjqdA29LcYU4gztObKWmwv5H5p7BRNRJ1uru3d6jXs1mEFmdBvFJNK4gbrU1DWrTlsDiTjPFRcmBAh2Hdan7NIzEgdctBKZbXWYUyDd4aXdZp3TPK8DPt6mFahD9wNc4O%2F0T30xFzj09V5mnnoMKzoAB4D%2FV%2F5uEn6QsZ92VgoYCA1T4zstUnCk5KgubLNSYDOKuLQ30jPXoRYV60QoMmSdlkBOVAp%2FCw0UyZB9xfJsvlUSjrXp72zHIo4Wt%2F%2B5sFBB3eT1qIlL9t9%2FMhuiBeiwC0gDyEqOTMPPfmL0GOqUBhF3RZpAvurbHiLAYr78ix8ltf%2BpUQ6bPX%2Bpl9My4%2BNHw1OHAZbWot3LcxZxPErGrnv3OQOeKd%2BjN40XU2reEXJHupNOtM1YyExQW%2FVMmgIgFO3T8xttCLAYsnaXuHXN5eaNZENDD5JTUUwtmW46L4Qix2XFQriFe1A6Lyp4%2FJHY%2Fqj6V1QLQnjAaSKGafGp3J0LMklxGMbmASyBlEgtf5D8z2vb4&X-Amz-Signature=ed2b5b0a8ea56de9a2bff9838753f28d9567a5bc456535c7ed044d18ef21648f&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XWY64M6C%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJHMEUCIQCwTMW8k8nL4ReWcMu6f3BM0LYwBeLXiYkEXgNQhJYyyQIgMxbPdJKAdEiX2ffx6%2BWNBj%2B0sOnoeeUaucnVwgcT0yoq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDEdvd5buEWHSPRFJsCrcAxVP2J1Y2WJMcB56QEefyLfLaXn3HO7WyyFyQWhj3zVRWECQV0%2F98I2gSItBz4XeN2Ob%2F1C%2FKawsruVQZ9sfqULzIhNJ%2Bh0Eg34wF%2BSU0T1YsBwrDqCeisIIrxiOT301nEA7rglv1xrbmvfDRUKL7rejhuv2HXJXBEHpmRLwkjWeGa08CQ9GEKgDGEk7YYfj7Zuq4VROVYGOQ4edudDnQdEsYSIrqNaHreiJTkkd%2BRa0WG28i0DVi%2FAVxkx%2FxuL3nDMOJKstO16m8HvUowAH1AGXdsA3PQkWTid1BszmSlorw1kmLdGyNVG48%2FZgT4UmBtCgBMXocXbGgvWTKXwwchBYz%2BECAhvs9eg%2Be85qduezGzruN3oNerR4%2Falbmqfv4sYs4eROOcAiuHInQThLifj%2F8ip%2BFcgdcT2t3heQLeFTiM5ln3%2BazHsfeVIS4eLwZge1s1iICSXOcY%2BZF%2FszA45FPlFPPUAkSNrNSIf8cKEp57XyY3OYsv9Y3hyok4FAEq1iflaP0zRKiP5XKnuS0UZFxsPNy4Krl9YFjAWvDW7VLYF9MqhOhrC64G5%2FqlVu3EIToHVyRGcAEhBmk3jETvePLz287LmesM4PSaj7fxX0KVI73F5%2BSykPoeFuMNngmL0GOqUBOuJxovHHa7ijmYTzGZbTSqfj8FPziY1Cw0FmwSYM1uBpj9BtdH2sbUc7sQF3r1%2FD4RT%2Bms3jRp32PUdQJIgVtFhPe2O3%2Fjlc2%2FUfR75r3A5VBLmEpTe%2Fj1AvmN0rUXywOdTMr0BPLvHeBfioO2bt0ef1aVnZfAPZFbWyUsaWHr3XJwnGiMKC6quo6IifVFWiIBa1HqAW%2FCiFAM2RsOjAPhKm2RLZ&X-Amz-Signature=8666b314633e3968651576a0233b2de0c258ba3318a393c37a78e185baea5a79&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XWY64M6C%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJHMEUCIQCwTMW8k8nL4ReWcMu6f3BM0LYwBeLXiYkEXgNQhJYyyQIgMxbPdJKAdEiX2ffx6%2BWNBj%2B0sOnoeeUaucnVwgcT0yoq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDEdvd5buEWHSPRFJsCrcAxVP2J1Y2WJMcB56QEefyLfLaXn3HO7WyyFyQWhj3zVRWECQV0%2F98I2gSItBz4XeN2Ob%2F1C%2FKawsruVQZ9sfqULzIhNJ%2Bh0Eg34wF%2BSU0T1YsBwrDqCeisIIrxiOT301nEA7rglv1xrbmvfDRUKL7rejhuv2HXJXBEHpmRLwkjWeGa08CQ9GEKgDGEk7YYfj7Zuq4VROVYGOQ4edudDnQdEsYSIrqNaHreiJTkkd%2BRa0WG28i0DVi%2FAVxkx%2FxuL3nDMOJKstO16m8HvUowAH1AGXdsA3PQkWTid1BszmSlorw1kmLdGyNVG48%2FZgT4UmBtCgBMXocXbGgvWTKXwwchBYz%2BECAhvs9eg%2Be85qduezGzruN3oNerR4%2Falbmqfv4sYs4eROOcAiuHInQThLifj%2F8ip%2BFcgdcT2t3heQLeFTiM5ln3%2BazHsfeVIS4eLwZge1s1iICSXOcY%2BZF%2FszA45FPlFPPUAkSNrNSIf8cKEp57XyY3OYsv9Y3hyok4FAEq1iflaP0zRKiP5XKnuS0UZFxsPNy4Krl9YFjAWvDW7VLYF9MqhOhrC64G5%2FqlVu3EIToHVyRGcAEhBmk3jETvePLz287LmesM4PSaj7fxX0KVI73F5%2BSykPoeFuMNngmL0GOqUBOuJxovHHa7ijmYTzGZbTSqfj8FPziY1Cw0FmwSYM1uBpj9BtdH2sbUc7sQF3r1%2FD4RT%2Bms3jRp32PUdQJIgVtFhPe2O3%2Fjlc2%2FUfR75r3A5VBLmEpTe%2Fj1AvmN0rUXywOdTMr0BPLvHeBfioO2bt0ef1aVnZfAPZFbWyUsaWHr3XJwnGiMKC6quo6IifVFWiIBa1HqAW%2FCiFAM2RsOjAPhKm2RLZ&X-Amz-Signature=8b13eac379f683c457443e8eb721db3262bb07bd4e9d42ac5cee7f18c267ea42&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XWY64M6C%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJHMEUCIQCwTMW8k8nL4ReWcMu6f3BM0LYwBeLXiYkEXgNQhJYyyQIgMxbPdJKAdEiX2ffx6%2BWNBj%2B0sOnoeeUaucnVwgcT0yoq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDEdvd5buEWHSPRFJsCrcAxVP2J1Y2WJMcB56QEefyLfLaXn3HO7WyyFyQWhj3zVRWECQV0%2F98I2gSItBz4XeN2Ob%2F1C%2FKawsruVQZ9sfqULzIhNJ%2Bh0Eg34wF%2BSU0T1YsBwrDqCeisIIrxiOT301nEA7rglv1xrbmvfDRUKL7rejhuv2HXJXBEHpmRLwkjWeGa08CQ9GEKgDGEk7YYfj7Zuq4VROVYGOQ4edudDnQdEsYSIrqNaHreiJTkkd%2BRa0WG28i0DVi%2FAVxkx%2FxuL3nDMOJKstO16m8HvUowAH1AGXdsA3PQkWTid1BszmSlorw1kmLdGyNVG48%2FZgT4UmBtCgBMXocXbGgvWTKXwwchBYz%2BECAhvs9eg%2Be85qduezGzruN3oNerR4%2Falbmqfv4sYs4eROOcAiuHInQThLifj%2F8ip%2BFcgdcT2t3heQLeFTiM5ln3%2BazHsfeVIS4eLwZge1s1iICSXOcY%2BZF%2FszA45FPlFPPUAkSNrNSIf8cKEp57XyY3OYsv9Y3hyok4FAEq1iflaP0zRKiP5XKnuS0UZFxsPNy4Krl9YFjAWvDW7VLYF9MqhOhrC64G5%2FqlVu3EIToHVyRGcAEhBmk3jETvePLz287LmesM4PSaj7fxX0KVI73F5%2BSykPoeFuMNngmL0GOqUBOuJxovHHa7ijmYTzGZbTSqfj8FPziY1Cw0FmwSYM1uBpj9BtdH2sbUc7sQF3r1%2FD4RT%2Bms3jRp32PUdQJIgVtFhPe2O3%2Fjlc2%2FUfR75r3A5VBLmEpTe%2Fj1AvmN0rUXywOdTMr0BPLvHeBfioO2bt0ef1aVnZfAPZFbWyUsaWHr3XJwnGiMKC6quo6IifVFWiIBa1HqAW%2FCiFAM2RsOjAPhKm2RLZ&X-Amz-Signature=f0788288cd97ea4371ba5615a9dd0a7d63349acfd74bd7d02e46cd218bb97132&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XWY64M6C%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJHMEUCIQCwTMW8k8nL4ReWcMu6f3BM0LYwBeLXiYkEXgNQhJYyyQIgMxbPdJKAdEiX2ffx6%2BWNBj%2B0sOnoeeUaucnVwgcT0yoq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDEdvd5buEWHSPRFJsCrcAxVP2J1Y2WJMcB56QEefyLfLaXn3HO7WyyFyQWhj3zVRWECQV0%2F98I2gSItBz4XeN2Ob%2F1C%2FKawsruVQZ9sfqULzIhNJ%2Bh0Eg34wF%2BSU0T1YsBwrDqCeisIIrxiOT301nEA7rglv1xrbmvfDRUKL7rejhuv2HXJXBEHpmRLwkjWeGa08CQ9GEKgDGEk7YYfj7Zuq4VROVYGOQ4edudDnQdEsYSIrqNaHreiJTkkd%2BRa0WG28i0DVi%2FAVxkx%2FxuL3nDMOJKstO16m8HvUowAH1AGXdsA3PQkWTid1BszmSlorw1kmLdGyNVG48%2FZgT4UmBtCgBMXocXbGgvWTKXwwchBYz%2BECAhvs9eg%2Be85qduezGzruN3oNerR4%2Falbmqfv4sYs4eROOcAiuHInQThLifj%2F8ip%2BFcgdcT2t3heQLeFTiM5ln3%2BazHsfeVIS4eLwZge1s1iICSXOcY%2BZF%2FszA45FPlFPPUAkSNrNSIf8cKEp57XyY3OYsv9Y3hyok4FAEq1iflaP0zRKiP5XKnuS0UZFxsPNy4Krl9YFjAWvDW7VLYF9MqhOhrC64G5%2FqlVu3EIToHVyRGcAEhBmk3jETvePLz287LmesM4PSaj7fxX0KVI73F5%2BSykPoeFuMNngmL0GOqUBOuJxovHHa7ijmYTzGZbTSqfj8FPziY1Cw0FmwSYM1uBpj9BtdH2sbUc7sQF3r1%2FD4RT%2Bms3jRp32PUdQJIgVtFhPe2O3%2Fjlc2%2FUfR75r3A5VBLmEpTe%2Fj1AvmN0rUXywOdTMr0BPLvHeBfioO2bt0ef1aVnZfAPZFbWyUsaWHr3XJwnGiMKC6quo6IifVFWiIBa1HqAW%2FCiFAM2RsOjAPhKm2RLZ&X-Amz-Signature=3ef06cc531eb296f28245e1e29d7b7417bd5acdedb291750b0b12d8209d05a50&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XWY64M6C%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJHMEUCIQCwTMW8k8nL4ReWcMu6f3BM0LYwBeLXiYkEXgNQhJYyyQIgMxbPdJKAdEiX2ffx6%2BWNBj%2B0sOnoeeUaucnVwgcT0yoq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDEdvd5buEWHSPRFJsCrcAxVP2J1Y2WJMcB56QEefyLfLaXn3HO7WyyFyQWhj3zVRWECQV0%2F98I2gSItBz4XeN2Ob%2F1C%2FKawsruVQZ9sfqULzIhNJ%2Bh0Eg34wF%2BSU0T1YsBwrDqCeisIIrxiOT301nEA7rglv1xrbmvfDRUKL7rejhuv2HXJXBEHpmRLwkjWeGa08CQ9GEKgDGEk7YYfj7Zuq4VROVYGOQ4edudDnQdEsYSIrqNaHreiJTkkd%2BRa0WG28i0DVi%2FAVxkx%2FxuL3nDMOJKstO16m8HvUowAH1AGXdsA3PQkWTid1BszmSlorw1kmLdGyNVG48%2FZgT4UmBtCgBMXocXbGgvWTKXwwchBYz%2BECAhvs9eg%2Be85qduezGzruN3oNerR4%2Falbmqfv4sYs4eROOcAiuHInQThLifj%2F8ip%2BFcgdcT2t3heQLeFTiM5ln3%2BazHsfeVIS4eLwZge1s1iICSXOcY%2BZF%2FszA45FPlFPPUAkSNrNSIf8cKEp57XyY3OYsv9Y3hyok4FAEq1iflaP0zRKiP5XKnuS0UZFxsPNy4Krl9YFjAWvDW7VLYF9MqhOhrC64G5%2FqlVu3EIToHVyRGcAEhBmk3jETvePLz287LmesM4PSaj7fxX0KVI73F5%2BSykPoeFuMNngmL0GOqUBOuJxovHHa7ijmYTzGZbTSqfj8FPziY1Cw0FmwSYM1uBpj9BtdH2sbUc7sQF3r1%2FD4RT%2Bms3jRp32PUdQJIgVtFhPe2O3%2Fjlc2%2FUfR75r3A5VBLmEpTe%2Fj1AvmN0rUXywOdTMr0BPLvHeBfioO2bt0ef1aVnZfAPZFbWyUsaWHr3XJwnGiMKC6quo6IifVFWiIBa1HqAW%2FCiFAM2RsOjAPhKm2RLZ&X-Amz-Signature=525fc76c4cea75c64e163adb87b7e5765c2ebbd60e2f16f9d7c6cfecb77494ae&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWPKKP5A%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJHMEUCIQCvM7Y7iFvjUkk0BIbeYsGinju%2BeZ4rbkTZNk1C4BXa0gIgWNZaVKyMKTPmqEDE3wN%2BgW%2Fx0Xx55nLC3m06llGkTE0q%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDFDGptFxTH1bLdGAxyrcA8p%2F%2B2YIB%2FMB7b8lkxrMvUy8unXubZXgCyC3R4pMwzvAvHzrw237G%2B7jzMJh4vmkWsQCf0zBVFAviPOQ48UAHNd4KCWKHTCjM7XEYqPLZKKFpbB47YPqK5VSfWGK9ffNxu0LUR6qgSEV75BH2bAfcKOklihCx%2FovgXgeeAIwEmpMqBw3mi6vUAYO2XZjGh7z7a9o3LngQ5iXUU3V1F22%2FnTlBCr0UJpUCKV%2BLgu0%2FAmQq%2BOIo8yi4pHO04ytswErUMP0TLnluwovHrCFmBKCzBneaGIRyQaPUcqrMLcu3jyV40f67sGLXNqgyeE1xYkewr3esz50aLOpPwTs3Ko8j8tJ%2BbXz%2BjqdA29LcYU4gztObKWmwv5H5p7BRNRJ1uru3d6jXs1mEFmdBvFJNK4gbrU1DWrTlsDiTjPFRcmBAh2Hdan7NIzEgdctBKZbXWYUyDd4aXdZp3TPK8DPt6mFahD9wNc4O%2F0T30xFzj09V5mnnoMKzoAB4D%2FV%2F5uEn6QsZ92VgoYCA1T4zstUnCk5KgubLNSYDOKuLQ30jPXoRYV60QoMmSdlkBOVAp%2FCw0UyZB9xfJsvlUSjrXp72zHIo4Wt%2F%2B5sFBB3eT1qIlL9t9%2FMhuiBeiwC0gDyEqOTMPPfmL0GOqUBhF3RZpAvurbHiLAYr78ix8ltf%2BpUQ6bPX%2Bpl9My4%2BNHw1OHAZbWot3LcxZxPErGrnv3OQOeKd%2BjN40XU2reEXJHupNOtM1YyExQW%2FVMmgIgFO3T8xttCLAYsnaXuHXN5eaNZENDD5JTUUwtmW46L4Qix2XFQriFe1A6Lyp4%2FJHY%2Fqj6V1QLQnjAaSKGafGp3J0LMklxGMbmASyBlEgtf5D8z2vb4&X-Amz-Signature=1daf30a82de5ff5193fab3f1adfe897393b71c3bf74a71cb88b69911f249231b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWPKKP5A%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJHMEUCIQCvM7Y7iFvjUkk0BIbeYsGinju%2BeZ4rbkTZNk1C4BXa0gIgWNZaVKyMKTPmqEDE3wN%2BgW%2Fx0Xx55nLC3m06llGkTE0q%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDFDGptFxTH1bLdGAxyrcA8p%2F%2B2YIB%2FMB7b8lkxrMvUy8unXubZXgCyC3R4pMwzvAvHzrw237G%2B7jzMJh4vmkWsQCf0zBVFAviPOQ48UAHNd4KCWKHTCjM7XEYqPLZKKFpbB47YPqK5VSfWGK9ffNxu0LUR6qgSEV75BH2bAfcKOklihCx%2FovgXgeeAIwEmpMqBw3mi6vUAYO2XZjGh7z7a9o3LngQ5iXUU3V1F22%2FnTlBCr0UJpUCKV%2BLgu0%2FAmQq%2BOIo8yi4pHO04ytswErUMP0TLnluwovHrCFmBKCzBneaGIRyQaPUcqrMLcu3jyV40f67sGLXNqgyeE1xYkewr3esz50aLOpPwTs3Ko8j8tJ%2BbXz%2BjqdA29LcYU4gztObKWmwv5H5p7BRNRJ1uru3d6jXs1mEFmdBvFJNK4gbrU1DWrTlsDiTjPFRcmBAh2Hdan7NIzEgdctBKZbXWYUyDd4aXdZp3TPK8DPt6mFahD9wNc4O%2F0T30xFzj09V5mnnoMKzoAB4D%2FV%2F5uEn6QsZ92VgoYCA1T4zstUnCk5KgubLNSYDOKuLQ30jPXoRYV60QoMmSdlkBOVAp%2FCw0UyZB9xfJsvlUSjrXp72zHIo4Wt%2F%2B5sFBB3eT1qIlL9t9%2FMhuiBeiwC0gDyEqOTMPPfmL0GOqUBhF3RZpAvurbHiLAYr78ix8ltf%2BpUQ6bPX%2Bpl9My4%2BNHw1OHAZbWot3LcxZxPErGrnv3OQOeKd%2BjN40XU2reEXJHupNOtM1YyExQW%2FVMmgIgFO3T8xttCLAYsnaXuHXN5eaNZENDD5JTUUwtmW46L4Qix2XFQriFe1A6Lyp4%2FJHY%2Fqj6V1QLQnjAaSKGafGp3J0LMklxGMbmASyBlEgtf5D8z2vb4&X-Amz-Signature=805a3f9f899c66dfd2a35cbf0aaa13c3f5a3f4f15edb0d86615309b195791ee1&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWPKKP5A%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJHMEUCIQCvM7Y7iFvjUkk0BIbeYsGinju%2BeZ4rbkTZNk1C4BXa0gIgWNZaVKyMKTPmqEDE3wN%2BgW%2Fx0Xx55nLC3m06llGkTE0q%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDFDGptFxTH1bLdGAxyrcA8p%2F%2B2YIB%2FMB7b8lkxrMvUy8unXubZXgCyC3R4pMwzvAvHzrw237G%2B7jzMJh4vmkWsQCf0zBVFAviPOQ48UAHNd4KCWKHTCjM7XEYqPLZKKFpbB47YPqK5VSfWGK9ffNxu0LUR6qgSEV75BH2bAfcKOklihCx%2FovgXgeeAIwEmpMqBw3mi6vUAYO2XZjGh7z7a9o3LngQ5iXUU3V1F22%2FnTlBCr0UJpUCKV%2BLgu0%2FAmQq%2BOIo8yi4pHO04ytswErUMP0TLnluwovHrCFmBKCzBneaGIRyQaPUcqrMLcu3jyV40f67sGLXNqgyeE1xYkewr3esz50aLOpPwTs3Ko8j8tJ%2BbXz%2BjqdA29LcYU4gztObKWmwv5H5p7BRNRJ1uru3d6jXs1mEFmdBvFJNK4gbrU1DWrTlsDiTjPFRcmBAh2Hdan7NIzEgdctBKZbXWYUyDd4aXdZp3TPK8DPt6mFahD9wNc4O%2F0T30xFzj09V5mnnoMKzoAB4D%2FV%2F5uEn6QsZ92VgoYCA1T4zstUnCk5KgubLNSYDOKuLQ30jPXoRYV60QoMmSdlkBOVAp%2FCw0UyZB9xfJsvlUSjrXp72zHIo4Wt%2F%2B5sFBB3eT1qIlL9t9%2FMhuiBeiwC0gDyEqOTMPPfmL0GOqUBhF3RZpAvurbHiLAYr78ix8ltf%2BpUQ6bPX%2Bpl9My4%2BNHw1OHAZbWot3LcxZxPErGrnv3OQOeKd%2BjN40XU2reEXJHupNOtM1YyExQW%2FVMmgIgFO3T8xttCLAYsnaXuHXN5eaNZENDD5JTUUwtmW46L4Qix2XFQriFe1A6Lyp4%2FJHY%2Fqj6V1QLQnjAaSKGafGp3J0LMklxGMbmASyBlEgtf5D8z2vb4&X-Amz-Signature=ab66a61e95be69b06b39240993eda9683630631130a4a1d8c8ada7da0a2a7bda&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWPKKP5A%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJHMEUCIQCvM7Y7iFvjUkk0BIbeYsGinju%2BeZ4rbkTZNk1C4BXa0gIgWNZaVKyMKTPmqEDE3wN%2BgW%2Fx0Xx55nLC3m06llGkTE0q%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDFDGptFxTH1bLdGAxyrcA8p%2F%2B2YIB%2FMB7b8lkxrMvUy8unXubZXgCyC3R4pMwzvAvHzrw237G%2B7jzMJh4vmkWsQCf0zBVFAviPOQ48UAHNd4KCWKHTCjM7XEYqPLZKKFpbB47YPqK5VSfWGK9ffNxu0LUR6qgSEV75BH2bAfcKOklihCx%2FovgXgeeAIwEmpMqBw3mi6vUAYO2XZjGh7z7a9o3LngQ5iXUU3V1F22%2FnTlBCr0UJpUCKV%2BLgu0%2FAmQq%2BOIo8yi4pHO04ytswErUMP0TLnluwovHrCFmBKCzBneaGIRyQaPUcqrMLcu3jyV40f67sGLXNqgyeE1xYkewr3esz50aLOpPwTs3Ko8j8tJ%2BbXz%2BjqdA29LcYU4gztObKWmwv5H5p7BRNRJ1uru3d6jXs1mEFmdBvFJNK4gbrU1DWrTlsDiTjPFRcmBAh2Hdan7NIzEgdctBKZbXWYUyDd4aXdZp3TPK8DPt6mFahD9wNc4O%2F0T30xFzj09V5mnnoMKzoAB4D%2FV%2F5uEn6QsZ92VgoYCA1T4zstUnCk5KgubLNSYDOKuLQ30jPXoRYV60QoMmSdlkBOVAp%2FCw0UyZB9xfJsvlUSjrXp72zHIo4Wt%2F%2B5sFBB3eT1qIlL9t9%2FMhuiBeiwC0gDyEqOTMPPfmL0GOqUBhF3RZpAvurbHiLAYr78ix8ltf%2BpUQ6bPX%2Bpl9My4%2BNHw1OHAZbWot3LcxZxPErGrnv3OQOeKd%2BjN40XU2reEXJHupNOtM1YyExQW%2FVMmgIgFO3T8xttCLAYsnaXuHXN5eaNZENDD5JTUUwtmW46L4Qix2XFQriFe1A6Lyp4%2FJHY%2Fqj6V1QLQnjAaSKGafGp3J0LMklxGMbmASyBlEgtf5D8z2vb4&X-Amz-Signature=35494ac58278e7573d805135d17855c8f7d59b51b3e6786602ff02e95c35cd83&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWPKKP5A%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJHMEUCIQCvM7Y7iFvjUkk0BIbeYsGinju%2BeZ4rbkTZNk1C4BXa0gIgWNZaVKyMKTPmqEDE3wN%2BgW%2Fx0Xx55nLC3m06llGkTE0q%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDFDGptFxTH1bLdGAxyrcA8p%2F%2B2YIB%2FMB7b8lkxrMvUy8unXubZXgCyC3R4pMwzvAvHzrw237G%2B7jzMJh4vmkWsQCf0zBVFAviPOQ48UAHNd4KCWKHTCjM7XEYqPLZKKFpbB47YPqK5VSfWGK9ffNxu0LUR6qgSEV75BH2bAfcKOklihCx%2FovgXgeeAIwEmpMqBw3mi6vUAYO2XZjGh7z7a9o3LngQ5iXUU3V1F22%2FnTlBCr0UJpUCKV%2BLgu0%2FAmQq%2BOIo8yi4pHO04ytswErUMP0TLnluwovHrCFmBKCzBneaGIRyQaPUcqrMLcu3jyV40f67sGLXNqgyeE1xYkewr3esz50aLOpPwTs3Ko8j8tJ%2BbXz%2BjqdA29LcYU4gztObKWmwv5H5p7BRNRJ1uru3d6jXs1mEFmdBvFJNK4gbrU1DWrTlsDiTjPFRcmBAh2Hdan7NIzEgdctBKZbXWYUyDd4aXdZp3TPK8DPt6mFahD9wNc4O%2F0T30xFzj09V5mnnoMKzoAB4D%2FV%2F5uEn6QsZ92VgoYCA1T4zstUnCk5KgubLNSYDOKuLQ30jPXoRYV60QoMmSdlkBOVAp%2FCw0UyZB9xfJsvlUSjrXp72zHIo4Wt%2F%2B5sFBB3eT1qIlL9t9%2FMhuiBeiwC0gDyEqOTMPPfmL0GOqUBhF3RZpAvurbHiLAYr78ix8ltf%2BpUQ6bPX%2Bpl9My4%2BNHw1OHAZbWot3LcxZxPErGrnv3OQOeKd%2BjN40XU2reEXJHupNOtM1YyExQW%2FVMmgIgFO3T8xttCLAYsnaXuHXN5eaNZENDD5JTUUwtmW46L4Qix2XFQriFe1A6Lyp4%2FJHY%2Fqj6V1QLQnjAaSKGafGp3J0LMklxGMbmASyBlEgtf5D8z2vb4&X-Amz-Signature=3871d1dc512ce03aedb0002eaa05ba503dfb7d5dea410b54b4062ffdab403b1a&X-Amz-SignedHeaders=host&x-id=GetObject)
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


