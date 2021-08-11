# Baseline Info 09.08.21

## Paper Links

* UMX/UMXL	[paper](https://paperswithcode.com/paper/open-unmix-a-reference-implementation-for) [github](https://github.com/sigsep/open-unmix-pytorch)
* XUMX 		[paper](https://arxiv.org/abs/2010.04228) [github](https://github.com/asteroid-team/asteroid/tree/master/egs/musdb18/X-UMX)
* Demucs 	[paper](https://hal.archives-ouvertes.fr/hal-02379796/document) [github](https://github.com/facebookresearch/demucs)
* Spleeter 	[paper](http://archives.ismir.net/ismir2019/latebreaking/000036.pdf) [github](https://github.com/deezer/spleeter) [blog](https://deezer.io/releasing-spleeter-deezer-r-d-source-separation-engine-2b88985e797e)


## Metrics
* umx: sdr
* xumx: sdr,sar, mse on spectrogram as loss
* demucs: sdr,MOS (human evaluation scores), l1 loss
* spleeter: sdr,sir,sar,isr with umx results!
* museeval: SRD,ISR,SIR,SAR

### Metrics Explained

All metrics are computed per source and then averaged 

#### SDR

<img src="https://render.githubusercontent.com/render/math?math=SDR_{source}=10log_10\frac{\sum_{n}(s_l(n)^2)+\sum_{n}(s_r(n)^2)}{\sum_{n}(s_l(n)-\hat{s}_l(n))^2+\sum_{n}(s_r(n)-\hat{s}_r(n))^2}">

