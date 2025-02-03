

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XFDDIYRD%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031918Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCC0j%2BtXtiqJbvxH4Rwn54IvmQEo8l2u7CDHBtjWTPJ7wIgJySwKkktk0K2P6Bln6%2BQlnooPjkPnVFCX9N8UhQyPDYqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFO74zVfEJ1oNmxrHircA1usx6GqRQMXvl82f60RLt63UfFsrdrhBA5y7LuwoD7Z9jrH7%2Bv3YE5Jiv0oF7E5%2F%2BPJfmQ8EDM3lOWg7RFYqmlFpBRIhHBpn0%2F7Ab%2B%2BsVFqnuzroBa23fsPzEKL20LdBqZhNzhNZdPt3lkyLFqAHSOUeNA4CtJRh1hhpY9Yw66JUzIL5gMq7nHKJL3Wq7GRrAVXGaP8mWZWl9cQJ3w8mcFuomBWLXmzsMOBqfvFHzMmL%2BMYPQGh7BDIVv%2FK9ymW3xkvFfvNcvtFf%2FbX4cFJgM2OtdpsmYjaT2%2BktNzEk0UhRybayhuZ%2Byv%2FE47c28oxfRgiU9QcDRxxSh4dTRycINYEyK80SJrlEcS8EAr69LD9vVz%2FyS1anyoGgSZ3IwoWsuoc2jhbLUgWYaSjhE%2F%2BJBgM3lp2azjQtjDmWg8xke%2BAegGy4FswGNt2l5L7ViEBQYdubDrOyruMbR9qjalDRNlXoWrlcYyfbwi%2BftZDmHyPL2giy9WHnvfv7soCgdhJYHlIV%2B6c0%2FX%2FRYVucbJFW35KWCmnfnXiVNOaOKb1kYalxAyxcu%2F18Lgiv%2B4cEfBEBQxwZ3JmrYK39AER4Jw67JYhS2tlgD3EBkOpJqL9xlzqWO3qdAWzGhHdncABML3AgL0GOqUB1ZJjpNu%2Fq3bfFlvI7eCnVUwPaM6suo0zc%2B84Scn30rdTi1q9LQihPw8d0uHdvP2zJSO85yYyP%2BAb5gIsqclJH8weAwrw94wbdNd4A4VbKIc6%2Bbc2qBzDWCNW1DEtlYpeUyRwuqJG%2BqUnCU1NiKsOkIwHeEXsJZh7ns%2BWsQMdkKzD%2BrxNvqPmrve2NnoXuBdRt4ekjMKmgoRmiUthQIsO%2BeJChTA9&X-Amz-Signature=0e93fff7a82bf3643b267477880a50e0bc160b84f8de6a1fddbe6521cd515b10&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZMOCMQXF%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031919Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC39%2BbfvoqSobyIckClHkhTONhyObVxZZMJG36Pz5571gIgHgyeeB75qj2CSffMWYpiLrYz59uanTF3NQ6U3QG%2BVNMqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGAZhnDyaxes5QwzuyrcA%2FGo51XftCguHd4sCPIU7thH617040J4M65l4yg8C1u3TVVxxPPATMrCKpmqPNVLxRmXZtZkmK3M0CT9q1NH84kIOrWx%2FkLW5BJahuJ5AHkGMWQ08nTuwHAVy8BIcHfe77yVPtK6nGJpBlIy3xhcOHtPPoR7Kiy1sUovND%2F%2FPjqyj2%2F06Sf4YJUpI%2FvqBqRiPxBFWsrz15G932phVuuWLcRyJeNHUhMQQ7FVigw8OJjdFoLboNuvW9u1RnMvKKX0A1E3Wh5DPlKrya5eOUJi%2FvhuBPGcZUtuoP%2FKc9DcwoJzzCgv8Wg4IUvOOANr8Ns5oKeF5%2Bd4lM9lz7u5u5YMHpYbxD8%2BKxVQq%2BgOTG4BlWqfpAajyJI6bJfwnxA4WGrbyj0njVLZGcLBnuXcROgoE2HPhqYl5wkYRGx3APUOTRvpk2yHaRi8kAmMUw6pdldZeaSeyhyRGl8n6AktlohfKQlzJUwdfApXBbDbTsRDAu27p8iQxcla5U0bspi6utvlI%2Fg9Kb77wDmAnZzZs4lJfZbuD5Cfay2kpv5eW3i6ybrUGb489zwg8jlB5xOy8jjM9Krm88lTujKOjXXae7PfT2kO6FnGDAti02UyNHupwO2Nwemkgn1du0dPxrYZMMu%2FgL0GOqUBwSN1L%2FdqUAv03lvj2KtT3j%2BlnWHfk9yF8OSe62nfT%2FnokyUd36gi1StVpQB9bgOufD0msVCad2IaTso5JNUa8CFp9ngCMHjM09OfzAvorLa3gykwtAGv0ji0jlPBW%2BDIllx1kx03K6xxiwYLFPvhMbE%2BWo1%2FvYqZos%2Bs1RNzM1fJHv0TNehdHy7yNCnLxo9ti4U%2BAgqXAGAW0z2qPzZgMrtzCsin&X-Amz-Signature=d83e09b1e3cfcfc56035813212c029349b4d9df91fdbe11d423573383bdf5850&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZMOCMQXF%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031919Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC39%2BbfvoqSobyIckClHkhTONhyObVxZZMJG36Pz5571gIgHgyeeB75qj2CSffMWYpiLrYz59uanTF3NQ6U3QG%2BVNMqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGAZhnDyaxes5QwzuyrcA%2FGo51XftCguHd4sCPIU7thH617040J4M65l4yg8C1u3TVVxxPPATMrCKpmqPNVLxRmXZtZkmK3M0CT9q1NH84kIOrWx%2FkLW5BJahuJ5AHkGMWQ08nTuwHAVy8BIcHfe77yVPtK6nGJpBlIy3xhcOHtPPoR7Kiy1sUovND%2F%2FPjqyj2%2F06Sf4YJUpI%2FvqBqRiPxBFWsrz15G932phVuuWLcRyJeNHUhMQQ7FVigw8OJjdFoLboNuvW9u1RnMvKKX0A1E3Wh5DPlKrya5eOUJi%2FvhuBPGcZUtuoP%2FKc9DcwoJzzCgv8Wg4IUvOOANr8Ns5oKeF5%2Bd4lM9lz7u5u5YMHpYbxD8%2BKxVQq%2BgOTG4BlWqfpAajyJI6bJfwnxA4WGrbyj0njVLZGcLBnuXcROgoE2HPhqYl5wkYRGx3APUOTRvpk2yHaRi8kAmMUw6pdldZeaSeyhyRGl8n6AktlohfKQlzJUwdfApXBbDbTsRDAu27p8iQxcla5U0bspi6utvlI%2Fg9Kb77wDmAnZzZs4lJfZbuD5Cfay2kpv5eW3i6ybrUGb489zwg8jlB5xOy8jjM9Krm88lTujKOjXXae7PfT2kO6FnGDAti02UyNHupwO2Nwemkgn1du0dPxrYZMMu%2FgL0GOqUBwSN1L%2FdqUAv03lvj2KtT3j%2BlnWHfk9yF8OSe62nfT%2FnokyUd36gi1StVpQB9bgOufD0msVCad2IaTso5JNUa8CFp9ngCMHjM09OfzAvorLa3gykwtAGv0ji0jlPBW%2BDIllx1kx03K6xxiwYLFPvhMbE%2BWo1%2FvYqZos%2Bs1RNzM1fJHv0TNehdHy7yNCnLxo9ti4U%2BAgqXAGAW0z2qPzZgMrtzCsin&X-Amz-Signature=3d50cfef37d1550e2f17b33b05d85001ea385950781d2763999dcb848b06a9e2&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZMOCMQXF%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031919Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC39%2BbfvoqSobyIckClHkhTONhyObVxZZMJG36Pz5571gIgHgyeeB75qj2CSffMWYpiLrYz59uanTF3NQ6U3QG%2BVNMqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGAZhnDyaxes5QwzuyrcA%2FGo51XftCguHd4sCPIU7thH617040J4M65l4yg8C1u3TVVxxPPATMrCKpmqPNVLxRmXZtZkmK3M0CT9q1NH84kIOrWx%2FkLW5BJahuJ5AHkGMWQ08nTuwHAVy8BIcHfe77yVPtK6nGJpBlIy3xhcOHtPPoR7Kiy1sUovND%2F%2FPjqyj2%2F06Sf4YJUpI%2FvqBqRiPxBFWsrz15G932phVuuWLcRyJeNHUhMQQ7FVigw8OJjdFoLboNuvW9u1RnMvKKX0A1E3Wh5DPlKrya5eOUJi%2FvhuBPGcZUtuoP%2FKc9DcwoJzzCgv8Wg4IUvOOANr8Ns5oKeF5%2Bd4lM9lz7u5u5YMHpYbxD8%2BKxVQq%2BgOTG4BlWqfpAajyJI6bJfwnxA4WGrbyj0njVLZGcLBnuXcROgoE2HPhqYl5wkYRGx3APUOTRvpk2yHaRi8kAmMUw6pdldZeaSeyhyRGl8n6AktlohfKQlzJUwdfApXBbDbTsRDAu27p8iQxcla5U0bspi6utvlI%2Fg9Kb77wDmAnZzZs4lJfZbuD5Cfay2kpv5eW3i6ybrUGb489zwg8jlB5xOy8jjM9Krm88lTujKOjXXae7PfT2kO6FnGDAti02UyNHupwO2Nwemkgn1du0dPxrYZMMu%2FgL0GOqUBwSN1L%2FdqUAv03lvj2KtT3j%2BlnWHfk9yF8OSe62nfT%2FnokyUd36gi1StVpQB9bgOufD0msVCad2IaTso5JNUa8CFp9ngCMHjM09OfzAvorLa3gykwtAGv0ji0jlPBW%2BDIllx1kx03K6xxiwYLFPvhMbE%2BWo1%2FvYqZos%2Bs1RNzM1fJHv0TNehdHy7yNCnLxo9ti4U%2BAgqXAGAW0z2qPzZgMrtzCsin&X-Amz-Signature=2c486a13c28521756a026998ff7460b8c43bc392ac22e78a1695da6f4cda1332&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZMOCMQXF%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031919Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC39%2BbfvoqSobyIckClHkhTONhyObVxZZMJG36Pz5571gIgHgyeeB75qj2CSffMWYpiLrYz59uanTF3NQ6U3QG%2BVNMqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGAZhnDyaxes5QwzuyrcA%2FGo51XftCguHd4sCPIU7thH617040J4M65l4yg8C1u3TVVxxPPATMrCKpmqPNVLxRmXZtZkmK3M0CT9q1NH84kIOrWx%2FkLW5BJahuJ5AHkGMWQ08nTuwHAVy8BIcHfe77yVPtK6nGJpBlIy3xhcOHtPPoR7Kiy1sUovND%2F%2FPjqyj2%2F06Sf4YJUpI%2FvqBqRiPxBFWsrz15G932phVuuWLcRyJeNHUhMQQ7FVigw8OJjdFoLboNuvW9u1RnMvKKX0A1E3Wh5DPlKrya5eOUJi%2FvhuBPGcZUtuoP%2FKc9DcwoJzzCgv8Wg4IUvOOANr8Ns5oKeF5%2Bd4lM9lz7u5u5YMHpYbxD8%2BKxVQq%2BgOTG4BlWqfpAajyJI6bJfwnxA4WGrbyj0njVLZGcLBnuXcROgoE2HPhqYl5wkYRGx3APUOTRvpk2yHaRi8kAmMUw6pdldZeaSeyhyRGl8n6AktlohfKQlzJUwdfApXBbDbTsRDAu27p8iQxcla5U0bspi6utvlI%2Fg9Kb77wDmAnZzZs4lJfZbuD5Cfay2kpv5eW3i6ybrUGb489zwg8jlB5xOy8jjM9Krm88lTujKOjXXae7PfT2kO6FnGDAti02UyNHupwO2Nwemkgn1du0dPxrYZMMu%2FgL0GOqUBwSN1L%2FdqUAv03lvj2KtT3j%2BlnWHfk9yF8OSe62nfT%2FnokyUd36gi1StVpQB9bgOufD0msVCad2IaTso5JNUa8CFp9ngCMHjM09OfzAvorLa3gykwtAGv0ji0jlPBW%2BDIllx1kx03K6xxiwYLFPvhMbE%2BWo1%2FvYqZos%2Bs1RNzM1fJHv0TNehdHy7yNCnLxo9ti4U%2BAgqXAGAW0z2qPzZgMrtzCsin&X-Amz-Signature=d8b03bac0ff66e2be6e2cbcfe088ef391d31f9aeb63fb8ba2f470add0e145040&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZMOCMQXF%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031919Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC39%2BbfvoqSobyIckClHkhTONhyObVxZZMJG36Pz5571gIgHgyeeB75qj2CSffMWYpiLrYz59uanTF3NQ6U3QG%2BVNMqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGAZhnDyaxes5QwzuyrcA%2FGo51XftCguHd4sCPIU7thH617040J4M65l4yg8C1u3TVVxxPPATMrCKpmqPNVLxRmXZtZkmK3M0CT9q1NH84kIOrWx%2FkLW5BJahuJ5AHkGMWQ08nTuwHAVy8BIcHfe77yVPtK6nGJpBlIy3xhcOHtPPoR7Kiy1sUovND%2F%2FPjqyj2%2F06Sf4YJUpI%2FvqBqRiPxBFWsrz15G932phVuuWLcRyJeNHUhMQQ7FVigw8OJjdFoLboNuvW9u1RnMvKKX0A1E3Wh5DPlKrya5eOUJi%2FvhuBPGcZUtuoP%2FKc9DcwoJzzCgv8Wg4IUvOOANr8Ns5oKeF5%2Bd4lM9lz7u5u5YMHpYbxD8%2BKxVQq%2BgOTG4BlWqfpAajyJI6bJfwnxA4WGrbyj0njVLZGcLBnuXcROgoE2HPhqYl5wkYRGx3APUOTRvpk2yHaRi8kAmMUw6pdldZeaSeyhyRGl8n6AktlohfKQlzJUwdfApXBbDbTsRDAu27p8iQxcla5U0bspi6utvlI%2Fg9Kb77wDmAnZzZs4lJfZbuD5Cfay2kpv5eW3i6ybrUGb489zwg8jlB5xOy8jjM9Krm88lTujKOjXXae7PfT2kO6FnGDAti02UyNHupwO2Nwemkgn1du0dPxrYZMMu%2FgL0GOqUBwSN1L%2FdqUAv03lvj2KtT3j%2BlnWHfk9yF8OSe62nfT%2FnokyUd36gi1StVpQB9bgOufD0msVCad2IaTso5JNUa8CFp9ngCMHjM09OfzAvorLa3gykwtAGv0ji0jlPBW%2BDIllx1kx03K6xxiwYLFPvhMbE%2BWo1%2FvYqZos%2Bs1RNzM1fJHv0TNehdHy7yNCnLxo9ti4U%2BAgqXAGAW0z2qPzZgMrtzCsin&X-Amz-Signature=2be18e781171078c1082a579528dd7214e9d3ed34ed2925db5b849ea21523e29&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XFDDIYRD%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031918Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCC0j%2BtXtiqJbvxH4Rwn54IvmQEo8l2u7CDHBtjWTPJ7wIgJySwKkktk0K2P6Bln6%2BQlnooPjkPnVFCX9N8UhQyPDYqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFO74zVfEJ1oNmxrHircA1usx6GqRQMXvl82f60RLt63UfFsrdrhBA5y7LuwoD7Z9jrH7%2Bv3YE5Jiv0oF7E5%2F%2BPJfmQ8EDM3lOWg7RFYqmlFpBRIhHBpn0%2F7Ab%2B%2BsVFqnuzroBa23fsPzEKL20LdBqZhNzhNZdPt3lkyLFqAHSOUeNA4CtJRh1hhpY9Yw66JUzIL5gMq7nHKJL3Wq7GRrAVXGaP8mWZWl9cQJ3w8mcFuomBWLXmzsMOBqfvFHzMmL%2BMYPQGh7BDIVv%2FK9ymW3xkvFfvNcvtFf%2FbX4cFJgM2OtdpsmYjaT2%2BktNzEk0UhRybayhuZ%2Byv%2FE47c28oxfRgiU9QcDRxxSh4dTRycINYEyK80SJrlEcS8EAr69LD9vVz%2FyS1anyoGgSZ3IwoWsuoc2jhbLUgWYaSjhE%2F%2BJBgM3lp2azjQtjDmWg8xke%2BAegGy4FswGNt2l5L7ViEBQYdubDrOyruMbR9qjalDRNlXoWrlcYyfbwi%2BftZDmHyPL2giy9WHnvfv7soCgdhJYHlIV%2B6c0%2FX%2FRYVucbJFW35KWCmnfnXiVNOaOKb1kYalxAyxcu%2F18Lgiv%2B4cEfBEBQxwZ3JmrYK39AER4Jw67JYhS2tlgD3EBkOpJqL9xlzqWO3qdAWzGhHdncABML3AgL0GOqUB1ZJjpNu%2Fq3bfFlvI7eCnVUwPaM6suo0zc%2B84Scn30rdTi1q9LQihPw8d0uHdvP2zJSO85yYyP%2BAb5gIsqclJH8weAwrw94wbdNd4A4VbKIc6%2Bbc2qBzDWCNW1DEtlYpeUyRwuqJG%2BqUnCU1NiKsOkIwHeEXsJZh7ns%2BWsQMdkKzD%2BrxNvqPmrve2NnoXuBdRt4ekjMKmgoRmiUthQIsO%2BeJChTA9&X-Amz-Signature=623b86e8b0f9ca5460283e233ea0c5f8ccbb69bdaf75215d8d42e3adfdcf71c1&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XFDDIYRD%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031918Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCC0j%2BtXtiqJbvxH4Rwn54IvmQEo8l2u7CDHBtjWTPJ7wIgJySwKkktk0K2P6Bln6%2BQlnooPjkPnVFCX9N8UhQyPDYqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFO74zVfEJ1oNmxrHircA1usx6GqRQMXvl82f60RLt63UfFsrdrhBA5y7LuwoD7Z9jrH7%2Bv3YE5Jiv0oF7E5%2F%2BPJfmQ8EDM3lOWg7RFYqmlFpBRIhHBpn0%2F7Ab%2B%2BsVFqnuzroBa23fsPzEKL20LdBqZhNzhNZdPt3lkyLFqAHSOUeNA4CtJRh1hhpY9Yw66JUzIL5gMq7nHKJL3Wq7GRrAVXGaP8mWZWl9cQJ3w8mcFuomBWLXmzsMOBqfvFHzMmL%2BMYPQGh7BDIVv%2FK9ymW3xkvFfvNcvtFf%2FbX4cFJgM2OtdpsmYjaT2%2BktNzEk0UhRybayhuZ%2Byv%2FE47c28oxfRgiU9QcDRxxSh4dTRycINYEyK80SJrlEcS8EAr69LD9vVz%2FyS1anyoGgSZ3IwoWsuoc2jhbLUgWYaSjhE%2F%2BJBgM3lp2azjQtjDmWg8xke%2BAegGy4FswGNt2l5L7ViEBQYdubDrOyruMbR9qjalDRNlXoWrlcYyfbwi%2BftZDmHyPL2giy9WHnvfv7soCgdhJYHlIV%2B6c0%2FX%2FRYVucbJFW35KWCmnfnXiVNOaOKb1kYalxAyxcu%2F18Lgiv%2B4cEfBEBQxwZ3JmrYK39AER4Jw67JYhS2tlgD3EBkOpJqL9xlzqWO3qdAWzGhHdncABML3AgL0GOqUB1ZJjpNu%2Fq3bfFlvI7eCnVUwPaM6suo0zc%2B84Scn30rdTi1q9LQihPw8d0uHdvP2zJSO85yYyP%2BAb5gIsqclJH8weAwrw94wbdNd4A4VbKIc6%2Bbc2qBzDWCNW1DEtlYpeUyRwuqJG%2BqUnCU1NiKsOkIwHeEXsJZh7ns%2BWsQMdkKzD%2BrxNvqPmrve2NnoXuBdRt4ekjMKmgoRmiUthQIsO%2BeJChTA9&X-Amz-Signature=abdab332bea9c0218afd4a42684000aac58a157c3303a965efb0a60cc2bb2115&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XFDDIYRD%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031918Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCC0j%2BtXtiqJbvxH4Rwn54IvmQEo8l2u7CDHBtjWTPJ7wIgJySwKkktk0K2P6Bln6%2BQlnooPjkPnVFCX9N8UhQyPDYqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFO74zVfEJ1oNmxrHircA1usx6GqRQMXvl82f60RLt63UfFsrdrhBA5y7LuwoD7Z9jrH7%2Bv3YE5Jiv0oF7E5%2F%2BPJfmQ8EDM3lOWg7RFYqmlFpBRIhHBpn0%2F7Ab%2B%2BsVFqnuzroBa23fsPzEKL20LdBqZhNzhNZdPt3lkyLFqAHSOUeNA4CtJRh1hhpY9Yw66JUzIL5gMq7nHKJL3Wq7GRrAVXGaP8mWZWl9cQJ3w8mcFuomBWLXmzsMOBqfvFHzMmL%2BMYPQGh7BDIVv%2FK9ymW3xkvFfvNcvtFf%2FbX4cFJgM2OtdpsmYjaT2%2BktNzEk0UhRybayhuZ%2Byv%2FE47c28oxfRgiU9QcDRxxSh4dTRycINYEyK80SJrlEcS8EAr69LD9vVz%2FyS1anyoGgSZ3IwoWsuoc2jhbLUgWYaSjhE%2F%2BJBgM3lp2azjQtjDmWg8xke%2BAegGy4FswGNt2l5L7ViEBQYdubDrOyruMbR9qjalDRNlXoWrlcYyfbwi%2BftZDmHyPL2giy9WHnvfv7soCgdhJYHlIV%2B6c0%2FX%2FRYVucbJFW35KWCmnfnXiVNOaOKb1kYalxAyxcu%2F18Lgiv%2B4cEfBEBQxwZ3JmrYK39AER4Jw67JYhS2tlgD3EBkOpJqL9xlzqWO3qdAWzGhHdncABML3AgL0GOqUB1ZJjpNu%2Fq3bfFlvI7eCnVUwPaM6suo0zc%2B84Scn30rdTi1q9LQihPw8d0uHdvP2zJSO85yYyP%2BAb5gIsqclJH8weAwrw94wbdNd4A4VbKIc6%2Bbc2qBzDWCNW1DEtlYpeUyRwuqJG%2BqUnCU1NiKsOkIwHeEXsJZh7ns%2BWsQMdkKzD%2BrxNvqPmrve2NnoXuBdRt4ekjMKmgoRmiUthQIsO%2BeJChTA9&X-Amz-Signature=3acff8eff680b3e508cf04450521aeda2276ce16f6f6e84d11883a6ba867c893&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XFDDIYRD%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031918Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCC0j%2BtXtiqJbvxH4Rwn54IvmQEo8l2u7CDHBtjWTPJ7wIgJySwKkktk0K2P6Bln6%2BQlnooPjkPnVFCX9N8UhQyPDYqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFO74zVfEJ1oNmxrHircA1usx6GqRQMXvl82f60RLt63UfFsrdrhBA5y7LuwoD7Z9jrH7%2Bv3YE5Jiv0oF7E5%2F%2BPJfmQ8EDM3lOWg7RFYqmlFpBRIhHBpn0%2F7Ab%2B%2BsVFqnuzroBa23fsPzEKL20LdBqZhNzhNZdPt3lkyLFqAHSOUeNA4CtJRh1hhpY9Yw66JUzIL5gMq7nHKJL3Wq7GRrAVXGaP8mWZWl9cQJ3w8mcFuomBWLXmzsMOBqfvFHzMmL%2BMYPQGh7BDIVv%2FK9ymW3xkvFfvNcvtFf%2FbX4cFJgM2OtdpsmYjaT2%2BktNzEk0UhRybayhuZ%2Byv%2FE47c28oxfRgiU9QcDRxxSh4dTRycINYEyK80SJrlEcS8EAr69LD9vVz%2FyS1anyoGgSZ3IwoWsuoc2jhbLUgWYaSjhE%2F%2BJBgM3lp2azjQtjDmWg8xke%2BAegGy4FswGNt2l5L7ViEBQYdubDrOyruMbR9qjalDRNlXoWrlcYyfbwi%2BftZDmHyPL2giy9WHnvfv7soCgdhJYHlIV%2B6c0%2FX%2FRYVucbJFW35KWCmnfnXiVNOaOKb1kYalxAyxcu%2F18Lgiv%2B4cEfBEBQxwZ3JmrYK39AER4Jw67JYhS2tlgD3EBkOpJqL9xlzqWO3qdAWzGhHdncABML3AgL0GOqUB1ZJjpNu%2Fq3bfFlvI7eCnVUwPaM6suo0zc%2B84Scn30rdTi1q9LQihPw8d0uHdvP2zJSO85yYyP%2BAb5gIsqclJH8weAwrw94wbdNd4A4VbKIc6%2Bbc2qBzDWCNW1DEtlYpeUyRwuqJG%2BqUnCU1NiKsOkIwHeEXsJZh7ns%2BWsQMdkKzD%2BrxNvqPmrve2NnoXuBdRt4ekjMKmgoRmiUthQIsO%2BeJChTA9&X-Amz-Signature=c3b95236a3b3c712a8cdc8eb9c310bc1fba50591044436f2f2dff1664834639f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XFDDIYRD%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031918Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCC0j%2BtXtiqJbvxH4Rwn54IvmQEo8l2u7CDHBtjWTPJ7wIgJySwKkktk0K2P6Bln6%2BQlnooPjkPnVFCX9N8UhQyPDYqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFO74zVfEJ1oNmxrHircA1usx6GqRQMXvl82f60RLt63UfFsrdrhBA5y7LuwoD7Z9jrH7%2Bv3YE5Jiv0oF7E5%2F%2BPJfmQ8EDM3lOWg7RFYqmlFpBRIhHBpn0%2F7Ab%2B%2BsVFqnuzroBa23fsPzEKL20LdBqZhNzhNZdPt3lkyLFqAHSOUeNA4CtJRh1hhpY9Yw66JUzIL5gMq7nHKJL3Wq7GRrAVXGaP8mWZWl9cQJ3w8mcFuomBWLXmzsMOBqfvFHzMmL%2BMYPQGh7BDIVv%2FK9ymW3xkvFfvNcvtFf%2FbX4cFJgM2OtdpsmYjaT2%2BktNzEk0UhRybayhuZ%2Byv%2FE47c28oxfRgiU9QcDRxxSh4dTRycINYEyK80SJrlEcS8EAr69LD9vVz%2FyS1anyoGgSZ3IwoWsuoc2jhbLUgWYaSjhE%2F%2BJBgM3lp2azjQtjDmWg8xke%2BAegGy4FswGNt2l5L7ViEBQYdubDrOyruMbR9qjalDRNlXoWrlcYyfbwi%2BftZDmHyPL2giy9WHnvfv7soCgdhJYHlIV%2B6c0%2FX%2FRYVucbJFW35KWCmnfnXiVNOaOKb1kYalxAyxcu%2F18Lgiv%2B4cEfBEBQxwZ3JmrYK39AER4Jw67JYhS2tlgD3EBkOpJqL9xlzqWO3qdAWzGhHdncABML3AgL0GOqUB1ZJjpNu%2Fq3bfFlvI7eCnVUwPaM6suo0zc%2B84Scn30rdTi1q9LQihPw8d0uHdvP2zJSO85yYyP%2BAb5gIsqclJH8weAwrw94wbdNd4A4VbKIc6%2Bbc2qBzDWCNW1DEtlYpeUyRwuqJG%2BqUnCU1NiKsOkIwHeEXsJZh7ns%2BWsQMdkKzD%2BrxNvqPmrve2NnoXuBdRt4ekjMKmgoRmiUthQIsO%2BeJChTA9&X-Amz-Signature=d85e9437f7721d9ec4547ba2fb5eff1c74eb94f70be1056f6a406a87133f69f9&X-Amz-SignedHeaders=host&x-id=GetObject)
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


