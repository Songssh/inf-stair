# Inf-stair
강화 학습을 이용한 무한의 계단 인공지능 입니다. 

## Requirements
- Python
- App player **(tested on bluestack)**

## Setup
1. Clone this repo
```sh
git clone https://github.com/Songssh/inf-stair.git
```
2. Set this repo
```
cd inf-stair
```
3. Create environment
```
# anaconda
conda create -n inf python=3.9.13
```
```
# Venv
python -m venv inf
```
4. Activate environment
```
# anaconda
activate inf
```
```
# Venv
source inf/Scripts/activate
```
5. Install python requirements
```
pip install -r requirements.txt
```

## Edit parameters
1. run **utils/get_position.py**

![](./assets/stair.png)

2. open **hparams.py** and edit
```
stair_x = 132 #
stair_y = 554 #
stair_x_len = 70 #px
stair_y_len = 30 #px
end_x = 390
end_y = 759
end_rgb = (204,  34,  34)

# 'q' 전환, 'e' 올라가기
keys = ['q', 'e']
```
3. make floating buttons

![](./assets/key.png)

## Train
[WARNING] Turn your **WIFI** off, ads might disturb your traning.
```
python train.py
```

## Run
```
python run.py
```

## Tutorial video
You can find tutorial video [here](https://youtu.be/Sm51kj2WZvc).

## Note
