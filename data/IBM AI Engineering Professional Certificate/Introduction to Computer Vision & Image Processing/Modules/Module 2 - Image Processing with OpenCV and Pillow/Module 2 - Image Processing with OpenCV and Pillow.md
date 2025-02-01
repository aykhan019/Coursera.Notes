

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662CNRJXKV%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFqGTwxGe0lI6HYZbzljNdIZjglXxRxT3iWCQMthhUAqAiEAi0f7NCO03jKIFC07r2S7TGS2w1RHqEWCoFKqcNN5Ww8qiAQIyf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJMQAOOn28ovXwOo%2FyrcA5m8dPOwdiO4wvdF2VICrkl4XnDrGXXOso%2B003Lc6HEarT8vL0lrQputwrSNMnxyGYyljYvoKBnr4Q1wRESaZNg01NmcgkJMHRUyW2yO4eCFaflvgWiIw0WPLFkuZZe2CH83Y26myJ9Luolz8b2OGvOTTe3rN0Xec9aL2iND2XJAVdR66yBVlGGiVF0vBetjttKcibpz4DOyV2vQ0kCrPSXXNcmJlyXd3KvMBr%2FbVwNHADKb6KvjkptuOLOIMP4i15E4b6hLWVNxWaDFxU2kLWdQWvUHxmDPuQgpq9D%2B9eKlYu%2BL44CE%2FUjhdSSalkcY63IMucpVhiWwapajRorexlSmd20CIbgXB40Qd1rJ9W7L5TpL7lK06zl1MD3c1wbEDB9I%2BcAXRosRcrgEgbY9H2Oyhq%2Brnaj519boebpKxrhtSF1Esy%2BDXcydSNgb3EG6Wgr1TyvHhCCIdh%2FOSiboRr0H4fFeUdx6p4ogbfUHSjMrOMh0cItQWeXvNjjieN5h4D0w3rvCoO7ceY2ZZY%2BPz1RGm0lFMWB%2BHfaxAEzQTTkA2qjqQ6QXXGmolSyeKZmQVhmPAog9NA31F0Pyyd%2BBdggwECoroYuF24LAg1t%2Bz%2BEQt4EcrLhWj79ERbo2MOvM9bwGOqUBxoZJwZSUefGLj4hmYEugpJk67k2LcZ%2BLyhbQAlVZX3JQ5eVLr5%2B9s6CeC3aPgpU728Brtvdj3YAyDkWFvJVU7TXELwkQoN8lJjNytUN6VfakmMO7rI%2B6E82krNamaJ26EEjxbmAOSMhU9iLR1FtRuwDOLFCndE7LaP2Nj1aqVVxgYuuV%2Bu1bsto3j2rj3Wn2soSazA%2Bs%2BAFiYII5tLcs8LAwCwDs&X-Amz-Signature=a9372a0db29abe41a60039d6550ec1e005569a4cf0d391e2efd3f5736abd4535&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665MEC2HH7%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCjxbbQbxWZ5rv6fRbpkemeYrSx6GTLfQ6sE9POMIikdgIgflfRJzealGtdg7SVx2XrHu%2BvRXvCQPLiP%2B5S5vcV940qiAQIyf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPRUx6BqWjyOQGlcECrcAwvYyqLVa%2BvHrghr%2FRoqp2tu00m41wHm4re40eiZV22G%2BZwBNmwhdPb3gyP3WluhP7MYfG9OK2Q38gjfbansfoLXB3rX9MH%2BWtwOi%2FqHA%2BXSZtjuGByzw0LKFARZ%2FHVYdQE5R03vyfdDXxGhsVBq84emG9FoTLIYy51RFUCJaiN6DaGry7b%2BXiNp%2FYVvSQZLpC4RgA%2FFDkid8%2BpRMbXfph3oxOBysAFGRsRSfscn6pOz8y%2BYcGfqFwB4e5ISJ35eUagIY0VaHAGHw1gyr406XaoaJOiUXBaqks7xpsRHeR3dcjnanve4C2ycNALarcup%2Fnu%2F0sVep4ex%2BZT%2BRVrSKgu8eE2qMO9qZFRKWhFC5sPOzHDpWzyBgiSBrMIQrUyf1aHdmMf3k1WToCtPaCHmDjljJWoG1WIbG4jxY581uFqdRTELJxg2Ofc0LD5gygCSr5NXTl3dravI7KymP%2FaQpIEF76Lt54fImg5vQExKKee%2FqsVQKH59U%2FzgRJg6yFKCgG7R6d%2B6eUlmDOlvyg2gcYtWLFoiXHAw4WqkvrYewc%2FzwyGEwb2dEiZs1yutMDqzk%2FTe9gw785e2hNh%2BBWXglgQ0c7Jk7Gu1VbLCW9UWvFsgFB7f0OdtkfUKHhwPMJDN9bwGOqUBQoKMAkzMvNhURFpXk3FVcOn0AO2Ku0o9%2FhSrPa57QZbJIF94FJXpERU0SWRycGYpABL40eHB4H00EF0AAe7xVrNRHpg%2B7pgqrvc7yy6G6GQqces3XK4TUCVitGeF5ICoAQW9G7yqmSN%2FLBiTqxWmlKuX2lAO9zWReC%2ByFJMN9VGCx6DWqctJC3%2B0lIDjTOo9MQ1vUw5TH9gUa8fbc6nXi7Gojur3&X-Amz-Signature=1404408ee346b6b24d3c45abe17b913fcada3dcd8b8f6de2436eb03b8a6892b5&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665MEC2HH7%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCjxbbQbxWZ5rv6fRbpkemeYrSx6GTLfQ6sE9POMIikdgIgflfRJzealGtdg7SVx2XrHu%2BvRXvCQPLiP%2B5S5vcV940qiAQIyf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPRUx6BqWjyOQGlcECrcAwvYyqLVa%2BvHrghr%2FRoqp2tu00m41wHm4re40eiZV22G%2BZwBNmwhdPb3gyP3WluhP7MYfG9OK2Q38gjfbansfoLXB3rX9MH%2BWtwOi%2FqHA%2BXSZtjuGByzw0LKFARZ%2FHVYdQE5R03vyfdDXxGhsVBq84emG9FoTLIYy51RFUCJaiN6DaGry7b%2BXiNp%2FYVvSQZLpC4RgA%2FFDkid8%2BpRMbXfph3oxOBysAFGRsRSfscn6pOz8y%2BYcGfqFwB4e5ISJ35eUagIY0VaHAGHw1gyr406XaoaJOiUXBaqks7xpsRHeR3dcjnanve4C2ycNALarcup%2Fnu%2F0sVep4ex%2BZT%2BRVrSKgu8eE2qMO9qZFRKWhFC5sPOzHDpWzyBgiSBrMIQrUyf1aHdmMf3k1WToCtPaCHmDjljJWoG1WIbG4jxY581uFqdRTELJxg2Ofc0LD5gygCSr5NXTl3dravI7KymP%2FaQpIEF76Lt54fImg5vQExKKee%2FqsVQKH59U%2FzgRJg6yFKCgG7R6d%2B6eUlmDOlvyg2gcYtWLFoiXHAw4WqkvrYewc%2FzwyGEwb2dEiZs1yutMDqzk%2FTe9gw785e2hNh%2BBWXglgQ0c7Jk7Gu1VbLCW9UWvFsgFB7f0OdtkfUKHhwPMJDN9bwGOqUBQoKMAkzMvNhURFpXk3FVcOn0AO2Ku0o9%2FhSrPa57QZbJIF94FJXpERU0SWRycGYpABL40eHB4H00EF0AAe7xVrNRHpg%2B7pgqrvc7yy6G6GQqces3XK4TUCVitGeF5ICoAQW9G7yqmSN%2FLBiTqxWmlKuX2lAO9zWReC%2ByFJMN9VGCx6DWqctJC3%2B0lIDjTOo9MQ1vUw5TH9gUa8fbc6nXi7Gojur3&X-Amz-Signature=3fc15e287f9d3ab300edcde248b8c0cd917ead205ff30c52166a705485f591c8&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665MEC2HH7%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCjxbbQbxWZ5rv6fRbpkemeYrSx6GTLfQ6sE9POMIikdgIgflfRJzealGtdg7SVx2XrHu%2BvRXvCQPLiP%2B5S5vcV940qiAQIyf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPRUx6BqWjyOQGlcECrcAwvYyqLVa%2BvHrghr%2FRoqp2tu00m41wHm4re40eiZV22G%2BZwBNmwhdPb3gyP3WluhP7MYfG9OK2Q38gjfbansfoLXB3rX9MH%2BWtwOi%2FqHA%2BXSZtjuGByzw0LKFARZ%2FHVYdQE5R03vyfdDXxGhsVBq84emG9FoTLIYy51RFUCJaiN6DaGry7b%2BXiNp%2FYVvSQZLpC4RgA%2FFDkid8%2BpRMbXfph3oxOBysAFGRsRSfscn6pOz8y%2BYcGfqFwB4e5ISJ35eUagIY0VaHAGHw1gyr406XaoaJOiUXBaqks7xpsRHeR3dcjnanve4C2ycNALarcup%2Fnu%2F0sVep4ex%2BZT%2BRVrSKgu8eE2qMO9qZFRKWhFC5sPOzHDpWzyBgiSBrMIQrUyf1aHdmMf3k1WToCtPaCHmDjljJWoG1WIbG4jxY581uFqdRTELJxg2Ofc0LD5gygCSr5NXTl3dravI7KymP%2FaQpIEF76Lt54fImg5vQExKKee%2FqsVQKH59U%2FzgRJg6yFKCgG7R6d%2B6eUlmDOlvyg2gcYtWLFoiXHAw4WqkvrYewc%2FzwyGEwb2dEiZs1yutMDqzk%2FTe9gw785e2hNh%2BBWXglgQ0c7Jk7Gu1VbLCW9UWvFsgFB7f0OdtkfUKHhwPMJDN9bwGOqUBQoKMAkzMvNhURFpXk3FVcOn0AO2Ku0o9%2FhSrPa57QZbJIF94FJXpERU0SWRycGYpABL40eHB4H00EF0AAe7xVrNRHpg%2B7pgqrvc7yy6G6GQqces3XK4TUCVitGeF5ICoAQW9G7yqmSN%2FLBiTqxWmlKuX2lAO9zWReC%2ByFJMN9VGCx6DWqctJC3%2B0lIDjTOo9MQ1vUw5TH9gUa8fbc6nXi7Gojur3&X-Amz-Signature=cb8dd54f00cc3539bba537d8c222948c3b24eec08f4e7b0f327c10a4503de482&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665MEC2HH7%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCjxbbQbxWZ5rv6fRbpkemeYrSx6GTLfQ6sE9POMIikdgIgflfRJzealGtdg7SVx2XrHu%2BvRXvCQPLiP%2B5S5vcV940qiAQIyf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPRUx6BqWjyOQGlcECrcAwvYyqLVa%2BvHrghr%2FRoqp2tu00m41wHm4re40eiZV22G%2BZwBNmwhdPb3gyP3WluhP7MYfG9OK2Q38gjfbansfoLXB3rX9MH%2BWtwOi%2FqHA%2BXSZtjuGByzw0LKFARZ%2FHVYdQE5R03vyfdDXxGhsVBq84emG9FoTLIYy51RFUCJaiN6DaGry7b%2BXiNp%2FYVvSQZLpC4RgA%2FFDkid8%2BpRMbXfph3oxOBysAFGRsRSfscn6pOz8y%2BYcGfqFwB4e5ISJ35eUagIY0VaHAGHw1gyr406XaoaJOiUXBaqks7xpsRHeR3dcjnanve4C2ycNALarcup%2Fnu%2F0sVep4ex%2BZT%2BRVrSKgu8eE2qMO9qZFRKWhFC5sPOzHDpWzyBgiSBrMIQrUyf1aHdmMf3k1WToCtPaCHmDjljJWoG1WIbG4jxY581uFqdRTELJxg2Ofc0LD5gygCSr5NXTl3dravI7KymP%2FaQpIEF76Lt54fImg5vQExKKee%2FqsVQKH59U%2FzgRJg6yFKCgG7R6d%2B6eUlmDOlvyg2gcYtWLFoiXHAw4WqkvrYewc%2FzwyGEwb2dEiZs1yutMDqzk%2FTe9gw785e2hNh%2BBWXglgQ0c7Jk7Gu1VbLCW9UWvFsgFB7f0OdtkfUKHhwPMJDN9bwGOqUBQoKMAkzMvNhURFpXk3FVcOn0AO2Ku0o9%2FhSrPa57QZbJIF94FJXpERU0SWRycGYpABL40eHB4H00EF0AAe7xVrNRHpg%2B7pgqrvc7yy6G6GQqces3XK4TUCVitGeF5ICoAQW9G7yqmSN%2FLBiTqxWmlKuX2lAO9zWReC%2ByFJMN9VGCx6DWqctJC3%2B0lIDjTOo9MQ1vUw5TH9gUa8fbc6nXi7Gojur3&X-Amz-Signature=4061516cc8633c2c007787e8a0399ba3a2f3f4f403d3abffcff63ca4ccd52602&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665MEC2HH7%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCjxbbQbxWZ5rv6fRbpkemeYrSx6GTLfQ6sE9POMIikdgIgflfRJzealGtdg7SVx2XrHu%2BvRXvCQPLiP%2B5S5vcV940qiAQIyf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPRUx6BqWjyOQGlcECrcAwvYyqLVa%2BvHrghr%2FRoqp2tu00m41wHm4re40eiZV22G%2BZwBNmwhdPb3gyP3WluhP7MYfG9OK2Q38gjfbansfoLXB3rX9MH%2BWtwOi%2FqHA%2BXSZtjuGByzw0LKFARZ%2FHVYdQE5R03vyfdDXxGhsVBq84emG9FoTLIYy51RFUCJaiN6DaGry7b%2BXiNp%2FYVvSQZLpC4RgA%2FFDkid8%2BpRMbXfph3oxOBysAFGRsRSfscn6pOz8y%2BYcGfqFwB4e5ISJ35eUagIY0VaHAGHw1gyr406XaoaJOiUXBaqks7xpsRHeR3dcjnanve4C2ycNALarcup%2Fnu%2F0sVep4ex%2BZT%2BRVrSKgu8eE2qMO9qZFRKWhFC5sPOzHDpWzyBgiSBrMIQrUyf1aHdmMf3k1WToCtPaCHmDjljJWoG1WIbG4jxY581uFqdRTELJxg2Ofc0LD5gygCSr5NXTl3dravI7KymP%2FaQpIEF76Lt54fImg5vQExKKee%2FqsVQKH59U%2FzgRJg6yFKCgG7R6d%2B6eUlmDOlvyg2gcYtWLFoiXHAw4WqkvrYewc%2FzwyGEwb2dEiZs1yutMDqzk%2FTe9gw785e2hNh%2BBWXglgQ0c7Jk7Gu1VbLCW9UWvFsgFB7f0OdtkfUKHhwPMJDN9bwGOqUBQoKMAkzMvNhURFpXk3FVcOn0AO2Ku0o9%2FhSrPa57QZbJIF94FJXpERU0SWRycGYpABL40eHB4H00EF0AAe7xVrNRHpg%2B7pgqrvc7yy6G6GQqces3XK4TUCVitGeF5ICoAQW9G7yqmSN%2FLBiTqxWmlKuX2lAO9zWReC%2ByFJMN9VGCx6DWqctJC3%2B0lIDjTOo9MQ1vUw5TH9gUa8fbc6nXi7Gojur3&X-Amz-Signature=b22cabdf25d4aa2a935c8d295c5930aa685c6eec3d33a77dcaba3d5d0c3596cc&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662CNRJXKV%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFqGTwxGe0lI6HYZbzljNdIZjglXxRxT3iWCQMthhUAqAiEAi0f7NCO03jKIFC07r2S7TGS2w1RHqEWCoFKqcNN5Ww8qiAQIyf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJMQAOOn28ovXwOo%2FyrcA5m8dPOwdiO4wvdF2VICrkl4XnDrGXXOso%2B003Lc6HEarT8vL0lrQputwrSNMnxyGYyljYvoKBnr4Q1wRESaZNg01NmcgkJMHRUyW2yO4eCFaflvgWiIw0WPLFkuZZe2CH83Y26myJ9Luolz8b2OGvOTTe3rN0Xec9aL2iND2XJAVdR66yBVlGGiVF0vBetjttKcibpz4DOyV2vQ0kCrPSXXNcmJlyXd3KvMBr%2FbVwNHADKb6KvjkptuOLOIMP4i15E4b6hLWVNxWaDFxU2kLWdQWvUHxmDPuQgpq9D%2B9eKlYu%2BL44CE%2FUjhdSSalkcY63IMucpVhiWwapajRorexlSmd20CIbgXB40Qd1rJ9W7L5TpL7lK06zl1MD3c1wbEDB9I%2BcAXRosRcrgEgbY9H2Oyhq%2Brnaj519boebpKxrhtSF1Esy%2BDXcydSNgb3EG6Wgr1TyvHhCCIdh%2FOSiboRr0H4fFeUdx6p4ogbfUHSjMrOMh0cItQWeXvNjjieN5h4D0w3rvCoO7ceY2ZZY%2BPz1RGm0lFMWB%2BHfaxAEzQTTkA2qjqQ6QXXGmolSyeKZmQVhmPAog9NA31F0Pyyd%2BBdggwECoroYuF24LAg1t%2Bz%2BEQt4EcrLhWj79ERbo2MOvM9bwGOqUBxoZJwZSUefGLj4hmYEugpJk67k2LcZ%2BLyhbQAlVZX3JQ5eVLr5%2B9s6CeC3aPgpU728Brtvdj3YAyDkWFvJVU7TXELwkQoN8lJjNytUN6VfakmMO7rI%2B6E82krNamaJ26EEjxbmAOSMhU9iLR1FtRuwDOLFCndE7LaP2Nj1aqVVxgYuuV%2Bu1bsto3j2rj3Wn2soSazA%2Bs%2BAFiYII5tLcs8LAwCwDs&X-Amz-Signature=8ed3332f2de78eaee6de29d7e6bd090dd1ecc6bd8d57907713693379dc4bd5b0&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662CNRJXKV%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFqGTwxGe0lI6HYZbzljNdIZjglXxRxT3iWCQMthhUAqAiEAi0f7NCO03jKIFC07r2S7TGS2w1RHqEWCoFKqcNN5Ww8qiAQIyf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJMQAOOn28ovXwOo%2FyrcA5m8dPOwdiO4wvdF2VICrkl4XnDrGXXOso%2B003Lc6HEarT8vL0lrQputwrSNMnxyGYyljYvoKBnr4Q1wRESaZNg01NmcgkJMHRUyW2yO4eCFaflvgWiIw0WPLFkuZZe2CH83Y26myJ9Luolz8b2OGvOTTe3rN0Xec9aL2iND2XJAVdR66yBVlGGiVF0vBetjttKcibpz4DOyV2vQ0kCrPSXXNcmJlyXd3KvMBr%2FbVwNHADKb6KvjkptuOLOIMP4i15E4b6hLWVNxWaDFxU2kLWdQWvUHxmDPuQgpq9D%2B9eKlYu%2BL44CE%2FUjhdSSalkcY63IMucpVhiWwapajRorexlSmd20CIbgXB40Qd1rJ9W7L5TpL7lK06zl1MD3c1wbEDB9I%2BcAXRosRcrgEgbY9H2Oyhq%2Brnaj519boebpKxrhtSF1Esy%2BDXcydSNgb3EG6Wgr1TyvHhCCIdh%2FOSiboRr0H4fFeUdx6p4ogbfUHSjMrOMh0cItQWeXvNjjieN5h4D0w3rvCoO7ceY2ZZY%2BPz1RGm0lFMWB%2BHfaxAEzQTTkA2qjqQ6QXXGmolSyeKZmQVhmPAog9NA31F0Pyyd%2BBdggwECoroYuF24LAg1t%2Bz%2BEQt4EcrLhWj79ERbo2MOvM9bwGOqUBxoZJwZSUefGLj4hmYEugpJk67k2LcZ%2BLyhbQAlVZX3JQ5eVLr5%2B9s6CeC3aPgpU728Brtvdj3YAyDkWFvJVU7TXELwkQoN8lJjNytUN6VfakmMO7rI%2B6E82krNamaJ26EEjxbmAOSMhU9iLR1FtRuwDOLFCndE7LaP2Nj1aqVVxgYuuV%2Bu1bsto3j2rj3Wn2soSazA%2Bs%2BAFiYII5tLcs8LAwCwDs&X-Amz-Signature=4b55c6cdf33d23f3e6f610f47d8c8b6e062d496363b452aa80b708cddc0178d4&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662CNRJXKV%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFqGTwxGe0lI6HYZbzljNdIZjglXxRxT3iWCQMthhUAqAiEAi0f7NCO03jKIFC07r2S7TGS2w1RHqEWCoFKqcNN5Ww8qiAQIyf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJMQAOOn28ovXwOo%2FyrcA5m8dPOwdiO4wvdF2VICrkl4XnDrGXXOso%2B003Lc6HEarT8vL0lrQputwrSNMnxyGYyljYvoKBnr4Q1wRESaZNg01NmcgkJMHRUyW2yO4eCFaflvgWiIw0WPLFkuZZe2CH83Y26myJ9Luolz8b2OGvOTTe3rN0Xec9aL2iND2XJAVdR66yBVlGGiVF0vBetjttKcibpz4DOyV2vQ0kCrPSXXNcmJlyXd3KvMBr%2FbVwNHADKb6KvjkptuOLOIMP4i15E4b6hLWVNxWaDFxU2kLWdQWvUHxmDPuQgpq9D%2B9eKlYu%2BL44CE%2FUjhdSSalkcY63IMucpVhiWwapajRorexlSmd20CIbgXB40Qd1rJ9W7L5TpL7lK06zl1MD3c1wbEDB9I%2BcAXRosRcrgEgbY9H2Oyhq%2Brnaj519boebpKxrhtSF1Esy%2BDXcydSNgb3EG6Wgr1TyvHhCCIdh%2FOSiboRr0H4fFeUdx6p4ogbfUHSjMrOMh0cItQWeXvNjjieN5h4D0w3rvCoO7ceY2ZZY%2BPz1RGm0lFMWB%2BHfaxAEzQTTkA2qjqQ6QXXGmolSyeKZmQVhmPAog9NA31F0Pyyd%2BBdggwECoroYuF24LAg1t%2Bz%2BEQt4EcrLhWj79ERbo2MOvM9bwGOqUBxoZJwZSUefGLj4hmYEugpJk67k2LcZ%2BLyhbQAlVZX3JQ5eVLr5%2B9s6CeC3aPgpU728Brtvdj3YAyDkWFvJVU7TXELwkQoN8lJjNytUN6VfakmMO7rI%2B6E82krNamaJ26EEjxbmAOSMhU9iLR1FtRuwDOLFCndE7LaP2Nj1aqVVxgYuuV%2Bu1bsto3j2rj3Wn2soSazA%2Bs%2BAFiYII5tLcs8LAwCwDs&X-Amz-Signature=02e5328883abb9e28fa74960f5617b83c72ab4e170306323ad863d038f8b299f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662CNRJXKV%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFqGTwxGe0lI6HYZbzljNdIZjglXxRxT3iWCQMthhUAqAiEAi0f7NCO03jKIFC07r2S7TGS2w1RHqEWCoFKqcNN5Ww8qiAQIyf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJMQAOOn28ovXwOo%2FyrcA5m8dPOwdiO4wvdF2VICrkl4XnDrGXXOso%2B003Lc6HEarT8vL0lrQputwrSNMnxyGYyljYvoKBnr4Q1wRESaZNg01NmcgkJMHRUyW2yO4eCFaflvgWiIw0WPLFkuZZe2CH83Y26myJ9Luolz8b2OGvOTTe3rN0Xec9aL2iND2XJAVdR66yBVlGGiVF0vBetjttKcibpz4DOyV2vQ0kCrPSXXNcmJlyXd3KvMBr%2FbVwNHADKb6KvjkptuOLOIMP4i15E4b6hLWVNxWaDFxU2kLWdQWvUHxmDPuQgpq9D%2B9eKlYu%2BL44CE%2FUjhdSSalkcY63IMucpVhiWwapajRorexlSmd20CIbgXB40Qd1rJ9W7L5TpL7lK06zl1MD3c1wbEDB9I%2BcAXRosRcrgEgbY9H2Oyhq%2Brnaj519boebpKxrhtSF1Esy%2BDXcydSNgb3EG6Wgr1TyvHhCCIdh%2FOSiboRr0H4fFeUdx6p4ogbfUHSjMrOMh0cItQWeXvNjjieN5h4D0w3rvCoO7ceY2ZZY%2BPz1RGm0lFMWB%2BHfaxAEzQTTkA2qjqQ6QXXGmolSyeKZmQVhmPAog9NA31F0Pyyd%2BBdggwECoroYuF24LAg1t%2Bz%2BEQt4EcrLhWj79ERbo2MOvM9bwGOqUBxoZJwZSUefGLj4hmYEugpJk67k2LcZ%2BLyhbQAlVZX3JQ5eVLr5%2B9s6CeC3aPgpU728Brtvdj3YAyDkWFvJVU7TXELwkQoN8lJjNytUN6VfakmMO7rI%2B6E82krNamaJ26EEjxbmAOSMhU9iLR1FtRuwDOLFCndE7LaP2Nj1aqVVxgYuuV%2Bu1bsto3j2rj3Wn2soSazA%2Bs%2BAFiYII5tLcs8LAwCwDs&X-Amz-Signature=14ffcaa21a3fb130016ce4f2a9337879b0d3800dad82ba40c585eadbfe4c963c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662CNRJXKV%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFqGTwxGe0lI6HYZbzljNdIZjglXxRxT3iWCQMthhUAqAiEAi0f7NCO03jKIFC07r2S7TGS2w1RHqEWCoFKqcNN5Ww8qiAQIyf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJMQAOOn28ovXwOo%2FyrcA5m8dPOwdiO4wvdF2VICrkl4XnDrGXXOso%2B003Lc6HEarT8vL0lrQputwrSNMnxyGYyljYvoKBnr4Q1wRESaZNg01NmcgkJMHRUyW2yO4eCFaflvgWiIw0WPLFkuZZe2CH83Y26myJ9Luolz8b2OGvOTTe3rN0Xec9aL2iND2XJAVdR66yBVlGGiVF0vBetjttKcibpz4DOyV2vQ0kCrPSXXNcmJlyXd3KvMBr%2FbVwNHADKb6KvjkptuOLOIMP4i15E4b6hLWVNxWaDFxU2kLWdQWvUHxmDPuQgpq9D%2B9eKlYu%2BL44CE%2FUjhdSSalkcY63IMucpVhiWwapajRorexlSmd20CIbgXB40Qd1rJ9W7L5TpL7lK06zl1MD3c1wbEDB9I%2BcAXRosRcrgEgbY9H2Oyhq%2Brnaj519boebpKxrhtSF1Esy%2BDXcydSNgb3EG6Wgr1TyvHhCCIdh%2FOSiboRr0H4fFeUdx6p4ogbfUHSjMrOMh0cItQWeXvNjjieN5h4D0w3rvCoO7ceY2ZZY%2BPz1RGm0lFMWB%2BHfaxAEzQTTkA2qjqQ6QXXGmolSyeKZmQVhmPAog9NA31F0Pyyd%2BBdggwECoroYuF24LAg1t%2Bz%2BEQt4EcrLhWj79ERbo2MOvM9bwGOqUBxoZJwZSUefGLj4hmYEugpJk67k2LcZ%2BLyhbQAlVZX3JQ5eVLr5%2B9s6CeC3aPgpU728Brtvdj3YAyDkWFvJVU7TXELwkQoN8lJjNytUN6VfakmMO7rI%2B6E82krNamaJ26EEjxbmAOSMhU9iLR1FtRuwDOLFCndE7LaP2Nj1aqVVxgYuuV%2Bu1bsto3j2rj3Wn2soSazA%2Bs%2BAFiYII5tLcs8LAwCwDs&X-Amz-Signature=33f70af0ab7c2559a8ba95daf53b8f7051a185da9c7ce064481aa67176c13dc7&X-Amz-SignedHeaders=host&x-id=GetObject)
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


