# This is so that I do not loss my mind :D


## External -> Kafka Produces
1. NEW_TASK

## Internal

    METADATA COLLECTOR
        Consumes :->
            1. NEW_TASK
        
        Produces :->
            1. META_DATA
    
    METADATA PROCESSER
        Consumes :->
            1. META_DATA
        
        Produces :->
            1. DATA_TASK

    METADATA DISPATCHER
        Consumes :->
             1. DATA_TASK
        
        Produces :->
            1. INFLUENTIAL_TASK
            2. BULK_TASK
    
    TINY BERT
        Consumes :->
            1. INFLUENTIAL_TASK
        
        Produces :->
            1. COMPLETED_INFLUENTIAL_TASK

    XGBOOST (2 Containers)
        Consumes :->
            1. BULK_TASK

        Produces :->
            1. COMPLETED_BULK_TASK
    
    INFLUENTIAL RESULT
        Consumes :->
            1. COMPLETED_INFLUENTIAL_TASK
        
        Sets it on the Database Table Influential :)

    XGBOOST RESULT
        Consumes :->
            1. COMPLETED_BULK_TASK
        
        Sets it on the Database Table Bulk :)
        

