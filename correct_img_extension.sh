for f in *; do 
    type=$(file -0 -F" " "$f" | grep -aPo '\0\s*\K\S+') 
    mv "$f" "${f%%.*}.${type,,}"  
done
