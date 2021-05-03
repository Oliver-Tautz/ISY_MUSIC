## Architecture and shapes of music transcriber

# Input


* Picture = (1, 128, 1654, 1). Why (1,.,.,1)? Are other images possible?
* picture is cropped to 128 lines. columns are variable.


# Output 

* SparseTensor with shape (1,28) [(1,?)] variable series output. Why Sparse? Other shapes possible? 
* ints mapped to vocabulary -> One hot encoding? Yes!
* Semantic Vocab size = 1782


Word - >    number -> (000...1...0)  ->        (0.3 0.1 0.7 ...)        ->       ->                -> (000...1...000)


                      (vocab_size,)  ->        (?,) latent encoding     -> RNN   -> softmax+argmax?-> output
