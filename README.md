# Vis4Protocol

 This is a toy project with word2vec. We are to visualize the 5G protocols, for the purpose of finding the relationship between each protocol.  

 The part of our works is as follows:  

 1、Download 5G protocols from [here](http://www.3gpp.org/ftp/Specs/archive/38_series/).  
 2、Transform the doc file to txt file.  
 3、Remove the useless punctuations in the txt file.  
 4、Use the txt file to train word2vec model.  
 5、visulize the vectors, in which X and Y is the mean of the word vectors in the protocol, and the size of the circle is the word number of protocol.  

 An example is shown:
 ![Visualization](https://github.com/floperry/Vis4Protocol/blob/master/Figure_1.png)


2018.3.11 Update:  
    Add punctuationDelete function, for removing the punctuations in file.

    
 To be continue...