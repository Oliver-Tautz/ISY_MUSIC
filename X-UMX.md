# X-UMX paper summary


* Same basic architecture as UMX 
* ![pic](pics/UMX.png)
* FNN + BLSTM  + FNN per source.
* In front/after BLSTM Average input/output
* Loss functions: MDL(Multi-Domain-Loss) and CL (Combination Loss)


## MDL
* Use both, MSE between Spec and Spec_pred and wSDR between 'estimated and reference time signals' What is that?
* Predict just one domain and transform to other for loss computation 
* ![pic](UMX.png)
 
## CL
* 
