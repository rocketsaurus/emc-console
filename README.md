# emc-console
Console testing script

<h2>Instructions - Mac</h2>
<ol>
    <li>git clone git@github.com:rocketsaurus/emc-console.git</li>
    <li>pip install -r requirements.txt</li>
    <li>chmod +x console_test.py</li>
    <li>./console_test.py -p='/dev/tty.USA19H142P1.1' -i=10</li>
</ol>

<h2>Flags</h2>
-p or --port specifies the serial port to connect to.  To check: ls /dev/tty*
-i or --iterations will set the number of times the script will repeat every second
-t or --tolerance specifies the pass/fail criteria in seconds
-v or --verbose if set will print out verbose logs

