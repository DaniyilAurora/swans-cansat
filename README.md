# Swans CanSat

This is a project that is being actively developed by a small team from Swans School Marbella to take part in the [CanSat Competition in Spain](https://esero.es/cansat).
The project consists from two separate modules, the ground station and the satellite itself.

### Mission Control
![](docs/images/mission-control.png)

### Parts used in the CanSat:
| Name | Purpose | Link | Price |
| ---- | ------- | ---- | ----- |
| Arduino Nano Every | Main Microcontroller | [Aliexpress](https://www.aliexpress.com/p/tesla-landing/index.html?scenario=c_ppc_item_bridge&productId=1005007124870640&_immersiveMode=true&withMainCard=true&src=google&aff_platform=true&isdl=y&src=google&albch=shopping&acnt=439-079-4345&isdl=y&slnk=&plac=&mtctp=&albbt=Google_7_shopping&aff_platform=google&aff_short_key=UneMJZVf&gclsrc=aw.ds&&albagn=888888&&ds_e_adid=&ds_e_matchtype=&ds_e_device=c&ds_e_network=x&ds_e_product_group_id=&ds_e_product_id=es1005007124870640&ds_e_product_merchant_id=742682956&ds_e_product_country=ES&ds_e_product_language=es&ds_e_product_channel=online&ds_e_product_store_id=&ds_url_v=2&albcp=21840696692&albag=&isSmbAutoCall=false&needSmbHouyi=false&gad_source=1&gad_campaignid=21844625911&gbraid=0AAAAACbpfvZQq1Krc4L_yx2REbbgX6oQT&gclid=Cj0KCQiAiqDJBhCXARIsABk2kSm1RpRqDKkQmOeoMJIboBZ461OSeCcyoHubgm7xB96QCOtk_UmW7JgaAp87EALX_wcB) | € 7.30 |
| ESP32 Lora V3 | Antenna / Communication Module | [Amazon](https://www.amazon.es/Meshtastic-Modules-Integrated-Bluetooth-Compatibility/dp/B0FP4V2F5B/ref=sr_1_3_sspa?crid=H4AIX1X5NQ59&dib=eyJ2IjoiMSJ9.zwetVbXiR7BCxoph8ssnVZ_Xf7GDX9qLktNk3j7BGPaF_2JwMLs3bMW4cwU2VnnwR9vOpWLq1AtweAUpiR3LSxaJclpKJu8YslozlQk7cG6qfYedzTUgNqlEaQLMYETGvoNz6OER7OkGh51I9x6KXzN45C760aZsgEoYfQa3JpsrnEduvdf1U9NXCoSCuzOYNkUsSPpJGawcXMQIDSB0cogDZzw3hgVg_6yUyao_3y3VFgXwU_22MW8CdxpNEZE63RbzSzJcvZIKRdaTGCROlevbrCwnt-I-h3LTE0CAYGE.Q9-R33MuNUlUu81I1830wppSjUnE8IzubKxU5iP5wj0&dib_tag=se&keywords=lora+32&qid=1764274741&sprefix=lora+32%2Caps%2C63&sr=8-3-spons&aref=C9ZI9PftmL&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1) | € 31.99 |
| DHT 22 | Temperature / Humidity Sensor | [Amazon](https://www.amazon.es/AZDelivery-Temperature-Humidity-Compatible-Raspberry/dp/B078SVZB1X/ref=sr_1_1_sspa?crid=371GS0JVQYX56&dib=eyJ2IjoiMSJ9.J-FR0IoZwnzinf-GYqv-VhBdcA0ZyltfXXLhhyfIBLYmdM2FcND2Xl92aFXKaQLa9gYd7X1mtxBO1BL14bF9d67daR2P2iLl6PkV2OsRLxQH1BraLJnK5JLElxB6TqVdzJZDyIm84bpEhrxOKf8wXfNC39b4C__J-cvXztVqAsJE0KaXq501IdTYox3NC-jcMrTK9U8duP0FJOjix4asjthxcEjd5k78Q_z8c2fm4OnIRF417proys-JM9eax7hKZDw15oZre86X73Cgxw2wTQatn6nS08li8jsIJ9BoEV0.ITxJJ3Avz78FsyDPZZHhNNb4kJ0TpBjboEGnbryaQ3Q&dib_tag=se&keywords=dht22&qid=1764274879&sprefix=dht22%2Caps%2C67&sr=8-1-spons&aref=uHvBAi11mb&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1) | € 9.99 |
| GY-NEO6MV2 | GPS Module | [Amazon](https://www.amazon.es/-/en/GY-NEO6MV2-Control-Ceramic-Antenna-Arduino/dp/B0DX1V4WS1/ref=sr_1_4?crid=3K9VKRPIJG7KC&dib=eyJ2IjoiMSJ9.JNRDOjW2JtY8W7bL5XdLlcubeYwdr2VgsueqlEVuhRmY4DRFC7VgYJyfNwejKBNtAf1_HNnNSLzaLTQ0_jTdpRygQk3Fr2Lhi_LWdMCRP_iiWlICER9fjI6JykHyWySgIdQK5rqj5-d1oJ4RYd5gcjLuHaRaLqU9RpR_IpJibEMvJzF16Nqd4N0pT60nSkrH1ZmhS1XPYwwPZ4KMcoBnyP86CVUY8MtDTo7sCNyAXASgf7HZK3WNKVOTWNc3FW4tHbzDIBcHG-ZeRHdgkH82mKoBcyN6Wm7EmLqr_zvUYQU.tA30CE4RDg0vrwzPNbsIN9V5WELAFnfP9hNfJI46QNI&dib_tag=se&keywords=gps+module&qid=1764275015&sprefix=gps+module%2Caps%2C64&sr=8-4) | € 10.84 |
| BMP-280 | Air Pressure Sensor | [Amazon](https://www.amazon.es/-/en/BMP280-3-3V-Atmospheric-Temperature-Barometric-Precision/dp/B0BN1NXG4D/ref=sr_1_3?crid=22FJRP31NLK8P&dib=eyJ2IjoiMSJ9.sLKQThOeJNaMsZUtLjoDVMlpDhbGNmUObbwpwF7aYmzKxFmeIlr494YiyQzznkHtfysyCRg_38Xiwt7q_llRxY2lzNXBs-rPIOO8ikgfPlnAVhFrz9cbGf0ahOsLUJOf3cU1g_VeChjB5pBqz-DVWhtXFEgkgMaP67pTyIF21gS7s5SPX9COt3r8hobY0MB1t98MhXG1ZZNdSuQ2o-VVC8Cfn1YdYgJ2iIIUnjbMD5QHCXqdWpCCSwyKNCMUvSyKu7fbKb9CZGsT4b4Fewj9riaIq8XBHifT_-B_6TAd9FY.Ni5rHQkroatzWSZ4gPvfRlBhD8zfVFBvV1R6hMxwZmo&dib_tag=se&keywords=bmt280&qid=1764275235&sprefix=bmt280%2Caps%2C63&sr=8-3) | € 8.49 |
| | | Total | € 68.61 |

### Parts used in the Ground Station:
| Name | Purpose | Link | Price |
| ---- | ------- | ---- | ------- |
| ESP32 Lora V3 | Antenna / Communication Module | [Amazon](https://www.amazon.es/Meshtastic-Modules-Integrated-Bluetooth-Compatibility/dp/B0FP4V2F5B/ref=sr_1_3_sspa?crid=H4AIX1X5NQ59&dib=eyJ2IjoiMSJ9.zwetVbXiR7BCxoph8ssnVZ_Xf7GDX9qLktNk3j7BGPaF_2JwMLs3bMW4cwU2VnnwR9vOpWLq1AtweAUpiR3LSxaJclpKJu8YslozlQk7cG6qfYedzTUgNqlEaQLMYETGvoNz6OER7OkGh51I9x6KXzN45C760aZsgEoYfQa3JpsrnEduvdf1U9NXCoSCuzOYNkUsSPpJGawcXMQIDSB0cogDZzw3hgVg_6yUyao_3y3VFgXwU_22MW8CdxpNEZE63RbzSzJcvZIKRdaTGCROlevbrCwnt-I-h3LTE0CAYGE.Q9-R33MuNUlUu81I1830wppSjUnE8IzubKxU5iP5wj0&dib_tag=se&keywords=lora+32&qid=1764274741&sprefix=lora+32%2Caps%2C63&sr=8-3-spons&aref=C9ZI9PftmL&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1) | € 31.99 |
| 3m Long 50 ohm coaxial cable | Connects the Yagi-Uda Antenna to the amplifier and the amplifier to the Lora receiver | [Aliexpress](https://www.amazon.es/Meshtastic-Modules-Integrated-Bluetooth-Compatibility/dp/B0FP4V2F5B/ref=sr_1_3_sspa?crid=H4AIX1X5NQ59&dib=eyJ2IjoiMSJ9.zwetVbXiR7BCxoph8ssnVZ_Xf7GDX9qLktNk3j7BGPaF_2JwMLs3bMW4cwU2VnnwR9vOpWLq1AtweAUpiR3LSxaJclpKJu8YslozlQk7cG6qfYedzTUgNqlEaQLMYETGvoNz6OER7OkGh51I9x6KXzN45C760aZsgEoYfQa3JpsrnEduvdf1U9NXCoSCuzOYNkUsSPpJGawcXMQIDSB0cogDZzw3hgVg_6yUyao_3y3VFgXwU_22MW8CdxpNEZE63RbzSzJcvZIKRdaTGCROlevbrCwnt-I-h3LTE0CAYGE.Q9-R33MuNUlUu81I1830wppSjUnE8IzubKxU5iP5wj0&dib_tag=se&keywords=lora+32&qid=1764274741&sprefix=lora+32%2Caps%2C63&sr=8-3-spons&aref=C9ZI9PftmL&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1]) | € 4.67 |
| | | Total | € 36.66 |


### What we plan to do:
- Establish good, stable communication between the satellite and ground station.
- Be able to display the data received by the ground station (graphs, statistics etc.).
- Save collected data into flight files for future, post flight analysis.
- Use collected data to do calculations.
- Design and order a custom PCB.
- Design and build a parachute.
- Assemble everything into one unit.


### Our Secondary Mission:
For our secondary mission we have decided to do advanced telemetry and atmospheric analysis. This will include extra sensors such as GPS, a Gyroscope, Temperature and Humidity, Low concentration ozon sensor and a a Carbon Dioxide sensor and in the future an oxygen sensor. With the data from these sensors, we hope to be able to determine whether the atmosphere of a certain planet is suitable for human life.








