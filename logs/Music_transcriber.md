## Architecture and shapes of music transcriber

# Input


* Picture = (1, 128, 1654, 1). Why (1,.,.,1)? Are other images possible?
* picture is cropped to 128 lines. columns are variable.


# Output 

* SparseTensor with shape (1,28) [(1,?)] variable series output. Why Sparse? Other shapes possible? 
* ints mapped to vocabulary -> One hot encoding? Yes!
* Semantic Vocab size = 1782


```
Word   ->    number -> (000...1...0)     ->  CNN ->     (0.3 0.1 0.7 ...)      -> RNN  ->  (0.001 0.02 ... 0.8 ... 0.01)   -> softmax+argmax    -> (000...1...000)                     -> ...

                    
String ->   int64   ->    (vocab_size,)  ->  CNN ->   (?,) latent encoding     -> RNN  ->   p(y|x).shape=(vocab_size,)     -> softmax+argmax?   -> output.shape=(vocab_size,)          -> ...
```
