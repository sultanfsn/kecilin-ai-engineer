# Bakuten Shoot Corp Beyblade Battle Analytics
- [How To Run](<#how-to-run>)

 Bakuten Shoot Corop Beyblade Analytics is a program intended for Kecilin take home assignment. This program has the ability to detect Beyblades. This repository demonstrate how to deploy that program and return the output path.

 ## How To Run
 This program is very simple to run. Set the input image name and run it.

 Run the program
 ```
>docker build -t <username/containername:version> .
 ```

 ```
 docker run --mount source=<shared-volume-mount>,target=/app/output <docker image> <input image>
 ```
 The return should be the path of inferenced image, example:
 /app/output/3243.jpg

 Your result will be stored in output folder. It will generate an image of the inference with random naming.