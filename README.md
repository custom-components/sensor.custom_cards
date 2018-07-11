# sensor.custom_cards

A sensor platfor that give you information of new versions of your cards.

## For now this wil ONLY work if your cards if from https://github.com/ciotlosm/custom-lovelace

## For this to work, you need to set install the component [custom_cards](https://github.com/custom-components/custom_cards) first

To get started put `/custom_components/sensor/custom_cards.py`  
here: `<config directory>/custom_components/sensor/custom_cards.py`  
  
**Example configuration.yaml:**

```yaml
sensor:
  platform: custom_cards
```

**Configuration variables:**  
  
key | description  
:--- | :---  
**platform (Required)** | The name of the sensor platform.