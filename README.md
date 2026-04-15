# Deep Learning Based Detection of Wild Bee Parasites under Natural Conditions
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
@article{Ionova2026,
  title = {Deep learning based detection of wild bee parasites under natural conditions},
  ISSN = {1574-9541},
  url = {http://dx.doi.org/10.1016/j.ecoinf.2026.103754},
  DOI = {10.1016/j.ecoinf.2026.103754},
  journal = {Ecological Informatics},
  publisher = {Elsevier BV},
  author = {Ionova,  Svetlana and Greil,  Henri and M\"{a}der,  Patrick and Seeland,  Marco},
  year = {2026},
  month = apr,
  pages = {103754}
}
```
