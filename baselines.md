# Baseline Info 09.08.21

Great source i found: [source-seperation-tutorial](https://source-separation.github.io/tutorial/landing.html)

## Paper Links

* UMX/UMXL	[paper](https://paperswithcode.com/paper/open-unmix-a-reference-implementation-for) [github](https://github.com/sigsep/open-unmix-pytorch), published at [joss](https://joss.theoj.org/papers/10.21105/joss.01667), 2 citations on google scolar
* XUMX 		[paper](https://arxiv.org/abs/2010.04228) [github](https://github.com/asteroid-team/asteroid/tree/master/egs/musdb18/X-UMX), published at [IEEE18/ICASSP21](https://ieeexplore.ieee.org/abstract/document/9414044?casa_token=kYvsc0qH5c0AAAAA:Rn7zBhxns4RYsFWAtXlVLu0LhXwyIFPwLgotzaGYT_gGu4ZBzUucZBwrQmGM-YorAZRgucTQSmIgjQ), 2 citations on google scolar
* Demucs 	[paper](https://hal.archives-ouvertes.fr/hal-02379796/document) [github](https://github.com/facebookresearch/demucs), published only on arxiv?!, 19 citations on google scolar
* Spleeter 	[paper](http://archives.ismir.net/ismir2019/latebreaking/000036.pdf) [github](https://github.com/deezer/spleeter) [blog](https://deezer.io/releasing-spleeter-deezer-r-d-source-separation-engine-2b88985e797e), published at [joss](https://joss.theoj.org/papers/10.21105/joss.02154), 45 citations on google scolar 


## Metrics
* umx: sdr
* xumx: sdr,sar, mse on spectrogram as loss
* demucs: sdr,MOS (human evaluation scores), l1 loss
* spleeter: sdr,sir,sar,isr with umx results!
* museeval: SRD,ISR,SIR,SAR
* Other SNR

### Metrics Explained

[Evaluation metrics](https://source-separation.github.io/tutorial/basics/evaluation.html)
  * there is a cheat example here! Could have helped for competition maybe...

[SDR-half-baked or well done? (SI-SDR)](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwjrjp638ajyAhXHDewKHfv0CKoQFnoECCYQAQ&url=https%3A%2F%2Farxiv.org%2Fpdf%2F1811.02508&usg=AOvVaw1ZAGHHtHA6Ks5avOT4O7c8)


All metrics are computed per source and then averaged. They are also averaged over all samples (songs) potentionally distorting the total distribution (no stddev reported ...)
### Open questions
* What us ISR?
* How are e_interf, e_noise and e_artif computed?!
* How does the bad signal get such high sdr?
* how different are the measures? What can our model do?
* What are journals? What are conferences? What are preprints? This is confusing to me

### Datasets

[source-sep](https://source-separation.github.io/tutorial/data/datasets.html)
[sigsep](https://sigsep.github.io/datasets/)


