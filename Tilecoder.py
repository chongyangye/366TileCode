numTilings = 8
    
def tilecode(x,y,tileIndices):
    # write your tilecoder here (5 lines or so)
    for i in range(numTilings):
        index=int(x/0.6)+(int(y/0.6)*11)
        x+=0.6/numTilings
        y+=0.6/numTilings
        tileIndices[i]=index+(121*i)
        
    
def printTileCoderIndices(x,y):
    tileIndices = [-1]*numTilings
    tilecode(x,y,tileIndices)
    print 'Tile indices for input (',x,',',y,') are : ', tileIndices

printTileCoderIndices(0.1,0.1)
printTileCoderIndices(4.0,2.0)
printTileCoderIndices(5.99,5.99)
printTileCoderIndices(4.0,2.1)
    
