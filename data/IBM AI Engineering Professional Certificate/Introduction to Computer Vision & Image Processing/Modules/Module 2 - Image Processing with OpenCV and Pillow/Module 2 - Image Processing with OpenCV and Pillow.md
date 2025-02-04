

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MKKEHME%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062049Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIAMo0lWF5yrg2OxaW6AY6zHr4%2BvzrD0fMH2swJ00NvG1AiEAgYnJcdpgrp4mDbGsxVVuYYdsCDtFNJDAWwbR7n09zdcq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDDolzxiFvr2IfL9rgSrcA2TBDFqDk0E%2FoKVnMNzQijsDfw1c3hVL1BeKgvcBcn4Q0itGrH7VuJmOF%2F5JZdlyNJMBQYrGSDsE9qIsNjYkPseqQwJ9X81d6lirRMG4BXteqoU5HxZRqt0wOr09zFP334M08ja%2B15rGMcMrQGw4I74hQJoHJmm4Nz39bqTjFWeG%2FXvHfAqLpumgl3Vrg2z%2BLpJRHDAbjtKyhhqpcTvFPTbbY81DrN1%2BTwWBBRAuWEtOiMHRV2yKEvxSlib8HedIt0vkhUqMX2lysfXj9Fx3GJntS2RN%2BkH4vfaDLj1CkZlnKii2edPK0B%2FnqOkRL%2BnYfbgiW%2BvQ3PcT1P%2BHouMBhcPfHH3smdYGt4w8BDhGEA4sIrZFPb9ZLOSdgJ9%2FbiF85KrPnpibWCovcszpEAeGbqVRIQ2u0jYgjAZvbr6kA6vL1qbg2QnJTcwlFNz8fP7uaRCgnVCJ6vSYLP4cXPwVXY3gxh6n6JGueQov%2FFErf1ZhMBFOskP3oD0EBSUVJ4uETVZ0%2BXMhRUqNCILeSk2vrdqYaBCNkNzyX0upQpP6Ew77BEz%2B9xFizKfl%2BklyBinDja%2B37i9O4tPA4NiW41c6AKpcNGjs2ZZJKODkb%2B3I0ODLQjwuy%2F3doN2y4FBUMP6%2Bhr0GOqUBi%2BSYBGSJk6neiHw9TZRtghcpjtLg80GJKV4wX5uZi0EtQf3%2F%2FUiQ38vKasX39br%2FaJSUUQCW9AtiJ6EQU74DR%2FZJgAtXltq2l2UmmFfTWIoav5AjjxmvHKtRTzqLeMyC8y8Q5CsAYMba8H24vQTKQ8UzcYcuqHlPtu92QFN%2F%2FnV%2B4pYdvDCkpt%2FHQwCgFgi%2FDaTLDMYixbWUsY6okTI1WXAiyRdX&X-Amz-Signature=4dff80426b9ffe40010ccd3c0d9ec93629222084f89e95fb49fe2667d745d78d&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663VSK6HIR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062050Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQD3KTdTWuSeAB%2BREhQPnHsk1RcJq7n6TrlvHmJ2C45DEwIhAO2e48oHWNGlu11klDYZJSmZ7jxiCpIA3DPiOzLZ%2B9yBKv8DCCYQABoMNjM3NDIzMTgzODA1IgwhK3NRCSOEQ0DXqXwq3APDltsRpioV1ONwI3Pz1NH1KsjhfxjyLUoVv2veM6CAvwjqOzI6lCD%2FcGW%2BeULWiXOWD3sc8qKfgzQC%2Bdnot%2FxKE8y5v87Mu1nh%2BA%2BYJpWqCC2jj0CqD3IjeYopfpAa5CiMMsklwmI%2FroF%2Ffp3DFTZkt5mNj21xXqtDatJMQShhA1IGbG5a1kj1X8Vf8d6EmSXBDk0Dpkr%2F2BBI0Ie%2BO3y4YoYwjHNtVuCD%2BcITCFJm4%2B6LwLYsjv%2Fs7tqXX80fe%2B24pcfTAg6qxrODKncTJuZ6CvTvo4lSQPyVqsd%2BEJskbB5jZenmawO%2Bbx6cDClbFfIWTA9Ymf9SUyZV3Oxeepldx4AXTjJQrjXUqNWe0lz3j3oPbBYFkjtyC2W9pGi%2BP1EPhLtCWBftasssML3Lu27hL%2BE6h5jNTe6xq3oSyyn30oosrS4o3PVkrsZJuVhmxYzMgChM%2FvGtd6icyRtDPfcjIA9bZL%2FY57sM%2BjWiurcGX8vW1AEOk5v2TbYd0zdCTQ5BtD2CSMWlnaTBK%2FP1v%2Bms%2BaM3u748rlKYCVahjXp4NTRIreRkzNzGxT0XZ%2F9NH3qcKKMeHepgy2wGNeGoEOPI3%2BFS9yhhrrLEPvS3od37tR6Bns4hRKjG%2BicyITCzvoa9BjqkAQETYr5VPb%2Be%2FehJSlLK3PfIE5qQy4pucIwrLkgkHCSxdgL2O17X9JEnLt3Vu99XHYsDEivkapeIxO4wkDUMRkYJBKMV2IvLdpnegLn%2BJ2lqy2GbL7Rd0kzc8WaapYI1RKqxwRNrenHKDFgBPg0lhs11qzfcTU5uBl%2Bzcsc%2FUWYQ84%2F3If4FNIx7Vh8qwEM5SyPu%2BdwFPpU2jAsbKpQGc2KXrYnd&X-Amz-Signature=8740d66f7cadc199611d195ca1920950777d4fdd718a81d3d101a0c4e0cf4211&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663VSK6HIR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062050Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQD3KTdTWuSeAB%2BREhQPnHsk1RcJq7n6TrlvHmJ2C45DEwIhAO2e48oHWNGlu11klDYZJSmZ7jxiCpIA3DPiOzLZ%2B9yBKv8DCCYQABoMNjM3NDIzMTgzODA1IgwhK3NRCSOEQ0DXqXwq3APDltsRpioV1ONwI3Pz1NH1KsjhfxjyLUoVv2veM6CAvwjqOzI6lCD%2FcGW%2BeULWiXOWD3sc8qKfgzQC%2Bdnot%2FxKE8y5v87Mu1nh%2BA%2BYJpWqCC2jj0CqD3IjeYopfpAa5CiMMsklwmI%2FroF%2Ffp3DFTZkt5mNj21xXqtDatJMQShhA1IGbG5a1kj1X8Vf8d6EmSXBDk0Dpkr%2F2BBI0Ie%2BO3y4YoYwjHNtVuCD%2BcITCFJm4%2B6LwLYsjv%2Fs7tqXX80fe%2B24pcfTAg6qxrODKncTJuZ6CvTvo4lSQPyVqsd%2BEJskbB5jZenmawO%2Bbx6cDClbFfIWTA9Ymf9SUyZV3Oxeepldx4AXTjJQrjXUqNWe0lz3j3oPbBYFkjtyC2W9pGi%2BP1EPhLtCWBftasssML3Lu27hL%2BE6h5jNTe6xq3oSyyn30oosrS4o3PVkrsZJuVhmxYzMgChM%2FvGtd6icyRtDPfcjIA9bZL%2FY57sM%2BjWiurcGX8vW1AEOk5v2TbYd0zdCTQ5BtD2CSMWlnaTBK%2FP1v%2Bms%2BaM3u748rlKYCVahjXp4NTRIreRkzNzGxT0XZ%2F9NH3qcKKMeHepgy2wGNeGoEOPI3%2BFS9yhhrrLEPvS3od37tR6Bns4hRKjG%2BicyITCzvoa9BjqkAQETYr5VPb%2Be%2FehJSlLK3PfIE5qQy4pucIwrLkgkHCSxdgL2O17X9JEnLt3Vu99XHYsDEivkapeIxO4wkDUMRkYJBKMV2IvLdpnegLn%2BJ2lqy2GbL7Rd0kzc8WaapYI1RKqxwRNrenHKDFgBPg0lhs11qzfcTU5uBl%2Bzcsc%2FUWYQ84%2F3If4FNIx7Vh8qwEM5SyPu%2BdwFPpU2jAsbKpQGc2KXrYnd&X-Amz-Signature=65e413e22724fb36e48633475c13083ef5dd48d3f04b50bbda47ba357b420d81&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663VSK6HIR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062050Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQD3KTdTWuSeAB%2BREhQPnHsk1RcJq7n6TrlvHmJ2C45DEwIhAO2e48oHWNGlu11klDYZJSmZ7jxiCpIA3DPiOzLZ%2B9yBKv8DCCYQABoMNjM3NDIzMTgzODA1IgwhK3NRCSOEQ0DXqXwq3APDltsRpioV1ONwI3Pz1NH1KsjhfxjyLUoVv2veM6CAvwjqOzI6lCD%2FcGW%2BeULWiXOWD3sc8qKfgzQC%2Bdnot%2FxKE8y5v87Mu1nh%2BA%2BYJpWqCC2jj0CqD3IjeYopfpAa5CiMMsklwmI%2FroF%2Ffp3DFTZkt5mNj21xXqtDatJMQShhA1IGbG5a1kj1X8Vf8d6EmSXBDk0Dpkr%2F2BBI0Ie%2BO3y4YoYwjHNtVuCD%2BcITCFJm4%2B6LwLYsjv%2Fs7tqXX80fe%2B24pcfTAg6qxrODKncTJuZ6CvTvo4lSQPyVqsd%2BEJskbB5jZenmawO%2Bbx6cDClbFfIWTA9Ymf9SUyZV3Oxeepldx4AXTjJQrjXUqNWe0lz3j3oPbBYFkjtyC2W9pGi%2BP1EPhLtCWBftasssML3Lu27hL%2BE6h5jNTe6xq3oSyyn30oosrS4o3PVkrsZJuVhmxYzMgChM%2FvGtd6icyRtDPfcjIA9bZL%2FY57sM%2BjWiurcGX8vW1AEOk5v2TbYd0zdCTQ5BtD2CSMWlnaTBK%2FP1v%2Bms%2BaM3u748rlKYCVahjXp4NTRIreRkzNzGxT0XZ%2F9NH3qcKKMeHepgy2wGNeGoEOPI3%2BFS9yhhrrLEPvS3od37tR6Bns4hRKjG%2BicyITCzvoa9BjqkAQETYr5VPb%2Be%2FehJSlLK3PfIE5qQy4pucIwrLkgkHCSxdgL2O17X9JEnLt3Vu99XHYsDEivkapeIxO4wkDUMRkYJBKMV2IvLdpnegLn%2BJ2lqy2GbL7Rd0kzc8WaapYI1RKqxwRNrenHKDFgBPg0lhs11qzfcTU5uBl%2Bzcsc%2FUWYQ84%2F3If4FNIx7Vh8qwEM5SyPu%2BdwFPpU2jAsbKpQGc2KXrYnd&X-Amz-Signature=27494e4134f4ba4da247243e34037cb938479b655f08494f48990565e738d835&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663VSK6HIR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062050Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQD3KTdTWuSeAB%2BREhQPnHsk1RcJq7n6TrlvHmJ2C45DEwIhAO2e48oHWNGlu11klDYZJSmZ7jxiCpIA3DPiOzLZ%2B9yBKv8DCCYQABoMNjM3NDIzMTgzODA1IgwhK3NRCSOEQ0DXqXwq3APDltsRpioV1ONwI3Pz1NH1KsjhfxjyLUoVv2veM6CAvwjqOzI6lCD%2FcGW%2BeULWiXOWD3sc8qKfgzQC%2Bdnot%2FxKE8y5v87Mu1nh%2BA%2BYJpWqCC2jj0CqD3IjeYopfpAa5CiMMsklwmI%2FroF%2Ffp3DFTZkt5mNj21xXqtDatJMQShhA1IGbG5a1kj1X8Vf8d6EmSXBDk0Dpkr%2F2BBI0Ie%2BO3y4YoYwjHNtVuCD%2BcITCFJm4%2B6LwLYsjv%2Fs7tqXX80fe%2B24pcfTAg6qxrODKncTJuZ6CvTvo4lSQPyVqsd%2BEJskbB5jZenmawO%2Bbx6cDClbFfIWTA9Ymf9SUyZV3Oxeepldx4AXTjJQrjXUqNWe0lz3j3oPbBYFkjtyC2W9pGi%2BP1EPhLtCWBftasssML3Lu27hL%2BE6h5jNTe6xq3oSyyn30oosrS4o3PVkrsZJuVhmxYzMgChM%2FvGtd6icyRtDPfcjIA9bZL%2FY57sM%2BjWiurcGX8vW1AEOk5v2TbYd0zdCTQ5BtD2CSMWlnaTBK%2FP1v%2Bms%2BaM3u748rlKYCVahjXp4NTRIreRkzNzGxT0XZ%2F9NH3qcKKMeHepgy2wGNeGoEOPI3%2BFS9yhhrrLEPvS3od37tR6Bns4hRKjG%2BicyITCzvoa9BjqkAQETYr5VPb%2Be%2FehJSlLK3PfIE5qQy4pucIwrLkgkHCSxdgL2O17X9JEnLt3Vu99XHYsDEivkapeIxO4wkDUMRkYJBKMV2IvLdpnegLn%2BJ2lqy2GbL7Rd0kzc8WaapYI1RKqxwRNrenHKDFgBPg0lhs11qzfcTU5uBl%2Bzcsc%2FUWYQ84%2F3If4FNIx7Vh8qwEM5SyPu%2BdwFPpU2jAsbKpQGc2KXrYnd&X-Amz-Signature=895a57416e996dcc445b18002cde3b6e219bca3fb29ba526f517fb897a6e392e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663VSK6HIR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062050Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQD3KTdTWuSeAB%2BREhQPnHsk1RcJq7n6TrlvHmJ2C45DEwIhAO2e48oHWNGlu11klDYZJSmZ7jxiCpIA3DPiOzLZ%2B9yBKv8DCCYQABoMNjM3NDIzMTgzODA1IgwhK3NRCSOEQ0DXqXwq3APDltsRpioV1ONwI3Pz1NH1KsjhfxjyLUoVv2veM6CAvwjqOzI6lCD%2FcGW%2BeULWiXOWD3sc8qKfgzQC%2Bdnot%2FxKE8y5v87Mu1nh%2BA%2BYJpWqCC2jj0CqD3IjeYopfpAa5CiMMsklwmI%2FroF%2Ffp3DFTZkt5mNj21xXqtDatJMQShhA1IGbG5a1kj1X8Vf8d6EmSXBDk0Dpkr%2F2BBI0Ie%2BO3y4YoYwjHNtVuCD%2BcITCFJm4%2B6LwLYsjv%2Fs7tqXX80fe%2B24pcfTAg6qxrODKncTJuZ6CvTvo4lSQPyVqsd%2BEJskbB5jZenmawO%2Bbx6cDClbFfIWTA9Ymf9SUyZV3Oxeepldx4AXTjJQrjXUqNWe0lz3j3oPbBYFkjtyC2W9pGi%2BP1EPhLtCWBftasssML3Lu27hL%2BE6h5jNTe6xq3oSyyn30oosrS4o3PVkrsZJuVhmxYzMgChM%2FvGtd6icyRtDPfcjIA9bZL%2FY57sM%2BjWiurcGX8vW1AEOk5v2TbYd0zdCTQ5BtD2CSMWlnaTBK%2FP1v%2Bms%2BaM3u748rlKYCVahjXp4NTRIreRkzNzGxT0XZ%2F9NH3qcKKMeHepgy2wGNeGoEOPI3%2BFS9yhhrrLEPvS3od37tR6Bns4hRKjG%2BicyITCzvoa9BjqkAQETYr5VPb%2Be%2FehJSlLK3PfIE5qQy4pucIwrLkgkHCSxdgL2O17X9JEnLt3Vu99XHYsDEivkapeIxO4wkDUMRkYJBKMV2IvLdpnegLn%2BJ2lqy2GbL7Rd0kzc8WaapYI1RKqxwRNrenHKDFgBPg0lhs11qzfcTU5uBl%2Bzcsc%2FUWYQ84%2F3If4FNIx7Vh8qwEM5SyPu%2BdwFPpU2jAsbKpQGc2KXrYnd&X-Amz-Signature=57fc16eae1c18d9a3f069409bb91dca0325af87499212a68f90d03f4bfcbf430&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MKKEHME%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062049Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIAMo0lWF5yrg2OxaW6AY6zHr4%2BvzrD0fMH2swJ00NvG1AiEAgYnJcdpgrp4mDbGsxVVuYYdsCDtFNJDAWwbR7n09zdcq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDDolzxiFvr2IfL9rgSrcA2TBDFqDk0E%2FoKVnMNzQijsDfw1c3hVL1BeKgvcBcn4Q0itGrH7VuJmOF%2F5JZdlyNJMBQYrGSDsE9qIsNjYkPseqQwJ9X81d6lirRMG4BXteqoU5HxZRqt0wOr09zFP334M08ja%2B15rGMcMrQGw4I74hQJoHJmm4Nz39bqTjFWeG%2FXvHfAqLpumgl3Vrg2z%2BLpJRHDAbjtKyhhqpcTvFPTbbY81DrN1%2BTwWBBRAuWEtOiMHRV2yKEvxSlib8HedIt0vkhUqMX2lysfXj9Fx3GJntS2RN%2BkH4vfaDLj1CkZlnKii2edPK0B%2FnqOkRL%2BnYfbgiW%2BvQ3PcT1P%2BHouMBhcPfHH3smdYGt4w8BDhGEA4sIrZFPb9ZLOSdgJ9%2FbiF85KrPnpibWCovcszpEAeGbqVRIQ2u0jYgjAZvbr6kA6vL1qbg2QnJTcwlFNz8fP7uaRCgnVCJ6vSYLP4cXPwVXY3gxh6n6JGueQov%2FFErf1ZhMBFOskP3oD0EBSUVJ4uETVZ0%2BXMhRUqNCILeSk2vrdqYaBCNkNzyX0upQpP6Ew77BEz%2B9xFizKfl%2BklyBinDja%2B37i9O4tPA4NiW41c6AKpcNGjs2ZZJKODkb%2B3I0ODLQjwuy%2F3doN2y4FBUMP6%2Bhr0GOqUBi%2BSYBGSJk6neiHw9TZRtghcpjtLg80GJKV4wX5uZi0EtQf3%2F%2FUiQ38vKasX39br%2FaJSUUQCW9AtiJ6EQU74DR%2FZJgAtXltq2l2UmmFfTWIoav5AjjxmvHKtRTzqLeMyC8y8Q5CsAYMba8H24vQTKQ8UzcYcuqHlPtu92QFN%2F%2FnV%2B4pYdvDCkpt%2FHQwCgFgi%2FDaTLDMYixbWUsY6okTI1WXAiyRdX&X-Amz-Signature=d6acebaf2a7e0dd0e5a0d5da97519f2010d1336d1acc5162b23b42f7295e3989&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MKKEHME%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062049Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIAMo0lWF5yrg2OxaW6AY6zHr4%2BvzrD0fMH2swJ00NvG1AiEAgYnJcdpgrp4mDbGsxVVuYYdsCDtFNJDAWwbR7n09zdcq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDDolzxiFvr2IfL9rgSrcA2TBDFqDk0E%2FoKVnMNzQijsDfw1c3hVL1BeKgvcBcn4Q0itGrH7VuJmOF%2F5JZdlyNJMBQYrGSDsE9qIsNjYkPseqQwJ9X81d6lirRMG4BXteqoU5HxZRqt0wOr09zFP334M08ja%2B15rGMcMrQGw4I74hQJoHJmm4Nz39bqTjFWeG%2FXvHfAqLpumgl3Vrg2z%2BLpJRHDAbjtKyhhqpcTvFPTbbY81DrN1%2BTwWBBRAuWEtOiMHRV2yKEvxSlib8HedIt0vkhUqMX2lysfXj9Fx3GJntS2RN%2BkH4vfaDLj1CkZlnKii2edPK0B%2FnqOkRL%2BnYfbgiW%2BvQ3PcT1P%2BHouMBhcPfHH3smdYGt4w8BDhGEA4sIrZFPb9ZLOSdgJ9%2FbiF85KrPnpibWCovcszpEAeGbqVRIQ2u0jYgjAZvbr6kA6vL1qbg2QnJTcwlFNz8fP7uaRCgnVCJ6vSYLP4cXPwVXY3gxh6n6JGueQov%2FFErf1ZhMBFOskP3oD0EBSUVJ4uETVZ0%2BXMhRUqNCILeSk2vrdqYaBCNkNzyX0upQpP6Ew77BEz%2B9xFizKfl%2BklyBinDja%2B37i9O4tPA4NiW41c6AKpcNGjs2ZZJKODkb%2B3I0ODLQjwuy%2F3doN2y4FBUMP6%2Bhr0GOqUBi%2BSYBGSJk6neiHw9TZRtghcpjtLg80GJKV4wX5uZi0EtQf3%2F%2FUiQ38vKasX39br%2FaJSUUQCW9AtiJ6EQU74DR%2FZJgAtXltq2l2UmmFfTWIoav5AjjxmvHKtRTzqLeMyC8y8Q5CsAYMba8H24vQTKQ8UzcYcuqHlPtu92QFN%2F%2FnV%2B4pYdvDCkpt%2FHQwCgFgi%2FDaTLDMYixbWUsY6okTI1WXAiyRdX&X-Amz-Signature=6388fcaf7e4b6c1dbd051f6f19ed06b5a378f3532063ca8f519d75e0ca6e703e&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MKKEHME%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062049Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIAMo0lWF5yrg2OxaW6AY6zHr4%2BvzrD0fMH2swJ00NvG1AiEAgYnJcdpgrp4mDbGsxVVuYYdsCDtFNJDAWwbR7n09zdcq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDDolzxiFvr2IfL9rgSrcA2TBDFqDk0E%2FoKVnMNzQijsDfw1c3hVL1BeKgvcBcn4Q0itGrH7VuJmOF%2F5JZdlyNJMBQYrGSDsE9qIsNjYkPseqQwJ9X81d6lirRMG4BXteqoU5HxZRqt0wOr09zFP334M08ja%2B15rGMcMrQGw4I74hQJoHJmm4Nz39bqTjFWeG%2FXvHfAqLpumgl3Vrg2z%2BLpJRHDAbjtKyhhqpcTvFPTbbY81DrN1%2BTwWBBRAuWEtOiMHRV2yKEvxSlib8HedIt0vkhUqMX2lysfXj9Fx3GJntS2RN%2BkH4vfaDLj1CkZlnKii2edPK0B%2FnqOkRL%2BnYfbgiW%2BvQ3PcT1P%2BHouMBhcPfHH3smdYGt4w8BDhGEA4sIrZFPb9ZLOSdgJ9%2FbiF85KrPnpibWCovcszpEAeGbqVRIQ2u0jYgjAZvbr6kA6vL1qbg2QnJTcwlFNz8fP7uaRCgnVCJ6vSYLP4cXPwVXY3gxh6n6JGueQov%2FFErf1ZhMBFOskP3oD0EBSUVJ4uETVZ0%2BXMhRUqNCILeSk2vrdqYaBCNkNzyX0upQpP6Ew77BEz%2B9xFizKfl%2BklyBinDja%2B37i9O4tPA4NiW41c6AKpcNGjs2ZZJKODkb%2B3I0ODLQjwuy%2F3doN2y4FBUMP6%2Bhr0GOqUBi%2BSYBGSJk6neiHw9TZRtghcpjtLg80GJKV4wX5uZi0EtQf3%2F%2FUiQ38vKasX39br%2FaJSUUQCW9AtiJ6EQU74DR%2FZJgAtXltq2l2UmmFfTWIoav5AjjxmvHKtRTzqLeMyC8y8Q5CsAYMba8H24vQTKQ8UzcYcuqHlPtu92QFN%2F%2FnV%2B4pYdvDCkpt%2FHQwCgFgi%2FDaTLDMYixbWUsY6okTI1WXAiyRdX&X-Amz-Signature=b36199ee0f87e7d31aff715494dca376356cdfc0cd4c5f63026981aa469f5123&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MKKEHME%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062049Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIAMo0lWF5yrg2OxaW6AY6zHr4%2BvzrD0fMH2swJ00NvG1AiEAgYnJcdpgrp4mDbGsxVVuYYdsCDtFNJDAWwbR7n09zdcq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDDolzxiFvr2IfL9rgSrcA2TBDFqDk0E%2FoKVnMNzQijsDfw1c3hVL1BeKgvcBcn4Q0itGrH7VuJmOF%2F5JZdlyNJMBQYrGSDsE9qIsNjYkPseqQwJ9X81d6lirRMG4BXteqoU5HxZRqt0wOr09zFP334M08ja%2B15rGMcMrQGw4I74hQJoHJmm4Nz39bqTjFWeG%2FXvHfAqLpumgl3Vrg2z%2BLpJRHDAbjtKyhhqpcTvFPTbbY81DrN1%2BTwWBBRAuWEtOiMHRV2yKEvxSlib8HedIt0vkhUqMX2lysfXj9Fx3GJntS2RN%2BkH4vfaDLj1CkZlnKii2edPK0B%2FnqOkRL%2BnYfbgiW%2BvQ3PcT1P%2BHouMBhcPfHH3smdYGt4w8BDhGEA4sIrZFPb9ZLOSdgJ9%2FbiF85KrPnpibWCovcszpEAeGbqVRIQ2u0jYgjAZvbr6kA6vL1qbg2QnJTcwlFNz8fP7uaRCgnVCJ6vSYLP4cXPwVXY3gxh6n6JGueQov%2FFErf1ZhMBFOskP3oD0EBSUVJ4uETVZ0%2BXMhRUqNCILeSk2vrdqYaBCNkNzyX0upQpP6Ew77BEz%2B9xFizKfl%2BklyBinDja%2B37i9O4tPA4NiW41c6AKpcNGjs2ZZJKODkb%2B3I0ODLQjwuy%2F3doN2y4FBUMP6%2Bhr0GOqUBi%2BSYBGSJk6neiHw9TZRtghcpjtLg80GJKV4wX5uZi0EtQf3%2F%2FUiQ38vKasX39br%2FaJSUUQCW9AtiJ6EQU74DR%2FZJgAtXltq2l2UmmFfTWIoav5AjjxmvHKtRTzqLeMyC8y8Q5CsAYMba8H24vQTKQ8UzcYcuqHlPtu92QFN%2F%2FnV%2B4pYdvDCkpt%2FHQwCgFgi%2FDaTLDMYixbWUsY6okTI1WXAiyRdX&X-Amz-Signature=3c9bb13794c6427ee084160ffbe8afcae4956f532521aa7435c9039534506afa&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MKKEHME%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062049Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIAMo0lWF5yrg2OxaW6AY6zHr4%2BvzrD0fMH2swJ00NvG1AiEAgYnJcdpgrp4mDbGsxVVuYYdsCDtFNJDAWwbR7n09zdcq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDDolzxiFvr2IfL9rgSrcA2TBDFqDk0E%2FoKVnMNzQijsDfw1c3hVL1BeKgvcBcn4Q0itGrH7VuJmOF%2F5JZdlyNJMBQYrGSDsE9qIsNjYkPseqQwJ9X81d6lirRMG4BXteqoU5HxZRqt0wOr09zFP334M08ja%2B15rGMcMrQGw4I74hQJoHJmm4Nz39bqTjFWeG%2FXvHfAqLpumgl3Vrg2z%2BLpJRHDAbjtKyhhqpcTvFPTbbY81DrN1%2BTwWBBRAuWEtOiMHRV2yKEvxSlib8HedIt0vkhUqMX2lysfXj9Fx3GJntS2RN%2BkH4vfaDLj1CkZlnKii2edPK0B%2FnqOkRL%2BnYfbgiW%2BvQ3PcT1P%2BHouMBhcPfHH3smdYGt4w8BDhGEA4sIrZFPb9ZLOSdgJ9%2FbiF85KrPnpibWCovcszpEAeGbqVRIQ2u0jYgjAZvbr6kA6vL1qbg2QnJTcwlFNz8fP7uaRCgnVCJ6vSYLP4cXPwVXY3gxh6n6JGueQov%2FFErf1ZhMBFOskP3oD0EBSUVJ4uETVZ0%2BXMhRUqNCILeSk2vrdqYaBCNkNzyX0upQpP6Ew77BEz%2B9xFizKfl%2BklyBinDja%2B37i9O4tPA4NiW41c6AKpcNGjs2ZZJKODkb%2B3I0ODLQjwuy%2F3doN2y4FBUMP6%2Bhr0GOqUBi%2BSYBGSJk6neiHw9TZRtghcpjtLg80GJKV4wX5uZi0EtQf3%2F%2FUiQ38vKasX39br%2FaJSUUQCW9AtiJ6EQU74DR%2FZJgAtXltq2l2UmmFfTWIoav5AjjxmvHKtRTzqLeMyC8y8Q5CsAYMba8H24vQTKQ8UzcYcuqHlPtu92QFN%2F%2FnV%2B4pYdvDCkpt%2FHQwCgFgi%2FDaTLDMYixbWUsY6okTI1WXAiyRdX&X-Amz-Signature=731e31a2211323401e9ba7524a9fcdac9d868caf7ac284607554fabebbb303db&X-Amz-SignedHeaders=host&x-id=GetObject)
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


