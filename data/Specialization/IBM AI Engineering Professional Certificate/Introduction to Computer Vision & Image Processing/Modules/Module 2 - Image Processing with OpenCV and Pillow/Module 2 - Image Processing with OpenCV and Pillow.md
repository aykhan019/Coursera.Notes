

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665B4WSL6J%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBoaMlOSvwc4TSNeDwxw7FPz90pfY6H56MAhszPw%2FMZ1AiEAsDUMMNqhgk%2BMD0VIaejX474cenSQne9oAcGiTvaODLkqiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM64DYQfgLWVl8sbayrcA4P8eG8E8%2F82w347bVTV0Hhd4I%2BwjYWGGR3%2FUEwdnRHr2W0baoKXgeRk%2BuolD8qx5VyTQVBZrykBVWA46Kt3F1ROMnGnBcLizHumiCHLfsne%2F73kEatsy%2BXxcgKzJ4O7s3dIzrgV4AOOsBs0F%2FZ6frKs1FcX%2BJmk4m5jPN2p%2F4OzgM560JOaJM%2FpCr83%2FHz%2B8i9B2%2FBfTDZbRmoZTOUVbka%2BC5RNQ%2B1S7ZuzN9%2F73jY43J50TQ%2BeRKkuhEFrNbvFYsnPNTKJPjd7FOmhTo8jqHCTb8HLOefSBjhMrEvwRyt65Q8jawGd4MZbZ4hXeUB%2BS%2FeZ%2F9MfVEeGD4TI79%2BLqIjrIvAunsSU0V0EOCtKA5nNJmMq9fLOxDrzZKp5F77R56whftlMUu35pD4bumFQq4uRpWN6hJJXGUh5moDVWq%2BwoDLMOCtZ4o3tRA46cVWJYQHOs40LCsKoW573cq%2BmGU0%2BHn1qlQlxJHCO0DN500WjdJ42OtdHWHzRoLLBIz8wEsf2W2tNDbLlqdt4LFCgurJXrGDswFyUZJ9nMALfPHD4fE5Uv03x%2Bic3rSC8fdRGxyoXZNGngsw85V%2BM0xl4eQ8PJYdEzDOHkQzXGj1XeSDD2%2BXl6MsSDAyV467JMNLF6rwGOqUB964Kb3wttKGoEeFLzH3aw51vppFOs5%2FIEWVu9HeWQF%2F6mfd8v1hJVIqm86CQ3LnfU5RYDEXCsu%2BnHSxtIpZWgleWVoBWsFcpYeNBDxIfy4DiUdKAsUQ3gx6WM4ZM3UXMixhkEZ4G4J2W0L637sN2o9gC%2BEDREWr3T6YkCWRN6ftbh1spjc%2FW%2Bg5BzLk3%2B2dZ4CQzi2wL4wL0CheWLDSLGJkeOzpZ&X-Amz-Signature=ae59316f1e61e894001f7ab22ac6a9cd1795d614a9fce0539e3a803f475a5218&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W4BYOBPH%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIALHGEC4SAIVRvwMqlq1GSB9fKN1XZZ9Lwa2gcmy6Bh2AiEA3jxYHy2YjDfBSP9Zdqw7sB%2BwbyV3Br7CliHmAfTHXkkqiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAJ0OOkGc42EedUYCSrcA6uHyfU0vb2Mi%2BccQ2C1c2ZbUlLS3vBBuJ8puq3LkXY%2FegTPYrprSdf8X62fCd4cPtFkR7jKybIfh6YZwF5AbJjN42ZqrP7MlBwBxUapVH6PUcadONNgeNW9nQ%2BLv8Fd7RszZHdRIKm8yFq3QvjZQYpDYMFoDaiURXlCu1I%2Bl6GLCjrPhIMfgDeP5ZXrbOlJhYv81dY47f9wW5PnvNq%2BQmx69pXWi1JuJ2O4lB1a5%2BrvBPGQgc%2FNgug8AWFNCw1gKbHg20Xdvsbe73ln%2Fecq50esanQyERp9em%2BZnPJBhIXB1kAOmsjLwXAk6yCj%2Bh7qocVqSrM6LxLLBAkfSDnIE2JgJlZfwyIQv7Vz9wrztK4jjAYTn54YMj8vfq45Xue889ckLbIrKrOrHsAFIP5H0tgJK29dNCti3MKKBAyd7KQOPawJMzuA2ZQ4J1KdSzcSlNLBMb0kWqDs2K073nViiGk1ZQzSHaumDpKJ5TztrEIebVRXpFIaDSUdw6ugm6FHIUYewi37ej9fIuhBdieVAJK6FrHaJWUxQnE%2Bzv%2F6kPlJVmxQ%2BpLC9MTQGsgdufATh9rAPZyOvgt5qZC%2FEoj%2Fu%2F3pM0Nqr7q%2F5usaAbjVMTvtex0YWN%2B0E9XNtN%2FCMOHF6rwGOqUBQXj8PIe%2FXOCmw2cV5WRxo6A1Xxo4ws5VcZVjqlKlJ%2BaaZqMEhNWgVV%2F%2FIoOP3TYWRF48wD8oFXZ8eVjOJVXAFIFX9EvN%2BdqrbMY54lwu1TXOBISH7SpSxnTdmAffBGRyd9KdhBs6rGqtf%2Fi52bg%2FEQK%2F77mL7zoiBYDRIcA9LGXY0nG7GoGjVTnHyQpXoLXAu5GCimwGbsg3%2Bsxpn9Fzi4FQjbNm&X-Amz-Signature=9842c6ed3530dd295d274b50508e83b504cbce357a16a5ec1399fb9d96ba0629&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W4BYOBPH%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIALHGEC4SAIVRvwMqlq1GSB9fKN1XZZ9Lwa2gcmy6Bh2AiEA3jxYHy2YjDfBSP9Zdqw7sB%2BwbyV3Br7CliHmAfTHXkkqiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAJ0OOkGc42EedUYCSrcA6uHyfU0vb2Mi%2BccQ2C1c2ZbUlLS3vBBuJ8puq3LkXY%2FegTPYrprSdf8X62fCd4cPtFkR7jKybIfh6YZwF5AbJjN42ZqrP7MlBwBxUapVH6PUcadONNgeNW9nQ%2BLv8Fd7RszZHdRIKm8yFq3QvjZQYpDYMFoDaiURXlCu1I%2Bl6GLCjrPhIMfgDeP5ZXrbOlJhYv81dY47f9wW5PnvNq%2BQmx69pXWi1JuJ2O4lB1a5%2BrvBPGQgc%2FNgug8AWFNCw1gKbHg20Xdvsbe73ln%2Fecq50esanQyERp9em%2BZnPJBhIXB1kAOmsjLwXAk6yCj%2Bh7qocVqSrM6LxLLBAkfSDnIE2JgJlZfwyIQv7Vz9wrztK4jjAYTn54YMj8vfq45Xue889ckLbIrKrOrHsAFIP5H0tgJK29dNCti3MKKBAyd7KQOPawJMzuA2ZQ4J1KdSzcSlNLBMb0kWqDs2K073nViiGk1ZQzSHaumDpKJ5TztrEIebVRXpFIaDSUdw6ugm6FHIUYewi37ej9fIuhBdieVAJK6FrHaJWUxQnE%2Bzv%2F6kPlJVmxQ%2BpLC9MTQGsgdufATh9rAPZyOvgt5qZC%2FEoj%2Fu%2F3pM0Nqr7q%2F5usaAbjVMTvtex0YWN%2B0E9XNtN%2FCMOHF6rwGOqUBQXj8PIe%2FXOCmw2cV5WRxo6A1Xxo4ws5VcZVjqlKlJ%2BaaZqMEhNWgVV%2F%2FIoOP3TYWRF48wD8oFXZ8eVjOJVXAFIFX9EvN%2BdqrbMY54lwu1TXOBISH7SpSxnTdmAffBGRyd9KdhBs6rGqtf%2Fi52bg%2FEQK%2F77mL7zoiBYDRIcA9LGXY0nG7GoGjVTnHyQpXoLXAu5GCimwGbsg3%2Bsxpn9Fzi4FQjbNm&X-Amz-Signature=35bb43fb9181a400d7c9bdd889e6eb04fd35dc2eb1b5f3ab70255b357b053d31&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W4BYOBPH%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIALHGEC4SAIVRvwMqlq1GSB9fKN1XZZ9Lwa2gcmy6Bh2AiEA3jxYHy2YjDfBSP9Zdqw7sB%2BwbyV3Br7CliHmAfTHXkkqiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAJ0OOkGc42EedUYCSrcA6uHyfU0vb2Mi%2BccQ2C1c2ZbUlLS3vBBuJ8puq3LkXY%2FegTPYrprSdf8X62fCd4cPtFkR7jKybIfh6YZwF5AbJjN42ZqrP7MlBwBxUapVH6PUcadONNgeNW9nQ%2BLv8Fd7RszZHdRIKm8yFq3QvjZQYpDYMFoDaiURXlCu1I%2Bl6GLCjrPhIMfgDeP5ZXrbOlJhYv81dY47f9wW5PnvNq%2BQmx69pXWi1JuJ2O4lB1a5%2BrvBPGQgc%2FNgug8AWFNCw1gKbHg20Xdvsbe73ln%2Fecq50esanQyERp9em%2BZnPJBhIXB1kAOmsjLwXAk6yCj%2Bh7qocVqSrM6LxLLBAkfSDnIE2JgJlZfwyIQv7Vz9wrztK4jjAYTn54YMj8vfq45Xue889ckLbIrKrOrHsAFIP5H0tgJK29dNCti3MKKBAyd7KQOPawJMzuA2ZQ4J1KdSzcSlNLBMb0kWqDs2K073nViiGk1ZQzSHaumDpKJ5TztrEIebVRXpFIaDSUdw6ugm6FHIUYewi37ej9fIuhBdieVAJK6FrHaJWUxQnE%2Bzv%2F6kPlJVmxQ%2BpLC9MTQGsgdufATh9rAPZyOvgt5qZC%2FEoj%2Fu%2F3pM0Nqr7q%2F5usaAbjVMTvtex0YWN%2B0E9XNtN%2FCMOHF6rwGOqUBQXj8PIe%2FXOCmw2cV5WRxo6A1Xxo4ws5VcZVjqlKlJ%2BaaZqMEhNWgVV%2F%2FIoOP3TYWRF48wD8oFXZ8eVjOJVXAFIFX9EvN%2BdqrbMY54lwu1TXOBISH7SpSxnTdmAffBGRyd9KdhBs6rGqtf%2Fi52bg%2FEQK%2F77mL7zoiBYDRIcA9LGXY0nG7GoGjVTnHyQpXoLXAu5GCimwGbsg3%2Bsxpn9Fzi4FQjbNm&X-Amz-Signature=32b513901a7d0cd253da755b9b42224c12062f976087384a02e46d5d38fec528&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W4BYOBPH%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIALHGEC4SAIVRvwMqlq1GSB9fKN1XZZ9Lwa2gcmy6Bh2AiEA3jxYHy2YjDfBSP9Zdqw7sB%2BwbyV3Br7CliHmAfTHXkkqiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAJ0OOkGc42EedUYCSrcA6uHyfU0vb2Mi%2BccQ2C1c2ZbUlLS3vBBuJ8puq3LkXY%2FegTPYrprSdf8X62fCd4cPtFkR7jKybIfh6YZwF5AbJjN42ZqrP7MlBwBxUapVH6PUcadONNgeNW9nQ%2BLv8Fd7RszZHdRIKm8yFq3QvjZQYpDYMFoDaiURXlCu1I%2Bl6GLCjrPhIMfgDeP5ZXrbOlJhYv81dY47f9wW5PnvNq%2BQmx69pXWi1JuJ2O4lB1a5%2BrvBPGQgc%2FNgug8AWFNCw1gKbHg20Xdvsbe73ln%2Fecq50esanQyERp9em%2BZnPJBhIXB1kAOmsjLwXAk6yCj%2Bh7qocVqSrM6LxLLBAkfSDnIE2JgJlZfwyIQv7Vz9wrztK4jjAYTn54YMj8vfq45Xue889ckLbIrKrOrHsAFIP5H0tgJK29dNCti3MKKBAyd7KQOPawJMzuA2ZQ4J1KdSzcSlNLBMb0kWqDs2K073nViiGk1ZQzSHaumDpKJ5TztrEIebVRXpFIaDSUdw6ugm6FHIUYewi37ej9fIuhBdieVAJK6FrHaJWUxQnE%2Bzv%2F6kPlJVmxQ%2BpLC9MTQGsgdufATh9rAPZyOvgt5qZC%2FEoj%2Fu%2F3pM0Nqr7q%2F5usaAbjVMTvtex0YWN%2B0E9XNtN%2FCMOHF6rwGOqUBQXj8PIe%2FXOCmw2cV5WRxo6A1Xxo4ws5VcZVjqlKlJ%2BaaZqMEhNWgVV%2F%2FIoOP3TYWRF48wD8oFXZ8eVjOJVXAFIFX9EvN%2BdqrbMY54lwu1TXOBISH7SpSxnTdmAffBGRyd9KdhBs6rGqtf%2Fi52bg%2FEQK%2F77mL7zoiBYDRIcA9LGXY0nG7GoGjVTnHyQpXoLXAu5GCimwGbsg3%2Bsxpn9Fzi4FQjbNm&X-Amz-Signature=5789690bf5ad7244956ca44d5af3ca857a76a6cec84d926052c615ef6c56a100&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W4BYOBPH%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIALHGEC4SAIVRvwMqlq1GSB9fKN1XZZ9Lwa2gcmy6Bh2AiEA3jxYHy2YjDfBSP9Zdqw7sB%2BwbyV3Br7CliHmAfTHXkkqiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAJ0OOkGc42EedUYCSrcA6uHyfU0vb2Mi%2BccQ2C1c2ZbUlLS3vBBuJ8puq3LkXY%2FegTPYrprSdf8X62fCd4cPtFkR7jKybIfh6YZwF5AbJjN42ZqrP7MlBwBxUapVH6PUcadONNgeNW9nQ%2BLv8Fd7RszZHdRIKm8yFq3QvjZQYpDYMFoDaiURXlCu1I%2Bl6GLCjrPhIMfgDeP5ZXrbOlJhYv81dY47f9wW5PnvNq%2BQmx69pXWi1JuJ2O4lB1a5%2BrvBPGQgc%2FNgug8AWFNCw1gKbHg20Xdvsbe73ln%2Fecq50esanQyERp9em%2BZnPJBhIXB1kAOmsjLwXAk6yCj%2Bh7qocVqSrM6LxLLBAkfSDnIE2JgJlZfwyIQv7Vz9wrztK4jjAYTn54YMj8vfq45Xue889ckLbIrKrOrHsAFIP5H0tgJK29dNCti3MKKBAyd7KQOPawJMzuA2ZQ4J1KdSzcSlNLBMb0kWqDs2K073nViiGk1ZQzSHaumDpKJ5TztrEIebVRXpFIaDSUdw6ugm6FHIUYewi37ej9fIuhBdieVAJK6FrHaJWUxQnE%2Bzv%2F6kPlJVmxQ%2BpLC9MTQGsgdufATh9rAPZyOvgt5qZC%2FEoj%2Fu%2F3pM0Nqr7q%2F5usaAbjVMTvtex0YWN%2B0E9XNtN%2FCMOHF6rwGOqUBQXj8PIe%2FXOCmw2cV5WRxo6A1Xxo4ws5VcZVjqlKlJ%2BaaZqMEhNWgVV%2F%2FIoOP3TYWRF48wD8oFXZ8eVjOJVXAFIFX9EvN%2BdqrbMY54lwu1TXOBISH7SpSxnTdmAffBGRyd9KdhBs6rGqtf%2Fi52bg%2FEQK%2F77mL7zoiBYDRIcA9LGXY0nG7GoGjVTnHyQpXoLXAu5GCimwGbsg3%2Bsxpn9Fzi4FQjbNm&X-Amz-Signature=a52bba18b6ad82f9445648573c00793edac82ae969c9ef77b3c8ebbfc7d6678c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665B4WSL6J%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBoaMlOSvwc4TSNeDwxw7FPz90pfY6H56MAhszPw%2FMZ1AiEAsDUMMNqhgk%2BMD0VIaejX474cenSQne9oAcGiTvaODLkqiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM64DYQfgLWVl8sbayrcA4P8eG8E8%2F82w347bVTV0Hhd4I%2BwjYWGGR3%2FUEwdnRHr2W0baoKXgeRk%2BuolD8qx5VyTQVBZrykBVWA46Kt3F1ROMnGnBcLizHumiCHLfsne%2F73kEatsy%2BXxcgKzJ4O7s3dIzrgV4AOOsBs0F%2FZ6frKs1FcX%2BJmk4m5jPN2p%2F4OzgM560JOaJM%2FpCr83%2FHz%2B8i9B2%2FBfTDZbRmoZTOUVbka%2BC5RNQ%2B1S7ZuzN9%2F73jY43J50TQ%2BeRKkuhEFrNbvFYsnPNTKJPjd7FOmhTo8jqHCTb8HLOefSBjhMrEvwRyt65Q8jawGd4MZbZ4hXeUB%2BS%2FeZ%2F9MfVEeGD4TI79%2BLqIjrIvAunsSU0V0EOCtKA5nNJmMq9fLOxDrzZKp5F77R56whftlMUu35pD4bumFQq4uRpWN6hJJXGUh5moDVWq%2BwoDLMOCtZ4o3tRA46cVWJYQHOs40LCsKoW573cq%2BmGU0%2BHn1qlQlxJHCO0DN500WjdJ42OtdHWHzRoLLBIz8wEsf2W2tNDbLlqdt4LFCgurJXrGDswFyUZJ9nMALfPHD4fE5Uv03x%2Bic3rSC8fdRGxyoXZNGngsw85V%2BM0xl4eQ8PJYdEzDOHkQzXGj1XeSDD2%2BXl6MsSDAyV467JMNLF6rwGOqUB964Kb3wttKGoEeFLzH3aw51vppFOs5%2FIEWVu9HeWQF%2F6mfd8v1hJVIqm86CQ3LnfU5RYDEXCsu%2BnHSxtIpZWgleWVoBWsFcpYeNBDxIfy4DiUdKAsUQ3gx6WM4ZM3UXMixhkEZ4G4J2W0L637sN2o9gC%2BEDREWr3T6YkCWRN6ftbh1spjc%2FW%2Bg5BzLk3%2B2dZ4CQzi2wL4wL0CheWLDSLGJkeOzpZ&X-Amz-Signature=8e0e5e1ceab30774bbadbc5b588494f952ef907951e34751d32ad9067225ac2a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665B4WSL6J%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBoaMlOSvwc4TSNeDwxw7FPz90pfY6H56MAhszPw%2FMZ1AiEAsDUMMNqhgk%2BMD0VIaejX474cenSQne9oAcGiTvaODLkqiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM64DYQfgLWVl8sbayrcA4P8eG8E8%2F82w347bVTV0Hhd4I%2BwjYWGGR3%2FUEwdnRHr2W0baoKXgeRk%2BuolD8qx5VyTQVBZrykBVWA46Kt3F1ROMnGnBcLizHumiCHLfsne%2F73kEatsy%2BXxcgKzJ4O7s3dIzrgV4AOOsBs0F%2FZ6frKs1FcX%2BJmk4m5jPN2p%2F4OzgM560JOaJM%2FpCr83%2FHz%2B8i9B2%2FBfTDZbRmoZTOUVbka%2BC5RNQ%2B1S7ZuzN9%2F73jY43J50TQ%2BeRKkuhEFrNbvFYsnPNTKJPjd7FOmhTo8jqHCTb8HLOefSBjhMrEvwRyt65Q8jawGd4MZbZ4hXeUB%2BS%2FeZ%2F9MfVEeGD4TI79%2BLqIjrIvAunsSU0V0EOCtKA5nNJmMq9fLOxDrzZKp5F77R56whftlMUu35pD4bumFQq4uRpWN6hJJXGUh5moDVWq%2BwoDLMOCtZ4o3tRA46cVWJYQHOs40LCsKoW573cq%2BmGU0%2BHn1qlQlxJHCO0DN500WjdJ42OtdHWHzRoLLBIz8wEsf2W2tNDbLlqdt4LFCgurJXrGDswFyUZJ9nMALfPHD4fE5Uv03x%2Bic3rSC8fdRGxyoXZNGngsw85V%2BM0xl4eQ8PJYdEzDOHkQzXGj1XeSDD2%2BXl6MsSDAyV467JMNLF6rwGOqUB964Kb3wttKGoEeFLzH3aw51vppFOs5%2FIEWVu9HeWQF%2F6mfd8v1hJVIqm86CQ3LnfU5RYDEXCsu%2BnHSxtIpZWgleWVoBWsFcpYeNBDxIfy4DiUdKAsUQ3gx6WM4ZM3UXMixhkEZ4G4J2W0L637sN2o9gC%2BEDREWr3T6YkCWRN6ftbh1spjc%2FW%2Bg5BzLk3%2B2dZ4CQzi2wL4wL0CheWLDSLGJkeOzpZ&X-Amz-Signature=d6ccd2c3d6f08539950292d558ff11ee4730986d31f56d8bd936320b824744ea&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665B4WSL6J%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBoaMlOSvwc4TSNeDwxw7FPz90pfY6H56MAhszPw%2FMZ1AiEAsDUMMNqhgk%2BMD0VIaejX474cenSQne9oAcGiTvaODLkqiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM64DYQfgLWVl8sbayrcA4P8eG8E8%2F82w347bVTV0Hhd4I%2BwjYWGGR3%2FUEwdnRHr2W0baoKXgeRk%2BuolD8qx5VyTQVBZrykBVWA46Kt3F1ROMnGnBcLizHumiCHLfsne%2F73kEatsy%2BXxcgKzJ4O7s3dIzrgV4AOOsBs0F%2FZ6frKs1FcX%2BJmk4m5jPN2p%2F4OzgM560JOaJM%2FpCr83%2FHz%2B8i9B2%2FBfTDZbRmoZTOUVbka%2BC5RNQ%2B1S7ZuzN9%2F73jY43J50TQ%2BeRKkuhEFrNbvFYsnPNTKJPjd7FOmhTo8jqHCTb8HLOefSBjhMrEvwRyt65Q8jawGd4MZbZ4hXeUB%2BS%2FeZ%2F9MfVEeGD4TI79%2BLqIjrIvAunsSU0V0EOCtKA5nNJmMq9fLOxDrzZKp5F77R56whftlMUu35pD4bumFQq4uRpWN6hJJXGUh5moDVWq%2BwoDLMOCtZ4o3tRA46cVWJYQHOs40LCsKoW573cq%2BmGU0%2BHn1qlQlxJHCO0DN500WjdJ42OtdHWHzRoLLBIz8wEsf2W2tNDbLlqdt4LFCgurJXrGDswFyUZJ9nMALfPHD4fE5Uv03x%2Bic3rSC8fdRGxyoXZNGngsw85V%2BM0xl4eQ8PJYdEzDOHkQzXGj1XeSDD2%2BXl6MsSDAyV467JMNLF6rwGOqUB964Kb3wttKGoEeFLzH3aw51vppFOs5%2FIEWVu9HeWQF%2F6mfd8v1hJVIqm86CQ3LnfU5RYDEXCsu%2BnHSxtIpZWgleWVoBWsFcpYeNBDxIfy4DiUdKAsUQ3gx6WM4ZM3UXMixhkEZ4G4J2W0L637sN2o9gC%2BEDREWr3T6YkCWRN6ftbh1spjc%2FW%2Bg5BzLk3%2B2dZ4CQzi2wL4wL0CheWLDSLGJkeOzpZ&X-Amz-Signature=738b9b3072d447ee0170894ca0d78bae3d8fff77f57ec8301de4ba4e9765ea1f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665B4WSL6J%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBoaMlOSvwc4TSNeDwxw7FPz90pfY6H56MAhszPw%2FMZ1AiEAsDUMMNqhgk%2BMD0VIaejX474cenSQne9oAcGiTvaODLkqiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM64DYQfgLWVl8sbayrcA4P8eG8E8%2F82w347bVTV0Hhd4I%2BwjYWGGR3%2FUEwdnRHr2W0baoKXgeRk%2BuolD8qx5VyTQVBZrykBVWA46Kt3F1ROMnGnBcLizHumiCHLfsne%2F73kEatsy%2BXxcgKzJ4O7s3dIzrgV4AOOsBs0F%2FZ6frKs1FcX%2BJmk4m5jPN2p%2F4OzgM560JOaJM%2FpCr83%2FHz%2B8i9B2%2FBfTDZbRmoZTOUVbka%2BC5RNQ%2B1S7ZuzN9%2F73jY43J50TQ%2BeRKkuhEFrNbvFYsnPNTKJPjd7FOmhTo8jqHCTb8HLOefSBjhMrEvwRyt65Q8jawGd4MZbZ4hXeUB%2BS%2FeZ%2F9MfVEeGD4TI79%2BLqIjrIvAunsSU0V0EOCtKA5nNJmMq9fLOxDrzZKp5F77R56whftlMUu35pD4bumFQq4uRpWN6hJJXGUh5moDVWq%2BwoDLMOCtZ4o3tRA46cVWJYQHOs40LCsKoW573cq%2BmGU0%2BHn1qlQlxJHCO0DN500WjdJ42OtdHWHzRoLLBIz8wEsf2W2tNDbLlqdt4LFCgurJXrGDswFyUZJ9nMALfPHD4fE5Uv03x%2Bic3rSC8fdRGxyoXZNGngsw85V%2BM0xl4eQ8PJYdEzDOHkQzXGj1XeSDD2%2BXl6MsSDAyV467JMNLF6rwGOqUB964Kb3wttKGoEeFLzH3aw51vppFOs5%2FIEWVu9HeWQF%2F6mfd8v1hJVIqm86CQ3LnfU5RYDEXCsu%2BnHSxtIpZWgleWVoBWsFcpYeNBDxIfy4DiUdKAsUQ3gx6WM4ZM3UXMixhkEZ4G4J2W0L637sN2o9gC%2BEDREWr3T6YkCWRN6ftbh1spjc%2FW%2Bg5BzLk3%2B2dZ4CQzi2wL4wL0CheWLDSLGJkeOzpZ&X-Amz-Signature=8660985aac35cbf96624ea8c802955b43dc08fe7a98c75bdecce5e8039e691a0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665B4WSL6J%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBoaMlOSvwc4TSNeDwxw7FPz90pfY6H56MAhszPw%2FMZ1AiEAsDUMMNqhgk%2BMD0VIaejX474cenSQne9oAcGiTvaODLkqiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM64DYQfgLWVl8sbayrcA4P8eG8E8%2F82w347bVTV0Hhd4I%2BwjYWGGR3%2FUEwdnRHr2W0baoKXgeRk%2BuolD8qx5VyTQVBZrykBVWA46Kt3F1ROMnGnBcLizHumiCHLfsne%2F73kEatsy%2BXxcgKzJ4O7s3dIzrgV4AOOsBs0F%2FZ6frKs1FcX%2BJmk4m5jPN2p%2F4OzgM560JOaJM%2FpCr83%2FHz%2B8i9B2%2FBfTDZbRmoZTOUVbka%2BC5RNQ%2B1S7ZuzN9%2F73jY43J50TQ%2BeRKkuhEFrNbvFYsnPNTKJPjd7FOmhTo8jqHCTb8HLOefSBjhMrEvwRyt65Q8jawGd4MZbZ4hXeUB%2BS%2FeZ%2F9MfVEeGD4TI79%2BLqIjrIvAunsSU0V0EOCtKA5nNJmMq9fLOxDrzZKp5F77R56whftlMUu35pD4bumFQq4uRpWN6hJJXGUh5moDVWq%2BwoDLMOCtZ4o3tRA46cVWJYQHOs40LCsKoW573cq%2BmGU0%2BHn1qlQlxJHCO0DN500WjdJ42OtdHWHzRoLLBIz8wEsf2W2tNDbLlqdt4LFCgurJXrGDswFyUZJ9nMALfPHD4fE5Uv03x%2Bic3rSC8fdRGxyoXZNGngsw85V%2BM0xl4eQ8PJYdEzDOHkQzXGj1XeSDD2%2BXl6MsSDAyV467JMNLF6rwGOqUB964Kb3wttKGoEeFLzH3aw51vppFOs5%2FIEWVu9HeWQF%2F6mfd8v1hJVIqm86CQ3LnfU5RYDEXCsu%2BnHSxtIpZWgleWVoBWsFcpYeNBDxIfy4DiUdKAsUQ3gx6WM4ZM3UXMixhkEZ4G4J2W0L637sN2o9gC%2BEDREWr3T6YkCWRN6ftbh1spjc%2FW%2Bg5BzLk3%2B2dZ4CQzi2wL4wL0CheWLDSLGJkeOzpZ&X-Amz-Signature=d52bc06c7e6b83478356e63adff45de8d9342f932a209bacf13469f614e7ae09&X-Amz-SignedHeaders=host&x-id=GetObject)
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


