

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667M3CE2JQ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAvdN8SwxiRCmRgEtA08JnzEnbELDlz2fB%2BPUkI1YiusAiAUKrwcOSCqxa2t4WbVtnC2fnJaNdgwbhZU8dQrpv0t7Cr%2FAwgXEAAaDDYzNzQyMzE4MzgwNSIMvrapKRzLik48e3AbKtwD9Y2mYyB2%2F7QbbVg7bRS6dI%2FBmsJi194WtgqUz1QEYv%2FARSGLEEuVmfLVio4KW%2FqTEQSGnFfBtxG9mgU83dEO8S7OLeEWBijclsduBu1ZxqWYC1W5I97eBHQrX2nc%2BBBqGBJxuiK%2BM%2Fa4YHYlRWK%2BhxGbcD0eonrL0VE70nytxXWOW35h3ndONjKBvHWXZ8HDY7Tr2617RfpqCdGiQDAT514tQ2dBWsxbiRpksWKJ6tdnKcsY0U91WJPV8J5XP9nadw2Qt6ZYBqdXdnOysn0jF8xJQtkMK8KhRuSuHhE09Gx%2F5MRNVcLSGdr7MYNuue7cPVf34nVxboKOctDxQbGnodQBxtY0uQavalWgzal4iaHcZPAWVjfUBV1mA8GEyx7RKA0Lkqqay%2F%2Fhs2ofiu4g6QO050x%2BDXTe7FEx28dvtpeSK%2FU8Jgvd%2F9I1wtqIFB0KM9fC7w5mNTptKk1QZBee6Jaas0RQh2yBaimpUNaMp%2F12pQTc4eOzJDR7puxg2Vfx8BEtbPDPcbF6CiQWL2Uqot1S9dvDNkTcUqPCzM2X%2Bfu26gBmuhBaUsGjGjg5%2Fi0gt4UeolE2oora9VSxph7GChbVOmw0LJ2lM5XesaQIraDpDQG15N7QmfN9IOsw0Y2DvQY6pgEHcDQzmT%2Fx88PbiPpLxcJAFn8XBXiQiT3aKiAkWVHm0FweQzcVHXfbFTkrffKNM%2B8Zicevuj9KY2xjaqilFcutxvIBeApmWVTb3KsL%2B55N%2BWw6efVIxxeRHMQAv0fQSHg%2Fsg853wmg%2FtfACP05oTTOXuzIGsyeYHtgkqjqZuUw2fZnqHjNMcMYBuwMVQksUU3PeBKZvac4GXrACUTf5ZCuPLXMB3Ur&X-Amz-Signature=88f622dc152eb96c6b3c30dcf2c0dfd01c2f0133a1afc041d9823142726f2be0&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663Q7A5PUX%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDLvLa99LyRLW%2FuUd8rUrYoQoxV1OLIqUupVCMBXh8NjQIgUniJGYSI5bC6Td%2FmIlUwkNLbIrHb901E9cyXA6IVokcq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDPLYzl79nnXO57jfNCrcA34mboFgFL%2BChJX6H07SkuM%2BJwStub9YZv2pXZqp%2FgCCQm%2FB17WqVcr6ASyjzthRmzpNT7jmogudIRYnH9It7ZDczTdaEwwlylmL1%2B8jIyQf4dCbIm5FiOIQskLc3KIvJcok4OPDA%2B7p%2FYL%2BOtiI8BO5fyN8a4FneMHfhhTS69nExCKSSHY8jcCdxmYJbr2huzYHTxbVnT1QkLZXKLOMLzuWENKXPpnP3Uhxfdq%2B4qwTEliwoF6i%2BSfq9Dm98miZ%2BIWW8XPch3%2B8lTySTwuuEuUiDfvH5DlNUChik6O7tyCzKr7%2F0DKAudFAdTsUYcV4ki7ZjFsH1cU2Hc3luU4QpgCM1R802y%2FWdv1P0GjWzELRzWCtog8NVg%2BUlVT8%2F2A9Op1MwryYbjpNqJ1TxoSgDW07wpBSGScR%2B1PkmmcKNKorNi0RoRpdiDupBdl6N2ueW%2FBT9fsWaKBXpUvl24HBhIX08ssJDMp8ycap0M5qoUV3lqdvW5QsXlQCz94IchCp1WRLX8rJ2yyk2dWaQib5nOTVGZO19IJ46l%2BKjNKWTqld4j49VwGnskI%2FL9JatmTjkc46GxshpHC9AIrUDJC1zZ74eSEPT6hMFRMKPqV3T8pQ7OGwFYP08gUdqIQvMPaNg70GOqUBAUHX7Y47l3IUSh1MwNWrOvCkWoRDHL4eH6510XWpAkKPXfkf3tuP0uLWAna2sdylp1J22ZqvYPbkcdLnhbQ7TnAGvkVxxbhM%2FwI6f%2B0TltLWi5PKyLOIjEAiw3z%2BX4XpR522nKO86VGLyDbLJKy0B9f83xyEjv4c3gAaMvTb%2Fo6vxpXITVBn51rbriezy7fki3eJ%2BImUrYUlbTuNxxs3vLk6VApR&X-Amz-Signature=1ba33eb40fe63b36d251348deca5f22f5f63f91defd2dae4bae9680b9187a131&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663Q7A5PUX%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDLvLa99LyRLW%2FuUd8rUrYoQoxV1OLIqUupVCMBXh8NjQIgUniJGYSI5bC6Td%2FmIlUwkNLbIrHb901E9cyXA6IVokcq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDPLYzl79nnXO57jfNCrcA34mboFgFL%2BChJX6H07SkuM%2BJwStub9YZv2pXZqp%2FgCCQm%2FB17WqVcr6ASyjzthRmzpNT7jmogudIRYnH9It7ZDczTdaEwwlylmL1%2B8jIyQf4dCbIm5FiOIQskLc3KIvJcok4OPDA%2B7p%2FYL%2BOtiI8BO5fyN8a4FneMHfhhTS69nExCKSSHY8jcCdxmYJbr2huzYHTxbVnT1QkLZXKLOMLzuWENKXPpnP3Uhxfdq%2B4qwTEliwoF6i%2BSfq9Dm98miZ%2BIWW8XPch3%2B8lTySTwuuEuUiDfvH5DlNUChik6O7tyCzKr7%2F0DKAudFAdTsUYcV4ki7ZjFsH1cU2Hc3luU4QpgCM1R802y%2FWdv1P0GjWzELRzWCtog8NVg%2BUlVT8%2F2A9Op1MwryYbjpNqJ1TxoSgDW07wpBSGScR%2B1PkmmcKNKorNi0RoRpdiDupBdl6N2ueW%2FBT9fsWaKBXpUvl24HBhIX08ssJDMp8ycap0M5qoUV3lqdvW5QsXlQCz94IchCp1WRLX8rJ2yyk2dWaQib5nOTVGZO19IJ46l%2BKjNKWTqld4j49VwGnskI%2FL9JatmTjkc46GxshpHC9AIrUDJC1zZ74eSEPT6hMFRMKPqV3T8pQ7OGwFYP08gUdqIQvMPaNg70GOqUBAUHX7Y47l3IUSh1MwNWrOvCkWoRDHL4eH6510XWpAkKPXfkf3tuP0uLWAna2sdylp1J22ZqvYPbkcdLnhbQ7TnAGvkVxxbhM%2FwI6f%2B0TltLWi5PKyLOIjEAiw3z%2BX4XpR522nKO86VGLyDbLJKy0B9f83xyEjv4c3gAaMvTb%2Fo6vxpXITVBn51rbriezy7fki3eJ%2BImUrYUlbTuNxxs3vLk6VApR&X-Amz-Signature=5e182ab0ee99c21aa5260de3260765380a97a946fb5ada3b01a456d8fd921a0d&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663Q7A5PUX%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDLvLa99LyRLW%2FuUd8rUrYoQoxV1OLIqUupVCMBXh8NjQIgUniJGYSI5bC6Td%2FmIlUwkNLbIrHb901E9cyXA6IVokcq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDPLYzl79nnXO57jfNCrcA34mboFgFL%2BChJX6H07SkuM%2BJwStub9YZv2pXZqp%2FgCCQm%2FB17WqVcr6ASyjzthRmzpNT7jmogudIRYnH9It7ZDczTdaEwwlylmL1%2B8jIyQf4dCbIm5FiOIQskLc3KIvJcok4OPDA%2B7p%2FYL%2BOtiI8BO5fyN8a4FneMHfhhTS69nExCKSSHY8jcCdxmYJbr2huzYHTxbVnT1QkLZXKLOMLzuWENKXPpnP3Uhxfdq%2B4qwTEliwoF6i%2BSfq9Dm98miZ%2BIWW8XPch3%2B8lTySTwuuEuUiDfvH5DlNUChik6O7tyCzKr7%2F0DKAudFAdTsUYcV4ki7ZjFsH1cU2Hc3luU4QpgCM1R802y%2FWdv1P0GjWzELRzWCtog8NVg%2BUlVT8%2F2A9Op1MwryYbjpNqJ1TxoSgDW07wpBSGScR%2B1PkmmcKNKorNi0RoRpdiDupBdl6N2ueW%2FBT9fsWaKBXpUvl24HBhIX08ssJDMp8ycap0M5qoUV3lqdvW5QsXlQCz94IchCp1WRLX8rJ2yyk2dWaQib5nOTVGZO19IJ46l%2BKjNKWTqld4j49VwGnskI%2FL9JatmTjkc46GxshpHC9AIrUDJC1zZ74eSEPT6hMFRMKPqV3T8pQ7OGwFYP08gUdqIQvMPaNg70GOqUBAUHX7Y47l3IUSh1MwNWrOvCkWoRDHL4eH6510XWpAkKPXfkf3tuP0uLWAna2sdylp1J22ZqvYPbkcdLnhbQ7TnAGvkVxxbhM%2FwI6f%2B0TltLWi5PKyLOIjEAiw3z%2BX4XpR522nKO86VGLyDbLJKy0B9f83xyEjv4c3gAaMvTb%2Fo6vxpXITVBn51rbriezy7fki3eJ%2BImUrYUlbTuNxxs3vLk6VApR&X-Amz-Signature=f13a48585bb5f22e6a0d8cf482b32247d1c7970f634a57b74a54d5d437dd275a&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663Q7A5PUX%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDLvLa99LyRLW%2FuUd8rUrYoQoxV1OLIqUupVCMBXh8NjQIgUniJGYSI5bC6Td%2FmIlUwkNLbIrHb901E9cyXA6IVokcq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDPLYzl79nnXO57jfNCrcA34mboFgFL%2BChJX6H07SkuM%2BJwStub9YZv2pXZqp%2FgCCQm%2FB17WqVcr6ASyjzthRmzpNT7jmogudIRYnH9It7ZDczTdaEwwlylmL1%2B8jIyQf4dCbIm5FiOIQskLc3KIvJcok4OPDA%2B7p%2FYL%2BOtiI8BO5fyN8a4FneMHfhhTS69nExCKSSHY8jcCdxmYJbr2huzYHTxbVnT1QkLZXKLOMLzuWENKXPpnP3Uhxfdq%2B4qwTEliwoF6i%2BSfq9Dm98miZ%2BIWW8XPch3%2B8lTySTwuuEuUiDfvH5DlNUChik6O7tyCzKr7%2F0DKAudFAdTsUYcV4ki7ZjFsH1cU2Hc3luU4QpgCM1R802y%2FWdv1P0GjWzELRzWCtog8NVg%2BUlVT8%2F2A9Op1MwryYbjpNqJ1TxoSgDW07wpBSGScR%2B1PkmmcKNKorNi0RoRpdiDupBdl6N2ueW%2FBT9fsWaKBXpUvl24HBhIX08ssJDMp8ycap0M5qoUV3lqdvW5QsXlQCz94IchCp1WRLX8rJ2yyk2dWaQib5nOTVGZO19IJ46l%2BKjNKWTqld4j49VwGnskI%2FL9JatmTjkc46GxshpHC9AIrUDJC1zZ74eSEPT6hMFRMKPqV3T8pQ7OGwFYP08gUdqIQvMPaNg70GOqUBAUHX7Y47l3IUSh1MwNWrOvCkWoRDHL4eH6510XWpAkKPXfkf3tuP0uLWAna2sdylp1J22ZqvYPbkcdLnhbQ7TnAGvkVxxbhM%2FwI6f%2B0TltLWi5PKyLOIjEAiw3z%2BX4XpR522nKO86VGLyDbLJKy0B9f83xyEjv4c3gAaMvTb%2Fo6vxpXITVBn51rbriezy7fki3eJ%2BImUrYUlbTuNxxs3vLk6VApR&X-Amz-Signature=73e22b3a6d8034f234dacd7269b6ad5647257f648acd343df755ae8677d5c15b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663Q7A5PUX%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDLvLa99LyRLW%2FuUd8rUrYoQoxV1OLIqUupVCMBXh8NjQIgUniJGYSI5bC6Td%2FmIlUwkNLbIrHb901E9cyXA6IVokcq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDPLYzl79nnXO57jfNCrcA34mboFgFL%2BChJX6H07SkuM%2BJwStub9YZv2pXZqp%2FgCCQm%2FB17WqVcr6ASyjzthRmzpNT7jmogudIRYnH9It7ZDczTdaEwwlylmL1%2B8jIyQf4dCbIm5FiOIQskLc3KIvJcok4OPDA%2B7p%2FYL%2BOtiI8BO5fyN8a4FneMHfhhTS69nExCKSSHY8jcCdxmYJbr2huzYHTxbVnT1QkLZXKLOMLzuWENKXPpnP3Uhxfdq%2B4qwTEliwoF6i%2BSfq9Dm98miZ%2BIWW8XPch3%2B8lTySTwuuEuUiDfvH5DlNUChik6O7tyCzKr7%2F0DKAudFAdTsUYcV4ki7ZjFsH1cU2Hc3luU4QpgCM1R802y%2FWdv1P0GjWzELRzWCtog8NVg%2BUlVT8%2F2A9Op1MwryYbjpNqJ1TxoSgDW07wpBSGScR%2B1PkmmcKNKorNi0RoRpdiDupBdl6N2ueW%2FBT9fsWaKBXpUvl24HBhIX08ssJDMp8ycap0M5qoUV3lqdvW5QsXlQCz94IchCp1WRLX8rJ2yyk2dWaQib5nOTVGZO19IJ46l%2BKjNKWTqld4j49VwGnskI%2FL9JatmTjkc46GxshpHC9AIrUDJC1zZ74eSEPT6hMFRMKPqV3T8pQ7OGwFYP08gUdqIQvMPaNg70GOqUBAUHX7Y47l3IUSh1MwNWrOvCkWoRDHL4eH6510XWpAkKPXfkf3tuP0uLWAna2sdylp1J22ZqvYPbkcdLnhbQ7TnAGvkVxxbhM%2FwI6f%2B0TltLWi5PKyLOIjEAiw3z%2BX4XpR522nKO86VGLyDbLJKy0B9f83xyEjv4c3gAaMvTb%2Fo6vxpXITVBn51rbriezy7fki3eJ%2BImUrYUlbTuNxxs3vLk6VApR&X-Amz-Signature=8c2cb939d812de24779cd7088fdb5a0b14cd86e4b4d9c9aed6a4ebab6e7acced&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667M3CE2JQ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAvdN8SwxiRCmRgEtA08JnzEnbELDlz2fB%2BPUkI1YiusAiAUKrwcOSCqxa2t4WbVtnC2fnJaNdgwbhZU8dQrpv0t7Cr%2FAwgXEAAaDDYzNzQyMzE4MzgwNSIMvrapKRzLik48e3AbKtwD9Y2mYyB2%2F7QbbVg7bRS6dI%2FBmsJi194WtgqUz1QEYv%2FARSGLEEuVmfLVio4KW%2FqTEQSGnFfBtxG9mgU83dEO8S7OLeEWBijclsduBu1ZxqWYC1W5I97eBHQrX2nc%2BBBqGBJxuiK%2BM%2Fa4YHYlRWK%2BhxGbcD0eonrL0VE70nytxXWOW35h3ndONjKBvHWXZ8HDY7Tr2617RfpqCdGiQDAT514tQ2dBWsxbiRpksWKJ6tdnKcsY0U91WJPV8J5XP9nadw2Qt6ZYBqdXdnOysn0jF8xJQtkMK8KhRuSuHhE09Gx%2F5MRNVcLSGdr7MYNuue7cPVf34nVxboKOctDxQbGnodQBxtY0uQavalWgzal4iaHcZPAWVjfUBV1mA8GEyx7RKA0Lkqqay%2F%2Fhs2ofiu4g6QO050x%2BDXTe7FEx28dvtpeSK%2FU8Jgvd%2F9I1wtqIFB0KM9fC7w5mNTptKk1QZBee6Jaas0RQh2yBaimpUNaMp%2F12pQTc4eOzJDR7puxg2Vfx8BEtbPDPcbF6CiQWL2Uqot1S9dvDNkTcUqPCzM2X%2Bfu26gBmuhBaUsGjGjg5%2Fi0gt4UeolE2oora9VSxph7GChbVOmw0LJ2lM5XesaQIraDpDQG15N7QmfN9IOsw0Y2DvQY6pgEHcDQzmT%2Fx88PbiPpLxcJAFn8XBXiQiT3aKiAkWVHm0FweQzcVHXfbFTkrffKNM%2B8Zicevuj9KY2xjaqilFcutxvIBeApmWVTb3KsL%2B55N%2BWw6efVIxxeRHMQAv0fQSHg%2Fsg853wmg%2FtfACP05oTTOXuzIGsyeYHtgkqjqZuUw2fZnqHjNMcMYBuwMVQksUU3PeBKZvac4GXrACUTf5ZCuPLXMB3Ur&X-Amz-Signature=cb1148c48ad2b8633c4dd23da0da7526b6196050dd707ba99c205b1c59253bda&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667M3CE2JQ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAvdN8SwxiRCmRgEtA08JnzEnbELDlz2fB%2BPUkI1YiusAiAUKrwcOSCqxa2t4WbVtnC2fnJaNdgwbhZU8dQrpv0t7Cr%2FAwgXEAAaDDYzNzQyMzE4MzgwNSIMvrapKRzLik48e3AbKtwD9Y2mYyB2%2F7QbbVg7bRS6dI%2FBmsJi194WtgqUz1QEYv%2FARSGLEEuVmfLVio4KW%2FqTEQSGnFfBtxG9mgU83dEO8S7OLeEWBijclsduBu1ZxqWYC1W5I97eBHQrX2nc%2BBBqGBJxuiK%2BM%2Fa4YHYlRWK%2BhxGbcD0eonrL0VE70nytxXWOW35h3ndONjKBvHWXZ8HDY7Tr2617RfpqCdGiQDAT514tQ2dBWsxbiRpksWKJ6tdnKcsY0U91WJPV8J5XP9nadw2Qt6ZYBqdXdnOysn0jF8xJQtkMK8KhRuSuHhE09Gx%2F5MRNVcLSGdr7MYNuue7cPVf34nVxboKOctDxQbGnodQBxtY0uQavalWgzal4iaHcZPAWVjfUBV1mA8GEyx7RKA0Lkqqay%2F%2Fhs2ofiu4g6QO050x%2BDXTe7FEx28dvtpeSK%2FU8Jgvd%2F9I1wtqIFB0KM9fC7w5mNTptKk1QZBee6Jaas0RQh2yBaimpUNaMp%2F12pQTc4eOzJDR7puxg2Vfx8BEtbPDPcbF6CiQWL2Uqot1S9dvDNkTcUqPCzM2X%2Bfu26gBmuhBaUsGjGjg5%2Fi0gt4UeolE2oora9VSxph7GChbVOmw0LJ2lM5XesaQIraDpDQG15N7QmfN9IOsw0Y2DvQY6pgEHcDQzmT%2Fx88PbiPpLxcJAFn8XBXiQiT3aKiAkWVHm0FweQzcVHXfbFTkrffKNM%2B8Zicevuj9KY2xjaqilFcutxvIBeApmWVTb3KsL%2B55N%2BWw6efVIxxeRHMQAv0fQSHg%2Fsg853wmg%2FtfACP05oTTOXuzIGsyeYHtgkqjqZuUw2fZnqHjNMcMYBuwMVQksUU3PeBKZvac4GXrACUTf5ZCuPLXMB3Ur&X-Amz-Signature=8161484fa307df9bf3233ff224c7e9b6e43f9b697a743b071950d28cedf92da1&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667M3CE2JQ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAvdN8SwxiRCmRgEtA08JnzEnbELDlz2fB%2BPUkI1YiusAiAUKrwcOSCqxa2t4WbVtnC2fnJaNdgwbhZU8dQrpv0t7Cr%2FAwgXEAAaDDYzNzQyMzE4MzgwNSIMvrapKRzLik48e3AbKtwD9Y2mYyB2%2F7QbbVg7bRS6dI%2FBmsJi194WtgqUz1QEYv%2FARSGLEEuVmfLVio4KW%2FqTEQSGnFfBtxG9mgU83dEO8S7OLeEWBijclsduBu1ZxqWYC1W5I97eBHQrX2nc%2BBBqGBJxuiK%2BM%2Fa4YHYlRWK%2BhxGbcD0eonrL0VE70nytxXWOW35h3ndONjKBvHWXZ8HDY7Tr2617RfpqCdGiQDAT514tQ2dBWsxbiRpksWKJ6tdnKcsY0U91WJPV8J5XP9nadw2Qt6ZYBqdXdnOysn0jF8xJQtkMK8KhRuSuHhE09Gx%2F5MRNVcLSGdr7MYNuue7cPVf34nVxboKOctDxQbGnodQBxtY0uQavalWgzal4iaHcZPAWVjfUBV1mA8GEyx7RKA0Lkqqay%2F%2Fhs2ofiu4g6QO050x%2BDXTe7FEx28dvtpeSK%2FU8Jgvd%2F9I1wtqIFB0KM9fC7w5mNTptKk1QZBee6Jaas0RQh2yBaimpUNaMp%2F12pQTc4eOzJDR7puxg2Vfx8BEtbPDPcbF6CiQWL2Uqot1S9dvDNkTcUqPCzM2X%2Bfu26gBmuhBaUsGjGjg5%2Fi0gt4UeolE2oora9VSxph7GChbVOmw0LJ2lM5XesaQIraDpDQG15N7QmfN9IOsw0Y2DvQY6pgEHcDQzmT%2Fx88PbiPpLxcJAFn8XBXiQiT3aKiAkWVHm0FweQzcVHXfbFTkrffKNM%2B8Zicevuj9KY2xjaqilFcutxvIBeApmWVTb3KsL%2B55N%2BWw6efVIxxeRHMQAv0fQSHg%2Fsg853wmg%2FtfACP05oTTOXuzIGsyeYHtgkqjqZuUw2fZnqHjNMcMYBuwMVQksUU3PeBKZvac4GXrACUTf5ZCuPLXMB3Ur&X-Amz-Signature=0a51283b95ebeb57c359bbbc3fbe88e1b01def02ba7dee61244e11c20a744419&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667M3CE2JQ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAvdN8SwxiRCmRgEtA08JnzEnbELDlz2fB%2BPUkI1YiusAiAUKrwcOSCqxa2t4WbVtnC2fnJaNdgwbhZU8dQrpv0t7Cr%2FAwgXEAAaDDYzNzQyMzE4MzgwNSIMvrapKRzLik48e3AbKtwD9Y2mYyB2%2F7QbbVg7bRS6dI%2FBmsJi194WtgqUz1QEYv%2FARSGLEEuVmfLVio4KW%2FqTEQSGnFfBtxG9mgU83dEO8S7OLeEWBijclsduBu1ZxqWYC1W5I97eBHQrX2nc%2BBBqGBJxuiK%2BM%2Fa4YHYlRWK%2BhxGbcD0eonrL0VE70nytxXWOW35h3ndONjKBvHWXZ8HDY7Tr2617RfpqCdGiQDAT514tQ2dBWsxbiRpksWKJ6tdnKcsY0U91WJPV8J5XP9nadw2Qt6ZYBqdXdnOysn0jF8xJQtkMK8KhRuSuHhE09Gx%2F5MRNVcLSGdr7MYNuue7cPVf34nVxboKOctDxQbGnodQBxtY0uQavalWgzal4iaHcZPAWVjfUBV1mA8GEyx7RKA0Lkqqay%2F%2Fhs2ofiu4g6QO050x%2BDXTe7FEx28dvtpeSK%2FU8Jgvd%2F9I1wtqIFB0KM9fC7w5mNTptKk1QZBee6Jaas0RQh2yBaimpUNaMp%2F12pQTc4eOzJDR7puxg2Vfx8BEtbPDPcbF6CiQWL2Uqot1S9dvDNkTcUqPCzM2X%2Bfu26gBmuhBaUsGjGjg5%2Fi0gt4UeolE2oora9VSxph7GChbVOmw0LJ2lM5XesaQIraDpDQG15N7QmfN9IOsw0Y2DvQY6pgEHcDQzmT%2Fx88PbiPpLxcJAFn8XBXiQiT3aKiAkWVHm0FweQzcVHXfbFTkrffKNM%2B8Zicevuj9KY2xjaqilFcutxvIBeApmWVTb3KsL%2B55N%2BWw6efVIxxeRHMQAv0fQSHg%2Fsg853wmg%2FtfACP05oTTOXuzIGsyeYHtgkqjqZuUw2fZnqHjNMcMYBuwMVQksUU3PeBKZvac4GXrACUTf5ZCuPLXMB3Ur&X-Amz-Signature=e9b2c1604843c54e6bb10a54d9177f31cdd1021bb5642b784a0f120123bbec87&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667M3CE2JQ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAvdN8SwxiRCmRgEtA08JnzEnbELDlz2fB%2BPUkI1YiusAiAUKrwcOSCqxa2t4WbVtnC2fnJaNdgwbhZU8dQrpv0t7Cr%2FAwgXEAAaDDYzNzQyMzE4MzgwNSIMvrapKRzLik48e3AbKtwD9Y2mYyB2%2F7QbbVg7bRS6dI%2FBmsJi194WtgqUz1QEYv%2FARSGLEEuVmfLVio4KW%2FqTEQSGnFfBtxG9mgU83dEO8S7OLeEWBijclsduBu1ZxqWYC1W5I97eBHQrX2nc%2BBBqGBJxuiK%2BM%2Fa4YHYlRWK%2BhxGbcD0eonrL0VE70nytxXWOW35h3ndONjKBvHWXZ8HDY7Tr2617RfpqCdGiQDAT514tQ2dBWsxbiRpksWKJ6tdnKcsY0U91WJPV8J5XP9nadw2Qt6ZYBqdXdnOysn0jF8xJQtkMK8KhRuSuHhE09Gx%2F5MRNVcLSGdr7MYNuue7cPVf34nVxboKOctDxQbGnodQBxtY0uQavalWgzal4iaHcZPAWVjfUBV1mA8GEyx7RKA0Lkqqay%2F%2Fhs2ofiu4g6QO050x%2BDXTe7FEx28dvtpeSK%2FU8Jgvd%2F9I1wtqIFB0KM9fC7w5mNTptKk1QZBee6Jaas0RQh2yBaimpUNaMp%2F12pQTc4eOzJDR7puxg2Vfx8BEtbPDPcbF6CiQWL2Uqot1S9dvDNkTcUqPCzM2X%2Bfu26gBmuhBaUsGjGjg5%2Fi0gt4UeolE2oora9VSxph7GChbVOmw0LJ2lM5XesaQIraDpDQG15N7QmfN9IOsw0Y2DvQY6pgEHcDQzmT%2Fx88PbiPpLxcJAFn8XBXiQiT3aKiAkWVHm0FweQzcVHXfbFTkrffKNM%2B8Zicevuj9KY2xjaqilFcutxvIBeApmWVTb3KsL%2B55N%2BWw6efVIxxeRHMQAv0fQSHg%2Fsg853wmg%2FtfACP05oTTOXuzIGsyeYHtgkqjqZuUw2fZnqHjNMcMYBuwMVQksUU3PeBKZvac4GXrACUTf5ZCuPLXMB3Ur&X-Amz-Signature=0e43f0ee03c6f4d944a665c78edda2cb65ea28feaa75aed7fdfd7bbc66ebcdb4&X-Amz-SignedHeaders=host&x-id=GetObject)
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


