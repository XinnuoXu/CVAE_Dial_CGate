#python translate.py -model dialogue-model_acc_37.49_ppl_34.85_e10.pt -src data/test.en -tgt data/test.vi -report_bleu -report_rouge -verbose -gpu 0

TEST_FILE="./data/"
MODEL=dialogue-model_acc_6.80_ppl_262.82_e7.pt

python translate.py -model $MODEL -src $TEST_FILE/test.en -tgt $TEST_FILE/test.vi -report_bleu -report_rouge -verbose -gpu 0
