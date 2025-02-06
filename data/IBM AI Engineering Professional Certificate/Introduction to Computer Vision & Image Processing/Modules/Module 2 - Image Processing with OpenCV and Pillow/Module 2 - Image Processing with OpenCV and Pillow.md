

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TEL5EP7A%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041747Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIQCBrv44dAc4wgnVvsx0M45CP1sRsTokrGqrk3CO8H%2F%2FEAIgENBHeycuY8MNtjFSEqtKMewFDq4wvEjlLFJpDugCdLsq%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDEzJAG2BIgK8lHTOyCrcA4JpQyvjBgU%2BzsHECYLikLkG9Oy9D%2B6gLGIwpuGv%2Feu2w%2Brxv1jAGb57I8v5dO%2B6pL2tJlfR8ajpqHP2AkgUFmpmbicKCDIoUuvE5ezZSUtZYns6LesMaK3%2Ful3Ufn3yzLvTC9O6bioiKlDXFslQn1wjF7%2B%2FqHM5cgH2JtqaE%2B9looBkqNJ1EuTzEHBh3C8ENObJQgXHc4SGPYcpa8Z6glMMM2SloV2evBwYXLFT74U75gkNKqgBsIYc3pCSkPp%2FgRGmKkT%2FvQvux7mubeXQYq2JZR9RYNtO4Em25p2Y6misK5DwG2lcF%2FvAm2hqG4RVzmyVmx%2Ffb%2BypfMJwVqcUo6QsSMWFJLkmIEX6Oh%2BcVRX64B%2BsPoMEYKLeKibDxHHpSFlTxjl4oGAiGfuoaQ%2B9CVrCgR9CGNreyneJhcUAT8%2Bj0guLXPp%2BKmso26c0%2FiOPmvTCNYPihaXSXgVjsO4l2NG76uDilmGC%2FhC5k93QgdWz%2F5HKYv6athySQ4qHoLekEMFblO9Ovcdj%2BODqhSBn80sZw5ew67%2BIzAqaDV31%2BCd2yecK1TOsyq6Qdn6%2FYXOn1AlYOn%2Bf1pymHNhFpnU8aXZ2W3kqxu9YfJa5J5Q4D6p8WKnNc0Aw3SIcBuxLMIrgkL0GOqUB%2Ftp0HK%2BlDBq7pjb6RhsioufsZEDhIszhCLuMtxPJ8%2FXDYnvbw%2FoCBw0As0yTi8Vq7JA7AOQtcWDR3Ix78YAoP045JGXCC%2BCC4sIZVQIVpG0D1cx%2Fc9yYfneRCiv8lZ3OcotCLFOQM%2FbArfUH4NiWuJdYogdTJeji8SsaZZV5tS0Lqy%2BoPzidnGbzig5LGRTPiUF6ZpUpEa3JImKvGoqSylJvGhxz&X-Amz-Signature=d41af73dd9386bdfa11b75be1dc9dd6c4c637398a669981b73074847a6eb8b5b&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662VBE2WAV%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041748Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIQDc9h5QbaOUPSMJwxsPzuWUVKNRQwwJ7ty6KtgijQXrnQIgSQGLrbjee0TbTxS0ZM7US6oZoC%2B8ER1A33aD72ID1nsq%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDC2CFPqcycvPuw%2BLKSrcAxOemelXFbHGD6tjZOJa5QIWlYzaQRLYVzr4Ws%2FbzngWyFkTEbzRA%2FpHunCzxFWeNgOS4GtE9h3bPUrJnxMMT%2F63a2TJEhlMFeICdWGruk23iak1OisTEwACB07GHEq6cRuCOG%2BlQgKTlcKpqxwuHsVGTNZAgpFtljjsmuAkq%2BPtV12tPgy6wyQhvmgJjdQDJcJySgeqSPdf%2FxJFXHj6Q0HiFBN24Pax44IppjxqbU5tzFc4PUiDE9h2eUHyQddGJocykGGdh7NASK4YPo%2BPXrLd43AjFjuNU3eXlfSIqr1EfPQOdLnh%2FvLzWPX8JCJAkygJ3JgF%2Brzo6qUaPDIEencyjEpWeX%2Fqn72uhdrh0bbBi2swEd9%2BgESbfOcUecNrjJiVPx%2B4dD50BMMBcwGnnscozY886sHluotza3OyH6aepIR%2F6axWIwYtSDvYxjjO6v1RbttFwoVT%2B5lXYRFiwb5DxmBXE16crUULa65dcahD0w5LAfiZJt0SkOHW3dyTKD3F0NPUuB2cggz0Za9kllgLRJ%2FzEO0LJ48nGuME912Do7HxrZE7HZh5%2BQ3V8mp7ZiIF8IJXlIDBacslBT%2BL0ysTYERBUcEPMV%2BNvOnxRcI9rLfkTefUgjX0OIy%2FMLbgkL0GOqUBxfnkf%2F%2B5r8zFjotOy2%2BnA7jniKawkARAchlR2r7EVnd6Ecdw5syhrp2uqpF1wrxDrTg%2BNqH1IQ01zkQuIorZHurT6OZR4c2kHQ8p4pnu29nfA5ZhnvY%2BKP9fuEBysDGfLnxuZf5i4mr%2B0nOOlrqEFg%2F0bID5xjKLNe62VKtCjFglA2%2BPMycv2DBDGTGr5EXGNyI%2FBrp14REkRUZQVRwwq3QSE%2F%2Fm&X-Amz-Signature=5652e5c7ccf6b55b65e7ae588e2bdae308082beb73c34190e72e97a1d72d4845&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662VBE2WAV%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041748Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIQDc9h5QbaOUPSMJwxsPzuWUVKNRQwwJ7ty6KtgijQXrnQIgSQGLrbjee0TbTxS0ZM7US6oZoC%2B8ER1A33aD72ID1nsq%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDC2CFPqcycvPuw%2BLKSrcAxOemelXFbHGD6tjZOJa5QIWlYzaQRLYVzr4Ws%2FbzngWyFkTEbzRA%2FpHunCzxFWeNgOS4GtE9h3bPUrJnxMMT%2F63a2TJEhlMFeICdWGruk23iak1OisTEwACB07GHEq6cRuCOG%2BlQgKTlcKpqxwuHsVGTNZAgpFtljjsmuAkq%2BPtV12tPgy6wyQhvmgJjdQDJcJySgeqSPdf%2FxJFXHj6Q0HiFBN24Pax44IppjxqbU5tzFc4PUiDE9h2eUHyQddGJocykGGdh7NASK4YPo%2BPXrLd43AjFjuNU3eXlfSIqr1EfPQOdLnh%2FvLzWPX8JCJAkygJ3JgF%2Brzo6qUaPDIEencyjEpWeX%2Fqn72uhdrh0bbBi2swEd9%2BgESbfOcUecNrjJiVPx%2B4dD50BMMBcwGnnscozY886sHluotza3OyH6aepIR%2F6axWIwYtSDvYxjjO6v1RbttFwoVT%2B5lXYRFiwb5DxmBXE16crUULa65dcahD0w5LAfiZJt0SkOHW3dyTKD3F0NPUuB2cggz0Za9kllgLRJ%2FzEO0LJ48nGuME912Do7HxrZE7HZh5%2BQ3V8mp7ZiIF8IJXlIDBacslBT%2BL0ysTYERBUcEPMV%2BNvOnxRcI9rLfkTefUgjX0OIy%2FMLbgkL0GOqUBxfnkf%2F%2B5r8zFjotOy2%2BnA7jniKawkARAchlR2r7EVnd6Ecdw5syhrp2uqpF1wrxDrTg%2BNqH1IQ01zkQuIorZHurT6OZR4c2kHQ8p4pnu29nfA5ZhnvY%2BKP9fuEBysDGfLnxuZf5i4mr%2B0nOOlrqEFg%2F0bID5xjKLNe62VKtCjFglA2%2BPMycv2DBDGTGr5EXGNyI%2FBrp14REkRUZQVRwwq3QSE%2F%2Fm&X-Amz-Signature=7afcaf3ea8ffc9da61af18d56829b1614a77a34797c2010687f2685cb55c544c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662VBE2WAV%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041748Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIQDc9h5QbaOUPSMJwxsPzuWUVKNRQwwJ7ty6KtgijQXrnQIgSQGLrbjee0TbTxS0ZM7US6oZoC%2B8ER1A33aD72ID1nsq%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDC2CFPqcycvPuw%2BLKSrcAxOemelXFbHGD6tjZOJa5QIWlYzaQRLYVzr4Ws%2FbzngWyFkTEbzRA%2FpHunCzxFWeNgOS4GtE9h3bPUrJnxMMT%2F63a2TJEhlMFeICdWGruk23iak1OisTEwACB07GHEq6cRuCOG%2BlQgKTlcKpqxwuHsVGTNZAgpFtljjsmuAkq%2BPtV12tPgy6wyQhvmgJjdQDJcJySgeqSPdf%2FxJFXHj6Q0HiFBN24Pax44IppjxqbU5tzFc4PUiDE9h2eUHyQddGJocykGGdh7NASK4YPo%2BPXrLd43AjFjuNU3eXlfSIqr1EfPQOdLnh%2FvLzWPX8JCJAkygJ3JgF%2Brzo6qUaPDIEencyjEpWeX%2Fqn72uhdrh0bbBi2swEd9%2BgESbfOcUecNrjJiVPx%2B4dD50BMMBcwGnnscozY886sHluotza3OyH6aepIR%2F6axWIwYtSDvYxjjO6v1RbttFwoVT%2B5lXYRFiwb5DxmBXE16crUULa65dcahD0w5LAfiZJt0SkOHW3dyTKD3F0NPUuB2cggz0Za9kllgLRJ%2FzEO0LJ48nGuME912Do7HxrZE7HZh5%2BQ3V8mp7ZiIF8IJXlIDBacslBT%2BL0ysTYERBUcEPMV%2BNvOnxRcI9rLfkTefUgjX0OIy%2FMLbgkL0GOqUBxfnkf%2F%2B5r8zFjotOy2%2BnA7jniKawkARAchlR2r7EVnd6Ecdw5syhrp2uqpF1wrxDrTg%2BNqH1IQ01zkQuIorZHurT6OZR4c2kHQ8p4pnu29nfA5ZhnvY%2BKP9fuEBysDGfLnxuZf5i4mr%2B0nOOlrqEFg%2F0bID5xjKLNe62VKtCjFglA2%2BPMycv2DBDGTGr5EXGNyI%2FBrp14REkRUZQVRwwq3QSE%2F%2Fm&X-Amz-Signature=8e59d90ecf3740cd0adbe0094cc392a8da2f03a693be18fab62d1b86392e9aec&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662VBE2WAV%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041748Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIQDc9h5QbaOUPSMJwxsPzuWUVKNRQwwJ7ty6KtgijQXrnQIgSQGLrbjee0TbTxS0ZM7US6oZoC%2B8ER1A33aD72ID1nsq%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDC2CFPqcycvPuw%2BLKSrcAxOemelXFbHGD6tjZOJa5QIWlYzaQRLYVzr4Ws%2FbzngWyFkTEbzRA%2FpHunCzxFWeNgOS4GtE9h3bPUrJnxMMT%2F63a2TJEhlMFeICdWGruk23iak1OisTEwACB07GHEq6cRuCOG%2BlQgKTlcKpqxwuHsVGTNZAgpFtljjsmuAkq%2BPtV12tPgy6wyQhvmgJjdQDJcJySgeqSPdf%2FxJFXHj6Q0HiFBN24Pax44IppjxqbU5tzFc4PUiDE9h2eUHyQddGJocykGGdh7NASK4YPo%2BPXrLd43AjFjuNU3eXlfSIqr1EfPQOdLnh%2FvLzWPX8JCJAkygJ3JgF%2Brzo6qUaPDIEencyjEpWeX%2Fqn72uhdrh0bbBi2swEd9%2BgESbfOcUecNrjJiVPx%2B4dD50BMMBcwGnnscozY886sHluotza3OyH6aepIR%2F6axWIwYtSDvYxjjO6v1RbttFwoVT%2B5lXYRFiwb5DxmBXE16crUULa65dcahD0w5LAfiZJt0SkOHW3dyTKD3F0NPUuB2cggz0Za9kllgLRJ%2FzEO0LJ48nGuME912Do7HxrZE7HZh5%2BQ3V8mp7ZiIF8IJXlIDBacslBT%2BL0ysTYERBUcEPMV%2BNvOnxRcI9rLfkTefUgjX0OIy%2FMLbgkL0GOqUBxfnkf%2F%2B5r8zFjotOy2%2BnA7jniKawkARAchlR2r7EVnd6Ecdw5syhrp2uqpF1wrxDrTg%2BNqH1IQ01zkQuIorZHurT6OZR4c2kHQ8p4pnu29nfA5ZhnvY%2BKP9fuEBysDGfLnxuZf5i4mr%2B0nOOlrqEFg%2F0bID5xjKLNe62VKtCjFglA2%2BPMycv2DBDGTGr5EXGNyI%2FBrp14REkRUZQVRwwq3QSE%2F%2Fm&X-Amz-Signature=67a0d12b1913f6a74286accac831b0374a52123c8bbabafdb53cf5e134f0fc47&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662VBE2WAV%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041748Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIQDc9h5QbaOUPSMJwxsPzuWUVKNRQwwJ7ty6KtgijQXrnQIgSQGLrbjee0TbTxS0ZM7US6oZoC%2B8ER1A33aD72ID1nsq%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDC2CFPqcycvPuw%2BLKSrcAxOemelXFbHGD6tjZOJa5QIWlYzaQRLYVzr4Ws%2FbzngWyFkTEbzRA%2FpHunCzxFWeNgOS4GtE9h3bPUrJnxMMT%2F63a2TJEhlMFeICdWGruk23iak1OisTEwACB07GHEq6cRuCOG%2BlQgKTlcKpqxwuHsVGTNZAgpFtljjsmuAkq%2BPtV12tPgy6wyQhvmgJjdQDJcJySgeqSPdf%2FxJFXHj6Q0HiFBN24Pax44IppjxqbU5tzFc4PUiDE9h2eUHyQddGJocykGGdh7NASK4YPo%2BPXrLd43AjFjuNU3eXlfSIqr1EfPQOdLnh%2FvLzWPX8JCJAkygJ3JgF%2Brzo6qUaPDIEencyjEpWeX%2Fqn72uhdrh0bbBi2swEd9%2BgESbfOcUecNrjJiVPx%2B4dD50BMMBcwGnnscozY886sHluotza3OyH6aepIR%2F6axWIwYtSDvYxjjO6v1RbttFwoVT%2B5lXYRFiwb5DxmBXE16crUULa65dcahD0w5LAfiZJt0SkOHW3dyTKD3F0NPUuB2cggz0Za9kllgLRJ%2FzEO0LJ48nGuME912Do7HxrZE7HZh5%2BQ3V8mp7ZiIF8IJXlIDBacslBT%2BL0ysTYERBUcEPMV%2BNvOnxRcI9rLfkTefUgjX0OIy%2FMLbgkL0GOqUBxfnkf%2F%2B5r8zFjotOy2%2BnA7jniKawkARAchlR2r7EVnd6Ecdw5syhrp2uqpF1wrxDrTg%2BNqH1IQ01zkQuIorZHurT6OZR4c2kHQ8p4pnu29nfA5ZhnvY%2BKP9fuEBysDGfLnxuZf5i4mr%2B0nOOlrqEFg%2F0bID5xjKLNe62VKtCjFglA2%2BPMycv2DBDGTGr5EXGNyI%2FBrp14REkRUZQVRwwq3QSE%2F%2Fm&X-Amz-Signature=1b922d1025356de5e39b25a4194816eb587b7ec798b6231f5e32808de35f6fdf&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TEL5EP7A%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041747Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIQCBrv44dAc4wgnVvsx0M45CP1sRsTokrGqrk3CO8H%2F%2FEAIgENBHeycuY8MNtjFSEqtKMewFDq4wvEjlLFJpDugCdLsq%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDEzJAG2BIgK8lHTOyCrcA4JpQyvjBgU%2BzsHECYLikLkG9Oy9D%2B6gLGIwpuGv%2Feu2w%2Brxv1jAGb57I8v5dO%2B6pL2tJlfR8ajpqHP2AkgUFmpmbicKCDIoUuvE5ezZSUtZYns6LesMaK3%2Ful3Ufn3yzLvTC9O6bioiKlDXFslQn1wjF7%2B%2FqHM5cgH2JtqaE%2B9looBkqNJ1EuTzEHBh3C8ENObJQgXHc4SGPYcpa8Z6glMMM2SloV2evBwYXLFT74U75gkNKqgBsIYc3pCSkPp%2FgRGmKkT%2FvQvux7mubeXQYq2JZR9RYNtO4Em25p2Y6misK5DwG2lcF%2FvAm2hqG4RVzmyVmx%2Ffb%2BypfMJwVqcUo6QsSMWFJLkmIEX6Oh%2BcVRX64B%2BsPoMEYKLeKibDxHHpSFlTxjl4oGAiGfuoaQ%2B9CVrCgR9CGNreyneJhcUAT8%2Bj0guLXPp%2BKmso26c0%2FiOPmvTCNYPihaXSXgVjsO4l2NG76uDilmGC%2FhC5k93QgdWz%2F5HKYv6athySQ4qHoLekEMFblO9Ovcdj%2BODqhSBn80sZw5ew67%2BIzAqaDV31%2BCd2yecK1TOsyq6Qdn6%2FYXOn1AlYOn%2Bf1pymHNhFpnU8aXZ2W3kqxu9YfJa5J5Q4D6p8WKnNc0Aw3SIcBuxLMIrgkL0GOqUB%2Ftp0HK%2BlDBq7pjb6RhsioufsZEDhIszhCLuMtxPJ8%2FXDYnvbw%2FoCBw0As0yTi8Vq7JA7AOQtcWDR3Ix78YAoP045JGXCC%2BCC4sIZVQIVpG0D1cx%2Fc9yYfneRCiv8lZ3OcotCLFOQM%2FbArfUH4NiWuJdYogdTJeji8SsaZZV5tS0Lqy%2BoPzidnGbzig5LGRTPiUF6ZpUpEa3JImKvGoqSylJvGhxz&X-Amz-Signature=13f26c683bac5bcfe26f2585972e5ee50f005e90ff01e47b6d24848658f41d91&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TEL5EP7A%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041747Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIQCBrv44dAc4wgnVvsx0M45CP1sRsTokrGqrk3CO8H%2F%2FEAIgENBHeycuY8MNtjFSEqtKMewFDq4wvEjlLFJpDugCdLsq%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDEzJAG2BIgK8lHTOyCrcA4JpQyvjBgU%2BzsHECYLikLkG9Oy9D%2B6gLGIwpuGv%2Feu2w%2Brxv1jAGb57I8v5dO%2B6pL2tJlfR8ajpqHP2AkgUFmpmbicKCDIoUuvE5ezZSUtZYns6LesMaK3%2Ful3Ufn3yzLvTC9O6bioiKlDXFslQn1wjF7%2B%2FqHM5cgH2JtqaE%2B9looBkqNJ1EuTzEHBh3C8ENObJQgXHc4SGPYcpa8Z6glMMM2SloV2evBwYXLFT74U75gkNKqgBsIYc3pCSkPp%2FgRGmKkT%2FvQvux7mubeXQYq2JZR9RYNtO4Em25p2Y6misK5DwG2lcF%2FvAm2hqG4RVzmyVmx%2Ffb%2BypfMJwVqcUo6QsSMWFJLkmIEX6Oh%2BcVRX64B%2BsPoMEYKLeKibDxHHpSFlTxjl4oGAiGfuoaQ%2B9CVrCgR9CGNreyneJhcUAT8%2Bj0guLXPp%2BKmso26c0%2FiOPmvTCNYPihaXSXgVjsO4l2NG76uDilmGC%2FhC5k93QgdWz%2F5HKYv6athySQ4qHoLekEMFblO9Ovcdj%2BODqhSBn80sZw5ew67%2BIzAqaDV31%2BCd2yecK1TOsyq6Qdn6%2FYXOn1AlYOn%2Bf1pymHNhFpnU8aXZ2W3kqxu9YfJa5J5Q4D6p8WKnNc0Aw3SIcBuxLMIrgkL0GOqUB%2Ftp0HK%2BlDBq7pjb6RhsioufsZEDhIszhCLuMtxPJ8%2FXDYnvbw%2FoCBw0As0yTi8Vq7JA7AOQtcWDR3Ix78YAoP045JGXCC%2BCC4sIZVQIVpG0D1cx%2Fc9yYfneRCiv8lZ3OcotCLFOQM%2FbArfUH4NiWuJdYogdTJeji8SsaZZV5tS0Lqy%2BoPzidnGbzig5LGRTPiUF6ZpUpEa3JImKvGoqSylJvGhxz&X-Amz-Signature=b9c5dc09429c8f7bbb842136fc559ab50e21918b435ba7c79c7a02a61ee1c9b9&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TEL5EP7A%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041747Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIQCBrv44dAc4wgnVvsx0M45CP1sRsTokrGqrk3CO8H%2F%2FEAIgENBHeycuY8MNtjFSEqtKMewFDq4wvEjlLFJpDugCdLsq%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDEzJAG2BIgK8lHTOyCrcA4JpQyvjBgU%2BzsHECYLikLkG9Oy9D%2B6gLGIwpuGv%2Feu2w%2Brxv1jAGb57I8v5dO%2B6pL2tJlfR8ajpqHP2AkgUFmpmbicKCDIoUuvE5ezZSUtZYns6LesMaK3%2Ful3Ufn3yzLvTC9O6bioiKlDXFslQn1wjF7%2B%2FqHM5cgH2JtqaE%2B9looBkqNJ1EuTzEHBh3C8ENObJQgXHc4SGPYcpa8Z6glMMM2SloV2evBwYXLFT74U75gkNKqgBsIYc3pCSkPp%2FgRGmKkT%2FvQvux7mubeXQYq2JZR9RYNtO4Em25p2Y6misK5DwG2lcF%2FvAm2hqG4RVzmyVmx%2Ffb%2BypfMJwVqcUo6QsSMWFJLkmIEX6Oh%2BcVRX64B%2BsPoMEYKLeKibDxHHpSFlTxjl4oGAiGfuoaQ%2B9CVrCgR9CGNreyneJhcUAT8%2Bj0guLXPp%2BKmso26c0%2FiOPmvTCNYPihaXSXgVjsO4l2NG76uDilmGC%2FhC5k93QgdWz%2F5HKYv6athySQ4qHoLekEMFblO9Ovcdj%2BODqhSBn80sZw5ew67%2BIzAqaDV31%2BCd2yecK1TOsyq6Qdn6%2FYXOn1AlYOn%2Bf1pymHNhFpnU8aXZ2W3kqxu9YfJa5J5Q4D6p8WKnNc0Aw3SIcBuxLMIrgkL0GOqUB%2Ftp0HK%2BlDBq7pjb6RhsioufsZEDhIszhCLuMtxPJ8%2FXDYnvbw%2FoCBw0As0yTi8Vq7JA7AOQtcWDR3Ix78YAoP045JGXCC%2BCC4sIZVQIVpG0D1cx%2Fc9yYfneRCiv8lZ3OcotCLFOQM%2FbArfUH4NiWuJdYogdTJeji8SsaZZV5tS0Lqy%2BoPzidnGbzig5LGRTPiUF6ZpUpEa3JImKvGoqSylJvGhxz&X-Amz-Signature=5ab04a8803c08e6c3fcc4b35fd7ac59f00ebca6499a6bcaf44149187793dfa72&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TEL5EP7A%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041747Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIQCBrv44dAc4wgnVvsx0M45CP1sRsTokrGqrk3CO8H%2F%2FEAIgENBHeycuY8MNtjFSEqtKMewFDq4wvEjlLFJpDugCdLsq%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDEzJAG2BIgK8lHTOyCrcA4JpQyvjBgU%2BzsHECYLikLkG9Oy9D%2B6gLGIwpuGv%2Feu2w%2Brxv1jAGb57I8v5dO%2B6pL2tJlfR8ajpqHP2AkgUFmpmbicKCDIoUuvE5ezZSUtZYns6LesMaK3%2Ful3Ufn3yzLvTC9O6bioiKlDXFslQn1wjF7%2B%2FqHM5cgH2JtqaE%2B9looBkqNJ1EuTzEHBh3C8ENObJQgXHc4SGPYcpa8Z6glMMM2SloV2evBwYXLFT74U75gkNKqgBsIYc3pCSkPp%2FgRGmKkT%2FvQvux7mubeXQYq2JZR9RYNtO4Em25p2Y6misK5DwG2lcF%2FvAm2hqG4RVzmyVmx%2Ffb%2BypfMJwVqcUo6QsSMWFJLkmIEX6Oh%2BcVRX64B%2BsPoMEYKLeKibDxHHpSFlTxjl4oGAiGfuoaQ%2B9CVrCgR9CGNreyneJhcUAT8%2Bj0guLXPp%2BKmso26c0%2FiOPmvTCNYPihaXSXgVjsO4l2NG76uDilmGC%2FhC5k93QgdWz%2F5HKYv6athySQ4qHoLekEMFblO9Ovcdj%2BODqhSBn80sZw5ew67%2BIzAqaDV31%2BCd2yecK1TOsyq6Qdn6%2FYXOn1AlYOn%2Bf1pymHNhFpnU8aXZ2W3kqxu9YfJa5J5Q4D6p8WKnNc0Aw3SIcBuxLMIrgkL0GOqUB%2Ftp0HK%2BlDBq7pjb6RhsioufsZEDhIszhCLuMtxPJ8%2FXDYnvbw%2FoCBw0As0yTi8Vq7JA7AOQtcWDR3Ix78YAoP045JGXCC%2BCC4sIZVQIVpG0D1cx%2Fc9yYfneRCiv8lZ3OcotCLFOQM%2FbArfUH4NiWuJdYogdTJeji8SsaZZV5tS0Lqy%2BoPzidnGbzig5LGRTPiUF6ZpUpEa3JImKvGoqSylJvGhxz&X-Amz-Signature=81282fd17f0c489f851ebd7ac4af3936e47bef6a521ea77651196aa7684f8265&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TEL5EP7A%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041747Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIQCBrv44dAc4wgnVvsx0M45CP1sRsTokrGqrk3CO8H%2F%2FEAIgENBHeycuY8MNtjFSEqtKMewFDq4wvEjlLFJpDugCdLsq%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDEzJAG2BIgK8lHTOyCrcA4JpQyvjBgU%2BzsHECYLikLkG9Oy9D%2B6gLGIwpuGv%2Feu2w%2Brxv1jAGb57I8v5dO%2B6pL2tJlfR8ajpqHP2AkgUFmpmbicKCDIoUuvE5ezZSUtZYns6LesMaK3%2Ful3Ufn3yzLvTC9O6bioiKlDXFslQn1wjF7%2B%2FqHM5cgH2JtqaE%2B9looBkqNJ1EuTzEHBh3C8ENObJQgXHc4SGPYcpa8Z6glMMM2SloV2evBwYXLFT74U75gkNKqgBsIYc3pCSkPp%2FgRGmKkT%2FvQvux7mubeXQYq2JZR9RYNtO4Em25p2Y6misK5DwG2lcF%2FvAm2hqG4RVzmyVmx%2Ffb%2BypfMJwVqcUo6QsSMWFJLkmIEX6Oh%2BcVRX64B%2BsPoMEYKLeKibDxHHpSFlTxjl4oGAiGfuoaQ%2B9CVrCgR9CGNreyneJhcUAT8%2Bj0guLXPp%2BKmso26c0%2FiOPmvTCNYPihaXSXgVjsO4l2NG76uDilmGC%2FhC5k93QgdWz%2F5HKYv6athySQ4qHoLekEMFblO9Ovcdj%2BODqhSBn80sZw5ew67%2BIzAqaDV31%2BCd2yecK1TOsyq6Qdn6%2FYXOn1AlYOn%2Bf1pymHNhFpnU8aXZ2W3kqxu9YfJa5J5Q4D6p8WKnNc0Aw3SIcBuxLMIrgkL0GOqUB%2Ftp0HK%2BlDBq7pjb6RhsioufsZEDhIszhCLuMtxPJ8%2FXDYnvbw%2FoCBw0As0yTi8Vq7JA7AOQtcWDR3Ix78YAoP045JGXCC%2BCC4sIZVQIVpG0D1cx%2Fc9yYfneRCiv8lZ3OcotCLFOQM%2FbArfUH4NiWuJdYogdTJeji8SsaZZV5tS0Lqy%2BoPzidnGbzig5LGRTPiUF6ZpUpEa3JImKvGoqSylJvGhxz&X-Amz-Signature=d0ca28aa662084458760cca69493f5f256c4b5561ea8be772cce8b7974a217d5&X-Amz-SignedHeaders=host&x-id=GetObject)
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


