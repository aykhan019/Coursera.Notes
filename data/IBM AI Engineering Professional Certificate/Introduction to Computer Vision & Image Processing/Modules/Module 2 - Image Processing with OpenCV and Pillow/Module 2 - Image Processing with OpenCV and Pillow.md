

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667GACL3SD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIQDo%2Bqr3bsgAUF70Q5iMJ%2FMUbjB2OkymPR3u8YaM9AecTQIgc%2BMW74bxk6jRqL6UzcsFEhOfpV%2FClnebZTyamUs9bQwq%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDKmiAD4l6u4Pwumr%2ByrcA%2Fs0K31WTIrQq4ctF703H%2BQ8xHCRdtfvL20LbHW726NggocvSPkRVLmgLl5e%2FvhQzX7CbtomdsGT8oEySyixwQMa2hsXDkAH2%2BEOovC%2F9gJwxZnJXX0bt%2F3ix2MK20ubTfOA8Q9Zg%2Fl10VxeKty8pRZ%2Fr7aWc9vejtfYJ7w3uLdmk4UaIhGFy9Y%2FEpIrvMwo6YfOvMtdgTjwE099ERsD9OflJ2w8RS2lAQtgjxJWdu2asROKGpXhHRgCAJl8dYNBmS93ZaxFARIo2J45gMm0pKMfIm9mMBClotbLfIbjWl2h6OJf9OP7QtnyVpH6cEfRiPNtLmlfcsUbIFPPsfzXoY6LAn7Sck2dgsp8X3QizorI%2BhrTQeBWz2cvQ4WOXNNYUOSz7M3jy8wbLHnl313nnO0%2B7%2FfjxbXaG98J0g76sSYsNMdxSIzMHZ%2FI5lw3uYKQ%2Fc2QfzGeoR91Ly3nnYsEn0RqeGni5jyWSR4NfrUaGY7CuOQzehkRppkLvFqkE5bJMLhjIDvMt28jKVfmgv4RCQ7J0Te9ONmBNvZzKBaJZn2EB7ygXazS2A2HBWSrghTM8aSSk9ZoAo2mRgmrHpEHMJJvm5t4ZW5khbifLRwQyxmEdekUYrXfjKL%2BHiwCMNP7k70GOqUBlUnlNySg7ydEOKSbcXjAR1ZJN2RrwKvPqNEHkDJtDJCqQjPCamU4SSvp4NlUif8zi9FNtHEm3o0xzSD%2BmQnI4yzvYPd9BYanAKuvTXT2DwRhM9xNamUbft1Bx0QAaxEiwrj%2FjV%2B9Q%2FFULqZ3oFTTRNGbDzuxh7DSMItj1ytBPXRu5Ff%2FTMQlpFE00tlUDHpWwkpH2Oz%2BU%2Fr8nhBaeOuGsTygIRnM&X-Amz-Signature=a746143f23bdcdcc3b526f890bd760ad6a84a3103f52f09aad13dbb32f7eb386&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5ZZC4TD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIF80uq4ugtkpZ%2FRYWBQJr7dlUn4RPN464nQjhbatF3GQAiBXh0bkuO4eN2mNKFVXMuji3WExd8Bal24R2%2BKC1ypI6ir%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIMoJAmuzX1Es7XKksqKtwDSGV8YGLaiaUEgzlX0Kb7EZ1l2KgxsOEQPEQXgMnIiRz1l4ZjlOK3UPk8uym8fGlJZNAw4vTB23MuDJUbytr2s6Lk1nfiCEEJ5XoCdEKqH2WY%2Bqrj4ZJL2KlDrZmcpZ7%2FA%2Fc8KE94NrLOL8lb0talnxP01cZSVPdwp%2BIdA2YWCOAFQ1W34b%2Fd72PjPF3sOs78kEEEJqKfcoO9styZpjzLFeuj9L%2BWrP4HHslrnpW72nyyuxgczOVFSu9UF%2FuZsGGVagRORRrVMAd%2F65fx3H7ZzegqWmEa1DGsQDEnW%2B%2Byr8NVViIJB0WJ0Zi2wixBXQ0L3qNgwzFDiVb8%2FSmf%2FuzuACl4criNMVAi0xisJmi5N4CaD%2BNCIo%2BvGFXQ3qEgQinkvSgWQxK1FGpvWOO4YL1rnRBLRmk0lI1onhG1BqcHNnoDCCPdkpl2bvTKZ9lEWKuCfUzqPyN664NMBUpYl46NczyeVStGAfU%2FPLq%2Fhm69niAEPdDVsp9ExBzdz9meg7KygpkpWkf3h2tTTuD3vrGPa5riN9psySV8uF%2BHZmJiZExTdhX%2FMJjbdZCvVF6qI4Z2dSTvJCrTnQuA6bKqUlsQu2Y5NCuOPP4LFUXo6MYaQtnI3pExBbC2JYHb9UgwmPuTvQY6pgGw7Ud2M7brW%2B319AhfZ3p%2Fbj1IMY1Q6DZpr4fWf09H8jPQ4Y7%2Bmm1G9v7T37SWTfs3mRG75x12awEfCeZsdHIYCaQmIHJRIShVTaj5%2FSxAU%2B1OIi9Hv1DDGoUPpkFixsvR50z3MpW9ZT7XHPoYx1hYDjbZlKv7z2tILty4iChzqxJ65zw7whfbkAuEx6c8bDtzWNrYXBRgRWRFlefTKlX0kgv7Q3p0&X-Amz-Signature=339df3981a7f133ca4e39681258b5efa06245298faffc509be38be9c711a81da&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5ZZC4TD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIF80uq4ugtkpZ%2FRYWBQJr7dlUn4RPN464nQjhbatF3GQAiBXh0bkuO4eN2mNKFVXMuji3WExd8Bal24R2%2BKC1ypI6ir%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIMoJAmuzX1Es7XKksqKtwDSGV8YGLaiaUEgzlX0Kb7EZ1l2KgxsOEQPEQXgMnIiRz1l4ZjlOK3UPk8uym8fGlJZNAw4vTB23MuDJUbytr2s6Lk1nfiCEEJ5XoCdEKqH2WY%2Bqrj4ZJL2KlDrZmcpZ7%2FA%2Fc8KE94NrLOL8lb0talnxP01cZSVPdwp%2BIdA2YWCOAFQ1W34b%2Fd72PjPF3sOs78kEEEJqKfcoO9styZpjzLFeuj9L%2BWrP4HHslrnpW72nyyuxgczOVFSu9UF%2FuZsGGVagRORRrVMAd%2F65fx3H7ZzegqWmEa1DGsQDEnW%2B%2Byr8NVViIJB0WJ0Zi2wixBXQ0L3qNgwzFDiVb8%2FSmf%2FuzuACl4criNMVAi0xisJmi5N4CaD%2BNCIo%2BvGFXQ3qEgQinkvSgWQxK1FGpvWOO4YL1rnRBLRmk0lI1onhG1BqcHNnoDCCPdkpl2bvTKZ9lEWKuCfUzqPyN664NMBUpYl46NczyeVStGAfU%2FPLq%2Fhm69niAEPdDVsp9ExBzdz9meg7KygpkpWkf3h2tTTuD3vrGPa5riN9psySV8uF%2BHZmJiZExTdhX%2FMJjbdZCvVF6qI4Z2dSTvJCrTnQuA6bKqUlsQu2Y5NCuOPP4LFUXo6MYaQtnI3pExBbC2JYHb9UgwmPuTvQY6pgGw7Ud2M7brW%2B319AhfZ3p%2Fbj1IMY1Q6DZpr4fWf09H8jPQ4Y7%2Bmm1G9v7T37SWTfs3mRG75x12awEfCeZsdHIYCaQmIHJRIShVTaj5%2FSxAU%2B1OIi9Hv1DDGoUPpkFixsvR50z3MpW9ZT7XHPoYx1hYDjbZlKv7z2tILty4iChzqxJ65zw7whfbkAuEx6c8bDtzWNrYXBRgRWRFlefTKlX0kgv7Q3p0&X-Amz-Signature=8fc41e987ba1fa0e34033e2ceb249f89a216b932263acad858e73e4b00c24325&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5ZZC4TD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIF80uq4ugtkpZ%2FRYWBQJr7dlUn4RPN464nQjhbatF3GQAiBXh0bkuO4eN2mNKFVXMuji3WExd8Bal24R2%2BKC1ypI6ir%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIMoJAmuzX1Es7XKksqKtwDSGV8YGLaiaUEgzlX0Kb7EZ1l2KgxsOEQPEQXgMnIiRz1l4ZjlOK3UPk8uym8fGlJZNAw4vTB23MuDJUbytr2s6Lk1nfiCEEJ5XoCdEKqH2WY%2Bqrj4ZJL2KlDrZmcpZ7%2FA%2Fc8KE94NrLOL8lb0talnxP01cZSVPdwp%2BIdA2YWCOAFQ1W34b%2Fd72PjPF3sOs78kEEEJqKfcoO9styZpjzLFeuj9L%2BWrP4HHslrnpW72nyyuxgczOVFSu9UF%2FuZsGGVagRORRrVMAd%2F65fx3H7ZzegqWmEa1DGsQDEnW%2B%2Byr8NVViIJB0WJ0Zi2wixBXQ0L3qNgwzFDiVb8%2FSmf%2FuzuACl4criNMVAi0xisJmi5N4CaD%2BNCIo%2BvGFXQ3qEgQinkvSgWQxK1FGpvWOO4YL1rnRBLRmk0lI1onhG1BqcHNnoDCCPdkpl2bvTKZ9lEWKuCfUzqPyN664NMBUpYl46NczyeVStGAfU%2FPLq%2Fhm69niAEPdDVsp9ExBzdz9meg7KygpkpWkf3h2tTTuD3vrGPa5riN9psySV8uF%2BHZmJiZExTdhX%2FMJjbdZCvVF6qI4Z2dSTvJCrTnQuA6bKqUlsQu2Y5NCuOPP4LFUXo6MYaQtnI3pExBbC2JYHb9UgwmPuTvQY6pgGw7Ud2M7brW%2B319AhfZ3p%2Fbj1IMY1Q6DZpr4fWf09H8jPQ4Y7%2Bmm1G9v7T37SWTfs3mRG75x12awEfCeZsdHIYCaQmIHJRIShVTaj5%2FSxAU%2B1OIi9Hv1DDGoUPpkFixsvR50z3MpW9ZT7XHPoYx1hYDjbZlKv7z2tILty4iChzqxJ65zw7whfbkAuEx6c8bDtzWNrYXBRgRWRFlefTKlX0kgv7Q3p0&X-Amz-Signature=1f9560159bef543c98512db48bc37a1ba711fd6752b320f2de558f66154ec652&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5ZZC4TD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIF80uq4ugtkpZ%2FRYWBQJr7dlUn4RPN464nQjhbatF3GQAiBXh0bkuO4eN2mNKFVXMuji3WExd8Bal24R2%2BKC1ypI6ir%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIMoJAmuzX1Es7XKksqKtwDSGV8YGLaiaUEgzlX0Kb7EZ1l2KgxsOEQPEQXgMnIiRz1l4ZjlOK3UPk8uym8fGlJZNAw4vTB23MuDJUbytr2s6Lk1nfiCEEJ5XoCdEKqH2WY%2Bqrj4ZJL2KlDrZmcpZ7%2FA%2Fc8KE94NrLOL8lb0talnxP01cZSVPdwp%2BIdA2YWCOAFQ1W34b%2Fd72PjPF3sOs78kEEEJqKfcoO9styZpjzLFeuj9L%2BWrP4HHslrnpW72nyyuxgczOVFSu9UF%2FuZsGGVagRORRrVMAd%2F65fx3H7ZzegqWmEa1DGsQDEnW%2B%2Byr8NVViIJB0WJ0Zi2wixBXQ0L3qNgwzFDiVb8%2FSmf%2FuzuACl4criNMVAi0xisJmi5N4CaD%2BNCIo%2BvGFXQ3qEgQinkvSgWQxK1FGpvWOO4YL1rnRBLRmk0lI1onhG1BqcHNnoDCCPdkpl2bvTKZ9lEWKuCfUzqPyN664NMBUpYl46NczyeVStGAfU%2FPLq%2Fhm69niAEPdDVsp9ExBzdz9meg7KygpkpWkf3h2tTTuD3vrGPa5riN9psySV8uF%2BHZmJiZExTdhX%2FMJjbdZCvVF6qI4Z2dSTvJCrTnQuA6bKqUlsQu2Y5NCuOPP4LFUXo6MYaQtnI3pExBbC2JYHb9UgwmPuTvQY6pgGw7Ud2M7brW%2B319AhfZ3p%2Fbj1IMY1Q6DZpr4fWf09H8jPQ4Y7%2Bmm1G9v7T37SWTfs3mRG75x12awEfCeZsdHIYCaQmIHJRIShVTaj5%2FSxAU%2B1OIi9Hv1DDGoUPpkFixsvR50z3MpW9ZT7XHPoYx1hYDjbZlKv7z2tILty4iChzqxJ65zw7whfbkAuEx6c8bDtzWNrYXBRgRWRFlefTKlX0kgv7Q3p0&X-Amz-Signature=aca3d38fd2eaa202af5e2a11740d62fa359c41286d11335d361147d874338225&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5ZZC4TD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIF80uq4ugtkpZ%2FRYWBQJr7dlUn4RPN464nQjhbatF3GQAiBXh0bkuO4eN2mNKFVXMuji3WExd8Bal24R2%2BKC1ypI6ir%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIMoJAmuzX1Es7XKksqKtwDSGV8YGLaiaUEgzlX0Kb7EZ1l2KgxsOEQPEQXgMnIiRz1l4ZjlOK3UPk8uym8fGlJZNAw4vTB23MuDJUbytr2s6Lk1nfiCEEJ5XoCdEKqH2WY%2Bqrj4ZJL2KlDrZmcpZ7%2FA%2Fc8KE94NrLOL8lb0talnxP01cZSVPdwp%2BIdA2YWCOAFQ1W34b%2Fd72PjPF3sOs78kEEEJqKfcoO9styZpjzLFeuj9L%2BWrP4HHslrnpW72nyyuxgczOVFSu9UF%2FuZsGGVagRORRrVMAd%2F65fx3H7ZzegqWmEa1DGsQDEnW%2B%2Byr8NVViIJB0WJ0Zi2wixBXQ0L3qNgwzFDiVb8%2FSmf%2FuzuACl4criNMVAi0xisJmi5N4CaD%2BNCIo%2BvGFXQ3qEgQinkvSgWQxK1FGpvWOO4YL1rnRBLRmk0lI1onhG1BqcHNnoDCCPdkpl2bvTKZ9lEWKuCfUzqPyN664NMBUpYl46NczyeVStGAfU%2FPLq%2Fhm69niAEPdDVsp9ExBzdz9meg7KygpkpWkf3h2tTTuD3vrGPa5riN9psySV8uF%2BHZmJiZExTdhX%2FMJjbdZCvVF6qI4Z2dSTvJCrTnQuA6bKqUlsQu2Y5NCuOPP4LFUXo6MYaQtnI3pExBbC2JYHb9UgwmPuTvQY6pgGw7Ud2M7brW%2B319AhfZ3p%2Fbj1IMY1Q6DZpr4fWf09H8jPQ4Y7%2Bmm1G9v7T37SWTfs3mRG75x12awEfCeZsdHIYCaQmIHJRIShVTaj5%2FSxAU%2B1OIi9Hv1DDGoUPpkFixsvR50z3MpW9ZT7XHPoYx1hYDjbZlKv7z2tILty4iChzqxJ65zw7whfbkAuEx6c8bDtzWNrYXBRgRWRFlefTKlX0kgv7Q3p0&X-Amz-Signature=5688f30fbac03651ddcb31bca1b34c3144887d544d8be0f11945114e28be8182&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667GACL3SD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIQDo%2Bqr3bsgAUF70Q5iMJ%2FMUbjB2OkymPR3u8YaM9AecTQIgc%2BMW74bxk6jRqL6UzcsFEhOfpV%2FClnebZTyamUs9bQwq%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDKmiAD4l6u4Pwumr%2ByrcA%2Fs0K31WTIrQq4ctF703H%2BQ8xHCRdtfvL20LbHW726NggocvSPkRVLmgLl5e%2FvhQzX7CbtomdsGT8oEySyixwQMa2hsXDkAH2%2BEOovC%2F9gJwxZnJXX0bt%2F3ix2MK20ubTfOA8Q9Zg%2Fl10VxeKty8pRZ%2Fr7aWc9vejtfYJ7w3uLdmk4UaIhGFy9Y%2FEpIrvMwo6YfOvMtdgTjwE099ERsD9OflJ2w8RS2lAQtgjxJWdu2asROKGpXhHRgCAJl8dYNBmS93ZaxFARIo2J45gMm0pKMfIm9mMBClotbLfIbjWl2h6OJf9OP7QtnyVpH6cEfRiPNtLmlfcsUbIFPPsfzXoY6LAn7Sck2dgsp8X3QizorI%2BhrTQeBWz2cvQ4WOXNNYUOSz7M3jy8wbLHnl313nnO0%2B7%2FfjxbXaG98J0g76sSYsNMdxSIzMHZ%2FI5lw3uYKQ%2Fc2QfzGeoR91Ly3nnYsEn0RqeGni5jyWSR4NfrUaGY7CuOQzehkRppkLvFqkE5bJMLhjIDvMt28jKVfmgv4RCQ7J0Te9ONmBNvZzKBaJZn2EB7ygXazS2A2HBWSrghTM8aSSk9ZoAo2mRgmrHpEHMJJvm5t4ZW5khbifLRwQyxmEdekUYrXfjKL%2BHiwCMNP7k70GOqUBlUnlNySg7ydEOKSbcXjAR1ZJN2RrwKvPqNEHkDJtDJCqQjPCamU4SSvp4NlUif8zi9FNtHEm3o0xzSD%2BmQnI4yzvYPd9BYanAKuvTXT2DwRhM9xNamUbft1Bx0QAaxEiwrj%2FjV%2B9Q%2FFULqZ3oFTTRNGbDzuxh7DSMItj1ytBPXRu5Ff%2FTMQlpFE00tlUDHpWwkpH2Oz%2BU%2Fr8nhBaeOuGsTygIRnM&X-Amz-Signature=e92a525d8f5fa6b13290f202f9ca32f51157a668d1cf3bffbb3156800e98aee7&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667GACL3SD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIQDo%2Bqr3bsgAUF70Q5iMJ%2FMUbjB2OkymPR3u8YaM9AecTQIgc%2BMW74bxk6jRqL6UzcsFEhOfpV%2FClnebZTyamUs9bQwq%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDKmiAD4l6u4Pwumr%2ByrcA%2Fs0K31WTIrQq4ctF703H%2BQ8xHCRdtfvL20LbHW726NggocvSPkRVLmgLl5e%2FvhQzX7CbtomdsGT8oEySyixwQMa2hsXDkAH2%2BEOovC%2F9gJwxZnJXX0bt%2F3ix2MK20ubTfOA8Q9Zg%2Fl10VxeKty8pRZ%2Fr7aWc9vejtfYJ7w3uLdmk4UaIhGFy9Y%2FEpIrvMwo6YfOvMtdgTjwE099ERsD9OflJ2w8RS2lAQtgjxJWdu2asROKGpXhHRgCAJl8dYNBmS93ZaxFARIo2J45gMm0pKMfIm9mMBClotbLfIbjWl2h6OJf9OP7QtnyVpH6cEfRiPNtLmlfcsUbIFPPsfzXoY6LAn7Sck2dgsp8X3QizorI%2BhrTQeBWz2cvQ4WOXNNYUOSz7M3jy8wbLHnl313nnO0%2B7%2FfjxbXaG98J0g76sSYsNMdxSIzMHZ%2FI5lw3uYKQ%2Fc2QfzGeoR91Ly3nnYsEn0RqeGni5jyWSR4NfrUaGY7CuOQzehkRppkLvFqkE5bJMLhjIDvMt28jKVfmgv4RCQ7J0Te9ONmBNvZzKBaJZn2EB7ygXazS2A2HBWSrghTM8aSSk9ZoAo2mRgmrHpEHMJJvm5t4ZW5khbifLRwQyxmEdekUYrXfjKL%2BHiwCMNP7k70GOqUBlUnlNySg7ydEOKSbcXjAR1ZJN2RrwKvPqNEHkDJtDJCqQjPCamU4SSvp4NlUif8zi9FNtHEm3o0xzSD%2BmQnI4yzvYPd9BYanAKuvTXT2DwRhM9xNamUbft1Bx0QAaxEiwrj%2FjV%2B9Q%2FFULqZ3oFTTRNGbDzuxh7DSMItj1ytBPXRu5Ff%2FTMQlpFE00tlUDHpWwkpH2Oz%2BU%2Fr8nhBaeOuGsTygIRnM&X-Amz-Signature=4222aae9d9146beac0501a7866662beb088e62b62742a5cfaa9b07fb4eef7bce&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667GACL3SD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIQDo%2Bqr3bsgAUF70Q5iMJ%2FMUbjB2OkymPR3u8YaM9AecTQIgc%2BMW74bxk6jRqL6UzcsFEhOfpV%2FClnebZTyamUs9bQwq%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDKmiAD4l6u4Pwumr%2ByrcA%2Fs0K31WTIrQq4ctF703H%2BQ8xHCRdtfvL20LbHW726NggocvSPkRVLmgLl5e%2FvhQzX7CbtomdsGT8oEySyixwQMa2hsXDkAH2%2BEOovC%2F9gJwxZnJXX0bt%2F3ix2MK20ubTfOA8Q9Zg%2Fl10VxeKty8pRZ%2Fr7aWc9vejtfYJ7w3uLdmk4UaIhGFy9Y%2FEpIrvMwo6YfOvMtdgTjwE099ERsD9OflJ2w8RS2lAQtgjxJWdu2asROKGpXhHRgCAJl8dYNBmS93ZaxFARIo2J45gMm0pKMfIm9mMBClotbLfIbjWl2h6OJf9OP7QtnyVpH6cEfRiPNtLmlfcsUbIFPPsfzXoY6LAn7Sck2dgsp8X3QizorI%2BhrTQeBWz2cvQ4WOXNNYUOSz7M3jy8wbLHnl313nnO0%2B7%2FfjxbXaG98J0g76sSYsNMdxSIzMHZ%2FI5lw3uYKQ%2Fc2QfzGeoR91Ly3nnYsEn0RqeGni5jyWSR4NfrUaGY7CuOQzehkRppkLvFqkE5bJMLhjIDvMt28jKVfmgv4RCQ7J0Te9ONmBNvZzKBaJZn2EB7ygXazS2A2HBWSrghTM8aSSk9ZoAo2mRgmrHpEHMJJvm5t4ZW5khbifLRwQyxmEdekUYrXfjKL%2BHiwCMNP7k70GOqUBlUnlNySg7ydEOKSbcXjAR1ZJN2RrwKvPqNEHkDJtDJCqQjPCamU4SSvp4NlUif8zi9FNtHEm3o0xzSD%2BmQnI4yzvYPd9BYanAKuvTXT2DwRhM9xNamUbft1Bx0QAaxEiwrj%2FjV%2B9Q%2FFULqZ3oFTTRNGbDzuxh7DSMItj1ytBPXRu5Ff%2FTMQlpFE00tlUDHpWwkpH2Oz%2BU%2Fr8nhBaeOuGsTygIRnM&X-Amz-Signature=b6d64e9fac1070276c16c9d14841226ea00ae4f736e5b801a8062cd37a173309&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667GACL3SD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIQDo%2Bqr3bsgAUF70Q5iMJ%2FMUbjB2OkymPR3u8YaM9AecTQIgc%2BMW74bxk6jRqL6UzcsFEhOfpV%2FClnebZTyamUs9bQwq%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDKmiAD4l6u4Pwumr%2ByrcA%2Fs0K31WTIrQq4ctF703H%2BQ8xHCRdtfvL20LbHW726NggocvSPkRVLmgLl5e%2FvhQzX7CbtomdsGT8oEySyixwQMa2hsXDkAH2%2BEOovC%2F9gJwxZnJXX0bt%2F3ix2MK20ubTfOA8Q9Zg%2Fl10VxeKty8pRZ%2Fr7aWc9vejtfYJ7w3uLdmk4UaIhGFy9Y%2FEpIrvMwo6YfOvMtdgTjwE099ERsD9OflJ2w8RS2lAQtgjxJWdu2asROKGpXhHRgCAJl8dYNBmS93ZaxFARIo2J45gMm0pKMfIm9mMBClotbLfIbjWl2h6OJf9OP7QtnyVpH6cEfRiPNtLmlfcsUbIFPPsfzXoY6LAn7Sck2dgsp8X3QizorI%2BhrTQeBWz2cvQ4WOXNNYUOSz7M3jy8wbLHnl313nnO0%2B7%2FfjxbXaG98J0g76sSYsNMdxSIzMHZ%2FI5lw3uYKQ%2Fc2QfzGeoR91Ly3nnYsEn0RqeGni5jyWSR4NfrUaGY7CuOQzehkRppkLvFqkE5bJMLhjIDvMt28jKVfmgv4RCQ7J0Te9ONmBNvZzKBaJZn2EB7ygXazS2A2HBWSrghTM8aSSk9ZoAo2mRgmrHpEHMJJvm5t4ZW5khbifLRwQyxmEdekUYrXfjKL%2BHiwCMNP7k70GOqUBlUnlNySg7ydEOKSbcXjAR1ZJN2RrwKvPqNEHkDJtDJCqQjPCamU4SSvp4NlUif8zi9FNtHEm3o0xzSD%2BmQnI4yzvYPd9BYanAKuvTXT2DwRhM9xNamUbft1Bx0QAaxEiwrj%2FjV%2B9Q%2FFULqZ3oFTTRNGbDzuxh7DSMItj1ytBPXRu5Ff%2FTMQlpFE00tlUDHpWwkpH2Oz%2BU%2Fr8nhBaeOuGsTygIRnM&X-Amz-Signature=ad79fe700668c792d28d72c3f3af179fa1b0341068de2f7f011fc81866d99203&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667GACL3SD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIQDo%2Bqr3bsgAUF70Q5iMJ%2FMUbjB2OkymPR3u8YaM9AecTQIgc%2BMW74bxk6jRqL6UzcsFEhOfpV%2FClnebZTyamUs9bQwq%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDKmiAD4l6u4Pwumr%2ByrcA%2Fs0K31WTIrQq4ctF703H%2BQ8xHCRdtfvL20LbHW726NggocvSPkRVLmgLl5e%2FvhQzX7CbtomdsGT8oEySyixwQMa2hsXDkAH2%2BEOovC%2F9gJwxZnJXX0bt%2F3ix2MK20ubTfOA8Q9Zg%2Fl10VxeKty8pRZ%2Fr7aWc9vejtfYJ7w3uLdmk4UaIhGFy9Y%2FEpIrvMwo6YfOvMtdgTjwE099ERsD9OflJ2w8RS2lAQtgjxJWdu2asROKGpXhHRgCAJl8dYNBmS93ZaxFARIo2J45gMm0pKMfIm9mMBClotbLfIbjWl2h6OJf9OP7QtnyVpH6cEfRiPNtLmlfcsUbIFPPsfzXoY6LAn7Sck2dgsp8X3QizorI%2BhrTQeBWz2cvQ4WOXNNYUOSz7M3jy8wbLHnl313nnO0%2B7%2FfjxbXaG98J0g76sSYsNMdxSIzMHZ%2FI5lw3uYKQ%2Fc2QfzGeoR91Ly3nnYsEn0RqeGni5jyWSR4NfrUaGY7CuOQzehkRppkLvFqkE5bJMLhjIDvMt28jKVfmgv4RCQ7J0Te9ONmBNvZzKBaJZn2EB7ygXazS2A2HBWSrghTM8aSSk9ZoAo2mRgmrHpEHMJJvm5t4ZW5khbifLRwQyxmEdekUYrXfjKL%2BHiwCMNP7k70GOqUBlUnlNySg7ydEOKSbcXjAR1ZJN2RrwKvPqNEHkDJtDJCqQjPCamU4SSvp4NlUif8zi9FNtHEm3o0xzSD%2BmQnI4yzvYPd9BYanAKuvTXT2DwRhM9xNamUbft1Bx0QAaxEiwrj%2FjV%2B9Q%2FFULqZ3oFTTRNGbDzuxh7DSMItj1ytBPXRu5Ff%2FTMQlpFE00tlUDHpWwkpH2Oz%2BU%2Fr8nhBaeOuGsTygIRnM&X-Amz-Signature=886ba32618275fa79fc3afe518647b931e1a59bca3176565a60730e3c829269d&X-Amz-SignedHeaders=host&x-id=GetObject)
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


