# CVAE_dialogue_generator

This project is a pytorch implementation for my paper "Xu, Dusek, Konstas, Rieser. Better Conversations by Modeling, Filtering, and Optimizing for Coherence and Diversity", which sadly has been neither accpted by any conference nor put on the arxiv :(

## Requirments <br />
* Python2.7
* [GloVe model](https://github.com/maciejkula/glove-python)
* [Opensubtitles processing tool](https://github.com/WattSocialBot/movie_tools)

## Quickstart <br />
### Step1: Download the OpenSubtitles dataset <br />
This code is based on OpenSubtitles dataset [Automatic Turn Segmentation for Movie & TV Subtitles](http://www.diva-portal.org/smash/get/diva2:1034694/FULLTEXT01.pdf). To get the data, please contact the authors [Pierre Lison](https://github.com/plison). You should unzip the datset and name it as `opensubtitles` and put it in 
```
data/filter/
```

### Step2: Creat datasets for generator <br />
We use toolkit [Opensubtitles processing tool](https://github.com/WattSocialBot/movie_tools) owned by [Ondrej Dusek](https://github.com/tuetschek) to extract dialogues from OpenSubtitles dataset `data/filter/opensubtitles/`.
```
~/data/movie_tools/convert_nrno_subs.py -D -s -S train:train-dev:devel:test -r 97:1:1:1 -d all_dialogues_cased opensubtitles/ dial.jsons.txt
```
The outputs are 

* `train.dial.jsons.txt`
* `train-dev.dial.jsons.txt`
* `devel.dial.jsons.txt`
* `test.dial.jsons.txt`

as the split ratio `97:1:1:1`.

### Step3: Filter the OpenSubtitles dataset <br />
**Step2.1: Train GloVe model on OpenSubtitles:** <br />
Run the following command in `data/filter/` to read subtitles from json files and save in file `bag_of_words` in the same directory.
```
python read_html.py
```
Then, run the following two commands to train a [GloVe model](https://github.com/maciejkula/glove-python) on the OpenSubtitles dataset. `get_corpus.py` is used to build the corpus model `corpus.model` and `train.py` train the model on `corpus.model`. The trained model is `glove.model` in the same directory.
```
python get_corpus.py
python train.py
```
**Step2.1: Train GloVe model on OpenSubtitles:** <br />
