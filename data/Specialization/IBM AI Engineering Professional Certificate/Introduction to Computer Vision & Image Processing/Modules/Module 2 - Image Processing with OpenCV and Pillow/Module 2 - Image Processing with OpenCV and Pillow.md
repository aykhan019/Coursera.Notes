

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WYHKA7H6%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191125Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGNUqnQ3cPRLxyBIVis5Z2gff70AmbUvriaZ8lb6ri8BAiEAwYez6DoXEH0725j0yKu%2BYcbqGwNEe37MoARPRj8JbC4qiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBxnUSTmRSiAREq25SrcA6zFL9ocR1txcMzbJeE9pSqTjhUSe7XVUDBVz4wJ9tKY5fzW3lctZXF%2BPqpUeHVcfGizrDbTbEGRBGhbkX2pxxxOFq6J7rDharGL%2Bx0rV%2FUxAvEhWyzqFF%2FDAiX1QeoCnXxeSWujzBBJG8T0%2FuoYZ0D%2FhujwtqEyzR4wT2UC4OnBpMEyvSUl5aKeI79SQyvNif3AfebRV2Am84wl4k%2FRUB%2B%2FDnsha7xUdgKgAItOgJwF1kXLEMbE9jf%2FsgdDLgVsmo9603x%2B0tbyRTX2HxQov8A%2Fftz7Ty582JOR5TbGWs8JnsuW2IIBNym6hsRAsiViB5a%2BY6UZGqTIiJEbMH3uva4Hp8sHBJtXKAiN5UeziWcn9woHthPhCjE%2FykBhe6s5XMq71Dnurbv2MmMx%2BOojEskxsxXRVYjIz88Rv%2FC%2Fm%2BRfcTvQL%2FByRJECSK4eTTuHRElBOAs1DGwwYyem24THSh1fosbfVf2HjsgUbGSv%2FRdUXfYZ13lZiNX5%2FSBGwxUL4LMQtkthurLkhlINATI%2Fz9tyH65xqdqEd9BUbnotvg5p7LRgD%2BirAHesvXo8SseVZgQwmNZ6bG51lhu61v9WCXspHEPnJNF62UiGg6Flp28%2BBVcP9sSB0FG%2BzNVrMIGO77wGOqUBCEzR4%2FTdHs%2FXejKPpQVLrs1ndJZ0iGOX5sEsXMlrbU2wsegBKGOW8n75M9tYU1UnorMK4IM90GVnzxoTc9zCrI43NP%2BVHRj0NdBNnIDk2vw%2BeHqNR98BTtrDheXmCqU7V6Ckzpf%2FYgJQjuhqzHPckflpqBgfQ4ceW%2F6xqWrLl%2FWHcEZodPUN5Q9q2fDjf%2BbiE9bCdUsAkSKet3cVoPh9VcS1o%2F5d&X-Amz-Signature=e4db9b1205a40f3ac8556130048f6ddf8e2a7d06f19a7a7b2ff9b56604bc044b&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664SAELFG5%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191125Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBzeL6EsO89J8k4a5vZ8Soelc0U4oGZDmjoaQnz22p2xAiEAylpAd4C61DdrQKnj%2BAs8ryVoaWmZnrGm5J5WY4ikPyMqiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEuKZzDYm%2BEksu2%2BySrcA%2BgWyqbEl%2FGEwRNJ7bIj7htp%2BCSG94m0l30Zx1w7OVpbIEkwK6Bf2mHPGD2YjDHp0%2FM8Y3Br54mBOn7%2B0wbc2IyVvh0FkYpW2T97NoeljbalxlVFtYm5LyBRSkY3bTGO7C6C%2Ff5%2FetVbjU7cBQxm09SU%2FPCWtgrS3SjaT0SzWAbO3KuulD7lq%2BFRz28syAcLEAPK2EOk%2BeYI90UVJDOMOist8zS%2FqVt3Z87Qs3Hg1Vs7cjFUpqi%2FG1vIKouqUOrj7A7s6vzgXN4vNsUiikAL293Kx0m8aSsPJx0t3cUybw%2F0L5bfOGqCThOQfRaEmgxqh8CxGpu1165fvK8l%2FSEn7QKvW1AuEdzLPrC0aIdD%2BpcHNBL%2Fk5UElj4cYihrJ7hT%2BIXN0HliaoVrqPDHX1Rc24OrE3waxcSTatLlk7WWQ5PGyljjFJyw9l35L6lTPXlTryS5nvrL%2Fw4Zyj4K0VBzXKGZf1AF5%2BJasFuwMo1NbubWGWKz3WsEUuhVEdju92pjQvb%2FttiYCHRlD5JYyWsZvpD72etRranjGpzotiFtG1KNpWaS9cnk4BpiXyEQRUmC%2Bptm4sjH%2BUT5mUiNuSz3%2BXdg0QO5%2FDzqhn23IfShQCh7g3SWyLS0bzQANcbCMJyO77wGOqUBL%2BDXalM00GaUe8TSbvjRL%2FwqFqEFFP2mZV%2BZARw0M10yoC8hD15LbznHAAtL88royamr7MMOO650hLNr8ydyE9ioIHrlvO3PyLLkLvcbEtzanZEUMx36lo8k%2BmbVXJdkrxdC1ixReGrX5yDDc8Hrk2ogcvqbUI%2B%2BVwm4stfS6b8QI3F3qGpU2Gy%2Beu%2BZJZWf%2B6ltfy%2F6Fe7lxwRl6%2FznplXHVYHj&X-Amz-Signature=1087a39feb3640e1dc69cae488cef1425c5ebd0a34029bae4929c885e3a8f761&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664SAELFG5%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191125Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBzeL6EsO89J8k4a5vZ8Soelc0U4oGZDmjoaQnz22p2xAiEAylpAd4C61DdrQKnj%2BAs8ryVoaWmZnrGm5J5WY4ikPyMqiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEuKZzDYm%2BEksu2%2BySrcA%2BgWyqbEl%2FGEwRNJ7bIj7htp%2BCSG94m0l30Zx1w7OVpbIEkwK6Bf2mHPGD2YjDHp0%2FM8Y3Br54mBOn7%2B0wbc2IyVvh0FkYpW2T97NoeljbalxlVFtYm5LyBRSkY3bTGO7C6C%2Ff5%2FetVbjU7cBQxm09SU%2FPCWtgrS3SjaT0SzWAbO3KuulD7lq%2BFRz28syAcLEAPK2EOk%2BeYI90UVJDOMOist8zS%2FqVt3Z87Qs3Hg1Vs7cjFUpqi%2FG1vIKouqUOrj7A7s6vzgXN4vNsUiikAL293Kx0m8aSsPJx0t3cUybw%2F0L5bfOGqCThOQfRaEmgxqh8CxGpu1165fvK8l%2FSEn7QKvW1AuEdzLPrC0aIdD%2BpcHNBL%2Fk5UElj4cYihrJ7hT%2BIXN0HliaoVrqPDHX1Rc24OrE3waxcSTatLlk7WWQ5PGyljjFJyw9l35L6lTPXlTryS5nvrL%2Fw4Zyj4K0VBzXKGZf1AF5%2BJasFuwMo1NbubWGWKz3WsEUuhVEdju92pjQvb%2FttiYCHRlD5JYyWsZvpD72etRranjGpzotiFtG1KNpWaS9cnk4BpiXyEQRUmC%2Bptm4sjH%2BUT5mUiNuSz3%2BXdg0QO5%2FDzqhn23IfShQCh7g3SWyLS0bzQANcbCMJyO77wGOqUBL%2BDXalM00GaUe8TSbvjRL%2FwqFqEFFP2mZV%2BZARw0M10yoC8hD15LbznHAAtL88royamr7MMOO650hLNr8ydyE9ioIHrlvO3PyLLkLvcbEtzanZEUMx36lo8k%2BmbVXJdkrxdC1ixReGrX5yDDc8Hrk2ogcvqbUI%2B%2BVwm4stfS6b8QI3F3qGpU2Gy%2Beu%2BZJZWf%2B6ltfy%2F6Fe7lxwRl6%2FznplXHVYHj&X-Amz-Signature=57ed76c4874a8e81d9f503d08305f4ded735f167125dec1969a4647baca41d90&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664SAELFG5%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191125Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBzeL6EsO89J8k4a5vZ8Soelc0U4oGZDmjoaQnz22p2xAiEAylpAd4C61DdrQKnj%2BAs8ryVoaWmZnrGm5J5WY4ikPyMqiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEuKZzDYm%2BEksu2%2BySrcA%2BgWyqbEl%2FGEwRNJ7bIj7htp%2BCSG94m0l30Zx1w7OVpbIEkwK6Bf2mHPGD2YjDHp0%2FM8Y3Br54mBOn7%2B0wbc2IyVvh0FkYpW2T97NoeljbalxlVFtYm5LyBRSkY3bTGO7C6C%2Ff5%2FetVbjU7cBQxm09SU%2FPCWtgrS3SjaT0SzWAbO3KuulD7lq%2BFRz28syAcLEAPK2EOk%2BeYI90UVJDOMOist8zS%2FqVt3Z87Qs3Hg1Vs7cjFUpqi%2FG1vIKouqUOrj7A7s6vzgXN4vNsUiikAL293Kx0m8aSsPJx0t3cUybw%2F0L5bfOGqCThOQfRaEmgxqh8CxGpu1165fvK8l%2FSEn7QKvW1AuEdzLPrC0aIdD%2BpcHNBL%2Fk5UElj4cYihrJ7hT%2BIXN0HliaoVrqPDHX1Rc24OrE3waxcSTatLlk7WWQ5PGyljjFJyw9l35L6lTPXlTryS5nvrL%2Fw4Zyj4K0VBzXKGZf1AF5%2BJasFuwMo1NbubWGWKz3WsEUuhVEdju92pjQvb%2FttiYCHRlD5JYyWsZvpD72etRranjGpzotiFtG1KNpWaS9cnk4BpiXyEQRUmC%2Bptm4sjH%2BUT5mUiNuSz3%2BXdg0QO5%2FDzqhn23IfShQCh7g3SWyLS0bzQANcbCMJyO77wGOqUBL%2BDXalM00GaUe8TSbvjRL%2FwqFqEFFP2mZV%2BZARw0M10yoC8hD15LbznHAAtL88royamr7MMOO650hLNr8ydyE9ioIHrlvO3PyLLkLvcbEtzanZEUMx36lo8k%2BmbVXJdkrxdC1ixReGrX5yDDc8Hrk2ogcvqbUI%2B%2BVwm4stfS6b8QI3F3qGpU2Gy%2Beu%2BZJZWf%2B6ltfy%2F6Fe7lxwRl6%2FznplXHVYHj&X-Amz-Signature=5ed035bb0f25ee197f539318ba9872a1665f5e740fd2cca511d82eeb8ed8168e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664SAELFG5%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191125Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBzeL6EsO89J8k4a5vZ8Soelc0U4oGZDmjoaQnz22p2xAiEAylpAd4C61DdrQKnj%2BAs8ryVoaWmZnrGm5J5WY4ikPyMqiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEuKZzDYm%2BEksu2%2BySrcA%2BgWyqbEl%2FGEwRNJ7bIj7htp%2BCSG94m0l30Zx1w7OVpbIEkwK6Bf2mHPGD2YjDHp0%2FM8Y3Br54mBOn7%2B0wbc2IyVvh0FkYpW2T97NoeljbalxlVFtYm5LyBRSkY3bTGO7C6C%2Ff5%2FetVbjU7cBQxm09SU%2FPCWtgrS3SjaT0SzWAbO3KuulD7lq%2BFRz28syAcLEAPK2EOk%2BeYI90UVJDOMOist8zS%2FqVt3Z87Qs3Hg1Vs7cjFUpqi%2FG1vIKouqUOrj7A7s6vzgXN4vNsUiikAL293Kx0m8aSsPJx0t3cUybw%2F0L5bfOGqCThOQfRaEmgxqh8CxGpu1165fvK8l%2FSEn7QKvW1AuEdzLPrC0aIdD%2BpcHNBL%2Fk5UElj4cYihrJ7hT%2BIXN0HliaoVrqPDHX1Rc24OrE3waxcSTatLlk7WWQ5PGyljjFJyw9l35L6lTPXlTryS5nvrL%2Fw4Zyj4K0VBzXKGZf1AF5%2BJasFuwMo1NbubWGWKz3WsEUuhVEdju92pjQvb%2FttiYCHRlD5JYyWsZvpD72etRranjGpzotiFtG1KNpWaS9cnk4BpiXyEQRUmC%2Bptm4sjH%2BUT5mUiNuSz3%2BXdg0QO5%2FDzqhn23IfShQCh7g3SWyLS0bzQANcbCMJyO77wGOqUBL%2BDXalM00GaUe8TSbvjRL%2FwqFqEFFP2mZV%2BZARw0M10yoC8hD15LbznHAAtL88royamr7MMOO650hLNr8ydyE9ioIHrlvO3PyLLkLvcbEtzanZEUMx36lo8k%2BmbVXJdkrxdC1ixReGrX5yDDc8Hrk2ogcvqbUI%2B%2BVwm4stfS6b8QI3F3qGpU2Gy%2Beu%2BZJZWf%2B6ltfy%2F6Fe7lxwRl6%2FznplXHVYHj&X-Amz-Signature=dd0238f108f938b97e816eaaea2b9146a57138f1b46d0634055a5b1a071ae8e7&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664SAELFG5%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191125Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBzeL6EsO89J8k4a5vZ8Soelc0U4oGZDmjoaQnz22p2xAiEAylpAd4C61DdrQKnj%2BAs8ryVoaWmZnrGm5J5WY4ikPyMqiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEuKZzDYm%2BEksu2%2BySrcA%2BgWyqbEl%2FGEwRNJ7bIj7htp%2BCSG94m0l30Zx1w7OVpbIEkwK6Bf2mHPGD2YjDHp0%2FM8Y3Br54mBOn7%2B0wbc2IyVvh0FkYpW2T97NoeljbalxlVFtYm5LyBRSkY3bTGO7C6C%2Ff5%2FetVbjU7cBQxm09SU%2FPCWtgrS3SjaT0SzWAbO3KuulD7lq%2BFRz28syAcLEAPK2EOk%2BeYI90UVJDOMOist8zS%2FqVt3Z87Qs3Hg1Vs7cjFUpqi%2FG1vIKouqUOrj7A7s6vzgXN4vNsUiikAL293Kx0m8aSsPJx0t3cUybw%2F0L5bfOGqCThOQfRaEmgxqh8CxGpu1165fvK8l%2FSEn7QKvW1AuEdzLPrC0aIdD%2BpcHNBL%2Fk5UElj4cYihrJ7hT%2BIXN0HliaoVrqPDHX1Rc24OrE3waxcSTatLlk7WWQ5PGyljjFJyw9l35L6lTPXlTryS5nvrL%2Fw4Zyj4K0VBzXKGZf1AF5%2BJasFuwMo1NbubWGWKz3WsEUuhVEdju92pjQvb%2FttiYCHRlD5JYyWsZvpD72etRranjGpzotiFtG1KNpWaS9cnk4BpiXyEQRUmC%2Bptm4sjH%2BUT5mUiNuSz3%2BXdg0QO5%2FDzqhn23IfShQCh7g3SWyLS0bzQANcbCMJyO77wGOqUBL%2BDXalM00GaUe8TSbvjRL%2FwqFqEFFP2mZV%2BZARw0M10yoC8hD15LbznHAAtL88royamr7MMOO650hLNr8ydyE9ioIHrlvO3PyLLkLvcbEtzanZEUMx36lo8k%2BmbVXJdkrxdC1ixReGrX5yDDc8Hrk2ogcvqbUI%2B%2BVwm4stfS6b8QI3F3qGpU2Gy%2Beu%2BZJZWf%2B6ltfy%2F6Fe7lxwRl6%2FznplXHVYHj&X-Amz-Signature=69afa1a58db2151bad9b98c441f13a1f5f0f4401a6098fcdf2866ae03e5344bc&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WYHKA7H6%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191125Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGNUqnQ3cPRLxyBIVis5Z2gff70AmbUvriaZ8lb6ri8BAiEAwYez6DoXEH0725j0yKu%2BYcbqGwNEe37MoARPRj8JbC4qiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBxnUSTmRSiAREq25SrcA6zFL9ocR1txcMzbJeE9pSqTjhUSe7XVUDBVz4wJ9tKY5fzW3lctZXF%2BPqpUeHVcfGizrDbTbEGRBGhbkX2pxxxOFq6J7rDharGL%2Bx0rV%2FUxAvEhWyzqFF%2FDAiX1QeoCnXxeSWujzBBJG8T0%2FuoYZ0D%2FhujwtqEyzR4wT2UC4OnBpMEyvSUl5aKeI79SQyvNif3AfebRV2Am84wl4k%2FRUB%2B%2FDnsha7xUdgKgAItOgJwF1kXLEMbE9jf%2FsgdDLgVsmo9603x%2B0tbyRTX2HxQov8A%2Fftz7Ty582JOR5TbGWs8JnsuW2IIBNym6hsRAsiViB5a%2BY6UZGqTIiJEbMH3uva4Hp8sHBJtXKAiN5UeziWcn9woHthPhCjE%2FykBhe6s5XMq71Dnurbv2MmMx%2BOojEskxsxXRVYjIz88Rv%2FC%2Fm%2BRfcTvQL%2FByRJECSK4eTTuHRElBOAs1DGwwYyem24THSh1fosbfVf2HjsgUbGSv%2FRdUXfYZ13lZiNX5%2FSBGwxUL4LMQtkthurLkhlINATI%2Fz9tyH65xqdqEd9BUbnotvg5p7LRgD%2BirAHesvXo8SseVZgQwmNZ6bG51lhu61v9WCXspHEPnJNF62UiGg6Flp28%2BBVcP9sSB0FG%2BzNVrMIGO77wGOqUBCEzR4%2FTdHs%2FXejKPpQVLrs1ndJZ0iGOX5sEsXMlrbU2wsegBKGOW8n75M9tYU1UnorMK4IM90GVnzxoTc9zCrI43NP%2BVHRj0NdBNnIDk2vw%2BeHqNR98BTtrDheXmCqU7V6Ckzpf%2FYgJQjuhqzHPckflpqBgfQ4ceW%2F6xqWrLl%2FWHcEZodPUN5Q9q2fDjf%2BbiE9bCdUsAkSKet3cVoPh9VcS1o%2F5d&X-Amz-Signature=812e76871ab99a89c2137ad19327be54d6c993f4b6a911649a6fec5e9a1924f5&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WYHKA7H6%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191125Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGNUqnQ3cPRLxyBIVis5Z2gff70AmbUvriaZ8lb6ri8BAiEAwYez6DoXEH0725j0yKu%2BYcbqGwNEe37MoARPRj8JbC4qiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBxnUSTmRSiAREq25SrcA6zFL9ocR1txcMzbJeE9pSqTjhUSe7XVUDBVz4wJ9tKY5fzW3lctZXF%2BPqpUeHVcfGizrDbTbEGRBGhbkX2pxxxOFq6J7rDharGL%2Bx0rV%2FUxAvEhWyzqFF%2FDAiX1QeoCnXxeSWujzBBJG8T0%2FuoYZ0D%2FhujwtqEyzR4wT2UC4OnBpMEyvSUl5aKeI79SQyvNif3AfebRV2Am84wl4k%2FRUB%2B%2FDnsha7xUdgKgAItOgJwF1kXLEMbE9jf%2FsgdDLgVsmo9603x%2B0tbyRTX2HxQov8A%2Fftz7Ty582JOR5TbGWs8JnsuW2IIBNym6hsRAsiViB5a%2BY6UZGqTIiJEbMH3uva4Hp8sHBJtXKAiN5UeziWcn9woHthPhCjE%2FykBhe6s5XMq71Dnurbv2MmMx%2BOojEskxsxXRVYjIz88Rv%2FC%2Fm%2BRfcTvQL%2FByRJECSK4eTTuHRElBOAs1DGwwYyem24THSh1fosbfVf2HjsgUbGSv%2FRdUXfYZ13lZiNX5%2FSBGwxUL4LMQtkthurLkhlINATI%2Fz9tyH65xqdqEd9BUbnotvg5p7LRgD%2BirAHesvXo8SseVZgQwmNZ6bG51lhu61v9WCXspHEPnJNF62UiGg6Flp28%2BBVcP9sSB0FG%2BzNVrMIGO77wGOqUBCEzR4%2FTdHs%2FXejKPpQVLrs1ndJZ0iGOX5sEsXMlrbU2wsegBKGOW8n75M9tYU1UnorMK4IM90GVnzxoTc9zCrI43NP%2BVHRj0NdBNnIDk2vw%2BeHqNR98BTtrDheXmCqU7V6Ckzpf%2FYgJQjuhqzHPckflpqBgfQ4ceW%2F6xqWrLl%2FWHcEZodPUN5Q9q2fDjf%2BbiE9bCdUsAkSKet3cVoPh9VcS1o%2F5d&X-Amz-Signature=b55d23e55957028e6945811508d6f243b162ed9f93ecaa6476018404f1dcfaa9&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WYHKA7H6%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191125Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGNUqnQ3cPRLxyBIVis5Z2gff70AmbUvriaZ8lb6ri8BAiEAwYez6DoXEH0725j0yKu%2BYcbqGwNEe37MoARPRj8JbC4qiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBxnUSTmRSiAREq25SrcA6zFL9ocR1txcMzbJeE9pSqTjhUSe7XVUDBVz4wJ9tKY5fzW3lctZXF%2BPqpUeHVcfGizrDbTbEGRBGhbkX2pxxxOFq6J7rDharGL%2Bx0rV%2FUxAvEhWyzqFF%2FDAiX1QeoCnXxeSWujzBBJG8T0%2FuoYZ0D%2FhujwtqEyzR4wT2UC4OnBpMEyvSUl5aKeI79SQyvNif3AfebRV2Am84wl4k%2FRUB%2B%2FDnsha7xUdgKgAItOgJwF1kXLEMbE9jf%2FsgdDLgVsmo9603x%2B0tbyRTX2HxQov8A%2Fftz7Ty582JOR5TbGWs8JnsuW2IIBNym6hsRAsiViB5a%2BY6UZGqTIiJEbMH3uva4Hp8sHBJtXKAiN5UeziWcn9woHthPhCjE%2FykBhe6s5XMq71Dnurbv2MmMx%2BOojEskxsxXRVYjIz88Rv%2FC%2Fm%2BRfcTvQL%2FByRJECSK4eTTuHRElBOAs1DGwwYyem24THSh1fosbfVf2HjsgUbGSv%2FRdUXfYZ13lZiNX5%2FSBGwxUL4LMQtkthurLkhlINATI%2Fz9tyH65xqdqEd9BUbnotvg5p7LRgD%2BirAHesvXo8SseVZgQwmNZ6bG51lhu61v9WCXspHEPnJNF62UiGg6Flp28%2BBVcP9sSB0FG%2BzNVrMIGO77wGOqUBCEzR4%2FTdHs%2FXejKPpQVLrs1ndJZ0iGOX5sEsXMlrbU2wsegBKGOW8n75M9tYU1UnorMK4IM90GVnzxoTc9zCrI43NP%2BVHRj0NdBNnIDk2vw%2BeHqNR98BTtrDheXmCqU7V6Ckzpf%2FYgJQjuhqzHPckflpqBgfQ4ceW%2F6xqWrLl%2FWHcEZodPUN5Q9q2fDjf%2BbiE9bCdUsAkSKet3cVoPh9VcS1o%2F5d&X-Amz-Signature=5bdd91333edc60a5426e6bf6252a0b8bd970c5a0a2324afb759efad1ff22eda8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WYHKA7H6%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191125Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGNUqnQ3cPRLxyBIVis5Z2gff70AmbUvriaZ8lb6ri8BAiEAwYez6DoXEH0725j0yKu%2BYcbqGwNEe37MoARPRj8JbC4qiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBxnUSTmRSiAREq25SrcA6zFL9ocR1txcMzbJeE9pSqTjhUSe7XVUDBVz4wJ9tKY5fzW3lctZXF%2BPqpUeHVcfGizrDbTbEGRBGhbkX2pxxxOFq6J7rDharGL%2Bx0rV%2FUxAvEhWyzqFF%2FDAiX1QeoCnXxeSWujzBBJG8T0%2FuoYZ0D%2FhujwtqEyzR4wT2UC4OnBpMEyvSUl5aKeI79SQyvNif3AfebRV2Am84wl4k%2FRUB%2B%2FDnsha7xUdgKgAItOgJwF1kXLEMbE9jf%2FsgdDLgVsmo9603x%2B0tbyRTX2HxQov8A%2Fftz7Ty582JOR5TbGWs8JnsuW2IIBNym6hsRAsiViB5a%2BY6UZGqTIiJEbMH3uva4Hp8sHBJtXKAiN5UeziWcn9woHthPhCjE%2FykBhe6s5XMq71Dnurbv2MmMx%2BOojEskxsxXRVYjIz88Rv%2FC%2Fm%2BRfcTvQL%2FByRJECSK4eTTuHRElBOAs1DGwwYyem24THSh1fosbfVf2HjsgUbGSv%2FRdUXfYZ13lZiNX5%2FSBGwxUL4LMQtkthurLkhlINATI%2Fz9tyH65xqdqEd9BUbnotvg5p7LRgD%2BirAHesvXo8SseVZgQwmNZ6bG51lhu61v9WCXspHEPnJNF62UiGg6Flp28%2BBVcP9sSB0FG%2BzNVrMIGO77wGOqUBCEzR4%2FTdHs%2FXejKPpQVLrs1ndJZ0iGOX5sEsXMlrbU2wsegBKGOW8n75M9tYU1UnorMK4IM90GVnzxoTc9zCrI43NP%2BVHRj0NdBNnIDk2vw%2BeHqNR98BTtrDheXmCqU7V6Ckzpf%2FYgJQjuhqzHPckflpqBgfQ4ceW%2F6xqWrLl%2FWHcEZodPUN5Q9q2fDjf%2BbiE9bCdUsAkSKet3cVoPh9VcS1o%2F5d&X-Amz-Signature=84cb134b3d03cc7bb98421bff9a9b4cee45e91546538f685c877205e81ad642c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WYHKA7H6%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191125Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGNUqnQ3cPRLxyBIVis5Z2gff70AmbUvriaZ8lb6ri8BAiEAwYez6DoXEH0725j0yKu%2BYcbqGwNEe37MoARPRj8JbC4qiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBxnUSTmRSiAREq25SrcA6zFL9ocR1txcMzbJeE9pSqTjhUSe7XVUDBVz4wJ9tKY5fzW3lctZXF%2BPqpUeHVcfGizrDbTbEGRBGhbkX2pxxxOFq6J7rDharGL%2Bx0rV%2FUxAvEhWyzqFF%2FDAiX1QeoCnXxeSWujzBBJG8T0%2FuoYZ0D%2FhujwtqEyzR4wT2UC4OnBpMEyvSUl5aKeI79SQyvNif3AfebRV2Am84wl4k%2FRUB%2B%2FDnsha7xUdgKgAItOgJwF1kXLEMbE9jf%2FsgdDLgVsmo9603x%2B0tbyRTX2HxQov8A%2Fftz7Ty582JOR5TbGWs8JnsuW2IIBNym6hsRAsiViB5a%2BY6UZGqTIiJEbMH3uva4Hp8sHBJtXKAiN5UeziWcn9woHthPhCjE%2FykBhe6s5XMq71Dnurbv2MmMx%2BOojEskxsxXRVYjIz88Rv%2FC%2Fm%2BRfcTvQL%2FByRJECSK4eTTuHRElBOAs1DGwwYyem24THSh1fosbfVf2HjsgUbGSv%2FRdUXfYZ13lZiNX5%2FSBGwxUL4LMQtkthurLkhlINATI%2Fz9tyH65xqdqEd9BUbnotvg5p7LRgD%2BirAHesvXo8SseVZgQwmNZ6bG51lhu61v9WCXspHEPnJNF62UiGg6Flp28%2BBVcP9sSB0FG%2BzNVrMIGO77wGOqUBCEzR4%2FTdHs%2FXejKPpQVLrs1ndJZ0iGOX5sEsXMlrbU2wsegBKGOW8n75M9tYU1UnorMK4IM90GVnzxoTc9zCrI43NP%2BVHRj0NdBNnIDk2vw%2BeHqNR98BTtrDheXmCqU7V6Ckzpf%2FYgJQjuhqzHPckflpqBgfQ4ceW%2F6xqWrLl%2FWHcEZodPUN5Q9q2fDjf%2BbiE9bCdUsAkSKet3cVoPh9VcS1o%2F5d&X-Amz-Signature=1307172761271f46e0ecb0f8e3cc7ce5154fa43a1060d7ac411e2763ac0dd593&X-Amz-SignedHeaders=host&x-id=GetObject)
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


