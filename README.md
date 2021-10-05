# _Pano_Cube_Pano_Convert_

------------------

# A. Setup

## 1. Install Python3.x (If python3 is not installed yet)

- Check is python installed?
```sh
$ python --version
$ python3 --version
```
![Alt text](https://github.com/xinccojp/Pano_Cube_Pano_Convert/blob/master/assert/python_version.png) 

=> use python3

- If not install --> Download here https://www.python.org/downloads/

## 2. Install pip3  (If pip3 is not installed yet)

- Check is pip3 installed?
```sh
$ pip3 --version
```

![Alt text](https://github.com/xinccojp/Pano_Cube_Pano_Convert/blob/master/assert/pip_version.png) 

- If not install --> try below
```sh
$ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
$ python3 get-pip.py
```

## 3. Install pakages from requirement.txt 
```sh
$ cd /Path/Project
$ pip3 install -r requirements.txt
```

## 4. Run
```sh
$ cd /Path/Project
$ python3 pano_cube_main.py
```
![Alt text](https://github.com/xinccojp/Pano_Cube_Pano_Convert/blob/master/assert/mode1_window.png) 


------------------

# B. Running

## 1. Choose open_folder, save_folder and mask_image by press "open, save, mask"

- After choose_open folder, it will automatically load all images name in that folder and list them in the right_List.

![Alt text](https://github.com/xinccojp/Pano_Cube_Pano_Convert/blob/master/assert/mode1_window.png)

## 2. Mode 1 : Pano -> Cube

- Click to any item from right_List

![Alt text](https://github.com/xinccojp/Pano_Cube_Pano_Convert/blob/master/assert/mode1_click.png) 

- Press Run and wait (4~7s)

![Alt text](https://github.com/xinccojp/Pano_Cube_Pano_Convert/blob/master/assert/mode1_result.png) 

- Show only cube image

![Alt text](https://github.com/xinccojp/Pano_Cube_Pano_Convert/blob/master/assert/mode1_cube_mode.png)

![Alt text](https://github.com/xinccojp/Pano_Cube_Pano_Convert/blob/master/assert/mode1_cube_only.png) 

## 3. Mode 2 : Pano -> Cube -> Pano

- Press "Mode 1", it will change to "Mode 2"

![Alt text](https://github.com/xinccojp/Pano_Cube_Pano_Convert/blob/master/assert/mode2_click.png) 

- Choose image, press Run and wait (4~6s)

![Alt text](https://github.com/xinccojp/Pano_Cube_Pano_Convert/blob/master/assert/mode2_result.png) 

## 4. Result

- After press Run or Run_all, all listed images in the right_List will be processed and then output images will be saved in save_folder.

--------

# License


