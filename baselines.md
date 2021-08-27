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

### Publishing opportunities 

* JOSS: 
    * umx,spleeter was published here
    * we need to be open source
    * it needs to be "research apllicaple"?
    * we need to be a*main contributor of the software
    * "Your paper must not focus on new research results accomplished with the software." ...
    *  no deadline i think
    *  [details](https://joss.readthedocs.io/en/latest/submitting.html)
    * seems unlikely to get accepted

* ICASSP 22:
    * XUMX was published here 
    * paper submission deadline is **01.10**
    * some deadline already passed, dont know if important
    * [details](https://2022.ieeeicassp.org/call_for_papers.php)
    * this seems like a good possibility

* IEEE COGMI 21
    * paper citing xumx was published here
    * broader scope ("general ai")
    * deadline **30.09** for round 2, round 1 already finished. 
    * [details](http://www.sis.pitt.edu/lersais/conference/cogmi/2021/calls.html)
    * explicitely call for "We invite original research papers that have not been previously published and are not currently under review for publication elsewhere."
    * I cant find someone to email to, but i can open a submission.

* IEEE Signal Processing Society
    * journal, so no dealine i think?
    * seems to have pretty high standard
    * [special issue deadlines](https://signalprocessingsociety.org/publications-resources/special-issue-deadlines)
    * [details](https://signalprocessingsociety.org/publications-resources/submit-manuscript)

* RSP Science Hub
    * journal so no deadline i think?  
    * metapaper about spleeter was published here
    * Not sure if suitable
    * [details](https://www.rspsciencehub.com/journal/authors.note)


* WASPAA 22
    * cant find infos/if it even exists
    * last time deadline was 28.04.21. So maybe next year the same?
    * [details](https://www.waspaa.com/call-for-papers/)


## Baseline performance
I think both run on cpu :(!

* UMX:
 * 4 models 34M each =  **132M**
 * ~4.3s/s demixing on cpu
 * ~?s/s demixing on gpu

* Demucs
 * 1 model **570M**
 * ~2.3s/s 
 * ~15.4s/s demixing on gpu
