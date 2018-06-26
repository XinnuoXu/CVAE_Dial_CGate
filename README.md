# CVAE_dialogue_generator

This project is a pytorch implementation for my paper "Xu, Dusek, Konstas, Rieser. Better Conversations by Modeling, Filtering, and Optimizing for Coherence and Diversity", which sadly has been neither accpted by any conference nor put on the arxiv :(

## Requirments <br />
This code works on Python2.7

## Quickstart <br />
### Step1: Download the OpenSubtitles dataset <br />
This code is based on OpenSubtitles dataset [Automatic Turn Segmentation for Movie & TV Subtitles](http://www.diva-portal.org/smash/get/diva2:1034694/FULLTEXT01.pdf). To get the data, please contact the authors [Pierre Lison](https://github.com/plison). You should unzip the datset and name it as `opensubtitles` and put it in 
```
data/filter/
```

### Step2: Preprocess the data <br />
Run the following command in `data/filter/`
```
python read_html.py
```
After running the preprocessing, file `bag_of_words` is generated in the same directory. Then, run
```
python get_corpus.py
```
to build the corpus model `corpus.model`. 
