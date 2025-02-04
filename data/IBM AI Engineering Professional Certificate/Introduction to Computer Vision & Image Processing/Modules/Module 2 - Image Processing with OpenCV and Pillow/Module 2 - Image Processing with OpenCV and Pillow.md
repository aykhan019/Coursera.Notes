

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y322KDY7%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCIQDXlCLACCHagyPafEmcGPJEg396iUQTPgene5rKvpp71wIgJy7zXu2PAVNUPpM34Vf%2BpYrmY%2BiLfrvmgO82z9ZMnk4q%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDNaqRsSHH%2BhnMbrcRyrcAwfgFd%2FJLriAFzLjTHK2eY9a2gotJZYbGUt3Vr3QXlcGRWQX2CqHGGBFt27FO2UsviBj0%2F5bbQJM1o0fcAZogxJqtgHbdbDSLAbs%2Fx31HpfUEQ0EmCJrWEC2Af5Qf0OMPIEsnOoGvYDNQRNJzHs0Uh67jyAqDxZe9V2X8mHPFWoWxGKol7aKNWPGTZZGwwkMH4f9IhBgxnAJ0dCVSpwMwFV5cfLqtp4Pbwgc%2BUa%2BsSoxUDrm5u%2BO0jC46isDTXkcMazPaGDEwNPaMcbdeqLfbLWKwuxC185WHrByaj4r7c9Rg96EBe6xzYywa1yo9fYRtt9JSNuhBA7xgXI4r%2F9Aejw2DP%2FQhTnA2pMB%2Fut%2FeNfCKNuTpRQu9T1UaKJ2VJKVRu19kAyd%2B3DaZUnjgDJxKzWTYcsVRh4GLnKL5rvc2XCLzQq%2FN1vccmAzRR4G9H8%2FdP1lp9Yv48Uu4l2P4ib95uKZLHDKLFmbyeF9bqWd2PS1QIOSTlxz7fYuUxqDF3VMaYFJ4ddXauxRQZhp8A9dXR3oBEP3KAuQF1toSEWgWfT43bloADi72buy7ZjCTk9jH2uHUAec09jgVLt26mmQESt99HDeybgmkDR9IRjqczwshKwqwr95oEg5hghcMOLlh70GOqUBnjAe%2BcjhQVNOW9LZjEbj0QoMKzTT3OlyG3tpi2Wa1AntH4pXlQ7V99nkGq%2FpHETSrWWwWfCZLxD2rgld%2By2WqmPDlaCfF95BcP1SBZ%2FyN3Ll%2FCXm%2F2zx4ejwTbz7Wb%2BT0oAOY4nL1MqYuIodrZQRgYsdP%2BwczprShVcFs%2BUOP0IEG%2BNjt1L2LdoSsN4C%2FZWin2DFmVKcqWRQvuiI5VGdarcp1IYS&X-Amz-Signature=84c401873c727dd30b736e009cd62f9feb04759189638883a565fc77411838e2&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RTQN3R3D%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCIQC2i9feynNpwykS%2FBMt9UDkEJ%2FN1HPKJePCuZ9%2BPpXWvAIgOlHh3jBjANbZ1fLA2QFqzPuQK%2FrOSQaQB7Q6j0UhGdgq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDC%2FakfuVnne6MdMvxircA0HRto24jAd2QUsbdSSh1L1NeCBgpRaKWZjMJwD5EixxGxuWaeBK4swG5NulGGvyualIsxHXH8uMzGLTlu5iCw6ctyfmb4OLOEwholWebINYtwC9WsrLRNW1MX9DYgx%2FrHz8IyL9SQ6I5jUV0Ttt6hJSYiIFHGyTjfQeC3Ae5hMLkgIQtW94gwVonzcxJ23ZJtGkYURskJvjDZlZgmzhR9UM5tQ2H6wk2BVDrpGL1558ARKKSBd48DpNv4Bb4pXCWZ93tCJOqtaX2lKdgJKjP4zqiIyJuUmb52ab2zfuqDdsePoIxQR1ZvT6phLiDrheqyzBCisI4y%2B8j6q%2FQ1IEYffBCKXun%2F4ejXSyKv3UhYb1vjNgyNBNTR52PRGzBzNi3XBcKBXEPLdLZczVbd14MBrZYo96zpHH%2BTmp3cYV43RKsDoFWQYIgECfX008QsR6UoFsrpVP6%2FGcscys5vy1%2BPjYKzLXEojRUNs6fVQ4hCQYCrIwu1ttvAHZ6FXGjVPY0tz8g%2B6tXb683lW%2FT30rfY85ajTBexzcKgGLy9RpCbBDUEGIF3HsS%2BF3Zp9cNlV5bCV2fAPmnGEBCUZ4ChnP5IRqshgUPpR70ESSc2psb8DOoskWaA66TcGbuyl5MIDmh70GOqUBxiM%2BjB%2Bya%2FIoJ9SJtaXH8lKUXTGcMciZckGJ8m7XCPgGERRuINRcE9z%2B%2FJXe%2BGqKsJNS0KWY4rgX%2FEuAg1%2BFXDthEOUlgzsRAJz9uX%2B88E0IR2IsLDVzD%2BVCSrzNyrMg9IB8he9V1QIjLn2wW7pQv%2BXArTR26g4CTIYBpvwFfiU4B3CfP%2BAP59gqMMoz45WCrSmx5umXmkhOMAW2kmw4RhewaZq%2F&X-Amz-Signature=84e9ad13ea410e76e93478a1441bd1c0cbf5f4dceff26b1469ce7d6361dc4abf&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RTQN3R3D%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCIQC2i9feynNpwykS%2FBMt9UDkEJ%2FN1HPKJePCuZ9%2BPpXWvAIgOlHh3jBjANbZ1fLA2QFqzPuQK%2FrOSQaQB7Q6j0UhGdgq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDC%2FakfuVnne6MdMvxircA0HRto24jAd2QUsbdSSh1L1NeCBgpRaKWZjMJwD5EixxGxuWaeBK4swG5NulGGvyualIsxHXH8uMzGLTlu5iCw6ctyfmb4OLOEwholWebINYtwC9WsrLRNW1MX9DYgx%2FrHz8IyL9SQ6I5jUV0Ttt6hJSYiIFHGyTjfQeC3Ae5hMLkgIQtW94gwVonzcxJ23ZJtGkYURskJvjDZlZgmzhR9UM5tQ2H6wk2BVDrpGL1558ARKKSBd48DpNv4Bb4pXCWZ93tCJOqtaX2lKdgJKjP4zqiIyJuUmb52ab2zfuqDdsePoIxQR1ZvT6phLiDrheqyzBCisI4y%2B8j6q%2FQ1IEYffBCKXun%2F4ejXSyKv3UhYb1vjNgyNBNTR52PRGzBzNi3XBcKBXEPLdLZczVbd14MBrZYo96zpHH%2BTmp3cYV43RKsDoFWQYIgECfX008QsR6UoFsrpVP6%2FGcscys5vy1%2BPjYKzLXEojRUNs6fVQ4hCQYCrIwu1ttvAHZ6FXGjVPY0tz8g%2B6tXb683lW%2FT30rfY85ajTBexzcKgGLy9RpCbBDUEGIF3HsS%2BF3Zp9cNlV5bCV2fAPmnGEBCUZ4ChnP5IRqshgUPpR70ESSc2psb8DOoskWaA66TcGbuyl5MIDmh70GOqUBxiM%2BjB%2Bya%2FIoJ9SJtaXH8lKUXTGcMciZckGJ8m7XCPgGERRuINRcE9z%2B%2FJXe%2BGqKsJNS0KWY4rgX%2FEuAg1%2BFXDthEOUlgzsRAJz9uX%2B88E0IR2IsLDVzD%2BVCSrzNyrMg9IB8he9V1QIjLn2wW7pQv%2BXArTR26g4CTIYBpvwFfiU4B3CfP%2BAP59gqMMoz45WCrSmx5umXmkhOMAW2kmw4RhewaZq%2F&X-Amz-Signature=b95fc41f9cfd716fef06270b5776d9048d2b19d162d2b9e2cb06ed517e687b43&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RTQN3R3D%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCIQC2i9feynNpwykS%2FBMt9UDkEJ%2FN1HPKJePCuZ9%2BPpXWvAIgOlHh3jBjANbZ1fLA2QFqzPuQK%2FrOSQaQB7Q6j0UhGdgq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDC%2FakfuVnne6MdMvxircA0HRto24jAd2QUsbdSSh1L1NeCBgpRaKWZjMJwD5EixxGxuWaeBK4swG5NulGGvyualIsxHXH8uMzGLTlu5iCw6ctyfmb4OLOEwholWebINYtwC9WsrLRNW1MX9DYgx%2FrHz8IyL9SQ6I5jUV0Ttt6hJSYiIFHGyTjfQeC3Ae5hMLkgIQtW94gwVonzcxJ23ZJtGkYURskJvjDZlZgmzhR9UM5tQ2H6wk2BVDrpGL1558ARKKSBd48DpNv4Bb4pXCWZ93tCJOqtaX2lKdgJKjP4zqiIyJuUmb52ab2zfuqDdsePoIxQR1ZvT6phLiDrheqyzBCisI4y%2B8j6q%2FQ1IEYffBCKXun%2F4ejXSyKv3UhYb1vjNgyNBNTR52PRGzBzNi3XBcKBXEPLdLZczVbd14MBrZYo96zpHH%2BTmp3cYV43RKsDoFWQYIgECfX008QsR6UoFsrpVP6%2FGcscys5vy1%2BPjYKzLXEojRUNs6fVQ4hCQYCrIwu1ttvAHZ6FXGjVPY0tz8g%2B6tXb683lW%2FT30rfY85ajTBexzcKgGLy9RpCbBDUEGIF3HsS%2BF3Zp9cNlV5bCV2fAPmnGEBCUZ4ChnP5IRqshgUPpR70ESSc2psb8DOoskWaA66TcGbuyl5MIDmh70GOqUBxiM%2BjB%2Bya%2FIoJ9SJtaXH8lKUXTGcMciZckGJ8m7XCPgGERRuINRcE9z%2B%2FJXe%2BGqKsJNS0KWY4rgX%2FEuAg1%2BFXDthEOUlgzsRAJz9uX%2B88E0IR2IsLDVzD%2BVCSrzNyrMg9IB8he9V1QIjLn2wW7pQv%2BXArTR26g4CTIYBpvwFfiU4B3CfP%2BAP59gqMMoz45WCrSmx5umXmkhOMAW2kmw4RhewaZq%2F&X-Amz-Signature=dace69acc248dc467ddf00c145084051f00a79ed132edc4af91c036e9c901a9e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RTQN3R3D%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCIQC2i9feynNpwykS%2FBMt9UDkEJ%2FN1HPKJePCuZ9%2BPpXWvAIgOlHh3jBjANbZ1fLA2QFqzPuQK%2FrOSQaQB7Q6j0UhGdgq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDC%2FakfuVnne6MdMvxircA0HRto24jAd2QUsbdSSh1L1NeCBgpRaKWZjMJwD5EixxGxuWaeBK4swG5NulGGvyualIsxHXH8uMzGLTlu5iCw6ctyfmb4OLOEwholWebINYtwC9WsrLRNW1MX9DYgx%2FrHz8IyL9SQ6I5jUV0Ttt6hJSYiIFHGyTjfQeC3Ae5hMLkgIQtW94gwVonzcxJ23ZJtGkYURskJvjDZlZgmzhR9UM5tQ2H6wk2BVDrpGL1558ARKKSBd48DpNv4Bb4pXCWZ93tCJOqtaX2lKdgJKjP4zqiIyJuUmb52ab2zfuqDdsePoIxQR1ZvT6phLiDrheqyzBCisI4y%2B8j6q%2FQ1IEYffBCKXun%2F4ejXSyKv3UhYb1vjNgyNBNTR52PRGzBzNi3XBcKBXEPLdLZczVbd14MBrZYo96zpHH%2BTmp3cYV43RKsDoFWQYIgECfX008QsR6UoFsrpVP6%2FGcscys5vy1%2BPjYKzLXEojRUNs6fVQ4hCQYCrIwu1ttvAHZ6FXGjVPY0tz8g%2B6tXb683lW%2FT30rfY85ajTBexzcKgGLy9RpCbBDUEGIF3HsS%2BF3Zp9cNlV5bCV2fAPmnGEBCUZ4ChnP5IRqshgUPpR70ESSc2psb8DOoskWaA66TcGbuyl5MIDmh70GOqUBxiM%2BjB%2Bya%2FIoJ9SJtaXH8lKUXTGcMciZckGJ8m7XCPgGERRuINRcE9z%2B%2FJXe%2BGqKsJNS0KWY4rgX%2FEuAg1%2BFXDthEOUlgzsRAJz9uX%2B88E0IR2IsLDVzD%2BVCSrzNyrMg9IB8he9V1QIjLn2wW7pQv%2BXArTR26g4CTIYBpvwFfiU4B3CfP%2BAP59gqMMoz45WCrSmx5umXmkhOMAW2kmw4RhewaZq%2F&X-Amz-Signature=04eb346cbf117abb001a34f1deb10080f7f16c857d310905adc110e9d9474a90&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RTQN3R3D%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCIQC2i9feynNpwykS%2FBMt9UDkEJ%2FN1HPKJePCuZ9%2BPpXWvAIgOlHh3jBjANbZ1fLA2QFqzPuQK%2FrOSQaQB7Q6j0UhGdgq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDC%2FakfuVnne6MdMvxircA0HRto24jAd2QUsbdSSh1L1NeCBgpRaKWZjMJwD5EixxGxuWaeBK4swG5NulGGvyualIsxHXH8uMzGLTlu5iCw6ctyfmb4OLOEwholWebINYtwC9WsrLRNW1MX9DYgx%2FrHz8IyL9SQ6I5jUV0Ttt6hJSYiIFHGyTjfQeC3Ae5hMLkgIQtW94gwVonzcxJ23ZJtGkYURskJvjDZlZgmzhR9UM5tQ2H6wk2BVDrpGL1558ARKKSBd48DpNv4Bb4pXCWZ93tCJOqtaX2lKdgJKjP4zqiIyJuUmb52ab2zfuqDdsePoIxQR1ZvT6phLiDrheqyzBCisI4y%2B8j6q%2FQ1IEYffBCKXun%2F4ejXSyKv3UhYb1vjNgyNBNTR52PRGzBzNi3XBcKBXEPLdLZczVbd14MBrZYo96zpHH%2BTmp3cYV43RKsDoFWQYIgECfX008QsR6UoFsrpVP6%2FGcscys5vy1%2BPjYKzLXEojRUNs6fVQ4hCQYCrIwu1ttvAHZ6FXGjVPY0tz8g%2B6tXb683lW%2FT30rfY85ajTBexzcKgGLy9RpCbBDUEGIF3HsS%2BF3Zp9cNlV5bCV2fAPmnGEBCUZ4ChnP5IRqshgUPpR70ESSc2psb8DOoskWaA66TcGbuyl5MIDmh70GOqUBxiM%2BjB%2Bya%2FIoJ9SJtaXH8lKUXTGcMciZckGJ8m7XCPgGERRuINRcE9z%2B%2FJXe%2BGqKsJNS0KWY4rgX%2FEuAg1%2BFXDthEOUlgzsRAJz9uX%2B88E0IR2IsLDVzD%2BVCSrzNyrMg9IB8he9V1QIjLn2wW7pQv%2BXArTR26g4CTIYBpvwFfiU4B3CfP%2BAP59gqMMoz45WCrSmx5umXmkhOMAW2kmw4RhewaZq%2F&X-Amz-Signature=092cf9f50d85c03cc8c4aa8f361f00d0e5b5e8a4770256ad6022da13518c3a04&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y322KDY7%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCIQDXlCLACCHagyPafEmcGPJEg396iUQTPgene5rKvpp71wIgJy7zXu2PAVNUPpM34Vf%2BpYrmY%2BiLfrvmgO82z9ZMnk4q%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDNaqRsSHH%2BhnMbrcRyrcAwfgFd%2FJLriAFzLjTHK2eY9a2gotJZYbGUt3Vr3QXlcGRWQX2CqHGGBFt27FO2UsviBj0%2F5bbQJM1o0fcAZogxJqtgHbdbDSLAbs%2Fx31HpfUEQ0EmCJrWEC2Af5Qf0OMPIEsnOoGvYDNQRNJzHs0Uh67jyAqDxZe9V2X8mHPFWoWxGKol7aKNWPGTZZGwwkMH4f9IhBgxnAJ0dCVSpwMwFV5cfLqtp4Pbwgc%2BUa%2BsSoxUDrm5u%2BO0jC46isDTXkcMazPaGDEwNPaMcbdeqLfbLWKwuxC185WHrByaj4r7c9Rg96EBe6xzYywa1yo9fYRtt9JSNuhBA7xgXI4r%2F9Aejw2DP%2FQhTnA2pMB%2Fut%2FeNfCKNuTpRQu9T1UaKJ2VJKVRu19kAyd%2B3DaZUnjgDJxKzWTYcsVRh4GLnKL5rvc2XCLzQq%2FN1vccmAzRR4G9H8%2FdP1lp9Yv48Uu4l2P4ib95uKZLHDKLFmbyeF9bqWd2PS1QIOSTlxz7fYuUxqDF3VMaYFJ4ddXauxRQZhp8A9dXR3oBEP3KAuQF1toSEWgWfT43bloADi72buy7ZjCTk9jH2uHUAec09jgVLt26mmQESt99HDeybgmkDR9IRjqczwshKwqwr95oEg5hghcMOLlh70GOqUBnjAe%2BcjhQVNOW9LZjEbj0QoMKzTT3OlyG3tpi2Wa1AntH4pXlQ7V99nkGq%2FpHETSrWWwWfCZLxD2rgld%2By2WqmPDlaCfF95BcP1SBZ%2FyN3Ll%2FCXm%2F2zx4ejwTbz7Wb%2BT0oAOY4nL1MqYuIodrZQRgYsdP%2BwczprShVcFs%2BUOP0IEG%2BNjt1L2LdoSsN4C%2FZWin2DFmVKcqWRQvuiI5VGdarcp1IYS&X-Amz-Signature=4892d04df336ad9573e67e22c5e15775ecb6c6605720cf61bab02323befb66f8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y322KDY7%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCIQDXlCLACCHagyPafEmcGPJEg396iUQTPgene5rKvpp71wIgJy7zXu2PAVNUPpM34Vf%2BpYrmY%2BiLfrvmgO82z9ZMnk4q%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDNaqRsSHH%2BhnMbrcRyrcAwfgFd%2FJLriAFzLjTHK2eY9a2gotJZYbGUt3Vr3QXlcGRWQX2CqHGGBFt27FO2UsviBj0%2F5bbQJM1o0fcAZogxJqtgHbdbDSLAbs%2Fx31HpfUEQ0EmCJrWEC2Af5Qf0OMPIEsnOoGvYDNQRNJzHs0Uh67jyAqDxZe9V2X8mHPFWoWxGKol7aKNWPGTZZGwwkMH4f9IhBgxnAJ0dCVSpwMwFV5cfLqtp4Pbwgc%2BUa%2BsSoxUDrm5u%2BO0jC46isDTXkcMazPaGDEwNPaMcbdeqLfbLWKwuxC185WHrByaj4r7c9Rg96EBe6xzYywa1yo9fYRtt9JSNuhBA7xgXI4r%2F9Aejw2DP%2FQhTnA2pMB%2Fut%2FeNfCKNuTpRQu9T1UaKJ2VJKVRu19kAyd%2B3DaZUnjgDJxKzWTYcsVRh4GLnKL5rvc2XCLzQq%2FN1vccmAzRR4G9H8%2FdP1lp9Yv48Uu4l2P4ib95uKZLHDKLFmbyeF9bqWd2PS1QIOSTlxz7fYuUxqDF3VMaYFJ4ddXauxRQZhp8A9dXR3oBEP3KAuQF1toSEWgWfT43bloADi72buy7ZjCTk9jH2uHUAec09jgVLt26mmQESt99HDeybgmkDR9IRjqczwshKwqwr95oEg5hghcMOLlh70GOqUBnjAe%2BcjhQVNOW9LZjEbj0QoMKzTT3OlyG3tpi2Wa1AntH4pXlQ7V99nkGq%2FpHETSrWWwWfCZLxD2rgld%2By2WqmPDlaCfF95BcP1SBZ%2FyN3Ll%2FCXm%2F2zx4ejwTbz7Wb%2BT0oAOY4nL1MqYuIodrZQRgYsdP%2BwczprShVcFs%2BUOP0IEG%2BNjt1L2LdoSsN4C%2FZWin2DFmVKcqWRQvuiI5VGdarcp1IYS&X-Amz-Signature=c0a85003e01035ea4a9882dff5251ef970ff1bf0cad595aedd7eb6e074b22113&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y322KDY7%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCIQDXlCLACCHagyPafEmcGPJEg396iUQTPgene5rKvpp71wIgJy7zXu2PAVNUPpM34Vf%2BpYrmY%2BiLfrvmgO82z9ZMnk4q%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDNaqRsSHH%2BhnMbrcRyrcAwfgFd%2FJLriAFzLjTHK2eY9a2gotJZYbGUt3Vr3QXlcGRWQX2CqHGGBFt27FO2UsviBj0%2F5bbQJM1o0fcAZogxJqtgHbdbDSLAbs%2Fx31HpfUEQ0EmCJrWEC2Af5Qf0OMPIEsnOoGvYDNQRNJzHs0Uh67jyAqDxZe9V2X8mHPFWoWxGKol7aKNWPGTZZGwwkMH4f9IhBgxnAJ0dCVSpwMwFV5cfLqtp4Pbwgc%2BUa%2BsSoxUDrm5u%2BO0jC46isDTXkcMazPaGDEwNPaMcbdeqLfbLWKwuxC185WHrByaj4r7c9Rg96EBe6xzYywa1yo9fYRtt9JSNuhBA7xgXI4r%2F9Aejw2DP%2FQhTnA2pMB%2Fut%2FeNfCKNuTpRQu9T1UaKJ2VJKVRu19kAyd%2B3DaZUnjgDJxKzWTYcsVRh4GLnKL5rvc2XCLzQq%2FN1vccmAzRR4G9H8%2FdP1lp9Yv48Uu4l2P4ib95uKZLHDKLFmbyeF9bqWd2PS1QIOSTlxz7fYuUxqDF3VMaYFJ4ddXauxRQZhp8A9dXR3oBEP3KAuQF1toSEWgWfT43bloADi72buy7ZjCTk9jH2uHUAec09jgVLt26mmQESt99HDeybgmkDR9IRjqczwshKwqwr95oEg5hghcMOLlh70GOqUBnjAe%2BcjhQVNOW9LZjEbj0QoMKzTT3OlyG3tpi2Wa1AntH4pXlQ7V99nkGq%2FpHETSrWWwWfCZLxD2rgld%2By2WqmPDlaCfF95BcP1SBZ%2FyN3Ll%2FCXm%2F2zx4ejwTbz7Wb%2BT0oAOY4nL1MqYuIodrZQRgYsdP%2BwczprShVcFs%2BUOP0IEG%2BNjt1L2LdoSsN4C%2FZWin2DFmVKcqWRQvuiI5VGdarcp1IYS&X-Amz-Signature=91c51821d08cdee0072af811cd09f1035c087bd6dbbfef5108743efadac98991&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y322KDY7%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCIQDXlCLACCHagyPafEmcGPJEg396iUQTPgene5rKvpp71wIgJy7zXu2PAVNUPpM34Vf%2BpYrmY%2BiLfrvmgO82z9ZMnk4q%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDNaqRsSHH%2BhnMbrcRyrcAwfgFd%2FJLriAFzLjTHK2eY9a2gotJZYbGUt3Vr3QXlcGRWQX2CqHGGBFt27FO2UsviBj0%2F5bbQJM1o0fcAZogxJqtgHbdbDSLAbs%2Fx31HpfUEQ0EmCJrWEC2Af5Qf0OMPIEsnOoGvYDNQRNJzHs0Uh67jyAqDxZe9V2X8mHPFWoWxGKol7aKNWPGTZZGwwkMH4f9IhBgxnAJ0dCVSpwMwFV5cfLqtp4Pbwgc%2BUa%2BsSoxUDrm5u%2BO0jC46isDTXkcMazPaGDEwNPaMcbdeqLfbLWKwuxC185WHrByaj4r7c9Rg96EBe6xzYywa1yo9fYRtt9JSNuhBA7xgXI4r%2F9Aejw2DP%2FQhTnA2pMB%2Fut%2FeNfCKNuTpRQu9T1UaKJ2VJKVRu19kAyd%2B3DaZUnjgDJxKzWTYcsVRh4GLnKL5rvc2XCLzQq%2FN1vccmAzRR4G9H8%2FdP1lp9Yv48Uu4l2P4ib95uKZLHDKLFmbyeF9bqWd2PS1QIOSTlxz7fYuUxqDF3VMaYFJ4ddXauxRQZhp8A9dXR3oBEP3KAuQF1toSEWgWfT43bloADi72buy7ZjCTk9jH2uHUAec09jgVLt26mmQESt99HDeybgmkDR9IRjqczwshKwqwr95oEg5hghcMOLlh70GOqUBnjAe%2BcjhQVNOW9LZjEbj0QoMKzTT3OlyG3tpi2Wa1AntH4pXlQ7V99nkGq%2FpHETSrWWwWfCZLxD2rgld%2By2WqmPDlaCfF95BcP1SBZ%2FyN3Ll%2FCXm%2F2zx4ejwTbz7Wb%2BT0oAOY4nL1MqYuIodrZQRgYsdP%2BwczprShVcFs%2BUOP0IEG%2BNjt1L2LdoSsN4C%2FZWin2DFmVKcqWRQvuiI5VGdarcp1IYS&X-Amz-Signature=1fdf04fd3f9bbde87102857a7982c79dc80b22fc939cb79f66f98a4443979301&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y322KDY7%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCIQDXlCLACCHagyPafEmcGPJEg396iUQTPgene5rKvpp71wIgJy7zXu2PAVNUPpM34Vf%2BpYrmY%2BiLfrvmgO82z9ZMnk4q%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDNaqRsSHH%2BhnMbrcRyrcAwfgFd%2FJLriAFzLjTHK2eY9a2gotJZYbGUt3Vr3QXlcGRWQX2CqHGGBFt27FO2UsviBj0%2F5bbQJM1o0fcAZogxJqtgHbdbDSLAbs%2Fx31HpfUEQ0EmCJrWEC2Af5Qf0OMPIEsnOoGvYDNQRNJzHs0Uh67jyAqDxZe9V2X8mHPFWoWxGKol7aKNWPGTZZGwwkMH4f9IhBgxnAJ0dCVSpwMwFV5cfLqtp4Pbwgc%2BUa%2BsSoxUDrm5u%2BO0jC46isDTXkcMazPaGDEwNPaMcbdeqLfbLWKwuxC185WHrByaj4r7c9Rg96EBe6xzYywa1yo9fYRtt9JSNuhBA7xgXI4r%2F9Aejw2DP%2FQhTnA2pMB%2Fut%2FeNfCKNuTpRQu9T1UaKJ2VJKVRu19kAyd%2B3DaZUnjgDJxKzWTYcsVRh4GLnKL5rvc2XCLzQq%2FN1vccmAzRR4G9H8%2FdP1lp9Yv48Uu4l2P4ib95uKZLHDKLFmbyeF9bqWd2PS1QIOSTlxz7fYuUxqDF3VMaYFJ4ddXauxRQZhp8A9dXR3oBEP3KAuQF1toSEWgWfT43bloADi72buy7ZjCTk9jH2uHUAec09jgVLt26mmQESt99HDeybgmkDR9IRjqczwshKwqwr95oEg5hghcMOLlh70GOqUBnjAe%2BcjhQVNOW9LZjEbj0QoMKzTT3OlyG3tpi2Wa1AntH4pXlQ7V99nkGq%2FpHETSrWWwWfCZLxD2rgld%2By2WqmPDlaCfF95BcP1SBZ%2FyN3Ll%2FCXm%2F2zx4ejwTbz7Wb%2BT0oAOY4nL1MqYuIodrZQRgYsdP%2BwczprShVcFs%2BUOP0IEG%2BNjt1L2LdoSsN4C%2FZWin2DFmVKcqWRQvuiI5VGdarcp1IYS&X-Amz-Signature=92e7dfeca7b1ac0b548b718b2ee7d1caf40a826208d4367a7194fffe587283cd&X-Amz-SignedHeaders=host&x-id=GetObject)
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


