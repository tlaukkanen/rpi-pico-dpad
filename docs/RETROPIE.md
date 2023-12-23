# Configurations for Retropie Emulationstation

```
pi@retropie:~ $ cat /opt/retropie/configs/all/emulationstation/es_input.cfg
<?xml version="1.0"?>
<inputList>
  <inputAction type="onfinish">
    <command>/opt/retropie/supplementary/emulationstation/scripts/inputconfiguration.sh</command>
  </inputAction>
  <inputConfig type="keyboard" deviceName="Keyboard" deviceGUID="-1">
    <input name="pageup" type="key" id="49" value="1"/>
    <input name="up" type="key" id="1073741906" value="1"/>
    <input name="left" type="key" id="1073741904" value="1"/>
    <input name="select" type="key" id="1073741892" value="1"/>
    <input name="leftanalogdown" type="key" id="106" value="1"/>
    <input name="leftanalogright" type="key" id="107" value="1"/>
    <input name="right" type="key" id="1073741903" value="1"/>
    <input name="leftanalogleft" type="key" id="104" value="1"/>
    <input name="pagedown" type="key" id="50" value="1"/>
    <input name="leftanalogup" type="key" id="117" value="1"/>
    <input name="y" type="key" id="49" value="1"/>
    <input name="x" type="key" id="13" value="1"/>
    <input name="down" type="key" id="1073741905" value="1"/>
    <input name="start" type="key" id="1073741882" value="1"/>
    <input name="b" type="key" id="32" value="1"/>
    <input name="a" type="key" id="97" value="1"/>
  </inputConfig>
</inputList>
```