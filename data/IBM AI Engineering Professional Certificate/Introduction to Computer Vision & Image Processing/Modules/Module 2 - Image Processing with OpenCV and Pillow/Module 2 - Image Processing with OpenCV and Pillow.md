

# Module 2: Image Processing with OpenCV and Pillow
## Digital Image Concepts and Processing in Python
### What is a Digital Image?
A **digital image** can be described as a **rectangular array of numbers**. It is commonly easier to interpret a **gray-scale image**, which is composed of varying **shades of gray**. If zoomed in, it becomes clear that the image is made up of a grid of blocks called **pixels**.
#### Pixel Representation
Each pixel is represented by a **numerical intensity value**:
- **Intensity values** range between **0 and 255**, where:
	- **0** represents **black**.
	- **255** represents **white**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fa1bb4aa-313a-44c2-a7b3-7fa4a8432b08/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RI3K7SX3%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171234Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIERr9erP4vKeLzRhZ%2FXPnbzZ1QX%2FYHPvhhoEtOuMqPK9AiAs9GFECea6g3jfx0OCVqkZqgGwna%2FzT3TLVnTySgG0RyqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMKjlvk%2BrN9THn3o2AKtwDRSudbCxnCFkxyc2RE58ZMd8YT12ErxpgvbJAG22KkflNvCq2iJcL5%2FYrcSKod0QCOyou5rOMfz5pd8wGWVfVg4%2Fljs%2BkfaR1ZXzuJ%2BHCLr3yA1PfxcRxRcbGsEnzGy%2FzhI5GNQOyHA6f111l1cFxo%2FJDR4sucOrtTS02p%2BZiW%2FAXnVkpALDX1yMKsmSzWFJxkiG%2FMaUxHvFW4LpTSsnHclpxDtN5Q1PpmbECD2ihO0N0u3uEsVGUAp6EfvxJFr2y5L3Ub%2BPqn8v74EuxnlyzqWAFPQsfcV0vPp2P9lOywOCzj6FABOAPfBUJfwzlQqKtE71IDvWu7UrCAzKtQ6O2WlS2FaMWXi%2FRkzUGRKuqlgDL715sUIfVPJLpwHJUSwcYaEgUiSU8osx%2BX%2F5DwoaZhpLngnuTCs5DqlEdgH5Jx9PFQtZwxHGQ%2Fak4R3hZEbBRuUJMLYNU%2BdpXHClJKkfx3rlR4Sf3q5y%2FyXhfw%2BT%2Fy2E8g6K%2FGNKNx1%2F%2FE8cOvJCcGiSGmYS34e1esXgWXvkufrCUOB8slVyswdUSLllYmlcoJBUiIE2usF8rEqcpAwE7QqZLV2YnfJOPakyHqjsSwWk%2B9r4tPll9MoaV7iv%2F2Yk50i1OSrcmXpoZoswwr8j4vAY6pgEMY7FOx0LNUmYAUE43sYwBAy68quuKeQ8Ya6DOp%2F6OkFIRwn5zLokW8j5%2FFsE0izqJ6xkFcWAGjTJFapkJnBEdyLhtF6CmDp0nHz1H08O%2FsaCxMMTszCCW8pwfe3LZBJj7w%2FmyHa%2Bq2s6gN%2BfjX7P4BBikglaV0oYHwXp0fHf6CeRU9naA%2B%2BHjrVwrjAvG3W%2BXqQkk8q%2BS%2BXpLx%2FN6iV3itaGbe%2FhO&X-Amz-Signature=9d1a02a4fb378c80744f7dc6c23f8effe3da0d1234124b2e818bf885ad9b0ee9&X-Amz-SignedHeaders=host&x-id=GetObject)
The number of intensity values directly impacts the **contrast** of the image:
- Higher intensity values provide better **contrast**.
- Reducing intensity values can result in visual changes, as seen in the following steps:
	- **256 intensity values**: The image appears clear and accurate.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0de7dfb4-99dc-4b87-8932-5165b3c3b775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667FCHA5UW%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICyN40ll3ayByYopjWZ1WeXePIHjoikv5rHLxEIqrdXTAiA5SQLWVTwGlhwdZjgPYxtMlV%2FSNXjN5G7VIP3ScUEv3CqIBAjW%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMM2D2LDQ4Rv0%2FetpCKtwDTzp70ghxD6dsN8JZA24rrmUd8vEbkvkGFCPNhTBL%2FkBkcNe5kfFjLgeldFIcw%2FjCq9tBC68l5kRU0ZCOtG%2BZLvKPCP8Dyj0BmpqJgbtukEvGEucMzoOtsB6GmF7Ls5metfUhoXtIGLoWdrutwMPTNC6kdIQoE5JDsoktR17f%2FErSmZUYWRwFEV6lPlZcrGIa5IY19JD%2BaNKRKM2wixbF3L5DVw2Zk70B0IK85eE6WX%2FUFCXgXVIMDRxUCbeF5Maf5CixgaHE828j4jfXFY4oBVAYBLc6LOiRnPyTW6%2BgxqzRV6%2B5OzoXQFHPIHSE6WuYqaB6x3P6lQYEXDWRmY4xHf2TZg9SIHH8HCGg1A%2B%2BIiTjHo4DTNpJwFJM2sqHcU4cRKkzkEvDvYPharGp0yqLA%2B5Ctr8LVftXGmcGBnUBC3ksoATVgHqEVMn7fl9DUnJxCZH7T85EmZcdQHbGzBPg9aHJ5gM4OqLtaz59GYXnY5XO0TfGPuLga9P1tdFs0IT%2BdOXl9fcKnGRh%2FK8RpY05aQSz%2FBZhkwa3unevAL46uoULDJlNVt5uZciV3tWQ76FjN4VIMkyPWce7FtaBoqQTTahQ19YjtW2ydfCpElm5ocTBAdINA6yFlgl2GAUw57L4vAY6pgE7ob4Twfe%2Bng9Dku5pXpmMoTpEpBnp7YOdT356uhLa18h852nzjMtUUGg64rvn1yRXwL9G7bC%2FydUMkr%2FyS84y9TMf4H6sxurJwRQk7Et72LinHgso7hQ3wzdau1ymHmbtKRzVNIxHEMoi8V%2Fw1x7CcSjOi7UHep7hYg0ZHDSVORk5yaVsYoPcyn6zBKGpltbEXAUQxzDewCchtVBsa4DS%2Ffi3Vh2B&X-Amz-Signature=eace80209468517a41b9eeb38e1ca7588b2099521102e56838f5b85f65d18c46&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **32 intensity values:**
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7eb81f08-b190-4c5a-ba2b-2a498a15b2c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667FCHA5UW%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICyN40ll3ayByYopjWZ1WeXePIHjoikv5rHLxEIqrdXTAiA5SQLWVTwGlhwdZjgPYxtMlV%2FSNXjN5G7VIP3ScUEv3CqIBAjW%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMM2D2LDQ4Rv0%2FetpCKtwDTzp70ghxD6dsN8JZA24rrmUd8vEbkvkGFCPNhTBL%2FkBkcNe5kfFjLgeldFIcw%2FjCq9tBC68l5kRU0ZCOtG%2BZLvKPCP8Dyj0BmpqJgbtukEvGEucMzoOtsB6GmF7Ls5metfUhoXtIGLoWdrutwMPTNC6kdIQoE5JDsoktR17f%2FErSmZUYWRwFEV6lPlZcrGIa5IY19JD%2BaNKRKM2wixbF3L5DVw2Zk70B0IK85eE6WX%2FUFCXgXVIMDRxUCbeF5Maf5CixgaHE828j4jfXFY4oBVAYBLc6LOiRnPyTW6%2BgxqzRV6%2B5OzoXQFHPIHSE6WuYqaB6x3P6lQYEXDWRmY4xHf2TZg9SIHH8HCGg1A%2B%2BIiTjHo4DTNpJwFJM2sqHcU4cRKkzkEvDvYPharGp0yqLA%2B5Ctr8LVftXGmcGBnUBC3ksoATVgHqEVMn7fl9DUnJxCZH7T85EmZcdQHbGzBPg9aHJ5gM4OqLtaz59GYXnY5XO0TfGPuLga9P1tdFs0IT%2BdOXl9fcKnGRh%2FK8RpY05aQSz%2FBZhkwa3unevAL46uoULDJlNVt5uZciV3tWQ76FjN4VIMkyPWce7FtaBoqQTTahQ19YjtW2ydfCpElm5ocTBAdINA6yFlgl2GAUw57L4vAY6pgE7ob4Twfe%2Bng9Dku5pXpmMoTpEpBnp7YOdT356uhLa18h852nzjMtUUGg64rvn1yRXwL9G7bC%2FydUMkr%2FyS84y9TMf4H6sxurJwRQk7Et72LinHgso7hQ3wzdau1ymHmbtKRzVNIxHEMoi8V%2Fw1x7CcSjOi7UHep7hYg0ZHDSVORk5yaVsYoPcyn6zBKGpltbEXAUQxzDewCchtVBsa4DS%2Ffi3Vh2B&X-Amz-Signature=bc8cdbc12e38a35c5a5810ccd3b94c9e8a0d2b5f7ced028b50e33c6defb82970&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **16 intensity values**: Differences are noticeable in low-contrast areas.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/6bf56d44-9a14-4b7b-98c2-1f00b8630f0c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667FCHA5UW%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICyN40ll3ayByYopjWZ1WeXePIHjoikv5rHLxEIqrdXTAiA5SQLWVTwGlhwdZjgPYxtMlV%2FSNXjN5G7VIP3ScUEv3CqIBAjW%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMM2D2LDQ4Rv0%2FetpCKtwDTzp70ghxD6dsN8JZA24rrmUd8vEbkvkGFCPNhTBL%2FkBkcNe5kfFjLgeldFIcw%2FjCq9tBC68l5kRU0ZCOtG%2BZLvKPCP8Dyj0BmpqJgbtukEvGEucMzoOtsB6GmF7Ls5metfUhoXtIGLoWdrutwMPTNC6kdIQoE5JDsoktR17f%2FErSmZUYWRwFEV6lPlZcrGIa5IY19JD%2BaNKRKM2wixbF3L5DVw2Zk70B0IK85eE6WX%2FUFCXgXVIMDRxUCbeF5Maf5CixgaHE828j4jfXFY4oBVAYBLc6LOiRnPyTW6%2BgxqzRV6%2B5OzoXQFHPIHSE6WuYqaB6x3P6lQYEXDWRmY4xHf2TZg9SIHH8HCGg1A%2B%2BIiTjHo4DTNpJwFJM2sqHcU4cRKkzkEvDvYPharGp0yqLA%2B5Ctr8LVftXGmcGBnUBC3ksoATVgHqEVMn7fl9DUnJxCZH7T85EmZcdQHbGzBPg9aHJ5gM4OqLtaz59GYXnY5XO0TfGPuLga9P1tdFs0IT%2BdOXl9fcKnGRh%2FK8RpY05aQSz%2FBZhkwa3unevAL46uoULDJlNVt5uZciV3tWQ76FjN4VIMkyPWce7FtaBoqQTTahQ19YjtW2ydfCpElm5ocTBAdINA6yFlgl2GAUw57L4vAY6pgE7ob4Twfe%2Bng9Dku5pXpmMoTpEpBnp7YOdT356uhLa18h852nzjMtUUGg64rvn1yRXwL9G7bC%2FydUMkr%2FyS84y9TMf4H6sxurJwRQk7Et72LinHgso7hQ3wzdau1ymHmbtKRzVNIxHEMoi8V%2Fw1x7CcSjOi7UHep7hYg0ZHDSVORk5yaVsYoPcyn6zBKGpltbEXAUQxzDewCchtVBsa4DS%2Ffi3Vh2B&X-Amz-Signature=16b4da5b222e5a200278e0795f840278a10b98fce32fe85a01429514ac8c0638&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **8 intensity values**: The image begins to lose definition.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cca05878-ca1a-43e0-8bec-1d146756f9ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667FCHA5UW%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICyN40ll3ayByYopjWZ1WeXePIHjoikv5rHLxEIqrdXTAiA5SQLWVTwGlhwdZjgPYxtMlV%2FSNXjN5G7VIP3ScUEv3CqIBAjW%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMM2D2LDQ4Rv0%2FetpCKtwDTzp70ghxD6dsN8JZA24rrmUd8vEbkvkGFCPNhTBL%2FkBkcNe5kfFjLgeldFIcw%2FjCq9tBC68l5kRU0ZCOtG%2BZLvKPCP8Dyj0BmpqJgbtukEvGEucMzoOtsB6GmF7Ls5metfUhoXtIGLoWdrutwMPTNC6kdIQoE5JDsoktR17f%2FErSmZUYWRwFEV6lPlZcrGIa5IY19JD%2BaNKRKM2wixbF3L5DVw2Zk70B0IK85eE6WX%2FUFCXgXVIMDRxUCbeF5Maf5CixgaHE828j4jfXFY4oBVAYBLc6LOiRnPyTW6%2BgxqzRV6%2B5OzoXQFHPIHSE6WuYqaB6x3P6lQYEXDWRmY4xHf2TZg9SIHH8HCGg1A%2B%2BIiTjHo4DTNpJwFJM2sqHcU4cRKkzkEvDvYPharGp0yqLA%2B5Ctr8LVftXGmcGBnUBC3ksoATVgHqEVMn7fl9DUnJxCZH7T85EmZcdQHbGzBPg9aHJ5gM4OqLtaz59GYXnY5XO0TfGPuLga9P1tdFs0IT%2BdOXl9fcKnGRh%2FK8RpY05aQSz%2FBZhkwa3unevAL46uoULDJlNVt5uZciV3tWQ76FjN4VIMkyPWce7FtaBoqQTTahQ19YjtW2ydfCpElm5ocTBAdINA6yFlgl2GAUw57L4vAY6pgE7ob4Twfe%2Bng9Dku5pXpmMoTpEpBnp7YOdT356uhLa18h852nzjMtUUGg64rvn1yRXwL9G7bC%2FydUMkr%2FyS84y9TMf4H6sxurJwRQk7Et72LinHgso7hQ3wzdau1ymHmbtKRzVNIxHEMoi8V%2Fw1x7CcSjOi7UHep7hYg0ZHDSVORk5yaVsYoPcyn6zBKGpltbEXAUQxzDewCchtVBsa4DS%2Ffi3Vh2B&X-Amz-Signature=af3886b1d067472310f5ed2364c3480224d655befe3f7c756af5ed3224e80f1a&X-Amz-SignedHeaders=host&x-id=GetObject)
	- **2 intensity values**: The image looks cartoonish.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/12da64d7-6b97-44e0-bc2c-52b9c47ce212/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667FCHA5UW%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICyN40ll3ayByYopjWZ1WeXePIHjoikv5rHLxEIqrdXTAiA5SQLWVTwGlhwdZjgPYxtMlV%2FSNXjN5G7VIP3ScUEv3CqIBAjW%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMM2D2LDQ4Rv0%2FetpCKtwDTzp70ghxD6dsN8JZA24rrmUd8vEbkvkGFCPNhTBL%2FkBkcNe5kfFjLgeldFIcw%2FjCq9tBC68l5kRU0ZCOtG%2BZLvKPCP8Dyj0BmpqJgbtukEvGEucMzoOtsB6GmF7Ls5metfUhoXtIGLoWdrutwMPTNC6kdIQoE5JDsoktR17f%2FErSmZUYWRwFEV6lPlZcrGIa5IY19JD%2BaNKRKM2wixbF3L5DVw2Zk70B0IK85eE6WX%2FUFCXgXVIMDRxUCbeF5Maf5CixgaHE828j4jfXFY4oBVAYBLc6LOiRnPyTW6%2BgxqzRV6%2B5OzoXQFHPIHSE6WuYqaB6x3P6lQYEXDWRmY4xHf2TZg9SIHH8HCGg1A%2B%2BIiTjHo4DTNpJwFJM2sqHcU4cRKkzkEvDvYPharGp0yqLA%2B5Ctr8LVftXGmcGBnUBC3ksoATVgHqEVMn7fl9DUnJxCZH7T85EmZcdQHbGzBPg9aHJ5gM4OqLtaz59GYXnY5XO0TfGPuLga9P1tdFs0IT%2BdOXl9fcKnGRh%2FK8RpY05aQSz%2FBZhkwa3unevAL46uoULDJlNVt5uZciV3tWQ76FjN4VIMkyPWce7FtaBoqQTTahQ19YjtW2ydfCpElm5ocTBAdINA6yFlgl2GAUw57L4vAY6pgE7ob4Twfe%2Bng9Dku5pXpmMoTpEpBnp7YOdT356uhLa18h852nzjMtUUGg64rvn1yRXwL9G7bC%2FydUMkr%2FyS84y9TMf4H6sxurJwRQk7Et72LinHgso7hQ3wzdau1ymHmbtKRzVNIxHEMoi8V%2Fw1x7CcSjOi7UHep7hYg0ZHDSVORk5yaVsYoPcyn6zBKGpltbEXAUQxzDewCchtVBsa4DS%2Ffi3Vh2B&X-Amz-Signature=66990d247554c3187666d75fe4674f4094e421d322b6581b54f634b80d0fb425&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Dimensions
- The **height** represents the number of **rows**.
- The **width** represents the number of **columns**.
- Each pixel is indexed based on its position in the row and column.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ff056335-e79e-4491-b508-30cd45b6c194/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RI3K7SX3%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIERr9erP4vKeLzRhZ%2FXPnbzZ1QX%2FYHPvhhoEtOuMqPK9AiAs9GFECea6g3jfx0OCVqkZqgGwna%2FzT3TLVnTySgG0RyqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMKjlvk%2BrN9THn3o2AKtwDRSudbCxnCFkxyc2RE58ZMd8YT12ErxpgvbJAG22KkflNvCq2iJcL5%2FYrcSKod0QCOyou5rOMfz5pd8wGWVfVg4%2Fljs%2BkfaR1ZXzuJ%2BHCLr3yA1PfxcRxRcbGsEnzGy%2FzhI5GNQOyHA6f111l1cFxo%2FJDR4sucOrtTS02p%2BZiW%2FAXnVkpALDX1yMKsmSzWFJxkiG%2FMaUxHvFW4LpTSsnHclpxDtN5Q1PpmbECD2ihO0N0u3uEsVGUAp6EfvxJFr2y5L3Ub%2BPqn8v74EuxnlyzqWAFPQsfcV0vPp2P9lOywOCzj6FABOAPfBUJfwzlQqKtE71IDvWu7UrCAzKtQ6O2WlS2FaMWXi%2FRkzUGRKuqlgDL715sUIfVPJLpwHJUSwcYaEgUiSU8osx%2BX%2F5DwoaZhpLngnuTCs5DqlEdgH5Jx9PFQtZwxHGQ%2Fak4R3hZEbBRuUJMLYNU%2BdpXHClJKkfx3rlR4Sf3q5y%2FyXhfw%2BT%2Fy2E8g6K%2FGNKNx1%2F%2FE8cOvJCcGiSGmYS34e1esXgWXvkufrCUOB8slVyswdUSLllYmlcoJBUiIE2usF8rEqcpAwE7QqZLV2YnfJOPakyHqjsSwWk%2B9r4tPll9MoaV7iv%2F2Yk50i1OSrcmXpoZoswwr8j4vAY6pgEMY7FOx0LNUmYAUE43sYwBAy68quuKeQ8Ya6DOp%2F6OkFIRwn5zLokW8j5%2FFsE0izqJ6xkFcWAGjTJFapkJnBEdyLhtF6CmDp0nHz1H08O%2FsaCxMMTszCCW8pwfe3LZBJj7w%2FmyHa%2Bq2s6gN%2BfjX7P4BBikglaV0oYHwXp0fHf6CeRU9naA%2B%2BHjrVwrjAvG3W%2BXqQkk8q%2BS%2BXpLx%2FN6iV3itaGbe%2FhO&X-Amz-Signature=96b36a2a3c7c726cc471cc71df4aadf5dbbf209895f9d15c0a38059c3ae8beee&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Composition
In **real-world images**, each pixel value comes from a grid of **sensors** that capture light. These values are then **quantized** into digital samples to form the image.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c721ea0-409b-4d32-b630-a00d6f170d18/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RI3K7SX3%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171234Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIERr9erP4vKeLzRhZ%2FXPnbzZ1QX%2FYHPvhhoEtOuMqPK9AiAs9GFECea6g3jfx0OCVqkZqgGwna%2FzT3TLVnTySgG0RyqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMKjlvk%2BrN9THn3o2AKtwDRSudbCxnCFkxyc2RE58ZMd8YT12ErxpgvbJAG22KkflNvCq2iJcL5%2FYrcSKod0QCOyou5rOMfz5pd8wGWVfVg4%2Fljs%2BkfaR1ZXzuJ%2BHCLr3yA1PfxcRxRcbGsEnzGy%2FzhI5GNQOyHA6f111l1cFxo%2FJDR4sucOrtTS02p%2BZiW%2FAXnVkpALDX1yMKsmSzWFJxkiG%2FMaUxHvFW4LpTSsnHclpxDtN5Q1PpmbECD2ihO0N0u3uEsVGUAp6EfvxJFr2y5L3Ub%2BPqn8v74EuxnlyzqWAFPQsfcV0vPp2P9lOywOCzj6FABOAPfBUJfwzlQqKtE71IDvWu7UrCAzKtQ6O2WlS2FaMWXi%2FRkzUGRKuqlgDL715sUIfVPJLpwHJUSwcYaEgUiSU8osx%2BX%2F5DwoaZhpLngnuTCs5DqlEdgH5Jx9PFQtZwxHGQ%2Fak4R3hZEbBRuUJMLYNU%2BdpXHClJKkfx3rlR4Sf3q5y%2FyXhfw%2BT%2Fy2E8g6K%2FGNKNx1%2F%2FE8cOvJCcGiSGmYS34e1esXgWXvkufrCUOB8slVyswdUSLllYmlcoJBUiIE2usF8rEqcpAwE7QqZLV2YnfJOPakyHqjsSwWk%2B9r4tPll9MoaV7iv%2F2Yk50i1OSrcmXpoZoswwr8j4vAY6pgEMY7FOx0LNUmYAUE43sYwBAy68quuKeQ8Ya6DOp%2F6OkFIRwn5zLokW8j5%2FFsE0izqJ6xkFcWAGjTJFapkJnBEdyLhtF6CmDp0nHz1H08O%2FsaCxMMTszCCW8pwfe3LZBJj7w%2FmyHa%2Bq2s6gN%2BfjX7P4BBikglaV0oYHwXp0fHf6CeRU9naA%2B%2BHjrVwrjAvG3W%2BXqQkk8q%2BS%2BXpLx%2FN6iV3itaGbe%2FhO&X-Amz-Signature=570616d0e444a8abbdb219db420ea5ab2f3490408cbc78a77b95b35843df54e3&X-Amz-SignedHeaders=host&x-id=GetObject)
### Color Images and Channels
A **color image** is composed of different **color channels** (e.g., **red**, **green**, and **blue**):
- Each channel is essentially a **gray-scale image** representing intensity values for that color.
- A color image is like a **cube** where each channel represents a **slice**.
For example:
- **Red channel**: Represents red intensities.
- **Green channel**: Represents green intensities.
- **Blue channel**: Represents blue intensities.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c0cc17c9-842f-413f-82e8-f3f44278cf74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RI3K7SX3%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171234Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIERr9erP4vKeLzRhZ%2FXPnbzZ1QX%2FYHPvhhoEtOuMqPK9AiAs9GFECea6g3jfx0OCVqkZqgGwna%2FzT3TLVnTySgG0RyqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMKjlvk%2BrN9THn3o2AKtwDRSudbCxnCFkxyc2RE58ZMd8YT12ErxpgvbJAG22KkflNvCq2iJcL5%2FYrcSKod0QCOyou5rOMfz5pd8wGWVfVg4%2Fljs%2BkfaR1ZXzuJ%2BHCLr3yA1PfxcRxRcbGsEnzGy%2FzhI5GNQOyHA6f111l1cFxo%2FJDR4sucOrtTS02p%2BZiW%2FAXnVkpALDX1yMKsmSzWFJxkiG%2FMaUxHvFW4LpTSsnHclpxDtN5Q1PpmbECD2ihO0N0u3uEsVGUAp6EfvxJFr2y5L3Ub%2BPqn8v74EuxnlyzqWAFPQsfcV0vPp2P9lOywOCzj6FABOAPfBUJfwzlQqKtE71IDvWu7UrCAzKtQ6O2WlS2FaMWXi%2FRkzUGRKuqlgDL715sUIfVPJLpwHJUSwcYaEgUiSU8osx%2BX%2F5DwoaZhpLngnuTCs5DqlEdgH5Jx9PFQtZwxHGQ%2Fak4R3hZEbBRuUJMLYNU%2BdpXHClJKkfx3rlR4Sf3q5y%2FyXhfw%2BT%2Fy2E8g6K%2FGNKNx1%2F%2FE8cOvJCcGiSGmYS34e1esXgWXvkufrCUOB8slVyswdUSLllYmlcoJBUiIE2usF8rEqcpAwE7QqZLV2YnfJOPakyHqjsSwWk%2B9r4tPll9MoaV7iv%2F2Yk50i1OSrcmXpoZoswwr8j4vAY6pgEMY7FOx0LNUmYAUE43sYwBAy68quuKeQ8Ya6DOp%2F6OkFIRwn5zLokW8j5%2FFsE0izqJ6xkFcWAGjTJFapkJnBEdyLhtF6CmDp0nHz1H08O%2FsaCxMMTszCCW8pwfe3LZBJj7w%2FmyHa%2Bq2s6gN%2BfjX7P4BBikglaV0oYHwXp0fHf6CeRU9naA%2B%2BHjrVwrjAvG3W%2BXqQkk8q%2BS%2BXpLx%2FN6iV3itaGbe%2FhO&X-Amz-Signature=e5bf8ba555356b25adebd3d42fb1147f499af35ea2836f4b430f2710ad31064a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Image Masks
- A **binary mask** can be used to identify specific objects in an image.
- Pixels corresponding to the object are represented as **1**, while the rest are **0**.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/667eab4d-d19d-4618-81d0-663b6beb002c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RI3K7SX3%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171234Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIERr9erP4vKeLzRhZ%2FXPnbzZ1QX%2FYHPvhhoEtOuMqPK9AiAs9GFECea6g3jfx0OCVqkZqgGwna%2FzT3TLVnTySgG0RyqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMKjlvk%2BrN9THn3o2AKtwDRSudbCxnCFkxyc2RE58ZMd8YT12ErxpgvbJAG22KkflNvCq2iJcL5%2FYrcSKod0QCOyou5rOMfz5pd8wGWVfVg4%2Fljs%2BkfaR1ZXzuJ%2BHCLr3yA1PfxcRxRcbGsEnzGy%2FzhI5GNQOyHA6f111l1cFxo%2FJDR4sucOrtTS02p%2BZiW%2FAXnVkpALDX1yMKsmSzWFJxkiG%2FMaUxHvFW4LpTSsnHclpxDtN5Q1PpmbECD2ihO0N0u3uEsVGUAp6EfvxJFr2y5L3Ub%2BPqn8v74EuxnlyzqWAFPQsfcV0vPp2P9lOywOCzj6FABOAPfBUJfwzlQqKtE71IDvWu7UrCAzKtQ6O2WlS2FaMWXi%2FRkzUGRKuqlgDL715sUIfVPJLpwHJUSwcYaEgUiSU8osx%2BX%2F5DwoaZhpLngnuTCs5DqlEdgH5Jx9PFQtZwxHGQ%2Fak4R3hZEbBRuUJMLYNU%2BdpXHClJKkfx3rlR4Sf3q5y%2FyXhfw%2BT%2Fy2E8g6K%2FGNKNx1%2F%2FE8cOvJCcGiSGmYS34e1esXgWXvkufrCUOB8slVyswdUSLllYmlcoJBUiIE2usF8rEqcpAwE7QqZLV2YnfJOPakyHqjsSwWk%2B9r4tPll9MoaV7iv%2F2Yk50i1OSrcmXpoZoswwr8j4vAY6pgEMY7FOx0LNUmYAUE43sYwBAy68quuKeQ8Ya6DOp%2F6OkFIRwn5zLokW8j5%2FFsE0izqJ6xkFcWAGjTJFapkJnBEdyLhtF6CmDp0nHz1H08O%2FsaCxMMTszCCW8pwfe3LZBJj7w%2FmyHa%2Bq2s6gN%2BfjX7P4BBikglaV0oYHwXp0fHf6CeRU9naA%2B%2BHjrVwrjAvG3W%2BXqQkk8q%2BS%2BXpLx%2FN6iV3itaGbe%2FhO&X-Amz-Signature=99ba2c74ce85e7315a45c0d20eb9bdded417bf83417686ba1e24a65c50e23089&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/25fcc977-54ea-484c-997e-9b6bd016f347/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RI3K7SX3%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIERr9erP4vKeLzRhZ%2FXPnbzZ1QX%2FYHPvhhoEtOuMqPK9AiAs9GFECea6g3jfx0OCVqkZqgGwna%2FzT3TLVnTySgG0RyqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMKjlvk%2BrN9THn3o2AKtwDRSudbCxnCFkxyc2RE58ZMd8YT12ErxpgvbJAG22KkflNvCq2iJcL5%2FYrcSKod0QCOyou5rOMfz5pd8wGWVfVg4%2Fljs%2BkfaR1ZXzuJ%2BHCLr3yA1PfxcRxRcbGsEnzGy%2FzhI5GNQOyHA6f111l1cFxo%2FJDR4sucOrtTS02p%2BZiW%2FAXnVkpALDX1yMKsmSzWFJxkiG%2FMaUxHvFW4LpTSsnHclpxDtN5Q1PpmbECD2ihO0N0u3uEsVGUAp6EfvxJFr2y5L3Ub%2BPqn8v74EuxnlyzqWAFPQsfcV0vPp2P9lOywOCzj6FABOAPfBUJfwzlQqKtE71IDvWu7UrCAzKtQ6O2WlS2FaMWXi%2FRkzUGRKuqlgDL715sUIfVPJLpwHJUSwcYaEgUiSU8osx%2BX%2F5DwoaZhpLngnuTCs5DqlEdgH5Jx9PFQtZwxHGQ%2Fak4R3hZEbBRuUJMLYNU%2BdpXHClJKkfx3rlR4Sf3q5y%2FyXhfw%2BT%2Fy2E8g6K%2FGNKNx1%2F%2FE8cOvJCcGiSGmYS34e1esXgWXvkufrCUOB8slVyswdUSLllYmlcoJBUiIE2usF8rEqcpAwE7QqZLV2YnfJOPakyHqjsSwWk%2B9r4tPll9MoaV7iv%2F2Yk50i1OSrcmXpoZoswwr8j4vAY6pgEMY7FOx0LNUmYAUE43sYwBAy68quuKeQ8Ya6DOp%2F6OkFIRwn5zLokW8j5%2FFsE0izqJ6xkFcWAGjTJFapkJnBEdyLhtF6CmDp0nHz1H08O%2FsaCxMMTszCCW8pwfe3LZBJj7w%2FmyHa%2Bq2s6gN%2BfjX7P4BBikglaV0oYHwXp0fHf6CeRU9naA%2B%2BHjrVwrjAvG3W%2BXqQkk8q%2BS%2BXpLx%2FN6iV3itaGbe%2FhO&X-Amz-Signature=bc2afba161caa16db58a5c27e22b7de9607f8d60a6438becd1ce7120c40a0d03&X-Amz-SignedHeaders=host&x-id=GetObject)
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


