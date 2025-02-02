

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676ABWFHY%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID9Sae%2BoAMjoORc0bRMzLwBdqheEa6HrssblACTrkePLAiAOs4J3pdC6KqM%2BGzDefOuUNF%2BFq8H70V6asw81cneJHCqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTF8zS0G2DeYqO38iKtwDWr8sEkowyunRwFnKegk8%2Bq42TRV9GL1sFZkZ0Ez53Hm9uocSiJpHRAUaEhWVu5SUl65xE2VDfcZSASrSVqWoe8z%2FVf%2FrJENCckNray8mMBzy4E7ufh2wjpnD%2FEogyxE8sfmk7cEamCB2YGQKzXcABhku2%2B0snezOsCSfbUEJV%2FFVsoIxEy96QTtu1raZjCGEfB2hSsqZ6aS9LOnjlpWTjGRGuQwu26YMq4ME2Bo8Bi%2F8mpmmgVyXD3lJ1bp3YI6shFDlfBMtAQt3GGfJu%2FDioW1QjiJ3Ez06SyNghVdjcHPXBPt3ZAiWfODFvVoEgbaAnF13bYILGgPSdaeEim2hygSJaidgB09A%2BDM7RB3Ev8OgYzDUQYF7%2BiuiJM0GRt%2B3Aod2gWVtBpA3olaw9ZJfa1pMXPMvOF0zoGAbdIpiTA%2ByysmYrdB53orYZxdbejPiz3uK2h8TrWxiodKM84NxWeiz79bnf2%2FZJBE0E%2FiRWCYD55R2IzLadI%2BsJQoiw%2BZunM0Ur5X6buxMdyy64q8vbi1zIB0skb0%2Br1idB6765KY8wrZ7r9ula960mIGcuGJvORMs7bUQwwopQMrr4EdcoevL0VgXG8HSzGc9rjs72srGesGIm0DeR8LbqQUw0N3%2BvAY6pgErLmLp6R3JZ3A4te2Stryp5N%2F%2BPmMq1cIbHZHXPgI0KBAjCFhkZGGbNBNkPo28hW2CEoSG0eX7yOwXW%2Bo5PhbEvquvwBRQJEoM5TEadSIj1FuX8eWlZlZ9LniGyufxBoMdsEX8%2Bsw5dwOYg2LF5%2FVKNuyzFKIAEmbMwPqI9dIbteGxF07G6HrFGza8IcXqgpEuORi4LAioAUMFKXaQw4aYWaOks74q&X-Amz-Signature=0025fa8a688543e520091e89a3ee18564a1d8b8cb90077d575a9280c732f545f&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46624PUVWA6%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDWPKhi0K5sY3HuiFwASFg%2FWbt4NqGf%2FLaUDYSWaGw2kQIhAINBD2P6GO3z2XeLfVC%2BhEpU341FGluKL%2F06WSMlw1vdKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy%2BfJ0OllvIR95urkAq3AMrtzU0Jgh5emZMOYUZZdHagdvA%2BK0hGFw9EeU2I6i2e3dlj1cxpqGd7Y2TG6S5O67jD2%2B06GvZ5cLlpoz%2BB%2BaHuwnqMN%2BdzDo%2FpOhtyA0hy06dPEpB90MqRibmSGKunaogNQq7rqANjRD%2BLw0WU52Yu3en%2F%2FJeOQxOv07K6PtwgW7GfdakwUuaAS0WhkXAxNIgPUcZ5fElcbnCMswWQfCGi2oGQaJ7yWyQt873Y8KVsOvih96D95svm%2FHQbAXFXT9ho1xnGdm1d40oj2%2Bezl7sl3kzMgZ5wp2lSsG1XRZ%2B84y2XnrUByroIqLJIukbO1G67cAZd6UkCSJ5Pvxcx93HXspuNolKwRgDs%2BdIyCZ1YeLLvKv7B9L3ZZpgwQO6plsu7kaFoJz0O5pPHaLGO6LMR3jr%2BKd7p%2BaAs8iJhsSBfOO9LJcJSBcYBzIZ%2Bnht4XNI72GjptI5h1Yqz%2B0%2BU%2BKBUs5jW%2FCZFJ8F%2BCatZHJ0C%2B%2FAZZXkVH0pPSP3Ya1EhcbvXPCWOgrQG8U5binGGhiN4Nr4KXcs%2FoMds3BAKVg%2FmpDS1oht5laJs%2BaD6m%2BGEf%2BIg4aAajXiDtOGLYW6zB1T0xLASa2Skwqu54KMI2bTN15jQy3jsPZyX45KwTC02P68BjqkAW7UW1U617%2BYaD%2By6i33d6vR4dDu%2FXAY31fZZcRJMSC1Z8qVxVeaq0pzLhaYuy9rk7ohqISM0Pj55v54gto7UZ9HfpZuVM2%2FPro2FF4AjhXl9%2FgR8zvELnaCKkWDBRrOnMTatzI7U6OGJPzp1sa5ArHQfzvwUKB6UNpMuyFhyIAJ3mBTq2LkNneqLYCbT8PsytiNQgBuh2z7KA%2FeNjobSj5KDkpq&X-Amz-Signature=bc4a6b337ca50b396149094826578ca263bd552dfd18530e7ca7a8208f3a64ba&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46624PUVWA6%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDWPKhi0K5sY3HuiFwASFg%2FWbt4NqGf%2FLaUDYSWaGw2kQIhAINBD2P6GO3z2XeLfVC%2BhEpU341FGluKL%2F06WSMlw1vdKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy%2BfJ0OllvIR95urkAq3AMrtzU0Jgh5emZMOYUZZdHagdvA%2BK0hGFw9EeU2I6i2e3dlj1cxpqGd7Y2TG6S5O67jD2%2B06GvZ5cLlpoz%2BB%2BaHuwnqMN%2BdzDo%2FpOhtyA0hy06dPEpB90MqRibmSGKunaogNQq7rqANjRD%2BLw0WU52Yu3en%2F%2FJeOQxOv07K6PtwgW7GfdakwUuaAS0WhkXAxNIgPUcZ5fElcbnCMswWQfCGi2oGQaJ7yWyQt873Y8KVsOvih96D95svm%2FHQbAXFXT9ho1xnGdm1d40oj2%2Bezl7sl3kzMgZ5wp2lSsG1XRZ%2B84y2XnrUByroIqLJIukbO1G67cAZd6UkCSJ5Pvxcx93HXspuNolKwRgDs%2BdIyCZ1YeLLvKv7B9L3ZZpgwQO6plsu7kaFoJz0O5pPHaLGO6LMR3jr%2BKd7p%2BaAs8iJhsSBfOO9LJcJSBcYBzIZ%2Bnht4XNI72GjptI5h1Yqz%2B0%2BU%2BKBUs5jW%2FCZFJ8F%2BCatZHJ0C%2B%2FAZZXkVH0pPSP3Ya1EhcbvXPCWOgrQG8U5binGGhiN4Nr4KXcs%2FoMds3BAKVg%2FmpDS1oht5laJs%2BaD6m%2BGEf%2BIg4aAajXiDtOGLYW6zB1T0xLASa2Skwqu54KMI2bTN15jQy3jsPZyX45KwTC02P68BjqkAW7UW1U617%2BYaD%2By6i33d6vR4dDu%2FXAY31fZZcRJMSC1Z8qVxVeaq0pzLhaYuy9rk7ohqISM0Pj55v54gto7UZ9HfpZuVM2%2FPro2FF4AjhXl9%2FgR8zvELnaCKkWDBRrOnMTatzI7U6OGJPzp1sa5ArHQfzvwUKB6UNpMuyFhyIAJ3mBTq2LkNneqLYCbT8PsytiNQgBuh2z7KA%2FeNjobSj5KDkpq&X-Amz-Signature=826f7a65413fb173fca5453ca0409c9e822393cd79301e8989c2b63b5869ad0f&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46624PUVWA6%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDWPKhi0K5sY3HuiFwASFg%2FWbt4NqGf%2FLaUDYSWaGw2kQIhAINBD2P6GO3z2XeLfVC%2BhEpU341FGluKL%2F06WSMlw1vdKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy%2BfJ0OllvIR95urkAq3AMrtzU0Jgh5emZMOYUZZdHagdvA%2BK0hGFw9EeU2I6i2e3dlj1cxpqGd7Y2TG6S5O67jD2%2B06GvZ5cLlpoz%2BB%2BaHuwnqMN%2BdzDo%2FpOhtyA0hy06dPEpB90MqRibmSGKunaogNQq7rqANjRD%2BLw0WU52Yu3en%2F%2FJeOQxOv07K6PtwgW7GfdakwUuaAS0WhkXAxNIgPUcZ5fElcbnCMswWQfCGi2oGQaJ7yWyQt873Y8KVsOvih96D95svm%2FHQbAXFXT9ho1xnGdm1d40oj2%2Bezl7sl3kzMgZ5wp2lSsG1XRZ%2B84y2XnrUByroIqLJIukbO1G67cAZd6UkCSJ5Pvxcx93HXspuNolKwRgDs%2BdIyCZ1YeLLvKv7B9L3ZZpgwQO6plsu7kaFoJz0O5pPHaLGO6LMR3jr%2BKd7p%2BaAs8iJhsSBfOO9LJcJSBcYBzIZ%2Bnht4XNI72GjptI5h1Yqz%2B0%2BU%2BKBUs5jW%2FCZFJ8F%2BCatZHJ0C%2B%2FAZZXkVH0pPSP3Ya1EhcbvXPCWOgrQG8U5binGGhiN4Nr4KXcs%2FoMds3BAKVg%2FmpDS1oht5laJs%2BaD6m%2BGEf%2BIg4aAajXiDtOGLYW6zB1T0xLASa2Skwqu54KMI2bTN15jQy3jsPZyX45KwTC02P68BjqkAW7UW1U617%2BYaD%2By6i33d6vR4dDu%2FXAY31fZZcRJMSC1Z8qVxVeaq0pzLhaYuy9rk7ohqISM0Pj55v54gto7UZ9HfpZuVM2%2FPro2FF4AjhXl9%2FgR8zvELnaCKkWDBRrOnMTatzI7U6OGJPzp1sa5ArHQfzvwUKB6UNpMuyFhyIAJ3mBTq2LkNneqLYCbT8PsytiNQgBuh2z7KA%2FeNjobSj5KDkpq&X-Amz-Signature=cde7634c835a2d43220feb3a61c263f32c5b1ad03890a9c5c319971683212c35&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46624PUVWA6%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDWPKhi0K5sY3HuiFwASFg%2FWbt4NqGf%2FLaUDYSWaGw2kQIhAINBD2P6GO3z2XeLfVC%2BhEpU341FGluKL%2F06WSMlw1vdKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy%2BfJ0OllvIR95urkAq3AMrtzU0Jgh5emZMOYUZZdHagdvA%2BK0hGFw9EeU2I6i2e3dlj1cxpqGd7Y2TG6S5O67jD2%2B06GvZ5cLlpoz%2BB%2BaHuwnqMN%2BdzDo%2FpOhtyA0hy06dPEpB90MqRibmSGKunaogNQq7rqANjRD%2BLw0WU52Yu3en%2F%2FJeOQxOv07K6PtwgW7GfdakwUuaAS0WhkXAxNIgPUcZ5fElcbnCMswWQfCGi2oGQaJ7yWyQt873Y8KVsOvih96D95svm%2FHQbAXFXT9ho1xnGdm1d40oj2%2Bezl7sl3kzMgZ5wp2lSsG1XRZ%2B84y2XnrUByroIqLJIukbO1G67cAZd6UkCSJ5Pvxcx93HXspuNolKwRgDs%2BdIyCZ1YeLLvKv7B9L3ZZpgwQO6plsu7kaFoJz0O5pPHaLGO6LMR3jr%2BKd7p%2BaAs8iJhsSBfOO9LJcJSBcYBzIZ%2Bnht4XNI72GjptI5h1Yqz%2B0%2BU%2BKBUs5jW%2FCZFJ8F%2BCatZHJ0C%2B%2FAZZXkVH0pPSP3Ya1EhcbvXPCWOgrQG8U5binGGhiN4Nr4KXcs%2FoMds3BAKVg%2FmpDS1oht5laJs%2BaD6m%2BGEf%2BIg4aAajXiDtOGLYW6zB1T0xLASa2Skwqu54KMI2bTN15jQy3jsPZyX45KwTC02P68BjqkAW7UW1U617%2BYaD%2By6i33d6vR4dDu%2FXAY31fZZcRJMSC1Z8qVxVeaq0pzLhaYuy9rk7ohqISM0Pj55v54gto7UZ9HfpZuVM2%2FPro2FF4AjhXl9%2FgR8zvELnaCKkWDBRrOnMTatzI7U6OGJPzp1sa5ArHQfzvwUKB6UNpMuyFhyIAJ3mBTq2LkNneqLYCbT8PsytiNQgBuh2z7KA%2FeNjobSj5KDkpq&X-Amz-Signature=f6d8d692d52a814aeaab8960e1847e74d085b463184aae68f4ad70faa73ce4f8&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46624PUVWA6%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDWPKhi0K5sY3HuiFwASFg%2FWbt4NqGf%2FLaUDYSWaGw2kQIhAINBD2P6GO3z2XeLfVC%2BhEpU341FGluKL%2F06WSMlw1vdKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy%2BfJ0OllvIR95urkAq3AMrtzU0Jgh5emZMOYUZZdHagdvA%2BK0hGFw9EeU2I6i2e3dlj1cxpqGd7Y2TG6S5O67jD2%2B06GvZ5cLlpoz%2BB%2BaHuwnqMN%2BdzDo%2FpOhtyA0hy06dPEpB90MqRibmSGKunaogNQq7rqANjRD%2BLw0WU52Yu3en%2F%2FJeOQxOv07K6PtwgW7GfdakwUuaAS0WhkXAxNIgPUcZ5fElcbnCMswWQfCGi2oGQaJ7yWyQt873Y8KVsOvih96D95svm%2FHQbAXFXT9ho1xnGdm1d40oj2%2Bezl7sl3kzMgZ5wp2lSsG1XRZ%2B84y2XnrUByroIqLJIukbO1G67cAZd6UkCSJ5Pvxcx93HXspuNolKwRgDs%2BdIyCZ1YeLLvKv7B9L3ZZpgwQO6plsu7kaFoJz0O5pPHaLGO6LMR3jr%2BKd7p%2BaAs8iJhsSBfOO9LJcJSBcYBzIZ%2Bnht4XNI72GjptI5h1Yqz%2B0%2BU%2BKBUs5jW%2FCZFJ8F%2BCatZHJ0C%2B%2FAZZXkVH0pPSP3Ya1EhcbvXPCWOgrQG8U5binGGhiN4Nr4KXcs%2FoMds3BAKVg%2FmpDS1oht5laJs%2BaD6m%2BGEf%2BIg4aAajXiDtOGLYW6zB1T0xLASa2Skwqu54KMI2bTN15jQy3jsPZyX45KwTC02P68BjqkAW7UW1U617%2BYaD%2By6i33d6vR4dDu%2FXAY31fZZcRJMSC1Z8qVxVeaq0pzLhaYuy9rk7ohqISM0Pj55v54gto7UZ9HfpZuVM2%2FPro2FF4AjhXl9%2FgR8zvELnaCKkWDBRrOnMTatzI7U6OGJPzp1sa5ArHQfzvwUKB6UNpMuyFhyIAJ3mBTq2LkNneqLYCbT8PsytiNQgBuh2z7KA%2FeNjobSj5KDkpq&X-Amz-Signature=57301ddf2eb6283cf1ec83079de3419a7139cf0b95cc9ff9f50516be0216ae56&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676ABWFHY%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID9Sae%2BoAMjoORc0bRMzLwBdqheEa6HrssblACTrkePLAiAOs4J3pdC6KqM%2BGzDefOuUNF%2BFq8H70V6asw81cneJHCqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTF8zS0G2DeYqO38iKtwDWr8sEkowyunRwFnKegk8%2Bq42TRV9GL1sFZkZ0Ez53Hm9uocSiJpHRAUaEhWVu5SUl65xE2VDfcZSASrSVqWoe8z%2FVf%2FrJENCckNray8mMBzy4E7ufh2wjpnD%2FEogyxE8sfmk7cEamCB2YGQKzXcABhku2%2B0snezOsCSfbUEJV%2FFVsoIxEy96QTtu1raZjCGEfB2hSsqZ6aS9LOnjlpWTjGRGuQwu26YMq4ME2Bo8Bi%2F8mpmmgVyXD3lJ1bp3YI6shFDlfBMtAQt3GGfJu%2FDioW1QjiJ3Ez06SyNghVdjcHPXBPt3ZAiWfODFvVoEgbaAnF13bYILGgPSdaeEim2hygSJaidgB09A%2BDM7RB3Ev8OgYzDUQYF7%2BiuiJM0GRt%2B3Aod2gWVtBpA3olaw9ZJfa1pMXPMvOF0zoGAbdIpiTA%2ByysmYrdB53orYZxdbejPiz3uK2h8TrWxiodKM84NxWeiz79bnf2%2FZJBE0E%2FiRWCYD55R2IzLadI%2BsJQoiw%2BZunM0Ur5X6buxMdyy64q8vbi1zIB0skb0%2Br1idB6765KY8wrZ7r9ula960mIGcuGJvORMs7bUQwwopQMrr4EdcoevL0VgXG8HSzGc9rjs72srGesGIm0DeR8LbqQUw0N3%2BvAY6pgErLmLp6R3JZ3A4te2Stryp5N%2F%2BPmMq1cIbHZHXPgI0KBAjCFhkZGGbNBNkPo28hW2CEoSG0eX7yOwXW%2Bo5PhbEvquvwBRQJEoM5TEadSIj1FuX8eWlZlZ9LniGyufxBoMdsEX8%2Bsw5dwOYg2LF5%2FVKNuyzFKIAEmbMwPqI9dIbteGxF07G6HrFGza8IcXqgpEuORi4LAioAUMFKXaQw4aYWaOks74q&X-Amz-Signature=38129b3ab68ca2cec66cc763e1200199612501c3d86027b892486a71fec19a8d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676ABWFHY%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID9Sae%2BoAMjoORc0bRMzLwBdqheEa6HrssblACTrkePLAiAOs4J3pdC6KqM%2BGzDefOuUNF%2BFq8H70V6asw81cneJHCqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTF8zS0G2DeYqO38iKtwDWr8sEkowyunRwFnKegk8%2Bq42TRV9GL1sFZkZ0Ez53Hm9uocSiJpHRAUaEhWVu5SUl65xE2VDfcZSASrSVqWoe8z%2FVf%2FrJENCckNray8mMBzy4E7ufh2wjpnD%2FEogyxE8sfmk7cEamCB2YGQKzXcABhku2%2B0snezOsCSfbUEJV%2FFVsoIxEy96QTtu1raZjCGEfB2hSsqZ6aS9LOnjlpWTjGRGuQwu26YMq4ME2Bo8Bi%2F8mpmmgVyXD3lJ1bp3YI6shFDlfBMtAQt3GGfJu%2FDioW1QjiJ3Ez06SyNghVdjcHPXBPt3ZAiWfODFvVoEgbaAnF13bYILGgPSdaeEim2hygSJaidgB09A%2BDM7RB3Ev8OgYzDUQYF7%2BiuiJM0GRt%2B3Aod2gWVtBpA3olaw9ZJfa1pMXPMvOF0zoGAbdIpiTA%2ByysmYrdB53orYZxdbejPiz3uK2h8TrWxiodKM84NxWeiz79bnf2%2FZJBE0E%2FiRWCYD55R2IzLadI%2BsJQoiw%2BZunM0Ur5X6buxMdyy64q8vbi1zIB0skb0%2Br1idB6765KY8wrZ7r9ula960mIGcuGJvORMs7bUQwwopQMrr4EdcoevL0VgXG8HSzGc9rjs72srGesGIm0DeR8LbqQUw0N3%2BvAY6pgErLmLp6R3JZ3A4te2Stryp5N%2F%2BPmMq1cIbHZHXPgI0KBAjCFhkZGGbNBNkPo28hW2CEoSG0eX7yOwXW%2Bo5PhbEvquvwBRQJEoM5TEadSIj1FuX8eWlZlZ9LniGyufxBoMdsEX8%2Bsw5dwOYg2LF5%2FVKNuyzFKIAEmbMwPqI9dIbteGxF07G6HrFGza8IcXqgpEuORi4LAioAUMFKXaQw4aYWaOks74q&X-Amz-Signature=b6b81db1a145cd820de41faf5d373fc4e6d45be09b97ebb092a471fbfb9b8a28&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676ABWFHY%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID9Sae%2BoAMjoORc0bRMzLwBdqheEa6HrssblACTrkePLAiAOs4J3pdC6KqM%2BGzDefOuUNF%2BFq8H70V6asw81cneJHCqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTF8zS0G2DeYqO38iKtwDWr8sEkowyunRwFnKegk8%2Bq42TRV9GL1sFZkZ0Ez53Hm9uocSiJpHRAUaEhWVu5SUl65xE2VDfcZSASrSVqWoe8z%2FVf%2FrJENCckNray8mMBzy4E7ufh2wjpnD%2FEogyxE8sfmk7cEamCB2YGQKzXcABhku2%2B0snezOsCSfbUEJV%2FFVsoIxEy96QTtu1raZjCGEfB2hSsqZ6aS9LOnjlpWTjGRGuQwu26YMq4ME2Bo8Bi%2F8mpmmgVyXD3lJ1bp3YI6shFDlfBMtAQt3GGfJu%2FDioW1QjiJ3Ez06SyNghVdjcHPXBPt3ZAiWfODFvVoEgbaAnF13bYILGgPSdaeEim2hygSJaidgB09A%2BDM7RB3Ev8OgYzDUQYF7%2BiuiJM0GRt%2B3Aod2gWVtBpA3olaw9ZJfa1pMXPMvOF0zoGAbdIpiTA%2ByysmYrdB53orYZxdbejPiz3uK2h8TrWxiodKM84NxWeiz79bnf2%2FZJBE0E%2FiRWCYD55R2IzLadI%2BsJQoiw%2BZunM0Ur5X6buxMdyy64q8vbi1zIB0skb0%2Br1idB6765KY8wrZ7r9ula960mIGcuGJvORMs7bUQwwopQMrr4EdcoevL0VgXG8HSzGc9rjs72srGesGIm0DeR8LbqQUw0N3%2BvAY6pgErLmLp6R3JZ3A4te2Stryp5N%2F%2BPmMq1cIbHZHXPgI0KBAjCFhkZGGbNBNkPo28hW2CEoSG0eX7yOwXW%2Bo5PhbEvquvwBRQJEoM5TEadSIj1FuX8eWlZlZ9LniGyufxBoMdsEX8%2Bsw5dwOYg2LF5%2FVKNuyzFKIAEmbMwPqI9dIbteGxF07G6HrFGza8IcXqgpEuORi4LAioAUMFKXaQw4aYWaOks74q&X-Amz-Signature=2a7856686ece1eb1c0e5d8d75045eee85031d59fc8a60617d3d72040c711378b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676ABWFHY%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID9Sae%2BoAMjoORc0bRMzLwBdqheEa6HrssblACTrkePLAiAOs4J3pdC6KqM%2BGzDefOuUNF%2BFq8H70V6asw81cneJHCqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTF8zS0G2DeYqO38iKtwDWr8sEkowyunRwFnKegk8%2Bq42TRV9GL1sFZkZ0Ez53Hm9uocSiJpHRAUaEhWVu5SUl65xE2VDfcZSASrSVqWoe8z%2FVf%2FrJENCckNray8mMBzy4E7ufh2wjpnD%2FEogyxE8sfmk7cEamCB2YGQKzXcABhku2%2B0snezOsCSfbUEJV%2FFVsoIxEy96QTtu1raZjCGEfB2hSsqZ6aS9LOnjlpWTjGRGuQwu26YMq4ME2Bo8Bi%2F8mpmmgVyXD3lJ1bp3YI6shFDlfBMtAQt3GGfJu%2FDioW1QjiJ3Ez06SyNghVdjcHPXBPt3ZAiWfODFvVoEgbaAnF13bYILGgPSdaeEim2hygSJaidgB09A%2BDM7RB3Ev8OgYzDUQYF7%2BiuiJM0GRt%2B3Aod2gWVtBpA3olaw9ZJfa1pMXPMvOF0zoGAbdIpiTA%2ByysmYrdB53orYZxdbejPiz3uK2h8TrWxiodKM84NxWeiz79bnf2%2FZJBE0E%2FiRWCYD55R2IzLadI%2BsJQoiw%2BZunM0Ur5X6buxMdyy64q8vbi1zIB0skb0%2Br1idB6765KY8wrZ7r9ula960mIGcuGJvORMs7bUQwwopQMrr4EdcoevL0VgXG8HSzGc9rjs72srGesGIm0DeR8LbqQUw0N3%2BvAY6pgErLmLp6R3JZ3A4te2Stryp5N%2F%2BPmMq1cIbHZHXPgI0KBAjCFhkZGGbNBNkPo28hW2CEoSG0eX7yOwXW%2Bo5PhbEvquvwBRQJEoM5TEadSIj1FuX8eWlZlZ9LniGyufxBoMdsEX8%2Bsw5dwOYg2LF5%2FVKNuyzFKIAEmbMwPqI9dIbteGxF07G6HrFGza8IcXqgpEuORi4LAioAUMFKXaQw4aYWaOks74q&X-Amz-Signature=241c36aeaf1262a3df8a73691681871ec8bf239d9745c6eb46e65d128ae7fa3c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676ABWFHY%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID9Sae%2BoAMjoORc0bRMzLwBdqheEa6HrssblACTrkePLAiAOs4J3pdC6KqM%2BGzDefOuUNF%2BFq8H70V6asw81cneJHCqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTF8zS0G2DeYqO38iKtwDWr8sEkowyunRwFnKegk8%2Bq42TRV9GL1sFZkZ0Ez53Hm9uocSiJpHRAUaEhWVu5SUl65xE2VDfcZSASrSVqWoe8z%2FVf%2FrJENCckNray8mMBzy4E7ufh2wjpnD%2FEogyxE8sfmk7cEamCB2YGQKzXcABhku2%2B0snezOsCSfbUEJV%2FFVsoIxEy96QTtu1raZjCGEfB2hSsqZ6aS9LOnjlpWTjGRGuQwu26YMq4ME2Bo8Bi%2F8mpmmgVyXD3lJ1bp3YI6shFDlfBMtAQt3GGfJu%2FDioW1QjiJ3Ez06SyNghVdjcHPXBPt3ZAiWfODFvVoEgbaAnF13bYILGgPSdaeEim2hygSJaidgB09A%2BDM7RB3Ev8OgYzDUQYF7%2BiuiJM0GRt%2B3Aod2gWVtBpA3olaw9ZJfa1pMXPMvOF0zoGAbdIpiTA%2ByysmYrdB53orYZxdbejPiz3uK2h8TrWxiodKM84NxWeiz79bnf2%2FZJBE0E%2FiRWCYD55R2IzLadI%2BsJQoiw%2BZunM0Ur5X6buxMdyy64q8vbi1zIB0skb0%2Br1idB6765KY8wrZ7r9ula960mIGcuGJvORMs7bUQwwopQMrr4EdcoevL0VgXG8HSzGc9rjs72srGesGIm0DeR8LbqQUw0N3%2BvAY6pgErLmLp6R3JZ3A4te2Stryp5N%2F%2BPmMq1cIbHZHXPgI0KBAjCFhkZGGbNBNkPo28hW2CEoSG0eX7yOwXW%2Bo5PhbEvquvwBRQJEoM5TEadSIj1FuX8eWlZlZ9LniGyufxBoMdsEX8%2Bsw5dwOYg2LF5%2FVKNuyzFKIAEmbMwPqI9dIbteGxF07G6HrFGza8IcXqgpEuORi4LAioAUMFKXaQw4aYWaOks74q&X-Amz-Signature=174fe6c394110fa06091d9e9efa93ac6e7959a048371f2a8951a0ce30e97dcc6&X-Amz-SignedHeaders=host&x-id=GetObject)
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


