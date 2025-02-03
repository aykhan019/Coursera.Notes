

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TR7UCLDF%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJIMEYCIQDU9QODHudD7P6V1iu86UVMraFAjOtbffl2ccd2Ij0%2BUwIhALuvlRt%2BPUh4t7RFOo9R8%2FP29rvzkeiiF0kXKQdChQmUKv8DCB8QABoMNjM3NDIzMTgzODA1IgzoqFTfxRLyeueh%2Ffkq3APLqPBBCKc44g5%2BrrA34Fd2Nup6yL8AbmfBBWcK8vuxTrkC46b9IQVp0qkZEBFuOOKVtTGf6Ov5ama%2BIyyDkPFsAr3jn78UPEPM9Q24Td1L6zf7eRjcMshjL3UwtcVkfY1z1gciYgtTn5n9QIZbojGSXkc9JR0%2BPyonjV3TYsGMERlX4nMhwNU5wug%2BAZPRHco1YYfbO6zMeCi%2BOTNslHQyjWKWcwEDcs0PuuCvG3Jzl3JuE9fhLASOujL%2BIBNEqg9yKZCFMju1KQdZntYIVwkc3WMiifLOnX6lcoLxxpHe%2FGGH2Fyt0S08ym9VRrrG%2BiwPi851uQYz2mDm3li%2BzKMYZ5Bd7dNHkcNBtpS5QqSydhz6q39b9zzvyZXqHR%2FEg1%2Fnr%2B0LZj%2FL%2FkGZbSMPlwRK4V5d6RR2a15cvkIJ%2FJThc4kZSrijwNhesv%2BgAM0JC4QubuWG6rM2wh0%2BNBgdk5A1gZnq0c33c7wo3YM%2BFD7HXVbEbVLRVzdxZiQBHOZtelKjStpXIyL4BIHhiUdQ778EmU%2B3MkO4xF411c%2B%2Bq8O7End%2BPTfNcGA5ab5gQPU%2FIsVmhi%2BewqPaL8Iv7ea8ib%2Bny3qawR0Pb5yxgeNP64YdRynm6xiU1j2aJL%2BxJTCp94S9BjqkAZIy8YPVdqQ1fk8sfCnQk3EblK8PHnGmbIbT84IvxRGZG3DLUCmRiI8qJzB%2BTK1eHj3UtSdNT0mqlhxuxLxK6Q2YZfUaMLruoo0H5pDKwCqYALNhh9YLGjqN5ihZBLLy%2BbUd5g6iaiYc5n3potRYcfZsLoc45EC%2FlC6awRSikiAb1NhTgq0iYSsEmDDUSk0SKszdkuJeq2V9inmU%2F3iTnONcQbTW&X-Amz-Signature=5e567ef7a6506c0b999f0cb8f1873637ef526db0122a08efddffc4124d7e0f8d&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677JKK4XV%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIQDzSe5JlWkOFOds%2BvdTcjdvb1%2BM4oe6vLYjGD9V0AnRegIgRAzGRIfLbQcpn3Yw9FIZ%2FhR8P5EiW9uAlWOqlvtE5B0q%2FwMIHxAAGgw2Mzc0MjMxODM4MDUiDLXrp%2BIQ0bqoe63IBCrcA2NGyYRmfMhuJfA2uymZ8EQXN1oK58dIIdVuqHRIO6vGngujQJYPzd0kKb6Lo8R0PeWXu5h1WTPdUmQ7JkUzQGVF6Ia73o8NKKw0Bu61XQ2SPcsP%2BdhrzQRadOq50EUNKzkMu8powfsIQE0skrJxZCTxahHWWE89SiJVGcGUXBKda0TDQE9Uak2xsgcihSy7xGkbRMssVHfDVNVDOhAaa%2F5IbVOI1%2Bh9O1NYWGeMgDI%2F8uixXHYhLtCuHnWPyRl4gM6ETHfWDuM7vK2iYOoIKaoBrqBR6RklOGLxgV46HxQ2i2CgPpV98nRoQVJeaPWY7kCNZ5GgDVyFlOA8ASuFk3QZoMCY4kMzytvOP7Bn4QYaBSDCTBdhvEg6fOlUOXvSCEd7UMaQr2zMpwdgV2QMpHYD070zYBzZooHfAiXpxUQQMNhx8%2FKYQUM3%2FJ9Kx2Xs7eqRovkNNF7DJpXNGa4bIOsLfqU3je47YfLH%2B6ovSWG5SB3fEWHVCPETAY0kQWG6d5ABCyxplhPrXwsonWwZWV97SN%2FfWuAnBK7cQcmdWXKNP%2FQLrCbFsZalb9kERVUH62ExcGghds3PEq9af0LibGZztt4VpyiRX9OoDGRqWp5rXp44d6PtdmKG1Kg8MPH2hL0GOqUBy%2BcBAr12oy1k518SdMz5QPNLCoz%2BNyOBJAjNakuML6qd3yzRhOeiuv7jRdpI%2FNrRPGWM8C9MlNMvEYPLzNU3Wj0SlaJtjswdPoDi0TspFMqI6ppvA2y68rsaiuoHXYnpkIRnoQkWsLSNuIlQei%2BQLTJ44GThHjDLkBis5%2FAow8vqHwLH4b5r6A7XJWJB4rBeliKGBRDLPpwBBZhy9p5OWyRPXhLr&X-Amz-Signature=fd231e7a4fb8fb5c74b883da444b7d628dac8fb02b18bf88bdca1fd65255fdd2&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677JKK4XV%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIQDzSe5JlWkOFOds%2BvdTcjdvb1%2BM4oe6vLYjGD9V0AnRegIgRAzGRIfLbQcpn3Yw9FIZ%2FhR8P5EiW9uAlWOqlvtE5B0q%2FwMIHxAAGgw2Mzc0MjMxODM4MDUiDLXrp%2BIQ0bqoe63IBCrcA2NGyYRmfMhuJfA2uymZ8EQXN1oK58dIIdVuqHRIO6vGngujQJYPzd0kKb6Lo8R0PeWXu5h1WTPdUmQ7JkUzQGVF6Ia73o8NKKw0Bu61XQ2SPcsP%2BdhrzQRadOq50EUNKzkMu8powfsIQE0skrJxZCTxahHWWE89SiJVGcGUXBKda0TDQE9Uak2xsgcihSy7xGkbRMssVHfDVNVDOhAaa%2F5IbVOI1%2Bh9O1NYWGeMgDI%2F8uixXHYhLtCuHnWPyRl4gM6ETHfWDuM7vK2iYOoIKaoBrqBR6RklOGLxgV46HxQ2i2CgPpV98nRoQVJeaPWY7kCNZ5GgDVyFlOA8ASuFk3QZoMCY4kMzytvOP7Bn4QYaBSDCTBdhvEg6fOlUOXvSCEd7UMaQr2zMpwdgV2QMpHYD070zYBzZooHfAiXpxUQQMNhx8%2FKYQUM3%2FJ9Kx2Xs7eqRovkNNF7DJpXNGa4bIOsLfqU3je47YfLH%2B6ovSWG5SB3fEWHVCPETAY0kQWG6d5ABCyxplhPrXwsonWwZWV97SN%2FfWuAnBK7cQcmdWXKNP%2FQLrCbFsZalb9kERVUH62ExcGghds3PEq9af0LibGZztt4VpyiRX9OoDGRqWp5rXp44d6PtdmKG1Kg8MPH2hL0GOqUBy%2BcBAr12oy1k518SdMz5QPNLCoz%2BNyOBJAjNakuML6qd3yzRhOeiuv7jRdpI%2FNrRPGWM8C9MlNMvEYPLzNU3Wj0SlaJtjswdPoDi0TspFMqI6ppvA2y68rsaiuoHXYnpkIRnoQkWsLSNuIlQei%2BQLTJ44GThHjDLkBis5%2FAow8vqHwLH4b5r6A7XJWJB4rBeliKGBRDLPpwBBZhy9p5OWyRPXhLr&X-Amz-Signature=8a2f680d265e59a3d7c2618cea8f132a7e552f0f5116036dea76fd0da8d583af&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677JKK4XV%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIQDzSe5JlWkOFOds%2BvdTcjdvb1%2BM4oe6vLYjGD9V0AnRegIgRAzGRIfLbQcpn3Yw9FIZ%2FhR8P5EiW9uAlWOqlvtE5B0q%2FwMIHxAAGgw2Mzc0MjMxODM4MDUiDLXrp%2BIQ0bqoe63IBCrcA2NGyYRmfMhuJfA2uymZ8EQXN1oK58dIIdVuqHRIO6vGngujQJYPzd0kKb6Lo8R0PeWXu5h1WTPdUmQ7JkUzQGVF6Ia73o8NKKw0Bu61XQ2SPcsP%2BdhrzQRadOq50EUNKzkMu8powfsIQE0skrJxZCTxahHWWE89SiJVGcGUXBKda0TDQE9Uak2xsgcihSy7xGkbRMssVHfDVNVDOhAaa%2F5IbVOI1%2Bh9O1NYWGeMgDI%2F8uixXHYhLtCuHnWPyRl4gM6ETHfWDuM7vK2iYOoIKaoBrqBR6RklOGLxgV46HxQ2i2CgPpV98nRoQVJeaPWY7kCNZ5GgDVyFlOA8ASuFk3QZoMCY4kMzytvOP7Bn4QYaBSDCTBdhvEg6fOlUOXvSCEd7UMaQr2zMpwdgV2QMpHYD070zYBzZooHfAiXpxUQQMNhx8%2FKYQUM3%2FJ9Kx2Xs7eqRovkNNF7DJpXNGa4bIOsLfqU3je47YfLH%2B6ovSWG5SB3fEWHVCPETAY0kQWG6d5ABCyxplhPrXwsonWwZWV97SN%2FfWuAnBK7cQcmdWXKNP%2FQLrCbFsZalb9kERVUH62ExcGghds3PEq9af0LibGZztt4VpyiRX9OoDGRqWp5rXp44d6PtdmKG1Kg8MPH2hL0GOqUBy%2BcBAr12oy1k518SdMz5QPNLCoz%2BNyOBJAjNakuML6qd3yzRhOeiuv7jRdpI%2FNrRPGWM8C9MlNMvEYPLzNU3Wj0SlaJtjswdPoDi0TspFMqI6ppvA2y68rsaiuoHXYnpkIRnoQkWsLSNuIlQei%2BQLTJ44GThHjDLkBis5%2FAow8vqHwLH4b5r6A7XJWJB4rBeliKGBRDLPpwBBZhy9p5OWyRPXhLr&X-Amz-Signature=588ce6b147750f69ce559a32951cccb87192b7e51f91ef4b6cf7a119250ee8da&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677JKK4XV%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIQDzSe5JlWkOFOds%2BvdTcjdvb1%2BM4oe6vLYjGD9V0AnRegIgRAzGRIfLbQcpn3Yw9FIZ%2FhR8P5EiW9uAlWOqlvtE5B0q%2FwMIHxAAGgw2Mzc0MjMxODM4MDUiDLXrp%2BIQ0bqoe63IBCrcA2NGyYRmfMhuJfA2uymZ8EQXN1oK58dIIdVuqHRIO6vGngujQJYPzd0kKb6Lo8R0PeWXu5h1WTPdUmQ7JkUzQGVF6Ia73o8NKKw0Bu61XQ2SPcsP%2BdhrzQRadOq50EUNKzkMu8powfsIQE0skrJxZCTxahHWWE89SiJVGcGUXBKda0TDQE9Uak2xsgcihSy7xGkbRMssVHfDVNVDOhAaa%2F5IbVOI1%2Bh9O1NYWGeMgDI%2F8uixXHYhLtCuHnWPyRl4gM6ETHfWDuM7vK2iYOoIKaoBrqBR6RklOGLxgV46HxQ2i2CgPpV98nRoQVJeaPWY7kCNZ5GgDVyFlOA8ASuFk3QZoMCY4kMzytvOP7Bn4QYaBSDCTBdhvEg6fOlUOXvSCEd7UMaQr2zMpwdgV2QMpHYD070zYBzZooHfAiXpxUQQMNhx8%2FKYQUM3%2FJ9Kx2Xs7eqRovkNNF7DJpXNGa4bIOsLfqU3je47YfLH%2B6ovSWG5SB3fEWHVCPETAY0kQWG6d5ABCyxplhPrXwsonWwZWV97SN%2FfWuAnBK7cQcmdWXKNP%2FQLrCbFsZalb9kERVUH62ExcGghds3PEq9af0LibGZztt4VpyiRX9OoDGRqWp5rXp44d6PtdmKG1Kg8MPH2hL0GOqUBy%2BcBAr12oy1k518SdMz5QPNLCoz%2BNyOBJAjNakuML6qd3yzRhOeiuv7jRdpI%2FNrRPGWM8C9MlNMvEYPLzNU3Wj0SlaJtjswdPoDi0TspFMqI6ppvA2y68rsaiuoHXYnpkIRnoQkWsLSNuIlQei%2BQLTJ44GThHjDLkBis5%2FAow8vqHwLH4b5r6A7XJWJB4rBeliKGBRDLPpwBBZhy9p5OWyRPXhLr&X-Amz-Signature=e59d72537246a7ffe1cd9c6983e103788213444f66c01d21c4794a4a59f0498b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677JKK4XV%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIQDzSe5JlWkOFOds%2BvdTcjdvb1%2BM4oe6vLYjGD9V0AnRegIgRAzGRIfLbQcpn3Yw9FIZ%2FhR8P5EiW9uAlWOqlvtE5B0q%2FwMIHxAAGgw2Mzc0MjMxODM4MDUiDLXrp%2BIQ0bqoe63IBCrcA2NGyYRmfMhuJfA2uymZ8EQXN1oK58dIIdVuqHRIO6vGngujQJYPzd0kKb6Lo8R0PeWXu5h1WTPdUmQ7JkUzQGVF6Ia73o8NKKw0Bu61XQ2SPcsP%2BdhrzQRadOq50EUNKzkMu8powfsIQE0skrJxZCTxahHWWE89SiJVGcGUXBKda0TDQE9Uak2xsgcihSy7xGkbRMssVHfDVNVDOhAaa%2F5IbVOI1%2Bh9O1NYWGeMgDI%2F8uixXHYhLtCuHnWPyRl4gM6ETHfWDuM7vK2iYOoIKaoBrqBR6RklOGLxgV46HxQ2i2CgPpV98nRoQVJeaPWY7kCNZ5GgDVyFlOA8ASuFk3QZoMCY4kMzytvOP7Bn4QYaBSDCTBdhvEg6fOlUOXvSCEd7UMaQr2zMpwdgV2QMpHYD070zYBzZooHfAiXpxUQQMNhx8%2FKYQUM3%2FJ9Kx2Xs7eqRovkNNF7DJpXNGa4bIOsLfqU3je47YfLH%2B6ovSWG5SB3fEWHVCPETAY0kQWG6d5ABCyxplhPrXwsonWwZWV97SN%2FfWuAnBK7cQcmdWXKNP%2FQLrCbFsZalb9kERVUH62ExcGghds3PEq9af0LibGZztt4VpyiRX9OoDGRqWp5rXp44d6PtdmKG1Kg8MPH2hL0GOqUBy%2BcBAr12oy1k518SdMz5QPNLCoz%2BNyOBJAjNakuML6qd3yzRhOeiuv7jRdpI%2FNrRPGWM8C9MlNMvEYPLzNU3Wj0SlaJtjswdPoDi0TspFMqI6ppvA2y68rsaiuoHXYnpkIRnoQkWsLSNuIlQei%2BQLTJ44GThHjDLkBis5%2FAow8vqHwLH4b5r6A7XJWJB4rBeliKGBRDLPpwBBZhy9p5OWyRPXhLr&X-Amz-Signature=4fa419f3dc254dbd9c7c5f4a8cc8c77ff5fa9646a855fad2196370565651aa05&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TR7UCLDF%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJIMEYCIQDU9QODHudD7P6V1iu86UVMraFAjOtbffl2ccd2Ij0%2BUwIhALuvlRt%2BPUh4t7RFOo9R8%2FP29rvzkeiiF0kXKQdChQmUKv8DCB8QABoMNjM3NDIzMTgzODA1IgzoqFTfxRLyeueh%2Ffkq3APLqPBBCKc44g5%2BrrA34Fd2Nup6yL8AbmfBBWcK8vuxTrkC46b9IQVp0qkZEBFuOOKVtTGf6Ov5ama%2BIyyDkPFsAr3jn78UPEPM9Q24Td1L6zf7eRjcMshjL3UwtcVkfY1z1gciYgtTn5n9QIZbojGSXkc9JR0%2BPyonjV3TYsGMERlX4nMhwNU5wug%2BAZPRHco1YYfbO6zMeCi%2BOTNslHQyjWKWcwEDcs0PuuCvG3Jzl3JuE9fhLASOujL%2BIBNEqg9yKZCFMju1KQdZntYIVwkc3WMiifLOnX6lcoLxxpHe%2FGGH2Fyt0S08ym9VRrrG%2BiwPi851uQYz2mDm3li%2BzKMYZ5Bd7dNHkcNBtpS5QqSydhz6q39b9zzvyZXqHR%2FEg1%2Fnr%2B0LZj%2FL%2FkGZbSMPlwRK4V5d6RR2a15cvkIJ%2FJThc4kZSrijwNhesv%2BgAM0JC4QubuWG6rM2wh0%2BNBgdk5A1gZnq0c33c7wo3YM%2BFD7HXVbEbVLRVzdxZiQBHOZtelKjStpXIyL4BIHhiUdQ778EmU%2B3MkO4xF411c%2B%2Bq8O7End%2BPTfNcGA5ab5gQPU%2FIsVmhi%2BewqPaL8Iv7ea8ib%2Bny3qawR0Pb5yxgeNP64YdRynm6xiU1j2aJL%2BxJTCp94S9BjqkAZIy8YPVdqQ1fk8sfCnQk3EblK8PHnGmbIbT84IvxRGZG3DLUCmRiI8qJzB%2BTK1eHj3UtSdNT0mqlhxuxLxK6Q2YZfUaMLruoo0H5pDKwCqYALNhh9YLGjqN5ihZBLLy%2BbUd5g6iaiYc5n3potRYcfZsLoc45EC%2FlC6awRSikiAb1NhTgq0iYSsEmDDUSk0SKszdkuJeq2V9inmU%2F3iTnONcQbTW&X-Amz-Signature=a908536ff03ec4f029d528227aaaa4d15b4f75508b0a7cddbcd4fc9cf5b53546&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TR7UCLDF%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJIMEYCIQDU9QODHudD7P6V1iu86UVMraFAjOtbffl2ccd2Ij0%2BUwIhALuvlRt%2BPUh4t7RFOo9R8%2FP29rvzkeiiF0kXKQdChQmUKv8DCB8QABoMNjM3NDIzMTgzODA1IgzoqFTfxRLyeueh%2Ffkq3APLqPBBCKc44g5%2BrrA34Fd2Nup6yL8AbmfBBWcK8vuxTrkC46b9IQVp0qkZEBFuOOKVtTGf6Ov5ama%2BIyyDkPFsAr3jn78UPEPM9Q24Td1L6zf7eRjcMshjL3UwtcVkfY1z1gciYgtTn5n9QIZbojGSXkc9JR0%2BPyonjV3TYsGMERlX4nMhwNU5wug%2BAZPRHco1YYfbO6zMeCi%2BOTNslHQyjWKWcwEDcs0PuuCvG3Jzl3JuE9fhLASOujL%2BIBNEqg9yKZCFMju1KQdZntYIVwkc3WMiifLOnX6lcoLxxpHe%2FGGH2Fyt0S08ym9VRrrG%2BiwPi851uQYz2mDm3li%2BzKMYZ5Bd7dNHkcNBtpS5QqSydhz6q39b9zzvyZXqHR%2FEg1%2Fnr%2B0LZj%2FL%2FkGZbSMPlwRK4V5d6RR2a15cvkIJ%2FJThc4kZSrijwNhesv%2BgAM0JC4QubuWG6rM2wh0%2BNBgdk5A1gZnq0c33c7wo3YM%2BFD7HXVbEbVLRVzdxZiQBHOZtelKjStpXIyL4BIHhiUdQ778EmU%2B3MkO4xF411c%2B%2Bq8O7End%2BPTfNcGA5ab5gQPU%2FIsVmhi%2BewqPaL8Iv7ea8ib%2Bny3qawR0Pb5yxgeNP64YdRynm6xiU1j2aJL%2BxJTCp94S9BjqkAZIy8YPVdqQ1fk8sfCnQk3EblK8PHnGmbIbT84IvxRGZG3DLUCmRiI8qJzB%2BTK1eHj3UtSdNT0mqlhxuxLxK6Q2YZfUaMLruoo0H5pDKwCqYALNhh9YLGjqN5ihZBLLy%2BbUd5g6iaiYc5n3potRYcfZsLoc45EC%2FlC6awRSikiAb1NhTgq0iYSsEmDDUSk0SKszdkuJeq2V9inmU%2F3iTnONcQbTW&X-Amz-Signature=8349d6d07405089fc7febd015cc99d32ae271b36793cf42302172a6367644a77&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TR7UCLDF%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJIMEYCIQDU9QODHudD7P6V1iu86UVMraFAjOtbffl2ccd2Ij0%2BUwIhALuvlRt%2BPUh4t7RFOo9R8%2FP29rvzkeiiF0kXKQdChQmUKv8DCB8QABoMNjM3NDIzMTgzODA1IgzoqFTfxRLyeueh%2Ffkq3APLqPBBCKc44g5%2BrrA34Fd2Nup6yL8AbmfBBWcK8vuxTrkC46b9IQVp0qkZEBFuOOKVtTGf6Ov5ama%2BIyyDkPFsAr3jn78UPEPM9Q24Td1L6zf7eRjcMshjL3UwtcVkfY1z1gciYgtTn5n9QIZbojGSXkc9JR0%2BPyonjV3TYsGMERlX4nMhwNU5wug%2BAZPRHco1YYfbO6zMeCi%2BOTNslHQyjWKWcwEDcs0PuuCvG3Jzl3JuE9fhLASOujL%2BIBNEqg9yKZCFMju1KQdZntYIVwkc3WMiifLOnX6lcoLxxpHe%2FGGH2Fyt0S08ym9VRrrG%2BiwPi851uQYz2mDm3li%2BzKMYZ5Bd7dNHkcNBtpS5QqSydhz6q39b9zzvyZXqHR%2FEg1%2Fnr%2B0LZj%2FL%2FkGZbSMPlwRK4V5d6RR2a15cvkIJ%2FJThc4kZSrijwNhesv%2BgAM0JC4QubuWG6rM2wh0%2BNBgdk5A1gZnq0c33c7wo3YM%2BFD7HXVbEbVLRVzdxZiQBHOZtelKjStpXIyL4BIHhiUdQ778EmU%2B3MkO4xF411c%2B%2Bq8O7End%2BPTfNcGA5ab5gQPU%2FIsVmhi%2BewqPaL8Iv7ea8ib%2Bny3qawR0Pb5yxgeNP64YdRynm6xiU1j2aJL%2BxJTCp94S9BjqkAZIy8YPVdqQ1fk8sfCnQk3EblK8PHnGmbIbT84IvxRGZG3DLUCmRiI8qJzB%2BTK1eHj3UtSdNT0mqlhxuxLxK6Q2YZfUaMLruoo0H5pDKwCqYALNhh9YLGjqN5ihZBLLy%2BbUd5g6iaiYc5n3potRYcfZsLoc45EC%2FlC6awRSikiAb1NhTgq0iYSsEmDDUSk0SKszdkuJeq2V9inmU%2F3iTnONcQbTW&X-Amz-Signature=f13c5f15d76c7a98214042d97eabb0197c32e320787ac1ad7ed47655f7e70a16&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TR7UCLDF%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJIMEYCIQDU9QODHudD7P6V1iu86UVMraFAjOtbffl2ccd2Ij0%2BUwIhALuvlRt%2BPUh4t7RFOo9R8%2FP29rvzkeiiF0kXKQdChQmUKv8DCB8QABoMNjM3NDIzMTgzODA1IgzoqFTfxRLyeueh%2Ffkq3APLqPBBCKc44g5%2BrrA34Fd2Nup6yL8AbmfBBWcK8vuxTrkC46b9IQVp0qkZEBFuOOKVtTGf6Ov5ama%2BIyyDkPFsAr3jn78UPEPM9Q24Td1L6zf7eRjcMshjL3UwtcVkfY1z1gciYgtTn5n9QIZbojGSXkc9JR0%2BPyonjV3TYsGMERlX4nMhwNU5wug%2BAZPRHco1YYfbO6zMeCi%2BOTNslHQyjWKWcwEDcs0PuuCvG3Jzl3JuE9fhLASOujL%2BIBNEqg9yKZCFMju1KQdZntYIVwkc3WMiifLOnX6lcoLxxpHe%2FGGH2Fyt0S08ym9VRrrG%2BiwPi851uQYz2mDm3li%2BzKMYZ5Bd7dNHkcNBtpS5QqSydhz6q39b9zzvyZXqHR%2FEg1%2Fnr%2B0LZj%2FL%2FkGZbSMPlwRK4V5d6RR2a15cvkIJ%2FJThc4kZSrijwNhesv%2BgAM0JC4QubuWG6rM2wh0%2BNBgdk5A1gZnq0c33c7wo3YM%2BFD7HXVbEbVLRVzdxZiQBHOZtelKjStpXIyL4BIHhiUdQ778EmU%2B3MkO4xF411c%2B%2Bq8O7End%2BPTfNcGA5ab5gQPU%2FIsVmhi%2BewqPaL8Iv7ea8ib%2Bny3qawR0Pb5yxgeNP64YdRynm6xiU1j2aJL%2BxJTCp94S9BjqkAZIy8YPVdqQ1fk8sfCnQk3EblK8PHnGmbIbT84IvxRGZG3DLUCmRiI8qJzB%2BTK1eHj3UtSdNT0mqlhxuxLxK6Q2YZfUaMLruoo0H5pDKwCqYALNhh9YLGjqN5ihZBLLy%2BbUd5g6iaiYc5n3potRYcfZsLoc45EC%2FlC6awRSikiAb1NhTgq0iYSsEmDDUSk0SKszdkuJeq2V9inmU%2F3iTnONcQbTW&X-Amz-Signature=37e423b4ee6423bdb3fb9eb720c113da31ce122c3dbfb8e3f29de4d68c68e4d0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TR7UCLDF%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJIMEYCIQDU9QODHudD7P6V1iu86UVMraFAjOtbffl2ccd2Ij0%2BUwIhALuvlRt%2BPUh4t7RFOo9R8%2FP29rvzkeiiF0kXKQdChQmUKv8DCB8QABoMNjM3NDIzMTgzODA1IgzoqFTfxRLyeueh%2Ffkq3APLqPBBCKc44g5%2BrrA34Fd2Nup6yL8AbmfBBWcK8vuxTrkC46b9IQVp0qkZEBFuOOKVtTGf6Ov5ama%2BIyyDkPFsAr3jn78UPEPM9Q24Td1L6zf7eRjcMshjL3UwtcVkfY1z1gciYgtTn5n9QIZbojGSXkc9JR0%2BPyonjV3TYsGMERlX4nMhwNU5wug%2BAZPRHco1YYfbO6zMeCi%2BOTNslHQyjWKWcwEDcs0PuuCvG3Jzl3JuE9fhLASOujL%2BIBNEqg9yKZCFMju1KQdZntYIVwkc3WMiifLOnX6lcoLxxpHe%2FGGH2Fyt0S08ym9VRrrG%2BiwPi851uQYz2mDm3li%2BzKMYZ5Bd7dNHkcNBtpS5QqSydhz6q39b9zzvyZXqHR%2FEg1%2Fnr%2B0LZj%2FL%2FkGZbSMPlwRK4V5d6RR2a15cvkIJ%2FJThc4kZSrijwNhesv%2BgAM0JC4QubuWG6rM2wh0%2BNBgdk5A1gZnq0c33c7wo3YM%2BFD7HXVbEbVLRVzdxZiQBHOZtelKjStpXIyL4BIHhiUdQ778EmU%2B3MkO4xF411c%2B%2Bq8O7End%2BPTfNcGA5ab5gQPU%2FIsVmhi%2BewqPaL8Iv7ea8ib%2Bny3qawR0Pb5yxgeNP64YdRynm6xiU1j2aJL%2BxJTCp94S9BjqkAZIy8YPVdqQ1fk8sfCnQk3EblK8PHnGmbIbT84IvxRGZG3DLUCmRiI8qJzB%2BTK1eHj3UtSdNT0mqlhxuxLxK6Q2YZfUaMLruoo0H5pDKwCqYALNhh9YLGjqN5ihZBLLy%2BbUd5g6iaiYc5n3potRYcfZsLoc45EC%2FlC6awRSikiAb1NhTgq0iYSsEmDDUSk0SKszdkuJeq2V9inmU%2F3iTnONcQbTW&X-Amz-Signature=63c5ac08e3d923d387801b46f5c66b6ac1fc4c1b27fd58302d594fffd4d543ac&X-Amz-SignedHeaders=host&x-id=GetObject)
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


