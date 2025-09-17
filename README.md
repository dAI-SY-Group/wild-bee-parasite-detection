# Deep Learning Based Detection of Bee Parasites
Svetlana Ionova · Henri Greil · Patrick Mäder · Marco Seeland 

## Data
The downloaded urls are available in `data/filtered_obs.csv` and `data/filtered_inat.csv` (cleaned). The list of added healthy bee images is available in `data/healthy_bees.csv`. 
### Composite Images
Parasites segmented from the images mentioned above comprised the foregrounds. The bee images which were used as backgrounds for composite image generation can be found in `data/background_bees.csv`. 
### Use Case Evaluation
We reserved 2500 images for the use case evaluation which are listed in `data/use_case_bees.txt`.
## Training
Model can be trained using `train.py`. We started from [OpenImages-v7 weights](https://docs.ultralytics.com/datasets/detect/open-images-v7) for YOLOv8m. Additionally, we modified the training script `ultralytics/engine/trainer.py` from the [Ultralytics' YOLO repository](https://github.com/ultralytics/ultralytics) (version 8.3.176) to progressively unfreeze the model. Our updated version can be found in `yolo/trainer.py`
## Citation
```
@inproceedings{wildbees_parasites,
  title = {Deep Learning Based Detection of Wild Bee Parasites under Natural Conditions},
  journal = {Ecological Informatics},
  author = {Ionova, Svetlana and Greil, Henri and M{\"a}der, Patrick and Seeland, Marco},
  volume = {},
  pages = {},
  year = {2025}
  issn = {},
  doi = {},
  url = {},
}
```