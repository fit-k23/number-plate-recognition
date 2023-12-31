# number-plate-recognition
NUMBER PLATE RECOGNITION

Nhận diện biển số xe!

Dataset và file train: https://drive.google.com/drive/folders/1O4CsL55yQUSPxQ3WLIGMVSwwyAGg5hQr

Video test: [tests](https://youtube.com/playlist?list=PL4MjhHHEFRBasa2vnYE1hZkhT0K4QbM1Z&si=BdJC-5SCD175M7lp)

|          Model | Decs                                                                                                                                                                                            | Link                                                                                                  |
|---------------:|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------|
| original.keras | train với dataset ban đầu, chỉ có biển số nước ngoài (0.8)                                                                                                                                      | [orinal.keras](https://drive.google.com/file/d/1-7e7GBqK3dDImv-mTPM8il149fE6CfIn/view?usp=drive_link) |
|      800.keras | model train với hơn 800 biển số Việt Nam (ô tô, xe máy, quân đội, doanh nghiệp, nhà nước), biển số nước ngoài (0.8)                                                                             | [800.keras](https://drive.google.com/file/d/1-JZ1kmy5KxpqLVvEmya6OvvQ3LApe_k5/view?usp=drive_link)    |
|     2000.keras | train với hơn 2000 biển số Việt Nam (ô tô, xe máy, quân đội, doanh nghiệp, nhà nước), biển số nước ngoài. Chiếm phần lớn là biển dân của ô tô và xe máy. (0.8)                                  | [2000.keras](https://drive.google.com/file/d/1-SC6MAzWY2QnygUjsYTlI8GUpkHAKZLj/view?usp=drive_link)   |
|        yolo v5 | model train với hơn 800 biển số Việt Nam (ô tô, xe máy, quân đội, doanh nghiệp, nhà nước), biển số nước ngoài với dữ liệu được chia 2/3 train và 1/3 test (dữ liệu được random trước khi train) | [yolo v5](https://drive.google.com/file/d/1eo4dlDV8NiDaXxg0flb6Nnm7wnKx47AC/view?usp=drive_link)      |

Nguồn dataset biển số Việt Nam: https://github.com/winter2897/Real-time-Auto-License-Plate-Recognition-with-Jetson-Nano/blob/main/doc/dataset.md

Công cụ tổng hợp dataset: https://github.com/fit-k23/number-plate-recognition/blob/main/input/group.py