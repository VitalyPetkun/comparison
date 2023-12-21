# Comparison of approaches

## Preface
This page aims to form an impression of the limitations 
of available approaches for automatic alignment. 
Such an analysis can only be performed on the basis of 
large volumes of labeled data, which we obviously do not have.
We limited ourselves to a small set of examples and focused 
on the maximum variability and clarity of these examples. 
The data was collected by people from the QA department 
who did not have much experience using these applications before.

### MScanner
| scanning conditions                                       | gnome                                | <-      | cleaner                                | <-      | printer                                | <-      | rabbit                                | <-      |
|-----------------------------------------------------------|--------------------------------------|---------|----------------------------------------|---------|----------------------------------------|---------|---------------------------------------|---------
| the same conditions as at the stage of creating the model | ![](src/scanner/scenario0/gnome.gif) | &check; | ![](src/scanner/scenario0/cleaner.gif) | &check; | ![](src/scanner/scenario0/printer.gif) | &check; | ![](src/scanner/scenario0/rabbit.gif) | &cross; |
| same pose, different place                                | ![](src/scanner/scenario1/gnome.gif) | &check; | ![](src/scanner/scenario1/cleaner.gif) | &check; | ![](src/scanner/scenario1/printer.gif) | &cross; | ![](src/scanner/scenario1/rabbit.gif) | &cross; |
| different pose                                            | ![](src/scanner/scenario2/gnome.gif) | &check; | ![](src/scanner/scenario2/cleaner.gif) | &check; | ![](src/scanner/scenario2/printer.gif) | &check; | ![](src/scanner/scenario2/rabbit.gif) | &check; |
| dim lighting                                              | ![](src/scanner/scenario3/gnome.gif) | &check; | ![](src/scanner/scenario3/cleaner.gif) | &check; | ![](src/scanner/scenario3/printer.gif) | &cross; | ![](src/scanner/scenario3/rabbit.gif) | &cross; |
| flash lighting                                            | ![](src/scanner/scenario4/gnome.gif) | &check; | ![](src/scanner/scenario4/cleaner.gif) | &cross; | ![](src/scanner/scenario4/printer.gif) | &cross; | ![](src/scanner/scenario4/rabbit.gif) | &cross; |
| change in appearance                                      | ![](src/scanner/scenario5/gnome.gif) | &cross; | ![](src/scanner/scenario5/cleaner.gif) | &check; | ![](src/scanner/scenario5/printer.gif) | &cross; | ![](src/scanner/scenario5/rabbit.gif) | &cross; |

This approach uses lidar to obtain information about the position of an object. 
Thus, we inherit all the problems associated with lidar, the difficult ones are:
- reflective objects
- objects paired with obscure lightning
- small objects
- geometrically simple objects.
At this stage we do not use color in order to have the greatest possible invariance to the lighting.

The approach involves two stages of scanning an object: to create an object and to recognize it.

**Summary:** This approach will work well for fairly large objects (bigger than a coffee machine) 
without 
major changes in illumination and without major changes in the appearance of the object.

### Reality Composer
| scanning conditions                                       | gnome                                 | <-      | cleaner                                 | <-      | printer                                 | <-      | rabbit                                 | <-      |
|-----------------------------------------------------------|---------------------------------------|---------|-----------------------------------------|---------|-----------------------------------------|---------|----------------------------------------|---------
| the same conditions as at the stage of creating the model | ![](src/composer/scenario0/gnome.gif) | &check; | ![](src/composer/scenario0/cleaner.gif) | &check; | ![](src/composer/scenario0/printer.gif) | &check; | ![](src/composer/scenario0/rabbit.gif) | &check; |
| same pose, different place                                | ![](src/composer/scenario1/gnome.gif) | &cross; | ![](src/composer/scenario1/cleaner.gif) | &cross; | ![](src/composer/scenario1/printer.gif) | &check; | ![](src/composer/scenario1/rabbit.gif) | &check; |
| different pose                                            | ![](src/composer/scenario2/gnome.gif) | &cross; | ![](src/composer/scenario2/cleaner.gif) | &cross; | ![](src/composer/scenario2/printer.gif) | &cross; | ![](src/composer/scenario2/rabbit.gif) | &cross; |
| dim lighting                                              | ![](src/composer/scenario3/gnome.gif) | &cross; | ![](src/composer/scenario3/cleaner.gif) | &check; | ![](src/composer/scenario3/printer.gif) | &cross; | ![](src/composer/scenario3/rabbit.gif) | &cross; |
| flash lighting                                            | ![](src/composer/scenario4/gnome.gif) | &cross; | ![](src/composer/scenario4/cleaner.gif) | &cross; | ![](src/composer/scenario4/printer.gif) | &cross; | ![](src/composer/scenario4/rabbit.gif) | &cross; |
| change in appearance                                      | ![](src/composer/scenario5/gnome.gif) | &cross; | ![](src/composer/scenario5/cleaner.gif) | &check; | ![](src/composer/scenario5/printer.gif) | &cross; | ![](src/composer/scenario5/rabbit.gif) | &cross; |

Also, given the available information about *RealityComposer*, 
we can form a set of assumptions about their approach:

- the approach is based on photographs taken during the 
creation of the model; the separation of the object 
from the scene in the process of creating the model 
occurs automatically. Therefore, major changes in 
lighting or object appearance will result in poor alignment accuracy.
 
- the approach uses a video stream from the camera for detection, 
so the scanning stage of the asset during recognition is omitted.

**Summary:** the approach is fast, does not require additional equipment, 
and is ideal for small but visually diverse objects on a flat surface. 
It will also be good to recognize objects if the environment does not 
differ from what it was during the creation of the model.


### Conclusion
Both approaches have their own set of 
applicable scenarios, and only the simplest 
cases are found at the intersection of these sets. 
*MScanner* imposes many restrictions on the objects themselves, 
while *RealityComposer* does not have any special restrictions 
on objects, but only works if there are no serious differences 
in the environment at the stages of model creation and recognition. 
On the other hand, the advantages of RealityComposer include speed and the 
absence of a 
dedicated stage of scanning the environment for recognition.