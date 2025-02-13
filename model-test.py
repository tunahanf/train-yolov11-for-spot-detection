from ultralytics import YOLO

model = YOLO("model.pt")

results = model.predict("./img", save=True)
