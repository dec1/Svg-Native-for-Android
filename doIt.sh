cd ./tux

./gradlew clean

./gradlew assembleRelease 

cd ..
python3 install_svg.py
