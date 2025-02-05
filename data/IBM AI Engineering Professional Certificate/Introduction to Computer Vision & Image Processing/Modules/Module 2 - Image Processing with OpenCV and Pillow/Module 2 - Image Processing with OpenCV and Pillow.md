

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UI4TDWOX%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151558Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJGMEQCIEZ2OQbsfQkwkxHKGS22iPnAYXxCRRUGpChpnVQHebQgAiA%2BrHKk9P0GnMjHMhpntOVnaP54C25HQ5nFYrziJLsw9Cr%2FAwhHEAAaDDYzNzQyMzE4MzgwNSIMWRCRyRaIijK6f69BKtwDgQvVWwSf%2BKoRNriO8780ZJDL5NOLxAd8GphLcF%2B3Tv%2F%2FQWG7L0DjA%2BL9Kem%2F6qAu6kb4ZgopZPpO2VFBlBISFUAHTr5jumQ1k5dJSWcI%2BrRZAJBdAJUF0Lb0vGvbUaLDuKwu4FbqW7I8XNPfVbBc6Kfl7TEm5RH0GRYJa%2Bc0z93G24C5A0MoMoAHWD1CsExTZL5fbwAPS5tWp0fkHBbQyZosHiF3%2FE8O8Ab13FUn8Rp6zxUPf%2BXiBr1G2WL3ueyhkZh%2FqMwH9QkrTn655Qbwl3nvR2NTS5ZopMwrsUv7%2FwMWu9hVjOG8ZLRxamhZLPwfh8g%2B9a40bNbFGG45rEcfcnHy3Wf1sO6Fgq0lJLFG0gNTDIWNswZLAOckXNykZGlK%2BMLdpu%2FHDhVARSU8OxApbVme%2BQMqRadIhZb4UbIn8JZpaHYHmjRvaQteG%2BPhr6gUtyYmG%2FM8Kc5GXFkcZAeXG0iFgGULSP4KgI5NX2%2BOFAZ%2BWlA%2BWpnvFOelb8%2BRQk9t0b7qBpZT%2F0KU7tdcKXMU4vX0Bknr9PvY%2BbhYuL9wnUQ6fOVpS768xqiyzMXYkHGpnXJT57BsVPPQLl34qES9m%2FkwQkn6jMn7%2Ba1%2FOevq95jwohI%2FKrwkBw0sCHUwkuSNvQY6pgHY1zpsd8qez8s41ramFkcK3SbRGdmczybS0Yhw54ys4rdFDCgk1zL60riVvfs3ivr%2BAZ3RqESJxO7T%2FrWU4HypmqzXz%2B7r5cHzW3b%2BcQN%2FfxqcOxpAAcn%2B27u5lpCWtnvs5sByad0OzWET3s7pxYWFfYlUadJrhq6EP5K1wjU%2BMMKYMZnr6F7y1J9er%2BYLA2adPY1vQ5E21cr8olxjJx%2BLCXa1xFeZ&X-Amz-Signature=14bfcb72031ec1fd0e53e9754e217be03698c521e0297a2f632fbd40c1d17fc5&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46654HLWEKP%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJIMEYCIQDJcUiOJwjFwMjOzmpZeKb1E0jgJG6TAFSI0SV2VAn0WQIhANMyrvTjE1twyl4xizmnFBdcNdRdLvFKeBWTbjmrqUhMKv8DCEgQABoMNjM3NDIzMTgzODA1IgxsB9PjFolZYlBOTsYq3ANjmzP%2B%2Fxjn%2BnqwBIoWcvz4w82nZnEe4GGYv0v3Ft5XPobCjTAVVex7L4Objwl2I6h%2B8DhDgYzvVa3tW4ZkG7EdSJyV3uxIICA7J2HX1uWuYd8ecYrykcAP50C8FbCkHieizW9NETwCB6OQ5y%2BMkms74E2%2Baa4Ph3dJTeYbtftYzNnsqLIfswSi0ZyxpD5SFXDDLOhXXPcVaL0bEwNEM814oXjUCbRBxEfr9PwoucG2VPuEBLcdiY9vyaEKjLoHi6q%2BkoaO%2FFsvvbqxmo33uGG9xSUZO2fhIFA2clENBfI3Id66gSe6oDLBNX%2FbVP7uFHdPNFY2%2BqnRjkAbRg4TyyOwVwZNJyGrDek%2Bm6WeA8usMBSTiGS0IplgW1KSzIxSlFQITAUk4Sj4s5iOhOJkHVePmMDJKtk8ha2zJydM5vBmec49Zax%2BtpIqLuC9SF1COLXCqOsmZuGnvlxt%2BzCLkgUqUkcxsmGHFFYXFzsiMyXWKI4XGlMehyjchkSyDYfvy3HLUwVwtBj8hP8ZaNq0%2BRzaTVWN1kqkrwRhDiTU%2Bd92YkjpyJSjulk%2FErqxGYEIseItCGEpd7qySM9wDSGrjPP5Vfq3Rqz%2FHGcLAnd3TJ3TnZ9QpxykjHxXco7pyjC3gI69BjqkAZsIJrYx%2BZTWA400dNXFJMlMzIAXodyfpVw2Z4UHQ8r5euBp9v8xzo%2FNQYYVPmVV%2F89u8aA8RN7g1WXWRYbEUE0xhNe6w5kwOzSwt%2BIjb2ZVTepr3SS1HoQQOO65Q0%2FL3LxqkWJfdifG10mIxfmSmGdB%2BRzuPkYofcUdwT9NSj7bTIpnaTlGvAnJpbkE4iBo7nvifC6PkxVMolYny%2BgZwUWsFjBj&X-Amz-Signature=df9457120210b1abe960452f508e5de81f2f726e5ce767e674c933c3047ece9a&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46654HLWEKP%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJIMEYCIQDJcUiOJwjFwMjOzmpZeKb1E0jgJG6TAFSI0SV2VAn0WQIhANMyrvTjE1twyl4xizmnFBdcNdRdLvFKeBWTbjmrqUhMKv8DCEgQABoMNjM3NDIzMTgzODA1IgxsB9PjFolZYlBOTsYq3ANjmzP%2B%2Fxjn%2BnqwBIoWcvz4w82nZnEe4GGYv0v3Ft5XPobCjTAVVex7L4Objwl2I6h%2B8DhDgYzvVa3tW4ZkG7EdSJyV3uxIICA7J2HX1uWuYd8ecYrykcAP50C8FbCkHieizW9NETwCB6OQ5y%2BMkms74E2%2Baa4Ph3dJTeYbtftYzNnsqLIfswSi0ZyxpD5SFXDDLOhXXPcVaL0bEwNEM814oXjUCbRBxEfr9PwoucG2VPuEBLcdiY9vyaEKjLoHi6q%2BkoaO%2FFsvvbqxmo33uGG9xSUZO2fhIFA2clENBfI3Id66gSe6oDLBNX%2FbVP7uFHdPNFY2%2BqnRjkAbRg4TyyOwVwZNJyGrDek%2Bm6WeA8usMBSTiGS0IplgW1KSzIxSlFQITAUk4Sj4s5iOhOJkHVePmMDJKtk8ha2zJydM5vBmec49Zax%2BtpIqLuC9SF1COLXCqOsmZuGnvlxt%2BzCLkgUqUkcxsmGHFFYXFzsiMyXWKI4XGlMehyjchkSyDYfvy3HLUwVwtBj8hP8ZaNq0%2BRzaTVWN1kqkrwRhDiTU%2Bd92YkjpyJSjulk%2FErqxGYEIseItCGEpd7qySM9wDSGrjPP5Vfq3Rqz%2FHGcLAnd3TJ3TnZ9QpxykjHxXco7pyjC3gI69BjqkAZsIJrYx%2BZTWA400dNXFJMlMzIAXodyfpVw2Z4UHQ8r5euBp9v8xzo%2FNQYYVPmVV%2F89u8aA8RN7g1WXWRYbEUE0xhNe6w5kwOzSwt%2BIjb2ZVTepr3SS1HoQQOO65Q0%2FL3LxqkWJfdifG10mIxfmSmGdB%2BRzuPkYofcUdwT9NSj7bTIpnaTlGvAnJpbkE4iBo7nvifC6PkxVMolYny%2BgZwUWsFjBj&X-Amz-Signature=41f9e6e79c083f292d7065221f15d8aeddd30825ac93cbadd228bc02c39645d3&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46654HLWEKP%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJIMEYCIQDJcUiOJwjFwMjOzmpZeKb1E0jgJG6TAFSI0SV2VAn0WQIhANMyrvTjE1twyl4xizmnFBdcNdRdLvFKeBWTbjmrqUhMKv8DCEgQABoMNjM3NDIzMTgzODA1IgxsB9PjFolZYlBOTsYq3ANjmzP%2B%2Fxjn%2BnqwBIoWcvz4w82nZnEe4GGYv0v3Ft5XPobCjTAVVex7L4Objwl2I6h%2B8DhDgYzvVa3tW4ZkG7EdSJyV3uxIICA7J2HX1uWuYd8ecYrykcAP50C8FbCkHieizW9NETwCB6OQ5y%2BMkms74E2%2Baa4Ph3dJTeYbtftYzNnsqLIfswSi0ZyxpD5SFXDDLOhXXPcVaL0bEwNEM814oXjUCbRBxEfr9PwoucG2VPuEBLcdiY9vyaEKjLoHi6q%2BkoaO%2FFsvvbqxmo33uGG9xSUZO2fhIFA2clENBfI3Id66gSe6oDLBNX%2FbVP7uFHdPNFY2%2BqnRjkAbRg4TyyOwVwZNJyGrDek%2Bm6WeA8usMBSTiGS0IplgW1KSzIxSlFQITAUk4Sj4s5iOhOJkHVePmMDJKtk8ha2zJydM5vBmec49Zax%2BtpIqLuC9SF1COLXCqOsmZuGnvlxt%2BzCLkgUqUkcxsmGHFFYXFzsiMyXWKI4XGlMehyjchkSyDYfvy3HLUwVwtBj8hP8ZaNq0%2BRzaTVWN1kqkrwRhDiTU%2Bd92YkjpyJSjulk%2FErqxGYEIseItCGEpd7qySM9wDSGrjPP5Vfq3Rqz%2FHGcLAnd3TJ3TnZ9QpxykjHxXco7pyjC3gI69BjqkAZsIJrYx%2BZTWA400dNXFJMlMzIAXodyfpVw2Z4UHQ8r5euBp9v8xzo%2FNQYYVPmVV%2F89u8aA8RN7g1WXWRYbEUE0xhNe6w5kwOzSwt%2BIjb2ZVTepr3SS1HoQQOO65Q0%2FL3LxqkWJfdifG10mIxfmSmGdB%2BRzuPkYofcUdwT9NSj7bTIpnaTlGvAnJpbkE4iBo7nvifC6PkxVMolYny%2BgZwUWsFjBj&X-Amz-Signature=d4da7a7e3dd795063beb184b367253309c8d42320b8347f9bb187e6ea39ee4ed&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46654HLWEKP%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJIMEYCIQDJcUiOJwjFwMjOzmpZeKb1E0jgJG6TAFSI0SV2VAn0WQIhANMyrvTjE1twyl4xizmnFBdcNdRdLvFKeBWTbjmrqUhMKv8DCEgQABoMNjM3NDIzMTgzODA1IgxsB9PjFolZYlBOTsYq3ANjmzP%2B%2Fxjn%2BnqwBIoWcvz4w82nZnEe4GGYv0v3Ft5XPobCjTAVVex7L4Objwl2I6h%2B8DhDgYzvVa3tW4ZkG7EdSJyV3uxIICA7J2HX1uWuYd8ecYrykcAP50C8FbCkHieizW9NETwCB6OQ5y%2BMkms74E2%2Baa4Ph3dJTeYbtftYzNnsqLIfswSi0ZyxpD5SFXDDLOhXXPcVaL0bEwNEM814oXjUCbRBxEfr9PwoucG2VPuEBLcdiY9vyaEKjLoHi6q%2BkoaO%2FFsvvbqxmo33uGG9xSUZO2fhIFA2clENBfI3Id66gSe6oDLBNX%2FbVP7uFHdPNFY2%2BqnRjkAbRg4TyyOwVwZNJyGrDek%2Bm6WeA8usMBSTiGS0IplgW1KSzIxSlFQITAUk4Sj4s5iOhOJkHVePmMDJKtk8ha2zJydM5vBmec49Zax%2BtpIqLuC9SF1COLXCqOsmZuGnvlxt%2BzCLkgUqUkcxsmGHFFYXFzsiMyXWKI4XGlMehyjchkSyDYfvy3HLUwVwtBj8hP8ZaNq0%2BRzaTVWN1kqkrwRhDiTU%2Bd92YkjpyJSjulk%2FErqxGYEIseItCGEpd7qySM9wDSGrjPP5Vfq3Rqz%2FHGcLAnd3TJ3TnZ9QpxykjHxXco7pyjC3gI69BjqkAZsIJrYx%2BZTWA400dNXFJMlMzIAXodyfpVw2Z4UHQ8r5euBp9v8xzo%2FNQYYVPmVV%2F89u8aA8RN7g1WXWRYbEUE0xhNe6w5kwOzSwt%2BIjb2ZVTepr3SS1HoQQOO65Q0%2FL3LxqkWJfdifG10mIxfmSmGdB%2BRzuPkYofcUdwT9NSj7bTIpnaTlGvAnJpbkE4iBo7nvifC6PkxVMolYny%2BgZwUWsFjBj&X-Amz-Signature=f86c878217cc0359b25cb32617ab3f851d6e201463408f7f48dedc9b398c1e04&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46654HLWEKP%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJIMEYCIQDJcUiOJwjFwMjOzmpZeKb1E0jgJG6TAFSI0SV2VAn0WQIhANMyrvTjE1twyl4xizmnFBdcNdRdLvFKeBWTbjmrqUhMKv8DCEgQABoMNjM3NDIzMTgzODA1IgxsB9PjFolZYlBOTsYq3ANjmzP%2B%2Fxjn%2BnqwBIoWcvz4w82nZnEe4GGYv0v3Ft5XPobCjTAVVex7L4Objwl2I6h%2B8DhDgYzvVa3tW4ZkG7EdSJyV3uxIICA7J2HX1uWuYd8ecYrykcAP50C8FbCkHieizW9NETwCB6OQ5y%2BMkms74E2%2Baa4Ph3dJTeYbtftYzNnsqLIfswSi0ZyxpD5SFXDDLOhXXPcVaL0bEwNEM814oXjUCbRBxEfr9PwoucG2VPuEBLcdiY9vyaEKjLoHi6q%2BkoaO%2FFsvvbqxmo33uGG9xSUZO2fhIFA2clENBfI3Id66gSe6oDLBNX%2FbVP7uFHdPNFY2%2BqnRjkAbRg4TyyOwVwZNJyGrDek%2Bm6WeA8usMBSTiGS0IplgW1KSzIxSlFQITAUk4Sj4s5iOhOJkHVePmMDJKtk8ha2zJydM5vBmec49Zax%2BtpIqLuC9SF1COLXCqOsmZuGnvlxt%2BzCLkgUqUkcxsmGHFFYXFzsiMyXWKI4XGlMehyjchkSyDYfvy3HLUwVwtBj8hP8ZaNq0%2BRzaTVWN1kqkrwRhDiTU%2Bd92YkjpyJSjulk%2FErqxGYEIseItCGEpd7qySM9wDSGrjPP5Vfq3Rqz%2FHGcLAnd3TJ3TnZ9QpxykjHxXco7pyjC3gI69BjqkAZsIJrYx%2BZTWA400dNXFJMlMzIAXodyfpVw2Z4UHQ8r5euBp9v8xzo%2FNQYYVPmVV%2F89u8aA8RN7g1WXWRYbEUE0xhNe6w5kwOzSwt%2BIjb2ZVTepr3SS1HoQQOO65Q0%2FL3LxqkWJfdifG10mIxfmSmGdB%2BRzuPkYofcUdwT9NSj7bTIpnaTlGvAnJpbkE4iBo7nvifC6PkxVMolYny%2BgZwUWsFjBj&X-Amz-Signature=1ea171ea4c76271cdbb74d8db9c8d56ba13f0fb759627f54755e20bd59e05c2c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UI4TDWOX%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151558Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJGMEQCIEZ2OQbsfQkwkxHKGS22iPnAYXxCRRUGpChpnVQHebQgAiA%2BrHKk9P0GnMjHMhpntOVnaP54C25HQ5nFYrziJLsw9Cr%2FAwhHEAAaDDYzNzQyMzE4MzgwNSIMWRCRyRaIijK6f69BKtwDgQvVWwSf%2BKoRNriO8780ZJDL5NOLxAd8GphLcF%2B3Tv%2F%2FQWG7L0DjA%2BL9Kem%2F6qAu6kb4ZgopZPpO2VFBlBISFUAHTr5jumQ1k5dJSWcI%2BrRZAJBdAJUF0Lb0vGvbUaLDuKwu4FbqW7I8XNPfVbBc6Kfl7TEm5RH0GRYJa%2Bc0z93G24C5A0MoMoAHWD1CsExTZL5fbwAPS5tWp0fkHBbQyZosHiF3%2FE8O8Ab13FUn8Rp6zxUPf%2BXiBr1G2WL3ueyhkZh%2FqMwH9QkrTn655Qbwl3nvR2NTS5ZopMwrsUv7%2FwMWu9hVjOG8ZLRxamhZLPwfh8g%2B9a40bNbFGG45rEcfcnHy3Wf1sO6Fgq0lJLFG0gNTDIWNswZLAOckXNykZGlK%2BMLdpu%2FHDhVARSU8OxApbVme%2BQMqRadIhZb4UbIn8JZpaHYHmjRvaQteG%2BPhr6gUtyYmG%2FM8Kc5GXFkcZAeXG0iFgGULSP4KgI5NX2%2BOFAZ%2BWlA%2BWpnvFOelb8%2BRQk9t0b7qBpZT%2F0KU7tdcKXMU4vX0Bknr9PvY%2BbhYuL9wnUQ6fOVpS768xqiyzMXYkHGpnXJT57BsVPPQLl34qES9m%2FkwQkn6jMn7%2Ba1%2FOevq95jwohI%2FKrwkBw0sCHUwkuSNvQY6pgHY1zpsd8qez8s41ramFkcK3SbRGdmczybS0Yhw54ys4rdFDCgk1zL60riVvfs3ivr%2BAZ3RqESJxO7T%2FrWU4HypmqzXz%2B7r5cHzW3b%2BcQN%2FfxqcOxpAAcn%2B27u5lpCWtnvs5sByad0OzWET3s7pxYWFfYlUadJrhq6EP5K1wjU%2BMMKYMZnr6F7y1J9er%2BYLA2adPY1vQ5E21cr8olxjJx%2BLCXa1xFeZ&X-Amz-Signature=d781a36a94e42618a7700427ed6844ae112872c1e1e3aa01bfcd1af2cc249798&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UI4TDWOX%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJGMEQCIEZ2OQbsfQkwkxHKGS22iPnAYXxCRRUGpChpnVQHebQgAiA%2BrHKk9P0GnMjHMhpntOVnaP54C25HQ5nFYrziJLsw9Cr%2FAwhHEAAaDDYzNzQyMzE4MzgwNSIMWRCRyRaIijK6f69BKtwDgQvVWwSf%2BKoRNriO8780ZJDL5NOLxAd8GphLcF%2B3Tv%2F%2FQWG7L0DjA%2BL9Kem%2F6qAu6kb4ZgopZPpO2VFBlBISFUAHTr5jumQ1k5dJSWcI%2BrRZAJBdAJUF0Lb0vGvbUaLDuKwu4FbqW7I8XNPfVbBc6Kfl7TEm5RH0GRYJa%2Bc0z93G24C5A0MoMoAHWD1CsExTZL5fbwAPS5tWp0fkHBbQyZosHiF3%2FE8O8Ab13FUn8Rp6zxUPf%2BXiBr1G2WL3ueyhkZh%2FqMwH9QkrTn655Qbwl3nvR2NTS5ZopMwrsUv7%2FwMWu9hVjOG8ZLRxamhZLPwfh8g%2B9a40bNbFGG45rEcfcnHy3Wf1sO6Fgq0lJLFG0gNTDIWNswZLAOckXNykZGlK%2BMLdpu%2FHDhVARSU8OxApbVme%2BQMqRadIhZb4UbIn8JZpaHYHmjRvaQteG%2BPhr6gUtyYmG%2FM8Kc5GXFkcZAeXG0iFgGULSP4KgI5NX2%2BOFAZ%2BWlA%2BWpnvFOelb8%2BRQk9t0b7qBpZT%2F0KU7tdcKXMU4vX0Bknr9PvY%2BbhYuL9wnUQ6fOVpS768xqiyzMXYkHGpnXJT57BsVPPQLl34qES9m%2FkwQkn6jMn7%2Ba1%2FOevq95jwohI%2FKrwkBw0sCHUwkuSNvQY6pgHY1zpsd8qez8s41ramFkcK3SbRGdmczybS0Yhw54ys4rdFDCgk1zL60riVvfs3ivr%2BAZ3RqESJxO7T%2FrWU4HypmqzXz%2B7r5cHzW3b%2BcQN%2FfxqcOxpAAcn%2B27u5lpCWtnvs5sByad0OzWET3s7pxYWFfYlUadJrhq6EP5K1wjU%2BMMKYMZnr6F7y1J9er%2BYLA2adPY1vQ5E21cr8olxjJx%2BLCXa1xFeZ&X-Amz-Signature=4fb2a14c8231464f999719f189531fd5de8839148b88452ea07a0d8d54f9e290&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UI4TDWOX%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJGMEQCIEZ2OQbsfQkwkxHKGS22iPnAYXxCRRUGpChpnVQHebQgAiA%2BrHKk9P0GnMjHMhpntOVnaP54C25HQ5nFYrziJLsw9Cr%2FAwhHEAAaDDYzNzQyMzE4MzgwNSIMWRCRyRaIijK6f69BKtwDgQvVWwSf%2BKoRNriO8780ZJDL5NOLxAd8GphLcF%2B3Tv%2F%2FQWG7L0DjA%2BL9Kem%2F6qAu6kb4ZgopZPpO2VFBlBISFUAHTr5jumQ1k5dJSWcI%2BrRZAJBdAJUF0Lb0vGvbUaLDuKwu4FbqW7I8XNPfVbBc6Kfl7TEm5RH0GRYJa%2Bc0z93G24C5A0MoMoAHWD1CsExTZL5fbwAPS5tWp0fkHBbQyZosHiF3%2FE8O8Ab13FUn8Rp6zxUPf%2BXiBr1G2WL3ueyhkZh%2FqMwH9QkrTn655Qbwl3nvR2NTS5ZopMwrsUv7%2FwMWu9hVjOG8ZLRxamhZLPwfh8g%2B9a40bNbFGG45rEcfcnHy3Wf1sO6Fgq0lJLFG0gNTDIWNswZLAOckXNykZGlK%2BMLdpu%2FHDhVARSU8OxApbVme%2BQMqRadIhZb4UbIn8JZpaHYHmjRvaQteG%2BPhr6gUtyYmG%2FM8Kc5GXFkcZAeXG0iFgGULSP4KgI5NX2%2BOFAZ%2BWlA%2BWpnvFOelb8%2BRQk9t0b7qBpZT%2F0KU7tdcKXMU4vX0Bknr9PvY%2BbhYuL9wnUQ6fOVpS768xqiyzMXYkHGpnXJT57BsVPPQLl34qES9m%2FkwQkn6jMn7%2Ba1%2FOevq95jwohI%2FKrwkBw0sCHUwkuSNvQY6pgHY1zpsd8qez8s41ramFkcK3SbRGdmczybS0Yhw54ys4rdFDCgk1zL60riVvfs3ivr%2BAZ3RqESJxO7T%2FrWU4HypmqzXz%2B7r5cHzW3b%2BcQN%2FfxqcOxpAAcn%2B27u5lpCWtnvs5sByad0OzWET3s7pxYWFfYlUadJrhq6EP5K1wjU%2BMMKYMZnr6F7y1J9er%2BYLA2adPY1vQ5E21cr8olxjJx%2BLCXa1xFeZ&X-Amz-Signature=b539ff5fcaa145211ed1d1c37f6a69da7d71ee6670922e087afc01dfc50a4166&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UI4TDWOX%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJGMEQCIEZ2OQbsfQkwkxHKGS22iPnAYXxCRRUGpChpnVQHebQgAiA%2BrHKk9P0GnMjHMhpntOVnaP54C25HQ5nFYrziJLsw9Cr%2FAwhHEAAaDDYzNzQyMzE4MzgwNSIMWRCRyRaIijK6f69BKtwDgQvVWwSf%2BKoRNriO8780ZJDL5NOLxAd8GphLcF%2B3Tv%2F%2FQWG7L0DjA%2BL9Kem%2F6qAu6kb4ZgopZPpO2VFBlBISFUAHTr5jumQ1k5dJSWcI%2BrRZAJBdAJUF0Lb0vGvbUaLDuKwu4FbqW7I8XNPfVbBc6Kfl7TEm5RH0GRYJa%2Bc0z93G24C5A0MoMoAHWD1CsExTZL5fbwAPS5tWp0fkHBbQyZosHiF3%2FE8O8Ab13FUn8Rp6zxUPf%2BXiBr1G2WL3ueyhkZh%2FqMwH9QkrTn655Qbwl3nvR2NTS5ZopMwrsUv7%2FwMWu9hVjOG8ZLRxamhZLPwfh8g%2B9a40bNbFGG45rEcfcnHy3Wf1sO6Fgq0lJLFG0gNTDIWNswZLAOckXNykZGlK%2BMLdpu%2FHDhVARSU8OxApbVme%2BQMqRadIhZb4UbIn8JZpaHYHmjRvaQteG%2BPhr6gUtyYmG%2FM8Kc5GXFkcZAeXG0iFgGULSP4KgI5NX2%2BOFAZ%2BWlA%2BWpnvFOelb8%2BRQk9t0b7qBpZT%2F0KU7tdcKXMU4vX0Bknr9PvY%2BbhYuL9wnUQ6fOVpS768xqiyzMXYkHGpnXJT57BsVPPQLl34qES9m%2FkwQkn6jMn7%2Ba1%2FOevq95jwohI%2FKrwkBw0sCHUwkuSNvQY6pgHY1zpsd8qez8s41ramFkcK3SbRGdmczybS0Yhw54ys4rdFDCgk1zL60riVvfs3ivr%2BAZ3RqESJxO7T%2FrWU4HypmqzXz%2B7r5cHzW3b%2BcQN%2FfxqcOxpAAcn%2B27u5lpCWtnvs5sByad0OzWET3s7pxYWFfYlUadJrhq6EP5K1wjU%2BMMKYMZnr6F7y1J9er%2BYLA2adPY1vQ5E21cr8olxjJx%2BLCXa1xFeZ&X-Amz-Signature=7130046c80250541393e87370fa4811b3c63fcf44358cbda2f6d928dc07d6108&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UI4TDWOX%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJGMEQCIEZ2OQbsfQkwkxHKGS22iPnAYXxCRRUGpChpnVQHebQgAiA%2BrHKk9P0GnMjHMhpntOVnaP54C25HQ5nFYrziJLsw9Cr%2FAwhHEAAaDDYzNzQyMzE4MzgwNSIMWRCRyRaIijK6f69BKtwDgQvVWwSf%2BKoRNriO8780ZJDL5NOLxAd8GphLcF%2B3Tv%2F%2FQWG7L0DjA%2BL9Kem%2F6qAu6kb4ZgopZPpO2VFBlBISFUAHTr5jumQ1k5dJSWcI%2BrRZAJBdAJUF0Lb0vGvbUaLDuKwu4FbqW7I8XNPfVbBc6Kfl7TEm5RH0GRYJa%2Bc0z93G24C5A0MoMoAHWD1CsExTZL5fbwAPS5tWp0fkHBbQyZosHiF3%2FE8O8Ab13FUn8Rp6zxUPf%2BXiBr1G2WL3ueyhkZh%2FqMwH9QkrTn655Qbwl3nvR2NTS5ZopMwrsUv7%2FwMWu9hVjOG8ZLRxamhZLPwfh8g%2B9a40bNbFGG45rEcfcnHy3Wf1sO6Fgq0lJLFG0gNTDIWNswZLAOckXNykZGlK%2BMLdpu%2FHDhVARSU8OxApbVme%2BQMqRadIhZb4UbIn8JZpaHYHmjRvaQteG%2BPhr6gUtyYmG%2FM8Kc5GXFkcZAeXG0iFgGULSP4KgI5NX2%2BOFAZ%2BWlA%2BWpnvFOelb8%2BRQk9t0b7qBpZT%2F0KU7tdcKXMU4vX0Bknr9PvY%2BbhYuL9wnUQ6fOVpS768xqiyzMXYkHGpnXJT57BsVPPQLl34qES9m%2FkwQkn6jMn7%2Ba1%2FOevq95jwohI%2FKrwkBw0sCHUwkuSNvQY6pgHY1zpsd8qez8s41ramFkcK3SbRGdmczybS0Yhw54ys4rdFDCgk1zL60riVvfs3ivr%2BAZ3RqESJxO7T%2FrWU4HypmqzXz%2B7r5cHzW3b%2BcQN%2FfxqcOxpAAcn%2B27u5lpCWtnvs5sByad0OzWET3s7pxYWFfYlUadJrhq6EP5K1wjU%2BMMKYMZnr6F7y1J9er%2BYLA2adPY1vQ5E21cr8olxjJx%2BLCXa1xFeZ&X-Amz-Signature=e910f5a63081df7b89c507f1dcdc2cd0e277ef7ed3a2a68916861a73be6c84a1&X-Amz-SignedHeaders=host&x-id=GetObject)
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


