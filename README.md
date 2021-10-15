# Crack Android Pattern Lock

Tested on Android 4.4 (API 19) on Samsung Galaxy S4.

<img src="pattern.png" width="200px">

<img src="result.png" width="400px">

## Usage

1. Copy `gesture.key` file to project

```
adb pull /data/system/gesture.key
```

2. Run

```
python pattern.py gesture.key
```

## Reference

- https://github.com/sch3m4/androidpatternlock
- https://gist.github.com/hubert3/8560499
