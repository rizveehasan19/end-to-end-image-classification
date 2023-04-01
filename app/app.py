from fastai.vision.all import *
import gradio as gr
#import pathlib
#temp = pathlib.PosixPath
#pathlib.PosixPath = pathlib.WindowsPath
flower_labels = (
    "aster",
    "daffodil",
    "dahlia",
    "daisy",
    "dandelion",
    "iris",
    "orchid",
    "rose",
    "sunflower",
    "tulip"
)
model = load_learner(f'models/flowers_recognizer-v1.pkl')
def recognize_image(image):
  pred, idx, probs = model.predict(image)
  print(pred)
  return dict(zip(flower_labels, map(float, probs)))

image = gr.inputs.Image(shape=(192,192))
label = gr.outputs.Label()

examples = [
    'test_images/test01.jpg',
    'test_images/test02.jpg',
    'test_images/test03.jpg',
    'test_images/test04.jpg'
    ]
iface = gr.Interface(fn=recognize_image, inputs=image, outputs=label, examples=examples)
iface.launch(inline=False)