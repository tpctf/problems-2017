#!/bin/bash                                                 
function chr {                                              
        local c                                             
        for c                                               
        do                                                  
        printf "\\$((c/64*100+c%64/8*10+c%8))"              
        done                                                
}                                                           
for ((i=32;i < 128; i++))                                   
do                                                          
 h="$(chr $i)"                                              
 echo "$h"                                                  
 echo "$(echo -e "0\n$1$h$2\n" | ./superencrypt)"        
done
