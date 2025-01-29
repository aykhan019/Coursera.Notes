

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TNHR3PO%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091514Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH2QARjNlvJqsW39JvYK7KBLVDFHUdjLowuF6HbYBmAZAiEAn7B64Rf7i6h8sIRdcmFPJm5RxLyUdyjGok3LJhFpwnIqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHfNIFSxOLiqv25vhSrcA3xoW84zcxduRd5Dc5EjfD6rqv90edts6bfdHiGvANEIIXmUyp28igXA64sPNNkQik5Ake%2BNtAk%2F0VD0yqYCYzR1QueKnceixgLbw8%2FLR9yhE%2B5R4dYSQCq%2BwBHBMgW5%2B8LhjihiiyYEdeJci1fDqhwAvsic4UZlxQGFSR5FAh%2B%2FcH7EKIDmodxJ2VNErH8o4vCLmszGwAlcM0kZKpYfY2dXqpGoiYCQnTgBL0V36r02fYX3o%2FHOfuLwzUItXSQ1k6bLlhCIsWVqxWLF9Skf7rEV9m1C3smK5bYdDw0oLceqgIk8hS6hVGJ120D9Q%2Bexm5%2FvlAPos2k9fN%2FBwy7yJK4s8HUevc7%2FvOUk6jHLl6IWJl3mNgkSW7U6tWAq5%2FVyHzSiqTQ3rTWp%2Fx6WzeaVQqH9QqmVuvp%2F8LlzpfC1eXa35uAPoqDSiYAB%2BDOhEym2AJF%2BZVibIKtwuciOZlwMLmSw2cSc4DA2oIVr5godjelk1XGm2nzfciNV6MYrkIfMrKSWVHg7Y2b1GutXFv3FHbrs%2BFO0jt9TUnM3FXmI6G4S82uBUNAAyg7mD3gfYSOiHmuMUdim4mDwWoD3LqisFBW16PdGipf3vWR3VWCaV1GuCvkE7XEXZD9rwewUMJrH57wGOqUB6IKXgal%2FFEzBrxSjZOEc3o5EfIRmcc8%2Fa2ER1ZePw%2Be9%2B0vCersKBAva3G%2BArGafEeLlOwcjwD9B8qRVOn2OYimzrX0GYxeXg8bRTfmD8FpKzftmCkte3xOLbbiMnJ2hCAQKR3MbmWVdP%2F28XpWndYuIqbO%2BncGKXfz46gIoZ671P9gfzUbSXe6%2FsYABVWsOb2gakm0y7QuxUvx%2BsoI8aU8AMMvU&X-Amz-Signature=267dbfdcbd68ff4490d79a6ed74604389773c6b3bcb27b7deff7f103c79e11b9&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UEVZH55O%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091515Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHDK8%2FolNfz4MZ4JYXc9ccgy9OkijUnTdHqIPxVLWYjDAiEAwBTXdLi45HWwRDxeXb%2BZH1sppE3l%2B9u1gtG8gDOSbMwqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGimTZBKSg3d%2BlSbFCrcA1SAwddJiZyzJTPj9WmwhnX0%2BFARwnW2qEl%2F0wpig%2BmlTzY8sVCN4Y%2BfhVsZZek5WTIzu2OwYb6x%2BpX4KTSdLXZfESkzxRHJQBp%2FaD6Z5yxL%2BnCjbYkC2xYLTaCnGAu%2B0jbFytdL4InX%2BXaW9d709ID2zoFoIZ2JDSJlyGxynzMG%2BQQJE0QrhE7J2rH5ax0v7F1o52we9KNICoHd2aKSuUxUm0mO8HcPh1bVS1NwhYHivpFtlT7tGlc2Q3R0zjg0%2FcmLqTcBHt%2F3pGmkDCI39EWGYs%2Bfa9gAZm1RVn4O2bpI%2FQplVTONRByV7DxNOPO8namwyGPtiu53ym%2F%2Fox1K4cNKxZxP5bLj7xQNx9umVwPEn5uL4MqdpYekb%2FnWQyACZWrpg0GVf8GCml4gWHuJbHLrnZj6m4A2O2A%2BodvKwlIlCq3O63g0AaxmtOUuGIYYb4nGv70H41jcDyD4nHC%2Fnkn1sCxUU44XP%2BLPlVAAeqPn%2FkzNZHQsDaQbtSUL6S2LHm%2BYXV%2BMmjhVyG9%2FVZ29UTqBzVqhtYtTsmdgBh0KshHZb7NzX23FTSyQh8GW7Osbgk6L%2FKfvY%2B90ToJAbXGYXbD3CHO2%2F9DsF1IWmFiJ%2FYUObueaxsJ2NWctVMNbMPXH57wGOqUB8Al6IzAXZ8MdZ0zCdpyZuMt0EMsw4rZEy%2FciFm2rLGDCL%2B2e0FPxHBRgmP3l8wdHl%2FQICfONBZoWMW%2BYur%2FrYY4QtdKRuE2ZyAsHJM%2FBiJvCRotGe8RrDY8E2HQ0YgFaxpGRLF3PiF%2B96NZ5AV8yMSZ79UbuyfPuRwFu%2BNHYJzlPw2iKMxy3i%2FRz1EJAGg%2BykWM6Mi9oIzsAH9NSY9j36FBRXziR&X-Amz-Signature=c4a10f84487be6c78cd94c0c3545cf1f7f0a3c39d508ab76ee6065c1af66df2c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UEVZH55O%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091515Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHDK8%2FolNfz4MZ4JYXc9ccgy9OkijUnTdHqIPxVLWYjDAiEAwBTXdLi45HWwRDxeXb%2BZH1sppE3l%2B9u1gtG8gDOSbMwqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGimTZBKSg3d%2BlSbFCrcA1SAwddJiZyzJTPj9WmwhnX0%2BFARwnW2qEl%2F0wpig%2BmlTzY8sVCN4Y%2BfhVsZZek5WTIzu2OwYb6x%2BpX4KTSdLXZfESkzxRHJQBp%2FaD6Z5yxL%2BnCjbYkC2xYLTaCnGAu%2B0jbFytdL4InX%2BXaW9d709ID2zoFoIZ2JDSJlyGxynzMG%2BQQJE0QrhE7J2rH5ax0v7F1o52we9KNICoHd2aKSuUxUm0mO8HcPh1bVS1NwhYHivpFtlT7tGlc2Q3R0zjg0%2FcmLqTcBHt%2F3pGmkDCI39EWGYs%2Bfa9gAZm1RVn4O2bpI%2FQplVTONRByV7DxNOPO8namwyGPtiu53ym%2F%2Fox1K4cNKxZxP5bLj7xQNx9umVwPEn5uL4MqdpYekb%2FnWQyACZWrpg0GVf8GCml4gWHuJbHLrnZj6m4A2O2A%2BodvKwlIlCq3O63g0AaxmtOUuGIYYb4nGv70H41jcDyD4nHC%2Fnkn1sCxUU44XP%2BLPlVAAeqPn%2FkzNZHQsDaQbtSUL6S2LHm%2BYXV%2BMmjhVyG9%2FVZ29UTqBzVqhtYtTsmdgBh0KshHZb7NzX23FTSyQh8GW7Osbgk6L%2FKfvY%2B90ToJAbXGYXbD3CHO2%2F9DsF1IWmFiJ%2FYUObueaxsJ2NWctVMNbMPXH57wGOqUB8Al6IzAXZ8MdZ0zCdpyZuMt0EMsw4rZEy%2FciFm2rLGDCL%2B2e0FPxHBRgmP3l8wdHl%2FQICfONBZoWMW%2BYur%2FrYY4QtdKRuE2ZyAsHJM%2FBiJvCRotGe8RrDY8E2HQ0YgFaxpGRLF3PiF%2B96NZ5AV8yMSZ79UbuyfPuRwFu%2BNHYJzlPw2iKMxy3i%2FRz1EJAGg%2BykWM6Mi9oIzsAH9NSY9j36FBRXziR&X-Amz-Signature=4c9f20472f3d6564ac2667868b8c20839a03c695ee48662231449c17feab30bd&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UEVZH55O%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091515Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHDK8%2FolNfz4MZ4JYXc9ccgy9OkijUnTdHqIPxVLWYjDAiEAwBTXdLi45HWwRDxeXb%2BZH1sppE3l%2B9u1gtG8gDOSbMwqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGimTZBKSg3d%2BlSbFCrcA1SAwddJiZyzJTPj9WmwhnX0%2BFARwnW2qEl%2F0wpig%2BmlTzY8sVCN4Y%2BfhVsZZek5WTIzu2OwYb6x%2BpX4KTSdLXZfESkzxRHJQBp%2FaD6Z5yxL%2BnCjbYkC2xYLTaCnGAu%2B0jbFytdL4InX%2BXaW9d709ID2zoFoIZ2JDSJlyGxynzMG%2BQQJE0QrhE7J2rH5ax0v7F1o52we9KNICoHd2aKSuUxUm0mO8HcPh1bVS1NwhYHivpFtlT7tGlc2Q3R0zjg0%2FcmLqTcBHt%2F3pGmkDCI39EWGYs%2Bfa9gAZm1RVn4O2bpI%2FQplVTONRByV7DxNOPO8namwyGPtiu53ym%2F%2Fox1K4cNKxZxP5bLj7xQNx9umVwPEn5uL4MqdpYekb%2FnWQyACZWrpg0GVf8GCml4gWHuJbHLrnZj6m4A2O2A%2BodvKwlIlCq3O63g0AaxmtOUuGIYYb4nGv70H41jcDyD4nHC%2Fnkn1sCxUU44XP%2BLPlVAAeqPn%2FkzNZHQsDaQbtSUL6S2LHm%2BYXV%2BMmjhVyG9%2FVZ29UTqBzVqhtYtTsmdgBh0KshHZb7NzX23FTSyQh8GW7Osbgk6L%2FKfvY%2B90ToJAbXGYXbD3CHO2%2F9DsF1IWmFiJ%2FYUObueaxsJ2NWctVMNbMPXH57wGOqUB8Al6IzAXZ8MdZ0zCdpyZuMt0EMsw4rZEy%2FciFm2rLGDCL%2B2e0FPxHBRgmP3l8wdHl%2FQICfONBZoWMW%2BYur%2FrYY4QtdKRuE2ZyAsHJM%2FBiJvCRotGe8RrDY8E2HQ0YgFaxpGRLF3PiF%2B96NZ5AV8yMSZ79UbuyfPuRwFu%2BNHYJzlPw2iKMxy3i%2FRz1EJAGg%2BykWM6Mi9oIzsAH9NSY9j36FBRXziR&X-Amz-Signature=4bb515ce667e96cccd5f6f11fec6d3ba755a3f262da006003aafbc27755e9f9c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UEVZH55O%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091515Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHDK8%2FolNfz4MZ4JYXc9ccgy9OkijUnTdHqIPxVLWYjDAiEAwBTXdLi45HWwRDxeXb%2BZH1sppE3l%2B9u1gtG8gDOSbMwqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGimTZBKSg3d%2BlSbFCrcA1SAwddJiZyzJTPj9WmwhnX0%2BFARwnW2qEl%2F0wpig%2BmlTzY8sVCN4Y%2BfhVsZZek5WTIzu2OwYb6x%2BpX4KTSdLXZfESkzxRHJQBp%2FaD6Z5yxL%2BnCjbYkC2xYLTaCnGAu%2B0jbFytdL4InX%2BXaW9d709ID2zoFoIZ2JDSJlyGxynzMG%2BQQJE0QrhE7J2rH5ax0v7F1o52we9KNICoHd2aKSuUxUm0mO8HcPh1bVS1NwhYHivpFtlT7tGlc2Q3R0zjg0%2FcmLqTcBHt%2F3pGmkDCI39EWGYs%2Bfa9gAZm1RVn4O2bpI%2FQplVTONRByV7DxNOPO8namwyGPtiu53ym%2F%2Fox1K4cNKxZxP5bLj7xQNx9umVwPEn5uL4MqdpYekb%2FnWQyACZWrpg0GVf8GCml4gWHuJbHLrnZj6m4A2O2A%2BodvKwlIlCq3O63g0AaxmtOUuGIYYb4nGv70H41jcDyD4nHC%2Fnkn1sCxUU44XP%2BLPlVAAeqPn%2FkzNZHQsDaQbtSUL6S2LHm%2BYXV%2BMmjhVyG9%2FVZ29UTqBzVqhtYtTsmdgBh0KshHZb7NzX23FTSyQh8GW7Osbgk6L%2FKfvY%2B90ToJAbXGYXbD3CHO2%2F9DsF1IWmFiJ%2FYUObueaxsJ2NWctVMNbMPXH57wGOqUB8Al6IzAXZ8MdZ0zCdpyZuMt0EMsw4rZEy%2FciFm2rLGDCL%2B2e0FPxHBRgmP3l8wdHl%2FQICfONBZoWMW%2BYur%2FrYY4QtdKRuE2ZyAsHJM%2FBiJvCRotGe8RrDY8E2HQ0YgFaxpGRLF3PiF%2B96NZ5AV8yMSZ79UbuyfPuRwFu%2BNHYJzlPw2iKMxy3i%2FRz1EJAGg%2BykWM6Mi9oIzsAH9NSY9j36FBRXziR&X-Amz-Signature=72950ecaec0b3746bb7ae1c4d8fc482bbf5f251e42fde447c0fa8faa954427e6&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UEVZH55O%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091515Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHDK8%2FolNfz4MZ4JYXc9ccgy9OkijUnTdHqIPxVLWYjDAiEAwBTXdLi45HWwRDxeXb%2BZH1sppE3l%2B9u1gtG8gDOSbMwqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGimTZBKSg3d%2BlSbFCrcA1SAwddJiZyzJTPj9WmwhnX0%2BFARwnW2qEl%2F0wpig%2BmlTzY8sVCN4Y%2BfhVsZZek5WTIzu2OwYb6x%2BpX4KTSdLXZfESkzxRHJQBp%2FaD6Z5yxL%2BnCjbYkC2xYLTaCnGAu%2B0jbFytdL4InX%2BXaW9d709ID2zoFoIZ2JDSJlyGxynzMG%2BQQJE0QrhE7J2rH5ax0v7F1o52we9KNICoHd2aKSuUxUm0mO8HcPh1bVS1NwhYHivpFtlT7tGlc2Q3R0zjg0%2FcmLqTcBHt%2F3pGmkDCI39EWGYs%2Bfa9gAZm1RVn4O2bpI%2FQplVTONRByV7DxNOPO8namwyGPtiu53ym%2F%2Fox1K4cNKxZxP5bLj7xQNx9umVwPEn5uL4MqdpYekb%2FnWQyACZWrpg0GVf8GCml4gWHuJbHLrnZj6m4A2O2A%2BodvKwlIlCq3O63g0AaxmtOUuGIYYb4nGv70H41jcDyD4nHC%2Fnkn1sCxUU44XP%2BLPlVAAeqPn%2FkzNZHQsDaQbtSUL6S2LHm%2BYXV%2BMmjhVyG9%2FVZ29UTqBzVqhtYtTsmdgBh0KshHZb7NzX23FTSyQh8GW7Osbgk6L%2FKfvY%2B90ToJAbXGYXbD3CHO2%2F9DsF1IWmFiJ%2FYUObueaxsJ2NWctVMNbMPXH57wGOqUB8Al6IzAXZ8MdZ0zCdpyZuMt0EMsw4rZEy%2FciFm2rLGDCL%2B2e0FPxHBRgmP3l8wdHl%2FQICfONBZoWMW%2BYur%2FrYY4QtdKRuE2ZyAsHJM%2FBiJvCRotGe8RrDY8E2HQ0YgFaxpGRLF3PiF%2B96NZ5AV8yMSZ79UbuyfPuRwFu%2BNHYJzlPw2iKMxy3i%2FRz1EJAGg%2BykWM6Mi9oIzsAH9NSY9j36FBRXziR&X-Amz-Signature=3bf711d3167b8eb0f382304c2f47118e2a70a4ae421a03a985840c94acf6fc93&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TNHR3PO%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091514Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH2QARjNlvJqsW39JvYK7KBLVDFHUdjLowuF6HbYBmAZAiEAn7B64Rf7i6h8sIRdcmFPJm5RxLyUdyjGok3LJhFpwnIqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHfNIFSxOLiqv25vhSrcA3xoW84zcxduRd5Dc5EjfD6rqv90edts6bfdHiGvANEIIXmUyp28igXA64sPNNkQik5Ake%2BNtAk%2F0VD0yqYCYzR1QueKnceixgLbw8%2FLR9yhE%2B5R4dYSQCq%2BwBHBMgW5%2B8LhjihiiyYEdeJci1fDqhwAvsic4UZlxQGFSR5FAh%2B%2FcH7EKIDmodxJ2VNErH8o4vCLmszGwAlcM0kZKpYfY2dXqpGoiYCQnTgBL0V36r02fYX3o%2FHOfuLwzUItXSQ1k6bLlhCIsWVqxWLF9Skf7rEV9m1C3smK5bYdDw0oLceqgIk8hS6hVGJ120D9Q%2Bexm5%2FvlAPos2k9fN%2FBwy7yJK4s8HUevc7%2FvOUk6jHLl6IWJl3mNgkSW7U6tWAq5%2FVyHzSiqTQ3rTWp%2Fx6WzeaVQqH9QqmVuvp%2F8LlzpfC1eXa35uAPoqDSiYAB%2BDOhEym2AJF%2BZVibIKtwuciOZlwMLmSw2cSc4DA2oIVr5godjelk1XGm2nzfciNV6MYrkIfMrKSWVHg7Y2b1GutXFv3FHbrs%2BFO0jt9TUnM3FXmI6G4S82uBUNAAyg7mD3gfYSOiHmuMUdim4mDwWoD3LqisFBW16PdGipf3vWR3VWCaV1GuCvkE7XEXZD9rwewUMJrH57wGOqUB6IKXgal%2FFEzBrxSjZOEc3o5EfIRmcc8%2Fa2ER1ZePw%2Be9%2B0vCersKBAva3G%2BArGafEeLlOwcjwD9B8qRVOn2OYimzrX0GYxeXg8bRTfmD8FpKzftmCkte3xOLbbiMnJ2hCAQKR3MbmWVdP%2F28XpWndYuIqbO%2BncGKXfz46gIoZ671P9gfzUbSXe6%2FsYABVWsOb2gakm0y7QuxUvx%2BsoI8aU8AMMvU&X-Amz-Signature=b74685104b7dbbcf6674bc18ba135dbc5595fde4a8345c25da77e8cafd157894&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TNHR3PO%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091514Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH2QARjNlvJqsW39JvYK7KBLVDFHUdjLowuF6HbYBmAZAiEAn7B64Rf7i6h8sIRdcmFPJm5RxLyUdyjGok3LJhFpwnIqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHfNIFSxOLiqv25vhSrcA3xoW84zcxduRd5Dc5EjfD6rqv90edts6bfdHiGvANEIIXmUyp28igXA64sPNNkQik5Ake%2BNtAk%2F0VD0yqYCYzR1QueKnceixgLbw8%2FLR9yhE%2B5R4dYSQCq%2BwBHBMgW5%2B8LhjihiiyYEdeJci1fDqhwAvsic4UZlxQGFSR5FAh%2B%2FcH7EKIDmodxJ2VNErH8o4vCLmszGwAlcM0kZKpYfY2dXqpGoiYCQnTgBL0V36r02fYX3o%2FHOfuLwzUItXSQ1k6bLlhCIsWVqxWLF9Skf7rEV9m1C3smK5bYdDw0oLceqgIk8hS6hVGJ120D9Q%2Bexm5%2FvlAPos2k9fN%2FBwy7yJK4s8HUevc7%2FvOUk6jHLl6IWJl3mNgkSW7U6tWAq5%2FVyHzSiqTQ3rTWp%2Fx6WzeaVQqH9QqmVuvp%2F8LlzpfC1eXa35uAPoqDSiYAB%2BDOhEym2AJF%2BZVibIKtwuciOZlwMLmSw2cSc4DA2oIVr5godjelk1XGm2nzfciNV6MYrkIfMrKSWVHg7Y2b1GutXFv3FHbrs%2BFO0jt9TUnM3FXmI6G4S82uBUNAAyg7mD3gfYSOiHmuMUdim4mDwWoD3LqisFBW16PdGipf3vWR3VWCaV1GuCvkE7XEXZD9rwewUMJrH57wGOqUB6IKXgal%2FFEzBrxSjZOEc3o5EfIRmcc8%2Fa2ER1ZePw%2Be9%2B0vCersKBAva3G%2BArGafEeLlOwcjwD9B8qRVOn2OYimzrX0GYxeXg8bRTfmD8FpKzftmCkte3xOLbbiMnJ2hCAQKR3MbmWVdP%2F28XpWndYuIqbO%2BncGKXfz46gIoZ671P9gfzUbSXe6%2FsYABVWsOb2gakm0y7QuxUvx%2BsoI8aU8AMMvU&X-Amz-Signature=efbb1b821af6cbe495f6922eb5bc5c86275f0244876c51859ba38146ca959072&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TNHR3PO%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091514Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH2QARjNlvJqsW39JvYK7KBLVDFHUdjLowuF6HbYBmAZAiEAn7B64Rf7i6h8sIRdcmFPJm5RxLyUdyjGok3LJhFpwnIqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHfNIFSxOLiqv25vhSrcA3xoW84zcxduRd5Dc5EjfD6rqv90edts6bfdHiGvANEIIXmUyp28igXA64sPNNkQik5Ake%2BNtAk%2F0VD0yqYCYzR1QueKnceixgLbw8%2FLR9yhE%2B5R4dYSQCq%2BwBHBMgW5%2B8LhjihiiyYEdeJci1fDqhwAvsic4UZlxQGFSR5FAh%2B%2FcH7EKIDmodxJ2VNErH8o4vCLmszGwAlcM0kZKpYfY2dXqpGoiYCQnTgBL0V36r02fYX3o%2FHOfuLwzUItXSQ1k6bLlhCIsWVqxWLF9Skf7rEV9m1C3smK5bYdDw0oLceqgIk8hS6hVGJ120D9Q%2Bexm5%2FvlAPos2k9fN%2FBwy7yJK4s8HUevc7%2FvOUk6jHLl6IWJl3mNgkSW7U6tWAq5%2FVyHzSiqTQ3rTWp%2Fx6WzeaVQqH9QqmVuvp%2F8LlzpfC1eXa35uAPoqDSiYAB%2BDOhEym2AJF%2BZVibIKtwuciOZlwMLmSw2cSc4DA2oIVr5godjelk1XGm2nzfciNV6MYrkIfMrKSWVHg7Y2b1GutXFv3FHbrs%2BFO0jt9TUnM3FXmI6G4S82uBUNAAyg7mD3gfYSOiHmuMUdim4mDwWoD3LqisFBW16PdGipf3vWR3VWCaV1GuCvkE7XEXZD9rwewUMJrH57wGOqUB6IKXgal%2FFEzBrxSjZOEc3o5EfIRmcc8%2Fa2ER1ZePw%2Be9%2B0vCersKBAva3G%2BArGafEeLlOwcjwD9B8qRVOn2OYimzrX0GYxeXg8bRTfmD8FpKzftmCkte3xOLbbiMnJ2hCAQKR3MbmWVdP%2F28XpWndYuIqbO%2BncGKXfz46gIoZ671P9gfzUbSXe6%2FsYABVWsOb2gakm0y7QuxUvx%2BsoI8aU8AMMvU&X-Amz-Signature=da59a54861c87a93a75ee92a2ed16d07200d11fa0b55f7a094be7af3bbaba15b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TNHR3PO%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091514Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH2QARjNlvJqsW39JvYK7KBLVDFHUdjLowuF6HbYBmAZAiEAn7B64Rf7i6h8sIRdcmFPJm5RxLyUdyjGok3LJhFpwnIqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHfNIFSxOLiqv25vhSrcA3xoW84zcxduRd5Dc5EjfD6rqv90edts6bfdHiGvANEIIXmUyp28igXA64sPNNkQik5Ake%2BNtAk%2F0VD0yqYCYzR1QueKnceixgLbw8%2FLR9yhE%2B5R4dYSQCq%2BwBHBMgW5%2B8LhjihiiyYEdeJci1fDqhwAvsic4UZlxQGFSR5FAh%2B%2FcH7EKIDmodxJ2VNErH8o4vCLmszGwAlcM0kZKpYfY2dXqpGoiYCQnTgBL0V36r02fYX3o%2FHOfuLwzUItXSQ1k6bLlhCIsWVqxWLF9Skf7rEV9m1C3smK5bYdDw0oLceqgIk8hS6hVGJ120D9Q%2Bexm5%2FvlAPos2k9fN%2FBwy7yJK4s8HUevc7%2FvOUk6jHLl6IWJl3mNgkSW7U6tWAq5%2FVyHzSiqTQ3rTWp%2Fx6WzeaVQqH9QqmVuvp%2F8LlzpfC1eXa35uAPoqDSiYAB%2BDOhEym2AJF%2BZVibIKtwuciOZlwMLmSw2cSc4DA2oIVr5godjelk1XGm2nzfciNV6MYrkIfMrKSWVHg7Y2b1GutXFv3FHbrs%2BFO0jt9TUnM3FXmI6G4S82uBUNAAyg7mD3gfYSOiHmuMUdim4mDwWoD3LqisFBW16PdGipf3vWR3VWCaV1GuCvkE7XEXZD9rwewUMJrH57wGOqUB6IKXgal%2FFEzBrxSjZOEc3o5EfIRmcc8%2Fa2ER1ZePw%2Be9%2B0vCersKBAva3G%2BArGafEeLlOwcjwD9B8qRVOn2OYimzrX0GYxeXg8bRTfmD8FpKzftmCkte3xOLbbiMnJ2hCAQKR3MbmWVdP%2F28XpWndYuIqbO%2BncGKXfz46gIoZ671P9gfzUbSXe6%2FsYABVWsOb2gakm0y7QuxUvx%2BsoI8aU8AMMvU&X-Amz-Signature=ef202a1311c9349a8ca6aa35f3d4cfca2737d86172a29c7ef06cc88d0eef0f6a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TNHR3PO%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091514Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH2QARjNlvJqsW39JvYK7KBLVDFHUdjLowuF6HbYBmAZAiEAn7B64Rf7i6h8sIRdcmFPJm5RxLyUdyjGok3LJhFpwnIqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHfNIFSxOLiqv25vhSrcA3xoW84zcxduRd5Dc5EjfD6rqv90edts6bfdHiGvANEIIXmUyp28igXA64sPNNkQik5Ake%2BNtAk%2F0VD0yqYCYzR1QueKnceixgLbw8%2FLR9yhE%2B5R4dYSQCq%2BwBHBMgW5%2B8LhjihiiyYEdeJci1fDqhwAvsic4UZlxQGFSR5FAh%2B%2FcH7EKIDmodxJ2VNErH8o4vCLmszGwAlcM0kZKpYfY2dXqpGoiYCQnTgBL0V36r02fYX3o%2FHOfuLwzUItXSQ1k6bLlhCIsWVqxWLF9Skf7rEV9m1C3smK5bYdDw0oLceqgIk8hS6hVGJ120D9Q%2Bexm5%2FvlAPos2k9fN%2FBwy7yJK4s8HUevc7%2FvOUk6jHLl6IWJl3mNgkSW7U6tWAq5%2FVyHzSiqTQ3rTWp%2Fx6WzeaVQqH9QqmVuvp%2F8LlzpfC1eXa35uAPoqDSiYAB%2BDOhEym2AJF%2BZVibIKtwuciOZlwMLmSw2cSc4DA2oIVr5godjelk1XGm2nzfciNV6MYrkIfMrKSWVHg7Y2b1GutXFv3FHbrs%2BFO0jt9TUnM3FXmI6G4S82uBUNAAyg7mD3gfYSOiHmuMUdim4mDwWoD3LqisFBW16PdGipf3vWR3VWCaV1GuCvkE7XEXZD9rwewUMJrH57wGOqUB6IKXgal%2FFEzBrxSjZOEc3o5EfIRmcc8%2Fa2ER1ZePw%2Be9%2B0vCersKBAva3G%2BArGafEeLlOwcjwD9B8qRVOn2OYimzrX0GYxeXg8bRTfmD8FpKzftmCkte3xOLbbiMnJ2hCAQKR3MbmWVdP%2F28XpWndYuIqbO%2BncGKXfz46gIoZ671P9gfzUbSXe6%2FsYABVWsOb2gakm0y7QuxUvx%2BsoI8aU8AMMvU&X-Amz-Signature=d1b62f3b7ca77af9a9fe331cb0333e932194dab08fdaa8785c0154b15f8ec4fe&X-Amz-SignedHeaders=host&x-id=GetObject)
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


