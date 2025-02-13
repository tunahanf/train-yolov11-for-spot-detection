
<div align ="center" id="toc">
  <ul style="list-style: none">
    <summary>
      <h1 align="center" id="title">Custom Trained YOLO for Spot Detection on Vehicles</h1>
    </summary>
  </ul>
</div>



  
  
<h2>🧐 Rundown</h2>

*   This project involves training a custom <strong>YOLOv11</strong> model to detect <strong>bird droppings on cars</strong>.
*   Initially, the model was intended to detect <strong>paint defects on car surfaces</strong>, but due to dataset limitations, it was adapted to bird dropping detection.
*   The trained model serves as a <strong>preparatory study</strong> for detecting macro defects on car parts in the future.
*   The dataset used for training was curated and annotated specifically for this task.

   
<h2>💻 Built with</h2>

*   <strong>Ultralytics</strong> - Used for implementing and training the YOLOv11 model.


<h2>📊 Results & Evaluation</h2>

*   <strong>Confusion Matrix</strong> - Visual representation of classification performance.

![Confusion Matrix](https://github.com/tunahanf/train-yolov11-for-spot-detection/blob/main/confusion_matrix_normalized.png)

*   <strong>F1 Curve</strong> - Assessment of precision and recall balance.

![F1 Curve](https://github.com/tunahanf/train-yolov11-for-spot-detection/blob/main/F1_curve.png)

*   <strong>Results Summary</strong> - Key performance indicators of the model.

![Results Summary](https://github.com/tunahanf/train-yolov11-for-spot-detection/blob/main/results.png)


<h2>🎯 Conclusion</h2>

<img src="https://github.com/tunahanf/train-yolov11-for-spot-detection/blob/main/img/drop.png" width="500"/> <img src="https://github.com/tunahanf/train-yolov11-for-spot-detection/blob/main/runs/detect/predict/drop.jpg" width="500"/> 


While initially intended for macro defect detection in automotive production, this project demonstrates the potential of a custom-trained YOLOv11 model. The results show promise, and future iterations will build on this foundation to achieve the original goal of macro defect detection on automotive parts.


<h2>🔗 References</h2>

*   Dataset obtained from [Roboflow](https://universe.roboflow.com/lee-tae-hun/bird-drop-b69yy/dataset/2)

*   Google Colab [Notebook](https://colab.research.google.com/drive/1tUvNciyyuDpfdXYKTdlUex5viAmOu0fl?usp=sharing)


