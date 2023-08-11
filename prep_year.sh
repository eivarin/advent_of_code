#!/usr/bin/zsh
if [ $# -eq 0 ]
  then
    echo "No year supplied"
    exit 1
fi
if [ -d $1 ]; then
    echo "Directory $1 exists."
    exit 1
fi

function prep_files() {
    touch silver.py
    echo "day, year, part = ($1, $2, \"a\")" >> silver.py
    cat ../../day_example.py >> silver.py
    touch gold.py
    echo "day, year, part = ($1, $2, \"b\")" >> gold.py
    cat ../../day_example.py >> gold.py
}

function make_day() {
    if [ $1 -lt 10 ]
      then
        mkdir -p day_0$1
        cd day_0$1
      else 
        mkdir -p day_$1
        cd day_$1
    fi
    prep_files $1 $2
    cd ..
}

echo "Preparing year $1"
mkdir -p $1
cd $1
for i in {1..25} ; do
    make_day $i $1
done
cd ..
echo "Done"
