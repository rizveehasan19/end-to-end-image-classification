# Flowers-Recognizer

This is an image classification project that includes data collection, cleaning, model training, deployment and API integration. <br/>
This model can classify `10` different types of flowers <br/>
The types are following: <br/>
1. aster
2. daffodil
3. dahlia
4. daisy
5. dandelion
6. iris
7. orchid
8. rose
9. sunflower
10. tulip

# Dataset Preparation
**Data Collection:** Downloaded from `DuckDuckGo` using term name <br/>
**DataLoader:** Used `fastai DataBlock API` to set up the DataLoader. <br/>
**Data Augmentation:** fastai provides default data augmentation which operates in GPU. <br/>
Details can be found in `notebooks/data_prep.ipynb`

# Training and Data Cleaning
**Training:** Fine-tuned a `resnet34` model for 5 epochs (2 times) and got upto `~86% accuracy`. <br/>
**Data Cleaning:** I cleaned and updated data using fastai `ImageClassifierCleaner`. I cleaned the data each time after training or fine tuning, except for the last time which was the final iteration of the model. <br/>

# Model Deployment
I deployed to model to `HuggingFace Spaces Gradio App`. The implementation can be found in the `deployment` folder and in the corresponding [Space](https://huggingface.co/spaces/rizveehasan19/flowers_recognizer). <br/>

# API integration with GitHub Pages
The deployed model API is integrated in [GitHub Pages](https://rizveehasan19.github.io/Flowers-Recognizer/) Website. Implementation and other details can be found in `docs` folder.
