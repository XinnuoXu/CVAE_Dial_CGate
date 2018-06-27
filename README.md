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

### Step2: Creat datasets for generator and discriminator <br />
For the generator, a training pair consists of a dialogue context and a corresponding response. We consider three consecutive turns as the dialogue context and the following turn as the response. For the discriminator, positive examples are dialogue contexts with their following turn as the response, while negative examples are dialogue contexts with an utterance randomly sampled in the same dialogue as the response.

We use toolkit [Opensubtitles processing tool](https://github.com/WattSocialBot/movie_tools) owned by [Ondrej Dusek](https://github.com/tuetschek) to extract dialogues from OpenSubtitles dataset `data/filter/opensubtitles/`.
```
~/data/movie_tools/convert_nrno_subs.py -D -s -S train:train-dev:devel:test -r 97:1:1:1 -d all_dialogues_cased opensubtitles/ dial.jsons.txt
```
The outputs are 

* `train.dial.jsons.txt`
* `train-dev.dial.jsons.txt`
* `devel.dial.jsons.txt`
* `test.dial.jsons.txt`

as the split ratio `97:1:1:1` with format of one dialogue per line

```
["utterance 1", "utterance 2", "utterance 3"...]
```

for example,

```
["Watch out !", "Oh , what fun !", "JON :", "That was fun .", "Oh , that was great !", "Oh , time for a break ?", "Dad , I 'm hungry .", "I 'm really hungry .", "Can we eat now ?", "Keep your shirt on .", "We 'll be in Potter 's Cove in 20 minutes .", "OK , how about some pictures ?", "Here we go .", "Everybody smile .", "Say cheese ."]
```

Then, we construct the training dataset for generator and discriminator from `train.dial.jsons.txt` by running

* `python data_reading.py`

The outputs are

* `train.en` inputs of encoder in generator (dialogue contexts)
* `train.vi` outputs of decoder in generator (expacted responses)
* `train.pos` positive examples for discriminator (dialogue contexts with their following turn as the response)
* `train.neg` negative examples for discriminator (dialogue contexts with an utterance randomly sampled in the same dialogue as the response)

The format of `train.en` is `utterance1 <u2> utterance2 <u1> utterance3` in each line, for example
```
well , i 'm glad you called me . <u2> i 'm not . <u1> no , you did the right thing .
```
The format of `train.vi` is `response` in each line, for example
```
you 'll protect him , won 't you ?
```
The formats for `train.pos` and `train.neg` are the same `utterance1 <u2> utterance2 <u1> utterance3 \t response`, for example
```
pull up sooner . <u2> ok , skipper ! <u1> do you think they 'll ever get it ?	            give them a week .
```

* `python data_reading_shaffle.py train-dev` for train-dev set
* `python data_reading_shaffle.py devel` for dev set
* `python data_reading_shaffle.py test` for testing set

For 

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
