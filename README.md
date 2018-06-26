# CVAE_dialogue_generator

This project is a pytorch implementation for my paper "Xu, Dusek, Konstas, Rieser. Better Conversations by Modeling, Filtering, and Optimizing for Coherence and Diversity", which sadly has been neither accpted by any conference nor put on the arxiv :(

## Requirments <br />
* Python2.7
* [GloVe model](https://github.com/maciejkula/glove-python)

## Quickstart <br />
### Step1: Download the OpenSubtitles dataset <br />
This code is based on OpenSubtitles dataset [Automatic Turn Segmentation for Movie & TV Subtitles](http://www.diva-portal.org/smash/get/diva2:1034694/FULLTEXT01.pdf). To get the data, please contact the authors [Pierre Lison](https://github.com/plison). You should unzip the datset and name it as `opensubtitles` and put it in 
```
data/filter/
```

### Step2: Filter the OpenSubtitles dataset <br />
Run the following command in `data/filter/` to read subtitles from json files and save in file `bag_of_words` in the same directory.
```
python read_html.py
```
Then, run the following two commands to train a [GloVe model](https://github.com/maciejkula/glove-python) on the OpenSubtitles dataset

to build the corpus model `corpus.model`. 
```
python get_corpus.py
python train.py
```

