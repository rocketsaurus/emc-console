# emc-console
Serial port testing script

<h2>Instructions - Mac</h2>

1. ```git clone https://github.com/rocketsaurus/emc-console```
2. ```cd emc-console```
3. ```pip install -r requirements.txt```
4. ```chmod +x console_test.py```
5. ```./console_test.py -p='/dev/tty.USA19H142P1.1' -i=10```

```
$ ./console_test.py -p='/dev/tty.USA19H142P1.1' -i=10
Connection Open? True
Local time: 2019-06-18 12:34:20.346520-07:00
Server time: 2019-06-18 12:33:29-07:00
Calibrated time delay: 0:00:51.346520
Tolerance: 0:00:52.346520
Measured time: 0:00:51.362988 - Pass
Measured time: 0:00:51.379842 - Pass
Measured time: 0:00:51.397187 - Pass
Measured time: 0:00:51.412739 - Pass
Measured time: 0:00:51.428326 - Pass
Measured time: 0:00:51.448028 - Pass
Measured time: 0:00:51.464338 - Pass
Measured time: 0:00:51.480852 - Pass
Measured time: 0:00:51.499239 - Pass
Measured time: 0:00:51.515244 - Pass
```

<h2>Flags</h2>

```-p``` or ```--port``` specifies the serial port to connect to.  To check: ls /dev/tty*

```-i``` or ```--iterations``` will set the number of times the script will repeat every second

```-t``` or ```--tolerance``` specifies the pass/fail criteria in seconds

```-v``` or ```--verbose``` if set will print out verbose logs

