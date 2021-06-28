# Compound Word Transformer

* main contribution is actually music embedding and not architecure?
* faster becasue embedding uses 'compund tokens', shrinking sequence length
* compound tokens are grouping of tokens by function (e.g. note = pitch+duration+velocity)
* fill up missing tokens with special token '[ignore]'

## What is x_t?

* [words] -> [[words] by 'group'. 
* specific: concat embeddings of tokens to one embedding + special embedding of 'family token' (see p.3)




## interesting citations

* "Our
experiment shows that, compared to state-of-the-art models,
the proposed model converges 5–10 times faster at training
(i.e., within a day on a single GPU with 11 GB memory)"


* "A main merit of CP is that we can customize the settings
for different token types."

* "A main proposal of our work is to use different feed-forward
heads for tokens of different types in a Transformer."


* "CP+linear is remarkably fast, taking on
average <30 seconds to complete the conditional generation
of a song."

## Links 


article : https://ailabs.tw/human-interaction/compound-word-transformer-generate-pop-piano-music-of-full-song-length/
paper : https://arxiv.org/abs/2101.02402
github: https://github.com/YatingMusic/compound-word-transformer


transformers are RNNs (linear transformer) : https://arxiv.org/abs/2006.16236
attention is all you need (transformers) video: https://www.youtube.com/watch?v=iDulhoQ2pro
